# arXiv:2603.19782v1[cs.AI]20 Mar 2026

## Embodied Science: Closing the Discovery Loop with Agentic Embodied AI

### Xiang Zhuang1,2, Chenyi Zhou1, Kehua Feng1, Zhihui Zhu1, Yunfan Gao3, Yijie Zhong3, Yichi Zhang1, Junjie Huang1, Keyan Ding1 , Lei Bai2 , Haofen Wang3 , Qiang Zhang1 , and Huajun Chen1

1Zhejiang University, Hangzhou, China 2Shanghai Artificial Intelligence Laboratory, Shanghai, China 3Tongji University, Shanghai, China

baisanshi@gmail.com, haofen.wang@tongji.edu.cn, {dingkeyan,qiang.zhang.cs,huajunsir}@zju.edu.cn

### ABSTRACT

Artificial intelligence has demonstrated remarkable capability in predicting scientific properties, yet scientific discovery remains an inherently physical, long-horizon pursuit governed by experimental cycles. Most current computational approaches are misaligned with this reality, framing discovery as isolated, task-specific predictions rather than continuous interaction with the physical world. Here, we argue for embodied science, a paradigm that reframes scientific discovery as a closed loop tightly coupling agentic reasoning with physical execution. We propose a unified Perception–Language–Action–Discovery (PLAD) framework, wherein embodied agents perceive experimental environments, reason over scientific knowledge, execute physical interventions, and internalize outcomes to drive subsequent exploration. By grounding computational reasoning in robust physical feedback, this approach bridges the gap between digital prediction and empirical validation, offering a roadmap for autonomous discovery systems in the life and chemical sciences.

### 1 Introduction

Artificial intelligence is reshaping how scientific knowledge is produced and acted upon1. Over the past decade, data-driven models have delivered striking advances in problems once considered intractable, from accurate protein structure prediction2,3 to learned models for molecular property prediction4–6, generative design7,8, and synthesis planning9. These successes, together with the rise of foundation models that unify representations across modalities10–12, have begun to shift AI for Science (AI4S) from a collection of specialized predictors toward more general-purpose scientific engines13.

Yet a central tension remains: scientific discovery is not a single-shot inference problem. Breakthroughs typically emerge from long-horizon, iterative interaction with the physical world, through a sustained loop of hypothesis formation, experimental design, execution under real constraints, analysis, and model revision14,15. Even when a predictive model is excellent, the discovery process can stall if the system cannot decide what to do next, cannot perceive the signals from instruments, or cannot reliably translate decisions into executable laboratory operations.

Recent efforts make this mismatch visible in the form of a bifurcated landscape. On one side, large language model (LLM)-based agents16–20 expand cognitive scope through language-mediated reasoning, planning, and tool use, often translating high-level scientific intent into experimental plans, code, and workflows. On the other side, automated and robotic laboratories21,22 demonstrate reliable embodied execution, enabling sustained experimentation and closed-loop optimization within well-defined experimental spaces. This split reflects broader empirical evidence that AI’s currently attributed scientific impact remains concentrated in cognitive augmentation, especially in data processing and pattern recognition, whereas the next critical step is to expand sensory and experimental capacity to enable the search for and acquisition of new forms of evidence beyond “standing” datasets23. Crucially, this split is not an incidental integration gap that will vanish by “connecting” modules. Each line optimizes a different

|Human-orchestrated, AI-assisted scientific discovery|
|---|


|Long-horizon autonomous scientific discovery|
|---|


![image 1](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile1.png)

![image 2](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile2.png)

![image 3](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile3.png)

![image 4](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile4.png)

![image 5](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile5.png)

![image 6](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile6.png)

![image 7](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile7.png)

![image 8](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile8.png)

![image 9](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile9.png)

![image 10](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile10.png)

![image 11](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile11.png)

![image 12](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile12.png)

Reasoning Planning

![image 13](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile13.png)

![image 14](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile14.png)

![image 15](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile15.png)

![image 16](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile16.png)

![image 17](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile17.png)

Reflecting ...

#### …

Scientific data from instruments Scientific cognition

Dataset Source

Design Training AI Model

Data Collection Model Training

Perception

Language

![image 18](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile18.png)

![image 19](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile19.png)

Experiments Prediction

Discovery

Action

![image 20](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile20.png)

![image 21](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile21.png)

![image 22](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile22.png)

![image 23](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile23.png)

![image 24](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile24.png)

![image 25](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile25.png)

![image 26](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile26.png)

![image 27](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile27.png)

![image 28](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile28.png)

![image 29](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile29.png)

![image 30](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile30.png)

![image 31](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile31.png)

![image 32](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile32.png)

![image 33](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile33.png)

![image 34](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile34.png)

![image 35](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile35.png)

![image 36](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile36.png)

![image 37](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile37.png)

![image 38](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile38.png)

![image 39](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile39.png)

![image 40](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile40.png)

![image 41](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile41.png)

![image 42](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile42.png)

![image 43](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile43.png)

![image 44](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile44.png)

![image 45](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile45.png)

![image 46](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile46.png)

![image 47](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile47.png)

![image 48](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile48.png)

![image 49](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile49.png)

![image 50](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile50.png)

![image 51](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile51.png)

![image 52](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile52.png)

![image 53](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile53.png)

![image 54](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile54.png)

![image 55](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile55.png)

![image 56](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile56.png)

![image 57](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile57.png)

![image 58](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile58.png)

![image 59](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile59.png)

Output Instruments Analysis

Input AI model Output

Internalize outcomes as insight Embodied execution

Disembodied AI assistant Agentic embodied AI

![image 60](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile60.png)

![image 61](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile61.png)

![image 62](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile62.png)

![image 63](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile63.png)

![image 64](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile64.png)

Prediction-centric AI for science

Embodied science

- Figure 1. From prediction-centric AI for science to embodied science. Left: the dominant AI4S workflow is human-orchestrated. Experts curate data sources into datasets, train task-specific models, and use predictions to inform the next experimental step; execution remains human-managed, yielding a loosely coupled loop across stages. Right: embodied science reframes discovery as a closed-loop process interaction with the physical world. Agentic embodied AI provides the enabling system layer that operationalizes this paradigm by integrating Perception


– Language – Action – Discovery (PLAD): it grounds cognition in instrument-derived evidence (Perception), conducts reasoning and planning (Language), carries out embodied experimentation (Action), and internalizes outcomes into scientific insight (Discovery). The system can sustain long-horizon autonomous scientific discovery, executing iterative cycles beyond task-bounded, single-shot assistance.

projection of discovery under the prevailing framing: cognition is powerful but weakly grounded in instrument-level evidence and physical constraints, whereas execution is robust but often optimized around predefined objectives and procedural boundaries. Without reframing discovery as an end-to-end closed loop, incremental scaling (such as stronger planners, better robots, or larger models) tends to reproduce fragmentation rather than resolve it.

Thus, autonomy in scientific discovery is a property of the coupled system, and realizing the capacity expansion required for continued exploration23 collapses when any of the three structural requirements is externalized: perception, cognition, and action. At the level of perception, scientific evidence is generated by instruments, not datasets: raw spectra, chromatograms, microscopy streams, sensor logs, calibration traces, and meta-data that capture drift, failure, and context. Models trained on curated tables often lack the ability to parse these multimodal, imperfect signals and to perform goal-directed sensing (e.g., adaptively zoom, re-measure, recalibrate, or switch modalities when anomalies occur). At the level of cognition, most AI4S systems optimize well-defined tasks (predict a structure, rank candidates, regress a property), but long-horizon discovery requires persistent goal management, experimental reasoning under uncertainty, and planning over contingencies and costs24. It demands not only selecting the next experiment, but also deciding what to measure, when to intervene, and how to revise hypotheses as evidence accumulates. At the level of action, discovery hinges on interventions in the world25. Many AI4S pipelines terminate at candidate suggestions, while real laboratories require precise, verifiable actions: manipulating reagents, configuring instruments, executing protocols, ensuring safety constraints, and recovering from errors. Without robust action grounding, “recommendations” cannot mature into discoveries.

