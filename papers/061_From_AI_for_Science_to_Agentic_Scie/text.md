## arXiv:2508.14111v2[cs.LG]20 Oct 2025

![image 1](Wei et al._2025_From AI for Science to Agentic Science A Survey on Autonomous Scientific Discovery_images/imageFile1.png)

![image 2](Wei et al._2025_From AI for Science to Agentic Science A Survey on Autonomous Scientific Discovery_images/imageFile2.png)

# From AI for Science to Agentic Science: A Survey on Autonomous Scientific Discovery

Jiaqi Wei1,2∗, Yuejin Yang1,3∗, Xiang Zhang4∗, Yuhan Chen1,5∗, Xiang Zhuang1,2∗, Zhangyang Gao1∗, Dongzhan Zhou1∗, Guangshuai Wang1,3, Zhiqiang Gao1, Juntai Cao4, Zijie Qiu1,3, Ming Hu1, Chenglong Ma1,3, Shixiang Tang1, Junjun He1, Chunfeng Song1, Xuming He1,2, Qiang Zhang2, Chenyu You8, Shuangjia Zheng7,10, Ning Ding10, Wanli Ouyang1,6, Nanqing Dong1, Yu Cheng1,6, Siqi Sun1,3†, Lei Bai1†, Bowen Zhou1,10†

1 Shanghai Artificial Intelligence Laboratory, 2 Zhejiang University, 3 Fudan University, 4 University of British Columbia, 5 Tongji University, 6 The Chinese University of Hong Kong 7 Shanghai Jiaotong University, 8 Stony Brook University, 9 Lingang Laboratory, 10 Tsinghua University

#### Abstract:

Artificial intelligence (AI) is reshaping scientific discovery, evolving from specialized computational tools into autonomous research partners. We position Agentic Science as a pivotal stage within the broader AI for Science paradigm, where AI systems progress from partial assistance to full scientific agency. Enabled by large language models (LLMs), multimodal systems, and integrated research platforms, agentic AI exhibits capabilities in hypothesis generation, experimental design, execution, analysis, and iterative refinement-behaviors once regarded as uniquely human. This survey offers a domain-oriented review of autonomous scientific discovery across life sciences, chemistry, materials, and physics, synthesizing research progress and advances within each discipline. We unify three previously fragmented perspectives-process-oriented, autonomy-oriented, and mechanism-oriented-through a comprehensive framework that connects foundational capabilities, core processes, and domain-specific realizations. Building on this framework, we (i) trace the evolution of AI for Science, (ii) identify five core capabilities underpinning scientific agency, (iii) model discovery as a dynamic four-stage workflow, (iv) review applications across life sciences, chemistry, materials science, and physics, and (v) synthesize key challenges and future opportunities. This work establishes a domain-oriented synthesis of autonomous scientific discovery and positions Agentic Science as a structured paradigm for advancing AI-driven research.

Keywords: Agentic Science, Autonomous Scientific Discovery, Natural Sciences, AI for Science, Agentic AI, Large Language Models

###### *: These authors contributed equally †: These authors jointly led the project

Homepage: https://agenticscience.github.io/

Github Repository: https://github.com/AgenticScience/Awesome-Agent-Scientists

### Contents

- 1 Introduction 4
- 2 The Evolution of AI for Science: From Tools to Autonomous Partners 5

- 2.1 The Evolution of AI for Science . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6

- 2.1.1 Level 1: AI as a Computational Oracle (Expert Tools) . . . . . . . . . . . . . . . . . . 6
- 2.1.2 Level 2: AI as an Automated Research Assistant (Partial Agentic Discovery) . . . . . . 7
- 2.1.3 Level 3: AI as an Autonomous Scientific Partner (Full Agentic Discovery) . . . . . . . 7
- 2.1.4 Level 4: AI as a Generative Architect (Future Prospect) . . . . . . . . . . . . . . . . . 8


- 2.2 The Human Scientist’s Evolving Role . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
- 2.3 Agentic Science: The Focus of This Survey . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
- 2.4 Modern Scientific Large Language Models for Agentic Science . . . . . . . . . . . . . . . . . 10


- 3 Scientific Agents: Core Abilities and Challenges 11

- 3.1 Planning and Reasoning Engines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
- 3.2 Tool Use and Integration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
- 3.3 Memory Mechanisms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
- 3.4 Collaboration between Agents . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
- 3.5 Optimization and Evolution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19


- 4 Agentic Science: Dynamic Workflow and Challenges 21

- 4.1 Observation and Hypothesis Generation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
- 4.2 Experimental Planning and Execution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
- 4.3 Data and Result Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
- 4.4 Synthesis, Validation, and Evolution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
- 4.5 Fully Autonomous Research Pipeline . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25


- 5 Agentic Life Sciences Research 27


- 5.1 General Frameworks and Methodologies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
- 5.2 Genomics, Transcriptomics, and Multi-Omics Analysis . . . . . . . . . . . . . . . . . . . . . . 30
- 5.3 Protein Science and Engineering . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
- 5.4 Drug and Therapeutic Discovery . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31


##### 6 Agentic Chemistry Research 33

- 6.1 General Frameworks and Methodologies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
- 6.2 Organic Synthesis and Reaction Optimization . . . . . . . . . . . . . . . . . . . . . . . . . . 35
- 6.3 Generative Chemistry and Molecular Design . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
- 6.4 Computational and Quantum Chemistry . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37


##### 7 Agentic Materials Science Research 37

- 7.1 General Methodologies and Discovery Platforms . . . . . . . . . . . . . . . . . . . . . . . . . 38
- 7.2 Design and Discovery of Novel Materials . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
- 7.3 Automated Simulation and Characterization . . . . . . . . . . . . . . . . . . . . . . . . . . . 40


##### 8 Agentic Physics and Astronomy Research 42

- 8.1 General Frameworks and Methodologies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
- 8.2 Astronomy and Cosmology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
- 8.3 Computational Mechanics and Fluid Dynamics . . . . . . . . . . . . . . . . . . . . . . . . . . 44
- 8.4 Quantum Computing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45


##### 9 Challenges in Agentic Science 45

- 9.1 Agentic Reproducibility and Reliability . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
- 9.2 Validation of Novelty . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
- 9.3 Transparency in Scientific Reasoning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
- 9.4 Ethical and Societal Dimensions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47


##### 10 Future Outlook of Agentic Science 47

- 10.1 From Automation to Autonomous Invention . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
- 10.2 Interdisciplinary Synthesis at Scale . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
- 10.3 The Global Cooperation Research Agent . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
- 10.4 The Nobel-Turing Test . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49


##### 11 Conclusion 49

### 1. Introduction

Scientific discovery is experiencing a transformative shift, driven by the rapid evolution of artificial intelligence (AI) from specialized tools to collaborative research partners. This progression marks a pivotal stage in the AI for Science paradigm, where AI systems have moved from acting as computational oracles for targeted tasks [157, 392, 429, 61, 113, 353, 447] toward the emergence of Agentic Science (Figure 1) [288, 278, 106, 345, 203]. Agentic Science denotes a specific stage within AI for Science evolution-corresponding primarily to Level 3 (Full Agentic Discovery) with precursors at Level 2 (Partial Agentic Discovery) in Figure 1. In this stage, AI operates as an autonomous scientific agent capable of formulating hypotheses, designing and executing experiments, interpreting results, and iteratively refining theories with reduced dependence on human guidance [288, 30]. This advancement is enabled by integrated platforms such as Intern-Discovery, which grants access to diverse AI agents and datasets, and by multimodal models like Intern-S11, which demonstrate deep scientific reasoning.

This transformation is fueled by recent breakthroughs in foundational models, particularly large language models (LLMs) [107, 322, 447, 37, 17, 103], which provide unprecedented capabilities in natural language understanding, complex reasoning, and tool use [309, 443, 411, 428, 427]. These capabilities have enabled the development of AI agents that transcend static learning pipelines, acting instead as dynamic, goal-driven entities navigating the scientific method [397, 115, 229, 454]. From hypothesis generation [393, 267] to autonomous experimentation [30, 404] and synthetic dataset creation [194], these agents demonstrate emergent behaviors once considered exclusively human.

Comparison with Existing Surveys. Despite rapid progress, a unified framework for understanding and designing increasingly autonomous scientific systems remains absent. Existing surveys can be categorized along three complementary axes. Process-oriented perspectives map LLM capabilities onto the classical

1https://github.com/InternLM/Intern-S1

![image 9](Wei et al._2025_From AI for Science to Agentic Science A Survey on Autonomous Scientific Discovery_images/imageFile9.png)

- Figure 1: The Evolution of AI for Science. From computational tools to creative collaborators: the four-stage journey of AI in science. Agentic Science is a stage within AI for Science, aligning primarily with Level 3 (Full Agentic Discovery) and building on Level 2 (Partial Agentic Discovery).


research cycle [222, 448, 56]. Autonomy-oriented studies grade systems by their initiative and responsibility [441, 371]. Mechanism-oriented analyses dissect the architectural primitives and evolving roles that enable agentic behavior [278, 420, 106, 345]. While these contributions lay valuable foundations, they remain fragmented-treating workflows, autonomy scales, or architectures in isolation.

Our Contributions. In contrast to prior surveys, which examine process, autonomy, or architecture in isolation, our work integrates and extends these perspectives through the comprehensive framework shown in Figure 2. This framework connects foundational capabilities, core processes, and domain realizations within autonomous scientific discovery. We present a domain-oriented review of autonomous scientific discovery across life sciences, chemistry, materials, and physics, providing a detailed synthesis of research progress and discoveries within each discipline. This unified lens positions Agentic Science not merely as an abstract stage, but as a structured research paradigm spanning capabilities, processes, and applications. Our contributions are as follows:

- 1. Charting the Evolution of AI for Science. We trace the evolution from computational oracles to autonomous research partners, formally defining Agentic Science as the stage where AI systems display autonomy, goal-driven reasoning, and iterative learning.
- 2. The Anatomy of Scientific Agents: Five Core Capabilities. We identify and analyze the five foundational capabilities required for a scientific agent: (i) Reasoning and Planning, (ii) Tool Integration, (iii) Memory Mechanisms, (iv) Multi-Agent Collaboration, and (v) Optimization and Evolution. For each, we review state-of-the-art implementations (e.g., [219, 35, 242, 46]) and domain-specific challenges.
- 3. The Dynamic Workflow of Agentic Science: Four Core Stages. We model the scientific discovery process as a dynamic, four-stage workflow driven by agents: (i) Observation and Hypothesis Generation, (ii) Experimental Planning and Execution, (iii) Data and Result Analysis, and (iv) Synthesis, Validation, and Evolution. We emphasize that agents can flexibly and dynamically combine these stages to tackle complex scientific problems [14, 30, 97, 96].
- 4. Systematic Review Across Natural Sciences. We conduct a comprehensive review of agentic systems across the four major domains of natural science (Figure 4): life sciences, chemistry, materials, and physics. Our analysis spans more than a dozen distinct subfields, from drug discovery [404] to materials design [147], showcasing the broad applicability and domain-specific innovations of Agentic Science.
- 5. Challenges and Future Opportunities. We synthesize the principal technical, ethical, and philosophical challenges confronting the field–including reproducibility, validation of novel discoveries, and humanagent collaboration–and outline a research roadmap to guide the future development of robust, trustworthy, and impactful scientific agents.


Through this synthesis, we aim to establish a conceptual and methodological foundation for Agentic Science, guiding future research toward the design of AI systems that co-evolve with human inquiry to accelerate the frontiers of discovery.

### 2. The Evolution of AI for Science: From Tools to Autonomous Partners

The landscape of AI in science is undergoing a fundamental transformation, evolving from narrowly-scoped computational augmentation to autonomous, end-to-end inquiry. This progression can be understood as an evolution through distinct levels of autonomy and capability, beginning with AI as a specialized tool and advancing towards AI as an autonomous scientific partner. This section delineates these levels, providing a formal description of each, and clarifies how they culminate in the emerging paradigm of Agentic Science.

![image 14](Wei et al._2025_From AI for Science to Agentic Science A Survey on Autonomous Scientific Discovery_images/imageFile14.png)

- Figure 2: Research frameworks for Autonomous Scientific Discovery: Integrating Foundational Capabilities, Core Processes, and Research Levels across Life Sciences, Chemistry, Materials Science, and Physics.


- 2.1. The Evolution of AI for Science


- 2.1.1. Level 1: AI as a Computational Oracle (Expert Tools)


At the foundational level, AI operates as a Computational Oracle, a collection of highly specialized, nonagentic models designed to solve discrete, well-defined problems within a human-led workflow. These expert tools excel at tasks such as prediction and generation but lack autonomy; they function as sophisticated function approximators that require constant human guidance for task definition, execution, and interpretation of results. The core of the scientific process-from forming hypotheses to designing experiments-remains entirely in the hands of the human researcher.

Formally, a human scientist H selects a model class M and a dataset D = {(xi, yi)}iN=1 to train a model M ∈ M. The objective is to find an optimal static function M∗ that minimizes a task-specific loss Ltask over the dataset. This is typically achieved by minimizing the empirical risk:

∑︁N

1 N

Ltask(M(xi), yi) (1)

M∗ = arg min

M∈M

i=1

The model’s role is confined to producing an output ypred = M∗(xnew) for a new input, with no capacity for subsequent independent action.

This paradigm has led to significant advances across the natural sciences. In life sciences, AI has revolutionized genomics [65, 12, 244], proteomics [3, 157, 277, 355, 429, 272, 118, 430, 158, 432, 431], and single-cell analysis [113, 61], medicine and healthcare [128, 191, 307, 384, 129]. In chemistry, models like MolGPT [15], ChemLLM [417], and ChemMLLM [317] have accelerated molecular design and property prediction [143]. Materials science has benefited from AI-driven discovery platforms [24, 386, 382, 383, 412].

In physics and astronomy, AI tools are used for tasks ranging from modeling quantum systems [256, 434, 340] and detecting phase transitions [104, 42] to analyzing astronomical data [246, 85, 353] and modeling fluid dynamics [72, 450, 202].

##### 2.1.2. Level 2: AI as an Automated Research Assistant (Partial Agentic Discovery)

The second level marks the introduction of AI as an Automated Research Assistant. Here, AI systems exhibit partial autonomy, functioning as agents that can execute specific, pre-defined stages of the research workflow. These agents can integrate multiple tools and carry out sequences of actions to complete well-defined subgoals, such as running a series of experiments or performing a standardized data analysis pipeline. However, the high-level scientific direction, including the initial hypothesis, is still provided by human researchers. The agent operates within a structured environment to achieve a goal set by the human.

Formally, given a high-level goal G and a set of available tools Ttools, the agent A follows a policy π to select a sequence of actions {a0, a1, . . . , aT} that execute a sub-procedure of the scientific method. The agent’s operation can be described as a finite-horizon decision process where the policy aims to complete the assigned task:

{a0, . . . , aT} ∼ π(·|G, Ttools) (2)

The agent’s autonomy is limited to the execution of this pre-defined sub-goal, after which control returns to the human scientist.

Examples of this level are becoming common. In life sciences, agents are used for bioinformatics workflow automation [373, 306, 418, 367, 204] and experimental design [135, 114, 281]. In chemistry, agentic systems are being developed for reaction optimization [54, 282] and automated experimentation [67, 64, 304, 299]. In materials science and physics, agents automate complex simulations [407, 262, 247, 325] and can assist in the design of power electronics [206] and spacecraft control [233].

##### 2.1.3. Level 3: AI as an Autonomous Scientific Partner (Full Agentic Discovery)

The third and most advanced level envisions AI as an Autonomous Scientific Partner. In this paradigm, the AI agent possesses the ability to conduct the entire scientific discovery cycle independently. It can observe a domain, formulate novel and non-obvious hypotheses, design and execute experiments to test them, analyze the results, and iteratively refine its knowledge and strategy with minimal human intervention. This represents the full realization of Agentic Science, where the AI transitions from a tool or assistant to a genuine collaborator in the creation of knowledge.

Formally, the agent A operates in a continuous, open-ended discovery loop. Its objective is to maximize a measure of cumulative scientific utility, such as the expected information gain I(·) about a set of evolving hypotheses H. The agent’s policy π∗ is optimized over an infinite horizon, constantly updating its state st (which includes its knowledge base Kt and experimental evidence Et) and actions at based on new information:

Eπ [︃ ∞

γt I(Ht; st+1|st, at)]︃ (3)

∑︁

π∗ = argmax

π

t=0

Here, γ ∈ [0,1] is a discount factor, and the set of hypotheses Ht itself can be modified by the agent’s actions. The human role shifts to that of a high-level strategist and validator, setting broad research directions and critically evaluating the agent’s discoveries.

This paradigm is exemplified by several pioneering systems. Coscientist demonstrated the ability to

autonomously research, design, and execute a chemical reaction [30]. In life sciences, Robin independently hypothesized and proposed a novel therapeutic use for an existing drug [97], while OriGene acts as a self-evolving biologist for therapeutic target discovery [437]. Other notable examples include the AI Co-scientist [99], The Virtual Lab for nanobody design [313], ChemCrow for multi-purpose chemical research [35], and MOFGen for discovering new materials [140]. These systems point towards a future of human-agent co-discovery [219, 404, 99, 305, 424, 248].

##### 2.1.4. Level 4: AI as a Generative Architect (Future Prospect)

The prospective fourth level represents AI as a Generative Architect, a system capable of not just working within existing scientific paradigms, but actively inventing new ones. This goes beyond discovering new facts to engaging in autonomous invention. Such agents would possess the capacity to design novel scientific instruments, create new experimental methodologies, or formulate new conceptual and mathematical frameworks to understand the world. The agent’s role transcends discovery to become one of creation, moving from a "tool-user to tool-creator". This level also envisions agents as engines for large-scale interdisciplinary synthesis, uncovering latent connections between disparate scientific fields to forge unifying principles.

Formally, the agent’s objective shifts from optimizing discoveries within a fixed scientific framework to generating new frameworks altogether. Let F be the space of all possible scientific frameworks (which includes methodologies, toolsets Ttools, and conceptual models). The agent employs a generative policy πgen to create a new framework fnew ∈ F that maximizes a measure of generative potential Φ, which quantifies the power and scope of the new scientific questions the framework enables. The objective is to find an optimal generative policy πgen∗ :

Efnew∼πgen(·|K)[Φ(fnew)] (4)

πgen∗ = argmax

πgen

Here, K represents the total accumulated knowledge of science. The ultimate realization of this level could be a Global Cooperation Research Agent, a decentralized ecosystem of specialized agents that collaborate, peer-review, and experiment at a planetary scale to solve grand challenges beyond human coordination. A benchmark for achieving this level could be the "Nobel-Turing Test," where an AI system makes a discovery worthy of a Nobel Prize.

![image 19](Wei et al._2025_From AI for Science to Agentic Science A Survey on Autonomous Scientific Discovery_images/imageFile19.png)

- Figure 3: The Human-Agent Co-Discovery Loop. A human scientist provides high-level direction and the scientific agent operates autonomously within the Discovery Loop, guided by five key capabilities.


##### 2.2. The Human Scientist’s Evolving Role

Agentic AI is reshaping science, moving the human role from executor to strategist (Figure 3). Instead of focusing on how tasks are done, scientists now define what should be achieved and why it matters. Their work centers on setting research goals, keeping methods ethical and reliable, and weaving results into coherent narratives.

Formally, the scientist provides a set of goals G = {g1, . . . , gm} that guide the agent’s actions and embed safety, reproducibility, and ethical limits. Supervision involves checking the agent’s reasoning, validating results against domain knowledge, and stepping in when outputs drift from the intended path. In this way, humans ensure that autonomous discovery stays true to scientific standards and societal values.

This shift also calls for new skills. Scientists must learn to give clear, context-rich instructions that shape the agent’s policy π (agent prompting), manage the toolset Ttools available to the agent, and judge when to trust its outputs versus when to apply deeper scrutiny. These practices will reshape research culture: labs may act as “human-on-the-loop” hubs coordinating many agents, funders may evaluate human-agent teams rather than fixed plans, and journals may require full agent traces—including reasoning logs, code, and tool use—for transparency and reproducibility.

Innovation itself becomes more distributed. Knowledge production shifts toward a human-agent system

where agents pursue subgoals Gsub ⊂ G that advance larger programs. Such agents can explore huge problem spaces, find patterns beyond human reach, and connect ideas across disciplines. In doing so, agentic AI not only speeds discovery but also expands what science can ask and answer [91].

##### 2.3. Agentic Science: The Focus of This Survey

This survey focuses on the emergent paradigm of Agentic Science, which encompasses both Level 2 and Level 3 of the described evolution. Agentic Science is characterized by the use of AI systems that are not merely passive tools but are active, goal-directed agents capable of autonomous reasoning, planning, and action within the scientific domain [288, 106, 278]. To systematically analyze this paradigm, we structure our review around a three-level research framework (Figure 2). At the base are the Five Foundational Capabilities (Section 3) that form the cognitive core of any scientific agent. These capabilities enable the Four Core Processes (Section 4) of the agentic discovery loop, which in turn drive progress in the highest level: Autonomous Scientific Discovery across various research domains like life sciences (Section 5), chemistry (Section 6), materials (Section 7), and physics (Section 8). This hierarchical structure provides a comprehensive lens through which to examine and categorize developments in the field.

While Level 2 represents a form of task-level autonomy, where agents automate specific parts of the research process, Level 3 signifies goal-level autonomy, where agents can independently pursue high-level scientific objectives. The common thread is the concept of agency-the ability to act purposefully and independently in an environment to achieve a goal. The development of these agentic capabilities, from planning and reasoning engines [138, 100, 102, 347, 320, 218, 127, 38, 151] to tool use [269, 229, 300, 438], memory [293, 338, 255], collaboration [359, 123, 184, 53, 216, 197, 198], and evolution [230, 410, 125], is the central theme of this survey. By examining the progress and challenges within these levels, we aim to provide a comprehensive overview of how agentic AI is poised to reshape the future of scientific discovery.

##### 2.4. Modern Scientific Large Language Models for Agentic Science

The conceptual shift from AI as a tool to an autonomous partner is not merely theoretical; it is propelled by concrete advancements in a class of models known as Scientific Large Language Models (Sci-LLMs). These models serve as the technological bedrock for the levels of autonomy previously described. While many specialized, domain-specific models exemplify the powerful function approximators of Level 1 Computational Oracles, the recent surge in general-purpose models with advanced reasoning and tool-use capabilities provides the foundation for Level 2 and 3 Agentic Systems. This section surveys the current landscape of Sci-LLMs, illustrating the practical implementations that enable this paradigm shift.

Current scientific LLMs are mainly developed from existing general-purpose models through several common strategies. A primary approach involves fine-tuning foundational models like LLaMA on curated, science-focused instruction datasets covering disciplines such as physics, chemistry, and materials science to enhance performance on specific tasks [372, 415]. To build more robust scientific capabilities, another strategy involves large-scale pre-training or domain-adaptive pre-training on extensive scientific corpora, which include scholarly papers, textbooks, and specialized data formats like chemical formulae and protein sequences. This method strengthens a model’s core understanding of scientific principles [321, 310, 265, 18]. A third, more recent trend focuses on improving complex reasoning through test-time scaling. This is achieved by integrating techniques like Chain-of-Thought, large-scale Reinforcement Learning (RL), and massive Mixture-of-Experts (MoE) architectures, enabling models to process multimodal data and tackle multi-step scientific problems [107, 385, 322, 60, 362]. These distinct development strategies correspond to different levels of scientific autonomy: fine-tuning typically creates powerful Level 1 expert tools, while large-scale pre-training and enhanced reasoning are the key enablers for the agentic capabilities of Levels 2 and 3.

In many cases, domain-specific Sci-LLMs offer superior performance on specialized tasks. These models are constructed with well-curated datasets and training schemes tailored to a target subject. Below, we introduce recent domain-specific Sci-LLMs across eight scientific disciplines.

Life Sciences This broad field has seen Sci-LLMs applied to multi-omics, molecular biology, and healthcare. In multi-omics, development follows two paths: foundational models trained from scratch on biological sequences (DNA, RNA, protein) to learn fundamental representations [244, 36, 280, 201, 117], and LLMaugmented systems that integrate these representations to enable conversational analysis, cross-modal translation, and controllable generation of biological sequences [199, 223, 208, 403, 63, 368, 139, 336, 375, 376, 2, 446]. Recent models aim to unify reasoning across different omics domains [363, 69]. In molecular and cellular biology, models are tuned for tasks like molecular property prediction from SMILES strings and analysis of single-cell genomic data, as well as de novo molecular design for drug discovery [212, 61, 76, 116]. In healthcare, models are often adapted from general-purpose LLMs. A common strategy is supervised fine-tuning (SFT) on medical dialogue and QA datasets [173, 31, 330, 112, 295, 346, 421]. More advanced models undergo continued pre-training on large medical corpora before SFT and reinforcement learning to improve performance and safety [357, 52, 328, 390, 370, 335]. A critical frontier is multimodal AI, where models integrate medical imaging (e.g., X-rays) with text for report generation, visual question answering (VQA), and complex diagnostic reasoning [183, 180, 214, 240, 51, 192, 289, 50, 377, 307].

Chemistry LLMs in chemistry are designed to understand and generate information across various data modalities, including molecular structures (SMILES), reaction data, and 3D conformations. By training on specialized datasets, these models can perform a range of core chemistry tasks, such as molecular property prediction, retrosynthesis analysis, and structure-based drug design, effectively bridging text, 2D representations, and 3D geometries [417, 43, 440, 317, 152].

Materials Science In materials science, transformer-based models are widely used for diverse applications. One approach employs encoders pre-trained on material representations like SMILES strings or scientific abstracts to predict material properties [344, 170, 168, 32]. Another utilizes decoder-only, GPT-style architectures to generate novel molecules and crystal structures with desired features [213, 21, 16, 80, 9]. More specialized models are fine-tuned for specific applications such as predicting reaction equations, assessing crystal synthesizability, and modeling material mechanics, often integrating retrieval-augmented generation (RAG) with domain knowledge graphs [19, 253, 301, 40].

Physics and Astronomy In physics, Sci-LLMs are evolving into interactive tools for scientific workflows. These models integrate language processing with physics engines and visual modules to perform tasks such as estimating physical parameters from visual data, learning solution operators for partial differential equations (PDEs), and serving as expert knowledge retrieval systems for high-energy physics [57, 122, 436, 261]. Astronomy-specific models are typically built upon general architectures like LLaMA and adapted through continual pre-training on astronomy literature (e.g., arXiv abstracts) and fine-tuning on domain-specific tasks [142, 257, 439, 186, 239, 297, 105]. These models enhance text understanding and generation for astronomical topics and, in their multimodal variants, integrate astronomical images to perform tasks like describing galaxy images from visual data [245, 409, 156].

### 3. Scientific Agents: Core Abilities and Challenges

To transition from a specialized tool to an autonomous partner in discovery, a scientific agent must possess a suite of sophisticated, interconnected capabilities that collectively enable it to navigate the complexities of the research lifecycle. Unlike general-purpose agents, which are often designed for discrete, short-horizon tasks, a scientific agent must manage long-term, iterative, and empirically grounded workflows. This section breaks down the anatomy of such an agent by examining its five foundational pillars: the Planning and Reasoning Engine, which serves as its cognitive core; the ability to integrate and leverage external Tools to interact with the world; robust Memory Mechanisms for learning and knowledge accumulation; sophisticated Collaboration protocols for multi-agent systems; and the capacity for continuous Optimization and Evolution. For each of these core abilities, we will first review the state-of-the-art methodologies that empower them and then critically analyze the unique and significant challenges that emerge when these capabilities are applied to the high-stakes, verifiable domain of scientific inquiry (Figure 5).

##### 3.1. Planning and Reasoning Engines

The planning and reasoning engine is the cognitive core of a scientific agent, responsible for orchestrating the entire discovery process (Table 1). This engine translates high-level scientific goals into a sequence of executable actions, such as formulating hypotheses, designing experiments, executing code, or querying databases. Effective planning is what enables an agent to navigate the vast and complex search space of scientific inquiry with purpose and efficiency [138, 111, 343]. The design of these engines can be broadly categorized by their approach to task decomposition and their ability to dynamically adapt through feedback.

A foundational approach to planning involves task decomposition through linear reasoning chains. This strategy breaks down a complex problem into a sequence of manageable subtasks. The simplest version is the plan-and-solve paradigm [74, 342], often implemented via zero-shot Chain-of-Thought (CoT) prompting [166, 352], where an agent first devises a sequential plan and then executes it step-by-step. While straightforward, this method can be brittle and prone to error accumulation. To improve robustness, many works enhance this linear process using ensemble-like methods, such as generating multiple reasoning chains

Planning and Reasoning Engines

e.g., CoT [166], self-consistency [347], debate [320], ToT [127], MCTS [108], ReAct [396], etc.

e.g., Code interpreters [101], search engines [143], ChemCrow [34], CRISPR-GPT [135], MuJoCo [329], docking tools [83], etc.

Tool Use and Integration

Core Abilities and Challenges of Scientific Agents

Memory Mechanism e.g., Reflexion [293], Voyager [338], RAG [181], DrugAgent [141], GraphRAG [75], etc. Collaboration between Agents

e.g., MetaGPT [123], Coscientist [30], AutoGen [359], ReConcile [53], DyLAN [216], etc.

e.g., SELF-REFINE [230], CRITIC [102], RL with self-reward [406], KnowAgent [453], CAMEL [184], debate [73], etc.

Optimization and Evolution

e.g., NovelSeek [323], The AI Scientist [219], X-Master [46], Biomni [136], Coscientist [30], LLM-RDF [282], MatPilot [248], PROTEUS [71], The Virtual Lab [313], AI co-scientist [99], VirSci [305], MAPS [424], DORA [242], MDAgents [164], DiscoveryWorld [146], STELLA [155], AgentRxiv [286], Agent Hospital [187], ResearchAgent [13], Agent Laboratory [287], OriGene [437], Dolphin [404], AlphaEvolve [250], Conversational Health Agents [1], etc.

Core Process Challenges of Agentic Science

Fully Autonomous Research Pipeline

General Frameworks and Methodologies

e.g., Biomni [136], STELLA [155], BioResearcher [221], PiFlow [266], Empowering BD [87], etc.

e.g., BIA [373], CellAgent [367], TAIS [204], CRISPR-GPT [135], SpatialAgent [339], PhenoGraph [249],BioAgents [237], BioMaster [306], TransAgent [418], CompBioAgent [419], PerTurboAgent [114], PROTEUS [71, 273], CellVoyager [6], AstroAgents [284], BioDiscoveryAgent [281], OminiCellAgent [134], etc.

Genomics, Transcriptomics, and Multi-Omics Analysis

Agentic Life Science Research

Protein Science and Engineering

e.g., ProtAgents [91], Sparks [96], etc.

e.g., The Virtual Lab [313], OriGene [437], LLM Agent for DD [251], TxAgent [88], Robin [97], DrugAgent [209], LIDDIA [11], PharmAgents [82], CLADD [179], Tippy [77], ACEGEN [33], AI Co-scientist [99], Exploring Modularity [333], DO Challenge [296], PrimeGen [348],etc.

Drug and Therapeutic Discovery

Taxonomy

e.g., ChemCrow [35], ChemAgents [299], MOOSE-Chem [395], MOOSE-Chem3 [210], ChemMiner [55], Eunomia [7], ChemAgent [358], ChemHAS [196], ChemToolAgent [401] , Chemagent [318], LabUtopia [189], CACTUS [236], GVIM [227], MT-Mol [162], CSstep [48], CRAG-MoW [41], etc.

General Frameworks and Methodologies

e.g., Coscientist [30], LLM-RDF [283], Chemist-X [54], ORGANA [67], Dai et al. [64], Strieth-Kalthoff et al. [304], AutoChemSchematic AI [303], etc.

Organic Synthesis and Reaction Optimization

Agentic Chemistry Research

e.g., ChatMOF [159], MOFGen [140], OSDA Agent [132], ChemReasoner [302], Horwood & Noutahi [124], etc.

Generative Chemistry and Molecular Design

Computational and Quantum Chemistry

e.g., El Agente Q [455], Aitomia [126], ChemGraph [262], xChemAgents [263], etc.

e.g., AILA [232], Foam-Agent [407], ChemGraph [262], MechAgents [247], MatPilot [248], LLMatDesign [149], MAPPS [444], LLaMP [58], HoneyComb [423], Bazgir et al. [25], PiFlow [266], dZiner [8], Kumbhar et al. [172], etc.

General Frameworks and Automated Workflows

Agentic Materials Research

e.g., AtomAgents [90, 94], Ghafarollahi et al. [92], metaAgent [130], CrossMatAgent [326], Lu et al. [220], etc.

Structural and Functional Materials

Advanced and Quantum Materials

e.g., SciAgents [95], PriM [175], TopoMAS [413], etc.

General Frameworks and Methodologies

e.g., MoRA [145], LP-COMDA [206], LLMSat [233], CosmoAgent [380], etc.

e.g., StarWhisper [337], mephisto [311], AI Agents [169], AI Cosmologist [241], MAS-Cosmology [178], SimAgents [433], etc.

Astronomy and Cosmology

Agentic Physics and Astronomy Research

e.g., OpenFOAMGPT [258], OpenFOAMGPT 2.0 [78], LLM-Agent [205], MechAgents [247], AutoGen-FEM [325], etc.

Computational Mechanics and Fluid Dynamics

Quantum Computing e.g., k-agents [44], etc.

- Figure 4: A comprehensive overview of the core abilities, challenges, and applications of scientific agents across various research domains, from life sciences to astronomy.


and using self-consistency [347] or majority voting [193] to determine the best path, or even employing multiple agents to debate and refine the plan [320].

More sophisticated engines employ non-linear, tree-based search and exploration to navigate the solution space. Instead of committing to a single path, these methods explore multiple potential reasoning

- Table 1: Structured capability taxonomy of planning & reasoning engines in scientific agents. Rows are grouped into three major paradigms: reasoning structure, adaptation mechanisms, and interaction channels.


Paradigm Purpose Representative Mechanisms Key References

- I. Reasoning Structure Linear task decomposition Sequentially break down complex

goals

Plan-and-solve; zero-shot CoT; step-by-step execution

[74, 342, 166, 352]

Robust linear planning Improve reliability of linear chains Self-consistency; majority voting; multi-agent debate

[347, 193, 320] Non-linear exploration Explore multiple reasoning

branches in parallel

Tree-of-Thought (ToT); backtracking search

[127, 218, 59] Search with lookahead Handle uncertainty and long hori-

zons

Monte Carlo Tree Search (MCTS); playouts; UCT

[38, 108, 211]

- II. Adaptation Mechanisms Dynamic plan adaptation Adjust reasoning mid-execution ReAct loops (thought–act–observe) [396, 29] Self-reflection Detect and correct own errors Reflection prompts; memory-based

revision

[334, 354] Meta-controllers Control search strategy adaptively Budget tuning; step granularity ad-

justment

[308, 144] RL-augmented planning Learn better policies over plans Reinforcement learning; reward

shaping

[416, 151]

- III. Interaction Channels Human-in-the-loop Incorporate domain knowledge


[185, 177, 428] Collaboration between Agents Use diverse perspectives for robust-

Interactive teaching; critique feedback

and correction

[320, 290] Embodied / robotic execution Apply planning to physical / simu-

