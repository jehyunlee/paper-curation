# arXiv:2412.21154v1[cs.AI]30 Dec 2024

## AVIARY: TRAINING LANGUAGE AGENTS ON CHALLENGING SCIENTIFIC TASKS

Siddharth Narayanan1 James D. Braza1 Ryan-Rhys Griffiths1 Manu Ponnapati1 Albert Bou1 Jon Laurent1

Ori Kabeli1 Geemi Wellawatte1 Sam Cox1 Samuel G. Rodriques1,3∗ Andrew D. White1,2∗

1FutureHouse Inc., San Francisco, CA 2University of Rochester, Rochester, NY 3 Francis Crick Institute, London, UK Correspondence to: {sam,andrew}@futurehouse.org

December 31, 2024

### ABSTRACT

Solving complex real-world tasks requires cycles of actions and observations. This is particularly true in science, where tasks require many cycles of analysis, tool use, and experimentation. Language agents are promising for automating intellectual tasks in science because they can interact with tools via natural language or code. Yet their flexibility creates conceptual and practical challenges for software implementations, since agents may comprise non-standard components such as internal reasoning, planning, tool usage, as well as the inherent stochasticity of temperature-sampled language models. Here, we introduce Aviary, an extensible gymnasium for language agents. We formalize agents as policies solving language-grounded partially observable Markov decision processes, which we term language decision processes. We then implement five environments, including three challenging scientific environments: (1) manipulating DNA constructs for molecular cloning, (2) answering research questions by accessing scientific literature, and (3) engineering protein stability. These environments were selected for their focus on multi-step reasoning and their relevance to contemporary biology research. Finally, with online training and scaling inference-time compute, we show that language agents backed by open-source, non-frontier LLMs can match and exceed both frontier LLM agents and human experts on multiple tasks at up to 100x lower inference cost.

### 1 Introduction

Language agents [1–4] are AI agents [5] that integrate LLMs [6–8] as core components. LLMs excel at zero-shot generalization [9,10], providing a notable advantage over traditional AI agents, such as those based on handcrafted rules or reinforcement learning, which often struggle to generalize to new environments [11]. While LLMs can exhibit flawed reasoning and logic when used in isolation [12–14], constructing a language agent by grounding LLMs in an environment with observational feedback can mitigate these issues. Early work on language agents used LLMs to directly output actions in the external environment [15–17], while more recently, language agents have been augmented with internal reasoning [18,19] and planning [20,21] procedures, as well as long-term memory storage [22,23].

An emergent research challenge is to pose a theoretical description of the learning problem solved by language agents [4,24] and to develop efficient methods to optimize the components of a language agent [24–26]. Here, we define common language agent tasks as language decision processes (LDPs) and frame language agents as stochastic computation graphs [27] that may be trained to solve LDPs. We show that pre-existing agents [18,19, 21] can be implemented within our stochastic computation graph framework and introduce a simple and extensible software package named LDP that enables modular interchange of environments, agents, and optimizers, simplifying experimentation across a variety of settings.

∗These authors jointly supervise technical work at FutureHouse.

![image 1](Narayanan et al._2024_Aviary training language agents on challenging scientific tasks_images/imageFile1.png)

- Figure 1: An overview of the five implemented Aviary environments and the language decision process (LDP) framework. The term language decision process here jointly refers to our theoretical description of the class of problems solved by language agents, as well as a software framework for implementing language agents based on a stochastic computation graph that enables training of language agent components such as LLM weights, prompts, memories, or LLM sampling parameters like temperature.


In the problems we consider, we use the term optimization of language agents in the reinforcement sense to encompass procedures that yield iterative improvement of the language agent over time through feedback from an environment. An example of one such optimization algorithm is expert iteration (EI) [28–30] which achieves learning through successive rounds of supervised fine-tuning on (self-) generated trajectories from a progressively stronger language agent. Other approaches include outcome supervision [31], which is similar to rejection-sampled expert iteration, and process supervision [32], which still selects high-reward trajectories, but also focuses on the individual steps of the outcome.

In what follows, we introduce our definition of an environment, a language decision process, and optimization of agents backed by a stochastic computation graph. We recast popular benchmarks such as GSM8K [33] and HOTPOTQA [34] as environments and integrate three scientific environments related to challenging tasks in the natural sciences. The scientific environments are (1) DNA construct engineering, where the task is to answer questions pertaining to molecular cloning [35], (2) scientific literature question answering, where the task is to answer a multiple choice question by finding a specific passage from the scientific literature [36,37], and (3) protein design, where the goal is to propose mutations to improve the stability of a given protein sequence [38,39]. On the DNA construct design and scientific literature question answering environments, we demonstrate that language agents based on the small, open-source Llama-3.1-8B-Instruct model, when trained with expert iteration and using inference-time majority vote sampling, can exceed the performance of both human experts and frontier LLMs.

The environment framework described in this work, Aviary, is available at github.com/Future-House/aviary and the stochastic computation graph framework together with language agent implementations and training code is available at github.com/Future-House/ldp. The components of and relationship between these frameworks is delineated in Figure 1.

### 2 Related Work

Language Agent Formalisms Although language agents have achieved impressive empirical performance across a range of applications [1,37,40], there is still no universally agreed upon theoretical framework for defining a language agent. In terms of conceptual models, the cognitive architectures for language agents (CoALA) framework [4], inspired by ideas from production systems and cognitive architectures, taxonomizes agents according to their information storage (working and long-term memories), decision-making procedures e.g. planning, and action space (divided into internal and external actions). Similarly, in [41], the author describes language agents as consisting of memory, planning, and tool usage components. Theoretically, many works represent language agents as partially observable Markov decision processes (POMDPs) [42–48] yet differ in their treatment of the action space e.g. in [43] the authors partition the action space into internal and external actions in a similar fashion to CoALA where internal actions are a family of functions that operate on the agent’s memory and external actions elicit an interaction with the environment. By contrast, in [44] the authors do not make a distinction between internal and external actions. In [49] the authors introduce a general

framework for studying the design and analysis of LLM-based algorithms based on a computational graph where they assume LLM nodes are stateless, leaving consideration of aspects of language agents such as memory to future work.

Language Agent Optimization Frameworks Optimization of language agents may involve the learning of prompts, tool usage, LLM weights, LLM inference hyperparameters such as temperature, as well as more exotic language agent components such as edges between nodes in multiagent computation graphs. Frameworks such as LangChain [50] and LlamaIndex [51] support manual optimization of prompts via human editing. Optimizers such as EcoOptiGen [52] leverage black-box optimization schemes to learn LLM inference hyperparameters such as temperature, the maximum number of tokens, and the number of completions. Prompt optimization comprises the optimization of white-box LLMs and black-box LLMs (LLMs that exist behind an API and for which numerical gradients are unavailable). In white-box prompt optimization [53–56] numerical gradients can be taken over soft prompts [57], the embedding representation of the text-based ‘hard’ prompt. In black-box prompt optimization a multitude of techniques have been applied which attempt to overcome the absence of gradients [58–79]. Tool learning [80,81] can be attempted through in-context demonstrations [82] or can seek to fine tune LLM weights on example demonstrations of appropriate tool usage [30,83] using techniques such as expert iteration [28,29]. In terms of methods that seek to optimize many components of a language agent simultaneously, the TextGrad framework, introduced in [25] backpropagates textual feedback received from an LLM. In a similar fashion, Zhou et. al [84] also backpropagate textual feedback by creating natural language simulacrums of weights, losses, and gradients. In [85] the authors use a metaprompt to encourage an LLM to perform discrete optimization over an agent architecture. The Trace framework introduced in [26] proposes the OptoPrime optimizer which passes code execution traces in place of gradients and uses an LLM to provide textual feedback and perform updates. Another popular language agent optimization framework is DSPy [86–88] which parametrizes a computational graph for language agents and focuses on automatically generating and selecting useful demonstrations for in-context learning. In the multi-agent setting, GPTSwarm [24] introduces a computation graph and performs binary edge-level optimization and node-level optimization over prompts. Lastly, OpenR [89] is a framework for LLM reinforcement learning and inference-time scaling, but is targeted at token-level optimization, not tool usage.

Language Agent Benchmarks Existing language agent benchmarks feature a broad range of applications including machine learning tasks [90], data science [91, 92], data analysis [93, 94], quantitative reasoning [95], and causal reasoning [96]. In Aviary, we place particular focus on scientific tasks. Relevant work in this area has included DiscoveryBench, a benchmark for data-driven hypothesis generation [97], ChemBench [98] which focuses on chemistry tasks, BLADE [99] which is concerned with data-driven science, SciAgent [100] a benchmark for scientific reasoning, DISCOVERYWORLD [101] which concentrates on cycles of scientific discovery, and ScienceWorld [102] which is concerned with scientific reasoning. For a review focused on scientifically-relevant agents the reader is directed to [103]. In Aviary, we focus on sequential decision-making tasks that necessitate multiple steps of agent-environment interactions. We construct environments from the pre-existing datasets such as GSM8K [33], HOTPOTQA [34], and LitQA2 [37] by casting them as parametrizable tools manipulating an environment state.

Our principal contributions are: (1) A precise definition of language decision processes (LDPs) for language-agent tasks and encompass many proposed agent architectures as stochastic computation graphs. (2) We introduce Aviary, a gym framework that emphasizes multi-step reasoning and tool usage, and provide five gym implementations (including three for scientific tasks). (3) We demonstrate that non-frontier LLMs, trained online with inference time sampling, can match or exceed the performance of frontier models on these tasks with a modest compute budget. (4) We release Aviary and our LDP framework as open-source software libraries to enable broader use and experimentation.

### 3 Theory

##### 3.1 Language Decision Processes

A language decision process (LDP) is a Partially-Observable Markov Decision Process (POMDP) [104] whose action and observation spaces are represented in natural language. More concretely, a LDP can be defined using the tuple (V,S,A,O,T,Z,R,γ). Here, V is a non-empty alphabet2, S is the state space, A ⊆ V∗ is the action space3, T(s′|s,a) : S × A  → P(S) is the transition function, R(s,a) : S × A  → P(R) is the reward function, O ⊆ V∗ is the observation space, Z(o|s′) : S × A  → P(O) is the observation function4, and γ ∈ [0,1] is the discount factor.

2In all LDPs we consider, V is the set of unicode characters, since Aviary is implemented in Python 3. 3Where V∗ def= ∞n=0 Vn is the Kleene closure of a set V [105,106]. 4In all LDPs we consider, a state s′ ∈ S uniquely defines an observation o ∈ O. Unless otherwise specified, we omit the

