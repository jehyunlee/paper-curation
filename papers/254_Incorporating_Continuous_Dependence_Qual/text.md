## arXiv:2603.25122v1[math.DS]26 Mar 2026

### Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning

Guojie Li1, Wuyue Yang2*, Liu Hong1* 1School of Mathematics, Sun Yat-sen University, Guangzhou, 510275, China. 2Beijing Institute of Mathematical Sciences and Applications, Beijing, 101408, China.

*Corresponding author(s). E-mail(s): yangwuyue@bimsa.cn; hongliu@sysu.edu.cn;

Abstract Physics-informed neural networks (PINNs) have been proven as a promising way for solving various partial differential equations, especially high-dimensional ones and those with irregular boundaries. However, their capabilities in real applications are highly restricted by their poor generalization performance. Inspired by the rigorous mathematical statements on the well-posedness of PDEs, we develop a novel extension of PINNs by incorporating the additional information on the continuous dependence of PDE solutions with respect to parameters and initial/boundary values (abbreviated as cd-PINN). Extensive numerical experiments demonstrate that, with limited labeled data, cd-PINN achieves 1-3 orders of magnitude lower in test MSE than DeepONet and FNO. Therefore, incorporating the continuous dependence of PDE solutions provides a simple way for qualifying PINNs for operator learning.

Keywords: Physics-Informed Neural Networks, Parameterized Partial Differential Equations, Continuous Dependence, Operator Learning

#### 1 Introduction

In many fields of science and engineering, such as computational fluid dynamics, climate prediction, medical imaging, and game simulation, it is often necessary to repeatedly solve complex partial differential equations (PDEs) with varied initial/boundary values and parameter configurations [1–5]. Traditional numerical solvers, including finite difference (FD), finite element (FE), and finite volume (FV) methods [6–9], rely on discretization and thus face an inherent trade-off between accuracy and computational cost: fine grids ensure accuracy but are time-consuming, while coarse grids improve efficiency at the expense of precision. This limitation makes it challenging to achieve both real-time performance and high fidelity in applications, highlighting the need for a more efficient PDE solver.

Deep-learning-based differential equation solvers are generally considered to have a significant potential to improve computational efficiency [10, 11]. One notable method is the physics-informed neural network [12], which integrates knowledge of governing equations into the loss function to train the model and approximates the solution to PDEs without discretizing the solution domain. Alternative approaches include Deep Galerkin method [13], Deep Ritz method [14] and many others [15–17]. However, these approaches treat each variation in parameters or initial/boundary values as an independent task, requiring costly retraining. To overcome this limitation, operatorlearning methods emerged, including DeepONet [18], Neural Operator[19], and Fourier Neural Operators [20], which learn mappings between functional spaces (see Fig.1 A) and enable rapid inference for unseen configurations. While their physics-enhanced variants, such as PI-DeepONet [21] and PINO [22], partially mitigate the heavy demand for labeled data by incorporating residual losses, data efficiency remains a challenge. More recently, meta-learning-based PINNs have been proposed to improve generalization across parameterized PDEs [23–25]. They treat variations in parameters and initial/boundary conditions as subtasks within a unified framework, enabling the model to leverage knowledge across related tasks. Feedforward meta-PINNs, such as Hyper-PINN and Meta-MgNet [26, 27], directly map equation configurations to PINN weights, whereas MAML-based methods, including MAD-PINN (Fig.1 B) and reptile-based PINNs [28, 29], focus on learning initialization states that adapt efficiently to new tasks. Despite these advances, meta-learning PINNs often suffer from long training time and computationally intensive fine-tuning when applied to a wide range of new configurations.

![image 1](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile1.png)

###### Fig. 1: Illustration of the idea, problem setup, and architecture of cd-PINN.

- (A) Schematic diagram of the input and output of neural operators. (B) MAD learns the solution of the equation under new configurations by fine-tuning the encoding c. (C) The objective function of cd-PINN is based on the continuity assumption. (D) Illustration of the labeled training data. For each output u(ti,xi), we require the same number of evaluations of a(ti,xi) and u0(xi) at the same scattered space-time point (ti,xi). (E) The flowchart for calculating residual loss. (F) The architecture of cdPINN.


The continuous dependence of PDE solutions on the initial/boundary values and parameters is one of the fundamental requirements for the well-posedness of PDEs[30], yet it is often overlooked in solving parameterized PDEs. To address the challenges of data inefficiency and repeated training in deep-learning-based solvers, we propose the continuous dependence physics-informed neural network (cd-PINN). By using an

appropriate encoding c for each configuration (e.g. u0), cd-PINN captures a higherdimensional solution space G(A) (shown in Fig.1 C) that continuously depends on both the encoding c and the spatial coordinate x. This design yields substantially improved data efficiency compared with models like DeepONet and FNO, while avoiding the retraining or fine-tuning typically required by PINN variants at the same time. The numerical results demonstrate the outstanding accuracy, reliability, and practicality of our proposed model for solving large-scale parameterized partial differential equations in real-time.

#### 2 Results and Discussion

To validate the outstanding performance of cd-PINN, we conducted numerical experiments on five representative PDEs whose solutions exhibit continuous dependence on their parameters or initial values. These include the three fundamental types of second-order PDEs, including the diffusion, wave, and Poisson equations, as well as high-dimensional diffusion-reaction equations, Burgers, and Navier-Stokes equations. In these examples, we demonstrate the superiority of our method over mainstream operator learning frameworks on diffusion and wave equations, analyze the effect of the loss function Lcd on residual-point density in Poisson equation and on PDE dimensionality in high-dimensional diffusion-reaction equations, and benchmark the efficiency and accuracy of cd-PINN against the traditional finite difference method on the Burgers equation. We also examine the diffusion equation in a setting where the theoretical guarantee of continuous dependence on the initial condition no longer holds. Finally, the proposed model was applied to the tau protein aggregation dynamics in Alzheimer’s disease based on both real and synthetic data. In what follows, the negative logarithm of the mean absolute error (NLMAE) is adopted for performance assessment, which is defined as:

NLMAE = −log10

n

1 n

i=1

uitrue − uipred . (1)

##### 2.1 Benchmarking Against State-of-the-Art Operator Learning Frameworks

To ensure a fair comparison, we evaluate all models on the same example by fixing the form of the initial value while varying its coefficients to test the predictive performance under continuously changing inputs. First, we examine the 1D diffusion equation, which is described by

∂2p ∂x2

∂p ∂t − D

= 0, x ∈ [−10.0,10.0],t ∈ [0.1,1.1] (2)

2

1)2

with initial condition p(x,0) = √102πσ exp − (x−µ)

