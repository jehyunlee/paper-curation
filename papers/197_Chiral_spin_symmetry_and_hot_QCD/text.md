# arXiv:2402.05852v2[hep-lat]15 Feb 2024

## Chiral spin symmetry and hot QCD ∗

#### L. Ya. Glozman

Institute of Physics, University of Graz, A-8010 Graz, Austria

Received February 16, 2024

In this talk we overview main results indicating existence in QCD of three qualitatively different regimes connected by smooth crossovers upon heating: a hadron gas, a stringy fluid and a quark-gluon plasma. In the combined large Nc and chiral limit these regimes likely become distinct phases separated by phase transitions: a chiral restoration phase transition around Tch ∼ 130 MeV and a deconfinement phase transition around Td ∼ 300 MeV. It should be an important task to verify this issue on the lattice. We will introduce a chiral spin symmetry, which is a symmetry of the electric part of electrodynamics and of QCD with light quarks. It is realized approximately in QCD above the chiral restoration crossover and disappears in the QGP regime. The center symmetry of the pure glue action and the chiral spin symmetry of the electric part of the QCD Lagrangian with light quarks are complementary to distinguish the confining regime and its disappearance. We also address other lattice evidences for stringy fluid: hadron resonances extracted from the lattice correlators; breakdown of the thermal perturbation theory at T < 600 MeV and fluctuations of conserved charges that point out the Nc scaling above T ∼ 155 MeV.

### 1. Chiral spin symmetry

Consider Maxwell equations that describe evolution of the electric and magnetic fields in a given reference frame:

divE⃗ = 4πρ rotB⃗ −

∂E⃗ ∂t

4π c

1 c

⃗j

=

∂B⃗ ∂t

1 c

rotE⃗ +

= 0 divB⃗ = 0. (1)

∗ Presented at Excited QCD 2024; Benasque, 14 - 20.01.2024

(1)

We define E⃗ and B⃗ in a given Lorentz frame in a gauge-invariant way through their action on charge and current,

⃗v c × B.⃗ (2)

F⃗ = qE⃗ + q

It is possible to measure directly F⃗ in electrodynamics but not possible in quantum chromodynamics. Is there another method to distinguish E⃗ and B⃗?

Consider charges to be massless particles with s = 1/2. They can be either right- or left-handed:

R L

. (3)

Consider a SU(2)CS chiral spin transformation that mixes R and L:

εnσn 2

R′ L′

R L →

R L

. (4) What happens with the charge density ρ?

= exp i

R′†R′ + L′†L′ = R†R + L†L, (5) i.e.

ρ′ = ρ. (6)

The charge density is invariant under the chiral spin transformation. However, upon the chiral spin transformation the current density⃗j and ⃗v change. We conclude that the interaction of a charge with the electric field is invariant under the chiral spin transformation, while interaction of a current with the magnetic field is not. This means that the chiral spin symmetry allows one to distinguish the electric and magnetic fields in a given reference frame. The electric part of the EM theory is more symmetric than the magnetic part.

The chromoelectric field of QCD is defined via interaction with the color charge

F⃗ = QaE⃗a; Qa = d3x q†(x)Taq(x), a = 1,...,8. (7)

The color charge, which is Lorentz-invariant, is invariant under SU(2)CS:

εnΣn 2

q → q′ = exp i

q, Σ = {γk,−iγ5γk,γ5}. (8)

In a given Lorentz frame interaction of quarks with the electric part of the gluonic field is chiral spin invariant like in electrodynamics. The SU(2)CS symmetry includes U(1)A as a subgroup.

We can extend the SU(2)CS symmetry to SU(2NF): SU(2)CS×SU(NF) ⊂

SU(2NF) and SU(NF)R × SU(NF)L × U(1)A ⊂ SU(2NF). The SU(2NF) is also a symmetry of the color charge and of the electric part of the QCD Lagrangian. I.e., the color charge and electric part of the theory have a SU(2NF) symmetry that is larger than the chiral symmetry of QCD as a whole. The fundamental vector of SU(2NF) at NF = 2 is

