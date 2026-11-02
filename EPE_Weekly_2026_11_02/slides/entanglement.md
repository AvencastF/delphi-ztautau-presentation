---
class: st pres tk tk-qis-intro
---

# Quantum-information observables

<div class="st-sub">The full spin density matrix <LaTeX formula="\rho" /> gives access to entanglement, quantum magic and Bell nonlocality.</div>

<div class="qis-columns">
<section class="qis-column qis-entanglement">
<h2>Quantum entanglement</h2>
<p class="qis-description">Quantified by concurrence</p>
<div class="qis-equation"><LaTeX formula="\mathcal C[\rho]=\max\!\left(0,\lambda_1-\lambda_2-\lambda_3-\lambda_4\right)" /></div>
<div class="qis-definition">
<p><LaTeX formula="\lambda_i" />: ordered square roots of eigenvalues of <LaTeX formula="\rho\tilde\rho" />.</p>
<LaTeX formula="\tilde\rho=(\sigma_y\otimes\sigma_y)\rho^*(\sigma_y\otimes\sigma_y)" />
</div>
<div class="qis-criteria qis-qe-criteria">
<p><LaTeX formula="\mathcal C\gt0" /> <span>Entangled; <LaTeX formula="\mathcal C=0" /> separable</span></p>
<p class="qis-witness-formula"><LaTeX formula="W=C_{nn}-C_{rr}+C_{kk}-1\gt0" /></p>
<small>Witness: sufficient, not necessary.</small>
</div>
</section>

<section class="qis-column qis-magic">
<h2>Quantum magic</h2>
<p class="qis-description">Non-stabilizerness</p>
<div class="qis-equation"><LaTeX formula="\mathcal M_2=-\log_2\!\left(\frac{1+S_4}{1+S_2}\right)" /></div>
<div class="qis-definition">
<LaTeX formula="S_p=\sum_i\!\left[(B_i^-)^p+(B_i^+)^p\right]+\sum_{ij}(C_{ij})^p" />
<p>Second stabilizer Rényi entropy in the chosen Pauli basis.</p>
</div>
<div class="qis-criteria">
<p><LaTeX formula="\mathcal M_2\gt0" /> <span>Magic for pure states</span></p>
<p><LaTeX formula="\mathcal M_2=0" /> <span>Pure stabilizer states</span></p>
<small>Mixed states: the extension defined above.</small>
</div>
</section>

<section class="qis-column qis-bell">
<h2>Bell nonlocality</h2>
<p class="qis-description">Optimal CHSH parameter</p>
<div class="qis-equation"><LaTeX formula="\mathcal B_{\max}=2\sqrt{m_1+m_2}" /></div>
<div class="qis-definition">
<p><LaTeX formula="m_1,m_2" />: the two largest eigenvalues of <LaTeX formula="C^{\mathsf T}C" />.</p>
<p>Uses the full spin-correlation matrix <LaTeX formula="C" />.</p>
</div>
<div class="qis-criteria">
<p><LaTeX formula="\mathcal B_{\max}\gt2" /> <span>CHSH violation</span></p>
<p><LaTeX formula="\mathcal B_{\max}\le2" /> <span>No CHSH violation</span></p>
</div>
</section>
</div>

<div class="tk-foot">Y.-C. Guo, T. Han, M. Low and Y. Su, <a href="https://arxiv.org/abs/2602.02719" target="_blank" rel="noopener noreferrer">arXiv:2602.02719</a>.</div>

<!--
Introductory observables, not results. Guo et al. arXiv:2602.02719 Section II, Eqs. 4-5 (concurrence), 8 (optimal CHSH), 11-12 (mixed-state SRE extension).
The screenshot's lambda definition was corrected: lambda_i are the nonnegative square roots of eigenvalues of rho times spin-flipped rho, not eigenvalues of rho. Spin flip is expressed in the computational basis. Avoid naming the auxiliary matrix R, already used for Pauli coefficients on the previous slide.
Bell uses the full correlation matrix and optimal CHSH expression, not the screenshot's restricted diagonal approximation. Failure to violate CHSH does not establish locality for every possible Bell test.
For magic, S_p is a compact algebraic abbreviation of Eq. 12; p=2 or 4. The pure-state interpretation is stated explicitly: for mixed states this Pauli-moment extension is not a faithful witness of membership outside the convex set of stabilizer mixtures. No claim that every positive mixed-state value proves resource-theoretic magic.
Collider-inferred Bell observables are not a loophole-free test of local realism. All simulated reference numbers and the prior result table have been removed from this introductory slide.
-->
