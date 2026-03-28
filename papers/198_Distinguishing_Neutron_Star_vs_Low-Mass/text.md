## arXiv:2507.15951v2[hep-ph]7 Aug 2025

Prepared for submission to JCAP

TIFR/TH/25-10

# Distinguishing Neutron Star vs. Low-Mass Black Hole Binaries with Late Inspiral & Postmerger Gravitational Waves — Sensitivity to Transmuted Black Holes and Non-Annihilating Dark Matter

ID b and Basudeb Dasgupta

ID a Shasvath Kapadia,

Sulagna Bhattacharya,

ID a

- a Tata Institute of Fundamental Research, Homi Bhabha Road, Mumbai 400005, India
- b Inter University Center for Astronomy and Astrophysics, Post Bag 4, Ganeshkhind, Pune 411007, India E-mail: sulagna@theory.tifr.res.in, shasvath.kapadia@iucaa.in, bdasgupta@theory.tifr.res.in


Abstract. The astrophysical origin of observed low-mass compact binary coalescences in the 1 − 2.5M⊙ range remains ambiguous. Both binary neutron star (BNS) and binary low-mass black hole (LMBH) mergers produce nearly identical inspiral waveforms, and electromagnetic follow-up is not always possible. Distinguishing between these scenarios therefore presents a key challenge. We demonstrate that waveform differences in the late-inspiral to postmerger epochs create significant mismatches that will be detectable by planned detectors, viz., NEMO, Cosmic Explorer, and Einstein Telescope, while the currently operational LIGO A+ will be effective only for nearby sources. These differences are enhanced for stiffer equations of state. We show how the redshift-dependent compact binary merger rate inferred from gravitational wave observations can be parsed into BNS and LMBH components, accounting for misclassification probability. We forecast model-independent 90% exclusion sensitivities for the LMBH fraction. Interpreting these LMBHs as dark matter capture-induced transmuted black holes, we convert exclusion sensitivities into projected exclusion bounds on heavy non-annihilating dark matter. Our results illustrate how gravitational wave measurements can disentangle compact object populations and provide new insights into particle dark matter interactions.

Keywords: Gravitational Waves, Low-Mass Black Hole, Binary Neutron Star, DarkMatter

### Contents

- 1 Introduction 1
- 2 Inputs: LMBH & BNS Waveforms and Benchmarks 4

- 2.1 LMBH Waveforms from PyCBC 4
- 2.2 BNS Waveforms from CoRe Database & Choice of EoSs 5
- 2.3 Benchmark Parameters 8


- 3 Methods: Distinguishability of LMBH & BNS Mergers 8

- 3.1 Fitting Factor & Bayes Factor 8
- 3.2 Projected Sensitivity of Planned Detectors 12

- 3.2.1 Advanced LIGO 13
- 3.2.2 NEMO 13
- 3.2.3 Cosmic Explorer 15
- 3.2.4 Einstein Telescope 15


- 3.3 Dependence on Luminosity Distance 16


- 4 Results: Constraints on Transmutation & Particle DM 17

- 4.1 Model-Independent Results on Transmutation 17

- 4.1.1 Parsing the CBC Rate into BNS & LMBH Rates 17
- 4.1.2 Exclusion Sensitivity for Transmutation Fraction 18


- 4.2 Exclusion Sensitivity for DM-Nucleon Interaction 21


- 5 Discussions & Conclusion 23 A Appendices 25


- A.1 Data Extraction from CoRe Database 25
- A.2 Exposure of the GW Detectors 27
- A.3 Projected Exclusion Significance 28


### 1 Introduction

Gravitational wave (GW) [1] observations of compact binary mergers provide key insights into strong-field gravity and relativistic astrophysics. GW170817[2], the first observed binary neutron star (BNS) merger, enabled multimessenger astronomy by linking gravitational waves to electromagnetic counterparts. GW150914[3], the first detected binary black hole (BBH) merger, confirmed the existence of stellar-mass black hole (BH) binaries and provided a new way to study general relativity.

During the O3a+b observing runs, the LIGO-Virgo-KAGRA (LVK) Collaboration[4] has reported a number of compact binary coalescence (CBC) events with component masses that resist clear classification as either neutron stars (NSs) or low-mass black holes (LMBHs). Examples include GW190425[5], GW190814[6], GW230529[7],

and SSM200308[8], where at least one of the components is either in the lower massgap region, viz. 2.5 − 5M⊙, or even lighter[9–11]. Such LMBHs are not expected as a product of standard stellar evolution, and thus the current practice is to provisionally classify CBCs as NSs or BHs using the inferred mass. Nevertheless, such a classification lacks robustness, and a more comprehensive approach is warranted.

In this paper, we therefore ask the question — Can we distinguish BNSs and LMBHs? This is motivated from two complementary viewpoints. Firstly, from an astrophysical/observational standpoint, it is desirable to classify a low-mass CBC as a BNS or an LMBH (we assume that these are the only two possibilities). This is important in order to obtain unbiased inferences on the NS population and merger rates. Secondly, from a fundamental physics perspective, the potential existence of these exotic LMBHs offers novel avenues to discover new physics[12–15].

A specific possibility involves dark matter (DM)[16, 17], which constitutes 27% of the Universe’s energy content. Despite its ubiquity, its particle identity remains elusive — with its mass uncertain within a huge range (10−22 − 1066 eV)[18] and no confirmed non-gravitational interactions. Non-annihilating DM particles, e.g., with masses in the range 102 − 107 GeV for bosons, are capable of producing LMBH mergers that mimic BNS signals. Galactic DM with non-gravitational nucleon interactions can be captured by NSs over their lifetimes[14, 16, 19–29]. Once captured, heavy DM can accumulate in the NS core, forming a dense dark core that may become gravitationally unstable and collapse into a microscopic BH. This BH can eventually consume the entire NS, ejecting ∼ 10−3 − 10−4 M⊙ [30], and forming an LMBH of comparable mass[14, 22, 23, 31–34]. Thus, a BNS system can evolve into an LMBH–LMBH system via DM-induced collapse. Such mergers should, in principle, be detectable by current GW instruments. Their apparent absence places constraints on DM mass and nucleon cross-sections[28], though these are tentative since the LVK collaboration classifies all compact objects below 2.5M⊙ as NSs[35]. Developing robust methods to identify such objects is therefore essential. Apart from this scenario, GW observations have been used to study DM-admixed binary neutron star mergers [36, 37], infer DMinduced modifications to NS oscillation modes [38, 39], and probe DM density spikes around massive black holes using extreme mass ratio inspirals (EMRIs) [40–43]. In addition, GW observations have also shed light on possible nature of DM by probing dark photons as DM[44], ultralight scalars[45], non-annihilating DM[28, 46, 47], compact DM[48–51], and self-interacting DM[52, 53], among others. It has been well established that GW observations can serve as a nobel probe of DM [54], complementing traditional direct, indirect and collider-based searches.

Previous work on distinguishing BNSs and LMBH mergers has considered the potential of multi-messenger detection. As in the case of GW170817[2], non-gravitational signals would provide clear evidence against LMBHs. However, it is estimated that most of the CBC detections at current and future GW detectors will not be adequately followed up by electromagnetic and neutrino searches[55–57]. This has to do with the limited sky coverage and/or angular resolution of the relevant telescopes, as well as imperfect localization of the GW sources.

In the absence of an electromagnetic or neutrino counterparts, it is challenging to distinguish a BNS merger from an LMBH merger, as the current GW observations primarily capture the inspiral phase, where the waveforms of these systems are nearly identical. This degeneracy becomes especially relevant for merger events with component masses in the 2−5M⊙ range. One promising approach involves measuring tidal effects during the inspiral. Neutron stars, being extended objects with internal structure, exhibit non-zero tidal deformability; whereas black holes, being point-like singularities without internal structure, have zero tidal polarizability. Accurate inference of the tidal parameters in the waveform thus offers a potential diagnostic to distinguish BNS from LMBH mergers[47]. Recent studies have explored this avenue[58–67], although such analyses require higher order post-Newtonian corrections (up to 5PN), adding significant computational complexity. Further, these tidal effects during the inspiral are subtle and typically do not offer any robust qualitative features, independent of the neutron star equation of state (EoS) that remains uncertain due to possible exotic matter at supranuclear densities [68, 69]. Thus, reliable extraction of tidal signatures demands favorable observational conditions: short luminosity distances, long inspiral durations with high signal-to-noise ratios (SNRs), and enhanced detector sensitivity at high frequencies (up to 3−4kHz), since the merger frequencies for 1M⊙-1M⊙ systems are approximately 2kHz[70].

To address the question posed at the beginning, in this paper we systematically investigate the similarity between GW waveforms from equal-mass LMBH–LMBH and BNS–BNS mergers, by comparing LMBH-LMBH mergers waveforms from numerical relativity simulations of the late-inspiral and postmerger epochs. We compute the Fitting Factors and Bayes Factors between these waveforms and identify the conditions under which they can be distinguished. To evaluate observational prospects, we analyze the sensitivity of both current and future GW detectors, viz., LIGO A+[71], NEMO[72], CE[73], and ET[74]. The main outcome of these studies is an estimate of the efficiency of correctly classifying a CBC as a BNS or an LMBH. We use this efficiency factor to estimate the most probable BNS and LMBH fraction in the CBC event rate, as well as to obtain exclusion sensitivity for the fraction of CBCs that could be LMBHs. Finally, we explore a physically motivated model for formation of LMBHs, via transmutation of NSs into similar mass BHs due to capture of heavy nonannihilating DM particles, and compute exclusion sensitivity to the DM mass mχ and its interaction cross section σχn with nucleons.

The paper is organized as follows: In Sec.2, we introduce the benchmark waveforms of LMBH-LMBH and NS-NS mergers using the PyCBC and CoRe simulation frameworks. Sec.3 presents the computation of the Fitting Factors and Bayes Factors, its dependence on EoSs, detector characteristics, and the source luminosity distance. In Sec.4, we present the results on BNS and LMBH merger rates and on DM parameters, and conclude in Sec.5 with a brief summary and outlook.

DL = 1Mpc

10−21

˜Strainh(f)[sec]

10−22

10−23

- (1+1)M

(1.35+1.35)M

- (2+2)M


10−24

102 103 104

Frequency f[Hz]

- Figure 1: LMBH binary waveform, strain h˜(f) vs. frequency (f), generated by IMRPhenomD[75, 76] with total masses 2M⊙, 2.7M⊙, and 4M⊙ respectively, with vanishing spin components, and with DL =1 Mpc. The strain falls as ∝ f−7/6 during the inspiral and scales as ∝ Mc5/6, as shown in Eq.2.1.


### 2 Inputs: LMBH & BNS Waveforms and Benchmarks

#### 2.1 LMBH Waveforms from PyCBC

Low-mass black holes have become a new avenue to look for the BSM physics through gravitational wave observations. In this section we will introduce the waveform of a LMBH merger, irrespective of its origin and evolution. We consider two nonspinning LMBHs with equal masses, m1 = m2 = 1.35M⊙, for which the chirp mass is Mc = µ3/5 M2/5 = 1.17M⊙, where µ ≡ m1m2/(m1+m2) is the reduced mass of the system and M ≡ (m1 + m2) is the total mass of the system. The ‘plus’ (+) and ‘cross’(×) polarized strain amplitudes for the (l = 2,m = 2)-mode can be found as[70],

h˜+(f) =

h˜×(f) =

5 24

5 24

1/2 1 π2/3

1 DL

1/2 1 π2/3

1 DL

+(f) 1 + cos2 ι 2

(GMc)5/6 f−7/6eiΨ

,

(GMc)5/6 f−7/6eiΨ×(f) cosι, (2.1)

where G is the gravitational constant, DL is the luminosity distance, Mc is the detectorframe chirp mass given by (1 + z)Mc|source rest frame. The redshift z can be assumed to be 0 for current observations so far. The inclination of the perpendicular to the orbital plane with respect to the line of sight is given as ι. If ι = π/2, the dominant strain amplitude is reduced by a factor of 1/2 and h× vanishes, resulting in a linearly polarized

wave; this orientation is termed as ‘edge-on’. For ι = 0&π, the system’s orbital angular momentum is aligned with the line of sight and this is termed as a ‘face-on’ orientation, resulting in a circularly polarized wave. For a face-on symmetric (m1 = m2) LMBH binary at DL =1 Mpc (with vanishing spins and m1 = m2 = 1.35M⊙), the strain amplitude will be

h˜(f) ≈ 4.2 × 10−22 sec

Mpc DL

Mc 1.17M⊙

5/6 f 100Hz

−7/6

. (2.2)

This waveform is valid up to a maximum frequency, termed as the frequency of innermost stable circular orbit (ISCO), given by

c3 GM ≈ 2.2kHz

1 6√6(2π)

fISCO =

M⊙ M

. (2.3)