observation function Z.

Unlike traditional reinforcement learning agents, feedback for language agents is “grounded” in the sense that environment observations must be converted to text [107]. As such, the alphabet V is an important component of the LDP definition and follows other works [42,44,45]. The solution to an LDP is a policy πθ : O  → A, where θ denotes the set of policy parameters we wish to learn. The parameter set θ is abstract and encapsulates any optimizable parameter of the language agent that may impact the action chosen such as LLM weights, inference hyperparameters such as temperature, as well as parametrized procedures such as internal reasoning.

In contrast to previous works which demarcate between internal and external actions [4,43], where internal actions include reasoning and memory retrieval, in our problem framing we consider the action space to strictly constitute interactions with the external environment, allowing our parameter set θ to subsume optimizable procedures that are internal to the language agent such as memory retrieval and internal reasoning. Practically, it is worth noting that the complexity of our environments is such that we do not expect to obtain the globally optimal πθ∗. Our more modest goal is to be able to optimize θ in a direction that improves πθ over time.

The observations in all environments we consider are deterministic functions of the state and so the reader may assume Z = 1 henceforth. For example, the environment may involve executing code and the observation is side-effects of the code. The state S would include all information necessary to induce the Markov property of the transition function: the file system, the versions of packages, any environment variables, the hardware, etc. However, the observation is just the output message of the executed code.

##### 3.2 Stochastic Computation Graphs

In the general case, a language agent may include both stochastic and deterministic operations. We build on the formalism of stochastic computation graphs (SCG) [27]: directed, acyclic graphs with nodes corresponding to computations and edges corresponding to arguments.

A deterministic node v corresponds to a function fv, and the node’s output o(v) is defined as:

- o(v) = fv({o(w)|w ∈ parents(v)}) (1) Similarly, a stochastic node u is defined by a (conditional) distribution pu, with output:
- o(u) ∼ pu(·|{o(w)|w ∈ parents(v)}) (2) Note that inputs to the graph can be treated as constant (deterministic) nodes. Outputs of the graph are leaf nodes.


A language agent’s policy is simply an SCG with a string input (the observation) and a string output (the action). Language agent architectures can be easily expressed as SCGs by combining deterministic and stochastic nodes. The SCGs of the below common language agent architectures are visualized in Figure 2.

- (a) Language model as policy: a single stochastic node corresponding to sampling from the language model.
- (b) Retrieval-augmented generation (RAG): a deterministic node (document retrieval) leading to a stochastic node (LLM sampling).
- (c) Rejection sampling from LLM: several stochastic nodes (LLM samples), all leading to a deterministic node (selecting the preferred sample).
- (d) ReAct [18]: two consecutive stochastic nodes, corresponding to sampling a reasoning string and an action (tool call).


In many cases, a language agent defines an agent state ξt that is a function of previous observations and actions. For example, the agent state of a multi-turn LLM conversation is typically defined as:

ξt = [o0,a0,...,at−1,ot−1] at ∼ pLM(·|ξt) (3)

The SCG output is then a tuple of (at,ξt+1), namely an action and a new state. Separating the state enables batching of agent states and observations, as well as keeping the SCG as a true function. Memories, if desired, are considered part of the agent state, and their retrieval is incorporated in the SCG.

##### 3.3 Training Methods

Below we describe commonly-used imitation learning [108–110] methods employed to improve language agent performance on our environments. These training methods do not optimize the SCG graph directly, instead we optimize only the language model node in the SCG.

|ot| |
|---|---|
| | |


|at ∼ pLLM(· | ot)|
|---|


(a) Language model as policy

|kNN|
|---|


|at ∼ pLLM(· | ot,KNN(ot))|
|---|


|ot|
|---|


(b) Retrieval-augmented generation

|a1t ∼ pLLM(· | ot)|
|---|


|at = argmaxq(ot,ait)|
|---|


|ot|
|---|


|a2t ∼ pLLM(· | ot)|
|---|


(c) Rejection sampling from language model

|ot| |
|---|---|
| | |


|x ∼ pLLM(· | ot)| |
|---|---|
| | |


|at ∼ pLLM(· | ot,x)|
|---|


(d) ReAct

- Figure 2: Simple language agent architectures represented as stochastic computation graphs. Deterministic nodes are solid rectangles; stochastic nodes are dashed. Note that we augment the graphs with a deterministic input node to indicate how the observation ot is consumed.


Behavior cloning (BC) BC [111, 112] refers to a general imitation learning technique that derives a policy by supervised learning on high quality trajectories termed expert demonstrations. In the context of language agents this is typically achieved by supervised fine-tuning (SFT) of an LLM on either human trajectories or trajectories generated from a stronger LLM [43,48,83,113,114]. In the context of our experiments, we use BC to initialize the trajectory buffer for an expert iteration loop on Llama-3.1-8B-Instruct, due to its inability to self-generate successful trajectories prior to training.

Expert iteration (EI) EI [28–30] performs behavior cloning in an iterative fashion, improving the demonstration data each iteration. The inputs to the EI algorithm are a base LLM represented as an initial policy π0 and a trajectory buffer D0, which may either be empty or consist of an initial set of demonstrations generated by a human expert or a stronger LLM. At each round of EI, first a batch B of trajectories are sampled from the current policy πi (via rollout). Then these trajectories {τi(j)}Bj=1 are filtered (the rejection sampling step [115]) based on return R exceeding a threshold value ρ. The filtered trajectories are then appended to the trajectory buffer Di and the current LLM, πi, is fine-tuned on Di using cross-entropy loss. Pseudocode for EI is provided in Algorithm 1.

Algorithm 1 Expert Iteration with Rejection Sampling Fine-Tuning

- 1: Inputs: initial policy π0, iteration rounds N, batch size B, return threshold ρ, trajectory buffer D0
- 2: for i = 1,...N do
- 3: Ti ← rollout(πi−1)
- 4: Di ← Di−1 ∪ {(τi(j),Ri(j))| τi(j) ∈ Ti,Ri(j) > ρ,j = 1,...,B} ▷ Rejection sample trajectories
- 5: πi ← SFT(Di) ▷ SFT on updated trajectory buffer
- 6: end for


Inference Compute Scaling Scaling inference-time compute to improve LLM performance is now a frequentlyemployed technique [116, 117]. There are two common settings: oracle-verified (pass@k) and majority vote (consensus@k). As shown in Brown et al. [116], if an oracle verifier can identify any correct solution – namely, if you can obtain just one correct answer among k – then it is possible to scale across multiple orders of magnitude. Without an oracle verifier, majority voting can be used [117]. Majority voting is simply the consensus response, which requires some natural binning of responses. Although oracle verification scales to very large numbers of completions [118], majority voting plateaus more quickly than oracle verification [116]. In this work, we omit any unsure or truncated trajectories (trajectories for which the agent did not submit an answer) from majority voting.

- 4 Environments We briefly detail the environments comprising Aviary. Further details on the environments may be found in the appendix.


##### 4.1 GSM8K

The GSM8K environment is based on the GSM8K dataset introduced in [33], which consists of linguistically diverse grade school math word problems designed to assess multi-step mathematical reasoning. The GSM8K dataset comprises a training set of 7,473 questions and a test set of 1,319 questions. The environment exposes a calculator tool.

##### 4.2 HOTPOTQA

The HOTPOTQA environment is based on the HOTPOTQA dataset introduced in [34], which was subsequently extended to a language agent environment in [18]. The HOTPOTQA dataset comprises 112,779 question-answer pairs. We run evals on the 7,405 eval subset of questions. In the HOTPOTQA environment, the agent is provided with a Wikipedia API and tasked with answering the questions. There are is no given context to the agent and the API supports access to all of Wikipedia articles and sections.

##### 4.3 PaperQA

PaperQA [36,37] is a language agent/environment pairing developed for literature research and question answering that leverages reranking and contextual summarization. Specifically in [37], an untrained version 2 of PaperQA, called PaperQA2, attained superhuman-level precision and human-level accuracy on version 2 of a literature question and answer task, called LitQA2 [35]. PaperQA2 was implemented with tools and a tool calling agent, so we refactored PaperQA2 to be an Aviary environment as part of the version 5 release of the paper-qa Python package. To make it easy for the machine learning community to use, we modified the search tool to center on local storage containing a set of PDF, text, and HTML files using tantivy [119]. This local search is why we call this PaperQA variant “PaperQA2 Local.” The citation traversal tool was omitted for this local setting. A complete tool was added to support agents that require at least one tool selection and allow the agent to declare if the answer addresses all parts of the question.

LitQA2 features 248 questions, 199 of which are publicly available and the remaining 49 were held out as a test set. We reuse the same test set here for comparability with [37]. The remaining 199 questions were randomly 80%-20% split such that the training set is 149 questions and the evaluation set is 40 questions. The test split questions can be found in the aviary-paper-data Hugging Face dataset. Note this PaperQA environment is capable of doing tasks beyond LitQA2. For example, it can do literature review writing and contradiction detection as reported in Skarlinski et. al [37].

To build the search indexes, we (1) aggregated all paper search or citation traversal results from a database of run logs made during [37], (2) binned the results corresponding to each LitQA2 question, and (3) combined bins based our train, evaluation, and test split LitQA2 questions. The end result is 18955 DOIs in the train split, 5457 DOIs in the evaluation split, and 5519 DOIs in the test split. The train, evaluation, and test split DOIs are can be found in the paper-qa GitHub repository. Each split has over 100X the reachable DOIs compared to contained questions so agents face a learnable retrieval task. Due to copyright of the underlying papers, we only distribute their DOIs, not the parsed text used by the environment index.

##### 4.4 Molecular Cloning

Molecular cloning is a fundamental technique of manipulating DNA in biomedical research, enabling a majority of basic research such gene function studies, creating transgenic models, and producing recombinant proteins [120,121]. The molecular cloning process results in a DNA “construct,” which is a general term for DNA that encodes for the desired biologic molecule or genes. Molecular cloning involves assembling DNA fragments, ligating them into vectors, introducing the recombinant DNA into host organisms, and screening for desired clones [120]. The steps in molecular cloning are usually done with a combination of human planning, specialized software, and databases of known purchasable components.