Here, we argue for embodied science as a foundational paradigm for long-horizon autonomous discovery. In embodied science, AI does not merely analyze data or recommend actions; it expands sensory and experimental capacity by participating directly in experimental workflows as part of a closed loop that couples perception of instrument signals, knowledge-grounded reasoning, and physical intervention. Scientific progress, under this paradigm, emerges from continuous engagement with real experimental environments rather than from one-off computation over static datasets. This perspective reframes AI-driven discovery as an exploration-driven process, in which hypotheses, experimental strategies, and operational behaviors co-evolve through repeated interaction with the physical world.

### 2 Scoping Embodied Science and Agentic Embodied AI

AI-driven discovery is transitioning from tool-based augmentation to system-level reconfiguration of the scientific method. To avoid terminology drift, we scope two concepts that organize this Perspective, Embodied Science and Agentic Embodied AI, and we define long-horizon autonomous scientific discovery as the operational outcome they aim to enable.

- 2.1 Embodied Science Definition. We use Embodied Science to denote a paradigm in which discovery is treated as an embodied, longhorizon, closed-loop process. AI is integrated into real experimental workflows and operates across the complete cycle of discovery by perceiving instrument-generated signals, reasoning with scientific knowledge, and executing laboratory interventions. Scientific progress therefore arises from sustained interaction with the physical world, rather than from isolated computation over static datasets.

Why embodiment matters in scientific exploration. Embodiment, in this view, is not laboratory automation in disguise. It is what makes AI-driven discovery actionable: plans are realized as physical interventions in the laboratory, and their consequences are returned as instrument-grounded feedback. Rather than mechanically executing fixed protocols, embodied capabilities enable systems to carry intent into the real world, observe what actually happens, and adapt subsequent decisions accordingly.

- 2.2 Agentic Embodied AI Embodied Science defines what kind of discovery process is needed; Agentic Embodied AI specifies what kind of AI system can realize it.

Definition. Agentic Embodied AI is a persistent cyber–physical scientific agent that couples (i) scientific cognition, (ii) experimental perception, and (iii) laboratory action within a single closed-loop controller, operating under explicit feasibility and safety constraints.

Three properties are essential: (1) Agentic autonomy: the ability to manage goals over extended horizons, plan under uncertainty and cost, and revise strategies in response to outcomes; (2) Embodiment in the experimental loop: interfaces to raw instrument streams, operational state, and actuation primitives to ground reasoning in laboratory reality; (3) Long-horizon persistence: memory, provenance, monitoring, and recovery behaviors that maintain continuity across cycles rather than treating each run as a standalone episode.

- 2.3 Long-Horizon Autonomous Scientific Discovery Because “autonomy” is often used loosely, we adopt an operational criterion:


Operational criterion. A system demonstrates long-horizon autonomous discovery if it can sustain multiple

end-to-end discovery cycles—hypothesis → experiment design → physical execution → interpretation → revisionover extended time spans with minimal human intervention, while maintaining reproducibility, provenance, and safety. This criterion sets a higher bar than most current demonstrations: it requires the loop to remain closed beyond a single episode, sustaining autonomous operation across instrument drift, stochastic outcomes, and accumulating uncertainty, while preserving reproducibility, provenance, and safety.

### 3 Analyzing the Current Landscape: Reasoning-Centric and Execution-Centric Paradigms

Motivated by the need to bridge computational reasoning and physical experimentation, scientific agents and embodied AI have recently emerged as promising routes toward more autonomous scientific discovery. In practice, however, existing efforts have largely bifurcated into two partial realizations: reasoning-centric systems that advance hypothesis generation and in silico exploration, and execution-centric platforms that enable autonomous, highthroughput experimentation within well-defined procedural boundaries. Each excels at a single component of the discovery process while remaining fundamentally decoupled from the others. Below, we analyze the current landscape and argue that these limitations are structural rather than incremental.

- 3.1 Disembodied Scientific Cognition: Reasoning without Physical Action Artificial intelligence has long supported scientific research through data-driven modeling and prediction, a trajectory often associated with the Fourth Paradigm of data-intensive science26. In recent years, this role has expanded toward cognition-centric scientific agents that aim to elevate AI from a passive analytical tool to an active reasoning entity.

- As summarized in Table 1, these approaches are unified by a common paradigm: they operate primarily on curated datasets, emphasize language-based scientific reasoning, and remain physically disembodied, with experimental execution and validation performed by humans.


Within this paradigm, a first subclass focuses on task decomposition and planning. Systems such as ChemCrow27, Biomni28, SciToolAgent29, and ToolUniverse30 leverage large language models to orchestrate domain-specific tools, dynamically assembling workflows for synthesis planning, reaction optimization, or biomedical analysis. Their strength lies in structuring complex scientific tasks and coordinating heterogeneous computational resources. However, their operational boundary is fundamentally cognitive: experimental actions are abstracted as tool calls, and physical execution remains external. A second subclass emphasizes hypothesis generation and problem-space exploration. Platforms such as Virtual Lab31, Robin32, and AI Co-scientist33 aim to emulate aspects of collaborative scientific reasoning by coordinating evidence gathering, hypothesis refinement, and iterative discussion across specified research problems. These systems move beyond task execution toward exploratory inquiry, yet their exploration remains confined to literature, databases, and simulations. Hypotheses are evaluated through manual evaluation by human experts rather than autonomous experimental falsification, leaving the core scientific loop incomplete. A third line of work frames discovery as iterative search and optimization in silico. Systems such as AlphaEvolve34, DeepScientist35 and InternAgent36,37 formalize scientific progress as a feedback-driven process in which hypotheses or programs are iteratively refined based on computational evaluation. While this paradigm introduces an explicit notion of iteration and feedback, the feedback signal is constrained to the execution of computational algorithms. Lacking physical embodiment and the ability to interact with the material world, these systems struggle to generalize across broader scientific domains, often producing candidates that fail to translate into physical experimental success. Finally, some efforts toward end-to-end research in silico, exemplified by systems such as AI Scientist38 and Kosmos39, extend cognition-centric agents to include automated manuscript writing and reporting. Although these systems appear to close the research loop across problem formulation, methodological design, experimental execution, and writing, their scope remains confined to computational domains. Without physical embodiment, they remain incapable of engaging with tangible experimental environments, leaving the loop fundamentally decoupled from the complexities of the material world.

Despite their diversity, reasoning-centric scientific agents share a fundamental structural limitation. Without embodied execution in real experimental environments, hypotheses cannot be autonomously tested, falsified, or revised through sustained interaction with the physical world. Feedback is indirect, delayed, or entirely computational, leading to a form of cognitive closure in which reasoning saturates without experimental grounding. Consequently, these approaches struggle to support long-horizon autonomous scientific discovery, which requires repeated, embodied cycles of hypothesis testing and revision.

- 3.2 Execution-Centric Embodiment: Action without Scientific Understanding In parallel with advances in cognition-centric scientific agents, embodied automation has made substantial progress toward the physical execution of experiments47. As characterized in Table 1, execution-centric embodied systems


Table 1. Landscape of current AI4S approaches toward autonomous scientific discovery. Existing efforts cluster into two partial realizations: reasoning-centric but physically disembodied systems, and execution-centric but cognitively shallow platforms. Notably, neither paradigm achieves a sustained coupling between language-level scientific reasoning and embodied experimental action.

Paradigm Characteristics Subtypes Example approaches

- • Strong language-based reasoning, but no coupling to embodied action;
- • Operate primarily on curated datasets rather than raw signals from instruments;
- • Remain physically disembodied, with experimental execution carried out by human scientists.


e.g., ChemCrow27; Biomni28; SciToolAgent29; ToolUniverse30

Task decomposition & planning

Language-heavy, action-light (physically disembodied)16,17

e.g., Virtual Lab31; Robin32; AI Co-scientist33

Hypothesis & problem exploration

e.g., AlphaEvolve34; DeepScientist35; InternAgent36,37

Iterative search & optimization in silico

