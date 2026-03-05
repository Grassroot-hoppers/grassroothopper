# "Makes You More Social" Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add Valentina and Arnaud personas to the social-v2 pitch deck and SPEC, reinforcing the "makes you more social" thesis throughout.

**Architecture:** Content-only changes across two files: the pitch deck (`website/social-v2.html`) and the product spec (`products/social-v2/SPEC.md`). No new files. No structural changes to the site. The pitch deck gets one new slide, one flywheel coda, two persona cards, and tagline refinements. The SPEC gets one new section.

**Tech Stack:** Vanilla HTML/CSS (pitch deck), Markdown (SPEC). No build tools.

---

### Task 1: Add Valentina's slide to pitch deck

**Files:**
- Modify: `website/social-v2.html` (insert new section between slide 05 "Who is this great for?" and slide 06 "How a painter fills a gallery")

**Step 1: Write the Valentina section HTML**

Insert a new `<section class="slide dark">` after the closing `</section>` of slide 05 (the personas slide, line ~1357). Use the existing visual language: `reveal` class, `slide-num`, stagger animations. Use a structure similar to Clara's flywheel but shorter (6 steps).

Content for the section:

- Slide number: no number (use `—` like the "other demo" slide, or fit between 05 and 06)
- Headline: `Valentina moved to Brussels three weeks ago.`
- Avatar: similar to Clara's `fc-avatar` but with a different emoji (biking or dancing)
- Trait badges: biking, soccer, salsa (small inline badges)
- 6 narrative steps:
  1. Valentina is from South America. She just moved to Brussels. She loves biking, plays soccer, and dances salsa.
  2. She goes to a salsa night. Has a great time. Someone says: "You should be on the app. Here, scan this."
  3. She goes home, creates an account — and can't stop scrolling. All these people she was dancing with tonight — one is a painter, another is a photographer, another organizes jazz nights. She had no idea.
  4. Wait — that guy looks like he's in a soccer team. She needs to ask him about it at the next salsa class.
  5. The next salsa class is tomorrow. She knows because the app has every event. She still has to earn those phone numbers the organic way — dance a little more, show up a few more times. It's not instant connection.
  6. But now she has so many things to say. So many reasons to walk up to someone. The gap between "stranger" and "someone I want to know" just collapsed.
- Result box: "Three weeks in a new city. Already surrounded by people." / detail: "The app didn't connect her. It gave her reasons to connect herself."

CSS: Reuse existing classes (`fc-center`, `fc-avatar`, `fc-story`, `fc-step`, `fc-marker`, `fw-result`). May need a new avatar gradient or emoji. Minimal new CSS.

**Step 2: Verify in browser**

Open `website/social-v2.html` in browser. Scroll to the new section. Check:
- Reveal animation works
- Stagger animation on steps works
- Result box renders correctly
- Responsive on mobile (check at 375px width)

**Step 3: Commit**

```bash
git add website/social-v2.html
git commit -m "feat(social-v2): add Valentina newcomer story to pitch deck"
```

---

### Task 2: Add Arnaud's coda to Clara's flywheel

