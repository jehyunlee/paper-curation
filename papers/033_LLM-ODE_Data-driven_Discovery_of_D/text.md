# arXiv:2603.20910v1[cs.LG]21 Mar 2026

## LLM-ODE: Data-driven Discovery of Dynamical Systems with Large Language Models

Amirmohammad Ziaei Bideh

aziaeibideh@gradcenter.cuny.edu The Graduate Center, CUNY New York, New York, USA

### Abstract

Discovering the governing equations of dynamical systems is a central problem across many scientific disciplines. As experimental data become increasingly available, automated equation discovery methods offer a promising data-driven approach to accelerate scientific discovery. Among these methods, genetic programming (GP) has been widely adopted due to its flexibility and interpretability. However, GP-based approaches often suffer from inefficient exploration of the symbolic search space, leading to slow convergence and suboptimal solutions. To address these limitations, we propose LLM-ODE, a large language model-aided model discovery framework that guides symbolic evolution using patterns extracted from elite candidate equations. By leveraging the generative prior of large language models, LLM-ODE produces more informed search trajectories while preserving the exploratory strengths of evolutionary algorithms. Empirical results on 91 dynamical systems show that LLM-ODE variants consistently outperform classical GP methods in terms of search efficiency and Pareto-front quality. Overall, our results demonstrate that LLM-ODE improves both efficiency and accuracy over traditional GP-based discovery and offers greater scalability to higher-dimensional systems compared to linear and Transformer-only model discovery methods.

### CCS Concepts

• Computing methodologies → Machine learning; • Mathematics of computing → Genetic programming.

### Keywords

Equation Discovery, Symbolic Regression, Dynamical Systems, Genetic Programming, Large Language Models

ACM Reference Format:

Amirmohammad Ziaei Bideh and Jonathan Gryak. 2026. LLM-ODE: Datadriven Discovery of Dynamical Systems with Large Language Models. In Proceedings of Genetic and Evolutionary Computation Conference (GECCO ’26). ACM, New York, NY, USA, 17 pages. https://doi.org/XXXXXXX.XXXXXXX

Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than the author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org.

GECCO ’26, San José, Costa Rica © 2026 Copyright held by the owner/author(s). Publication rights licensed to ACM. ACM ISBN 978-1-4503-XXXX-X/2018/06 https://doi.org/XXXXXXX.XXXXXXX

Jonathan Gryak

jonathan.gryak@qc.cuny.edu Queens College and The Graduate Center, CUNY New York, New York, USA

1. Observed Trajectory

2. LLM-based Optimization

Sample equations

| |Population|
|---|---|
| | |


| | |
|---|---|
|Optimization| |


|LLM| | |
|---|---|---|
| | | |


Generate equation skeletons

3. Model Selection via Pareto Front

Cartesian product

Figure 1: Schematic overview of LLM-ODE. (1) Given trajectory data from an unknown dynamical system, the observations are decomposed into state variables. (2) A large language model acts as an evolutionary operator, guiding the evolution of symbolic equation populations toward higherfitness candidates. (3) The final system of equations is selected from the Cartesian product of equation-level Pareto fronts.

### 1 Introduction

Many natural and engineered phenomena are governed by systems of differential equations. Identifying the underlying governing equations is fundamental to understanding system dynamics and enables accurate prediction, analysis, and control across scientific domains such as physics, biology, chemistry, and engineering. Traditionally, the discovery of such equations has relied heavily on domain expertise, physical intuition, and manual derivation. While effective in well-understood settings, this process is time-consuming, difficult to scale, and increasingly inadequate for modern data-rich scientific problems.

Motivated by the growing availability of experimental and simulation data, data-driven model discovery methods have emerged as a promising alternative for uncovering interpretable governing equations directly from observations. Among these approaches, genetic programming (GP) [15] has been one of the most widely adopted tools for symbolic equation discovery due to its flexibility and expressiveness. However, GP-based methods typically rely on stochastic mutation and crossover operators, which often lead to inefficient exploration of the vast combinatorial search space of

symbolic expressions [16]. As a result, GP can suffer from slow convergence, limited scalability, and difficulty in discovering highquality equations for complex or high-dimensional dynamical systems.

Recent advances in large language models (LLMs) suggest a new opportunity to address these challenges. Beyond their success in natural language processing [32] and code generation [20], LLMs have demonstrated strong capabilities in scientific reasoning and discovery [35], optimization [38], and black-box recombination [19, 24]. These models implicitly capture rich structural and syntactic patterns from large corpora, making them well suited to propose meaningful symbolic expressions and transformations. This raises a natural question: can LLMs be used to guide symbolic evolution toward more informative and efficient search trajectories?

In this work, we answer this question by introducing LLM-ODE, an LLM-guided genetic programming framework for discovering the governing equations of dynamical systems. As illustrated in Figure 1, LLM-ODE replaces conventional stochastic evolutionary operators, such as random mutation and crossover, with LLM-generated proposals that exploit patterns observed in high-performing candidate equations. Given observed trajectory data from an unknown dynamical system, LLM-ODE decomposes the system into its state variables and evolves symbolic expressions for each governing equation using LLM-guided operators. Candidate equations are evaluated using multi-objective criteria, and final systems are selected from the Cartesian product of equation-level Pareto fronts.

While prior work has explored LLM-based symbolic regression for discovering single equations, to the best of our knowledge this is the first method that leverages LLMs within an evolutionary framework to discover systems of coupled differential equations describing dynamical systems. By combining the generative prior of LLMs with the diversity of evolutionary search, LLM-ODE aims to achieve more efficient and scalable model discovery.

Our main contributions are summarized as follows:

- • We introduce a new LLM-aided framework that leverages the strength of LLMs and evolutionary search to discover the governing equations of dynamical systems.
- • We conduct acomprehensiveempirical evaluation on a benchmark suite of 91 dynamical systems, spanning one to four state variables and including chaotic dynamics.
- • We show that LLM-ODE, across multiple LLM variants, consistently outperforms traditional GP in terms of search efficiency and system Pareto-front quality.


### 2 Related Work

Symbolic regression (SR) methods aim to infer interpretable equations directly from data. More broadly, model discovery methods seek to uncover analytical expressions that govern nonlinear dynamical systems. In contrast with other ML algorithms, SR methods enjoy several advantages [12]: 1) they do not need a predefined model structure, 2) they automatically generate concise, humanreadable equations modeling the relationship between data, and 3) they often exhibit stronger extrapolation performance, a property more pronounced in scarce-data settings [36].

Model discovery approaches can be categorized into several groups. Linear Models (LM), pioneered by SINDy [8] and its extensions, e.g., Messenger and Bortz [23], work with the assumption that the governing equations are a linear combination of predefined basic functions with sparse scalar coefficients. Such methods impose a strong prior on the equation space – linearity in library terms – which can be useful in discovering simple models with few involving variables. These methods are limited by the need for specifying data-specific candidate library terms, which hinders the scalability of the scientific discovery task.

GP methods relax the linearity assumption and aim to search among the expression trees that best fit the data. These methods, such as Cranmer [10] and Burlacu et al. [9], iteratively evolve a pool of expression trees through evolutionary variations between equations while maintaining high-performing equations. It has been shown that GP methods remain among the most accurate approaches for model discovery [1, 4, 18]. One of the limitations of GP-based methods for SR is their inefficiency in exploring the search space, mainly due to the repeated evaluation of semantically equivalent equations during the search process [16].

Large-scale pretraining (LSPT) algorithms are Transformer models [33] that are pre-trained on a large synthetic SR dataset. The pre-trained model auto-regressively generates symbolic equations directly from new data points [5, 11, 14]. While some methods optimize the constants in the equations with an external component [5], in other methods, the Transformer directly produces complete mathematical equations [11]. More recent work adds search components such as Monte Carlo Tree Search to LSPT methods to improve the transformer equation generation process [28].

LLM-aided methods have flourished from a recently developed paradigm for scientific discovery [27], where LLMs’ optimization [38] and in-context learning abilities [24] are leveraged as intelligent variational operators [6]. LLM-SR [29] aims to uncover the governing equations given a natural language description of the scientific problem. Merler et al. [22] omits the equation descriptions and includes data points directly in the LLM input. [13] introduces an LLM-aided GP framework for model discovery of nonlinear dynamics, limited to dynamics solely with one state variable. More recent work allows more LLM flexibility by promoting the LLM as an autonomous AI scientist that can perform explanatory data analysis for scientific discovery [37].

For a more comprehensive analysis of model discovery methods, see Aldeia et al. [1], Bideh et al. [4], Dong and Zhong [12].

### 3 Methodology 3.1 Problem Statement

We consider the problem of discovering governing equations of an unknown dynamical system from observed trajectory data. Let X ∈ R𝑁×𝐷 denote a time series of 𝑁 samples of a 𝐷-dimensional state x(𝑡) = (𝑥1(𝑡), . . .,𝑥𝐷(𝑡)). The system is assumed to evolve according to a set of autonomous ordinary differential equations (ODEs)

x𝑖 = 𝑓𝑖(x), 𝑖 = 1, . . .,𝐷,

where each 𝑓𝑖 : R𝐷 → R is an unknown symbolic expression.

Our goal is to recover a system 𝑆 := {𝑓1, . . ., 𝑓𝐷}

that accurately reproduces the observed dynamics while remaining compact and interpretable. To formalize this trade-off, we define the complexity of an expression 𝑓 as the number of nodes in its expression tree, denoted C(𝑓 ). The complexity of a system is then

∑︁𝐷

C(𝑆) =

##### C(𝑓𝑖).

𝑖=1

We seek models that jointly minimize prediction error and symbolic complexity.

### 3.2 Overview of LLM-ODE

LLM-ODE is a hybrid symbolic regression framework that combines GP with LLMs to improve search efficiency in the space of symbolic expressions. Classical GP-based symbolic regression methods often suffer from inefficient exploration of the exponentially large space of expression trees, leading to slow convergence and premature stagnation [16]. LLM-ODE addresses this limitation by using an LLM to propose structurally informed mutations and recombinations, leveraging patterns observed in high-performing equations [6, 25].

The algorithm follows an island-based evolutionary strategy [10], where multiple populations evolve in parallel. Each island maintains a population of candidate symbolic expressions and evolves independently for several iterations, promoting exploration of diverse regions of the search space.

Rather than searching directly over full systems of equations, LLM-ODE decomposes the problem across state variables. For each state variable 𝑥𝑖, the algorithm independently learns a symbolic approximation of its time derivative 𝑓𝑖(x). This decomposition reduces the combinatorial complexity of the search and allows targeted optimization of each equation.

