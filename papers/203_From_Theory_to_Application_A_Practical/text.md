## From Theory to Application: A Practical Introduction to Neural Operators in Scientific Computing

Prashant K. Jha1

# arXiv:2503.05598v1[cs.CE]7 Mar 2025

### Abstract

This focused review explores a range of neural operator architectures for approximating solutions to parametric partial differential equations (PDEs), emphasizing high-level concepts and practical implementation strategies. The study covers foundational models such as Deep Operator Networks (DeepONet), Principal Component Analysis-based Neural Networks (PCANet), and Fourier Neural Operators (FNO), providing comparative insights into their core methodologies and performance. These architectures are demonstrated on two classical linear parametric PDEs—the Poisson equation and linear elastic deformation. Beyond forward problem-solving, the review delves into applying neural operators as surrogates in Bayesian inference problems, showcasing their effectiveness in accelerating posterior inference while maintaining accuracy. The paper concludes by discussing current challenges, particularly in controlling prediction accuracy and generalization. It outlines emerging strategies to address these issues, such as residual-based error correction and multi-level training. This review can be seen as a comprehensive guide to implementing neural operators and integrating them into scientific computing workflows.

Keywords: neural operators; neural networks; operator learning; surrogate modeling; Bayesian inference

Contents

- 1 Introduction 2

- 1.1 Organization of the article . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3

2 Preliminaries 4

- 2.1 Notations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4


- 2.2 Series representation of functions and finite-dimensional approximation . . . . . . . 6

- 2.2.1 Finite element approximation . . . . . . . . . . . . . . . . . . . . . . . . . . 7

2.3 Dimensional reduction and singular-value decomposition (SVD) . . . . . . . . . . . 8

- 2.3.1 Projectors via SVD . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8

2.4 Probability sampling of functions aka infinite-dimensional random variables . . . . 10

- 2.4.1 Gaussian measures based on Laplacian-like operators . . . . . . . . . . . . . 10




1Department of Mechanical Engineering, South Dakota School of Mines and Technology, Rapid City, SD 57701, USA. Email address: prashant.jha@sdsmt.edu

### 3 Model problems 13

- 3.1 Poisson problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13

- 3.1.1 Setup details and data generation . . . . . . . . . . . . . . . . . . . . . . . 14

3.2 Linear elasticity problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17

- 3.2.1 Setup details and data generation . . . . . . . . . . . . . . . . . . . . . . . 18




### 4 Neural networks as surrogate of the forward problem 19

- 4.1 Deep Operator Network (DeepONet) . . . . . . . . . . . . . . . . . . . . . . . . . . 19

- 4.1.1 Implementation of DeepONet . . . . . . . . . . . . . . . . . . . . . . . . . . 21
- 4.1.2 Architecture and preliminary results . . . . . . . . . . . . . . . . . . . . . . 25


- 4.2 Principal Component Analysis-based Neural Operator (PCANet) . . . . . . . . . . 27

- 4.2.1 Implementation of PCANet . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
- 4.2.2 Architecture and preliminary results . . . . . . . . . . . . . . . . . . . . . . 31


- 4.3 Fourier Neural Operator (FNO) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31


- 4.3.1 Implementation of FNO . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
- 4.3.2 Architecture and preliminary results . . . . . . . . . . . . . . . . . . . . . . 37


### 5 Neural Operators applied to Bayesian inference problems 37

- 5.1 Abstract Bayesian inference problem in infinite dimensions . . . . . . . . . . . . . 37 5.1.1 Markov chain Monte Carlo (MCMC) method to sample from the posterior

measure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39

- 5.2 Inference of the diffusivity in Poisson problem . . . . . . . . . . . . . . . . . . . . . 41

- 5.2.1 Setup of the forward problem, prior measure, and synthetic data . . . . . . 42
- 5.2.2 Inference results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42


- 5.3 Inference of Young’s modulus in linear elasticity problem . . . . . . . . . . . . . . . 45


- 5.3.1 Setup of the forward problem, prior measure, and synthetic data . . . . . . 45
- 5.3.2 Inference results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45


### 6 Conclusion 48

- 6.1 Growing field of neural operators . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
- 6.2 Controlling the neural operator prediction accuracy . . . . . . . . . . . . . . . . . . 49
- 6.3 Final thoughts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51


References 51

- 1. Introduction


Neural operators have emerged as powerful tools for approximating solution operators of parametric partial differential equations (PDEs). Their key advantages include learning highly nonlinear mappings between function spaces and effectively reducing modeling errors when observational data is available, even if the underlying models are poorly formed. Additionally, their capacity for fast evaluations makes them particularly valuable in applications like real-time optimization and control.

This article offers a practical and hands-on introduction to several key neural operator architectures that have gained prominence in scientific computing. The following neural operators are explored:

- 1. Deep Operator Network (DeepONet) Wang et al. (2021a); Lu et al. (2021a,b); Goswami et al.

(2020);

- 2. Principle Component Analysis/Proper Orthogonal Decomposition-based Neural Operator (PCANet/PODNet) Bhattacharya et al. (2021); Fresca and Manzoni (2022); and
- 3. Fourier Neural Operator (FNO) Li et al. (2021); Kovachki et al. (2021).


This introduction is designed to be self-contained, hands-on, and transparent regarding algorithmic details. Rather than providing an exhaustive review of generalizations or diverse applications, the focus remains on the foundational ideas behind these core neural operators and the practical aspects of their implementation. The aim is to equip readers with a solid understanding that can serve as a stepping stone for exploring broader extensions in the literature.

Several crucial topics are addressed to ensure a deeper understanding of neural operators:

- • Sampling random functions using Gaussian measures on function spaces;
- • Defining data structures specific to each neural operator;
- • Algorithms and Python implementations for all critical computations, including random function sampling and Markov Chain Monte Carlo (MCMC) for Bayesian inference; and
- • A detailed exploration of neural operators’ application to Bayesian inverse problems.


To illustrate the use of neural operators, two classical linear parametric PDEs are used as model problems. The first model is based on the Poisson equation for a temperature distribution on a rectangular domain, where the input parameter field is the diffusivity. The second model corresponds to the in-plane deformation of a thin elastic plate, with Young’s modulus being the input parameter field. For these model problems, neural operators approximating the solution operator are constructed, and their accuracy for random samples of the input function is assessed. For the demonstration, neural operators are used as a surrogate in Bayesian inference problems, where the parameter fields in the above two model problems are inferred from the observational data. The performance of neural operators as surrogates is comparable to the “true” model. The model problems considered in this work are linear and have a fast decay of singular values of input and output data. This indicates a low dimensional structure of the solution operator, making it easier to approximate using neural operators. For highly nonlinear problems and challenging inference and optimization problems, neural operators may show significant errors. This issue is discussed in the conclusion section, where some existing works on controlling neural operator prediction errors are surveyed.

- 1.1. Organization of the article


- • Section 2 introduces notations and key mathematical preliminaries, covering finite-dimensional function approximations, singular value decomposition, and sampling random functions using Gaussian measures.
- • Section 3 presents the two parametric PDEs used as model problems for developing neural operators.


- • Section 4 discusses the architectures and implementations of DeepONet, PCANet, and FNO, focusing on their core principles, critical implementation details in Python, and an evaluation of their predictive performance.
- • Section 5 explores the application of neural operators to Bayesian inverse problems, using them as surrogates for forward models in MCMC simulations.
- • Section 6 concludes the article, summarizing key insights, referencing additional neural operator architectures not covered here, and discussing strategies for controlling prediction errors. The subsection on prediction accuracy (Section 6.2) highlights related works and outlines potential future research directions.


Codes and Jupyter notebooks for neural operator training and Bayesian inference are available at: https://github.com/CEADpx/neural_operators/ (check out tag survey25_v1). The data is shared separately in the Dropbox folder NeuralOperator_Survey_Shared_Data_March2025.

### 2. Preliminaries

This section collects crucial information that will provide a solid foundation for the topics covered in the rest of the sections. It begins by fixing the notations.

- 2.1. Notations


Let N,Z,R denote the space of natural numbers, integers, and real numbers, respectively, and R+ denotes the space of all nonnegative real numbers. Rn denotes the n-dimensional Euclidean space. Space of L2-integrable functions f : D ⊂ Rq → Rd is denoted by L2(D;Rd); space Hs(D;Rd) for functions in L2(D;Rd) with generalized derivatives up to order s in L2(D;Rq×si=1−1q×d). L(M;U) denotes the space of continuous linear maps from M to U and C1(A;U) space of continuous and differentiable maps from A ⊂ M to U. Given a generic complete normed (function) Banach space A, ∥·∥ denotes the norm, and if it is a Hilbert space ⟨u,v⟩ denotes the inner production for u,v ∈ A. A∗ denotes the dual of the Banach space A and ⟨a,b⟩, where a ∈ U∗ and b ∈ U.

Throughout the text, m ∈ M will denote the input or parameter field in the parametric boundary value problem, M the appropriate Banach function space for input fields, u ∈ U the solution field, where U is the Banach space for solutions of the PDE. The so-called solution operator or forward operator that maps the parameter field m ∈ M to the solution u ∈ U of the PDE is denoted by F(m). The neural network approximation of the forward operator F(m) is denoted using FNN(m). The finite-dimensional approximation of functions m ∈ M and u ∈ U are denoted by the bold Roman letter m and u, and more generally for any a ∈ A, a. The corresponding map between discrete versions of input and output functions is u = F(m). The projections of discretizations of functions, m and u, onto lower-dimensional subspaces will be denoted by m˜ and u˜, respectively. The mapping between lower-dimensional subspaces will be denoted using˜on top (e.g., F˜).

The key notations used throughout the text are collected in Table 1.

|Symbol<br><br>|Description|
|---|---|


m Typical parameter field in the parametric PDEs, which is also the input function to neural operators

u Typical solution of the PDE given m, which is also the output of the neural operator Da Domain of some abstract function a ∂D,Γb Boundary of the domain D and subset of ∂D tagged by b,

respectively qa Dimension of the domain of function a da Dimension of the pointwise values of the function a

- M = {m : Dm ⊆ Rqm → Rdm} Function space of the parameters in the parametric PDEs U = {u : Du ⊆ Rqu → Rdu} Function space of the solution of the PDE


F : m ∈ M  → F(m) = u ∈ U Forward solution operator, which is also the target operator of neural operators

ϕa = {ϕai}∞i=1 Basis functions for the function space associated with the function a, e.g., ϕm for M so m ∈ M has representation m = i miϕai

- x ∈ Dm Spatial coordinates in the domain of input/parameter functions

- y ∈ Du Spatial coordinates in the domain of output/solutions


a ∈ Rpa Bold Roman symbol indicates the finite-dimensional representation/approximation of the function a, e.g., nodal values (m1,m2,...,mpm) in finite element discretization of m ∈ M

pa Dimension of the finite-dimensional representation of function

a, i.e., a lives in Rpa ai ith component of a F : m ∈ Rpm  → F(m) = u ∈ Rpu Finite-dimensional approximation of the operator F : M → U ra Dimension of the reduced dimensional representation of a ∈

Rpa, ra << pa a˜ ∈ Rra The reduced-dimensional representation of a ∈ Rpa P˜a : Rpa → Rra Projection operator that takes finite-dimensional representa-

tion of function a ∈ Rpa to the reduced space a˜ = P˜a(a) ∈ Rra

F˜r : m˜ ∈ Rrm  → F˜r(m˜ ) = u˜ ∈ Rru Reduced-order approximation of F mapping between reduced

(latent) spaces of input and output functions N(m,C) Gaussian random field with mean m ∈ M and covariance

operator C : M × M → M

N(m,C) Gaussian random field in finite-dimensional space Rpm, where

m ∈ Rpm and C : Rpm × Rpm

FNN : M × Θ → U Typical neural operator approximation of F : M → U with

trainable neural network parameters Θ ∈ Rpnn

FNN : Rpm × Θ → Rpu Neural operator approximation of finite-dimensional repre-

sentation of the map F : Rpm → Rpu

- N Number of data for training and testing neural operators


mI,uI,mI,uI Ith sample of input and output functions in functional and finite-dimensional settings

- X = (m1,m2,...,mN)T ∈ RN×pm Input data to the neural operator, where mI ∈ Rpm is seen as a column vector

Xtr ∈ RN×Ntr×qm Input data to the trunk network of the DeepONet neural operator, where for each I, 1 ≤ I ≤ N, XItr is Ntr ×qm and it consists of Ntr number of spatial coordinates in the domain Du ⊆ Rqu

- Y = (u1,u2,...,uN)T ∈ RN×pu Output data to the neural operator XI,YI Ith sample, 1 ≤ I ≤ N, of the data from X,Y, respectively


Table 1: Key notations used in this text.

- 2.2. Series representation of functions and finite-dimensional approximation


One of the central ideas that various neural operators leverage is the finite-dimensional representation of functions consisting of coefficients and basis functions in their respective spaces. Following the notations in the previous section and Table 1, suppose that M and U are Hilbert spaces, and, therefore, have orthonormal sequences ϕm = {ϕmi}∞i=1 and ϕu = {ϕui}∞i=1, respectively, so that

∞

miϕmi(x), ∀x ∈ Dm , (1)

m(x) =

i=1

where mi = ⟨m,ϕmi⟩ are the coefficients or degrees of freedom associated with the ith mode. It is useful to consider the example with Dm = (0,1) and m ∈ L2(Dm;R). In this case, one can write

- m = ∞i=1 miϕmi(x), where basis functions take the form


cos(2πx) √2

ϕm1 = 1,Φm2 =

sin(2πx) √2

cos(2jπx) √2

sin(2jπx) √2

,···,ϕm2j =

,··· (2)

,ϕm3 =

,ϕm2j+1 =

and the coefficients are given by

mi = ⟨m,ϕmi⟩ =

1

m(x)ϕmi(x)dx, ∀i. (3)

0

Focusing on the abstract setting, let {ϕmi}pi=1m , where pm a finite integer, are the finite collection of basis functions, and {mi}pi=1m are the corresponding coefficients. Then, the finite-dimensional approximation is pi=1m miϕmi(x) ≈ m(x) with the error given by ∥m − ( pi=1m miϕmi)∥. The same can be done for the function u ∈ U to have u(y) ≈ pi=1u uiϕui(y), y ∈ Du. Very often, the neural operator will try to imitate this finite-dimensional approximation technique, where the goal will be to find (learn) the bases {ϕui}pi=1u (or its pointwise values {ϕui(y)}pi=1u for y ∈ Du [e.g., in DeepONet]) and the coefficients {ui}pi=1u such that pi=1u uiϕui provides the “best” approximation of u = F(m), m ∈ M being the input function to the operator.

- 2.2.1. Finite element approximation


