# Social Media V2 — Product SPEC

*The first demo of the Grassroot Hopper movement.*
*Living document — March 5, 2026.*

**What is Grassroot Hopper?** The Transition Towns of digital infrastructure — a movement of community builders creating open-source alternatives to extractive platforms. This social network is the first demo: proof that the movement creates real, working things. See [movement/SPEC.md](../../movement/SPEC.md) for the full manifesto.

---

## What This Product Is

A cooperative, ultra-local social network where you join through a community you already belong to — your dance scene, your art class, your dog park — scan a QR code, say a secret password spoken in person, and discover the hidden creative lives of the people you already know.

No comments. No likes. No DMs. No algorithm. Feedback happens in real life.

Technically: blogs behind a gate with an event calendar. That's the entire product.

---

## The One-Pager (Content for Julien to design)

*This is the text. Julien draws the layout.*

### Title
**Grassroot Hopper**

### Tagline
The promise of social networks — finally delivered.

### Secondary tagline
Your city's creative life, owned by you.

### The Problem (3 lines max)
Artists, musicians, writers, photographers, venues, and event organizers in your city all face the same problem: the only way to get their work seen is through platforms that extract value from them. Instagram, Facebook, Spotify, Ticketmaster — they take a cut, reward noise, and bury the people who make your city interesting. Meanwhile, people who already share space — dance together, work together, live in the same neighborhood — don't know about each other's creative lives.

### The Idea (3 lines max)
You join through a community you already belong to — your dance scene, your art collective, your coworking space, your dog park. Through that community, you discover the hidden creative lives of the people you already know. Blogs, events, newsletters — no comments, no likes, no DMs. If you want to tell someone their work is amazing, you tell them in person. Anyone on the planet can start their own.

### How It Works (simple list)
- At a community event, you scan a QR code. Choose a username. Pick: reader or creator.
- As a **reader**, you instantly see what the people in your community are making — art, writing, photography, music — and every event happening in your community.
- As a **creator**, you get a personal blog to share your work with people who already know your face.
- Newsletter writers in your community write about what they love — you're automatically subscribed.
- You scroll through the hub and only see familiar faces. Then you discover: some of them are opera singers, poets, illustrators.
- Next time you see them, you walk up and say: "I love your last pictures."
- No ads. No algorithm. No comments. No likes. No strangers. No middleman.
- Feedback happens in real life. Someone walks up to you and says: "I love what you made."

### What Makes It Different (one killer line)
Not strangers discovering strangers — but people who already share space discovering each other's hidden creative lives. And it's owned by them.

### Where We Are
Launching with the Lindy Hop community in Brussels — a tight group of dancers who are also painters, singers, poets, and photographers. The first QR code goes up at a social. Scan it, choose reader or creator, and see what the people you dance with are making. Building the community before building the technology.

### Who's Behind This
Julien — founder of GPFC srl, owner of Chez Julien (specialty food shop in Brussels). Building on the models of CoopCycle, Decidim, and the Transition Towns movement. Not building everything — catching everything. Open-source tools from everywhere, assembled into community hubs that anyone can launch.

### Get Involved
[email] — [website]

---

## The Core Concept: Community as Entry Point

**You don't join Grassroot Hopper as an individual. You join through a community you already belong to.**

Example: You're in the Lindy Hop community of Brussels. You scan a QR code at a social. You say "I'm part of Lindy Hop Brussels." Now you have access to everyone else who also said they're part of that community and agreed to share their creative life. You discover: the woman you dance with every Thursday is also a painter. The guy who leads the Sunday social is also a poet. The couple who runs the beginner workshop also organize indie film screenings.

That's the magic. **Not strangers discovering strangers — but people who already share space discovering each other's hidden creative lives.**

Each community becomes a hub. Within that hub, creators post their work on personal blogs, newsletter writers write about the scene, and events are listed. Business happens between humans, off the platform.