Debate, negotiation, role specialization

ness

[224, 10, 279] Surveys & meta-analysis Provide taxonomies, evaluation

Action abstraction; safety-aware exploration

lated environments

Systematic reviews; benchmark design

[138, 111, 343]

frameworks

trajectories simultaneously. The Tree-of-Thought (ToT) approach [127, 218, 59] exemplifies this, allowing an agent to evaluate different intermediate steps and backtrack from unpromising paths, which is crucial for tasks involving trial-and-error. This exploration can be guided by advanced algorithms like Monte Carlo Tree Search (MCTS) [38], a technique proven effective in complex domains like strategic gameplaying [108, 211] and robotics [224, 10, 279] that share similarities with the exploratory nature of scientific research. A critical element for both linear and tree-based approaches is dynamic plan adaptation via feedback and reflection. Modern agents rarely follow a static plan. Instead, they dynamically adjust their course using frameworks like ReAct [396], which interleaves reasoning with action and observation. This allows the agent to incorporate feedback from diverse sources: the environment (e.g., the output of a simulation) [29], human guidance [185, 177, 428], model self-reflection [334, 354], or other collaborating agents [290]. This continuous, iterative process of planning, acting, and refining [308, 144], often enhanced with reinforcement learning techniques [416, 151], is what endows agents with the adaptability needed to tackle the unpredictability of scientific discovery.

Challenges for Scientific Reasoning. Despite this progress, developing planning and reasoning engines for scientific discovery presents unique challenges not typically found in general domains. First, scientific planning operates under a paradigm of high-stakes and strict verifiability; a flawed plan can lead to wasted resources, incorrect conclusions, or even unsafe lab experiments, demanding a high degree of reliability

- Table 2: Structured capability taxonomy of tool use and integration in scientific agents. Rows are grouped into three major paradigms: foundational tools, domain-specific tools, and experimental/simulation platforms.


Paradigm Purpose Representative Mechanisms Key References

- I. Foundational, general-purpose tools Information retrieval Access external knowledge beyond

model memory

Search engines; scientific databases; integration with retrieval APIs

[269, 389, 405, 143, 324]

Computational utilities Solve well-defined problems; perform symbolic and numerical analysis

Code interpreters; mathematical libraries (SymPy, SciPy)

[101, 174]

- II. Domain-specific computational and analytical tools Chemistry & materials science Predict reactions; estimate proper-

ties; integrate scientific APIs

ChemCrow; CACTUS; HoneyComb [34, 236, 422] Biology & genomics Support genome editing and bioin-

formatics workflows

CRISPR-GPT; domain bioinformatics suites

[135] Multi-domain tool hubs Generalize integration across di-

verse scientific domains

SciAgent; extensible toolkits for physics, finance, materials

[228]

- III. Experimental and simulation platforms Physical dynamics engines Model real-world physics for hy-


[207, 329] Engineering & climatology models Evaluate designs and environmen-

MuJoCo; physics simulation engines

pothesis testing

[171, 167] Molecular docking simulators Guide molecule generation via

MyCrunchGPT; ClimSight; computational fluid dynamics models

tal impacts

DockingGA; docking-based evaluation loops

[83]

docking feedback

and physical plausibility. Second, scientific inquiry often involves navigating vast, unstructured, and poorlyunderstood search spaces (e.g., all possible chemical compounds), requiring sophisticated strategies to balance exploration and exploitation [329]. Third, the feedback loop in science is not simple text but often consists of noisy, multimodal experimental data that the agent must correctly interpret to refine its plan [302]. Finally, scientific agents must engage in long-horizon planning to manage multi-step research projects and aim for causal understanding [285] rather than mere correlation, all while mitigating the risk of error accumulation that plagues sequential reasoning.

##### 3.2. Tool Use and Integration

The capacity to harness external tools is essential for scientific agents, enabling them to overcome the intrinsic constraints of language models in computation, data access and interaction with the physical world [235, 292, 79]. Tool integration within scientific workflows can be organised by function, spanning from foundational utilities to highly specialised experimental platforms (Table 2).

The first tier comprises foundational, general-purpose tools that provide essential computational and informational capabilities. As with general-purpose agents, scientific agents must determine both the timing and the manner of tool use [269, 389, 405]. These include search engines and databases for information retrieval, as demonstrated by MAPI-LLM [143] and ClimateGPT [324], as well as code interpreters and mathematical libraries such as SymPy and SciPy, which support the solution of well-defined problems. Such capacities are refined in systems like Tora [101] and assessed in data science benchmarks [174]. These tools form the bedrock upon which higher-order scientific reasoning is constructed.

Building upon this foundation, the second category comprises domain-specific computational and analytical tools. These encapsulate expert knowledge and advanced algorithms, enabling agents to address complex scientific questions. In chemistry and materials science, for instance, ChemCrow [34] and CACTUS [236] integrate specialized toolkits for reaction prediction and molecular property estimation. HoneyComb [422] combines a materials science knowledge base with a hub of domain-specific APIs. In biology, CRISPRGPT [135] integrates a suite of bioinformatics tools for genome-editing experiment design. Frameworks such as SciAgent [228] illustrate how tool-use capabilities can be generalized across diverse scientific domains, from physics to finance, through the development of comprehensive, multi-domain toolsets. Such deep integration enables agents to perform specialized analyses that would otherwise be intractable.

The third and most advanced category centres on experimental and simulation tools for hypothesis validation. This capability is essential for emulating the scientific method, as it enables agents to actively test hypotheses and generate new empirical data. Agents can interact with high-fidelity simulators to investigate complex systems. For example, physics engines such as MuJoCo have been employed to reason about physical dynamics [207, 329]. In engineering and climatology, systems including MyCrunchGPT [171] and ClimSight [167] integrate computational fluid dynamics and climate models to optimise designs and evaluate environmental impacts. Similarly, DockingGA [83] employs molecular docking simulations as a feedback mechanism for guiding molecular generation. By engaging with such virtual laboratories, agents can iteratively refine their understanding and uncover novel scientific insights.

Challenges in Scientific Tool Use. Notwithstanding these advances, the integration of tools into scientific agents presents distinctive challenges that extend beyond those encountered by general-purpose agents. First, scientific tools demand exceptional precision and deep domain-specific understanding. Unlike a routine web search, even a minor error in parameterizing a bioinformatics tool or a physics simulation can yield scientifically invalid outcomes, making it essential for agents to interpret complex documentation and scientific context accurately. Second, reproducibility and provenance are non-negotiable in scientific research: an agent must not only execute a tool correctly but also record, with meticulous detail, the tool versions, parameters, and data lineage to enable independent verification of its findings. Third, scientific discovery often necessitates the construction of complex, interoperable workflows that chain multiple specialized tools–a process hindered by heterogeneous interfaces and non-standardised data formats. As benchmarks such as ShortcutsBench [291] demonstrate, managing dependencies and adapting to API changes constitute significant obstacles, further exacerbated by the rapid evolution of the scientific software ecosystem. Finally, many high-fidelity simulators and proprietary databases impose substantial computational and financial costs, requiring agents to conduct rigorous cost–benefit analyses and apply effective resource management to ensure research efficiency.

##### 3.3. Memory Mechanisms

Memory is a foundational capability of agentic intelligence, enabling agents to retain information, learn from experience, and maintain context during complex tasks [378, 238]. For scientific agents, memory mechanisms are not just about recalling past dialogue but are fundamental to emulating the scientific process of iterative refinement, knowledge accumulation, and hypothesis testing. We categorize memory mechanisms based on their functional role in the agent’s workflow: memory for iterative task execution, which supports in-context learning and adaptation, and memory as a knowledge hub, which connects the agent to vast external information repositories (Table 3).

First, memory for iterative task execution allows an agent to maintain a coherent understanding of an

![image 36](Wei et al._2025_From AI for Science to Agentic Science A Survey on Autonomous Scientific Discovery_images/imageFile36.png)

- Figure 5: Core abilities of scientific agents.


ongoing research task by storing and reflecting on its recent history. This includes short-term context from dialogues and environmental feedback, as seen in frameworks like ReAct [396], as well as more structured memory derived from the agent’s own actions. For instance, agents can learn from both successes and failures by building experience repositories, a technique central to Reflexion [293] and ExpeL [438], allowing them to refine their strategies over successive trials. This experiential memory can be further structured into reusable skill libraries, where successful action sequences are codified for future use, as demonstrated by Voyager [338] in exploration tasks and AtomAgents [90] through dedicated tool memory. This form of memory transforms short-lived interactions into persistent, actionable knowledge that guides the agent through the cycles of scientific inquiry.

Second, memory as a knowledge hub extends an agent’s capabilities by integrating external information sources, grounding its reasoning in established scientific knowledge. The most prevalent approach is RetrievalAugmented Generation (RAG) [181, 354], which dynamically fetches relevant information from text corpora. This is crucial for tasks like automated literature review, as seen in PaperQA [176] and the LitLLM toolkit [4]. Beyond unstructured text, scientific agents leverage structured knowledge graphs to ensure their hypotheses are consistent with known scientific concepts [93, 75]. Some agents, like DrugAgent [141], query specialized databases to retrieve specific information like drug-target interactions. Advanced architectures interleave retrieval with reasoning steps [332] or use tiered memory systems like MemGPT [255] to efficiently manage both internal context and external knowledge, enabling agents to surpass their training data and engage with the vast, ever-expanding body of scientific information.

Challenges in Scientific Memory Mechanisms. Despite these advancements, memory for scientific agents presents distinct and significant challenges. First, the accuracy and decay of scientific knowledge is a critical hurdle; information in scientific fields can become outdated, and agents must be able to validate and update their memory to avoid relying on superseded facts. Second, scientific data is inherently heterogeneous and multi-modal, comprising not just text but also tables, chemical structures, genomic sequences, and experimental imagery. Current memory architectures are ill-equipped to store, retrieve, and reason across these diverse data types seamlessly. Finally, scientific discovery often involves long-term causal reasoning, where insights gained months or even years into a project may depend on early, seemingly minor experimental results. Existing memory systems lack the capacity to maintain such extended, causally-linked histories with

- Table 3: Structured capability taxonomy of memory mechanisms in scientific agents. Rows are grouped into two major paradigms: memory for iterative task execution and memory as a knowledge hub.


Paradigm Purpose Representative Mechanisms Key References

- I. Memory for iterative task execution Short-term & feedback memory Maintain coherent understanding

of ongoing tasks; incorporate observations

Dialogue/context windows; tooloutput logs; thought–act–observe loops (ReAct)

[396]

Experience repositories Learn from past attempts to refine strategies

Episodic traces; critique-and-retry; outcome-indexed memory

[293, 438] Reusable skill libraries Turn successful action sequences

into reusable skills/macros

Skill discovery; action chunking; competence tracking

[338, 90] Memory governance & persistence Decide what to store, summarize,

and forget across trials

Summarization, saliency filters, lifetime management

[378, 238]

- II. Memory as a knowledge hub RAG Ground reasoning in external liter-


Dense/sparse retrieval; chunking; reranking; cite-while-generate

[181, 354]

ature; go beyond parametric memory

[176, 4] Structured knowledge graphs Enforce consistency with scientific

Literature assistants Automate literature review and evidence aggregation

PaperQA; LitLLM toolkit; query planning + citation tracking

[75, 93] Specialized scientific databases Retrieve task-specific entities (e.g.,

GraphRAG; domain KGs; constraint checking

ontologies; relational reasoning

[141] Interleaved retrieval–reasoning Pull information at intermediate

API connectors; schema-aware queries; evidence linking

drug–target data)

Step-wise retrieval policies; tool-augmented CoT; planningintegrated RAG

[332]

steps of multi-hop reasoning

[255] Surveys & meta-frameworks Synthesize patterns; provide evalu-

Tiered memory architectures Manage long-term external memory with internal working memory

Memory managers; paging; pointers to external stores (MemGPT)

Taxonomies; memory governance principles; benchmarks

[378, 238]

ation and design guidance

high fidelity, which is essential for ensuring the reproducibility of agent-driven discoveries–a foundation of the scientific method.

##### 3.4. Collaboration between Agents

Effective collaboration enables multi-agent systems to address complex scientific problems that surpass the capabilities of any single agent [62, 68, 402, 341]. By distributing tasks, synthesizing diverse information, and iteratively refining solutions, collaborative frameworks enhance both the robustness and creativity of agentic research [331, 110]. The mechanisms governing such interactions can be broadly categorized by their primary collaborative strategy: structured workflows, deliberative refinement, and dynamic adaptation (Table 4).

A prominent strategy is hierarchical task execution, where a structured, top-down approach is employed for problem-solving. In these systems, a primary agent or predefined workflow decomposes a complex goal into smaller, tractable subtasks, which are then assigned to specialized agents. This manager–worker paradigm emphasizes efficiency and organized execution. For example, MetaGPT [123] implements this paradigm by assigning role-specific agents within a simulated software company, using Standard Operating Procedures (SOPs) to formalize coherent workflows. Similarly, ChatDev [268] simulates a software development team with distinct roles. Other frameworks achieve this through explicit task decomposition by a controller, as

- Table 4: Structured capability taxonomy of collaboration strategies in multi-agent scientific systems. Rows are grouped into three major strategies: hierarchical task execution, deliberative refinement, and dynamic adaptive topologies.


Paradigm Purpose Representative Mechanisms Key References

- I. Hierarchical task execution Manager–worker decomposition Break complex goals into subtasks

assigned to specialized agents

Workflow controllers; SOP-driven orchestration (MetaGPT, ChatDev)

[123, 268] Role differentiation Assign functional roles (planner, ex-

ecutor, tool-user)

Role-playing agents; metaprompting

[312, 271, 184] Structured scientific workflows Organize multi-phase experiments

or multi-tier planning

Coscientist; AFlow [30, 425]

- II. Deliberative refinement Dialogue-based debate Improve factuality and reasoning

via structured exchanges

Peer review dialogue; group-chat settings (AutoGen, MAD, MDebate)

[360, 197, 73, 163]

Iterative peer refinement Incrementally improve shared outputs through critique & revision

Reflexion; ReConcile; METAL; DSAgent

[293, 354, 53, 182, 109]

Competitive vs cooperative roles Assign critic/actor or explainer/evaluator to balance strengths

LEGO; Reflexion (actor–evaluator loops)

[120, 293]

Ensemble and consensus methods Aggregate multiple solutions for robustness

Majority voting; best-component synthesis; expert review

[150, 426, 160, 66, 319]

- III. Dynamic adaptive topologies Predefined communication patterns Select topology based on task (relay,


Exchange-of-Thought (EoT) [399] Learned adaptive routing Dynamically reconfigure collabora-

debate, star, tree)

[164, 217, 148] Teacher–student policies Learn adaptive collaboration

MDAgents; DyLAN; graph-based orchestrators (DAGs)

tion graph by task complexity

Teacher–student frameworks for adaptive teaming

[195]

through meta-learning

in Meta-Prompting [312], or by differentiating a single model into functional roles such as planner and tool-user [271]. This hierarchical approach is particularly suited to structured scientific workflows, such as managing experimental phases in Coscientist [30], coordinating multi-tier planning in AFlow [425], or structuring complex role-playing tasks as in CAMEL [184].

A second major strategy is deliberative, refinement-based collaboration, which seeks to improve solution quality through iterative peer interaction, often inspired by scholarly debate and review. Some systems facilitate direct dialogue, where agents engage in structured exchanges to challenge and refine each other’s ideas, a process shown to improve factuality and reasoning [73, 374, 197]. AutoGen [360] supports this through a group-chat setting, while frameworks such as MAD [197], MADR [163], and MDebate [73] define specific protocols to encourage critical feedback and consensus-building. Another approach involves independent refinement of a shared solution. This may be competitive, as in LEGO [120], where an “Explainer” is critiqued by a “Critic,” or cooperative, as in Reflexion [293, 354], where an “Evaluator” provides feedback to an “Actor.” In ReConcile [53], agents iteratively improve a common answer, while METAL [182] and DS-Agent [109] employ specialized revision agents. This category also encompasses ensemble methods, where multiple agent-generated solutions are synthesized–either by combining the best components [150] or through consensus mechanisms such as majority voting [426, 160] or expert consultation, as in scientific review systems like MARG [66] and medical diagnosis frameworks like MedAgents [319].

The most advanced systems employ dynamic, adaptive topologies, in which the interaction structure

itself is flexible and optimized for the task. Rather than relying on fixed hierarchies or communication patterns, these frameworks reconfigure their collaboration graph in response to task requirements or real-time performance feedback. Some offer predefined topologies, such as communication paradigms (e.g., relay, debate) and network structures (e.g., star, tree) in EoT [399], which can be selected to match a specific problem. Others learn the optimal structure dynamically. For instance, MDAgents [164] routes tasks to different collaborative configurations based on an initial complexity assessment. DyLAN [217] follows a twostage process: first identifying the most critical agents for a task, then reconfiguring communication pathways to amplify their influence. Similarly, graph-based orchestrators dynamically construct Directed Acyclic Graphs (DAGs) of tasks and dependencies, enabling parallel execution and flexible collaboration [148]. Additional research explores adaptive collaboration policies learned through teacher–student frameworks [195].

Challenges in Scientific Collaboration Mechanism. While these general frameworks are foundational, scientific collaboration introduces distinctive challenges. First, it must be grounded in empirical reality: unlike general-purpose tasks, the aim is not merely to produce plausible text, but to generate testable hypotheses and verifiable experimental plans [30, 314]. The consensus among agents must be scientifically valid, avoiding pitfalls such as amplified hallucinations [123] that could compromise results. Second, scientific inquiry requires managing epistemic diversity and uncertainty. Progress often arises from competing hypotheses; thus, agent collaboration should both foster a diversity of ideas and implement rigorous evaluation against evidence, quantify uncertainty, and prevent premature consensus that could hinder innovation [98]. Finally, scientific discovery demands integrating complex, multimodal information across extended workflows. Agents must collectively reason over heterogeneous data and coordinate the use of specialized software and physical instruments [34, 276]. This necessitates communication protocols far more sophisticated than plain text exchange–requiring orchestration, static or dynamic, that can maintain state and share structured knowledge throughout the multi-stage process of scientific investigation.

##### 3.5. Optimization and Evolution

For a Scientific Agent, the ability to optimize and evolve is not merely about refining parameters but about enhancing the entire apparatus of scientific inquiry [84, 445, 200]. Unlike agents in more constrained domains, a scientific agent’s evolution must target its core scientific reasoning, its internal world model, and its collaborative structure to navigate the complexities of discovery. This process unfolds along several key axes: evolving the scientific strategy, the internal knowledge base, and the agent’s own architecture (Table 5).

A primary mechanism for agent improvement is iterative self-refinement, where an agent enhances its outputs through a cycle of generation, feedback, and correction. This process can be entirely self-contained, as seen in methods like SELF-REFINE [230, 354], which uses self-generated feedback, or STaR [410] and V-STaR [125], which bootstrap reasoning capabilities from a few examples. Agents can also leverage external tool-based feedback for more grounded correction, as demonstrated by CRITIC [102], which uses tools to validate and revise outputs, and SelfEvolve [153], which debugs code based on execution results. This trial-and-error process, whether simulated [300] or actual, allows agents to progressively reduce errors and improve the quality and reliability of their solutions through direct interaction with a task environment.

Beyond refining a single output, agents can evolve their underlying models and knowledge structures through self-learning and interaction. This includes self-supervised approaches that improve the core model, such as SE [442] and DiverseEvol [361], which enhance pre-training and instruction tuning, respectively. Reinforcement learning with self-generated rewards offers another path, where agents learn to produce their own reward signals to guide improvement, as seen in Self-Rewarding models [406], RLCD [388], and

- Table 5: Structured capability taxonomy of optimization and evolution in scientific agents. Rows are grouped into three major paradigms: iterative self-refinement, self-learning & interaction, and population-based co-evolution.


Paradigm Purpose Representative Mechanisms Key References

- I. Iterative self-refinement Self-feedback correction Improve outputs by reflecting on

own errors

SELF-REFINE; STaR; V-STaR (bootstrapped reasoning)

[230, 354, 410, 125]

Tool-based feedback Ground refinements via external validators

CRITIC; SelfEvolve (executionbased debugging)

[102, 153] Trial-and-error refinement Incrementally improve through

simulation or direct interaction

Iterative testing frameworks; simulated environments

[300]

- II. Self-learning and interaction Model-level self-improvement Enhance pretraining or tuning via

self-supervision

SE; DiverseEvol (self-supervised learning)

[442, 361] Self-reward reinforcement learning Generate intrinsic rewards to guide

policy evolution

Self-Rewarding LMs; RLCD; RLC [406, 388, 259] Knowledge-guided evolution Integrate structured priors and ex-

ternal knowledge into planning

KnowAgent; WKM [453, 270]

- III. Population-based co-evolution Cooperative evolution Improve strategies via collaborative


[184, 414, 226] Competitive evolution Sharpen reasoning or robustness

CAMEL (role-playing); ProAgent; CORY (multi-agent RL)

multi-agent interaction

Multi-agent debate; Red-Teaming [73, 198, 225] Mixed dynamics Balance collaboration and competi-

through adversarial settings

Hybrid role-based or adversarial–synergistic frameworks

[331, 110]

tion for diverse improvement

RLC [259]. Furthermore, agents can evolve by explicitly integrating external knowledge, which provides structured priors to guide planning and decision-making, as exemplified by KnowAgent [453] and WKM [270]. These methods focus on evolving the agent’s intrinsic capabilities, leading to more robust and generalizable performance.

A third paradigm involves population-based co-evolution, where improvement emerges from the interactions within a group of agents. These interactions can be cooperative, where agents work together to solve problems. For instance, CAMEL [184] uses a role-playing framework for collaboration, ProAgent [414] enables agents to infer teammates’ intent for better coordination, and CORY [226] uses multi-agent RL for fine-tuning. Conversely, evolution can be driven by competition. Multi-agent debate frameworks [73, 198] force agents to critique and defend positions, sharpening their reasoning. Similarly, adversarial setups like Red-Teaming [225] use competition to uncover and patch vulnerabilities. This co-evolutionary pressure, whether collaborative or competitive, drives the development of more sophisticated and resilient strategies across the agent population, mirroring evolutionary dynamics found in nature.

Challenges in Scientific Optimization and Evolution. Applying these optimization and evolution techniques to scientific agents presents unique challenges not typically found in other domains. First, the evaluation of a scientific hypothesis or experiment is often resource-intensive, time-consuming, and expensive, making rapid, iterative feedback loops (central to many RL and self-correction methods) impractical. Unlike compiling code or checking a factual answer, a single evaluation may require days of lab work. Second, the reward landscape in scientific discovery is exceptionally sparse and complex; breakthroughs are rare, and the path to discovery often involves long periods with no positive feedback signal. This makes it difficult

![image 47](Wei et al._2025_From AI for Science to Agentic Science A Survey on Autonomous Scientific Discovery_images/imageFile47.png)

- Figure 6: Core process of Agentic Science. Not all steps are required in every instance, and execution order may be dynamically adjusted based on agent objectives, context, and ongoing results.


for agents to learn meaningful policies. Finally, the outputs of scientific agents must be grounded in physical reality and adhere to strict safety protocols. An "optimized" chemical synthesis procedure that is dangerously explosive is a catastrophic failure. Therefore, the optimization process must be constrained by scientific validity, safety, and the ultimate goal of producing reproducible and verifiable knowledge, adding layers of complexity beyond achieving high scores on a typical benchmark.

### 4. Agentic Science: Dynamic Workflow and Challenges

Agentic Science redefines the scientific method as an autonomous, closed-loop workflow, managed by intelligent agents. At its core, this paradigm contains a continual, self-improving cycle of discovery comprising four key stages: (1) Observation and Hypothesis Generation, (2) Experimental Planning and Execution, (3) Result Analysis, and (4) Synthesis, Validation, and Evolution. This section analyzes each stage by connecting it to the core agentic capabilities and challenges discussed previously, highlighting its implementation in current agentic systems. Note: Not all steps are required in every agentic system, and execution order may be dynamically adjusted based on agent objectives, context, and ongoing results.

##### 4.1. Observation and Hypothesis Generation

The initiation of agentic inquiry centers on the formulation of novel, testable hypotheses derived from prior knowledge. This process relies fundamentally on the agent’s memory mechanism, particularly its ability to function as a knowledge connector.

Agents begin with knowledge ingestion, using techniques like Retrieval-Augmented Generation (RAG) [181]

to query and synthesize vast scientific corpora, as demonstrated in systems like the LitLLM toolkit [4] and ResearchAgent [14]. This information is then organized via knowledge structuring into formats like taxonomies or knowledge graphs [86, 243, 75] to ground subsequent reasoning. Building on this structured knowledge, the agent’s planning and reasoning engine engages in hypothesis formulation [294, 131, 356]. This can

- Table 6: The Agentic Science Loop: Mapping Core Processes to Agent Abilities and Scientific Challenges.


Key Activities & Representative Works Primary Agent Abilities Utilized

Unique Scientific Challenges

Core Process in Agentic Science

Observation & Hypothesis Generation

Knowledge Ingestion & Structuring: Syn-

Memory Mechanism (as a knowledge nexus) Planning & Reasoning Engines (for exploratory pattern discovery)

Vast Hypothesis Space: Navigating an enormous and ill-defined space of possible scientific ideas. Knowledge Veracity: Contending with outdated or conflicting scientific knowledge. Causal Discovery: Aiming to generate hypotheses about causation, not just correlation.

thesizing corpora via RAG (e.g., LitLLM toolkit [4]); organizing into knowledge graphs [75] or taxonomies.

Hypothesis Formulation: Reasoning over structured knowledge to identify novel, testable ideas (e.g., SciAgents [95], Robin [97], OriGene [437]).

Experimental Planning & Execution

Optimized Plan Generation: Decomposing goals into structured, resource-efficient experimental workflows. Automated Execution: Controlling robotic hardware (e.g., Coscientist [30], ORGANA [67]) or running simulations (e.g., The Virtual Lab [313]). Autonomous Coding: Generating and executing analysis pipelines (e.g., CellAgent [367], BIA [373]).

Planning & Reasoning Engines (for task decomposition and adaptation) Tool Use & Integration (for real-world interaction and computation)

Physical Plausibility & Safety: Ensuring plans are grounded in reality and adhere to safety protocols. Strict Reproducibility: Demanding meticulous provenance tracking of all parameters, code, and tool versions. Cost & Resource Management: Balancing goals with real-world financial and computational budgets.

Data & Result Analysis

Multimodal Data Extraction: Parsing semantic content from charts [234], tables [350], and other outputs. Structured Interpretation: Interleaving reasoning and action to connect results to hypotheses [396]. Insight Generation: Uncovering mechanistic explanations from raw data (e.g., PROTEUS [71], SpatialAgent [339]).

Tool Use & Integration (to parse experimental data) Planning & Reasoning Engines (to interpret outcomes)

Noisy & Ambiguous Feedback: Scientific results are often incomplete or require expert interpretation. Heterogeneous Data Integration: Seamlessly reasoning across diverse data types (text, images, spectra, sequences). Avoiding Confirmation Bias: Objectively evaluating results, especially those that contradict the hypothesis.

Memory Mechanism (to contextualize new findings)

Synthesis, Validation, & Evolution

Evidence Synthesis & Critique: Emulating peer review via multi-agent debate to validate claims [254].

Collaboration between Agents (for peer review and critique)

Long-Term Causal History: Maintaining a coherent, causally-linked record of a longterm research project. Expensive & Sparse Rewards: Scientific breakthroughs are rare, providing infrequent signals for learning algorithms. Sustained, Productive Improvement: Ensuring agent "evolution" is scientifically valid and not just reinforcing biases.

Automated Reproducibility: Verifying findings through automated replication checks.

Optimization & Evolution (for selfimprovement) Memory Mechanism (for long-term learning)

Adaptive Refinement: Learning from past experiments to improve future strategy (e.g., Reflexion [293], Sparks [96], MOOSEChem3 [210]).

be formally represented as the maximization of a potential function P over a set of candidate hypotheses Hcand, conditioned on a structured memory M derived from the knowledge base K:

P(h|M(K)) (5)

hnew = arg max

h∈Hcand

This is not merely a linear deduction but often an exploratory process of pattern discovery and symbolic reasoning to identify promising research directions [13, 219, 266, 381, 305, 260, 215, 394, 99]. Systems like SciAgents [95] and MOOSE-Chem [395] exemplify this by reasoning over structure-property relationships and chemical reactivity, respectively.

This stage faces significant challenges unique to the scientific domain: heterogeneous data formats, dynamic knowledge updating, and large search space. The primary challenge lies in the nature of scientific knowledge itself: its veracity can decay over time, and it is highly heterogeneous and multi-modal. An agent’s memory system must therefore not only ingest data but also grapple with potentially outdated facts and

seamlessly reason across text, tables, and images. Furthermore, the reasoning engine must navigate a vast, unstructured search space of possible hypotheses, requiring sophisticated strategies to balance exploration and exploitation [329]. The ultimate goal is to formulate hypotheses that aim for causal understanding [285], a far more complex task than correlational pattern matching common in general domains.

Empirical results underscore the potential of this agentic formulation. OriGene [437], a virtual disease biologist, integrates multimodal data to generate and prioritize therapeutic targets. It identified GPR160 and ARG2 as novel candidates for liver and colorectal cancer, respectively–both of which were subsequently validated in patient-derived systems. Similarly, Robin [97], a collaborative multi-agent system, autonomously hypothesized the use of ripasudil for treating dry age-related macular degeneration (dAMD)–a drug previously unlinked to the condition–by autonomously conducting background research and inference. In another domain, CellVoyager [6] exemplifies data-driven hypothesis generation by reanalyzing aging-related transcriptomic datasets. It uncovered a previously unreported link between increased transcriptional noise and brain aging, demonstrating the capacity of agentic systems to surface latent biological insights.

##### 4.2. Experimental Planning and Execution

The second phase of Agentic Science operationalizes hypotheses through end-to-end experimental workflows. This stage is managed by the agent’s planning and reasoning engine, which performs optimized plan generation. This involves decomposing a high-level goal into a structured, resource-efficient plan, which could be a biological protocol [252] or an algorithm for causal discovery [188].

This process can be modeled as a constrained optimization problem, where the agent seeks to find an experimental plan π∗ that minimizes cost C(π) while ensuring the plan’s validity V(π, h) for testing hypothesis h exceeds a certain threshold θ:

C(π) s.t. V(π, h) ≥ θ (6)

π∗ = argmin π∈Π

The execution of this plan, yielding results R, depends on the agent’s tool use and integration capability, denoted by an execution function that leverages a set of available tools T: R = Execute(π∗, T). The agent must perform dynamic tool selection, mapping abstract plan steps to concrete tool invocations, and then engage in automated execution by generating code or controlling robotic hardware. This capability is seen in systems that autonomously generate research code [147, 250, 287, 81], as evaluated by benchmarks like SciCode [327] and MLE-Bench [47]. To enhance reliability, especially in complex tasks, agents can employ advanced planning strategies like tree search [154] to explore and backtrack from potential execution paths.

Executing scientific experiments introduces formidable challenges that stress agentic capabilities. Scientific planning operates under a paradigm of high-stakes and strict verifiability, where a flawed plan can lead to wasted resources or invalid conclusions. This demands exceptional reliability from the reasoning engine. The tool use itself requires an extremely high degree of precision and domain understanding, as minor errors in parameterizing a simulation or a lab instrument can invalidate results. Moreover, reproducibility and provenance are non-negotiable; the agent must meticulously log all tool versions and parameters to ensure its work can be verified. This is further complicated by the need to create complex workflows by chaining multiple specialized tools, a task known to be difficult [291]. Finally, because many scientific tools (e.g., high-fidelity simulators, lab equipment) are expensive, the agent must perform sophisticated cost-benefit analysis, a challenge rarely faced by general-purpose agents.

Agentic systems increasingly demonstrate proficiency in closed-loop planning and execution across both virtual and physical domains. For instance, Coscientist [30] autonomously designed and optimized

a palladium-catalyzed cross-coupling reaction by interfacing with robotic hardware, showcasing an endto-end experimental loop. Similarly, the robotic agent ORGANA [67] executed a 19-step synthesis and characterization protocol for quinone derivatives, reducing human workload by over 80%. In virtual labs, The Virtual Lab [313] autonomously constructed a computational pipeline incorporating AlphaFold and docking simulations to design 92 novel SARS-CoV-2 nanobodies, two of which demonstrated strong binding in subsequent empirical tests. In bioinformatics, agents such as BIA [373] and CellAgent [367] have demonstrated robust pipeline planning and execution for tasks like single-cell RNA-seq analysis.

##### 4.3. Data and Result Analysis

Following experiment execution, the agent must extract actionable insights from raw outputs to update its belief about the hypothesis. This phase relies on a tight integration of tool use, reasoning, and memory.

The process begins with multimodal data extraction [369], using specialized tools or vision-language models to parse semantic content from outputs like scientific charts [234, 351]. Subsequently, the agent’s reasoning engine performs structured interpretation, employing techniques like Chain-of-Table to understand complex relational data [350]. This entire analysis is a practical application of the ReAct [396] framework, where the agent observes the experimental outcome and reasons about its implications. This can be conceptualized as a Bayesian update to the agent’s belief in the hypothesis h, where the posterior probability P(h|R) is proportional to the likelihood of observing the results R given the hypothesis, P(R|h), multiplied by the prior belief P(h):

P(h|R) ∝ P(R|h) · P(h) (7)

This reasoning is contextualized by the agent’s memory, which holds the prior experimental history and domain knowledge necessary for accurate interpretation and hypothesis validation. Agents may even generate scientific figures to communicate their findings [26, 408].

The primary challenge in this stage stems from the nature of scientific feedback loops, which often involve noisy, multimodal experimental data. An agent’s reasoning engine must be robust enough to correctly interpret this data, distinguishing signal from noise without succumbing to confirmation bias. This is compounded by the heterogeneous data types involved; an agent’s memory and reasoning architecture must seamlessly handle a mix of text, tables, genomic sequences, and imagery to form a coherent conclusion. Unlike general tasks where feedback is often a clear text-based signal, scientific analysis demands a deep, contextual understanding of complex and often ambiguous data formats.

Agentic systems have demonstrated increasing autonomy and sophistication in scientific interpretation. For example, after generating a therapeutic hypothesis and proposing an RNA-seq experiment, Robin [97] autonomously analyzed the resulting data to uncover the increase in expression of ABCA1, a lipid efflux regulator, as a potential mechanism of action. In proteomics, PROTEUS [71] performs end-to-end analysis of raw mass spectrometry data, generating mechanistic hypotheses judged by human experts to be both valid and insightful. SpatialAgent [339] achieved expert-level performance on spatial biology datasets comprising over two million single-cell measurements. Beyond biology, LLM-RDF [283] integrates specialized analytical agents–including a Spectrum Analyzer and a Result Interpreter–that process experimental feedback to directly inform the next stages of chemical synthesis.

##### 4.4. Synthesis, Validation, and Evolution

The final stage of the agentic scientific loop involves synthesizing outcomes, validating hypotheses, and refining future lines of inquiry. This process heavily leverages collaboration between agents and advanced

##### memory mechanisms.