We have formulated this into an environment. The molecular cloning environment is composed of the main tools used by experts in the lab: (1) an annotation tool that can predict the function of segments of a plasmid (2) a natural language search tool that retrieves sequences given text and (3) tools required to plan the protocols. The protocol specific tools include PCR primer design, ligation, codon optimization, Gibson or Golden gate assembly, and fetching genes from standard organisms. Many implementations use or were derived from the Go poly library. The annotation tools were built using MMSeqs2 [122]. The complete list of tools is given in the supporting information.

The specific tasks used for evaluation come from the SeqQA benchmark [35]. SeqQA consists of “textbook” style questions, such as counting the fragments after digestion, predicting translated sequences, and identifying polymerase chain reaction primers. A complete description of their construction and human evaluation is given in Laurent et. al [35]. The test SeqQA questions in this work have not been previously released, but are created using the same procedure and are available in the aviary-paper-data Hugging Face dataset. There are 150 test questions, although we omit 10 related to RNA specifically. There are 500 train questions, which we take from the original SeqQA release accessible here. SeqQA is solvable with only a subset of the tools, and the tools have not been engineered specifically for the conventions of SeqQA. For example, SeqQA questions assume 1-indexing, but the tools are 0-indexed and thus the language agent needs to learn to convert. Another example is that SeqQA only considers coding open reading frames, but the tools can consider both reading frames.

The combination of tools for manipulating DNA constructs, annotating sequences or plasmids, and searching for DNA components in databases enables tasks beyond SeqQA. The environment also supports working with “CloningScenarios,” which is a more multiple-choice benchmark for working with DNA constructs derived from real lab notebooks [35]. One can also do normal plasmid tasks, such as “Clone the given protein [protein] into [plasmid] to express in yeast with a GFP fusion (check annotations above, plus GFP in correct relative orientation).”

##### 4.5 Protein Stability

Engineering proteins with increased stability is an essential task in protein engineering, with wide-ranging applications in enzyme engineering and drug design [123]. Protein stability is a general term for a protein’s ability to retain function under non-native conditions, such as increased temperature, lowered pH, or aggregation-inducing solvents. Numerous sequence-based and structure-based approaches have been developed to enhance protein stability [124], including deep learning methods such as ThermoMPNN [125]. However, protein stability is determined by complex protein sequence and structure properties along with biological context making it challenging to predict accurately with existing in-silico approaches [126]. Therefore, an approach that integrates protein structure and sequence methods, including physics-based methods like Rosetta, can provide a more comprehensive understanding of biophysical determinants of protein stability [127].

The protein stability environment is composed of tools commonly used by human experts to analyze a protein sequence and structure. The main tools are (1)a biochemical description tool,that describes the types of bonds between any residues in the protein sequence,; 2) a sequence property description tool that describes the molecular weight, aromaticity, instability index, iso-electric point, sequence charge, and average hydropathy of a protein sequence; 3) a secondary structure annotation tool; and (4) a Rosetta tool to compute aggregation propensity score per residue [128].

310.ai [129] introduced a chat interface for natural language-based protein design, though it is not an agent. Conversely, methods such as ProteinForceGPT, an autonomous large language model (LLM) agent introduced by [130], uses pretrained models to predict force–separation curves, supplemented by models like Chroma [131] and OmegaFold [132]. Furthermore, recent work has shown the effectiveness of LLM as biological sequence optimizers [133]. Our environment offers a framework for training of agents that can effectively integrate knowledge from physics-based models, biochemical principles, and pre-trained protein models while leveraging experimental results to improve protein stability.

We assess the language agent’s performance on 40 proteins randomly selected from the megascale protein stability dataset, excluding any that are mentioned in the text of [134]. Proposed mutations are evaluated using the Rosetta cart_ddg protocol [135].

### 5 Results

We assess the capabilities of tool-equipped language agents to solve problems in the aforementioned environments. These environments require iterative cycles of tool calls and observation. We then explore behavior cloning and expert iteration to train agents on specific tasks in environments. Finally, we explore using inference-time compute via majority sampling to improve performance.

An overview of the models used in this work and their performance on our tasks is shown in Figure 3. This includes both trained (described below) and frontier language models. They are:

- • Zero-shot Claude 3.5 Sonnet: claude-3-5-sonnet-20241022 is prompted to solve the tasks without access to the environment or any tools. No example output or formatting instructions are given.
- • Claude 3.5 Sonnet agent: A language agent that prompts claude-3-5-sonnet-20241022 to call environment tools until the task is solved. It uses the recommended Anthropic API tool-calling schema [136]. The observation emitted from a tool call may include a summary or details about the environment state.


- • LDP-trained language agent: An LDP agent that has been trained to solve tasks using the environment. This can either be based on fine-tuned gpt-4o (GSM8K, hotpotQA) or Llama-3.1-8B-Instruct (SeqQA, LitQA2).
- • Majority voting: We sample 32 trajectories using the trained LDP agent and use their consensus as the solution to the task. For protein stability, we do oracle-verification/pass@k, as in protein engineering one typically tests a batch and only keep the most successful. [116]


The mixture of existing benchmarks and closed-source models was chosen to demonstrate the flexibility of the Aviary software. Claude 3.5 Sonnet was the best frontier LLM we tested across tasks, and was thus used as the benchmark for comparison. With the exception of GSM8K, all agents are able to improve over the zero-shot baseline when given access to the environment. In the case of GSM8K, we hypothesize that a sequence of calculator calls (with no intermediate reasoning) is out-of-distribution with respect to the LLMs’ training data, which may also contain math word problems. This is consistent with recent findings [137], where modifying elements of the original questions or adding irrelevant information also caused performance degradation across multiple models, as such changes similarly introduce a distribution shift from the training data.

Training LDP agents improves performance over untrained LDP agents of the same architecture. On challenging tasks (SeqQA, LitQA2), a relatively small model (Llama-3.1-8B-Instruct) can be trained to match performance of a much larger frontier model (claude-3-5-sonnet). Majority voting can be used to sample multiple times from the LDP agents, giving a further large gain at the cost of increased inference compute. The protein stability task sees a large improvement for pass@16, which is a well-known effect for oracle-verified problems [116]. These results are broken out in more detail below.

![image 2](Narayanan et al._2024_Aviary training language agents on challenging scientific tasks_images/imageFile2.png)

- Figure 3: Ability of LLMs and language agents to solve tasks using Aviary environments. All LDP-trained agents are optimized using behavior cloning and expert iteration. For GSM8K and HOTPOTQA, EI is performed on gpt-4o; SeqQA and LitQA2 use Llama-3.1-8B-Instruct (see Section 5.1). The difference in GSM8K zero-shot reported here (89%) vs Anthropic benchmarks [136] (96.5%) is likely because Anthropic’s use of chain-of-thought prompting, which we did not use. All agents are rolled out on the environment for a maximum of 10 steps, with the exception of PaperQA, which allowed up to 18 steps.


##### 5.1 Behavior Cloning and Expert Iteration

Using ldp, we train language agents in the environments described above. Since these environments are challenging, expert iteration initially rejects the majority of trajectories, leading to very slow learning. We therefore begin with a period of behavior cloning, using high-quality trajectories collected by rejection-sampling from a larger LLM. Once the language agent can solve a reasonable fraction of training problems, we switch to expert iteration. All experiments are conducted with Llama-3.1-8B-Instruct [138] as the base language model, using Nvidia A100 GPUs.

- In Figure 4A, we show the results of training an agent (Llama-3.1-8B EI) to solve SeqQA tasks using the molecular cloning environment. Expert iteration is seeded with 2841 valid trajectories (behavior cloning), followed by 8 further EI epochs using trajectories from the agent as it improves. Behavior cloning provides a large initial jump in performance, with a further 14% (absolute) improvement from online learning. We note a gap in performance on train and test set tasks, indicating some degree of overfitting.
- In Figure 4B, we show the results of a similar procedure applied to LitQA2 problems in the PaperQA environment. In this case, the untrained Llama-3.1-8B agent has non-trivial performance (30% accuracy), but still significantly improves from behavior cloning (430 trajectories). Because some LitQA2 problems are easier than others, we want to focus training on difficult tasks. Therefore, during expert iteration, we sample trajectories from each task in the dataset with probability:


wk j wj

; wk = M · (1 − fpassk ) (4)

P(task k) =

where fpassk is a moving average of task k’s pass rate as the agent is trained and M is a scaling factor (set to 20). With this, EI produces a small improvement beyond behavior cloning, up to 72% on the test set.

![image 3](Narayanan et al._2024_Aviary training language agents on challenging scientific tasks_images/imageFile3.png)

- Figure 4: Training language agents to solve (A) SeqQA tasks using the molecular cloning environment and (B) LitQA2 problems using the PaperQA environment. The first epoch represents behavior cloning, followed by expert iteration. These experiments use multiple workers to asynchronously collect trajectories and train the model, so GPU-hours measures the total time spent sampling and training. An untrained Llama-3.1-8B-Instruct agent solves 1% of SeqQA tasks, so we omit the data point at GPU-hours=0 in panel A.


Finally, in Figure 5, we study the distribution of SeqQA trajectories explored by a trained language agent. The demonstration trajectories (all correct) heavily feature assembly simulations and are relatively long. The trained agent was initially cloned from the demonstrations, but through online learning discovered significantly different ways to solve SeqQA tasks. Its trajectories are generally shorter and less diverse, suggesting that self-training tends to converge on a subset of possible paths.

##### 5.2 Inference Compute Scaling

We assessed majority voting on two of the environments that have multiple choice answers – SeqQA and LitQA2 – to see if it improves benchmarks in the LDP setting. We evaluated on test splits that we neither trained on nor should be

![image 4](Narayanan et al._2024_Aviary training language agents on challenging scientific tasks_images/imageFile4.png)

- Figure 5: Patterns of tool calls across trajectories. Colored boxes represent different tool categories, and edges between boxes represent consecutive actions taken in a trajectory, with darker edges implying more trajectories. In panel (A), we show the demonstration trajectories used for behavior cloning. Panels (B) and (C) show the trajectories sampled from the Llama-3.1-8B EI agent after expert iteration.


in frontier LLM training corpus because they are not on the public internet. Figure 6 shows the results on these two environments. Majority voting generally gives large improvements for these agents - about 20 percentage points of accuracy on both environments. Figure 6B shows that the LLM, without tools, gets about a 10 percentage point gain (although from a much lower starting accuracy). Figure 6D shows an example of what the majority votes look like on one specific LitQA2 question. Option 1 is correct, option 2 is a minority option and sometimes chosen, there is an unsure option, and lastly any truncated trajectories (e.g. unexpected failure during rollout or hitting max allowable steps). For majority voting, we filter out the unsure and failed trajectories. The biggest gains in accuracy are from 0 to 4 samples, but it continues up to 32 samples. These two environments are less than 200 unique questions, so the trend may continue if we have a larger set of unique questions.

