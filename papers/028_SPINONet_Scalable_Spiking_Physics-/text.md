SPINONET: SCALABLE SPIKING PHYSICS-INFORMED NEURAL
OPERATOR FOR COMPUTATIONAL MECHANICS APPLICATIONS
A PREPRINT
Shailesh Garg
Department of Applied Mechanics
Indian Institute of Technology Delhi
Hauz Khas, New Delhi 110016, India.
shaileshgarg96@gmail.com
Luis Mandl
Institute of Structural Mechanics and Dynamics in Aerospace Engineering
Faculty of Aerospace Engineering and Geodesy
University of Stuttgart, Stuttgart, Germany.
Experimental Hepatobiliary Surgery Group
Department of Hepatobiliary Surgery and Visceral Transplantation
University of Leipzig Medical Center, Leipzig, Germany.
Department of Civil and Systems Engineering
Johns Hopkins University, Maryland 21218, USA.
luis.mandl@isd.uni-stuttgart.de
Somdatta Goswami
Department of Civil and Systems Engineering
Data Science and AI Institute
Johns Hopkins University, Maryland 21218, USA.
somdatta@jhu.edu
Souvik Chakraborty
Department of Applied Mechanics
Yardi School of Artificial Intelligence (YScAI)
Indian Institute of Technology Delhi
Hauz Khas, New Delhi 110016, India.
souvik@am.iitd.ac.in
March 24, 2026
ABSTRACT
Energy efficiency remains a critical challenge in deploying physics-informed operator learning mod-
els for computational mechanics and scientific computing, particularly in power-constrained settings
such as edge and embedded devices, where repeated operator evaluations in dense networks incur
substantial computational and energy costs. To address this challenge, we introduce the Separable
Physics-informed Neuroscience-inspired Operator Network (SPINONet), a neuroscience-inspired
framework that reduces redundant computation across repeated evaluations while remaining com-
patible with physics-informed training. SPINONet incorporates regression-friendly neuroscience-
inspired spiking neurons through an architecture-aware design that enables sparse, event-driven
computation, improving energy efficiency while preserving the continuous, coordinate-differentiable
pathways required for computing spatio-temporal derivatives. We evaluate SPINONet on a range of
partial differential equations representative of computational mechanics problems, with spatial, tem-
poral, and parametric dependencies in both time-dependent and steady-state settings, and demon-
strate predictive performance comparable to conventional physics-informed operator learning ap-
proaches despite the induced sparse communication. In addition, limited data supervision in a hy-
brid setup is shown to improve performance in challenging regimes where purely physics-informed
arXiv:2603.21674v1  [physics.comp-ph]  23 Mar 2026

A PREPRINT - MARCH 24, 2026
training may converge to spurious solutions. Finally, we provide an analytical discussion linking
architectural components and design choices of SPINONet to reductions in computational load and
energy consumption.
Keywords Variable Spiking Neurons · Physics-informed Operator Learning · Separable DeepONet · Spiking Neural
Networks · Energy-efficient Inference
1
Introduction
Physics-informed deep learning [1, 2, 3, 4]offers an effective framework in mechanical science, where observational
data are limited, but the governing physical laws are well understood. By embedding these laws into the learning
process, physics-informed deep learning models [1, 5, 6, 4] restrict the space of admissible solutions and enable
discretization-invariant surrogate modeling once training is complete, a desirable property in computational mechan-
ics workflows. Incorporating operator learning [7, 8, 9, 10] with physics-informed learning extends this paradigm by
learning mappings between function spaces rather than individual solution instances, enabling rapid evaluation of so-
lution fields for unseen but in-distribution inputs without re-training or re-solving the underlying PDE. This capability
is especially valuable in applications such as parametric PDE analysis [11, 12], uncertainty quantification [13, 14], and
digital twin modeling [15, 16] in computational mechanics, where the input function space must be queried repeatedly
across multiple evaluations.
Physics-informed operator-learning frameworks based on Deep Operator Networks (DeepONet) [17, 18, 19], Fourier
Neural Operators [20, 21], and Wavelet Neural Operators [22, 23] have demonstrated strong performance in learning
various PDEs Recent work has additionally focused on improving the scalability of these approaches for tackling high-
dimensional problems. Within this context, the separable physics-informed deep operator network [17] framework has
gained attention. The framework leverages the idea of solving PDEs with separation of variables, thereby exploiting
coordinate-wise factorization and enabling efficient residual computation via forward-mode automatic differentiation
to reduce the cost of evaluating the PDE residual. However, in its vanilla form, these architectures rely on continuously
active neurons, i.e., neurons are evaluated, and a full set of multiply-accumulate operations is executed at every forward
evaluation, irrespective of the effective information content of the input. This results in increased computational load
and hinders deployment under constrained computational or power budgets, as encountered in edge computing [24, 25]
or embedded [26, 27] environments.
To address this execution bottleneck in physics-informed learning, we focus on how information is represented and
propagated, rather than modifying the operator’s functional form or the physics-informed loss. Sparse, event-driven
neuron models [28, 29, 30, 31], inspired by biological computation, offer a principled mechanism to reduce redundant
communication by activating neurons only when informative signals are present. However, their discontinuous dy-
namics pose challenges for residual-based physics-informed training, where accurate spatial and temporal derivatives
are essential for enforcing physical constraints [32, 23].
Recent efforts have explored neuroscience-inspired physics-informed neural networks [33, 34, 35], demonstrating that
spiking or event-driven mechanisms can be incorporated into PINN-style frameworks. However, these approaches
operate at the level of solution networks and do not address neural operators, which learn mappings between func-
tion spaces and are critical for parametric PDEs and multi-query evaluation settings. The only prior work integrating
spiking dynamics with neural operators is the neuroscience-inspired WNO proposed in [23], built upon the WNO
backbone [9]. While it yields reasonably accurate result, its wavelet-based architecture differs structurally from
DeepONet-style operators, which offer additional flexibility. Separable DeepONet variants, in particular, can seam-
lessly handle high-dimensional problems. These considerations motivate the investigation of neuroscience-inspired
DeepONet architectures, especially separable variants, as a structurally principled direction for enabling sparse, event-
driven operator learning that remains fully compatible with residual-based physics-informed training and can scale to
high dimensional problems.
In this paper, we propose the Separable Physics-informed and Neuroscience-inspired Operator Network (SPINONet).
The central design principle of SPINONet is to resolve the apparent incompatibility between spiking neural dynamics
and physics-informed operator learning through architectural separation. In separable physics-informed deep operator
networks, physics-informed residuals require coordinate derivatives only through the coordinate-dependent compo-
nents (trunk), while the input-function encoding (branch) enters the operator algebraically and remains independent
of spatial and temporal differentiation. SPINONet leverages this structural decoupling to introduce spiking dynamics
exclusively within the input-function encoding pathway, while preserving continuous, fully differentiable coordinate
pathways required for physics-informed training. Realizing sparse, event-driven computation in this setting, how-
ever, necessitates a spiking neuron model compatible with regression tasks and continuous function approximation.
The class of such neuron models that can be trained natively and perform reliably in regression settings is limited,
2

A PREPRINT - MARCH 24, 2026
with primary candidates being the Variable Spiking Neuron (VSN) [36] and the Quadratic Integrate-and-Fire (QIF)
model [37]. While the proposed framework is compatible with either (and with future regression-friendly spiking
models), we adopt VSN [36], which supports graded, continuous-valued spikes and has demonstrated strong perfor-
mance in regression and operator-learning contexts [38, 39, 36]. The key contributions of this work can be summarized
as follows,
• Architectural separation enabling physics-informed spiking operator learning. We introduce SPINONet,
a separable physics-informed operator-learning framework that resolves the incompatibility between spiking
dynamics and physics-based differentiation through structural decoupling. By confining spiking computa-
tion to the input-function encoding pathway, where inputs enter algebraically, and preserving continuous
coordinate-dependent components for derivative evaluation, SPINONet enables sparse, event-driven compu-
tation without compromising operator expressivity or physics-informed training consistency. The coordinate-
wise factorization further eliminates explicit full-mesh evaluations, ensuring smoothly scaling computational
cost with increasing resolution.
• Accuracy retention with enhanced stability and scalability. Across a diverse suite of time-dependent
and steady-state PDEs, including high-dimensional spatio-temporal-parametric settings, SPINONet achieves
predictive accuracy comparable to dense physics-informed operator-learning baselines while substantially
reducing computational burden. Owing to its separable architecture, the framework scales smoothly with
increasing dimension without incurring full mesh-based evaluation costs. We further demonstrate that in-
corporating a small amount of supervised data effectively mitigates degenerate solutions encountered in
purely physics-informed regimes, improving stability and predictive fidelity without modifying the under-
lying physics-informed loss formulation.
• Analytical foundations for computational and energy efficiency. We present a hardware-agnostic analyt-
ical framework that rigorously links sparse spiking activity and separable trunk evaluation to reductions in
computational and energy cost. In addition, we formally analyze how forward-mode automatic differentiation
synergizes with the proposed architecture to yield further efficiency gains, providing theoretical grounding
for scalable operator learning.
The remainder of the paper is organized as follows.
Section 2 reviews physics-informed operator learning and
neuroscience-inspired computation. Section 3 introduces the SPINONet framework in detail. Section 4 presents
and discusses the numerical experiments. Section 5 concludes the paper and outlines directions for future work.
2
Problem Statement
We consider parametric partial differential equations (PDEs) on a spatial domain Ω⊂R ˆd and, for time-dependent
problems, a temporal domain T ⊂R,
N(u(x, t); λ) = 0,
(x, t) ∈Ω× T ,
NB(u(x, t); λ) = 0,
(x, t) ∈∂Ω× T ,
NI(u(x, t); λ) = 0,
(x, t) ∈Ω× {t0}.
(1)
where N denotes the governing differential operator, NB and NI encode boundary and initial conditions, and λ
collects physical parameters. For steady-state problems, T and NI are omitted. Many computational mechanics and
scientific computing applications require repeatedly solving such PDEs for varying inputs. This motivates learning
the solution operator G : U →Y that maps admissible input functions to solution fields. Physics-informed operator
learning seeks a parametric surrogate Gθ ≈G that generalizes to unseen inputs without re-solving the PDE. DeepONets
approximate nonlinear operators by expressing the solution at a location (x, t) as,
Gθ(u)(x, t) =
p
X
k=1
bk(u) ˜tk(x, t),
(2)
where the branch network, bk(·) encodes the input u and the trunk network, ˜tk(x, t) encodes the spatial and temporal
coordinates. In physics-informed DeepONet, the PDE is enforced via residual minimization, requiring spatial and
temporal derivatives of Gθ. While the vanilla physics-informed DeepONet performs well for a wide range of computa-
tional mechanics tasks, it is prohibitively expensive on large spatio-temporal grids. The coordinate-dependent network
must be evaluated at every grid point, causing the cost to scale with grid resolution. Additionally, continuously acti-
vated neurons require full multiply-accumulate operations at each evaluation, regardless of input complexity, leading
to high energy consumption during training and repeated inference. The objective of this paper is to address these
limitations by developing scalable operator-learning frameworks that reduce redundant neural activity and execution
cost without modifying the operator representation or the formulation of the physics-informed loss.
3

