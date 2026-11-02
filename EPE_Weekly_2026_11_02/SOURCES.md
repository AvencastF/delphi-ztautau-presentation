# Sources — EPE_Weekly_2026_11_02

Slide-by-slide provenance of every number shown. Convention as in the status deck: dated sections; a later section supersedes earlier rows for the same slide.

Primary local source for all analysis numbers: the status deck [`Internal_Note`](../Internal_Note/) (its `slides/*.md` with presenter notes, its `SOURCES.md`, and `data/nersc-all-years-rq-20261026/`), which in turn cites the project artifacts (`/Users/avencastmini/ZtautauLEP/artifacts/...`), the project guide, and the NERSC runs. Rows below name the Internal_Note slide the value was copied from; the artifact path is in that slide's notes and in `Internal_Note/SOURCES.md`. "Derived" marks values computed for this deck.

## 2026-11-02 — EveNet scaling figure

Inserted after the detector-input slide and before the classification comparison. Figure file `public/figures/ml/evenet-scaling.png`, sha256 `60f88c08aff1390f`, copied unmodified from `~/Downloads/ML4Jets.png` (4968×2972) on 2026-11-02, replacing the earlier 1024×612 screenshot. Printed on the figure, not recomputed: scratch fit \(2.53\,N^{-0.114}\pm 0.03\); FM fit \(0.80\,N^{-0.031}\pm 0.04\); vertical axis \(1-\) top-1 accuracy. The user identified the red FM curve as EveNet pretrained on LHC data and fine-tuned on LEP, and the blue curve as training from scratch on LEP. That identification is not printed on the axes.

## 2026-11-02 — cutflows included from Internal_Note

Slides 10–13 are the Internal_Note files themselves (`cutflow-anim.md`, `cutflow-inclusive.md`, `cutflow-points.md`, `cutflow-children.md`), referenced from this deck's `slides.md`. No number was recopied. Provenance, exact values, and the run-quality caveat stay in those slides' presenter notes and in `Internal_Note/SOURCES.md` (2026-10-31 rows for the 1992–1995 rerun). The composition matrix and the two appendix cutflow tables stay in Internal_Note; this talk still summarises composition on `channels.md`.

## 2026-11-02 — EPE weekly revision

- Deck folder renamed to `EPE_Weekly_2026_11_02`. Cover: Yulei Zhang, EPE weekly, 2 November 2026. Title sits at the top of the landing-page scene.
- Slide 2 replaced. \(t\bar t\) entanglement: ATLAS Collaboration, Nature 633 (2024) 542. \(H\to ZZ\): ATLAS Collaboration, Phys. Rev. Lett. 137 (2026) 111804 (published 11 September 2026). \(H\to WW\): stated as ongoing; no paper cited. The kinematic contrast (observables split across \(t\bar t\) phase space, coincident at the \(Z\) pole) is the seminar point, not a new numerical result.
- Main-slide titles shortened. Numbers on later slides are unchanged.

## 2026-11-02 — public 25-minute rewrite

Main-deck order after the rewrite (cover through thank you, then backup). Numbers are unchanged from the first-draft rows below; only the slide index and which plots stay in the main text changed.

| main # | file | content |
|---|---|---|
| 1 | cover | title scene |
| 2 | motivation | superseded 2026-11-02: qubit landscape, see the EPE weekly revision |
| 3 | ch-spin | chapter, no numbers |
| 4 | analyser | analysing powers, 2.2 mm |
| 5 | spin-state | density-matrix parametrisation |
| 6 | entanglement | SM $C_{nn,rr,kk}$, $W$, concurrence, Bell |
| 7 | ch-delphi | chapter |
| 8 | delphi | $137\,\mathrm{pb}^{-1}$, 8 points, 1994 share |
| 9 | event | 56,472 selected, $160^\circ$ |
| 10–13 | Internal_Note cutflow-anim, cutflow-inclusive, cutflow-points, cutflow-children | included by reference 2026-11-02; numbers not recopied |
| 14 | datamc | 56,472; 0.98; 96 % |
| 15 | channels | cut-based purities |
| 16 | ch-ml | chapter |
| 17 | ambiguity | 0.59 / 0.72 / 0.91; $1.55^\circ\to0.88^\circ$ |
| 18 | model | EveNet arXiv:2601.17126 |
| 19 | ml-channels | 0.41→0.88, 0.57→0.79 |
| 20 | ml-direction | 0.59→0.72; artefact $\mp1.8$ |
| 21 | ch-fit | chapter |
| 22 | workflow | 16×15×10 (derived 2,400) |
| 23 | template | $C_{kk}$ template figure |
| 24 | expected | matrix and derived $\pm$ |
| 25 | gain | concurrence $\sigma$ per point |
| 26 | significance | $7.0\sigma$, $2.2\sigma$ |
| 27 | ch-outlook | chapter |
| 28 | outlook | no new numbers |
| 29 | summary | repeats the data/simulation, identification, and significance slides |
| 30 | end | close |

Moved to backup, numbers unchanged: `chain`, `fit-chain`, `covariance`, `test`. New chapter scenes are decorative and carry no measured values.

## 2026-11-02 — first draft (public talk)

### Slide 1 — cover
- Title, author Yulei Zhang, seminar EPE weekly, date 2 November 2026: user request of 2026-11-02. Supersedes the unset venue/date note.
- Animated scene: port of `gh-pages/assets/tau-scene.js` (decorative; the three marked energies 89.4 / 91.2 / 93.0 GeV only label the schematic line shape).

### Slide 2 — motivation
- "Entanglement observed in top-quark pairs at the LHC (2024)": ATLAS Collaboration, Nature 633 (2024) 542; CMS Collaboration, Rep. Prog. Phys. 87 (2024) 117801. Public references, not local artifacts.
- "Millions of Z decays recorded 1989–1995": LEP1 running period; public knowledge, no specific number shown.
- "15 coefficients": 6 polarisations + 9 correlations, standard two-qubit parametrisation (Internal_Note `fit-observables.md`).

### Slide 3 — spin state (component `SpinState.vue`)
- Density-matrix formula and frame definitions: Internal_Note `fit-observables.md` notes (ρ = ¼(1⊗1 + Σ B⁻ σ⊗1 + Σ B⁺ 1⊗σ + Σ C σ⊗σ); k along the τ flight, r in the production plane, n normal).
- Presenter-note only: LEP combined A_τ = 0.1439 ± 0.0043, ALEPH/DELPHI/L3/OPAL + LEP EWWG, Phys. Rept. 427 (2006) 257 (public reference; not shown on the slide).