ΨT = (uR uL dR dL). (9)

Notice that the Dirac Lagrangian is not invariant under SU(2)CS and SU(2NF) above: The chiral spin symmetry and its flavor extension are explicitly broken by magnetic interactions and by the quark kinetic terms.

Since the confining interaction in QCD is associated with the emergence of the color-electric flux tubes that connect static quarks we can consider the chiral spin symmetry as a symmetry of the confining interaction with the ultrarelativistic light quarks. The necessary and sufficient conditions for emergence of the approximate chiral spin symmetry are: (i) both chiral symmetries in QCD must be at least approximately restored and (ii) the quark-electric interaction must strongly dominate over the quark-magnetic interaction and over quark kinetic terms. The latter condition means that the physics must be dominated by a confining electric field.

The discussed symmetries were introduced in Refs. [1, 2]. For review on symmetries and their implications for hadrons and for hot QCD see Ref. [3].

### 2. Emergence of the chiral spin symmetry above chiral restoration crossover and its implications

The most detailed information about QCD is encoded in correlation functions

CΓ(t,x,y,z) = ⟨OΓ(t,x,y,z)OΓ(0,0)†⟩ . (10) They carry the full spectral information.

In Fig. 1 we show spatial correlators of all possible J = 0,1 isovector

bilinears OΓ at different temperatures obtained within NF = 2 QCD with chirally symmetric Dirac operator [4]. We see a distinct multiplet structure

of the correlators. The multiplet E1 evidences restored U(1)A symmetry (at least approximately); the multiplet E2 demonstrates approximate chiral spin and SU(4) symmetries; the multiplet E3 is consistent with chiral symmetry alone and with chiral spin (and SU(4)) symmetry and hence could

100

100

###### 220 MeV 32x12

###### 380 MeV 32x8

10-1

10-1

10-2

10-2

E1

C(n) / C(n=1)zz

C(n) / C(n=1)zz

10-3

PS

10-3

S

E1

10-4

E2

Vx

Vt

10-4

10-5

Ax

E3

At Tx Tt

| | |
|---|---|
| | |
| | |


E3 E2

10-6

10-5

Xx

| | |
|---|---|
| | |


| | |
|---|---|
| | |


10-7

Xt

10-6

0.0 0.5 1.0 1.5 2.0

0.0 0.5 1.0 1.5 zT

zT

- Fig.1. Spatial correlators of all possible J = 0,1 bilinears. Source: From Ref. [4].

10-2

10-1

100

0.1 0.2 0.3 0.4 0.5

PS, S

b1, ρ(1/2,1/2)b

a1, ρ(1,0)+(0,1)

non interacting

C(t) / C(t=1)

tT

0.1 0.2 0.3 0.4 0.5

10-2

10-1

100

PS, S

b1, ρ(1/2,1/2)b

a1, ρ(1,0)+(0,1)

full QCD

C(t) / C(t=1)

tT

PS

S ρ(0,1)+(1,0)

- a1

ρ(1/2,1/2)b

- b1


- Fig.2. Temporal correlators for 12 × 483 lattices. Left: correlators obtained with free quarks. Right: full QCD correlators at T = 220 MeV. Source: From Ref. [5]


be ignored. The chiral spin symmetry and its flavor extension persist up to T ∼ 500 MeV. At larger temperatures two distinct multiplets E1 and E2 disappear because the QCD correlators approach correlators obtained with free quarks. Notice that the latter correlators do not have the chiral spin symmetry because the Dirac Lagrangian is not CS-symmetric; for analytic and lattice results for all possible ”free correlators” see Ref. [4]. An apparent mergence of the E1 and E2 multiplets at very high temperatures is due to the fact that at T → ∞ all J = 0,1 screening masses from E1 and E2 approach their limiting value 2πT, which is not related to any dynamical symmetry.

In Fig. 2 we show temporal correlators for all possible J = 0,1 isovector bilinears [5]. The full QCD correlators demonstrate U(1)A and SU(2)L × SU(2)R multiplets as well as approximate SU(2)CS and SU(4) multiplets. In contrast, qualitatively different correlators obtained with noninteracting quarks exhibit only U(1)A and SU(2)L × SU(2)R multiplets.

