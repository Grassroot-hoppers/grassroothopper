---
title: "The Sun Is Out"
date: 2026-03-09
day: 1
status: done
hero_image: media/day-1-screenshot.png
shipped: ["Repo bootstrap", "Excel-to-dashboard workflow", "Dashboard coherence research"]
---

My laptop is in the sun. It's a genuinely beautiful day, and I'm mixing three screens — phone Cursor, browser Cursor, MacBook — because I want this workflow to work for the kind of mornings where you only have one hand free.

Before touching any code, I asked for a roadmap. Not a sprint board. A roadmap based on what I already wrote in the spec. I wanted to start from what I knew, not from what felt exciting.

## What this hackathon is actually about

Not building the final product in five days. Building a serious `v0.1` intelligence demo — something real, grounded in real shop data, that proves the whole stack can work.

What it's NOT: drifting into production architecture, pretending this is already a live ordering tool, widening into multi-store or auth or anything that isn't directly needed to prove the point.

The framing matters. Scope creep doesn't announce itself. It shows up as "while I'm here I might as well..." The phase gate — *no dashboard wiring until one real export proves the file format* — was Day 1's way of enforcing that.

## The momentum

By end of day, the repo went from empty to contributor-ready. AGENTS.md, phone-agent workflow, French operator-facing copy, an issue backlog. Someone could pick this up and know where to start.

The Excel-to-dashboard mapping took most of the day. I sat with the data — what files exist, what they actually contain, what I'm assuming versus what I've verified. The key decision: nothing gets wired into the dashboard until one live POS export proves the file format in practice. Documentation helps. The actual CSV decides.

The design direction also shifted. I'd been working with a warm artisanal palette — cream, earth tones. But the real users are 26-27 year olds who open this at 7am before a shift. They don't want something that looks like a chalkboard menu. They want sharp, dark, fast. That's what we're building.

## Tomorrow

Tomorrow is the data day. The goal is to go from zero real data to a pipeline that proves the whole chain works — POS exports in, something useful out.

---

*Full technical log: [DEV_LOG_DAY1.md](DEV_LOG_DAY1.md)*
