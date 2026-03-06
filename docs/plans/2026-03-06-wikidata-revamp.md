# Wikidata Description Revamp — Complete

*March 6, 2026 — Julien + GPT-5.4 Thinking + Claude Opus 4.6*

---

## Entity Scope

**Wikidata Q138589387 describes the Grassroots Hoppers initiative** — not GPFC srl (the company behind it) or grassroothopper.com (the website). GPFC srl will get its own Wikidata entry as a separate Belgian company entity (see `2026-03-06-julien-online-presence.md`).

---

## Description Strategy (Three Formats)

Three descriptions serve three contexts. All approved March 6, 2026.

### 1. Wikidata Description (short, neutral, identifying)

> Brussels-based open-source initiative for community-owned software

Published on Wikidata Q138589387 — English and French (FR: *initiative bruxelloise open source de logiciels communautaires*).

### 2. SEO / Structured Data Description (meta tags, README headers, knowledge graphs)

> Brussels-based open-source social innovation initiative helping communities create, govern, and replicate community-owned software and digital commons through workshops, roadmaps, and no-code, AI-assisted development

Used in: SPEC.md header, README.md header, website meta description tags, index.html meta tags.

### 3. Pitch Bio (about pages, LinkedIn, social profiles)

> Brussels-based initiative helping communities create and govern shared digital tools. We build open-source projects, document them as roadmaps and workshops, and make them easy to replicate with no-code and AI-assisted development.

First-person, two sentences. Best for human-facing contexts where you have more room.

### Catch Phrase

> We create practical open-source projects, turn them into roadmaps and workshops, and help communities replicate them for their own needs.

Used in: website og:description and twitter:description meta tags.

---

## Where Each Format Is Deployed

| Format | Where |
|---|---|
| Wikidata (short) | Wikidata Q138589387 EN + FR |
| SEO one-liner | `movement/SPEC.md` header, `README.md` header, `website/index.html` meta description, `index.html` (root) meta description |
| Pitch bio | LinkedIn (planned), about pages (planned), social profiles (planned) |
| Catch phrase | `website/index.html` og:description + twitter:description, `index.html` (root) og:description + twitter:description |

---

## LLM Validation (March 6, 2026)

Both descriptions were independently tested on GPT-5.4 and another LLM.

**What both LLMs correctly inferred:** civic-tech / digital commons studio, community-governed, Brussels ecosystem, replicable model, mission-driven, process design not just software delivery, public-interest infrastructure.

**On the SEO one-liner as a Wikidata description:** scored 6/10 accuracy, 3/10 fit — "too long, reads promotional, includes activity details that belong in an article." This led to the shorter Wikidata-specific format.

**On the pitch bio:** highest human readability score, best for explaining to someone unfamiliar. Both LLMs flagged the same gaps: unclear who pays, what "digital tools" means concretely, whether the initiative mainly builds, teaches, or advises. These are the questions the website and pitch materials need to answer.

**Conclusion:** each format serves its context. Short for structured data, full for SEO, pitch for humans.

### Website Due Diligence Review (GPT-5.4, March 6, 2026)

A separate LLM review assessed the full website for credibility and movement viability. Key findings:

**On the "cost/barrier collapse" claim:** "Directionally right, but overstated." v0.1 costs have collapsed for bounded tools; maintenance, governance, support, and trust costs have not. Four barrier types identified: technical (reduced), economic (reduced not removed), organizational (still high), distribution/trust (still very high). Website was updated to reflect this nuance — Section 02 now says "building the tool is only 20% of the work."

**On movement probability:**
- Successful as a niche European movement: 35–50%
- Durable ecosystem with working projects and recognizable identity: 20–30%
- Broad mainstream movement comparable to Transition Towns: under 10%

**What would raise the odds:** repeatable product wins, clear ownership rules, and maintainer/support structures within the next year. "Their best shot at success is not becoming 'the future of all software,' but becoming a recognizable European niche movement for community-built local tools."

**Verdict:** "Good diagnosis, inflated rhetoric, plausible niche future, low odds of mass movement." Website copy pass was applied to address the rhetoric inflation and add credibility anchors (GPFC srl, AGPL-3.0, cooperative structure, Build→Document→Replicate method).

---

## Naming: Grassroot → Grassroots

Renamed across the entire repository on March 6, 2026. "Grassroots" is the standard English form (adjective derived from the plural noun). "Grassroot" (singular) was a spelling error. See `docs/plans/2026-03-06-grassroots-rename.md` for the full roadmap including domain strategy and GitHub org rename.

The Wikidata label was updated from "Grassroot Hoppers" to "Grassroots Hoppers" in both EN and FR. Old spelling variants are preserved as aliases for discoverability.

---

## How We Got Here (Decision Log)

### Original description (pre-March 6)

> Brussels-based cooperative movement applying the Transition Towns model to open-source software

### Diagnosis (GPT-5.4)

The old description was too abstract — it told the place, inspiration, and domain but not what the group actually is in practice. Three missing elements: a concrete identity word, the primary activity, and the audience. Core problem: "sounds more like a manifesto than an identification."

It needed: **place + type + action + purpose**.

### Key decisions during revision

| Decision | Rationale |
|---|---|
| "initiative" not "movement" | Honest about current stage (one person). Movement is the aspiration, initiative is today's reality. |
| Dropped Transition Towns reference | Inspiration is real but naming it made it sound derivative. |
| Added "social innovation" | Positions in EU funding vocabulary. User insisted: "can't lose social innovation." |
| "community-owned software and digital commons" | Concrete ("software") + principled ("digital commons"). User flagged "digital tools" as too vague. |
| "workshops, roadmaps" | Names the educational delivery concretely — the Rob Hopkins playbook. |
| "no-code, AI-assisted development" | The frontier method and key discoverability term. |
| Three-format split | GPT-5.4 flagged the full one-liner as too promotional for Wikidata. Led to short/SEO/pitch separation. |

---

## TODO

- [x] Decide entity scope: initiative (not company, not website)
- [x] Julien to review and pick direction for the short description
- [x] Final description approved — three-format strategy
- [x] Update Wikidata entry — English (published by Julien)
- [x] Update Wikidata entry — French (published by Julien)
- [x] Align website copy and SPEC.md identity language with new description
- [x] Rename Grassroot → Grassroots across repo + Wikidata
- [ ] Deploy pitch bio to LinkedIn profile
- [ ] Deploy pitch bio to other social profiles (Fosstodon, X)
- [ ] Create separate Wikidata entries for GPFC srl, Julien Thibaut, Chez Julien (see `2026-03-06-julien-online-presence.md`)