We conclude that above the chiral restoration crossover QCD partition function is not only chiral symmetric, but is also approximately SU(2)CS and SU(4) symmetric. This suggests that QCD is still in the confining regime until roughly 500 MeV where confining chromoelectric field gets screened and SU(2)CS and SU(4) symmetries smoothly disappear. Similar results have recently been obtained in 2 + 1 + 1 QCD [6].

6.8

mP mV

mscr./T

ud¯

1.08

6.6

1.06

6.4

m/2πT

6.2

1.04

A V S P

6.0

1.02

Nτ = 6 Nτ = 8 Nτ = 10 Nτ = 12

5.8

1

T[GeV]

5.6

80 GeV 10 GeV 2 GeV 1 GeV

0.5 1.0 1.5 2.0 2.5 3.0

0 0.5 1 1.5 2 2.5

gˆ2

- Fig.3. Left:Temperature dependence of the pseudoscalar and vector screening masses at very large T. Source: From Ref. [7]. Right: The same but for lower temperatures. Source: From Ref. [8]


### 3. Breakdown of thermal perturbation theory below 500 − 600MeV

Lattice results for pseudoscalar and vector screening masses obtained at very large temperatures T ∼ 1 - 160 GeV [7] are shown in Fig. 3, left panel. They can be parameterized [7] over two orders of magnitude by

mPS 2πT

= 1 + p2 gˆ2(T) + p3 gˆ3(T) + p4 gˆ4(T) ,

mPS 2πT

mV 2πT

+ s4 gˆ4(T) ,

=

where p2 is fixed by EQCD calculations and p3,p4,s4 are numbers that are fitted to lattice results. A perturbative description of screening masses suggests partonic degrees of freedom, which is a signal of QGP.

Screening masses at lower temperatures, above chiral restoration crossover

up to T ∼ 2.5 GeV are shown in the right panel [8]. While the temperature dependence of screening masses above 500 - 600 MeV is flat and consistent with those shown in the left panel, at lower temperatures the screening masses demonstrate a steep increase. The temperature dependence in the partonic (QGP) regime is only in coupling constants. Given that the coefficients p2,p3,p4,s4 are fixed by the high T behavior of screening masses, the perturbative expansion cannot explain screening masses below 500-600 MeV. We observe an apparent change of dynamics at temperatures below 500-600 MeV. The behavior of meson screening masses from 12 different channels provides an independent demonstration of the existence of the regime below 500-600 MeV where chiral symmetry is restored but the dynamics is inconsistent with the partonic description. The discussed behavior of screening masses must be reflected in the equation of state. Indeed, a very

- 1.× 10-13

- 2.× 10-13

- 3.× 10-13

- 4.× 10-13

- 5.× 10-13

- 6.× 10-13

- 7.× 10-13


|T=220 MeV T=320 MeV T=380 MeV T=480 MeV T=660 MeV T=960 MeV<br><br>|
|---|


-24/ω[]MeVPS

ρ

0

0 500 1000 1500 2000 2500 3000

ω [MeV]

- Fig.4. Pion spectral function at different temperatures reconstructed from spatial lattice correlators presented in Fig. 1. Source: From Ref. [12].


steep increase of p/T4 with temperature in the same temperature interval is observed [9]. The analysis presented in this section was done in Ref. [10].

### 4. Pion spectral function

Direct evidence of the hadron-like degrees of freedom in stringy fluid should be observation of states in spectral functions. Using a finite T generalization of the K¨llen-Lehmann spectral representation [11] Refs. [12, 13] reconstructed pion and kaon spectral functions from the spatial lattice correlators above chiral restoration. The pion spectral function is shown in Fig.

- 4 [12]. The spectral function demonstrates two distinct peaks corresponding to pion and its first radial excitations. These peaks get broader with temperature and eventually melt above 500-600 MeV out. The so obtained spectral function can be controlled because it predicts the temporal correlators that can be compared with lattice results. The comparison shows a good agreement at large Euclidean times.
- 5. Conserved charges and their fluctuations in hadron gas and at higher temperatures. Temperature evolution of the Polyakov


