# arXiv:2511.18345v1[quant-ph]23 Nov 2025

## Nonlinear Stochastic and Quantum Motion from Coulomb Forces

Luca Ornigotti,∗ Darren W. Moore,† and Radim Filip‡

Department of Optics, Palacký University, 17. listopadu 1192/12, 771 46 Olomouc, Czech Republic

Controllable nonlinear quantum interactions are a much sought after target for modern quantum technologies. They are typically difficult and costly to engineer for bespoke purposes. However controllable nonlinearities may have always been in reach via the natural and fundamental forces between quantum particles. The Coulomb interaction between charged particles is the simplest example. We show that after eliminating the harmonic part of the Coulomb force by an auxiliary linear force, the remaining reciprocal nonlinear part results in a directly observable non-reciprocal nonlinear effect: increase of the signal-to-noise ratio (SNR) of the coherent displacement of one particle, driven by the position noise, or uncertainty in quantum regime, in another particle. This essential evidence of nonlinear forces is present across large ranges of trap frequency and mass scales, as well as visible in both stochastic and quantum regimes.

#### I. INTRODUCTION

The control of quantum systems has proceeded apace and many experimental settings possess precise control over linear quantum systems [1, 2], as in quantum optics [3, 4] and quantum optomechanics [5], and the most simple nonlinear systems such as the Jaynes-Cummings model, exemplified in cavity-QED [6] or trapped ion systems [7]. To construct a large scale nonlinear system from such simple nonlinear systems is a current challenge and therefore many experiments are pushing into exciting nonlinear regimes where standard modes of analysis fail, often catastrophically. Such nonlinear regimes are, as might be expected, also the site of yet uncovered quantum phenomena and absolutely required for the most advanced quantum technologies to come to fruition [8, 9]. Similar statements can be made regarding recently developed platforms operating entirely in the classical regime and near the classical-quantum boundary, such as levitated nano-objects [10–21]. Such systems are on the road from being inherently stochastic in a high temperature environment to gradually reaching semiclassical and quantum domains. The resulting classical-toquantum transition with macroscopic objects will likely open access to unexplored physics once they enter nonlinear regimes, such as entanglement-by-heating [22], and with the possibility of applications in topics such as quantum sensing for parameter estimation [23, 24] or of gravity [25], quantum thermodynamics [26, 27] and even quantum computing [28, 29].

In fact the most prospective systems work in a regime derived from the natural forces between the particles. Perhaps the most widely exploited is the direct reciprocal interaction by the Coulomb force between a pair of charged particles. With state of the art technology such interactions can be controllably realised on large ranges of mass and frequency scales, from charged levitated

∗ luca.ornigotti@gmail.com † darren.moore@upol.cz ‡ filip@optics.upol.cz

nanoparticles [30–32] all the way down to trapped individual ions [33] and even recently between pairs of electrons [34]. When confined by effective harmonic traps, the linearisation of the force results in coupled harmonic oscillations, with each directional mode decoupled from the others [35]. We promote an approach to nonlinear effects which show themselves in the intermodal coupling achievable by going beyond the harmonic approximation. Such effects have already been observed in the rotating wave approximation for trapped ion systems [36–38]. However, the steps beyond this approximation in macroscopic mechanical systems have not been exploited yet. On the other hand, in the context of microscopic single ion heat engines cubic interactions between different radial and axial modes have been engineered by tailoring the trap geometry [39, 40].

As the first step we investigate directly observable nonlinear effects arising from fundamental forces beyond the harmonic approximation and outside any rotating wave approximations, in both classical stochastic and quantum mechanical regimes. In essence, the nonlinear effects are made manifest non-reciprocally through the noise or uncertainty stimulated properties of the system, in our case a coherent displacement of one particle driven via the noise or uncertainty in the other. By definition, this can only occur via nonlinear interaction of the particles. Even in an approximation where the intermodal effects along different directions are suppressed, this effect can be predicted by expanding the Coulomb interaction only to third order, the first nontrivial nonlinear term, and focusing on a single nonlinear interaction along the straight line between the particles. The interaction is compound, maintaining the reciprocity of the Coulomb force, but does not prevent the observation of non-reciprocal effects in classical and quantum regimes.

In what follows we will make these propositions more precise by introducing the simplest model, presenting testable results, then demonstrating how such effects can be understood in terms of a suitable approximation. The detection of nonlinear motion, quantified by a noise/uncertainty driven increase in the signal-to-noise ratio of the momentum displacement, demonstrates the activity of the nonlinear part of the Coulomb interac-

tion. These effects are shown to be observable across a range of experimentally relevant parameters. This forms a proof-of-principle step towards experimental verification in the stochastic and, later, the quantum regime. We expect that the observation of such effects will open further directions for further investigations beyond Gaussian entanglement [30, 31].

II. RESULTS

A. Nonlinear Motion From the Coulomb Force

