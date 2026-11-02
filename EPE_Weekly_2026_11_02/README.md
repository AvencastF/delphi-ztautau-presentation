# Measurement of Spin and Quantum Correlations in $Z \to \tau^+\tau^-$ Decays at LEP with DELPHI

Public-audience Slidev talk, ~25 minutes. Graphite & Gold presentation language of the EveNet CCNU seminar; title-page animation from this repository's landing page. Numbers are those of the [Internal_Note](../Internal_Note/) status deck (1992–1995 analysis, expected spin-fit sensitivity). This is not a status report.

```bash
cd /Users/avencastmini/ZtautauLEP/slides
npm run dev -- EPE_Weekly_2026_11_02
npm run build -- EPE_Weekly_2026_11_02
python3 EPE_Weekly_2026_11_02/data/checks.py 70
```

## Audience and writing

Students and faculty in HEP, not LEP or $\tau$-pair specialists. One or two ATLAS $\tau$ experts may be present. Owner decisions for this deck (2026-11-02):

- Conference narrative, not a group-meeting note. No timestamps, run names, job IDs, repository paths, or project shorthand on the slides. Terms that are not standard HEP language are defined when they first appear (spin density matrix, analysing power, concurrence, witness).
- Expected / simulation-only / statistics-only results are labelled once on the slide, not hedged in the body. Residual calibration items live in the backup and in presenter notes.
- Body text $\le$ 70 words (table cells, captions, tags, footers, and click-staged component copy excluded). One plain-words footer per content slide. No “Source:” footnote (2026-11-02); citations stay in `SOURCES.md` and presenter notes.
- LaTeX for every audience-visible symbol. Display precision: luminosities $0.1\,\mathrm{pb}^{-1}$; coefficients two decimals (polarisation uncertainties three); significances one decimal; fractions as percents without a decimal in prose.

## Slide map (owner correction, 2026-11-02)

1–10: opening physics, DELPHI introduction and animated selection.
11–14: quantitative selection evidence restored to the main talk: cumulative cutflow, energy-point yields, decay-category yields/composition and data/simulation kinematics.
15–21: reconstruction strategy, conventional method, EveNet classification and neutrino reconstruction.
22–29: forward-folding method, covariance validation and expected sensitivity.
30–32: measurement programme, summary and acknowledgements.
33–50: supporting diagnostics and detailed methods.

The latest pass refines the previous slides 11–14. Later slides retain the preceding revision for subsequent review; this is not a full rollback of the reconstruction/fit section. Numerical tables and plots are essential main-talk evidence. Prefer concise interpretation alongside them rather than replacing them with introductory text.

## Components

Deck-local: `TauScene` (landing-page canvas), `TalkChapterScene` (EveNet-style chapter backgrounds), `TalkChapters`, `Analyser`, `SpinState`, `EventSketch`, `Ambiguity`, `TwoHeads`, `SpinMatrix`, `GainBars`, `FitChain`, `AnalysisChain`. Shared: `LaTeX`, `ZoomablePlot`, `ChapterRail`, `useStepMotion`.

## Provenance

Every number is in [SOURCES.md](SOURCES.md), copied from Internal_Note. Spin-fit results are simulation-only, expected, statistics-only. Luminosities are the DELPHI run-table values after detector-quality selection.

## TODO

1. Listing on the repository landing page requires a separate request.
2. Visual check of every click state in the browser; reduced-motion stills of the chapter scenes.

## 2026-11-02 — opening-slide refinement

- Cover follows the CCNU seminar typography, divider and author hierarchy. Text occupies the left side; a local opacity mask protects it from the decorative scene. The canvas and animation behaviour are unchanged. This supersedes the earlier top-only cover placement.
- Motivation uses a full-height experimental-landscape / lepton-opportunity layout. Content remains readable at every click; clicks highlight the narrative rather than leaving blank regions. User screenshots are context, not evidence of current unpublished programme status.
- Spin-state slide expands all sixteen Pauli-basis entries (one fixed normalisation plus fifteen free coefficients). The coefficient matrix is called R, and its contraction with the Pauli basis defines rho; R is not mislabelled as the density matrix in a spin eigenbasis. Clicks highlight normalisation, axes, polarisations, correlations.
- Scope: slides 1, 2 and 5 and their deck-local components/styles. Internal_Note and shared infrastructure unchanged.

