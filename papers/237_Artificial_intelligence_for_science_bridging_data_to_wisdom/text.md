## arXiv:2410.19843v3[eess.SY]24 Mar 2026

###### Artificial intelligence for partial differential equations in computational mechanics: A review

Yizheng Wanga,b, Jinshuai Baia,e,f, Zhongya Lina, Qimin Wangc, Cosmin Anitescub, Jia Sund, Mohammad Sadegh Eshaghic, Yuantong Gue,f, Xi-Qiao Fenga, Xiaoying Zhuangc, Timon Rabczukb,∗, Yinghua Liua,∗

aDepartment of Engineering Mechanics, Tsinghua University, Beijing 100084, China bInstitute of Structural Mechanics, Bauhaus-Universität Weimar, Marienstr. 15, D-99423 Weimar, Germany cChair of Computational Science and Simulation Technology, Institute of Photonics, Leibniz University Hannover, Hannover 30167, Germany dDrilling Mechanical Department, CNPC Engineering Technology RD Company Limited, Beijing 102206, China eSchool of Mechanical, Medical and Process Engineering, Queensland University of Technology, Brisbane, QLD 4000, Australia fARC Industrial Transformation Training Centre—Joint Biomechanics, Queensland University of Technology, Brisbane, QLD 4000, Australia

###### Abstract

In recent years, Artificial intelligence (AI) has become ubiquitous, empowering various fields, especially integrating artificial intelligence and traditional science (AI for Science: Artificial intelligence for science), which has attracted widespread attention. In AI for Science, using artificial intelligence algorithms to solve partial differential equations (AI for PDEs: Artificial intelligence for partial differential equations) has become a focal point in computational mechanics. The core of AI for PDEs is the fusion of data and partial differential equations (PDEs), which can solve almost any PDEs. Therefore, this article provides a comprehensive review of the research on AI for PDEs, summarizing the existing algorithms and theories. The article discusses the applications of AI for PDEs in computational mechanics, including solid mechanics, fluid mechanics, and biomechanics. The existing AI for PDEs algorithms include those based on Physics-Informed Neural Networks (PINNs), Deep Energy Methods (DEM), Operator Learning, and Physics-Informed Neural Operator (PINO). AI for PDEs represents a new method of scientific simulation that provides approximate solutions to specific problems using large amounts of data, then fine-tuning according to specific physical laws, avoiding the need to compute from scratch like traditional algorithms. Thus, AI for PDEs is the prototype for future foundation models in computational mechanics, capable of significantly accelerating traditional numerical algorithms.

Keywords: Artificial intelligence, Artificial intelligence for science, Artificial intelligence for partial differential equations, Computational mechanics, Physics-informed neural networks, Operator learning

###### 1. Introduction

Recently, the integration of AI and traditional science (AI4Science: AI for Science) has drawn broad attention [1]. Due to many physical computing problems being closely related to the solution of partial differential equations (PDEs), using artificial intelligence algorithms to solve PDEs [2], a key research area known as AI4PDEs, has gained substantial interest among researchers in computational physics and mathematics [3]. This area is recognized as one of the most important research directions within the broader field of AI4Science [4]. Fig. 1 displays the relationship between AI4PDEs and AI4Science. This review specifically focuses on the role of AI4PDEs in computational mechanics. As shown in Fig. 1, recent progress has rapidly expanded across several major branches of computational mechanics. It is worth emphasizing that computational mechanics is a broad

∗Corresponding author

Email addresses: wang-yz19@tsinghua.org.cn (Yizheng Wang), timon.rabczuk@uni-weimar.de (Timon Rabczuk), yhliu@mail.tsinghua.edu.cn (Yinghua Liu)

Forward

| | |
|---|---|
| | |
| | |


Method

Application

Solid Mechanics

| | |
|---|---|
| | |


Operator Learning

Inverse

Physics-informed Neural Operator

Forward

Computational Mechanics

s

Fluid Mechanics

A

- D
- E


I

f

o

P

r M

r

o

a t e

f

I

Forward and inverse

r i a

Inverse

A

l

AI for Science

A

y

I f o

g

Forward

o

l

o

r C h e m i

i

B

Biomechanics

r

o

f

I

A

- s
- t


r

y

Inverse

Elasticity

Elastoplasticity Hyperelasticity Fracture

Identification of Material Parameters Identification of Constitutive Law

Topology Optimization Defect Identification

Hydrodynamics Aerodynamics and Shock Wave

Multiphase and Moving Boundary Multiscale and Multiphysics

Field Reconstruction Parameter esitimation

Soft Tissue Deformation

Blood Flow

Modeling Blood Flow

Material Parameter Identification in soft tissue

- Fig. 1. The role of AI4PDEs in AI4Science, along with an introduction to AI4PDEs in computational mechanics, including solid mechanics, fluid mechanics, and biomechanics.


discipline. Accordingly, this review concentrates on representative scenarios where AI4PDEs interacts with solid mechanics, fluid mechanics, and biomechanics, with particular attention to methodological developments, practical challenges, and emerging opportunities in these domains.

AI contributes to PDE-based simulation in two complementary ways. First, it enables the acceleration of existing workflows through surrogate models, neural operators [5] and hybrid approaches [6] that reduce computational cost while maintaining accuracy. Second, it opens the possibility of scientific discovery [4], where machine learning models are used to identify unknown parameters, infer constitutive relations or extract governing principles from data. While the former direction is already demonstrating practical impact, the latter remains more challenging due to issues such as data scarcity, noise, and identifiability, particularly in engineering applications [7]. In the long term, these developments may contribute to more general and adaptive models for computational mechanics, capable of transferring knowledge across geometries, materials and physical processes. However, such a vision remains far from realization. Current limitations in data availability, generalization and reliability highlight the need for approaches that combine data-driven learning with strong physical structure rather than relying on purely data-driven paradigms.

The field of computational mechanics has also been impacted by AI4Science. The integration of AI4Science and computational mechanics mainly occurs in two aspects. One is through deep learning methods, utilizing real experimental data or reliable numerical results [8] (such as those obtained from finite element methods) and then using neural networks to construct surrogate models. This is a type of implicit programming [9], where "implicit programming" refers to inputting data and utilizing the strong fitting ability of AI algorithms to output "programs," which consist of neural network parameters, thus eliminating the need for humans to write programs to solve particular problems specifically. This traditional method of explicitly writing programs to solve specific problems often requires designing programs to transform abstract principles into computerreadable code. Artificial intelligence algorithms represent a form of implicit programming that uses data to build surrogate models. The core idea is to use the fitting power of neural networks to model the abstract

relationships between data [8]. If training is successful, and the test set and training set are consistent in data distribution, surrogate models often exhibit very high computational efficiency and accuracy on the test set. However, this method has some unavoidable problems, such as requiring large amounts of data, and the quality and quantity of data determining the effectiveness of the model. This integration method relies entirely on data, necessitating the use of existing methods to obtain relevant data. Therefore, it faces challenges like the curse of dimensionality [10, 11]. Additionally, due to the lack of physical constraints, the interpretability is poor, leading to consequences that make it difficult to improve the model’s effectiveness. This disadvantage causes a significant amount of manual, trial and error based parameter tuning, so using neural networks to establish surrogate models is essentially a black-box approach. The choice of surrogate models often benefits from computer vision algorithms to better integrate with current physical problems. For instance, computer vision algorithms like the Swin Transformer were used to predict weather in the PanGu foundation model [5], or to predict the equivalent modulus of non-uniform materials [8]. Overall, the first aspect is a completely data-driven modeling method. The limitation of this type of algorithm is that it only has the potential to be faster, but it is difficult to have the potential to be more accurate, because the data-driven modeling method is based on fitting existing high-precision data, and the accuracy can only be infinitely close to the existing high-precision data.

The other important aspect of the integration between AI4Science and mechanics is the incorporation of physical laws into the loss function of neural networks, which is a core part of AI4PDEs. Using physical information, by which the need for high-quality data is reduced [12], often reflected in solving PDEs, i.e., using AI4PDEs algorithms to solve PDEs of computational mechanics. The introduction of physical equations reduces the data requirement because it incorporates inductive biases, which refers to the assumptions on which algorithm models are based, helping the model to make predictions and reducing the amount of data needed. PDEs also represent a special form of inductive bias, as physical equations are often derived using more basic assumptions (such as assumptions of linearity, small deformations, and continuity in elasticity mechanics) and then derived with mathematical tools to describe the laws of material motion. Thus, PDEs are a form of advanced inductive bias [13]. In this review, AI for PDEs is primarily organized into three major methodological paradigms: Physics-Informed Neural Networks (PINNs), operator learning, and physics-informed neural operators, which currently constitute the dominant research directions in computational mechanics. Beyond these three mainstream paradigms, emerging directions such as reinforcement-learning-based PDE control [14], generative surrogate modeling [15], and foundation-model-assisted scientific computing [16] are also attracting increasing attention, although they remain less mature in computational mechanics applications at present. Moreover, it is important to note that AI for PDEs do not always replace classical numerical techniques such as finite element methods (FEM). In many applications, AI for PDEs are integrated within traditional PDE solvers, for example, by accelerating multiscale simulations [17]. These hybrid approaches complement classical methods while leveraging the efficiency and generalization capabilities of AI.

The use of deep learning to solve PDEs (AI4PDEs) first appeared with the Physics-Informed Neural Networks (PINNs), a term coined by Raissi et al. in 2019 [2]. However, the concept of using neural networks to solve PDEs dates back to 1990 [18], 1994 [19] and 1998 [20]. Because deep neural networks (DNNs), powerful GPU computing, and associated software tools were not available at that time, these ideas did not receive sufficient attention. Recently, with the rapid development of computer hardware, advancements in machine learning algorithms, and the convenient implementation of automatic differentiation algorithms within artificial intelligence frameworks like PyTorch and TensorFlow, the PINNs algorithm has garnered considerable attention, leading to an increase in the complexity of the problems that can be solved [7]. Compared to traditional numerical methods, PINNs has two main advantages: firstly, utilizing the powerful fitting capabilities of neural networks for solving challenging PDEs problems, such as those involving significant nonlinearity, convectiondominated, or shock problems, provides a new method of scientific computation [7]. For forward problems, since PINNs are a type of mesh-free method where the approximate function is a neural network and the solution is obtained for the entire domain at once, they share similar advantages with mesh-free methods, such as handling large deformation problems with significant mesh distortion. For inverse problems, the code format can be easily adapted, allowing for straightforward application with automatic differentiation (AD: Automatic Differentiation) [21]. The second advantage is its suitability for solving high-dimensional problems, mainly due to the construction of the PINNs loss function using the Monte Carlo method, which itself is a powerful

tool for high-dimensional integral calculations. Therefore, the advantages of PINNs in solving high-dimensional problems do not originate from neural networks but from the Monte Carlo method used in the loss function. In theory, if traditional methods also adopt the Monte Carlo approach for integral calculations, they would possess the same capabilities as PINNs in solving high-dimensional problems. PINNs can solve almost all PDE problems because the core of PINNs involves setting the approximate function as a neural network, so the computational approach is similar to traditional methods. Thus, any PDEs problem that traditional methods can solve, PINNs can also address, such as linear PDEs [22, 23], non-linear PDEs [24, 25], stochastic PDEs [26, 27], and integral differential equations (IDEs) [28]. PINNs also have drawbacks, including a lack of robustness, accuracy, and computational efficiency [29] in many applications. For instance, even when the forward problem is well-posed and linear, the PINN formulation can lead to ill-posed (nonlinear) optimization problems [30].

Mathematically, PINNs are divided into two formats: the original strong form of PINNs [2] and the energy form of PINNs [23]. The strong form and energy form of PINNs are explained in detail in Section 2.1.1 and

- Section 2.1.2, respectively. The energy form is the deep Ritz method introduced by Yu in 2018 [23], which was later applied to the field of computational mechanics by Samaniego et al. (2020) [31], proposing the Deep Energy Method (DEM). The core idea of DEM is minimizing the potential energy of the system. In contrast to the strong form of PINNs, which utilizes PDEs, DEM approaches the problem through the system’s total energy using the variational principle. Notably, although DEM mainly follows the energy form, it also incorporates the idea of the strong form of PINNs in the original review [31], called the deep collocation method (DCM), which is the strong form of PINNs. It can be said that DEM is the first major summary and large-scale application of PINNs in computational mechanics. The main difference between the strong form and energy form of PINNs lies in the composition of the loss function. The loss function of the strong form combines PDEs directly through weighted residuals, while the loss function of DEM is based on the principle of least action, such as the principle of minimum potential energy in mechanics. Both the strong form and energy form of PINNs are shown in the upper left corner of Fig. 2. A significant advantage of PINNs is that they can combine data and physical equations, making them a semi-supervised algorithm particularly suitable for problems involving both data and equations. Additionally, PINNs can be easily adapted for inverse problems, with the programming code being nearly identical to that for forward problems. It only requires setting the variables to be solved in the inverse problem as trainable optimization variables and incorporating them into the loss function. Thus, compared to traditional inverse problem algorithms, PINNs is very easy to program for solving inverse problems [3].

Overall, PINNs leverage existing physical laws, significantly reducing the need for datasets and offering better interpretability than purely data-driven approaches. However, assigning physical meaning to the hyperparameters in PINNs remains challenging, especially in comparison to the finite element method (FEM). The accuracy of PINNs in solving forward problems was difficulties in surpassing traditional methods. The main reason is the non-convex nature of neural networks. Although the non-convexity of neural networks provides powerful fitting capabilities, it also introduces difficulties in optimization. PINNs are suitable for problems with clear physical laws and small data volumes. Of course, if the data volume is large enough, PINNs can be used, but in such cases, operator learning would be more appropriate (please note that the original PINNs do not require a specific data volume).

In recent years, operator learning has become a hot research topic, as shown in the upper right corner of Fig. 2. Representative works include DeepONet [32] and FNO (Fourier Neural Operator) [33]. The initial proposals for operator learning were purely data-driven, making them highly suitable for large data volume problems (even if the physical processes are unclear, operator learning can still rely on learning the abstract complex relationships within the data). The difference from traditional data-driven methods lies in the reliable mathematical theory supporting operator learning and the advantage of discretization-invariance in operator learning. In terms of theoretical support, for example, DeepONet is based on the theory proposed by Chen et al. (1995) [37] that neural networks can fit any continuous operator, which led to the design of the algorithm. FNO is based on Fourier transforms; discretization-invariance roughly refers to the ability to train and test on any grid, and after the mesh size changes, retraining is not required. This will be explained in detail in

- Section 2.2. It is important to note that some neural operator algorithms actually learn the mapping from a discrete input function to a discrete output function space, rather than the differential operator itself. To address this, Bartolucci et al. [38] proposed RENOs (Representation Equivalent Neural Operators) to learn the operator mapping of PDEs.


Any

Clear λPINNs

v(t−1)

Strong form

Neural Network

Energy Form

###### a



UX

P( )

- X

Z

a

a

a

a

a

L( )

- Y


a

a UY

mode

Loss

Lossi

UZ

a

Physical Laws

Physical Laws

Data Data

W

λi

MSE

Input Layer (Coordinates) Hidden Layers Output Layer

ℜ

mode

No Loss<tol?

 −1

σ (t)

Yes

vFNO FNO Layer

Done

Any

Enough

| | | |
|---|---|---|
|Limited<br><br>Physical Laws<br><br>Data|Based on approximation physical equations<br><br>Data with higher accuracy<br><br>Operator<br><br>Big data<br><br>![image 1](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile1.png)<br><br>PINO: Physics-informed neural operator|Clear<br><br>Physical Laws<br><br>Data|


PINNs

learning

Use data to fine-tune

Use PDEs to fine-tune

Solve for approximate solutions

Solve for approximate solutions

Enough

Not Clear

###### Fig. 2. Main methods of AI4PDEs: Physics-informed neural networks [2, 31, 23], operator learning [32, 33, 34], and physicsinformed neural operators [35, 36]. PINNs are primarily trained using governing physical equations and do not intrinsically require observational data. Operator learning is a data-driven approach for approximating solution operators from input-output pairs, while PINO integrates physical equations into operator learning, enabling physics-informed training of neural operators.

Existing approaches in computational mechanics differ primarily in how they handle generalization and solution strategies [39]. Neural operator [40, 33] and transformer-based models [41] aim to learn parametric mappings between problem inputs, such as geometry, material parameters and boundary conditions, and the corresponding solution fields. Once trained, these models enable fast evaluation across families of problems without resolving each instance from more detailed simulations. In contrast, classical numerical methods such as the finite element or finite volume methods, solve each problem instance independently through discretization and iterative solution procedures [42]. While modern simulation software platforms provide broad applicability across geometries and physics, the underlying solution process remains instance-specific and computationally intensive. Bridging these two paradigms, combining the generalization capabilities of learned operators with the robustness and accuracy of classical solvers, represents a central challenge in AI-assisted scientific computing [6, 43].

A key obstacle in this context is not only the solution of the governing equations, but the representation and processing of the geometry [44]. This challenge extends beyond classical CAD-based workflows and includes a wide range of geometric representations, such as surface triangulations, voxelized data, level-set descriptions, and point clouds obtained from imaging or scanning technologies [45]. Traditional simulation pipelines require these representations to be converted into watertight volumetric meshes, a process that is often brittle, timeconsuming and difficult to automate. Recent developments in hybrid neural operator-based methods such as PFEM [6] suggest an alternative perspective, where geometry can be treated in a more flexible and direct manner. In such approaches, geometry is encoded through implicit or discrete representations and processed together with physical parameters to predict solution fields. Hybrid strategies that combine these models with classical solvers provide a promising direction, where learned operators can serve as fast predictors or initial guesses, while numerical solvers ensure robustness and accuracy [43, 17]. In this setting, the choice of physical constraints plays a critical role. Recent studies based formulations based on variational principles or energy minimization provide a natural and effective way to enforce physical consistency [46]. Such approaches can improve stability, reduce the need for large training datasets, and enable closer integration between learningbased models and classical numerical methods.

Moreover, many complex engineering problems face the challenge of unclear physical processes. Even if PDEs are used to describe them, they are not completely accurate, and the data volume is also limited. The latest development of physics-informed neural operators (PINO: Physics-informed neural operator [35]) can handle these issues of vague physics and insufficient data to some extent, as shown in the lower left corner of Fig. 2. Initially, an approximate solution is obtained by relying on approximate physical equations and corresponding boundary initial conditions, which is then fine-tuned using limited data [36]. Additionally, for problems with large data volumes and clear physical processes, physics-informed neural operators can also be effectively applied to these issues [47, 35, 42, 30], as shown in the lower right corner of Fig. 2. The approach is to first obtain a good approximate solution using operator learning and then fine-tune it based on clear physical processes. Since solving PDEs relies on operator learning partly, it can significantly accelerate PDEs computations, thousands to tens of thousands of times faster than traditional numerical methods [48]. At the same time, iterating the approximate solution by operator learning according to the physical equation does not require much time because the initial solution (approximate solution) is not far from the true solution. This simultaneously possesses the speed of operator learning and the accuracy of physical equations. Therefore, it can reduce the dependence on supercomputers for solving complex PDEs and solve larger problems with fixed computing power. Thus, the potential of PINO is substantial not only in academia but also in industry. A detailed explanation will be provided in Section 2.3. It is worth noting that PINO is unlike the initially proposed PINNs which can only solve specific problems, i.e., once boundary conditions, geometric shapes, or materials change, a new solution is required in PINNs. However, PINO learns a series of mappings of PDEs family, allowing for rapid attainment of target solutions even if the aforementioned conditions change. Therefore, this will be one of the most promising directions in the field of computational mechanics. The essence of PINO is the combination of operators and physical equations, incorporating the ideas of PINNs in the physical equations and operator learning using data-driven like DeepONet or FNO. Therefore, PINO simultaneously includes PINNs and operator learning. If the data volume is large enough, PINO can be reduced to operator learning. If the physical process is clear, it can be reduced to PINNs.

Finally, a fundamental practical limitation in AI-driven computational mechanics is the availability of high-

quality data [35]. Unlike fields such as computer vision, where large standardized datasets are readily available

- [49], data in computational mechanics often requires expensive numerical simulations or experiments. This limitation motivates the development of physics-informed and hybrid approaches that reduce reliance on large datasets while maintaining predictive accuracy [43, 6].

The outline of this article is shown in Fig. 1. Section 2 systematically summarizes AI4PDEs algorithms, including the strong form of PINNs, energy form, operator learning, and physics-informed neural operators. Section 3 introduces some theoretical work on AI4PDEs. Sections 4 and 5 discuss some applications of AI4PDEs in computational mechanics, including forward and inverse problems in solid, fluid, and biomechanics1. Section 6 predicts the likely emergence of the foundation model in computational mechanics and the potential opportunities and challenges AI4PDEs may face in the future.

- 2. AI for PDEs: Methodology


A multitude of physical phenomena rely on PDEs for modeling. Once the boundary and initial conditions become complex, the analytical solution of PDEs is often difficult to obtain. At this point, various numerical methods are employed to achieve approximate solutions, such as the commonly used finite element methods

- [50, 51, 52, 53], mesh-free methods [54, 55, 56, 57, 58, 59], finite difference methods [60], finite volume methods [61], boundary element methods [62], and spectral methods [63]. Despite the great success of traditional numerical methods in computational mechanics over the past 50 years, we still struggle to integrate data into traditional algorithms, especially in industries where multimodal, multi-resolution, and high-error complex data are common [64]. Moreover, finding a model that can describe such complex systems is also a challenge [34], as PDEs describing these systems are also models [36]. Therefore, integrating data into computational models is of significant importance to describe complex systems. Additionally, when solving inverse problems and large, complex nonlinear problems, traditional algorithms often involve large computational loads and complex formats, especially when dealing with highly complex nonlinear issues, which require vast amounts of code and are not friendly to updates [3], such as OpenFOAM [65], which has more than 100,000 lines of code. For low-dimensional and relatively simple geometric problems, traditional numerical methods can offer high computational accuracy and efficiency.


While these methods, such as the FEM, are quite effective in dealing with many complex problems, challenges can arise when dealing with high-dimensional problems and complex geometric shapes [11, 66]. However, the latest AlphaGeometry [67] may assist mesh generators in the future. Additionally, traditional FEM often require the selection of specific basis functions (shape functions).

AI for PDEs, unlike traditional numerical methods, refers to a class of algorithms that use deep learning to solve PDEs. From the perspective of deep learning, it can be seen as learning a mapping relationship, which maps the input field through a neural network to the interested physical field and this mapping is achieved through composite functions, which is different from the current the predominance of additive methods for approximating mappings. The reason why deep learning is effective in solving PDEs boils down to the following points:

• Powerful approximation capability of neural networks: Under the condition of monotonically bounded activation functions, with a certain distribution of hidden layer neurons (at least one hidden layer), any continuous function can be approximated [68, 69]. Therefore, for some field functions with drastic changes, AI4PDEs can theoretically select the best basis functions automatically through the powerful fitting capabilities of neural networks, thereby avoiding the need to design shape functions like finite elements, which undoubtedly reduces the intellectual cost [29]. Additionally, neural networks can also fit any continuous operator [37], with DeepONet proposed by Lu et al. [32] utilizing this theory. This theory [37] provides a good theoretical prospect for the current hot research topic of operator learning.

1Please note that most of the images in Section 4 and Section 5 are adapted from the most important papers closely related to this review, combined with text and formulas, to clearly explain their important ideas. Due to the limited length of this article, for details on the algorithms, please refer to the original papers.

- • Direct integration of data and physical laws: AI4PDEs can utilize the powerful fitting capabilities of neural networks to learn the abstract rules behind data and physical equations, especially for complex physical processes where the physical laws are not very clear, and where the data volume is not large. An approximate solution can be obtained based on the physical equation and then adjusted with a small amount of data to achieve a solution closer to the real laws compared to traditional numerical methods [36]. Additionally, for domains with large data volumes and clear physical laws, operator learning can be used to pre-train the data and then fine-tune it according to the physical equation, significantly improving the speed of traditional numerical methods because the initial solution obtained by operator learning needs fewer iteration steps compared to a random initial solution by traditional numerical methods. This direction is currently one of the most cutting-edge in AI4PDEs [42, 47, 35].
- • Precision and convenience of derivatives by automatic differentiation: This is because backpropagation uses the method of analytic gradient flow to calculate gradients, rather than using numerical methods, thereby obtaining precise gradient values. This feature has been efficiently implemented in deep learning frameworks, making backpropagation very easy, thus AI4PDEs are simple in computation format and conducive to updates and iterations [64]. Although the mathematical format of AI4PDEs is not simple, thanks to the current optimization frameworks, such as Pytorch and Tensorflow, these frameworks facilitate the programming of AI4PDEs [70, 71], and the core solver usually does not exceed a hundred lines of code. Additionally, due to the wide applicability and adaptability of these frameworks, it reduces the need for people to be deeply familiar with traditional algorithms, especially inverse problem [3].


Due to the powerful fitting capabilities of neural networks as trial functions, the new paradigm of integrating data and equations, coupled with convenient code implementation, these unique advantages make AI4PDEs important and highly promising in solving mechanical PDEs, i.e., computational mechanics. AI4PDEs represent a class of numerical algorithms independent of finite elements, providing another possibility for computational mechanics. AI4PDEs have two important modules, the physical and data-driven modules, which we will introduce separately. AI4PDEs’ physical module is based on the idea of PINNs, with the two mainstream methods being the strong form and energy form of PINNs, both of which essentially use neural networks to replace the approximate functions in the weighted residual method. The strong form of PINNs often writes the domain equation, boundary conditions, and initial conditions into the loss function through hyperparameter-weighted residuals for optimization, different choices of approximate functions (trial functions), and weight functions (test functions) result in different numerical methods of PINNs strong form, similar to the research idea of different numerical methods arising from different trial and test functions in finite elements. PINNs’ strong form often does not rely on numerical integration, and since all PDEs have a weighted residual form, the strong form of PINNs is general, almost any PDEs can be solved. However, PINNs’ strong form has numerous hyperparameters, often requiring tuning, and when facing specific problems, the optimal hyperparameters are often unknown. Another important method of PINNs is the energy form, which essentially uses the variational principle, converting the strong form into an integral functional. The advantage of PINNs energy form is the dramatic reduction in hyperparameters, often higher accuracy and efficiency (the variational principle has fewer derivative orders). The drawback of PINNs energy form is also very obvious: it is highly dependent on the choice of numerical integration scheme, also, not all PDEs have a well-behaved extremum variational principle, so its generality is not as good as PINNs strong form. AI4PDEs’ data-driven module is based on the recently developed operator learning, which is actually a special kind of pure data-driven algorithm. Using operator learning to learn the mapping of PDEs families, this mapping can be understood as the same type of PDEs under different parameters. The reason why it is possible to use neural networks to fit PDEs solutions is because we can understand PDEs as a kind of implicit mapping, which maps boundary conditions, geometric shapes, material fields to the solution fields. However, the mapping is very complex and difficult to write out in an analytic explicit form, therefore, it might be possible to use neural networks to learn the mapping. If successful, then inputting different boundary conditions, geometric shapes, and material fields can quickly obtain the needed field variables (such as displacement field), and the high-precision data obtained using traditional methods is the premise for learning PDEs’ implicit mapping. Some recent works hope to combine physical equations into the operator [42, 47, 35, 72], which can use the physical equation to fine-tune the initial solution given by operator learning, thereby achieving lower computational cost compared to purely physics-based models. The current direction is

still explored and has great research prospects, but the key is how to better combine prior knowledge and data together to better train the model.

Considering that the physical and data modules are the two most important parts of AI4PDEs, this chapter will review the AI4PDEs physical module (PINNs: Physics-informed neural networks), including the strong form and energy form. In addition, the AI4PDEs data module will be reviewed, including operator learning and the integration of data and physical modules (PINO: Physics-informed neural operators).

- 2.1. PINNs: Physics-informed neural networks


- 2.1.1. Strong form PINNs consist of two main aspects:


- • The first is the use of neural networks to replace the approximate functions. The core of finite element in computational mechanics involves the selection of trial functions and test functions, and different selections form various types of finite element methods. PINNs mainly change shape function of FEM to neural networks in the trial function. The solution procedures of FEM and PINNs are fundamentally different. PINNs solve a non-convex optimization problem, whereas FEM addresses a linearized system of equations.
- • The second aspect is the adoption of convenient automatic differentiation technology from artificial intelligence algorithm frameworks in the optimization algorithm to implement the physical equation loss function formed by PDEs. Using PDEs to construct the loss function essentially restricts the optimization space of neural networks, thereby obtaining an approximate solution space [7].


The idea of PINNs is very simple and straightforward, fundamentally introducing pre-known knowledge into the neural network, reducing the optimization space, and thereby improving accuracy and efficiency. The idea of combining traditional knowledge into algorithms has been very common in traditional machine learning, for example, Lauer et al. (2008) [73] embedded the prior knowledge of functions and their derivatives as constraints into support vector regression (SVR: Support Vector Regression) to reduce approximation errors.

PINNs were first introduced in the strong form, as shown in Fig. 3. The strong form of PINNs is an approximation function using neural networks in the weighted residual method. Considering the specific PDE, the original PDEs is:

 

Domain PDEs: L(u(x,t)) = f(x,t) ∀(x,t) ∈ Ω (0,T] Boundary condition: u(x,t) = h(x,t) ∀(x,t) ∈ ∂Ω (0,T] Initial condition: u(x) = g(x) ∀(x,t) ∈ Ω {t = 0}

. (1)



We change the original equation into residual form, divided into three parts:

 

Domain PDEs residual: rd(u˜(x,t)) = L(u˜(x,t)) − f(x,t) ∀(x,t) ∈ Ω (0,T] Boundary condition residual: rb(x,t) = u˜(x,t) − h(x,t) ∀(x,t) ∈ ∂Ω (0,T] Initial condition residual: rini(x) = u˜(x,t = 0) − g(x) ∀(x,t) ∈ Ω {t = 0}

, (2)



where L is the differential operator, f is the non-homogeneous term of the PDEs, Ω is the spatial domain, ∂Ω is the boundary, x is the spatial coordinate, t is time. u is the field of interest approximated by the neural network, and controlled by the parameters of the neural network. The neural network is denoted as u(x,t;W), where W represents the parameters of the neural network. h and g are the conditions that must be satisfied by the boundary conditions and initial conditions, respectively, which can often be analytically represented as functions h(x,t) and g(x), respectively. rd, rb, and rini are the domain residual, boundary condition residual, and initial condition residual, respectively.

The above residuals rd, rb, and rini are numerically summed using weight functions:

 

Domain PDEs residual weighted integral: Rdi = N

###### I=1 vdi (xI,tI) rd(u˜(xI,tI)) ∀(x,t) ∈ Ω (0,T] Boundary condition residual weighted integral: Rbi = N

d

I=1 vbi(xI,tI) rb(u˜(xI,tI)) ∀(x,t) ∈ ∂Ω (0,T] Initial condition residual weighted integral: Rinii = NI=1ini vinii (xI) rini(u˜(xI)) ∀(x,t) ∈ Ω {t = 0}

,

b



(3)

Neural network

Data Loss

x1

y1

###### Loss

xm t

PDEs Loss

yn

Input Hidden Layer Output

Boundary/ Initial Loss

No Loss<tol?

Yes Done

Fig. 3. AI for PDEs method: Schematic of PINNs strong form [2].

