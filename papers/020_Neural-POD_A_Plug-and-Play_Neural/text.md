# arXiv:2602.15632v2[physics.comp-ph]1 Mar 2026

## Neural-POD: A Plug-and-Play Neural Operator Framework for Infinite-Dimensional Functional Nonlinear Proper Orthogonal Decomposition

##### Changhong Mou1, Binghang Lu2, Guang Lin3,4*

1Department of Mathematics and Statistics, Utah State University, 3900 Old Main Hill, Logan, UT, 84322, USA. 2School of Electrical and Computer Engineering, Purdue University, 610 Purdue Mall, West Lafayette, IN, 47907, USA. 3Department of Mathematics, Purdue University, 610 Purdue Mall, West Lafayette, IN, 47907, USA. 4School of Mechanical Engineering, Purdue University, 610 Purdue Mall, West Lafayette, IN, 47907, USA.

*Corresponding author(s). E-mail(s): guanglin@purdue.edu; Contributing authors: changhong.mou@usu.edu; lu895@purdue.edu;

Abstract AI for science (AI4Science) models often suffer from discretization: learned representations remain tied to the training grid, limiting transfer across resolutions, solvers and applications. We introduce Neural Proper Orthogonal Decomposition (Neural-POD), a plug-and-play neural operator that learns nonlinear, orthogonal basis functions directly in function space and can be integrated in both projection-based reduced order models and operator-learning frameworks such as DeepONet. Neural-POD replaces SVD-derived, resolutiondependent linear modes with continuous, resolution-invariant bases learned via sequential residual minimization, analogous to Gram–Schmidt orthogonalization. The framework supports training under task-specific norms (e.g., L2, L1), improves out-of-distribution generalization to unseen parameter regimes, and captures nonlinear structure in complex systems. Because the learned bases are interpretable and reusable, Neural-POD serves as a general representation module for AI4Science workflows. We demonstrate Neural-POD on Burgers’ and Navier–Stokes equations.

Keywords: Neural Operator, Plug-and-Play, Operator Learning, Reduced Order Modeling, Function Space Orthogonal Bases

