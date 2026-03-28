# arXiv:2603.25330v1[cond-mat.mtrl-sci]26 Mar 2026

## Highlights

Machine-Learned Interatomic Potentials for Predicting Physicochemical Properties of Molten Metal–Salt Systems for Calcium Electrolysis.

M. Polovinkin, N. Rybin, D. Maksimov, F. Valiev, A. Khudorozhkova, M. Laptev, A. Rudenko, A. Shapeev

- • Moment Tensor Potentials for the molten Ca-Cu alloy and the CaCl2KCl molten salt are developed for the first time
- • The Moment Tensor Potential for the Ca-Cu alloy is compositionally transferable
- • The same potentials are used to calculate structural, thermodynamic, and transport properties of the systems
- • The ionic conductivity of the CaCl2-KCl molten salt predicted by Moment Tensor Potential molecular dynamics agrees with experiment


## Machine-Learned Interatomic Potentials for Predicting Physicochemical Properties of Molten Metal–Salt Systems for Calcium Electrolysis.

M. Polovinkina,b, N. Rybina,b, D. Maksimovb, F. Valievc, A. Khudorozhkovac, M. Laptevc, A. Rudenkoc, A. Shapeeva,b

aSkolkovo Institute of Science and Technology, Skolkovo Innovation Center, Bolshoy Bulvar, 30, Moscow, 143026, Russia bDigital Materials LLC, Odintsovo, Kutuzovskaya str. 4A, Moscow Region, 143001, Russia cInstitute of High Temperature Electrochemistry, Ural Branch of the Russian Academy of Sciences, Academicheskaya Street, 20, Yekaterinburg, 620066, Russia

### Abstract

The design of efficient electrolysis devices for pure metal production requires accurate data on the properties of the melts used in the process. This work focuses on two key systems for calcium production: the molten Ca-Cu alloy and the CaCl2-KCl electrolyte. High-temperature experiments are often expensive and time-consuming; however, we demonstrate that molecular dynamics (MD) simulations driven by machine-learned Moment Tensor Potentials (MTPs), trained on highly accurate density functional theory data, offer an effective and accurate alternative. Our MTP-driven MD simulations accurately reproduce the structural, thermodynamic, and transport properties across a range of temperatures and compositions relevant to electrolysis systems. We report calculated densities, radial distribution functions, heat capacities, thermal conductivities, ionic conductivities (for the electrolyte), viscosities, and diffusion coefficients, with deviations from experimental data within 20%. The strong agreement between calculations and experiments validates the proposed approach, establishing a robust framework for the computational exploration and optimization of liquid systems in metallurgical applications.

Keywords: electrolysis, molten salts, liquid alloys, molecular dynamics, machine learning interatomic potentials, moment tensor potential, physicochemical

Preprint submitted to Electrochimica Acta March 27, 2026

properties, ionic conductivity PACS: 0000, 1111 2000 MSC: 0000, 1111

### 1. Introduction

Metallic calcium is a critical element with a wide range of industrial applications, including steelmaking, battery production, and the synthesis of advanced alloys and magnetic materials [1, 2, 3, 4]. As demand grows, improving calcium production methods is becoming increasingly important. The primary industrial route for producing high-purity calcium is molten salt electrolysis. This process involves two high-temperature liquid phases: a molten Ca-Cu alloy acting as a liquid cathode and a CaCl2-based molten salt electrolyte [5].

Optimizing the efficiency of production processes is a key industrial objective. Multiphysics modeling using digital twins can greatly assist in these efforts [6]. However, digital twins require precise knowledge of the structural, thermodynamic, and transport properties of both the electrolyte and the liquid cathode under operating conditions. This includes the temperature dependence of key properties such as density, viscosity, diffusion coefficients, thermal conductivity, heat capacity, and ionic conductivity.

To the best of our knowledge, a gap exists in the available data for several physicochemical properties of the liquid Ca-Cu alloy and CaCl2-KCl molten salt. The temperature dependence of density has been measured for several compositions of molten Ca-Cu alloys [7, 3, 8]. In contrast, structural investigations have been limited to pure Ca and Cu melts [9, 10], leaving a gap in our understanding of the alloy structure. The heat capacity of Ca-Cu alloys remains unknown, and reported diffusion coefficients and viscosities require refinement, as they are available from only a single source [3] and contain inconsistencies. While the properties of the CaCl2-KCl molten salts have been studied for other compositions [11, 12, 13], data for the specific 80:20 mass% ratio used in production are lacking.

Acquiring these data through high-temperature experiments is often resource-

intensive, expensive, and challenging, making such approaches impractical for the large-scale parameter screening—across composition, temperature, and pressure—that industrial optimization demands. Computational approaches offer a viable alternative to experiments [14]. While ab initio molecular

dynamics (AIMD) can predict physicochemical properties, its computational cost is prohibitively high for sufficient configuration sampling and for the calculation of transport properties. Molecular dynamics (MD) modeling with machine-learning interatomic potentials (MLIPs), including Moment Tensor Potentials (MTPs), offers a favorable trade-off, providing accurate modeling at a fraction of the computational cost [15, 16].

In this article, we develop and benchmark a computational methodology employing MTPs to fill data gaps for these systems. First, we construct diverse training sets from density functional theory (DFT) calculations to fit reliable potentials. We then employ MTP-MD to compute a comprehensive set of physicochemical properties for both systems involved in the electrolytic production of calcium. For the Ca-Cu alloy, we address notable gaps in the literature by reporting the composition dependence of heat capacity and by refining inconsistencies in the available viscosity and diffusion data. For the CaCl2-KCl electrolyte, we provide a complete set of properties, including ionic conductivity. To support our computational results, we conducted a series of experiments measuring the density, viscosity, and ionic conductivity of the molten salt. Combined with literature data, these results enable a proper benchmark.

The computational framework established here is both general and transferable. It can be reliably applied to calculate the physicochemical properties of other molten salts and liquid alloys, providing a powerful tool for the design of new materials and the optimization of production processes.

### 2. Methods

- 2.1. MTP fitting To calculate the physicochemical properties, we conducted the MD simu-


lation in LAMMPS [17, 18]. The MTPs, implemented in MLIP-2 [19], were used as the interaction potentials. In the MTP, the energy of an atomic configuration is represented as a sum of energies of local atomic environments. These energies are expanded through a set of basis functions, with linear coefficients determined by fitting energies, forces, and stresses to reference ones. For a comprehensive theoretical description of the MTPs, we refer the reader to the original publications [20, 19, 21].

For the systems of the Ca-Cu melt (for all compositions) and the CaCl2KCl (80:20 mass%, 28:10 in molar fractions) electrolyte, we developed potentials containing 127 and 343 parameters, respectively. The potential for

Ca-Cu liquid alloy was designed to be compositionally transferable. In the MTPs we used the Chebyshev radial basis and a cutoff distance of 5 ˚A. Potentials were trained on atomic configurations sampled from the liquid bulk phase, with the simulation cell size ensuring a minimum length of twice the cutoff distance. The MTPs were trained in a multi-stage procedure developed to ensure both accuracy and stability in MD modeling.

