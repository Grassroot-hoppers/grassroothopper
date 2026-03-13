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

## The vibe coding curve — a multi-graph thesis

The central metaphor for the entire dev log series. Not one graph — a four-graph framework backed by real data. This is the intellectual backbone of the story, introduced progressively across the 5 days but fully articulated in Day 5.

---

### Graph 1: The three development curves (progress vs. time)

The core thesis graph. Three curves on the same axes.

**Curve 1 — Pure vibe coder (red dotted):** Steep early climb. AI generates features fast. Everything seems to work. Then tech debt compounds — each fix creates new problems, each feature requires understanding more context than the vibe coder can hold. Progress-per-hour collapses. Without engineering skills, you can fully plateau.

This is what happened in the hackathon. Days 1-3 were the steep part. Day 4 was the plateau.

The pattern shows up everywhere: vibe-coded games are playable in 3 days, then spend weeks grinding on balance, UI, and broken features. What works in vibe coding works straight away. What doesn't takes ages to fix.

Real data: GitClear's analysis of 211 million lines of code found that AI-assisted code churn rose from 5.5% in 2020 to 7.9% in 2024 — a 44% increase in code that gets rewritten within two weeks. That's the plateau mechanism: every "fix" creates new problems.

**Curve 2 — Software engineer (teal dashed):** Slow start. Days of planning, architecture, proper abstractions, tests. Looks like nothing is shipping. Then steady S-curve growth following the classic Norden-Rayleigh cumulative model used in software cost estimation for 40+ years. There's a crossover point (around day 5-6) where the engineer's total output passes the vibe coder's — and then keeps going.

**Curve 3 — Grassroot Hopper fix (blue solid):** Front-load research with zero visible progress. Paper first. System design with LLMs. Understand the data model, the architecture, the product design *before writing a single line of code*.

Then vibe code from that foundation. Steep climb like Curve 1, but from better ground. The plateau still comes — Grassroot Hoppers aren't engineers and don't need to be — but it arrives **later and higher** than the pure vibe coder. The research phase pushed the inflection point out.

The hackathon lesson: if Day 0 had been spent on paper — researching database systems, working with LLMs purely on system design, architecture, and product design — the steep climb would have lasted through Day 4 instead of dying on it. One day of zero visible progress buys two more days of steep climb.

```
Progress
  ▲
  │                                               ╱ ← Engineer (teal, steady)
  │                                             ╱
  │             · · · · · · · · · · · · · ·   ╱
  │           ·  ← Vibe coder (red, plateau)╱
  │         ·                     ○ ○ ○ ○ ○╱○ ○  ← GH fix (blue, higher plateau)
  │       ·                    ○         ╱
  │     ·                   ○          ╱
  │   ·                  ○           ╱
  │  ·                ○            ╱
  │ ·              ○             ╱
  │·            ○              ╱
  │          ○               ╱
  │        |               ╱
  │  ╱   |research|      ╱
  │╱                    ╱
  └──────────────────────────────────────────────► Time
```

---

### Graph 2: The flow-debt tradeoff (the perception gap)

Two lines on the same axes that diverge over time:

**Perceived progress** — rises fast, flattens. You feel like you're 80% done.

**Hidden tech debt** — rises exponentially and crosses perceived progress at the cut-off point.

This directly maps the Waseem et al. 2025 framework on vibe coding. Google's 2024 DORA report found a 7.2% decrease in delivery stability for every 25% increase in AI adoption.

The cut-off point is where "it looks done" but is actually breaking underneath. Day 4 was this exact moment — the dashboard rendered, the numbers were right, but every fix required re-reading code through six transformation layers. It looked like a finished product. It was a house of cards.

This graph explains why Day 4 felt so disorienting: the visible output suggested the project was 80% done. The hidden debt said otherwise.

```
  ▲
  │                              ╱ Hidden tech debt (exponential)
  │                            ╱
  │                  ·  ·  · ╱·  ·  ·  Perceived progress (flat)
  │               ·       ╱
  │            ·       ╱
  │         ·       ╱
  │       ·      ╱
  │     ·     ╱
  │   ·    ╱
  │  ·  ╱    ← CUT-OFF: "looks done, actually breaking"
  │ · ╱         (Day 4)
  │·╱
  └──────────────────────────────────────────────► Time
```

---

### Graph 3: Marginal productivity rate (progress-per-hour)

The derivative of Graph 1. This is THE founder-skill graph — it shows not total progress, but **how much progress each additional hour produces**.

The vibe coder's rate peaks on Day 1 and collapses by Day 3-4. The engineer's rate peaks around Day 5-6. The Grassroot Hopper's rate stays high between Days 2-7 because the research phase delayed the peak.

**The red threshold line** is the key: below that line, every hour of work produces negligible output. Knowing where each curve crosses that threshold is literally the Grassroot Hopper moat — you design your product to ship before crossing it.