e.g., AI Scientist38; Kosmos39

End-to-end research in silico

- • Reliable embodied execution, but limited language-level reasoning and hypothesis formation;
- • Operate directly on raw instrument signals using heuristic decision-making (e.g., Bayesian optimization);
- • Enable autonomous execution within narrow task scopes and fixed procedural boundaries.


Single-step, instrument-bound

e.g., automated liquid handlers; robotic pipetting and weighing systems

Action-heavy, language-light (cognitively shallow)21,22

e.g., Chemputer40; FLUID41

Multi-step, protocoldriven automation

e.g., A-Lab42 RoboChem43; CRESt44

Closed-loop execution and optimization

e.g., Coscientist45; ChemAgents46

Language-instructed experimental execution

operate on raw instrument signals, rely primarily on heuristic or statistical decision-making, and enable direct interaction with the physical world. However, these systems are typically cognitively shallow: while they excel at executing experiments, they lack the capacity for mechanism-aware reasoning and hypothesis-driven inquiry.

At one end of the execution-centric spectrum are single-step, instrument-bound systems. Automated liquid handlers, robotic pipetting platforms, and weighing systems exemplify this class. They automate isolated experimental operations with high precision and repeatability, yet each action is executed independently of the broader scientific context. Consequently, these systems constitute the basic infrastructure of automated experimentation: they robustly perform prescribed single-step actions, yet lack the capacity to analyze outcomes, reason about experimental context, or adapt behavior beyond explicit instructions. A more advanced, yet still execution-bound subclass extends automation to multi-step, protocol-driven execution. Platforms such as the Chemputer40 and FLUID40 encode experimental procedures as machine-executable workflows, enabling the automated realization of complex, multi-stage protocols. Compared to single-step systems, this approach extends automation from isolated actions to coordinated, multi-stage experimental execution. Although execution now spans multiple stages, the system does not analyze intermediate outcomes, reason about experimental context, or deviate from the prescribed workflow when unexpected results occur. At the most integrated end of execution-centric systems are closed-loop, feedback-driven platforms, including A-Lab42, RoboChem43, and CRESt44. By integrating robotic execution with online characterization and statistical optimization methods, including Bayesian optimization and evolutionary search, these platforms demonstrate impressive autonomy over extended experimental campaigns, adapting parameters in response to observed outcomes and achieving local optimization in high-dimensional spaces. However, the closed loop operates primarily at the level of numerical feedback rather than scientific representation. When experiments fail or yield anomalous results, adaptation proceeds through parameter adjustment rather than counterfactual reasoning or

hypothesis revision. With the introduction of large language models, robotic systems have begun to blur the boundary between execution-centric automation and cognitive planning, using LLMs to design experimental workflows and drive embodied laboratory systems for physical execution45,46. Despite this progress, LLM integration primarily improves the flexibility of workflow design and control, without conferring sustained, long-horizon scientific agency. Experimental outcomes are used to refine individual tasks, leading to episodic, task-bounded reasoning rather than cumulative, discovery-driven iteration.

Despite increasing integration, execution-centric systems face two persistent limitations at the level of embodiment. First, most platforms rely on fixed or rail-mounted manipulators tightly coupled to predefined laboratory layouts, which provide reliability but limit physical flexibility across heterogeneous instruments and reconfigurable environments. Second, the development, calibration, and maintenance of such systems remain labor-intensive, requiring substantial human effort to debug workflows and adapt execution logic to new experimental settings. To alleviate these constraints, execution-centric autonomy has been extended through mobile embodiments and digital twin–based simulation. Mobile robotics48,49 address the limitation of rigid embodiment by physically interconnecting spatially distributed instruments, thereby expanding the scope of executable workflows beyond fixed workcells. In parallel, digital twin frameworks such as MATTERIX50 target the engineering bottleneck by enabling virtual validation and sim-to-real transfer51, reducing the cost and risk associated with deploying automated experimental workflows. However, both advances operate strictly at the level of execution. They improve flexibility and reliability in how experiments are carried out, but do not enable systems to interpret experimental outcomes, revise scientific hypotheses, or engage in mechanism-aware reasoning. In this sense, mobile robots and digital twins address execution bottlenecks, not scientific cognition.

Consequently, execution-centric embodied systems often function as powerful execution engines rather than as scientists. Their decision-making is guided by predefined objective functions and fixed parameter spaces, limiting their ability to generalize beyond narrowly scoped tasks. Although they may achieve efficient optimization within constrained domains, they do not accumulate transferable scientific insight. Experimentation is treated as a process of executing and scoring trials, rather than as an active inquiry in which hypotheses are formulated, challenged, and revised. This gap between action and understanding gives rise to an illusion of scientific progress: local performance improves, yet discovery remains decoupled from scientific understanding.

- 3.3 Why Incremental Scaling Is Insufficient The limitations above do not disappear by scaling one side. More powerful language reasoning does not automatically yield procedural correctness, instrument awareness, or safe execution. More capable robotics does not automatically yield hypothesis-driven inquiry, evidence integration, or scientific generalization. Long-horizon autonomy requires a unified system-level coupling between perception, language-level reasoning, embodied action, and cumulative discovery52,53. This motivates a closed-loop framework that treats autonomy as an end-to-end property rather than a component upgrade.
- 4 PLAD: Towards Closed-Loop Agentic Embodied AI for Scientific Discovery


We argue that agentic embodied AI represents a critical technological pathway toward long-horizon autonomous scientific discovery. To this end, we propose the Perception–Language–Action–Discovery (PLAD) closed-loop paradigm (Figure 2) as an overarching framework for implementation. Unlike the Vision–Language–Action (VLA)54 paradigm that underpins general-purpose embodied intelligence, where the primary objective is to understand open environments, generate linguistic descriptions, and execute physical actions. PLAD is explicitly centered on scientific discovery as its core goal. Accordingly, its design is aligned with the distinctive requirements of scientific research across cognitive structures, perceptual targets, and forms of action.

Within PLAD, scientific discovery is modeled as a continuously operating closed-loop process. An agent perceives the experimental environment (Perception), reasons and plans under the support of scientific language and knowledge (Language), executes experiments through embodied actions in real laboratory settings (Action), and internalizes experimental outcomes as new scientific insights (Discovery), which in turn drive subsequent rounds of exploration. Below, we introduce each component of the PLAD paradigm in detail.

###### Reasoning with Models, Knowledge, and Tools

Embodied Execution in Physical World

· Stationary Manipulator · Linear Track Manipulator

· Specialized Knowledge ↓

![image 65](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile65.png)

![image 66](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile66.png)

![image 67](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile67.png)

![image 68](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile68.png)

![image 69](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile69.png)

![image 70](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile70.png)

![image 71](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile71.png)

![image 72](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile72.png)

![image 73](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile73.png)

![image 74](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile74.png)

Scientific Brain

General Large Language Model

Paper Sci-KG Database

![image 75](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile75.png)

grounds & bounds invokes & orchestrates

· Humanoid Robots · Mobile Manipulator

![image 76](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile76.png)

![image 77](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile77.png)

![image 78](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile78.png)

![image 79](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile79.png)

![image 80](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile80.png)

|Long-h|orizon|
|---|---|
|Autono Scientific|mous Discovery|


###### · Specialized Tools ↓

![image 81](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile81.png)

![image 82](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile82.png)

![image 83](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile83.png)

… …

Web search

Database query

Model execution

Spatially Constrained: Autonomy Spatially Unconstrained: Flexibility

![image 84](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile84.png)

· Instrument-mediated Physical Observables ↓

![image 85](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile85.png)

![image 86](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile86.png)

![image 87](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile87.png)

![image 88](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile88.png)

![image 89](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile89.png)

…

…

![image 90](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile90.png)

Exploration question New insight

Spectral measurements

Microscopy images

Cryo-EM outputs

![image 91](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile91.png)

![image 92](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile92.png)

![image 93](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile93.png)

![image 94](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile94.png)

![image 95](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile95.png)

![image 96](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile96.png)

![image 97](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile97.png)

