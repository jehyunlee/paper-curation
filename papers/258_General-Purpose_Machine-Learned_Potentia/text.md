# arXiv:2603.25616v1[cond-mat.mtrl-sci]26 Mar 2026

## General-Purpose Machine-Learned Potential for CrCoNi Alloys Enabling Large-Scale Atomistic Simulations with First-Principles Accuracy

Yong-Chao Wu,∗ Tero M¨kinen, and Mikko Alava

Aalto University, Department of Applied Physics, PO Box 11000, 00076 Aalto, Espoo, Finland

Amin Esfandiarpour†

NOMATEN Centre of Excellence, National Center for Nuclear Research, A. Soltana 7 St., 05-400 Otwock, Poland (Dated: March 27, 2026)

CrCoNi medium-entropy alloys exhibit exceptional mechanical properties arising from pronounced chemical complexity, including short-range order (SRO), and low stacking fault energy, posing challenges for large-scale atomistic simulations. While most models focus on equimolar compositions, deviations from equimolarity provide an effective route to tuning properties, requiring transferable interatomic potentials that capture composition-dependent behavior. Here we develop a generalpurpose machine-learned interatomic potential for the CrCoNi system within the neuroevolution potential (NEP) framework, achieving near first-principles accuracy with high computational efficiency. Trained on a comprehensive dataset spanning pure elements, binary and ternary alloys across a wide compositional range, diverse crystal structures and thermodynamic conditions, and based on spin-polarized ab initio data, the model accurately reproduces equations of state, phonons, elastic constants, dislocation dissociation, surface and defect energies, melting temperatures and strain-induced phase transformations. It further captures SRO and its effect on stacking fault energies across both equimolar and non-equimolar compositions, in agreement with first-principles and experiments. In contrast to existing potentials, typically limited to equimolar alloys and less accurate for pure elements, the present model delivers consistent accuracy across the full compositional space while retaining superior efficiency. These results enable reliable atomistic simulations of composition-dependent behaviour and provide a framework for the design of non-equimolar CrCoNi alloys.

#### I. INTRODUCTION

High- and medium-entropy alloys (H/MEAs) have attracted significant attention in recent years due to their vast compositional design space and their potential to exhibit exceptional mechanical and physical properties [1–3]. Among these systems, the CrCoNi alloy has emerged as a model material because of its outstanding mechanical performance, including exceptional strength, ductility, and fracture toughness over a wide temperature range, from cryogenic to ambient conditions [4, 5]. In addition, experiments involving dynamic impact, laser shock, and irradiation have demonstrated its remarkable resistance to damage, impact loading, and radiation-induced defects [6–8]. These exceptional properties originate from the interplay of multiple deformation mechanisms, including dislocation slip, deformation twinning, and strain-induced phase transformation from face-centered cubic (FCC) to hexagonal close-packed (HCP) structures [5, 6, 9]. The activation of these mechanisms is highly sensitive to temperature and the local chemical environment, which influence the relative stability of competing phases [10]. In particular, chemical short-range order (SRO) has been identified as a key factor governing stacking fault energy (SFE), dislocation behavior, and phase stability, thereby strongly affecting the overall mechanical response [11, 12].

Beyond equiatomic compositions, recent studies have demonstrated that deviations from equimolar or nearequimolar ratios provide an effective strategy for further enhancing mechanical properties. In particular, nonequimolar CrCoNi alloys have been shown to achieve significantly higher strength while maintaining excellent ductility. For example, Coury et al. reported that a Cr45Co27.5Ni27.5 alloy exhibits a yield strength more than 50% higher than that of equimolar CrCoNi, with comparable ductility [13]. Similar observations have been reported in subsequent studies, highlighting the critical role of composition in tuning phase stability, SFE, and deformation mechanisms [14]. These findings indicate that the vast compositional space of CrCoNi alloys offers substantial opportunities for materials design beyond the equimolar limit. However, understanding and predicting composition-dependent behavior at the atomistic scale remain major challenges. Despite extensive efforts, the fundamental atomistic origins of deformation and strengthening mechanisms in CrCoNi alloys remain incompletely understood. A notable discrepancy persists between theoretical predictions and experimental measurements of SFE: density functional theory (DFT) calculations

∗ Contact author: yongchao.wu@aalto.fi † Contact author: amin.esfandiarpour@ncbj.gov.pl

typically predict negative values, whereas experiments report positive values [12]. Whether this inconsistency arises from the presence of SRO [12], strong solute–dislocation interactions [15], or other factors remains under active debate. Moreover, the role of SRO in strengthening, whether it enhances [12] or has negligible effects [16, 17], has not yet reached a consensus. Large-scale atomistic simulations provide a powerful approach for probing the nanoscale chemical environment and revealing the atomic origins of the exceptional mechanical properties. Although quantummechanical methods such as DFT offer high accuracy, their application is limited to relatively small system sizes and short time scales. In contrast, classical molecular dynamics (MD) and Monte Carlo (MC) methods are significantly more computationally efficient but rely critically on the accuracy of interatomic potentials. For metallic systems, the embedded-atom method (EAM) [18] and the modified embedded-atom method (MEAM) [19] have been widely used over the past decades, particularly for elemental metals and their alloys. However, these empirical potentials often lack the accuracy required to reliably describe complex chemical interactions due to their constrained functional forms.

Recently, machine-learning interatomic potentials (MLPs) [20, 21] have emerged as a promising alternative. In MLPs, the potential energy surface is represented using flexible machine-learning models, enabling the use of a substantially larger number of fitting parameters compared with traditional many-body potentials. Freed from rigid analytical functional forms, MLPs can achieve significantly improved accuracy and transferability across diverse atomic configurations. A machine-learning potential based on the Moment Tensor Potential (MTP) [22, 23] framework has recently been developed for the CoCrNi system [24]. While this model demonstrates good performance for equimolar ternary alloys, its applicability remains largely restricted to near-equimolar compositions and does not provide reliable accuracy for the constituent unary elements or for compositionally off-equimolar alloys. This limitation hinders its use in predictive simulations aimed at exploring composition-dependent properties and designing non-equimolar alloys. In addition, the computational cost of MLP is still significantly higher than that of traditional empirical potentials, which can limit its application in large-scale simulations. To the best of our knowledge, a transferable and computationally efficient MLP capable of accurately describing both unary elements and the full CrCoNi compositional space, including non-equimolar alloys, is still lacking.

In this work, we develop a general-purpose machine-learning potential for the CrCoNi system based on the neuroevolution potential (NEP) [25, 26] framework. The proposed model is trained on a diverse dataset spanning unary, binary, and ternary configurations, enabling accurate reproduction of key structural, thermodynamic, and mechanical properties across the compositional space. Importantly, the dataset explicitly includes non-equimolar compositions, ensuring transferability beyond the equiatomic limit. Comprehensive benchmarking demonstrates that the present model outperforms widely used empirical potentials and existing MLPs while maintaining high computational efficiency suitable for large-scale atomistic simulations. This enables predictive simulations of composition-dependent properties across the full CrCoNi compositional space.

#### II. RESULTS

In this section, we evaluate the performance of the NEP model with respect to several key properties. For comparison, we consider several representative classical interatomic potentials, including two EAM potentials developed by Li et al. [27] (denoted as EAM1) and Farkas et al. [28] (denoted as EAM2), as well as a MEAM potential developed by Choi et al. [29]. These empirical potentials have been widely used in previous studies to investigate the mechanical properties of CrCoNi alloys [30–35]. In addition, a recently developed MTP model (TS-f version, as recommended) by Cao et al. [24] is included as a representative example of modern machine-learning interatomic potentials.

A. Energy, force and stress validation

We first evaluate the predictive performance of these potentials for energies, forces, and stresses using three datasets: the NEP training dataset, the MTP dataset, and an independently prepared validation dataset. The NEP dataset contains 3030 diverse atomic configurations, while the MTP dataset contains 5798 structures. The validation dataset was generated from 2 ns MD simulations conducted over a temperature range from 5 to 3000 K using seven different initial structures. Detailed procedures for dataset generation are provided in the Methods section. As shown in Fig. 1, NEP exhibits the best overall agreement with DFT results for energies, forces, and stresses across all three datasets, indicating excellent transferability and high accuracy. MTP also demonstrates good accuracy in force prediction but shows relatively poor performance in describing stresses. Interestingly, MTP correctly predicts the energies for only a portion of the dataset, primarily corresponding to CrCoNi ternary alloy structures, while exhibiting large discrepancies under other conditions. In contrast, all empirical potentials show significant deviations from the DFT results. The root mean square errors (RMSEs) of the various potentials are summarized in Table I. For force prediction, NEP

achieves the lowest RMSE values across all datasets: 106.1 meV/˚A on the NEP dataset, 144.04 meV/˚A on the MTP dataset, and 121.41 meV/˚A on the validation dataset. MTP exhibits a comparable force prediction performance on the MTP dataset (144.77 meV/˚A), but shows larger RMSE values on the NEP dataset (153.76 meV/˚A) and the validation dataset (192.41 meV/˚A) compared with NEP. Among the empirical potentials, EAM1 provides the best force prediction performance, followed by EAM2 and MEAM across all datasets.

![image 1](Wu et al._2026_General-Purpose Machine-Learned Potential for CrCoNi Alloys Enabling Large-Scale Atomistic Simulatio_images/imageFile1.png)

- FIG. 1. Pairwise comparisons of energies, forces, and stresses for the (a) NEP training dataset, (b) MTP dataset [24], and (c) validation dataset, as predicted by NEP, EAM1 [27], EAM2 [28], MEAM [29], and MTP [24]. (d) Principal component analysis (PCA) of the dataset based on NEP descriptors, where each point represents an individual atomic configuration.


