# Aggregated from the frozen run all-event-detector-1994-20261012 (cutflows/cutflow.csv, exclusive_confusion.csv)

Rows with sample "1994/Total MC (Z_ee excluded)" are taken verbatim from the CSV; tau = sum of all Z_tautau_* ordered-label samples.

| region | cut | data | total MC excl. Z_ee (signed sumw) | of which Z_tautau | data/MC |
|---|---|---:|---:|---:|---:|
| inclusive_1p1p | input | 828850 | 2698666.249335 | 67799.911 | 0.3071 |
| inclusive_1p1p | hemispheres | 334830 | 1732900.217561 | 58116.656 | 0.1932 |
| inclusive_1p1p | acceptance | 322437 | 1673443.487097 | 57292.059 | 0.1927 |
| inclusive_1p1p | multiplicity | 266778 | 340365.020668 | 55708.327 | 0.7838 |
| inclusive_1p1p | isolation | 199915 | 194466.083756 | 53671.906 | 1.0280 |
| inclusive_1p1p | z_origin | 193935 | 190401.269830 | 53069.396 | 1.0186 |
| inclusive_1p1p | d_origin | 188524 | 185417.412265 | 52153.301 | 1.0168 |
| inclusive_1p1p | one_close | 187655 | 185042.790106 | 52104.717 | 1.0141 |
| inclusive_1p1p | relative_z | 187008 | 184589.375092 | 51961.032 | 1.0131 |
| inclusive_1p1p | energy | 184876 | 182368.007559 | 51635.841 | 1.0138 |
| inclusive_1p1p | transverse | 173851 | 169339.151477 | 51227.178 | 1.0266 |
| inclusive_1p1p | nn_one_prong | 123843 | 120069.367913 | 38756.192 | 1.0314 |
| inclusive_1p1p | nn_acol | 61620 | 59078.423330 | 38296.899 | 1.0430 |
| inclusive_1p1p | nn_boundary_no_pe | 60141 | 57740.096872 | 38179.831 | 1.0416 |
| inclusive_1p1p | nn_pe_keep_unknown | 48707 | 46785.405998 | 37640.958 | 1.0411 |
| inclusive_1p1p | nn_is_1p1p | 33739 | 32862.683621 | 25735.772 | 1.0267 |
| inclusive_1p1p | exclusive_erad | 32531 | 31795.685713 | 25613.611 | 1.0231 |
| inclusive_1p1p | exclusive_prad | 26631 | 25780.069403 | 24914.933 | 1.0330 |
| inclusive_1p1p | neutral_hemisphere_limit | 23073 | 23198.931168 | 22412.038 | 0.9946 |
| inclusive_1p1p_ee | input | 23073 | 23198.931168 | 22412.038 | 0.9946 |
| inclusive_1p1p_ee | id_ee | 882 | 896.952225 | 746.395 | 0.9833 |
| inclusive_1p1p_emu | input | 23073 | 23198.931168 | 22412.038 | 0.9946 |
| inclusive_1p1p_emu | id_emu | 1638 | 1717.109015 | 1715.943 | 0.9539 |
| inclusive_1p1p_epi | input | 23073 | 23198.931168 | 22412.038 | 0.9946 |
| inclusive_1p1p_epi | id_epi | 1694 | 1751.834696 | 1671.162 | 0.9670 |
| inclusive_1p1p_erho | input | 23073 | 23198.931168 | 22412.038 | 0.9946 |
| inclusive_1p1p_erho | id_erho | 1076 | 1082.589670 | 1077.990 | 0.9939 |
| inclusive_1p1p_mumu | input | 23073 | 23198.931168 | 22412.038 | 0.9946 |
| inclusive_1p1p_mumu | id_mumu | 1160 | 1067.873977 | 952.828 | 1.0863 |
| inclusive_1p1p_mupi | input | 23073 | 23198.931168 | 22412.038 | 0.9946 |
| inclusive_1p1p_mupi | id_mupi | 1912 | 1938.235467 | 1914.638 | 0.9865 |
| inclusive_1p1p_murho | input | 23073 | 23198.931168 | 22412.038 | 0.9946 |
| inclusive_1p1p_murho | id_murho | 1242 | 1210.722115 | 1209.668 | 1.0258 |
| inclusive_1p1p_pipi | input | 23073 | 23198.931168 | 22412.038 | 0.9946 |
| inclusive_1p1p_pipi | id_pipi | 952 | 947.373915 | 938.464 | 1.0049 |
| inclusive_1p1p_pirho | input | 23073 | 23198.931168 | 22412.038 | 0.9946 |
| inclusive_1p1p_pirho | id_pirho | 1216 | 1189.673045 | 1188.855 | 1.0221 |
| inclusive_1p1p_rhorho | input | 23073 | 23198.931168 | 22412.038 | 0.9946 |
| inclusive_1p1p_rhorho | id_rhorho | 389 | 378.267116 | 378.267 | 1.0284 |

