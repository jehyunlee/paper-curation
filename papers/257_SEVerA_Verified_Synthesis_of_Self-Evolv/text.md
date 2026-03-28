# arXiv:2603.25111v1[cs.LG]26 Mar 2026

## SEVerA: Verified Synthesis of Self-Evolving Agents

DEBANGSHU BANERJEE∗, CHANGMING XU∗, and GAGANDEEP SINGH, University of Illinois Urbana-Champaign, USA

Recent advances have demonstrated the effectiveness of self-evolving LLM agents on tasks such as program repair and scientific discovery. In this paradigm, a planner LLM synthesizes an agent program that invokes parametric models, including probabilistic generative models such as LLMs, smaller neural networks, and external tools such as SMT solvers. These components are then tuned per task to improve performance. However, unlike traditional constraint-guided program synthesis, existing self-evolving agent frameworks provide no formal guarantees of safety or correctness. Because such synthesized programs are often executed autonomously on unseen inputs, the lack of formal guarantees raises serious reliability and security concerns. To address this gap, we formulate agentic code generation as a constrained learning problem that combines hard formal specifications with soft objectives capturing task utility. We introduce Formally Guarded Generative Models (FGGM), which allow the planner LLM to specify a formal output contract for each generative-model call using first-order logic. Each FGGM call automatically wraps the underlying parametric generative model in a rejection sampler with a verified fallback, treating model outputs as samples from a proposal distribution. As a result, every returned output satisfies the specified contract for any input and any parameter setting of the underlying model. Building on FGGM, we present SEVerA (Self-Evolving Verified Agents), a three-stage framework for solving constrained learning problems arising from agent synthesis. In Search, the planner LLM synthesizes candidate parametric programs that may contain multiple FGGM calls. In Verification, we prove correctness with respect to the hard constraints for all parameter values, reducing the problem to unconstrained learning. In Learning, we apply scalable gradient-based optimization, including GRPO-style fine-tuning for LLMs, to improve the soft objective while preserving formal correctness. We evaluate SEVerA on constrained symbolic regression, invariant generation for Dafny programs, symbolic mathematical expression synthesis, and policy-compliant agentic tool use (𝜏2-bench). Across all tasks, SEVerA achieves zero constraint violations while simultaneously improving task performance over unconstrained and state-of-the-art baselines. Our results demonstrate that formal behavioral constraints not only guarantee correctness but also prune the space of candidate programs, steering synthesis toward higher-quality agents.

CCS Concepts: • LLM Agents → Automated Verification. Additional Key Words and Phrases: LLM Agents, Automated Verification, Deductive Program Synthesis. ACM Reference Format: Debangshu Banerjee, Changming Xu, and Gagandeep Singh. 2026. SEVerA: Verified Synthesis of Self-Evolving Agents. 1, 1 (March 2026), 42 pages. https://doi.org/10.1145/nnnnnnn.nnnnnnn

#### 1 Introduction

Recent works have leveraged the code-generation capabilities of large language models (LLMs) to automatically synthesize LLM-based agents, expressed as programs, from natural language task

∗These authors contributed equally to this work.

Authors’ Contact Information: Debangshu Banerjee, db21@illinois.edu; Changming Xu, cx23@illinois.edu; Gagandeep Singh, ggnds@illinois.edu, University of Illinois Urbana-Champaign, USA.

Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than the author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org.

© 2026 Copyright held by the owner/author(s). Publication rights licensed to ACM. ACM XXXX-XXXX/2026/3-ART https://doi.org/10.1145/nnnnnnn.nnnnnnn

descriptions [13, 19, 47, 49, 53]. Given a user-defined task, a planner LLM generates a program that invokes parametric models, including LLMs, smaller neural networks, and external tools such as SMT solvers, and executes this program on user inputs to compute outputs. While this paradigm is powerful, it introduces serious safety and reliability concerns: the synthesized programs are executed autonomously on unseen inputs. Modern self-evolving frameworks [11, 43, 48, 51] further complicate formal safety verification as they fine-tune the parameters of models embedded in the synthesized programs to improve task-specific performance. Consequently, any correctness guarantee provided on an agentic program must continue to hold after parameter updates. The absence of formal safety verification leads to failures across diverse domains. In program verification, agents cheat by subtly modifying the input program (e.g., altering variable initializations) so that the modified program with proposed annotations passes verification, inflating task accuracy [3]. In code repair, agents delete failing tests rather than fixing the underlying bugs [50]. In agentic tool use, unconstrained agents violate domain-specific policies, such as refund eligibility and booking-modification rules, on 65-76% of interactions [20]. In deployment, rogue agents have been observed bypassing security protections in the wild [14, 15, 25]. These are not isolated incidents; they are a consequence of evaluating synthesized agents solely on soft performance metrics without formal behavioral specifications. Natural-language task descriptions and testing on fixed inputs is not sufficient to completely prevent such failures. Agentic programs need formal hard constraints to ensure safety. In this paper, we aim to achieve both the formal guarantees of constraint-guided synthesis [1] and the flexibility and performance benefits of self-evolving agentic frameworks. Key Challenges: We summarize the challenges below.

- • Balancing Safety and Performance: A safe agent synthesis algorithm must ensure formal correctness guarantees while simultaneously improving task-specific performance. Existing work on deductive program synthesis [1, 22, 38] provides formal guarantees but typically does not optimize task-specific performance objectives. Meanwhile, popular gradient-based optimization methods for LLMs, such as GRPO [36], empirically improve output quality but provide no assurance that post-training outputs satisfy specified constraints.
- • Enforcing Constraints per Model Call: Generative models (GMs), such as LLMs, may be used in an agentic program at different places with different constraints. For example, one call may require generating Python programs, while another may require producing symbolic mathematical expressions conforming to a specific formal grammar. Thus, we require a mechanism to specify formal output constraints for each GM call in an agentic program and a way to use these specifications to verify that an agentic program satisfies the user-provided behavioral specification. Recent work on constrained decoding [4, 35, 45] can enforce context-free grammar–based syntactic constraints and limited semantic constraints such as variable naming or simple type checks. However, these approaches are restricted in the types of constraints they support and require modifying the model’s decoding procedure, which limits their applicability to open-source models. Moreover, constrained decoding strategies are known to distort the output distribution, producing outputs that satisfy constraints but degrade task performance [4, 35].


Our Contributions: We summarize our contributions below.

- • We introduce the novel concept of Formally Guarded Generative Models (FGGM), which allow us to define and enforce local contracts on model calls through formal input-output specifications expressed in first-order logic. FGGM operates solely on LLM output strings and can be applied to both open and closed source models. Using FGGM, we retain the formal guarantees of deductive synthesis while utilizing the performance gained through gradient-based parameter optimization.
- • We introduce SEVerA: the first self-evolving agent synthesis algorithm with verifiable guarantees. The approach consists of three stages: (a) Search, where a planner LLM samples program strings in


- a verifier-aware language such as Dafny, and use the proposed FGGMs to establish local contracts on the embedded model calls; (b) Verify, where the language’s built-in verifier is used to prove that the sampled programs satisfy all specified contracts over all parameters of the embedded parametric model calls; and (c) Learn, where verified parametric programs reduce the constrained learning problem to an unconstrained optimization problem over model parameters, enabling scalable gradient-based training without sacrificing correctness.
- • We prove that SEVerA is sound: any agent returned satisfies the behavioral specification for all inputs and all parameter values (Theorem 5.4). We also establish a sufficient condition under which a verified agent exists that satisfies the hard constraints while incurring no greater task loss than any unconstrained generative model with initial parameters, with strict improvement whenever the unconstrained model violates the specification (Theorem 5.5).
- • We evaluate SEVerA on tasks spanning LLM-assisted program verification, symbolic math synthesis, agentic tool use, and constrained symbolic regression. Across all benchmarks, SEVerA achieves provably zero constraint violations while outperforming state-of-the-art agents in task performance: 97.0% verification rate on HumanEvalDafny (vs. 86.9% for the best baseline), 66.0% accuracy on GSM-Symbolic (vs. 44.7% for the best constrained-decoding method), and 52.6% pass rate 𝜏2-bench’s airline domain using Qwen3-8B. Notably, on 𝜏2-bench airline SEVerA even beats Agent-C [20] with Claude Sonnet 4.5, a state-of-the-art constrained agent using a frontier model. These results demonstrate that behavioral constraints do not merely enforce safety but actively prune the search space of candidate programs and steer synthesis toward higher-quality agents. The code is available on github.


#### 2 Background

Notations and Terminology: We use Σ to denote the alphabet, a finite set of characters. All LLMs output finite strings over Σ. We use lowercase letters (𝑥) to denote constants, bold letters (𝑥) to denote strings, capital letters (𝑋) to denote sets (including sets of functions), and |𝑥| to denote string length. In the rest of the paper, we treat neural networks as a restricted form of generative model that produces a single output for a fixed input.

LLMs: LLMs L : Σ∗ → Σ∗ are probabilistic string generators that, given a prompt 𝑝 ∈ Σ∗ over the alphabet Σ, sample an output string 𝑦 ∈ Σ∗. Typically, the output length |𝑦| is bounded by a fixed user-specified 𝑛, i.e., |𝑦| ≤ 𝑛 or equivalently 𝑦 ∈ Σ≤𝑛. Fixed-length generation L𝑛 : Σ∗ → Σ≤𝑛 is implemented by iteratively composing two high-level steps, repeated at most 𝑛 times. Each iteration samples a single character (sometimes referred to as a token) from Σ or the special end-ofsequence symbol ⟨𝑒𝑜𝑠⟩ ∉ Σ that marks termination of generation. The first step is the distribution prediction step, defined as L𝑝 : Σ∗ → P(Σ ∪ ⟨𝑒𝑜𝑠⟩), which maps a prefix string 𝑥 ∈ Σ∗ to a probability distribution over Σ ∪ ⟨𝑒𝑜𝑠⟩. This distribution captures how likely each character is to appear next. The second step is the decoding step, defined as D : Σ∗ × P(Σ ∪ ⟨𝑒𝑜𝑠⟩) → Σ ∪ ⟨𝑒𝑜𝑠⟩, which draws the next character using the current prefix 𝑥 and the predicted distribution. If the decoding step produces ⟨𝑒𝑜𝑠⟩, the generation terminates. Otherwise, the sampled character 𝑐 is appended to the prefix, and generation continues. Henceforth, we drop the subscript𝑛 for simplicity.

Definition 2.1 (LLMs). For a fixed 𝑛 ∈ N, an LLM is a bounded string generator L𝑛 : Σ∗ → Σ≤𝑛 that samples an output string 𝑦 ∈ Σ≤𝑛 for input 𝑥. 𝑦 on 𝑥 is computed recursively as 𝑦0 = 𝑥, and 𝑦𝑖 = 𝑦𝑖−1 · 𝑐𝑖 if (∀𝑗 ≤ 𝑖.𝑐𝑗 ≠ ⟨𝑒𝑜𝑠⟩) else 𝑦𝑖−1 where 𝑖 ∈ [𝑛], 𝑐𝑖 = D(𝑦𝑖−1, L𝑝(𝑦𝑖−1)) and 𝑥 · 𝑦 = 𝑦𝑛.

Rejection Sampling: Rejection sampling is a popular Monte Carlo method for generating samples from a target distribution 𝜋𝑡 when direct sampling from 𝜋𝑡 is difficult. Instead, it relies on a proposal distribution 𝜋𝑝 from which sampling is easy. The support set 𝑆(𝜋𝑝) (see Definition 2.2) must cover 𝑆(𝜋𝑡), i.e., 𝑆(𝜋𝑡) ⊆ 𝑆(𝜋𝑝). Intuitively, 𝜋𝑝 generates candidate samples, and the rejection sampler

decides whether to accept each candidate, rejecting those that are unlikely under 𝜋𝑡 (details in Appendix B). The rejection sampler guarantees that no accepted sample lies outside 𝑆(𝜋𝑡).

Definition 2.2. Let 𝜋 be a probability distribution over Ω with density function 𝐷𝜋 : Ω → R+. The support set 𝑆(𝜋) of 𝜋 captures all points with positive probability 𝑆(𝜋) = {𝑥 ∈ Ω; |𝐷𝜋 (𝑥) > 0}.

Self-evolving LLM agents: In this work, we focus on LLM agents modeled as programs 𝑓 : 𝑇𝑖 → 𝑇𝑜 that, given any user input 𝑥 ∈ 𝑇𝑖, compute the output 𝑦 = 𝑓 (𝑥). Typically, 𝑓 is written in a popular imperative language such as Python. The program invokes one or more parametric models (formally defined in § 5.1), such as LLMs, as well as other tools such as an SMT solver, to compute the output𝑦. All parametric models F𝑝 and tool calls F𝑐 are provided as a collection of pre-implemented library functions. We denote this library by F = F𝑝 ∪ F𝑐 (formal definition in § 5.1). In the self-evolving paradigm, the program 𝑓 is not handwritten. Instead, it is generated by a planner LLM based on task-specific instructions provided as a prompt. The goal is to synthesize a program 𝑓 that, given a training dataset of input and optional ground-truth output pairs D ⊆ 𝑇𝑖 ×𝑇𝑜 and a loss function L : 𝑇𝑖 × 𝑇𝑜 × 𝑇𝑜 → R+, minimizes the aggregated loss |D1| (𝑥𝑖,𝑦𝑖)∈D L(𝑥𝑖,𝑦𝑖, 𝑓 (𝑥𝑖)). For certain tasks, the ground truth 𝑦𝑖 may not be available; in such cases, the loss is denoted as L(𝑥𝑖, _, 𝑓 (𝑥𝑖)). Assume that a context-free grammar (CFG) 𝐺 defines the set of syntactically valid programs 𝑓 as 𝐿(𝐺) ⊆ Σ∗. Given the library functions F, let S(𝐺, F) denote the search space for 𝑓 : 𝑇𝑖 → 𝑇𝑜 with type signature (𝑇𝑖 → 𝑇𝑜), including all parametric values of the models in F𝑝. Self-evolving agentic frameworks aim to find the optimal solution 𝑓 ∗ to the following optimization problem.

1

𝑓 ∗ = argmin 𝑓 ∈S(𝐺,F)

|D| × (𝑥𝑖,_)∈D L(𝑥𝑖, _, 𝑓 (𝑥𝑖)) (1)

#### 3 Problem Formulation

High-level formulation of agent synthesis with formal constraints: Eq. 1 searches only for the optimal program 𝑓 ∗ that minimizes the loss on the training set D. However, it provides no guarantee about how 𝑓 ∗ performs on unseen user inputs outside D. In contrast, deductive program synthesis [1, 38] allows program generation to be controlled by formal behavioral input Φ : 𝑇𝑖 → {𝑇, 𝐹} and output specifications Ψ : 𝑇𝑖 × 𝑇𝑜 → {𝑇, 𝐹}. The use of formal behavioral specifications 1 enables proving the correctness of the synthesized program for all inputs that satisfy the input specification, and 2 can guide the search for 𝑓 ∗ by eliminating unverified program candidates. With (Φ, Ψ), the unconstrained learning problem in Eq. 1 can be reformulated as the constrained learning problem shown below.

soft learning objective 1

hard formal constraints

∀𝑥 ∈ 𝑇𝑖. Φ(𝑥) =⇒ Ψ(𝑥, 𝑓 (𝑥)) (2)

|D| × (𝑥𝑖,_)∈D L(𝑥𝑖, _, 𝑓 (𝑥𝑖)) s.t.

𝑓 ∗ = argmin 𝑓 ∈S(𝐺,F)

The central question is whether Eq. 2 can be solved while retaining the performance benefits and scalability of gradient-based methods designed for Eq. 1. Next, we illustrate how practical constraints from several application domains can be encoded as behavioral specifications (Φ, Ψ).

Examples of formal constraints (Φ, Ψ): The output specification Ψ characterizes the agent’s expected behavior on any valid input, not just on examples in D. Hard constraints therefore detect and mitigate errors during synthesis that would not be revealed by performance evaluation on a fixed dataset D. We show encodings of (Φ, Ψ) for four different tasks from distinct domains. a Scientific Discovery: We consider constrained symbolic regression, where the task is to recover an unknown mathematical formula from observed data. The formal constraints (Φ, Ψ) encode prior knowledge about the target formula, such as known symbolic bounds [7, 17, 28] or asymptotic behavior [27]. Any generated formula that violates these hard constraints is invalid, regardless of its empirical fit to the data. Moreover, in the presence of noise, the constraints (Φ, Ψ) help prevent overfitting, which cannot be addressed solely by optimizing a soft objective [24]. b Program Verification: Given a

program in a verification-aware language such as Dafny with a predefined specification, the agent is expected to synthesize annotations (e.g., loop invariants, assertions, ranking functions) [29, 31, 39]. Task success depends on whether the annotated program verifies. Recent work [3] shows that agents using frontier models (e.g., Claude) may cheat by subtly modifying the input program, such as altering variable initializations, instead of producing correct annotations. [3] reports that such modifications were not detected by prior string-based checkers, leading to inflated task accuracy. In contrast, formal AST-based diff checkers that syntactically enforce equivalence between the input program and the annotated output serve as hard constraints, ensuring the agent cannot cheat even on unseen inputs. c Constrained LLM Generation: Constrained generation captures a class of problems in which LLMs are required to generate strings that follow a formal structure. Typically, these formal structures are defined using formal grammars (regular [40] or context-free grammars [35, 45]), or static analyzers such as type checkers [32, 33]. In our setting, these formal structures define the output specification Ψ. We consider the task of generating symbolic math expressions from natural language questions, where hard constraints ensure that the synthesized agent always produces at least a structurally valid expression. d Agentic Tool Use: Conversational LLM agents deployed in customer-service settings must select and invoke API tools to resolve user requests while respecting domain-specific policies, such as refund eligibility, booking-modification rules, and authentication-before-access requirements [5]. These temporal and logical policy constraints can be expressed as formal specifications that govern the ordering and content of agent actions. Agent-C [20] provides a domain-specific language for specifying such temporal properties and translates them into linear temporal logic (LTL), enabling SMT-based checking of the generated tool calls. Crucially, the hard constraint is enforced at each individual tool call: given the current tool-call trace, the Agent-C checker verifies whether the next proposed tool call complies with the defined formal policy before it is executed. Task performance (utility), in contrast, is measured over the entire multi-turn interaction trace as whether the agent successfully resolves the user request. In our formulation, Ψ uses the Agent-C checker to define a hard constraint applied to each tool call, ensuring that synthesized agents never violate domain policies at any step, regardless of user input. Overall, hard behavioral constraints capture the minimal requirements that synthesized agents must satisfy on all inputs, thereby enabling the pruning of untrusted candidates during synthesis.

#### 4 Overview

Fig. 1 gives a high-level overview of SEVerA for solving the constrained learning problem in Eq. 2 over the search space S(𝐺, F). In this setting, we need to simultaneously optimize task-specific performance while guaranteeing that the resulting program provably satisfies the given behavioral constraints. This is difficult because the search space contains both discrete program structure and continuous model parameters, and because although GMs such as LLMs are powerful, they are inherently unreliable, which makes it hard to ensure conformance with behavioral specifications. To address these challenges, SEVerA retains the best of both worlds: constraint-guided program search from deductive synthesis and unconstrained gradient-based parameter optimization. Specifically, SEVerA employs a CEGIS-style loop in which a planner LLM proposes candidate parametric programs and a verifier checks their correctness with respect to the behavioral specification. Once a parametric program is verified, SEVerA applies unconstrained gradient-based optimization to tune the underlying GM parameters and reduce the task-specific loss L. The proposed Formally Guarded Generative Model (FGGM) serves as the critical link between these two strategies. The FGGM setup allows one to bind each GM call to explicit local input–output contracts and a verified non-parametric fallback program, ensuring that these contracts hold regardless of the underlying GM parameters. The verifier then leverages these local contracts to prove the correctness of the parametric program with respect to the behavioral specification. Beyond providing correctness

![image 1](Banerjee et al._2026_SEVerA Verified Synthesis of Self-Evolving Agents_images/imageFile1.png)

Fig. 1. Overview of SEVerA, which operates in three key steps. (1) Search: Given the task information, library functions F𝑐, a list of parametric generative models (GMs) F𝑝, and specifications (Φ, Ψ), the planner LLM outputs a parametric agentic program in which all formal output specifications of GM calls are defined using the FGGM setup. (2) Verify: Given the parametric agentic code, this step first verifies all FGGM definitions proposed by the planner. Once verified, it uses their local contracts to check the program against (Φ, Ψ). If all checks pass, the program is accepted and the unconstrained learning step is invoked on the verified program; otherwise, an error message is returned to the planner. (3) Learn: This step optimizes the parameters of the underlying GMs within each FGGM to improve conformance with local contracts defined in step (1), while also reducing the task-loss L over the dataset D. After tuning, SEVerA maintains a pool of verified fine-tuned agents and uses their execution traces on D to generate new candidates via step (1). All agents in the pool are valid candidate solutions, and the one with the lowest L on D is returned. Central to SEVerA is the Formally Guarded Generative Model (FGGM), which binds each GM call to local input–output contracts (Φ𝑙, Ψ𝑙) and a verified non-parametric fallback, ensuring that the contracts hold irrespective of the underlying GM parameters. This enables unconstrained gradient-based parameter optimization without compromising formal correctness.

guarantees, these contracts also extract local learning objectives by characterizing the expected outputs of each GM call. This enables gradient-based optimization to improve the GM’s conformance to its local contracts, thereby connecting constrained program search with unconstrained learning. Next, we discuss the components of SEVerA through two representative and easy-to-understand problem instances from different domains: scientific discovery and program verification.

#### 4.1 Example Instantiation of SEVerA

- 4.1.1 Constrained Symbolic Regression: In symbolic regression, each problem instance consists of possibly noisy observations of input–output pairs generated by an unknown ground-truth function


𝑓𝑔𝑡. The goal is to recover this ground-truth function from the training data D, a popular task in scientific discovery and neuro-symbolic program synthesis [10, 37]. In constrained symbolic regression [7, 17], users encode known properties of 𝑓𝑔𝑡 beyond what is captured in D as formal constraints, ensuring that the recovered function 𝑓 satisfies these constraints. This setup directly follows the constrained learning formulation in Eq. 2, where the synthesized agent 𝑓 ∗ corresponds to the recovered function. For illustration, we consider the problem instance with ground-truth

function 𝑓𝑔𝑡 (𝑥) = √︁1.23 × max(𝑥, 0.0), taken from [28]. The dataset D contains input–output pairs (𝑥,𝑦) ∈ R2, where 𝑦 = 𝑓𝑔𝑡 (𝑥) + 𝜖 is a noisy observation of 𝑓𝑔𝑡 (𝑥) and 𝜖 ∼ N(0,𝜎) denotes additive Gaussian noise. The pointwise loss function L is the commonly used Normalized Mean Squared Error (NMSE) (see Eq. 3). For this instance, the agent’s type signature 𝜏 is (R → R), and the behavioral specifications (Φ, Ψ) define known symbolic bounds on 𝑓𝑔𝑡 (see Eq. 4) where 𝑠𝑞𝑟𝑡 : R → R is a provided library function.