Algorithms 1, 2, and 3 summarize the pseudocode of LLM-ODE. Each population is initialized with two randomly generated simple equations of complexity three, and is subsequently evolved in an iterative manner.

At each iteration,𝑘 individuals are sampled from the current population according to a softmax distribution proportional to exp(𝑠), where 𝑠 denotes the fitness score computed with Equation 1. The selected individuals are used as in-context examples to prompt the LLM, which proposes 𝑏 candidate expressions intended to improve upon the sampled equations.

For each candidate, the symbolic structure is fixed while its numerical constants and coefficients are optimized on the training data using an external numerical optimizer. The resulting expressions are then evaluated, and the optimized candidates are inserted back into the population for subsequent evolution.

Eachislandevolvesindependentlyand may therefore over-specialize

in a restricted region of the equation search space. To alleviate this effect and promote broader exploration, we introduce a periodic refinement step. After every 𝑛refine evolutionary rounds, 𝑛mix equations from each island are randomly exchanged with another island, after which the lower-performing half of each population is pruned. This mechanism encourages information sharing across islands

while maintaining selection pressure, thereby improving diversity and preventing premature convergence.

After completing𝑛iter iterations, the algorithm returns the Pareto front of individuals with respect to symbolic complexity and prediction error. In this setting, the Pareto front consists of all expressions 𝑓𝑖 such that there exists no 𝑓𝑗 satisfying

C(𝑓𝑗) ≤ C(𝑓𝑖) and S(𝑓𝑗) > S(𝑓𝑖),

where C(·) denotes symbolic complexity and S(·) denotes the fitness score. The fitness score is defined as negative mean squared error

S(𝑓𝑖) = −MSE ( x, 𝑓𝑖 (x)) . (1)

To construct a final system of ordinary differential equations, we further aggregate candidate equations into systems and compute a second Pareto front over systems, trading off total complexity and trajectory-level accuracy. System-level fitness is defined as the negative mean squared error (MSE) between predicted and observed trajectories on a validation set,

T (𝑆) = −MSE 𝑆(x0), x ,

where 𝑆(x0) denotes the trajectory obtained by numerically integrating system 𝑆 from the observed initial condition x0.

To balance model complexity and predictive accuracy, we select the final discovered system from the system-level Pareto front S = {𝑆1, . . .,𝑆𝑀} by identifying the point of maximum marginal gain in trajectory fitness per unit increase in complexity. Specifically, we solve

##### T (𝑆𝑖) − T (𝑆𝑖−1) C(𝑆𝑖) − C(𝑆𝑖−1)

s.t. T (𝑆𝑖) ≥ ℎ Tmax, (2)

arg max

𝑖∈{2,...,𝑀}

where Tmax = max𝑖 T (𝑆𝑖). The threshold ℎ = 0.1 prevents premature selection of overly simple but inaccurate systems by restricting the search to sufficiently well-performing candidates.

#### Algorithm 1 LLM-ODE

- 1: Input: ODE trajectories X = {Xtrain, Xval}
- 2: Output: optimal system of equations 𝑆∗
- 3: Param: minimum accuracy threshold ℎ
- 4: 𝑛 ← number of state variables
- 5: 𝐸 ← {} // Pareto fronts
- 6: for 𝑖 ← 1 to 𝑛 do
- 7: 𝑦train,𝑦val ← approximate𝑑𝑥𝑖/𝑑𝑡 for Xtrain, Xval, respectively
- 8: 𝐸′ ← LLMSymReg(Xtrain, Xval,𝑦train,𝑦val)
- 9: 𝐸 ← 𝐸 ∪ {𝐸′}
- 10: end for
- 11: systemPool ← cartesianProduct(𝐸) // pool of system of equations from all the combinations of discovered equations
- 12: systemPF ← System Pareto front of systemPool
- 13: 𝑆∗ ← argmax𝑆∈systemPF ΔT(𝑆)

ΔC(𝑆) s.t. T (𝑆) ≥ ℎTmax

- 14: Return 𝑆∗


- Algorithm 2 LLMSymReg (LLM-aided symbolic regression)

- 1: Input: Xtrain, Xval,𝑦train,𝑦val
- 2: Output: equations along the Pareto front 𝐸
- 3: Param: number of populations or islands 𝑛𝑝, number of iterations 𝑛iter, refinement frequency 𝑛refine, number of equations to mix 𝑛mix
- 4: // initialize seed equations
- 5: for 𝑖 ← 1 to 𝑛𝑝 do
- 6: 𝑃𝑖 ← 2 random, simple equations
- 7: for 𝑝 in 𝑃𝑖 do
- 8: Optimize constants in 𝑝 to minimize MSE(𝑦train,𝑝(Xtrain))
- 9: end for
- 10: end for
- 11: for 𝑛 ← 1 to 𝑛iter do
- 12: for 𝑖 ← 1 to 𝑛𝑝 do
- 13: 𝑃𝑖 ← evolve(𝑃𝑖, Xtrain,𝑦train(𝑖) )
- 14: end for
- 15: if 𝑛 mod 𝑛refine = 0 then
- 16: Prune all islands ∪𝑖𝑃𝑖
- 17: Sample 𝑛mix equations from every island and add to another random island
- 18: end if
- 19: end for
- 20: 𝑃 ← ∪𝑖𝑃𝑖
- 21: 𝐸 ← Pareto front of 𝑝 ∈ 𝑃 on Xval,𝑦val
- 22: Return E


- Algorithm 3 evolve (LLM-aided Evolution)

- 1: Input: an island consisting of single equations 𝑃, observed trajectory Xtrain, target values 𝑦
- 2: Output: evolved island 𝑃
- 3: Param: LLM 𝜋, number of in-context examples 𝑘, number of samples per prompt 𝑏
- 4: score ← 𝑝 ∈ 𝑃 : −MSE(𝑦,𝑝(Xtrain))
- 5: 𝑤 ← 𝑒𝑒scorescore

- 6: 𝑄 ← sample 𝑘 equations from island 𝑃 weighted by 𝑤
- 7: 𝑄′ ← sample𝑏 new equations from the LLM 𝜋 given in-context examples 𝑄
- 8: optimize constants in 𝑝 ∈ 𝑄′ to minimize MSE(𝑦,𝑝(Xtrain))
- 9: 𝑃 ← 𝑃 ∪ 𝑄′
- 10: Return P


- 4 Experiments


### 4.1 LLM-ODE Setup

As noted in prior work [30], a key challenge in evaluating LLMaided methods for scientific discovery is the memorization problem, whereby well-known scientific equations may have been encountered during the LLM’s pretraining phase. To mitigate this issue, we remove any information about the semantic meaning of state variables and the underlying physical characteristics of the dynamical system from the input prompts. This design choice encourages the LLM to rely on structural reasoning and pattern matching [25], rather than direct recall of memorized equations.

Listing 1 Example input prompt with 𝑘 = 8 in-context examples and 𝑏 = 3 generated equations.

// LLM input [

{

"role": "system", "content": "You are a scientist whose task is to perform

Symbolic Regression. You should search the function space to find the best simple function that fits the data. You are given 8 examples of proposed equations sorted from worst to best. Your goal is to suggest 3 improved equations of varying complexity. Replace all numerical constants with "C" -- they will be optimized with an external optimizer. Write one equation per line from simplest to most complex with no extra explanation. Available operators: +, -, *,

↩→ ↩→ ↩→ ↩→ ↩→ ↩→ ↩→ ↩→ ↩→ ↩→ ↩→

**, /, sin, log, exp, abs. Independent variables: x_0, x_1, x_2."

}, {

"role": "user", "content": "x_1**C C*x_0 + x_1 C*sin(x_2) C*log(exp(x_2) + Abs(x_1)) C*x_0 + C*sin(x_2) C*x_0*x_1 (C + Abs(x_2))**C*(C*x_0**C + C*exp(x_1)) C*log(x_0 + Abs(x_1)) + C*sin(x_2)"

}

] // LLM output [

{

"role": "assistant", "content": "C*x_0 + C*log(Abs(x_1) + 1) C*(x_0 + sin(x_2)) * exp(x_1) C*(x_0**2 + x_1**2) / (1 + abs(x_2))"

} ]]

To account for variability across language models, we evaluate LLM-ODE using three different LLM backends: Qwen3-30B-A3B-

Instruct-2507 (Qwen) [31], Ministral-3-14B-Instruct-2512 (Mistral) [21], and Olmo-3.1-32B-Instruct (Olmo) [26]. All models are served using vLLM, which provides high-throughput inference via efficient key-value cache management with PagedAttention [17].

The LLM-ODE framework employs four independent evolutionary islands, each initialized with two seed expressions. Each island is evolved for 200 iterations, with the number of in-context examples set to 𝑘 = 8 and the number of samples per prompt set to 𝑏 = 3. The refinement procedure is applied every 𝑛refine = 5 iterations.

The input to the framework consists of a single observed trajectory along with estimated time derivatives. Throughout this work, we compute derivatives using a fourth-order finite-difference

scheme [3]. These derivatives are used to optimize constant placeholders in candidate equations via the BFGS algorithm [7]. Discovered systems of ordinary differential equations are then simulated using SciPy’s ODE solver [34], which employ explicit Runge-Kutta integration. The set of admissible mathematical operators is restricted to {+, −, /, ^, sin, log, exp, abs} and is explicitly specified in the input prompt. A representative prompt and corresponding LLM-generated output are provided in Listing 1.

To promote reproducibility and facilitate future research, we release the full source code for dataset generation, LLM-ODE, and all baseline methods in a publicly available GitHub repository.

### 4.2 Baseline Methods

In order to assess the significance of the improvement in model discovery using the proposed framework, we evaluate three different methods from distinct algorithmic classes to establish a baseline. PySR [10] is an efficient implementation of a GP algorithm. This method serves as a baseline for a regular GP algorithm with no heuristic used in guiding the search space exploration. SINDy [8] and ODEFormer [11] are included as representative approaches from LM and LSPT methods, respectively.

To make a fair comparison, we have endeavored to make the training process for all the baseline models similar to LLM-ODE. PySR performs SR on each state variable separately and computes a set of complexity-error Pareto fronts for each equation in the system. We follow the same procedure as LLM-ODE to construct the proposed system of equations and balance the tradeoff.