Beyond the ISCO, the inspiral phase ends and the binary undergoes a rapid plunge, marking the onset of the merger phase, which is followed by a damped sinusoidal ringdown[77, 78] as the remnant approaches equilibrium.

To generate the LMBH waveforms we use the publicly available software PyCBC[79]. We employ its time domain and frequency domain module named IMRPhenomD[75, 76], which is a phenomenological model of GW signal from the inspiralmerger-ringdown of non-precessing (aligned spin) black hole binaries. These waveforms are generated using numerical relativity (NR) simulations and cover the entire coalescence, including the strong gravity regimes of merger and ringdown unlike the waveforms generated using perturbative expansion in v/c, where v is the orbital velocity and c is the speed of light. We show symmetric LMBH binary frequency domain waveforms in Fig.1 with the total masses 2M⊙, 2.7M⊙, and 4M⊙ respectively. These assume non-spinning BHs and starts with a frequency of 40Hz with frequency steps (∆f) of 0.125 Hz, with DL = 1Mpc.

#### 2.2 BNS Waveforms from CoRe Database & Choice of EoSs

Binary neutron star mergers, observed through gravitational waves and electromagnetic signals, provide key insights into multi-messenger and particle astrophysics, as confirmed by GW170817[2]. Whereas, events like GW190425[5] and GW190814[6] open a new window for exotic physics and constrain the NS EoSs.

The Computational Relativity (CoRe) database[80] compiles multi-messenger observations of these events, enabling precise studies of their properties and dynamics. In this section we will explain how we used this database to generate several BNS waveforms for different EoSs. We have focused on symmetric m1 = m2 = 1.35M⊙ BNS systems, mimicking the observed Galactic binary neutron star mass distribution that is approximately a Gaussian between 1.08−1.57M⊙, with a mean at 1.35M⊙ [81]. When components of the BNS mergers are far apart, their dynamics can be approximated using point-particle methods similar to BBHs. However, in the strong-gravity regime near merger and post-merger, non-linear hydrodynamics, neutrino transport, magnetic fields, and dense nuclear microphysics become essential to accurately model

tidal interactions, matter ejection, and the neutron star EoS, necessitating fully numerical relativistic simulations[82–86].

CoRe provides a diverse set of GW templates to constrain the neutron star equation of state, and to analyze merger dynamics and remnant properties. The first release of CoRe[87] comprised 367 waveforms derived from numerical simulations adhering to general relativity principles and, 164 distinct setups, varying parameters such as total binary mass, mass ratio, initial separation, eccentricity, and stellar spins. The second release[88] included 254 distinct BNS configurations, resulting in a total of 590 numerical-relativity simulations performed at various grid resolutions. These simulations encompass a wide range of possibilities with 18 different EoSs and, with a wide range of parameters. These simulations are executed with two independent mesh-based methods: BAM[89, 90] and THC[91]. BAM is better adapted to treat the NS surface, multiple orbits in the inspiral, followed by the merger and post-merger. Whereas THC is preferentially used to address the microphysics of the NS, as it contains different neutrino transport schemes, different mixing and dissipation mechanisms during the merger. For this work, we chose 6 EoSs from BAM simulations and 2 from THC simulations. The absolute value of the strain amplitude is more important for our study, than the phase evolution associated with the detailed microphysics.

The model parameters of this simulation are the masses of the component NSs, m1 and m2, and the effective spin parameter,

m1χ1 + m2χ2 M

, (2.4)

χeff =

where χi for ith NS represents the spin component aligned with the angular momentum vector, and M = m1 + m2 is the total binary mass. The tidal coupling constant and the reduced tidal parameters[92, 93] are defined as

κT2 = 3ν

16 13

Λ =˜

m1 M

m2 M

3

Λ1 +

(m1 + 12m2)m41Λ1 M5

3

Λ2 ,

(m2 + 12m1)m42Λ2 M5

+

, (2.5)

where ν = m1m2/M2 is called the symmetric mass ratio. For m1 = m2 = m it is 1/4. Λi = 23κ2,iCi−5 is the tidal polarizability parameter for the ith NS, where κ2,i & Ci are the gravito-electric Love number and compactness of the ith NS respectively. With these inputs, the radiated gravitational wave decomposed in (l,m) multipoles is

∞

h+ − ih× = DL−1

l=2

l

hlm(t)−2Ylm(ι,ϕ), (2.6)

m=−l

where −2Ylm are the s = −2 spin-weighted spherical harmonics[70]. The inclination and orbital phase, ι and ϕ, respectively, give the inclination of the perpendicular to the orbital plane with respect to the line of sight, and the orbital phase of the binary at a particular time.

10−22

|DL = 1Mpc<br><br>2H<br><br>MS1b<br><br>H4<br><br>BHBΛφ<br><br>ALF2 LS220 SLy<br><br>2B|
|---|


10−23

˜Strainh(f)[sec]

10−24

10−25

10−26

500 1000 1500 2000 2500 3000 3500 4000

Frequency f[Hz]

- Figure 2: Frequency domain waveforms of 1.35M⊙ − 1.35M⊙ BNS mergers, with non-spinning components, for the EoSs described in Table 2. The key feature is the postmerger second peak which may furnish a way to distinguish BNS from LMBHs.


CoRe simulations use 18 different EoS models, including finite temperature EoS in the first release. BAM simulations are performed with analytical EoS in the form

P (ρ,ϵ) = Ppwp (ρ) + (γth − 1)ρ(ϵ − ϵpwp) , (2.7)

where Ppwp(ρ) is a given piecewise polytropic EoS model[94]. The specific parameters employed for the piecewise polytropic EoS are available on the CoRe website[80] and they mimic the zero temperature EoS models described in[94]. Fig.1 of Ref.[88] shows the mNS −RNS diagram and the Λ−mNS diagram of these EoS models, which gives an overview of the current parameter space of EoS models. For a given mass, M = 1.4M⊙, the EoS 2H furnishes the largest radius RTOV ≈15.21 km, and EoS 2B the smallest ≈9.75 km[88, 95]. Evidently 2H is the stiffest (high pressure for a given density) and

- 2B is the softest (lower pressure for a given density) EoS as used in this database. The larger (smaller) values of tidal polarizability parameter Λ correspond to stiffer (softer) EoSs, resulting in long-lived remnant (prompt collapse) in the post-merger. In the following section, we outline the benchmark parameters adopted for this analysis and specify the set of EoSs selected for our study.


The extraction of BNS waveforms from this database is discussed in detail (with the file structure and nomenclature) in the Appendix A.1. This data is in time-domain, and a Fourier transform gives the waveform in frequency domain. A sample of BNS waveforms from CoRe is shown in Fig.2. They exhibit qualitative differences from that of a LMBH binary, primarily due to the matter effects. Depending on the EoS, the

BNS merger remnant may result in a hypermassive NS that subsequently collapses to a BH, or undergo a prompt collapse. This behavior typically produces a characteristic second peak in the postmerger spectrum. Note the second peak seen for all the EoSs, at f ≲ 4kHz, except for 2B which is in tension with NS mass-radius data[88].

#### 2.3 Benchmark Parameters

We now summarize the fiducial parameters used throughout our analysis. These include the intrinsic source properties, the NS EoSs adopted for BNS mergers, and the assumed source DL for different detector configurations.

Table 1 lists the intrinsic parameters used for both LMBH and BNS systems. In both cases, we consider equal-mass binaries with component masses m1 = m2 = 1.35M⊙ and vanishing dimensionless spin parameters χ1 = χ2 = 0. For this study we have chosen eight EoSs, and generated the waveform in frequency domain. We use 6 BAM waveforms (2H, MS1b, H4, ALF2[96], SLy, 2B) with zero-temperature EoSs and 2 finite-temperature EoSs (BHBΛϕ[97], LS220[98]) for our study. We list them in Table 2 from stiffer to softer models[88, 99], along with their tidal coupling constant and the reduced tidal parameter (see Eq.2.5), with their CoRe IDs alongside. Finally, Table 3 summarizes the source luminosity distances DL, for each GW detector considered; LIGO A+[71], NEMO[72], CE[73], and ET[74]. These distances are chosen based on the detector sensitivities (see Fig.4), such that the norm remains significant for detection.

System Component Masses Dimensionless Spins LMBH–LMBH m1 = m2 = 1.35M⊙ χ1 = χ2 = 0

BNS–BNS m1 = m2 = 1.35M⊙ χ1 = χ2 = 0

- Table 1: Benchmark intrinsic parameters used in this study for LMBH and BNS systems. All sources are assumed to be equal-mass, non-spinning binaries.


### 3 Methods: Distinguishability of LMBH & BNS Mergers

#### 3.1 Fitting Factor & Bayes Factor

The Neyman-Pearson lemma provides that matched filtering is the optimal method to search for GW signals of known shape in the detector data[102]. The detector signal is modeled as a time-series, s(t) = h(t) + n(t), where h(t) is the signal strain and n(t) is the noise in the detector, which is cross-correlated with a template to generate signal to noise ratio (SNR) statistics of a particular event[70, 103]. The optimal SNR (for this case the norm) for a specific frequency range is[103],

|h˜(f)|2 Sn(f)

fmax

df ≡ norm(h), (3.1)

ρopt = 4

fmin

EoS CoRe ID κT2 Λ˜ fmerge in Hz

2H BAM:0002 436 2325 1230 MS1b BAM:0065 287 1531 1407

H4 BAM:0035 208 1111 1554

BHBΛϕ THC:0003 159 848 1677 ALF2 BAM:0003 137 733 1743 LS220 THC:0019 128 684 1774

SLy BAM:0098 73 390 2001 2B BAM:0001 24 127 2298

- Table 2: The EoSs, considered for this study, with their CoRe IDs. The reduced

tidal parameters κT2 & Λ˜ are also provided (Eq.2.5). The last column gives the merger frequencies[99–101] for different EoSs, that separate the inspiral & postmerger phases.

Detector Source Luminosity Distance [Mpc] LIGO A+ 100

NEMO 300

Cosmic Explorer (CE) 350 Einstein Telescope (ET) 350

- Table 3: Benchmark source luminosity distance for each detector configuration analyzed in this work (see Fig.4).


where h˜(f) is the Fourier transform (frequency domain) of the time domain data h(t), which is basically the linear combination of two GW polarizations. Sn(f) is the onesided power spectral density (PSD) of the detector[70],

- 1

- 2


′

′

⟨n˜(f)˜n∗(f

δ(f − f

)⟩ =

)Sn(f). (3.2)

In reality, there remains some mismatch between the template hT and the detector data, which can be further analyzed to infer the parameter values and errors associated with each of them. If the noise is stationary and Gaussian the likelihood is[104],

- 1

- 2⟨s−hT(θ)|s−hT(θ)⟩ , (3.3)


L = p(s|θ⃗) ∝ e− where θ⃗ are the model parameters with which the template has been constructed, and

- s is the signal received. The notation ⟨.|.⟩ denotes the noise weighted inner product given by[104, 105]


⟨h1|h2⟩ = 2

1(f)h˜2(f) + h˜2∗(f)h˜1(f) Sn(f)

h˜∗

fmax

df

, (3.4)

fmin

with fmin &fmax being the minimum and maximum of the frequency over which the inner product is evaluated. This frequency range is discussed later in the context of the problem’s requirement.

- 0.95
- 1

MMatch()

LIGO A+

|LIGO A+ (postmerger)<br><br>H4<br><br>BHBΛφ<br><br>LS220<br><br>SLy<br><br>2B|
|---|


2.0 2.5 3.0 3.5 4.0 4.5 5.0

Total Mass M (M )

0.6

0.65

0.7

0.75

0.8

0.85

0.9

- 0.95
- 1


MMatch()

2H

MS1b

ALF2

|(Inspiral + Postmerger)|
|---|


2.0 2.5 3.0 3.5 4.0 4.5 5.0

Total Mass M (M )

0.7

0.75

0.8

0.85

0.9

- 0.95
- 1


MMatch()

LIGO A+

|NEMO (Inspiral)|
|---|


- 2.0 2.5 3.0 3.5 4.0 4.5 5.0 Total Mass M (M )


|(Inspiral)|
|---|


0.9

0.85

0.8

0.75

0.7

2.0 2.5 3.0 3.5 4.0 4.5 5.0

Total Mass M (M )

- 0.95
- 1

MMatch()

|NEMO (postmerger)<br><br>2H<br><br>MS1b H4<br><br>BHBΛφ<br><br>2B|
|---|


2.0 2.5 3.0 3.5 4.0 4.5 5.0

Total Mass M (M )

0.6

0.65

0.7

0.75

0.8

0.85

0.9

- 0.95
- 1


MMatch()

ALF2

LS220

SLy

|NEMO (Inspiral + Postmerger)|
|---|


2.0 2.5 3.0 3.5 4.0 4.5 5.0

Total Mass M (M )

0.8

0.85

0.9