![image 98](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile98.png)

· Instrument-defined Experimental States ↓

· Cumulative scientific knowledge ↓

… …

…

… …

…

Enzyme function

Reaction pathway

Material property

Drug Activity

Equipment status

Electronic lab notebook

Laboratory information systems

Progress states

Instruments as Extensions of Scientific Senses Internalizing Outcomes as Scientific Insight

- Figure 2. The PLAD loop for long-horizon autonolous scientific discovery. Perception transforms raw instrument signals into structured evidence. Language integrates foundation models with specialized knowledge and tools to support hypothesis formation, reasoning, and experimental planning. Action compiles plans into verifiable laboratory operations. Discovery internalizes outcomes into transferable scientific knowledge that shapes subsequent exploration across cycles.


- 4.1 Perception: Instruments as Extensions of Scientific Senses Perception characterizes an agent’s capacity to sense the scientific environment through instruments that extend the limits of human perception. In embodied science, instruments do not merely record data; they function as artificial scientific senses, defining what aspects of the physical world are observable and how experimental information is structured. Scientific perception comprises two complementary forms of instrument sensing.


First, instruments provide instrument-mediated physical observations, through which latent physical phenomena are rendered observable. These include high-dimensional signals such as microscopy images, cryo-electron microscopy reconstructions, spectral measurements, and other modality-specific outputs. Such observations expose structural, dynamical, or compositional properties of experimental systems that are inaccessible to unaided human senses. Second, instruments define instrument-defined experimental states, which encode the operational and procedural context of experimentation. These include progress indicators, equipment status, and structured records maintained in electronic lab notebooks or laboratory information systems. Rather than capturing physical phenomena

directly, these signals formalize the evolving state of an experiment, enabling agents to track execution, detect deviations, and coordinate multi-step workflows. Together, these two forms allow embodied agents to perceive not only what is occurring in an experiment, but also where it resides within the broader scientific process, forming a stable foundation for closed-loop reasoning and action.

##### 4.2 Language: Reasoning with Models, Knowledge, and Tools

Language constitutes the “scientific brain” of an agent, responsible for scientific reasoning, interpretation, and planning. Within PLAD, this component is centered on large language models (LLMs)18,19, understood as a general class of foundation models that encompass multimodal LLMs11,12,55 capable of reasoning over heterogeneous scientific inputs. While LLMs supply general reasoning capability, reliable scientific intelligence cannot emerge from models alone. Instead, it arises from a structured integration of models, specialized knowledge, and task-specific tools, enabling a dynamic balance between generality and specialization.

At the model level, LLMs used for scientific tasks must extend beyond natural language understanding to interpret multimodal scientific inputs produced by perception, including experimental data, instrument outputs, and structured records. In addition, the slow-thinking56 of LLMs enables sustained reasoning over complex instrument data as well as hypothesis inference and experimental planning. Such capacity allows models to integrate heterogeneous evidence, examine intermediate conclusions, and reason counterfactually about alternative explanations, experimental conditions, or mechanistic hypotheses. These requirements motivate a set of science-oriented design considerations. These include modality-aware encoding for spectra, images, and time series; specialized tokenization schemes for chemical, biological, or materials representations; and architectural support for reasoning over long contexts. Training pipelines further benefit from integrating scientific literature with instrument-generated data, enabling LLMs to acquire long chain-of-thought reasoning patterns that align with empirical scientific practice.

Knowledge provides the specialized grounding and constraint that anchors general LLM reasoning in domain reality. Such knowledge spans unstructured scientific literature and structured resources, including databases and scientific knowledge graphs (Sci-KGs)57. Sci-KGs systematically encode scientific concepts and their relationships in the form of triples, integrating structured databases with unstructured textual knowledge to provide a more comprehensive and stable foundation. Moreover, knowledge graphs can incorporate multimodal information, such as omics data, imaging data, and dynamical trajectories from computational simulations, thereby offering rich contextual support for scientific reasoning. Importantly, grounding and constraint are not abstract properties but are operationalized through concrete mechanisms58. During training, structured knowledge can be transformed into reasoning supervision, for example, via knowledge-graph-to-corpus approaches59 that convert graph structure into long-chain scientific reasoning data, yielding high-reliability learning signals. During inference, literature, databases, and knowledge graphs are integrated through retrieval-augmented generation (RAG)60,61, supplying authoritative context that constrains model outputs and stabilizes reasoning under uncertainty. In this way, knowledge injects precision, consistency, and domain depth that general-purpose LLMs alone cannot guarantee.

Tools constitute a second axis of specialization by extending reasoning into executable operations. Through tool invocation, such as web search, database querying, and computational model invocation, LLMs can actively acquire external evidence, perform specialized analyses, and validate intermediate hypotheses. Unlike the general reasoning capacity of LLMs, tools encode expert procedures and formal methods that deliver accuracy and reliability on well-defined scientific tasks, effectively externalizing domain expertise into verifiable operations.

Together, this model–knowledge–tool integration enables a dynamic balance between generality and specialization. General-purpose LLMs provide adaptability, contextual understanding, and analogical reasoning across domains; specialized knowledge and tools deliver precision, depth, and task reliability. Within PLAD, agents dynamically adjust their reliance on these components according to task demands, allowing them to robustly interpret scientific data, perform mechanism-aware reasoning, and plan experiments that are both flexible across domains and dependable within specific scientific contexts.

- 4.3 Action: Embodied Execution in Physical World Action corresponds to the scientific body of an embodied agent and denotes its capacity to intervene in the physical world through experimental execution. In PLAD, action is defined by the agent’s ability to physically manipulate materials, instruments, and experimental processes, thereby grounding scientific reasoning in reality. Embodied execution can be broadly organized along a key dimension: the degree of physical constraint under which an agent operates. Along this axis, embodied forms range from spatially constrained embodiments, which trade autonomy for reliability, to spatially unconstrained embodiments, which prioritize flexibility at the cost of execution certainty.

Spatially constrained embodiments operate within predefined mechanical boundaries and are tightly coupled to laboratory infrastructure, with two representative forms: stationary manipulators and linear track manipulators62. Stationary manipulators are fixed robotic arms deployed at individual experimental stations, automating well-defined manual operations such as dispensing, sample loading or unloading, and instrument handling. Their limited work envelope enables high precision, stability, and repeatability, but also confines them to step-level execution within isolated experimental stages. Linear track manipulators extend this capability by mounting robotic arms on meterscale rails that connect multiple functional stations, such as synthesis and characterization zones. This configuration enables coordinated, multi-step experimental workflows and sustained high-throughput execution under predefined pipelines, significantly expanding experimental coverage while preserving execution reliability. Nevertheless, both forms remain constrained by fixed layouts and preconfigured trajectories, favoring robustness and safety over autonomy and limiting their adaptability to unstructured or rapidly evolving laboratory settings.

In contrast, spatially unconstrained embodiments operate without predefined trajectories or fixed work envelopes. This category includes mobile manipulators, which integrate robotic arms with wheels, as well as humanoid robots48,49. Such embodiments can navigate complex laboratory spaces, transport samples and consumables, and interact with diverse instruments across distributed environments. Their physical freedom enables higher-level autonomy and more closely mimics the behaviors of human researchers. At the same time, this flexibility introduces challenges in motion planning and execution reliability, particularly in safety-critical laboratory settings characterized by dense equipment and intricate procedures.

These two classes of embodiment define complementary regimes of embodied action63,64. Spatially constrained systems provide a stable and reliable foundation for routine experimentation, while spatially unconstrained systems enable flexibility and integration across heterogeneous laboratory contexts. Among the latter, humanoid robots offer a distinctive long-term advantage: by directly operating within human-oriented laboratory layouts, tools, and protocols, they minimize the need for environment reconfiguration and thus represent a promising pathway toward general-purpose laboratory autonomy. Long-horizon autonomous scientific discovery arises from integrating constrained reliability with unconstrained adaptability, with embodied action in PLAD bridging reasoning and sustained physical experimentation.

