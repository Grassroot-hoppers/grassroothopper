# Dev Log Rewrite — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Rewrite all 5 hackathon dev logs from engineering postmortems to honest diary-style entries, write Day 5 fresh, and publish all days to the website.

**Architecture:** The `day-*.md` source files in `docs/devlog/` get rewritten. The `DEV_LOG_DAY*.md` files stay untouched as technical reference. The build pipeline (`scripts/build-hackathon.py`) and templates stay unchanged. Placeholder graph images go into `website/hackathon/media/`. Screenshots get renamed to web-safe paths.

**Design doc:** `docs/plans/2026-03-13-devlog-rewrite-design.md`

---

## Task 1: Rename screenshot files to web-safe paths

**Files:**
- Move: `docs/devlog/Capture d'écran 2026-03-13 à 14.58.37.png` → `website/hackathon/media/uncle-bob-vibe-coding.png`
- Move: `docs/devlog/Capture d'écran 2026-03-13 à 14.59.36.png` → `website/hackathon/media/craig-weiss-vibe-coding.png`

**Step 1:** Move the files

```bash
cd docs/devlog
cp Capture*.58.37.png ../../website/hackathon/media/uncle-bob-vibe-coding.png
cp Capture*.59.36.png ../../website/hackathon/media/craig-weiss-vibe-coding.png
```

**Step 2:** Verify

```bash
ls -la website/hackathon/media/uncle-bob-vibe-coding.png
ls -la website/hackathon/media/craig-weiss-vibe-coding.png
```

**Step 3:** Commit

```bash
git add website/hackathon/media/uncle-bob-vibe-coding.png website/hackathon/media/craig-weiss-vibe-coding.png
git commit -m "add vibe coding discourse screenshots with web-safe names"
```

---

## Task 2: Create placeholder graph images

Perplexity will provide the final graph assets later. For now, create simple placeholder images so the markdown can reference them and the pipeline doesn't break.

**Files:**
- Create: `website/hackathon/media/vibe-coding-three-curves.png` (placeholder)
- Create: `website/hackathon/media/vibe-coding-flow-debt.png` (placeholder)
- Create: `website/hackathon/media/vibe-coding-productivity-rate.png` (placeholder)

**Step 1:** Create minimal placeholder SVGs converted to PNG (or just use the ASCII art graphs from the design doc rendered as images). For now, a simple text-based placeholder is fine — these will be swapped for Perplexity-generated graphs.

**Step 2:** Commit

```bash
git add website/hackathon/media/vibe-coding-*.png
git commit -m "add placeholder graph images for vibe coding curve thesis"
```

---

## Task 3: Rewrite Day 1

**Files:**
- Modify: `docs/devlog/day-1.md`
- Reference (read-only): current `day-1.md` for source material

**Voice:** Diary format. Day 4's "The Wall" is the tone benchmark. First person, honest, no jargon for jargon's sake.

**Target length:** ~60-70 lines of markdown (down from ~103)

**Frontmatter stays functional:**
```yaml
---
title: "The Sun Is Out"
date: 2026-03-09
day: 1
status: done
hero_image: media/day-1-screenshot.png
shipped: ["Repo bootstrap", "Excel-to-dashboard workflow", "Dashboard coherence research"]
---
```

**What to keep (narrative beats):**
1. Opening image: laptop in the sun, beautiful day, mixing phone + laptop + Cursor
2. The brainstorm framing: what this hackathon is (v0.1 intelligence demo) and what it's NOT (don't drift into production, don't pretend it's live, don't widen scope)
3. The feeling of momentum — repo went from nothing to contributor-ready scaffolding
4. The Excel-to-dashboard workflow discovery — sitting with the data, realizing how messy POS exports are
5. The phase gate decision: no dashboard wiring until one real export proves the file format
6. The design direction shift: warm artisanal palette is out, users are 26-27 year olds who want modern and sharp
7. End on anticipation: tomorrow is the data day

**What to cut entirely:**
- Repo bootstrap 5-commit list
- Dashboard coherence research details (signal hierarchy, Notion/codebase/Pencil comparison)
- Pencil design exploration details
- All file paths, commit counts, export specifications
- The detailed "What's next" task list — replace with one sentence
- The video/timelapse embed HTML (keep hero image only)

**Bottom of page:** Add link to full technical log:

```markdown
---

*Full technical log: [DEV_LOG_DAY1.md](../docs/devlog/2026-03-09-day-1.md)*
```

Note: There's no `DEV_LOG_DAY1.md` file. Link to the date-prefixed version `2026-03-09-day-1.md` if it has technical content, or skip the link if it's just a stub.