For a general class of function space M ⊆ {m : Dm ⊆ Rqm → Rdm} and spatial domain Dm, the theory above to develop a finite-dimensional approximation of functions can be restrictive. The more straightforward and numerical way to obtain the finite-dimensional approximation is using numerical techniques such as finite difference and finite element approximation. In this work, the finite element method is used (e.g., to generate samples of input functions using Gaussian priors, solve PDE-based problems, and solve the Bayesian inference). To be more precise, consider a finite element discretization Dmh of the domain Dm consisting of simplex elements {Te}Ne=1e so that Dmh = ∪eT¯e ≈ Dm. Suppose ϕmi is the linear Lagrange basis of the ith vertex. Let Vmh = span{ϕmi}pi=1m , pm being the number of vertices. Then, the function m ∈ M can be approximated by a function mh ∈ Vmh given by

pm

m(x) ≈ mh(x) =

miϕmi(x), ∀x ∈ Dmh , (4)

i=1

provided the coefficients m ∈ Rpm is selected appropriately. For example, m is selected such that it minimizes the L2 error e = ||m − mh||L2).

Given finite dimensional approximations mh and uh of m and u, respectively, the map F(m) = u is also approximated by Fh(mh) = uh in the sense that Fh takes mh and returns the output hh such that the error

||F(m) − Fh(mh)|| (5) is small for the appropriate collection of m.

Before concluding this section, note that, for the fixed mesh and the basis functions ϕm, it is easy to see that if m ∈ Rpm is fixed, then the function mh is completely characterized. If the mh is fixed, using the unique representation of mh, the coefficients m are completely characterized. So, Vmh can be identified using Rpm (and vice versa). This makes it possible to represent the finite-dimensional function space Vmh by the Euclidean space Rpm of the coefficients. Throughout the paper, functions m and u will be represented by the finite-dimensional approximations m and

u, where the functional representation of coefficients m and u, m and u, respectively, is assumed implicitly. In the same spirit, since uh = Fh(mh) (for a given mh) can be identified by u, a map F : Rpm → Rpu is defined as follows:

pu

pm

F(m) = u ⇒ Fh(mh) = uh =

uiϕui with mh =

miϕmi . (6)

i=1

i=1

Here, F maps the coefficient vector m to u and is induced by the map F.

- 2.3. Dimensional reduction and singular-value decomposition (SVD)


While the theory is based on functions defined on a continuum domain, computer implementations introduce discretization of the domain and, consequently, discrete approximation of functions. For example, the training data for neural operators is typically a collection of pairs (mI,uI) where

- mI ∈ Rpm and uI = F(mI) ∈ Rpu are discrete approximations of functions in M and U, F being the finite-dimensional mapping between Rpm and Rpu approximating the operator of interest F(m).


Generally speaking, the dimensions of input and target functions, pm and pu, are large, and the problem of approximating the map F between high dimensional spaces becomes challenging and quite possibly ill-posed.

The second key idea, the first being the linear basis representation discussed earlier, used in various neural operators is reducing the dimensions of discretized input and output functions; see Bhattacharya et al. (2021). If m ∈ Rpm and u ∈ Rpu, and the goal is to determine a map m  → u = F(m) from the data {(mI,uI)}NI=1, then, alternative to learning/approximating the map F, one could attempt to characterize the map F˜, where

m  → u = P˜Tu F˜ P˜m(m) . (7)

Here, P˜m ∈ Rrm×pm is the projection operator that projects m ∈ Rpm into a lower dimensional subspace, m˜ := P˜m(m) ∈ Rrm (with rm << pm). P˜u ∈ Rru×pu has the same role as P˜m but for target functions u ∈ Rpu. The transpose of P˜u, P˜Tu, projects the element in Rru into Rpu. Note that F˜ : Rrm → Rru that needs to be learned is the mapping between two smaller dimensional spaces, and, hence, identifying F˜ is less daunting compared to F. In summary, using P˜m and P˜u, the dimensions of the operator inference problem are significantly reduced, and, by controlling rm and ru, one can balance the trade-off between accuracy and computational cost.

- 2.3.1. Projectors via SVD The projectors P˜m and P˜u for dimensional reduction can be obtained via singular-value de-


composition (SVD). Focusing on the input space Rpm, let R denote a pm × N matrix such that, for 1 ≤ I ≤ N, mI makes up the Ith column of the matrix R. Let rR = rank(R) ≤ min{pm,N} be the rank of the matrix, and R = UDVT its singular-value decomposition, where U and V are column-orthonormal matrices of sizes pm × pm and N × N, respectively, and D is a pm × N diagonal matrix. Focusing on the matrix U, the ith column is denoted by a vector wi ∈ Rpm. The set of vectors (columns of U) {wi}pi=1m form the orthonormal basis for Rpm.

Let rm > 0 such that rm ≤ rank(R) is the dimension of the reduced space Rrm for which a projector Pm : Rpm → Rrm is sought. Given rm, a matrix Urm of size pm × rm is constructed by

removing the (pm − rm) columns of U from the end:





| | | w1 w2 ··· wrm | | |

Urm =

. (8)

 

 

Noting the properties of Urm (e.g., see (Jha, 2024, Section 3.2.1)), UTrm is taken as the projector, i.e., P˜m := UTrm.

For u, the projector P˜u is obtained following the same procedure as above using a matrix R of size pu × N with uI making its Ith column. SVD of R, say U, is truncated by retaining the first ru columns of U. If the truncated matrix is Uru then P˜u := UTru.

![image 1](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile1.png)

Figure 1: Singular values of input and output data (centered and normalized) {mi = exp(wi)|wi ∼ N(0, C)}, and {ui = F(mi)}, where N(0, C) is the pm-dimensional Gaussian density obtained via the finite element approximation of the random Gaussian field in function space M := L2(Dm; R) (see Section 2.4 for details), mi discretized input to the parametric PDE, and F a discretized solution operator associated with the PDE. σa, a ∈ {m, u}, represents the normalized singular values. Small dots show corresponding modes when the normalized singular value is 0.01 or 0.1. The dimension of the reduced space is 100, and the grey dots show the corresponding singular value in the plot.

In Figure 7, the normalized singular values of representative centered and normalized input and output data are shown. The grey, brown, and cadet blue dots on each curve represent the singular value at mode 100, the mode with a singular value of 0.1, and the mode with a singular value of 0.01. Based on the plot, if u is projected using SVD to 100, 10, and 49, the average projection error will be around 0.3%, 10%, and 1%, respectively, relative to the most significant singular value. Similarly, for m, projection into reduced dimension r = 100, 35, and 290 will result in the average projection error (approx.) 3.3%, 10%, and 1%, respectively.

- 2.4. Probability sampling of functions aka infinite-dimensional random variables The final topic to conclude this section is sampling random parameters, which are functions.


Consider a probability space (Ω,F,P), where Ω is a sample space and F is a σ-algebra on which probability measure P is defined with P(Ω) = 1. The goal is to draw W-valued random fields, where W is assumed to be a separable Hilbert space (i.e., design a random field Z : Ω → W such that given z ∈ Ω, w = Z(z) ∈ W). Suppose such an Z is designed; then, the probability that values of Z are in some subset A ⊆ W is the pushforward measure µZ of A given by

µZ(A) = probability of Z ∈ A = P({z ∈ Ω : Z(z) ∈ A}) = P Z−1(A) , (9)

where Z−1(A) ∈ F is assumed to be measurable in probability space (Ω,F,P). Thus, µZ is a measure on W induced by the random field Z. Now, suppose that a random field Z is such that the

measure µZ is Gaussian in the sense of Dashti and Stuart (2017); Mandel (2023), (e.g., see (Dashti and Stuart, 2017, Definition 6 and Lemma 23)). In this case, µZ is written as µZ = N( ¯w,C). Here, w¯ ∈ W is the mean function, and C : W → W is called the covariance operator. At the outset, C is assumed to be a trace-class operator; see (Dashti and Stuart, 2017, Lemma 23) and (Mandel, 2023, Theorem 7).

Our next goal is to consider specific examples of Z such that µZ is Gaussian, as mentioned above, and see how the random samples of functions are generated. In this direction, it is useful to highlight the role of C in generating samples w = Z(z) ∈ W; this will help to understand why the widely-used forms of C make sense and work. Consider another random field S : Ω → W such that µS = N(0,1), where 0 ∈ W is the mean function and 1 : C → C is the identity covariance operator. Given w¯ ∈ W and C : W → W, a sample w = Z(z) (Z such that µZ = N( ¯w,C)) is computed by transforming the sample s = S(z) as follows:

Z(z) = w := w¯ + C1/2s. (10)

Thus, C1/2, the square root of the covariance operator, plays a key role in generating random functions. As such, C should be designed so that C1/2 is more straightforward to apply while satisfying the properties such that the W-valued samples are well-defined, have desired regularity, and have bounded correlation between pointwise values.

- 2.4.1. Gaussian measures based on Laplacian-like operators


Following Bui-Thanh et al. (2013), let C = L−∆2, where L∆ : WL∆ ⊂ W → W is a Laplacian-like operator given by

L∆ := −ac∇ · bc∇ + cc , in Dw , γn · bc∇, on ∂Dw .

(11)

Here, Dw is the domain of functions w, and ac,bc,cc are parameters in the operator (they could vary over the domain or be taken as constants). In this work, ac and cc will be constant, and in some situations, bc will be considered to be a spatially varying scalar-valued L2(Dw) function. In the literature, it is also common to take bc as Rqw×dw × Rqw×dw-valued function allowing one to encode anisotropy and inhomogeneous behavior in the prior. In the above, WL∆ ⊆ W is the domain of operator L∆ such that L∆(w) is well-defined for all w ∈ L∆. The natural choice is WL∆ = {w ∈ W : ||w||H2 < ∞}. If L∆ is defined in a weak form, i.e.,

⟨v,L∆(w)⟩ =

[acbc∇w · ∇v + ccwv] dx, ∀w,v ∈ W ∩ H1(Dw;Rdw), (12)

Dw

then WL∆ can be taken as WL∆ = W ∩ H1(Dw;Rdw).

With the above specific form of C and what was discussed earlier, the sampling of functions w ∈ W can be summarized as follows:

- 1. Fix w¯ ∈ W, C = L−∆2, and S : Ω → W a random field such that µS = N(0,1);
- 2. Draw a sample s = S(z), z ∈ Ω; and
- 3. Compute w = w¯ + C1/2(s)


⇒ w = w¯ + L−∆1(s)

⇒ w = w¯ + v , where v satisfies: s = L∆(v)

(13)

⇒ w = w¯ + v , where v satisfies: ⟨g,s⟩ = ⟨g,L∆(v)⟩, ∀g ∈ W ,

⇒ w = w¯ + v , where v satisfies:

[acbc∇v · ∇g + ccvg] dx, ∀g ∈ W ,

sg dx =

Dw

Dw

where the last two equations spell out the weak form definition of L∆ that can be solved using the finite element method.

In terms of the numerical implementation, consider a finite element mesh Dwh and finite element function space Vh ⊂ W with dim(Vh) = pw, and proceed as follows:

- 1. Draw s = S(z) ∈ Vh:

- (a) For each i, 1 ≤ i ≤ pw, draw a number si ∼ N(0,1), where N(0,1) is a standard normal probability density on R; and
- (b) Take s = i siϕi, where {ϕi} are the finite element basis functions.


- 2. Solve for v ∈ Vh such that L∆(w) = s in Vh:

- (a) Assemble matrix and load vector from the variational form

Dw

sg dx =

Dw

[acbc∇v · ∇g + ccvg] dx, (14)

where v ∈ Vh and g ∈ Vh are trial and test functions, respectively; and

- (b) Solve the underlying matrix problem to get v ∈ Rpw and v = i viϕi.


- 3. A new sample w is then w = w¯ + v.
- 4. Optionally, since the state space Vh is finite-dimensional, compute the negative log of probability density π(w) using


−log π(w) = ||w − w¯||C + const.

= ⟨C−1/2(w − w¯),C−1/2(w − w¯)⟩W + const.

= ⟨C−1/2C1/2s,C−1/2C1/2s⟩W + const.

= ⟨s,s⟩W + const.

= s · (Ms) + const.

(15)

ϕiϕj dx. In Listing 1, the above algorithm is implemented using a python library FEniCS Alnæs et al. (2015). In Figure 2, results from Gaussian sampler with parameters ac = 0.01, cc = 0.2, inhomogeneous diffusivity function bc, and zero mean w¯ = 0 ∈ W are shown.

#### where M is the mass matrix such that Mij = D

w

- 1 ...

- 2 import numpy as np

- 3 import dolfin as dl

- 4 ...

- 5

- 6 class PriorSampler:

- 7

- 8 def __init__(self, V, gamma, delta, seed = 0):

- 9 ...

- 10 # function space

- 11 self.V = V

- 12

- 13 # vertex to dof vector and dof vector to vertex maps

- 14 self.V_vec2vv, self.V_vv2vec = build_vector_vertex_maps(self.V)

- 15 ...

- 16 self.a_form = self.a*self.b_fn\

- 17 *dl.inner(dl.nabla_grad(self.u_trial), \

- 18 dl.nabla_grad(self.u_test))*dl.dx \

- 19 + self.c*self.u_trial*self.u_test*dl.dx

- 20 self.L_form = self.s_fn*self.u_test*dl.dx

- 21 ...

- 22

- 23 def assemble(self):

- 24 self.lhs = dl.assemble(self.a_form)

- 25 self.rhs = dl.assemble(self.L_form)

- 26

- 27 def __call__(self, m = None):

- 28 # forcing term

- 29 self.s_fn.vector().zero()

- 30 self.s_fn.vector().set_local(np.random.normal(0.,1.,self.s_dim))

- 31 ...

- 32 # assemble (no need to reassemble A) --> if diffusion is changed, then A would have been assembled at that time

- 33 self.rhs = dl.assemble(self.L_form)

- 34

- 35 # solve

- 36 self.u_fn.vector().zero()

- 37 dl.solve(self.lhs, self.u_fn.vector(), self.rhs)

- 38

- 39 # add mean

- 40 self.u_fn.vector().axpy(1., self.mean_fn.vector())

- 41

- 42 # vertex_dof ordered

- 43 self.u = self.u_fn.vector().get_local()[self.V_vec2vv]

- 44 ...

- 45 if m is not None:

- 46 m = self.u.copy()

- 47 return m

- 48 else:

- 49 return self.u.copy() Listing 1: Generating random functions with Gaussian measure.


![image 2](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile2.png)

![image 3](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile3.png)

(a) Diffusivity bc in L∆ (b) Random samples

Figure 2: Random samples w using Gaussian measure based on a Laplacian-like operator L∆ defined in (11).

### 3. Model problems

Neural operators will be discussed in the context of solving two PDE-based problems. These are presented in the following two subsections. 3.1. Poisson problem

Consider a two dimensional domain Du = (0,L1) × (0,L2) ⊂ R2 and suppose u : Du → R denotes the temperature field. The balance of energy governs it via the differential equation:

