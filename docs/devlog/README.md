# Hackathon Devlog

This folder is the reporting spine for the David Toolkit hackathon running from March 10 to March 14, 2026.

## Format

Each day gets:

- one short progress note
- one screenshot or GIF
- one honest line about what changed in the plan

The sprint ends with one retrospective.

## Publishing Surfaces

- `julien.care`: long-form reflection and founder story
- GitHub: canonical code/project home
- Fosstodon: short social amplification

## Source Files

The generator reads these markdown files directly:

- [`day-1.md`](day-1.md)
- [`day-2.md`](day-2.md)
- [`day-3.md`](day-3.md)
- [`day-4.md`](day-4.md)
- [`day-5.md`](day-5.md)
- [`retrospective.md`](retrospective.md)

## Publishing Rules

- `status: draft` keeps a page in markdown only. It is not linked or published to `website/hackathon/`.
- `status: live` publishes the page and marks it as the current public entry.
- `status: done` publishes the page as completed.
- GitHub Pages installs `requirements.txt` and runs `python scripts/build-hackathon.py` on every push to `main`.

## Posting Discipline

- Write the daily note after shipping, not before.
- Keep the GitHub note concise and factual.
- Put the best screenshot at the top.
- If the day slipped, say what slipped and why.