To ensure robustness, agents can engage in evidence synthesis and critique, emulating peer review by assessing the plausibility of claims [254]. This is often implemented in deliberative multi-agent systems where agents challenge and refine each other’s conclusions [359, 73]. Automated validation further strengthens findings through reproducibility checks [316, 365]. Crucially, the agent undergoes adaptive refinement, where it evolves its strategy based on cumulative experience. This relies on memory frameworks like Reflexion [293], where agents learn from a repository of past successes and failures. This evolution can be described as updating the agent’s internal policy ϕ based on a learning function L applied to its memory M of past trajectories (hypothesis, plan, result tuples):

ϕt+1 ← L(ϕt, Mt) (8)

The agent’s planning engine can then use this refined policy to guide long-term strategy, for instance by using MCTS to optimize hypothesis selection over an entire research campaign [275] or applying formal verification to refine its internal logic [274].

This final stage faces the most profound long-term challenges. The core difficulty is enabling long-term causal reasoning, as scientific insights can emerge from connecting experiments conducted months or even years apart. Existing memory systems are ill-equipped to maintain such extended, causally-linked histories with the high fidelity required for ensuring the reproducibility and integrity of discoveries. This is the ultimate test of an agentic system: not just executing a single loop, but learning and improving over many loops to conduct a long-horizon research project. Successfully managing this iterative process of self-correction and knowledge accumulation is the key to transforming agents from single-task tools into true partners in sustained scientific discovery.

Agentic systems have begun to demonstrate these abilities. The Sparks framework [96], for instance, integrates generation-and-reflection agents to autonomously discover two novel protein design rules via iterative self-correction. OriGene [437] embeds a self-evolving architecture that assimilates experimental and human feedback to progressively refine its disease-targeting protocols. In single-cell data analysis, CellAgent [367] employs a recursive evaluator-planner loop that critiques and improves analysis pipelines, yielding expert-level interpretations. Targeted discovery optimization is also realized in MOOSE-Chem3 [210], which proposes an experiment-guided candidate ranking strategy. By learning from past hypothesis performance, the system adaptively prioritizes the most promising next experiments–closing the loop between evaluation and exploration.

##### 4.5. Fully Autonomous Research Pipeline

An emerging frontier in Agentic Science is the development of frameworks that automate the entire scientific research pipeline, from idea generation to discovery and reporting. These systems aim to construct a productive cycle of hypothesis, experimentation, and analysis, effectively creating an autonomous or semiautonomous researcher (Table 7).

Early frameworks such as The AI Scientist [219] and NovelSeek [323] established this paradigm by proposing comprehensive, closed-loop systems capable of performing research across multiple domains. The AI Scientist demonstrated a fully automated workflow that generates ideas, writes and executes code, and drafts a full scientific paper, applying it to subfields within machine learning. Similarly, NovelSeek showcased a unified multi-agent framework that achieved performance gains in tasks like reaction yield and enhancer activity prediction. Other systems like Dolphin [404] emphasize a feedback-driven loop where ideas are refined based on prior experimental results and literature analysis, demonstrating continuous performance

##### Table 7: Paradigms of Fully Autonomous Research Pipelines. Note that we only report the most significantfeatures of each paper.

Pipeline Paradigm Core Contribution & Mechanism Representative Systems & Works

Foundational End-to-End Frameworks

Establishes the viability of a complete, closed-loop research cycle. These systems integrate hypothesis generation, coding, experimentation (often virtual), and reporting into a single, cohesive workflow.

The AI Scientist [219], NovelSeek [323], Dolphin [404], X-Master [46], DiscoveryWorld (evaluation environment) [146]

Domain-Specific Automation

Applies the end-to-end paradigm to specialized, high-impact scientific domains. This often involves interfacing with real-world lab robotics, complex simulators, or highly structured domain-specific data formats.

Coscientist [30], LLM-RDF [282], MatPilot [248], Biomni [136], SpatialAgent [339], PROTEUS [71], OriGene [437], The Virtual Lab [313], AI coscientist [99]

Multi-Agent Collaborative Structures

Emulates the collaborative and adversarial nature of scientific inquiry using teams of agents. These systems explore different organizational structures (e.g., Socratic dialogue, hierarchical teams, peer review) to enhance creativity and rigor.

VirSci [305], MAPS [424], DORA [242], MDAgents [164], AgentRxiv (cross-system collaboration) [286]

Self-Evolving & Adaptive Systems

Focuses on the pipeline’s ability to learn and improve over time. These agents autonomously refine their strategies, expand their toolkits, or update their internal knowledge based on cumulative experience and feedback.

STELLA [155], Agent Hospital [187], ResearchAgent [13], OriGene [437], AlphaEvolve [250]

Human-in-the-Loop Integration

Explicitly designs the pipeline to incorporate human expertise and oversight. These frameworks treat the human researcher as a collaborator, leveraging their feedback to guide the autonomous process and ensure alignment with scientific goals.

Agent Laboratory [287], Conversational Health Agents [1], MatPilot [248]

improvement on tasks such as 3D point classification. These foundational efforts established the viability of end-to-end agentic research pipelines.

Building on this general paradigm, subsequent work has specialized these pipelines for high-impact scientific domains, often integrating with real-world laboratory hardware or complex simulation tools. In chemistry, Coscientist [30] demonstrated a landmark achievement by using a GPT-4-powered agent to autonomously design, plan, and execute a palladium-catalyzed cross-coupling reaction in a physical lab. This was supported by other systems like LLM-RDF [282], a multi-agent framework with specialized agents for literature scouting, experiment design, and result interpretation to automate chemical synthesis development. This approach was also extended to materials science with MatPilot [248], which uses a human-machine collaborative framework for materials discovery. In biomedicine, Biomni [136] acts as a general-purpose agent that autonomously builds its own action space by mining tools and protocols from publications, achieving strong generalization across tasks like drug repurposing and molecular cloning. More specialized agents like SpatialAgent [339] and PROTEUS [71] have achieved expert-level performance in complex fields like spatial biology and proteomics, respectively. The feasibility of virtual research teams was shown by The Virtual Lab [313], where a team of LLM agents designed novel SARS-CoV-2 nanobodies that were later experimentally validated. Similarly, an AI co-scientist [99] proposed and validated novel epigenetic targets for liver fibrosis. The scope of agentic pipelines extends even to pure mathematics and computer science, with ToRA [100] integrating symbolic solvers for mathematical reasoning and AlphaEvolve [250] using an evolutionary coding agent to discover novel, provably correct algorithms, including an improvement over Strassen’s matrix multiplication.

A key structure in these general pipelines is the use of multi-agent systems to emulate the collaborative nature of scientific research. The core insight, demonstrated by systems like VirSci [305], is that a team of collaborative agents can generate more innovative and impactful scientific ideas than a single agent. These systems explore diverse collaboration structures. For example, MAPS [424] employs a team of seven agents inspired by personality traits and Socratic dialogue to solve multimodal scientific problems. DORA [242] utilizes hierarchical teams of generalist and specialist agents to automate the generation of research reports. In the medical domain, MDAgents [164] dynamically adapts the collaboration structure–assigning tasks to solo or group agents–based on the complexity of the medical decision, leading to improved performance on clinical diagnosis benchmarks. Extending collaboration beyond a single system, AgentRxiv [286] introduces a novel framework where multiple agent "laboratories" upload and retrieve research from a shared preprint server, enabling them to iteratively build on each other’s work and achieve faster progress than isolated systems.

The long-term success of these pipelines depends on their ability to learn, evolve, and effectively integrate human expertise. Self-evolution is a central theme in systems like STELLA [155], a biomedical agent that autonomously improves its own performance by dynamically expanding its library of tools and reasoning templates. This enables its accuracy on benchmarks to nearly double with increased operational experience. Similarly, Agent Hospital [187] introduces a medical simulation where doctor agents evolve and improve their diagnostic capabilities by treating tens of thousands of simulated patients. Iterative refinement through agent-based peer review is another powerful mechanism, as seen in ResearchAgent [13], which uses a panel of reviewing agents to provide feedback and progressively enhance research ideas generated from scientific literature. Recognizing the value of human oversight, frameworks like Agent Laboratory [287] and Conversational Health Agents [1] are explicitly designed to incorporate human feedback at various stages, from idea generation to final report generation, ensuring that the autonomous process remains aligned with researcher goals and significantly improving research quality while reducing costs.

Underpinning these complex research pipelines are foundational agent capabilities and the critical need for robust evaluation methods. The ability to perform complex, tool-augmented reasoning is a prerequisite for any scientific agent. Systems like X-Master [46] are designed to validate this core competence, achieving state-of-the-art performance on exceedingly difficult benchmarks like Humanity’s Last Exam by emulating how human researchers flexibly interact with tools. A crucial upstream capability is open-domain hypothesis discovery, where agents must generate novel and valid scientific hypotheses directly from unstructured data like raw web corpora, a challenge tackled in [393]. Given the complexity of these end-to-end systems, evaluating their capacity for genuine scientific discovery is a major challenge. To address this, specialized evaluation environments are being developed. DiscoveryWorld [146] is a virtual environment that provides a suite of simulated, multi-modal scientific tasks, enabling the benchmarking of an agent’s ability to complete a full discovery cycle in a controlled and repeatable setting.

### 5. Agentic Life Sciences Research

The application of agentic AI systems is rapidly transforming life sciences research, a domain characterized by vast, complex datasets and intricate, multi-step experimental workflows. From genomics and proteomics to drug discovery and protein engineering, AI agents are being developed to automate data analysis, generate novel hypotheses, design experiments, and even interpret results, thereby accelerating the pace of discovery. These systems typically employ a multi-agent architecture, where specialized agents (e.g., planner, executor, analyst) collaborate to tackle complex problems that traditionally require significant human expertise and labor. This section surveys the emerging landscape of agentic systems in life sciences, categorized by their

![image 62](Wei et al._2025_From AI for Science to Agentic Science A Survey on Autonomous Scientific Discovery_images/imageFile62.png)

- Figure 7: Agentic AI-based Natural Scientific Research. Note that only representative tasks are shown in the figure.


primary application domain (Table 8 and Table 9).

##### 5.1. General Frameworks and Methodologies

Beyond specialized applications, a number of projects focus on creating foundational, adaptable agentic frameworks capable of addressing a wide range of biomedical research tasks. These systems emphasize self-evolution, modular design, and the integration of scientific principles to build more robust and versatile AI research assistants.

STELLA [155] is a self-evolving AI agent designed to overcome the limitations of static toolsets. Its method is a multi-agent architecture featuring two core adaptive mechanisms: an evolving Template Library for reasoning strategies and a dynamic Tool Ocean that expands as a dedicated agent autonomously discovers and integrates new bioinformatics tools. This design allows STELLA to learn from experience; its results show that its accuracy on challenging biomedical benchmarks systematically improves with increased trials, outperforming leading models. Biomni [136] is presented as a general-purpose biomedical AI agent designed for flexibility across a wide array of tasks. Its method is based on decomposing complex user queries into multi-step plans and executing them by dynamically selecting from an expanding set of tools. m-KAILIN [366] is presented as a knowledge-driven agentic framework for biomedical corpus distillation, designed to enhance large language model training. Its method is based on a multi-agent collaboration architecture guided by the MeSH knowledge hierarchy, where specialized agents autonomously generate, evaluate, and refine question–answer pairs from scientific literature to produce high-quality, ontology-aligned datasets for biomedical LLMs. BioResearcher [221] is another end-to-end automated system that employs a modular, multi-agent architecture for search, literature processing, experimental design, and programming. A key feature of its method is an LLM-based reviewer for in-process quality control, which enabled the system to achieve an average execution success rate of 63.07% across eight previously unmet research objectives. A more theoretical framework, PiFlow [266], recasts automated scientific discovery as a structured uncertainty reduction problem. Its information-theoretical method guides a multi-agent system’s exploration using

- Table 8: Classification of Agentic Systems in Life Sciences, organized to correspond with the survey text. Column Key: Hypo.: Observation or Hypothesis Generation, Exper.: Experimental Planning or Execution, Analysis: Data and Result Analysis, Validation: Synthesis, Validation, and Evolution. ▲ means level 2 and ⋆ means level 3.


Core Process Paper Application Domain Hypo. Exper. Analysis Validation Level

General Biomedical Research Frameworks Biomni [136] General Biomedical Tasks ✓ ✓ ▲ STELLA [155] Self-Evolving Research ✓ ✓ ✓ ▲ BioResearcher [221] End-to-End Dry Lab Research ✓ ✓ ✓ ⋆ PiFlow [266] Principled Scientific Discovery ✓ ✓ ✓ ⋆ Empowering BD [87] Perspective on AI Scientists - - - - Healthflow [452] Autonomous Healthcare Research ✓ ✓ ✓ ✓ ⋆

Genomics, Transcriptomics, and Multi-Omics Analysis

BIA [373] Bioinformatics Workflow ✓ ✓ ✓ ▲ CellAgent [367] scRNA-seq Analysis ✓ ✓ ✓ ▲ TAIS [204] Gene Expression Analysis ✓ ✓ ▲ CRISPR-GPT [135] Gene-Editing Design ✓ ▲ SpatialAgent [339] Spatial Biology ✓ ✓ ✓ ✓ ⋆ PhenoGraph [249] Spatial Transcriptomics ✓ ✓ ▲ BioAgents [237] Bioinformatics Analysis ✓ ▲ BioMaster [306] Bioinformatics Workflow ✓ ✓ ✓ ▲ TransAgent [418] Transcriptional Regulation ✓ ✓ ▲ CompBioAgent [419] scRNA-seq Exploration ✓ ▲ PerTurboAgent [114] Perturb-seq Design ✓ ✓ ✓ ▲ PROTEUS [71, 273] Proteomics/Multi-Omics ✓ ✓ ✓ ✓ ⋆ CellVoyager [6] scRNA-seq Discovery ✓ ✓ ✓ ✓ ⋆ AstroAgents [284] Mass Spectrometry Analysis ✓ ✓ ✓ ✓ ⋆ BioDiscoveryAgent [281] Perturbation Experiment Design ✓ ✓ ⋆ OmniCellAgent [134] scRNA-seq Data-driven Biomedical Research ✓ ✓ ✓ ✓ ⋆ GeneAgent [349] Gene Set Knowledge Discovery ✓ ✓ ✓ ✓ ⋆ PrimeGen [348] Primer Design ✓ ✓ ▲

Protein Science and Engineering

ProtAgents [91] De Novo Protein Design ✓ ✓ ▲ Sparks [96] Protein Principle Discovery ✓ ✓ ✓ ✓ ⋆

Drug and Therapeutic Discovery The Virtual Lab [313] Nanobody Design ✓ ✓ ✓ ✓ ▲ OriGene [437] Therapeutic Target Discovery ✓ ✓ ✓ ✓ ⋆ LLM Agent for DD [251] Drug Discovery Pipeline ✓ ▲ TxAgent [88] Precision Therapy ✓ ✓ ✓ ▲ Robin [97] Therapeutic Candidate Discovery ✓ ✓ ✓ ✓ ⋆ DrugAgent [209] Drug Discovery Programming ✓ ✓ ✓ ▲ LIDDIA [11] In Silico Drug Discovery ✓ ✓ ✓ ⋆ PharmAgents [82] Virtual Drug Discovery ✓ ✓ ✓ ⋆ CLADD [179] RAG-based Drug Discovery ✓ ✓ ▲ Tippy [77] DMTA Cycle Automation ✓ ✓ ✓ ⋆ ACEGEN [33] Generative Drug Design ✓ ▲ AI Co-scientist [99] Drug Repurposing & Target Discovery ✓ ✓ ✓ ▲ Exploring Modularity [333] Meta-Analysis of Drug Discovery Agents - - - - DO Challenge [296] Benchmark for Drug Discovery Agents - - - - -

scientific principles, which resulted in a 73.55% increase in discovery efficiency and a 94.06% enhancement

in solution quality in domains including biomolecule discovery. Finally, a perspective piece envisions future "AI scientists" as collaborative agents that integrate AI models, biomedical tools, and experimental platforms [87]. The authors argue that such systems, which feature structured memory for continual learning, will empower human researchers by handling large-scale data analysis and repetitive tasks, leaving creative and strategic oversight to humans.

##### 5.2. Genomics, Transcriptomics, and Multi-Omics Analysis

The fields of genomics, transcriptomics, and other omics disciplines are inundated with high-dimensional data from technologies like single-cell RNA sequencing (scRNA-seq), spatial transcriptomics, and mass spectrometry. Key challenges include the need for specialized computational skills to process and interpret this data, the difficulty of integrating multi-modal data, and the labor-intensive nature of designing and executing analysis workflows. AI agents are being developed to make accessible and automate these complex analyses.

A significant focus has been on automating single-cell data analysis. BIA [373] is an intelligent agent designed to autonomously perform bioinformatics analysis from natural language. Its method involves using an LLM to manage the entire pipeline, from data extraction and processing to workflow design, code generation, and final reporting, with a focus on scRNA-seq. The results demonstrate BIA’s proficiency in complex information processing and task execution, showcasing a viable path to automated analysis. Similarly, CellAgent [367] is a multi-agent framework designed for full automation. Its method is based on a hierarchical team of LLM-driven agents—a planner, executor, and evaluator—that are coordinated by a hierarchical decision-making mechanism. Crucially, it incorporates a self-iterative optimization loop that allows the system to autonomously refine its choice of tools and hyperparameters. When evaluated on a large benchmark, CellAgent consistently identified optimal analysis strategies, achieving high-quality results without human intervention. To enhance accessibility, CompBioAgent [419] offers a user-friendly web application that converts natural language queries into visualizations. Its method integrates an LLM with established platforms like CellDepot and Cellxgene VIP, allowing non-programmers to explore scRNA-seq data interactively. Shifting from executing predefined tasks to autonomous discovery, CellVoyager [6] is an agent that autonomously explores scRNA-seq datasets to generate novel hypotheses. Its method involves conditioning its exploration on a record of prior user-run analyses, allowing it to seek out new biological insights. In case studies, CellVoyager’s findings were rated as creative and sound by the original study authors, and it successfully discovered a previously unreported link between increased transcriptional noise and aging in the brain.

Agents are also being tailored for other specific data types and experimental designs. CRISPR-GPT [135] is an LLM agent that automates the intricate design of CRISPR gene-editing experiments. Its method augments an LLM with domain-specific knowledge and external tools to assist non-experts in selecting CRISPR systems, designing guide RNAs, and drafting experimental protocols. Its effectiveness was validated in a real-world use case. For analyzing gene expression data, the Team of AI-made Scientists (TAIS) [204] framework simulates a human research team. The method uses multiple LLMs to represent a project manager, a data engineer, and a domain expert that collaborate to identify disease-predictive genes. For designing sequential experiments, PerTurboAgent [114] is a self-planning agent that excels at designing iterative Perturb-seq experiments. Through self-directed data analysis and knowledge retrieval, it prioritizes genes for subsequent rounds of testing, and its performance was shown to outperform existing active learning strategies in identifying impactful gene perturbations.

The analysis of spatial and multi-omics data presents further challenges of integration and interpretation.

SpatialAgent [339] is a fully autonomous agent for spatial biology research. Its method combines LLMs with dynamic tool execution and adaptive reasoning to manage the entire research pipeline, from experimental design to hypothesis generation. On complex datasets, its performance matched or exceeded that of human scientists. For phenotype-driven discovery, PhenoGraph [249] is a multi-agent system that automates the analysis of spatial transcriptomics data. A key aspect of its method is the augmentation of its reasoning with biological knowledge graphs, which enhances the interpretability of its findings. Addressing broader bioinformatics workflows, several agents aim to democratize access. BioAgents [237] uses a multi-agent system built on fine-tuned small language models and Retrieval-Augmented Generation (RAG), enabling accessible, local operation with expert-level performance. BioMaster [306] employs a robust multi-agent framework with enhanced validation and memory management to reliably handle long, complex workflows like RNA-seq and ChIP-seq analysis, outperforming existing methods in scalability and accuracy. TransAgent [418] focuses specifically on transcriptional regulation, with a method that automates complex multi-omics data integration by integrating over 30 specialized tools and 20 data sources. Finally, agents are emerging for proteomics and mass spectrometry. PROTEUS [71, 273] is a fully automated system that takes raw proteomics or multi-omics data as input. Its method uses hierarchical planning and iterative workflow refinement to generate research objectives, analysis results, and novel, evaluable hypotheses. AstroAgents [284] is a multi-agent system designed specifically for hypothesis generation from mass spectrometry data.

##### 5.3. Protein Science and Engineering

Designing novel proteins with specific functions or properties is a central goal in synthetic biology and biomedical engineering. This process involves navigating a vast sequence space and understanding complex relationships between sequence, structure, and function. Current AI models are often limited to specific objectives, lacking the flexibility to incorporate diverse knowledge or perform comprehensive analyses.

To address these limitations, agentic systems are being developed to create a more dynamic and collaborative design environment. ProtAgents [91] introduces a platform for de novo protein design where multiple AI agents with distinct skills collaborate. Its method establishes a dynamic environment where agents specializing in knowledge retrieval, protein structure analysis, and physics-based simulations work in concert. The results demonstrated a synergistic approach where the system designed new proteins with targeted mechanical properties and performed novel analyses, such as calculating natural vibrational frequencies. This collaborative method allows for a more versatile and powerful approach to protein design. Expanding on this, Sparks [96] represents a significant leap towards autonomous scientific discovery. It is a multiagent AI model that autonomously executes the entire discovery cycle: hypothesis generation, experiment design, and iterative refinement, culminating in a final report without human intervention. The method combines generative sequence design, high-accuracy structure prediction, and physics-aware models, with paired generation-and-reflection agents enforcing self-correction. When applied to protein science, Sparks independently uncovered two previously unknown phenomena: a length-dependent mechanical crossover in peptide unfolding force and a chain-length/secondary-structure stability map revealing unexpectedly robust architectures. These results demonstrate Sparks’s ability to conduct rigorous scientific inquiry and discover novel, verifiable design principles, marking a key milestone for agentic science.

##### 5.4. Drug and Therapeutic Discovery

Drug discovery is notoriously long, costly, and prone to failure. The process involves numerous stages, from target identification and lead compound generation to preclinical analysis and optimization. Agentic AI aims to create integrated, automated systems that can streamline this entire pipeline, reason about therapeutic

strategies, and accelerate the identification of promising drug candidates.

Several agent frameworks function as comprehensive, end-to-end virtual drug discovery platforms. PharmAgents [82] simulates a virtual pharmaceutical ecosystem with a method that uses LLM-driven agents equipped with specialized machine learning models to manage the entire workflow, from target discovery and lead compound optimization to in silico analysis of toxicity and synthetic feasibility, establishing a paradigm for autonomous and scalable research. LIDDiA [11] is an autonomous agent whose method leverages LLM reasoning to intelligently navigate the in silico discovery process, strategically balancing exploration and exploitation of chemical space. As a result, it successfully generated molecules meeting key pharmaceutical criteria for over 70% of 30 clinically relevant targets and identified promising novel candidates for the critical EGFR cancer target. DrugAgent [209] focuses on automating the crucial ML programming aspect of drug discovery. Its method employs a Planner agent to formulate high-level ideas and an Instructor agent to translate them into robust code, outperforming baselines with a 4.92% relative improvement in ROC-AUC for drug-target interaction prediction. Bridging the virtual and physical, Tippy [77] is a production-ready multi-agent system designed to automate the full Design-Make-Test-Analyze (DMTA) cycle in a laboratory setting. Its method uses five specialized agents (Supervisor, Molecule, Lab, Analysis, Report) with safety guardrails, demonstrating significant improvements in workflow efficiency and decision-making speed. A modular framework detailed in [251] combines LLM reasoning with domain-specific tools for tasks like molecular generation and refinement. In a case study targeting BCL-2, its iterative refinement process more than doubled the number of candidate molecules that passed key drug-likeness rules. Finally, CLADD [179] proposes a RAG-empowered agentic system that avoids costly domain-specific fine-tuning. Its method dynamically retrieves information from biomedical knowledge bases to contextualize queries, outperforming both general-purpose and domain-specific LLMs on a variety of discovery tasks.

Other agents focus on specific, critical stages of the discovery pipeline where AI can have an outsized impact. For therapeutic target discovery, OriGene [437] acts as a "virtual disease biologist." Its method is a selfevolving multi-agent system that integrates diverse data modalities (genetics, pharmacology, clinical records) and uses human and experimental feedback to refine its reasoning. OriGene outperformed human experts on a large benchmark and, critically, nominated two previously underexplored targets for liver (GPR160) and colorectal cancer (ARG2) that showed significant anti-tumor activity in patient-derived organoid models. Also demonstrating real-world discovery, Robin [97] is a multi-agent system that automated the intellectual steps of discovery, from background research to experimental design. This led to the identification of ripasudil, a clinically used ROCK inhibitor, as a novel therapeutic candidate for dry age-related macular degeneration (dAMD). Robin then proposed and analyzed a follow-up RNA-seq experiment to elucidate its mechanism of action. The AI co-scientist from [99] utilizes a "generate, debate, and evolve" methodology, where agents use a tournament evolution process to refine hypotheses. This approach led to the discovery of promising drug repurposing candidates for acute myeloid leukemia and novel epigenetic targets for liver fibrosis, both of which were subsequently validated in lab.

Agents are also being developed for experimental design and specialized therapeutic reasoning. BioDiscoveryAgent [281] designs genetic perturbation experiments by leveraging its intrinsic biological knowledge, avoiding the need for a pre-trained model or Bayesian acquisition function. This method led to a 21% average improvement in predicting relevant genetic perturbations over specialized baselines. TxAgent [88] is an agent specialized in therapeutic reasoning. Its method leverages a "ToolUniverse" of 211 validated tools to analyze drug interactions and contraindications, achieving 92.1% accuracy on open-ended drug reasoning tasks. ACEGEN [33] is a streamlined toolkit using reinforcement learning to create generative agents for drug design, which showed performance comparable to or better than other state-of-the-art generative algorithms. For nanomedicine, the Virtual Lab [313] used a team of LLM agents (chemist, computer scientist, critic)

- Table 9: Examples of Validated Scientific Discoveries Achieved by AI Agents in Life Sciences.


Agent System Application Domain Novel Scientific Contribution or Validated Discovery ProtAgents [91] De Novo Protein Design Designed new proteins and obtained new first-principles data (natural vibrational

frequencies) via physics simulations.

The Virtual Lab [313]

Nanobody Design for SARS-CoV-2 Designed 92 new nanobodies, with experimental validation confirming two candidates exhibit improved binding to recent SARS-CoV-2 variants (JN.1 or KP.3).

Sparks [96] Protein Principle Discovery Discovered two previously unknown phenomena: 1) a length-dependent mechanical crossover in peptide unfolding force, establishing a new design principle, and 2) a stability map revealing robust beta-sheet architectures and a "frustration zone" in mixed folds.

OriGene [437] Therapeutic Target Discovery Nominated and validated previously underexplored therapeutic targets for liver cancer (GPR160) and colorectal cancer (ARG2), which showed significant anti-tumor activity in patient-derived models.

Robin [97] Therapeutic Candidate Discovery Identified and validated a novel treatment for dry age-related macular degeneration (dAMD), the clinically-used drug ripasudil. It also proposed a novel therapeutic target (ABCA1) by elucidating the drug’s mechanism.

CellVoyager [6] scRNA-seq Discovery Autonomously re-analyzing existing datasets, it generated new, validated insights: 1) discovered that CD8+ T cells in COVID-19 are primed for pyroptosis, and 2) found a previously unreported link between increased transcriptional noise and aging in the brain’s subventricular zone.

AI co-scientist [99] Drug Repurposing & Target Discovery Proposed and validated new uses for existing drugs for acute myeloid leukemia. It also discovered and validated new epigenetic targets for liver fibrosis using human hepatic organoids and independently discovered a novel gene transfer mechanism in bacteria.

guided by a human to design novel nanobody binders for SARS-CoV-2. The agents created a design pipeline using ESM and AlphaFold, resulting in 92 candidates, two of which were experimentally validated to have improved binding to recent viral variants.

Finally, some work focuses on benchmarking and understanding the agentic systems themselves. The DO Challenge [296] introduces a benchmark to evaluate the ability of agents to design and implement drug discovery pipelines, testing their capacity to navigate chemical space and manage resources. Another study critically examines the modularity of these systems, finding that core components like LLMs are not easily interchangeable without significant prompt re-engineering, highlighting the need for research into developing stable and scalable solutions [333].

### 6. Agentic Chemistry Research

The application of agentic AI is rapidly transforming chemical research, automating complex processes from hypothesis generation to experimental execution and analysis. By integrating large language models (LLMs) with specialized chemical tools and robotic platforms, these AI agents can autonomously design and perform experiments, discover novel materials, and optimize synthetic reactions. This section surveys the emerging landscape of agentic chemistry, categorized by the primary function of the agents, to highlight the major challenges, proposed frameworks, and significant achievements (Table 10 and Table 11).

##### 6.1. General Frameworks and Methodologies

Beyond specific applications, a significant body of research focuses on developing the foundational methodologies, architectures, and tools that support chemical AI agents. This work addresses broad challenges such as effective tool integration, robust reasoning, hypothesis generation, and literature comprehension, which are essential for creating truly autonomous and versatile scientific agents.

- Table 10: Classification of Agentic Systems in Chemistry Science, organized to correspond with the survey text. The checkmark (✓) indicates the system’s primary capabilities. Column Key: Hypo.: Observation or Hypothesis Generation, Exper.: Experimental Planning or Execution, Analysis: Data and Result Analysis, Validation: Synthesis, Validation, and Evolution. Level: Level of autonomy. ▲ means level 2 and ⋆ means level 3.


Core Process

Paper Application Domain Hypo. Exper. Analysis Validation Level General Frameworks and Methodologies

ChemCrow [35] Organic Synthesis ✓ ✓ ▲ ChemAgents [299] Hierarchical Multi-Agent Robotic Chemist ✓ ✓ ✓ ✓ ⋆ MOOSE-Chem [395] Rediscovery of Scientific Hypotheses ✓ ✓ ▲ MOOSE-Chem3 [210] Experiment-Guided Hypothesis Ranking ✓ ✓ ✓ ▲ ChemMiner [55] Agent for Chemical Literature Data Mining ✓ ✓ ▲ Eunomia [7] Agent for Building Datasets From Literature ✓ ✓ ✓ ▲ ChemAgent [358] Tool Learning ✓ ✓ ✓ ▲ ChemHAS [196] Hierarchical Agent Stacking to Enhance Tools ✓ ✓ ▲ ChemToolAgent [401] Meta-Analysis of Tool Impact ✓ ✓ ✓ ▲ Chemagent [318] Improving Reasoning With a Library ✓ ✓ ✓ ▲ LabUtopia [189] Simulation for Embodied Agents ✓ ▲ CACTUS [236] Agent Connecting Tools for Problem-Solving ✓ ✓ ▲ GVIM [227] Intelligent Research Assistant System ✓ ✓ ✓ ✓ ⋆ MT-Mol [162] Multi-Agent System for Molecular Optimization ✓ ✓ ✓ ✓ ⋆ CSstep [48] Multi-Agent RL for Exploring Chemical Space ✓ ✓ ✓ ▲ CRAG-MoW [41] Mixture-of-Workflows for Multi-Modal Search ✓ ✓ ✓ ▲

Organic Synthesis and Reaction Optimization

Coscientist [30] Reaction Optimization (Pd Cross-Coupling) ✓ ✓ ✓ ✓ ⋆ LLM-RDF [282] End-to-End Synthesis Development ✓ ✓ ✓ ✓ ⋆ Chemist-X [54] Reaction Condition Optimization ✓ ✓ ✓ ✓ ⋆ ORGANA [67] Robotic Chemistry Experimentation ✓ ✓ ✓ ▲ Dai et al. [64] Exploratory Synthesis With Mobile Robots ✓ ✓ ✓ ✓ ⋆ Strieth-Kalthoff et al. [304] Closed-Loop Discovery of Laser Emitters ✓ ✓ ✓ ✓ ⋆ AutoChemSchematic AI [303] Generation of Industrial Process Diagrams ✓ ✓ ✓ ⋆

Generative Chemistry and Molecular Design

ChatMOF [159] Generative Design of MOFs ✓ ✓ ✓ ▲ MOFGen [140] De Novo Discovery of Synthesizable MOFs ✓ ✓ ✓ ✓ ⋆ OSDA Agent [132] De Novo Design of Molecules for Zeolites ✓ ✓ ✓ ⋆ ChemReasoner [302] Heuristic Search for Catalyst Discovery ✓ ✓ ✓ ✓ ⋆ Horwood & Noutahi [124] Molecular Design via Reinforcement Learning ✓ ✓ ✓ ✓ ⋆

Computational and Quantum Chemistry

El Agente Q [455] Autonomous Quantum Chemistry Workflows ✓ ✓ ✓ ▲ Aitomia [126] Intelligent Assistant for Atomistic Simulations ✓ ✓ ▲ ChemGraph [262] Automated Computational Chemistry Workflows ✓ ✓ ✓ ▲ xChemAgents [263] Explainable Quantum Chemistry Prediction ✓ ✓ ✓ ▲

Several papers propose general-purpose agent frameworks designed for broad chemical tasks. ChemCrow is an LLM agent augmented with 18 expert-designed tools to accomplish tasks across organic synthesis, drug discovery, and materials design [35]. It demonstrated its capability by autonomously planning and

executing the synthesis of an insect repellent and several organocatalysts. Similarly, ChemAgents is a hierarchical multi-agent system powered by an on-board LLM that coordinates four role-specific agents–a Literature Reader, Experiment Designer, Computation Performer, and Robot Operator–to execute complex, multi-step experiments with minimal human intervention [299]. Methodologies for reasoning and hypothesis generation are also critical. MOOSE-Chem formalizes hypothesis discovery by decomposing the task into retrieving inspirations from literature, composing hypotheses, and ranking them, successfully rediscovering the core innovations of 51 recent high-impact papers [395]. Following this, MOOSE-Chem3 tackles the problem of ranking these hypotheses by introducing an "experiment-guided" approach that uses a simulator to generate feedback, allowing it to prioritize candidates based on the outcomes of previously tested ones [210].

A central theme is the effective use of tools and knowledge. ChemAgent (by Wu et al.) integrates 137 external chemical tools using a Hierarchical Evolutionary Monte Carlo Tree Search (HE-MCTS) framework for planning and execution, significantly improving performance on QA and discovery tasks [358]. Taking a different angle, ChemHAS explores how agents can enhance the tools themselves, proposing a hierarchical agent stacking method to compensate for the inherent prediction errors of chemistry tools [196]. However, ChemToolAgent provides a nuanced analysis, finding that while tools are beneficial for specialized tasks like synthesis prediction, they do not consistently improve performance on general chemistry questions where core knowledge and reasoning are paramount [401]. To improve knowledge integration, Chemagent (by Tang et al.) uses a dynamic, self-updating library compiled from decomposed sub-tasks to enhance reasoning, achieving performance gains of up to 46% on the SciBench benchmark [318]. For knowledge extraction, systems like ChemMiner [55], which uses three specialized agents for text, multimodal, and synthesis analysis, and Eunomia [7], which autonomously creates structured datasets from unstructured text, are designed to mine accurate data from the scientific literature.

Finally, some works provide crucial infrastructure for the field. LabUtopia offers a comprehensive simulation and benchmarking suite specifically for training and evaluating scientific embodied agents [189]. It includes an accurate simulator (‘LabSim’), a procedural scene generator (‘LabScene’), and a hierarchical benchmark (‘LabBench’), providing a rigorous platform to advance the integration of perception, planning, and control in laboratory settings.