exp − (x−µ

2σ2 + √210πσ

2σ12 . In practice, we fix σ1 = 1.0,µ1 = 5.0, use 20 labeled data with σ = 1.0,µ = −5.0, and 214 residual data points to train the model. The test data consists of 101,000 sets

1

of solutions corresponding to values of σ ∈ [0.1,10.0] and µ ∈ [−5.0,5.0], totaling 8,080,000 data points.

We conduct a comprehensive validation of our proposed models against existing baseline models, including FNO and DeepONet. As shown in Fig. 2A, we compared the test MSE of each model and tracked its evolution across training epochs with only 20 labeled training data points. The results show that the predictions of DeepONet and FNO are significantly worse than those of cd-PINN, PINN, and cd-PINN#, where PINN means no additional differentiability loss Lcd is added, while cd-PINN# means no explicit encoding is used, but rather encoding is performed using a deep-learningbased encoder (see Supplementary Information). In practice, we experimented with both a MLP-based encoder and an encoder-only Transformer [31] to encode a(t,x) and u0(x), and found the former shows a better performance. In Supplementary Information, we give the results of DeepONet and FNO when labeled training data is 20, 100, 1000, and 10000, respectively, to ensure the correctness of our reproduction model. Panel B in Fig. 2 shows the NLMAE of DeepONet, PINN, cd-PINN and cd-PINN# in the phase space defined by parameters µ and σ. Each point represents the negative logarithm of the mean absolute error between the predicted solution and the true solution for the corresponding (µ,σ). DeepONet, constrained by sparse labeled data and the lack of continuity exploitation with respect to initial values, exhibits significantly lower predictive accuracy compared with cd-PINN#. Compared with cd-PINN#, if we know the specific form of the initial condition p0(x), the NLMAE of PINN can be improved by an order of magnitude, thanks to the inclusion of physical information. By further incorporating the differentiability constraint Lcd on the solution coefficients into PINN, the resulting model not only achieves a higher NLMAE overall but also significantly improves its performance in regions where PINN performs poorly – particularly for small σ. In Fig. 2C, we present the predicted solutions for a new configuration (σ = 0.2,µ = 0.0) unseen during labeled training data. While DeepONet shows a marked deviation from the ground truth, the cd-PINN and cd-PINN# models demonstrate superior generalization by accurately recovering the underlying solution morphology.

To make a further verification, we consider the 2D wave system as a special case of the general hyperbolic equations, which is described by

∂2u ∂t2

= c2

∂2u ∂y2

∂2u ∂x2

+

, x ∈ [0,1], y ∈ [0,1], t ∈ [0,0.5], (3)

with initial condition and boundary conditions

u(x,y,t = 0) = 10sin(kx)sin(ky), ut(x,y,t = 0) = 0, x ∈ [0,1], y ∈ [0,0.5], u(x = 0,y,t) = 0, u(x = 1,y,t) = 10sin(k)sin(ky)cos(

√

2ckt), y ∈ [0,1], t ∈ [0,0.5], u(x,y = 0,t) = 0, u(x,y = 1,t) = 10sin(kx)sin(k)cos(

√

2ckt), x ∈ [0,1], t ∈ [0,0.5]. (4)

In practice, we use 20 labeled data with c = 0.505,k = 0.505 (see Fig. 2G) and 213 residual data points to train the model. The test data consists of 441 sets of solutions

corresponding to values of c ∈ [0.01,1.0] and k ∈ [0.01,1.0], totaling over 4 million data points. To ensure the accuracy of the test, both the training data and the test data are generated with a true solution of the equation. The specific data settings are summarized in Table 1.

Table 1: Summary on the setup and results of diffusion, wave, Poisson, and diffusionreaction equations

Equation Model Params Configurations Labeled Residual NRMSE

cd-PINN ≈ 8 × 104 1 20 16384 5.24 × 10−3

PINN ≈ 8 × 104 1 20 16384 2.07 × 10−2 cd-PINN# ≈ 9 × 104 1 20 16384 8.40 × 10−2 DeepONet ≈ 4 × 104 1 20 − 7.80 × 10−1

Diffusion

FNO ≈ 2 × 105 1 20 − 1.98 × 10−1

cd-PINN ≈ 8 × 104 1 20 8192 1.20 × 10−3 cd-PINN# ≈ 1 × 105 1 20 8192 1.22 × 10−2

Wave

PI-DeepONet ≈ 1 × 105 1 20 8192 3.43 × 10−2 DeepONet ≈ 1 × 105 100 20000 − 1.06 × 10−1

FNO ≈ 9 × 104 100 20000 − 6.58 × 10−1 Poisson

cd-PINN ≈ 8 × 104 1 20 2048 2.68 × 10−3

PINN ≈ 8 × 104 1 20 2048 2.14 × 10−2 D-R 2d

cd-PINN ≈ 8 × 104 1 100 8192 2.12 × 10−3

PINN ≈ 8 × 104 1 100 8192 1.79 × 10−2 D-R 5d

cd-PINN ≈ 8 × 104 1 100 8192 5.36 × 10−3

PINN ≈ 8 × 104 1 100 8192 1.52 × 10−2 D-R 8d

cd-PINN ≈ 8 × 104 1 100 8192 1.61 × 10−1 PINN ≈ 8 × 104 1 100 8192 1.85 × 10−1

![image 2](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile2.png)

- Fig. 2: Results of the parameterized diffusion and wave equations. (A) The test MSE of cd-PINN, PINN, cd-PINN#, FNO, and DeepONet on the test dataset as the number of training epochs increases for the parameterized diffusion equation. (B) The NLMAE of predictions, (C) predictions on new configurations σ = 0.2,µ = 0.0 without labeled training data, and (D) the test MSE as a function of the number of training epochs. (E) The NLMAE, (F) predictions, and (H) absolute errors of cd-PINN, PI-DeepONet, DeepONet, and FNO for parameterized wave equation at c = 0.505,k = 0.505. (G) 20 labeled training data points randomly selected from the low-resolution with c = 0.505,k = 0.505.


As shown in Fig. 2D, after 20,000 training epochs, cd-PINN# exhibits a test MSE nearly one order of magnitude lower than DeepONet and FNO, while cd-PINN achieves a test MSE approximately two orders of magnitude lower than PI-DeepONet. Compared with FNO and DeepONet, cd-PINN and PI-DeepONet have significantly improved in NLMAE due to the addition of equation information (see Fig. 2E). It is worth noting that FNO shows the worst performance, which might be attributed to the fact that FNO is suitable for learning the solution from parameters to a specific time moment, while other models can learn the solution mapping of the entire

time region, in contrast. To align with other models, we also use time t as the input to the FNO. Compared to PI-DeepONet, cd-PINN exhibits a notable advantage in NLMAE across a wide range of parameters and time regions, owing to the inclusion of constraints on the continuous dependence of the solution on the parameters. In addition, we also compared the two models in NRMSE, as shown in Table 1, cd-PINN (1.20 × 10−3) outperforms PI-DeepONet (3.43 × 10−2) by an order of magnitude.

In addition to comparing the four models globally, we also made a comparison between the predicted solutions and true solutions of the four models under the parameter c = 0.505,k = 0.505, which is used for generating training data. Fig. 2F gives a high-resolution true solution and the predicted solutions of cd-PINN, PI-DeepONet, DeepONet, and FNO from left to right, while their absolute errors are shown separately in Fig. 2H. Again, FNO gives the worst prediction results. PI-DeepONet, cd-PINN, and DeepONet can all learn the overall shape of the solution, but in terms of the absolute error, DeepONet is much worse than both cd-PINN and PI-DeepONet. Moreover, cd-PINN has a significant improvement over PI-DeepONet in the maximum absolute error.

##### 2.2 Effect of Residual Point Density

The density of residual points is a key factor influencing the performance of physicsinformed models. As noted in [17], incorporating the equation gradient into the loss can enhance the model’s accuracy even with a few residual points. The primary distinction between cd-PINN and PINN lies in the inclusion of the Lcd term. Here, we investigate how residual point density affects both models and assess the role of Lcd under lowdensity conditions. Consider a 2D Poisson equation, which is a representative of general elliptic equations, specified as

uxx + uyy = −(a2 + b2)cos(ax)sin(by), x ∈ [0,π], y ∈ [0,π], (5) with boundary condition

u(x = 0,y) = sin(by), y ∈ [0,π], u(x = π,y) = cos(aπ)sin(by), y ∈ [0,π], u(x,y = 0) = 0, x ∈ [0,π], u(x,y = π) = cos(ax)sin(bπ), x ∈ [0,π].

(6)

In practice, we use 20 labeled data with a = 2.45,b = 2.45 (see Fig. 3E) and 211 residual data points to train the model. The test data consists of 250 sets of solutions corresponding to values of a ∈ [0.0,5.0] and b ∈ [0.0,5.0], totaling over 2 million data points.

In Fig. 3A, the percentage stacked bar chart shows that cd-PINN achieves a lower NRMSE than PINN across different numbers of residual points, with the gap narrowing as the point density increases. Fig. 3B illustrates that, with 211 residual points, cdPINN maintains a clear advantage in test MSE during training. This improvement may be attributed to the inclusion of Lcd, which prevents the model from being trapped

in a local minimum (Fig. 3C). The benefit of Lcd is also evident in Fig. 3D, where cd-PINN achieves higher NLMAE across a broad range of parameter configurations. The advantage becomes more pronounced for larger values of a and b, corresponding to more complex, high-periodicity solutions. To illustrate this, we compare the true solution (Fig. 3F), and the predicted solutions of cd-PINN and PINN (Fig.3 G) when a = 5.0,b = 5.0. The latter leads to lower absolute errors by an order of magnitude (Fig.3H).

![image 3](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile3.png)

- Fig. 3: Results of the parameterized Poisson equation. (A) Comparison of the NRMSE between cd-PINN and PINN with respect to different numbers of residual points, where the vertical axis represents the number of 2N residual data points used.


- (B) The test MSE and (C) Lcd term of cd-PINN and PINN as the number of training epochs changes when the number of residual points is fixed as 211. (D) The NLMAE of predictions of cd-PINN and PINN. (E) 20 labeled training data points randomly selected from the low-resolution data when a = 2.45,b = 2.45. (F) The high-resolution true solution of the equation at new configurations a = 5.0,b = 5.0. (G) The predicted results and (H) absolute errors of cd-PINN and PINN at configurations a = 5.0,b = 5.0.


##### 2.3 Influence of PDE Dimensionality

One of the major strengths of physics-informed models is their ability to handle highdimensional problems. Here, we investigate the impact of PDE dimensionality on the performance of cd-PINN and PINN using the d-dimensional diffusion-reaction

equation with a negative linear term accounting for degradation.

∂u ∂t

= D∇2u − λu,x ∈ [0.0,0.1]d,t ∈ [0.0,0.1], (7)

whose initial condition reads

d i=1 x2i

1 (2πσ2)d2

exp −

u(x,0) =

2σ2

. (8)

For each d = 2,5,8, we fixed 100 labeled data with D = 0.06,λ = 0.06 and 213 residual data points to train the model. The test data consists of 100 sets of solutions corresponding to values of D ∈ [0.01,0.1] and λ ∈ [−0.1,−0.01].

![image 4](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile4.png)

Fig. 4: Results of the parameterized diffusion-reaction equation. (A), (B), and (C) show results for 2D, 5D, and 8D diffusion-reaction equations, respectively. For each dimension, from left to right: NLMAE of PINN and cd-PINN, test MSE, and Lcd versus training iterations.

Fig. 4 A-C show the results of the cd-PINN and PINN models when applied to the diffusion-reaction equation in 2d, 5d, and 8d, respectively. The first and second columns display the NLMAE of cd-PINN and PINN, respectively. In all dimensions, the incorporation of the loss term Lcd results in a higher NLMAE for cd-PINN than that of PINN. However, since the number of residual points is fixed at 213 across all

cases, the model performance progressively degrades with the increase of dimension due to insufficient sampling of the domain. This highlights a major limitation of PINNbased models: although they can be extended to high-dimensional problems, a large number of residual points are required, and the GPU memory is extremely demanding. The third column illustrates how the test MSE of cd-PINN and PINN evolves over training iterations. The black dashed line represents the transition point between the epochs optimized by the Adam optimizer and those optimized by the LBFGS optimizer. As the dimensionality increases, the number of residual points shifts from sufficient to insufficient, resulting in an increasing performance gap between cd-PINN and PINN. The fourth column illustrates how the loss term Lcd changes during training for both models. Although Lcd is not included in the loss function of PINN, we compute and record it for comparison. In all dimensions, the value of Lcd in PINN converges to a higher level, and this convergence value increases with dimensionality.

##### 2.4 Comparison to FDM

The Burgers equation is a widely used PDE in fluid mechanics, such as in the modeling of nonlinear waves and turbulence. As the viscosity coefficient goes to zero (ν → 0), the solution develops shocks. To compare the computational efficiency and accuracy with traditional FDM, we consider the 1D Burgers equation

∂2u ∂x2

∂u ∂t

∂u ∂x

, x ∈ [−1.0,1.0], t ∈ [0.0,0.5], (9)

+ u

= ν

with initial and boundary conditions

u(x,0) = −sin(πx), x ∈ [−1.0,1.0], u(−1,t) = u(1,t) = 0, t ∈ [0.0,0.5].

(10)

We use this benchmark problem to evaluate the effectiveness and computational efficiency of the proposed cd-PINN model by direct comparison with the Newton-Implicit FDM. Specifically, we use 20 labeled data samples from 200 × 200 numerical solution of Newton-Implicit FDM corresponding to ν = 0.05 and 213 residual data points. The test data consist of 40 solution instances corresponding to values of ν ∈ [0.01,0.1], each with a resolution of 200 × 200. Details of the Newton-Implicit FDM implementation and data generation process are provided in Supplementary Information.

To verify whether cd-PINN can effectively learn the solution of the equation as ν varies, we present the NLMAE of each pair (t,ν) in Fig.5 A. Overall, the mean absolute error of the predicted solution increases over time or as ν decreases. This aligns with our intuitions that the smaller ν is more prone to the formation of shocks. When t > 0.2, the solution transits from a smooth profile to a viscous shock, making it increasingly difficult for the MLP-based model to fit. This explains why minimum NLMAE appears around t ≈ 0.22,ν = 0.01. In Fig.5 D, E, we compare the numerical solutions and predicted solutions of FDM and cd-PINN for ν = 0.01,0.03,0.05,0.10, respectively. The two solutions are visually almost indistinguishable. In Fig. 5F, it can be seen that when ν = 0.01, the maximum absolute error reaches 0.2025, and then

gradually decreases as ν increases. In Fig. 5G, we further present a comparison between the predicted solution of cd-PINN and the numerical solution obtained by FDM at different values of ν at time instances t = 0.0,0.25 and 0.50. In addition to the cases within the residual point sample range ν ∈ [0.01,0.10] – specifically, ν = 0.01,0.05 and 0.10 – we also include the results for the inviscid Burgers equation (ν = 0.00), where the numerical solution is obtained using the Mac-Cormack method. Remarkably, the predicted solution of cd-PINN is almost visually indistinguishable from the numerical solution across all tested values of ν, highlighting the strong generalization ability of the proposed model.

In addition to comparing accuracy, we also evaluate the efficiency of the NewtonImplicit FDM and cd-PINN. The total number of residual points is a major factor determining the trade-off between model accuracy and computational cost. On one hand, more residual points increase the number of gradient computations, thereby extending the training time; on the other hand, they provide more comprehensive physical constraint information, potentially improving the accuracy. To investigate this trade-off, we examine how the number of residual points affects the time required for each training epoch and the final test NRMSE, while keeping other factors – such as network depth/width and number of training iterations – fixed. Fig.5 B shows how the total number of residual points impacts both epoch time and final NRMSE. As the number of residual points increases, the time per epoch increases gradually, while the final NRMSE decreases and then stabilizes. When the number of residual points reaches over 213, we compare the training time, inference time, and cumulative time required for FDM to solve the equation for multiple ν values (Fig.5 C). Especially, when the number of ν values exceeds 30, the cumulative computation time of FDM surpasses the total training time of cd-PINN, while the inference time of cd-PINN remains negligible.

##### 2.5 Applicability to Complex Systems

Besides its accuracy, efficiency and transferability, cd-PINN has a remarkable capability to apply to complex systems and phenomena, which is demonstrated through the 2d Navier-Stokes equation [32] for viscous, incompressible fluid in the vorticity form:

∂ω ∂t

= −u∇ω + ν∆ω + f, ∇u = 0, (11)

where u is the velocity field and ω = ∇×u is the vorticity. u,ω lie on a spatial domain with periodic boundary conditions, ν is the viscosity and f is a constant forcing term. The spatial domain is Ω = [−0.5,0.5) × [−0.5,0.5), the time interval is t ∈ [0.0,0.5], the viscosity is ν ∈ [10−3,10−2], and the forcing term is set as:

f(x1,x2) = 0.1 sin(2π(x1 + x2)) + cos(2π(x1 + x2)) , ∀x ∈ Ω. (12)

Here we use 20 labeled data sampled from 128×128 numerical solution corresponding to ν = 5e−3, and 213 residual data points.

![image 5](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile5.png)

Fig. 5: Results of the parameterized Burgers equation. (A) The NLMAE of predictions of the cd-PINN model under each set of (t,ν). (B) NRMSE and epochs per second v.s. number of residual points. The blue line represents the epochs per second, while the red line represents the NRMSE of the predicted results. (C) Comparison on the computational efficiency of cd-PINN and Newton-Implicit FDM. (D) The numerical solutions of Newton-Implicit FDM, (E) predicted solutions of cd-PINN as well as (F) absolute errors between the two methods at ν = 0.01,0.03,0.05,0.07 and 0.10, respectively. (G) Comparison of cd-PINN predicted solutions and numerical solution obtained via the FDM at t = 0.0,0.25,0.50 for various values of ν.

![image 6](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile6.png)

Fig. 6: Results of the parameterized Navier-Stokes equation. The first row presents the reference solution computed using the spectral method. The second row displays the corresponding predictions obtained by the cd-PINN model, while the third row shows the point-wise absolute errors. From left to right, the viscosity coefficients are set to 1 × 10−3,3 × 10−3,5 × 10−3, and 1 × 10−2, respectively.

This case demonstrates that the proposed cd-PINN is capable to capture the complex vortical behaviors of 2D viscous fluid, even though the model is trained using only a limited number of labeled data samples at a single viscosity coefficient. As shown in Fig. 6, the predictions of cd-PINN agree well with the reference solution in both low and high viscosity regions, and the point absolute error remains small throughout most of the spatial domain.

##### 2.6 Failure of Regularity

Through previous examples, we demonstrate that our model performs well if the solution of the PDEs has a continuous dependence on initial values, parameters, and even source terms. A natural question arises: if there is no theoretical guarantee that the solution has a continuous dependence on the initial values or parameters, can cd-PINN still have an excellent generalization capability?

To address this critical issue, let us consider the initial-value problem of the diffusion equation with negative diffusion coefficients:

∂2u ∂x2

∂u ∂t − D

= 0, (x,t) ∈ QT, u(x,t) = u0(x), (x,t) ∈ ∂pQT,

(13)

where QT = Ω × (0,T), and ∂pQT = Ω × {t = 0}, Ω ⊂ Rn is a bounded region, ∂Ω ∈ C∞, and T > 0. Perform the Fourier transform on the initial value u0(x), and we have uˆ0(k) = −∞∞ u0(x)e−ikxdk, then the solution of the equation can be formally written as:

∞

- 1

- 2π


2teikxdk. (14) It is easily seen that when D > 0, the modal factor e−Dk

uˆ0(k)e−Dk

u(x,t) =

−∞

2t decays with time t, and the high frequency decays faster, so that the solution of this problem remains smooth and stable. In contrast, when D < 0, the model factor becomes e|D|k

2t, the high frequency component grows exponentially, meaning the solution will be exploded within a very small time, and the system becomes ill-posed. To be concrete, consider the onedimensional case with D = −1 and the initial value un(x,0) = e−n sin(nx)[33, 34]. This problem can be explicitly solved with the solution un(x,t) = e−n sin(nx)en

2t. Then un(x,0) → 0 uniformly as n → ∞, so are all its spatial derivatives. But sup

|un(x,t)| → ∞ as n → ∞ for any t > 0. As a consequence, the solution does not continuously depend on the initial value.

x∈R

Although the diffusion equation with negative diffusivity (D < 0) is theoretically ill-posed and lacks continuous dependence on the initial value, the solution may still exhibit transient stability over a short time interval numerically. Consider the same initial value problem as in Section 2.1, but choose D = −0.002. Within the prescribed time window, the solution remains well-defined and unique, with all other settings identical to those in Section 2.1.

![image 7](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile7.png)

Fig. 7: Results of the parameterized diffusion equation with negative diffusion coefficients. The NLMAE of predictions of (A) PINN and (B) cd-PINN under each configuration. The total loss L, continuous dependence loss Lcd, and the test MSE of (C) PINN and (D) cd-PINN as the number of training epochs changes. (E) The true solution (left), and predicted solutions by PINN (middle) and cd-PINN (right) at µ = −5.0,σ = 0.1.

As shown in Fig.7 A and B, although the solution is only stable within a limited time window, both PINN and cd-PINN demonstrate good performance in prediction. The inclusion of Lcd enables cd-PINN to outperform PINN, achieving a prediction NRMSE of 6.65 × 10−2 compared to 1.23 × 10−1 for PINN. Subfigures C and D illustrate the decrease of the total loss, Lcd, and the test MSE over training epochs for PINN and cd-PINN, respectively. Unlike the case of D > 0 in Section 2.1, the MSE does not converge to the same magnitude as the total loss, indicating a certain degree of overfitting. This may be attributed to insufficient regularization of both the PDE loss and the differentiability loss under the ill-posed condition when D < 0. To examine model performance under blow-up conditions, we visualize the true and predicted solutions of PINN and cd-PINN for µ = −5.0, and σ = 0.1 in Fig.7 E. The solution diverges to infinity for t ≥ 2.5, and thus the true solution is omitted beyond this point. While neither model accurately captures the blow-up, cd-PINN provides a prediction close to the true solution in the pre-blow-up regime.

##### 2.7 Real Application: Protein Aggregation Dynamics in Alzheimer’s Disease

Alzheimer’s disease (AD) is a progressive neurodegenerative disorder characterized by the accumulation and spread of misfolded proteins, mainly amyloid β-protein (Aβ) plaques and hyperphosphorylated tau protein tangles, within interconnected brain regions. The spatiotemporal evolution of protein concentration c(x,t) follows the

classical Fisher-Kolmogorov (F-K) equation:

∂c ∂t

= D∇2c + α c(1 − c), (15)

where c(x,t) ∈ [0,1] represents the normalized protein concentration, D is the diffusion coefficient, and α is the aggregation rate. We aim to estimate unknown parameters D,α from few-shot observations.

We adopt an offline-online strategy for this inverse problem, with the complete algorithm detailed in Algorithm S1 (see Supplementary Information). During the offline stage, we first train cd-PINN to approximate the solution c(t,x;D,α) over a wide range of reasonable parameter values. Next, the online stage freezes the network weights and, given observations {cobs(ti,xi)}N

i=1 , estimates D and α by directly solving a least-squares minimization problem

obs

Nobs

1 Nobs

(D∗,α∗) = arg min

D,α

i=1

cˆ(xi,ti;D,α) − c(obsi)

2

, (16)

where cˆ denotes predictions of the pre-trained network with frozen weights. The explicit encoding of parameters (D,α) as network inputs enables gradient-based optimization. Compared to the traditional way of solving inverse problems by using PINNs, our current approach avoids repeatedly re-tuning neural networks for finding a sufficiently good approximation to the PDE solution during parameter updates, and thus saves a huge amount of time which is unaffordable for online tasks.

We first examine our approach with respect to the continuous F-K equation (15) on synthetic data set. Both PINN and cd-PINN are trained at a single parameter configuration (D = 0.3,α = 1.0) and evaluated across a broad parameter range. As shown in Figs. 8A–D, cd-PINN significantly reduces the prediction error throughout the entire parameter space, and shows remarkable improvement in the regions far from the training point. The test MSE convergence curves (Fig. 8E) reveal that cd-PINN not only converges faster but also achieves lower final errors (3.42 × 10−5) than PINN (1.04 × 10−3). For the inverse problem, we evaluate parameter estimation performance across all 99 test configurations (Fig. 8H–I). cd-PINN outperforms PINN in 73 cases (73.7%), achieving an average parameter estimation error of 4.74% compared to 8.23% for PINN. To understand this improvement, we visualize the loss landscapes and optimization trajectories for a representative case with true parameters (D = 0.15,α = 1.30) and initial guess (D = 0.40,α = 0.70) in Fig. 8F–G. The loss landscape of cd-PINN exhibits a smoother, more convex structure that facilitates gradient-based optimization, with the trajectory converging to (D = 0.130,α = 1.299), close to the ground truth. In contrast, the PINN’s landscape contains spurious local minima, and the optimizer converges to (D = 0.100,α = 1.255), a less accurate estimate.

![image 8](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile8.png)

Fig. 8: Evaluation of PINN and cd-PINN for Fisher-Kolmogorov equation in continuous and network settings. Continuous domain (synthetic data): (A–B) MAE and (C–D) NLMAE across diffusion-aggregation parameter space (D,α), with models trained at single configuration. (E) Test MSE convergence during training over 10,000 iterations. (F–G) Loss landscapes for the inverse problem with true parameters D = 0.15 and α = 1.3. ( H) Comparison of parameter estimation errors across all 99 test configurations. (I) Heatmap of error differences in the (D,α) space. Network domain (brain connectome): (J–K) MAE and (L–M) NLMAE heatmaps of PINN and cd-PINN. (N–O) Spatial distribution of prediction errors on the brain connectivity graph. Node colors represent absolute errors at each brain region. (P–Q) Scatter plots of true and predicted solutions for inverse parameter estimation across all test configurations.

The human brain exhibits a complex connectome structure, within which misfolded proteins spread over anatomically connected regions. To account for the network topology, we discretize the continuous spatial domain onto the brain connectome, representing it as a graph with N cortical and subcortical regions. The continuous Laplacian operator ∇2 in the F-K model is then replaced by the graph Laplacian L = Ddeg − A, where A is the adjacency matrix encoding structural connectivity of different brain regions, and Ddeg is the degree matrix. The discretized F-K equation on networks reads:

dc dt

= −DLc + αc ⊙ (1 − c), t ∈ [0,T], (17)

where c ∈ RN represents protein concentrations in N brain regions, ⊙ denotes elementwise multiplication, D > 0 is a constant diffusion coefficient, and α > 0 is the common aggregation rate.

We evaluate the model performance on both synthetic data generated by the discretized F-K equation on a brain network with N = 83 regions and real medical data. For the forward problem, cd-PINN achieves a test MSE of 2.93 × 10−5 compared to 1.81 × 10−4 for PINN. Beyond global accuracy metrics, we also examine the spatial distribution of prediction errors on the brain connectivity graph (Fig. 8N–O). The continuous-dependence requirement enables the cd-PINN to achieve lower spatial errors in all 83 brain regions. For the inverse problem, we tested both models across all parameter combinations with observations added by 2% Gaussian noise. Supplementary Figs. 7 and 8 show detailed temporal predictions for three representative regions of the brain (nodes 0, 40, and 82) in all combinations of parameters. When estimating parameters from simulated observations, the RMSE of cd-PINN across the entire parameter space is lower than that of PINN (Fig. 8P–Q). Especially under low and high concentration conditions, its performance improvement is significant.

To further verify the practical applicability of our method, we then performed patient-specific parameter estimation using real clinical data from the Alzheimer’s Disease Neuroimaging Initiative (ADNI)[35]. Specifically, we use the ADNI UC Berkeley tau partial volume–corrected (PVC) dataset, which provides continuous standardized uptake value ratios (SUVRs) quantifying tau PET uptake, together with FreeSurferdefined regional volumes (in mm3) for each PET region of interest (ROI). In our experiments, we selected subjects with data available for at least four consecutive years from this dataset.

Alzheimer’s disease typically progresses through various clinical stages, ranging from individuals with normal cognition (CN) to those with early mild cognitive impairment (EMCI), mild cognitive impairment (MCI), late mild cognitive impairment (LMCI), and finally patients diagnosed with Alzheimer’s disease (AD). Fig. 9B presents the longitudinal SUVR prediction results for six representative patients at different disease stages. Both PINN and cd-PINN successfully fit the observed data within the measurement period, with the fitting error of cd-PINN is always lower than that of PINN. The shaded area indicates the uncertainty of the model (meaning ±1 standard deviation), while cd-PINN consistently produces more stable extrapolations with tighter confidence bounds. Beyond temporal dynamics, we also examined

the distribution of tau protein in different brain regions. Fig. 9 C displays brain surface SUVR maps for both CN and AD patients at different time points. The upper rows show the observed PET data, while the lower rows display the cd-PINN fitted and predicted values. For the CN patient, throughout the entire observation period as well as the predicted future stages (indicated by question marks), the accumulation of tau protein in most areas of the brain is extremely low. In contrast, the AD patient exhibits substantially higher and more widespread tau pathology. Additional brain surface visualizations for intermediate disease stages (EMCI, MCI, and LMCI patients) are provided in the Supplementary Information.

#### 3 Methods

We consider the dynamical system in the form of

du dt

= P(u,a), in Ω × [0,T], u = g, in ∂Ω × [0,T], u = u0, in Ω¯ × {0}.

(18)

where Ω ⊂ Rd is a bounded, open set, the vector a ∈ A ⊂ Rd

denotes the PDE coefficients (or parameters), and the function g gives a fixed boundary condition, which can also potentially be entered as a parameter. u(t,x) ∈ U = U(Ω) is the unknown for each fixed time point t ≥ 0, where U is a properly defined function space for the PDE solution. u0 ∈ U denotes the initial condition.

a

##### 3.1 Regularity Theory for Parabolic PDE

Here, we take the Cauchy problem of the diffusion equation as an illustration[30].

∂u ∂t − ∆u = f(x,t), (x,t) ∈ QT, u(x,t) = u0(x,t), (x,t) ∈ ∂pQT,

(19)

For the elliptic-type Poisson equation and the hyperbolic-type wave equation, there exist similar results; see Supplementary Information for details. Theorem 1. (Maximum Principle for Cauchy Problem of Diffusion Equation) Suppose u ∈ C2,1(Ω × (0,T]) ∩ C(Ω × [0,T]) solves

∂u ∂t − ∆u = 0, (x,t) ∈ QT,

u(x,t) = u0(x), (x,t) ∈ ∂pQT.

(20)

and satisfies the growth estimate

2

u(x,t) ≤ Aea|x|

, (∀x ∈ Ω, 0 ≤ t ≤ T) (21)

![image 9](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile9.png)

![image 10](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile10.png)

![image 11](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile11.png)

![image 12](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile12.png)

###### 0.0 year 2.8 year 5.9 year

0.0 year 2.8 year 5.9 year

![image 13](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile13.png)

![image 14](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile14.png)

![image 15](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile15.png)

![image 16](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile16.png)

![image 17](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile17.png)

![image 18](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile18.png)

![image 19](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile19.png)

![image 20](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile20.png)

![image 21](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile21.png)

![image 22](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile22.png)

![image 23](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile23.png)

![image 24](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile24.png)

8.0 year

0.0 year 2.8 year 5.9 year 8 year

![image 25](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile25.png)

![image 26](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile26.png)

![image 27](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile27.png)

![image 28](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile28.png)

# ？

![image 29](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile29.png)

![image 30](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile30.png)

![image 31](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile31.png)

![image 32](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile32.png)

![image 33](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile33.png)

![image 34](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile34.png)

![image 35](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile35.png)

![image 36](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile36.png)

###### Observedcd-PINNObservedcd-PINN

![image 37](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile37.png)

![image 38](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile38.png)

![image 39](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile39.png)

![image 40](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile40.png)

- 0
- 1


- 0
- 1


- 0
- 1


![image 41](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile41.png)

![image 42](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile42.png)

![image 43](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile43.png)

![image 44](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile44.png)

![image 45](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile45.png)

![image 46](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile46.png)

![image 47](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile47.png)

![image 48](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile48.png)

![image 49](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile49.png)

![image 50](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile50.png)

![image 51](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile51.png)

![image 52](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile52.png)

![image 53](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile53.png)

![image 54](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile54.png)

![image 55](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile55.png)

![image 56](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile56.png)

![image 57](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile57.png)

![image 58](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile58.png)

![image 59](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile59.png)

![image 60](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile60.png)

![image 61](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile61.png)

![image 62](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile62.png)

![image 63](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile63.png)

![image 64](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile64.png)

![image 65](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile65.png)

![image 66](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile66.png)

![image 67](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile67.png)

![image 68](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile68.png)

![image 69](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile69.png)

![image 70](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile70.png)

![image 71](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile71.png)

![image 72](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile72.png)

![image 73](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile73.png)

![image 74](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile74.png)

![image 75](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile75.png)

![image 76](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile76.png)

![image 77](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile77.png)

![image 78](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile78.png)

![image 79](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile79.png)

![image 80](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile80.png)

![image 81](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile81.png)

![image 82](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile82.png)

![image 83](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile83.png)

![image 84](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile84.png)

1

- 0
- 1


- 0
- 1


- 0
- 1


![image 85](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile85.png)

![image 86](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile86.png)

![image 87](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile87.png)

![image 88](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile88.png)

![image 89](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile89.png)

![image 90](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile90.png)

![image 91](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile91.png)

![image 92](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile92.png)

![image 93](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile93.png)

![image 94](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile94.png)

![image 95](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile95.png)

![image 96](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile96.png)

![image 97](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile97.png)

![image 98](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile98.png)

![image 99](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile99.png)

![image 100](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile100.png)

- 0

- (A)
- (B)
- (C)


- 1


0.0 year 1.0 year 2.0 year 8.0 year

![image 101](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile101.png)

![image 102](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile102.png)

![image 103](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile103.png)

![image 104](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile104.png)

![image 105](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile105.png)

![image 106](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile106.png)

![image 107](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile107.png)

![image 108](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile108.png)

![image 109](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile109.png)

![image 110](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile110.png)

![image 111](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile111.png)

![image 112](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile112.png)

![image 113](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile113.png)

![image 114](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile114.png)

![image 115](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile115.png)

# ？

![image 116](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile116.png)

![image 117](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile117.png)

![image 118](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile118.png)

![image 119](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile119.png)

![image 120](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile120.png)

![image 121](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile121.png)

![image 122](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile122.png)

![image 123](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile123.png)

![image 124](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile124.png)

![image 125](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile125.png)

![image 126](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile126.png)

![image 127](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile127.png)

1

1

![image 128](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile128.png)

![image 129](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile129.png)

![image 130](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile130.png)

![image 131](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile131.png)

![image 132](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile132.png)

![image 133](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile133.png)

![image 134](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile134.png)

![image 135](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile135.png)

![image 136](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile136.png)

![image 137](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile137.png)

![image 138](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile138.png)

![image 139](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile139.png)

0 0

- 0
- 1


![image 140](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile140.png)

![image 141](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile141.png)

![image 142](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile142.png)

![image 143](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile143.png)

![image 144](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile144.png)

![image 145](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile145.png)

![image 146](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile146.png)

![image 147](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile147.png)

![image 148](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile148.png)

![image 149](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile149.png)

![image 150](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile150.png)

![image 151](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile151.png)

![image 152](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile152.png)

![image 153](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile153.png)

![image 154](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile154.png)

![image 155](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile155.png)

![image 156](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile156.png)

![image 157](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile157.png)

![image 158](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile158.png)

![image 159](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile159.png)

![image 160](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile160.png)

![image 161](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile161.png)

![image 162](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile162.png)

![image 163](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile163.png)

![image 164](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile164.png)

![image 165](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile165.png)

![image 166](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile166.png)

![image 167](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile167.png)

![image 168](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile168.png)

![image 169](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile169.png)

![image 170](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile170.png)

![image 171](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile171.png)

![image 172](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile172.png)

![image 173](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile173.png)

![image 174](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile174.png)

![image 175](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile175.png)

![image 176](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile176.png)

![image 177](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile177.png)

![image 178](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile178.png)

![image 179](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile179.png)

1

- 0
- 1


- 0
- 1


![image 180](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile180.png)

![image 181](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile181.png)

![image 182](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile182.png)

![image 183](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile183.png)

![image 184](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile184.png)

![image 185](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile185.png)

![image 186](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile186.png)

![image 187](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile187.png)

![image 188](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile188.png)

![image 189](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile189.png)

![image 190](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile190.png)

![image 191](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile191.png)

![image 192](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile192.png)

![image 193](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile193.png)

![image 194](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile194.png)

![image 195](Li et al._2026_Incorporating Continuous Dependence Qualifies Physics-Informed Neural Networks for Operator Learning_images/imageFile195.png)

0 0

Fig. 9: Patient-specific modeling of tau protein aggregation using real clinical data. (A)Schematic of the cd-PINN framework. Top (Offline Training): Neural network are pre-trained over a wide range of parameters, whose weights θ∗ are saved for online tasks. Bottom (Online Inference): Frozen pretrained network enables fast estimation of α∗,β∗ from new observations without retraining. (B) Longitudinal SUVR predictions for patients across different disease stages (CN, EMCI, MCI, LMCI, AD). Stars: observed data; solid/dashed lines: PINN/cd-PINN predictions; shaded regions: ±1 standard deviation; vertical lines: last observation time. (C) Brain surface SUVR maps comparing CN (top) and AD (bottom) patients. Upper rows: observed PET data; lower rows: cd-PINN fitted/predicted values. “?” indicates unavailable future observations.

21

for constants A, a > 0. Then

sup

u(x,t) = sup

Ω

Ω×[0,T]

u0(x), (22)

where QT = Ω × (0,T), and ∂pQT = Ω × {t = 0}, Ω ⊂ Rn is a bounded region, ∂Ω ∈ C∞, and T > 0.

According to Theorem 1 and some simple proof, we have the following theorem.

Theorem 2. (Existence and Uniqueness of Diffusion Equation) Let u0 ∈ C(Ω), f ∈ C(Ω×[0,T]). Then there exists at most one solution u ∈ C2,1(Ω×(0,T])∩ C(Ω × [0,T]) to the Cauchy problem (19) satisfying the growth estimate |u(x,t)| ≤ Aea|x|

2

, (∀x ∈ Ω,0 ≤ t ≤ T) for constants A,a > 0.

In Theorem 2, we show the existence and uniqueness of the solution to the diffusion equation, which is bounded in Ω ∈ Rn and the boundary ∂Ω ∈ C∞, making it not applicable to general regions. However, we can relax the restrictions on the region as well as the requirements of f and u0. More details can be found in Supplementary Information.

Suppose u1 and u2 are the solutions to equation (19) with the same source term f but different initial conditions u0

2| < ϵ everywhere on ∂pQT, where ϵ ≪ 1 is a given constant. Let w = u1 − u2, it is easy to prove that w is the solution of diffusion equation in (20) with the initial condition u0

, satisfying |u0

1 − u0

###### and u0

1

2

1 −u0

. According to Theorem 1,

2

###### (x) − u0

(x)) ≤ ϵ, (23)