A PREPRINT - MARCH 24, 2026
3
Proposed Framework
This section formally introduces the Separable Physics-informed Neuroscience-inspired Operator Network
(SPINONet), a unified operator-learning framework that enables sparse, event-driven neural computation while pre-
serving the mathematical structure required for physics-informed training. To substantiate the efficiency and scalability
of SPINONet, we present three analytical studies: (i) a hardware-agnostic analysis of the execution benefits of sparse
spiking activity, (ii) a quantitative assessment of the computational advantages of separable trunk evaluation, and (iii)
a formal justification for employing forward-mode automatic differentiation in residual computation. Finally, we ad-
dress the challenges posed by discontinuous spiking dynamics and describe how gradient-based training is achieved
within the proposed architecture.
3.1
Separable Physics-informed Neuroscience-inspired Operator Network
We start by presenting the mathematical formulation of SPINONet, highlighting its separable construction, event-
driven coefficient generation, and structural compatibility with residual-based physics enforcement. Let Gθ : U →Y
denote the solution operator mapping admissible inputs to the solution fields. For a d-dimensional spatio-temporal
coordinate vector ξ ∈Rd, vanilla separable DeepONet employs d independent trunk networks, each taking a one-
dimensional coordinate vector as input. Specifically, the jth trunk network trj : R →Rpr, that takes ξj ∈R as input
and produces pr basis functions, where p denotes the latent dimension and r the low-rank decomposition rank.
For each coordinate direction j ∈{1, . . . , d}, let kj ∈{1, . . . , nj} denote the grid index along the ξj coordinate.
Evaluating trj(ξj) at nj discrete locations ˆξj = {ξ(kj)
j
}nj
kj=1 along the ξj axis yields an output ˆtr
j(ˆξj) of size nj ×pr,
later reshaped to nj × p × r. Given a set of one-dimensional coordinate grids, along each axis, the d trunk networks
therefore generate coordinate-wise embeddings that can be combined through a separable outer-product construction.
The resulting elements of the basis functions at a location ξ = (ξ(k1)
1
, . . . , ξ(kd)
d
) of the spatio-temporal grid are defined
as,
˜tk1,...,kd,m(ξ) =
r
X
i=1


d
Y
j=1
ˆtr
j
kj,m,i(ˆξj)

,
m = 1, . . . , p.
(3)
Using the elements computed in the above equation, the final trunk output eT ∈Rn1×n2×···×nd×p is constructed
over the full lattice grid, despite each trunk network being evaluated only on one-dimensional coordinate samples
along a single axis. Given an input function u, the branch network B(u) ∈Rp outputs p coefficients; and now, the
operator output at a particular location is obtained by contracting the branch and trunk representations along the latent
dimension p as,
Gθ(u)(ξ) =
p
X
m=1
Bm(u) ˜tk1,...,kd,m(ξ).
(4)
The solution tensor of size n1 × · · · × nd over the whole spatio-temporal domain Ω× T , can be obtained as,
Gθ(u) =
p
X
m=1
Bm(u) eT...,m.
(5)
Physics-informed training is achieved by enforcing the governing equations in a residual sense. Given the operator
approximation in Eq. (4), the interior residual at a collocation point c ∈Ω× T is defined as
Rθ(c; u) = N(Gθ(u)(c); λ) ,
(6)
and the corresponding interior loss is given by
Lint(θ) = 1
Nc
Nc
X
i=1
∥Rθ(ci; u)∥2 .
(7)
Boundary and initial condition constraints are enforced analogously by defining residuals associated with the boundary
operator NB(·) and the initial condition operator NI(·) at collocation points on ∂Ω× T and Ω× {t0}, yielding losses
Lbc(θ) and Lic(θ). The total physics-informed loss is then
Lphys(θ) = Lint(θ) + λbc Lbc(θ) + λic Lic(θ),
(8)
4

A PREPRINT - MARCH 24, 2026
where λbc and λic balance the enforcement of boundary and initial conditions relative to the interior residual. A
defining structural property of the operator representation (4) is that differentiation with respect to the spatio-temporal
coordinates acts exclusively on the coordinate-dependent trunk components. Specifically,
∇ξGθ(u)(ξ) =
p
X
m=1
Bm(u) ∇ξ˜tk1,...,kd,m(ξ).
(9)
The branch coefficients Bm(u) remain independent of the spatio-temporal coordinates ξ. This structural decoupling
enables efficient evaluation of physics-informed residuals using forward-mode automatic differentiation, which is
critical for scalable training in high-dimensional settings. Since coordinate derivatives do not act on the coefficient of
the branch network, modifications to the input-function encoding pathway do not interfere with the spatio-temporal
derivatives required for residual evaluation. SPINONet leverages this property to introduce sparsity-promoting VSNs
at the level of coefficient generation while preserving physics-consistent training. In the proposed framework, the
branch coefficients are generated using VSNs as the activation function, which support graded, continuous-valued
information propagation while exhibiting sparse firing behavior. The dynamics of a VSN are governed by
m(τ) = βl m(τ−1) + z(τ),
(10)
where z(τ) denotes the presynaptic input at spike time step1 τ, m(τ) is the membrane potential, and βl ∈(0, 1) is a
leakage parameter. The neuron produces an output
ey(τ) = H(m(τ) −Th)
y(τ) = ϕ(z(τ)ey(τ))
(11)
where y(τ) is the neuron output at τ spike time step, H(·) denotes the Heaviside function, Th is a firing threshold and
ϕ(·) is a continuous activation function. In the event of a spiking event, i.e. ey(τ) = 1, the memory of VSN is reset
to zero. The graded spiking outputs obtained after the last activation of the branch net are aggregated to form the
coefficient vector B(u) = [b1(u), . . . , bp(u)]⊤, enabling sparse neural computation while maintaining suitability for
regression-based operator learning. Since VSN dynamics involve discontinuous spike-generation mechanisms, special
care is required for gradient-based training; this issue is addressed in Section 3.5.
Training is primarily performed by minimizing the physics-informed objective Lphys(θ) defined above. However,
in certain regimes, purely physics-informed training may converge to degenerate or trivial solutions. When a small
amount of paired training data {(u(i), y(i))}Nd
i=1 along with the grid where the target solution is obtained is available,
this behavior can be mitigated by augmenting the loss with an additional data supervision term,
Ldata(θ) = 1
Nd
Nd
X
i=1
Gθ(u(i)) −y(i)
2
.
(12)
The resulting training objective is then given by
L(θ) = Lphys(θ) + λdata Ldata(θ),
(13)
where λdata controls the contribution of the data term. In the absence of training data, we set λdata = 0 and recover
purely physics-informed training. Algorithm 1 summarizes the complete training procedure for SPINONet, including
residual evaluation through the separable trunk structure and the generation of branch coefficients using VSN-based
sparse computation.
3.2
Energy Efficiency of Sparse Spiking Computation
The primary motivation for using VSNs in SPINONet is the principle of sparse communication, widely regarded
as a key mechanism for enabling energy-efficient information processing in biological neural systems in vivo. By
restricting neural activity to discrete spike events, spiking models reduce the number of active computations, thereby
offering the potential for substantially lower energy consumption. Since absolute energy measurements depend on
hardware architecture and implementation details, we adopt a conservative, hardware-agnostic analysis that isolates
dominant contributors to energy expenditure. In particular, we focus on arithmetic operations and memory read/write
activity, which dominate energy consumption on modern digital platforms.
1In spiking models, neuron dynamics are evaluated over a discrete sequence of spike time steps. We denote the total number of
such steps (i.e., the spike-train length) by Ts, and index individual spike time steps by τ = 1, . . . , Ts. Unless stated otherwise, we
use Ts = 1, which yields sparse, event-driven computation while avoiding additional time-unrolling overhead during training and
inference.
5