−∇ · (m(x)∇u(x)) = f(x), ∀x ∈ Du ,

u(x) = 0, ∀x ∈ Γud , m(x)∇u(x) · n(x) = q(x), ∀x ∈ Γun ,

(16)

where Γud := {x ∈ ∂Du : x1 < L1} (i.e., all sides except the right side of the rectangular domain) and Γun := ∂Du−Γud. Here, f(x) is the specified heat source (J/m3/s), m(x) diffusivity (J/K/m/s), n(x) unit outward normal, and q(x) specified heat flux (J/m2/s). To be consistent with the notations in Section 2.1, here Dm = Dw = Du (domains of functions m, w (w to be introduced shortly), and u), qw = qm = qu = 2 (dimensions of the domains of functions), and dm = dw = du = 1 (dimensions of the pointwise values of functions). The appropriate function spaces for diffusivity and temperature are:

M := m : Dm → R+ : ∥m∥L2 < ∞ and U := u ∈ H1(D;R) : u(x) = 0 ∀x ∈ Γud . (17) The diffusivity field m is assumed to be the unknown and uncertain parameter field. To ensure that m is a positive function (diffusivity can not be zero or negative), consider a random field

Z : Ω → W := L2(Dw;R) (with Dw = Dm = Du) and suppose the associated measure µZ on W is Gaussian N(0,C) (0 mean and C covariance operator defined in Section 2.4.1 with parameters ac,bc,cc). Now, given a sample w = Z(z) ∈ W, sample m = Q(z) is computed as follows:

Q(z) = m = αm exp(w) + βm , where z ∈ Ω,w = Z(z), and µZ = N(0,C). (18)

Here, αm and βm are constants. The generation of samples w is discussed in Section 2.4, and given w, computing m using the formula above is straightforward; see transform_gaussian_pointwise() in Listing 3.

Finally, given m ∈ M, let F(m) = u ∈ U be the solution of boundary value problem (BVP)

(16), i.e., F : M → U is the solution/forward operator. 3.1.1. Setup details and data generation

Let L1 = L2 = 1, and consider following for f and q

f(x) = 1000(1 − x2)x2(1 − x1)2 and q(x) = 50sin(5πx2). (19) For the covariance operator C in µZ = N(0,C), it is taken to be C = L−∆2, where L∆ is defined in

(11). The parameters in L∆ and transformation of w into m take the following values: ac = 0.005, bc = 1, cc = 0.2, αm = 1, βm = 0. (20)

Data for neural operator training is generated using finite element discretization with triangle elements and linear interpolation for both input and output functions. The number of elements, the nodes in the mesh, and the number of degrees of freedom for u and m are 5000, Nnodes = 2601, and pm = pu = 2601, respectively. Listing 3 details the setup and solution of the Poisson model problem (16) building on the abstract class shown in Listing 2. The sampling of uncertain parameter m = αm exp(w) + βm ∼ µQ, where w ∼ µZ = N(0,C), is straight-forward using the method and implementation of sampling w ∼ µZ discussed in Section 2.4.1 and Listing 1. In Figure 3a, samples of w and corresponding (m,u) pairs are shown. The notebook Poisson.ipynb2 implements methods to generate and post-process data for neural operator training.

- 1 import numpy as np

- 2 import dolfin as dl

- 3 from fenicsUtilities import build_vector_vertex_maps

- 4

- 5 class PDEModel:

- 6

- 7 def __init__(self, Vm, Vu, \

- 8 prior_sampler, seed = 0):

- 9 ...

- 10 # prior and transform parameters

- 11 self.prior_sampler = prior_sampler

- 12

- 13 # FE setup

- 14 self.Vm = Vm

- 15 self.Vu = Vu

- 16 self.mesh = self.Vm.mesh()


2https://github.com/CEADpx/neural_operators/blob/survey25_v1/survey_work/problems/ poisson/Poisson.ipynb

- 17 ...

- 18 # vertex to dof vector and dof vector to vertex maps

- 19 self.Vm_vec2vv, self.Vm_vv2vec = build_vector_vertex_maps(self.Vm)

- 20 self.Vu_vec2vv, self.Vu_vv2vec = build_vector_vertex_maps(self.Vu)

- 21 ...

- 22 # variational form

- 23 self.u_trial = None

- 24 self.u_test = None

- 25 self.a_form = None

- 26 self.L_form = None

- 27 self.bc = None

- 28 self.lhs = None

- 29 self.rhs = None

- 30

- 31 def empty_u(self):

- 32 return np.zeros(self.u_dim)

- 33

- 34 def empty_m(self):

- 35 return np.zeros(self.m_dim)

- 36

- 37 # following functions must be defined in the inherited class

- 38 # boundaryU(x, on_boundary)

- 39 # is_point_on_dirichlet_boundary(x)

- 40 # assemble(self, assemble_lhs = True, assemble_rhs = True)

- 41 # empty_u(self)

- 42 # compute_mean(self, m)

- 43 # solveFwd(self, u = None, m = None, transform_m = False)

- 44 # samplePrior(self, m = None, transform_m = False) Listing 2: Abstract PDE class


- 1 ...

- 2 import dolfin as dl

- 3 ...

- 4 from pdeModel import PDEModel

- 5 ...

- 6

- 7 class PoissonModel(PDEModel):

- 8 def __init__(self, Vm, Vu, \

- 9 prior_sampler, \

- 10 logn_scale = 1., \

- 11 logn_translate = 0., \

- 12 seed = 0):

- 13 super().__init__(Vm, Vu, prior_sampler, seed)

- 14 # prior transform parameters

- 15 self.logn_scale = logn_scale

- 16 self.logn_translate = logn_translate

- 17

- 18 # Boundary conditions

- 19 self.f = dl.Expression("1000*(1-x[1])*x[1]*(1-x[0])*(1-x[0])", degree=2)

- 20 self.q = dl.Expression("50*sin(5*pi*x[1])", degree=2)

- 21

- 22 # store transformed m where input is from Gaussian prior

- 23 self.m_mean = self.compute_mean(self.m_mean)

- 24

- 25 # input and output functions (will be updated in solveFwd)

- 26 self.m_fn = dl.Function(self.Vm)


- 27 self.m_fn = self.vertex_to_function(self.m_mean, self.m_fn, is_m = True)

- 28 self.u_fn = dl.Function(self.Vu)

- 29

- 30 # variational form

- 31 ...

- 32 self.a_form = self.m_fn*dl.inner(dl.nabla_grad(self.u_trial), dl.nabla_grad( self.u_test))*dl.dx

- 33 self.L_form = self.f*self.u_test*dl.dx \

- 34 + self.q*self.u_test*dl.ds # boundary term

- 35

- 36 self.bc = [dl.DirichletBC(self.Vu, dl.Constant(0), self.boundaryU)]

- 37

- 38 # assemble matrix and vector

- 39 self.assemble()

- 40

- 41 @staticmethod

- 42 def boundaryU(x, on_boundary):

- 43 return on_boundary and x[0] < 1. - 1e-10

- 44

- 45 @staticmethod

- 46 def is_point_on_dirichlet_boundary(x):

- 47 # locate boundary nodes

- 48 tol = 1.e-10

- 49 if np.abs(x[0]) < tol \

- 50 or np.abs(x[1]) < tol \

- 51 or np.abs(x[0] - 1.) < tol \

- 52 or np.abs(x[1] - 1.) < tol:

- 53 # select all boundary nodes except the right boundary

- 54 if x[0] < 1. - tol:

- 55 return True

- 56 return False

- 57

- 58 def assemble(self, assemble_lhs = True, assemble_rhs = True):

- 59 if assemble_lhs or self.lhs is None:

- 60 self.lhs = dl.assemble(self.a_form)

- 61 if assemble_rhs or self.rhs is None:

- 62 self.rhs = dl.assemble(self.L_form)

- 63

- 64 for bc in self.bc:

- 65 if assemble_lhs and assemble_rhs:

- 66 bc.apply(self.lhs, self.rhs)

- 67 elif assemble_rhs:

- 68 bc.apply(self.rhs)

- 69 elif assemble_lhs:

- 70 bc.apply(self.lhs)

- 71

- 72 def transform_gaussian_pointwise(self, w, m_local = None):

- 73 if m_local is None:

- 74 self.m_transformed = self.logn_scale*np.exp(w) + self.logn_translate

- 75 return self.m_transformed.copy()

- 76 else:

- 77 m_local = self.logn_scale*np.exp(w) + self.logn_translate

- 78 return m_local

- 79

- 80 def compute_mean(self, m):

- 81 return self.transform_gaussian_pointwise(self.prior_sampler.mean, m)


- 82

- 83 def solveFwd(self, u = None, m = None, transform_m = False):

- 84 ...

- 85 # reassamble (don’t need to reassemble L)

- 86 self.assemble(assemble_lhs = True, assemble_rhs = False)

- 87

- 88 # solve

- 89 dl.solve(self.lhs, self.u_fn.vector(), self.rhs)

- 90

- 91 return self.function_to_vertex(self.u_fn, u, is_m = False)

- 92

- 93 def samplePrior(self, m = None, transform_m = False):

- 94 if transform_m:

- 95 self.m_transformed = self.transform_gaussian_pointwise(self.prior_sampler ()[0], self.m_transformed)

- 96 else:

- 97 self.m_transformed = self.prior_sampler()[0]

- 98

- 99 if m is None:

- 100 return self.m_transformed.copy()

- 101 else:

- 102 m = self.m_transformed.copy()

- 103 return m


Listing 3: Class for the Poisson problem. It takes random parameter field sampler and function spaces as input, defines the variational forms, and provides a method to solve for the state variable given the input parameter field.

![image 4](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile4.png)

![image 5](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile5.png)

(a) Poisson problem (b) Linear elasticity problem

Figure 3: Some representative data samples for Poisson (a) and linear elasticity (b) problems.

3.2. Linear elasticity problem

The second problem concerns the in-plane deformation of the thin plate with the center plane given by Du = (0,L1) × (0,L2) ⊂ R2. Suppose E(x) is the Young’s modulus at a point x ∈ Du and ν Poisson ratio, u = (u1,u2) : Du → R2 displacement field, e(x) = sym(∇u) = (∇u + ∇uT)/2 linearized strain, σ(x) Cauchy stress, and b(x) body force per unit volume. The equation for u is

based on the balance of linear momentum and reads:

−∇ · σ(x) = b(x), ∀x ∈ Du , σ(x) = λ(x)eiiI + 2µ(x)e, ∀x ∈ Du , u(x) = 0, ∀x ∈ Γud ,

(21)

σ(x)n(x) = t(x), ∀x ∈ Γuq , σ(x)n(x) = 0, ∀x ∈ ∂Du − Γuq − Γud ,

where I is the identity second order tensor, and λ and µ are Lam´e parameters and are related to E and ν as follows:

E(x)ν (1 + ν)(1 − 2ν)

E(x) 2(1 + ν)

λ(x) =

and µ(x) =

. (22)

In (21), Γud := {x ∈ ∂Du : x1 = 0} and Γuq := {x ∈ ∂Du : x1 = L1}, n unit outward normal, and t is the specified traction on the right edge of the domain. The scalar field E ∈ M is considered to be uncertain, and the forward map F : M → U is defined such that given E ∈ M, F(m) = u ∈ U solves the BVP (21). To be consistent with the notations, here Dw = Dm = Du, qw = qm = qu = 2, dw = dm = 1, and du = 2. Appropriate function spaces for the parameter field and solution are as follows:

M := m : Dm → R+ : ∥m∥L2 < ∞ and U := u ∈ H1(Du;R2) : u(x) = 0 ∀x ∈ Γud . (23)

As in the case of the Poisson problem, the samples of E are generated by transforming the Gaussian samples, i.e.,

Q(z) = E = αm exp(w) + βm , where z ∈ Ω,w = Z(z), and µZ = N(0,C). (24) 3.2.1. Setup details and data generation

Let L1 = L2 = 1, and consider following for b and t b(x) = 0ˆe1 + 0ˆe2 and t(x) = 0ˆe1 + 10ˆe2 . (25)

The covariance operator in N(0,C) is taken to be L−∆2, where L∆ is defined in (11), and parameters in L∆ and parameters associated with the transformation of w into m are given by

ac = 0.005, bc = 1, cc = 0.2, αm = 100, βm = 1000. (26)

As in the case of the Poisson problem, finite element approximation with triangle elements and linear interpolation is utilized for both the input and output functions. The number of elements, the nodes in the mesh, and the number of degrees of freedom for u and m are 5000, Nnodes = 2601, pu = 5202, and pm = 2601, respectively. Listing 4 outlines crucial steps in solving the problem. The sampling of E is similar to m in problem 1. Figure 3b shows representative samples of w and corresponding (m,u) pair. The notebook LinearElasticity.ipynb3 implements methods to generate and post-process data for neural operator training.

3https://github.com/CEADpx/neural_operators/blob/survey25_v1/survey_work/problems/ linear_elasticity/LinearElasticity.ipynb

- 1 ...

- 2 from pdeModel import PDEModel

- 3

- 4 class LinearElasticityModel(PDEModel):

- 5

- 6 def __init__(self, Vm, Vu, \

- 7 prior_sampler, \

- 8 logn_scale = 1., \

- 9 logn_translate = 0., \

- 10 seed = 0):

- 11 ...

- 12 self.bc = [dl.DirichletBC(self.Vu, dl.Constant((0,0)), self.boundaryU)]

- 13

- 14 facets = dl.MeshFunction("size_t", self.mesh, self.mesh.topology().dim()-1)

- 15 dl.AutoSubDomain(self.boundaryQ).mark(facets, 1)

- 16 self.ds = dl.Measure("ds", domain=self.mesh, subdomain_data=facets)

- 17 ...

- 18 self.nu = 0.25

- 19 self.lam_fact = dl.Constant(self.nu / (1+self.nu)*(1-2*self.nu))

- 20 self.mu_fact = dl.Constant(1/(2*(1+self.nu)))

- 21

- 22 self.spatial_dim = self.u_fn.geometric_dimension()

- 23 self.a_form = self.m_fn*dl.inner(self.lam_fact*dl.tr(dl.grad(self.u_trial))*dl

.Identity(self.spatial_dim) \

- 24 + 2*self.mu_fact * dl.sym(dl.grad(self.u_trial )), \

- 25 dl.sym(dl.grad(self.u_test)))*dl.dx

- 26

- 27 self.L_form = dl.inner(self.b, self.u_test)*dl.dx + dl.inner(self.t, self. u_test)*self.ds

- 28 ...

- 29

- 30 ...

- 31 def solveFwd(self, u = None, m = None, transform_m = False):

- 32 # similar to the solveFwd() in Listing 3

- 33

- 34 def samplePrior(self, m = None, transform_m = False):

- 35 # similar to the samplePriors() in Listing 3


Listing 4: Class for the linear elastic problem. Here, only the initialization part is shown, as all other functions are similar to the implementation of the Poisson problem in Listing 3.