sup

ω(x,t) = sup

(u0

1

2

Ω

Ω×[0,T]

and ω is positive on Ω × [0,T], we have |ω| = |u1 − u2| ≤ ϵ, which means the solution of diffusion equation in (19) is continuously depending on the given initial condition.

On the other hand, towards the diffusion coefficient D in the diffusion equation, we consider the following simple situation. Let the diffusion constants D1 and D2 be greater than 0, satisfying |D1 − D2| < ϵ, where ϵ ≪ 1 is a given positive constant. Let u1,u2 ∈ C∞(Ω) satisfy

- ∂u1 ∂t − D1∆u1 = f(x,t), (x,t) ∈ Ω × (0,T),

- ∂u2 ∂t − D2∆u2 = f(x,t), (x,t) ∈ Ω × (0,T),


u1 = u2 = u0(x,t), (x,t) ∈ Ω × {t = 0}, u1 = u2 = φ(x,t), (x,t) ∈ ∂Ω × (0,T).

(24)

Let D1 = D2 + r (r < ϵ), and ω = u1 − u2, then ω satisfies

∂ω ∂t − D2∆ω = r∆u1, (x,t) ∈ Ω × (0,T),

ω = 0, (x,t) ∈ Ω × {t = 0}, ω = 0, (x,t) ∈ ∂Ω × (0,T).

(25)

That is, ω satisfies a non-homogeneous diffusion equation with an initial boundary value 0 and a source term r∆u1. Theorem 3. (Energy Estimation for Second-Order Parabolic Equations) For the general second-order parabolic equation with initial and boundary conditions as

∂u ∂t −

∂ ∂xi

i,j=1

∂u ∂xj

aij(x,t)

n

+

bi(x,t)

i=1

u(x,t) = g(x,t), (x,t) ∈ Ω × {t = 0}, u(x,t) = 0, (x,t) ∈ ∂Ω × (0,T),

∂u ∂xi

+ c(x,t)u = f(x,t),

(26)

where (aij(x,t))i,j=1,···,n is a positive-definite matrix, that is for a constant α > 0 it satisfies

n

aijξiξj ≥ α|ξ|2, ∀ξ ∈ Rn. (27)

i,j=1

The coefficients on the left side of equation (26) are assumed to be C∞ functions in the region under consideration.

Define QT = Ω × (0,T). Assume u ∈ C∞(Q¯T) is the solution of equation (26), and f ∈ L2(QT), then ∀t ∈ [0,T], we have the estimates

T

f2dxdt , (28)

E(t) ≤ C E(0) +

0 Ω

where E(t) = Ω u2(x,t)dx denotes the energy.

It is easy to verify that ω satisfies the equation (26) and the relevant conditions in Theorem 3, so we get

ω2(x,t)dx ≤ Cr2

Ω

T

∆u21dxdt < ϵ.˜ (29)

0 Ω

It follows that in this case, the solution to the diffusion equation is continuously dependent on the diffusion constant. Regarding the source term, we can also draw similar conclusions based on the energy estimation inequality above.

Towards the parameterized PDE solution problem in (18), a central premise for an algorithm’s success, no matter it is an operator learning or the improved PINN algorithm based on meta-learning, is that the PDE solution is existed and unique under the new parameters and initial/boundary values. Therefore, in this paper, we assume that for any set of configurations in the PDE to be solved, the classical solution exists uniquely without proof.

##### 3.2 PINN with Continuous Dependence (cd-PINN)

We assume that the classical solution u to a PDE system uniquely exists and is bounded for all time and for every u0 ∈ U. Let

G : A × U × [0,T] × Ω  → Rd

, G(a,u0,t,x) = u(t,x), ∀(t,x) ∈ [0,T] × Ω. (30)

u

###### be a nonlinear map. We study maps G which arise as the solution operators of the parametric PDEs. Suppose we have a few observations {aj,u0

###### ,uj}Nj=1, where uj = u(aj,u0

j

,t,x), seen Fig. 1 D. In practice, N is often a very small number. In some of our examples, we choose N = 1.