A PREPRINT - MARCH 24, 2026
Algorithm 1 Training Algorithm for SPINONet
Require: Training inputs {u(i)}Nu
i=1; interior collocation points {c(j)}Nc
j=1 ⊂Ω× T ; boundary collocation points
{c(j)
b }Nb
j=1 ⊂∂Ω× T ; initial collocation points {c(j)
0 }N0
j=1 ⊂Ω× {t0}; (optional) paired data {(u(i), y(i))}Nd
i=1
along with corresponding grid; separation rank r; latent dimension p; loss weights λbc, λic, λdata.
1: Initialize trunk and branch network parameters.
2: for each training iteration do
3:
Sample a minibatch of inputs {u(i)}.
4:
for each input function u(i) in the minibatch do
5:
Compute branch coefficients B(u(i)) ∈Rp using the VSN-based branch network. In this step, the Heaviside
function to compute ey(τ) within a VSN is retained in its original form in this step.
6:
Evaluate coordinate-wise trunk networks to obtain trunk embeddings.
7:
Evaluate the operator output Gθ(u(i))(ξ) on interior, boundary, and initial collocation points.
8:
Compute physics-informed residuals via forward-mode automatic differentiation.
▷Algorithm 2
9:
end for
10:
Form physics-informed loss Lphys = Lint + λbcLbc + λicLic.
11:
If paired data are available, augment the loss with a data supervision term.
12:
Compute gradients of loss function w.r.t. trainable parameters of the SPINONet. For computing gradients
through branch network, surrogate gradients must be used to approximate gradients of Heaviside function.
▷Algorithm 3
13:
Update all trainable parameters using gradient-based optimization.
14: end for
Outcome: Trained SPINONet parameters θ.
We compare a densely connected artificial neural network (ANN) layer and a densely connected VSN layer with input
and output dimensions, Nin and Nout, respectively. For the VSN layer, computation unfolds over Ts spike time steps,
and input activity is assumed sparse. Total energy is decomposed into compute and memory components,
Etotal = Eops + Emem,
(14)
where Eops represents the energy spent in synaptic operations and Emem represents the energy spent in memory related
operations. In a dense ANN layer, inference is executed as a matrix-vector multiplication, resulting in a fixed number
of multiply-accumulate (MAC) operations,
MACANN = NinNout.
(15)
By contrast, the VSN layer performs synaptic computation only when spikes occur. Let αin denote the average input
spiking activity per time step. The total number of input spikes over a window of Ts spike time steps is modeled as
θl−1 = NinTsαin.
(16)
Each spike fans out to all output neurons, yielding synaptic MACs equal to θl−1Nout. In addition, each output neuron
incurs one multiplication per spike time step due to leakage dynamics. Thus, the total MAC count for the VSN layer
is
MACVSN = θl−1Nout + TsNout.
(17)
When αin ≪1, synaptic computation scales with activity rather than full layer size, leading to substantially fewer
multiplications than dense ANN execution. To account for additional control and integration overhead, we include
accumulation (ACC) operations. For ANN layers, this overhead is small and deterministic, while for VSN layers it
scales with the number of time steps and spike-triggered updates. We model these costs as
ACCANN = Nout + (Nin + Nout),
ACCVSN = 2TsNout + θl−1Nout.
(18)
Although this introduces overhead absent in ANN layers, ACC operations typically consume significantly less energy
than MACs and memory access operations, so reductions in MACs and memory traffic remain the dominant factor
driving energy savings in sparse regimes. Memory access energy is modeled by counting SRAM read and write
operations. For ANN inference, inputs are read once, and all weights and biases are read once,
RdANN = Nin + (Nin + 1)Nout,
WrOutANN = Nout.
(19)
For the VSN layer, input reads occur only when spikes arrive, and synaptic weight reads are similarly spike-triggered.
Conservatively, we assume membrane potentials must be stored in SRAM and accessed at every spike time step, and
that each neuron requires threshold and leakage parameters. The total read count is therefore
RdVSN = θl−1 + (θl−1 + 1)Nout + TsNout + 2Nout.
(20)
6

A PREPRINT - MARCH 24, 2026
Energy is also expended on write operations. The VSN layer writes output spikes and updated neuron states, giving
WrOutVSN = θl + TsNout,
(21)
where θl denotes the total number of output spikes produced over the Ts spike time steps. Let EMAC and EACC denote
the energy cost of a single MAC and ACC operation, and let ERd and EWr denote the energy cost of a single SRAM
read and write. Then, for i ∈{ANN, VSN}, the compute and memory energy are modeled as
Eopsi = EMACMACi + EACCACCi,
Ememi = ERdRdi + EWrWrOuti,
(22)
where EMAC, EACC, ERd and EWr represent the energy spent in MAC, ACC, memory read and memory write operations
respectively. This model is intentionally pessimistic for VSN execution because it assumes frequent state read/write
operations; in practice, architectures may retain neuron states in registers or local buffers, further reducing memory
energy. Using representative energy parameters of 45 nm CMOS technology [40], analysis with varying spiking
activity and number of nodes in layers shows that energy parity between dense ANN and VSN execution is approached
only at high activity levels, approximately ∼90% for Ts = 1 and ∼86% for Ts = 2.
Overall, the discussion above indicates that cumulative spiking activity directly governs energy consumption, since
both arithmetic operations and memory accesses scale with the total number of spikes. Consequently, total spiking
activity provides a physically meaningful and practically useful proxy for energy efficiency. It is worth noting that
model-level optimizations, such as pruning and quantization, can further reduce energy consumption in dense artificial
neural networks, and these optimizations are also applicable to spiking neural networks [41, 42, 43, 44]. Since such
techniques are orthogonal to the execution paradigm, they are not explicitly considered here in order to isolate the
energy implications of sparse, event-driven computation.
3.3
Energy Efficiency of Separable Trunk Evaluation
In this section, we discuss the energy implications of separable trunk evaluation. A complementary and orthogonal
source of energy efficiency in SPINONet arises from the separable structure of the operator architecture, which sub-
stantially reduces the number of coordinate-dependent network evaluations required to produce a solution field. In a
conventional, non-separable, DeepONet architecture, the trunk network is evaluated explicitly at every spatio-temporal
query point on a discretized grid. For a d-dimensional grid with N1, . . . , Nd points along each coordinate axis, this
results in Qd
j=1 Nj trunk evaluations, each incurring a full forward pass through the trunk network and associated
arithmetic and memory costs.
By contrast, in separable operator architectures, coordinate-dependent embeddings are computed independently along
each axis and combined algebraically through outer-product constructions. As a result, the total number of trunk
network evaluations scales as Pd
j=1 Nj, rather than Qd
j=1 Nj. This reduction replaces an exponential dependence on
dimensionality with a linear one, yielding orders-of-magnitude savings in the number of neural network evaluations
for moderately sized grids. To make this reduction more concrete, we consider the arithmetic cost of evaluating a
single dense layer of the trunk network. Let the trunk layer consist of N neurons with fully connected inputs of
dimension Nin. A single evaluation of this layer incurs NinN multiply-accumulate (MAC) operations, along with
O(N) accumulation operations. In a conventional, non-separable DeepONet, this trunk layer is evaluated at every
spatio-temporal grid point. For an d-dimensional grid with N1, . . . , Nd points along each coordinate axis, the total
MAC count for a single trunk layer scales as
MACvanilla
trunk = NinN
d
Y
j=1
Nj,
(23)
with a corresponding accumulation cost that scales proportionally. By contrast, in a separable operator architecture,
the same trunk layer is evaluated independently along each coordinate axis. The resulting total MAC count scales as
MACseparable
trunk
= NinN
d
X
j=1
Nj,
(24)
since coordinate-wise embeddings are computed once per axis and combined algebraically to form the full grid rep-
resentation. Accumulation costs again follow the same scaling behavior. It is worth noting that the outer-product
construction used to assemble the full grid representation introduces additional algebraic operations. However, these
operations scale with the latent rank and the number of grid points only through simple tensor contractions, and do not
involve additional neural network evaluations. As a result, their cost is negligible compared to the savings obtained by
avoiding full trunk forward passes over the spatio-temporal mesh.
7