- 4.4 Discovery: Internalizing Execution Outcomes as Scientific Insight Discovery denotes the process by which an agent internalizes the outcomes of embodied action into scientific insight. Rather than treating experimental results as isolated observations, discovery abstracts execution feedback into transferable scientific understanding. Within PLAD, this process converts exploratory questions into new insights, such as refined interpretations of enzyme function, inferred reaction pathways, or updated structure–property relationships. By feeding these insights back into subsequent reasoning and action, discovery enables the continual refinement of research objectives and supports long-horizon autonomous scientific discovery.
- 4.5 PLAD Examples Using enzyme design and chemical reaction optimization as representative examples, this section illustrates how the PLAD framework can be instantiated across diverse experimental settings (Figure 3). While the underlying scientific questions and experimental modalities differ, PLAD provides a common organizational structure for integrating perception, reasoning, and action into closed-loop discovery processes.


![image 99](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile99.png)

![image 100](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile100.png)

|Language Action<br><br>Perception Discovery<br><br>Structural and functional signals<br><br>· Structural data<br><br>Structure–function hypothesis<br><br>· MD simulation · Structure prediction · Database search<br><br>![image 101](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile101.png)<br><br>![image 102](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile102.png)<br><br>![image 103](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile103.png)<br><br>![image 104](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile104.png)<br><br>![image 105](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile105.png)<br><br>![image 106](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile106.png)<br><br>![image 107](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile107.png)<br><br>![image 108](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile108.png)<br><br>![image 109](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile109.png)<br><br>![image 110](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile110.png)<br><br>![image 111](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile111.png)<br><br>![image 112](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile112.png)<br><br>![image 113](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile113.png)<br><br>![image 114](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile114.png)<br><br>![image 115](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile115.png)<br><br>![image 116](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile116.png)<br><br>![image 117](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile117.png)<br><br>![image 118](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile118.png)<br><br>Active-site mutation<br><br>![image 119](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile119.png)<br><br>Biofoundry-driven mutant generation and screening<br><br>·Mutant library ·Expression ·Purification ·Screening<br><br>Internalized design rules for activity–stability<br><br>Functional mutation<br><br>Silent mutation<br><br>![image 120](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile120.png)<br><br>![image 121](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile121.png)<br><br>![image 122](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile122.png)<br><br>![image 123](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile123.png)<br><br>![image 124](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile124.png)<br><br>L<br><br>A<br><br>D<br><br>P<br><br>![image 125](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile125.png)<br><br>![image 126](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile126.png)<br><br>![image 127](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile127.png)<br><br>![image 128](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile128.png)<br><br>Enzyme Design<br><br>![image 129](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile129.png)<br><br>![image 130](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile130.png)<br><br>|![image 131](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile131.png)|
|---|
<br><br>|![image 132](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile132.png)|
|---|
<br><br>· Functional data · Stability<br><br>metrics<br><br>|![image 133](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile133.png)<br><br>![image 134](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile134.png)<br><br>![image 135](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile135.png)|
|---|
<br><br>![image 136](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile136.png)<br><br>a|
|---|


![image 137](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile137.png)

|Language Action<br><br>Perception Discovery<br><br>Spectroscopic data and reaction trajectories<br><br>Mechanism-driven chemical reasoning Automated reaction execution<br><br>Internalized insight into reaction pathways<br><br>![image 138](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile138.png)<br><br>![image 139](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile139.png)<br><br>![image 140](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile140.png)<br><br>· Spectroscopic<br><br>characterization data<br><br>· Time-resolved<br><br>information<br><br>·Mechanistic reasoning ·Competing pathway inference · Intervention strategy<br><br>·Mobile roboticchemist · Automatedworkstation<br><br>|![image 141](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile141.png)|
|---|
<br><br>![image 142](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile142.png)<br><br>![image 143](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile143.png)<br><br>L<br><br>A<br><br>D<br><br>P<br><br>Chemical Reaction Optimization<br><br>·Competing pathway · Updated rule<br><br>![image 144](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile144.png)<br><br>![image 145](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile145.png)<br><br>![image 146](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile146.png)<br><br>![image 147](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile147.png)<br><br>![image 148](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile148.png)<br><br>![image 149](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile149.png)<br><br>![image 150](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile150.png)<br><br>![image 151](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile151.png)<br><br>![image 152](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile152.png)<br><br>b|
|---|


![image 153](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile153.png)

![image 154](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile154.png)

![image 155](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile155.png)

![image 156](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile156.png)

- Figure 3. Instantiating PLAD in scientific discovery. (a) Enzyme design: Perception integrates structural and functional measurements; Language forms structure–function hypotheses under constraints; Action executes library construction and screening; Discovery internalizes design rules and counterexamples for future cycles. (b) Chemical reaction optimization: Perception tracks spectroscopic and kinetic trajectories; Language performs mechanism-aware reasoning; Action executes targeted campaigns; Discovery internalizes mechanistic explanations and pathway-level constraints that generalize beyond parameter tuning.
- 4.5.1 Enzyme Design In enzyme design, Perception focuses on processing instrument-derived protein structural outputs (e.g., from


![image 157](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile157.png)

![image 158](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile158.png)

cryo-electron microscopy or X-ray crystallography), functional and kinetic measurements (such as Km, kcat, and time-resolved activity profiles), and experimental indicators of stability and expression (including thermal stability, expression levels, and purification yield), among other inputs. Language is centered on constructing hypotheses about enzyme structure–function relationships. It aims to infer which structural changes are likely to drive functional improvements. For example, it must determine whether enhanced activity arises from optimized substrate-binding conformations or from increased global stability, and distinguish whether activity loss results from direct perturbation of the active site or from conformational instability caused by distal mutations. Based on these inferences, it proposes design strategies, such as prioritizing mutations at active-site residues or shifting focus to modifying secondary-structure interfaces to enhance stability. This reasoning process is supported by computational and analytical tools, including protein structure prediction and molecular dynamics simulations to assess how mutations affect conformational stability and dynamics, as well as database queries to examine evolutionary conservation or

homologous variant distributions. Action subsequently translates these reasoning outcomes into concrete, embodied experimental execution. Action is implemented through control of physical experiments, such as generating mutant libraries on a biofoundry and orchestrating high-throughput expression, purification, and activity screening. Through iterative cycles, structure–function hypotheses are tested and refined over extended experimental horizons.

- 4.5.2 Chemical Reaction Optimization In chemical reaction optimization, Perception emphasizes dynamic and process-level signals, including spectroscopic characterization data (such as NMR and IR) as well as time-resolved information, including reaction progress curves and by-product formation trajectories. Together, these signals reflect the temporal evolution of reaction pathways, intermediate states, and operational stability. Language is centered on mechanism-driven chemical reasoning. It focuses on how solvent, additives, and ligand structure modulate key elementary steps, such as oxidative addition, migratory insertion, and reductive elimination. When undesired outcomes arise, such as diminished enantioselectivity or increased by-product formation, the focus shifts from global parameter adjustment to targeted hypothesis refinement. The formation of specific side products may indicate a competing mechanistic pathway, prompting structural modifications or the introduction of additives to suppress or intercept that pathway. This reasoning process is also supported by computational tools, including quantum chemical modeling and kinetic analysis, which are used to assess relative energetics, barrier heights, and selectivity trends under different conditions. Action then translates these into embodied experimental execution. Actions are realized through automated workstations or mobile robotic chemists that execute targeted reaction campaigns, experimentally validating mechanistic hypotheses and suppressing undesired pathways. Through such embodied intervention, mechanism-aware exploration can be sustained across extended experimental cycles.

5 Challenges and Design Considerations

In this section, we identify challenges that constrain the stability, reliability, and safety of long-horizon PLAD loops, and outline corresponding design responses that are necessary to keep such systems operational, cumulative, and trustworthy (Figure 4).