### 4. Neural networks as surrogate of the forward problem

Over the years, several neural operator architectures have been introduced that leverage neural networks to build fast and efficient approximations of F. This section considers a few key neural operators, extracts core ideas and implementation details, and creates a strong working knowledge,

- as done in the subsequent sub-sections. The following three subsections will introduce and go into implementation details of DeepONet,


PCANet, and FNO. 4.1. Deep Operator Network (DeepONet)

DeepONet was first introduced in Lu et al. (2019), and over the years, various extensions of the general framework and applications have been realized, e.g., Lu et al. (2021b); Goswami et al.

| | |
|---|---|


Figure 4: Schematics of three neural operators, DeepONet, PCANet, and FNO. Grey and light green circles represent the input and output of neural operators. The blue box includes a parameterized neural network-based map. In this work, the blue boxes for DeepONet and PCANet employ multilayer perceptron fully-connected neural networks. In the case of FNO, trainable parameters (namely, Rl, Wl, bl) appear within each Fourier layer.

(2023). Consider some m, and suppose {ϕu}pi=1u ⊂ U is finite collection of basis functions, then, at x ∈ Du,

F(m)(x) = u(x) ≈ ⟨F(m),ϕui⟩

ϕui(x), (27)

=:αi(m)

where, coefficients αi = αi(m) depend on m. DeepONet’s underlying idea is to learn the above finite-dimensional representation of the output of operator F. That is, identify the linear bases or

more precisely learn the values of basis functions ϕui(x) at coordinates x ∈ Du, and the coefficients associated with the bases dependent on the input m, {αi(m)} so that i αi(m)ϕui(x) is approximately equal to F(m)(x) = u(x). Towards this, DeepONet considers two neural networks, so-called

branch and trunk networks; see Figure 4. The branch network takes discretization of the input function, denoted by m ∈ Rpm, and the neural network produces Nbr number of coefficients, which are used as {αi}Ni=1br. On the other hand, the trunk network takes as input the spatial coordinate, x, and outputs Ntr numbers, which play the role of {ϕui(x)}Ni=1tr in (27). Here, m and u are assumed to be scalar fields, and Ntr = Nbr. Finally, the loss function is defined in terms of the norm of the difference between the ground truth and approximation by the joint output from the branch and trunk networks, Ni=1br αi(m)ϕui(x). In summary, the operator approximation in DeepONet takes the form, for m ∈ Rpm and x ∈ Du,

Nbr

FNOp(m)(x) =

αi(m;θbr)ϕui(x;θtr) + b, (28)

i=1

where

- (i) αi = αi(m;θbr), 1 ≤ i ≤ Nbr, are outputs of the branch network with θbr neural network trainable parameters,
- (ii) ϕui(x;θtr), 1 ≤ i ≤ Ntr = Nbr, are outputs of the trunk network with θtr neural network trainable parameters, and
- (iii) b ∈ Rdo is a bias. Here, do is the dimension of the pointwise value of the output function u, i.e., do is such that u(ξ) ∈ Rdo.


As mentioned in several works Lu et al. (2021b); Goswami et al. (2023), it is interesting to note how the learning of the coefficients and learning pointwise values of bases are separated via branch and trunk networks. Another crucial property of DeepONet is that an approximation of u = F(m)

- at any arbitrary point x ∈ Ωu can be computed.


4.1.1. Implementation of DeepONet

To simplify the presentation, the input and output functions, m ∈ M and u ∈ U, respectively, are assumed to be scalar-valued, and these functions are appropriately discretized, e.g., using finite element approximation. Extending the cases when one or both of these functions are vector-valued is trivial; see Remark 1.

Let m ∈ Rpm and u = F(m) ∈ Rpu are input and output (discretized) functions, F is the discretization of the operator F of interest. The following constitutes data for DeepONet:

- 1. Consider the Nm × pm-matrix, Xbr, where Nm is the number of input function samples and Ith row of Xbr is the sample mI ∈ Rpm. Each row of Xbr will be the input to the branch network.
- 2. Select Nx number of locations, {xI}NI=1x , where xI ∈ Du ⊆ Rqu and qu is the dimension of the domain. Each location xI will be the input to the trunk neural network so that the output of DeepONet is the prediction of the value of the target function at xI. In the present implementation, the typical input coordinate xI corresponds to the Ith discretization grid or nodes of a mesh so that the value of the output function u at xI is simply the element uI in the vector u corresponding to that grid/node. The matrix Xtr of size Nx × qu is the data for the trunk network, and each row of Xtr is the input to the trunk network.


- 3. Nm×Nx-matrix Y , such that an element YIJ is the value of output data uI(xJ) = F(mI)(xJ).


I.e., YIJ is the value of the output data function uI corresponding to the branch network input data function mI (Ith row of Xbr) at trunk network input location xJ (Jth row of Xtr).

Next, the goal is to find the combined training parameters θ = {θbr,θtr,b} ∈ RNθ such that the error is minimized:

2

θ∗ = arg min

θ={θbr,θtr,b}∈RNθ

Nm

Nx

1 NmNx

I=1

J=1

YIJ −

Nbr

αk(mI;θbr)ϕuk(xJ;θtr) + b

k=1

DeepONet output

. (29)

Remark 1. The DeepONet framework described so far can be easily extended to the case when the target function of the operator is vector-valued. Suppose u(x) = (u1(x),u2(x),...,udo(x)) ∈ Rdo, uj being the components. The approach used in this work is as follows. Suppose Ntr is the number of outputs from the trunk network. Then the branch network is designed to produce Nbr = doNtr outputs, and the prediction, upred = (upred,1,upred,2,...,upred,do), of u, for xJ row of Xtr and mI row of Xbr, is given by

- upred,1 =

Ntr

k=1

αk(mI;θb)ϕuk(xJ;θt) + b1

- upred,2 =


Ntr

αk+Ntr(mI;θb)ϕuk(xJ;θt) + b2 ··· ,

k=1

Ntr

αk+(do−1)Ntr(mI;θb)ϕuk(xJ;θt) + bdo ,

upred,do =

k=1

(30)

i.e., the first Ntr outputs of the branch are used to predict u1 component, the next Ntr branch outputs are used to predict u2 component, and so on. In the above, the same trunk outputs are used for all components of the target functions.

Multi-layer perception (MLP) is used as branch and trunk networks. The implementation used in this work is based on the DeepONet Github repository4 with some minor modifications. Listing 5 shows the implementation of MLP and Listing 6 implements the DeepONet framework.

- 1

- 2 import torch

- 3 import torch.nn as nn

- 4

- 5 class MLP(nn.Module):

- 6

- 7 def __init__(self, input_size, hidden_size, num_classes, depth, act):

- 8 super(MLP, self).__init__()

- 9 self.layers = nn.ModuleList()


4https://github.com/GideonIlung/DeepONet

- 10 self.act = act

- 11

- 12 # input layer

- 13 self.layers.append(nn.Linear(input_size, hidden_size))

- 14

- 15 # hidden layers

- 16 for _ in range(depth - 2):

- 17 self.layers.append(nn.Linear(hidden_size, hidden_size))

- 18

- 19 # output layer

- 20 self.layers.append(nn.Linear(hidden_size, num_classes))

- 21

- 22 def forward(self, x, final_act=False):

- 23 for i in range(len(self.layers) - 1):

- 24 x = self.act(self.layers[i](x))

- 25

- 26 # last layer

- 27 x = self.layers[-1](x)

- 28 if final_act == False:

- 29 return x

- 30 else:

- 31 return torch.relu(x) Listing 5: Multilayer Perceptron (MLP) implementation following DeepONet Github repository4


- 1 ...

- 2 import torch

- 3 import torch.nn as nn

- 4 from torch_mlp import MLP

- 5 ...

- 6

- 7 class DeepONet(nn.Module):

- 8

- 9 def __init__(self, ...):

- 10

- 11 super(DeepONet, self).__init__()

- 12 ...

- 13 # branch network

- 14 self.branch_net = MLP(input_size=num_inp_fn_points, \

- 15 hidden_size=num_neurons, \

- 16 num_classes=num_br_outputs, \

- 17 depth=num_layers, \

- 18 act=act)

- 19 self.branch_net.float()

- 20

- 21 # trunk network

- 22 self.trunk_net = MLP(input_size=out_coordinate_dimension, \

- 23 hidden_size=num_neurons, \

- 24 num_classes=num_tr_outputs, \

- 25 depth=num_layers, \

- 26 act=act)

- 27 self.trunk_net.float()

- 28

- 29 # bias added to the product of branch and trunk networks

- 30 self.bias = [nn.Parameter(torch.ones((1,)),requires_grad=True) for i in range( num_Y_components)]

- 31 ...


- 32 # record losses

- 33 self.train_loss_log = []

- 34 self.test_loss_log = []

- 35

- 36 def convert_np_to_tensor(self,array):

- 37 if isinstance(array, np.ndarray):

- 38 tensor = torch.from_numpy(array)

- 39 return tensor.to(torch.float32)

- 40 else:

- 41 return array

- 42

- 43 def forward(self, X, X_trunk):

- 44

- 45 X = self.convert_np_to_tensor(X)

- 46 X_trunk = self.convert_np_to_tensor(X_trunk)

- 47

- 48 branch_out = self.branch_net.forward(X)

- 49 trunk_out = self.trunk_net.forward(X_trunk,final_act=True)

- 50

- 51 if self.num_Y_components == 1:

- 52 output = branch_out @ trunk_out.t() + self.bias[0]

- 53 else:

- 54 # when d_o > 1, split the branch output and compute the product

- 55 output = []

- 56 for i in range(self.num_Y_components):

- 57 output.append(branch_out[:,i*self.num_tr_outputs:(i+1)*self. num_tr_outputs] @ trunk_out.t() + self.bias[i])

- 58

- 59 # stack and reshape

- 60 output = torch.stack(output, dim=-1)

- 61 output = output.reshape(-1, X_trunk.shape[0] * self.num_Y_components)

- 62

- 63 return output

- 64

- 65 def train(self, train_data, test_data, batch_size=32, epochs = 1000, lr=0.001,

...):

- 66 ...

- 67 # loss and optimizer setup

- 68 criterion = nn.MSELoss()

- 69 optimizer = optim.Adam(self.parameters(), lr=lr, weight_decay=1e-4)

- 70 scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=100, gamma=0.5)

- 71 ...

- 72 # training and testing loop

- 73 start_time = time.perf_counter()

- 74

- 75 self.trainable_params = sum(p.numel() for p in self.parameters() if p. requires_grad)

- 76 ...

- 77 for epoch in range(1, epochs+1):

- 78 ...

- 79 # training loop

- 80 for X_train, _, Y_train in dataloader:

- 81 ...

- 82 # clear gradients

- 83 optimizer.zero_grad()

- 84


- 85 # forward pass through model

- 86 Y_train_pred = self.forward(X_train, X_trunk)

- 87

- 88 # compute and save loss

- 89 loss = criterion(Y_train_pred, Y_train)

- 90 train_losses.append(loss.item())

- 91

- 92 # backward pass

- 93 loss.backward()

- 94

- 95 # update parameters

- 96 optimizer.step()

- 97

- 98 # update learning rate

- 99 scheduler.step()

- 100

- 101 # testing loop

- 102 with torch.no_grad():

- 103 for X_test, _, Y_test in test_dataloader:

- 104

- 105 # forward pass through model

- 106 Y_test_pred = self.forward(X_test, X_trunk)

- 107

- 108 # compute and save test loss

- 109 test_loss = criterion(Y_test_pred, Y_test)

- 110 test_losses.append(test_loss.item())

- 111

- 112 # log losses

- 113 self.train_loss_log[epoch-1, 0] = np.mean(train_losses)

- 114 self.test_loss_log[epoch-1, 0] = np.mean(test_losses)

- 115 ...

- 116 def predict(self, X, X_trunk):

- 117 with torch.no_grad():

- 118 return self.forward(X, X_trunk) Listing 6: DeepONet implementation


- 4.1.2. Architecture and preliminary results A four-layer fully connected network is considered for both the branch and trunk networks.


Neural network and optimization-related parameters are tabulated in Table 2. For the linear elasticity problem, Nbr = 200 and Ntr = 100, and the formula for the prediction of a vector-valued is based on Remark 1.

For the Poisson problem, Figure 5 shows the typical prediction error using the DeepONet. In Figure 6, the results for the linear elasticity problem are shown. These figures also compare the accuracy of PCANet and FNO, which will be discussed in the following two subsections. The notebooks DeepONet-Poisson5 and DeepONet-Linear Elasticity6 show the steps involved in instantiating DeepONet and training and testing.

- 5https://github.com/CEADpx/neural_operators/blob/survey25_v1/survey_work/problems/

poisson/DeepONet/training_and_testing.ipynb

- 6https://github.com/CEADpx/neural_operators/blob/survey25_v1/survey_work/problems/


linear_elasticity/DeepONet/training_and_testing.ipynb

|Parameter|Value|Description|
|---|---|---|
|Layers|4|Number of layers in DeepONet (branch and trunk each)|
| | |and PCANet|
|Hidden layer width|128|Number of neurons in hidden layers|
|Ntrain, Ntest|3500, 1000|Number of training and testing pairs (mI,uI)|
|Nm|3500|Nm is same as Ntrain (notation used for DeepONet);|
|Nx|2601|Number of coordinates for evaluation of u (DeepONet)|
|pm, pu|2601, 2601do|Dimensions of discretized functions;|
| | |do = 1 for Poisson and do = 2 for linear elasticity|
|rm, ru|100, 100|Reduced dimensions for the Poisson problem (PCANet)|
|rm, ru|50, 50|Reduced dimensions for the elasticity problem (PCANet)|
|Nbr, Ntr|100do, 100|Number of branch and trunk outputs in DeepONet|
|Batch size|20|Neural networks are trained on “batch size” samples|
|Batch size (FNO)|20|Batch size specifically for FNO|
|Epochs|1000|Number of optimization steps|
|Epochs (FNO)|500|Number of optimization steps specifically for FNO|
|Learning rate|0.001|A parameter controlling the parameter update in|
| | |gradient-based methods|
|Activation|ReLU|Activation function|
|dh|20|Dimension of FNO layer outputs|
|L|3|Number of FNO layers|
|kmax|8|Number of Fourier modes to keep in FNO|
|n1, n2|51, 51|Number of grid points in grid mesh of Du = (0,1)2 for FNO|


##### Table 2: Summary of various parameters used in neural operator training and testing calculations.

![image 6](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile6.png)

![image 7](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile7.png)

![image 8](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile8.png)

![image 9](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile9.png)

![image 10](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile10.png)

![image 11](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile11.png)

![image 12](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile12.png)

![image 13](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile13.png)

![image 14](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile14.png)

![image 15](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile15.png)

![image 16](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile16.png)

![image 17](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile17.png)

![image 18](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile18.png)