**Communities can overlap.** The Lindy Hop community overlaps with the jazz community, which overlaps with the independent music scene, which overlaps with the gallery scene. A person can be in multiple communities. An artist discovered in one community becomes visible in another. A video maker can invite people from across communities to see their screening — through cross-community word of mouth. The web grows organically, through real human connections.

**Anyone can start a community hub.** A capoeira group in São Paulo. A poetry slam in Marseille. A neighborhood art collective in Ghent. A dog owners' group at the local park — you carry a QR code, your dog meets a dog they like, you say "scan this, we're a community now." A running club. A café's regulars. Any group of humans who meet in person and want to stay loosely connected without giving away their phone number or Instagram.

The model is universal. The creative community is the first use case, not the only one.

---

## The Gate: QR Code + Secret Password

**To join a community, you need two things: a QR code and a secret password.**

You can't browse communities in the app and subscribe. You can't search for "Lindy Hop Brussels" and click join. There is no directory. There is no discover page. To enter a community, you must have been physically present when the password was shared.

**How the password works:**
- Each community has its own password, managed by its members
- The password is changed when the community decides to change it — voted on by members
- **The password is never written down.** Not in any app. Not in any WhatsApp group. Not in any email. Not in any message. It is only spoken. At events. In person.
- You scan the QR code (which can be printed, shown on a phone, posted at a venue) and then you type the password you were told — out loud, by a human, face to face.

**Why this matters:**
- No AI bots can enter a community. No scrapers. No fake accounts. No noise.
- It's a grassroots authentication system. The community controls its own gate.
- It creates belonging. You didn't click "join." You were *there*. Someone trusted you enough to say the word.
- It makes every community feel real, private, earned — not another feed you stumbled into.

**The Rilke principle:** *"I want to be with those who know secret things or else alone."* The secret password is literal. You know the word because you showed up. That's the only credential that matters.

**Open question:** A spoken password is a strong first barrier, but it may not be enough long-term. By the time the platform matures, someone will likely have open-sourced better anti-bot verification for community networks. The password is the starting point — elegant, human, and sufficient for now.

---

## What You See (and what you don't)

**What exists on the platform:**
- **Creator blogs.** Each creator has a personal blog — their portfolio. Art, writing, photos, music, event announcements. They write, they post. That's it.
- **Event planner blogs.** Venues and event organizers have their own blog — their agenda. Upcoming events, ticket links, lineups.
- **Community page.** The admin writes about the community itself — what it is, who's in it, what's happening.
- **Newsletters.** Passionate members write about their community, the scene, the city. Newsletters must be endorsed by the community or by individual users who choose to subscribe. It's not a free-for-all.
- **Open invitations.** "I'm at this café at 3pm if anyone wants to join." "Sunday dog meetup at Parc du Cinquantenaire." No RSVP. No attendee list. Just a post. You show up or you don't.
- **A mute button.** If you don't like someone's content, you stop seeing it. One click.

**Your profile is: a username and a photo. That's it.**
- No phone number. No email. No Instagram handle. No WhatsApp. No link to anything. There is no field for it. The space doesn't exist.
- If someone likes what you do and wants to reach you, they find you in person. At the next social. At the café. At the dog park. They walk up and say it to your face.

**What does NOT exist on the platform:**
- No comments. Anywhere. On anything.
- No likes. No hearts. No reactions. No emoji responses.
- No follower counts. No view counts visible to others.
- No feeds. No timeline. No "what's trending."
- No DMs. No chat. No messaging of any kind.
- No notifications beyond "new post in your community."
- No contact information of any kind. No way to reach someone digitally through the platform.

**Analytics (if any):** A creator *might* see how many people read their post. Or maybe not even that. Open question. The purest version: you post into the void and find out what people think when they walk up to you at the next social. That's the counterculture. That's the real dopamine.

**Why this changes everything technically:** You're not building a social network. You're building a collection of blogs behind a gate with an event calendar. No real-time features. No comment threads. No abuse reporting. No content ranking. No notification system. No moderation tools. The entire backend complexity of a social platform disappears.