### loop.

The hadron resonance gas model assumes a dilute system of point-like structureless hadrons that do not interact. For T < 155 MeV the hadron resonance gas model reproduces fluctuations of conserved charges calculated on the lattice, see e.g. [14]. At larger temperatures the lattice results radically deviate from the HRG model predictions.

Here [15] we focus on charges associated with the net number of up, down and strange quarks:

Nq ≡ d3x nq(x) with nq(x) = q¯(x)γ0q(x), q = u,d,s (11)

Each quark can be in one of the Nc color states. This means that the conserved flavor charges Nq, scale as Nc1. The key point is that the fluctuations of quark number densities scale as Nc1 above chiral crossover and that in the stringy fluid phase at large Nc, they would be expected to differ from their vacuum and hadron gas values (of order Nc0) by Nc.

In Fig. 5 we show typical results for fluctuations of quark numbers of u,d quarks taken from Ref. [14] and their comparison with the hadron resonance gas model. We see that the fluctuations of the quark numbers deviate from the HRG just at the chiral restoration temperature 155 MeV.

- 0

- 0.5

- 1


- 1.5

- 2


χU4

243x8 323x10 403x12 483x16

| | |
|---|---|
| | |
| | |


4stout (W-B) HRG

T [MeV]

120 130 140 150 160 170 180 190 200 210 220

P3 N

τ = 6

Nτ = 8 Nτ = 10 Nτ = 12

0.8

0.6

0.4

0.2

0.0

100 200 300 400 500 600 700 T [MeV]

- Fig.5. Left:Fluctuations of conserved net u,d quark numbers in 2+1 QCD at physical quark masses. Source: From Ref. [14]. Right: Temperature evolution of the properly renormalized Polyakov loop in 2+1 QCD at physical quark masses. Source: From Ref. [19]


Since the quark numbers scale as Nc1 the above behavior of fluctuations of conserved charges is consistent with the crossover from the hadron gas to the stringy fluid regime, where all main thermodynamical quantities scale as Nc1 (it will be discussed in the next section). To demonstrate a transition to the QGP regime one needs an observable that is sensitive to presence of ∼ Nc2 deconfined gluons. A natural observable of this kind is Polyakov loop.

The expectation value of the Polyakov loop in a pure glue theory is the order parameter for ZNc center symmetry and for confinement. In the center symmetric confining phase the expectation value of the Polyakov loop identically vanishes while above the first order deconfinement phase transition at Td ∼ 270 − 300 MeV the center symmetry gets spontaneously broken and the expectation value of the Polyakov loop jumps to 0.5-0.6. An important issue is that the Polyakov loop in the deconfined phase, where it is not zero, is explicitly sensitive to Nc2 − 1 gluons. Confining properties of QCD with light quarks and of pure Yang-Mills theory are identical in the large Nc limit. Then one expects a similar deconfinement temperature in QCD with light quarks at large Nc.

In the real world Nc = 3 in QCD with light quarks the center symmetry of the action is explicitly broken by quark loops and the deconfinement

first order phase transition is replaced by a very smooth crossover. The renormalized Polyakov loop informs us about the deconfinement crossover region. The temperature evolution of the properly renormalized Polyakov loop, taken from Ref. [19], is shown in Fig. 5. We observe that indeed the deconfinement crossover is nothing else but a smeared broad transition around Td ∼ 300 MeV. Above the chiral restoration temperature around Tch ∼ 155 MeV the Polyakov loop is very small which suggests that here QCD is in the confining regime. At the same time at these temperatures fluctuations of conserved charges demonstrate that the hadron gas picture does not work. Both these facts are consistent with the crossover from the hadron gas to the stringy fluid. The Polyakov loop reaches the value around 0.5 at a temperature roughly 400−500 MeV, in agreement with the temperature of smooth disappearance of the chiral spin symmetry.

### 6. Large Nc QCD phase diagram at µB = 0