Figure 6C shows that majority voting on LitQA2 with a Claude 3.5 Sonnet agent gives 0.89 accuracy on the test set, significantly exceeding previously reported scores of 0.67 from Skarlinski et. al [37] and human performance reported in Laurent et. al [35]. The Llama-3.1-8B EI agent shows good performance, matching human and previously reported best at only one sample. Three samples exceeds those marks, but it cannot match the Sonnet agent if it also uses majority voting on more than one sample. Nevertheless, exceeding a frontier LLM in the single sample setting on unseen data with a small model is a surprising result.

Figure 6A shows that consensus sampling of the Llama-3.1-8B EI agent significantly exceeds a Claude 3.5 Sonnet agent at all sample counts. SeqQA is more structured than LitQA2, requiring more consistent and longer tool call sequences. The Llama-3.1-8B EI agent can be sampled from cheaply, and so we ran 945 rollouts (Figure 6A inset). We still observe gains out to 100s of samples, giving a final accuracy of 0.89. The highest previously reported result on SeqQA was from a joint technical report from the US and UK AI Safety Institutes on pre-deployment evaluation of claude-3.5-sonnet-20241022 at 0.87 accuracy.

##### 5.3 Inference Cost Scaling

The results of the previous sections demonstrate how the performance of different agents scales as training time and sampled trajectories are increased. In this section, we offer a more practical metric: inference cost. This becomes especially relevant in a high-throughput setting, in which agents are tasked to solve thousands of problems in parallel.

We focus our comparison on the Claude 3.5 Sonnet agent versus the Llama-3.1-8B EI agent. We use the following rates for LLM inference at time of writing:

#### A)

#### B)

1.00

| |
|---|


Llama-3.1-8B EI Agent

0.2

Claude 3.5 Sonnet Agent

Accuracy

Joint AISI Report

Accuracy

0.75

SeqQA

Human

1.0

0.1

Claude 3.5 Sonnet

0.50

0.5

0.0

100 101 102 103

OutcomesonPQAQuestion1

0.25

#### C)

D)

1.00

21

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


Claude 3.5 Sonnet Agent

18

Llama-3.1-8B EI Agent

15

0.75

Human

Accuracy

LitQA2

12

Skarlinski et. al Claude 3.5 Sonnet

9

0.50

6

3

0.25

0

0 4 8 12 16 20 24 28 32 Inference Samples

Option1

Option2

Unsure

Failed

- Figure 6: A) majority voting accuracy in SeqQA setting as a function of sampled trajectories for trained Llama-3.1-8B EI agent and claude-3-5-sonnet-241022 agent. The majority voting increases performance to exceed previously reported scaffolded agents on this task (Joint AISI Report) [139], which used claude-3-5-sonnet-241022. “Claude 3.5 Sonnet” is claude-3-5-sonnet-241022 without tools (simply answering questions directly). The inset shows further gains from 0.86 to 0.89 from 32 to 945 samples. B) shows the change in accuracy of an LLM without tools vs. the language agent on SeqQA. The language agent has a greater gain from majority voting, showing >0.2 gain. C) majority voting accuracy on LitQA2 in PaperQA2 environment. Both agents significantly exceed previously measured human performance and best previous models on this task [37]. Claude 3.5-Sonnet Agent plateaus at 90% accuracy. D) Shows an example question voting on LitQA2 (question id 3e6d7a54). Option 1 is the correct response, option 2 is incorrect, and failure is because the agent did not submit an answer prior to trajectory termination. Error bars in the plots are computed by bootstrap resampling.


- • Claude 3.5 Sonnet: $3/1M input tokens and $15/1M output tokens5.
- • Llama-3.1-8B: $0.03/1M input and output tokens, a price typical in the LLM inference market6. While this price refers to inference of the vanilla model, we use it as a reasonable estimate for serving a EI-trained model with a similar set of optimizations.


In Figure 7, we report performance and inference cost on SeqQA and LitQA2. While majority voting with the Claude 3.5 Sonnet agent clearly outperforms other settings, this requires O($1) per task. We reach the same SeqQA accuracy using the Llama-3.1-8B EI agent for 100x less cost. While this was not achievable for LitQA2, we note that majority voting with Llama-3.1-8B EI still exceeds single-rollout with Sonnet for 3x less cost.

### 6 Discussion

We have presented a framework of a language agent and environment interacting to solve tasks that require multiple steps of reasoning and tool usage, which we call a language decision process. We implemented five environments, including three related to biology problems. These three environments contain a variety of tasks, but we focus on tasks with benchmarks that are easy to evaluate, namely LitQA and SeqQA (multiple choice) as well as a task focussed on modifying enzymes to improve their stability. Language agents in these environments perform significantly better than non-agentic LLMs.

We have applied two methods to improve the performance of language agents on the tasks we consider: expert iteration and majority voting. Smaller models, such as Llama-3.1-8B-Instruct, perform poorly without additional training.

- 5https://www.anthropic.com/pricing#anthropic-api
- 6https://lambdalabs.com/inference#pricing


![image 5](Narayanan et al._2024_Aviary training language agents on challenging scientific tasks_images/imageFile5.png)

- Figure 7: Accuracy vs. inference cost of two agents (Claude 3.5 Sonnet and Llama-3.1-8B EI) on two sets of tasks (SeqQA and LitQA2). For both agents, both the single-rollout and majority-voting settings are considered. Note that all inference settings here outperform human performance (reported in [37] and [35]).


The application of behavior cloning and expert iteration can overcome this limitation, however, achieving comparable performance to the best evaluated agents based on black-box frontier models (in this case claude-3-5-sonnet-241022). Majority voting provides additional performance gains at inference time. Majority voting benefits all agents and non-agentic LLMs tested, though it provides more benefit to agents. This is likely due to the fact that environment trajectories possess elevated level of stochasticity relative to a completion sampled from a non-agentic LLM. The protein stability task also benefits from increasing inference compute, though it uses oracle-verification.

Using an 8B model reduces the inference costs such that it is feasible to vote amongst ∼1000 rollouts per task. For reference, our SeqQA tasks require 7-10 LLM calls (Figure 5) and cost $0.07 on average per trajectory with claude-3-5-sonnet-241022 and $0.00066 per trajectory at current pricing with Llama-3.1-8B EI (although the tasks could be run for free on many consumer laptops). The human PhD contractors that represent the human data series in Figure 6 cost between $4 and $12 per question (see Laurent et. al [35] for a description of the combined hourly, performance, and completion bonuses). In summary, trained agents can exceed the accuracy of human and frontier models at 100x cheaper cost.

There are some limitations in this work. The comparisons are not exactly matched between humans and other previous reported results on benchmarks. One reason is that the Environments are complex pieces of software, with dozens of dependencies that all have specific versions. Another issue is that the splits we used are only now available (although they were included in the human assessments). We used splits that were impossible to have been scraped in training data. One reason we took this precaution is that websites have re-hosted the LitQA2 benchmark without the canary string [140], so that it is plausibly now in LLM pre-training corpuses.

Comparing against humans is also fraught, because they do not have access to the same tools. Although, in Laurent et. al [35] there were incentives for correct answers, ample time, and only restrictions against using AI tools. Nevertheless, it’s always possible that the humans could have been given better or more precise technology for the task. Ultimately, the test of these language agents is their ability to make novel scientific discoveries and not getting high scores on benchmarks.

### 7 Conclusion

We have presented Aviary, a gymnasium for language agents. Aviary currently contains five environments, three of which focus on challenging scientific tasks. Language agents, implemented in these environments, exceed the performance of zero-shot frontier LLMs on the SeqQA, HOTPOTQA, LitQA2, and protein stability tasks. Language agents also exceed human performance on SeqQA and LitQA2.

We have introduced the language decision process (LDP) framework for formally describing language agent tasks and showed that language agents can be cast as stochastic computation graphs. Through behavior cloning, expert iteration, and inference-time sampling, we demonstrated that trained Llama-3.1-8B EI agents can match and exceed the performance of humans and frontier LLMs in the LitQA2 and SeqQA benchmarks at significantly lower cost. Thus, we have demonstrated that modest compute budgets and model sizes can be competitive at solving realistic scientific tasks. The reported trained Llama-3.1-8B EI agents are compute efficient and exceed human-level task performance, enabling high-throughput automation of meaningful scientific tasks across biology.

Both the Aviary (aviary) and LDP (ldp) frameworks are open source and should serve as useful libraries for implementing environments and language agents.

### Acknowledgments

Work at FutureHouse is supported by the generosity of Eric and Wendy Schmidt. The results and models reported in this work used compute resources from the National AI Research Resource Pilot, including support from NVIDIA and the NVIDIA DGX Cloud. We also acknowledge all members of FutureHouse for useful discussions, including Cade Gordon, Peter Chang, Michael Skarlinski, and Conor Igoe.

### References

- [1] Grégoire Mialon, Roberto Dessi, Maria Lomeli, Christoforos Nalmpantis, Ramakanth Pasunuru, Roberta Raileanu, Baptiste Roziere, Timo Schick, Jane Dwivedi-Yu, Asli Celikyilmaz, et al. Augmented language models: a survey. Transactions on Machine Learning Research, 2023. 1, 2
- [2] Zhiheng Xi, Wenxiang Chen, Xin Guo, Wei He, Yiwen Ding, Boyang Hong, Ming Zhang, Junzhe Wang, Senjie Jin, Enyu Zhou, et al. The rise and potential of large language model based agents: A survey. arXiv preprint arXiv:2309.07864, 2023. 1
- [3] Chen Gao, Xiaochong Lan, Nian Li, Yuan Yuan, Jingtao Ding, Zhilun Zhou, Fengli Xu, and Yong Li. Large language models empowered agent-based modeling and simulation: A survey and perspectives. arXiv preprint arXiv:2312.11970, 2023. 1
- [4] Theodore Sumers, Shunyu Yao, Karthik Narasimhan, and Thomas Griffiths. Cognitive architectures for language agents. Transactions on Machine Learning Research, 2024. Survey Certification. 1, 2, 4
- [5] Stuart J Russell and Peter Norvig. Artificial intelligence: a modern approach. Pearson, 2016. 1
- [6] Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. Language models are few-shot learners. Advances in Neural Information Processing Systems, 33:1877–1901, 2020. 1
- [7] Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, et al. GPT-4 Technical Report. arXiv preprint arXiv:2303.08774, 2023. 1
- [8] Samuel R Bowman. Eight things to know about large language models. arXiv preprint arXiv:2304.00612, 2023. 1
- [9] Andy Zeng, Maria Attarian, Krzysztof Marcin Choromanski, Adrian Wong, Stefan Welker, Federico Tombari, Aveek Purohit, Michael S Ryoo, Vikas Sindhwani, Johnny Lee, et al. Socratic models: Composing zero-shot multimodal reasoning with language. In The Eleventh International Conference on Learning Representations,