We train PySR for 200 iterations with 4 islands, 3 cycles per iterations, 20 individuals, and the same set of allowed operators as in LLM-ODE. The SINDy model is trained using the STLSQ algorithm with all the combinations in the hyperparameter search space, which is shown in Table 2 in Appendix. For ODEFormer, we follow the authors’ guidelines and set beam size to 50 and use a temperature of 0.1. We consider the 50 generated systems resulting from beam search as the Pareto front. All baseline models use Equation 2 to pick the final discovered system of equations along the system Pareto front.

### 4.3 Dataset

We evaluate LLM-ODE alongside several baseline methods on a comprehensive suite of 91 dynamical systems, all simulated from real-world models. Our experiments begin with the ODEBench dataset [11] (𝑛 = 63), which provides a diverse set of systems for benchmarking. Upon inspection, we observed that the ODEBench dataset is heavily skewed toward systems with fewer state variables, limiting its coverage of high-dimensional and chaotic dynamics. To address this gap, we extend the dataset with additional systems exhibiting more complex behaviors, resulting in a total of 23 systems with 𝐷 = 1, 28 with 𝐷 = 2, 22 with 𝐷 = 3, and 18 with 𝐷 = 4. Detailed specifications of the equations and their parameters are provided in Appendix B and in the code supplementary material.

For each system, we generate two distinct trajectories corresponding to different initial conditions. One trajectory is used for training, while the other serves as the test set. All trajectories are integrated over the time interval (measured in seconds) 𝑡 = 0 to 𝑡 = 10 using a uniform sampling interval of 0.1 seconds. In our

experiments, we use the trajectory segment from 𝑡 = 0 to 𝑡 = 5 for parameter optimization. The full training trajectory is then employed for model selection to ensure robust evaluation across different dynamical regimes.

### 4.4 Results

- 4.4.1 System Discovery. Table 1 reports the number of systems successfully discovered by each method as a function of the normalized mean squared error (NMSE) threshold 𝜆, stratified by system dimensionality 𝐷. A successful discovery is defined as achieving a test trajectory NMSE below 𝜆. We use NMSE rather than MSE to normalize for differences in the scale of state variables across systems, enabling fairer comparisons between systems of varying magnitudes.

Across all dimensions, performance degrades monotonically as the error tolerance becomes stricter (smaller 𝜆), which is expected and validates the consistency of the evaluation. Lower-dimensional systems (𝐷 = 1 and 𝐷 = 2) are substantially easier to recover than higher-dimensional ones (𝐷 = 3, 4), indicating a sharp increase in discovery difficulty with state dimension.

The LLM-ODE variants consistently outperform or match classical GP baseline across nearly all settings. For 𝐷 = 1, LLM-ODE methods recover a large fraction of systems even at stringent thresholds (𝜆 ≤ 10−4), whereas PySR, ODEFormer, and SINDy exhibit a more rapid drop-off in successful discoveries.

LLM-ODE methods consistently outperform ODEFormer across all system classes and error thresholds. This observation suggests that purely Transformer-based approaches may be limited in their ability to directly infer precise governing equations from raw observational data. In contrast, hybrid frameworks that integrate learned priors with an explicit symbolic search component appear to yield more accurate and reliable system discovery.

For low-dimensional dynamical systems with a single state variable (𝐷 = 1), LLM-ODE achieves consistently higher discovery rates than PySR and SINDy across a wide range of error thresholds. In intermediate dimensions (𝐷 = 2, 3), SINDy attains competitive, and in some regimes higher, discovery rates relative to other methods. However, this trend does not persist in higher dimensions: for 𝐷 = 4, SINDy’s performance collapses, while LLM-ODE variants continue to successfully recover multiple systems. The degradation of SINDy in higher dimensions is likely due to the exponential growth of candidate library terms and the resulting difficulty of sparse regression. In contrast, LLM-ODE methods remain effective and discover substantially more systems than stochastic genetic programming approaches, highlighting their superior scalability in complex search spaces.

These results demonstrate that LLM-guided search substantially improves symbolic system discovery, particularly under strict accuracy constraints and increasing system complexity. The consistent advantage of LLM-ODE over PySR suggests that leveraging language-model priors enables more effective exploration of the hypothesis space than uninformed symbolic search.

- 4.4.2 Convergence Rate. Figure 2 illustrates the discovery rate of GP-based methods as a function of search iterations across various successful discovery thresholds. Across all tested precision thresholds, LLM-ODE methods consistently outperform PySR in


#### Table 1: Number of discovered systems by method based on test trajectory accuracy. A successful discovery corresponds to a system with test trajectory NMSE below 𝜆. The dataset is stratified with respect to the number of state variables 𝐷, followed by the number of relevant systems. In almost all cases, LLM-ODE methods achieve a higher or equal discovery rate compared to PySR, suggesting the superiority of LLM-based search to uninformed search.

Method D = 1 (𝑛 = 23) D = 2 (𝑛 = 28) D = 3 (𝑛 = 22) D = 4 (𝑛 = 18) 𝜆 10−1 10−2 10−3 10−4 10−5 10−6 10−1 10−2 10−3 10−4 10−5 10−6 10−1 10−2 10−3 10−4 10−5 10−6 10−1 10−2 10−3 10−4 10−5 10−6

|LLM-ODE (Mistral) 20 19 16 15 13 8 LLM-ODE (Olmo) 21 19 18 16 11 8 LLM-ODE (Qwen) 21 20 17 16 13 8 PySR 20 20 16 13 8 6|15 10 7 6 3 1<br><br>18 12 10 9 5 1 17 11 9 4 4 3<br><br>16 9 6 6 2 1<br><br><br>|3 3 3 2 1 0<br>4 2 0 0 0 0 8 6 4 2 0 0 4 4 3 1 1 0<br>|4 4 3 3 3 3 6 4 1 1 1 0 4 2 2 1 0 0 1 1 0 0 0 0<br><br>|
|---|---|---|---|
|ODEFormer 18 16 10 4 2 0 SINDy 20 15 12 6 5 3|12 5 1 0 0 0 18 16 12 9 6 3<br><br>|2 1 0 0 0 0 10 8 5 1 0 0<br><br>|1 0 0 0 0 0 1 0 0 0 0 0|


LLM-ODE (Mistral) LLM-ODE (Olmo) LLM-ODE (Qwen) PySR

= 10 1

###### = 10 4

= 10 5

= 10 2

###### = 10 3

= 10 6

12.5

40

DiscoveryRate(%)

| |
|---|


| |
|---|


20

| |
|---|


50

30

| |
|---|


| |
|---|


10.0

20

30

15

20

40

7.5

20

10

10

5.0

10

30

10

5

2.5

0 100 200

0 100 200

0 100 200

0 100 200

0 100 200

0 100 200

Iteration

#### Figure 2: System discovery rate as a function of search iterations across various NMSE thresholds 𝜆. Overall, LLM-ODE methodsachieve higher discovery rates across all iteration limits. LLM-ODE methods enjoy a faster convergence rate than PySR.

14

12

AverageSystemPFSize

10

LLM-ODE (Qwen) LLM-ODE (Olmo) LLM-ODE (Mistral) PySR

8

| |
|---|


| |
|---|


6

| |
|---|


4

2

0

5 50 150 200

Iteration

#### Figure 3: The number of points along the system Pareto frontof GP-based methods during training. The error bars repre-sent 95% confidence intervals. LLM-ODE methods are moreefficient at obtaining a diverse Pareto-front as compared tostochastic GP.

both total discovery rate and convergence speed. Notably, LLMODE variants achieve a significantly higher discovery rate within the first 50 iterations than PySR achieves after 200 iterations in several scenarios (e.g., at 𝜆 = 10−3 and 𝜆 = 10−5). This suggests that leveraging the prior knowledge and reasoning capabilities of LLMs as evolutionary operators provides a more intelligent and

efficient search compared to the uninformed search mechanisms used in classic GP methods.

As the discovery threshold 𝜆 becomes stricter (moving from 10−1 to 10−6), the absolute discovery rate for all methods naturally decreases. However, the performance gap between LLMODE and PySR remains robust. At high tolerance regimes (𝜆 ∈ {10−1, 10−2, 10−3}), LLM-ODE (Qwen) maintains a dominant lead, reaching near-plateau discovery rates much earlier than other models. At low tolerance thresholds (𝜆 ∈ {10−5, 10−6}), LLM-ODE (Mistral) demonstrates remarkable resilience, eventually overtaking other LLM variants and maintaining a clear margin over PySR, which struggles to exceed a 10% discovery rate at 𝜆 = 10−6.

4.4.3 Pareto Front Analysis. From a multi-objective optimization perspective, the number and distribution of points along the Pareto front are widely used as proxies for search quality. A larger, welldistributed Pareto front implies better coverage of the objective space and greater diversity in the underlying population. In genetic programming and evolutionary computation, maintaining a diverse set of non-dominated individuals is known to improve robustness, reduce premature convergence, and increase the probability of discovering globally competitive solutions [2].

Figure 3 compares the evolution of Pareto fronts obtained by LLM-ODE variants and PySR over training iterations for all the systems in the dataset. Each Pareto front captures the trade-off between model complexity and validation error, and thus provides a direct view into the structure and quality of the explored equation search space.

In the initial training steps, the population evolved by LLMs show a substantially richer Pareto front compared to PySR. However, this gap shrinks as the evolution continues, to the point that no significant difference is observed. This observation suggests that intelligent search operations require fewer search iterations to achieve a rich, diverse Pareto front, whereas uninformed GP methods are slower and less efficient in achieving the same level of Pareto front richness.

In this work, to mitigate potential information leakage and prevent LLMs from simply exploiting memorized equations, we deliberately exclude all system-level metadata from the input prompts, including the system description, state variable names, and physical units. Access to such information could allow the LLMs to leverage embedded scientific knowledge and accelerate convergence toward accurate equations in fewer evolution steps. As a direction for future work, the LLM-ODE framework can be applied to genuinely novel scientific systems, where system information is made available to the backend LLM, enabling the discovery of previously unknown models.

The observed Pareto front richness of LLM-ODE therefore suggests a more effective exploration of the equation search space. By leveraging LLM-generated priors to guide symbolic search, LLMODE appears to explore multiple semantically distinct regions of the space simultaneously, rather than relying solely on stochastic variation. This results not only in better best-case solutions, but also in a broader set of viable models that reflect different structural hypotheses.

### References

