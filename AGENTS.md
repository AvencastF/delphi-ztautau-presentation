# Agent instructions

## Start here

This repository contains independent Slidev presentations about the DELPHI
$Z \to \tau^+\tau^-$ spin-density-matrix analysis, backed by one root npm
installation. Read [the authoring guide](docs/authoring.md) before creating a
deck or changing shared infrastructure. The wider analysis project lives in
`/Users/avencastmini/ZtautauLEP/`; its `AGENTS.md` and `docs/PROJECT_GUIDE.md`
govern the physics, data, and NERSC rules that slide content reports on.

1. Check `git status` and the current branch. Preserve unrelated edits, notes, and generated exports; do not stage them with your work.
2. Identify whether the task changes one deck, shared infrastructure, build tools, or documentation. Keep the scope explicit.
3. Search before implementing: inspect `shared/slidev-addon-ztautau/components/`, `shared/slidev-addon-ztautau/composable/`, `shared/styles/`, and existing deck-local components. Reuse an existing implementation when it fits.
4. Before editing a deck, read its `README.md`, `SOURCES.md`, and `slides.md`. A deck README records that talk's owner decisions, presentation rules, and caveats; it takes precedence over the repository defaults below for that deck.

## Create and edit decks

Run these commands from the repository root:

```bash
npm ci                                  # Initial setup or after lockfile changes
npm run new -- My_Talk
npm run dev -- My_Talk
npm run build -- My_Talk
npm run export -- My_Talk                # When an export is requested
```

- Use the generator, not a copy of another presentation directory. It creates the starter `slides.md` and `style.ts`; add `slides/`, `public/`, `components/`, `data/`, `SOURCES.md`, and `README.md` as the talk needs them.
- Keep the generated default theme, `slidev-addon-ztautau` addon reference, hash routing, and stylesheet import order unless the user requests a change.
- Put talk-specific Markdown, data, figures, figure generators, and unique components inside the selected deck. Read the target deck's README and entry file before editing it.
- Never add per-deck manifests, lockfiles, dependency directories, GitHub workflows, copied shared component libraries, or manual infrastructure symlinks. The addon workspace's own package manifest is intentional.
- New decks consume shared components directly. Do not copy `LaTeX.vue`, `ZoomablePlot.vue`, `ChapterRail.vue`, `useStepMotion.ts`, `tex.ts`, or `global-top.vue` into a deck.
- Every top-level directory containing `slides.md` is included in `build:all`; the landing page is separate. Do not create throwaway decks in the repository root and forget them. Listing a talk publicly or publishing its content requires appropriate user authorization.

## Shared versus local

- `shared/slidev-addon-ztautau/` owns reusable Vue components (`LaTeX`, `ZoomablePlot`, `ChapterRail`), composables (`useStepMotion`, `tex`), the global page-number layer, and common UnoCSS/Vite configuration. `shared/styles/` owns common CSS. `shared/brand/` owns the bundled DM Sans font.
- Prefer props, slots, and existing CSS variables over copying a component or stylesheet. Introduce shared APIs for demonstrated reuse, not speculative generalization.
- Shared code must not import a particular deck's Markdown, datasets, figures, or components. Pass talk-specific inputs from the deck. Keep slide content, datasets, provenance files, and public assets local even when similar content appears in another talk.
- Keep one-off behavior in a deck-local component with a distinct name. For example, the status deck's `DeckChapters.vue` fixes its seven chapter names and wraps the shared `ChapterRail`. A same-name local component overrides the addon component; use that only deliberately and document why in the deck README.
- Load common CSS through the ordered TypeScript imports in `style.ts`, not CSS `@import`. Add deck-local `./styles/*.css` imports after the shared ones.
- Global layers are additive, not same-name overrides. Do not copy the addon's `global-top.vue` into a deck; it would render the page number twice.
- Shared changes affect all consumers. Preserve existing defaults and backwards-compatible props. If a requested change would alter existing presentations, explain the impact and get direction before widening the scope.

## Mathematics and particle notation

- Use LaTeX by default for all audience-visible mathematical symbols, formulas, units with exponents, particle names, and decay/reaction notation, including slide titles, prose, captions, table cells, and diagram labels. Use another representation only when the user explicitly requests it.
- Use Slidev inline/block math in Markdown and the shared [LaTeX.vue](shared/slidev-addon-ztautau/components/LaTeX.vue) component in HTML/Vue layouts. For example: `<LaTeX formula="\tau^+\tau^-" />`, `<LaTeX formula="e^+e^- \to Z/\gamma^* \to \tau^+\tau^-" />`, and `<LaTeX formula="\chi^2/\mathrm{dof}" />`. The component accepts a `formula` string and an optional `block` boolean, renders synchronously with the bundled KaTeX, and imports the KaTeX stylesheet itself. Inside Vue/SVG components that build strings, use `tex()` or `mixed()` from the addon's `composable/tex.ts`.
- Do not substitute Unicode or HTML entities for mathematical/particle symbols, or construct notation with HTML `<sub>`/`<sup>`. In SVG diagrams, use an HTML `foreignObject` with the LaTeX component when adding editable notation. Preserve labels embedded in existing scientific figure assets. Source identifiers, paths, speaker notes, alt text, and `SOURCES.md` remain plain text.