![image 19](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile19.png)

![image 20](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile20.png)

![image 21](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile21.png)

![image 22](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile22.png)

![image 23](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile23.png)

![image 24](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile24.png)

![image 25](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile25.png)

- Figure 5: Comparing DeepONet, PCANet, and FNO predictions with the finite element solution for four random samples of diffusivity in the Poisson problem. Here, e is the relative percentage l2 error corresponding to the sample.


- 4.2. Principal Component Analysis-based Neural Operator (PCANet)


The second neural operator of interest is the PCANet introduced in Bhattacharya et al. (2021), which utilizes PCA to reduce the dimensions of input and output functions and poses an operator learning problem in the reduced dimensional spaces, thereby making the learning efficient. Consider {(mI,uI = F(mI))}NI=1 set of paired data, where mI ∈ Rpm and ui ∈ Rpu. Let rm and ru denote the reduced dimensions for input and output functions, respectively, and P˜m ∈ Rrm×pm and P˜u ∈ Rru×pu are the projectors based on SVD for dimension reduction. Learning the approximation of the target map F : Rpm → Rpu becomes challenging if pm and pu are large. Moreover, the complexity of neural networks working with high-dimensional input and output is large. PCANet alleviates these challenges by introducing a low-dimensional approximation of F. Specifically, in PCANet, the dimensions of input and output functions are reduced using SVD, and the neural network between reduced dimensional inputs and outputs is introduced to approximate the mapping. To make this precise, consider a parameterized neural network map F˜θ : Rrm → Rru to construct the

![image 26](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile26.png)

![image 27](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile27.png)

![image 28](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile28.png)

![image 29](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile29.png)

![image 30](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile30.png)

![image 31](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile31.png)

![image 32](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile32.png)

![image 33](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile33.png)

![image 34](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile34.png)

![image 35](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile35.png)

![image 36](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile36.png)

![image 37](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile37.png)

![image 38](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile38.png)

![image 39](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile39.png)

![image 40](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile40.png)

![image 41](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile41.png)

![image 42](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile42.png)

![image 43](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile43.png)

![image 44](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile44.png)

![image 45](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile45.png)

- Figure 6: Comparing DeepONet, PCANet, and FNO predictions with the finite element solution for four random samples of Young’s modulus in the linear elasticity problem. Here, e is the relative percentage l2 error corresponding to the sample.


approximation FNOp of F as follows, for given m ∈ Rpm,





  

   P˜m(m)

Rpu ∋ u = F(m) ≈ FNOp(m) = P˜Tu

F˜θ

)

 

 

=:m˜ (project m)

=:u˜ (low-dim map)

lift u˜

∈ Rpu . (31)

The parameters θ are determined via the optimization problem:

N

1 N

θ∗ = arg min

θ∈Θ

I=1

F(mI) − P˜Tu F˜θ P˜m(mI)

2

, (32)

where ∥·∥ denotes the l2-norm, and Θ ⊂ Rpθ appropriate space of neural networks parameters. Figure 4 presents the schematics of PCANet and the projection steps.

4.2.1. Implementation of PCANet

Let X and Y are two N × pm and N × pu matrices, respectively, such that rows of X and Y are input and output function samples, mI ∈ Rpm and uI ∈ Rpu, where 1 ≤ I ≤ N. The data for neural network-based map F˜ is constructed using the following steps, which include the preprocessing to construct SVD-based projectors:

- 1. Centering and scaling X and Y data by subtracting the mean and dividing (elementwise) the sample standard deviation. E.g., if X¯ and σX are 1 × pm mean and standard deviation matrices, then Xˆ = (X − X¯)/(σX + tol), where the division is element-wise and tol small number. Similarly, Yˆ is obtained.
- 2. SVD projectors for input and output data are determined following the procedure in Section 2.3.1. E.g., take A = XˆT and compute a rm × pm matrix, P˜m, where rm is the specified reduced dimension. Similarly, P˜u can be obtained for the output data.
- 3. Projected data for neural network are computed by taking the rows of Xˆ and projecting them into reduced space. To be specific, let Ith row of matrix Xˆ is (mˆ I)T ∈ R1×pm, where mˆ I is the centered and scaled Ith input sample. Its projection is m˜ I = P˜m(mˆ I) ∈ Rrm. Using the projection, a new matrix X˜ of size N × rm is formed, where (m˜ I)T ∈ R1×rm gives the Ith row of the matrix. Similarly, Y˜ of size N × ru is obtained by transforming each row of Yˆ by applying P˜u.
- 4. For the reduced dimensional map Rru ∋ u˜ = F˜θ(m˜ ), with m˜ ∈ Rrm, X˜ and Y˜ constitutes as input and output data, respectively.


Given data X˜ and Y˜ and a neural network-based map F˜θ, the optimization problem to determine θ is given by

N

1 N

2

Y˜I − F˜θ(X˜I)

θ∗ = arg min

, (33)

θ∈Θ

I=1

where (·)I denotes the Ith row of matrix. The core steps in implementing PCANet, i.e., F˜θ, are shown in Listing 7.

- 1 ...

- 2 import torch

- 3 import torch.nn as nn

- 4 from torch_mlp import MLP

- 5 ...

- 6

- 7 class PCANet(nn.Module):

- 8

- 9 def __init__(self, ...):

- 10

- 11 super(PCANet, self).__init__()

- 12 ...

- 13 # network

- 14 self.net = MLP(input_size=num_inp_red_dim, \

- 15 hidden_size=num_neurons, \


- 16 num_classes=num_out_red_dim, \

- 17 depth=num_layers, \

- 18 act=act)

- 19 self.net.float()

- 20

- 21 # record losses

- 22 self.train_loss_log = []

- 23 self.test_loss_log = []

- 24

- 25 def convert_np_to_tensor(self,array):

- 26 if isinstance(array, np.ndarray):

- 27 tensor = torch.from_numpy(array)

- 28 return tensor.to(torch.float32)

- 29 else:

- 30 return array

- 31

- 32 def forward(self, X):

- 33 X = self.convert_np_to_tensor(X)

- 34 return self.net.forward(X)

- 35

- 36 def train(self, train_data, test_data, batch_size=32, epochs = 1000, lr=0.001,

...):

- 37 ...

- 38 # loss and optimizer setup

- 39 criterion = nn.MSELoss()

- 40 optimizer = optim.Adam(self.parameters(), lr=lr, weight_decay=1e-4)

- 41 scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=100, gamma=0.5)

- 42 ...

- 43 # training and testing loop

- 44 start_time = time.perf_counter()

- 45

- 46 self.trainable_params = sum(p.numel() for p in self.parameters() if p. requires_grad)

- 47 ...

- 48 for epoch in range(1, epochs+1):

- 49 ...

- 50 # training loop

- 51 for X_train, Y_train in dataloader:

- 52

- 53 # clear gradients

- 54 optimizer.zero_grad()

- 55

- 56 # forward pass through model

- 57 Y_train_pred = self.forward(X_train)

- 58

- 59 # compute and save loss

- 60 loss = criterion(Y_train_pred, Y_train)

- 61 train_losses.append(loss.item())

- 62

- 63 # backward pass

- 64 loss.backward()

- 65

- 66 # update parameters

- 67 optimizer.step()

- 68

- 69 # update learning rate


- 70 scheduler.step()

- 71

- 72 # testing loop

- 73 with torch.no_grad():

- 74 for X_test, Y_test in test_dataloader:

- 75

- 76 # forward pass through model

- 77 Y_test_pred = self.forward(X_test)

- 78

- 79 # compute and save test loss

- 80 test_loss = criterion(Y_test_pred, Y_test)

- 81 test_losses.append(test_loss.item())

- 82

- 83 # log losses

- 84 self.train_loss_log[epoch-1, 0] = np.mean(train_losses)

- 85 self.test_loss_log[epoch-1, 0] = np.mean(test_losses)

- 86 ...

- 87 def predict(self, X):

- 88 with torch.no_grad():

- 89 return self.forward(X)


Listing 7: PCANet implementation. The interface is similar to the DeepONet, but with one key difference: PCANet does not require spatial coordinates as input.

- 4.2.2. Architecture and preliminary results A fully connected neural network with four layers is considered for testing the PCANet. Other

parameters, including the reduced dimension, are listed in Table 2. First, the singular values of the input and output data are analyzed. This helps decide the dimension of reduced space so that accuracy is not significantly compromised. In Figure 7, the plots of singular values for the input and output data show a rapid spectrum decay; the figure also shows the singular values at reduced dimensions for input and output data. The prediction and the performance of PCANet for the Poisson and linear elasticity problems are shown in Figure 5 and Figure 6, respectively. The notebooks PCANet-Poisson7 and PCANet-Linear Elasticity8 apply the PCANet to the two problems.

- 4.3. Fourier Neural Operator (FNO)


Fourier neural operator considers the composition of layers, with a typical layer involving affine transformation and an integral kernel operator followed by nonlinear activation; see Li et al. (2020a, 2021); Kovachki et al. (2021). These affine and integral kernel operations are parameterized. While there are multiple choices of integral kernel operator Kovachki et al. (2021), this work uses Fourier transform. Consider the case of Dm = Du = D ⊂ Rq, where qm = qu = q, and the neural operator

- 7https://github.com/CEADpx/neural_operators/blob/survey25_v1/survey_work/problems/

poisson/PCANet/training_and_testing.ipynb

- 8https://github.com/CEADpx/neural_operators/blob/survey25_v1/survey_work/problems/


linear_elasticity/PCANet/training_and_testing.ipynb

![image 46](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile46.png)

![image 47](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile47.png)

(a) Poisson equation (b) Linear elasticity

Figure 7: Singular values of input and output data matrices Xˆ and Yˆ (centered and scaled data). Green and red curves represent the normalized singular values for input and output data, respectively. For both curves, the annotation is displayed close to the 10% (brown dots) and 1% (blue dots), i.e., 0.1 and 0.01 fractions of the largest singular value. The grey dots correspond to the fixed reduced dimensions in PCANet. The rapid decay of singular values shows that both problems are inherently low-dimensional.

approximation FNOp such that





  GL−1 ···G1

  P (m(x))

  

  

u(x) = F(m)(x) ≈ FNOp(m)(x) := Q

GL

)

, (34)

 

 

=z0∈Rdh

=zL∈Rdh

or, concisely,

FNOp = Q ◦ GL ◦ GL−1 ◦ ··· ◦ G1 ◦ P . (35) The map FNOp involves the following operations (see Li et al. (2020a); Kovachki et al. (2023)):

- • Lifting m(x) ∈ Rdm to Rdh, where dh is the dimension of outputs from hidden layers via the trainable matrix P of size dh × dm.
- • Projecting the final hidden layer output zL ∈ Rdh onto Rdu (space of u(x)) via the du × dh matrix Q. Here, Q is also trainable.
- • Application of operators Gl, 1 ≤ l ≤ L, where Gl is defined via:


   Wlzl−1 + bl

   . (36)

Rdh ∋ zl = Gl(zl−1) = σl

#### + Kl(zl−1)

nonlocal operation

linear/local operation

Here, zl−1 is the output of the preceding layer, σl activation function, Wl weight matrix, bl a bias vector, and Kl(·) a integral kernel operator.

Up until now, the map FNOp in Equation (34) with the above definitions of P, Q, Gl, l = 1,...,L, is abstract due to the generality of Kl. The linear operation in (36) captures the local effects on the reconstructed function, while the Kl is designed to capture the non-local effects (interaction with other degrees of freedom) via the integral kernel operation. There are various choices for Kl, as discussed in Kovachki et al. (2023). For example:

- (1) Low-rank Neural Operator (LNO) in which Kl takes the form Kl(z) = rj=1⟨ψ(i),z⟩ϕ(i)(x), where ϕ(i) and ψ(i) are some parameterized functions;
- (2) Graph Neural Operator (GNO) in which Kl = |B(x,r1 )| y

i∈B(x,r) k(x,yi)z(yi), k(·,·) kernel function; and

- (3) Fourier Neural Operator (FNO) maps z to Fourier space, followed by mapping the weighted Fourier modes back to the real space. Since FNO is the main focus of this article, it is discussed in more detail next. Readers are referred to Li et al. (2020a, 2021); Kovachki et al.


(2021) for further discussion of FNO and associated ideas. In FNO, Kl(z), for z ∈ Rdh, takes the form:

Kl(z) = F−1 (RlF(z)) , (37) where

- • F(z) is the Fourier transform applied to each components of z. Only the first kmax modes are retained, so the output of F(z) is in Rd×kmax.
- • Rl applies the weighting to different Fourier modes. Rl is a complex-valued dh × dh × kmax trainable matrix and RlF(z) ∈ Rdh×kmax.
- • F−1(·) ∈ Rdh is the inverse Fourier transform.


Figure 4 displays the FNO framework based on Fourier transforms. Summarizing, the trainable parameters in (34) with the specific forms of Gl and Kl are:

θ := P ∈ Rdh×di ,Q ∈ Rdo×dh , Wl ∈ Rdh×dh ,bl ∈ Rdh ,Rl ∈ Cdh×dh×kmax ,1 ≤ l ≤ L . (38) Finally, in the discrete setting, one evaluates the FNO output at all grid points to have

Rpu ∋ u = F(m) ≈ FNOp(m) := Q(GL (GL−1 ···G1 (P(m)))) , for m ∈ Rpm . (39) The optimization problem to determine θ is given by

Nm

1 Nm

θ∗ = arg min

θ∈Θ

I=1

uI − FNOp(mI) 2 . (40)

4.3.1. Implementation of FNO

The implementation of FNO requires function values at grid locations, and thus, preprocessing is required to obtain the function values at grid points from the finite element field. Suppose Dm = Du = D = (0,1)2 and consider the grid division of closure(D) consisting of n1 and n2 number of points in x1 and x2 directions, respectively. Linear interpolation is used to compute function values at grid points. The following describes the data:

- 1. Let X be N × n1 × n2 × 3 matrix, where the outer dimension corresponds to the number of samples. The element of X at Ith outer index is a n1 × n2 × 3 matrix containing the interpolated values of a function mI at all grid (x1,x2) points and the coordinates x1 and x2 of all grid points; thus, the inner dimension is three. Next, the function values are centered and scaled using the mean and standard deviation computed from the samples 1 ≤ I ≤ N.
- 2. Let Y be N ×n1×n2×do matrix such that the element of Y at Ith outer index is a n1×n2×do matrix containing the interpolated values of do-valued function uI at all grid points. Note that the element of X and Y at Ith outer index corresponds to mI and uI = F(mI) on a grid, thereby establishing the correspondence between input and output. Function values at grid points are also centered and scaled using the sample mean and standard deviation.