To further analyze the structural diversity of the datasets, principal component analysis (PCA) was applied to reduce the dimensionality of the NEP descriptor space for the three datasets. The first two principal components account for 97% of the explained variance, indicating that they capture the dominant structural features of the datasets. As illustrated in Fig. 1d, the NEP dataset exhibits a broader and more uniform distribution in descriptor space, indicating greater structural diversity. In contrast, the MTP dataset is mainly concentrated near the corners

- TABLE I. Root Mean Square Error (RMSE) of energy (meV/atom), force (meV/˚A), and stress (GPa) predicted by EAM1 [27], EAM2 [28], MEAM [29], MTP [24], and NEP on the NEP, MTP, and validation datasets.


Potential NEP Dataset MTP Dataset Validation Dataset Energy Force Stress Energy Force Stress Energy Force Stress

EAM1 3154.27 419.86 9.55 3087.76 699.59 7.63 3283.37 453.48 7.91 EAM2 3134.91 728.65 5.82 3142.17 1085.47 5.26 3316.21 829.59 4.88 MEAM 3192.76 800.29 4.41 3189.40 1125.57 5.03 3356.37 988.00 5.06 MTP 775.41 153.76 5.74 547.57 144.77 2.39 866.23 192.41 0.72 NEP 2.45 106.10 0.39 10.65 144.04 0.64 3.10 121.41 0.42

and central regions, lacking configurations corresponding to non-equiatomic ternary alloys, despite having a larger total number of structures than the NEP dataset.

B. Basic crystal properties

We next evaluate the fundamental physical properties of the elemental metals and the ternary CrCoNi alloy to further assess the accuracy of the developed NEP model. Fig. 2 shows the energy–volume (equation of state, EOS) curves for body centered cubic (BCC) Cr, HCP Co, FCC Ni, and equiatomic CrCoNi MEA obtained from interatomic potentials and DFT calculations. For the elemental metals, 2 × 2 × 2 primitive supercells are used, while a 3 × 3 × 3 conventional supercell is employed for the CrCoNi alloy. The energies and volumes are reported per atom, and identical atomic structures are used in both the potential-based calculations and the DFT reference to ensure a consistent comparison. Except for NEP, the energy curves of all other potentials have been shifted so that their minimum energies coincide with the DFT minimum. The NEP predictions show excellent agreement with DFT across the entire volume range examined, corresponding to volumetric strains of ±10%. Accurate EOS curves are essential for describing the mechanical response of materials under a wide range of volumetric strains and pressures. While all interatomic potentials reproduce the EOS of Ni reasonably well and show relatively small deviations for CrCoNi, noticeable discrepancies are observed for Cr and Co when using empirical potentials and MTP, particularly under compression. These results indicate the limited capability of these potentials in accurately describing the EOS of the elemental metals.

Fig. 3 compares the phonon dispersion relations of the elemental metals obtained from interatomic potentials and DFT calculations, together with available experimental data, to characterize lattice vibrational properties. The phonon spectra are computed using the finite-displacement method [36] along high-symmetry directions in the Brillouin zone. The NEP results agree well with both DFT and experimental data for all three elemental metals, with only minor deviations observed for the optical phonon branches of Co. In contrast, other potentials show significant discrepancies for BCC Cr and HCP Co. In particular, EAM2 predicts imaginary phonon frequencies, indicating dynamical instability, as shown in Fig. 3d. Most potentials reproduce the phonon dispersions of Ni reasonably well; however, MEAM and MTP exhibit noticeable deviations in the high-frequency region (Fig. 3f). Overall, NEP provides the most accurate description of the phonon dispersions among the considered potentials.

We further compare several key crystal properties of the elemental metals and the ternary alloy, including the lattice parameter (a), elastic constants (Cij), surface formation energy (Es), and vacancy formation energy (Evf), as summarized in Table II. Relative errors exceeding 25% with respect to the DFT reference values are highlighted. All properties predicted by NEP fall within this threshold, demonstrating consistently high accuracy. In contrast, 8, 10, 10, and 7 properties predicted by EAM1, EAM2, MEAM, and MTP, respectively, exhibit errors larger than 25%. All potentials predict equilibrium lattice constants that are comparable to the DFT and experimental values. For the surface energies of Ni and Co, all models give results consistent with DFT and correctly indicate that the {111} closepacked plane has the lowest surface energy in Ni, while {10¯10} corresponds to the highest surface energy in Co. In contrast, EAM2, MEAM, and MTP significantly underestimate the surface energy of Cr. Most potentials reasonably reproduce the vacancy formation energies of Ni and Co, while they generally underestimate this property in Cr. Notably, NEP also accurately reproduces the low-index grain boundary energies of Ni, predicting Σ3[1¯10](111) as the lowest grain boundary energy, consistent with most experimental observations [40]. No grain boundary structures were included in the NEP training dataset, indicating strong transferability. In contrast, empirical potentials systematically overestimate the Σ3[1¯10](112) grain boundary energy, while MTP even predicts a negative value for the Σ3[1¯10](111) boundary. Additionally, all potentials yield reasonable intrinsic stacking fault energies (γisf) for Ni except MTP, which predicts a negative γisf, far from the DFT and experimental values. All empirical potentials also overestimate the unstable stacking fault energy (γusf) of Ni. These results suggest that the empirical potentials and MTP are

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


3 3

##### FIG. 2. Energyatomic volume relations for (a) BCC Cr, (b) HCP Co, (c) FCC Ni, and (d) CrCoNi alloy, as obtained fromDFT, NEP, EAM1 [27], EAM2 [28], MEAM [29], and MTP [24] calculations.

| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |


| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |


| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |


| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |


| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |


| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |


##### FIG. 3. Phonon dispersions of (a) BCC Cr, (b) HCP Co, and (c) FCC Ni calculated using DFT, NEP, and experimentaldata. The corresponding comparisons with EAM1 [27], EAM2 [28], MEAM [29], and MTP [24] are shown in (d)(f) for clarity.Experimental data for BCC Cr [37], HCP Co [38], and FCC Ni [39], obtained from room-temperature neutron diffractionmeasurements, are included for comparison.

- TABLE II. Comparison of fundamental crystal properties for FCC Ni, BCC Cr, HCP Co, and equiatomic FCC CrCoNi alloy obtained from density functional theory (DFT), experiment (Exp.), and predicted by EAM1 [27], EAM2 [28], MEAM [29], MTP [24], and NEP. These properties include the lattice parameter (a), elastic constants (Cij), surface formation energy (Es), vacancy formation energy (Evf), low-index grain boundary energy, intrinsic stacking fault energy (γisf), and unstable stacking fault energy (γusf). Relative errors exceeding 25% with respect to the DFT reference values are marked. DFT results from this work are used as the primary reference; when unavailable, DFT values from the literature are adopted.


Property DFT DFT (other works) Exp. NEP EAM1 EAM2 MEAM MTP FCC Ni a (˚A) 3.52 3.52 [41] 3.52 [42] 3.52 3.52 3.52 3.52 3.51

- C11 (GPa) 276 276 [41] 261 [41] 281 257 255 261 253
- C12 (GPa) 158 156 [41] 151 [41] 162 151 151 151 163 C44 (GPa) 129 131 [41] 132 [41] 124 122 134 132 110


Es{100} (J/m2) 2.27 2.24 [41] - 2.22 2.20 1.88 1.94 1.76

- Es{110} (J/m2) 2.30 2.34 [41] - 2.28 2.39 2.05 2.04 1.86
- Es{111} (J/m2) 1.98 1.92 [41] - 1.99 2.03 1.63 1.60 1.57 Evf (eV) - 1.42 [41] 1.4–1.8 [43] 1.46 1.93(+35.9%) 1.60 1.51 1.38


- Σ3[1¯10](111) (mJ/m2) - 68 [41] - 52 80 63 63 -23(−133.8%)
- Σ3[1¯10](112) (mJ/m2) - 896 [41] - 1029 1171(+30.7%) 1236(+37.9%) 1200(+33.9%) 872 Σ5[100](0¯21) (mJ/m2) - 1289 [41] - 1363 1429 1602 1449 1232


Σ11[1¯10](113) (mJ/m2) - 454 [41] - 447 535 541 516 379 γisf (mJ/m2) - 136 [41] 125 [44] 105 160 129 126 -46(−133.8%) γusf (mJ/m2) - 280 [41] - 328 359(+28.2%) 403(+43.9%) 521(86.1%) 233 BCC Cr

a (˚A) 2.84 2.85 [45] 2.88 [46] 2.84 2.92 2.79 2.88 2.85

- C11 487 484 [45], 429 [47] 391 [47] 513 360(−26.1%) 171(−64.9%) 345(−29.2%) 552
- C12 147 140 [45], 119 [47] 90 [47] 164 172 170 114 381(159.2%) C44 91 105 [45], 91 [47] 103 [47] 95 76 137(+50.5%) 131(+44.0%) 66(−27.5%)


Es{100} (J/m2) 3.27 - - 3.53 3.34 1.89(−42.2%) 2.37(−27.5%) 2.58

- Es{110} (J/m2) 3.42 - - 3.00 3.13 1.76(−48.5%) 2.43(−28.9%) 2.39(−30.1%)
- Es{111} (J/m2) 3.49 - - 3.59 3.43 2.11(−39.5%) 2.57(−26.4%) 2.76 Evf (eV) - 2.86 [48] - 2.61 2.02(−29.4%) 0.51(−82.2%) 1.96(−31.5%) 2.10(−26.6%)


HCP Co

a (˚A) 2.49 2.52 [49], 2.49 [50] 2.51 [51] 2.49 2.51 2.50 2.50 2.50 c (˚A) 4.02 4.08 [49], 4.02 [50] 4.08 [51] 4.02 4.09 4.20 4.08 4.00

