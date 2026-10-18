# DECODED

[Open DECODED](https://decoded.tekwiz17.chatgpt.site)

Small lessons, big lightbulb moments. DECODED turns our class notes into a playful learning path with Byte, an animated computer study buddy.

Currently available: **Biology → Unit 2 → Chemistry of life**. No other classes, units, or enzyme extension are included. More can be added as new notes arrive.

## What you can do
- Follow five guided lessons: water, pH and indicators, building/breaking molecules, molecule families, and protein structure.
- Read one idea at a time, explore an animated model, and answer practice questions with explanations.
- Earn 20 XP the first time you finish each topic, plus 10 XP for a practice set once per local day.
- Set a daily XP goal, build a study streak, and earn simple achievement badges. No lives, timers, or punishment for wrong answers.
- Use 30 flashcards, missed-question review, and 16 original practice questions.
- Sign in with ChatGPT to save private progress across devices, or keep learning as a guest with browser-local saves.

## Development
Uses the Sites Vinext starter with Cloudflare D1 and Drizzle. Node 22.13+ is required. Install using the Sites dependency helper (or the project's documented installation scripts), then run `npm run dev`. Run `npm run db:generate` after schema changes and apply the generated migration to the local D1 preview before testing signed-in persistence. Hosted authentication is owned by ChatGPT Sites. Do not supply your own identity headers on the public internet.

- `app/Decoded.tsx`: browser shell and ordered asset loading
- `public/decoded.js`: learning path, Byte SVG, lesson loop, XP, goals, streaks, and account synchronization
- `public/app.js`: notes, flashcards, practice, and progress integration
- `public/models.js`: animated SVG models with pause and reduced-motion support
- `public/content.js`: current class content; regenerate with `python make_content.py`
- `app/api/progress/route.ts`: authenticated per-user progress API, validation, same-origin writes, optimistic concurrency
- `lib/progress.ts`, `db/schema.ts`, `drizzle/`: validation and schema-only migrations
- `app/globals.css`: responsive visual design

Run `node check.cjs` for model and lesson-flow checks and `node node_modules/typescript/bin/tsc --noEmit` for type checking. Build through the Sites build helper when publishing. The source uses Sites-managed hosting; no hosted secrets are included.

## Accounts and privacy
Account records use the stable, site-specific ChatGPT user ID. The progress database stores study progress and a timestamp; it does not store names, email addresses, passwords, or teacher grades. Progress reads and writes are scoped on the server to the authenticated user. Public content remains accessible anonymously. Guest progress is not silently imported into an account; learners can choose to import it from their profile. A save error is shown and a local copy is retained. Revision conflicts reject stale writes; reload before resuming on another device.

XP is a personal motivational tool, not an anti-cheat system or a formal grade. There are no public leaderboards, analytics, or student-to-student messaging. Google Fonts is optional; system fonts are fallbacks.

The notes video and original worksheets are not published. Lessons, Byte, diagrams, and practice questions are original. References appear in About & privacy: NYSED Life Science Biology and OpenStax Biology 2e. Independent study resource, not an official NYSED course. Inspired by short, rewarding learning experiences, with its own branding and character.

## Reading levels
The shared reading setting applies across the app and is saved with account progress (or on the guest device): **EASY** uses everyday words and short steps, **MEDIUM** uses clear ninth-grade explanations, and **EXPERT** restores detailed notes vocabulary. It changes explanations, not the learning objectives, answer key, completion, or XP. Learners can switch mid-lesson, mid-flashcard, or after submitting a practice answer without losing their place.

`make_reading.py` authors the three versions in `public/reading-content.js`; run it after `make_content.py` changes. `public/reading.js` handles the shared selector, updates content in place, and preserves activity state. Every future topic can register `READING_CONTENT.topics[topicId]` with matching `easy`, `medium`, and `expert` objects. Keep section counts and question option meanings aligned across levels. Missing future variants fall back to the original text rather than silently inventing science. Only Biology Unit 2 is currently authored.
