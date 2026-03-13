# Dev Log Rewrite — Design Doc

**Date:** 2026-03-13
**Status:** Draft — awaiting annotation

---

## The problem

The current dev logs (days 1-3) read like engineering postmortems. Day 2 is 228 lines. Day 3 is 238 lines. The narrative moments — the stock lie, the €207K revenue mistake, losing an afternoon to rabbit holes while sick — are buried under phase breakdowns, importer tables, and Gold builder schemas.

The audience isn't engineers picking up the codebase. The audience is friends, enthusiasts, and a potential tech co-founder. The logs need to be honest, readable, and tell a story — not document a pipeline.

Day 4 is already good. It's written as a diary entry, not a status report. The other days need to match that voice.

Day 5 doesn't exist yet.

---

## Audience

**Primary:** A potential tech co-founder. Someone technical who's reading between the lines for: "Is this person serious? Do they have taste? Do they know what they don't know? Would I want to build with them?"

**Secondary:** Friends and movement enthusiasts. People following the Grassroot Hopper story who want to see the real thing, not a polished pitch.

**What the audience cares about:** Honesty, self-awareness, the emotional arc, the moments where reality broke the plan. NOT: which files were committed, how many Silver importers were built, what verification checks pass.

---

## The vibe coding curve

The central metaphor for the entire series. A graph of progress vs. time:

```
Progress
  ▲
  │          ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  (plateau)
  │       ·
  │     ·
  │   ·
  │  ·
  │ ·
  │·
  └──────────────────────────────────────────────────► Time
  Day 1    Day 2    Day 3    Day 4    Day 5
```

Days 1-3: steep climb. Massive output from vibe coding with AI. Day 4: flatline. Hours in, zero code shipped. Day 5: small bump (bug fixes, closing) but the curve stays flat.

This isn't unique to this hackathon. It's a pattern: vibe coding games show it (playable in 3 days, then weeks grinding on balance and broken features). What works in vibe coding works straight away. What doesn't takes ages to fix.

The graph is a real visual asset — embedded in the published dev logs, referenced across multiple days.

### The voices from the discourse

Two screenshots captured during the hackathon (in `docs/devlog/`) anchor this in the broader conversation:

- **Uncle Bob Martin:** "For all the hype and hullabaloo about AI and vibe coding; this is not a layman's domain. The engineering bar is going way up."
- **Craig Weiss:** "If you want to survive in the age of vibe coding, you need to become an expert in system design, architecture & product design. The highest ROI has moved up the stack."
- **Ben Dickson:** "The biggest winners of AI-assisted coding and vibe coding will be people who have actual experience writing real code and building software pre-AI era."

These voices say the bar is going up. Julien's hackathon is the lived case study.

### The Grassroot Hopper insight

The curve has a predictable shape. If you can know in advance where the plateau hits, you can design products that ship before crossing it.

This requires: design sense, deep understanding of what AI is good at vs bad at, and the discipline to scope ruthlessly. The Grassroot Hopper position is NOT on the edge of software engineering — it's on the edge of what everyday people can build with open-source tools. Leading the vibe coders and hobbyists.

A tech co-founder's role: provide "beyond the edge" insight. They can see where things will break before you hit the wall. They extend the sweet spot. They're the radar that lets you stay on the edge instead of falling off it.

---

## Voice and format

**Voice:** Diary format. No template. Each day reads like Day 4 already does — honest journal entries. What happened, how it felt, what was learned. Stream of consciousness with editorial polish.

**Tone benchmark:** Day 4's "The Wall" section. Personal, specific, no jargon for jargon's sake. Technical terms only when they serve the story (e.g., "the stock field turned out to be fiction" — not "the STOCK column in the Bronze-layer POS export CSV contained cumulative sold units from an initial value of zero").

**Length:** 60-80 lines per day. Days 1-3 cut from 200+ lines. Day 4 stays roughly as-is (~110 lines — it earns its length). Day 5 written fresh.

---

## What gets kept from each day

### Day 1 — "The Sun Is Out" (or similar)

**Keep:**
- The opening image: laptop in the sun, beautiful day, mixing phone + laptop + Cursor
- The brainstorm framing: what this hackathon is and what it's NOT
- The feeling of "I'm actually doing this"
- The phase gate decision: no dashboard until we have real data

**Cut:**
- Repo bootstrap details (5 commits list)
- Dashboard coherence research details
- Pencil design exploration
- All file paths, commit counts, export specifications
- The "What's next" detailed task list