- 0.95
- 1


MMatch()

|(Inspiral)|
|---|


- 2.0 2.5 3.0 3.5 4.0 4.5 5.0 Total Mass M (M )


0.9

0.85

- 0.95
- 1

MMatch()

CE

|CE (postmerger)<br><br>MS1b<br><br>H4<br><br>BHBΛφ<br><br>ALF2<br><br>LS220<br><br>SLy<br><br>2B|
|---|


2.0 2.5 3.0 3.5 4.0 4.5 5.0

Total Mass M (M )

0.6

0.65

0.7

0.75

0.8

0.85

0.9

- 0.95
- 1


MMatch()

2H

|Postmerger)|
|---|


2.0 2.5 3.0 3.5 4.0 4.5 5.0

Total Mass M (M )

0.7

0.75

0.8

0.85

0.9

- 0.95
- 1


MMatch()

CE (Inspiral +

|(Inspiral)|
|---|


- 2.0 2.5 3.0 3.5 4.0 4.5 5.0 Total Mass M (M )


0.9

0.85

0.8

0.75

0.7

- 0.95
- 1


MMatch()

0.9

0.85

0.8

0.75

###### ET

0.7

- 0.95
- 1


|ET (postmerger)<br><br>2H<br><br>MS1b<br><br>H4<br><br>BHBΛφ<br><br>ALF2<br><br>LS220<br><br>SLy<br><br>2B|
|---|


0.9

MMatch()

0.85

0.8

0.75

0.7

0.65

0.6

2.0 2.5 3.0 3.5 4.0 4.5 5.0

Total Mass M (M )

- 0.95
- 1


|Postmerger)|
|---|


MMatch()

0.9

0.85

0.8

0.75

ET (Inspiral +

0.7

2.0 2.5 3.0 3.5 4.0 4.5 5.0

Total Mass M (M )

- Figure 3: The match M between BNS & LMBH mergers is shown as a function of total mass M for various EoSs, with each row corresponding to a different detector: LIGO A+, NEMO, CE, and ET respectively (sensitivities in Fig.4). Left panels show the inspiral-only case, where M remains high and weakly dependent on M. Middle panels show postmerger-only results, where matter effects of BNS mergers degrade the match and they exhibit EoS-dependent variations due to shifts in the secondary peak (see Fig.2). Right panels present results over the full frequency range (400 − 5000Hz), where inspiral dominance suppresses postmerger differences in all detectors except NEMO. For our analysis, the Fitting Factor is defined as the maximum match across


M = 2– 5M⊙, using a 1.35M⊙ symmetric BNS waveform as signal and scanning over symmetric LMBH templates by keeping other parameters the same. Each black point denotes a non-spinning, equal-mass (m1 = m2 = 1.35M⊙) comparison. Even for NEMO, this equal-mass match is within a few percent of the FF; for other detectors, FF shows insignificant mass dependence due to inspiral-phase dominance. Softer EoSs typically yield higher matches, with exceptions: BHBΛϕ and LS220. The legend for the EoSs (Table2) is shown in the middle panels. As a normalized inner product, FF remains invariant under extrinsic parameters like the luminosity distance.

Our aim is to see whether, for a fixed signal, an LMBH template is favored over a BNS template or vice versa. This comparison can be performed by calculating the ‘Fitting Factor’ FF between two waveforms h1 (signal) and h2 (template),

M

FF = max

templates

fmax

(h∗1(f)h2(f) + h1(f)h∗2(f)) Sn(f) × ⟨h1(f)|h1(f)⟩ × ⟨h2(f)|h2(f)⟩

. (3.5)

= max

2

df

templates

fmin

This is the match, M = ⟨hˆ1(f)|hˆ2(f)⟩, maximized over intrinsic parameters of the models[105, 106], and typically used to estimate the maximum overlap achievable between an observed signal (say h1) and the best-matching waveform (say h2) within a given template bank. It is normalized, which makes it independent of the extrinsic parameters which affect the norms (for our case, mainly DL). The FF of exactly same waveforms is unity, and any deviation of the template from the signal will lead to smaller FF values, resulting in the SNR loss in the detector,

SNRobserved = FF × SNRopt . (3.6)

- A reduction in FF greater than 0.03 corresponds ≳ 10% loss in the recovered signal amplitude, and hence leads to a significant decrease in the evidential support for the waveform model[107, 108]. The FF is related to the likelihood ratio and can be used for model selection.


The Bayes Factor BF is simply the ratio between two likelihoods, which determines whether hypothesis 1 (H1) is favored over hypothesis2 (H2). In our case, the functional form of BF can be approximated (using a saddle-point argument) in terms of FF between two models and the ρopt (Eq.3.1)[100, 106], as

2 1 opt

- p(H1 |s)

- p(H2 |s)


2)ρ