2023. 1

- [10] Andrew Szot, Max Schwarzer, Harsh Agrawal, Bogdan Mazoure, Rin Metcalf, Walter Talbott, Natalie Mackraz, R Devon Hjelm, and Alexander T Toshev. Large language models as generalizable policies for embodied tasks. In The Twelfth International Conference on Learning Representations, 2024. 1
- [11] Brenden M Lake, Tomer D Ullman, Joshua B Tenenbaum, and Samuel J Gershman. Building machines that learn and think like people. Behavioral and Brain Sciences, 40:e253, 2017. 1
- [12] Antonia Creswell, Murray Shanahan, and Irina Higgins. Selection-inference: exploiting large language models for interpretable logical reasoning. In The Eleventh International Conference on Learning Representations, 2023. 1
- [13] Simon Frieder, Luca Pinchetti, Ryan-Rhys Griffiths, Tommaso Salvatori, Thomas Lukasiewicz, Philipp Petersen, and Julius Berner. Mathematical capabilities of ChatGPT. Advances in Neural Information Processing Systems, 36, 2024. 1


- [14] Simon Frieder, Jonas Bayer, Katherine M Collins, Julius Berner, Jacob Loader, András Juhász, Fabian Ruehle, Sean Welleck, Gabriel Poesia, Ryan-Rhys Griffiths, et al. Data for mathematical copilots: Better ways of presenting proofs for machine learning. arXiv preprint arXiv:2412.15184, 2024. 1
- [15] Anthony Brohan, Yevgen Chebotar, Chelsea Finn, Karol Hausman, Alexander Herzog, Daniel Ho, Julian Ibarz, Alex Irpan, Eric Jang, Ryan Julian, et al. Do as I can, not as I say: grounding language in robotic affordances. In Conference on Robot Learning, pages 287–318. PMLR, 2023. 1
- [16] Wenlong Huang, Pieter Abbeel, Deepak Pathak, and Igor Mordatch. Language models as zero-shot planners: Extracting actionable knowledge for embodied agents. In International Conference on Machine Learning, pages 9118–9147. PMLR, 2022. 1
- [17] Ishita Dasgupta, Christine Kaeser-Chen, Kenneth Marino, Arun Ahuja, Sheila Babayan, Felix Hill, and Rob Fergus. Collaborating with language models for embodied reasoning. In NeurIPS 2022 Foundation Models for Decision Making Workshop, 2022. 1
- [18] Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao. ReAct: synergizing reasoning and acting in language models. In International Conference on Learning Representations (ICLR), 2023. 1, 4, 6
- [19] Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao. Reflexion: Language agents with verbal reinforcement learning. Advances in Neural Information Processing Systems, 36, 2024. 1
- [20] Shibo Hao, Yi Gu, Haodi Ma, Joshua Hong, Zhen Wang, Daisy Wang, and Zhiting Hu. Reasoning with language model is planning with world model. In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, pages 8154–8173, 2023. 1
- [21] Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Tom Griffiths, Yuan Cao, and Karthik Narasimhan. Tree of thoughts: Deliberate problem solving with large language models. Advances in Neural Information Processing Systems, 36, 2024. 1
- [22] Joon Sung Park, Joseph O’Brien, Carrie Jun Cai, Meredith Ringel Morris, Percy Liang, and Michael S Bernstein. Generative agents: Interactive simulacra of human behavior. In Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology, pages 1–22, 2023. 1
- [23] Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, and Anima Anandkumar. Voyager: An open-ended embodied agent with large language models. Transactions on Machine Learning Research, 2024. 1
- [24] Mingchen Zhuge, Wenyi Wang, Louis Kirsch, Francesco Faccio, Dmitrii Khizbullin, and Jürgen Schmidhuber. GPTSwarm: Language agents as optimizable graphs. In Forty-first International Conference on Machine Learning, 2024. 1, 3
- [25] Mert Yuksekgonul, Federico Bianchi, Joseph Boen, Sheng Liu, Zhi Huang, Carlos Guestrin, and James Zou. TextGrad: Automatic" differentiation" via text. arXiv preprint arXiv:2406.07496, 2024. 1, 3
- [26] Ching-An Cheng, Allen Nie, and Adith Swaminathan. Trace is the New AutoDiff–unlocking efficient optimization of computational workflows. arXiv preprint arXiv:2406.16218, 2024. 1, 3
- [27] John Schulman, Nicolas Heess, Theophane Weber, and Pieter Abbeel. Gradient estimation using stochastic computation graphs. Advances in Neural Information Processing Systems, 28, 2015. 1, 4
- [28] Thomas Anthony, Zheng Tian, and David Barber. Thinking fast and slow with deep learning and tree search. In Proceedings of the 31st International Conference on Neural Information Processing Systems, pages 5366–5376,

2017. 2, 3, 5

- [29] Thomas William Anthony. Expert iteration. PhD thesis, UCL (University College London), 2021. 2, 3, 5
- [30] Alex Havrilla, Yuqing Du, Sharath Chandra Raparthy, Christoforos Nalmpantis, Jane Dwivedi-Yu, Maksym Zhuravinskyi, Eric Hambro, Sainbayar Sukhbaatar, and Roberta Raileanu. Teaching large language models to reason with reinforcement learning. arXiv preprint arXiv:2403.04642, 2024. 2, 3, 5
- [31] Jonathan Uesato, Nate Kushman, Ramana Kumar, Francis Song, Noah Siegel, Lisa Wang, Antonia Creswell, Geoffrey Irving, and Irina Higgins. Solving math word problems with process-and outcome-based feedback. arXiv preprint arXiv:2211.14275, 2022. 2
- [32] Hunter Lightman, Vineet Kosaraju, Yuri Burda, Harrison Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, and Karl Cobbe. Let’s verify step by step. In The Twelfth International Conference on Learning Representations, 2024. 2


- [33] Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, et al. Training verifiers to solve math word problems. arXiv preprint arXiv:2110.14168, 2021. 2, 3, 6
- [34] Zhilin Yang, Peng Qi, Saizheng Zhang, Yoshua Bengio, William Cohen, Ruslan Salakhutdinov, and Christopher D Manning. HotpotQA: A dataset for diverse, explainable multi-hop question answering. In Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing, pages 2369–2380, 2018. 2, 3, 6
- [35] Jon M Laurent, Joseph D Janizek, Michael Ruzo, Michaela M Hinks, Michael J Hammerling, Siddharth Narayanan, Manvitha Ponnapati, Andrew D White, and Samuel G Rodriques. LAB-Bench: Measuring capabilities of language models for biology research. arXiv preprint arXiv:2407.10362, 2024. 2, 6, 7, 10, 12
- [36] Jakub Lála, Odhran O’Donoghue, Aleksandar Shtedritski, Sam Cox, Samuel G Rodriques, and Andrew D White. PaperQA: Retrieval-augmented generative agent for scientific research. arXiv preprint arXiv:2312.07559, 2023. 2, 6
- [37] Michael D Skarlinski, Sam Cox, Jon M Laurent, James D Braza, Michaela Hinks, Michael J Hammerling, Manvitha Ponnapati, Samuel G Rodriques, and Andrew D White. Language agents achieve superhuman synthesis of scientific knowledge. arXiv preprint arXiv:2409.13740, 2024. 2, 3, 6, 10, 11, 12
- [38] Wenhao Gao, Sai Pooja Mahajan, Jeremias Sulam, and Jeffrey J. Gray. Deep learning in protein structural modeling and design. Patterns, 1(9):100142, December 2020. 2
- [39] Hamed Khakzad, Ilia Igashov, Arne Schneuing, Casper Goverde, Michael Bronstein, and Bruno Correia. A new age in protein design empowered by deep learning. Cell Systems, 14(11):925–939, 2023. 2
- [40] Kaixuan Huang, Yuanhao Qu, Henry Cousins, William A Johnson, Di Yin, Mihir Shah, Denny Zhou, Russ Altman, Mengdi Wang, and Le Cong. CRISPR-GPT: An LLM agent for automated design of gene-editing experiments. arXiv preprint arXiv:2404.18021, 2024. 2
- [41] Lilian Weng. LLM-powered autonomous agents. lilianweng.github.io, Jun 2023. 2
- [42] Thomas Carta, Clément Romac, Thomas Wolf, Sylvain Lamprier, Olivier Sigaud, and Pierre-Yves Oudeyer. Grounding large language models in interactive environments with online reinforcement learning. In International Conference on Machine Learning, pages 3676–3713. PMLR, 2023. 2, 4
- [43] Filippos Christianos, Georgios Papoudakis, Matthieu Zimmer, Thomas Coste, Zhihao Wu, Jingxuan Chen, Khyati Khandelwal, James Doran, Xidong Feng, Jiacheng Liu, et al. Pangu-Agent: A fine-tunable generalist agent with structured reasoning. arXiv preprint arXiv:2312.14878, 2023. 2, 4, 5
- [44] Muning Wen, Ziyu Wan, Weinan Zhang, Jun Wang, and Ying Wen. Reinforcing language agents via policy optimization with action decomposition. arXiv preprint arXiv:2405.15821, 2024. 2, 4
- [45] Muning Wen, Cheng Deng, Jun Wang, Weinan Zhang, and Ying Wen. Entropy-regularized token-level policy optimization for large language models. arXiv preprint arXiv:2402.06700, 2024. 2, 4
- [46] Dang Nguyen, Viet Dac Lai, Seunghyun Yoon, Ryan A Rossi, Handong Zhao, Ruiyi Zhang, Puneet Mathur, Nedim Lipka, Yu Wang, Trung Bui, et al. DynaSaur: Large language agents beyond predefined actions. arXiv preprint arXiv:2411.01747, 2024. 2
- [47] Yuanzhao Zhai, Tingkai Yang, Kele Xu, Feng Dawei, Cheng Yang, Bo Ding, and Huaimin Wang. Enhancing decision-making for LLM agents via step-level q-value models. arXiv preprint arXiv:2409.09345, 2024. 2
- [48] Yifan Song, Da Yin, Xiang Yue, Jie Huang, Sujian Li, and Bill Yuchen Lin. Trial and error: Exploration-based trajectory optimization for LLM agents. arXiv preprint arXiv:2403.02502, 2024. 2, 5
- [49] Yanxi Chen, Yaliang Li, Bolin Ding, and Jingren Zhou. On the Design and Analysis of LLM-Based Algorithms. arXiv preprint arXiv:2407.14788, 2024. 2
- [50] Harrison Chase. LangChain, October 2022. 3
- [51] Jerry Liu. LlamaIndex, November 2022. 3
- [52] Chi Wang, Xueqing Liu, and Ahmed Hassan Awadallah. Cost-effective hyperparameter optimization for large language model generation inference. In International Conference on Automated Machine Learning, pages 21–1. PMLR, 2023. 3
- [53] Taylor Shin, Yasaman Razeghi, Robert L Logan IV, Eric Wallace, and Sameer Singh. AutoPrompt: Eliciting knowledge from language models with automatically generated prompts. In Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP), pages 4222–4235, 2020. 3