A PREPRINT - MARCH 24, 2026
This comparison highlights that separable trunk evaluation replaces a multiplicative dependence on grid resolution
with an additive one, yielding orders-of-magnitude reductions in arithmetic operations and reduced activation memory
traffic in practice for moderately to large-sized spatio-temporal grids. These reductions are independent of spiking
activity and arise purely from the architectural structure of the operator representation.
3.4
Forward-Mode Automatic Differentiation and SPINONet
In previous sections, we analyzed the energy efficiency of SPINONet primarily from an inference perspective, focusing
on arithmetic operations and memory access patterns induced by sparse spiking activity and separable trunk evaluation.
Here, we explore the benefits of forward mode automatic differentiation (FAD) over reverse mode AD (RAD) under
the condition of the input dimension being less than the output dimension. We also discuss how the separable trunk
architecture of SPINONet amplifies this advantage compared to a non-separable architecture.
To begin our discussion, let’s first assume input u ∈Rnin and output s ∈Rnout and a network with L hidden layers
hi ∈Rni, i = 1, . . . , L. Now using chain rule, ∂s
∂u can be written as,
∂s
∂u =
 ∂s
∂hL

nout×nL
 ∂hL
∂hL−1

nL×nL−1
· · ·
∂h2
∂h1

n2×n1
∂h1
∂u

n1×nin
.
(25)
The difference in FAD and RAD comes in the order in which the above Jacobian is computed. Visually, in FAD, the
computation flow can be written as,
∂s
∂u = ∂s
∂hL
 
∂hL
∂hL−1

· · ·
 ∂h3
∂h2
 ∂h2
∂h1
∂h1
∂u

· · ·
!
,
(26)
and in RAD can be written as,
∂s
∂u =
 
· · ·
   ∂s
∂hL
∂hL
∂hL−1
∂hL−1
∂hL−2

· · ·
∂h2
∂h1
!
∂h1
∂u .
(27)
Thus, once the individual Jacobians are realized, the total computational cost of forming the final Jacobian can be
expressed in terms of the number of multiply-accumulate (MAC) operations. For FAD, MAC operations MACFAD
can be computed as below,
MACFAD = noutnLnin + nLnL−1nin + · · · + n3n2nin + n2n1nin
MACFAD = nout nL nin +
L
X
ℓ=2
nℓnℓ−1 nin.
(28)
Similarly, MAC operations in RAD, MACRAD can be computed as,
MACRAD = noutnLnL−1 + noutnL−1nL−2 + · · · + noutn1nin
MACRAD = nout n1 nin +
L
X
ℓ=2
nout nℓnℓ−1.
(29)
From the preceding expressions, the computational asymmetry between forward- and reverse-mode automatic dif-
ferentiation becomes explicit, the leading-order cost of FAD scales linearly with the input dimension nin, whereas
the corresponding cost of reverse-mode AD scales linearly with the output dimension nout[45, 46]. This distinction
carries over directly to gradient evaluation via automatic differentiation, where FAD evaluates Jacobian-vector prod-
ucts, and reverse-mode AD evaluates vector-Jacobian products. These scaling behaviors are well established in the
literature [4, 47, 45], and imply that FAD is computationally and memory efficient when the final Jacobian is tall, i.e.,
nin ≪nout, while reverse-mode AD is more appropriate in the complementary regime, i.e., nin ≫nout.
We now discuss the benefit of forward-mode automatic differentiation formally when combined with SPINONet’s
separable trunk structure. The operator approximation from Eq. (4) admits a separable form, where the branch coeffi-
cients Bm(u) depend only on the input function, and all coordinate dependence is confined to the trunk representation.
Consequently, differentiation with respect to ξ acts only on the trunk networks, as shown in Eq. (9). Each trunk net-
work trj : R →Rp×r takes a scalar coordinate ξj as input and outputs a vector of size pr, which is reshaped to size
p×r. Let nj denote the number of sampled points along the j-th coordinate direction, and let Cf denote the computa-
tional cost of a single forward-mode derivative evaluation of a trunk network. In the separable setting, forward-mode
8

A PREPRINT - MARCH 24, 2026
automatic differentiation evaluates coordinate derivatives independently for each trunk network. Since each trunk net-
work receives a scalar input, the effective input dimension for differentiation is one, placing the residual evaluation
firmly in the regime where FAD is computationally favorable. Assuming residuals are evaluated independently at each
discretization point and that no cross-point derivative reuse is available, the cost of forward-mode differentiation scales
as follows:
Csep ∝
d
X
j=1
nj Cf.
(30)
By contrast, a non-separable architecture that maps the full coordinate vector ξ ∈Rd to the solution field requires
forward-mode differentiation at every point on the tensor-product grid. The corresponding cost scales as,
Cnon-sep ∝


d
Y
j=1
nj

Cf.
(31)
After computing the coordinate-wise derivatives, these terms are combined through outer-product constructions and
contracted with the branch coefficients to form the final operator output. This combination step is derivative-free and
is required, in some form, whether a separable or non-separable architecture is employed. This cost is not included in
the forward-mode differentiation cost Csep, which accounts exclusively for derivative evaluations.
In summary, the advantage of forward-mode automatic differentiation in SPINONet arises from two structural prop-
erties: first, the scaling of FAD with the input dimension, and second, the confinement of all coordinate dependence
to separable, one-dimensional trunk networks. Together, these properties significantly reduce the cost of computing
the residual-based loss function. As a consequence of reduced computational load, lower memory requirements, and
the avoidance of derivative evaluations over the whole unrolled spatio-temporal grid, it is reasonable to expect that the
combination of FAD and separable trunk architectures supports an energy-efficient training paradigm for SPINONet.
While the precise energy savings depend on implementation details at both the software and hardware levels, the anal-
ysis presented here provides a system-agnostic surrogate that captures the fundamental computational advantages of
this design. Algorithm 2 summarizes forward-mode residual evaluation in SPINONet for a single collocation point.
The pointwise formulation is adopted for notational clarity; in practice, trunk evaluations and forward-mode derivative
propagation are executed simultaneously over all collocation points using appropriate tensor operations.
Algorithm 2 Forward-Mode Residual Evaluation in SPINONet
Require: Trunk networks {trj}d
j=1; set of differentiated coordinates D ⊆{1, . . . , d}; branch coefficients B(u);
collocation point c.
1: for each coordinate direction j = 1, . . . , d do
2:
Evaluate trunk features trj(ξj) at c.
3:
if j ∈D then
4:
Compute forward-mode derivative ∂trj/∂ξj.
5:
end if
6: end for
7: Assemble required trunk derivatives via separable outer products.
8: Contract with B(u) to obtain Gθ(u) and required coordinate derivatives.
9: Evaluate PDE residual.
Output: Physics-informed residual at c.
3.5
Surrogate Gradient Training in Branch Network
The spike-generation mechanism in VSNs is governed by a discontinuous heaviside function, which precludes the
direct application of standard backpropagation. In particular, derivatives of the form ∂eyτ/∂mτ are undefined in the
classical sense. As a result, standard gradient-based optimization methods cannot be directly applied to networks
containing spiking neurons. To enable end-to-end training, we employ the surrogate gradient method [32, 28], in
which the discontinuous spike function is replaced by a smooth approximation during the backward pass, while the
original hard thresholding operation is retained in the forward pass. This approach preserves the event-driven dynamics
of spiking neurons during inference, while providing meaningful gradients for parameter updates during training.
9

A PREPRINT - MARCH 24, 2026
Applying the chain rule through spike time steps in VSN dynamics, the required derivatives can be expressed in terms
of the membrane potential and spike variables as
dy(i)
dz(j) = ∂y(i)
∂ey(i)
∂ey(i)
∂m(i)
i−1
Y
k=j
∂m(k+1)
∂m(k)
+ ∂m(k+1)
∂ey(k)
∂ey(k)
∂m(k)
 ∂m(j)
∂z(j) ,
i < j,
dy(i)
dz(j) = ∂y(i)
∂ey(i)
∂ey(i)
∂m(i)
∂m(i)
∂z(i) + ∂y(i)
∂z(i) ,
i = j.
(32)
The main challenge in evaluating the above expressions lies in computing ∂ey(τ)/∂m(τ), since spike generation is
governed by a discontinuous threshold function. Following standard surrogate-gradient approaches, we retain the hard
threshold in the forward pass,
eyτ = H(mτ −Th) ,
(33)
and approximate its derivative during backpropagation by a smooth function as,
∂ey(τ)
∂m(τ) = ∂H(mτ −Th)
∂m(τ)
b=
1
1 + Ks
m(τ) −Th
,
(34)
where Ks is a slope parameter controlling the sharpness of the surrogate gradient. A different surrogate gradient can
also be applied depending on the needs of the task at hand.
This surrogate-gradient formulation enables stable gradient-based optimization of the VSN-based branch network in
SPINONet while preserving the discontinuous spiking behavior during inference. It should be noted that because sur-
rogate gradients only approximate the true derivative, their use introduces an approximation error in gradient computa-
tion. Incorporating VSNs into the coordinate-dependent trunk networks would therefore contaminate the computation
of physics-informed residuals, leading to biased PDE learning. For this reason, VSNs are employed exclusively in the
branch network, where they affect only the generation of coefficient vectors and do not interfere with spatio-temporal
differentiation. Algorithm 3 summarizes the surrogate-gradient backpropagation procedure used to compute gradients
for the VSN-based branch network. For clarity, the procedure is presented for a single input sample; in practice, it is
applied in minibatches.
Algorithm 3 Surrogate Gradient Backpropagation in the SPINONet Branch Network
Require: Input u; branch parameters θB; loss L.
1: Perform forward pass through VSN using ey(τ) = H(m(τ) −Th) to obtain B(u).
2: Evaluate loss L using physics-informed and data supervision terms.
3: Backpropagate through VSN dynamics using surrogate derivatives ∂ey(τ)/∂m(τ).
4: Accumulate gradients ∇θBL for branch parameters.
Output: Gradients ∇θBL for updating θB.
In practice, VSNs can be unrolled along the spike-time dimension and accept inputs represented as spike trains of
appropriate length. However, for regression-based operator learning, we observe that directly supplying continuous-
valued inputs, repeated over all Ts spike time steps, yields the best empirical performance. This strategy avoids
unnecessary encoding overhead while retaining sparse, event-driven computation.
4
Numerical Examples
This section presents numerical studies demonstrating the performance of SPINONet on representative PDE bench-
marks. We consider three problems of increasing complexity, namely, (i) the viscous Burgers equation, involving one
spatial and one temporal dimension, (ii) heat equation with parametric diffusion, involving two spatial dimensions,
one temporal dimension and one parameteric dependency, and, (iii) Eikonal equation with parametric boundaries,
involving two spatial dimensions. These examples collectively test nonlinear dynamics, parametric dependence, and
geometric input representations. In all cases, we learn a solution operator G : U →Y that maps admissible inputs
u ∈U (e.g., initial conditions, parameters, or boundary descriptions) to spatio-temporal solution fields y = G(u) ∈Y.
Model predictions are evaluated on unseen test samples and queried on structured grids. We compare SPINONet
against a vanilla separable physics-informed DeepONet, hereafter referred to as vanilla baseline and, where feasible,
a Physics-informed DeepONet (PI-DeepONet), assessing both predictive accuracy and computational efficiency.
10