## Confusion (truth rows x reco columns, signed MC sumw, tau MC only)

| truth \ reco | ee | emu | epi | erho | mumu | mupi | murho | pipi | pirho | rhorho | conflict | residual |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ee | 677.58 | 0.02 | 51.32 | 0.91 | 0.00 | 0.00 | 0.00 | 1.98 | 0.18 | 0.00 | 0.02 | 322.57 |
| emu | 0.11 | 1582.84 | 90.65 | 0.40 | 0.00 | 62.24 | 1.36 | 3.62 | 0.02 | 0.00 | 0.62 | 496.27 |
| epi | 12.87 | 9.41 | 728.05 | 9.61 | 0.00 | 0.62 | 0.00 | 31.00 | 1.09 | 0.00 | 0.02 | 470.77 |
| erho | 34.02 | 25.06 | 540.43 | 756.89 | 0.00 | 1.25 | 0.00 | 26.10 | 27.42 | 0.47 | 0.16 | 1551.94 |
| mumu | 0.00 | 0.33 | 0.00 | 0.00 | 896.64 | 107.22 | 0.49 | 3.05 | 0.04 | 0.00 | 0.62 | 164.34 |
| mupi | 0.00 | 15.32 | 0.89 | 0.00 | 12.47 | 840.45 | 11.81 | 51.65 | 0.78 | 0.00 | 0.36 | 389.12 |
| murho | 0.02 | 44.36 | 2.67 | 0.04 | 29.95 | 632.39 | 869.71 | 36.80 | 51.54 | 0.20 | 1.02 | 1440.74 |
| pipi | 0.00 | 0.11 | 6.20 | 0.13 | 0.09 | 5.16 | 0.13 | 171.19 | 4.31 | 0.02 | 0.04 | 144.46 |
| pirho | 0.18 | 0.62 | 24.55 | 7.65 | 0.24 | 17.21 | 5.54 | 286.12 | 402.50 | 4.96 | 0.18 | 955.16 |
| rhorho | 0.36 | 0.40 | 14.23 | 21.41 | 0.22 | 9.43 | 13.72 | 113.22 | 293.71 | 208.59 | 0.20 | 1295.85 |
| other_1p1p | 20.81 | 36.78 | 207.97 | 279.32 | 13.05 | 233.94 | 305.38 | 208.52 | 402.97 | 163.34 | 0.93 | 3337.52 |
| other_tau_tau | 0.44 | 0.69 | 4.20 | 1.62 | 0.16 | 4.74 | 1.53 | 5.20 | 4.29 | 0.69 | 0.04 | 44.87 |
| unknown | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

| reco child | tau-MC reco marginal sumw | matching truth sumw | matching fraction |
|---|---:|---:|---:|
| ee | 746.395 | 677.577 | 0.908 |
| emu | 1715.943 | 1582.843 | 0.922 |
| epi | 1671.162 | 728.051 | 0.436 |
| erho | 1077.990 | 756.890 | 0.702 |
| mumu | 952.828 | 896.639 | 0.941 |
| mupi | 1914.638 | 840.450 | 0.439 |
| murho | 1209.668 | 869.712 | 0.719 |
| pipi | 938.464 | 171.190 | 0.182 |
| pirho | 1188.855 | 402.504 | 0.339 |
| rhorho | 378.267 | 208.589 | 0.551 |
| conflict | 4.225 | 0.000 | 0.000 |
| residual | 10613.603 | 0.000 | 0.000 |