where vdi , vbi, and vinii are the domain, boundary, and initial weight functions, respectively, whose dimensions correspond one-to-one with rd, rb, and rini. Rdi , Rbi, and Rinii are the domain residual integral, boundary condition residual integral, and initial condition residual integral, respectively. ⊙ is the element-wise operation, meaning corresponding elements are multiplied without changing the tensor’s shape. Nd, Nb, and Nini are the total number of numerical summation points in the domain, boundary, and initial areas, respectively. All of the above integral forms of residuals are weighted summed to form the loss function of PINNs in the strong form:

L = λpdesLpdes + λbLb + λdataLdata

Sd

βdj · (Rdj)2

Lpdes =

j=1

Sb

βbj · (Rbj)2 +

Lb = [

j=1

Sini

βinij · (Rij)2]

j=1

Ndata

[u˜(xI,tI) − u¯(xI,tI)]2,

Ldata =

I=1

(4)

where Sd, Sb, and Sini are the number of weight functions in the domain, boundary, and initial conditions, respectively; βdj, βbj, and βinij are the weights of the domain, boundary, and initial condition residual integrals, respectively. λpdes, λb, and λdata are the weights of the PDEs, boundary (initial), and data loss, respectively. Ndata is the number of existing high-precision data points. The training process involves adjusting the trainable weights of the neural network to minimize the loss function.

All important methods of PINNs in the strong form are almost always developed around Eq. (3) and Eq. (4). This article summarizes the existing important methods of PINNs in strong form from the perspectives of whether the trial functions and test functions are partitioned, types of trial functions and test functions, and the method of imposing essential boundary conditions, as shown in Table 1, where partitioning refers to dividing different areas into different neural networks.

###### Table 1 Current status of PINNs strong form methods

Methods Trial function: subdomains Test function: subdomains Trial function: type Test function: type Method of Imposing Essential Boundary

PINNs [2] No (Global) No (Global) Fully Connected Dirac delta Penalty Function DGM [74] No (Global) No (Global) Fully Connected Least Squares Penalty Function

VPINNs [75] No (Global) No (Global) Fully Connected Mixed Weight Functions Penalty Function PIELM [76] Yes (Subdomains) No (Global) ELM[77] Dirac delta Penalty Function cPINN [78] Yes (Subdomains) No (Global) Fully Connected Dirac delta Penalty Function XPINN [79] Yes (Subdomains) No (Global) Fully Connected Dirac delta Penalty Function

hp-VPINNs [12] No (Global) Yes (Subdomains) Fully Connected Orthogonal Polynomials Penalty Function PhyGeoNet [80] No (Global) No (Global) Convolutional Network (CNN) Dirac delta Strictly Enforced

PIGCN [81] No (Global) No (Global) Graph Convolution (GCN) Trial Function Space Strictly Enforced SPINN [82] No (Global) No (Global) Radial Basis Function Trial Function Space Penalty Function

BINN [83] No (Global) No (Global) Fully Connected Fundamental Solution of PDEs Boundary Integral Terms KINN [84] No (Global) No (Global) Kolmogorov Arnold Network [85] Dirac delta Penalty Function

The strong form of PINNs fundamentally uses a collocation method, where the approximate function is replaced with a neural network. PINNs in the strong form can be applied not only to solve forward problems of PDEs but also to determine unknown coefficients in inverse problems. In inverse problems, some data combined with a data-driven approach is often required, and the loss function includes a norm of the error between predictions and true values, as shown in Eq. (4) for Ldata. Unknown parameters of the inverse problem, such as elastic modulus and Poisson’s ratio, are treated as trainable variables to be optimized. By solving for the gradients of the optimization variables in inverse problems, the parameters needed for the inverse problems are inferred to solve the inverse problem. It is noteworthy that in PINNs, the optimization variables of inverse problems are optimized using Lpdes. The optimization of inverse problems in PINNs can also be split into two parts: initially fitting the data with a neural network without considering the physical equations, and after the fit, optimizing the variables needed for the inverse problem using the PDEs loss. However, in traditional PINNs, the loss from data and PDEs is optimized together through hyperparameters. It is important to note that whether these are split or not, the mathematical optimization goals are the same, essentially solving the same problem but with different optimization strategies. Moreover, traditional PINNs in strong form solving inverse problems (optimizing PDEs loss and data loss together) generally do not manage to make both Lpdes and Ldata zero simultaneously; the optimization process is a trade-off between Lpdes and Ldata, often resulting in Ldata reaching zero faster, while Lpdes tends to optimize more slowly. Lu et al. (2021) [86] proposed the HPINN algorithm, which handles constraints using the augmented Lagrangian method [87], thereby enhancing the accuracy of solving inverse problems.

The strong form of PINNs does not require labeled data when addressing forward problems, although having labeled data can increase the efficiency and accuracy of the algorithm. The strong form of PINNs only requires spatial coordinates to use the powerful approximation capabilities of neural networks to map spacetime fields to the solution space [2]. From the perspective of computational mechanics, it is a type of trial function represented by a fully connected neural network and a Dirac delta mesh-free method for test functions. In their original paper [2], the boundary initial conditions were added by a soft constraint method using penalty functions, which involves adjusting extra hyperparameters. Around the same time, Sirignano et al. (2018) [74] introduced the DGM, which is very similar to PINNs, except that DGM does not address inverse problems. Additionally, DGM proposed using Monte Carlo algorithms instead of AD algorithms for derivative approximation, a method that can reduce the computational demands of high-dimensional problems [88], and DGM mathematically proved the convergence of PINNs in solving quasi-linear parabolic equations. Subsequently, Kharazmi et al. (2019) [75] drew on traditional finite element and numerical analysis ideas to propose VPINNs, a variational form of the weighted residual method that changes the test functions in PINNs from Dirac delta to polynomials and trigonometric functions, thus extending the weighted residual method of PINNs strong formulation. However, VPINNs has limitations; if the test functions use Legendre orthogonal polynomials, higher-order orthogonal polynomials that satisfy the loss function to zero must exist. Given the strong fitting capabilities of neural networks, there’s no reason why the network would not fit higher-order orthogonal polynomials, thereby causing non-uniqueness in the solution [89]. Later, the same authors [12], improved VPINNs and further introduced hp-VPINNs, which are based on VPINNs but involve partitioning, meaning different areas have different test functions. This method found that orthogonal polynomials have high accuracy in this form, and it also compared different

orders of variational weak forms. Jagtap et al. (2020) proposed cPINN [78] and XPINNs [79], which partition the global domain like finite elements into different areas, each using a different neural network as the trial function approximation. However, special handling is required at the interfaces, where continuity conditions for the interface and gradient continuity conditions (related to the highest derivative of the PDEs) must be added to the loss function. For second-order mechanical PDEs, continuity conditions for displacement and force must be added as interface loss function terms. cPINN is suitable for handling problems with drastic changes, using deeper neural networks where changes are large and shallow networks where changes are mild. Shukla et al. [90] integrated parallel algorithms into cPINN and XPINNs, enhancing the efficiency of the partitioned PINNs algorithms.

Most of the work discussed revolves around whether trial functions and test functions are partitioned and the types of test functions. Additionally, some work focuses on changing the type of network used for the trial functions, essentially modifying the trial function’s approximation. Dwivedi et. al (2020) [76] used Extreme Learning Machines (ELM) for PINNs in strong form. ELMs are a type of single hidden layer fully connected neural network, where the single hidden layer is obtained through traditional nonlinear mapping followed by a linear transformation to produce the final output. Notably, unlike traditional FNNs, the nonlinear transformation of the single hidden layer in ELM is randomly initialized and requires no training; ELM only trains the final linear transformation. This brings many benefits, as the optimization in ELM is not iterative but can be accomplished through direct methods to obtain the weights of the linear transformation, significantly reducing the computational load. Therefore, Dwivedi et. al (2020) [76] proposed using ELM to replace the approximation function in the strong form of PINNs, calling this method PIELM. Since ELM sacrifices the expressive power of FNNs for efficiency, PIELM often does not perform well in cases of complex exact solutions. In such cases, partitioning ideas are needed to enhance the approximation capability of PIELM, thus improving its accuracy. Undoubtedly, since PIELM determines the weights of the neural network through direct solution methods, it is more efficient than most works in PINNs based on iterative algorithms. Additionally, some researchers have used new neural network structures to replace fully connected neural networks, such as Gao et al. (2021) [80], who initially proposed PhyGeoNet, which essentially replaces fully connected neural networks with convolutional neural networks. The backward derivation in PhyGeoNet is achieved using fixed-weight convolutional kernels, and PhyGeoNet uses the idea of parametric transformation to solve problems in irregular domains that are challenging for physically based convolutional neural networks. The boundary conditions in this algorithm are strongly enforced. Later, Gao et al. (2022) [81] continued to improve PhyGeoNet and introduced PIGCN, which uses graph neural networks as approximation functions, and the loss function is constructed in weak form. Graph-based learned simulators have emerged as an important direction in computational mechanics. By operating directly on mesh connectivity, graph neural networks naturally accommodate irregular discretizations and preserve local geometric relations, making them particularly attractive for engineering simulations on unstructured meshes [91]. Ramabathiran et al. (2021) [82] proposed SPINN, which uses radial basis functions (RBF) as approximation functions, aiming to reduce the complexity of the neural network. Bai et al. (2023) [92] further validated the use of RBF networks for solving nonlinear equations through systematic verification via NTK (Neural Tangent Kernel) theory [93]. Sun et al. (2023) [83] first combined boundary elements with PINNs methods, using the residual of the boundary integral equation as the loss function. Overall, the experience of changing the network structure of PINNs strong form is that smaller neural networks often lack expressive power, but more complex neural networks are typically difficult to train, so choosing the best neural network structure requires considering the complexity of the problem [7], similar to choosing element types in finite elements, as different element types in finite elements essentially choose different approximation functions, and PINNs choosing network structures essentially also choose different approximation functions. Wang et al. (2024) proposed KINN [84], which uses KAN proposed by Liu et al. (2024) [85] to replace MLP in PINNs, utilizing the strong form, energy form, and inverse form for the first time. Compared with traditional PINNs, the convergence speed and the accuracy of KINN were greatly improved.

In time-dependent PINNs strong form algorithms, there are two ways to solve time-dependent problems: expanding by one dimension or using a time-marching scheme (commonly FDM) [94]. Mattey et al. (2022) [10] proposed bc-PINN, which enhances the computational efficiency and accuracy of PINNs in solving strong nonlinear and high-order dynamic equations. Meng et al. (2020) [95] proposed PPINN, which uses a small network to enhance the efficiency of PINNs algorithms for long-term PDEs problems. Additionally, for data

of different accuracies, Meng et al. (2020) [96] proposed MPINN, which combines high-precision data with low-precision data. In the area of stochastic PDEs, Yang et al. (2020) [26] proposed PIGAN, which combines physical equations with GANs (Generative Adversarial Networks) to solve the direct and inverse problems of stochastic PDEs (SPDEs).

There are several PINN libraries available, such as DeepXDE based on TensorFlow [70], SciANN based on Keras [97], NeuralPDE based on Julia [98], and SimNet [99], which facilitate the application of PINNs in solving PDEs and are suitable for both academia and industry. These libraries facilitate the application of PINNs in solving PDEs.

Table 2 lists several open-source AI for PDEs codes developed for computational mechanics.

- 2.1.2. Energy form DEM is a deep learning method for solving PDEs, designed based on the principle of least action in physics.


When applied to a mechanical system, the principle of least action is manifested as Hamilton’s principle:

H = ˆ t

1

Ldt (5)

t0

where H represents the Hamiltonian action, which is the spacetime functional of the entire system. t0 and t1 represent the initial and final times respectively. L is the Lagrangian function:

L = T − V (6)

where T and V represent the kinetic energy and potential energy of the system, respectively. For an elastic system, the expressions for kinetic energy T and potential energy V are given as:

T = ˆ

Ω

V = ˆ

Ω

- 1

- 2


ρv · vdΩ

ΨdΩ − ˆ

f · udΩ − ˆ

Γt

Ω

¯t · udΓ

(7)

where ρ, v, and Ψ is the density, velocity and the strain energy density respectively. f and ¯t are the body force and the surface force vector at the traction boundary condition Γt, respectively. In DEM, the entire functional H is optimized as the loss function. If we consider a static system where T = 0, DEM uses the potential energy

- V as the loss function as illustrated in Fig. 4. The mathematical form of the DEM loss function is given by:


L = H = ˆ t

1

t0

Ldt = ˆ

ΨdΩ − ˆ

Ω

Ω

f · udΩ − ˆ

Γt

¯t · udΓ (8)

The principle of DEM is to use the minimum potential energy principle under the condition that the displacement field satisfies the essential displacement conditions, i.e., to select the displacement field that minimizes the total potential energy L among all admissible displacements. Note that DEM requires the defintion of an incremental energy and thus not only limited to static problems but it can also deal with transient and history dependent problems including plasticity [112], viscoelasticity [122], damage and fracture [123, 109]. In particular, DEM has been applied to phase field models of fracture [109]. DEM directly optimizes the energy without needing to express virtual work in the corresponding weak form like finite elements. The admissible displacement field is constructed through a neural network, but this admissible displacement field often needs to be pre-built to naturally satisfy the enforced displacement boundary conditions. The construction method for the admissible displacement field u˜(x) is commonly adopted as:

u˜(x) = P(x) + D(x) ∗ u(x;θ), (9)

where P(x) is a boundary network that satisfies the PDEs displacement boundary conditions, i.e., if the coordinate point falls exactly on the essential boundary condition, it outputs the value of the essential boundary condition; D(x) is a distance network, indicating the shortest distance from the current coordinate point to

Operatorlearning

PINNs

###### PINO

DEM:DeepEnergyMethod

ThestrongformofPINNs

DeepONet

###### FNO

ReferenceThelinkofcodeBriefDescriptionofMethod

https://github.com/somdattagoswami/IGAPack-PhaseField[108,109]Phasefieldforfracturemechanics https://github.com/MinhNguyenIKM/dem_hyperelasticity[110]Hyperelasticity

https://github.com/yizheng-wang[29]DEMwithsubdomains https://github.com/weili101/DeepPlates[106,107]Kirchhoffplate

https://github.com/gegewen/ufno[120]Multiphaseflow https://github.com/neuraloperator/Geo-FNO[121]FNOforgeneralgeometries

https://github.com/neuraloperator/neuraloperator[33]Theoriginalcode https://github.com/eshaghi-ms/DeepNetBeam[119]FunctionallyGradedPorousBeams

https://github.com/Jasiuk-Research-Group/ResUNet-DeepONet-Plasticity[118]DeepONetforelastoplastic

https://github.com/lululxvi/deeponet[32]Theoriginalcode https://github.com/lu-group/deeponet-extrapolation[117]DeepONetwithphysicsorsparseobservations

https://github.com/sbuoso/Cardio-PINN/[115]Heart https://github.com/dodaltuin/soft-tissue-pignn[116]Softtissue

https://github.com/MinhNguyenIKM/parametric-deep-energy-method[113]ParametricDEM https://github.com/Jasiuk-Research-Group/DeepEnergy-TopOpt[114]Topologyoptimization

https://github.com/JinshuaiBai/RPIM_NNS[111]Hyperelasticity https://github.com/Jasiuk-Research-Group/DEM_for_J2_plasticity[112]J2elastoplasticity

https://github.com/Raocp/PINN-laminar-flow[104]Incompressiblelaminarflows https://github.com/shengzesnail/AIV_MAOAC[105]Bloodflow

https://github.com/Jianxun-Wang/LabelFree-DNN-Surrogate[102]IncompressibleNS https://github.com/PredictiveIntelligenceLab/DeepStefan[103]Multiphaseandmovingboundaryproblems

https://github.com/Raocp/PINN-elastodynamics[100]Elastodynamics https://github.com/imcs-compsim/pinns_for_comp_mech[101]Contactmechanics

https://github.com/somdattagoswami/IGAPack-PhaseField[47]DEMwithDeepONet https://github.com/yizheng-wang[30]DCEMwithDeepONet

https://github.com/neuraloperator/physics_informed[35]PINNswithFNO https://github.com/PredictiveIntelligenceLab/Physics-informed-DeepONets[42]PINNswithDeepONet

https://github.com/ISM-Weimar/DeepEnergyMethods[31]Theoriginalcode https://github.com/yizheng-wang[30]DCEM

https://github.com/XuhuiM/PPINN[95]Time-dependentPDEs https://github.com/sciann/sciann-applications/tree/master/SciANN-SolidMechanics-BCs[24]Solidmechanics

https://github.com/AmeyaJagtap/Conservative_PINNs[78]PINNswithsubdomains https://github.com/lululxvi/hpinn[86]Inversedesign

https://github.com/maziarraissi/PINNs[2]Theoriginalcode https://github.com/ehsankharazmi/hp-VPINNs[12]VariationalPINNs

Table2 ThecodesofAIforPDEsincomputationalmechanics

#### (a) (b)

###### Neural Network

Particular Netθp

Data loss

Pretrain

P1

###### a

UX

Boundary Condition

- X

Z

a

a

a

a

a

- Y


Pm

Optimize First

a

a UY

Stress function

UZ

a

Basis Netθba

x1

Input Layer (Coordinates) Hidden Layers Output Layer

Pretrain

P1

Pm

No: Update Parameters

xm

Optimize Second

Minimum ?

Internal Energy

| |Integral|
|---|---|
| |Admissible|


| | |
|---|---|
| | |


Trunk Net θt

P1

u(x;θ)

Pm

Yes

Potential energy

Complementary energy

ible Displacement

Minimize

θbr

Branch Net

FNN CNN RNN

θt θbr

Geometry

External Energy

Material Force ...

Done

Transformer ...

- Fig. 4. AI for PDEs method: Schematic of PINNs energy form [31] (a) DEM based on the principle of minimum potential energy


- [31], (b) DCEM based on the principle of minimum complementary energy [30].


the nearest essential boundary condition location; u(x;θ) is a generalized network that needs to be trained by substituting it into the minimum potential energy loss function. The idea of the admissible displacement field to satisfy the essential boundary conditions also exists in meshless methods [124]. Note that boundary and distance networks do not necessarily need to be neural networks; choosing any other fitting function, such

- as Radial Basis Function (RBF) [29] is also possible. We discuss the construction method of the admissible displacement field in detail in Section 3.4.


In the study of PINNs energy form, we provide a review of the status of PINNs energy form from four perspectives: whether subdomains are partitioned (whether trial functions are partitioned), types of trial functions, how essential boundary conditions are applied, and what kind of energy principle is used, as shown in

- Table 3 on the current state of research on PINNs energy form. Sheng et al. (2021) [125] extended Deep Ritz and proposed PFNN, using distance, boundary, and generalized networks to construct admissible displacement fields. Fuhg et al. (2022) [126] proposed a classical mixed formulation mDEM, which integrates strong form, energy form, and constitutive equations into the loss function for optimization. Nguyen-Thanh et al. (2021) [113] expanded DEM with P-DEM, borrowing the idea of parametric elements from finite elements to address complex geometric boundary problems. Wang et al. (2022) [29] expanded DEM and proposed CENN, proposing a subdomain form of the deep energy method. In terms of neural network structures, He et al. (2023) [127] introduced GCN-DEM, replacing the original fully connected neural network with a graph convolutional neural network. As current deep energy forms are based on the minimum potential energy principle, Wang et al. (2023) [30] first used the minimum complementary energy principle to propose DCEM, which parallels the deep energy method DEM, and combined operator learning with physical equations, making it an important complementary form to DEM. Wang et al. (2024) proposed KINN [84], which utilizes KAN, as proposed by Liu et al. (2024) [85], to replace MLP in PINNs, and employed strong form, energy form, and inverse form for the first time.


- 2.2. Operator learning Neural operators learn the mapping between different functions, which has extensive applications in science


and engineering [34]. For instance, the input function could be the boundary conditions of a PDEs, and the output is the function field of interest. Although functions are infinite-dimensional in mathematical terms, in practice, we often input discretized data on a finite mesh to approximate continuous functions.

###### Table 3 Current status of PINNs energy form methods

Methods Trial function: subdomains Trial function: type Method of Imposing Essential Boundary Energy Principle Deep Ritz [23] No (Global) Fully Connected Penalty Function Variational Principle

DEM [31] No (Global) Fully Connected distance, boundary, and generalized networks Minimum Potential Energy PFNN [125] No (Global) Fully Connected distance, boundary, and generalized networks Variational Principle mDEM [126] No (Global) Fully Connected distance, boundary, and generalized networks Mixed Form P-DEM [113] No (Global) Fully Connected Penalty Function Minimum Potential Energy

CENN [29] Yes (Subdomain) Fully Connected distance, boundary, and generalized networks Minimum Potential Energy

GCN-DEM [127] No (Global) Graph Convolutional (GCN) distance, boundary, and generalized networks Minimum Potential Energy PIRBN [92] No (Global) Radial Basis Function distance, boundary, and generalized networks Minimum Potential Energy DCEM [30] No (Global) Fully Connected distance, boundary, and generalized networks Minimum Complementary Energy

KINN [84] No (Global) Kolmogorov Arnold Network [85] distance, boundary, and generalized networks Minimum Potential Energy

Unlike previous data-driven methods based on neural networks, operator learning is discretization-invariant, characterized by:

- • The ability to input at any resolution.
- • The capability to output at any location.
- • Convergence of results as the mesh is refined.


Traditional neural network-based data-driven algorithms are often related to the degree of discretization; once the resolution of the input-output functions is changed, the model usually needs to be retrained. However, operator learning does not need to restart training for data of different resolutions due to the characteristic of the discretization-invariance. Additionally, not all fitting algorithms can be termed as neural operators. Neural operators not only need to satisfy discretization-invariance but also meet the requirements of the generalized approximation [37]. It can be said that neural operators are a superior class of algorithms within operator learning, such as the Fourier Neural Operator (FNO) [33]. Operator learning can be applied not only in deterministic models but also in probabilistic models, like the diffusion model [128], to learn the probability density in function spaces, such as solving stochastic PDEs. Physics-informed diffusion models combine scorebased generation with physical constraints and have recently shown strong potential in scientific computing tasks, especially for structural topology optimization [15].

The design philosophy of operator learning algorithms is shown in Fig. 5a, with the core being the kernel integral method in the neural operator layers:

H(t)(v(t);θ(kt))(x) = ˆ

D(t)

k(t)(x,y;θ(kt))v(t)(y)dy, (10)

- where v(t)(y) is the input to the neural operator layer; k(t)(x,y) is the kernel function, similar to the Green’s


function in linear PDEs, and k(t)(x,y) is approximated using neural networks, where θ(kt) are the parameters for approximating the kernel function. The reason it’s a kernel integral method is that the kernel operator H(t) acts on the function v(t), and through integration, H(t) transforms v(t) into another class of functions H(t)(v(t))(x). H(t) is similar to integral transformations in mathematical equations. In terms of methods of mathematical physics, H(t)(v(t))(x) is referred to the image function, v(t)(y) is the original function, and k(t)(x,y) is the kernel function. Note that the t index indicates the t-th neural operator layer. Hence, the overall computation process of the operator learning is:

Gθ(a(x);θ) =Q(v(T+1);θQ) ◦ σ[H(T)(v(T);θ(kT)) + W(T)(v(T);θ(wT)) + b(T)(θ(bT))] ◦ ···

, (11)

◦ σ[H(1)(v(1);θ(1)k ) + W(1)(v(1);θ(1)w ) + b(1)(θ(1)b )] ◦ P(a(x);θP)

where P and Q are respectively for elevating and reducing dimensions of the original data, with corresponding learnable parameters θP and θQ. H(t), W(t), and b(t) are respectively the kernel integral, linear transformation, and bias, with the corresponding learnable parameters being θ(kt), θ(wt), and θ(bt). Note that these learnable parameters are generally approximated using neural networks.

(a) (b)

a

P Layer 1 Layer t Layer T Q u

Input Function u Coordinate y

u(xj) u(xm)

u(x1)

|Trunk Net 1|
|---|


|Branch Net 1|
|---|


- 1

NNB

- 2


- 1

NNT

- 2


###### ( )

, ; ()( )d ()( ())

|Trunk Net 2|
|---|


|Branch Net 2|
|---|


( ) ( )

t t t t t D k b

NNB

∫ k x y θ v y y +b θ

NNT

( )

t

v(t−1)

σ

v(t)

W

|Trunk Net p|
|---|


|Branch Net p|
|---|


p NNB

p NNT

Graph Neural Operator (GNO)

G(u,y)

y

v(t−1)

σ

v(t)

W

Output Function

(c)

Low-rank Neural Operator (LNO)

a

u

Different Neural Operator Layers

P Q

v(t−1)

Fourier Layer 1 Fourier Layer t Fourier Layer T

σ

v(t)

W

mode

mode

ℜ

 −1



Fourier Neural Operator (FNO)

v(t−1) σ v(t)

v(t−1)

σ

v(t)

W

W

- Fig. 5. AI for PDEs Method: Schematic of Operator Learning. (a) Neural Operator Layer Structure: Graph Neural Operator (GNO) [129], Local Neural Operator (LNO), and Fourier Neural Operator (FNO) [33] can serve as the core of the neural operator architecture [34]. (b) Details of DeepONet [32]. (c) Details of FNO [33].


Different choices of kernel functions constitute various operator learning algorithms, hence designing the kernel function is central to operator learning. When specifically forming a Fourier transform, it results in the Fourier Neural Operator (FNO). There is theoretical evidence that Eq. (11) meets the general approximation requirements [130, 131], hence operator learning algorithms designed according to Eq. (11) possess excellent convergence properties. DeepONet [32] also meets the general approximation requirements [37], essentially designed through the theory proposed by [37]. Although the FNO and DeepONet are designed differently, they both exhibit excellent convergence properties. The two most typical algorithms in operator learning are FNO and DeepONet, thus this paper will focus on these two algorithms below.

- 2.2.1. FNO: Fourier neural operator The Fourier Neural Operator (FNO) is an operator learning algorithm introduced by Li et al. (2020) [33],


which has received considerable attention. The initially proposed FNO is a completely data-driven model. Even earlier than FNO, the same first author, Li et al. [129], used graph neural networks to learn relationships between field variables (GNO), but FNO demonstrated better performance than GNO. The essence of FNO involves integrating Fourier transforms into operator learning, representing Eq. (10) with a Fourier transform:

H(t)(v(t);θ(kt))(x) = ˆ

D(t)

k(t)(x,y;θ(kt))v(t)(y)dy = F−1 ◦ ℜ ◦ F(v(t)(x)), (12)

where F and F−1 are the Fourier transform and its inverse, respectively, R is a linear transformation. To clarify the process of the FNO algorithm, we combine the framework and examples of the FNO algorithm. The framework of the FNO algorithm is shown in Fig. 5c.

As a simple illustrative example of the capability of FNO, we consider the one-dimensional Burgers equation, which is commonly used as a benchmark problem because of its nonlinear and space-time-dependent characteristics. u denotes the field variable to be solved, ν is the viscosity coefficient, and the boundary conditions are fixed. For a given initial condition u0, the corresponding solution u is uniquely determined. Thus, in this

problem, the input is the initial condition u0 ∈ Rd

i (i.e., a(x) in [33]), and the output is u(x,t1) at a future time t1. The FNO algorithm process first uses a fully connected neural network P to elevate the dimension of the input a(x) to dc (i.e., P : R → Rd

c, dc similar to channels in computer vision):

i∗dc. (13)

v(0)(x) = P(a(x)) ∈ Rd

Next, v(0)(x) is sent into Fourier layer, where each channel of v(0)(x) undergoes a Fourier transform, transforming into:

f(1)(x) = F(v(0)(x)) ∈ Cd

i∗dc. (14)

High frequencies are filtered out, retaining low frequencies, and cutting off the frequency at dm(1 ≤ dm ≤ di), thus the data structure transforms into f(1)(x) ∈ Cd

m×dc. A linear transformation R is applied to each frequency of all channels:

f(1)L (x) = ℜ(f(1)(x)) ∈ Cd

m∗dc. (15)

Since different frequencies use different linear transformations, there are dm linear transformation matrices, and the linear transformation is from dc to dc, so the linear transformation matrix is Rd

c×dc×dm. After the linear transformation R, the data’s dimensional structure is not changed. Since the next step involves Fourier inverse transformation, high frequencies removed by cutting are replaced by zeros. Fourier inverse transformation is

performed on f(1)L (x):

v(1)f = F−1(f(1)L (x)) ∈ Rd

i∗dc. (16)

The advantage of the linear transformation R is that it learns the mapping relationships between data in the Fourier frequency space while filtering out high frequencies. R is a special form of regularization that reduces overfitting and enhances the model’s generalization capability.

Furthermore, using the idea of residual networks from [132], another linear transformation is directly applied to the channels of v(0)(x), the same linear transformation for all different frequencies, only one linear transformation, i.e., W ∈ Rd

c×dc:

v(1)L = W(v(0)(x)) ∈ Rd

i∗dc. (17)

- W uses the idea of residual networks to reintroduce high-frequency components filtered out by the Fourier transform back into the network for learning, preventing a decrease in network prediction performance due to the high frequencies filtered out by the Fourier transform. The results of the Fourier transform and the linear transformation are added together to obtain:


v(1)(x) = σ(v(1)f + v(1)L + b(1)) ∈ Rd

i∗dc, (18)

where b(1) is the bias. Adding a nonlinear transformation σ not only increases the network’s expressive capability but also further enhances the high-frequency fitting capability. The Fourier layer is the computational core of FNO, and the above operations are repeated T times to obtain v(T)(x). Finally, the dimension dc is reduced to the target dimension by Q : Rd

→ R.

c

The two major advantages of FNO are, first, since the Fourier transform filters out high-frequency modes, it can enhance the model’s speed and generalization ability, reducing overfitting; second, discretization-invariance, since all operations in FNO are unrelated to the data’s mesh and are based on point-wise operations, so it has the advantage of discretization-invariance. The initially proposed FNO has two major flaws. First, the Fourier Neural Operator (FNO) employs the fast Fourier transform, which requires the input data to be defined over a regular domain. Although it is feasible to enclose an irregular domain within a larger regular one, this approach often yields suboptimal results. To address this, Li et al. [121] introduced Geo-FNO, specifically designed to handle irregular domains effectively. Second, while FNO requires data points to be positioned on a uniform mesh, points on an uneven mesh must be converted into a uniform mesh using interpolation. Thus, the error of interpolation decreases the accuracy of FNO. An alternative to Geo-FNO is ϕ-FEM-FNO [133], where the geometry is described by signed distance functions (SDFs), usually level sets as in CUTFEM [134]. This approach avoids interpolation entirely because the training data is generated on the same background grid and the SDF implicitly encodes the geometry without remeshing. It inherits the same difficulties as CUTFEM.

Most importantly, for problems requiring geometry evolution, the level set must be updated, and the error from the transport equation solves accumulates. This occurs frequently in fluid mechanics and problems in solid mechanics involving history dependent constitutive models with large deformations and fracture.

- 2.2.2. DeepONet The general operator learning framework introduced in Eq. (11) constructs neural operators through iter-


ative kernel integral layers, with the key distinction among methods being the parameterization of the kernel function (for example, FNO employs Fourier-based integral kernels). As an alternative and equally important implementation of operator learning, DeepONet follows a different design principle: it builds upon the universal operator approximation theorem [37] and decomposes the operator into an inner product of two subnetworks, the Branch and Trunk networks. The mathematical structure of DeepONet is analogous to a Taylor series:

f(u)(x) =

n

αi(u)ϕi(x). (19)

i=1

As illustrated in Fig. 5b, the Trunk net employs neural networks to approximate the basis functions ϕi(x). Trunk net shares a common idea with PINNs, where neural networks fit from the coordinate space to the target function. However, in DeepONet, it is the basis functions ϕi(x) that are fitted by the Trunk net, rather than the target functions. The coefficients before the basis functions αi(u) are fitted by the Branch net. It is noteworthy that inputting the same function into the Branch net produces fixed weights αi(u), aligning with the concept of function approximation in numerical analysis. Unlike traditional function approximation algorithms that preselect basis functions, DeepONet uses neural networks to adaptively select suitable basis functions and weights based on data.