In previous sections we have demonstrated numerous lattice evidences that upon increasing temperature there are three qualitatively different regimes in QCD that are connected by smooth crossovers: a hadron gas below T ∼ 155 MeV, an intermediate stringy fluid regime at 155 < T <∼ 500 MeV and a quark-gluon plasma at higher temperatures. These regimes reflect different approximate symmetries and effective degrees of freedom. In the hadron gas the degrees of freedom are well separated hadrons and chiral symmetry is spontaneously broken. In the stringy fluid chiral symmetry is restored and approximate chiral spin symmetry emerges, which is a symmetry of confining interaction. One could view this medium as a densely packed system of the color-singlet clusters. The quark interchanges between clusters required by Pauli principle should be significant. Still it is a system with confinement. The QGP matter at high temperatures consists of decofined quark and gluon quasiparticles.

The large Nc limit of QCD with massless quarks should clarify issues since in this case QCD with light quarks is manifestly center symmetric. This allows one to define unambiguously possible phases with confinement or deconfinement and with spontaneously broken or restored chiral symmetry. Standard large Nc analysis [16] suggests that three regimes at Nc = 3 and small but nonzero quark masses might become distinct phases separated by phase transitions with different scaling of main thermodynamical quantities: energy density ϵ, pressure P and entropy density s:

ϵHG ∼ Nc0 , PHG ∼ Nc0 , sHG ∼ Nc0 , (12)

ϵstr ∼ Nc1 , Pstr ∼ Nc1 , sstr ∼ Nc1 , (13)

ϵQGP ∼ Nc2 , PQGP ∼ Nc2 , sQGP ∼ Nc2 . (14)

A peculiar feature of the intermediate phase is that it should contain a gas of noninteracting glueballs, as in the hadron gas, while the degrees of freedom containing quarks are radically changed. Lattice large Nc studies could clarify this picture.

It is known that the deconfinement temperature in pure Yang-Mills theory is practically Nc-independent [17]. At the same time confining properties of QCD with light quarks are identical with those in Yang-Mills at infinite Nc. Then one expects a deconfinement temperature in large Nc QCD with light quarks to be around Td ∼ 300 MeV. It is also found on the lattice that at T = 0 the quark condensate scales practically exactly as Nc1 and the 1/Nc corrections are negligibly small [18]. This strongly suggests that the physics of chiral symmetry breaking in QCD at Nc = 3 and at large Nc is the same. Then one expects a chiral restoration phase transition in large Nc QCD around the same temperature as at Nc = 3. The latter temperature was established to be around Tch ∼ 130 MeV [20]. If correct, one anticipates two different phase transitions at large Nc, as was discussed above.

### 7. Outlook

The next important step to clarify the QCD phase diagram would be to perform lattice measurements of the chiral restoration temperature at large Nc. It is important to stress that the chiral and large Nc limits do not commute and a proper sequence of limits should be taken. First the large Nc limit and then the chiral limit. This sequence of limits significantly simplifies the numerical problem. As the first step the pure glue (quenched) configurations should be generated at large Nc. There are two strategies of doing this. The first strategy would be to employ gluonic ensembles at large volumes at reasonably large Nc ∼ 10 − 20 as was done in Ref. [17]. Then the eigenvalue problem for the Dirac operator should be solved to determine the quark condensate via the Banks-Casher relation. Upon increasing temperature the temperature of the chiral restoration phase transition could be obtained. The alternative strategy would be to follow the Eguchi-Kawai volume independence to address the problem at very large Nc but in a not large volume, as was done in Ref. [18]. The results for chiral restoration temperatures should give in principle the same answer in both approaches.

REFERENCES

