# Grassroots Hoppers

Brussels-based open-source social innovation initiative helping communities create, govern, and replicate community-owned software and digital commons through workshops, roadmaps, and no-code, AI-assisted development

Grassroots Hoppers is the initiative shell: the public website, manifesto, product strategy, and companion artifacts that explain the operating model behind the products.

This repository is intentionally not the place where product runtime code lives. Product code belongs in separate contributor-ready repositories with their own licenses, docs, issue trackers, and release cadence.

## What Lives Here

- `website/` contains the public site deployed to [grassroothopper.com](https://grassroothopper.com).
- `movement/` contains the manifesto, research references, and strategic framing.
- `products/` contains product concept specs and positioning docs.
- `website/chez-julien-workflow-map.html` is the strategic companion artifact for David Toolkit: an ideal future-state workflow map for Chez Julien.
- `docs/` contains the March 9 to March 13, 2026 hackathon plan, devlog templates, and launch guidance.

## Product Repositories

The first real product now has its own repo:

| Product | Purpose | Repo | License |
| --- | --- | --- | --- |
| David Toolkit | Browser-first retail intelligence demo for small shop owners | [Grassroot-hoppers/david-toolkit](https://github.com/Grassroot-hoppers/david-toolkit) | `AGPL-3.0-only` |

This umbrella repository is licensed under `CC BY-SA 4.0` for docs, narrative, and website content unless a subdirectory states otherwise.

## March 2026 Status

Grassroots Hoppers is no longer just a thesis repo.

- The initiative site is live.
- David Toolkit is moving into a five-day public hackathon from March 9 to March 13, 2026.
- The product runtime now lives in a separate repo.
- The workflow map in this repo shows the operating model David Toolkit is meant to support.

## Open-Source Posture

The standard is explicit:

- no custom “source-available” license during the hackathon
- no hiding the runnable code inside the initiative repo
- no vague “open” claims without docs, setup, and contribution paths

The initiative repo explains the why. The product repo carries the real OSS burden: runnable demo, issues, contribution docs, security policy, and roadmap.

## Build In Public

The hackathon reporting structure lives in [`docs/devlog/README.md`](docs/devlog/README.md).

- Long-form home: [julien.care](https://julien.care)
- Code home: GitHub
- Social amplification: Fosstodon

Launch sequencing for the sprint is documented in [`docs/LAUNCH-PLAYBOOK.md`](docs/LAUNCH-PLAYBOOK.md).

## Website Deployment

GitHub Pages deploys from `website/` through the workflow in `.github/workflows/pages.yml`.

## Contact

- Human: [staycreative@julien.care](mailto:staycreative@julien.care)
- Website: [grassroothopper.com](https://grassroothopper.com)

Good people, for good people.
