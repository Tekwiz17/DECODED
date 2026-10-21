# DECODED

[Open DECODED](https://decoded.tekwiz17.chatgpt.site)

Original learning paths with Byte, a computer study companion. Purple/blue design, short interactive lessons, search and playful progress. Existing lesson IDs are preserved.

Twenty courses include ten introductory math paths (Kindergarten–Grade 8 and optional Precalculus). Together with Algebra I, Geometry and Algebra II, there is a suggested math option for every grade K–12. The new math paths contain five introductory lessons each and are not complete grade-level syllabi. The ten Regents courses cover Algebra I, Geometry, Algebra II, Life Science: Biology, Earth and Space Sciences, Physical Science: Chemistry, Physical Science: Physics, English Language Arts, Global History and Geography II, and U.S. History and Government.

- 111 suggested units, 267 original lessons and 484 term cards. Units have variable lesson counts.
- Read → reveal worked steps → apply → connect a term → explain in your own words.
- Start fresh or take a skippable placement check with application and term-matching tasks. Recommendations do not lock units or award completion.
- 15 interactive science challenges and 11 compass-and-straightedge construction tutorials.
- 146 selected released NYSED multiple-choice references with official paper, stimulus page range and answer-key links. Actual question text and third-party passages stay in the original PDFs. Some units have no indexed question yet.
- Search courses, unit topics, lesson titles and terms, with grade filtering.
- Winding lesson paths, completion celebrations, quests, XP and level progress.
- Vocabulary cards, definition quizzes, TSV and Quizizz-style CSV exports.
- Required ChatGPT Sites sign-in, private D1 progress, lesson resume, XP, local-calendar streaks, goals and a page-to-page tutorial.

## Scope and provenance

Frameworks and exam links verified October 19, 2026. Unit order is DECODED’s suggested teaching sequence, not a state-mandated order. Standards-family/key-idea mapping is included; this is a course-spanning study release, not certification that every individual performance expectation is fully covered and assessed. Models state their assumptions and do not replace laboratory credit. See `curriculum/source-notes.json` and the on-site Sources page.

## Development

Uses the retained Sites Vinext/Cloudflare D1 starter. Node 22.13+ required. Install dependencies with the Sites install helper, then use `npm run dev` in a supported local environment. `python curriculum/build.py` regenerates the courses, public catalog and validation manifest from original authored content and committed research metadata. No downloaded PDFs are required for generation.

- `curriculum/author.py`: original Regents content.
- `curriculum/grade-paths.py`, `curriculum/expand.py`: introductory math paths and combined catalog.
- `app/experience.css`: purple/blue responsive redesign.
- `curriculum/research/`: provenance, standards families and selected official exam mappings.
- `curriculum/courses/`: generated server-only course JSON.
- `public/catalog.json`: public metadata; no lesson content.
- `public/learn.js`: interface, placement, lesson loop, vocabulary, exams and account synchronization.
- `public/science.js`, `public/constructions.js`, `public/byte.js`: models, construction studio and original SVG mascot.
- `app/api/course/route.ts`: authenticated course content.
- `app/api/progress/route.ts`, `lib/progress.ts`: same-origin account-scoped saves, validation and revision conflicts.

Check with `node check.cjs`, `node check-api.cjs`, `node check-ui.cjs`, and `node node_modules/typescript/bin/tsc --noEmit`. Package using the Sites build helper. Authentication is owned by Sites; never trust user-supplied identity headers on the public internet. No password is stored by this application.

Validation: automated content, account/API and UI-logic checks. Browser preview was unavailable, so visual layout and hosted sign-in were not end-to-end verified during this update. Reading levels adjust support and depth; not every existing lesson has a separate rewrite.
