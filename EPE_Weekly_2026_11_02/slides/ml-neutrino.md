---
class: st pres tk tk-academic
---

# Detector information beyond the two tag slots

<div class="st-sub">Measured detector quantities + availability masks · learned embedding into the pretrained token</div>
<table class="nu-input-table"><thead><tr><th>Information</th><th>Inputs to the detector embedding</th><th>Reconstruction information</th></tr></thead><tbody>
<tr><td>Particle identification</td><td>Electron ID; muon flags, hits and refit <LaTeX formula="\chi^2" /><br/>Combined hadron tags; calibrated <LaTeX formula="\mathrm{d}E/\mathrm{d}x" />; RICH angles and photon counts</td><td>Decay mode and particle species</td></tr>
<tr><td>Tracking and lifetime</td><td><LaTeX formula="d_0^{\rm PV},z_0^{\rm PV},d_0^{\rm BS},\sigma(z_0)" /><br/>Track fit quality, length, detector mask; transverse lifetime probability</td><td>Displacement and decay geometry</td></tr>
<tr><td>Calorimetry</td><td>Shower energies, positions and multiplicities<br/>HCAL layer energies; neutral shower–track separation</td><td>Neutral energy and visible momentum</td></tr>
<tr><td>Detector availability</td><td>Per-value validity; association status; unpacked detector flags</td><td>Missing measurement distinguished from zero</td></tr>
</tbody></table>
<div class="nu-input-paths"><section><h2>Particle representation</h2><p>Detector embedding <LaTeX formula="\longrightarrow (t_0,t_1)" /></p><div><LaTeX formula="[E,p_T,\eta,\phi,t_0,t_1,q]" /> <span><LaTeX formula="\longrightarrow" /> PET</span></div></section><section><h2>Direct conditioning: 84 channels</h2><p>Leading-track lifetime + ambiguity discriminant<br/>Missing momentum · cone quantities · <LaTeX formula="\sqrt{s}" /> · year</p><div><LaTeX formula="\longrightarrow" /> FiLM modulation of the diffusion head</div></section></div>

<!--
Source: PycharmProjects/EveNet-Align/Ztautau/configs/converter-all-years.yaml detector/globals and converter/README.md. This expands actual input families without listing excluded fields: raw MTPC dEdx, sigma_D0, VD hit counts and HPC longitudinal profile are not claimed. Two slots are learned detector embeddings, not two raw ID codes. Availability/status retained. Direct FiLM lifetime channels avoid compressing all displacement information through these slots. 84 includes values, availability and year encoding; not84 independent physical observables. No feature-level causal gain asserted. 1994 v2-v5 comparison found no measurable gain from added cone globals alone.
-->