First, for each system, an initial training set was generated from a short

- 2 ps AIMD simulation. We sampled 150 evenly spaced atomic configurations from the last 1.5 ps of the trajectory. This set of configurations was used to train an initial MTP of level 10. To enhance the stability of the potential in MD, we employed an active learning procedure [22]. It consists of performing 100 ps isothermal-isobaric ensemble (NPT) MD modeling, during which atomic configurations with the highest extrapolation grade are automatically added to the training set.


The initial AIMD produced atomic configurations that were structurally similar. To construct diverse and representative training sets, we performed a ”resampling” step using a stable potential. For the Ca-Cu alloy, to ensure transferability across compositions, six separate 60 ps trajectories were run, with the calcium molar fraction ranging from 0.0 to 1.0 in steps of 0.2. For the molten salt, a single 300 ps trajectory was used. From these simulations, 360 (Ca-Cu) and 300 (CaCl2-KCl) atomic configurations were sampled. This approach is effective because the structural relaxation times in these molten systems are short, on the order of 5–10 ps.

Based on the collected diverse training sets, we trained new potentials of level 10. Then, we conducted active learning over a broad temperature range (900–1600 K) to enrich the training set with atomic configurations at various temperatures. Finally, higher-level potentials were fitted to the enriched training set and underwent a final round of active learning to guarantee their stability. This pipeline ensures that the potentials are trained on sets covering

- a broad chemical space and stable enough to run long MD simulations for the calculation of physicochemical properties.


Reference energies, forces, and stresses for MTP fitting were computed within the DFT framework in the Vienna Ab initio Simulation Package (VASP) [23] employing the projector-augmented-wave and the GGA approximation with the PBE functional [24]. The plane-wave basis kinetic energy cutoff was set to 520 eV and 500 eV for the liquid alloy and molten salt, respectively. A 1 × 1 × 1 Γ-centered k-point mesh was used to sample the Brillouin zone. The width of smearing in the Gaussian method was chosen

to be 0.05 eV. The vdW-dispersion correction term was accounted for by the DFT-D3 method of Grimme [25, 26] for the Ca-Cu liquid alloy and by the dDsC method [27, 28] for the molten salt. The choice of dDsC was based on the results of our in-house tests conducted on the AlF3-NaF molten salt. Details are provided in Section 1 of the Supplementary Information.

To quantify the accuracy of the MTP in reproducing the DFT results, we computed the root-mean-square errors (RMSE) for energies and forces between the MTP and reference DFT calculations on an independent validation set collected from MD with the final potentials.

- 2.2. Physicochemical properties calculation


In MTP-driven MD simulations, we used a 1 fs time step and periodic boundary conditions. Initial configurations were prepared using the PACKMOL [29] package. The Nose–Hoover thermostat and barostat [30, 31] with damping parameters set to 0.1 ps and 1 ps, respectively, were used to maintain a constant temperature and a pressure of 0 bar. Properties were calculated in simulation cells containing 800 and 832 atoms for the liquid alloy and the molten salt, respectively. Prior to the production run, the systems were equilibrated for 50 ps.

Densities of the systems were calculated in the NPT ensemble. The total number of frames analyzed for every composition and temperature was 500; these were evenly sampled from 500 ps (for the liquid alloy) and 1 ns (for the molten salt) long trajectories. The local structure was analyzed via partial radial distribution functions (RDFs). These distribution functions were calculated from 100 configurations evenly sampled from 100 ps equilibrium MD trajectories. For the metallic melt, we employed larger 4000-atom systems for the RDF analysis to access longer-range distances.

The specific heat capacity at constant pressure, CP, was calculated by direct estimation of the slope of the temperature T dependence of enthalpy H:

H(T) = CP · T + const. (1)

In Equation 1, enthalpy H is substituted by internal energy E in our calculations, since the simulations were carried out at a pressure of 0 bar.

For the studied systems, the temperature dependencies of viscosity, diffusion coefficients, and ionic conductivity (for the molten salt system) were calculated using MTP-MD. We employed the same trajectories that were used for the density calculations.

For viscosity calculations, we employed the Green–Kubo (GK) theory [32, 33, 34, 35, 36], computing the integral of the pressure tensor autocorrelation function. The integral was truncated after 5 ps for the liquid alloy and 25 ps for the molten salt, based on our convergence tests of the autocorrelation decay. The diffusion coefficients for each atomic species were obtained from the slope of the mean-squared displacement in the diffusive regime, according to the Einstein relation [36].

For the Ca-Cu molten alloy, we tested the Stokes–Einstein–Sutherland (SES) equation

kBT bπηRh

, (2)

D =

where D is the self-diffusion coefficient of the particle, kB is the Boltzmann constant, T is the temperature in the system, η is the viscosity of the system, Rh is the hydrodynamic radius of the particle. As we calculated viscosity and diffusion coefficients independently in our methodology, we checked whether

- b = 4 or b = 6 is more appropriate. For the molten salt we calculated the temperature dependence of ionic


conductivity, σ. We employed the GK relation:

1 3V kBT

σ =

∞

dt⟨Jq(t) · Jq(0)⟩, (3)

0

where V is the volume of the system, kB is the Boltzmann constant, T is the temperature in the system. Jq(t) is the charge flux

Jq(t) = e

N

zivi(t), (4)

i=1

where e is the elementary charge, N counts all the ions in the system, zi and vi are the charge and velocity of a particle. Ions were assigned fixed partial charges in our calculations: zCa = +2, zK = +1, and zCl = −1. We truncated the GK integral at 25 ps. Additionally, for calculations of ionic conductivity we tested the Nernst–Einstein (NE) formula:

e2 V kBT k

σ =

Nkzk2Dk, (5)

where e is the electron charge, Nk is the number of k species ions, zk is the charge of k species ions, Dk is the diffusion coefficient of k species ions. The

NE formula is an approximation, which is valid in the absence of correlations in ionic motion. We compared the approach accounting for all correlations (the GK method) with the NE formalism.

Thermal conductivity was computed using the non-equilibrium MullerPlathe method [37], which imposes a heat flux and measures the resulting temperature gradient via Fourier’s law. We used a 3.6 nm × 3.6 nm × 18 nm cell for the simulations, with a temperature gradient established along the z-axis. After a 500 ps equilibration, data were collected over a 2000 ps production run. The thermal conductivity was computed only for the molten salt. We omitted this property for the Ca-Cu alloy because the ionic contribution accounted for by classical MD is negligible compared to the electronic contribution. The latter requires additional DFT calculations beyond the scope of this work [38, 39].

- 2.3. Experimental measurements To validate the molecular dynamics calculations, several properties of the


CaCl2-KCl molten salt relevant to electrolysis were measured experimentally. The temperature dependencies of density, viscosity, and ionic conductivity were obtained. Details of the experimental techniques and setups are provided in Section 2 of the Supplementary Information.

### 3. Results and discussion