Validation for this refinement: deployment-base build passed; 10 root tests passed; all 43 slides passed the existing 70-word and LaTeX-substitution checks. Chromium at 1470x827: inspected opening slides 1/2/5 and their initial/final states; captured all three intermediate clicks on 2/5; checked cover motion and reduced motion, direct-link refresh, presenter and overview routes. Final motivation label bounds confirm no collision with neighbouring prose. No failed asset requests or KaTeX errors; headless browser reports a non-blocking Wake Lock permission denial. Design scan found only a pre-existing thick border on unrelated `.tk-points` styling. Screenshots and local QA scripts are under ignored `output/playwright/epe-opening/`. Full-deck visual QA remains outside this opening-slide pass.

## 2026-11-02 — academic opening (owner revision)

Supersedes the earlier opening-slide copy and motivation click design. Cover retains the exact full requested title, split into four lines with the decay process in LaTeX. Motivation preserves the left-hand experimental overview, replaces promotional wording on the right with phenomenological context, the DELPHI analysis and measurement objectives, and has no click stages. Page 3 introduces “Spin density matrix and quantum observables”: decay spin analysis, pair-state parametrisation, entanglement and Bell observables. Use academic, descriptive wording throughout future refinements; avoid advertising-style slogans.

## 2026-11-02 — concise motivation and spin introduction

Owner revision: page 2 labels the ATLAS H to ZZ result as hypothesis testing, removes the H to WW group-status caption, and keeps only phenomenology and the proposed DELPHI Z-pole measurement in the right column. No click stages. Page 3 now reads “Accessing the quantum state through spin”, with one supporting sentence about decay angles; the long outline and context label are removed.

## 2026-11-02 — spin opener composition

Page 3 uses a deck-local `tk-spin-intro` class: bounded left text column, three-line title with gold emphasis, short divider, supporting sentence and compact decay angles → spin observables → density matrix relation. A left-side mask separates text from the existing illustrative animated spin-pair scene. Other chapter styles and shared components are unchanged. Deployment-base build and browser rendering checked; no KaTeX errors.

## 2026-11-02 — restore full-SDM animation

Owner correction: expansion of the SDM supplements the existing animation; it does not replace it. The Full Spin Density Matrix slide restores the original animated pair sketch, precessing spin arrows, and three click stages (axes, polarisations, correlations), alongside the expanded Pauli coefficient matrix and rho definition. Removed the normalisation explanation; the only explanatory groups are polarisations and correlations. The fixed identity entry remains part of the mathematical expansion. Page 3's section opener is unchanged. Browser checked all four states, live arrow motion and reduced-motion stability; no KaTeX errors. This supersedes the static-matrix-only layout.

## 2026-11-02 — helicity basis and SDM typography

Full SDM explicitly labels the helicity basis (n,r,k), retaining the flight/production-plane/normal definitions below the schematic. Increased particle, axis and coefficient labels in the animation; reduced matrix text from 25 to 20 px. Removed duplicate explanatory text inside the schematic while retaining its stages and motion.

## 2026-11-02 — simplified pair schematic

Owner revision removes both correlation curves, the shared-state label and the precessing blue/orange arrows. Helicity axes are dashed green and translated below the tau-plus particle with unchanged directions. Tau labels are reduced to fit their circles. Coefficient reveals and matrix highlighting remain click-driven. This supersedes the earlier precessing-arrow design. All four states visually checked.

## 2026-11-02 — helicity-axis layer correction

Owner clarified “below” means drawing order, not spatial displacement. Axes again originate at tau-plus, but are painted before the particle circle and label so they sit behind them. This supersedes the translated-axis placement above. Dashed green styling and smaller tau labels remain.

## 2026-11-02 — QIS introduction, page 6