- C11 361 373 [49], 386 [50] 293 [52] 367 336 326 322 363
- C12 153 166 [49], 151 [50] 143 [52] 171 191 182 140 151
- C13 113 113 [49], 114 [50] 90 [52] 121 194(+71.7%) 110 123 94 C33 426 386 [49], 403 [50] 339 [52] 385 354 396 339 319(−25.1%) C44 100 93 [49], 97 [50] 78 [52] 76 58(−42.0%) 45(−55.0%) 69(−31.0%) 76


Es{0001} (J/m2) 2.08 - - 2.28 2.18 1.60 1.93 1.70

- Es{10¯10} (J/m2) 2.92 - - 2.87 2.87 2.60 2.46 2.39
- Es{10¯11} (J/m2) 2.08 - - 2.28 2.18 1.60 1.93 1.70 Es{11¯22} (J/m2) 2.06 - - 2.28 2.21 1.61 1.94 1.70


Evf (eV) 1.85 - 1.4 [50] 1.67 1.52 1.47 1.47 1.64 FCC CrCoNi a (˚A) - 3.53 [53] 3.56 [54] 3.54 3.59 3.53 3.55 3.53

- C11 - 267 [53] 249 [54] 295 235 215 247 303
- C12 - 182 [53] 159 [54] 185 176 146 165 191 C44 - 178 [53] 138 [54] 142 90(−49.4%) 130(−27.0%) 83(−53.4%) 151


less reliable for describing defect-related properties in elemental systems, whereas NEP exhibits overall excellent performance for these key static properties.

C. Short range order

It has been established that chemical short-range order affects various chemistry-microstructure relationships that influence the mechanical properties of alloys. The SRO in crystalline phases can be quantified using the WarrenCowley (WC) parameters αij = 1 − pij/cj, where pij denotes the probability of finding an atom of species j in the first-neighbor shell of an atom of type i, and cj is the atomic concentration of species j. A value of αij = 0 corresponds to a completely random solution. Positive values of αij indicate a tendency to reduce the number of i-j atomic pairs, whereas negative values indicate a preference for forming i-j pairs. Here, we compute the SRO of equiatomic CrCoNi MEA at various temperatures using a hybrid MC/MD strategy (see details in the Methods section) with different interatomic potentials, and compare the results with DFT-based MC simulations. As shown in Fig. 4, both NEP and MTP reproduce the WC parameters well at 500 K. In contrast, MEAM only captures the tendencies of Cr–Ni and Ni– Ni pairs, while EAM1 reproduces only the Co–Co pair tendency and fails for the other pairs. Notably, EAM2 predicts WC parameters close to zero for all pairs, suggesting the absence of SRO, which is physically unreasonable. With increasing temperature, the absolute values of the WC parameters generally decrease, indicating weaker SRO effects. This trend is consistent with previous computational studies [24, 55]. Although some discrepancies between NEP and DFT results appear at 1200 K, the overall variation trends remain similar. To quantitatively evaluate the accuracy of the SRO predictions for different potentials, the relative error with respect to the DFT reference is defined as εSRO = ( 3i=1 3j=i αijMD − αijDFT )/( 3i=1 3j=i αijDFT ). The cumulative εSRO for the three temperatures is shown in Fig. 4d. NEP exhibits the lowest error, while MTP shows comparable performance and significantly smaller errors than the empirical potentials. These results demonstrate that NEP can reliably reproduce SRO behavior over a wide temperature range.

| | |
|---|---|
| | |


| | |
|---|---|
| | |


| | |
|---|---|
| | |


SRO

| | |
|---|---|
| | |


| | | | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |


- FIG. 4. Comparison of WarrenCowley short-range order parameters at (a) 500 K, (b) 800 K, and (c) 1200 K as predicted by NEP, EAM1 [27], EAM2 [28], MEAM [29], and MTP [24]. Error bars represent the standard deviation obtained from 20 independent simulations with different initial configurations. At 500 K, the shaded gray region denotes the range of DFT MC results reported in three literature sources [24, 56, 57]. For 800 and 1200 K, where only single DFT reference values are available [57], the results are shown as discrete points. (d) Cumulative relative error (εSRO) with respect to DFT.


D. Stacking fault energy and dislocation dissociation

Based on the validation of the models ability to capture short-range order in the previous section, we further investigate its effects on the stacking fault energy of the CrCoNi alloy. Fig. 5 presents the SFE of both random and ordered CrCoNi solid solutions equilibrated using hybrid MC/MD simulations using various potentials. For each case, the results are averaged over 150 independent configurations to ensure the robustness of the predicted SFE; additional details are provided in the Methods section. For the random solid solution, the NEP-predicted SFE is -52 mJ/m2, which falls well within the DFT range of -26 to -60 mJ/m2, as summarized in Ref. [11]. This wide variation suggests that SFE calculations require sampling a sufficiently large number of configurations to achieve convergence, whereas only a limited number of structures have been considered in some previous DFT studies [58, 59]. Note that Ding et al. [56] calculated the SFE using 108 configurations and reported an average DFT value of -43 mJ/m2, which is close to our prediction. Among the empirical potentials, MTP slightly underestimates the SFE (-61 mJ/m2), whereas MEAM slightly overestimates it (-21 mJ/m2). EAM1 yields a reasonable average SFE (-41 mJ/m2), in contrast, EAM2 predicts a positive SFE (80 mJ/m2), which is physically inconsistent with both DFT calculations and previous simulations. Despite these discrepancies, both MD and DFT calculations consistently predict a negative SFE for the random alloy, which contradicts experimental measurements discussed earlier.

2mJ/misf

2mJ/misf

Å

Å

| | | | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |


Å

Å

- FIG. 5. Intrinsic stacking fault energies γisf for (a) random solid solutions and (b) ordered solid solutions, predicted by NEP, EAM1 [27], EAM2 [28], MEAM [29], and MTP [24]. DFT results for random solid solutions in (a) are taken from Ref. [11], while experimental data for ordered solid solutions in (b) are from Refs. [60, 61]. Stacking fault widths associated with edge and screw dislocations in (cd) Ni and (ef) CrCoNi. The experimental data in (c) are taken from Ref. [44], while the DFT results in (d) are from Ref. [62].


To resolve this discrepancy, we further examine the influence of chemical SRO. As shown in Fig. 5b, the SFE of the ordered alloy predicted by NEP increases significantly from -52 to 17 mJ/m2, placing it within the experimental range of 18±4 mJ/m2 [61] and 22±4 mJ/m2 [60]. This result is also highly consistent with the DFT-MC study of Ding et al. [56], in which the SFE increases from -43 to 30 mJ/m2, averaged over 18 initial structures. These findings support the conclusion that chemical SRO can significantly increase the SFE and suggest that experimentally studied CrCoNi alloys likely possess a substantial degree of local chemical ordering rather than existing as purely random

solid solutions. EAM1 and MTP exhibit a similar trend of increasing SFE with the introduction of SRO, although they still underestimate the SFE of the ordered structures. In contrast, EAM2 and MEAM show only minor changes in SFE, indicating that these potentials are unable to adequately capture the effects of SRO in the CrCoNi alloy.

It is well established that stacking faults are generated during the dissociation of lattice dislocations into partial dislocations in order to reduce the elastic energy [15]. The width of the stacking fault region, defined as the distance between the two partial dislocations, is therefore determined by the balance between the repulsive elastic interaction of the partial dislocations and the energy required to form the stacking fault between them, i.e., SFE. Fig. 5c-f show the stacking fault width (SFW) resulting from the dissociation of edge and screw dislocations in Ni and CrCoNi at 0 K. For the edge dislocation in Ni, the SFW predicted by NEP is 21.5 ˚A, which agrees well with the experimental measurement of 26 ± 8 ˚A [44] (see Fig. 5c). EAM2 and MEAM yield SFW values of 19.2 and 18.2 ˚A, respectively, both of which also fall within the experimental range, whereas EAM1 underestimates the SFW, giving a value of 15.5 ˚A. These results exhibit an inverse correlation with the SFE values (see Table II), as expected from classical elastic theory [63]. Notably, MTP predicts a significantly larger SFW of 36.4 ˚A, which can be attributed to its unphysical negative SFE. For the screw dislocation in Ni, the SFW predicted by NEP is 12.1 ˚A. Although experimental measurements for this quantity are scarce, this value is in good agreement with previous DFT calculations, which report an SFW of approximately 12 ˚A [62]. In contrast, all empirical potentials underestimate this value, while MTP predicts no dissociation (SFW = 0), as shown in Fig. 5d.

For the CrCoNi alloy, although the SFE is negative, the SFW remains finite at 0 K, consistent with previous theoretical studies [15]. The SFWs for both edge and screw dislocations are larger than those in Ni due to the lower SFE. NEP and MTP produce similar average results and successfully capture fluctuations arising from variations in the local chemical environment; the reported values are averaged over ten independent configurations. In contrast, EAM2 and MEAM show nearly identical results across different structures, indicating a lack of sensitivity to chemical disorder. While EAM1 partially captures this variability, it systematically underestimates the SFW compared to NEP and MTP. The effects of temperature and SRO on dislocation dissociation require substantially greater computational effort and will be addressed in future work. In comparing zero-temperature calculations with room-temperature experiments, finite-temperature stacking fault energies must include entropy contributions from atomic vibrations, magnetism, and electronic excitations [64]. Niu et al. [64] showed that vibrational contributions change the HCPFCC free-energy difference by less than 15% between 0 and 300 K in random CoCrNi alloys. We therefore expect a similarly minor effect on SFE over this temperature range, implying that experimental values extrapolated to 0 K would be only slightly reduced. Accordingly, the SFE-dependent SFW should also exhibit only minor changes over this temperature range.

E. Composition-dependent properties of CrCoNi alloys

We further examine the composition-dependent FCCBCC phase stability, SFE, shear modulus G, and lattice constant a across the CrCoNi ternary space, as shown in Fig. 6. The NEP model predicts that the FCC phase is more stable than the BCC phase when the Cr content is below 55 at.%, where ∆EFCC−BCC < 0. This agrees well with experimental observations, in which stable FCC phases are predominantly found in this compositional regime

