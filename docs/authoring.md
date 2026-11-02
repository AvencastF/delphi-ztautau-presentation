# Creating presentations without duplicating infrastructure

This is the practical companion to [AGENTS.md](../AGENTS.md). The short version: generate a deck, write its content with a provenance record, and consume the shared addon. Do not clone an entire old talk.

## 1. Create a deck

From the repository root, with a current Node.js LTS release:

```bash
npm ci
npm run new -- My_Talk
npm run dev -- My_Talk
```

`npm ci` is initial setup, not a per-presentation step. Run it again when the lockfile changes or the installation needs replacing. npm automatically links the local `slidev-addon-ztautau` workspace; no manual symlink or package publishing is needed.

The generator creates the starter entry and stylesheet loader. Add the other directories as the talk needs them:

```text
My_Talk/
  slides.md       Entry, settings, and initial slide (generated)
  style.ts        Ordered shared stylesheet imports (generated)
  slides/         Markdown sections, one file per slide or section
  public/         This talk's figures and other static assets
  components/     Components unique to this talk
  data/           Talk datasets and slide/figure generators
  SOURCES.md      Provenance of every number shown
  README.md       Owner decisions, presentation rules, caveats, TODO
```

Names must start with a letter or number and contain only letters, numbers, underscores, or hyphens. Do not run the generator on an existing deck name. `site`, `node_modules`, `shared`, `tools`, `gh-pages`, `output`, and `docs` are reserved. Empty directories are not tracked by Git; that is normal until you add content.

The generated headmatter already includes:

```yaml
theme: default
addons:
  - slidev-addon-ztautau
```