Replaces “Three tests” and its simulated-result table with a static three-column introduction to concurrence, quantum magic and optimal CHSH, derived from full SDM. No results appear. Matches the owner's reference topics with corrected concurrence eigenvalue definition, general optimal CHSH formula and explicit pure-state scope for the magic interpretation. The S_p shorthand keeps the full B/C moment expression readable. No click stages.

## 2026-11-02 — balance QIS columns

Condensed QE to one concurrence-interpretation line, one witness equation and a short sufficiency qualification. Removed the separate witness subsection; all three columns share the same definition/criteria boundary and similar overall depth. The spin-flip definition remains visible. Browser checked page 6 with no KaTeX errors.

## 2026-11-02 — LEP-1 and DELPHI introduction

Page 8 now introduces LEP-1 and the detector, explains the owner's 1992–1995 choice, and makes the public archive plus preserved simulation/reconstruction software visible. Detailed luminosity and energy-point statistics are removed from this introduction; their historical provenance remains. Two experiment-overview columns sit above a data/software section, with clickable academic citations. Only this page and deck-local styles changed.


### 2026-11-02 — DELPHI introduction: three questions
Page 8 reorganized into experiment, Z-pole tau-spin motivation, and feasibility. Keywords replace prose; public archive and 1992–1995 owner selection rationale retained. Sources remain the CERN LEP and DELPHI Open Data references above. Clean initial state and tau-decay spin analysis are qualitative motivation, not a sensitivity or validation claim.


### 2026-11-02 — PID and preservation links
Page 8 emphasizes PID together with tracking/calorimetry for identified visible tau daughters and momenta; no claim of detecting neutrinos or perfect reconstruction. Archive text links to CERN Open Data. Software text links to https://github.com/delphi-fullDST-edm4hep/delphi-sim-pipeline (README verified 2026-11-02), a modern-generator front end to legacy DELSIM simulation and DELANA reconstruction.


### 2026-11-02 — Event topology definitions
Page 9 retains three animated reveals, replaces paragraphs with four short definition blocks, and separates track/photon labels using leader lines. Hemisphere divider is perpendicular to thrust in the schematic. Visible candidates and the one-prong analysis scope are explicit. Removed the selected yield and detailed cuts from the displayed introduction; existing cutflow provenance remains applicable. Removed erroneous half-beam-energy wording.

## 2026-11-02 — reconstruction and forward-folding narrative

Owner-directed rewrite from slide 11 onward. Replaced long prose with aligned method definitions, compact equations and figure annotations. Two separate EveNet fine-tunings share the pretrained starting point; the direction model is conditional diffusion, not a generic regression head. Citation updated to the Nature Machine Intelligence publication. The current joint_fit Model C is the source for the forward-folding description, rather than the older spin_fit PSD implementation. The fit uses 2,400 nominal bins, full event-derived covariance and unconstrained linear GLS. The witness-null is not identified with the full set of separable states. Expected significance uses the constrained/free chi-squared statistic; tail extrapolation and reference-model status remain visible. Full coefficients, legacy reconstruction comparisons and different plot cohorts are labelled separately. Backup tag language now gives numerical tag thresholds without assigning invented working-point names.

Validation of the reconstruction/fit rewrite: deployment-base build passed; 10 root tests passed; all 50 slides passed the deck word/LaTeX checks. Chromium at 1470x827 captured slides 11–50 at initial and final click states; main and backup contact sheets reviewed, with the forward-folding formulas checked at full size after a CSS fix. Revised animated gain/fit-chain final states rechecked. No KaTeX errors; only the existing headless Wake Lock permission message. QA artifacts: ignored output/playwright/epe-opening/. Intermediate click states, all plot-zoom interactions and presenter routes were not exhaustively rechecked in this pass. No analysis jobs, training, export, deployment or changes to Internal_Note were performed.

## 2026-11-02 — restore quantitative selection slides