Since the Trunk network is similar to PINNs, we can apply automatic differentiation algorithms in PINNs to construct partial differential operators and obtain new loss functions (strong or energy form). If the Branch network is fixed, DeepONet can be reduced to PINNs.

DeepONet’s network structure is constructed according to the theory of universal operator approximation from [37]. The mathematical form of this approximation theory in [37] is:

 σ(Wk · y + Bk) |< ϵ. (20)

 

p

m

n

wijk u(xj) + bki

cki σ

| G(u,y) −

j=1

i=1

k=1

DeepONet replaces the terms in the above equation with neural networks:

 

 

n

m

NNBk(u(x);θBNN) =

cki σ

wijk u(xj) + bki

i=1

j=1

, (21)

NNTk(y;θTNN) = σ(Wk · y + Bk) NNO(y;u) =

p

NNBk(u(x);θBNN) · NNTk(y;θTNN)

k=1

where NNBk, NNTk, and NNO are respectively the Branch network, Trunk network, and the output of DeepONet. u(x) can be approximated from sensors x (discrete points approximating a continuous function). For instance,

if the input u(x) of NNB is the gravitational potential energy of a three-dimensional cubic material over [0,1]3, then the gravitational potential energy field within [0,1]3 might be sampled at 0.01 intervals taking 1013 points. Data structure of u(x) can vary, such as data structures similar to images. Therefore, we can use network structures for the Branch network that are appropriate for the type of data, such as CNNs for local features similar to image data, and RNNs for time-related features. It is important that the network structure of the Branch network must consider the particularities of the problem to choose the most appropriate network structure. Thus, u(x) determines the output of the Branch network in DeepONet, which is related to the

weights αi(u) in Eq. (19) and is independent of the coordinates of interest. Similarly, the coordinates fully determine the output of the Trunk network, precisely defining the basis functions ϕi(x) in Eq. (19). Therefore, DeepONet shares many similarities with traditional function approximation. It can be said that DeepONet can adaptively learn basis functions and weights based on data. For more details and extensions on DeepONet, see

- [32]. For the comparison between FNO and DeepONet, Lu et al. [13] systematically analyzed both methods.


They introduced enhancements to FNO to handle mappings of different dimensionalities and complex geometries, while also improving DeepONet to accelerate training and enhance accuracy, supplemented by theoretical comparisons.

- 2.3. PINO: Physics-informed neural operator The concept of the Physics-Informed Neural Operator (PINO) was proposed by Z. Li et al. (2021) [35]. As


shown by the black lines in Fig. 6, the idea is very concise: first, operator learning is trained using big data, then a good initial solution is provided on the test set using operator learning, which is then fine-tuned based on physical equations. Since the initial solution is not arbitrarily given but inferred from historical data, it only needs some adjustment to be fine-tuned to the true solution. Therefore, theoretically, the PINO algorithm not only possesses very high precision (since it is controlled by physical equations) but also leverages the efficiency advantage of operator learning. The above process involves using operator learning to provide an initial solution, followed by fine-tuning with PDEs. For example, [30] isolates the training of physical equations and data. The approach first uses purely data-driven training for operator learning and then fine-tunes with PDEs for specific problems. Additionally, PDEs and data can be combined together to train an operator constrained by physical equations, similar to the training mode of PINNs. For example, Wang et al. (2021) [42] proposed combining DeepONet with physical equations, and combined the data loss with PDEs loss together. Later, Goswami et al. (2022) [47] built on the idea proposed by [42] to predict crack propagation (by combining DeepONet with the phase field method of predicting crack path). Currently, there is no conclusion as to which method is better; both are still being explored. The advantage of isolating the training of PDEs and data is that it can avoid catastrophic forgetting and reduce hyperparameters, specifically those used to balance data and PDE losses. The downside is that it requires additional fine-tuning on new PDEs, thereby increasing the testing time. On the other hand, integrating PDEs and data during training has the advantage of high efficiency during the testing period, as PDEs are already incorporated into the operator during training. However, this undoubtedly increases the training time. Additionally, it introduces extra hyperparameters to balance the data and PDEs, and faces the risk of catastrophic forgetting [135]. This occurs because the PDEs under the current parameters can significantly lose the knowledge and performance of the PDEs under previous parameters, thereby increasing the training cost.

Although incorporating PDEs to train neural operators increases computational cost, it remains an effective approach in scenarios where data is scarce but PDEs are available. Eshaghi et al. [46] proposed the Variational Physics-Informed Neural Operator (VINO). Unlike PINO, VINO leverages the variational form of PDEs to train a fully Fourier Neural Operator, and further employs finite element shape functions to replace automatic differentiation (AD) in computing differential operators, thereby enhancing the stability and accuracy of derivative computations through more precise integration. Similarly, Wang et al. [6] proposed the Pretrained Finite Element Method (PFEM), a physics-driven framework that bridges the efficiency of neural operator learning with the accuracy and robustness of classical finite element methods (FEM). Like VINO, PFEM fully exploits the governing PDEs to train the neural operator. PFEM employs Transolver [44] as the backbone operator. Unlike FNO, which requires a structured rectangular grid, Transolver operates directly on point clouds, providing a flexible and efficient approach for future large-scale computational mechanics models. In addition, PFEM uses the Transolver-predicted solution as an initial guess for the iterative FEM solver, significantly reducing the number of iterations required while maintaining high accuracy.

Another way of combining data and physical equations is for some complex physical processes [36], which refers to those that cannot be accurately described based on current understanding and can only be approximated by some physical equations. We can use PINNs to solve for an approximate solution (low-fidelity) based on approximate physical equations and boundary conditions, and then adjust the deep parameters of the neural network according to the available data, thereby obtaining a data-based solution (high-fidelity) that does not

Big Data

![image 2](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile2.png)

![image 3](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile3.png)

Data Loss

Neural Operator

PDEs Loss

Optimize

Initial Solution

Approximate PDEs Physical Laws

Fine-tuning

![image 4](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile4.png)

Limited Data

![image 5](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile5.png)

Fine-tuning

Approximate Solution More accurate Solution

- Fig. 6. AI for PDEs method: Schematic of Physics-Informed Neural Operator (PINO). There are two implementation approaches. The first, depicted by the black lines, is suitable for scenarios with precise physical equations. Initially, the neural operator is trained using extensive data and physical equations. The method involves using the neural operator to provide an initial solution and establishing a data loss with the data labels, followed by constructing a PDEs loss based on the physical equations. The combination of data loss and PDEs loss allows for more effective training of the neural operator compared to purely data-driven methods [35]. After training, the neural operator is fine-tuned with the physical equations of specific problems to provide highly accurate solutions. The second approach, depicted by the red lines, is suited for cases with only approximate physical equations, such as complex phenomena not well understood by humans. This method starts with an approximate solution derived from the approximate PDEs, which is then fine-tuned using limited data [36].


require exact knowledge of the physical process. This allows us to fuse experimental data with approximate physical equations, as shown by red lines in Fig. 6. Although this method of combination currently does not use operator learning, it can be easily modified using operator learning algorithms when obtaining high-fidelity results in the future, which is a promising direction, specifically targeting those complex physical processes and combining operators with physical equations.

Given that the concept of Physical Neural Operator (PINO) was only recently introduced, numerous research challenges remain to be explored. Key questions include how to more effectively integrate physical equations into operator learning, how to handle noisy data, and how to perform learning with limited samples. In this paper, we focus on the first issue, as we have encountered significant difficulties in integrating physical equations into operator learning. Specifically, after training the Fourier Neural Operator (FNO) with large datasets, we observed a sudden increase in the loss function when incorporating physical equations via finite difference methods. This increase in loss reduces efficiency. In some extreme cases, the combination of data and PDEs may even be worse than using physical equations directly (without data). We hypothesize that this issue arises due to a non-overlapping optimization space between data loss and physical equation loss, which leads to difficulties in their integration. Despite these challenges, we believe that PINO holds substantial promise for academic research. Its theoretical foundation is both robust and promising, providing ample opportunities for exploration and innovation.

Since the PINO inherently combines operator learning with physical equations, it can be seen as encompassing both Physics-Informed Neural Networks (PINNs) and operator learning. If only physical equations are utilized, PINO reduces to PINNs; if solely data-driven methods are applied, PINO reduces to operator learning.

- 2.4. Summary This chapter introduced the methodologies of AI for PDEs, including PINNs, operator learning, and physics-


informed neural operators. Specific algorithms have been reviewed in their respective sections. Here, we discuss notable points and potential directions for future research:

The advantage of the strong form of PINNs in solving high-dimensional problems arises not from the neural network itself but from the way the loss function is computed, specifically through Monte Carlo integration. Monte Carlo integration is a well-established area in applied statistics, and many concepts from this field can be borrowed to enhance PINNs, such as variance reduction techniques. These techniques involve altering the probability density of sampling points to reduce the variance of the Monte Carlo integral, which is crucial for the convergence speed of PINNs. The smaller the variance of the loss function, the faster the convergence of PINNs. The selection of collocation points has always been a core issue for PINNs. Therefore, combining Monte Carlo integration techniques from applied statistics with PINNs is essential for optimizing point selection and reducing variance, thereby accelerating convergence.

Although energy-based PINNs often achieve higher accuracy and computational efficiency than strongform PINNs in many mechanics problems, and usually involve fewer manually balanced hyperparameters [107], their applicability is restricted by the existence and mathematical properties of the underlying variational functional. Not all PDEs admit a corresponding energy formulation, and energy-based approaches generally impose higher requirements on numerical integration accuracy. A fundamental mathematical limitation arises when the variational formulation leads to a stationary saddle-point problem rather than a true minimization problem. In such cases, the loss function seeks a saddle point instead of a minimum, which substantially increases optimization difficulty. Although dedicated saddle-point optimization methods such as the Alternating Direction Method of Multipliers (ADMM) may provide partial improvement, reliable convergence remains challenging in practice. In addition, neural-network-based optimization introduces a second level of difficulty: the loss landscape itself is highly non-convex and contains numerous spurious stationary points. As a result, even when a stationary point is reached, it is often difficult to determine whether it corresponds to the physically correct saddle-point solution of the original variational problem. This issue becomes particularly severe when generalized variational principles are adopted, such as the Hu–Washizu three-field variational principle or the Hellinger–Reissner mixed variational principle, whose stationary solutions are not naturally associated with easily identifiable optimization targets in neural parameter space. Therefore, energy-based PINNs are most naturally applicable when the governing functional is bounded below and locally coercive, for example when δ2L > 0, where L denotes the variational functional. By contrast, strong-form PINNs do not rely on variational

structure and therefore remain more broadly applicable across general PDE classes, although they introduce their own challenges such as residual balancing and boundary-condition enforcement. Future progress in PINNs will depend not only on developments in computational mechanics formulations, but also on advances in optimization algorithms for highly non-convex scientific machine learning problems.

Operator learning algorithms essentially learn the implicit mapping of PDE families through big data. The main operator learning algorithms currently are FNO and DeepONet, both supported by corresponding theories. The core of these algorithms is the kernel integral method, and different kernel integral schemes can give rise to various operator learning algorithms. While Fourier transformation is currently in use, other transformations such as Laplace transform and Z-transform can be considered special cases of kernel integration, leading to diverse neural operator algorithms. Additionally, DeepONet is based on the mathematical proof of approximating continuous operators by neural networks from 1995 [37], substituting this mathematical proof’s convergence criteria with neural networks. We believe that other theories have proven the same thing, that neural networks can approximate any continuous operator. As a result, other theories can be exploited to create various algorithms similar to DeepONet in the future.

The algorithm based on the physics-informed neural operator is particularly interesting and has significant research and industrial application prospects. This is because this method can continually self-learn. The algorithm can become faster over time, and with gradually increasing data, it can train increasingly accurate operators. Essentially, the connection is universal; although the problems we are currently solving have not precisely appeared in the training set, they share similarities, and we can leverage existing data for unknown tests, and then correct them based on physical equations. The larger the dataset, the more accurate the initial solution predicted by operator learning will be, and thus the physical equation correction time will be shorter. Another combination method is for unknown phenomena, where an approximate equation can provide an approximate solution, which is then fine-tuned based on data, making it very suitable for complex phenomena, such as biomechanics.

In this chapter, we primarily introduced some methodologies of AI for PDEs. In the next chapter, we will introduce some theoretical research on AI for PDEs, focusing on PINNs. In addition, recent studies have begun exploring the use of foundation models for assisting AI4PDE development through automatic scientific programming [16]. Beyond code generation, AI agents are attracting increasing attention because they offer the possibility of end-to-end scientific workflow automation, including problem formulation, solver construction, execution, and result interpretation [136]. In computational mechanics, geometry modeling is widely recognized as one of the most time-consuming components in simulation pipelines, often requiring substantial user interaction during preprocessing. Recently, Wang et al. [137] integrated large language models into the deep energy method framework, demonstrating that foundation models can assist geometry generation and preprocessing under natural-language instructions. Although the integration of AI agents with AI4PDEs is still at an early exploratory stage, it represents a highly promising future direction. In particular, foundation models may gradually support automatic hyperparameter adjustment in PINNs, adaptive balancing of multiple loss terms, architecture selection, and solver strategy optimization, thereby improving both usability and efficiency of AI4PDE solvers.

###### 3. AI for PDEs: Theoretical Research

- 3.1. Activation functions


The choice of activation function affects the function representation of PINNs. Essentially, the activation function determines the degree of nonlinearity, thereby altering the neural network’s fitting ability. The tanh function is the most commonly selected activation function for PINNs, though other non-linear activation functions are also viable. PINNS must avoid activation functions with discontinuous higher-order derivatives or those whose higher-order derivatives are identically equal to zero, because PDEs often contain higher-order derivatives. The chain rule results in an ineffective optimization when the derivative of the activation function is not satisfied with the above condition. Therefore, activation functions like ReLu, which have a second-order derivative of zero, should not be chosen in higher-order derivative PDEs, especially when the highest order of the derivatives in the PDEs is greater than or equal to 2. The above is achieved by specifically changing the

type of activation function to alter the accuracy and efficiency of PINNs. However, Jagtap et al. [138] proposed a strategy applicable to any activation function, involving the multiplication of a trainable parameter a after each neural network linear transformation layer, and the idea behind the strategy is similar to KAN [85]. This parameter alters the activation function shape to achieve faster convergence, expressed mathematically as:

u(x) = (Lk ◦ σ ◦ naLk−1 ◦ σ ◦ naLk−2 ··· ◦ σ ◦ naL1)(x), (22)

where n is a non-trainable parameter set to determine the basic shape of the activation function, Li (where i ranges from 1 to k) represents the linear mapping layers of the network, and σ is the non-linear activation function. Later, Jagtap et al. [139] further refined the algorithm by independently adjusting each linear layer’s a and added a loss function term for a, aiming to increase a to prevent gradient vanishing and thus further speeding up convergence. Essentially, the concept behind adjusting the activation function shape resonates with regularization in machine learning.

- 3.2. Errors


The errors in AI for PDEs primarily consist of four components: approximation error, optimization error, generalization error [32], and integral error.

Although neural networks have the capability to approximate any continuous function, a specific neural network structure must still be selected. Therefore, there will inevitably be some discrepancy between the solution space of the neural network and the actual solution space, which constitutes the approximation error. Optimization error refers to the error arising from the local optima due to the highly non-convex nature of neural networks. Generalization error is generally not specific to PINNs but is raised concerning operator learning because PINNs solve specific problems described by physical equations, whereas operator learning studies families of PDEs. Thus, operator learning deals with physical problems across different geometries, constitutive models, and boundary conditions, making generalization error a measure of how well operator learning approximates a family of PDEs. PINNs involve an integral error, which is determined by the number and distribution of collocation points. In the strong form of PINNs, integral error refers to the discrepancy between the integral of the least squares loss function and the exact integral. In the energy form of PINNs, integral error refers to the discrepancy between the integral over the energy functional and the exact energy functional. Most loss functions in PINNs typically use Monte Carlo integration for approximation. The expectation of Monte Carlo integration generally matches the exact value, and the variance measures the convergence efficiency of the integration. The expectation and variance of Monte Carlo integration are determined by the way collocation points are arranged. Therefore, researching how to reduce errors and enhance accuracy in PINNs by studying collocation methods is crucial, as these methods can reduce integral error.

Fig. 7 shows a visual representation for an intuitive understanding of errors in PINNs. For better comprehension, we compare PINNs with traditional computational mechanics methods. In traditional computational mechanics, such as finite element methods, the size of the function space for approximation is determined by the type and number of elements. In contrast, PINNs use neural networks as approximation functions, so the function space is significantly larger due to the universal approximation [140]. However, due to the optimization methods and the highly non-convex nature of neural networks, the full potential of PINNs’ powerful fitting capabilities is not realized, leading to optimization error. Additionally, the integral error introduced by the collocation method determines the extent to which the PINNs’ loss function approximates the true loss function, thus also limiting the approximation capability of PINNs. Finally, because the structure of the neural network is specifically given, the mathematical operations behind PINNs are very clear, meaning the approximation function space is already determined and the gap between the function space of NN and the exact solution introduces approximation error. From this perspective, the structure of the neural network plays a role similar to the element type in finite elements, as both determine the approximation function space. Displacement finite elements obtain nodal displacement values which is used to acquire the physical field of the entire domain through interpolation with shape functions, while PINNs simulate field variables by optimizing neural network parameters. Thus, the parameters of the neural network in PINNs are analogous to the nodal displacements in finite element methods.

Determined by Optimization Methods

Determined by NN Architectures

Whole Function Space

Function Space of PINNs

Determined by Type and Number of Elements in FEM

Exact solution

Solution by PINNs

Function Space of Finite Element Method

Integral error

Optimization error

Approximation error

Gradient Decent

Initial solutoin

Fig. 7. Error comparison between PINNs and FEM.

To better understand the integral error in PINNs, we provide the following example to illustrate. Consider a simple ordinary differential equation example [89]:

′′

(x) = 0 x ∈ (−1,1) u(−1) = 0 ,u(1) = 1

u

. (23)

If we select Nu + 2 points between -1 (inclusive) and 1 (inclusive), excluding x = 0, to construct the loss function for the strong form of PINNs, we observe an interesting phenomenon. The loss function is:

Nu

1 Nu

′′

(xi)|2 + u(−1)2 + [u(1) − 1]2. (24)

|u

Loss =

i=1

As Nu approaches infinity, it is easy to verify that the piece function in Eq. (25) can make the loss function in Eq. (24) zero.

0 x < 0 x x ≥ 0

(25)

u(x) =

However, the exact solution to Eq. (23) is u(x) = x + 1/2. Due to the powerful fitting capabilities of neural networks, theoretically, exact solution and Eq. (25) both could potentially be optimized (in fact, many other solutions that satisfy the zero loss function also exist). The phenomenon of non-unique solutions is not only due to the powerful fitting capabilities of neural networks but also due to the integral error in PINNs. The neural network brings theoretical advantages of a large approximation function space but also introduces the drawback of non-uniqueness in numerical solutions (traditional methods are very robust and stable due to the limitations of approximation function space). Because the approximation function space of the neural network is very large, regularization techniques are crucial for AI for PDEs [7].

We summarizes articles related to mathematical proofs of convergence for AI for PDEs. As shown in

- Table 4, the proofs are divided into three main parts: the first part concerns the convergence proofs for both


y

y

y

f

f

x

x

a x∈[a,b] b

a b

a

b

w1,b1

 − ≤ ≤

1, 0.5 0.5 0,

x others

A ne transformation

y

y

y

=   σ=1

σ

w1x +b1

x

x

a

b

-0.5 0.5

-0.5 0.5

-0.5 0.5

−0.5 ≤ w1x +b1 ≤ 0.5

−0.5≤ w2x+b2 ≤ 0.5 −0.5 ≤ wNx +bN ≤ 0.5

y

y

y

( )

s2σ w2x+b2 ( )

s1σ(w1x +b1)

sNσ wNx +bN

f

f

f

x

x

−

0.5 b w − − 1

0.5 b w

1 1

1

w2,b2,s2 wN,bN,sN

w1,b1,s1

N

N

###### ( )

= ∑ +

= ∑ +

NN x sσ w x b

NN x sσ w x b

( )

( ) lim ( )

i i i N

i i i i

→+∞

=

1

=

N →+∞ 1

i

f

Fig. 8. A brief explanation of the universal approximation theorem for neural networks.

direct and inverse problems in PINNs, along with proofs that neural networks can approximate any continuous function and articles on uncertainty estimates in PINNs; the second part relates to operator learning, which includes proofs that neural operators can approximate any continuous operator, specific proofs of convergence for the Fourier Neural Operator (FNO) within neural operators, and proofs that DeepONet can approximate any continuous operator, meaning it can approximate any family of continuous PDEs; the third part discusses how Physics-Informed Neural Operators (PINO) can approximate any continuous function or any continuous operator.

In summary, a single-layer feedforward network can represent any continuous function (universal approximation theory) [141]. Fig. 8 briefly illustrates the core concept of the universal approximation theory. To explain it briefly, we consider an arbitrary one-dimensional continuous function f(x), where x ∈ [a,b]. We approximate

it using a fully connected neural network NN(x) = Ni=1 siσ(wix + bi), where the activation function is chosen as:

σ(x) =

1 if − 0.5 ≤ x ≤ 0.5 0 otherwise

(26)

It is easy to observe that wix + bi is non-zero only when it lies within the range [−0.5,0.5]; outside this range, the result is zero. Therefore, after applying the activation function σ, the range of x where σ(wix + bi) is non-zero can be expressed as:

−0.5 − bi wi ≤ x ≤

0.5 − bi wi

(27) Next, we only need to adjust si such that:

AI for PDEs convergence proofs

Literature Brief Description of Proof [69][68][140][143] Proofs of the strong fitting capabilities of NNs

- [144] Convergence proofs for elliptic second-order linear and parabolic PDEs using PINNs
- [145] Proofs of approximation properties of inverse problems using PINNs
- [146] Estimations of uncertainty in PINNs [34] Proofs that neural operators can approximate any continuous operator

[131] Proofs that the FNO in neural operators can approximate any continuous operator [37] Theoretical support for DeepONet: NNs can approximate any continuous operator

- [147] Proofs that DeepONet can approximate any continuous operator [130] PINO can approximate any continuous function or any continuous operator


||f(x) − siσ(wix + bi)||L∞ ≤ εi, where −0.5 − bi wi ≤ x ≤

0.5 − bi wi

(28)

where || · ||L∞ represents the maximum value of the function. Clearly, by controlling the affine transformations wi and bi, we can achieve a piecewise approximation, as shown in Fig. 8. Therefore, with a sufficient number of parameters {wi,bi,si}Ni=1, we can approximate f within any desired error ε. Mathematically, this can be expressed as follows: for any given error ε, there exists an N such that:

N

siσ(wix + bi)||L∞ ≤ ε = max{εi}Ni=1, where a ≤ x ≤ b (29)

||f(x) −

i=1

The above explanation is an informal but intuitive interpretation of the universal approximation theorem. This proof only applies to single-layer networks with a one-dimensional target function, not to higher dimensions. A formal proof can be found in Table 4 under "Proofs of the strong fitting capabilities of NNs." Empirically, using deeper networks can achieve the same function with fewer units and improve generalization error [142]. However, neural networks may require an impractically large number of units and may struggle with optimization problems. Most of the convergence proofs demonstrate that a neural network exists which can approximate a function or operator within ε, but they do not provide a method for determining its parameters and hyperparameters. Therefore, future research could focus on developing theoretical frameworks that offer guidance on neural network architecture design to achieve better convergence.

- 3.3. Weight Selection The optimization process of PINNs is essentially a multi-task learning problem, where balancing different


loss terms is crucial for algorithm efficiency and accuracy. From an optimization perspective, gradient-based algorithms tend to prioritize components with larger gradient magnitudes, potentially neglecting others [21]. The multi-task loss function can be expressed as:

L = λrLr + λiLi + λbLb + λdLd, (30)

where {λr,Lr}, {λi,Li}, {λb,Lb}, and {λd,Ld} represent the weights and loss functions for PDE residuals, initial conditions, boundary conditions, and data, respectively. Research on weight selection primarily focuses on how to adaptively determine these λ values. Table 5 summarizes representative studies on PINNs weight selection. We categorize them into the following four types.

Gradient-based methods. Wang et al. [9] proposed adaptively adjusting weights by comparing gradients. The weight for each loss component is computed as the ratio between the maximum gradient of the PDE residual loss and the mean gradient of that component. A moving average scheme, similar to RMSprop and Adam optimizers, is then applied to stabilize the weight updates during training.

Current research on PINNs weight selection

Reference Brief Description of Method [9] Selecting weights by comparing the gradients of different components of the loss function

- [148] Using NTK theory to select weights [93] Identifying the frequency tendencies of neural networks using NTK theory
- [149] Modifying the PINNs loss function into a saddle point problem
- [150] Modifying the loss function using maximum likelihood estimation


NTK-based methods. The Neural Tangent Kernel (NTK) theory [151] provides a framework for analyzing neural network training dynamics. Wang et al. [148] leveraged NTK to adjust loss weights based on the convergence rate of different components. The NTK matrix captures how changes at one training point affect predictions

- at others, with larger eigenvalues indicating faster convergence. By balancing the trace of NTK matrices corresponding to different loss terms, optimal weights can be determined. Subsequently, Wang et al. [93] used NTK to analyze the spectral bias of neural networks—the tendency to learn low frequencies first—and proposed input coordinate transformations to address this issue in multi-scale PDE problems.


Saddle point formulation. Liu et al. [149] transformed the loss function into a saddle point problem using constrained Lagrange multiplier methods:

L(θ,α) =

min

max

α

θ

j

λj(α)Lj(θ), (31)

where θ are network parameters, α are trainable parameters, and λj are obtained by applying softmax to α. This formulation generalizes the traditional weighted loss and allows the model to automatically learn optimal weights during training.

Maximum likelihood estimation. Xu et al. [150] adapted an uncertainty weighting method [152] for PINNs. By assuming that model predictions follow Gaussian distributions with task-specific uncertainties σi, the maximum likelihood estimation leads to the loss function:

k

L =

i=1

Li 2σi2

- 1

- 2


lnσi2 , (32)

+

where Li are the individual loss components. Tasks with higher uncertainty (larger σi2) automatically receive lower weights, enabling dynamic balancing during training without pre-specified hyperparameters. The uncer-

tainty parameters σi are learned jointly with the network parameters.

- 3.4. Distance Networks In addition to the constraints of the PDEs, there are also the constraints of boundary conditions. The


simplest implementation is through penalty factors to satisfy the constraints of boundary conditions:

Lossb = β

N

|NN(xi;θ) − u¯(xi)|2 (33)

i=1

where Lossb is the boundary loss, NN(xi;θ) is the neural network of the variable of interest, θ is the trainable parameter of the neural network, and u¯(xi) is the boundary condition at xi. β is the penalty factor.

However, the penalty factors introduce additional hyperparameters and can compromise the uniqueness of the solution. The penalty factor is a method of satisfying boundary conditions as a soft constraint, which is an approximate way of meeting boundary conditions. Therefore, using a penalty factor to approximately satisfy boundary conditions can theoretically lead to non-unique solutions in PINNs.

Therefore, strictly enforcing boundary conditions is a very important direction for PINNs. One method of strict enforcement is through the use of distance networks which is very similar to the idea of imposing boundary conditions in immersed and meshfree methods proposed in the early 1990s. Consider the following mechanical equation:

 

Domain Control Equation: L(u(x)) = f(x) ∀x ∈ Ω Displacement Boundary Condition: u(x) = h(x) ∀x ∈ Γu Force Boundary Condition: σ(x) · n(x) = t(x) ∀x ∈ Γt

, (34)



where L is the differential operator, u(x) is the displacement at x, f(x) is the body force, h(x) is the Dirichlet boundary (Γu) condition, t(x) is the Neumann boundary (Γt) condition, and σ(x) is the stress tensor. To solve this PDEs, we construct the displacement as follows:

u(x) = h(x) + D(x) ∗ ug(x;θ), (35)

where an approximation function fits h(x) as particular network, D(x) is the distance network, which outputs the shortest distance to the displacement boundary based on the coordinate x:

(x − y) · (x − y). (36)

D(x) = min

y∈Γu

This distance can be pre-calculated for a finite set of points using nearest neighbor algorithms and then approximated by a fitter D(x). Finally, ug(x;θ) is a neural network that learns based on the PDEs and the force boundary condition. The advantage of the distance network is that if the coordinate point lies on the displacement boundary Γu, where the displacement network D(x) equals zero, the output of the displacement field from Eq. (35) is exactly h(x). This means that during the training of PINNs in the strong form, there is no need to consider the displacement boundary condition.

Thus, distance networks are important for PINNs, both in the strong and energy forms. Research on distance networks primarily focuses on exploring admissible displacement field compositions to better train PINNs. The following is a review of distance networks: Lagaris et al. (1998) [20] initially proposed the concept of PINNs

- as well as the construction of admissible displacement fields that meet essential boundary conditions, but only provided a general mathematical form and specific construction methods in regular domains, i.e., converting the distance network into a multiplication by coordinates. Later, Lagaris et al. (2000) [153] proposed the construction of admissible displacement fields for irregular domains. McFall et al. (2009) [154, 155] discussed in detail the procedure for solving boundary value problems of arbitrary boundary shapes using neural networks. With PINNs receiving significant attention in recent years, this research area has been revitalized, and Berg et al.


(2018) [66] proposed the form of admissible displacement fields in Eq. (35), where the particular solution network h(x), distance network D(x), and general network ug(x;θ) are all approximated through fully connected neural networks, essentially similar to the method proposed by Lagaris et al. (2000) [153]. In DEM, Samaniego et al. [31] were the first to employ distance function in order to impose Dirichlet boundary conditions. Later, Rao et al. (2021) [100] extended the form of admissible displacement fields to linear elastic dynamics; Sheng et al. (2021) [125] proposed using RBF (Radial Basis Function) instead of the fully connected form of the distance network to solve the energy form of PINNs. It is worth mentioning that Sukumar et al. (2022) [156] discussed PINNs’ distance networks in great detail, even satisfying force boundary conditions in addition to displacement boundary conditions.

In summary, research on distance networks seems to have reached its developmental limit at the methodological level. In the future, the concept of distance networks is expected to be more widely integrated into various PINNs and operator learning algorithms, aiming to enhance the accuracy of these algorithms and reduce their reliance on hyperparameters.

- 3.5. Transfer Learning


Transfer learning is a crucial concept and application in machine learning, and also applied in PINNs. The main advantage of using transfer learning in PINNs is due to iterative algorithms, which can inherit previously

trained parameters, thus requiring fewer iterations for similar new tasks. The application approach of transfer learning in PINNs is generally the same, which involves directly inheriting the parameters from the previous task and then iterating in new tasks. There are two main methods of parameter iteration:

