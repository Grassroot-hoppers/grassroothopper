---
title: "Hackathon Kickoff & Data Archaeology"
date: 2026-03-09
day: 1
status: live
hero_image: media/day-1-screenshot.png
shipped: ["Repo bootstrap", "Excel-to-dashboard workflow", "Dashboard coherence research", "Pencil design exploration"]
---

My laptop is in the sun. It is a beautiful day, so I want to mix a phone-based Cursor/agent workflow with Cursor on the web and Cursor on my MacBook Pro.

I started this session by asking for a roadmap based on the spec that was already written instead of jumping straight into implementation.

<div class="video-embed">
  <video controls playsinline preload="metadata" poster="media/day-1-screenshot.png">
    <source src="media/day-1-recap.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
  <p class="video-caption">Day 1 recap — 1½ min</p>
</div>

<div class="video-embed">
  <img src="media/day-1-timelapse.gif" alt="Day 1 accelerated timelapse" class="timelapse-gif">
  <p class="video-caption">Day 1 timelapse — 2x speed</p>
</div>

## The brainstorm: what this hackathon is really about

Today is not about trying to build the final product in one leap. It is about turning the existing spec, POS context, and messy high-context notes into a working execution loop.

The core decision is to treat this hackathon as the creation of a serious `v0.1` intelligence demo first, not an "AI ordering engine" yet.

**What the hackathon is:**

- Build a browser-first intelligence center that can ingest real-shop shaped exports.
- Preserve the raw-vs-interpreted contract so the software stays trustworthy.
- Make the repo contributor-ready early, not only after the demo is pretty.
- Use Cursor, phone, and laptop together as part of the product-building workflow, not as a side experiment.

**What not to do today:**

- Do not drift into production architecture.
- Do not pretend this is already a live ordering assistant.
- Do not widen into multi-store, auth, or heavy infrastructure.
- Do not lose the founder narrative under technical noise.

## What actually got done

A lot happened for a Day 1. The plan was to set up the operating rhythm and ground everything in reality. That happened — and then some.

### Repo bootstrap

Initial demo committed. AGENTS.md, phone-agent workflow docs, cloud agent starter skill, French operator-facing product copy, issue backlog. The repo went from nothing to contributor-ready scaffolding.

### Excel-to-dashboard workflow

Biggest chunk of work. Mapped the path from raw shop exports to a trustworthy dashboard pipeline — what files exist, what they contain, what is still unverified, and what needs a live export before any dashboard logic can claim to be real.

Five commits, with dedicated verification around the export workflow:

1. **Canonical export registry** — a versioned map of the raw files, the evidence behind them, and the rules for trusting them
2. **Source index + report families** — 8 report families (category stats, daily closure, CA/TVA, evolutionary stats, stock movements, client segments, product listings, client listings)
3. **Dashboard workflow mapping** — clarified how raw exports can become usable sales, stock, client, and ordering signals inside the dashboard
4. **Phase gate + live evidence protocol** — 5 explicit unknowns that need live export verification. Phase 2 is blocked until we capture one real `44A` CSV export
5. **Data intake structure + 3-year export SOP** — how exports get captured and stored going forward

The key decision: **no dashboard wiring until we have one real export proving the file format in practice.** Documentation helps, but the live files decide.

### Dashboard coherence research

Deep dive into what Notion actually contains vs what the codebase assumes vs what the old Pencil prompt described. Established a signal hierarchy:

1. **Notion** (strongest) — the real operational system with 23 suppliers, Cap 2026 financial framework
2. **Codebase** (solid) — POS scoring engine works but runs on synthetic data
3. **Old Pencil prompt** (weakest) — written without checking Notion, data examples were wrong

Locked several decisions: build-time data pipeline, Open-Meteo for weather, Todoist for tasks, all 23 suppliers (not a subset), performance zones drive ordering confidence.

### Pencil design exploration

Researched Pencil (.pen files) as a design-as-code tool. Assessed fit for the David dashboard — strong match for Git-native design, CSS variable sync, and component extraction. Created the first `.pen` file (`davidtoolkit.pen`) and wrote a detailed prompt for the "Tableau de Pilotage" dashboard.

Key design shift: the warm/artisanal cream palette is out. The real users are 26-27 year olds — they want modern, sharp, high-impact. Dark background, clean typography, performance zone colors that pop.

## Decisions

- **The export workflow is evidence-first, not assumption-first.** Raw files first, dashboard logic second.
- **Performance zones are the core logic.** Rouge/Orange/Vert/Bleu isn't decoration — it's the ordering confidence signal that drives the entire dashboard.
- **Old Pencil prompt is discarded.** A new prompt must be grounded in Notion reality and the chosen visual direction.
- **Phase gate is real.** No data pipeline or UI work until one live export proves the file shape.
- **Design direction needs brainstorming.** Structure (3 zones, no-scroll, ordering confidence) stays. The visual skin is open.

## What's next (Day 2)

Tomorrow is the data day. The goal is to go from synthetic demo data to real shop data feeding the dashboard.

- **Export two years of POS data** — pull category stats, CA/TVA, and evolutionary reports from the POS.
- **Clean and normalize the exports** — handle the usual POS export mess: semicolons, Latin-1 encoding, decimal commas, inconsistent date formats.
- **Build the canonical database** — replace the synthetic `demo.json` with a real data pipeline.
- **Wire live data sources** — Open-Meteo for weather, Todoist for daily tasks, Notion for supplier cadences. All at build time.
- **Unblock Phase 2** — the first real `44A` CSV export lifts the phase gate on the export workflow.
- **Design direction** — if time allows, brainstorm the new visual direction and write the updated Pencil prompt.