- [1] Guilherme S Imai Aldeia, Hengzhe Zhang, Geoffrey Bomarito, Miles Cranmer, Alcides Fonseca, Bogdan Burlacu, William G La Cava, and Fabrício Olivetti de França. 2025. Call for Action: towards the next generation of symbolic regression benchmark. arXiv preprint arXiv:2505.03977 (2025).
- [2] Charles Audet, Jean Bigeon, Dominique Cartier, Sébastien Le Digabel, and Ludovic Salomon. 2021. Performance indicators in multiobjective optimization. European journal of operational research 292, 2 (2021), 397–422.
- [3] M. Baer. 2018. findiff Software Package. https://github.com/maroba/findiff https://github.com/maroba/findiff.
- [4] Amirmohammad Ziaei Bideh, Aleksandra Georgievska, and Jonathan Gryak.

2025. MDBench: Benchmarking Data-Driven Methods for Model Discovery. arXiv:2509.20529 [cs.LG] https://arxiv.org/abs/2509.20529

- [5] Luca Biggio, Tommaso Bendinelli, Alexander Neitz, Aurelien Lucchi, and Giambattista Parascandolo. 2021. Neural symbolic regression that scales. In International Conference on Machine Learning. Pmlr, 936–945.
- [6] Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. 2020. Language models are few-shot learners. Advances in neural information processing systems 33 (2020), 1877–1901.
- [7] Charles George Broyden. 1970. The convergence of a class of double-rank minimization algorithms 1. general considerations. IMA Journal of Applied Mathematics 6, 1 (1970), 76–90.
- [8] Steven L Brunton, Joshua L Proctor, and J Nathan Kutz. 2016. Discovering governing equations from data by sparse identification of nonlinear dynamical systems. Proceedings of the national academy of sciences 113, 15 (2016), 3932–3937.
- [9] Bogdan Burlacu, Gabriel Kronberger, and Michael Kommenda. 2020. Operon C++ an efficient genetic programming framework for symbolic regression. In Proceedings of the 2020 Genetic and Evolutionary Computation Conference Companion. 1562–1570.
- [10] Miles Cranmer. 2023. Interpretable machine learning for science with PySR and SymbolicRegression. jl. arXiv preprint arXiv:2305.01582 (2023).
- [11] Stéphane d’Ascoli, Sören Becker, Philippe Schwaller, Alexander Mathis, and Niki Kilbertus. 2024. ODEFormer: Symbolic Regression of Dynamical Systems with Transformers. In The Twelfth International Conference on Learning Representations. https://openreview.net/forum?id=TzoHLiGVMo
- [12] Junlan Dong and Jinghui Zhong. 2025. Recent Advances in Symbolic Regression. Comput. Surveys 57, 11 (2025), 1–37.
- [13] Mengge Du, Yuntian Chen, Zhongzheng Wang, Longfeng Nie, and Dongxiao Zhang. 2024. Large language models for automatic equation discovery of nonlinear dynamics. Physics of Fluids 36, 9 (2024).
- [14] Pierre-Alexandre Kamienny, Stéphane d’Ascoli, Guillaume Lample, and François Charton. 2022. End-to-end symbolic regression with transformers. Advances in Neural Information Processing Systems 35 (2022), 10269–10281.
- [15] John R Koza. 1994. Genetic programming as a means for programming computers by natural selection. Statistics and computing 4 (1994), 87–112.
- [16] Gabriel Kronberger, Fabricio Olivetti de Franca, Harry Desmond, Deaglan J Bartlett, and Lukas Kammerer. 2024. The inefficiency of genetic programming for symbolic regression. In International Conference on Parallel Problem Solving from Nature. Springer, 273–289.
- [17] Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Hao Yu, Joseph Gonzalez, Hao Zhang, and Ion Stoica. 2023. Efficient memory management for large language model serving with pagedattention. In Proceedings of the 29th symposium on operating systems principles. 611–626.
- [18] William La Cava, Bogdan Burlacu, Marco Virgolin, Michael Kommenda, Patryk Orzechowski, Fabrício Olivetti de França, Ying Jin, and Jason H Moore. 2021. Contemporary symbolic regression methods and their relative performance. Advances in neural information processing systems 2021, DB1 (2021), 1.
- [19] Robert Lange, Yingtao Tian, and Yujin Tang. 2024. Large language models as evolution strategies. In Proceedings of the Genetic and Evolutionary Computation Conference Companion. 579–582.


4.4.4 Limitations. The proposed framework relies on an LLM to generate candidate equations during the GP steps. The latency of LLM inference introduces a computational bottleneck, resulting in slower execution compared to non-LLM GP methods. Moreover, running LLMs typically requires specialized hardware that may not be accessible to all users. Quantized and low-rank approximation LLM models offer faster and more lightweight alternatives, broadening the accessibility of the framework at the cost of modest performance degradation.

### 5 Conclusion

This work presents LLM-ODE, a novel framework that integrates large language models with genetic programming for discovering governing equations of dynamical systems from observational data. By replacing traditional stochastic evolutionary operators with LLM-guided suggestions, our approach achieves more intelligent exploration of the equation search space. Empirical evaluation on 91 dynamical systems demonstrates that LLM-ODE consistently outperforms classical genetic programming methods and Transformeronly approaches across multiple dimensions of system complexity.

Our results reveal several key insights. First, LLM-guided search substantially improves both discovery rate and convergence speed, particularly for low-dimensional systems where LLM-ODE variants discover accurate equations within 50 iterations, a milestone that traditional GP methods fail to reach even after 200 iterations.

Second, the LLM-aided GP variants result in more diverse system Pareto front in fewer steps compared to uninformed GP, suggesting that leveraging language model priors enables more effective hypothesis space exploration than uninformed symbolic search.

Third,LLM-ODEdemonstratesbetter scalability to higher-dimensional

systems compared to not only the stochastic GP and Transformerbased methods, but also linear model-based approaches like SINDy, which collapse in four-dimensional settings while LLM-ODE continues to successfully recover multiple systems. The remaining performance gap with ground truth solutions in higher dimensions indicates that scalability remains an open challenge; however, the gains over other model discovery methods across all precision thresholds support LLM-based approaches as a promising direction for robust, scalable model discovery.

- [20] Yujia Li, David Choi, Junyoung Chung, Nate Kushman, Julian Schrittwieser, Rémi Leblond, Tom Eccles, James Keeling, Felix Gimeno, Agustin Dal Lago, et al. 2022. Competition-level code generation with alphacode. Science 378, 6624 (2022), 1092–1097.
- [21] Alexander H. Liu, Kartik Khandelwal, Sandeep Subramanian, Victor Jouault, Abhinav Rastogi, Adrien Sadé, Alan Jeffares, Albert Jiang, Alexandre Cahill, Alexandre Gavaudan, Alexandre Sablayrolles, Amélie Héliou, Amos You, Andy Ehrenberg, Andy Lo, Anton Eliseev, Antonia Calvi, Avinash Sooriyarachchi, Baptiste Bout, Baptiste Rozière, Baudouin De Monicault, Clémence Lanfranchi, Corentin Barreau, Cyprien Courtot, Daniele Grattarola, Darius Dabert, Diego de las Casas, Elliot Chane-Sane, Faruk Ahmed, Gabrielle Berrada, Gaëtan Ecrepont, Gauthier Guinet, Georgii Novikov, Guillaume Kunsch, Guillaume Lample, Guillaume Martin, Gunshi Gupta, Jan Ludziejewski, Jason Rute, Joachim Studnia, Jonas Amar, Joséphine Delas, Josselin Somerville Roberts, Karmesh Yadav, Khyathi Chandu, Kush Jain, Laurence Aitchison, Laurent Fainsin, Léonard Blier, Lingxiao Zhao, Louis Martin, Lucile Saulnier, Luyu Gao, Maarten Buyl, Margaret Jennings, Marie Pellat, Mark Prins, Mathieu Poirée, Mathilde Guillaumin, Matthieu Dinot, Matthieu Futeral, Maxime Darrin, Maximilian Augustin, Mia Chiquier, Michel Schimpf, Nathan Grinsztajn, Neha Gupta, Nikhil Raghuraman, Olivier Bousquet, Olivier Duchenne, Patricia Wang, Patrick von Platen, Paul Jacob, Paul Wambergue, Paula Kurylowicz, Pavankumar Reddy Muddireddy, Philomène Chagniot, Pierre Stock, Pravesh Agrawal, Quentin Torroba, Romain Sauvestre, Roman Soletskyi, Rupert Menneer, Sagar Vaze, Samuel Barry, Sanchit Gandhi, Siddhant Waghjale, Siddharth Gandhi, Soham Ghosh, Srijan Mishra, Sumukh Aithal, Szymon Antoniak, Teven Le Scao, Théo Cachet, Theo Simon Sorg, Thibaut Lavril, Thiziri Nait Saada, Thomas Chabal, Thomas Foubert, Thomas Robert, Thomas Wang, Tim Lawson, Tom Bewley, Tom Bewley, Tom Edwards, Umar Jamil, Umberto Tomasini, Valeriia Nemychnikova, Van Phung, Vincent Maladière, Virgile Richard, Wassim Bouaziz, Wen-Ding Li, William Marshall, Xinghui Li, Xinyu Yang, Yassine El Ouahidi, Yihan Wang, Yunhao Tang, and Zaccharie Ramzi. 2026. Ministral 3. arXiv:2601.08584 [cs.CL] https://arxiv.org/abs/2601.08584
- [22] Matteo Merler, Katsiaryna Haitsiukevich, Nicola Dainese, and Pekka Marttinen.

2024. In-Context Symbolic Regression: Leveraging Large Language Models for Function Discovery. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 4: Student Research Workshop), Xiyan Fu and Eve Fleisig (Eds.). Association for Computational Linguistics, Bangkok, Thailand, 427–444. doi:10.18653/v1/2024.acl-srw.49

- [23] Daniel A Messenger and David M Bortz. 2021. Weak SINDy for partial differential equations. J. Comput. Phys. 443 (2021), 110525.
- [24] Elliot Meyerson, Mark J Nelson, Herbie Bradley, Adam Gaier, Arash Moradi, Amy K Hoover, and Joel Lehman. 2024. Language model crossover: Variation through few-shot prompting. ACM Transactions on Evolutionary Learning 4, 4

(2024), 1–40.

