# arXiv:2509.14185v1[math.AP]17 Sep 2025

## Discovery of Unstable Singularities

#### Yongji Wang1, 2, Mehdi Bennani3, James Martens3, Sebastien Racani´ ere` 3, Sam Blackwell3, Alex Matthews3, Stanislav Nikolov3, Gonzalo Cao-Labora1, 4, Daniel S. Park5, Martin Arjovsky3, †, Daniel Worrall3, †, Chongli Qin3, †, Ferran Alet3, †, Borislav Kozlovskii3, †, Nenad Tomasevˇ 3, †, Alex Davies3, Pushmeet Kohli3, Tristan Buckmaster1,*, Bogdan Georgiev3,*, Javier Gomez-Serrano´ 6,*, Ray Jiang3,* and Ching-Yao Lai2,*

1New York University, Department of Mathematics, New York, NY 10012, USA 2Stanford University, Department of Geophysics, Stanford, CA 94305, USA 3Google DeepMind, London, N1C 4DJ, UK 4Ecole Polytechnique F´ ed´ erale de Lausanne, Institute of Mathematics, Lausanne, VA 1015, Switzerland´ 5Google DeepMind, New York, NY 10011, USA 6Brown University, Department of Mathematics, Providence, RI 02912, USA †These authors have comparable contributions

- *Corresponding author: buckmaster@cims.nyu.edu
- *Corresponding author: bogeorgiev@google.com
- *Corresponding author: javier gomez serrano@brown.edu

- *Corresponding author: rayjiang@google.com
- *Corresponding author: cyaolai@stanford.edu
- *All corresponding authors contributed equally and are listed in alphabetical order


#### ABSTRACT

Whether singularities can form in fluids remains a foundational unanswered question in mathematics. This phenomenon occurs when solutions to governing equations, such as the 3D Euler equations, develop infinite gradients from smooth initial conditions. Historically, numerical approaches have primarily identified stable singularities. However, these are not expected to exist for key open problems, such as the boundary-free Euler and Navier-Stokes cases, where unstable singularities are hypothesized to play a crucial role. Here, we present the first systematic discovery of new families of unstable singularities. A stable singularity is a robust outcome, forming even if the initial state is slightly perturbed. In contrast, unstable singularities are exceptionally elusive; they require initial conditions tuned with infinite precision, being in a state of instability whereby infinitesimal perturbations immediately divert the solution from its blow-up trajectory. In particular, we present multiple new, unstable self-similar solutions for the incompressible porous media equation and the 3D Euler equation with boundary, revealing a simple empirical asymptotic formula relating the blow-up rate to the order of instability. Our approach combines curated machine learning architectures and training schemes with a high-precision Gauss-Newton optimizer, achieving accuracies that significantly surpass previous work across all discovered solutions. Crucially, for specific solutions (the Córdoba-Córdoba-Fontelos (CCF) stable and 1st unstable solutions), we reach near double-float machine precision, attaining a level of accuracy constrained only by the inherent round-off errors of the GPU hardware. This level of precision meets the stringent requirements for rigorous mathematical validation via computer-assisted proofs. This work provides a new playbook for exploring the complex landscape of nonlinear partial differential equations (PDEs) and tackling long-standing challenges in mathematical physics.

Understanding whether the partial differential equations governing fluid motion can develop singularities from smooth initial conditions – where mathematical solutions exhibit infinite gradients or velocities in finite time – represents one of the most enduring challenges in mathematics. This fundamental question spans a broad class of nonlinear fluid equations, including the incompressible 3D Euler equations1 (first formulated in 1752), the Boussinesq equations2 which model atmospheric flows, and the incompressible porous media (IPM) equation3, describing fluid motion through porous materials like soil or rock. Crucial insights into these dynamics are also gained through the study of simplified analogues, such as the 1D Córdoba-Córdoba-Fontelos (CCF) model4.

Among these systems, the 3D Navier-Stokes equations, the viscous analogue of the 3D Euler equations, represent perhaps the most famous case. The question of finite-time blow-up for Navier-Stokes is recognized as one of the seven Millennium Prize Problems5 and the Smale Problems6 (the 15th), with profound implications for mathematics and physics. We refer to the surveys7,8 for developments on this problem. If singularities can develop from smooth initial conditions, the equations predict physically impossible outcomes, such as infinite velocity gradients, in finite time. This would signal a fundamental breakdown in the predictive power of the equations.

A crucial aspect of singularity formation is stability. A singularity is considered stable if it reliably emerges from a range of initial conditions. Conversely, an unstable singularity requires infinitely precise initial conditions; any slight perturbation causes the system to deviate from the blow-up trajectory. It is hypothesized that singularities in foundational, boundary-free problems like the 3D Euler and Navier-Stokes equations must be unstable. While the presence of boundaries can stabilize solutions, developing the techniques to discover and resolve unstable singularities, even in systems with boundaries, is a critical intermediate step toward tackling the boundary-free challenge. Furthermore, it is expected that highly unstable solutions are better candidates for persisting when transitioning from idealized equations to more realistic, viscous ones, making their discovery essential for resolving these fundamental questions.

Efforts to resolve the problem of singularity formation have spanned both numerical simulations and classical analysis. In terms of numerical candidates to Euler blow-up, several works have considered the possibility of colliding dipoles9–11. By performing space-time simulations up to times very close to the singularity, Luo and Hou12 presented compelling numerical evidence for finite-time blow-up for the axisymmetric 3D Euler equations if one introduces a cylindrical boundary.

An emerging approach combines high-precision numerics with rigorous mathematical analysis in the form of a computer-assisted proof (CAP) via the use of interval arithmetic13. The self-similar profile corresponding to the Luo-Hou scenario was first found numerically using physics-informed neural networks (PINNs)14,15 by Wang et al.16 and proven rigorously using a CAP by Chen and Hou17,18 (c.f. Wang et al.19). A key ingredient in this hybrid approach20–22 is the use of self-similar coordinates. These coordinates rescale space and time around the point of blow-up23–25. This removes the difficulty of tracking rapidly diverging physical quantities by transforming the problem from a time-evolving simulation into finding a stationary, smooth self-similar profile.

This work addresses the following critical, previously unsolved challenge. Previous frameworks utilizing numerical tools such as B-splines on non-uniform meshes12, finite elements26 or spectral methods27 excel at resolving stable blow-up solutions, yet they may face significant limitations in capturing unstable ones. Performing time-stepping simulations (even self-similar) to identify unstable solutions requires extreme precision to overcome the exponential instabilities arising from being on the unstable manifold. This limitation is more notable when those solutions are quantized (as opposed to a continuum of solutions in terms of a continuous parameter) and continuation methods cannot be applied. Indeed, in the case of colliding dipoles, instabilities present preclude the use of such numerical techniques as a basis for a mathematical construction of blow-up. In order to render the problem accessible by such numerics, Hou28 added viscous terms to stabilize the blow-up; however, due to the singular nature of such terms, it is not clear how the solutions found relate to the original equations considered. The critical challenge, therefore, has been developing a computational framework capable of discovering and accurately resolving these elusive, unstable solutions to the precision required for mathematical proof.

In this work, we introduce such a framework (see Figure 1), combining curated neural network architectures and training schemes with a high-precision Gauss-Newton optimizer. This approach enables the first systematic discovery of new families of unstable singularities for the IPM and Boussinesq equations, revealing a simple empirical asymptotic formula relating the blow-up rate to the order of instability (see Figure 2). We achieve a level of accuracy that significantly surpasses previous work across all discovered solutions; crucially, for specific CCF solutions, we reach near double-float machine precision, a level constrained only by the inherent round-off errors of the GPU hardware.

###### High Precision Self-Similar Solution Discovery

###### Solution Analysis

##### a

|Stability analysis of the linearized PDE around smooth singularity solutions<br><br>Highly accurate stable and unstable smooth singularity solutions with up to double-ﬂoat machine precision<br><br>Characterization of stable and unstable solutions<br><br>unstable direction in solution space: perturbations diverge from singularity solution<br><br>stable direction in<br><br>solution space: singularity solution remains stable to perturbations<br><br>![image 1](Wang et al._2025_Discovery of Unstable Singularities_images/imageFile1.png)<br><br>![image 2](Wang et al._2025_Discovery of Unstable Singularities_images/imageFile2.png)<br><br>b|
|---|


Mathematical Modeling

- (i)

- (ii)


Self-similar Solution Ansatz

insights from candidate solution

![image 3](Wang et al._2025_Discovery of Unstable Singularities_images/imageFile3.png)

![image 4](Wang et al._2025_Discovery of Unstable Singularities_images/imageFile4.png)