A pair of equally charged particles of masses mi, i ∈ {1,2}, confined to a three dimensional harmonic trap and interacting via the Coulomb potential, can be arranged along the z axis by having a much greater trap frequency in that direction [15, 20, 21]. The axes can then be chosen so that the equilibrium points are d(i) = 0 0 zi,0 . Even beyond the harmonic approximation, where the motional axes are not decoupled, the interactions depend upon the distances between the two particles along the respective axes. If motion along the x and y axes is sufficiently cooled so that fluctuations along these axes are small, then the interactions between x or y, and z are suppressed. The Hamiltonian of the system can then be written as

p2i mi

- 1

- 2 i


κ (z1 − z2 − d)2

+ miωi2(zi − zi,0)2 +

H =

, (1)

where ωi are the trap frequencies, κ = q1q2/4πϵ0 is the coupling strength of the reciprocal interaction calculated

via the charge qi and the electric permittivity in vacuum ϵ0, and d = z1,0 − z2,0 the initial distance between the particles’ equilibrium positions. The setup is illustrated in Fig. 1a. In the harmonic approximation, expanding around the distance between the particles in each direction to second order, results in an extra displacement term in the z direction for both particles. The motion of the charged particles is then described by harmomically coupled oscillators with modified frequencies. The coupling induced between the particles is intramodal such that the modes along different axes do not talk to each other. The third order term introduces nonlinear and intermodal interactions. To isolate them, a compensating force eliminating the lower order contributions is necessary. The constant force can be compensated via linear tilt through an electrostatic force [41], whereas the linear force can be compensated by parametric control, such as feedback [42–44]. In the regime of optimal compensation, assumed throughout the manuscript, the still reciprocal interaction Hamiltonian can be approximated as

κ d4

κ d4

(z1 − z2)3 =

z13 − z23 + 3(z1z22 − z12z2) .

H3 ≈

(2) A non-optimal compensation still results in the nonreciprocal nonlinear effect, albeit reduced in visibility, see

SM Note 3. Due to the nonlinearity of the Coulomb force a reciprocal cubic interaction emerges along the z axis. This is a minimal model of the nonlinear Coulomb interaction between two particles. While similar nonlinear interactions can be constructed for ions directly via the trap geometry for hybrid radial and axial modes [39, 40], here the nonlinearity emerges directly from the Coulombic interaction between the particles. Both the trap and the compensation operate in the harmonic approximation, and therefore cannot contribute to the nonlinear effects outlined below. Differently than for optical cubic potentials [45], the interaction in Eq. 2 combines competing cubic nonlinearities. That is, the cubic single particle potential z13, z23, and the cubic interparticle potential z1z22, z12z2. Their vying nature may limit the direct observation of the interparticle nonlinear noise or uncertainty induced phenomena. Quantisation can be accomplished by promoting the canonical variables to operators satisfying the commutation relations [zi,pi] = i.

1. Classical Noise-Induced Momentum

Nonlinear interactions such as z12z2 allow for the possibility to coherently displace the momentum of one particle via increases in the initial position noise of the other. Heuristically, the complete reciprocal interaction term of Eq. (2) indicates that for initially uncorrelated states the mean momentum displacement in one mode is rapidly driven by the noise in the other i.e. ⟨pz

2,0⟩ − 3κ(⟨z12,0⟩ − 2⟨z2,0⟩⟨z1,0⟩ + ⟨z22,0⟩)t/d4. The reciprocal nature of the interaction Hamiltonian of Eq. (2) suggests that a separate asymmetrical manipulation performed solely on one of the two particles can enhance the inter-particle non-reciprocal noise-induced nonlinear effect observed on the other. For parametrically symmetric interactions, m1 = m2 and ω1 = ω2, the minimal asymmetrical manipulation is accomplished by unbalancing the initial distribution of thermal noise. That is, prepare the initial thermal state at temperature T = 300 K of particle 2 at an effective temperature of T2′ = 10 mK by cooling, while particle 1 is prepared in an oscillator thermal-equilibrium state at room temperature T1 = 300 K. These are zero-mean Gaussian states with variances in position σz2 = kBT/mω and momentum σp2 = mkBT, where T is the effective temperature of mode z and kB is the Boltzmann constant. During the dynamics the modes are immersed in thermal environments with T1,T2 = 300 K. This initial thermal distribution imbalance between T1 and T2′ minimises the thermal fluctuations ⟨p2z

2⟩ ≈ ⟨pz

2,0⟩, which otherwise obscure the noiseinduced effect, while simultaneously minimising any unwanted back-action effects on the particle whose noise drives the noise-induced effect. While the technical details of this preparation depend strongly on the chosen platform, we suggest a proof-of-principle state preparation scheme in SM Note 4.

In Fig. 2a we show the noise induced motion for this

![image 1](Ornigotti et al._2025_Nonlinear stochastic and quantum motion from Coulomb forces_images/imageFile1.png)

