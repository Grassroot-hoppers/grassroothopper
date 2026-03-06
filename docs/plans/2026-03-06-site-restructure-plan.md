# Site Restructure Plan — "Hell Yes" Pass

**Date:** March 6, 2026
**Input:** Three independent audits (Claude, GPT-5.4 #1, GPT-5.4 #2)
**Constraint:** Honest traction state — no deployed product yet. Hackathon (March 10–14) delivers first real proof. Co-op is aspirational, only GPFC srl exists.

---

## Core Strategy

**Don't fake traction. Frame the site as "building in public, first proof shipping next week."**

The hackathon is the site's centerpiece right now. Everything points toward it. After March 14, the site flips: the devlog and shipped tools become the proof strip that all audiences need.

**Lead with David Toolkit as the wedge, not the whole movement.** The movement framing stays, but it moves from "this is a movement" to "this is how a movement starts — with one real tool for one real shop."

---

## What Changes

### 1. Persistent Navigation (all pages)

Add a fixed top nav bar to every page. Current state: hero has demo buttons, no real nav.

```
[GH logo/name]                    [About] [Learn] [Hackathon] [GitHub →]
```

Hackathon link gets a teal accent badge while the event is upcoming/live.

### 2. Hero Rewrite

**Current:** "We help communities create and govern their own software."
**Problem:** Mission statement, not a hook. Doesn't say what's happening *now*.

**New hero (pre-hackathon):**
```
Grassroots Hoppers

Community-owned software,
built in the open.

We're building open-source tools for small businesses and local
communities — starting with a specialty food shop in Brussels.
First public build: March 10–14.

[Follow the hackathon →]  [Read the SPEC →]

Brussels · Open source · AGPL-3.0 · Est. 2025
```

**New hero (post-hackathon, after March 14):**
```
Grassroots Hoppers

Community-owned software,
built in the open.

We built two open-source retail tools in 5 days for a real shop
in Brussels. Now we're documenting the roadmap so any shop can
replicate them.

[See what we built →]  [Read the playbook →]

Brussels · Open source · AGPL-3.0 · Est. 2025
```

### 3. Proof Strip (below hero)

A single horizontal bar with honest, hard facts. No inflated language.

**Pre-hackathon:**
```
1 shop (Chez Julien, Brussels) · 2 tools in development · 5-day public build starting March 10 · All code AGPL-3.0 on GitHub
```

**Post-hackathon:**
```
1 shop · 2 tools shipped · 5 days · [X] commits · [X] devlog entries · All code AGPL-3.0 on GitHub
```

### 4. Audience Entry Points (new section after proof strip)

Replace the current "explore demos" top bar with a lightweight audience router.

**Section: "What brings you here?"**

Four cards, one line each:

| Card | Label | Destination |
|------|-------|-------------|
| Incubator/Accelerator | "I evaluate ventures" | #for-incubators (anchor or future page) |
| Social Investor | "I fund impact" | #for-investors (anchor or future page) |
| Movement Builder | "I build communities" | #for-movement (anchor or future page) |
| Event Organizer | "I program events" | /speak.html |
| Developer | "I write code" | GitHub repo |
| Shop Owner | "I run a small business" | #for-shops (anchor or future page) |

For now, these scroll to relevant sections on the main page. Post-hackathon, the high-value ones (investor, incubator) get dedicated landing pages.

### 5. The Story (sections 02–07) — Tighten, Don't Rewrite

The narrative sections are the site's strength. Keep them but:

- **Section 02 (The Shift):** Add one sentence at the end: "That's the thesis. The hackathon is the first test."
- **Section 04 (The Pattern):** Keep the external examples but add a bridge: "These builders prove it's possible. Grassroots Hoppers exists to make it *repeatable*."
- **Section 06 (The Blueprint):** This is where Rob Hopkins people land. Add: "We're not replacing Transition Towns. We're adding the digital layer — community-owned software as infrastructure, the same way Transition added community-owned food and energy."
- **Section 07 (The Name):** Cut from 4 cards to 2 (Grassroots + Grace Hopper). The hop farming and "hopping" cards are charming but dilute the pitch for serious audiences. Move them to an About page.

### 6. Section 08 (How It Works) — Keep, Add Honesty Layer

The Build → Document → Replicate flywheel is clear. Add a status indicator:

```
Build       → [In progress — Hackathon March 10–14]
Document    → [Starting — devlog goes live March 10]
Replicate   → [Planned — playbooks publish after hackathon]
```

This turns abstract method into visible progress.

### 7. Section 09 (First Projects) — Reframe as "The Wedge"

**Current:** "Two projects. Both open source. Both designed to replicate."
**Problem:** Oversells. Neither project is shipped yet.

**New framing:**
```
THE FIRST PROOF

David Toolkit is the wedge. A specialty food shop in Brussels
needs demand prediction and workflow tools. Big chains have this.
Small shops don't. We're building it open-source, documenting
every step, and publishing the playbook.

Social Media V2 is the bigger bet. A cooperative social network
for local communities — no algorithm, no ads, city by city. The
SPEC is published. Development starts after David Toolkit ships.
```

### 8. Section 10 (The Model) — Downgrade Co-op Language

**Current:** "Contributors don't get paid. They get ownership." + co-op (SC) language.
**Problem:** The co-op doesn't exist yet. This reads as promise, not structure.

**New framing:**
```
THE MODEL

Grassroots Hoppers is built by GPFC srl, a registered Belgian
company (BCE BE0545849385). All code is AGPL-3.0 — free to use,
required to stay open.

The roadmap includes cooperative governance: a legal structure
(SC — société coopérative under Belgian law) where contributors
become co-owners. That structure is being designed now. Until it's
filed, the commitment is simple: everything is open-source,
everything is documented, and the governance templates will be
published for any community to adopt.

We'd rather be honest about what's real than promise what isn't.
```

### 9. New Section: "Where We Are" (Roadmap)

Add between Model and Ecosystem. Concrete timeline.

```
WHERE WE ARE

Done:
· GPFC srl registered (BCE BE0545849385)
· Initiative SPEC published
· Social Media V2 SPEC published
· David Toolkit repo live on GitHub
· Workflow map prototype built
· Website + hackathon infrastructure ready

March 10–14:
· Shop Owner Hackathon #001
· Sales prediction engine (POS + weather)
· Interactive workflow map
· 5-day public devlog

Q2 2026:
· David Toolkit playbook published
· First "Fork & Deploy" workshop template
· Cooperative governance design (SC statutes draft)

Q3–Q4 2026:
· Social Media V2 development begins
· First community replication pilot
· SC cooperative filing
```

### 10. CTA Rewrite — Audience-Specific Asks

**Current:** "Talk to the founder" / "Read the full SPEC" / "Fork & contribute"
**Problem:** Generic. No audience knows what to do.

**New CTA:**

```
GET INVOLVED

[For event organizers]
Book Julien for a talk or workshop.
→ speak.html

[For incubators & investors]
Back a community software pilot.
→ mailto: with subject line "Partnership inquiry"

[For developers]
Fork a project. Open an issue. Ship a PR.
→ GitHub

[For shop owners]
Get a tool built for your shop.
→ mailto: with subject line "I run a shop"

[For movement builders]
Run a Grassroots Hoppers workshop in your city.
→ learn.html
```

### 11. New Page: About (about.html)

```
ABOUT

Julien Thibaut
Shop owner. Self-taught developer. Brussels.

Julien runs Chez Julien, a specialty food shop in Brussels. In
2025, he started building software tools for his own shop using
AI-assisted development — no technical background, no team, no
funding. The quality of what one person could build surprised him.

Grassroots Hoppers is the question that followed: if one shop
owner can build real tools, what happens when communities do it
together?

GPFC srl is the company behind the initiative. Registered in
Belgium (BCE BE0545849385). The first product is David Toolkit.
The first public build event is March 10–14, 2026.

[Photo placeholder]

Contact: staycreative@julien.care
GitHub: github.com/Grassroot-hoppers
```

### 12. New Page: Speak (speak.html)

```
BOOK JULIEN

Talk: "What Changed in 2025"
Why non-technical people can now build civic and local economic
tools — and what that means for communities, cooperatives, and
local economies.

Workshop: "Build Your Own Tool"
3-hour hands-on session. Participants go from idea to working
prototype using no-code and AI-assisted development.

Format: Keynote (30–45 min), Workshop (3 hours), Panel

Audience fit: Social innovation, cooperative economy, open source,
civic tech, local economic development, Transition network events

Languages: French, English, Dutch (conversational)

Based in: Brussels. Available across Europe.

[Contact: staycreative@julien.care]
[Subject: Speaking inquiry]
```

### 13. Ecosystem Section — Trim

Keep but shorten. Remove Rilke quote entirely (every audit flagged it as noise for serious audiences). Move domain list to footer.

### 14. Kill / Move List

| Item | Action |
|------|--------|
| Rilke quote | Delete |
| Name etymology cards 3+4 (Hopping, Hop) | Move to About page |
| "Eyes light up — you're one of us" | Replace with audience-specific CTA |
| "Explore the demos ↓" top bar | Replace with persistent nav |
| "Contributors don't get paid. They get ownership." | Rewrite to honest current state |
| "Both designed to replicate" | Replace with "First one ships March 14" |
| "Coming soon" items on Learn page | Keep but add dates, or remove if no date |

---

## Execution Order

1. **Persistent nav** — affects all pages, do first
2. **about.html** — needed by every audience
3. **speak.html** — needed by event organizers (fastest "hell yes" to unlock)
4. **Hero + proof strip rewrite** — the first 10 seconds
5. **Audience entry points** — the next 10 seconds
6. **Sections 02–07 tightening** — minor edits, big impact
7. **Section 08–09 reframe** — honesty about status
8. **Section 10 co-op language downgrade**
9. **New "Where We Are" roadmap section**
10. **CTA rewrite**
11. **Ecosystem trim**
12. **Update learn.html, hackathon/, and other pages with new nav**

---

## Post-Hackathon Flip (March 15+)

After the hackathon ships:
- Hero changes from "starting March 10" to "we built two tools in 5 days"
- Proof strip gets real numbers (commits, devlog entries, tools deployed)
- David Toolkit section links to live demo / screenshots
- "Where We Are" roadmap updates Done section
- Devlog becomes the site's strongest proof piece
- Learn page gets first real playbook

This is a 30-minute content swap, not a redesign. The structure we build now supports both states.