A PREPRINT - MARCH 24, 2026
To improve readability, architectural choices, discretization strategies, and training configurations for all examples
are summarized in Table 1. Table 2 presents the errors observed in testing data and compares SPINONet against the
PI-DeepONet architecture as well. The reported relative L2 errors are computed as,
Rel-L2 =
1
Ntest
Ntest
X
i=1
bs(i) −s(i)
2
s(i)
2
,
(35)
where s(i) denotes the reference solution field for the i-th test sample, bs(i) denotes the corresponding predicted solution
field, and Ntest is the total number of test samples. The norm ∥·∥2 is taken over all spatio-temporal grid points. While
the errors observed are in a similar range, the training time per epoch is significantly faster in SPINONet, supported by
its separable architecture and use of forward mode automatic differentiation. Below, we focus on qualitative behavior,
accuracy, sparsity, and scaling characteristics.
Table 1: Summary of architectures, discretization, and training configurations for all numerical examples.
Burgers
Heat (Parametric)
Eikonal
Spatial dimension
1D
2D
2D
Temporal dimension
1
1
–
Parameter
IC
α and IC
Geometry
Total dim., d
2
4
2
Branch hidden layers
6 × 100
5 × 50
5 × 50
Branch input size
101
1
400
Trunk hidden layers
6 × 50
5 × 50
5 × 50
Separable ranks (p, r)
20
50
25
Test samples
1000
150
1000
Collocation points
2,601
923,521
1,600
Optimizer
Adam
Adam
Adam
Epochs
40k
100k
40k
Table 2: Comparison of test L2 error and runtime per epoch for PI-DeepONet, Vanilla Baseline, and SPINONet across
Burgers, Heat, and Eikonal equations. Average spiking activity averaged across all VSN layers of the branch net of
SPINONet is also shown.
Equation
Model
L2 error
Runtime (s)/Epoch
Spiking Activity
Burgers
PI-DeepONet
0.05
∼0.604
-
Vanilla Baseline
0.06
∼0.012
-
SPINONet
0.07
∼0.013
53.41
Heat
PI-DeepONet
-
-
-
Vanilla Baseline
0.10
∼0.097
-
SPINONet
0.09
∼0.095
46.33
Eikonal
PI-DeepONet
0.005
∼0.261
-
Vanilla Baseline
0.007
∼0.039
-
SPINONet
0.016
∼0.041
32.22
4.1
Example E-I: Viscous Burgers Equation
We first consider the one-dimensional viscous Burgers equation, a canonical nonlinear convection–diffusion model
that exhibits wave steepening and viscous regularization:
∂u
∂t (x, t) + u(x, t)∂u
∂x(x, t) = ν ∂2u
∂x2 (x, t),
(x, t) ∈Ω× T .
(36)
Periodic boundary conditions are imposed, and initial conditions are sampled from a Gaussian process. The learning
objective is to approximate the operator mapping u(x, 0) 7→u(x, t). To test the performance of the trained model,
predictions were made on a spatio-temporal grid of size 101× 101.
11

A PREPRINT - MARCH 24, 2026
1
2
3
4
5
6
VSN layer index
0
10
20
30
40
50
60
70
80
90
100
Spiking activity %
Ex-1: Burgers
Ex-2: Heat
Ex-3: Eikonal
Figure 1: Mean per-layer spiking activity in the branch-network VSN layers across all numerical examples.
Figure 2 shows representative spatio-temporal predictions on unseen test samples. SPINONet accurately captures
the evolution of the solution and closely matches the reference fields. The error patterns are comparable to those
of the vanilla baseline, with discrepancies primarily localized near regions of steep gradients. Across test samples,
SPINONet exhibits sparse activity in the branch network, with mean firing rates between approximately 45% and 65%
across VSN layers (Fig. 1). The average relative L2 error is 0.07, compared to 0.06 for the vanilla baseline and 0.05
for PI-DeepONet.
Beyond accuracy, SPINONet demonstrates favorable computational scaling. Figures 3a and 3b compare GPU mem-
ory usage and average training time per epoch against PI-DeepONet across increasing grid resolutions. SPINONet
consistently requires substantially less memory and exhibits slower growth in runtime as resolution increases. These
gains arise from the separable operator representation in SPINONet, which enables coordinate-wise trunk evaluation
and algebraic assembly of the solution field. In contrast, PI-DeepONet evaluates the trunk network over the full spatio-
temporal grid, leading to rapidly increasing computational and memory costs. This structural difference explains the
superior scalability observed for SPINONet.
4.2
Example E-II: Heat Equation with Parametric Diffusion
We next consider the two-dimensional heat equation with a parametric diffusion coefficient:
∂u
∂t (x, y, t) = α
∂2u
∂x2 (x, y, t) + ∂2u
∂y2 (x, y, t)

,
(x, y, t) ∈Ω× T .
(37)
Zero Dirichlet boundary conditions are imposed. The learned operator maps the scalar initial condition and diffusion
parameter to the full spatio-temporal solution field, u(x, y, 0; α) 7→u(x, y, t; α). The diffusion parameter is incorpo-
rated into the trunk input as α1/2 to improve numerical conditioning. In this example, predictions from the trained
model were made on a spatio-temporal grid of size 51×51×51, with the grid resolved for 150 values of α.
Figure 4 visualizes representative SPINONet predictions for different values of α. The model reproduces the expected
diffusive behavior, with larger diffusion coefficients producing faster temporal decay and increased spatial smoothing.
Figure 5 compares SPINONet and vanilla baseline predictions against reference solutions. SPINONet achieves a
mean relative L2 error of 0.09, slightly outperforming the vanilla baseline (0.10), while maintaining sparse branch
computation with firing rates between approximately 34% and 58%. PI-DeepONet failed to converge for this example
due to prohibitive memory requirements. These results further highlight the scalability advantages of the separable
formulation in SPINONet. Training SPINONet using data loss alone yields significantly larger errors, underscoring
the importance of physics-informed constraints for this problem.
12

A PREPRINT - MARCH 24, 2026
0.25
0.00
0.25
u(x,0)
0.00
0.25
0.50
0.75
1.00
x
Sample #1
Initial Condition
0
1
t
0
1
x
Ground Truth
0
1
t
0
1
x
SPINONet Prediction
0
1
t
0
1
x
Vanilla Prediction
0.5
0.0
0.5
u(x,0)
0.00
0.25
0.50
0.75
1.00
x
Sample #2
0
1
t
0
1
x
0
1
t
0
1
x
0
1
t
0
1
x
0.1
0.0
0.1
u(x,0)
0.00
0.25
0.50
0.75
1.00
x
Sample #3
0
1
t
0
1
x
0
1
t
0
1
x
0
1
t
0
1
x
0.2
0.0
0.2
0.50
0.25
0.00
0.25
0.50
0.10
0.05
0.00
0.05
(a) Initial conditions, ground-truth solutions, and corresponding predictions produced by SPINONet and the vanilla
baseline for representative test samples.
0
1
t
0
1
x
Sample #1
|SPINONet 
 GT|
0
1
t
0
1
x
|Vanilla 
 GT|
