---
title: "v0.1"
date: 2026-03-13
day: 5
status: done
hero_image:
shipped: ["Bug fixes (sparklines, field naming)", "v0.1 tagged", "The vibe coding thesis"]
---

Closing day, not building day.

Two visual bugs carried from Day 4: 122 products showed a flat red sparkline — a dead line instead of a blank — because they have no monthly history in the POS data. A `displayName` field referenced throughout `app.js` didn't exist on any product. Both fixed. Small things. The kind of work that takes 20 minutes when you know what you're doing.

## What v0.1 is

A working retail intelligence dashboard for an independent shop, built in 5 days by a non-engineer between shop shifts.

**What works:**
- Tab 1 (Briefing): zone signal, ordering reminders, next-week revenue prediction, 14-day weather
- Tab 2 (Produits): 481 products, ABCD ranking, search, category filter, sparklines for 359 products
- Tab 3 (Catégories): category mix with revenue, share, YoY growth
- Tab 4 (Fournisseurs): supplier ranking, ordering days, top products per supplier

**What doesn't work yet:** sparklines for 122 products with no monthly POS data, Tabs 5–7, real-time refresh.

Honest. Not apologetic.

## The vibe coding curve

Three days of building felt like the hard part was over. Day 4 proved it wasn't.

Look at where the progress went: Day 1 — every hour produced visible output. Day 2 — the pipeline shipped in an afternoon. Day 3 — the entire Dashboard V2 materialized overnight. Day 4 — hours of work, zero code shipped. The marginal productivity rate didn't slow down. It crashed.

<iframe src="graph3_community.html" width="100%" height="480" frameborder="0" scrolling="no" style="border:none;border-radius:8px;"></iframe>

This isn't a personal failure. It's a pattern. Vibe-coded games do this too: playable in three days, weeks of grinding after. What works in vibe coding works straight away. What doesn't takes ages to fix — because "what doesn't work" usually means a structural problem, not a missing line.

The three curves:

<iframe src="graph1_roadmap.html" width="100%" height="480" frameborder="0" scrolling="no" style="border:none;border-radius:8px;"></iframe>

The **pure vibe coder** (what I did): rapid early output, then a wall. The **software engineer** (what an experienced engineer would have done): slower start, research phase, architecture first — then more sustainable progress, no wall. The **Grassroot Hopper fix** (what I'll do next time): research phase up front, even though it produces zero visible output. Buy the sustainable curve. Ship in the sweet spot.

---

## The Grassroot Hopper insight

The curve is predictable. Once you know its shape, you can design products that stay in the productive zone — past the research phase, before the plateau.

This requires three things: **design sense** (scope ruthlessly — the dashboard that does one tab well beats the dashboard that does seven tabs badly), **research discipline** (paper before code — the Medallion Architecture came from a Perplexity research pass, not from instinct), and **pattern recognition** (know when the returns are starting to diminish, and stop before the wall).

Grassroot Hoppers lead the vibe coders. Not on the edge of professional software engineering — on the edge of what everyday people can build. That edge is moving fast. The question is whether you're ahead of it or running into it.

## The co-founder gap

Day 4 wasn't a bad day because I hit a bug. It was a bad day because I hit the limits of what I can see alone.

The technical co-founder isn't "someone to write the code for me." They're the radar — they see past the edge so I can stay on it. They know what a naming convention inconsistency costs at scale before it costs it. They see the pipeline complexity building before it becomes the wall.

Uncle Bob Martin said it this week: *"For all the hype and hullabaloo about AI and vibe coding; this is not a layman's domain. The engineering bar is going way up."* Craig Weiss put it differently: *"The highest ROI has moved up the stack."*

Both right. Both describing the same gap. With a co-founder, Day 4 doesn't happen. Not because they write the code — because they push the threshold line upward, and I stay in the productive zone longer.

## The foundation

What v0.1 leaves behind: real POS data, a documented architecture, a working pipeline, catalogued debt. A codebase that somebody else could pick up.

What comes next: fix the sparkline data source, modularize `build-demo.mjs`, implement Tabs 5–7. Find the person who reads Day 4 and thinks "I know exactly how to fix that."

If that's you — [the repo is open](https://github.com/gpfc-srl/david-retail).

---

*Full technical log: [DEV_LOG_DAY5.md](DEV_LOG_DAY5.md)*