- [25] Suvir Mirchandani, Fei Xia, Pete Florence, Brian Ichter, Danny Driess, Montserrat Gonzalez Arenas, Kanishka Rao, Dorsa Sadigh, and Andy Zeng. 2023. Large Language Models as General Pattern Machines. In Conference on Robot Learning. PMLR, 2498–2518.
- [26] Team Olmo, Allyson Ettinger, Amanda Bertsch, Bailey Kuehl, David Graham, David Heineman, Dirk Groeneveld, Faeze Brahman, Finbarr Timbers, Hamish Ivison, et al. 2025. Olmo 3. arXiv preprint arXiv:2512.13961 (2025).
- [27] Bernardino Romera-Paredes, Mohammadamin Barekatain, Alexander Novikov, Matej Balog, M Pawan Kumar, Emilien Dupont, Francisco JR Ruiz, Jordan S Ellenberg, Pengming Wang, Omar Fawzi, et al. 2024. Mathematical discoveries from program search with large language models. Nature 625, 7995 (2024), 468–475.
- [28] Parshin Shojaee, Kazem Meidani, Amir Barati Farimani, and Chandan Reddy.

2023. Transformer-based planning for symbolic regression. Advances in Neural Information Processing Systems 36 (2023), 45907–45919.

- [29] Parshin Shojaee, Kazem Meidani, Shashank Gupta, Amir Barati Farimani, and Chandan K. Reddy. 2025. LLM-SR: Scientific Equation Discovery via Programming with Large Language Models. In The Thirteenth International Conference on Learning Representations. https://openreview.net/forum?id=m2nmp8P5in
- [30] Parshin Shojaee, Ngoc-Hieu Nguyen, Kazem Meidani, Amir Barati Farimani, Khoa D Doan, and Chandan K Reddy. 2025. Llm-srbench: A new benchmark for scientific equation discovery with large language models. arXiv preprint arXiv:2504.10415 (2025).
- [31] Qwen Team. 2025. Qwen3 Technical Report. arXiv:2505.09388 [cs.CL] https: //arxiv.org/abs/2505.09388
- [32] Iulia Turc, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. 2019. WellRead Students Learn Better: On the Importance of Pre-training Compact Models. arXiv preprint arXiv:1908.08962v2 (2019).
- [33] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz Kaiser, and Illia Polosukhin. 2017. Attention is all you need. Advances in neural information processing systems 30 (2017).
- [34] Pauli Virtanen, Ralf Gommers, Travis E. Oliphant, Matt Haberland, Tyler Reddy, David Cournapeau, Evgeni Burovski, Pearu Peterson, Warren Weckesser, Jonathan Bright, Stéfan J. van der Walt, Matthew Brett, Joshua Wilson, K. Jarrod Millman, Nikolay Mayorov, Andrew R. J. Nelson, Eric Jones, Robert Kern,


- Eric Larson, C J Carey, İlhan Polat, Yu Feng, Eric W. Moore, Jake VanderPlas, Denis Laxalde, Josef Perktold, Robert Cimrman, Ian Henriksen, E. A. Quintero, Charles R. Harris, Anne M. Archibald, Antônio H. Ribeiro, Fabian Pedregosa, Paul van Mulbregt, and SciPy 1.0 Contributors. 2020. SciPy 1.0: Fundamental Algorithms for Scientific Computing in Python. Nature Methods 17 (2020), 261–272. doi:10.1038/s41592-019-0686-2
- [35] Hanchen Wang, Tianfan Fu, Yuanqi Du, Wenhao Gao, Kexin Huang, Ziming Liu, Payal Chandak, Shengchao Liu, Peter Van Katwyk, Andreea Deac, et al. 2023. Scientific discovery in the age of artificial intelligence. Nature 620, 7972 (2023), 47–60.
- [36] Casper Wilstrup and Jaan Kasak. 2021. Symbolic regression outperforms other models for small data sets. arXiv preprint arXiv:2103.15147 (2021).
- [37] Shijie Xia, Yuhan Sun, and Pengfei Liu. 2025. Sr-scientist: Scientific equation discovery with agentic ai. arXiv preprint arXiv:2510.11661 (2025).
- [38] Chengrun Yang, Xuezhi Wang, Yifeng Lu, Hanxiao Liu, Quoc V Le, Denny Zhou, and Xinyun Chen. 2023. Large language models as optimizers. In The Twelfth International Conference on Learning Representations.


### A Hyperparameters

The hyperparamter search space for the baseline method SINDy is provided in Table 2.

Hyperparameter Possible Values

Optimizer threshold 0.05, 0.1, 0.15 Optimizer alpha 0.025, 0.05, 0.075 Max iterations 20, 100 Polynomial degree 1, 2, . . ., 10 Basis functions { polynomials }

{ polynomials, sin, cos, exp} { polynomials, sin, cos, log, exp, sqrt, inverse }

Table 2: Hyperparameter search space of SINDy.

### B ODE Systems

Tables 3, 4, 5, and 6 represent the ground-truth governing equations of the dynamical systems studied in this paper. Figures 4, 5, 6, and 7 visualize the trajectories of the systems, simulated from the training values. For more information about the systems including the references and system descriptions, please refer to the accompanied code supplementary material.

#### Table 3: The governing equations and the initial values of one-dimensional (𝐷 = 1) dynamical systems.

|Name|Train IV<br><br>|Test IV|Equation|
|---|---|---|---|
|RC-circuit|𝑥0 = 10.0<br><br>|𝑥0 = 3.54|𝑥0 = 0.303 − 0.361𝑥0|
|Population growth (naive)|𝑥0 = 4.78<br><br>|𝑥0 = 0.87|𝑥0 = 0.23𝑥0|
|Population growth (carrying capacity)|𝑥0 = 7.3|𝑥0 = 21.0|𝑥0 = 0.79𝑥0 (1 − 0.0135𝑥0)|
|RC-circuit (nonlinear resistor)|𝑥0 = 0.8<br><br>|𝑥0 = 0.02|𝑥0 = −0.5 +<br><br>1 1 1.65𝑒−1.04𝑥0<br><br>|
|Velocity of a falling object<br><br>|𝑥0 = 0.5|𝑥0 = 73.0|+<br><br>𝑥0 = 9.81 − 0.00212𝑥02|
|Autocatalysis|𝑥0 = 0.13|𝑥0 = 2.24<br><br>|𝑥0 = −0.5𝑥02 + 2.1𝑥0|
|Gompertz law (tumor growth)|𝑥0 = 1.73|𝑥0 = 9.5<br><br>|𝑥0 = 0.032𝑥0 log(2.29𝑥0)|
|Logistic equation (Allee effect)|𝑥0 = 6.12<br><br>|𝑥0 = 2.1|𝑥0 = 0.14𝑥0(1 − 0.00769𝑥0)(0.227𝑥0 − 1)|
|Language death model|𝑥0 = 0.14<br><br>|𝑥0 = 0.55|𝑥0 = 0.32 − 0.6𝑥0|
|Refined language death model<br><br>|𝑥0 = 0.83|𝑥0 = 0.34<br><br>|𝑥0 = −0.8𝑥0(1 − 𝑥0)1.2 + 0.2𝑥01.2(1 − 𝑥0)|
|Naive critical slowing down|𝑥0 = 3.4<br><br>|𝑥0 = 1.6|𝑥0 = −𝑥03|
|Photons in a laser<br><br>|𝑥0 = 11.0|𝑥0 = 1.3<br><br>|𝑥0 = −0.111𝑥02 + 1.8𝑥0|
|Overdamped bead|𝑥0 = 3.1<br><br>|𝑥0 = 2.4|𝑥0 = 0.0981 (9.7cos𝑥0 − 1) sin𝑥0|
|Budworm outbreak model<br><br>|𝑥0 = 2.76|𝑥0 = 23.3|𝑥0 = −<br><br>0.9𝑥02 𝑥02 + 449.44 + 0.78𝑥0(1 − 0.0123𝑥0)<br><br>|
|Budworm outbreak (predation)|𝑥0 = 44.3|𝑥0 = 4.5|𝑥0 = −<br><br>𝑥02 𝑥02 + 1 + 0.4𝑥0(1 − 0.0105𝑥0)<br><br>|
|Landau equation<br><br>|𝑥0 = 0.94<br><br>|𝑥0 = 1.65<br><br>|𝑥0 = −0.001𝑥05 + 0.04𝑥03 + 0.1𝑥0|
|Logistic equation (harvesting)<br><br>|𝑥0 = 14.3|𝑥0 = 34.2<br><br>|𝑥0 = 0.4𝑥0(1 − 0.01𝑥0) − 0.3|
|Improved logistic equation (harvesting)|𝑥0 = 21.1<br><br>|𝑥0 = 44.1<br><br>|𝑥0 = 0.4𝑥0(1 − 0.01𝑥0) −<br><br>0.24𝑥0 𝑥0 + 50<br><br>|
|Improved logistic equation (dimensionless)<br><br>|𝑥0 = 0.13|𝑥0 = 0.03|𝑥0 = 𝑥0(1 − 𝑥0) −<br><br>0.08𝑥0 𝑥0 + 0.8<br><br>|
|Autocatalytic gene switching<br><br>|𝑥0 = 0.002<br><br>|𝑥0 = 0.25|𝑥0 =<br><br>𝑥02 𝑥02 + 1 − 0.55𝑥0 + 0.1<br><br>|
|Dimensionally reduced SIR|𝑥0 = 0.0<br><br>|𝑥0 = 0.8<br><br>|𝑥0 = −0.2𝑥0 + 1.2 − 𝑒−𝑥0|
|Protein expression<br><br>|𝑥0 = 3.1|𝑥0 = 6.3<br><br>|𝑥0 =<br><br>0.4𝑥05 𝑥05 + 123 − 0.89𝑥0 + 1.4<br><br>|
|Overdamped pendulum<br><br>|𝑥0 = −2.74|𝑥0 = 1.65<br><br>|𝑥0 = 0.21 − sin𝑥0|


#### Table 4: The governing equations and the initial values of two-dimensional (𝐷 = 2) dynamical systems.