The first method is very simple; it involves completely inheriting the parameters and then re-iterating [24]. The second method involves freezing the first few layers of the neural network and only training the later layers to achieve the effect of transfer learning. For example, Goswami et al. (2020) [109] proposed using transfer learning to reduce the computational cost of phase-field modeling in fracture mechanics. In phase-field modeling, incremental step loading is required, so recalculating each step would be computationally expensive. By transferring the parameters learned by the PINNs energy method from the previous step to the next incremental step and training only the later layers, the iteration time for subsequent steps is reduced. Similarly, Chakraborty (2021) [36] proposed a transfer learning approach that incorporates approximate PDEs, and freezed the parameters of the initial layers, and uses high-precision experimental data to train the parameters of the later layers of the neural network that have been trained by PDEs. Xu et al. (2023) [150] suggested first training PINNs on a simple geometric model, and freezing the parameters of the shallow layers of the fully connected neural network while only training the deep layers in real tests with complex geometries. The rationale is that most geometric problems in structural mechanics are similar, and the basic features extracted by the shallow layers can be combined with the deep layers to form similar geometries, allowing the parameters to be directly transferred and reducing the number of iterations in PINNs. Recently, Wang et al. incorporated LoRA (Low-Rank Adaptation) [157] into both the strong and energy forms of PINNs across different boundary conditions, materials, and geometries [158]. In theory, LoRA can be regarded as a generalized form of the two aforementioned transfer learning strategies, since the rank in LoRA provides a flexible mechanism to control the extent of parameter adaptation during transfer.

In summary, these two methods in transfer learning are quite common in machine learning. This approach allows us to leverage models that have been pre-trained on large datasets and use transfer learning to address new tasks with smaller datasets or tasks that are slightly different from the original ones.

- 3.6. Gradient Approximation


The core of AI for PDEs lies in the computation of differential operators for PDEs. Therefore, the calculation of gradients is particularly crucial for solving PDEs using neural networks. There are generally three methods to compute gradients in this field: numerical difference approximation, symbolic computation, and automatic differentiation [159]. Each of these methods is reviewed below.

Numerical Difference Approximation. This method essentially approximates the limit form of derivatives, ignoring higher-order terms to achieve an approximate differential. The approach to approximate gradients using the numerical difference in AI for PDEs aligns with traditional numerical analysis and doesn’t fundamentally differ. Numerical differences include forward, backward, and central differences, which differ in terms of error order. The advantage of numerical difference lies in its simplicity and wide applicability; it does not require knowledge of the derivative’s analytic form. However, its drawbacks include significant truncation and rounding errors. Therefore, despite its broad applicability, its error characteristics must be carefully considered. Recently, some methods have used CNNs to approximate gradients, essentially using fixed convolution kernel weights to simulate finite difference [89].

Symbolic Computation. This method obtains analytical solutions of gradients through derivative operations (e.g., product rule, chain rule), and then inserts specific values to achieve the final gradients. Typically implemented recursively, this method offers high precision but can become inefficient with complex functions due to expression swelling [160], which is challenging to simplify.

Automatic Differentiation. Automatic differentiation is similar to symbolic computation but avoids the problem of expression swelling by breaking down complex functions into combinations of simple functions and using known derivatives of basic functions through the chain rule. During derivative computation, node values from forward operations are used in the chain rule formulas, thus eliminating the need for a complete analytical expression of gradients, thereby addressing the issue of expression swelling seen in symbolic computation. There

are two modes of implementation for automatic differentiation: forward mode and reverse mode. Forward mode computes function values and gradients simultaneously in one forward operation, which requires less memory and is suitable for problems with fewer parameters. However, reverse mode, which computes derivatives layer by layer from the output back inward, is more common in deep learning due to its suitability for problems with smaller output dimensions and larger parameter sets. Overall, automatic differentiation not only provides precise derivatives, similar to symbolic computation, but also solves the weaknesses of symbolic methods, such as expression swelling. Furthermore, the reverse mode is particularly well-suited to the small-output-dimensional context of deep learning. In AI for PDEs, it is common to compute the derivatives of a single scalar (such as the loss function) concerning a large number of weights, making the reverse mode very suitable for this scenario. Thus, the reverse mode is the predominant choice for derivative computation in the AI4PDEs domain.

In recent years, apart from automatic differentiation, another method of gradient approximation has emerged through statistical approaches [88, 74]. This method does not require backward gradient propagation for differentiation.

- 3.7. All Roads Lead to Rome

In theory, there are multiple ways to train an operator mapping from the input function space to the solution space, as illustrated in Fig. 9. For example, FNO can successfully learn a PDEs family operator purely from data [33]; VINO can also successfully learn the PDEs family operator solely from the governing PDEs [46]; PINO, by combining data and the physical equations, can also successfully learn the PDEs family operator [35]. This implies that there are multiple ways to achieve the training of a PDEs family operator, i.e., “All Roads Lead to Rome.”

The approach combining data and physical equations has more advantages compared to using data-only or physics-only methods. Training purely with data does not require additional effort to construct a PDE loss function, while the physics-based approach can compensate for insufficient training data. Therefore, theoretically, the data-physics hybrid approach is the optimal way to train a PDEs family operator. However, this approach may face a trade-off between the data loss and the PDE loss, which could necessitate additional hyperparameter tuning during training.

The idea of “All Roads Lead to Rome” is similar to the observation that there is not a single way to realize intelligence. For example, it has been found that modifying just one pixel in an image can completely fool a computer vision algorithm for classification tasks, whereas the human brain remains unaffected. This indicates that although both human brains and artificial intelligence can perform well on computer vision tasks, the underlying mechanisms by which intelligence is realized are different.

- 3.8. Benefits of Operator Learning as Good Initial Guesses


The predictions provided by operator learning can serve as initial guesses for iterative solvers, significantly reducing the required number of iterations compared to traditional numerical algorithms. We explain this by analyzing the convergence of iterative methods for linear systems.

Consider the iterative scheme

X(k) = BX(k−1) + f (37) Clearly, the exact solution X∗ satisfies

X∗ = BX∗ + f (38) Define the error as

e(k) = X(k) − X∗ (39) Substituting Eq. (37) and Eq. (38) into Eq. (39) yields

Recursively, we have

e(k) = (BX(k−1) + f) − (BX∗ + f)

= B(X(k−1) − X∗) = Be(k−1)

(40)

e(k) = Bke(0) (41)

Training

Operator Solution

Geometry Material Boundary

Approximate

Neural Network

|θ1|
|---|


|θ2|
|---|


|θ3|
|---|


|Loss<br><br>θ1 θ2 θ3<br><br>PDEs family θ|
|---|


Input

Data PDEs Data+PDEs

Training Source

- Fig. 9. Illustration of training PDEs family using neural networks: θ1 denotes the parameters of the neural network trained purely with data; θ2 denotes the parameters trained purely with PDEs; θ3 denotes the parameters obtained by combining data and PDEs for training.


Note that the quality of the initial guess is mathematically captured by e(0) = X(0) − X∗. That is, a better initial guess results in a smaller norm ||e(0)||. Using the subordinate matrix norm, we have

||Bke(0)|| ||e(0)||

||Bke(0)|| ||e(0)||

||Bk|| = max

(42)

≥

e(0)

||e(k)|| = ||Bke(0)|| ≤ ||Bk||||e(0)|| (43)

This clearly implies that, to achieve the same accuracy ||e(k)||, a better initial guess reduces the upper bound on the number of iterations k. This theoretically explains why operator learning can provide better initial guesses, thereby reducing the iteration count in the fine-tuning phase, especially when traditional iterative algorithms cannot provide good initial values.

The benefit diminishes as the tolerance (tol) becomes smaller. Rewriting Eq. (43), we obtain

||e(k)|| ||e(0)||

≤ ||Bk|| (44)

Let ε = ||Bk||, then Eq. (44) becomes

||e(k)|| ||e(0)||

≤ ε (45) Taking logarithms:

||Bk||1/k = ε1/k ln||Bk||1/k = lnε1/k

k = −lnε −ln||Bk||1/k

(46)

The asymptotic convergence rate is defined as R(B) = lim

−ln||Bk||1/k (47)

k→+∞

which depends only on the iteration matrix B, not on k or the initial guess. For large k, substituting Eq. (47) into Eq. (46) gives

k = −lnε R(B)

(48) The difference in iteration tolerance (tol) essentially corresponds to a difference in ||e(k)||. Let tol = 10−m,

and approximate ||e(k)|| ≈ tol. Then Eq. (45) becomes

10−m ||e(0)||

≤ ε

10−m ||e(0)||

≤ lnε

ln

−mln10 − ln||e(0)|| ≤ lnε (49) Substituting Eq. (49) into Eq. (48) yields

k = −lnε

R(B) ≤

mln10 + ln||e(0)|| R(B)

mln10 R(B)

=

ln||e(0)|| R(B)

+

(50)

From Eq. (50), we see that mln10/R(B) quantifies the impact of the iteration tolerance (tol) on the number of iterations, while ln||e(0)||/R(B) captures the influence of the initial guess. Clearly, the smaller the tolerance (larger m), the smaller the effect of the initial guess on the iteration count.

###### 4. AI for PDEs in the application of forward problems of computational mechanics

In this chapter, we review the applications of AI for PDEs in computational mechanics. Specifically, we focus on their application in addressing forward problems across various domains such as solid mechanics, fluid dynamics, and biomechanics.

- 4.1. Solid mechanics


We focus on discussing the latest research developments in the field of AI for PDEs within solid mechanics. Therefore, we detail various examples of applications of AI for PDEs in solid mechanics. For the strong form of PINNs, it can solve almost any forward problem in solid mechanics, but for the energy form, it is only applicable to solid mechanics problems that adhere to energy principles, such as linear elastic statics, hyperelastic problems, and phase field method simulations of fractures.

- 4.1.1. Linear elasticity mechanics The domain PDEs in linear elasticity mechanics are composed of three sets of equations: the equilibrium


equations, constitutive equations, and kinematic equations:

 

Equilibrium equations: σij,j + fi = ρu¨i ∀(x,t) ∈ Ω [0,T] Constitutive equations: σij = 2Gεij + λεkkδij ∀(x,t) ∈ Ω [0,T] Kinematic equations: εij = 12(ui,j + uj,i) ∀(x,t) ∈ Ω [0,T]

, (51)



where λ and G are the Lame parameters. u, ϵ, and σ are the displacement, strain, and stress respectively. Boundary and initial conditions include initial displacement conditions, initial velocity conditions, displacement boundary conditions, and force boundary conditions:

 

Initial displacement condition: u(x,0) = u0(x) ∀x ∈ Ω Initial velocity condition: u˙ (x,0) = v0(x) ∀x ∈ Ω Displacement boundary condition: u(x,t) = u¯(x,t) ∀(x,t) ∈ Γu [0,T] Force boundary condition: t(x,t) = ¯t(x,t) ∀(x,t) ∈ Γt [0,T]

. (52)



The above set of equations represents all the control equations and boundary conditions in linear elasticity mechanics. If we consider the structural characteristics of the problem, these equations can be simplified, such as in plate and shell mechanics. However, the essence of the core solution remains solving PDEs in Eq. (51) with boundary conditions in Eq. (52). In the strong form of PINNs, Eq. (51) and Eq. (52) are directly coupled through different hyperparameters into one loss function for solving. In the energy form of PINNs, these equations are transformed into an energy functional, such as the principle of minimum potential energy or minimum complementary energy. However, only static problems can be transformed. Although dynamic problems also involve the Hamiltonian functional, the functional of dynamic problems is stationary problems. The requirement of minimum potential and complementary energies is an extremum problem. Due to the highly non-convex nature of neural networks, solving the Hamiltonian functional in dynamics faces immense optimization difficulties due to infinite saddle points, making it extremely challenging to obtain stationary points. Additionally, a significant difficulty with the Hamiltonian functional’s admissible displacement field is that it requires the displacement field to satisfy the final moment displacement solution (a necessity in Hamiltonian theory). Unfortunately, we do not know what the final moment displacement field is. Thus, the high degree of non-convexity and the unknown nature of the final moment displacement field pose significant challenges for the energy method of PINNs in dynamic problems in linear elasticity. The above analysis is just an application of PINNs in linear elasticity problems, while AI for PDEs encompasses not only PINNs but also operator learning and PINO. Therefore, we will next provide an overview of AI for PDEs in the forward problems of linear elasticity in solid mechanics.

Rao et al. (2021) [100] used the strong form of PINNs algorithm and the construction of admissible displacement fields to solve linear elasticity dynamics problems, as shown in Fig. 10a. Guo et al. (2021) [161] used the strong form of PINNs algorithm for the first time in Kirchhoff plates. Subsequently, Zhuang et al.

(2021) [106] applied the energy form of PINNs using the principle of minimum potential energy in Kirchhoff plates. Li et al. (2021) [107] compared the strong and energy forms of PINNs in Kirchhoff plates, as illustrated in Fig. 10b. Bai et al. [162] studied modified loss functions in strong form, solving elastic problems with geometric nonlinearity and constitutive linearity. Later, Sun et al. (2023) [83] combined PINNs with boundary element methods. Mathematically, the strong form of PDEs can be converted into the weak form through Gauss’s divergence theorem. If the differential equation involves a linear self-adjoint operator, the weak form can be further transformed into an energy form. If the weak form is subjected to Gauss’s divergence theorem again until the highest derivatives in the test functions are achieved, thereby reducing the differential equation to its lowest order, it then transforms into the inverse form. Boundary elements leverage the inverse form to formulate boundary integral equations. Thus, the strong form, energy form (or weak form), and inverse form are all different representations of the same PDEs. However, due to limitations in the fundamental solutions of Green’s functions in boundary elements, currently, only problems in linear elasticity can be solved, as shown in

- Fig. 10c. The above literature review discusses using PINNs to replace traditional numerical methods, such as the


finite element method, for solving linear elasticity problems. Additionally, operator learning combined with finite element methods has also been applied to linear elasticity problems, especially for multiscale problem. For instance, Wang et al. (2026) [17] proposed using the Fourier Neural Operator (FNO) to replace the calculation process of elastic tensors in mechanical homogenization. In the original problem, traditional methods required finite element calculations of displacement fields under six loading conditions for different geometries, followed by numerical homogenization formulas to obtain the fourth-order equivalent elastic tensor. Since the boundary conditions in the numerical homogenization process are fixed and only the geometry changes, a large amount of data can be calculated using finite elements for different geometries, then operator learning can be used to learn the mapping from geometry to displacement fields, and finally, it can be input into traditional numerical homogenization programs, significantly improving computational efficiency (about 1000 times faster compared to traditional finite element methods). The solution predicted by the FNO is then used as the initial guess for the finite element iterative solver. Since this initial guess is much closer to the reference solution, the number of required numerical iterations is greatly reduced compared to traditional finite element methods. This strategy thus achieves both the computational efficiency of operator learning and the accuracy of the classical finite element method.

- 4.1.2. Elastoplastic mechanics Elastoplastic theories encompass various models that describe the relationship between strain increments


and stress during the plastic deformation phase. Abueidda et al. (2021) [25] utilized PINNs with J2 flow theory, kinematic hardening, and isotropic hardening models to address elastoplastic problems. Here, we illustrate how PINNs solve elastoplastic issues, starting by specifying parameters for elastoplastic problems: the Lame constants λ and G, yield stress σs, parameters K describing isotropic hardening of the yield surface, and parameter H for back stress evolution. Using traditional PINNs, sufficient points are sampled on the domain displacement boundaries, and force boundaries. We initialize variables that will evolve iteratively. The variables to be initialized include initial plastic strain epo, initial back stress qo, and initial internal variable α0 for isotropic hardening. According to J2 flow theory, the yield condition with the kinematic hardening and the isotropic hardening models is:

F(σ,q,α) = √η : η −

- 2

- 3


(σy + Kα), (53)

where η = s−q, with s representing the deviatoric stress tensor reduced by the hydrostatic stress, and q is the back stress. Given the path-dependent nature of plastic mechanics, we typically employ incremental loading for numerical simulation. Setting boundary conditions incrementally, we consider a pseudo-time t = 1 scenario, using the PINNs network (inputting coordinates, outputting displacement fields) to output displacement fields

- at points within the domain and on displacement and force boundaries. Using automatic differentiation, we derive the gradient of displacement. From the relationship between strain and displacement gradients, we compute the strain at t = 1, denoted ε1, and from this strain, compute the deviatoric strain e1.


According to the predefined variables, including initial plastic strain epo, initial back stress qo, and initial

- (a)
- (b) (c)


- (1) Initial/boundary condition DNN (Parameters )

Automatic Differentiation Governing equations

Physical Laws

Physics Loss Function:

- (2) Distance function DNN (Parameters )

- (3) General DNN (Parameters )


Pretrained

Pretrained

![image 6](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile6.png)

![image 7](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile7.png)

![image 8](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile8.png)

- Fig. 10. Applications of PINNs in elastic mechanics. (a) Strong form: linear elastic dynamics [100] , (b) Strong and energy form: Kirchhoff plates [107], (c) Inverse form: elasticity problems [83]


isotropic hardening internal variable α0, we calculate the trial deviatoric stress strial1 , trial relative stress ηtrial1 , and the trial state of the yield condition F1trial:

strial1 = 2G(e1 − ep0) ηtrial1 = strial1 − qo

. (54)

- 2

- 3


F1trial = ηtrial1 : ηtrial1 −

(σy + Kα0)

We determine whether the material enters the plastic phase by checking if F1trial is less than or equal to zero. If F1trial is less than or equal to zero, the material is considered to be in the elastic phase, and stress is calculated directly using strial1 :

σ1 = λtrace(ε1)I + strial1 . (55) Using this stress and displacement field, we compute the loss function for t = 1 using the balance equations, displacement boundary conditions, and force boundary conditions, and optimize the parameters of the PINNs network, verifying in each optimization cycle whether the material remains elastic. If F1trial exceeds zero, we must adjust the previous steps, notably changing how stress is computed. Using ηtrial1 and F1trial, we compute the flow direction n1, plastic flow increment γ1, and updated isotropic hardening internal variable α1 at t = 1:

ηtrial1

n1 =

ηtrial1 : ηtrial1 γ1 = F1trial

. (56)

2(G + H3 + K3 ) α1 = α0 +

- 2

- 3


γ1

The back stress q, plastic strain ep, and stress σ are updated accordingly:

- 2

- 3


q1 = q0 +

γ1Hn1 ep1 = ep0 + γ1n1 σ1 = λtrace(ε1)I + strial1 − 2G γ1n1

. (57)

The loss function is optimized in the same way as during the elastic phase, using the revised stress and displacement fields along with corresponding equations and boundary conditions. This process continues iteratively through incremental loading steps until the loss function converges, marking the end of the elastoplastic simulation in the strong form of PINNs. The simulation results are compared with FEM solutions, focusing on displacement fields as illustrated in Fig. 11a.

The steps involved in solving elastoplastic problems using the strong form of PINNs are similar to traditional computational mechanics, except that the approximation function has shifted from the shape functions in FEM to neural networks. Due to the abundance of plasticity theories, aside from the J2 flow rule, other theories can also be simulated using PINNs, thus facilitating the evaluation of PINNs models in handling plastomechanical issues. Furthermore, He et al. (2023) [112] proposed using the energy method with the plastic variational formulation for calculating elastoplastic problems, as shown in the process diagram in Fig. 11a. The plastic variational formulation is based on the theory proposed by Simo et al. (2006) [163]. Since elastoplastic problems are related to the historical loading path, both the strong form and energy form of PINNs iteratively address each loading step.

Additionally, data-driven simulations of elastoplastic issues have been conducted, with Li et al. (2023) [121] using Geo-FNO (an enhanced version of FNO capable of operator learning for any geometry) to simulate forming and stamping processes. The algorithmic framework and simulation results are depicted in Fig. 11b.

###### (a) (b)

![image 9](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile9.png)

![image 10](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile10.png)

![image 11](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile11.png)

![image 12](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile12.png)

- Fig. 11. Applications of PINNs and operator learning in elastoplastic mechanics: (a) PINNs in strong form [25] and energy form [112], (b) Operator learning with Geo-FNO [121].


The return mapping in Eq. (57) is a numerical algorithm for the elastoplastic KKT conditions. Mathematically, the KKT can be easily transformed into an optimization problem using e.g. Fischer-Burmeister replacement functions [164], which allows for much larger load steps and can lead to computational savings. Therefore, in the future, a PINNs algorithm based on Fischer-Burmeister replacement functions could be developed to solve elastoplastic problems.

- 4.1.3. Hyperelastic mechanics Hyperelastic problems not only involve geometrical nonlinearity but also material nonlinearity, and they


can be computed using the minimum potential energy principle in the energy form of PINNs. Traditional hyperelastic problems are path-independent, making them a simpler type of nonlinear mechanics problem. Therefore, many studies in mechanics using PINNs often choose hyperelastic problems as examples. There are two main considerations in the PINNs simulation of hyperelastic problems: the first is the selection of the potential function according to the constitutive law of hyperelasticity material, and the second is that the kinematic equations must consider the nonlinear terms of large deformations. To illustrate, let us consider the potential function of the Neo-Hookean constitutive model:

Ψ =

- 1

- 2


λ(lnJ)2 − GlnJ +

- 1

- 2


G(trace(C) − 3) , (58)

where J is the determinant of the deformation gradient F, and C is the right Cauchy-Green deformation tensor (C = FTF). We first establish a neural network mapping from material coordinates X to spatial coordinates x. We scatter points within the domain and then use automatic differentiation to calculate the deformation gradient F = ∂x/∂X, which is substituted into Eq. (58) to determine the density of the hyperelastic strain energy. Once F is known, hyperelastic strain energy can be obtained through some simple algebraic operations. Since the potential energy principle must consider the work done by external forces and the displacement field must satisfy displacement boundary conditions in advance, we consider displacement boundary conditions when hypothesizing admissible displacement fields, employing the construction method of Eq. (35). However, if the structure’s shape is simple, the distance function can be directly constructed analytically (often by multiplying by coordinates, as suggested by [110].) For the work of external forces, the construction is entirely the same as in linear elasticity problems. Finally, we construct the overall loss function:

L = ˆ

Ω

(Ψ − f · u)dΩ − ˆ

Γt

¯t · udΓ. (59)

###### (a) (b)

|Material 1|
|---|


Neural network (NN) Energy informed NN

Boundary condition

![image 13](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile13.png)

![image 14](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile14.png)

![image 15](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile15.png)

![image 16](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile16.png)

![image 17](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile17.png)

![image 18](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile18.png)

![image 19](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile19.png)

![image 20](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile20.png)

Natural Boundary Interface Essential Boundary

![image 21](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile21.png)

![image 22](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile22.png)

![image 23](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile23.png)

External energy NN

![image 24](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile24.png)

![image 25](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile25.png)

![image 26](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile26.png)

![image 27](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile27.png)

|Material 2|
|---|


Internal energy NN

![image 28](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile28.png)

![image 29](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile29.png)

![image 30](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile30.png)

Argmin

Potential energy loss

![image 31](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile31.png)

Strong

- Domain points in Material 1
- Domain points in Material 2 Natural boundary points Interface points


Energy

PDE

Neural Network

L(⋅)

Variational

a

a

###### a

![image 32](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile32.png)

P(⋅)

y1

x1

a

a

a

Loss

yn

xm

Lossi

a

a

a

λi

MSE

Input Layer Hidden Layer Output Layer

No Loss<tol?

Done

- Fig. 12. Applications of PINNs in energy form for hyperelastic mechanics: (a) PINNs in energy form [110, 126] (b) PINNs in energy form with subdomains [29].


By optimizing the above loss function, we can obtain the neural network parameters for the mapping from material coordinates X to spatial coordinates x, thus determining the corresponding mapping relationship. Once the mapping from material coordinates X to spatial coordinates x is known, all mechanical quantities become clear, including the displacement field, the first Piola-Kirchhoff stress P, and the second Piola-Kirchhoff stress S:

u = x − X P =

∂Ψ ∂F

. (60)

= GFT + [λlnJ − G]F−1 S = P · F−T

It is worth emphasizing that numerical integration in the energy form of PINNs is crucial, as it directly affects the calculation of functional. Nguyen-Thanh et al. (2020) [110] were the first to apply the PINNs energy principle to hyperelastic problems and introduced traditional numerical integration schemes into the PINNs energy form (DEM), as shown in Fig. 12a. Subsequently, Fuhg et al. (2022) [126] extended the PINNs energy form by dividing the loss function into two parts: one based on the minimum potential energy principle and the other constructed through the equilibrium equation, as shown in Fig. 12a below. Wang et al. (2022) [29] extended the PINNs energy form algorithm to a subdomain form to solve hyperelastic problems, as shown in

- Fig. 12b. Bai et al. (2024) [111] use Radial Basis Function (RBF) networks to solve hyperelasticity torsional buckling cases in energy form. Although Abueidda et al. (2022) [165] were not the first to use the PINNs energy method to solve hyperelastic problems, they were the first to propose using the PINNs energy method to solve viscoelastic problems. Of course, we can also use the PINNs strong form to simulate hyperelastic problems, but the order of derivatives will increase, thereby reducing computational efficiency and accuracy, such as Abueidda et al. (2021) [25] using the PINNs strong form, directly considering the balance equation and boundary conditions to construct the loss function. It can be seen that the core difference between the PINNs strong form and the energy form is in the construction of the loss function.


- 4.1.4. Fracture Mechanics The Deep Energy Method (DEM), also referred to as the energy-based PINNs approach, is particularly


attractive for fracture mechanics, where the governing equations naturally derive from an energy functional

[109]. DEM has been applied to both discrete fracture models and continuous damage models, with several representative studies. For discrete fracture models, Zhao et al. employed DEM to simulate crack propagation [166], although their approach required additional collocation points along the crack path. Chen et al. [167] applied strong-form PINNs combined with asymptotic fracture solutions to simulate fatigue crack growth but did not exploit the energy formulation.

In the context of continuous damage models, Goswami et al. first introduced DEM for phase-field fracture, applying PINNs to both second-order [109] and fourth-order phase-field models [108]. Nevertheless, modeling shear failure (mode-II) remained challenging. Later, Goswami et al. integrated DEM with DeepONet [47, 168]. Zheng [169] proposed a FEM-inspired approach, where nodal values were predicted by neural networks and interpolated via shape functions to construct displacement and phase fields. However, this approach still required mesh refinement along the crack path, similar to FEM. Building on this idea, Manav et al. [170] conducted a more systematic study, applying DEM to crack nucleation, propagation, kinking, branching, and coalescence. Compared with traditional FEM and IGA, a key advantage of DEM is the ability to use larger load increments [109], thus enhancing the efficiency of crack propagation simulations.

Recently, Wang et al. [123] proposed the Extended Deep Energy Method (XDEM) shown in Fig. 13, a unified deep learning framework that incorporates both displacement discontinuities and crack-tip asymptotics in the discrete setting, while flexibly coupling displacement and phase fields in the continuous setting. XDEM leverages Heaviside functions and crack-tip asymptotic enrichment from XFEM, significantly enhancing the robustness and accuracy of DEM in solving fracture mechanics problems.

Continuous damage model

Penalization

LoRA:

Π =Ue +Uc −Wext Low-Rank Adaptation

History Field

Irreversibility of the phase  eld

Transfer Learning

##### φ

###### Uc

| | |
|---|---|
| | |
| | |


To Next Step

Phase Field

Crack Energy

Done

MLP

Monte Carlo

KAN

Yes

Gauss Integration

RBF

......

......

Potential Energy

Minimum Reached?

Numerical Integration

Neural Network

###### U U

Ue

No

Dirichlet Boundary

Dis Field

Strain Energy

Admissible Dis Field

Discrete crack model

Π =Ue −Wext

Crack Function

Wext

Neumann Boundary External Work

Extended Function

Extended Deep Energy Method

Update Trainable Parameters of Neural Network

- Fig. 13. Applications of PINNs in fracture mechanics, which consist of discrete and continuous models. The continuous formulation is indicated by dashed lines [123].


###### Below, we provide a introduction to XDEM, which currently represents one of the most promising directions

for solving fracture mechanics problems using PINNs. XDEM can be formulated in both discrete and continuous forms.

The discrete crack model of XDEM is governed by the PDEs of linear elasticity: 

σij,j + fi = 0, x ∈ Ω, σij = Cijklεkl, x ∈ Ω, εij = 21(ui,j + uj,i), x ∈ Ω \ Γc, u+i ̸≡ u−i , x ∈ Γc, σijnj = t¯i, x ∈ Γt, ui = u¯i, x ∈ Γu.



(61)



Here, σ, C, ε, and u denote the stress tensor, stiffness tensor, strain tensor, and displacement vector, respectively. Ω is the domain, while Γu, Γt, and Γc denote Dirichlet boundaries, Neumann boundaries, and the crack surface. The body force, prescribed traction, and prescribed displacement are denoted by f, ¯t, and u¯, respectively. The symbol ̸≡ indicates potential displacement discontinuities across Γc. In this study, we consider only Dirichlet and Neumann boundary conditions, with traction-free conditions on the crack surface.

Using the principle of minimum potential energy, the system in Eq. (61) can be reformulated as:

u = arg min

Π,

u

Π = Ue − Wext, Ue = ˆ

1 2

ε : C : εdV,

Ω

Wext = ˆ

f · udV + ˆ

¯t · udS,

Γt

Ω

s.t. ui = u¯i, x ∈ Γu; u+i ̸≡ u−i , x ∈ Γc.

(62)

It is straightforward to show that δΠ = 0 is equivalent to Eq. (61).

By solving Eq. (62), the displacement field can be obtained, from which the stress field follows via the constitutive and geometric relations. To further simulate crack propagation, a fracture criterion must be specified. Common criteria include the maximum circumferential stress criterion [171], the maximum energy release rate criterion [172], and the minimum strain energy density criterion [173]. XDEM adopt the maximum circumferential stress criterion, whereby the crack propagates in the direction of the maximum hoop tensile stress.

The discrete XDEM optimization problem is:

un+1 = arg min

Π,

u

Π = Ue − Wext, Ue = ˆ

- 1

- 2


###### ε(x;θu) : C : ε(x;θu)dV,

Ω

Wext = ˆ

f · u(x;θu)dV + ˆ

¯t · u(x;θu)dS, s.t. ui(x;θu) = u¯i(x,tn+1), x ∈ Γu; u+i ̸≡ u−i , x ∈ Γc.

Γt

Ω

(63)

Here, θu represents the trainable parameters of the displacement neural network NN(x;θu). XDEM incorporates a crack function to represent the discontinuous field across cracks and an extended function to embed the asymptotic solution near the crack tip into the displacement neural network, detailed in [123]

For continuous damage, XDEM employs the classical phase-field fracture model [174], based on the varia-

tional principle of Francfort and Marigo [175]. The energy functional is extended to include fracture energy:

u,ϕ = arg min

Π,

u,ϕ

Π = Ue + Uc − Wext, Ue(u,ϕ) = ˆ

w(ϕ)Ψ+(ε) + Ψ−(ε)dV,

Ω

(64)

Gc cw

g(ϕ) l0

ˆ

+ l0 (∇ϕ) · (∇ϕ)dV,

Uc(u,ϕ) =

Ω

Wext = ˆ

f · udV + ˆ

¯t · udS, s.t. ui = u¯i, x ∈ Γu; ϕn+1 ≥ ϕn.

Γt

Ω

- where w(ϕ) is the degradation function that represents the reduction of material stiffness. It must satisfy the following conditions: w(0) = 1, w(1) = 0, w′(1) = 0, and w′(ϕ) < 0. A common choice is w(ϕ) = (1 − ϕ)2. Ψ+(ε) and Ψ−(ε) denote the tensile and compressive contributions of the strain energy, respectively. Typical decompositions include the formulations of Miehe [176] and Amor [177]:


3

Miehe: Ψ+(ε) = 12λ⟨εii⟩2+ + G

⟨λi⟩2+,

i=1

3

(65)

Ψ−(ε) = 12λ⟨εii⟩2− + G

⟨λi⟩2−,

i=1

