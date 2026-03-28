# arXiv:2201.05624v4[cs.LG]7 Jun 2022

## Scientiﬁc Machine Learning through Physics-Informed Neural Networks: Where we are and What’s next

##### Salvatore Cuomo1, Vincenzo Schiano Di Cola2*, Fabio Giampaolo1, Gianluigi Rozza2, Maziar Raissi3 and Francesco Piccialli1*

1*Department of Mathematics and Applications ”R. Caccioppoli”, University of Naples Federico II, Napoli, 80126, Italy . 2*Department of Electrical Engineering and Information Technology, University of Naples Federico II, Via Claudio, Napoli, 80125, Italy . 2SISSA – International School for Advanced Studies, Street, City, 10587, Italy. 3Department of Applied Mathematics, University of Colorado Boulder, Street, Boulder, 610101, United States.

*Corresponding author(s). E-mail(s): vincenzo.schianodicola@unina.it; francesco.piccialli@unina.it; Contributing authors: salvatore.cuomo@unina.it; fabio.giampaolo@unina.it; grozza@sissa.it; mara4513@colorado.edu;

Abstract Physics-Informed Neural Networks (PINN) are neural networks (NNs) that encode model equations, like Partial Diﬀerential Equations (PDE), as a component of the neural network itself. PINNs are nowadays used to solve PDEs, fractional equations, integral-diﬀerential equations, and stochastic PDEs. This novel methodology has arisen as a multi-task learning framework in which a NN must ﬁt observed data while reducing a PDE residual. This article provides a comprehensive review of the literature on PINNs: while the primary goal of the study was to

1

characterize these networks and their related advantages and disadvantages. The review also attempts to incorporate publications on a broader range of collocation-based physics informed neural networks, which stars form the vanilla PINN, as well as many other variants, such as physics-constrained neural networks (PCNN), variational hpVPINN, and conservative PINN (CPINN). The study indicates that most research has focused on customizing the PINN through diﬀerent activation functions, gradient optimization techniques, neural network structures, and loss function structures. Despite the wide range of applications for which PINNs have been used, by demonstrating their ability to be more feasible in some contexts than classical numerical techniques like Finite Element Method (FEM), advancements are still possible, most notably theoretical issues that remain unresolved.

Keywords: Physics-Informed Neural Networks, Scientiﬁc Machine Learning, Deep Neural Networks, Nonlinear equations, Numerical methods, Partial Diﬀerential Equations, Uncertainty

### 1 Introduction

Deep neural networks have succeeded in tasks such as computer vision, natural language processing, and game theory. Deep Learning (DL) has transformed how categorization, pattern recognition, and regression tasks are performed across various application domains.

Deep neural networks are increasingly being used to tackle classical applied mathematics problems such as partial diﬀerential equations (PDEs) utilizing machine learning and artiﬁcial intelligence approaches. Due to, for example, signiﬁcant nonlinearities, convection dominance, or shocks, some PDEs are notoriously diﬃcult to solve using standard numerical approaches. Deep learning has recently emerged as a new paradigm of scientiﬁc computing thanks to neural networks’ universal approximation and great expressivity. Recent studies have shown deep learning to be a promising method for building metamodels for fast predictions of dynamic systems. In particular, NNs have proven to represent the underlying nonlinear input-output relationship in complex systems. Unfortunately, dealing with such high dimensional-complex systems are not exempt from the curse of dimensionality, which Bellman ﬁrst described in the context of optimal control problems (Bellman, 1966). However, machine learning-based algorithms are promising for solving PDEs (Blechschmidt and Ernst, 2021).

Indeed, Blechschmidt and Ernst (2021) consider machine learning-based PDE solution approaches will continue to be an important study subject in the next years as deep learning develops in methodological, theoretical, and algorithmic developments. Simple neural network models, such as MLPs with few hidden layers, were used in early work for solving diﬀerential equations (Lagaris

et al, 1998). Modern methods, based on NN techniques, take advantage of optimization frameworks and auto-diﬀerentiation, like Berg and Nystr¨m (2018) that suggested a uniﬁed deep neural network technique for estimating PDE solutions. Furthermore, it is envisioned that DNN will be able to create an interpretable hybrid Earth system model based on neural networks for Earth and climate sciences (Irrgang et al, 2021).

Nowadays, the literature does not have a clear nomenclature for integrating previous knowledge of a physical phenomenon with deep learning. ‘Physicsinformed,’ ‘physics-based,’ ‘physics-guided,’ and ‘theory-guided’ are often some used terms. Kim et al (2021b) developed the overall taxonomy of what they called informed deep learning, followed by a literature review in the ﬁeld of dynamical systems. Their taxonomy is organized into three conceptual stages: (i) what kind of deep neural network is used, (ii) how physical knowledge is represented, and (iii) how physical information is integrated. Inspired by their work, we will investigate PINNs, a 2017 framework, and demonstrate how neural network features are used, how physical information is supplied, and what physical problems have been solved in the literature.

#### 1.1 What the PINNs are

Physics-Informed Neural Networks (PINNs) are a scientiﬁc machine learning technique used to solve problems involving Partial Diﬀerential Equations (PDEs). PINNs approximate PDE solutions by training a neural network to minimize a loss function; it includes terms reﬂecting the initial and boundary conditions along the space-time domain’s boundary and the PDE residual at selected points in the domain (called collocation point). PINNs are deeplearning networks that, given an input point in the integration domain, produce an estimated solution in that point of a diﬀerential equation after training. Incorporating a residual network that encodes the governing physics equations is a signiﬁcant novelty with PINNs. The basic concept behind PINN training is that it can be thought of as an unsupervised strategy that does not require labelled data, such as results from prior simulations or experiments. The PINN algorithm is essentially a mesh-free technique that ﬁnds PDE solutions by converting the problem of directly solving the governing equations into a loss function optimization problem. It works by integrating the mathematical model into the network and reinforcing the loss function with a residual term from the governing equation, which acts as a penalizing term to restrict the space of acceptable solutions.

PINNs take into account the underlying PDE, i.e. the physics of the problem, rather than attempting to deduce the solution based solely on data, i.e. by ﬁtting a neural network to a set of state-value pairs. The idea of creating physics-informed learning machines that employ systematically structured prior knowledge about the solution can be traced back to earlier research by Owhadi (2015), which revealed the promising technique of leveraging such prior knowledge. Raissi et al (2017a,b) used Gaussian process regression to construct representations of linear operator functionals, accurately inferring the solution

and providing uncertainty estimates for a variety of physical problems; this was then extended in (Raissi and Karniadakis, 2018; Raissi et al, 2018). PINNs were introduced in 2017 as a new class of data-driven solvers in a two-part article (Raissi et al, 2017c,d) published in a merged version afterwards in 2019 (Raissi

- et al, 2019). Raissi et al (2019) introduce and illustrate the PINN approach for solving nonlinear PDEs, like Schr¨dinger, Burgers, and Allen-Cahn equations. They created physics-informed neural networks (PINNs) which can handle both forward problems of estimating the solutions of governing mathematical models and inverse problems, where the model parameters are learnt from observable data.


The concept of incorporating prior knowledge into a machine learning algorithm is not entirely novel. In fact Dissanayake and Phan-Thien (1994) can be considered one of the ﬁrst PINNs. This paper followed the results of the universal approximation achievements of the late 1980s, (Hornik et al, 1989); then in the early 90s several methodologies were proposed to use neural networks to approximate PDEs, like the work on constrained neural networks (Psichogios and Ungar, 1992; Lagaris et al, 1998) or (Lee and Kang, 1990). In particular Dissanayake and Phan-Thien (1994) employed a simple neural networks to approximate a PDE, where the neural network’s output was a single value that was designed to approximate the solution value at the speciﬁed input position. The network had two hidden layers, with 3, 5 or 10 nodes for each layer. The network loss function approximated the L2 error of the approximation on the interior and boundary of the domain using point-collocation. While, the loss is evaluated using a quasi-Newtonian approach and the gradients are evaluated using ﬁnite diﬀerence. In Lagaris et al (1998), the solution of a diﬀerential equation is expressed as a constant term and an adjustable term with unknown parameters, the best parameter values are determined via a neural network. However, their method only works for problems with regular borders. Lagaris et al (2000) extends the method to problems with irregular borders.

As computing power increased during the 2000s, increasingly sophisticated models with more parameters and numerous layers became the standard Ozbay¨ et al (2021). Diﬀerent deep model using MLP, were introduced, also using Radial Basis Function Kumar and Yadav (2011).

Research into the use of NNs to solve PDEs continued to gain traction in the late 2010s, thanks to advancements in the hardware used to run NN training, the discovery of better practices for training NNs, and the availability of opensource packages, such as Tensorﬂow (Haghighat and Juanes, 2021), and the availability of Automatic diﬀerentiation in such packages (Paszke et al, 2017).

Finally, more recent advancements by Kondor and Trivedi (2018), and Mallat (2016), brought to Raissi et al (2019) solution that extended previous notions while also introducing fundamentally new approaches, such as a discrete time-stepping scheme that eﬃciently leverages the predictive ability of neural networks (Kollmannsberger et al, 2021). The fact that the framework

could be utilized directly by plugging it into any diﬀerential problem simpliﬁed the learning curve for beginning to use such, and it was the ﬁrst step for many researchers who wanted to solve their problems with a Neural network approach (Markidis, 2021). The success of the PINNs can be seen from the rate at which Raissi et al (2019) is cited, and the exponentially growing number of citations in the recent years (Figure 1).

However, PINN is not the only NN framework utilized to solve PDEs. Various frameworks have been proposed in recent years, and, while not exhaustive, we have attempted to highlight the most relevant ones in this paragraph.

The Deep Ritz method (DRM) (E and Yu, 2018), where the loss is deﬁned as the energy of the problem’s solution.

Then there approaches based on the Galerkin method, or Petrov–Galerkin method, where the loss is given by multiplying the residual by a test function, and when is the volumetric residual we have a Deep Galerkin Method (DGM) (Sirignano and Spiliopoulos, 2018). Whereas, when a Galerkin approach is used on collocation points the framework is a variant of PINNs, i.e. a hp-VPINN Kharazmi et al (2021b).

Within the a collocation based approach, i.e. PINN methodology (Raissi

- et al, 2019; Yang and Perdikaris, 2019; Meng et al, 2020), many other variants were proposed, as the variational hp-VPINN, as well as conservative PINN (CPINN)(Jagtap et al, 2020b). Another approach is physics-constrained neural networks (PCNNs) (Zhu et al, 2019; Sun et al, 2020a; Liu and Wang, 2021). while PINNs incorporate both the PDE and its initial/boundary conditions (soft BC) in the training loss function, PCNNs, are “data-free” NNs, i.e. they enforce the initial/boundary conditions (hard BC) via a custom NN architecture while embedding the PDE in the training loss. This soft form technique is described in Raissi et al (2019), where the term “physics-informed neural networks” was coined (PINNs).


Because there are more articles on PINN than any other speciﬁc variant, such as PCNN, hp-VPINN, CPINN, and so on, this review will primarily focus on PINN, with some discussion of the various variants that have emerged, that is, NN architectures that solve diﬀerential equations based on collocation points.

Finally, the acronym PINN will be written in its singular form rather than its plural form in this review, as it is considered representative of a family of neural networks of the same type.

Various review papers involving PINN have been published. About the potentials, limitations and applications for forward and inverse problems (Karniadakis et al, 2021) for three-dimensional ﬂows (Cai et al, 2021a), or a comparison with other ML techniques (Blechschmidt and Ernst, 2021). An introductory course on PINNs that covers the fundamentals of Machine Learning and Neural Networks can be found from Kollmannsberger et al (2021). PINN is also compared against other methods that can be applied to solve PDEs, like the one based on the Feynman–Kac theorem (Blechschmidt and

Ernst, 2021). Finally, PINNs have also been extended to solve integrodifferential equations (IDEs)(Pang et al, 2019; Yuan et al, 2022) or stochastic diﬀerential equations (SDEs) (Yang et al, 2020).

Being able to learn PDEs, PINNs have several advantages over conventional methods. PINNs, in particular, are mesh-free methods that enable on-demand solution computation after a training stage, and they allow solutions to be made diﬀerentiable using analytical gradients. Finally, they provide an easy way to solve forward jointly and inverse problems using the same optimization problem. In addition to solving diﬀerential equations (the forward problem), PINNs may be used to solve inverse problems such as characterizing ﬂuid ﬂows from sensor data. In fact, the same code used to solve forward problems can be used to solve inverse problems with minimal modiﬁcation. Indeed, PINNs can address PDEs in domains with very complicated geometries or in very high dimensions that are all diﬃcult to numerically simulate as well as inverse problems and constrained optimization problems.

#### 1.2 What is this review about

In this survey, we focus on how PINNs are used to address diﬀerent scientiﬁc computing problems, the building blocks of PINNs, the aspects related to learning theory, what toolsets are already available, future directions and recent trends, and issues regarding accuracy and convergence. According to diﬀerent problems, we show how PINNs solvers have been customized in literature by conﬁguring the depth, layer size, activation functions and using transfer learning.

This article can be considered as an extensive literature review on PINNs. It was mostly conducted by searching Scopus for the terms: ((physic* OR physical) W/2 (informed OR constrained) W/2 ‘‘neural network’’)

The primary research question was to determine what PINNs are and their associated beneﬁts and drawbacks. The research also focused on the outputs from the CRUNCH research group in the Division of Applied Mathematics at Brown University and then on the (Physics-Informed Learning Machines for Multiscale and Multiphysics Problems) PhILMs Center, which is a collaboration with the Paciﬁc Northwest National Laboratory. In such a frame, the primary authors who have been involved in this literature research are Karniadakis G.E., Perdikaris P., and Raissi M. Additionally, the review considered studies that addressed a broader topic than PINNs, namely physics-guided neural networks, as well as physics-informed machine learning and deep learning.

Figure 1 summarizes what the inﬂuence of PINN is in today’s literature and applications.