|Name|Train IV<br><br>|Test IV|Equations|
|---|---|---|---|
|Harmonic oscillator<br><br>|𝑥0 = 0.40<br>𝑥1 = −0.03<br>|𝑥0 = 0.0<br>𝑥1 = 0.20<br><br><br>|𝑥0 = 𝑥1<br>𝑥1 = −2.1𝑥0<br>|
|Harmonic oscillator (damping)|𝑥0 = 0.12<br>𝑥1 = 0.043<br><br><br>|𝑥0 = 0.0<br>𝑥1 = −0.30<br><br><br>|𝑥0 = 𝑥1 𝑥1 = −4.5𝑥0 − 0.43𝑥1|
|Lotka–Volterra competition<br><br>|𝑥0 = 5.0<br>𝑥1 = 4.3<br>|𝑥0 = 2.3<br>𝑥1 = 3.6<br>|𝑥0 = 𝑥0(−𝑥0 − 2𝑥1 + 3)<br>𝑥1 = 𝑥1(−𝑥0 − 𝑥1 + 2)<br>|
|Lotka–Volterra simple<br><br>|𝑥0 = 8.3<br>𝑥1 = 3.4<br><br><br>|𝑥0 = 0.40<br>𝑥1 = 0.65<br>|𝑥0 = 𝑥0(1.84 − 1.45𝑥1)<br>𝑥1 = −𝑥1(3.0 − 1.62𝑥0)<br>|
|Pendulum without friction|𝑥0 = −1.9<br>𝑥1 = 0.0<br>|𝑥0 = 0.30<br>𝑥1 = 0.80<br>|𝑥0 = 𝑥1 𝑥1 = −0.9sin(𝑥0)|
|Dipole fixed point<br><br>|𝑥0 = 3.2<br>𝑥1 = 1.4<br><br><br>|𝑥0 = 1.3<br>𝑥1 = 0.20<br>|𝑥0 = 0.65𝑥0𝑥1<br>𝑥1 = −𝑥02 + 𝑥12<br>|
|Catalyzing RNA molecules<br><br>|𝑥0 = 0.30<br>𝑥1 = 0.04<br>|𝑥0 = 0.10<br>𝑥1 = 0.21<br>|𝑥0 = 𝑥0(−1.61𝑥0𝑥1 + 𝑥1)<br>𝑥1 = 𝑥1(−1.61𝑥0𝑥1 + 𝑥0)<br>|
|SIR infection<br><br>|𝑥0 = 7.2<br>𝑥1 = 0.98<br><br><br>|𝑥0 = 20.0<br>𝑥1 = 12.4<br>|𝑥0 = −0.4𝑥0𝑥1 𝑥1 = 0.4𝑥0𝑥1 − 0.314𝑥1|
|Damped double well oscillator<br><br>|𝑥0 = −1.8<br>𝑥1 = −1.8<br>|𝑥0 = 5.8<br>𝑥1 = 0.0<br><br><br>|𝑥0 = 𝑥1 𝑥1 = −𝑥03 + 𝑥0 − 0.18𝑥1|
|Glider|𝑥0 = 5.0<br>𝑥1 = 0.7<br><br><br>|𝑥0 = 9.81<br>𝑥1 = −0.8<br>|𝑥0 = −0.08𝑥02 − sin(𝑥1)<br>𝑥1 = 𝑥0 − cos(𝑥1)/𝑥0<br>|
|Frictionless bead|𝑥0 = 2.1<br>𝑥1 = 0.0<br>|𝑥0 = −1.2<br>𝑥1 = −0.2<br><br><br>|𝑥0 = 𝑥1 𝑥1 = (cos𝑥0 − 0.93) sin𝑥0|
|Rotational dynamics|𝑥0 = 1.13<br>𝑥1 = −0.3<br>|𝑥0 = 2.4<br>𝑥1 = 1.7<br><br><br>|𝑥0 = cos(𝑥0) cot(𝑥1) 𝑥1 = (4.2sin2 𝑥1 + cos2 𝑥1) sin𝑥0|
|Pendulum (nonlinear damping)|𝑥0 = 0.45<br>𝑥1 = 0.9<br><br><br>|𝑥0 = 1.34<br>𝑥1 = −0.8<br>|𝑥0 = 𝑥1 𝑥1 = −0.07𝑥1 cos𝑥0 − 𝑥1 − sin𝑥0|
|Van der Pol oscillator|𝑥0 = 2.2<br>𝑥1 = 0.0<br>|𝑥0 = 0.10<br>𝑥1 = 3.2<br><br><br>|𝑥0 = 𝑥1 𝑥1 = −𝑥0 − 0.43𝑥1(𝑥02 − 1)|
|Van der Pol (simplified)<br><br>|𝑥0 = 0.7<br>𝑥1 = 0.0<br><br><br>|𝑥0 = −1.1<br>𝑥1 = −0.7<br>|𝑥0 = −1.12𝑥03 + 3.37𝑥0 + 3.37𝑥1 𝑥1 = −0.297𝑥0|
|Glycolytic oscillator|𝑥0 = 0.40<br>𝑥1 = 0.31<br><br><br>|𝑥0 = 0.20<br>𝑥1 = −0.7<br><br><br>|𝑥0 = 𝑥02𝑥1 − 𝑥0 + 2.4𝑥1<br>𝑥1 = −𝑥02𝑥1 − 2.4𝑥0 + 0.07<br>|
|Duffing equation<br><br>|𝑥0 = 0.63<br>𝑥1 = −0.03<br>|𝑥0 = 0.20<br>𝑥1 = 0.20<br><br><br>|𝑥0 = 𝑥1 𝑥1 = −𝑥0 + 0.886𝑥1(1 − 𝑥02)|
|Cell cycle model<br><br>|𝑥0 = 0.8<br>𝑥1 = 0.3<br>|𝑥0 = 0.02<br>𝑥1 = 1.2<br><br><br>|𝑥0 = −𝑥0 + 15.3(−𝑥0 + 𝑥1)(𝑥02 + 0.001) 𝑥1 = 0.3 − 𝑥0|
|CDIMA reaction<br><br>|𝑥0 = 0.20<br>𝑥1 = 0.35<br>|𝑥0 = 3.0<br>𝑥1 = 7.8<br><br><br>|𝑥0 = −4𝑥𝑥20𝑥1<br><br>0+1 − 𝑥0 + 8.9<br><br>𝑥1 = 1.4𝑥0 1 − 𝑥𝑥21<br><br><br>0+1|
|Driven pendulum (linear damping)|𝑥0 = 1.47<br>𝑥1 = −0.2<br>|𝑥0 = −1.9<br>𝑥1 = 0.03<br><br><br>|𝑥0 = 𝑥1 𝑥1 = −0.64𝑥1 − sin𝑥0 + 1.67|
|Driven pendulum (quadratic damping)<br><br>|𝑥0 = 1.47<br>𝑥1 = −0.2<br><br><br>|𝑥0 = −1.9<br>𝑥1 = 0.03<br>|𝑥0 = 𝑥1 𝑥1 = −0.64𝑥1|𝑥1| − sin𝑥0 + 1.67|
|Gray–Scott model|𝑥0 = 1.4<br>𝑥1 = 0.2<br>|𝑥0 = 0.32<br>𝑥1 = 0.64<br><br><br>|𝑥0 = −𝑥0𝑥12 − 0.5𝑥0 + 0.5 𝑥1 = 𝑥0𝑥12 − 0.02𝑥1|
|Interacting bar magnets<br><br>|𝑥0 = 0.54<br>𝑥1 = −0.1<br><br><br>|𝑥0 = 0.43<br>𝑥1 = 1.21<br>|𝑥0 = −sin𝑥0 + 0.33sin(𝑥0 − 𝑥1)<br>𝑥1 = −sin𝑥1 − 0.33sin(𝑥0 − 𝑥1)<br>|
|Binocular rivalry model<br><br>|𝑥0 = 0.65<br>𝑥1 = 0.59<br><br><br>|𝑥0 = 3.2<br>𝑥1 = 10.3<br>|𝑥0 = −𝑥0 + 0.247𝑒41.89𝑥1+1<br><br>𝑥1 = −𝑥1 + 0.247𝑒41.89𝑥0 1<br><br><br>|
|Bacterial respiration model|𝑥0 = 0.1<br>𝑥1 = 30.4<br><br><br>|𝑥0 = 13.2<br>𝑥1 = 5.21<br>|+<br><br>𝑥0 = −0.48𝑥0𝑥𝑥21<br><br>0+1 − 𝑥0 + 18.3<br><br>𝑥1 = −0.48𝑥0𝑥𝑥21<br><br><br>0+1 + 11.23|
|Brusselator<br><br>|𝑥0 = 0.7<br>𝑥1 = −1.4<br>|𝑥0 = 2.1<br>𝑥1 = 1.3<br><br><br>|𝑥0 = 3.1𝑥02𝑥1 − 4.03𝑥0 + 1<br>𝑥1 = −3.1𝑥02𝑥1 + 3.03𝑥0<br>|
|Schnackenberg model<br><br>|𝑥0 = 0.14<br>𝑥1 = 0.6<br><br><br>|𝑥0 = 1.5<br>𝑥1 = 0.9<br>|𝑥0 = 𝑥02𝑥1 − 𝑥0 + 0.24<br>𝑥1 = −𝑥02𝑥1 + 1.43<br>|
|Oscillator death model<br><br>|𝑥0 = 2.2<br>𝑥1 = 0.67<br><br><br>|𝑥0 = 0.03<br>𝑥1 = −0.12<br>|𝑥0 = sin𝑥1 cos𝑥0 + 1.432<br>𝑥1 = sin𝑥1 cos𝑥0 + 0.972<br>|


#### Table 5: The governing equations and the initial values of three-dimensional (𝐷 = 3) dynamical systems.