= e(1−FF

B21 =

2 . (3.7)

Here B21 is the evidence of H1 over H2, given the signal s.

We interpret the BF, computed using the FF between BNS merger (say, H1) and LMBH merger waveforms (H2), for a fixed SNR, as the relative likelihood of each model, given a fixed signal. We take the BNS merger waveform (Fig.2) as a true signal and compare the fit with LMBH merger waveforms (Fig.3), for each different EoSs (listed in Table 2), and the other specifications are described in Sec.2.3. As seen from Figs.1 & 2, at lower frequencies (mostly from the inspiral) these two models have a significant resemblance whereas in the high-frequency regime (dominated by the postmerger) they significantly differ with each other. Depending on the EoS, the tidal effects cause the remnant to either go a prompt collapse (smallerΛ) or live as a stable remnant for some time (largerΛ) which results in a second peak (at different frequencies) in the waveform unlike the sinusoidal decay of the strain in the case of LMBH mergers[109–111]. For our analysis we set the frequency range from 500 − 4000Hz, where 500Hz − fmerge(depending on κT2 , hence EoS) is the inspiral phase and fmerge −4000Hz is the postmerger phase. For existing and proposed detectors we start

|ET<br><br>CE<br><br>NEMO<br><br>LIGO A+<br><br>LMBH<br><br>BNS|
|---|


10−19

DimensionlessSensitivity/Strain

10−20

10−21

10−22

10−23

10−24

10−25

500 1000 1500 2000 2500 3000 3500 4000

Frequency f[Hz]

- Figure 4: Amplitude Spectral Density (ASD) of the detector-noise, considered in this study. Grey lines denote the dimensionless strain amplitudes fh˜(f), for the benchmark BNS merger and LMBH merger, with DL = 1 Mpc. The different detector-noise ASDs are shown as fSn(f) to keep it dimensionless. Sn(f) denotes the one-sided power spectral density of the detector-noise.


losing sensitivity after 4000Hz, resulting in no significant contribution from yet higher frequencies (Fig.4). We use an analytical fit from Ref.[99] to evaluate fmerge using

1 + (1.3067 × 10−3)ζ3199.8 1 + (5.0064 × 10−3)ζ3199.8

Mfmerge = 3.3184 × 10−2

, (3.8)

where ζ3199.8 = κT2 + 3199.8(1 − 4ν), with ν being the symmetric mass ratio. Table 2 shows the merger frequency for the EoSs used, along with their κT2 values.

Since analytically varying all physical parameters for BNS systems is impractical due to the complex microphysical effects and simulation requirements, we restrict our analysis to eight representative EoSs given in Table 2. We report the values in the next subsection for different choices of detectors and explain the trend in the values. Using the FF and ρopt for the true signal chosen as BNS, we then calculate the Bayes Factor BLMBHBNS , Eq.3.7, and comment on the Bayesian evidence in the inspiral and the postmerger part of the signal.

#### 3.2 Projected Sensitivity of Planned Detectors

The LVK collaboration, comprising the 2nd generation, LIGO, Virgo, and KAGRA detectors, has played a foundational role in GW astronomy by enabling the first direct detections of compact binary coalescences and supporting multi-messenger observations[71]. The Neutron Star Extreme Matter Observatory (NEMO), a 2.5 generation

detector, is designed for optimal sensitivity in the high-frequency regime (above∼2kHz), making it ideal for capturing postmerger signatures from NS mergers and probing the EoS at supranuclear densities[72]. The Cosmic Explorer (CE), a 3rd generation detector, aims to achieve ten times the sensitivity of current detectors, expanding the observational horizon to the edge of the observable universe and significantly improving our understanding of GW sources[73, 112]. Similarly the proposed Einstein Telescope(ET), again a 3rd generation European detector, is designed to improve sensitivity by an order of magnitude, thereby extending GW detection to cosmological distances and enhancing our ability to probe early-universe phenomena[74, 113]. Together, these detectors cover a broad frequency spectrum: ET and CE excel in the low-frequency band crucial for tracking inspiral dynamics, while NEMO targets the high-frequency postmerger regime, making this combination particularly powerful for distinguishing between NS-NS and LMBH-LMBH mergers and understanding matter effects in extreme gravity.

In Fig.4 we show the noise sensitivity curve of each of these detectors in the frequency range of our concern. We also show the strain curves for a symmetric BNS and LMBH mergers in dimensionless units. In Table 2 we provide the merger frequency for each different EoS, and for this analysis we take 500Hz − fmerge as inspiral phase and fmerge − 4000Hz as postmerger phase. In the following subsections we report our results for each of these detectors and explain how the sensitivity affects the fitting and the Bayes Factor, inferring new details.

#### 3.2.1 Advanced LIGO

Among the mentioned detectors, Advanced LIGO (LIGO A+) has the lowest sensitivity[71], particularly at high and low frequencies, limiting its ability to probe deep inspiral or post-merger dynamics compared to next-generation observatories. In Table 4 we show the norm (or the SNR) of the true LMBH-LMBH signal in both the inspiral and post merger phase, and the Bayes Factor BBNSLMBH for both the inspiral and postmerger phases, highlighting that for certain stiffer EoSs the Bayesian evidence favoring the LMBH hypothesis is higher in the postmerger phase than in the inspiral phase. Here we chose the DL as 350 Mpc. The BF calculated for the whole frequency range Btotal are also shown. BF close to 1 indicates no significant preference between the models. For simplicity of notation, we denote the Bayes Factor BBNSLMBH as B.

#### 3.2.2 NEMO

NEMO is expected to operate at cryogenic temperatures and employs shorter, stiffer suspensions to reduce thermal vibrations, especially suspension thermal noise, a dominant source at high frequencies[72]. Other key improvements include the reduction of internal thermal noise from the mirror substrates and coatings, as well as minimizing shot noise, which arises from quantum fluctuations in the laser light[72]. These combined features make NEMO particularly well-suited for capturing the detailed structure of post-merger signals, enabling deeper insight into the NS EoS and other extreme matter phenomena.

EoS norm (Ins) norm (PM) FFIns FFPM FFtotal BIns BPM Btotal

2H 3.51 1.04 0.97 0.77 0.96 1.38 1.24 1.73 MS1b 3.72 0.82 0.98 0.84 0.98 1.26 1.11 1.4

H4 3.89 0.97 0.99 0.71 0.97 1.23 1.26 1.55 BHBΛϕ 2.31 0.87 0.78 0.82 0.76 2.9 1.12 3.5

ALF2 4.00 0.75 0.99 0.68 0.98 1.14 1.16 1.33 LS220 2.35 0.76 0.79 0.73 0.77 2.89 1.14 3.42

SLy 4.23 0.62 0.99 0.76 0.99 1.11 1.08 1.21 2B 4.37 0.31 0.997 0.99 0.997 1.06 1.00 1.07

- Table 4: Fitting Factor FF & Bayes Factor B for LMBH vs BNS models for different

EoS. B is calculated assuming the BNS as the true signal at LIGO A+[71]. The ρopt of each EoS are shown separately for the late inspiral and postmerger phases. The

- B for the postmerger part is not enough to draw a conclusion, as the norm in the postmerger part is less than the inspiral part. Here DL is chosen to be 100 Mpc (m1 = m2 = 1.35M⊙). The EoSs are listed from stiffer to softer cases. Evidently the mismatch is significant in the case of stiffer EoSs. 2B being the softest of all, mimics the LMBH signal, leaving almost equal evidence for both the cases. Interestingly, for the two finite-temperature EoSs - BHBΛϕ & LS220, the fit in the inspiral part is itself worse, resulting in a comparatively higher Bayesian evidence.


EoS norm (Ins) norm (PM) FFIns FFPM FFtotal BIns BPM Btotal 2H 3.06 2.72 0.97 0.71 0.87 1.33 6.32 8.5

MS1b 3.42 2.45 0.98 0.81 0.93 1.27 2.78 3.53 H4 3.67 3.22 0.98 0.7 0.87 1.3 14.8 20.2

BHBΛϕ 2.95 2.72 0.89 0.83 0.85 2.46 3.2 12.37 ALF2 3.94 2.32 0.99 0.68 0.92 1.22 4.23 5.2 LS220 3.05 2.26 0.9 0.74 0.84 2.4 3.15 8.5

SLy 4.32 1.84 0.99 0.81 0.97 1.2 1.8 2.2 2B 4.71 0.98 0.997 0.99 0.997 1.07 1.01 1.11

- Table 5: Fitting Factor FF & Bayes Factor B for LMBH vs BNS models for different


EoS with NEMO, taking the BNS merger as the true signal. DL is chosen to be 300Mpc.

In Table 5, we present the values of the FF and B calculated separately for the inspiral and postmerger phases, as well as for the full frequency range spanning 500Hz to 4000Hz. A notable observation is that, owing to NEMO’s enhanced sensitivity in the high-frequency regime, certain stiffer EoSs (H4, 2H, ALF2) yield remarkably higher Bayesian evidence in the postmerger phase compared to the inspiral phase, highlighting the importance of the second peak observed in frequency domain waveform of Fig.2. As the sensitivity of NEMO is better than LIGO A+, throughout the frequency range

of our concern (Fig.4), we take more distant sources, such as DL = 300 Mpc for an acceptable SNR.

#### 3.2.3 Cosmic Explorer

EoS norm (Ins) norm (PM) FFIns FFPM FFtotal BIns BPM Btotal

2H 14.51 4.11 0.98 0.79 0.97 260.15 24.8 7006.4 MS1b 15.4 3.22 0.99 0.86 0.98 49.5 4.1 210

H4 16.1 3.55 0.99 0.72 0.98 36.7 20.3 747.2

BHBΛϕ 9.47 3.03 0.78 0.84 0.77 O(108) 4 O(109) ALF2 16.56 2.56 0.99 0.71 0.987 9.8 5.1 53.57 LS220 9.65 2.52 0.79 0.76 0.78 O(108) 3.75 O(109) SLy 17.45 2.04 0.994 0.79 0.992 6.01 2.2 13.13 2B 18.04 1.05 0.997 0.988 0.997 2.69 1.01 2.88

Table 6: Fitting Factor FF & Bayes Factor B for LMBH vs BNS models for different EoS with CE, taking the BNS merger as the true signal. The DL is chosen to be 350 Mpc.

Cosmic Explorer (CE) is a proposed third-generation ground-based GW detector designed with 40 km arm lengths, an order of magnitude larger than Advanced LIGO’s 4 km arms, offering vastly improved strain sensitivity across a broad frequency range, particularly in the low-frequency band (5 − 1000Hz), which is crucial for observing the full inspiral phase of CBC with high SNR[73, 112]. In Table 6 we show the FF and B for each EoS. See the caption of Table 4 for the specifications of the mergers. As the sensitivity of CE significantly exceeds that of LIGO A+, we chose the DL as 350Mpc. The key observation here is that the Bayesian evidence is already significantly high in the inspiral phase due to CE’s superior low-frequency sensitivity; the inclusion of the postmerger phase further enhances the evidence, offering a more confident characterization of the source.

#### 3.2.4 Einstein Telescope

The Einstein Telescope (ET) is a proposed third-generation underground GW observatory featuring a unique triangular configuration with 10 km arms, designed to achieve unprecedented sensitivity across a broad frequency range, particularly below 10Hz, surpassing Advanced LIGO+ and NEMO by mitigating low-frequency seismic, suspension and thermal noise through underground installation and cryogenic technologies[74, 113]. ET, and CE are particularly powerful for studying early inspiral physics, precision cosmology, and multi-band GW astronomy in synergy with spacebased detectors. In Table 7 we provide the FF and B for all the EoSs in both the inspiral and postmerger phase. Here we chose the DL as 350 Mpc. As for CE, for ET the Bayesian evidence is already strong in the inspiral phase. This is primarily due to its excellent low-frequency sensitivity, achieved through underground placement and advanced noise mitigation strategies. The addition of the postmerger phase further improves the evidence.

EoS norm (Ins) norm (PM) FFIns FFPM FFtotal BIns BPM Btotal

2H 14.74 3.67 0.98 0.78 0.97 213.9 14.5 3525.5 MS1b 15.56 2.92 0.99 0.84 0.98 39.19 3.52 147.7

H4 16.22 3.5 0.99 0.72 0.98 28.3 21.4 604.8

BHBΛϕ 9.02 3 0.77 0.83 0.76 O(108) 4.2 O(109) ALF2 16.6 2.6 0.99 0.69 0.986 8.4 6.1 53.13 LS220 9.18 2.58 0.78 0.74 0.77 O(108) 4.6 O(109) SLy 17.46 2.15 0.995 0.78 0.992 5.6 2.5 14.2

2B 18 1.08 0.997 0.991 0.997 2.74 1.01 2.93

- Table 7: Fitting Factor FF & Bayes Factor B for LMBH vs BNS models for different


EoS with ET, taking the BNS merger as the true signal. The source DL is chosen to be 350 Mpc.

#### 3.3 Dependence on Luminosity Distance

Having analyzed the FF and the B across various EoS and for the different detectors, we now investigate how B varies as a function of the luminosity distance DL. We have argued that the waveform fit in the postmerger phase is generally poorer than in the inspiral phase. However, the corresponding Bayesian evidence varies across detectors due to their differing sensitivity profiles. For most cases, the evidence is higher in the inspiral phase, primarily because current detectors exhibit superior sensitivity at lower frequencies. Nonetheless, for stiffer EoS and in detectors with enhanced high-frequency sensitivity; such as NEMO, the Bayesian evidence in the postmerger phase can surpass that of the inspiral phase.

In Fig.5, we present the Bayes Factor BLMBHBNS as a function of DL for the different detectors under consideration, illustrating how the discriminating power between LMBH-LMBH and BNS mergers evolves with increasing source distance. For this comparison, we present the total Bayes Factor evaluated over the full frequency range from 500 Hz to 4000 Hz. As before, we consider the BNS merger as the true signal. The strongest Bayesian evidence is observed for stiffer EoS. For the EoSs 2H & H4, the NEMO detector yields a B exceeding 1000 even at a distance of 200 Mpc, whereas LIGOA+ provides negligible evidence at that distance. However, with LIGOA+ and with the stiffest EoS 2H, events within 50 Mpc still yield significant evidence. For CE and ET, the evidence remains strong, exceeding a factor of 100, up to 600 Mpc for the same EoSs. The Bayesian evidence decreases progressively from stiffer to softer EoSs. For the softest EoS (2B), the evidence becomes notably small, as the NSs are sufficiently compact to closely mimic the LMBH waveform. Even with the most sensitive detectors like CE and ET, the Bayes Factor for EoS 2B is only around 11 at 200 Mpc. The intermediate EoSs exhibit evidence values that lie between those of 2H and 2B, and this trend is consistently observed across all detectors. The two finitetemperature EoSs, BHBΛϕ[97] and LS220[98], lead to noticeable differences in the waveform already from the late inspiral phase, resulting in a huge Bayesian evidence from the inspiral phase itself. To be conservative, here we omit them.

- 100
- 101
- 102
- 103
- 104
- 105


|LIGO A+ 2H H4<br><br>MS1b ALF2 SLy<br><br>2B|
|---|


BNSBBayesFactorLMBH

10 50 100 500 1000

Luminosity Distance DL(Mpc)

- 100
- 101
- 102
- 103
- 104
- 105


|NEMO 2H H4<br><br>ALF2 MS1b SLy<br><br>2B|
|---|


BNSBBayesFactorLMBH

100 200 400 600 800 1000

Luminosity Distance DL(Mpc)

- 100
- 101
- 102
- 103
- 104
- 105


|Cosmic Explorer 2H H4<br><br>MS1b ALF2 SLy<br><br>2B|
|---|


BNSBBayesFactorLMBH

100 500 1000 5000

Luminosity Distance DL(Mpc)

- 100
- 101
- 102
- 103
- 104
- 105


|Einstein Telescope 2H H4<br><br>MS1b ALF2 SLy<br><br>2B|
|---|


BNSBBayesFactorLMBH

100 500 1000 5000

Luminosity Distance DL(Mpc)

- Figure 5: Bayes Factor (B) as a function of DL for different detectors and different EoSs. This essentially demonstrates how the ability to distinguish between source models depends critically on the NS EoS and the DL of the event. The dependence


is given by B ∝ exp(1/DL2). The evidence against the LMBH merger case over BNS merger become significantly large for stiffer EoSs. Interestingly for two EoSs, which we haven’t shown in this figure – BHBΛϕ, & LS220, the Bayesian evidence against LMBH will be very high as these BNS merger waveforms have significant mismatch with the LMBH waveform from the inspiral part itself, as discussed in the main text. Note the different axis-scaling of DL for different detectors.

### 4 Results: Constraints on Transmutation & Particle DM

#### 4.1 Model-Independent Results on Transmutation

- 4.1.1 Parsing the CBC Rate into BNS & LMBH Rates As we discussed in the introduction, in current GW data analysis pipelines events with


component masses in the range of 1−2.5M⊙ are generally categorized as BNS mergers by the LVK collaboration[35]. However, without a simultaneous EM counterpart, such as a kilonova or a short gamma-ray burst, this classification is not robust. This uncertainty becomes critical when estimating the astrophysical merger rate of BNS systems, as it opens up the possibility that some of these events may, in fact, originate from LMBH–LMBH systems. Consequently, it is important to account for this potential contamination to avoid overestimating the true BNS merger rate.

The theoretical prediction of the CBC rate, based on stellar evolution and binary formation, is given as[114–117],

t

dρ∗ dtf

dPm dt

λ

. (4.1)

RCBC(t) =

dtf

t∗

Here tf denotes the binary formation time, and dρ∗/dtf denotes the cosmic star formation rate at time tf [118]. The fraction of stellar mass that got bound as a binary is given as λ = 10−5M⊙−1 [114]. The merger time delay distribution dPm/dt ∝ 1/(t − tf) is the probability density that the binary formed at time tf, will merge within a time

- t − tf [114]. The time t∗ = 4.9 × 108 years corresponds to z = 10, taken as the epoch for the formation of the first stars.


The above rate density can be normalized to LVK’s estimate for the same, viz., 10 − 1700Gpc−3 yr−1, at the current time t = 13.8 billion years or z = 0. Now, as suggested earlier, this normalization is subject to the fact that there is no background in the NS-NS signal. In reality there can be LMBH-LMBH signals, which are nondistinguishable from BNSs beyond a certain DL. If we assume there are only two candidates for a low-mass CBC, viz., NS-NS mergers & LMBH-LMBH mergers, then for a fixed ρopt with BNSs being the truth, the Bayes Factor B ≡ BLMBHBNS = BBNSLMBH, and gives the probabilities of these CBCs either being NS-NS or LMBH-LMBH mergers as

p(BNS|data) = B 1 + B

1 1 + B

and p(LMBH|data) =

. (4.2)

For small values of DL, the Bayes Factor remains sufficiently large to favor one model over the other. As DL increases and B starts decreasing, eventually tending to 1, the model probabilities approach 1/2, indicating indistinguishability. In Fig.6 we show the theoretical CBC rate (Eq.4.1, solid blue line) as a function of the luminosity distance. The rate has been normalized using LVK’s current observation, which predicts the rate to be within 10 − 1700Gpc−3yr−1 [35]. Among three different statistical models mentioned in[35], we choose the Multi-Source Model (MS), which predicts the rate to be within 130 − 1700Gpc−3yr−1, and for the normalization at z = 0, we choose the mean of this model, given as 915Gpc−3yr−1.

Up to a source distance of approximately 400 (25) Mpc, the Bayesian evidence remains sufficiently high to reliably distinguish between BNS and LMBH mergers with ET (LIGO A+), implying that the inferred BNS merger rate is consistent with the true rate. However, beyond 400 (25) Mpc, the Bayesian evidence gradually decreases, and the probability of misidentifying LMBH-LMBH mergers as BNS mergers (or vice versa) increases. Beyond ∼ 1200 (120) Mpc for ET (LIGO A+), the distinction becomes difficult, and the two types of sources appear nearly identical. As a result, the inferred BNS merger rate may be overestimated. As noted earlier, stiffer EoSs enhance the ability to distinguish BNS from LMBH mergers, enabling reliable separation at larger DL and resulting in tighter constraints.

- 4.1.2 Exclusion Sensitivity for Transmutation Fraction Unlike the previous section, where we estimated the rates, now we ask a different question: What is the fraction fLMBH of the CBC rate that can be compatible with


- 102

- 103

- 104


EOS-SLy & with LIGO A+

−−31Mergerrate[Gpcyr]

Compact Binary Merger Rate Inferred BNS Merger Rate

Inferred LMBH Merger Rate

100 101 102

Luminosity Distance DL [Mpc]

- 102

- 103

- 104


EOS-SLy & with Einstein Telescope

−−31Mergerrate[Gpcyr]

Compact Binary Merger Rate

Inferred BNS Merger Rate

Inferred LMBH Merger Rate

101 102 103

Luminosity Distance DL [Mpc]

- Figure 6: Merger rates as a function of DL observable by LIGOA+(left panel) and ET (right panel). The blue solid line represents the theoretically predicted CBC merger rate, normalized to the latest observational limits from the LVK collaboration. The red and green dotted lines denote the most probable BNS and LMBH merger rates that would be inferred, respectively, using the Bayes Factors. Note the differing scales on the horizontal axes: with LIGO A+ reliable source classification becomes challenging beyond ∼ 120 Mpc due to reduced SNR, while for ET this limitation occurs beyond ∼ 1200 Mpc. For this analysis, we adopt the SLy EoS as a conservative benchmark; stiffer EoSs enhance distinguishability.


being LMBHs? To answer this question, we assume that we are given the detector specifications and the true model where all CBCs are in fact BNSs.

The expected number of CBCs (NCBC) has been computed earlier and can be expressed as[105, 114, 119],

NCBC = T ×

∞

4πDc2(z) (1 + z)H(z)

CΘ RCBC(z), (4.3)

dz

0

where T is the years of observation, RCBC is defined in Eq.4.1, Dc(z) denotes the comoving radial distance as a function of redshift, and H(z) is the Hubble expansion rate at a redshift z. The cosmological parameters are taken from the latest Planck measurements[120]. The angular dependence of the SNR is encoded within the cumu-

5/6

DL(z) r0

1.2 M⊙ (1+z) Mc

lative distribution of Θ; given by CΘ, where the argument Θ = ρ

0

8

varies within 0 and 4[119, 121], calculated from the geometry of the sources and the antenna. DL(z) = (1+z)Dc(z) is the luminosity distance at redshift z, the chirp mass of the merging binary is denoted by Mc, and ρ0 and r0 denote the SNR threshold and characteristic distance reach of a particular detector, respectively. For this analysis we have considered two cases, taking ρ0 = 8 and r0 = 80 Mpc for LIGO A+ and & 1591 Mpc for ET, respectively[121]. Apart from RCBC, the remainder of the expression in Eq.4.3 denotes the exposure ⟨VT⟩ for a specific detector. See Appendix A.2 for the details of the detector exposure.

We perform a hypothesis test, assuming all potentially detected events will be consistent with background BNS merger events (i.e., no true LMBH merger events).

1.000

LIGO A+ 10 years

0.100

ET 1 year

fLMBH

ET 10 years

0.010

0.001

100 200 300 400

Luminosity Distance DL (Mpc)

- Figure 7: Exclusion sensitivity (90% confidence; upper limit)[122, 123] on the frac-


tion of LMBH mergers (fLMBH) in CBCs, shown for LIGO A+ and the ET across nine luminosity distance bins, each of width 50Mpc. The constraints improve with increasing distance due to enhanced exposure (see Fig.11), but begin to weaken beyond ∼ 250Mpc (for ET) as the distinguishability starts to decrease, reducing the ability to differentiate LMBH signals from BNS mergers, resulting in more numbers of backgrounds. LIGO A+ requires approximately 10 years of data to achieve meaningful constraints, while ET achieves stronger limits with just 1 year of observation. The exposure starts to rapidly decrease after 250 Mpc for LIGO A+, where ET can go up to very high luminosity distances.

In each independent redshift bin i, the total number of observed LMBH events is modeled as a Poisson variable with mean ⟨ni⟩ = µSi + Bi, where Si is the expected number of LMBH (TBH in our case) merger events, and Bi is the expected number of background BNS events which are misclassified as LMBH events, and µ is a hypothesis label with µ = 1 representing the presence of LMBH signals and µ = 0 corresponding to the null (background-only) hypothesis. We construct a log-likelihood ratio between the µ = 1 over µ = 0 hypothesis, and equate its square root to a desired statistical threshold (e.g., Z = 1.28 for 90% confidence[122, 123], see Appendix A.3).

If a fraction fi of the CBCs are LMBHs by origin, then the signals and backgrounds for the ith bin are given by Eq.4.3 as,

Bi 1 + Bi Bi = (1 − fi) × RCBC,i ⟨VT⟩i

Si = fi × RCBC,i ⟨VT⟩i

1 1 + Bi

, (4.4)

where B = BBNSLMBH = BLMBHBNS , assuming a fixed ρopt. A test statistic value of Z ≥ 1.28

corresponds to a rejection of the signal+background hypothesis over background-only hypothesis at the 90% confidence level. This threshold places a projected upper limit on the LMBH fraction, such that true values of fi exceeding this bound would lead to incompatibility with a BNS-only interpretation.

In Fig.7, we present the 90% exclusion sensitivity to the LMBH merger fraction, denoted by fLMBH, as a function of DL, for both LIGO A+ and the ET. The analysis is performed in nine bins, each with a width of 50 Mpc. The blue shaded region corresponds to 10 years of LIGO A+ observations, while the green shaded regions corresponding to ET, shown for 1 year and 10 years of observation time. For this analysis, we assume a fiducial CBC rate of RCBC = 1000Gpc−3 yr−1. Variations in this rate act

- as an overall normalization and scale the resulting constraints proportionally. As expected, the sensitivity drops at higher distances (owing to lack of distinguishability) and at very small distances (owing to small number of events). We have again adopted a conservative choice of the EoS on the softer side, specifically the SLy EoS (see Fig.2). Choosing a stiffer EoS would lead to more pronounced matter effects in the waveform, thereby yielding comparatively stronger sensitivities.

4.2 Exclusion Sensitivity for DM-Nucleon Interaction

The preceding discussions are agnostic to the origin of LMBHs. However, now we specifically consider the scenario in which LMBHs are formed via DM capture-induced collapse of BNS systems[14, 22, 28, 31]. The LMBH merger rate becomes directly dependent on the underlying BNS merger rate, and one can obtain limits on the DMnucleon interaction cross section σχn.

Non-annihilating DM particles, with mass mχ and scattering cross-section with nucleons σχn, can be captured by a NS over its lifetime[25, 26, 31]. Considering a constant σχn, corresponding to a heavy mediator of the DM-nucleon interactions, the capture rate is given as[22, 28, 32],

C = 1.4 × 1020 s−1 0.4 GeV cmρχ

−3

105 GeV mχ

σχn 10−45 cm2

× 1 − 1−e−A

2 A2

vesc 1.9×105km s−1

2 220 km s−1

v¯gal . (4.5)

The factor involving A2 = 6mχmnvesc2 /v¯gal2 (mχ − mn)2 accounts for inadequate momentum transfers at larger mχ, given NS escape speed vesc and typical DM density ρχ and speeds v¯gal in the galaxy. For a typical 1.35M⊙ NS, with 10 km radius, with a lifetime of 1 Gyr, the accumulated DM mass can reach up to ∼ 10−15 M⊙. If the captured DM particles are sufficiently massive, they can drift toward the center of the star and thermalize, forming a dense core within a thermal radius rth. For example, DM with mχ = 105 GeV can form such a core within a radius of approximately 5cm[28]. This overdense core may eventually undergo gravitational collapse, either due to self-gravitation or due to overcoming the fermi-degeneracy pressure, depending on whether the DM particle is bosonic or fermionic[14, 22]. The resulting collapse can lead to the formation of a small BH at the center of the NS. Once formed, the small BH

- at the core of the NS can eventually consume the entire star, leading to the formation


10−45

LIGO A+ 10 years Observation

10−46

ET1yearObservation

10−47

2σ[cm]χn

10−48

10−49

10−50

Bosonic DM Observed upto 450 Mpc

10−51

102 103 104 105 106 107

mχ [GeV]

- Figure 8: Exclusion sensitivity for DM-nucleon cross section σχn as a function of DM mass mχ. This analysis assume bosonic non-annihilating DM, and includes all events within DL ≤ 450Mpc. We adopt a fiducial compact binary coalescence rate of RCBC = 1000Gpc−3 yr−1, which acts as a normalization factor for the limits. The distinguishability between LMBH mergers and BNS mergers is computed assuming a soft nuclear EoS for the BNS mergers (SLy); adopting a stiffer EoS would yield stronger constraints due to significant mismatch between these two cases. Competing limits on this parameter space can be found in[28] where the limit was calculated assuming no background of LMBH mergers, and with considering a uniform prior on the CBC rate, which is estimated to be within 10 − 1700Gpc−3 yr−1 till LVK’s 3rd observing run.


of a black hole with mass comparable to that of the progenitor[30]. Such LMBHs, originating from DM capture-induced collapse of NSs, are referred to as Transmuted Black Holes(TBHs).

The merger rate of these TBH-TBH binaries[14] is given as:

t0

dRCBC

df dr

dtf × Θ[t0 − tf − τtrans [mχ,σχn,ρext(r,t0)]] , (4.6) where df/dr is the radial distribution of the progenitor BNSs in a galaxy. The transmuted black hole merger rate intrinsically depends on the BNS merger rate, as only a fraction of originally BNS systems can evolve into TBH binaries. This fraction is captured by the step function Θ[t0 − tf − τtrans(mχ,σχn,ρext(r,t0))], which encodes the condition that the transmutation timescale τtrans = τcollapse + τswallow, which a function of the dark matter mass mχ, nucleon scattering cross-section σχn, and ambient dark matter density ρext, must be shorter than the time available since binary formation. Table 1 of Ref.[124] provides the brief details of the timescales required in this scenario.

dtf

RTBH = dr

t∗

The TBH-TBH mergers could be observable in GW detectors as LMBH mergers. The absence of such detections thus places stringent constraints on the DM-nucleon

scattering cross-section σχn [28, 47]. However, the constraints in Ref.[28] were obtained under the assumption that no LMBHs would be actually detected. The method presented in this paper can be used to assess the exclusion sensitivity to the DM parameter space without making the above assumption. Interpreting the LMBHs as TBHs (Eq.4.6), we translate our limits on fLMBH into bounds on the DM mass and its scattering cross section with nucleons, as shown in Fig.8. For this purpose, we replace f × RCBC in Eq.4.4 with the TBH-TBH merger rate RTBH (Eq.4.6), and determine the region in the (mχ − σχn) plane where the statistical significance Z is ≥ 1.28.

In Fig.8 we shows projected exclusion on the DM parameter space. For this analysis, we integrated up to a maximum luminosity distance of DL = 450Mpc to compute the total number of signal and background events. The resulting bounds thus reflect the contribution from all the nine bins up to 450 Mpc. The exclusion sensitivity of Fig. 8, for 10 years observation with LIGO A+, is slightly stronger than the projected upper limits in Fig.1 of Ref.[28]. This is simply because the ⟨VT⟩ in this case is approximately twice the exposure used in the forecasted limit in Ref.[28]. Evidently, ET can achieve stronger exclusions with 1 year of data. Although here we focused on bosonic DM, the same technique can be applied to other scenarios, including fermionic DM or bosonic DM that forms a Bose Einstein condensate (BEC)[28].

### 5 Discussions & Conclusion

In this study, we have systematically investigated the potential degeneracy between BNS mergers and LMBH mergers. As a first step, we considered systems with identical component masses and spin configurations for both BNS and LMBH binaries, focusing on the 1.35M⊙-1.35M⊙ case. While the LMBH waveform can be obtained directly from standard general relativistic binary black hole models, generating accurate BNS waveforms is considerably more challenging due to the involvement of complex microphysical processes, most notably the dependence on the NS EoS. To capture this effect, we extracted BNS waveforms from the publicly available CoRe database, carefully selecting eight different EoSs ranging from the stiffest to the softest cases, and analyzed their impact on the waveform morphology, particularly in the late inspiral and postmerger phases.

After obtaining the two sets of waveforms, we analyzed the mismatch between them. We found that the primary source of mismatch arises in the high-frequency regime, where strong matter effects become significant due to the increasing influence of gravity in the late inspiral and postmerger phases. This behavior is consistent with the expectation that the microphysical properties of NS matter, governed by the EoS, manifest predominantly in the strong-field regime. We divide the waveforms into two distinct phases; the inspiral and the postmerger. Through this separation, we demonstrate that the fit between the BNS and LMBH waveforms deteriorates significantly in the postmerger phase compared to the inspiral. This is expected, as the postmerger dynamics are strongly influenced by matter effects and the tidal interactions that depend sensitively on the NS EoS. These EoS-dependent effects result in diverse outcomes for BNS merger remnants, which can be short-lived or long-lived hypermassive NS, or

may undergo a prompt collapse into a BH, leading to characteristic differences in the emitted GW signal. We compute the Bayesian evidence in favor of LMBH models over BNS models across a variety of NS EoSs, focusing on how this evidence evolves as a function of luminosity distance. Our analysis highlights the critical role of detector sensitivity and matter effects at different distances, which in turn influences the ability to distinguish between LMBH and BNS mergers. This variation in Bayesian evidence with distance has direct implications for key astrophysical measurements, most notably, the estimation of the BNS merger rate. Misidentification of LMBH mergers as BNS events at large distances can lead to an overestimation of the true BNS rate, thereby impacting theoretical modeling, and population studies.

We then computed expected exclusions on the maximal fraction of LMBH mergers contributing to the population of CBCs. We perform a thorough statistical analysis incorporating both genuine LMBH merger signals and background contributions arising from the misclassification of BNS mergers, particularly in regimes where waveform degeneracies occur due to limited detector sensitivity. We further consider the scenario in which these LMBHs originate from DM capture-induced transmutation of BNSs. In this context, the limits on fLMBH can be translated into constraints on the DM parameter space, specifically the DM mass mχ and its scattering cross section with nucleonsσχn. These exclusions are similarly based on rejecting the LMBH+BNS hypothesis in favor of the BNS-only hypothesis, i.e. in the absence of observed LMBH signals. We intentionally exclude the case of mixed LMBH-NS binaries in this study, as one of our motivations was LMBHs formed via dark matter capture-induced transmutation. Given that the binary neutron stars are typically close enough to reside in the same ambient DM environment, it is expected that both components undergo transmutation, resulting in symmetric LMBH-LMBH systems.

To summarize, we present a numerical-relativity–based framework to distinguish BNSs from LMBHs and constrain exotic formation channels, including DM-induced scenarios such as TBH formation. Unlike prior studies relying on inspiral-only waveforms, our analysis spans both inspiral and postmerger regimes and quantifies waveform degeneracies using Bayesian evidence and Fitting Factors across detector sensitivities and distances. Prima facie the inspiral phase provides a stronger discrimination between BNSs and LMBHs than the corresponding postmerger phase. However, this may not remain true when one includes more parameters (e.g., spins). The Fitting Factors for the waveforms in the postmerger phase may be less subject to parameter degeneracies, as the difference comes from a distinct feature. This has implications for dark matter constraints and BNS rate estimates, and highlights the need for improved high-frequency modeling[125] for probing NS EoSs and exotic physics[126].

### Note Added

After our work was completed, we became aware of the preprint arXiv:2507.07895[127]. The above preprint explores tidal effects in the inspiral phase of GW190425-like systems

- as a means to distinguish NSs from BHs. In contrast, our work presents the first systematic study of the postmerger regime, incorporating a broad set of EoSs and


- leveraging the information from the second peak beyond the inspiral. While the above preprint advocates for and uses a Savage-Dickey ratio to quantify distinguishability, appropriate in the case of nested hypotheses, we use the more generally applicable Bayes Factor. More broadly, while these two studies have a similar aim, they differ significantly in focus, scope, and detail. Our work has been presented previously, e.g.,
- at PPC 2024 in IIT Hyderabad, at GW BSM 2025 in ICTS-TIFR Bengaluru, and at NDM 2025 in IHP Paris.


### Acknowledgments

We thank Parameswaran Ajith, Aryaman Bhutani, Prolay Krishna Chanda, Ranjan Laha, David Radice, Anupam Ray, and Aditya Vijaykumar for helpful discussions and suggestions while this manuscript was being prepared. BD thanks Reed Essick, Maya Fishbach, and Philippe Landry at CITA for hospitality during the summer of 2023 and for helpful conversations that motivated this study. This work is supported by the Dept. of Atomic Energy (Govt. of India) research project RTI 4002, and by the Dept. of Science and Technology (Govt. of India) through a Swarnajayanti Fellowship to BD. BD and SB acknowledge the support of the Institut Henri Poincar´e (UAR 839 CNRSSorbonne Universite´), and LabEx CARMIN (ANR-10-LABX-59-01) during the “NDM 2025” workshop. SB thanks the organizers of N3AS summer school on Multi-messenger Astrophysics for hospitality.

### A Appendices

#### A.1 Data Extraction from CoRe Database

The CoRe[80] database website provides a section named ‘GW-DB’ where one can find the instructions about accessing the datasets required. One can also find information on the EoSs and a description of the data structure. The data for each waveform is stored in a HDF5[128] file, for example named as BAMXXXX.h5. Dismantling the file with h5py[129] module of python, one can find the data structure of each waveform. The file is written in three groups:

- 1. Energy — contains the binding energy information of the binary in relation with reduced angular momentum[130].
- 2. rh22 — contains the l = m = 2 multipole of the metric waveform extracted at some coordinate radius r.
- 3. rψ4|lm — contains the Weyl curvature[131] waveform up to l = m = 4 multipole.


As we will generate the BNS strain vs. frequency waveform for different EoSs, we are only concerned with the second group (rh22).

|BAM:0098| |
|---|---|
| | |


|Strain (rh22)| |
|---|---|
| | |
|1. Rh l2 m2 r00450.txt<br><br>2. Rh l2 m2 r00600.txt<br><br>3. Rh l2 m2 r00800.txt<br><br>4. Rh l2 m2 r01000.txt<br><br><br>| |


|Weyl multipole (rψ4|lm)| |
|---|---|
| | |
|1. Rpsi4 lx my r00450.txt<br><br>2. Rpsi4 lx my r00600.txt<br><br>3. Rpsi4 lx my r00800.txt<br><br>4. Rpsi4 lx my r01000.txt<br><br><br>| |


|Energy| |
|---|---|
| | |
|1. EJ r00450.txt<br><br>2. EJ r00600.txt<br><br>3. EJ r00800.txt<br><br>4. EJ r01000.txt<br><br><br>| |


- Figure 9: Structure of BAM0098.h5 file. In the Weyl curvature multipole section, filenames are written as Rpsi4 lx my r00450.txt, where x takes values from 2–4 and y from 0–4 depending on the l values. R denotes the extraction radius where these quantities are calculated, with values 450M⊙, 600M⊙, 800M⊙, and 1000M⊙.

−0.02 −0.01 0.00 0.01 0.02

Time t [sec]

10−23

10−22

10−21

10−20

htStrain()

EoS SLy, DL = 1Mpc

|EoS SLy, DL = 1Mpc|
|---|


500 1000 1500 2000 2500 3000 3500 4000

Frequency f [Hz]

10−25

10−24

10−23

10−22

˜hfStrain()[sec]

- Figure 10: The time domain and frequency domain strain amplitudes are shown for the SLy EoS[132, 133], obtained from the BAM:0098 waveform dataset. Waveforms corresponding to seven additional EoSs have been extracted using the same procedure. For subsequent analysis, the frequency domain representations are used.


#### Strain vs Frequency Waveform from BAM:0098

As an example, consider BAM:0098.h5 which is simulated with the EoS SLy[132, 133], with initial parameters as per our requirement. Fig.9 shows its detailed data structure explaining the groups and attributes of the HDF5 file. The precise values of the initial input can be found in the metadata.txt file under the main file. We will now discuss the second group of the main data file, i.e., the l = 2,m = 2 strain part (rh22).

The dominant l = m = 2 mode of the radiated GW, corresponds to h22(t) in the rh22 part of the datafile. For this EoS we choose the BAM0098 Rh l2 m2 r00800.txt file, where the data is extracted at a radius of 800M⊙ (in geometric units, with G =

- 100
- 101
- 102


|LIGO A+ ET|
|---|


−−31VT[Gpcyr]

10−1

10−2

10−3

- 10−3 10−2 10−1 100 101 Redshift [z]

10−6

10−5

- 10−4


- Figure 11: Exposure of the detectors. The detector specifications and the angular information are taken from[114, 119, 121]. The value of Mc is chosen to be 1.17M⊙, i.e., the chirp mass of a symmetric binary with m = 1.35M⊙.


c = 1, using mass as the dimension). The first three columns of this file provide the time (u), real part of l = m = 2 strain (Rerh22), imaginary part of l = m = 2 strain (Imrh22), respectively. The moment of the merger is defined as the time at which the h22 amplitude is the highest. Waveforms are given in terms of retarded time defined as[88],

u = t − r∗(r) = t − r + rsln

r rs − 1 , (A.1)

where r is the coordinate extraction radius in the simulations (= 800M⊙, in this example), r∗ is the associated tortoise Schwarzschild coordinate and rs = 2M is the Schwarzschild radius. From these inputs one can obtain the h(t) vs. t waveform. In Fig.10 (left panel), we show the time domain waveform for face-on orientation (ι = 0) of the binary at a luminosity distance DL = 1Mpc. Here, t = 0 sec denotes the time of merger. In the right panel of Fig.10 the frequency domain (h(f) − f) waveform is shown, which is obtained using a Fourier transform on the time domain data.

#### A.2 Exposure of the GW Detectors

Here we present the exposure for both LIGO A+ and the Einstein Telescope (Fig.11). The y-axis shows the volume-time exposure, defined as the product of the sensitive volume and observation time,

⟨VT⟩ = T ×

∞

4πDc2(z) (1 + z)H(z)

dz

CΘ

0

ρ0 8

DL(z) r0

1.2M⊙ (1 + z)Mc

5/6

##### . (A.2)

Here in Fig.11, we assume 1 year of data acquisition for each detector. The x-axis corresponds to redshift. For reference, a redshift of z = 0.1 approximately corresponds to a luminosity distance (DL) of ∼ 450Mpc.

#### A.3 Projected Exclusion Significance

- 1
- 2
- 3
- 4
- 5
- 6


|ET 1 year<br><br>LIGO A+ 10 years<br><br>Events upto 450 Mpc<br><br>Z=1.28 (90% Conﬁdence Level)|
|---|
| |


ExclusionSigniﬁcanceZ

10−2 10−1 100

fLMBH

- Figure 12: Exclusion significance Z as a function of the LMBH merger fraction fLMBH. As fLMBH increases, the number of LMBH-induced signal events rises relative to the background, leading to a stronger statistical preference for the signal-plus-background hypothesis over the background-only hypothesis. The significance grows accordingly,


allowing higher values of fLMBH to be excluded with increased confidence for the nonobservation of signal. The EoS SLy has been assumed for the BNS mergers to compute the Fitting Factor and Bayes Factor that inform expected rates.

The total number of events in the ith bin, from a Poisson process is given by,

e−(µS

(µSi + Bi)n

i+Bi)

i

, (A.3)

P(ni) =

ni!

where Si & Bi in our case can be calculated using Eq.4.3. The log-likelihood ratio of the signal hypothesis (µ = 1) over background-only hypothesis (µ = 0) is given by,

q = −2ln L(S|µ=1) L(Sˆ|µ=0)

Si + Bi

Bi − Si . (A.4) We define the median expected exclusion significance Z, i.e. the statistical mea-

= −2

Bi ln

i

sure for rejecting the signal-plus-background hypothesis in favor of the background-only

hypothesis (i.e. no signal is observed), as

Z = √q = 2

Bi Si + Bi

Bi ln

+ Si . (A.5)

i

A threshold of Z ≥ 1.28[122, 123] corresponds to a 90% confidence level, meaning that if the observed data yield Z ≥ 1.28 (see Fig.12), we can exclude the signal+background model at 90% confidence.

### References

- [1] K.S. Thorne, Gravitational Wave Research: Current Status and Future Prospects, Rev. Mod. Phys. 52 (1980) 285.
- [2] LIGO Scientific, Virgo collaboration, GW170817: Observation of Gravitational Waves from a Binary Neutron Star Inspiral, Phys. Rev. Lett. 119 (2017) 161101 [1710.05832].
- [3] LIGO Scientific, Virgo collaboration, Observation of Gravitational Waves from a Binary Black Hole Merger, Phys. Rev. Lett. 116 (2016) 061102 [1602.03837].
- [4] LIGO Scientific Collaboration, “LIGO Scientific Collaboration.” https://www.ligo.caltech.edu/page/ligo-scientific-collaboration.
- [5] LIGO Scientific, Virgo collaboration, GW190425: Observation of a Compact

Binary Coalescence with Total Mass ∼ 3.4M⊙, Astrophys. J. Lett. 892 (2020) L3 [2001.01761].

- [6] LIGO Scientific, Virgo collaboration, GW190814: Gravitational Waves from the Coalescence of a 23 Solar Mass Black Hole with a 2.6 Solar Mass Compact Object, Astrophys. J. Lett. 896 (2020) L44 [2006.12611].
- [7] LIGO Scientific, Virgo,, KAGRA, VIRGO collaboration, Observation of

Gravitational Waves from the Coalescence of a 2.5–4.5 M ⊙ Compact Object and a Neutron Star, Astrophys. J. Lett. 970 (2024) L34 [2404.04248].

- [8] M. Prunier, G. Morr´s, J.F.N.n. Siles, S. Clesse, J. Garcı´a-Bellido and E. Ruiz Morales, Analysis of the subsolar-mass black hole candidate SSM200308 from the second part of the third observing run of Advanced LIGO-Virgo, Phys. Dark Univ. 46 (2024) 101582 [2311.16085].
- [9] C.D. Bailyn, R.K. Jain, P. Coppi and J.A. Orosz, The Mass distribution of stellar black holes, Astrophys. J. 499 (1998) 367 [astro-ph/9708032].
- [10] F. Ozel, D. Psaltis, R. Narayan and J.E. McClintock, The Black Hole Mass Distribution in the Galaxy, Astrophys. J. 725 (2010) 1918 [1006.2834].
- [11] W.M. Farr, N. Sravan, A. Cantrell, L. Kreidberg, C.D. Bailyn, I. Mandel et al., The Mass Distribution of Stellar-Mass Black Holes, Astrophys. J. 741 (2011) 103 [1011.1459].
- [12] B. Carr and F. Kuhnel, Primordial Black Holes as Dark Matter: Recent Developments, Ann. Rev. Nucl. Part. Sci. 70 (2020) 355 [2006.02838].


- [13] M. Abramowicz, M. Bejger, A. Udalski and M. Wielgus, A Robust Test of the Existence of Primordial Black Holes in Galactic Dark Matter Halos, Astrophys. J. Lett. 935 (2022) L28 [2206.13335].
- [14] B. Dasgupta, R. Laha and A. Ray, Low Mass Black Holes from Dark Core Collapse, Phys. Rev. Lett. 126 (2021) 141105 [2009.01825].
- [15] D. Singh, M. Ryan, R. Magee, T. Akhter, S. Shandera, D. Jeong et al., Gravitational-wave limit on the Chandrasekhar mass of dark matter, Phys. Rev. D 104 (2021) 044015 [2009.05209].
- [16] J. Bramante and N. Raj, Dark matter in compact stars, Phys. Rept. 1052 (2024) 1 [2307.14435].
- [17] M. Cirelli, A. Strumia and J. Zupan, Dark Matter, 2406.01705.
- [18] C. Balazs, T. Bringmann, F. Kahlhoefer and M. White, A Primer on Dark Matter, 2411.05062.
- [19] A. Gould, Resonant Enhancements in WIMP Capture by the Earth, Astrophys. J. 321 (1987) 571.
- [20] A. Gould, Direct and Indirect Capture of Wimps by the Earth, Astrophys. J. 328

(1988) 919.

- [21] G. Bertone and M. Fairbairn, Compact Stars as Dark Matter Probes, Phys. Rev. D 77 (2008) 043515 [0709.1485].
- [22] S.D. McDermott, H.-B. Yu and K.M. Zurek, Constraints on Scalar Asymmetric Dark Matter from Black Hole Formation in Neutron Stars, Phys. Rev. D 85 (2012) 023519 [1103.5472].
- [23] C. Kouvaris, P. Tinyakov and M.H.G. Tytgat, NonPrimordial Solar Mass Black Holes, Phys. Rev. Lett. 121 (2018) 221102 [1804.06740].
- [24] A. Joglekar, N. Raj, P. Tanedo and H.-B. Yu, Relativistic capture of dark matter by electrons in neutron stars, Phys. Lett. B 809 (2020) 135767 [1911.13293].
- [25] B. Dasgupta, A. Gupta and A. Ray, Dark matter capture in celestial objects: light mediators, self-interactions, and complementarity with direct detection, JCAP 10

(2020) 023 [2006.10773].

- [26] N.F. Bell, G. Busoni, S. Robles and M. Virgato, Improved Treatment of Dark Matter Capture in Neutron Stars, JCAP 09 (2020) 028 [2004.14888].
- [27] J.F. Acevedo, J. Bramante, A. Goodman, J. Kopp and T. Opferkuch, Dark Matter, Destroyer of Worlds: Neutrino, Thermal, and Existential Signatures from Black Holes in the Sun and Earth, JCAP 04 (2021) 026 [2012.09176].
- [28] S. Bhattacharya, B. Dasgupta, R. Laha and A. Ray, Can LIGO Detect Nonannihilating Dark Matter?, Phys. Rev. Lett. 131 (2023) 091401 [2302.07898].
- [29] A. Ray, Celestial objects as strongly-interacting nonannihilating dark matter detectors, Phys. Rev. D 107 (2023) 083012 [2301.03625].
- [30] W.E. East and L. Lehner, Fate of a neutron star with an endoparasitic black hole and implications for dark matter, Phys. Rev. D 100 (2019) 124026 [1909.07968].


- [31] I. Goldman and S. Nussinov, Weakly Interacting Massive Particles and Neutron Stars, Phys. Rev. D 40 (1989) 3221.
- [32] R. Garani, Y. Genolini and T. Hambye, New Analysis of Neutron Star Constraints on Asymmetric Dark Matter, JCAP 05 (2019) 035 [1812.08773].
- [33] K. Dutta, D. Ghosh and B. Mukhopadhyaya, Improved treatment of bosonic dark matter dynamics in neutron stars: consequences and constraints, JCAP 12 (2024) 053 [2408.16091].
- [34] N. Liu and A.K. Mishra, Neutron star collapse from accretion: A probe of massive dark matter particles, Phys. Dark Univ. 47 (2025) 101740 [2408.00594].
- [35] KAGRA, VIRGO, LIGO Scientific collaboration, Population of Merging Compact Binaries Inferred Using Gravitational Waves through GWTC-3, Phys. Rev. X 13 (2023) 011048 [2111.03634].
- [36] E. Giangrandi, H. Rueter, N. Kunert, M. Emma, A. Abac, A. Adhikari et al., Numerical Relativity Simulations of Dark Matter Admixed Binary Neutron Stars, 2504.20825.
- [37] S. Mukherjee, P.S. Aswathi, C. Singha and A. Ganguly, Bose-Einstein Condensate Dark Matter in the Core of Neutron Stars: Implications for Gravitational-wave Observations, 2506.22353.
- [38] S. Shirke, S. Ghosh, D. Chatterjee, L. Sagunski and J. Schaffner-Bielich, R-modes as a new probe of dark matter in neutron stars, JCAP 12 (2023) 008 [2305.05664].
- [39] S. Shirke, B.K. Pradhan, D. Chatterjee, L. Sagunski and J. Schaffner-Bielich, Effects of dark matter on f-mode oscillations of neutron stars, Phys. Rev. D 110 (2024) 063025 [2403.18740].
- [40] G.-L. Li, Y. Tang and Y.-L. Wu, Probing dark matter spikes via gravitational waves of extreme-mass-ratio inspirals, Sci. China Phys. Mech. Astron. 65 (2022) 100412 [2112.14041].
- [41] P.S. Cole, A. Coogan, B.J. Kavanagh and G. Bertone, Measuring dark matter spikes around primordial black holes with Einstein Telescope and Cosmic Explorer, Phys. Rev. D 107 (2023) 083006 [2207.07576].
- [42] T.K. Karydas, B.J. Kavanagh and G. Bertone, Sharpening the dark matter signature in gravitational waveforms. I. Accretion and eccentricity evolution, Phys. Rev. D 111

(2025) 063070 [2402.13053].

- [43] B.J. Kavanagh, T.K. Karydas, G. Bertone, P. Di Cintio and M. Pasquato, Sharpening the dark matter signature in gravitational waveforms. II. Numerical simulations, Phys. Rev. D 111 (2025) 063071 [2402.13762].
- [44] A. Pierce, K. Riles and Y. Zhao, Searching for Dark Photon Dark Matter with Gravitational Wave Detectors, Phys. Rev. Lett. 121 (2018) 061102 [1801.10161].
- [45] S. Morisaki and T. Suyama, Detectability of ultralight scalar field dark matter with gravitational-wave detectors, Phys. Rev. D 100 (2019) 123512 [1811.05003].
- [46] S. Bhattacharya, A.L. Miller and A. Ray, Continuous gravitational waves: A new window to look for heavy nonannihilating dark matter, Phys. Rev. D 110 (2024) 043006 [2403.13886].


- [47] D. Singh, A. Gupta, E. Berti, S. Reddy and B.S. Sathyaprakash, Constraining properties of asymmetric dark matter candidates from gravitational-wave observations, Phys. Rev. D 107 (2023) 083037 [2210.15739].
- [48] M. Sasaki, T. Suyama, T. Tanaka and S. Yokoyama, Primordial Black Hole Scenario for the Gravitational-Wave Event GW150914, Phys. Rev. Lett. 117 (2016) 061101 [1603.08338].
- [49] S. Bird, I. Cholis, J.B. Mun˜oz, Y. Ali-Haı¨moud, M. Kamionkowski, E.D. Kovetz et al., Did LIGO detect dark matter?, Phys. Rev. Lett. 116 (2016) 201301 [1603.00464].
- [50] LIGO Scientific, Virgo collaboration, Search for Subsolar Mass Ultracompact Binaries in Advanced LIGO’s Second Observing Run, Phys. Rev. Lett. 123 (2019) 161102 [1904.08976].
- [51] V. De Luca, V. Desjacques, G. Franciolini, P. Pani and A. Riotto, GW190521 Mass Gap Event and the Primordial Black Hole Scenario, Phys. Rev. Lett. 126 (2021) 051101 [2009.01728].
- [52] K. Kadota, J.H. Kim, P. Ko and X.-Y. Yang, Gravitational wave probes on self-interacting dark matter surrounding an intermediate mass black hole, Phys. Rev. D 109 (2024) 015022 [2306.10828].
- [53] C. Han, K.-P. Xie, J.M. Yang and M. Zhang, Self-interacting dark matter implied by nano-Hertz gravitational waves, Phys. Rev. D 109 (2024) 115025 [2306.16966].
- [54] G. Bertone et al., Gravitational wave probes of dark matter: challenges and opportunities, SciPost Phys. Core 3 (2020) 007 [1907.10610].
- [55] M. Saleem, A. Pai, K. Misra, L. Resmi and K.G. Arun, Rates of Short-GRB afterglows in association with Binary Neutron Star mergers, Mon. Not. Roy. Astron. Soc. 475 (2018) 699 [1710.06111].
- [56] G. Stratta and A. Santangelo, X- and Gamma-ray astrophysics in the era of Multi-messenger astronomy, 2205.10774.
- [57] M. Nicholl and I. Andreoni, Electromagnetic follow-up of gravitational waves: review and lessons learned, Phil. Trans. Roy. Soc. Lond. A 383 (2025) 20240126 [2410.18274].
- [58] M. Fishbach, R. Essick and D.E. Holz, Does Matter Matter? Using the mass distribution to distinguish neutron stars and black holes, Astrophys. J. Lett. 899

(2020) L8 [2006.13178].

- [59] R. Essick and P. Landry, Discriminating between Neutron Stars and Black Holes with Imperfect Knowledge of the Maximum Neutron Star Mass, Astrophys. J. 904 (2020) 80 [2007.01372].
- [60] S. Datta, K.S. Phukon and S. Bose, Recognizing black holes in gravitational-wave observations: Challenges in telling apart impostors in mass-gap binaries, Phys. Rev. D 104 (2021) 084006 [2004.05974].
- [61] A.M. Farah, M. Fishbach, R. Essick, D.E. Holz and S. Galaudage, Bridging the Gap: Categorizing Gravitational-wave Events at the Transition between Neutron Stars and Black Holes, Astrophys. J. 931 (2022) 108 [2111.03498].


- [62] S. Mukherjee, S. Datta, S. Tiwari, K.S. Phukon and S. Bose, Toward establishing the presence or absence of horizons in coalescing binaries of compact objects by using their gravitational wave signals, Phys. Rev. D 106 (2022) 104032 [2202.08661].
- [63] S. Mukherjee, K.S. Phukon, S. Datta and S. Bose, Phenomenological gravitational waveform model of binary black holes incorporating horizon fluxes, Phys. Rev. D 110

(2024) 124027 [2311.17554].

- [64] F. Crescimbeni, G. Franciolini, P. Pani and M. Vaglio, Cosmology and nuclear-physics implications of a subsolar gravitational-wave event, 2408.14287.
- [65] V. De Luca, G. Franciolini and A. Riotto, Flea on the elephant: Tidal Love numbers in subsolar primordial black hole searches, Phys. Rev. D 110 (2024) 104041 [2408.14207].
- [66] F. Crescimbeni, G. Franciolini, P. Pani and A. Riotto, Can we identify primordial black holes? Tidal tests for subsolar-mass gravitational-wave observations, Phys. Rev. D 109 (2024) 124063 [2402.18656].
- [67] J. Golomb, I. Legred, K. Chatziioannou, A. Abac and T. Dietrich, Using equation of state constraints to classify low-mass compact binary mergers, Phys. Rev. D 110

(2024) 063014 [2403.07697].

- [68] J.M. Lattimer and M. Prakash, Neutron star structure and the equation of state, Astrophys. J. 550 (2001) 426 [astro-ph/0002232].
- [69] G.F. Burgio, H.J. Schulze, I. Vidana and J.B. Wei, Neutron stars and the nuclear equation of state, Prog. Part. Nucl. Phys. 120 (2021) 103879 [2105.03747].
- [70] M. Maggiore, Gravitational Waves. Vol. 1: Theory and Experiments, Oxford University Press (2007), 10.1093/acprof:oso/9780198570745.001.0001.
- [71] LIGO Scientific collaboration, Advanced LIGO, Class. Quant. Grav. 32 (2015) 074001 [1411.4547].
- [72] K. Ackley et al., Neutron Star Extreme Matter Observatory: A kilohertz-band gravitational-wave detector in the global network, Publ. Astron. Soc. Austral. 37

(2020) e047 [2007.03128].

- [73] D. Reitze et al., Cosmic Explorer: The U.S. Contribution to Gravitational-Wave Astronomy beyond LIGO, Bull. Am. Astron. Soc. 51 (2019) [1907.04833].
- [74] M. Punturo et al., The Einstein Telescope: A third-generation gravitational wave observatory, Class. Quant. Grav. 27 (2010) 194002.
- [75] S. Husa, S. Khan, M. Hannam, M. Pu¨rrer, F. Ohme, X. Jime´nez Forteza et al., Frequency-domain gravitational waves from nonprecessing black-hole binaries. I. New numerical waveforms and anatomy of the signal, Phys. Rev. D 93 (2016) 044006 [1508.07250].
- [76] S. Khan, S. Husa, M. Hannam, F. Ohme, M. Pu¨rrer, X. Jime´nez Forteza et al., Frequency-domain gravitational waves from nonprecessing black-hole binaries. II. A phenomenological model for the advanced detector era, Phys. Rev. D 93 (2016) 044007 [1508.07253].
- [77] S.A. Hughes, A. Apte, G. Khanna and H. Lim, Learning about black hole binaries from their ringdown spectra, Phys. Rev. Lett. 123 (2019) 161101 [1901.05900].


- [78] E. Berti, V. Cardoso and A.O. Starinets, Quasinormal modes of black holes and black branes, Class. Quant. Grav. 26 (2009) 163001 [0905.2975].
- [79] A. Nitz, I. Harry, D. Brown, C.M. Biwer, J. Willis, T.D. Canton et al., gwastro/pycbc: v2.3.3 release of PyCBC, Jan., 2024. 10.5281/zenodo.10473621.
- [80] Core Database Official Website, “Core Database Official Website.” http://www.computational-relativity.org/.
- [81] F. Ozel¨ and P. Freire, Masses, Radii, and the Equation of State of Neutron Stars, Ann. Rev. Astron. Astrophys. 54 (2016) 401 [1603.02698].
- [82] R. Dudi, T. Dietrich, A. Rashti, B. Bruegmann, J. Steinhoff and W. Tichy, High-accuracy simulations of highly spinning binary neutron star systems, Phys. Rev. D 105 (2022) 064050 [2108.10429].
- [83] A. Samajdar and T. Dietrich, Waveform systematics for binary neutron star gravitational wave signals: effects of the point-particle baseline and tidal descriptions, Phys. Rev. D 98 (2018) 124030 [1810.03936].
- [84] A. Samajdar and T. Dietrich, Waveform systematics for binary neutron star gravitational wave signals: Effects of spin, precession, and the observation of electromagnetic counterparts, Phys. Rev. D 100 (2019) 024046 [1905.03118].
- [85] T. Dietrich, S. Bernuzzi and W. Tichy, Closed-form tidal approximants for binary neutron star gravitational waveforms constructed from high-resolution numerical relativity simulations, Phys. Rev. D 96 (2017) 121501 [1706.02969].
- [86] T. Dietrich, T. Hinderer and A. Samajdar, Interpreting Binary Neutron Star Mergers: Describing the Binary Neutron Star Dynamics, Modelling Gravitational Waveforms, and Analyzing Detections, Gen. Rel. Grav. 53 (2021) 27 [2004.02527].
- [87] T. Dietrich, D. Radice, S. Bernuzzi, F. Zappa, A. Perego, B. Br¨ugmann et al., CoRe database of binary neutron star merger waveforms, Class. Quant. Grav. 35 (2018) 24LT01 [1806.01625].
- [88] A. Gonzalez et al., Second release of the CoRe database of binary neutron star merger waveforms, Class. Quant. Grav. 40 (2023) 085011 [2210.16366].
- [89] B. Bruegmann, J.A. Gonzalez, M. Hannam, S. Husa, U. Sperhake and W. Tichy, Calibration of Moving Puncture Simulations, Phys. Rev. D 77 (2008) 024027 [gr-qc/0610128].
- [90] M. Thierfelder, S. Bernuzzi and B. Bruegmann, Numerical relativity simulations of binary neutron stars, Phys. Rev. D 84 (2011) 044012 [1104.4751].
- [91] D. Radice and L. Rezzolla, THC: a new high-order finite-difference high-resolution shock-capturing code for special-relativistic hydrodynamics, Astron. Astrophys. 547

(2012) A26 [1206.6502].

- [92] T. Damour and A. Nagar, Effective One Body description of tidal effects in inspiralling compact binaries, Phys. Rev. D 81 (2010) 084016 [0911.5041].
- [93] M. Favata, Systematic parameter errors in inspiraling neutron star binaries, Phys. Rev. Lett. 112 (2014) 101101 [1310.8288].
- [94] J.S. Read, B.D. Lackey, B.J. Owen and J.L. Friedman, Constraints on a


phenomenologically parameterized neutron-star equation of state, Phys. Rev. D 79

(2009) 124032 [0812.2163].

- [95] J.M. Lattimer, The nuclear equation of state and neutron star masses, Ann. Rev. Nucl. Part. Sci. 62 (2012) 485 [1305.3510].
- [96] M. Alford, M. Braby, M.W. Paris and S. Reddy, Hybrid stars that masquerade as neutron stars, Astrophys. J. 629 (2005) 969 [nucl-th/0411016].
- [97] S. Banik, M. Hempel and D. Bandyopadhyay, New Hyperon Equations of State for Supernovae and Neutron Stars in Density-dependent Hadron Field Theory, Astrophys. J. Suppl. 214 (2014) 22 [1404.6173].
- [98] J.M. Lattimer and F.D. Swesty, A Generalized equation of state for hot, dense matter, Nucl. Phys. A 535 (1991) 331.
- [99] M. Breschi, S. Bernuzzi, F. Zappa, M. Agathos, A. Perego, D. Radice et al., kiloHertz gravitational waves from binary neutron star remnants: time-domain model and constraints on extreme matter, Phys. Rev. D 100 (2019) 104029 [1908.11418].
- [100] A. Vijaykumar, S.J. Kapadia and P. Ajith, Can a binary neutron star merger in the vicinity of a supermassive black hole enable a detection of a post-merger gravitational wave signal?, Mon. Not. Roy. Astron. Soc. 513 (2022) 3577 [2202.08673].
- [101] S. Bernuzzi, A. Nagar, S. Balmelli, T. Dietrich and M. Ujevic, Quasiuniversal properties of neutron star mergers, Phys. Rev. Lett. 112 (2014) 201101 [1402.6244].
- [102] L.A. Wainstein and V.D. Zubakov, Extraction of Signals from Noise, Prentice-Hall

(1970).

- [103] J.D.E. Creighton and W.G. Anderson, Gravitational-wave Physics and Astronomy: An Introduction to Theory, Experiment and Data Analysis, Wiley-VCH (2011).
- [104] C. Cutler and E.E. Flanagan, Gravitational waves from merging compact binaries: How accurately can one extract the binary’s parameters from the inspiral wave form?, Phys. Rev. D 49 (1994) 2658 [gr-qc/9402014].
- [105] L.S. Finn, Detection, measurement and gravitational radiation, Phys. Rev. D 46

(1992) 5236 [gr-qc/9209010].

- [106] N. Cornish, L. Sampson, N. Yunes and F. Pretorius, Gravitational Wave Tests of General Relativity with the Parameterized Post-Einsteinian Framework, Phys. Rev. D 84 (2011) 062003 [1105.2088].
- [107] B.J. Owen, Search templates for gravitational waves from inspiraling binaries: Choice of template spacing, Phys. Rev. D 53 (1996) 6749 [gr-qc/9511032].
- [108] S.V. Dhurandhar and B.S. Sathyaprakash, Choice of filters for the detection of gravitational waves from coalescing binaries. 2. Detection in colored noise, Phys. Rev. D 49 (1994) 1707.
- [109] D. Radice, A. Perego, K. Hotokezaka, S.A. Fromm, S. Bernuzzi and L.F. Roberts, Binary Neutron Star Mergers: Mass Ejection, Electromagnetic Counterparts and Nucleosynthesis, Astrophys. J. 869 (2018) 130 [1809.11161].
- [110] A. Bauswein, T.W. Baumgarte and H.T. Janka, Prompt merger collapse and the maximum mass of neutron stars, Phys. Rev. Lett. 111 (2013) 131101 [1307.5191].


- [111] K. Hotokezaka, K. Kyutoku, H. Okawa, M. Shibata and K. Kiuchi, Binary Neutron Star Mergers: Dependence on the Nuclear Equation of State, Phys. Rev. D 83 (2011) 124008 [1105.4370].
- [112] M. Evans et al., A Horizon Study for Cosmic Explorer: Science, Observatories, and Community, 2109.09882.
- [113] A. Abac et al., The Science of the Einstein Telescope, 2503.12263.
- [114] S.R. Taylor and J.R. Gair, Cosmology with the lights off: standard sirens in the Einstein Telescope era, Phys. Rev. D 86 (2012) 023502 [1204.6739].
- [115] R. O’Shaughnessy, V. Kalogera and K. Belczynski, Binary Compact Object Coalescence Rates: The Role of Elliptical Galaxies, Astrophys. J. 716 (2010) 615 [0908.3635].
- [116] R.W. O’Shaughnessy, V. Kalogera and K. Belczynski, Short Gamma-Ray Bursts and Binary Mergers in Spiral and Elliptical Galaxies: Redshift Distribution and Hosts, Astrophys. J. 675 (2008) 566 [0706.4139].
- [117] J.A. de Freitas Pacheco, The NS NS coalescence rate in galaxies and its significance to the VIRGO gravitational antenna, Astropart. Phys. 8 (1997) 21.
- [118] P. Madau and M. Dickinson, Cosmic Star Formation History, Ann. Rev. Astron. Astrophys. 52 (2014) 415 [1403.0007].
- [119] S.R. Taylor, J.R. Gair and I. Mandel, Hubble without the Hubble: Cosmology using advanced gravitational-wave detectors alone, Phys. Rev. D 85 (2012) 023535 [1108.5161].
- [120] Planck collaboration, Planck 2018 results. VI. Cosmological parameters, Astron. Astrophys. 641 (2020) A6 [1807.06209].
- [121] L.S. Finn, Binary inspiral, gravitational radiation, and cosmology, Phys. Rev. D 53

(1996) 2878 [gr-qc/9601048].

- [122] Particle Data Group collaboration, Review of particle physics, Phys. Rev. D 110

(2024) 030001.

- [123] G. Cowan, K. Cranmer, E. Gross and O. Vitells, Asymptotic formulae for likelihood-based tests of new physics, Eur. Phys. J. C 71 (2011) 1554 [1007.1727].
- [124] S. Bhattacharya, Gravitational Waves as a Probe of Particle Dark Matter, 12, 2024 [2412.02453].
- [125] N. Aggarwal et al., Challenges and Opportunities of Gravitational Wave Searches above 10 kHz, 2501.11723.
- [126] R. Harada, K. Cannon, K. Hotokezaka and K. Kyutoku, Testability of the quark-hadron transition using gravitational waves from merging binary neutron stars, Phys. Rev. D 110 (2024) 123005 [2310.13603].
- [127] S. Khadkikar and D. Singh, A case study of GW190425 for classifying binary neutron star versus binary black hole mergers and constraining asymmetric dark matter with gravitational wave detectors, 2507.07895.
- [128] The HDF Group, “Hdf5: Data model, library, and file format.” https://www.hdfgroup.org/solutions/hdf5/.


- [129] h5py Developers, “h5py: Python interface to hdf5.” https://docs.h5py.org/en/stable/index.html.
- [130] T. Damour, A. Nagar, D. Pollney and C. Reisswig, Energy versus Angular Momentum in Black Hole Binaries, Phys. Rev. Lett. 108 (2012) 131101 [1110.2938].
- [131] J.W. van Holten, Curvature Dynamics in General Relativity, Universe 9 (2023) 110 [2211.10123].
- [132] F. Douchin and P. Haensel, A unified equation of state of dense matter and neutron star structure, Astron. Astrophys. 380 (2001) 151 [astro-ph/0111092].
- [133] A.S. Schneider, L.F. Roberts and C.D. Ott, Open-source nuclear equation of state framework based on the liquid-drop model with Skyrme interaction, Phys. Rev. C 96


(2017) 065802 [1707.01527].