- 3.1. Potential fitting Using the strategies described in Section 2, we successfully developed


MTPs for both the Ca-Cu liquid alloy and the CaCl2-KCl molten salt. The resulting training and validation set sizes are reported in Table 1, along with the errors in energies per atom and forces acting on atoms. Correlation plots between the DFT and MTP are presented in Section 3 of the Supplementary Information for both systems.

For both systems, we obtained errors of approximately 5 meV/atom in energies per atom. The forces in atomic configurations are also reproduced with RMSEs of 80 and 136 meV/˚A for the Ca-Cu alloy and the CaCl2-KCl electrolyte, respectively. These low errors confirm that the MTPs accurately reproduce the DFT data. Moreover, for the liquid alloy system, the potential is able to describe interactions in configurations spanning the entire range of compositions. This establishes a basis for the MTP for Ca-Cu to be compositionally transferable.

Since the obtained potentials reproduce the interactions accurately, we expect the structural and dynamic properties of the liquids to be well-reproduced. A force error on the order of 100 meV/˚A has been shown to be sufficient for reproducing of the properties of atomic systems [40, 41, 42]. This provides a reliable foundation for calculating physicochemical properties.

Table 1: Summary on the trained potentials and their errors in validation. Ntrain – number of configurations in the training set. Nvalid – number of configurations in the validation set. RMSE is reported as the error of potential for both energies and forces.

|System<br><br>|Level|Ntrain<br><br>|Nvalid<br><br>|Energy error, meV/atom|Force error, meV/˚A|
|---|---|---|---|---|---|
|Ca-Cu<br><br>|12|463|240<br><br>|5.4<br><br>|80|
|CaCl2-KCl|14|591|200<br><br>|5.0<br><br>|136|


- 3.2. Physicochemical properties of Ca-Cu liquid alloy We benchmarked our potential against the structural properties of the


melt. Density was calculated for temperatures ranging from 900 to 1400 K. At 1400 K, all the compositions are liquid. As the temperature decreases, the range of liquid compositions diminishes [43]. Therefore, in accordance with the phase diagram, we calculated the density of the alloy only for the liquid phase.

In Figure 1, we present the results of our MTP-MD calculations. The potential reproduces the density at lower temperatures (900 and 1000 K) with good accuracy. For alloys with a calcium molar fraction from 0.5 to 0.8, the relative errors compared to literature data [3] are approximately 3–4%. The potential also reproduces the density well for pure copper. For liquid copper at T=1400 K we obtained a density of 7.93 g/cm3, while the experimental value is 7.68 g/cm3 (a relative error of 3%) [8]. However, for liquid calcium, the error is slightly higher. At a temperature of 1400 K, the experimental density is 1.31 g/cm3 [7], while the MTP-MD result is 1.44 g/cm3 (a relative error of 10%). The MTP-MD underestimates the thermal expansion of CaCu liquid alloy: at higher temperatures, the simulation overestimates the density. However, the density estimation for the temperature range relevant to electrolysis is accurate.

In Figures 2 (a) and (b), we report RDFs for liquid calcium (at 1123 K) and copper (at 1423 K) to provide additional validation of the potential, comparing RDFs to literature data [9, 44, 10]. For the RDFs of the pure

alloy melts, excellent agreement is observed between the positions of the peaks and their heights. Thus, we conclude that the MTP captures the shortrange structure of pure liquid metals. In Figures 2 (c) and (d), we report the RDFs for melts with a calcium molar fraction of 0.5 and 0.8 for the first time. In both melts, we observe a structure with local density oscillations specific to liquids. In the melt with a higher concentration of calcium, the strength of the secondary peaks decays more slowly, and more peaks in RDFs can be distinguished. The atomic radii of the species are consistent with the first peak positions in the RDFs.

Structural properties of the Ca-Cu melts are reproduced across a wide range of compositions. This provides strong evidence of the applicability of the MTP to liquid alloy systems.

The composition dependence of the specific heat capacity at constant pressure was calculated for the Ca-Cu melt. In Figure 3, we report the calculated mass-specific heat capacity in J/(kg·K). The calculations reveal that the mass-specific heat capacity increases nonlinearly with increasing calcium molar fraction. No experimental data are available for the massspecific heat capacity of Ca-Cu liquid alloys. However, the values calculated with MTP-MD fall between the experimental values for the pure melts of calcium and copper. The experimental data for pure calcium range from 798 to 948 J/(kg·K) [45]. The mass-specific heat capacity of liquid copper is reported to be 571 J/(kg·K) in Ref. [46]; in other studies, it ranges from 409 to 526 J/(kg·K) [46]. The molar-specific heat capacity in J/(mol·K) shows the opposite trend and decreases with increasing calcium concentration.

Figure 4 presents the composition dependence of viscosity, comparing our MTP-MD results with literature data from [3, 8]. Overall, the calculations show excellent agreement across all studied compositions. The viscosity exhibits an almost linear decrease with increasing calcium molar fraction. Notably, deviations from the linear trend in the literature data are most likely outliers. Thus, our model helps to resolve a physical inconsistency in the existing data. The accurate reproduction of the melt’s viscosity provides confidence in the predicted diffusion coefficients, which are shown for calcium and copper in Figure 5. The coefficients increase with higher calcium concentration, a trend that is consistent with the observed decrease in viscosity. Both dependencies are approximately linear.

To test the SES equation 2, we used the collected data. Since we obtained the diffusion coefficient and viscosity independently, we directly calculated the average value of b for each system. For the Ca-Cu liquid alloy, we obtained

![image 1](Polovinkin et al._2026_Machine-Learned Interatomic Potentials for Predicting Physicochemical Properties of Molten Metal-Sal_images/imageFile1.png)

- Figure 1: Composition dependence of Ca-Cu liquid alloy density at temperatures 900, 1000, 1200, and 1400 K. Experimental data for Ca-Cu liquid alloy are taken from [7, 3, 8].


a value of 3.7 ± 0.4. Slip boundary conditions (b=4) are more appropriate for these alloys than the widely used stick conditions (b=6). This conclusion is consistent with findings for other liquid alloys [47, 48]. This finding is significant because the SES relation is widely used to estimate diffusion coefficients from viscosity data. Consequently, our results provide a refined value of b that can be used to correct the diffusion coefficients derived from the viscosity data in [3] and for further calculations in other alloys.

The agreement of the calculated properties of the Ca-Cu liquid alloy

![image 2](Polovinkin et al._2026_Machine-Learned Interatomic Potentials for Predicting Physicochemical Properties of Molten Metal-Sal_images/imageFile2.png)

- Figure 2: RDFs for liquid alloys systems. (a) RDF in pure copper at temperature 1423 K. Experimental curve from [9]. (b) RDF in pure calcium at temperature 1123 K. Experimental curve from [10]. (c-d) RDFs in Ca-Cu liquid alloy at molar fraction of calcium 0.5 and 0.8, temperature 1000 K.


demonstrates that we have successfully developed a machine-learned potential that is reliable and compositionally transferable. Its accuracy across this range of structural, thermodynamic, and transport properties confirms the MTP’s robustness for simulating liquid alloy systems.