- [54] Xiang Lisa Li and Percy Liang. Prefix-tuning: Optimizing continuous prompts for generation. In Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers), pages 4582–4597, 2021. 3
- [55] Menglin Jia, Luming Tang, Bor-Chun Chen, Claire Cardie, Serge Belongie, Bharath Hariharan, and Ser-Nam Lim. Visual prompt tuning. In European Conference on Computer Vision, pages 709–727. Springer, 2022. 3
- [56] Xiang Chen, Ningyu Zhang, Xin Xie, Shumin Deng, Yunzhi Yao, Chuanqi Tan, Fei Huang, Luo Si, and Huajun Chen. Knowprompt: Knowledge-aware prompt-tuning with synergistic optimization for relation extraction. In Proceedings of the ACM Web conference 2022, pages 2778–2788, 2022. 3
- [57] Guanghui Qin and Jason Eisner. Learning how to ask: Querying lms with mixtures of soft prompts. In Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, pages 5203–5212, 2021. 3
- [58] Qingyan Guo, Rui Wang, Junliang Guo, Bei Li, Kaitao Song, Xu Tan, Guoqing Liu, Jiang Bian, and Yujiu Yang. Connecting large language models with evolutionary algorithms yields powerful prompt optimizers. In The Twelfth International Conference on Learning Representations, 2024. 3
- [59] Ruotian Ma, Xiaolei Wang, Xin Zhou, Jian Li, Nan Du, Tao Gui, Qi Zhang, and Xuanjing Huang. Are large language models good prompt optimizers? arXiv preprint arXiv:2402.02101, 2024. 3
- [60] Tuo Zhang, Jinyue Yuan, and Salman Avestimehr. Revisiting OPRO: The Limitations of Small-Scale LLMs as Optimizers. arXiv preprint arXiv:2405.10276, 2024. 3
- [61] Jiale Cheng, Xiao Liu, Kehan Zheng, Pei Ke, Hongning Wang, Yuxiao Dong, Jie Tang, and Minlie Huang. Black-box prompt optimization: Aligning large language models without model training. arXiv preprint arXiv:2311.04155, 2023. 3
- [62] Chengrun Yang, Xuezhi Wang, Yifeng Lu, Hanxiao Liu, Quoc V Le, Denny Zhou, and Xinyun Chen. Large language models as optimizers. In The Twelfth International Conference on Learning Representations, 2024. 3
- [63] Xiaoqiang Lin, Zhongxiang Dai, Arun Verma, See-Kiong Ng, Patrick Jaillet, and Bryan Kian Hsiang Low. Prompt optimization with human feedback. arXiv preprint arXiv:2405.17346, 2024. 3
- [64] Wenyang Hu, Yao Shu, Zongmin Yu, Zhaoxuan Wu, Xiangqiang Lin, Zhongxiang Dai, See-Kiong Ng, and Bryan Kian Hsiang Low. Localized zeroth-order prompt optimization. arXiv preprint arXiv:2403.02993, 2024. 3
- [65] Zhaoxuan Wu, Xiaoqiang Lin, Zhongxiang Dai, Wenyang Hu, Yao Shu, See-Kiong Ng, Patrick Jaillet, and Bryan Kian Hsiang Low. Prompt optimization with EASE? Efficient ordering-aware automated selection of exemplars. arXiv preprint arXiv:2405.16122, 2024. 3
- [66] Xiaoqiang Lin, Zhaoxuan Wu, Zhongxiang Dai, Wenyang Hu, Yao Shu, See-Kiong Ng, Patrick Jaillet, and Bryan Kian Hsiang Low. Use your INSTINCT: INSTruction optimization for LLMs using neural bandits coupled with transformers. In Forty-first International Conference on Machine Learning, 2024. 3
- [67] Lichang Chen, Jiuhai Chen, Tom Goldstein, Heng Huang, and Tianyi Zhou. InstructZero: Efficient instruction optimization for black-box large language models. In Forty-first International Conference on Machine Learning,

2024. 3

- [68] Yongchao Zhou, Andrei Ioan Muresanu, Ziwen Han, Keiran Paster, Silviu Pitis, Harris Chan, and Jimmy Ba. Large language models are human-level prompt engineers. In The Eleventh International Conference on Learning Representations, 2023. 3
- [69] Reid Pryzant, Dan Iter, Jerry Li, Yin Tat Lee, Chenguang Zhu, and Michael Zeng. Automatic prompt optimization with ”gradient descent” and beam search. In The 2023 Conference on Empirical Methods in Natural Language Processing, 2023. 3
- [70] Antonio Sabbatella, Andrea Ponti, Ilaria Giordani, Antonio Candelieri, and Francesco Archetti. Prompt optimization in large language models. Mathematics, 12(6):929, 2024. 3
- [71] Yuyan Chen, Zhihao Wen, Ge Fan, Zhengyu Chen, Wei Wu, Dayiheng Liu, Zhixu Li, Bang Liu, and Yanghua Xiao. MAPO: Boosting large language model performance with model-adaptive prompt optimization. In The 2023 Conference on Empirical Methods in Natural Language Processing, 2023. 3
- [72] Xinyuan Wang, Chenxi Li, Zhen Wang, Fan Bai, Haotian Luo, Jiayou Zhang, Nebojsa Jojic, Eric Xing, and Zhiting Hu. PromptAgent: Strategic planning with language models enables expert-level prompt optimization. In The Twelfth International Conference on Learning Representations, 2024. 3
- [73] Oscar Mañas, Pietro Astolfi, Melissa Hall, Candace Ross, Jack Urbanek, Adina Williams, Aishwarya Agrawal, Adriana Romero-Soriano, and Michal Drozdzal. Improving text-to-image consistency via automatic prompt optimization. arXiv preprint arXiv:2403.17804, 2024. 3


- [74] Xuan Long Do, Yiran Zhao, Hannah Brown, Yuxi Xie, James Xu Zhao, Nancy F Chen, Kenji Kawaguchi, Michael Shieh, and Junxian He. Prompt optimization via adversarial in-context learning. arXiv preprint arXiv:2312.02614, 2023. 3
- [75] Alessandro Sordoni, Eric Yuan, Marc-Alexandre Côté, Matheus Pereira, Adam Trischler, Ziang Xiao, Arian Hosseini, Friederike Niedtner, and Nicolas Le Roux. Joint prompt optimization of stacked LLMs using variational inference. Advances in Neural Information Processing Systems, 36, 2024. 3
- [76] Antonio Sabbatella, Andrea Ponti, Antonio Candelieri, Ilaria Giordani, and Francesco Archetti. A Bayesian approach for prompt optimization in pre-trained language models. arXiv preprint arXiv:2312.00471, 2023. 3
- [77] Yuxin Wen, Neel Jain, John Kirchenbauer, Micah Goldblum, Jonas Geiping, and Tom Goldstein. Hard prompts made easy: Gradient-based discrete optimization for prompt tuning and discovery. Advances in Neural Information Processing Systems, 36, 2024. 3
- [78] Qinyuan Ye, Maxamed Axmed, Reid Pryzant, and Fereshte Khani. Prompt engineering a prompt engineer. arXiv preprint arXiv:2311.05661, 2023. 3
- [79] Shirley Wu, Shiyu Zhao, Qian Huang, Kexin Huang, Michihiro Yasunaga, Kaidi Cao, Vassilis N Ioannidis, Karthik Subbian, Jure Leskovec, and James Zou. AvaTaR: Optimizing LLM agents for tool-assisted knowledge retrieval. arXiv preprint arXiv:2406.11200, 2024. 3
- [80] Changle Qu, Sunhao Dai, Xiaochi Wei, Hengyi Cai, Shuaiqiang Wang, Dawei Yin, Jun Xu, and Ji-Rong Wen. Tool learning with large language models: A survey. arXiv preprint arXiv:2405.17935, 2024. 3
- [81] Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Eric Hambro, Luke Zettlemoyer, Nicola Cancedda, and Thomas Scialom. Toolformer: Language models can teach themselves to use tools. Advances in Neural Information Processing Systems, 36, 2024. 3
- [82] Yujia Qin, Shengding Hu, Yankai Lin, Weize Chen, Ning Ding, Ganqu Cui, Zheni Zeng, Yufei Huang, Chaojun Xiao, Chi Han, et al. Tool learning with foundation models. arXiv preprint arXiv.2304.08354, 10, 2023. 3
- [83] Da Yin, Faeze Brahman, Abhilasha Ravichander, Khyathi Chandu, Kai-Wei Chang, Yejin Choi, and Bill Yuchen Lin. Agent Lumos: Unified and modular training for open-source language agents. In Lun-Wei Ku, Andre Martins, and Vivek Srikumar, editors, Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 12380–12403, Bangkok, Thailand, August 2024. Association for Computational Linguistics. 3, 5
- [84] Wangchunshu Zhou, Yixin Ou, Shengwei Ding, Long Li, Jialong Wu, Tiannan Wang, Jiamin Chen, Shuai Wang, Xiaohua Xu, Ningyu Zhang, et al. Symbolic learning enables self-evolving agents. arXiv preprint arXiv:2406.18532, 2024. 3
- [85] Shengran Hu, Cong Lu, and Jeff Clune. Automated design of agentic systems. arXiv preprint arXiv:2408.08435,

2024. 3

