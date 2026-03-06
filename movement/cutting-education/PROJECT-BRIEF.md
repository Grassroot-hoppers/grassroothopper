# Cutting Education — Project Brief

*Internal project under Grassroots Hopper · GPFC srl · March 2026*

---

## The Idea

The technical barrier to building software is collapsing — that's the Grassroots Hopper thesis. But knowing the barrier is collapsing and actually walking through it are two different things. Most people still don't believe they can build software. They've never seen it happen. They've never done it themselves.

**Cutting Education is the bridge.** It's a teaching initiative that takes normal people — not developers, not engineers — and walks them through building real, working apps using AI-assisted tools. Not tutorials. Not theory. Building things together, live, from scratch.

The name is deliberate: we're cutting through the mystique of software creation. We're cutting the education gap between "I have an idea" and "I shipped it." And we're doing it as a visible, public part of the Grassroots Hopper initiative — proof that this works, that the thesis is real, that anyone can do this.

Content for the initiative will be generated through workshops, recordings, and documentation.

---

## Why This Matters for Grassroots Hopper

The initiative needs believers. Not people who nod at the thesis, but people who've experienced it firsthand — who've gone from zero to a working app and felt what that unlocks. Every person who builds something through Cutting Education becomes a natural evangelist for the initiative. They don't need convincing anymore. They've lived it.

Cutting Education serves three purposes simultaneously:

1. **Recruitment.** Every workshop participant is a potential Grassroots Hopper. They arrive curious; they leave capable. The best ones stick around and start building real products for the initiative.

2. **Proof of concept.** Every app built in a workshop is tangible evidence that the thesis works. These aren't demos built by Julien — they're apps built by regular people in real time. That story is compelling for press, for funding applications, for community talks.

3. **Content engine.** Every live session, every workshop, every app built together generates material — recordings, write-ups, open-source repos, social posts. This feeds the initiative's visibility without requiring a separate content strategy.

**Initiative conversion** metrics will track how many workshop participants eventually contribute to Grassroots Hopper products.

---

## The Format

### Workshops

In-person or hybrid sessions (2–4 hours) where a small group builds an app together from start to finish. One facilitator (Julien or a trained Grassroots Hopper), one shared screen, one project. Participants follow along on their own machines, ask questions, make decisions together.

The workshop is structured around a real person's real idea — not a contrived exercise. Someone in the room (or on the call) has a problem they want solved, and the group builds the solution together. This is what makes it compelling: the stakes are real, the outcome is useful, and the person whose idea it is walks away with something that actually works.

Target group size: 5–15 people. Small enough for real interaction, large enough to feel like an event.

### Live Sessions

Shorter, more casual formats — 1–2 hours, streamed or recorded. These could be:

- **Build-alongs:** Julien or a Grassroots Hopper builds something live, narrating the process, taking audience suggestions.
- **Idea-to-app sprints:** Someone submits an idea beforehand, and the session is dedicated to building it from scratch.
- **Debug parties:** Bring your half-finished project, and the group helps you get unstuck.

### Game Jams

The flagship format. A game jam is inherently exciting — it has a deadline, a creative constraint, and a playable result at the end. Building simple video games is the perfect teaching vehicle because games require UI, logic, data, design, and creativity all at once. And people actually want to play what they build.

Game jams could be:

- **Themed weekends:** 48-hour jam around a theme ("community," "local food," "Brussels"). Teams of 2–3 build small browser games.
- **Workshop games:** Single-session workshops where the group builds one game together (a quiz, a platformer, a card game, a local trivia game).
- **Monthly challenges:** Ongoing, asynchronous — build a game this month around a theme, share it, vote on favorites.

---

## Pilot Project: Lucas's French Dubbing Explorer

### The Person

Lucas is an employee at GPFC. He's not a developer. He watches a lot of TV series, anime, and movies in French dubs, and he's fascinated by the voice actors behind the characters. He's noticed that certain French dubbing actors voice dozens of different characters across wildly different shows, and he wants a way to explore and navigate this.

### The App Idea

**VoixFR** (working title) — a searchable app that maps French dubbing actors to the characters and shows they've voiced. The core experience:

- **Search by actor:** Type a French dubbing actor's name, see every character they've voiced across TV, anime, and film.
- **Search by character/show:** Look up a show or character, see who voices them in French.
- **Discover connections:** "The person who voices Naruto in French also voices this character in Breaking Bad" — the surprising overlaps are the fun part.
- **Voice actor profiles:** Photo, bio, notable roles, career timeline.