![image 5](Wang et al._2025_Discovery of Unstable Singularities_images/imageFile5.png)

![image 6](Wang et al._2025_Discovery of Unstable Singularities_images/imageFile6.png)

Self-similar solution candidate

(iii)

Candidate U with scaling rate λ

PINN outputs

![image 7](Wang et al._2025_Discovery of Unstable Singularities_images/imageFile7.png)

![image 8](Wang et al._2025_Discovery of Unstable Singularities_images/imageFile8.png)

mathematical inductive bias

Machine Learning

Physics-Informed Neural Network (PINN)

Multi-stage training

![image 9](Wang et al._2025_Discovery of Unstable Singularities_images/imageFile9.png)

![image 10](Wang et al._2025_Discovery of Unstable Singularities_images/imageFile10.png)

![image 11](Wang et al._2025_Discovery of Unstable Singularities_images/imageFile11.png)

Equation residual

10-5

![image 12](Wang et al._2025_Discovery of Unstable Singularities_images/imageFile12.png)

input transform

Multi-layer Perceptron

10-15

ﬁeld ansatz

10-25

0 50k 100k

ﬁelds

![image 13](Wang et al._2025_Discovery of Unstable Singularities_images/imageFile13.png)

![image 14](Wang et al._2025_Discovery of Unstable Singularities_images/imageFile14.png)

PDE

![image 15](Wang et al._2025_Discovery of Unstable Singularities_images/imageFile15.png)

boundary cond.

Gauss-Newton optimization

Equation residuals

![image 16](Wang et al._2025_Discovery of Unstable Singularities_images/imageFile16.png)

![image 17](Wang et al._2025_Discovery of Unstable Singularities_images/imageFile17.png)

![image 18](Wang et al._2025_Discovery of Unstable Singularities_images/imageFile18.png)

residual derivatives

machine learning modeling insights

|![image 19](Wang et al._2025_Discovery of Unstable Singularities_images/imageFile19.png)|
|---|


loss

- Figure 1. Research flowchart. Our research methodology consists of two main stages. a) Solution discovery. We start with a candidate solution that allows us to search for self-similar spatial profiles of blow-up solutions characterized by a self-similar scaling rate λ, illustrated in (i) with Burgers’ Equation. We then refine our machine learning pipeline (ii) and solution accuracy using an iterative approach. Empirical results from candidate solutions (iii) and their accuracy guide the mathematical modeling and neural network architecture. Mathematical modeling in turn guides the inductive biases built into the network architecture, such as input coordinate transforms and the shaping of the output fields. We use a Physics-informed Neural Network (PINN) with a Gauss-Newton optimiser and a multi-stage refinement training scheme to generate a highly accurate candidate solution while finding the right scaling rate λ. b) Solution analysis. We analyze the stability of a high-precision candidate solution by linearising the PDE around it. We discover unstable modes, along which any slight perturbation causes the system to deviate from the blow-up trajectory. Thus, we characterize the degree of stability and confirm the discovery of highly accurate stable and unstable singularities.


#### Discovery of Unstable Singularities

In this study, we discover unstable singularities in three canonical fluid systems: the CCF equations4, the 2D IPM equations, and the 2D Boussinesq equations. In the presence of a boundary, the 2D Boussinesq equations are mathematically analogous (up to exponentially small terms) to the incompressible 3D Euler equations under the assumption of axial symmetry.

To discover singularities, each equation is reformulated in self-similar coordinates – a time-dependent rescaling of space parameterized by a scaling parameter λ that governs the blow-up spatiotemporal structure (see Methods Self-similar Coordinates). By construction, finding a self-similar singularity entails the task of identifying λ values admitting smooth solutions in those coordinates. We say such values of λ are admissible. The self-similar parameter λ dictates the nature of the singularity (see Methods Identifying admissible λ). A smaller value of λ corresponds to a more unstable solution and, consequently, a more severe singularity with a faster blow-up rate, which allows it to overcome greater dissipative effects (e.g. going from Euler to Navier-Stokes).

We quantify the accuracy of the discovered numerical solutions using the maximum residual, which is defined as the maximum absolute value of the equation residual over the entire spatial domains when a candidate solution is

![image 20](Wang et al._2025_Discovery of Unstable Singularities_images/imageFile20.png)

a IPM: 3rd unstable solution b Boussinesq: 3rd unstable solution e

![image 21](Wang et al._2025_Discovery of Unstable Singularities_images/imageFile21.png)

![image 22](Wang et al._2025_Discovery of Unstable Singularities_images/imageFile22.png)

###### c d f

|Lambda|CCF|IPM with boundary|Boussinesq|
|---|---|---|---|
|Stable|1.1807776628998|1.0285722760222|1.9205599746927|
|1st unstable|0.6057337012032|0.4721297362414|1.3990961221852|
|2nd unstable|0.4713248638620|0.3149620267088|1.2523481636489|
|3rd unstable| |0.2415604743989|1.1842500861997|
|4th unstable| | |1.1448833556188|


![image 23](Wang et al._2025_Discovery of Unstable Singularities_images/imageFile23.png)

![image 24](Wang et al._2025_Discovery of Unstable Singularities_images/imageFile24.png)

- Figure 2. Self-similar singularities to IPM and Boussinesq. a, b, Spatial profile of the vorticity Ω for the third unstable solutions of the IPM (in a) and Boussinesq equations (in b) near the origin. c, d, The cross section of the vorticity profiles


along the y1 axis, namely Ω(y1,0) for the stable to third unstable solutions of the IPM (in c) and Boussinesq equations (in d). e, Inverse scaling rate versus the instability order, the plot reveals a linear trend for both systems (shaded area denotes one standard deviation). f, The scaling parameters of the unstable solutions discovered in the paper (green and yellow) and the previously discovered solutions (blue). The significant digits of the scaling parameters are marked in bold-face. The 4th unstable solution of the Boussinesq equation is un-validated.

substituted into the governing equations. To establish a meaningful and comparable metric across different solutions, it is essential to fix the scale (normalization). The maximum (absolute) residual, calculated across all equations and a dense spatial validation grid, therefore provides a standardized measure of how accurately the solution satisfies the system. Beyond evaluating the residual, we employ other validation methods. Crucially, we analyze the spectrum of the linearisation of the governing equations around the candidate solution, checking for expected properties related to the stability of the solution, such as the number of unstable modes. Once a numerical solution and its corresponding scaling factor λ is determined, we validate the significant digits of λ by finding the minimum amount of perturbation that can be applied to λ for which the solution quality is unchanged. We discuss these validation methods in detail in Methods and the Supplementary Information.1

The CCF equations can be viewed as a simplified model for the 3D Euler equations and the Navier-Stokes equation. An important open question29 [30, Open Problem 1] regarding the CCF equations is whether singularities still occur in the presence of fractional dissipation (−∆)α/2 for 12 ≤ α ≤ 1. This problem involves the fundamental balance between nonlinear amplification (which causes blow-up) and dissipative mechanisms (which regularize the solution). The first unstable blow-up profile for CCF was discovered by Eggers and Fontelos31, and recently confirmed using PINN-based methods by Wang et al.16 with λ1 ≈ 0.6057, suggesting that singularities exist for any α ≤ 1/(1+λ1) ≈ 0.623, ultimately culminating in a mathematically rigorous proof (manuscript in preparation). The challenge of finding higher unstable solutions for the CCF equations lies in the extremely sharp gradients of their profiles, often believed to trap the optimization in local minima. In this work, we improve the stable and first unstable singularities of Wang et al.16 to achieve PDE residuals of order O(10−13) for both solutions. We also

1The Supplementary Information to the paper will be uploaded in a forthcoming version of the manuscript.

discover the second unstable profile with λ2 = 0.4703 with residuals of order O(10−7). This discovery increases the critical α for singularity formation to α ≤ 1/(1+λ2) ≈ 0.68, advancing our understanding of dissipative thresholds in fluid systems and shedding light on an old and fundamental open question.

The IPM equations describe density evolution driven by incompressible flows governed by Darcy’s law under gravity3. While prior literature provides no evidence of self-similar solutions in IPM32,33, we identify the stable and three unstable singularities with residuals whose orders of magnitude range from O(10−11) to O(10−8).

For the Boussinesq equations, we are able to confirm the stable solution and discover three distinct unstable singularities with residuals whose orders of magnitude range from O(10−8) to O(10−7). Furthermore, we have identified a candidate for the fourth unstable solution. This solution, however, is not resolved to the same level of accuracy as the others; in particular, we do not yet have a reliable evaluation of the accuracy of its corresponding λ value. We refer to the Supplementary Information for more details regarding this candidate. This marks the first discovery of any smooth unstable self-similar solution to any unforced incompressible fluid equation, leading to a finite time blow-up. We refer to Methods and Supplementary Information for the presentation and analysis of all solutions.