- 3.3. Physicochemical properties of the CaCl2-KCl molten salt Next, we tested the calculation of physicochemical properties using the


MTP prepared for the molten salt system. The density of the electrolyte was calculated over the temperature range from 900 to 1100 K. In Figure 6 (a), we report the temperature dependence of the density at a fixed composition. Our calculations are in good agreement with the experimental measurements conducted in this work, with a relative error of approximately 2–3%. This

![image 3](Polovinkin et al._2026_Machine-Learned Interatomic Potentials for Predicting Physicochemical Properties of Molten Metal-Sal_images/imageFile3.png)

Figure 3: Composition dependence of mass-specific heat capacity for Ca-Cu melt.

quantitative validation confirms the reliability of our approach using MD with the MTP for the structural properties of molten salts.

In the RDFs presented in Figure 6 (b), calculated at a temperature of 1000 K, we observe that calcium coordinates with chlorine atoms more strongly than potassium. The Ca–Cl peak is sharper and more intense than the K–Cl peak, which indicates stronger and more localized bonding between calcium and chlorine. The positions of the peaks are consistent with the atomic radii.

The MTP-MD specific heat capacity of the molten salt is 980±10 J/(kg·K),

which agrees well with the experimental value of approximately 960 J/(kg·K) reported for similar compositions [49]. At 1000 K, the thermal conductivity was determined to be 0.438 W/(m·K). This result is consistent with a previous computational study that employed the more expensive DeepMD potential [13] and with the experimental value of 0.436 W/(m·K) for the

![image 4](Polovinkin et al._2026_Machine-Learned Interatomic Potentials for Predicting Physicochemical Properties of Molten Metal-Sal_images/imageFile4.png)

- Figure 4: Composition dependence of viscosity at temperatures 1000, 1200, and 1400 K. Experimental data for Ca-Cu liquid alloy is taken from [3, 8].


pure CaCl2 molten salt at 1000 K [50]. These agreements demonstrate that the MTP-MD accurately reproduces the thermodynamic properties and heat transport phenomena in the CaCl2-KCl system.

Next, we calculated the transport properties of the CaCl2-KCl molten salt, which are key for electrolysis efficiency: viscosity, diffusion coefficients, and ionic conductivity. In Figures 7, we report the viscosity (a) and diffusion coefficients of atoms in the molten salt (b). The viscosity of the electrolyte decreases with rising temperature, as expected. We observe excellent agreement between the MTP-MD calculations and the experimental data for viscosity, which were obtained for this study. The MTP-MD demonstrates an ability to capture subtle physicochemical trends in molten salts. The achieved agreement for viscosity provides a solid foundation for reliable diffusion coefficient

![image 5](Polovinkin et al._2026_Machine-Learned Interatomic Potentials for Predicting Physicochemical Properties of Molten Metal-Sal_images/imageFile5.png)

- Figure 5: Diffusion coefficients of Ca-Cu liquid alloy at temperatures 900, 1000, 1200, and 1400 K. (a) Composition dependence of calcium diffusion coefficient. (b) Composition dependence of copper diffusion coefficient.

![image 6](Polovinkin et al._2026_Machine-Learned Interatomic Potentials for Predicting Physicochemical Properties of Molten Metal-Sal_images/imageFile6.png)

- Figure 6: (a) Temperature dependence of the CaCl2-KCl molten salt density. MTP-MD results (pink squares) are compared with our experimental data (blue line). (b) CaCl2-KCl molten salt RDFs calculated at temperature 1000 K.


calculations. In the temperature dependence of the diffusion coefficients, we observe that calcium atoms are less mobile than potassium. While potassium has a larger atomic radius and would be expected to be less mobile, our result indicates that in CaCl2-KCl, calcium ions coordinate with chlorine atoms and consequently have a larger effective hydrodynamic radius.

As shown in Figure 8, the ionic conductivity exhibits a linear increase with temperature, a trend captured by both the GK and NE formalisms. This correctly reproduces the expected thermodynamic behavior, which reflects

enhanced ion mobility at higher temperatures (see Figure 7).

The GK method consistently underestimates the ionic conductivity by 10–25 S/m, resulting in a relative error of approximately 6–20%. However, with the respect to uncertainty of calculations, the agreement between the calculations and experimental measurements are reached. Relative errors are lower for the NE method, which are 4–15% over the measured temperatures; however, the NE approach predicts an incorrect slope for the temperature dependence of ionic conductivity, as shown by the fit in Figure 8. This leads to larger errors in the high-temperature region, where the experimental data are extrapolated. The GK method does not have this disadvantage. Moreover, the data on diffusion coefficients from Ref. [13] indicate that at higher calcium concentrations, the atomic coordination is higher, which will lead to larger errors for the NE method. Therefore, we still recommend using the method that accounts for all the correlations in ionic motion. In Section

- 4 of Supplementary Information the additional details on the conductivity calculations using the GK method are provided. The underestimation of ionic conductivity by GK can be attributed to the system size dependence of ionic conductivity, which will be studied extensively in future research.


In summary, the MTP-MD approach provides a robust framework for predicting properties of molten salts. It accurately reproduces densities, viscosities, thermal conductivities, and ionic conductivities, along with their correct thermodynamic trends.

![image 7](Polovinkin et al._2026_Machine-Learned Interatomic Potentials for Predicting Physicochemical Properties of Molten Metal-Sal_images/imageFile7.png)

##### Figure 7: Transport properties of the CaCl2-KCl molten salt in the temperature range of900-1100 K. (a) Viscosity as a function of temperature. Pink circles show the MTP-MDresults, while the blue line represents our experimental data. (b) Diffusion coefficients asa function of temperature for Ca2+ (pink squares), K+ (blue triangles), and Cl− (orangetriangles) ions.

![image 8](Polovinkin et al._2026_Machine-Learned Interatomic Potentials for Predicting Physicochemical Properties of Molten Metal-Sal_images/imageFile8.png)

##### Figure 8: Temperature dependence of ionic conductivity in the CaCl2-KCl molten salt.Results from the Green-Kubo (GK, pink squares) and Nernst-Einstein (NE, golden crosses)methods are compared with experimental data (blue line) obtained in this work. Solidlines represent the calculated or experimental data, while dashed lines show linear fits.

### 4. Conclusion

In this work, we demonstrate that MTP-MD provides an accurate and efficient framework for simulating key systems in calcium electrolysis. Applied to the molten Ca-Cu cathode, the MTP’s compositional transferability allows a single potential to reproduce physicochemical properties across the entire liquid composition range. For the CaCl2-KCl molten salt electrolyte, we show that a local MTP effectively captures the structure and dynamics of the ionic melt. The results indicate that the MTP implicitly handles shortrange electrostatics, enabling stable simulations. Furthermore, MTP-MD is significantly faster than AIMD.