### Why This Is a Perfect Teaching Project

Lucas's app is ideal for a first Cutting Education workshop because:

- **It's personally motivated.** Lucas genuinely wants this. He's not doing homework — he's building something for himself.
- **It's relatable.** Anyone who watches dubbed content has wondered about the voices. The concept needs zero explanation.
- **It's technically complete.** The app touches every fundamental skill: data sourcing, data modeling, UI design, search functionality, responsive layout. It's a real app, not a toy.
- **It's scopeable.** You can build a meaningful MVP in a single workshop session (a searchable list with basic data), then extend it over subsequent sessions (richer data, better UI, community contributions).
- **It's showcaseable.** A working French dubbing explorer is the kind of thing people share — "look what I built" material.

### Data Sources

French dubbing data is scattered but findable:

- **Behind The Voice Actors** (behindthevoiceactors.com) — the largest English-language database, includes French voice actors for many titles.
- **Doublage Québec / RS Doublage** — French-language dubbing databases with actor-to-role mappings.
- **Wikipedia** — many anime and series pages list French voice cast in the dubbing section.
- **Manual curation** — for the MVP, starting with a hand-curated dataset of Lucas's favorite shows is faster and more accurate than scraping.

### Suggested MVP Scope (One Workshop Session)

Build a React app with:

- A curated JSON dataset of ~20 French dubbing actors and their roles across ~30 shows
- A search bar that filters by actor name, character name, or show title
- Actor profile cards showing their roles
- Show pages listing the French voice cast
- Clean, mobile-friendly design

This is achievable in a 3–4 hour workshop with AI-assisted development, and it produces something Lucas can actually use and share.

### Extension Roadmap (Subsequent Sessions)

- Session 2: Expand the dataset — scraping or API integration, add images
- Session 3: Add "surprise me" feature — random connections, "did you know" facts
- Session 4: Community contributions — let users submit corrections or missing data
- Session 5: Audio samples — link to clips where possible, so you can actually hear the voices

---

## Timeline and Milestones

### Phase 1 — Internal Pilot (March–April 2026)

- Build Lucas's app as the first internal workshop
- Document the process thoroughly (notes, screenshots, decisions, mistakes)
- Record the session if possible — raw material for future content
- Outcome: one working app, one documented workshop template

### Phase 2 — First Public Workshop (May–June 2026)

- Host the first external workshop in Brussels
- Use the documented template from Phase 1
- A new participant's idea becomes the project
- Outcome: proof that this format works with strangers, not just employees

### Phase 3 — First Game Jam (Summer 2026)

- Organize a themed weekend game jam (in-person in Brussels, remote participants welcome)
- Theme tied to Grassroots Hopper values — community, local, cooperative
- Outcome: 3–5 playable browser games, content for the movement, energy and visibility

### Phase 4 — Repeatable Format (Autumn 2026)

- Monthly workshops (alternating in-person and online)
- Quarterly game jams
- Begin training other Grassroots Hoppers to facilitate
- Outcome: Cutting Education runs without Julien being in every room

---

## Resources Needed

**Minimal to start.** That's the point — if we need a big budget to teach people that building software is easy, the message is already broken.

- A room with WiFi and a projector (GPFC office, a community space, a café)
- Participants with laptops
- A facilitator who knows the AI tools
- A Notion or GitHub space to share templates, datasets, and repos
- Optional: streaming setup for remote participants (a laptop with OBS is enough)

**Funding opportunities:** This format maps directly onto several Brussels and EU funding categories — digital literacy, social innovation, open-source education, cooperative development. Innoviris, Actiris training subsidies, and Digital Belgium Fund are all relevant.

---

## Success Metrics

- **Apps built:** Number of working apps produced through workshops and jams
- **Participants:** Number of people who've attended at least one session
- **Repeat participants:** People who come back for a second session (the real signal)
- **Initiative conversion:** Participants who go on to contribute to Grassroots Hopper products
- **Content generated:** Workshop recordings, write-ups, repos published
- **Press and visibility:** Mentions, invitations to speak, partnership inquiries

---

## Relationship to the Initiative

Cutting Education is not a product — it's an arm of the initiative. It sits alongside the products (Social V2, David Retail) as one of the ways the Grassroots Hopper initiative grows and proves its thesis.

Content for the initiative will be generated through these workshops and sessions.

The products prove that communities can own their own tools.
Cutting Education proves that anyone can build them.

Together, they're the complete argument.

---

*This brief is a living document. It will change as we run the first sessions and learn what works. That's the point.*
