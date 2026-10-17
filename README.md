# Bio, decoded

An interactive Biology A study website starting with Unit 2. Built for students who want the ideas explained clearly, with examples and practice.

## Included
- Six chemistry-of-life sections: water, pH/indicators, synthesis/hydrolysis, molecule families, protein structure, and an enzyme extension.
- Six later subject sections: cells/transport, energy, homeostasis, genetics, evolution, and ecology. These are not assigned classroom unit numbers.
- Twelve interactive models, 65 flashcards, and 35 original practice questions.
- Topic filters, learn-as-you-go practice, test mode, missed-question review, and browser-local progress.
- Responsive layout, semantic controls, keyboard-friendly flashcards, and reduced-motion support.

## Run
Serve `dist` with any static web server, for example `python3 -m http.server 8000 --directory dist`, then open localhost:8000. No build, API keys, accounts, or paid services required.

Edit `dist/content.js` for lesson, card, and question data; `dist/app.js` for interactions; `dist/style.css` for appearance. `make_content.py` regenerates content.js (adjust its output path for your checkout). `node check.cjs` runs data integrity and application-flow checks with a minimal DOM harness. Browser visual QA should also be performed when available.

## Scope and references
Unit 2 topic selection came from a user-supplied notes video. The video and worksheet scans are not included. Explanations, diagrams, and practice items are original; this is an independent study aid, not an official NYSED course or exam.

Reference links appear in the site's Sources & scope page: NYSED Life Science Biology and OpenStax Biology 2e. Models are simplified and label their assumptions. Later subject coverage is introductory and can be expanded to follow the teacher's next notes.

Progress uses localStorage only. No student accounts, analytics, or server-stored scores. Google Fonts is optional; system fonts are fallbacks.