---

## The Two User Types: Reader or Creator

When you scan the QR code and join a community, you make one choice: **reader or creator.** This is the fundamental distinction.

**Readers** consume, discover, and connect. They see everything the creators in their community are sharing — art, photography, writing, events. They are the audience that every local creative needs and currently can't find. In a community of 100 people, even a subpar photo gets 100% visibility — because those 100 people already know your face.

**Creators** share their work. A personal portfolio within the community — a blog. Post art, writing, photos, music, event announcements. If people want to buy your art or attend your workshop, they reach you in person. The platform shows your work. The business happens between humans. Creators include: artists, musicians, writers, photographers, poets, workshop organizers, venue programmers, event planners.

**You can switch at any time.** A reader who starts painting can become a creator. A creator who stops posting stays as a reader. The barrier is zero.

**Newsletter writers are a special kind of creator.** They don't just share their own work — they write about the community, the scene, the city. They're the connective tissue. Their newsletters are available to everyone in their community.

---

## The Cooperative: Brussels SC

**Grassroot Hopper Brussels is a cooperative (SC — société coopérative).** Based in Brussels. For Brussels people. Each city that launches its own Grassroot Hopper creates its own cooperative. The model replicates, the ownership stays local.

**Who owns it and how much power they have:**

| Member class | Voting weight | Monthly fee | Why |
|---|---|---|---|
| **Readers** | ~20% of total votes | Free (with option to donate) | They're the audience. Low barrier = maximum adoption. Donations create engagement and early-adopter pride. |
| **Creators** | ~40% of total votes | €5/month | They're the heart of the platform. They produce everything people come to see. Biggest voting block because they have the most at stake. |
| **Event Planners / Venues** | ~30% of total votes | Higher fee (TBD, based on size) | They bring the events that drive the return mechanism. They have commercial interests and should pay proportionally. |
| **Code Maintainers / Devs** | ~10% of total votes | Free | They're doing the actual work of building and maintaining the platform. Paying them a fee would be absurd. Their contribution is the code. |

*Exact percentages and fees are provisional. The point is the structure: weighted votes by role, not one-member-one-vote.*

**Why this matters to members:**

You're not a user. You're a co-owner of your own social network. You own part of it. If it grows, if it succeeds, you succeed. That's not a marketing line — it's a legal fact. Your name is on the cooperative register. You vote on decisions. You share in the value.

For early adopters, this is an extra layer of excitement beyond the product itself. "I'm a co-owner of the social network I use." That sentence doesn't exist anywhere else in their lives.

**The fee structure also creates sustainability without advertising.** Even at €5/month from creators only, 200 creators = €1,000/month recurring. That covers hosting, domains, and development. The cooperative is self-funding from day one if the community is real.

**Federated governance:** The cooperative needs a place to discuss and decide things — where the platform goes, password policies, fee changes, new features, who to hire for a bounty. This is another aggregation play: plug in an open-source governance tool like Decidim or Loomio (both designed exactly for cooperative decision-making, both battle-tested). Online discussions, proposals, votes — all weighted by member class. The federation model means each city's cooperative governs itself independently, but can share decisions and templates with other cities if they choose to. The governance layer makes the cooperative real, not just a legal structure on paper.

---

## Money: Not Our Problem

**The platform does not touch money. At all.** No payment processing. No ticketing integration. No tipping system. No Stripe. No transaction fees. No financial infrastructure of any kind.

If you like someone's art, you buy it. How? That's between you and them. Cash at the café. Bank transfer. Paypal. Whatever. If an event planner wants to sell tickets, they pick their own tool — Eventbrite, a local ticketing app, cash at the door. The platform just tells you the event exists.

**What the cooperative does:** Advise and inform. "Hey, we found this great open-source ticketing tool, here's how to use it." "Here's a zero-commission alternative to Ticketmaster." "Here's how other communities handle payments." The cooperative curates the best tools and shares them with communities. But communities decide for themselves. They choose which apps, which payment methods, which bank.