- (Fig. 6a). EAM1 yields similar results, whereas MTP and MEAM overestimate the Cr content at the FCCBCC phase boundary. In contrast, EAM2 produces an unphysical prediction, with the FCC phase more stable than BCC across the entire composition space. Only compositions corresponding to stable FCC phases are considered for evaluating SFE, G, and a. The NEP model predicts a strong composition dependence of the SFE, which increases from negative to positive values with increasing Ni content and decreasing Cr content, consistent with first-principles calculations. For example, Yan et al. [14] reported SFE values ranging from 46.4 to 88.5 mJ/m2 as the Cr content decreases from


67 to 0 at.% in Co33CrxNi67−x alloys, and predicted an FCCBCC transition at x < 57.3, in good agreement with NEP. Although MTP reproduces a similar trend, it underestimates the SFE and fails to yield positive values, likely due to its inaccurate description of pure Ni, indicating limited transferability to non-equimolar compositions. EAM1 and EAM2 show significant deviations, with the former mispredicting SFE at low Ni content and the latter yielding uniformly positive SFE. MEAM captures the qualitative trend but predicts a significantly shifted transition boundary.

For elastic properties, NEP predicts that G increases from 60 to 120 GPa with increasing Co content and decreasing Ni/Cr content, consistent with the higher intrinsic stiffness of Co (Table II). This trend agrees well with first-principles results [14], which show an increase in G from 86.5 to 123.4 GPa as Co content increases from 0 to 67 at.% in CoxCr33Ni67−x. MTP reproduces a similar trend, whereas other empirical potentials fail to capture it accurately. The lattice constant a is also well reproduced by NEP, decreasing from 3.55 to 3.51 ˚A with increasing Co content, in close agreement with first-principles calculations [14]. Overall, these results demonstrate that the NEP model provides an accurate and consistent description of composition-dependent properties across both equimolar and non-equimolar CrCoNi alloys, outperforming existing potentials.

![image 2](Wu et al._2026_General-Purpose Machine-Learned Potential for CrCoNi Alloys Enabling Large-Scale Atomistic Simulatio_images/imageFile2.png)

- FIG. 6. Ternary plots of ∆EFCC−BCC, intrinsic stacking fault energy γisf, shear module G and lattice constant a predicted by (a) NEP, (b) MTP [24], (c) EAM1 [27], (d) EAM2 [28] and (e) MEAM [29] across the CrCoNi compositional space. White symbols in (a) indicate experimentally observed stable FCC compositions, including Cr30Co40Ni30 [65], Cr40Co55Ni5 [66], Cr45Co27.5Ni27.5 [67], Cr25Co37.5Ni37.5 [67], Cr30Co30Ni40 [68], Cr36Co36Ni28 [68], Cr40Co20Ni40 [69], Cr20Co60Ni20 [69], Cr33Co38Ni29 [70], Cr33Co42Ni25 [70], Cr40Co40Ni20 [71], Co40Ni60 [72], Co60Ni40 [73], Cr5Co47.5Ni47.5 [73], Cr20Co40Ni40 [73], as well as pure FCC Ni and pure BCC Co.


F. Melting properties

We further evaluate the performance of the NEP model under high-temperature conditions by examining its ability to predict the melting points of elemental metals and the equiatomic CrCoNi, as well as its capability to describe

the partial radial distribution functions g(r) of the alloy in the fully liquid state. The melting temperature (Tm) is evaluated using solidliquid phase coexistence molecular dynamics simulations, in which the temperature, pressure, and fraction of liquid atoms remain stable for 400 ps, as shown in Fig. 7a. The inset showing the microstructure of CrCoNi in the final simulation frame further illustrates the clear interface between the solid and liquid phases. The melting temperature is obtained by averaging the temperature over the last 200 ps of the simulation.

![image 3](Wu et al._2026_General-Purpose Machine-Learned Potential for CrCoNi Alloys Enabling Large-Scale Atomistic Simulatio_images/imageFile3.png)

- FIG. 7. (a) Evolution of normalized temperature, pressure, and liquid fraction during the two-phase coexistence process of the CrCoNi alloy computed using NEP. The inset shows the atomic configuration at 400 ps, colored by PTM analysis [74],


where yellow represents FCC atoms and grey indicates liquid atoms. (b) Melting temperature (Tm) predicted by EAM1 [27], EAM2 [28], MEAM [29], MTP [24], and NEP. (c) Cumulative relative error εTm, compared with experimental values for Cr [75], Co [50], Ni [41], and CrCoNi [76]. (d) Partial radial distribution functions g(r) of the liquid phase for equiatomic CrCoNi at 2684 K, calculated using potentials and DFT [24].

### The predicted Tm values from different potentials are compared with experimental data in Fig. 7b. To quantitatively assess the accuracy, the relative error with respect to experimental measurements is defined as εT

### = (TMDm − TExpm )/TExpm . The NEP model slightly overestimates the melting temperature of Cr, whereas MTP underestimates that of Co. Nevertheless, both potentials show high accuracy for Ni and the CrCoNi alloy, and their cumulative εT

m

### values are comparable, as shown in Fig. 7c. In particular, the melting temperature of CrCoNi predicted by

m

NEP is 1638 K, which is close to the experimental value of 1690 K [76]. In contrast, the empirical potentials exhibit significantly larger deviations in predicting the melting temperature of CrCoNi, yielding values of 1398 K (EAM1), 2084 K (EAM2), and 1920 K (MEAM).

The partial radial distribution functions of liquid CrCoNi at 2684 K are compared in Fig. 7d for all elemental pairs. The results show that the predictions from NEP and MTP almost completely overlap and both agree well with the DFT-based ab initio molecular dynamics results [24]. The largest deviation occurs for the CrCr pair, where the position of the first peak is slightly shifted to a shorter distance by approximately 0.05 ˚A. Notably, the first peak of the CrCr pair is significantly lower than those of the other elemental pairs, indicating that this chemical interaction is energetically less favorable. This observation suggests that the liquid phase is also influenced by the considerable chemical complexity present in the crystalline phase. In contrast, the other empirical potentials exhibit varying degrees of error and fail to reproduce the DFT radial distribution curves.

G. Uniaxial tensile deformation

As a stringent test of the NEP model, we probe the allotropic phase transformations of Ni and equiatomic CrCoNi under uniaxial tension along [100] at a constant strain rate of 109 s−1, using a 3 × 3 × 3 conventional supercell (108 atoms). For pure Ni, the stressstrain response shows a monotonic increase in stress with increasing strain, followed by a sudden drop at a strain of approximately 0.14, as shown in Fig. 8a. The inset atomic configurations illustrate the corresponding atomic structures at different strain levels, revealing the evolution from strained FCC to BCC and finally to HCP structures. These snapshots indicate that the abrupt stress drop corresponds to an FCCBCCHCP phase transformation. The stress changes from tensile (positive) to compressive (negative) due to the volume change associated with the phase transformation. A similar phenomenon has also been reported in tensile-induced FCCBCC transformations in HEA in a previous MD study [77]. Subsequently, the HCP phase remains stable, and the stress increases again as the strain continues to 0.3.

![image 4](Wu et al._2026_General-Purpose Machine-Learned Potential for CrCoNi Alloys Enabling Large-Scale Atomistic Simulatio_images/imageFile4.png)

- FIG. 8. Stressstrain curves under uniaxial tensile deformation for (a) Ni and (b) CrCoNi predicted using EAM1 [27], EAM2 [28], MEAM [29], MTP [24], NEP, and DFT. The inset structures are colored according to the local crystal structure identified by PTM analysis [74], where FCC, BCC, HCP, and other structures are shown in yellow, blue, red, and grey, respectively.


A previous machine-learning potential developed specifically for Ni [41] also predicted an FCC-to-HCP transformation, following the same crystallographic orientation relationship, namely {010}FCC ∥ {0001}HCP and ⟨001⟩FCC ∥ ⟨11¯20⟩HCP. The main difference is that our model predicts a transient BCC phase during the transformation. This intermediate phase exists only for a very short time and is likely related to the high strain rate and finite-size effects in the simulation. Similar FCC-BCC-HCP transformation pathways have been reported in previous MD studies of Cu nanowires [78], where the transformation was also induced by high strain rates. In that work, the orientation relationship was reported as {010}FCC ∥ {110}BCC ∥ {0001}HCP. Moreover, strain-induced FCC-to-HCP transformations in nanocrystalline Ni have also been observed experimentally [79, 80]. The stressstrain behavior predicted by

NEP is in excellent agreement with our DFT results, and the average atomic energy at the transition state decreases from -5.38 eV/atom (FCC) to -5.40 eV/atom (BCC) and further to -5.42 eV/atom (HCP), indicating that the HCP structure becomes energetically more stable under the applied strain. In contrast, the other potentials predict different mechanical responses and phase transformation pathways compared with the NEP and DFT results.

Fig. 8b shows the stressstrain response for the CrCoNi MEA. In this case, the transition state between the FCC and HCP phases exhibits a mixed-phase structure due to the complex chemical environment and lattice distortion. The FCC-to-HCP transformation follows the same crystallographic orientation relationship observed in Ni. Interestingly, a second stress drop occurs within the HCP phase at a strain of 0.265, followed by a recovery in stress as the strain increases to 0.3. The inset structures in Fig. 8b indicate that this behavior is associated with a rotation of the crystalline orientation during deformation. Notably, an in situ neutron diffraction study reported a bulk FCCHCP phase transformation in CrCoNi at 15 K under tensile loading, beginning at a strain of approximately 0.14 [81]. The stress predicted by NEP is very close to the DFT results, further demonstrating the high accuracy of the model. MTP also shows a similar tensile response to NEP, whereas the other empirical potentials fail to reproduce the observed mechanical deformation behavior.