- 5.1 Reasoning over Scientific Data Reasoning over scientific data is fundamental to bridging the gap between Perception and Language. In experiments, perceptual inputs typically manifest as complex, noisy signals, such as liquid chromatography–mass spectrometry (LC–MS) spectra, nuclear magnetic resonance (NMR) and infrared (IR) spectra, time-resolved reaction kinetic profiles, microscopy images, and instrument status logs. Interpretation of these data is deeply contingent on domain-specific knowledge and contextual experimental details. Consider LC–MS data as an illustrative example: a spectrum is not a simple “product fingerprint” but rather the superposition of multiple physicochemical processes, including variations in ionization efficiency, matrix effects, diverse fragmentation pathways, co-elution of isomers, and dynamic changes in signal-to-noise ratio over time. Consequently, the appearance, disappearance, or intensity shift of a peak does not necessarily correlate with reaction progress or the formation of a target compound; accurate interpretation requires integrating retention time, isotopic distribution patterns, fragment ion signatures, and experimental conditions into a coherent assessment. Similarly, scientific instruments characterize reaction through process signals and operational states. Parameters such as temperature, pressure, and flow rate, along with sensor readings or visual cues (e.g., phase transitions or color evolution captured in images), are routinely used to assess whether a reaction has stalled or deviated from its intended trajectory. Such judgments, however, also rely on a deep understanding of the underlying reaction mechanisms and experimental protocols.


Addressing this challenge requires coordinated advances in model design and tool-assisted reasoning. At the architectural level, large language models must be adapted to scientific environments so as to accommodate the structural or temporal properties of experimental data. This enables reasoning to operate directly over instrumentgenerated representations, rather than relying solely on linguistic descriptions. Such science-adapted language models are often described as scientific large language models (Sci-LLMs)11. Even with these adaptations, it is difficult for LLMs to natively cover all dimensions of scientific data analysis. Reliable interpretation also depends on

###### a. Reasoning over Scientific Data b. Embodied Execution Reliability

###### Challenge Resolution

###### Challenge Resolution

Heterogeneous, noisy instrument signals

Sci-LLMs with tool-grounded interpretation

Heterogeneous physical embodiments

Digital Twin

Modality-aware encoding of raw scientific signals

![image 159](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile159.png)

![image 160](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile160.png)

![image 161](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile161.png)

![image 162](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile162.png)

![image 163](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile163.png)

![image 164](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile164.png)

![image 165](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile165.png)

![image 166](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile166.png)

![image 167](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile167.png)

Signals Structural/Temporal Encoding

simulation & trajectory learning

High-precision, safety-critical execution

Tool-based, precise, and verifiable analysis

![image 168](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile168.png)

![image 169](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile169.png)

![image 170](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile170.png)

![image 171](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile171.png)

![image 172](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile172.png)

![image 173](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile173.png)

![image 174](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile174.png)

![image 175](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile175.png)

Interpretation requires a mechanistic understanding

![image 176](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile176.png)

Sci-LLM Tools

Sim-to-real transfer

###### c. Long-Horizon Knowledge Accumulation

Challenge Resolution

Knowledge struggles to accumulate beyond local updates

Experimental memory is fragmented across cycles

Knowledge graph for outcome-to-knowledge internalization

![image 177](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile177.png)

![image 178](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile178.png)

Experiment 1 Experiment 2

Experiment 1 Experiment 2 Experiment 3

Experiment

![image 179](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile179.png)

![image 180](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile180.png)

Success

![image 181](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile181.png)

![image 182](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile182.png)

- 1

Experiment

- 2

Experiment

- 3


![image 183](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile183.png)

![image 184](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile184.png)

![image 185](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile185.png)

![image 186](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile186.png)

![image 187](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile187.png)

Failure

Scientific hypotheses & conclusion

Newly identified regularities, causal relations

Experiment 3

Experimental record

![image 188](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile188.png)

Knowledge graph

![image 189](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile189.png)

![image 190](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile190.png)

anomaly

update update update

###### d. Protocolization of Scientific Infrastructure

e. Safety and Risk Governance

![image 191](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile191.png)

###### Challenge Resolution

###### Challenge Resolution

Irreversible embodiment amplifies cascading risk in long-horizon autonomy

Fragmented, non-interoperable infrastructure

Agent-interpretable action-observation protocols

Governance embedded throughout the PLAD loop

![image 192](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile192.png)

Perception from instrument

Pre-execution safety gating

Observation Action PLAD loop Reasoning & planning

![image 193](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile193.png)

Chemical hazards

Biological risks

![image 194](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile194.png)

![image 195](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile195.png)

![image 196](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile196.png)

…

![image 197](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile197.png)

![image 198](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile198.png)

Model-based risk assessment

![image 199](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile199.png)

Scientific brain

![image 200](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile200.png)

Standardized actions Structured observations Explicit failure states

![image 201](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile201.png)

![image 202](Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI_images/imageFile202.png)

Knowledge-based safety boundaries

Embodied action

##### Figure 4. Challenges and design resolution for sustaining long-horizon PLAD loops. (a) Reasoning over

scientific data: Heterogeneous, noisy instrument signals require mechanism-aware interpretation; science-adapted LLMs, modality-aware encoders, and tool-grounded analysis support reliable reasoning. (b) Embodied execution

reliability: Robust execution across diverse robotic embodiments requires large-scale simulation, trajectory learning, and sim-to-real transfer. (c) Long-horizon knowledge accumulation: Knowledge graphs convert fragmented experimental records into cumulative scientific insight across cycles. (d) Protocolization of scientific

infrastructure: Agent-interpretable action–observation protocols standardize actions, observations, and failure states, enabling composable closed-loop workflows. (e) Safety and risk governance: Trustworthy long-horizon autonomy requires integrated safety gating, model-based risk assessment, and knowledge-based safety boundaries.

tool invocation, in which models work in concert with specialized computational tools to execute precise analytical procedures while maintaining control over higher-level scientific inference. Both model-based and tool-assisted reasoning rely critically on appropriate training paradigms. Agentic reinforcement learning has been shown to be effective in training slow-thinking and contextual tool use, enabling agents to invoke, interpret, and integrate tool outputs within sustained reasoning and planning processes. Together, these design and training strategies support the analysis of raw experimental signals within long-horizon autonomous discovery loops.

- 5.2 Embodied Execution Reliability The core challenge of embodied execution in scientific scenarios lies in execution reliability: whether the experimental actions can be executed correctly, consistently, and repeatedly in complex laboratory environments under strict safety constraints. Scientific experimentation may not be carried out by a single, uniform robotic form. Instead, embodied execution spans a diverse set of physical carriers, including stationary or mobile manipulators and humanoid robots. Ensuring reliable execution across such heterogeneous embodiments amplifies the difficulty of autonomy in scientific environments. Beyond the diversity of embodiments, scientific experiments themselves demand a wide range of precise and highly specialized skills, such as liquid dispensing, powder weighing, apparatus grasping, sample transfer, and instrument interfacing. More importantly, real experiments often involve hazardous chemicals, high temperatures, high pressures, or biosafety risks, making it difficult to scale up learning approaches that rely on physical trial and error. To address these challenges, sim-to-real approaches based on digital twin environments play a central role51. Digital twins enable systematic modeling not only of laboratory layouts and instrument geometries, but also of the interaction dynamics specific to different embodiments and experimental mechanisms. In scientific scenarios, the key to digital twins is not limited to simulation accuracy in terms of geometry or motion, but also includes the accurate depiction of experimental mechanisms. For example, by modeling heat transfer processes, temperature changes in the virtual environment can accurately reflect thermal behaviors in physical experiments, ensuring that execution strategies developed in the simulation environment remain valid in real experiments50. Leveraging simulation environments for large-scale, low-cost training and trial and error, combined with high-quality trajectory data generated from human demonstrations and robot executions, can gradually narrow the gap between virtual and real worlds, enabling smooth migration from simulation training to real-world deployment.
- 5.3 Long-Horizon Knowledge Accumulation The essence of long-horizon autonomy lies in the sustained bidirectional closure between cognition and execution across multiple experimental cycles. Scientific discovery is not a collection of isolated experiments, but a process of cumulative knowledge construction, revision, and extension. First, long-horizon autonomy imposes stringent requirements on memory management65. Agents must continuously record, organize, and revisit historical hypotheses, experimental designs, and observations across extended timescales, such that prior experience can be reliably carried forward into future decision-making. Such continuity cannot be reliably supported by language-model context windows or unstructured experimental logs alone. Second, long-horizon discovery requires that experimental outcomes be systematically analyzed and internalized as evolving scientific knowledge. Newly generated results should not remain as transient observations or isolated performance metrics; rather, they must be integrated into the agent’s internal state. This integration ensures that past successes, failures, and anomalies exert lasting influence, thereby enabling cumulative rather than repetitive discovery.