An additional advantage of our approach is the use of MTP-MD to compute a wide range of physicochemical properties without fitting to experimental data. The calculated densities and radial distribution functions agree well with available experimental data, with errors of 3–4% in the temperature range relevant to electrolysis. We report specific heat capacities for both systems that are in quantitative agreement with the existing data. MTPMD accurately predicts transport properties, including viscosity and ionic conductivity (with a maximal relative error of 20%). This confirms that MTP-MD reliably captures both the structure and dynamics of these melts.

The success in modeling CaCl2-KCl promises expansion to related electrolytes such as CaO-CaCl2-KCl, CaCl2-CaF2, and CaCl2-NaCl, enabling the prediction of how additives affect properties relevant to electrolysis. More broadly, the approach can be applied to optimize other high-temperature molten salt processes, e.g., production of aluminum, magnesium, and other metals.

Building on this validated foundation, the framework can be extended to tackle other critical challenges, such as calculating solubility and surface tension. Prior studies have successfully reported computed surface tension in alloys using MD [51, 52], and given the accuracy of our MTPs in the bulk phase, we anticipate no impediment to modeling vacuum–alloy interfaces. Calculating solubility, as attempted for molten salt reactor-relevant salts [53], is a crucial next step, as it directly impacts electrolysis efficiency; for example, lower calcium solubility in the melt hinders Ca-Cu alloy enrichment and wastes energy. The calculation of these properties represents a clear and important direction for future work.

### 5. Data availability

MTPs for the Ca-Cu and CaCl2-KCl systems, along with the corresponding training and validation sets, are available in the GitHub repository.

### Author Contributions

Mikhail Polovinkin: methodology, investigation, validation, conceptualization, data curation, writing — original draft. Nikita Rybin: conceptualization, methodology, supervision, writing — review and editing. Dmitrii Maksimov: conceptualization. F. Valiev: investigation. A. Khudorozhkova: investigation. M. Laptev: investigation. A. Rudenko: investigation. Alexander Shapeev: resources, funding acquisition, supervision.

### Acknowledgments

The work was supported by the grant for research centers in the field of AI provided by the Ministry of Economic Development of the Russian Federation in accordance with the agreement 000000C313925P4F0002 and the agreement with Skoltech №139-10-2025-033.

### References

- [1] E. Naumova, Use of calcium in alloys: from modifying to alloying, Russian Journal of Non-Ferrous Metals 59 (3) (2018) 284–298.
- [2] S. E. Hluchan, K. Pomerantz, Calcium and Calcium Alloys, John Wiley & Sons, Ltd, 2006. doi:https://doi.org/10.1002/14356007.a04_ 515.pub2.
- [3] Y. Zaikov, N. Shurov, A. Suzdaltsev, Vysokotemperaturnaya elektrokhimiya kaltsiya (High-temperature electrochemistry of calcium), Editorship-Publishing Department of UB RAS, Yekaterinburg, 2013. doi:10.13140/RG.2.1.3905.2242.
- [4] R. J. Gummow, G. Vamvounis, B. M. Kannan, Y. He, Calcium-ion batteries: current state-of-the-art and future perspectives, Advanced Materials 30 (39) (2018) 1801702.
- [5] Y. P. Zaikov, V. P. Batukhtin, N. I. Shurov, A. V. Suzdaltsev, High-temperature electrochemistry of calcium, Electrochemical Materials and Technologies 1 (1) (2022). doi:https://doi.org/10.15826/ elmattech.2022.1.007.
- [6] D. Vergara, A. del Bosque, P. Fern´andez-Arias, A decade of digital twins in materials science and engineering, Computers, Materials and Continua 85 (1) (2025) 41–64. doi:https: //doi.org/10.32604/cmc.2025.067881. URL https://www.sciencedirect.com/science/article/pii/ S1546221825008331
- [7] S. Hiemstra, D. Prins, G. Gabrielse, J. B. V. Zytveld, Densities of liquid metals: calcium, strontium, barium, Physics and Chemistry of Liquids 6 (4) (1977) 271–279. doi:10.1080/00319107708084145.
- [8] M. J. Assael, A. E. Kalyva, K. D. Antoniadis, R. M. Banish, I. Egry, J. Wu, E. Kaschnitz, W. A. Wakeham, Reference data for the density and viscosity of liquid copper and liquid tin, Journal of Physical and Chemical Reference Data 39 (3) (2010) 033105. doi:10.1063/1. 3467496.


- [9] Y. Waseda, K. Yokoyama, K. Suzuki, The structure of liquid alkaline earth metals, The Philosophical Magazine: A Journal of Theoretical Experimental and Applied Physics 30 (5) (1974) 1195–1198. doi:10. 1080/14786437408207275.
- [10] Y. Waseda, The structure of non-crystalline materials mcgraw-hill, New York (1980) 18.
- [11] G. Janz, Thermodynamic and Transport Properties for Molten Salts: Correlation Equations for Critically Evaluated Density, Surface Tension, Electrical Conductance, and Viscosity Data, no. 17 in Journal of physical and chemical reference data, American Chemical Society and the American Institute of Physics, 1988. URL https://books.google.ru/books?id=qSXxAAAAMAAJ
- [12] M. Smirnov, V. Khokhlov, E. Filatov, Thermal conductivity of molten alkali halides and their mixtures, Electrochimica Acta 32 (7) (1987) 1019–1026. doi:https://doi.org/10.1016/0013-4686(87)90027-2. URL https://www.sciencedirect.com/science/article/pii/ 0013468687900272
- [13] M. Bu, W. Liang, G. Lu, J. Yu, Local structure elucidation and properties prediction on kcl–cacl2 molten salt: A deep potential molecular dynamics study, Solar Energy Materials and Solar Cells 232 (2021)

111346. doi:https://doi.org/10.1016/j.solmat.2021.111346. URL https://www.sciencedirect.com/science/article/pii/ S0927024821003883

- [14] T. Porter, M. M. Vaka, P. Steenblik, D. Della Corte, Computational methods to simulate molten salt thermophysical properties, Communications Chemistry 5 (1) (2022) 69.
- [15] Y. Zuo, C. Chen, X. Li, Z. Deng, Y. Chen, J. Behler, G. Csanyi, A. V. Shapeev, A. P. Thompson, M. A. Wood, et al., Performance and cost assessment of machine learning interatomic potentials, The Journal of Physical Chemistry A 124 (4) (2020) 731–745.
- [16] R. Jacobs, D. Morgan, S. Attarian, J. Meng, C. Shen, Z. Wu, C. Y. Xie, J. H. Yang, N. Artrith, B. Blaiszik, G. Ceder, K. Choudhary, G. Csanyi, E. D. Cubuk, B. Deng, R. Drautz, X. Fu, J. Godwin,


V. Honavar, O. Isayev, A. Johansson, B. Kozinsky, S. Martiniani, S. P. Ong, I. Poltavsky, K. Schmidt, S. Takamoto, A. P. Thompson, J. Westermayr, B. M. Wood, A practical guide to machine learning interatomic potentials – status and future, Current Opinion in Solid State and Materials Science 35 (2025) 101214. doi:https://doi.org/10.1016/j.cossms.2025.101214.