0
1
t
0
1
x
Sample #2
0
1
t
0
1
x
0
1
t
0
1
x
Sample #3
0
1
t
0
1
x
0.00
0.02
0.04
0.06
0.0
0.1
0.2
0.000
0.002
0.004
0.006
(b) Absolute error fields corresponding to the predictions
shown above for SPINONet and the vanilla baseline.
Figure 2: Viscous Burgers equation: Representative comparisons between SPINONet and the vanilla baseline on un-
seen test samples. Rows correspond to different test cases, while columns show solution fields and error distributions.
4.3
Example E-III: Eikonal Equation with Parametric Boundaries
Finally, we consider a two-dimensional Eikonal equation to assess SPINONet’s ability to handle geometric input
representations:
q
sx(x, y)2 + sy(x, y)2 = 1,
(x, y) ∈Ω,
(38)
13

A PREPRINT - MARCH 24, 2026
250×250
500×500
750×750
1000×1000
1250×1250
1500×1500
1750×1750
2000×2000
2250×2250
Grid size
0
10
20
30
40
Max GPU memory (GB)
SPiNONet
Pi-DeepONet
(a) GPU memory consumption.
250×250
500×500
750×750
1000×1000
1250×1250
1500×1500
1750×1750
2000×2000
2250×2250
Grid size
0
1
2
3
4
5
Avg epoch time (s)
SPiNONet
Pi-DeepONet
(b) Average training time per epoch.
Figure 3: Viscous Burgers equation: Comparison of SPINONet and PI-DeepONet computational cost as a function
of grid size. The top panel shows GPU memory consumption, and the bottom panel shows average training time per
epoch. Error bars indicate one standard deviation computed over independent runs.
with Dirichlet boundary conditions s = 0 on ∂Ω. The solution corresponds to the signed distance function to the
boundary. The input to the model is a discretized representation of a circular boundary, and the output is the signed
distance field over the spatial domain. Both SPINONet and the vanilla baseline employ separable trunk representations
with ξ = (x, y). During training, we observed that purely physics-informed formulations may converge to degenerate
solutions. To mitigate this, a small supervised loss is added on the residual grid. 200 training samples were used for
this purpose. Predictions using the trained network were made on a spatial grid of size 200 × 200.
Figure 6 shows representative predictions on test samples. Both models accurately recover the signed distance fields,
with errors concentrated near the boundary. SPINONet achieves a relative L2 error of 0.016, compared to 0.007 for
the vanilla baseline and 0.005 for PI-DeepONet, while maintaining sparse branch activity with firing rates between
approximately 28% and 37%. Runtime per epoch remains comparable to the vanilla baseline, whereas PI-DeepONet
incurs substantially higher computational cost.
5
Conclusion
This work introduced the Separable Physics-informed Neuroscience-inspired Operator Network (SPINONet), a
physics-informed operator-learning framework designed to reduce computational cost in settings where learned oper-
ators are evaluated repeatedly, without sacrificing accuracy or compatibility with residual-based training. The key idea
behind SPINONet is to exploit the separable structure of physics-informed operator networks to enable sparse, event-
driven computation in the branch pathway using neuroscience-inspired spiking neurons, while preserving continuous,
coordinate-differentiable trunk networks required for computing spatio-temporal derivatives. Specifically, we employ
Variable Spiking Neurons (VSNs) within the SPINONet architecture due to their graded, continuous-valued spike for-
mulation and demonstrated effectiveness in regression and operator-learning settings. This separation allows sparsity
to be introduced without altering the physics-informed loss formulation and directly targets redundant computation
during repeated operator queries on grids.
We evaluated SPINONet on multiple PDEs with coupled spatial, temporal, and parametric dependencies. Collectively,
these benchmarks require learning operators over high-dimensional input spaces, providing a nontrivial test of scal-
ability. For instance, the parameterized heat equation involves two spatial dimensions, one temporal dimension, and
one parameter dimension, resulting in a four-dimensional operator-learning problem. Across all examples, SPINONet
consistently produced accurate solution fields while exhibiting clear gains in computational efficiency and scalability
compared to dense operator-learning baselines. In particular, SPINONet achieved competitive prediction accuracy
while maintaining substantial sparsity in the branch network, with firing rates ranging from approximately 28% to
65% across problems. Despite this sparsity, the model remained fully compatible with physics-informed residual
training, as the continuous and differentiable trunk pathways required for computing spatio-temporal derivatives were
preserved throughout. Runtime per epoch remained comparable to the dense separable baseline, while non-separable
14

A PREPRINT - MARCH 24, 2026
0.00
0.25
0.50
0.75
1.00
y
0.0
0.2
0.4
0.6
0.8
1.0
x
= 0.10
0.00
0.25
0.50
0.75
1.00
y
0.0
0.2
0.4
0.6
0.8
1.0
x
= 0.17
0.00
0.25
0.50
0.75
1.00
y
0.0
0.2
0.4
0.6
0.8
1.0
x
= 0.32
0.00
0.25
0.50
0.75
1.00
y
0.0
0.2
0.4
0.6
0.8
1.0
x
= 0.55
0.00
0.25
0.50
0.75
1.00
y
0.0
0.2
0.4
0.6
0.8
1.0
x
= 1.00
0.00
0.25
0.50
0.75
1.00
t
0.0
0.2
0.4
0.6
0.8
1.0
y
0.00
0.25
0.50
0.75
1.00
t
0.0
0.2
0.4
0.6
0.8
1.0
y
0.00
0.25
0.50
0.75
1.00
t
0.0
0.2
0.4
0.6
0.8
1.0
y
0.00
0.25
0.50
0.75
1.00
t
0.0
0.2
0.4
0.6
0.8
1.0
y
0.00
0.25
0.50
0.75
1.00
t
0.0
0.2
0.4
0.6
0.8
1.0
y
0.00
0.25
0.50
0.75
1.00
t
0.0
0.2
0.4
0.6
0.8
1.0
x
0.00
0.25
0.50
0.75
1.00
t
0.0
0.2
0.4
0.6
0.8
1.0
x
0.00
0.25
0.50
0.75
1.00
t
0.0
0.2
0.4
0.6
0.8
1.0
x
0.00
0.25
0.50
0.75
1.00
t
0.0
0.2
0.4
0.6
0.8
1.0
x
0.00
0.25
0.50
0.75
1.00
t
0.0
0.2
0.4
0.6
0.8
1.0
x
y
x
t
y
x
t
y
x
t
y
x
t
y
x
t
0.0
0.2
0.4
0.6
0.8
1.0
Figure 4: Heat equation with Parameteric Diffusion: SPINONet predictions at selected values of α. Shown are
representative planar slices and volumetric renderings of u(x, y, t).
architectures such as PI-DeepONet incurred significantly higher computational and memory costs and, in some cases,
failed to converge.
The benefits of the proposed architecture were especially apparent in challenging regimes. In the parametric heat-
equation example, SPINONet remained tractable, where PI-DeepONet became prohibitively memory-intensive. In
the Eikonal example, the addition of a small supervised loss successfully mitigated degenerate solutions encountered
under purely physics-informed training, improving stability without changing the residual formulation. Across all
problems, SPINONet demonstrated smooth scaling with increasing spatial and temporal resolution and produced stable
predictions across a wide range of evaluation grids.
Overall, these results show that sparse, event-driven computation can be integrated into separable physics-informed
operator learning in a principled and practical way. While challenges common to deep learning remain, such as sensi-
tivity to optimization settings and initialization, the proposed framework provides a promising step toward energy- and
resource-aware operator learning. Future work will explore hardware-aware implementations, sparsity-aware training
objectives, and extensions to higher-dimensional and multi-physics systems. Taken together, SPINONet offers a com-
pelling approach for accurate and scalable operator evaluation under realistic computational and power constraints.
Acknowledgment
The first author acknowledges financial support from the Ministry of Education, India, through the Prime Minister’s
Research Fellows (PMRF) scholarship. The third author acknowledges the support from the U.S. Department of En-
ergy (DOE), Office of Science, Office of Advanced Scientific Computing Research, under Award No. DE-SC0024162.
15

A PREPRINT - MARCH 24, 2026
0
1
t
0
1
x
Ground Truth
Sample #1
T0 = 0.709, 
2 = 0.262
0
1
t
0
1
x
Sample #2
T0 = 0.967, 
2 = 0.860
0
1
t
0
1
x
Sample #3
T0 = 0.506, 
2 = 0.103
0
1
t
0
1
x
Sample #4
T0 = 0.112, 
2 = 0.017
0
1
t
0
1
x
SPINONet Pred.
0
1
t
0
1
x
0
1
t
0
1
x
0
1
t
0
1
x
0
1
t
0
1
x
Vanilla Pred.
0
1
t
0
1
x
0
1
t
0
1
x
0
1
t
0
1
x
0
1
t
0
1
x
|SPINONet
GT|
0
1
t
0
1
x
0
1
t
0
1
x
0
1
t
0
1
x
0
1
t
0
1
x
|Vanilla
GT|
0
1
t
0
1
x
0
1
t
0
1
x
0
1
t
0
1
x
0.00
0.25
0.50
0.75
1.00
0.00
0.25
0.50
0.75
1.00
0.00
0.25
0.50
0.75
1.00
0.0
0.1
0.2
0.3
0.0
0.1
0.2
0.3
0.00
0.25
0.50
0.75
1.00
0.00
0.25
0.50
0.75
1.00
0.00
0.25
0.50
0.75
1.00
0.0
0.2
0.4
0.6
0.0
0.2
0.4
0.6
0.00
0.25
0.50
0.75
1.00
0.00
0.25
0.50
0.75
1.00
0.00
0.25
0.50
0.75
1.00
0.0
0.1
0.2
0.0
0.1
0.2
0.00
0.25
0.50
0.75
1.00
0.00
0.25
0.50
0.75
1.00
0.00
0.25
0.50
0.75
1.00
0.00
0.01
0.02
0.00
0.01
0.02
Figure 5: Heat equation with Parameteric Diffusion: Comparison of reference solutions, SPINONet predictions,
vanilla baseline predictions, and absolute errors. Columns correspond to different test cases, while rows show so-
lution fields and error distributions.
The fourth author acknowledges the financial support received from the Anusandhan National Research Foundation
(ANRF) via grant no. CRG/2023/007667 and from the Ministry of Port and Shipping via letter no. ST-14011/74/MT
(356529).
A
Degenerate convergence modes in physics-informed training for the Eikonal equation
In the Eikonal example, we observed that purely physics-informed training can sometimes converge to solutions that
satisfy the PDE constraint numerically but fail to represent the correct signed distance field. This behavior is not
unique to our model and was observed for both the vanilla baseline and SPINONet during early experiments. The core
issue is that the Eikonal constraint ∥∇s∥= 1 does not, by itself, uniquely select the correct signed distance field unless
additional information anchors the sign structure and the boundary condition behavior in a consistent way across the
domain. As a result, optimization may settle into alternative solutions that appear reasonable under the residual but do
not correspond to the desired interior-exterior signed distance map.
16

