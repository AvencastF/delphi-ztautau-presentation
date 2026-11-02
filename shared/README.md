# Shared presentation infrastructure

Start with the [authoring guide](../docs/authoring.md) and [agent instructions](../AGENTS.md).

- `slidev-addon-ztautau/` is a private npm workspace linked by the root installation. It extends the default Slidev theme; it is not a separate presentation or a replacement theme.
- `slidev-addon-ztautau/components/` holds reusable, talk-independent components: `LaTeX.vue` (synchronous KaTeX; `formula`, optional `block`), `ZoomablePlot.vue` (click-to-fullscreen figure that resolves `import.meta.env.BASE_URL`), and `ChapterRail.vue` (`chapters`, 1-based `active`). Consume them from slides through the addon, or import from `slidev-addon-ztautau/components/<Name>.vue` when necessary.
- `slidev-addon-ztautau/composable/` holds reusable helpers: `useStepMotion.ts` (anime.js click-step driver) and `tex.ts` (`tex()` and `mixed()` KaTeX strings for Vue/SVG components). Shared code must not import from a deck directory.
- The addon's `global-top.vue` (page number, hidden on the first slide) and its UnoCSS/Vite configuration (including the `delay-*` safelist) are loaded for every deck that opts into it. Global layers are additive; do not copy them into decks.
- `styles/` contains common CSS: `main.css`, `animations.css`, `base.css`, `graphite.css` (Graphite & Gold theme and the `.nju-subtitle`/`.nju-caption`/`.nju-takeaway`/`.nju-source` helpers), `chapters.css` (chapter rail and chapter bridge), and `status.css` (status-report tables, `.st-*` figure grids, captions, $\chi^2/\mathrm{dof}$ badges, semantic tags).
- `brand/fonts.css` and `brand/fonts/` bundle the DM Sans variable font and its OFL licence so decks render offline.
- Deck `style.ts` files import `brand/fonts.css`, then `main.css`, `animations.css`, `base.css`, `graphite.css`, `chapters.css`, and `status.css` in that order, followed by any deck-local styles.

Do not put talk Markdown, datasets, result figures, provenance files, generated output, or per-deck dependency copies here. Prefer existing props and CSS variables; preserve defaults when extending shared behavior. Keep one-off changes, such as a talk's fixed chapter list, local and narrowly scoped.

Changes here can alter all presentations. Run `npm test` and `npm run build:all`, inspect affected renders/interactions against a baseline, and document any intentional change. Adding a new talk should normally require no changes to this directory.