##### 6.2. Organic Synthesis and Reaction Optimization

Organic synthesis is a key area of chemistry, yet it presents considerable challenges, including the laborious optimization of reaction conditions, the creative design of multi-step synthetic routes, and the safe execution of complex experimental protocols. Agentic AI is being developed to address these issues by automating the entire workflow, from experimental design to robotic execution and result interpretation, thereby accelerating the pace of discovery.

A primary focus has been on automating reaction optimization and execution. For instance, Coscientist [30] is an AI system driven by GPT-4 that showcases the ability to autonomously design, plan, and execute complex experiments from start to finish. In a notable demonstration, it successfully optimized the reaction conditions for palladium-catalyzed cross-couplings, a widely used and important reaction class. Similarly, the LLM-based Reaction Development Framework (LLM-RDF) [282] employs a suite of six specialized agents– a Literature Scouter, Experiment Designer, Hardware Executor, Spectrum Analyzer, Separation Instructor, and Result Interpreter–to manage the entire synthesis development workflow. The framework demonstrated its utility by guiding the end-to-end process for several reaction types, including copper/TEMPO catalyzed alcohol oxidation, from literature review and condition screening to scale-up and purification. Addressing the same challenge, Chemist-X [54] targets reaction condition optimization by implementing a novel

retrieval-augmented generation (RAG) scheme. This allows the agent to first consult molecular and literature databases to narrow the search space before an AI controller executes the proposed conditions in a wet lab using an automated robotic system.

Another line of research focuses on integrating agentic AI with robotics to physically perform experiments. ORGANA [67] acts as a robotic assistant that automates diverse and labor-intensive experiments such as solubility testing, pH measurement, and recrystallization. It interacts with chemists via natural language to derive experimental goals and provides detailed logs, with user studies showing it reduces physical demand by over 50% and saves researchers an average of 80% of their time. Autonomous mobile robots [64] have been deployed to create a more flexible automated lab. These robots physically shuttle samples between standard, unmodified laboratory instruments like a synthesis platform, an LC-MS, and an NMR spectrometer. This approach allows automated systems to share equipment with human researchers and enables a heuristic decision-maker to process orthogonal data from multiple analysis techniques to guide the experimental campaign. A landmark achievement in this area is the delocalized, asynchronous, closed-loop discovery of organic laser emitters [304]. This work utilized a cloud-based AI planner to coordinate robotic synthesis and characterization across five international laboratories. This distributed workflow resulted in the discovery of 21 new state-of-the-art materials, demonstrating a blueprint for global, accessible scientific discovery. Finally, bridging the gap from laboratory discovery to industrial application, AutoChemSchematic AI [303] is a closed-loop, physics-aware framework designed to automatically generate industrial-scale Process Flow Diagrams (PFDs) and Piping and Instrumentation Diagrams (P&IDs). It integrates specialized language models with a process simulator (DWSIM) to ensure the generated plans are physically viable, streamlining the transition from bench-scale chemistry to full-scale manufacturing.

##### 6.3. Generative Chemistry and Molecular Design

A major frontier in chemistry is the de novo design of novel molecules and materials with precisely tailored properties. This involves navigating a vast and complex chemical space to identify promising candidates. Agentic AI excels at this generative task by combining large-scale knowledge models with targeted search strategies and computational validation.

The design of porous materials has been a significant target for generative agents. ChatMOF [159] is an autonomous AI system that uses GPT-4 to process natural language queries for predicting properties and generating new Metal-Organic Frameworks (MOFs). Its architecture comprises three core components– an agent, a toolkit, and an evaluator–and has demonstrated high accuracy (over 95% for prediction) in performing its designated tasks. Building on this, MOFGen [140] employs a more complex system of interconnected agents to discover novel, synthesizable MOFs. This system includes a large language model as a proposer, a diffusion model for generating 3D crystal structures, quantum mechanical agents for computational validation, and synthetic-feasibility agents guided by expert rules. This powerful combination led to the generation of hundreds of thousands of novel MOF structures and resulted in the successful experimental synthesis of five entirely new “AI-dreamt” MOFs.

Agents are also being created to design specific functional molecules for complex applications. For zeolite synthesis, OSDA Agent [132] performs de novo design of Organic Structure Directing Agents (OSDAs) using an LLM-based Actor-Evaluator-Self-reflector framework. The Actor generates potential OSDAs, the Evaluator uses computational chemistry to score them, and the Self-reflector analyzes the results to provide feedback, creating a refinement loop that improves generation quality. For catalyst discovery, ChemReasoner [302] integrates LLM-based reasoning with quantum-chemical feedback. The agent formulates hypotheses about effective catalysts and iteratively refines its search by using feedback from atomistic simulations, which

provide scoring functions based on adsorption energies and reaction barriers to steer the exploration toward highly effective candidates. Another approach utilizes deep reinforcement learning to explore chemical space under realistic constraints [124]. Here, an agent learns to optimize pharmacologically relevant objectives by navigating a space composed only of synthetically accessible molecules. This is achieved by defining state transitions within the Markov decision process as known chemical reactions, effectively using established synthetic routes as a powerful inductive bias to ensure the generated molecules are practical to create.

##### 6.4. Computational and Quantum Chemistry

Computational and quantum chemistry provide powerful tools for understanding molecular behavior, but their use often requires specialized expertise to set up, execute, and interpret complex simulations. Agentic AI is emerging as a solution to make these tools accessible by creating intelligent assistants that can translate natural language prompts into executable workflows, manage simulations, and analyze results.

Several agentic systems function as intelligent assistants for complex simulations. El Agente Q is an LLM-based multi-agent system that dynamically generates and executes quantum chemistry workflows from natural language prompts [455]. It is built on a novel cognitive architecture featuring a hierarchical memory framework that enables flexible task decomposition and adaptive tool selection. It demonstrated robust problem-solving, achieving an average success rate of over 87% on benchmark tasks, and features adaptive error handling through in situ debugging. Similarly, Aitomia is a publicly accessible online platform with AI agents and chatbots that assists both experts and non-experts in running atomistic and quantum chemical simulations [126]. It leverages open-source LLMs, rule-based agents, and a RAG system to handle setup, monitoring, analysis, and summarization for a wide range of tasks, including geometry optimizations and spectra calculations.

Other frameworks focus on creating structured, automated workflows for specific computational tasks. ChemGraph is an agentic framework designed to simplify and automate computational chemistry workflows, such as geometry optimization, vibrational analysis, and thermochemistry calculations [262]. It uses LLMs for natural language understanding and task planning while leveraging graph neural network (GNN)-based foundation models for accurate and efficient calculations, demonstrating that multi-agent decomposition can enable smaller LLMs to match the performance of larger models on complex tasks. Aiming for improved explainability and accuracy, xChemAgents introduces a cooperative agent framework for quantum chemistry property prediction [263]. It comprises two agents: a Selector, which adaptively identifies a sparse, relevant subset of chemical descriptors and provides a natural language rationale, and a Validator, which enforces physical constraints through iterative dialogue. This approach achieved up to a 22% reduction in mean absolute error over baselines while producing human-interpretable explanations.

### 7. Agentic Materials Science Research

This section delves into the application of agentic AI frameworks in materials science, a field ripe for automation due to its vast design spaces and complex, multi-step discovery workflows. We categorize the contributions into three main areas: the design and discovery of novel materials, the automation of simulation and characterization processes, and the development of general discovery platforms (Table 12 and Table 13).

- Table 11: Examples of Validated Scientific Discoveries Achieved by AI Agents in Chemistry.


Agent System Application Domain Novel Scientific Contribution or Validated Discovery

Cloud-based AI Planner [304]

Closed-loop Discovery of Laser Emitters

Discovered 21 new state-of-the-art organic solid-state laser emitters. The agent orchestrated a workflow across five laboratories, leading to the gram-scale synthesis and verification of a material with best-in-class stimulated emission.

ChemCrow [35] Organic Synthesis Guided the discovery of a novel chromophore by autonomously planning

and executing the required synthesis steps. ChemAgents [299] Hierarchical Multi-agent Robotic

Executed complex, multistep experiments that culminated in the discovery and optimization of new functional materials.

Chemist

MOFGen [140] De novo Discovery of Synthesiz-

Designed novel Metal-Organic Frameworks (MOFs), leading to the successful experimental synthesis of five previously unknown "AIdreamt" MOFs, validating the system’s ability to create synthesizable materials.

able MOFs

##### 7.1. General Methodologies and Discovery Platforms

Beyond specialized applications, a significant research effort focuses on creating general, flexible, and robust agentic platforms for materials science. The primary challenges are integrating diverse data sources, ensuring the reliability of LLM-generated knowledge, enabling autonomous planning of complex workflows, and facilitating seamless human-AI collaboration. These general-purpose platforms aim to provide extensible frameworks that can be adapted to various subdomains of materials science.

Several platforms focus on improving the reliability and knowledge-grounding of agents. LLaMP [58] is a retrieval-augmented generation (RAG) framework that uses a hierarchy of agents to interact with materials databases (like the Materials Project) and run simulations. By dynamically fetching and processing data, LLaMP effectively mitigates LLM hallucination without fine-tuning, demonstrating strong performance in retrieving properties like bulk moduli and bandgaps. HoneyComb [423] is another agent system designed specifically for materials science, addressing the issue of outdated or inaccurate knowledge in general-purpose LLMs. It introduces a high-quality, curated materials science knowledge base (MatSciKB) and a tool hub with an inductive method for creating and refining tools, significantly outperforming baseline models on specialized tasks.

Other frameworks concentrate on creating comprehensive, human-in-the-loop "AI scientists". MatPilot [248] is an LLM-enabled AI materials scientist designed for human-machine collaboration. It integrates human cognitive strengths with AI capabilities for information processing and storage. MatPilot can generate hypotheses, design experiments, and control an automated experimental platform, demonstrating a closed loop of iterative optimization and learning. MAPPS (Materials Agent unifying Planning, Physics, and Scientists) [444] aims to grant agents greater autonomy by automating the planning of entire discovery workflows from high-level goals. Its architecture includes a Workflow Planner, a Tool Code Generator that invokes physics-based models, and a Scientific Mediator to incorporate human feedback and manage errors. MAPPS achieved a five-fold improvement in generating stable and novel crystal structures compared to previous models.

The ability to generate and evaluate hypotheses is a critical component of scientific discovery. To this end, researchers have developed a novel dataset and evaluation metric specifically for testing the ability of LLM agents to generate viable materials discovery hypotheses under given constraints [172]. This work provides

- Table 12: Classification of Agentic Systems in Materials Science. The table is organized to correspond with the survey sections. Column Key: Hypo.: Observation or Hypothesis Generation, Exper.: Experimental Planning or Execution, Analysis: Data and Result Analysis, Validation: Synthesis, Validation, and Evolution.


▲ means level 2 and ⋆ means level 3.

Core Process

Paper Application Domain Hypo. Exper. Analysis Validation Level General Methodologies and Discovery Platforms

MatPilot [248] General Materials Discovery ✓ ✓ ✓ ✓ ⋆ LLMatDesign [149] General Materials Design ✓ ✓ ✓ ✓ ⋆ MAPPS [444] Autonomous Materials Discovery ✓ ✓ ✓ ✓ ▲ dZiner [8] Inverse Molecular Design ✓ ✓ ✓ ✓ ⋆ LLaMP [58] Materials Informatics (RAG) ✓ ✓ ✓ ▲ HoneyComb [423] Materials Knowledge Systems ✓ ✓ ✓ ▲ PiFlow [266] General Discovery Methodology ✓ ✓ ✓ ✓ ⋆ Kumbhar et al. [172] Scientific Hypothesis Generation ✓ ✓ ▲ Bazgir et al. [25] Multimodal Data Integration ✓ ✓ ▲

Design and Discovery of Novel Materials

AtomAgents [94, 90] Alloy Design ✓ ✓ ✓ ✓ ⋆ Ghafarollahi et al. [92] Alloy Design ✓ ✓ ✓ ✓ ⋆ SciAgents [95] Biologically Inspired Materials ✓ ✓ ✓ ⋆ PriM [175] Nanomaterial Mechanics ✓ ✓ ✓ ✓ ⋆ TopoMAS [413] Topological Materials ✓ ✓ ✓ ✓ ⋆ metaAgent [130] Electromagnetic Metamaterials ✓ ✓ ✓ ▲ CrossMatAgent [326] Generative Metamaterial Design ✓ ✓ ✓ ✓ ⋆ Lu et al. [220] Inverse Photonic Design ✓ ✓ ✓ ▲

Automated Simulation and Characterization

AILA [232] AFM Nanocharacterization ✓ ✓ ▲ Foam-Agent [407] Computational Fluid Dynamics (CFD) ✓ ✓ ▲ ChemGraph [262] Computational Chemistry (DFT, MD) ✓ ✓ ▲ MechAgents [247] Computational Solid Mechanics ✓ ✓ ▲

a structured framework for advancing and benchmarking the hypothesis-generation capabilities of future agentic systems. Finally, to handle the diverse and siloed nature of materials data, a multicrossmodal agent framework [25] was developed. It uses a team of specialized agents to process different data types (images, text, tables, videos), projecting their insights into a shared embedding space for unified reasoning. This approach enhances data integration and retrieval accuracy without requiring expensive model retraining.

##### 7.2. Design and Discovery of Novel Materials

The design of new materials with specific target properties is a cornerstone of materials science, yet it presents immense challenges. The chemical design space is combinatorially vast, making exhaustive exploration impossible. Traditional methods rely on expert intuition and laborious trial-and-error, which are often slow

and biased. A key challenge is to develop systems that can autonomously navigate this space, generate plausible hypotheses, and iteratively refine designs based on physical principles and computational feedback, thereby accelerating the discovery of materials for applications ranging from sustainable energy to advanced electronics.

Agentic frameworks are being developed to address these challenges by automating the discovery cycle. For instance, SciAgents [95] was designed to automate the discovery of novel biologically inspired materials. The framework employs a multi-agent system that utilizes a large-scale knowledge graph to represent scientific concepts. These agents autonomously generate and refine research hypotheses by identifying hidden relationships in data, leading to the discovery of a new biocomposite with enhanced mechanical properties and sustainability. Similarly, in the realm of alloy design, a widely known as complex multiobjective problem, AtomAgents [94] utilizes a physics-aware multi-agent system to design alloys with superior properties. The agents, with specialized roles in knowledge retrieval, simulation, and analysis, collaborate to navigate the design space, successfully identifying new alloys with enhanced characteristics. A related work automates this process further by integrating a Graph Neural Network (GNN) for rapid property prediction, reducing the reliance on costly simulations and accelerating the discovery of novel NbMoTa-based alloys [92].

Other systems focus on specific classes of advanced materials. TopoMAS [413] is a multi-agent system dedicated to discovering topological materials. It coordinates the entire workflow from data retrieval to first-principles validation, guided by human-AI collaboration. A key feature is its dynamic knowledge graph, which is continuously updated with computational results, enabling iterative knowledge refinement. TopoMAS successfully identified a novel topological phase, SrSbO3. For metamaterials, CrossMatAgent [326] integrates LLMs (GPT-4o) with generative models (DALL-E 3, Stable Diffusion) to automate design. Its hierarchical agent team specializes in tasks like pattern analysis and synthesis, producing simulation-ready designs. Another framework for photonic metamaterials uses an agent to autonomously develop a deep learning model for inverse design based on a desired optical spectrum [220]. In a different approach, the metaAgent [130] operates as a cognitive entity that reasons in natural language to perform complex electromagnetic field manipulations, demonstrating advanced capabilities by planning and executing tasks in collaboration with robots and humans.

Inverse design, which aims to find a material structure given a desired property, is another area of focus. dZiner [8] is an AI agent that performs rational inverse design by leveraging literature insights to propose new compounds (e.g., surfactants, ligands, MOFs) and iteratively evaluates them with surrogate models. The framework supports both fully autonomous and human-in-the-loop workflows. Similarly, LLMatDesign [149] uses LLM agents to translate human instructions into material modifications, demonstrating effective zero-shot adaptation for designing materials with user-defined properties in silico. Other works like PriM [175] and PiFlow [266] emphasize guidance by scientific principles. PriM uses a multi-agent "roundtable" to guide the discovery of nano-helical materials, while PiFlow frames discovery as a principle-guided uncertainty reduction problem, showing significant efficiency gains in discovering nanomaterials, biomolecules, and superconductors.

##### 7.3. Automated Simulation and Characterization

A major bottleneck in materials science is the high level of domain expertise and manual effort required to set up, execute, and analyze computational simulations and physical characterization experiments. Complex software packages often have steep learning curves, and experiments require precise, adaptive control. Automating these workflows can democratize access to powerful scientific tools, reduce human error, and

- Table 13: Examples of Validated Scientific Discoveries Achieved by AI Agents in Materials Science.


Agent System Application Domain Novel Scientific Contribution or Validated Discovery

SciAgents [95] Biologically Inspired Materials Autonomously discovered a new biocomposite material with enhanced mechanical properties and improved sustainability by identifying hidden interdisciplinary relationships and design principles from nature.

TopoMAS [413] Topological Materials In collaboration with human experts, the system guided the identification and confirmation (via first-principles calculations) of novel topological phases in the material Strontium Antimonate (SrSbO3).

AtomAgents [94] Alloy Design Autonomously designed and discovered novel metallic alloys with enhanced properties compared to their pure elemental counterparts, demonstrating the crucial role of solid solution alloying.

enable high-throughput screening and characterization.

Agentic systems are emerging to tackle these challenges by providing natural language interfaces to complex scientific instruments and software. In computational fluid dynamics (CFD), Foam-Agent [407] was developed to automate intricate OpenFOAM simulation workflows. It interprets natural language instructions using a multi-agent framework featuring a hierarchical retrieval system and a dependency-aware file generation process. Critically, its iterative error correction mechanism can diagnose and resolve simulation failures autonomously, achieving a high success rate (83.6%) on benchmark tasks and significantly lowering the expertise barrier for CFD.

Similarly, ChemGraph [262] is an agentic framework designed to streamline computational chemistry workflows. It uses LLMs for task planning and reasoning, allowing users to perform complex calculations (e.g., geometry optimization, thermochemistry) via natural language. The framework intelligently decomposes complex tasks for smaller LLMs and integrates various simulation tools, from machine learning potentials to density functional theory (DFT), making advanced atomistic simulations more accessible. In the field of solid mechanics, MechAgents [247] uses a team of collaborating LLM agents to solve complex elasticity problems. The agents autonomously write, execute, and self-correct code to perform finite element analysis, handling various geometries, boundary conditions, and material laws. The collaborative "criticism" among agents enhances the reliability of the solutions.

Beyond simulation, agents are also being applied to automate physical experiments. AILA (Artificially Intelligent Lab Assistant) [232] is a framework that uses LLM-driven agents to automate atomic force microscopy (AFM). The work introduces AFMBench, a suite for evaluating agent performance across the scientific workflow, from experimental design to data analysis. The study found that multi-agent architectures outperform single agents and highlighted the need for rigorous benchmarking, as domain-specific knowledge (QA proficiency) did not directly translate to effective experimental control.The AutoMat [391] framework was developed as an agentic AI system that autonomously reconstructs atomic crystal structures and predicts material properties from high-resolution microscopy images. Deployed as an end-to-end pipeline integrating denoising, physics-guided template retrieval, symmetry-constrained reconstruction, and ML-based property prediction, it bridges experimental STEM imaging with atomistic simulation—achieving accurate, closed-loop reasoning from microscopy to materials modeling.

- Table 14: Classification of Agentic Systems in Physics and Astronomy Science, organized to correspond with the survey text. Column Key: Level: Automation level of the agent, Hypo.: Observation or Hypothesis Generation, Exper.: Experimental Planning or Execution, Analysis: Data and Result Analysis, Validation: Synthesis, Validation, and Evolution. ▲ means level 2 and ⋆ means level 3.


Core Process

Paper Application Domain Hypo. Exper. Analysis Validation Level Quantum Computing

k-agents [44] Quantum Processor Control ✓ ✓ ✓ ▲

General Frameworks and Methodologies

MoRA [145] Physics Problem Solving ✓ ▲ LP-COMDA [206] Power Converter Design ✓ ✓ ✓ ▲ LLMSat [233] Autonomous Spacecraft Control ✓ ✓ ▲ CosmoAgent [380] Agent-based Civilization Modeling ✓ ✓ ✓ ▲

Astronomy and Cosmology

StarWhisper [337] Supernova Survey Automation ✓ ✓ ✓ ▲ mephisto [311] Galaxy Observation Interpretation ✓ ✓ ✓ ▲ AI Agents [169] Gamma-ray Astronomy Pipelines ✓ ▲ AI Cosmologist [241] Cosmological ML Research ✓ ✓ ✓ ✓ ⋆ SimAgents [433] Cosmological Simulation Setup ✓ ✓ ▲

Computational Mechanics and Fluid Dynamics

OpenFOAMGPT [258] CFD Simulation (OpenFOAM) ✓ ✓ ✓ ▲ OpenFOAMGPT 2.0 [78] CFD Simulation (OpenFOAM) ✓ ✓ ✓ ✓ ⋆ LLM-Agent [205] Structural Beam Analysis (FEM) ✓ ✓ ▲ MechAgents [247] Solid Mechanics (FEM) ✓ ✓ ✓ ▲ AutoGen-FEM [325] Finite Element Analysis Automation ✓ ✓ ✓ ▲

### 8. Agentic Physics and Astronomy Research

The application of agentic AI is rapidly transforming research in physics and astronomy, fields characterized by vast datasets, complex simulations, and intricate experimental procedures. From automating telescope operations to solving complex problems in mechanics and quantum computing, agent-based systems are accelerating the scientific discovery pipeline. These agents assist researchers by managing complex software, analyzing data, formulating and testing hypotheses, and even automating the entire research cycle from literature review to final publication. This section reviews recent advancements, categorized by sub-discipline, showcasing how agentic AI is tackling key challenges in these domains (Table 14 and Table 15).

##### 8.1. General Frameworks and Methodologies

Agentic AI is also being applied to a diverse range of other problems in physics and engineering, from fundamental reasoning to applied system design and theoretical exploration.

A significant challenge for LLMs is scientific reasoning, particularly in physics, where they often exhibit

problem miscomprehension, incorrect concept application, and computational errors. To enhance this capability, the Mixture of Refinement Agents (MoRA) framework was developed [145]. MoRA uses an ensemble of specialized agents to iteratively refine a base solution generated by an LLM, with each agent targeting a different type of error. This approach significantly improved the accuracy of open-source LLMs on physics reasoning benchmarks like SciEval and PhysicsQA by up to 16%. In the field of power electronics, LP-COMDA is a physics-informed autonomous agent designed to automate the modulation design of power converters [206]. An LLM-based planner coordinates with physics-informed tools to iteratively generate and refine designs, providing an explainable workflow that reduced error by 63.2% compared to the next-best method and was over 33 times faster than conventional human-led design processes.

In astronautics, the LLMSat agent was developed to serve as a high-level, goal-oriented controller for autonomous spacecraft, aiming to reduce reliance on human mission control for deep space exploration [233]. Tested in the Kerbal Space Program simulator, the work found that while current LLMs have limitations in handling high-complexity missions, their performance can be improved with advanced prompting frameworks and by carefully defining the agent’s level of authority over the spacecraft. In fundamental physics, the ArgoLOOM framework was developed to act as an agentic AI orchestrator that autonomously coordinates computational tools across cosmology, collider, and nuclear physics domains [20]. Tested on case studies involving sterile-neutrino scenarios, the system demonstrated its ability to link large-scale cosmological simulations with collider and deep-inelastic-scattering analyses through an LLM-driven planning pipeline. In experimental physics, the Accelerator Assistant framework was developed as an agentic AI system capable of autonomously executing multi-stage experiments at a large-scale synchrotron user facility [121]. Deployed at the Advanced Light Source, it translates natural-language prompts into structured execution plans that integrate data retrieval, control-system interaction, and analysis workflows under strict safety and reproducibility constraints, demonstrating a two-order-of-magnitude reduction in experiment preparation time for machine-physics studies. Finally, in a more theoretical application, the CosmoAgent system uses LLM-based agents to simulate interactions between human and hypothetical extraterrestrial civilizations [380]. By programming agents with different worldviews and ethical paradigms, the system explores potential inter-civilizational dynamics, providing a novel tool for studying cooperation and conflict under conditions of asymmetric information.

##### 8.2. Astronomy and Cosmology

Modern astronomy and cosmology face significant challenges driven by the data flood from next-generation telescopes like the James Webb Space Telescope (JWST) and the upcoming Cherenkov Telescope Array (CTA). Key issues include managing complex, large-scale observation schedules, processing and analyzing petabytes of data, and navigating sophisticated simulation software to test theoretical models against observations.

To address the high operational workload in astronomical surveys, the StarWhisper Telescope System was developed as an agent-based observation assistant for the Nearby Galaxy Supernovae Survey (NGSS) [337]. This system automates the entire observational workflow, from generating customized observation lists to executing telescope operations via natural language commands. Its agents analyze images in real-time to detect transients and automatically generate follow-up proposals, significantly reducing the manual effort for astronomers. In the domain of data interpretation, mephisto is a multi-agent framework designed to emulate human reasoning when interpreting multi-band galaxy observations [311]. Mephisto interacts with the CIGALE spectral energy distribution (SED) fitting codebase, employing self-play and tree search to explore hypotheses and build a dynamic knowledge base. This method achieved near-human proficiency in analyzing JWST data, even identifying novel "Little Red Dot" galaxy populations.

For ground-based gamma-ray astronomy, the complexity of instruments like the CTA presents challenges in system control and data analysis. To mitigate this, AI agents have been proposed that are instructionfinetuned on specific documentation and codebases, such as the Gammapy framework [169]. These agents assist users by understanding the environmental context and automating complex tasks, including the maintenance of data models for the Array Control and Data Acquisition (ACADA) system and the generation of code for analysis pipelines.

Several agentic systems aim to automate the entire research workflow. The AI Cosmologist is an agentic system with specialized agents for planning, coding, execution, analysis, and synthesis, capable of autonomously conducting machine learning research from idea generation to paper writing [241]. It mimics the human research process by generating diverse implementation strategies and iterating based on experimental outcomes. Similarly, a multi-agent system built on the autogen/ag2 framework was developed to automate cosmological parameter analysis [178]. This system uses Retrieval Augmented Generation (RAG) and local code execution, demonstrating its potential on data from the Atacama Cosmology Telescope. Another multi-agent system, SimAgents, addresses the bottleneck of translating parameters from academic literature into executable scripts for cosmological simulations [433]. Its specialized agents for physics reasoning and software validation demonstrated strong performance on a dataset of over 40 simulations, accurately extracting and configuring simulation parameters from published papers.

##### 8.3. Computational Mechanics and Fluid Dynamics

Computational mechanics and fluid dynamics rely heavily on sophisticated and often user-unfriendly software for the Finite Element Method (FEM) and Computational Fluid Dynamics (CFD). A major challenge is the steep learning curve required to set up, run, and debug complex simulations, which limits accessibility and slows down research and engineering innovation.

To lower this barrier, OpenFOAMGPT was introduced as an LLM-based agent to streamline CFD simulations using the OpenFOAM solver [258]. The agent, augmented with a Retrieval-Augmented Generation (RAG) pipeline to embed domain-specific knowledge, successfully handles complex tasks like zero-shot case setup, boundary condition modification, and code translation across various engineering scenarios. Its successor, OpenFOAMGPT 2.0, expands this into a multi-agent framework for fully automated, end-to-end simulations from natural language queries [78]. Featuring specialized agents for pre-processing, prompt generation, simulation, and post-processing, it achieved 100% success and reproducibility across over 450 test cases, demonstrating the reliability of orchestrated agent systems for scientific computing.

In solid mechanics, LLMs often lack the quantitative reliability needed for engineering applications. To address this, an LLM-empowered agent was created for structural beam analysis that reframes the problem as a code generation task [205]. By using chain-of-thought and few-shot prompting to generate and execute OpeeSeesPy code, the agent achieved over 99.0% accuracy on a benchmark dataset, showing robust performance across diverse conditions. Expanding on this, MechAgents leverages multi-agent collaboration to solve complex elasticity problems [247]. Agent teams with specialized roles (e.g., planner, coder, critic) autonomously write, execute, and self-correct FEM code, demonstrating that synergistic collaboration and mutual correction improve overall performance. Research has also focused on optimizing these collaborations; one study used the AutoGen framework to systematically test configurations of agents with roles like "Engineer," "Executor," and "Expert" for Finite Element Analysis [325]. It found that well-defined roles and interaction patterns significantly increase task success rates, providing a foundation for automating complex simulation methodologies.

- Table 15: Examples of Validated Scientific Discoveries Achieved by AI Agents in Physical Sciences.


Agent System Application Domain Novel Scientific Contribution or Validated Discovery

mephisto [311] Galaxy Observation Interpretation Interprets new multi-band observations from the James Webb Space Telescope

to reason about the physical scenarios of a recently discovered population of "Little Red Dot" galaxies, achieving near-human proficiency and contributing directly to the understanding of these objects.

The AI Cosmologist [241]

Cosmological ML Research Automates the entire research workflow, from idea generation and experimental design to data analysis and the autonomous production of complete scientific publications. The system develops novel approaches by iterating on experimental outcomes, thereby generating new scientific insights directly from datasets.

##### 8.4. Quantum Computing

A central goal in quantum computing is the development of self-driving laboratories capable of highthroughput experimentation for tasks like processor calibration and characterization. A key challenge is integrating unstructured and multimodal laboratory knowledge into autonomous AI systems to enable closed-loop, intelligent control over experiments.

To tackle this, the k-agents framework was introduced to support the automation of quantum experiments [44]. This framework employs LLM-based agents to encapsulate complex laboratory knowledge, including available experimental operations and data analysis methods. Execution agents then break down experimental procedures into agent-based state machines, interacting with other agents to perform each step. The analyzed results from one step are used to drive state transitions, creating a closed-loop feedback system. When applied to a superconducting quantum processor, the agent system autonomously planned and executed experiments for hours, successfully producing and characterizing entangled quantum states with a proficiency matching that of human scientists.

### 9. Challenges in Agentic Science

As AI systems evolve from narrowly scoped tools to autonomous scientific agents, they bring forth a new class of foundational and ethical challenges. These concerns reach beyond the well-documented limitations of large language models-such as hallucination, knowledge-updating inefficiencies, and catastrophic forgetting [165, 137, 435]-and strike at the philosophical core of scientific inquiry: how knowledge is generated, validated, and trusted. Navigating these challenges is critical for the safe and credible integration of agentic AI into the natural sciences (Figure 8).

##### 9.1. Agentic Reproducibility and Reliability

Scientific progress is predicated on reproducibility, yet agentic systems strain this foundational principle. Unlike conventional experiments that can be reproduced by rerunning code, agentic discovery involves replicating a stochastic and context-sensitive discovery trajectory. Such trajectories are shaped by emergent reasoning patterns and contingent decisions, which are difficult to reproduce consistently [219]. This challenge is compounded by several factors:

- • Planning and Execution Failures: The planning capabilities of base LLMs are a fundamental weakness; in autonomous modes, they often fail to generate executable plans, producing irrational or illogical


- steps that deviate from the intended task [138]. Furthermore, their ability to translate conceptual plans into correct, executable code is severely limited, with state-of-the-art benchmarks showing execution accuracy as low as 39% [364].
- • System Instability: The continual adaptation of these agents to evolving environments [231, 161] is threatened by catastrophic forgetting-the tendency to lose previously acquired knowledge when trained on new data [165]. This instability undermines an agent’s ability to maintain a coherent knowledge base over time, making it difficult to reproduce earlier findings after model updates.
- • Prompt Sensitivity: In multi-stage experiments, agents exhibit a critical sensitivity to prompt wording. Minor variations, even when conveying the same intent, can lead to inconsistent guidance and divergent outcomes, making the discovery trajectory highly fragile and difficult to replicate reliably.


Achieving meaningful reproducibility will require formalizing new standards for logging agent states, decision policies, reasoning justifications, and environmental contingencies. Absent such mechanisms, we risk a future where scientific claims become irreproducible anomalies rather than verifiable contributions.

##### 9.2. Validation of Novelty

A central promise of autonomous scientific agents is their capacity to generate genuinely novel hypothesesinsights that transcend the agent’s training distribution [398]. Yet this very capability introduces a fundamental validation dilemma: how can we differentiate between an authentic conceptual leap and an artifact of sophisticated interpolation or hallucination [89, 398]? LLMs are fundamentally constrained by their training data, which leads them to generate ideas that often lack true originality and are repetitive across different runs [219]. The tendency to produce plausible-sounding but false or unverifiable content, known

- as hallucination, can manifest as fabricated findings, data, or references, undermining the credibility of the output [137, 435].


Verifying that a proposed hypothesis is not a derivative synthesis of existing patterns requires tools capable of auditing the agent’s reasoning lineage. This problem is compounded by model opacity, as validation of novelty hinges on interpretability: the ability to trace and understand the inferential steps that led to a claim [379]. Without such transparency, we are left with compelling-seeming conjectures that may lack genuine originality. Furthermore, the lack of reliable, objective, and scalable evaluation frameworks for AI-generated hypotheses remains a significant bottleneck, as current methods rely on resource-intensive and subjective human expert judgment.

##### 9.3. Transparency in Scientific Reasoning

Scientific reasoning demands not only correct conclusions but also intelligible and auditable justifications. However, the architecture of many high-performing AI models inherently resists interpretation, undermining their trustworthiness as scientific collaborators [5]. Delegating scientific discovery to black-box oracles is unsound, as this opacity undermines scientific validation, trust, and the assimilation of AI-driven insights [379]. Accordingly, there is an urgent need to move beyond post-hoc explainability toward the development of agents that are interpretable by design—systems whose reasoning mechanisms are transparent, verifiable, and aligned with established scientific paradigms [28]. Structured internal logs and clear documentation are vital for auditing the AI’s reasoning and ensuring its conclusions are based on sound logic [23, 22]. Interpretability is not a peripheral concern; it is essential for integrating machine-generated knowledge into the broader scientific corpus and ensuring that such knowledge can be critically evaluated and built upon by human researchers [22].

##### 9.4. Ethical and Societal Dimensions

The deployment of autonomous discovery agents introduces novel ethical and societal risks distinct from those associated with passive LLMs [402]. Without the capacity for ethical judgment or self-regulation based on potential risks, these agents pose multifaceted challenges [27]. These include:

- • Accountability and Risk: If an autonomous agent generates erroneous findings or uncovers hazardous compounds, who bears responsibility [23]? The possibility of dual-use outcomes-such as the autonomous discovery of toxins, pathogens, or other harmful technologies [133]-raises acute concerns about misuse, particularly in the presence of adversarial attacks like backdoors or dataset poisoning [119, 451, 387]. Effective governance must include mechanisms for attribution, traceability, and rapid response.
- • Impact on Scientific Labor and Education: Agentic AI systems may significantly alter the structure of scientific labor and education. While they hold the promise of democratizing access to discovery, they also risk displacing human scientists from critical roles and reshaping the ecosystem of expertise and creativity [315]. Over-reliance on AI for core research tasks could erode critical thinking and hands-on skills, diminishing scientific literacy from early training to expert practice [381]. This calls for rethinking human-agent collaboration models and preserving the creative agency of human researchers in the scientific process.
- • Governance and Integrity: Ensuring ethical behavior from autonomous agents necessitates embedding normative constraints and values directly into their architectures [190]. The large-scale generation of AI-driven research threatens to overwhelm peer-review systems and lower publication standards [219]. Furthermore, biases in AI can skew research priorities toward topics with abundant data, exacerbating funding inequalities [381]. This involves setting principled boundaries on agent autonomy, maintaining continuous audit trails, and instituting robust oversight frameworks that include ethical red-teaming, pre-deployment verification, and post-deployment monitoring [264, 39].