A PREPRINT - MARCH 24, 2026
1
0
1
x
1
0
1
y
Sample #1
GT
1
0
1
x
1
0
1
y
SPINONet
1
0
1
x
1
0
1
y
Vanilla
1
0
1
x
1
0
1
y
|SPINONet
GT|
1
0
1
x
1
0
1
y
|Vanilla
GT|
1
0
1
x
1
0
1
y
Sample #2
1
0
1
x
1
0
1
y
1
0
1
x
1
0
1
y
1
0
1
x
1
0
1
y
1
0
1
x
1
0
1
y
1
0
1
x
1
0
1
y
Sample #3
1
0
1
x
1
0
1
y
1
0
1
x
1
0
1
y
1
0
1
x
1
0
1
y
1
0
1
x
1
0
1
y
1
0
1
x
1
0
1
y
Sample #4
1
0
1
x
1
0
1
y
1
0
1
x
1
0
1
y
1
0
1
x
1
0
1
y
1
0
1
x
1
0
1
y
0
1
0.00
0.01
0.02
0
1
0.00
0.01
0.02
0
1
0.00
0.01
0.02
0
1
0.00
0.01
0.02
Figure 6: Eikonal equation with parametric boundaries: Comparison of reference solutions, SPINONet predictions,
vanilla baseline predictions, and corresponding absolute errors. Rows correspond to test samples; columns show
solution fields and absolute errors.
1
0
1
x
1.0
0.5
0.0
0.5
1.0
y
Sample #1
Ground Truth
1
0
1
x
1.0
0.5
0.0
0.5
1.0
y
Erroneous Convergence
(Vanilla)
1
0
1
x
1.0
0.5
0.0
0.5
1.0
y
Flipped Convergence
(Vanilla)
1
0
1
x
1.0
0.5
0.0
0.5
1.0
y
Error (Erroneous)
1
0
1
x
1.0
0.5
0.0
0.5
1.0
y
Error (Flipped)
1
0
1
x
1.0
0.5
0.0
0.5
1.0
y
Sample #2
1
0
1
x
1.0
0.5
0.0
0.5
1.0
y
1
0
1
x
1.0
0.5
0.0
0.5
1.0
y
1
0
1
x
1.0
0.5
0.0
0.5
1.0
y
1
0
1
x
1.0
0.5
0.0
0.5
1.0
y
0.5
0.0
0.5
1.0
0.5
1.0
0.5
0.0
0.5
1.0
0.5
1.0
1.5
Figure 7: Eikonal equation with parametric boundaries: Representative degenerate convergence modes for the Eikonal
equation using the vanilla baseline. Erroneous convergence and flipped-sign convergence, along with the correspond-
ing absolute errors.
This behavior is illustrated in Fig. 7, where the vanilla baseline is shown to converge to two different failure modes
depending on initialization and training dynamics: an erroneous convergence case and a flipped convergence case.
In the erroneous case, the predicted field develops non-physical directional artifacts and vertical band-like structures,
even though the boundary is still visually captured. In the flipped case, the network converges to a solution with the
17

A PREPRINT - MARCH 24, 2026
opposite sign convention, producing a field that resembles a valid distance map but assigns positive values outside
and negative values inside. The corresponding error plots show that the erroneous solution produces large structured
errors across the domain, while the flipped solution produces a characteristic ring-shaped error concentrated around
the interface, reflecting the global sign reversal.
1
0
1
x
1.0
0.5
0.0
0.5
1.0
y
Sample #1
Ground Truth
1
0
1
x
1.0
0.5
0.0
0.5
1.0
y
True Convergence
SPINONet
1
0
1
x
1.0
0.5
0.0
0.5
1.0
y
Flipped Convergence
SPINONet
1
0
1
x
1.0
0.5
0.0
0.5
1.0
y
Error (True)
1
0
1
x
1.0
0.5
0.0
0.5
1.0
y
Error (Flipped)
1
0
1
x
1.0
0.5
0.0
0.5
1.0
y
Sample #2
1
0
1
x
1.0
0.5
0.0
0.5
1.0
y
1
0
1
x
1.0
0.5
0.0
0.5
1.0
y
1
0
1
x
1.0
0.5
0.0
0.5
1.0
y
1
0
1
x
1.0
0.5
0.0
0.5
1.0
y
0.5
0.0
0.5
1.0
0.5
1.0
0.5
0.0
0.5
1.0
0.5
1.0
1.5
Figure 8: Eikonal equation with parametric boundaries: Comparison of true convergence and flipped-sign convergence
for the Eikonal equation, with corresponding absolute errors, when using the proposed SPINONet.
Similar trends were observed when using SPINONet. Fig. 8 compares a true convergence case against the flipped
convergence behavior for the same PDE setup, when using SPINONet for prediction. In the true convergence case, the
predicted signed distance field aligns closely with the ground truth, and the error remains small throughout the domain,
with only faint star-like numerical patterns that are negligible in magnitude. In contrast, the flipped convergence
again produces a smooth-looking field with the correct boundary location but the wrong sign assignment, leading
to a large, spatially coherent error despite an apparently reasonable shape. This highlights that visual smoothness
alone is not sufficient to guarantee correct convergence for Eikonal-based training, and that additional supervision or
sign-consistent constraints are needed to prevent this degenerate behavior. As discussed in the respective example
of the Numerical Illustration section, motivated by these observations, we augment the physics-only objective with a
small supervised loss on the same grid used for residual enforcement. This additional signal acts as an anchor that
discourages flipped or distorted solutions and consistently guides training toward the correct signed distance field
across the full range of boundary instances.
References
[1] Maziar Raissi, Paris Perdikaris, and George E Karniadakis. Physics-informed neural networks: A deep learning
framework for solving forward and inverse problems involving nonlinear partial differential equations. Journal
of Computational physics, 378:686–707, 2019.
[2] George Em Karniadakis, Ioannis G Kevrekidis, Lu Lu, Paris Perdikaris, Sifan Wang, and Liu Yang. Physics-
informed machine learning. Nature Reviews Physics, 3(6):422–440, 2021.
[3] Maziar Raissi and George Em Karniadakis.
Hidden physics models: Machine learning of nonlinear partial
differential equations. Journal of Computational Physics, 357:125–141, 2018.
[4] Junwoo Cho, Seungtae Nam, Hyunmo Yang, Seok-Bae Yun, Youngjoon Hong, and Eunbyung Park. Separable
physics-informed neural networks. Advances in Neural Information Processing Systems, 36:23761–23788, 2023.
[5] Souvik Chakraborty. Transfer learning based multi-fidelity physics informed deep neural network. Journal of
Computational Physics, 426:109942, 2021.
[6] Somdatta Goswami, Cosmin Anitescu, Souvik Chakraborty, and Timon Rabczuk. Transfer learning enhanced
physics informed neural network for phase-field modeling of fracture. Theoretical and Applied Fracture Me-
chanics, 106:102447, 2020.
18