For every unstable solution discovered for the CCF, IPM and Boussinesq equations, we conduct a stability analysis by linearizing the governing equations around the solution. For the n-th unstable solution discovered, we find n unstable modes that respect the same symmetry assumptions as the solution. Since such unstable modes specify directions in which the solution can be pushed to become more stable, this suggests that the family of solutions discovered so far are complete within the range of admissible λ values considered.

One proposed approach to addressing the Clay Millennium Prize Problem involves finding a sequence of self-similar profiles, corresponding to a sequence of self-similar scaling parameters λn, for the 3D Euler equations, each with an increasing number of unstable directions. It is expected that higher-order instability makes it more feasible to treat viscosity as a perturbative error, as the timescales in which the viscous effects come into play are much slower than the ones leading to the finite time singularity. This phenomenon has been observed in the compressible Navier-Stokes equations and the defocusing Nonlinear Schrödinger (NLS) equation34,35.

Based on the discovery of families of unstable singularities we have made, we are able to extrapolate an empirical rule for admissible λ values of the Boussinesq/Euler equations and the IPM equations. For the Boussinesq/Euler equations, we find that λn ∼ 1/(1.4187n + 1.0863) + 1, where λn indicates the λ value for the n-th unstable singularity. For IPM with boundary, the empirical relation of λ for higher-order unstable modes is λn ∼ 1/(1.1459n+

- 0.9723). Both asymptotic expansions fit well for larger values of n. For the CCF equations, a clear asymptotic relationship has not yet been identified from the solutions discovered so far, making a reliable extrapolation premature. These formulae provide candidate values for admissible λ for higher-order unstable modes, which can guide future studies of singularity hierarchies in these equations. Moreover, they can make numerical discovery of new solutions easier by providing high-quality initialization values for λ, making thus the distance between the initial value at training and the final value smaller, yielding faster and more reliable convergence.


#### Targeted PDE solution discovery with PINNs

In this study, all unstable singularities are discovered by modeling the solutions with physics-informed neural networks (PINNs), which has emerged as a new tool for solving differential equations14,15. Wang et al.16 have demonstrated the potential of using PINNs for discovering stable singularities in fluids. PINNs have also been applied to explore unstable numerical solutions, for instance, in 2D cavity flow problems36,37. So far, the accuracies commonly achieved by PINNs (e.g., an error of O(10−3) for Boussinesq in Wang et al.16) have been insufficient for the numerical solutions to be used for a rigorous proof.

The application of a PINN to a problem is characterized by three core components: the neural network architecture, the loss function, and the optimization algorithm. Substantial research has been focused on improving the performance of PINNs by advancing these components. This includes developments in network design (such as activation function selection38,39 and configuration40,41), sophisticated strategies for weighting the loss function42–45, the adoption of more effective optimization methods46,47 and the employment of hierarchical training schemes48,49.

###### a b

![image 25](Wang et al._2025_Discovery of Unstable Singularities_images/imageFile25.png)

|Equation|Solution|log10 Maximum Residual|
|---|---|---|
|CCF|Stable|-13.714|
| |1st unstable|-13.589|
| |2nd unstable|-6.664|
|IPM with boundary|Stable|-11.183|
| |1st unstable|-10.510|
| |2nd unstable|-8.101|
| |3rd unstable|-7.526|
|Boussinesq|Stable|-8.178|
| |1st unstable|-8.038|
| |2nd unstable|-7.772|
| |3rd unstable|-7.558|
| |4th unstable|-7.020|


- Figure 3. Solution accuracy. a, Spatial profiles of the equation residual for the 1st unstable solution to the IPM equation after multistage training. b, List of the log-10 maximum equation residuals for the best solutions discovered for the CCF, IPM and Boussinesq equations.


Given that there is recent concern about overoptimism in using PINNs as general-purpose PDE solvers50, we stress that PINNs are not used for this purpose in this work. Rather, the goal is to discover solutions to differential equations that have not been found before. Here, PINNs are utilized to parameterize the particular solution of partial differential equations we wish to discover, and the pipelines for training the models are designed and constructed with the intention of making the network satisfy all the mathematical assumptions and constraints imposed by the problem at hand.

Since our goal is discovery, we do not claim improvement in efficiency or speed against any benchmarks. The validation metrics we present only concern the quality of the solutions that have been discovered. In figure 3b, we present the best maximum residuals we have been able to achieve for all solutions. The maximum residuals generally range from O(10−8) to O(10−7), achieving multiple orders of magnitude improvement in this metric compared to the literature16,19. For the CCF equations, we are able to approach precision limited only by the double-floating point round-off errors (O(10−13)), a level of accuracy currently required for enabling subsequent computer-assisted proofs.

###### Incorporating mathematical structure into a neural network

We represent solutions as smooth functions parameterized by neural networks. This allows us to directly embed known mathematical properties of the target solution into the network architecture. This embedding acts as a strong inductive bias, guiding the optimization toward mathematically relevant solutions and away from trivial or degenerate ones.

We enforce constraints derived from the governing equations through architectural design. Symmetries and periodicity are imposed via input transformations. Infinite domains, inherent in self-similar problems, are handled using coordinate transformations that compactify the space27 (see Methods Solution Modeling). Furthermore, we utilize tailored "solution envelopes" – multiplicative factors applied to the network output – to enforce behaviors such as asymptotic decay at infinity and local series expansions near the origin. Crucially, smoothness requirements

![image 26](Wang et al._2025_Discovery of Unstable Singularities_images/imageFile26.png)

- Figure 4. High-precision training. a, The log-10 maxium residual value of the solution evaluated on the evaluation grid for the CCF first unstable solution when training with different optimizers. The Gaussian-Newton optimizer shows better performance and significantly faster convergence than the classical Adam + L-BFGS optimizers. Multi-stage training is able to further improve the results by five orders of magnitude. b, The two residuals of the CCF first unstable solution obtained by multi-stage training plotted against the self-similar spatial coordinate y.


at the origin can also be used to derive an analytical relationship for the self-similar parameter λ (see51 for an analogous application). This provides a robust alternative to learning λ as a standard trainable parameter16.

While formal analysis provides essential guidance, it often relies on assumptions (e.g. selecting one branch from several formal possibilities) that are not guaranteed a priori. We overcome this through a feedback loop between numerical experiments and mathematical analysis (see Figure 1). Initial experiments reveal hidden structures which are then incorporated back into the network architecture a posteriori. For example, experiments for the IPM and Boussinesq equations suggest that the solutions vanish faster near the origin than required by minimal symmetry assumptions. Incorporating this insight allows us to explicitly factor this vanishing behavior out from the solution representation. We then are able to reformulate the governing equations for the remaining component, which significantly improves optimization stability by structuring the terms the network must satisfy (see Methods and Supplementary Information).

By systematically embedding these mathematical features, both those known a priori and those discovered iteratively, we enhance the optimization landscape. This integration of mathematical structure accelerates convergence and ultimately enables the discovery of previously inaccessible high-order unstable solutions.

###### High-precision training

Improving the training procedure is a crucial element to achieving the extreme precision required for discovering unstable singularities. We find the two key components to attaining high-precision training to be the utilization of a full-matrix Gauss-Newton optimizer, and the employment of multi-stage training.

As presented in figure 4, we find standard gradient optimization methods, e.g., Adam or L-BFGS, to be insufficient for producing high quality solutions to the self-similar equations, c.f. McGreivy and Hakim50. Recent works have explored the use of stronger second-order optimizers, which involve approximations to the curvature matrix to remain computationally feasible for large networks, for related tasks46,47,52.

In contrast, we adopt a full-matrix Gauss-Newton (GN) approach53, to optimize our neural networks54. Since no structural approximations to the GN matrix are made, we are able to compute an essentially unbiased stochastic estimate of it. While generally computationally infeasible for most applications of neural networks, this approach is viable for us due to the relatively small size of our networks, whose number of parameters range from thousands to at most tens of thousands.

We efficiently estimate the GN matrix using an inexpensive, unbiased rank-1 estimator, which we average across iterations using an exponential moving average to reduce variance. To ensure robust convergence without manual tuning, we integrate this approach with automated methods55 for determining nearly optimal per-iteration learning

rates and momentum coefficients. This (nearly) fully automated scheme, implemented using the open-source library kfac-jax56, allows us to rapidly iterate on modeling choices without expensive hyperparameter sweeps. In