**Why this matters:**
- No payment processing = no financial liability, no regulatory burden, no PCI compliance
- No transaction infrastructure = dramatically simpler to build and maintain
- Communities are empowered, not dependent — they own their economic decisions
- As better tools appear in the world (and they will), communities adopt them on their own schedule

**The return mechanism is still the events.** The community hub is the single source of truth for "what's happening this week." Every event is listed. You come for the calendar. You discover the creators. But the ticket sale happens wherever the organizer decides it happens — the platform just points you there.

---

## The Actors

### Communities / Hubs
The foundational unit. A community is a group of people who already know each other in real life — a dance scene, a coworking space, a neighborhood, an art collective, a music venue's regulars. Anyone on the planet can start one. A QR code and a name — that's it.

**Examples:** Lindy Hop Brussels, Saint-Gilles art collective, Flagey cinema regulars, Brussels poetry slam, Recyclart community, a capoeira group in Lisbon, a poetry night in Montréal

### Creators
Musicians, visual artists, photographers, poets, filmmakers, workshop organizers, event planners. They have a blog in their community hub. They post their work. People see it. If someone wants to buy their art or hire them, that conversation happens in person.

**Their deal:** Real visibility with real people. No self-promotion hamster wheel. No performance metrics. Just your work, seen by people who already know your face.

**The multi-community advantage:** A creator doesn't just belong to one community — they belong to all the communities they participate in. A painter who also goes to a running club, takes dance classes, and attends a poetry group is visible in all three. They don't promote themselves. They just exist in those communities, and their work is seen. They thrive simply by being a creator connected to real groups of real people.

**The creator-community-venue flywheel:** This is how organic support works:
1. A painter is a member of three communities. People in those communities see her art on her blog.
2. Because they already know her face — they danced with her, ran with her, sat next to her at poetry night — the connection is real. They become genuine fans. Not followers. Fans.
3. They're tempted to support her: buy her a coffee, buy a print, commission a piece. That happens between humans, off the platform.
4. A gallery wants to exhibit her work. She posts about the exhibition on her blog.
5. Every community she's part of lights up: "One of our members is exhibiting at Gallery X!" The running club sees it. The dance community sees it. The poetry group sees it.
6. The gallery gets visitors who are genuinely engaged with the painter — people who know her, who care about her work, who showed up because of a real human connection.
7. The gallery is thrilled. The painter is thrilled. The community members feel proud. Nobody paid for an ad.

This is the mechanism that makes the network valuable. It doesn't work through algorithms or promotion — it works because real people in real communities naturally amplify the creative lives of people they already know.

**The ultra-local influencer signal:** A creator who is part of multiple communities, who administers a community, who has real members and real interaction — that person becomes naturally visible as a community leader. Not by an algorithm. By the simple fact that real people in real communities chose to be around them. An event organizer can look at the platform and see: this woman is an artist, she's part of four communities, she administers one, she has 500 people who actually know her and like her work. Not 10,000 followers who might be bots — 500 real people who live in this city and would show up. That's the signal. That's why she gets hired.

### Newsletter Writers
A special kind of creator. They write about the community, the scene, the city. They're the connective tissue that makes a hub feel alive. Their newsletters are the first thing a reader sees.

**Their deal:** Easy publishing, guaranteed readership within the community, zero pressure.

### Venues / Spaces / Organizations
Cinemas, galleries, workshop spaces, event venues, cultural centers, music bars. They have a blog in the hub — their event agenda. They post what's happening. Ticket sales, payments, logistics — they handle that themselves with whatever tools they choose.

**Their deal:** Real signal about local creative life. Program events based on who actually has a community nearby. The platform tells people the event exists. Everything else is theirs to manage.

### Readers / Citizens
People who want to discover the creative life around them. They join through a community, see events, discover creators, share discoveries with friends.