URL https://www.sciencedirect.com/science/article/pii/ S1359028625000014

- [17] S. Plimpton, Fast parallel algorithms for short-range molecular dynamics, Journal of Computational Physics 117 (1) (1995) 1–19. doi:https: //doi.org/10.1006/jcph.1995.1039.
- [18] A. P. Thompson, H. M. Aktulga, R. Berger, D. S. Bolintineanu, W. M. Brown, P. S. Crozier, P. J. in ’t Veld, A. Kohlmeyer, S. G. Moore, T. D. Nguyen, R. Shan, M. J. Stevens, J. Tranchida, C. Trott, S. J. Plimpton, Lammps - a flexible simulation tool for particle-based materials modeling at the atomic, meso, and continuum scales, Computer Physics Communications 271 (2022) 108171. doi:https://doi.org/10.1016/ j.cpc.2021.108171.
- [19] I. S. Novikov, K. Gubaev, E. V. Podryabinkin, A. V. Shapeev, The mlip package: moment tensor potentials with mpi and active learning, Machine Learning: Science and Technology 2 (2) (2020) 025002. doi: 10.1088/2632-2153/abc9fe.
- [20] A. V. Shapeev, Moment tensor potentials: A class of systematically improvable interatomic potentials, Multiscale Modeling & Simulation 14 (3) (2016) 1153–1173.
- [21] E. Podryabinkin, K. Garifullin, A. Shapeev, I. Novikov, Mlip3: Active learning on atomic environments with moment tensor potentials, The Journal of Chemical Physics 159 (8) (2023)

084112. arXiv:https://pubs.aip.org/aip/jcp/article-pdf/doi/ 10.1063/5.0155887/18099231/084112\_1\_5.0155887.pdf, doi:10. 1063/5.0155887.

URL https://doi.org/10.1063/5.0155887

- [22] E. V. Podryabinkin, A. V. Shapeev, Active learning of linearly parametrized interatomic potentials, Computational Materials Science


- 140 (2017) 171–180. doi:https://doi.org/10.1016/j.commatsci. 2017.08.031.
- [23] G. Kresse, D. Joubert, From ultrasoft pseudopotentials to the projector augmented-wave method, Phys. Rev. B 59 (1999) 1758–1775. doi:10. 1103/PhysRevB.59.1758. URL https://link.aps.org/doi/10.1103/PhysRevB.59.1758
- [24] J. P. Perdew, K. Burke, M. Ernzerhof, Generalized gradient approximation made simple, Phys. Rev. Lett. 77 (1996) 3865–3868. doi: 10.1103/PhysRevLett.77.3865. URL https://link.aps.org/doi/10.1103/PhysRevLett.77.3865
- [25] S. Grimme, J. Antony, S. Ehrlich, H. Krieg, A consistent and accurate ab initio parametrization of density functional dispersion correction (dftd) for the 94 elements h-pu, The Journal of Chemical Physics 132 (15)

(2010) 154104. doi:10.1063/1.3382344.

- [26] S. Grimme, S. Ehrlich, L. Goerigk, Effect of the damping function in dispersion corrected density functional theory, Journal of Computational Chemistry 32 (7) (2011) 1456–1465. doi:https://doi.org/10.1002/ jcc.21759.
- [27] S. N. Steinmann, C. Corminboeuf, A generalized-gradient approximation exchange hole model for dispersion coefficients, The Journal of chemical physics 134 (4) (2011).
- [28] S. N. Steinmann, C. Corminboeuf, Comprehensive benchmarking of a density-dependent dispersion correction, Journal of chemical theory and computation 7 (11) (2011) 3567–3577.
- [29] L. Martı´nez, R. Andrade, E. G. Birgin, J. M. Martı´nez, Packmol: A package for building initial configurations for molecular dynamics simulations, Journal of Computational Chemistry 30 (13) (2009) 2157–2164. doi:https://doi.org/10.1002/jcc.21224.
- [30] W. G. Hoover, Canonical dynamics: Equilibrium phase-space distributions, Phys. Rev. A 31 (1985) 1695–1697. doi:10.1103/PhysRevA.31. 1695. URL https://link.aps.org/doi/10.1103/PhysRevA.31.1695


- [31] S. Nose, A molecular dynamics method for simulations in the canonical ensemble, Molecular Physics 100 (1) (2002) 191–198. doi:10.1080/ 00268970110089108.
- [32] M. S. Green, Markoff random processes and the statistical mechanics of time-dependent phenomena. ii. irreversible processes in fluids, The Journal of Chemical Physics 22 (3) (1954) 398–413. doi:10.1063/1. 1740082.
- [33] R. Kubo, Statistical-mechanical theory of irreversible processes. i. general theory and simple applications to magnetic and conduction problems, Journal of the Physical Society of Japan 12 (6) (1957) 570–586. doi:10.1143/JPSJ.12.570.
- [34] B. Hess, Determining the shear viscosity of model liquids from molecular dynamics simulations, The Journal of Chemical Physics 116 (1) (2002) 209–217. doi:10.1063/1.1421362.
- [35] M. Allen, D. Tildesley, Computer Simulation of Liquids, Oxford science publications, Oxford University Press, 2017. URL https://books.google.ru/books?id=nlExDwAAQBAJ
- [36] E. Maginn, R. Messerly, D. Carlson, D. Roe, J. Elliott, Best practices for computing transport properties 1. self-diffusivity and viscosity from equilibrium molecular dynamics [article v1.0], Living Journal of Computational Molecular Science 1 (01 2018). doi:10.33011/livecoms.1. 1.6324.
- [37] F. Mu¨ller-Plathe, A simple nonequilibrium molecular dynamics method for calculating the thermal conductivity, The Journal of Chemical Physics 106 (14) (1997) 6082–6085. doi:10.1063/1.473271.
- [38] D. V. Knyazev, P. R. Levashov, Thermodynamic, transport, and optical properties of dense silver plasma calculated using the greekup code

(2019).

- [39] I. S. Galtsov, V. B. Fokin, A. V. Dorovatovsky, M. A. Paramonov, G. S. Demyanov, D. V. Minakov, M. A. Sheindlin, P. R. Levashov, Thermophysical properties of solid and liquid nickel near melting point, Journal of Applied Physics 136 (14) (2024).


- [40] T. Feng, J. Zhao, W. Liang, G. Lu, Molecular dynamics simulations of lanthanum chloride by deep learning potential, Computational Materials Science 210 (2022) 111014. doi:https://doi.org/10.1016/j. commatsci.2021.111014.
- [41] L. Kamaeva, E. Tsiok, N. Chtchelkatchev, Deep machine learning, molecular dynamics and experimental studies of liquid al-cu-co alloys, Journal of Molecular Liquids 393 (2024) 123659. doi:10.1016/j. molliq.2023.123659.
- [42] N. Rybin, D. Maksimov, Y. Zaikov, A. Shapeev, Thermophysical properties of molten flinak: A moment tensor potential approach, Journal of Molecular Liquids 410 (2024) 125402. doi:https://doi.org/10.1016/ j.molliq.2024.125402.
- [43] G. Bruzzone, The binary systems calcium-copper, strontium-copper and barium-copper, Journal of the Less Common Metals 25 (4) (1971) 361–