- Figure 4 we demonstrate the efficacy of this optimizer, which is able to discover solutions with maximum residuals of O(10−8) within 50k iterations (≈ 3 A100 GPU hours), compared to standard optimization techniques.


Using a better optimizer alone does not get us to the precision of solutions we would like to ultimately achieve. To that end, we employ multi-stage training49, in which a second neural network is optimized to efficiently correct the remaining high frequency error of the first network that has already been trained. The output of the first and second networks are combined to produce the solution. We utilize multi-stage training for the stable and first unstable solutions of the CCF and IPM equations. For the solutions of the CCF equations, we are able to improve the maximum residuals by five orders of magnitude down to O(10−13), a level sufficient for rigorous mathematical validation based on a CAP. See fig. 4 for the validation curve for multi-stage training applied to the first unstable solution of CCF, as well as the spatial distribution of the residuals of the discovered solution. For the IPM stable and first unstable solutions, we are able to achieve maximum residuals of O(10−11) and O(10−10) respectively through multi-stage training (Fig. 3a).

#### Implications for Future Studies

Since their introduction14, PINNs have been widely studied in science and engineering15. Here, we demonstrate their advantage as a specialized discovery tool for finding new and highly accurate numerical solutions that advance mathematical understanding. Rather than proposing PINNs as general-purpose PDE solvers, we leverage their designability to seek specific, elusive solutions – such as the unstable singularities detailed in this paper – that pose considerable challenges for discovery. Our approach is able to reduce PDE residuals by multiple orders of magnitude compared to those reported in the literature, achieving double-float machine precision for solutions of the CCF equation. This level of accuracy proves to be sufficient for utilizing the numerical solution for computer-assisted proofs for this specific problem2, although the required precision for such proofs is generally problem-dependent. We hope our results would encourage new numerical designs and discovery methods to develop for similar applications across the computational community. Our results highlight the importance of combining domain-specific mathematical insights with modern computational tools to tackle problems that have resisted purely analytical or purely numerical methods. This interdisciplinary approach opens new possibilities for exploring complex solution landscapes in nonlinear PDEs. However, significant challenges remain. A key challenge is to discover self-similar solutions to the incompressible 3D Euler equations (or similar equations such as IPM) in the absence of boundary. To address this problem, we will need to further understand the qualitative properties of such solutions that can guide the design of PINN architecture and training pipelines.

#### References

- 1. Euler, L. Principes généraux du mouvement des fluides. Mémoires de l’académie des sciences de Berlin 274– 315 (1757).

- 2. Majda, A. J. & Bertozzi, A. L. Vorticity and incompressible flow, vol. 27 of Cambridge Texts in Applied Mathematics (Cambridge University Press, Cambridge, 2002).

- 3. Bear, J. Dynamics of fluids in porous media (Courier Dover Publications, 1972).

- 4. Córdoba, A., Córdoba, D. & Fontelos, M. A. Formation of singularities for a transport equation with nonlocal velocity. Ann. Math. (2) 162, 1377–1389, DOI: 10.4007/annals.2005.162.1377 (2005).

- 5. Fefferman, C. L. Existence and smoothness of the Navier-Stokes equation. The millennium prize problems 57, 67 (2000).

- 6. Smale, S. Mathematical problems for the next century. Math. Intell. 20, 7–15, DOI: 10.1007/BF03025291


(1998).

2Manuscript in preparation.

- 7. Hou, T. Y. Blow-up or no blow-up? A unified computational and analytic approach to 3D incompressible Euler and Navier-Stokes equations. Acta Numer. 18, 277–346, DOI: 10.1017/S0962492906420018 (2009).

- 8. Gibbon, J. D. The three-dimensional Euler equations: where do we stand? Phys. D 237, 1894–1904, DOI: 10.1016/j.physd.2007.10.014 (2008).

- 9. Pumir, A. & Siggia, E. Collapsing solutions to the 3-d euler equations. Phys. Fluids A: Fluid Dyn. 2, 220–241, DOI: 10.1063/1.857824 (1990). https://pubs.aip.org/aip/pof/article-pdf/2/2/220/12260670/220_1_online.pdf.

- 10. Kerr, R. M. Evidence for a singularity of the three-dimensional, incompressible euler equations. Phys. Fluids A: Fluid Dyn. 5, 1725–1746, DOI: 10.1063/1.858849 (1993). https://pubs.aip.org/aip/pof/ article-pdf/5/7/1725/12783847/1725_1_online.pdf.

- 11. Hou, T. Y. Potential singularity of the 3d euler equations in the interior domain. Foundations Comput. Math. 23, 2203–2249, DOI: 10.1007/s10208-022-09585-5 (2022).

- 12. Luo, G. & Hou, T. Y. Potentially singular solutions of the 3d axisymmetric euler equations. Proc. Natl. Acad. Sci. 111, 12968–12973, DOI: 10.1073/pnas.1405238111 (2014). http://www.pnas.org/content/111/36/12968.full.pdf.

- 13. Gómez-Serrano, J. Computer-assisted proofs in PDE: a survey. SeMA J. 76, 459–484, DOI: 10.1007/ s40324-019-00186-x (2019).

- 14. Raissi, M., Perdikaris, P. & Karniadakis, G. Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations. J. Comput. Phys. 378, 686–707, DOI: 10.1016/j.jcp.2018.10.045 (2019).

- 15. Karniadakis, G. E. et al. Physics-informed machine learning. Nat. Rev. Phys. 3, 422–440, DOI: 10.1038/ s42254-021-00314-5 (2021).

- 16. Wang, Y., Lai, C.-Y., Gómez-Serrano, J. & Buckmaster, T. Asymptotic Self-Similar Blow-Up Profile for Three-Dimensional Axisymmetric Euler Equations Using Neural Networks. Phys. Rev. Lett. 130, Paper No. 244002, DOI: 10.1103/physrevlett.130.244002 (2023).

- 17. Chen, J. & Hou, T. Y. Stable nearly self-similar blowup of the 2d boussinesq and 3d euler equations with smooth

- data i: Analysis. arXiv preprint arXiv:2210.07191 (2022).

18. Chen, J. & Hou, T. Y. Stable nearly self-similar blowup of the 2d boussinesq and 3d euler equations with smooth

- data ii: rigorous numerics. arXiv preprint arXiv:2305.05660 (2023).


- 19. Wang, Y., Liu, Z., Li, Z., Anandkumar, A. & Hou, T. Y. High precision PINNs in unbounded domains: application to singularity formulation in PDEs. arXiv e-prints arXiv:2506.19243, DOI: 10.48550/arXiv.2506. 19243 (2025). 2506.19243.

- 20. Costin, O. & Tanveer, S. Analytical approximation of the Blasius similarity solution with rigorous error bounds. SIAM J. Math. Anal. 46, 3782–3813, DOI: 10.1137/13091470X (2014).

- 21. Elgindi, T. & Pasqualotto, F. Invertibility of a linearized Boussinesq flow: a symbolic approach. Arxiv preprint arXiv:2310.19781 (2022).

- 22. Castro, A., Córdoba, D. & Gómez-Serrano, J. Global smooth solutions for the inviscid SQG equation. Memoirs AMS 266, 89 pages (2020).

- 23. Buckmaster, T., Cao-Labora, G. & Gómez-Serrano, J. Smooth imploding solutions for 3D compressible fluids. Forum Math. Pi 13, Paper No. e6, DOI: 10.1017/fmp.2024.12 (2025).

- 24. Eggers, J. & Fontelos, M. A. The role of self-similarity in singularities of partial differential equations. Nonlinearity 22, R1–R44, DOI: 10.1088/0951-7715/22/1/001 (2009).

- 25. Elgindi, T. Finite-time singularity formation for C1,α solutions to the incompressible Euler equations on R3. Ann. Math. (2) 194, 647–727, DOI: 10.4007/annals.2021.194.3.2 (2021).


- 26. Guillod, J. & Šverák, V. Numerical investigations of non-uniqueness for the Navier-Stokes initial value problem in borderline spaces. J. Math. Fluid Mech. 25, Paper No. 46, 25, DOI: 10.1007/s00021-023-00789-5 (2023).

- 27. Lushnikov, P. M., Silantyev, D. A. & Siegel, M. Collapse Versus Blow-Up and Global Existence in the Generalized Constantin–Lax–Majda Equation. J. Nonlinear Sci. 31, DOI: 10.1007/s00332-021-09737-x (2021).

- 28. Hou, T. Y. Potential singularity of the 3D Euler equations in the interior domain. Found. Comput. Math. 23, 2203–2249, DOI: 10.1007/s10208-022-09585-5 (2023).