- Figure 1. Noise and uncertainty-induced momentum displacement via a nonlinear Coulomb interaction. a (i), a (ii) Illustration of the principle idea in classical and quantum regime. Two harmonically confined particles (blue, yellow) experience a nonlinear Coulomb interaction (red spring) along a single axis, together with a compensating force (green). In the classical regime, the stochastic particle 1 is prepared in oscillator equilibrium states via dissipation to thermal environment at


temperature T1, while particle 2 is initially cooled to T2′ = 10 mK in a room temperature environment T1 = T2 = 300 K. In the quantum regime, the particles are prepared in ground states and the only fluctuations arise from the quantum uncertainties. A weak linear damping with a rate Γ, acting only on particle 2, is present in order to ensure the stability of the effect. The trap frequency modulation, and mass disproportion of particle 1, as showed in the table, are used to generate unidirectional flow of fluctuations to particle 2, thus avoiding back-actions. b (i), b (ii) Time evolution of mean momentum ⟨pz2⟩, normalised to the initial standard deviation (top) and signal-to-noise ratio SNRpz

(bottom). For large noise (full circles), the SNR = 1/√2 is quickly reached by all regimes, but tuning frequency (blue) allows for better noise control. At lower noise (empty circles), the parametric symmetry is the only regime reaching the SNR bound (grey). In the quantum regime (b (ii)), the ground state fluctuations (empty circles) are equally harnessed by all regimes, whereas an initial uncertainty amplification, by freefall, (full circle) allows the SNR bound to be reached by all regimes. Symmetric (grey) and Tuning Frequency (blue) further experience the faster uncertainty growth (SNR drop), not visible for tuning mass (orange), which is also the best regime here.

2

parametrically symmetric case (grey). The classical simulations are carried out with the parameters ωi = 50 kHz, m1 = m2 = 8 × 10−17 kg, κ = 2.3 × 10−24 N m2 and

d = 3 µm, inspired by optical levitation [15, 20, 21, 32] and enriched with magnetic levitation [16, 17] platforms in mind as they operate with a wider trapping frequency

![image 2](Ornigotti et al._2025_Nonlinear stochastic and quantum motion from Coulomb forces_images/imageFile2.png)

#### Figure 2. Analysis of time evolution of variables undergoing nonlinear motion. Analysis of time evolution of position

z1 and momentum pz2 at different initial fluctuations of z1. The shaded area represents the standard deviation around the mean evolution (solid). All quantities are normalised to the standard deviation of their respective initial states. Symmetry

breaking by mass tuning (orange) and frequency tuning (blue) allows to control divergence in pz2 in both mean and standard deviation. In the classical regime (a) the mass tuning visibly performs better than the other strategies as it produces larger

momentum drift ⟨pz2⟩. For the quantum regime (b), the symmetric (grey) and frequency tuned (blue) outperform the mass tuned with the same metric. It confirms the result presented in Fig. 1 (b (i),b (ii)).

range. No displacement occurs in z1, however the noise grows rapidly. The mean momentum of the second particle, however, experiences a positive sharp increase away from zero as well as an increase in noise. This displacement is not critically outperformed by noise, as seen in the signal-to-noise ratio (SNR) in Fig. 1b(i) (empty circles). This is a sign of a direct noise-induced coherent

effect. Importantly, the SNR grows with increasing σz

(full circles) and can saturate the maximum of 1/√2 at the cost of large noise in the initial position of z1.

1,0

This effect can be explained by examining the Langevin equations of motion for the third order Coulomb term. These are given by

3κ d4

m2z¨2(t) + m2Γ ˙z2(t) ≈

m1z¨1(t) + m1Γ ˙z1(t) ≈ −

6κ d4

z12(t) + z22(t) − m2ω22 +

z1(t) z2(t) + 2ΓkBT2ξ2(t),

6κ d4

3κ d4

z2(t)2 + z12(t) − m1ω12 −

z2(t) z1(t) + 2ΓkBT1ξ1(t),

(3)

where Γ is the drag coefficient whose value and phenomenological origin depend upon implementation and ξ1,ξ2 are independent zero-mean Gaussian white noises with ⟨ξi(t′)ξi(t′′)⟩ = δ(t′ − t′′). In what follows we focus on the underdamped regime, with Γ = 10−4 Hz, as in the overdamped regime the nonlinear effect in momentum pz

2

is not visible (see SM Note 1). For parametric symmetry it is useful to discuss the dynamics using the mean value approximation, by reducing the two-body interaction into a one-body problem by virtue of the effective potentials V˜(z2) = −3κ⟨z1⟩2z2/d4 + ω˜2z22 − κz23/d4 and

V˜(z1) = 3κ⟨z2⟩2z1/d4 + ω˜1z12 + κz13/d4. In this framework, the unwanted back-action of z2 on z1 is understood as the mean displacement ⟨z2⟩ which (i) generates a drift in z1, as visible from the first term in V˜(z1), and (ii) modifies the frequency of the harmonic confinement of z1 via ω˜1 = m1ω12/2 − 3κ⟨z2⟩/d4. The imbalance in the initial noise properties minimises both back-action contributions at short transients t < 20 µs. That is, low temperature T2′ makes the noise-induced shift generated by the cubic potential in V˜(z2) negligible, keeping the position below the critical value of ⟨z2⟩ ≈ 1 µm