Given a sample from X, denoted x = (mI(x1,x2),x1,x2) ∈ R3, it is first lifted into Rdh, where dh > 3 is a dimension of the input and output spaces of FNO layers, to get z0 = P(x) = WP x+bP, where WP ∈ Rdh×3 and bP ∈ Rdh. Next, z0 goes through L FNO layers such that given zl−1 an output of (l−1)th layer, zl = Gl(zl−1). The Listing 8 presents the implementation of an FNO layer Gl based on the Operator-Learning repository9 De Hoop et al. (2022). The lth layer involves a linear transformation zl1 = Wlzl−1 + bl and Fourier-based transformation zL2 = F−1(Rl · F(zl)), where Rl is a complex matrix of size dh ×dh ×kmax ×kmax, kmax denoting the number of Fourier modes that are retained after the Fourier transform. Here, Wl and bl are weight and bias parameters. The output of the final layer zL = GL(zL−1) ∈ Rdh is projected to uNOp(x1,x2) = Q(zL) ∈ Rdo; the projection operator Q introduces WQ ∈ Rdo×dh and bQ ∈ Rdo parameters. In Listing 9, lift, FNO layer applications, and projection are combined to create an FNO model; see the forward method. The trainable parameters are:

θ := (WP,bP) ∈ Rdh×3 × Rdh , (WQ,bQ) ∈ Rdo×dh × Rdo , Wl ∈ Rdh×dh ,bl ∈ Rdh ,Rl ∈ Cdh×dh×kmax×kmax , 1 ≤ l ≤ L .

(41)

It should be noted that extending the above to a vector-valued function (for a linear elasticity problem) as input and output is relatively straightforward.

Before writing the loss function, note that while an input to FNO is a triplet (m(x1,x2),x1,x2), during training and testing, the input is applied in a batch. The FNO is applied to input matrix X of size N × n1 × n2 × 3 altogether, i.e., N samples of mI and grid locations. FNO produces N × n1 × n2 × do outputs, corresponding to N functions uI at all grid locations. Noting this, the optimization problem to train parameters θ reads:

N

1 N n1 n2

θ∗ = arg min

θ∈Θ

I=1

n1

n2

j=1

k=1

uI(x1jk,x2jk) − FNOp(mI)(x1jk,x2jk) 2 . (42)

9https://github.com/Zhengyu-Huang/Operator-Learning

- 1 import torch

- 2 import torch.nn as nn

- 3 import torch.nn.functional as nnF

- 4

- 5 class FNO2DLayer(nn.Module):

- 6 def __init__(self, in_channels, out_channels, \

- 7 modes1, modes2, \

- 8 apply_act = True, \

- 9 act = nnF.gelu):

- 10 super(FNO2DLayer, self).__init__()

- 11 ...

- 12 # parameters in nonlocal transformation

- 13 self.scale = (1 / (in_channels * out_channels))

- 14 self.weights1 = nn.Parameter(self.scale * torch.rand(in_channels, out_channels , self.modes1, self.modes2, dtype = torch.cfloat))

- 15 self.weights2 = nn.Parameter(self.scale * torch.rand(in_channels, out_channels , self.modes1, self.modes2, dtype = torch.cfloat))

- 16

- 17 # parameters in linear transformation

- 18 self.w = nn.Conv2d(self.out_channels, self.out_channels, 1)

- 19

- 20 # complex multiplication

- 21 def compl_mul2d(self, a, b):

- 22 # (batch, in_channel, x,y ), (in_channel, out_channel, x,y) -> (batch, out_channel, x,y)

- 23 op = torch.einsum("bixy,ioxy->boxy",a,b)

- 24 return op

- 25

- 26 def fourier_transform(self, x):

- 27 batchsize = x.shape[0]

- 28

- 29 # compute Fourier coeffcients

- 30 x_ft = torch.fft.rfft2(x)

- 31

- 32 # Multiply relevant Fourier modes

- 33 out_ft = torch.zeros(batchsize, self.out_channels, x.size(-2), x.size(-1)//2

+ 1, device=x.device, dtype=torch.cfloat)

- 34 out_ft[:, :, :self.modes1, :self.modes2] = \

- 35 self.compl_mul2d(x_ft[:, :, :self.modes1, :self.modes2], self.weights1)

- 36 out_ft[:, :, -self.modes1:, :self.modes2] = \

- 37 self.compl_mul2d(x_ft[:, :, -self.modes1:, :self.modes2], self.weights2)

- 38

- 39 # return to physical space

- 40 x = torch.fft.irfft2(out_ft,s=(x.size(-2),x.size(-1)))

- 41 return x

- 42

- 43 def linear_transform(self, x):

- 44 return self.w(x)

- 45

- 46 def forward(self, x):

- 47 x = self.fourier_transform(x) + self.linear_transform(x)

- 48 if self.apply_act:

- 49 return self.act(x)

- 50 else:

- 51 return x Listing 8: Implementation of FNO layer based on Operator-Learning repository9 De Hoop et al. (2022)


- 1 ...

- 2 from torch_fno2dlayer import FNO2DLayer

- 3

- 4 class FNO2D(nn.Module):

- 5 def __init__(self, num_layers, width, \

- 6 fourier_modes1, fourier_modes2, \

- 7 num_Y_components, save_file=None):

- 8 super(FNO2D, self).__init__()

- 9 ...

- 10 # create hidden layers (FNO layers)

- 11 self.fno_layers = nn.ModuleList()

- 12 for _ in range(num_layers):

- 13 self.fno_layers.append(FNO2DLayer(self.width, \

- 14 self.width, \

- 15 self.fourier_modes1, \

- 16 self.fourier_modes2))

- 17

- 18 # no activation in the last hidden layer

- 19 self.fno_layers[-1].apply_act = False

- 20

- 21 # define input-to-hidden projector

- 22 # input has 3 components: m(x,y), x_1, x_2

- 23 self.input_projector = nn.Linear(3, self.width)

- 24

- 25 # define hidden-to-output projector

- 26 # project to the dimension of u(x) \in Rˆd_o

- 27 self.output_projector = nn.Linear(self.width, self.num_Y_components)

- 28

- 29 # record losses

- 30 self.train_loss_log = []

- 31 self.test_loss_log = []

- 32 ...

- 33

- 34 def forward(self, X):

- 35 x = self.convert_np_to_tensor(X)

- 36

- 37 # input-to-hidden projector

- 38 x = self.input_projector(x)

- 39

- 40 # rearrange x so that it has the shape (batch, width, x, y)

- 41 x = x.permute(0, 3, 1, 2)

- 42

- 43 # pass through hidden layers

- 44 for i in range(self.num_layers):

- 45 x = self.fno_layers[i](x)

- 46

- 47 # rearrange x so that it has the shape (batch, x, y, width)

- 48 x = x.permute(0, 2, 3, 1)

- 49

- 50 # hidden-to-output projector

- 51 x = self.output_projector(x)

- 52

- 53 return x

- 54

- 55 def train(self, train_data, test_data, \

- 56 batch_size=32, epochs = 1000, \


- 57 lr=0.001, log=True, \

- 58 loss_print_freq = 100, \

- 59 save_model = False, save_file = None, save_epoch = 100):

- 60 # similar to the train() of Listing 7 (PCANet).

- 61

- 62 def predict(self, X):

- 63 # similar to the predict() of Listing 5. Listing 9: Implementation of FNO


- 4.3.2. Architecture and preliminary results In the implementation, three FNO layers are considered with hidden layer output dimension

dh = 20. Other relevant parameters are listed in Table 2. Figure 5 and Figure 6 display the FNO prediction for test input samples, comparing it with the “ground truth”. FNO training and testing for the two problems are implemented in the following two notebooks: FNO-Poisson10 and FNO-Linear Elasticity11.

- 5. Neural Operators applied to Bayesian inference problems


As an application of neural operator surrogates of the parametric PDEs, the Bayesian inference problem is considered to determine the posterior distribution of the parameter field from the synthetic data. Following the key contributions in this topic Dashti and Stuart (2017); Bui-Thanh et al. (2013); Stuart (2010), the Bayesian inference problem in an abstract setting is discussed. Subsequently, the setup and results for the cases of Poisson and linear elasticity models are considered.

5.1. Abstract Bayesian inference problem in infinite dimensions

Consider a parameter field m ∈ M to be inferred from the data o ∈ Rdo and the corresponding solution of the PDE, u = F(m) ∈ U. Consider the state-to-observable map B¯ : U → Rdo such that B¯(u) gives the prediction of data o given u (u depends on m). It is possible to use the observational data to find the m that produces prediction B¯(u) closely matching the data. In the Bayesian setting, this corresponds to finding the distribution of m such that

o = B¯(u) + η = B¯(F(m)) + η , (43)

where η ∼ N(0,Γo) is the combined noise due to noise in the data and modeling error, and Γo is a do × do covariance matrix. The covariance matrix is assumed to be of the form Γo = σo2I, where σo is the standard deviation and I the do-dimensional identity matrix.

Generally, the admissible space of parameter fields Mad is a subspace of M, and it is obtained by introducing some restrictions on m ∈ M. For example, diffusivity and Young’s modulus parameters in Poisson and linear elasticity problems must be strictly positive at all spatial locations for the

- 10https://github.com/CEADpx/neural_operators/blob/survey25_v1/survey_work/problems/

poisson/FNO/training_and_testing.ipynb

- 11https://github.com/CEADpx/neural_operators/blob/survey25_v1/survey_work/problems/


linear_elasticity/FNO/training_and_testing.ipynb

problem to be well-posed. Focusing on our applications, to ensure m is positive, it is taken as a transformation of w ∈ W as follows

m = αm exp(w) + βm , (44)

where, αm and βm are constants. In what follows, the inference problem is posed on w ∈ W with W assumed to be a Hilbert space and m given by (44). Introducing a parameter-to-observable map B : W → Rdo such that B(w) = B¯(F(m(w))) leads to the problem of finding the probability distribution of w such that

o = B(w) + η . (45)

The above equation prescribes the conditional probability distribution of data o given w. The conditional probability distribution is referred to as likelihood, and using o−B(w) = η, it is given by the translation of N(0,Γo) by B(w), i.e.,

1 det(Γo)(2π)

πlike(o|w) = N(o − B(w),Γo) =

exp −

do 2

- 1

- 2


(o − B(w))TΓ−o 1(o − B(w)) . (46)

It is useful to define a likelihood potential function Φ as follows:

Φ(w) := −log πlike(o|w), (47) where, the data o is assumed to be fixed so that Φ can be seen as a function of w.

Suppose µ⊘ is a Gaussian measure on W with the mean function 0 and covariance operator C, i.e., µ⊘ = N(0,C), and the parameters αm and βm in (44) are assigned some fixed values. This results in the log-normal prior distribution on model parameter field m. The choice of C, αm, and βm is based on the prior knowledge on m.

Bayes’ rule relates the prior measure µ⊘, the likelihood πlike, and posterior measure µo (distribution of w conditioned on data o) as follows:

dµo dµ⊘(w) =

1 Z

πlike(o|w) =

where Z is the normalizing constant given by

1 Z

exp(−Φ(w)) , (48)

Z =

exp(−Φ(w)) dµ⊘(w). (49)

W

Bayes’ rule (48) indicates how the new posterior and prior measures are related. In fact, given

(48), it is straightforward to see

f(w)dµo(w)

Eµo [f] =

W

dµo dµ⊘(w)dµ⊘(w) =

=

f(w)

W

exp(−Φ(·)) Z

= Eµ⊘ f(·)

.

exp(−Φ(w)) Z

dµ⊘(w)

f(w)

W

(50)

5.1.1. Markov chain Monte Carlo (MCMC) method to sample from the posterior measure

To sample from posterior measure µo, i.e., to generate samples w ∈ W with measure µo, there are several algorithms available, see (Cotter et al., 2013, Section 4) and Dashti and Stuart (2017). This work utilizes the preconditioned Crank-Nicolson (pCN) method due to its simplicity. The pCN algorithm based on Cotter et al. (2013) is as follows:

- 1. Compute initial sample w(0) ∼ µ⊘ = N(0,C)
- 2. For 1 ≤ k ≤ kmax

- (a) Propose v(k) = u(k) 1 − β2 + βξ, where ξ ∼ µ⊘

- (b) Compute a = a(w(k),v(k)) = Φ(w(k)) − Φ(v(k)), and draw b ∼ Uniform[0,1]
- (c) If exp(a) > b (equivalently a > log(b)), accept v(k) and set w(k+1) = v(k). Else, w(k+1) = w(k).
- (d) k → k + 1


- 3. Burn initial kburn samples, and take {w(k)}kkmax=kburn+1 as the samples from posterior. The mean of posterior samples is simply


kmax

1 kmax − kburn

w(k) . (51)

w¯ =

k=kburn+1

In the above, β is the hyperparameter. To verify that the algorithm works as intended, consider two cases: (1) when the current sample w(k) has lower cost compared to the proposed sample v(k), i.e., Φ(u(k)) < Φ(v(k)). In this case, exp(a) < 1, and therefore the proposed sample v(k) may be accepted or rejected depending on the draw b. (2) when the proposal has a lower cost compared to the current sample, a > 0 and exp(a) > 1, the proposed sample will be accepted regardless of the draw b.

In Listing 10, the implementation of MCMC based on the pCN method is shown. The core implementation of the pCN method is in functions proposal and sample. The listing also shows the application of surrogate models in computing the forward solution in the solveFwd function.

- 1 ...

- 2 import numpy as np

- 3 ...

- 4 from state import State

- 5 from tracer import Tracer

- 6 ...

- 7

- 8 class MCMC:

- 9 def __init__(self, model, prior, data, sigma_noise, pcn_beta = 0.2, \

- 10 surrogate_to_use = None, surrogate_models = None, seed = 0):

- 11 # model class that provides solveFwd()

- 12 self.model = model

- 13 ...

- 14 # prior class that provides () and logPrior()

- 15 self.prior = prior

- 16

- 17 # data (dict) that provides x_obs, u_obs, m_true, u_true, etc.

- 18 self.data = data


- 19

- 20 # noise (std-dev) in the observations

- 21 self.sigma_noise = sigma_noise

- 22

- 23 # preconditioned Crank-Nicolson parameter

- 24 self.pcn_beta = pcn_beta

- 25 ...

- 26 # current and proposed input parameter and state variables

- 27 self.current = State(self.m_dim, self.u_dim, self.u_obs_dim)

- 28 self.proposed = State(self.m_dim, self.u_dim, self.u_obs_dim)

- 29 self.init_sample = State(self.m_dim, self.u_dim, self.u_obs_dim)

- 30 ...

- 31 # tracer

- 32 self.tracer = Tracer(self)

- 33 self.log_file = None

- 34

- 35 def solveFwd(self, current):

- 36 if self.surrogate_to_use is not None:

- 37 current.u = self.surrogate_models[self.surrogate_to_use].solveFwd(current. m)

- 38 else:

- 39 current.u = self.model.solveFwd(u = current.u, m = current.m, transform_m

= True)

- 40

- 41 return current.u