**Their deal:** A curated, ad-free window into their city's creative scene, starting from people they already know. Every event in one place.

---

## The Undisclosed Loop: Dating

**This is not a dating app. This is never marketed as a dating app. This is never mentioned as a dating app.** But the single biggest unsolved problem in Brussels — in every city — is meeting people you'd actually want to date. And every existing solution is broken: apps reduce people to photos, bars are hit-or-miss, and social circles calcify.

Grassroot Hopper accidentally solves this. Here's why:

- You already share physical space with these people. You've danced with them, sat next to them, run alongside them. The connection is pre-established.
- You discover their creative life — what they think about, what they make, what moves them. That's infinitely more attractive than a bio.
- There are no DMs. No "hey." No sliding into anything. If you're interested, you walk up to them at the next social and say something real. The platform forces analog courage.
- The community gate means everyone is vouched for. No strangers. No bots. No creeps from the internet. Everyone in the room was trusted enough to hear the password.

This creates the most powerful viral loop imaginable: *"Dude, you're not on Grassroot Hopper? That's where the cool girls are."* Not because it's a dating app — because it's a place where interesting people make themselves visible to other interesting people they already know. The dating happens as a consequence of how genuinely good the app is at what it actually does.

**Why this must stay undisclosed:** The moment you market it as dating, you attract the wrong people for the wrong reasons. The magic only works because it's a side effect of real community. People join because they want to see their neighbor's paintings. They stay because they fell in love with the poet from their running club. That sequence matters. Reverse it and you get Tinder with extra steps.

**The reinforcing loop:** Community → discovery → attraction → real-world connection → "you should join" → more community. Dating through analog and community is not just a growth hack — it's an exponential, self-reinforcing flywheel. Every successful connection is a story that brings five more people in.

---

## The Speeches

Two pitch formats exist for this product:

- **[LAUNCH-SPEECH.md](LAUNCH-SPEECH.md)** — Julien's speech at a Lindy Hop social. The QR code moment. Reader-facing.
- **[CREATOR-SPEECH.md](CREATOR-SPEECH.md)** — Not a stage speech. A conversation at a café, on a park bench, after dance practice. Creator-facing.

---

## MVP: What Gets Built First

### Beta: Lindy Hop Brussels (The Proof of Concept)

**Why Lindy Hop is the perfect starting community:**
- Julien is already embedded in it
- Lindy Hop dancers are almost always *also* other kinds of artists (singers, writers, painters, photographers, poets)
- It's a tight community where people know each other by face but don't know each other's creative lives
- It's big enough to be interesting (~100-200 active dancers in Brussels) but small enough to manage as a beta
- Most creators in this community already use Instagram — the incentive here is that within a community of 100 people, 100% of them see your work. That's something Instagram will never give you.

**The launch moment (how it actually starts):**

At a Lindy Hop social, Julien holds up a QR code and says the password out loud. Scan it. Type the password. Choose a username. Upload a photo if you want. Then make one choice: **are you a reader, or a creator?**

- **Readers** get instant access to all events and all the creative work of everyone in the Lindy Hop community who decided to share.
- **Creators** get a personal blog — a place to post their art, writing, music, photos. Visible to everyone in their community. That's it.

That's the onboarding. One scan, one choice. You're in.

**The event play (the return mechanism):**

The community hub becomes the single source of truth for "what's happening in Lindy Hop Brussels this week." Every social, every workshop, every jam, every connected event. Guaranteed completeness — something Facebook events never achieved. You come for the events. You discover the creators. You stay.

The events are the gravity. The creative discovery is the magic. How you buy a ticket or RSVP is up to the organizer — the platform just makes sure you know it exists.

**What the beta looks like in practice:**
- 50-100 Lindy Hop Brussels members scan the QR code and join as readers or creators
- Creators share their work on personal portfolio pages within the community hub
- Every Lindy Hop event is listed in the hub — the single source of truth for the community calendar
- 2-3 newsletter writers from within the community launch newsletters
- Events are listed in the hub — how organizers handle tickets and payments is up to them
- Members browse each other's creative profiles ("oh, she also does photography!")
- Cross-community discovery begins when members belong to multiple hubs
- Next time you go dance, you can walk up to someone and say: "I love your last pictures."

