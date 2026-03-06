#!/usr/bin/env python3
"""
build-hackathon.py — Static site generator for the Grassroots Hoppers hackathon.

Reads markdown files from docs/devlog/, converts them to HTML,
and outputs static pages into website/hackathon/.

Usage:
    python3 scripts/build-hackathon.py

Markdown files must have YAML-like frontmatter:
    ---
    title: "Day Title"
    date: 2026-03-10
    day: 1
    status: draft|live|done
    hero_image: optional-path.png
    shipped: ["item1", "item2"]
    ---

Status meanings:
    draft  — kept in markdown only, not published or linked
    live   — currently active day
    done   — completed day
"""

import os
import re
import json
from datetime import datetime
from pathlib import Path

try:
    import markdown
except ImportError:
    print("Error: 'markdown' package required. Install with: pip install markdown --break-system-packages")
    exit(1)

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parent.parent
DEVLOG_DIR = ROOT / "docs" / "devlog"
OUTPUT_DIR = ROOT / "website" / "hackathon"
ENTRY_PAGE = ROOT / "website" / "hackathon.html"
TEMPLATE_DIR = ROOT / "scripts" / "templates"

# ---------------------------------------------------------------------------
# Frontmatter parser (no PyYAML dependency)
# ---------------------------------------------------------------------------
def parse_frontmatter(text):
    """Parse simple YAML frontmatter from markdown text."""
    meta = {}
    content = text

    match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', text, re.DOTALL)
    if not match:
        return meta, content

    fm_text, content = match.group(1), match.group(2)

    for line in fm_text.split('\n'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        m = re.match(r'^(\w+)\s*:\s*(.*)$', line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            # Remove quotes
            if val.startswith('"') and val.endswith('"'):
                val = val[1:-1]
            elif val.startswith("'") and val.endswith("'"):
                val = val[1:-1]
            # Parse arrays
            if val.startswith('[') and val.endswith(']'):
                try:
                    val = json.loads(val)
                except json.JSONDecodeError:
                    val = [v.strip().strip('"').strip("'") for v in val[1:-1].split(',') if v.strip()]
            # Parse booleans/numbers
            elif val.lower() == 'true':
                val = True
            elif val.lower() == 'false':
                val = False
            elif val == '':
                val = None
            else:
                try:
                    val = int(val)
                except ValueError:
                    pass
            meta[key] = val

    return meta, content


# ---------------------------------------------------------------------------
# Markdown → HTML
# ---------------------------------------------------------------------------
def md_to_html(text):
    """Convert markdown to HTML with common extensions."""
    return markdown.markdown(text, extensions=['fenced_code', 'tables', 'toc'])


# ---------------------------------------------------------------------------
# Template loading
# ---------------------------------------------------------------------------
def load_template(name):
    """Load an HTML template from the templates directory."""
    path = TEMPLATE_DIR / f"{name}.html"
    if not path.exists():
        print(f"  Warning: Template {path} not found, using fallback")
        return None
    return path.read_text(encoding='utf-8')


def render_template(template, **kwargs):
    """Simple {{variable}} replacement in templates."""
    result = template
    for key, val in kwargs.items():
        result = result.replace('{{' + key + '}}', str(val) if val is not None else '')
    return result


# ---------------------------------------------------------------------------
# Page builders
# ---------------------------------------------------------------------------
def is_public(status):
    """Return True when a page should be published."""
    return status in ('live', 'done')


def public_day_numbers(all_days):
    """Return day numbers that should be linked and generated."""
    return [
        d for d in sorted(k for k in all_days if isinstance(k, int))
        if is_public(all_days[d].get('status', 'draft'))
    ]


def validate_statuses(all_days, retro_meta):
    """Ensure only one entry is marked live at a time."""
    live_entries = [
        f"day-{day_num}" for day_num, meta in all_days.items()
        if isinstance(day_num, int) and meta.get('status') == 'live'
    ]
    if retro_meta.get('status') == 'live':
        live_entries.append('retrospective')

    if len(live_entries) > 1:
        raise SystemExit(
            "Error: only one entry can be marked live at a time. "
            f"Found: {', '.join(live_entries)}"
        )


def has_public_content(all_days, retro_meta):
    """Return True when any hackathon page should be publicly exposed."""
    return bool(public_day_numbers(all_days)) or is_public(retro_meta.get('status', 'draft'))


def build_day_page(meta, content_html, all_days):
    """Build a single day page."""
    template = load_template('day')
    if not template:
        return None

    day_num = meta.get('day', 0)
    title = meta.get('title', f'Day {day_num}')
    date = meta.get('date', '')
    status = meta.get('status', 'draft')
    hero_image = meta.get('hero_image')
    shipped = meta.get('shipped', [])

    # Status badge
    status_class = {'draft': 'upcoming', 'live': 'live', 'done': 'done'}.get(status, 'upcoming')
    status_label = {'draft': 'Draft', 'live': 'Live', 'done': 'Completed'}.get(status, 'Draft')

    # Shipped items
    shipped_html = ''
    if shipped and isinstance(shipped, list) and any(shipped):
        items = ''.join(f'<li>{item}</li>' for item in shipped)
        shipped_html = f'<div class="shipped-list"><h4>Shipped today</h4><ul>{items}</ul></div>'

    # Hero image
    hero_html = ''
    if hero_image:
        hero_html = f'<div class="hero-image"><img src="{hero_image}" alt="Day {day_num} hero"></div>'

    public_days = public_day_numbers(all_days)
    current_index = public_days.index(day_num) if day_num in public_days else -1

    # Navigation (prev/next)
    prev_link = ''
    next_link = ''
    if current_index > 0:
        prev_day = public_days[current_index - 1]
        prev_link = f'<a href="day-{prev_day}.html" class="nav-arrow">&larr; Day {prev_day}</a>'
    else:
        prev_link = '<span></span>'

    if 0 <= current_index < len(public_days) - 1:
        next_day = public_days[current_index + 1]
        next_link = f'<a href="day-{next_day}.html" class="nav-arrow">Day {next_day} &rarr;</a>'
    elif current_index >= 0:
        retro_meta = all_days.get('retrospective', {})
        if is_public(retro_meta.get('status', 'draft')):
            next_link = f'<a href="retrospective.html" class="nav-arrow">Retrospective &rarr;</a>'
        else:
            next_link = '<span></span>'
    else:
        next_link = '<span></span>'

    # Day indicator dots
    dots_html = ''
    for d in public_days:
        active = 'active' if d == day_num else ''
        d_meta = all_days.get(d, {})
        d_status = d_meta.get('status', 'draft')
        dot_class = f'dot {active} {d_status}'
        dots_html += f'<a href="day-{d}.html" class="{dot_class}">{d}</a>'

    # Format date nicely
    date_str = str(date)
    try:
        dt = datetime.strptime(date_str, '%Y-%m-%d')
        date_formatted = dt.strftime('%A, %B %d')
    except (ValueError, TypeError):
        date_formatted = date_str

    return render_template(template,
        title=title,
        day=str(day_num),
        date=date_formatted,
        date_iso=date_str,
        status_class=status_class,
        status_label=status_label,
        hero_html=hero_html,
        shipped_html=shipped_html,
        content=content_html,
        prev_link=prev_link,
        next_link=next_link,
        dots=dots_html,
    )


def build_retrospective(meta, content_html):
    """Build the retrospective page."""
    template = load_template('retrospective')
    if not template:
        return None

    status = meta.get('status', 'draft')
    status_class = {'draft': 'upcoming', 'live': 'live', 'done': 'done'}.get(status, 'upcoming')
    status_label = {'draft': 'Draft', 'live': 'Live', 'done': 'Published'}.get(status, 'Draft')

    return render_template(template,
        status_class=status_class,
        status_label=status_label,
        content=content_html,
    )


def build_entry_page(all_days, retro_meta):
    """Build the stable public hackathon route."""
    if has_public_content(all_days, retro_meta):
        return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="0; url=hackathon/index.html">
    <title>Redirecting to Hackathon...</title>
</head>
<body>
    <p>Redirecting to <a href="hackathon/index.html">hackathon/index.html</a>...</p>
</body>
</html>
"""

    return load_template('preview')


def build_index(all_days, retro_meta):
    """Build the hackathon index/landing page."""
    if not has_public_content(all_days, retro_meta):
        return None

    template = load_template('index')
    if not template:
        return None

    # Build timeline entries
    timeline_html = ''
    latest_day = 0
    for d in public_day_numbers(all_days):
        meta = all_days.get(d, {})
        title = meta.get('title', f'Day {d}')
        date = str(meta.get('date', ''))
        status = meta.get('status', 'draft')
        shipped = meta.get('shipped', [])

        try:
            dt = datetime.strptime(date, '%Y-%m-%d')
            date_formatted = dt.strftime('%A, %B %d')
        except (ValueError, TypeError):
            date_formatted = date

        status_class = {'draft': '', 'live': 'active', 'done': 'done'}.get(status, '')

        shipped_html = ''
        if shipped and isinstance(shipped, list) and any(shipped):
            items = ''.join(f'<span class="badge">{item}</span>' for item in shipped)
            shipped_html = f'<div class="shipped-badges">{items}</div>'

        latest_day = d

        timeline_html += f'''
            <div class="day-entry {status_class}" id="day-{d}">
                <div class="day-dot"></div>
                <div class="day-label">{date_formatted} &mdash; Day {d}</div>
                <div class="day-title"><a href="day-{d}.html">{title}</a></div>
                {shipped_html}
            </div>'''

    # Progress
    day_metas = [meta for key, meta in all_days.items() if isinstance(key, int)]
    done_count = sum(1 for meta in day_metas if meta.get('status') == 'done')
    live_count = sum(1 for meta in day_metas if meta.get('status') == 'live')
    progress = int(((done_count + live_count * 0.5) / 5) * 100) if all_days else 0

    # Latest card
    latest_html = ''
    if latest_day > 0:
        lm = all_days[latest_day]
        lt = lm.get('title', f'Day {latest_day}')
        ls = lm.get('status', 'draft')
        badge = 'Live now' if ls == 'live' else 'Latest'
        latest_html = f'''
        <div class="latest-card">
            <span class="latest-badge">{badge}</span>
            <h3><a href="day-{latest_day}.html">Day {latest_day}: {lt}</a></h3>
            <p class="card-link"><a href="day-{latest_day}.html" class="accent">Read day {latest_day} &rarr;</a></p>
        </div>'''

    # Retro link
    retro_status = retro_meta.get('status', 'draft')
    retro_html = ''
    if is_public(retro_status):
        retro_html = '<p style="margin-top: 1.5rem;"><a href="retrospective.html" class="accent" style="font-family: var(--mono); font-size: 0.95rem;">Read the retrospective &rarr;</a></p>'
    else:
        retro_html = '<p style="margin-top: 1.5rem; font-family: var(--mono); font-size: 0.85rem; opacity: 0.5;">Retrospective publishes after Day 5.</p>'

    return render_template(template,
        timeline=timeline_html,
        progress=str(progress),
        latest_card=latest_html,
        retrospective_link=retro_html,
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print(f"Building hackathon pages...")
    print(f"  Source: {DEVLOG_DIR}")
    print(f"  Output: {OUTPUT_DIR}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for stale_name in [*(f"day-{d}.html" for d in range(1, 6)), "retrospective.html", "index.html"]:
        stale_path = OUTPUT_DIR / stale_name
        if stale_path.exists():
            stale_path.unlink()

    # Read all day files
    all_days = {}
    day_contents = {}

    for d in range(1, 6):
        path = DEVLOG_DIR / f"day-{d}.md"
        if path.exists():
            text = path.read_text(encoding='utf-8')
            meta, content = parse_frontmatter(text)
            all_days[d] = meta
            day_contents[d] = content
            print(f"  Read day-{d}.md: \"{meta.get('title', '?')}\" [{meta.get('status', 'draft')}]")
        else:
            print(f"  Skipped day-{d}.md (not found)")

    # Read retrospective
    retro_path = DEVLOG_DIR / "retrospective.md"
    retro_meta = {}
    retro_content = ''
    if retro_path.exists():
        text = retro_path.read_text(encoding='utf-8')
        retro_meta, retro_content = parse_frontmatter(text)
        print(f"  Read retrospective.md [{retro_meta.get('status', 'draft')}]")
    all_days['retrospective'] = retro_meta
    validate_statuses(all_days, retro_meta)

    # Build day pages
    for d, content in day_contents.items():
        if not is_public(all_days[d].get('status', 'draft')):
            print(f"  Skipped day-{d}.html (draft)")
            continue
        content_html = md_to_html(content)
        page_html = build_day_page(all_days[d], content_html, all_days)
        if page_html:
            out_path = OUTPUT_DIR / f"day-{d}.html"
            out_path.write_text(page_html, encoding='utf-8')
            print(f"  Built day-{d}.html")

    # Build retrospective
    if retro_content and is_public(retro_meta.get('status', 'draft')):
        retro_html = build_retrospective(retro_meta, md_to_html(retro_content))
        if retro_html:
            (OUTPUT_DIR / "retrospective.html").write_text(retro_html, encoding='utf-8')
            print(f"  Built retrospective.html")
    elif retro_content:
        print(f"  Skipped retrospective.html (draft)")

    entry_html = build_entry_page(all_days, retro_meta)
    if entry_html:
        ENTRY_PAGE.write_text(entry_html, encoding='utf-8')
        print(f"  Built {ENTRY_PAGE.name}")

    # Build index
    index_html = build_index(all_days, retro_meta)
    if index_html:
        (OUTPUT_DIR / "index.html").write_text(index_html, encoding='utf-8')
        print(f"  Built index.html")
    else:
        print(f"  Skipped index.html (no public content)")

    page_count = len(public_day_numbers(all_days)) + (1 if is_public(retro_meta.get('status', 'draft')) else 0) + (1 if index_html else 0)
    print(f"Done. {page_count} pages generated.")


if __name__ == '__main__':
    main()