###### ,t,x) = G(aj,u0

j

j

Now, the question is how to identify and learn the solution to the PDE among multiple configurations. For operator learning methods such as FNO and DeepONet, they build a specific model architecture and systematically learn the manifold architecture of solution mapping. For example, DeepONet aims to learn the mapping function from parameters to solutions: G : u0  → u, see Fig. 1A. For meta-learning based PINN Meta-Auto-Decoder(MAD) [28], it tries to learn a Lipschitz continuous mapping in a low-dimensional space: G¯ : c  → u, where c ∈ C ⊂ Rl(l ≪ da), such that G(A) ⊂ G¯(C), see Fig.1 B. In other words, for any u0 ∈ A, it hopes that there exists c ∈ C satisfying G¯(c) = G(u0).

Our goal is to learn an operator G : (a,u0,t,x)  → u(t,x), where u(t,x) satisfies the parameterized differential equation (18). To this end, we set part of the model’s input to be (t,x) and the model’s output as u(t,x). When we need to obtain the differential equation solution u(t,x) at a new spacetime point in the solution domain that is different from the training point, we can directly call the model for output. Such a kind of design has another advantage. When solving a large class of differential equations, such as heat equations, we can quickly make full use of the information in the equation, as shown in Fig. 1E.

On the other hand, we hope that the operator we learned is still valid when the equation parameters or initial/boundary conditions change, such as the diffusion coefficient or initial conditions in the diffusion equation. Towards this problem, we assume that for these given configurations, there exists a unique encoding c such that the solution directly depends on (x,t,c). As an illustration, the following theorem establishes the mathematical foundation for using neural networks to approximate this continuous mapping from the encoding c to the solution of the Cauchy problem of the diffusion equation.