(calculated for the parameters used in numerical simulation) after which the effective frequency ω˜1 becomes negative and the harmonic confinement becomes an inverted quadratic potential, leading to unstable diverging trajectories. However, the noise in z1 is still substantially increasing in time, and can in general complicate both predictions and applications of nonlinearities. For large initial noise, as visible in Fig. 2 (a, grey), the higher order nonlinear terms of the Coulomb interaction make for a positive back-action z2 on z1. It results in a decrease of the noise of z1, even below that of its initial thermal state.

When the reciprocity in the nonlinear effect is further broken by either tuning the mass (at fixed frequency) or frequency (at fixed mass) of particle 1, the fluctuations in z1 are modified and the properties of the coherent motion are altered. The initial thermal state of z1 is determined by its dynamical variables m1, ω1, and local environmental temperature T1 via the standard deviation σz

1,0 = kBT/m1ω1. Changing the mass or frequency to pursue the symmetry breaking techniques results in a modification of the initial fluctuations. We therefore fix the noise properties to σz

1,0 = 30 nm to observe the effect arising from the nonlinear interaction with constant initial noise across different parameters regimes. That is, z1 is not prepared in an equilibrium state of its local oscillator but rather in an out-of-equilibrium thermally squeezed state.

Trapping a massive particle m1 ≫ m2 minimises its kinetic term p2z

/2m1, and as a result the position does not move away from its initial mean condition ⟨z1⟩ ≈ ⟨z1,0⟩. That is, the back-action is negligible for short transients,

1

- as visible. Differently than parametric symmetry, the additional imbalance of the mass reshapes the noise evolution of z1, keeping it close to its initial distribution


for low initial fluctuations. However, as visible in Fig. 2 (a, orange), large initial noise promotes a positive back-action loop over time, decreasing the fluctuations of z1 below the initial thermal state. It is similar to the parametric symmetry (grey) back-action effect, however its effect on particle 2 showcases a larger displacement although with larger fluctuations (orange shaded area). The resulting SNR in Fig. 1b(i), while increasing even at low fluctuations (empty circles), only saturates the bound for larger initial noise σz

σz

- 1,0


### (full circle). The short transient of p2 evolves as pz

1,0

(t′) ≈ pz

2

′

2,0 + 3κ t

0 ds′ z12(s′)/d4 − m2ω22z2,0t′ in the limit of zero damping Γ = 0. For mass tuning it leads to the following moments

3κtσz2

, SNR = ⟨p2⟩ σp

1,0 d4

⟨p2(t)⟩ ≈

≈

2

1 √2

. (4)

Alternatively, trapping particle 1 in a stiffer harmonic potential ω1 ≫ ω2 confines its noise dynamics to that of a harmonic oscillator for short transients. Its evolution is described by coherent oscillations approximately described by z1 ≈ z1,0 cos(ω1t) under the assumption of

vanishing initial velocity z˙1,0 = 0. As visible in Fig. 2 (a, blue) this oscillatory evolution dominates over the back-action for times of few tenths of microseconds. This added imbalance of frequency negatively impacts the dynamics, generating a lower momentum drift ⟨pz

2⟩, and a lower signal-to-noise ratio output Fig. 1 (b(i), blue) at small initial noise (empty circles), but it too saturates the 1/√2 bound at large initial noise σz

(full circles).

1,0

For tuning frequencies, the moments of momentum p2 approach

3κ 4d4ω1

1 √2

[2θ + sin(2θ)]σz2

, (5)

⟨pz

(t)⟩ ≈

1,0, SNR ≈

2

where θ = ω1t.

In the low noise limit, the added symmetry breaking lowers the SNR relative to the symmetric case (see

- Fig. 1b(i), empty circle). To reach it, an extra cost of

increasing initial noise σz

1,0 is required. Specifically, for tuning stiffness, the same SNR is reached at smaller displacement (see Fig. 2a, blue), while for tuning mass the SNR saturation is obtained with a much larger displacement (orange), making it a favorable strategy. This is further highlighted in Fig. 3a, where a target SNR = 1/√2 is fixed, and the output momentum displacement ⟨pz

2⟩ (top), and standard deviation σp

z2

(bottom) are plotted against input noise cost σz

1,0. It shows that for initial noise below σz

1,0 ≲ 100 nm, the parametric symmetry (grey) harnesses the noise of z1 through the Coulomb interaction more efficiently. However, for initial noise input beyond σz

1,0 ≳ 100 nm, tuning frequency (blue) generates the same signal-to-noise ratio with smaller output noise and momentum drift, while tuning mass (orange) reaches it with larger momentum drift. Fig. 3 shows that the best strategy, for large initial noise, is to break the symmetry by tuning mass to reach the target signal-tonoise with the largest momentum drift.