## Scientific provenance

- Every number on a slide must have a provenance entry in the deck's `SOURCES.md`: the file, table, or command output it was copied from, with dates and revisions. Mark values derived on the slide (sums, ratios) as derived and record how. Follow the existing [status deck SOURCES.md](ztautau-status-1994-20261022/SOURCES.md) convention of dated sections that supersede earlier rows.
- Do not invent or round away numbers, dataset names, luminosities, cut values, efficiencies, or validation outcomes. If a value is not in a local artifact or a reachable recorded source, leave a visible gap and list it in the deck README's TODO section.
- Documentation, a runbook, or a plan is not evidence that a production, calibration, or validation was run. State the status that the source supports (planned, run, closure only, validated) and nothing stronger.
- Label simulation-only, Asimov/expected, closure-on-simulation, and statistics-only results as such on the slide itself, not only in the notes. Do not present an uncertain or uncertified input (for example a user-supplied luminosity) as final.
- Keep historical caveats and dated owner decisions in the deck README when revising a talk; supersede them with a new dated entry rather than deleting the reason.

## Presentation defaults

Unless a deck README records different owner decisions, new decks follow the status deck's rules: at most 70 words of body text per slide (table cells, captions, and tags excluded); one plain-words "Source:" footer per slide; raw identifiers only as small italic `<span class="id">…</span>` notes, with the full identifiers in `SOURCES.md` or presenter notes; $\chi^2/\mathrm{dof}$ badges green at most 1.5, amber at most 3, red above 3; semantic tags `data`, `sim` (simulation), `sel` (selection), `ml`, `fit`, `decision`, and `open`. Each deck README states its display-precision conventions.

## Dependencies, output, and deployment

- Install and manage dependencies at the repository root only. Check for an existing dependency first; do not upgrade or regenerate the lockfile just to create a talk.
- Preserve the pinned `@slidev/cli` and `@slidev/client` `52.11.3`, `@slidev/theme-default` `0.25.0`, and `animejs` `4.5.0`, and the `katex ^0.16` and `unocss ^66` ranges, unless a dependency change is explicitly requested. Update the root manifest and lockfile together when an authorized change requires it.
- A single build writes `<deck>/dist/`. `npm run build:all` recreates `site/`, builds every deck with base `/<repository>/<deck>/`, and copies the `gh-pages/` landing tree into `site/`. The default repository name is `delphi-ztautau-presentation`; pass `-- --base /x/` to override it.
- Keep existing deck folder names, `/<repository>/<deck>/` bases, hash routes, public asset paths, slide order, and settings unchanged during infrastructure-only work.
- CI uses one root `npm ci`. Do not restore per-deck installs, per-deck workflows, output caching, or parallel builds as incidental changes.
- Do not edit generated `site/`, `dist/`, or `node_modules/` as source. Do not remove unrelated exports. Do not push, merge, or deploy unless requested.

## Verification and handoff

- Run `npm test` for changes to build tools, the generator, dependencies, shared code, or documentation.
- For a new deck or deck-local change: build that deck and inspect its rendered output, relevant click states, figures, formulas, and interactions. Check its deployment base, not just the dev root URL. Rerun the deck's own checks (for example its word-count and LaTeX checks) when they exist.
- For shared styles/components/configuration or dependency changes: build all decks and compare all affected presentations against a baseline. A passing build alone does not prove rendering equivalence.
- For visual changes, use the same browser, viewport, fonts, and settled animation states. Check initial/final click states and relevant intermediate interactions, direct links/refresh, presenter/overview routes, public assets, and console errors. Record actual coverage and any gaps.
- For tool/generator changes: also check starter creation, no-overwrite/invalid-name/reserved-name behavior, argument forwarding, and failure propagation. Verify the starter's dev/build/export workflow when those paths change.
- Documentation-only changes need working examples and link checks, not a full presentation rebuild.
- Report pre-existing failures separately; do not silently fix unrelated rendering issues.
- Review the final diff and summarize changed scope, checks performed, and limitations. Keep browser QA artifacts under ignored `output/playwright/`.

## Conversation titles

When the interface supports renaming the conversation, use `YY.MM | TYPE | SUBJECT`: current year/month, a short category such as CODE, TALK, DEBUG, REVIEW, or WRITE, and a 2–5 word subject. Do not repeat the project name or use a sentence-like title.