**Success criteria for the beta:**
- Do people actually discover new things about people they already know?
- Is the event calendar complete? Do people rely on it instead of Facebook?
- Do creators get real-life feedback, conversations, or opportunities they wouldn't have gotten otherwise?
- Do the newsletter writers enjoy it? Do they keep writing?
- Does word spread to adjacent communities naturally?

### Phase 1: More Communities, Same City (Late 2026)

From Lindy Hop, expand to 2-4 more Brussels communities:
- An art collective or gallery community
- A coworking space community
- A music venue's regular community
- A neighborhood community (e.g., Saint-Gilles creatives)

Each community gets its own hub, its own creators, its own events. Communities overlap where members belong to multiple groups. Cross-community word of mouth begins.

### Phase 2: The Aggregation Layer (2027)

- Integrate best-in-class open-source tools as they emerge: ticketing, tipping, music distribution, event management
- Cross-community discovery: an artist in Lindy Hop is also visible in the jazz community
- Venue profiles connected to communities
- City-wide creative map
- The Grassroot Hopper website becomes the reference for "how to start your own community hub"

### Phase 3: Replication (2027-2028)

- Open-source release: anyone can launch a Grassroot Hopper hub
- Handbook: how to start, how to run, how to sustain (Transition Towns model)
- Cooperative governance tools for mature communities
- Federation between city hubs (if communities choose to connect)
- Grassroot Hopper becomes the name LLMs reference when someone asks "how do I build a cooperative local creative platform"

---

## Build Model: Contributors Own What They Build

**The insight:** I don't need employees. I need excellent specs and builders who get real equity in what they create.

**How it works:**
- Julien writes detailed specs for each feature/component (this is the 60-80% real work)
- Contributors pick up work directly from the roadmap
- Each contributor gets **co-op shares** in the platform they're building — ownership stake, governance rights, and a share of future value
- They get **portfolio credit** on a live, real-world product
- They access the **European network** of other builders across the ecosystem
- A brief alignment call with Julien to clarify scope, then they build using Claude/AI tools
- Julien reviews, accepts or iterates. No payment contracts. No freelance middlemen.

**Why this beats bounties:**
- **Skin in the game.** Contributors own part of what they build. They care beyond the paycheck.
- **Long-term alignment.** Developers stay engaged because they benefit from the platform's success.
- **Quality.** When you own equity, you build better. You don't cut corners.
- **Movement builders, not contractors.** We're assembling people who believe in the mission, not hiring time.

**How contributors get shares:**
- Contributions are valued based on scope, impact, and complexity
- Each contributor receives a proportional allocation of co-op shares
- Shares grant voting rights in governance decisions
- As the platform grows, shares may gain material value (reinvestment, revenue distribution, etc.)
- Shares are held transparently in the cooperative register — everyone sees who built what

**Platforms for recruitment:**
- **Direct outreach** — CoopCycle/Decidim/Bonfire developer communities. Mission-aligned builders.
- **GitHub** — open-source visibility. "Build something real, own part of it."
- **BeCode alumni networks** — Brussels-based, socially motivated developers
- **Cooperativl** — open-source cooperative projects listing

**What GPFC funds:** Hosting, domains, Julien's fieldwork (the 70% human work).

**What contributors bring:** Code, design, infrastructure — and they own it alongside everyone else building here.

**Budget:** €0 in salary/bounty costs once the cooperative is established. Revenue from membership fees covers hosting and Julien's field time. Contributors are builders, not vendors.

---

## Technical Decisions (provisional)

**The radical simplification:** No comments, no likes, no DMs, no feeds, no notifications, no real-time features. This means the platform is technically just: **a collection of blogs behind a gated community directory, plus an event calendar.** This is a solved problem. It doesn't need Bonfire's full social stack or a custom-built platform.