**Step 1:** Read current `day-1.md` and `2026-03-09-day-1.md` for source material

**Step 2:** Write the rewritten `day-1.md` following the beats above, diary voice, ~60-70 lines

**Step 3:** Verify frontmatter is valid for the build pipeline

**Step 4:** Commit

```bash
git add docs/devlog/day-1.md
git commit -m "rewrite day 1 log: diary voice, narrative focus"
```

---

## Task 4: Rewrite Day 2

**Files:**
- Modify: `docs/devlog/day-2.md`
- Reference (read-only): current `day-2.md`, `DEV_LOG_DAY2.md`

**Target length:** ~60-80 lines (down from ~228)

**Frontmatter:**
```yaml
---
title: "The Data Day"
date: 2026-03-10
day: 2
status: done
hero_image: media/day-2-brainstorming.png
shipped: ["24 POS exports", "Data pipeline", "Alpha dashboard", "The stock lie"]
---
```

**What to keep (narrative beats):**
1. Morning at the POS terminal — the archaeology metaphor. Sitting at the machine, exporting everything.
2. "24 CSV files. CP1252 encoding, semicolons, European decimal commas. The usual Belgian POS mess." (one line, evocative, not an inventory)
3. The pipeline design decision — briefly. Don't explain Medallion Architecture in detail. Just: "The data isn't for one dashboard. It's for everything that comes after. So we built layers: raw truth, cleaned truth, computed truth." Three sentences max.
4. The speed: 21 tasks in 25 minutes, 15 commits in 24 minutes. Mention the speed as a FEELING, not as a project management artifact. This is the steep part of the vibe coding curve.
5. **The stock lie** — THE discovery. The STOCK field isn't current inventory, it's cumulative sold units. The ordering confidence framework is built on fiction. This is the emotional center of Day 2.
6. The reframe: dashboard can't be an ordering tool. It becomes an intelligence tool. What it can honestly do.
7. The brainstorming pivot: "Is this actually useful? Not yet." The honest question.
8. First hint toward the curve — a sentence about how fast everything moved, how it felt like the hard part was over. (Foreshadowing the plateau.)

**What to cut entirely:**
- Full data inventory (7 types, row counts, column details)
- Medallion Architecture diagram and explanation
- Phase breakdown (Phases 1-5)
- Silver importer details (6 importers, what each handles)
- Gold builder table (7 files)
- Category cleanup numbers
- Supplier normalization details
- "By the numbers" table
- The alpha ships details (app.js rewrite, HTML rebuild, etc.)

**Step 1:** Read current `day-2.md` for source material
**Step 2:** Write rewritten version, diary voice, ~60-80 lines
**Step 3:** Commit

```bash
git add docs/devlog/day-2.md
git commit -m "rewrite day 2 log: the stock lie, the speed, the pivot"
```

---

## Task 5: Rewrite Day 3

**Files:**
- Modify: `docs/devlog/day-3.md`
- Reference (read-only): current `day-3.md`

**Target length:** ~70-80 lines (down from ~238)

**Frontmatter:**
```yaml
---
title: "The Cracks"
date: 2026-03-11
day: 3
status: done
hero_image:
shipped: ["Pipeline end-to-end", "Revenue fix €207K → €501K", "Dashboard V2", "Perplexity workflow"]
---
```

**What to keep (narrative beats):**
1. Morning: questioning the AI. 45-minute Q&A to probe if the AI understands the shop or is pattern-matching. It got most things right — the gaps became the work items.
2. The revenue discrepancy: €207K vs €501K. The number was wrong by 2.4x. How it happened (annual stats only captured 2,407 of 3,667 products — weighed items, variable-weight cheese missing). The fix.
3. The lost afternoon: three honest lessons.
   - Email sorting with Claude co-work: poor results, should have been abandoned after 15 minutes
   - OpenClaw bot attempt: rabbit hole, zero output
   - Being sick while the shop performs well: fever-brain + ambitious side experiments = wasted hours
4. "The fix was simple and painful: work until 21h."
5. The evening grind produced the entire Dashboard V2, three implementation plans, and repo cleanup. Productivity under pressure was higher than the scattered afternoon — because scope was locked and the plan was written.
6. The Perplexity discovery: inserting deep research between brainstorming and plan execution dramatically improves quality. This is a process insight, not a technical one.
7. **End of day: excitement starting to fade.** The foreshadowing. Something about the pattern feeling unsustainable. Not explicit — just a note that the energy is different from Day 1.