![image 1](Cuomo et al._2022_Scientific Machine Learning through Physics-Informed Neural Networks Where we are and What's next_images/imageFile1.png)

- Fig. 1: A number of papers related to PINNs (on the right) addressed problems on which PINNs are applied (on the left) by year. PINN is having a signiﬁcant impact in the literature and in scientiﬁc applications. The number of papers referencing Raissi or including PINN in their abstract title or keywords is increasing exponentially. The number of papers about PINN more than quintupled between 2019 and 2020, and there were twice as many new papers published in 2021 as there were in 2020. Since Raissi’s ﬁrst papers on arXiv in 2019 (Raissi et al, 2019), a boost in citations can be seen in late 2018 and 2019. On the left, we display a sample problem solved in that year by one of the articles, speciﬁcally a type of time-dependent equation. Some of the addressed problems to be solved in the ﬁrst vanilla PINN, for example, were the Allen–Cahn equation, the Korteweg–de Vries equation, or the 1D nonlinear Shro¨dinger problem (SE). By the end of 2019 Mao et al (2020) solved with the same PINN Euler equations (EE) that model high-speed aerodynamic ﬂows. By the end of 2020 Jin et al (2021) solved the incompressible Navier-Stokes equations (NSE). Finally, in 2021 Cai et al (2021c) coupled the Navier–Stokes equations with the corresponding temperature equation for analyzing heat ﬂow convection (NSE+HE).


### 2 The building blocks of a PINN

Physically-informed neural networks can address problems that are described by few data, or noisy experiment observations. Because they can use known data while adhering to any given physical law speciﬁed by general nonlinear partial diﬀerential equations, PINNs can also be considered neural networks that deal with supervised learning problems (Goswami et al, 2020). PINNs can

solve diﬀerential equations expressed, in the most general form, like: F(u(z); γ) = f(z) z in Ω, B(u(z)) = g(z) z in ∂Ω

(1)

deﬁned on the domain Ω ⊂ Rd with the boundary ∂Ω. Where z := [x1,...,xd−1; t] indicates the space-time coordinate vector, u represents the unknown solution, γ are the parameters related to the physics, f is the function identifying the data of the problem and F is the non linear diﬀerential operator. Finally, since the initial condition can actually be considered as a type of Dirichlet boundary condition on the spatio-temporal domain, it is possible to denote B as the operator indicating arbitrary initial or boundary conditions related to the problem and g the boundary function. Indeed, the boundary conditions can be Dirichlet, Neumann, Robin, or periodic boundary conditions.

Equation (1) can describe numerous physical systems including both forward and inverse problems. The goal of forward problems is to ﬁnd the function u for every z, where γ are speciﬁed parameters. In the case of the inverse problem, γ must also be determined from the data. The reader can ﬁnd an operator based mathematical formulation of equation (1) in the work of Mishra and Molinaro (2021a).

In the PINN methodology, u(z) is computationally predicted by a NN, parametrized by a set of parameters θ, giving rise to an approximation

uˆθ(z) ≈ u(z);

where (ˆ·)θ denotes a NN approximation realized with θ.

In this context, where forward and inverse problems are analyzed in the same framework, and given that PINN can adequately solve both problems, we will use θ to represent both the vector of all unknown parameters in the neural network that represents the surrogate model and unknown parameters γ in the case of an inverse problem.

In such a context, the NN must learn to approximate the diﬀerential equations through ﬁnding θ that deﬁne the NN by minimizing a loss function that depends on the diﬀerential equation LF, the boundary conditions LB, and eventually some known data Ldata, each of them adequately weighted:

θ∗ = arg min

(ωFLF(θ) + ωBLB(θ) + ωdLdata(θ)). (2)

θ

To summarize, PINN can be viewed as an unsupervised learning approach when they are trained solely using physical equations and boundary conditions for forward problems; however, for inverse problems or when some physical properties are derived from data that may be noisy, PINN can be considered supervised learning methodologies.

In the following paragraph, we will discuss the types of NN used to approximate u(z), how the information derived by F is incorporated in the model, and how the NN learns from the equations and additional given data.

Figure 2 summarizes all the PINN’s building blocks discussed in this section. PINN are composed of three components: a neural network, a physicsinformed network, and a feedback mechanism. The ﬁrst block is a NN, uˆθ, that accepts vector variables z from the equation (1) and outputs the ﬁled value u. The second block can be thought of PINN’s functional component, as it computes the derivative to determine the losses of equation terms, as well as the terms of the initial and boundary conditions of equation (2). Generally, the ﬁrst two blocks are linked using algorithmic diﬀerentiation, which is used to inject physical equations into the NN during the training phase. Thus, the feedback mechanism minimizes the loss according to some learning rate, in order to ﬁx the NN parameters vector θ of the NN uˆθ. In the following, it will be clear from the context to what network we are referring to, whether the NN or the functional network that derives the physical information.

![image 2](Cuomo et al._2022_Scientific Machine Learning through Physics-Informed Neural Networks Where we are and What's next_images/imageFile2.png)

- Fig. 2: Physics-informed neural networks building blocks. PINNs are made up of diﬀerential equation residual (loss) terms, as well as initial and boundary conditions. The network’s inputs (variables) are transformed into network outputs (the ﬁeld u). The network is deﬁned by θ. The second area is the physics informed network, which takes the output ﬁeld u and computes the derivative using the given equations. The boundary/initial condition is also evaluated (if it has not already been hard-encoded in the neural network), and also the labeled data observations are calculated (in case there is any data available). The ﬁnal step with all of these residuals is the feedback mechanism, that minimizes the loss, using an optimizer, according to some learning rate in order to obtain the NN parameters θ.


#### 2.1 Neural Network Architecture

The representational ability of neural networks is well established. According to the universal approximation theorem, any continuous function can be arbitrarily closely approximated by a multi-layer perceptron with only one hidden layer and a ﬁnite number of neurons (Hornik et al, 1989; Cybenko, 1989; Yarotsky, 2017; Berman et al, 2019). While neural networks can express very complex functions compactly, determining the precise parameters (weights and biases) required to solve a speciﬁc PDE can be diﬃcult (Waheed et al, 2021). Furthermore, identifying the appropriate artiﬁcial neural network (ANN) architecture can be challenging. There are two approaches: shallow learning networks, which have a single hidden layer and can still produce any non-linear continuous function, and deep neural networks (DNN), a type of ANN that uses more than two layers of neural networks to model complicated relationships (Aldweesh et al, 2020). Finally, the taxonomy of various Deep Learning architectures is still a matter of research (Muhammad et al, 2021; Aldweesh et al, 2020; Sengupta

- et al, 2020) The main architectures covered in the Deep Learning literature include fully


connected feed-forward networks (called FFNN, or also FNN, FCNN, or FFDNN), convolutional neural networks (CNNs), and recurrent neural networks (RNNs) (LeCun et al, 2015; Chen et al, 2018). Other more recent architectures encompass Auto-Encoder (AE), Deep Belief Network (DBN), Generative Adversarial Network (GAN), and Bayesian Deep Learning (BDL) (Alom et al, 2019; Berman et al, 2019).

Various PINN extensions have been investigated, based on some of these networks. An example is estimating the PINN solution’s uncertainty using Bayesian neural networks. Alternatively, when training CNNs and RNNs, ﬁnite-diﬀerence ﬁlters can be used to construct the diﬀerential equation residual in a PINN-like loss function. This section will illustrate all of these examples and more; ﬁrst, we will deﬁne the mathematical framework for characterizing the various networks.

According to Caterini and Chang (2018a) a generic deep neural network with L layers, can be represented as the composition of L functions fi(xi,θi) where xi are known as state variables, and θi denote the set of parameters for the i-th layer. So a function u(x) is approximated as

uθ(x) = fL ◦ fL−1 ... ◦ f1(x). (3)

where each fi is deﬁned on two inner product spaces Ei and Hi, being fi ∈ Ei×Hi and the layer composition, represented by ◦, is to be read as f2◦f1(x) = f2(f1(x)).

Since Raissi et al (2019) original vanilla PINN, the majority of solutions have used feed-forward neural networks. However, some researchers have experimented with diﬀerent types of neural networks to see how they aﬀect overall PINN performance, in particular with CNN, RNN, and GAN, and there seems there has been not yet a full investigation of other networks within the PINN

framework. In this subsection, we attempt to synthesize the mainstream solutions, utilizing feed-forward networks, and all of the other versions. Table 1 contains a synthesis reporting the kind of neural network and the paper that implemented it.

###### 2.1.1 Feed-forward neural network

A feed-forward neural network, also known as a multi-layer perceptron (MLP), is a collection of neurons organized in layers that perform calculations sequentially through the layers. Feed-forward networks, also known as multilayer perceptrons (MLP), are DNNs with several hidden layers that only move for-

- ward (no loopback). In a fully connected neural network, neurons in adjacent layers are connected, whereas neurons inside a single layer are not linked. Each neuron is a mathematical operation that applies an activation function to the weighted sum of it’s own inputs plus a bias factor (Waheed et al, 2021). Given an input x ∈ Ω an MLP transforms it to an output, through a layer of units (neurons) which compose of aﬃne-linear maps between units (in successive layers) and scalar non-linear activation functions within units, resulting in a composition of functions. So for MLP, it is possible to specify (3) as


fi(xi; Wi,bi) = αi(Wi · xi + bi)

equipping each Ei and Hi with the standard Euclidean inner product, i.e. E = H = R (Caterini and Chang, 2018b), and αi is a scalar (non-linear) activation function. The machine learning literature has studied several diﬀerent activation functions, which we shall discuss later in this section. Equation (3) can also be rewritten in conformity with the notation used in Mishra and Molinaro (2021a):

uθ(x) = CK ◦ α ◦ CK−1 ... ◦ α ◦ C1(x), (4) where for any 1 ≤ k ≤ K, it it is deﬁned

Ck(xk) = Wkxk + bk. (5)

Thus a neural network consists of an input layer, an output layer, and (K −2) hidden layers.

###### FFNN architectures

While the ideal DNN architecture is still an ongoing research; papers implementing PINN have attempted to empirically optimise the architecture’s characteristics, such as the number of layers and neurons in each layer. Smaller DNNs may be unable to eﬀectively approximate unknown functions, whereas too large DNNs may be diﬃcult to train, particularly with small datasets. Raissi et al (2019) used diﬀerent typologies of DNN, for each problem, like a

5-layer deep neural network with 100 neurons per layer, an DNN with 4 hidden layers and 200 neurons per layer or a 9 layers with 20 neuron each layer. Tartakovsky et al (2020) empirically determine the feedforward network size, in particular they use three hidden layers and 50 units per layer, all with an hyperbolic tangent activation function. Another example of how the diﬀerential problem aﬀects network architecture can be found in Kharazmi et al (2021b) for their hp-VPINN. The architecture is implemented with four layers and twenty neurons per layer, but for an advection equation with a double discontinuity of the exact solution, they use an eight-layered deep network. For a constrained approach, by utilizing a speciﬁc portion of the NN to satisfy the required boundary conditions, Zhu et al (2021) use ﬁve hidden layers and 250 neurons per layer to constitute the fully connected neural network. Bringing the number of layers higher, in PINNeik (Waheed et al, 2021), a DNN with ten hidden layers containing twenty neurons each is utilized, with a locally adaptive inverse tangent function as the activation function for all hidden layers except the ﬁnal layer, which has a linear activation function. He et al (2020) examines the eﬀect of neural network size on state estimation accuracy. They begin by experimenting with various hidden layer sizes ranging from three to ﬁve, while maintaining a value of 32 neurons per layer. Then they set the number of hidden layers to three, the activation function to hyperbolic tangent, while varying the number of neurons in each hidden layer. Other publications have attempted to understand how the number of layers, neurons, and activation functions eﬀect the NN’s approximation quality with respect to the problem to be solved, like (Blechschmidt and Ernst, 2021).

###### Multiple FFNN

Although many publications employ a single fully connected network, a rising number of research papers have been addressing PINN with multiple fully connected network blended together, e.g. to approximate speciﬁc equation of a larger mathematical model. An architecture composed of ﬁve the feed-forward neural network is proposed by Haghighat et al (2021b). In a two-phase Stefan problem, discussed later in this review and in Cai et al (2021c), a DNN is used to model the unknown interface between two diﬀerent material phases, while another DNN describes the two temperature distributions of the phases. Instead of a single NN across the entire domain, Moseley et al (2021) suggests using multiple neural networks, one for each subdomain. Finally, Lu et al (2021a) employed a pair of DNN, one for encoding the input space (branch net) and the other for encoding the domain of the output functions (trunk net). This architecture, known as DeepONet, is particularly generic because no requirements are made to the topology of the branch or trunk network, despite the fact that the two sub-networks have been implemented as FFNNs as in Lin et al (2021b).

###### Shallow networks

To overcome some diﬃculties, various researchers have also tried to investigate shallower network solutions: these can be sparse neural networks, instead of fully connected architectures, or more likely single hidden layers as ELM (Extreme Learning Machine) (Huang et al, 2011). When compared to the shallow architecture, more hidden layers aid in the modeling of complicated nonlinear relationships (Sengupta et al, 2020), however, using PINNs for real problems can result in deep networks with many layers associated with high training costs and eﬃciency issues. For this reason, not only deep neural networks have been employed for PINNs but also shallow ANN are reported in the literature. X-TFC, developed by Schiassi et al (2021), employs a single-layer NN trained using the ELM algorithm. While PIELM (Dwivedi and Srinivasan,

- 2020) is proposed as a faster alternative, using a hybrid neural network-based method that combines two ideas from PINN and ELM. ELM only updates the weights of the outer layer, leaving the weights of the inner layer unchanged. Finally, in Ramabathiran and Ramachandran (2021) a Sparse, Physics-based, and partially Interpretable Neural Networks (SPINN) is proposed. The authors suggest a sparse architecture, using kernel networks, that yields interpretable results while requiring fewer parameters than fully connected solutions. They consider various kernels such as Radial Basis Functions (RBF), softplus hat, or Gaussian kernels, and apply their proof of concept architecture to a variety of mathematical problems.


###### Activation function

The activation function has a signiﬁcant impact on DNN training performance. ReLU, Sigmoid, Tanh are commonly used activations (Sun et al, 2020a). Recent research has recommended training an adjustable activation function like Swish, which is deﬁned as x · Sigmoid(βx) and β is a trainable parameter, and where Sigmoid is supposed to be a general sigmoid curve, an S-shaped function, or in some cases a logistic function. Among the most used activation functions there are logistic sigmoid, hyperbolic tangent, ReLu, and leaky ReLu. Most authors tend to use the inﬁnitely diﬀerentiable hyperbolic tangent activation function α(x) = tanh(x) (He et al, 2020), whereas Cheng and Zhang (2021) use a Resnet block to improve the stability of the fully-connected neural network (FC-NN). They also prove that Swish activation function outperforms the others in terms of enhancing the neural network’s convergence rate and accuracy. Nonetheless, because of the second order derivative evaluation, it is pivotal to choose the activation function in a PINN framework with caution. For example, while rescaling the PDE to dimensionless form, it is preferable to choose a range of [0,1] rather than a wider domain, because most activation functions (such as Sigmoid, Tanh, Swish) are nonlinear near 0. Moreover the regularity of PINNs can be ensured by using smooth activation functions like as the sigmoid and hyperbolic tangent, allowing estimations of PINN generalization error to hold true (Mishra and Molinaro, 2021a).

###### 2.1.2 Convolutional neural networks

Convolutional neural networks (ConvNet or CNN) are intended to process data in the form of several arrays, for example a color image made of three 2D arrays. CNNs usually have a number of convolution and pooling layers. The convolution layer is made up of a collection of ﬁlters (or kernels) that convolve across the full input rather than general matrix multiplication. The pooling layer instead performs subsampling, reducing the dimensionality.

For CNNs, according to Caterini and Chang (2018b), the layerwise function f can be written as

fi(xi; Wi) = Φi(αi(Ci(Wi,xi)))

where α is an elementwise nonlinearity, Φ is the max-pooling map, and C the convolution operator.

It is worth noting that the convolution operation preserves translations and pooling is unaﬀected by minor data translations. This is applied to input image properties, such as corners, edges, and so on, that are translationally invariant, and will still be represented in the convolution layer’s output.

As a result, CNNs perform well with multidimensional data such as images and speech signals, in fact is in the domain of images that these networks have been used in a physic informed network framework.

For more on these topic the reader can look at LeCun et al (2015); Chen

- et al (2018); Muhammad et al (2021); Aldweesh et al (2020); Berman et al


- (2019); Calin (2020a)


###### CNN architectures

Because CNNs were originally created for image recognition, they are better suited to handling image-like data and may not be directly applicable to scientiﬁc computing problems, as most geometries are irregular with nonuniform grids; for example, Euclidean-distance-based convolution ﬁlters lose their invariance on non-uniform meshes.

A physics-informed geometry-adaptive convolutional neural network (PhyGeoNet) was introduced in Gao et al (2021). PhyGeoNet is a physics-informed CNN that uses coordinate transformation to convert solution ﬁelds from an irregular physical domain to a rectangular reference domain. Additionally, boundary conditions are strictly enforced making it a physics-constrained neural network.

Fang (2021) observes that a Laplacian operator has been discretized in a convolution operation employing a ﬁnite-diﬀerence stencil kernel. Indeed, a Laplacian operator can be discretized using the ﬁnite volume approach, and the discretization procedure is equivalent to convolution. As a result, he enhances PINN by using a ﬁnite volume numerical approach with a CNN structure. He devised and implemented a CNN-inspired technique in which, rather than using a Cartesian grid, he computes convolution on a mesh or graph. Furthermore, rather than zero padding, the padding data serve as the boundary

condition. Finally, Fang (2021) does not use pooling because the data does not require compression.

###### Convolutional encoder-decoder network

Autoencoders (AE) (or encoder–decoders) are commonly used to reduce dimensionality in a nonlinear way. It consists of two NN components: an encoder that translates the data from the input layer to a ﬁnite number of hidden units, and a decoder that has an output layer with the same number of nodes as the input layer (Chen et al, 2018).

For modeling stochastic ﬂuid ﬂows, Zhu et al (2019) developed a physicsconstrained convolutional encoder-decoder network and a generative model. Zhu et al (2019) propose a CNN-based technique for solving stochastic PDEs with high-dimensional spatially changing coeﬃcients, demonstrating that it outperforms FC-NN methods in terms of processing eﬃciency. AE architecture of the convolutional neural network (CNN) is also used in Wang et al (2021a). The authors propose a framework called a Theory-guided Auto-Encoder (TgAE) capable of incorporating physical constraints into the convolutional neural network.

Geneva and Zabaras (2020) propose a deep auto-regressive dense encoderdecoder and the physics-constrained training algorithm for predicting transient PDEs. They extend this model to a Bayesian framework to quantify both epistemic and aleatoric uncertainty. Finally, Grubiˇsic´ et al (2021) also used an encoder–decoder fully convolutional neural network.

###### 2.1.3 Recurrent neural networks

Recurrent neural network (RNN) is a further ANN type, where unlike feedforward NNs, neurons in the same hidden layer are connected to form a directed cycle. RNNs may accept sequential data as input, making them ideal for timedependent tasks (Chen et al, 2018). The RNN processes inputs one at a time, using the hidden unit output as extra input for the next element (Berman et al, 2019). An RNN’s hidden units can keep a state vector that holds a memory of previous occurrences in the sequence.

It is feasible to think of RNN in two ways: ﬁrst, as a state system with the property that each state, except the ﬁrst, yields an outcome; secondly, as a sequence of vanilla feedforward neural networks, each of which feeds information from one hidden layer to the next. For RNNs, according to Caterini and Chang (2018b), the layerwise function f can be written as

fi(hi−1) = α(W · hi−1 + U · xi + b).

where α is an elementwise nonlinearity (a typical choice for RNN is the tanh function), and where the hidden vector state h evolves according to a hiddento-hidden weight matrix W, which starts from an input-to-hidden weight matrix U and a bias vector b.

RNNs have also been enhanced with several memory unit types, such as long short time memory (LSTM) and gated recurrent unit (GRU) (Aldweesh

- et al, 2020). Long short-term memory (LSTM) units have been created to allow RNNs to handle challenges requiring long-term memories, since LSTM units have a structure called a memory cell that stores information. Each LSTM layer has a set of interacting units, or cells, similar to those found in a neural network. An LSTM is made up of four interacting units: an internal cell, an input gate, a forget gate, and an output gate. The cell state, controlled by the gates, can selectively propagate relevant information throughout the temporal sequence to capture the long short-term time dependency in a dynamical system (Zhang et al, 2020). The gated recurrent unit (GRU) is another RNN unit developed for extended memory; GRUs are comparable to LSTM, however they contain fewer parameters and are hence easier to train (Berman et al, 2019).


###### RNN architectures

Viana et al (2021) introduce, in the form of a neural network, a model discrepancy term into a given ordinary diﬀerential equation. Recurrent neural networks are seen as ideal for dynamical systems because they expand classic feedforward networks to incorporate time-dependent responses. Because a recurrent neural network applies transformations to given states in a sequence on a periodic basis, it is possible to design a recurrent neural network cell that does Euler integration; in fact, physics-informed recurrent neural networks can be used to perform numerical integration.

Viana et al (2021) build recurrent neural network cells in such a way that speciﬁc numerical integration methods (e.g., Euler, Riemann, Runge-Kutta, etc.) are employed. The recurrent neural network is then represented as a directed graph, with nodes representing individual kernels of the physicsinformed model. The graph created for the physics-informed model can be used to add data-driven nodes (such as multilayer perceptrons) to adjust the outputs of certain nodes in the graph, minimizing model discrepancy.

###### LSTM architectures

Physicists have typically employed distinct LSTM networks to depict the sequence-to-sequence input-output relationship; however, these networks are not homogeneous and cannot be directly connected to one another. In Zhang

- et al (2020) this relationship is expressed using a single network and a central ﬁnite diﬀerence ﬁlter-based numerical diﬀerentiator. Zhang et al (2020) show two architectures for representation learning of sequence-to-sequence features from limited data that is augmented by physics models. The proposed networks is made up of two (PhyLSTM2) or three (PhyLSTM3) deep LSTM networks that describe state space variables, nonlinear restoring force, and hysteretic parameter. Finally, a tensor diﬀerentiator, which determines the derivative of state space variables, connects the LSTM networks.


Another approach is Yucesan and Viana (2021) for temporal integration, that implement an LSTM using a previously introduced Euler integration cell.

###### 2.1.4 Other architectures for PINN

Apart from fully connected feed forward neural networks, convolutional neural networks, and recurrent neural networks, this section discusses other approaches that have been investigated. While there have been numerous other networks proposed in the literature, we discovered that only Bayesian neural networks (BNNs) and generative adversarial networks (GANs) have been applied to PINNs. Finally, an interesting application is to combine multiple PINNs, each with its own neural network.

Bayesian Neural Network In the Bayesian framework, Yang et al (2021) propose to use Bayesian neural networks (BNNs), in their B-PINNs, that consists of a Bayesian neural network subject to the PDE constraint that acts as a prior. BNN are neural networks with weights that are distributions rather than deterministic values, and these distributions are learned using Bayesian inference. For estimating the posterior distributions, the B-PINN authors use the Hamiltonian Monte Carlo (HMC) method and the variational inference (VI). Yang et al (2021) ﬁnd that for the posterior estimate of B-PINNs, HMC is more appropriate than VI with mean ﬁeld Gaussian approximation. They analyse also the possibility to use the Karhunen-Lo`eve expansion as a stochastic process representation, instead of BNN. Although the KL is as accurate as BNN and considerably quicker, it cannot be easily applied to highdimensional situations. Finally, they observe that to estimate the posterior of a Bayesian framework, KL-HMC or deep normalizing ﬂow (DNF) models can be employed. While DNF is more computationally expensive than HMC, it is more capable of extracting independent samples from the target distribution after training. This might be useful for data-driven PDE solutions, however it is only applicable to low-dimensional problems.

###### GAN architectures

In generative adversarial networks (GANs), two neural networks compete in a zero-sum game to deceive each other. One network generates and the other discriminates. The generator accepts input data and outputs data with realistic characteristics. The discriminator compares the real input data to the output of the generator. After training, the generator can generate new data that is indistinguishable from real data (Berman et al, 2019).

Yang et al (2020) propose a new class of generative adversarial networks (PI-GANs) to address forward, inverse, and mixed stochastic problems in a uniﬁed manner. Unlike typical GANs, which rely purely on data for training, PI-GANs use automatic diﬀerentiation to embed the governing physical laws in the form of stochastic diﬀerential equations (SDEs) into the architecture of

PINNs. The discriminator in PI-GAN is represented by a basic FFNN, while the generators are a combination of FFNNs and a NN induced by the SDE.

###### Multiple PINNs

A ﬁnal possibility is to combine several PINNs, each of which could be implemented using a diﬀerent neural network. Jagtap et al (2020b) propose a conservative physics-informed neural network (cPINN) on discrete domains. In this framework, the complete solution is recreated by patching together all of the solutions in each sub-domain using the appropriate interface conditions. This type of domain segmentation also allows for easy network parallelization, which is critical for obtaining computing eﬃciency. This method may be expanded to a more general situation, called by the authors as Mortar PINN, for connecting non-overlapping deconstructed domains. Moreover, the suggested technique may use totally distinct neural networks, in each subdomain, with various architectures to solve the same underlying PDE.

Stiller et al (2020) proposes the GatedPINN architecture by incorporating conditional computation into PINN. This architecture design is composed of a gating network and set of PINNs, hereinafter referred to as “experts”; each expert solves the problem for each space-time point, and their results are integrated via a gating network. The gating network determines which expert should be used and how to combine them. We will use one of the expert networks as an example in the following section of this review.

#### 2.2 Injection of Physical laws

To solve a PDE with PINNs, derivatives of the network’s output with respect to the inputs are needed. Since the function u is approximated by a NN with smooth activation function, uˆθ, it can be diﬀerentiated. There are four methods for calculating derivatives: hand-coded, symbolic, numerical, and automatic. Manually calculating derivatives may be correct, but it is not automated and thus impractical (Waheed et al, 2021).

Symbolic and numerical methods like ﬁnite diﬀerentiation perform very badly when applied to complex functions; automatic diﬀerentiation (AD), on the other hand, overcomes numerous restrictions as ﬂoating-point precision errors, for numerical diﬀerentiation, or memory intensive symbolic approach. AD use exact expressions with ﬂoating-point values rather than symbolic strings, there is no approximation error (Waheed et al, 2021).

Automatic diﬀerentiation (AD) is also known as autodiﬀ, or algorithmic diﬀerentiation, although it would be better to call it algorithmic diﬀerentiation since AD does not totally automate diﬀerentiation: instead of symbolically evaluating derivatives operations, AD performs an analytical evaluation of them.

Considering a function f : Rn → Rm of which we want to calculate the Jacobian J, after calculating the graph of all the operations composing the mathematical expression, AD can then work in either forward or reverse mode for calculating the numerical derivative.

###### NN family NN type Papers

Dwivedi and Srinivasan (2020), Schiassi et al (2021)

1 layer / EML

FF-NN

32 neurons per layer He et al (2020) 50 neurons per layer Tartakovsky et al (2020)

2-4 layers

5-8 layers 250 neurons per layer Zhu et al (2021)

Cheng and Zhang (2021) Waheed et al (2021)

9+ layers

Sparse Ramabathiran and Ramachandran (2021)

Amini Niaki et al (2021) Islam et al (2021)

multi FC-DNN

CNN

Gao et al (2021) Fang (2021)

plain CNN

Zhu et al (2019), Geneva and Zabaras (2020) Wang et al (2021a)

AE CNN

RNN

RNN Viana et al (2021)

Zhang et al (2020) Yucesan and Viana (2021)

LSTM

BNN Yang et al (2021) GAN Yang et al (2020)

Other

- Table 1: The main neural network utilized in PINN implementations is synthesized in this table. We summarize Section 2 by showcasing some of the papers that represent each of the many Neural Network implementations of PINN. Feedforward neural networks (FFNNs), convolutional neural networks (CNNs), and recurrent neural networks (RNN) are the three major families of Neural Networks reported here. A publication is reported for each type that either used this type of network ﬁrst or best describes its implementation. In the literature, PINNs have mostly been implemented with FFNNs with 5-10 layers. CNN appears to have been applied in a PCNN manner for the ﬁrst time, by incorporating the boundary condition into the neural network structure rather than the loss.


AD results being the main technique used in literature and used by all PINN implementations, in particular only Fang (2021) use local ﬁtting method

approximation of the diﬀerential operator to solve the PDEs instead of automatic diﬀerentiation (AD). Moreover, by using local ﬁtting method rather than employing automated diﬀerentiation, Fang is able to verify that a his PINN implementation has a convergence.

Essentially, AD incorporates a PDE into the neural network’s loss equation (2), where the diﬀerential equation residual is

rF[uˆθ](z) = rθ(z) := F(uˆθ(z); γ) − f,

and similarly the residual NN corresponding to boundary conditions (BC) or initial conditions (IC) is obtained by substituting uˆθ in the second equation of (1), i.e.

rB[uˆθ](z) := B(uˆθ(z)) − g(z). Using these residuals, it is possible to assess how well an approximation uθ satisﬁes (1). It is worth noting that for the exact solution, u, the residuals are rF[u] = rB[u] = 0 (De Ryck et al, 2022).

In Raissi and Karniadakis (2018); Raissi et al (2019), the original formulation of the aforementioned diﬀerential equation residual, leads to the form of

∂ ∂t

uˆθ(x,t) + Fxuˆθ(x,t).

rF[ˆuθ](z) = rθ(x,t) =

In the deep learning framework, the principle of imposing physical constraints is represented by diﬀerentiating neural networks with respect to input spatiotemporal coordinates using the chain rule. In Mathews et al (2021) the model loss functions are embedded and then further normalized into dimensionless form. The repeated diﬀerentiation, with AD, and composition of networks used to create each individual term in the partial diﬀerential equations results in a much larger resultant computational graph. As a result, the cumulative computation graph is eﬀectively an approximation of the PDE equations (Mathews et al, 2021).

The chain rule is used in automatic diﬀerentiation for several layers to compute derivatives hierarchically from the output layer to the input layer. Nonetheless, there are some situations in which the basic chain rule does not apply. Pang et al (2019) substitute fractional diﬀerential operators with their discrete versions, which are subsequently incorporated into the PINNs’ loss function.

#### 2.3 Model estimation by learning approaches

The PINN methodology determines the parameters θ of the NN, uˆθ, by minimizing a loss function, i.e.

where

L(θ)

θ = arg min

θ

L(θ) = ωFLF(θ) + ωBLB(θ) + ωdLdata(θ). (6)

The three terms of L refer to the errors in describing the initial Li or boundary condition Lb, both indicated as LB, the loss respect the partial diﬀerential equation LF, and the validation of known data points Ldata. Losses are usually deﬁned in the literature as a sum, similar to the previous equations, however they can be considered as integrals

LF(θ) =

(F(uˆθ(z)) − f(zi)))2 dz

Ω¯

This formulation is not only useful for a theoretical study, as we will see in 2.4, but it is also implemented in a PINN package, NVIDIA Modulus (NVIDIA Corporation, 2021), allowing for more eﬀective integration strategies, such as sampling with higher frequency in speciﬁc areas of the domain to more eﬃciently approximate the integral losses.

Note that, if the PINN framework is employed as a supervised methodology, the neural network parameters are chosen by minimizing the diﬀerence between the observed outputs and the model’s predictions; otherwise, just the PDE residuals are taken into account.

As in equation (6) the ﬁrst term, LF, represents the loss produced by a mismatch with the governing diﬀerential equations F (He et al, 2020; Stiller

- et al, 2020). It enforces the diﬀerential equation F at the collocation points, which can be chosen uniformly or unevenly over the domain Ω of equation (1). The remaining two losses attempt to ﬁt the known data over the NN. The loss caused by a mismatch with the data (i.e., the measurements of u) is denoted


by Ldata(θ). The second term typically forces uˆθ to mach the measurements of u over provided points (z,u∗), which can be given as synthetic data or actual measurements, and the weight ωd can account for the quality of such measurements. The other term is the loss due to mismatch with the boundary or initial conditions, B(uˆθ) = g from equation (1).

Essentially, the training approach recovers the shared network parameters θ from:

- • few scattered observations of u(z), speciﬁcally {zi,u∗i }, i = 1,...,Nd
- • as well as a greater number of collocation points {zi,ri = 0}, i = 1,...,Nr for the residual,


The resulting optimization problem can be handled using normal stochastic gradient descent without the need for constrained optimization approaches by minimizing the combined loss function. A typical implementation of the loss uses a mean square error formulation (Kollmannsberger et al, 2021), where:

1 Nc

LF(θ) = MSEF =

Nc

Nc

1 Nc

 F(uˆθ(zi)) − f(zi)) 2 =

i=1

i=1

rθ(ui) − ri 2

enforces the PDE on a wide set of randomly selected collocation locations inside the domain, i.e. penalizes the diﬀerence between the estimated left-hand side of a PDE and the known right-hand side of a PDE (Kollmannsberger

- et al, 2021); other approaches may employ an integral deﬁnition of the loss (Hennigh et al, 2021). As for the boundary and initial conditions, instead


1 NB

LB(θ) = MSEB =

whereas for the data points,

NB

 B(uˆθ(z)) − g(zi)) 2

i=1

Nd

1 Nd

Ldata(θ) = MSEdata =

i=1

uˆθ(zi) − u∗i 2.

computes the error of the approximation u(t,x) at known data points. In the case of a forward problem, the data loss might also indicate the boundary and initial conditions, while in an inverse problem it refers to the solution at various places inside the domain (Kollmannsberger et al, 2021).

In Raissi and Karniadakis (2018); Raissi et al (2019), original approach the overall loss (6) was formulated as

Nc

1 Nc

L(θ) =

i=1

Nd

∂ ∂t

1 Nd

uˆθ(x,t) + Fxuˆθ(x,t) − ri 2 +

i=1

uˆθ(xi,ti) − u∗i 2.

The gradients in F are derived using automated diﬀerentiation. The resulting predictions are thus driven to inherit any physical attributes imposed by the PDE constraint (Yang and Perdikaris, 2019). The physics constraints are included in the loss function to enforce model training, which can accurately reﬂect latent system nonlinearity even when training data points are scarce (Zhang et al, 2020).

###### Observations about the loss

The loss LF(θ) is calculated by utilizing automated diﬀerentiation (AD) to compute the derivatives of uˆθ(z) (He et al, 2020). Most ML libraries, including TensorFlow and Pytorch, provide AD, which is mostly used to compute derivatives with respect to DNN weights (i.e. θ). AD permits the PINN approach to implement any PDE and boundary condition requirements without numerically discretizing and solving the PDE (He et al, 2020).

Additionally, by applying PDE constraints via the penalty term LF(θ), it is possible to use the related weight ωF to account for the PDE model’s ﬁdelity. To a low-ﬁdelity PDE model, for example, can be given a lower weight. In general, the number of unknown parameters in θ is substantially greater than the number of measurements, therefore regularization is required for DNN training (He et al, 2020).

By removing loss for equations from the optimization process (i.e., setting ωF = 0), neural networks could be trained without any knowledge of the underlying governing equations. Alternatively, supplying initial and boundary conditions for all dynamical variables would correspond to solving the equations directly with neural networks on a regular basis (Mathews et al,

- 2021). While it is preferable to enforce the physics model across the entire domain,


the computational cost of estimating and reducing the loss function (6), while training, grows with the number of residual points (He et al, 2020). Apart the number of residual points, also the position (distribution) of residual points are crucial parameters in PINNs because they can change the design of the loss function (Mao et al, 2020).

A deep neural network can reduce approximation error by increasing network expressivity, but it can also produce a large generalization error. Other hyperparameters, such as learning rate, number of iterations, and so on, can be adjusted to further control and improve this issue.

The addition of extra parameters layer by layer in a NN modiﬁes the slope of the activation function in each hidden-layer, improving the training speed. Through the slope recovery term, these activation slopes can also contribute to the loss function (Jagtap et al, 2020b).

Soft and hard constraint BC constraints can be regarded as penalty terms (soft BC enforcement) (Zhu

- et al, 2019), or they can be encoded into the network design (hard BC enforcement) (Sun et al, 2020a). Many existing PINN frameworks use a soft approach to constrain the BCs by creating extra loss components deﬁned on the collocation points of borders. The disadvantages of this technique are twofold:


- 1. satisfying the BCs accurately is not guaranteed;
- 2. the assigned weight of BC loss might eﬀect learning eﬃciency, and no theory exists to guide determining the weights at this time.


Zhu et al (2021) address the Dirichlet BC in a hard approach by employing a speciﬁc component of the neural network to purely meet the speciﬁed Dirichlet BC. Therefore, the initial boundary conditions are regarded as part of the labeled data constraint.

When compared to the residual-based loss functions typically found in the literature, the variational energy-based loss function is simpler to minimize and so performs better (Goswami et al, 2020). Loss function can be constructed using collocation points, weighted residuals derived by the Galerkin-Method (Kharazmi et al, 2019), or energy based. Alternative loss functions approaches are compared in Li et al (2021), by using either only data-driven (with no physics model), a PDE-based loss, and an energy-based loss. They observe that there are advantages and disadvantages for both PDE-based and energybased approaches. PDE-based loss function has more hyperparameters than the energy-based loss function. The energy-based strategy is more sensitive to

the size and resolution of the training samples than the PDE-based strategy, but it is more computationally eﬃcient.

###### Optimization methods

The minimization process of the loss function is called training; in most of the PINN literature, loss functions are optimized using minibatch sampling using Adam and the limited-memory Broyden-Fletcher-Goldfarb-Shanno (LBFGS) algorithm, a quasi-Newton optimization algorithm. When monitoring noisy data, Mathews et al (2021) found that increasing the sample size and training only with L-BFGS achieved the optimum for learning.

For a moderately sized NN, such as one with four hidden layers (depth of the NN is 5) and twenty neurons in each layer (width of the NN is 20), we have over 1000 parameters to optimize. There are several local minima for the loss function, and the gradient-based optimizer will almost certainly become caught in one of them; ﬁnding global minima is an NP-hard problem (Pang

- et al, 2019). The Adam approach, which combines adaptive learning rate and momen-


tum methods, is employed in Zhu et al (2021) to increase convergence speed, because stochastic gradient descent (SGD) hardly manages random collocation points, especially in 3D setup.

Yang et al (2020) use Wasserstein GANs with gradient penalty (WGANGP) and prove that they are more stable than vanilla GANs, in particular for approximating stochastic processes with deterministic boundary conditions.

cPINN (Jagtap et al, 2020b) allow to ﬂexibly select network hyperparameters such as optimization technique, activation function, network depth, or network width based on intuitive knowledge of solution regularity in each sub-domain. E.g. for smooth zones, a shallow network may be used, and a deep neural network can be used in an area where a complex nature is assumed.

He et al (2020) propose a two-step training approach in which the loss function is minimized ﬁrst by the Adam algorithm with a predeﬁned stop condition, then by the L-BFGS-B optimizer. According to the aforementioned paper, for cases with a little amount of training data and/or residual points, L-BFGS-B, performs better with a faster rate of convergence and reduced computing cost.

Finally, let’s look at a practical examples for optimizing the training process; dimensionless and normalized data are used in DeepONet training to improve stability (Lin et al, 2021b). Moreover the governing equations in dimensionless form, including the Stokes equations, electric potential, and ion transport equations, are presented in DeepM&Mnets (Cai et al, 2021b).

In terms of training procedure initialization, slow and fast convergence behaviors are produced by bad and good initialization, respectively, but Pang

- et al (2019) reports a technique for selecting the most suitable one. By using a limited number of iterations, one can ﬁrst solve the inverse problem. This preliminary solution has low accuracy due to discretization, sampling, and


optimization errors. The optimized parameters from the low-ﬁdelity problem can then be used as a suitable initialization.

#### 2.4 Learning theory of PINN

This ﬁnal subsection provides most recent theoretical studies on PINN to better understand how they work and their potential limits. These investigations are still in their early stages, and much work remains to be done.

Let us start by looking at how PINN can approximate the true solution of a diﬀerential equation, similar to how error analysis is done a computational framework. In traditional numerical analysis, we approximate the true solution u(z) of a problem with an approximation scheme that computes uˆθ(z). The main theoretical issue is to estimate the global error

E = uˆθ(z) − u(z). Ideally, we want to ﬁnd a set of parameters, θ, such that E = 0.

When solving diﬀerential equations using a numerical discretization technique, we are interested in the numerical method’s stability, consistency, and convergence (Ryaben’kii and Tsynkov, 2006; Arnold, 2015; Thompson, 1992). In such setting, discretization’s error can be bound in terms of consistency and stability, a basic result in numerical analysis. The Lax-Richtmyer Equivalence Theorem is often referred to as a fundamental result of numerical analysis where roughly the convergence is ensured when there is consistency and stability.

When studying PINN to mimic this paradigm, the convergence and stability are related to how well the NN learns from physical laws and data. In this conceptual framework, we use a NN, which is a parameterized approximation of problem solutions modeled by physical laws. In this context, we will (i) introduce the concept of convergence for PINNs, (ii) revisit the main error analysis deﬁnitions in a statistical learning framework, and (iii) ﬁnally report results for the generalization error.

###### 2.4.1 Convergence aspects

The goal of a mathematical foundation for the PINN theory is to investigate the convergence of the computed uˆθ(z) to the solution of problem (1), u(z).

Consider a NN conﬁguration with coeﬃcients compounded in the vector θ and a cardinality equal to the number of coeﬃcients of the NN, #θ. In such setting, we can consider the hypothesis class

Hn = {uθ : #θ = n}

composed of all the predictors representing a NN whose number of coeﬃcients of the architecture is n. The capacity of a PINN to be able to learn, is related to how big is n, i.e. the expressivity of Hn.

In such setting, a theoretical issue, is to investigate, how dose the sequence of compute predictors, uˆθ, converges to the solution of the physical problem

(1)

uˆθ(n) → u, n → ∞. A recent result in this direction was obtained by De Ryck et al (2021) in

which they proved that the diﬀerence uˆθ(n) − u converges to zero as the width of a predeﬁned NN, with activation function tanh, goes to inﬁnity.

Practically, the PINN requires choosing a network class Hn and a loss function given a collection of N-training data (Shin et al, 2020a). Since the quantity and quality of training data aﬀect Hn, the goal is to minimize the loss, by ﬁnding a uθ∗ ∈ Hn, by training the N using an optimization process. Even if Hn includes the exact solution u to PDEs and a global minimizer is established, there is no guarantee that the minimizer and the solution u will coincide. A ﬁrst work related on PINN (Shin et al, 2020a), the authors show that the sequence of minimizers uˆθ∗ strongly converges to the solution of a linear second-order elliptic and parabolic type PDE.

###### 2.4.2 Statistical Learning error analysis

The entire learning process of a PINN can be considered as a statistical learning problem, and it involves mathematical foundations aspects for the error analysis (Kutyniok, 2022). For a mathematical treatment of errors in PINN, it is important to take into account: optimization, generalization errors, and approximation error. It is worth noting that the last one is dependent on the architectural design. Let be N collocation points on Ω = Ω¯ ∪∂Ω, a NN approximation realized with θ, denoted by uˆθ, evaluated at points zi, whose exact value is hi. Following the notation of Kutyniok (2022), the empirical risk is deﬁned as

N

1 N

R[uθ] :=

i=1

uˆθ(zi) − hi, 2 (7)

and represents how well the NN is able to predict the exact value of the problem. The empirical risk actually corresponds to the loss deﬁned in 2.3, where uˆθ = F(uˆθ(zi)) and hi = f(zi) and similarly for the boundaries.

A continuum perspective is the risk of using an approximator uˆθ, calculated as follows:

(ˆuθ(z) − u(z))2 dz, (8)

R[ˆuθ] :=

Ω¯

where the distance between the approximation uˆθ and the solution u is obtained with the L2-norm. The ﬁnal approximation computed by the PINN,

after a training process of DNN, is uˆ∗θ. The main aim in error analysis, is to ﬁnd suitable estimate for the risk of predicting u i.e. R[ˆu∗θ]. The training process, uses gradient-based optimization techniques to minimize a generally non convex cost function. In practice, the algorithmic optimization

scheme will not always ﬁnd a global minimum. So the error analysis takes into account the optimization error deﬁned as follows:

EO := R[ˆu∗θ] − inf

R[uθ]

θ∈Θ

Because the objective function is nonconvex, the optimization error is unknown. Optimization frequently involves a variety of engineering methods and time-consuming ﬁne-tuning, using, gradient-based optimization methods. Several stochastic gradient descent methods have been proposed,and many PINN use Adam and L-BFGS. Empirical evidence suggests that gradient-based optimization techniques perform well in diﬀerent challenging tasks; however, gradient-based optimization might not ﬁnd a global minimum for many ML tasks, such as for PINN, and this is still an open problem (Shin et al, 2020a).

Moreover a measure of the prediction accuracy on unseen data in machine learning is the generalization error:

EG := sup θ∈Θ

|R[uθ] − R[uθ]|

The generalization error measures how well the loss integral is approximated in relation to a speciﬁc trained neural network. One of the ﬁrst paper focused with convergence of generalization error is Shin et al (2020a).

About the ability of the NN to approximate the exact solution, the approximation error is deﬁned as

EA := inf

R[uθ]

θ∈Θ

The approximation error is well studied in general, in fact we know that one layer neural network with a high width can evenly estimate a function and its partial derivative as shown by Pinkus (1999).

Finally, as stated in Kutyniok (2022), the global error between the trained

deep neural network uˆ∗θ and the correct solution function u of problem (1), can so be bounded by the previously deﬁned error in the following way

R[ˆu∗θ] ≤ EO + 2EG + EA (9)

These considerations lead to the major research threads addressed in recent studies, which are currently being investigated for PINN and DNNs in general Kutyniok (2022).

###### 2.4.3 Error analysis results for PINN

About the approximating error, since it depends on the NN architecture, mathematical foundations results are generally discussed in papers deeply focused on this topic Calin (2020b); Elbr¨chter et al (2021).

However, a ﬁrst argumentation strictly related to PINN is reported in Shin

- et al (2020b). One of the main theoretical results on EA, can be found in De Ryck et al (2021). They demonstrate that for a neural network with a


tanh activation function and only two hidden layers, uˆθ, may approximate a function u with a bound in a Sobolev space:

ln(cN)k Ns−k

N − u Wk,∞ ≤ C

uˆθ

where N is the number of training points, c,C > 0 are constants independent of N and explicitly known, u ∈ Ws,∞([0,1]d). We remark that the NN has width Nd, and #θ depends on both the number of training points N and the dimension of the problem d.

Formal ﬁndings for generalization errors in PINN are provided speciﬁcally for a certain class of PDE. In Shin et al (2020a) they provide convergence estimate for linear second-order elliptic and parabolic type PDEs, while in Shin et al (2020b) they extend the results to all linear problems, including hyperbolic equations. Mishra and Molinaro (2022) gives an abstract framework for PINN on forward problem for PDEs, they estimate the generalization error by means of training error (empirical risk), and number of training points, such abstract framework is also addressed for inverse problems (Mishra and Molinaro, 2021a). In De Ryck et al (2022) the authors speciﬁcally address Navier-Stokes equations and show that small training error imply a small generalization error, by proving that

1 d

R[ˆuθ] = u − uˆθ L2 ≤ CR[uθ] + O N−

- 1

- 2


.

This estimate suﬀer from the curse of dimensionality (CoD), that is to say, in order to reduce the error by a certain factor, the number of training points needed and the size of the neural network, scales up exponentially.

De Ryck and Mishra (2021) prove that for a Kolmogorov type PDE (i.e. heat equation or Black-Scholes equation), the following inequality holds, almost always,

- 1

- 2


- 1

- 2


R[ˆuθ] ≤ CR[uθ] + O N−

, and is not dependant on the dimension of the problem d.

Finally, Mishra and Molinaro (2021b) investigates the radiative transfer equation, which is noteworthy for its high-dimensionality, with the radiative intensity being a function of 7 variables (instead of 3, as common in many physical problems). The authors prove also here that the generalization error is bounded by the training error and the number of training points, and the

dimensional dependence is on a logarithmic factor:

R[ˆuθ] ≤ CR[uθ]2 + c

(lnN)2d N

- 1

- 2


.

The authors are able to show that PINN does not suﬀer from the dimensionality curse for this problem, observing that the training error does not depend on the dimension but only on the number of training points.

### 3 Diﬀerential problems dealt with PINNs

The ﬁrst vanilla PINN (Raissi et al, 2019) was built to solve complex nonlinear PDE equations of the form ut +Fxu = 0, where x is a vector of space coordinates, t is a vector time coordinate, and Fx is a nonlinear diﬀerential operator with respect to spatial coordinates. First and mainly, the PINN architecture was shown to be capable of handling both forward and inverse problems. Eventually, in the years ahead, PINNs have been employed to solve a wide variety of ordinary diﬀerential equations (ODEs), partial diﬀerential equations (PDEs), Fractional PDEs, and integro-diﬀerential equations (IDEs), as well as stochastic diﬀerential equations (SDEs). This section is dedicated to illustrate where research has progressed in addressing various sorts of equations, by grouping equations according to their form and addressing the primary work in literature that employed PINN to solve such equation. All PINN papers dealing with ODEs will be presented ﬁrst. Then, works on steady-state PDEs such as Elliptic type equations, steady-state diﬀusion, and the Eikonal equation are reported. The Navier–Stokes equations are followed by more dynamical problems such as heat transport, advection-diﬀusion-reaction system, hyperbolic equations, and Euler equations or quantum harmonic oscillator. Finally, while all of the previous PDEs can be addressed in their respective Bayesian problems, the ﬁnal section provides insight into how uncertainly is addressed, as in stochastic equations.

#### 3.1 Ordinary Diﬀerential Equations

ODEs can be used to simulate complex nonlinear systems which are diﬃcult to model using simply physics-based models (Lai et al, 2021). A typical ODE system is written as

du(x,t) dt

= f(u(x,t),t)

where initial conditions can be speciﬁed as B(u(t)) = g(t), resulting in an initial value problem or boundary value problem with B(u(x)) = g(x). A PINN approach is used by Lai et al (2021) for structural identiﬁcation, using Neural Ordinary Diﬀerential Equations (Neural ODEs). Neural ODEs can be considered as a continuous representation of ResNets (Residual Networks), by using a neural network to parameterize a dynamical system in the form of

ODE for an initial value problem (IVP):

du(t) dt

= fθ(u(t),t); u(t0) = u0

where f is the neural network parameterized by the vector θ.

The idea is to use Neural ODEs as learners of the governing dynamics of the systems, and so to structure of Neural ODEs into two parts: a physics-informed term and an unknown discrepancy term. The framework is tested using a spring-mass model as a 4-degree-of-freedom dynamical system with cubic nonlinearity, with also noisy measured data. Furthermore, they use experimental data to learn the governing dynamics of a structure equipped with a negative stiﬀness device (Lai et al, 2021).

Zhang et al (2020) employ deep long short-term memory (LSTM) networks in the PINN approach to solve nonlinear structural system subjected to seismic excitation, like steel moment resistant frame and the single degree-of-freedom Bouc–Wen model, a nonlinear system with rate-dependent hysteresis (Zhang

- et al, 2020). In general they tried to address the problems of nonlinear equation of motion :


u¨ + g = −Γag where g(t) = M−1h(t) denotes the mass-normalized restoring force, being M the mass matrices; h the total nonlinear restoring force, and Γ force distribution vector.

Directed graph models can be used to directly implement ODE as deep neural networks (Viana et al, 2021), while using an Euler RNN for numerical integration.

In Nascimento et al (2020) is presented a tutorial on how to use Python to implement the integration of ODEs using recurrent neural networks.

ODE-net idea is used in Tong et al (2021) for creating Symplectic Taylor neural networks. These NNs consist of two sub-networks, that use symplectic integrators instead of Runge-Kutta, as done originally in ODE-net, which are based on residual blocks calculated with the Euler method. Hamiltonian systems as Lotka–Volterra, Kepler, and H´enon–Heiles systems are also tested in the aforementioned paper.

#### 3.2 Partial Diﬀerential Equations

Partial Diﬀerential Equations are the building bricks of a large part of models that are used to mathematically describe physics phenomenologies. Such models have been deeply investigated and often solved with the help of different numerical strategies. Stability and convergence of these strategies have been deeply investigated in literature, providing a solid theoretical framework to approximately solve diﬀerential problems. In this Section, the application of the novel methodology of PINNs on diﬀerent typologies of Partial Diﬀerential models is explored.

###### 3.2.1 Steady State PDEs

In Kharazmi et al (2021b, 2019), a general steady state problem is addressed as:

Fs(u(x); q) = f(x) x ∈ Ω, B(u(x)) = 0 x ∈ ∂Ω

over the domain Ω ⊂ Rd with dimensions d and bounds ∂Ω. Fs typically contains diﬀerential and/or integro-diﬀerential operators with parameters q and f(x) indicates some forcing term.

In particular an Elliptic equation can generally be written by setting

Fs(u(x); σ,µ) = −div(µ∇u)) + σu Tartakovsky et al (2020) consider a linear

Fs(u(x); σ) = ∇ · (K(x)∇u(x)) = 0 and non linear

Fs(u(x); σ) = ∇ · [K(u)∇u(x)] = 0 diﬀusion equation with unknown diﬀusion coeﬃcient K. The equation essentially describes an unsaturated ﬂow in a homogeneous porous medium, where u is the water pressure and K(u) is the porous medium’s conductivity. It is diﬃcult to measure K(u) directly, so Tartakovsky et al (2020) assume that only a ﬁnite number of measurements of u are available.

Tartakovsky et al (2020) demonstrate that the PINN method outperforms the state-of-the-art maximum a posteriori probability method. Moreover, they show that utilizing only capillary pressure data for unsaturated ﬂow, PINNs can estimate the pressure-conductivity for unsaturated ﬂow. One of the ﬁrst novel approach, PINN based, was the variational physics-informed neural network (VPINN) introduced in Kharazmi et al (2019), which has the advantage of decreasing the order of the diﬀerential operator through integration-byparts. The authors tested VPINN with the steady Burgers equation, and on the two dimensional Poisson’s equation. VPINN Kharazmi et al (2019) is also used to solve Schr¨dinger Hamiltonians, i.e. an elliptic reaction-diﬀusion operator (Grubiˇsi´c et al, 2021).

In Haghighat et al (2021a) a nonlocal approach with the PINN framework is used to solve two-dimensional quasi-static mechanics for linear-elastic and elastoplastic deformation. They deﬁne a loss function for elastoplasticity, and the input variables to the feed-forward neural network are the displacements, while the output variables are the components of the strain tensor and stress tensor. The localized deformation and strong gradients in the solution make the boundary value problem diﬃcult solve. The Peridynamic Diﬀerential Operator (PDDO) is used in a nonlocal approach with the PINN paradigm in Haghighat

- et al (2021a). They demonstrated that the PDDO framework can capture stress and strain concentrations using global functions.


In Dwivedi and Srinivasan (2020) the authors address diﬀerent 1D-2D linear advection and/or diﬀusion steady-state problems from Berg and Nystr¨m

- (2018), by using their PIELM, a PINN combined with ELM (Extreme Learning Machine). A critical point is that the proposed PIELM only takes into account linear diﬀerential operators.


In Ramabathiran and Ramachandran (2021) they consider linear elliptic PDEs, such as the solution of the Poisson equation in both regular and irregular domains, by addressing non-smoothness in solutions.

The authors in Ramabathiran and Ramachandran (2021) propose a class of partially interpretable sparse neural network architectures (SPINN), and this architecture is achieved by reinterpreting meshless representation of PDE solutions.

Laplace-Beltrami Equation is solved on 3D surfaces, like complex geometries, and high dimensional surfaces, by discussing the relationship between sample size, the structure of the PINN, and accuracy (Fang and Zhan, 2020b).

The PINN paradigm has also been applied to Eikonal equations, i.e. are hyperbolic problems written as

1 v2(x)

 ∇u(x) 2 =

, ∀x ∈ Ω,

where v is a velocity and u an unknown activation time. The Eikonal equation describes wave propagation, like the travel time of seismic wave (Waheed et al, 2021; Smith et al, 2021a) or cardiac activation electrical waves (Sahli Costabal

- et al, 2020; Grandits et al, 2021). By implementing EikoNet, for solving a 3D Eikonal equation, Smith et al


(2021a) ﬁnd the travel-time ﬁeld in heterogeneous 3D structures; however, the proposed PINN model is only valid for a single ﬁxed velocity model, hence changing the velocity, even slightly, requires retraining the neural network. EikoNet essentially predicts the time required to go from a source location to a receiver location, and it has a wide range of applications, like earthquake detection.

PINN is also proved to outperform the ﬁrst-order fast sweeping solution in accuracy tests (Waheed et al, 2021), especially in the anisotropic model.

Another approach involves synthetic and patient data for learning heart tissue ﬁber orientations from electroanatomical maps, modeled with anisotropic Eikonal equation (Grandits et al, 2021). In their implementation the authors add to the loss function also a Total Variation regularization for the conductivity vector.

By neglecting anisotropy, cardiac activation mapping is also addressed by Sahli Costabal et al (2020) where PINNs are used with randomized prior functions to quantify data uncertainty and create an adaptive sampling strategy for acquiring and creating activation maps.

Helmholtz equation for weakly inhomogeneous two-dimensional (2D) media under transverse magnetic polarization excitation is addressed in Chen et al

- (2020b) as:


∇2Ez (x,y) + εr (x,y)k02Ez = 0, whereas high frequency Helmholtz equation (frequency domain Maxwell’s equation) is solved in Fang and Zhan (2020a).

###### 3.2.2 Unsteady PDEs

Unsteady PDEs usually describe the evolution in time of a physics phenomena. Also in this case, PINNs have proven their reliability in solving such type of problems resulting in a ﬂexible methodology.

###### 3.2.2.1 Advection-Diﬀusion-Reaction Problems Originally Raissi et al

- (2019) addressed unsteady state problem as:


ut = Fx(u(x)) x ∈ Ω, B(u(x)) = 0 x ∈ ∂Ω

where Fx typically contains diﬀerential operators of the variable x. In particular a general advection-diﬀusion reaction equation can be written by setting

Fx(u(x); b,µ,σ) = −div(µ∇u)) + b∇u + σu, where, given the parameters b,µ,σ, −div(µ∇u)) is the diﬀusion term, while the advection term is b∇u which is also known as transport term, and ﬁnally σu is the reaction term.

Diﬀusion Problems For a composite material, Amini Niaki et al (2021) study a system of equations, that models heat transfer with the known heat equation,

∂2T ∂x2

∂T ∂t

dα dt

= a

+ b

where a,b are parameters, and a second equation for internal heat generation expressed as a derivative of time of the degree of cure α ∈ (0,1) is present.

Amini Niaki et al (2021) propose a PINN composed of two disconnected subnetworks and the use of a sequential training algorithm that automatically adapts the weights in the loss, hence increasing the model’s prediction accuracy.

Based on physics observations, an activation function with a positive output parameter and a non-zero derivative is selected for the temperature describing network’s last layer, i.e. a Softplus activation function, that is a smooth approximation to the ReLU activation function. The Sigmoid function is instead chosen for the last layer of the network that represents the degree of cure. Finally, because of its smoothness and non-zero derivative,

the hyperbolic-tangent function is employed as the activation function for all hidden layers.

Since accurate exotherm forecasts are critical in the processing of composite materials inside autoclaves, Amini Niaki et al (2021) show that PINN correctly predict the maximum part temperature, i.e. exotherm, that occurs in the center of the composite material due to internal heat.

A more complex problem was addressed in Cai et al (2021c), where the authors study a kind of free boundary problem, known as the Stefan problem.

The Stefan problems can be divided into two types: the direct Stefan problem, in its traditional form, entails determining the temperature distribution in a domain during a phase transition. The latter, inverse problem, is distinguished by a set of free boundary conditions known as Stefan conditions Wang and Perdikaris (2021).

The authors characterize temperature distributions using a PINN model, that consists of a DNN to represent the unknown interface and another FCNN with two outputs, one for each phase. This leads to three residuals, each of

which is generated using three neural networks, namely the two phases u(1)θ , u(2)θ , as well as the interface sβ that takes the boundary conditions into consideration. The two sets of parameters θ and β are minimized through the mean squared errors losses:

LF(θ) = L(1)r (θ) + L(2)r (θ) enforces the two PDEs of the heat equation, one for each phase state:

Nc

1 Nc

L(rk)(θ) =

i=1

∂u(θk) ∂t

∂2u(θk) ∂x2

(xi,ti) − ωk

(xi,ti) 2, k = 1,2.

on a set of randomly selected collocation locations {(xi,ti)}N

i=1, and ω1,ω2 are two additional training parameters. While, as for the boundary and initial conditions:

c

LB(θ) = L(1)sbc(θ,β) + L(2)sbc(θ,β) + LsNc

(θ,β) + Ls0

(β)

where L(skbc)

are the boundary condition of u(k) on the moving boundary s(t), LsNc

is the free boundary Stefan problem equation, and Ls0

is the initial condition on the free boundary function. Finally, as for the data,

Nd

1 Nd

Ldata(θ) =

i=1

uθ(xidata,tidata) − u∗i 2,

computes the error of the approximation u(x,t) at known data points.

With the previous setup the authors in Cai et al (2021c) ﬁnd an accurate solution, however, the basic PINN model fails to appropriately identify the unknown thermal diﬀusive values, for the inverse problem, due to a local minimum in the training procedure.

So they employ a dynamic weights technique (Wang et al, 2021b), which mitigates problems that arise during the training of PINNs due to stiﬀness in the gradient ﬂow dynamics. The method signiﬁcantly minimizes the relative prediction error, showing that the weights in the loss function are crucial and that choosing ideal weight coeﬃcients can increase the performance of PINNs (Cai et al, 2021c).

In Wang and Perdikaris (2021), the authors conclude that the PINNs prove to be versatile in approximating complicated functions like the Stefan problem, despite the absence of adequate theoretical analysis like approximation error or numerical stability.

Advection Problems In He and Tartakovsky (2021), multiple advection-dispersion equations are addressed, like

ut + ∇ · (−κ∇u +  vu) = s where κ is the dispersion coeﬃcient.

The authors ﬁnd that the PINN method is accurate and produces results that are superior to those obtained using typical discretization-based methods. Moreover both Dwivedi and Srinivasan (2020) and He and Tartakovsky (2021) solve the same 2D advection-dispersion equation,

ut + ∇ · (−κ∇u + au) = 0

In this comparison, the PINN technique (He and Tartakovsky, 2021) performs better that the ELM method (Dwivedi and Srinivasan, 2020), given the errors that emerge along borders, probably due to larger wights assigned to boundary and initial conditions in He and Tartakovsky (2021).

Moreover, in Dwivedi and Srinivasan (2020), an interesting case of PINN and PIELM failure in solving the linear advection equation is shown, involving PDE with sharp gradient solutions.

He et al (2020) solve Darcy and advection–dispersion equations proposing a Multiphysics-informed neural network (MPINN) for subsurface transport problems, and also explore the inﬂuence of the neural network size on the accuracy of parameter and state estimates.

In Schiassi et al (2021), a comparison of two methods is shown, Deep-TFC and X-TFC, on how the former performs better in terms of accuracy when the problem becomes suﬃciently stiﬀ. The examples are mainly based on 1D time-dependent Burgers’ equation and the Navier—Stokes (NS) equations.

In the example of the two-dimensional Burgers equation, Jagtap et al

- (2020b) demonstrate that by having an approximate a priori knowledge of the position of shock, one can appropriately partition the domain to capture the steep descents in solution. This is accomplished through the cPINN domain decomposition ﬂexibility.


While Arnold and King (2021) addressed the Burgers equations in the context of model predictive control (MPC).

In Meng et al (2020) the authors study a two-dimensional diﬀusion-reaction equation that involves long-time integration and they use a parareal PINN (PPINN) to divide the time interval into equal-length sub-domains. PPINN is composed of a fast coarse-grained (CG) solver and a ﬁner solver given by PINN.

- 3.2.2.2 Flow Problems Particular cases for unsteady diﬀerential problems are the ones connected to the motion of ﬂuids. Navier-Stokes equations are widely present in literature, and connected to a large number of problems and disciplines. This outlines the importance that reliable strategies for solving them has for the scientiﬁc community. Many numerical strategies have been developed to solve this kind of problems. However, computational issues connected to speciﬁc methods, as well as diﬃculties that arise in the choice of the discrete spatio-temporal domain may aﬀect the quality of numerical solution. PINNs, providing meshfree solvers, may allow to overcome some issues of standard numerical methods, oﬀering a novel perspective in this ﬁeld.


Navier-Stokes Equations Generally Navier-Stokes equations are written as

Fx(u(x); ν,p) = −div[ν(∇u + ∇uT)] + (u + ∇)u + ∇p − f,

where, u is the speed of the ﬂuid, p the pressure and ν the viscosity (Quarteroni, 2013). The dynamic equation is coupled with

div(u) = 0 for expressing mass conservation.

The Burgers equation, a special case of the Navier-Stokes equations, was covered in the previous section.

Using quick parameter sweeps, Arthurs and King (2021) demonstrate how PINNs may be utilized to determine the degree of narrowing in a tube. PINNs are trained using ﬁnite element data to estimate Navier-Stokes pressure and velocity ﬁelds throughout a parametric domain. The authors present an active learning algorithm (ALA) for training PINNs to predict PDE solutions over vast areas of parameter space by combining ALA, a domain and mesh generator, and a traditional PDE solver with PINN.

PINNs are also applied on the drift-reduced Braginskii model by learning turbulent ﬁelds using limited electron pressure data (Mathews et al, 2021). The authors simulated synthetic plasma using the global drift-ballooning (GDB) ﬁnite-diﬀerence algorithm by solving a ﬂuid model, ie. two-ﬂuid drift-reduced Braginskii equations. They also observe the possibility to infer 3D turbulent ﬁelds from only 2D observations and representations of the evolution equations. This can be used for ﬂuctuations that are diﬃcult to monitor or when plasma diagnostics are unavailable.

Xiao et al (2020) review available turbulent ﬂow databases and propose benchmark datasets by systematically altering ﬂow conditions.

Zhu et al (2021) predict the temperature and melt pool ﬂuid dynamics in

- 3D metal additive manufacturing AM processes. The thermal-ﬂuid model is characterized by Navier-Stokes equations


(momentum and mass conservation), and energy conservation equations.

They approach the Dirichlet BC in a “hard” manner, employing a speciﬁc piece of the neural network to solely meet the prescribed Dirichlet BC; while Neumann BCs, that account for surface tension, are treated conventionally by adding the term to the loss function. They choose the loss weights based on the ratios of the distinct components of the loss function (Zhu et al, 2021).

Cheng and Zhang (2021) solve ﬂuid ﬂows dynamics with Res-PINN, PINN paired with a Resnet blocks, that is used to improve the stability of the neural network. They validate the model with Burgers’ equation and Navier-Stokes (N-S) equation, in particular, they deal with the cavity ﬂow and ﬂow past cylinder problems. A curious phenomena observed by Cheng and Zhang (2021) is a diﬀerence in magnitude between the predicted and actual pressure despite the fact that the distribution of the pressure ﬁled is essentially the same.

To estimate the solutions of parametric Navier–Stokes equations, Sun et al (2020a) created a physics-constrained, data-free, FC-NN for incompressible ﬂows. The DNN is trained purely by reducing the residuals of the governing N-S conservation equations, without employing CFD simulated data. The boundary conditions are also hard-coded into the DNN architecture, since the aforementioned authors claim that in data-free settings, “hard” boundary enforcement is preferable than “soft” boundary approach.

Three ﬂow examples relevant to cardiovascular applications were used to evaluate the suggested approaches.

In particular, the Navier–Stokes equations are given (Sun et al, 2020a) as:

 

∇ · u = 0, x,t ∈ Ω,γ ∈ Rd,

F(u,p) = 0 :=

∂u ∂t

1 ρ∇p − ν∇2u + bf = 0, x,t ∈ Ω,γ ∈ Rd



+ (u · ∇)u +

where γ is a parameter vector, and with I(x,p,u,γ) = 0, x ∈ Ω,t = 0,γ ∈ Rd, B(t,x,p,u,γ) = 0, x,t ∈ ∂Ω × [0,T],γ ∈ Rd,

where I and B are generic diﬀerential operators that determine the initial and boundary conditions.

The boundary conditions (IC/BC) are addressed individually in Sun et al (2020a). The Neumann BC are formulated into the equation loss, i.e., in a soft manner, whereas the IC and Dirichlet BC are encoded in the DNN, i.e., in a hard manner.

As a last example, NSFnets (Jin et al, 2021) has been developed considering two alternative mathematical representations of the Navier–Stokes equations: the velocity-pressure (VP) formulation and the vorticity-velocity (VV) formulation.

Hyperbolic Equations Hyperbolic conservation law is used to simplify the Navier–Stokes equations in hemodynamics (Kissas et al, 2020).

Hyperbolic partial diﬀerential equations are also addressed by Abreu and Florindo (2021): in particular, they study the inviscid nonlinear Burgers’ equation and 1D Buckley-Leverett two-phase problem. They actually try to address problems of the following type:

∂H(u) ∂x

∂u ∂t

= 0, x ∈ R, t > 0, u(x,0) = u0(x),

+

whose results were compared with those obtained by the Lagrangian-Eulerian and Lax-Friedrichs schemes. While Patel et al (2022) proposes a PINN for discovering thermodynamically consistent equations that ensure hyperbolicity for inverse problems in shock hydrodynamics.

Euler equations are hyperbolic conservation laws that might permit discontinuous solutions such as shock and contact waves, and in particular a one dimensional Euler system is written as (Jagtap et al, 2020b)

∂U ∂t

+ ∇ · f(U) = 0, x ∈ Ω ⊂ R2,

where

 

  f =

 

 

ρ ρu ρE

ρu, p + ρu2 pu + ρuE

U =

given ρ as the density, p as the pressure, u the velocity, and E the total energy. These equations regulate a variety of high-speed ﬂuid ﬂows, including transonic, supersonic, and hypersonic ﬂows. Mao et al (2020) can precisely capture such discontinuous ﬂows solutions for one-dimensional Euler equations, which is a challenging task for existing numerical techniques. According to Mao et al (2020), appropriate clustering of training data points around a high gradient area can improve solution accuracy in that area and reduces error propagation to the entire domain. This enhancement suggests the use of a separate localized powerful network in the region with high gradient solution, resulting in the development of a collection of individual local PINNs with varied features that comply with the known prior knowledge of the solution in each sub-domain. As done in Jagtap et al (2020b), cPINN splits the domain into a number of small subdomains in which multiple neural networks with diﬀerent architectures (known as sub-PINN networks) can be used to solve the same underlying PDE.

Still in reference to Mao et al (2020), the authors solve the one-dimensional Euler equations and a two-dimensional oblique shock wave problem. The authors can capture the solutions with only a few scattered points distributed randomly around the discontinuities. The above-mentioned paper employ density gradient and pressure p(x,t) data, as well as conservation laws, to infer all states of interest (density, velocity, and pressure ﬁelds) for the inverse problem without employing any IC/BCs. They were inspired by the experimental photography technique of Schlieren.

They also illustrate that the position of the training points is essential for the training process. The results produced by combining the data with the Euler equations in characteristic form outperform the results obtained using conservative forms.

- 3.2.2.3 Quantum Problems A 1D nonlinear Schr¨dinger equation is addressed in Raissi (2018), and Raissi et al (2019) as:


∂2ψ ∂x2

∂ψ ∂t

- 1

- 2


+ |ψ|2ψ = 0 (10)

i

+

where ψ(x,t) is the complex-valued solution. This problem was chosen to demonstrate the PINN’s capacity to handle complex-valued answers and we will develop this example in section 3.4. Also a quantum harmonic oscillator (QHO)

∂ψ(x,t) ∂t

- 1

- 2


∆ψ(x,t) − V (x,t) = 0

i

+

is addressed in Stiller et al (2020), with V a scalar potential. They propose a gating network that determines which MLP to use, while each MLP consists of linear layers and tanh activation functions; so the solution becomes a weighted sum of MLP predictions. The quality of the approximated solution of PINNs was comparable to that of state-of-the-art spectral solvers that exploit domain knowledge by solving the equation in the Fourier domain or by employing Hermite polynomials.

Vector solitons, which are solitary waves with multiple components in the the coupled nonlinear Schr¨dinger equation (CNLSE) is addressed by Mo et al (2022), who extended PINNs with a pre-ﬁxed multi-stage training algorithm. These ﬁndings can be extendable to similar type of equations, such as equations with a rogue wave (Wang and Yan, 2021) solution or the Sasa-Satsuma equation and Camassa-Holm equation.

#### 3.3 Other Problems

Physics Informed Neural Networks have been also applied to a wide variety of problems that go beyond classical diﬀerential problems. As examples, in the following, the application of such a strategy as been discussed regarding Fractional PDEs and Uncertainty estimation.

###### 3.3.1 Diﬀerential Equations of Fractional Order

Fractional PDEs can be used to model a wide variety of phenomenological properties found in nature with parameters that must be calculated from experiment data, however in the spatiotemporal domain, ﬁeld or experimental measurements are typically scarce and may be aﬀected by noise (Pang et al, 2019). Because automatic diﬀerentiation is not applicable to fractional operators, the construction of PINNs for fractional models is more complex. One possible solution is to calculate the fractional derivative using the L1 scheme (Mehta et al, 2019).

In the ﬁrst example from Mehta et al (2019) they solve a turbulent ﬂow with one dimensional mean ﬂow.

In Pang et al (2019), the authors focus on identifying the parameters of fractional PDEs with known overall form but unknown coeﬃcients and unknown operators, by giving rise to fPINN. They construct the loss function using a hybrid technique that includes both automatic diﬀerentiation for integerorder operators and numerical discretization for fractional operators. They also analyse the convergence of fractional advection-diﬀusion equations (fractional ADEs)

The solution proposed in Pang et al (2019), is then extended in Kharazmi et al (2021a) where they address also time-dependent fractional orders. The formulation in Kharazmi et al (2021a) uses separate neural network to represent each fractional order and use a large neural network to represent states.

###### 3.3.2 Uncertainty Estimation

In data-driven PDE solvers, there are several causes of uncertainty. The quality of the training data has a signiﬁcant impact on the solution’s accuracy.

To address forward and inverse nonlinear problems represented by partial diﬀerential equations (PDEs) with noisy data, Yang et al (2021) propose a Bayesian physics-informed neural network (B-PINN). The Bayesian neural network acts as the prior in this Bayesian framework, while an Hamiltonian Monte Carlo (HMC) method or variational inference (VI) method can be used to estimate the posterior.

B-PINNs (Yang et al, 2021) leverage both physical principles and scattered noisy observations to give predictions and quantify the aleatoric uncertainty coming from the noisy data.

Yang et al (2021) test their network on some forward problems (1D Poisson equation, Flow in one dimension across porous material with a boundary layer, Nonlinear Poisson equation in one dimension and the 2D Allen-Cahn equation), while for inverse problems the 1D diﬀusion-reaction system with nonlinear source term and 2D nonlinear diﬀusion-reaction system are addressed.

Yang et al (2021) use also the B-PINNs for a high-dimensional diﬀusionreaction system, where the locations of three contaminating sources are inferred from a set of noisy data.

Yang et al (2020) considers the solution of elliptic stochastic diﬀerential equations (SDEs) that required approximations of three stochastic processes: the solution u(x; γ), the forcing term f(x; γ), and the diﬀusion coeﬃcient k(x; γ).

In particular, Yang et al (2020) investigates the following, time independent, SDE

Fx[u(x; γ); k(x; γ)] = f(x; γ),

Bx[u(x; γ)] = b(x; γ), where k(x; γ) and f(x; γ) are independent stochastic processes, with k strictly positive.

Furthermore, they investigate what happens when there are a limited number of measurements from scattered sensors for the stochastic processes. They show how the problem gradually transform from forward to mixed, and ﬁnally to inverse problem. This is accomplished by assuming that there are a sufﬁcient number of measurements from some sensors for f(x; γ), and then as the number of sensors measurements for k(x; γ) is decreased, the number of sensors measurements on u(x; γ) is increased, and thus a forward problem is obtained when there are only sensors for k and not for u, while an inverse problem has to be solved when there are only sensors for u and not for k.

In order to characterizing shape changes (morphodynamics) for cell-drug interactions, Cavanagh et al (2021) use kernel density estimation (KDE) for translating morphspace embeddings into probability density functions (PDFs). Then they use a top-down Fokker-Planck model of diﬀusive development over Waddington-type landscapes, with a PINN learning such landscapes by ﬁtting the PDFs to the Fokker–Planck equation. The architecture includes a neural network for each condition to learn: the PDF, diﬀusivity, and landscape. All parameters are ﬁtted using approximate Bayesian computing with sequential Monte Carlo (aBc-SMC) methods: in this case, aBc selects parameters from a prior distribution and runs simulations; if the simulations match the data within a certain level of similarity, the parameters are saved. So the posterior distribution is formed by the density over the stored parameters (Cavanagh

- et al, 2021).


#### 3.4 Solving a diﬀerential problem with PINN

Finally, this subsection discusses a realistic example of a 1D nonlinear Shro¨dinger (NLS) problem, as seen in Figure 3. The nonlinear problem is the same presented in Raissi (2018); Raissi et al (2017c), used to demonstrate the PINN’s ability to deal with periodic boundary conditions and complex-valued solutions.

Starting from an initial state ψ(x,0) = 2 sech(x) and assuming periodic boundary conditions equation (10) with all boundary conditions results in the

![image 3](Cuomo et al._2022_Scientific Machine Learning through Physics-Informed Neural Networks Where we are and What's next_images/imageFile3.png)

![image 4](Cuomo et al._2022_Scientific Machine Learning through Physics-Informed Neural Networks Where we are and What's next_images/imageFile4.png)

- Fig. 3: 1D nonlinear Shr¨dinger (NLS) solution module |ψ¯|. The solution is generated with Chebfun open-source software (Driscoll et al, 2014) and used as a reference solution. We also show the solution at three diﬀerent time frames, t = π8, π4, 38π. We expect the solution to be symmetric with respect to π4.


initial boundary value problem, given a domain Ω = [−5,5]×(0,T] written as:

 

iψt + 0.5ψxx + |ψ|2ψ = 0 (x,t) ∈ Ω ψ(0,x) = 2 sech(x) x ∈ [−5,5]

(11)

ψ(t,−5) = ψ(t,5) t ∈ (0,T] ψx(t,−5) = ψx(t,5) t ∈ (0,T]



where T = π/2.

To assess the PINN’s accuracy, Raissi et al (2017c) created a high-resolution data set by simulating the Schr¨dinger equation using conventional spectral methods. The authors integrated the Schr¨dinger equation up to a ﬁnal time T = π/2 using the MATLAB based Chebfun open-source software (Driscoll et al, 2014).

The PINN solutions are trained on a subset of measurements, which includes initial data, boundary data, and collocation points inside the domain. The initial time data, t = 0, are {xi0,ψ0i}N

###### i=1, the boundary collocation points are {tib}N

0

###### i=1, and the collocation points on F(t,x) are {tic,xic}N

i=1. In Raissi et al (2017c) a total of N0 = 50 initial data points on ψ(x,0) are randomly sampled from the whole high-resolution data-set to be included in the training set, as well as Nb = 50 randomly sampled boundary points to enforce the periodic boundaries. Finally for the solution domain, it is assumed Nc = 20 000 randomly sampled collocation points.

b

c

The neural network architecture has two inputs, one for the time t and the other one the location x, while the output has also length 2 rather than 1, as it would normally be assumed, because the output of this NN is expected to ﬁnd the real and imaginary parts of the solution.

The network is trained in order to minimize the losses due to the initial and boundary conditions, LB, as well as to satisfy the Schrodinger equation on the collocation points, i.e. LF. Because we are interested in a model that

is a surrogate for the PDE, no extra data, Ldata = 0, is used. In fact we only train the PINN with the known data point from the initial time step t = 0. So the losses of (6) are:

N0

1 N0

|ψ(0,xi0) − ψ0i|2+

LB =

i=1

Nb

1 Nb

|ψi(tib,−5) − ψi(tib,5)|2 + |ψxi (tib,−5) − ψxi (tib,5)|2

i=1

and

Nc

1 Nc

|F(tic,xic)|2.

LF =

i=1

The Latin Hypercube Sampling technique (Stein, 1987) is used to create all randomly sampled points among the benchmark data prior to training the NN.

In our training we use Adam, with a learning rate of 10−3, followed by a ﬁnal ﬁne-tuning with LBFGS. We then explore diﬀerent settings and architectures as in Table 2, by analysing the Mean Absolute Error (MAE) and Mean Squared Error (MSE). We used the PyTorch implementation from Stiller et al (2020) which is accessible on GitHub. While the benchmark solutions are from the GitHub of Raissi et al (2017c).

Raissi et al (2017c) ﬁrst used a DNN with 5 layers each with 100 neurons per layer and a hyperbolic tangent activation function in order to represent the unknown function ψ for both real and imaginary parts. In our test, we report the original conﬁguration but we also analyze other network architectures and training point amounts.

A comparison of the predicted and exact solutions at three diﬀerent temporal snapshots is shown in Figures 3, and 4. All the diﬀerent conﬁgurations reported in Table 2 show similar patterns of Figure 4, the only diﬀerence is in the order of magnitude of the error.

In particular in such Figure, we show the best conﬁguration obtained in our test, with an average value of 5,17·10−04 according to the MSE. Figure 4 ﬁrst shows the modulus of the predicted spatio-temporal solution |ψ(x,t)|, with respect to the benchmark solution, by plotting the error at each point. This PINN has some diﬃculty predicting the central height around (x,t) = (0,π/4), as well as in mapping value on in t ∈ (π/4,π/2) that are symmetric to the time interval t ∈ (0,π/4).

Finally, in Table 2, we present the results of a few runs in which we analyze what happens to the training loss, relative L2, MAE, and MSE when we vary the boundary data, and initial value data. In addition, we can examine how the error grows as the solution progresses through time.

![image 5](Cuomo et al._2022_Scientific Machine Learning through Physics-Informed Neural Networks Where we are and What's next_images/imageFile5.png)

![image 6](Cuomo et al._2022_Scientific Machine Learning through Physics-Informed Neural Networks Where we are and What's next_images/imageFile6.png)

- Fig. 4: PINN solutions of the 1D nonlinear Shr¨dinger (NLS) problem. As illustrated in the ﬁrst image, the error is represented as the diﬀerence among the benchmark solution and PINN result, whereas the second image depicts the PINN’s solution at three independent time steps: t = π/8,π/4,3/8π. In this case, we would have expected the solution to overlap at both π/8 and 3/8π, but there isn’t a perfect adherence; in fact, the MSE is 5,17 · 10−04 in this case, with some local peak error of 10−01 in the second half of the domain.


###### N0 Nb Nc Training loss relative L2 MAE MSE

40 50 20000 9 × 10−4 0.025 ± 0.003 0.065 ± 0.004 0.019 ± 0.002 40 100 20000 1 × 10−3 0.024 ± 0.002 0.065 ± 0.003 0.019 ± 0.002 80 50 20000 6 × 10−4 0.007 ± 0.001 0.035 ± 0.004 0.005 ± 0.001 80 100 20000 6 × 10−4 0.006 ± 0.002 0.033 ± 0.005 0.005 ± 0.002

- (a) Case where the NN is ﬁxed with 100 neurons per layer and four hidden layers. Only the number the number of training points on boundary conditions are doubled.

time t relative L2 MAE MSE

0 (5 ± 1) × 10−4 0.012 ± 0.002 (4 ± 1) × 10−4

- 0.39 (15 ± 5) × 10−4 0.015 ± 0.002 (12 ± 4) × 10−3

- 0.79 0.009 ± 0.003 0.038 ± 0.006 0.007 ± 0.003
- 1.18 0.01 ± 0.004 0.051 ± 0.009 0.009 ± 0.003


- 1.56 0.005 ± 0.001 0.044 ± 0.005 0.004 ± 0.001


- (b) Error behavior at various time steps for the best occurrence in Table, when a, where N0 = 80, Nb = 100, Nc = 20000.


- Table 2: Two subtables exploring the eﬀect of the amount of data points on convergence for PINN and the inherent problems of vanilla pINN to adhere to the solution for longer time intervals, in solving the 1D nonlinear Shr¨dinger (NLS) equation (11). In a, the NN consists of four layers, each of which contains 100 neurons, and we can observe how increasing the number of training points over initial or boundary conditions will decrease error rates. Furthermore, doubling the initial condition points has a much more meaningful inﬂuence impact than doubling the points on the spatial daily domain in this problem setup. In b, diven the best NN, we can observe that a vanilla PINN has diﬃculties in maintaining a strong performance overall the whole space-time domain, especially for longer times, this issue is a matter of research discussed in 5.3. All errors, MAE, MSE and L2-norm Rel are average over 10 runs. For all setups, the same optimization parameters are used, including training with 9000 epochs using Adam with a learning rate of 0.001 and a ﬁnal L-BFGS ﬁne-tuning step.


### 4 PINNs: Data, Applications and Software

The preceding sections cover the neural network component of a PINN framework and which equations have been addressed in the literature. This section ﬁrst discusses the physical information aspect, which is how the data and model are managed to be eﬀective in a PINN framework. Following that, we’ll look at some of the real-world applications of PINNs and how various soft-

- ware packages such as DeepXDE, NeuralPDE, NeuroDiﬀEq, and others were launched in 2019 to assist with PINNs’ design.


#### 4.1 Data

The PINN technique is based not only on the mathematical description of the problems, embedded in the loss or the NN, but also on the information used to train the model, which takes the form of training points, and impacts the quality of the predictions. Working with PINNs requires an awareness of the challenges to be addressed, i.e. knowledge of the key constitutive equations, and also experience in Neural Network building.

Moreover, the learning process of a PINN can be inﬂuenced by the relative magnitudes of the diﬀerent physical parameters. For example to address this issue, Kissas et al (2020) used a non-dimensionalization and normalization technique.

However, taking into account the geometry of the problem can be done without eﬀort. PINNs do not require ﬁxed meshes or grids, providing greater ﬂexibility in solving high-dimensional problems on complex-geometry domains. The training points for PINNs can be arbitrarily distributed in the spatiotemporal domain (Pang et al, 2019). However, the distribution of training points inﬂuences the ﬂexibility of PINNs. Increasing the number of training points obviously improves the approximation, although in some applications, the location of training places is crucial. Among the various methods for selecting training points, Pang et al (2019) addressed lattice-like sampling, i.e. equispaced, and quasi-random sequences, such as the Sobol sequences or the Latin hypercube sampling.

Another key property of PINN is its ability to describe latent nonlinear state variables that are not observable. For instance, Zhang et al (2020) observed that when a variable’s measurement was missing, the PINN implementation was capable of accurately predicting that variable.

#### 4.2 Applications

In this section, we will explore the real-world applications of PINNs, focusing on the positive leapfrog applications and innovation that PINNs may bring to our daily lives, as well as the implementation of such applications, such as the ability to collect data in easily accessible locations and simulate dynamics in other parts of the system, or applications to hemodynamics ﬂows, elastic models, or geoscience.

Hemodynamics Three ﬂow examples in hemodynamics applications are presented in Sun et al

- (2020a), for addressing either stenotic ﬂow and aneurysmal ﬂow, with standardized vessel geometries and varying viscosity. In the paper, they not only validate the results against CFD benchmarks, but they also estimate the solutions of the parametric Navier–Stokes equation without labeled data by designing a DNN that enforces the initial and boundary conditions and training the DNN by only minimizing the loss on conservation equations of mass and momentum.


In order to extract velocity and pressure ﬁelds directly from images, Raissi et al (2020) proposed the Hidden ﬂuid mechanics (HFM) framework. The general structure could be applied for electric or magnetic ﬁelds in engineering and biology. They speciﬁcally apply it to hemodynamics in a three-dimensional intracranial aneurysm.

Patient-speciﬁc systemic artery network topologies can make precise predictions about ﬂow patterns, wall shear stresses, and pulse wave propagation. Such typologies of systemic artery networks are used to estimate Windkessel model parameters (Kissas et al, 2020). PINN methodology is applied on a simpliﬁed form of the Navier–Stokes equations, where a hyperbolic conservation law deﬁnes the evolution of blood velocity and cross-sectional area instead of mass and momentum conservation. Kissas et al (2020) devise a new method for creating 3D simulations of blood ﬂow: they estimate pressure and retrieve ﬂow information using data from medical imaging. Pre-trained neural network models can quickly be changed to a new patient condition. This allows Windkessel parameters to be calculated as a simple post-processing step, resulting in a straightforward approach for calibrating more complex models. By processing noisy measurements of blood velocity and wall displacement, Kissas et al (2020) present a physically valid prediction of ﬂow and pressure wave propagation derived directly from non-invasive MRI ﬂow. They train neural networks to provide output that is consistent with clinical data.

###### Flows problems

Mathews et al (2021) observe the possibility to infer 3D turbulent ﬁelds from only 2D data. To infer unobserved ﬁeld dynamics from partial observations of synthetic plasma, they simulate the drift-reduced Braginskii model using physics-informed neural networks (PINNs) trained to solve supervised learning tasks while preserving nonlinear partial diﬀerential equations. This paradigm is applicable to the study of quasineutral plasmas in magnetized collisional situations and provides paths for the construction of plasma diagnostics using artiﬁcial intelligence. This methodology has the potential to improve the direct testing of reduced turbulence models in both experiment and simulation in ways previously unattainable with standard analytic methods. As a result, this deep learning technique for diagnosing turbulent ﬁelds is simply transferrable, allowing for systematic application across magnetic conﬁnement fusion experiments. The methodology proposed in Mathews et al (2021) can be adapted

to many contexts in the interdisciplinary research (both computational and experimental) of magnetized collisional plasmas in propulsion engines and astrophysical environments.

Xiao et al (2020) examine existing turbulent ﬂow databases and proposes benchmark datasets by methodically changing ﬂow conditions.

In the context of high-speed aerodynamic ﬂows, Mao et al (2020), investigates Euler equations solutions approximated by PINN. The authors study both forward and inverse, 1D and 2D, problems. As for inverse problems, they analyze two sorts of problems that cannot be addressed using conventional approaches. In the ﬁrst problem they determine the density, velocity, and pressure using data from the density gradient; in the second problem, they determine the value of the parameter in a two-dimensional oblique wave equation of state by providing density, velocity, and pressure data.

Projecting solutions in time beyond the temporal area used in training is hard to address with the vanilla version of PINN, and such problem is discussed and tested in Kim et al (2021a). The authors show that vanilla PINN performs poorly on extrapolation tasks in a variety of Burges’ equations benchmark problems, and provide a novel NN with a diﬀerent training approach.

PINN methodology is also used also to address the 1D Buckley-Leverett two-phase problem used in petroleum engineering that has a non-convex ﬂow function with one inﬂection point, making the problem quite complex (Abreu and Florindo, 2021). Results are compared with those obtained by the Lagrangian-Eulerian and Lax-Friedrichs schemes.

Finally, Buckley-Leverett’s problem is also addressed in Almajid and AbuAl-Saud (2022), where PINN is compared to an ANN without physical loss: when only early-time saturation proﬁles are provided as data, ANN cannot predict the solution.

###### Optics and Electromagnetic applications

The hybrid PINN from Fang (2021), based on CNN and local ﬁtting method, addresses applications such as the 3-D Helmholtz equation, quasi-linear PDE operators, and inverse problems. Additionally, the author tested his hybrid PINN on an icosahedron-based mesh produced by Meshzoo for the purpose of solving surface PDEs.

A PINN was also developed to address power system applications (Misyris

- et al, 2020) by solving the swing equation, which has been simpliﬁed to an ODE. The authors went on to expand on their research results in a subsequent study (Stiasny et al, 2021).


In (Kovacs et al, 2022) a whole class of microelectromagnetic problems is addressed with a single PINN model, which learns the solutions of classes of eigenvalue problems, related to the nucleation ﬁeld associated with defects in magnetic materials.

In Chen et al (2020b), the authors solve inverse scattering problems in photonic metamaterials and nano-optics. They use PINNs to retrieve the eﬀective permittivity characteristics of a number of ﬁnite-size scattering systems

involving multiple interacting nanostructures and multi-component nanoparticles. Approaches for building electromagnetic metamaterials are explored in Fang and Zhan (2020a). E.g. cloaking problem is addressed in both Fang and Zhan (2020a); Chen et al (2020b). A survey of DL methodologies, including PINNs, applied to nanophotonics may be found in Wiecha et al (2021).

As a benchmark problem for DeepM&Mnet, Cai et al (2021b) choose electroconvection, which depicts electrolyte ﬂow driven by an electric voltage and involves multiphysics, including mass, momentum, cation/anion transport, and electrostatic ﬁelds.

###### Molecular dynamics and materials related applications

Long-range molecular dynamics simulation is addressed with multi-ﬁdelity PINN (MPINN) by estimating nanoﬂuid viscosity over a wide range of sample space using a very small number of molecular dynamics simulations Islam et al

- (2021). The authors were able to estimate system energy per atom, system pressure, and diﬀusion coeﬃcients, in particular with the viscosity of argoncopper nanoﬂuid. PINNs can recreate fragile and non-reproducible particles, as demonstrated by Stielow and Scheel (2021), whose network reconstructs the shape and orientation of silver nano-clusters from single-shot scattering images. An encoder-decoder architecture is used to turn 2D images into 3D object space. Following that, the loss score is computed in the scatter space rather than the object space. The scatter loss is calculated by computing the mean-squared diﬀerence error between the network prediction and the target’s dispersion pattern. Finally, a binary loss is applied to the prediction in order to reinforce the physical concept of the problem’s binary nature. They also discover novel geometric shapes that accurately mimic the experimental scattering data.


A multiscale application is done in Lin et al (2021a,b), where the authors describe tiny bubbles at both the continuum and atomic levels, the former level using the Rayleigh–Plesset equation and the latter using the dissipative particle dynamics technique. In this paper, the DeepONet architecture (Lu

- et al, 2021a) is demonstrated to be capable of forecasting bubble growth on the ﬂy across spatial and temporal scales that diﬀer by four orders of magnitude.


###### Geoscience and elastostatic problems

Based on F¨ppl–von K´rma´n (FvK) equations, Li et al (2021) test their model to four loading cases: in-plane tension with non-uniformly distributed stretching forces, central-hole in-plane tension, deﬂection out-of-plane, and compression buckling. Moreover stress distribution and displacement ﬁeld in solid mechanics problems was addressed by Haghighat and Juanes (2021).

For earthquake hypocenter inversion, Smith et al (2021b) use Stein variational inference with a PINN trained to solve the Eikonal equation as a forward model, and then test the method against a database of Southern California earthquakes.

###### Industrial application

A broad range of applications, particularly in industrial processes, extends the concept of PINN by adapting to circumstances when the whole underlying physical model of the process is unknown.

The process of lubricant deterioration is still unclear, and models in this ﬁeld have signiﬁcant inaccuracies; this is why Yucesan and Viana (2021) introduced a hybrid PINN for main bearing fatigue damage accumulation calibrated solely through visual inspections. They use a combination of PINN and ordinal classiﬁer called discrete ordinal classiﬁcation (DOrC) approach. The authors looked at a case study in which 120 wind turbines were inspected once a month for six months and found the model to be accurate and error-free. The grease damage accumulation model was also trained using noisy visual grease inspection data. Under fairly conservative ranking, researchers can utilize the derived model to optimize regreasing intervals for a particular useful life goal. As for, corrosion-fatigue crack growth and bearing fatigue are examples studied in Viana et al (2021).

For simulating heat transmission inside a channel, Modulus from NVIDIA (Hennigh et al, 2021) trains on a parametrized geometry with many design variables. They speciﬁcally change the ﬁn dimensions of the heat sink (thickness, length, and height) to create a design space for various heat sinks (NVIDIA Corporation, 2021). When compared to traditional solvers, which are limited to single geometry simulations, the PINN framework can accelerate design optimization by parameterizing the geometry. Their ﬁndings make it possible to perform more eﬃcient design space search tasks for complex systems (Cai

- et al, 2021c).


#### 4.3 Software

Several software packages, including DeepXDE (Lu et al, 2021b), NVIDIA Modulus (previously SimNet) (Hennigh et al, 2021), PyDEns (Koryagin et al, 2019), and NeuroDiﬀEq (Chen et al, 2020a) were released in 2019 to make training PINNs easier and faster. The libraries all used feed-forward NNs and the automatic diﬀerentiation mechanism to compute analytical derivatives necessary to determine the loss function. The way packages deal with boundary conditions, whether as a hard constraint or soft constraint, makes a signiﬁcant diﬀerence. When boundary conditions are not embedded in the NN but are included in the loss, various losses must be appropriately evaluated. Multiple loss evaluations and their weighted sum complicate hyper-parameter tuning, justifying the need for such libraries to aid in the design of PINNs.

More libraries have been built in recent years, and others are being updated on a continuous basis, making this a dynamic ﬁeld of research and development. In this subsection, we will examine each library while also presenting a comprehensive synthesis in Table 3.

###### DeepXDE

DeepXDE (Lu et al, 2021b) was one of the initial libraries built by one of the vanilla PINN authors. This library emphasizes its problem-solving capability, allowing it to combine diverse boundary conditions and solve problems on domains with complex geometries. They also present residual-based adaptive reﬁnement (RAR), a strategy for optimizing the distribution of residual points during the training stage that is comparable to FEM reﬁnement approaches. RAR works by adding more points in locations where the PDE residual is larger and continuing to add points until the mean residual is less than a threshold limit. DeepXDE also supports complex geometry domains based on the constructive solid geometry (CSG) technique. This package showcases ﬁve applications in its ﬁrst version in 2019, all solved on scattered points: Poisson Equation across an L-shaped Domain, 2D Burgers Equation, ﬁrstorder Volterra integrodiﬀerential equation, Inverse Problem for the Lorenz System, and Diﬀusion-Reaction Systems.

Since the package’s initial release, a signiﬁcant number of other articles have been published that make use of it. DeepXDE is used by the authors for: for inverse scattering (Chen et al, 2020b), or deriving mechanical characteristics from materials with MFNNs (Lu et al, 2020). While other PINNs are implemented using DeepXDE, like hPINN (Kharazmi et al, 2021b). Furthermore, more sophisticated tools are built on DeepXDE, such as DeepONets (Lu et al, 2021a), and its later extension DeepM&Mnet (Cai et al, 2021b; Mao

- et al, 2021). DeepONets and their derivatives are considered by the authors to have the signiﬁcant potential in approximating operators and addressing multi-physics and multi-scale problems, like inferring bubble dynamics (Lin et al, 2021a,b).


Finally, DeepXDE is utilized for medical ultrasonography applications to simulate a linear wave equation with a single time-dependent sinusoidal source function (Alkhadhr et al, 2021), and the open-source library is also employed for the Buckley-Leverett problem (Almajid and Abu-Al-Saud, 2022). A list of research publications that made use of DeepXDE is available online 1 .

###### NeuroDiﬀEq

NeuroDiﬀEq (Chen et al, 2020a) is a PyTorch-based library for solving differential equations with neural networks, which is being used at Harvard IACS. NeuroDiﬀEq solves traditional PDEs (such as the heat equation and the Poisson equation) in 2D by imposing strict constraints, i.e. by fulﬁlling initial/boundary conditions via NN construction, which makes it a PCNN. They employ a strategy that is similar to the trial function approach (Lagaris et al, 1998), but with a diﬀerent form of the trial function. However, because NeuroDiﬀEq enforces explicit boundary constraints rather than adding the corresponding losses, they appear to be inadequate for arbitrary bounds that the library does not support (Balu et al, 2021).

1https://deepxde.readthedocs.io/en/latest/user/research.html

###### Modulus

Modulus (NVIDIA Corporation, 2021), previously known as NVIDIA SimNet (Hennigh et al, 2021), from Nvidia, is a toolset for academics and engineers that aims to be both an extendable research platform and a problem solver for real-world and industrial challenges.

It is a PINN toolbox with support to Multiplicative Filter Networks and a gradient aggregation method for larger batch sizes. Modulus also oﬀers Constructive Solid Geometry (CSG) and Tessellated Geometry (TG) capabilities, allowing it to parameterize a wide range of geometries.

In terms of more technical aspects of package implementations, Modulus uses an integral formulation of losses rather than a summation as is typically done. Furthermore, global learning rate annealing is used to ﬁne-tune the weights parameters ω in the loss equation 6. Unlike many other packages, Modulus appears to be capable of dealing with a wide range of PDE in either strong or weak form. Additionally, the toolbox supports a wide range of NN, such as Fourier Networks and the DGM architecture, which is similar to the LSTM architecture.

Nvidia showcased the PINN-based code to address multiphysics problems like heat transfer in sophisticated parameterized heat sink geometry (Cheung and See, 2021), 3D blood ﬂow in Intracranial Aneurysm or address data assimilation and inverse problems on a ﬂow passing a 2D cylinder (NVIDIA Corporation, 2021). Moreover, Modulus solves the heat transport problem more quickly than previous solvers.

###### SciANN

SciANN (Haghighat and Juanes, 2021) is an implementation of PINN as a high-level Keras wrapper. Furthermore, the SciANN repository collects a wide range of examples so that others can replicate the results and use those examples to build other solutions, such as elasticity, structural mechanics, and vibration applications. SciANN is used by the same authors also for creating a nonlocal PINN method in Haghighat et al (2021a), or for a PINN multinetwork model applied on solid mechanics (Haghighat et al, 2021b). Although tests for simulating 2D ﬂood, on Shallow Water Equations, are conducted using SciANN (Jamali et al, 2021), the authors wrote the feedforward step into a separate function to avoid the overhead associated with using additional libraries. A general comparison of many types of mesh-free surrogate models based on machine learning (ML) and deep learning (DL) methods is presented in Hoﬀer et al (2021), where SciANN is used among other toolsets. Finally, the PINN framework for solving the Eikonal equation by Waheed et al (2021) was implemented using SciAnn.

###### PyDENs

PyDENs (Koryagin et al, 2019) is an open-source neural network PDE solver that allows to deﬁne and conﬁgure the solution of heat and wave equations. It

impose initial/boundary conditions in the NN, making it a PCNN. After the ﬁrst release in 2019, the development appears to have stopped in 2020.

###### NeuralPDE.jl

NeuralPDE.jl is part of SciML, a collection of tools for scientiﬁc machine learning and diﬀerential equation modeling. In particular SciML (Scientiﬁc Machine Learning) (Rackauckas et al, 2021) is a program written in Julia that combines physical laws and scientiﬁc models with machine learning techniques.

###### ADCME

ADCME (Xu and Darve, 2020) can be used to develop numerical techniques and connect them to neural networks: in particular, ADCME was developed by extending and enhancing the functionality of TensorFlow. In Xu and Darve (2020), ADCME is used to solve diﬀerent examples, like nonlinear elasticity, Stokes problems, and Burgers’ equations. Furthermore, ADCME is used by Xu and Darve (2021) for solving inverse problems in stochastic models by using a neural network to approximate the unknown distribution.

###### Nangs

Nangs (Pedro et al, 2019) is a Python library that uses the PDE’s independent variables as NN (inputs), it then computes the derivatives of the dependent variables (outputs), with the derivatives they calculate the PDEs loss function used during the unsupervised training procedure. It has been applied and tested on a 1D and 2D advection-diﬀusion problem. After a release in 2020, the development appears to have stopped. Although, NeuroDiﬀEq and Nangs libraries were found to outperform PyDEns in solving higher-dimensional PDEs (Pratama et al, 2021).

###### TensorDiﬀEq

TensorDiﬀEq (McClenny et al, 2021) is a Scientiﬁc Machine Learning PINN based toolkit on Tensorﬂow for Multi-Worker Distributed Computing. Its primary goal is to solve PINNs (inference) and inverse problems (discovery) eﬃciently through scalability. It implements a Self-Adaptive PINN to increase the weights when the corresponding loss is greater; this task is accomplished by training the network to simultaneously minimize losses and maximize weights.

###### IDRLnet

IDRLnet (Peng et al, 2021) is a Python’s PINN toolbox inspired by Nvidia SimNet (Hennigh et al, 2021). It provides a way to mix geometric objects, data sources, artiﬁcial neural networks, loss metrics, and optimizers. It can also solve noisy inverse problems, variational minimization problem, and integral diﬀerential equations.

###### Elvet

Elvet (Araz et al, 2021) is a Python library for solving diﬀerential equations and variational problems. It can solve systems of coupled ODEs or PDEs (like the quantum harmonic oscillator) and variational problems involving minimization of a given functional (like the catenary or geodesics solutions-based problems).

###### Other packages

Packages that are speciﬁcally created for PINN can not only solve problems using PINN, but they can also be used to provide the groundwork for future research on PINN developments. However, there are other packages that can take advantage of future research developments, such as techniques based on kernel methods (Karniadakis et al, 2021). Indeed, rather than switching approaches on optimizers, losses, and so on, an alternative approach with respect to PINN framework is to vary the way the function is represented. Throughout this aspect, rather than using Neural Networks, a kernel method based on Gaussian process could be used. The two most noteworthy Gaussian processes toolkit are the Neural Tangents (Novak et al, 2020) kernel (NTK), based on JAX, and GPyTorch (Gardner et al, 2018), written using PyTorch. Neural Tangents handles inﬁnite-width neural networks, allowing for the speciﬁcation of intricate hierarchical neural network topologies. While GPyTorch models Gaussian processes based on Blackbox Matrix-Matrix multiplication using a speciﬁc preconditioner to accelerate convergence.

### 5 PINN Future Challenges and directions

What comes next in the PINN theoretical or applied setup is unknown. What we can assess here are the paper’s incomplete results, which papers assess the most controversial aspects of PINN, where we see unexplored areas, and where we identify intersections with other disciplines.

Although several articles have been published that have enhanced PINNs capabilities, there are still numerous unresolved issues, such as various applications to real-world situations and equations. These span from more theoretical considerations (such as convergence and stability) to implementation issues (boundary conditions management, neural networks design, general PINN architecture design, and optimization aspects). PINNs and other DL methods using physics prior have the potential to be an eﬀective way of solving highdimensional PDEs, which are signiﬁcant in physics, engineering, and ﬁnance. PINNs, on the other hand, struggle to accurately approximate the solution of PDEs when compared to other numerical methods designed for a speciﬁc PDE, in particular, they can fail to learn complex physical phenomena, like solutions that exhibit multi-scale, chaotic, or turbulent behavior.

2022 neural-tangents

26,2022 NeuralPDE.jl

2021 TensorDiﬀEq

version CodeLink

12,2021 neurodiﬀeq

2021 ADCME.jl

2021 gpytorch

25,2022 modulus

2022 deepxde

2022 pydens

2021 idrlnet

21 sciann

Dec5,2021 nangs

2021 elvet

2019 v1.4.0May20,

27,2019 v0.7.3May22,

2021 v0.2.0-Nov17

Jul05,2021 v0.0.1Jul21,

21,2019 v0.6.5.0Sep9

2019 v0.5.0-Feb23,

2020 v2021.12.6-

2019 v4.9.0-May

Oct02,2018 v1.6.0Dec04,

24,2019 v0.5.2onDec

14,2019 v1.0.2-Jan20,

9,2021 v22.03onApr

2021 v1.0.0Mar29,

Table3:Majorsoftwarelibrariesspeciﬁcallydesignedforphysics-informedmachinelearning

SoftwareNameBackendAvailableforUsageLicenseFirstreleaseLatest

ADCMEXuandDarve(2020)JuliaTensorFlowJuliaWrapperMITLicensevalpha-Aug

NeuralTangentsNovaketal(2020)JAXPythonWrapperApache-2.0Licensev0.1.1Nov11,

TensorDiﬀEqMcClennyetal(2021)Tensorﬂow2.xPythonSolverMITLicensev0.1.0-Feb03,

NVIDIAModulusHennighetal(2021)TensorFlowPythonbasedAPISolverProprietaryv21.06onNov

NeuroDiﬀEqChenetal(2020a)PyTorchPythonSolverMITLicensevalpha-Mar

PyDEnsKoryaginetal(2019)TensorﬂowPythonSolverApache-2.0Licensevalpha-Jul

DeepXDELuetal(2021b)TensorFlowPythonSolverApache-2.0Licensev0.1.0-Jun13,

ElvetArazetal(2021)TensorﬂowPythonSolverMITLicensev0.1.0Mar26,

NangsPedroetal(2019)PytorchPythonSolverApache-2.0Licensev0.0.1-Jan9,

GPyTorchGardneretal(2018)PyTorchPythonWrapperMITLicensev0.1.0alpha

NeuralPDEZubovetal(2021a)JuliaJuliaSolverMITLicensev0.0.1-Jun22,

SciANNHaghighatandJuanes(2021)TensorFlowPython2.7-3.6WrapperMITLicensevalpha-Jul

IDRLnetPengetal(2021)PyTorch,SympyPythonSolverApache-2.0Licensev0.0.1-alpha

Scientiﬁc Machine Learning through PINNs 55

#### 5.1 Overcoming theoretical diﬃculties in PINN

A PINN can be thought of as a three-part modular structure, with an approximation (the neural network), a module to deﬁne how we want to correct the approximation (the physics informed network, i.e. the loss), and the module that manages the minimization of the losses. The NN architecture deﬁnes how well the NN can approximate a function, and the error we make in approximating is called approximation error, as seen in Section 2.4. Then, how we decide to iteratively improve the approximator will be determined by how we deﬁne the loss and how many data points we are integrating or calculating the sum, with the quality of such deviation measured as the generalization error. Finally, the quality of iterations in minimizing the losses is dependent on the optimization process, which gives the optimization error.

All of these factors raise numerous questions for future PINN research, the most important of which is whether or not PINN converges to the correct solution of a diﬀerential equation. The approximation errors must tend to zero to achieve stability, which is inﬂuenced by the network topology. The outcomes of this research are extremely limited. For example, the relative error for several neural architectures was calculated by altering the number of hidden layers and the number of neurons per layer in Mo et al (2022). In another example, Blechschmidt and Ernst (2021) shows the number of successes (i.e. when training loss that is less than a threshold) after ten diﬀerent runs and for different network topologies (number of layers, neurons, and activation function). Instead, Mishra and Molinaro (2021a) obtain error estimates and identify possible methods by which PINNs can approximate PDEs. It seems that initial hidden layers may be in charge of encoding low-frequency components (fewer points are required to represent low-frequency signals) and the subsequent hidden layers may be in charge of representing higher-frequency components (Markidis, 2021). This could be an extension of the Frequency-principle, Fprinciple (Zhi-Qin et al, 2020), according to which DNNs ﬁt target functions from low to high frequencies during training, implying a low-frequency bias in DNNs and explaining why DNNs do not generalize well on randomized datasets. For PINN, large-scale features should arise ﬁrst while small-scale features will require multiple training epochs.

The eﬀects of initialization and loss function on DNN learning, speciﬁcally on generalization error, should be investigated. Many theoretical results treat loos estimation based on quadrature rules, on points selected randomly and identically distributed. There are some PINN approaches that propose to select collocations points in speciﬁc areas of the space-time domain (Nabian et al,

- 2021); this should be investigated as well. Finally, dynamic loss weighting for PINN appears to be a promising research direction (Nandi et al, 2022).


Optimization tasks are required to improve the performances of NNs, which also holds for PINN. However, given the physical integration, this new PINN methodology will require additional theoretical foundations on optimization and numerical analysis, and dynamical systems theory. According to (Wang

et al, 2021b, 2022b), a key issue is to understand the relationship between PDE stiﬀness and the impact of algorithms as the gradient descent on the PINNs.

Another intriguing research topic is why PINN does not suﬀer from dimensionality. According to the papers published on PINN, they can scale up easily independently of the size of the problems (Mishra and Molinaro, 2021b). The computational cost of PINN does not increase exponentially as the problem dimensionality increases; this property is common to neural network architecture, and there is no formal explanation for such patterns (De Ryck and Mishra, 2021). Bauer and Kohler (2019) recently demonstrated that least-squares estimates based on FNN can avoid the curse of dimensionality in nonparametric regression. While Zubov et al (2021b) demonstrates the capability of the PINN technique with quadrature methods in solving high dimensional problems.

In PINN the process of learning gives rise to a predictor, uθ, which minimizes the empirical risk (loss). In machine learning theory, the prediction error can be divided into two components: bias error and variance error. The bias-variance trade-oﬀ appears to contradict the empirical evidence of recent machine-learning systems when neural networks trained to interpolate training data produce near-optimal test results. It is known that a model should balance underﬁtting and overﬁtting, as in the typical U curve, according to the bias-variance trade-oﬀ. However, extremely rich models like neural networks are trained to exactly ﬁt (i.e., interpolate) the data. Belkin et al (2019), demonstrate the existence of a double-descent risk curve across a wide range of models and datasets, and they oﬀer a mechanism for its genesis. The behavior of PINN in such a framework of Learning Theory for Deep Learning remains to be investigated and could lead to further research questions. In particular, the function class H of the hypothesis space in which PINN is optimized might be further examined by specifying such space based on the type of diﬀerential equations that it is solving and thus taking into account the physics informed portion of the network.

In general, PINN can fail to approximate a solution, not due to the lack of expressivity in the NN architecture but due to soft PDE constraint optimization problems Krishnapriyan et al (2021).

#### 5.2 Improving implementation aspects in PINN

When developing a PINN, the PINN designer must be aware that there may be additional conﬁgurations that need to be thoroughly investigated in the literature, as well as various tweaks to consider and good practices that can aid in the development of the PINN, by systematically addressing each of the PINN’s three modules. From neural network architecture options to activation function type. In terms of loss development, the approaching calculation of the loss integral, as well as the implementation of the physical problem from adimensionalization or the solution space constrains. Finally, the best training procedure should be designed. How to implement these aspects at the most fundamental level, for each physical problem appears to be a matter of ongoing

research, giving rise to a diverse range of papers, which we addressed in this survey, and the missing aspects are summarized in this subsection.

Regarding neural networks architectures, there is still a lack of research for non FFNN types, like CNN and RNN, and what involves their theoretical impact on PINNs (Wang et al, 2022b); moreover, as for the FFNNs many questions remain, like implementations ones regarding the selection of network size (Haghighat et al, 2021a). By looking at Table 1, only a small subset of Neural Networks has been instigated as the network architecture for a PINN, and on a quite restricted set of problems. Many alternative architectures are proposed in the DL literature (Dargan et al, 2020), and PINN development can beneﬁt from this wide range of combinations in such research ﬁelds. A possible idea could be to apply Fourier neural operator (FNO) (Wen

- et al, 2022), in order to learn a generalized functional space (Raﬁq et al,


- 2022). N-BEATS (Oreshkin et al, 2020), a deep stack of fully connected layers connected with forward and backward residual links, could be used for time series based phenomena. Transformer architecture instead could handle long-range dependencies by modeling global relationships in complex physical problems (Kashinath et al, 2021). Finally, sinusoidal representation networks (SIRENs) Sitzmann et al (2020) that are highly suited for expressing complicated natural signals and their derivatives, could be used in PINN. Some preliminary ﬁndings are already available (Wong et al, 2022; Huang et al,


- 2021). A research line is to study if it is better to increase the breadth or depth of the FFNN to improve PINN outcomes. Some general studies on DNN make diﬀerent assertions about whether expanding width has the same beneﬁts as increasing depth. This may prompt the question of whether there is a minimum depth/width below which a network cannot understand the physics (Torabi Rad et al, 2020). The interoperability of PINN will also play an important role in future research (Rudin et al, 2022). A greater understanding of PINN’s activation function is needed. Jagtap et al (2020a) show that scalable activation function may be tuned to maximize network performance, in terms of convergence rate and solution correctness. Further research can look into alternative or hybrid methods of diﬀerentiating the diﬀerential equations. To speed up PINN training, the loss function in Chiu et al (2022) is deﬁned using numerical diﬀerentiation and automatic diﬀerentiation. The proposed can-PINN, i.e. coupled-automatic–numerical diﬀerentiation PINN, shows to be more sample eﬃcient and more accurate than traditional PINN; because PINN with automatic diﬀerentiation can only achieve high accuracy with many collocation points. While the PINNs training points can be distributed spatially and temporally, making them highly versatile, on the other hand, the position of training locations aﬀects the quality of the results. One downside of PINNs is that the boundary conditions must be established during the training stage, which means that if the boundary conditions change, a new network must be created (Wiecha et al, 2021).


As for the loss, it is important to note that a NN will always focus on minimizing the largest loss terms in the weighted equation, therefore all loss

terms must be of the same order of magnitude; increasing emphasis on one component of the loss may aﬀect other parts of it. There does not appear to be an objective method for determining the weight variables in the loss equation, nor does there appear to be a mechanism to assure that a certain equation can be solved to a predetermined tolerance before training begins; these are topics that still need to be researched (Nandi et al, 2021).

It seems there has been a lack of research on optimization tasks for PINNs. Not many solutions appear to be implemented, apart from standard solutions such as Adam and BFGS algorithms (Wong et al, 2021). The Adam algorithm generates a workﬂow that can be studied using dynamical systems theory, giving a gradient descent dynamic. More in detail, to reduce stiﬀness in gradient ﬂow dynamics, studying the limiting neural tangent kernel is needed. Given that there has been great work to solve optimization problems or improve these approaches in machine learning, there is still room for improvement in PINNs optimization techniques (Sun et al, 2020b). The L-BFGS-B is the most common BFGS used in PINNs, and it is now the most critical PINN technology Markidis (2021).

Moreover, the impact of learning rate on PINN training behavior has not been fully investigated. Finally, gradient normalization is another key research topic (Nandi et al, 2022). It is an approach that dynamically assigns weights to different constraints to remove the dominance of any component of the global loss function.

It is necessary to investigate an error estimation for PINN. One of the few examples comes from Hillebrecht and Unger (2022), where using an ODE, they construct an upper bound on the PINN prediction error. They suggest adding an additional weighting parameter to the physics-inspired part of the loss function, which allows for balancing the error contribution of the initial condition and the ODE residual. Unfortunately, only a toy example is oﬀered in this article, and a detailed analysis of the possibility of providing lower bounds on the error estimator needs still to be addressed, as well as an extension to PDEs.

#### 5.3 PINN in the SciML framework

PINNs, and SciML in general, hold a lot of potential for applying machine learning to critical scientiﬁc and technical challenges. However, many questions remain unsolved, particularly if neural networks are to be used as a replacement for traditional numerical methods such as ﬁnite diﬀerence or ﬁnite volume. In Krishnapriyan et al (2021) the authors analyze two basic PDE problems of diﬀusion and convection and show that PINN can fail to learn the ph problem physics when convection or viscosity coeﬃcients are high. They found that the PINN loss landscape becomes increasingly complex for large coeﬃcients. This is partly due to an optimization problem, because of the PINN soft constraint. However, lower errors are obtained when posing the problem as a sequence-to-sequence learning task instead of solving for the entire space-time at once. These kinds of challenges must be solved if

PINN has to be used beyond basic copy-paste by creating in-depth relations between the scientiﬁc problem and the machine learning approaches.

Moreover, unexpected uses of PINN can result from applying this framework to diﬀerent domains. PINN has been employed as linear solvers for the Poisson equation Markidis (2021), by bringing attention to the prospect of using PINN as linear solvers that are as quick and accurate as other highperformance solvers such as PETSc solvers. PINNs appear to have some intriguing advantages over more traditional numerical techniques, such as the Finite Element Method (FEM), as explained in Lu et al (2021b). Given that PINNs approximate functions and their derivatives nonlinearly, whereas FEM approximates functions linearly, PINNs appear to be well suited for broad use in a wide variety of engineering applications. However, one of the key disadvantages is the requirement to train the NN, which may take signiﬁcantly longer time than more extensively used numerical methods.

On the other hand, PINNs appear to be useful in a paradigm distinct from that of standard numerical approaches. PINNs can be deployed in an online-oﬄine fashion, with a single PINN being utilized for rapid evaluations of dynamics in real-time, improving predictions.Moving from 2D to 3D poses new obstacles for PINN. As training complexity grows in general, there is a requirement for better representation capacity of neural networks, a demand for a larger batch size that can be limited by GPU memory, and an increased training time to convergence (Nandi et al, 2021). Another task is to incorporate PINN into more traditional scientiﬁc programs and libraries written in Fortran and C/C++, as well as to integrate PINN solvers into legacy HPC applications (Markidis, 2021). PINN could also be implemented on Modern HPC Clusters, by using Horovod (Sergeev and Del Balso, 2018). Additionally, when developing the mathematical model that a PINN will solve, the user should be aware of pre-normalizing the problem. At the same time, packages can assist users in dealing with such problems by writing the PDEs in a symbolic form, for example, using SymPy.

PINNs have trouble propagating information from the initial condition or boundary condition to unseen areas of the interior or to future times as an iterative solver (Jin et al, 2021; Dwivedi and Srinivasan, 2020). This aspect has recently been addressed by Wang et al (2022a) that provided a reformulation of PINNs loss functions that may explicitly account for physical causation during model training. They assess that PINN training algorithms should be designed to respect how information propagates in accordance with the underlying rules that control the evolution of a given system. With the new implementation they observe considerable accuracy gains, as well as the possibility to assess the convergence of a PINNs model, and so PINN, can run for the chaotic Lorenz system, the Kuramoto–Sivashinsky equation in the chaotic domain, and the Navier–Stokes equations in the turbulent regime. However there is still research to be done for hybrid/inverse problems, where

observational data should be considered as point sources of information, and PDE residuals should be minimized at those points before propagating information outwards. Another approach is to use ensemble agreement as to the criterion for incorporating new points in the loss calculated from PDEs (Haitsiukevich and Ilin, 2022). The idea is that in the neighborhood of observed/initial data, all ensemble members converge to the same solution, whereas they may be driven towards diﬀerent incorrect solutions further away from the observations, especially or large time intervals.

PINN can also have a signiﬁcant impact on our daily lives, as for the example, from Yucesan and Viana (2021), where PINNs are used to anticipate grease maintenance; in the industry 4.0 paradigm, they can assist engineers in simulating materials and constructions or analyzing in real-time buildings structures by embedding elastostatic trained PINNs (Haghighat et al,

- 2021b; Minh Nguyen-Thanh et al, 2020). PINNs also fail to solve PDEs with high-frequency or multi-scale structure (Wang et al, 2022b, 2021b; Fuks and Tchelepi, 2020). The region of attraction of a speciﬁc equilibria of a given autonomous dynamical system could also be investigated with PINN (Scharzenberger and Hays, 2021).


However, to employ PINN in a safety-critical scenario it will still be important to analyze stability and focus on the method’s more theoretical component. Many application areas still require signiﬁcant work, such as the cultural heritage sector, the healthcare sector, ﬂuid dynamics, particle physics, and the modeling of general relativity with PINN. It will be important to develop a PINN methodology for stiﬀ problems, as well as use PINN in digital twin applications such as real-time control, cybersecurity, and machine health monitoring (Nandi et al, 2021). Finally, there is currently a lack of PINNs applications in multi-scale applications, particularly in climate modeling (Irrgang et al, 2021), although the PINN methodology has proven capable of addressing its capabilities in numerous applications such as bubble dynamics on multiple scales (Lin et al, 2021a,b).

#### 5.4 PINN in the AI framework

PINN could be viewed as a building block in a larger AI framework, or other AI technologies could help to improve the PINN framework.

For more practical applications, PINNs can be used as a tool for engaging deep reinforcement learning (DRL) that combines reinforcement Learning (RL) and deep learning. RL enables agents to conduct experiments to comprehend their environment better, allowing them to acquire high-level causal links and reasoning about causes and eﬀects (Arulkumaran et al, 2017). The main principle of reinforcement learning is to have an agent learn from its surroundings through exploration and by deﬁning a reward (Shrestha and Mahmood, 2019). In the DRL framework, the PINNs can be used as agents. In this scenario, information from the environment could be directly embedded

in the agent using knowledge from actuators, sensors, and the prior-physical law, like in a transfer learning paradigm.

PINNs can also be viewed as an example of merging deep learning with symbolic artiﬁcial intelligence. The symbolic paradigm is based on the fact that intelligence arises by manipulating abstract models of representations and interactions. This approach has the advantage to discover features of a problem using logical inference, but it lacks the easiness of adhering to realworld data, as in DL. A fulﬁlling combination of symbolic intelligence and DL would provide the best of both worlds. The model representations could be built up directly from a small amount of data with some priors (Garnelo and Shanahan, 2019). In the PINN framework, the physical injection of physical laws could be treated as symbolic intelligence by adding reasoning procedures.

Causal Models are intermediate descriptions that abstract physical models while answering statistical model questions (Scho¨lkopf et al, 2021). Diﬀerential equations model allows to forecast a physical system’s future behavior, assess the impact of interventions, and predict statistical dependencies between variables. On the other hand, a statistical model often doesn’t refer to dynamic processes, but rather how some variables allow the prediction of others when the experimental conditions remain constant. In this context, a causal representation learning, merging Machine learning and graphical causality, is a novel research topic, and given the need to model physical phenomena given known data, it may be interesting to investigate whether PINN, can help to determine causality when used to solve hybrid (mixed forward and inverse) problems.

### 6 Conclusion

This review can be considered an in-depth study of an innovation process over the last four years rather than a simple research survey in the ﬁeld of PINNs. Raissi’s ﬁrst research (Raissi et al, 2017c,d), which developed the PINN framework, focused on implementing a PINN to solve known physical models. These innovative papers helped PINN methodology gain traction and justify its original concept even more. Most of the analyzed studies have attempted to personalize the PINNs by modifying the activation functions, gradient optimization procedures, neural networks, or loss function structures. A border extension of PINNs original idea brings to use in the physical loss function bare minimum information of the model, without using a typical PDE equation, and on the other side to embed directly in the NN structure the validity of initial or boundary conditions. Only a few have looked into alternatives to automatic diﬀerentiation (Fang, 2021) or at convergence problems (Wang et al, 2021b, 2022b). Finally, a core subset of publications has attempted to take this process to a new meta-level by proposing all-inclusive frameworks for many sub-types of physical problems or multi-physics systems (Cai et al,

- 2021b). The brilliance of the ﬁrst PINN articles (Raissi et al, 2017c,d) lies in resurrecting the concept of optimizing a problem with a physical constraint by approximating the unknown function with a neural network (Dissanayake and Phan-Thien, 1994) and then extending this concept to a hybrid data-equation driven approach within modern research. Countless studies in previous years have approximated the unknown function using ways diﬀerent than neural networks, such as the kernel approaches (Owhadi and Yoo, 2019), or other approaches that have used PDE functions as constraints in an optimization problem (Hinze et al, 2008).


However, PINNs are intrinsically driven by physical information, either from the data point values or the physical equation. The former can be provided at any point in the domain but is usually only as initial or boundary data. More importantly, the latter are the collocation points where the NN is forced to obey the physical model equation.

We examined the literature on PINNs in this paper, beginning with the ﬁrst papers from Raissi et al (2017c,d) and continuing with the research on including physical priors on Neural Networks. This survey looks at PINNs, as a collocation-based method for solving diﬀerential questions with Neural networks. Apart from the vanilla PINN solution we look at most of its variants, like variational PINN (VPINN) as well as in its soft form, with loss including the initial and boundary conditions, and its hard form version with boundary conditions encoded in the Neural network structure.

This survey explains the PINN pipeline, analyzing each building block; ﬁrst, the neural networks, then the loss construction based on the physical model and feedback mechanism. Then, an overall analysis of examples of equations in which the PINN methodology has been used, and ﬁnally, an insight into PINNs on where they can be concretely applied and the packages available.

Finally, we can conclude that numerous improvements are still possible; most notably, in unsolved theoretical issues. There is still potential for development in training PINNs optimally and extending PINNs to solve multiple equations.

### References

Abreu E, Florindo JB (2021) A Study on a Feedforward Neural Network to Solve Partial Diﬀerential Equations in Hyperbolic-Transport Problems. In: Paszynski M, Kranzlmu¨ller D, Krzhizhanovskaya VV, et al (eds) Computational Science – ICCS 2021. Springer International Publishing, Cham, Lecture Notes in Computer Science, pp 398–411, https://doi.org/10.1007/ 978-3-030-77964-1 31

Aldweesh A, Derhab A, Emam AZ (2020) Deep learning approaches for anomaly-based intrusion detection systems: A survey, taxonomy, and open issues. Knowledge-Based Systems 189:105,124. https://doi.org/https: //doi.org/10.1016/j.knosys.2019.105124, URL https://www.sciencedirect. com/science/article/pii/S0950705119304897

Alkhadhr S, Liu X, Almekkawy M (2021) Modeling of the Forward Wave Propagation Using Physics-Informed Neural Networks. In: 2021 IEEE International Ultrasonics Symposium (IUS), pp 1–4, https://doi.org/10.1109/ IUS52206.2021.9593574, iSSN: 1948-5727

Almajid MM, Abu-Al-Saud MO (2022) Prediction of porous media ﬂuid ﬂow using physics informed neural networks. Journal of Petroleum Science and Engineering 208:109,205. https://doi.org/10.1016/j.petrol. 2021.109205, URL https://www.sciencedirect.com/science/article/pii/ S0920410521008597

Alom MZ, Taha TM, Yakopcic C, et al (2019) A state-of-the-art survey on deep learning theory and architectures. Electronics 8(3). https://doi.org/10. 3390/electronics8030292, URL https://www.mdpi.com/2079-9292/8/3/292

Amini Niaki S, Haghighat E, Campbell T, et al (2021) Physics-informed neural network for modelling the thermochemical curing process of composite-tool systems during manufacture. Computer Methods in Applied Mechanics and Engineering 384:113,959. https://doi.org/10.1016/j.cma.2021.113959, URL https://www.sciencedirect.com/science/article/pii/S0045782521002966

Araz JY, Criado JC, Spannowsky M (2021) Elvet – a neural network-based diﬀerential equation and variational problem solver. arXiv:210314575 [heplat, physics:hep-ph, physics:hep-th, stat] URL http://arxiv.org/abs/2103. 14575, arXiv: 2103.14575

Arnold DN (2015) Stability, Consistency, and Convergence of Numerical Discretizations. Springer, Berlin, Heidelberg, p 1358–1364, https: //doi.org/10.1007/978-3-540-70529-1 407, URL https://doi.org/10.1007/ 978-3-540-70529-1 407

Arnold F, King R (2021) State–space modeling for control based on physicsinformed neural networks. Engineering Applications of Artiﬁcial Intelligence 101:104,195. https://doi.org/10.1016/j.engappai.2021.104195, URL https:// www.sciencedirect.com/science/article/pii/S0952197621000427

Arthurs CJ, King AP (2021) Active training of physics-informed neural networks to aggregate and interpolate parametric solutions to the NavierStokes equations. Journal of Computational Physics 438:110,364. https: //doi.org/10.1016/j.jcp.2021.110364, URL https://www.sciencedirect.com/ science/article/pii/S002199912100259X

Arulkumaran K, Deisenroth MP, Brundage M, et al (2017) Deep Reinforcement Learning: A Brief Survey. IEEE Signal Processing Magazine 34(6):26–38. https://doi.org/10.1109/MSP.2017.2743240

Balu A, Botelho S, Khara B, et al (2021) Distributed multigrid neural solvers on megavoxel domains. In: Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis. Association for Computing Machinery, New York, NY, USA, SC ’21, https:// doi.org/10.1145/3458817.3476218, URL https://doi.org/10.1145/3458817. 3476218

Bauer B, Kohler M (2019) On deep learning as a remedy for the curse of dimensionality in nonparametric regression. The Annals of Statistics 47(4):2261–2285. https://doi.org/10.1214/18-AOS1747, URL https://projecteuclid.org/journals/annals-of-statistics/volume-47/issue-4/ On-deep-learning-as-a-remedy-for-the-curse-of/10.1214/18-AOS1747.full

Belkin M, Hsu D, Ma S, et al (2019) Reconciling modern machinelearning practice and the classical bias–variance trade-oﬀ. Proceedings of the National Academy of Sciences 116(32):15,849–15,854. https://doi.org/ 10.1073/pnas.1903070116, URL https://www.pnas.org/doi/10.1073/pnas. 1903070116

Bellman R (1966) Dynamic programming. Science 153(3731):34–37

Berg J, Nystr¨m K (2018) A uniﬁed deep artiﬁcial neural network approach to partial diﬀerential equations in complex geometries. Neurocomputing 317:28–41. https://doi.org/10.1016/j.neucom.2018.06.056, URL https: //www.sciencedirect.com/science/article/pii/S092523121830794X

Berman DS, Buczak AL, Chavis JS, et al (2019) A survey of deep learning methods for cyber security. Information 10(4). https://doi.org/10.3390/ info10040122, URL https://www.mdpi.com/2078-2489/10/4/122

Blechschmidt J, Ernst OG (2021) Three ways to solve partial diﬀerential equations with neural networks — A review. GAMM-Mitteilungen 44(2):e202100,006. https://doi.org/10.1002/gamm.202100006, URL https: //onlinelibrary.wiley.com/doi/abs/10.1002/gamm.202100006

Cai S, Mao Z, Wang Z, et al (2021a) Physics-informed neural networks (PINNs) for ﬂuid mechanics: a review. Acta Mechanica Sinica 37(12):1727– 1738. https://doi.org/10.1007/s10409-021-01148-1, URL https://doi.org/ 10.1007/s10409-021-01148-1

Cai S, Wang Z, Lu L, et al (2021b) DeepM&Mnet: Inferring the electroconvection multiphysics ﬁelds based on operator approximation by neural networks. Journal of Computational Physics 436:110,296. https://doi.org/10.1016/ j.jcp.2021.110296, URL https://www.sciencedirect.com/science/article/pii/ S0021999121001911

Cai S, Wang Z, Wang S, et al (2021c) Physics-Informed Neural Networks for Heat Transfer Problems. Journal of Heat Transfer 143(6). https://doi.org/ 10.1115/1.4050542, URL https://doi.org/10.1115/1.4050542

- Calin O (2020a) Convolutional Networks, Springer International Publishing, Cham, pp 517–542. https://doi.org/10.1007/978-3-030-36721-3 16, URL https://doi.org/10.1007/978-3-030-36721-3 16

- Calin O (2020b) Universal Approximators. Springer Series in the Data Sciences, Springer International Publishing, Cham, p 251– 284, https://doi.org/10.1007/978-3-030-36721-3 9, URL https://doi.org/10. 1007/978-3-030-36721-3 9


- Caterini AL, Chang DE (2018a) Generic Representation of Neural Networks. In: Caterini AL, Chang DE (eds) Deep Neural Networks in a Mathematical Framework. SpringerBriefs in Computer Science, Springer International Publishing, Cham, p 23–34, https://doi.org/10.1007/978-3-319-75304-1 3, URL https://doi.org/10.1007/978-3-319-75304-1 3

- Caterini AL, Chang DE (2018b) Speciﬁc Network Descriptions. In: Caterini AL, Chang DE (eds) Deep Neural Networks in a Mathematical Framework. SpringerBriefs in Computer Science, Springer International Publishing, Cham, p 35–58, https://doi.org/10.1007/978-3-319-75304-1 4, URL https: //doi.org/10.1007/978-3-319-75304-1 4


Cavanagh H, Mosbach A, Scalliet G, et al (2021) Physics-informed deep learning characterizes morphodynamics of asian soybean rust disease. Nature Communications 12(1):6424. https://doi.org/10.1038/s41467-021-26577-1, URL https://doi.org/10.1038/s41467-021-26577-1

Chen F, Sondak D, Protopapas P, et al (2020a) Neurodiﬀeq: A python package for solving diﬀerential equations with neural networks. Journal of Open Source Software 5(46):1931

Chen H, Engkvist O, Wang Y, et al (2018) The rise of deep learning in drug discovery. Drug Discovery Today 23(6):1241–1250. https://doi.org/https:// doi.org/10.1016/j.drudis.2018.01.039, URL https://www.sciencedirect.com/ science/article/pii/S1359644617303598

Chen Y, Lu L, Karniadakis GE, et al (2020b) Physics-informed neural networks for inverse problems in nano-optics and metamaterials. Optics Express 28(8):11,618–11,633. https://doi.org/10.1364/OE.384875, URL https://www.osapublishing.org/oe/abstract.cfm?uri=oe-28-8-11618

Cheng C, Zhang GT (2021) Deep Learning Method Based on Physics Informed Neural Network with Resnet Block for Solving Fluid Flow Problems. Water 13(4):423. https://doi.org/10.3390/w13040423, URL https://www.

mdpi.com/2073-4441/13/4/423

Cheung KC, See S (2021) Recent advance in machine learning for partial diﬀerential equation. CCF Transactions on High Performance Computing 3(3):298–310. https://doi.org/10.1007/s42514-021-00076-7, URL https: //doi.org/10.1007/s42514-021-00076-7

Chiu PH, Wong JC, Ooi C, et al (2022) CAN-PINN: A fast physicsinformed neural network based on coupled-automatic–numerical diﬀerentiation method. Computer Methods in Applied Mechanics and Engineering 395:114,909. https://doi.org/10.1016/j.cma.2022.114909, URL https:// www.sciencedirect.com/science/article/pii/S0045782522001906

Cybenko G (1989) Approximation by superpositions of a sigmoidal function. Mathematics of Control, Signals and Systems 2(4):303–314. https://doi.org/ 10.1007/BF02551274, URL https://doi.org/10.1007/BF02551274

Dargan S, Kumar M, Ayyagari MR, et al (2020) A Survey of Deep Learning and Its Applications: A New Paradigm to Machine Learning. Archives of Computational Methods in Engineering 27(4):1071– 1092. https://doi.org/10.1007/s11831-019-09344-w, URL https://doi.org/ 10.1007/s11831-019-09344-w

De Ryck T, Mishra S (2021) Error analysis for physics informed neural networks (PINNs) approximating Kolmogorov PDEs. arXiv:210614473 [cs, math] URL http://arxiv.org/abs/2106.14473, arXiv: 2106.14473

De Ryck T, Lanthaler S, Mishra S (2021) On the approximation of functions by tanh neural networks. Neural Networks 143:732–750. https://doi.org/10. 1016/j.neunet.2021.08.015, URL https://www.sciencedirect.com/science/ article/pii/S0893608021003208

De Ryck T, Jagtap AD, Mishra S (2022) Error estimates for physics informed neural networks approximating the Navier-Stokes equations. arXiv:220309346 [cs, math] URL http://arxiv.org/abs/2203.09346, arXiv: 2203.09346

Dissanayake MWMG, Phan-Thien N (1994) Neural-network-based approximations for solving partial diﬀerential equations. Communications in Numerical Methods in Engineering 10(3):195–201. https://doi.org/10.1002/cnm. 1640100303, URL https://onlinelibrary.wiley.com/doi/abs/10.1002/cnm. 1640100303

Driscoll TA, Hale N, Trefethen LN (2014) Chebfun Guide. Pafnuty Publications, URL http://www.chebfun.org/docs/guide/

Dwivedi V, Srinivasan B (2020) Physics Informed Extreme Learning Machine (PIELM)–A rapid method for the numerical solution of partial diﬀerential equations. Neurocomputing 391:96–118. https://doi.org/10.1016/j. neucom.2019.12.099, URL https://www.sciencedirect.com/science/article/ pii/S0925231219318144

E W, Yu B (2018) The Deep Ritz Method: A Deep Learning-Based Numerical Algorithm for Solving Variational Problems. Communications in Mathematics and Statistics 6(1):1–12. https://doi.org/10.1007/s40304-018-0127-z, URL https://doi.org/10.1007/s40304-018-0127-z

Elbr¨chter D, Perekrestenko D, Grohs P, et al (2021) Deep Neural Network Approximation Theory. IEEE Transactions on Information Theory 67(5):2581–2623. https://doi.org/10.1109/TIT.2021.3062161

Fang Z (2021) A High-Eﬃcient Hybrid Physics-Informed Neural Networks Based on Convolutional Neural Network. IEEE Transactions on Neural Networks and Learning Systems pp 1–13. https://doi.org/10.1109/TNNLS. 2021.3070878

- Fang Z, Zhan J (2020a) Deep Physical Informed Neural Networks for Metamaterial Design. IEEE Access 8:24,506–24,513. https://doi.org/10.1109/ ACCESS.2019.2963375
- Fang Z, Zhan J (2020b) A Physics-Informed Neural Network Framework for PDEs on 3D Surfaces: Time Independent Problems. IEEE Access 8:26,328– 26,335. https://doi.org/10.1109/ACCESS.2019.2963390


Fuks O, Tchelepi HA (2020) LIMITATIONS OF PHYSICS INFORMED MACHINE LEARNING FOR NONLINEAR TWO-PHASE TRANSPORT IN POROUS MEDIA. Journal of Machine Learning for Modeling and Computing 1(1). https://doi.org/10.1615/.2020033905, URL https://www.dl.begellhouse.com/journals/558048804a15188a, 583c4e56625ba94e,415f83b5707fde65.html

Gao H, Sun L, Wang JX (2021) PhyGeoNet: Physics-informed geometryadaptive convolutional neural networks for solving parameterized steadystate PDEs on irregular domain. Journal of Computational Physics 428:110,079. https://doi.org/10.1016/j.jcp.2020.110079, URL https://www. sciencedirect.com/science/article/pii/S0021999120308536

Gardner JR, Pleiss G, Bindel D, et al (2018) Gpytorch: Blackbox matrixmatrix gaussian process inference with gpu acceleration. In: Advances in Neural Information Processing Systems

Garnelo M, Shanahan M (2019) Reconciling deep learning with symbolic artiﬁcial intelligence: representing objects and relations. Current Opinion in Behavioral Sciences 29:17–23. https://doi.org/10.1016/ j.cobeha.2018.12.010, URL https://www.sciencedirect.com/science/article/ pii/S2352154618301943

Geneva N, Zabaras N (2020) Modeling the dynamics of pde systems with physics-constrained deep auto-regressive networks. Journal of Computational Physics 403:109,056. https://doi.org/https://doi.org/10.1016/j. jcp.2019.109056, URL https://www.sciencedirect.com/science/article/pii/ S0021999119307612

Goswami S, Anitescu C, Chakraborty S, et al (2020) Transfer learning enhanced physics informed neural network for phase-ﬁeld modeling of fracture. Theoretical and Applied Fracture Mechanics 106:102,447. https:// doi.org/https://doi.org/10.1016/j.tafmec.2019.102447, URL https://www. sciencedirect.com/science/article/pii/S016784421930357X

Grandits T, Pezzuto S, Costabal FS, et al (2021) Learning Atrial Fiber Orientations and Conductivity Tensors from Intracardiac Maps Using Physics-Informed Neural Networks. In: Ennis DB, Perotti LE, Wang VY (eds) Functional Imaging and Modeling of the Heart. Springer International Publishing, Cham, Lecture Notes in Computer Science, pp 650–658, https://doi.org/10.1007/978-3-030-78710-3 62

Grubiˇsi´c L, Hajba M, Lacmanovi´c D (2021) Deep Neural Network Model for Approximating Eigenmodes Localized by a Conﬁning Potential. Entropy 23(1):95. https://doi.org/10.3390/e23010095, URL https://www. mdpi.com/1099-4300/23/1/95

Haghighat E, Juanes R (2021) SciANN: A Keras/Tensorﬂow wrapper for scientiﬁc computations and physics-informed deep learning using artiﬁcial neural networks. Computer Methods in Applied Mechanics and Engineering 373:113,552. https://doi.org/10.1016/j.cma.2020.113552, URL http://arxiv. org/abs/2005.08803, arXiv: 2005.08803

Haghighat E, Bekar AC, Madenci E, et al (2021a) A nonlocal physics-informed deep learning framework using the peridynamic diﬀerential operator. Computer Methods in Applied Mechanics and Engineering 385:114,012. https:// doi.org/10.1016/j.cma.2021.114012, URL https://www.sciencedirect.com/ science/article/pii/S0045782521003431

Haghighat E, Raissi M, Moure A, et al (2021b) A physics-informed deep learning framework for inversion and surrogate modeling in solid mechanics. Computer Methods in Applied Mechanics and Engineering 379:113,741. https:// doi.org/10.1016/j.cma.2021.113741, URL https://www.sciencedirect.com/ science/article/pii/S0045782521000773

Haitsiukevich K, Ilin A (2022) Improved Training of Physics-Informed Neural Networks with Model Ensembles. arXiv:220405108 [cs, stat] URL http:// arxiv.org/abs/2204.05108, arXiv: 2204.05108

He Q, Tartakovsky AM (2021) Physics-informed neural network method for forward and backward advection-dispersion equations. Water Resources Research 57(7):e2020WR029,479. https://doi.org/10.1029/2020WR029479, URL https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/ 2020WR029479, e2020WR029479 2020WR029479

He Q, Barajas-Solano D, Tartakovsky G, et al (2020) Physics-informed neural networks for multiphysics data assimilation with application to subsurface transport. Advances in Water Resources 141:103,610. https:// doi.org/10.1016/j.advwatres.2020.103610, URL https://www.sciencedirect. com/science/article/pii/S0309170819311649

Hennigh O, Narasimhan S, Nabian MA, et al (2021) NVIDIA SimNet™: An AIAccelerated Multi-Physics Simulation Framework. In: Paszynski M, Kranzlmu¨ller D, Krzhizhanovskaya VV, et al (eds) Computational Science – ICCS 2021. Springer International Publishing, Cham, Lecture Notes in Computer Science, pp 447–461, https://doi.org/10.1007/978-3-030-77977-1 36

Hillebrecht B, Unger B (2022) Certiﬁed machine learning: A posteriori error estimation for physics-informed neural networks. Tech. rep., https:// doi.org/10.48550/arXiv.2203.17055, URL http://arxiv.org/abs/2203.17055, arXiv:2203.17055 [cs, math] type: article

Hinze M, Pinnau R, Ulbrich M, et al (2008) Optimization with PDE constraints, vol 23. Springer Science & Business Media

Hoﬀer JG, Geiger BC, Ofner P, et al (2021) Mesh-Free Surrogate Models for Structural Mechanic FEM Simulation: A Comparative Study of Approaches. Applied Sciences 11(20):9411. https://doi.org/10.3390/app11209411, URL https://www.mdpi.com/2076-3417/11/20/9411

Hornik K, Stinchcombe M, White H (1989) Multilayer feedforward networks are universal approximators. Neural Networks 2(5):359–366. https: //doi.org/10.1016/0893-6080(89)90020-8, URL https://www.sciencedirect. com/science/article/pii/0893608089900208

Huang GB, Wang DH, Lan Y (2011) Extreme learning machines: a survey. International Journal of Machine Learning and Cybernetics 2(2):107–122. https://doi.org/10.1007/s13042-011-0019-y, URL https://doi.org/10.1007/ s13042-011-0019-y

Huang X, Liu H, Shi B, et al (2021) Solving Partial Diﬀerential Equations with Point Source Based on Physics-Informed Neural Networks. arXiv:211101394

[physics] URL http://arxiv.org/abs/2111.01394, arXiv: 2111.01394

Irrgang C, Boers N, Sonnewald M, et al (2021) Towards neural Earth system modelling by integrating artiﬁcial intelligence in Earth system science. Nature Machine Intelligence 3(8):667–674. https://doi. org/10.1038/s42256-021-00374-3, URL https://www.nature.com/articles/ s42256-021-00374-3

Islam M, Thakur MSH, Mojumder S, et al (2021) Extraction of material properties through multi-ﬁdelity deep learning from molecular dynamics simulation. Computational Materials Science 188:110,187. https:// doi.org/10.1016/j.commatsci.2020.110187, URL https://www.sciencedirect. com/science/article/pii/S0927025620306789

Jagtap AD, Kawaguchi K, Karniadakis GE (2020a) Adaptive activation functions accelerate convergence in deep and physics-informed neural networks. Journal of Computational Physics 404:109,136. https://doi.org/10.1016/ j.jcp.2019.109136, URL https://www.sciencedirect.com/science/article/pii/ S0021999119308411

Jagtap AD, Kharazmi E, Karniadakis GE (2020b) Conservative physicsinformed neural networks on discrete domains for conservation laws: Applications to forward and inverse problems. Computer Methods in Applied Mechanics and Engineering 365:113,028. https://doi.org/10.1016/j. cma.2020.113028, URL https://www.sciencedirect.com/science/article/pii/ S0045782520302127

Jamali B, Haghighat E, Ignjatovic A, et al (2021) Machine learning for accelerating 2D ﬂood models: Potential and challenges. Hydrological Processes 35(4):e14,064. https://doi.org/10.1002/hyp.14064, URL https:// onlinelibrary.wiley.com/doi/abs/10.1002/hyp.14064

Jin X, Cai S, Li H, et al (2021) NSFnets (Navier-Stokes ﬂow nets): Physicsinformed neural networks for the incompressible Navier-Stokes equations. Journal of Computational Physics 426:109,951. https://doi.org/10.1016/ j.jcp.2020.109951, URL https://www.sciencedirect.com/science/article/pii/ S0021999120307257

Karniadakis GE, Kevrekidis IG, Lu L, et al (2021) Physics-informed machine learning. Nature Reviews Physics 3(6):422–440. https://doi. org/10.1038/s42254-021-00314-5, URL https://www.nature.com/articles/ s42254-021-00314-5

Kashinath K, Mustafa M, Albert A, et al (2021) Physics-informed machine learning: case studies for weather and climate modelling. Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences 379(2194):20200,093. https://doi.org/10.1098/rsta.2020.0093,

URL https://royalsocietypublishing.org/doi/full/10.1098/rsta.2020.0093

Kharazmi E, Zhang Z, Karniadakis GE (2019) Variational PhysicsInformed Neural Networks For Solving Partial Diﬀerential Equations. arXiv:191200873 [physics, stat] URL http://arxiv.org/abs/1912.00873, arXiv: 1912.00873

Kharazmi E, Cai M, Zheng X, et al (2021a) Identiﬁability and predictability of integer- and fractional-order epidemiological models using physics-informed neural networks. Nature Computational Science 1(11):744– 753. https://doi.org/10.1038/s43588-021-00158-0, URL https://doi.org/10. 1038/s43588-021-00158-0

Kharazmi E, Zhang Z, Karniadakis GEM (2021b) hp-VPINNs: Variational physics-informed neural networks with domain decomposition. Computer Methods in Applied Mechanics and Engineering 374:113,547. https:// doi.org/10.1016/j.cma.2020.113547, URL https://www.sciencedirect.com/ science/article/pii/S0045782520307325

Kim J, Lee K, Lee D, et al (2021a) DPM: A Novel Training Method for Physics-Informed Neural Networks in Extrapolation. Proceedings of the AAAI Conference on Artiﬁcial Intelligence 35(9):8146–8154. URL https: //ojs.aaai.org/index.php/AAAI/article/view/16992

Kim SW, Kim I, Lee J, et al (2021b) Knowledge Integration into deep learning in dynamical systems: an overview and taxonomy. Journal of Mechanical Science and Technology 35(4):1331–1342. https://doi.org/10. 1007/s12206-021-0342-5, URL https://doi.org/10.1007/s12206-021-0342-5

Kissas G, Yang Y, Hwuang E, et al (2020) Machine learning in cardiovascular ﬂows modeling: Predicting arterial blood pressure from non-invasive 4D ﬂow MRI data using physics-informed neural networks. Computer Methods in Applied Mechanics and Engineering 358:112,623. https://doi.org/10.1016/j. cma.2019.112623, URL https://www.sciencedirect.com/science/article/pii/ S0045782519305055

Kollmannsberger S, D’Angella D, Jokeit M, et al (2021) Physics-Informed Neural Networks. In: Kollmannsberger S, D’Angella D, Jokeit M, et al (eds) Deep Learning in Computational Mechanics. Studies in Computational Intelligence, Springer International Publishing, Cham, p 55– 84, https://doi.org/10.1007/978-3-030-76587-3 5, URL https://doi.org/10. 1007/978-3-030-76587-3 5

Kondor R, Trivedi S (2018) On the Generalization of Equivariance and Convolution in Neural Networks to the Action of Compact Groups. In: Dy J, Krause A (eds) Proceedings of the 35th International Conference on Machine Learning, Proceedings of Machine Learning Research, vol 80. PMLR, pp

2747–2755, URL https://proceedings.mlr.press/v80/kondor18a.html

Koryagin A, Khudorozkov R, Tsimfer S (2019) PyDEns: a Python Framework for Solving Diﬀerential Equations with Neural Networks. arXiv:190911544 [cs, stat] URL http://arxiv.org/abs/1909.11544, arXiv: 1909.11544

Kovacs A, Exl L, Kornell A, et al (2022) Conditional physics informed neural networks. Communications in Nonlinear Science and Numerical Simulation 104:106,041. https://doi.org/10.1016/j.cnsns.2021.106041, URL https: //www.sciencedirect.com/science/article/pii/S1007570421003531

Krishnapriyan A, Gholami A, Zhe S, et al (2021) Characterizing possible failure modes in physics-informed neural networks. In: Ranzato M, Beygelzimer A, Dauphin Y, et al (eds) Advances in Neural Information Processing Systems, vol 34. Curran Associates, Inc., pp 26,548–26,560, URL https://proceedings.neurips.cc/paper/2021/ﬁle/ df438e5206f31600e6ae4af72f2725f1-Paper.pdf

Kumar M, Yadav N (2011) Multilayer perceptrons and radial basis function neural network methods for the solution of diﬀerential equations: A survey. Computers & Mathematics with Applications 62(10):3796–3811. https: //doi.org/10.1016/j.camwa.2011.09.028, URL https://www.sciencedirect. com/science/article/pii/S0898122111007966

Kutyniok G (2022) The Mathematics of Artiﬁcial Intelligence. arXiv:220308890 [cs, math, stat] URL http://arxiv.org/abs/2203.08890, arXiv: 2203.08890

Lagaris I, Likas A, Fotiadis D (1998) Artiﬁcial neural networks for solving ordinary and partial diﬀerential equations. IEEE Transactions on Neural Networks 9(5):987–1000. https://doi.org/10.1109/72.712178

Lagaris I, Likas A, Papageorgiou D (2000) Neural-network methods for boundary value problems with irregular boundaries. IEEE Transactions on Neural Networks 11(5):1041–1049. https://doi.org/10.1109/72.870037

Lai Z, Mylonas C, Nagarajaiah S, et al (2021) Structural identiﬁcation with physics-informed neural ordinary diﬀerential equations. Journal of Sound and Vibration 508:116,196. https://doi.org/https://doi.org/10.1016/ j.jsv.2021.116196, URL https://www.sciencedirect.com/science/article/pii/ S0022460X21002686

LeCun Y, Bengio Y, Hinton G (2015) Deep learning. Nature 521(7553):436–

444. https://doi.org/10.1038/nature14539, URL https://doi.org/10.1038/ nature14539

Lee H, Kang IS (1990) Neural algorithm for solving diﬀerential equations. Journal of Computational Physics 91(1):110–131. https://doi.org/10. 1016/0021-9991(90)90007-N, URL https://www.sciencedirect.com/science/ article/pii/002199919090007N

Li W, Bazant MZ, Zhu J (2021) A physics-guided neural network framework for elastic plates: Comparison of governing equations-based and energy-based approaches. Computer Methods in Applied Mechanics and Engineering 383:113,933. https://doi.org/10.1016/j.cma.2021.113933, URL https://www.sciencedirect.com/science/article/pii/S004578252100270X

Lin C, Li Z, Lu L, et al (2021a) Operator learning for predicting multiscale bubble growth dynamics. The Journal of Chemical Physics 154(10):104,118. https://doi.org/10.1063/5.0041203, URL https://aip.scitation.org/doi/10. 1063/5.0041203

Lin C, Maxey M, Li Z, et al (2021b) A seamless multiscale operator neural network for inferring bubble dynamics. Journal of Fluid Mechanics 929. https://doi.org/10.1017/jfm.2021.866, URL https: //www.cambridge.org/core/journals/journal-of-ﬂuid-mechanics/article/ seamless-multiscale-operator-neural-network-for-inferring-bubble-dynamics/ D516AB0EF954D0FF56AD864DB2618E94

Liu D, Wang Y (2021) A Dual-Dimer method for training physicsconstrained neural networks with minimax architecture. Neural Networks 136:112–125. https://doi.org/10.1016/j.neunet.2020.12.028, URL https:// www.sciencedirect.com/science/article/pii/S0893608020304536

Lu L, Dao M, Kumar P, et al (2020) Extraction of mechanical properties of materials through deep learning from instrumented indentation. Proceedings of the National Academy of Sciences 117(13):7052–7062. https://doi.org/10. 1073/pnas.1922210117, URL https://www.pnas.org/content/117/13/7052, https://arxiv.org/abs/https://www.pnas.org/content/117/13/7052.full.pdf

Lu L, Jin P, Pang G, et al (2021a) Learning nonlinear operators via DeepONet based on the universal approximation theorem of operators. Nature Machine Intelligence 3(3):218–229. https://doi. org/10.1038/s42256-021-00302-5, URL https://www.nature.com/articles/ s42256-021-00302-5

Lu L, Meng X, Mao Z, et al (2021b) DeepXDE: A deep learning library for solving diﬀerential equations. SIAM Review 63(1):208–228. https://doi.org/ 10.1137/19M1274067

Mallat S (2016) Understanding deep convolutional networks. Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences 374(2065):20150,203. https://doi.org/10.1098/rsta.2015.0203,

URL https://royalsocietypublishing.org/doi/10.1098/rsta.2015.0203

Mao Z, Jagtap AD, Karniadakis GE (2020) Physics-informed neural networks for high-speed ﬂows. Computer Methods in Applied Mechanics and Engineering 360:112,789. https://doi.org/10.1016/j.cma.2019.112789, URL https://www.sciencedirect.com/science/article/pii/S0045782519306814

Mao Z, Lu L, Marxen O, et al (2021) DeepM&Mnet for hypersonics: Predicting the coupled ﬂow and ﬁnite-rate chemistry behind a normal shock using neural-network approximation of operators. Journal of Computational Physics 447:110,698. https://doi.org/10.1016/j.jcp.2021.110698, URL https://www.sciencedirect.com/science/article/pii/S0021999121005933

Markidis S (2021) The Old and the New: Can Physics-Informed Deep-Learning Replace Traditional Linear Solvers? Frontiers in Big Data 4. URL https: //www.frontiersin.org/article/10.3389/fdata.2021.669097

Mathews A, Francisquez M, Hughes JW, et al (2021) Uncovering turbulent plasma dynamics via deep learning from partial observations. Physical Review E 104(2). https://doi.org/10.1103/physreve.104.025205, URL https: //www.osti.gov/pages/biblio/1813020

McClenny LD, Haile MA, Braga-Neto UM (2021) Tensordiﬀeq: Scalable multigpu forward and inverse solvers for physics informed neural networks. arXiv preprint arXiv:210316034

Mehta PP, Pang G, Song F, et al (2019) Discovering a universal variableorder fractional model for turbulent couette ﬂow using a physicsinformed neural network. Fractional Calculus and Applied Analysis 22(6):1675–1688. https://doi.org/10.1515/fca-2019-0086, URL https://doi. org/10.1515/fca-2019-0086

Meng X, Li Z, Zhang D, et al (2020) Ppinn: Parareal physics-informed neural network for time-dependent pdes. Computer Methods in Applied Mechanics and Engineering 370:113,250. https://doi.org/https://doi.org/10.1016/j. cma.2020.113250, URL https://www.sciencedirect.com/science/article/pii/ S0045782520304357

Minh Nguyen-Thanh V, Trong Khiem Nguyen L, Rabczuk T, et al (2020) A surrogate model for computational homogenization of elastostatics at ﬁnite strain using high-dimensional model representation-based neural network. International Journal for Numerical Methods in Engineering 121(21):4811– 4842. https://doi.org/10.1002/nme.6493, URL https://onlinelibrary.wiley. com/doi/abs/10.1002/nme.6493

- Mishra S, Molinaro R (2021a) Estimates on the generalization error of physicsinformed neural networks for approximating a class of inverse problems


- for PDEs. IMA Journal of Numerical Analysis https://doi.org/10.1093/ imanum/drab032, URL https://doi.org/10.1093/imanum/drab032
- Mishra S, Molinaro R (2021b) Physics informed neural networks for simulating radiative transfer. Journal of Quantitative Spectroscopy and Radiative Transfer 270:107,705. https://doi.org/10.1016/j.jqsrt.2021.107705, URL https://www.sciencedirect.com/science/article/pii/S0022407321001989


Mishra S, Molinaro R (2022) Estimates on the generalization error of physics-informed neural networks for approximating PDEs. IMA Journal of Numerical Analysis p drab093. https://doi.org/10.1093/imanum/drab093, URL https://doi.org/10.1093/imanum/drab093

Misyris GS, Venzke A, Chatzivasileiadis S (2020) Physics-informed neural networks for power systems. 2020 IEEE Power & Energy Society General Meeting (PESGM) pp 1–5

Mo Y, Ling L, Zeng D (2022) Data-driven vector soliton solutions of coupled nonlinear Schr¨dinger equation using a deep learning algorithm. Physics Letters A 421:127,739. https://doi.org/10.1016/j.physleta.2021.127739, URL https://www.sciencedirect.com/science/article/pii/S0375960121006034

Moseley B, Markham A, Nissen-Meyer T (2021) Finite Basis Physics-Informed Neural Networks (FBPINNs): a scalable domain decomposition approach for solving diﬀerential equations. arXiv:210707871 [physics] URL http://arxiv. org/abs/2107.07871, arXiv: 2107.07871

Muhammad AN, Aseere AM, Chiroma H, et al (2021) Deep learning application in smart cities: recent development, taxonomy, challenges and research prospects. Neural Computing and Applications 33(7):2973– 3009. https://doi.org/10.1007/s00521-020-05151-8, URL https://doi.org/ 10.1007/s00521-020-05151-8

Nabian MA, Gladstone RJ, Meidani H (2021) Eﬃcient training of physicsinformed neural networks via importance sampling. Computer-Aided Civil and Infrastructure Engineering 36(8):962–977. https://doi.org/10. 1111/mice.12685, URL https://onlinelibrary.wiley.com/doi/abs/10.1111/ mice.12685

- Nandi T, Hennigh O, Nabian M, et al (2021) Progress Towards Solving High Reynolds Number Reacting Flows in SimNet. Tech. rep., URL https://www.osti.gov/biblio/ 1846970-progress-towards-solving-high-reynolds-number-reacting-ﬂows-simnet
- Nandi T, Hennigh O, Nabian M, et al (2022) Developing Digital Twins for Energy Applications Using Modulus. Tech. rep., URL https://www.osti. gov/biblio/1866819


Nascimento RG, Fricke K, Viana FA (2020) A tutorial on solving ordinary diﬀerential equations using python and hybrid physics-informed neural network. Engineering Applications of Artiﬁcial Intelligence 96:103,996. https: //doi.org/https://doi.org/10.1016/j.engappai.2020.103996, URL https:// www.sciencedirect.com/science/article/pii/S095219762030292X

Novak R, Xiao L, Hron J, et al (2020) Neural tangents: Fast and easy inﬁnite neural networks in python. In: International Conference on Learning Representations, URL https://github.com/google/neural-tangents

NVIDIA Corporation (2021) Modulus User Guide. https://developer.nvidia. com/modulus-user-guide-v2106, release v21.06 – November 9, 2021

Oreshkin BN, Carpov D, Chapados N, et al (2020) N-BEATS: Neural basis expansion analysis for interpretable time series forecasting. arXiv:190510437 [cs, stat] URL http://arxiv.org/abs/1905.10437, arXiv: 1905.10437

Owhadi H (2015) Bayesian numerical homogenization. Multiscale Modeling & Simulation 13(3):812–828. https://doi.org/ 10.1137/140974596, URL https://doi.org/10.1137/140974596, https://arxiv.org/abs/https://doi.org/10.1137/140974596

Owhadi H, Yoo GR (2019) Kernel Flows: From learning kernels from data into the abyss. Journal of Computational Physics 389:22–47. https: //doi.org/10.1016/j.jcp.2019.03.040, URL https://www.sciencedirect.com/ science/article/pii/S0021999119302232

Pang G, Lu L, Karniadakis GE (2019) fPINNs: Fractional Physics-Informed Neural Networks. SIAM Journal on Scientiﬁc Computing 41(4):A2603– A2626. https://doi.org/10.1137/18M1229845, URL https://epubs.siam.org/ doi/abs/10.1137/18M1229845

Paszke A, Gross S, Chintala S, et al (2017) Automatic diﬀerentiation in PyTorch. Tech. rep., URL https://openreview.net/forum?id=BJJsrmfCZ

Patel RG, Manickam I, Trask NA, et al (2022) Thermodynamically consistent physics-informed neural networks for hyperbolic systems. Journal of Computational Physics 449:110,754. https://doi.org/10.1016/j. jcp.2021.110754, URL https://www.sciencedirect.com/science/article/pii/ S0021999121006495

Pedro JB, Maron˜as J, Paredes R (2019) Solving Partial Diﬀerential Equations with Neural Networks. arXiv:191204737 [physics] URL http://arxiv.org/ abs/1912.04737, arXiv: 1912.04737

Peng W, Zhang J, Zhou W, et al (2021) IDRLnet: A Physics-Informed Neural Network Library. arXiv:210704320 [cs, math] URL http://arxiv.org/abs/

2107.04320, arXiv: 2107.04320

Pinkus A (1999) Approximation theory of the MLP model in neural networks. Acta Numerica 8:143–195. https://doi.org/10.1017/S0962492900002919, URL https://www.cambridge.org/core/journals/acta-numerica/article/ abs/approximation-theory-of-the-mlp-model-in-neural-networks/ 18072C558C8410C4F92A82BCC8FC8CF9

Pratama DA, Bakar MA, Man M, et al (2021) ANNs-Based Method for Solving Partial Diﬀerential Equations : A Survey. Preprint https: //doi.org/10.20944/preprints202102.0160.v1, URL https://www.preprints. org/manuscript/202102.0160/v1

Psichogios DC, Ungar LH (1992) A hybrid neural network-ﬁrst principles approach to process modeling. AIChE Journal 38(10):1499–1511. https:// doi.org/10.1002/aic.690381003, URL https://onlinelibrary.wiley.com/doi/ abs/10.1002/aic.690381003

Quarteroni A (2013) Numerical Models for Diﬀerential Problems, 2nd edn. Springer Publishing Company, Incorporated

Rackauckas C, Ma Y, Martensen J, et al (2021) Universal Diﬀerential Equations for Scientiﬁc Machine Learning. arXiv:200104385 [cs, math, q-bio, stat] URL http://arxiv.org/abs/2001.04385, arXiv: 2001.04385

Raﬁq M, Raﬁq G, Choi GS (2022) DSFA-PINN: Deep Spectral Feature Aggregation Physics Informed Neural Network. IEEE Access 10:22,247–22,259. https://doi.org/10.1109/ACCESS.2022.3153056

Raissi M (2018) Deep hidden physics models: Deep learning of nonlinear partial diﬀerential equations. Journal of Machine Learning Research 19(25):1–24. URL http://jmlr.org/papers/v19/18-046.html

Raissi M, Karniadakis GE (2018) Hidden physics models: Machine learning of nonlinear partial diﬀerential equations. Journal of Computational Physics 357:125–141. https://doi.org/10.1016/j.jcp.2017.11.039, URL https://www. sciencedirect.com/science/article/pii/S0021999117309014

- Raissi M, Perdikaris P, Karniadakis GE (2017a) Inferring solutions of diﬀerential equations using noisy multi-ﬁdelity data. Journal of Computational Physics 335:736–746. https://doi.org/10.1016/j.jcp.2017.01.060, URL https: //www.sciencedirect.com/science/article/pii/S0021999117300761
- Raissi M, Perdikaris P, Karniadakis GE (2017b) Machine learning of linear diﬀerential equations using Gaussian processes. Journal of Computational Physics 348:683–693. https://doi.org/10.1016/j.jcp.2017.07.050, URL https: //www.sciencedirect.com/science/article/pii/S0021999117305582


- Raissi M, Perdikaris P, Karniadakis GE (2017c) Physics Informed Deep Learning (Part I): Data-driven Solutions of Nonlinear Partial Diﬀerential Equations. arXiv:171110561 [cs, math, stat] URL http://arxiv.org/abs/ 1711.10561, arXiv: 1711.10561
- Raissi M, Perdikaris P, Karniadakis GE (2017d) Physics Informed Deep Learning (Part II): Data-driven Discovery of Nonlinear Partial Diﬀerential Equations. arXiv:171110566 [cs, math, stat] URL http://arxiv.org/abs/ 1711.10566, arXiv: 1711.10566


- Raissi M, Perdikaris P, Karniadakis GE (2018) Numerical gaussian processes for time-dependent and nonlinear partial diﬀerential equations. SIAM Journal on Scientiﬁc Computing 40(1):A172–A198. https://doi.org/10.1137/ 17M1120762, https://arxiv.org/abs/https://doi.org/10.1137/17M1120762
- Raissi M, Perdikaris P, Karniadakis GE (2019) Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial diﬀerential equations. Journal of Computational Physics 378:686–707. https://doi.org/10.1016/j.jcp.2018.10.045, URL https: //www.sciencedirect.com/science/article/pii/S0021999118307125


Raissi M, Yazdani A, Karniadakis GE (2020) Hidden ﬂuid mechanics: Learning velocity and pressure ﬁelds from ﬂow visualizations. Science 367(6481):1026– 1030. https://doi.org/10.1126/science.aaw4741, URL https://www.science. org/doi/10.1126/science.aaw4741

Ramabathiran AA, Ramachandran P (2021) SPINN: Sparse, Physics-based, and partially Interpretable Neural Networks for PDEs. Journal of Computational Physics 445:110,600. https://doi.org/10.1016/j.jcp.2021.110600, URL https://www.sciencedirect.com/science/article/pii/S0021999121004952

Rudin C, Chen C, Chen Z, et al (2022) Interpretable machine learning: Fundamental principles and 10 grand challenges. Statistics Surveys 16(none):1–85. https://doi.org/10.1214/21-SS133, URL https: //projecteuclid.org/journals/statistics-surveys/volume-16/issue-none/ Interpretable-machine-learning-Fundamental-principles-and-10-grand-challenges/ 10.1214/21-SS133.full

Ryaben’kii VS, Tsynkov SV (2006) A Theoretical Introduction to Numerical Analysis. CRC Press

Sahli Costabal F, Yang Y, Perdikaris P, et al (2020) Physics-Informed Neural Networks for Cardiac Activation Mapping. Frontiers in Physics 8:42. https://doi.org/10.3389/fphy.2020.00042, URL https://www.frontiersin. org/article/10.3389/fphy.2020.00042

Scharzenberger C, Hays J (2021) Learning To Estimate Regions Of Attraction Of Autonomous Dynamical Systems Using Physics-Informed Neural Networks. Tech. rep., https://doi.org/10.48550/arXiv.2111.09930, URL http: //arxiv.org/abs/2111.09930, arXiv:2111.09930 [cs] type: article

Schiassi E, Furfaro R, Leake C, et al (2021) Extreme theory of functional connections: A fast physics-informed neural network method for solving ordinary and partial diﬀerential equations. Neurocomputing 457:334–356. https: //doi.org/10.1016/j.neucom.2021.06.015, URL https://www.sciencedirect. com/science/article/pii/S0925231221009140

Scho¨lkopf B, Locatello F, Bauer S, et al (2021) Toward Causal Representation Learning. Proceedings of the IEEE 109(5):612–634. https://doi.org/10. 1109/JPROC.2021.3058954

Sengupta S, Basak S, Saikia P, et al (2020) A review of deep learning with special emphasis on architectures, applications and recent trends. Knowledge-Based Systems 194:105,596. https://doi.org/https://doi.org/10. 1016/j.knosys.2020.105596, URL https://www.sciencedirect.com/science/ article/pii/S095070512030071X

Sergeev A, Del Balso M (2018) Horovod: fast and easy distributed deep learning in TensorFlow. Tech. rep., https://doi.org/10.48550/arXiv.1802.05799, URL http://arxiv.org/abs/1802.05799, arXiv:1802.05799 [cs, stat] type: article

Shin Y, Darbon J, Karniadakis GE (2020a) On the convergence of physics informed neural networks for linear second-order elliptic and parabolic type PDEs. Communications in Computational Physics 28(5):2042– 2074. https://doi.org/10.4208/cicp.OA-2020-0193, URL http://arxiv.org/ abs/2004.01806, arXiv: 2004.01806

Shin Y, Zhang Z, Karniadakis GE (2020b) Error estimates of residual minimization using neural networks for linear PDEs. arXiv:201008019 [cs, math] URL http://arxiv.org/abs/2010.08019, arXiv: 2010.08019

Shrestha A, Mahmood A (2019) Review of Deep Learning Algorithms and Architectures. IEEE Access 7:53,040–53,065. https://doi.org/10.1109/ ACCESS.2019.2912200

Sirignano J, Spiliopoulos K (2018) DGM: A deep learning algorithm for solving partial diﬀerential equations. Journal of Computational Physics 375:1339–1364. https://doi.org/10.1016/j.jcp.2018.08.029, URL https:// www.sciencedirect.com/science/article/pii/S0021999118305527

Sitzmann V, Martel JNP, Bergman AW, et al (2020) Implicit Neural Representations with Periodic Activation Functions. arXiv:200609661 [cs, eess]

URL http://arxiv.org/abs/2006.09661, arXiv: 2006.09661

Smith JD, Azizzadenesheli K, Ross ZE (2021a) EikoNet: Solving the Eikonal Equation With Deep Neural Networks. IEEE Transactions on Geoscience and Remote Sensing 59(12):10,685–10,696. https://doi.org/10.1109/TGRS. 2020.3039165

Smith JD, Ross ZE, Azizzadenesheli K, et al (2021b) HypoSVI: Hypocentre inversion with Stein variational inference and physics informed neural networks. Geophysical Journal International 228(1):698–710. https://doi.org/ 10.1093/gji/ggab309, URL https://doi.org/10.1093/gji/ggab309

Stein ML (1987) Large sample properties of simulations using latin hypercube sampling. Technometrics 29:143–151

Stiasny J, Misyris GS, Chatzivasileiadis S (2021) Physics-Informed Neural Networks for Non-linear System Identiﬁcation for Power System Dynamics. In: 2021 IEEE Madrid PowerTech, pp 1–6, https://doi.org/10.1109/ PowerTech46648.2021.9495063

Stielow T, Scheel S (2021) Reconstruction of nanoscale particles from single-shot wide-angle free-electron-laser diﬀraction patterns with physicsinformed neural networks. Physical Review E 103(5):053,312. https://doi. org/10.1103/PhysRevE.103.053312, URL https://link.aps.org/doi/10.1103/ PhysRevE.103.053312

Stiller P, Bethke F, B¨hme M, et al (2020) Large-Scale Neural Solvers for Partial Diﬀerential Equations. In: Nichols J, Verastegui B, Maccabe AB, et al (eds) Driving Scientiﬁc and Engineering Discoveries Through the Convergence of HPC, Big Data and AI. Springer International Publishing, Cham, Communications in Computer and Information Science, pp 20–34, https://doi.org/10.1007/978-3-030-63393-6 2

Sun L, Gao H, Pan S, et al (2020a) Surrogate modeling for ﬂuid ﬂows based on physics-constrained deep learning without simulation data. Computer Methods in Applied Mechanics and Engineering 361:112,732. https://doi.org/ 10.1016/j.cma.2019.112732, URL https://www.sciencedirect.com/science/ article/pii/S004578251930622X

Sun S, Cao Z, Zhu H, et al (2020b) A Survey of Optimization Methods From a Machine Learning Perspective. IEEE Transactions on Cybernetics 50(8):3668–3681. https://doi.org/10.1109/TCYB.2019.2950779

Tartakovsky AM, Marrero CO, Perdikaris P, et al (2020) PhysicsInformed Deep Neural Networks for Learning Parameters and Constitutive Relationships in Subsurface Flow Problems. Water Resources Research 56(5):e2019WR026,731. https://doi.org/10.1029/2019WR026731,

URL https://onlinelibrary.wiley.com/doi/abs/10.1029/2019WR026731

Thompson DB (1992) Numerical Methods 101 – Convergence of Numerical Models. ASCE, pp 398–403, URL https://cedb.asce.org/CEDBsearch/ record.jsp?dockey=0078142

Tong Y, Xiong S, He X, et al (2021) Symplectic neural networks in taylor series form for hamiltonian systems. Journal of Computational Physics 437:110,325. https://doi.org/https://doi.org/10.1016/j. jcp.2021.110325, URL https://www.sciencedirect.com/science/article/pii/ S0021999121002205

Torabi Rad M, Viardin A, Schmitz GJ, et al (2020) Theory-training deep neural networks for an alloy solidiﬁcation benchmark problem. Computational Materials Science 180:109,687. https://doi.org/ 10.1016/j.commatsci.2020.109687, URL https://www.sciencedirect.com/ science/article/pii/S0927025620301786

Viana FAC, Nascimento RG, Dourado A, et al (2021) Estimating model inadequacy in ordinary diﬀerential equations with physicsinformed neural networks. Computers & Structures 245:106,458. https:// doi.org/10.1016/j.compstruc.2020.106458, URL https://www.sciencedirect. com/science/article/pii/S0045794920302613

Waheed Ub, Haghighat E, Alkhalifah T, et al (2021) PINNeik: Eikonal solution using physics-informed neural networks. Computers & Geosciences 155:104,833. https://doi.org/10.1016/j.cageo.2021.104833, URL https:// www.sciencedirect.com/science/article/pii/S009830042100131X

Wang L, Yan Z (2021) Data-driven rogue waves and parameter discovery in the defocusing nonlinear Schr¨dinger equation with a potential using the PINN deep learning. Physics Letters A 404:127,408. https://doi.org/10. 1016/j.physleta.2021.127408, URL https://www.sciencedirect.com/science/ article/pii/S0375960121002723

Wang N, Chang H, Zhang D (2021a) Theory-guided auto-encoder for surrogate construction and inverse modeling. Computer Methods in Applied Mechanics and Engineering 385:114,037. https://doi.org/10.1016/j. cma.2021.114037, URL https://www.sciencedirect.com/science/article/pii/ S0045782521003686

Wang S, Perdikaris P (2021) Deep learning of free boundary and Stefan problems. Journal of Computational Physics 428:109,914. https: //doi.org/10.1016/j.jcp.2020.109914, URL https://www.sciencedirect.com/ science/article/pii/S0021999120306884

Wang S, Teng Y, Perdikaris P (2021b) Understanding and Mitigating Gradient Flow Pathologies in Physics-Informed Neural Networks. SIAM Journal on Scientiﬁc Computing 43(5):A3055–A3081. https://doi.org/10.1137/ 20M1318043, URL https://epubs.siam.org/doi/abs/10.1137/20M1318043

Wang S, Sankaran S, Perdikaris P (2022a) Respecting causality is all you need for training physics-informed neural networks. arXiv:220307404 [nlin, physics:physics, stat] URL http://arxiv.org/abs/2203.07404, arXiv: 2203.07404

Wang S, Yu X, Perdikaris P (2022b) When and why PINNs fail to train: A neural tangent kernel perspective. Journal of Computational Physics 449:110,768. https://doi.org/10.1016/j.jcp.2021.110768, URL https://www. sciencedirect.com/science/article/pii/S002199912100663X

Wen G, Li Z, Azizzadenesheli K, et al (2022) U-FNO—An enhanced Fourier neural operator-based deep-learning model for multiphase ﬂow. Advances in Water Resources 163:104,180. https://doi.org/10.1016/j.advwatres. 2022.104180, URL https://www.sciencedirect.com/science/article/pii/ S0309170822000562

Wiecha PR, Arbouet A, Arbouet A, et al (2021) Deep learning in nano-photonics: inverse design and beyond. Photonics Research 9(5):B182–B200. https://doi.org/10.1364/PRJ.415960, URL https://www. osapublishing.org/prj/abstract.cfm?uri=prj-9-5-B182

Wong JC, Gupta A, Ong YS (2021) Can Transfer Neuroevolution Tractably Solve Your Diﬀerential Equations? IEEE Computational Intelligence Magazine 16(2):14–30. https://doi.org/10.1109/MCI.2021.3061854

Wong JC, Ooi C, Gupta A, et al (2022) Learning in Sinusoidal Spaces with Physics-Informed Neural Networks. arXiv:210909338 [physics] URL http: //arxiv.org/abs/2109.09338, arXiv: 2109.09338

Xiao H, Wu JL, Laizet S, et al (2020) Flows over periodic hills of parameterized geometries: A dataset for data-driven turbulence modeling from direct simulations. Computers & Fluids 200:104,431. https:// doi.org/10.1016/j.compﬂuid.2020.104431, URL https://www.sciencedirect. com/science/article/pii/S0045793020300074

- Xu K, Darve E (2020) ADCME: Learning Spatially-varying Physical Fields using Deep Neural Networks. arXiv:201111955 [cs, math] URL http://arxiv. org/abs/2011.11955, arXiv: 2011.11955
- Xu K, Darve E (2021) Solving inverse problems in stochastic models using deep neural networks and adversarial training. Computer Methods in Applied Mechanics and Engineering 384:113,976. https://doi.org/10.1016/j.


cma.2021.113976, URL https://www.sciencedirect.com/science/article/pii/ S0045782521003078

Yang L, Zhang D, Karniadakis GE (2020) Physics-informed generative adversarial networks for stochastic diﬀerential equations. SIAM Journal on Scientiﬁc Computing 42(1):A292–A317. https://doi.org/ 10.1137/18M1225409, URL https://doi.org/10.1137/18M1225409, https://arxiv.org/abs/https://doi.org/10.1137/18M1225409

Yang L, Meng X, Karniadakis GE (2021) B-PINNs: Bayesian physics-informed neural networks for forward and inverse PDE problems with noisy data. Journal of Computational Physics 425:109,913. https://doi.org/10.1016/ j.jcp.2020.109913, URL https://www.sciencedirect.com/science/article/pii/ S0021999120306872

Yang Y, Perdikaris P (2019) Adversarial uncertainty quantiﬁcation in physicsinformed neural networks. Journal of Computational Physics 394:136–152. https://doi.org/10.1016/j.jcp.2019.05.027, URL https://www.sciencedirect. com/science/article/pii/S0021999119303584

Yarotsky D (2017) Error bounds for approximations with deep relu networks. Neural Networks 94:103–114. https://doi.org/https://doi.org/10. 1016/j.neunet.2017.07.002, URL https://www.sciencedirect.com/science/ article/pii/S0893608017301545

Yuan L, Ni YQ, Deng XY, et al (2022) A-PINN: Auxiliary physics informed neural networks for forward and inverse problems of nonlinear integrodiﬀerential equations. Journal of Computational Physics 462:111,260. https: //doi.org/10.1016/j.jcp.2022.111260, URL https://www.sciencedirect.com/ science/article/pii/S0021999122003229

Yucesan YA, Viana FAC (2021) Hybrid physics-informed neural networks for main bearing fatigue prognosis with visual grease inspection. Computers in Industry 125:103,386. https://doi.org/10.1016/j.compind.2020.103386, URL https://www.sciencedirect.com/science/article/pii/S0166361520306205

Ozbay¨ AG, Hamzehloo A, Laizet S, et al (2021) Poisson CNN: Convolutional neural networks for the solution of the Poisson equation on a Cartesian mesh. Data-Centric Engineering 2. https://doi.org/10.1017/dce.2021.7, URL https:// www.cambridge.org/core/journals/data-centric-engineering/article/ poisson-cnn-convolutional-neural-networks-for-the-solution-of-the-poisson-equation-on-a-cartesian-mesh/ 8CDFD5C9D5172E51B924E9AA1BA253A1

Zhang R, Liu Y, Sun H (2020) Physics-informed multi-LSTM networks for metamodeling of nonlinear structures. Computer Methods in Applied Mechanics and Engineering 369:113,226. https://doi.org/10.1016/j.

cma.2020.113226, URL https://www.sciencedirect.com/science/article/pii/ S0045782520304114

Zhi-Qin, Xu J, , et al (2020) Frequency principle: Fourier analysis sheds light on deep neural networks. Communications in Computational Physics 28(5):1746–1767. https://doi.org/https://doi.org/10. 4208/cicp.OA-2020-0085, URL http://global-sci.org/intro/article detail/ cicp/18395.html

Zhu Q, Liu Z, Yan J (2021) Machine learning for metal additive manufacturing: predicting temperature and melt pool ﬂuid dynamics using physics-informed neural networks. Computational Mechanics 67(2):619– 635. https://doi.org/10.1007/s00466-020-01952-9, URL https://doi.org/10. 1007/s00466-020-01952-9

Zhu Y, Zabaras N, Koutsourelakis PS, et al (2019) Physics-constrained deep learning for high-dimensional surrogate modeling and uncertainty quantiﬁcation without labeled data. Journal of Computational Physics 394:56–81. https://doi.org/https://doi.org/10.1016/j.jcp.2019.05.024, URL https://www.sciencedirect.com/science/article/pii/S0021999119303559

- Zubov K, McCarthy Z, Ma Y, et al (2021a) NeuralPDE: Automating Physics-Informed Neural Networks (PINNs) with Error Approximations. arXiv:210709443 [cs] URL http://arxiv.org/abs/2107.09443, arXiv: 2107.09443
- Zubov K, McCarthy Z, Ma Y, et al (2021b) NeuralPDE: Automating Physics-Informed Neural Networks (PINNs) with Error Approximations. arXiv:210709443 [cs] URL http://arxiv.org/abs/2107.09443, arXiv: 2107.09443