A central strategy for addressing these challenges is the introduction of knowledge graphs as structured representational skeletons66. At the memory level, they transform fragmented experimental records, hypotheses, and conclusions into structured representations that support retrieval, comparison, and reasoning across temporal scales. At the discovery level, newly identified scientific regularities, causal relationships, or anomalous behaviors can be incorporated as new nodes or relationships, allowing scientific understanding to be continuously expanded and refined. Overall, long-horizon knowledge accumulation is a systemic requirement for the stability and effectiveness of the entire closed loop. Only when scientific knowledge can be persistently accumulated, structured, and revised across experimental cycles can embodied agents move beyond short-term optimization and genuinely assume responsibility for long-horizon autonomous scientific discovery.

- 5.4 Protocolization of Scientific Infrastructure In most laboratories, experimental devices, sensing instruments, and execution modules typically operate as isolated systems. Scientific instruments extend the perceptual boundary of discovery by rendering processes observable; their states and outputs need to be acquired continuously to support reasoning. In practice, however, measurements, device states, and operational logs are recorded locally or exposed only as low-level signals. As a result, perceptual


information cannot flow continuously into the scientific brain, and reasoning outcomes cannot be reliably grounded in the evolving experimental state. This challenge is further amplified in complex experimental settings that involve multi-step procedures and coordinated embodied action. Executing such workflows requires agents to orchestrate heterogeneous robots and manipulators. Without a unified representation of actions and system states, high-level experimental plans cannot be systematically decomposed into executable embodied behaviors. Together, these factors create a structural disconnection between perception, reasoning, and action, constituting a fundamental bottleneck for closed-loop autonomy.

Overcoming this bottleneck requires a principled reorganization of how experimental components are represented and interfaced. Protocolized infrastructure addresses this challenge by defining a unified, agent-interpretable abstraction over distributed experimental components67,68. While networked connectivity enables heterogeneous instruments, sensors, and execution systems to expose their states and outputs, protocolization lifts raw connectivity into agent-operable capability. For example, the Science Context Protocol (SCP)67 offers a standardized way to expose and orchestrate scientific resources, including tools, models, datasets, and physical instruments, thereby transforming heterogeneous laboratory connectivity into agent-operable capability. By standardizing how experimental actions, perceptual observations, and failure or exception states are represented, protocols enable agents to interpret, compare, and compose interactions across instruments and experimental contexts. This allows actions and observations to function as reusable, verifiable primitives within the PLAD loop, supporting traceability, composability, and cumulative discovery across long-horizon cycles.

- 5.5 Safety and Risk Governance Safety constitutes a fundamental challenge for long-horizon autonomous scientific exploration. A defining feature of PLAD is that experimental actions are embodied and irreversible. Physical interventions permanently alter materials, instruments, and environmental states, and erroneous actions cannot be rolled back as failed computations. Risk is further amplified by the iteration of PLAD. It also creates the potential for runaway autonomy, progressively relax implicit safety margins. These factors substantially amplify safety hazards during experimentation, including the execution of unsafe procedures or the generation of hazardous outcomes. For example, operating under extreme temperatures or pressures, employing toxic reagents outside validated regimes, or producing products that pose chemical, biological, or environmental risks beyond the experimental boundary.

Safety governance in PLAD relies on a deliberate complementarity between knowledge-driven constraints and model-based risk assessment. Explicit safety knowledge can be derived from laboratory regulations, instrument specifications, hazard databases, and experimental manuals. It defines operational boundaries that delimit where autonomous exploration must not go. These constraints encode known hazards and non-negotiable limits, ensuring that hypothesis generation and experimental planning remain within validated and auditable regimes. However, long-horizon autonomous discovery routinely encounters risk that cannot be exhaustively specified in advance. As PLAD iterates, hazards may emerge from contextual interactions, cumulative deviations, or gradual extrapolation toward extreme conditions. Model-based safety supervision is therefore required to assess such context-dependent and emergent risks. Safety-aware guard models evaluate candidate plans within their historical and experimental context, estimating whether sequences of otherwise permissible actions collectively approach unsafe regimes.

- 6 Conclusion


Embodied Science reframes discovery as a long-horizon closed-loop process in which reasoning is continuously grounded, corrected, and enriched through physical interaction with the world. This perspective highlights a structural limitation in today’s AI4S landscape: scaling language reasoning improves cognitive breadth, and advancing laboratory automation improves throughput, but neither alone satisfies the core requirement of autonomous discovery, namely the ability to iteratively generate, test, falsify, and revise hypotheses over extended horizons. Without embodiment, reasoning risks becoming self-referential; without scientific cognition, execution risks degenerating into blind optimization.

PLAD provides an organizing principle for overcoming this divide. By integrating Perception, Language, Action, and Discovery into a coupled system, PLAD shifts autonomy from short-term performance to cumulative scientific

understanding, learning not only from success but also from failure, anomaly, and uncertainty. Realizing this vision will require coordinated advances across foundation models, instrument-aware perception, protocol compilation and control, scientific infrastructure, evaluation standards, and safety governance. The central question is no longer whether AI can assist science, but whether scientific discovery can be engineered as an embodied, long-horizon process that remains trustworthy as autonomy scales.

### References

- 1. Wang, H. et al. Scientific discovery in the age of artificial intelligence. Nature 620, 47–60 (2023).
- 2. Jumper, J. et al. Highly accurate protein structure prediction with alphafold. Nature 596, 583–589 (2021).
- 3. Baek, M. et al. Accurate prediction of protein structures and interactions using a three-track neural network. Science 373, 871–876 (2021).
- 4. Wu, Z. et al. Moleculenet: A benchmark for molecular machine learning. Chem. science 9, 513–530 (2018).
- 5. Yu, T. et al. Enzyme function prediction using contrastive learning. Science 379, 1358–1363 (2023).
- 6. Fang, Y. et al. Knowledge graph-enhanced molecular contrastive learning with functional prompt. Nat. Mach. Intell. 5, 542–553 (2023).
- 7. Krishna, R. et al. Generalized biomolecular modeling and design with rosettafold all-atom. Science 384, eadl2528 (2024).
- 8. Zeni, C. et al. A generative model for inorganic materials design. Nature 639, 624–632 (2025).
- 9. Han, Y. et al. Retrosynthesis prediction with an iterative string editing model. Nat. Commun. 15, 6404 (2024).
- 10. Wang, X. et al. Multimodal learning with next-token prediction for large multimodal models. Nature 1–7

(2026).

- 11. Bai, L. et al. Intern-s1: A scientific multimodal foundation model (2025).
- 12. Zhuang, X. et al. Advancing biomolecular understanding and design following human instructions. Nat. Mach. Intell. 7, 1154–1167 (2025).
- 13. Xu, W. et al. Probing scientific general intelligence of llms with scientist-aligned workflows. arXiv preprint arXiv:2512.16969 (2025).
- 14. Kuhn, T. S. & Hacking, I. The structure of scientific revolutions, vol. 2 (University of Chicago press Chicago, 1970).
- 15. Popper, K. The logic of scientific discovery (Routledge, 2005).
- 16. Gao, S. et al. Empowering biomedical discovery with ai agents. Cell 187, 6125–6151 (2024).
- 17. Wei, J. et al. From AI for science to agentic science: A survey on autonomous scientific discovery. CoRR abs/2508.14111 (2025).
- 18. Naveed, H. et al. A comprehensive overview of large language models. ACM Transactions on Intell. Syst. Technol. 16, 1–72 (2025).
- 19. Achiam, J. et al. Gpt-4 technical report. arXiv preprint arXiv:2303.08774 (2023).
- 20. Li, B., Saini, A. K., Hernandez, J. G. & Moore, J. H. Agentic ai and the rise of in silico team science in biomedical research. Nat. Biotechnol. 1–15 (2026).
- 21. Tom, G. et al. Self-driving laboratories for chemistry and materials science. Chem. Rev. 124, 9633–9732 (2024).
- 22. Canty, R. B. et al. Science acceleration and accessibility with self-driving labs. Nat. Commun. 16, 3856 (2025).
- 23. Hao, Q., Xu, F., Li, Y. & Evans, J. Artificial intelligence tools expand scientists’ impact but contract science’s focus. Nature 1–7 (2026).