```
Progress/hour
  ▲
  │·
  │ ·    ← Vibe coder rate (peaks early, crashes)
  │  ·
  │   ·        ○ ○
  │    ·     ○     ○  ← GH fix rate (delayed peak, longer plateau)
  │     ·  ○         ○
  │──────·─○───────────○──╱──── RED THRESHOLD (diminishing returns)
  │       · ·         ╱ ○
  │  ╱      · ·    ╱     ○
  │╱    ╱      ·╱·          ← Engineer rate (slow build, peaks late)
  │  ╱      ╱
  │╱     ╱
  └──────────────────────────────────────────────► Time
```

The founder who understands this graph doesn't try to push past the threshold. They design projects where Day 1 of coding (after research) starts near the peak and the product ships before crossing the threshold. That's the moat.

---

### Graph 4: The hard data

Real numbers from multiple research sources. These aren't opinions — they're measurements.

| Metric | Number | Source |
|--------|--------|--------|
| Initial velocity boost | 37.5% (range: 20-55%) | Industry midpoint |
| Code churn increase | 44% (5.5% → 7.9%) | GitClear, 211M LOC, 2020-2024 |
| Maintenance cost increase | 62.5% (20-25% → 30-50%) | Industry comparison |
| Delivery stability loss | 7.2% per 25% AI adoption | Google DORA 2024 |
| Perception gap | 39% | Developer surveys vs measured output |
| Tech debt accumulation increase | 35.5% | GitClear structural analysis |

The story the numbers tell: AI-assisted development is genuinely faster at the start (37.5%) but produces code that gets rewritten 44% more often, costs 62.5% more to maintain, and degrades delivery stability measurably. The 39% perception gap means developers think they're going faster than they are.

Key sources for citation:
- GitClear AI Code Quality Research 2025: https://www.gitclear.com/ai_assistant_code_quality_2025_research
- Waseem et al. 2025 (vibe coding framework): https://arxiv.org/abs/2512.11922
- DORA report on AI adoption impact
- Ars Technica: "Study finds AI tools made open-source developers 19% slower"

---

### How the graphs appear in the dev logs

The four graphs aren't dumped on the reader at once. They appear progressively:

- **Day 2 or 3:** First hint. A sentence about the progress feeling unsustainable. No graph yet.
- **Day 4 ("The Wall"):** Graph 1 introduced — the three curves. Graph 2 referenced (the perception gap: "it looked done but was breaking underneath"). This is where the reader first sees the pattern.
- **Day 5 ("v0.1"):** Full thesis. Graph 3 (marginal productivity — the founder-skill graph) and Graph 4 (hard data). The Grassroot Hopper insight fully articulated. The co-founder pitch grounded in real numbers.

The actual visual assets (SVG or similar) will be created during implementation for the website. The dev log markdown can reference them or embed the key insight in prose.

---

### The voices from the discourse

Two screenshots captured during the hackathon (in `docs/devlog/`) anchor this in the broader conversation happening right now:

- **Uncle Bob Martin:** "For all the hype and hullabaloo about AI and vibe coding; this is not a layman's domain. The engineering bar is going way up, and getting over that bar will not be easy."
- **Craig Weiss:** "If you want to survive in the age of vibe coding, you need to become an expert in system design, architecture & product design. The highest ROI has moved up the stack."
- **Ben Dickson:** "The biggest winners of AI-assisted coding and vibe coding will be people who have actual experience writing real code and building software pre-AI era."

These voices say the bar is going up and vibe coding doesn't change that. Julien's hackathon is the lived case study — 5 days that show exactly where the bar is, what happens when you hit it, and what it would take to push it.

---

### The Grassroot Hopper position

Grassroot Hoppers don't care about software engineering. They are NOT trying to become engineers. They are on the edge of what everyday people can build with open-source tools — leading the vibe coders and hobbyists.

The thesis crystallizes into one sentence: **the new skill isn't engineering — it's knowing the shape of the curve and designing products that ship before the plateau.**

This requires:

1. **Design sense** — scope ruthlessly, build things AI can deliver well
2. **Research discipline** — spend time on paper before touching code. System design, architecture, product design with LLMs. Zero visible progress that pays off later.
3. **Pattern recognition** — know when you're approaching the plateau and stop, hand off, or simplify before you cross it. Graph 3's threshold line is the decision boundary.

A tech co-founder's role is not to replace the vibe coder. It's to provide **"beyond the edge" insight** — they can see where things will break before Julien hits the wall. They push the threshold line in Graph 3 upward. They extend the sweet spot. They're the radar that lets you stay on the edge instead of falling off it.

The combination of a design-minded founder who understands the curve + a technical co-founder who can see beyond it = products that non-engineers build and engineers can sustain. That's the Grassroot Hopper model.

The co-founder pitch becomes: "I understand where the boundary is. I need someone who can push the boundary itself upward."

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