A PREPRINT - MARCH 24, 2026
[7] Lu Lu, Pengzhan Jin, Guofei Pang, Zhongqiang Zhang, and George Em Karniadakis. Learning nonlinear op-
erators via deeponet based on the universal approximation theorem of operators. Nature machine intelligence,
3(3):218–229, 2021.
[8] Zongyi Li, Nikola Kovachki, Kamyar Azizzadenesheli, Burigede Liu, Kaushik Bhattacharya, Andrew Stuart,
and Anima Anandkumar. Fourier neural operator for parametric partial differential equations. arXiv preprint
arXiv:2010.08895, 2020.
[9] Tapas Tripura and Souvik Chakraborty.
Wavelet neural operator for solving parametric partial differential
equations in computational mechanics problems. Computer Methods in Applied Mechanics and Engineering,
404:115783, 2023.
[10] Nikola Kovachki, Zongyi Li, Burigede Liu, Kamyar Azizzadenesheli, Kaushik Bhattacharya, Andrew Stuart,
and Anima Anandkumar. Neural operator: Learning maps between function spaces with applications to pdes.
Journal of Machine Learning Research, 24(89):1–97, 2023.
[11] Jan S Hesthaven, Gianluigi Rozza, Benjamin Stamm, et al. Certified reduced basis methods for parametrized
partial differential equations, volume 590. Springer, 2016.
[12] Christophe Prud’Homme, Dimitrios V Rovas, Karen Veroy, and Anthony T Patera. A mathematical and compu-
tational framework for reliable real-time solution of parametrized partial differential equations. ESAIM: Mathe-
matical Modelling and Numerical Analysis, 36(5):747–771, 2002.
[13] Yinhao Zhu and Nicholas Zabaras. Bayesian deep convolutional encoder–decoder networks for surrogate mod-
eling and uncertainty quantification. Journal of Computational Physics, 366:415–447, 2018.
[14] Ralph C Smith. Uncertainty quantification: theory, implementation, and applications. SIAM, 2024.
[15] Adil Rasheed, Omer San, and Trond Kvamsdal. Digital twin: Values, challenges and enablers from a modeling
perspective. IEEE access, 8:21980–22012, 2020.
[16] Fei Tao, Jiangfeng Cheng, Qinglin Qi, Meng Zhang, He Zhang, and Fangyuan Sui. Digital twin-driven prod-
uct design, manufacturing and service with big data. The International Journal of Advanced Manufacturing
Technology, 94(9):3563–3576, 2018.
[17] Luis Mandl, Somdatta Goswami, Lena Lambers, and Tim Ricken. Separable physics-informed deeponet: Break-
ing the curse of dimensionality in physics-informed machine learning. Computer Methods in Applied Mechanics
and Engineering, 434:117586, 2025.
[18] Sifan Wang, Hanwen Wang, and Paris Perdikaris. Learning the solution operator of parametric partial differential
equations with physics-informed deeponets. Science advances, 7(40):eabi8605, 2021.
[19] Anran Jiao, Qile Yan, Jhn Harlim, and Lu Lu. Solving forward and inverse pde problems on unknown manifolds
via physics-informed neural operators. arXiv preprint arXiv:2407.05477, 2024.
[20] Zongyi Li, Hongkai Zheng, Nikola Kovachki, David Jin, Haoxuan Chen, Burigede Liu, Kamyar Azizzadenesheli,
and Anima Anandkumar. Physics-informed neural operator for learning partial differential equations. ACM/IMS
Journal of Data Science, 1(3):1–27, 2024.
[21] Mohammad Sadegh Eshaghi, Cosmin Anitescu, Manish Thombre, Yizheng Wang, Xiaoying Zhuang, and Timon
Rabczuk. Variational physics-informed neural operator (vino) for solving partial differential equations. Computer
Methods in Applied Mechanics and Engineering, 437:117785, 2025.
[22] N Navaneeth, Tapas Tripura, and Souvik Chakraborty. Physics informed wno. Computer Methods in Applied
Mechanics and Engineering, 418:116546, 2024.
[23] Shailesh Garg and Souvik Chakraborty. Event-driven physics-informed operator learning for reliability analysis.
arXiv preprint arXiv:2511.06083, 2025.
[24] Weisong Shi, Jie Cao, Quan Zhang, Youhuizi Li, and Lanyu Xu. Edge computing: Vision and challenges. IEEE
internet of things journal, 3(5):637–646, 2016.
[25] Xubin Wang, Zhiqing Tang, Jianxiong Guo, Tianhui Meng, Chenhao Wang, Tian Wang, and Weijia Jia. Empow-
ering edge intelligence: A comprehensive survey on on-device ai models. ACM Computing Surveys, 57(9):1–39,
2025.
[26] Sizhe An, Yigit Tuncel, Toygun Basaklar, and Umit Y Ogras. A survey of embedded machine learning for smart
and sustainable healthcare applications. In Embedded Machine Learning for Cyber-Physical, IoT, and Edge
Computing: Use Cases and Emerging Challenges, pages 127–150. Springer, 2023.
[27] Taiwo Samuel Ajani, Agbotiname Lucky Imoize, and Aderemi A Atayero. An overview of machine learning
within embedded and mobile devices–optimizations and applications. Sensors, 21(13):4412, 2021.
19

A PREPRINT - MARCH 24, 2026
[28] Kashu Yamazaki, Viet-Khoa Vo-Ho, Darshan Bulsara, and Ngan Le. Spiking neural networks and their applica-
tions: A review. Brain sciences, 12(7):863, 2022.
[29] Duy-Anh Nguyen, Xuan-Tu Tran, and Francesca Iacopi. A review of algorithms and hardware implementations
for spiking neural networks. Journal of Low Power Electronics and Applications, 11(2):23, 2021.
[30] Shirin Dora and Nikola Kasabov. Spiking neural networks for computational intelligence: an overview. Big Data
and Cognitive Computing, 5(4):67, 2021.
[31] Rachmad Vidya Wicaksana Putra and Muhammad Shafique. Fspinn: An optimization framework for memory-
efficient and energy-efficient spiking neural networks. IEEE Transactions on Computer-Aided Design of Inte-
grated Circuits and Systems, 39(11):3601–3613, 2020.
[32] Emre O Neftci, Hesham Mostafa, and Friedemann Zenke. Surrogate gradient learning in spiking neural net-
works: Bringing the power of gradient-based optimization to spiking neural networks. IEEE Signal Processing
Magazine, 36(6):51–63, 2019.
[33] Qinglai Wei, Qizhi Yang, Liyuan Han, and Tielin Zhang.
Physics-informed spiking neural networks for
continuous-time dynamic systems. Neurocomputing, page 132192, 2025.
[34] Siqi Wang, Pietro Maris Ferreira, and Aziz Benlarbi-Delai. Physics informed spiking neural networks: Applica-
tion to digital predistortion for power amplifier linearization. IEEE Access, 11:48441–48453, 2023.
[35] Saurabh Balkrishna Tandale and Marcus Stoffel. Physics-based self-learning spiking neural network enhanced
time-integration scheme for computing viscoplastic structural finite element response. Computer Methods in
Applied Mechanics and Engineering, 422:116847, 2024.
[36] Shailesh Garg and Souvik Chakraborty. Neuroscience inspired scientific machine learning (part-1): Variable
spiking neuron for regression. arXiv preprint arXiv:2311.09267, 2023.
[37] Ruyin Wan, George Em Karniadakis, and Panos Stinis. From lif to qif: Toward differentiable spiking neurons
for scientific machine learning. arXiv preprint arXiv:2511.06614, 2025.
[38] Isha Jain, Shailesh Garg, Shaurya Shriyam, and Souvik Chakraborty. Hybrid variable spiking graph neural
networks for energy-efficient scientific machine learning. Journal of the Mechanics and Physics of Solids, page
106152, 2025.
[39] Shailesh Garg and Souvik Chakraborty. Neuroscience inspired neural operator for partial differential equations.
Journal of Computational Physics, 515:113266, 2024.
[40] Norman P Jouppi, Doe Hyun Yoon, Matthew Ashcraft, Mark Gottscho, Thomas B Jablin, George Kurian, James
Laudon, Sheng Li, Peter Ma, Xiaoyu Ma, et al. Ten lessons from three generations shaped google’s tpuv4i:
Industrial product. In 2021 ACM/IEEE 48th Annual International Symposium on Computer Architecture (ISCA),
pages 1–14. IEEE, 2021.
[41] Chen Li, Lei Ma, and Steve Furber. Quantization framework for fast spiking neural networks. Frontiers in
Neuroscience, 16:918793, 2022.
[42] Wenjie Wei, Malu Zhang, Zijian Zhou, Ammar Belatreche, Yimeng Shan, Yu Liang, Honglin Cao, Jieyuan
Zhang, and Yang Yang.
Qp-snn:
Quantized and pruned spiking neural networks.
arXiv preprint
arXiv:2502.05905, 2025.
[43] Yi Jiang, Malyaban Bal, Brian Matejek, Susmit Jha, Adam Cobb, and Abhronil Sengupta. Spatio-temporal
pruning for compressed spiking large language models. arXiv preprint arXiv:2508.20122, 2025.
[44] Yanqi Chen, Zhaofei Yu, Wei Fang, Tiejun Huang, and Yonghong Tian. Pruning of deep spiking neural networks
through gradient rewiring. arXiv preprint arXiv:2105.04916, 2021.
[45] Atilim Gunes Baydin, Barak A Pearlmutter, Alexey Andreyevich Radul, and Jeffrey Mark Siskind. Automatic
differentiation in machine learning: a survey. Journal of machine learning research, 18(153):1–43, 2018.
[46] https://math.stackexchange.com/users/64344/user664303. Reverse mode differentiation vs. forward mode dif-
ferentiation - where are the benefits?, 2024. Published on 04-05-2024, accessed on 28-01-2026.
[47] Andreas Griewank and Andrea Walther. Evaluating derivatives: principles and techniques of algorithmic differ-
entiation. SIAM, 2008.
20