These foundational and ethical dimensions must be addressed not as afterthoughts but as integral design considerations in the development of agentic scientific systems.

### 10. Future Outlook of Agentic Science

Despite significant conceptual, technical, and ethical hurdles, the trajectory of agentic AI suggests the emergence of a transformative paradigm in scientific discovery. Beyond incremental automation, these systems may catalyze a shift toward computational epistemology—a mode of inquiry where artificial agents participate in the invention, justification, and dissemination of scientific knowledge. This section outlines the key directions required to bridge current gaps, envisions the distinct evolutionary pathways for AI scientists, and presents four prospective frontiers that could define the next era of agentic science.

##### 10.1. From Automation to Autonomous Invention

While current AI agents are predominantly constrained to automating existing workflows, a profound leap will occur when agents begin to engage in autonomous invention. Such systems would possess the capacity to interrogate the conceptual limitations of current methodologies and propose novel scientific instruments or conceptual frameworks. For instance, an agent might invent a new imaging modality to reveal a previously inaccessible subcellular process or formulate a novel mathematical abstraction to model emergent behaviors

![image 103](Wei et al._2025_From AI for Science to Agentic Science A Survey on Autonomous Scientific Discovery_images/imageFile103.png)

- Figure 8: Exploring the Path to Agentic Scientists: Addressing Current Challenges, Enabling Autonomous Invention, and Pioneering the Nobel Turing Test Across Life Sciences, Chemistry, Materials, and Physics.


in complex systems. This marks a transition from tool-user to tool-creator, constituting a qualitatively distinct form of machine-driven scientific creativity.

##### 10.2. Interdisciplinary Synthesis at Scale

Many of the most consequential scientific breakthroughs emerge at disciplinary intersections, yet human researchers are often limited by cognitive load and siloed expertise. Future agentic systems, trained on multimodal corpora spanning diverse scientific domains, could act as scalable engines for interdisciplinary synthesis. These agents could surface latent analogies between disparate fields–for example, mapping techniques from topological quantum field theory to deep learning architectures, or leveraging ecological dynamics to model economic systems. Such cross-domain reasoning transcends information retrieval, potentially enabling the discovery of unifying principles that reconfigure entire fields.

##### 10.3. The Global Cooperation Research Agent

Looking further ahead, we envision a global cooperation ecosystem of scientific agents, distributed across institutions and research infrastructures. In this paradigm, specialized agents–e.g., a proteomics agent

- at one lab, a pharmacodynamics agent at another–interact within a decentralized, trust-aware network. These agents would not only share data but also engage in critical peer-review, hypothesis refinement, and collaborative experimentation [70]. Such a system could operate as a planetary-scale scientific engine, capable of tackling grand challenge problems whose complexity defies centralized human coordination. Realizing this vision will require advances in federated agent protocols, secure multi-agent reasoning (e.g., to mitigate recursive attack propagation [449]), and mechanisms for conceptual accountability such as proof-of-thought cryptographic trails [49].


##### 10.4. The Nobel-Turing Test

A provocative benchmark for agentic science is what we term the Nobel-Turing Test: can an autonomous agent, or a hybrid human-agent team, generate a discovery worthy of the Nobel Prize? Such a feat would demand more than competent execution of predefined tasks; it would require the agent to autonomously identify an unresolved and foundational scientific gap, generate a non-obvious and empirically testable hypothesis, and design a novel experimental methodology–potentially leveraging robotic systems and multiagent collaboration [400, 298]. Crucially, it must also contextualize and interpret findings in a way that instigates a paradigmatic shift. Achieving this would mark the maturation of a fully autonomous scientific cycle, where agents are not merely instruments of execution, but originators of scientific insight [45].

### 11. Conclusion

Agentic Science marks a transformative stage in the evolution of AI for Science, where AI systems transition from computational assistants to autonomous research partners capable of reasoning, experimentation, and iterative discovery. Through our unified framework connecting foundational capabilities, core processes, and domain realizations, we provide a domain-oriented synthesis of autonomous scientific discovery across life sciences, chemistry, materials science, and physics. By situating agentic AI within this structured paradigm, we highlight both its broad applicability and the technical, ethical, and philosophical challenges that must be addressed to ensure trustworthy and impactful progress. We envision Agentic Science not as a replacement for human inquiry, but as a co-evolving paradigm that augments scientific creativity, accelerates discovery, and reshapes the future of research.

### References

- [1] Mahyar Abbasian, Iman Azimi, Amir M Rahmani, and Ramesh Jain. Conversational health agents: A personalized llm-powered agent framework. arXiv preprint arXiv:2310.02374, 2023.
- [2] Hadi Abdine, Michail Chatzianastasis, Costas Bouyioukos, and Michalis Vazirgiannis. Prot2text: Multimodal protein’s function generation with gnns and transformers. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 38, pages 10757–10765, 2024. doi: 10.1609/aaai.v38i10. 28948.
- [3] Josh Abramson, Jonas Adler, Jack Dunger, Richard Evans, Tim Green, Alexander Pritzel, Olaf Ronneberger, Lindsay Willmore, Andrew J Ballard, Joshua Bambrick, et al. Accurate structure prediction of biomolecular interactions with alphafold 3. Nature, 630(8016):493–500, 2024.
- [4] Shubham Agarwal, Gaurav Sahu, Abhay Puri, Issam H Laradji, Krishnamurthy DJ Dvijotham, Jason Stanley, Laurent Charlin, and Christopher Pal. Litllm: A toolkit for scientific literature review. arXiv preprint arXiv:2402.01788, 2024.
- [5] Pegah Ahadian and Qiang Guan. Ai trustworthy challenges in drug discovery. In Hao Chen, Yuyin Zhou, Daguang Xu, and Varut Vince Vardhanabhuti, editors, Trustworthy Artificial Intelligence for Healthcare, pages 1–12, Cham, 2024. Springer Nature Switzerland. ISBN 978-3-031-67751-9.
- [6] Samuel Alber, Bowen Chen, Eric Sun, Alina Isakova, Aaron James Wilk, and James Zou. Cellvoyager: Ai compbio agent generates new insights by autonomously analyzing biological data. bioRxiv, pages 2025–06, 2025.
- [7] Mehrad Ansari and Seyed Mohamad Moosavi. Agent-based learning of materials datasets from the scientific literature. Digital Discovery, 3(12):2607–2617, 2024.
- [8] Mehrad Ansari, Jeffrey Watchorn, Carla E Brown, and Joseph S Brown. dziner: Rational inverse design of materials with ai agents. arXiv preprint arXiv:2410.03963, 2024.
- [9] Luis M. Antunes, Keith T. Butler, and Ricardo Grau-Crespo. Crystal structure generation with autoregressive large language modeling. Nature Communications, 15(1):10570, Dec 2024. ISSN 2041-1723. doi: 10.1038/s41467-024-54639-7. URL https://doi.org/10.1038/s41467-024-54639-7.
- [10] Jicong Ao, Fan Wu, Yansong Wu, Abdalla Swikir, and Sami Haddadin. Llm as bt-planner: Leveraging llms for behavior tree generation in robot task planning. arXiv preprint arXiv:2409.10444, 2024.
- [11] Reza Averly, Frazier N Baker, and Xia Ning. Liddia: Language-based intelligent drug discovery agent. arXiv preprint arXiv:2502.13959, 2025.
- [12] Žiga Avsec, Natasha Latysheva, Jun Cheng, Guido Novati, Kyle R Taylor, Tom Ward, Clare Bycroft, Lauren Nicolaisen, Eirini Arvaniti, Joshua Pan, et al. Alphagenome: advancing regulatory variant effect prediction with a unified dna sequence model. bioRxiv, pages 2025–06, 2025.
- [13] Jinheon Baek, Sujay Kumar Jauhar, Silviu Cucerzan, and Sung Ju Hwang. Researchagent: Iterative research idea generation over scientific literature with large language models. arXiv preprint arXiv:2404.07738, 2024.


- [14] Jinheon Baek, Sujay Kumar Jauhar, Silviu Cucerzan, and Sung Ju Hwang. Researchagent: Iterative research idea generation over scientific literature with large language models, 2025. URL https: //arxiv.org/abs/2404.07738.
- [15] Viraj Bagal, Rishal Aggarwal, PK Vinod, and U Deva Priyakumar. Molgpt: molecular generation using a transformer-decoder model. Journal of chemical information and modeling, 62(9):2064–2076, 2021.
- [16] Viraj Bagal, Rishal Aggarwal, P. K. Vinod, and U. Deva Priyakumar. MolGPT: Molecular Generation Using a Transformer-Decoder Model. Journal of Chemical Information and Modeling, 62(9):2064–2076, May 2022. ISSN 1549-9596. doi: 10.1021/acs.jcim.1c00600. URL https://doi.org/10.1021/ acs.jcim.1c00600.
- [17] Jinze Bai, Shuai Bai, Yunfei Chu, Zeyu Cui, Kai Dang, Xiaodong Deng, Yang Fan, Wenbin Ge, Yu Han, Fei Huang, et al. Qwen technical report. arXiv preprint arXiv:2309.16609, 2023.
- [18] Lei Bai, Zhongrui Cai, Maosong Cao, Weihan Cao, Chiyu Chen, Haojiong Chen, Kai Chen, Pengcheng Chen, Ying Chen, Yongkang Chen, Yu Cheng, Yu Cheng, Pei Chu, Tao Chu, Erfei Cui, Ganqu Cui, Long Cui, Ziyun Cui, Nianchen Deng, Ning Ding, Nanqin Dong, Peijie Dong, Shihan Dou, Sinan Du, Haodong Duan, Caihua Fan, Ben Gao, Changjiang Gao, Jianfei Gao, Songyang Gao, Yang Gao, Zhangwei Gao, Jiaye Ge, Qiming Ge, Lixin Gu, Yuzhe Gu, Aijia Guo, Qipeng Guo, Xu Guo, Conghui He, Junjun He, Yili Hong, Siyuan Hou, Caiyu Hu, Hanglei Hu, Jucheng Hu, Ming Hu, Zhouqi Hua, Haian Huang, Junhao Huang, Xu Huang, Zixian Huang, Zhe Jiang, Lingkai Kong, Linyang Li, Peiji Li, Pengze Li, Shuaibin Li, Tianbin Li, Wei Li, Yuqiang Li, Dahua Lin, Junyao Lin, Tianyi Lin, Zhishan Lin, Hongwei Liu, Jiangning Liu, Jiyao Liu, Junnan Liu, Kai Liu, Kaiwen Liu, Kuikun Liu, Shichun Liu, Shudong Liu, Wei Liu, Xinyao Liu, Yuhong Liu, Zhan Liu, Yinquan Lu, Haijun Lv, Hongxia Lv, Huijie Lv, Qidang Lv, Ying Lv, Chengqi Lyu, Chenglong Ma, Jianpeng Ma, Ren Ma, Runmin Ma, Runyuan Ma, Xinzhu Ma, Yichuan Ma, Zihan Ma, Sixuan Mi, Junzhi Ning, Wenchang Ning, Xinle Pang, Jiahui Peng, Runyu Peng, Yu Qiao, Jiantao Qiu, Xiaoye Qu, Yuan Qu, Yuchen Ren, Fukai Shang, Wenqi Shao, Junhao Shen, Shuaike Shen, Chunfeng Song, Demin Song, Diping Song, Chenlin Su, Weijie Su, Weigao Sun, Yu Sun, Qian Tan, Cheng Tang, Huanze Tang, Kexian Tang, Shixiang Tang, Jian Tong, Aoran Wang, Bin Wang, Dong Wang, Lintao Wang, Rui Wang, Weiyun Wang, Wenhai Wang, Yi Wang, Ziyi Wang, Ling-I Wu, Wen Wu, Yue Wu, Zijian Wu, Linchen Xiao, Shuhao Xing, Chao Xu, Huihui Xu, Jun Xu, Ruiliang Xu, Wanghan Xu, GanLin Yang, Yuming Yang, Haochen Ye, Jin Ye, Shenglong Ye, Jia Yu, Jiashuo Yu, Jing Yu, Fei Yuan, Bo Zhang, Chao Zhang, Chen Zhang, Hongjie Zhang, Jin Zhang, Qiaosheng Zhang, Qiuyinzhe Zhang, Songyang Zhang, Taolin Zhang, Wenlong Zhang, Wenwei Zhang, Yechen Zhang, Ziyang Zhang, Haiteng Zhao, Qian Zhao, Xiangyu Zhao, Xiangyu Zhao, Bowen Zhou, Dongzhan Zhou, Peiheng Zhou, Yuhao Zhou, Yunhua Zhou, Dongsheng Zhu, Lin Zhu, and Yicheng Zou. Intern-s1: A scientific multimodal foundation model. arXiv preprint arXiv:2508.15763, 2025.
- [19] Xuefeng Bai, Song He, Yi Li, Yabo Xie, Xin Zhang, Wenli Du, and Jian-Rong Li. Construction of a knowledge graph for framework material enabled by large language models and its application. npj Computational Materials, 11(1):51, Feb 2025. ISSN 2057-3960. doi: 10.1038/s41524-025-01540-6. URL https://doi.org/10.1038/s41524-025-01540-6.
- [20] SD Bakshi, P Barry, C Bissolotti, I Cloet, S Corrodi, Z Djurcic, S Habib, K Heitmann, TJ Hobbs, W Hopkins, et al. Argoloom: agentic ai for fundamental physics from quarks to cosmos. arXiv preprint arXiv:2510.02426, 2025.


- [21] Suryanarayanan Balaji, Rishikesh Magar, Yayati Jadhav, and Amir Barati Farimani. Gpt-molberta: Gpt molecular features language model for molecular property prediction, 2023. URL https: //arxiv.org/abs/2310.03030.
- [22] Soumya Banerjee et al. On the ethical considerations of generative agents. arXiv preprint arXiv:2411.19211, 2024.
- [23] Muneera Bano, Didar Zowghi, Pip Shea, and Georgina Ibarra. Investigating responsible ai for scientific research: an empirical study. arXiv preprint arXiv:2312.09561, 2023.
- [24] Ilyes Batatia, Philipp Benner, Yuan Chiang, Alin M Elena, Dávid P Kovács, Janosh Riebesell, Xavier R Advincula, Mark Asta, Matthew Avaylon, William J Baldwin, et al. A foundation model for atomistic materials chemistry. arXiv preprint arXiv:2401.00096, 2023.
- [25] Adib Bazgir, Yuwen Zhang, et al. Multicrossmodal automated agent for integrating diverse materials science data. arXiv preprint arXiv:2505.15132, 2025.
- [26] Jonas Belouadi, Anne Lauscher, and Steffen Eger. Automatikz: Text-guided synthesis of scientific vector graphics with tikz, 2024. URL https://arxiv.org/abs/2310.00367.
- [27] Yoshua Bengio, Michael Cohen, Damiano Fornasiere, Joumana Ghosn, Pietro Greiner, Matt MacDermott, Sören Mindermann, Adam Oberman, Jesse Richardson, Oliver Richardson, et al. Superintelligent agents pose catastrophic risks: Can scientist ai offer a safer path? arXiv preprint arXiv:2502.15657, 2025.
- [28] Yoshua Bengio, Michael Cohen, Damiano Fornasiere, Joumana Ghosn, Pietro Greiner, Matt MacDermott, Sören Mindermann, Adam Oberman, Jesse Richardson, Oliver Richardson, Marc-Antoine Rondeau, Pierre-Luc St-Charles, and David Williams-King. Superintelligent agents pose catastrophic risks: Can scientist ai offer a safer path?, 2025. URL https://arxiv.org/abs/2502.15657.
- [29] Vineet Bhat, Ali Umut Kaypak, Prashanth Krishnamurthy, Ramesh Karri, and Farshad Khorrami. Grounding llms for robot task planning using closed-loop state feedback. arXiv preprint arXiv:2402.08546, 2024.
- [30] Daniil A Boiko, Robert MacKnight, Ben Kline, and Gabe Gomes. Autonomous chemical research with large language models. Nature, 624(7992):570–578, 2023.
- [31] Elliot Bolton, Abhinav Venigalla, Michihiro Yasunaga, David Hall, Betty Xiong, Tony Lee, Roxana Daneshjou, Jonathan Frankle, Percy Liang, Michael Carbin, and Christopher D. Manning. Biomedlm: A 2.7b parameter language model trained on biomedical text, 2024. URL https://arxiv.org/ abs/2403.18421.
- [32] Jannis Born and Matteo Manica. Regression transformer enables concurrent sequence regression and generation for molecular language modelling. Nature Machine Intelligence, 5(4):432–444, April

2023. ISSN 2522-5839. doi: 10.1038/s42256-023-00639-z. URL http://dx.doi.org/10.1038/ s42256-023-00639-z.

- [33] Albert Bou, Morgan Thomas, Sebastian Dittert, Carles Navarro, Maciej Majewski, Ye Wang, Shivam Patel, Gary Tresadern, Mazen Ahmad, Vincent Moens, et al. Acegen: Reinforcement learning of generative chemical agents for drug discovery. Journal of Chemical Information and Modeling, 64(15): 5900–5911, 2024.


- [34] Andres Bran, Sam Cox, Oliver Schilter, Carlo Baldassari, Andrew D. White, and Philippe Schwaller. Augmenting large language models with chemistry tools. Nature Machine Intelligence, 6(5):525–535, May 2024. ISSN 2522-5839. doi: 10.1038/s42256-024-00832-8. URL https://doi.org/10. 1038/s42256-024-00832-8.
- [35] Andres M Bran, Sam Cox, Oliver Schilter, Carlo Baldassari, Andrew D White, and Philippe Schwaller. Chemcrow: Augmenting large-language models with chemistry tools. arXiv preprint arXiv:2304.05376, 2023.
- [36] Garyk Brixi, Matthew G Durrant, Jerome Ku, Michael Poli, Greg Brockman, Daniel Chang, Gabriel A Gonzalez, Samuel H King, David B Li, Aditi T Merchant, et al. Genome modeling and design across all domains of life with evo 2. BioRxiv, pages 2025–02, 2025.
- [37] Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, et al. Language models are few-shot learners. In Advances in Neural Information Processing Systems, 2020.
- [38] Cameron B Browne, Edward Powley, Daniel Whitehouse, Simon M Lucas, Peter I Cowling, Philipp Rohlfshagen, Stephen Tavener, Diego Perez, Spyridon Samothrakis, and Simon Colton. A survey of monte carlo tree search methods. IEEE Transactions on Computational Intelligence and AI in games, 4

(1):1–43, 2012.

- [39] Miles Brundage, Shahar Avin, Jasmine Wang, Haydn Belfield, Gretchen Krueger, Gillian Hadfield, Heidy Khlaaf, Jingying Yang, Helen Toner, Ruth Fong, et al. Toward Trustworthy AI Development: Mechanisms for Supporting Verifiable Claims. arXiv preprint arXiv:2004.07213, 2020.
- [40] Markus J Buehler. MechGPT, a language-based strategy for mechanics and materials modeling that connects knowledge across scales, disciplines, and modalities. Applied Mechanics Reviews, 76(2): 021001, 2024.
- [41] Tiffany J Callahan, Nathaniel H Park, and Sara Capponi. Agentic mixture-of-workflows for multi-modal chemical search. arXiv preprint arXiv:2502.19629, 2025.
- [42] Askery Canabarro, Felipe Fernandes Fanchini, André Luiz Malvezzi, Rodrigo Pereira, and Rafael Chaves. Unveiling phase transitions with machine learning. Physical Review B, 100(4):045129, 2019.
- [43] He Cao, Zijing Liu, Xingyu Lu, Yuan Yao, and Yu Li. Instructmol: Multi-modal integration for building a versatile and reliable molecular assistant in drug discovery. arXiv preprint arXiv:2311.16208, 2023.
- [44] Shuxiang Cao, Zijian Zhang, Mohammed Alghadeer, Simone D Fasciati, Michele Piscitelli, Mustafa Bakr, Peter Leek, and Alán Aspuru-Guzik. Agents for self-driving laboratories applied to quantum computing. arXiv preprint arXiv:2412.07978, 2024.
- [45] Thomas Carta, Clément Romac, Thomas Wolf, Sylvain Lamprier, Olivier Sigaud, and Pierre-Yves Oudeyer. Grounding large language models in interactive environments with online reinforcement learning. In Andreas Krause, Emma Brunskill, Kyunghyun Cho, Barbara Engelhardt, Sivan Sabato, and Jonathan Scarlett, editors, Proceedings of the 40th International Conference on Machine Learning, volume 202 of Proceedings of Machine Learning Research, pages 3676–3713. PMLR, 23–29 Jul 2023. URL https://proceedings.mlr.press/v202/carta23a.html.
- [46] Jingyi Chai, Shuo Tang, Rui Ye, Yuwen Du, Xinyu Zhu, Mengcheng Zhou, Yanfeng Wang, Siheng Chen, et al. Scimaster: Towards general-purpose scientific ai agents, part i. x-master as foundation: Can we lead on humanity’s last exam? arXiv preprint arXiv:2507.05241, 2025.


- [47] Jun Shern Chan, Neil Chowdhury, Oliver Jaffe, James Aung, Dane Sherburn, Evan Mays, Giulio Starace, Kevin Liu, Leon Maksin, Tejal Patwardhan, Lilian Weng, and Aleksander Mądry. Mlebench: Evaluating machine learning agents on machine learning engineering, 2025. URL https: //arxiv.org/abs/2410.07095.
- [48] Xinhao Che, Yujing Zhao, Qilei Liu, Fang Yu, Hanyu Gao, and Lei Zhang. Csstep: Step-by-step exploration of the chemical space of drug molecules via multi-agent and multi-stage reinforcement learning. Chemical Engineering Science, page 122048, 2025.
- [49] Bei Chen, Gaolei Li, Xi Lin, Zheng Wang, and Jianhua Li. Blockagents: Towards byzantine-robust llm-based multi-agent coordination via blockchain. In ACM Turing Award Celebration Conference, pages 187–192, 2024.
- [50] Junying Chen, Zhenyang Cai, Ke Ji, Xidong Wang, Wanlong Liu, Rongsheng Wang, Jianye Hou, and Benyou Wang. Huatuogpt-o1, towards medical complex reasoning with llms. arXiv preprint arXiv:2412.18925, 2024.
- [51] Junying Chen, Chi Gui, Ruyi Ouyang, Anningzhe Gao, Shunian Chen, Guiming Hardy Chen, Xidong Wang, Ruifei Zhang, Zhenyang Cai, Ke Ji, Guangjun Yu, Xiang Wan, and Benyou Wang. Huatuogptvision, towards injecting medical visual knowledge into multimodal llms at scale, 2024. URL https: //arxiv.org/abs/2406.19280.
- [52] Junying Chen, Xidong Wang, Ke Ji, Anningzhe Gao, Feng Jiang, Shunian Chen, Hongbo Zhang, Dingjie Song, Wenya Xie, Chuyi Kong, Jianquan Li, Xiang Wan, Haizhou Li, and Benyou Wang. Huatuogpt-ii, one-stage training for medical adaption of llms. Proceedings of COLM (arXiv:2311.09774v2), 2024. URL https://arxiv.org/abs/2311.09774.
- [53] Justin Chih-Yao Chen, Swarnadeep Saha, and Mohit Bansal. Reconcile: Round-table conference improves reasoning via consensus among diverse llms. arXiv preprint arXiv:2309.13007, 2023.
- [54] Kexin Chen, Junyou Li, Kunyi Wang, Yuyang Du, Jiahui Yu, Jiamin Lu, Lanqing Li, Jiezhong Qiu, Jianzhang Pan, Yi Huang, et al. Chemist-x: Large language model-empowered agent for reaction condition recommendation in chemical synthesis. arXiv preprint arXiv:2311.10776, 2023.
- [55] Kexin Chen, Hanqun Cao, Junyou Li, Yuyang Du, Menghao Guo, Xin Zeng, Lanqing Li, Jiezhong Qiu, Pheng Ann Heng, and Guangyong Chen. An autonomous large language model agent for chemical literature data mining. arXiv preprint arXiv:2402.12993, 2024.
- [56] Qiguang Chen, Mingda Yang, Libo Qin, Jinhao Liu, Zheng Yan, Jiannan Guan, Dengyun Peng, Yiyan Ji, Hanjing Li, Mengkang Hu, et al. Ai4research: A survey of artificial intelligence for scientific research. arXiv preprint arXiv:2507.01903, 2025.
- [57] Anoop Cherian, Radu Corcodel, Siddarth Jain, and Diego Romeres. LLMPhy: Complex physical reasoning using large language models and world models. arXiv preprint arXiv:2411.08027, 2024.
- [58] Yuan Chiang, Elvis Hsieh, Chia-Hong Chou, and Janosh Riebesell. Llamp: Large language model made powerful for high-fidelity materials knowledge retrieval and distillation. arXiv preprint arXiv:2401.17244, 2024.
- [59] Jae-Woo Choi, Hyungmin Kim, Hyobin Ong, Youngwoo Yoon, Minsu Jang, Jaehong Kim, et al. Reactree: Hierarchical task planning with dynamic tree expansion using llm agent nodes. 2025.


- [60] Gheorghe Comanici, Eric Bieber, Mike Schaekermann, Ice Pasupat, Noveen Sachdeva, Inderjit Dhillon, Marcel Blistein, Ori Ram, Dan Zhang, Evan Rosen, et al. Gemini 2.5: Pushing the frontier with advanced reasoning, multimodality, long context, and next generation agentic capabilities. arXiv preprint arXiv:2507.06261, 2025.
- [61] Haotian Cui, Chloe Wang, Hassaan Maan, Kuan Pang, Fengning Luo, Nan Duan, and Bo Wang. scgpt: toward building a foundation model for single-cell multi-omics using generative ai. Nature methods, 21(8):1470–1480, 2024.
- [62] Allan Dafoe et al. Open problems in cooperative ai, 2020.
- [63] F. Dai et al. Toward de novo protein design from natural language. bioRxiv, 2025. doi: 10.1101/2024.08.01.606258. URL https://www.biorxiv.org/content/10.1101/2024. 08.01.606258v4.
- [64] Tianwei Dai, Sriram Vijayakrishnan, Filip T Szczypi ’nski, Jean-Fran ccois Ayme, Ehsan Simaei, Thomas Fellowes, Rob Clowes, Lyubomir Kotopanov, Caitlin E Shields, Zhengxue Zhou, et al. Autonomous mobile robots for exploratory synthetic chemistry. Nature, 635

(8040):890–897, 2024.

- [65] Hugo Dalla-Torre, Liam Gonzalez, Javier Mendoza-Revilla, Nicolas Lopez Carranza, Adam Henryk Grzywaczewski, Francesco Oteri, Christian Dallago, Evan Trop, Bernardo P de Almeida, Hassan Sirelkhatim, et al. Nucleotide transformer: building and evaluating robust foundation models for human genomics. Nature Methods, 22(2):287–297, 2025.
- [66] Mike D’Arcy et al. Marg: Multi-agent review generation for scientific papers, 2024.
- [67] Kourosh Darvish, Marta Skreta, Yuchi Zhao, Naruki Yoshikawa, Sagnik Som, Miroslav Bogdanovic, Yang Cao, Han Hao, Haoping Xu, Alán Aspuru-Guzik, et al. Organa: A robotic assistant for automated chemistry experimentation and characterization. arXiv preprint arXiv:2401.06949, 2024.
- [68] Ayushman Das et al. Enabling synergistic knowledge sharing and reasoning in large language models with collaborative multi-agents. In IEEE International Conference on Collaboration and Internet Computing, 2023.
- [69] Bernardo P de Almeida, Guillaume Richard, Hugo Dalla-Torre, Christopher Blum, Lorenz Hexemer, Priyanka Pandey, Stefan Laurent, Chandana Rajesh, Marie Lopez, Alexandre Laterre, et al. A multimodal conversational agent for dna, rna and protein tasks. Nature Machine Intelligence, pages 1–14, 2025.
- [70] José Antonio Siqueira de Cerqueira, Mamia Agbese, Rebekah Rousi, Nannan Xi, Juho Hamari, and Pekka Abrahamsson. Can we trust ai agents? an experimental study towards trustworthy llm-based multi-agent systems for ai ethics. arXiv preprint arXiv:2411.08881, 2024.
- [71] Ning Ding, Shang Qu, Linhai Xie, Yifei Li, Zaoqu Liu, Kaiyan Zhang, Yibai Xiong, Yuxin Zuo, Zhangren Chen, Ermo Hua, et al. Automating exploratory proteomics research via language models. arXiv preprint arXiv:2411.03743, 2024.
- [72] Zhehao Dong, Zhen Lu, and Yue Yang. Fine-tuning a large language model for automating computational fluid dynamics simulations. Theoretical and Applied Mechanics Letters, page 100594, 2025.


- [73] Yilun Du, Shuang Li, Antonio Torralba, Joshua B Tenenbaum, and Igor Mordatch. Improving factuality and reasoning in language models through multiagent debate. 2023.
- [74] Edmund H Durfee. Distributed problem solving and planning. In ECCAI Advanced Course on Artificial Intelligence, pages 118–149. Springer, 2001.
- [75] Darren Edge, Ha Trinh, Newman Cheng, Joshua Bradley, Alex Chao, Apurva Mody, Steven Truitt, Dasha Metropolitansky, Robert Osazuwa Ness, and Jonathan Larson. From local to global: A graph rag approach to query-focused summarization. arXiv preprint arXiv:2404.16130, 2024.
- [76] Carl Edwards, Tuan Lai, Kevin Ros, Garrett Honke, Kyunghyun Cho, and Heng Ji. Translation between molecules and natural language. In 2022 Conference on Empirical Methods in Natural Language Processing, EMNLP 2022, pages 375–413. Association for Computational Linguistics (ACL), 2022.
- [77] Yao Fehlis, Charles Crain, Aidan Jensen, Michael Watson, James Juhasz, Paul Mandel, Betty Liu, Shawn Mahon, Daren Wilson, Nick Lynch-Jonely, et al. Accelerating drug discovery through agentic ai: A multi-agent approach to laboratory automation in the dmta cycle. arXiv preprint arXiv:2507.09023, 2025.
- [78] Jingsen Feng, Ran Xu, and Xu Chu. Openfoamgpt 2.0: end-to-end, trustworthy automation for computational fluid dynamics. arXiv preprint arXiv:2504.19338, 2025.
- [79] Mohamed Amine Ferrag, Norbert Tihanyi, and Merouane Debbah. From llm reasoning to autonomous ai agents: A comprehensive review. arXiv preprint arXiv:2504.19678, 2025.
- [80] Daniel Flam-Shepherd and Alán Aspuru-Guzik. Language models can generate molecules, materials, and protein binding sites directly in three dimensions as xyz, cif, and pdb files, 2023. URL https: //arxiv.org/abs/2305.05708.
- [81] Shubham Gandhi, Dhruv Shah, Manasi Patwardhan, Lovekesh Vig, and Gautam Shroff. Researchcodeagent: An llm multi-agent system for automated codification of research methodologies. In International Workshop on AI for Transportation, pages 3–37. Springer, 2025.
- [82] Bowen Gao, Yanwen Huang, Yiqiao Liu, Wenxuan Xie, Wei-Ying Ma, Ya-Qin Zhang, and Yanyan Lan. Pharmagents: Building a virtual pharma with large language model agents. arXiv preprint arXiv:2503.22164, 2025.
- [83] Changnan Gao, Wenjie Bao, Shuang Wang, Jianyang Zheng, Lulu Wang, Yongqi Ren, Linfang Jiao, Jianmin Wang, and Xun Wang. Dockingga: enhancing targeted molecule generation using transformer neural network and genetic algorithm with docking simulation. Briefings in Functional Genomics, 23

(5):595–606, 04 2024. ISSN 2041-2657. doi: 10.1093/bfgp/elae011. URL https://doi.org/10. 1093/bfgp/elae011.

- [84] Huan-ang Gao, Jiayi Geng, Wenyue Hua, Mengkang Hu, Xinzhe Juan, Hongzhang Liu, Shilong Liu, Jiahao Qiu, Xuan Qi, Yiran Wu, et al. A survey of self-evolving agents: On path to artificial super intelligence. arXiv preprint arXiv:2507.21046, 2025.
- [85] Jialin Gao, Jianyu Chen, Jiaqi Wei, Bin Jiang, and A-Li Luo. Deep multimodal networks for m-type star classification with paired spectrum and photometric image. Publications of the Astronomical Society of the Pacific, 135(1046):044503, 2023.


- [86] Muhan Gao, Jash Shah, Weiqi Wang, and Daniel Khashabi. Science hierarchography: Hierarchical organization of science literature, 2025. URL https://arxiv.org/abs/2504.13834.
- [87] Shanghua Gao, Ada Fang, Yepeng Huang, Valentina Giunchiglia, Ayush Noori, Jonathan Richard Schwarz, Yasha Ektefaie, Jovana Kondic, and Marinka Zitnik. Empowering biomedical discovery with ai agents. Cell, 187(22):6125–6151, 2024.
- [88] Shanghua Gao, Richard Zhu, Zhenglun Kong, Ayush Noori, Xiaorui Su, Curtis Ginder, Theodoros Tsiligkaridis, and Marinka Zitnik. Txagent: An ai agent for therapeutic reasoning across a universe of tools. arXiv preprint arXiv:2503.10970, 2025.
- [89] Yubin Ge, Neeraja Kirtane, Hao Peng, and Dilek Hakkani-Tür. Llms are vulnerable to malicious prompts disguised as scientific language. arXiv preprint arXiv:2501.14073, 2025.
- [90] Alireza Ghafarollahi and Markus J Buehler. Atomagents: Alloy design and discovery through physicsaware multi-modal multi-agent artificial intelligence. arXiv preprint arXiv:2407.10022, 2024.
- [91] Alireza Ghafarollahi and Markus J Buehler. Protagents: protein discovery via large language model multi-agent collaborations combining physics and machine learning. Digital Discovery, 2024.
- [92] Alireza Ghafarollahi and Markus J Buehler. Rapid and automated alloy design with graph neural network-powered llm-driven multi-agent systems. arXiv preprint arXiv:2410.13768, 2024.
- [93] Alireza Ghafarollahi and Markus J. Buehler. Sciagents: Automating scientific discovery through multi-agent intelligent graph reasoning, 2024. URL https://arxiv.org/abs/2409.05556.
- [94] Alireza Ghafarollahi and Markus J Buehler. Automating alloy design and discovery with physics-aware multimodal multiagent ai. Proceedings of the National Academy of Sciences, 122(4):e2414074122, 2025.
- [95] Alireza Ghafarollahi and Markus J Buehler. Sciagents: automating scientific discovery through bioinspired multi-agent intelligent graph reasoning. Advanced Materials, 37(22):2413523, 2025.
- [96] Alireza Ghafarollahi and Markus J Buehler. Sparks: Multi-agent artificial intelligence model discovers protein design principles. arXiv preprint arXiv:2504.19017, 2025.
- [97] Ali Essam Ghareeb, Benjamin Chang, Ludovico Mitchener, Angela Yiu, Caralyn J Szostkiewicz, Jon M Laurent, Muhammed T Razzak, Andrew D White, Michaela M Hinks, and Samuel G Rodriques. Robin: A multi-agent system for automating scientific discovery. arXiv preprint arXiv:2505.13400, 2025.
- [98] Juraj Gottweis, Wei-Hung Weng, Alexander Daryin, Tao Tu, Anil Palepu, Petar Sirkovic, Artiom Myaskovsky, Felix Weissenberger, Keran Rong, Ryutaro Tanno, et al. Towards an ai co-scientist, 2025. URL https://arxiv.org/abs/2502.18864.
- [99] Juraj Gottweis, Wei-Hung Weng, Alexander Daryin, Tao Tu, Anil Palepu, Petar Sirkovic, Artiom Myaskovsky, Felix Weissenberger, Keran Rong, Ryutaro Tanno, et al. Towards an ai co-scientist. arXiv preprint arXiv:2502.18864, 2025.
- [100] Zhibin Gou, Zhihong Shao, Yeyun Gong, Yelong Shen, Yujiu Yang, Minlie Huang, Nan Duan, and Weizhu Chen. Tora: A tool-integrated reasoning agent for mathematical problem solving. arXiv preprint arXiv:2309.17452, 2023.