Theorem 4. Suppose u0 ∈ C(Ω),f ∈ C(Ω × [0,T]), there exists a unique encoding c ∈ Rm such that the solution of the Cauchy problem (19) is continuously depending on c, that is, u(x,t,c) is a continuous function with respect to c. Then ∀ ϵ > 0, there exists N > 0, {αj}Nj=1 ∈ R, {ωj}Nj=1 ⊂ Rn+1+m, and {bj}Nj=1 ⊂ R, such that the following defined function

G(x,t,c) =

N

αjσ(ωjTz + bj), where z = [xT,t,cT]T ∈ Rn+1+m, (31)

j=1

satisfies

|u(x,t,c) − G(x,t,c)| < ϵ. (32) where σ is a general non-polynomial function.

sup

(x,t,c)∈Rn+1+m

Proof. Let z = [xT,t,cT]T ∈ Rn+1+m,K = Ω×R×Rm, then u(x,t,c) can be regarded as u(z), which is continuous on K. Since σ is a general non-polynomial function, it

satisfies the requirements of Cybenko’s theorem [36]. Define a family of functions

G = G(z) =

N

αjσ(ωjTz + bj) : N ∈ N,αj,ωj ∈ Rn+1+m,bj ∈ R . (33)

j=1

According to Cybenko’s theorem or more general Hornik’s theorem [37], G is dense in C(K). That is ∀ϵ > 0, there exists G ∈ G, satisfies