- 42

- 43 def state_to_obs(self, u):

- 44 # interpolate PDE solution on observation grid

- 45 if self.u_comps == 1:

- 46 return griddata(self.u_nodes, u, self.x_obs, method=’linear’)

- 47 else:

- 48 num_nodes = self.u_nodes.shape[0]

- 49 num_grid_nodes = self.x_obs.shape[0]

- 50 obs = np.zeros(num_grid_nodes*2)

- 51 for i in range(self.u_comps):

- 52 obs[i*num_grid_nodes:(i+1)*num_grid_nodes] = griddata(self.u_nodes, u[ i*num_nodes:(i+1)*num_nodes], self.x_obs, method=’linear’)

- 53

- 54 return obs

- 55

- 56 def logLikelihood(self, current):

- 57 current.u = self.solveFwd(current)

- 58 current.u_obs = self.state_to_obs(current.u)

- 59 current.err_obs = current.u_obs - self.u_obs

- 60 current.cost = 0.5 * np.linalg.norm(current.err_obs)**2 / self.sigma_noise**2

- 61 current.log_likelihood = -current.cost

- 62

- 63 return current.log_likelihood

- 64

- 65 def logPosterior(self, current):

- 66 current.log_prior = self.prior.logPrior(current.m)

- 67 current.log_likelihood = self.logLikelihood(current)

- 68 current.log_posterior = current.log_prior + current.log_likelihood

- 69

- 70 return current.log_posterior

- 71


- 72 def proposal(self, current, proposed):

- 73 # preconditioned Crank-Nicolson

- 74 proposed.m, proposed.log_prior = self.prior(proposed.m)

- 75 return self.pcn_beta * proposed.m + np.sqrt(1 - self.pcn_beta**2) * current.m

- 76

- 77 def sample(self, current):

- 78 # compute the proposed state

- 79 self.proposed.m = self.proposal(current, self.proposed)

- 80 self.proposed.log_posterior = self.logPosterior(self.proposed)

- 81

- 82 # accept or reject (based on -log-likelihood

- 83 alpha = current.cost - self.proposed.cost

- 84 if alpha > np.log(np.random.uniform()):

- 85 current.set(self.proposed)

- 86 return 1

- 87

- 88 return 0

- 89

- 90 def run(self, init_m = None, n_samples = 1000, \

- 91 n_burnin = 100, pcn_beta = 0.2, sigma_noise = 0.01, ...):

- 92 ...

- 93 # run the MCMC

- 94 init_done = False

- 95 for i in range(n_samples + n_burnin):

- 96 # sample

- 97 accept = self.sample(self.current)

- 98

- 99 # postprocess/print

- 100 self.process_and_print(i)

- 101

- 102 if i < n_burnin: continue

- 103

- 104 self.save(i, self.current, accept)

- 105

- 106 # save the final state

- 107 self.tracer.append(i, self.current, accept, force_save=True)

- 108

- 109 # print final message

- 110 end_time = time.perf_counter()

- 111 self.logger(’-’*50)

- 112 self.logger(’MCMC finished in {:.3e}s. \nTotal samples: {:4d}, Accepted samples: {:4d}, Acceptance Rate: {:.3e}, Cost mean: {:.3e}’.format(end_time start_time, n_samples + n_burnin, self.tracer.acceptances, self.tracer. current_acceptance_rate, self.tracer.accepted_samples_cost_mean))

- 113 self.logger(’-’*50) Listing 10: Core functions of MCMC implementation using pCN method


- 5.2. Inference of the diffusivity in Poisson problem This section explores the application of neural operators as a surrogate in the Bayesian in-


ference of the diffusivity field m in the Poisson problem. Suppose that u = F(m) solves the Poisson problem given m, and FNOp(m) is the neural operator approximation of u, where NOp ∈ {DeepONet,PCANet,FNO} The inference problem is posed on the function w ∈ W with m = αm exp(w) + βm to ensure that the diffusivity is positive. The following sub-section presents the prior measure and synthetic data generation, followed by the sub-section on inference results.

![image 48](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile48.png)

Figure 8: Synthetic w and corresponding diffusivity m and the solution u of the Poisson problem. The data o ∈ Rdo with do = 162 is obtained via the interpolation of u on 16 × 16 grid over Du = (0, 1)2.

- 5.2.1. Setup of the forward problem, prior measure, and synthetic data The setup of the forward problem is the same as in Section 3.1.1. For the prior measure µ⊘ on

W, consider the probability measure µZ described in Section 3.1.1. The values of the αm and βm parameters in the transformation of w into m, see (44), and parameters of the covariance operator

C are given in Section 3.1.1. ETheprior measure is the same as the probability measure w ∼ µZ to generate the input data {mI} for the neural operator.

Synthetic data is obtained by taking the specific function w as shown in Figure 8 (see the figure on the left). Corresponding to w, the “true” diffusivity m is obtained by transforming w following (44), and the “true” solution u is obtained. The data o is the values of “true” u on 16 × 16 grid over the domain Du = (0,1)2. In Figure 8, synthetic data along with the w, m, and u fields are plotted; the implementation can be found in the notebook Generate_GroundTruth.ipynb12.

- 5.2.2. Inference results Using the setup, Gaussian prior measure, and synthetic data, MCMC was used to generate the


posterior samples. Parameters of the MCMC simulation are as follows: kmax = 10500, kburn = 500, β = 0.2, and σo = 1.329 (recall that the covariance matrix in the noise model is Γo = σo2I). Here, σo is taken to be 5% of the mean of the o (i.e., σo = 0.05 × d1

do i=1 oi). The same MCMC simulation with four different forward models was performed. In the first case, the state field u was computed using the finite element approximation of the Poisson problem, i.e., using the “true” model. The remaining three simulations utilized DeepONet, PCANet, and FNO neural operator approximations of the forward problem. Here, the trained neural operators from the Section 4 are used; their accuracy for random samples from Gaussian prior measure is shown in Figure 5 for the Poisson problem. The notebook BayesianInversion.ipynb13 sets up the problem, loads trained neural operators, and runs MCMC simulation.

o

Acceptance rate and cost during MCMC simulations for four inference problems corresponding to the “true” and surrogate models are shown in Figure 9. The results, including the posterior mean and a sample from the posterior, from the “true” model are shown in Figure 10. The results with DeepONet, PCANet, and FNO surrogates are shown in Figure 11. Comparing the results when the “true” model is used, all three surrogates produced a posterior mean of w with a slightly

- 12https://github.com/CEADpx/neural_operators/blob/survey25_v1/survey_work/

applications/bayesian_inverse_problem_poisson/Generate_GroundTruth.ipynb

- 13https://github.com/CEADpx/neural_operators/blob/survey25_v1/survey_work/


applications/bayesian_inverse_problem_poisson/BayesianInversion.ipynb

#### higher error. However, the error of posterior mean m obtained using the surrogates is about one percent. This demonstrates that neural operators are robust for the current Bayesian inference problem, even when the target parameter field has features that the prior samples can not produce.

![image 49](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile49.png)

![image 50](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile50.png)

(a) Acceptance rate (b) Cost

Figure 9: Acceptance rate and cost during MCMC simulation for the Poisson problem.

|![image 51](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile51.png)|
|---|


|![image 52](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile52.png)|
|---|


- Figure 10: Bayesian inference of diffusivity in the Poisson problem using the “true” model (numerical approximation of PDE). The top panel shows the synthetic w field used to generate m, the corresponding PDE solution u, and the observation of u at 16 × 16 grid points. The panel below shows the posterior sample and posterior mean using the true model.


|![image 53](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile53.png)|
|---|


|![image 54](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile54.png)|
|---|


|![image 55](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile55.png)|
|---|


##### Figure 11: Comparing the Bayesian inference of diffusivity in the Poisson problem using DeepONet, PCANet, andFNO surrogates. The panels show the posterior sample and posterior mean using different surrogates. These resultsshould be compared with the inference results using the “true” model in Figure 10.

![image 56](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile56.png)

- Figure 12: Synthetic w field and corresponding Young’s modulus field m and the solution u of the linear elasticity problem. The data o ∈ Rdo with do = 2 × 162 is obtained via the interpolation of displacement field u on 16 × 16 grid over Du = (0, 1)2.


- 5.3. Inference of Young’s modulus in linear elasticity problem


This section explores the application of neural operators as a surrogate in the Bayesian inference of Young’s modulus field m in the linear elasticity problem. As in the case of the Poisson problem, to ensure that Young’s modulus is positive, the inference problem is posed for the function w ∈ W such that m = αm exp(w)+βm. The following sub-section presents the prior measure and synthetic data generation, followed by the sub-section on inference results.

- 5.3.1. Setup of the forward problem, prior measure, and synthetic data The setup of the forward problem is the same as in Section 3.2.1. The Gaussian prior measure


µ⊘ on W is the same as µZ used in generating training data for neural operators. The values of the αm and βm and the covariance operator parameters are given in Section 3.2.1.

The data is generated synthetically following the same procedure as in the case of the Poisson problem in Section 5.2.1. In this case, however, data at a grid point consists of two scalars corresponding to the displacement components, and, as a result, do = 2 × 162 in o ∈ Rdo. In Figure 12, synthetic data along with the w, m, and u fields are plotted; the implementation can be found in the link Generate_GroundTruth.ipynb14.

- 5.3.2. Inference results


Parameters of the MCMC simulation are as follows: kmax = 10500, kburn = 500, β = 0.15, and σo = 0.0411. Here, σo is taken to be 1% of the mean of the o. The notebook in the link BayesianInversion.ipynb15 sets up the problem, loads trained neural operators, and runs MCMC simulation.

Acceptance rate and cost during MCMC simulations for four inference problems corresponding to the “true” and surrogate models are shown in Figure 13. The results, including the posterior mean and a sample from the posterior, from the “true” model are shown in Figure 14. The results with DeepONet, PCANet, and FNO surrogates are shown in Figure 15. In this case, the posterior mean obtained using the “true” forward model and the surrogates have almost the same error. Also, the error of the posterior mean of m contained using the “true” model and surrogates is less

- 14https://github.com/CEADpx/neural_operators/blob/survey25_v1/survey_work/

applications/bayesian_inverse_problem_linear_elasticity/Generate_GroundTruth.ipynb

- 15https://github.com/CEADpx/neural_operators/blob/survey25_v1/survey_work/


applications/bayesian_inverse_problem_linear_elasticity/BayesianInversion.ipynb

#### than one percent. Note that the synthetic field w had a slightly larger value along the diagonal, and the posterior mean w is seen to capture the variations in w.

![image 57](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile57.png)

![image 58](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile58.png)

(a) Acceptance rate (b) Cost

Figure 13: Acceptance rate and cost during MCMC simulation for the Linear Elasticity problem.

|![image 59](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile59.png)|
|---|


|![image 60](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile60.png)|
|---|


- Figure 14: Bayesian inference of Young’s modulus in the Linear Elasticity problem using the “true” model. The top panel shows the synthetic w field used to generate m, the corresponding PDE solution u, and the observation of u at 16 × 16 grid points. The panel below shows the posterior sample and posterior mean using the true model.


|![image 61](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile61.png)|
|---|


|![image 62](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile62.png)|
|---|


|![image 63](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile63.png)|
|---|


##### Figure 15: Comparing the Bayesian inference of Young’s modulus in the Linear Elasticity problem using DeepONet,PCANet, and FNO surrogates. The panels show the posterior sample and posterior mean using different surrogates.These results should be compared with the inference results using the “true” model in Figure 14.

### 6. Conclusion

- 6.1. Growing field of neural operators While this article has primarily focused on core architectures like DeepONet, PCANet, and


the Fourier Neural Operator (FNO), the field of neural operators continues to evolve with several frameworks that draw from other fields and address specific challenges in scientific computing. Physics-Informed Neural Operators (PINO) integrate physical laws directly into the training process, enhancing generalization for complex physical systems; see Li et al. (2024); Goswami et al.

- (2023); Wang et al. (2021b). The main idea behind PINO is that the loss function includes the residual of the PDE problem in addition to the loss due to model output and data error. Graphbased Neural Operators (GNO) Li et al. (2020b); Kovachki et al. (2023) consider the graph-based discretization of the spatial domain and, therefore, are attractive for problems with irregular domains. Their structure is similar to the FNO structure shown in (34), with a different form of the nonlocal kernel operation. The Wavelet Neural Operator (WNO) Tripura and Chakraborty


(2022) shares the structure of FNO with a different nonlocal operator (see (36)). In WNO, nonlocal operation is based on the wavelet transforms. Derivative-Informed Neural Operators (DINO) O’Leary-Roseberry et al. (2024) exploit derivative information to improve learning efficiency and accuracy in gradient-dominated systems. There is a considerable effort to extend neural operator frameworks into the Bayesian domain, integrating uncertainty quantification directly into the operator learning process; see Psaros et al. (2023); Jospin et al. (2022); Garg and Chakraborty (2022). These works aim to provide point estimates of the solution operator and probabilistic predictions that reflect the uncertainty in both the data and the model parameters.

Recently, the Kolmogorov-Arnold Neural Network (KAN) has been proposed Liu et al. (2024) that is inspired by the Kolmogorov-Arnold Representation Theorem, which states that for an n-dimensional function f : [0,1]n → R the following holds

2n+1

n

f(x) = f(x1,x2,...,xn) =

Φi

Φij(xj) , (52)

j=1

i=1

where Φi : R → R and Φij(·) : [0,1] → R are continuous functions of single variable. Note that the term inside the bracket on the right-hand side is the argument of the function Φi. The above mapping that takes input x to f(x) can be seen as a two-layer network, where the first layer takes input x (just one component) and produces n(2n + 1) outputs, each corresponding to {{Φij}ni=1}j2=1n+1, and the second layer takes n(2n+1) and produces 2n+1 outputs, each corresponding to {Φi}2i=1n+1. The final output is then obtained by summing up the outputs of the second layer.

Therefore, KAN, as a direct extension of the above equation, can be written as

2n+1

Φθi

f(x) = f(x1,x2,...,xn) =

j=1

n

Φθij(xj) , (53)

i=1

where, Φθi and Φθij are the parameterized function with parameters θ (e.g., B-spline curve). The parameter θ can be obtained by solving the appropriate optimization problem. The reference Liu et al. (2024) mentions that the above framework is limited in representing arbitrary functions, which prompts the authors to propose the more general form below

f(x) ≈ fKAN(x) = ΦθL ◦ ΦθL−1 ···Φθ1 ◦ Φθ0 x. (54)

Here, for layer l, Φθl are the tensors (say, of size nl+1 × nl), with each component being a parameterized function; see (Liu et al., 2024, Section 2.2). KAN offers an alternative structure compared

to multi-layer perception (MLP), and it has led to several new neural network and operator architectures.