Owner correction: earlier revision condensed the presentation too far. Restored previous pages 11–14 to their original main-talk positions; removed their duplicate backup inclusions. Cutflows now use deck-local Markdown derived from Internal_Note, preserving its source comments and values; the internal deck is unchanged. Page 11 separates data and simulation count columns from year ratios. Page 12 retains all eight points, luminosities and statistical ratio errors. Page 13 retains all ten categories, year ratios and true-pair fractions with their explicit tau-only denominator. Page 14 enlarges the two existing plots and adds their recorded chi-squared values. Precision of rate and signal fraction is retained at 0.982 and 96.4 percent. Cutflow luminosities keep the source-table precision as an exception to the default 0.1 inverse-pb display rule.

Validation: deployment-base build passed; all four pages visually inspected at 1470x827, with no KaTeX errors. Only the existing headless Wake Lock message was reported. No scientific results recomputed.


## 2026-11-02 — candidate definitions before the cutflow
New slide 10, immediately after the topology slide, reuses EventSketch with an identification variant. Four click-highlighted definitions: electron ELID>=3 with muon veto; muon numeric MUID>=7 with electron veto; charged-hadron pion with measured N_gamma=0; rho with N_gamma=1 or2 and 0.5<m(track+photons)<1.04GeV. Common hadron momentum threshold p/Ebeam>0.05 and nearby photon E>0.5GeV, DeltaR<0.3 are visible. The full hadron predicate remains in speaker notes and the detailed ID backup.
Sources inspected live: tau_analysis/analysis/exclusive_id.py (hadron_inputs, classify_leg and numeric_ge7/final_hadron call sites), analysis/photon_quality.py, docs/EXCLUSIVE_DECAY_HANDOFF_20261007.md. Unavailable/ambiguous inputs retain residual status; conflicting positive lepton tags are conflicts. No production definitions changed.
The animated cutflow now starts at slide11; quantitative selection pages move to12–15; all later slide numbers increase by one. Build and all four new slide states checked in Chromium at1470x827; formulas render without errors.


### 2026-11-02 — two-click candidate definitions
Slide10 now has two clicks: electron H1/muon H2, then pion H1/rho H2. Photons appear only in the second state. ELID/MUID are defined as DELPHI identification codes with the numerical thresholds and competing-tag veto. The hadronic state displays the common momentum/lepton requirements and both alternative routes: RPROCO2/3 plus HPC E/p<0.6 or certified absent association; alternatively complete HCAL mean occupied-layer energy>=3GeV. HPC/HCAL and photon cuts are defined below the schematic. Source predicates and validity requirements remain in the slide notes; source is the same inspected exclusive_id.py and handoff document. Supersedes the previous four-definition click design.


### 2026-11-02 — expand numerical identification semantics
Electron accepted codes explicitly mapped:3 loose,4 standard,5 tight (ParticleId.cpp PSCELD). Muon flags:1 very loose,2 loose,4 standard,8 tight,16 HCAL (ParticleId.cpp PSCMUD; archived literature-code-report.md and SKELANA manual p51). For valid five-bit values, numeric>=7 is exactly value7 or any value with bit8/16; this does not relabel the cut as one tightness level or replace it by mask28. Hadron RPROCO values2/3 expanded to standard/tight combined RICH and TPC dE/dx pion identification (converter README lines463–479). Existing E_HPC/p<0.6, certified absence route, HCAL mean>=3GeV and momentum/photon/mass cuts retained. These are decoded stored decisions, not newly derived elementary detector cut thresholds. Primary source linked on slide: https://opendata.cern.ch/record/80502/files/skelana.pdf . Full numeric reconstruction thresholds of ELECID/MUCAL2 are not asserted from ordinal labels. No analysis selection changes.

### 2026-11-02 — fixed illustration and ID blocks
Removed the bottom electron/muon identification-code strip. The schematic uses fixed height/top alignment across both clicks. Definitions now have separate colour-coded panels: pink H1, mint H2 and amber common hadron ID, with numeric electron levels/muon flags and separated alternative hadron routes. Scientific predicates and other slide content are unchanged. Both states visually checked after deployment-base build, without overlap or KaTeX errors.