|u(x,t,c) − G(x,t,c)| < ϵ. (34)

sup

(x,t,c)∈Rn+1+m

| |
|---|


Following Theorem 4, to ensure the assumptions are satisfied, we assume that we know the specific functional forms of the parameter a(t,x) and the initial condition u0(x) in the model. Therefore, we can directly use the variable coefficients in a(t,x) and u0(x) as the encoding c, because they have unique encoded a(t,x) and u0(x). Furthermore, there is a solid theoretical basis to tell us that the solution u(t,x) continuously depends on these variables, thus ensuring that the solution uθ we learned is continuously dependent on the encoding.

To enforce the continuity, we incorporate the differentiability constraints of the solution u(t,x) on the variable of parameter a(t,x) and the initial condition u0(x) into the loss function. This idea comes from the continuous dependence constraints of ODEs [38] and PDEs [30], and has achieved great success in plenty of concrete applications [39]. We name the model as cd-PINN, whose loss function can be written

- as L(Θ) = λdataLdata + λresLres + λcdLcd, (35)


where

Ndata

1 Ndata

∥(uˆ − u)(ti, xi, ci)∥22

Ldata =

i=1

Nr

duˆ dt

1 Nr

(ti, xi, ci) − P(ti, xi, uˆi, ci)

Lres =