- 29. Silvestre, L. & Vicol, V. On a transport equation with nonlocal drift. Trans. Amer. Math. Soc. 368, 6159–6188, DOI: 10.1090/tran6651 (2016).

- 30. Kiselev, A. Regularity and blow up for active scalars. Math. Model. Nat. Phenom. 5, 225–255, DOI: 10.1051/ mmnp/20105410 (2010).

- 31. Eggers, J. & Fontelos, M. A. Selection of singular solutions in non-local transport equations. Nonlinearity 33, 325, DOI: 10.1088/1361-6544/ab4e0b (2019).

- 32. Córdoba, D., Gancedo, F. & Orive, R. Analytical behavior of two-dimensional incompressible flow in porous media. J. Math. Phys. 48, 065206, 19, DOI: 10.1063/1.2404593 (2007).

- 33. Córdoba, D. & Martínez-Zoroa, L. Finite time singularities of smooth solutions for the 2D incompressible porous media (IPM) equation with a smooth source. arXiv preprint arXiv:2410.22920 (2024).

- 34. Merle, F., Raphaël, P., Rodnianski, I. & Szeftel, J. On the implosion of a compressible fluid II: singularity formation. Ann. Math. (2) 196, 779–889, DOI: 10.4007/annals.2022.196.2.4 (2022).

- 35. Merle, F., Raphaël, P., Rodnianski, I. & Szeftel, J. On blow up for the energy super critical defocusing nonlinear Schrödinger equations. Invent. Math. 227, 247–413, DOI: 10.1007/s00222-021-01067-9 (2022).

- 36. Wang, Z., Meng, X., Jiang, X., Xiang, H. & Karniadakis, G. E. Solution multiplicity and effects of data and eddy viscosity on navier-stokes solutions inferred by physics-informed neural networks. arXiv preprint arXiv:2309.06010 (2023).

- 37. Zou, Z., Wang, Z. & Karniadakis, G. E. Learning and discovering multiple solutions using physics-informed neural networks with random initialization and deep ensemble. arXiv preprint arXiv:2503.06320 (2025).

- 38. Jagtap, A. D., Kawaguchi, K. & Karniadakis, G. E. Adaptive activation functions accelerate convergence in deep and physics-informed neural networks. J. Comput. Phys. 404, 109136 (2020).

- 39. Wang, H., Lu, L., Song, S. & Huang, G. Learning specialized activation functions for physics-informed neural networks. arXiv preprint arXiv:2308.04073 (2023).

- 40. Jagtap, A. D. & Karniadakis, G. E. Extended physics-informed neural networks (xpinns): A generalized space-time domain decomposition based deep learning framework for nonlinear partial differential equations. In AAAI Spring Symposium: MLPS, 2002–2041 (2021).

- 41. Moseley, B., Markham, A. & Nissen-Meyer, T. Finite basis physics-informed neural networks (fbpinns): a scalable domain decomposition approach for solving differential equations. Adv. Comput. Math. 49, 62 (2023).

- 42. McClenny, L. & Braga-Neto, U. Self-adaptive physics-informed neural networks using a soft attention mechanism. arXiv preprint arXiv:2009.04544 (2020).

- 43. Wang, S., Teng, Y. & Perdikaris, P. Understanding and mitigating gradient flow pathologies in physics-informed neural networks. SIAM J. on Sci. Comput. 43, A3055–A3081 (2021).

- 44. Wang, S., Yu, X. & Perdikaris, P. When and why pinns fail to train: A neural tangent kernel perspective. J. Comput. Phys. 449, 110768 (2022).

- 45. Wang, S., Sankaran, S. & Perdikaris, P. Respecting causality is all you need for training physics-informed neural networks. arXiv preprint arXiv:2203.07404 (2022).


- 46. Müller, J. & Zeinhofer, M. Achieving high accuracy with pinns via energy natural gradient descent. In International Conference on Machine Learning, 25471–25485 (PMLR, 2023).

- 47. Jnini, A., Vella, F. & Zeinhofer, M. Gauss-newton natural gradient descent for physics-informed computational fluid dynamics. arXiv preprint arXiv:2402.10680 (2024).

- 48. Aldirany, Z., Cottereau, R., Laforest, M. & Prudhomme, S. Multi-level neural networks for accurate solutions of boundary-value problems. Comput. Methods Appl. Mech. Eng. 419, 116666 (2024).

- 49. Wang, Y. & Lai, C.-Y. Multi-stage neural networks: function approximator of machine precision. J. Comput. Phys. 504, Paper No. 112865, 28, DOI: 10.1016/j.jcp.2024.112865 (2024).

- 50. McGreivy, N. & Hakim, A. Weak baselines and reporting biases lead to overoptimism in machine learning for fluid-related partial differential equations. Nat. Mach. Intell. 6, 1256–1269 (2024).

- 51. Dahne, J. & Gómez-Serrano, J. Highest cusped waves for the Burgers-Hilbert equation. Arch. Ration. Mech. Anal. 247, Paper No. 74, 55, DOI: 10.1007/s00205-023-01904-6 (2023).

- 52. Dangel, F., Müller, J. & Zeinhofer, M. Kronecker-factored approximate curvature for physics-informed neural networks. arXiv preprint arXiv:2405.15603 (2024).

- 53. Nocedal, J. & Wright, S. J. Numerical optimization (Springer, 1999).

- 54. Martens, J. New insights and perspectives on the natural gradient method. J. Mach. Learn. Res. 21, 1–76

(2020).

- 55. Martens, J. & Grosse, R. Optimizing neural networks with kronecker-factored approximate curvature. In International conference on machine learning, 2408–2417 (PMLR, 2015).

- 56. Botev, A. & Martens, J. KFAC-JAX (2022).
- 57. Eggers, J. & Fontelos, M. A. The role of self-similarity in singularities of pde’s (2008).
- 58. Grosch, C. E. & Orszag, S. A. Numerical solution of problems in unbounded regions: coordinate transforms. J. Comput. Phys. 25, 273–295 (1977).

- 59. Lushnikov, P. M., Dyachenko, S. A. & A. Silantyev, D. New conformal mapping for adaptive resolving of the complex singularities of stokes wave. Proc. Royal Soc. A: Math. Phys. Eng. Sci. 473, 20170198 (2017).

- 60. Boyd, J. P. Spectral methods using rational basis functions on an infinite interval. J. computational physics 69, 112–142 (1987).

- 61. Rathore, P., Lei, W., Frangella, Z., Lu, L. & Udell, M. Challenges in training pinns: A loss landscape perspective. arXiv preprint arXiv:2402.01868 (2024).

- 62. Wang, S., Bhartari, A. K., Li, B. & Perdikaris, P. Gradient alignment in physics-informed neural networks: A second-order optimization perspective. arXiv preprint arXiv:2502.00604 (2025).

- 63. Levenberg, K. A method for the solution of certain non-linear problems in least squares. Q. applied mathematics 2, 164–168 (1944).

- 64. Marquardt, D. W. An algorithm for least-squares estimation of nonlinear parameters. J. society for Ind. Appl. Math. 11, 431–441 (1963).

- 65. Prat-Colomer, M. Machine Learning Methods in Incompressible Fluid Dynamics. Master’s thesis, Universitat Politecnica de Catalunya (2024).

- 66. Trask, N., Henriksen, A., Martinez, C. & Cyr, E. Hierarchical partition of unity networks: fast multilevel training. In Mathematical and Scientific Machine Learning, 271–286 (PMLR, 2022).

- 67. Howard, A. A., Murphy, S. H., Ahmed, S. E. & Stinis, P. Stacked networks improve physics-informed training: applications to neural networks and deep operator networks. arXiv preprint arXiv:2311.06483 (2023).


#### Methods

We aim to discover self-similar blow-up solutions to a system of fluid equations with high numerical accuracy using Physics-Informed Neural Networks (PINNs). The governing equations that define the problem describe the time evolution of physical quantities of the fluid such as fluid density or velocity. Such fields can be written as mappings of the form φA(x,t) : Rd ×R → R for fields labeled by A = 1,2,··· ,NF, where NF is the number of field components of the problem. We use d to denote the spatial dimension involved. We can omit the field index and collect the fields into a vector:

φ(x,t) : Rd ×R → RNF . (1) We use NE to denote the number of governing equations. Self-similar Solutions

We seek solutions whose initial profile evolves in a self-similar manner and blows up at time t = 1. To do so, we introduce the self-similar coordinate y and assume that the behavior of the fields with respect to time is fixed to have a power law behavior. In other words, we assume that there exists a self-similar scaling parameter λ, and for each field with label A, a constant exponent kA(λ) such that:

φA(x,t) = (1−t)kA(λ)ΦA(y) with y = (1−t)−(1+λ)x (2)

solves the governing equations. When d > 1, it is understood that both y and x are vectors related by the timedependent multiplicative factor. The exponents kA(λ) are linear functions of λ assigned in a way such that a power of (1−t) can be factored out of each governing equation. Put differently, kA is determined so that the governing equations, labeled by index k = 1,2,··· ,NE, factor into the form (1−t)fk(λ) ·Ek(Φ(y),λ) = 0 upon plugging in the ansatz of eq. (2). The original dynamical equations are now converted into the steady equations

Ek(Φ(y),λ) = 0, (3) satisfied by the smooth self-similar fields

Φ(y) : Rd → RNF , (4) which only depend on the spatial dimension.

The self-similar scaling parameter λ plays a crucial role in characterizing the self-similar solution, as the governing equations themselves have an explicit dependency on the parameter λ. In fact, for many examples, there is evidence, and in few cases proof57, that smooth self-similar solutions only exist for isolated values of λ. As noted in the main text, we say such values of λ are admissible.

Through the transformation of eq. (2) we have converted the original problem to finding an admissible value of λ and the corresponding smooth self-similar profile Φ(y) satisfying the static equations eq. (3). We model the self-similar profile with neural networks and apply specialized optimization methods to solve the self-similar equations.

###### Solution Modeling and Equation Factorisation

A challenging aspect of solving the self-similar blow-up equations is that they are defined over infinite or semi-infinite spatial domains. Numerically solving these equations in a truncated finite domain introduces significant (truncation) error. In order to overcome this issue, we design a coordinate transformation that maps the entire infinite domain to a finite one58–60. For ease of exposition, we restrict our attention to two-dimensional problems in our presentation, although analogous devices are employed for the one-dimensional case. More details specific to each problem can be found in the Supplementary Information.

A key mathematical constraint we need to satisfy is the asymptotic behavior of the profile at infinity. The asymptotic behavior is dominated by some of the linear terms in the equation, e.g. for the Boussinesq equation, we

expect the vorticity to behave like Ω = curl(U) ∼ |y|−α for the self-similar spatial variable y = (y1,y2) and exponent α = 1/(1+λ).

Based on the power-law decay, we introduce the new coordinate system z = (q,β) whose components are

###### q = ( 1+|y|2)−α = (1+|y|2)−1/(2(1+λ)), β = y2/ 1+y21 +y22. (5)

With these new coordinates, we translate a problem defined on an unbounded domain to that of a bounded domain, since the map y = (y1,y2)  → z = (q,β) maps the y-halfplane to a subset of (0,1]×(−1,1). We pass the pair (q,β) as the input to the neural networks. This allows the networks to learn the profile of the solution within a normalized, finite domain, where its functional variation is expected to be simpler than in the original coordinates.

This coordinate transformation introduces an implicit constraint. Since q(y1,y2) and β(y1,y2) are both even functions of the coordinate y1, any standard neural network receiving them as input will produce an output that is also inherently even in y1. This is not a problem if the field we intend to model has this symmetry, but is an issue if the behavior is expected to be different. We thus construct a structured solution ansatz for each physical quantity based on their symmetry properties. Rather than having the network learn the solution directly, we have it learn a simpler, even function, which is then multiplied by a prefactor designed to enforce the correct symmetry and asymptotic behavior.

Again, we use the vorticity, Ω, from the Boussinesq equation as an example. For this problem, we look for an Ω which is an odd function of y1 and decays at infinity with the power-law exponent α. We formulate the expression for Ω as:

  y1

 

Ω(y1,y2) =

·NNΩ[q,β]· q(y1,y2)

(6)

1+y21 +y22

Asymptotic Decay

Odd Symmetry

where the prefactor is a simple odd function that imposes the correct symmetry on the entire expression. The neural network output, NNΩ[q,β], learns the remaining even part of the spatial profile of the solution in the transformed coordinates. The final multiplication by q(y1,y2) explicitly enforces the required power-law decay rate at infinity.

This construction is generalized for each variable in the problems we solve, allowing us to hard-code both symmetry and asymptotic boundary conditions directly into the model architecture. This strategy offloads the burden of learning global physical constraints from the optimizer and shifts it onto the network design itself. As a result, the network can focus its capacity on learning the localized features of the solution.

We use multi-layer perceptrons (MLPs) with tanh activations as the neural network component. We choose to use an MLP in this context because we want a versatile, hierarchical, nonlinear function approximator, building on the success of Wang et al.16 in this specific context. We use small neural networks with thousands to tens of thousands of parameters. The output of the fields must capture fluctuations of multiple orders of magnitude. Thus the final layer of the network is set to be an exponential or exponential-adjacent activation layer.

Meanwhile, we find that the governing equations of the self similar solutions of eq. (3) can factorize in a useful way. More precisely, writing the neural network component of the field as

Φˆ θ : Rd → RNF where Φˆ A,θ = NNA,θ(z(y)), (7) we find that the governing equations factor in the form:

Ek(Φ(y),λ) = Fk(y)·Rk(Φˆ θ(y),λ), (8)

such that Fk is well defined in the domain of the fields. We add the θ subscript here to make the dependence of Φˆ on the neural network parameters θ explicit. Fk may be the identity for some equations, in which case Ek and Rk would be identical.

We factor the effect of Fk out from the governing equations and denote the remaining factors Rk(Φˆ θ(y),λ), "residuals" of the equations. By doing so, we dispose of the components of the governing equations that are mechanically determined by the assumptions we make about the solution or by the structure of the equation. Now the machine learning problem becomes the problem of finding parameters of the neural networks Φˆ θ that minimize the size of the residuals Rk(Φˆ θ(y),λ). The precise definition of the equation residuals for the CCF, IPM and Boussinesq equations can be found in the Supplementary Information.

###### Training Loss

The goal of training is to make the magnitude of residuals Rk as small as possible across the entire domain of the fields. Thus, the key component of the loss is the zeroth-derivative, or "d0," loss:

1

Nd0NE ∑

ρ

Ld0(Y0) =

(y,ρ)∈Y0

NE

### ∑

k=1

Rk(Φˆ θ(y),λ) 2 . (9)

The dependence of the loss on the sampling batch Y0 is made explicit in this expression. An element of a batch is given by the pair (y,ρ), where y is the sampling point, and ρ is the loss weight assigned to that point.

Only training with the d0 loss can result in a spiky solution, that only has small residuals in a small neighborhood around the d0 training points. To make the residuals as close to a constant as possible, we also utilize higher derivative losses:

NE

1

Nd1NEd ∑

### ∑

ρ

Ld1(Y1) =

(y,ρ)∈Y1

k=1

1

Nd2NEd2 ∑

ρ

Ld2(Y2) =

(y,ρ)∈Y2

d

∂yiRk(Φˆ θ(y),λ) 2 , (10)

### ∑

i=1

NE

d

∂yi∂yjRk(Φˆ θ(y),λ) 2 , (11)

### ∑

### ∑

i,j=1

k=1

where we have used i and j to index the spatial dimensions. The "equation loss" is expressed as a linear combination of these losses:

Lequation = cd0 ·Ld0 +cd1 ·Ld1 +cd2 ·Ld2. (12) We note that each loss has its own assigned training batch.

Without additional constraints imposed, the neural network is bound to produce a constant zero function. Furthermore, there are rescaling symmetries that can act on a solution to produce another solution. In order to avoid such trivial solutions and fix such symmetries, we add normalization conditions on the network where we impose constraints on the field values or its derivatives at certain points. To do so, a point ynorm is chosen at a high gradient region at which the value of a specific field ΦA0 is required to take some value Cnorm. Also, the same field is required to have vanishing value at a set of points Y∞ far away from the origin. A typical "data loss" incorporating these basic constraints takes the form:

Ldata =cˆnorm(ΦA0(ynorm)−Cnorm)2+cˆ∞ ∑

ΦA0(y)2. (13)

y∈Y∞

The constraint points are fixed throughout training. For certain problems, we may introduce constraints for more than one field or derivatives of the field. We also may enforce bounds by acting on a constraint with a relu function before squaring it to add to the data loss. Details on the exact data loss used for each problem can be found in the Supplementary Information. The training loss is obtained by adding the data loss to the equation loss:

Ltrain = Lequation +Ldata. (14)

###### Validation Metrics for Solutions