## 2026-11-02 — reconstruction architecture refinement
Owner requested more technical detail on previous16–18. Now16 is the parallel conventional/ML reconstruction chart;17 is EveNet inputs, independent task adaptation, outputs and data split. The former conventional-only page is folded into16; file retained. Performance plots now start18;50 slides total. All subsequent plots/tables preserved. Diagram labels and parameter captions on these two information-rich pages exceed the simple text-count heuristic (81/99 words before arrow markup); accepted for this requested detailed schematic, not a new global prose limit. The two LaTeX heuristic warnings are prose class/step counts, not substituted particle notation.


## 2026-11-02 — EveNet animation restored
Slide17 now opens the EveNet shell on one click to reveal PET, classifier object encoder and conditional diffusion. Unused heads removed. Separate task fine-tuning remains explicit. FiLM conditions and directional targets sit below the animated chart; full linked NMI citation included at owner request. Browser QA covers initial and expanded states at1470x827 on the deployment-base preview; remaining slides unchanged.

## 2026-11-02 — quantitative classifier slides18–19
Replaced sparse introduction with original internal-note confusion matrices (classic, ML, difference) and all ten efficiency–purity panels. Explicit classic/argmax/threshold-scan definitions and four-channel numerical comparison added. Earlier pipi fourfold-efficiency statement corrected: fourfold purity; efficiency51.7→74.6%. No extra footnotes; provenance in SOURCES and presenter notes. All quantities labelled held-out simulation. Figures retain click-to-enlarge. Original plot labels are preserved.


## 2026-11-02 — reconstruction section expanded
Former20–21 replaced by three pages:20 detector input families and embedding/FiLM paths;21 ambiguity geometry and branch-sign performance;22 tau angular quantiles and momentum RMS. Subsequent fit section starts23;51slides total. Old mixed1994-plot/all-years-summary removed from main talk. Energy residual degradation is shown alongside spatial improvements. No independently evaluated neutrino distribution is available in this local all-years archive; diagram illustrates p_missing=p_tau-p_visible and defines leptonic missing systems. Browser QA covers all three pages at1470x827.


## 2026-11-02 — reconstruction section ordering
Owner order:17 EveNet architecture;18 general detector inputs (ml-neutrino.md retained as filename);19–20 CLS comparison and working points;21–22 Neutrino ambiguity and resolution. CLS:/Neutrino: title prefixes added. Scientific content unchanged;51slides total.

## 2026-11-02 — resolution plots and branch explanation
Slide21 defines best truth-aided branch and signed impact-parameter geometry. Slide22 replaces tables with three direct analytical/EveNet comparison plots, with plain-language definitions below: median,84% containment and residual RMS. Underlying cohort and numerical sources unchanged. No raw residual distributions available in the local all-years archive were inferred from aggregate metrics.


## 2026-11-02 — web-native charts and concise labels
Page22 title: Neutrino: reconstruction resolution. Three native paired-dot charts match deck typography/colors and expose exact values on hover. Page21 removes truth-aided branch; hybrid explicitly means analytical solution closest to ML, not an ML event region. Footnotes removed from these pages; metric definitions remain in the content.


## 2026-11-02 — ambiguity animation
Page21 now has three clicks: initial cone intersections; symmetric-momentum ambiguity/conditional mean; displaced-track IP geometry; conditional ML inference and default-versus-EveNet performance. Hybrid removed. Scientific scope is ideal two-body hadronic geometry; leptonic decays and full-model performance not claimed to satisfy exact cones. All four states visually checked; no footnote.

## 2026-11-02 — fit section rebuilt from archived Model C results

Owner request supersedes the previous main fit narrative. Main 24–32: forward folding and literature; joint sample/region combination; correlated angular fit; all 15 SDM coefficients; regional statistical variance contributions; event-level toy validation; QIS reference-toy distributions; null tests; linearized covariance propagation. Outlook/summary now 33–34, end35, backup starts36. Earlier reconstruction slides1–22 unchanged.