366. doi:https://doi.org/10.1016/0022-5088(71)90178-0.

- [44] J. K. Baria, A. R. Jani, Molecular dynamics of liquid alkaline-earth metals near the melting point, Pramana 75 (4) (2010) 737–748.
- [45] R. Abdullaev, R. Khairulin, A. Agazhanov, A. Khairulin, Y. Kozlovskii, D. Samoshkin, Density, thermal expansion, enthalpy, heat capacity, and thermal conductivity of calcium in the temperature range 720–1290 k, Russian Journal of Inorganic Chemistry 68 (2023) 125–132. doi:10. 1134/S0036023622602549.
- [46] V. Y. Chekhovskoi, V. D. Tarasov, Y. V. Gusev, Calorific properties of liquid copper, High Temperature 38 (3) (2000) 394–399.
- [47] F. J. Cherne, M. I. Baskes, P. A. Deymier, Properties of liquid nickel: A critical comparison of eam and meam calculations, Phys. Rev. B 65

(2001) 024209. doi:10.1103/PhysRevB.65.024209.

- [48] D. Sheppard, S. Mazevet, F. J. Cherne, R. C. Albers, K. Kadau, T. C. Germann, J. D. Kress, L. A. Collins, Dynamical and transport properties of liquid gallium at high pressures, Phys. Rev. E 91 (2015) 063101. doi:10.1103/PhysRevE.91.063101.


- [49] G. J. Janz, C. B. Allen, N. P. Bansal, R. M. Murphy, R. Tomkins, Physical properties data compilations relevant to energy storage. ii. molten salts: data on single and multi-component salt systems, Tech. rep., Rensselaer Polytechnic Inst., Troy, NY (USA). Cogswell Lab. (1979).
- [50] A. E. Gheribi, J. A. Torres, P. Chartrand, Recommended values for the thermal conductivity of molten salts between the melting and boiling points, Solar Energy Materials and Solar Cells 126 (2014) 11–25. doi:https://doi.org/10.1016/j.solmat.2014.03.028. URL https://www.sciencedirect.com/science/article/pii/ S0927024814001597
- [51] H. Jua´rez, E. Yousefi, A. Kunwar, Y. Sun, M. Guo, N. Moelans, D. Seveno, Modeling of surface phenomena of liquid al–ni alloys using molecular dynamics, Scientific Reports 13 (2023) 4642. doi:10.1038/ s41598-023-31844-w.
- [52] R. L. Xiao, Q. Wang, J. Y. Qin, J. F. Zhao, Y. Ruan, H. P. Wang, H. Li, B. Wei, A deep learning approach to predict thermophysical properties of metastable liquid Ti-Ni-Cr-Al alloy, Journal of Applied Physics 133 (8)

(2023) 085102. doi:10.1063/5.0138001.

- [53] C. I. Maxwell, Molecular dynamics study of fission gas behaviour and solubility in molten flinak salt, Journal of Nuclear Materials 563 (2022)

153633. doi:https://doi.org/10.1016/j.jnucmat.2022.153633. URL https://www.sciencedirect.com/science/article/pii/ S0022311522001295

- [54] A. Tkatchenko, M. Scheffler, Accurate molecular van der waals interactions from ground-state electron density and freeatom reference data, Phys. Rev. Lett. 102 (2009) 073005. doi:10.1103/PhysRevLett.102.073005. URL https://link.aps.org/doi/10.1103/PhysRevLett.102. 073005
- [55] G. J. Janz, G. L. Gardner, U. Krebs, R. P. T. Tomkins, Molten salts: Volume 4, part 1, fluorides and mixtures electrical conductance, density, viscosity, and surface tension data, Journal of Physical and Chemical Reference Data 3 (1) (1974) 1–115. arXiv:https://pubs.aip. org/aip/jpr/article-pdf/3/1/1/19207799/1_1_online.pdf, doi:


- 10.1063/1.3253134. URL https://doi.org/10.1063/1.3253134
- [56] A. Rudenko, A. A. Kataev, O. Y. Tkacheva, Rotational viscometry for studying the viscosity of cryolite melts, Russian Metallurgy 2023 (2)


(2023) 141–146. doi:10.1134/S0036029523020192.

### Supplementary Information

The Supplementary Information contains additional information and details of calculations supporting the main text. The experimental techniques used for the molten salt properties measurements are described. The justification of dDsC dispersion correction is presented. We compare DFT and MTP energy and forces acting on the atoms. Also, we provide two ionic conductivity GK integral vs time dependencies as the convergence test.

### Dispersion correction selection.

In the AlF3-NaF (1:1 molar fractions) molten salt at 973 K for in-house research we conducted experiments to choose the best performing dispersion correction in VASP. The D3 [25, 26], TS [54] and dDsC [27, 28] corrections were tested. The comparison of molten salt density for various dispersion corrections is presented in Figure 9.

![image 9](Polovinkin et al._2026_Machine-Learned Interatomic Potentials for Predicting Physicochemical Properties of Molten Metal-Sal_images/imageFile9.png)

- Figure 9: Density of AlF3-NaF molten salt calculated with potentials fitted on DFT with various dispersion corrections and experimental value [55].


Experimental methods Density measurements

The density of molten salt systems was measured using the hydrostatic weighing method. The principle of the method is that a sinker of known volume, when immersed in a molten medium, displaces an equal volume of the liquid. Knowing the change in the sinker mass upon immersion in the melt and the sinker’s volume, the density of the displaced liquid can be calculated using Equation (6):

m1 − m2 V

(6)

ρ =

where ρ is melt density, m1 and m2 mass of the sinker weighed in an argon atmosphere and in the melt correspondingly and V is volume of the sinker.

The measurements were conducted in a glovebox setup under a highpurity argon atmosphere with an oxygen content of < 0.1 ppm (Figure 10). The measuring cell consisted of a quartz retort. A spherical platinum sinker was suspended on a platinum wire approximately 0.6 m long and 0.5 mm in diameter, connected to a Radwag XA210.4Y electronic balance of special (Class I) accuracy. The immersion and extraction of the platinum sinker into/from the melt were performed using a lifting mechanism. The sinker was weighed first in the gas atmosphere and then in the molten salt under study.

Before starting the measurements, the measuring cell was calibrated by determining the temperature dependence of the platinum sinker’s volume. The sphere was immersed in a melt of known density, 0.51:0.49 NaCl–KCl (molar fractions). The melt density at each temperature was calculated using Equation (2) from reference [11]:

ρ = 2.1314 − 5.6793 · 10−4 · T(K) (7)

Using the mass difference at each temperature (m1 − m2) and the calculated density ρcalc of the KCl-NaCl mixture, the sinker’s volume was determined using Equation 8:

m1 − m2 ρcalc