- [86] Omar Khattab, Keshav Santhanam, Xiang Lisa Li, David Hall, Percy Liang, Christopher Potts, and Matei Zaharia. Demonstrate-search-predict: Composing retrieval and language models for knowledge-intensive NLP. arXiv preprint arXiv:2212.14024, 2022. 3
- [87] Arnav Singhvi, Manish Shetty, Shangyin Tan, Christopher Potts, Koushik Sen, Matei Zaharia, and Omar Khattab. DSPy assertions: Computational constraints for self-refining language model pipelines. arXiv preprint arXiv:2312.13382, 2023. 3
- [88] Omar Khattab, Arnav Singhvi, Paridhi Maheshwari, Zhiyuan Zhang, Keshav Santhanam, Saiful Haq, Ashutosh Sharma, Thomas T Joshi, Hanna Moazam, Heather Miller, et al. DSPy: Compiling Declarative Language Model Calls into State-of-the-Art Pipelines. In The Twelfth International Conference on Learning Representations,

2024. 3

- [89] Jun Wang, Meng Fang, Ziyu Wan, Muning Wen, Jiachen Zhu, Anjie Liu, Ziqin Gong, Yan Song, Lei Chen, Lionel M Ni, et al. OpenR: An open source framework for advanced reasoning with large language models. arXiv preprint arXiv:2410.09671, 2024. 3
- [90] Qian Huang, Jian Vora, Percy Liang, and Jure Leskovec. MLAgentBench: Evaluating language agents on machine learning experimentation. In Forty-first International Conference on Machine Learning, 2024. 3
- [91] Siyuan Guo, Cheng Deng, Ying Wen, Hechang Chen, Yi Chang, and Jun Wang. DS-Agent: Automated data science by empowering large language models with case-based reasoning. arXiv preprint arXiv:2402.17453,


2024. 3

- [92] Antoine Grosnit, Alexandre Maraval, James Doran, Giuseppe Paolo, Albert Thomas, Refinath Shahul Hameed Nabeezath Beevi, Jonas Gonzalez, Khyati Khandelwal, Ignacio Iacobacci, Abdelhakim Benechehab, et al. Large language models orchestrating structured reasoning achieve Kaggle grandmaster level. arXiv preprint arXiv:2411.03562, 2024. 3
- [93] Xueyu Hu, Ziyu Zhao, Shuang Wei, Ziwei Chai, Qianli Ma, Guoyin Wang, Xuwu Wang, Jing Su, Jingjing Xu, Ming Zhu, et al. InfiAgent-DABench: Evaluating agents on data analysis tasks. In Forty-first International Conference on Machine Learning, 2024. 3
- [94] Jinyang Li, Nan Huo, Yan Gao, Jiayi Shi, Yingxiu Zhao, Ge Qu, Yurong Wu, Chenhao Ma, Jian-Guang Lou, and Reynold Cheng. Tapilot-Crossing: Benchmarking and evolving llms towards interactive data analysis agents. arXiv preprint arXiv:2403.05307, 2024. 3
- [95] Xiao Liu, Zirui Wu, Xueqing Wu, Pan Lu, Kai-Wei Chang, and Yansong Feng. Are LLMs capable of data-based statistical and causal reasoning? benchmarking advanced quantitative reasoning with data. arXiv preprint arXiv:2402.17644, 2024. 3
- [96] Zhijing Jin, Yuen Chen, Felix Leeb, Luigi Gresele, Ojasv Kamal, Zhiheng LYU, Kevin Blin, Fernando Gonzalez Adauto, Max Kleiman-Weiner, Mrinmaya Sachan, and Bernhard Schölkopf. CLadder: A benchmark to assess causal reasoning capabilities of language models. In Thirty-seventh Conference on Neural Information Processing Systems, 2023. 3
- [97] Bodhisattwa Prasad Majumder, Harshit Surana, Dhruv Agarwal, Bhavana Dalvi Mishra, Abhijeetsingh Meena, Aryan Prakhar, Tirth Vora, Tushar Khot, Ashish Sabharwal, and Peter Clark. DiscoveryBench: Towards data-driven discovery with large language models. arXiv preprint arXiv:2407.01725, 2024. 3
- [98] Adrian Mirza, Nawaf Alampara, Sreekanth Kunchapu, Benedict Emoekabu, Aswanth Krishnan, Mara Wilhelmi, Macjonathan Okereke, Juliane Eberhardt, Amir Mohammad Elahi, Maximilian Greiner, et al. Are large language models superhuman chemists? arXiv preprint arXiv:2404.01475, 2024. 3
- [99] Ken Gu, Ruoxi Shang, Ruien Jiang, Keying Kuang, Richard-John Lin, Donghe Lyu, Yue Mao, Youran Pan, Teng Wu, Jiaqian Yu, et al. BLADE: Benchmarking language model agents for data-driven science. In Empirical Methods in Natural Language Processing, 2024. 3
- [100] Yubo Ma, Zhibin Gou, Junheng Hao, Ruochen Xu, Shuohang Wang, Liangming Pan, Yujiu Yang, Yixin Cao, and Aixin Sun. SciAgent: Tool-augmented language models for scientific reasoning. In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, 2024. 3
- [101] Peter Jansen, Marc-Alexandre Côté, Tushar Khot, Erin Bransom, Bhavana Dalvi Mishra, Bodhisattwa Prasad Majumder, Oyvind Tafjord, and Peter Clark. DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents. In Advances in Neural Information Processing Systems,

2024. 3

- [102] Ruoyao Wang, Peter Jansen, Marc-Alexandre Côté, and Prithviraj Ammanabrolu. ScienceWorld: Is your agent smarter than a 5th grader? In Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing, pages 11279–11298, 2022. 3
- [103] Mayk Caldas Ramos, Christopher Collison, and Andrew D White. A review of large language models and autonomous agents in chemistry. Chemical Science, 2024. 3
- [104] Karl Johan Åström. Optimal control of Markov processes with incomplete state information I. Journal of Mathematical Analysis and Applications, 10:174–205, 1965. 3
- [105] SC Kleene. Representation of events in nerve nets and finite automata. Automata Studies: Annals of Mathematics Studies. Number 34, 34:3, 1956. 3
- [106] Clara Meister, Tiago Pimentel, Gian Wiher, and Ryan Cotterell. Locally typical sampling. Transactions of the Association for Computational Linguistics, 11:102–121, 2023. 3
- [107] Yue Wu, Yewen Fan, Paul Pu Liang, Amos Azaria, Yuanzhi Li, and Tom M Mitchell. Read and reap the rewards: Learning to play Atari with the help of instruction manuals. Advances in Neural Information Processing Systems, 36, 2024. 4
- [108] B Widrow and FW Smith. Computer and Information Sciences, chapter Pattern recognising control systems. Clever Hume Press, 1964. 4
- [109] Roger A Chambers and Donald Michie. Man-machine co-operation on a learning task. Computer Graphics: Techniques and Applications, pages 179–186, 1969. 4
- [110] Dean A Pomerleau. ALVINN: An autonomous land vehicle in a neural network. Advances in neural information processing systems, 1, 1988. 4


- [111] D. Michie, M. Bain, and J. Hayes-Michie. Cognitive models from subcognitive skills, chapter Chapter 5, pages 71–99. The Institution of Engineering and Technology, 1990. 5
- [112] Michael Bain and Claude Sammut. A framework for behavioural cloning. Machine Intelligence, 15:103–129,

1995. 5

- [113] Baian Chen, Chang Shu, Ehsan Shareghi, Nigel Collier, Karthik Narasimhan, and Shunyu Yao. FireAct: Toward language agent fine-tuning. arXiv preprint arXiv:2310.05915, 2023. 5
- [114] Aohan Zeng, Mingdao Liu, Rui Lu, Bowen Wang, Xiao Liu, Yuxiao Dong, and Jie Tang. AgentTuning: Enabling generalized agent abilities for LLMs. arXiv preprint arXiv:2310.12823, 2023. 5
- [115] Zheng Yuan, Hongyi Yuan, Chengpeng Li, Guanting Dong, Keming Lu, Chuanqi Tan, Chang Zhou, and Jingren Zhou. Scaling relationship on learning mathematical reasoning with large language models. arXiv preprint arXiv:2308.01825, 2023. 5
- [116] Bradley Brown, Jordan Juravsky, Ryan Ehrlich, Ronald Clark, Quoc V Le, Christopher Ré, and Azalia Mirhoseini. Large language monkeys: Scaling inference compute with repeated sampling. arXiv preprint arXiv:2407.21787,

2024. 5, 8

- [117] Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V Le, Ed H. Chi, Sharan Narang, Aakanksha Chowdhery, and Denny Zhou. Self-consistency improves chain of thought reasoning in language models. In The Eleventh International Conference on Learning Representations, 2023. 5
- [118] Yujia Li, David Choi, Junyoung Chung, Nate Kushman, Julian Schrittwieser, Rémi Leblond, Tom Eccles, James Keeling, Felix Gimeno, Agustin Dal Lago, et al. Competition-level code generation with alphacode. Science, 378(6624):1092–1097, 2022. 5
- [119] Quickwit Inc. tantivy, October 2024. 6
- [120] Alessandro Bertero, Stephanie Brown, and Ludovic Vallier. Methods of Cloning, page 19–39. Elsevier, 2017. 6
- [121] Kamal Sharma, Ajay Kumar Mishra, Vikram Mehraj, and Ganesh Selvaraj Duraisamy. Advances and applications of molecular cloning in clinical microbiology. Biotechnology and Genetic Engineering Reviews, 30(1):65–78,

2014. 6