Amor: Ψ+(ε) = 21K⟨εii⟩2+ + Gε′ijε′ij, Ψ−(ε) = 12K⟨εii⟩2−,

where λ and G are the Lamé constants, K = λ + 2G/3 is the bulk modulus, λi are the eigenvalues of the strain tensor ε, and ε′ij = εij − εkkδij/3 is the deviatoric strain tensor. The positive and negative parts of a scalar are defined as ⟨x⟩+ = (x + |x|)/2 and ⟨x⟩− = (x − |x|)/2. In the manuscript, we use Miehe as the form of the energy decomposition.

´ 1

In Eq. (64), Gc is the critical energy release rate, and cw = 4

0 g(ϕ)dϕ is a normalization constant. The function g(ϕ) denotes the local dissipation function, commonly chosen as in the AT1 (g = ϕ, cw = 8/3) or AT2 (g = ϕ2, cw = 2) models.

In practical phase-field simulations, the choices of w(ϕ) and g(ϕ), the type of energy decomposition, and the length-scale parameter l0 must be specified in advance. By minimizing Π in Eq. (64), both the displacement field u and the phase-field variable ϕ can be obtained. Compared with discrete crack models, the phasefield model has the advantage of allowing spontaneous crack nucleation without prescribing a fracture criterion. However, its major drawback is the significantly higher computational cost. It is also important to note that the irreversibility condition ϕn+1 ≥ ϕn is typically enforced by either a history field approach [176] or a penalization technique [178]

For the continuous phase-field fracture model, the XDEM optimization problem is given by: {un+1,ϕn+1} = arg min

Π(u(x;θu),ϕ(x;θϕ)) Π = Ue + Uc − Wext

θu,θϕ

Ue(u,ϕ) = ˆ

[w(ϕ(x;θϕ))Ψ+(u(x;θu)) + Ψ−(u(x;θu))]dV

Ω

, (66)

Gc cw

g(ϕ(x;θϕ)) l0

ˆ

+ l0(∇ϕ(x;θϕ)) · (∇ϕ(x;θϕ))dV

Uc(u,ϕ) =

Ω

Wext = ˆ

f · u(x;θu)dV + ˆ

¯t · u(x;θu)dS. s.t. ui(x;θu) = u¯i(x,tn+1),x ∈ Γu;ϕn+1 ≥ ϕn

Γt

Ω

where θu and θϕ denote the trainable parameters of the displacement neural network NN(x;θu) and the phase-field neural network NN(x;θϕ), respectively. Unlike discrete models, the phase-field formulation does not require a predefined crack propagation criterion, as cracks can nucleate and evolve naturally. However, the irreversibility condition ϕn+1 ≥ ϕn must be satisfied, ensuring that cracks cannot heal once formed. The continuous phase-field fracture model of XDEM uses KAN for displacement-field approximation and RBF for phase-field approximation, as detailed in [123].

XDEM has been systematically validated on classical fracture mechanics benchmarks, including stress intensity factor predictions and crack path simulations [123].

- 4.1.5. Summary Overall, for addressing forward problems, current PINNs, in terms of accuracy and efficiency, still lag behind


traditional numerical methods [24]. Recent studies have shown that operator learning can significantly enhance the computational efficiency for forward problems. Although traditional operator learning is purely datadriven, current theoretical explanations suggest that after extensive data training, operator learning can learn the mappings of PDEs families. Additionally, the integration of operator learning with physical equations holds promising academic and industrial prospects. This involves using existing data to propose a good initial solution, which is then fine-tuned using physical equations. This approach theoretically offers significant benefits in computational efficiency and accuracy, especially for complex nonlinear problems. In mathematics, some nonlinear problems can be transformed into iterations of nonlinear equation systems, where a good initial solution is vital for reducing iteration time. For instance, in hyperelasticity problems, operator learning can provide a good initial solution, followed by iterations based on the nonlinear equation system. Here, using finite element methods instead of PINNs to solve physical equations could enhance accuracy and efficiency, suggesting a combination of finite element methods and operator learning to greatly improve the computational efficiency of nonlinear problems.

This section has introduced the applications of AI for PDEs in addressing forward problems in solid mechanics. Next, we will discuss the applications of AI for PDEs in solving forward problems in fluid mechanics.

- 4.2. Fluid mechanics In this section, we will focus on the latest research on fluid mechanics with AI for PDEs. The algorithms in


Section 2 are very popular in fluid mechanics.

- 4.2.1. Hydrodynamics Hydrodynamics, a sub-discipline of fluid dynamics, focuses on the motion of liquids and the forces acting


upon them. In hydrodynamics, the most popular governing equations, the Navier-Stokes (NS) equations, can be written as

D (ρv) Dt

+ ρv (∇ · v) = ∇ · σ + ρf (67)

∂ρ ∂t

+ ∇ · (ρv) = 0, (68)

where ρ is the density of the fluid, v is the velocity vector in this section, p is the pressure, σ is the stress tensor and f is the body force. Eq. (67) describes the conservation of momentum, while Eq. (68) ensures the conservation of mass. For incompressible flow, the material derivative of density is zero, i.e. Dρ/Dt = ∂ρ/∂t + ρ,ivi = 0. Therefore, Eq. (68) can be simplified as

∇ · v = 0. (69)

To impose the incompressibility as a hard constraint in 2D problems, the stream function φ can be used as the direct output of neural networks. In this manner, the velocity can be computed by

- u =

∂φ ∂y

- v = −


. (70)

∂φ ∂x

It is easy to verify that Eq. (70) automatically satisfies the hard constraint of incompressibility in Eq. (69). For the sake of simplicity, herein we only introduce the Newtonian fluid model

′

ij (71) S

σij = (−p + λSkk)δij + 2µS

1 3

′

Skkδij (72) Sij =

ij = Sij −

- 1

- 2


(vi,j + vj,i) (73)

where µ and λ are the viscosity coefficients. According to Eq. (69), we substitute Eq. (72) into Eq. (71), and obtain:

σij = −pδij + µ(vi,j + vj,i). (74) According to Eq. (69), substituting Eq. (74) into Eq. (67) yields the following equation:

D(ρv) Dt

= −∇p + µ∇2v + ρf. (75)

Guiding by Eq. (75), various formats of PDEs for fluid mechanics have been proposed, such as the VP format based on velocity and pressure, and the VV format based on vorticity and velocity. Rao et al. [104] proposed PINNs framework for incompressible laminar flows based VP formulation, as shown in Fig. 14a. In the framework, only the conservation of momentum is explicitly embedded into the loss function, while the incompressibility is naturally satisfied by using Eq. (70). Jin et al.[179] further provided a PINNs framework (NSFnets) informed by vorticity-velocity (VV) formulation for incompressible hydrodynamics and compared VV with VP formulation, as shown in Fig. 14b. By taking the curl of Eq. (75), VV formulation is obtained:

D(v) Dt

p ρ

v ρ

+ µ∇2

∇

= ∇ (−∇

+ f)

1 ρ

ϵijkv˙j,i + ϵijk(vsvj,s),i = −

ϵijkp,ji + νϵijkvj,ssi + ϵijkfj,i ϵijkv˙j,i + ϵijkvs,ivj,s + ϵijkvsvj,si = νϵijkvj,ssi

, (76)

D(w) Dt − w · (∇u) = ν∇2w

where ν = µ/ρ is the dynamic viscosity and w = ∇ v denotes the vorticity. Note that the fluid is still incompressible, so in our derivation, we actually use ∂ρ/∂t = 0.

Although the VP and VV formats mathematically address the same physical problem, they are not computationally equivalent. For instance, the VV format is more effective at high Reynolds numbers, while the VP format can directly describe velocity and pressure. The VV format involves first solving for vorticity and then using the resulting vorticity to update the velocity field through the Poisson equation.

Moreover, the adaptive weight technique proposed in [9] can be adopted. It is reported that PINNs can achieve high accuracy at Re = 100. Zhang et al. [180] introduced a PINN framework, the so-called dynamics random vorticity network (DRVN), via the random vortex method [181]. The proposed DRVN is capable of effectively addressing fractural and sharp singularity issues, which the NSFnet [179] struggles with. Rui et al. [182] implemented the Reynolds-averaged Navier-Stokes (RANS) equations. The Reynolds decomposition, which divides flow quantities into time-averaged and fluctuating terms, is applied to the NS equations. Thus, the governing equations in RANS can be written as

ρv¯ · (∇v¯) = ρf − ∇p¯+ µ∇ · (∇v¯ + v¯∇) − ρ∇ · v′v′, (77)

where v and v′ are the mean (time-averaged) velocity and the fluctuating velocity, respectively. Reynolds decomposition refers that we can decompose velocity into the time average v and the fluctuating velocity v

′

, i.e. v(x,t) = v¯(x) + v

′

(x,t), note that although v′ = 0, but v′v′ ̸= 0. Thus, −ρv′v′ is the Reynolds stress due

(a) (b)

![image 33](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile33.png)

![image 34](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile34.png)

![image 35](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile35.png)

![image 36](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile36.png)

- Fig. 14. Different Formats of PINNs for Solving Fluid Dynamics Equations: (a) VP format PINNs for incompressible laminar flow [104]. (b) VV format PINNs for incompressible Navier-Stokes equations[179].


to the fluctuating velocity field. This nonlinear Reynolds stress term requires additional modeling to close the RANS equation and has led to the creation of many different turbulence models.

Various neural network structures are adopted in the framework of PINN. Wang et al. [183] combined the PINNs with long-short term memory (LSTM) [184] model for hydrodynamics. The LSTM has the advantage of extracting temporal features in raw data. Thus, the fusion of PINNs and LSTM further enhanced the extrapolation ability for hydrodynamics modeling. Han et al. [185] used criss-cross convolutional neural network [186] to learn the solution of parametric flow problems with spatial heterogeneity, while Cheng and Zhang [187] applied the Resnet [132] for flow modeling.

In the context of neural operators, hydrodynamics problems have become the most prevailing benchmarks. Initially fully data-driven, Li et al. [129] tested the performances of GNO through the 2D Darcy flow problems. Subsequently, operator learning is combined with physical equations. Zhu et al. [117] utilized the DeepONet framework, initially training it with data and subsequently fine-tuning it for specific problems based on physical equations. This process involved constructing PDEs loss functions using the automatic differentiation (AD) algorithm. The results of Zhu et al. [117] are shown in Fig. 15a. On the other hand, Li et al. [35] employed the Fourier Neural Operator (FNO) framework, initially training it with data and then constructing the PDEs’ loss using finite differences for specific tasks. The results of Li et al. [35] are shown in Fig. 15b. In specific fluid dynamics applications, Rosofsky et al. [188] leveraged the PINO to simulate the magnetohydrodynamics. Li and Shatarah [189] proposed a composite neural network, which comprised a series of DeepONet and a PINN. The proposed framework could not only accurately predict the velocity field and the particulate matter (PM) concentration contours by limited ground truth data, but also seamlessly coped with scenarios with different geometries.

- 4.2.2. Aerodynamics and shock waves The NS equations are also applicable to describe the aerodynamics problems. Unlike hydrodynamics, fluids


in aerodynamics are generally compressible and inviscidity. Consequently, in aerodynamics, the rheological model in Eq. (71) set the viscosity coefficients λ = µ = 0. It is important to note that since aerodynamic

###### (a) (b)

![image 37](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile37.png)

Relative Lerror2

PINO (operator learning) PINO (instance-wise learning) PINN LAAF-PINN SA-PINN

0.5

0.4

0.3

0.2

0.1

0.0

100 101 102 103

10-1

Runtime (s)

- Fig. 15. The results of solving Fluid Dynamics Equations with PINO: (a) Utilizing DeepONet to provide an initial solution, followed by constructing PDEs losses using the AD algorithm [117] (b) Employing FNO to provide an initial solution, then constructing PDEs losses using finite differences [35].


fluids are compressible, ∇ · v ̸= 0. Therefore, Eq. (67) is modified according to the compressible and inviscid properties of fluids in aerodynamics:

D(ρv) Dt

+ ρv(∇ · v) = −∇p + ρf

. (78)

∂ρ ∂t

+ ∇ · (ρv) = 0

Mao et al. [190] used Eq. (78) to model the high-speed compressible inviscid aerodynamics problems, for example, the Sod shock-tube problem, as shown Fig. 16a. The authors also discussed the strategies for selecting the positions of sample points for discontinuous problem. Instead of using FNN, Peng et al. [191] applied graph neural network (GNN) with the Euler equations to study the transient compressible fields via limited probed data. It has been shown that, once the network is well-trained, the predictions can be made within 1 ms and highly reliable explosive overpressure can be inferred. Ren et al. [192] extend PINNs to learn and forecast the steady-state aerodynamics flows around a cylinder with high Reynold numbers. Apart from the limited measured data, the RANS equations in Eq. (77) and Eq. (78) served as additional knowledge for neural network training [192], as shown in Fig. 16b.

Other works have extended the application of PINNs to aerodynamics. Li et al. [193] utilized PINNs for predicting the gas bearing problems, including the flow field and aerodynamics characteristics. Joshi et al. [194] introduced specific weights (hyperparameters) to balance the loss terms from different equations for both low and high speeds. Auddy et al. [195] considered self-gravity of gas flows, which is essential in astrophysics.

- 4.2.3. Multiphase and moving boundary problems The boundary tracking algorithms are also possible to be modeled by PINNs when facing multiphase and


moving boundary problems. Wang and Perdikaris [103] tested the performances of PINNs with respect to simple Stefan problems where moving boundaries or free surfaces exist. In the numerical examples, the authors also presented promising results for multi phases scenarios. However, the moving and free boundaries considered in that work did not undergo any deformations. The moving boundaries have remained the same shape throughout the whole modeling. Jalili et al. [196] implemented the well-known Volume-of-Fluid (VOF) method [197], which is a prevailing boundary tracking algorithm in hydrodynamics study, in the PINNs loss function. By doing so, floating bubbles under a thermal field were modeled.

Based on the Lagrangian description, some hydrodynamics methods have been also developed. The use of the Lagrangian description makes the framework easily track free surface boundaries, which are denoted by training sample points, during the modeling. Among them, the neural particle method (NPM) is the most typical one

###### (a) (b)

![image 38](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile38.png)

![image 39](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile39.png)

![image 40](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile40.png)

![image 41](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile41.png)

- Fig. 16. Applications of PINNs in Aerodynamics: (a) Solving the compressible and inviscid Euler equations [190]. (b) Solving the RANS equations [192].


for free surface boundaries [198]. As presented, the NPM discretized the temporal domain into pieces, while the neural network is utilized to approximate the spatial domain. Later, Bai. et al. [94] extended the framework and proposed the general neural particle method (gNPM). The flowchart of the gNPM is presented in Fig. 17a. In the gNPM, spatial derivatives and outputs of neural networks are simplified to speed up the training process. Moreover, a pressure normalization scheme is introduced into the framework so that the gNPM can produce a reliable pressure field. Due to the use of the Lagrangian particles, Shao et al. [199] integrated the alpha-shape algorithm [200] with the NPM to identify the boundary particles, enabling interactions between flow and solid boundaries or structures.

Another way to solve the moving boundaries is to transfer the Eulerian description into the Lagrangian frame [201], the transformation is given by

∂xE ∂XL

∂ ∂xE

∂ ∂XL

, (79)

=

where xE and XL are the coordinates under Eulerian and Lagrangian descriptions, respectively. Besides, the distance network in Eq. (35) is applied to exactly impose the zero-pressure condition for the free surface. By exploiting the versatility of neural networks, PINNs-based algorithms are robust and stable for irregular node distributions, as shown in Fig. 17a.

Operator learning also serves as an alternative way to cope with multiphase and moving boundary problems. Wen et al. [120] integrated the U-Net structure with FNO and proposed the U-FNO model, as shown in

- Fig. 17b. In their work, the flow of CO2 and water in the context of geological storage of CO2 was considered. Compared to the traditional models of deep learning, the U-FNO exhibited excellent generalization properties and convergence rates. Furthermore, the U-FNO can achieve better accuracy when facing heterogeneous inputs. Diab et al. [202] proposed physics-informed DeepONet (PI-DeepONet) for multiphase flow in porous media. Using operator learning, the trained PI-DeepONet was capable of predicting solutions under any given flux functions (boundary conditions), which greatly alleviated the computational expense of multiphase modeling in porous media.

- 4.2.4. Multiscale and multiphysics The multiscale formulation also provides a different way to solve fluid mechanics. In general, the solution


fields can be decomposed into the fine-scale term and the coarse-scale term. By applying the variational multiscale formulation, Hsieh and Huang [203] derived a novel physics-informed loss function based on the least squares multiscale functional form. In the case studies, the 2D and 3D advection-dominated flow problems were conducted to demonstrate the effectiveness of the proposed loss function. Apart from using multiscale losses, Jin et al. [204] focused on neural network structures and developed the asymptotic-preserving neural network (APNN) for linear transportation equations, which decomposed the micro- and macro-variables via two independent networks, as shown in Fig. 18a.

Alongside PINNs, operator learning also sheds light on multiscale fluid modeling. Lin et al. [205] implemented the DeepONet to infer the bubble dynamics across different scales. In general, different equations and methods are required to deal with the bubble growth at different scales, for example, using the Rayleigh–Plesset (R-P) equation for the macroscale and the dissipative particle dynamics (DPD) for microscale. In the paper, the R-P and DPD modeling results were used to train different DeepONets. Through numerical tests, the authors demonstrate the possibility of using DeepONets to speed up the solving process of the bubble dynamics at different scales. Later, the framework was extended by seamlessly combining both the macroscale and microscale knowledge in a single DeepONet to predict the dynamic behaviors of bubbles at different scales [206]. It has been demonstrated that DeepONet successfully learned the mapping operators for bubble growth dynamics.

More importantly, the DeepONet offered a novel way to form a unified modeling method across scales instead of using traditional multiscale modeling approaches. Cai et al. [207] and Mao et al. [208] proposed the DeepM&Mnet, where the “M&M” denotes the words “multiphysics” and “multiscale” based on the operator learning technique. The proposed DeepM&Mnet comprised numbers of pre-trained DeepONets, as shown in

- Fig. 18b. In Mao’s framework, the DeepM&Mnet was developed for hypersonic flow problems with shocks, which may involve sharp density gradients spanning across various magnitudes. By preparing data in terms


![image 42](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile42.png)

- (a)
- (b)


![image 43](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile43.png)

![image 44](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile44.png)

![image 45](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile45.png)

![image 46](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile46.png)

- Fig. 17. Applications of PINNs and operator learning in multiphase and moving boundary problems: (a) The flowchart of the general neural particle method (gNPM) [94]: comparisons between the general neural particle method (gNPM) and the incompressible smoothed particle hydrodynamics (ISPH) for the 2D dam-breaking problem. (b) The schematic of the U-FNO for multiphase flow and error evolution for different algorithms [120].


- (a)
- (b)


![image 47](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile47.png)

![image 48](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile48.png)

![image 49](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile49.png)

![image 50](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile50.png)

![image 51](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile51.png)

- Fig. 18. Applications of PINNs and PINOs in multiscale and multiphysics: (a) Multiscale PINNs for linear transportation equations. Two neural networks are designed for micro- and macro-variables, respectively [204]. (b) The multiscale physics-informed DeepONets for multiscale fluid modeling problems [207, 208].


of flow velocity and temperature under scenarios whose densities span eight orders of magnitude downstream of the shock, the DeepM&Mnet accurately and efficiently predicted velocity and density fields. To ensure the accuracy of the wide range of velocity fields, the mean absolute percentage error (MAPE) was implemented in the loss function.

Wu et al. [209] proposed two convolutional DeepONets to deal with the linear transportation problem. Ahmed and Stinis [210] developed the multi-fidelity operator network (MFON), where an auxiliary term that comes from the Galerkin proper orthogonal decomposition was added to a DeepONet. The effectiveness of the proposed MFON was then demonstrated via a viscous Burgers equation problem and a 2D vortex merger problem.

- 4.2.5. Summary The same as aforementioned in solid mechanics, PINNs is currently still in its infancy as a forward problem


solver in computational fluid mechanics. The computational efficiency still impedes the use of PINNs on many problems of interest. Besides, the variational loss is not commonly seen in the context of hydrodynamics problems, while the strong form loss function still plays a vital role. As it is well known, with an increasing number of loss terms, more challenges and difficulties will be encountered during the training process. Therefore, training robustness also remains a huge issue that hinders the applications of PINNs in the context of fluid

modeling. However, the great potential of PINNs has been found as an effective tool for inverse problems in fluid mechanics, such as field reconstruction and essential parameter estimation. The above PINNs frameworks for forward problems can be applied to inverse studies with small modifications in fluid mechanics. More details regarding the PINNs for inverse problems can be found in Section 5.2.

On the contrary, operator learning serves as a surrogate modeling scheme for fluid flows. Despite its datadriven nature, physics knowledge in terms of governing equations can also guide the learning process, such as PINO. It has shown excellent generalization properties for predicting fluid flow problems even with sharp gradients and complex geometries. Moreover, once the neural operator is trained, the neural operator can be reused for different boundary conditions. This is an extraordinary advantage compared to PINNs, because a PINNs is generally applicable for one set of boundary conditions. Re-training is necessary for a PINN if the boundary conditions of the target fluid problem are changed. Another advantage of operator learning is its discretization-invariant properties. In fact, great efforts have been witnessed in fluid modeling enhanced by operator learning, trying to reveal details of fluid fields via low-resolution results. By using operator learning, it is straightforward and effective to obtain super-resolution results.

In the future, uncertainties, which are crucial in practical applications, should be effectively incorporated into or considered within AI for PDEs (AI4PDEs).

- 4.3. Biomechanics


- 4.3.1. Soft tissue deformation Computational models of soft tissue mechanics have the potential to provide valuable patient-specific di-

agnostic insights. However, their clinical deployment has been limited due to the high computational costs associated with traditional numerical solvers for biomechanical simulations. PINNs can be used to simulate the deformation of soft tissues, such as skin or organs, under various loads or boundary conditions [211]. This capability is critical for understanding and predicting tissue behavior in different scenarios.

Buoso et al. [115] introduce a novel approach to generate realistic numerical phantoms of the left ventricle by combining statistical shape learning, biophysical simulations, and tissue texture generation, as shown in Fig. 19a. This study addresses the limitations of previous in-silico phantoms by increasing variability and realism. The generated data can be used for standardized performance assessment of cardiovascular magnetic resonance acquisition, reconstruction, and processing methods.

PINNs based on graph convolutional networks (GCNs) and the variational principle has also been proposed, which can unify the solving of PDE-governed forward and inverse problems [81]. Then, Dalton et al. developed an efficient emulation of soft tissue mechanics using the PINNs based on graph neural networks (GNNs) [116], as shown in Fig. 19b. GNNs can handle the unique geometry of a patient’s soft tissue without requiring low-order approximations. The physics-informed training approach simulates the soft tissue mechanical behavior. With PDEs, the approach based on PINNs accurately predicts the deformation field of the liver, left ventricle, and brain models under various loading conditions. PINNs based on GNNs are also used to solve brain mechanics, aiding in understanding the microstructure-mechanics relationship in human brain tissue [212].

Lin et al. [122] developed the energy-based PINNs for viscoelastic buckling, biological tissue growth and morphological evolution. This study found that the inherent oscillations of the neural network optimizer during training could serve as a natural perturbation, allowing the model to capture creep buckling and structural instabilities without the manual introduction of artificial imperfections. PINNs could be useful for studying the specific folding and wrinkling patterns seen in developing tissues.We found that the approach to using PINNs for simulating soft tissue problems is similar to that for solid mechanical problems, where the minimum potential energy function is used as the loss function.

- 4.3.2. Blood flow of biomechanics Computational modeling of blood flow and cardiovascular dynamics presents significant challenges due to


the complexity of the underlying physics and patient-specific geometries. PINNs integrate PDEs and data to provide a novel approach for modeling blood flow in biomechanics. This capability has significant implications for cardiovascular disease diagnosis, treatment planning, and personalized medicine.

Sun et al. [102] developed a physics-constrained deep learning approach shown in Fig. 20a for surrogate modeling of fluid flows without relying on any simulation data, making it suitable for parametric fluid dynamics

- (a)
- (b)


![image 52](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile52.png)

![image 53](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile53.png)

![image 54](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile54.png)

- Fig. 19. Applications of PINNs in soft tissue: (a) three main blocks of the framework: generation of the shape model (I), generation of the functional model (II), and definition of the personalized biophysical left ventricular model [115]. (b) The schematic of a physics-informed GNN emulator and emulation results for Liver and Left Ventricle model [116].


(a) (b)

![image 55](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile55.png)

![image 56](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile56.png)

![image 57](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile57.png)

![image 58](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile58.png)

- Fig. 20. Applications of PINNs in blood flow of biomechanics: (a) The PINNs framework for surrogate modeling of blood flows, and results of PINNs and CFD solutions of idealized stenotic flows at different viscosity parameters [102]. (b) Physics-constrained prediction of idealized stenotic flows and aneurysmal flows of different geometries, the simulation geometries included two idealized structures (cylinder, bifurcation), and two aneurysms that were segmented from brain digital subtraction angiography (DSA) images [215].


problems where data is often scarce. Their numerical experiments on various internal flow problems relevant to hemodynamics demonstrate the potential of this approach. Additionally, PINNs has been used to model blood flow in patient-specific geometries by incorporating clinical data, providing insights into complex cardiovascular dynamics [213].

The applications of AI for PDEs in various cardiovascular imaging modalities, including echocardiography, cardiac computed tomography (CT), cardiovascular magnetic resonance imaging (CMR), and imaging in the catheterization laboratory, have also been explored, demonstrating the versatility of AI for PDEs [214]. Furthermore, various neural network architectures, such as fully connected networks, Fourier networks, and multiplicative filter networks have been employed to model 3D blood flows using PINNs, showcasing the potential for efficient and accurate modeling of complex blood flow shown in Fig. 20b [215].

Moreover, optimization techniques, such as variable-separated physics-informed neural networks based on adaptive weighted loss functions (AW-vsPINN), have been developed to apply to blood flow models in arteries. These methods decompose the blood flow problem into simpler sub-problems, reducing complexity and improving the efficiency of the neural network training process [216].

We have found that the simulation of blood flow in biomechanics closely aligns with the governing equations used in fluid mechanics. Therefore, the study of blood flow in biomechanics closely resembles the application of fluid mechanics to biological vascular flows.

- 4.3.3. Summary


AI for PDEs is a powerful tool for addressing the forward problem in biomechanics. It has been applied to various biomechanical issues such as tissue deformation, blood flow simulation, and morphodynamics. By enhancing our understanding of these phenomena, AI for PDEs can aid in developing new treatments for diseases like cardiopathy and other cardiovascular conditions. By incorporating the governing equations of biomechanics into neural networks, AI for PDEs can provide more accurate predictions of biological tissue behavior. With proper training, it can solve complex biomechanical problems more efficiently than traditional numerical methods, which are often computationally expensive. Moreover, AI for PDEs can model a wide range of biomechanical phenomena, from simple to complex systems, thereby broadening their applicability in the field.

Biomechanics employs methodologies from both solid and fluid mechanics, such as the use of hyperelastic constitutive equations from solid mechanics. Therefore, the application of AI for PDEs in biomechanics shares similarities with both solid and fluid mechanics. However, solving biomechanical problems requires extra consideration of biochemical factors such as nutrient diffusion, growth factor concentration, and gene expression.

Traditional modeling approaches often rely on simplified assumptions and conditions that struggle to capture the complexity of morphogenetic processes. However, recent advances in AI for PDEs offer promising avenues for integrating physical principles with data-driven approaches. In the future, AI for PDEs has the potential to combine multiscale data and bridge the gap between molecular, cellular, and tissue-level processes. AI for PDEs could be instrumental in uncovering missing or unknown physical relationships and mechanisms. By integrating PDEs with experimental data, we can potentially gain new insights into the intricate interplay of multiscale processes in biomechanics.

###### 5. AI for PDEs in the application of inverse problems of computational mechanics

- 5.1. Solid mechanics


- 5.1.1. Identification of Elastic Modulus and Poisson’s Ratio


Haghighat et al. (2021) [24] were the first to propose the use of PINNs to solve inverse problems in solid mechanics, addressing both elastic and elastoplastic issues, as illustrated in Fig. 21a. In elasticity, the approach starts by gathering data through analytical solutions or high-precision numerical solutions. Multiple neural networks are used to fit multiple variables (displacement and stress), and a loss function is constructed using data loss, equilibrium equations, and constitutive equations. We consider the problem of two-dimensional plane stress to explain the idea:

L = |uˆx − u∗x| + |uˆy − u∗y| + |σˆxx − σxx∗ | + |σˆyy − σyy∗ | + |σˆxy − σxy∗ |

+ |σxx,x + σxy,y − fx∗| + |σyx,x + σyy,y − fy∗|

+ |(λ + 2G)εxx + λεyy − σxx| + |(λ + 2G)εyy + λεxx − σyy| + |2Gεxy − σxy|

(80)

where the superscript ∗ indicates the given data, and λ and G are Lame constants (set as the inverse problem variables to be optimized). The least squares | · | is used for fitting, and λ and G are obtained by optimization using the given displacement, stress, and body force fields. Note that this formulation assumes simultaneous availability of both displacement and stress field data. In practical experimental settings however, stress fields are rarely measured directly and are typically obtained from displacements via constitutive assumptions.

For elastoplastic mechanics, the approach is similar, although the equations change to J2 flow theory for plane strain conditions. According to the J2 flow theory, we add plasticity multiplier γ and the KKT conditions

for convex optimization: L = |uˆx − u∗x| + |uˆy − u∗y| + |σˆxx − σxx∗ | + |σˆyy − σyy∗ | + |σˆxy − σxy∗ | + |σˆzz − σzz∗ |

+ |σxx,x + σxy,y − fx∗| + |σyx,x + σyy,y − fy∗|

- 2

- 3


- 2

- 3


G)εkk + 2G(εxx − ε∗xxp) − σxx| + |(λ +

G)εkk + 2G(εyy − ε∗yyp) − σyy|

+ |(λ +

, (81)

2 3

G)εkk + 2G(εzz − ε∗zzp) − σzz| + |2G(εxy − ε∗xyp) − σxy|

+ |(λ +

σs 3G

) − ε¯∗p| + |[1 − sign(¯ε∗p)]|ε¯∗p|| + |(1 + sign(F))|F|| + |ε¯∗pF|