H. Computational efficiency

In the above sections, we have examined the accuracy of the developed NEP model in predicting fundamental crystal properties, short-range order, stacking fault energies, high-temperature properties, and deformation behavior. However, despite the high accuracy of MLPs, their computational efficiency is often less discussed [24, 41]. In general, MLPs are significantly faster than DFT calculations, as the computational cost of MLPs scales linearly with system size, whereas DFT typically scales cubically. Nevertheless, MLPs may still be considerably slower than classical empirical potentials, which can limit their applicability in large-scale and long-time molecular dynamics simulations. Here, we compare the computational efficiency of two MLPs, NEP and MTP, with classical empirical potentials, including EAM and MEAM. As shown in Fig. 9a, all potentials exhibit approximately linear scaling with increasing system size, accompanied by a decrease in the number of simulation steps per second. However, the fastest potential, EAM, is nearly two orders of magnitude faster than the slowest potential, MTP. For the GPU-accelerated NEP model, the simulation speed remains nearly constant as the system size increases up to approximately 10,000 atoms, after which it decreases linearly. This behavior arises because the GPU becomes fully utilized beyond this system size.

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |


- FIG. 9. Benchmark of computational efficiency for different interatomic potentials, including EAM [27], MEAM [29], MTP [24], and NEP. (a) Simulation speed (steps per second) as a function of system size. (b) Computational throughput (atoms × steps per second) for the different potentials, normalized to the performance of MTP for a system containing 1,372,000 atoms. All CPU-based tests were performed on a 64-core AMD Rome 7H12 processor using LAMMPS (22 Jul 2025 Update 2) [82]. For NEP, GPU performance on one to four Tesla V100-SXM2-16GB devices using GPUMD-4.9 [83] is also presented.


The computational throughput (atoms × steps per second) for a system containing 1,372,000 atoms is shown in Fig. 9b. The performance is normalized with respect to MTP. NEP running on a CPU is approximately five

times faster than MTP, while the use of a single Tesla V100 GPU provides a 48-fold speedup; notably, the GPU has a comparable cost to the CPU platform. A recently developed GPU-accelerated MTP implementation [84] is not included in this comparison due to its substantially higher memory requirements. For the system considered here, it requires on the order of hundreds of gigabytes of GPU memory, whereas NEP can be executed with only 16 GB, highlighting its superior memory efficiency. Using four V100 GPUs in parallel further increases the speed to approximately 117 times that of MTP, with a parallel efficiency of 61%. This level of acceleration enables large-scale molecular dynamics simulations with machine-learning potentials.

#### III. CONCLUSION

In conclusion, we developed a high-fidelity machine-learning potential based on the NEP framework for the CrCoNi system. The model achieves nearDFT-level accuracy in predicting a wide range of properties for both elemental metals and equiatomic or non-equiatomic CrCoNi medium-entropy alloys, including lattice parameters, elastic constants, equations of state, phonon spectra, defect energetics, dislocation dissociation, and melting temperatures. For the CrCoNi alloy, the NEP model accurately captures chemical short-range order across a range of temperatures and quantitatively reveals its influence on stacking fault energy, bringing the predicted values into agreement with experimental measurements. In addition, the model successfully describes strain-induced FCCHCP phase transformations and their crystallographic orientation relationships during deformation. Comprehensive benchmarking against widely used empirical potentials and existing machine-learning potentials demonstrates that the NEP model provides superior overall accuracy while maintaining high computational efficiency. This capability enables reliable large-scale and long-time MD/MC simulations for the investigation and design of advanced CrCoNi MEAs. Furthermore, the dataset generated in this work provides a valuable foundation for the future development of MLPs for CrCoNi-based HEAs.

#### IV. METHODS

1. Density functional theory calculations

All DFT calculations were performed using the Perdew-Burke-Ernzerhof (PBE) [85] exchange-correlation functional and projector-augmented wave (PAW) pseudopotentials [86], as implemented in the Vienna ab initio Simulation Package (VASP, version 6.4.2) [87–91]. The PAW datasets (potpaw.PBE.64) treated the valence electrons of Cr, Co, and Ni as 3p63d54s1, 3d84s1, and 3d84s2, respectively. All calculations were carried out within a collinear spinpolarized framework, with an initial magnetic moment of 3 µB assigned to each element, where µB denotes the Bohr magneton. Convergence tests were conducted separately for the plane-wave energy cutoff and the MonkhorstPack k-point mesh density. These parameters were iteratively optimized until the total energy converged to within 1 meV/atom. The final converged settings were an energy cutoff of 450 eV for all elemental systems, and a minimum k-point spacing of 0.25 ˚A−1. Because the systems studied are metallic, a smearing scheme was employed to improve the convergence of the electronic self-consistency cycle. Specifically, first-order Methfessel-Paxton smearing with a width of 0.1 eV was used. The electronic self-consistency and ionic relaxation convergence criteria were set to 10−5 eV and 0.02 eV/˚A, respectively.

2. MLP development

The development of the NEP model consists of two main stages: (i) preparation of the initial dataset and (ii) iterative exploration via active learning. The initial dataset was constructed by combining two existing MTP datasets. The first dataset was developed by Cao et al. [24] and includes the TS-0, TS-3, and TS-f subsets. It should be noted that the so-called MTP dataset referenced in Fig. 1 comprises the complete set of TS-0 to TS-5 and TS-f; detailed descriptions of these subsets can be found in the Methods section of Ref. [24]. The second dataset was originally developed for the CrCoFeNi system, from which the CrCoNi subset was extracted [92].

Since these datasets lack sufficient coverage of non-equiatomic CrCoNi compositions, we further constructed additional structures by systematically sampling the composition space. Specifically, the concentration of each element was varied from 0 to 100 at.% with an interval of 4 at.%, and for each composition both FCC and BCC structures were generated. To enhance structural diversity, random atomic displacements of ±0.1 ˚A were applied. The resulting dataset contains approximately 8000 structures. To reduce redundancy and ensure representative sampling, we employed the periodic SOAP descriptor [93] as implemented in the Dscribe package [94] and performed principal

component analysis. The SOAP parameters were set as follows: a cutoff radius of 6.0 ˚A, nmax = 8, and lmax = 6. Farthest point sampling was then applied in the PCA-reduced space to select 2000 representative structures, which were subsequently labeled using high-accuracy DFT calculations and used as the initial training dataset.

We then employed an iterative active learning strategy [95] to further enrich the dataset. Starting from the initial dataset, a preliminary NEP model was trained and subsequently used to perform MD simulations to sample new configurations for retraining. During this process, we progressively incorporated diverse configurations, including elemental systems sampled over a temperature range of 13000 K, point-defect structures at 3001000 K, stacking faults, as well as structures subjected to compressive and tensile deformations. All thermal simulations were conducted under zero-pressure conditions. The systems considered include FCC Ni, BCC Cr, HCP Co, and binary and ternary FCC CrCoNi alloys. At each iteration, configurations that were significantly outside the existing training domain were discarded, and structures associated with non-converged DFT calculations were excluded. The latter is commonly encountered in spin-polarized magnetic calculations and is computationally demanding. After several iterations, a sufficiently diverse dataset was obtained.

A separate validation dataset was then constructed to assess model performance. Seven representative initial structures were selected: FCC Ni, BCC Cr, HCP Co, equiatomic binary FCC alloys (CrCo, CrNi, CoNi), and ternary FCC CrCoNi. These systems were simulated in the isothermalisobaric (NPT) ensemble over a temperature range of 53000 K for 2 ns. The extended simulation time ensures both model stability and thorough exploration of the configuration space. From each trajectory, 12 configurations were uniformly sampled, resulting in a validation dataset comprising 84 structures (Fig. 1). The active learning iterations were terminated when the RMSEs of energy, force, and stress for the validation dataset became comparable to those of the training dataset; otherwise, the validation structures were incorporated into the training set and the process was repeated. As summarized in Table I, the RMSEs for the training and validation datasets are in close agreement. The final NEP dataset contains 3030 structures. The model was trained with optimized hyperparameters using eight Tesla V100 GPUs, requiring 57 hours and approximately 400,000 generations to achieve convergence.

3. Hybrid MD/MC simulation

The MD/MC simulations shown in Fig. 4 were initialized from chemically random configurations and performed in the NPT ensemble using a Nos´eHoover thermostat and barostat to maintain zero pressure at temperatures of 500, 800, and 1200 K. Each system was equilibrated for 5000 steps in a 3×3×3 conventional FCC supercell containing 108 atoms. Subsequently, hybrid MD/MC simulations were carried out for an additional 5000 steps, during which atomic species were randomly swapped according to the Metropolis criterion within the NPT ensemble, following a procedure similar to previous DFT-based MC simulations [24]. The WarrenCowley parameters were calculated by averaging over the final 100 steps of each simulation. For each interatomic potential, a total of 20 independent simulations were performed. All simulations were performed using the LAMMPS code [82] with a timestep of 1 fs. Atomic configurations were visualized using OVITO [96], and all data pre- and post-processing were carried out using the self-developed open-source code MDAPY [97].

The stacking fault energy (SFE) shown in Fig. 5a was calculated using a supercell containing 216 atoms, with orthogonal axes aligned along the [112], [1¯10], and [11¯1] directions of the FCC lattice. The SFE was obtained from the energy difference before and after displacing the upper half of the crystal along the z-direction by a distance of a/√6, where a is the lattice constant. For each interatomic potential, the SFE was averaged over 150 structures with random elemental distributions. To evaluate the effect of short-range order (SRO), each of these 150 structures was further subjected to 5000 MC swap steps at 0 K, after which the SFE of the ordered configurations was calculated (Fig. 5b).