|Name<br><br>|Train IV|Test IV<br><br>|Equations|
|---|---|---|---|
|Maxwell-Bloch equations|[1.3, 1.1, 0.89]<br><br>|[0.89, 1.3, 1.1]|𝑥0 = −0.1𝑥0 + 0.1𝑥1<br>𝑥1 = 0.21𝑥0𝑥2 − 0.21𝑥1<br><br><br>𝑥2 = −1.054𝑥0𝑥1 − 0.34𝑥2 + 1.394|
|Apoptosis model<br><br>|[0.005, 0.26, 2.15]<br><br>|[0.248, 0.097, 0.003]|𝑥0 = −0.4𝑥0𝑥1/(𝑥0 + 0.1) − 0.05𝑥0 + 0.1<br><br>𝑥1 = −7.95𝑥0𝑥1/(𝑥1 + 2.0) − 0.2𝑥1/(𝑥1 + 0.1) + 0.6𝑥2(𝑥1 + 0.1)<br>𝑥2 = 7.95𝑥0𝑥1/(𝑥1 + 2.0) + 0.2𝑥1/(𝑥1 + 0.1) − 0.6𝑥2(𝑥1 + 0.1)<br>|
|Lorenz equations periodic<br><br>|[2.3, 8.1, 12.4]<br><br>|[10.0, 20.0, 30.0]<br><br>|𝑥0 = −5.1𝑥0 + 5.1𝑥1<br>𝑥1 = −𝑥0𝑥2 + 12.0𝑥0 − 𝑥1 𝑥2 = 𝑥0𝑥1 − 1.67𝑥2<br>|
|Lorenz equations complex periodic|[2.3, 8.1, 12.4]<br><br>|[10.0, 20.0, 30.0]|𝑥0 = −10.0𝑥0 + 10.0𝑥1<br>𝑥1 = −𝑥0𝑥2 + 99.96𝑥0 − 𝑥1 𝑥2 = 𝑥0𝑥1 − 2.67𝑥2<br>|
|Lorenz equations chaotic<br><br>|[2.3, 8.1, 12.4]|[10.0, 20.0, 30.0]<br><br>|𝑥0 = −10.0𝑥0 + 10.0𝑥1<br>𝑥1 = −𝑥0𝑥2 + 28.0𝑥0 − 𝑥1 𝑥2 = 𝑥0𝑥1 − 2.67𝑥2<br>|
|Rössler fixed point<br><br>|[2.3, 1.1, 0.8]|[−0.1, 4.1, −2.1]<br><br>|𝑥0 = −5.0𝑥1 − 5.0𝑥2<br>𝑥1 = 5.0𝑥0 − 1.0𝑥1<br><br><br>𝑥2 = 5.0𝑥2(𝑥0 − 5.7) + 1.0|
|Rössler attractor periodic|[2.3, 1.1, 0.8]|[−0.1, 4.1, −2.1]<br><br>|𝑥0 = −5.0𝑥1 − 5.0𝑥2<br>𝑥1 = 5.0𝑥0 + 0.5𝑥1<br><br><br>𝑥2 = 5.0𝑥2(𝑥0 − 5.7) + 1.0|
|Rössler attractor chaotic|[2.3, 1.1, 0.8]|[−0.1, 4.1, −2.1]<br><br>|𝑥0 = −5.0𝑥1 − 5.0𝑥2<br>𝑥1 = 5.0𝑥0 + 1.0𝑥1<br><br><br>𝑥2 = 5.0𝑥2(𝑥0 − 5.7) + 1.0|
|Aizawa attractor<br><br>|[0.1, 0.05, 0.05]|[−0.3, 0.2, 0.1]|𝑥0 = 𝑥0(𝑥2 − 0.7) − 3.5𝑥1<br>𝑥1 = 3.5𝑥0 + 𝑥1(𝑥2 − 0.7)<br><br><br>𝑥2 = 0.1𝑥03𝑥2 − 0.33𝑥23 + 0.95𝑥2 − (𝑥02 + 𝑥12)(0.25𝑥2 + 1) + 0.65|
|Chen-Lee attractor<br><br>|[15, −15, −15]<br><br>|[8, 14, −10]|𝑥0 = 5.0𝑥0 − 𝑥1𝑥2<br>𝑥1 = 𝑥0𝑥2 − 10.0𝑥1<br>𝑥2 = 0.33𝑥0𝑥1 − 3.8𝑥2<br>|
|Gissinger chaotic reversals|[3, 0.5, 1.5]|[1.0, 1.0, 0]<br><br>|𝑥0 = 0.119𝑥0 − 𝑥1𝑥2<br>𝑥1 = 𝑥0𝑥2 − 0.1𝑥1<br>𝑥2 = 𝑥0𝑥1 − 𝑥2 + 0.9<br>|
|Nonlinear oscillator with 3 states|[−0.56, 0.05, 0.38]|[−0.1, 0.4, 1]<br><br>|𝑥0 = 3𝑥0𝑥2 + 0.4𝑥0 − 20.25𝑥1 + 1.6𝑥2(𝑥02 + 𝑥12) 𝑥1 = 20.25𝑥0 + 3𝑥1𝑥2 + 0.4𝑥1<br><br>𝑥2 = −0.44𝑥02 − 0.44𝑥12 − 0.4𝑥23 − 𝑥22 + 1.7|
|Sprott chaotic system<br><br>|[−8.68, −2.47, 0.07]|[−2.1, 2, 0]<br><br>|𝑥0 = −1.4𝑥0 − 𝑥12 − 4𝑥1 − 4𝑥2<br>𝑥1 = −4𝑥0 − 1.4𝑥1 − 𝑥22 − 4𝑥2<br>𝑥2 = −𝑥02 − 4𝑥0 − 4𝑥1 − 1.4𝑥2<br>|
|Hindmarsh-Rose model<br><br>|[−1, 0, 0]|[−0.5, 0.2, −1]|𝑥0 = −𝑥03 + 3𝑥02 + 𝑥1 − 𝑥2 + 2 𝑥1 = −5𝑥02 − 𝑥1 + 1 𝑥2 = 0.4𝑥0 − 0.1𝑥2 + 0.64|
|Lorenz-84 system<br><br>|[0.1, 0.1, 0.1]<br><br>|[−0.1, 0.2, 0.4]|𝑥0 = −0.25𝑥0 − 𝑥12 − 𝑥22 + 1.7115<br>𝑥1 = 𝑥0𝑥1 − 4.0𝑥0𝑥2 − 𝑥1 + 1.287 𝑥2 = 4.0𝑥0𝑥1 + 𝑥0𝑥2 − 𝑥2<br>|
|Diffusionless Lorenz system|[5, 2.1, 0.1]<br><br>|[−2, −1.2, 0.4]|𝑥0 = −𝑥0 + 𝑥1<br>𝑥1 = −𝑥0𝑥2<br>𝑥2 = 𝑥0𝑥1 − 4.7<br>|
|Sprott multifractal system|[0.1, 0.1, 0.1]<br><br>|[−1.1, 0.2, −4]|𝑥0 = 𝑥1<br><br>𝑥1 = −𝑥0 − 𝑥1 sgn(𝑥2)<br>𝑥2 = 𝑥12 − exp(−𝑥02)<br>|
|Nosé-Hoover system<br><br>|[0.0, 0.1, 0.0]|[1.0, −1.0, 0.0]|𝑥0 = 𝑥1<br><br>𝑥1 = −𝑥0 + 𝑥1𝑥2<br>𝑥2 = 1 − 𝑥12<br>|
|Rikitake’s dynamo<br><br>|[1.0, 0.0, 0.6]<br><br>|[−1.0, 0.0, −0.6]|𝑥0 = −1.0𝑥0 + 𝑥1𝑥2 𝑥1 = 𝑥0(𝑥2 − 1.0) − 1.0𝑥1 𝑥2 = −𝑥0𝑥1 + 1|
|Li system<br><br>|[−2.9, 3.89, 3.07]<br><br>|[1.3, −4.34, 9]|𝑥0 = 1.0𝑥0 + 𝑥1𝑥2 + 𝑥1<br>𝑥1 = −𝑥0𝑥2 + 𝑥1𝑥2<br><br><br>𝑥2 = −1.0𝑥0𝑥1 − 𝑥2 + 1.0|
|Sprott dissipativeconservative system<br><br>|[1.0, 0.0, 0.0]|[2.0, 0.0, 0.0]|𝑥0 = 2.0𝑥0𝑥1 + 𝑥0𝑥2 + 𝑥1<br>𝑥1 = −2𝑥02 + 1.0𝑥1𝑥2 + 1<br>𝑥2 = −𝑥02 + 1.0𝑥0 − 𝑥12<br>|
|Chua chaotic circuit|[0.7, 0.1, −0.2]<br><br>|[3.23, 0.1, −7.2]<br><br>|𝑥0 = −11.14𝑥0 + 15.6𝑥1 + 3.34(|𝑥0 − 1| − |𝑥0 + 1|) 𝑥1 = 𝑥0 − 𝑥1 + 𝑥2, 𝑥2 = −25.58𝑥1|


#### Table 6: The governing equations and the initial values of four-dimensional (𝐷 = 4) dynamical systems.