In order to judge the quality of individual solutions during and after training, we compute the maximum dn residuals of the solutions on a dense validation grid. While the grid may be constructed to span an arbitrary large range within the domain, for example, using the compactified coordinates, practically, the points with large residuals are focused around small regions with high gradients not far from the origin. Thus, for the purpose of evaluation, using a grid that densely samples those regions turns out to be more important. The grids used for evaluating solutions of each problem are specified in detail in the Supplementary Information.

Given a validation grid, the maximum dn residual is defined to be the maximum absolute value of the n-derivative of the residuals, taken along the grid points, the possible derivatives, and the governing equations. More formally,

max d0 residualgrid(Φˆ θ,λ) = max

k∈[NF] y∈grid

Rk(Φˆ θ(y),λ) , (15)

while more generally for n ≥ 1,

max dn residualgrid(Φˆ θ,λ) = max

k∈[NF] i1,···,in∈[d] y∈grid

n

### ∏

∂im Rk(Φˆ θ(y),λ) . (16)

m=1

###### Training Collocation Points

An important element of the training process is the selection of collocation points. Since the residuals of the equations can be computed for any point in space, we must specify how collocation points in space are to be sampled to produce a training batch for the model. We have two challenges. The first is to sample points that have high information content. For example, the solution behaves trivially when we move far away from the origin, while the cancellation of terms in the governing equation are highly non-trivial in regions where the field values and their derivatives are large. Meanwhile, we would like to avoid overfitting, where the model ends up only focusing on lowering the residuals in select regions and choosing to neglect others.

To address both of these challenges, we employ two different sampling methods. The first is location based sampling, where points are sampled from a fixed region in space with an empirical measure. How the regions are selected, how the sampling measure is set, and what loss weights are assigned to the samples are determined empirically and explained in detail in the Supplementary Information.

The next is adaptive sampling, where points are globally sampled but in a way so that points where the model currently does not perform well, i.e., where the residuals of the governing equations are large, are sampled more frequently. In practice, a global grid of points are defined over the compactified coordinates z. The residuals Rk and their derivatives are evaluated over the grid points, and used to define the adaptive sampling weight. For example, for the Boussinesq equation, we define the sampling weight to be proportional to the fourth power of the squared sum of the residuals. After the grid points are sampled, a small perturbation may be applied to the grid point so that a neighboring point is sampled.

For each loss Ld0, Ld1 and Ld2, we define a sampling scheme for the training batches Y0, Y1 and Y2 passed to the loss. The sampling scheme consists of defining point groups and how many samples should taken from each of the point groups. For each group, we designate a sampling method. If location based sampling is being used, we specify the region of space to be sampled from, what the sampling measure is and what the loss weight assignment should be. Typically, a global region, as well as regions close to the origin or peaks of the solutions are utilized. If adaptive sampling is being used, we specify the sampling weight as a function of the residuals and their derivatives, as well as the loss weights for the points. The sampling schemes, regions, measures and loss weights used for the CCF, IPM and Boussinesq equations are presented in full detail in the Supplementary Information.

Diminishing the residuals on a set of collocation points turns out to be a difficult task. Thus resampling the training points very frequently does not lead to meaningful training. We therefore train with a given set of collocation points for an extended number of steps, and only resample them after an order of thousands of steps have elapsed.

###### Second-order Optimizer

The PINN training objective function L (θ,y) can be written as h(θ,y) = ∑ici∥fi(θ,y)∥2 for nonlinear vector-valued functions fi, scalar constants ci > 0, parameter vector θ ∈ Rn, and a vector y representing all of the collocation points. Given an objective of this form, we can apply the classical Gauss-Newton optimization method53, which is a preconditioned gradient descent of the form θt+1 = θt −(G(θt,y)+γtI)−1∇h(θ,y), where G is the Gauss-Newton matrix and γ is a “damping" coefficient.

Unlike other recent works46,47,52,61,62 applying second-order optimization to PINNs, which use approximations that simplify the structure of G, we compute an essentially unbiased stochastic estimate of the full G matrix. In particular, we estimate G using an exponential moving average (across optimizer iterations) of an unbiased rank-1 estimator of G that can be computed from a single matrix-vector product with the Jacobian of the fi’s. This full-matrix approach is feasible due to the small size of our networks.

Because of estimation variance and slight bias of the exponential moving average, we cannot simply use a constant learning rate of 1 (which is viable when G is computed precisely), and instead adopt the scheme described by Martens and Grosse55 to compute "optimal" learning rate and momentum values in closed form at each iteration. This approach increases the per-iteration cost of the method by factor of about 2 to 3 (excluding the cost of matrix inversion, which is non-dominant), but frees us from having to tune learning rate schedules via trial and error and expensive sweeps, and in particular gives us a schedule customized to our training problem.

The optimization algorithm involves the damping coefficient γ, which controls how much we trust the local quadratic approximation of the objective underlying our second-order optimizer. How γ is adjusted throughout optimization is crucial to the robust performance of second-order methods. Depending on the problem, we either use the classical Levenberg-Marquardt method63,64 or employ custom schedules for adjusting the value of γ.

This optimizer can be fully realized using a particular configuration of the open source kfac-jax library56, which is a general framework supporting different 2nd-order optimizers including, but not restricted to, K-FAC. For a fully detailed description of our optimization method and its implementation, see the Supplementary Information.

###### Identifying Admissible λ Values

The scaling parameter λ plays a central role in studying self-similar solutions. We operate with the assumption that there exist discrete admissible values of λ that admit smooth solutions to the self-similar equations, which we present empirical evidence for later on. Thus identifying admissible values of λ is a key element to discovering solutions to the self-similar equations.

In this work, we simultaneously optimize λ as we train the parameters of the neural network. Three different methods for λ optimization are employed. The combination of λ optimization methods used for each problem and solution can be found in the Supplementary Information.

- 1. Gradient training: The simplest way to optimize λ is to introduce it as a trainable parameter and optimize it along with the other neural network parameters16. While gradient training is able to successfully identify admissible values of λ for stable blow-up solutions in the CCF, IPM, and Boussinesq problems, we find it to be unreliable for discovering unstable, high-order solutions.
- 2. λ Inference: We use the λ inference method (c.f. Prat-Colomer65 in the context of ML and rotating solutions of the Euler equation), where we infer the value of λ best suited for describing the current numerical solution from the governing equations. Assuming the smoothness of the solution, we take the first derivative of the nonlinear self-similar equation for the given problem and evaluate it at the origin. Requiring that this value vanishes allows us to derive an explicit analytical relationship between λ and field values at the origin (y1,y2) = (0,0). For example,

the relation derived for the Boussinesq problem is that λ = −3−2∂y1U1(0,0), where ∂y1U1(0,0) is the velocity gradient at the origin. We then implement this relationship as a direct analytical update rule for λ during training, bypassing the need for an optimization-based search.

- 3. Funnel Inference: Another method we introduce for optimizing λ is funnel inference. This method is


based on the principle that the governing equation can be perfectly satisfied only at admissible values of λ. Thus in the neighborhood of an admissible value λ∗ of the self-similar scaling parameter, the smallest achievable maximum residual as a function of λ should have a funnel-like shape, the bottom of which is positioned at λ∗. If we consider this residual with sign, in other words, define the residual with maximum absolute value to be r(λ), r(λ) should be approximately linear near λ∗ where it has zero value. The idea of funnel inference is to use the secant method to find the zero of this function r(λ).

Since r(λ) is not directly measurable, we find a proxy for r(λ). To do so, for a given constant λ value, we proceed to train the neural network with this fixed λ value until the solution has relaxed sufficiently. Operating with the assumption that this signal can be accurately captured by examining a small neighborhood of the origin, we measure the residuals of the equation and identify the value of the residual with maximum absolute value in this region to be rˆ(λ). Then λ is updated to a new value, and the training process repeats. The update rule is given as follows. Given the history of λ values λ0,··· ,λn and the corresponding rˆ(λ) values rˆ0,··· ,rˆn, if n ≥ 1, λn+1 is obtained by using the secant formula on λn−1 and λn:

λn−1 −λn rˆn−1 −rˆn

λn+1 = λn −rˆn−1 ·

. (17)

If n = 1, we use a small value ∆λ to perturb λn−1: λ1 = λ0 +∆λ . (18)

The updates terminate if a sufficient amount of training steps have been taken. Further details on the funnel inference algorithm may be found in the Supplementary Information.

###### Multi-stage Training