For the ternary phase diagram (Fig. 6), the composition of each element was varied from 0 to 100 at.% in increments of 5 at.%. For each composition, a 3×3×3 FCC supercell (108 atoms) and a 4×4×4 BCC supercell (128 atoms) were constructed and subjected to cell optimization and energy minimization using various interatomic potentials. The properties at each composition were averaged over five independent structures to obtain ∆FCC−BCC and the lattice constant a. Subsequently, SFE and shear modulus (G) were calculated only for compositions where the FCC phase is more stable than the BCC phase, using the optimized lattice constant. For each selected composition, 150 independent structures were generated for SFE calculations, while the shear modulus was evaluated using a single 3×3×3 FCC supercell (108 atoms).

4. Dislocation dissociation

### To investigate dislocation dissociation (Fig. 5c-f), a Ni bulk system was constructed with crystallographic orientations along [110], [¯111], and [112], with dimensions of approximately 200×152×22 ˚A. Two edge dislocations were

introduced, with the dislocation line along the z-direction and the Burgers vector along the x-direction. This dipole configuration ensures a zero net Burgers vector, enabling fully periodic boundary conditions. A similar approach was employed to construct screw dislocation models using a supercell oriented along [1¯12], [¯111], and [110], with dimensions of approximately 258×244×25 ˚A. In this case, four screw dislocations were introduced to form a quadrupole configuration, ensuring periodicity in all directions.

For the dipole edge configuration, the two dislocations were positioned at (x, y) coordinates of (0.25, 0.25) and (0.75, 0.75). For the quadrupole screw configuration, four dislocations were placed at (x, y) coordinates of (0.25, 0.25), (0.75, 0.25), (0.25, 0.75), and (0.75, 0.75). The maximum stacking fault widths (SFWs) observed in Fig. 5 are approximately 65 ˚A for edge dislocations and 38 ˚A for screw dislocations in the CrCoNi alloy. These values are well below half of the box length in the edge dislocation model (∼100 ˚A) and one quarter in the screw dislocation model (∼64.5 ˚A) along the slip (x) direction, ensuring negligible interactions between dissociated dislocations and their periodic images.

All dislocation structures were generated using ATOMSK [98]. The same dislocation models were further used to construct ten equiatomic CrCoNi samples with different elemental distributions. All systems were subjected to full cell optimization and energy minimization at 0 K using different interatomic potentials. The convergence criteria for energy and force are set to 1×10−12 eV and 1×10−12 eV/˚A, respectively. During relaxation, the dislocations dissociate along the x-direction into two partial dislocations separated by a stacking fault. The stacking fault width was averaged over the two (edge) or four (screw) dislocations in Ni, and further averaged over ten independent configurations for the CrCoNi alloy.

5. Liquid state simulation

The two-phase coexistence method was employed to determine the melting temperature (Tm) of FCC Ni, BCC Cr, HCP Co, and the equiatomic FCC CrCoNi alloy. The supercell was constructed with a length of approximately 70 ˚A along the x-direction and 36 ˚A along the other directions, containing between 8,000 and 9,400 atoms. Each supercell was divided along the x-direction into two regions: a solid region and a liquid region.

The system was first equilibrated at Tguess−1000 K for 20 ps, where Tguess denotes the initial estimate of the melting temperature. Then, the solid region was fixed, and the liquid region was directly set to 2Tguess K and maintained for 40 ps using a Langevin thermostat to ensure complete melting. The system was subsequently evolved in the isobaricisoenthalpic (NPH) ensemble, maintaining zero pressure, for 400 ps. If solidliquid coexistence was sustained over this timescale, the melting temperature Tm was determined by averaging the temperature over the final 100 ps

- (Fig. 7a,b). If the system fully solidified, Tguess was increased; if it completely melted, Tguess was decreased. This procedure was iteratively repeated until the correct Tm was obtained.


For the radial distribution function shown in Fig. 7d, a 10×10×10 FCC supercell containing 4000 atoms was equilibrated in the NPT ensemble at 2684 K and zero hydrostatic pressure for 20 ps. The element-resolved partial RDFs were computed using configurations collected over the final 10 ps.

#### V. DATA AVAILABILITY

All datasets and the trained NEP model will be made publicly available in a GitHub repository upon acceptance of the manuscript.

#### VI. CODE AVAILABILITY

The source code for MDAPY is available at the Github repository: https://github.com/mushroomfire/mdapy. The source code for LAMMPS is available at the Github repository: https://github.com/lammps/lammps. The source code for GPUMD is available at the Github repository: https://github.com/brucefan1983/GPUMD.

#### ACKNOWLEDGMENTS

Y.-C. W., T. M. and M. A. acknowledge the support from FinnCERES flagship (grant no. 151830423), Business Finland (grant nos. 211835, 211909, and 211989), the Research Council of Finland (grant no. 13361245), and the Future Makers program. M. A. acknowledges support from the Academy of Finland Center of Excellence program (program nos. 278367 and 317464), as well as the Finnish Cultural Foundation. A. E. acknowledges support from

the European Union Horizon 2020 research and innovation program under Grant Agreement No. 857470, from the European Regional Development Fund under the Foundation for Polish Science International Research Agenda PLUS program (Grant No. MAB PLUS/2018/8), and from the initiative of the Ministry of Science and Higher Education Support for the activities of Centers of Excellence established in Poland under the Horizon 2020 program (Agreement No. MEiN/2023/DIR/3795). The authors acknowledge the computational resources provided by the Aalto University School of Science Science-IT project, as well as by CSC (Finland) via the project 2015437.

- [1] E. P. George, D. Raabe, and R. O. Ritchie, High-entropy alloys, Nature reviews materials 4, 515 (2019).
- [2] W.-T. Zhang, X.-Q. Wang, F.-Q. Zhang, X.-Y. Cui, B.-B. Fan, J.-M. Guo, Z.-M. Guo, R. Huang, W. Huang, X.-B. Li, et al., Frontiers in high entropy alloys and high entropy functional materials, Rare Metals 43, 4639 (2024).
- [3] A. Esfandiarpour, S. T. Nori, S. Bonfanti, M. Alava, A. Wadowski, W. Huo, L. Kurpaska, M. Pecelerowicz, and J. S. Wro´bel, Machine learning applied to high entropy alloys under irradiation, Advanced Engineering Materials 27, e202402280 (2025).
- [4] Z. Li, S. Zhao, R. O. Ritchie, and M. A. Meyers, Mechanical properties of high-entropy alloys with emphasis on face-centered cubic alloys, Progress in Materials Science 102, 296 (2019).
- [5] D. Liu, Q. Yu, S. Kabra, M. Jiang, P. Forna-Kreutzer, R. Zhang, M. Payne, F. Walsh, B. Gludovatz, M. Asta, A. M. Minor, E. P. George, and R. O. Ritchie, Exceptional fracture toughness of crconi-based medium- and high-entropy alloys at 20 kelvin, Science 378, 978 (2022).
- [6] M. Yang, L. Zhou, C. Wang, P. Jiang, F. Yuan, E. Ma, and X. Wu, High impact toughness of crconi medium-entropy alloy at liquid-helium temperature, Scripta Materialia 172, 66 (2019).
- [7] S. Zhao, S. Yin, X. Liang, F. Cao, Q. Yu, R. Zhang, L. Dai, C. J. Ruestes, R. O. Ritchie, and A. M. Minor, Deformation and failure of the crconi medium-entropy alloy subjected to extreme shock loading, Science Advances 9, eadf8602 (2023).
- [8] F. Granberg, K. Nordlund, M. W. Ullah, K. Jin, C. Lu, H. Bei, L. M. Wang, F. Djurabekova, W. J. Weber, and Y. Zhang, Mechanism of radiation damage reduction in equiatomic multicomponent single phase alloys, Phys. Rev. Lett. 116, 135504

(2016).

- [9] C. Slone, S. Chakraborty, J. Miao, E. George, M. Mills, and S. Niezgoda, Influence of deformation induced nanoscale twinning and fcc-hcp transformation on hardening and texture development in medium-entropy crconi alloy, Acta Materialia 158, 38 (2018).
- [10] F. G. Coury, G. Zepon, and C. Bolfarini, Multi-principal element alloys from the crconi family: outlook and perspectives, Journal of Materials Research and Technology 15, 3461 (2021).
- [11] L. Zhu and Z. Wu, Effects of short range ordering on the generalized stacking fault energy and deformation mechanisms in fcc multiprincipal element alloys, Acta Materialia 259, 119230 (2023).
- [12] R. Zhang, S. Zhao, J. Ding, Y. Chong, T. Jia, C. Ophus, M. Asta, R. O. Ritchie, and A. M. Minor, Short-range order and its impact on the crconi medium-entropy alloy, Nature 581, 283 (2020).
- [13] F. G. Coury, K. D. Clarke, C. S. Kiminami, M. J. Kaufman, and A. J. Clarke, High throughput discovery and design of strong multicomponent metallic solid solutions, Scientific reports 8, 8600 (2018).
- [14] J. Yan, Z. Zhang, P. Zhang, J. Liu, H. Yu, Q. Hu, J. Yang, and Z. Zhang, Design and optimization of the composition and mechanical properties for non-equiatomic cocrni medium-entropy alloys, Journal of Materials Science & Technology 139, 232 (2023).
- [15] M. Shih, J. Miao, M. Mills, and M. Ghazisaeidi, Stacking fault energy in concentrated alloys, Nature communications 12, 3590 (2021).
- [16] N. Rasooli and M. Daly, Searching for evidence of strengthening from short-range order in the crconi medium entropy alloy, Scripta Materialia 271, 116997 (2026).
- [17] L. Li, Z. Chen, S. Kuroiwa, M. Ito, K. Yuge, K. Kishida, H. Tanimoto, Y. Yu, H. Inui, and E. P. George, Evolution of shortrange order and its effects on the plastic deformation behavior of single crystals of the equiatomic cr-co-ni medium-entropy alloy, Acta Materialia 243, 118537 (2023).
- [18] M. S. Daw and M. I. Baskes, Embedded-atom method: Derivation and application to impurities, surfaces, and other defects in metals, Phys. Rev. B 29, 6443 (1984).
- [19] B.-J. Lee and M. I. Baskes, Second nearest-neighbor modified embedded-atom-method potential, Phys. Rev. B 62, 8564