**Files:**
- Modify: `website/social-v2.html` (insert Arnaud's arc after Clara's `fw-result` box, still inside slide 06's `slide-inner`)

**Step 1: Write the Arnaud coda HTML**

After Clara's result box (line ~1431, the `<div class="fw-result">` that says "From running shoes to art on the wall to co-op governance"), add a new sub-section within the same slide. Use a visual separator (some spacing + a new mini-headline).

Content:

- Mini-headline: `Remember Arnaud? The runner who bought the painting.`
- 5 narrative steps using the same `fc-step` / `fc-marker` pattern:
  1. Arnaud is an electrical engineer. Girlfriend from a dating app. A few university friends. He likes cycling and running. He recently made the biggest effort of his life: joining a running club.
  2. It's been months. He likes running with people. He feels more connected. But he never speaks to anyone. He believes he has nothing interesting to say. *They're all so cool.*
  3. One day, someone in the running club creates a community on the app. Everyone signs up — because that's where all the events will be now. This same person writes a newsletter about the best running races in Brussels and across Europe. By joining the community, you get access to her newsletter too. Arnaud signs up for the events and the newsletter. But then he starts scrolling. And he discovers who these people are — the ones he's been running next to in silence. One paints. One photographs. One organizes film screenings. He had no idea.
  4. Now he has things to say. At the next run, he walks up to someone: "I saw your paintings on the app. They're incredible." The ice was never really there — he just needed a reason to speak.
  5. Months later, Arnaud has real friends. And he's finally made the jump he never dared: he started painting. Art was a foreign concept in his family, in his friend circle. But now he's surrounded by people who do it. It feels normal. He starts.
- Result box: "The app didn't just connect him to others. It connected him to a part of himself he was afraid to explore."

**Step 2: Verify in browser**

Open `website/social-v2.html`. Scroll to Clara's flywheel. After the Clara result, Arnaud's section should appear naturally. Check reveal/stagger animations and mobile responsiveness.

**Step 3: Commit**

```bash
git add website/social-v2.html
git commit -m "feat(social-v2): add Arnaud's arc as coda to Clara's flywheel"
```

---

### Task 3: Add shy/newcomer persona cards to slide 05

**Files:**
- Modify: `website/social-v2.html` (add two cards to the `.personas` grid in slide 05, around line ~1331)

**Step 1: Add two persona cards**

After the existing 6 persona cards (Readers, Creators, Event planners, Galleries & cinemas, Workshops & classes, Newsletter writers), add:

```html
<div class="persona stagger">
  <div class="persona-role">The shy one</div>
  <div class="persona-desc">You never speak up, but you'll show up. The app gives you reasons to walk up to someone. Things to say. The ice was never really there &mdash; you just needed a reason.</div>
</div>
<div class="persona stagger">
  <div class="persona-role">The newcomer</div>
  <div class="persona-desc">You just moved here. You don't know anyone. Within weeks of joining your first community, you're surrounded by people &mdash; and you have a hundred things to talk about.</div>
</div>
```

**Step 2: Verify in browser**

Check the persona grid. With 8 cards the grid should still work (it uses `auto-fit, minmax(230px, 1fr)`). Check mobile stacking.

**Step 3: Commit**

```bash
git add website/social-v2.html
git commit -m "feat(social-v2): add shy/newcomer persona cards to 'who is this for' grid"
```

---

### Task 4: Refine hero tagline and CTA closing

**Files:**
- Modify: `website/social-v2.html` (hero section ~line 1187, CTA section ~line 1722)

**Step 1: Update hero sub-tagline**

Current hero tagline (line ~1187):
```html
<p class="hero-tagline">The open source social network that makes you more social.<br>An open idea looking for dreamers and builders.</p>
```

Change to:
```html
<p class="hero-tagline">The open source social network that makes you more social.<br>Not by connecting you to strangers. By showing you who the people you already know really are.</p>
```

Keep the second line from the old tagline ("An open idea looking for dreamers and builders") — move it to a smaller `<p>` below the tagline if it still matters, or drop it. Decision: keep it as a `hero-meta` style line below, since the page is positioned as an open idea.

**Step 2: Update CTA closing text**

In slide 12 (the CTA), after the headline "If this made your eyes light up", update the `<p class="sub">` to weave in the thesis. Add a line like:

"This is not just a social network. It's the thing that actually makes you more social — by giving you reasons to show up, things to say, and the courage to walk up to someone."

**Step 3: Verify in browser**

Check hero and CTA sections render correctly. Ensure line breaks look good on mobile.

**Step 4: Commit**

```bash
git add website/social-v2.html
git commit -m "feat(social-v2): refine hero tagline and CTA with 'makes you more social' thesis"
```

---

### Task 5: Add "The Socializing Effect" section to SPEC

**Files:**
- Modify: `products/social-v2/SPEC.md` (insert new section after "The Undisclosed Loop: Dating", before "The Speeches")

**Step 1: Write the new SPEC section**

Insert after the "The Undisclosed Loop: Dating" section (after line ~253) and before "The Speeches" section:

```markdown
---

## The Socializing Effect

**This app will make you more social.** Not by connecting you to strangers — by showing you who the people you already know really are.

The underlying mechanic: when a community is small enough, seeing an event or a blog post from someone you know feels like a personal invitation. You don't have to be tagged. You don't have to be DMed. You just see it on your calendar — and you show up. For shy people, that's everything: no ice to break, no awkward "are you going?" conversation, just a natural pull. For newcomers in a new city, it's a socializing accelerator: within weeks, they're surrounded by people and have a hundred things to talk about.

The app gives you ammunition for connection: things to say, reasons to walk up to someone, permission to explore parts of yourself you were afraid to try. It doesn't replace the human moment — it makes the human moment inevitable.

**Arnaud — the shy one.** Electrical engineer. Has a girlfriend he met on a dating app. A few friends from university. Likes cycling and running. Recently made the biggest effort of his life: joining a running club. It's been months. He likes running with people. He feels more connected. But he never speaks to anyone. He believes he has nothing interesting to say. *They're all so cool.*

One day, someone in the running club creates a community on the app. Everyone signs up — because that's where all the events will be. This same person writes a newsletter about the best running races in Brussels and across Europe. Arnaud signs up for the events and the newsletter. But then he starts scrolling. And he discovers who these people are — the ones he's been running next to in silence. One paints. One photographs. One organizes film screenings.

Now he has things to say. At the next run, he walks up to someone: "I saw your paintings on the app. They're incredible." The ice was never really there — he just needed a reason to speak. Months later, Arnaud has real friends. And he's finally made the jump he never dared: he started painting. Art was a foreign concept in his family, in his friend circle. But now he's surrounded by people who do it. It feels normal. He starts.

The app didn't just connect him to others. It connected him to a part of himself he was afraid to explore.

**Valentina — the newcomer.** From South America. Just moved to Brussels. Loves biking, plays soccer, dances salsa. She goes to a salsa night, has a great time. Someone says: "You should be on the app." She goes home, creates an account — and can't stop scrolling. All these people she was dancing with tonight — a painter, a photographer, someone who organizes jazz nights. She had no idea.

She spots a guy who looks like he's in a soccer team. She needs to ask him about it at the next salsa class — which is tomorrow, because the app has every event. She still has to earn those phone numbers the organic way. Dance a little more. Show up a few more times. It's not instant connection.

But now she has so many things to say. So many reasons to walk up to someone. Three weeks in a new city — already surrounded by people. The app didn't connect her. It gave her reasons to connect herself.
```

**Step 2: Verify markdown renders correctly**

Read the file and confirm formatting, section placement, and flow relative to adjacent sections.

**Step 3: Commit**

```bash
git add products/social-v2/SPEC.md
git commit -m "feat(social-v2): add 'The Socializing Effect' section with Arnaud and Valentina personas"
```

---

### Task 6: Final review and commit

**Step 1: Review all changes**

```bash
git diff --stat
git diff
```

Scan the full diff. Check:
- No orphan HTML tags
- No broken section numbering (slide numbers may need adjustment)
- SPEC section flows naturally between Dating and Speeches
- All commits have clear messages

**Step 2: Verify pitch deck end-to-end**

Open `website/social-v2.html` in browser. Scroll through the entire page. Check:
- Valentina's section appears between personas and Clara's flywheel
- Arnaud's coda appears after Clara's result box
- New persona cards render in the grid
- Hero tagline reads well
- CTA closing reads well
- Mobile responsive at 375px

**Step 3: Final commit if any fixes needed**

```bash
git add -A
git commit -m "fix(social-v2): polish makes-you-more-social additions"
```