### Day 2 — "The Data Day"

**Keep:**
- The morning at the POS terminal, exporting everything (the archaeology metaphor)
- "24 CSV files. CP1252 encoding. The usual Belgian POS mess." (one line, not a 7-type inventory)
- The stock lie — the most important discovery. Built on fiction.
- The brainstorming pivot: "Is this actually useful? Not yet."
- The reframe from ordering tool to intelligence tool

**Cut:**
- Full data inventory (7 file types, row counts, column details)
- Medallion Architecture explanation and diagram
- "21 tasks in 25 minutes" phase breakdown
- Silver importer details (6 importers, what each handles)
- Gold builder table
- Category cleanup numbers
- Supplier normalization details
- "By the numbers" table

### Day 3 — "The Cracks"

**Keep:**
- The morning Q&A: questioning whether the AI actually understands the shop
- The revenue discrepancy: €207K vs €501K — the number was wrong by 2.4x
- The lost afternoon: three honest lessons (email sorting failure, OpenClaw rabbit hole, being sick)
- "The fix was simple and painful: work until 21h"
- The Perplexity discovery as a workflow insight
- The admission that excitement was fading by end of day

**Cut:**
- Pipeline first run details
- Master Config implementation details
- Verification checks list
- Dashboard V2 build breakdown (7 phases, config layer, build-demo expansion)
- "By the numbers" table
- Category YoY/FRAIS technical details

### Day 4 — "The Wall"

**Keep:** Almost everything. This is the emotional core.
- "The wall is the point where the complexity of what exists exceeds the maintainer's ability to reason about it"
- The vibe coding analysis (enhanced with Uncle Bob / Craig Weiss voices)
- The specific debt section (lightly trimmed)
- "That's not nothing. But it's not a hackathon win."
- Options A and B
- The deeper lesson

**Add:**
- The vibe coding curve graph
- The Uncle Bob / Craig Weiss quotes as context

**Trim slightly:**
- The three specific debt examples could be shortened to one representative example

### Day 5 — "v0.1" (written fresh)

**The beats:**
1. Opening: this is closing day, not building day
2. What v0.1 actually is: a working retail intelligence dashboard built in 5 days by a non-engineer between shop shifts. What works, what doesn't. Brief.
3. The vibe coding curve realized: looking back at the 5 days with the graph in hand. Where the progress was, where it stalled, what that means.
4. The Grassroot Hopper insight: the curve is predictable. Design products that ship before the plateau. This is the new skill — not engineering, but knowing where the boundary is.
5. The co-founder gap: not "I need someone to write code for me" but "I need someone who can see beyond the edge, so I can stay on it." The radar.
6. Close: what the foundation looks like, what happens next, and an honest invitation.

**No retrospective page.** Day 5 IS the retrospective.

---

## Technical details — where they go

The `DEV_LOG_DAY*.md` files stay in the repo as-is. They're the technical reference for anyone who wants implementation details.

Each rewritten `day-*.md` file includes a note at the bottom:

> *Full technical log: [DEV_LOG_DAY2.md](DEV_LOG_DAY2.md)*

This gives depth without cluttering the story.

---

## Publishing

The `day-*.md` files feed the website generator via `scripts/build-hackathon.py`. The frontmatter (`title`, `date`, `day`, `status`, `hero_image`, `shipped`) stays functional. The `shipped` field populates the badges on the hackathon index page — those stay as compact summaries.

The vibe coding curve graph needs to be created as an image asset in `website/hackathon/media/` for embedding.

The Uncle Bob / Craig Weiss screenshots get renamed from "Capture d'écran..." to something web-safe and moved to `website/hackathon/media/`.

Status fields update:
- Days 1-5: `status: done`
- Retrospective: `status: cancelled` (merged into Day 5)

---

## What this design does NOT cover

- Rewriting the hackathon index page (`website/hackathon/index.html`) — the current page links to day pages and shows badges. That structure still works.
- Changing the build/publish pipeline.
- Editing the `DEV_LOG_DAY*.md` files.
- Creating new day pages for days 4 and 5 in `website/hackathon/`.

Those are implementation concerns for the plan phase.

---

## Open questions

1. **Day titles** — Working titles above. Final titles during implementation.
2. **The graph** — Hand-drawn feel? Clean SVG? ASCII art in markdown + rendered image for HTML? Recommend: simple SVG, minimal, dark background matching the site theme.
3. **The screenshots** — Embed directly or quote the text? Recommend: quote the text with attribution, screenshots as optional visual.
