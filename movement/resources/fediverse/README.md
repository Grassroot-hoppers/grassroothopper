# Fediverse & Federated Social

## What it is

The Fediverse is a network of interconnected, independently operated social platforms that communicate via the ActivityPub protocol. Mastodon is the most well-known, but the ecosystem includes Pleroma, Pixelfed (photos), PeerTube (video), Lemmy (forums), and — most relevant to us — **Bonfire Networks**.

## What Grassroots Hopper learns from it

**Bonfire Networks is the most relevant project.** A modular ActivityPub toolkit, EU-funded (NLnet/NGI0), shipped v1.0.1 in January 2026. Bonfire lets communities build customized social experiences from modular components. They're actively seeking pilot communities — Grassroots Hopper could be one.

**Modularity matters.** Bonfire's approach of composable extensions (add what you need, remove what you don't) maps perfectly to Grassroots Hopper's "aggregate, don't build" philosophy. We don't need the full social stack — we need blogs + gate + calendar. Bonfire might let us build exactly that.

**Federation is optional, not mandatory.** A single Grassroots Hopper community doesn't need to federate with anyone. Federation becomes useful when multiple cities want to connect — and even then, it's opt-in. The Fediverse shows that federation works, but also that it adds complexity. Start local, federate later.

**ActivityPub as the protocol layer.** If Grassroots Hopper instances use ActivityPub under the hood, communities could theoretically connect with the wider Fediverse. But this is a future consideration, not a launch requirement.

## Key links

- Bonfire Networks: https://bonfirenetworks.org
- Bonfire GitHub: https://github.com/bonfire-networks
- Bonfire Matrix chat: https://matrix.to/#/%23bonfire-networks:matrix.org
- ActivityPub spec: https://www.w3.org/TR/activitypub/
- Fediverse overview: https://fediverse.info

## Bonfire — potential partnership

Bonfire is seeking community pilots for modular use-cases. Grassroots Hopper's stripped-down "blogs behind a gate" model could be an interesting test case for their modular system. Outreach message is in SPEC.md.

## Open questions

- Can Bonfire's modular system support our "no interactions" model? (Remove comments, likes, DMs at the module level)
- What's the overhead of running a Bonfire instance vs. a simpler static setup?
- Is ActivityPub federation useful for cross-city Grassroots Hopper connections, or overkill?
- How mature is Bonfire's documentation and deployment story?
