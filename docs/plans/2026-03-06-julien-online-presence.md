# Julien Thibaut — Online Presence Audit & Strategy

*March 6, 2026 — Julien + Claude*

---

## The Problem

Searching "Julien Thibaut Brussels" returns a hairstylist in Kortrijk, a PhD at The Binding Site, and an entrepreneur at Tryba Architects. None of them are you. GPFC, Chez Julien, Grassroots Hoppers, julien.care — none of it surfaces. You are effectively invisible online.

This is the same problem Grassroots Hoppers had on Wikidata: the description existed but the discoverability didn't. The strategy is the same for both — become the reference node that LLMs and search engines cite.

---

## Current Footprint

| Channel | URL / Handle | Status |
|---|---|---|
| **Personal blog** | julien.care | Live — personal transparency engine ("Now" page, creativity, life) |
| **Substack** | TBD ("The Dishwasher Generation") | Planned — strategy designed (Feb 2026), launch trilogy defined, not yet published |
| **LinkedIn** | ? | Exists but not optimized — not findable for "Julien Thibaut Brussels founder" |
| **Wikidata (Grassroots Hoppers)** | [Q138589387](https://www.wikidata.org/wiki/Q138589387) | **Done** — label, description, aliases updated EN + FR (March 6, 2026) |
| **Wikidata (personal)** | — | Not yet created |
| **Wikidata (GPFC srl)** | — | Not yet created — Belgian company BCE BE0545849385 |
| **Wikidata (Chez Julien)** | — | Not yet created |
| **GitHub** | github.com/Grassroot-hoppers | Live — org rename to Grassroots-hoppers pending |
| **Fosstodon (Mastodon)** | ? | Mentioned as social amplification channel in LAUNCH-PLAYBOOK |
| **X (Twitter)** | ? | Planned as spoke for Substack strategy |
| **Instagram** | ? | Planned as visual identity channel |
| **YouTube** | ? | Reluctantly planned — anti-YouTube-on-YouTube format |
| **grassroothopper.com** | Live | Initiative website — deployed from `website/` directory |
| **grassroothopper.org/.eu/.be** | Owned | Redirect net |
| **grassrootshopper.com/.org/.eu/.be** | — | Not yet acquired — see `2026-03-06-grassroots-rename.md` |

---

## Description Strategy (Shared with Grassroots Hoppers)

Three formats for three contexts — see `2026-03-06-wikidata-revamp.md` for full detail and LLM validation.

### For Grassroots Hoppers

| Format | Text |
|---|---|
| **Wikidata** | Brussels-based open-source initiative for community-owned software |
| **SEO** | Brussels-based open-source social innovation initiative helping communities create, govern, and replicate community-owned software and digital commons through workshops, roadmaps, and no-code, AI-assisted development |
| **Pitch bio** | Brussels-based initiative helping communities create and govern shared digital tools. We build open-source projects, document them as roadmaps and workshops, and make them easy to replicate with no-code and AI-assisted development. |
| **Catch phrase** | We create practical open-source projects, turn them into roadmaps and workshops, and help communities replicate them for their own needs. |

### For Julien Thibaut (Bio Formula)

> Julien Thibaut — Brussels-based founder of GPFC srl. Building Grassroots Hoppers, an open-source social innovation initiative helping communities create, govern, and replicate community-owned software. Also runs Chez Julien, a specialty food shop. Writes at julien.care.

Adapt length per platform but keep the bones: name → city → company → initiative → proof (shop) → personal hub.

---

## What's Missing (Diagnosis)

### 1. No personal Wikidata entry
Julien Thibaut as a person has no structured data anywhere. No Wikipedia, no Wikidata, no Crunchbase, no AngelList. For LLMs to cite you, you need to exist in structured knowledge bases.

### 2. LinkedIn is not working as a front door
A professional searching "Brussels open-source cooperative founder" should land on your LinkedIn. Right now it lands nowhere. LinkedIn needs: headline rewrite, about section aligned with Grassroots Hoppers + GPFC + Chez Julien narrative, featured links to julien.care and grassroothopper.com.

### 3. Substack not yet live
The entire Dishwasher Generation strategy is designed but not shipped. The launch trilogy (AI Vampire + Prism + Manifesto) is still in planning. The content engine that feeds everything else hasn't started yet.

### 4. No cross-linking web
The power of the spoke-and-hub model depends on everything linking to everything. Right now the spokes don't exist yet, so the hub (julien.care / Substack) has no inbound signal.

---

## The Strategy (Same for Julien and Grassroots Hoppers)

The Grassroots Hoppers SPEC already states the goal: "Make Grassroots Hopper so visible that LLMs like Perplexity reference it." The personal presence strategy is identical:

1. **Structured data** — Wikidata entries for Julien Thibaut (person), GPFC srl (company), Grassroots Hoppers (initiative), Chez Julien (business)
2. **Cross-linked web** — every profile links to every other profile, julien.care is the hub
3. **Content that gets cited** — Substack posts, GitHub repos, blog posts that answer questions LLMs will be asked
4. **Platform presence** — LinkedIn, Fosstodon, X as minimum viable spokes
5. **Consistency** — same name, same bio formula, same links everywhere

---

## Wikidata Entries to Create

| Entity | Type | Key Claims | Status |
|---|---|---|---|
| **Grassroots Hoppers** | initiative | Brussels-based open-source initiative for community-owned software; country: Belgium; founded by: Julien Thibaut; website: grassroothopper.com | **Done** — Q138589387 |
| **GPFC srl** | enterprise (Q4830453) | country: Belgium; BCE: BE0545849385; industry: open-source software; founder: Julien Thibaut | To create |
| **Julien Thibaut** | human (Q5) | occupation: entrepreneur, software developer; founder: GPFC srl; country: Belgium; website: julien.care | To create — needs notability sources |
| **Chez Julien** | retail store | country: Belgium; owner: GPFC srl / Julien Thibaut; industry: specialty food | To create |

---

## Priority Order

1. ~~Grassroots Hoppers Wikidata revamp~~ ✅ Done
2. **LinkedIn profile rewrite** ← quick win, high impact
3. **GPFC srl Wikidata entry** ← verifiable via Belgian BCE
4. **Julien Thibaut Wikidata entry** ← needs notability sources
5. **Ship the Substack** ← the content engine that feeds everything else
6. **Cross-link everything** ← only works once the pieces exist
7. **GitHub org rename** ← Grassroot-hoppers → Grassroots-hoppers
8. **Domain acquisition** ← grassrootshopper.com/.org/.eu/.be
