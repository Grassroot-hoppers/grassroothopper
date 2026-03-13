---
title: "The Cracks"
date: 2026-03-11
day: 3
status: done
hero_image:
shipped: ["Pipeline end-to-end", "Revenue fix €207K → €501K", "Dashboard V2", "Perplexity workflow"]
---

Day 3 started differently. Before touching any code, 45 minutes of questions — designed to find out whether the AI actually understands the shop or is pattern-matching on data I fed it.

The AI got most of it right. Where it didn't, those became the work items.

## The revenue lie

The pipeline ran end-to-end for the first time. 24 CSVs went in. 21 Silver files came out. 7 Gold files. And then the numbers started talking.

One of them was wrong by a factor of 2.4.

The `store-summary.json` showed €207,000 in revenue for 2025. Everyone who's ever been in that shop knows it does around €500K. Something upstream was broken.

The annual export — the file I'd used as the revenue source — only captured 2,407 of 3,667 products. The missing ones are weighed items, variable-weight cheese, anything sold by piece rather than scanned barcode. The POS annual stats export simply doesn't include everything the shop sells.

Switched to monthly stats as the revenue source. 2025 revenue: €501K. That's the real number.

## The lost afternoon

I was sick. Not a little tired — genuinely sick, running a fever, trying to keep working because the shop was doing well and there were things that needed attention. Bad combination.

I spent a meaningful block trying to use Claude's collaborative mode to sort through email backlog. Poor results — the AI couldn't maintain context across threads, and the overhead of correcting it was higher than just doing it myself. Should have killed it after 15 minutes.

Then I tried to build an OpenClaw bot. Went nowhere. Another rabbit hole.

Fever-brain plus ambitious side projects equals wasted afternoon. The fix was simple and painful: work until 21h.

The evening session produced the entire Dashboard V2, three implementation plans, and the repo cleanup. Productivity under pressure was higher than the scattered afternoon — because the scope was locked and the plan was written.

## Perplexity as a research layer

The most valuable process insight of the day wasn't a feature. It was a workflow.

Inserting a Perplexity deep research pass between brainstorming and plan execution dramatically improves both. The step catches things the AI wouldn't surface on its own — real-world patterns, architecture precedents, edge cases. The Medallion Architecture on Day 2 came from that kind of research pass. The transaction-first pipeline simplification today came from the same move.

**Brainstorm → Research → Plan → Execute.** Not optional.

## The foreshadowing

The evening grind produced real things. Dashboard V2, two full implementation plan documents, a cleaned repo. Good output.

But the energy was different from Day 1. Day 1 felt like acceleration. Day 3 felt like making up ground. There's a difference. I didn't name it yet, but I felt it.

---

*Full technical log: [DEV_LOG_DAY3.md](DEV_LOG_DAY3.md)*