- [101] Zhibin Gou, Zhihong Shao, Yeyun Gong, Yelong Shen, Yujiu Yang, Minlie Huang, Nan Duan, and Weizhu Chen. Tora: A tool-integrated reasoning agent for mathematical problem solving. In The Twelfth International Conference on Learning Representations, ICLR 2024, Vienna, Austria, May 7-11,

2024. OpenReview.net, 2024. URL https://openreview.net/forum?id=Ep0TtjVoap.

- [102] Zhibin Gou, Zhihong Shao, Yeyun Gong, Yujiu Yang, Nan Duan, Weizhu Chen, et al. Critic: Large language models can self-correct with tool-interactive critiquing. 2024.
- [103] Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Alex Vaughan, et al. The llama 3 herd of models. arXiv preprint arXiv:2407.21783, 2024.
- [104] Eliska Greplova, Agnes Valenti, Gregor Boschung, Frank Schäfer, Niels Lörch, and Sebastian D Huber. Unsupervised identification of topological phase transitions using predictive models. New Journal of Physics, 22(4):045003, 2020.
- [105] Felix Grezes, Sergi Blanco-Cuaresma, Alberto Accomazzi, Michael J Kurtz, Golnaz Shapurian, Edwin Henneken, Carolyn S Grant, Donna M Thompson, Roman Chyla, Stephen McDonald, et al. Building astrobert, a language model for astronomy & astrophysics. arXiv preprint arXiv:2112.00590, 2021.
- [106] Mourad Gridach, Jay Nanavati, Khaldoun Zine El Abidine, Lenon Mendes, and Christina Mack. Agentic ai for scientific discovery: A survey of progress, challenges, and future directions. arXiv preprint arXiv:2503.08979, 2025.
- [107] Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, et al. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning. arXiv preprint arXiv:2501.12948, 2025.
- [108] Hongyi Guo, Zhihan Liu, Yufeng Zhang, and Zhaoran Wang. Can large language models play games? a case study of a self-play approach. arXiv preprint arXiv:2403.05632, 2024.
- [109] Siyuan Guo, Cheng Deng, Ying Wen, Hechang Chen, Yi Chang, and Jun Wang. Ds-agent: Automated data science by empowering large language models with case-based reasoning. arXiv preprint arXiv:2402.17453, 2024.
- [110] Taicheng Guo, Xiuying Chen, Yaqi Wang, Ruidi Chang, Shichao Pei, Nitesh V Chawla, Olaf Wiest, and Xiangliang Zhang. Large language model based multi-agents: A survey of progress and challenges. arXiv preprint arXiv:2402.01680, 2024.
- [111] Siwei Han, Peng Xia, Ruiyi Zhang, Tong Sun, Yun Li, Hongtu Zhu, and Huaxiu Yao. Mdocagent: A multi-modal multi-agent framework for document understanding. arXiv preprint arXiv:2503.13964, 2025.
- [112] Tianyu Han, Lisa C Adams, Jens-Michalis Papaioannou, Paul Grundmann, Tom Oberhauser, Alexander Löser, Daniel Truhn, and Keno K Bressem. Medalpaca–an open-source collection of medical conversational ai models and training data. arXiv preprint arXiv:2304.08247, 2023.
- [113] Minsheng Hao, Jing Gong, Xin Zeng, Chiming Liu, Yucheng Guo, Xingyi Cheng, Taifeng Wang, Jianzhu Ma, Xuegong Zhang, and Le Song. Large-scale foundation model on single-cell transcriptomics. Nature methods, 21(8):1481–1491, 2024.


- [114] Minsheng Hao, Yongju Lee, Hanchen Wang, Gabriele Scalia, and Aviv Regev. Perturboagent: A self-planning agent for boosting sequential perturb-seq experiments. bioRxiv, pages 2025–05, 2025.
- [115] Kenneth D Harris. Airus: a simple workflow for ai-assisted exploration of scientific data. bioRxiv, pages 2025–02, 2025.
- [116] Kan Hatakeyama-Sato, Naoki Yamane, Yasuhiko Igarashi, Yuta Nabae, and Teruaki Hayakawa. Prompt engineering of gpt-4 for chemical research: what can/cannot be done? Science and Technology of Advanced Materials: Methods, 3(1):2260300, 2023.
- [117] Thomas Hayes, Roshan Rao, Halil Akin, Nicholas J. Sofroniew, Deniz Oktay, Zeming Lin, Robert Verkuil, Vincent Q. Tran, Jonathan Deaton, Marius Wiggert, Rohil Badkundri, Irhum Shafkat, Jun Gong, Alexander Derry, Raul S. Molina, Neil Thomas, Yousuf A. Khan, Chetan Mishra, Carolyn Kim, Liam J. Bartie, Matthew Nemeth, Patrick D. Hsu, Tom Sercu, Salvatore Candido, and Alexander Rives. Simulating 500 million years of evolution with a language model. Science, 387(6736):850– 858, 2025. doi: 10.1126/science.ads0018. URL https://www.science.org/doi/10.1126/ science.ads0018.
- [118] Thomas Hayes, Roshan Rao, Halil Akin, Nicholas J Sofroniew, Deniz Oktay, Zeming Lin, Robert Verkuil, Vincent Q Tran, Jonathan Deaton, Marius Wiggert, et al. Simulating 500 million years of evolution with a language model. Science, 387(6736):850–858, 2025.
- [119] Jiyan He, Weitao Feng, Yaosen Min, Jingwei Yi, Kunsheng Tang, Shuai Li, Jie Zhang, Kejiang Chen, Wenbo Zhou, Xing Xie, Weiming Zhang, Nenghai Yu, and Shuxin Zheng. Control risk for potential misuse of artificial intelligence in science, 2023. URL https://arxiv.org/abs/2312.06632.
- [120] Zhitao He et al. LEGO: A multi-agent collaborative framework with role-playing and iterative feedback for causality explanation generation. In Houda Bouamor, Juan Pino, and Kalika Bali, editors, Findings of the Association for Computational Linguistics: EMNLP 2023, pages 9142–9163, Singapore, December

2023. Association for Computational Linguistics.

- [121] Thorsten Hellert, Drew Bertwistle, Simon C Leemann, Antonin Sulc, and Marco Venturini. Agentic ai for multi-stage physics experiments at a large-scale user facility particle accelerator. arXiv preprint arXiv:2509.17255, 2025.
- [122] Maximilian Herde, Bogdan Raonic, Tobias Rohner, Roger Käppeli, Roberto Molinaro, Emmanuel de Bézenac, and Siddhartha Mishra. Poseidon: Efficient foundation models for PDEs. Advances in Neural Information Processing Systems, 37:72525–72624, 2024.
- [123] Sirui Hong, Xiawu Zheng, Jonathan Chen, Yuheng Cheng, Jinlin Wang, Ceyao Zhang, Zili Wang, Steven Ka Shing Yau, Zijuan Lin, Liyang Zhou, et al. Metagpt: Meta programming for a multi-agent collaborative framework. 2024.
- [124] Julien Horwood and Emmanuel Noutahi. Molecular design in synthetically accessible chemical space via deep reinforcement learning. ACS omega, 5(51):32984–32994, 2020.
- [125] Arian Hosseini, Xingdi Yuan, Nikolay Malkin, Aaron Courville, Alessandro Sordoni, and Rishabh Agarwal. V-star: Training verifiers for self-taught reasoners. arXiv preprint arXiv:2402.06457, 2024.
- [126] Jinming Hu, Hassan Nawaz, Yuting Rui, Lijie Chi, Arif Ullah, and Pavlo O Dral. Aitomia: Your intelligent assistant for ai-driven atomistic and quantum chemical simulations. arXiv preprint arXiv:2505.08195, 2025.


- [127] Mengkang Hu, Yao Mu, Xinmiao Yu, Mingyu Ding, Shiguang Wu, Wenqi Shao, Qiguang Chen, Bin Wang, Yu Qiao, and Ping Luo. Tree-planner: Efficient close-loop task planning with large language models. arXiv preprint arXiv:2310.08582, 2023.
- [128] Ming Hu, Kun Yuan, Yaling Shen, Feilong Tang, Xiaohao Xu, Lin Zhou, Wei Li, Ying Chen, Zhongxing Xu, Zelin Peng, et al. Ophclip: Hierarchical retrieval-augmented learning for ophthalmic surgical video-language pretraining. arXiv preprint arXiv:2411.15421, 2024.
- [129] Ming Hu, Zhengdi Yu, Feilong Tang, Kaiwen Chen, Yulong Li, Imran Razzak, Junjun He, Tolga Birdal, Kaijing Zhou, and Zongyuan Ge. Towards dynamic 3d reconstruction of hand-instrument interaction in ophthalmic surgery. arXiv preprint arXiv:2505.17677, 2025.
- [130] Shengguo Hu, Mingyi Li, Jiawen Xu, Hongrui Zhang, Shanghang Zhang, Tie Jun Cui, Philipp Del Hougne, and Lianlin Li. Electromagnetic metamaterial agent. Light: Science & Applications, 14(1):12, 2025.
- [131] Xiang Hu, Hongyu Fu, Jinge Wang, Yifeng Wang, Zhikun Li, Renjun Xu, Yu Lu, Yaochu Jin, Lili Pan, and Zhenzhong Lan. Nova: An iterative planning and search approach to enhance novelty and diversity of llm generated ideas. arXiv preprint arXiv:2410.14255, 2024.
- [132] Zhaolin Hu, Yixiao Zhou, Zhongan Wang, Xin Li, Weimin Yang, Hehe Fan, and Yi Yang. OSDA agent: Leveraging large language models for de novo design of organic structure directing agents. In The Thirteenth International Conference on Learning Representations, 2025. URL <https://openreview. net/forum?id=9YNyiCJE3k>.
- [133] Changwu Huang, Zeqi Zhang, Bifei Mao, and Xin Yao. An overview of artificial intelligence ethics. IEEE Transactions on Artificial Intelligence, 4(4):799–819, 2022.
- [134] Di Huang, Hao Li, Wenyu Li, Heming Zhang, Patricia Dickson, Ming Zhan, J Philip Miller, Carlos Cruchaga, Michael Province, Yixin Chen, Philip Payne, and Fuhai Li. Omnicellagent: Towards ai coscientists for scientific discovery in precision medicine. August 2025. doi: 10.1101/2025.07.31.667797. URL http://dx.doi.org/10.1101/2025.07.31.667797.
- [135] Kaixuan Huang, Yuanhao Qu, Henry Cousins, William A Johnson, Di Yin, Mihir Shah, Denny Zhou, Russ Altman, Mengdi Wang, and Le Cong. Crispr-gpt: An llm agent for automated design of geneediting experiments. arXiv preprint arXiv:2404.18021, 2024.
- [136] Kexin Huang, Serena Zhang, Hanchen Wang, Yuanhao Qu, Yingzhou Lu, Yusuf Roohani, Ryan Li, Lin Qiu, Junze Zhang, Yin Di, et al. Biomni: A general-purpose biomedical ai agent. bioRxiv, pages 2025–05, 2025.
- [137] Lei Huang, Weijiang Yu, Weitao Ma, Weihong Zhong, Zhangyin Feng, Haotian Wang, Qianglong Chen, Weihua Peng, Xiaocheng Feng, Bing Qin, et al. A survey on hallucination in large language models: Principles, taxonomy, challenges, and open questions. ACM Transactions on Information Systems, 43

(2):1–55, 2025.

- [138] Xu Huang, Weiwen Liu, Xiaolong Chen, Xingmei Wang, Hao Wang, Defu Lian, Yasheng Wang, Ruiming Tang, and Enhong Chen. Understanding the planning of llm agents: A survey. arXiv preprint arXiv:2402.02716, 2024.


- [139] Mingjia Huo, Han Guo, Xingyi Cheng, Digvijay Singh, Hamidreza Rahmani, Shen Li, Philipp Gerlof, Trey Ideker, Danielle A Grotjahn, Elizabeth Villa, et al. Multi-modal large language model enables protein function prediction. bioRxiv, pages 2024–08, 2024.
- [140] Theo Jaffrelot Inizan, Sherry Yang, Aaron Kaplan, Yen-hsu Lin, Jian Yin, Saber Mirzaei, Mona Abdelgaid, Ali H Alawadhi, KwangHwan Cho, Zhiling Zheng, et al. System of agentic ai for the discovery of metal-organic frameworks. arXiv preprint arXiv:2504.14110, 2025.
- [141] Yoshitaka Inoue, Tianci Song, and Tianfan Fu. Drugagent: Explainable drug repurposing agent with large language model-based reasoning. arXiv preprint arXiv:2408.13378, 2024.
- [142] Kartheik G Iyer, Mikaeel Yunus, Charles O’Neill, Christine Ye, Alina Hyk, Kiera Mccormick, Ioana Ciucă, John F Wu, Alberto Accomazzi, Simone Astarita, et al. pathfinder: A semantic framework for literature review and knowledge discovery in astronomy. The Astrophysical Journal Supplement Series, 275(2):38, 2024.
- [143] Kevin Maik Jablonka, Qianxiang Ai, Alexander Al-Feghali, Shruti Badhwar, Joshua D Bocarsly, Andres M Bran, Stefan Bringuier, L Catherine Brinson, Kamal Choudhary, Defne Circi, et al. 14 examples of how llms can transform materials science and chemistry: a reflection on a large language model hackathon. Digital Discovery, 2(5):1233–1250, 2023.
- [144] Masoud Jafaripour, Shadan Golestan, Shotaro Miwa, Yoshihiro Mitsuka, and Osmar Zaiane. Adaptive iterative feedback prompting for obstacle-aware path planning via llms. In AAAI Workshop, 2025.
- [145] Raj Jaiswal, Dhruv Jain, Harsh Parimal Popat, Avinash Anand, Abhishek Dharmadhikari, Atharva Marathe, and Rajiv Ratn Shah. Improving physics reasoning in large language models using mixture of refinement agents. arXiv preprint arXiv:2412.00821, 2024.
- [146] Peter Jansen, Marc-Alexandre Côté, Tushar Khot, Erin Bransom, Bhavana Dalvi Mishra, Bodhisattwa Prasad Majumder, Oyvind Tafjord, and Peter Clark. Discoveryworld: A virtual environment for developing and evaluating automated scientific discovery agents. Advances in Neural Information Processing Systems, 37:10088–10116, 2024.
- [147] Peter Jansen, Oyvind Tafjord, Marissa Radensky, Pao Siangliulue, Tom Hope, Bhavana Dalvi Mishra, Bodhisattwa Prasad Majumder, Daniel S Weld, and Peter Clark. Codescientist: End-to-end semiautomated scientific discovery with code-based experimentation. arXiv preprint arXiv:2503.22708, 2025.
- [148] Shankar Kumar Jeyakumar, Alaa Alameer Ahmad, and Adrian Garret Gabriel. Advancing agentic systems: Dynamic task decomposition, tool integration and evaluation using novel metrics and dataset. In NeurIPS 2024 Workshop on Open-World Agents, 2024.
- [149] Shuyi Jia, Chao Zhang, and Victor Fung. Llmatdesign: Autonomous materials discovery with large language models. arXiv preprint arXiv:2406.13163, 2024.
- [150] Huiqiang Jiang, Qianhui Wu, Chin-Yew Lin, Yuqing Yang, and Lili Qiu. Llmlingua: Compressing prompts for accelerated inference of large language models. pages 13358–13376, 2023.
- [151] Jinhao Jiang, Zhipeng Chen, Yingqian Min, Jie Chen, Xiaoxue Cheng, Jiapeng Wang, Yiru Tang, Haoxiang Sun, Jia Deng, Wayne Xin Zhao, et al. Technical report: Enhancing llm reasoning with reward-guided tree search. arXiv preprint arXiv:2411.11694, 2024.


- [152] Lei Jiang, Shuzhou Sun, Biqing Qi, Yuchen Fu, Xiaohua Xu, Yuqiang Li, Dongzhan Zhou, and Tianfan Fu. Chem3dllm: 3d multimodal large language models for chemistry. arXiv preprint, 2025.
- [153] Shuyang Jiang, Yuhao Wang, and Yu Wang. Selfevolve: A code evolution framework via large language models. arXiv preprint arXiv:2306.02907, 2023.
- [154] Zhengyao Jiang, Dominik Schmidt, Dhruv Srikanth, Dixing Xu, Ian Kaplan, Deniss Jacenko, and Yuxiang Wu. Aide: Ai-driven exploration in the space of code, 2025. URL https://arxiv.org/ abs/2502.13138.
- [155] Ruofan Jin, Zaixi Zhang, Mengdi Wang, and Le Cong. Stella: Self-evolving llm agent for biomedical research. arXiv preprint arXiv:2507.02004, 2025.
- [156] Sebastian Antony Joseph, Syed Murtaza Husain, Stella SR Offner, Stéphanie Juneau, Paul Torrey, Adam S Bolton, Juan P Farias, Niall Gaffney, Greg Durrett, and Junyi Jessy Li. Astrovisbench: A code benchmark for scientific computing and visualization in astronomy. arXiv preprint arXiv:2505.20538, 2025.
- [157] John Jumper, Richard Evans, Alexander Pritzel, Tim Green, Michael Figurnov, Olaf Ronneberger, Kathryn Tunyasuvunakool, Russ Bates, Augustin Žídek, Anna Potapenko, et al. Highly accurate protein structure prediction with alphafold. nature, 596(7873):583–589, 2021.
- [158] A Jun, Xiang Zhang, Xiaofan Zhang, Jiaqi Wei, Te Zhang, Yamin Deng, Pu Liu, Zongxiang Nie, Yi Chen, Nanqin Dong, et al. Massnet: billion-scale ai-friendly mass spectral corpus enables robust de novo peptide sequencing. bioRxiv, 2025.
- [159] Yeonghun Kang and Jihan Kim. Chatmof: An autonomous ai system for predicting and generating metal-organic frameworks. arXiv preprint arXiv:2308.01423, 2023.
- [160] Akbir Khan, John Hughes, Dan Valentine, Laura Ruis, Kshitij Sachan, Ansh Radhakrishnan, Edward Grefenstette, Samuel R Bowman, Tim Rocktäschel, and Ethan Perez. Debating with more persuasive llms leads to more truthful answers. arXiv preprint arXiv:2402.06782, 2024.
- [161] Byeonghwi Kim, Minhyuk Seo, and Jonghyun Choi. Online continual learning for interactive instruction following agents, 2024. URL https://arxiv.org/abs/2403.07548.
- [162] Hyomin Kim, Yunhui Jang, and Sungsoo Ahn. Mt-mol: Multi agent system with tool-based reasoning for molecular optimization. arXiv preprint arXiv:2505.20820, 2025.
- [163] Kyungha Kim, Sangyun Lee, Kung-Hsiang Huang, Hou Pong Chan, Manling Li, and Heng Ji. Can llms produce faithful explanations for fact-checking? towards faithful explainable fact-checking via multi-agent debate. arXiv preprint arXiv:2402.07401, 2024.
- [164] Yubin Kim, Chanwoo Park, Hyewon Jeong, Yik Siu Chan, Xuhai Xu, Daniel McDuff, Hyeonhoon Lee, Marzyeh Ghassemi, Cynthia Breazeal, Hae Park, et al. Mdagents: An adaptive collaboration of llms for medical decision-making. 37:79410–79452, 2024.
- [165] James Kirkpatrick, Razvan Pascanu, Neil Rabinowitz, Joel Veness, Guillaume Desjardins, Andrei A Rusu, Kieran Milan, John Quan, Tiago Ramalho, Agnieszka Grabska-Barwinska, et al. Overcoming catastrophic forgetting in neural networks. Proceedings of the national academy of sciences, 114(13): 3521–3526, 2017.


- [166] Takeshi Kojima, Shixiang Shane Gu, Machel Reid, Yutaka Matsuo, and Yusuke Iwasawa. Large language models are zero-shot reasoners. 35:22199–22213, 2022.
- [167] Nikolay Koldunov and Thomas Jung. Local climate services for all, courtesy of large language models. Communications Earth & Environment, 5(1):13, Jan 2024. ISSN 2662-4435. doi: 10.1038/ s43247-023-01199-1. URL https://doi.org/10.1038/s43247-023-01199-1.
- [168] Vadim Korolev and Pavel Protsenko. Accurate, interpretable predictions of materials properties within transformer language models. Patterns, 4(10):100803, October 2023. ISSN 2666-3899. doi: 10. 1016/j.patter.2023.100803. URL http://dx.doi.org/10.1016/j.patter.2023.100803.
- [169] Dmitriy Kostunin, Vladimir Sotnikov, Sergo Golovachev, and Alexandre Strube. Ai agents for groundbased gamma astronomy. arXiv preprint arXiv:2503.00821, 2025.
- [170] Christopher Kuenneth and Rampi Ramprasad. polybert: a chemical language model to enable fully machine-driven ultrafast polymer informatics. Nature Communications, 14(1), July 2023. ISSN 2041-1723. doi: 10.1038/s41467-023-39868-6. URL http://dx.doi.org/10.1038/ s41467-023-39868-6.
- [171] Varun Kumar, Leonard Gleyzer, Adar Kahana, Khemraj Shukla, and George Em Karniadakis. Mycrunchgpt: A llm assisted framework for scientific machine learning. Journal of Machine Learning for Modeling and Computing, 4(4), 2023.
- [172] Shrinidhi Kumbhar, Venkatesh Mishra, Kevin Coutinho, Divij Handa, Ashif Iquebal, and Chitta Baral. Hypothesis generation for materials discovery and design using goal-driven and constraint-guided llm agents. arXiv preprint arXiv:2501.13299, 2025.
- [173] Yanis Labrak, Adrien Bazoge, Emmanuel Morin, Pierre-Antoine Gourraud, Mickael Rouvier, and Richard Dufour. Biomistral: A collection of open-source pretrained large language models for medical domains, 2024.
- [174] Yuhang Lai, Chengxi Li, Yiming Wang, Tianyi Zhang, Ruiqi Zhong, Luke Zettlemoyer, Scott Wen tau Yih, Daniel Fried, Sida Wang, and Tao Yu. Ds-1000: A natural and reliable benchmark for data science code generation, 2022. URL https://arxiv.org/abs/2211.11501.
- [175] Zheyuan Lai and Yingming Pu. Prim: Principle-inspired material discovery through multi-agent collaboration. arXiv preprint arXiv:2504.08810, 2025.
- [176] Jakub Lála, Odhran O’Donoghue, Aleksandar Shtedritski, Sam Cox, Samuel G Rodriques, and Andrew D White. Paperqa: Retrieval-augmented generative agent for scientific research. 2023.
- [177] Alireza Rashidi Laleh and Majid Nili Ahmadabadi. A survey on enhancing reinforcement learning in complex environments: Insights from human and llm feedback. arXiv preprint arXiv:2411.13410, 2024.
- [178] Andrew Laverick, Kristen Surrao, Inigo Zubeldia, Boris Bolliet, Miles Cranmer, Antony Lewis, Blake Sherwin, and Julien Lesgourgues. Multi-agent system for cosmological parameter analysis. arXiv preprint arXiv:2412.00431, 2024.
- [179] Namkyeong Lee, Edward De Brouwer, Ehsan Hajiramezanali, Tommaso Biancalani, Chanyoung Park, and Gabriele Scalia. Rag-enhanced collaborative llm agents for drug discovery. arXiv preprint arXiv:2502.17506, 2025.


- [180] Seowoo Lee, Jiwon Youn, Hyungjin Kim, Mansu Kim, and Soon Ho Yoon. Cxr-llava: a multimodal large language model for interpreting chest x-ray images, 2024. URL https://arxiv.org/abs/ 2310.18341.
- [181] Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, et al. Retrieval-augmented generation for knowledge-intensive nlp tasks. Advances in neural information processing systems, 33:9459–9474, 2020.
- [182] Bingxuan Li, Yiwei Wang, Jiuxiang Gu, Kai-Wei Chang, and Nanyun Peng. Metal: A multi-agent framework for chart generation with test-time scaling. arXiv preprint arXiv:2502.17651, 2025.
- [183] Chunyuan Li, Cliff Wong, Sheng Zhang, Naoto Usuyama, Haotian Liu, Jianwei Yang, Tristan Naumann, Hoifung Poon, and Jianfeng Gao. LLaVA-Med: Training a large language-and-vision assistant for biomedicine in one day. Advances in Neural Information Processing Systems, 36:28541–28564, 2023.
- [184] Guohao Li, Hasan Abed Al Kader Hammoud, Hani Itani, Dmitrii Khizbullin, and Bernard Ghanem. Camel: Communicative agents for "mind" exploration of large language model society. 2023.
- [185] Haoyuan Li, Hao Jiang, Tianke Zhang, Zhelun Yu, Aoxiong Yin, Hao Cheng, Siming Fu, Yuhao Zhang, and Wanggui He. Traineragent: Customizable and efficient model training through llm-powered multi-agent system. arXiv preprint arXiv:2311.06622, 2023.
- [186] Jie Li, Fuyong Zhao, Panfeng Chen, Jiafu Xie, Xiangrui Zhang, Hui Li, Mei Chen, Yanhao Wang, and Ming Zhu. An astronomical question answering dataset for evaluating large language models. Scientific Data, 12(1):447, 2025.
- [187] Junkai Li, Yunghwei Lai, Weitao Li, Jingyi Ren, Meng Zhang, Xinhui Kang, Siyu Wang, Peng Li, Ya-Qin Zhang, Weizhi Ma, et al. Agent hospital: A simulacrum of hospital with evolvable medical agents. arXiv preprint arXiv:2405.02957, 2024.
- [188] Junyi Li, Yongqiang Chen, Chenxi Liu, Qianyi Cai, Tongliang Liu, Bo Han, Kun Zhang, and Hui Xiong. Can large language models help experimental design for causal discovery?, 2025. URL https://arxiv.org/abs/2503.01139.
- [189] Rui Li, Zixuan Hu, Wenxi Qu, Jinouwen Zhang, Zhenfei Yin, Sha Zhang, Xuantuo Huang, Hanqing Wang, Tai Wang, Jiangmiao Pang, et al. Labutopia: High-fidelity simulation and hierarchical benchmark for scientific embodied agents. arXiv preprint arXiv:2505.22634, 2025.
- [190] Shimin Li, Tianxiang Sun, Qinyuan Cheng, and Xipeng Qiu. Agent alignment in evolving social norms,

2024. URL https://arxiv.org/abs/2401.04620.

- [191] Tianbin Li, Yanzhou Su, Wei Li, Bin Fu, Zhe Chen, Ziyan Huang, Guoan Wang, Chenglong Ma, Ying Chen, Ming Hu, et al. Gmai-vl & gmai-vl-5.5 m: A large vision-language model and a comprehensive multimodal dataset towards general medical ai. arXiv preprint arXiv:2411.14522, 2024.
- [192] Tianbin Li, Yanzhou Su, Wei Li, Bin Fu, Zhe Chen, Ziyan Huang, Guoan Wang, Chenglong Ma, Ying Chen, Ming Hu, Yanjun Li, Pengcheng Chen, Xiaowei Hu, Zhongying Deng, Yuanfeng Ji, Jin Ye, Yu Qiao, and Junjun He. GMAI-VL & GMAI-VL-5.5m: A large vision-language model and a comprehensive multimodal dataset towards general medical ai. arXiv preprint arXiv:2411.14522, 2025.


- [193] Weichen Li and Weimin Pan. Enhancing chain-of-thought reasoning in large language models through text style diversity and prompt fusion. In EIBDCT, volume 13181, pages 226–232. SPIE, 2024.
- [194] Yifei Li, Hanane Nour Moussa, Ziru Chen, Shijie Chen, Botao Yu, Mingyi Xue, Benjamin Burns, Tzu-Yao Chiu, Vishal Dey, Zitong Lu, et al. Autosdt: Scaling data-driven discovery tasks toward open co-scientists. arXiv preprint arXiv:2506.08140, 2025.
- [195] Yiming Li, Shunli Ren, Pengxiang Wu, Siheng Chen, Chen Feng, and Wenjun Zhang. Learning distilled collaboration graph for multi-agent perception. 34:29541–29552, 2021.
- [196] Zhucong Li, Bowei Zhang, Jin Xiao, Zhijian Zhou, Fenglei Cao, Jiaqing Liang, and Yuan Qi. Chemhas: Hierarchical agent stacking for enhancing chemistry tools. arXiv preprint arXiv:2505.21569, 2025.
- [197] Tian Liang, Zhiwei He, Wenxiang Jiao, Xing Wang, Yan Wang, Rui Wang, Yujiu Yang, Shuming Shi, and Zhaopeng Tu. Encouraging divergent thinking in large language models through multi-agent debate. arXiv preprint arXiv:2305.19118, 2023.
- [198] Tian Liang, Zhiwei He, Wenxiang Jiao, Xing Wang, Yan Wang, Rui Wang, Yujiu Yang, Shuming Shi, and Zhaopeng Tu. Encouraging divergent thinking in large language models through multi-agent debate. pages 17889–17904, 2024.
- [199] Wang Liang. LLaMA-Gene: A general-purpose gene task large language model based on instruction fine-tuning. arXiv preprint arXiv:2412.00471, 2024.
- [200] Xuechen Liang, Yangfan He, Yinghui Xia, Xinyuan Song, Jianhui Wang, Meiling Tao, Li Sun, Xinhang Yuan, Jiayi Su, Keqin Li, et al. Self-evolving agents with reflective and memory-augmented abilities. arXiv preprint arXiv:2409.00872, 2024.
- [201] Zeming Lin, Halil Akin, Roshan Rao, Brian Hie, Zhongkai Zhu, Wenting Lu, Nikita Smetanin, Allan dos Santos Costa, Maryam Fazel-Zarandi, Tom Sercu, Sal Candido, et al. Language models of protein sequences at the scale of evolution enable accurate structure prediction. bioRxiv, 2022.
- [202] Mario Lino, Stathi Fotiadis, Anil A Bharath, and Chris D Cantwell. Current and emerging deep-learning methods for the simulation of fluid dynamics. Proceedings of the Royal Society A, 479(2275):20230058, 2023.
- [203] Bang Liu, Xinfeng Li, Jiayi Zhang, Jinlin Wang, Tanjin He, Sirui Hong, Hongzhang Liu, Shaokun Zhang, Kaitao Song, Kunlun Zhu, et al. Advances and challenges in foundation agents: From brain-inspired intelligence to evolutionary, collaborative, and safe systems. arXiv preprint arXiv:2504.01990, 2025.
- [204] Haoyang Liu, Yijiang Li, Jinglin Jian, Yuxuan Cheng, Jianrong Lu, Shuyi Guo, Jinglei Zhu, Mianchen Zhang, Miantong Zhang, and Haohan Wang. Toward a team of ai-made scientists for scientific discovery from gene expression data. arXiv preprint arXiv:2402.12391, 2024.
- [205] Jiachen Liu, Ziheng Geng, Ran Cao, Lu Cheng, Paolo Bocchini, and Minghui Cheng. A large language model-empowered agent for reliable and robust structural analysis. arXiv preprint arXiv:2507.02938, 2025.
- [206] Junhua Liu, Fanfan Lin, Xinze Li, Kwan Hui Lim, and Shuai Zhao. Physics-informed llm-agent for automated modulation design in power electronics systems. arXiv preprint arXiv:2411.14214, 2024.


- [207] Ruibo Liu, Jason Wei, Shixiang Shane Gu, Te-Yen Wu, Soroush Vosoughi, Claire Cui, Denny Zhou, and Andrew M. Dai. Mind’s eye: Grounded language model reasoning through simulation. In The Eleventh International Conference on Learning Representations, ICLR 2023, Kigali, Rwanda, May 1-5,

2023. OpenReview.net, 2023. URL https://openreview.net/forum?id=4rXMRuoJlai.

- [208] Shengchao Liu, Yanjing Li, Zhuoxinran Li, Anthony Gitter, Yutao Zhu, Jiarui Lu, Zhao Xu, Weili Nie, Arvind Ramanathan, Chaowei Xiao, Jian Tang, Hongyu Guo, and Anima Anandkumar. A text-guided protein design framework. arXiv preprint, 2023. doi: 10.48550/arXiv.2302.04611. v4, 2025.
- [209] Sizhe Liu, Yizhou Lu, Siyu Chen, Xiyang Hu, Jieyu Zhao, Yingzhou Lu, and Yue Zhao. Drugagent: Automating ai-aided drug discovery programming through llm multi-agent collaboration. arXiv preprint arXiv:2411.15692, 2024.
- [210] Wanhao Liu, Zonglin Yang, Jue Wang, Lidong Bing, Di Zhang, Dongzhan Zhou, Yuqiang Li, Houqiang Li, Erik Cambria, and Wanli Ouyang. Moose-chem3: Toward experiment-guided hypothesis ranking via simulated experimental feedback. arXiv preprint arXiv:2505.17873, 2025.
- [211] Yang Liu, Peng Sun, and Hang Li. Large language models as agents in two-player games. arXiv preprint arXiv:2402.08078, 2024.
- [212] Yuyan Liu, Sirui Ding, Sheng Zhou, Wenqi Fan, and Qiaoyu Tan. Moleculargpt: Open large language model (llm) for few-shot molecular property prediction. arXiv preprint arXiv:2406.12950, 2024.
- [213] Zequn Liu, Wei Zhang, Yingce Xia, Lijun Wu, Shufang Xie, Tao Qin, Ming Zhang, and Tie-Yan Liu. Molxpt: Wrapping molecules with text for generative pre-training, 2023. URL https://arxiv. org/abs/2305.10688.
- [214] Zhengliang Liu, Yiwei Li, Peng Shu, Aoxiao Zhong, Longtao Yang, Chao Ju, Zihao Wu, Chong Ma, Jie Luo, Cheng Chen, Sekeun Kim, Jiang Hu, Haixing Dai, Lin Zhao, Dajiang Zhu, Jun Liu, Wei Liu, Dinggang Shen, Tianming Liu, Quanzheng Li, and Xiang Li. Radiology-llama2: Best-in-class large language model for radiology, 2023. URL https://arxiv.org/abs/2309.06419.
- [215] Zijun Liu, Kaiming Liu, Yiqi Zhu, Xuanyu Lei, Zonghan Yang, Zhenhe Zhang, Peng Li, and Yang Liu. Aigs: Generating science from ai-powered automated falsification. arXiv preprint arXiv:2411.11910, 2024.
- [216] Zijun Liu, Yanzhe Zhang, Peng Li, Yang Liu, and Diyi Yang. A dynamic llm-powered agent network for task-oriented agent collaboration. In COLM, 2024.
- [217] Zijun Liu et al. A dynamic LLM-powered agent network for task-oriented agent collaboration. In First Conference on Language Modeling, Oct. 2024.
- [218] Jieyi Long. Large language model guided tree-of-thought. arXiv preprint arXiv:2305.08291, 2023.
- [219] Chris Lu, Cong Lu, Robert Tjarko Lange, Jakob Foerster, Jeff Clune, and David Ha. The ai scientist: Towards fully automated open-ended scientific discovery. arXiv preprint arXiv:2408.06292v3, 2024. URL https://www.arxiv.org/abs/2408.06292v3.
- [220] Darui Lu, Jordan M Malof, and Willie J Padilla. An agentic framework for autonomous metamaterial modeling and inverse design. arXiv preprint arXiv:2506.06935, 2025.


