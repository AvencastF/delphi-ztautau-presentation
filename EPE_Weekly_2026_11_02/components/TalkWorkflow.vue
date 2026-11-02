<template>
  <div>
    <div class="tk-flow">
      <div class="tk-endpoint">
        <span class="tk-symbol"><LaTeX formula="Z\to\tau^+\tau^-" /></span>
        <h2>Selected events</h2>
        <p>Common preselection<br>Data and simulation</p>
      </div>
      <div class="tk-lanes">
        <div class="tk-lane">
          <h3>Decay identification</h3>
          <div class="tk-steps">
            <span>Four visible types per <LaTeX formula="\tau" /></span>
            <span class="tk-arrow"><LaTeX formula="\longrightarrow" /></span>
            <span>16 decay-pair regions</span>
          </div>
          <small><LaTeX formula="e,\;\mu,\;\pi,\;\rho" /> — here <LaTeX formula="\rho" /> is the rho meson</small>
        </div>
        <div class="tk-lane">
          <h3>Direction reconstruction</h3>
          <div class="tk-steps">
            <span>Generate the missing kinematics</span>
            <span class="tk-arrow"><LaTeX formula="\longrightarrow" /></span>
            <span>Rest-frame decay angles</span>
          </div>
          <small>Single angles probe polarisation; products probe correlations</small>
        </div>
      </div>
      <div class="tk-endpoint">
        <span class="tk-symbol"><LaTeX formula="\rho" /></span>
        <h2>Spin state</h2>
        <p>Six polarisations<br>Nine correlations</p>
      </div>
    </div>

    <div class="tk-primer">
      <div class="goal">
        <h3><LaTeX formula="\rho" /> · Full spin density matrix</h3>
        <p>The quantum state of the pair.</p>
      </div>
      <div>
        <h3><LaTeX formula="B_i^{\pm}" /> · 6 polarisation components</h3>
        <p>Each particle's average spin along three axes.</p>
      </div>
      <div>
        <h3><LaTeX formula="C_{ij}" /> · 9 spin correlations</h3>
        <p>How the two spins are related, for each pair of axes.</p>
      </div>
    </div>
  </div>
</template>