|Name|Train IV<br><br>|Test IV<br><br>|Equations|
|---|---|---|---|
|Binocular rivalry adaptation|[2.25, −0.5, −1.13, 0.4]<br><br>|0.34, −0.43, −0.86, 0.04]<br><br>|𝑥0 = −𝑥0 + (0.247𝑒0.4𝑥1+0.89𝑥2 + 1)−1,𝑥1 = 𝑥0 − 𝑥1 𝑥2 = −𝑥2 + (0.247𝑒0.89𝑥0+0.4𝑥3 + 1)−1,𝑥3 = 𝑥2 − 𝑥3|
|SEIR infection<br><br>|[0.6, 0.3, 0.09, 0.01]|[0.4, 0.3, 0.25, 0.05]<br><br>|𝑥0 = −0.28𝑥0𝑥2, 𝑥1 = 0.28𝑥0𝑥2 − 0.47𝑥1 𝑥2 = 0.47𝑥1 − 0.3𝑥2, 𝑥3 = 0.3𝑥2|
|Hénon-Heiles<br><br>|[0, −0.25, 0.42, 0]<br><br>|[0.3, −0.2, 0.28, 0.01]|𝑥0 = 𝑥2, 𝑥1 = 𝑥3 𝑥2 = −2𝑥0𝑥1 − 𝑥0, 𝑥3 = −𝑥02 + 𝑥12 − 𝑥1|
|Hyperchaotic Lu system (Bo-Cheng & Zhong)<br><br>|[5, 8, 12, 21]|[9, 8, 5.8, 11]<br><br>|𝑥0 = −36𝑥0 + 36𝑥1 + 𝑥3, 𝑥1 = −𝑥0𝑥2 + 20.5𝑥1 𝑥2 = 𝑥0𝑥1 − 3𝑥2, 𝑥3 = 21𝑥0 − 0.1𝑥1𝑥2|
|Cai-Huang hyperchaotic finance system|[1, 8, 20, 10]<br><br>|[2, 5, 15, 17]|𝑥0 = −27.5𝑥0 + 27.5𝑥1, 𝑥2 = 𝑥12 − 2.9𝑥2<br>𝑥1 = −𝑥0𝑥2 + 3𝑥0 + 19.3𝑥1 + 𝑥3, 𝑥3 = −3.3𝑥0<br>|
|Hyperchaotic Lorenz system (Hussain-Gondal-Hussain)<br><br>|[0.1, 0.1, 0.1, 0.1]|[−10, −6, 0, 10]<br><br>|𝑥0 = −10𝑥0 + 10𝑥1 + 𝑥3, 𝑥1 = 𝑥0(28 − 𝑥2) − 𝑥1 𝑥2 = 𝑥0𝑥1 − 2.67𝑥2, 𝑥3 = −𝑥0𝑥2 + 1.3𝑥3|
|Hyperchaotic Lorenz system (Wang-Wang)<br><br>|[−10, −6, 0, 10]|[4, 0.2, 0, −1]<br><br>|𝑥0 = −10𝑥0 + 10𝑥1 + 𝑥3, 𝑥1 = 𝑥0(28 − 𝑥2) − 𝑥1 𝑥2 = 𝑥0𝑥1 − 2.67𝑥2, 𝑥3 = −𝑥1𝑥2 − 𝑥3|
|Hyperchaotic Lu system (Chen-Lu-Lü-Yu)<br><br>|[5, 8, 12, 21]<br><br>|[0.2, −0.2, 0.2, 0.1]|𝑥0 = −36𝑥0 + 36𝑥1 + 𝑥3, 𝑥1 = −𝑥0𝑥2 + 20𝑥1 𝑥2 = 𝑥0𝑥1 − 3𝑥2, 𝑥3 = 𝑥0𝑥2 + 1.3𝑥3|
|Hyperchaotic Pang system<br><br>|[1, 1, 10, 1]|[0.2, −0.2, −0.2, −0.1]|𝑥0 = −36𝑥0 + 36𝑥1, 𝑥1 = −𝑥0𝑥2 + 20𝑥1 + 𝑥3 𝑥2 = 𝑥0𝑥1 − 3𝑥2, 𝑥3 = −2𝑥0 − 2𝑥1|
|Hyperchaotic Qi system<br><br>|[1, 1.5, 2, 2.2]|[0.1, −3.1, 0.2, −0.1]<br><br>|𝑥0 = −5𝑥0 + 𝑥1𝑥2 + 5𝑥1, 𝑥1 = −𝑥0𝑥2 + 2.4𝑥0 + 2.4𝑥1 𝑥2 = 𝑥0𝑥1 − 1.3𝑥2 − 3.3𝑥3, 𝑥3 = 𝑥0𝑥1 + 3𝑥2 − 0.8𝑥3|
|Hyperchaotic Rössler system|[−10, −6, 0, 10]<br><br>|[−0.2, −6, 0, 11]|𝑥0 = −𝑥1 − 𝑥2, 𝑥1 = 𝑥0 + 0.25𝑥1 + 𝑥3 𝑥2 = 𝑥0𝑥2 + 3, 𝑥3 = −0.5𝑥2 + 0.05𝑥3|
|Hyperchaotic Wang system<br><br>|[5, 1, 30, 1]<br><br>|[1, 1, 1, 1]|𝑥0 = −10𝑥0 + 10𝑥1, 𝑥1 = −𝑥0𝑥2 + 40𝑥0 + 𝑥3 𝑥2 = 4𝑥02 − 2.5𝑥2, 𝑥3 = −10.6𝑥0|
|Hyperchaotic Xu system|[2, −1, −2, −10]|[−1, 1, 1, −1]<br><br>|𝑥0 = −10𝑥0 + 10𝑥1 + 𝑥3, 𝑥1 = 16𝑥0𝑥2 + 40𝑥0 𝑥2 = −𝑥0𝑥1 − 2.5𝑥2, 𝑥3 = 𝑥0𝑥2 − 2𝑥1|
|Swinging Atwood’s machine|[0.11, 1.57, 0.11, 0.18]|[0.6, 2.9, −0.1, 0.1]<br><br>|𝑥0 = 0.33𝑥1, 𝑥1 = 9.81cos(𝑥2) − 19.61 + 𝑥32/𝑥03 𝑥2 = 𝑥3/𝑥02, 𝑥3 = −9.81𝑥0 sin(𝑥2)|
|Polymer DA cross-linking and rDA de-cross-linking<br><br>|[30, 0, 0, 10]|[0.01, 0.08, 0.03, 0.03]<br><br>|𝑥0 = −0.03𝑥0𝑥1 − 0.01𝑥0𝑥3 + 0.08𝑥1 + 0.03𝑥2<br>𝑥1 = −0.03𝑥0𝑥1 + 0.01𝑥0𝑥3 − 0.08𝑥1 + 0.03𝑥2<br>𝑥2 = 0.03𝑥0𝑥1 − 0.03𝑥2, 𝑥3 = −0.01𝑥0𝑥3 + 0.08𝑥1<br>|
|Double Pendulum<br><br>|[0.5, 0.5, 0, 0]|[0.1, 0.2, 0, 0]<br><br>|𝑥0 = 𝑥2, 𝑥1 = 𝑥3, Δ = 𝑥0 − 𝑥1<br><br>𝑥2 = 2(−0.55𝑥<br><br>2 2 sin Δ cos Δ−2.09𝑥2<br><br>3 sin Δ−22.56sin𝑥0+10.79sin𝑥1 cos Δ) 2.3−1.1cos2 Δ<br><br>𝑥3 = 0.53(1.15𝑥<br><br><br>2 2 sin Δ+2.09𝑥2<br><br>3 sin Δ cos Δ+22.56sin𝑥0 cos Δ−22.56sin𝑥1) 2.3 1.1cos2 Δ<br><br>|
|Enzyme kinetics (Michaelis-Menten)<br><br>|[1.3, 1.2, 0.1, 0.05]|[0.1, 0.2, 0.3, 0.4]<br><br>|− 𝑥0 = −0.1𝑥0𝑥1 + 0.52𝑥2, 𝑥1 = −0.1𝑥0𝑥1 + 0.02𝑥2 𝑥2 = 0.1𝑥0𝑥1 − 0.52𝑥2, 𝑥3 = 0.5𝑥2|
|Two-mass spring system with damping and force|[−1, −2, −0.5, −0.5]|[−0.1, 0.3, 0.3, −0.4]<br><br>|𝑥0 = 𝑥1, 𝑥2 = 𝑥3 𝑥1 = −0.09𝑥0 − 0.13𝑥1 + 0.09𝑥2 + 0.13𝑥3 𝑥3 = 0.11𝑥0 + 0.16𝑥1 − 0.11𝑥2 − 0.16𝑥3 + 0.2|


3.5

10

60

- 0
- 1
- 2
- 3
- 4


3.0

40

50

60

8

40

2.5

30

6

40

30

2.0

20

4

20

1.5

20

10

10

2

1.0

0

3.5

0.8

- 11
- 12
- 13
- 14
- 15
- 16


0.5

2.8

3.0

80

2.6

0.6

2.5

0.4

60

2.4

2.0

0.4

0.3

1.5

2.2

40

1.0

2.0

0.2

20

0.2

0.5

1.8

0.0

80

90

3.0

x

- 1
- 2
- 3
- 4
- 5
- 6


80

80

80

60

2.5

60

70

60

40

40

60

2.0

40

20

50

20

1.5

20

0

1.0

| |
|---|


3.00

0.0

0.3

- 0
- 1
- 2
- 3
- 4


0.8

0.8

2.75

0.5

0.2

0.6

2.50

1.0

0.6

2.25

1.5

0.4

0.4

0.1

2.00

2.0

0.2

1.75

0.2

2.5

0.0

0.0

0 5 10

0 5 10

0 5 10

0 5 10

0 5 10

0 5 10

t

#### Figure 4: The training trajectories of dynamical systems with 𝐷 = 1 state variables.

- 0
- 1
- 2


0.6

- 0
- 1
- 2
- 3
- 4
- 5


- 0
- 1
- 2
- 3


8

0.4

0.1

0.2

6

0.0

0.0

4

0.2

0.1

1

1

2

0.4

0.2

2

0

0.6

2

20

- 0
- 1
- 2


- 0
- 1
- 2


- 0
- 1


0.5

6

15

0.4

4

0.3

10

1

0.2

2

1

1

5

2

0.1

2

2

3

0

0

1.2

- 0
- 1
- 2


0.4

- 0
- 1
- 2


- 0
- 1
- 2


0.75

1.0

0.50

0.2

0.8

0.25

0.6

0.0

x

1

0.00

0.4

1

1

0.25

0.2

2

0.2

2

2

15.0

20

8

0.6

12.5

- 0
- 1
- 2
- 3


0.4

15

6

10.0

0.5

7.5

0.2

10

4

5.0

0.4

5

2

0.0

2.5

0.3

0.0

0

0

1.0

1.0

| |
|---|


15.0

1.5

- 0
- 1
- 2
- 3


40

0.8

0.8

12.5

1.0

30

0.6

0.6

0.5

10.0

0.0

7.5

20

0.4

0.4

0.5

5.0

10

0.2

0.2

1.0

2.5

0

1.5

0.0

0.0

0.0

0 5 10

0 5 10

0 5 10

0 5 10

0 5 10

0 5 10

t

#### Figure 5: The training trajectories of dynamical systems with 𝐷 = 2 state variables.

150

14

40

- 0
- 1
- 2


2.0

1.2

12

30

100

1.5

1.0

20

10

50

10

8

1.0

0.8

0

6

0

0.5

0.6

1

10

4

50

20

0.0

2

0.4

4

- 0
- 1
- 2


- 0
- 1
- 2
- 3


20

5

2

20

10

0

0

0

0

1

2

5

20

1

2

10

4

4

4

2

- 0
- 1
- 2


7.5

5

x

0

5.0

2

2

0

2.5

2

0

0

5

0.0

4

2

2.5

2

6

10

1

5.0

4

8

1.0

1.0

10.0

0.75

| |
|---|


- 0
- 1
- 2
- 3


7.5

0.50

1.0

0.8

0.8

5.0

0.25

0.6

0.6

0.5

2.5

0.00

0.4

0.4

0.0

0.0

0.25

2.5

0.2

0.2

0.50

0.5

5.0

0.75

0.0

0.0

0 5 10

0 5 10

0 5 10

0 5 10

0 5 10

0 5 10

t

#### Figure 6: The training trajectories of dynamical systems with 𝐷 = 3 state variables.

40

80

0.6

- 0
- 1
- 2


150

0.4

30

0.5

60

100

0.2

20

0.4

40

50

0.0

10

0.3

20

0

0.2

0.2

0

50

0

0.1

0.4

10

100

20

1

0.0

0.6

100

100

100

10

30

80

40

50

50

20

60

0

20

0

10

40

0

50

0

20

0

10

x

100

50

10

0

150

20

20

20

20

100

200

0

- 0
- 1
- 2
- 3


30

| |
|---|


1.2

5

25

2

0

1.0

0

20

4

0.8

5

5

15

0.6

6

10

10

1

0.4

10

8

5

0.2

2

15

0

0.0

10

0 5 10

0 5 10

0 5 10

0 5 10

0 5 10

0 5 10

t

#### Figure 7: The training trajectories of dynamical systems with 𝐷 = 4 state variables.