- [1] L. Y. Glozman, Eur. Phys. J. A 51 (2015) no.3, 27 doi:10.1140/epja/i201515027-x [arXiv:1407.2798 [hep-ph]].
- [2] L. Y. Glozman and M. Pak, Phys. Rev. D 92 (2015) no.1, 016001 doi:10.1103/PhysRevD.92.016001 [arXiv:1504.02323 [hep-lat]].
- [3] L. Y. Glozman, Prog. Part. Nucl. Phys. 131 (2023), 104049 doi:10.1016/j.ppnp.2023.104049 [arXiv:2209.10235 [hep-lat]].
- [4] C. Rohrhofer, Y. Aoki, G. Cossu, H. Fukaya, C. Gattringer, L. Y. Glozman, S. Hashimoto, C. B. Lang and S. Prelovsek, Phys. Rev. D 100 (2019) no.1, 014502 doi:10.1103/PhysRevD.100.014502 [arXiv:1902.03191 [hep-lat]].
- [5] C. Rohrhofer, Y. Aoki, L. Y. Glozman and S. Hashimoto, Phys. Lett. B 802

(2020), 135245 doi:10.1016/j.physletb.2020.135245 [arXiv:1909.00927 [hep-lat]].

- [6] T. W. Chiu, Phys. Rev. D 107 (2023) no.11, 114501 doi:10.1103/PhysRevD.107.114501 [arXiv:2302.06073 [hep-lat]].
- [7] M. Dalla Brida, L. Giusti, T. Harris, D. Laudicina and M. Pepe, JHEP 04

(2022), 034 doi:10.1007/JHEP04(2022)034 [arXiv:2112.05427 [hep-lat]].

- [8] A. Bazavov, S. Dentinger, H. T. Ding, P. Hegde, O. Kaczmarek, F. Karsch, E. Laermann, A. Lahiri, S. Mukherjee and H. Ohno, et al. Phys. Rev. D 100

(2019) no.9, 094510 doi:10.1103/PhysRevD.100.094510 [arXiv:1908.09552 [heplat]].

- [9] A. Bazavov, P. Petreczky and J. H. Weber, Phys. Rev. D 97 (2018) no.1, 014510 doi:10.1103/PhysRevD.97.014510 [arXiv:1710.05024 [hep-lat]].
- [10] L. Y. Glozman, O. Philipsen and R. D. Pisarski, Eur. Phys. J. A 58 (2022) no.12, 247 doi:10.1140/epja/s10050-022-00895-4 [arXiv:2204.05083 [hep-ph]].
- [11] J. Bros and D. Buchholz, Z. Phys. C 55 (1992), 509-514 doi:10.1007/BF01565114
- [12] P. Lowdon and O. Philipsen, “Pion spectral properties above the chiral crossover of QCD,” JHEP 10 (2022), 161 doi:10.1007/JHEP10(2022)161 [arXiv:2207.14718 [hep-lat]].
- [13] D. Bala, O. Kaczmarek, P. Lowdon, O. Philipsen and T. Ueding, [arXiv:2310.13476 [hep-lat]].
- [14] R. Bellwied, S. Borsanyi, Z. Fodor, S. D. Katz, A. Pasztor, C. Ratti and K. K. Szabo, Phys. Rev. D 92 (2015) no.11, 114505 doi:10.1103/PhysRevD.92.114505 [arXiv:1507.04627 [hep-lat]].
- [15] T. D. Cohen and L. Y. Glozman, [arXiv:2401.04194 [hep-ph]].
- [16] T. D. Cohen and L. Y. Glozman, [arXiv:2311.07333 [hep-ph]].
- [17] B. Lucini and M. Panero, Phys. Rept. 526 (2013), 93-163 doi:10.1016/j.physrep.2013.01.001 [arXiv:1210.4997 [hep-th]].
- [18] C. Bonanno, P. Butti, M. Garcı´a Pere´z, A. Gonz´lez-Arroyo, K. I. Ishikawa and M. Okawa, [arXiv:2309.15540 [hep-lat]].
- [19] P. Petreczky and H. P. Schadler, Phys. Rev. D 92 (2015) no.9, 094517 doi:10.1103/PhysRevD.92.094517 [arXiv:1509.07874 [hep-lat]].
- [20] H. T. Ding et al. [HotQCD], Phys. Rev. Lett. 123 (2019) no.6, 062002 doi:10.1103/PhysRevLett.123.062002 [arXiv:1903.04801 [hep-lat]].