If we only employ methods described up to this point, we are unable to reach maximum equation residuals much below 10−8. To discover higher-precision solutions, we employ multi-stage training49, which divides the training process into different stages, each with a dedicated neural network, c.f. hierarchical training66,67. In this study, we apply two-stage training to the stable and first unstable solutions of the CCF and IPM equations. This approach lets us reach machine precision, as shown in the Supplementary Information. In the second stage, we train a new neural network that specifically learns the error Rkstage-1 between the first-stage networks and the exact solution. The final solution is obtained by composing the output of the two networks. This approach offers two advantages over single stage training.

1. Linearized governing equation: Despite the nonlinearity of the original equation, the governing equation for the second stage training is effectively linear. We can formalize this mathematically by expressing the exact solution, Φˆ exact, as the sum of the first-stage solution, Φˆ stage-1, and a small error correction term: Φˆ exact = Φˆ stage-1 +εΦˆ stage-2. Assuming that the first-stage training converges properly, the magnitude of the error ε should be much less than

- 1. Then Φˆ stage-2 becomes the normalized error profile that the second-stage network is trained to approximate. Substituting this ansatz into a governing PDE, we arrive at the governing equation for the error profile Φˆ stage-2:

−εDk[Φˆ stage-1]Φˆ stage-2 +O(ε2) = Rkstage-1, (19) where Dk[Φˆ stage-1] is the linear operator obtained by expanding the residual Rk around the approximate solution

- Φˆ stage-1. By neglecting the O(ε2) and higher-order terms, this equation becomes linear with respect to the function
- Φˆ stage-2. The right-hand side of Equation (19) is the equation residual from the first stage, which now acts as a known source term for the linear equation governing second stage training.


- 2. Informed network structure: Given the near-linearity of the second stage governing equations, the properties of the first-stage residuals Rkstage-1 can inform the optimal architecture for the second-stage network. As shown in Wang & Lai49, the characteristic features of the error profile Φˆ stage-2 are governed by the source term Rkstage-1. For


![image 27](Wang et al._2025_Discovery of Unstable Singularities_images/imageFile27.png)

- Figure 5. Smoothness signal in λ. Maximum residuals over the input space as a function of λ −λi for admissible λi of the Boussinesq equation with error bars. The plotted values and error bars are produced based on five experiments with varying seeds. Each subplot is centered around a different admissible lambda value, where λ0 is the self-similar scaling parameter for the stable solution, and λn with n ≥ 1 is that for the n-th unstable solution. The x-axis shows the difference between the lambda value and the closest admissible lambda value (λ −λi), while the y-axis shows the mean and standard deviation of the log 10 maximum residual at 400k training steps. The plots show how the residuals increase as the lambda value deviates from λi for each i, indicating that λi is close to the local minimum of smoothness errors.


example, the equation residual typically exhibits higher frequency content than the solution Φˆ stage-1. This implies that the error function Rkstage-1 is also a high-frequency function. Leveraging this fact, we can embed the appropriate inductive bias into the second stage network. Instead of using a standard MLP, we employ a Fourier feature network, which incorporates a Fourier mapping layer [cos(Bx),sin(Bx)] placed after the linear input layer. The weights B of this layer are sampled from a Gaussian distribution B ∼ N (0,σ), where σ indicates the standard deviation of the distribution. We directly set the hyperparameter σ using the dominant frequency fd(e) of the first-stage equation residuals Rkstage-1, namely σ = 2π fd(e). This provides a principled way of designing a network that is inherently suited to learn the high-frequency error function.

###### Validation of λ

Once we discover a numerical solution Φˆ ∗ and the associated self-similar scaling parameter λ∗, we also validate the admissibility of λ∗. Ideally, if we are able to evaluate the function R(λ) which returns the lowest possible maximum residual achievable with a numerical function Φˆ θ for a given λ, that is,

R(λ) = min

θ

max d0 residualgrid(Φˆ θ,λ) , (20)

the admissibility of λ can be validated at this level by requiring that λ∗ is a local minimum of R(λ). We refer to R(λ) as the smoothness error of λ in this section.

Since we do not have the ability to evaluate R, we construct a proxy for the smoothness error by running the training pipeline that we have presented up to now, but with constant λ, and evaluating the maximum residual of the final solution obtained this way. In practice, this is done for a set number of neural networks initialized with different seeds. We take the geometric mean of the maximum residuals of the final solutions to produce the proxy function R˜(λ) for R(λ). We also compute the standard deviation of the metrics in log space to measure the uncertainty E˜(λ) of this value. We construct a small exponentially spaced grid centered at λ∗, evaluate R˜(λ) at those grid points and plot them against the λ values. This is done for the λ values discovered for the Boussinesq equation in figure 5. Note that the plots have a funnel shape centered around the discovered λ values.

In figure 6 we take the plots of figure 5 and scale the λ-axis to be in symlog-scale. We find that the log-symlog plot of smoothness signal has a bowl shape due to the numerical nature of the evaluation method. In other words, there exists a limit to the resolution of λ at which this method can discern admissibility.

Based on these observations, we use these funnel plots as a method to validate admissibility of a λ∗ value, and to determine its significant digits. First, we require that λ∗ lie at a basin of the bowl of the zoomed-in funnel

![image 28](Wang et al._2025_Discovery of Unstable Singularities_images/imageFile28.png)

- Figure 6. Funnel plots for validation. Figure 5 with the x-axis in symlog-scale. The λi values displayed now have been truncated to their significant digits based on the width of the basin of each plot.


plot in order to be considered valid. Furthermore, we interpret the width of the basin to be the resolution at which admissibility can be determined. We hence identify the last digit of the numerically attained admissible scaling parameter by the minimum perturbation that pushes the λ value out of the basin of the bowl.

###### Spectrum of Linearization

The self-similar profiles constructed are steady-state solutions to their respective governing equations when viewed in an appropriate rescaled or co-moving coordinate system. The linear stability of such a steady state, which we denote as Φλ, is determined by the spectral properties of the operator D[Φλ] derived by linearizing the system around Φλ. This leads to an eigenvalue problem of the form:

D[Φλ]Ψ = µΨ. Here, the eigenfunction problem is restricted to Ψ that lie within the same symmetry class as the original solution.

A profile Φλ is considered linearly stable if the portion of its spectrum with a non-negative real part, ℜ(µ) ≥ 0, consists solely of the trivial eigenvalues arising from the symmetries of the problem. If the spectrum contains any other eigenvalues in this region, the solution is considered linearly unstable. The number of these non-trivial eigenvalues µi with a non-negative real part, ℜ(µi) ≥ 0, is referred to as the order of instability. For a computerassisted proof to be feasible, it is desirable that the spectrum in the right-half µ-plane consists of a finite number of eigenvalues.

In order to analyze the stability of the new solutions discovered in this work, we learn the non-negative real eigenvalues of the corresponding linearized operators, under the assumption that there exist eigenvalues with non-negative real part that lie on the real axis. We again employ PINNs to solve the eigenvalue problem, optimizing the eigenvalue µ simultaneously with the neural network representing the eigenfunction Ψ. The methods used to discover the solution of the self-similar equations themselves are largely transferred over to discovering the solutions to the eigenvalue problem. The PINNs are now trained to minimize eigenvalue equation residuals. The specific linearized operators, as well as details on the eigenfunction training setup for each problem can be found in the Supplementary Information.

#### Acknowledgements

C-Y. Lai acknowledges the NSF via grant DMS-2245228. T. Buckmaster and Y. Wang were supported in part by the NSF grant DMS-2243205 and the Simons Foundation Mathematical and Physical Sciences collaborative grant ‘Wave Turbulence’. T. Buckmaster was also supported by the NSF grant DMS-2244879. Y. Wang’s research was additionally supported by a gift to Buckmaster from Google as well as an NYU Postdoctoral Research and Professional Development Support Grant. Both T. Buckmaster and Y. Wang gratefully acknowledge Google for providing computing credits and subscriptions, as well as Stanford Research Computing and New York University High Performance Computing for providing computational resources and support. G. Cao-Labora has been supported

by NSF under grant DMS-2052651 during part of this work. G. Cao-Labora and J. Gómez-Serrano have also been partially supported by the MICINN research grant number PID2021–125021NA–I00. J. Gómez-Serrano was partially supported by NSF Grants DMS-2245017, DMS-2247537 and DMS-2434314; and by the Simons Foundation through a Simons Fellowship.

We thank A. P. Badia, J. Bausch, C. Blundell, A. Botev, V. Dalibard, D. Hassabis, G. Holland, P.-S. Huang, Y. Li, A. Novikov, S. Nowozin, A. Pritzel, D. Rezende and P. Wirnsberger for their contributions, sponsorship, advice and helpful discussions.

This work represents a collaboration between academic institutions and Google DeepMind.