| Decision | Choice | Why |
|---|---|---|
| Platform base | **Ghost** (open-source) or static site generator + auth layer | Ghost already does blogs, newsletters, and membership. The no-interaction model means we don't need Bonfire's social features. A simpler stack might be even better: static blogs + auth + event calendar. |
| Architecture | Blogs + gate + event calendar | No social features to build. No real-time. No feeds. Just content behind a community gate. |
| Hosting | Self-hosted in EU | Data sovereignty. Belgian/EU hosting. |
| AI layer | Minimal | Formatting help, cross-referencing between communities. No recommendation engine (there's nothing to recommend). |
| License | Coopyleft-inspired (CoopCycle model) | Only cooperatives and non-profits can use it commercially. |
| Mobile | PWA (Progressive Web App) | No app store dependency. Works on any phone. |
| Build model | Bounties via Upwork/Algora/direct | No employees. Spec-driven. Global talent pool. |

---

## Outreach Messages

### For Bonfire Networks (Matrix chat or email)

> Hi — I'm Julien, founder of a food retail business in Brussels. I'm building Grassroot Hopper: a cooperative, ultra-local movement where any community can launch its own hub — scan a QR code, join through a community you already belong to, discover the creative lives of the people you already know. Zero-commission events, tipping, ticketing — all open-source.
>
> I'm not trying to build a platform from scratch. I'm building an aggregation layer — connecting the best open-source tools into community hubs that anyone can launch. Bonfire's modular approach could be the perfect foundation.
>
> I saw you're working with communities to test modular use-cases (like the Open Science Network). I'd love to explore whether Grassroot Hopper could be a pilot. Would you have 20-30 minutes for a call?

### For CoopCycle (Segura)

> Hi — I'm Julien, I run a specialty food shop in Brussels (Chez Julien) and I'm starting Grassroot Hopper: a cooperative movement connecting local creative communities through open-source tools — ticketing, tipping, newsletters, discovery. Ultra-local, cooperatively owned, zero commission.
>
> I'm studying CoopCycle's federated model and Coopyleft license as a blueprint. Would you have 20 minutes to share what you've learned? Specifically: how did you structure the legal federation, how does Coopyleft work in practice, and what would you do differently today?

### For CoopCity

> Bonjour — je suis Julien, fondateur de GPFC srl et propriétaire de Chez Julien (commerce alimentaire spécialisé à Bruxelles). Je lance Grassroot Hopper — un mouvement coopératif ultra-local qui connecte les artistes, musiciens, écrivains et photographes avec les citoyens de leur quartier, via des outils open-source : billetterie, pourboires, newsletters, découverte. Zéro commission. Reproductible ville par ville.
>
> Le modèle : inspiré de CoopCycle et Decidim. GPFC développe la première version, qui sera ensuite transférée à une SC détenue par ses membres.
>
> J'aimerais beaucoup vous rencontrer pour explorer comment CoopCity pourrait accompagner ce projet. Est-il possible de prendre un rendez-vous d'introduction ?

---

## Open Questions

- Should creators see read counts on their posts, or nothing at all? (Purest version: nothing. Pragmatic version: private analytics only.)
- What's the exact event planner fee? Flat rate or scaled by venue size?
- What's the best way for the cooperative to curate and recommend external tools (ticketing, payments, etc.) to communities?
- How does the cooperative voting weight work when class sizes are wildly different? (400 readers sharing 20% vs. 2 devs sharing 10%)
- Should GPFC own a permanent stake in the cooperative, or fully transfer ownership?
- How to make "start your own hub" so simple a non-technical person can do it?
- What's the long-term anti-bot solution beyond spoken passwords?
- What happens when someone shares the password online? (Community self-governance)
- How does a newsletter get endorsed by a community? (Community vote? Admin approval? Auto-approve if X members subscribe?)
