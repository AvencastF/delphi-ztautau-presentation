---
class: st pres tk
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Transfer learning

<div class="st-sub">Pretrained on LHC collisions, then fine-tuned on LEP</div>

<div class="tk-fig" style="height:372px"><ZoomablePlot src="/figures/ml/evenet-scaling.png" alt="Classification error versus LEP training-set size, for a model trained from scratch and for the LHC-pretrained model" /></div>
<div class="tk-cap">Lower is better. Blue: trained from scratch on LEP. Red: the same task after LHC pretraining. The pretrained model needs less LEP data to reach a low error.</div>

<!--
Figure supplied by the user on 2026-11-02 as ~/Downloads/ML4Jets.png (4968x2972), copied unmodified to public/figures/ml/evenet-scaling.png, sha256 60f88c08aff1390f. Replaces the earlier 1024x612 screenshot. Axis title on the figure: "Scaling law"; y = 1 - tau top-1 accuracy; x = training set size N. Legend: Scratch (blue) and FM (red). Fit annotations printed on the figure, not recomputed here: scratch err = 2.53 N^{-0.114} ± 0.03; fm err = 0.80 N^{-0.031} ± 0.04. User statement with the figure: FM is EveNet pretrained on LHC and fine-tuned on LEP; Scratch is trained on LEP only. That mapping is not written on the axes. One red point near 10^5 lies below the fit band; left as drawn.
-->