**What to cut entirely:**
- Pipeline first run details (21 Silver files, 7 Gold files)
- Master Config implementation (three config registries, two-pass import)
- Verification checks list (22 checks)
- Dashboard V2 build breakdown (7 phases)
- FRAIS redistribution details
- Category YoY technical issue
- "By the numbers" table
- Experiment queued section (GitHub agentic workflow)
- "What's still in flight" detailed backlog

**Step 1:** Read current `day-3.md` for source material
**Step 2:** Write rewritten version, diary voice, ~70-80 lines
**Step 3:** Commit

```bash
git add docs/devlog/day-3.md
git commit -m "rewrite day 3 log: the cracks, the revenue lie, the lost afternoon"
```

---

## Task 6: Edit Day 4

**Files:**
- Modify: `docs/devlog/day-4.md`
- Reference (read-only): `DEV_LOG_DAY4.md` (the good version to use as source)

**This is NOT a rewrite.** Day 4's voice is already the benchmark. The task is to:

1. Copy the content from `DEV_LOG_DAY4.md` into `day-4.md` (which is currently an empty template)
2. Add proper frontmatter for the build pipeline
3. Add the Uncle Bob / Craig Weiss quotes into the "What vibe coding actually is" section
4. Add reference to Graph 1 (three curves) and Graph 2 (flow-debt / perception gap) — either as embedded images or as prose description with image reference
5. Lightly trim the "specific debt" section — keep one representative example instead of three
6. Add the technical log link at the bottom

**Frontmatter:**
```yaml
---
title: "The Wall"
date: 2026-03-12
day: 4
status: done
hero_image:
shipped: ["2 implementation plans", "0 code shipped", "Clarity gained"]
---
```

**Where to add the discourse voices:** After the paragraph "Software engineering — real software engineering — is the discipline of building systems that stay comprehensible as they grow." Add:

> This isn't just my experience. Uncle Bob Martin said it this week: "For all the hype and hullabaloo about AI and vibe coding; this is not a layman's domain. The engineering bar is going way up." Craig Weiss put it differently: "The highest ROI has moved up the stack." They're right. The bar isn't going down. It's going up — and vibe coding doesn't change that. It just changes where you hit it.

**Where to add graph references:** In "The wall" section, after describing the wall, reference Graph 1:

> [placeholder: vibe-coding-three-curves.png — the three development curves]

In the perception gap moment (Day 4 felt disorienting because the dashboard looked done), reference Graph 2:

> [placeholder: vibe-coding-flow-debt.png — perceived progress vs hidden tech debt]

**Step 1:** Copy `DEV_LOG_DAY4.md` content into `day-4.md` with proper frontmatter
**Step 2:** Add Uncle Bob / Craig Weiss quotes
**Step 3:** Add graph references
**Step 4:** Trim specific debt to one example
**Step 5:** Add technical log link at bottom
**Step 6:** Commit

```bash
git add docs/devlog/day-4.md
git commit -m "publish day 4 log: the wall, enhanced with discourse voices and graph refs"
```

---

## Task 7: Write Day 5

**Files:**
- Modify: `docs/devlog/day-5.md`
- Reference (read-only): `DEV_LOG_DAY5.md` for shipped items and facts

**This is written fresh.** Day 5 IS the retrospective. No separate retrospective page.

**Target length:** ~80-100 lines. This is the longest day because it carries the thesis.

**Frontmatter:**
```yaml
---
title: "v0.1"
date: 2026-03-13
day: 5
status: done
hero_image:
shipped: ["Bug fixes (sparklines, field naming)", "v0.1 tagged", "The vibe coding thesis"]
---
```

**The beats (in order):**

1. **Opening:** This is closing day, not building day. Two visual bugs fixed from Day 4 (dead sparklines, field naming). Small things. The kind of work that takes 20 minutes when you know what you're doing.

2. **What v0.1 is:** Brief. A working retail intelligence dashboard for an independent shop, built in 5 days by a non-engineer between shop shifts. What works (4 tabs, 481 products, real data, weather). What doesn't (122 sparklines, 3 stub tabs, no real-time refresh). Honest, not apologetic.

