# Figure manifest — EPE_Weekly_2026_11_02

Every file under `public/figures/`, its origin, and the sha256 of the copy (first 16 hex digits). All figures were copied unmodified on 2026-11-02 from the status deck `Internal_Note/public/figures/`, whose own `MANIFEST.md` records the NERSC / artifact origin of each file (the "origin" column below repeats that entry). Labels baked into the figures are preserved. The two `fit-explainer` SVGs in the status deck were regenerated after its manifest entry was written (its recorded hashes differ); the hashes below are those of the files copied here.

| deck path | copied from (Internal_Note/public/figures/…) | upstream origin (per Internal_Note MANIFEST) | sha256 |
|---|---|---|---|
| `datamc/lead-p-over-pbeam-h0.svg` | `datamc-1992-1995/inclusive/inclusive_1p1p-selected-leadtrack_hemi0_p_over_pbeam-rate_lin.svg` | NERSC `analysis-runs/1992_1993_1994_1995/all-years-rq-20261026/plots/all-years-baseline/` (selection job 60333695, plots job 60340876) | `f24ec06ef1c6b55f` |
| `datamc/lead-p-over-pbeam-h1.svg` | `datamc-1992-1995/inclusive/inclusive_1p1p-selected-leadtrack_hemi1_p_over_pbeam-rate_lin.svg` | same | `bcda121323f76183` |
| `datamc/lead-costheta-h0.svg` | `datamc-1992-1995/inclusive/inclusive_1p1p-selected-leadtrack_hemi0_costheta-rate_lin.svg` | same | `69933fade4e4838c` |
| `datamc/visible-mass.svg` | `datamc-1992-1995/inclusive/inclusive_1p1p-selected-visible_tautau_mass-rate_lin.svg` | same | `bdad7b909df8da09` |
| `datamc/hcal-mean-h0.svg` | `datamc-1992-1995/inclusive/inclusive_1p1p-selected-exclusive_hemi0_hcal_mean-rate_lin.svg` | same | `6e88c2ce6bcbd803` |
| `datamc/pirho-rho-mass.svg` | `datamc-1992-1995/children-pirho/inclusive_1p1p_pirho-selected-candidate1_rho_mass-rate_lin.svg` | same run, `all-years-children-inclusive_1p1p_pirho/` | `f16f290445afd2d8` |
| `ml/efficiency-purity.svg` | `ml-all-years/cls/05_efficiency_purity.svg` | NERSC `…/all-years-rq-20261026/skim-cls-nu-cls-eval/05_efficiency_purity.svg` (job 60363881) | `a90427f96bfb413b` |
| `ml/confusion-purity.svg` | `ml-all-years/cls/02_confusion_purity.svg` | same, `svg/02_confusion/purity.svg` | `83839fd51a40dca2` |
| `ml/channel-agreement.svg` | `ml-all-years/cls/06_agreement.svg` | same, `06_agreement.svg` | `2395fabbf92c7109` |
| `ml/direction.svg` | `ml-all-years/year-1994/06_direction.svg` | NERSC `…/all-years-rq-20261026/skim-cls-nu-nu-eval-year-1994/06_direction.svg` (job 60366303) | `40dd30eb99535168` |
| `ml/evenet-scaling.png` | user-supplied 2026-11-02 | `~/Downloads/ML4Jets.png` (4968×2972), copied unmodified; replaces the 1024×612 screenshot | `60f88c08aff1390f` |
| `fit/template-ckk.svg` | `fit-explainer/template-ckk.svg` | made by `Internal_Note/data/make_fit_explainer_figs.py` from `artifacts/joint-fit-20261031/modelB/combined-ml/base_templates.npz` | `b0bdfb2c0bb7c0b0` |
| `fit/pull-widths.svg` | `fit-explainer/pull-widths.svg` | same script, from `modelB/combined-ml/summary.md` and `modelC/combined-ml/summary.md` | `e7fae1ba5ea84703` |
| `fit/witness-null.png` | `fit/step2-W-null.png` | `artifacts/joint-fit-20261031/step2/combined-ml/W_null_distribution.png` | `503c842b973f156a` |
| `fit/witness-public.svg` | redrawn | public labels from the reported toy widths (null σ 0.2344, SM σ 0.2256, W 1.6407); `EPE_Weekly_2026_11_02/data/make_witness_public.py` | generated 2026-11-02 |
| `fit/pulls.png` | `fit/modelC-pulls.png` | `artifacts/joint-fit-20261031/modelC/combined-ml/pulls_modelC.png` | `67890bfcdae22506` |
| `fit/correlation.png` | `fit/modelC-correlation.png` | `artifacts/joint-fit-20261031/modelC/combined-ml/correlation_modelC.png` | `b270a34128bc2999` |
| `fit/per-point.png` | `fit/allyears-per-point.png` | `artifacts/legacy-fit-ml-allyears-20261030/runs-fits/comparison.png` | `e3b00a05f0bfcb50` |

Other public assets: `nersc-logo.svg`, `perlmutter-logo.svg` (copied from `Internal_Note/public/`, used on the closing slide).