- [221] Yi Luo, Linghang Shi, Yihao Li, Aobo Zhuang, Yeyun Gong, Ling Liu, and Chen Lin. From intention to implementation: automating biomedical research via llms. Science China Information Sciences, 68(7): 1–18, 2025.
- [222] Ziming Luo, Zonglin Yang, Zexin Xu, Wei Yang, and Xinya Du. Llm4sr: A survey on large language models for scientific research. arXiv preprint arXiv:2501.04306, 2025.
- [223] Liuzhenghao Lv, Zongying Lin, Hao Li, Yuyang Liu, Jiaxi Cui, Calvin Yu-Chian Chen, Li Yuan, and Yonghong Tian. Prollama: A protein language model for multi-task protein language processing. arXiv preprint, 2024. doi: 10.48550/arXiv.2402.16445.
- [224] Artem Lykov, Maria Dronova, Nikolay Naglov, Mikhail Litvinov, Sergei Satsevich, Artem Bazhenov, Vladimir Berman, Aleksei Shcherbak, and Dzmitry Tsetserukou. Llm-mars: Large language model for behavior tree generation and nlp-enhanced dialogue in multi-agent robot systems. arXiv preprint arXiv:2312.09348, 2023.
- [225] Chengdong Ma, Ziran Yang, Hai Ci, Jun Gao, Minquan Gao, Xuehai Pan, and Yaodong Yang. Evolving diverse red-team language models in multi-round multi-agent games. arXiv preprint arXiv:2310.00322, 2023.
- [226] Hao Ma, Tianyi Hu, Zhiqiang Pu, Liu Boyin, Xiaolin Ai, Yanyan Liang, and Min Chen. Coevolving with the other you: Fine-tuning llm with sequential cooperative multi-agent reinforcement learning. 37:15497–15525, 2024.
- [227] Kangyong Ma. Ai agents in chemical research: Gvim–an intelligent research assistant system. Digital Discovery, 4(2):355–375, 2025.
- [228] Yubo Ma, Zhibin Gou, Junheng Hao, Ruochen Xu, Shuohang Wang, Liangming Pan, Yujiu Yang, Yixin Cao, and Aixin Sun. Sciagent: Tool-augmented language models for scientific reasoning. In Yaser Al-Onaizan, Mohit Bansal, and Yun-Nung Chen, editors, Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, EMNLP 2024, Miami, FL, USA, November 12-16, 2024, pages 15701–15736. Association for Computational Linguistics, 2024. URL https: //aclanthology.org/2024.emnlp-main.880.
- [229] Yubo Ma, Zhibin Gou, Junheng Hao, Ruochen Xu, Shuohang Wang, Liangming Pan, Yujiu Yang, Yixin Cao, Aixin Sun, Hany Awadalla, et al. Sciagent: Tool-augmented language models for scientific reasoning. arXiv preprint arXiv:2402.11451, 2024.
- [230] Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, et al. Self-refine: Iterative refinement with self-feedback. 36:46534–46594, 2023.
- [231] Bodhisattwa Prasad Majumder, Bhavana Dalvi Mishra, Peter Jansen, Oyvind Tafjord, Niket Tandon, Li Zhang, Chris Callison-Burch, and Peter Clark. Clin: A continually learning language agent for rapid task adaptation and generalization, 2023. URL https://arxiv.org/abs/2310.10134.
- [232] Indrajeet Mandal, Jitendra Soni, Mohd Zaki, Morten M Smedskjaer, Katrin Wondraczek, Lothar Wondraczek, Nitya Nand Gosvami, and NM Krishnan. Autonomous microscopy experiments through large language model agents. arXiv preprint arXiv:2501.10385, 2024.
- [233] David Maranto. Llmsat: A large language model-based goal-oriented agent for autonomous space exploration. arXiv preprint arXiv:2405.01392, 2024.


- [234] Ahmed Masry, Do Xuan Long, Jia Qing Tan, Shafiq Joty, and Enamul Hoque. Chartqa: A benchmark for question answering about charts with visual and logical reasoning, 2022. URL https://arxiv. org/abs/2203.10244.
- [235] Tula Masterman, Sandi Besen, Mason Sawtell, and Alex Chao. The landscape of emerging ai agent architectures for reasoning, planning, and tool calling: A survey. arXiv preprint arXiv:2404.11584, 2024.
- [236] Andrew D McNaughton, Gautham Krishna Sankar Ramalaxmi, Agustin Kruel, Carter R Knutson, Rohith A Varikoti, and Neeraj Kumar. Cactus: Chemistry agent connecting tool usage to science. ACS omega, 9(46):46563–46573, 2024.
- [237] Nikita Mehandru, Amanda K Hall, Olesya Melnichenko, Yulia Dubinina, Daniel Tsirulnikov, David Bamman, Ahmed Alaa, Scott Saponas, and Venkat S Malladi. Bioagents: Democratizing bioinformatics analysis with multi-agent systems. arXiv preprint arXiv:2501.06314, 2025.
- [238] Lingrui Mei, Jiayu Yao, Yuyao Ge, Yiwei Wang, Baolong Bi, Yujun Cai, Jiazhi Liu, Mingyu Li, Zhong-Zhi Li, Duzhen Zhang, et al. A survey of context engineering for large language models. arXiv preprint arXiv:2507.13334, 2025.
- [239] Siddharth Mishra-Sharma, Yiding Song, and Jesse Thaler. Paperclip: Associating astronomical observations and natural language with multi-modal models. arXiv preprint arXiv:2403.08851, 2024.
- [240] Michael Moor, Qian Huang, Shirley Wu, Michihiro Yasunaga, Cyril Zakka, Yash Dalmia, Eduardo Pontes Reis, Pranav Rajpurkar, and Jure Leskovec. Med-flamingo: A multimodal medical few-shot learner. arXiv preprint arXiv:2307.15189, 2023.
- [241] Adam Moss. The ai cosmologist i: An agentic system for automated data analysis. arXiv preprint arXiv:2504.03424, 2025.
- [242] Vladimir Naumov, Diana Zagirova, Sha Lin, Yupeng Xie, Wenhao Gou, Anatoly Urban, Nina Tikhonova, Khadija Alawi, Mike Durymanov, Fedor Galkin, et al. Dora ai scientist: Multi-agent virtual research team for scientific exploration discovery and automated report generation. bioRxiv, 2025.
- [243] Benjamin Newman, Yoonjoo Lee, Aakanksha Naik, Pao Siangliulue, Raymond Fok, Juho Kim, Daniel S. Weld, Joseph Chee Chang, and Kyle Lo. Arxivdigestables: Synthesizing scientific literature into tables using language models, 2024. URL https://arxiv.org/abs/2410.22360.
- [244] Eric Nguyen, Michael Poli, Matthew G Durrant, Brian Kang, Dhruva Katrekar, David B Li, Liam J Bartie, Armin W Thomas, Samuel H King, Garyk Brixi, et al. Sequence modeling and design from molecular to genome scale with evo. Science, 386(6723):eado9336, 2024.
- [245] Tuan Dung Nguyen, Yuan-Sen Ting, Ioana Ciucă, Charlie O’Neill, Ze-Chang Sun, Maja Jabłońska, Sandor Kruk, Ernest Perkowski, Jack Miller, Jason Li, et al. Astrollama: Towards specialized foundation models in astronomy. arXiv preprint arXiv:2309.06126, 2023.
- [246] Tuan Dung Nguyen, Yuan-Sen Ting, Ioana Ciucă, Charlie O’Neill, Ze-Chang Sun, Maja Jabłońska, Sandor Kruk, Ernest Perkowski, Jack Miller, Jason Li, et al. Astrollama: Towards specialized foundation models in astronomy. arXiv preprint arXiv:2309.06126, 2023.


- [247] Bo Ni and Markus J Buehler. Mechagents: Large language model multi-agent collaborations can solve mechanics problems, generate new data, and integrate knowledge. Extreme Mechanics Letters, 67: 102131, 2024.
- [248] Ziqi Ni, Yahao Li, Kaijia Hu, Kunyuan Han, Ming Xu, Xingyu Chen, Fengqi Liu, Yicong Ye, and Shuxin Bai. Matpilot: an llm-enabled ai materials scientist under the framework of human-machine collaboration. arXiv preprint arXiv:2411.08063, 2024.
- [249] Seyednami Niyakan and Xiaoning Qian. Phenograph: A multi-agent framework for phenotype-driven discovery in spatial transcriptomics data augmented with knowledge graphs. bioRxiv, pages 2025–06, 2025.
- [250] Alexander Novikov, Ngân V˜u, Marvin Eisenberger, Emilien Dupont, Po-Sen Huang, Adam Zsolt Wagner, Sergey Shirobokov, Borislav Kozlovskii, Francisco JR Ruiz, Abbas Mehrabian, et al. Alphaevolve: A coding agent for scientific and algorithmic discovery. arXiv preprint arXiv:2506.13131, 2025.
- [251] Janghoon Ock, Radheesh Sharma Meda, Srivathsan Badrinarayanan, Neha S Aluru, Achuth Chandrasekhar, and Amir Barati Farimani. Large language model agent for modular task execution in drug discovery. arXiv preprint arXiv:2507.02925, 2025.
- [252] Odhran O’Donoghue, Aleksandar Shtedritski, John Ginger, Ralph Abboud, Ali Essa Ghareeb, Justin Booth, and Samuel G Rodriques. Bioplanner: Automatic evaluation of llms on protocol planning in biology, 2023. URL https://arxiv.org/abs/2310.10632.
- [253] Ryotaro Okabe, Zack West, Abhijatmedhi Chotrattanapituk, Mouyang Cheng, Denisse Córdova Carrizales, Weiwei Xie, Robert J. Cava, and Mingda Li. Large language model-guided prediction toward quantum materials synthesis, 2024. URL https://arxiv.org/abs/2410.20976.
- [254] Jiefu Ou, William Gantt Walden, Kate Sanders, Zhengping Jiang, Kaiser Sun, Jeffrey Cheng, William Jurayj, Miriam Wanner, Shaobo Liang, Candice Morgan, Seunghoon Han, Weiqi Wang, Chandler May, Hannah Recknor, Daniel Khashabi, and Benjamin Van Durme. Claimcheck: How grounded are llm critiques of scientific papers?, 2025. URL https://arxiv.org/abs/2503.21717.
- [255] Charles Packer, Vivian Fang, Shishir G Patil, Kevin Lin, Sarah Wooders, and Joseph E Gonzalez. Memgpt: Towards llms as operating systems. CoRR, 2023.
- [256] Haining Pan, Nayantara Mudur, William Taranto, Maria Tikhanovskaya, Subhashini Venugopalan, Yasaman Bahri, Michael P Brenner, and Eun-Ah Kim. Quantum many-body physics calculations with large language models. Communications Physics, 8(1):49, 2025.
- [257] Rui Pan, Tuan Dung Nguyen, Hardik Arora, Alberto Accomazzi, Tirthankar Ghosal, and Yuan-Sen Ting. Astromlab 2: Astrollama-2-70b model and benchmarking specialised llms for astronomy. In SC24-W: Workshops of the International Conference for High Performance Computing, Networking, Storage and Analysis, pages 87–96. IEEE, 2024.
- [258] Sandeep Pandey, Ran Xu, Wenkang Wang, and Xu Chu. Openfoamgpt: a rag-augmented llm agent for openfoam-based computational fluid dynamics. arXiv preprint arXiv:2501.06327, 2025.
- [259] Jing-Cheng Pang, Pengyuan Wang, Kaiyuan Li, Xiong-Hui Chen, Jiacheng Xu, Zongzhang Zhang, and Yang Yu. Language model self-improvement by reinforcement learning contemplation. 2024.


- [260] J Gregory Pauloski, Yadu Babuji, Ryan Chard, Mansi Sakarvadia, Kyle Chard, and Ian Foster. Empowering scientific workflows with federated agents. arXiv preprint arXiv:2505.05428, 2025.
- [261] Ernest Perkowski, Rui Pan, Tuan Dung Nguyen, Yuan-Sen Ting, Sandor Kruk, Tong Zhang, Charlie O’Neill, Maja Jablonska, Zechang Sun, Michael J Smith, et al. Astrollama-chat: Scaling astrollama with conversational and diverse datasets. Research Notes of the AAS, 8(1):7, 2024.
- [262] Thang D Pham, Aditya Tanikanti, and Murat Keçeli. Chemgraph: An agentic framework for computational chemistry workflows. arXiv preprint arXiv:2506.06363, 2025.
- [263] Can Polat, Mehmet Tuncel, Mustafa Kurban, Erchin Serpedin, and Hasan Kurban. xchemagents: Agentic ai for explainable quantum chemistry. arXiv preprint arXiv:2505.20574, 2025.
- [264] Evangelos Pournaras. Science in the era of chatgpt, large language models and generative ai. KIKritik/AI Critique Volume 6, page 275, 2023.
- [265] Vignesh Prabhakar, Md Amirul Islam, Adam Atanas, Yao-Ting Wang, Joah Han, Aastha Jhunjhunwala, Rucha Apte, Robert Clark, Kang Xu, Zihan Wang, et al. Omniscience: A domain-specialized llm for scientific reasoning and discovery. arXiv preprint arXiv:2503.17604, 2025.
- [266] Yingming Pu, Tao Lin, and Hongyu Chen. Piflow: Principle-aware scientific discovery with multi-agent collaboration. arXiv preprint arXiv:2505.15047, 2025.
- [267] Biqing Qi, Kaiyan Zhang, Haoxiang Li, Kai Tian, Sihang Zeng, Zhang-Ren Chen, and Bowen Zhou. Large language models are zero shot hypothesis proposers. arXiv preprint arXiv:2311.05965, 2023.
- [268] Chen Qian et al. ChatDev: Communicative agents for software development. In Proceedings of the Annual Meeting of the Association for Computational Linguistics, Aug. 2024.
- [269] Shuofei Qiao, Honghao Gui, Chengfei Lv, Qianghuai Jia, Huajun Chen, and Ningyu Zhang. Making language models better tool learners with execution feedback. arXiv preprint arXiv:2305.13068, 2023.
- [270] Shuofei Qiao, Runnan Fang, Ningyu Zhang, Yuqi Zhu, Xiang Chen, Shumin Deng, Yong Jiang, Pengjun Xie, Fei Huang, and Huajun Chen. Agent planning with world knowledge model. 37:114843–114871, 2024.
- [271] Shuofei Qiao, Ningyu Zhang, Runnan Fang, Yujie Luo, Wangchunshu Zhou, Yuchen Eleanor Jiang, Chengfei Lv, and Huajun Chen. Autoact: Automatic agent learning from scratch for qa via self-planning. arXiv preprint arXiv:2401.05268, 2024.
- [272] Zijie Qiu, Jiaqi Wei, Xiang Zhang, Sheng Xu, Kai Zou, Zhi Jin, Zhiqiang Gao, Nanqing Dong, and Siqi Sun. Universal biological sequence reranking for improved de novo peptide sequencing. arXiv preprint arXiv:2505.17552, 2025.
- [273] Shang Qu, Ning Ding, Linhai Xie, Yifei Li, Zaoqu Liu, Kaiyan Zhang, Yibai Xiong, Yuxin Zuo, Zhangren Chen, Ermo Hua, et al. Automating exploratory multiomics research via language models. arXiv preprint arXiv:2506.07591, 2025.
- [274] Xin Quan, Marco Valentino, Louise A. Dennis, and André Freitas. Verification and refinement of natural language explanations through llm-symbolic theorem proving, 2024. URL https://arxiv. org/abs/2405.01379.


- [275] Gollam Rabby, Diyana Muhammed, Prasenjit Mitra, and Sören Auer. Iterative hypothesis generation for scientific discovery with monte carlo nash equilibrium self-refining trees, 2025. URL https: //arxiv.org/abs/2503.19309.
- [276] Mayk Caldas Ramos, Christopher J Collison, and Andrew D White. A review of large language models and autonomous agents in chemistry. Chemical Science, 2025.
- [277] Roshan M Rao, Jason Liu, Robert Verkuil, Joshua Meier, John Canny, Pieter Abbeel, Tom Sercu, and Alexander Rives. Msa transformer. In International conference on machine learning, pages 8844–8856. PMLR, 2021.
- [278] Shuo Ren, Pu Jian, Zhenjiang Ren, Chunlin Leng, Can Xie, and Jiajun Zhang. Towards scientific intelligence: A survey of llm-based scientific agents. arXiv preprint arXiv:2503.24047, 2025.
- [279] Corban Rivera, Grayson Byrd, William Paul, Tyler Feldman, Meghan Booker, Emma Holmes, David Handelman, Bethany Kemp, Andrew Badger, Aurora Schmidt, et al. Conceptagent: Llm-driven precondition grounding and tree search for robust task planning and execution. arXiv preprint arXiv:2410.06108, 2024.
- [280] Alexander Rives, Joshua Meier, Tom Sercu, Siddharth Goyal, Zeming Lin, et al. Biological structure and function emerge from scaling unsupervised learning to 250 million protein sequences. Proceedings of the National Academy of Sciences, 118(15), 2021.
- [281] Yusuf Roohani, Andrew Lee, Qian Huang, Jian Vora, Zachary Steinhart, Kexin Huang, Alexander Marson, Percy Liang, and Jure Leskovec. Biodiscoveryagent: An ai agent for designing genetic perturbation experiments. arXiv preprint arXiv:2405.17631, 2024.
- [282] Yixiang Ruan, Chenyin Lu, Ning Xu, Yuchen He, Yixin Chen, Jian Zhang, Jun Xuan, Jianzhang Pan, Qun Fang, Hanyu Gao, et al. An automatic end-to-end chemical synthesis development platform powered by large language models. Nature communications, 15(1):10160, 2024.
- [283] Yixiang Ruan, Chenyin Lu, Ning Xu, Jian Zhang, Jun Xuan, Jianzhang Pan, Qun Fang, Hanyu Gao, Xiaodong Shen, Ning Ye, et al. Accelerated end-to-end chemical synthesis development with large language models. doi:10.26434/chemrxiv-2024-6wmg4, 2024.
- [284] Daniel Saeedi, Denise Buckner, Jose C Aponte, and Amirali Aghazadeh. Astroagents: A multi-agent ai for hypothesis generation from mass spectrometry data. arXiv preprint arXiv:2503.23170, 2025.
- [285] Andreas WM Sauter, Erman Acar, and Vincent Francois-Lavet. A meta-reinforcement learning algorithm for causal discovery. In Conference on Causal Learning and Reasoning, pages 602–619. PMLR, 2023.
- [286] Samuel Schmidgall and Michael Moor. Agentrxiv: Towards collaborative autonomous research. arXiv preprint arXiv:2503.18102, 2025.
- [287] Samuel Schmidgall, Yusheng Su, Ze Wang, Ximeng Sun, Jialian Wu, Xiaodong Yu, Jiang Liu, Zicheng Liu, and Emad Barsoum. Agent laboratory: Using llm agents as research assistants. arXiv preprint arXiv:2501.04227, 2025.
- [288] Johannes Schneider. Generative to agentic ai: Survey, conceptualization, and challenges. arXiv preprint arXiv:2504.18875, 2025.


- [289] Andrew Sellergren, Sahar Kazemzadeh, Tiam Jaroensri, Atilla Kiraly, Madeleine Traverse, Timo Kohlberger, Shawn Xu, Fayaz Jamil, Cían Hughes, Charles Lau, et al. Medgemma technical report. arXiv preprint arXiv:2507.05201, 2025.
- [290] SeungWon Seo, Junhyeok Lee, SeongRae Noh, and HyeongYeop Kang. Llm-based cooperative agents using information relevance and plan validation. arXiv preprint arXiv:2405.16751, 2024.
- [291] Haiyang Shen, Yue Li, Desong Meng, Dongqi Cai, Sheng Qi, Li Zhang, Mengwei Xu, and Yun Ma. Shortcutsbench: A large-scale real-world benchmark for api-based agents. In The Thirteenth International Conference on Learning Representations, 2025.
- [292] Zhengliang Shi, Shen Gao, Lingyong Yan, Yue Feng, Xiuyi Chen, Zhumin Chen, Dawei Yin, Suzan Verberne, and Zhaochun Ren. Tool learning in the wild: Empowering language models as automatic tool agents. In Proceedings of the ACM on Web Conference 2025, pages 2222–2237, 2025.
- [293] Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao. Reflexion: Language agents with verbal reinforcement learning. 36:8634–8652, 2023.
- [294] Chenglei Si, Diyi Yang, and Tatsunori Hashimoto. Can llms generate novel research ideas? a large-scale human study with 100+ nlp researchers. arXiv preprint arXiv:2409.04109, 2024.
- [295] Karan Singhal, Tao Tu, Juraj Gottweis, Rory Sayres, Ellery Wulczyn, Le Hou, Kevin Clark, Stephen Pfohl, Heather Cole-Lewis, Darlene Neal, Mike Schaekermann, Amy Wang, Mohamed Amin, Sami Lachgar, Philip Mansfield, Sushant Prakash, Bradley Green, Ewa Dominowska, Blaise Aguera y Arcas, Nenad Tomasev, Yun Liu, Renee Wong, Christopher Semturs, S. Sara Mahdavi, Joelle Barral, Dale Webster, Greg S. Corrado, Yossi Matias, Shekoofeh Azizi, Alan Karthikesalingam, and Vivek Natarajan. Towards expert-level medical question answering with large language models, 2023. URL https: //arxiv.org/abs/2305.09617.
- [296] Khachik Smbatyan, Tsolak Ghukasyan, Tigran Aghajanyan, Hovhannes Dabaghyan, Sergey Adamyan, Aram Bughdaryan, Vahagn Altunyan, Gagik Navasardyan, Aram Davtyan, Anush Hakobyan, et al. Can ai agents design and implement drug discovery pipelines? arXiv preprint arXiv:2504.19912, 2025.
- [297] Michael J Smith, Ryan J Roberts, Eirini Angeloudi, and Marc Huertas-Company. Astropt: Scaling large observation models for astronomy. arXiv preprint arXiv:2405.14930, 2024.
- [298] Tao Song, Man Luo, Linjiang Chen, Yan Huang, Qing Zhu, Daobin Liu, Baicheng Zhang, Gang Zou, Fei Zhang, Weiwei Shang, Jun Jiang, and Yi Luo. A multi-agent-driven robotic ai chemist enabling autonomous chemical research on demand. ChemRxiv, July 2024. doi: 10.26434/chemrxiv-2024-w953h-v2. URL https://chemrxiv.org/engage/chemrxiv/ article-details/66a8c11bc9c6a5c07a7a59c0. Preprint.
- [299] Tao Song, Man Luo, Xiaolong Zhang, Linjiang Chen, Yan Huang, Jiaqi Cao, Qing Zhu, Daobin Liu, Baicheng Zhang, Gang Zou, et al. A multiagent-driven robotic ai chemist enabling autonomous chemical research on demand. Journal of the American Chemical Society, 147(15):12534–12545, 2025.
- [300] Yifan Song, Da Yin, Xiang Yue, Jie Huang, Sujian Li, and Bill Yuchen Lin. Trial and error: Explorationbased trajectory optimization of llm agents. pages 7584–7600, 2024.


- [301] Zhilong Song, Shuaihua Lu, Minggang Ju, Qionghua Zhou, and Jinlan Wang. Is large language model all you need to predict the synthesizability and precursors of crystal structures?, 2024. URL https://arxiv.org/abs/2407.07016.
- [302] Henry W Sprueill, Carl Edwards, Khushbu Agarwal, Mariefel V Olarte, Udishnu Sanyal, Conrad Johnston, Hongbin Liu, Heng Ji, and Sutanay Choudhury. Chemreasoner: Heuristic search over a large language model’s knowledge space using quantum-chemical feedback. arXiv preprint arXiv:2402.10980, 2024.
- [303] Sakhinana Sagar Srinivas, Shivam Gupta, and Venkataramana Runkana. Autochemschematic ai: A closed-loop, physics-aware agentic framework for auto-generating chemical process and instrumentation diagrams. arXiv preprint arXiv:2505.24584, 2025.
- [304] Felix Strieth-Kalthoff, Han Hao, Vandana Rathore, Joshua Derasp, Théophile Gaudin, Nicholas H Angello, Martin Seifrid, Ekaterina Trushina, Mason Guy, Junliang Liu, et al. Delocalized, asynchronous, closed-loop discovery of organic laser emitters. Science, 384(6697):eadk9227, 2024.
- [305] Haoyang Su, Renqi Chen, Shixiang Tang, Zhenfei Yin, Xinzhe Zheng, Jinzhe Li, Biqing Qi, Qi Wu, Hui Li, Wanli Ouyang, Philip Torr, Bowen Zhou, and Nanqing Dong. Many heads are better than one: Improved scientific idea generation by a LLM-based multi-agent system. In Wanxiang Che, Joyce Nabende, Ekaterina Shutova, and Mohammad Taher Pilehvar, editors, Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 28201–28240, Vienna, Austria, July 2025. Association for Computational Linguistics. ISBN 979-8-89176-251-0. URL https://aclanthology.org/2025.acl-long.1368/.
- [306] Houcheng Su, Weicai Long, and Yanlin Zhang. Biomaster: Multi-agent system for automated bioinformatics analysis workflow. bioRxiv, pages 2025–01, 2025.
- [307] Yanzhou Su, Tianbin Li, Jiyao Liu, Chenglong Ma, Junzhi Ning, Cheng Tang, Sibo Ju, Jin Ye, Pengcheng Chen, Ming Hu, et al. Gmai-vl-r1: Harnessing reinforcement learning for multimodal medical reasoning. arXiv preprint arXiv:2504.01886, 2025.
- [308] Haotian Sun, Yuchen Zhuang, Lingkai Kong, Bo Dai, and Chao Zhang. Adaplanner: Adaptive planning from feedback with language models. 36:58202–58245, 2023.
- [309] Jiankai Sun, Chuanyang Zheng, Enze Xie, Zhengying Liu, Ruihang Chu, Jianing Qiu, Jiaqi Xu, Mingyu Ding, Hongyang Li, Mengzhe Geng, et al. A survey of reasoning with foundation models: Concepts, methodologies, and outlook. ACM Computing Surveys, 57(11):1–43, 2025.
- [310] Liangtai Sun, Danyu Luo, Da Ma, Zihan Zhao, Baocai Chen, Zhennan Shen, Su Zhu, Lu Chen, Xin Chen, and Kai Yu. Scidfm: A large language model with mixture-of-experts for science. arXiv preprint arXiv:2409.18412, 2024.
- [311] Zechang Sun, Yuan-Sen Ting, Yaobo Liang, Nan Duan, Song Huang, and Zheng Cai. Interpreting multiband galaxy observations with large language model-based agents. arXiv preprint arXiv:2409.14807, 2024.
- [312] Mirac Suzgun and Adam Tauman Kalai. Meta-prompting: Enhancing language models with taskagnostic scaffolding. arXiv preprint arXiv:2401.12954, 2024.
- [313] Kyle Swanson, Wesley Wu, Nash L Bulaong, John E Pak, and James Zou. The virtual lab: Ai agents design new sars-cov-2 nanobodies with experimental validation. bioRxiv, pages 2024–11, 2024.


- [314] Nathan J Szymanski, Bernardus Rendy, Yuxing Fei, Rishi E Kumar, Tanjin He, David Milsted, Matthew J McDermott, Max Gallant, Ekin Dogus Cubuk, Amil Merchant, et al. An autonomous laboratory for the accelerated synthesis of novel materials. Nature, 624(7990):86–91, 2023.
- [315] Pratiksha Tadas and Sudhir Agarmore. Redefining Work in the Age of AI: Challenges and Pathways to Opportunities. In SPICES, pages 1–5. IEEE, 2024.
- [316] Shiro Takagi, Ryutaro Yamauchi, and Wataru Kumagai. Towards autonomous hypothesis verification via language models with minimal guidance, 2023. URL https://arxiv.org/abs/2311.09706.
- [317] Qian Tan, Dongzhan Zhou, Peng Xia, Wanhao Liu, Wanli Ouyang, Lei Bai, Yuqiang Li, and Tianfan Fu. Chemmllm: Chemical multimodal large language model. arXiv preprint arXiv:2505.16326, 2025.
- [318] Xiangru Tang, Tianyu Hu, Muyang Ye, Yanjun Shao, Xunjian Yin, Siru Ouyang, Wangchunshu Zhou, Pan Lu, Zhuosheng Zhang, Yilun Zhao, et al. Chemagent: Self-updating library in large language models improves chemical reasoning. arXiv preprint arXiv:2501.06590, 2025.
- [319] Xiangru Tang et al. MedAgents: Large language models as collaborators for zero-shot medical reasoning. In Findings of the Association for Computational Linguistics, Aug. 2024.
- [320] Mingxu Tao, Dongyan Zhao, and Yansong Feng. Chain-of-discussion: A multi-model framework for complex evidence-based question answering. arXiv preprint arXiv:2402.16313, 2024.
- [321] Ross Taylor, Marcin Kardas, Guillem Cucurull, Thomas Scialom, Anthony Hartshorn, Elvis Saravia, Andrew Poulton, Viktor Kerkez, and Robert Stojnic. Galactica: A large language model for science. arXiv preprint arXiv:2211.09085, 2022.
- [322] Kimi Team, Angang Du, Bofei Gao, Bowei Xing, Changjiu Jiang, Cheng Chen, Cheng Li, Chenjun Xiao, Chenzhuang Du, Chonghua Liao, et al. Kimi k1. 5: Scaling reinforcement learning with llms. arXiv preprint arXiv:2501.12599, 2025.
- [323] NovelSeek Team, Bo Zhang, Shiyang Feng, Xiangchao Yan, Jiakang Yuan, Zhiyin Yu, Xiaohan He, Songtao Huang, Shaowei Hou, Zheng Nie, et al. Novelseek: When agent becomes the scientist–building closed-loop system from hypothesis to verification. arXiv preprint arXiv:2505.16938, 2025.
- [324] David Thulke, Yingbo Gao, Petrus Pelser, Rein Brune, Rricha Jalota, Floris Fok, Michael Ramos, Ian van Wyk, Abdallah Nasir, Hayden Goldstein, et al. Climategpt: Towards ai synthesizing interdisciplinary research on climate change. arXiv preprint arXiv:2401.09646, 2024.
- [325] Chuan Tian et al. Optimizing collaboration of large language model based agents for autonomous finite element analysis. 2025.
- [326] Jie Tian, Martin Taylor Sobczak, Dhanush Patil, Jixin Hou, Lin Pang, Arunachalam Ramanathan, Libin Yang, Xianyan Chen, Yuval Golan, Xiaoming Zhai, et al. A multi-agent framework integrating large language models and generative ai for accelerated metamaterial design. arXiv preprint arXiv:2503.19889, 2025.
- [327] Minyang Tian, Luyu Gao, Shizhuo Dylan Zhang, Xinan Chen, Cunwei Fan, Xuefei Guo, Roland Haas, Pan Ji, Kittithat Krongchon, Yao Li, Shengyan Liu, Di Luo, Yutao Ma, Hao Tong, Kha Trinh, Chenyu Tian, Zihan Wang, Bohao Wu, Yanyu Xiong, Shengzhu Yin, Minhui Zhu, Kilian Lieret, Yanxin Lu, Genglin Liu, Yufeng Du, Tianhua Tao, Ofir Press, Jamie Callan, Eliu Huerta, and Hao Peng. Scicode: A research coding benchmark curated by scientists, 2024. URL https://arxiv.org/abs/2407.13168.


- [328] Yuanhe Tian, Ruyi Gan, Yan Song, Jiaxing Zhang, and Yongdong Zhang. Chimed-gpt: A chinese medical large language model with full training regime and better alignment to human preferences. arXiv preprint arXiv:2311.06025, 2023.
- [329] Emanuel Todorov, Tom Erez, and Yuval Tassa. Mujoco: A physics engine for model-based control. In 2012 IEEE/RSJ International Conference on Intelligent Robots and Systems, pages 5026–5033. IEEE,

2012. doi: 10.1109/IROS.2012.6386109.

- [330] Augustin Toma, Patrick R Lawler, Jimmy Ba, Rahul G Krishnan, Barry B Rubin, and Bo Wang. Clinical camel: An open expert-level medical language model with dialogue-based knowledge encoding. arXiv preprint arXiv:2305.12031, 2023.
- [331] Khanh-Tung Tran, Dung Dao, Minh-Duong Nguyen, Quoc-Viet Pham, Barry O’Sullivan, and Hoang D Nguyen. Multi-agent collaboration mechanisms: A survey of llms. arXiv preprint arXiv:2501.06322, 2025.
- [332] Harsh Trivedi, Niranjan Balasubramanian, Tushar Khot, and Ashish Sabharwal. Interleaving retrieval with chain-of-thought reasoning for knowledge-intensive multi-step questions. arXiv preprint arXiv:2212.10509, 2022.
- [333] Laura van Weesep, Samuel Genheden, Ola Engkvist, and Jens Sjölund. Exploring modularity of agentic systems for drug discovery. arXiv preprint arXiv:2506.22189, 2025.
- [334] Guangya Wan, Yuqi Wu, Jie Chen, and Sheng Li. Dynamic self-consistency: Leveraging reasoning paths for efficient llm sampling. arXiv preprint arXiv:2408.17017, 2024.
- [335] Bingning Wang, Haizhou Zhao, Huozhi Zhou, Liang Song, Mingyu Xu, Wei Cheng, Xiangrong Zeng, Yupeng Zhang, Yuqi Huo, Zecheng Wang, et al. Baichuan-m1: Pushing the medical capability of large language models. arXiv preprint arXiv:2502.12671, 2025.
- [336] Chao Wang, Hehe Fan, Ruijie Quan, and Yi Yang. Protchatgpt: Towards understanding proteins with large language models. arXiv preprint, 2024. doi: 10.48550/arXiv.2402.09649. v2, 2025.
- [337] Cunshi Wang, Xinjie Hu, Yu Zhang, Xunhao Chen, Pengliang Du, Yiming Mao, Rui Wang, Yuyang Li, Ying Wu, Hang Yang, et al. Starwhisper telescope: Agent-based observation assistant system to approach ai astrophysicist. arXiv preprint arXiv:2412.06412, 2024.
- [338] Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, and Anima Anandkumar. Voyager: An open-ended embodied agent with large language models. 2023.
- [339] Hanchen Wang, Yichun He, Paula P Coelho, Matthew Bucci, Abbas Nazir, Bob Chen, Linh Trinh, Serena Zhang, Kexin Huang, Vineethkrishna Chandrasekar, et al. Spatialagent: An autonomous ai agent for spatial biology. bioRxiv, pages 2025–04, 2025.
- [340] Haoran Wang, Pingzhi Li, Min Chen, Jinglei Cheng, Junyu Liu, and Tianlong Chen. Grovergpt: A large language model with 8 billion parameters for quantum searching. arXiv preprint arXiv:2501.00135, 2024.
- [341] Kun Wang, Guibin Zhang, Zhenhong Zhou, Jiahao Wu, Miao Yu, Shiqian Zhao, Chenlong Yin, Jinhu Fu, Yibo Yan, Hanjun Luo, et al. A comprehensive survey in llm (-agent) full stack safety: Data, training and deployment. arXiv preprint arXiv:2504.15585, 2025.


