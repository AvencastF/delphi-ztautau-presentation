---
class: st pres tk tk-datamc-evidence kinematics-six
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Selected-event kinematics

<div class="st-sub">1992–1995 · inclusive selection · luminosity-normalised simulation · lower panels: data / MC</div>

<div class="kinematics-grid">
<section><div class="kin-caption">Leading track: <LaTeX formula="p/p_{\rm beam}" /></div><div class="tk-fig"><ZoomablePlot src="/figures/datamc/lead-p-over-pbeam-h0.svg" alt="leadtrack_hemi0_p_over_pbeam: inclusive 1992–1995 data and luminosity-normalised simulation with ratio panel" /></div></section>
<section><div class="kin-caption">Leading track: <LaTeX formula="\cos\theta" /></div><div class="tk-fig"><ZoomablePlot src="/figures/datamc/lead-costheta-h0.svg" alt="leadtrack_hemi0_costheta: inclusive 1992–1995 data and luminosity-normalised simulation with ratio panel" /></div></section>
<section><div class="kin-caption">Nearby photon: <LaTeX formula="E_\gamma" /></div><div class="tk-fig"><ZoomablePlot src="/figures/datamc/photon-energy-h0.svg" alt="exclusive_hemi0_nearby_photon_energy: inclusive 1992–1995 data and luminosity-normalised simulation with ratio panel" /></div></section>
<section><div class="kin-caption">Visible pair mass: <LaTeX formula="m_{\tau\tau}^{\rm vis}" /></div><div class="tk-fig"><ZoomablePlot src="/figures/datamc/visible-mass.svg" alt="visible_tautau_mass: inclusive 1992–1995 data and luminosity-normalised simulation with ratio panel" /></div></section>
<section><div class="kin-caption">Radiative veto: <LaTeX formula="E_{\rm rad}/E_{\rm beam}" /></div><div class="tk-fig"><ZoomablePlot src="/figures/datamc/erad-over-ebeam.svg" alt="erad_over_ebeam: inclusive 1992–1995 data and luminosity-normalised simulation with ratio panel" /></div></section>
<section><div class="kin-caption">Radiative veto: <LaTeX formula="p_{\rm rad}/p_{\rm beam}" /></div><div class="tk-fig"><ZoomablePlot src="/figures/datamc/prad-over-pbeam.svg" alt="prad_over_pbeam: inclusive 1992–1995 data and luminosity-normalised simulation with ratio panel" /></div></section>
</div>

<!--
Original SVGs from Internal_Note datamc-inclusive-01/03/04; same inclusive selection after18cuts.
Leading track / nearby photons: source hemisphere0 (first thrust hemisphere; H1 in this talk's illustrations).
Nearby-photon spectrum is per photon, with correlated entries; no independent-bin chi2 is claimed.
Visible mass is reconstructed visible tau-pair mass, not a neutrino-reconstructed mass.
Radiative veto definitions remain those of preceding selection slides. Original numerical content and ratio panels unchanged.
1992–1995 signed MC normalised per year/process/point to run-quality luminosities; Z_ee excluded as documented in the note.
Calibration and data/MC differences are not treated as resolved. Click each plot to enlarge.
-->
