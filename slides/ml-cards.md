---
class: st pres
---

# Classifier versus neutrino model

<div class="st-cols st-cols-2">
<div class="kv ml"><h3><span class="tag ml">ML</span> Decay-mode classifier · v1</h3><dl>
<dt>Target</dt><dd>12 classes: 10 τ channels + other τ + lepton pairs</dd>
<dt>Inputs</dt><dd>first conversion, 229 particle channels, 18 globals</dd>
<dt>Weights</dt><dd>unit event weights, class loss cap 0.4</dd>
<dt>Training</dt><dd>2026-10-16; Bhabha replaces Z_ee</dd>
<dt>Checkpoint</dt><dd>epoch 29, raw weights <span class="id">epoch=29_train=0.1037_val=0.4805</span></dd>
</dl></div>
<div class="kv ml"><h3><span class="tag ml">ML</span> Neutrino-direction model · v5</h3><dl>
<dt>Target</dt><dd>(δθ, δφ) of each τ to its leading track, detector frame</dd>
<dt>Inputs</dt><dd>fifth conversion; same tokens</dd>
<dt>Conditioning</dt><dd>74 event quantities via FiLM</dd>
<dt>Training</dt><dd>2026-10-21, 4 GPUs, 100 epochs, 1 h 57 min</dd>
<dt>Checkpoint</dt><dd>last epoch, EMA weights; 1 sample × 50 steps</dd>
</dl></div>
</div>

<div style="margin-top:10px;font-size:12.5px;color:var(--fg-1)"><b style="color:var(--fg-0)">Input tags:</b>
<span class="tag data">E, p_T, η, φ, charge</span> <span class="tag data">mass, track length</span> <span class="tag data">electron tag</span> <span class="tag data">muon word</span> <span class="tag data">hadron tags</span> <span class="tag data">calibrated dE/dx</span> <span class="tag data">lifetime probability</span> <span class="tag data">calorimeter sums</span> <span class="tag data">RICH quantities</span> <span class="tag sim">neutral filter: &lt;1 GeV needs EM shower</span> <span class="tag sim">event bound 137 GeV</span></div>

<div class="st-source">Source: converter configuration, version-5 archive README and the 1994 runbook (ML stage)</div>

<!--
converter-1994.yaml: max_particles 24 (12 per hemisphere, leading tracks kept), slots 0-3 kinematics, 4-5 detector embedding, 6 charge; detector: MAIN mass, TrackLength, DetectorMask bits; PID sDST_ELID_ElectronID, sDST_MUID_MuonID, sDST_RPROCO_CombinedTags, sDST_BBDXGET_Dedx (response, error, quality), AABTAG R-phi probability; neutral_filter require_emnc_below_gev 1.0; event_bounds evis/pt/visible_tautau_mass 137 GeV (174 of 1,019,014 training events removed); class_balance_max 0.4; processes Z_mumu, Bhabha, yy_ll -> Zll; Z_ee not trained; Z_qq 0 rows. Neutrino v5: 74 condition channels, job 60075238 train 0.2449 / val 0.2284; prediction job 60079489 appends nu_delta_theta/phi_{plus,minus}, nu_label, nu_status, nu_split. Classifier checkpoint ml-runs/evenet-inputs-1994/runs/classification/checkpoints/epoch=29_train=0.1037_val=0.4805.ckpt. First conversion 229 particle channels after the dE/dx fix; v5 smoke 255 x / 74 condition channels.
-->