- 24. Yao, S. et al. React: Synergizing reasoning and acting in language models. In ICLR (OpenReview.net, 2023).
- 25. Fung, P. et al. Embodied AI agents: Modeling the world. CoRR abs/2506.22355 (2025).
- 26. Hey, T., Tansley, S., Tolle, K. M. et al. The fourth paradigm: Data-intensive scientific discovery, vol. 1 (Microsoft research Redmond, WA, 2009).
- 27. M. Bran, A. et al. Augmenting large language models with chemistry tools. Nat. Mach. Intell. 6, 525–535

(2024).

- 28. Huang, K. et al. Biomni: A general-purpose biomedical ai agent. bioRxiv 2025–05 (2025).
- 29. Ding, K. et al. Scitoolagent: A knowledge-graph-driven scientific agent for multitool integration. Nat. Comput. Sci. 5, 962–972 (2025).
- 30. Gao, S. et al. Democratizing AI scientists using tooluniverse. CoRR abs/2509.23426 (2025).
- 31. Swanson, K., Wu, W., Bulaong, N. L., Pak, J. E. & Zou, J. The virtual lab of ai agents designs new sars-cov-2 nanobodies. Nature 646, 716–723 (2025).
- 32. Ghareeb, A. E. et al. Robin: A multi-agent system for automating scientific discovery. CoRR abs/2505.13400

(2025).

- 33. Penadés, J. R. et al. Ai mirrors experimental science to uncover a mechanism of gene transfer crucial to bacterial evolution. Cell 188, 6654–6665 (2025).
- 34. Novikov, A. et al. Alphaevolve: A coding agent for scientific and algorithmic discovery. CoRR abs/2506.13131

(2025).

- 35. Weng, Y. et al. Deepscientist: Advancing frontier-pushing scientific findings progressively. CoRR abs/2509.26603 (2025).
- 36. Team, I. et al. Internagent: When agent becomes the scientist–building closed-loop system from hypothesis to verification. arXiv e-prints arXiv–2505 (2025).
- 37. Feng, S. et al. Internagent-1.5: A unified agentic framework for long-horizon autonomous scientific discovery. arXiv preprint arXiv:2602.08990 (2026).
- 38. Lu, C. et al. The AI scientist: Towards fully automated open-ended scientific discovery. CoRR abs/2408.06292

(2024).

- 39. Mitchener, L. et al. Kosmos: An AI scientist for autonomous discovery. CoRR abs/2511.02824 (2025).
- 40. Steiner, S. et al. Organic synthesis in a modular robotic system driven by a chemical programming language. Science 363, eaav2211 (2019).
- 41. Kuwahara, M. et al. Development of an open-source 3d-printed material synthesis robot fluid: Hardware and software blueprints for accessible automation in materials science. ACS Appl. Eng. Mater. 3, 978–987 (2025).
- 42. Szymanski, N. J. et al. An autonomous laboratory for the accelerated synthesis of inorganic materials. Nature 624, 86–91 (2023).
- 43. Slattery, A. et al. Automated self-optimization, intensification, and scale-up of photocatalysis in flow. Science 383, eadj1817 (2024).
- 44. Zhang, Z. et al. A multimodal robotic platform for multi-element electrocatalyst discovery. Nature 647, 390–396

(2025).

- 45. Boiko, D. A., MacKnight, R., Kline, B. & Gomes, G. Autonomous chemical research with large language models. Nature 624, 570–578 (2023).
- 46. Song, T. et al. A multiagent-driven robotic ai chemist enabling autonomous chemical research on demand. J. Am. Chem. Soc. 147, 12534–12545 (2025).
- 47. King, R. D. et al. The automation of science. Science 324, 85–89 (2009).


- 48. Burger, B. et al. A mobile robotic chemist. Nature 583, 237–241 (2020).
- 49. Dai, T. et al. Autonomous mobile robots for exploratory synthetic chemistry. Nature 635, 890–897 (2024).
- 50. Darvish, K. et al. Matterix: Toward a digital twin for robotics-assisted chemistry laboratory automation. Nat. computational science 1–16 (2025).
- 51. Zhao, W., Queralta, J. P. & Westerlund, T. Sim-to-real transfer in deep reinforcement learning for robotics: A survey. In 2020 IEEE symposium series on computational intelligence (SSCI), 737–744 (IEEE, 2020).
- 52. Xu, Y. et al. Lumi-lab: A foundation model-driven autonomous platform enabling discovery of ionizable lipid designs for mrna delivery. Cell (2026).
- 53. Shi, T. et al. Knowledge-driven autonomous materials research via collaborative multi-agent and robotic system. Matter (2026).
- 54. Zitkovich, B. et al. RT-2: Vision-language-action models transfer web knowledge to robotic control. In 7th Annual Conference on Robot Learning (2023).
- 55. Wang, P. et al. Qwen2-vl: Enhancing vision-language model’s perception of the world at any resolution. arXiv preprint arXiv:2409.12191 (2024).
- 56. Guo, D. et al. Deepseek-r1 incentivizes reasoning in llms through reinforcement learning. Nature 645, 633–638

(2025).

- 57. Ding, K. et al. Bridging data and discovery: A survey on knowledge graphs in ai for science. Natl. Sci. Rev. nwag140 (2026).
- 58. Meng, Z., Chen, J., Zhuang, X. & Zhang, Q. Integrating knowledge graphs and large language models for advancing scientific research. In 2025 IEEE 45th International Conference on Distributed Computing Systems Workshops (ICDCSW), 393–396 (IEEE, 2025).
- 59. Agarwal, O., Ge, H., Shakeri, S. & Al-Rfou, R. Knowledge graph based synthetic corpus generation for knowledge-enhanced language model pre-training. In NAACL-HLT, 3554–3565 (Association for Computational Linguistics, 2021).
- 60. Gao, Y. et al. Retrieval-augmented generation for large language models: A survey. CoRR abs/2312.10997

(2023).

- 61. Liang, L. et al. Kag: Boosting llms in professional domains via knowledge augmented generation. In Companion Proceedings of the ACM on Web Conference 2025, WWW ’25, 334–343 (Association for Computing Machinery, New York, NY, USA, 2025).
- 62. Lu, J.-M., Pan, J.-Z., Mo, Y.-M. & Fang, Q. Automated intelligent platforms for high-throughput chemical synthesis. Artif. Intell. Chem. 2, 100057 (2024).
- 63. Orouji, N. et al. Autonomous catalysis research with human–ai–robot collaboration. Nat. Catal. 1–11 (2025).
- 64. Zhao, H. Biofoundry: Nsf ibiofoundry for basic and applied biology. NSF Award. Number 2400058. Dir. for Biol. Sci. 24, 58 (2024).
- 65. Hu, Y. et al. Memory in the age of ai agents. arXiv preprint arXiv:2512.13564 (2025).
- 66. Chhikara, P., Khant, D., Aryan, S., Singh, T. & Yadav, D. Mem0: Building production-ready ai agents with scalable long-term memory. arXiv preprint arXiv:2504.19413 (2025).
- 67. Jiang, Y. et al. Scp: Accelerating discovery with a global web of autonomous scientific agents. arXiv preprint arXiv:2512.24189 (2025).
- 68. Sim, M. et al. Chemos 2.0: An orchestration architecture for chemical self-driving laboratories. Matter 7, 2959–2977 (2024).