AI for science (AI4Science) increasingly relies on learned representations that must transfer reliably across discretizations, geometries, and parameter regimes, rather than being tied to a particular grid or snapshot resolution. In this setting, a central challenge is to build low-dimensional structures that are both faithful to the underlying infinite-dimensional dynamics and reusable across solvers and data that supports efficient simulation without retraining from scratch whenever the discretization changes. Consequently, Proper Orthogonal Decomposition (POD) is widely used in AI4Science as a physics-informed representation tool that provides compact low-dimensional bases for high-dimensional data that support efficient learning, inference and prediction across different scientific tasks. POD, also known as principal component analysis (PCA), is a foundational technique in computational modeling for extracting dominant coherent structures from high-dimensional data. Historically, it emerged from early ideas in statistics and stochastic-process theory (PCA and the Karhunen–Loe`ve viewpoint) and was later adopted in fluid mechanics and turbulence as a dominant way to identify energetic coherent modes from spatiotemporal measurements and simulations [1–3]. POD supports a broad range of methodologies, including reduced order modeling (ROM), where POD modes provide low-rank representations that enable efficient simulation while preserving essential dynamics [4–6], and scientific machine learning (SciML), where POD-based decompositions offer structured low-dimensional representations for learning operators and dynamics (for example, POD–DeepONet architectures [7]). Beyond ROM and operator learning, POD is widely used for data compression, feature extraction and modal analysis in complex spatiotemporal systems. Classical POD is typically computed via singular value decomposition (SVD), yielding L2-optimal linear basis functions from snapshot data [8]. Yet, when modern applications demand robustness for different discretizations, diverse regimes and strongly nonlinear behaviours, traditional POD faces persistent obstacles.

These obstacles are well recognized. First, POD is often resolution-dependent: modes learned on one discretization may lose optimality or even effectiveness when the grid changes, limiting transferability across resolutions [9]. Second, POD may lose accuracy even for in-distribution interpolation and can fail more severely for out-ofdistribution extrapolation beyond the training regime, which limits its reliability in previously unseen scenarios [10]. Third, although POD is optimal in an L2 sense within the training dataset, its linear subspace structure can be too restrictive to represent the nonlinear features that drive many physical systems [4, 11]. As a consequence, sharp gradients, discontinuities and other strongly nonlinear structures may be poorly captured, especially when such features dominate the dynamics [12]. Taken together, these challenges complicate deployment in multi-resolution regimes and hinder realtime simulation, where one needs a compact representation that generalizes reliably as dynamical or physical regimes change.

To address these limitations, we propose neural proper orthogonal decomposition (Neural-POD), a drop-in framework that replaces linear POD modes with

nonlinear basis functions parameterized by neural networks. The key idea is to preserve the progressive, mode-by-mode error reduction of POD while upgrading the representational power and enabling transfer across resolutions and regimes. Given snapshot data, Neural-POD learns the first mode by minimizing a reconstruction loss between the snapshots and a neural representation with a learnable time-dependent coefficient; subsequent modes are learned sequentially by training new networks on the residual from the previous approximation [13–15]. This iterative procedure yields an orthogonal set of Neural-POD modes while directly retaining the structures most relevant to the data. Crucially, after training, only the Neural-POD model parameters (and the associated low-dimensional coefficients) need to be stored, not resolutionspecific basis vectors nor the full snapshot matrix, which makes the representation compact and easy to deploy. This compactness enables rapid online evaluation and supports real-time or many-query tasks, where one repeatedly updates reduced states or operators under limited computational budgets.

Neural-POD offers additional benefits that directly target the above challenges. First, the training objective is flexible that allows optimization in task-relevant norms (for example L2, L1 or H1), rather than being prescribed to a fixed L2 criterion. Second, representing modes as neural functions admits resolution independence and improves in-distribution and out-of-distribution across multi-resolution settings [16]. Third, the learned representation can be reused across parameter variations with substantially reduced retraining burden, enabling efficient parametric studies. Finally, Neural-POD can serve as a pretrained, drop-in component inside broader operatorlearning frameworks [17] that provides a structured latent representation that is both compact to store and fast to evaluate for real-time development.

These properties position Neural-POD as a bridge can between projection-based ROM and modern deep learning. In classical ROM, Neural-POD can be inserted into Galerkin projection frameworks to provide a more expressive and transferable basis while retaining the interpretability and structure of projection methods [18–20]. In operator learning, Neural-POD offers a principle low-dimensional representation that can improve both efficiency and interpretability. For instance, Deep Operator Networks (DeepONets) comprise a branch network that encodes the input function sampled at sensor locations and a trunk network that encodes query locations for the output [21–23]. By using Neural-POD as the branch network, DeepONets can incorporate orthogonal, data-driven nonlinear modes that capture underlying dynamics while remaining resolution-independent. This integration can improve generalization across discretizations and reduce training costs (since only Neural-POD can be pretrained), thereby enabling more efficient and robust operator learning in real-time or near-real-time settings. In brief summary, our primary contributions include the following:

• Neural-POD is a plug-and-play component for both Galerkin ROM and operator learning: once the basis/model is learned offline, it can be dropped into a reduced order model with minimal modification, and the online stage only requires assembling and evolving the reduced system for fast, easy deployment across parameterized PDEs (see Figure 1b). This bridges traditional ROM and surrogate

modeling with operator learning by fitting naturally into familiar offline/online workflows and existing Galerkin solvers (see Figure 2a). Moreover, the same plug-and-play interface enables straightforward reuse across PDEs with different parameters which supports a pretrained, open-source database and a shared repository of benchmark problems spanning diverse geometries and parameter settings.

- • Neural-POD also has strong educational value as an easy-to-use ROM and operator-learning tool. (see Figure 2b) Its modular, plug-and-play property makes it well-suited for classroom adoption (e.g., undergraduate numerical analysis, scientific computing, and introductory SciML courses), where students can rapidly learn reduced order models and operator learning, explore the offline/online procedures, and build intuition for projection-based modeling without heavy software overhead. This positions Neural-POD as a practical foundation for course modules, hands-on assignments, and open teaching resources with broad educational impact.
- • Neural-POD enables accurate in-distribution prediction and reasonable generalization for out of distribution prediction by learning resolutionindependent basis functions that remain effective under modest parameter shifts, without retraining (see Figure 4d–4e and Table 1).
- • Neural-POD constructs nonlinear, orthogonal basis functions through an iterative residual minimization procedure using with neural networks that is analogous to Gram–Schmidt orthogonalization and capable of capturing complex features (see Figure 1c).
- • Neural-POD supports training under different norms (e.g., L2, L1), which enables the learned bases to reflect smoothness, discontinuities, or other structural characteristics induced by the chosen norm (see Figures 4a–4c).
- • Neural-POD is formulated in infinite-dimensional function spaces, which matters because it learns basis functions rather than grid-dependent vectors. Therefore, the same modes can be evaluated consistently on different discretizations, enabling resolution-independent basis construction and seamless deployment across spatial resolutions (See Algorithm 1).


The above novelties are also illustrated in Figures 1a and 1b.

Rapid progress in AI4Science for reduced representations and operator learning has exposed a key gap: performance can be highly sensitive to discretization choices (resolution, numerical schemes, and discretization error), limiting reliability and generalization for different regimes. We address this by studying the robustness of Neural-POD’s nonlinear functional representations and integrating them into (i) projection-based ROMs and (ii) DeepONet-style operator learning. We further assess performance under a fixed training budget to identify when Neural-POD remains effective. Using Burgers’ equation and 2D Navier–Stokes, we benchmark NeuralPOD against classical POD in reconstruction, predictive accuracy, and robustness to in-distribution and out-of-distribution parameters.

| | |
|---|---|
| | |
| | |
| | |
| | |


###### POD Limitation Neural-POD Advantage

Functional Nonlinear ApproximationNeural networks are universal function approximates. See Figs. 3(b). and 5(d).

###### Discrete Linear Representation

Defined only at the training grid points; basis functions are discrete vectors.

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


Φ(x)

###### Resolution-Dependence

###### Resolution-Independence

Bases are discrete vectors tied to a mesh.

Learns a continuous functional mapping ϕ(x) in infinite-dimensional space, evaluable on any grid.

###### Parameter-Dependence

Plug-and-PlayLearns a continuousGeneralizationparameter-tobasis map that generalizes to new PDE parameters. See Figs. 2. and 4 (d–e).

Requires new snapshots and SVD for new parameters.

∀κ

###### Fixed L2 Optimality

###### Flexible Optimality

L2

L2

SVD inherently minimizes the L2 norm.

The loss function can be defined in any norm L1, L2, H1, etc. See Fig. 4.

L1 H1

- (a) Comparison between classical POD and Neural-POD. Classical POD constructs discrete, resolution-dependent basis vectors tied to training grids and parameters, whereas NeuralPOD learns continuous, nonlinear, resolution-invariant basis functions expressed by neural networks, enabling parameter generalization and flexible optimality norms.

M

Classical Methods

Galerkin Projection

Branch Trunk

×

Operator Learning

DeepONets

Neural–POD

Neural-POD-ROM

- • Basis functions represented directly by neural networks
- • Nonlinear and parameteraware structure
- • Compatible with classical projection-based ROMs
- • See Section 2.3.


Pretrained Neural-POD:

- • Orthogonal, nonlinear bases
- • Infinite-dimensional function spaces
- • Functional formulation allows modest extrapolation without retraining


Neural-POD-DeepONet

- • Pre-trained Branch Net
- • Physically interpretable representations
- • Resolution-invariant operator learning
- • See Section 2.4.


- (b) Neural-POD as a bridge between projection-based reduced-order models and operator learning. Neural-POD provides orthogonal, nonlinear basis functions for Galerkin ROMs while simultaneously serving as a pretrained, physically interpretable Branch Network within DeepONet architectures.

|NN|
|---|


Φ1(x;κ)

x

|F|
|---|


Ψ1(t;κ)

t

×

|NN|
|---|


Φ2(x;κ)

x

|F|
|---|


Ψ2(t;κ)

t

×

...

|NN|
|---|


Φn(x;κ)

x

|F|
|---|


Ψn(t;κ)

t

×

u(1)(x,t) ≈ u0(x;κ) + Φ1(x;κ)Ψ1(t;κ)

u(2)(x,t) ≈ u0(x;κ) + Φ1(x;κ)Ψ1(t;κ)

+ Φ2(x;κ)Ψ2(t;κ)

u(N)(x,t) ≈ u0(x;κ) +

N

i=1

Φi(x;κ)Ψi(t;κ)

Ω1

Ω1 ⊥ Ω2

∪Ni=1−1Ωi ⊥ ΩN

Neural-POD Training

![image 1](Mou et al._2026_Neural-POD A Plug-and-Play Neural Operator Framework for Infinite-Dimensional Functional Nonlinear_images/imageFile1.png)

![image 2](Mou et al._2026_Neural-POD A Plug-and-Play Neural Operator Framework for Infinite-Dimensional Functional Nonlinear_images/imageFile2.png)

![image 3](Mou et al._2026_Neural-POD A Plug-and-Play Neural Operator Framework for Infinite-Dimensional Functional Nonlinear_images/imageFile3.png)

![image 4](Mou et al._2026_Neural-POD A Plug-and-Play Neural Operator Framework for Infinite-Dimensional Functional Nonlinear_images/imageFile4.png)

![image 5](Mou et al._2026_Neural-POD A Plug-and-Play Neural Operator Framework for Infinite-Dimensional Functional Nonlinear_images/imageFile5.png)

![image 6](Mou et al._2026_Neural-POD A Plug-and-Play Neural Operator Framework for Infinite-Dimensional Functional Nonlinear_images/imageFile6.png)

![image 7](Mou et al._2026_Neural-POD A Plug-and-Play Neural Operator Framework for Infinite-Dimensional Functional Nonlinear_images/imageFile7.png)

![image 8](Mou et al._2026_Neural-POD A Plug-and-Play Neural Operator Framework for Infinite-Dimensional Functional Nonlinear_images/imageFile8.png)

![image 9](Mou et al._2026_Neural-POD A Plug-and-Play Neural Operator Framework for Infinite-Dimensional Functional Nonlinear_images/imageFile9.png)

![image 10](Mou et al._2026_Neural-POD A Plug-and-Play Neural Operator Framework for Infinite-Dimensional Functional Nonlinear_images/imageFile10.png)

![image 11](Mou et al._2026_Neural-POD A Plug-and-Play Neural Operator Framework for Infinite-Dimensional Functional Nonlinear_images/imageFile11.png)

![image 12](Mou et al._2026_Neural-POD A Plug-and-Play Neural Operator Framework for Infinite-Dimensional Functional Nonlinear_images/imageFile12.png)

time

t

parameter κ

κ1 κ2 κ3

Snapshots u(x,t,κ)

mode

parameter κ

κ1 κ2

Neural POD: ϕ1(ˆx,κˆ), ... ,ϕP(ˆx,κˆ)

Plug-and-play with any discretization x and parameter choice κ.

- (c) Overview of Neural-POD training. Snapshots u(x, t, κ) are collected over time for varying parameter values κ (upper left). The training architecture decomposes each snapshot into


products of spatial mode functions Φi(x; κ) and temporal coefficients Ψi(t; κ), which guarantees the orthogonality for all modes (bottom left). Once trained, the Neural-POD basis provides plug-and-play reduced representations that can be evaluated on any discretization xˆ and parameter choice κˆ (right, κˆ may differ from the training snapshots’ parameter κ).

Fig. 1: Neural-POD for resolution-independent model reduction and operator learning.

Neural-POD-ROMs

Plug-and-play with arbitrary meshes at arbitrary resolution

###### Pretrained Neural POD

###### Parameters from PDEs

- a(1)1

- a(1)2


- a(2)1

- a(2)2


a(3)1

x1

.

###### .

- a(1)1

- a(1)2


- a(2)1

- a(2)2


.

.

a(3)1

x1

a(3)m

xn

- a(1)1

- a(1)2


- a(2)1

- a(2)2


a(1)m

a(2)m

a(3)1

x .

.

1

κ1,κ2,...,

ϕP

.

.

.

.

a(3)m

xn

.

.

a(1)m

a(2)m

a(3)m

xn

ϕ2

a(1)m

a(2)m

ϕ1

###### Snapshots for parameter κ

###### Galerkin Projection

POD Modes

###### Truncation

###### Projection of PDEs on Rr

r

ϕP

us

SVD

αˆk ϕk, r ≪ P

ur =

∂uˆr ∂t

, ϕk = (F(ˆur), ϕk) k = 1, . . . , r ROM obtained

k=1

ϕ1

u1

r: most energetic modes, ur ∈ Rr: linear reduced states

da dt

= F(a)

F: nonlinear PDE operator a = [ ˆα1 αˆ2 . . . αˆr ]⊤: sought ROM solution

v = [ ϕ1 ϕ2 . . . ϕP ] P: full rank modes

Y = [ u1 u2 . . . uS ] S: number of snapshots

POD–ROMs

POD Reduced Order Models (POD-ROMs) Neural-POD Reduced Order Models (Neural-POD-ROMs)

- (a) Schematic diagram of the proposed Neural-POD-ROMs and traditional POD-based reduced order models (POD-ROMs). Top portion: the Neural-POD extension that enables plug-and-play operation on arbitrary meshes and at arbitrary resolution, informed by pretrained neural representations of POD bases and PDE parameters. Bottom portion: the traditional POD flowchart, including snapshot generation for parameter κ, computation of full POD modes via SVD, construction of the reduced basis, and Galerkin projection of the governing PDE.

Branch Net

Input layer Hidden layers Output layer

.

Trunk Net

.

×

Gθ(u)(x)

Initial Condition Samples

![image 13](Mou et al._2026_Neural-POD A Plug-and-Play Neural Operator Framework for Infinite-Dimensional Functional Nonlinear_images/imageFile13.png)

![image 14](Mou et al._2026_Neural-POD A Plug-and-Play Neural Operator Framework for Infinite-Dimensional Functional Nonlinear_images/imageFile14.png)

![image 15](Mou et al._2026_Neural-POD A Plug-and-Play Neural Operator Framework for Infinite-Dimensional Functional Nonlinear_images/imageFile15.png)

![image 16](Mou et al._2026_Neural-POD A Plug-and-Play Neural Operator Framework for Infinite-Dimensional Functional Nonlinear_images/imageFile16.png)

- u1(x;θ)
- u2(x;θ)
- u3(x;θ)


.

uM(x;θ)

Pretrained Neural POD

x1

xn

.

- a(1)1

- a(1)2


a(1)m

.

- a(2)1

- a(2)2


a(2)m

.

a(3)1

a(3)m

.

x1

xn

.

- a(1)1

- a(1)2


a(1)m

.

- a(2)1

- a(2)2


a(2)m

.

a(3)1

a(3)m

x .

1

xn

.

- a(1)1

- a(1)2


a(1)m

.

- a(2)1

- a(2)2


a(2)m

.

a(3)1

a(3)m

- ϕ1 .
- ϕ2


.

ϕP

Neural-POD Deep Operator Network (NP-DeepONet)

- (b) Schematic of the proposed Neural-POD Deep Operator Network (NP-DeepONet). The branch network takes initial condition fields as input, while the trunk network evaluates functions at spatial query points. A pretrained Neural-POD module provides reduced basis information ϕ1, ϕ2, . . . , ϕP obtained from snapshot data. The outputs are combined to produce the operator evaluation Gθ(um)(x), enabling efficient and data-driven surrogate modeling of PDE solutions in reduced coordinates.


###### Fig. 2: Neural-POD integrations for reduced order modeling and operator learning.

### Results

#### Neural-POD for Burgers’ equation

To demonstrate the capability of the proposed framework in addressing nonlinear PDEs, we use the one-dimensional (1D) Burgers’ equation with periodic boundary conditions as discussed in Li et al. [24, 25].

∂2u ∂x2

∂u ∂t

∂u ∂x − ν

= 0, (x,t) ∈ (0,1) × (0,1], (1) u(x,0) = u0(x), x ∈ (0,1), (2) u(0,t) = u(1,t),

+ u

du dx

du dx

(1,t), t ∈ (0,1). (3)

(0,t) =

where t ∈ (0,1), and the initial condition u(x) is generated from one distribution of GRF ∼ N(0,252(−∆ + 52I)−4), satisfying the periodic boundary conditions.

In the following experiments, the Neural-POD model is trained using snapshot data generated at viscosity values ν sampled within the interval [0.005,,0.01]. This parameter range defines the training domain for the Neural-POD basis learning. Figure 3a shows the evolution of the one-dimensional Burgers equation for different sampled viscosity values ν used to construct the training dataset for Neural-POD. As ν decreases (right to left), the solution transitions from a smooth diffusive profile to one dominated by advective nonlinearities, leading to the formation of sharp fronts and nearly discontinuous shock structures. This coupled effects of convection and diffusion underscores the limits of traditional POD in handling unseen parameters, motivating parametric POD formulations that adapt to viscosity and smoothness variations. Extended Data Figure 1 shows the first three Neural-POD modes trained from FOM data for different viscosity values. As the viscosity changes, the Neural-POD modes behaves significantly different behavior, with ν decreases, Neural-POD becomes increasingly oscillatory and sharply localized near the shock region. Such sensitivity of the Neural-POD basis to the viscosity parameter indicates that the modes are not easily transferable across regimes, making it challenging to construct a compact parametric traditional POD representation that remains accurate for a wide range of different viscosity flows.

###### Neural-POD with L1 and L2 loss

In addition to the standard L2 based training loss, we also consider an L1 norm formulation to show the robustness of the Neural-POD framework. The corresponding loss terms are defined as

L1 Optimality: Ldata =

N

Boundary conditions: Lbc =

i=1

N

|Φ(xi)Ψ(ti) − ui|, (4)

i=1

2

N

∂ubci ∂x

∂Φ(xbci ) ∂x −

Φ(xbci ) − ubci 2 +

. (5)

i=1

Compared to the L2-norm, the L1-based loss penalizes large residuals less aggressively, thereby reducing the influence of outliers and improving the representation of localized or discontinuous features in the data.

Extended Data Figure 2 illustrates the reconstruction of spatiotemporal fields using the Neural-POD model for a viscosity case not included in the training data. The results are shown for latent dimensions of 2, 4, and 6. Since the traditional POD basis depends on snapshot data from the training parameters, it cannot be constructed for this unseen case. In contrast, the Neural-POD can accurately reconstruct the spatio-temporal dynamics even with only two or four modes which shows strong generalization capability and the ability to capture nonlinear correlations between spatial and temporal features beyond the training regime. As the dimension of modes increases, the Neural-POD reconstructions further improve and closely approach the truth solution, consistently yielding lower reconstruction errors and better preservation of localized fine-scale structures over time. For the case with r = 6, the model trained with the L1 loss exhibits better performance compared to its L2 loss Neural-POD, as it more effectively captures the steep gradients and localized features. Figure 3b compares the first three spatial modes obtained from the classical POD and those learned through Neural-POD training using L1- and L2-based losses across different viscosity regimes. The L2-optimal Neural-POD tends to emphasize smooth, energy-dominant structures, while the L1-based formulation better preserves localized sharp transitions by penalizing large pointwise deviations less severely. Figure 4a shows that the NeuralPOD residual decreases rapidly with the number of modes, closely mirroring the decay of the classical POD residual.

8

![image 17](Mou et al._2026_Neural-POD A Plug-and-Play Neural Operator Framework for Infinite-Dimensional Functional Nonlinear_images/imageFile17.png)

- (a) Solution snapshots of the Burgers equation at different sampled viscosity values ν used for Neural-POD training.

![image 18](Mou et al._2026_Neural-POD A Plug-and-Play Neural Operator Framework for Infinite-Dimensional Functional Nonlinear_images/imageFile18.png)

- (b) First three traditional POD modes and Neural-POD under different loss choices, i.e., L1 and L2 norms, for different viscosity values.


###### Fig. 3: Burgers equations: (a) solution snapshots for different viscosities ν; (b) traditional POD modes versus Neural-POD bases learned with L1 and L2 losses.

![image 19](Mou et al._2026_Neural-POD A Plug-and-Play Neural Operator Framework for Infinite-Dimensional Functional Nonlinear_images/imageFile19.png)

![image 20](Mou et al._2026_Neural-POD A Plug-and-Play Neural Operator Framework for Infinite-Dimensional Functional Nonlinear_images/imageFile20.png)

- (a) Neural-POD residuals versus modes r for the L2 loss (left) and the L1 loss (right).

![image 21](Mou et al._2026_Neural-POD A Plug-and-Play Neural Operator Framework for Infinite-Dimensional Functional Nonlinear_images/imageFile21.png)

![image 22](Mou et al._2026_Neural-POD A Plug-and-Play Neural Operator Framework for Infinite-Dimensional Functional Nonlinear_images/imageFile22.png)

![image 23](Mou et al._2026_Neural-POD A Plug-and-Play Neural Operator Framework for Infinite-Dimensional Functional Nonlinear_images/imageFile23.png)

- (b) L2 norm of the residuals for L1- and L2-optimal Neural-POD reconstructions.

![image 24](Mou et al._2026_Neural-POD A Plug-and-Play Neural Operator Framework for Infinite-Dimensional Functional Nonlinear_images/imageFile24.png)

![image 25](Mou et al._2026_Neural-POD A Plug-and-Play Neural Operator Framework for Infinite-Dimensional Functional Nonlinear_images/imageFile25.png)

![image 26](Mou et al._2026_Neural-POD A Plug-and-Play Neural Operator Framework for Infinite-Dimensional Functional Nonlinear_images/imageFile26.png)

- (c) L1 norm of the residuals for L1- and L2-optimal Neural-POD reconstructions.
- (d) In-distribution results of the first three POD modes: comparison between traditional POD with extra snapshots and Neural-POD for an unseen viscosity value ν.

![image 27](Mou et al._2026_Neural-POD A Plug-and-Play Neural Operator Framework for Infinite-Dimensional Functional Nonlinear_images/imageFile27.png)

- (e) Out-of-distribution results of the first three POD modes: comparison between traditional POD with extra snapshots and Neural-POD for an unseen viscosity value ν.


![image 28](Mou et al._2026_Neural-POD A Plug-and-Play Neural Operator Framework for Infinite-Dimensional Functional Nonlinear_images/imageFile28.png)

Fig. 4: Summary of Burgers Neural-POD results: (a) training residual decay versus mode index for L2 and L1 losses; (b–c) reconstruction residuals under L2 and L1 metrics across representative viscosities; (d–e) in-distribution and out-of-distribution comparisons of POD (with extra snapshots) and Neural-POD for an unseen viscosity ν.

Figures 4b–4c compares the L1 and L2 norms of the reconstruction residuals obtained from Neural-POD models trained with L1- and L2-based loss functions across different viscosity values. Panels 4b and 4c correspond to the L2 and L1 residual norms, respectively, evaluated for three representative cases of ν = 0.01, ν = 0.03, and ν = 0.05. In panel 4b, the L2-optimal Neural-POD produces smooth and globally accurate reconstructions, with residuals remaining low throughout the spatial domain, particularly for higher viscosity values where the flow is predominantly diffusive. Panel 4c presents the corresponding L1 residual norms for both the L1- and L2-trained models. The L1-optimal Neural-POD exhibits improved accuracy in certain cases, particularly for specific reduced dimensions r (r = 1 and r = 3) where it better captures localized steep gradients and nonlinear features. Because the L1 norm penalizes large deviations less severely, it allows for sharper reconstructions in regions of strong nonlinearity, while the L2 formulation maintains smoother but more globally averaged behavior. Overall, the comparison indicates that the relative performance of the two loss formulations depends on both the viscosity parameter and the dimension r.

###### Neural-POD for in-distribution and out-of-distribution viscosity values

In the following experiments, the Neural-POD model is trained under the same numerical setting as in Figure 3a, using snapshot data generated at viscosity values ν sampled within the interval [0.005,,0.01]. This interval defines the training parameter domain for Neural-POD basis learning. Figures 4d–4e show both the in-distribution and outof-distribution performance of the Neural-POD framework. Here, in-distribution refers to evaluating the learned Neural-POD model at viscosity values ν within the parameter interval used for training, while out-of-distribution refers to evaluating the model at ν values outside that interval. More specifically, Figure 4d and Figure 4e compare the first three basis modes from traditional POD with those produced by Neural-POD trained using the L2 loss. Because traditional POD constructs modes only at the discrete viscosity levels contained in the snapshot data, it cannot directly produce basis functions for intermediate or out-of-range parameter values. Neural-POD, on the other hand, learns a continuous mapping from ν to the modal space, allowing it to generate basis functions for both unseen in-distribution and out-of-distribution parameter regimes. Notably, even for the fully unseen parameter value ν = 4 × 10−3 (see Figure 4e), which lies outside the training interval [0.005,,0.01] and represents a 20% out-of-distribution shift below its lower bound, Neural-POD still generates modes that remain consistent with the corresponding POD modes that confirms its generalization capability.

#### Neural-POD for Navier-Stokes equations

We also consider the Navier-Stokes equations (NSE) [20, 26, 27]:

∂u ∂t − Re−1∆u + u · ∇u + ∇p = 0, (6)

∇ · u = 0, (7)

where u is the velocity, p the pressure, and Re the Reynolds number. The computational domain is a 2.2 × 0.41 rectangular channel with a radius = 0.05 cylinder, centered at (0.2,0.2), see Figures 5a–5b. We prescribe no-slip boundary conditions on the walls and cylinder, and the following inflow and outflow profiles:

- u1(0,y,t) = u1(2.2,y,t) =

6 0.412

y(0.41 − y), (8)

- u2(0,y,t) = u2(2.2,y,t) = 0, (9)


where u = ⟨u1,u2⟩.

The dataset used is generated by a high-fidelity finite element simulation of the unsteady Navier–Stokes equations at Re = 50. The spatial discretization employs a Taylor–Hood element pair (quadratic velocity, linear pressure) on an unstructured triangular mesh that provides sufficient resolution of the boundary layers and wake structures. The resulting finite element discretization yields approximately 1.2 × 104 velocity degrees of freedom (DOFs). Temporal integration is performed using a secondorder backward differentiation formula (BDF2). A total of 1000 velocity snapshots are recorded uniformly in time over the interval [10,20]. To make a consistent comparison, these snapshots are used to generate both the Proper Orthogonal Decomposition (POD) basis and to train the Neural–POD. Figures 5c–5d illustrates the first two spatial modes identified by the classical POD and Neural–POD. The close agreement between the two confirms the consistency of Neural–POD with the traditional POD framework.

#### Neural-POD in Reduced Order Modeling

In this section, we investigate the Neural-POD applied in Galerkin projection reduced order models (Galerkin ROM) in the numerical simulation of the one-dimensional viscous Burgers equation in equations (15) with the initial condition:

u(x,0) = u0(x) =

1, x ∈ (0,1/2], 0, x ∈ (1/2,1],

(10)

and ν = 10−3. This test problem has been used in [20, 28]. Snapshot Generation

The truth data are obtained using a linear finite element spatial discretization with mesh size h = 1/512 and a Crank–Nicolson time discretization with timestep size ∆t = 10−4. A total of 101 snapshots are collected at equally spaced time instances over the interval t ∈ [0,1] for constructing the POD and Neural-POD modes. More details are provided in Supplementary Section A.2. and Supplementary Data, Fig. A3.

2.2

| | | |
|---|---|---|
| |0.2 0.05<br><br>| |
| | | |


0.41

0.2

(a) Geometry of two-dimensional flow past the cylinder.

![image 29](Mou et al._2026_Neural-POD A Plug-and-Play Neural Operator Framework for Infinite-Dimensional Functional Nonlinear_images/imageFile29.png)

(b) Sampling points for the flow past the cylinder test problem.

![image 30](Mou et al._2026_Neural-POD A Plug-and-Play Neural Operator Framework for Infinite-Dimensional Functional Nonlinear_images/imageFile30.png)

(c) First two POD modes.

![image 31](Mou et al._2026_Neural-POD A Plug-and-Play Neural Operator Framework for Infinite-Dimensional Functional Nonlinear_images/imageFile31.png)

(d) First two Neural-POD modes.

Fig. 5: (a–b) Geometry and sampling points of the two-dimensional flow past a cylinder problem. (c–d) First two modes of POD and Neural-POD for two-dimensional flow past the cylinder with Re = 50.

###### Discussion of Numerical Results

Figure 3 compares the modes from classical POD and Neural–POD under different optimality criteria for Burgers equation with initial condition in (15) . The L2-optimal Neural–POD modes closely resemble the classical POD modes, showing that the neural representation preserves the same energy-optimization structure when trained in the same norm. In contrast, the L1-optimal Neural–POD produces sharper and more localized modes, emphasizing regions with strong gradients or discontinuities. This indicates that while the L2-trained Neural–POD recovers the traditional POD basis, the L1 formulation provides a flexible alternative for capturing nonlinear and nonsmooth dynamics. We consider two projection-based ROMs: the standard POD-ROM, which uses classical POD modes, and the Neural-POD-ROM, which employs modes learned via Neural-POD.

Table 1: L2 errors of POD–ROM and Neural–POD–ROM for the one-dimensional Burgers equation. At ν = 0.002, training snapshots are available for both models. At ν = 0.005, Neural–POD–ROM is evaluated in a prediction setting without training snapshots.

ν Model r = 2 r = 4 r = 6 0.002

POD–ROM 2.10e-01 1.66e-01 1.76e-01 Neural–POD–ROM (L2) 2.11e-01 1.67e-01 1.77e-01

###### POD–ROM No in distribution ability Neural–POD–ROM (L2) 9.61e-02 1.18e-01 1.35e-01

0.0025

POD–ROM No out of distribution ability Neural–POD–ROM (L2) 1.91e-01 1.21e-01 8.46e-02

0.005

Table 1 compares the L2 reconstruction errors of the standard POD–ROM and the proposed Neural–POD–ROM for the one-dimensional Burgers equation for viscosity values ν = 0.002 with different ROM dimensions r. At this parameter value, where training snapshots are available, both POD-ROM and Neural-POD-ROM achieve comparable accuracy for all different ROM dimensions. This confirms that, when training data are available at the given parameter value, the neural representation of basis functions matches the ability of classical POD to capture the dominant coherent structures. Table 1 presents ROM results at the unseen viscosity value ν = 0.005, which is not included in the training snapshots. In this regime, the classical POD–ROM cannot be constructed due to the absence of simulation snapshots at the target parameter value. In contrast, the Neural–POD–ROM can still be formulated using pretrained Neural–POD predictions even when the PDE parameter, i.e., the viscosity ν, is not included in the training set, and it continues to produce accurate reconstructions for all ROM dimensions.

#### Neural-POD in Deep Operator Learning

We consider the one-dimensional Burgers’ equations (1)–(3) following the same configuration described in Section 4. The dataset is adopted from [7], where the initial conditions are sampled from a Gaussian random field characterized by a Riesz kernel, µ = R(0,,625(−∆ + 25I)−2), with µ denoting the probability measure over the function space and ∆ and I representing the Laplacian and identity operators, respectively. Both input and output fields are discretized on a uniform grid with 128 spatial points.

In contrast to the method proposed in [7], which employs snapshots at t = 1 to construct the POD basis, our Neural-POD framework learns the basis functions directly from the temporal evolution of the Burgers’ equation across multiple time steps. We employ four latent modes in the reduced representation and train the model on 128-point spatial grids, while evaluating its reconstruction and generalization performance on coarser 64-point grids. This setup enables assessment of both the model’s spatial resolution robustness and its capacity to generalize across varying discretizations and viscosity parameters. This is further confirmed by Extended Data Tables 1. At the coarse resolution (N = 64), the Neural-POD–DeepONet achieves lower testing errors than the traditional POD–DeepONet, with roughly a 20% reduction in both L1 and L2 metrics. These results, consistent with Extended Data Figure 2b, show that the Neural-POD framework offers clear benefits under limited resolution, while recovering classical POD behavior as the discretization becomes sufficiently fine. At coarse resolution (N = 32), the Neural-POD–DeepONet exhibits noticeably improved reconstructions over the traditional POD–DeepONet, capturing sharper transitions. This improvement can be attributed to the adaptive and data-driven nature of the Neural-POD basis, which enhances the representation of localized features under limited spatial resolution. As the training resolution increases to N = 64, the difference between the two approaches becomes less pronounced, though the Neural-POD still achieves slightly lower reconstruction errors. For the finest resolution (N = 128), both Neural-POD–DeepONet and POD–DeepONet produce nearly similar results, indicating that the advantage of the learned basis diminishes as the resolution becomes sufficiently high to resolve the dominant flow structures. In this regime, the L1-based Neural-POD performs marginally worse than the L2 variant due to its less stringent global smoothness constraint. Overall, the results suggest that the Neural-POD framework provides clear advantages at coarse or moderately resolved training settings, where it compensates for the loss of spatial detail through adaptive modal learning, while converging to the classical POD behavior at higher resolutions. Extended Data Figure 4 shows the comparison between the proposed Neural-POD–DeepONet and the traditional POD–DeepONet with different spatial training resolutions, N = 32, N = 64, and N = 128. Each model is evaluated on unseen initial conditions of the Burgers’ equation to verify its ability to generalize for both data realizations and discretization levels.

### Discusssions

In this work, we introduced the Neural Proper Orthogonal Decomposition (NeuralPOD), a neural operator approach that generalizes the classical POD through nonlinear basis learning with neural networks. Unlike traditional linear POD, which relies on a fixed linear subspace derived from singular value decomposition, Neural-POD constructs orthogonal basis functions via iterative residual minimization using trainable neural representations. This neural formulation enables basis optimization under arbitrary norms, such as L1, L2, and naturally accommodates nonlinear and multiscale dynamics captures nonlinear spatiotemporal features. Numerical tests are performed on benchmark problems, including the one-dimensional Burgers’ equation and the two-dimensional Navier–Stokes equations, which shows the robustness of the proposed framework. We also show that Neural-POD can be effectively used in projection-based reduced order models (ROMs), and deep operator network (DeepONet) with numerical tests. The pretrained and plug-and-play properties of Neural-POD also creates a promising pathway toward an open-source, community-driven database, in which shared Neural-POD basis libraries may further facilitate reproducibility and further expand the applicability in communities of ROM and operator learning.

Future research will focus on the following different directions: First, we will extend the Neural-POD framework to more challenging and high-dimensional scientific problems such the turbulent three-dimensional Navier–Stokes or Boussinesq equations, where nonlinear modal interactions and multi-scale energy cascades provide a demanding test [29–31]. Another promising direction is the integration of Neural-POD with physics-informed neural networks (PINNs) to enforce physical constraints during basis construction, thereby improving interpretability and extrapolation for physics-guided model reduction [32, 33]. Furthermore, coupling Neural-POD with data assimilation techniques such as Ensemble Kalman Filters (EnKF) or variational methods may enable real-time state estimation and model correction in dynamical systems [34, 35]. Also, in digital-twin applications, Neural-POD can be employed to build efficient and adaptive surrogate models that enable real-time monitoring, prediction, and control of complex physical systems [36, 37]. Lastly, we plan to extend the framework to parameterize and learn geometrical variations that enables the community to contribute new mesh configurations and expand the applicability of Neural-POD to complex domains with heterogeneous geometries [38].

### Methods

#### Classic Proper Orthogonal Decomposition (POD)

The classical Proper Orthogonal Decomposition (POD) is a widely used technique for extracting low-dimensional structures from high-dimensional spatiotemporal data [39, 40]. It is especially prominent in fluid dynamics, model reduction, and system identification due to its mathematical rigor, computational efficiency, and optimality properties in the L2 norm.

Given a set of M snapshots u(x,tj)j = 1M collected from a high-dimensional system, POD seeks a set of orthonormal basis functions ϕi(x)i = 1r that best approximate the snapshots in a least-squares sense. Formally, POD solves the following minimization problem:

M

1

min

M

{ϕi}ri=1

j=1

u(x,tj) −

r

⟨u(·,tj),ϕi⟩ϕi(x)

i=1

2

, (11)

L2

subject to the orthonormality constraint (ϕi,ϕj) = δij. The solution is obtained via singular value decomposition (SVD) of the snapshot matrix, and the resulting modes ϕi span an r-dimensional subspace that captures the most energetic components of the dataset [41–43]. POD guarantees optimality in the L2 sense: for any given rank r, the POD basis minimizes the projection error among all r-dimensional linear subspaces. This makes it a powerful tool for linear dimensionality reduction and the foundation for many reduced order models (ROMs), where the governing equations are projected onto the POD subspace using Galerkin or Petrov–Galerkin projection [44–47].

Despite its strengths, classical POD has several limitations. Because its basis is strictly linear, it often struggles to represent complex nonlinear features, sharp gradients, or discontinuities [19, 48]. Furthermore, the POD basis is highly dependent on the resolution and parameter regime of the snapshot data, limiting its generalizability [49, 50]. These limitations (see left panel of Figure 1a) motivate the development of more flexible, data-driven alternatives, such as the N eural-POD framework introduced in this work (see right panel of Figure 1a).

#### Neural-POD Framework

The Neural Proper Orthogonal Decomposition (Neural-POD) in this work provides a data-driven framework for constructing low-dimensional representations of highdimensional spatiotemporal data. Unlike traditional POD methods that employ linear decompositions via singular value decomposition (SVD), Neural-POD utilizes neural networks to learn flexible spatial and temporal basis functions that are capable of capturing nonlinear structures in the data. Algorithm 1 provides a sketch of the NeuralPOD.

The algorithm starts with the input of a dataset Du = {Du(i)}Ni=1, where each snapshot Du(i) consists of a time point t(i) and a collection of M spatial-temporal samples {(x(i,j),u(i,j))}Mj=1. A small tolerance parameter Tol > 0 is also provided to determine the desired approximation accuracy. The objective is to iteratively decompose the data into a sum of separable spatiotemporal modes parameterized by neural networks until the residual error falls below the specified tolerance. The process begins by initializing the index p = 0 and training a neural network Φ0(x;θ0) that minimizes the mean L2 error between neural network output and the provided data u(x,t), sampled over the entire dataset. This first Neural-POD serves as the initial approximation to the solution, often capturing the dominant spatial pattern. The residual r(x,t) is then computed as the difference between the original data and the initial approximation. If the residual error, measured in the L2 sense over all (x,t) pairs, is within the tolerance,

the algorithm proceeds to iteratively add new modes. In each iteration, p is incrementally increased, i.e., p → p + 1, and two neural networks Φp(x;θp) and Ψp(t;βp) are randomly initialized. These networks are trained jointly to approximate the residual r(x,t) by the product Φp(x;θp)Ψp(t;βp). After training, the residual is updated by subtracting the new mode from it. Upon completion, the algorithm returns the number of modes P, the initial approximation Φ0(x;θ0), and the set of learned spatial and temporal basis functions {Φp(x;θp),Ψp(t;βp)}Pp=1. This decomposition provides a compact, interpretable, and expressive representation of the original system, which can be further used for reduced order modeling.

Beyond being a standalone data-driven method, Neural-POD can also be interpreted as a bridge between classical projection-based reduced order modeling (ROM) and modern operator learning frameworks. As illustrated in Figure 1b, the learned neural representations of POD basis functions can be directly used in Galerkin projection-based ROMs, while simultaneously functioning as pretrained, interpretable branch networks within DeepONet architectures.

Algorithm 1 Neural Proper Orthogonal Decomposition (Neural-POD)

- 1: Input:

Du = Du(i)

N i=1

, Du(i) = t(i), x(i,j), u(i,j) Mj=1 // N snapshots of u(x,t)

0 < Tol ≪ 1 // small tolerance for target accuracy

- 2: Output:

P, Φ0(·;θ0), {Φp(·;θp), Ψp(·;βp)}Pp=1 // a set of 2P + 1 parameterized basis functions

- 3: p ← 0
- 4: θ0 ← arg min θ0

(x,t)∼Du

u(x,t) − Φ0 x;θ0 22

- 5: r(x,t) ← u(x,t) − Φ0 x;θ0
- 6: while x,t

r2(x,t) ≥ Tol do

- 7: p ← p + 1
- 8: Randomly initialize new neural networks Φp x;θp , Ψp t;βp
- 9: θp, βp ← arg min θp,βp

(x,t)∼Du

r(x,t) − Φp x;θp Ψp t;βp

2 2

- 10: r(x,t) ← r(x,t) − Φp x;θp Ψp t;βp
- 11: end while


Architecture

The proposed Neural-POD architecture comprises two distinct sub-networks, designated as the parameter network and the basis network, which are integrated into a composite framework termed Neural-POD. This design strategically decouples the

parameter-dependent representation from the basis function expansion, thereby facilitating a flexible approach to modeling complex datasets. Within the composite architecture, the Neural-POD network processes inputs by independently computing the outputs of the parameter and basis sub-networks. These outputs are then combined via element-wise multiplication, and the resulting product is summed over the appropriate dimensions to yield a single scalar output for each sample.

###### Loss Functions

In the Neural-POD framework, the basis network is designed to generate a set of basis functions analogous to those used in finite element methods (FEM). These basis functions are assumed to satisfy the following:

- 1. Optimality: They provide the optimal representation for the data with a given norm, e.g., L2 optimality.
- 2. Orthogonality: They are mutually orthogonal.
- 3. Boundary conditions: They satisfy the prescribed boundary conditions of the original PDE systems.


The optimality, normalization and boundary conditions can be enforced by involving them into the loss functions.

Optimality: Ldata =

N

Boundary conditions: Lbc =

i=1

N

∥Φ(xi)Ψ(ti) − ui∥S , (12)

i=1

2

N

∂Φ(xbci ) ∂x −

∂ubci ∂x

Φ(xbci ) − ubci 2 +

(13)

i=1

To ensure a balanced optimization, reciprocal weights are computed from the initial loss contributions of the data fidelity and basis regularization terms. Consequently, the overall loss function employed during training is expressed as a weighted sum:

L = wdata · Ldata + wbc · Lbc, (14)

where wdata, wbasis, and wbc are the weights assigned to the data loss, basis regularization, and any additional boundary condition loss Lbc, respectively. This balanced loss formulation promotes both an accurate data fit and a well-scaled basis function. where wdata, wbasis, and wbc are the weights assigned to the data loss, basis regularization, and any additional boundary condition loss Lbc, respectively. These loss functions guarantee both an optimal data representation and a normalized basis function.

In Algorithm 1, the temporal variation of the data is expressed as a neural network; however, training two neural network at a time is computationally expensive. One may consider to choose one of the neural network ψk as a trainable function.

#### Neural-POD in Galerkin Projection Based Reduced Order Models

We first introduce the Neural-POD framework in the context of Galerkin projection reduced-order models (Galerkin ROMs or POD-ROMs). Although the methodology is applicable to general POD-based ROM constructions for a broad class of parameterized PDEs, we use the one-dimensional viscous Burgers equation as a simple and illustrative example. Specifically, we consider the Burgers equation posed on a spatial domain Ω ⊂ R over a finite time interval [0,T]. The solution is denoted by u = u(x,t) for (x,t) ∈ Ω × [0,T].The governing equation is equipped with Dirichlet boundary conditions and a prescribed initial condition:

 

ut − νuxx + uux = 0, (x,t) ∈ Ω × (0,T], u(x,t) = 0, (x,t) ∈ ∂Ω × (0,T], u(x,0) = u0(x), x ∈ Ω.

(15)



###### Traditional Projection-ROM

To construct a ROM, we approximate the solution u(x,t) by a linear combination of r orthonormal basis functions {ϕi(x)}ri=1 that can be obtained either from POD or Neural-POD:

r

ur(x,t) =

ai(t)ϕi(x), (16)

i=1

where ai(t) are the time-dependent basis coefficients. Substituting ur(x,t) into the Burgers’ equation (15) and applying Galerkin projection, we obtain the following:

∂2ur ∂x2

∂ur ∂t

∂ur ∂x − ν

+ ur

, ϕk = 0, for k = 1,...,r, (17)

where (·,·) denotes the standard L2 inner product. This yields the following dynamic system:

r

r

r

d2ϕi dx2

dϕj dx

a˙k(t) = −

,ϕk , k = 1,...,r.

ai(t)aj(t) ϕi

,ϕk + ν

ai(t)

i=1

j=1

i=1

(18) where

Cijk = ϕi

Dik =

∂2ϕi ∂x2

dϕj dx

,ϕk , (19)

,ϕk . (20)

With these definitions, equation (18) becomes:

r

a˙k(t) = −

i=1

r

r

ai(t)aj(t)Cijk + ν

j=1

i=1

ai(t)Dik, k = 1,...,r. (21)

###### Neural-POD-ROM

In the Neural-POD-ROM framework, the ROM basis {ϕi(x,ν)}ri=1 is obtained from a pretrained Neural-POD model evaluated at a given PDE parameter setting—such as the viscosity ν in the Burgers equation—and a prescribed set of spatial grid points {xj}Nj=1, which may differ from those used during training, in contrast to classical snapshot-based POD, whose basis functions are fixed by the training snapshots and are therefore restricted to the viscosity and spatial resolution represented in the training data.

Once the Neural-POD modes are learned and fixed, the ROM solution can be expressed in the same form,

ur(x,t;ν) =

r

ai(t)ϕi(x,ν), (22)

i=1

and the governing equations are derived by substituting ur into the Burgers’ equation and applying Galerkin projection onto the Neural-POD basis. This results in the same reduced dynamical system as in the traditional POD-ROM,

r

a˙k(t) = −

i=1

r

ai(t)aj(t)Cijk + ν

j=1

r

ai(t)Dik, k = 1,...,r, (23)

i=1

where the tensors Cijk and Dik are now computed using the Neural-POD modes. The projection-based ROM using POD and Neural-POD is specifically illustrated in Figure 2a.

Remark 1 A fundamental difference between Neural-POD-ROM and classical POD-ROM lies in the flexibility of the reduced basis: Neural-POD-ROM allows evaluation at new viscosity values and spatial resolutions, while classical POD-ROM remains tied to the parameter and grid of the training snapshots.

#### Neural-POD in Deep Operator Networks

Operator learning seeks to approximate mappings between infinite-dimensional function spaces and has become an effective framework for modeling PDE-governed systems. Given an input function v ∈ V (e.g., forcing terms or initial conditions) and an output function u ∈ U (e.g., the PDE solution), the objective is to learn an operator

G : V → U, u = G(v), (24)

from a dataset of paired input–output functions. Deep Operator Network (DeepONet) [21] is a representative neural operator architecture that realizes this mapping using a branch–trunk decomposition and has demonstrated strong performance in a variety of applications [7, 25].

In vanilla DeepONet, the branch network encodes a discretized representation of the input function v, while the trunk network takes the output coordinates ξ ∈ D′ as input. The operator output is expressed as

G(v)(ξ) =

p

bk(v)tk(ξ) + b0, (25)

k=1

where {bk(v)} and {tk(ξ)} denote the outputs of the branch and trunk networks, respectively. In this formulation, the trunk network implicitly learns a basis for the output function space directly from data.

To improve interpretability and efficiency, POD–DeepONet [7] replaces the learned trunk basis with pre-obtained POD modes from the training data. As a result, after subtracting the mean field, ϕ0(ξ), the output operator is represented as

G(v)(ξ) =

p

bk(v)ϕk(ξ) + ϕ0(ξ), (26)

k=1

where {ϕk}pk=1 are fixed POD basis functions and the coefficients bk(v) are learned by the branch network.

Following this framework, Neural-POD is applied within DeepONet by using pretrained Neural-POD modes in place of classical snapshot-based POD modes to construct the trunk representation. In this case, the operator output is expressed as

G(v)(ξ;ν,X) =

p

bk(v)ϕk(ξ;ν,X) + ϕ0(ξ;ν,X), (27)

k=1

where ϕk(·;ν,X) denote the pretrained Neural-POD modes evaluated at viscosity ν and spatial grid X = {xi}Ni=1, and ϕ0 is the corresponding mean field. The branch network outputs bk(v) represent the modal coefficients associated with these NeuralPOD basis functions. The Neural-POD-DeepONet framework is illustrated in Figure 2b.

### Acknowledgment

We would like to thank the support of National Science Foundation (DMS-2533878, DMS-2053746, DMS-2134209, ECCS-2328241, CBET-2347401 and OAC-2311848), and U.S. Department of Energy (DOE) Office of Science Advanced Scientific Computing Research program DE-SC0023161, the SciDAC LEADS Institute, and DOE–Fusion Energy Science, under grant number: DE-SC0024583.

### Data availability

Data used in this study are available at https://github.com/chhmou/Neural-POD . The full dataset is available upon reasonable request to the authors of the associated paper.

### Code availability

The code used in this study, including scripts for data analysis in MATLAB (R2025b) and Python (v3.10), is available via GitHub at https://github.com/chhmou/ Neural-POD. Python packages used for analysis include PyTorch, pandas, numpy, scikit-learn, matplotlib and statsmodels. Code annotations were generated using ChatGPT 4o (gpt-4o-2024-08-06).

### References

- [1] Pearson, K.: Liii. on lines and planes of closest fit to systems of points in space. The London, Edinburgh, and Dublin philosophical magazine and journal of science 2(11), 559–572 (1901)
- [2] Hotelling, H.: Analysis of a complex of statistical variables into principal components. Journal of educational psychology 24(6), 417 (1933)
- [3] Lumley, J.: Similarity and the turbulent energy spectrum. The physics of fluids 10(4), 855–858 (1967)
- [4] Benner, P., Gugercin, S., Willcox, K.: A survey of projection-based model reduction methods for parametric dynamical systems. SIAM Rev. 57(4), 483–531

(2015)

- [5] Lucia, D.J., Beran, P.S., Silva, W.A.: Reduced-order modeling: new approaches for computational physics. Progress in aerospace sciences 40(1-2), 51–117 (2004)
- [6] Yu, J., Yan, C., Guo, M.: Non-intrusive reduced-order modeling for fluid problems: A brief review. Proceedings of the Institution of Mechanical Engineers, Part G: Journal of Aerospace Engineering 233(16), 5896–5912 (2019)
- [7] Lu, L., Meng, X., Cai, S., Mao, Z., Goswami, S., Zhang, Z., Karniadakis, G.E.: A comprehensive and fair comparison of two neural operators (with practical extensions) based on fair data. Computer Methods in Applied Mechanics and Engineering 393, 114778 (2022)
- [8] Holmes, P., Lumley, J.L., Berkooz, G.: Turbulence, Coherent Structures, Dynamical Systems and Symmetry. Cambridge, ??? (1996)
- [9] Taira, K., Brunton, S.L., Dawson, S., Rowley, C.W., Colonius, T., McKeon, B.J., Schmidt, O.T., Gordeyev, S., Theofilis, V., Ukeiley, L.S.: Modal analysis of fluid


- flows: An overview. AIAA J., 4013–4041 (2017)
- [10] Carlberg, K., Bou-Mosleh, C., Farhat, C.: Efficient non-linear model reduction via a least-squares Petrov–Galerkin projection and compressive tensor approximations. Int. J. Num. Meth. Eng. 86(2), 155–181 (2011)
- [11] Quarteroni, A., Manzoni, A., Negri, F.: Reduced Basis Methods for Partial Differential Equations: An Introduction vol. 92. Springer, ??? (2015)
- [12] Rowley, C.W., Colonius, T., Murray, R.M.: Model reduction for compressible flows using POD and Galerkin projection. Phys. D 189(1), 115–129 (2004)
- [13] Shadden, S.C.: Lagrangian coherent structures. Transport and Mixing in Laminar Flows: From Microfluidics to Oceanic Currents, 59–89 (2011)
- [14] Yosinski, J., Clune, J., Bengio, Y., Lipson, H.: How transferable are features in deep neural networks? Advances in neural information processing systems 27

(2014)

- [15] Deng, W., Pan, J., Zhou, T., Kong, D., Flores, A., Lin, G.: Deeplight: Deep lightweight feature interactions for accelerating ctr predictions in ad serving. In: Proceedings of the 14th ACM International Conference on Web Search and Data Mining, pp. 922–930 (2021)
- [16] Mendez, M.A., Balabane, M., Buchlin, J.-M.: Multi-scale proper orthogonal decomposition of complex fluid flows. Journal of Fluid Mechanics 870, 988–1036

(2019)

- [17] Zahr, M.J., Farhat, C.: Progressive construction of a parametric reduced-order model for pde-constrained optimization. International Journal for Numerical Methods in Engineering 102(5), 1111–1135 (2015)
- [18] Kunisch, K., Volkwein, S.: Galerkin proper orthogonal decomposition methods for parabolic problems. Numer. Math. 90(1), 117–148 (2001)
- [19] Iliescu, T., Wang, Z.: Are the snapshot difference quotients needed in the proper orthogonal decomposition? SIAM J. Sci. Comput. 36(3), 1221–1250 (2014)
- [20] Mou, C., Koc, B., San, O., Rebholz, L.G., Iliescu, T.: Data-driven variational multiscale reduced order models. Computer Methods in Applied Mechanics and Engineering 373, 113470 (2021)
- [21] Lu, L., Jin, P., Karniadakis, G.E.: Deeponet: Learning nonlinear operators for identifying differential equations based on the universal approximation theorem of operators. arXiv preprint arXiv:1910.03193 (2019)
- [22] Winovich, N., Daneker, M., Lu, L., Lin, G.: Active operator learning with predictive uncertainty quantification for partial differential equations. arXiv preprint


- arXiv:2503.03178 (2025)
- [23] Lu, B., Mou, C., Lin, G.: An evolutionary multi-objective optimization for replicaexchange-based physics-informed operator learning network. arXiv preprint arXiv:2509.00663 (2025)
- [24] Li, Z., Kovachki, N., Azizzadenesheli, K., Liu, B., Bhattacharya, K., Stuart, A., Anandkumar, A.: Fourier neural operator for parametric partial differential equations. arXiv preprint arXiv:2010.08895 (2020)
- [25] Wang, S., Wang, H., Perdikaris, P.: Learning the solution operator of parametric partial differential equations with physics-informed deeponets. Science advances 7(40), 8605 (2021)
- [26] Layton, W.J.: A mathematical introduction to large eddy simulation. In: Deconinck, H. (ed.) Computational Fluid Dynamics-Multiscale Methods. Von Karman Institute for Fluid Dynamics, Rhode-Saint-Gen`ese, Belgium
- [27] Koc, B., Mou, C., Liu, H., Wang, Z., Rozza, G., Iliescu, T.: Verifiability of the data-driven variational multiscale reduced order model. Journal of Scientific Computing 93(2), 54 (2022)
- [28] Koc, B., Chacon Rebollo, T., Rubino, S.: Uniform bounds with difference quotients for proper orthogonal decomposition reduced order models of the burgers equation. Journal of Scientific Computing 95(2), 43 (2023)
- [29] Mou, C., Merzari, E., San, O., Iliescu, T.: An energy-based lengthscale for reduced order models of turbulent flows. Nuclear Engineering and Design 412, 112454

(2023)

- [30] Bright, I., Lin, G., Kutz, J.N.: Compressive sensing based machine learning strategy for characterizing the flow around a cylinder with limited pressure measurements. Physics of Fluids 25(12) (2013)
- [31] Lin, G., Tartakovsky, A.M.: An efficient, high-order probabilistic collocation method on sparse grids for three-dimensional flow and solute transport in randomly heterogeneous porous media. Advances in Water Resources 32(5), 712–722

(2009)

- [32] Cai, S., Mao, Z., Wang, Z., Yin, M., Karniadakis, G.E.: Physics-informed neural networks (pinns) for fluid mechanics: A review. Acta Mechanica Sinica 37(12), 1727–1738 (2021)
- [33] Lu, B., Mou, C., Lin, G.: Mopinnenkf: Iterative model inference using genericpinn-based ensemble kalman filter. arXiv preprint arXiv:2506.00731 (2025)
- [34] Popov, A.A., Mou, C., Sandu, A., Iliescu, T.: A multifidelity ensemble kalman


- filter with reduced order control variates. SIAM Journal on Scientific Computing 43(2), 1134–1162 (2021)
- [35] Bilionis, I., Zabaras, N., Konomi, B.A., Lin, G.: Multi-output separable gaussian process: Towards an efficient, fully bayesian paradigm for uncertainty quantification. Journal of Computational Physics 241, 212–239 (2013)
- [36] Xiu, D., Tartakovsky, D.M.: Computational framework for real-time digital twins. In: Thermopedia. Begel House Inc., ??? (2025)
- [37] Jones, D., Snider, C., Nassehi, A., Yon, J., Hicks, B.: Characterising the digital twin: A systematic literature review. CIRP journal of manufacturing science and technology 29, 36–52 (2020)
- [38] Shukla, K., Oommen, V., Peyvan, A., Penwarden, M., Plewacki, N., Bravo, L., Ghoshal, A., Kirby, R.M., Karniadakis, G.E.: Deep neural operators as accurate surrogates for shape optimization. Engineering Applications of Artificial Intelligence 129, 107615 (2024)
- [39] Berkooz, G., Holmes, P., Lumley, J.L.: The proper orthogonal decomposition in the analysis of turbulent flows. Annual review of fluid mechanics 25(1), 539–575

(1993)

- [40] Chatterjee, A.: An introduction to the proper orthogonal decomposition. Current science, 808–817 (2000)
- [41] Gubisch, M., Volkwein, S.: Proper orthogonal decomposition for linear-quadratic optimal control. Model reduction and approximation: theory and algorithms 15(1) (2017)
- [42] Kunisch, K., Volkwein, S.: Proper orthogonal decomposition for optimality systems. ESAIM: Math. Model. Numer. Anal. 42(1), 1–23 (2008)
- [43] Berkooz, G.: Observations on the proper orthogonal decomposition. Studies in Turbulence, 229–247 (1992)
- [44] Girfoglio, M., Quaini, A., Rozza, G.: A pod-galerkin reduced order model for a les filtering approach. Journal of Computational Physics 436, 110260 (2021)
- [45] Iliescu, T., Wang, Z.: Variational multiscale proper orthogonal decomposition: Convection-dominated convection-diffusion-reaction equations. Math. Comput. 82(283), 1357–1378 (2013)
- [46] Mou, C., Liu, H., Wells, D.R., Iliescu, T.: Data-driven correction reduced order models for the quasi-geostrophic equations: A numerical investigation. Int. J. Comput. Fluid Dyn., 1–13 (2020)
- [47] Tsai, P.-H., Fischer, P., Iliescu, T.: A time-relaxation reduced order model for the


- turbulent channel flow. Journal of Computational Physics 521, 113563 (2025)
- [48] Volkwein, S.: Proper orthogonal decomposition: Theory and reduced-order modelling. Lecture Notes, University of Konstanz (2013). http://www.math. uni-konstanz.de/numerik/personen/volkwein/teaching/POD-Book.pdf
- [49] Mifsud, M., MacManus, D.G., Shaw, S.: A variable-fidelity aerodynamic model using proper orthogonal decomposition. International Journal for Numerical Methods in Fluids 82(10), 646–663 (2016)
- [50] Roderick, O., Anitescu, M., Peet, Y.: Proper orthogonal decompositions in multifidelity uncertainty quantification of complex simulation models. International Journal of Computer Mathematics 91(4), 748–769 (2014)


### Extended Data Figures and Tables

![image 32](Mou et al._2026_Neural-POD A Plug-and-Play Neural Operator Framework for Infinite-Dimensional Functional Nonlinear_images/imageFile32.png)

Extended Data Fig. 1: First three Neural-POD modes for different viscosity values

![image 33](Mou et al._2026_Neural-POD A Plug-and-Play Neural Operator Framework for Infinite-Dimensional Functional Nonlinear_images/imageFile33.png)

![image 34](Mou et al._2026_Neural-POD A Plug-and-Play Neural Operator Framework for Infinite-Dimensional Functional Nonlinear_images/imageFile34.png)

###### Extended Data Fig. 2: Reconstruction of spatiotemporal fields for the onedimensional Burgers’ equation at an unseen viscosity parameter using Neural-POD with different latent dimensions (2 and 4).

![image 35](Mou et al._2026_Neural-POD A Plug-and-Play Neural Operator Framework for Infinite-Dimensional Functional Nonlinear_images/imageFile35.png)

(a) POD results for the 1D Burgers equation.

![image 36](Mou et al._2026_Neural-POD A Plug-and-Play Neural Operator Framework for Infinite-Dimensional Functional Nonlinear_images/imageFile36.png)

- (b) Neural-POD results for the 1D Burgers equation (L2 optimality).

![image 37](Mou et al._2026_Neural-POD A Plug-and-Play Neural Operator Framework for Infinite-Dimensional Functional Nonlinear_images/imageFile37.png)

- (c) Neural-POD results for the 1D Burgers equation (L1 optimality).


Extended Data Fig. 3: Comparison of POD and Neural-POD on the 1D Burgers equation for different viscosity values: (a) classical POD , (b) Neural-POD trained with L2 loss, (c) Neural-POD trained with L1 loss.

Extended Data Table 1: L2 and L1 error comparison between Neural-PODDeepONet and POD-DeepONet models trained on 64 spatial points with 100,000 training iterations.

Metric Neural-POD-DeepONet POD-DeepONet

Training Loss 3.47 × 10−3 4.10 × 10−3 Testing L2 Error 3.40 × 10−3 4.37 × 10−3 Testing L1 Error 3.16 × 10−2 3.59 × 10−2

![image 38](Mou et al._2026_Neural-POD A Plug-and-Play Neural Operator Framework for Infinite-Dimensional Functional Nonlinear_images/imageFile38.png)

- (a) Training resolution N = 32

![image 39](Mou et al._2026_Neural-POD A Plug-and-Play Neural Operator Framework for Infinite-Dimensional Functional Nonlinear_images/imageFile39.png)

- (b) Training resolution N = 64

![image 40](Mou et al._2026_Neural-POD A Plug-and-Play Neural Operator Framework for Infinite-Dimensional Functional Nonlinear_images/imageFile40.png)

- (c) Training resolution N = 128


31

Extended Data Fig. 4: Resolution-independent Neural-POD in DeepONet: A comparison of L1 and L2 errors for Neural-POD-DeepOnet versus POD-DeepOnet for different initial conditions and training resolutions.