- [122] Martin Steinegger and Johannes Söding. MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature Biotechnology, 35(11):1026–1028, 2017. 6
- [123] Roger A Sheldon and John M Woodley. Role of biocatalysis in sustainable chemistry. Chemical reviews, 118(2):801–838, 2018. 7
- [124] Adi Goldenzweig and Sarel J Fleishman. Principles of protein stability and their application in computational design. Annu. Rev. Biochem., 87:105–129, June 2018. 7
- [125] Henry Dieckhaus, Michael Brocidiacono, Nicholas Z. Randolph, and Brian Kuhlman. Transfer learning to leverage larger datasets for improved prediction of protein stability changes. Proceedings of the National Academy of Sciences, 121(6):e2314853121, 2024. 7
- [126] Aron Broom, Kyle Trainor, Zachary Jacobi, and Elizabeth M. Meiering. Computational modeling of protein stability: Quantitative analysis reveals solutions to pervasive problems. Structure, 28(6):717–726.e3, 2020. 7
- [127] Josef Laimer, Heidi Hofer, Marko Fritz, Stefan Wegenkittl, and Peter Lackner. MAESTRO–multi agent stability prediction upon point mutations. BMC Bioinformatics, 16(1):116, April 2015. 7
- [128] Timothy M Lauer, Neeraj J Agrawal, Naresh Chennamsetty, Kamal Egodage, Bernhard Helk, and Bernhardt L Trout. Developability index: a rapid in silico tool for the screening of antibody aggregation propensity. J. Pharm. Sci., 101(1):102–115, January 2012. 7
- [129] 310.ai. 310 copilot. 2024. 7
- [130] Alireza Ghafarollahi and Markus J Buehler. ProtAgents: protein discovery via large language model multi-agent collaborations combining physics and machine learning. Digital Discovery, 2024. 7
- [131] John B. Ingraham, Maxim Baranov, Zak Costello, et al. Illuminating protein space with a programmable generative model. Nature, 623:1070–1078, 2023. 7
- [132] Ruidong Wu, Fan Ding, Rui Wang, Rui Shen, Xiwen Zhang, Shitong Luo, Chenpeng Su, Zuofan Wu, Qi Xie, Bonnie Berger, Jianzhu Ma, and Jian Peng. High-resolution de novo structure prediction from primary sequence. bioRxiv, 2022. 7
- [133] Angelica Chen, Samuel D Stanton, Robert G Alberstein, Andrew M Watkins, Richard Bonneau, Vladimir Gligorijevi, Kyunghyun Cho, and Nathan C Frey. LLMs are highly-constrained biophysical sequence optimizers. arXiv preprint arXiv:2410.22296, 2024. 7


- [134] Kotaro Tsuboyama, Justas Dauparas, Jonathan Chen, Elodie Laine, Yasser Mohseni Behbahani, Jonathan J. Weinstein, Niall M. Mangan, Sergey Ovchinnikov, and Gabriel J. Rocklin. Mega-scale experimental analysis of protein folding stability in biology and design. Nature, 620(7973):434–444, Aug 2023. 7
- [135] Brandon Frenz, Steven M Lewis, Indigo King, Frank DiMaio, Hahnbeom Park, and Yifan Song. Prediction of protein mutational free energy: Benchmark and sampling improvements increase classification accuracy. Front. Bioeng. Biotechnol., 8:558247, October 2020. 7
- [136] Anthropic. Introducing the next generation of Claude, 2024. https://www.anthropic.com/news/claude-3-family. 7, 8
- [137] Iman Mirzadeh, Keivan Alizadeh, Hooman Shahrokhi, Oncel Tuzel, Samy Bengio, and Mehrdad Farajtabar. GSM-symbolic: Understanding the limitations of mathematical reasoning in large language models. arXiv preprint arXiv:2410.05229, 2024. 8
- [138] Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, and Aiesha Letman et. al. The Llama 3 herd of models, 2024. 8
- [139] UK AI Safety Institute US AI Safety Institute. Pre-deployment evaluation of Anthropic’s upgraded Claude 3.5 Sonnet. Technical Report, 2024. 11
- [140] BIG bench authors. Beyond the imitation game: Quantifying and extrapolating the capabilities of language models. Transactions on Machine Learning Research, 2023. 12


### A Environment Details

Table A1: Environments implemented within the Aviary framework.

|PaperQA| |
|---|---|
|Task|LitQA2 questions|
|Example Task Element<br><br>|Q: Which base editor has been shown to be the most efficient for inducing the mutation K352E in CD45 in human T-cells?<br><br>Options:<br><br>A) ABE8e-NG<br>B) ABE8e–SpRY<br>C) SPACE-NG<br>D) Insufficient information to answer this question<br>E) ABE8e-SpG Answer:<br>|
|Tools<br><br>|• paper_search(query: str, min_year: int | None, max_year: int | None) Full-text semantic search through a local search index.<br>• gather_evidence(question: str) - Perform LLM reranking and contextual summarization given a question on paper_search results.<br>• gen_answer() - Attempt to answer given the top ranked contextual summaries.<br>• complete(has_successful_answer: bool) - Terminate using the last proposed answer, with the argument declaring if the answer addressed all parts of the question.<br>|
|Reward R| <br><br><br><br>1 correct answer, −1 incorrect answer, 0.1 unsure answer.|
|Transition Function T|Nondeterministic, due to the stochastic nature of LLM prompting within both the gather_evidence and gen_answer tools.|
|Code|paper-qa==5.6.1|
|HOTPOTQA| |
|Task|HOTPOTQA questions|
|Example Task Element|A robe takes 2 bolts of blue fiber and half that much white fiber. How many bolts in total does it take?|
|Tools<br><br>|• search(entity: str) - Search Wikipedia for an entity, keeping either matching sentences or most similar pages.<br>• lookup(keyword: str) - Keyword lookup within all search results, emulating the “find” functionality of a web browser.<br>• submit_answer(answer: str) - Check if an answer is correct.<br>|
|Reward R<br><br>|1 correct answer, 0 otherwise.|
|Transition Function T<br><br>|Deterministic.|
|Code|aviary.gsm8k==0.11.0|
|GSM8k| |
|Task|GSM8k questions|
|Example Task Element<br><br>|Weng earns $12 an hour for babysitting. Yesterday, she just did 50 minutes of babysitting. How much did she earn?|


|Tools|• calculator(expr: str) - Return the result of a numerical expression.<br>• submit_answer(answer: str) - Check if an answer is correct.<br>|
|---|---|
|Reward R| <br><br><br><br>1 correct answer, −1 invalid tool call, 0 otherwise.|
|Transition Function T|Deterministic.|
|Code|aviary.hotpotqa==0.11.0|
|Molecular Cloning| |
|Task<br><br>|SeqQA questions|
|Example Task Element|Q: Which of the following RNA sequences contains an ORF that is most likely to have high translation efficiency in a human cell?<br><br>Options:<br><br>A) [RNA sequence]<br>B) [RNA sequence]<br>C) Insufficient information to answer this question<br>D) [RNA sequence]<br>E) [RNA sequence]<br>|


|Tools|• search(query: str) - Search Plasmid and NCBI nucleotide databases.<br>• annotate(sequence: Sequence) - Annotate proteins, ORFs, restriction sites in a DNA sequence.<br>• gibson(sequences: list[Sequence]) - Simulate gibson assembly.<br>• goldengate(sequences: list[Sequence], enzyme: str) - Simulate golden gate assembly/<br>• simulate_pcr(sequence: Sequence, forward_primer: Sequence | None, forward_primer_name: str | None) - Simulate polymerase chain reaction.<br>• optimize_translation(sequence: Sequence, cg_content: int, codon_table: int, min_repeat_length: int) - Codon optimization.<br>• separate(sequences: list[Sequence]) - Simulate gel electrophoresis.<br>• enzyme_cut(sequence: Sequence, enzyme: str) - Simulate restriction digest.<br>• search(query: str) - Search Plasmid and NCBI nucleotide databases.<br>• annotate(sequence: Sequence) - Annotate proteins, ORFs, restriction sites in a DNA sequence.<br>• gibson(sequences: list[Sequence]) - Simulate gibson assembly.<br>• goldengate(sequences: list[Sequence], enzyme: str) - Simulate golden gate assembly.<br>• simulate_pcr(sequence: Sequence, forward_primer: Sequence | None, forward_primer_name: str | None) - Simulate polymerase chain reaction. Primers can be sequence (by ref) or name of enzyme or sequence value.<br>• optimize_translation(sequence: Sequence, cg_content: int, codon_table: int, min_repeat_length: int) - Codon optimization.<br>• separate(sequences: list[Sequence]) - Simulate gel electrophoresis.<br>• enzyme_cut(sequence: Sequence, enzyme: str) - Simulate restriction digest.<br>• find_sequence_overlap(sequence1: Sequence, sequence2: Sequence, reverse: bool) - Find overlapping regions between two sequences.<br>• find_orfs(sequence: Sequence, min_length: int, codon_table: int, strand: int) - Find open reading frames in a DNA sequence.<br>• design_primers(sequence: Sequence, target_tm: float, forward_overhang_name: str, reverse_overhang_name: str) - Design PCR primers for a sequence.<br>• merge(sequences: list[Sequence]) - Combine multiple sequences, needed to do assembly simulation.<br>• add(sequence1: Sequence, sequence2: Sequence) - Add two sequences together.<br>• slice_sequence(sequence: Sequence, start: int, end: int, name: str)<br><br>- Extract a subsequence.<br><br>• view_translation(sequence: Sequence) - View the amino acid translation of a DNA sequence.<br>• view_sequence_stats(sequence: Sequence) - View sequence statistics.<br>• view_restriction_sites(sequence: Sequence) - View restriction enzyme cut sites.<br>• view_sequence(sequence: Sequence) - View the raw sequence.<br>• submit_answer(answer: str)<br>|
|---|---|


|Reward R<br><br>| <br><br><br><br>1 correct answer, −1 incorrect answer, 0.1 unsure answer.|
|---|---|
|Transition Function T<br><br>|Deterministic.|
|Protein Design| |
|Task|Protein Stability|
|Example Task|Design at least 3 mutations and a maximum of 7 mutations to the protein sequence {sequence} that would improve its stability. The sequence of this protein is provided in the text file located at {local_txt_file}, and the structure of the protein can be found in the PDB file located at {local_pdb_file}.|
|Tools|• get_bond_types_between(residues: list[int], bond_type: str) - Describes all instances of the specified bond type among a given list of residues as outlined in the function description.<br>• get_secondary_structure(pdb_string: str) - Describes secondary structure elements found in the protein structure by residue.<br>• get_sequence_properties(mutations: list[str], return_wt: bool) - Describes properties like instability index, molar extinction coefficient, fraction of charged residues, iso-electric point.<br>• get_distance_between_residues(mutation: list[str]) - Get pairwise distances between list of residues.<br>• get_residue_at_position(residues: list[int]) - Returns the residue present at a specific position and describes whether it is acidic or basic or charged, polar or aliphatic or aromatic.<br>• get_hydrophobicity_score(local_pdb_file: str) - Calculates aggregation propensity by residue using Rosetta.<br>• get_mutant_protein_sequence(mutations: list[str]) - Returns the sequence of the protein after the mutations are applied to the sequence.<br>|
|Reward R|1 RosettaddG < 0, 0 otherwise.|
|Transition Function T<br><br>|Deterministic.|