i=1

N0

1 N0

∥uˆ(t0, xj, cj) − u0(xj, cj)∥22

+

j=1

Nb

2

1 Nb

∥(uˆ − g)(tk, xk, ck)∥22

+

2

k=1

Nb

Nr

2

2

∂2uˆ ∂c∂t −

∂P ∂uˆ

∂P ∂c

∂uˆ ∂c −

∂uˆ ∂c −

1 Nr

1 Nb

∂g ∂c

Lcd =

(ti, xi, ci)

+

(tk, xk, ck)

2

2

i=1

k=1

N0

2

∂uˆ ∂c

1 N0

∂u0 ∂c

(t0, xj, cj) −

,

+

(xj, cj)

2

j=1

###### (36) where c denotes all the variable coefficients in a(t,x) and u0(x).

It is worth noting that our model has a significant superiority over DeepONet and FNO. Once trained, it can be solved quickly in the full-time domain, allowing for arbitrarily high-resolution solutions to be obtained. Compared to the meta-learning-based PINN model, our model does not require fine-tuning and can be deployed immediately after training, similar to recent GPT models [40, 41] for language modeling.

#### 4 Conclusion

In this paper, based on the concept of continuous dependence of the PDE solution on its parameters and initial/boundary values, we propose cd-PINN for solving parameterized PDEs. Compared to existing operator learning frameworks such as DeepONet and FNO, our models require significantly less labeled data. Once trained, the proposed model enables rapid inference of the PDE solution at any point in time and space within the solution domain, thereby achieving high-resolution prediction. Unlike metalearning-based PINN variants such as MAD-PINN, our proposed model can directly output the solution of a PDE after training without requiring retraining or fine-tuning on new configurations. This capability enables efficient deployment in application domains such as climate prediction and medical imaging, where complex PDEs with varying initial and boundary conditions or parameters need to be solved repeatedly and at different scales.

We numerically demonstrate that the proposed model outperforms benchmark methods such as FNO, DeepONet, and PI-DeepONet under small samples. Additionally, we validate the effectiveness of the explicit encoding and differentiability assumptions, as well as the performance of cd-PINN in high-dimensional problems. In the example of Burgers’ equation, we compared the proposed cd-PINN with the Newton-Implicit FDM in terms of computational efficiency, and showed that cd-PINN is more efficient in large-scale simulations. Finally, we evaluate the model on problems where the theoretical assumptions are only approximately satisfied, and find that it remains effective when the solution exhibits transient stability over a short time interval.

There are several promising directions for future work, including extending the model to handle weak solutions of PDEs[42], which are common in problems involving shocks, discontinuous, or other non-smooth behaviors. Addressing such cases would significantly broaden the applicability of the method to real-world phenomena governed by conservation laws or nonlinear dynamics. Another valuable direction is to apply the model to practical domains such as weather forecasting[43], where data is often scarce, high-dimensional, and noisy.

Code & Data availability. The source code and data for this project are available

- at https://github.com/jay-mini/cd-PINN.git.


Acknowledgements. This work was supported by the National Key R&D Program of China (Grant No. 2023YFC2308702), the National Natural Science Foundation of China (12301617), and the Guangdong Provincial Key Laboratory of Mathematical and Neural Dynamical Systems (2024B1212010004).

Author Contributions. Guojie Li: Investigation, Conceptualization, Methodology, Data curation, Formal analysis, Visualization, Writing-original draft. Wuyue Yang: Data Curation, Formal analysis, Visualization, Writing-original draft. Liu Hong: Supervision, Funding Acquisition, Conceptualization, Project Administration, Writing-Review & Editing. All authors reviewed the manuscript.

Competing Interests. Authors declare that they have no conflict of interest.

#### References

- [1] Richard, C., David, H.: Methods of Mathematical Physics: Partial Differential Equations. John Wiley and Sons (2008)
- [2] Raissi, M., Yazdani, A., Karniadakis, G.E.: Hidden fluid mechanics: Learning velocity and pressure fields from flow visualizations. Science 367(6481), 1026– 1030 (2020)
- [3] Tartakovsky, A.M., Marrero, C.O., Perdikaris, P., Tartakovsky, G.D., BarajasSolano, D.: Physics-informed deep neural networks for learning parameters and constitutive relationships in subsurface flow problems. Water Resources Research 56(5), 2019–026731 (2020)
- [4] Goswami, S., Anitescu, C., Chakraborty, S., Rabczuk, T.: Transfer learning enhanced physics informed neural network for phase-field modeling of fracture. Theoretical and Applied Fracture Mechanics 106, 102447 (2020)
- [5] Hennigh, O., Narasimhan, S., Nabian, M.A., Subramaniam, A., Tangsali, K., Fang, Z., Rietmann, M., Byeon, W., Choudhry, S.: Nvidia simnet™: An aiaccelerated multi-physics simulation framework. In: International Conference on Computational Science, pp. 447–461 (2021). Springer
- [6] LeVeque, R.J.: Finite Difference Methods for Ordinary and Partial Differential Equations: Steady-State and Time-Dependent Problems. Classics in Applied Mathematics, vol. 98. SIAM, Philadelphia, PA (2007)
- [7] Zienkiewicz, O.C., Taylor, R.L., Zhu, J.Z.: In: The Finite Element Method: Its Basis and Fundamentals (Seventh Edition), Seventh edition edn., pp. 1–20. Butterworth-Heinemann, Oxford (2013)
- [8] LeVeque, R.J.: Finite Volume Methods for Hyperbolic Problems. Cambridge Texts in Applied Mathematics, vol. 31. Cambridge University Press, Cambridge

