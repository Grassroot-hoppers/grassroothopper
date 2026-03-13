---
title: "The Wall"
date: 2026-03-12
day: 4
status: done
hero_image:
shipped: ["2 implementation plans", "0 code shipped", "Clarity gained"]
---

* Product Master design doc written — the right solution to keyword-matching technical debt
* Implementation plan written for product-master.csv (6 tasks, ~30 min estimate)
* Day 4 MVP polish plan written (Tab 1 + Tab 2 correct/good/usable)
* None of it shipped

Day 4 was supposed to be the polish pass that turns a rough demo into something you could show to a shop owner. Instead it became a reckoning.

---

### The wall

Days 1–3 were ideas. The energy was high, the output was visible, the pipeline went from nothing to 24 CSVs → 21 Silver files → 7 Gold files → a live dashboard in 72 hours. The commits accumulated. The logs got longer. It felt like progress — because it was.

Day 4 is where that kind of momentum breaks.

The codebase is now real enough to resist. `build-demo.mjs` is 900+ lines. The pipeline has four layers (Bronze, Master Config, Silver, Gold), three config registries, a two-pass import, and a cascade of fallback logic that nobody wrote down in one place. Every new feature or fix requires understanding how all of it connects — which CSVs produce which Silver files, which Silver fields feed which Gold aggregations, which Gold shape the dashboard reads.

When something doesn't work, the failure could be in the POS export, the Bronze parsing, the Master Config transformation, the Silver schema, the Gold aggregation, the demo.json build, or the UI rendering. Six places to look. And looking requires reading code that I didn't write in a single clear-headed pass — I wrote it in sprints, at night, from plans that were sometimes overtaken by the code before the plan was finished.

This is the wall. Not a bug. Not a missing feature. The wall is the point where the complexity of what exists exceeds the maintainer's ability to reason about it.

<iframe src="graph1_roadmap.html" width="100%" height="480" frameborder="0" scrolling="no" style="border:none;border-radius:8px;"></iframe>

---

### What "vibe coding" actually is

There's a phrase circulating in software engineering communities right now: **vibe coding**. It describes a way of building that's become possible with AI-assisted development — move fast, generate code from descriptions, iterate in real time, let the AI hold the context you can't. It produces remarkable early output. In three days, a non-engineer ran a medallion architecture data pipeline for a French cheese shop and shipped a dark-theme analytics dashboard with sparklines, ABCD ranking, and a weather integration.

But vibe coding has a ceiling. The ceiling shows up when:

- The codebase grows past the point where any single context window can reason about all of it at once.
- Bugs require understanding the interaction between layers that were built in different sessions, sometimes by different AI models.
- Adding a feature means tracing data from origin through four transformations — and the tracing itself requires a level of code literacy that "describe what you want and generate it" can't replace.

Software engineering — real software engineering — is the discipline of building systems that stay comprehensible as they grow. That means naming conventions enforced everywhere, not just when remembered. Schema definitions that live in one place. Functions that do one thing. Tests that break when the contract changes. Architecture that's written before the code, not reverse-engineered from it.

I skipped most of that. Not because I didn't know it mattered — Day 2 had Perplexity research on the Medallion Architecture, Day 3 had 22 verification checks — but because I don't have the instincts to enforce it while also moving fast. The plans were good. The execution left seams.

> This isn't just my experience. Uncle Bob Martin said it this week: "For all the hype and hullabaloo about AI and vibe coding; this is not a layman's domain. The engineering bar is going way up." Craig Weiss put it differently: "The highest ROI has moved up the stack." They're right. The bar isn't going down. It's going up — and vibe coding doesn't change that. It just changes where you hit it.

<iframe src="graph2_research.html" width="100%" height="480" frameborder="0" scrolling="no" style="border:none;border-radius:8px;"></iframe>

---

### The specific debt

The hardest thing to admit: the CSV-to-Gold pipeline is more complex than I can reliably maintain alone.

It's not unmaintainable in principle — a data engineer would look at it and find it straightforward. But I'm not a data engineer. The gap isn't intelligence. It's pattern recognition built over years of reading code, debugging pipelines, and knowing intuitively which failure modes to expect.

Here's the clearest example: why do the product groups show the wrong members in Tab 2? I know it's a `displayName` vs `name` field mismatch between `build-demo.mjs` and `app.js`. I know exactly where to look. But every time I fix one field mismatch, another appears — because the same data goes through five transformations and I didn't enforce a consistent naming convention from the start.

The pipeline works. The dashboard renders. The data is real and the numbers are right. But the system is brittle in ways I can't see until something breaks, and fixing breaks requires more code comprehension than I reliably have under pressure.

---

### The hackathon result

The hackathon won't be what I hoped. The goal was a fully working, polished demo — Tab 1 and Tab 2 correct, good, and usable, shown to the shop operator with confidence. That's not what Day 4 produced.

What Day 4 produced: a clearer understanding of where the architecture needs to go, two well-written plans for the fixes, and an honest accounting of the gap between "built fast with AI" and "built to last."

That's not nothing. But it's not a hackathon win.

---

### What comes next

Two options, and I haven't decided between them.

**Option A: Simplify the pipeline before touching the dashboard.**
The product-master.csv plan is correct — replace keyword matching with an explicit lookup. The category YoY fix is a known 10-line change. The field naming is a 30-minute audit. Do the three foundation fixes first, then polish the UI.

**Option B: Start the pipeline from scratch with a simpler contract.**
One script. One output format. No Silver, no Gold, no four-layer medallion. The simplest possible pipeline: read CSVs, output one JSON with exactly the fields the dashboard needs, nothing more.

Option B feels like giving up. It isn't. It's what a software engineer would have built on Day 1 if they'd known how the project would grow. The Medallion Architecture is the right long-term answer. It's not the right answer for a dashboard that one person has to maintain on the side of running a shop.

---

### The deeper lesson

Vibe coding is a real skill. It's not a shortcut — it's a way of working that requires genuine judgment about what to generate, when to stop, and what debt you're taking on. The problem isn't the method. The problem is that I'm still learning what "knowing when to stop" feels like in practice.

The signal that I missed: every time I added a new config registry or fallback layer to handle an edge case, I should have asked whether the edge case was a pipeline design problem or a data quality problem. Most of them were data quality problems. And data quality problems don't get fixed by making the pipeline smarter.

Three days of building taught me that. Day 4 of not shipping confirmed it.

---

*Full technical log: [DEV_LOG_DAY4.md](DEV_LOG_DAY4.md)*