2. Quantum Uncertainty-Induced Momentum

As we decrease the initial noise to the ground state extension, that is σz

1,0

= 0.01 nm, the nonlinear effect in the stochastic framework described by Eq.(3) vanishes (see SM Note 2). Operating in the quantum regime of Eq. (3), using pure initial states, an analog of the previous noise-induced phenomena comes directly from the quantum fluctuations in z1. As expected, it is sufficient to produce momentum displacement on z2, as visible in

- Fig. 2b. In this section, the numerical simulation are performed


directly on Eq. (3), see SM Note 2, using the same parameters outlined in the previous section. All quantities are rescaled by the standard deviation of the initial state. For parametric symmetry, the quantum fluctuations of z1 induce a small drift in the momentum, further enhanced by the quantum fluctuation of z2 through the cubic nonlinearity, reaching ⟨pz

### )t/d4. The unwanted back-action force is too small to induce instabil-

2⟩ ≈ 3κ(σz2

### + σz2

1,0

2,0

![image 3](Ornigotti et al._2025_Nonlinear stochastic and quantum motion from Coulomb forces_images/imageFile3.png)

#### Figure 3. Noise/Uncertainty induced momentum under noise confinement. (a): The output displacement ⟨pz2⟩ (i),

= 1/√2 are plotted for the stochastic classical dynamics against the input noise σz1,0. At low initial input noise the parametric symmetry (grey) always reaches the target. At large input noise all regimes reach the target, but breaking the symmetry via tuning frequency (blue) provides the least noise output, and thus even smaller momentum displacement. Breaking symmetry by tuning mass (orange) is useful only between noise input 60 ≲ σz1,0 ≲ 100 nm. (b): The output displacement ⟨pz2⟩ (i), and standard deviation σpz

(ii) at the target signal-to-noise ratio SNRpz

and standard deviation σpz

2

2

(ii) at the target SNR for different initial uncertainty σz1,0. All regimes reach the target, but at different times. For parametric symmetry (grey) and tuning frequency (blue) the target is reached at t ≈ 1 µs, while for tuning mass (orange) the target is reached at larger times t ≈ 2 µs. Regardless of the required time, when the target is reached, all regimes produce the same displacement and standard deviation output making the parametric symmetry (grey) the preferred strategy to reach the target with the minimum noise cost. Note, breaking symmetry requires extra squeezing to reach the same initial noise input. The dashed filled circles record the value of momentum displacement and standard deviation when the target SNR is not reached .

2

ity, therefore the noise of z1 does not increase larger than its reference state. It drives the momentum ⟨pz

2⟩ with an increasing SNR (panel c1, empty circles) that does not reach the maximum of 1/√2, as for times t > 2µs the cubic nonlinearity dominates both dynamics and the back-action strongly drives z1 to instability. It enhances the noise of p2 beyond the initial ground state, thus resulting in a drop of the SNR. The conservative symmetry breaking strategies, introduced for the stochastic dynamics, result in a qualitatively similar time evolution (see Fig. 2b, blue and orange).

The initial standard deviation σz

1,0 = ℏ/(2m1ω1) is calculated using the same parameters of the stochastic system. For parametric symmetry, i.e., m1 = 8×10−17 kg and ω1 = 50 kHz, the initial standard deviation results in σz

1,0 = 0.01 nm. For tuning frequency, i.e., ω1 = 2500 kHz, and tuning mass m1 = 8 × 10−16 kg, the initial standard deviations assume different values.

1,0 = 0.003 nm. To observe only the effects of the nonlinear interaction given by the dynamics, under the same initial noise conditions, the initial state of z1 is squeezed by a factor ξ = −log(σtrg m1ω1/ℏ)/2 to reach the unified target standard deviation of σtrg = 0.01 nm. That is, the position variance is amplified σz

Respectively σz

1,0 = 0.001 nm, and σz

1,0 = ξ ℏ/(2m1ω1) by ξ, while the momentum variance is attenuated by the inverse amount σp

= ℏm1ω1/2/ξ.

z1,0

When the initial ground state of z1 is further squeezed in momentum, it realises a larger drift reaching a SNR = 1/√2 at short transients (Fig. 1, panel b2). Notice that parametric symmetry (grey) and tuning frequency (blue) are subjected to instability for times larger than t ≈ 1µs, resulting in a drop of the signal-to-noise ratio, while tuning mass (orange) is not yet affected by it.

For tuning mass m1 ≫ m2 the short transient of the

moments of p2 approach

3κtσz2

1,0 d4

⟨pz

2⟩ ≈

,

d8σp2

m22ω24d8σz2

− 21

1 √2

z2,0 18κ2σz4

2,0 18κ2σz4

≈

SNRp

1 +

+

.

1,0t2

z2

1,0

(6)

For short transients, the ground state momentum noise σp2

z2,0 prevents the signal-to-noise ratio from reaching the 1/√2 bound. At larger time it becomes negligible, leaving the position noise σz2

2,0 as the dominant limiting term of the evolution. For fixed m2,ω2, an amplification of position noise σz2

1,0 by ξ allows to reach a SNR = 1√2 as visible in Fig. 1b(ii) , full orange circle. That is, the initial state is further squeezed in momentum. Squeezing the position noise σz2

1,0 = ξσz2

2,0 can in principle improve upon the signal-to-noise ratio of Eq. (6). However, the complementary amplification of momentum noise σp2

z2,0 increases the back-action to particle 1

- at larger times, thus leading to the divergence quicker.


For tuning frequency ω1 ≫ ω2, the noise of z1 is confined in a stiffer harmonic bound, and its dynamics is described as z1 ≈ z1,0 cos(θ), with θ = ω1t. In this regime the dynamics evolves similarly to that of the parametric symmetry as visible in Fig. 1(ii), blue and grey circles. Its momenta evolve in short transients according to

3κσz2

1,0 4d4ω1

⟨pz

2⟩ ≈

[2θ + sin(2θ)],

8ω22d8σp2

z2,0 + 8ω12d8t2σz2

− 21

1 √2

2,0 9κ2σz4

≈

SNRp

.

1 +

1,0 [2θ + sin(2θ)]2

z2

(7) For an initial ground state σz2

1,0 = ℏ/(2m1ω1), the momentum and position noise of the initial state of particle

- 2, i.e., σz2


z2,0 hinders the uncertainty-induced effect from reaching the SNR = 1/√2 bound at short transients. For longer time the instability from the cubic potential, not accounted for in Eq. (7), dominates the dynamics resulting in a drop of the signal-to-noise ratio. Similar to tuning mass, to reach the signal-to-noise bound for short transients, the amplification of position noise σz2

2,0,σp2

1,0 is required, as visible in Fig. 1b(ii), full blue circles. Moreover, squeezing the position noise σz

2,0 results in faster divergence, similar to the case of tuning mass.

The hidden cost of parametric symmetry breaking lies in the preparation of the initial state, which requires squeezing of the ground state. That is, to have comparable noise in position of σz

1,0 = 0.01 nm after tuning mass and frequency the ground state must be squeezed, by ξ = 1.15 and ξ = 1.96 respectively. For the large noise case, a further amplification by freefall is then used to reach the position noise in all regimes of σz

1,0 = 0.08 nm. In Fig. 3b, the target SNR = 1/√2 is reached equally by all regimes for initial input noise σz

1,0 ≳ 0.06 nm, but at different times. Ultimately, the parametric symmetry

emerges as the best regime, as it does not require any extra costs, i.e., the initial squeezing to σz

1,0 = 0.01 nm, as is the case of the mass and frequency tuning regimes.

#### III. CONCLUSION

Experiments involving the interaction of trapped charged particles typically operate in the harmonic approximation [30, 31, 35], where the motion decouples into oscillations along each coordinate axis. This can only result in Gaussian effects: single particle and multiparticle squeezing, and potentially, entanglement in the quantum regime. Here we have shown a proof-of-principle method to go beyond this approximation, showing that the inherently nonlinear effect of noise-induced coherent motion can be seen and explained using the first nontrivial nonlinear term in an expansion of the reciprocal Coulomb interaction between two charged particles. This is observed in Fig. 1b(i) by the non-reciprocal effect: improvement in SNR of one particle due to increased position thermal noise in another nonlinearly coupled particle. This effect persists into the quantum regime, where now the quantum uncertainty rather than classical noise drive the dynamics of the test particle to the same SNR bound of classical dynamics, at smaller momentum displacement. It is visible in Fig. 1b(ii).

This method provides the first step to analysing one of the most basic two-particle nonlinear effects, as visible in Fig. 3. Noise control is an important basic tool for control of technologies that are inherently stochastic. Advantageously, this can be done autonomously through naturally occurring forces, lowering the engineering requirements to make such effects visible across a broad range of parameters and platforms. It should be noted that nano-particles possess a natural advantage compared to ions as their mass-charge ratio favours observation of the short time nonlinear effects. That is, their high charge and high mass range capabilities allow for a stronger interaction tunability and slower divergence respectively.

To date, the most in-depth studies of motional nonlinear systems are of single-mode nonlinearities, possibly linked to other linear systems. Increasingly detailed studies of experimentally accessible two-particle nonlinear interactions will likely unveil many unexpected effects. Breaching further into genuinely multipartite systems combines the complexity of the many possible configurations (chains, triangles, lattices, or clusters) [46– 48] with that of a nonlinear interaction distributed across multiple particles, likely hiding exciting nonlinear effects. This then opens the possibility to further exploit such nonlinearity in naturally occurring interactions.

#### IV. ACKNOWLEDGEMENTS

We acknowledge the project GA23-06224S of the Czech Science Foundation, EU and MEYS Czech Republic No.

CZ.02.01.01/00/22_008/0004649 (QUEENTEC). R.F. also acknowledges funding from the MEYS of the Czech Republic (Grant Agreement 8C22001). Project SPARQL has received funding from the European Union’s Horizon 2020 Research and Innovation Programme under Grant Agreement no. 731473 and 101017733 (QuantERA).

#### V. DATA AND CODE AVAILABILITY

Data sharing not applicable to this article as no datasets were generated or analysed during the current study. Code available upon reasonable request.

#### VI. COMPETING INTERESTS

The authors declare no competing interests.

#### VII. AUTHOR CONTRIBUTIONS

LO performed the numerical simulations and analytical solutions to the classical dynamics and DM performed the quantum mechanical calculations. Both received theory inputs from RF. RF conceived and supervised the project. All authors contributed to the analysis of the results and composition of the article.

- [1] C. Weedbrook, S. Pirandola, R. García-Patrón, N. J. Cerf, T. C. Ralph, J. H. Shapiro, and S. Lloyd, Reviews of Modern Physics 84, 621 (2012), publisher: American Physical Society.
- [2] G. Adesso, S. Ragy, and A. R. Lee, Open Systems & Information Dynamics 21, 1440001 (2014), publisher: World Scientific Publishing Co.
- [3] N. J. Cerf, G. Leuchs, and E. S. Polzik, Quantum Information with Continuous Variables of Atoms and Light (Imperial College Press, 2007).
- [4] W. Asavanant and A. Furusawa, Optical Quantum Computers: A Route to Practical Continuous Variable Quantum Information Processing (AIP Publishing LLCMelville, New York, 2022).
- [5] W. P. Bowen and G. J. Milburn, Quantum Optomechanics (CRC Press, 2015).
- [6] A. Blais, A. L. Grimsmo, S. M. Girvin, and A. Wallraff, Reviews of Modern Physics 93, 025005 (2021), publisher: American Physical Society.
- [7] C. Monroe, W. C. Campbell, L.-M. Duan, Z.-X. Gong, A. V. Gorshkov, P. W. Hess, R. Islam, K. Kim, N. M. Linke, G. Pagano, P. Richerme, C. Senko, and N. Y. Yao, Reviews of Modern Physics 93, 025001 (2021), publisher: American Physical Society.
- [8] C. Calcluth, N. Reichel, A. Ferraro, and G. Ferrini, PRX Quantum 5, 020337 (2024), publisher: American Physical Society.
- [9] W. Asavanant and A. Furusawa, Physical Review A 109, 040101 (2024), publisher: American Physical Society.
- [10] C. Timberlake, G. Gasbarri, A. Vinante, A. Setter, and H. Ulbricht, Applied Physics Letters 115, 224101 (2019).
- [11] A. Vinante, P. Falferi, G. Gasbarri, A. Setter, C. Timberlake, and H. Ulbricht, Phys. Rev. Appl. 13, 064027

(2020).

- [12] G. P. Conangla, R. A. Rica, and R. Quidant, Nano Letters 20, 6018 (2020).
- [13] V. Svak, J. Flajšmanová, L. Chvátal, M. Šiler, A. Jonáš, J. Ježek, S. H. Simpson, P. Zemánek, and O. Brzobohatý, Optica, Optica 8, 220 (2021).
- [14] F. Tebbenjohanns, M. L. Mattana, M. Rossi, M. Frimmer, and L. Novotny, Nature 595, 378 (2021).
- [15] J. Rieser, M. A. Ciampini, H. Rudolph, N. Kiesel, K. Hornberger, B. A. Stickler, M. Aspelmeyer, and U. Delić, Science 377, 987 (2022).


- [16] J. Hofer, R. Gross, G. Higgins, H. Huebl, O. F. Kieler, R. Kleiner, D. Koelle, P. Schmidt, J. A. Slater, M. Trupke, K. Uhl, T. Weimann, W. Wieczorek, and M. Aspelmeyer, Phys. Rev. Lett. 131, 043603 (2023).
- [17] M. Gutierrez Latorre, G. Higgins, A. Paradkar, T. Bauch, and W. Wieczorek, Phys. Rev. Appl. 19, 054047 (2023).
- [18] C. D. Brown, Y. Wang, M. Namazi, G. I. Harris, M. T. Uysal, and J. G. E. Harris, Phys. Rev. Lett. 130, 216001

(2023).

- [19] D. S. Bykov, L. Dania, F. Goschin, and T. E. Northup, Optica 10, 438 (2023).
- [20] O. Brzobohatý, M. Duchaň, P. Jákl, J. Ježek, M. Šiler, P. Zemánek, and S. H. Simpson, Nature Communications 14, 5441 (2023).
- [21] M. Reisenbauer, H. Rudolph, L. Egyed, K. Hornberger, A. V. Zasedatelev, M. Abuzarli, B. A. Stickler, and U. Delić, Nature Physics , 1 (2024), publisher: Nature Publishing Group.
- [22] P. Laha, D. W. Moore, and R. Filip, Physical Review Letters 132, 210201 (2024), publisher: American Physical Society.
- [23] P. A. Ivanov, Physical Review A 105, 032617 (2022), publisher: American Physical Society.
- [24] P. Mahmoudi, A. Ritboon, and R. Filip, Physical Review Research 6, 043215 (2024), publisher: American Physical Society.
- [25] M. Carlesso, A. Bassi, M. Paternostro, and H. Ulbricht, New Journal of Physics 21, 093052 (2019), publisher: IOP Publishing.
- [26] E. A. Martinez, Physical Review Letters 110 (2013), 10.1103/PhysRevLett.110.130406.
- [27] K. J. Ray, A. B. Boyd, G. Guarnieri, and J. P. Crutchfield, Physical Review E 108, 054126 (2023), publisher: American Physical Society.
- [28] D. W. Moore, Physical Review A 100, 062301 (2019).
- [29] L. Vandré’, B. Jing, Y. Xiang, O. Gühne, and Q. He, “Graphical Calculus for Non-Gaussian Quantum States,”

(2024).

- [30] H. Rudolph, U. Delič, M. Aspelmeyer, K. Hornberger, and B. A. Stickler, Physical Review Letters 129, 193602

(2022), publisher: American Physical Society.

- [31] T. W. Penny, A. Pontin, and P. F. Barker, Physical Review Research 5, 013070 (2023), publisher: American Physical Society.


- [32] Q. Deplano, A. Pontin, A. Ranfagni, F. Marino, and F. Marin, “Coulomb coupling between two nanospheres trapped in a bichromatic optical tweezer,” (2024).
- [33] C.-H. Nguyen, K.-W. Tseng, G. Maslennikov, H. C. J. Gan, and D. Matsukevich, arXiv:2103.10219 [physics, physics:quant-ph] (2021), arXiv: 2103.10219.
- [34] N. R. Beysengulov, O. S. Schøyen, S. D. Bilek, J. B. Flaten, O. Leinonen, M. Hjorth-Jensen, J. Pollanen, H. E. Kristiansen, Z. J. Stewart, J. D. Weidman, and A. K. Wilson, PRX Quantum 5, 030324 (2024).
- [35] X.-L. Deng, D. Porras, and J. I. Cirac, Physical Review A 77, 033403 (2008), publisher: American Physical Society.
- [36] S. Ding, G. Maslennikov, R. Hablützel, H. Loh, and D. Matsukevich, Physical Review Letters 119, 150404

(2017), publisher: American Physical Society.

- [37] S. Ding, G. Maslennikov, R. Hablützel, and D. Matsukevich, Physical Review Letters 121, 130502 (2018), publisher: American Physical Society.
- [38] G. Maslennikov, S. Ding, R. Hablützel, J. Gan, A. Roulet, S. Nimmrichter, J. Dai, V. Scarani, and D. Matsukevich, Nature Communications 10, 202 (2019), number: 1 Publisher: Nature Publishing Group.
- [39] O. Abah, J. Roßnagel, G. Jacob, S. Deffner, F. SchmidtKaler, K. Singer, and E. Lutz, Physical Review Letters 109, 203006 (2012), publisher: American Physical Soci-


- ety.
- [40] J. Roßnagel, S. T. Dawkins, K. N. Tolazzi, O. Abah, E. Lutz, F. Schmidt-Kaler, and K. Singer, Science 352, 325 (2016).
- [41] M. A. Ciampini, T. Wenzl, M. Konopik, G. Thalhammer, M. Aspelmeyer, E. Lutz, and N. Kiesel, “Experimental nonequilibrium memory erasure beyond Landauer’s bound,” (2021).
- [42] A. Setter, M. Toroš, J. F. Ralph, and H. Ulbricht, Physical Review A 97, 033822 (2018).
- [43] G. P. Conangla, F. Ricci, M. T. Cuairan, A. W. Schell, N. Meyer, and R. Quidant, Physical Review Letters 122, 223602 (2019).
- [44] L. Magrini, P. Rosenzweig, C. Bach, A. DeutschmannOlek, S. G. Hofer, S. Hong, N. Kiesel, A. Kugi, and M. Aspelmeyer, Nature 595, 373 (2021).
- [45] A. A. Rakhubovsky and R. Filip, npj Quantum Information 7, 1 (2021).
- [46] Y. Lu, W. Chen, S. Zhang, K. Zhang, J. Zhang, J.-N. Zhang, and K. Kim, (2023), arXiv:2311.04864 [quantph].
- [47] N. E. Frattini, U. Vool, S. Shankar, A. Narla, K. M. Sliwa, and M. H. Devoret, Applied Physics Letters 110, 222603 (2017).
- [48] D. S. Bykov, M. Meusburger, L. Dania, and T. E. Northup, Review of Scientific Instruments 93, 073201


(2022).

