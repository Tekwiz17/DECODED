# DECODED

[Open DECODED](https://decoded.tekwiz17.chatgpt.site)

Small lessons, big lightbulb moments. DECODED turns our class notes into a playful learning path with Byte, an animated computer study buddy.

Currently available: **Biology A - Regents → Unit 2 → Chemistry of life** and **Geometry A (Regents) → Units 1–4**. Future material is added only as class notes arrive. The subject and unit selectors remain available across lessons and tools.

## What you can do
- Follow five guided lessons: water, pH and indicators, building/breaking molecules, molecule families, and protein structure.
- Read one idea at a time, explore an animated model, and answer practice questions with explanations.
- Earn 20 XP the first time you finish each topic, plus 10 XP for a practice set once per local day.
- Set a daily XP goal, build a study streak, and earn simple achievement badges. No lives, timers, or punishment for wrong answers.
- Biology has 16 original practice questions. All 88 flashcards across both subjects are terms and definitions (38 Biology, 50 Geometry). Geometry follows all 21 days in the uploaded packets, with 63 original practice questions, 11 interactive concept models, and 11 guided compass-and-straightedge tutorials. Review queues and practice sets follow the selected unit.
- Sign in with ChatGPT to save private progress across devices, or keep learning as a guest with browser-local saves.

## Development
Uses the Sites Vinext starter with Cloudflare D1 and Drizzle. Node 22.13+ is required. Install using the Sites dependency helper (or the project's documented installation scripts), then run `npm run dev`. Run `npm run db:generate` after schema changes and apply the generated migration to the local D1 preview before testing signed-in persistence. Hosted authentication is owned by ChatGPT Sites. Do not supply your own identity headers on the public internet.

- `app/Decoded.tsx`: browser shell and ordered asset loading
- `public/decoded.js`: learning path, Byte SVG, lesson loop, XP, goals, streaks, and account synchronization
- `public/app.js`: notes, flashcards, practice, and progress integration
- `public/models.js`: animated SVG models with pause and reduced-motion support
- `public/content.js`: Biology content; regenerate with `python make_content.py`
- `public/geometry-content.js`: Geometry packet content and all three reading levels; regenerate with `python make_geometry.py`
- `public/catalog.js`: subject/unit navigation and stable course identities
- `public/geometry-models.js`: mathematical SVG models, smooth transitions, pause, and reduced motion
- `lib/course-catalog.json`: server validation bounds; regenerate with `node make_catalog.cjs` after content changes
- `app/api/progress/route.ts`: authenticated per-user progress API, validation, same-origin writes, optimistic concurrency
- `lib/progress.ts`, `db/schema.ts`, `drizzle/`: validation and schema-only migrations
- `app/globals.css`: responsive visual design

Run `node check.cjs` for model and lesson-flow checks and `node node_modules/typescript/bin/tsc --noEmit` for type checking. Build through the Sites build helper when publishing. The source uses Sites-managed hosting; no hosted secrets are included.

## Accounts and privacy
Account records use the stable, site-specific ChatGPT user ID. The progress database stores study progress and a timestamp; it does not store names, email addresses, passwords, or teacher grades. Progress reads and writes are scoped on the server to the authenticated user. Public content remains accessible anonymously. Guest progress is not silently imported into an account; learners can choose to import it from their profile. A save error is shown and a local copy is retained. Revision conflicts reject stale writes; reload before resuming on another device.

XP is a personal motivational tool, not an anti-cheat system or a formal grade. There are no public leaderboards, analytics, or student-to-student messaging. Google Fonts is optional; system fonts are fallbacks.

The notes video and original worksheets are not published. Lessons, Byte, diagrams, and practice questions are original. References appear in About & privacy: NYSED Life Science Biology and OpenStax Biology 2e. Independent study resource, not an official NYSED course. Inspired by short, rewarding learning experiences, with its own branding and character.

## Reading levels
Easy means concise, age-appropriate secondary-school explanations with the correct terms retained. No personified math prompts are used. The shared reading setting applies across the app and is saved with account progress (or on the guest device): **EASY** uses everyday words and short steps, **MEDIUM** uses clear ninth-grade explanations, and **EXPERT** restores detailed notes vocabulary. It changes explanations, not the learning objectives, answer key, completion, or XP. Learners can switch mid-lesson, mid-flashcard, or after submitting a practice answer without losing their place.

`make_reading.py` authors the three versions in `public/reading-content.js`; run it after `make_content.py` changes. `public/reading.js` handles the shared selector, updates content in place, and preserves activity state. Every future topic can register `READING_CONTENT.topics[topicId]` with matching `easy`, `medium`, and `expert` objects. Keep section counts and question option meanings aligned across levels. Missing future variants fall back to the original text rather than silently inventing science. Only Biology Unit 2 is currently authored.

## Byte’s study-companion behavior
`public/byte-activity.js` adds a persistent, dismissible Byte companion. It reacts to lesson starts, model exploration, answer feedback, three-answer streaks, flashcard review, lesson completion, and daily goals. Tap Byte for encouragement. Its settings can quiet unsolicited tips or pause all Byte animations, and system reduced-motion preferences take priority. Preferences stay on the device. There is no sound, push notification system, guilt messaging, or extra XP awarded by the mascot. Model tips are throttled so sliders do not flood the screen. Messages dismiss automatically and can be closed manually.

## Study toolbox and returning learners
`public/study.js` adds a toolbox, searchable 24-term glossary, eight-example molecule sorting activity, a personalized next-step card on the home page, and a review queue. The queue prioritizes currently missed questions and scheduled flashcards. “Got it” schedules a card in 1, 3, 7, then 14 days; “Still learning” makes it due today. Same-day successful repeats do not inflate the interval. Scheduling uses the device’s local date and is a study aid, not a mastery score.

Guided lessons checkpoint their current step, question order, selection, and revealed feedback. Resume returns to that state, including after a refresh. Completed lessons clear the checkpoint. Signed-in learners’ review schedule and checkpoint use the existing private progress record; guests keep them locally. Sorting awards 10 XP once per local day, independently of the existing practice reward. It is keyboard/tap friendly and requires no dragging. All tools stay within the current Biology Unit 2 notes.

## Geometry packet scope
Navigation follows the four uploaded files in order: radicals/right triangles; quadratics/systems; coordinates/segments; angles/lines/constructions. The third and fourth packets print Unit 2 and Unit 3 respectively; this difference is disclosed on those learning paths and in About. No later Geometry material is included. Original PDFs are not committed or hosted. Existing Biology question/card indices are preserved, Daily lesson IDs preserve compatible completion. Card schema 2 replaces explanation prompts with terms and starts their review schedules fresh, while preserving XP and lesson completion. Old Geometry resume checkpoints are cleared once because the lesson layout changed.

## Daily lessons and construction teaching
Geometry unit/day counts follow the four uploaded packet groups: 5, 4, 5, and 7. Construction Studio covers segment copies, midpoints/perpendicular bisectors, angle copies, angle bisectors, incircles, both parallel-line methods, perpendiculars from points on/off a line, and circumcircles. Tutorials reveal exact geometric diagrams with previous/next steps, replay, reasons, and a paper-practice checklist. Regenerate all course outputs with `python make_geometry.py`, `python make_terms.py`, then `node make_catalog.cjs`.