L(𝑥𝑖,𝑦𝑖, 𝑓 (𝑥𝑖)) = (𝑓 (𝑥𝑖𝐶)−𝑦𝑖)2 where 𝐶 = (𝑥𝑖,𝑦𝑖)∈D𝑦𝑖2 (3) Φ(𝑥) : (𝑥 ≥ 0), Ψ(𝑥, 𝑓 (𝑥)) : ((𝑥 ≤ 1) =⇒ (𝑓 (𝑥) ≥ 𝑝𝑜𝑤(𝑥, 0.8)) ∧ ((𝑥 ≥ 1) =⇒ (𝑓 (𝑥) ≥ 𝑠𝑞𝑟𝑡((𝑥))) (4)

Search Space: SEVerA defines the search space using a restricted subset of Dafny supporting four basic types {𝑖𝑛𝑡,𝑏𝑜𝑜𝑙,𝑟𝑒𝑎𝑙,𝑠𝑡𝑟}, conditional blocks, while loops, and function calls. We formalize the search space in § 5.1.

Library Functions: For this task, the library function set F includes common transcendental functions (e.g., 𝑠𝑖𝑛, 𝑐𝑜𝑠, 𝑝𝑜𝑤, 𝑠𝑞𝑟𝑡) as well as small parametric neural networks (NNs), enabling the search space to capture a wide range of neuro-symbolic programs. Users provide type signatures and formal contracts for all non-parametric library functions; the planner LLM defines formal contracts for each parametric model call through the FGGM setup (§ 4.2). We present representative type signatures and specifications in Eq. 5, with the complete set in Appendix C.

𝑠𝑞𝑟𝑡(𝑥 : 𝑟𝑒𝑎𝑙) → 𝑟𝑒𝑎𝑙, Φ𝑠𝑞𝑟𝑡 (𝑥) : (𝑥 ≥ 0), Ψ𝑠𝑞𝑟𝑡 (𝑥,𝑠𝑞𝑟𝑡(𝑥)) : (𝑠𝑞𝑟𝑡(𝑥) ≥ 0); 𝑁𝑁𝜃(1)(𝑥1 : 𝑟𝑒𝑎𝑙) → 𝑟𝑒𝑎𝑙 (5) ∀𝑥,𝑑1,𝑑2 ∈ R.(𝑥 ≥ 1) ∧ (𝑑1 ≥ 𝑑2) =⇒ 𝑝𝑜𝑤(𝑥,𝑑1) ≥ 𝑝𝑜𝑤(𝑥,𝑑2) (6) ∀𝑥,𝑑1,𝑑2 ∈ R.(𝑥 ≤ 1) ∧ (𝑑1 ≥ 𝑑2) =⇒ 𝑝𝑜𝑤(𝑥,𝑑1) ≤ 𝑝𝑜𝑤(𝑥,𝑑2) (7)

𝜑A =⇒ ∀𝑥 ∈ 𝑇𝑖. Φ(𝑥) =⇒ Ψ(𝑥, 𝑓 (𝑥)) where 𝜑A = ( 𝜑∈A 𝜑) (8)

Axioms: The axioms A encode known properties of library functions in F, including their formal contracts as universally quantified first-order sentences, where library functions are treated as uninterpreted. For example, Eq. 7 captures a property of 𝑝𝑜𝑤. These axioms assist automated verification as shown in Eq. 8. We provide the formal syntax for defining A in § 5.1 and the complete axiom set for this task in Appendix D. Like other synthesis frameworks with library functions [12], SEVerA assumes that all library functions have correct input–output specifications, and that they are pure and terminating. Verifying the correctness of the library functions and axioms is outside the scope of SEVerA.

- 4.1.2 LLM-Assisted Automated Verification. This task aims to synthesize annotations, such as inductive loop invariants, ranking functions, and assertions, that enable automatic verification and termination checking of input Dafny programs with pre-encoded input–output specifications [29, 39]. The agent has type signature (𝑝 : 𝑠𝑡𝑟) → 𝑠𝑡𝑟, mapping an input Dafny program with pre-encoded specifications, represented as a string, to an annotated Dafny program. The point-wise loss function L evaluates whether the annotated program verifies within a pre-fixed time budget, assigning1to unverified programs and0to verified ones (Eq. 10). Hard constraints (Φ, Ψ) ensure that, for any parsable input program, the output remains parsable and does not change the input program beyond adding annotations (Eq. 11). We use the Dafny built-in verifier to define L, and the Dafny parser together with the AST-based formal diff checker from [3] to define (Φ, Ψ). 𝑛𝑜𝐷𝑖𝑓 𝑓 returns True if the second input program is syntactically equivalent to the first (ignoring annotations), and False otherwise. The library function set F includes all these components. Although parsing and diff checks could be incorporated into L by penalizing invalid outputs on D, these constraints must hold for all possible inputs, not only those in D. Therefore, any candidate agent that fails to satisfy them must be filtered out.


Library Functions: We use the same search space as constrained symbolic regression. F includes the verifier with a pre-fixed time budget 𝑣𝑒𝑟𝑖𝑓𝑦, the Dafny parser 𝑝𝑎𝑟𝑠𝑒, the diff-checker 𝑛𝑜𝐷𝑖𝑓 𝑓 . We show the type signature and formal contract of representative functions in Eq. 9 while providing the rest in Appendix E.

𝑛𝑜𝐷𝑖𝑓 𝑓 (𝑥 : 𝑠𝑡𝑟,𝑦𝑦 : 𝑠𝑡𝑟) → 𝑏𝑜𝑜𝑙, Φ(𝑥𝑥,𝑦𝑦) : 𝑝𝑎𝑟𝑠𝑒(𝑥), Ψ(𝑥𝑥,𝑦𝑦𝑦,𝑛𝑜𝐷𝑖𝑓 𝑓 (𝑥𝑥,𝑦𝑦)) : 𝑇 (9) L(𝑥𝑥, _,𝑦𝑦) = 1 − I(𝑝𝑎𝑟𝑠𝑒(𝑦) ∧ 𝑛𝑜𝐷𝑖𝑓 𝑓 (𝑥𝑥,𝑦𝑦) ∧ 𝑣𝑒𝑟𝑖𝑓𝑦(𝑦)) (10) Φ(𝑥) : 𝑝𝑎𝑟𝑠𝑒(𝑥); Ψ(𝑥𝑥, 𝑓 (𝑥)) : 𝑝𝑎𝑟𝑠𝑒(𝑓 (𝑥)) ∧ 𝑛𝑜𝐷𝑖𝑓 𝑓 (𝑥𝑥, 𝑓 (𝑥)) (11)

Axioms: Example of a first-order sentence encoding known properties of𝑛𝑜𝐷𝑖𝑓 𝑓 in Eq. 12.𝑛𝑜𝐷𝑖𝑓 𝑓 is both reflexive and transitive w.r.t all parsable Dafny programs. It is easy to see that same program will always have no difference with itself. We list all the axioms in Appendix F.

Reflexivity: ∀𝑥 ∈ Σ∗. 𝑝𝑎𝑟𝑠𝑒(𝑥) =⇒ 𝑛𝑜𝐷𝑖𝑓 𝑓 (𝑥𝑥,𝑥𝑥) (12)

- 4.2 Formally Guarded Generative Model Formally Guarded Generative Model (FGGM) setup allows the planner LLM to bind each generative


model (GM) call to local input–output contracts (Φ𝑙, Ψ𝑙) that formally characterize the output. Once the FGGM is verified to be well-formed, the defined contracts can be used to prove the correctness of the agentic program against the behavioral specifications (Φ, Ψ). Our FGGM design ensures the following essential properties. 1 Flexibility: Unlike functions in F𝑐, output contracts cannot be predefined by users because the expected output of a GM varies across calls depending on the prompt. In our design, the planner LLM synthesizes custom first-order formulas over terms involving non-parametric functions (e.g., sqrt) and predicates (e.g., 𝑛𝑜𝐷𝑖𝑓 𝑓 ) from F𝑐 to specify local contracts. 2 Parameter-Independent Correctness: Provided the defined FGGM is well-formed, the specified contracts hold irrespective of the parameters of the underlying GM. This property is crucial to ensure that gradient-based parameter optimization never breaks the correctness guarantees. 3

Local Learning Objective: Although correctness holds irrespective of parameter values, the local contracts (Φ𝑙, Ψ𝑙) extract the local learning objective for a particular GM call by characterizing its expected output. This objective can guide gradient-based optimization so that, after tuning, the GM’s conformance with (Φ𝑙, Ψ𝑙) improves (§ 4.2.3).

- 4.2.1 Intuition. For each FGGM with local contracts (Φ𝑙, Ψ𝑙) and underlying parametric GM LΘ, the planner LLM synthesizes two non-parametric programs using only functions from F𝑐. The first is a fallback program 𝑓𝑑 that satisfies (Φ𝑙, Ψ𝑙) and guards against edge cases in which the GM hallucinates or produces outputs that violate the specification. Without a verified fallback, the rejection sampler could exhaust all samples; the fallback is what makes the contract hold


unconditionally for all parameter values. Intuitively, although 𝑓𝑑 may lack the GM’s task-solving capability (low task performance), it prevents the candidate agent from entering unsafe program

states during execution (high constraint satisfaction). The second is a prompting program 𝑓𝑝, which constructs the input to the GM (which may be just a neural network). For LLMs, 𝑓𝑝 encodes task-specific natural-language instructions, analogous to prompt-tuning techniques [6, 21] known to improve GM performance and instruction adherence. Once the planner LLM proposes Φ𝑙, Ψ𝑙, 𝑓𝑝, and 𝑓𝑑, SEVerA automatically constructs a rejection sampler that treats outputs of underlying GM as samples from a proposal distribution 𝜋𝑝 for an input 𝑝. The local specifications (Φ𝑙, Ψ𝑙) define the support set (Definition 2.2) of the target distribution 𝜋𝑡 on 𝑝, assigning zero probability to outputs that violate (Φ𝑙, Ψ𝑙). The rejection sampler draws a fixed number 𝐾 ≥ 1 of samples from LΘ, as specified by the user, and falls back to 𝑓𝑑 if all samples are rejected (Fig 2). The purpose of 𝑓𝑝 and optional conformance tuning is to improve the acceptance rate of the rejection sampler

for any input, thereby reducing reliance on the fallback 𝑓𝑑. We formally define the FGGM syntax, well-formedness conditions, and the computability of the output checker in § 5.2.1.

- 4.2.2 Examples. We show a couple of example FGGM definitions that the planner LLM suggests: one from symbolic regression and one from Dafny program verification. The first example from symbolic regression (Eq. 13) with id 𝑏𝑜𝑢𝑛𝑑𝑒𝑑𝑃𝑎𝑟𝑎𝑚, type signature (𝑙 : 𝑟𝑒𝑎𝑙,𝑢 : 𝑟𝑒𝑎𝑙) → 𝑟𝑒𝑎𝑙, underlying parametric GM which is a neural network 𝑁𝑁Θ(2) : R2 → R for this case, Φ𝑙 : (𝑙 ≤ 𝑢) Ψ𝑙

- (Eq. 13) restricts 𝑏𝑜𝑢𝑛𝑑𝑒𝑑𝑃𝑎𝑟𝑎𝑚(𝑙,𝑢) to lie within [𝑙,𝑢]. The fallback clamps any violating sample 𝑦 using library functions 𝑚𝑖𝑛 and 𝑚𝑎𝑥, ensuring contract preservation. The second example from Dafny program verification
- (Eq. 14) with id 𝑑𝑎𝑓𝑛𝑦𝐴𝑛𝑛𝑜𝑡𝑎𝑡𝑒, type signature (𝑝 : 𝑠𝑡𝑟) → 𝑠𝑡𝑟, underlying parametric GM which is a LLM


LΘ : Σ∗ → Σ∗, Φ𝑙 : 𝑝𝑎𝑟𝑠𝑒(𝑝), Ψ𝑙 (Eq. 14) ensures 𝑑𝑎𝑓𝑛𝑦𝐴𝑛𝑛𝑜𝑡𝑎𝑡𝑒(𝑝) always outputs a syntactically valid program and only adds annotations to the input program

𝑝. If all samples are rejected, the fallback safely returns the original program 𝑝, guaranteeing Ψ𝑙 under Φ𝑙 utilizing the reflexivity axiom (Eq 12). These examples show how a planner LLM can define FGGMs with fallbacks to avoid incorrect program states for diverse tasks.

Ψ𝑙 : (𝑙 ≤ 𝑓 (𝑙,𝑢)) ∧ (𝑓 (𝑙,𝑢) ≤ 𝑢), 𝑓𝑑 : function 𝑓𝑑(l:real, u:real, y:real) {return 𝑚𝑖𝑛(𝑚𝑎𝑥(𝑙,𝑦),𝑢);} (13) Ψ𝑙 : 𝑝𝑎𝑟𝑠𝑒(𝑝) ∧ 𝑛𝑜𝐷𝑖𝑓 𝑓 (𝑝, 𝑓 (𝑝)), 𝑓𝑑 : function 𝑓𝑑(p:str, y:str) : (𝑠𝑡𝑟) {return 𝑝;} (14)

Design Considerations. Alternative approaches for enforcing formal constraints on generative model calls exist, but they fall short of FGGM. Constrained decoding [4, 33, 35, 45] modifies the model’s internal decoding procedure, which limits its applicability to open-source models and restricts constraints to syntactic forms such as context-free grammars. Post-hoc output filtering without a fallback provides no guarantees: if all sampled outputs are rejected, the program produces no valid output. Fully verifying an agentic program is computationally intractable, as it depends on large parametric components such as LLMs. FGGM addresses all three limitations: it operates solely on model outputs, making it compatible with closed-source models; it incorporates a verified fallback that guarantees a valid output on every execution; and it decomposes verification into parameter-independent local contracts. Moreover, these local contracts can be utilized during learning to guide parameter tuning, improving conformance, and reducing reliance on the fallback.

- 4.2.3 Conformance Tuning. A FGGM that always uses the fallback is formally correct but practically no better than a non-parametric program 𝑓𝑑, conformance tuning helps avoid this by teaching the GM to satisfy the defined contract directly. The local contracts (Φ𝑙, Ψ𝑙) define the local learning objective to avoid the fallback and assign higher probability to outputs that pass the check 𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙. The objective in Eq. 20 minimizes the expected contract violation of GM samples over


function 𝑖𝑑(𝑥1 : 𝑇1, . . .,𝑥𝑛 : 𝑇𝑛) : (𝑇𝑜) requires Φ𝑙 (𝑥1, . . .,𝑥𝑛) { var 𝑝 : 𝑇𝑖𝑛 := 𝑓𝑝(𝑥1, . . .,𝑥𝑛),𝑦 : 𝑇𝑜;



for 𝑖 = 1 . . .𝐾 { 𝑦 := LΘ(𝑝); if 𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 (𝑥1, . . .,𝑥𝑛,𝑦)

1

return 𝑦; }

 

return 𝑓𝑑(𝑥1, . . .,𝑥𝑛,𝑦); 2 }

Fig. 2. Auto-synthesized guarded GM with rejection sampler (1) and fallback (2).

an input set P. For any 𝜃 ∈ Θ, the inner term L𝜃Φ

𝑙,Ψ𝑙 (𝑝) measures the probability that a sampled output from L𝜃 (𝑝) violates 𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 (Φ𝑙, Ψ𝑙,𝑥1, . . .,𝑥𝑛,𝑦), while LΦ𝑙,Ψ𝑙 (𝜃) aggregates this violation across inputs in P. By optimizing 𝜃 ∈ Θ to reduce this loss, the GM post-tuning is encouraged

to concentrate the probability mass on the support defined by (Φ𝑙, Ψ𝑙) (details in § 5.2.5). Overall conformance tuning improves the acceptance rate of the rejection sampler, reducing reliance on 𝑓𝑑. We formalize the conformance loss in § 5.2.5 (Eq. 20).

- 4.3 SEVerA SEVerA employs a three-step strategy to solve the constrained learning problem in Eq. 2: (1) Search:


The planner LLM defines FGGMs with their prompting programs 𝑓𝑝, then samples candidate parametric programs that invoke these FGGMs. Direct calls to parametric GMs are disallowed; each must be wrapped within a verified FGGM.

(2) Verify: SEVerA checks all FGGM definitions for well-formedness and then verifies the candidate program against (Φ, Ψ) using the Dafny built-in verifier. If verification fails, error feedback is returned to the planner LLM to refine the candidate (CEGIS-style loop). Due to the FGGM setup, any verified program satisfies the behavioral specifications for all parameter values. (3) Learn: The learning step applies unconstrained gradient-based optimization to tune GM parameters, guided by the global task loss L and local conformance losses from each FGGM. For closed-source LLMs without accessible parameters, the learning step is skipped and improvements rely on prompt tuning through 𝑓𝑝. We formalize the search-verify-learn loop in § 5.2 (Algorithms 1 and 2).

function 𝑎𝑔𝑒𝑛𝑡(𝑥 : 𝑟𝑒𝑎𝑙) : (𝑟𝑒𝑎𝑙) { var 𝑎 : 𝑟𝑒𝑎𝑙 := 𝑏𝑜𝑢𝑛𝑑𝑒𝑑𝑃𝑎𝑟𝑎𝑚(0.0, 1.0); var 𝑏 : 𝑟𝑒𝑎𝑙 := 𝑏𝑜𝑢𝑛𝑑𝑒𝑑𝑃𝑎𝑟𝑎𝑚(0.0, 1.0); var 𝑙𝑖𝑛𝑒𝑎𝑟_𝑥 : 𝑟𝑒𝑎𝑙 := 𝑎 ∗ 𝑥; var 𝑦 : 𝑟𝑒𝑎𝑙 := 𝑙𝑖𝑛𝑒𝑎𝑟_𝑥 + 𝑏; return 𝑦;

###### }

(a) Unverified parametric program pruned out.

function 𝑎𝑔𝑒𝑛𝑡(𝑥 : 𝑟𝑒𝑎𝑙) : (𝑟𝑒𝑎𝑙) { if (𝑥 ≤ 0.0) {return 0.0; } var 𝑎 : 𝑟𝑒𝑎𝑙 := 𝑏𝑜𝑢𝑛𝑑𝑒𝑑𝑃𝑎𝑟𝑎𝑚(1.0, 1.5); var 𝑑 : 𝑟𝑒𝑎𝑙 := 𝑏𝑜𝑢𝑛𝑑𝑒𝑑𝑃𝑎𝑟𝑎𝑚(0.5, 0.8); assert 𝑥 ≥ 0.0; var 𝑝𝑜𝑤_𝑥 : 𝑟𝑒𝑎𝑙 := 𝑝𝑜𝑤(𝑥,𝑑); assert (𝑑 ≤ 0.8); assert (𝑑 ≥ 0.5); assert (𝑥 ≤ 1) =⇒ (𝑝𝑜𝑤_𝑥 ≥ 𝑝𝑜𝑤(𝑥, 0.8)); assert (𝑥 ≥ 1) =⇒ (𝑝𝑜𝑤_𝑥 ≥ 𝑝𝑜𝑤(𝑥, 0.5)); assert (𝑥 ≥ 0) =⇒ (𝑝𝑜𝑤(𝑥, 0.5) = 𝑠𝑞𝑟𝑡(𝑥)); var 𝑦 : 𝑟𝑒𝑎𝑙 := 𝑎 ∗ 𝑝𝑜𝑤_𝑥; return 𝑦;

- 4.3.1 Candidate Pool and Execution Feedback. SEVerA maintains a pool of verified candidate agentic programs with fine-tuned parameters (Fig. 1). SEVerA selects the best-performing candidate agent from the pool, i.e., the one with the minimal task loss L, and uses its execution traces on data D to iteratively search for new candidates via the planner LLM. The number of parametric candidate sampling steps is capped by the user. Once this limit is reached, SEVerA returns the agent in the pool with the lowest task loss L. Fig. 3 shows two candidate parametric programs sampled by the planner LLM. Each program invokes the FGGM defined in Eq. 13 with id 𝑏𝑜𝑢𝑛𝑑𝑒𝑑𝑃𝑎𝑟𝑎𝑚 from two different locations. Fig. 3a shows the first parametric program, which fails to verify against the behavioral specification and is therefore pruned by the verifier. This candidate represents the output as a parametric affine function of the input 𝑥, which does not match the ground truth, illustrating how strict behavioral constraints eliminate poor candidates. The second candidate verifies for


###### }

(b) Verified parametric program.

Fig. 3. Two example candidate parametric programs generated for symbolic regression.

all parameters of the neural networks 𝑁𝑁Θ(2) wrapped inside the 𝑏𝑜𝑢𝑛𝑑𝑒𝑑𝑃𝑎𝑟𝑎𝑚 calls. After parameter tuning, it recovers the ground truth with negligible error, as discussed below. Currently,

SEVerA does not share parameters across FGGM calls at different locations and instead assigns separate parameter sets to each 𝑏𝑜𝑢𝑛𝑑𝑒𝑑𝑃𝑎𝑟𝑎𝑚 call. This design allows the system to potentially learn different parameters at different call sites to improve task-specific performance. Since both 𝑏𝑜𝑢𝑛𝑑𝑒𝑑𝑃𝑎𝑟𝑎𝑚 calls receive constant inputs, after fine-tuning they return constant values, i.e., 𝑎 = 1.11 and 𝑑 = 0.503. This recovers the ground-truth function √︁1.23 × max(𝑥, 0) with negligible error. Note that SEVerA currently neither shares parameters nor caps the number of FGGM calls.

However, SEVerA can be extended to support both these checks to reduce the computational budget required for parameter learning, as discussed in § 6.5. The parametric candidate programs and all FGGM definitions with synthesized prompting programs 𝑓𝑝 for the program verification task are included in Appendix K. In the next section, we formalize the search space, provide complete algorithmic details for each step, and establish theoretical guarantees for the framework.

#### 5 Technical Details

We formalize the search space in § 5.1, provide the details of the steps search, verify, and learn along with FGGM in § 5.2. We provide formal proof of soundness and a sufficient condition for agent synthesis success with non-trivial utility in § 5.3.

#### 5.1 Search Space

Program Search Space: We use a restricted subset of the popular verification-aware language Dafny [26] to define the search space of candidate programs. In this restricted subset, we allow conditional blocks, while loops, assignment statements, assertion statements, function calls, and annotations including invariant clauses and ranking functions (decreases clauses), along with first-order input–output specifications. We present the BNF grammar 𝐺𝐷 capturing this subset in Appendix A. We allow four basic types T = {𝑏𝑜𝑜𝑙,𝑖𝑛𝑡,𝑟𝑒𝑎𝑙,𝑠𝑡𝑟𝑖𝑛𝑔}, basic built-in arithmetic functions B𝑎 = {+, −, ×, /}, boolean functions B𝑏 = {&&, ||, !, =⇒ }, and relations B𝑟 = {==, ≤, ≥, <, >} with their usual semantics. We use a planner LLM L𝑝 : Σ∗ → Σ∗ to search the program space by sampling candidate programs as strings. We assume that L𝑝’s output space can represent all valid Dafny programs 𝐿(𝐺𝐷) ⊆ Σ∗ and that the type 𝑠𝑡𝑟𝑖𝑛𝑔 can represent all strings Σ∗ over Σ. SEVerA provides built-in predicates 𝑙𝑒𝑥𝑇 (𝑥 : 𝑠𝑡𝑟𝑖𝑛𝑔) → 𝑏𝑜𝑜𝑙 to check whether a string can be parsed as a specific type 𝑇 ∈ {𝑏𝑜𝑜𝑙,𝑖𝑛𝑡,𝑟𝑒𝑎𝑙}. Using Dafny as the language allows us to leverage its built-in verifier to check candidate programs against a first-order input–output specification, as well as its built-in termination checker. This choice is motivated by several factors: (1) Dafny’s built-in verification infrastructure directly supports the formal guarantees central to SEVerA, (2) its type system aligns with the basic types T used in our specification language, and (3) it supports annotations such as loop invariants and ranking functions that our planner LLM can synthesize to aid the verifier. While the framework is not language-specific, using a verification-aware host language avoids re-implementing a custom verifier and termination checker.

Library Functions: We categorize the set of library functions F into two disjoint sets: F𝑐, the set of non-parametric functions, and F𝑝, the set of parametric functions. F𝑐 includes all built-in functions. Each user specified non-parametric function of arity 𝑛 is specified by a tuple (𝑖𝑑(𝑓𝑛),𝜏𝑓𝑛, 𝑓𝑛Φ, 𝑓𝑛Ψ), where 𝑖𝑑(𝑓𝑛) is the function name, 𝜏𝑓𝑛 = (𝑇1 × · · · ×𝑇𝑛 → 𝑇0) is the type signature with 𝑇𝑖 ∈ T, and (𝑓𝑛Φ, 𝑓𝑛Ψ) are first-order input–output specifications defining a formal over-approximate semantics of 𝑓𝑛. The function 𝑓𝑛 : 𝑇1 × · · · ×𝑇𝑛 → 𝑇0 halts for any inputs 𝑥1 ∈ 𝑇1, . . .,𝑥𝑛 ∈ 𝑇𝑛 and computes 𝑟 = 𝑓𝑛(𝑥1, . . .,𝑥𝑛). The computed output 𝑟, together with (𝑥1, . . .,𝑥𝑛), always satisfies ∀𝑥1 ∈ 𝑇1, . . .,∀𝑥𝑛 ∈ 𝑇𝑛. 𝑓𝑛Φ(𝑥1, . . .,𝑥𝑛) =⇒ 𝑓𝑛Ψ(𝑥1, . . .,𝑥𝑛,𝑟). A contains all these formal contracts.

Parametric Functions: Each 𝑓𝑛Θ in F𝑝 is specified by the tuple (𝑖𝑑(𝑓𝑛Θ),𝜏𝑓Θ

,𝜃0, Θ), where 𝑖𝑑(𝑓𝑛Θ) denotes the function name, 𝜏𝑓Θ

𝑛

is the type signature, Θ is a continuous set of parameters, and

𝑛

𝜃0 ∈ Θ denotes the default parameters. Here, 𝑓𝑛Θ = {𝑓𝑛𝜃 | 𝜃 ∈ Θ} represents an infinite set of functions with the same type signature 𝜏𝑓Θ

, where each individual function 𝑓𝑛𝜃 ∈ 𝑓𝑛Θ is instantiated by a concrete parameter value 𝜃 ∈ Θ. Although 𝑓𝑛Θ represents a set of functions, we sometimes abuse this notation to denote a single function corresponding to 𝑓𝑛𝜃0 with the default parameters.

𝑛

The input I = (F, A, L, D, Φ, Ψ,𝐼) to SEVerA includes the library functions F, axioms A, point-wise differentiable loss L, dataset D, behavioral specifications (Φ, Ψ), and textual task information 𝐼 used by the planner LLM L𝑝. We use PC : Σ∗ → {𝑇, 𝐹} to denote the parser for checking the syntactic validity of input programs, VC[Φ, Ψ] : Σ∗ → {𝑇, 𝐹} to denote the verifier that checks a program against the specifications (Φ, Ψ), and TC : Σ∗ → {𝑇, 𝐹} to denote the termination checker. Each of PC, VC[Φ, Ψ], and TC is instantiated with user-provided context C = (𝐺𝐷, F, A). Both VC[Φ, Ψ] and TC are restricted to a fixed timeout and return false if they cannot verify (Φ, Ψ) or prove termination within the allotted time budget.

#### 5.2 Key Steps

- 5.2.1 FGGM Formal Definition. Eq. 15 specifies the formal syntax for defining an FGGM.

⟨𝐹𝐺𝐺𝑀⟩ ::= ⟨𝑖𝑑⟩ ";" ⟨𝐺𝑀𝑖𝑑⟩";"

signature + formal contract

⟨𝑡𝑦𝑝𝑒𝑆𝑖𝑔⟩ ";" ⟨Φ𝑙⟩";" ⟨Ψ𝑙⟩ ";" ⟨𝑓𝑝⟩";" prompt

⟨𝑓𝑑⟩";" fallback

⟨𝑖𝑛𝑓𝑜⟩ (15)

The planner LLM defines a guarded GM following Eq. 15, where: (a) id: is the unique identifier of the created FGGM; (b) GMid: identifies the underlying GM used as the proposal distribution; (c) typeSig: defines the type signature of the FGGM, including input variables with their types and the output type, e.g., (𝑥1 : 𝑇1, . . .,𝑥𝑛 : 𝑇𝑛) → 𝑇𝑜; (d) (Φ𝑙, Ψ𝑙): are first-order formulas whose terms can include non-parametric library functions from F𝑐; (e) 𝑓𝑝: is the program that constructs the GM input from the typed input variables and the task description; (f) 𝑓𝑑: is a non-parametric fallback program that satisfies the local specifications (Φ𝑙, Ψ𝑙); and (g) info: is a textual description of the defined FGGM, utilized by the planner LLM during the generation of the parametric program. SEVerA parses these inputs, validates the definition, and automatically synthesizes a rejection

- sampler with fallback, as shown in Fig. 2 where LΘ is the parametric GM specified by GMid. The defined FGGM is then invoked in the candidate program via its identifier 𝑖𝑑. For valid definitions,


SEVerA synthesizes 𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙, which checks whether a concrete input–output pair (𝑥1, . . .,𝑥𝑛,𝑦) satisfies the proposed contract (Φ𝑙, Ψ𝑙), as elaborated in § 5.2.3. We provide the BNF grammar for parsing the FGGM definition in Appendix L. Next, we discuss correctness checks for a proposed FGGM definition. Provided the SEVerA validates definition including the fallback 𝑓𝑑, ∀𝜃 ∈ Θ.∀𝑥1 ∈ 𝑇1 . . .∀𝑥𝑛 ∈ 𝑇𝑛.Φ𝑙(𝑥1, . . .,𝑥𝑛) =⇒ Ψ𝑙(𝑥1, . . .,𝑥𝑛,𝑖𝑑(𝑥1, . . .,𝑥𝑛)) holds ensuring formal contracts are preserved for all parametric values 𝜃 ∈ Θ.

- 5.2.2 FGGM Well-formedness. Given an FGGM definition G = (𝑖𝑑G, 𝑓GΘ,𝜏G, Φ𝑙, Ψ𝑙, 𝑓𝑝, 𝑓𝑑,𝑖𝑛𝑓𝑜) following Eq. 15, this step checks whether the definition is well-formed. Let the parametric GM identified by GMid be LΘ : 𝑇𝑖𝑛 → 𝑇𝑜. SEVerA first checks the well-formedness of the type signature 𝜏G = (𝑇1 × · · · ×𝑇𝑛) → 𝑇𝑜 and the well-formedness of the local contracts (Φ𝑙, Ψ𝑙). We then verify that all terms in Φ𝑙 and subsequently in Ψ𝑙 that involve non-parametric functions from F𝑐 are valid (details in Appendix M). The G definition is considered valid provided both 𝑓𝑝 and 𝑓𝑑 are type-checked and terminating, and the fallback 𝑓𝑑 satisfies the contract VC[Φ𝑙, Ψ𝑙](𝑓𝑑). After the validity check, SEVerA constructs 𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 : (𝑇1 × · · · ×𝑇𝑛 ×𝑇𝑜) → {𝑇, 𝐹} that checks whether a concrete input–output tuple (𝑥1, . . .,𝑥𝑛,𝑦) satisfies the local output contract Ψ𝑙 (see § 5.2.3). We provide the pseudocode of 𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 along with a soundness proof showing 𝜑A =⇒ ∀𝑥1 ∈ 𝑇1, . . .,∀𝑥𝑛 ∈ 𝑇𝑛,∀𝑦 ∈ 𝑇𝑜. Φ𝑙(𝑥1, . . .,𝑥𝑛) =⇒ 𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 (𝑥1, . . .,𝑥𝑛,𝑦) =⇒ Ψ𝑙(𝑥1, . . .,𝑥𝑛,𝑦) in Appendix R. Furthermore, for quantifier-free Ψ𝑙, the checker is complete (Lemma 5.1).


Lemma 5.1 (Completeness of Checker). For any valid FGGM G with quantifier-free Ψ𝑙, ∀𝑥1 ∈ 𝑇1, . . .,∀𝑥𝑛 ∈ 𝑇𝑛,∀𝑦 ∈ 𝑇𝑜. Φ𝑙(𝑥1, . . .,𝑥𝑛) =⇒ 𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 (𝑥1, . . .,𝑥𝑛,𝑦) ⇐⇒ Ψ𝑙(𝑥1, . . .,𝑥𝑛,𝑦) .

Proof Sketch. We prove this by structural induction on the quantifier-free formula Ψ𝑙. Base case: If Ψ𝑙 is an atomic predicate over terms built from computable library functions in F𝑐, then under any concrete substitution (𝑥1, . . .,𝑥𝑛,𝑦), 𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 evaluates the same computable terms and returns the same boolean value as Ψ𝑙. Inductive step: Assume the claim holds for formulas 𝜙 and 𝜓. For compound formulas ¬𝜙, 𝜙 ∧ 𝜓, and 𝜙 ∨ 𝜓, 𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 recursively evaluates the subformulas and applies the corresponding boolean operator, and returns the result. Thus, by induction on the structure of Ψ𝑙, 𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 (𝑥1, . . .,𝑥𝑛,𝑦) returns true iff Ψ𝑙(𝑥1, . . .,𝑥𝑛,𝑦) holds whenever Φ𝑙(𝑥1, . . .,𝑥𝑛) holds. Hence, the checker is complete. Formal details in Appendix R. □

For any valid FGGM G, the rejection sampler 𝑖𝑑G : 𝑇1 × · · · ×𝑇𝑛 → 𝑇𝑜 with fallback synthesized by SEVerA (Fig. 2) satisfies the defined contract (Φ𝑙, Ψ𝑙) for all well-typed inputs (𝑥1, . . .,𝑥𝑛). Crucially the contract preservation holds over all parameters 𝜃 ∈ Θ of the underlying parametric model 𝑓GΘ. The function 𝑖𝑑G terminates on all inputs since the number of samples 𝐾 is finite and 𝑓𝑝, 𝑓𝑑, and 𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 are all terminating. We provide a soundness proof sketch in Theorem 5.2.

Theorem 5.2 (Valid Local contract). For any valid FGGM G with (Φ𝑙, Ψ𝑙) and parametric GM 𝑓GΘ, 𝜑A =⇒ ∀𝜃 ∈ Θ,∀𝑥1 ∈ 𝑇1, . . .,∀𝑥𝑛 ∈ 𝑇𝑛. Φ𝑙(𝑥1, . . .,𝑥𝑛) =⇒ Ψ𝑙(𝑥1, . . .,𝑥𝑛,𝑖𝑑G(𝑥1, . . .,𝑥𝑛)) .

Proof Sketch. Let𝑟 = 𝑖𝑑G(𝑥1, . . .,𝑥𝑛). Based ontherejectionsamplerwith the checker𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙,

the following condition always holds for the output 𝑟 (Eq. 16). Eq. 17 follows from the validity of the fallback 𝑓𝑑, and Eq. 18 follows from the soundness of the checker 𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙. To simplify the notation, we used (∀𝑥𝑖 ∈ 𝑇𝑖) to denote (∀𝑥1 ∈ 𝑇1, . . .,∀𝑥𝑛 ∈ 𝑇𝑛) and 𝑦𝑓 is the final rejected sample if 𝑓𝑑 is used.

𝜑A =⇒ (∀𝜃 ∈ Θ.(∀𝑥𝑖 ∈ 𝑇𝑖).Φ𝑙 (𝑥1, . . .,𝑥𝑛) =⇒ 𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 (𝑥1, . . .,𝑥𝑛,𝑟) ∨ (𝑟 = 𝑓𝑑(𝑥1, . . .,𝑥𝑛,𝑦𝑓 )) (16) 𝜑A =⇒ ∀𝜃 ∈ Θ.(∀𝑥𝑖 ∈ 𝑇𝑖).Φ𝑙 (𝑥1, . . .,𝑥𝑛) ∧ (𝑟 = 𝑓𝑑(𝑥1, . . .,𝑥𝑛,𝑦𝑓 )) =⇒ Ψ𝑙 (𝑥1, . . .,𝑥𝑛,𝑟) (17) 𝜑A =⇒ (∀𝜃 ∈ Θ.(∀𝑥𝑖 ∈ 𝑇𝑖).(Φ𝑙 (𝑥1, . . .,𝑥𝑛) ∧ 𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 (𝑥1, . . .,𝑥𝑛,𝑟)) =⇒ Ψ𝑙 (𝑥1, . . .,𝑥𝑛,𝑟)) (18) 𝜑A =⇒ (∀𝜃 ∈ Θ.(∀𝑥𝑖 ∈ 𝑇𝑖).Φ𝑙 (𝑥1, . . .,𝑥𝑛) =⇒ Ψ𝑙 (𝑥1, . . .,𝑥𝑛,𝑟)) Using Eq. (16, 17, 18)

We provide the detailed formal proof in Appendix R. □

- 5.2.3 Computability of 𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 (Fig. 2) on concrete values. The auto-synthesized rejection

- sampler (Fig. 2) requires checking whether a sample 𝑦 from LΘ, given a concrete input (𝑥1, . . .,𝑥𝑛), satisfies the planner LLM–defined Ψ𝑙. We show that for any quantifier-free Ψ𝑙, this check can be computed efficiently for all concrete values (𝑥1, . . .,𝑥𝑛,𝑦). Since all library functions in F𝑐 are


computable,𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 can evaluate every term on the concrete inputs (𝑥1, . . .,𝑥𝑛,𝑦). Satisfiability can then be decided in linear time in the number of terms in Ψ𝑙. We provide formal completeness for the quantifier-free fragment in Lemma 5.1. For Ψ𝑙 with quantifiers, we instantiate 𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 with the axioms A. Then, 𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 substitutes the free variables in Ψ𝑙 with their corresponding concrete values, encodes the axioms A and Φ𝑙 similarly to Eq. 8, and submits the resulting formula to an SMT solver. First-order formulas over the basic types T and uninterpreted library functions may lie outside decidable fragments. Therefore, we bound the SMT solver with a user-specified timeout. 𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 returns true only if the solver succeeds within the timeout; otherwise, it returns false. This guarantees soundness; however, in the presence of quantifiers, 𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 may be incomplete and may incorrectly reject valid samples 𝑦.

- 5.2.4 Search and Verify. The search and verification steps jointly implement a CEGIS-style loop that explores candidate parametric programs while enforcing the behavioral specification. In the


search phase, the planner LLM L𝑝 first synthesizes a set of FGGM definitions G = {G1, . . ., G𝑚} following Eq. 15. Each FGGM wraps a parametric model with local contracts and a verified fallback. Using these FGGMs as callable functions, the planner then samples a candidate parametric program

P{Θ} where {Θ} = {Θ1, . . ., Θ𝑘} represents the set of all optimizable parameters in P{Θ}. As mentioned in § 4.3.1, FGGM calls at different program locations do not share parameters and add their own parameter in {Θ}. In the verification phase, SEVerA first checks the well-formedness of every G𝑖 ∈ G. If any of the definitions fail to verify it returns an error message. If all definitions are valid, the verification context C = (𝐺𝐷, F, A) is extended with the synthesized FGGMs and their local contracts. The updated context C′ = (𝐺𝐷, F∪G, A∪AG) adds all FGGMs G along with AG containing local contracts (G𝑖Φ𝑙, G𝑖Ψ𝑙) of each FGGM G𝑖 ∈ G. The candidate program P{Θ} is then checked for syntactic validity, termination, and compliance with the behavioral specification (Φ, Ψ). If verification succeeds, SEVerA accepts the parametric program P{Θ} and ensures that P{Θ} satisfies (Φ, Ψ) over all parameters (Theorem 5.3). Algorithm 1 summarizes the combined search–verification loop.

Given the input specification I and planner L𝑝, the algorithm iteratively proposes candidate solutions within a fixed budget 𝛿 (Lines 1–4). In each iteration, the planner first synthesizes a set of FGGM definitions G (Line 6), which are then checked for well-formedness using 𝑣𝑎𝑙𝑖𝑑𝑎𝑡𝑒𝐹𝐺𝐺𝑀 (Line 7). Within G, the planner LLM L𝑝 also synthesizes the prompting functions 𝑓𝑝, enabling each FGGM-specific customization. If the definitions are valid, the planner samples a candidate parametric program P{Θ} that may invoke these FGGMs (Line 11), and the verification context is extended with their contracts (Line 12). The candidate program is then validated for syntactic correctness, termination, and compliance with the behavioral specification using 𝑣𝑎𝑙𝑖𝑑𝑎𝑡𝑒𝑃𝑟𝑜𝑔𝑟𝑎𝑚 (Line 13). If verification succeeds, the program is returned (Lines 14–15); otherwise, theloop continueswith the error feedback until the search budget is exhausted (Lines 16–18).

### Algorithm 1 searchVerify

- 1: Input: I = (F, A, Φ, Ψ,𝐼), planner L𝑝, budget 𝛿
- 2: Input: Previous attempts feed-back 𝐼′
- 3: Output: Verified Parametric Program P{Θ} else ⊥
- 4: 𝑖 ← 0, err ← {}
- 5: while 𝑖 < 𝛿 do
- 6: G ← 𝑑𝑒𝑓 𝑖𝑛𝑒𝐹𝐺𝐺𝑀(L𝑝,𝐼, F, A,𝐼′, err)
- 7: err ← 𝑣𝑎𝑙𝑖𝑑𝑎𝑡𝑒𝐹𝐺𝐺𝑀(G, F𝑐, A)
- 8: if err ≠ {} then
- 9: 𝑖 ← 𝑖 + 1; continue
- 10: end if
- 11: P{Θ} ← 𝑠𝑎𝑚𝑝𝑙𝑒𝑃𝑟𝑜𝑔𝑟𝑎𝑚(L𝑝,𝐼, F, A,𝐼′, G, err)
- 12: C ← (𝐺𝐷, F ∪ G, A ∪ AG)
- 13: err ← 𝑣𝑎𝑙𝑖𝑑𝑎𝑡𝑒𝑃𝑟𝑜𝑔𝑟𝑎𝑚(P{Θ}, PC, TC, VC[Φ, Ψ])
- 14: if err = {} then
- 15: return P{Θ}
- 16: end if
- 17: 𝑖 ← 𝑖 + 1
- 18: end while
- 19: return ⊥


Theorem 5.3. If P{Θ} ≠ ⊥ with FGGM set G, then ∀𝜃1 ∈ Θ1, . . .,∀𝜃𝑘 ∈ Θ𝑘.𝜑A =⇒ ∀𝑥1 ∈ 𝑇1, . . .,∀𝑥𝑛 ∈ 𝑇𝑛.Φ(𝑥1, . . .,𝑥𝑛) =⇒ Ψ(𝑥1, . . .,𝑥𝑛, P{(𝜃1,...,𝜃𝑘)/Θ}(𝑥1, . . .,𝑥𝑛)) .

Proof Sketch. Follows from Theorem 5.2 with details in Appendix R. □

- 5.2.5 Learn. Once a candidate parametric program P{Θ} passes the search–verification loop (Algorithm 1), the verification step guarantees that P{Θ} satisfies the behavioral specification (Φ, Ψ) for all parameter values (Theorem 5.3). Hence, the learning step can freely select parameters without violating (Φ, Ψ). Finding the optimal solution to the general formulation in Eq. 19 over {Θ} for a general loss L is practically intractable. Instead, SEVerA employs a scalable gradient-descent–based optimization to efficiently search over {Θ}.


(𝑥,𝑦)∈D L(𝑥,𝑦, P{(𝜃1,...,𝜃𝑘)/Θ}(𝑥)) (19)

(𝜃1∗, . . .,𝜃𝑘∗) = argmin

(𝜃1,...,𝜃𝑘 )∈{Θ}

Conformance loss LΦ𝑙,Ψ𝑙 for each local contract (Φ𝑙, Ψ𝑙) encourages the parameters to produce outputs that satisfy their local contracts. By improving conformance with these contracts, SEVerA increases the success rate of the corresponding rejection sampler and thereby avoids triggering the static non-parametric fallback program. Since the fallback cannot be tuned, reducing its usage allows the gradient-based search to more effectively guide the parameters toward solutions that

reduce the final loss L. Our experiments in § 6.3 substantiate this observation, showing that reducing reliance on the fallback improves task performance. For a single FGGM with local contracts (Φ𝑙, Ψ𝑙) and parameter 𝜃, we define the conformance loss over an input set P in Eq. 20. The inner term L𝜃Φ

𝑙,Ψ𝑙 (𝑝) measures the probability that a sampled output from L𝜃 (𝑝) violates 𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙, while LΦ𝑙,Ψ𝑙 (𝜃) aggregates this violation across inputs.

LΦ𝑙,Ψ𝑙 (𝜃) = |P1| × 𝑝∈P L𝜃Φ

, where L𝜃Φ𝑙,Ψ𝑙 (𝑝) = E𝑦∼L𝜃 (𝑝)1 − I(𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 (𝑥1, . . .,𝑥𝑛,𝑦))

(20)

𝑙,Ψ𝑙 (𝑝) Aggregated constraint violation over P

Expected constraint violation on single GM input 𝑝

The augmented objective, which includes a local conformance loss for each FGGM call, is defined in Eq. 21, where 𝜆 ∈ R+ is a user-provided constant.

𝑙,Ψ𝑙 (𝜃𝑖) (21)

(𝑥,𝑦)∈D L(𝑥,𝑦, P{(𝜃1,...,𝜃𝑘)/Θ}(𝑥)) + 𝜆 × 𝑖∈𝑘,(𝑥,𝑦)∈D L𝑖Φ

Here, the first term is the task-specific loss over the dataset D, and the second term aggregates the local conformance losses (Eq. 20) of the FGGMs appearing in the program. Optimizing all parameters jointly according to Eq. 21, while feasible for smaller neural networks, becomes practically expensive for agents with multiple interdependent LLM calls. To address this challenge, we leverage a key

structural property: the conformance loss L𝑖Φ

𝑙,Ψ𝑙 (𝜃𝑖) for each FGGM depends only on the local inputs to that FGGM call and the outputs of its underlying GM, not on the parameters of other FGGMs. This independence arises because each FGGM’s rejection sampler and 𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 checker operate solely on the local contract (Φ𝑙𝑖, Ψ𝑙𝑖) and the corresponding GM’s outputs. As a result, the conformance term decomposes naturally across FGGM calls. Following this observation, for larger models we approximate the augmented loss by optimizing each FGGM 𝑖𝑑𝜃𝑖 with parameter 𝜃𝑖 independently, as shown in Eq. 22. Here, the first term includes the task-specific loss L only when the output 𝑦𝑙 of 𝑖𝑑𝜃𝑖 matches the final output 𝑦 of the agent on input 𝑥, where (𝑥, _) ∈ D. The modularized loss (Eq. 22) enables efficient parallelized training across different 𝜃𝑖.

L𝑎(𝜃𝑖) = |P1| × 𝑝∈P L𝜃𝑎𝑖 (𝑝); L𝜃𝑎𝑖 (𝑝) = E𝑦𝑙∼𝑖𝑑𝜃

𝑙,Ψ𝑙 (𝑝) (22) R(𝑝,𝑦𝑙) = 1 − 𝑆𝑖𝑔𝑚𝑜𝑖𝑑 L(𝑥, _,𝑦) × I(𝑦 = 𝑦𝑙) + 𝜆 × (1 − I(𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 (𝑝,𝑦𝑙)) (23)

𝑖 (𝑝)L(𝑥, _,𝑦) × I(𝑦 = 𝑦𝑙) + 𝜆 × L𝜃Φ𝑖

For generative models with accessible parameters, the objective in Eq. 22 can be optimized using reinforcement learning–based fine-tuning methods such as GRPO [36] (details in Appendix N). Eq. 23 defines the reward for an input-output pair (𝑝,𝑦𝑙), with the goal of learning an output distribution over 𝑦𝑙 for inputs 𝑝 ∈ P that maximizes total reward R(𝑝,𝑦𝑙). The reward function combines two signals: (1) the task-specific loss L, which drives the GM toward outputs that reduce overall task error, and (2) the conformance indicator I(𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 (𝑝,𝑦𝑙)), which rewards outputs satisfying the local contract. The sigmoid transformation maps the combined penalty to the [0, 1] range, providing a smooth reward landscape. Outputs that violate the local contract receive nearzero reward due to the (1−I(𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 (𝑝,𝑦𝑙))) penalty term, strongly discouraging the GM from producing outputs that would be rejected by the rejection sampler. The reward function need not be differentiable w.r.t. 𝜃𝑖, as long as the outputs𝑦𝑙 remain differentiable w.r.t. 𝜃𝑖 [36]. For closed-source models with inaccessible parameters, the learning step is skipped, and performance improvements rely solely on prompt tuning through the synthesized 𝑓𝑝 programs within each FGGM.

- 5.2.6 SEVerA. Algorithm 2 summarizes the overall workflow of SEVerA. The algorithm maintains a pool P of verified candidate agents and iteratively improves it through a search–verify–learn loop. In each iteration, SEVerA first invokes the searchVerify procedure (Algorithm 1), which performs CEGIS-style discrete search to synthesize FGGM definitions and candidate parametric program


P{Θ} that satisfy the behavioral specification (Φ, Ψ). If verification succeeds, the program is passed to the learn procedure, which optimizes the parameters of the underlying generative models using the dataset D and task loss L. For closed-source models with inaccessible parameters, this step is

skipped, and performance improvements rely solely on prompt tuning through the synthesized 𝑓𝑝 programs in each FGGM.

The resulting tuned agent is added to the candidate pool, and its execution traces on D are used to construct feedback 𝐼′ (see Appendix P) that guides the planner in subsequent search iterations. After the search budget Δ is exhausted, SEVerA returns the agent in the pool that achieves the lowest task loss on the dataset. If P is empty, SEVerA returns ⊥.

Algorithm 2 SEVerA

- 1: Input: I = (F, A, L, D, Φ, Ψ,𝐼), planner L𝑝
- 2: Input: total budget Δ, budget per candidate 𝛿
- 3: Output: Best agent 𝑓 ∗ or ⊥ if search fails
- 4: P ← {} ⊲ Pool of verified candidates
- 5: 𝐼′ ← ∅
- 6: while 𝛿 ≤ Δ do
- 7: P{Θ} ← 𝑠𝑒𝑎𝑟𝑐ℎ𝑉𝑒𝑟𝑖𝑓 𝑦(F, A, Φ, Ψ,𝐼, L𝑝, 𝛿,𝐼′)
- 8: Δ ← Δ − 𝛿
- 9: if P{Θ} = ⊥ then
- 10: continue
- 11: end if
- 12: if {Θ} ≠ {} then
- 13: (𝜃1∗, . . .,𝜃𝑘∗) ← 𝑙𝑒𝑎𝑟𝑛(P{Θ}, L, D)
- 14: P ← P ∪ {P{(𝜃1∗,...,𝜃𝑘∗)/Θ}}
- 15: else
- 16: P ← P ∪ {P{Θ}}
- 17: end if
- 18: 𝐼′ ← 𝑐𝑜𝑙𝑙𝑒𝑐𝑡𝐹𝑒𝑒𝑑𝑏𝑎𝑐𝑘(P{Θ}, D)
- 19: end while
- 20: 𝑓 ∗ ← argmin𝑓 ∈P (𝑥,𝑦)∈D L(𝑥, 𝑦, 𝑓 (𝑥))
- 21: return 𝑓 ∗


#### 5.3 Theoretical Results

The soundness of SEVerA guarantees that any agent program 𝑓 ∗ ≠ ⊥ returned satisfies the behavioral specifications (Φ, Ψ). The searchVerify step generates candidate programs P{Θ} that satisfy (Φ, Ψ) for all (𝜃1, . . .,𝜃𝑘) ∈ {Θ}. Consequently, the parameters (𝜃1∗, . . .,𝜃𝑘∗) predicted by the learning step preserve constraint satisfaction. The pool P is either empty or contains only programs that satisfy the behavioral specifications.

Theorem 5.4 (Soundness). If 𝑓 ∗ ≠ ⊥ then, 𝜑A =⇒ ∀𝑥1 ∈ 𝑇1, . . .,∀𝑥𝑛 ∈ 𝑇𝑛.Φ(𝑥1, . . .,𝑥𝑛) =⇒ Ψ(𝑥1, . . .,𝑥𝑛, 𝑓 ∗(𝑥1, . . .,𝑥𝑛)).

Proof Sketch. (𝑓 ∗ ≠ ⊥) =⇒ (𝑓 ∗ ∈ P) and all program 𝑓 ∈ P satisfies 𝜑A =⇒ ∀𝑥1 ∈ 𝑇1, . . .,∀𝑥𝑛 ∈ 𝑇𝑛.Φ(𝑥1, . . .,𝑥𝑛) =⇒ Ψ(𝑥1, . . .,𝑥𝑛, 𝑓 (𝑥1, . . .,𝑥𝑛)) following Theorem 5.3. We provide the formal details in Appendix R. □

Next, we characterize a sufficient condition that ensures the existence of a candidate solution 𝑓 ∈ S(𝐺, F) that satisfies (Φ, Ψ) and achieves no worse loss L than any generative model 𝑓𝑛𝜃 ∈ F𝑝 with any prompting function 𝑓𝑝 ∈ S(𝐺, F𝑐) and initial parameters 𝜃0. The high-level idea is as follows. If there exists a non-parametric program 𝑓𝑑 ∈ S(𝐺, F𝑐) that satisfies (Φ, Ψ), we can use it as a fallback together with any type-correct generative model 𝑓𝑛𝜃 (i.e., with output type𝑇𝑜) to construct an FGGM. A program that invokes this FGGM on the input and returns its output satisfies (Φ, Ψ). Moreover, if 𝑐ℎ𝑒𝑐𝑘A,Φ,Ψ is complete and does not incorrectly reject valid samples from 𝑓𝑛𝜃, then the FGGM always returns valid samples from 𝑓𝑛𝜃. Lemma 5.1 shows that 𝑐ℎ𝑒𝑐𝑘A,Φ,Ψ is complete when Ψ is quantifier-free. Assume: (i) L penalizes constraint-violating outputs more than constraintsatisfying ones, i.e., ∀𝑥 ∈ 𝑇𝑖, ∀𝑦,𝑦′ ∈ 𝑇𝑜. (Φ(𝑥) ∧ ¬Ψ(𝑥,𝑦) ∧ Ψ(𝑥,𝑦′)) =⇒ L(𝑥, _,𝑦′) < L(𝑥, _,𝑦), (ii) Ψ is quantifier-free, and (iii) there exists a valid non-parametric program 𝑓𝑑 satisfying (Φ, Ψ). Then there exists a program 𝑓 ∈ S(𝐺, F) that satisfies (Φ, Ψ) and incurs no greater loss than any type-correct generative model 𝑓𝑛𝜃 : 𝑇𝑖 → 𝑇𝑜 with initial parameters. Moreover, if 𝑓𝑛𝜃 (𝑥) violates Ψ(𝑥, 𝑓𝑛𝜃 (𝑥)) for some (𝑥, _) ∈ D, the improvement in loss is strict.

Theorem 5.5 (Sufficient Success Condition). If (i) L penalizes constraint violations, i.e.,∀𝑥 ∈ 𝑇𝑖, ∀𝑦,𝑦′ ∈ 𝑇𝑜. (Φ(𝑥)∧¬Ψ(𝑥,𝑦)∧Ψ(𝑥,𝑦′)) =⇒ L(𝑥, _,𝑦′) < L(𝑥, _,𝑦),, (ii) Ψ is quantifier-free, (iii) there exists a non-parametric program 𝑓𝑑 ∈ S(𝐺, F𝑐) such that 𝑓𝑑 satisfies (Φ, Ψ). Then, for any typecorrect generative model 𝑓𝑛𝜃 : 𝑇𝑖 → 𝑇𝑜 with initial parameters and any prompting program 𝑓𝑝, there

exists a program 𝑓 ∈ S(𝐺, F) such that: (1) 𝑓 satisfies (Φ, Ψ), and (2) L(𝑓 ) ≤ L(𝑓𝑛𝜃). Moreover, if there exists (𝑥, _) ∈ D such that ¬Ψ(𝑥, 𝑓𝑛𝜃 (𝑥)), then L(𝑓 ) < L(𝑓𝑛𝜃) where 𝐿(𝑓 ) = (𝑥,_)∈D L(𝑥, _, 𝑓 (𝑥)).

Proof Sketch. Define G = (𝑖𝑑, 𝑓𝑛𝜃,𝜏, Φ𝑙, Ψ𝑙, 𝑓𝑝, 𝑓𝑑,𝑖𝑛𝑓𝑜) where (Φ𝑙, Ψ𝑙) := (Φ, Ψ). Since 𝑓𝑑 satisfies (Φ, Ψ), the FGGM is valid. Define the program:

function 𝑓 (𝑥1 : 𝑇1, . . .,𝑥𝑛 : 𝑇𝑛) : 𝑇𝑜{return 𝑖𝑑(𝑥1, . . .,𝑥𝑛); }

For any input satisfying Φ, by completeness of 𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 (Lemma 5.1), 𝑖𝑑 returns 𝑓𝑛𝜃 (𝑥) when-

ever Ψ(𝑥, 𝑓𝑛𝜃 (𝑥)) holds, and otherwise returns 𝑓𝑑(𝑥), which satisfies Ψ. For each (𝑥, _) ∈ D, 𝑓 (𝑥) either equals 𝑓𝑛𝜃 (𝑥) (if valid) or 𝑓𝑑(𝑥). By assumption (i), such replacement cannot increase loss, so L(𝑓 ) ≤ L(𝑓𝑛𝜃). If 𝑓𝑛𝜃 violates Ψ on some (𝑥, _) ∈ D, the improvement is strict. Formal details in Appendix R. □

Theorem 5.5 provides a constructive argument: the FGGM mechanism can always improve upon a bare GM call by filtering out constraint-violating outputs and substituting the fallback. The three assumptions are mild in practice. Assumption (i) requires only that constraint-satisfying outputs are preferred over violating ones, which holds for any reasonable loss function in constrained settings. Assumption (ii), requiring quantifier-free Ψ, ensures completeness of the checker 𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 (Lemma 5.1) so that no valid GM outputs are incorrectly rejected. In our experiments, the symbolic regression task uses quantifier-free specifications, while the program verification task uses library-function predicates (e.g., 𝑝𝑎𝑟𝑠𝑒, 𝑛𝑜𝐷𝑖𝑓 𝑓 ) that are computable on concrete inputs, effectively behaving as quantifier-free checks at runtime. Assumption (iii), the existence of a valid fallback, is a natural requirement: if no non-parametric program can satisfy the specification, then the specification may be too strong for the given library. The theorem does not guarantee that SEVerA will find the optimal program, as the planner LLM may not propose the right candidate within the search budget. Rather, it establishes that the search space S(𝐺, F) is rich enough to contain solutions that dominate unconstrained GM calls.

#### 6 Evaluation

We evaluate SEVerA on four tasks spanning scientific discovery, program verification, mathematical reasoning, and agentic tool use. The evaluation seeks to answer three main questions: whether formal constraints improve safety, whether learning remains effective under those constraints, and how conformance tuning with local constraints improves performance.

#### 6.1 Experimental Setup

- 6.1.1 Tasks and Datasets. We instantiate SEVerA on four tasks, each representative of a different kind of constrained agent synthesis problem. LLM-Assisted Program Verification (DafnyBench). The agent receives a Dafny program with pre-encoded input-output specifications and must synthesize annotations that enable verification against the pre-encoded specification inside the input program [29]. The behavioral specification of the agent requires the output to remain parsable and equivalent to the input modulo added annotations. The task performance is measured by verification success within a fixed time budget. The underlying LLM is Claude Sonnet 4.5 [2], a closed-source model whose weights are not accessible; consequently, the learning step (i.e., parameter tuning) is not applicable to this task. Symbolic Math Synthesis (GSM-Symbolic). GSM-Symbolic is a benchmark of grade-school math word problems generated from symbolic templates [30]. We use it to evaluate the LLM’s ability to synthesize correct symbolic mathematical expressions. Behavioral specification of the agent enforces that each generated expression is syntactically valid with respect to a formal grammar, and task performance measures whether the answer is equivalent to the ground-truth expression.


Agentic Tool Use (𝜏2-bench). 𝜏2-bench [5] evaluates conversational LLM agents in realistic customer-service scenarios. We use the retail and airlines domains. The agent must select and invoke API tools to resolve user requests while respecting domain-specific policies. Unlike the other tasks, the hard constraint and the utility metric operate at different granularities. The hard constraint is enforced at each individual tool call: before every tool call is executed, the Agent-C checker [20] verifies that the proposed call complies with temporal policy-compliance rules (e.g., refund eligibility, booking-modification policies) given the trace of prior calls. Task performance (pass rate) is measured over the entire multi-turn interaction trace as the percentage of interactions where the agent successfully resolves the user request.

Constrained Symbolic Regression (SymReg). In symbolic regression, each synthesis instance consists of noisy input–output observations generated by an unknown ground-truth function 𝑓𝑔𝑡, along with a behavioral specification encoding prior knowledge about 𝑓𝑔𝑡. The goal is to synthesize a neuro-symbolic program (i.e., the agent) that fits the observed input–output pairs while provably satisfying the behavioral specifications. We consider a total of 35 synthesis tasks, each with 2 different training sets corresponding to varying noise levels (5%, 10%), and behavioral specifications that encode symbolic bounds on the ground truth. Each training set includes 600 noisy

- samples and 400 test samples. All synthesis instances are drawn from popular benchmarks [7, 17].


- 6.1.2 Implementation Details. All experiments are conducted on NVIDIA A100 GPUs (40GB). Across all tasks we use the same high-level pipeline: planner-guided program search with a budget of Δ = 10 iterations, FGGM-based rejection sampling with a fixed sample budget 𝐾 = 5, deductive verification with bounded verifier and SMT timeouts, and hyperparameter tuning when model parameters are accessible. The planner LLM is provided with 3 ground-truth examples as in-context examples (2 for 𝜏2-bench, due to the long traces); these examples are excluded from all train and test splits. The full planner prompt template is given in Appendix Q, and details on how execution feedback is constructed and provided to the planner between iterations are given in Appendix P.
- 6.1.3 Learning Implementation. Once a program verifies, SEVerA uses Dafny’s built-in transpiler [9] to translate the verified code into Python. Parameter tuning and experiments are then conducted on the transpiled code. SEVerA assumes that Dafny’s transpiler is sound for this restricted subset of the language.
- 6.1.4 Metrics. For each task, we report: (a) the constraint violation rate on a held-out test set of unseen inputs, measuring the fraction of outputs that violate the behavioral specification (Φ, Ψ); (b) task performance, measured by mean squared error for SymReg, verification success rate for Dafny, answer accuracy for GSM-Symbolic, and pass rate for 𝜏2-Bench; and (c) wall-clock time.
- 6.1.5 Baseline. For all four tasks outside GSM-symbolic, we consider state-of-the-art (SOTA) handcrafted agents. For GSM-Symbolic, we use the SOTA constrained decoder [4]. Some hand-crafted agents (e.g., Agent-C on 𝜏2-Bench) manually enforce hard constraints; however, being static, they achieve lower task performance. We also consider self-evolving frameworks without constraints, which do not verify the generated programs against behavioral specifications and accept all planner programs provided they are syntactically valid and type-checked. Consequently, such frameworks provide no guarantees about the correctness or safety of the generated code. To ensure fairness, unconstrained self-evolving frameworks are only allowed to use the same set of library functions.
- 6.1.6 Verification Success. For program verification, tool calling, and GSM-Symbolic, SEVerA consistently finds a valid program satisfying (Φ, Ψ) within 10 attempts. For symbolic regression, it produces a verified program in 33 out of 35 cases, whereas the baselines generate at least 11 cases where the generated program violates the behavioral specification on test inputs.


- Table 2. Dafny program verification results on HumanEvalDafny and DafnyBench. Verif. & NoDiff counts a program as correct only if it both verifies and passes the AST-based diff check against the original; Verif. counts verification alone.


###### Dataset Method Ver. & NoDiff (%) ↑ Ver. (%) ↑ Vio. (%) ↓ Time (s)

LLM (Claude Sonnet 4.5) 73.7 76.8 8.1 9.8 DafnyBench baseline 86.9 87.9 4.0 16.1 SEVerA (w/o constraints) 84.8 88.9 5.1 15.7 SEVerA 97.0 (+10.1) 97.0 (+9.1) 0.0 (-4.0) 18.2

HumanEvalDafny

LLM (Claude Sonnet 4.5) 68.7 71.1 10.3 10.3 DafnyBench baseline 81.6 84.0 8.2 20.1 SEVerA (w/o constraints) 79.2 84.8 7.9 18.4 SEVerA 89.1 (+7.5) 89.1 (+5.1) 0.0 (-8.2) 25.6

DafnyBench

- 6.1.7 Dataset splits. Table 1 summarizes the dataset sizes for each synthesis task. For each task, a small training set is used for the learning step and the remaining examples form the held-out test set on which all reported metrics are computed. GSM-Symbolic uses a larger training fraction (50%) because its learning step performs GRPO-based fine-tuning, which requires more training data than the other tasks.
- 6.1.8 Task-specific details. For Dafny, the underlying LLM is Claude Sonnet 4.5 [2], a closedsource model; because model weights are inaccessible, Dafny experiments use only the search and verification stages of SEVerA and do not perform parameter tuning. For 𝜏2-bench, parameter tuning is also omitted because the long, multi-turn execution traces make gradient-based fine-tuning prohibitively expensive. For GSM-Symbolic, the learning step uses GRPO [36] with LoRA adapters [18] on Qwen3-8B [42]. Additional hyperparameters (LoRA rank, solver timeouts, etc.) are reported in Appendix O.


Dataset Total Train HumanEvalDafny 135 30 DafnyBench 760 50 𝜏2-bench Retail 114 15 𝜏2-bench Airline 50 10 GSM-Symbolic 100 50 Symbolic Regression 600 400 Table 1. Dataset sizes and train/test splits.

- 6.2 Main Results We begin with the central question motivating SEVerA:


RQ1 (Safety). What goes wrong without formal constraints, and does SEVerA eliminate these failures?

We compare unconstrained agent synthesis against SEVerA across all four tasks to show that hard behavioral specifications are necessary: without them, agents silently produce invalid outputs on unseen inputs that are undetectable by soft performance metrics.

- 6.2.1 LLM-Assisted Program Verification (Dafny). Table 2 presents results on two Dafny programverification benchmarks and offers the clearest illustration of why formal constraints are indispensable. The gap between the Verif. and Verif. & NoDiff columns reveals the core safety issue (RQ1): without hard constraints, agents inflate their verification rate by modifying the original program. The LLM baseline reports 76.8% verification on HumanEvalDafny, yet only 73.7% of those outputs actually preserve the input program. Overall, 8.1% of all outputs are violations that would go undetected by a metric that checks verification alone. The DafnyBench baseline and SEVerA without constraints reduce but do not eliminate this problem (4.0% and 5.1% violations, respectively). Only the full SEVerA pipeline, which enforces the NoDiff behavioral specification, achieves a 0% violation rate on both benchmarks while simultaneously attaining the highest Verif.


###### Table 3. 𝜏2-bench results with Qwen3-8B on the retail and airline domains. Higher pass rate is better; lowerviolation rate is better.

Domain Method Pass Rate (%) ↑ Violation (%) ↓ Time (s)

LLM (Qwen3-8B) 11.3 76.3 146.6 Agent-C (Qwen3-8B) 42.2 0.0 234.7 SEVerA (w/o constraints) 49.4 10.3 238.3 SEVerA 53.6 (+11.4) 0.0 (0.0) 212.4

Retail

LLM (Qwen3-8B) 13.2 68.4 184.8 Agent-C (Qwen3-8B) 39.4 0.0 272.6 SEVerA (w/o constraints) 44.7 25.5 268.4 SEVerA 52.6 (+13.2) 0.0 (0.0) 241.1

Airline

& NoDiff rate (97.0% on HumanEvalDafny, 89.1% on DafnyBench). This confirms that FGGM-based rejection sampling with a verified fallback does not merely filter outputs but actively steers the planner toward higher-quality candidates. This result is particularly notable because it is achieved without any parameter tuning (the underlying model, Claude Sonnet 4.5, is closed-source), the gains come entirely from making constraints visible to the planner and enforcing them at synthesis time. The overhead introduced by SEVerA is modest. The full pipeline takes 18.2s per instance on HumanEvalDafny compared to 9.8 s for LLM generation, roughly a 1.9× factor that includes Dafny verification and up to 𝑘 LLM calls. On DafnyBench the factor is 2.5× (25.6s vs. 10.3s). Given that the LLM baseline produces untrustworthy outputs on 8 to 10% of inputs, we believe this overhead is justified for the formal guarantees it provides.

- 6.2.2 Agentic Tool Use (𝜏2-bench). Table 3 reports performance on 𝜏2-bench. The LLM baseline (Qwen3-8B without constraints) violates domain policies on 76.3% of retail interactions and 68.4% of airline interactions, yielding pass rates of only 11.3% and 13.2%, respectively. Both Agent-C and SEVerA reduce the violation rate to 0%, confirming that formal policy enforcement is necessary. SEVerA without constraints illustrates an intermediate point: by running the search loop without informing the planner of the policy specification, SEVerA (w/o constraints) improves pass rates to 49.4% (retail) and 44.7% (airline), but still incurs 10.3% and 25.5% violation rates, respectively. Enforcing constraints eliminates all violations while further improving pass rates to 53.6% and 52.6%. This gap reflects SEVerA’s search-verify-learn design. By synthesizing agent programs that are verified to satisfy the per-call policy specification, SEVerA can explore a wider space of compliant strategies rather than relying solely on runtime constraint checking. The per-call hard constraint ensures that every individual tool call is policy-compliant, while the search loop optimizes the agent’s overall strategy to maximize the end-of-trace pass rate. Impressively, SEVerA with the small open-weight Qwen3-8B outperforms Agent-C [20] with Claude Sonnet 4.5 (52.6 vs 47.3). SEVerA is also faster than Agent-C in both domains (212.4s vs. 234.7s in retail and 241.1s vs. 272.6s in airline). The LLM baseline is fastest because it performs no policy checking, but its outputs are unusable in practice given the violation rates.
- 6.2.3 Symbolic Math Synthesis (GSM-Symbolic). GSM-Symbolic uses Qwen3-8B as the underlying LLM. Qwen3-8B is open-weight, making parameter tuning feasible. This allows us to ask:


RQ2 (Training Impact). Does parameter tuning improve task performance under formal constraints?

###### Table 4 compares SEVerA against the LLM baseline and CRANE [4], a state-of-the-art constrained-decoding method, on GSM-Symbolic using Qwen3-8B. The LLM baseline (Qwen3-8B) achieves

- Table 4. GSM-Symbolic results with Qwen3-8B. Higher accuracy is better; lower violation rate is better. Method Accuracy (%) ↑ Violation (%) ↓ Time (s)

LLM (Qwen3-8B) 38.3 10.6 10.9 CRANE [4] 44.7 2.1 12.4 SEVerA (no parameter tuning) 53.2 (+8.5) 0.0 (-2.1) 18.8 SEVerA (with parameter tuning) 66.0 (+21.3) 0.0 (-2.1) 16.7

- Table 5. % of synthesised instances that violate behavioral specifications on the test set.

Method 𝜖 (5%) ↓ 𝜖 (10%) ↓

PySR 62.86% 62.86% LLM-SR 31.43% 34.29% SEVerA 0.00% 0.00%

Table 6. NMSE values averaged over all instances that do not violate constraints on test data.

Comparison 𝜖 = 0.05 𝜖 = 0.1

SEVerA Baseline SEVerA Baseline

vs PySR 0.0593 0.3113 0.0879 0.1217 vs LLM-SR 0.0200 0.1580 0.0205 0.1583

only 38.3% accuracy with a 10.6% constraint violation rate (RQ1), confirming that a vanilla LLM frequently produces outputs that are syntactically or semantically invalid. CRANE improves accuracy to 44.7% and reduces violations to 2.1% by augmenting the output grammar with reasoning tokens. 1SEVerA without parameter tuning already achieves 53.2% accuracy and eliminates all violations, an 8.5% accuracy improvement over CRANE with strictly stronger correctness guarantees. This improvement stems from the FGGM mechanism: the rejection sampler with a verified fallback ensures that every output satisfies the formal grammar and the semantic specification, while the synthesized prompting program 𝑓𝑝 guides the underlying LLM toward correct answers. We also compare the performance of SEVerA with and without parameter tuning (RQ2). We finetune Qwen3-8B via GRPO with LoRA adapters under the same formal constraints. This provides a further 12.8% accuracy gain (from 53.2% to 66.0%) while maintaining the zero-violation guarantee. The tuned model produces outputs that more often pass the FGGM checker 𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 on the first sample, reducing reliance on the fallback and thereby improving answer quality. Notably, the tuned variant is also faster than the untuned one (16.7s vs. 18.8s), because higher conformance reduces the number of rejection-sampling iterations needed per call.

- 6.2.4 Constrained Symbolic Regression. In constrained symbolic regression, we consider the SOTA genetic programming–based method PySR [8], as well as the existing self-evolving method LLM-SR [37], which samples parametric programs with optimizable PyTorch parameters and refines them to minimize loss. We denote the noise level by𝜖. As shown in Table 5, both baselines frequently produce programs that violate the behavioral specifications on the test data, with violations occurring in up to 62.86% of synthesis instances for PySR and up to 34.29% for LLM-SR. For both noise levels, SEVerA finds a verified solution in 33 out of 35 instances. Table 6 presents a pairwise comparison between SEVerA and the baselines in terms of normalized mean squared error (NMSE) on the test dataset. We compute the average NMSE over only those instances where the baseline-generated programs satisfy the behavioral constraints, pruning instances that correspond to invalid solutions. SEVerA achieves significantly lower NMSE values compared to both baselines.


#### 6.3 Constraint Decomposition

The previous section showed that formal constraints improve both safety and performance. We now ask a finer-grained question:

1CRANE only ensures that at every decoding step, the generated partial output is a valid prefix of the target grammar.

- Table 7. Constraint decomposition ablation on GSM-Symbolic (Qwen3-8B). Local = FGGM contracts only; Global = behavioral specification only; Full = both.


###### Configuration Accuracy (%) ↑ Violation (%) ↓

LLM (Qwen3-8B) 38.3 10.6 SEVerA (no parameter tuning) 53.2 (+14.9) 0.0 (-10.6) SEVerA (local only parameter tuning) 55.3 (+17.0) 0.0 (-10.6) SEVerA (global only parameter tuning) 61.7 (+23.4) 0.0 (-10.6) SEVerA (full) 66.0 (+27.7) 0.0 (-10.6)

RQ3 (Constraint Decomposition). What are the individual contributions of parameter tuning with local FGGM contracts versus global loss L?

We ablate each component independently on GSM-Symbolic. Table 7 decomposes the 12.8% gain that parameter tuning provides (from 53.2% to 66.0%, as shown in Table 4) into its two sources. Starting from SEVerA without parameter tuning (53.2%), adding local-only tuning, which optimizes the FGGM conformance loss so that the model’s outputs more frequently satisfy per-call contracts, yields a modest improvement to 55.3%. This 2.1% gain indicates that parameter tuning alone helps the model produce syntactically valid outputs more reliably, reducing reliance on rejection sampling. Global-only tuning, which optimizes the task loss L without the FGGM conformance component, provides a substantially larger gain to 61.7%. This 8.5% improvement reflects the direct benefit of training the model to produce semantically correct answers. The full SEVerA pipeline combines both losses and achieves 66.0%, a 4.3% gain. This demonstrates that the two training signals are complementary: global tuning improves answer correctness while local conformance tuning ensures outputs satisfy per-call contracts, jointly yielding the best overall accuracy.

#### 6.4 Example Synthesized Agent

We provide a complete agent program synthesised by SEVerA for the DafnyBench task in Appendix K. The agent defines three FGGMs: 𝑖𝑛𝑖𝑡𝑖𝑎𝑙𝐹𝐺𝐺𝑀, 𝑑𝑖𝑓 𝑓 𝐸𝑟𝑟𝑜𝑟𝐹𝐺𝐺𝑀, and 𝑣𝑒𝑟𝑖𝑓𝑖𝑒𝑟𝐸𝑟𝑟𝑜𝑟𝐹𝐺𝐺𝑀. Each sharing the local output contract Ψ𝑙 := 𝑛𝑜𝐷𝑖𝑓 𝑓 (𝑏𝑎𝑠𝑒_𝑝𝑟𝑜𝑔𝑟𝑎𝑚, ·) and differing only in their prompting function 𝑓𝑝, which specialises the LLM prompt for initial annotation, diff-checker repair, and verifier-error repair, respectively. The resulting agent program is verified to provably comply with the diff-checker specification for all inputs and all parameter values, ensuring that no synthesised output modifies the original program beyond adding annotations.

#### 6.5 Discussion

Across all four tasks, SEVerA achieves zero constraint violations on held-out test inputs while simultaneously improving task performance over every baseline. These results confirm that formal behavioral specifications do not merely enforce safety but actively prune the space of candidate programs, steering synthesis toward higher-quality agents. SEVerA’s runtime overhead is competitive: on 𝜏2-bench it is faster than Agent-C, and on Dafny and GSM-Symbolic the full pipeline introduces a modest 1.9–2.5× slowdown relative to the LLM baseline, attributable to the verification and rejection-sampling steps. One current limitation is that the formulation is resource-unaware: behavioral specifications constrain functional correctness but do not account for computational resources such as LLM calls, token usage, or wall-clock budget. Extending SEVerA with resource-bound specifications [23], for example by encoding token or call budgets as additional hard constraints within the FGGM framework, is a promising direction for future work.

#### 7 Related Work

Self-Evolving Agents and Their Risks. Recent work has explored automatic agent synthesis and self-improvement, from code-based action unification [49] and open-ended skill libraries [47] to architecture search [13, 19, 53], gradient-free symbolic updates [51], co-evolution with world models [11], and reinforcement-learning-driven skill refinement [43, 48]. However, none of these provide formal behavioral guarantees, a gap made urgent by demonstrated risks of coding-agent exploits [14, 15, 25], test-case exploitation [50], and verification cheating [3]. SEVerA addresses this by imposing and verifying hard formal specifications before deployment.

Runtime Monitoring and Shielding. Rather than verifying at synthesis time, runtime approaches enforce safety on observed executions. Shield synthesis from neural policies [52] and temporal-logic runtime checking of tool-call sequences [20] are representative examples, but both are limited to observed traces and cannot guarantee safety on unseen inputs. SEVerA instead verifies the synthesized program for all inputs and parameter values at synthesis time. The monitoring checks can be used to define the specification as done with [20].

Neuro-Symbolic Program Synthesis. Neuro-symbolic methods, including neural program generation from examples [34], type-directed differentiable programming [46], wake-sleep library learning [10], vision-language program composition [41], and LLM-guided symbolic regression [37], synthesize programs that invoke neural components but lack formal correctness guarantees over the composed system. SEVerA extends this paradigm with FGGMs that bind each model call to a verified local contract, enabling end-to-end verification.

Constrained Decoding. Constrained decoding restricts LLM outputs to a formal language through grammar-based [35, 44, 45], diffusion-based [40], programming-abstraction [6, 21], reasoningpreserving [4], type-based [32], and semantic [33] techniques. These approaches require access to the model’s decoding internals (precluding closed-source models) and enforce per-token or per-output constraints, not program-level behavioral specifications. SEVerA’s FGGM mechanism operates on model outputs via rejection sampling, supports rich first-order logic specifications verified at the program level, and is model-agnostic.

DeductiveProgramSynthesis.Classicaldeductivesynthesis,including syntax-guided [1], semantics-

guided [22], counterexample-guided [38], abstraction-guided [16], and component-based [12] approaches, provides strong correctness guarantees but targets deterministic, non-parametric programs. SEVerA bridges this gap with a CEGIS-style search–verify loop for program structure while using FGGMs to encapsulate parametric generative models within verified contracts.

#### 8 Conclusion

We presented SEVerA, a framework for synthesizing self-evolving LLM agents with formal behavioral guarantees. By introducing Formally Guarded Generative Models (FGGMs), SEVerA binds each generative model call to a verified local contract backed by a rejection sampler with a provably correct fallback, ensuring that specifications hold for all inputs and all parameter values. This design decomposes the constrained learning problem into a CEGIS-style discrete search over program structure followed by unconstrained gradient-based parameter optimization, retaining the scalability of modern fine-tuning methods such as GRPO while providing end-to-end correctness guarantees. Our evaluation across constrained symbolic regression, LLM-assisted Dafny verification, symbolic math synthesis, and policy-compliant agentic tool use demonstrates that SEVerA achieves zero constraint violations on all tasks while simultaneously improving task performance over unconstrained and state-of-the-art baselines. These results show that formal behavioral constraints are not merely a safety mechanism but an active guide that prunes the search space and steers synthesis toward higher-quality agents.

#### References

- [1] Rajeev Alur, Rastislav Bodik, Garvit Juniwal, Milo M. K. Martin, Mukund Raghothaman, Sanjit A. Seshia, Rishabh Singh, Armando Solar-Lezama, Emina Torlak, and Abhishek Udupa. 2013. Syntax-guided synthesis. In 2013 Formal Methods in Computer-Aided Design. 1–8. doi:10.1109/FMCAD.2013.6679385
- [2] Anthropic. 2025. System Card: Claude Sonnet 4.5. https://www-cdn.anthropic.com/ 963373e433e489a87a10c823c52a0a013e9172dd.pdf. Accessed: 2026-03-18.
- [3] Debangshu Banerjee, Olivier Bouissou, and Stefan Zetzsche. 2026. DafnyPro: LLM-Assisted Automated Verification for Dafny Programs. arXiv:2601.05385 [cs.SE] https://arxiv.org/abs/2601.05385
- [4] Debangshu Banerjee, Tarun Suresh, Shubham Ugare, Sasa Misailovic, and Gagandeep Singh. 2025. CRANE: Reasoning with constrained LLM generation. In Forty-second International Conference on Machine Learning. https://openreview. net/forum?id=wKs9fHYxCV
- [5] Victor Barres, Honghua Dong, Soham Ray, Xujie Si, and Karthik Narasimhan. 2025. 𝜏2-Bench: Evaluating Conversational Agents in a Dual-Control Environment. arXiv:2506.07982 [cs.AI] https://arxiv.org/abs/2506.07982
- [6] Luca Beurer-Kellner, Marc Fischer, and Martin Vechev. 2023. Prompting Is Programming: A Query Language for Large Language Models. Proc. ACM Program. Lang. 7, PLDI, Article 186 (June 2023), 24 pages. doi:10.1145/3591300
- [7] Iwo Błądek and Krzysztof Krawiec. 2019. Solving symbolic regression problems with formal constraints. In Proceedings of the Genetic and Evolutionary Computation Conference (Prague, Czech Republic) (GECCO ’19). Association for Computing Machinery, New York, NY, USA, 977–984. doi:10.1145/3321707.3321743
- [8] Miles Cranmer. 2023. Interpretable Machine Learning for Science with PySR and SymbolicRegression.jl. arXiv:2305.01582 [astro-ph.IM] https://arxiv.org/abs/2305.01582
- [9] Dafny Language Community. 2023. Integrating Dafny and Python Code. https://dafny.org/v3.10.0/DafnyRef/ integration-py/IntegrationPython. Accessed: 2026-03-17.
- [10] Kevin Ellis, Catherine Wong, Maxwell Nye, Mathias Sablé-Meyer, Lucas Morales, Luke Hewitt, Luc Cary, Armando Solar-Lezama, and Joshua B. Tenenbaum. 2021. DreamCoder: bootstrapping inductive program synthesis with wakesleep library learning. In Proceedings of the 42nd ACM SIGPLAN International Conference on Programming Language Design and Implementation (Virtual, Canada) (PLDI 2021). Association for Computing Machinery, New York, NY, USA, 835–850. doi:10.1145/3453483.3454080
- [11] Tianqing Fang, Hongming Zhang, Zhisong Zhang, Kaixin Ma, Wenhao Yu, Haitao Mi, and Dong Yu. 2025. WebEvolver: Enhancing Web Agent Self-Improvement with Coevolving World Model. arXiv preprint arXiv:2504.21024 (2025).
- [12] Yu Feng, Ruben Martins, Jacob Van Geffen, Isil Dillig, and Swarat Chaudhuri. 2017. Component-based synthesis of table consolidation and transformation tasks from examples. In Proceedings of the 38th ACM SIGPLAN Conference on Programming Language Design and Implementation (Barcelona, Spain) (PLDI 2017). Association for Computing Machinery, New York, NY, USA, 422–436. doi:10.1145/3062341.3062351
- [13] Hongcheng Gao, Yue Liu, Yufei He, Longxu Dou, Chao Du, Zhijie Deng, Bryan Hooi, Min Lin, and Tianyu Pang. 2025. FlowReasoner: Reinforcing Query-Level Meta-Agents. arXiv:2504.15257 [cs.AI] https://arxiv.org/abs/2504.15257
- [14] The Guardian. 2026. Rogue AI agents published passwords and bypassed security protections. News investigation.
- [15] Chengquan Guo, Xun Liu, Chulin Xie, Andy Zhou, Yi Zeng, Zinan Lin, Dawn Song, and Bo Li. 2024. RedCode: Risky Code Execution and Generation Benchmark for Code Agents. In The Thirty-eight Conference on Neural Information Processing Systems Datasets and Benchmarks Track. https://openreview.net/forum?id=mAG68wdggA
- [16] Sankha Narayan Guria, Jeffrey S. Foster, and David Van Horn. 2023. Absynthe: Abstract Interpretation-Guided Synthesis. Proc. ACM Program. Lang. 7, PLDI, Article 171 (June 2023), 24 pages. doi:10.1145/3591285
- [17] Christian Haider and Gabriel Kronberger. 2022. Shape-Constrained Symbolic Regression with NSGA-III. In Computer Aided Systems Theory – EUROCAST 2022: 18th International Conference, Las Palmas de Gran Canaria, Spain, February 20–25, 2022, Revised Selected Papers (Las Palmas de Gran Canaria, Spain). Springer-Verlag, Berlin, Heidelberg, 164–172. doi:10.1007/978-3-031-25312-6_19
- [18] Edward J Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Liang Wang, Weizhu Chen, et al. 2022. Lora: Low-rank adaptation of large language models. Iclr 1, 2 (2022), 3.
- [19] Shengran Hu, Cong Lu, and Jeff Clune. 2025. Automated Design of Agentic Systems. In The Thirteenth International Conference on Learning Representations. https://openreview.net/forum?id=t9U3LW7JVX
- [20] Adharsh Kamath, Sishen Zhang, Calvin Xu, Shubham Ugare, Gagandeep Singh, and Sasa Misailovic. 2025. Enforcing Temporal Constraints for LLM Agents. arXiv:2512.23738 [cs.PL] https://arxiv.org/abs/2512.23738
- [21] Omar Khattab, Arnav Singhvi, Paridhi Maheshwari, Zhiyuan Zhang, Keshav Santhanam, Sri Vardhamanan A, Saiful Haq, Ashutosh Sharma, Thomas T. Joshi, Hanna Moazam, Heather Miller, Matei Zaharia, and Christopher Potts.

2024. DSPy: Compiling Declarative Language Model Calls into State-of-the-Art Pipelines. In The Twelfth International Conference on Learning Representations. https://openreview.net/forum?id=sY5N0zY5Od

- [22] Jinwoo Kim, Qinheping Hu, Loris D’Antoni, and Thomas Reps. 2021. Semantics-guided synthesis. Proc. ACM Program. Lang. 5, POPL, Article 30 (Jan. 2021), 32 pages. doi:10.1145/3434311


- [23] Tristan Knoth, Di Wang, Nadia Polikarpova, and Jan Hoffmann. 2019. Resource-guided program synthesis. In Proceedings of the 40th ACM SIGPLAN Conference on Programming Language Design and Implementation (Phoenix, AZ, USA) (PLDI 2019). Association for Computing Machinery, New York, NY, USA, 253–268. doi:10.1145/3314221.3314602
- [24] G. Kronberger, F. O. de Franca, B. Burlacu, C. Haider, and M. Kommenda. 2022. Shape-Constrained Symbolic Regression—Improving Extrapolation with Prior Knowledge. Evolutionary Computation 30, 1 (03 2022), 75–98. arXiv:https://direct.mit.edu/evco/article-pdf/30/1/75/1995582/evco_a_00294.pdf doi:10.1162/evco_a_00294
- [25] Eunkyu Lee, Donghyeon Kim, Wonyoung Kim, and Insu Yun. 2025. Takedown: How It’s Done in Modern Coding Agent Exploits. arXiv:2509.24240 [cs.CR] https://arxiv.org/abs/2509.24240
- [26] K. Rustan M. Leino. 2010. Dafny: an automatic program verifier for functional correctness. In Proceedings of the 16th International Conference on Logic for Programming, Artificial Intelligence, and Reasoning (Dakar, Senegal) (LPAR’10). Springer-Verlag, Berlin, Heidelberg, 348–370.
- [27] Li Li, Minjie Fan, Rishabh Singh, and Patrick Riley. 2019. Neural-Guided Symbolic Regression with Asymptotic Constraints. arXiv:1901.07714 [cs.LG] https://arxiv.org/abs/1901.07714
- [28] Wenqiang Li, Weijun Li, Linjun Sun, Min Wu, Lina Yu, Jingyi Liu, Yanjie Li, and Songsong Tian. 2023. Transformerbased model for symbolic regression via joint supervised learning. In The Eleventh International Conference on Learning Representations. https://openreview.net/forum?id=ULzyv9M1j5
- [29] Chloe R Loughridge, Qinyi Sun, Seth Ahrenbach, Federico Cassano, Chuyue Sun, Ying Sheng, Anish Mudide, Md Rakib Hossain Misu, Nada Amin, and Max Tegmark. 2025. DafnyBench: A Benchmark for Formal Software Verification. Transactions on Machine Learning Research (2025). https://openreview.net/forum?id=yBgTVWccIx
- [30] Iman Mirzadeh, Keivan Alizadeh, Hooman Shahrokhi, Oncel Tuzel, Samy Bengio, and Mehrdad Farajtabar. 2024. Gsm-symbolic: Understanding the limitations of mathematical reasoning in large language models. arXiv preprint arXiv:2410.05229 (2024).
- [31] Eric Mugnier, Emmanuel Anaya Gonzalez, Nadia Polikarpova, Ranjit Jhala, and Zhou Yuanyuan. 2025. Laurel: Unblocking Automated Verification with Large Language Models. Proc. ACM Program. Lang. 9, OOPSLA1, Article 134 (April 2025), 27 pages. doi:10.1145/3720499
- [32] Niels Mündler, Jingxuan He, Hao Wang, Koushik Sen, Dawn Song, and Martin Vechev. 2025. Type-Constrained Code Generation with Language Models. Proc. ACM Program. Lang. 9, PLDI, Article 171 (June 2025), 26 pages. doi:10.1145/3729274
- [33] Shaan Nagy, Timothy Zhou, Nadia Polikarpova, and Loris D’Antoni. 2026. ChopChop: A Programmable Framework for Semantically Constraining the Output of Language Models. Proc. ACM Program. Lang. 10, POPL, Article 66 (Jan. 2026), 28 pages. doi:10.1145/3776708
- [34] Emilio Parisotto, Abdel rahman Mohamed, Rishabh Singh, Lihong Li, Dengyong Zhou, and Pushmeet Kohli. 2016. Neuro-Symbolic Program Synthesis. arXiv:1611.01855 [cs.AI] https://arxiv.org/abs/1611.01855
- [35] Kanghee Park, Jiayu Wang, Taylor Berg-Kirkpatrick, Nadia Polikarpova, and Loris D’Antoni. 2024. Grammar-Aligned Decoding. In The Thirty-eighth Annual Conference on Neural Information Processing Systems. https://openreview.net/ forum?id=5G7ve8E1Lu
- [36] Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, Y. K. Li, Y. Wu, and Daya Guo. 2024. DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models. arXiv:2402.03300 [cs.CL] https://arxiv.org/abs/2402.03300
- [37] Parshin Shojaee, Kazem Meidani, Shashank Gupta, Amir Barati Farimani, and Chandan K. Reddy. 2025. LLM-SR: Scientific Equation Discovery via Programming with Large Language Models. In The Thirteenth International Conference on Learning Representations. https://openreview.net/forum?id=m2nmp8P5in
- [38] Armando Solar-Lezama. 2013. Program Sketching. International Journal on Software Tools for Technology Transfer 15, 5

(2013), 475–495. doi:10.1007/s10009-012-0249-7

- [39] Chuyue Sun, Ying Sheng, Oded Padon, and Clark Barrett. 2024. Clover: Closed-Loop Verifiable Code Generation. In AI Verification: First International Symposium, SAIV 2024, Montreal, QC, Canada, July 22–23, 2024, Proceedings (Montreal, QC, Canada). Springer-Verlag, Berlin, Heidelberg, 134–155. doi:10.1007/978-3-031-65112-0_7
- [40] Tarun Suresh, Debangshu Banerjee, Shubham Ugare, Sasa Misailovic, and Gagandeep Singh. 2025. DINGO: Constrained Inference for Diffusion LLMs. In The Thirty-ninth Annual Conference on Neural Information Processing Systems. https: //openreview.net/forum?id=KaYMGsnZ4R
- [41] Dídac Surís, Sachit Menon, and Carl Vondrick. 2023. ViperGPT: Visual Inference via Python Execution for Reasoning. In 2023 IEEE/CVF International Conference on Computer Vision (ICCV). 11854–11864. doi:10.1109/ICCV51070.2023.01092
- [42] Qwen Team. 2025. Qwen3 Technical Report. arXiv:2505.09388 [cs.CL] https://arxiv.org/abs/2505.09388
- [43] Wanxin Tian, Shijie Zhang, Kevin Zhang, Xiaowei Chi, Chunkai Fan, Junyu Lu, Yulin Luo, Qiang Zhou, Yiming Zhao, Ning Liu, Siyu Lin, Zhiyuan Qin, Xiaozhu Ju, Shanghang Zhang, and Jian Tang. 2025. SEEA-R1: Tree-Structured Reinforcement Fine-Tuning for Self-Evolving Embodied Agents. arXiv:2506.21669 [cs.AI] https://arxiv.org/abs/2506. 21669


- [44] Shubham Ugare, Rohan Gumaste, Tarun Suresh, Gagandeep Singh, and Sasa Misailovic. 2025. IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking. In The Thirteenth International Conference on Learning Representations. https://openreview.net/forum?id=ac93gRzxxV
- [45] Shubham Ugare, Tarun Suresh, Hangoo Kang, Sasa Misailovic, and Gagandeep Singh. 2025. SynCode: LLM Generation with Grammar Augmentation. Transactions on Machine Learning Research (2025). https://openreview.net/forum?id= HiUZtgAPoH
- [46] Lazar Valkov, Dipak Chaudhari, Akash Srivastava, Charles Sutton, and Swarat Chaudhuri. 2018. HOUDINI: lifelong learning as program synthesis. In Proceedings of the 32nd International Conference on Neural Information Processing Systems (Montréal, Canada) (NIPS’18). Curran Associates Inc., Red Hook, NY, USA, 8701–8712.
- [47] Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, and Anima Anandkumar.

2023. Voyager: An Open-Ended Embodied Agent with Large Language Models. arXiv:2305.16291 [cs.AI] https: //arxiv.org/abs/2305.16291

- [48] Jiongxiao Wang, Qiaojing Yan, Yawei Wang, Yijun Tian, Soumya Smruti Mishra, Zhichao Xu, Megha Gandhi, Panpan Xu, and Lin Lee Cheong. 2026. Reinforcement Learning for Self-Improving Agent with Skill Library. arXiv:2512.17102 [cs.AI] https://arxiv.org/abs/2512.17102
- [49] Xingyao Wang, Yangyi Chen, Lifan Yuan, Yizhe Zhang, Yunzhu Li, Hao Peng, and Heng Ji. 2024. Executable code actions elicit better LLM agents. In Proceedings of the 41st International Conference on Machine Learning (Vienna, Austria) (ICML’24). JMLR.org, Article 2054, 25 pages.
- [50] Ziqian Zhong, Aditi Raghunathan, and Nicholas Carlini. 2025. ImpossibleBench: Measuring LLMs’ Propensity of Exploiting Test Cases. arXiv preprint arXiv:2510.20270 (2025).
- [51] Wangchunshu Zhou, Yixin Ou, Shengwei Ding, Long Li, Jialong Wu, Tiannan Wang, Jiamin Chen, Shuai Wang, Xiaohua Xu, Ningyu Zhang, Huajun Chen, and Yuchen Eleanor Jiang. 2024. Symbolic Learning Enables Self-Evolving Agents. arXiv:2406.18532 [cs.CL] https://arxiv.org/abs/2406.18532
- [52] He Zhu, Zikang Xiong, Stephen Magill, and Suresh Jagannathan. 2019. An inductive synthesis framework for verifiable reinforcement learning. In Proceedings of the 40th ACM SIGPLAN Conference on Programming Language Design and Implementation (Phoenix, AZ, USA) (PLDI 2019). Association for Computing Machinery, New York, NY, USA, 686–701. doi:10.1145/3314221.3314638
- [53] Mingchen Zhuge, Wenyi Wang, Louis Kirsch, Francesco Faccio, Dmitrii Khizbullin, and Jürgen Schmidhuber. 2024. GPTSwarm: Language Agents as Optimizable Graphs. In Forty-first International Conference on Machine Learning. https://openreview.net/forum?id=uTC9AFXIhg


#### A Restricted Dafny Grammar

⟨𝑝𝑟𝑜𝑔𝑟𝑎𝑚⟩ ::= ⟨𝑚𝑒𝑡ℎ𝑜𝑑_𝑑𝑒𝑐𝑙⟩ | ⟨𝑓𝑢𝑛𝑐𝑡𝑖𝑜𝑛_𝑑𝑒𝑐𝑙⟩ ⟨𝑚𝑒𝑡ℎ𝑜𝑑_𝑑𝑒𝑐𝑙⟩ ::= method ⟨𝑖𝑑𝑒𝑛𝑡⟩(⟨𝑝𝑎𝑟𝑎𝑚𝑠⟩) ⟨𝑠𝑝𝑒𝑐𝑠⟩ {⟨𝑠𝑡𝑚𝑡_𝑙𝑖𝑠𝑡⟩} ⟨𝑓𝑢𝑛𝑐𝑡𝑖𝑜𝑛_𝑑𝑒𝑐𝑙⟩ ::= function ⟨𝑖𝑑𝑒𝑛𝑡⟩(⟨𝑝𝑎𝑟𝑎𝑚𝑠⟩) : ⟨𝑡𝑦𝑝𝑒⟩ ⟨𝑠𝑝𝑒𝑐𝑠⟩ ⟨𝑒𝑥𝑝𝑟⟩ ⟨𝑝𝑎𝑟𝑎𝑚𝑠⟩ ::= 𝜖 | ⟨𝑝𝑎𝑟𝑎𝑚⟩ | ⟨𝑝𝑎𝑟𝑎𝑚⟩, ⟨𝑝𝑎𝑟𝑎𝑚𝑠⟩ ⟨𝑝𝑎𝑟𝑎𝑚⟩ ::= ⟨𝑖𝑑𝑒𝑛𝑡⟩ : ⟨𝑡𝑦𝑝𝑒⟩

⟨𝑡𝑦𝑝𝑒⟩ ::= int | bool | string | real ⟨𝑠𝑝𝑒𝑐𝑠⟩ ::= 𝜖 | ⟨𝑠𝑝𝑒𝑐⟩⟨𝑠𝑝𝑒𝑐𝑠⟩

⟨𝑠𝑝𝑒𝑐⟩ ::= requires ⟨𝑓𝑜𝑟𝑚𝑢𝑙𝑎⟩ | ensures ⟨𝑓𝑜𝑟𝑚𝑢𝑙𝑎⟩ ⟨𝑠𝑡𝑚𝑡_𝑙𝑖𝑠𝑡⟩ ::= 𝜖 | ⟨𝑠𝑡𝑚𝑡⟩⟨𝑠𝑡𝑚𝑡_𝑙𝑖𝑠𝑡⟩

⟨𝑠𝑡𝑚𝑡⟩ ::= ⟨𝑎𝑠𝑠𝑖𝑔𝑛_𝑠𝑡𝑚𝑡⟩ | ⟨𝑖𝑓 _𝑠𝑡𝑚𝑡⟩ | ⟨𝑤ℎ𝑖𝑙𝑒_𝑠𝑡𝑚𝑡⟩ | ⟨𝑎𝑠𝑠𝑒𝑟𝑡_𝑠𝑡𝑚𝑡⟩ | ⟨𝑐𝑎𝑙𝑙_𝑠𝑡𝑚𝑡⟩ ⟨𝑎𝑠𝑠𝑖𝑔𝑛_𝑠𝑡𝑚𝑡⟩ ::= ⟨𝑖𝑑𝑒𝑛𝑡⟩ := ⟨𝑒𝑥𝑝𝑟⟩;

⟨𝑐𝑎𝑙𝑙_𝑠𝑡𝑚𝑡⟩ ::= ⟨𝑖𝑑𝑒𝑛𝑡⟩(⟨𝑎𝑟𝑔𝑠⟩);

⟨𝑎𝑟𝑔𝑠⟩ ::= 𝜖 | ⟨𝑒𝑥𝑝𝑟⟩ | ⟨𝑒𝑥𝑝𝑟⟩, ⟨𝑎𝑟𝑔𝑠⟩ ⟨𝑖𝑓 _𝑠𝑡𝑚𝑡⟩ ::= if (⟨𝑓𝑜𝑟𝑚𝑢𝑙𝑎⟩){⟨𝑠𝑡𝑚𝑡_𝑙𝑖𝑠𝑡⟩}

| if (⟨𝑓𝑜𝑟𝑚𝑢𝑙𝑎⟩){⟨𝑠𝑡𝑚𝑡_𝑙𝑖𝑠𝑡⟩} else {⟨𝑠𝑡𝑚𝑡_𝑙𝑖𝑠𝑡⟩} ⟨𝑤ℎ𝑖𝑙𝑒_𝑠𝑡𝑚𝑡⟩ ::= while (⟨𝑓𝑜𝑟𝑚𝑢𝑙𝑎⟩) ⟨𝑙𝑜𝑜𝑝_𝑎𝑛𝑛𝑜𝑡𝑠⟩ {⟨𝑠𝑡𝑚𝑡_𝑙𝑖𝑠𝑡⟩}

⟨𝑙𝑜𝑜𝑝_𝑎𝑛𝑛𝑜𝑡𝑠⟩ ::= 𝜖 | ⟨𝑙𝑜𝑜𝑝_𝑎𝑛𝑛𝑜𝑡⟩⟨𝑙𝑜𝑜𝑝_𝑎𝑛𝑛𝑜𝑡𝑠⟩ ⟨𝑙𝑜𝑜𝑝_𝑎𝑛𝑛𝑜𝑡⟩ ::= invariant ⟨𝑓𝑜𝑟𝑚𝑢𝑙𝑎⟩ | decreases ⟨𝑒𝑥𝑝𝑟⟩ ⟨𝑎𝑠𝑠𝑒𝑟𝑡_𝑠𝑡𝑚𝑡⟩ ::= assert ⟨𝑓𝑜𝑟𝑚𝑢𝑙𝑎⟩;

⟨𝑒𝑥𝑝𝑟⟩ ::= ⟨𝑎𝑒𝑥𝑝𝑟⟩ | ⟨𝑠𝑒𝑥𝑝𝑟⟩ ⟨𝑎𝑒𝑥𝑝𝑟⟩ ::= ⟨𝑖𝑛𝑡_𝑙𝑖𝑡⟩ | ⟨𝑖𝑑𝑒𝑛𝑡⟩ | ⟨𝑎𝑒𝑥𝑝𝑟⟩ ⟨𝑎𝑟𝑖𝑡ℎ_𝑜𝑝⟩ ⟨𝑎𝑒𝑥𝑝𝑟⟩ | (⟨𝑎𝑒𝑥𝑝𝑟⟩) | ⟨𝑖𝑑𝑒𝑛𝑡⟩(⟨𝑎𝑟𝑔𝑠⟩) ⟨𝑠𝑒𝑥𝑝𝑟⟩ ::= ⟨𝑠𝑡𝑟𝑖𝑛𝑔_𝑙𝑖𝑡⟩ | ⟨𝑖𝑑𝑒𝑛𝑡⟩ | (⟨𝑠𝑒𝑥𝑝𝑟⟩) | ⟨𝑖𝑑𝑒𝑛𝑡⟩(⟨𝑎𝑟𝑔𝑠⟩)

⟨𝑓𝑜𝑟𝑚𝑢𝑙𝑎⟩ ::= ⟨𝑒𝑥𝑝𝑟⟩ ⟨𝑟𝑒𝑙_𝑜𝑝⟩ ⟨𝑒𝑥𝑝𝑟⟩ | ! ⟨𝑓𝑜𝑟𝑚𝑢𝑙𝑎⟩ | (⟨𝑓𝑜𝑟𝑚𝑢𝑙𝑎⟩) | ⟨𝑖𝑑𝑒𝑛𝑡⟩(⟨𝑎𝑟𝑔𝑠⟩) | forall ⟨𝑏𝑜𝑢𝑛𝑑_𝑣𝑎𝑟𝑠⟩ :: ⟨𝑓𝑜𝑟𝑚𝑢𝑙𝑎⟩ | exists ⟨𝑏𝑜𝑢𝑛𝑑_𝑣𝑎𝑟𝑠⟩ :: ⟨𝑓𝑜𝑟𝑚𝑢𝑙𝑎⟩

⟨𝑏𝑜𝑢𝑛𝑑_𝑣𝑎𝑟𝑠⟩ ::= ⟨𝑖𝑑𝑒𝑛𝑡⟩ : ⟨𝑡𝑦𝑝𝑒⟩ | ⟨𝑖𝑑𝑒𝑛𝑡⟩ : ⟨𝑡𝑦𝑝𝑒⟩, ⟨𝑏𝑜𝑢𝑛𝑑_𝑣𝑎𝑟𝑠⟩

⟨𝑎𝑟𝑖𝑡ℎ_𝑜𝑝⟩ ::= + | − | ∗ | / ⟨𝑟𝑒𝑙_𝑜𝑝⟩ ::= =|≠|<|>|≤|≥ ⟨𝑙𝑖𝑡𝑒𝑟𝑎𝑙⟩ ::= ⟨𝑖𝑛𝑡_𝑙𝑖𝑡⟩ | ⟨𝑠𝑡𝑟𝑖𝑛𝑔_𝑙𝑖𝑡⟩ | true | false ⟨𝑖𝑛𝑡_𝑙𝑖𝑡⟩ ::= 0 | 1 | · · · | 9 (and sequences thereof)

⟨𝑠𝑡𝑟𝑖𝑛𝑔_𝑙𝑖𝑡⟩ ::= ”⟨𝑐ℎ𝑎𝑟⟩∗” ⟨𝑖𝑑𝑒𝑛𝑡⟩ ::= ⟨𝑙𝑒𝑡𝑡𝑒𝑟⟩ | ⟨𝑙𝑒𝑡𝑡𝑒𝑟⟩⟨𝑖𝑑𝑒𝑛𝑡⟩ ⟨𝑙𝑒𝑡𝑡𝑒𝑟⟩ ::= 𝑎 | 𝑏 | · · · | 𝑧 | 𝐴 | 𝐵 | · · · | 𝑍 ⟨𝑑𝑖𝑔𝑖𝑡⟩ ::= 0 | 1 | · · · | 9

#### B Rejection Sampling Details

Rejection Sampling Details. Given a target distribution 𝜋𝑡 and a proposal distribution 𝜋𝑝 with 𝑆(𝜋𝑡) ⊆ 𝑆(𝜋𝑝), assume there exists 𝑀 ≥ 1 such that ∀𝑧 ∈ Ω, 𝐷𝜋𝑡 (𝑧) ≤ 𝑀 ·𝐷𝜋𝑝 (𝑧). The procedure samples 𝑧 ∼ 𝜋𝑝 and 𝑢 ∼ Uniform(0, 1), and accepts 𝑧 iff 𝑢 ≤ 𝑀𝐷·𝐷𝜋𝑡 (𝑧)

𝜋𝑝 (𝑧) . Otherwise, the sample is rejected and the process repeats. Accepted samples follow 𝜋𝑡. Moreover, any 𝑧 ∉ 𝑆(𝜋𝑡) is always rejected since 𝐷𝜋𝑡 (𝑧) = 0, ensuring all accepted samples lie in 𝑆(𝜋𝑡). The acceptance probability is 1/𝑀, so efficiency depends on how tightly 𝜋𝑝 upper-bounds 𝜋𝑡. For this paper, we assume 𝑀 = 1.

#### C Library Functions for Symbolic RegressionLibrary Function Set F.

- • 𝑎𝑏𝑠(𝑥 : 𝑟𝑒𝑎𝑙) → 𝑟 : 𝑟𝑒𝑎𝑙 ensures 𝑟 ≥ 0 ensures 𝑟 = 𝑥 ∨ 𝑟 = −𝑥
- • 𝑚𝑎𝑥(𝑥 : 𝑟𝑒𝑎𝑙,𝑦 : 𝑟𝑒𝑎𝑙) → 𝑟 : 𝑟𝑒𝑎𝑙 ensures (𝑥 ≤ 𝑟) ∧ (𝑦 ≤ 𝑟) ensures (𝑟 = 𝑥) ∨ (𝑟 = 𝑦)
- • 𝑚𝑖𝑛(𝑥 : 𝑟𝑒𝑎𝑙,𝑦 : 𝑟𝑒𝑎𝑙) → 𝑟 : 𝑟𝑒𝑎𝑙 ensures (𝑥 ≥ 𝑟) ∧ (𝑦 ≥ 𝑟) ensures (𝑟 = 𝑥) ∨ (𝑟 = 𝑦)
- • 𝑠𝑖𝑛(𝑥 : 𝑟𝑒𝑎𝑙) → 𝑟 : 𝑟𝑒𝑎𝑙 ensures −1 ≤ 𝑟 ≤ 1 ensures (𝑥 = 0) ⇒ (𝑟 = 0)
- • 𝑐𝑜𝑠(𝑥 : 𝑟𝑒𝑎𝑙) → 𝑟 : 𝑟𝑒𝑎𝑙 ensures −1 ≤ 𝑟 ≤ 1 ensures (𝑥 = 0) ⇒ (𝑟 = 1)
- • 𝑝𝑖(𝑥 : 𝑟𝑒𝑎𝑙) → 𝑟 : 𝑟𝑒𝑎𝑙 requires 𝑥 ≥ 0 ensures 3.141592653589790 · 𝑥 ≤ 𝑟 ensures 𝑟 ≤ 3.141592653589793 · 𝑥
- • 𝑝𝑜𝑤(𝑥 : 𝑟𝑒𝑎𝑙,𝑑 : 𝑟𝑒𝑎𝑙) → 𝑟 : 𝑟𝑒𝑎𝑙 requires 𝑥 ≥ 0 requires (𝑥 ≠ 0) ∨ (𝑑 ≥ 0) ensures 𝑟 ≥ 0 ensures (𝑥 > 0) ⇒ (𝑟 > 0) ensures (𝑑 = 0) ⇒ (𝑟 = 1) ensures (𝑥 ≥ 1 ∧ 𝑑 ≥ 0) ⇒ (𝑟 ≥ 1) ensures (𝑥 ≥ 1 ∧ 𝑑 ≤ 0) ⇒ (𝑟 ≤ 1) ensures (𝑥 ≤ 1 ∧ 𝑑 ≥ 0) ⇒ (𝑟 ≤ 1) ensures (𝑥 ≤ 1 ∧ 𝑑 ≤ 0) ⇒ (𝑟 ≥ 1)
- • 𝑠𝑞𝑟𝑡(𝑥 : 𝑟𝑒𝑎𝑙) → 𝑟 : 𝑟𝑒𝑎𝑙 requires 𝑥 ≥ 0 ensures 𝑟 ≥ 0 ensures 𝑟 · 𝑟 = 𝑥
- • 𝑒𝑥𝑝(𝑥 : 𝑟𝑒𝑎𝑙) → 𝑟 : 𝑟𝑒𝑎𝑙 ensures 𝑟 ≥ 0 ensures (𝑥 ≤ 0) ⇒ (𝑟 ≤ 1) ensures (𝑥 ≥ 0) ⇒ (𝑟 ≥ 1) ensures (𝑥 = 1) ⇒ (2.71 ≤ 𝑟 ≤ 2.72) ensures 𝑟 ≥ (1 + 𝑥)
- • 𝑙𝑜𝑔(𝑥 : 𝑟𝑒𝑎𝑙) → 𝑟 : 𝑟𝑒𝑎𝑙 requires 𝑥 > 0 ensures (𝑥 ≥ 1) ⇒ (𝑟 ≥ 0) ensures (𝑥 ≤ 1) ⇒ (𝑟 ≤ 0) ensures (𝑥 = 1) ⇒ (𝑟 = 0)
- • 𝑛𝑒𝑢𝑟𝑎𝑙1(𝑥 : 𝑟𝑒𝑎𝑙) → 𝑟 : 𝑟𝑒𝑎𝑙
- • 𝑛𝑒𝑢𝑟𝑎𝑙2(𝑥1 : 𝑟𝑒𝑎𝑙,𝑥2 : 𝑟𝑒𝑎𝑙) → 𝑟 : 𝑟𝑒𝑎𝑙
- • 𝑛𝑒𝑢𝑟𝑎𝑙3(𝑥1 : 𝑟𝑒𝑎𝑙,𝑥2 : 𝑟𝑒𝑎𝑙,𝑥3 : 𝑟𝑒𝑎𝑙) → 𝑟 : 𝑟𝑒𝑎𝑙


#### D Additional Axioms for Symbolic RegressionD.1 Axiom Syntax

⟨axiom⟩ ::= ⟨𝑓𝑜𝑟𝑚𝑢𝑙𝑎⟩ Axiom Set A.

• Interval Multiplication Rule: ∀𝑥,𝑦,𝑥𝑙𝑏,𝑥𝑢𝑏,𝑦𝑙𝑏,𝑦𝑢𝑏 ∈ R. (𝑥𝑙𝑏 ≤ 𝑥 ≤ 𝑥𝑢𝑏) ∧ (𝑦𝑙𝑏 ≤ 𝑦 ≤

𝑦𝑢𝑏) =⇒ 𝑚𝑖𝑛(𝑥𝑙𝑏 ×𝑦𝑙𝑏, 𝑥𝑙𝑏 ×𝑦𝑢𝑏, 𝑥𝑢𝑏 ×𝑦𝑙𝑏, 𝑥𝑢𝑏 ×𝑦𝑢𝑏) ≤ 𝑥 ×𝑦 ≤ 𝑚𝑎𝑥(𝑥𝑙𝑏 ×𝑦𝑙𝑏, 𝑥𝑙𝑏 ×𝑦𝑢𝑏, 𝑥𝑢𝑏 ×𝑦𝑙𝑏, 𝑥𝑢𝑏 ×𝑦𝑢𝑏).

- • ∀𝑥,𝑑1,𝑑2 ∈ R. (0 ≤ 𝑥 ≤ 1) ∧ (𝑑1 ≤ 𝑑2) =⇒ 𝑝𝑜𝑤(𝑥,𝑑1) ≥ 𝑝𝑜𝑤(𝑥,𝑑2).
- • ∀𝑥,𝑑1,𝑑2 ∈ R. (𝑥 ≥ 1) ∧ (𝑑1 ≤ 𝑑2) =⇒ 𝑝𝑜𝑤(𝑥,𝑑1) ≤ 𝑝𝑜𝑤(𝑥,𝑑2).
- • ∀𝑥 ∈ R. 𝑒𝑥𝑝(𝑥) = 𝑝𝑜𝑤(𝑒𝑥𝑝(1), 𝑥).
- • ∀𝑥 ∈ R. (𝑥 > 0) =⇒ ∀𝑟 ∈ R. 𝑟 = 𝑙𝑜𝑔(𝑥) ⇐⇒ 𝑒𝑥𝑝(𝑟) = 𝑥 .
- • ∀𝑥 ∈ R. (𝑥 ≥ 0) =⇒ (𝑠𝑞𝑟𝑡(𝑥) = 𝑝𝑜𝑤(𝑥, 0.5)).


#### E Library Functions for Dafny Program VerificationLibrary Function Set F.

- • 𝑐𝑙𝑎𝑢𝑑𝑒(𝑝𝑟𝑜𝑚𝑝𝑡 : 𝑠𝑡𝑟) → 𝑟 : 𝑠𝑡𝑟
- • 𝑛𝑜𝐷𝑖𝑓 𝑓 (𝑏𝑎𝑠𝑒_𝑐𝑜𝑑𝑒 : 𝑠𝑡𝑟,𝑎𝑛𝑛𝑜𝑡𝑎𝑡𝑒𝑑_𝑐𝑜𝑑𝑒 : 𝑠𝑡𝑟) → 𝑟 : 𝑏𝑜𝑜𝑙
- • 𝑛𝑜𝐷𝑖𝑓 𝑓𝑊𝑖𝑡ℎ𝐸𝑟𝑟𝑜𝑟𝑀𝑠𝑔(𝑏𝑎𝑠𝑒_𝑐𝑜𝑑𝑒 : 𝑠𝑡𝑟,𝑎𝑛𝑛𝑜𝑡𝑎𝑡𝑒𝑑_𝑐𝑜𝑑𝑒 : 𝑠𝑡𝑟) → 𝑟 : 𝑠𝑡𝑟
- • 𝑑𝑎𝑓𝑛𝑦𝑉𝑒𝑟𝑖𝑓𝑖𝑒𝑟(𝑑𝑎𝑓𝑛𝑦_𝑐𝑜𝑑𝑒 : 𝑠𝑡𝑟) → 𝑟 : 𝑏𝑜𝑜𝑙
- • 𝑑𝑎𝑓𝑛𝑦𝑉𝑒𝑟𝑖𝑓𝑖𝑒𝑟𝑊𝑖𝑡ℎ𝐸𝑟𝑟𝑜𝑟𝑀𝑠𝑔(𝑑𝑎𝑓𝑛𝑦_𝑐𝑜𝑑𝑒 : 𝑠𝑡𝑟) → 𝑟 : 𝑠𝑡𝑟
- • 𝑒𝑥𝑡𝑟𝑎𝑐𝑡𝐷𝑎𝑓𝑛𝑦𝐶𝑜𝑑𝑒(𝑡𝑒𝑥𝑡 : 𝑠𝑡𝑟) → 𝑟 : 𝑠𝑡𝑟
- • 𝑖𝑠𝑆𝑢𝑏𝑠𝑡𝑟𝑖𝑛𝑔(𝑠𝑢𝑏 : 𝑠𝑡𝑟, 𝑓𝑢𝑙𝑙 : 𝑠𝑡𝑟) → 𝑟 : 𝑏𝑜𝑜𝑙


#### F Additional Axioms for Dafny Program VerificationAxiom Set A.

- • Reflexivity: ∀𝑎,𝑏 ∈ Σ∗. (𝑎 = 𝑏) =⇒ 𝑛𝑜𝐷𝑖𝑓 𝑓 (𝑎,𝑏).
- • Transitivity: ∀𝑎,𝑏,𝑐 ∈ Σ∗. 𝑛𝑜𝐷𝑖𝑓 𝑓 (𝑎,𝑏) ∧ 𝑛𝑜𝐷𝑖𝑓 𝑓 (𝑏,𝑐) =⇒ 𝑛𝑜𝐷𝑖𝑓 𝑓 (𝑎,𝑐).
- • ∀𝑎,𝑏 ∈ Σ∗. 𝑛𝑜𝐷𝑖𝑓 𝑓𝑊𝑖𝑡ℎ𝐸𝑟𝑟𝑜𝑟𝑀𝑠𝑔(𝑎,𝑏) = “” ⇐⇒ 𝑛𝑜𝐷𝑖𝑓 𝑓 (𝑎,𝑏).
- • ∀𝑐 ∈ Σ∗. 𝑑𝑎𝑓𝑛𝑦𝑉𝑒𝑟𝑖𝑓𝑖𝑒𝑟𝑊𝑖𝑡ℎ𝐸𝑟𝑟𝑜𝑟𝑀𝑠𝑔(𝑐) = “” ⇐⇒ 𝑑𝑎𝑓𝑛𝑦𝑉𝑒𝑟𝑖𝑓𝑖𝑒𝑟(𝑐).


#### G Library Functions for 𝜏2-benchLibrary Function Set F.

- • 𝑞𝑤𝑒𝑛(𝑝𝑟𝑜𝑚𝑝𝑡 : 𝑠𝑡𝑟) → 𝑟 : 𝑠𝑡𝑟
- • 𝑎𝑔𝑒𝑛𝑡𝐶𝐶ℎ𝑒𝑐𝑘(𝑡𝑜𝑜𝑙 : 𝑠𝑡𝑟,𝑡𝑟𝑎𝑐𝑒 : 𝑠𝑡𝑟,𝑑𝑜𝑚𝑎𝑖𝑛 : 𝑠𝑡𝑟) → 𝑟 : 𝑏𝑜𝑜𝑙
- • 𝑖𝑠𝑇𝑜𝑜𝑙𝐶𝑎𝑙𝑙(𝑟𝑒𝑠𝑝𝑜𝑛𝑠𝑒 : 𝑠𝑡𝑟) → 𝑟 : 𝑏𝑜𝑜𝑙
- • 𝑝𝑎𝑟𝑠𝑒𝑇𝑜𝑜𝑙𝐶𝑎𝑙𝑙𝑁𝑎𝑚𝑒(𝑟𝑒𝑠𝑝𝑜𝑛𝑠𝑒 : 𝑠𝑡𝑟) → 𝑟 : 𝑠𝑡𝑟


#### H Additional Axioms for 𝜏2-benchAxiom Set A.

- • Non-tool-call safety: ∀𝑟,𝑡,𝑑 ∈ Σ∗. ¬𝑖𝑠𝑇𝑜𝑜𝑙𝐶𝑎𝑙𝑙(𝑟) =⇒ 𝑎𝑔𝑒𝑛𝑡𝐶𝐶ℎ𝑒𝑐𝑘(𝑟,𝑡,𝑑).
- • Transfer-to-human satisfiability: ∀𝑟,𝑡,𝑑 ∈ Σ∗. 𝑖𝑠𝑇𝑜𝑜𝑙𝐶𝑎𝑙𝑙(𝑟) ∧𝑝𝑎𝑟𝑠𝑒𝑇𝑜𝑜𝑙𝐶𝑎𝑙𝑙𝑁𝑎𝑚𝑒(𝑟) = “transfer_to_human_agents” =⇒ 𝑎𝑔𝑒𝑛𝑡𝐶𝐶ℎ𝑒𝑐𝑘(𝑟,𝑡,𝑑).


#### I Library Functions for GSM-SymbolicLibrary Function Set F.

- • 𝑞𝑤𝑒𝑛(𝑝𝑟𝑜𝑚𝑝𝑡 : 𝑠𝑡𝑟) → 𝑟 : 𝑠𝑡𝑟
- • 𝑔𝑠𝑚𝑃𝑎𝑟𝑠𝑒𝑟(𝑒𝑥𝑝𝑟𝑒𝑠𝑠𝑖𝑜𝑛 : 𝑠𝑡𝑟) → 𝑟 : 𝑏𝑜𝑜𝑙
- • 𝑔𝑠𝑚𝑃𝑎𝑟𝑠𝑒𝑟𝑊𝑖𝑡ℎ𝐸𝑟𝑟𝑜𝑟𝑀𝑠𝑔(𝑒𝑥𝑝𝑟𝑒𝑠𝑠𝑖𝑜𝑛 : 𝑠𝑡𝑟) → 𝑟 : 𝑠𝑡𝑟
- • 𝑒𝑥𝑡𝑟𝑎𝑐𝑡𝐸𝑥𝑝𝑟𝑒𝑠𝑠𝑖𝑜𝑛(𝑡𝑒𝑥𝑡 : 𝑠𝑡𝑟) → 𝑟 : 𝑠𝑡𝑟


#### J Additional Axioms for GSM-SymbolicAxiom Set A.

- • 𝑔𝑠𝑚𝑃𝑎𝑟𝑠𝑒𝑟(“« »”).
- • ∀𝑒 ∈ Σ∗. 𝑔𝑠𝑚𝑃𝑎𝑟𝑠𝑒𝑟𝑊𝑖𝑡ℎ𝐸𝑟𝑟𝑜𝑟𝑀𝑠𝑔(𝑒) = “” ⇐⇒ 𝑔𝑠𝑚𝑃𝑎𝑟𝑠𝑒𝑟(𝑒).


#### K Example Agents for LLM Assisted Program Verification

The following is an example verified agent program for the Dafny program verification task. The agent defines and invokes three FGGMs—𝑖𝑛𝑖𝑡𝑖𝑎𝑙𝐹𝐺𝐺𝑀 (Fig. 4), 𝑑𝑖𝑓 𝑓 𝐸𝑟𝑟𝑜𝑟𝐹𝐺𝐺𝑀 (Fig. 5), and 𝑣𝑒𝑟𝑖𝑓𝑖𝑒𝑟𝐸𝑟𝑟𝑜𝑟𝐹𝐺𝐺𝑀 (Fig. 6)—each with local contract Ψ𝑙 : 𝑛𝑜𝐷𝑖𝑓 𝑓 (𝑏𝑎𝑠𝑒_𝑝𝑟𝑜𝑔𝑟𝑎𝑚, ·) and a fallback that returns the original program (justified by the reflexivity axiom). All three share 𝐺𝑀𝑖𝑑 := 𝑐𝑙𝑎𝑢𝑑𝑒 and differ only in the prompting function 𝑓𝑝: the first generates an initial annotation with context-specific guidance, the second repairs after a diff-checker failure, and the third repairs

###### after a verification failure with error-specific feedback. The agent program (Fig. 7) dispatches to the appropriate FGGM on each loop iteration.

𝑖𝑑 := 𝑖𝑛𝑖𝑡𝑖𝑎𝑙𝐹𝐺𝐺𝑀 𝐺𝑀𝑖𝑑 := 𝑐𝑙𝑎𝑢𝑑𝑒 𝑡𝑦𝑝𝑒𝑆𝑖𝑔 := (𝑏𝑎𝑠𝑒_𝑝𝑟𝑜𝑔𝑟𝑎𝑚 : 𝑠𝑡𝑟) → 𝑠𝑡𝑟

Φ𝑙 := true Ψ𝑙 := 𝑛𝑜𝐷𝑖𝑓 𝑓 (𝑏𝑎𝑠𝑒_𝑝𝑟𝑜𝑔𝑟𝑎𝑚, 𝑓 (𝑏𝑎𝑠𝑒_𝑝𝑟𝑜𝑔𝑟𝑎𝑚)) 𝑓𝑝 := function 𝑓𝑝 (𝑏𝑎𝑠𝑒_𝑝𝑟𝑜𝑔𝑟𝑎𝑚 : 𝑠𝑡𝑟) : (𝑠𝑡𝑟) {

var 𝑔 : 𝑠𝑡𝑟 :=

“You are an expert in Dafny verification. Given the following unannotated Dafny code, ”

+ “add appropriate loop invariants, assertions, and decreases clauses to make it verify.\n\n”

+ “IMPORTANT RULES:\n”

- + “1. Do NOT modify the method signatures, requires clauses, or ensures clauses\n”
- + “2. Only add invariants, assertions, and decreases clauses\n”
- + “3. Do NOT change the logic or control flow\n”
- + “4. Keep invariants MINIMAL - only what’s necessary for postconditions\n”
- + “5. Add decreases clauses for termination\n”;


if (𝑖𝑠𝑆𝑢𝑏𝑠𝑡𝑟𝑖𝑛𝑔(“lemma ”, 𝑏𝑎𝑠𝑒_𝑝𝑟𝑜𝑔𝑟𝑎𝑚)) {

𝑔 := 𝑔

+ “6. LEMMAS: If a lemma has a non-trivial postcondition, add explicit proof steps:\n”

+ “ - Use assertions to unfold function definitions\n”

+ “ - Add case analysis or pattern matching if needed\n”

+ “ - Call other lemmas to establish intermediate facts\n”

+ “ - Do NOT leave lemma bodies empty unless postcondition is trivial\n”; } if (𝑖𝑠𝑆𝑢𝑏𝑠𝑡𝑟𝑖𝑛𝑔(“<”, 𝑏𝑎𝑠𝑒_𝑝𝑟𝑜𝑔𝑟𝑎𝑚) ∧ 𝑖𝑠𝑆𝑢𝑏𝑠𝑡𝑟𝑖𝑛𝑔(“>”, 𝑏𝑎𝑠𝑒_𝑝𝑟𝑜𝑔𝑟𝑎𝑚)) {

𝑔 := 𝑔

+ “7. GENERICS: When calling generic functions/lemmas, propagate type constraints:\n”

+ “ - If a called function requires T(00), declare it in the caller too\n”

+ “ - Explicitly instantiate type parameters when needed\n”; }

if (𝑖𝑠𝑆𝑢𝑏𝑠𝑡𝑟𝑖𝑛𝑔(“set<”, 𝑏𝑎𝑠𝑒_𝑝𝑟𝑜𝑔𝑟𝑎𝑚) ∨ 𝑖𝑠𝑆𝑢𝑏𝑠𝑡𝑟𝑖𝑛𝑔(“set ”, 𝑏𝑎𝑠𝑒_𝑝𝑟𝑜𝑔𝑟𝑎𝑚)) {

𝑔 := 𝑔

+ “8. SETS: Use simple, direct assertions for set reasoning:\n”

+ “ - Assert set equality decompositions: A == B + (A - B)\n”

+ “ - Use cardinality constraints: |A| == |B| + |C|\n”

+ “ - Avoid complex witness variables or case analysis\n”

+ “ - Let Dafny’s built-in set theory automation work\n”; } if (𝑖𝑠𝑆𝑢𝑏𝑠𝑡𝑟𝑖𝑛𝑔(“multiset”, 𝑏𝑎𝑠𝑒_𝑝𝑟𝑜𝑔𝑟𝑎𝑚)) {

𝑔 := 𝑔

+ “9. MULTISETS: Match the structure of postconditions directly\n”

+ “ - Use simple decomposition assertions\n”

+ “ - Avoid unnecessary intermediate steps\n”; } return 𝑔 + “\nBase program:\n” + 𝑏𝑎𝑠𝑒_𝑝𝑟𝑜𝑔𝑟𝑎𝑚

+ “\n\nReturn ONLY the annotated Dafny code in a ```dafny code block.”; } 𝑓𝑑 := function 𝑓𝑑 (𝑏𝑎𝑠𝑒_𝑝𝑟𝑜𝑔𝑟𝑎𝑚 : 𝑠𝑡𝑟, 𝑦 : 𝑠𝑡𝑟) : (𝑠𝑡𝑟)

ensures 𝑛𝑜𝐷𝑖𝑓 𝑓 (𝑏𝑎𝑠𝑒_𝑝𝑟𝑜𝑔𝑟𝑎𝑚, 𝑓𝑑 (𝑏𝑎𝑠𝑒_𝑝𝑟𝑜𝑔𝑟𝑎𝑚, 𝑦)) {

return 𝑏𝑎𝑠𝑒_𝑝𝑟𝑜𝑔𝑟𝑎𝑚; }

- Fig. 4. FGGM definition for 𝑖𝑛𝑖𝑡𝑖𝑎𝑙𝐹𝐺𝐺𝑀. The prompting function builds context-specific guidance by checking for lemmas, generics, sets, and multisets in the base program. The fallback returns the original program, satisfying Ψ𝑙 by the reflexivity axiom.


𝑖𝑑 := 𝑑𝑖𝑓 𝑓 𝐸𝑟𝑟𝑜𝑟𝐹𝐺𝐺𝑀 𝐺𝑀𝑖𝑑 := 𝑐𝑙𝑎𝑢𝑑𝑒 𝑡𝑦𝑝𝑒𝑆𝑖𝑔 := (𝑏𝑎𝑠𝑒_𝑝𝑟𝑜𝑔𝑟𝑎𝑚 : 𝑠𝑡𝑟, 𝑑𝑖𝑓 𝑓 _𝑒𝑟𝑟𝑜𝑟 : 𝑠𝑡𝑟, 𝑝𝑟𝑒𝑣_𝑎𝑡𝑡𝑒𝑚𝑝𝑡 : 𝑠𝑡𝑟) → 𝑠𝑡𝑟

Φ𝑙 := true Ψ𝑙 := 𝑛𝑜𝐷𝑖𝑓 𝑓 (𝑏𝑎𝑠𝑒_𝑝𝑟𝑜𝑔𝑟𝑎𝑚, 𝑓 (𝑏𝑎𝑠𝑒_𝑝𝑟𝑜𝑔𝑟𝑎𝑚, 𝑑𝑖𝑓 𝑓 _𝑒𝑟𝑟𝑜𝑟, 𝑝𝑟𝑒𝑣_𝑎𝑡𝑡𝑒𝑚𝑝𝑡)) 𝑓𝑝 := function 𝑓𝑝 (𝑏𝑎𝑠𝑒_𝑝𝑟𝑜𝑔𝑟𝑎𝑚 : 𝑠𝑡𝑟, 𝑑𝑖𝑓 𝑓 _𝑒𝑟𝑟𝑜𝑟 : 𝑠𝑡𝑟, 𝑝𝑟𝑒𝑣_𝑎𝑡𝑡𝑒𝑚𝑝𝑡 : 𝑠𝑡𝑟) : (𝑠𝑡𝑟) {

return

“The previous Dafny annotation modified the base program logic incorrectly.\n\n”

+ “noDiff error:\n” + 𝑑𝑖𝑓 𝑓 _𝑒𝑟𝑟𝑜𝑟 + “\n\n”

+ “Base program:\n” +𝑏𝑎𝑠𝑒_𝑝𝑟𝑜𝑔𝑟𝑎𝑚 + “\n\n”

+ “Previous attempt:\n” + 𝑝𝑟𝑒𝑣_𝑎𝑡𝑡𝑒𝑚𝑝𝑡 + “\n\n”

+ “Please add annotations WITHOUT changing:\n”

+ “- Method signatures\n”

+ “- Requires/ensures clauses\n”

+ “- Program logic or control flow\n”

+ “Only add invariants, assertions, and decreases clauses.\n”

+ “Return ONLY the corrected Dafny code in a ```dafny code block.”; }

𝑓𝑑 := function 𝑓𝑑 (𝑏𝑎𝑠𝑒_𝑝𝑟𝑜𝑔𝑟𝑎𝑚 : 𝑠𝑡𝑟, 𝑑𝑖𝑓 𝑓 _𝑒𝑟𝑟𝑜𝑟 : 𝑠𝑡𝑟, 𝑝𝑟𝑒𝑣_𝑎𝑡𝑡𝑒𝑚𝑝𝑡 : 𝑠𝑡𝑟, 𝑦 : 𝑠𝑡𝑟) : (𝑠𝑡𝑟)

ensures 𝑛𝑜𝐷𝑖𝑓 𝑓 (𝑏𝑎𝑠𝑒_𝑝𝑟𝑜𝑔𝑟𝑎𝑚, 𝑓𝑑 (𝑏𝑎𝑠𝑒_𝑝𝑟𝑜𝑔𝑟𝑎𝑚, 𝑑𝑖𝑓 𝑓 _𝑒𝑟𝑟𝑜𝑟, 𝑝𝑟𝑒𝑣_𝑎𝑡𝑡𝑒𝑚𝑝𝑡, 𝑦)) {

return 𝑏𝑎𝑠𝑒_𝑝𝑟𝑜𝑔𝑟𝑎𝑚; }

- Fig. 5. FGGM definition for 𝑑𝑖𝑓 𝑓 𝐸𝑟𝑟𝑜𝑟𝐹𝐺𝐺𝑀. Invoked when the previous iteration’s output failed the diff checker. The prompt includes the diff error and previous attempt, instructing the model to preserve the base program logic.


𝑖𝑑 := 𝑣𝑒𝑟𝑖𝑓 𝑖𝑒𝑟𝐸𝑟𝑟𝑜𝑟𝐹𝐺𝐺𝑀 𝐺𝑀𝑖𝑑 := 𝑐𝑙𝑎𝑢𝑑𝑒 𝑡𝑦𝑝𝑒𝑆𝑖𝑔 := (𝑏𝑎𝑠𝑒_𝑝𝑟𝑜𝑔𝑟𝑎𝑚 : 𝑠𝑡𝑟, 𝑣𝑒𝑟𝑖𝑓 𝑦_𝑒𝑟𝑟𝑜𝑟 : 𝑠𝑡𝑟, 𝑝𝑟𝑒𝑣_𝑎𝑡𝑡𝑒𝑚𝑝𝑡 : 𝑠𝑡𝑟) → 𝑠𝑡𝑟

Φ𝑙 := true Ψ𝑙 := 𝑛𝑜𝐷𝑖𝑓 𝑓 (𝑏𝑎𝑠𝑒_𝑝𝑟𝑜𝑔𝑟𝑎𝑚, 𝑓 (𝑏𝑎𝑠𝑒_𝑝𝑟𝑜𝑔𝑟𝑎𝑚, 𝑣𝑒𝑟𝑖𝑓 𝑦_𝑒𝑟𝑟𝑜𝑟, 𝑝𝑟𝑒𝑣_𝑎𝑡𝑡𝑒𝑚𝑝𝑡)) 𝑓𝑝 := function 𝑓𝑝 (𝑏𝑎𝑠𝑒_𝑝𝑟𝑜𝑔𝑟𝑎𝑚 : 𝑠𝑡𝑟, 𝑣𝑒𝑟𝑖𝑓 𝑦_𝑒𝑟𝑟𝑜𝑟 : 𝑠𝑡𝑟, 𝑝𝑟𝑒𝑣_𝑎𝑡𝑡𝑒𝑚𝑝𝑡 : 𝑠𝑡𝑟) : (𝑠𝑡𝑟) {

var 𝑠𝑔 : 𝑠𝑡𝑟 :=

“Focus on:\n”

+ “- Strengthening invariants MINIMALLY\n”

+ “- Adding simple decomposition assertions\n”

+ “- Ensuring decreases clauses are correct\n”;

if (𝑖𝑠𝑆𝑢𝑏𝑠𝑡𝑟𝑖𝑛𝑔(“timeout”, 𝑣𝑒𝑟𝑖𝑓 𝑦_𝑒𝑟𝑟𝑜𝑟) ∨ 𝑖𝑠𝑆𝑢𝑏𝑠𝑡𝑟𝑖𝑛𝑔(“resource”, 𝑣𝑒𝑟𝑖𝑓 𝑦_𝑒𝑟𝑟𝑜𝑟)) {

𝑠𝑔 := “TIMEOUT/RESOURCE ISSUE: Break down the proof into smaller steps:\n”

+ “- Add strategic intermediate assertions\n”

+ “- Call helper lemmas to establish sub-goals\n”

+ “- Simplify complex invariants\n”; }

if (𝑖𝑠𝑆𝑢𝑏𝑠𝑡𝑟𝑖𝑛𝑔(“lemma”, 𝑣𝑒𝑟𝑖𝑓 𝑦_𝑒𝑟𝑟𝑜𝑟) ∨ 𝑖𝑠𝑆𝑢𝑏𝑠𝑡𝑟𝑖𝑛𝑔(“postcondition”, 𝑣𝑒𝑟𝑖𝑓 𝑦_𝑒𝑟𝑟𝑜𝑟)) {

𝑠𝑔 := “LEMMA PROOF ISSUE: Add explicit proof steps in lemma body:\n”

+ “- Assert intermediate facts that lead to postcondition\n”

+ “- Unfold recursive function definitions\n”

+ “- Use case analysis if needed\n”; }

if (𝑖𝑠𝑆𝑢𝑏𝑠𝑡𝑟𝑖𝑛𝑔(“invariant”, 𝑣𝑒𝑟𝑖𝑓 𝑦_𝑒𝑟𝑟𝑜𝑟)) {

𝑠𝑔 := “INVARIANT ISSUE: Adjust loop invariants:\n”

+ “- Ensure invariants are maintained after each iteration\n”

+ “- Add bounds and relationships incrementally\n”

+ “- Keep invariants minimal but sufficient\n”; }

if (𝑖𝑠𝑆𝑢𝑏𝑠𝑡𝑟𝑖𝑛𝑔(“type”, 𝑣𝑒𝑟𝑖𝑓 𝑦_𝑒𝑟𝑟𝑜𝑟) ∨ 𝑖𝑠𝑆𝑢𝑏𝑠𝑡𝑟𝑖𝑛𝑔(“constraint”, 𝑣𝑒𝑟𝑖𝑓 𝑦_𝑒𝑟𝑟𝑜𝑟)) {

𝑠𝑔 := “TYPE CONSTRAINT ISSUE: Check generic type parameters:\n”

+ “- Propagate nonemptiness constraints like T(00)\n”

+ “- Ensure type parameters match between caller and callee\n”; } return

“The previous Dafny annotation preserved the base logic but failed verification.\n\n”

+ “Verification error:\n” + 𝑣𝑒𝑟𝑖𝑓 𝑦_𝑒𝑟𝑟𝑜𝑟 + “\n\n”

+ 𝑠𝑔 + “\n”

+ “Base program:\n” +𝑏𝑎𝑠𝑒_𝑝𝑟𝑜𝑔𝑟𝑎𝑚 + “\n\n”

+ “Previous attempt:\n” + 𝑝𝑟𝑒𝑣_𝑎𝑡𝑡𝑒𝑚𝑝𝑡 + “\n\n”

+ “Please fix the annotations. Do NOT modify method signatures, requires, or ensures clauses.\n”

+ “Return ONLY the corrected Dafny code in a ```dafny code block.”; }

𝑓𝑑 := function 𝑓𝑑 (𝑏𝑎𝑠𝑒_𝑝𝑟𝑜𝑔𝑟𝑎𝑚 : 𝑠𝑡𝑟, 𝑣𝑒𝑟𝑖𝑓 𝑦_𝑒𝑟𝑟𝑜𝑟 : 𝑠𝑡𝑟, 𝑝𝑟𝑒𝑣_𝑎𝑡𝑡𝑒𝑚𝑝𝑡 : 𝑠𝑡𝑟, 𝑦 : 𝑠𝑡𝑟) : (𝑠𝑡𝑟)

ensures 𝑛𝑜𝐷𝑖𝑓 𝑓 (𝑏𝑎𝑠𝑒_𝑝𝑟𝑜𝑔𝑟𝑎𝑚, 𝑓𝑑 (𝑏𝑎𝑠𝑒_𝑝𝑟𝑜𝑔𝑟𝑎𝑚, 𝑣𝑒𝑟𝑖𝑓 𝑦_𝑒𝑟𝑟𝑜𝑟, 𝑝𝑟𝑒𝑣_𝑎𝑡𝑡𝑒𝑚𝑝𝑡, 𝑦)) {

return 𝑏𝑎𝑠𝑒_𝑝𝑟𝑜𝑔𝑟𝑎𝑚; }

- Fig. 6. FGGM definition for 𝑣𝑒𝑟𝑖𝑓𝑖𝑒𝑟𝐸𝑟𝑟𝑜𝑟𝐹𝐺𝐺𝑀. Invoked when the previous iteration passed the diff checker but failed verification. The prompting function analyzes the verification error to provide targeted guidance (timeout, lemma, invariant, or type issues).


method 𝑎𝑔𝑒𝑛𝑡 (𝑏𝑎𝑠𝑒_𝑝𝑟𝑜𝑔𝑟𝑎𝑚 : 𝑠𝑡𝑟) returns (𝑟 : 𝑠𝑡𝑟)

ensures 𝑛𝑜𝐷𝑖𝑓 𝑓 (𝑏𝑎𝑠𝑒_𝑝𝑟𝑜𝑔𝑟𝑎𝑚,𝑟) {

var 𝑚𝑎𝑥_𝑎𝑡𝑡𝑒𝑚𝑝𝑡𝑠 : 𝑖𝑛𝑡 := 5; var 𝑎𝑡𝑡𝑒𝑚𝑝𝑡 : 𝑖𝑛𝑡 := 0; var 𝑏𝑒𝑠𝑡 : 𝑠𝑡𝑟 := 𝑏𝑎𝑠𝑒_𝑝𝑟𝑜𝑔𝑟𝑎𝑚; var 𝑏𝑒𝑠𝑡_𝑣𝑒𝑟𝑖𝑓 𝑖𝑒𝑑 : 𝑏𝑜𝑜𝑙 := false;

var 𝑝𝑟𝑒𝑣_𝑑𝑖𝑓 𝑓 _𝑒𝑟𝑟 : 𝑠𝑡𝑟 := “”; var 𝑝𝑟𝑒𝑣_𝑣𝑒𝑟_𝑒𝑟𝑟 : 𝑠𝑡𝑟 := “”; var 𝑝𝑟𝑒𝑣_𝑐𝑜𝑑𝑒 : 𝑠𝑡𝑟 := “”;

while (𝑎𝑡𝑡𝑒𝑚𝑝𝑡 < 𝑚𝑎𝑥_𝑎𝑡𝑡𝑒𝑚𝑝𝑡𝑠) invariant 𝑛𝑜𝐷𝑖𝑓 𝑓 (𝑏𝑎𝑠𝑒_𝑝𝑟𝑜𝑔𝑟𝑎𝑚,𝑏𝑒𝑠𝑡) decreases 𝑚𝑎𝑥_𝑎𝑡𝑡𝑒𝑚𝑝𝑡𝑠 − 𝑎𝑡𝑡𝑒𝑚𝑝𝑡

{

var 𝑦 : 𝑠𝑡𝑟; if (𝑎𝑡𝑡𝑒𝑚𝑝𝑡 = 0) {

𝑦 := 𝑖𝑛𝑖𝑡𝑖𝑎𝑙𝐹𝐺𝐺𝑀(𝑏𝑎𝑠𝑒_𝑝𝑟𝑜𝑔𝑟𝑎𝑚); } else {

if (𝑝𝑟𝑒𝑣_𝑑𝑖𝑓 𝑓 _𝑒𝑟𝑟 ≠ “”) {

𝑦 := 𝑑𝑖𝑓 𝑓 𝐸𝑟𝑟𝑜𝑟𝐹𝐺𝐺𝑀(𝑏𝑎𝑠𝑒_𝑝𝑟𝑜𝑔𝑟𝑎𝑚, 𝑝𝑟𝑒𝑣_𝑑𝑖𝑓 𝑓 _𝑒𝑟𝑟, 𝑝𝑟𝑒𝑣_𝑐𝑜𝑑𝑒); } else {

𝑦 := 𝑣𝑒𝑟𝑖𝑓 𝑖𝑒𝑟𝐸𝑟𝑟𝑜𝑟𝐹𝐺𝐺𝑀(𝑏𝑎𝑠𝑒_𝑝𝑟𝑜𝑔𝑟𝑎𝑚, 𝑝𝑟𝑒𝑣_𝑣𝑒𝑟_𝑒𝑟𝑟, 𝑝𝑟𝑒𝑣_𝑐𝑜𝑑𝑒); }

}

𝑝𝑟𝑒𝑣_𝑑𝑖𝑓 𝑓 _𝑒𝑟𝑟 := “”; 𝑝𝑟𝑒𝑣_𝑣𝑒𝑟_𝑒𝑟𝑟 := “”; 𝑝𝑟𝑒𝑣_𝑐𝑜𝑑𝑒 := 𝑦;

var 𝑑𝑖𝑓 𝑓 _𝑒𝑟𝑟 : 𝑠𝑡𝑟 := 𝑛𝑜𝐷𝑖𝑓 𝑓𝑊𝑖𝑡ℎ𝐸𝑟𝑟𝑜𝑟𝑀𝑠𝑔(𝑏𝑎𝑠𝑒_𝑝𝑟𝑜𝑔𝑟𝑎𝑚, 𝑦); if (𝑑𝑖𝑓 𝑓 _𝑒𝑟𝑟 = “”) {

var 𝑣_𝑒𝑟𝑟 : 𝑠𝑡𝑟 := 𝑑𝑎𝑓 𝑛𝑦𝑉𝑒𝑟𝑖𝑓 𝑖𝑒𝑟𝑊𝑖𝑡ℎ𝐸𝑟𝑟𝑜𝑟𝑀𝑠𝑔(𝑦); if (𝑣_𝑒𝑟𝑟 = “”) {

###### 𝑟 := 𝑦; return;

} else { if (¬𝑏𝑒𝑠𝑡_𝑣𝑒𝑟𝑖𝑓 𝑖𝑒𝑑) { 𝑏𝑒𝑠𝑡 := 𝑦; } 𝑝𝑟𝑒𝑣_𝑣𝑒𝑟_𝑒𝑟𝑟 := 𝑣_𝑒𝑟𝑟;

} } else {

𝑝𝑟𝑒𝑣_𝑑𝑖𝑓 𝑓 _𝑒𝑟𝑟 := 𝑑𝑖𝑓 𝑓 _𝑒𝑟𝑟;

} 𝑎𝑡𝑡𝑒𝑚𝑝𝑡 := 𝑎𝑡𝑡𝑒𝑚𝑝𝑡 + 1;

} 𝑟 := 𝑏𝑒𝑠𝑡; return;

}

- Fig. 7. Verified agent program for Dafny annotation synthesis. On the first iteration, 𝑖𝑛𝑖𝑡𝑖𝑎𝑙𝐹𝐺𝐺𝑀 (Fig. 4) generates an initial annotation. On subsequent iterations, the agent dispatches to 𝑑𝑖𝑓 𝑓 𝐸𝑟𝑟𝑜𝑟𝐹𝐺𝐺𝑀 (Fig. 5) or 𝑣𝑒𝑟𝑖𝑓𝑖𝑒𝑟𝐸𝑟𝑟𝑜𝑟𝐹𝐺𝐺𝑀 (Fig. 6) depending on the previous error type. Each FGGM guarantees 𝑛𝑜𝐷𝑖𝑓 𝑓 (𝑏𝑎𝑠𝑒_𝑝𝑟𝑜𝑔𝑟𝑎𝑚,𝑦), maintaining the loop invariant. Upon exhausting all attempts, the agent returns 𝑏𝑒𝑠𝑡, which satisfies the postcondition by the loop invariant.


#### L FGGM Syntax

The syntax of a first-order guarded generative model (FGGM) can be described using the following BNF grammar.Weusetheproduction rules (⟨ident⟩, ⟨type⟩, ⟨spec⟩, ⟨program⟩, ⟨string_lit⟩, ⟨formula⟩) from Appendix A.

⟨𝑖𝑑⟩ ::= ⟨ident⟩ ⟨𝐺𝑀𝑖𝑑⟩ ::= ⟨ident⟩

⟨𝑡𝑦𝑝𝑒𝑆𝑖𝑔⟩ ::= ”(”⟨typedVars⟩”)”” → ”⟨type⟩ ⟨typedVars⟩ ::= ⟨typedVar⟩ | ⟨typedVar⟩, ⟨typedVars⟩

⟨typedVar⟩ ::= ⟨ident⟩ : ⟨type⟩ ⟨Φ𝑙⟩ ::= "requires" ⟨formula⟩ ⟨Ψ𝑙⟩ ::= "ensures" ⟨formula⟩ ⟨𝑓𝑝⟩ ::= ⟨program⟩ ⟨𝑓𝑑⟩ ::= ⟨program⟩

⟨info⟩ ::= ⟨string_lit⟩

#### M FGGM Validity Check

- Algorithm 3 checks whether an FGGM definition is valid. It verifies that the type signature and local contracts are syntactically well-formed and that all terms using library functions satisfy their input specifications. It then checks that the prompting program and fallback program are type-correct and terminating. Finally, the fallback program is verified using the deductive verifier to ensure it satisfies the local contract for all inputs. The FGGM definition is accepted only if no errors are found.


- Algorithm 3 validateFGGM

- 1: Input: FGGM definition G = (𝑖𝑑,𝐺𝑀𝑖𝑑,𝑡𝑦𝑝𝑒𝑆𝑖𝑔, Φ𝑙, Ψ𝑙, 𝑓𝑝, 𝑓𝑑 )
- 2: Input: Library functions F𝑐, axioms A
- 3: Output: {} if valid else set of errors err
- 4: err ← {}
- 5: if ¬𝑊𝑒𝑙𝑙𝑇𝑦𝑝𝑒𝑑(𝑡𝑦𝑝𝑒𝑆𝑖𝑔) then
- 6: err ← err ∪ {Invalid type signature}
- 7: end if
- 8: if ¬𝑊𝑒𝑙𝑙𝐹𝑜𝑟𝑚𝑒𝑑𝐹𝑜𝑟𝑚𝑢𝑙𝑎(Φ𝑙 ) then
- 9: err ← err ∪ {Invalid input contract}
- 10: end if
- 11: if ¬𝑊𝑒𝑙𝑙𝐹𝑜𝑟𝑚𝑒𝑑𝐹𝑜𝑟𝑚𝑢𝑙𝑎(Ψ𝑙 ) then
- 12: err ← err ∪ {Invalid output contract}
- 13: end if
- 14: if ¬𝐶ℎ𝑒𝑐𝑘𝑇𝑒𝑟𝑚𝑠(Φ𝑙, F𝑐 ) then
- 15: err ← err ∪ {Invalid library terms in Φ𝑙 }
- 16: end if
- 17: if ¬𝐶ℎ𝑒𝑐𝑘𝑇𝑒𝑟𝑚𝑠(Ψ𝑙, F𝑐 ) then
- 18: err ← err ∪ {Invalid library terms in Ψ𝑙 }
- 19: end if
- 20: if ¬𝑇𝑦𝑝𝑒𝐶ℎ𝑒𝑐𝑘(𝑓𝑝) or ¬𝑇𝑒𝑟𝑚𝑖𝑛𝑎𝑡𝑒𝑠(𝑓𝑝) then
- 21: err ← err ∪ {Invalid prompting program}
- 22: end if
- 23: if ¬𝑇𝑦𝑝𝑒𝐶ℎ𝑒𝑐𝑘(𝑓𝑑 ) or ¬𝑇𝑒𝑟𝑚𝑖𝑛𝑎𝑡𝑒𝑠(𝑓𝑑 ) then
- 24: err ← err ∪ {Invalid fallback program}
- 25: end if
- 26: if ¬𝑉𝑒𝑟𝑖𝑓 𝑦(∀𝑥1 . . .𝑥𝑛, 𝑦. Φ𝑙 (𝑥1 . . .𝑥𝑛) ⇒ Ψ𝑙 (𝑥1 . . .𝑥𝑛, 𝑓𝑑 (𝑥1 . . .𝑥𝑛, 𝑦))) then
- 27: err ← err ∪ {Fallback violates contract}
- 28: end if
- 29: return err


- Algorithm 4 checks whether a concrete input–output tuple satisfies the FGGM output contract.


It first substitutes the concrete values into the specification Ψ𝑙. If the resulting formula is quantifierfree, the checker directly evaluates it by computing all terms using the library functions. If the specification contains quantifiers, the substituted formula is combined with the axioms and input specification and submitted to an SMT solver with a timeout. The procedure returns true only if the solver confirms satisfiability within the time bound.

- Algorithm 4 𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 Contract Checker


- 1: Input: Concrete values (𝑥1, . . .,𝑥𝑛, 𝑦)
- 2: Input: Local contracts (Φ𝑙, Ψ𝑙 ), axioms A
- 3: Output: 𝑇 if contract satisfied else 𝐹
- 4: 𝜙 ← 𝑆𝑢𝑏𝑠𝑡𝑖𝑡𝑢𝑡𝑒(Ψ𝑙, {𝑥1, . . .,𝑥𝑛, 𝑦})
- 5: if 𝑄𝑢𝑎𝑛𝑡𝑖𝑓 𝑖𝑒𝑟𝐹𝑟𝑒𝑒(𝜙) then
- 6: if 𝜙 = ¬𝜙′ then return ¬𝑐ℎ𝑒𝑐𝑘A,Φ,𝜙′ (𝑥1, . . .,𝑥𝑛, 𝑦)
- 7: else if 𝜙 = 𝜙′ ∨𝜓 then return 𝑐ℎ𝑒𝑐𝑘A,Φ,𝜙′ (𝑥1, . . .,𝑥𝑛, 𝑦) ∨𝑐ℎ𝑒𝑐𝑘A,Φ,𝜓 (𝑥1, . . .,𝑥𝑛, 𝑦) ⊲ Recursively evaluate on subformulas
- 8: else if 𝜙 = 𝜙′ ∧𝜓 then return 𝑐ℎ𝑒𝑐𝑘A,Φ,𝜙′ (𝑥1, . . .,𝑥𝑛, 𝑦) ∧ 𝑐ℎ𝑒𝑐𝑘A,Φ,𝜓 (𝑥1, . . .,𝑥𝑛, 𝑦)
- 9: else if 𝑖𝑠𝐴𝑡𝑜𝑚𝑖𝑐(𝜙) then return 𝜙(𝑥1, . . .,𝑥𝑛, 𝑦) ⊲ Compute the atomic predicate 𝜙 value on (𝑥1, . . .,𝑥𝑛, 𝑦) 𝑇 or 𝐹
- 10: end if
- 11: end if
- 12: 𝜓 ← 𝜑A ∧ Φ𝑙 (𝑥1, . . .,𝑥𝑛) ∧ 𝜙
- 13: 𝑟𝑒𝑠 ← 𝑆𝑀𝑇𝑆𝑜𝑙𝑣𝑒(𝜓,𝑡𝑖𝑚𝑒)
- 14: if 𝑟𝑒𝑠 = 𝑆𝐴𝑇 then
- 15: return 𝑇
- 16: else
- 17: return 𝐹
- 18: end if


#### N Background on GRPO

Group Relative Policy Optimization (GRPO): GRPO is a reinforcement learning–based finetuning method for generative models that optimizes a policy by comparing outputs relative to other samples from the same input, rather than relying on an explicit value function. Let 𝜋𝜃 (𝑦 | 𝑝) denote the parametric policy for an FGGM 𝑖𝑑𝜃𝑖, where 𝑝 ∈ P is the input prompt and 𝑦𝑙 ∼ 𝜋𝜃 (· | 𝑝) is a sampled output. For each input 𝑝, GRPO samples a group of 𝐺 candidate outputs {𝑦(1), . . .,𝑦(𝐺)} from the current policy. Each sample is assigned a scalar reward 𝑟(𝑗) = R(𝑝,𝑦(𝑗)). Instead of using absolute rewards directly, GRPO computes relative advantages within the group:

∑︁𝐺

∑︁𝐺

𝑟(𝑗) − 𝜇𝑝 𝜎𝑝

𝑟(𝑗), 𝜎𝑝 = 𝐺1

, 𝜇𝑝 = 𝐺1

(𝑟(𝑗) − 𝜇𝑝)2 + 𝜖 (24)

𝐴(𝑗) =

𝑗=1

𝑗=1

Here 𝜇𝑝 and 𝜎𝑝 are the mean and standard deviation of rewards within the group.

∑︁𝐺

E𝑝∼P 𝐺1

max

min 𝜌(𝑗)𝐴(𝑗), clip(𝜌(𝑗), 1 − 𝜖, 1 + 𝜖)𝐴(𝑗) (25)

𝜃

𝑗=1

(𝑗) |𝑝)

where 𝜌(𝑗) = 𝜋𝜃 (𝑦

𝜋𝜃old(𝑦(𝑗)|𝑝) is the importance ratio. This clipped objective, similar to PPO, ensures

stable policy updates. In our setting, each FGGM 𝑖𝑑𝜃𝑖 defines a policy 𝜋𝜃𝑖 (𝑦𝑙 | 𝑝) over outputs 𝑦𝑙 for input 𝑝. The reward function defined in Eq. 23:

R(𝑝,𝑦𝑙) = 1 − 𝑆𝑖𝑔𝑚𝑜𝑖𝑑 L(𝑥, _,𝑦) × I(𝑦 = 𝑦𝑙) + 𝜆 × (1 − I(𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 (𝑝,𝑦𝑙))) (26)

#### O Hyperparameters

- Table 8 lists all hyperparameters used across the four evaluation tasks. The top block reports the shared pipeline settings applied uniformly across tasks; the middle blocks report task-specific training configurations for GSM-Symbolic and Symbolic Regression; the bottom block reports the per-task verifier and solver timeouts.


Table 8. Hyperparameter settings for all evaluation tasks.

###### Category Hyperparameter Value

Planner search budget (Δ) 10 FGGM rejection-sample budget (𝐾) 5 In-context examples 3 (2 for 𝜏2-bench)

Shared pipeline

Base model Qwen3-8B LoRA rank 16 LoRA alpha (𝛼) 32 GRPO training epochs 5 GRPO batch size 64 GRPO learning rate 1 × 10−5 GRPO generations per prompt (𝐺) 8

GRPO / LoRA (GSM-Symbolic)

Optimizer Adam Learning rate 0.05 Backpropagation steps 40

Parameter tuning (Symbolic Regression)

Dafny — dafny verify timeout 240s per subprocess call 𝜏2-bench — Z3 solver.check() timeout 10s per call (up to 2 retries) GSM-Symbolic — Z3 solver.check() timeout 5s per call

Verifier timeouts

#### P Planner Feedback

After each search–verify–learn iteration, SEVerA constructs structured feedback 𝐼′ from the execution traces of the current best candidate agent on the training data D (Algorithm 2, line 31). The planner LLM receives the task-performance score of the previous program along with per-example error diagnostics. Specifically, for each training example on which the previous candidate failed, SEVerA provides the planner with the example input, the agent’s output, and the corresponding error message (e.g., a verification error, a grammar violation, or an incorrect answer). The planner is then asked to generate a one-to-two sentence description and a suggested fix for each failed example. The resulting list of per-example descriptions and suggestions is collected and fed back to the planner as part of the context 𝐼′ when it samples the next candidate program. This feedback mechanism enables the planner to identify recurring failure patterns and adjust its synthesized FGGM definitions and prompting programs 𝑓𝑝 accordingly in subsequent iterations.

#### Q Planner LLM Prompt

The following is the prompt template used by the planner LLM to synthesize candidate agent programs. Placeholders in braces (e.g., {task_description}) are populated at each iteration with the task specification, postcondition, available operator library, agent signature, and feedback from the previous iteration’s execution traces (Appendix P).

You are an expert programmer tasked with writing a Dafny agent function. ## TASK {task_description} ## CRITICAL POSTCONDITION {postcondition_description} ## AVAILABLE OPERATORS You can use these operators in your agent: ```dafny {library_functions} ``` ## AGENT SIGNATURE AND POSTCONDITION ```dafny {agent_signature} ``` ## CONSTRAINTS

- - Fully Typed: All variables must have type annotations
- - No imports: All operators are already available in scope
- - No recursion: Don't call agent() recursively
- - Always satisfy postcondition: Every return path must satisfy the postcondition
- - No f-strings: Do not use format strings (f-strings); use the addition operator for concatenation {task_specific_constraints}

## FEW-SHOT EXAMPLES {few_shot_examples}

## PREVIOUS AGENT CODE {previous_agent_code}

## PREVIOUS ATTEMPT FEEDBACK {feedback}

## SCORING INFORMATION {scoring_info}

## OUTPUT Write ONLY the agent function inside a ```dafny``` block.

Make sure to:

- - Check the postcondition before every return
- - If the task fails, return a safe fallback value
- - LLM calls are stateless, calling the LLM again does not maintain previous context
- - Predefine variables before using them to avoid syntax errors {task_specific_output_tips}


- Fig. 8. Planner LLM prompt template. The planner receives this prompt at each search–verify–learn iteration, with placeholders filled from the task specification and feedback from the previous iteration.


#### R Proof Details

Lemma 5.1 (Completeness of Checker). For any valid FGGM G with quantifier-free Ψ𝑙, ∀𝑥1 ∈ 𝑇1, . . .,∀𝑥𝑛 ∈ 𝑇𝑛,∀𝑦 ∈ 𝑇𝑜. Φ𝑙(𝑥1, . . .,𝑥𝑛) =⇒ 𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 (𝑥1, . . .,𝑥𝑛,𝑦) ⇐⇒ Ψ𝑙(𝑥1, . . .,𝑥𝑛,𝑦) .

Proof of Lemma 5.1. We prove the claim by structural induction on the quantifier-free formula Ψ𝑙. Fix arbitrary (𝑥1, . . .,𝑥𝑛,𝑦). We show:

𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 (𝑥1, . . .,𝑥𝑛,𝑦) ⇐⇒ Ψ𝑙(𝑥1, . . .,𝑥𝑛,𝑦).

Base case. Suppose Ψ𝑙 is an atomic predicate 𝑃(𝑥1, . . .,𝑥𝑛,𝑦) over terms constructed from computable library functions in F𝑐. Under the substitution (𝑥1, . . .,𝑥𝑛,𝑦),𝑐ℎ𝑒𝑐𝑘A,Φ,𝑃 evaluates each term

by executing the corresponding functions in F𝑐. Since these functions are computable 𝑐ℎ𝑒𝑐𝑘A,Φ,𝑃 exactly computes the atomic predicate 𝑃(𝑥1, . . .,𝑥𝑛,𝑦) on (𝑥1, . . .,𝑥𝑛,𝑦) which reduces to 𝑇 or 𝐹.

Inductive step. Assume the claim holds for formulas 𝜙 and𝜓 i.e. 𝑐ℎ𝑒𝑐𝑘A,Φ,𝜙(𝑥1, . . .,𝑥𝑛,𝑦) ⇐⇒ 𝜙(𝑥1, . . .,𝑥𝑛,𝑦) and𝑐ℎ𝑒𝑐𝑘A,Φ,𝜓 (𝑥1, . . .,𝑥𝑛,𝑦) ⇐⇒ 𝜓(𝑥1, . . .,𝑥𝑛,𝑦) We show it holds for compound formulas:

- • If Ψ𝑙 = ¬𝜙, then by definition of 𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙, 𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 (𝑥1, . . .,𝑥𝑛,𝑦) = ¬𝑐ℎ𝑒𝑐𝑘A,Φ,𝜙(𝑥1, . . .,𝑥𝑛,𝑦).

By the inductive hypothesis, 𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 (𝑥1, . . .,𝑥𝑛,𝑦) ⇐⇒ ¬ 𝑐ℎ𝑒𝑐𝑘A,Φ,𝜙(𝑥1, . . .,𝑥𝑛,𝑦) ⇐⇒

¬ 𝜙(𝑥1, . . .,𝑥𝑛,𝑦) ⇐⇒ Ψ𝑙(𝑥1, . . .,𝑥𝑛,𝑦)

- • If Ψ𝑙 = 𝜙 ∧𝜓, then

𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 (𝑥1, . . .,𝑥𝑛,𝑦) = 𝑐ℎ𝑒𝑐𝑘A,Φ,𝜙(𝑥1, . . .,𝑥𝑛,𝑦) ∧ 𝑐ℎ𝑒𝑐𝑘A,Φ,𝜓 (𝑥1, . . .,𝑥𝑛,𝑦), which, by the inductive hypothesis,

𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 (𝑥1, . . .,𝑥𝑛,𝑦) ⇐⇒ 𝑐ℎ𝑒𝑐𝑘A,Φ,𝜙(𝑥1, . . .,𝑥𝑛,𝑦) ∧ 𝑐ℎ𝑒𝑐𝑘A,Φ,𝜓 (𝑥1, . . .,𝑥𝑛,𝑦)

⇐⇒ 𝜙(𝑥1, . . .,𝑥𝑛,𝑦) ∧𝜓(𝑥1, . . .,𝑥𝑛,𝑦) ⇐⇒ Ψ𝑙(𝑥1, . . .,𝑥𝑛,𝑦)

- • If Ψ𝑙 = 𝜙 ∨𝜓, the argument is analogous tp Ψ𝑙 = 𝜙 ∧𝜓.


##### □

Lemma R.1(CheckerSoundness). 𝜑A =⇒ ∀𝑥1 ∈ 𝑇1, . . .,∀𝑥𝑛 ∈ 𝑇𝑛,∀𝑦 ∈ 𝑇𝑜. Φ𝑙(𝑥1, . . .,𝑥𝑛) =⇒ 𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 (𝑥1, . . .,𝑥𝑛,𝑦) =⇒ Ψ𝑙(𝑥1, . . .,𝑥𝑛,𝑦) .

Proof. For quantifier-free Ψ𝑙 soundnessfollowsfromLemma5.1. For Ψ𝑙 with qunatifier𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 returns true if (𝜑A ∧ Φ𝑙(𝑥1, . . .,𝑥𝑛)) ∧ Ψ𝑙(𝑥1, . . .,𝑥𝑛,𝑦) is evalautes to true within timeout. Hence for any (𝑥1, . . .,𝑥𝑛,𝑦)

𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 (𝑥1, . . .,𝑥𝑛,𝑦) =⇒ (𝜑A ∧ Φ𝑙(𝑥1, . . .,𝑥𝑛)) ∧ Ψ𝑙(𝑥1, . . .,𝑥𝑛,𝑦) (𝜑A ∧ 𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 (𝑥1, . . .,𝑥𝑛,𝑦)) =⇒ Φ𝑙(𝑥1, . . .,𝑥𝑛) ∧ Ψ𝑙(𝑥1, . . .,𝑥𝑛,𝑦) (𝜑A ∧ 𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 (𝑥1, . . .,𝑥𝑛,𝑦) ∧ Φ𝑙(𝑥1, . . .,𝑥𝑛)) =⇒ Ψ𝑙(𝑥1, . . .,𝑥𝑛,𝑦)

(𝜑A ∧ Φ𝑙(𝑥1, . . .,𝑥𝑛)) =⇒ (𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 (𝑥1, . . .,𝑥𝑛,𝑦)) =⇒ Ψ𝑙(𝑥1, . . .,𝑥𝑛,𝑦))

𝜑A =⇒ Φ𝑙(𝑥1, . . .,𝑥𝑛)) =⇒ ((𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 (𝑥1, . . .,𝑥𝑛,𝑦)) =⇒ Ψ𝑙(𝑥1, . . .,𝑥𝑛,𝑦)) (27) From Eq 27 it follows , 𝜑A =⇒ ∀𝑥1 ∈ 𝑇1, . . .,∀𝑥𝑛 ∈ 𝑇𝑛,∀𝑦 ∈ 𝑇𝑜. Φ𝑙(𝑥1, . . .,𝑥𝑛) =⇒

𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 (𝑥1, . . .,𝑥𝑛,𝑦) =⇒ Ψ𝑙(𝑥1, . . .,𝑥𝑛,𝑦) . □

Theorem 5.2 (Valid Local contract). For any valid FGGM G with (Φ𝑙, Ψ𝑙) and parametric GM 𝑓GΘ, 𝜑A =⇒ ∀𝜃 ∈ Θ,∀𝑥1 ∈ 𝑇1, . . .,∀𝑥𝑛 ∈ 𝑇𝑛. Φ𝑙(𝑥1, . . .,𝑥𝑛) =⇒ Ψ𝑙(𝑥1, . . .,𝑥𝑛,𝑖𝑑G(𝑥1, . . .,𝑥𝑛)) .

Proof. Let 𝑟 = 𝑖𝑑G(𝑥1, . . .,𝑥𝑛). Based on the rejection sampler with the checker 𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 (Fig 2).𝑟 is returned from the if branch if𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 (𝑥1, . . .,𝑥𝑛,𝑦){return𝑦; } or from the fallback 𝑟 = 𝑓𝑑(𝑥1, . . .,𝑥𝑛,𝑦). Using the semantics of an if block, the following condition always holds for the output 𝑟 where 𝑦𝑓 is the final rejected sample.

𝜑A =⇒ (∀𝜃 ∈ Θ.(∀𝑥𝑖 ∈ 𝑇𝑖).Φ𝑙 (𝑥1, . . .,𝑥𝑛) =⇒ (𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 (𝑥1, . . .,𝑥𝑛,𝑟) ∨ (𝑟 = 𝑓𝑑(𝑥1, . . .,𝑥𝑛,𝑦𝑓 ))) (28)

Eq. 29 follows from the validity of the fallback 𝑓𝑑, and Eq. 18 follows from the soundness of the checker 𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 (lemma R.1). To simplify the notation, we used (∀𝑥𝑖 ∈ 𝑇𝑖) to denote (∀𝑥1 ∈ 𝑇1, . . .,∀𝑥𝑛 ∈ 𝑇𝑛).

𝜑A =⇒ ∀𝜃 ∈ Θ.(∀𝑥𝑖 ∈ 𝑇𝑖).Φ𝑙 (𝑥1, . . .,𝑥𝑛) ∧ (𝑟 = 𝑓𝑑(𝑥1, . . .,𝑥𝑛,𝑦𝑓 )) =⇒ Ψ𝑙 (𝑥1, . . .,𝑥𝑛,𝑟) (29) 𝜑A =⇒ (∀𝜃 ∈ Θ.(∀𝑥𝑖 ∈ 𝑇𝑖).(Φ𝑙 (𝑥1, . . .,𝑥𝑛) ∧ 𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 (𝑥1, . . .,𝑥𝑛,𝑟)) =⇒ Ψ𝑙 (𝑥1, . . .,𝑥𝑛,𝑟)) (30) 𝜑A =⇒ (∀𝜃 ∈ Θ.(∀𝑥𝑖 ∈ 𝑇𝑖).Φ𝑙 (𝑥1, . . .,𝑥𝑛) =⇒ Ψ𝑙 (𝑥1, . . .,𝑥𝑛,𝑟)) Using Eq. (28, 29, 30)

□ Theorem 5.3. If P{Θ} ≠ ⊥ with FGGM set G, then ∀𝜃1 ∈ Θ1, . . .,∀𝜃𝑘 ∈ Θ𝑘.𝜑A =⇒ ∀𝑥1 ∈

𝑇1, . . .,∀𝑥𝑛 ∈ 𝑇𝑛.Φ(𝑥1, . . .,𝑥𝑛) =⇒ Ψ(𝑥1, . . .,𝑥𝑛, P{(𝜃1,...,𝜃𝑘)/Θ}(𝑥1, . . .,𝑥𝑛)) . Proof. Let, G = {G1, . . ., G𝑘} and AG denote the set of first-order sentences defining all the

local contracts as shown below. AG = {𝜑G1, . . .,𝜑G𝑘 } where 𝜑G𝑖 defined below 𝜑G𝑖 : ∀𝑥1 ∈ 𝑇1, . . .,𝑥𝑛 ∈ 𝑇𝑛.G𝑖Φ𝑙 (𝑥1, . . .,𝑥𝑛) =⇒ G𝑖Ψ𝑙 (𝑥1, . . .,𝑥𝑛, G𝑖(𝑥1, . . .,𝑥𝑛)) (𝜑A =⇒ (∀𝜃1 ∈ Θ1.𝜑G1)) ∧ · · · ∧ (𝜑A =⇒ (∀𝜃𝑘 ∈ Θ𝑘.𝜑G𝑘)) from Theorem 5.2

𝜑A =⇒ ∧𝑘𝑖=1(∀𝜃𝑖 ∈ Θ𝑖.𝜑G𝑖) (31) If P{Θ} ≠ ⊥ then VC[Φ, Ψ] with C = (𝐺𝐷, F ∪ G, A ∪ AG) enusres

(P{Θ} ≠ ⊥) =⇒ ((𝜑A ∧ (∧𝑘𝑖=1∀𝜃𝑖 ∈ Θ𝑖.𝜑G𝑖) =⇒ ∀𝑥1 ∈ 𝑇1 . . .∀𝑥𝑛 ∈ 𝑇𝑛.Φ(𝑥1, . . .,𝑥𝑛) =⇒ Ψ(𝑥1, . . .,𝑥𝑛, P{(𝜃1,...,𝜃𝑘)/Θ}(𝑥1, . . .,𝑥𝑛)) (32) (P{Θ} ≠ ⊥) =⇒ ((𝜑A =⇒

∀𝜃1 ∈ Θ1, . . .,∀𝜃𝑘 ∈ Θ𝑘,∀𝑥1 ∈ 𝑇1 . . .∀𝑥𝑛 ∈ 𝑇𝑛. Φ(𝑥1, . . .,𝑥𝑛) =⇒ Ψ(𝑥1, . . .,𝑥𝑛, P{(𝜃1,...,𝜃𝑘)/Θ}(𝑥1, . . .,𝑥𝑛)) Using Eq. 31 and Eq. 32

□ Theorem 5.4 (Soundness). If 𝑓 ∗ ≠ ⊥ then, 𝜑A =⇒ ∀𝑥1 ∈ 𝑇1, . . .,∀𝑥𝑛 ∈ 𝑇𝑛.Φ(𝑥1, . . .,𝑥𝑛) =⇒

Ψ(𝑥1, . . .,𝑥𝑛, 𝑓 ∗(𝑥1, . . .,𝑥𝑛)).

Proof. 𝑓 ∗ ← argmin𝑓 ∈P (𝑥,𝑦)∈D L(𝑥,𝑦, 𝑓 (𝑥)). If 𝑓 ∗ ≠ ⊥, then by definition (P ≠ {}) ∧ (𝑓 ∗ ∈ P). By Theorem 5.3, every program 𝑓 ∈ P that satisfies 𝜑A also satisfies

∀𝑥1 ∈ 𝑇1, . . .,∀𝑥𝑛 ∈ 𝑇𝑛, Φ(𝑥1, . . .,𝑥𝑛) =⇒ Ψ(𝑥1, . . .,𝑥𝑛, 𝑓 (𝑥1, . . .,𝑥𝑛)).

□

Theorem 5.5 (Sufficient Success Condition). If (i) L penalizes constraint violations, i.e.,∀𝑥 ∈ 𝑇𝑖, ∀𝑦,𝑦′ ∈ 𝑇𝑜. (Φ(𝑥)∧¬Ψ(𝑥,𝑦)∧Ψ(𝑥,𝑦′)) =⇒ L(𝑥, _,𝑦′) < L(𝑥, _,𝑦),, (ii) Ψ is quantifier-free, (iii) there exists a non-parametric program 𝑓𝑑 ∈ S(𝐺, F𝑐) such that 𝑓𝑑 satisfies (Φ, Ψ). Then, for any typecorrect generative model 𝑓𝑛𝜃 : 𝑇𝑖 → 𝑇𝑜 with initial parameters and any prompting program 𝑓𝑝, there exists a program 𝑓 ∈ S(𝐺, F) such that: (1) 𝑓 satisfies (Φ, Ψ), and (2) L(𝑓 ) ≤ L(𝑓𝑛𝜃). Moreover, if there exists (𝑥, _) ∈ D such that ¬Ψ(𝑥, 𝑓𝑛𝜃 (𝑥)), then L(𝑓 ) < L(𝑓𝑛𝜃) where 𝐿(𝑓 ) = (𝑥,_)∈D L(𝑥, _, 𝑓 (𝑥)).

Proof. Let 𝑓𝑛𝜃 : 𝑇1 × · · · ×𝑇𝑛 → 𝑇𝑜 be any type-correct generative model. By assumption (iii), there exists 𝑓𝑑 ∈ S(𝐺, F𝑐) such that

𝜑A =⇒ ∀𝑥1, . . .,𝑥𝑛.;Φ(𝑥1, . . .,𝑥𝑛) =⇒ Ψ(𝑥1, . . .,𝑥𝑛, 𝑓𝑑(𝑥1, . . .,𝑥𝑛)). Construction. Define

G = (𝑖𝑑, 𝑓𝑛𝜃,𝜏, Φ𝑙, Ψ𝑙, 𝑓𝑝, 𝑓𝑑,𝑖𝑛𝑓𝑜),

with (Φ𝑙, Ψ𝑙) := (Φ, Ψ) and any well-typed 𝑓𝑝. Since 𝑓𝑑 satisfies the contract and Ψ is quantifier-free, G is valid and 𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 is complete (Lemma 5.1).

Define the program 𝑓 ∈ S(𝐺, F) as:

function 𝑓 (𝑥1 : 𝑇1, . . .,𝑥𝑛 : 𝑇𝑛) : 𝑇𝑜 {return 𝑖𝑑(𝑥1, . . .,𝑥𝑛); }. Correctness. For any (𝑥1, . . .,𝑥𝑛) such that Φ(𝑥1, . . .,𝑥𝑛) holds, by Theorem 5.2,

Ψ(𝑥1, . . .,𝑥𝑛, 𝑓 (𝑥1, . . .,𝑥𝑛)).

Output of 𝑓 . Fix (𝑥1, . . .,𝑥𝑛) with Φ(𝑥1, . . .,𝑥𝑛). By completeness,

𝑐ℎ𝑒𝑐𝑘A,Φ𝑙,Ψ𝑙 (𝑥1, . . .,𝑥𝑛,𝑦) ⇐⇒ Ψ(𝑥1, . . .,𝑥𝑛,𝑦). Hence,

𝑓𝑛𝜃 (𝑥1, . . .,𝑥𝑛) if Ψ(𝑥1, . . .,𝑥𝑛, 𝑓𝑛𝜃 (𝑥1, . . .,𝑥𝑛)), 𝑓𝑑(𝑥1, . . .,𝑥𝑛) otherwise.

𝑓 (𝑥1, . . .,𝑥𝑛) =

#### Loss comparison. For any (𝑥, _) ∈ D:

- Case 1: Ψ(𝑥, 𝑓𝑛𝜃 (𝑥)). Then 𝑓 (𝑥) = 𝑓𝑛𝜃 (𝑥) and L(𝑥, _, 𝑓 (𝑥)) = L(𝑥, _, 𝑓𝑛𝜃 (𝑥)).
- Case 2: ¬Ψ(𝑥, 𝑓𝑛𝜃 (𝑥)). Then 𝑓 (𝑥) = 𝑓𝑑(𝑥) and Ψ(𝑥, 𝑓 (𝑥)) holds. By assumption (i),


L(𝑥, _, 𝑓 (𝑥)) < L(𝑥, _, 𝑓𝑛𝜃 (𝑥)). Thus,

∀(𝑥, _) ∈ D. L(𝑥, _, 𝑓 (𝑥)) ≤ L(𝑥, _, 𝑓𝑛𝜃 (𝑥)), which implies

L(𝑓 ) ≤ L(𝑓𝑛𝜃).

Strict improvement. If ∃(𝑥,) ∈ D such that ¬Ψ(𝑥, 𝑓𝑛𝜃 (𝑥)), then Case 2 holds for at least one point, yielding

L(𝑓 ) < L(𝑓𝑛𝜃). Conclusion. The constructed program 𝑓 satisfies (Φ, Ψ) and achieves no greater loss than 𝑓𝑛𝜃, with strict improvement when violations occur. Note the program verification setup satisfies this sufficient condition. □