(2002)

- [9] Hughes, T.J.R.: The Finite Element Method: Linear Static and Dynamic Finite Element Analysis, p. 803. Prentice Hall, Englewood Cliffs, NJ (1987)
- [10] Esmaeilzadeh, S., Azizzadenesheli, K., Kashinath, K., Mustafa, M., Tchelepi, H.A., Marcus, P., Prabhat, M., Anandkumar, A., et al.: Meshfreeflownet: A physics-constrained deep continuous space-time super-resolution framework. In: SC20: International Conference for High Performance Computing, Networking, Storage and Analysis, pp. 1–15 (2020). IEEE
- [11] Kochkov, D., Smith, J.A., Alieva, A., Wang, Q., Brenner, M.P., Hoyer, S.: Machine learning–accelerated computational fluid dynamics. Proceedings of the National Academy of Sciences 118(21), 2101784118 (2021)


- [12] Raissi, M., Perdikaris, P., Karniadakis, G.E.: Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations. Journal of Computational physics 378, 686–707 (2019)
- [13] Sirignano, J., Spiliopoulos, K.: Dgm: A deep learning algorithm for solving partial differential equations. Journal of computational physics 375, 1339–1364 (2018)
- [14] Yu, B., et al.: The deep ritz method: a deep learning-based numerical algorithm for solving variational problems. Communications in Mathematics and Statistics 6(1), 1–12 (2018)
- [15] Jagtap, A.D., Kharazmi, E., Karniadakis, G.E.: Conservative physics-informed neural networks on discrete domains for conservation laws: Applications to forward and inverse problems. Computer Methods in Applied Mechanics and Engineering 365, 113028 (2020)
- [16] Jagtap, A.D., Karniadakis, G.E.: Extended physics-informed neural networks (xpinns): A generalized space-time domain decomposition based deep learning framework for nonlinear partial differential equations. Communications in Computational Physics 28(5) (2020)
- [17] Yu, J., Lu, L., Meng, X., Karniadakis, G.E.: Gradient-enhanced physics-informed neural networks for forward and inverse pde problems. Computer Methods in Applied Mechanics and Engineering 393, 114823 (2022)
- [18] Lu, L., Jin, P., Pang, G., Zhang, Z., Karniadakis, G.E.: Learning nonlinear operators via deeponet based on the universal approximation theorem of operators. Nature machine intelligence 3(3), 218–229 (2021)
- [19] Kovachki, N., Li, Z., Liu, B., Azizzadenesheli, K., Bhattacharya, K., Stuart, A., Anandkumar, A.: Neural operator: Learning maps between function spaces with applications to pdes. Journal of Machine Learning Research 24(89), 1–97 (2023)
- [20] Li, Z., Kovachki, N., Azizzadenesheli, K., Liu, B., Bhattacharya, K., Stuart, A., Anandkumar, A.: Fourier neural operator for parametric partial differential equations. arXiv preprint arXiv:2010.08895 (2020)
- [21] Wang, S., Wang, H., Perdikaris, P.: Learning the solution operator of parametric partial differential equations with physics-informed deeponets. Science advances 7(40), 8605 (2021)
- [22] Li, Z., Zheng, H., Kovachki, N., Jin, D., Chen, H., Liu, B., Azizzadenesheli, K., Anandkumar, A.: Physics-informed neural operator for learning partial differential equations. ACM/JMS Journal of Data Science 1(3), 1–27 (2024)
- [23] Finn, C., Abbeel, P., Levine, S.: Model-agnostic meta-learning for fast adaptation


- of deep networks. In: International Conference on Machine Learning, pp. 1126– 1135 (2017). PMLR
- [24] Antoniou, A., Edwards, H., Storkey, A.: How to train your maml. In: International Conference on Learning Representations (2018)
- [25] Nichol, A., Schulman, J.: Reptile: a scalable metalearning algorithm. arXiv preprint arXiv:1803.02999 2(3), 4 (2018)
- [26] Avila Belbute-Peres, F., Chen, Y.-f., Sha, F.: Hyperpinn: Learning parameterized differential equations with physics-informed hypernetworks. The symbiosis of deep learning and differential equations 690 (2021)
- [27] Chen, Y., Dong, B., Xu, J.: Meta-mgnet: Meta multigrid networks for solving parameterized partial differential equations. Journal of computational physics 455, 110996 (2022)
- [28] Huang, X., Ye, Z., Liu, H., Ji, S., Wang, Z., Yang, K., Li, Y., Wang, M., Chu, H., Yu, F., et al.: Meta-auto-decoder for solving parametric partial differential equations. Advances in Neural Information Processing Systems 35, 23426–23438

(2022)

- [29] Liu, X., Zhang, X., Peng, W., Zhou, W., Yao, W.: A novel meta-learning initialization method for physics-informed neural networks. Neural Computing and Applications 34(17), 14511–14534 (2022)
- [30] Evans, L.C.: Partial Differential Equations, 2nd edn. Graduate Studies in Mathematics, vol. 19. American Mathematical Society, Providence, RI (2022)
- [31] Radford, A., Wu, J., Child, R., Luan, D., Amodei, D., Sutskever, I., et al.: Language models are unsupervised multitask learners. OpenAI blog 1(8), 9

(2019)

- [32] Stokes, G.G., et al.: On the effect of the internal friction of fluids on the motion of pendulums (1851)
- [33] H¨rmander, L.: The Analysis of Linear Partial Differential Operators III: PseudoDifferential Operators. Springer, Berlin Heidelberg (2007)
- [34] Bers, L., John, F., Schechter, M.: Partial Differential Equations. American Mathematical Society, Providence, RI (1964)
- [35] Petersen, R.C., Aisen, P.S., Beckett, L.A., Donohue, M.C., Gamst, A.C., Harvey, D.J., Jack Jr, C., Jagust, W.J., Shaw, L.M., Toga, A.W., et al.: Alzheimer’s disease neuroimaging initiative (adni) clinical characterization. Neurology 74(3), 201–209 (2010)


- [36] Cybenko, G.: Approximation by superpositions of a sigmoidal function. Mathematics of control, signals and systems 2(4), 303–314 (1989)
- [37] Hornik, K., Stinchcombe, M., White, H.: Multilayer feedforward networks are universal approximators. Neural networks 2(5), 359–366 (1989)
- [38] Hartman, P.: Ordinary Differential Equations. SIAM, Philadelphia, PA (2002)
- [39] Li, G., Ran, S., Yang, W., Hong, L.: Improving generalization ability of deeplearning-based ode solvers using continuous dependence. npj Artificial Intelligence 1(1), 22 (2025)
- [40] Brown, T., Mann, B., Ryder, N., Subbiah, M., Kaplan, J.D., Dhariwal, P., Neelakantan, A., Shyam, P., Sastry, G., Askell, A., et al.: Language models are few-shot learners. Advances in neural information processing systems 33, 1877–1901 (2020)
- [41] Achiam, J., Adler, S., Agarwal, S., Ahmad, L., Akkaya, I., Aleman, F.L., Almeida, D., Altenschmidt, J., Altman, S., Anadkat, S., et al.: Gpt-4 technical report. arXiv preprint arXiv:2303.08774 (2023)
- [42] Kharazmi, E., Zhang, Z., Karniadakis, G.E.: Variational physics-informed neural networks for solving partial differential equations. arXiv preprint arXiv:1912.00873 (2019)
- [43] Pathak, J., Subramanian, S., Harrington, P., Raja, S., Chattopadhyay, A., Mardani, M., Kurth, T., Hall, D., Li, Z., Azizzadenesheli, K., et al.: Fourcastnet: A global data-driven high-resolution weather model using adaptive fourier neural operators. arXiv preprint arXiv:2202.11214 (2022)


