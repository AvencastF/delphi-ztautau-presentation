---
class: st pres
clicks: 3
---

<script setup>
import MLFlow from '../components/MLFlow.vue'
</script>

# The two models: shared pretrained body, two heads

<div class="st-sub">Click through. Both start from the same pretrained EveNet checkpoint; the particle token is unchanged.</div>

<MLFlow :step="$clicks" />

<div class="st-source">Source: converter and training configurations in the EveNet-Align Ztautau code</div>

<!--
EveNet-Align/Ztautau/configs/converter-1994.yaml (classes, neutrino target leading_track delta_theta/delta_phi), train-neutrino.yaml (pretrain_model_load_path /global/cfs/cdirs/m5019/avencast/Checkpoints/checkpoints.20M.ablation.4.newcls/epoch=29_train=2.4809_val=2.5040.ckpt; FiLM; binning [101,-0.25,0.25]). Owner measured ~10 % better classification with pretraining (2026-10-16), hence the 7-slot token [E, pT, eta, phi, tag0, tag1, q] and PET body stay unchanged.
-->