Keep the other generated settings too, such as hash routing, canvas width, and aspect ratio. An addon supplements the default theme rather than replacing its layouts/fonts. See [Slidev's theme/addon documentation](https://sli.dev/guide/theme-addon). The DM Sans font is bundled in `shared/brand/` and loaded by `style.ts`, so the preview also works offline.

Development retains `--open --remote`, so it opens a browser and exposes the preview to the network. Additional CLI arguments are forwarded:

```bash
npm run dev -- My_Talk --port 3031
```

## 2. Write content locally

Keep the generated headmatter at the beginning of `My_Talk/slides.md`. Replace the placeholder body and add section references, for example:

```markdown
# Tau-pair spin correlations at LEP

An introduction for this audience.

---
src: ./slides/method.md
---
```

Then create `My_Talk/slides/method.md`:

```markdown
# Decays as spin analysers

The process $e^+e^- \to Z/\gamma^* \to \tau^+\tau^-$ fixes the pair's spin state.

<LaTeX formula="\rho = \tfrac{1}{4}\Big(\mathbb{1} + \sum_i B^+_i\sigma_i \otimes \mathbb{1} + \sum_j B^-_j\,\mathbb{1}\otimes\sigma_j + \sum_{ij} C_{ij}\,\sigma_i\otimes\sigma_j\Big)" block />

<v-clicks>

- Each <LaTeX formula="\tau" /> decay is an analyser of its spin.
- Simulation only, Asimov, statistics only.

</v-clicks>

<div class="nju-source">Source: the spin-fit study note (paths in SOURCES.md)</div>
```

The entry file controls ordering; a Markdown file is not included merely because it exists in `slides/`. Keep talk-specific datasets and generators in `My_Talk/data/`. Do not import another deck's sections or data to avoid maintaining local content; copy the specific numbers you need and cite them in your own `SOURCES.md`.

### Provenance and labelling

Start `My_Talk/SOURCES.md` with the first slide. For each slide, record the file(s), tables, revisions, and dates every number was read from, and mark values derived on the slide. Follow the dated-section convention of the [status deck's SOURCES.md](../ztautau-status-1994-20261022/SOURCES.md). A runbook or plan is not evidence that a result was produced or validated. Label simulation-only, Asimov/expected, closure-on-simulation, and statistics-only results on the slide itself. Record anything you could not source in the deck README's TODO list rather than filling it in.

### Presentation defaults

Unless the deck README records different owner decisions:

- At most 70 words of body text per slide (table cells, figure captions, key-value entries, and tags excluded). Move removed prose to presenter notes (`<!-- -->`).
- One short "Source:" footer per slide, in plain words, for example `<div class="nju-source">…</div>`.
- No internal shorthand in the slide body. Describe regions, cuts, campaigns, and model versions in plain words, with the raw identifier as `<span class="id">…</span>`.
- $\chi^2/\mathrm{dof}$ badges: `<span class="badge g">` up to 1.5, `badge a` up to 3, `badge r` above 3, `badge n` when no $\chi^2$ is available.
- Semantic tags: `tag data`, `tag sim`, `tag sel`, `tag ml`, `tag fit`, `tag decision`, `tag open`.
- State the display-precision conventions (cross sections, fractions, luminosity, $\chi^2/\mathrm{dof}$ format) in the deck README.

### Mathematics and particle notation

Use LaTeX for every audience-visible symbol, formula, unit with an exponent, particle name, and decay: Slidev `$…$`/`$$…$$` in Markdown, `<LaTeX formula="…" />` in HTML blocks and Vue templates, and an HTML `foreignObject` holding `<LaTeX>` in SVG. Do not write Unicode or HTML-entity substitutes (τ, χ², pb⁻¹) or `<sub>`/`<sup>` notation in slide content. Labels baked into figure assets stay as they are. Alt text, identifiers, presenter notes, and `SOURCES.md` stay plain text.

## 3. Reuse before writing new infrastructure

Use this ownership rule:

| What you need | Where it belongs |
| --- | --- |
| Narrative, slide order, speaker notes, results/data, provenance | The deck (`slides.md`, `slides/`, `data/`, `SOURCES.md`) |
| Figures with stable public URLs | The deck's `public/` |
| One-off Vue behavior or styling, fixed chapter lists | `<deck>/components/` or `<deck>/styles/` |
| Reusable, talk-independent Vue behavior | `shared/slidev-addon-ztautau/components/` |
| Reusable animation drivers and KaTeX helpers | `shared/slidev-addon-ztautau/composable/` |
| Common palette, typography, chapter rail, status-report layouts | `shared/styles/` |
| Bundled fonts | `shared/brand/` |
| Common global layers and UnoCSS/Vite configuration | `shared/slidev-addon-ztautau/` |
| Dependencies and CLI/build behavior | Root manifests and `tools/` |

Search the existing implementations and their callers first:

```bash
rg --files shared
rg -n 'LaTeX|ZoomablePlot|ChapterRail|useStepMotion' shared ztautau-status-1994-20261022/slides ztautau-status-1994-20261022/components
rg --files ztautau-status-1994-20261022/components
```

The shared addon provides:

| Name | Use |
| --- | --- |
| `LaTeX` | `<LaTeX formula="\tau^+\tau^-" />`; optional `block` boolean. Synchronous KaTeX rendering; imports the KaTeX stylesheet itself. |
| `ZoomablePlot` | `<ZoomablePlot src="/figures/x.svg" alt="…" />`; click opens a fullscreen view. Prefixes `import.meta.env.BASE_URL`, so `/figures/…` paths from `public/` work under the Pages sub-path. |
| `ChapterRail` | `<ChapterRail :chapters="['Inputs', 'Selection']" :active="1" />`; `active` is 1-based. |
| `useStepMotion` | `useStepMotion(step, max, duration)`: anime.js driver that animates a stage toward the slide's click count while the slide is active and motion is allowed, and jumps to the final state otherwise. `step` is a getter, typically `() => props.step` with `$clicks` passed in from the slide. |
| `tex`, `mixed` | KaTeX strings for `v-html` inside Vue/SVG components; `mixed()` renders `$…$` fragments and escapes the rest. |
| `global-top.vue` | Page number on every slide except the first. Loaded automatically. |

Read a component's props and existing usages instead of guessing its API. These components are available in slides through the addon; new decks need no local copy. For example, a figure slide can contain:

```markdown
# Leading-track momentum

<div class="st-fig"><ZoomablePlot src="/figures/datamc/lead-p.svg" alt="leading-track momentum, data and simulation" /></div>
<div class="st-cap">leading-track <LaTeX formula="p" /> [GeV]<span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 41.2 / 38</span></div>
```

A click-driven animation lives in the deck and uses the shared driver:

```vue
<!-- My_Talk/components/StageSketch.vue -->
<script setup lang="ts">
import { useStepMotion } from 'slidev-addon-ztautau/composable/useStepMotion'
import { mixed } from 'slidev-addon-ztautau/composable/tex'
const props = defineProps<{ step: number }>()
const { reveal } = useStepMotion(() => props.step, 3, 900)
</script>

<template>
  <div :style="{ opacity: reveal(1) }" v-html="mixed('pair $\\tau^+\\tau^-$')" />
</template>
```

```markdown
---
clicks: 3
---

# The chain in three stages

<StageSketch :step="$clicks" />
```

When an explicit import is useful, use the workspace package name, as above or for components:

```ts
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
```

### Extend without copying

1. Use an existing component's props or wrap it in a distinctly named local component for one talk. The status deck's `DeckChapters.vue` is the pattern: it fixes that talk's seven chapter names and renders the shared `ChapterRail`.
2. If multiple talks genuinely need a new capability, make a small backwards-compatible shared API. Keep current defaults unchanged; pass labels, data, colors, or asset URLs from the deck.
3. Shared modules must not reach into `ztautau-status-1994-20261022/` or another deck. Dependency direction is deck → shared, never shared → deck.
4. Keep a unique implementation local until its reuse and stable interface are clear. Do not create `ComponentV2.vue` as a near-copy to change one label or color.
5. Before extracting apparently identical code, compare all copies and callers. Preserve intentional differences and output. Test every consumer after extraction.

Deck-local same-name components override shared components. Prefer a distinct local name; if an override is necessary, explain it in that deck's README. `global-top.vue` and `global-bottom.vue` are different: their layers are additive. Copying the addon's `global-top.vue` locally duplicates the page number rather than replacing it.

## 4. Styles and icons

Keep the generated `style.ts` imports in this exact order:

```ts
import '../shared/brand/fonts.css'
import '../shared/styles/main.css'
import '../shared/styles/animations.css'
import '../shared/styles/base.css'
import '../shared/styles/graphite.css'
import '../shared/styles/chapters.css'
import '../shared/styles/status.css'
```

`graphite.css` holds the Graphite & Gold theme and the common `.nju-subtitle`, `.nju-caption`, `.nju-takeaway`, and `.nju-source` helpers. `chapters.css` holds the chapter rail and chapter-bridge layout. `status.css` holds the status-report tables, `.st-*` figure grids and captions, $\chi^2/\mathrm{dof}$ badges, and semantic tags. Use the existing CSS variables such as `--fg-0`, `--fg-1`, `--card-bg`, `--accent`, and `--nju-accent` before inventing another palette. Common styling is shared; a talk's special layout should be local and narrowly scoped.

For a local extension, create `<deck>/styles/local.css` and append this import after the shared imports:

```ts
import './styles/local.css'
```

Do not replace the loader with CSS `@import`: shared UnoCSS directives would be left unexpanded. Do not copy shared CSS files into a deck.

Common UnoCSS presets and rules (including the `delay-*` safelist used by staged animations) already come from the addon. A deck-local `uno.config.ts` should contain only additions, for example an icon needed by dynamic markup:

```ts
export default {
  safelist: ['i-carbon:chart-line'],
}
```

Use the installed icon collections (`carbon`, `logos`, `ri`) first. Changing shared fonts, global selectors, presets, or animation defaults requires checking all decks.

## 5. Assets and public URLs

Place a new talk's figure at `My_Talk/public/figures/result.svg`. `<ZoomablePlot src="/figures/result.svg" />` resolves the deployment base itself. For other Vue-bound URLs, include the configured base rather than hard-coding the repository/deck or referencing `/public/`:

```markdown
<script setup>
const figureUrl = `${import.meta.env.BASE_URL}figures/result.svg`
</script>

# Result

<img :src="figureUrl" alt="Result of the study" />
```

The file is published as `/delphi-ztautau-presentation/My_Talk/figures/result.svg`. Pass that resolved URL to a reusable component when needed. A dev-root URL that works at `/` is not sufficient evidence that GitHub Pages paths work.

Record each figure's origin (source path, producing job or revision, and preferably a checksum) in the deck, as the status deck does in its `public/figures/MANIFEST.md`. Preserve existing public directories and filenames. Do not move a deck's images to `shared/`, rewrite existing links, or copy another talk's entire public directory. Add only the assets the new talk needs, with appropriate attribution.

## 6. Build, verify, and hand off

```bash
npm test
npm run build -- My_Talk
npm run build -- My_Talk --base /delphi-ztautau-presentation/My_Talk/
npm run export -- My_Talk
```

Single-deck output defaults to `My_Talk/dist/`. Export retains `--with-clicks --per-slide --wait-until none`; it requires Playwright Chromium. If it is missing, install it with `npx playwright install chromium`. Generate exports when requested, and do not overwrite or remove unrelated existing exports.

For the complete website, or after shared infrastructure changes:

```bash
npm run build:all
```

This recreates disposable `site/`, discovers every top-level `slides.md`, builds sequentially into `site/<deck>/` with base `/delphi-ztautau-presentation/<deck>/` (override with `-- --base /x/`), and copies `gh-pages/` into `site/`. CI performs one root installation and publishes the complete site; any failed build prevents deployment.

New decks are discovered automatically, but `gh-pages/` is not rewritten by the generator. Add the talk to the `talks` array in `gh-pages/index.html` separately when listing it is part of the request. A deck can still be built and published even when no landing entry points to it. Do not add private drafts as top-level decks to a deployment-bound change inadvertently.

Before handing off:

- Inspect the selected deck's initial/final click states and relevant intermediate steps, formulas, figure zoom, chapter rails, and fonts. Build success alone is insufficient.
- Check that every new number has a `SOURCES.md` entry and that simulation-only, Asimov, or statistics-only results are labelled on the slide. Rerun the deck's own checks (word count, leftover Unicode math) when it has them.
- For a shared change, compare all affected decks against their baseline with consistent browser/viewport/fonts and settled animations. Verify direct links/refresh, presenter/overview, public responses, and console errors.
- For dependency changes, preserve unrelated locked versions, run a clean root install, and rebuild all decks. Do not run `npm update`, regenerate the lockfile, or change CI as incidental authoring work.
- Review `git diff` and `git status`; exclude temporary decks, notes unrelated to the task, generated site output, dependencies, and QA screenshots from commits. Keep QA files under ignored `output/playwright/`.
- Report what changed, what you reused, the checks actually performed, and any limitations. Keep pre-existing issues separate. Push/merge/deploy only when requested.

For documentation-only edits, check links and examples and run the tests; a full slide rebuild is unnecessary. For general syntax and component conventions, consult [Slidev syntax](https://sli.dev/guide/syntax), [components](https://sli.dev/guide/component), and [directory structure](https://sli.dev/custom/directory-structure); the repository's pinned version and tested behavior take precedence over newer documentation examples.