(2000).

- [20] Y. Mishin, Machine-learning interatomic potentials for materials science, Acta Materialia 214, 116980 (2021).
- [21] J.-P. Du, P. Yu, S. Shinzato, F.-S. Meng, Y. Sato, Y. Li, Y. Fan, and S. Ogata, Chemical domain structure and its formation kinetics in crconi medium-entropy alloy, Acta Materialia 240, 118314 (2022).
- [22] I. Novikov, B. Grabowski, F. Ko¨rmann, and A. Shapeev, Magnetic moment tensor potentials for collinear spin-polarized materials reproduce different magnetic states of bcc fe, npj Computational Materials 8, 13 (2022).
- [23] E. Podryabinkin, K. Garifullin, A. Shapeev, and I. Novikov, Mlip-3: Active learning on atomic environments with moment tensor potentials, The Journal of Chemical Physics 159, 084112 (2023).
- [24] Y. Cao, K. Sheriff, and R. Freitas, Capturing short-range order in high-entropy alloys with machine learning potentials, npj Comput Mater 11, 268 (2025).
- [25] Z. Fan, Z. Zeng, C. Zhang, Y. Wang, K. Song, H. Dong, Y. Chen, and T. Ala-Nissila, Neuroevolution machine learning potentials: Combining high accuracy and low cost in atomistic simulations and application to heat transport, Phys. Rev.


- B 104, 104309 (2021).
- [26] K. Song, R. Zhao, J. Liu, Y. Wang, E. Lindgren, Y. Wang, S. Chen, K. Xu, T. Liang, P. Ying, et al., General-purpose machine-learned potential for 16 elemental metals and their alloys, Nature Communications 15, 10208 (2024).
- [27] Q.-J. Li, H. Sheng, and E. Ma, Strengthening in multi-principal element alloys with local-chemical-order roughened dislocation pathways, Nat Commun 10, 3563 (2019).
- [28] D. Farkas and A. Caro, Model interatomic potentials for FeNiCrCoAl high-entropy alloys, J. Mater. Res. 35, 3031 (2020).
- [29] W.-M. Choi, Y. H. Jo, S. S. Sohn, S. Lee, and B.-J. Lee, Understanding the physical metallurgy of the cocrfemnni highentropy alloy: an atomistic simulation study, npj Computational Materials 4, 1 (2018).
- [30] Y. Han, H. Chen, Y. Sun, J. Liu, S. Wei, B. Xie, Z. Zhang, Y. Zhu, M. Li, J. Yang, et al., Ubiquitous short-range order in multi-principal element alloys, Nature Communications 15, 6486 (2024).
- [31] D. Hua, Q. Zhou, Y. Shi, S. Li, K. Hua, H. Wang, S. Li, and W. Liu, Revealing the deformation mechanisms of 110 symmetric tilt grain boundaries in cocrni medium-entropy alloy, International Journal of Plasticity 171, 103832 (2023).
- [32] S. Yan, Y. Nie, and A. Paradowska, Effect of specimen size and crystallographic orientation on the nano/microscale mechanical properties and deformation behavior of crconi medium-entropy alloy, Materials & Design 235, 112387 (2023).
- [33] Z. Zhu, S. Yan, H. Chen, and G. Gou, Unprecedented combination of strength and ductility in laser welded nicocr medium entropy alloy joints, Materials Science and Engineering: A 803, 140501 (2021).
- [34] D. Utt, S. Lee, Y. Xing, H. Jeong, A. Stukowski, S. H. Oh, G. Dehm, and K. Albe, The origin of jerky dislocation motion in high-entropy alloys, Nature communications 13, 4777 (2022).
- [35] A. Esfandiarpour, S. Papanikolaou, and M. Alava, Edge dislocations in multicomponent solid solution alloys: Beyond traditional elastic depinning, Phys. Rev. Res. 4, L022043 (2022).
- [36] A. Togo, L. Chaput, T. Tadano, and I. Tanaka, Implementation strategies in phonopy and phono3py, J. Phys. Condens. Matter 35, 353001 (2023).
- [37] W. M. Shaw and L. D. Muhlestein, Investigation of the Phonon Dispersion Relations of Chromium by Inelastic Neutron Scattering, Phys. Rev. B 4, 969 (1971).
- [38] N. Wakabayashi, R. H. Scherm, and H. G. Smith, Lattice dynamic of ti, co, tc, and other hcp transition metals, Phys. Rev. B 25, 5122 (1982).
- [39] R. J. Birgeneau, J. Cordes, G. Dolling, and A. D. B. Woods, Normal Modes of Vibration in Nickel, Phys. Rev. 136, A1359

(1964).

- [40] V. Randle and G. Owen, Mechanisms of grain boundary engineering, Acta Materialia 54, 1777 (2006).
- [41] X. Gong, Z. Li, A. S. L. S. Pattamatta, T. Wen, and D. J. Srolovitz, An accurate and transferable machine learning interatomic potential for nickel, Commun Mater 5, 157 (2024).
- [42] N. S. Kanhe, A. Kumar, S. Yusuf, A. Nawale, S. Gaikwad, S. A. Raut, S. Bhoraskar, S. Y. Wu, A. Das, and V. Mathe, Investigation of structural and magnetic properties of thermal plasma-synthesized Fe1xNi alloy nanoparticles, Journal of Alloys and Compounds 663, 30 (2016).
- [43] E. H. Megchiche, S. P´erusin, J.-C. Barthelat, and C. Mijoule, Density functional calculations of the formation and migration enthalpies of monovacancies in Ni: Comparison of local and nonlocal approaches, Phys. Rev. B 74, 064111 (2006).
- [44] C. B. Carter and S. M. Holmes, The stacking-fault energy of nickel, The Philosophical Magazine: A Journal of Theoretical Experimental and Applied Physics 35, 1161 (1977).
- [45] V. I. Razumovskiy, A. V. Ruban, and P. A. Korzhavyi, First-principles study of elastic properties of Cr- and Fe-rich Fe-Cr alloys, Phys. Rev. B 84, 024106 (2011).
- [46] M. C. Gao, Y. Suzuki, H. Schweiger, O. N. Dog˘an, J. Hawk, and M. Widom, Phase stability and elastic properties of CrV alloys, J. Phys.: Condens. Matter 25, 075402 (2013).
- [47] P. So¨derlind, R. Ahuja, O. Eriksson, J. M. Wills, and B. Johansson, Crystal structure and elastic-constant anomalies in the magnetic 3 d transition metals, Phys. Rev. B 50, 5918 (1994).
- [48] T. Korhonen, M. J. Puska, and R. M. Nieminen, Vacancy-formation energies for fcc and bcc transition metals, Phys. Rev. B 51, 9526 (1995).
- [49] B. Kong, T.-X. Zeng, H.-B. Xu, D.-l. Chen, Z.-W. Zhou, and Z.-J. Fu, Phase diagram, mechanical and thermodynamics properties of metallic Co under high temperature and high pressure, Computational Materials Science 104, 130 (2015).
- [50] M. Bideault, J. Creuze, R. Asahi, and E. Wimmer, Polyvalent machine-learned potential for cobalt: From bulk to nanoparticles, Phys. Rev. Materials 8, 123803 (2024).
- [51] A. Dewaele, M. Torrent, P. Loubeyre, and M. Mezouar, Compression curves of transition metals in the Mbar range: Experiments and projector augmented-wave calculations, Phys. Rev. B 78, 104102 (2008).
- [52] D. Antonangeli, M. Krisch, G. Fiquet, D. L. Farber, C. M. Aracne, J. Badro, F. Occelli, and H. Requardt, Elasticity of Cobalt at High Pressure Studied by Inelastic X-Ray Scattering, Phys. Rev. Lett. 93, 215505 (2004).
- [53] H. Ge, H. Song, J. Shen, and F. Tian, Effect of alloying on the thermal-elastic properties of 3d high-entropy alloys, Materials Chemistry and Physics 210, 320 (2018).
- [54] G. Laplanche, M. Schneider, F. Scholz, J. Frenzel, G. Eggeler, and J. Schreuer, Processing of a single-crystalline CrCoNi medium-entropy alloy and evolution of its thermal expansion and elastic stiffness coefficients with temperature, Scripta Materialia 177, 44 (2020).
- [55] S. Ghosh, V. Sotskov, A. V. Shapeev, J. Neugebauer, and F. Ko¨rmann, Short-range order and phase stability of crconi explored with machine learning potentials, Phys. Rev. Mater. 6, 113804 (2022).
- [56] J. Ding, Q. Yu, M. Asta, and R. O. Ritchie, Tunable stacking fault energies by tailoring local chemical order in crconi medium-entropy alloys, Proceedings of the National Academy of Sciences 115, 8919 (2018).