- [342] Lei Wang, Wanyu Xu, Yihuai Lan, Zhiqiang Hu, Yunshi Lan, Roy Ka-Wei Lee, and Ee-Peng Lim. Plan-and-solve prompting: Improving zero-shot chain-of-thought reasoning by large language models. arXiv preprint arXiv:2305.04091, 2023.
- [343] Qineng Wang, Zihao Wang, Ying Su, Hanghang Tong, and Yangqiu Song. Rethinking the bounds of llm reasoning: Are multi-agent discussions the key? arXiv preprint arXiv:2402.18272, 2024.
- [344] Sheng Wang, Yuzhi Guo, Yuhong Wang, Hongmao Sun, and Junzhou Huang. Smiles-bert: Large scale unsupervised pre-training for molecular property prediction. In Proceedings of the 10th ACM International Conference on Bioinformatics, Computational Biology and Health Informatics, BCB ’19, page 429–436, New York, NY, USA, 2019. Association for Computing Machinery. ISBN 9781450366663. doi: 10.1145/3307339.3342186. URL https://doi.org/10.1145/3307339.3342186.
- [345] Wenxuan Wang, Zizhan Ma, Zheng Wang, Chenghan Wu, Jiaming Ji, Wenting Chen, Xiang Li, and Yixuan Yuan. A survey of llm-based agents in medicine: How far are we from baymax? arXiv preprint arXiv:2502.11211, 2025.
- [346] Xidong Wang, Nuo Chen, Junyin Chen, Yan Hu, Yidong Wang, Xiangbo Wu, Anningzhe Gao, Xiang Wan, Haizhou Li, and Benyou Wang. Apollo: Lightweight multilingual medical llms towards democratizing medical ai to 6b people, 2024.
- [347] Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery, and Denny Zhou. Self-consistency improves chain of thought reasoning in language models. arXiv preprint arXiv:2203.11171, 2022.
- [348] Yi Wang, Yuejie Hou, Lin Yang, Shisen Li, Weiting Tang, Hui Tang, Qiushun He, Siyuan Lin, Yanyan Zhang, Xingyu Li, et al. Accelerating primer design for amplicon sequencing using large language model-powered agents. Nature Biomedical Engineering, pages 1–16, 2025.
- [349] Zhizheng Wang, Qiao Jin, Chih-Hsuan Wei, Shubo Tian, Po-Ting Lai, Qingqing Zhu, Chi-Ping Day, Christina Ross, and Zhiyong Lu. Geneagent: Self-verification language agent for gene set knowledge discovery using domain databases. arXiv preprint arXiv:2405.16205, 2024.
- [350] Zilong Wang, Hao Zhang, Chun-Liang Li, Julian Martin Eisenschlos, Vincent Perot, Zifeng Wang, Lesly Miculicich, Yasuhisa Fujii, Jingbo Shang, Chen-Yu Lee, and Tomas Pfister. Chain-of-table: Evolving tables in the reasoning chain for table understanding, 2024. URL https://arxiv.org/abs/2401. 04398.
- [351] Zirui Wang, Mengzhou Xia, Luxi He, Howard Chen, Yitao Liu, Richard Zhu, Kaiqu Liang, Xindi Wu, Haotian Liu, Sadhika Malladi, Alexis Chevalier, Sanjeev Arora, and Danqi Chen. Charxiv: Charting gaps in realistic chart understanding in multimodal llms, 2024. URL https://arxiv.org/abs/ 2406.18521.
- [352] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou, et al. Chain-of-thought prompting elicits reasoning in large language models. 35:24824–24837, 2022.
- [353] Jiaqi Wei, Bin Jiang, and Yanxia Zhang. Identification of blue horizontal branch stars with multimodal fusion. Publications of the Astronomical Society of the Pacific, 135(1050):084501, 2023.
- [354] Jiaqi Wei, Hao Zhou, Xiang Zhang, Di Zhang, Zijie Qiu, Wei Wei, Jinzhe Li, Wanli Ouyang, and Siqi Sun. Alignrag: Leveraging critique learning for evidence-sensitive retrieval-augmented reasoning. arXiv preprint arXiv:2504.14858, 2025.


- [355] Bo Wen, Wen-Feng Zeng, Yuxing Liao, Zhiao Shi, Sara R Savage, Wen Jiang, and Bing Zhang. Deep learning in proteomics. Proteomics, 20(21-22):1900335, 2020.
- [356] Yixuan Weng, Minjun Zhu, Guangsheng Bao, Hongbo Zhang, Jindong Wang, Yue Zhang, and Linyi Yang. Cycleresearcher: Improving automated research via automated review. In The Thirteenth International Conference on Learning Representations, 2025. URL https://openreview.net/ forum?id=bjcsVLoHYs.
- [357] Chaoyi Wu, Weixiong Lin, Xiaoman Zhang, Ya Zhang, Yanfeng Wang, and Weidi Xie. Pmc-llama: Towards building open-source language models for medicine, 2023. URL https://arxiv.org/ abs/2304.14454.
- [358] Mengsong Wu, YaFei Wang, Yidong Ming, Yuqi An, Yuwei Wan, Wenliang Chen, Binbin Lin, Yuqiang Li, Tong Xie, and Dongzhan Zhou. Chemagent: Enhancing llms for chemistry and materials science through tree-search based tool learning. arXiv preprint arXiv:2506.07551, 2025.
- [359] Qingyun Wu, Gagan Bansal, Jieyu Zhang, Yiran Wu, Beibin Li, Erkang Zhu, Li Jiang, Xiaoyun Zhang, Shaokun Zhang, Jiale Liu, Ahmed Hassan Awadallah, Ryen W White, Doug Burger, and Chi Wang. Autogen: Enabling next-gen llm applications via multi-agent conversation, 2023.
- [360] Qingyun Wu et al. Autogen: Enabling next-gen LLM applications via multi-agent conversation, 2024.
- [361] Shengguang Wu, Keming Lu, Benfeng Xu, Junyang Lin, Qi Su, and Chang Zhou. Self-evolved diverse data sampling for efficient instruction tuning. arXiv preprint arXiv:2311.08182, 2023.
- [362] xAI. Grok 4, 2025. URL https://x.ai/news/grok-4.
- [363] Yingce Xia, Peiran Jin, Shufang Xie, Liang He, Chuan Cao, Renqian Luo, Guoqing Liu, Yue Wang, Zequn Liu, Yuan-Jyue Chen, et al. Nature language model: Deciphering the language of nature for scientific discovery. arXiv preprint arXiv:2502.07527, 2025.
- [364] Yanzheng Xiang, Hanqi Yan, Shuyin Ouyang, Lin Gui, and Yulan He. Scireplicate-bench: Benchmarking llms in agent-driven algorithmic reproduction from research papers. arXiv preprint arXiv:2504.00255, 2025.
- [365] Yanzheng Xiang, Hanqi Yan, Shuyin Ouyang, Lin Gui, and Yulan He. Scireplicate-bench: Benchmarking llms in agent-driven algorithmic reproduction from research papers, 2025. URL https://arxiv. org/abs/2504.00255.
- [366] Meng Xiao, Xunxin Cai, Qingqing Long, Chengrui Wang, Yuanchun Zhou, and Hengshu Zhu. m-kailin: Knowledge-driven agentic scientific corpus distillation framework for biomedical large language models training. arXiv preprint arXiv:2504.19565, 2025.
- [367] Yihang Xiao, Jinyi Liu, Yan Zheng, Xiaohan Xie, Jianye Hao, Mingzhi Li, Ruitao Wang, Fei Ni, Yuxiao Li, Jintian Luo, et al. Cellagent: An llm-driven multi-agent framework for automated single-cell data analysis. bioRxiv, pages 2024–05, 2024.
- [368] Yijia Xiao, Edward Sun, Yiqiao Jin, Qifan Wang, and Wei Wang. Proteingpt: Multimodal llm for protein property prediction and structure understanding. arXiv preprint, 2024. doi: 10.48550/arXiv. 2408.11363. v2, 2025.


- [369] Junlin Xie, Zhihong Chen, Ruifei Zhang, Xiang Wan, and Guanbin Li. Large multimodal agents: A survey. arXiv preprint arXiv:2402.15116, 2024.
- [370] Qianqian Xie, Qingyu Chen, Aokun Chen, Cheng Peng, Yan Hu, Fongci Lin, Xueqing Peng, Jimin Huang, Jeffrey Zhang, Vipina Keloth, Xinyu Zhou, Lingfei Qian, Huan He, Dennis Shung, Lucila Ohno-Machado, Yonghui Wu, Hua Xu, and Jiang Bian. Me llama: Foundation large language models for medical applications, 2024. URL https://arxiv.org/abs/2402.12749.
- [371] Qiujie Xie, Yixuan Weng, Minjun Zhu, Fuchen Shen, Shulin Huang, Zhen Lin, Jiahui Zhou, Zilan Mao, Zijie Yang, Linyi Yang, et al. How far are ai scientists from changing the world? arXiv preprint arXiv:2507.23276, 2025.
- [372] Tong Xie, Yuwei Wan, Wei Huang, Zhenyu Yin, Yixuan Liu, Shaozhou Wang, Qingyuan Linghu, Chunyu Kit, Clara Grazian, Wenjie Zhang, et al. Darwin series: Domain specific large language models for natural science. arXiv preprint arXiv:2308.13565, 2023.
- [373] Qi Xin, Quyu Kong, Hongyi Ji, Yue Shen, Yuqi Liu, Yan Sun, Zhilin Zhang, Zhaorong Li, Xunlong Xia, Bing Deng, et al. Bioinformatics agent (bia): Unleashing the power of large language models to reshape bioinformatics workflow. bioRxiv, pages 2024–05, 2024.
- [374] Kai Xiong et al. Examining inter-consistency of large language models collaboration: An in-depth analysis via debate. In Findings of the Association for Computational Linguistics: EMNLP 2023, Dec. 2023.
- [375] Hanwen Xu and Sheng Wang. Protranslator: Zero-shot protein function prediction using textual description. arXiv preprint, 2022. doi: 10.48550/arXiv.2204.10286.
- [376] Hanwen Xu, Addie Woicik, Russ B. Altman, Hoifung Poon, and Sheng Wang. Multilingual translation for zero-shot biomedical classification using biotranslator. Nature Communications, 14, 2023. doi: 10.1038/s41467-023-36476-2. URL https://www.nature.com/articles/ s41467-023-36476-2.
- [377] Huihui Xu, Yuanpeng Nie, Hualiang Wang, Ying Chen, Wei Li, Junzhi Ning, Lihao Liu, Hongqiu Wang, Lei Zhu, Jiyao Liu, et al. Medground-r1: Advancing medical image grounding via spatial-semantic rewarded group relative policy optimization. arXiv preprint arXiv:2507.02994, 2025.
- [378] Wujiang Xu, Kai Mei, Hang Gao, Juntao Tan, Zujie Liang, and Yongfeng Zhang. A-mem: Agentic memory for llm agents. arXiv preprint arXiv:2502.12110, 2025.
- [379] Yinggan Xu, Hana Kimlee, Yijia Xiao, and Di Luo. Advancing ai-scientist understanding: Making llm think like a physicist with interpretable reasoning, 2025. URL https://arxiv.org/abs/2504. 01911.
- [380] Zhaoqian Xue, Beichen Wang, Suiyuan Zhu, Kai Mei, Hua Tang, Wenyue Hua, Mengnan Du, and Yongfeng Zhang. What if llms have different world views: Simulating alien civilizations with llm-based agents. arXiv preprint arXiv:2402.13184, 2024.
- [381] Yutaro Yamada, Robert Tjarko Lange, Cong Lu, Shengran Hu, Chris Lu, Jakob Foerster, Jeff Clune, and David Ha. The ai scientist-v2: Workshop-level automated scientific discovery via agentic tree search. arXiv preprint arXiv:2504.08066, 2025.


- [382] Keqiang Yan, Yi Liu, Yuchao Lin, and Shuiwang Ji. Periodic graph transformers for crystal material property prediction. Advances in Neural Information Processing Systems, 35:15066–15080, 2022.
- [383] Keqiang Yan, Cong Fu, Xiaofeng Qian, Xiaoning Qian, and Shuiwang Ji. Complete and efficient graph transformers for crystal material property prediction. arXiv preprint arXiv:2403.11857, 2024.
- [384] Siyuan Yan, Ming Hu, Yiwen Jiang, Xieji Li, Hao Fei, Philipp Tschandl, Harald Kittler, and Zongyuan Ge. Derm1m: A million-scale vision-language dataset aligned with clinical ontology knowledge for dermatology. arXiv preprint arXiv:2503.14911, 2025.
- [385] An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao, Chengen Huang, Chenxu Lv, et al. Qwen3 technical report. arXiv preprint arXiv:2505.09388, 2025.
- [386] Han Yang, Chenxi Hu, Yichi Zhou, Xixian Liu, Yu Shi, Jielan Li, Guanzhi Li, Zekun Chen, Shuizhou Chen, Claudio Zeni, et al. Mattersim: A deep learning atomistic model across elements, temperatures and pressures. arXiv preprint arXiv:2405.04967, 2024.
- [387] Junwei Yang, Hanwen Xu, Srbuhi Mirzoyan, Tong Chen, Zixuan Liu, Zequn Liu, Wei Ju, Luchen Liu, Zhiping Xiao, Ming Zhang, et al. Poisoning medical knowledge using large language models. Nature Machine Intelligence, 6(10):1156–1168, 2024.
- [388] Kevin Yang, Dan Klein, Asli Celikyilmaz, Nanyun Peng, and Yuandong Tian. Rlcd: Reinforcement learning from contrastive distillation for lm alignment. 2024.
- [389] Rui Yang, Lin Song, Yanwei Li, Sijie Zhao, Yixiao Ge, Xiu Li, and Ying Shan. Gpt4tools: Teaching large language model to use tools via self-instruction. 36:71995–72007, 2023.
- [390] Songhua Yang, Hanjie Zhao, Senbin Zhu, Guangyu Zhou, Hongfei Xu, Yuxiang Jia, and Hongying Zan. Zhongjing: Enhancing the chinese medical capabilities of large language model through expert feedback and real-world multi-turn dialogue. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 38, pages 19368–19376, 2024.
- [391] Yaotian Yang, Yiwen Tang, Yizhe Chen, Xiao Chen, Jiangjie Qiu, Hao Xiong, Haoyu Yin, Zhiyao Luo, Yifei Zhang, Sijia Tao, et al. Automat: Enabling automated crystal structure reconstruction from microscopy via agentic tool use. arXiv preprint arXiv:2505.12650, 2025.
- [392] Zhenyu Yang, Xiaoxi Zeng, Yi Zhao, and Runsheng Chen. Alphafold2 and its applications in the fields of biology and medicine. Signal Transduction and Targeted Therapy, 8(1):115, 2023.
- [393] Zonglin Yang, Xinya Du, Junxian Li, Jie Zheng, Soujanya Poria, and Erik Cambria. Large language models for automated open-domain scientific hypotheses discovery. arXiv preprint arXiv:2309.02726, 2023.
- [394] Zonglin Yang, Xinya Du, Junxian Li, Jie Zheng, Soujanya Poria, and Erik Cambria. Large language models for automated open-domain scientific hypotheses discovery. In Findings of the Association for Computational Linguistics ACL 2024, pages 13545–13565, 2024.
- [395] Zonglin Yang, Wanhao Liu, Ben Gao, Tong Xie, Yuqiang Li, Wanli Ouyang, Soujanya Poria, Erik Cambria, and Dongzhan Zhou. Moose-chem: Large language models for rediscovering unseen chemistry scientific hypotheses. arXiv preprint arXiv:2410.07076, 2024.


- [396] Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao. React: Synergizing reasoning and acting in language models. 2023.
- [397] Nicolas Yax, Hernán Anlló, and Stefano Palminteri. Studying and improving reasoning in humans and machines. Communications Psychology, 2(1):51, 2024.
- [398] Asaf Yehudai, Lilach Eden, Alan Li, Guy Uziel, Yilun Zhao, Roy Bar-Haim, Arman Cohan, and Michal Shmueli-Scheuer. Survey on evaluation of llm-based agents. arXiv preprint arXiv:2503.16416, 2025.
- [399] Zhangyue Yin et al. Exchange-of-thought: Enhancing large language model capabilities through cross-model communication. In Houda Bouamor, Juan Pino, and Kalika Bali, editors, Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, pages 15135–15153, Singapore, December 2023. Association for Computational Linguistics.
- [400] Naruki Yoshikawa, Marta Skreta, Kourosh Darvish, Sebastian Arellano-Rubach, Zhi Ji, Lasse Bjørn Kristensen, Andrew Zou Li, Yuchi Zhao, Haoping Xu, Artur Kuramshin, Alán Aspuru-Guzik, Florian Shkurti, and Animesh Garg. Large language models for chemistry robotics. Autonomous Robots, 47: 1057–1086, 2023. doi: 10.1007/s10514-023-10136-2. URL https://link.springer.com/ article/10.1007/s10514-023-10136-2.
- [401] Botao Yu, Frazier N Baker, Ziru Chen, Garrett Herb, Boyu Gou, Daniel Adu-Ampratwum, Xia Ning, and Huan Sun. Chemtoolagent: The impact of tools on language agents for chemistry problem solving. arXiv preprint arXiv:2411.07228, 2024.
- [402] Miao Yu, Fanci Meng, Xinyun Zhou, Shilong Wang, Junyuan Mao, Linsey Pan, Tianlong Chen, Kun Wang, Xinfeng Li, Yongfeng Zhang, et al. A survey on trustworthy llm agents: Threats and countermeasures. In Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V. 2, pages 6216–6226, 2025.
- [403] Chaohao Yuan, Songyou Li, Geyan Ye, Yikun Zhang, Long-Kai Huang, Wenbing Huang, Wei Liu, Jianhua Yao, and Yu Rong. Annotation-guided protein design with multi-level domain alignment. arXiv preprint, 2024.
- [404] Jiakang Yuan, Xiangchao Yan, Botian Shi, Tao Chen, Wanli Ouyang, Bo Zhang, Lei Bai, Yu Qiao, and Bowen Zhou. Dolphin: Closed-loop open-ended auto-research through thinking, practice, and feedback. arXiv e-prints, pages arXiv–2501, 2025.
- [405] Siyu Yuan, Kaitao Song, Jiangjie Chen, Xu Tan, Yongliang Shen, Ren Kan, Dongsheng Li, and Deqing Yang. Easytool: Enhancing llm-based agents with concise tool instruction. arXiv preprint arXiv:2401.06201, 2024.
- [406] Weizhe Yuan, Richard Yuanzhe Pang, Kyunghyun Cho, Xian Li, Sainbayar Sukhbaatar, Jing Xu, and Jason Weston. Self-rewarding language models, 2024.
- [407] Ling Yue, Nithin Somasekharan, Yadi Cao, and Shaowu Pan. Foam-agent: Towards automated intelligent cfd workflows. arXiv preprint arXiv:2505.04997, 2025.
- [408] Fatemeh Pesaran Zadeh, Juyeon Kim, Jin-Hwa Kim, and Gunhee Kim. Text2chart31: Instruction tuning for chart generation with automatic feedback, 2025. URL https://arxiv.org/abs/2410. 04064.


- [409] Sharaf Zaman, Michael J Smith, Pranav Khetarpal, Rishabh Chakrabarty, Michele Ginolfi, Marc Huertas-Company, Maja Jabłońska, Sandor Kruk, Matthieu Le Lain, Sergio José Rodríguez Méndez, et al. Astrollava: towards the unification of astronomical data and natural language. arXiv preprint arXiv:2504.08583, 2025.
- [410] Eric Zelikman, YH Wu, Jesse Mu, and Noah D Goodman. Star: Self-taught reasoner bootstrapping reasoning with reasoning. volume 1126, 2024.
- [411] Shenglai Zeng, Jiankun Zhang, Pengfei He, Yue Xing, Yiding Liu, Han Xu, Jie Ren, Shuaiqiang Wang, Dawei Yin, Yi Chang, et al. The good and the bad: Exploring privacy issues in retrieval-augmented generation (rag). arXiv preprint arXiv:2402.16893, 2024.
- [412] Claudio Zeni, Robert Pinsler, Daniel Zügner, Andrew Fowler, Matthew Horton, Xiang Fu, Zilong Wang, Aliaksandra Shysheya, Jonathan Crabbé, Shoko Ueda, et al. A generative model for inorganic materials design. Nature, 639(8055):624–632, 2025.
- [413] Baohua Zhang, Xin Li, Huangchao Xu, Zhong Jin, Quansheng Wu, and Ce Li. Topomas: Large language model driven topological materials multiagent system. arXiv preprint arXiv:2507.04053, 2025.
- [414] Ceyao Zhang, Kaijie Yang, Siyi Hu, Zihao Wang, Guanghe Li, Yihang Sun, Cheng Zhang, Zhaowei Zhang, Anji Liu, Song-Chun Zhu, et al. Proagent: building proactive cooperative agents with large language models. volume 38, pages 17591–17599, 2024.
- [415] Dan Zhang, Ziniu Hu, Sining Zhoubian, Zhengxiao Du, Kaiyu Yang, Zihan Wang, Yisong Yue, Yuxiao Dong, and Jie Tang. Sciglm: Training scientific language models with self-reflective instruction annotation and tuning. arXiv preprint arXiv:2401.07950, 2024.
- [416] Dan Zhang, Sining Zhoubian, Ziniu Hu, Yisong Yue, Yuxiao Dong, and Jie Tang. Rest-mcts*: Llm self-training via process reward guided tree search. 37:64735–64772, 2024.
- [417] Di Zhang, Wei Liu, Qian Tan, Jingdan Chen, Hang Yan, Yuliang Yan, Jiatong Li, Weiran Huang, Xiangyu Yue, Wanli Ouyang, et al. Chemllm: A chemical large language model. arXiv preprint arXiv:2402.06852, 2024.
- [418] Guorui Zhang, Chao Song, Liyuan Liu, Qiuyu Wang, and Chunquan Li. Transagent: Dynamizing transcriptional regulation analysis via multi-omics-aware ai agent. bioRxiv, pages 2025–04, 2025.
- [419] Haotian Zhang, Yu H Sun, Wenxing Hu, Xu Cui, Zhengyu Ouyang, Derrick Cheng, Xinmin Zhang, and Baohong Zhang. Compbioagent: An llm-powered agent for single-cell rna-seq data exploration. bioRxiv, pages 2025–03, 2025.
- [420] Haoxuan Zhang, Ruochi Li, Yang Zhang, Ting Xiao, Jiangping Chen, Junhua Ding, and Haihua Chen. The evolving role of large language models in scientific innovation: Evaluator, collaborator, and scientist. arXiv preprint arXiv:2507.11810, 2025.
- [421] Hongbo Zhang, Junying Chen, Feng Jiang, Fei Yu, Zhihong Chen, Jianquan Li, Guiming Chen, Xiangbo Wu, Zhiyi Zhang, Qingying Xiao, Xiang Wan, Benyou Wang, and Haizhou Li. Huatuogpt, towards taming language models to be a doctor. arXiv preprint arXiv:2305.15075, 2023.


- [422] Huan Zhang, Yu Song, Ziyu Hou, Santiago Miret, and Bang Liu. HoneyComb: A flexible LLMbased agent system for materials science. In Yaser Al-Onaizan, Mohit Bansal, and Yun-Nung Chen, editors, Findings of the Association for Computational Linguistics: EMNLP 2024, pages 3369–3382, Miami, Florida, USA, nov 2024. Association for Computational Linguistics. doi: 10.18653/v1/2024. findings-emnlp.192. URL https://aclanthology.org/2024.findings-emnlp.192/.
- [423] Huan Zhang, Yu Song, Ziyu Hou, Santiago Miret, and Bang Liu. Honeycomb: A flexible llm-based agent system for materials science. arXiv preprint arXiv:2409.00135, 2024.
- [424] Jian Zhang, Zhiyuan Wang, Zhangqi Wang, Xinyu Zhang, Fangzhi Xu, Qika Lin, Rui Mao, Erik Cambria, and Jun Liu. Maps: A multi-agent framework based on big seven personality and socratic guidance for multimodal scientific problem solving. arXiv preprint arXiv:2503.16905, 2025.
- [425] Jiayi Zhang, Jinyu Xiang, Zhaoyang Yu, Fengwei Teng, Xiong-Hui Chen, Jiaqi Chen, Mingchen Zhuge, Xin Cheng, Sirui Hong, Jinlin Wang, Bang Liu, Yuyu Luo, and Chenglin Wu. AFlow: Automating agentic workflow generation. 2025.
- [426] Jintian Zhang et al. Exploring collaboration mechanisms for LLM agents: A social psychology view. In Proceedings of the Annual Meeting of the Association for Computational Linguistics, Aug. 2024.
- [427] Qiang Zhang, Keyan Ding, Tianwen Lv, Xinda Wang, Qingyu Yin, Yiwen Zhang, Jing Yu, Yuhao Wang, Xiaotong Li, Zhuoyi Xiang, et al. Scientific large language models: A survey on biological & chemical domains. ACM Computing Surveys, 57(6):1–38, 2025.
- [428] Xiang Zhang, Juntai Cao, Jiaqi Wei, Chenyu You, and Dujian Ding. Why prompt design matters and works: A complexity analysis of prompt search space in llms. arXiv preprint arXiv:2503.10084, 2025.
- [429] Xiang Zhang, Tianze Ling, Zhi Jin, Sheng Xu, Zhiqiang Gao, Boyan Sun, Zijie Qiu, Jiaqi Wei, Nanqing Dong, Guangshuai Wang, et al. π-primenovo: an accurate and efficient non-autoregressive deep learning model for de novo peptide sequencing. Nature Communications, 16(1):267, 2025.
- [430] Xiang Zhang, Jiaqi Wei, Zijie Qiu, Sheng Xu, Nanqing Dong, Zhiqiang Gao, and Siqi Sun. Curriculum learning for biological sequence prediction: The case of de novo peptide sequencing. arXiv preprint arXiv:2506.13485, 2025.
- [431] Xiang Zhang, Jiaqi Wei, Zijie Qiu, Sheng Xu, Zhi Jin, ZhiQiang Gao, Nanqing Dong, and Siqi Sun. Bidirectional representations augmented autoregressive biological sequence generation: Application in de novo peptide sequencing. arXiv preprint arXiv:2510.08169, 2025.
- [432] Xiang Zhang, Jiaqi Wei, Zijie Qiu, Sheng Xu, Zhi Jin, ZhiQiang Gao, Nanqing Dong, and Siqi Sun. Bidirectional representations augmented autoregressive biological sequence generation:application in de novo peptide sequencing, 2025. URL https://arxiv.org/abs/2510.08169.
- [433] Xiaowen Zhang, Zhenyu Bi, Xuan Wang, Tiziana Di Matteo, and Rupert AC Croft. Bridging literature and the universe via a multi-agent large language model system. arXiv preprint arXiv:2507.08958, 2025.
- [434] Yuan-Hang Zhang and Massimiliano Di Ventra. Transformer quantum state: A multipurpose model for quantum many-body problems. Physical Review B, 107(7):075147, 2023.


- [435] Yue Zhang, Yafu Li, Leyang Cui, Deng Cai, Lemao Liu, Tingchen Fu, Xinting Huang, Enbo Zhao, Yu Zhang, Yulong Chen, et al. Siren’s song in the ai ocean: A survey on hallucination in large language models. Computational Linguistics, pages 1–45, 2025.
- [436] Zhengde Zhang, Yiyu Zhang, Haodong Yao, Jianwen Luo, Rui Zhao, Bo Huang, Jiameng Zhao, Yipu Liao, Ke Li, Lina Zhao, et al. Xiwu: A basis flexible and learnable llm for high energy physics. arXiv preprint arXiv:2404.08001, 2024.
- [437] Zhongyue Zhang, Zijie Qiu, Yingcheng Wu, Shuya Li, Dingyan Wang, Zhuomin Zhou, Duo An, Yuhan Chen, Yu Li, Yongbo Wang, et al. Origene: A self-evolving virtual disease biologist automating therapeutic target discovery. bioRxiv, pages 2025–06, 2025.
- [438] Andrew Zhao, Daniel Huang, Quentin Xu, Matthieu Lin, Yong-Jin Liu, and Gao Huang. Expel: Llm agents are experiential learners. pages 19632–19642, 2024.
- [439] Fuyong Zhao, Yuyang Li, Yanhao Wang, Hui Li, Mei Chen, Panfeng Chen, Ningchen Sun, Cunshi Wang, and Jifeng Liu. Pulsar candidate classification with multimodal large language models. In Neurips 2024 Workshop Foundation Models for Science: Progress, Opportunities, and Challenges, 2024. URL https://openreview.net/forum?id=8SKgWpZiDL.
- [440] Zihan Zhao, Da Ma, Lu Chen, Liangtai Sun, Zihao Li, Yi Xia, Bo Chen, Hongshen Xu, Zichen Zhu, Su Zhu, et al. Chemdfm: a large language foundation model for chemistry. arXiv preprint arXiv:2401.14818, 2024.
- [441] Tianshi Zheng, Zheye Deng, Hong Ting Tsang, Weiqi Wang, Jiaxin Bai, Zihao Wang, and Yangqiu Song. From automation to autonomy: A survey on large language models in scientific discovery. arXiv preprint arXiv:2505.13259, 2025.
- [442] Qihuang Zhong, Liang Ding, Juhua Liu, Bo Du, and Dacheng Tao. Self-evolution learning for discriminative language model pretraining. pages 4130–4145, 2023.
- [443] Tianyang Zhong, Zhengliang Liu, Yi Pan, Yutong Zhang, Yifan Zhou, Shizhe Liang, Zihao Wu, Yanjun Lyu, Peng Shu, Xiaowei Yu, et al. Evaluation of openai o1: Opportunities and challenges of agi. arXiv preprint arXiv:2409.18486, 2024.
- [444] Lianhao Zhou, Hongyi Ling, Keqiang Yan, Kaiji Zhao, Xiaoning Qian, Raymundo Arróyave, Xiaofeng Qian, and Shuiwang Ji. Toward greater autonomy in materials discovery agents: Unifying planning, physics, and scientists. arXiv preprint arXiv:2506.05616, 2025.
- [445] Wangchunshu Zhou, Yixin Ou, Shengwei Ding, Long Li, Jialong Wu, Tiannan Wang, Jiamin Chen, Shuai Wang, Xiaohua Xu, Ningyu Zhang, et al. Symbolic learning enables self-evolving agents. arXiv preprint arXiv:2406.18532, 2024.
- [446] Xibin Zhou, Chenchen Han, Yingqi Zhang, Jin Su, Kai Zhuang, Shiyu Jiang, Zichen Yuan, Wei Zheng, Fengyuan Dai, Yuyang Zhou, et al. Decoding the molecular language of proteins with evolla. bioRxiv, pages 2025–01, 2025.
- [447] Yuhao Zhou, Yiheng Wang, Xuming He, Ruoyao Xiao, Zhiwei Li, Qiantai Feng, Zijie Guo, Yuejin Yang, Hao Wu, Wenxuan Huang, et al. Scientists’ first exam: Probing cognitive abilities of mllm via perception, understanding, and reasoning. arXiv preprint arXiv:2506.10521, 2025.


- [448] Zekun Zhou, Xiaocheng Feng, Lei Huang, Xiachong Feng, Ziyun Song, Ruihan Chen, Liang Zhao, Weitao Ma, Yuxuan Gu, Baoxin Wang, et al. From hypothesis to publication: A comprehensive survey of ai-driven research support systems. arXiv preprint arXiv:2503.01424, 2025.
- [449] Zhenhong Zhou, Zherui Li, Jie Zhang, Yuanhe Zhang, Kun Wang, Yang Liu, and Qing Guo. Corba: Contagious recursive blocking attacks on multi-agent systems based on large language models. arXiv preprint arXiv:2502.14529, 2025.
- [450] Max Zhu, Adrián Bazaga, and Pietro Liò. Fluid-llm: Learning computational fluid dynamics with spatiotemporal-aware large language models. arXiv preprint arXiv:2406.04501, 2024.
- [451] Pengyu Zhu, Zhenhong Zhou, Yuanhe Zhang, Shilinlu Yan, Kun Wang, and Sen Su. Demonagent: Dynamically encrypted multi-backdoor implantation attack on llm-based agent. arXiv preprint arXiv:2502.12575, 2025.
- [452] Yinghao Zhu, Yifan Qi, Zixiang Wang, Lei Gu, Dehao Sui, Haoran Hu, Xichen Zhang, Ziyi He, Liantao Ma, and Lequan Yu. Healthflow: A self-evolving ai agent with meta planning for autonomous healthcare research. arXiv preprint arXiv:2508.02621, 2025.
- [453] Yuqi Zhu, Shuofei Qiao, Yixin Ou, Shumin Deng, Ningyu Zhang, Shiwei Lyu, Yue Shen, Lei Liang, Jinjie Gu, and Huajun Chen. Knowagent: Knowledge-augmented planning for llm-based agents. arXiv preprint arXiv:2403.03101, 2024.
- [454] Xiang Zhuang, Keyan Ding, Tianwen Lyu, Yinuo Jiang, Xiaotong Li, Zhuoyi Xiang, Zeyuan Wang, Ming Qin, Kehua Feng, Jike Wang, et al. Advancing biomolecular understanding and design following human instructions. Nature Machine Intelligence, pages 1–14, 2025.
- [455] Yunheng Zou, Austin H. Cheng, Abdulrahman Aldossary, Jiaru Bai, Shi Xuan Leong, Jorge Arturo Campos-Gonzalez-Angulo, Changhyeok Choi, Cher Tian Ser, Gary Tom, Andrew Wang, Zijian Zhang, Ilya Yakavets, Han Hao, Chris Crebolder, Varinia Bernales, and Alán Aspuru-Guzik. El Agente: An Autonomous Agent for Quantum Chemistry. arXiv e-prints, art. arXiv:2505.02484, May 2025. doi: 10.48550/arXiv.2505.02484.