### Slide 4 — analyser (component `Analyser.vue`)
- Analysing powers π 1.00, ρ 0.41, e −0.33, μ −0.34: Internal_Note `fit-observables.md` table (legacy averaged values used by the fit).
- Branching fractions, shown as central values: PDG 2024 τ listings, https://pdg.lbl.gov/2024/listings/rpp2024-list-tau.pdf. πν 10.82 ± 0.05 % (Γ9); ρ row is τ → π π⁰ ν 25.49 ± 0.09 % (Γ14); eνν 17.82 ± 0.04 % (Γ5); μνν 17.39 ± 0.04 % (Γ3). Uncertainties are not on the slide.
- Angular distribution ½(1 + κ P cos θ), drawn for the pion at P = 1: standard formula. Owner decision 2026-11-02: the analysing power on the slide is κ.
- Flight length ≈ 2.2 mm at E_τ = 45.6 GeV: derived, γcτ = (45.6/1.777) × 87.0 μm with the PDG τ lifetime 290.3 fs (cτ = 87.0 μm); as in Internal_Note `fit-why.md` notes ("about 2 mm").

### Slide 5 — entanglement, concurrence, Bell
- Definitions W = C_nn − C_rr + C_kk − 1 (separable ⇒ W ≤ 0), concurrence ½(|C_nn − C_rr| + C_kk − 1), Bell |C_kk − C_rr| > √2: Internal_Note `fit-observables.md` and `fit-hypothesis.md` notes (joint-fit README).
- Simulation reference values C_nn +0.80, C_rr −0.81, C_kk +1.03; W 1.64; concurrence 0.82; |C_kk − C_rr| 1.84: Internal_Note `fit-results.md` and `fit-toys.md` (combined 1992–1995 reference: C_nn +0.7965, C_rr −0.8135, C_kk +1.0307; W 1.6407, concurrence 0.8204, Bell 1.8442; `artifacts/joint-fit-20261031/modelC/combined-ml/summary.md`).
- "C_kk slightly above 1 … finite precision of the simulated reference": Internal_Note `fit-results.md` / `fit-caveats.md` notes (reference density matrix eigenvalue −0.013; treated as an analysing-power systematic per the owner's brief, origin not studied).

### Slide 7 — LEP and DELPHI table
- Luminosities 24.04; 9.67 / 16.45 / 9.99; 45.79; 8.45 / 13.78 / 9.32 pb⁻¹ (run-quality good-cassette values, user-supplied DELPHI tables, uncertified): Internal_Note `status-1992-1995.md`, `inputs-goodrun.md`; shown rounded to 0.1 pb⁻¹. Total ≈ 137 pb⁻¹: derived (sum = 137.49).
- Energies 91.3; 89.4 / 91.2 / 93.0; 91.2; 89.4 / 91.3 / 93.0 GeV: Internal_Note `status-1992-1995.md` (91.278; 89.432 / 91.223 / 93.015; 91.202; 89.438 / 91.295 / 92.965), rounded.
- "1994 alone is a third": derived, 45.79 / 137.49 = 0.33.
- Vertex detector rφ-only before 1994, z readout from 1994: Internal_Note `ml-nu-allyears.md` ("no vertex-detector z readout before 1994") and public DELPHI detector descriptions.

### Slide 8 — analysis chain (component `AnalysisChain.vue`)
- Data 2.4 M events (2,395,361 converted, 334 files): Internal_Note `inputs-data.md`.
- Simulation 38 M events (38,440,229 converted; 42,741,000 generated; 17 campaigns; seven processes; PYTHIA 8.315, BHWIDE 1.05; detector descriptions per year): Internal_Note `inputs-mc.md`.
- Selection 18 cuts, 56,472 data events, data/MC 0.982: Internal_Note `cutflow-anim.md`, `datamc-inclusive-01.md` notes.
- ML trained on half of the simulation: Internal_Note `ch-ml.md`, `ml-split` policy (owner decision 2026-10-27).
- Fit 16 regions × 15 histograms: Internal_Note `fit-inputs.md`.

### Slide 9 — event sketch (component `EventSketch.vue`)
- Cut values quoted in the component text (opening angle > 160°, one charged track per hemisphere, ≤ 3 neutral objects, 18 cuts): Internal_Note `cuts-1.md`, `cuts-2.md`.
- Identification rules (lepton tags; π = hadron without nearby photon; ρ = hadron + 1–2 photons, 0.5 < m < 1.04 GeV): Internal_Note `children-id.md`. "m ≈ 0.77 GeV" in the sketch is the PDG ρ mass, illustrative.

### Slide 10 — data and simulation
- Figures: `public/figures/MANIFEST.md`. χ²/dof (notes only): p/p_beam 73.9/42, visible mass 129.1/49 (Internal_Note `datamc-inclusive-01.md` and `datamc-residuals.md` notes).
- 56,472 data / 57,520.06 simulated (0.982); Z→ττ 55,456.6 ⇒ ≈ 96 % (derived): Internal_Note `cutflow-anim.md` notes.
- 1994 / 1995 rates 2–3 % low, simulation side: Internal_Note `inputs-goodrun.md` notes (0.969 / 0.977; about half attributable to the 1994/1995 detector descriptions).

### Slide 11 — cut-based channel composition
- Derived from the signed-weight composition table in Internal_Note `confusion.md` (notes give the unlisted rows). Column sums over tau rows + other-1-prong + other-tau rows: eπ 4,226 (correct 1,789 = 42 %; other listed τ pairs 1,896 = 45 %); μπ 4,729 (2,032 = 43 %; 2,112 = 45 %); ππ 2,449 (423 = 17 %; 1,479 = 60 %); πρ 2,996 (984 = 33 %; 989 = 33 %); ρρ 921 (503 = 55 %; 14 = 2 %). Lepton-channel purities 74 / 92 / 84 % and the Bhabha / Z→μμ contaminations: the cut-based panel of `ml/confusion-purity.svg`. Non-τ background in the hadron channels (< 1 %) neglected in these sums.

### Slide 13 — direction ambiguity (component `Ambiguity.vue`)
- Correct branch 0.591 (conventional), 0.910 (best possible), 0.724 (network); π-leg median 1.55° → 0.88°; medians 0.88–1.18° per leg type; 2,359,482 held-out events: Internal_Note `ml-ambiguity.md`, `ml-why.md`, `ml-nu-allyears.md` notes.

### Slide 14 — model (component `TwoHeads.vue`)
- EveNet paper arXiv:2601.17126: EveNet seminar cover (`/Users/avencastmini/EveNet-Presentation/CCNU_Seminar/slides/cover.md`).
- Particle token, 84 conditions incl. √s and year, pretrained checkpoint, training/hold halves, ~10 % gain from pretraining: Internal_Note `ml-models.md` notes.
- Classifier classes: ten τ decay pairs plus background classes (`ml/confusion-purity.svg` axis labels).

### Slide 15 — decay-mode identification
- Accuracy 0.408 → 0.884; per year 0.875 / 0.886 / 0.887 / 0.886; signal fraction 0.573 → 0.786; ππ efficiency 0.746 / purity 0.664; ee purity 0.867: Internal_Note `ml-cls-allyears.md`. ππ cut-based purity 0.173: `confusion.md`. "Four times the efficiency": read from `ml/efficiency-purity.svg` (cut-based ππ point ≈ 0.18 vs 0.75).

### Slide 16 — τ direction
- 0.59 → 0.72, best 0.91; 1.55° → 0.88°; medians ≤ 1.18°; C_rn / C_nr −1.756 / +1.752 (conventional) vs +0.000 / −0.002 (network), truth 0: Internal_Note `ml-why.md`, `ml-nu-allyears.md` notes. 1992–1993 weaker (no VD z readout): `ml-nu-allyears.md`.
- Figure: 1994 held-out evaluation (`ml/direction.svg`), 1994 values 0.746 and 0.81° in the notes.

### Slide 18 — fit chain (component `FitChain.vue`)
- 16 regions × 15 observables × 10 bins = 2,400; fit requirements; 32,336 combined simulated events after the fit cut; full covariance, closed-form solution, iminuit agreement 5e-5; 20,000 null toys: Internal_Note `fit-flow.md`, `fit-inputs.md`, `fit-model.md`, `fit-hypothesis.md` notes.

### Slide 19 — template fit
- Figure `fit/template-ckk.svg` (see MANIFEST); 670 weighted ππ events; floating 87.4 %, fixed 11.7 % + 0.9 %: Internal_Note `fit-template.md`, `fit-inputs.md`.

### Slide 20 — covariance and validation
- Pull widths naive up to 2.28 (C_kk), final 0.972–1.026; closure 1.000000 (max 2.9e-12); 0.27 % beyond 3σ; z-spread 1.003; error ratio final/legacy 0.936–0.988 (→ "up to 6 %"), C_nr/C_rn 1.066/1.065: Internal_Note `fit-covariance.md`, `fit-validation.md`, `fit-precision.md` notes.

### Slide 21 — expected precision (component `SpinMatrix.vue`)
- σ(B): 0.0313, 0.0357, 0.0315 / 0.0314, 0.0358, 0.0316 → shown 0.031, 0.036, 0.032; C_nn +0.7965 ± 0.1063, C_rr −0.8135 ± 0.1281, C_kk +1.0307 ± 0.1372; off-diagonal σ 0.1693, 0.1503, 0.1684, 0.1715, 0.1512, 0.1717: Internal_Note `fit-results.md` notes (modelC/combined-ml/summary.md).
- Derived quantities W 1.64 ± 0.22 (1994: 1.63 ± 0.33), concurrence 0.82 ± 0.11 (0.82 ± 0.17), Bell 1.84 ± 0.19 (1.83 ± 0.28); 1994 B 0.049–0.052, off-diagonal 0.225–0.243: `fit-results.md`.
- "Factor 0.65": derived, 0.2200 / 0.3314 = 0.66 (W), 0.1372 / 0.2117 = 0.65 (C_kk). Toy spreads within 3 % of analytic: `fit-toys.md` (0.2243 vs 0.2200 etc.).

### Slide 22 — ML gain (component `GainBars.vue`)
- Concurrence σ per point, conventional / network: 1992 0.5831 / 0.2490; 1993 2.1161 / 0.7447, 0.6857 / 0.2794, 2.2045 / 0.7077; 1994 0.3416 / 0.1562; 1995 2.3617 / 0.7103, 0.7357 / 0.2904, 2.1891 / 0.6595; combined 0.2076 / 0.1034; geometric-mean coefficient ratio 0.429 → "five times more data" (derived (1/0.429)² = 5.4): Internal_Note `fit-ml-gain.md` and notes. Factor "2.2–3.3": derived from the ratios 0.30–0.46.

### Slide 23 — entanglement test
- Null construction, 20,000 toys, witness linearity, Bell null: Internal_Note `fit-hypothesis.md` notes. Production figure `fit/witness-null.png` (null σ 0.2344, SM-toy σ 0.2256, W 1.6407; made with the legacy model, Z_A 7.00), kept for the backup test slide. Main-text `fit/witness-public.svg` is a public-language redraw of those two Gaussians (`data/make_witness_public.py`, 2026-11-02).

### Slide 24 — expected significance
- Witness 7.0σ (combined; 6.96 Z_A, calibrated 7.00 ± 0.04, extrapolated beyond ≈3.7σ, 0/20,000 null toys), 4.6σ (1994); Bell 2.2σ (265/20,000), 1.45σ → shown 1.5σ (1,505/20,000); eigenvalue cross-check 6.8 / 4.3σ (notes): Internal_Note `fit-significance.md` and notes.
- Concurrence 0.82 ± 0.11 ⇒ 13 %: derived (0.1100/0.8204 = 13.4 %).
- "Once in 10¹²": one-sided Gaussian tail at 7.0σ = 1.3 × 10⁻¹² (derived, textbook).

### Slide 26 — outlook
- Open items (calorimeter / photon mismodelling; rates; C_kk reference; fixed 12.6 %; luminosity): Internal_Note `fit-caveats.md`, `datamc-residuals.md`, `status-next.md`. Plan items are proposals (`status-next.md` notes: "no order has been decided by the owner").
- Belle II / future e⁺e⁻ remark: general statement, no local result.

### Slide 27 — summary
- All numbers repeat slides 10, 15, 16, 21, 22, 24.

### Backup slides
- 30 (cuts): Internal_Note `cuts-1.md`, `cuts-2.md`.
- 31 (identification): `children-id.md` (identifier names replaced by plain words).
- 32 (composition figure): `ml/confusion-purity.svg`.
- 33 (data/MC): χ²/dof 101.8/42, 102.2/37, 18.7/11, 384/60: `datamc-inclusive-01.md`, `datamc-child-pirho.md`, `datamc-residuals.md`.
- 34 (residuals): table copied from `datamc-residuals.md` (purity range 17–43 % = matching fractions 0.173–0.43).
- 35 (ML per year): `ml-cls-allyears.md`, `ml-nu-allyears.md` (1994-only-model column dropped).
- 36 (channel agreement figure and 0.94 / 1.24 / 0.85): `ml-cls-allyears.md` notes.
- 37 (fit regions): `fit-inputs.md` (1994 composition table; 1–3 % cross-check).
- 38 (validation): `fit-validation.md`, `fit-toys.md` (correlations −0.35 combined, −0.22 1994; others ≤ 0.11).
- 39 (per point): `fit-ml-gain.md` table; "ratios 0.35–0.6 everywhere": read from `fit/per-point.png` lower panel (excluding the 1995·89 GeV clipped outlier).
- 40 (simulation table): `inputs-mc.md` (converted counts); "45 times the data": `fit-precision.md` notes (1994 fit-selection MC/data 45.0). PYTHIA 8 τ spin correlations: public PYTHIA 8 feature (Ilten, 2012), not a local artifact.
- 41 (points): `inputs-1992-1995.md` (yields, luminosities; sums 29,770 / 30,359 and 42,293 / 43,096). "42 % more events": derived, 42,293 / 29,770 = 1.42. Total 137.49 pb⁻¹ derived.

### Display precision
Luminosities 0.1 pb⁻¹ (main) / 0.01 pb⁻¹ (backup); coefficients and uncertainties 2 decimals (B uncertainties 3 decimals); fractions as percentages without decimals in prose, 3 decimals in backup tables; angles 2 decimals in degrees; significances 1 decimal; χ²/dof as "73.9 / 42".

## 2026-11-02 — opening-slide refinement (supersedes earlier opening copy)

- Cover: same author, venue and date; visual reference is `/Users/avencastmini/EveNet-Presentation/CCNU_Seminar/slides/cover.md`. No new measured quantities.
- Motivation: ATLAS top-pair entanglement observation, https://www.nature.com/articles/s41586-024-07824-z (2024); ATLAS Z-pair entanglement measurement in Higgs decays, https://journals.aps.org/prl/abstract/10.1103/y1nh-1b82 (11 September 2026). Publication metadata checked on 2 November 2026. H to WW remains an attributed group-status statement from the existing deck, not a verified published result.
- Tau phenomenology: Zhang et al., https://arxiv.org/abs/2504.01496, JHEP 04 (2026) 190; abstract explicitly identifies simulations, quantum tomography, entanglement and Bell nonlocality. The slide labels this simulated LHC work separately from the DELPHI measurement objective. Removed the overly categorical claim that every test coincides in one kinematic region.
- Spin matrix: algebraic expansion of the existing two-qubit Pauli parametrisation in Internal_Note/slides/fit-observables.md and this file's original spin-state entry. R_00=1, R_i0=B^-_i, R_0j=B^+_j, R_ij=C_ij; index order (0,n,r,k), sigma_0=identity. rho=1/4 sum_ab R_ab sigma_a tensor sigma_b. All six B and nine C entries are displayed, with no symmetry assumption. The displayed counts 6, 9 and 15 are derived from 3+3 and 3x3; the factor 1/4 fixes unit trace.

## 2026-11-02 — academic opening wording

The full cover title follows the owner's exact wording. Motivation claims retain the references in the preceding opening-slide refinement; no new results or numerical claims. Page 3 is a section outline of the subsequent analyser, spin-state and entanglement slides, not a result.

## 2026-11-02 — H to ZZ hypothesis-test qualification

ATLAS, Phys. Rev. Lett. 137 (2026) 111804, https://journals.aps.org/prl/abstract/10.1103/y1nh-1b82 ; preprint https://arxiv.org/abs/2603.26463 . Abstract checked on 2 November 2026: a complementary full-angular-distribution hypothesis test compares the separable and entangled Standard Model hypotheses, with assumptions about Standard Model decays. Slide 2 explicitly says “hypothesis test under SM assumptions”; no significance is added. The DELPHI statement is a proposed measurement, per the owner, not a completed result.

## 2026-11-02 — spin opener relation

The schematic decay angles → spin observables → rho relation summarises the following analyser and spin-state slides and their existing provenance; it adds no numerical result. “Spin observables” includes both single-particle polarisations and pair correlations. The background remains illustrative.

## 2026-11-02 — restored spin illustration

The Full SDM slide reuses the original SpinState.vue animated schematic preserved in the local QA snapshot before the opening-slide edits. It is illustrative, not an event or measurement. The expanded coefficient matrix and its relation to rho retain the existing Pauli-expansion provenance. No new numerical results.

## 2026-11-02 — explicit helicity-basis label

The helicity-basis label names the existing frame convention already documented in the original SpinState implementation and spin-state notes: k along tau flight, r in the production plane, n normal to the plane. No convention or fit input is changed.

## 2026-11-02 — page 6 QIS definitions (supersedes former results on this slide)

Source: Guo, Han, Low and Su, “Quantum Tomography of Fermion Pairs in e+e− Collisions: Longitudinal Beam Polarization Effects”, https://arxiv.org/html/2602.02719v1 , Section II, checked 2 November 2026.
- Concurrence: Eqs. 4–5. Lambda_i are descending square roots of eigenvalues of rho times spin-flipped rho (equivalently eigenvalues of the square-root auxiliary matrix); the screenshot incorrectly called them eigenvalues of rho. Range and separability criterion are definitions, not results.
- Magic: Eqs. 11–12. S_p abbreviates the sum of both single-spin coefficient p-th powers and all correlation coefficient p-th powers, for p=2,4. This gives exactly the quoted mixed-state SSRE extension. Pure-state interpretation is explicitly labelled; no universal mixed-state stabilizer-mixture witness is claimed.
- Bell: Eq. 8. B_max=2 sqrt(m1+m2), where m1,m2 are the largest eigenvalues of C^T C. The general full-matrix definition replaces the screenshot's restricted diagonal approximation. B_max<=2 is labelled “No CHSH violation”, not universal Bell locality.
- Every previous simulation number, significance or reference value has been removed from this introductory page. Prior provenance remains historical.

## 2026-11-02 — introductory entanglement witness

Page 6 now includes W=C_nn-C_rr+C_kk-1, with W>0 sufficient for entanglement and W<=0 inconclusive. Same convention as Internal_Note/slides/fit-hypothesis.md and fit-observables.md. Derived bound: for a separable mixture of Bloch-product states, a^T diag(1,-1,1)b <= |a||b| <=1, hence W<=0; convex mixtures preserve the bound. No assumption of vanishing polarisation or diagonal C is required for sufficiency. No result is added.

## 2026-11-02 — LEP-1 / DELPHI introduction (page 8)

Supersedes the previous luminosity/year-summary slide. Removed the uncertified total luminosity and per-year/scan-point details from this introduction.
- LEP-1 1989–1995 near the Z pole: CERN, https://cern-courier.web.cern.ch/a/experiments-finally-unveil-a-precise-portrait-of-the-z/ ; https://home.cern/science/accelerators/large-electron-positron-collider/ .
- DELPHI as one of four experiments; tracking/vertexing, particle identification, calorimetry: CERN, https://home.cern/science/experiments/delphi ; https://opendata.cern.ch/docs/about-delphi ; P. Aarnio et al. (DELPHI), NIM A303 (1991) 233–276, https://doi.org/10.1016/0168-9002(91)90793-P . Detailed detector overview: https://vincent-hedberg.web.cern.ch/delphi/delphi.html . These are general detector capabilities, not a statement of uniform performance across runs.
- 1992–1995 choice: owner instruction in this chat, sufficient luminosity and generally good detector conditions. Run-quality selection remains required.
- Public archive and software: DELPHI Collaboration, 15 August 2024, https://opendata.cern.ch/docs/delphi-data-release-2024 . The release includes raw/reconstructed collision data, simulated data and conditions database. Original simulation/reconstruction code covers 1992–2000; this range is explicitly software coverage. See also https://opendata.cern.ch/docs/delphi-guide-simulation for year-dependent detector setups. Public availability is not evidence of completed revalidation.
All public sources checked 2 November 2026.


### 2026-11-02 — DELPHI introduction: three questions
Page 8 reorganized into experiment, Z-pole tau-spin motivation, and feasibility. Keywords replace prose; public archive and 1992–1995 owner selection rationale retained. Sources remain the CERN LEP and DELPHI Open Data references above. Clean initial state and tau-decay spin analysis are qualitative motivation, not a sensitivity or validation claim.


### 2026-11-02 — PID and preservation links
Page 8 emphasizes PID together with tracking/calorimetry for identified visible tau daughters and momenta; no claim of detecting neutrinos or perfect reconstruction. Archive text links to CERN Open Data. Software text links to https://github.com/delphi-fullDST-edm4hep/delphi-sim-pipeline (README verified 2026-11-02), a modern-generator front end to legacy DELSIM simulation and DELANA reconstruction.


### 2026-11-02 — Event topology definitions
Page 9 retains three animated reveals, replaces paragraphs with four short definition blocks, and separates track/photon labels using leader lines. Hemisphere divider is perpendicular to thrust in the schematic. Visible candidates and the one-prong analysis scope are explicit. Removed the selected yield and detailed cuts from the displayed introduction; existing cutflow provenance remains applicable. Removed erroneous half-beam-energy wording.

## 2026-11-02 — reconstruction and fit rewrite (supersedes earlier slide order)

- Slides 11–17: Internal_Note/slides/ml-models.md, ml-split.md, ml-cls-allyears.md, ml-nu-allyears.md, children-id.md; Internal_Note/components/MLFlow.vue. Fixed half-split, separate models, 12 classes (10 unordered tau pairs, other tau, lepton background), 16 charge-ordered fit regions, angular diffusion targets, one sample with 50 steps. Parent artifacts/ml-all-years-v1-20261027/README.md checked for executed training and hold-half evaluation. No new training or physics jobs run for this deck edit.
- EveNet publication: T.-H. Hsu, B. Zhou, Q. Liu et al., “Foundation model for particle collision data analysis”, Nature Machine Intelligence (2026), published 29 October 2026; https://doi.org/10.1038/s42256-026-01322-9 . Publisher search result verified on 2026-11-02 (article direct fetch redirects to Nature login; full indexed publisher text includes citation and architecture). Pretrained point–edge transformer, downstream task-specific heads. DELPHI-specific configurations come from local records, not the publication.
- Conventional constraints: parent docs/PROJECT_GUIDE.md, analytical-neutrino reconstruction section, and tau_analysis/docs/NEUTRINO_RECONSTRUCTION.md. Single massless-neutrino hadronic hypothesis with no ISR recoil. No claim of exact two-body leptonic reconstruction.
- Slides 19–22: /Users/avencastmini/ZtautauLEP/tau_analysis/joint_fit/README.md, Model C, inspected live. Reweighting at truth, filling reconstructed bins, fixed other tau/non-tau terms, reference-linear templates; full covariance and GLS. 16 x 15 x 10 = 2400 nominal bins (derived); redundant modes removed. Model C is not the older PSD-constrained spin_fit baseline. Reference-density floor has zero affected reconstructed rows in the reported samples.
- Performance and precision numbers remain those of the previous SOURCES entries: classification .408 to .884; per-year .875–.887; pipi purity .173 to .664; branch .591 to .724; pi direction 1.55 to .88 degrees, rho 1.43 to .98. Main direction figure is 1994; numerical summary is all years. These cohorts are labelled.
- Model-C validation: Internal_Note/slides/fit-validation.md, fit-covariance.md and joint_fit README. 2000 same-template event-level pseudo-experiments; 20 injected states; pulls .972–1.026. This is statistical-model closure; finite template errors and independent detector validation are not established by it.
- Expected results: unchanged Model-C coefficients and 7.00/2.22 calibrated significances. Null statistic is q=chi2_null-chi2_free, with 20000 null toys and extrapolated entanglement tail. W<=0 is a witness-null superset of separable states; the Bell combination is a restricted test, not the general optimal-CHSH observable of slide 6. Witness illustration is from legacy model A and labelled. GainBars remains the legacy-fit comparison, not Model-C combined precision.
- Remaining modelling programme: Internal_Note/slides/fit-caveats.md. Reference Ckk=1.0307 and rho nonpositivity, fixed contributions, pooled energies, systematic uncertainties and uncertified luminosity remain unresolved inputs; next steps are proposals. No newly completed calibration or data-spin measurement is asserted.
- All assets retain their original local figure provenance. Internal_Note and parent analysis files are read-only for this work.

## 2026-11-02 — quantitative slides 11–14 restored

Supersedes the immediately preceding slide map. Pages 11–13 are deck-local refinements of Internal_Note/slides/cutflow-inclusive.md, cutflow-points.md, cutflow-children.md, inspected during this edit. All cumulative yields, per-year ratios, per-point luminosities/errors and channel composition fractions are copied without recalculation; original source comments are retained. The new local copies allow presentation-specific layout without editing Internal_Note. Page 13 true-pair fraction uses only simulated tau pairs in its denominator, rather than all backgrounds. The 29,821 assigned data events and 0.173 pion-pair matching fraction are unchanged.

Page 14 uses the same lead-p-over-pbeam-h0.svg and visible-mass.svg plots. Existing recorded chi2/dof values 73.9/42 and 129.1/49 are now displayed. Combined selected data 56,472, data/MC0.982, and tau fraction96.4% retain earlier provenance from rates-by-group.md and Internal_Note. No new calculation or physics validation. Simulation excludes Z_ee in the quoted rate tables; luminosity certification status remains explicit.


## 2026-11-02 — candidate definitions before the cutflow
New slide 10, immediately after the topology slide, reuses EventSketch with an identification variant. Four click-highlighted definitions: electron ELID>=3 with muon veto; muon numeric MUID>=7 with electron veto; charged-hadron pion with measured N_gamma=0; rho with N_gamma=1 or2 and 0.5<m(track+photons)<1.04GeV. Common hadron momentum threshold p/Ebeam>0.05 and nearby photon E>0.5GeV, DeltaR<0.3 are visible. The full hadron predicate remains in speaker notes and the detailed ID backup.
Sources inspected live: tau_analysis/analysis/exclusive_id.py (hadron_inputs, classify_leg and numeric_ge7/final_hadron call sites), analysis/photon_quality.py, docs/EXCLUSIVE_DECAY_HANDOFF_20261007.md. Unavailable/ambiguous inputs retain residual status; conflicting positive lepton tags are conflicts. No production definitions changed.
The animated cutflow now starts at slide11; quantitative selection pages move to12–15; all later slide numbers increase by one. Build and all four new slide states checked in Chromium at1470x827; formulas render without errors.


### 2026-11-02 — two-click candidate definitions
Slide10 now has two clicks: electron H1/muon H2, then pion H1/rho H2. Photons appear only in the second state. ELID/MUID are defined as DELPHI identification codes with the numerical thresholds and competing-tag veto. The hadronic state displays the common momentum/lepton requirements and both alternative routes: RPROCO2/3 plus HPC E/p<0.6 or certified absent association; alternatively complete HCAL mean occupied-layer energy>=3GeV. HPC/HCAL and photon cuts are defined below the schematic. Source predicates and validity requirements remain in the slide notes; source is the same inspected exclusive_id.py and handoff document. Supersedes the previous four-definition click design.


### 2026-11-02 — expand numerical identification semantics
Electron accepted codes explicitly mapped:3 loose,4 standard,5 tight (ParticleId.cpp PSCELD). Muon flags:1 very loose,2 loose,4 standard,8 tight,16 HCAL (ParticleId.cpp PSCMUD; archived literature-code-report.md and SKELANA manual p51). For valid five-bit values, numeric>=7 is exactly value7 or any value with bit8/16; this does not relabel the cut as one tightness level or replace it by mask28. Hadron RPROCO values2/3 expanded to standard/tight combined RICH and TPC dE/dx pion identification (converter README lines463–479). Existing E_HPC/p<0.6, certified absence route, HCAL mean>=3GeV and momentum/photon/mass cuts retained. These are decoded stored decisions, not newly derived elementary detector cut thresholds. Primary source linked on slide: https://opendata.cern.ch/record/80502/files/skelana.pdf . Full numeric reconstruction thresholds of ELECID/MUCAL2 are not asserted from ordinal labels. No analysis selection changes.


## 2026-11-02 — parallel reconstruction and EveNet architecture
Replaces previous slides16–18 with two pages. Conventional classification and analytical reconstruction are condensed into the parallel strategy; standalone conventional.md retained but removed from main sequence. Analytical constraints from tau_analysis/docs/PROJECT_GUIDE.md: hadronic single massless neutrino, beam-energy tau, back-to-back approximation, two branches. Parallel-flow reference: user-provided 20260801 ICHEP.pdf p5 and EveNet-Presentation/CCNU_Seminar/slides/delphi-transfer.md (itself adapted from ML4Jets). Old talk numerical results and targets not imported.
Current architecture numbers from Internal_Note/components/MLFlow.vue, inspected 2026-11-02:24 particles,12 per hemisphere,7 token slots,12 classes (10 unordered pairs + other tau + lepton background),84 conditions,1 sample with50 steps. Split from Internal_Note/slides/ml-split.md. PET geometry/attention description checked against CCNU_Seminar/slides/model-overview.md. Two independent fine-tunings explicitly drawn. NMI citation: T.-H. Hsu, B. Zhou, Q. Liu et al., Foundation model for particle collision data analysis, DOI10.1038/s42256-026-01322-9. No new performance claims added.


## 2026-11-02 — animated EveNet adaptation
Slide17 reuses the shell opening, PET attention, object encoder and animated paths from EveNet-Presentation/CCNU_Seminar/components/NJUAnimatedEveNet.vue, adapted into deck-local DelphiAnimatedEveNet.vue. Unused heads removed; diffusion bypasses object encoder, with84 conditions plus diffusion time into its decoder via FiLM. Shared useStepMotion provides visibility/reduced-motion lifecycle. Inputs and numerical settings retain Internal_Note/components/MLFlow.vue provenance above. Logo copied from reference public/evenet-logo-gold.svg. Full NMI citation and DOI restored at explicit owner request. Animated particles/edges are schematic, not measured attention or generated predictions.

## 2026-11-02 — classification comparison and working points
Slides18–19 now use original all-years hold-half plots from Internal_Note/public/figures/ml-all-years/cls/{02_confusion_purity.svg,05_efficiency_purity.svg}, copied byte-for-byte into this deck. The first includes classic, ML and their difference, column-normalised over the MC stack. Working-point curves distinguish independent score-threshold scans, ML argmax and classic regions; no final score threshold is claimed.
Numerical source: /Users/avencastmini/ZtautauLEP/artifacts/ml-all-years-v1-20261027/cls-eval-hold.md and cls-eval-hold-metrics.json (inspected2026-11-02). Same unseen MC cohort and inclusive_1p1p region. Accuracy .4079→.8841, difference47.622pp shown47.6pp. Representative efficiency/purity cut→ML: emu .688→.963/.921→.950; pipi .517→.746/.169→.664; pirho .233→.819/.328→.649; rhorho .104→.829/.547→.650. Percentages shown to0.1%; uncertainty-bearing values remain in source. Ratios from report central values: pipi purity .664/.169=3.93; rhorho efficiency .829/.104=7.97. All ten tabulated channels improve both central metrics at argmax. Year accuracy range .8752–.8869 from per-year reports / Internal_Note/slides/ml-cls-allyears.md.
Correction supersedes earlier slide19/SOURCES statements: pipi fourfold gain is purity, not efficiency; use stack purity16.9%, not tau-only matching17.3%. These are classification-performance gains, not fitted spin-sensitivity gains.


## 2026-11-02 — detector inputs, ambiguity and quantitative reconstruction
Replaces previous20–21 with20–22; following slides shift+1 (51total). Source files inspected directly: /Users/avencastmini/PycharmProjects/EveNet-Align/Ztautau/configs/converter-all-years.yaml (detector, globals, neutrino), converter/README.md, converter/evaluate_neutrino.py. Two tag slots encode the grouped detector inputs; FiLM gets84 condition channels including availability/year encoding, with uncompressed lead-track lifetime and ambiguity_D. Expanded lists include only configured fields, not excluded rawTPC dEdx, sigma_D0 or HPC longitudinal shapes. D=(ip_minus-ip_plus) dot (p_minus cross p_plus). The illustration is a schematic vector sum, not an observed event or posterior.
Numerical evidence: artifacts/ml-all-years-v1-20261027/nu-eval-hold.md and nu-eval-hold-metrics.json. Branch inclusive analytical/default .591, hybrid .713, ML .724, truth-selected .910; pipi .501/.758/.735/.981. Hybrid chooses analytical branch closest to ML directions. Angular median/q84 tables directly from angle.inclusive for e,mu,pi,rho and analytical/analytical+nu/nu, rounded2decimals. RMS from four_momentum.inclusive.{analytical,nu}.minus: px1.1224855015/.9865391760; py1.1231342002/.9832139005; pz1.2765652843/1.0708833580; E.4066867042/.8926603810 GeV. evaluate_neutrino.py residual_stats uses histogram-bin-centre weighted standard deviation about the mean; P4_EDGES [-6,6] with60bins. Caption states range and distinguishes from angular quantiles. Method-valid samples differ (e.g. pi legs336964 analytical vs596279 ML); not a matched-event causal comparison. Beam-energy reconstruction shown explicitly. Neutrino-system momentum is derived; no standalone neutrino RMS or individual leptonic-neutrino measurement fabricated. Historical1994 input comparison (Internal_Note/ml-nu-compare and artifacts/neutrino-ml-v5-20261021) does not support attributing gains to extra cone globals alone.

## 2026-11-02 — explain branch diagnostic and plot resolution metrics
Slide21 now defines truth-aided branch selection (minimum summed tau opening-angle distance to simulation truth, evaluate_neutrino.py457); explicitly unavailable in data. Corrected ambiguity_D formula to use the UNIT track-plane normal, matching converter/features.py395–425; earlier unnormalised formula has same sign but different magnitude. Impact vectors are primary vertex to closest point on each track line; finite tau flight supplies signed displacement information beyond two-body momentum constraints. No claim that IP gives perfect identification.
Slide22 resolution-explained.svg regenerated by data/plot_neutrino_resolution.py from the exact archived nu-eval-hold-metrics.json used in previous revision: angle.inclusive.{analytical,nu}.{e,mu,pi,rho}.{median_deg,q84_deg}; four_momentum.inclusive.{analytical,nu}.minus.{px,py,pz,E}.rms. Display2decimals. Three panels: median,84% containment,RMS about mean. Method-valid subsets and histogram range remain explicit. This is a summary-metric plot, not an invented residual distribution. Original all-years06_direction.svg has a hard-coded1994 label, so not used for this replacement. Energy degradation retained. Plot generated with existing EveNet-Align Python/Matplotlib environment.


## 2026-11-02 — native web resolution charts
Slide22 now renders paired-dot HTML/Vue/SVG charts through NeutrinoResolutionCharts.vue, with exact archived metrics extracted into data/neutrino-resolution.json. No Plotly dependency or remote script introduced. Same values and definitions as preceding source section; two-decimal labels, hover full precision. Earlier generated SVG retained as unused artifact. Removed truth-aided comparator from slide21 at owner request; hybrid renamed Analytical solution closest to ML, preserving its method rather than implying an event region. Footnotes removed from21–22, detailed provenance remains here and in speaker notes.


## 2026-11-02 — animated ambiguity explanation
Page21 replaced with deck-local DecayAmbiguity.vue, three clicks/four states. Exact schematic cone intersections calculated on unit sphere, with both constraints expressed for same tau (second visible axis reflected). Equal-weight squared-loss conditional mean illustrated separately from diffusion, which can model both modes. Finite flight side-view shows track positions with identical momentum direction but reflected normal displacement. Relation b_perp=b.n=L.n holds because track direction lies in mirror plane. Full impact vector need not reverse. Unit-normal D matches converter/features.py. Removed analytical-closest-to-ML and truth-aided comparators. Final table retains original full-model held-out accuracy, not an IP-only ablation. User's absolute only-IP, exact average-for-diffusion,20micron resolution and year-causal claims not adopted without evidence.
Public sources checked: Physics of tau leptons, CERN-PPE/95-147 https://cds.cern.ch/record/290480/files/ppe-95-147.pdf (twofold hadronic reconstruction without radiative corrections); DELPHI precise tau lifetime measurement https://arxiv.org/abs/hep-ex/0410010 ; primary DELPHI lifetime study https://pure.uva.nl/ws/files/2149575/1869_20685y.pdf (impact parameter difference and miss distance). These support geometry/lifetime context, not identity between this network and a historical likelihood method. No detector-resolution numbers or causal detector-year explanation added.

## 2026-11-02 — forward-folded fit section, superseding earlier main-fit slides

Scope: main slides 24–32, with the summary/outlook updated for consistency. All fit results are **Asimov/reference simulation, expected data-statistical only**. No new fit, pseudo-experiment generation, physical projection, MC-statistical uncertainty evaluation, or systematic fit was performed. Earlier template and witness illustrations and per-year gain comparison are no longer used in the main fit section.

Primary artifact directory: `/Users/avencastmini/ZtautauLEP/artifacts/joint-fit-20261031/modelC/combined-ml/`, archived 2026-10-31, inspected 2026-11-02. Implementation: `tau_analysis/joint_fit/model_c.py`, `spin_reweight.py`, `legacy_bridge.py`, and README. Cross-check: Internal_Note `fit-model`, `fit-results`, `fit-precision`, `fit-toys`, `fit-significance`.

| Content | Exact provenance / derivation |
|---|---|
| Forward-folded response and sample combination | `model_c.py` module documentation; `mu=mu0+T delta`. Floating true e/mu/pi/rho pairs include cross-feed; other tau decays and non-tau backgrounds are fixed. Floor 0.02 affects zero reconstructed events in this sample; hence displayed ratio is exact for these events. Pooled sample uses one luminosity-weighted reference. |
| Longitudinal template plot | `covariance_modelC.npz`: `mu0[14,0,:]`, `T[14,14,0,:]`, offsets -0.3,0,+0.3 (illustrative choices, not fitted results). Legacy observable order is coefficient order, Ckk last. Points are Asimov with sqrt(expected yield) errors. Replaces old template illustration. |
| 16 regional yields, total 32,335.8 | `mu0[0].sum(axis=-1)`; total 32335.84248185319. One observable counts each event once. Table rounded to nearest event, total to one decimal. Region string first decay is tau+ (A); second tau- (B), as in `spin_reweight.py`. |
| 15 observables, 10 bins, 2400/2176 bins | `covariance_modelC.npz` array shapes / keep_local; 16 x 15 x 10; 14 exact redundant modes per region. `V=sum w ssT` is expected event-Poisson data covariance, not MC sumw2. |
| Full SDM coefficient table and error bars | NPZ `reference`, `sqrt(diag(C))`, `bc_names`. B_A labelled B+, B_B labelled B- following `spin_reweight.py`. 3 decimal display for all coefficients to retain small off-diagonal values. This supersedes earlier two-decimal convention for this table only. Ckk1.03068695 is unconstrained, not a physical-state data measurement. |
| Regional variance fractions | **Derived** from saved NPZ: X_r = flattened T at region_flat_index/keep_local; F_r = X_r.T solve(V_r,X_r); Sigma_r=C F_r C. Fractions diagonal(Sigma_r)/diagonal(C); W uses g=(0,...,1,0,0,0,-1,0,0,0,1). Independent regions sum exactly to archived F and C within numerical precision (asserted). Charge-conjugate pairs grouped only for display. This is the variance budget of the combined estimator, not standalone region uncertainties or a systematic decomposition. |
| Pull plots | `toys_modelC_sm.npz` C_delta / sqrt(diag(C)), 2000 archived toys. Widths use ddof=1: 0.971650–1.026012; approximate width error 1/sqrt(2*(2000-1))=0.0158. |
| W, Bell, magic distributions | Same archived C_delta + reference. W/Bell also directly from C_W/C_Bell; magic = -log2[(1+sum c^4)/(1+sum c^2)] matching model_c.magic. Histograms show reference toys, not null distributions. |
| Toy intervals and propagated errors | `results_modelC.json` derived.C: W nominal1.6407375, linear sigma0.2199502, toy std0.2242665; Bell1.8442099,0.1888773,0.1901539; magic0.1962194,0.1814496,0.1895841. Medians/16/84/2.5/97.5 percentiles copied from same dictionary, three-decimal display. Unconstrained magic can be negative; no physical-state or magic-null inference claimed. |
| Null tests | `summary.md` / `results_modelC.json` tests: 20000 toys per boundary null; W 0 exceedances, **calibrated extrapolation** 7.002 +-0.037 sigma, displayed7.00; Bell265/20000=1.325%, count/calibration about2.22sigma. W<=0 includes separable states but is not equivalent to separability. Bell fixed-axis combination is not optimized CHSH. No magic null calibration exists in this artifact. |

Reproducible lightweight rendering: `data/build_fit_section.py`, derived values `data/fit-section.json`, five `public/figures/fit/modelc-*.svg`/`sdm-errors.svg`/`region-budget.svg` figures. Uses existing local NumPy/Matplotlib environment; no new dependencies. Generator reads original artifacts only, and does not alter them.

Literature (verified 2026-11-02):
- CMS Collaboration, *Phys. Rev. D* **110** (2024) 112016, [arXiv:2409.11067](https://arxiv.org/abs/2409.11067). Section 8, detector-level templates obtained from generator reweighting, simultaneous coefficient extraction and category combination. Supports the methodological analogy; CMS likelihood is not asserted to be this GLS implementation.
- DELPHI Collaboration, P. Abreu et al., *Phys. Lett. B* **404** (1997) 194–206, [doi:10.1016/S0370-2693(97)00586-8](https://doi.org/10.1016/S0370-2693(97)00586-8). LEP transverse-spin precedent only; no claim that its estimator equals the present forward-folding implementation.

### Slide 26 covariance clarification (2026-11-02)

Replaced GLS/Fisher equations with the entry definition Cov(n_ra,n_rb) and an actual normalised covariance image. Source: same combined-ml `covariance_modelC.npz`, `V0_blocks[0]`, region pipi, full150x150 before redundant-bin removal. Display divided by sqrt(Vaa Vbb), range0–1; fit retains unnormalised covariance. Each10x10block is a pair of angular histograms. Gold boundary separates six single-angle from nine product projections. Figure generator: `data/build_covariance_figure.py`. No new numerical physics results. Corrected “independent bins” to “non-redundant bins”; retained bins remain correlated.

### Interpretation and merged QIS results (2026-11-02)

Slide28:46.5% is the rounded pi-pi entry for W in `data/fit-section.json`, calculated analytically as previously documented. “Fluctuate only one region” defines the same fixed-estimator variance decomposition; no new regional toys were generated. Larger variance share describes statistical influence, not a standalone fit uncertainty or removal-induced precision loss. Slide29 conclusion uses archived pull means and widths, with fixed templates and reference-model scope explicitly stated. Slides31–32 merged without numerical changes; old31 null-test quantities and old32 propagation results now appear together in31. Owner-requested callouts removed from26/27; underlying fit and provenance unchanged.

### Closing slide32 (2026-11-02 owner revision)

Plan/status statements (track-momentum/HPC-energy calibration per year/CME, ongoing pion-related ML optimisation, final-inference decision, order1%systematics working estimate) supplied in this user turn. The1% estimate is explicitly provisional, not a calculated uncertainty or proof of subdominance. Full-SDM priority is presented as the programme goal, not a completed first measurement. Expected entanglement7.0sigma/Bell2.2sigma and magic0.196+-0.181 repeat archived Model C combined-ml values above. LHC-pretrained EveNet with task fine-tuning follows the verified architecture/source on17; classification40.8%→88.4% repeats held-out cut-based versus ML accuracy40.79%→88.41%, not an ablation of pretraining. Further QIS/spin/CP observables are the intended physics scope of SDM extraction.

### Slide15 six-panel kinematics (2026-11-02)

Expanded the original leading-track momentum and visible mass with four complementary distributions from the same inclusive selection. All six original SVGs copied without numerical/graphical modification from `Internal_Note/public/figures/datamc-1992-1995/inclusive/inclusive_1p1p-selected-<variable>-rate_lin.svg`. Variables: `leadtrack_hemi0_p_over_pbeam`, `leadtrack_hemi0_costheta`, `exclusive_hemi0_nearby_photon_energy`, `visible_tautau_mass`, `erad_over_ebeam`, `prad_over_pbeam`. Internal_Note slides `datamc-inclusive-01`, `03`, `04` and figure MANIFEST record selection60333695, plotting60340876, tau_analysis67bffe7, all-years-rq-20261026. Same1992–1995 inclusive sample, luminosity-normalised signed MC, original ratio panels retained. Leading-track/photon panels use source hemisphere0. Photon spectrum is per photon; correlated entries, no chi-square annotation added. Existing diagnostic caveats (uncertified run-table luminosities, calibration unresolved) retained in note/source history. No new data processing or normalization.