- [57] A. Tamm, A. Aabloo, M. Klintenberg, M. Stocks, and A. Caro, Atomic-scale properties of ni-based fcc ternary, and quaternary alloys, Acta Materialia 99, 307 (2015).
- [58] Z. Zhang, H. Sheng, Z. Wang, B. Gludovatz, Z. Zhang, E. P. George, Q. Yu, S. X. Mao, and R. O. Ritchie, Dislocation mechanisms and 3d twin architectures generate exceptional strength-ductility-toughness combination in crconi mediumentropy alloy, Nature communications 8, 14390 (2017).
- [59] Y. Zhang, Y. Zhuang, A. Hu, J.-J. Kai, and C. T. Liu, The origin of negative stacking fault energies and nano-twin formation in face-centered cubic high entropy alloys, Scripta Materialia 130, 96 (2017).
- [60] G. Laplanche, A. Kostka, C. Reinhart, J. Hunfeld, G. Eggeler, and E. George, Reasons for the superior mechanical properties of medium-entropy crconi compared to high-entropy crmnfeconi, Acta Materialia 128, 292 (2017).
- [61] S. Liu, Y. Wu, H. Wang, J. He, J. Liu, C. Chen, X. Liu, H. Wang, and Z. Lu, Stacking fault energy of face-centered-cubic high entropy alloys, Intermetallics 93, 269 (2018).
- [62] A. M. Z. Tan, C. Woodward, and D. R. Trinkle, Dislocation core structures in ni-based superalloys computed using a density functional theory based flexible boundary condition approach, Phys. Rev. Mater. 3, 033609 (2019).
- [63] D. Bacon, D. Barnett, and R. O. Scattergood, Anisotropic continuum theory of lattice defects, Progress in Materials Science 23, 51 (1980).
- [64] C. Niu, C. R. LaRosa, J. Miao, M. J. Mills, and M. Ghazisaeidi, Magnetically-driven phase transformation strengthening in high entropy alloys, Nature communications 9, 1363 (2018).
- [65] H. Deng, M. Wang, Z. Xie, T. Zhang, X. Wang, Q. Fang, and Y. Xiong, Enhancement of strength and ductility in nonequiatomic cocrni medium-entropy alloy at room temperature via transformation-induced plasticity, Materials Science and Engineering: A 804, 140516 (2021).
- [66] F. G. Coury, D. Santana, Y. Guo, J. Copley, L. Otani, S. Fonseca, G. Zepon, C. Kiminami, M. Kaufman, and A. Clarke, Design and in-situ characterization of a strong and ductile co-rich multicomponent alloy with transformation induced plasticity, Scripta Materialia 173, 70 (2019).
- [67] F. G. Coury, K. D. Clarke, C. S. Kiminami, M. J. Kaufman, and A. J. Clarke, High throughput discovery and design of strong multicomponent metallic solid solutions, Scientific reports 8, 8600 (2018).
- [68] Z. Yang, S. Lu, Y. Tian, Z. Gu, J. Sun, and L. Vitos, Theoretical and experimental study of phase transformation and twinning behavior in metastable high-entropy alloys, Journal of Materials Science & Technology 99, 161 (2022).
- [69] S. Yoshida, T. Ikeuchi, Y. Bai, and N. Tsuji, Effect of cobalt-content on mechanical properties of non-equiatomic cocrni medium entropy alloys, MATERIALS TRANSACTIONS 61, 587 (2020).
- [70] D. Huang, Y. Zhuang, and C. Wang, Advanced mechanical properties obtained via accurately tailoring stacking fault energy in co-rich and ni-depleted coxcr33ni67-x medium-entropy alloys, Scripta Materialia 207, 114269 (2022).
- [71] G. Bertoli, L. B. Otani, A. J. Clarke, C. S. Kiminami, and F. G. Coury, Hallpetch and grain growth kinetics of the low stacking fault energy trip cr40co40ni20 multi-principal element alloy, Applied Physics Letters 119, 061903 (2021).
- [72] R. Madhavan, R. Ray, and S. Suwas, Texture transition in cold-rolled nickel40wt.% cobalt alloy, Acta Materialia 74, 151

(2014).

- [73] S. Yoshida, T. Ikeuchi, Y. Bai, A. Shibata, N. Hansen, X. Huang, and N. Tsuji, Deformation microstructures and strength of face-centered cubic high/medium entropy alloys, IOP Conference Series: Materials Science and Engineering 580, 012053

(2019).

- [74] P. M. Larsen, S. Schmidt, and J. Schiotz, Robust structural identification via polyhedral template matching, Modelling and Simulation in Materials Science and Engineering 24, 055007 (2016).
- [75] K. Ioroi, Y. Aono, X. Xu, T. Omori, and R. Kainuma, Melting Point of Pure Cr and Phase Equilibria in the Cr-Si Binary System, J. Phase Equilib. Diffus. 43, 229 (2022).
- [76] Z. Wu, H. Bei, G. Pharr, and E. George, Temperature dependence of the mechanical properties of equiatomic solid solution alloys with face-centered cubic crystal structures, Acta Materialia 81, 428 (2014).
- [77] J. Li, Q. Fang, B. Liu, and Y. Liu, Transformation induced softening and plasticity in high entropy alloys, Acta Materialia 147, 35 (2018).
- [78] H. Xie, F. Yin, T. Yu, G. Lu, and Y. Zhang, A new strain-rate-induced deformation mechanism of cu nanowire: Transition from dislocation nucleation to phase transformation, Acta Materialia 85, 191 (2015).
- [79] X. Guo, Z. Luo, X. Li, and K. Lu, Plastic deformation induced extremely fine nano-grains in nickel, Materials Science and Engineering: A 802, 140664 (2021).
- [80] Z. Luo, X. Guo, J. Hou, X. Zhou, X. Li, and K. Lu, Plastic deformation induced hexagonal-close-packed nickel nano-grains, Scripta Materialia 168, 67 (2019).
- [81] H. He, M. Naeem, F. Zhang, Y. Zhao, S. Harjo, T. Kawasaki, B. Wang, X. Wu, S. Lan, Z. Wu, W. Yin, Y. Wu, Z. Lu, J.-J. Kai, C.-T. Liu, and X.-L. Wang, Stacking fault driven phase transformation in crconi medium entropy alloy, Nano Letters 21, 1419 (2021), pMID: 33464087.
- [82] A. P. Thompson, H. M. Aktulga, R. Berger, D. S. Bolintineanu, W. M. Brown, P. S. Crozier, P. J. in ’t Veld, A. Kohlmeyer, S. G. Moore, T. D. Nguyen, R. Shan, M. J. Stevens, J. Tranchida, C. Trott, and S. J. Plimpton, Lammps - a flexible simulation tool for particle-based materials modeling at the atomic, meso, and continuum scales, Computer Physics Communications 271, 108171 (2022).
- [83] K. Xu, H. Bu, S. Pan, E. Lindgren, Y. Wu, Y. Wang, J. Liu, K. Song, B. Xu, Y. Li, T. Hainer, L. Svensson, J. Wiktor,


- R. Zhao, H. Huang, C. Qian, S. Zhang, Z. Zeng, B. Zhang, B. Tang, Y. Xiao, Z. Yan, J. Shi, Z. Liang, J. Wang, T. Liang,
- S. Cao, Y. Wang, P. Ying, N. Xu, C. Chen, Y. Zhang, Z. Chen, X. Wu, W. Jiang, E. Berger, Y. Li, S. Chen, A. J. Gabourie, H. Dong, S. Xiong, N. Wei, Y. Chen, J. Xu, F. Ding, Z. Sun, T. Ala-Nissila, A. Harju, J. Zheng, P. Guan, P. Erhart, J. Sun, W. Ouyang, Y. Su, and Z. Fan, Gpumd 4.0: A high-performance molecular dynamics package for versatile materials


simulations with machine-learned potentials, Materials Genome Engineering Advances 3, e70028 (2025).

- [84] Z. Meng, K. Zongo, E. Torres, C. Maxwell, R. Grant, and L. K. Be´land, A kokkos-accelerated moment tensor potential implementation for lammps, SoftwareX 33, 102524 (2026).
- [85] J. P. Perdew, K. Burke, and M. Ernzerhof, Generalized gradient approximation made simple, Phys. Rev. Lett. 77, 3865

(1996).

- [86] P. E. Blo¨chl, Projector augmented-wave method, Phys. Rev. B 50, 17953 (1994).
- [87] G. Kresse and J. Hafner, Ab initio molecular dynamics for liquid metals, Phys. Rev. B 47, 558 (1993).
- [88] G. Kresse and J. Furthm¨uller, Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set, Phys. Rev. B 54, 11169 (1996).
- [89] G. Kresse and J. Furthm¨uller, Efficiency of ab-initio total energy calculations for metals and semiconductors using a plane-wave basis set, Computational Materials Science 6, 15 (1996).
- [90] G. Kresse and J. Hafner, Ab initio molecular-dynamics simulation of the liquid-metal–amorphous-semiconductor transition in germanium, Phys. Rev. B 49, 14251 (1994).
- [91] G. Kresse and D. Joubert, From ultrasoft pseudopotentials to the projector augmented-wave method, Phys. Rev. B 59, 1758 (1999).
- [92] M. S. Nitol, A. Tamm, S. Mubassira, S. Xu, and S. J. Fensin, Achieving DFT accuracy in short range ordering and stacking fault energy using moment tensor potential for CoCrFeNi and CoCrNi (2025), arXiv:2509.11231 [cond-mat].
- [93] A. P. Barto´k, R. Kondor, and G. Csa´nyi, On representing chemical environments, Phys. Rev. B 87, 184115 (2013).
- [94] J. Laakso, L. Himanen, H. Homm, E. V. Morooka, M. O. J¨ager, M. Todorovic´, and P. Rinke, Updates to the dscribe library: New descriptors and derivatives, The Journal of Chemical Physics 158 (2023).
- [95] Y.-C. Wu, X. Chang, Z. G. Yu, Y.-W. Zhang, and J.-L. Shao, Revealing the role of al4c3 in the mechanical behavior of aluminum/graphene composites through machine learning potential-driven atomistic simulations, Mechanics of Materials 209, 105428 (2025).
- [96] A. Stukowski, Visualization and analysis of atomistic simulation data with ovitothe open visualization tool, Modelling and Simulation in Materials Science and Engineering 18, 015012 (2009).
- [97] Y.-C. Wu and J.-L. Shao, mdapy: A flexible and efficient analysis software for molecular dynamics simulations, Computer Physics Communications 290, 108764 (2023).
- [98] P. Hirel, Atomsk: A tool for manipulating and converting atomic data files, Computer Physics Communications 197, 212


(2015).