+ |(¯ε −

where the first line represents data loss (all variables marked with ∗ are given beforehand), the second line represents the equilibrium equations, the third and fourth lines are the constitutive equations with the superscript p indicating the plastic part, and the last line includes the KKT conditions. The first item in the KKT

conditions is the J2 theory plasticity multiplier γ = ε¯∗p = ε¯− σs/(3G), ε¯ = 2εijεij/3, and ε¯p = 2εpijεpij/3. F is the yield surface function, defined by J2 theory as F = 3sijsij/2 − σs. sign is as follows:

 

1 x > 0 0 x = 0 −1 x < 0

(82)

sign(x) =



One issue of the above formulation is the reliance on plastic strain data, which are probably difficult to measure experimentally. Furthermore, the inclusion of KKT conditions via sign functions introduces nondifferentiabilities that will complicate gradient-based optimization. It is worth noting that the units of stress and displacement in Eq. (80) and Eq. (81) must be consistent. Clearly, Eq. (81) encompasses all the PDEs described by J2 theory for elastoplastic mechanics. Hence, optimizing Eq. (81) involves fitting displacement and stress using multiple neural networks (similar to Eq. (80)), then setting λ, G, and σs as optimization variables for solving the inverse problem. If a theory other than J2 is used, the method remains the same, though the specific PDEs would differ. Moreover, the plastic strain in Eq. (81) is difficult to measure experimentally in practice, which precludes the use of this framework for material identification.

For isotropic but heterogeneous materials, Chen et al. (2021) [217] suggest identifying the elastic field in isotropic and inhomogeneous materials as shown in Fig. 21b. However, instead of mapping coordinates to displacement fields, it maps coordinates to elastic modulus fields. The strain field is calculated from the given displacement field using kinematic equations, and the elastic field is then computed at the coordinates of the strain fields using neural networks. Stresses are subsequently calculated using isotropic elasticity constitutive relations, and these stresses are used to derive partial differential fields through convolutional kernel differentiation. The final loss function is established based on equilibrium equations, and it’s optimized to tune the neural network parameters in the elastic modulus field. It’s critical to note that merely using equilibrium equations is insufficient. Theoretically, we must also incorporate force boundary conditions or an average modulus of elasticity. This average modulus is used to calibrate the learned modulus back to realistic conditions because the modulus field learned solely from equilibrium equations can just represent a pattern, whose amplitude is undetermined. Thus, an average modulus is required to realign it with reality, assuming prior knowledge of the material’s properties. If there is no prior knowledge, applying force boundary conditions is necessary. It is important to emphasize that these force boundary conditions are not only applied at the boundaries but can also be implemented in internal domains if the loading conditions are special. Details can be referred to [217]. Unlike learning a fixed modulus, this neural network mapping establishes a link from coordinates to the elastic modulus field, not merely as optimization variables. Additionally, learning physical equations through convolutional neural networks’ kernel functions is feasible by setting the elastic modulus and strain fields in advance. There are also approaches that learn PDEs. Brunton et al. [218] proposed SINDy, which discovers governing equations from data for nonlinear dynamical systems.

Furthermore, Liu et al. (2024) [219] presented a similar idea for solving the inverse problem of thermal conductivity for isotropic and heterogeneous materials. They fit temperature data using Data Net and then

- (a)
- (b) (c)


![image 59](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile59.png)

![image 60](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile60.png)

![image 61](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile61.png)

![image 62](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile62.png)

![image 63](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile63.png)

- Fig. 21. Applications of PINNs in identifying elastic modulus and poisson’s ratio: (a) Identification of elastic modulus, Poisson’s ratio, and yield stress in homogeneous and isotropic elastoplastic materials [24], (b) Identification of the elastic modulus field in non-uniform isotropic materials [217], (c) Identification of thermal conductivity in non-uniform isotropic materials [219].


used PDEs Net, based on PINNs, to solve for non-uniform thermal conductivity, as depicted in Fig. 21c. This method combines direct data fitting with physical laws to refine the prediction of material properties.

- 5.1.2. Identification of Constitutive Equations The identification of constitutive equations remains a core issue in solid mechanics, primarily focusing on


the relationship between stress and strain. Traditional methods usually involve defining a specific form of the constitutive equation and then determining the unknown parameters of the model based on experimental results (displacement fields and external load forces). Li et al. (2022) [220] proposed using a neural network to replace the constitutive equation, where the relationship from strain to stress is determined by the parameters of the neural network, as shown in Fig. 22a. The loss function is defined as:

L = ˆ

|σij,j + fi|2dΩ +

Ω

s=1

σij = NN(εij;θ)

βs|ˆ

(σijnj)dΓ − Ts|2

, (83)

Γts

s, and Ts can be easily obtained from universal testing machines for the corresponding load. Additionally, the displacement field under Ts can be captured using Digital

where Ts is the total force for the s-th force boundary Γt

### (a) (b)

![image 64](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile64.png)

![image 65](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile65.png)

![image 66](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile66.png)

![image 67](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile67.png)

- Fig. 22. Applications of AI for PDEs in Constitutive Equation Identification: (a) Non-parametric model: neural network fitting of strain and stress relationships in hyperelastic materials [220], (b) Parametric model: predefined hyperelastic constitutive forms with fitting of preceding parameters [211, 221].


Image Correlation (DIC), and then the strain is calculated using kinematic equations and inputted into the neural network NN(εij;θ) to obtain the corresponding stress. The stress field is used to establish the loss of internal balance equation and the force boundary conditions. The loss about force boundary conditions integrates over the force boundary Γt

s using experimental load data. Note that non-homogeneous force boundary conditions are essential. If only displacement data are available without force boundary conditions, it is impossible to determine the constitutive equation theoretically. Fig. 22a outlines a non-parametric hyperelastic constitutive model using a neural network, but a parametric model as shown in Fig. 22b can also be established. For example, the form of the constitutive equation can be pre-determined (e.g., the HGO model for biomaterials by [211]), considering all possible base functions in the constitutive equation [221], and then using optimization techniques to determine the parameters ahead of these base functions to define the form of the constitutive equation.

It is important to note that both parametric and non-parametric models require non-homogeneous force boundary conditions. It is easy to imagine two different materials subjected to a displacement-controlled tensile test that exhibit exactly the same displacement field. If non-homogeneous force boundary conditions are not provided, it is impossible to distinguish between these two materials solely from the displacement field, without any information about the applied forces. Therefore, non-homogeneous force boundary conditions constitute indispensable information for inverse problems. The essential difference between these implementation methods lies in the form of σij = NN(εij;θ) in Eq. (83), where the non-parametric model uses a neural network and the parametric model uses a predefined function. Currently, AI for PDEs applications in identifying constitutive equations are primarily focused on hyperelastic materials, with fewer studies on history- and path-dependent elastoplastic materials, and rate-dependent viscoelastic materials. Future research using neural networks to replace constitutive equations will gradually address such complex materials requiring solid constitutive theory

foundations to establish physically meaningful neural network constitutive models. We believe this research area holds significant potential and prospects because constitutive equations primarily involve fitting, and neural networks inherently possess robust fitting capabilities.

It is important to distinguish between two classes of inverse problems in constitutive modeling: parameter identification, where the functional form of the constitutive law is known a priori and only material constants are unknown; and constitutive law discovery, where the functional form itself is learned from data. The former is well-suited for PINNs with trainable scalar parameters, while the latter often requires more expressive representations such as neural networks with built-in physical constraints such as polyconvexity or thermodynamic consistency [222]. The latter remains an active area of research with significant open challenges, including ensuring physical admissibility of learned constitutive relations.

An alternative to neural-network-based constitutive modeling is sparse regression in the weak form, often referred to as Variational System Identification (VSI). This approach constructs a library of candidate functions such as polynomial, exponential or physics-inspired terms and solves a sparse linear system to identify which terms govern the material response. Unlike PINNs-based methods, VSI does not require neural network training, yields interpretable models and is naturally robust to noise due to integration by parts. A very interesting approach has been recently presented in the context of phase field models for fracture by Livingston et al. [223], who employed VSI to infer the degradation function, geometric crack function, and crack driving history term from synthetically generated data, demonstrating successful model selection among competing fracture formulations.

- 5.1.3. Topology Optimization Topology optimization is a classic inverse problem. It modifies the material distribution based on a prede-


fined objective function, such as minimizing compliance. Typically, changing the material distribution requires sensitivity analysis, which mathematically involves deriving the objective function with respect to the density field (the physical representation of material distribution). Notably, the objective function alone is insufficient without the stress-deformation state under the current density field, which can be mathematically expressed as:

- 1

- 2


ˆ

σ∗ : εdΩ

Objective Function (Minimize Compliance): min

F =

ρ

Ω

, (84)

Material Constraint: ˆ

ρ(x)dΩ = V¯

Ω

where ρ is the density field (material distribution), a scalar field function ranging from 0 to 1. σ∗ is the stress field adjusted according to the density field ρ, dictating the material degradation, typically set as σ∗(x) = g(ρ)∗σ(x). A widely used choice is the SIMP [224] interpolation, for which g(ρ) = ρp with p > 1 being a penalization parameter. σ(x) is determined by substituting the displacement field u into the kinematic equation and then through the constitutive relation. For linear elastic problems, the original stress field is modified to σ∗(x) as expressed mathematically:

- 1

- 2


L = ˆ

σ∗ : εdΩ − ˆ

f · udΩ − ˆ

¯t · udΓ Displacement Constraint: u(x) = u¯(x),x ∈ Γu

Minimum Potential Energy Principle: min

, (85)

u

Γt

Ω

Ω

where σ∗(x) is derived from the displacement field and the current density field, with the constraint that the displacement field satisfies essential boundary (Γu) conditions.

Notably, the compliance minimization in Eq. (84) is not independent of the equilibrium condition, but must be carried out subject to the equilibrium constraint represented by the minimum potential energy principle in Eq. (85). These two optimization problems differ in that each update to the density field in Eq. (84) through gradient descent, ρ∗ = ρ − α∂F/∂ρ, necessitates a complete optimization of the potential energy L. Thus, mathematically, it is a coupled optimization problem under material and displacement constraints. While compliance optimization can rely on traditional optimization algorithms, the displacement field can be obtained using solvers like the traditional finite element method.

- (a)
- (b)


![image 68](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile68.png)

![image 69](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile69.png)

![image 70](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile70.png)

![image 71](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile71.png)

Element sensitivity

|MMA<br><br>optimizer|
|---|


![image 72](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile72.png)

![image 73](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile73.png)

Element density

Deep energy method

Optimized

simulation

designs

![image 74](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile74.png)

- Fig. 23. Applications of DEM in topology optimization: (a) Traditional methods such as the moving asymptote method is used to iterate the density field for compliance minimization, and DEM is for the displacement field [114]. (b) DEM is used for both the density and displacement field [226]


Recent studies have proposed using DEM to replace compliance and potential energy optimization. He et al. (2023) [114] adopted the idea from Zehnder et al. (2021) [225] to replace the finite element calculation with the DEM method for minimum potential energy, but the target compliance minimization function is still calculated using traditional methods like the moving asymptote method, as illustrated in Fig. 23a. Subsequently, Jeong et al. (2023) [226] also replaced the traditional algorithms with an idea similar to DEM for target compliance minimization function, establishing a fully connected neural network function mapping coordinates to the density field. Compliance obtained from the displacement field and the density field is then optimized once, updating the neural network parameters of the density field and this optimized density field is re-entered into the DEM to compute the displacement field, repeating until convergence, as shown in Fig. 23b. It is noteworthy that the combination of DEM and topology optimization centralizes some optimization problems using neural network optimization algorithms instead of traditional methods, such as using PINNs or DEM to replace finite element calculations for PDEs in solid mechanics. With target optimization functions solved using PINNs methods [226], traditional SIMP [227], or traditional MMA [114], different algorithms for solving target optimization functions and different methods for solving mechanical displacement fields form various works combining deep learning and topology optimization.

Since the bulk of the computational effort comes from continually recalculating the displacement field for updated geometric topologies, using operator learning to accelerate the computation of the forward problem in topology optimization has significant potential to enhance the total speed of topology optimization.

- 5.1.4. Defect Identification Defect identification in solid mechanics has garnered significant attention and presents a challenging task


because it involves solving inverse problems with unknown geometries, topologies (such as the locations of the

internal defects), and material properties of inclusions. Therefore, characterizing internal inclusions and defects is a classical and complex inverse problem. Zhang et al. (2022) [228] applied PINNs to defect identification. Their approach involves placing displacement sensors along the boundaries, using known loads and boundary displacement fields to infer the locations of internal defects in problems without body forces. The mathematical expression, similar to classical PINNs that include data and PDEs loss, is as follows:

L = β1Lpdes + β2Lu + β3Lt + β4Ldata, (86)

where Lpdes, Lu, Lt, and Ldata respectively represent the loss from physical equations, displacement boundary conditions, force boundary conditions, and boundary data loss functions as follows:

Npde

1 Npdes

|σ(x(n))ij,j|2,x(n) ∈ Ω(θgeo)

Lpdes =

n=1

Nu

1 Nu

|u(in)(x(n)) − u¯(in)(x(n))|2,x(n) ∈ Γu(θgeo)

Lu =

n=1

Nt

1 Nt

|σij(x(n))nj − t¯i(x(n))|2,x(n) ∈ Γt(θgeo)

Lt =

n=1

Nd

1 Nd

|ui(x(n)) − u¯∗i (x(n))|2,x(n) ∈ Γdata(θgeo)

Ldata =

n=1

(87)

where the domain Ω(θgeo) and the boundaries Γu(θgeo), Γt(θgeo), Γdata(θgeo) are functions of the geometric parameters θgeo, which denote the internal defect locations. For instance, a circular defect could be described by the circle’s center and radius, θgeo = {xc,yc,r}. This approach’s core integrates θgeo into the sampling coordinates, allowing optimization of both the parameters of the neural network for coordinates-to-displacement field and θgeo during backpropagation. Ultimately, extracting the θgeo parameters serves to pinpoint the defect location. Notably, Zhang et al. (2022) [228] applied PINNs not only to linear elasticity but also to hyperelasticity and elastoplasticity problems, detecting internal defects’ material parameters by treating them as optimization variables. The overall framework of their method is shown in Fig. 24a. Sun et al. (2023) [229] proposed a purely data-driven algorithm for identifying multiple defects, using boundary element methods to calculate defects and displacement fields and employing convolutional neural networks to map boundary displacement fields to defects as shown in Fig. 24b.

However, current defect detection has not yet incorporated operator learning, which could potentially accelerate the computation of the forward problem under various defects, thereby enhancing the overall speed of defect detection.

- 5.1.5. Summary We have identified three main approaches for applying AI for PDEs to inverse problems in solid mechanics.


The first approach involves setting the variables to be identified in the inverse problem as optimization variables, such as elastic moduli and Poisson’s ratios, and using PINNs for tasks like defect detection. The second approach is applied when the inverse problem is more complex, such as when dealing with heterogeneous fields, where a new neural network is constructed to approximate the heterogeneous field and incorporated into the loss function for optimization, e.g., in density function optimization for topology. The third approach leverages neural networks to learn the mapping between variables, such as constitutive equation identification (mapping strain to stress via a neural network).

For many inverse problems, the first approach offers a simpler framework because it avoids the traditional method of repeatedly solving forward problems to determine the parameters. Instead, the parameters are directly set as optimization variables within the existing deep learning framework, making the program and code structure relatively straightforward. This, however, does not imply that the underlying computations are trivial; they still involve derivatives of the loss function with respect to the optimization variables, which remain

- (a)
- (b)


![image 75](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile75.png)

- Fig. 24. Applications of AI for PDEs in defect identification: (a) PINNs for defect detection: Utilizing PINNs to identify internal defects by analyzing known loads and displacement fields at boundaries, applied to linear, hyperelastic, and elastoplastic issues by [228]. (b) Data-driven defect detection: An approach by [229] employing boundary element methods and convolutional neural networks to map displacement fields to detect multiple defects.


computationally intensive and complex. Nevertheless, current deep learning optimization frameworks effectively encapsulate these processes, making them appear simpler.

In the future, incorporating operator learning into inverse problems holds significant potential, as the core of most current inverse problems remains using PINNs to substitute finite element computations. Integrating operator learning could significantly accelerate the computation of each forward problem to enhance the computational efficiency of inverse problems substantially.

- 5.2. Fluid mechanics


- 5.2.1. Field reconstruction Raissi et al. [230] introduced the hidden fluid mechanics (HFM) that combined the knowledge from ob-


servation snapshots and the NS equations to evacuate and reconstruct the velocity, pressure fields, and even diffusions of passive scalars. A typical example of the HFM is shown in Fig. 25a. It has been demonstrated to be effective for studying the 3D hemodynamics of intracranial aneurysms without boundary conditions and inlet flow waveform, where only the concentration of a given passive scalar was known. Cai et al. [231] harnessed PINNs to infer 3D fields on an espresso cup. In that work, the tomographic background-oriented Schlieren (Tomo-BOS) imaging technique measures the density and temperature fields above a cup of espresso. Then, the authors embedded the measurements as well as the NS equations into the training process, enabling PINNs to reconstruct the 3D field in terms of velocity and pressure.

Later, a framework based on PINNs named artificial intelligence velocimetry (AIV), as shown in Fig. 25b, was proposed to recover the blood flow in physiology problems [105]. Only 2D velocity data, which was measured by snapshots of the platelet-tracking technique, was applied without knowledge of the inlet and outlet conditions. The AIV successfully reconstructs various 3D fields of quantities, including the velocity, pressure, and even the shear stress at vessel boundaries, as shown in Fig. 25b. The same framework also was extended to study the murine perivascular flows [232] and non-Newtonian fluids [233]. By combining the NS equations, non-linear rheological model, and sparse observation data, the PINNs successfully reconstructed both the velocity and stress fields at not only the in-domain area but also boundaries. Molnar et al. [234] also integrated backgroundoriented Schlieren techniques with PINN to study the global velocity and pressure fields in supersonic flows. In their framework, the Euler equations as well as the irrotational equation are treated as additional knowledge for learning.

Turbulent flow estimation is even more challenging due to its complexity. Integrating the NS equation and adjoint-variational data assimilation, PINNs has been demonstrated to be effective for evaluating the spatialtemporal evolution of turbulent flow with low dimension [235]. However, one of the disadvantages of the PINNs for turbulence is that it is hard to assess the neural network structure. The accuracy of PINNs is highly related to networks’ structure, while the relation remains to be explored [235]. Zhang et al. [236] harnessed PINNs to recover the vorticity fields of tornados with limited measurements. The predicted velocity can achieve great accuracies at different stages of tornados, including the single-cell stage, vortex breakdown stage, and multi-cell stage.

The neural operator is another way to recover the field quantities of fluid flows. Renn et al. [237] leveraged FNO to infer the vortex flow in subcritical cylinder wakes. It has been shown that the FNO was able to achieve high accuracy even at a Re number of 3060. Meanwhile, the FNO exhibited favorable computational efficiency, potentially enabling faster than real-time modeling and reconstruction. Rosofsky et al. [238] offered a wide range of inverse fluid benchmarks by using PINO, including wave equations, linear and nonlinear shallow water equations, and Burgers equations, as shown in Fig. 26. Lu et al. [239] proposed the multifidality DeepONet for the Boltzmann transportation equation. It is worth highlighting that, with the fast reconstructed global field quantities and traditional topology optimization algorithms, it is straightforward to further guide the design of structures under fluid flow conditions for multiple objectives. Li et al. [240] applied FNO to cope with 3D turbulent flow and large eddy simulation (LES). In terms of velocity spectrum, probability density functions of vorticity, and velocity increments, the results showed that the FNO performed better and more efficiently than traditional LES methods. More importantly, FNO can be extended to LES and turbulent modeling with high Re numbers.

- (a)
- (b)


![image 76](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile76.png)

![image 77](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile77.png)

![image 78](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile78.png)

![image 79](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile79.png)

- Fig. 25. Applications of PINNs in field reconstruction: (a) The typical example of the hidden fluid mechanics (HFM) [230]. (b) The artificial intelligence velocimetry (AIV) framework [105].


![image 80](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile80.png)

Fig. 26. Applications of FNO and PINO in field reconstruction for 2D inviscid Burgers equation [238].

### (a) (b)

![image 81](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile81.png)

![image 82](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile82.png)

- Fig. 27. Applications of PINNs in fluid parameter estimation and identification: (a) Inferring the boundary velocity condition of the lid-driven stenosis problem [81]. (b) Unveil the viscosity using PINNs [244].


- 5.2.2. Parameter estimation and identification in fluid Estimating and identifying parameters of fluids in terms of viscosity, density and other passive scalars are also

of great importance for fluid mechanics. In general, the unknown parameters can be simultaneously tuned along with the field reconstruction. Jagtap et al. [78] elucidated a general form of extracting essential parameters from fluid flows. In their work, the governing equations of fluid flows were considered to consist of various differential terms and a nonlinear operator

∂v ∂t

=H(x,t,v,vx,vxx,··· ,v2,v3,··· ,vxv2,···) H =a0 + a1x + a2x2 + ··· + b1v + b2v2 + ··· + c1vx + c2vxx + ··· + d1vxv2 + ··· ,

(88)

where a, b, c and d are unknown parameters that remain to be determined.

The effectiveness of that PINNs framework was demonstrated by a 1D viscous Burgers equation and a 2D inviscid Burgers equation. Yu et al. [241] employed PINNs with a gradient-enhanced technique to infer the effective viscosity and permeability in porous media. By numerical examples, the proposed PINNs framework provided reliable viscosity as well as permeability with only 5 to 10 sets of measured data at different sensor locations. Lou. et al. [242] extended this framework by the Bhatnagar-Gross-Krook (BGK) collision model. The numerical examples have shown that it is very efficient in solving inverse problems, even if the problem is ill-posed. Kou et al. [243] utilized PINNs to estimate the turbulent viscosity and mass diffusivity for turbulent mass transfer problems. Jin et al. [179] applied PINNs to infer unknown Re numbers using velocity data and NS equations. More surprisingly, the PINNs can be also effective even with missing or noisy boundary conditions. Gao et al. [81] utilized the graph neural networks to predict the velocity boundary condition of a lid-driven stenosis, as shown in Fig. 27a. Arzani et al. [244] developed a PINNs framework that incorporates the NS equations and boundary conditions as soft constraints during the training process, enabling the accurate reconstruction of near-wall blood flow from sparse data. Moreover, the framework was able to infer the viscosity of fluids, as shown in Fig. 27b. The proposed framework has potential applications in cardiovascular disease diagnosis and treatment planning.

- 5.2.3. Summary Field reconstruction and the estimation of the parameters are the major inverse problems in fluid mechanics.


It has been shown that AI for PDEs is very effective not only for laminar flows, but also for turbulent flows

with vorticities.

In summary, the loss functions, which are informed by physics, regulate the reconstructed fields from neural networks along with the limited observations. Thus, PINNs offers a novel and effective way to unveil the knowledge deeply hidden inside fluid flow, which is considered challenging to measure by conventional experimental equipment. As for operator learning, it focuses on learning the mapping between functions by available data. Its extraordinary generalization and discretization-invariant characteristics have made the operator learning distinguish from other CFD and deep learning-based fluid algorithms. In other words, a well-trained operator learning framework for fluid modeling can be generalized to a wide range of scenarios (with different boundary conditions, essential parameters, and even problem geometries) as well as maintaining accuracy and achieving super-resolutions. Therefore, it can be concluded that both PINNs and neural operators have appended the arsenal of computational fluid dynamics (CFD) and serve as additional tools for studying fluid phenomena inversely.

- 5.3. Biomechanics


- 5.3.1. Modeling Blood Flow Accurate modeling of blood flow is essential for understanding and predicting cardiovascular diseases such

as atherosclerosis and heart failure. Traditional CFD methods require high-resolution data, which is often challenging to obtain, especially near vessel walls. AI for PDEs can bridge this gap by incorporating governing equations into the learning framework, thus enabling accurate predictions from limited data.

Near-wall blood flow is particularly crucial for understanding cardiovascular diseases and designing effective treatments. Due to the limitations of medical imaging techniques, obtaining high-resolution data near vessel walls is challenging. Arzani et al. [244] developed a PINNs framework that incorporates the Navier-Stokes equations and boundary conditions as soft constraints during the training process, enabling the accurate reconstruction of near-wall blood flow from sparse data, as shown in Fig. 28a. This PINNs framework accounts for uncertainties in the data and enables accurate reconstruction of near-wall blood flow from sparse data. Besides, the coordinate transformation technique that maps the irregular physical domain to a rectangular computational domain is applied, which can handle complex vessel geometries. This represents a significant advancement over traditional CFD methods, which require high-resolution data for accurate simulations. The proposed method has potential applications in cardiovascular disease diagnosis and treatment planning.

Accurate prediction of arterial blood pressure is vital for cardiovascular disease diagnosis and treatment planning. Traditional methods, such as invasive catheterization or simplified computational models, often lack patient specificity. Kissas et al. [245] addressed these limitations by leveraging non-invasive 4D flow Magnetic Resonance Imaging (MRI) data and physics-informed machine learning techniques, as shown in Fig. 28b.. Their PINNs framework incorporates the governing equations of fluid dynamics (Navier-Stokes equations) and the arterial Windkessel model into the neural network architecture. In addition to predicting blood pressure, PINNs has been used for the super-resolution and denoising of 4D flow MRI data, enhancing the quality and utility of MRI data in clinical applications. These advanced techniques ensure more accurate and reliable measurements, further supporting cardiovascular disease diagnosis and treatment planning [246].

- 5.3.2. Material parameter identification in soft tissue Elasticity imaging aims to uncover the spatial distribution of mechanical properties such as the elastic mod-


ulus and Poisson’s ratio within biological tissues. This information is critical for various applications, including tumor detection and characterization. Traditional methods often rely on simplifying assumptions, such as homogeneous distributions for one material parameter, which can result in inaccuracies. Kamali et al. [247] leverage PINNs to solve linear elasticity problems and discover space-dependent distributions of both Young’s modulus and Poisson’s ratio using strain data, normal stress boundary conditions, and the governing physics equations, as shown in Fig. 29a. Unlike conventional methods that estimate one material parameter while assuming the other is homogeneous, the framework based on PINNs simultaneously estimates the spatial distributions of both elastic modulus and Poisson’s ratio. This approach was successfully demonstrated on a simulated hydrogel sample containing a human brain slice with distinct gray matter and white matter regions, accurately capturing the spatial distribution of mechanical properties and tissue interfaces [247]. The application of PINNs in

(a) (b)

![image 83](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile83.png)

![image 84](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile84.png)

![image 85](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile85.png)

![image 86](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile86.png)

![image 87](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile87.png)

- Fig. 28. Applications of PINNs in modeling blood flow: (a) PINNs could be used for solving Navier–Stokes equations. A few sensors (red dots) are used in the 2D stenosis model and aneurysm model, and the results predicted by PINNs are compared with the reference CFD data [244]. (b) Flow through the aorta/carotid bifurcation of a healthy human subject [245].

nonhomogeneous soft tissue identification allows for the precise determination of mechanical properties based on full-field displacement measurements under quasi-static loading conditions [248]. The PINNs also provides a tool for cardiac electrophysiology characterization and parameter estimation from sparse data [249].

Brain hemodynamics, which involves quantifying blood flow velocity, vessel cross-sectional area, and pressure, is crucial for diagnosing and treating cerebrovascular diseases. Transcranial Doppler (TCD) ultrasound is a common clinical technique for non-invasively measuring blood flow velocity within cerebral arteries. However, TCD is spatially limited due to constrained accessibility through the skull’s acoustic windows, providing measurements only at select locations across the cerebrovasculature. To address these limitations, Sarabian et al. [250] propose a novel physics-informed deep learning framework that integrates real-time TCD velocity measurements with baseline vessel cross-sectional areas obtained from 3D angiography images, as shown in

- Fig. 29b. This framework utilizes a physics-informed deep learning model to generate high-resolution maps of velocity, area, and pressure throughout the entire brain vasculature. By augmenting sparse clinical measurements with one-dimensional (1D) Reduced-Order Model (ROM) simulations, the model ensures that the predicted hemodynamic parameters are physically consistent and adhere to the governing equations of fluid dynamics. This approach enables the estimation and quantification of subject-specific cerebral hemodynamic variables with high accuracy, even without detailed knowledge of inlet and outlet boundary conditions [251].


- 5.3.3. Summary


While AI for PDEs represents significant advancements in the field of biomechanics, offering the potential for more accurate and efficient modeling of complex biological systems, several challenges remain. Addressing these challenges—data acquisition, interpretability, validation, model complexity, and generalizability—will be essential for the broader adoption and successful application of AI for PDEs in biomechanics and clinical practice. Future research should focus on developing strategies to overcome these barriers, such as improved data collection methods, enhanced interpretability techniques, robust validation protocols, simplified model implementation processes, and approaches to increase model generalizability. Through these efforts, the full potential of AI for PDEs in advancing our understanding and treatment of biomechanical phenomena can be realized.

- (a)
- (b)


![image 88](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile88.png)

![image 89](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile89.png)

![image 90](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile90.png)

![image 91](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile91.png)

|Available clinical data:<br><br>• 3D-ToF<br>• TCD ultrasound<br>| | |
|---|---|---|
| | | |
| |Area time-series<br><br>Velocity time-series<br><br>Initial area| |


|Compute initial velocities<br><br>Solve continuity equation| |
|---|---|
| |Initial velocities|


|Identify Windkessel model parameters, i.e.,<br><br>![image 92](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile92.png)|
|---|


|Validate:<br><br>• 4D flow MRI|
|---|


Predict:

![image 93](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile93.png)

| | |
|---|---|
|Physics-informed neural network (PINN)<br><br>Transformer networks<br><br>Residual loss<br><br>Minimize<br><br>Measurement loss<br><br>Interface loss<br><br>: Total number of collocation points : Total number of measurements : Slope recovery loss : Velocity residual loss : Area residual loss : Pressure residual loss<br><br>![image 94](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile94.png)<br><br>![image 95](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile95.png)<br><br>![image 96](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile96.png)<br><br>![image 97](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile97.png)<br><br>![image 98](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile98.png)<br><br>![image 99](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile99.png)<br><br>: Velocity measurement loss : Area measurement loss : Interface loss : Total loss : Ground Truth<br><br>![image 100](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile100.png)<br><br>![image 101](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile101.png)<br><br>![image 102](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile102.png)<br><br>![image 103](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile103.png)<br><br>![image 104](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile104.png)<br><br>![image 105](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile105.png)<br><br>![image 106](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile106.png)<br><br>![image 107](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile107.png)<br><br>Slope recovery loss<br><br>![image 108](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile108.png)<br><br>![image 109](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile109.png)<br><br>![image 110](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile110.png)<br><br>![image 111](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile111.png)<br><br>![image 112](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile112.png)<br><br>![image 113](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile113.png)<br><br>![image 114](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile114.png)<br><br>![image 115](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile115.png)<br><br>![image 116](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile116.png)<br><br>![image 117](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile117.png)<br><br>![image 118](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile118.png)<br><br>![image 119](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile119.png)<br><br>![image 120](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile120.png)<br><br>![image 121](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile121.png)<br><br>![image 122](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile122.png)<br><br>![image 123](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile123.png)<br><br>![image 124](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile124.png)<br><br>![image 125](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile125.png)<br><br>![image 126](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile126.png)<br><br>![image 127](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile127.png)<br><br>![image 128](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile128.png)<br><br>![image 129](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile129.png)<br><br>![image 130](2024_Artificial intelligence for partial differential equations in computational mechanics A review_images/imageFile130.png)| |


###### Fig. 29. Applications of PINNs in material parameters identification in soft issue . (a) Parameter estimation PINNs for 2D elasticity and results for the discovery of material parameter and stress distributions for the brain [247]. (b) Overview of the procedure of brain hemodynamics [250].

###### 6. Conclusion and outlook

This paper mainly reviews the algorithms of AI for PDEs (including Physics-Informed Neural Networks, Operator Learning, and Physics-Informed Neural Operators), the related theoretical research, and applications in the forward and inverse problems of computational mechanics, including solid mechanics, fluid mechanics, and biomechanics. Based on the current state of research, possible future directions for AI for PDEs in computational mechanics might include:

- (1) Nonlinear Problems: The core component of AI for PDEs is neural networks, which have strong

nonlinear capabilities. Therefore, future research on nonlinear problems theoretically has good prospects. For linear elasticity problems in solid mechanics, finite element methods are already quite perfect due to the positive definiteness and sparsity of the stiffness matrix, which can be quickly and accurately solved by direct matrix inversion. However, for some nonlinear problems, traditional finite element methods either solve the nonlinear equation system directly using Newton’s iterative method or transform and solve it explicitly using incremental steps. Neural networks, due to their inherent nonlinear capabilities, theoretically have an advantage in solving nonlinear problems in computational mechanics. Also, by training operator neural networks with existing numerical simulations or experimental results, and then using operator learning to provide a good initial solution for the initial iteration vector of the nonlinear equation system, the computational efficiency could be greatly improved theoretically. Hyperelastic problems, for example, are a good entry point because they are pathindependent and can be directly formulated as a nonlinear equation system.

- (2) Complex Phenomena with Inadequate Understanding: For such problems, due to their complex-

ity, the mathematical PDEs descriptions of these issues can only be approximations, meaning the simulation results still differ from actual experimental results. In this case, we can rely on data to fine-tune the results. That is, an approximate solution is first provided by the boundary conditions and an approximate physical equation, and then the simulation results are fine-tuned according to the experimental data, blending a small amount of data with an approximate physical equation, especially for simulating complex phenomena. As humanity’s understanding of the phenomenon becomes clearer, only the physical equations need to be corrected, and this framework remains unchanged.

- (3) Constitutive Equations: Constitutive equations have always been a core issue in mechanics, where

most of the work involves fitting. Typically, experts first construct a specific form of the constitutive model based on some basic physical principles and then fit the parameters in the model according to experimental stress-strain points. However, because of the fitting characteristics of neural networks, theoretically, they can replace constitutive equations. Most current research uses neural networks to directly fit the relationship between strain and stress. However, future studies could integrate fundamental principles of constitutive behavior, such as Noll’s three theorems and thermodynamic postulates like Drucker’s postulate in plasticity, into the neural network framework for constitutive equations. This would improve the convergence speed of the constitutive model and reduce the experimental data needed for stress and strain. Currently, most constitutive work in solid mechanics focuses on elasticity and hyperelasticity, but future explorations could include rate-dependent viscoelasticity and history-dependent elastoplasticity.

- (4) Foundation Models in Computational Mechanics: Based on current research on PINNs and


operator learning, it is very likely that the foundation model in computational mechanics will emerge in the future. Although current PINNs and traditional finite element methods still have significant gaps in accuracy and efficiency, PINNs may ultimately teach us how to incorporate physical equations into neural networks. Recent studies have found that operator learning can significantly speed up the simulation of forward problems, and there is theoretical evidence that operator learning can learn the families behind PDEs. Therefore, combining operator learning with algorithms for solving PDEs (algorithms for solving PDEs are not limited to PINNs, as finite element methods are also applicable) has a very promising academic and industrial future. Not only could it significantly increase the simulation speed for forward problems (accelerating by tens of thousands of times), but it could also use experimental data to simulate complex phenomena and integrate approximate constitutive equations to form a whole new set of foundation models in computational mechanics. These models would not only act as ultra-fast solvers for forward problems, but more importantly, they would serve as powerful engines for scientific discovery. By enabling real-time inverse analysis and learning from the interplay of data and physics, they could unveil new constitutive laws, identify hidden parameters in complex systems and accelerate

the design of novel materials and structures. Such a foundation model would be the ultimate computational engine for a digital twin, a living, virtual replica of a physical system, capable of integrating real-time sensor data to provide instantaneous predictions and insights, thereby revolutionizing predictive maintenance, design optimization, and operational control. In the past, expert systems were developed, but their performance was often lacking. However, with the advent of neural networks, there is renewed potential to revitalize expert systems. AI for PDEs soon play a crucial role in determining which models, physical laws, discretizations, and other factors are best suited for a given problem. Moreover, AI possesses various capabilities that can enhance and improve traditional techniques, solvers, and mesh generators. The recent achievement of AI earning a silver medal in the International Mathematical Olympiad (IMO) demonstrates that AI can perform complex mathematical reasoning [252]. These developments suggest that AI for PDEs holds significant promise in computational mechanics, potentially leading to the emergence of foundation models in this field.

At the same time, comparisons between AI for PDE and classical numerical methods such as finite element methods (FEM) should be interpreted with caution. Reported advantages in inference speed are often meaningful only when substantial offline training cost is amortized over many repeated-query scenarios, which is particularly relevant for operator-learning-based approaches. For single-instance engineering simulations, classical FEM often remains highly competitive in robustness, interpretability, and reliability. Similarly, accuracy comparisons are only fair when discretization level, computational budget, and geometric generalization range are matched consistently. Recent studies have shown that weak numerical baselines or incomplete reporting of training cost may lead to overly optimistic conclusions regarding machine-learning superiority [253]. Therefore, future development of AI for PDEs should place increasing emphasis on fair benchmarking and out-of-distribution generalization.

Scientific Artificial Intelligence (AI4Science) has garnered significant attention, similar to the work on neural networks in computer vision and language over the past decade. Its growth could mirror the rapid development seen in the Cambrian explosion of species. Initially, deep learning showed potential in these traditional scientific fields, but over time, its limitations became apparent. To overcome these shortcomings, traditional domain knowledge has been integrated to enhance AI’s effectiveness in these scientific areas. AI for PDEs is a prime example of such integration.

PDEs reflect a profound and quantified expression of human understanding of the physical world. Thus, PDEs constitute a form of knowledge that can be integrated into neural network training. The core idea behind AI for PDEs is the integration of data with physical equations, aimed at scenarios with infinite data, where the physical laws derived from human understanding of nature would become unnecessary. However, in the current era where data is not infinite, integrating physical equations into data-driven approaches provides a useful transition and balancing point. This integration involves using previously calculated results for operator learning to pre-train the system, then providing a good initial solution for specific problems, and finally finetuning with physical equations. Most importantly, the combination of data and physical laws enables a selflearning algorithm that becomes faster with more accurate data. All past computed results are used to train operator learning, improving the accuracy of operator learning and thus reducing the iterations needed for finetuning by physical equations. Therefore, AI for PDEs possesses a self-updating iterative capability, promising a significant and forward-looking direction in computational mechanics.

AI for PDEs represents the future of computational mechanics. In the past, the emergence of computers brought about computational mechanics. At present, artificial intelligence is actually the previous computer, so artificial intelligence will have a new manifestation in computational mechanics, that is, AI for PDEs.

###### Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

###### Acknowledgement

The study was supported by the Key Project of the National Natural Science Foundation of China (12332005) and scholarship from Bauhaus University in Weimar. Thank Zhongkai Hao for the helpful discussion.

###### Author Contributions Statement

Yizheng Wang wrote the methodology, theoretical research, and the application of AI4PDEs to solid mechanics. Jinshuai Bai wrote the application of AI4PDEs to fluid mechanics. Zhongya Lin wrote the application of AI4PDEs to biomechanics. Qimin Wang applied the permissions of pictures and drew some pictures. Cosmin Anitescu reviewed the paper. Mohammad Sadegh Eshaghi reviewed the paper. Yuantong Gu supervised the project. Xiqiao Feng supervised the project. Xiaoying Zhuang supervised the project. Timon Rabczuk reviewed the paper and supervised the project. Yinghua Liu supervised the project.

###### References

- [1] X. Zhang, L. Wang, J. Helwig, Y. Luo, C. Fu, Y. Xie, M. Liu, Y. Lin, Z. Xu, K. Yan, et al., Artificial intelligence for science in quantum, atomistic, and continuum systems, arXiv preprint arXiv:2307.08423

(2023).

- [2] M. Raissi, P. Perdikaris, G. E. Karniadakis, Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations, Journal of Computational Physics 378 (2019) 686–707.
- [3] G. E. Karniadakis, I. G. Kevrekidis, L. Lu, P. Perdikaris, S. Wang, L. Yang, Physics-informed machine learning, Nature Reviews Physics 3 (6) (2021) 422–440. doi:10.1038/s42254-021-00314-5.
- [4] H. Wang, T. Fu, Y. Du, W. Gao, K. Huang, Z. Liu, P. Chandak, S. Liu, P. Van Katwyk, A. Deac, et al., Scientific discovery in the age of artificial intelligence, Nature 620 (7972) (2023) 47–60.
- [5] K. Bi, L. Xie, H. Zhang, X. Chen, X. Gu, Q. Tian, Accurate medium-range global weather forecasting with 3d neural networks, Nature (2023) 1–6.
- [6] Y. Wang, Z. Hao, M. S. Eshaghi, C. Anitescu, X. Zhuang, T. Rabczuk, Y. Liu, Pretrain finite element method: A pretraining and warm-start framework for pdes via physics-informed neural operators, arXiv preprint arXiv:2601.03086 (2026).
- [7] S. Cuomo, V. S. Di Cola, F. Giampaolo, G. Rozza, M. Raissi, F. Piccialli, Scientific machine learning through physics–informed neural networks: Where we are and what next, Journal of Scientific Computing 92 (3) (2022) 88.
- [8] X. Li, Z. Liu, S. Cui, C. Luo, C. Li, Z. Zhuang, Predicting the effective mechanical property of heterogeneous materials by image based modeling and deep learning, Computer Methods in Applied Mechanics and Engineering 347 (2019) 735–753.
- [9] S. Wang, Y. Teng, P. J. S. J. o. S. C. Perdikaris, Understanding and mitigating gradient flow pathologies in physics-informed neural networks, SIAM Journal on Scientific Computing 43 (5) (2021) A3055–A3081.
- [10] R. Mattey, S. Ghosh, A novel sequential method to train physics informed neural networks for allen cahn and cahn hilliard equations, Computer Methods in Applied Mechanics and Engineering 390 (2022) 114474.
- [11] J. Han, A. Jentzen, E. Weinan, Solving high-dimensional partial differential equations using deep learning, Proceedings of the National Academy of Sciences 115 (34) (2018) 8505–8510.
- [12] E. Kharazmi, Z. Zhang, G. E. Karniadakis, hp-vpinns: Variational physics-informed neural networks with domain decomposition, Computer Methods in Applied Mechanics and Engineering 374 (2021) 113547.
- [13] L. Lu, X. Meng, S. Cai, Z. Mao, S. Goswami, Z. Zhang, G. E. Karniadakis, A comprehensive and fair comparison of two neural operators (with practical extensions) based on fair data, Computer Methods in Applied Mechanics and Engineering 393 (2022) 114778.


- [14] H. Yu, S. Park, A. Bayen, S. Moura, M. Krstic, Reinforcement learning versus pde backstepping and pi control for congested freeway traffic, IEEE Transactions on Control Systems Technology 30 (4) (2021) 1595–1611.
- [15] J.-H. Bastek, W. Sun, D. M. Kochmann, Physics-informed diffusion models, arXiv preprint arXiv:2403.14404 (2024).
- [16] Q. Jiang, Z. Gao, G. E. Karniadakis, Deepseek vs. chatgpt vs. claude: A comparative study for scientific computing and scientific machine learning tasks, Theoretical and Applied Mechanics Letters 15 (3) (2025) 100583.
- [17] Y. Wang, X. Li, Z. Yan, S. Ma, J. Bai, B. Liu, T. Rabczuk, Y. Liu, A pretraining-finetuning computational framework for material homogenization, International Journal of Mechanical Sciences 314 (2026) 111388.
- [18] H. Lee, I. S. Kang, Neural algorithm for solving differential equations, Journal of Computational Physics 91 (1) (1990) 110–131.
- [19] M. Dissanayake, N. Phan-Thien, Neural-network-based approximations for solving partial differential equations, communications in Numerical Methods in Engineering 10 (3) (1994) 195–201.
- [20] I. E. Lagaris, A. Likas, D. I. Fotiadis, Artificial neural networks for solving ordinary and partial differential equations, IEEE transactions on neural networks 9 (5) (1998) 987–1000.
- [21] L. D. McClenny, U. M. Braga-Neto, Self-adaptive physics-informed neural networks, Journal of Computational Physics 474 (2023) 111722.
- [22] Z. Wang, Z. Zhang, A mesh-free method for interface problems using the deep learning approach, Journal of Computational Physics 400 (2020) 108963. doi:10.1016/j.jcp.2019.108963.
- [23] B. Yu, et al., The deep ritz method: a deep learning-based numerical algorithm for solving variational problems, Communications in Mathematics and Statistics 6 (1) (2018) 1–12.
- [24] E. Haghighat, M. Raissi, A. Moure, H. Gomez, R. Juanes, A physics-informed deep learning framework for inversion and surrogate modeling in solid mechanics, Computer Methods in Applied Mechanics and Engineering 379 (2021) 113741. doi:10.1016/j.cma.2021.113741.
- [25] D. W. Abueidda, Q. Lu, S. Koric, Meshless physics-informed deep learning method for three-dimensional solid mechanics, International Journal for Numerical Methods in Engineering 122 (23) (2021) 7182–7201.
- [26] L. Yang, D. Zhang, G. E. Karniadakis, Physics-informed generative adversarial networks for stochastic differential equations, SIAM Journal on Scientific Computing 42 (1) (2020) A292–A317.
- [27] D. Zhang, L. Lu, L. Guo, G. E. Karniadakis, Quantifying total uncertainty in physics-informed neural networks for solving forward and inverse stochastic problems, Journal of Computational Physics 397 (2019) 108850.
- [28] L. Yuan, Y.-Q. Ni, X.-Y. Deng, S. Hao, A-pinn: Auxiliary physics informed neural networks for forward and inverse problems of nonlinear integro-differential equations, Journal of Computational Physics 462

(2022) 111260.

- [29] Y. Wang, J. Sun, W. Li, Z. Lu, Y. Liu, Cenn: Conservative energy method based on neural networks with subdomains for solving variational problems involving heterogeneous and complex geometries, Computer Methods in Applied Mechanics and Engineering 400 (2022) 115491.
- [30] Y. Wang, J. Sun, T. Rabczuk, Y. Liu, Dcem: A deep complementary energy method for solid mechanics, International Journal for Numerical Methods in Engineering (2024). doi:10.1002/nme.7585.


- [31] E. Samaniego, C. Anitescu, S. Goswami, V. M. Nguyen-Thanh, H. Guo, K. Hamdia, X. Zhuang, T. Rabczuk, An energy approach to the solution of partial differential equations in computational mechanics via machine learning: Concepts, implementation and applications, Computer Methods in Applied Mechanics and Engineering 362 (2020) 112790.
- [32] L. Lu, P. Jin, G. Pang, Z. Zhang, G. E. Karniadakis, Learning nonlinear operators via deeponet based on the universal approximation theorem of operators, Nature Machine Intelligence 3 (3) (2021) 218–229. doi:10.1038/s42256-021-00302-5.
- [33] Z. Li, N. Kovachki, K. Azizzadenesheli, B. Liu, K. Bhattacharya, A. Stuart, A. Anandkumar, Fourier neural operator for parametric partial differential equations, arXiv preprint arXiv:2010.08895 (2020).
- [34] N. B. Kovachki, Z. Li, B. Liu, K. Azizzadenesheli, K. Bhattacharya, A. M. Stuart, A. Anandkumar, Neural operator: Learning maps between function spaces with applications to pdes., J. Mach. Learn. Res. 24 (89)

(2023) 1–97.

- [35] Z. Li, H. Zheng, N. Kovachki, D. Jin, H. Chen, B. Liu, K. Azizzadenesheli, A. Anandkumar, Physicsinformed neural operator for learning partial differential equations, ACM/JMS Journal of Data Science 1 (3) (2024) 1–27.
- [36] S. Chakraborty, Transfer learning based multi-fidelity physics informed deep neural network, Journal of Computational Physics 426 (2021) 109942.
- [37] T. Chen, H. Chen, Universal approximation to nonlinear operators by neural networks with arbitrary activation functions and its application to dynamical systems, IEEE Transactions on Neural Networks 6 (4) (1995) 911–917.
- [38] F. Bartolucci, E. de Bézenac, B. Raonic, R. Molinaro, S. Mishra, R. Alaifari, Representation equivalent neural operators: a framework for alias-free operator learning, Advances in Neural Information Processing Systems 36 (2024).
- [39] A. Kahana, E. Zhang, S. Goswami, G. Karniadakis, R. Ranade, J. Pathak, On the geometry transferability of the hybrid iterative numerical solver for differential equations, Computational Mechanics 72 (3) (2023) 471–484.
- [40] L. Lu, P. Jin, G. E. Karniadakis, Deeponet: Learning nonlinear operators for identifying differential equations based on the universal approximation theorem of operators, arXiv preprint arXiv:1910.03193

(2019).

- [41] Z. Hao, Z. Wang, H. Su, C. Ying, Y. Dong, S. Liu, Z. Cheng, J. Song, J. Zhu, Gnot: A general neural operator transformer for operator learning, in: International conference on machine learning, PMLR, 2023, pp. 12556–12569.
- [42] S. Wang, H. Wang, P. Perdikaris, Learning the solution operator of parametric partial differential equations with physics-informed deeponets, Science advances 7 (40) (2021) eabi8605.
- [43] M. S. Eshaghi, C. Anitescu, N. Valizadeh, Y. Wang, X. Zhuang, T. Rabczuk, Nows: Neural operator warm starts for accelerating iterative solvers, arXiv preprint arXiv:2511.02481 (2025).
- [44] H. Wu, H. Luo, H. Wang, J. Wang, M. Long, Transolver: A fast transformer solver for pdes on general geometries, arXiv preprint arXiv:2402.02366 (2024).
- [45] T. J. Hughes, J. A. Cottrell, Y. Bazilevs, Isogeometric analysis: Cad, finite elements, nurbs, exact geometry and mesh refinement, Computer methods in applied mechanics and engineering 194 (39-41) (2005) 4135– 4195.


- [46] M. S. Eshaghi, C. Anitescu, M. Thombre, Y. Wang, X. Zhuang, T. Rabczuk, Variational physics-informed neural operator (vino) for solving partial differential equations, Computer Methods in Applied Mechanics and Engineering 437 (2025) 117785.
- [47] S. Goswami, M. Yin, Y. Yu, G. E. Karniadakis, A physics-informed variational deeponet for predicting crack path in quasi-brittle materials, Computer Methods in Applied Mechanics and Engineering 391 (2022) 114587.
- [48] K. Hao, Ai has cracked a key mathematical puzzle for understanding our world, MIT Technology Review 15 (2020) 2021.
- [49] J. Deng, W. Dong, R. Socher, L.-J. Li, K. Li, L. Fei-Fei, Imagenet: A large-scale hierarchical image database, in: 2009 IEEE conference on computer vision and pattern recognition, Ieee, 2009, pp. 248–255.
- [50] O. C. Zienkiewicz, R. L. Taylor, J. Z. Zhu, The finite element method: its basis and fundamentals, Elsevier, 2005.
- [51] T. J. Hughes, The finite element method: linear static and dynamic finite element analysis, Courier Corporation, 2012.
- [52] K.-J. Bathe, Finite element procedures, Klaus-Jurgen Bathe, 2006.
- [53] J. N. Reddy, Introduction to the finite element method, McGraw-Hill Education, 2019.
- [54] X. Zhang, Z. Chen, Y. Liu, The material point method: a continuum-based particle method for extreme loading cases, Academic Press, 2016.
- [55] G.-R. Liu, D. Karamanlidis, Mesh free methods: moving beyond the finite element method, Appl. Mech. Rev. 56 (2) (2003) B17–B18.
- [56] T. Rabczuk, T. Belytschko, Cracking particles: a simplified meshfree method for arbitrary evolving cracks, International journal for numerical methods in engineering 61 (13) (2004) 2316–2343.
- [57] T. Rabczuk, T. Belytschko, A three-dimensional large deformation meshfree method for arbitrary evolving cracks, Computer methods in applied mechanics and engineering 196 (29-30) (2007) 2777–2799.
- [58] T. Rabczuk, J.-H. Song, X. Zhuang, C. Anitescu, Extended finite element and meshfree methods, Academic Press, 2019.
- [59] V. P. Nguyen, T. Rabczuk, S. Bordas, M. Duflot, Meshless methods: a review and computer implementation aspects, Mathematics and computers in simulation 79 (3) (2008) 763–813.
- [60] R. J. LeVeque, Finite difference methods for ordinary and partial differential equations: steady-state and time-dependent problems, SIAM, 2007.
- [61] M. Darwish, F. Moukalled, The finite volume method in computational fluid dynamics: an advanced introduction with OpenFOAM® and Matlab®, Springer, 2016.
- [62] C. A. Brebbia, J. C. F. Telles, L. C. Wrobel, Boundary element techniques: theory and applications in engineering, Springer Science & Business Media, 2012.
- [63] G. Karniadakis, S. J. Sherwin, Spectral/hp element methods for computational fluid dynamics, Oxford University Press, USA, 2005.
- [64] S. Cai, Z. Mao, Z. Wang, M. Yin, G. E. Karniadakis, Physics-informed neural networks (pinns) for fluid mechanics: A review, Acta Mechanica Sinica 37 (12) (2021) 1727–1738.
- [65] H. Jasak, A. Jemcov, Z. Tukovic, et al., Openfoam: A c++ library for complex physics simulations, in: International workshop on coupled methods in numerical dynamics, Vol. 1000, 2007, pp. 1–20.


- [66] J. Berg, K. Nyström, A unified deep artificial neural network approach to partial differential equations in complex geometries, Neurocomputing 317 (2018) 28–41.
- [67] T. Trinh, T. Luong, Alphageometry: An olympiad-level ai system for geometry (2024). URL https://deepmind.google/discover/blog/alphageometry-an-olympiad-level-ai-system-f or-geometry/
- [68] G. Cybenko, Approximation by superpositions of a sigmoidal function, Mathematics of control, signals and systems 2 (4) (1989) 303–314.
- [69] K. Hornik, M. Stinchcombe, H. White, Multilayer feedforward networks are universal approximators, Neural networks 2 (5) (1989) 359–366.
- [70] L. Lu, X. Meng, Z. Mao, G. E. Karniadakis, Deepxde: A deep learning library for solving differential equations, SIAM Review 63 (1) (2021) 208–228. doi:10.1137/19m1274067.
- [71] J. Bai, H. Jeong, C. Batuwatta-Gamage, S. Xiao, Q. Wang, C. Rathnayaka, L. Alzubaidi, G. R. Liu, Y. Gu, An introduction to programming physics-informed neural network-based computational solid mechanics, International Journal of Computational Methods (2023).
- [72] H. Xu, Y. Chen, D. Zhang, Worth of prior knowledge for enhancing deep learning, Nexus (2024).
- [73] F. Lauer, G. Bloch, Incorporating prior knowledge in support vector machines for classification: A review, Neurocomputing 71 (7-9) (2008) 1578–1594.
- [74] J. Sirignano, K. Spiliopoulos, Dgm: A deep learning algorithm for solving partial differential equations, Journal of computational physics 375 (2018) 1339–1364.
- [75] E. Kharazmi, Z. Zhang, G. E. Karniadakis, Variational physics-informed neural networks for solving partial differential equations, arXiv preprint arXiv:1912.00873 (2019).
- [76] V. Dwivedi, B. Srinivasan, Physics informed extreme learning machine (pielm)–a rapid method for the numerical solution of partial differential equations, Neurocomputing 391 (2020) 96–118.
- [77] G.-B. Huang, Q.-Y. Zhu, C.-K. Siew, Extreme learning machine: theory and applications, Neurocomputing 70 (1-3) (2006) 489–501.
- [78] A. D. Jagtap, E. Kharazmi, G. E. Karniadakis, Conservative physics-informed neural networks on discrete domains for conservation laws: Applications to forward and inverse problems, Computer Methods in Applied Mechanics and Engineering 365 (2020) 113028.
- [79] A. D. Jagtap, G. E. Karniadakis, Extended physics-informed neural networks (xpinns): A generalized space-time domain decomposition based deep learning framework for nonlinear partial differential equations, Communications in Computational Physics 28 (5) (2020) 2002–2041.
- [80] H. Gao, L. Sun, J.-X. Wang, Phygeonet: Physics-informed geometry-adaptive convolutional neural networks for solving parameterized steady-state pdes on irregular domain, Journal of Computational Physics 428 (2021) 110079.
- [81] H. Gao, M. J. Zahr, J.-X. Wang, Physics-informed graph neural galerkin networks: A unified framework for solving pde-governed forward and inverse problems, Computer Methods in Applied Mechanics and Engineering 390 (2022) 114502.
- [82] A. A. Ramabathiran, P. Ramachandran, Spinn: sparse, physics-based, and partially interpretable neural networks for pdes, Journal of Computational Physics 445 (2021) 110600.


- [83] J. Sun, Y. Liu, Y. Wang, Z. Yao, X. Zheng, Binn: A deep learning approach for computational mechanics problems based on boundary integral equations, Computer Methods in Applied Mechanics and Engineering 410 (2023) 116012.
- [84] Y. Wang, J. Sun, J. Bai, C. Anitescu, M. S. Eshaghi, X. Zhuang, T. Rabczuk, Y. Liu, Kolmogorov– arnold-informed neural network: A physics-informed deep learning framework for solving forward and inverse problems based on kolmogorov–arnold networks, Computer Methods in Applied Mechanics and Engineering 433 (2025) 117518.
- [85] Z. Liu, Y. Wang, S. Vaidya, F. Ruehle, J. Halverson, M. Soljačić, T. Y. Hou, M. Tegmark, Kan: Kolmogorov-arnold networks, arXiv preprint arXiv:2404.19756 (2024).
- [86] L. Lu, R. Pestourie, W. Yao, Z. Wang, F. Verdugo, S. G. Johnson, Physics-informed neural networks with hard constraints for inverse design, SIAM Journal on Scientific Computing 43 (6) (2021) B1105–B1132.
- [87] M. R. Hestenes, Multiplier and gradient methods, Journal of optimization theory and applications 4 (5)

(1969) 303–320.

- [88] D. He, S. Li, W. Shi, X. Gao, J. Zhang, J. Bian, L. Wang, T.-Y. Liu, Learning physics-informed neural networks without stacked back-propagation, in: International Conference on Artificial Intelligence and Statistics, PMLR, 2023, pp. 3034–3047.
- [89] Z. Fang, A high-efficient hybrid physics-informed neural networks based on convolutional neural network, IEEE Transactions on Neural Networks and Learning Systems 33 (10) (2021) 5514–5526.
- [90] K. Shukla, A. D. Jagtap, G. E. Karniadakis, Parallel physics-informed neural networks via domain decomposition, Journal of Computational Physics 447 (2021) 110683. doi:10.1016/j.jcp.2021.110683.
- [91] T. Pfaff, M. Fortunato, A. Sanchez-Gonzalez, P. Battaglia, Learning mesh-based simulation with graph networks, in: International conference on learning representations, 2020.
- [92] J. Bai, G.-R. Liu, A. Gupta, L. Alzubaidi, X.-Q. Feng, Y. Gu, Physics-informed radial basis network (pirbn): A local approximating neural network for solving nonlinear partial differential equations, Computer Methods in Applied Mechanics and Engineering 415 (2023) 116290.
- [93] S. Wang, H. Wang, P. Perdikaris, On the eigenvector bias of fourier feature networks: From regression to solving multi-scale pdes with physics-informed neural networks, Computer Methods in Applied Mechanics and Engineering 384 (2021) 113938. doi:10.1016/j.cma.2021.113938.
- [94] J. Bai, Y. Zhou, Y. Ma, H. Jeong, H. Zhan, C. Rathnayaka, E. Sauret, Y. Gu, A general neural particle method for hydrodynamics modeling, Computer Methods in Applied Mechanics and Engineering 393

(2022) 114740.

- [95] X. Meng, Z. Li, D. Zhang, G. E. Karniadakis, Ppinn: Parareal physics-informed neural network for time-dependent pdes, Computer Methods in Applied Mechanics and Engineering 370 (2020) 113250.
- [96] X. Meng, G. E. Karniadakis, A composite neural network that learns from multi-fidelity data: Application to function approximation and inverse pde problems, Journal of Computational Physics 401 (2020) 109020.
- [97] E. Haghighat, R. Juanes, Sciann: A keras/tensorflow wrapper for scientific computations and physicsinformed deep learning using artificial neural networks, Computer Methods in Applied Mechanics and Engineering 373 (2021) 113552.
- [98] K. Zubov, Z. McCarthy, Y. Ma, F. Calisto, V. Pagliarino, S. Azeglio, L. Bottero, E. Luján, V. Sulzer, A. Bharambe, et al., Neuralpde: Automating physics-informed neural networks (pinns) with error approximations, arXiv preprint arXiv:2107.09443 (2021).


- [99] O. Hennigh, S. Narasimhan, M. A. Nabian, A. Subramaniam, K. Tangsali, Z. Fang, M. Rietmann, W. Byeon, S. Choudhry, Nvidia simnet: An ai-accelerated multi-physics simulation framework, in: International conference on computational science, Springer, 2021, pp. 447–461.
- [100] C. Rao, H. Sun, Y. Liu, Physics-informed deep learning for computational elastodynamics without labeled data, Journal of Engineering Mechanics 147 (8) (2021) 04021043.
- [101] T. Sahin, M. von Danwitz, A. Popp, Solving forward and inverse problems of contact mechanics using physics-informed neural networks, Advanced Modeling and Simulation in Engineering Sciences 11 (1)

(2024) 11.

- [102] L. Sun, H. Gao, S. Pan, J.-X. Wang, Surrogate modeling for fluid flows based on physics-constrained deep learning without simulation data, Computer Methods in Applied Mechanics and Engineering 361 (2020) 112732.
- [103] S. Wang, P. Perdikaris, Deep learning of free boundary and stefan problems, Journal of Computational Physics 428 (2021) 109914.
- [104] C. Rao, H. Sun, Y. Liu, Physics-informed deep learning for incompressible laminar flows, Theoretical and Applied Mechanics Letters 10 (3) (2020) 207–212.
- [105] S. Cai, H. Li, F. Zheng, F. Kong, M. Dao, G. E. Karniadakis, S. Suresh, Artificial intelligence velocimetry and microaneurysm-on-a-chip for three-dimensional analysis of blood flow in physiology and disease, Proceedings of the National Academy of Sciences 118 (13) (2021) e2100697118.
- [106] X. Zhuang, H. Guo, N. Alajlan, H. Zhu, T. Rabczuk, Deep autoencoder based energy method for the bending, vibration, and buckling analysis of kirchhoff plates with transfer learning, European Journal of Mechanics-A/Solids 87 (2021) 104225.
- [107] W. Li, M. Z. Bazant, J. Zhu, A physics-guided neural network framework for elastic plates: Comparison of governing equations-based and energy-based approaches, Computer Methods in Applied Mechanics and Engineering 383 (2021) 113933. doi:10.1016/j.cma.2021.113933.
- [108] S. Goswami, C. Anitescu, T. Rabczuk, Adaptive fourth-order phase field analysis using deep energy minimization, Theoretical and Applied Fracture Mechanics 107 (2020) 102527.
- [109] S. Goswami, C. Anitescu, S. Chakraborty, T. Rabczuk, Transfer learning enhanced physics informed neural network for phase-field modeling of fracture, Theoretical and Applied Fracture Mechanics 106

(2020) 102447.

- [110] V. M. Nguyen-Thanh, X. Zhuang, T. Rabczuk, A deep energy method for finite deformation hyperelasticity, European Journal of Mechanics-A/Solids 80 (2020) 103874.
- [111] J. Bai, G.-R. Liu, T. Rabczuk, Y. Wang, X.-Q. Feng, Y. Gu, A robust radial point interpolation method empowered with neural network solvers (rpim-nns) for nonlinear solid mechanics, Computer Methods in Applied Mechanics and Engineering 429 (2024) 117159.
- [112] J. He, D. Abueidda, R. A. Al-Rub, S. Koric, I. Jasiuk, A deep learning energy-based method for classical elastoplasticity, International Journal of Plasticity (2023) 103531.
- [113] V. M. Nguyen-Thanh, C. Anitescu, N. Alajlan, T. Rabczuk, X. Zhuang, Parametric deep energy approach for elasticity accounting for strain gradient effects, Computer Methods in Applied Mechanics and Engineering 386 (2021) 114096. doi:10.1016/j.cma.2021.114096.
- [114] J. He, C. Chadha, S. Kushwaha, S. Koric, D. Abueidda, I. Jasiuk, Deep energy method in topology optimization applications, Acta Mechanica 234 (4) (2023) 1365–1379.


- [115] S. Buoso, T. Joyce, S. Kozerke, Personalising left-ventricular biophysical models of the heart using parametric physics-informed neural networks, Medical Image Analysis 71 (2021) 102066.
- [116] D. Dalton, D. Husmeier, H. Gao, Physics-informed graph neural network emulation of soft-tissue mechanics, Computer Methods in Applied Mechanics and Engineering 417 (2023) 116351.
- [117] M. Zhu, H. Zhang, A. Jiao, G. E. Karniadakis, L. Lu, Reliable extrapolation of deep neural operators informed by physics or sparse observations, Computer Methods in Applied Mechanics and Engineering 412 (2023) 116064.
- [118] J. He, S. Koric, S. Kushwaha, J. Park, D. Abueidda, I. Jasiuk, Novel deeponet architecture to predict stresses in elastoplastic structures with variable complex geometries and loads, Computer Methods in Applied Mechanics and Engineering 415 (2023) 116277.
- [119] M. S. Eshaghi, M. Bamdad, C. Anitescu, Y. Wang, X. Zhuang, T. Rabczuk, Applications of scientific machine learning for the analysis of functionally graded porous beams, Neurocomputing 619 (2025) 129119.
- [120] G. Wen, Z. Li, K. Azizzadenesheli, A. Anandkumar, S. M. Benson, U-fno—an enhanced fourier neural operator-based deep-learning model for multiphase flow, Advances in Water Resources 163 (2022) 104180.
- [121] Z. Li, D. Z. Huang, B. Liu, A. Anandkumar, Fourier neural operator with learned deformations for pdes on general geometries, Journal of Machine Learning Research 24 (388) (2023) 1–26.
- [122] Z. Lin, J. Bai, S. Li, X. Chen, B. Li, X.-Q. Feng, A physics-informed neural network framework for simulating creep buckling in growing viscoelastic biological tissues, Computer Methods in Applied Mechanics and Engineering 452 (2026) 118715.
- [123] Y. Wang, Y. Lin, S. Goswami, L. Zhao, H. Zhang, J. Bai, C. Anitescu, M. S. Eshaghi, X. Zhuang, T. Rabczuk, et al., Towards unified ai-driven fracture mechanics: The extended deep energy method (xdem), arXiv preprint arXiv:2511.05888 (2025).
- [124] S. Li, W. K. Liu, Meshfree and particle methods and their applications, Appl. Mech. Rev. 55 (1) (2002) 1–34.
- [125] H. Sheng, C. Yang, Pfnn: A penalty-free neural network method for solving a class of second-order boundary-value problems on complex geometries, Journal of Computational Physics 428 (2021) 110085.
- [126] J. N. Fuhg, N. Bouklas, The mixed deep energy method for resolving concentration features in finite strain hyperelasticity, Journal of Computational Physics 451 (2022) 110839.
- [127] J. He, D. Abueidda, S. Koric, I. Jasiuk, On the use of graph neural networks and shape-function-based gradient computation in the deep energy method, International Journal for Numerical Methods in Engineering 124 (4) (2023) 864–879.
- [128] L. Yang, Z. Zhang, Y. Song, S. Hong, R. Xu, Y. Zhao, W. Zhang, B. Cui, M.-H. Yang, Diffusion models: A comprehensive survey of methods and applications, ACM Computing Surveys (2022).
- [129] Z. Li, N. Kovachki, K. Azizzadenesheli, B. Liu, K. Bhattacharya, A. Stuart, A. Anandkumar, Neural operator: Graph kernel network for partial differential equations, arXiv preprint arXiv:2003.03485 (2020).
- [130] T. De Ryck, S. Mishra, Generic bounds on the approximation error for physics-informed (and) operator learning, Advances in Neural Information Processing Systems 35 (2022) 10945–10958.
- [131] N. Kovachki, S. Lanthaler, S. Mishra, On universal approximation and error bounds for fourier neural operators, The Journal of Machine Learning Research 22 (1) (2021) 13237–13312.
- [132] K. He, X. Zhang, S. Ren, J. Sun, Deep residual learning for image recognition, in: Proceedings of the IEEE conference on computer vision and pattern recognition, 2016, pp. 770–778.


- [133] M. Duprez, V. Lleras, A. Lozinski, V. Vigon, K. Vuillemot, φ-fem-fno: a new approach to train a neural operator as a fast pde solver for variable geometries, Communications in Nonlinear Science and Numerical Simulation (2025) 109131.
- [134] E. Burman, S. Claus, P. Hansbo, M. G. Larson, A. Massing, Cutfem: discretizing geometry and partial differential equations, International Journal for Numerical Methods in Engineering 104 (7) (2015) 472–501.
- [135] I. J. Goodfellow, M. Mirza, D. Xiao, A. Courville, Y. Bengio, An empirical investigation of catastrophic forgetting in gradient-based neural networks, arXiv preprint arXiv:1312.6211 (2013).
- [136] C. Lu, C. Lu, R. T. Lange, J. Foerster, J. Clune, D. Ha, The ai scientist: Towards fully automated open-ended scientific discovery, arXiv preprint arXiv:2408.06292 (2024).
- [137] Y. Wang, C. Anitescu, M. S. Eshaghi, X. Zhuang, T. Rabczuk, Y. Liu, Deep energy method with large language model assistance: an open-source streamlit-based platform for solving variational pdes, arXiv preprint arXiv:2602.07838 (2026).
- [138] A. D. Jagtap, K. Kawaguchi, G. E. Karniadakis, Adaptive activation functions accelerate convergence in deep and physics-informed neural networks, Journal of Computational Physics 404 (2020) 109136. doi:10.1016/j.jcp.2019.109136.
- [139] A. D. Jagtap, K. Kawaguchi, G. Em Karniadakis, Locally adaptive activation functions with slope recovery for deep and physics-informed neural networks, Proceedings of the Royal Society A: Mathematical, Physical and Engineering Sciences 476 (2239) (2020) 20200334. doi:10.1098/rspa.2020.0334.
- [140] A. Pinkus, Approximation theory of the mlp model in neural networks, Acta numerica 8 (1999) 143–195.
- [141] K. Hornik, Approximation capabilities of multilayer feedforward networks, Neural networks 4 (2) (1991) 251–257.
- [142] I. Goodfellow, Y. Bengio, A. Courville, Deep learning, MIT press, 2016.
- [143] N. Cohen, O. Sharir, A. Shashua, On the expressive power of deep learning: A tensor analysis, in: Conference on learning theory, PMLR, 2016, pp. 698–728.
- [144] Y. Shin, J. Darbon, G. E. Karniadakis, On the convergence of physics informed neural networks for linear second-order elliptic and parabolic type pdes, arXiv preprint arXiv:2004.01806 (2020).
- [145] S. Mishra, R. Molinaro, Estimates on the generalization error of physics-informed neural networks for approximating a class of inverse problems for pdes, IMA Journal of Numerical Analysis 42 (2) (2022) 981–1022.
- [146] A. F. Psaros, X. Meng, Z. Zou, L. Guo, G. E. Karniadakis, Uncertainty quantification in scientific machine learning: Methods, metrics, and comparisons, Journal of Computational Physics 477 (2023) 111902.
- [147] S. Lanthaler, S. Mishra, G. E. Karniadakis, Error estimates for deeponets: A deep learning framework in infinite dimensions, Transactions of Mathematics and Its Applications 6 (1) (2022) tnac001.
- [148] S. Wang, X. Yu, P. Perdikaris, When and why pinns fail to train: A neural tangent kernel perspective, Journal of Computational Physics 449 (2022) 110768.
- [149] D. Liu, Y. Wang, A dual-dimer method for training physics-constrained neural networks with minimax architecture, Neural Networks 136 (2021) 112–125.
- [150] C. Xu, B. T. Cao, Y. Yuan, G. Meschke, Transfer learning based physics-informed neural networks for solving inverse problems in engineering structures under different loading scenarios, Computer Methods in Applied Mechanics and Engineering 405 (2023) 115852.


- [151] A. Jacot, F. Gabriel, C. Hongler, Neural tangent kernel: Convergence and generalization in neural networks, Advances in neural information processing systems 31 (2018).
- [152] A. Kendall, Y. Gal, R. Cipolla, Multi-task learning using uncertainty to weigh losses for scene geometry and semantics, in: Proceedings of the IEEE conference on computer vision and pattern recognition, 2018, pp. 7482–7491.
- [153] I. E. Lagaris, A. C. Likas, D. G. Papageorgiou, Neural-network methods for boundary value problems with irregular boundaries, IEEE Transactions on Neural Networks 11 (5) (2000) 1041–1049.
- [154] K. S. McFall, An artificial neural network method for solving boundary value problems with arbitrary irregular boundaries, Georgia Institute of Technology, 2006.
- [155] K. S. McFall, J. R. Mahan, Artificial neural network method for solution of boundary value problems with exact satisfaction of arbitrary boundary conditions, IEEE Transactions on Neural Networks 20 (8) (2009) 1221–1233.
- [156] N. Sukumar, A. Srivastava, Exact imposition of boundary conditions with distance functions in physicsinformed deep neural networks, Computer Methods in Applied Mechanics and Engineering 389 (2022) 114333.
- [157] E. J. Hu, Y. Shen, P. Wallis, Z. Allen-Zhu, Y. Li, S. Wang, L. Wang, W. Chen, et al., Lora: Low-rank adaptation of large language models., Iclr 1 (2) (2022) 3.
- [158] Y. Wang, J. Bai, M. S. Eshaghi, C. Anitescu, X. Zhuang, T. Rabczuk, Y. Liu, Transfer learning in physics-informed neurals networks: full fine-tuning, lightweight fine-tuning, and low-rank adaptation, International Journal of Mechanical System Dynamics 5 (2) (2025) 212–235.
- [159] A. G. Baydin, B. A. Pearlmutter, A. A. Radul, J. M. Siskind, Automatic differentiation in machine learning: a survey, Journal of Marchine Learning Research 18 (2018) 1–43.
- [160] A. K. Noor, C. Andersen, Computerized symbolic manipulation in structural mechanics—progress and potential, Computers & Structures 10 (1-2) (1979) 95–118.
- [161] H. Guo, X. Zhuang, T. Rabczuk, A deep collocation method for the bending analysis of kirchhoff plate, arXiv preprint arXiv:2102.02617 (2021).
- [162] J. Bai, T. Rabczuk, A. Gupta, L. Alzubaidi, Y. Gu, A physics-informed neural network technique based on a modified loss function for computational 2d and 3d solid mechanics, Computational Mechanics 71 (3)

(2023) 543–562.

- [163] J. C. Simo, T. J. Hughes, Computational inelasticity, Vol. 7, Springer Science & Business Media, 2006.
- [164] X. Zhou, D. Lu, Y. Zhang, X. Du, T. Rabczuk, An open-source unconstrained stress updating algorithm for the modified cam-clay model, Computer Methods in Applied Mechanics and Engineering 390 (2022) 114356.
- [165] D. W. Abueidda, S. Koric, R. A. Al-Rub, C. M. Parrott, K. A. James, N. A. Sobh, A deep learning energy method for hyperelasticity and viscoelasticity, European Journal of Mechanics-A/Solids 95 (2022) 104639.
- [166] L. Zhao, Q. Shao, Denns: Discontinuity-embedded neural networks for fracture mechanics, Computer Methods in Applied Mechanics and Engineering 446 (2025) 118184.
- [167] Z. Chen, Y. Dai, Y. Liu, Crack propagation simulation and overload fatigue life prediction via enhanced physics-informed neural networks, International Journal of Fatigue 186 (2024) 108382.


- [168] E. Kiyani, M. Manav, N. Kadivar, L. De Lorenzis, G. E. Karniadakis, Predicting crack nucleation and propagation in brittle materials using deep operator networks with diverse trunk architectures, Computer Methods in Applied Mechanics and Engineering 441 (2025) 117984.
- [169] B. Zheng, T. Li, H. Qi, L. Gao, X. Liu, L. Yuan, Physics-informed machine learning model for computational fracture of quasi-brittle materials without labelled data, International Journal of Mechanical Sciences 223 (2022) 107282.
- [170] M. Manav, R. Molinaro, S. Mishra, L. De Lorenzis, Phase-field modeling of fracture with physics-informed deep learning, Computer Methods in Applied Mechanics and Engineering 429 (2024) 117104.
- [171] F. Erdogan, G. Sih, On the crack extension in plates under plane loading and transverse shear, Journal of basic engineering 85 (4) (1963) 519–525.
- [172] M. Hussain, S. Pu, J. Underwood1, Strain energy release rate e for a crack under combined mode i and mode ii, in: Fracture analysis: Proceedings of the 1973 national symposium on fracture mechanics, part II, Vol. 560, ASTM International, 1974, p. 2.
- [173] G. C. Sih, Strain-energy-density factor applied to mixed mode crack problems, International Journal of fracture 10 (3) (1974) 305–321.
- [174] B. Bourdin, G. A. Francfort, J.-J. Marigo, Numerical experiments in revisited brittle fracture, Journal of the Mechanics and Physics of Solids 48 (4) (2000) 797–826.
- [175] G. A. Francfort, J.-J. Marigo, Revisiting brittle fracture as an energy minimization problem, Journal of the Mechanics and Physics of Solids 46 (8) (1998) 1319–1342.
- [176] C. Miehe, M. Hofacker, F. Welschinger, A phase field model for rate-independent crack propagation: Robust algorithmic implementation based on operator splits, Computer Methods in Applied Mechanics and Engineering 199 (45-48) (2010) 2765–2778.
- [177] H. Amor, J.-J. Marigo, C. Maurini, Regularized formulation of the variational brittle fracture with unilateral contact: Numerical experiments, Journal of the Mechanics and Physics of Solids 57 (8) (2009) 1209–1229.
- [178] T. Gerasimov, L. De Lorenzis, On penalization in variational phase-field models of brittle fracture, Computer Methods in Applied Mechanics and Engineering 354 (2019) 990–1026.
- [179] X. Jin, S. Cai, H. Li, G. E. Karniadakis, Nsfnets (navier-stokes flow nets): Physics-informed neural networks for the incompressible navier-stokes equations, Journal of Computational Physics 426 (2021) 109951.
- [180] R. Zhang, P. Hu, Q. Meng, Y. Wang, R. Zhu, B. Chen, Z.-M. Ma, T.-Y. Liu, Drvn (deep random vortex network): A new physics-informed machine learning method for simulating and inferring incompressible fluid flows, Physics of Fluids 34 (10) (2022).
- [181] A. J. Majda, A. L. Bertozzi, A. Ogawa, Vorticity and incompressible flow. cambridge texts in applied mathematics, Appl. Mech. Rev. 55 (4) (2002) B77–B78.
- [182] E.-Z. Rui, G.-Z. Zeng, Y.-Q. Ni, Z.-W. Chen, S. Hao, Time-averaged flow field reconstruction based on a multifidelity model using physics-informed neural network (pinn) and nonlinear information fusion, International Journal of Numerical Methods for Heat & Fluid Flow 34 (1) (2024) 131–149.
- [183] T.-s. Wang, G. Xi, Z.-g. Sun, Z. Huang, The prediction of external flow field and hydrodynamic force with limited data using deep neural network, Journal of Hydrodynamics 35 (3) (2023) 549–570.
- [184] S. Hochreiter, J. Schmidhuber, Long short-term memory, Neural computation 9 (8) (1997) 1735–1780.


- [185] J. Han, L. Xue, Y. Jia, M. S. Mwasamwasa, F. Nanguka, C. Sangweni, H. Liu, Q. Li, Prediction of porous media fluid flow with spatial heterogeneity using criss-cross physics-informed convolutional neural networks, CMES-Computer Modeling in Engineering & Sciences 138 (2) (2024) 1323–1340.
- [186] Z. Huang, X. Wang, L. Huang, C. Huang, Y. Wei, W. Liu, Ccnet: Criss-cross attention for semantic segmentation, in: Proceedings of the IEEE/CVF international conference on computer vision, 2019, pp. 603–612.
- [187] C. Cheng, G.-T. Zhang, Deep learning method based on physics informed neural network with resnet block for solving fluid flow problems, Water 13 (4) (2021) 423.
- [188] S. G. Rosofsky, E. Huerta, Magnetohydrodynamics with physics informed neural operators, Machine Learning: Science and Technology 4 (3) (2023) 035002.
- [189] H. Li, M. Shatarah, Operator learning for urban water clarification hydrodynamics and particulate matter transport with physics-informed neural networks, Water Research 251 (2024) 121123.
- [190] Z. Mao, A. D. Jagtap, G. E. Karniadakis, Physics-informed neural networks for high-speed flows, Computer Methods in Applied Mechanics and Engineering 360 (2020) 112789.
- [191] J.-Z. Peng, Z.-Q. Wang, X. Rong, M. Mei, M. Wang, Y. He, W.-T. Wu, Rapid and sparse reconstruction of high-speed steady-state and transient compressible flow fields using physics-informed graph neural networks, Physics of Fluids 36 (4) (2024).
- [192] X. Ren, P. Hu, H. Su, F. Zhang, H. Yu, Physics-informed neural networks for transonic flow around a cylinder with high reynolds number, Physics of Fluids 36 (3) (2024).
- [193] L. Li, Y. Li, Q. Du, T. Liu, Y. Xie, Ref-nets: Physics-informed neural network for reynolds equation of gas bearing, Computer Methods in Applied Mechanics and Engineering 391 (2022) 114524.
- [194] A. Joshi, A. Papados, R. Kumar, Investigation of low and high-speed fluid dynamics problems using physics-informed neural network, International Journal of Computational Fluid Dynamics 37 (2) (2023) 149–166.
- [195] S. Auddy, R. Dey, N. J. Turner, S. Basu, Grinn: a physics-informed neural network for solving hydrodynamic systems in the presence of self-gravity, Machine Learning: Science and Technology 5 (2) (2024) 025014.
- [196] D. Jalili, S. Jang, M. Jadidi, G. Giustini, A. Keshmiri, Y. Mahmoudi, Physics-informed neural networks for heat transfer prediction in two-phase flows, International Journal of Heat and Mass Transfer 221 (2024) 125089.
- [197] C. W. Hirt, B. D. Nichols, Volume of fluid (vof) method for the dynamics of free boundaries, Journal of computational physics 39 (1) (1981) 201–225.
- [198] H. Wessels, C. Weißenfels, P. Wriggers, The neural particle method–an updated lagrangian physics informed neural network for computational fluid dynamics, Computer Methods in Applied Mechanics and Engineering 368 (2020) 113127.
- [199] K. Shao, Y. Wu, S. Jia, An improved neural particle method for complex free surface flow simulation using physics-informed neural networks, Mathematics 11 (8) (2023) 1805.
- [200] D. Kirkpatrick, R. Seidel, On the shape of a set of points in the plane, IEEE Transactions on Information Theory 29 (4) (1983) 551–559.
- [201] Y. H. Huang, Z. Xu, C. Qian, L. Liu, Solving free-surface problems for non-shallow water using boundary and initial conditions-free physics-informed neural network (bif-pinn), Journal of Computational Physics 479 (2023) 112003.


- [202] W. Diab, O. Chaabi, S. Alkobaisi, A. Awotunde, M. Al Kobaisi, Learning generic solutions for multiphase transport in porous media via the flux functions operator, Advances in Water Resources 183 (2024) 104609.
- [203] T.-Y. Hsieh, T.-H. Huang, A multiscale stabilized physics informed neural networks with weakly imposed boundary conditions transfer learning method for modeling advection dominated flow, Engineering with Computers (2024) 1–35.
- [204] S. Jin, Z. Ma, K. Wu, Asymptotic-preserving neural networks for multiscale time-dependent linear transport equations, Journal of Scientific Computing 94 (3) (2023) 57.
- [205] C. Lin, Z. Li, L. Lu, S. Cai, M. Maxey, G. E. Karniadakis, Operator learning for predicting multiscale bubble growth dynamics, The Journal of Chemical Physics 154 (10) (2021).
- [206] C. Lin, M. Maxey, Z. Li, G. E. Karniadakis, A seamless multiscale operator neural network for inferring bubble dynamics, Journal of Fluid Mechanics 929 (2021) A18.
- [207] S. Cai, Z. Wang, L. Lu, T. A. Zaki, G. E. Karniadakis, Deepm&mnet: Inferring the electroconvection multiphysics fields based on operator approximation by neural networks, Journal of Computational Physics 436 (2021) 110296.
- [208] Z. Mao, L. Lu, O. Marxen, T. A. Zaki, G. E. Karniadakis, Deepm&mnet for hypersonics: Predicting the coupled flow and finite-rate chemistry behind a normal shock using neural-network approximation of operators, Journal of computational physics 447 (2021) 110698.
- [209] K. Wu, X.-B. Yan, S. Jin, Z. Ma, Capturing the diffusive behavior of the multiscale linear transport equations by asymptotic-preserving convolutional deeponets, Computer Methods in Applied Mechanics and Engineering 418 (2024) 116531.
- [210] S. E. Ahmed, P. Stinis, A multifidelity deep operator network approach to closure for multiscale systems, Computer Methods in Applied Mechanics and Engineering 414 (2023) 116161.
- [211] M. Liu, L. Liang, W. Sun, A generic physics-informed neural network-based constitutive model for soft biological tissues, Computer methods in applied mechanics and engineering 372 (2020) 113402.
- [212] K. Linka, N. Reiter, J. Würges, M. Schicht, L. Bräuer, C. J. Cyron, F. Paulsen, S. Budday, Unraveling the local relation between tissue composition and human brain mechanics through machine learning, Frontiers in bioengineering and biotechnology 9 (2021) 704738.
- [213] R. Qiu, R. Huang, Y. Xiao, J. Wang, Z. Zhang, J. Yue, Z. Zeng, Y. Wang, Physics-informed neural networks for phase-field method in two-phase flow, Physics of Fluids 34 (5) (2022).
- [214] L. J. Lim, G. H. Tison, F. N. Delling, Artificial intelligence in cardiovascular imaging, Methodist DeBakey Cardiovascular Journal 16 (2) (2020) 138.
- [215] P. Moser, W. Fenz, S. Thumfart, I. Ganitzer, M. Giretzlehner, Modeling of 3d blood flows with physicsinformed neural networks: comparison of network architectures, Fluids 8 (2) (2023) 46.
- [216] Y. Liu, L. Cai, Y. Chen, P. Ma, Q. Zhong, Variable separated physics-informed neural networks based on adaptive weighted loss functions for blood flow model, Computers & Mathematics with Applications 153

(2024) 108–122.

- [217] C.-T. Chen, G. X. Gu, Learning hidden elasticity with deep neural networks, Proceedings of the National Academy of Sciences 118 (31) (2021) e2102721118.
- [218] S. L. Brunton, J. L. Proctor, J. N. Kutz, Discovering governing equations from data by sparse identification of nonlinear dynamical systems, Proceedings of the national academy of sciences 113 (15) (2016) 3932– 3937.


- [219] B. Liu, Y. Wang, T. Rabczuk, T. Olofsson, W. Lu, Multi-scale modeling in thermal conductivity of polyurethane incorporated with phase change materials using physics-informed neural networks, Renewable Energy 220 (2024) 119565.
- [220] L. Li, C. Chen, Equilibrium-based convolution neural networks for constitutive modeling of hyperelastic materials, Journal of the Mechanics and Physics of Solids 164 (2022) 104931.
- [221] M. Flaschel, S. Kumar, L. De Lorenzis, Unsupervised discovery of interpretable hyperelastic constitutive laws, Computer Methods in Applied Mechanics and Engineering 381 (2021) 113852.
- [222] P. Thakolkaran, A. Joshi, Y. Zheng, M. Flaschel, L. De Lorenzis, S. Kumar, Nn-euclid: Deep-learning hyperelasticity without stress data, Journal of the Mechanics and Physics of Solids 169 (2022) 105076.
- [223] E. Livingston, S. Srivastava, J. Holber, H. M. Mourad, K. Garikipati, Inference of phase field fracture models, Journal of the Mechanics and Physics of Solids (2025) 106495.
- [224] M. P. Bendsøe, O. Sigmund, Material interpolation schemes in topology optimization, Archive of applied mechanics 69 (9) (1999) 635–654.
- [225] J. Zehnder, Y. Li, S. Coros, B. Thomaszewski, Ntopo: Mesh-free topology optimization using implicit neural representations, Advances in Neural Information Processing Systems 34 (2021) 10368–10381.
- [226] H. Jeong, C. Batuwatta-Gamage, J. Bai, Y. M. Xie, C. Rathnayaka, Y. Zhou, Y. Gu, A complete physicsinformed neural network-based framework for structural topology optimization, Computer Methods in Applied Mechanics and Engineering 417 (2023) 116401.
- [227] H. Jeong, J. Bai, C. P. Batuwatta-Gamage, C. Rathnayaka, Y. Zhou, Y. Gu, A physics-informed neural network-based topology optimization (pinnto) framework for structural optimization, Engineering Structures 278 (2023) 115484.
- [228] E. Zhang, M. Dao, G. E. Karniadakis, S. Suresh, Analyses of internal structures and defects in materials using physics-informed neural networks, Science advances 8 (7) (2022) eabk0644.
- [229] J. Sun, Y. Liu, Z. Yao, X. Zheng, A data-driven multi-flaw detection strategy based on deep learning and boundary element method, Computational Mechanics 71 (3) (2023) 517–542.
- [230] M. Raissi, A. Yazdani, G. E. Karniadakis, Hidden fluid mechanics: Learning velocity and pressure fields from flow visualizations, Science 367 (6481) (2020) 1026–1030.
- [231] S. Cai, Z. Wang, F. Fuest, Y. J. Jeon, C. Gray, G. E. Karniadakis, Flow over an espresso cup: inferring 3-d velocity and pressure fields from tomographic background oriented schlieren via physics-informed neural networks, Journal of Fluid Mechanics 915 (2021) A102.
- [232] K. A. Boster, S. Cai, A. Ladrón-de Guevara, J. Sun, X. Zheng, T. Du, J. H. Thomas, M. Nedergaard, G. E. Karniadakis, D. H. Kelley, Artificial intelligence velocimetry reveals in vivo flow rates, pressure gradients, and shear stresses in murine perivascular flows, Proceedings of the National Academy of Sciences 120 (14)

(2023) e2217744120.

- [233] M. Mahmoudabadbozchelou, G. E. Karniadakis, S. Jamali, nn-pinns: Non-newtonian physics-informed neural networks for complex fluid modeling, Soft Matter 18 (1) (2022) 172–185.
- [234] M. Schierholz, Y. Hassab, C. Schuster, Engineering-informed design space reduction for pcb based power delivery networks, IEEE Transactions on Components, Packaging and Manufacturing Technology (2023).
- [235] Y. Du, M. Wang, T. A. Zaki, State estimation in minimal turbulent channel flow: A comparative study of 4dvar and pinn, International Journal of Heat and Fluid Flow 99 (2023) 109073.


- [236] H. Zhang, H. Wang, Z. Xu, Z. Liu, B. C. Khoo, A physics-informed neural network-based approach to reconstruct the tornado vortices from limited observed data, Journal of Wind Engineering and Industrial Aerodynamics 241 (2023) 105534.
- [237] P. I. Renn, C. Wang, S. Lale, Z. Li, A. Anandkumar, M. Gharib, Forecasting subcritical cylinder wakes with fourier neural operators, arXiv preprint arXiv:2301.08290 (2023).
- [238] S. G. Rosofsky, H. Al Majed, E. Huerta, Applications of physics informed neural operators, Machine Learning: Science and Technology 4 (2) (2023) 025022.
- [239] L. Lu, R. Pestourie, S. G. Johnson, G. Romano, Multifidelity deep neural operators for efficient learning of partial differential equations with application to fast inverse design of nanoscale heat transport, Physical Review Research 4 (2) (2022) 023210.
- [240] Z. Li, W. Peng, Z. Yuan, J. Wang, Fourier neural operator approach to large eddy simulation of threedimensional turbulence, Theoretical and Applied Mechanics Letters 12 (6) (2022) 100389.
- [241] J. Yu, L. Lu, X. Meng, G. E. Karniadakis, Gradient-enhanced physics-informed neural networks for forward and inverse pde problems, Computer Methods in Applied Mechanics and Engineering 393 (2022) 114823.
- [242] Q. Lou, X. Meng, G. E. Karniadakis, Physics-informed neural networks for solving forward and inverse flow problems via the boltzmann-bgk formulation, Journal of Computational Physics 447 (2021) 110676.
- [243] C. Kou, Y. Yin, Y. Zeng, S. Jia, Y. Luo, X. Yuan, Physics-informed neural network integrate with unclosed mechanism model for turbulent mass transfer, Chemical Engineering Science 288 (2024) 119752.
- [244] A. Arzani, J.-X. Wang, R. M. D’Souza, Uncovering near-wall blood flow from sparse data with physicsinformed neural networks, Physics of Fluids 33 (7) (2021).
- [245] G. Kissas, Y. Yang, E. Hwuang, W. R. Witschey, J. A. Detre, P. Perdikaris, Machine learning in cardiovascular flows modeling: Predicting arterial blood pressure from non-invasive 4d flow mri data using physics-informed neural networks, Computer Methods in Applied Mechanics and Engineering 358 (2020) 112623.
- [246] M. F. Fathi, I. Perez-Raya, A. Baghaie, P. Berg, G. Janiga, A. Arzani, R. M. D’Souza, Super-resolution and denoising of 4d-flow mri using physics-informed deep neural nets, Computer Methods and Programs in Biomedicine 197 (2020) 105729.
- [247] A. Kamali, M. Sarabian, K. Laksari, Elasticity imaging using physics-informed neural networks: Spatial discovery of elastic modulus and poisson’s ratio, Acta biomaterialia 155 (2023) 400–409.
- [248] E. Zhang, M. Yin, G. E. Karniadakis, Physics-informed neural networks for nonhomogeneous material identification in elasticity imaging, arXiv preprint arXiv:2009.04525 (2020).
- [249] C. Herrero Martin, A. Oved, R. A. Chowdhury, E. Ullmann, N. S. Peters, A. A. Bharath, M. Varela, Ep-pinns: Cardiac electrophysiology characterisation using physics-informed neural networks, Frontiers in Cardiovascular Medicine 8 (2022) 768419.
- [250] M. Sarabian, H. Babaee, K. Laksari, Physics-informed neural networks for brain hemodynamic predictions using medical imaging, IEEE transactions on medical imaging 41 (9) (2022) 2285–2303.
- [251] C. Wu, Y. Xu, J. Fang, Q. Li, Machine learning in biomaterials, biomechanics/mechanobiology, and biofabrication: State of the art and perspective, Archives of Computational Methods in Engineering


(2024) 1–67.

- [252] AlphaProof, A. teams, Ai achieves silver-medal standard solving international mathematical olympiad problems (2024). URL https://deepmind.google/discover/blog/ai-solves-imo-problems-at-silver-medal-level /
- [253] N. McGreivy, A. Hakim, Weak baselines and reporting biases lead to overoptimism in machine learning for fluid-related partial differential equations, Nature machine intelligence 6 (10) (2024) 1256–1269.