Neural operators have demonstrated tremendous potential across multiple scientific and engineering domains. In Bayesian inverse problems, they accelerate computational processes by serving as efficient surrogates for expensive PDE solvers, enabling rapid posterior sampling in high-dimensional spaces Cao et al. (2023, 2024); Gao et al. (2024). Neural operators are attractive for optimization and control problems, where the bottleneck is the computation of the forward solution given the updated parameter field Shukla et al. (2024). The major hurdle in this direction is the unpredictability of the accuracy of neural operator predictions. This stems from the fact that the training data is generated based on prior knowledge of the distribution of the parameter field, and during the optimization and control iterations, the parameter fields for which solutions are sought could be far from the training regime; Jha (2024) shows that neural operators trained on a prior distribution perform poorly in the optimization problem.

Digital twins are another area that is seeing rapid expanse due to increased computational capacity, multiscale multiphysics modeling capabilities, innovation in sensors and actuators to measure and control the system, and growth in artificial intelligence; see the review on digital twins Juarez et al. (2021); Wagg et al. (2020). Neural operators show great potential in aiding the computations in digital twins. They can be used as a surrogate of the computationally demanding task of computing the next state of the system given the current state and model and control parameters Kobayashi and Alam (2024).

- 6.2. Controlling the neural operator prediction accuracy


Neural operators often struggle to meet high precision demands, particularly in complex PDEs and high-dimensional function spaces. Predictability of accuracy is the central issue in realizing the practical and robust applications of neural operators in uncertainty quantification, Bayesian inference, optimization, and control problems. Below, some of the key works in this direction are reviewed.

The multi-level neural network framework Aldirany et al. (2024) iteratively refines solutions by training successive networks to minimize residual errors from previous levels. This hierarchical approach progressively reduces approximation error. By capturing high-frequency components in subsequent neural networks and therefore reducing modeling error, it addresses the limitations of neural network approximations in capturing these modes due to the low sensitivity of network parameters to higher-frequency modes. The multi-stage neural network framework Wang and Lai

- (2024) addresses convergence plateauing in deep learning by dividing training into sequential stages, with each stage fitting the residual from the previous one. This approach progressively refines the approximation. The methods in references Aldirany et al. (2024); Wang and Lai (2024) achieve errors near machine precision (10−16), far exceeding the typical 10−5 limit of single-stage training.


The Galerkin neural network framework Ainsworth and Dong (2021) integrates the classical Galerkin method with neural networks, using the neurons in a neural network layer as basis functions to approximate variational equations. It adaptively adds new neurons to a single-layer neural network; each neuron corresponds to the basis function, and by adding more neurons, the dimension of approximation is increased in a way that the new subspace produces less error compared to the subspace with smaller dimensions.

The residual-based error correction method Cao et al. (2023); Jha (2024), see Figure 16, building on the idea of using lower-fidelity solutions to estimate modeling errors Jha and Oden (2022), treats the neural operator’s prediction as an initial guess and solves a variational problem to correct the residual error. This approach improves accuracy in applications like Bayesian inverse problems and topology optimization, where small errors can propagate and amplify. The trade-off in the residual-based error correction method is the introduction of the linear variational problem on the modeling error field, which must be solved and added to the neural operator prediction to get the improved prediction. For challenging nonlinear problems, the approach leads to significant speedups. In Bayesian settings, it enhances posterior estimates without increasing computational costs Cao et al. (2023). For the example optimization problem of seeking a diffusivity field in the Poisson equation that minimizes the compliance, neural operators, when used as a surrogate of the forward problem, produced minimizers with significant errors (about 80%). The error here is the norm of the difference between the minimizer obtained using the “true” forward model and the surrogate of the forward model. Neural operator surrogates with the residual-based error correction produced minimize with errors below 6%; see Figure 17, where the optimized diffusivity using the “true” model and surrogates are compared.

- Figure 16: Residual-based error correction of neural operator predictions Cao et al. (2023); Jha (2024). The corrector problem is a linear BVP, and if the predictor uNN is sufficiently close to the PDE solution u, the corrector gives quadratic error reduction Jha (2024).

![image 64](Jha_2025_From Theory to Application A Practical Introduction to Neural Operators in Scientific Computing_images/imageFile64.png)

- Figure 17: Optimized diffusivity in a Poisson equation and the optimized diffusivity using the neural operator surrogates with and without corrector. For more details about the problem and results, see (Jha, 2024, Section 4.3).


Some of the key limitations of the work mentioned above that address the issue of the reliability of neural networks include

- • Computational overhead. Many error control methods, like residual-based correctors and multi-level networks, introduce additional computational steps, potentially offsetting the efficiency gains of neural operators.
- • Scalability challenges. Iterative methods (e.g., multi-level and multi-stage networks) can become computationally intensive and less practical for high-dimensional or large-scale problems, leading to diminishing returns in accuracy improvement.
- • Risk of overfitting. While multi-stage and multi-level networks aim to reduce residual errors and capture high-frequency components, they risk overfitting in later stages or failing to generalize if residuals are small or noisy.


This underscores the scope for new research in controlling the accuracy of neural operators without compromising the computational speedup associated with neural operators.

- 6.3. Final thoughts Neural operators have emerged as transformative tools for solving parametric partial differential


equations (PDEs). They offer efficient surrogates that bridge the gap between traditional numerical methods and modern machine learning. Their ability to map between infinite-dimensional function spaces and fast evaluations makes them attractive approximators for parametric PDEs; they can lead to significant speedups in uncertain quantification, Bayesian inference, optimization, and control problems. Even more, for problems where observational data exists and where the confidence in mathematical models is low or in doubt, trained neural operators can combine the features of the model and data in a way that the accuracy of the model does not limit the neural operator predictions.

Despite these advancements, challenges remain, particularly in controlling prediction accuracy and ensuring generalization across diverse problem domains. Strategies like residual-based error correction, multi-level neural networks, and adaptively building neural networks can significantly improve the robustness and precision. Yet, each method presents trade-offs between computational cost and accuracy, underscoring the need for further research into scalable and adaptive error control mechanisms.

Looking forward, the integration of uncertainty quantification, physics-informed constraints, and multi-fidelity modeling represents promising directions for future work. These enhancements and strategies to control the prediction errors will be crucial for deploying neural operators in complex, real-world systems where precision and reliability are paramount.

### References

Ainsworth, M., Dong, J., 2021. Galerkin neural networks: A framework for approximating variational equations with error control. SIAM Journal on Scientific Computing 43, A2474–A2501. Aldirany, Z., Cottereau, R., Laforest, M., Prudhomme, S., 2024. Multi-level neural networks for accurate solutions of boundary-value problems. Computer Methods in Applied Mechanics and Engineering 419, 116666. Alnæs, M., Blechta, J., Hake, J., Johansson, A., Kehlet, B., Logg, A., Richardson, C., Ring, J., Rognes, M.E., Wells, G.N., 2015. The fenics project version 1.5. Archive of Numerical Software 3. Bhattacharya, K., Hosseini, B., Kovachki, N.B., Stuart, A.M., 2021. Model reduction and neural networks for parametric PDEs. SMAI Journal of Computational Mathematics, Volume 7 .

Bui-Thanh, T., Ghattas, O., Martin, J., Stadler, G., 2013. A computational framework for infinite-dimensional bayesian inverse problems part i: The linearized case, with application to global seismic inversion. SIAM Journal on Scientific Computing 35, A2494–A2523.

Cao, L., O’Leary-Roseberry, T., Ghattas, O., 2024. Derivative-informed neural operator acceleration of geometric mcmc for infinite-dimensional bayesian inverse problems. arXiv preprint arXiv:2403.08220 .

Cao, L., O’Leary-Roseberry, T., Jha, P.K., Oden, J.T., Ghattas, O., 2023. Residual-based error correction for neural operator accelerated infinite-dimensional bayesian inverse problems. Journal of Computational Physics 486, 112104.

Cotter, S.L., Roberts, G.O., Stuart, A.M., White, D., 2013. MCMC Methods for Functions: Modifying Old Algorithms to Make Them Faster. Statistical Science 28, 424 – 446. URL: https://doi.org/10.1214/13-STS421, doi:10.1214/13-STS421.

Dashti, M., Stuart, A.M., 2017. The Bayesian Approach to Inverse Problems. Springer International Publishing, Cham. pp. 311–428. URL: https://doi.org/10.1007/978-3-319-12385-1_7, doi:10.1007/ 978-3-319-12385-1_7.

De Hoop, M., Huang, D.Z., Qian, E., Stuart, A.M., 2022. The cost-accuracy trade-off in operator learning with neural networks. arXiv preprint arXiv:2203.13181 .

Fresca, S., Manzoni, A., 2022. POD-DL-ROM: Enhancing deep learning–based reduced order models for nonlinear parametrized PDEs by proper orthogonal decomposition. Computer Methods in Applied Mechanics and Engineering 388, 114181.

Gao, Z., Yan, L., Zhou, T., 2024. Adaptive operator learning for infinite-dimensional bayesian inverse problems. SIAM/ASA Journal on Uncertainty Quantification 12, 1389–1423. Garg, S., Chakraborty, S., 2022. Variational bayes deep operator network: A data-driven bayesian solver for parametric differential equations. arXiv preprint arXiv:2206.05655 . Goswami, S., Anitescu, C., Chakraborty, S., Rabczuk, T., 2020. Transfer learning enhanced physics informed neural network for phase-field modeling of fracture. Theoretical and Applied Fracture Mechanics 106, 102447. Goswami, S., Bora, A., Yu, Y., Karniadakis, G.E., 2023. Physics-informed deep neural operator networks, in: Machine Learning in Modeling and Simulation: Methods and Applications. Springer, pp. 219–254.

Jha, P.K., 2024. Residual-based error corrector operator to enhance accuracy and reliability of neural operator surrogates of nonlinear variational boundary-value problems. Computer Methods in Applied Mechanics and Engineering 419, 116595.

Jha, P.K., Oden, J.T., 2022. Goal-oriented a-posteriori estimation of model error as an aid to parameter estimation. Journal of Computational Physics 470, 111575. doi:10.1016/j.jcp.2022.111575. Jospin, L.V., Laga, H., Boussaid, F., Buntine, W., Bennamoun, M., 2022. Hands-on bayesian neural networks—a tutorial for deep learning users. IEEE Computational Intelligence Magazine 17, 29–48. Juarez, M.G., Botti, V.J., Giret, A.S., 2021. Digital twins: Review and challenges. Journal of Computing and Information Science in Engineering 21, 030802. Kobayashi, K., Alam, S.B., 2024. Deep neural operator-driven real-time inference to enable digital twin solutions for nuclear energy systems. Scientific reports 14, 2101. Kovachki, N., Li, Z., Liu, B., Azizzadenesheli, K., Bhattacharya, K., Stuart, A., Anandkumar, A., 2021. Neural operator: Learning maps between function spaces. arXiv preprint arXiv:2108.08481 .

Kovachki, N., Li, Z., Liu, B., Azizzadenesheli, K., Bhattacharya, K., Stuart, A., Anandkumar, A., 2023. Neural operator: Learning maps between function spaces with applications to pdes. Journal of Machine Learning Research 24, 1–97.

- Li, Z., Kovachki, N., Azizzadenesheli, K., Liu, B., Bhattacharya, K., Stuart, A., Anandkumar, A., 2020a. Fourier neural operator for parametric partial differential equations. arXiv preprint arXiv:2010.08895 .
- Li, Z., Kovachki, N., Azizzadenesheli, K., Liu, B., Bhattacharya, K., Stuart, A., Anandkumar, A., 2020b. Neural operator: Graph kernel network for partial differential equations. arXiv preprint arXiv:2003.03485 .


Li, Z., Kovachki, N., Azizzadenesheli, K., Liu, B., Bhattacharya, K., Stuart, A., Anandkumar, A., 2021. Fourier neural operator for parametric partial differential equations. International Conference on Learning Representations

. Li, Z., Zheng, H., Kovachki, N., Jin, D., Chen, H., Liu, B., Azizzadenesheli, K., Anandkumar, A., 2024. Physicsinformed neural operator for learning partial differential equations. ACM/JMS Journal of Data Science 1, 1–27. Liu, Z., Wang, Y., Vaidya, S., Ruehle, F., Halverson, J., Soljacˇic´, M., Hou, T.Y., Tegmark, M., 2024. Kan: Kolmogorov-arnold networks. arXiv preprint arXiv:2404.19756 . Lu, L., Jin, P., Karniadakis, G.E., 2019. Deeponet: Learning nonlinear operators for identifying differential equations based on the universal approximation theorem of operators. arXiv preprint arXiv:1910.03193 .

Lu, L., Jin, P., Pang, G., Karniadakis, G.E., 2021a. DeepONet: Learning nonlinear operators for identifying differential equations based on the universal approximation theorem of operators. Nature Machine Intelligence . Lu, L., Jin, P., Pang, G., Zhang, Z., Karniadakis, G.E., 2021b. Learning nonlinear operators via deeponet based on the universal approximation theorem of operators. Nature machine intelligence 3, 218–229.

Mandel, J., 2023. Introduction to infinite dimensional statistics and applications. arXiv preprint arXiv:2310.15818 . O’Leary-Roseberry, T., Chen, P., Villa, U., Ghattas, O., 2024. Derivative-informed neural operator: an efficient

framework for high-dimensional parametric derivative learning. Journal of Computational Physics 496, 112555. Psaros, A.F., Meng, X., Zou, Z., Guo, L., Karniadakis, G.E., 2023. Uncertainty quantification in scientific machine learning: Methods, metrics, and comparisons. Journal of Computational Physics 477, 111902.

Shukla, K., Oommen, V., Peyvan, A., Penwarden, M., Plewacki, N., Bravo, L., Ghoshal, A., Kirby, R.M., Karniadakis, G.E., 2024. Deep neural operators as accurate surrogates for shape optimization. Engineering Applications of Artificial Intelligence 129, 107615.

Stuart, A.M., 2010. Inverse problems: a bayesian perspective. Acta numerica 19, 451–559. Tripura, T., Chakraborty, S., 2022. Wavelet neural operator: a neural operator for parametric partial differential

equations. arXiv preprint arXiv:2205.02191 .

Wagg, D., Worden, K., Barthorpe, R., Gardner, P., 2020. Digital twins: state-of-the-art and future directions for modeling and simulation in engineering dynamics applications. ASCE-ASME Journal of Risk and Uncertainty in Engineering Systems, Part B: Mechanical Engineering 6, 030901.

- Wang, S., Wang, H., Perdikaris, P., 2021a. Learning the solution operator of parametric partial differential equations with physics-informed DeepONets. Science advances 7, eabi8605.
- Wang, S., Wang, H., Perdikaris, P., 2021b. Learning the solution operator of parametric partial differential equations with physics-informed deeponets. Science advances 7, eabi8605.


Wang, Y., Lai, C.Y., 2024. Multi-stage neural networks: Function approximator of machine precision. Journal of Computational Physics 504, 112865.