3. **The vibe coding curve — the thesis:**
   This is where the four-graph framework lands. Not as academic analysis — as lived experience.

   Start with the feeling: "Three days of building felt like the hard part was over. Day 4 proved it wasn't."

   Introduce Graph 3 (marginal productivity rate) — progress-per-hour. Day 1: every hour produced visible output. Day 4: hours of work, zero code shipped. The rate crashed.

   The three curves: pure vibe coder (what I did), software engineer (what an engineer would have done), and the Grassroot Hopper fix (what I'll do next time). The research phase — zero visible progress that buys more sustainable progress later.

   Reference the hard data (Graph 4) — not all six metrics, just the most compelling 2-3. The 44% code churn. The perception gap. Enough to show this isn't just one person's experience.

   The pattern: vibe-coded games do this too. Playable in 3 days, weeks of grinding after. What works in vibe coding works straight away. What doesn't takes ages to fix.

4. **The Grassroot Hopper insight:**
   The curve is predictable. If you understand its shape, you can design products that ship in the sweet spot — after the research phase, before the plateau.

   Grassroot Hoppers lead the vibe coders and hobbyists. Not on the edge of software engineering — on the edge of what everyday people can build.

   This requires: design sense (scope ruthlessly), research discipline (paper before code), and pattern recognition (know when to stop).

5. **The co-founder gap:**
   Not "I need someone to write code for me." The tech co-founder is the radar — they see beyond the edge so you can stay on it. They push the threshold line upward. Without them, Day 4 happens. With them, Day 4 doesn't.

   Quote Uncle Bob: "The engineering bar is going way up." Quote Craig Weiss: "The highest ROI has moved up the stack." Both right — and that's exactly why this model needs two people, not one.

6. **Close:**
   What the foundation looks like: real data, real pipeline, documented architecture, catalogued debt. What happens next. And the honest invitation — written for the co-founder who's reading this.

**Step 1:** Write `day-5.md` following the beats above
**Step 2:** Verify frontmatter
**Step 3:** Commit

```bash
git add docs/devlog/day-5.md
git commit -m "write day 5 log: v0.1, the vibe coding thesis, the co-founder pitch"
```

---

## Task 8: Update retrospective to cancelled

**Files:**
- Modify: `docs/devlog/retrospective.md`

**Step 1:** Update frontmatter status to `draft` (keeping it as draft means it won't be published — no need for a `cancelled` status since the generator only publishes `live` or `done`). Add a note that the retrospective is merged into Day 5.

```yaml
---
title: "Retrospective"
date: 2026-03-14
status: draft
hero_image:
---

Retrospective content merged into Day 5.
```

**Step 2:** Commit

```bash
git add docs/devlog/retrospective.md
git commit -m "mark retrospective as merged into day 5"
```

---

## Task 9: Ensure DEV_LOG files exist for all days

**Files:**
- Check: `docs/devlog/DEV_LOG_DAY1.md` — does not exist. The technical detail for Day 1 lives in the date-prefixed `2026-03-09-day-1.md` (which is a stub) and in the original `day-1.md` before rewrite.
- Check: `docs/devlog/DEV_LOG_DAY3.md` — does not exist. Technical detail for Day 3 lives in the original `day-3.md` before rewrite.

**Step 1:** Before rewriting days 1 and 3, save the current content as DEV_LOG files:

```bash
cp docs/devlog/day-1.md docs/devlog/DEV_LOG_DAY1.md
cp docs/devlog/day-3.md docs/devlog/DEV_LOG_DAY3.md
```

**Step 2:** Commit these BEFORE doing any rewrites

```bash
git add docs/devlog/DEV_LOG_DAY1.md docs/devlog/DEV_LOG_DAY3.md
git commit -m "preserve day 1 and day 3 technical detail as DEV_LOG files"
```

**IMPORTANT:** This task MUST run before Tasks 3 and 5.

---

## Task 10: Build and verify

**Step 1:** Run the build pipeline

```bash
python3 scripts/build-hackathon.py
```

**Expected output:** All 5 days should build (status: done). Retrospective should be skipped (status: draft). Index page should build with all 5 days in the timeline.

**Step 2:** Verify the generated HTML files exist

```bash
ls -la website/hackathon/day-{1,2,3,4,5}.html
ls -la website/hackathon/index.html
```

**Step 3:** Open in browser to verify

```bash
open website/hackathon/index.html
```

**Step 4:** Commit generated HTML

```bash
git add website/hackathon/
git commit -m "rebuild hackathon site with all 5 days published"
```

---

## Execution order

Tasks have dependencies:

1. **Task 9** (preserve DEV_LOGs) — MUST run first
2. **Task 1** (rename screenshots) — independent
3. **Task 2** (placeholder graphs) — independent
4. **Tasks 3, 4, 5, 6, 7** (rewrite/write days 1-5) — depend on Task 9, independent of each other
5. **Task 8** (retrospective) — independent
6. **Task 10** (build and verify) — depends on all above

Parallelizable groups:
- Group A (do first): Task 9
- Group B (parallel after A): Tasks 1, 2, 3, 4, 5, 6, 7, 8
- Group C (last): Task 10