No visible source footers in this section. Two linked methodological/historical citations appear on the forward-folding slide as explicitly requested. Compact HEP tables and plots take priority over narrative prose. Regional decomposition is of statistical variance in the combined estimator; systematics and MC-template statistics remain excluded. Results are expected, not fitted DELPHI data. Magic is included in toy distributions and covariance propagation; no calibrated magic significance is available. W7sigma is an extrapolated, calibrated toy tail, not a directly sampled probability. Retain these scientific distinctions in future revisions.

Validation: deployment-base build passed; 10 root tests passed. Chromium at1470x827 inspected every rebuilt slide24–32 after final edits: no KaTeX errors, no visible overlap/clipping. Static pages have no click stages. Direct slide links were tested. Only known non-blocking Wake Lock denial appeared. All changed slides pass70-word and LaTeX checks; pre-existing slide16 remains81words. Fisher/covariance sum closure asserted against saved NPZ. QA screenshots: ignored `output/playwright/epe-opening/fit-24.png` through `fit-32.png`. Presenter/overview and earlier/backup slides were not re-audited in this pass. Port3030 untouched.

Slide26 owner refinement: one covariance definition, actual pion-region normalised covariance plot, diagonal/off-diagonal explanations, and non-redundant-bin wording. Removed chi-square and Fisher formulas from this slide. Build and Chromium1470x827 visual check passed; no KaTeX substitutions. Existing slide16 word-count excess unchanged.

## 2026-11-02 — fit interpretation and compact QIS summary

Owner changes: remove equal-histogram-totals block on26 and the unconstrained-reference callout on27. Expected/Asimov labels and numerical table remain. Slide28 now defines regional variance shares operationally, gives the46.5% pion-pair witness example, and distinguishes statistical influence from leave-one-region-out precision loss. Formula derivation retained in presenter notes. Slide29 adds the reference-model toy conclusion (no significant bias; statistical uncertainties reproduced). Old31–32 merged into31 with values, propagated/toy widths, null boundaries/counts/calibration, significances, magic95%interval, and all three observable definitions retained. Subsequent slides shift down one; deck52slides. Original separate covariance-propagation Markdown remains unreferenced, preserving content history.

Verification for this revision: deployment-base build and10root tests passed. Chromium1470x827 checked slides24–32, including all changed pages and merged31; no KaTeX errors or content clipping after compact-layout adjustment. Only known Wake Lock denial. Changed slides pass70-word/LaTeX checks; existing slide16 word-count excess remains. Port3030 untouched.

## 2026-11-02 — single closing slide

Owner requested removal of the remaining tail after31 and a combined next-plan/conclusion slide. Manifest now ends at32 (`closing.md`); previous outlook, summary, end, and backup files retained on disk but no longer included. Closing slide covers per-year/per-energy track/HPC calibration, pion-channel ML optimisation, systematics and final inference choices; conclusions summarise the full-SDM objective, expected QIS results, LHC-to-LEP fine-tuning and further QIS/spin/CP observables. “First” is an objective; expected magic is not relabelled as a data measurement. Order1%systematics is an owner-provided provisional estimate, not validated precision.

Closing verification: deployment-base build passed;10root tests passed. Chromium1470x827 inspected final32/32 layout, with all eight items visible and no KaTeX errors. Slide32 meets70-word limit; pre-existing slide16 remains over. Removed tail is absent from slide manifest; source files retained. Port3030 untouched.

## 2026-11-02 — six kinematic distributions on15

Owner requested broader data/MC evidence. Slide15 is now a3x2grid: leading-track momentum, polar angle, nearby-photon energy, visible pair mass, radiative energy and momentum ratios. Uses six original inclusive Internal_Note SVGs, full data/MC ratios and existing click-to-enlarge; no new normalization or data manipulation. Same sample/year coverage. Scope limited to15, its local style, added plot assets, and provenance.

Validation for15: deployment-base build and10root tests passed; Chromium1470x827 six-panel layout inspected, all ratio panels retained without clipping, all six enlargement dialogs opened/closed with loaded images. No KaTeX errors. Deck checks retain only pre-existing slide16 word-count excess. Concurrently present ml-scaling slide and manifest changes preserved; current deck33slides. QA under ignored output/playwright/epe-opening/kinematics-15.png. Port3030 untouched.