(8) where ρcalc is the density of the KCl-NaCl mixture melt calculated using

V =

Equation (6), m1 and m2 mass of the sinker weighed in an argon atmosphere

![image 10](Polovinkin et al._2026_Machine-Learned Interatomic Potentials for Predicting Physicochemical Properties of Molten Metal-Sal_images/imageFile10.png)

- Figure 10: Schematic of the glovebox-equipped measurement setup: 1 – Vertical split-tube resistance furnace of shaft type; 2 – Lifting-lowering mechanism; 3 – Vertical displacement unit (frame); 4 – Platform; 5 – Analytical balance with bottom suspension; 6 – Stepper motor; 7 – Quartz container; 8 – Retort; 9 – Platinum wire; 10 – Pt-Pt/Rh thermocouple (Type S) in alumina sheath; 11 – Glassy carbon crucible; 12 – Molten electrolyte under study; 13 – Platinum sinker; 14 – Electronic control unit; 15 – Glovebox main airlock; 16


– Glovebox small airlock; 17 – Glovebox gas purification unit.

and in the KCl-NaCl melt correspondingly and V is volume of the platinum sinker.

Once the temperature dependence of the platinum sinker’s volume was established, the density of the studied melt was measured. Ionic conductivity measurements

The ionic conductivity was measured using electrochemical impedance spectroscopy with parallel metallic (platinum) electrodes.

The method is based on recording the impedance of an electrochemical system containing the melt of the analyzed salt over an alternating current

frequency range from 100 Hz to 150 kHz with an AC voltage amplitude of 10 mV. Measurements were performed using a Z-1500J impedance analyzer. The resistance of the molten electrolyte under study was determined from the impedance spectrum plot (the so-called Nyquist plot) by the real part of the impedance at the intersection point with the abscissa axis.

The resistance, determined by the frequency-independent active component of the impedance, is taken as the resistance of the molten electrolyte. This value is then used to calculate the ionic conductivity κ (S/m) of the analyzed electrolyte using Equation (9):

K Rel

(9) where K is the cell constant and Rel is the ohmic resistance of the electrolyte.

κ =

The temperature dependence of the cell constant was determined during calibration using parallel platinum electrodes and a reference salt melt with a known temperature-dependent conductivity. For this purpose, an equimolar KCl-NaCl mixture (0.5NaCl–0.5KCl) was used, the conductivity of which has been well-studied in the temperature range from 933 K to 1103 K.

Both the cell calibration and the conductivity measurements of the molten electrolytes were performed using a glovebox-based measurement setup (Figure 11).

Measurements were carried out at temperatures ranging from 953 to 1023 K. The ionic conductivity of the studied electrolytes at a given temperature (within the 953–1023 K range) was calculated using the cell constant determined at the same temperature.

Viscosity measurements

The viscosity of molten salts was measured using a high-temperature rotational rheometer FRS-1600 (Anton Paar) in the temperature range of 573–1873 K. The operating principle involves the rotation of an inner graphite cylinder (diameter 15 mm, height 20 mm) within a stationary outer cylinder (inner diameter 30 mm), with a 2 mm gap filled with the molten sample. Viscosity measurements were conducted in an inert gas atmosphere, supplied through nozzles at the bottom of the setup. During heating, thermal expansion of the measurement system occurs, which is compensated by an automatic gap control system.

The sample mass (m, g) was calculated using the formula: m = vρ (10)

![image 11](Polovinkin et al._2026_Machine-Learned Interatomic Potentials for Predicting Physicochemical Properties of Molten Metal-Sal_images/imageFile11.png)

- Figure 11: Schematic diagram of the glovebox-equipped setup for specific conductivity measurements: 1 - Argon-atmosphere glovebox; 2 - Fluoroplastic cover; 3 - Retort; 4 Stainless steel tube; 5 - Alumina electrode sheath; 6 - Pt-Rh/Pt thermocouple (Type S) in alumina sheath; 7 - Parallel platinum electrodes; 8 - Glassy carbon crucible; 9 - Alumina protection sleeve; 10 - Molten electrolyte under analysis; 11 - Graphite container; 12 Electronic control unit; 13 - Glovebox main airlock; 14 - Glovebox small airlock; 15 Glovebox gas purification unit; 16 - Vertical split-tube resistance furnace of shaft type.


where v is the volume, 35±2 cm3, and ρ is the density of the molten sample at the measurement temperature.

The sample was loaded into the crucible in air. Heating was performed in a Carbolite STF16/180 furnace under an inert gas atmosphere. After melting (Tliquidus = 914 K) and homogenization of the melt by rotor rotation for 40-50 minutes, the shear rate was measured. The rotational method is based on Newton’s law for the flow of a Newtonian fluid:

τ = ηγ˙ (11)

where τ is the shear stress, η is the dynamic viscosity, and γ˙ is the shear rate.

To ensure accurate viscosity measurements, laminar flow was established in the sample. The dependence of viscosity on shear rate was determined from flow and viscosity curves, and a shear rate of 11 s−1 was selected, at which the melt behaves as a Newtonian fluid. Viscosity measurements were then conducted at a cooling rate of 2 K/min. The viscosity measurement methodology is described in detail in [56].

### Correlation plots for energies and forces.

In figures 12 and 13 the correlation plots for energies and forces are presented for Ca-Cu and CaCl2-KCl systems, respectively. These plots were obtained for validation sets containing independent configurations sampled from the equilibrium of systems. We does not observe any outliers on these plots.

![image 12](Polovinkin et al._2026_Machine-Learned Interatomic Potentials for Predicting Physicochemical Properties of Molten Metal-Sal_images/imageFile12.png)

- Figure 12: Correlation plots of energies per atoms (a) and forces (b) in Ca-Cu validation set. The size of validation set was 240 configurations with calcium molar fraction from 0 to 1.


![image 13](Polovinkin et al._2026_Machine-Learned Interatomic Potentials for Predicting Physicochemical Properties of Molten Metal-Sal_images/imageFile13.png)

##### Figure 13: Correlation plots of energies per atoms (a) and forces (b) in CaCl2-KCl vali-dation set. The size of validation set was 200 configurations.

### Green-Kubo integrals for ionic electric conductivity.

We provide time dependencies of GK integration for ionic electric conductivity. Averaging over 10 trajectories (red) is employed for mean value calculation (blue). The standard deviation is reported the uncertainty. We observe that at both temperatures (900 and 1100 K) the integrals are converged. Possible, the smaller time (e.g., 10 ps) could be enough for calculations.

![image 14](Polovinkin et al._2026_Machine-Learned Interatomic Potentials for Predicting Physicochemical Properties of Molten Metal-Sal_images/imageFile14.png)

- Figure 14: Dependence of ionic conductivity on the integration time in GK method. Temperature 900 K.


![image 15](Polovinkin et al._2026_Machine-Learned Interatomic Potentials for Predicting Physicochemical Properties of Molten Metal-Sal_images/imageFile15.png)

##### Figure 15: Dependence of ionic conductivity on the integration time in GK method.Temperature 1100 K.

