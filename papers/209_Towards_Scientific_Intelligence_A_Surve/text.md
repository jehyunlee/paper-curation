# arXiv:2503.24047v3[cs.AI]2 Feb 2026

## Towards Scientific Intelligence: A Survey of LLM-based Scientific Agents

Shuo Ren*1,2, Can Xie*1,3, Pu Jian1,3, Zhenjiang Ren1,3, Chunlin Leng1,3, Jiajun Zhang†1,2,3,4

- 1 State Key Laboratory of Multimodal Artificial Intelligence Systems,
- 2 Foundation Model Research Center, Institute of Automation, CAS.
- 3 University of Chinese Academy of Science, Beijing, China.
- 4 Wuhan AI Research, Wuhan, China. †jjzhang@nlpr.ia.ac.cn


*{shuo.ren, xiecan2024, jianpu2023, renzhenjiang2024, lengchunlin2023}@ia.ac.cn

### Abstract

As scientific research becomes increasingly complex, innovative tools are needed to manage vast data, facilitate interdisciplinary collaboration, and accelerate discovery. Large language models (LLMs) are now evolving into LLM-based scientific agents that automate critical tasks—ranging from hypothesis generation and experiment design to data analysis and simulation. Unlike general-purpose LLMs, these specialized agents integrate domain-specific knowledge, advanced tool sets, and robust validation mechanisms, enabling them to handle complex data types, ensure reproducibility, and drive scientific breakthroughs. This survey provides a focused review of the architectures, design, benchmarks, applications, and ethical considerations surrounding LLM-based scientific agents. We highlight why they differ from general agents and the ways in which they advance research across various scientific fields. By examining their development and challenges, this survey offers a comprehensive roadmap for researchers and practitioners to harness these agents for more efficient, reliable, and ethically sound scientific discovery.

### 1 Introduction

Imagine an AI agent that autonomously designs a groundbreaking vaccine, optimizes chemical reactions with precision, or uncovers hidden patterns in astronomical data—all while maintaining ethical standards and reproducibility. This is no longer science fiction. Large language models (LLMs), once confined to text generation, are now transforming scientific research by evolving into scientific agents capable of automating complex tasks such as hypothesis generation, experimental design, and data analysis. Unlike general-purpose LLM agents, which are optimized for broad applications like dialogue or coding assistance, scientific

*These authors contribute equally to this work. †Corresponding author.

agents integrate domain-specific knowledge, interact through diverse action spaces (including software APIs, simulators, and analytical tools), and process heterogeneous data types ranging from numerical datasets to molecular structures and biological sequences. This specialization equips them to manage the growing complexity of modern science, facilitate interdisciplinary discovery, and accelerate the pace of breakthrough research.

As the adoption of LLM-based scientific agents grows, a systematic review of their development, applications, and challenges becomes essential. While existing surveys provide comprehensive overviews of general LLM-based agents (Wang et al., 2024a; Xi et al., 2023; Guo et al., 2024; Hu et al., 2024a; Li et al., 2024e; Xie et al., 2024; Cheng et al., 2024; Shen, 2024; Gridach et al., 2025), focusing specifically on LLM-based scientific agents is crucial given their distinctive roles and requirements in the scientific domain. Several recent surveys have begun to address this gap from different vantage points: Luo et al. (2025) emphasize the contributions of LLMs to discrete scientific tasks such as hypothesis generation, experimental design, and peer review; Wang et al. (2025c) present the Hitchhiker’s Guide to Scientific Agents, framing scientific agents along the research lifecycle and classifying them into three capability levels (Assistant, Partner, Avatar); and Wei et al. (2025) introduce Agentic Science as a paradigm shift where AI systems evolve from computational tools to autonomous research partners, offering a domain-oriented review across life sciences, chemistry, materials, and physics. In contrast, our work adopts a mechanism-centric perspective, focusing on the architectural and algorithmic foundations—planners, memory modules, action space, and verifiers—that enable scientific agents to operate with rigor, reproducibility, and ethical alignment. By analyzing these four components as the building blocks of autonomy, we connect high-

level agent capabilities to their underlying design principles. This perspective complements existing lifecycle- and role-based surveys while advancing a design-focused taxonomy that clarifies how LLMbased agents achieve trustworthy and scientifically valid performance.

Our contributions can be summarized as follows:

- • Mechanism-oriented taxonomy: We propose a taxonomy of LLM-based scientific agents that emphasizes four architectural mechanisms—planner, memory, action space, and verifier—rather than application roles or lifecycle stages.
- • Component-wise construction blueprint: We provide multiple sub-types of each component or mechanism, and show how they can be mixed-and-matched to build fit-for-purpose agents. A running, end-to-end cathode-design example consistently illustrates every component, offering researchers an intuitive “recipe book” for agent assembly.
- • Comprehensive literature & benchmark atlas: The survey synthesises >120 representative papers and >40 domain benchmarks, and classifies all related works into fine-grained, mechanism-level categories according to their signature characteristics. This curated map enables domain experts to quickly locate transferable techniques and baselines for their own tasks.
- • Ethics and reproducibility as design imperatives: We extend prior discussions by framing ethics, bias mitigation, and reproducibility not as peripheral concerns but as intrinsic design constraints embedded within the agent’s architecture and verification modules.
- • Research outlook: We identify open challenges and future directions, particularly the integration of interdisciplinary knowledge, dynamic adaptation, and standardized reproducibility protocols.


The remainder of this survey is organized as follows: In Section 2 Architecture, we begin by examining the fundamental design of these agents. This section is subdivided into four main parts: first, the role of the Planner (Section 2.1) in decomposing and managing scientific tasks; second, the

various Memory mechanisms (Section 2.2) that enable context retention and iterative learning; third, the Action Space (Section 2.3) that operationalizes agentic reasoning through tool invocation, code execution, and interaction with external environments; and finally, the Verifier (Section 2.4), which ensures reliability, factual accuracy, and empirical consistency. Additionally, each subsection concludes with open challenges and future directions, offering guidance for both scholars and practitioners in harnessing the full potential of them.

After that, Section 3 Benchmarks reviews the evaluation frameworks used to assess both general reasoning and scientific research performance. Section 4 Applications explores real-world deployments of LLM-based agents across diverse disciplines, while Section 5 Ethics addresses ethical implications and reproducibility challenges, emphasizing responsible and transparent use.

Finally, in Appendix A, we classified all the related works into fine-grained, mechanism-level categories, and group them according to their domains. We hope this could provide domain researchers with quick understand of how to build scientific agents of their own domains.

![image 1](Ren et al._2025_Towards Scientific Intelligence A Survey of LLM-based Scientific Agents_images/imageFile1.png)

Figure 1: A typical architecture of LLM-based scientific agents. Note that in mainstream agent frameworks, planners are predominantly implemented based on LLMs, and their capabilities include task planning, reflection, and verification, etc. For the sake of abstraction, we represent these functions with a single planner in this architecture diagram. However, in specific implementations, different agents might be set up to accomplish distinct functions (see Section 2.1 for further discussion about planner types).

- P1. Instructional/ Schema-Driven

AutoLabs (Panapitiya et al., 2025), Coscientist (Boiko et al., 2023), CRISPR-GPT (Huang et al., 2024a), GeneGPT (Jin et al., 2024), k-agents (Cao et al., 2024), LLMSat (Maranto, 2024), ORGANA (Darvish et al., 2025), ResearchAgent (Baek et al., 2024), StarWhisper (Wang et al., 2025a),etc.

- P2. ContextAugmented

CellVoyager (Alber et al., 2025), CoI (Li et al., 2024b), Coscientist (Boiko et al., 2023), GeoSim.AI (Bekele, 2025), HoneyComb (Zhang et al., 2024a), IR-Agent (Noh et al., 2025), PaSa (He et al., 2025), ResearchAgent (Baek et al., 2024), SciMON (Wang et al., 2024b), STELLA (Jin et al., 2025), VirSci (Su et al., 2024), etc.

- P3. Deliberative/ Reflective

AtlasAgent (Yin et al., 2025), CellForge (Tang et al., 2025d), dZiner (Ansari et al., 2024), k-agents (Cao et al., 2024), MoRA (Jaiswal et al., 2024), LLMatDesign (Jia et al., 2024), OriGene (Zhang et al., 2025e), VirSci (Su et al., 2024), OpenFOAMGPT 2.0 (Feng et al., 2025a), etc.

- P4. Search-Based

AI Scientist-v2 (Yamada et al., 2025), CheMatAgent (Wu et al., 2025), ChemReasoner (Sprueill et al., 2024), GeoAgent (Chen et al., 2024a), InternAgent (Team et al., 2025a), Mephisto (Sun et al., 2024b), SGA (Ma et al., 2024a) etc.

- P5. Role-Interactive/ Multi-Agent

AI co-scientist (Gottweis et al., 2025), AIGS (Liu et al., 2024c), AtomAgents (Ghafarollahi and Buehler, 2024a), El Agente (Zou et al., 2025), Foam-Agent (Yue et al., 2025), InternAgent (Team et al., 2025a), IR-Agent (Noh et al., 2025), LLM-RDF (Ruan et al., 2024), MechAgents (Ni and Buehler, 2024), MedAgents (Tang et al., 2023), ProtAgents (Ghafarollahi and Buehler, 2024b), Robin (Ghareeb et al., 2025), STELLA (Jin et al., 2025), TAIS (Liu et al., 2024a), VirSci (Su et al., 2024), xChemAgents (Polat et al., 2025), etc.

- P6. Programmatic (Code/DSL/DAG)


Prompt-Native Planners

Planner

AIGS (Liu et al., 2024c), AlphaEvolve (Novikov et al., 2025), Biomni (Huang et al., 2025a), Chemist-X (Chen et al.), K-Dense Analyst (Li et al., 2025b), ORGANA (Darvish et al., 2025), SGA (Ma et al., 2024a), etc.

AstroMLab (de Haan et al., 2025), BioGPT (Luo et al., 2022), Chemma (Zhang et al., 2025d), DrugAssist (Ye et al., 2023a), DrugPilot (Li et al., 2025a), GatorTronGPT (Peng et al., 2023), GeoMinLM (Fu et al., 2025a), MatChat (Chen et al., 2023), NatureLM (Xia et al., 2025b), ToRA (Gou et al., 2024), etc.

L1. SFT/ Domain-Trained

Learned Planners

BioScientist Agent (Zhang et al., 2025a), CheMatAgent (Wu et al., 2025), Chemma (Zhang et al., 2025d), CycleResearcher (Weng et al., 2025), ReFT (Luong et al., 2024), STEP-DPO (Lai et al., 2024), Flow-DPO (Deng and Mineiro, 2024), SciMARL (Bae and Koumoutsakos, 2022), MolRL-MGPT (Hu et al., 2024b), PaSa (He et al., 2025), etc.

L2. RL/ Preference-Optimized

###### Figure 2: Taxonomy of the planner mechanism of representative scientific agents with P1-P6: Prompt-Native Planners and L1-L2: Learned Planners

### 2 Architecture

The architecture of LLM-based scientific agents is designed to enable iterative, context-aware processing of complex scientific tasks. It typically consists of four core components: Planner, Memory, Action Space, and Verifier, as shown in Figure 1. The workflow begins with the user submitting a query, typically a scientific problem expressed in text and associated data. The query is received as input by the system. The Planner decomposes the task into sub-tasks, retrieves relevant context or knowledge from Memory, and executes actions through the Action Space (e.g., APIs, simulators, laboratory instruments, or search engines). The LLM itself can also function as part of the Action Space when performing reasoning, computation, or intermediate analysis. These actions generate intermediate results that are examined by the Verifier to ensure accuracy, consistency, and scientific plausibility. Verified results are then stored in Memory to refine future decisions. If verification indicates further actions or corrections, the Planner generates new plans and re-invokes the Action Space. This iterative process continues until the Verifier confirms that the output meets standards of validity and reproducibility, after which the final integrated result is returned to the user. Note that while previous LLM-based multimodal agents often included a separate perceptron module to handle multimodal inputs (Xie et al., 2024), our survey integrates multimodal scientific data perception as an intrinsic capability of the Planner for conceptual simplicity. In the following subsections, we introduce these four components in detail.

#### 2.1 Planner

The planner serves as the architectural core of LLM-based scientific agents, translating high-level research objectives into structured, actionable task sequences that orchestrate tool invocations, memory operations, and verification steps. In autonomous scientific discovery, planning encompasses the decomposition of complex research goals—from hypothesis formulation to experimental design, data analysis, and validation—into executable workflows that coordinate the agent’s capabilities toward scientific outcomes. Effective planners must balance task granularity, dependency management, and adaptive replanning to navigate the inherent uncertainty and open-endedness of scientific inquiry. According to their operational

mechanisms, current scientific agent planners can be categorized into two families: prompt-native planners as in subsection 2.1.1, which structure plans entirely through language-based instructions and templates, and learned planners as in subsection 2.1.2, which internalize planning strategies through training on domain-specific trajectories or reward signals.

#### 2.1.1 Prompt-Native Planners

Prompt-native planners construct task decomposition and workflow orchestration entirely through carefully designed prompts, leveraging the LLM’s in-context learning capabilities to generate and structure plans without parameter modification. This approach provides direct interpretability so that researchers can inspect and modify planning logic through prompt editing—and rapid adaptability to new scientific domains. The six major prompt-native subtypes represent distinct approaches to plan construction as shown in Figure 3: instructional/schema-driven planners encode procedural templates directly in prompts; context-augmented planners encode historical or searched context in prompts; deliberative/reflective planners incorporate self-critique cycles to refine plans; search-based planners explore multiple alternative plan candidates; role-interactive planners distribute planning across collaborative agent ensembles; and programmatic planners generate machine-executable plan representations. Note that some works use more than one type of prompt, and we only exemplify their typical type.

#### (1) P1. Instructional / Schema-Driven Planners

Instructional or schema-driven planners structure scientific workflows by embedding predefined instructions or procedural templates directly into system prompts that guide task decomposition and action sequencing. These instructions can take various forms: structured workflow templates encoding domain methodologies (e.g., "literature review → hypothesis formulation → experimental design → validation"), standardized response formats specifying expected output structures (e.g., ReAct’s Thought-Action-Observation format (Yao et al., 2023b)), tool usage schemas defining available operations and their invocation patterns, or domainspecific guidelines prescribing best practices and constraints. Rather than discovering task decompositions dynamically through learning, schemadriven planners instantiate plans by following pre-

|RESEARCH GOAL: "Design and synthesize a high-capacity cathode material for Li-ion ba eries (>200 mAh/g, stable for 500+ cycles)"|
|---|


|SYSTEM PROMPT (Battery Schema)<br><br>|Persona: "You are a battery materials expert..." Procedural Schema:<br><br>1. Crystal Structure Design → 2. DFT Screening → 3. Synthesis Planning → 4. Electrochemical Testing Tool Inventory: [VASP, XRD_Simulator, Autolab_API] Constraints: Avoid Co (cost), target voltage >4V|
|---|
|
|---|


|AUGMENTED PROMPT<br><br>|[Historical] NMC811 failed @400 cycles (capacity fade) [Historical] LFP stable but capacity only 160 mAh/g [KB] Target conductivity: σ >1000 mS/cm for rate capability [KB] Voltage window: 4.0-4.3V vs Li/Li+ Design new material avoiding NMC811's Mn dissolution issue while exceeding LFP capacity...|
|---|
|
|---|


![image 2](Ren et al._2025_Towards Scientific Intelligence A Survey of LLM-based Scientific Agents_images/imageFile2.png)

Records

![image 3](Ren et al._2025_Towards Scientific Intelligence A Survey of LLM-based Scientific Agents_images/imageFile3.png)

KBs

P2. Context -Augmented Planners

P1. Instructional / Schema - Driven Planners

|Plan: STEP1 xxx -> STEP2 xxx -> ...|
|---|


![image 4](Ren et al._2025_Towards Scientific Intelligence A Survey of LLM-based Scientific Agents_images/imageFile4.png)

|Plan: STEP1 xxx -> STEP2 xxx -> ...|
|---|


![image 5](Ren et al._2025_Towards Scientific Intelligence A Survey of LLM-based Scientific Agents_images/imageFile5.png)

![image 6](Ren et al._2025_Towards Scientific Intelligence A Survey of LLM-based Scientific Agents_images/imageFile6.png)

![image 7](Ren et al._2025_Towards Scientific Intelligence A Survey of LLM-based Scientific Agents_images/imageFile7.png)

|Final Plan with reflection|
|---|


|Final Plan with max reward path|
|---|


###### P4. Search-Based Planners

###### P3. Deliberative / Reflective Planners

Yes

|[ROOT: Cathode >200 mAh/g]<br><br>[LFP Variant] (Score: 0.5)<br><br>[NMC Variant] (Score: 0.7)<br><br>[Co-free Layered] (Score: 0.65)<br><br>[NMCMg]<br><br>(0.82)<br><br>[NMC-Al] ( 0.75)<br><br>| |DFT_SIMULATOR E_cal = -3.1 eV Cycles: 520|
|---|---|
| | |
|
|---|


|Generate Initial Plan: Li-rich oxide| |
|---|---|
| | |


|Reflect: Cycles=550 ✓ Converged?|
|---|


|No| |
|---|---|
|Revise: Mg-doping<br><br>+ Al2O3 coating| |


|Reflect: Evaluate flaws<br><br>- Cycles: 480 (<500)<br>- Safety: O2 release risk<br>| |
|---|---|
| | |


![image 8](Ren et al._2025_Towards Scientific Intelligence A Survey of LLM-based Scientific Agents_images/imageFile8.png)

![image 9](Ren et al._2025_Towards Scientific Intelligence A Survey of LLM-based Scientific Agents_images/imageFile9.png)

|Consensus Plan|
|---|


|Excution Plan|
|---|


P5. Role-Interactive / Multi-Agent Prompting

P6. Programma c Plan Synthesis

|LiNiO2-Mg Proposal|
|---|


|EXECUTABLE ARTIFACT ```python workflow = DSL_Pipeline() workflow.add(DFT_Screening(can didates=100, criteria={"capacity": ">200"}))<br><br>....<br><br>(OR: DAG with explicit task dependencies)|
|---|


|LLM CODE GENERATOR Prompt: "Generate DFT+Synthesis pipeline as Python script"|
|---|


||Materials Designer|
|---|
<br><br>|Safety Critic|
|---|
<br><br>|Synthesis Engineer|
|---|
|
|---|


| | |
|---|---|
|Revise: Mn-rich| |


|Evaluation and debate<br><br>→ D:✓ C:✗ E:?|
|---|


Figure 3: Different types of prompt-native planners of LLM-based scientific agents.

defined instructional patterns.

Mechanistically, these planners operate by providing a single LLM agent with explicit planning instructions through system prompts. These instructions may include: (1) procedural schemas outlining required workflow stages, permissible actions at each stage, and transition conditions between stages (Xia et al., 2025a; Moss, 2025; Lu

- et al., 2024a; Yamada et al., 2025; Liu et al., 2024c; Mandal et al., 2024; Liu et al., 2024b; Schmidgall
- et al., 2025; Yin et al., 2025; Panapitiya et al., 2025; Luo et al., 2022; Li et al., 2024c; McNaughton


- et al., 2024; Huang et al., 2024a; Tang et al., 2025d; Kang and Kim, 2024; Tang et al., 2025b; Bran


- et al., 2024; Li et al., 2024b; Boiko et al., 2023; Xue et al., 2024; Inoue et al., 2024; Peng et al.,

- 2023; Jin et al., 2024; Bekele, 2025; Ruan et al.,
- 2024; Maranto, 2024; Zhou et al., 2025; Li et al.,


- 2024d; Yang et al., 2024b; Ni and Buehler, 2024; Sun et al., 2024b; Yu et al., 2024; Jaiswal et al.,


- 2024; Riffle et al., 2025; Darvish et al., 2025; Hu

et al., 2025b; Feng et al., 2025a; Zhang et al.,

- 2025e; Pantiukhin et al., 2025; Baek et al., 2024;




- Ma et al., 2024a; Ghafarollahi and Buehler, 2024c; Wang et al., 2025a; Zhang et al., 2025b; Su et al.,


- 2024; Ansari et al., 2024; Cao et al., 2024); (2) response format specifications defining the structure of planning outputs, such as ReAct’s ThoughtAction-Observation or question/thought/input/observation sequences (Moss, 2025; Lu et al., 2024a; Yamada et al., 2025; Liu et al., 2024c; Mandal et al.,


- 2024; Liu et al., 2024b; Schmidgall et al., 2025; Yin et al., 2025; Panapitiya et al., 2025; Roohani

- et al., 2024; Li et al., 2024c; McNaughton et al.,


- 2024; Kang and Kim, 2024; Tang et al., 2025b; Bran et al., 2024; Pham et al., 2025; Sprueill et al.,

- 2024; Li et al., 2024b; Boiko et al., 2023; Xue

- et al., 2024; Inoue et al., 2024; Peng et al., 2023; Huang et al., 2025b; Bekele, 2025; Ning et al.,

2025; Ruan et al., 2024; Maranto, 2024; Zhou

- et al., 2025; Li et al., 2024d; Chen et al., 2023; Riffle et al., 2025; Darvish et al., 2025; Hu et al.,




- 2025b; Zhang et al., 2025e; Ma et al., 2024a; Ghafarollahi and Buehler, 2024c, 2025; Wang et al.,


- 2025a; Zhang et al., 2025b; Su et al., 2024; Ansari


- et al., 2024); (3) tool inventories with descriptions of available tools, their inputs/outputs, and usage contexts (Xia et al., 2025a; Yamada et al., 2025; Gottweis et al., 2025; Schmidgall et al., 2025; Ye


- et al., 2023b; McNaughton et al., 2024; Kang and Kim, 2024; Bran et al., 2024; Pham et al., 2025; Boiko et al., 2023; Jin et al., 2024; Bekele, 2025;


Ruan et al., 2024; Maranto, 2024; Zhou et al., 2025; Kumar et al., 2023; Hu et al., 2025b; Zhang et al., 2025e; Pantiukhin et al., 2025; Ghafarollahi and Buehler, 2024c; Wang et al., 2025a; Zhang et al., 2025b; Ansari et al., 2024); (4) domain-specific guidelines encoding experimental best practices, safety constraints, or resource limitations (Moss, 2025; Lu et al., 2024a; Panapitiya et al., 2025; Tang et al., 2025d; Sprueill et al., 2024; Xue et al., 2024; Bekele, 2025; Ning et al., 2025; Ruan et al., 2024; Zhou et al., 2025; Li et al., 2024d; Darvish et al., 2025; Hu et al., 2025b; Feng et al., 2025a; Ansari

- et al., 2024); (5) task-specific persona descriptions providing domain context, such as "You are a chemist designing synthesis routes" (Moss, 2025; Lu et al., 2024a; Yamada et al., 2025; Gottweis
- et al., 2025; Liu et al., 2024c; Mandal et al., 2024; Liu et al., 2024b; Schmidgall et al., 2025; Yin et al., 2025; Panapitiya et al., 2025; Roohani et al., 2024; Luo et al., 2022; Li et al., 2024c; Huang et al.,


- 2024a; Tang et al., 2025d; Kang and Kim, 2024; Tang et al., 2025b; Bran et al., 2024; Pham et al.,
- 2025; Li et al., 2024b; Boiko et al., 2023; Xue


- et al., 2024; Inoue et al., 2024; Peng et al., 2023; Bekele, 2025; Ruan et al., 2024; Maranto, 2024; Zhou et al., 2025; Ni and Buehler, 2024; Sun et al., 2024b; Yu et al., 2024; Jaiswal et al., 2024; Kumar et al., 2023; Riffle et al., 2025; Darvish et al., 2025; Hu et al., 2025b; Feng et al., 2025a; Pantiukhin
- et al., 2025; Baek et al., 2024; Ghafarollahi and Buehler, 2024c, 2025; Wang et al., 2025a; Zhang et al., 2025b; Su et al., 2024; Ansari et al., 2024; Cao et al., 2024). The planner decomposes incoming research goals into subtasks matching these instructional templates, then sequences subtasks according to schema constraints. This ensures procedural consistency and reproducibility—agents given identical schemas and goals will generate structurally similar plans.


Representative implementations demonstrate diverse instructional approaches. Coscientist (Boiko et al., 2023) guides autonomous chemical experimentation through four predefined commands (“GOOGLE", “PYTHON", “DOCUMENTATION", “EXPERIMENT"), with the Planner module (GPT-4) invoking these commands to collect knowledge and fix code in case of software errors—ensuring reproducible laboratory cycles. GeneGPT (Jin et al., 2024) utilizes specifically designed prompts consisting of four modules: an instruction providing overall task description, API documentations offering natural language descrip-

tions of E-utils and BLAST functionality, API demonstrations providing concrete usage examples, and test questions—guiding Codex stepby-step on NCBI API interaction for genomics queries. LLMSat (Maranto, 2024) employs a spacecraft controller prompt with three sections (system prompt, console prompt, operation logs), using ReAct framework to generate interleaved reasoning traces and actions, with a self-discovery design philosophy where the agent learns console operation on-the-fly. StarWhisper (Wang et al., 2025a) implements telescope control workflows based on LLM agents, structuring astronomical observation planning through predefined operational schemas for instrument commands and observation sequencing. ORGANA (Darvish et al., 2025) uses structured prompts guiding a “robot chemist" through experiment information gathering, with templates for filling items (experiment description, lab setup, example experiments, rationale, expected outcomes), asking one question at a time until “<DONE>". k-agents (Cao et al., 2024) encapsulates laboratory knowledge including available operations and analysis methods, breaking multi-step experimental procedures into agent-based state machines with transition rules. ResearchAgent (Baek

- et al., 2024) organizes idea generation into iterative literature-grounded steps, using prompt templates encoding “background–method–evaluation" structures. CRISPR-GPT (Huang et al., 2024a) instructs planners to respect task dependencies in Task Description Tables, decomposing requests into dependency-aware task lists ensuring prerequisite completion. AutoLabs (Panapitiya et al., 2025) initializes supervisors with comprehensive prompts encoding hardware specifications (vial sizes, array configurations, step types, parameter limits), syntax guidelines for procedural steps, and chemical best practices (capping volatile solvents, prioritizing solid additions).


This approach excels in transparency, reproducibility, and rapid deployment across domains with codifiable methodologies. However, schemadriven planners exhibit limited adaptability—they cannot dynamically restructure plans when encountering novel problem types not anticipated in templates, and their performance depends critically on schema quality and completeness.

#### (2) P2. Context-Augmented Planners

Context-augmented planners embed external or retrieved scientific evidence—such as literature findings, empirical data, or experimental meta-

data—directly into prompts to guide task decomposition and workflow construction. By coupling retrieval mechanisms with in-context learning, they ground each planning step in verifiable domain knowledge, enabling LLMs to emulate expert scientists who construct plans from prior records rather than pure abstraction. This integration transforms language models from generic plan generators into evidence-aware planners capable of producing empirically anchored and reproducible scientific workflows.

Mechanistically, context-augmented planners operate by first querying external knowledge sources—literature databases, knowledge graphs, experimental archives, or documentation repositories—then injecting retrieved content into planning prompts as contextual evidence. The planner uses this evidence to inform task prioritization, validate plan feasibility, and select appropriate methodologies. Retrieval may be triggered explicitly (user specifies literature to consult) or automatically (planner queries databases based on task keywords), with retrieved content formatted as contextual background, methodological examples, or constraint specifications within the prompt (Tang et al., 2025a; Schmidgall et al., 2025; Novikov et al., 2025; Mehandru et al., 2025; Su et al., 2025; Sprueill et al., 2024; Chen et al.; Li et al., 2024b; Boiko et al., 2023; Weng et al., 2025; Inoue et al.,

- 2024; Chen et al., 2024a; Fu et al., 2025a; Bekele,
- 2025; Zhang et al., 2024a; Noh et al., 2025; Ning et al., 2025; Sun et al., 2024b; Yu et al., 2024; Pantiukhin et al., 2025; He et al., 2025; Baek et al., 2024; Ma et al., 2024b; Wang et al., 2024b; Ghafarollahi and Buehler, 2025; Su et al., 2024; Perlis et al., 2024).


Representative implementations illustrate diverse strategies. ResearchAgent (Baek et al., 2024) integrates prior publications and methodological descriptions into prompt memory, allowing the planner to evaluate research ideas against documented evidence before refinement, grounding each planning step in literature-validated approaches. CoI (Li et al., 2024b) prompts the LLM with the constructed Chain-of-Idea, the developing trends of existing works, and the key entities extracted from existing literature, to predict future research directions, and craft ideas through stepby-step consolidation and iterative novelty checks. Coscientist (Boiko et al., 2023) retrieves and summarizes relevant technical documentation through “DOCUMENTATION" commands, to refine the un-

derstanding of APIs and invoke experiments. HoneyComb (Zhang et al., 2024a) queries large-scale MatSciKB to retrieve thermodynamic data, synthesis precedents, and property relationships, contextualizing materials design decisions with empirical evidence. CellVoyager (Alber et al., 2025) uses self-critiquing and replanning based on code execution outputs and interpretations (via a visionlanguage model) as the context, for autonomously exploring scRNA-seq datasets in novel directions. GeoSim.AI (Bekele, 2025) integrates comprehensive geomechanics knowledge bases (theoretical information, empirical data, simulation best practices) via RAG to guide computational workflow construction. IR-Agent’s retriever expert (Noh

- et al., 2025) identifies similar IR spectra from spectral databases, using retrieved analogues to provide global contextual clues that guide molecular structure reasoning. PaSa (He et al., 2025) optimizes paper search planning using crawler histories spanning hundreds of papers, with Selector agents taking scholar queries and research papers as inputs for relevance assessment. SciMON (Wang et al.,


- 2024b) iteratively compares generated plans to retrieved prior papers, triggering replanning until sufficient novelty differentiation is achieved. For longduration quantum computing experiments, k-agents (Cao et al., 2024) determines whether the instruction should be translated using a specific experiment class based on previous analysis as context, helping to avoid hallucinations. VirSci (Su et al.,


- 2024) defines scientist agents with personal information (name, role, affiliation, research interests, citation situation, collaboration history) serving as context for collaborative idea generation. STELLA (Jin et al., 2025) implements of self-evolving mechanisms consisting of a dynamic Template Library and an expandable Tool Ocean, enabling it to continuously expand its knowledge and skills, acting as a dynamic scientific partner, which persistently provides context for better planning.


Contextual prompting improves accuracy and reproducibility but also presents challenges in information selection and coherence management. Overly large or noisy contextual windows may dilute the model’s focus, leading to inconsistencies or factual drift.

#### (3) P3. Deliberative / Reflective Planners

Deliberative or reflective planners augment basic task decomposition with self-evaluation mechanisms, enabling iterative plan refinement through explicit critique and revision cycles. These plan-

ners generate initial plans then invoke reflection stages that assess plan quality, identify potential flaws or gaps, and regenerate improved versions. This mirrors scientific practice where researchers iteratively refine experimental designs through critical self-assessment before execution.

Operationally, reflective planners implement multi-turn workflows alternating between plan generation and plan critique. After producing an initial task decomposition, the planner receives metaprompts such as "Evaluate this experimental plan for logical consistency and feasibility" or "Identify potential failure modes and revise accordingly." Critique outputs inform subsequent plan generation rounds, creating refinement loops that continue until quality thresholds are met or iteration limits are reached. This self-supervision mechanism enables plan improvement without external feedback, though it operates within the constraints of the LLM’s own evaluation capabilities. Implementations vary by reflection mechanism: chainof-thought self-reflection for iterative idea and plan refinement (Lu et al., 2024a; Yamada et al., 2025; Gottweis et al., 2025; Novikov et al., 2025; Xin et al., 2024; Alber et al., 2025; Ansari et al.,

- 2024; Zhang et al., 2024a; Jia et al., 2024; Chen

- et al., 2023; Jaiswal et al., 2024; Darvish et al.,

2025; Zhang et al., 2025e; Wang et al., 2024b; Su

- et al., 2024); error-driven replanning where execution failures trigger plan revision cycles (Ye et al., 2023b; Liu et al., 2024b; Panapitiya et al.,
- 2025; Roohani et al., 2024; McNaughton et al.,




- 2024; Tang et al., 2025d; Kang and Kim, 2024; Peng et al., 2023; Maranto, 2024; Li et al., 2024d; Yang et al., 2024b; Sun et al., 2024b; Hu et al.,
- 2025b; Pandey et al., 2025; Feng et al., 2025a; Ma et al., 2024a); explicit reflection stages with dedicated critique prompts requiring assessment before proceeding (Tang et al., 2025d; Kang and Kim, 2024; Sprueill et al., 2024; Roohani et al., 2024; Ansari et al., 2024); and VLM-based reflection for multi-modal plan evaluation (Yamada et al., 2025).


Representative implementations demonstrate diverse strategies. LLMatDesign (Jia et al., 2024) applies self-reflection on its previous materials design decisions, enabling to adapt rapidly to new tasks and conditions in a zero-shot manner. dZiner (Ansari et al., 2024) iteratively reviews modified materials and modification history using chain-ofthought reasoning, stopping when convergence criteria (no further improvements or maximum iterations) are met, with human chemists able to provide

feedback for refinement. Similarly, AtlasAgent (Yin et al., 2025) applies chain-of-thought reasoning with few-shot and zero-shot prompting for systematic evaluation of batch correction quality, biological signal preservation, and over-correction risks, to accelerate atlas-scale single-cell integration evaluation. MoRA (Jaiswal et al., 2024) introduces Mixture of Refinement Agents framework iteratively refining solutions through two-step processes: advanced models identify errors using flags and scores, then prioritized agent routing activates appropriate agents to address specific errors progressively. OriGene (Zhang et al., 2025e) implements self-evolving mechanisms where agents continuously refine experimental strategies based on prior outcomes. VirSci (Su et al., 2024) employs team discussion with iterative inter- and intrarefinement dialogues, with novelty assessment requiring agents to compare ideas with related papers and vote with reasoning. CellForge (Tang

- et al., 2025d) orchestrates graph-structured debates where Design agents propose, Critics review and score, requiring revisions until consensus emerges. OpenFOAMGPT 2.0 (Feng et al., 2025a) create self-correcting simulation loops with error-driven iterative refinement through Configuration Generation, Automated Execution Management, and Error-Driven Refinement modules.


Deliberative planning enhances plan robustness and reduces execution failures from poorly conceived task decompositions. However, reflection quality depends on the LLM’s introspective capabilities—planners may fail to identify flaws requiring domain expertise or empirical validation beyond linguistic evaluation.

#### (4) P4. Search-Based Planners

Search-based planners reformulate plan generation as exploration over plan spaces, systematically generating and evaluating multiple candidate plans before selecting optimal solutions. By adopting Tree-of-Thought (ToT) (Yao et al., 2023a), Monte Carlo Tree Search (MCTS), or beam search algorithms, these planners treat planning as sequential decision-making under uncertainty, expanding promising plan branches while pruning low-quality alternatives.

Mechanistically, search-based planners construct search trees where nodes represent partial plans and edges represent plan extensions (adding subtasks, refining task parameters). The planner generates multiple alternative extensions at each node, evaluates them using heuristic scoring functions or

learned value models, and selectively expands highscoring branches (Yamada et al., 2025; Sprueill et al., 2024; Chen et al., 2024a; Team et al., 2025a; Sun et al., 2024b; Ma et al., 2024a). This enables systematic exploration of diverse planning strategies, with evaluation signals guiding search toward high-quality solutions.

For example, ChemReasoner (Sprueill et al., 2024) constructs a hierarchical search tree where each node embodies a distinct hypothesis generated through “query plans” that include catalyst type, inclusion/exclusion criteria, and relational operators. The planner then uses quantumchemical feedback—derived from atomistic simulations evaluating adsorption energies, reaction energy barriers, and structural stability—to assign rewards that prune unpromising pathways and iteratively refine the hypothesis space. Similarly, AI Scientist-v2 (Yamada et al., 2025) implements agentic tree-search for experimental planning, with an experiment manager coordinating expansion across four defined stages (Preliminary Investigation, Hyperparameter Tuning, Research Agenda Execution, Ablation Studies). At each stage, the planner generates multiple candidate experimental plans, executes them in parallel, evaluates results (including VLM-assessed figure quality), and selects best-performing nodes for further expansion—effectively searching through experimental design space. CheMatAgent (Wu et al., 2025) proposes a similar Hierarchical Evolutionary Monte Carlo Tree Search (HE-MCTS) framework that decouples tool planning (Policy Model) and execution (Execution Model) for respective optimization. In InternAgent (Team et al., 2025a), the idea innovation agent can first generate ideas and then evolve the generated ideas in an iterative manner, employing a hierarchical idea evolution tree. Similarly, Mephisto (Sun et al., 2024b) conducts deliberate reasoning via tree search, accumulates knowledge through self-play, and dynamically updates its knowledge base. SGA (Ma et al., 2024a) integrates search with scientific simulators: the planner generates alternative experimental designs, simulates outcomes for each branch, and expands only physically plausible plans, using simulation feedback as search guidance. Che Hierarchical Evolutionary Monte Carlo Tree Search (HE-MCTS) framework, enabling independent optimization of tool planning and execution. GeoAgent (Chen et al., 2024a) integrates LLMs with MCTS to facilitate dynamic adjustments during task programming for geospa-

tial data analysis, which employs beam search combined with execution filtering in child node sampling and prompt updating throughout the MCTS expansion process, and incorporates a comprehensive error traceback and analysis mechanism to dynamically refine each subtask.

Search-based planning enables systematic exploration of plan spaces and principled selection among alternatives through explicit evaluation. However, it incurs high computational costs from generating and evaluating multiple candidates, requires effective evaluation functions to guide search, and faces scalability challenges in highdimensional plan spaces.

#### (5) P5. Role-Interactive / Multi-Agent Prompting

Role-interactive planners distribute plan generation across multiple distinct LLM agent instances with specialized functions, implementing planning as collaborative dialogue where planner agents propose task decompositions, critic agents identify flaws, and executor agents provide feasibility feedback. This architecture mirrors scientific team dynamics where researchers with different expertise collectively design experiments through iterative discussion and consensus-building. Unlike A1 where a single agent follows a schema under one persona, A4 employs multiple agents each with different functional responsibilities that interact to co-construct plans.

These planners implement structured communication protocols defining how agents exchange plan proposals, critiques, and revisions. Each separate agent instance operates under role-specific prompts establishing its unique planning responsibilities—a planner agent might focus on highlevel task decomposition, a domain expert agent on scientific validity, and a resource agent on experimental feasibility. Plans emerge from multiturn dialogues where proposals are iteratively refined through distributed critique until consensus is reached. Implementations vary by agent architecture: supervisor-coordinated multi-agent teams with specialized sub-agents for different planning subtasks (Gottweis et al., 2025; Tang et al., 2025a; Panapitiya et al., 2025; Mandal et al., 2024; Pham

- et al., 2025; Inoue et al., 2024; Zou et al., 2025; Yue et al., 2025; Huang et al., 2024c; Noh et al.,


- 2025; Ni and Buehler, 2024; Tang et al., 2023; Hu et al., 2025a; Bazgir et al., 2025; Pu et al.,


- 2025; Lai and Pu, 2025; Ghareeb et al., 2025; Ghafarollahi and Buehler, 2025; Liu et al., 2024b; Su


- et al., 2024); stage-specific planning agents coordinating across experimental phases (Yamada et al., 2025; Liu et al., 2024c; Team et al., 2025a); collaborative debate frameworks with domain expert agents proposing and critiquing plans until consensus (Kumbhar et al., 2025; Tang et al., 2025d; Yin et al., 2025; Roohani et al., 2024; Su et al., 2025; Zhang et al., 2025a; Xiao et al., 2024; Alber
- et al., 2025; Song et al., 2025; Sun et al., 2024b; Darvish et al., 2025; Ghafarollahi and Buehler, 2024b; Polat et al., 2025); and distributed role systems where planner-critic-executor roles interact (Novikov et al., 2025; Saeedi et al., 2025; Ghafarollahi and Buehler, 2024a; Xue et al., 2024; Ni et al., 2024; Feng et al., 2025a; Pantiukhin et al., 2025; Baek et al., 2024).


Representative implementations demonstrate collaborative architectures. AI co-scientist (Gottweis et al., 2025) designs specialized agents, each equipped with customized instruction prompts, are designed to execute these sub-tasks. These agents operate as workers coordinated by the Supervisor agent. Foam-Agent (Yue et al., 2025) comprises four agents in cyclical workflow: Architect Agent interprets requirements and plans simulation structure, Input Writer Agent generates configuration files, Runner Agent executes OpenFOAM simulations, and Reviewer Agent analyzes errors proposing corrections—automating complex CFD workflows through role specialization. IR-Agent (Noh et al., 2025) employs three specialized sub-agents: Table Interpretation Expert performs table-guided absorption analysis extracting local structural information from IR spectra, Retriever Expert identifies similar spectra from databases providing global contextual information, and Structure Elucidation Expert integrates both analyses for final molecular structure prediction—each contributing complementary knowledge. LLM-RDF (Ruan et al., 2024) comprises six specialized agents (Literature Scouter, Experiment Designer, Hardware Executor, Spectrum Analyzer, Separation Instructor, Result Interpreter) pre-prompted for designated chemical synthesis tasks, with Experiment Designer transforming natural language procedures into standardized execution protocols and Hardware Executor generating running codes for automation platforms. MechAgents (Ni and Buehler, 2024) designs a two-agent team demonstrating the benefits of self-correction via continuous conversation in solving mechanics problems, and a group of agents that play the roles of the administrator (ad-

min), the planner, the scientist, the engineer, the executor, the critic and the group-chat manager, for autonomous, interactive and dynamic group chatting. MedAgents (Tang et al., 2023) leverages role-playing with five critical steps: gathering domain experts, proposing individual analyses, summarizing into reports, iterating discussions until consensus, and making decisions. TAIS (Liu et al.,

- 2024a) comprises simulated roles (project manager, data engineer, domain expert, statistician, code reviewer) collaborating through ’Write–Run–Audit’ and ’Consultative Coding’ patterns, to replicate the tasks typically performed by data scientists. VirSci (Su et al., 2024) defines scientist agents with personal information (name, role, affiliation, research interests, citation situation, collaboration history), implementing team discussion with interand intra-refinement dialogues and novelty voting with reasoning. xChemAgents (Polat et al.,
- 2025) uses cooperative agents: Selector adaptively identifies weighted descriptor subsets with natural language rationale, and Validator enforces physical constraints (dimensional consistency, scaling laws) through iterative dialogue (up to three rounds) before validated features pass to GNN. El Agente (Zou et al., 2025) implements hierarchical multi-agent architecture where higher-level computational chemistry agents handle strategic planning while mid-level agents (geometry, quantum calculation, file I/O modules) manage execution details, responding with summarized feedback. Besides, Robin (Ghareeb et al., 2025), STELLA (Jin et al., 2025), ProtAgents (Ghafarollahi and Buehler,


- 2024b), and InternAgent (Team et al., 2025a) also employ various orchestration and closed-loop coordination architectures.


Multi-agent planning provides robust plan generation through distributed expertise and crossvalidation. However, it introduces coordination complexity, potential communication overhead from multi-agent dialogues, and challenges in achieving consensus when agents propose conflicting plans.

#### (6) P6. Programmatic Plan Synthesis (Code / DSL / DAG)

Programmatic planners generate plans as executable artifacts—source code, domain-specific languages (DSLs), or directed acyclic graphs (DAGs)—rather than natural language task descriptions. These plans explicitly encode task dependencies, control flow, and execution parameters in machine-interpretable formats, enabling direct

execution by downstream systems and ensuring precise, reproducible workflow orchestration.

The planning process involves translating highlevel research goals into formal plan representations. Implementations vary by representation formalism: DSL-based plans using domain-specific grammars to encode experimental operations (Liu et al., 2024c; Darvish et al., 2025); executable code plans generating Python scripts following API specifications (Novikov et al., 2025; Ye et al., 2023b; Huang et al., 2025a; Chen et al.; Ma et al.,

- 2024a); and structured symbolic plans producing reaction trees or calculation workflows (Liu et al., 2024c; Novikov et al., 2025; Ye et al., 2023b; Darvish et al., 2025; Ma et al., 2024a).

AIGS (Liu et al., 2024c) generates plans in DSL format where PROPOSALAGENT produces DSL expressions with pre-defined grammars encoding experimental parameters, methodology, experiment settings, and hypotheses, which EXPAGENT interprets into executable code—bridging high-level scientific planning and low-level experimental execution. ORGANA (Darvish et al.,

- 2025) employs CLAIRify to convert natural language chemistry experiment descriptions into XDL (XML-based chemical description language) structured codes using iterative prompting to guarantee syntactic validity, with PLANNER using PDDLStream for structured planning—combining DSL and DAG approaches. K-Dense Analyst (Li et al., 2025b) designs dual-loop architecture comprising a planning Loop and an implementation loop to achieve autonomous bioinformatics analysis. The implementation loop incorporates a coding planning agent to convert high-level analysis step to executable task blocks. AlphaEvolve (Novikov et al., 2025) orchestrates LLM pipelines where planners generate code modifications (diffs) directly altering programs, with each plan representing concrete algorithmic changes evaluated through execution in asynchronous computational pipelines—discovering novel algorithms like improved matrix multiplication searches. SGA (Ma et al., 2024a) generates plans as Python code snippets describing constitutive equations or molecular designs interfacing with physics simulators, using bilevel optimization pairing LLM-generated ideas with simulator-validated implementations. Chemist-X (Chen et al.) generates Python code for database searches, CAD tool operation via API programming, and auto-lab equipment control scripts (e.g., using ‘pyautogui‘ for robotic control), em-


ploying in-context learning with exemplar codes. Biomni (Huang et al., 2025a) prompts LLMs to generate numbered bullet-list plans then generates code executing in Python/R/Bash environments, iterating until converging on validated solutions.

Programmatic planning ensures reproducibility through formal plan specifications and enables automated execution without human interpretation. However, it requires planners to master both domain knowledge and programming language semantics, and plan inflexibility can arise from rigid formal representations that cannot easily accommodate runtime adaptations.

#### 2.1.2 Learned Planners

Learned planners internalize planning logic within parameters through training, enabling consistent autonomous decision-making by leveraging learned patterns from expert demonstrations or rewardoptimized exploration rather than relying solely on prompt-specified instructions. We classify learned planners into SFT/Domain-Trained planners and RL/Preference-optimized planners, as illustrated in

- Figure 4


#### (1) L1. SFT / Domain-Trained Planners

SFT and domain-trained planners acquire planning capabilities through training on datasets of expert-generated plans, learning to reproduce domain-specific task decomposition strategies directly from demonstrated examples. By optimizing the model to predict correct planning sequences given task contexts, these planners internalize procedural knowledge—such as standard experimental workflows, typical tool invocation patterns, and domain-specific task orderings.

The training process exposes models to diverse planning scenarios with corresponding expert plans. Implementations vary by domain training: biomedical and biological planning (Mehandru et al., 2025; Thulke et al., 2024); chemical synthesis planning (Wu et al., 2025; Huang et al., 2025c; Zhang et al.,

- 2025d; Ye et al., 2023a; Li et al., 2025a); materials science planning (Chen et al., 2023); astronomy and physics planning (de Haan et al., 2025; Jin et al., 2025); geoscience planning (Feng et al.,


- 2025b; Fu et al., 2025a); mathematical and analytical planning (Gou et al., 2024; Li et al., 2025b;


- Ma et al., 2024b); and interdisciplinary scientific planning (O’Neill et al., 2025).


Concretely, AstroMLab’s AstroSage-Llama-3.170B (de Haan et al., 2025) underwent 168,000 GPU-hours continued pretraining on astronom-

ical literature followed by SFT with reasoning chains integrated into datasets, encoding astrophysical planning patterns (observational strategies, analysis pipelines, hypothesis testing). MatChat (Chen et al., 2023) harnesses LLaMA2-7B enhanced through learning on 13,878 structured material knowledge pieces, employing supervised fine-tuning and reinforcement learning with human feedback, training on 35,675 solution-based synthesis processes from scientific papers. Similarly, based on LLaMA-2-7b, Chemma (Zhang et al., 2025d) derives two stages for model training. Chemma-SFT is developed by fine-tuning LLaMA2-7b with multi-task Q&A datasets for forward prediction, retrosynthesis, and condition generation, while Chemma-RM is trained for reaction optimization using pair-wise ranking Q&A datasets and experimental feedback, leveraging the proximal policy optimization algorithm. ToRA (Gou et al., 2024) integrates tool-augmented reasoning training, learning when and how to invoke mathematical solvers within planning workflows for theorem proving. GeoMinLM (Fu et al., 2025a) trains on 5.16 million words specific to geology and mineral exploration, integrating expert knowledge via knowledge graphs. DrugAssist (Ye et al., 2023a) fine-tunes Llama-2-7B-Chat on over one million instruction-response demonstrations for interactive molecule optimization, while DrugPilot (Li et al., 2025a) fine-tunes a series of small-scale LLMs on tool-calling benchmark construction (TCDD) using LoRA to to enhance LLMs’ specialized capabilities in drug-related tool calling. Besides, GatorTronGPT (Peng et al., 2023) is pre-trained using 277 billion words of mixed clinical and English text with a GPT-3 architecture of 20 billion parameters, which improves biomedical natural language processing for medical research.

Domain-trained planners exhibit stable performance on in-distribution tasks and require minimal prompting once trained. However, they face generalization challenges on out-of-distribution tasks, depend on availability of high-quality training data, and provide limited interpretability into why specific plans are generated.

#### (2) L2. RL / Preference-Optimized Planners

Reinforcement learning (RL) and preferenceoptimized planners acquire planning strategies through interaction with reward signals or human preferences, learning to generate plans that maximize task success rather than merely imitating demonstrations. By incorporating feedback

|RESEARCH GOAL: "Design and synthesize a high-capacity cathode material for Li-ion ba eries (>200 mAh/g, stable for 500+ cycles)"|
|---|


![image 10](Ren et al._2025_Towards Scientific Intelligence A Survey of LLM-based Scientific Agents_images/imageFile10.png)

|INFERENCE User: "Design xxxx" Model: [Directly outputs plan]|
|---|


L2. RL / PreferenceOp mized Planners

TRAINING CORPUS (Ba ery Literature)

|Paper 1: "Li-rich oxides show 250 mAh/g..."<br>Paper 2: "Mg doping improves cycle life to 600..." Dataset: 50k planning trajectories from chemists<br>|
|---|


###### PLANNER POLICY π_θ "Propose: xxx"

Iteration N

|SFT TRAINING (Qwen 2.5 → Battery-Expert-72B) Loss: Minimize Δ(predicted_plan, expert_plan)|
|---|


|INFERENCE User: "Design xxxx" Model: [Directly outputs plan]|
|---|


EXECUTION & EVALUATION Synthesis → Test: Capacity=215 mAh/g, Cycles=480

|PPO/DPO Update|
|---|


REWARD FUNCTION r = (capacity/200)×0.5 + (cycles/500)×0.5 = 0.91

L1. SFT / DomainTrained Planners

![image 11](Ren et al._2025_Towards Scientific Intelligence A Survey of LLM-based Scientific Agents_images/imageFile11.png)

Figure 4: Different types of learned planners of LLM-based scientific agents.

from plan execution outcomes—experiment success rates, hypothesis validity, or human preference judgments—these planners can discover novel planning strategies potentially superior to human expert approaches.

effort optimally across planning stages. STEPDPO (Lai et al., 2024) and Flow-DPO (Deng and Mineiro, 2024) optimize planning paths at step level through direct preference optimization, training planners to generate steps aligned with human or automated preferences—FlowDPO specifically employing online multi-agent DPO for reasoning trajectories. PaSa (He et al., 2025) is optimized with an RL architecture for literature search planning using synthetic dataset AutoScholarQuery, optimizing from paper relevance preference signals. BioScientist Agent (Zhang et al., 2025a) devises an adversarial actor–critic reinforcementlearning algorithm that discovers biologically plausible drug–target–disease pathways, yielding interpretable mechanistic explanations for each prediction. Chemma (Zhang et al., 2025d) trains reward model (Chemma-RM) using RLHF identifying optimal reaction conditions, constructing pair-wise ranking datasets based on varying preference levels determined by reaction performance (yield and selectivity), with active learning iteratively fine-tuning based on wet experiment feedback. CheMatAgent (Wu et al., 2025) trains Process Reward Model (PRM) and Outcome Reward Model (ORM) guiding Hierarchical Evolutionary Monte Carlo Tree Search, with models trained on self-generated trajectories evaluating reasoning steps and final answers surpassing GPT-4o. SciMARL (Bae and Koumoutsakos, 2022) applies multi-agent RL for autonomous scientific exploration in fluid dynamics, enabling collaborative policy optimization through shared simulation outcome rewards. CycleResearcher (Weng et al.,

Training employs reward functions quantifying plan quality: successful experimental outcomes, validated hypotheses, or human preference scores. Through policy optimization algorithms (PPO (Schulman et al., 2017), DPO (Rafailov et al.,

- 2023)), the planner iteratively adjusts its planning strategy to maximize expected rewards. This enables learning from sparse feedback—final experiment outcomes rather than step-by-step supervision—and discovering non-obvious planning strategies through exploration. Implementations vary by optimization approach: reinforcement learning with PPO for complex problem-solving and adaptive planning (Panapitiya et al., 2025; Luong et al.,


- 2024; Bae and Koumoutsakos, 2022); direct preference optimization incorporating human or automated preferences for step-wise planning (Huang


- et al., 2024d; Deng and Mineiro, 2024; Lai et al.,


- 2024; He et al., 2025); reward-based molecular design planning optimizing for chemical properties and synthesis feasibility (Wu et al., 2025; Zhang et al., 2025d; Hu et al., 2024b); and iterative policy refinement from hypothesis validation or experimental outcome feedback (Weng et al.,


- 2025). ReFT (Luong et al., 2024) pioneers RL-


enhanced chain-of-thought optimization where reward signals from correct solutions guide planning depth, learning to allocate computational

- 2025) employs hypothesis validation feedback to refine policies through policy gradients, learning improved experimental design strategies.


RL-based planners can discover innovative planning strategies and adapt to task-specific reward structures. However, they require careful reward function design to avoid misaligned optimization, demand substantial computational resources for training, and face challenges in sample efficiency when rewards are expensive to evaluate.

#### 2.1.3 Discussion

Scientific agent planners exhibit diverse architectural patterns reflecting different planning paradigms. Some implement linear sequential planning suitable for deterministic workflows; others employ hierarchical decomposition mirroring the scientific method’s layered structure from highlevel goals to specific experimental actions. Graphand DAG-based planners explicitly model task dependencies enabling parallel execution and complex workflows. Tree-based search planners explore alternative plans before commitment. Reactive planners dynamically replan based on execution feedback.

A clear trend toward hybrid planning architectures combines multiple paradigms: schema-driven templates provide structural scaffolding, deliberative reflection ensures plan quality, multi-agent collaboration brings diverse expertise, and learned components provide domain-specific efficiency. Systems like AI co-scientist, CellForge, and AutoLabs integrate prompt-based flexibility for interpretability with learned or RL-optimized components for performance, yielding planners that balance transparency, adaptability, and effectiveness.

As scientific agents evolve toward autonomous, long-running research programs, planning architectures must advance beyond current task-specific designs toward general scientific planning capabilities supporting open-ended discovery, multitimescale coordination (from immediate experiments to long-term research programs), and adaptive replanning under uncertainty—ultimately determining whether LLM-based agents can achieve the methodological sophistication of human scientists in orchestrating complex scientific investigations.

#### 2.2 Memory

Memory in LLM-based scientific agents extends beyond simple context retention, enabling long-

term accumulation of research findings, iterative hypothesis refinement, and cross-project continuity. By mirroring the cognitive processes of human scientists, these agents maintain detailed historical context, integrate domain-specific external knowledge, and leverage intrinsic model capabilities to ensure that each experiment or literature insight informs future decisions. Memory serves as the epistemic foundation determining whether agents can synthesize cross-disciplinary insights, avoid redundant exploration, and build upon prior discoveries. We categorize these memory mechanisms into three major types: Historical Context as in

- subsection 2.2.1, External Knowledge Base as in
- subsection 2.2.2, and Intrinsic Knowledge as in
- subsection 2.2.3 — three facets that collectively address the timeline-driven nature of scientific inquiry, the breadth of specialized data sources, and the deep, model-level understanding required for advanced tasks. While not mutually exclusive, each category highlights a distinct dimension of how scientific agents store and utilize information to reproduce results, accumulate evidence, and push the boundaries of autonomous research. We compare the three mechanisms in Table 1 and illustrate them in Figure 6. We also list the related studies in Figure 5.


#### 2.2.1 M1. Historical Context

Historical context—encompassing both short-term contextual memory and long-term persistent storage—is vital for scientific agents to maintain continuity and iterative progress in research workflows. Unlike general agents that merely hold transient dialogue, scientific agents accumulate and leverage past interactions, experimental outcomes, and reasoning steps to refine hypotheses and improve experiment designs over time. This robust memory enables them to mimic the cumulative nature of scientific inquiry, ensuring each cycle of analysis builds on previous insights and supports reproducible results. Historical context spans a spectrum from volatile session-specific memory residing in the LLM’s active context window to durable crosssession archives stored in persistent databases or files, with sophisticated agents employing hybrid approaches that balance immediate accessibility for real-time decision-making against long-term retention for cumulative learning.

Mechanistically, historical context operates through two complementary patterns. Most scientific agents rely on within-session memory residing

AI Scientist (Lu et al., 2024a), AI Scientist-v2 (Yamada et al., 2025), AIGS (Liu et al., 2024c), AtomAgents (Ghafarollahi and Buehler, 2024a), BioDiscoveryAgent (Roohani et al., 2024), CellAgent (Xiao et al., 2024), MLR-Copilot (Li et al., 2024d), LLMatDesign (Jia et al., 2024), MedAgents (Tang et al., 2023), MetaAgent (Hu et al., 2025a), STELLA (Jin et al., 2025), etc

M1. Historical Context

AccelMat (Kumbhar et al., 2025), BiomedRAG (Li et al., 2024c), Agent Laboratory (Schmidgall et al., 2025), BioScientist Agent (Zhang et al., 2025a), Coscientist (Boiko et al., 2023), DrugAgent (Inoue et al., 2024), Foam-Agent (Yue et al., 2025), GeoSim.AI (Bekele, 2025), OpenFOAMGPT (Pandey et al., 2025), ResearchAgent (Baek et al., 2024), SciAgents (Ghafarollahi and Buehler, 2024c), VirSci (Su et al., 2024), etc

M2. External Knowledge Base

Memory

ChemDFM (Zhao et al., 2025), MatChat (Chen et al., 2023), GeoMinLM (Fu et al., 2025a), AstroMLab (de Haan et al., 2025), NatureLM (Xia et al., 2025b), Chemma (Zhang et al., 2025d), ToRA (Gou et al., 2024), ProLLaMA (Lv et al., 2024), MOOSE-Chem (Yang et al., 2024b), Tx-LLM (Chaves et al., 2024), Agent Laboratory (Schmidgall et al., 2025), etc

M3. Intrinsic Knowledge

- Figure 5: Taxonomy of the memory mechanism of representative scientific agents with M1: Historical Context, M2: External Knowledge Base, M3: Intrinsic Knowledge


|RESEARCH GOAL: "Design and synthesize a high-capacity cathode material for Li-ion ba eries (>200 mAh/g, stable for 500+ cycles)"|
|---|


M1 Historical Context

|Former reasoning chains: "Try Mg-doping→coat surface"; "Reject Co-rich→choose Mn-base"|
|---|


![image 12](Ren et al._2025_Towards Scientific Intelligence A Survey of LLM-based Scientific Agents_images/imageFile12.png)

Prev. trials: NMC-811 fades @400 cycles; LFP stable but only 160 mAh/g

Experimental results

Multi-agent review archives: Safety critic flagged Ni4+ risk; Cost critic warned Co price spike; Synthesis critic noted O2 sensitivity

![image 13](Ren et al._2025_Towards Scientific Intelligence A Survey of LLM-based Scientific Agents_images/imageFile13.png)

Review agents

###### (Stored in local session RAM + persisitent record)

|M2 External Knowledge Base<br><br>|Papers: Paper 2024: "Li-rich Mn-based delivers 250 mAh/g with 600 cycles (DOI:10.1000/abc) .."|
|---|
<br><br>|MatSci KB snippets: Li2MnO3 σ=1.2 mS/cm, Voltage window 2.0-4.8 V vs Li|
|---|
<br><br>|Search results: Query: "Mn-rich cathode coating"<br><br>→10 hits→extract MgAl2O4 coating data|
|---|
<br><br>(Provided with RAG-augmented prompt)|
|---|


![image 14](Ren et al._2025_Towards Scientific Intelligence A Survey of LLM-based Scientific Agents_images/imageFile14.png)

Papers & KBs & Patens & ...

Let me see ...

![image 15](Ren et al._2025_Towards Scientific Intelligence A Survey of LLM-based Scientific Agents_images/imageFile15.png)

![image 16](Ren et al._2025_Towards Scientific Intelligence A Survey of LLM-based Scientific Agents_images/imageFile16.png)

Web search results

Planner

###### M3 Intrinsic Knowledge

Battery chemistry rules, crystal-field theory, voltage-capacity relations,

![image 17](Ren et al._2025_Towards Scientific Intelligence A Survey of LLM-based Scientific Agents_images/imageFile17.png)

......

Pre-trained or SFT or RL Training

(Encoded in Transformer weights)

###### Figure 6: Different types of memories of LLM-based scientific agents.

Table 1: Comparison of different memory types

|Type|Methodology<br><br>|Strengths and Limitations<br><br>|Typical Use Cases|
|---|---|---|---|
|Historical Context<br><br>|Maintains conversational logs or iterative action sequences; stores previous interactions and experimental outcomes<br><br>|✓ Enables coherent iterative refinement<br><br>✓ Supports dynamic adaptation × Limited by model’s context window × Explicit retrieval challenging<br><br>|Iterative hypothesis refinement, tracking multi-turn research sessions, adapting strategies from previous interactions|
|External Knowledge Base<br><br>|Accesses curated external sources such as literature databases and structured knowledge graphs|✓ Expansive, up-to-date domain information<br><br>✓ Reasoning in validated research × Integration complexity × Dependent on source quality|Comprehensive literature reviews, retrieving domain-specific data<br><br>|
|Intrinsic Knowledge|Inherent capabilities from pre-training and fine-tuning|✓ Robust foundation for language understanding<br><br>✓ Immediately available × May become outdated × Limited by training data scope<br><br>|General scientific reasoning, initial hypothesis generation, foundational tasks|


in the LLM’s context window (4K-128K tokens), accumulating conversational turns, tool outputs, intermediate results, and reflective annotations during active execution, enabling agents to track iterative hypothesis refinement (Kumbhar et al., 2025; Liu et al., 2024c; Lu et al., 2024a; Yamada et al.,

- 2025; Roohani et al., 2024; Sprueill et al., 2024; Weng et al., 2025; Ansari et al., 2024; Zhang et al.,


- 2025e; Lai and Pu, 2025; Jin et al., 2025), preserve intermediate analytical results across multistep pipelines (Xia et al., 2025a; Xin et al., 2024; Huang et al., 2025a; Xiao et al., 2024; Alber et al., 2025; Chen et al., 2024a; Team et al., 2025a; Li


- et al., 2025b; Zhang et al., 2025b), maintain error traces for self-optimization (Schmidgall et al., 2025; Novikov et al., 2025; Wu et al., 2025; Pham


- et al., 2025; Huang et al., 2025c; Yue et al., 2025; Chen et al., 2024a; Ni and Buehler, 2024; Riffle et al., 2025; Pandey et al., 2025; Pantiukhin et al., 2025), record multi-agent communications (Liu et al., 2024c; Gottweis et al., 2025; Ghafarol-


- lahi and Buehler, 2024a; Tang et al., 2025d; Song et al., 2025; Team et al., 2025a; Tang et al., 2023; Sun et al., 2024b; Hu et al., 2025a; Ghafarollahi and Buehler, 2024c, 2025; Su et al., 2024; Cao et al., 2024), and manage tool states (Mandal et al.,


- 2024; Liu et al., 2024b; McNaughton et al., 2024; Bran et al., 2024; Chen et al.; Boiko et al., 2023;

- Huang et al., 2024a; Inoue et al., 2024; Feng et al.,


- 2025b; Zou et al., 2025; Jin et al., 2024; Huang et al., 2025b; Zhang et al., 2024a; Noh et al., 2025; Maranto, 2024; Zhou et al., 2025; Ni et al., 2024; Li et al., 2024d; Yu et al., 2024; Jaiswal et al., 2024; Bazgir et al., 2025; Kumar et al., 2023; Hu et al., 2025b; Pu et al., 2025; Ghafarollahi and Buehler,


- 2024b; Baek et al., 2024; Ghareeb et al., 2025; Ma


- et al., 2024a,b; Wang et al., 2025a; Liu et al., 2024a;


Gou et al., 2024). Advanced systems additionally implement across-session persistent storage with explicit evidence of cross-session retention: solution archives storing validated programs or successful protocols as reusable exemplars (Schmidgall et al., 2025; Lu et al., 2024a; Novikov et al., 2025), experience replay buffers for RL-based learning from past trajectories (Hu et al., 2024b; Luong et al., 2024; Ma et al., 2024a), and state persistence enabling restoration across application relaunches (Ye et al., 2023b).

Representative implementations illustrate the spectrum of historical context strategies. CellAgent (Xiao et al., 2024) implements a distinctive dual-layer architecture: local memory retains stepspecific dialogue including each code snippet (correct or incorrect), error messages, and optimization processes, resetting when subtasks end while enabling perception of the entire self-optimization process; global memory stores only final successfully executed code from each historical step, allowing the Executor to reference proven solutions across the agent’s operational lifespan. AIGS (Liu et al., 2024c) demonstrates multi-turn log management in its Pre-Falsification phase where iterative exchanges between PROPOSALAGENT, EXPAGENT, and REVIEWAGENT are explicitly used as history context to refine proposals, with FALSIFICATIONAGENT accessing all history records to synthesize final discoveries. AI Scientist (Lu et al., 2024a) implements a self-expanding knowledge archive that iteratively develops ideas and adds them to a growing persistent repository, mimicking cumulative knowledge building in the scientific community, with generated papers and reviewer feedback stored across sessions enabling future idea generations to build upon accumulated

research output. BioDiscoveryAgent (Roohani et al., 2024) and MLR-Copilot (Li et al., 2024d) exemplify experimental feedback integration, constructing prompts that include results from all previous experimental rounds to maintain consistent strategies, with BioDiscoveryAgent additionally implementing context summarization when token limits are exceeded. AtomAgents (Ghafarollahi and Buehler, 2024a) provides dedicated memory modules distinguishing "core memory" (storing conversations between core agents and tool responses throughout problem-solving) from "tool memory" (storing intra-tool agent conversations with summaries returned to core upon task completion), ensuring structured historical data accessibility. Agent Laboratory combines structured contextual buffers for immediate context with persistent top-performing program collections employing top program sampling and replacement strategies, curating a database of successful coding solutions guiding future generation. MedAgents (Tang et al.,

- 2023) and MetaAgent (Hu et al., 2025a) exemplify collaborative historical context where multi-agent discussions build shared understanding: MedAgents uses iterative clinical consultations where specialized roles (attending physician, pharmacist, radiologist, pathologist) progressively build upon each other’s observations to reach consensus diagnoses, while MetaAgent’s cerebrum component maintains dialogue history coordinating electromagnetic field manipulation strategies across specialized agents. LLMatDesign (Jia et al., 2024) incorporates self-reflection on previous design decisions, preserving commentary on each modification’s success or failure and incorporating it into subsequent prompts, enabling rapid zero-shot adaptation to new material design tasks by consolidating insights from prior cycles. STELLA (Jin et al.,


2025) employs self-evolving memory consolidating successful experimental strategies, validated hypotheses, and effective tool usage patterns across biomedical research cycles, while AI Scientist-v2 (Yamada et al., 2025) maintains rich experimental node states (script, plan, error trace, metrics, VLM feedback) in agentic tree search with the Experiment Progress Manager selecting best-performing nodes for subsequent stages.

Historical context excels in maintaining procedural continuity, enabling rapid iteration, and supporting self-improvement through accumulated experience. However, within-session memory faces finite context window constraints where critical

early information may be truncated as complexity increases, while persistent memory faces consolidation challenges determining what merits long-term retention and efficiently retrieving relevant insights from growing archives—necessitating complementary external knowledge bases and intrinsic knowledge for long-horizon discovery.

#### 2.2.2 M2. External Knowledge Base

External knowledge bases (KBs) are essential for scientific agents, providing a curated repository of up-to-date, domain-specific information that extends beyond the static training data of LLMs and the limitations of active context windows. These KBs are not merely supplemental—they are deeply integrated into the agent’s reasoning process through retrieval-augmented generation (RAG), enabling agents to retrieve, synthesize, and connect complex scientific concepts. This external integration is critical for tasks that demand indepth domain expertise and comprehensive literature awareness. By systematically incorporating external knowledge, scientific agents can enhance hypothesis generation, experimental design, and data analysis, ensuring that their outputs remain current, robust, and contextually relevant. External knowledge is particularly vital for scientific agents because required knowledge is often highly specialized (found only in domain-specific databases or recent publications), rapidly evolving (new discoveries constantly update the factual landscape), or too voluminous to encode entirely within model parameters (comprehensive databases of chemical properties, genomic sequences, or astronomical observations), requiring external retrieval mechanisms to access authoritative, current information without the prohibitive cost and latency of continuous model retraining.

Mechanistically, external knowledge bases integrate into agent workflows through query-driven retrieval processes combining semantic search and structured querying with context integration. First, agents formulate queries from task requirements—extracting keywords, generating semantic descriptions, or constructing database queries—then submit to external systems returning ranked results via embedding-based similarity (vector databases), logical filtering (knowledge graphs, relational databases), or relevance scoring (literature APIs). Second, retrieved content—document passages, knowledge graph triples, database records, full articles—is injected into

active context, reformatted as natural language background, structured tables, or procedural examples augmenting prompts for subsequent reasoning. This bridges the gap between limited internal representations and vast external repositories encoding collective scientific knowledge. Implementation patterns vary by knowledge source type: scientific literature retrieval where agents employ RAG with literature databases, querying scholarly repositories like arXiv, PubMed, Semantic Scholar, INSPIRE-HEP, or Google Scholar to access publications, abstracts, and methodological precedents, grounding reasoning in existing research and enabling agents to assess novelty, contextualize findings, and build upon established work (Moss, 2025; Lu et al., 2024a; Yamada et al.,

- 2025; Tang et al., 2025a; Schmidgall et al., 2025; Novikov et al., 2025; Saeedi et al., 2025; Mehandru et al., 2025; Roohani et al., 2024; Luo et al.,


- 2022; Su et al., 2025; Zhang et al., 2025a; Li et al.,


- 2024c; Tang et al., 2025d,b; Song et al., 2025; Bran


- et al., 2024; Huang et al., 2025c; Sprueill et al.,

- 2024; Chen et al.; Thulke et al., 2024; Li et al.,

- 2024b; Boiko et al., 2023; Xue et al., 2024; Weng


et al., 2025; Inoue et al., 2024; Li et al., 2025a; Huang et al., 2024c; Peng et al., 2023; Jin et al.,

- 2024; Chen et al., 2024a; Huang et al., 2025b; Fu

et al., 2025a; O’Neill et al., 2025; Team et al.,

- 2025a; Zhou et al., 2025; Yang et al., 2024b; Ni and Buehler, 2024; Sun et al., 2024b; Hu et al.,


- 2025a; Darvish et al., 2025; Pantiukhin et al., 2025; He et al., 2025; Lai and Pu, 2025; Ghafarollahi




- and Buehler, 2024b; Baek et al., 2024; Ghareeb et al., 2025; Ma et al., 2024b; Ghafarollahi and Buehler, 2024c; Wang et al., 2024b; Ghafarollahi
- and Buehler, 2025; Wang et al., 2025a; Liu et al.,


- 2024a; Su et al., 2024); knowledge graphs and structured ontologies where agents query largescale ontological KGs to organize scientific concepts, extract drug-target interactions, navigate biological pathways, or explore materials relationships, ensuring generated hypotheses are rooted in interconnected validated scientific knowledge (Zhang et al., 2025a; Inoue et al., 2024; Ghafarollahi and Buehler, 2024c; Su et al., 2024) or employ GNN models combined with LLM-driven agents to rapidly predict material properties and explore compositional spaces, with knowledge embedding enabling efficient traversal and link prediction for discovering novel relationships (Kumbhar et al.,
- 2025; Ghafarollahi and Buehler, 2024a; Xin et al.,


- 2024; Huang et al., 2025a, 2024a; Kang and Kim,


- 2024; Zhang et al., 2025d; Zou et al., 2025; Bekele,
- 2025; Zhang et al., 2024a; Noh et al., 2025; Li et al., 2025b; Ning et al., 2025; Ruan et al., 2024; Ni et al., 2024; Yu et al., 2024; Bazgir et al., 2025; Pandey et al., 2025; Feng et al., 2025a; Gou et al., 2024; Ansari et al., 2024; Cao et al., 2024); and diverse specialized resources including web search capabilities for browsing internet and relevant documentation (Boiko et al., 2023), curated geospatial data sources like OpenStreetMap and US Census data for autonomous geospatial retrieval (Ning et al., 2025), dynamically updated astronomical knowledge bases where domain knowledge is continuously extracted and validated (Sun et al., 2024b), and entity-centric knowledge stores built from literature co-occurrences capturing underlying relationships to facilitate cross-pollination of ideas (Baek et al., 2024).


Representative implementations demonstrate versatile external knowledge integration. BiomedRAG (Li et al., 2024c) develops a tailored chunk scorer trained using LLM scores as supervision to select the most relevant documents from a specifically curated diverse chunk database, improving retrieval quality by adapting the retriever to assist predictions—representing sophisticated literature RAG optimization. ResearchAgent (Baek et al.,

- 2024) builds an "entity-centric knowledge store" from literature co-occurrences to capture underlying relationships and facilitate cross-pollination of ideas, while Agent Laboratory (Schmidgall et al.,
- 2025) illustrates straightforward literature utilization through the arXiv API for retrieving abstracts and full texts during literature review and report writing phases. BioScientist Agent (Zhang et al., 2025a) unifies a billion-fact biomedical knowledge graph (RTX-KG2) integrating DrugBank, ChEMBL, Gene Ontology, UniProt, and HMDB, using it for representation learning through variational graph auto-encoder training, link prediction, and path traversal via adversarial actor-critic RL to recover mechanistic paths, additionally querying PubMed for entity co-occurrences filtered to extract causal sentences—exemplifying comprehensive KG-based reasoning. SciAgents (Ghafarollahi and Buehler, 2024c) reasons over ontological knowledge graphs to ensure hypotheses are rooted in interconnected scientific relationships, while DrugAgent (Inoue et al., 2024)’s Knowledge Graph Agent extracts drug-target interactions from biomedical KGs for domain-specific querying. AccelMat (Kumbhar et al., 2025) integrates


MatKG, the largest materials science knowledge graph, querying it with keywords from experimental goals to retrieve empirical property data enriching hypothesis generation. Coscientist (Boiko et al.,

- 2023) integrates diverse resources combining Web Searcher for internet browsing with Documentation search using OpenAI’s ada model to embed documentation sections (OT-2 API, ECL functions) and distance-based vector search for operational knowledge access. GeoSim.AI (Bekele, 2025) employs domain-specific RAG with comprehensive geomechanics Knowledge Base and Data & Tools Base guiding simulation input generation, while OpenFOAMGPT (Pandey et al., 2025) embeds OpenFOAM documentation into vector databases enabling dynamic CFD procedural knowledge retrieval. Foam-Agent (Yue et al., 2025) employs multi-agent automation of OpenFOAM CFD workflows with hierarchical multi-index retrieval systems segmenting domain knowledge into specialized FAISS indices for different simulation aspects. VirSci (Su et al., 2024) adopts the KnowledgeBank module embedding scientist agent profiles into an author knowledge bank facilitating collaboration, and Mephisto implements dynamically updated astronomical knowledge bases through continuous extraction and validation.


External KBs provide scalable, dynamically updatable knowledge access incorporating posttraining information, ground reasoning in established scientific knowledge, enhance transparency through source attribution, and reduce hallucinations by anchoring generation in validated facts. Implementation strategies span from RAG-based retrieval from unstructured text to structured KG querying, API integrations, and web browsing. However, challenges include latency from external queries, retrieval quality issues with poorly formulated queries, and context dilution when retrieved content is voluminous or tangentially relevant—necessitating sophisticated filtering and ranking strategies.

#### 2.2.3 M3. Intrinsic Knowledge

In the context of scientific agents powered by Large Language Models, intrinsic knowledge of LLMs serves as the foundational cognitive bedrock. This refers to the inherent capabilities and information that the LLM itself embodies, meticulously cultivated during its pre-training phase on massive and diverse corpora, crucially including scientific literature, datasets, and domain-specific knowl-

edge. This intrinsic knowledge is further refined through task-specific fine-tuning. For a scientific agent, this isn’t merely passive data storage; it’s the very source of an agent’s reasoning faculties, natural language competency, and fundamentally, its foundational scientific understanding. Intrinsic knowledge refers to domain knowledge, procedural patterns, and conceptual representations encoded directly within the model’s neural network parameters—weights, embeddings, attention patterns—enabling domain-fluent outputs, factual recall, reasoning pattern application, and coherent scientific narratives without external queries or limited context window maintenance. The intrinsic knowledge, therefore, empowers a scientific agent to operate effectively within scientific contexts, providing the essential base for scientific reasoning, comprehension of scientific language, representation of scientific concepts (chemical bond theory, biological pathways, physical laws), mastery of domain-specific terminology and notation (chemical formulae, mathematical expressions, genomic nomenclature), command of characteristic reasoning patterns (hypothesis formulation strategies, experimental design principles, analytical methodologies), and the broad scientific literacy required to function as an autonomous scientific explorer and problem-solver.

Mechanistically, intrinsic knowledge operates through distributed representations learned during training, where model parameters implicitly store domain knowledge, reasoning patterns, and conceptual relationships extracted through gradient-based optimization. When agents reason about scientific phenomena, they draw upon these internalized representations to generate coherent hypotheses, interpret results, and structure arguments. Enhancement strategies for building specialized scientific LLMs span: domain-specific pre-training or continued pre-training on specialized scientific corpora to encode domain expertise (de Haan et al., 2025; Luo et al., 2022; Zhao et al., 2025; Peng et al., 2023; Fu et al., 2025a; Chen et al., 2023; Yang et al., 2024b; Xia et al., 2025b); supervised finetuning on domain-specific instruction datasets or structured data for task adaptation (de Haan et al., 2025; Wu et al., 2025; Zhao et al., 2025; Zhang et al., 2025d; Weng et al., 2025; Chen et al., 2023; Chaves et al., 2024); and parameter-efficient or reinforcement learning-based adaptation employing techniques like Low-Rank Adaptation or policy optimization (Wu et al., 2025; He et al., 2025; Luong

- et al., 2024; Lai et al., 2024; Lv et al., 2024). The majority of scientific agents, however, leverage existing foundation models (GPT-4, Claude, Llama, Gemini) without additional training, relying on the models’ general parametric knowledge activated through careful prompting and role specification.


Representative systems illustrate varied approaches to constructing intrinsic knowledge. ChemDFM (Zhao et al., 2025) pioneers domainspecific LLM development through pre-training on 34B tokens from chemical literature and textbooks followed by fine-tuning using 2.7M chemical instructions, enabling free-form chemical dialogue, self-correction in multi-turn interactions, reaction prediction, and reasoning about unforeseen situations—demonstrating comprehensive chemical expertise encoded in parameters. AstroMLab’s AstroSage (de Haan et al., 2025) underwent extensive continued pretraining ( 168,000 GPU-hours) on astronomical literature, with supervised fine-tuning incorporating explicit reasoning chains enabling either immediate answers or step-by-step thought processes, imbuing stellar evolution, cosmological models, and observational techniques into weights. MatChat (Chen et al., 2023) enhances Llama2-7B with structured material knowledge data demonstrating targeted fine-tuning efficacy, while TxLLM (Chaves et al., 2024) distinguishes itself by fine-tuning from PaLM-2 (Anil et al., 2023) on 709 datasets encompassing 66 drug discovery tasks, creating a generalist therapeutics model with broad pipeline coverage. NatureLM (Xia et al.,

- 2025b) adopts multi-domain pre-training on small molecules, materials, proteins, DNA and RNA, offering a unified versatile model across scientific applications rather than single-domain specialization. ProLLaMA (Lv et al., 2024) introduces Low-Rank Adaptation for efficient Protein Language Model fine-tuning, improving learning efficiency while reducing computational requirements. PaSa (He et al., 2025) optimizes an LLM agent for academic search via reinforcement learning with synthetic query-paper datasets. Agent Laboratory (Schmidgall et al., 2025) activates parametric knowledge in GPT-4o/o1 backends through role descriptions ("expert machine learning engineer," "AI researcher reviewing a paper"), while MOOSE-Chem (Yang et al., 2024b) builds chemical memory via multi-modal (SMILES, SELFIES, molecular graphs) pretraining enhancing molecular understanding beyond text-only models.


Intrinsic knowledge provides immediate, zero-

latency access to domain understanding, supports fluent scientific communication, and enables broad generalization across related tasks. Implementation approaches range from full domain-specific pre-training to targeted fine-tuning or parameterefficient techniques. However, critical limitations include knowledge staleness where information is limited by training cutoff dates, lack of source attribution making citation and verification difficult, opacity in knowledge provenance risking hallucinations, and inability to adapt to new discoveries without expensive retraining—motivating combination with external knowledge bases for current information and historical context for task-specific learning.

#### 2.2.4 Discussion

Historical context enables agents to maintain conversational coherence and iterative refinement by retaining and recalling prior interactions, emulating the cumulative nature of human research. External knowledge bases expand the agent’s informational scope by integrating up-to-date and domainspecific data, allowing for retrieval, synthesis, and contextualization of complex scientific concepts. Meanwhile, intrinsic knowledge enables agents to apply core scientific reasoning from the outset, serving as the bedrock for advanced, context-rich memory layers. The most capable agents deliberately employ hybrid architectures combining these mechanisms: AccelMat (Kumbhar et al., 2025) integrates historical context tracking hypothesis refinement cycles, external knowledge bases querying MatKG for materials data, and intrinsic knowledge in GPT-4o/Claude/Gemini for foundational understanding; CellForge (Tang et al., 2025d) combines symbolic memory for history-aware refinement, vector-based retrieval over PubMed/GitHub, and parametric knowledge for domain fluency; BioMaster (Su et al., 2025) maintains local memory for tracking actions, RAG for bioinformatics knowledge, and LLM parametric expertise.

Despite their complementary roles, current memory mechanisms face several limitations. Many approaches—especially those using textual memorysuffer from scalability issues and information loss since context windows are limited. Parametric methods, while more efficient, often lack interpretability and require extensive fine-tuning. Moreover, external knowledge integration remains brittle in dynamically changing domains, leading to potential mismatches or outdated retrievals. Recent

studies (Xu et al., 2025b; Zeng et al., 2024) emphasize the need for more adaptive, self-organizing memory systems that can dynamically link and update stored information. Additionally, improved lifelong learning techniques and efficient forgetting mechanisms are essential to mitigate memory overload and maintain performance over extended research cycles.

#### 2.3 Action Space

The action space defines the set of concrete operations that LLM-based scientific agents can perform to interact with their environment, execute experimental procedures, acquire information, and transform ideas into tangible research outcomes. While planners determine what to do and in what sequence, the action space defines how agents actualize these plans through executable operations that bridge the gap between abstract reasoning and concrete scientific work. In scientific research contexts, actions extend far beyond simple text generation to encompass diverse operational modalities: invoking external computational tools and controlling physical or simulated laboratory equipment, querying knowledge repositories and retrieving information from scientific literature or databases, generating executable code that implements analytical workflows or orchestrates complex pipelines, and performing sophisticated reasoning operations that synthesize information, generate hypotheses, or draw conclusions from evidence. The breadth and sophistication of an agent’s action space fundamentally constrains what research tasks it can accomplish. Based on the nature and purpose of operations, we categorize action types into four major classes: tool use and environmental control

- as in subsection 2.3.1, search and information retrieval as in subsection 2.3.2, code generation and execution as in subsection 2.3.3, and LLM-based reasoning and cognitive actions as in subsection


- 2.3.4. These categories are not mutually exclusive; sophisticated agents typically integrate multiple action types into unified workflows where reasoning informs tool selection, retrieved information guides code generation, and tool execution results feed back into reasoning cycles. We illustrate them in Figure 8 and list the related studies in Figure 7.


#### 2.3.1 T1. Tool Use / Environmental Control

Tool use and environmental control actions enable agents to invoke external computational systems, control physical or simulated experimental

equipment, and manipulate environmental states beyond the LLM’s internal processing. While LLMs demonstrate robust problem-solving capabilities for general tasks and foundational scientific inquiries, they encounter limitations when addressing advanced scientific challenges, particularly those in STEM-related domains, due to insufficient domain-specific expertise and computational resources. Tool sets extend the LLM’s capabilities beyond natural language processing by enabling real-time data retrieval, precise code execution, domain-specific scientific computation, and rigorous experimental simulation. This tight integration allows scientific agents to access accurate, up-to-date information, perform computationally intensive analyses, and process data in specialized modalities—capabilities essential for simulating and validating experiments. Consequently, tool sets serve not just as supplementary resources but as core components of the agent’s architecture, fundamentally enhancing scientific reasoning, reliability, and adaptability in complex research environments. Based on functional types, we categorize tool use into two major classes: tool sets based on APIs and code libraries, and tool sets based on simulators and emulation platforms.

#### (1) Tool Sets Based on APIs and Code Libraries

APIs and code libraries aim to extend the knowledge boundaries and computational capacities of LLMs in scientific tasks by encapsulating domainspecific knowledge bases and specialized algorithm libraries into standardized functional interfaces, enabling LLMs to transcend limitations imposed by training data timeliness, domain depth, and computational constraints. This category encompasses both pre-existing general-purpose tools, disciplinespecific scientific tools, and novel tools synthesized by researchers. Sophisticated multifunctional API integration significantly augments agent capabilities across diverse scientific domains. In mathematics, ToRA (Gou et al., 2024) integrates Python libraries (SymPy, SciPy, CVXPY) into natural language reasoning frameworks, demonstrating significant performance improvements across mathematical reasoning benchmarks by grounding calculations in symbolic computation. In chemistry and materials science, ChemCrow (Bran et al., 2024) deploys 18 expert-designed tools supporting molecular property queries, reaction prediction, and synthesis planning, empowering LLMs to autonomously design and execute complex work-

- T1. Tool Use / Environmen-

tal Control

AI co-scientist (Gottweis et al., 2025), AtomAgents (Ghafarollahi and Buehler, 2024a), ChatMOF (Kang and Kim, 2024), ChemCrow (Bran et al., 2024), CRISPR-GPT (Huang et al., 2024a), dZiner (Ansari et al., 2024), Foam-Agent (Yue et al., 2025), GeneGPT (Jin et al., 2024), HoneyComb (Zhang et al., 2024a), LLMatDesign (Jia et al., 2024), MechAgents (Ni and Buehler, 2024), MyCrunchGPT (Kumar et al., 2023), OpenFOAMGPT (Pandey et al., 2025), ProtAgents (Ghafarollahi and Buehler, 2024b), ToRA (Gou et al., 2024), SciAgent (Ma

et al., 2024b), SGA (Ma et al., 2024a), Sparks (Ghafarollahi and Buehler, 2025), StarWhisper (Wang et al., 2025a), etc

- T2. Search & Informa-


AI Cosmologist (Moss, 2025), BioDiscoveryAgent (Roohani et al., 2024), BioScientist Agent (Zhang et al., 2025a), ClimateGPT (Thulke et al., 2024), DrugAgent (Inoue et al., 2024), FoamAgent (Yue et al., 2025), GeoSim.AI (Bekele, 2025), HoneyComb (Zhang et al., 2024a), PaSa (He et al., 2025), ResearchAgent (Baek et al., 2024), SciMON (Wang et al., 2024b), etc

tion Retrieval

Action Space

- T3. Code Generation & Execution

Agent Laboratory (Schmidgall et al., 2025), AI Scientist (Lu et al., 2024a), AILA (Mandal et al., 2024), AlphaEvolve (Novikov et al., 2025), AmadeusGPT (Ye et al., 2023b), AutoLabs (Panapitiya et al., 2025), BioAgents (Mehandru et al., 2025), Biomni (Huang et al., 2025a), CellAgent (Xiao et al., 2024), SGA (Ma et al., 2024a), MLR-Copilot (Li et al., 2024d), OpenFOAMGPT (Pandey et al., 2025),

- T4. LLM-Based Reasoning / Cog-


AI co-scientist (Gottweis et al., 2025), AI Scientist-v2 (Yamada et al., 2025), AIGS (Liu et al., 2024c), AstroMLab (de Haan et al., 2025), BioDiscoveryAgent (Roohani et al., 2024), CoI (Li et al., 2024b), ChemReasoner (Sprueill et al., 2024), DrugAgent (Inoue et al., 2024), HyperGen (Kumbhar et al., 2025), MedAgents (Tang et al., 2023), OriGene (Zhang et al., 2025e), SciMON (Wang et al., 2024b), etc

nitive Actions

Figure 7: Taxonomy of the action space mechanisms of representative scientific agents: T1 (Tool Use / Environmental Control), T2 (Search & Information Retrieval), T3 (Code Generation & Execution), T4 (LLM-Based Reasoning / Cognitive Actions).

flows in organic synthesis, drug discovery, and materials design; CACTUS (McNaughton et al.,

- 2024) leverages a collection of cheminformatics helper functions that wrap well-known Python libraries into well-described tools for an agent to use; HoneyComb (Zhang et al., 2024a) integrates MatSciKB gathering structured knowledge from literature with ToolHub incorporating search engines, Python interpreters, and domain-specific APIs con-


structed via inductive tool construction methodology. In biology, CRISPR-GPT (Huang et al., 2024a) synergizes Google Search, Primer3, Broad Institute’s guideRNA library, CRISPRPick tool set, and scholarly databases, enabling researchers to select suitable CRISPR systems and design genomeediting protocols. GeneGPT (Jin et al., 2024) proposes to teach LLMs to use the Web APIs of the National Center for Biotechnology Information

RESEARCH GOAL: "Design and synthesize a high-capacity cathode material for Li-ion batteries (>200 mAh/g, stable for 500+ cycles)"

![image 18](Ren et al._2025_Towards Scientific Intelligence A Survey of LLM-based Scientific Agents_images/imageFile18.png)

###### “I can take actions like ...”

T1 Tool Use / Environmental Control

###### T2 Search & Information Retrieval

![image 19](Ren et al._2025_Towards Scientific Intelligence A Survey of LLM-based Scientific Agents_images/imageFile19.png)

![image 20](Ren et al._2025_Towards Scientific Intelligence A Survey of LLM-based Scientific Agents_images/imageFile20.png)

![image 21](Ren et al._2025_Towards Scientific Intelligence A Survey of LLM-based Scientific Agents_images/imageFile21.png)

Search arXiv│PubMed│MatSci KB│Web Query:“Li-rich Mn cathode coating stability”

![image 22](Ren et al._2025_Towards Scientific Intelligence A Survey of LLM-based Scientific Agents_images/imageFile22.png)

Planner

Domain Models

Tool APIs Simulators

Paper: DOI 10.1000/abc (250 mAh/g) MatSciKB: Li2MnO3 σ = 1.2 mS/cm Web: USPTO 12345678B2 MgAl2O4 coat

RDKit VASP LAMMPS PyLab AlphaFold

###### T3 Code Generation & Execution

T4 LLM-Based Reasoning / Cognitive Actions

![image 23](Ren et al._2025_Towards Scientific Intelligence A Survey of LLM-based Scientific Agents_images/imageFile23.png)

Hypothesize OR Evaluate OR Compare OR Rank

Generate Python│Bash│DSL│YAML ....

Idea: “Mg-doped Li-rich w/ Al2O3 coat” Test Debug Pipline

![image 24](Ren et al._2025_Towards Scientific Intelligence A Survey of LLM-based Scientific Agents_images/imageFile24.png)

Evaluation: cycles 550 ✓, cost ↑, safety ✓ Rank: 1st vs bare (2nd) vs Co-rich (3rd)

Script

Figure 8: Different types of actions taken by LLM-based scientific agents.

(NCBI). NCBI provides API access to its entire biomedical databases and tools. SciAgent (Ma

ONet surrogates and Nektar++ CFD simulator to optimize 2D NACA airfoils in aerodynamic design, with LLMs employing DeepONet for flow field computations during optimization and validating results through high-fidelity simulations; OpenFOAMGPT (Pandey et al., 2025) and FoamAgent (Yue et al., 2025) automate OpenFOAM CFD workflows generating simulation configurations, invoking solvers, and post-processing results; MechAgents (Ni and Buehler, 2024) employs FEniCS simulation environment for structural mechanics problems. Chemistry agents leverage molecular simulation platforms: Coscientist (Boiko et al., 2023) integrates robotic laboratory equipment for autonomous synthesis execution; AtomAgents (Ghafarollahi and Buehler, 2024a) orchestrates LAMMPS molecular dynamics simulations for alloy design; ADAM (Xia et al., 2025a) employs DSDP for molecular docking, SPONGE for MD trajectory calculations, and PySCF for DFT quantum mechanical property computations. Astronomy agents control observational platforms: StarWhisper (Wang et al., 2025a) interfaces with telescope control systems translating natural language observation requests into instrument commands; LLMSat (Maranto, 2024) presents an agentic spacecraft controller tested in Kerbal Space Program simulation environment with multi-level validation.

- et al., 2024b) generalizes mathematical tool utilization to other domains through cross-retrieval strategies, developing a human-validated multi-domain tool set (SciToolBench) encompassing mathematics, physics, chemistry, finance, electrical engineering, and computer science.


#### (2) Tool Sets Based on Simulators and Emulation Platforms

Simulators and emulation platforms provide specialized, domain-specific tools enabling agents to simulate experimental procedures and validate results through tight integration with experimental workflows. By translating natural language instructions into executable simulation codes or parameterized control signals using LLMs, these tool sets facilitate deep integration often tightly coupled with planning processes, ensuring correct parameterization and validation throughout simulations or laboratory automation steps—particularly valuable in complex research tasks. Physics-related agents frequently employ this approach: SGA (Ma

- et al., 2024a) utilizes physics simulators as experimental platforms on which LLMs generate scientific hypotheses and perform reasoning, with simulators providing observational feedback and enabling differentiable optimization of continuous parameters, achieving validated results in constitutive law discovery and molecular design; MyCrunchGPT (Kumar et al., 2023) integrates Deep-


The integration of simulation tool sets addresses LLM limitations in understanding physical laws

and reasoning about dynamic processes, enhancing computational accuracy and validity for complex problems. This modular, extensible integration strategy has proven effective in mitigating LLMs’ inherent limitations in domain expertise and computational precision. However, challenges persist: practical adoption remains constrained by high computational costs and temporal overheads of precision simulators; proficient simulator utilization and accurate parameter generation pose significant challenges for LLMs; non-standardized interfaces, limited tool diversity, and tool generation complexity hinder broader adoption; tool integration complexity with heterogeneous APIs, error handling difficulties from unpredictable failures, and cost and latency constraints for expensive simulations or slow physical equipment create workflow bottlenecks—motivating development of standardized interface protocols, robust error detection mechanisms, and hybrid strategies combining fast approximate tools for screening with precise validation.

#### (3) Domain Models as Tools

Domain-specific AI models represent a distinct category of tools where scientific agents invoke specialized, pre-trained neural network models designed for particular scientific tasks, leveraging their domain expertise as computational resources. Unlike general-purpose LLMs that serve as the agent’s reasoning engine, these domain models function as specialized tools that agents call to perform specific predictions, analyses, or transformations that require deep domain knowledge or computationally intensive model inference. This approach enables agents to access state-of-the-art domain expertise—such as protein structure prediction, molecular property estimation, or materials property forecasting—without requiring the agent’s core LLM to internalize all domain-specific knowledge. The integration of domain models as tools creates a hybrid architecture where the agent orchestrates workflows, makes strategic decisions, and synthesizes results, while domain models provide expert-level predictions and analyses within their specialized domains.

Representative implementations demonstrate diverse applications of domain models as tools. For example, in protein science, ProtAgents (Ghafarollahi and Buehler, 2024b) integrates multiple domain-specific models: Chroma (Ingraham et al.,

- 2023) for de novo protein design generating novel protein sequences, OmegaFold v2 (Wu et al., 2024) for 3D protein structure prediction from amino acid


sequences, and their developed ProteinForceGPT for predicting mechanical properties including maximum unfolding force and unfolding energy—each model invoked as a tool within the agent’s workflow for protein engineering tasks. Sparks (Ghafarollahi and Buehler, 2025) employs a similar strategy, utilizing Chroma for sequence design, OmegaFold v2 for structure prediction, and ProteinForceGPT for mechanical property prediction, with these domain models integrated into multi-agent workflows for autonomous protein discovery. The AI co-scientist (Gottweis et al., 2025) leverages AlphaFold (Jumper et al., 2021) as a validation tool to assess structural plausibility of AI-proposed protein sequences, integrating domain model feedback into iterative refinement loops where protein engineering hypotheses are validated against structural constraints predicted by the specialized model. In materials science, agents also invoke property prediction models trained on domain-specific datasets to estimate material characteristics without requiring the core LLM to encode extensive materials knowledge: dZiner (Ansari et al., 2024) iteratively evaluates candidate materials using cost-efficient surrogate models for property estimation, incorporating epistemic uncertainty through ensemble modeling, and employs domain-expert models (potentially physics-based) to assess molecule modulation effectiveness; ChatMOF (Kang and Kim, 2024) configures the MOFTransformer model (Kang et al., 2023; Park et al., 2023) as a prediction tool for forecasting MOF properties, utilizing property and material formats to designate prediction targets; LLMatDesign (Jia et al., 2024) validates material properties using surrogate models as computationally efficient stand-ins for expensive density functional theory calculations. These domain models are typically accessed through APIs or local inference endpoints, allowing agents to seamlessly integrate their predictions into broader research workflows.

The use of domain models as tools addresses critical limitations in LLM-based scientific agents: it provides access to cutting-edge domain expertise that would be impractical to encode in the agent’s core model, enables computationally efficient access to specialized predictions without retraining the agent, and allows agents to leverage models that have been optimized on large-scale domain-specific datasets. However, challenges include model availability and accessibility where state-of-the-art domain models may require significant computational

resources or proprietary access; integration complexity where different models may have heterogeneous interfaces and output formats; and model reliability where domain models may have failure modes or limitations that agents must recognize and handle appropriately—motivating development of standardized model interfaces, robust error handling for model invocations, and agent capabilities to assess and validate domain model outputs.

#### 2.3.2 T2. Search & Information Retrieval

Search and information retrieval actions enable agents to acquire knowledge from external sources, query databases for relevant data, retrieve scientific literature pertinent to research questions, and access factual information not encoded in the LLM’s parameters. This action class includes diverse retrieval modalities: scientific literature search where agents query scholarly databases using keyword queries, semantic search, or citation networks to identify relevant publications, retrieve abstracts or full texts, extract methodological precedents, and discover prior work (Moss, 2025; Lu et al., 2024a; Yamada et al., 2025; Gottweis et al., 2025; Tang

- et al., 2025a; Schmidgall et al., 2025; Novikov


- et al., 2025; Saeedi et al., 2025; Yin et al., 2025; Ghafarollahi and Buehler, 2024a; Xin et al., 2024; Mehandru et al., 2025; Roohani et al., 2024; Luo et al., 2022; Su et al., 2025; Huang et al., 2025a; Zhang et al., 2025a; Huang et al., 2024a; Tang et al.,


- 2025d; Kang and Kim, 2024; Tang et al., 2025b; Song et al., 2025; Bran et al., 2024; Zhao et al.,


- 2025; Huang et al., 2025c; Sprueill et al., 2024; Chen et al.; Zhang et al., 2025d; Thulke et al.,


- 2024; Li et al., 2024b; Boiko et al., 2023; Xue


- et al., 2024; Weng et al., 2025; Inoue et al., 2024;

- Li et al., 2025a; Huang et al., 2024c; Peng et al.,


2023; Jin et al., 2024; Chen et al., 2024a; Huang

- et al., 2025b; Fu et al., 2025a; O’Neill et al., 2025; Team et al., 2025a; Zhou et al., 2025; Yang et al.,


- 2024b; Ni et al., 2024; Ni and Buehler, 2024; Sun


- et al., 2024b; Hu et al., 2025a; Darvish et al., 2025; Pandey et al., 2025; Feng et al., 2025a; Pantiukhin
- et al., 2025; He et al., 2025; Lai and Pu, 2025; Gha-


- farollahi and Buehler, 2024b; Baek et al., 2024; Ghareeb et al., 2025; Ma et al., 2024a,b; Ghafarollahi and Buehler, 2024c; Wang et al., 2024b; Gha-
- farollahi and Buehler, 2025; Wang et al., 2025a; Liu et al., 2024a; Su et al., 2024); knowledge base and structured database querying with RAG where agents access structured repositories including chemical, biological, materials, geological, and


astronomical databases retrieving specific records, property data, or relational information (Xia et al., 2025a; Liu et al., 2024b; Yin et al., 2025; Ghafarollahi and Buehler, 2024a; Xin et al., 2024; Mehandru et al., 2025; Roohani et al., 2024; Su et al., 2025; Zhang et al., 2025a; Huang et al., 2025a; Li et al., 2024c; McNaughton et al., 2024; Huang et al., 2024a; Kang and Kim, 2024; Wu et al., 2025; Tang et al., 2025b; Song et al., 2025; Bran et al., 2024; Huang et al., 2025c; Chen et al.; Zhang et al., 2025d; Thulke et al., 2024; Boiko

- et al., 2023; Inoue et al., 2024; Li et al., 2025a; Zou et al., 2025; Yue et al., 2025; Huang et al., 2024c; Chen et al., 2024a; Huang et al., 2025b; Fu et al., 2025a; Bekele, 2025; Zhang et al., 2024a; Noh et al., 2025; Team et al., 2025a; Li et al., 2025b; Ruan et al., 2024; Maranto, 2024; Zhou et al., 2025; Yang et al., 2024b; Ni et al., 2024; Ni and Buehler,

- 2024; Bazgir et al., 2025; Darvish et al., 2025; Hu et al., 2025b; Pandey et al., 2025; Feng et al.,
- 2025a; Pantiukhin et al., 2025; Lai and Pu, 2025; Ghareeb et al., 2025; Ghafarollahi and Buehler, 2024c; Gou et al., 2024; Ansari et al., 2024; Cao


- et al., 2024); and web and general retrieval where agents perform general-purpose web searches for factual information, technical documentation, or supplementary resources (Gottweis et al., 2025; Lu et al., 2024a; Tang et al., 2025a; Ghafarollahi and Buehler, 2024a; Li et al., 2024c; Bran et al., 2024; Boiko et al., 2023; Huang et al., 2024c; Team et al., 2025a; Ansari et al., 2024).


Mechanistically, search and retrieval actions follow a query-retrieve-extract pattern where the agent formulates search queries, executes queries receiving ranked result lists, filters and ranks results, extracts relevant information, and synthesizes retrieved information into coherent summaries. Advanced implementations employ iterative query refinement, multi-source integration, and citation network traversal. The effectiveness depends on query formulation quality and the agent’s ability to assess relevance and extract key information.

Representative implementations showcase sophisticated retrieval strategies. SciMON (Wang et al., 2024b) implements literature-grounded idea generation where agents query scientific publication databases using research area keywords, retrieve recent papers, extract key concepts and methodologies, and synthesize novel research ideas by identifying gaps or proposing extensions. ResearchAgent (Baek et al., 2024) derives a knowledge store derived from shared underlying con-

cepts mined across numerous papers, and is augmented with the co-occurrences of key concepts in the scientific literature for iterative research idea generation. Similarly, PaSa (He et al., 2025) implements comprehensive academic paper search combining keyword-based querying of multiple scholarly databases, semantic similarity ranking using embedding models to identify conceptually related work, and citation network expansion recursively exploring references to build comprehensive literature maps. ClimateGPT (Thulke et al., 2024) integrates retrieval mechanisms accessing curated climatological research reports and peer-reviewed papers, enhancing response accuracy in climate science. FoamAgent (Yue et al., 2025) utilizes hierarchical multi-index retrieval systems providing context-specific knowledge with dependencyaware file generation ensuring consistency across OpenFOAM configuration files, democratizing access to complex CFD simulation tools through natural language interaction. BioDiscoveryAgent (Roohani et al., 2024)has access to tools for searching the biomedical literature, executing code to analyze biological datasets, and prompting another agent to critically eval-uate its predictions. BioScientist Agent (Zhang et al., 2025a) queries PubMed for biomedical abstracts related to gene-disease relationships, filters results for relevance using learned ranking models, extracts causal statements linking entities, and constructs evidence sets supporting or refuting therapeutic hypotheses. The search agent designed in DrugAgent (Inoue et al.,

- 2024) analyzes search results to extract evidence and score interactions through keyword matching, summarizing reasons from search engine results (titles, links, and content) by LLM. AI Cosmologist (Moss, 2025) employs Literature Agents automatically searching arXiv and INSPIRE-HEP for papers related to cosmological analysis tasks, retrieving full texts, extracting methodological descriptions and benchmark results, and maintaining structured bibliographies linking implementation choices to scientific precedents. GeoSim.AI (Bekele, 2025) builds Knowledge Base of detailed information on various numerical methods such as finite element analysis, finite difference methods, and discrete element methods. This dynamic integration of curated knowledge with the LLM’s inherent language understanding capabilities allows GeoSim.AI to provide responses that are both linguistically coherent and technically accurate in the domain of geotechnical engineering. HoneyComb (Zhang et al., 2024a)


queries MatSciKB materials science knowledge base to retrieve properties of known materials enabling agents to ground hypotheses in empirical data.

Search and retrieval actions enable access to current specialized knowledge exceeding model parameters, ground reasoning in authoritative sources, and build upon established work. However, challenges include query formulation difficulty, information overload requiring sophisticated relevance assessment, source quality concerns, and integration complexity synthesizing potentially contradictory information—driving development of better query generation, relevance ranking, and multisource synthesis strategies.

#### 2.3.3 T3. Code Generation & Execution

Code generation and execution actions enable agents to synthesize executable programs, scripts, and computational workflows that implement analytical procedures, orchestrate complex multi-tool pipelines, process and visualize data, or automate repetitive computational tasks. This action class encompasses complementary operational dimensions: code synthesis where agents generate programs in various languages implementing algorithmic logic, data processing procedures, visualization routines, or computational workflows (Xia et al., 2025a; Moss, 2025; Lu et al., 2024a; Yamada et al., 2025; Tang et al., 2025a; Mandal et al.,

- 2024; Liu et al., 2024b; Kumbhar et al., 2025; Schmidgall et al., 2025; Novikov et al., 2025; Ye

- et al., 2023b; Ghafarollahi and Buehler, 2024a; Panapitiya et al., 2025; Xin et al., 2024; Mehandru et al., 2025; Roohani et al., 2024; Su et al., 2025; Huang et al., 2025a; McNaughton et al., 2024; Huang et al., 2024a; Xiao et al., 2024; Tang et al.,

2025d; Alber et al., 2025; Kang and Kim, 2024; Wu et al., 2025; Tang et al., 2025b; Song et al., 2025; Pham et al., 2025; Huang et al., 2025c; Chen et al.; Zhang et al., 2025d; Boiko et al., 2023; Weng et al., 2025; Inoue et al., 2024; Li et al., 2025a; Zou et al., 2025; Yue et al., 2025; Jin et al., 2024; Chen et al., 2024a; Huang et al., 2025b; Bekele, 2025; Zhang et al., 2024a; Noh et al., 2025; Team et al., 2025a; Li et al., 2025b; Ning et al., 2025; Ruan

- et al., 2024; Jia et al., 2024; Zhou et al., 2025; Li

- et al., 2024d; Yang et al., 2024b; Ni et al., 2024; Ni and Buehler, 2024; Hu et al., 2025a; Yu et al., 2024; Jaiswal et al., 2024; Bazgir et al., 2025; Riffle et al.,

2025; Darvish et al., 2025; Hu et al., 2025b; Pandey

- et al., 2025; Feng et al., 2025a; Pantiukhin et al.,






- 2025; Pu et al., 2025; Lai and Pu, 2025; Ghafarol-


- lahi and Buehler, 2024b; Ghareeb et al., 2025; Ma et al., 2024a,b; Ghafarollahi and Buehler, 2024c,


- 2025; Wang et al., 2025a; Liu et al., 2024a; Gou


- et al., 2024; Zhang et al., 2025b; Ansari et al., 2024; Cao et al., 2024; Polat et al., 2025); and code execution and evaluation where generated programs are run in computational environments producing outputs, error messages, or diagnostic information that advance research objectives or guide iterative refinement (Xia et al., 2025a; Moss, 2025; Lu et al.,

- 2024a; Yamada et al., 2025; Tang et al., 2025a; Mandal et al., 2024; Liu et al., 2024b; Schmidgall

et al., 2025; Novikov et al., 2025; Ye et al., 2023b; Yin et al., 2025; Ghafarollahi and Buehler, 2024a; Panapitiya et al., 2025; Xin et al., 2024; Mehandru et al., 2025; Roohani et al., 2024; Su et al., 2025; Huang et al., 2025a; McNaughton et al., 2024; Huang et al., 2024a; Xiao et al., 2024; Tang et al., 2025d; Alber et al., 2025; Kang and Kim, 2024; Wu et al., 2025; Tang et al., 2025b; Song et al., 2025; Pham et al., 2025; Huang et al., 2025c; Chen et al.;

- Zhang et al., 2025d; Boiko et al., 2023; Weng et al.,


- 2025; Inoue et al., 2024; Li et al., 2025a; Zou et al., 2025; Yue et al., 2025; Jin et al., 2024; Chen et al.,




- 2024a; Huang et al., 2025b; Bekele, 2025; Zhang


- et al., 2024a; Noh et al., 2025; Team et al., 2025a;


- Li et al., 2025b; Ning et al., 2025; Ruan et al., 2024; Jia et al., 2024; Zhou et al., 2025; Li et al., 2024d; Yang et al., 2024b; Ni et al., 2024; Ni and Buehler,


- 2024; Hu et al., 2025a; Yu et al., 2024; Jaiswal

- et al., 2024; Bazgir et al., 2025; Riffle et al., 2025; Darvish et al., 2025; Hu et al., 2025b; Pandey et al.,


- 2025; Feng et al., 2025a; Pantiukhin et al., 2025; Pu et al., 2025; Lai and Pu, 2025; Ghafarollahi and Buehler, 2024b; Ghareeb et al., 2025; Ma et al., 2024a,b; Ghafarollahi and Buehler, 2024c, 2025; Wang et al., 2025a; Liu et al., 2024a; Gou et al.,


- 2024; Zhang et al., 2025b; Ansari et al., 2024; Cao


- et al., 2024; Polat et al., 2025). Mechanistically, code generation actions unfold


through specification-synthesis-execution cycles where the agent interprets high-level research objectives, translates requirements into concrete algorithmic steps, generates syntactically correct code, and executes generated code capturing outputs and diagnostic information. Advanced implementations include iterative debugging, test-driven development, modular code organization, and documentation generation. Quality depends on the agent’s training on code repositories, task description clarity, and debugging sophistication.

Representative systems demonstrate sophisticated code generation capabilities. AI Scientist (Lu et al., 2024a) generates novel research ideas, writes code, and executes experiments, which uses Aider to implement code changes for experiments, which are then executed. If errors occur, Aider attempts to fix the code and re-attempt. For autonomous machine learning research, MLR-Copilot (Li et al., 2024d) automatically generates experimental plans into executables with ExperimentAgent, which then manages the execution of these experiments. The system inspects scripts, executes models, and retrieves models as part of its operation. Similarly, Agent Laboratory (Schmidgall et al., 2025) writes Python code for ML experiments including dataset preparation, model training with hyperparameter tuning, performance evaluation, and results logging, iteratively debugging based on execution feedback. Biomni (Huang et al., 2025a) applies LLM-based reasoning and domain expertise to generate a detailed, step-by-step plan, with each step expressed through executable code, enabling precise and flexible compositions of biomedical actions. CellAgent (Xiao et al., 2024) generates bioinformatics analysis code for single-cell RNA-seq data processing including quality control, normalization, dimensionality reduction, clustering, differential expression analysis, and pathway enrichment, with self-optimization cycles refining code based on execution errors. BioAgents (Mehandru et al., 2025) generates code or workflows for tasks like providing quality metrics on FASTQ files, aligning RNA-seq data, and assembling/annotating SARS-CoV-2 genomes. AutoLabs (Panapitiya et al., 2025) autonomously translates natural-language instructions into executable protocols and generates a hardware-ready file with rule-based coding to drive the robot for automatic chemistry experiments. AmadeusGPT (Ye et al., 2023b) synthesizes behavior analysis code for neuroscience research translating natural language descriptions of behavioral patterns into Python scripts using pose estimation libraries, implementing custom metrics, and generating visualizations. OpenFOAMGPT (Pandey et al., 2025) generates CFD simulation configuration files and preprocessing scripts setting up computational meshes, boundary conditions, solver parameters, and post-processing workflows. AlphaEvolve (Novikov et al., 2025) evolves algorithmic code through iterative modification generating candidate implementations of numerical algorithms, testing them on benchmark

problems, comparing performance against existing methods, and proposing refined versions. SGA (Ma

- et al., 2024a) generates Python implementations of physics-based models that are subsequently tested in physics simulators providing objective performance feedback. AILA (Mandal et al., 2024) generates specific Python scripts for each stage of an AFM experiment, controlling the instrument in real time through an API. The Code Executor tool runs these Python scripts directly on the local system, for automating microscopy experiments.

Code generation enables precise, reproducible analytical workflows that can be verified, reused, and shared as executable artifacts. However, challenges include code correctness where subtle bugs may evade simple testing, complexity management where generated code may be difficult to maintain, and dependency management where code relies on specific configurations—motivating better validation techniques, quality metrics, and containerization practices.

- 2.3.4 T4. LLM-Based Reasoning / Cognitive Actions


LLM-based reasoning and cognitive actions leverage the agent’s native language model capabilities to perform intellectual operations central to scientific reasoning including hypothesis generation, analytical reasoning, creative synthesis, critical evaluation, and analogical reasoning. Unlike tool use, retrieval, or code execution which invoke external systems, reasoning actions exploit the LLM’s internal capabilities to perform cognitive operations that transform information, generate insights, and draw conclusions. These actions constitute the "thinking" component of scientific agents. This encompasses two primary cognitive dimensions: hypothesis generation and creative synthesis where agents propose novel explanations, predictions, or research directions, generate innovative ideas by combining disparate concepts, formulate testable hypotheses, design experiments, or synthesize crossdisciplinary insights (Moss, 2025; Lu et al., 2024a; Yamada et al., 2025; Gottweis et al., 2025; Tang

- et al., 2025a; Liu et al., 2024c,b; Novikov et al.,


- 2025; Ye et al., 2023b; Ghafarollahi and Buehler,


- 2024a; Mehandru et al., 2025; Roohani et al., 2024; Luo et al., 2022; Su et al., 2025; Zhang et al., 2025a; McNaughton et al., 2024; Tang et al., 2025d; Alber et al., 2025; Kang and Kim, 2024; Tang et al., 2025b; Song et al., 2025; Bran et al., 2024; Zhao


- et al., 2025; Pham et al., 2025; Sprueill et al.,


- 2024; Chen et al.; Thulke et al., 2024; Li et al.,

- 2024b; Boiko et al., 2023; Xue et al., 2024; Weng et al., 2025; Inoue et al., 2024; Feng et al., 2025b; Zou et al., 2025; Yue et al., 2025; Huang et al.,
- 2024c; Peng et al., 2023; Jin et al., 2024; Chen


- et al., 2024a; O’Neill et al., 2025; Noh et al., 2025; Team et al., 2025a; Jia et al., 2024; Zhou et al.,

2025; Li et al., 2024d; Yang et al., 2024b; Chen

- et al., 2023; Tang et al., 2023; Sun et al., 2024b; Hu et al., 2025a, 2024b; Jaiswal et al., 2024; Bazgir et al., 2025; Darvish et al., 2025; Pantiukhin

et al., 2025; He et al., 2025; Pu et al., 2025; Lai and Pu, 2025; Ghafarollahi and Buehler, 2024b; Baek et al., 2024; Ghareeb et al., 2025; Ma et al.,

- 2024b; Ghafarollahi and Buehler, 2024c; Wang

et al., 2024b; Ghafarollahi and Buehler, 2025; Su

- et al., 2024; Ansari et al., 2024; Polat et al., 2025); and analytical reasoning and interpretation where agents systematically decompose complex problems through logical chains of inference, critically evaluate arguments and evidence, interpret experimental results, perform multi-step logical deductions, or provide explanations linking observations to underlying mechanisms (Xia et al., 2025a; Moss,

2025; Lu et al., 2024a; Yamada et al., 2025; Tang

- et al., 2025a; Liu et al., 2024c,b; Kumbhar et al.,


- 2025; Schmidgall et al., 2025; Novikov et al., 2025; Ye et al., 2023b; de Haan et al., 2025; Yin et al., 2025; Ghafarollahi and Buehler, 2024a; Panapitiya et al., 2025; Xin et al., 2024; Mehandru et al., 2025; Roohani et al., 2024; Su et al., 2025; Zhang et al., 2025a; Huang et al., 2025a; McNaughton et al., 2024; Huang et al., 2024a; Xiao et al., 2024; Tang et al., 2025d; Alber et al., 2025; Kang and Kim,








- 2024; Wu et al., 2025; Tang et al., 2025b; Song et al., 2025; Bran et al., 2024; Zhao et al., 2025; Pham et al., 2025; Huang et al., 2025c; Sprueill et al., 2024; Chen et al.; Zhang et al., 2025d; Thulke et al., 2024; Li et al., 2024b; Boiko et al., 2023; Xue

- et al., 2024; Weng et al., 2025; Inoue et al., 2024; Li et al., 2025a; Feng et al., 2025b; Zou et al., 2025; Yue et al., 2025; Huang et al., 2024c; Peng et al.,

- 2023; Jin et al., 2024; Chen et al., 2024a; Huang

et al., 2025b; Bekele, 2025; Zhang et al., 2024a; O’Neill et al., 2025; Noh et al., 2025; Team et al., 2025a; Li et al., 2025b; Ning et al., 2025; Ruan

- et al., 2024; Maranto, 2024; Jia et al., 2024; Zhou
- et al., 2025; Li et al., 2024d; Yang et al., 2024b; Chen et al., 2023; Ni et al., 2024; Ni and Buehler,


- 2024; Tang et al., 2023; Sun et al., 2024b; Hu et al.,
- 2025a; Yu et al., 2024; Jaiswal et al., 2024; Hu et al., 2024b; Bazgir et al., 2025; Kumar et al.,






- 2023; Riffle et al., 2025; Darvish et al., 2025; Hu

et al., 2025b; Pandey et al., 2025; Feng et al., 2025a; Zhang et al., 2025e; Pantiukhin et al., 2025; He et al., 2025; Pu et al., 2025; Lai and Pu, 2025; Gha-

- farollahi and Buehler, 2024b; Luong et al., 2024; Baek et al., 2024; Ghareeb et al., 2025; Ma et al.,

2024a; Lai et al., 2024; Ma et al., 2024b; Ghafarollahi and Buehler, 2024c; Wang et al., 2024b; Gha-

- farollahi and Buehler, 2025; Wang et al., 2025a;




- Liu et al., 2024a; Gou et al., 2024; Zhang et al., 2025b; Su et al., 2024; Ansari et al., 2024; Cao


- et al., 2024; Polat et al., 2025). Mechanistically, reasoning actions are imple-


mented through carefully designed prompts that elicit specific cognitive operations including hypothesis generation prompts, analytical reasoning prompts, creative synthesis prompts, critical evaluation prompts, and chain-of-thought reasoning prompts. The sophistication and reliability depend on the underlying LLM’s capabilities and the quality of prompts which determine whether reasoning capabilities are effectively activated and channeled toward productive scientific thinking.

Representative implementations illustrate diverse reasoning patterns. CoI (Li et al., 2024b) implements Chain-of-Ideas where agents generate research ideas through iterative refinement—initial broad ideas are progressively specialized and elaborated through multi-step reasoning that explores implications, identifies challenges, and proposes solutions. SciMON (Wang et al., 2024b) performs novelty-optimizing idea generation where agents analyze existing literature to identify research gaps, reason about what approaches might fill those gaps, and synthesize novel research proposals explicitly designed to maximize scientific contribution. AI Scientist-v2 (Yamada et al., 2025) formulates scientific hypotheses and engages in open-ended thinking about research directions, experimental designs, and assesses the novelty and feasibility of proposed concepts. It also evaluates candidates for tree search based on performance metrics and training dynamics, and critically analyzes figures and captions. HyperGen (Kumbhar et al., 2025) frames hypothesis generation as conditional language modelling, with the model fine-tuned on Bit-Flip-Spark and the Chain-of-Reasoning. AIGS (Liu et al.,

- 2024c) designs LLM-powered planner to orchestrate user interactions and coordinates specialized agents, dissecting complex queries into sequential objectives and directing specific tools for analysis, such as calculating average friction or surface


roughness. ChemReasoner (Sprueill et al., 2024) employs process-supervised reasoning for catalysis where complex reaction problems are decomposed into sequential reasoning steps, each step involves hypothesis generation about reaction mechanisms followed by validation against chemical principles, and the agent explicitly chains inferences building toward final synthesis recommendations. MedAgents (Tang et al., 2023) implements clinical reasoning where specialized agents analyze patient symptoms, generate differential diagnoses by reasoning from symptoms to potential underlying conditions, propose diagnostic tests to discriminate between hypotheses, and synthesize evidence to reach diagnostic conclusions mimicking expert clinician thinking. To accelerate biomedical scientific discovery, the AI co-scientist (Gottweis et al., 2025) continuously generates, reviews, debates, and improves research hypotheses and proposals toward the research goal provided by the scientist, with different specialist agents. BioDiscoveryAgent (Roohani et al., 2024) performs hypothesis-driven experiment design where agents reason about what genetic perturbations would test specific biological hypotheses, predict expected outcomes under alternative mechanistic scenarios, and design multiround experimental strategies that maximize information gain about underlying biological mechanisms. OriGene (Zhang et al., 2025e) functions as a virtual disease biologist, systematically identifying original and mechanistically grounded therapeutic targets at scale. It coordinates specialized agents (Coordinator, Planning, Reasoning, Critic, Reporting) that reason over diverse modalities. DrugAgent (Inoue et al., 2024) employs multi-agent reasoning where different agents specialize in distinct analytical perspectives (pharmacological mechanism reasoning, toxicity risk assessment, synthetic accessibility evaluation), and collective reasoning integrates these perspectives to evaluate drug candidates holistically. AstroMLab (de Haan et al., 2025) demonstrates domain-specialized reasoning through continued pretraining, enabling the model to emit step-by-step astronomical reasoning chains that apply domain-specific knowledge and problemsolving patterns.

LLM-based reasoning provides flexible cognitive capabilities across domains, enables creative hypothesis generation and insight synthesis, and supports natural language collaboration. However, limitations include reasoning reliability where models may produce plausible but flawed reasoning,

lack of formal correctness guarantees, and hallucination risks—necessitating integration with toolbased validation, retrieval-augmented grounding, and careful prompt engineering.

#### 2.3.5 Discussion

The action space fundamentally defines what scientific work agents can autonomously perform. The four action types—tool use, search and retrieval, code generation, and LLM reasoning—are complementary capabilities addressing distinct LLM limitations: tool use enables precise computation and environment interaction; search and retrieval grounds reasoning in authoritative sources mitigating hallucination; code generation produces reproducible executable workflows; and LLM reasoning synthesizes information and orchestrates complex processes. The most capable agents integrate all four types into unified workflows spanning hypothesis generation through experimental execution to analysis.

Action space design reveals critical architectural considerations. Tool sets—whether API-based libraries or simulator platforms—represent a design pattern decoupling high-level reasoning from lowlevel execution. By encapsulating specialized algorithms, domain knowledge, and computational resources behind well-defined interfaces, tools allow LLMs to focus on strategic planning rather than implementation details, addressing the tension between LLMs’ natural language strengths and domain-specific computational limitations. APIbased tools provide curated algorithms and knowledge bases enabling agents to leverage scientific software engineering without reimplementation. Simulator-based tools integrate experimental validation into reasoning loops, enabling hypothesis testing through virtual experiments that would be expensive, dangerous, or time-consuming physically. These strategies substantially enhance LLMs’ planning, reasoning, computational, and execution capabilities, transforming them from language processors into capable scientific assistants.

However, current implementations face systemic limitations. Many systems rely on pre-defined, static tool sets and well-documented repositories, fundamentally limiting adaptability in dynamic research environments. Benchmarks like ShortcutsBench (Shen et al., 2025) reveal that even stateof-the-art systems struggle with API dependency management and adapting to frequently updated services—challenges particularly acute in rapidly

evolving fields like computational biology and materials informatics. High subscription costs for APIs, computational overheads of simulators, and temporal delays in equipment control create practical barriers. Error handling across heterogeneous tools remains unsolved, as failures cascade unpredictably and agents lack robust diagnostic mechanisms. Security and reproducibility concerns persist, as agents may inadvertently expose sensitive data through API calls or produce non-reproducible results from version-dependent tool behavior.

Advancing action space capabilities requires multiple research directions. Autonomous, selfadaptive frameworks that dynamically discover, integrate, and compose tools at runtime would dramatically expand flexibility. Middleware layers providing unified abstractions would simplify integration and enable higher-level reasoning about tool selection. As highlighted by Shen et al. (2025); Gu et al. (2024), dynamic middleware-based solutions can adapt to real-time changes in scientific environments. Standardizing tool interfaces, documentation, and error semantics would reduce integration friction. Intelligent action selection strategies reasoning probabilistically about which actions best advance goals given evidence, costs, and uncertainties would improve efficiency. Composable action primitives enabling novel workflow construction would support open-ended exploration. Resource-aware planning considering computational budgets, time constraints, and accuracy tradeoffs would make agents practical in resource-limited settings. Finally, establishing formal safety constraints and validation protocols becomes critical as action spaces expand to encompass increasingly powerful operations in experimental automation and autonomous research.

#### 2.4 Verifier

Verification mechanisms constitute the quality control layer of LLM-based scientific agents, implementing critical safeguards against hallucination, logical inconsistencies, factual inaccuracies, and procedural errors that could compromise research integrity, lead to false discoveries, or waste experimental resources on unviable hypotheses. Because LLMs can generate superficially plausible but fundamentally flawed outputs—proposing chemically impossible reactions, suggesting biologically implausible mechanisms, recommending computationally intractable experiments, or making logically inconsistent inferences—systematic verifica-

AI Scientist (Lu et al., 2024a), ASA (Liu et al., 2024b), CellForge (Tang et al., 2025d), CellVoyager (Alber et al., 2025), ChemAgent (Tang et al., 2025b), ChemOrch (Huang et al., 2025c), DrugPilot (Li et al., 2025a), dZiner (Ansari et al., 2024), GeoAgent (Chen et al., 2024a), ToRA (Gou et al., 2024), OriGene (Zhang et al., 2025e), etc

V1. Self-Correction / Reflective Verification

AccelMat (Kumbhar et al., 2025), AI co-scientist (Gottweis et al., 2025), AtomAgents (Ghafarollahi and Buehler, 2024a), AutoLabs (Panapitiya et al., 2025), CellAgent (Xiao et al., 2024), MedAgents (Tang et al., 2023), Sparks (Ghafarollahi and Buehler, 2025), VirSci (Su et al., 2024), STELLA (Jin et al., 2025),etc

V2. MultiAgent Critique / Role-Based Verification

Verifier

Agent Laboratory (Schmidgall et al., 2025), BIA (Xin et al., 2024), ChemCrow (Bran et al., 2024), Chemma (Zhang et al., 2025d), CRISPR-GPT (Huang et al., 2024a), dZiner (Ansari et al., 2024), MAPPS (Zhou et al., 2025), MatPilot (Ni et al., 2024), ORGANA (Darvish et al., 2025), Robin (Ghareeb et al., 2025), ResearchAgent (Baek et al., 2024), StarWhisper (Wang et al., 2025a), etc

V3. Humanin-the-Loop / Expert Oversight

AILA (Mandal et al., 2024), Agent Laboratory (Schmidgall et al., 2025), BioDiscoveryAgent (Roohani et al., 2024), Coscientist (Boiko et al., 2023), GeoSim.AI (Bekele, 2025), SGA (Ma et al., 2024a), ToRA (Gou et al., 2024), xChemAgents (Polat et al., 2025), etc

V4. Tool-Based Validation / Computational Verification

Figure 9: Taxonomy of verification mechanisms in representative scientific agents: V1 (Self-Correction / Reflective Verification), V2 (Multi-Agent Critique / Role-Based Verification), V3 (Human-in-the-Loop / Expert Oversight), V4 (Tool-Based Validation / Computational Verification).

tion is essential for ensuring that agent-generated hypotheses, experimental designs, analytical procedures, and scientific claims meet standards of validity, feasibility, and consistency before being acted upon, published, or used to guide resource allocation in physical experiments. Verification architectures in scientific agents span a spectrum from lightweight self-correction mechanisms where single LLM instances iteratively refine their own outputs, to sophisticated multi-agent critique systems implementing role-based adversarial review, human-in-the-loop oversight providing expert validation at critical decision points, and tool-based validation leveraging external computational tools, databases, or simulators to objectively assess correctness, feasibility, or performance. Based on the source and nature of verification signals, we categorize verification mechanisms into four types: self-correction as in subsection 2.4.1, multi-agent

critique as in subsection 2.4.2, human-in-the-loop verification as in subsection 2.4.3, and tool-based validation as in subsection 2.4.4. These mechanisms are not mutually exclusive; robust scientific agents often implement layered verification combining multiple strategies to provide complementary checks addressing different types of errors. We illustrate them in Figure 10 and list the related works of different verifiers in Figure 9.

2.4.1 V1. Self-Correction / Reflective Verification

Self-correction or reflective verification involves a single LLM instance iteratively evaluating and refining its own outputs through introspective prompting, where the agent is instructed to critically examine its proposed hypotheses, experimental designs, code implementations, or analytical conclusions, identify potential flaws or inconsistencies, and gen-

|RESEARCH GOAL: "Design and synthesize a high-capacity cathode material for Li-ion ba eries (>200 mAh/g, stable for 500+ cycles)"|
|---|


|V1 Self-Correction / Reflective Verification<br><br>|Self-critique: “Cycles 480 (<500) & Ni4+ unsafe. Try Mg-doped + Al2O3 coat”|
|---|
<br><br>![image 25](Ren et al._2025_Towards Scientific Intelligence A Survey of LLM-based Scientific Agents_images/imageFile25.png)<br><br>|Plan: LiNiO2 220 mAh/g|
|---|
<br><br>Planner|
|---|


I`ve got some results

|V2 Multi-Agent Critique / Role-Based Verification<br><br>|220 ✓| |
|---|---|
| | |
<br><br>Materials Designer<br><br>Safety Critic<br><br>Synthesis Engineer<br><br>Cost Critic<br><br>![image 26](Ren et al._2025_Towards Scientific Intelligence A Survey of LLM-based Scientific Agents_images/imageFile26.png)<br><br>![image 27](Ren et al._2025_Towards Scientific Intelligence A Survey of LLM-based Scientific Agents_images/imageFile27.png)<br><br>![image 28](Ren et al._2025_Towards Scientific Intelligence A Survey of LLM-based Scientific Agents_images/imageFile28.png)<br><br>![image 29](Ren et al._2025_Towards Scientific Intelligence A Survey of LLM-based Scientific Agents_images/imageFile29.png)<br><br>|Ni4+ ✗| |
|---|---|
| | |
<br><br>|Co ↑ ✗| |
|---|---|
| | |
<br><br>|O2 sensitive !| |
|---|---|
| | |
<br><br>|Consensus: not approved|
|---|
<br><br>|Plan: LiNiO2 220 mAh/ g| |
|---|---|
| | |
|
|---|


![image 30](Ren et al._2025_Towards Scientific Intelligence A Survey of LLM-based Scientific Agents_images/imageFile30.png)

![image 31](Ren et al._2025_Towards Scientific Intelligence A Survey of LLM-based Scientific Agents_images/imageFile31.png)

Report

Planner

Plan & Execute

|V3 Human-in-the-Loop / Expert Oversight<br><br>“Lower Co, good rate, ok safety—proceed... I think I can approve this.”<br><br>|Plan: Mn-rich Mg-coated cathode|
|---|
<br><br>![image 32](Ren et al._2025_Towards Scientific Intelligence A Survey of LLM-based Scientific Agents_images/imageFile32.png)<br><br>Expert Chemist|
|---|


|V4 Tool-Based Validation / Computational Verification<br><br>|Plan: LiNiO2 220 mAh/g|
|---|
<br><br>![image 33](Ren et al._2025_Towards Scientific Intelligence A Survey of LLM-based Scientific Agents_images/imageFile33.png)<br><br>|Code run: no syntax err|
|---|
<br><br>![image 34](Ren et al._2025_Towards Scientific Intelligence A Survey of LLM-based Scientific Agents_images/imageFile34.png)<br><br>![image 35](Ren et al._2025_Towards Scientific Intelligence A Survey of LLM-based Scientific Agents_images/imageFile35.png)<br><br>|DFT: ΔE = -3.1 eV vs Li+ (stable)|
|---|
<br><br>|Sim: capacity fade 0.02 % per cycle|
|---|
|
|---|


###### Figure 10: Different types of verification mechanisms of LLM-based scientific agents.

erate improved versions addressing the identified issues. This paradigm leverages the LLM’s capacity for meta-reasoning—the ability to reason about its own reasoning processes—through carefully designed prompts that trigger reflective evaluation modes, often by explicitly instructing the model to adopt a critical stance, sometimes augmented with structured critique templates that guide systematic evaluation across multiple dimensions (scientific validity, methodological soundness, computational feasibility, logical consistency). The iterative nature is critical: rather than accepting initial outputs as final, the agent engages in multi-turn self-dialogue where each iteration produces both a critique of the current version and a revised version addressing the critique, continuing until predefined stopping criteria are met.

Mechanistically, self-correction typically unfolds through reflection-revision cycles where the agent first generates an initial candidate output, then assumes a critical reviewer role producing a structured critique identifying specific issues, and finally generates a revised version attempting to address each identified issue. Implementation patterns vary by verification target: chain-of-thought and multi-round reflection for idea generation and hypothesis refinement where ideas are iteratively evaluated and improved across multiple reflection cycles (Lu et al., 2024a; Yamada et al., 2025; Li

- et al., 2024b; Wang et al., 2024b); code debugging and error correction where execution failures trigger automatic code revision with error messages guiding targeted fixes (Mandal et al., 2024; Moss, 2025; Novikov et al., 2025; Ye et al., 2023b;


- Liu et al., 2024b; Schmidgall et al., 2025; Xiao


- et al., 2024; Alber et al., 2025; Tang et al., 2025b; Pham et al., 2025; Huang et al., 2025c; Boiko et al.,

- 2023; Chen et al., 2024a; Ning et al., 2025; Ni and Buehler, 2024); self-consistency and retry mechanisms where multiple attempts are generated and evaluated for consistency or correctness (de Haan


- et al., 2025; Yin et al., 2025; Huang et al., 2024d); and iterative refinement with feedback incorporation where agents adjust experimental protocols, molecular designs, or analytical workflows based on self-generated critiques (Kumbhar et al., 2025; Ghafarollahi and Buehler, 2024a; Panapitiya et al.,


- 2025; Mehandru et al., 2025; Su et al., 2025; Zhang


- et al., 2025a; Tang et al., 2025d; Wu et al., 2025; Zhao et al., 2025; Sprueill et al., 2024; Weng et al.,


- 2025; Li et al., 2025a; Ansari et al., 2024; Zou et al.,


- 2025; Team et al., 2025a; Cao et al., 2024; Jia et al.,


2024; Maranto, 2024).

Representative implementations showcase diverse self-correction strategies, which are often combined with reflective planners (P3 of Section 2.1.1). For example, AI Scientist (Lu

- et al., 2024a) leverages chain-of-thought and selfreflection across multiple stages: multiple rounds for refining ideas, up to four retry attempts for experiment iteration when failures occur, one round of self-reflection during initial section writing plus a final round section-by-section for paper refinement, and 5 rounds of self-reflection to improve automated reviewer decision-making. OriGene (Zhang et al., 2025e) implements multi-round hypothesis refinement where hypothesis generation modules produce initial therapeutic target candidates, evaluation modules assess validity and novelty, and feedback loops enable iterative improvement across cycles until quality thresholds are met. DrugPilot (Li et al., 2025a) introduces the feedbackfocus (Fe-Fo) mechanism during drug reasoning and discovery process, to help LLMs correct common reasoning errors when interpreting PMP and invoking tools, and to maintain focus on the original task in extended dialogues. CellVoyager (Alber
- et al., 2025) incorporates a self-critiquing mechanism where it generates and tests new hypotheses within a Jupyter notebook environment, and if the code produces an error, the agent rewrites the code, and it also reflects on its current exploration blueprint, modifying it as necessary, and replans the next steps based on code execution outputs and error messages. Similarly, The Experiment Execution Module of the virtual cell models optimization agent CellForge (Tang et al., 2025d) includes a Code Generator that self-debugs by receiving tracebacks, analyzing failures, patching code, and re-executing until unit tests pass or a rollback is triggered. The chemist AI agent dZiner (Ansari et al., 2024) leverage the self-reflection mechanism that iteratively reviews the modified materials and the entire modification history, stopping the generation of new candidates once the convergence criteria are met. For chemical reasoning, ChemAgent (Tang et al., 2025b) examines sub-solutions for conflicts with fundamental knowledge or common errors, and if discrepancies are identified, a new sub-solution is generated by refining the original. If a sub-task fails due to insufficient conditions or misalignment with the main task, the sub-tasks are restructured. The self-evolution analysis shows that ChemAgent can enhance its performance through


a simple correct-or-not evaluation of past solutions. Similarly, ChemOrch (Huang et al., 2025c) introduces multi-stage self-repair mechanism where if execution of a script fails, the model captures the error trace and attempts to repair until success or a retry limit is reached, or it consults external documentation and regenerates the scrip. ToRA (Gou et al., 2024) employs multi-round self-correction

- as part of its tool-integrated mathematical reasoning format. When a program execution yields an unexpected output or an error, the model generates a new rationale to adjust its approach or correct the subsequent portions of an invalid trajectory. ASA (Liu et al., 2024b) includes a Python code debugging process as the self-correction strategy, for autonomous polymer physics and celestial mechanics simulation. When bugs are detected, error messages are passed to the LLM, which is then prompted to revise the code. This process is iterative until the code executes correctly. Similarly, GeoAgent (Chen et al., 2024a) employs a self-refinement algorithm involving an iterative refinement process within a MCTS tree, for complex geospatial data analysis tasks. In the event of undefined variables, it removes the problematic subtree and inserts a new task to define the variable. For incorrect function calls, static analysis tools (like Python Jedi) retrieve accessible APIs to guide the LLM to regenerate the node.


Self-correction provides valuable first-pass error detection without external dependencies, enabling rapid iteration. However, fundamental limitations include single-model blind spots where systematic biases persist across reflection iterations, absence of external grounding for detecting factual inaccuracies, and potential for hallucinated critiques—motivating complementary verification through multi-agent systems, human experts, or external tools.

- 2.4.2 V2. Multi-Agent Critique / Role-Based Verification


Multi-agent critique or role-based verification implements collaborative validation through multiple LLM instances assigned distinct evaluative perspectives, where specialized critic agents—each embodying particular expertise domains, evaluation criteria, or critical stances—independently assess proposed hypotheses, experimental designs, or analytical conclusions from their respective viewpoints, producing diverse critiques that collectively provide more comprehensive error detection than

single-agent self-correction. This approach leverages role specialization and perspective diversity: by assigning agents different critical lenses, the system can identify a broader range of potential issues spanning multiple dimensions of scientific validity. The multi-agent architecture introduces constructive tension—agents may disagree in their assessments, requiring synthesis or adjudication mechanisms to resolve conflicts—and enables more sophisticated verification workflows including debatestyle adversarial review, consensus-building, and hierarchical review.

Mechanistically, multi-agent critique systems instantiate multiple LLM instances with differentiated system prompts that define their roles, expertise domains, and evaluative responsibilities, just as described in P5 of Section 2.1.1. A typical workflow proceeds as follows: a generator agent produces an initial output; multiple critic agents receive this output along with role-specific prompts defining their evaluation criteria; each critic independently generates a review highlighting issues from their perspective; critiques are aggregated to form comprehensive feedback; and either the original generator agent or a dedicated revision agent produces an improved version addressing the collected critiques. Implementation patterns include: paper review and scientific evaluation where reviewer agents simulate peer review processes providing feedback on research quality, novelty, and methodological soundness (Schmidgall et al., 2025; Lu et al., 2024a; Yamada et al., 2025; Weng et al., 2025); specialized domain critique where agents evaluate different technical aspects such as diversity, feasibility, and scientific rigor (Kumbhar et al., 2025; Ghafarollahi and Buehler,

- 2024a; Su et al., 2025; Tang et al., 2025b; Hu et al.,
- 2025a; Lai and Pu, 2025); debate and tournamentbased evaluation where multiple agents argue positions or compete in pairwise comparisons to assess relative quality (Gottweis et al., 2025; Li et al., 2024b); and graph-structured collaborative refinement where expert agents exchange proposals and critiques through structured message-passing until convergence (Tang et al., 2025d; Team et al., 2025a; Ghafarollahi and Buehler, 2024c, 2025; Su et al., 2024).


Representative systems demonstrate sophisticated multi-agent critique architectures. AI co-scientist (Gottweis et al., 2025) implements tournament-style debate where four debate agents (two for and two against a research proposal) en-

gage in structured argumentation, a judge agent evaluates arguments and declares winners, and a meta-review agent synthesizes insights from multiple tournament rounds to identify recurring patterns and optimize agent performance in subsequent iterations. MedAgents (Tang et al., 2023) incorporates a role-playing setting with multi-round discussions to enhance zero-shot medical reasoning, where several expert agents give their votes (yes/no) on a preliminary summary report and propose modification opinions if they vote no. The report is then revised based on these modifications iteratively until all experts agree or a maximum attempts threshold is reached. VirSci (Su et al., 2024) implements structured idea refinement through critic agents who evaluate generated research ideas for novelty, feasibility, and impact potential, with low-scoring ideas filtered out and high-scoring ideas refined through targeted feedback. Other agents implement special critic agents for verification. For example, CellAgent (Xiao et al., 2024) employs a multi-agent critique mechanism where the Evaluator agent assesses the quality of current results and allows the Executor to optimize solutions based on evaluation or potential code exceptions, through hyperparameter tuning or tool selection, for automated, high-quality single-cell RNA sequencing data analysis. The protein design discovery agent Sparks (Ghafarollahi and Buehler, 2025) utilizes a generation–reflection strategy where each core agent is paired with a corresponding reflection agent. These reflection agents evaluate the output of their generator counterparts for clarity, novelty, feasibility, technical correctness, completeness, and adherence to system standards. AccelMat (Kumbhar et al., 2025) employs specialized critic agents: a Diversity Critic evaluating whether proposed hypotheses explore sufficiently diverse regions of the materials space avoiding redundant similar proposals, a Feasibility Critic assessing whether hypotheses are experimentally realizable given available equipment and constraints, and a Scientific Rigor Critic checking whether hypotheses are grounded in valid scientific principles with clear testable predictions. STELLA (Jin et al., 2025) orchestrates a multi-agent ecosystem where a Dev Agent focuses on environment building, code creation, model training, and report writing, and a Critic Agent that assesses intermediate results, identifies flaws, and provides actionable feedback to refine the approach, creating a robust, iterative problem-solving loop. AtomAgents (Ghafarollahi and Buehler, 2024a) incorporates the

’Critic’ agent performing role-based verification by evaluating the plan proposed by the ’Planner’ agent, ensuring its completeness and correctness. AutoLabs (Panapitiya et al., 2025) utilizes a multi-agent architecture where a supervisor agent orchestrates workflow among specialized sub-agents. These sub-agents (e.g., Understand and Refine, Chemical Calculations, Vial Arrangement, Processing Steps, Final Steps) collaboratively decompose experimental goals into discrete tasks, and the Self-Checks agent acts as a final verification step.

Multi-agent critique provides comprehensive error coverage through diverse perspectives and supports sophisticated collaborative reasoning patterns. However, challenges include coordination overhead from managing multiple agents and synthesizing conflicting feedback, increased computational costs from invoking multiple LLM instances, and potential echo chambers where agents share underlying model biases despite different role prompts—motivating integration with human oversight and external tools for authoritative validation.

2.4.3 V3. Human-in-the-Loop / Expert Oversight

Human-in-the-loop (HITL) or expert oversight verification integrates human domain experts directly into the agent workflow, positioning them as authoritative evaluators who review agent-generated outputs at critical decision points, provide binding approval or rejection decisions, offer qualitative feedback that informs subsequent agent reasoning, and intervene when automated verification mechanisms fail to resolve ambiguities or when the stakes of decisions demand human judgment. This paradigm recognizes fundamental limitations of purely automated verification: LLMs lack genuine understanding of physical reality and cannot reliably detect all classes of errors, particularly those requiring deep domain expertise, tacit knowledge, or awareness of subtle contextual factors. HITL verification is particularly critical for high-stakes scientific workflows where errors could waste expensive experimental resources, compromise safety, or lead to false scientific claims.

Mechanistically, HITL verification integrates human interaction points into otherwise-automated agent workflows, with integration patterns varying along a spectrum from continuous oversight to selective intervention to exception-based involvement. Common interaction modalities span diverse use cases: approval gates for experimental proto-

cols and safety-critical procedures where agents pause execution to present synthesis procedures, robotic control sequences, or hazardous operations awaiting explicit human approval before proceeding (Mandal et al., 2024; Boiko et al., 2023; Zhou

- et al., 2025; Wang et al., 2025a); evaluation and feedback on research outputs where human domain experts assess scientific quality, novelty, and validity of generated hypotheses, papers, or experimental designs providing qualitative critiques that inform refinement (Xin et al., 2024; Bran et al.,


- 2024; Ansari et al., 2024; Schmidgall et al., 2025; Lu et al., 2024a; Gottweis et al., 2025; Tang et al.,
- 2025a; de Haan et al., 2025; Yin et al., 2025; Ghafarollahi and Buehler, 2024a; Mehandru et al., 2025; Roohani et al., 2024; Su et al., 2025; Li et al.,


- 2024b; Tang et al., 2025d; Alber et al., 2025; Tang


- et al., 2025b; Zhao et al., 2025; Weng et al., 2025; Team et al., 2025a; Ghareeb et al., 2025; Su et al.,


- 2024); collaborative human-AI iteration where scientists and agents engage in multi-turn dialogues with humans providing guidance, constraints, or corrections that shape agent exploration (Zhang et al., 2025d; Gottweis et al., 2025; Novikov et al.,
- 2025; Pham et al., 2025; Ansari et al., 2024; Zou et al., 2025; Jin et al., 2024; He et al., 2025; Baek


- et al., 2024); and intervention for debugging and error resolution where automated self-correction fails and human experts manually edit code, adjust parameters, or redirect workflows (Chen et al.,

- 2024a; Cao et al., 2024; Ni and Buehler, 2024). Representative implementations illustrate di-


verse HITL integration strategies. Agent Laboratory (Schmidgall et al., 2025) is designed to assist human scientists to do machine learning research, enabling users to provide feedback and guidance at each stage, i.e., high-level notes for improvement or deciding to proceed. StarWhisper (Wang

- et al., 2025a) integrates astronomers into telescope operation workflows where the agent interprets natural language observation requests, generates specific telescope control sequences, presents planned observations to astronomers for verification that they match intended scientific goals, and executes only after plan revising and approval by humans. ORGANA (Darvish et al., 2025) engages with chemists via natural language to clarify goals, handle disambiguation, and provide updates about experiments. A HITL approach is adopted where ORGANA.REASONER prompts the user to investigate and decide on further actions if experimental outcomes do not match expectations. BIA (Xin


et al., 2024) incorporate human intervention at critical junctures to ensure accuracy and relevance. When undertaking dynamic workflows, such as subset segmentation, manual intervention tends to be indispensable to guarantee precision and tailor the process to particular needs. The chemistry agent ChemCrow (Bran et al., 2024) conduct evaluation was by a panel of four expert chemists who assessed the performance across three dimensions: Correctness of the chemistry, Quality of reasoning, and Degree of task completion. Human interaction is also required to fix invalid actions in synthesis procedures before execution on the robotic platform if ChemCrow cannot autonomously adapt them. dZiner (Ansari et al., 2024) supports both closed-loop and human-in-the-loop feedback cycles enabling human-AI collaboration in molecular design. In a human-in-the-loop process, a chemist can review the agent’s proposed candidates and reasoning, offering feedback and suggesting additional modifications or constraints. Chemma (Zhang et al., 2025d) integrates in an active learning framework, where chemists interact with Chemma by providing feedback from collected wet experiment results. This human-AI collaboration is crucial for autonomously experimental exploration and optimization in open reaction spaces, and for fine-tuning Chemma to better adapt to specific reactions. MAPPS (Zhou et al., 2025) integrates scientists into the discovery loop where the framework generates materials hypotheses and experimental designs, presents them to domain experts for evaluation and ranking, incorporates expert feedback to refine proposals, and requires explicit scientist approval before initiating computationally expensive simulations or experimental syntheses. Similarly, MatPilot (Ni et al., 2024) develops a humanmachine collaboration framework through natural language interaction, where human experts contribute domain knowledge, research experience, and strategic guidance, infusing the system’s innovation process with high-level professional insights and verification. ResearchAgent (Baek et al., 2024) incoporates human evaluation to validate, involving assigning scores for criteria and conducting pairwise comparisons between ideas, with expert researchers judging ideas generated based on their own papers. Robin (Ghareeb et al., 2025) involves clinicians throughout drug discovery where the agent identifies therapeutic target candidates and biomarkers, presents rationales and supporting evidence to medical domain experts, incorporates

feedback on clinical relevance and biological plausibility, and proceeds to experimental validation only for expert-approved candidates.

HITL verification provides irreplaceable benefits including authoritative quality assurance, safetycritical oversight, and credibility for agent-assisted discoveries. However, challenges include expert bottlenecks creating delays and throughput constraints, subjectivity where experts may provide conflicting assessments, and cost concerns for continuous involvement—motivating active learning approaches that focus expert attention on highuncertainty decisions and automated mechanisms handling routine validation.

- 2.4.4 V4. Tool-Based Validation / Computational Verification


Tool-based validation or computational verification leverages external computational tools, simulators, databases, and execution environments to objectively assess the correctness, feasibility, or performance of agent-generated outputs through empirical testing rather than relying solely on LLM reasoning or human judgment. This paradigm implements ground-truth verification by executing agent proposals in controlled computational environments and observing outcomes: running agentgenerated code to detect syntax errors, logic bugs, or runtime failures; simulating agent-proposed chemical reactions or physical processes to verify thermodynamic feasibility and predict outcomes; querying authoritative databases or APIs to factcheck claims about chemical properties, biological pathways, or experimental precedents. Toolbased verification provides uniquely valuable objective signals that are independent of LLM biases and hallucination tendencies—if agent-generated code raises a syntax error when parsed, a proposed molecule violates established chemical valence rules when checked, or a simulated experiment fails to produce predicted outcomes, these constitute definitive evidence of errors requiring correction.

Mechanistically, tool-based validation integrates external computational resources into agent workflows through several architectural patterns. Code execution and testing where agent-generated programs are run in sandboxed environments, capturing outputs, error messages, and execution traces, providing feedback for debugging and refinement through iterative correction until code executes successfully (Schmidgall et al., 2025; Moss, 2025; Lu

- et al., 2024a; Yamada et al., 2025; Mandal et al.,

- 2024; Novikov et al., 2025; Ye et al., 2023b; Liu

et al., 2024b; Yin et al., 2025; Ghafarollahi and Buehler, 2024a; Panapitiya et al., 2025; Mehandru et al., 2025; Su et al., 2025; Xiao et al., 2024; Tang et al., 2025d; Alber et al., 2025; Tang et al.,

- 2025b; Pham et al., 2025; Boiko et al., 2023; Weng et al., 2025; Li et al., 2025a; Zou et al., 2025; Chen et al., 2024a; Team et al., 2025a; Cao et al.,




- 2024; Ning et al., 2025; Maranto, 2024; Zhou et al., 2025; Ni and Buehler, 2024); simulatorbased physics and chemistry validation where agent proposals are fed into domain-specific simulators including molecular dynamics engines, computational fluid dynamics solvers, circuit simulators, quantum chemistry packages, executing simulations to predict properties or behaviors, comparing predictions against agent claims or design requirements (Novikov et al., 2025; Gottweis et al., 2025; Ghafarollahi and Buehler, 2024a; Panapitiya et al.,
- 2025; Tang et al., 2025d; Boiko et al., 2023; Ansari


- et al., 2024; Jia et al., 2024; Maranto, 2024; Zhou
- et al., 2025; Ni and Buehler, 2024); and database and API factual cross-checking validating factual claims by querying authoritative external sources, verifying chemical properties, gene-disease associations, or experimental protocols against validated repositories (Gottweis et al., 2025; Lu et al., 2024a; Yin et al., 2025; Ghafarollahi and Buehler, 2024a; Panapitiya et al., 2025; Luo et al., 2022; Li et al., 2024c; Tang et al., 2025d; Huang et al., 2025c; Li et al., 2024b; Boiko et al., 2023; Li et al., 2025a; Ansari et al., 2024; Maranto, 2024; Polat et al., 2025).


Representative systems showcase sophisticated tool-based validation strategies. Agent Laboratory (Schmidgall et al., 2025) implements comprehensive code execution verification where generated Python code is executed in controlled environments, runtime errors and exceptions are captured and fed back to debugging agents, test suites verify functional correctness, and performance metrics assess efficiency, with the revision cycle continuing until all tests pass and performance meets criteria. SGA (Ma et al., 2024a) couples LLMgenerated hypotheses (novel algorithmic ideas for physics simulations) with physics simulators executing these ideas: the simulator provides objective performance measurements which serve as definitive validation of whether LLM-generated concepts actually work, creating bilevel optimization loop where simulation feedback guides ideation.

Coscientist (Boiko et al., 2023) integrates chemical validity checking through RDKit cheminformatics library to verify molecular structures, reaction feasibility assessment using reaction prediction tools, and experimental verification where agent-designed synthesis procedures are executed by robotic lab equipment with sensors providing objective outcome data. AILA (Mandal et al., 2024) implements AFM simulator-based validation where it employs a Code Executor tool to run Python code directly on the local system for operating the AFM, and it returns a success message or a detailed error description, allowing for systematic addressing of issues in the script. GeoSim.AI (Bekele, 2025) validates geological simulation setups by invoking domain-specific checkers verifying parameter ranges fall within physically meaningful bounds, mesh configurations satisfy numerical stability criteria, and boundary conditions are self-consistent before launching computationally expensive finite element simulations. ToRA (Gou et al., 2024) validates mathematical reasoning by executing agentgenerated code computing numerical solutions, comparing results against known ground truth for test problems, and accepting reasoning chains only when computational results match expected answers within tolerance thresholds. BioDiscoveryAgent (Roohani et al., 2024) validates genetic perturbation experiment designs by querying gene expression databases to verify proposed interventions target actually existing genes, biological pathway databases to confirm mechanistic plausibility, and prior experimental literature to check whether similar perturbations have been attempted. Similarly, xChemAgents (Polat et al., 2025) performs factual cross-check through the Selector agent querying a descriptor pool provided with the enriched QM9 dataset, with the descriptors themselves augmented with metadata retrieved from PubChem, which serves as a factual database for chemical information.

Tool-based validation provides objective verification grounded in computational ground truth, enables automated validation at scale, and generates quantitative metrics guiding refinement. However, limitations include tool availability where many domains lack mature validation tools, fidelity concerns where simulators may not perfectly capture real-world phenomena, and computational cost for high-fidelity simulations—motivating multifidelity validation pipelines and learned surrogate models for efficient large-scale validation.

#### 2.5 Discussion

The most robust scientific agents employ layered verification architectures combining multiple types, creating defense-in-depth quality assurance where mechanisms address complementary error classes. Self-correction provides rapid first-pass refinement; multi-agent critique adds diverse specialized perspectives; human oversight supplies authoritative validation; and tool-based validation offers objective empirical grounding. Representative integrated systems include AIGS (Liu et al., 2024c) combining self-correction, multi-agent critique, human review, and simulator/physical validation in iterative cycles; Agent Laboratory (Schmidgall et al., 2025) integrating self-optimization, multi-agent review, and tool-based execution testing; AtomAgents (Ghafarollahi and Buehler, 2024a) combining self-critique, specialist agents, human approval, and DFT validation; and Coscientist (Boiko et al., 2023) employing self-correction, multi-agent feedback, human safety gates, and physical experiment execution.

Verification strategy selection depends on multiple factors. Task criticality drives HITL integration for drug discovery and hazardous chemistry (Inoue et al., 2024; Ghareeb et al., 2025; Boiko et al., 2023; Panapitiya et al., 2025) versus automated verification for computational research (Lu et al., 2024a). Domain maturity enables tool-based validation in chemistry, physics, and biology with established simulators and databases (Bran et al., 2024; McNaughton et al., 2024; Ma et al., 2024a; Ni and Buehler, 2024; Pandey et al., 2025; Ghafarollahi and Buehler, 2024b; Roohani et al., 2024), while emerging domains rely more on model-based and human verification. Cost constraints shape depth: rapid iteration uses lightweight self-correction (Li

- et al., 2024b; Wang et al., 2024b), while highvalue campaigns justify expensive validation (Zhou
- et al., 2025; Ghafarollahi and Buehler, 2024a). Automation requirements influence architecture: autonomous systems rely on self-correction and tools (Lu et al., 2024a; Weng et al., 2025), while collaborative systems integrate experts throughout (Baek et al., 2024; Su et al., 2024).


Emerging challenges include developing metaverification assessing signal reliability, adaptive verification dynamically adjusting depth based on uncertainty, verification-aware learning where agents learn to generate proposals likely to pass validation, and formal verification frameworks

providing guarantees for safety-critical applications—advances critical for deploying agents in autonomous, high-stakes workflows.

### 3 Benchmarks

Benchmarks are basic solutions for evaluating the efficacy of LLM-based scientific agents, ensuring their capability to handle the multifaceted demands of scientific research. They are designed to measure various aspects of these agents’ performance, from basic problem-solving, such as fundamental cognitive and analytical skills, to complex scientific research, such as some research-oriented paper reading and experiment designing abilities. In this section, we classify the evaluation benchmarks into two categories: general reasoning ability as in subsection 3.1 and domain-specific scientific capability

- as in subsection 3.2, as shown in Figure 11.


#### 3.1 General Reasoning Ability Evaluation

General reasoning ability evaluation focuses on assessing the fundamental cognitive and analytical skills of LLM-based scientific agents. These benchmarks measure problem-solving capabilities in mathematical reasoning, logical inference, and domain-specific knowledge retrieval, ensuring that agents can perform essential tasks required for scientific research and higher education. By evaluating models across different levels, from K-12 foundational skills to higher education and expert-level assessments, these benchmarks provide insights into the reasoning proficiency and adaptability of LLMs in various academic disciplines. We summarize the available benchmarks in Table 2.

K-12 Foundational Skills: At the foundational level, agents are expected to exhibit proficiency in key areas such as geometry (plane and analytic geometry), algebraic operations, logical reasoning, and basic statistical analysis. Benchmarks like Geometry3K (Lu et al., 2021) and GeoEval (Zhang et al., 2024b) assess geometric reasoning. MathVista (Lu et al., 2024b) is used for algebra and statistical tasks intertwined with visual understanding. Meanwhile, VisScience (Jiang et al., 2024) broadens this focus by integrating visual reasoning tasks within mathematics, physics, and chemistry contexts. PhysicsQA (Jaiswal et al., 2024) comprises 370 carefully selected high school physics questions requiring application of multiple concepts, intricate computations, and multihop reasoning, with the Mixture of Refinement Agents

framework demonstrating significant accuracy improvements through iterative refinement. These test agents’ abilities to solve geometric problems, understand algebraic concepts, and make statistical inferences—critical skills for advancing to higher levels of scientific reasoning.

Higher Education Level: As agents progress, they must handle more advanced tasks such as scientific computing, retrieval of domain-specific knowledge, and application of this knowledge to solve complex scientific problems. Key benchmarks include SciBench (Wang et al., 2024c) and SciEval (Sun et al., 2024a). These datasets evaluate how well agents engage in advanced scientific tasks such as solving problems in physics, chemistry, and biology, along with retrieving and applying knowledge from scientific literature. Expanding the multimodal dimension, MME-SCI (Ruan et al., 2025) provides a comprehensive evaluation of multimodal large language models in scientific contexts with 1,019 question-answer pairs covering mathematics, physics, chemistry, and biology across five languages, highlighting the importance of integrating visual and textual reasoning. Domain-specific benchmarks further assess specialized knowledge: EarthSE (Xu et al., 2025a) evaluates capabilities in Earth sciences covering five Earth spheres and 114 disciplines through foundational question-answering datasets (Earth-Iron and Earth-Silver) and an advanced open-ended multiturn dialogue dataset (Earth-Gold) for scientific exploration; AstroMMBench (Shi et al., 2025) focuses on astronomical image interpretation with 621 multiple-choice questions across six astrophysical subfields, curated by domain experts to assess models’ understanding of complex astronomical data. Such benchmarks reflect the complexities of real-world research in academic and professional settings.

Graduate and Expert Level: At the most advanced levels, benchmarks challenge agents with problems requiring deep expertise and sophisticated reasoning. GPQA (Rein et al., 2024) presents graduate-level questions in physics, chemistry, and biology that are challenging even with internet access, testing models’ depth of understanding. Similarly, SuperGPQA (Team et al., 2025b) introduces a broader evaluation framework, covering 285 specialized academic fields, including light industry, agriculture, and service-oriented disciplines. This benchmark underscores the need for advancements in LLM reasoning across diverse knowledge do-

Geometry3K (Lu et al., 2021), GeoEval (Zhang et al.,

K-12 Foundational Skills

2024b), VisScience (Jiang et al., 2024), MathVista (Lu et al., 2024b), PhysicsQA (Jaiswal et al., 2024), etc.

SciBench (Wang et al., 2024c), SciEval (Sun et al., 2024a), MME-SCI (Ruan et al., 2025), EarthSE (Xu et al., 2025a), AstroMMBench (Shi et al., 2025), etc.

Higher Education Level

General Reasoning Ability Evaluation

GPQA (Rein et al., 2024), SuperGPQA (Team et al., 2025b), CosmosPaperQA (Xu et al., 2025c), JEEBench, HLE (Phan et al., 2025), TRQA (OriGene), FrontierMath (Glazer et al., 2024), OlympiadBench (He et al., 2024), etc.

Graduate & Expert Level

Scientific Paper Chart Comprehension

FigureQA (Kahou et al., 2018), ArXivQA (Li et al., 2024a), MMSCI (Li et al., 2024f), etc.

Benchmarks

SciMON (Wang et al., 2024b), MOOSE-Chem (Yang et al., 2024c), ResearchBench (Liu et al., 2025), PaperArena (Wang et al., 2025b), DiscoveryBench (Majumder et al., 2024), DiscoveryWorld (Jansen et al., 2024), AstaBench (Bragg et al., 2025), ScienceBoard (Sun et al., 2025), etc.

Scientific Hypothesis Discovery

Scientific Research-Oriented Ability Evaluation

GAIA (Mialon et al., 2023), TaskBench (Shen et al., 2024), MLAgentBench (Huang et al., 2024b), DiscoveryWorld (Jansen et al., 2024), DSBench (Jing et al., 2024), ScienceAgentBench (Chen et al., 2024b), SciCode (Tian et al., 2024), LABBench (Laurent et al., 2024), BixBench (Mitchener et al., 2025), BioML-bench (Miller et al., 2025), CellBench (Alber et al., 2025), ChemToolBench (Wu et al., 2025), AFMBench (Mandal et al., 2024), ThinkGeo (Singh et al., 2024), MLE-bench (Chan et al., 2024), RAS-Eval (Fu et al., 2025b), Core-bench (Siegel et al., 2024), etc.

Experimental Design and Automation

- Figure 11: Taxonomy of the LLM-based scientific agents evaluation benchmarks with newly added benchmarks (2024-2025)


- Table 2: Summary of benchmarks for general reasoning ability evaluation in LLM-based scientific agents. "General" means a benchmark is not designed for a particular discipline


|Benchmark Name<br><br>|Scope Size Discipline|
|---|---|
|Geometry3K (Lu et al., 2021) GeoEval (Zhang et al., 2024b) VisScience (Jiang et al., 2024) MathVista (Lu et al., 2024b) PhysicsQA (Jaiswal et al., 2024) SciBench (Wang et al., 2024c) SciEval (Sun et al., 2024a) MME-SCI (Ruan et al., 2025) EarthSE (Xu et al., 2025a) AstroMMBench (Shi et al., 2025) CosmosPaperQA (Xu et al., 2025c) JEEBench (Arora et al., 2023) GPQA (Rein et al., 2024) SuperGPQA (Team et al., 2025b) TRQA (Zhang et al., 2025e) OlympiadBench (He et al., 2024) HLE (Phan et al., 2025) FrontierMath (Glazer et al., 2024)|K-12 3002 Mathematics K-12 5050 Mathematics K-12 3000 Physics & Chemistry & Mathematics<br><br>K-12 & College 6141 Mathematics<br><br>K-12 370 Physics<br><br>College 869 Physics & Chemistry & Mathematics<br><br>College 18000 Physics & Chemistry & Biology<br><br>College 1019 Physics & Chemistry & Biology & Mathematics<br><br>College - Earth Sciences<br><br>College 621 Astronomy<br><br>Graduate-Level 105 Astrophysics<br><br>Graduate-Level 515 Mathematics & Physics & Chemistry<br><br>Graduate-Level 448 Physics & Chemistry & Biology<br><br>Graduate-Level 26529 General<br><br>Expert-Level 1900 Biomedical<br><br>Expert-Level 8476 Mathematics & Physics<br><br>Expert-Level 3000 Humanity & Science & Mathematics<br><br>Expert-Level 350 Mathematics|


- Table 3: Summary of benchmarks for scientific research-oriented abilities evaluation in LLM-based scientific agents. FC=Scientific Figure Comprehension; HD=Hypothesis Discovery; ED=Experiment Design; EW= Experiment Execution & Workflow Automation. "General" means a benchmark is not designed for a particular discipline


|Benchmark Name<br><br>|FC HD ED EW Discipline|
|---|---|
|FigureQA (Kahou et al., 2018) ArXivQA (Li et al., 2024a) MMSCI (Li et al., 2024f) SciMON (Wang et al., 2024b) MOOSE-Chem (Yang et al., 2024c) ResearchBench (Liu et al., 2025) DiscoveryBench (Majumder et al., 2024) PaperArena (Wang et al., 2025b) GAIA (Mialon et al., 2023) TaskBench (Shen et al., 2024) MLAgentBench (Huang et al., 2024b) DiscoveryWorld (Jansen et al., 2024) LAB-Bench (Laurent et al., 2024) DSBench (Jing et al., 2024) ScienceAgentBench (Chen et al., 2024b) SciCode (Tian et al., 2024) BixBench (Mitchener et al., 2025) BioML-bench (Miller et al., 2025) CellBench (Alber et al., 2025) ChemToolBench (Wu et al., 2025) AFMBench (Mandal et al., 2024) ThinkGeo (Singh et al., 2024) MLE-bench (Chan et al., 2024) RAS-Eval (Fu et al., 2025b) ScienceBoard (Sun et al., 2025) AstaBench (Bragg et al., 2025) Core-bench (Siegel et al., 2024)|- - - General<br><br>- - - General<br><br>- - - General<br>- - - NLP & Biomedical<br><br>- - - Chemistry & Material Science<br><br>- - - General<br><br>- - - Social Science & Biology & Humanity<br><br>- - - General<br><br>- - General<br><br>- - - General<br><br>- - General<br><br>- General<br><br>- - - Biology<br><br>- - - Data Science<br><br>- - - Psychology & Bioinformatics & Geomatics & Chemistry<br><br>- - - Physics & Chemistry & Mathematics & Biology<br><br>- - Computational Biology<br><br>- - Bioinformatics<br><br>- - - Single-cell Biology<br><br>- - Chemistry & Materials<br><br>- - Materials Science<br><br>- - - Geospatial<br><br>- - Machine Learning<br><br>- - - Security<br><br>- General<br><br>- General<br><br>- - Computational Reproducibility<br><br><br>|


mains and provides valuable insights into largescale expert-driven dataset construction. CosmosPaperQA (Xu et al., 2025c) provides 105 expertcurated question-answer pairs derived from highlycited cosmological literature, capturing authentic research scenarios by extracting questions directly from research papers. JEEBench (Arora et al.,

- 2023) presents 515 challenging pre-engineering problems from the highly competitive IIT JEEAdvanced exam, requiring long-horizon reasoning on top of deep in-domain knowledge across mathematics, physics, and chemistry. Humanity’s Last Exam (HLE) (Phan et al., 2025) has been introduced as a more challenging measure of LLM capabilities in response to the saturation of existing benchmarks. It consists of 3,000 rigorous questions across a wide range of disciplines, including mathematics, humanities, and natural sciences. Unlike traditional benchmarks, the questions in HLE are designed to be extremely difficult and unsearchable through basic internet retrieval, making it a critical test for evaluating the limits of current LLM performance. The benchmark highlights a significant gap between the capabilities of stateof-the-art LLMs and expert-level knowledge in closed-ended academic tasks. TRQA (Zhang et al.,


- 2025e) comprises over 1,900 expert-level question-


answer pairs spanning therapeutic target discovery, with TRQA-lit focusing on literature-based biological research and TRQA-db emphasizing database-derived competitive landscape analysis. FrontierMath (Glazer et al., 2024) pushes boundaries further with Olympiad-level mathematics problems requiring creative problem-solving and advanced mathematical insight beyond standard curriculum knowledge. OlympiadBench (He et al., 2024) features 8,476 problems from Olympiadlevel mathematics and physics competitions with expert-level annotations for step-by-step reasoning, representing the pinnacle of pre-collegiate scientific problem-solving.

3.2 Scientific Research-Oriented Ability Evaluation

While general reasoning benchmarks assess broad problem-solving and analytical skills, scientific research-oriented benchmarks evaluate the ability of LLM-based scientific agents to perform specialized scientific tasks. These include extracting and interpreting data from research papers, discovering novel scientific hypotheses, and designing and automating experimental procedures. By simulating real-world scientific workflows, these benchmarks help measure the extent to which LLMs can func-

tion as effective tools for scientific discovery and innovation. Table 3 presents a categorized summary of these benchmarks.

Scientific Paper Chart Comprehension: Understanding and interpreting data visualizations in scientific papers is a fundamental skill for agents in research environments. Benchmarks such as FigureQA (Kahou et al., 2018), ArXivQA (Li et al.,

- 2024a) and MMSCI (Li et al., 2024f) test agents’ ability to comprehend and reason over figures, including graphs, charts, and tables, from scientific papers. These are essential for tasks such as literature reviews, where agents need to extract and comprehend information from graphical data.

Scientific Hypothesis Discovery: A critical task in scientific research is the generation of novel hypotheses from existing literature or experimental data. Datasets like SciMON (Wang et al., 2024b) and MOOSE-Chem (Yang et al., 2024c) focus on deriving new scientific discoveries by analyzing key sections of existing literature, such as abstracts and methodologies. ResearchBench (Liu et al.,

- 2025) introduces a large-scale benchmark specifically designed to evaluate LLMs in inspiration retrieval, hypothesis composition, and hypothesis ranking, covering 12 scientific disciplines. PaperArena (Wang et al., 2025b) addresses the more complex challenge of cross-paper reasoning, evaluating agents’ abilities to integrate information across multiple scientific papers using tool-augmented reasoning for parsing multimodal data, retrieving relevant contexts, and performing computations. In contrast, DiscoveryBench (Majumder et al., 2024) and DiscoveryWorld (Jansen et al., 2024) emphasize the exploration of novel findings based on experimental data. Comprehensive end-to-end benchmarks have emerged to evaluate the complete research pipeline: AstaBench (Bragg et al., 2025) introduces rigorous benchmarking spanning from ideation to execution, assessing agents’ ability to complete a research project from initial ideas to final reports and code; ScienceBoard (Sun et al.,


- 2025) offers a multimodal evaluation framework for autonomous agents in realistic scientific workflows across multiple domains. These benchmarks collectively challenge agents to extract meaningful insights from both textual sources and empirical observations, evaluating their ability to generate and refine scientific hypotheses. Such capabilities are essential for driving forward scientific innovation.


Experimental Design and Automation: The ability to design experiments, decompose complex

tasks, and automate scientific workflows is critical for LLM-based scientific agents. DiscoveryWorld (Jansen et al., 2024), DSBench (Jing et al., 2024) and ScienceAgentBench (Chen et al., 2024b) assess agents’ capabilities in hypothesis-driven and datadriven experimental design, focusing on scientific discovery and real-world data science tasks. ScienceAgentBench in particular comprises 102 tasks derived from 44 peer-reviewed publications across psychology, bioinformatics, geomatics, and chemistry, validated by domain experts with diverse evaluation metrics. Meanwhile, SciCode (Tian et al.,

- 2024) focuses on problem-solving through code generation for domain-specific scientific challenges across physics, chemistry, mathematics, and biology. For workflow automation, GAIA (Mialon et al., 2023), TaskBench (Shen et al., 2024) and MLAgentBench (Huang et al., 2024b) evaluate an agent’s ability to structure tasks, iterate on models, and optimize performance in general scenarios.

Domain-specific benchmarks have emerged to evaluate experimental design and automation in specialized fields. In biological sciences, LABBench (Laurent et al., 2024) tests protocol planning, data analysis, and experiment troubleshooting; BixBench (Mitchener et al., 2025) provides a comprehensive benchmark for computational biology with over 50 real-world scenarios and nearly 300 open-ended questions, revealing model accuracies as low as 17% in complex bioinformatics workflows; BioML-bench (Miller et al., 2025) evaluates end-to-end biomedical machine learning workflows from data preprocessing to model evaluation; CellBench (Alber et al., 2025) assesses single-cell RNA sequencing analysis capabilities including clustering and trajectory inference. In chemistry and materials science, ChemToolBench (Tang et al.,

- 2025b) evaluates computational chemistry tasks with 137 external tools for molecular property prediction and reaction forecasting; AFMBench (Mandal et al., 2024) provides 100 expertly curated tasks for atomic force microscopy automation across documentation, analysis, and calculation domains. In Earth sciences, ThinkGeo (Singh et al., 2024) evaluates tool-augmented agents for remote sensing and geospatial analysis. In Machine learning, MLEbench (Chan et al., 2024) is proposed for measuring how well AI agents perform at machine learning engineering, such as training models, preparing datasets, and running experiments. Cross-cutting evaluation includes RAS-Eval (Fu et al., 2025b) for security robustness assessment and Core-bench


(Siegel et al., 2024) for computational reproducibility, addressing the critical challenge of validating published results and fostering research credibility. SciTrust 2.0 (Herron et al., 2025) evaluates trustworthiness of LLMs in scientific applications across dimensions including truthfulness, adversarial robustness, scientific safety, and ethics, incorporating novel benchmarks for assessing scientific exploration capabilities alongside ethical considerations.

#### 3.3 Discussion

The above benchmarks provide a robust framework for evaluating LLM-based scientific agents, addressing a wide range of scientific skills across different stages of research and development. These benchmarks enable comprehensive assessments, from foundational reasoning skills to advanced scientific hypothesis generation and experimental automation, making them critical for guiding the future development of scientific AI systems.

Despite these advances, several limitations remain. First, current benchmarks often rely on static datasets and pre-defined tasks that may not fully capture the dynamic and iterative nature of realworld scientific research. Many evaluations focus on end-to-end performance, thereby obscuring the nuanced failures occurring at individual steps of scientific reasoning and decision-making. Additionally, the diversity of scientific domains—from biomedical research to materials science—presents challenges in standardizing evaluation metrics that can fairly compare agents across different fields.

Future research should focus on developing adaptive and continuously updated benchmarks that mimic authentic scientific workflows. For example, dynamic benchmarks could integrate multi-turn interactions where agents iteratively refine hypothe-

- ses based on experimental feedback, akin to real laboratory processes. Establishing domain-specific evaluation metrics and expanding benchmarks to include cross-disciplinary tasks will be critical for assessing the potential of scientific agents.


### 4 Applications

LLM-based scientific agents have significantly advanced scientific research, automating complex tasks and enhancing the efficiency of discovery processes across various disciplines.

Scientific research is an arduous process involving numerous steps, including hypothesis formula-

tion, experimental design, planning, and data analysis and evaluation. These processes are typically labor-intensive and costly, and thus, they are often conducted by human scientists who possess specialized expertise and substantial capital investment. However, the emergence of scientific agents has revolutionized research efficiency. By automating multiple stages that previously required manual intervention, these computational systems achieve optimal equilibrium in resource utilization. This enhancement in automation not only increases operational efficiency throughout the scientific workflow but also reduces the barriers to entry for conducting rigorous scientific investigations.

Below is a concise exploration of the applications of LLM-based scientific agents, categorized by their specific domains and functionalities, as illustrated in Figures 12, 13 and 14.

4.1 Chemistry and Materials Science 4.1.1 Chemical Synthesis and Reaction

Optimization

LLM-based agents have demonstrated remarkable capabilities in automating chemical synthesis planning, reaction condition optimization, and experimental execution. Coscientist (Boiko et al., 2023) pioneered autonomous chemical experimentation by integrating LLM planning with robotic laboratory equipment, designing and executing synthesis procedures including Suzuki and Sonogashira cross-coupling reactions with minimal human intervention. ChemCrow (Bran et al., 2024) deploys an agent system invoking 18+ specialized cheminformatics tools for synthesis planning, drug design, and materials tasks, demonstrating versatile tool integration for chemical reasoning. Chemist-X (Chen et al.) focuses on reaction condition optimization through a novel RAG scheme interrogating molecular and literature databases to narrow the search space, then employing computer-aided design tools to select promising conditions before validating via wet-lab experiments. AutoLabs (Panapitiya et al., 2025) implements multi-agent systems with self-correction mechanisms for autonomous chemical experimentation, translating natural language instructions into executable protocols for high-throughput liquid handlers. LLM-RDF (Ruan et al., 2024) presents an LLM-based multi-agent system, leveraging GPT-4, to accelerate end-to-end chemical synthesis development, automating tasks from literature search and experimental design to

AutoLabs (Panapitiya et al., 2025), ChemCrow (Bran et al., 2024), Chemist-X (Chen et al.), Chemma (Zhang et al., 2025d), ChemAgents (Song et al., 2025), ChemReasoner (Sprueill et al., 2024), Coscientist (Boiko et al., 2023), LLM-RDF (Ruan et al., 2024), OSDA Agent (Hu et al., 2025b), xChemAgents (Polat et al., 2025), etc

Chemical Synthesis and Reaction Optimization

CACTUS (McNaughton et al., 2024), CheMatAgent (Wu et al., 2025), ChemDFM (Zhao et al., 2025), ChemGraph (Pham et al., 2025), ChemOrch (Huang et al., 2025c), dZiner (Ansari et al., 2024), El Agente (Zou et al., 2025), IR-Agent (Noh et al., 2025), MolRL-MGPT (Hu et al., 2024b), etc

Molecular Design and Optimization

Chemistry and Materials Science

AccelMat (Kumbhar et al., 2025), AILA (Mandal et al., 2024), AtomAgents (Ghafarollahi and Buehler, 2024a), ChatMOF (Kang and Kim, 2024), HoneyComb (Zhang et al., 2024a), LLMatDesign (Jia et al., 2024), MatChat (Chen et al., 2023), MatPilot (Ni et al., 2024), MatterChat (Tang et al., 2025e), MAPPS (Zhou et al., 2025),

Materials Discovery and Characterization

PriM (Lai and Pu, 2025), etc

Applications (Part I)

AI co-scientist (Gottweis et al., 2025), BioScientist Agent (Zhang et al., 2025a), DrugAgent (Inoue et al., 2024), DrugPilot (Li et al., 2025a), DrugAssist (Ye et al., 2023a), GatorTronGPT (Peng et al., 2023), MedAgents (Tang et al., 2023), OriGene (Zhang et al., 2025e), Robin (Ghareeb et al., 2025), STELLA (Jin et al., 2025), etc

Drug Discovery and Target Identification

AtlasAgent (Yin et al., 2025), BIA (Xin et al., 2024), BioAgents (Mehandru et al., 2025), BioDiscoveryAgent (Roohani et al., 2024), BioMaster (Su et al., 2025), BiomedRAG (Li et al., 2024c), Biomni (Huang et al., 2025a), CellAgent (Xiao et al., 2024), CellVoyager (Alber et al., 2025), GeneGPT (Jin et al., 2024), K-Dense Analyst (Li et al., 2025b), TAIS (Liu et al., 2024a), TransAgent (Zhang et al., 2025b), etc

Life and Biomedical Sciences

Genomics and Bioinformatics Workflows

ADAM (Xia et al., 2025a), CellForge (Tang et al., 2025d), CRISPR-GPT (Huang et al., 2024a), ProtAgents (Ghafarollahi and Buehler, 2024b), Sparks (Ghafarollahi and Buehler, 2025), etc

Protein Engineering and CRISPR Applications

- Figure 12: Applications of representative LLM-based scientific agents (Part I): Chemistry & Materials Science; Life & Biomedical Sciences.


reaction optimization and product purification, thus streamlining traditional workflows. ChemAgents

(Song et al., 2025) builds multi-agent systems capable of executing complex, multi-step chemical ex-

periments by coordinating specialized agents (Literature Reader, Experiment Designer, Computation Performer, Robot Operator) underpinned by comprehensive literature databases and protocol libraries. xChemAgents (Polat et al., 2025) uses a Selector to adaptively identify relevant textual chemical descriptors and a Validator to enforce physical constraints, leading to improved predictive accuracy and human-interpretable explanations for quantum chemistry properties. ChemReasoner (Sprueill et al., 2024) employs process-supervised reasoning for catalytic search, combining LLMderived hypotheses with GNN-derived feedback in heuristic search processes to identify optimal catalysts. Chemma (Zhang et al., 2025d) fine-tuned large language model (LLM) based on LLaMA2-7b, and is designed to accelerate organic chemistry synthesis by excelling in tasks like retrosynthesis, yield prediction, condition generation, and autonomous reaction exploration in both closed and open reaction space. OSDA Agent (Hu et al.,

- 2025b) specializes in organic structure-directing agent discovery for zeolite synthesis. These systems collectively demonstrate that LLM agents can orchestrate end-to-end chemical workflows from literature review and synthesis planning through experimental execution and results analysis, significantly accelerating chemical discovery cycles while maintaining safety and reproducibility standards.


#### 4.1.2 Molecular Design and Optimization

Beyond synthesis planning, LLM agents excel at molecular design tasks including inverse design, property prediction, and structure optimization. dZiner (Ansari et al., 2024) discovers new compounds with desired properties via inverse design, iteratively reviewing modified materials and modification history while leveraging domain-specific design guidelines retrieved from scientific literature to enable efficient chemical space exploration. ChemDFM (Zhao et al., 2025) presents a large language foundation model for chemistry developed through domain-specific pre-training on 34B tokens from chemical literature, enabling free-form chemical dialogue, reaction prediction, and reasoning about novel chemical scenarios. MolRLMGPT (Hu et al., 2024b) combines supervised learning with reinforcement learning in an RLdriven multi-agent framework for de novo molecular generation and optimization, employing experience replay to guide molecular design toward

drug-like chemical space. IR-Agent (Noh et al., 2025) develops a multi-agent framework for molecular structure elucidation from IR spectra, coordinating specialized agents (TI Expert, Ret Expert, Str Expert) to interpret spectroscopic data. CheMatAgent (Wu et al., 2025) enhances chemical and materials agents through tree-search based tool learning, decoupling tool selection (Policy Model) from tool execution (Execution Model) with selftraining on decision trajectories. El Agente (Zou et al., 2025) streamlines quantum chemistry workflows including geometry optimizations and property predictions through a hierarchical multi-agent system with specialized procedural, semantic, and episodic memory components. ChemOrch (Huang et al., 2025c) provides an instruction-enhanced agent for chemical QA and reasoning with multistage self-repair mechanisms and sufficiency validation. These molecular design agents demonstrate sophisticated optimization capabilities, balancing multiple objectives (activity, synthesizability, toxicity) while navigating vast chemical spaces guided by learned chemical principles and computational predictions.

4.1.3 Materials Discovery and Characterization

LLM agents are increasingly applied to materials science for hypothesis generation, property prediction, and experimental validation. MAPPS (Zhou et al., 2025) achieves flexible and reliable materials discovery by unifying planning, physicsbased simulations, and human scientist feedback in closed-loop workflows, with agents generating hypotheses, the physics toolbox computing properties, and scientists providing oversight before experimental synthesis. AtomAgents (Ghafarollahi and Buehler, 2024a) presents a physics-aware multi-agent platform for alloy discovery combining multi-modal data integration (text, numerical data, simulation images) with physics-based LAMMPS simulations, demonstrating successful hypothesis generation, validation, and materials characterization. LLMatDesign (Jia et al., 2024) implements iterative material design for specific target properties through self-reflection on previous design decisions, enabling rapid zero-shot adaptation to new materials challenges. AILA (Mandal et al., 2024) presents a framework driven by LLM agents, automating atomic force microscopy (AFM) experiments across the full scientific workflow. MatPilot (Ni et al., 2024) integrates multi-agents to generate

materials hypotheses and drive an automated experimental platform, closing the loop between computational predictions and physical synthesis. PriM (Lai and Pu, 2025) combines automated material hypothesis generation with experimental validation through integrated workflows. HoneyComb (Zhang

- et al., 2024a) creates a materials agent system integrating MatSciKB (materials science knowledge base) with ToolHub (computational tools suite), enabling intelligent tool assessment and execution for materials science question-answering tasks. Multicrossmodal (Bazgir et al., 2025) addresses the challenge of integrating and cross-correlating multiple material data modalities through agent-based coordination. SciAgents (Ghafarollahi and Buehler,


- 2024c) reasons over large-scale ontological knowledge graphs for materials science, enabling hypothesis generation grounded in structured domain knowledge. ChatMOF (Kang and Kim, 2024) leverages large language models (GPT-4, GPT-3.5-turbo,


- GPT-3.5-turbo-16k) to successfully predicts and generates metal-organic frameworks (MOFs) by extracting key details from textual inputs and delivering appropriate responses, eliminating the need for rigid structured queries. Those works collectively showcase the breadth of materials science applications enabled by LLM agents.


- 4.2 Life and Biomedical Sciences


- 4.2.1 Drug Discovery and Biomedical Research


LLM agents have transformed drug discovery workflows by automating target identification, drugtarget interaction prediction, and therapeutic candidate validation. DrugAgent (Inoue et al., 2024) implements a multi-agent system integrating ML predictions, biomedical knowledge graphs (DrugBank, CTD, STITCH), and literature search to predict drug-target interactions, with specialized agents (AI Agent, KG Agent, Search Agent, Reasoning Agent) collaboratively evaluating candidates. Robin (Ghareeb et al., 2025), a multi-agent AI system that automates the entire scientific discovery process, from hypothesis generation to experimental data analysis, demonstrate its capability by discovering ripasudil as a novel therapeutic candidate for dry age-related macular degeneration (dAMD) and elucidating its mechanism of action. BioScientist Agent (Zhang et al., 2025a) employs KG-augmented RL reasoning modules for drug repurposing, unifying a billion-fact biomedi-

cal knowledge graph (RTX-KG2) with adversarial actor-critic algorithms to traverse paths and identify repurposing opportunities. OriGene (Zhang et al., 2025e) develops a self-evolving multi-agent system, functions as a virtual disease biologist, systematically identifying original and mechanistically grounded therapeutic targets at scale, successfully nominated and experimentally validated previously under-explored therapeutic targets, GPR160 for liver cancer and ARG2 for colorectal cancer. DrugPilot (Li et al., 2025a) introduces a parameterized reasoning architecture for end-to-end drug discovery workflows, employing a feedback-focus mechanism to correct reasoning errors and maintain task focus. DrugAssist (Ye et al., 2023a) provides a dialogue agent for molecule optimization through interactive human-AI collaboration. AI co-scientist (Gottweis et al., 2025) generates novel research hypotheses and proposals via a multi-agent mechanism, validated in three biomedical areas: drug repurposing, novel target discovery, and bacterial evolution/anti-microbial resistance. STELLA (Jin et al., 2025) is a self-evolving AI agent for biomedical research that autonomously improves its capabilities through an evolving Template Library and a dynamic Tool Ocean, achieving state-of-the-art accuracy on biomedical benchmarks and systematically improving its performance with experience. MedAgents (Tang et al., 2023) assigns multi-agent clinician roles for medical reasoning, simulating clinical consultations across specialized perspectives. GatorTronGPT (Peng et al., 2023) specializes in medical domain knowledge Q&A and relation extraction through domain-specific pre-training on clinical texts, with its utility in generating highquality synthetic clinical text for training NLP models, and its ability to produce clinical content indistinguishable from human-written notes by physicians. These systems collectively demonstrate that LLM agents can navigate the complex, multi-stage drug discovery pipeline from target identification through candidate optimization to validation, significantly accelerating timelines while incorporating domain knowledge, literature evidence, and expert oversight.

4.2.2 Genomics and Bioinformatics Workflows

Genomic data analysis and bioinformatics represent a major application area where LLM agents automate complex computational workflows. BioMaster (Su et al., 2025) provides multi-agents

that automate and streamline complex bioinformatics workflows from planning through execution with RAG-enhanced domain knowledge retrieval and debug agents handling iterative error correction. CellAgent (Xiao et al., 2024) focuses on automatic processing and execution of single-cell RNA-seq data analysis tasks, employing dual-layer memory (global and local) and self-iterative optimization to ensure high-quality results. Biomni (Huang et al.,

- 2025a) offers a generalist agentic architecture integrating LLM reasoning with retrieval-augmented planning and code-based execution to carry out complex biomedical workflows without predefined templates, pre-installed with 150+ specialized tools, 105 software packages, and 59 databases. BIA (Xin et al., 2024) enables information processing and analysis from scRNA-seq data through autonomous workflow design and code generation. K-Dense Analyst (Li et al., 2025b) achieves autonomous bioinformatics analysis through a multiagent system with specialized code and shell example access in secure sandboxed environments. CellVoyager (Alber et al., 2025) autonomously explores scRNA-seq datasets in novel directions conditioned on prior user-run analyses, generating and testing new hypotheses through iterative code execution in Jupyter environments. BioAgents (Mehandru et al., 2025) generates end-toend bioinformatics workflows with multi-agents fine-tuned on tool documentation and enhanced with RAG. TransAgent (Zhang et al., 2025b) automates transcriptional regulation analysis from raw data to insights, successfully reconstructing super-enhancer regulatory circuits in esophageal squamous cell carcinoma and identified key regulators in cardiomyocyte. TAIS (Liu et al., 2024a) identifies disease-predictive genes through multiagent coordination. AtlasAgent (Yin et al., 2025) provides VLM-guided framework for evaluating atlas-scale single-cell integration. BiomedRAG (Li et al., 2024c) implements biomedical RAG for QA and synthesis tasks with tailored chunk scoring. GeneGPT (Jin et al., 2024) augments large language models with NCBI Web APIs through incontext learning and an augmented decoding algorithm to achieve state-of-the-art performance on genomics question-answering tasks. These genomics agents demonstrate sophisticated capabilities in automating data-intensive analytical pipelines, from quality control and normalization through clustering, differential expression analysis, and biological interpretation.


#### 4.2.3 Protein Engineering and CRISPRApplications

LLM agents are increasingly applied to protein design, gene editing, and molecular biology experimentation. Sparks (Ghafarollahi and Buehler, 2025) represents a breakthrough in multi-agent AI discovering protein design principles end-to-end, autonomously identifying design rules through iterative computational and experimental validation cycles. ProtAgents (Ghafarollahi and Buehler, 2024b) provides multi-agent systems for successfully performing de novo protein design, analysis, and data acquisition by dynamically combining physics and machine learning method. CRISPR-GPT (Huang

- et al., 2024a) assists CRISPR experiments by facilitating CRISPR system selection, guide RNA design, cellular delivery method recommendation, protocol drafting, and validation experiment design through integration of expert knowledge and computational toolkits. ADAM (Xia et al., 2025a) offers a multi-agent framework for computational biophysics including molecular docking, molecular dynamics simulations, and electronic structure analysis. CellForge (Tang et al., 2025d) transforms datasets and research goals into computational models for virtual cells through collaborative role-specialized agents engaging in graphstructured debates to converge on optimized architectures. These protein and gene editing agents showcase the potential for AI-driven molecular biology, from rational protein design guided by physical principles to practical CRISPR experiment planning grounded in literature and expert knowledge, enabling researchers to accelerate discovery while maintaining experimental rigor and biological plausibility.

4.3 Physics and Engineering 4.3.1 Computational Fluid Dynamics and

Mechanics

LLM agents are transforming physics simulation workflows, particularly in fluid dynamics and mechanical engineering. OpenFOAMGPT (Pandey

- et al., 2025) and OpenFOAMGPT 2.0 (Feng et al., 2025a) provide OpenFOAM-centric computational fluid dynamics (CFD) simulation automation, translating natural language engineering requirements into complete simulation configurations including mesh generation, boundary conditions, solver parameters, and post-processing scripts through RAG over embedded OpenFOAM documentation. Foam-


Agent (Yue et al., 2025) employs multi-agent automation of OpenFOAM CFD workflows with hierarchical multi-index retrieval systems segmenting domain knowledge into specialized FAISS indices for different simulation aspects, coupled with iterative refinement processes and reviewer agents maintaining review trajectory analysis. MechAgents (Ni and Buehler, 2024) addresses mechanics problems by leveraging diverse capabilities and dynamic interactions among agents, with a two-agent team setup with self-correction mechanisms and a multi-agent group setup with division of labor and mutual correction via dynamic group chatting. MoRA (Jaiswal et al., 2024) presents an agentic refinement framework for physical reasoning that iteratively improves physics problem-solving through feedback loops. SciMARL (Bae and Koumoutsakos, 2022) employs scientific multi-agent reinforcement learning for autonomous exploration in fluid dynamics, discovering improved wall models through RL-based parameter exploration. These systems demonstrate that LLM agents can significantly reduce the expertise barrier for sophisticated physics simulations, enabling non-expert users to

- set up, execute, and interpret complex CFD and mechanics calculations while automating tedious configuration tasks that traditionally require deep domain knowledge and extensive manual effort.


- 4.3.2 Electromagnetic Fields and Quantum Systems


LLM agents are being applied to specialized physics domains including electromagnetic field manipulation and quantum computing. MetaAgent (Hu et al., 2025a) provides multi-agent systems for electromagnetic (EM) field manipulations, employing multi-agent discussion mechanisms in its cerebrum component to coordinate specialized agents for EM wave control, and metamaterial optimization. k-agents (Cao et al., 2024) provides a knowledge-based multi-agent system to organize laboratory knowledge and automate complex experiments, successfully demonstrating autonomous calibration and operation of a superconducting quantum processor at a human-level performance. SGA (Ma et al., 2024a) implements bilevel optimization pairing LLM-generated ideas with physics simulators across domains spanning physics, chemistry, and pharmacology, discovering novel constitutive laws and molecular designs through iterative LLM ideation guided by simulation feedback. These specialized physics appli-

cations showcase the potential for LLM agents to tackle cutting-edge experimental physics challenges, from quantum state engineering requiring precise hardware control to electromagnetic design optimization demanding sophisticated multiphysics reasoning, demonstrating that agents can bridge the gap between high-level scientific goals and low-level experimental implementation in advanced physics research.

4.4 Astronomy and Astrophysics

- 4.4.1 Astronomical Observation and Telescope Control

LLM agents are automating astronomical observation workflows from planning through execution and data analysis. StarWhisper (Wang et al., 2025a) implements telescope control workflows based on LLM agents, interpreting natural language observation requests from astronomers, generating specific telescope control sequences (pointing coordinates, exposure times, filter selections), presenting planned observations for verification, and executing approved observation programs. LLMSat (Maranto, 2024) presents an agentic spacecraft controller using LLM as a reasoning engine for autonomous space exploration, and is evaluated using a series of deep space mission scenarios simulated within the Kerbal Space Program (KSP) game engine. Mephisto (Sun et al., 2024b) employs a selfimproving LLM-based agent framework that emulates human-like reasoning to interpret multi-band galaxy observations through iterative SED modeling, demonstrating transparent and efficient analysis across diverse galaxy populations, including novel "Little Red Dot" galaxies. These observationfocused systems demonstrate that LLM agents can serve as intelligent interfaces between astronomers’ high-level scientific objectives and complex telescope control systems, reducing cognitive load on observers while ensuring that observation strategies align with scientific goals, handling unexpected situations through adaptive reasoning, and maintaining safety constraints critical for protecting expensive astronomical instrumentation.

- 4.4.2 Cosmological Data Analysis and Modeling


LLM agents are increasingly applied to cosmological and astronomical data analysis workflows requiring sophisticated statistical reasoning and computational modeling. AI Cosmologist (Moss, 2025) automates cosmological and astronomical

Foam-Agent (Yue et al., 2025), MechAgents (Ni and Buehler, 2024), MoRA (Jaiswal et al., 2024), OpenFOAMGPT (Pandey et al., 2025), OpenFOAMGPT 2.0 (Feng et al., 2025a), SciMARL (Bae and Koumoutsakos, 2022), etc Electromagnetic Fields and Quantum Systems

Computational Fluid Dynamics and Mechanics

Physics and Engineering

metaAgent (Hu et al., 2025a), k-agents (Cao et al., 2024),

SGA (Ma et al., 2024a), etc

Astronomical Observation and Telescope Control

LLMSat (Maranto, 2024), mephisto (Sun et al., 2024b), StarWhisper (Wang et al., 2025a), etc

Applications (Part II)

Astronomy and Astrophysics

AI Cosmologist (Moss, 2025), ASA (Liu et al., 2024b), AstroMLab (de Haan et al., 2025),

Cosmological Data Analysis and Modeling

CosmoAgent (Xue et al., 2024), etc

ClimateGPT (Thulke et al., 2024), Earth-Agent (Feng et al., 2025b), GeoAgent (Chen et al., 2024a), GeoMap-Agent (Huang et al., 2025b), GeoMinLM (Fu et al., 2025a), GeoSim.AI (Bekele, 2025), LLM-Find (Ning et al., 2025), MineAgent (Yu et al., 2024), PANGAEA GPT (Pantiukhin et al., 2025), etc

Geospatial Analysis and Geological / Climate Modeling

Earth Environmental and Climate Sciences

- Figure 13: Applications of representative LLM-based scientific agents (Part II): Physics & Engineering; Astronomy & Astrophysics; Earth, Environmental & Climate Sciences.


data analysis and machine learning research workflows through specialized multi-agent systems, enabling autonomous exploration of cosmological datasets like Galaxy Zoo 2 and Quijote simulations. AstroMLab (de Haan et al., 2025) provides domain-specific training for astronomy Q&A through AstroSage-Llama-3.1-70B, a model undergoing extensive continued pretraining ( 168,000

- GPU-hours) on astronomical literature with supervised fine-tuning incorporating explicit reasoning chains, enabling either immediate answers or stepby-step thought processes for astronomical queries. CosmoAgent (Xue et al., 2024) takes a unique approach by simulating interactions between human and extraterrestrial civilizations, employing mathematical models and state transition matrices to analyze growth trajectories and explore dynamics under diverse worldviews and information asymmetry. ASA (Liu et al., 2024b) provides end-to-end simulation workflow agents for physics research including celestial mechanics, autonomously designing simulations, remotely uploading and executing them, collecting data, and compiling research reports. These cosmological analysis agents showcase the potential for automating complex dataintensive astronomical research, from hypothesis formulation through computational analysis to sci-


entific interpretation, enabling astronomers to explore larger datasets and test more hypotheses than feasible through manual analysis alone.

4.5 Earth, Environmental, and Climate Sciences

4.5.1 Geospatial Analysis, and Geological/Climate Modeling

LLM agents are being deployed for geospatial data processing, geological map interpretation, mineral exploration and climate data analysis. GeoAgent (Chen et al., 2024a) pioneers integration of code interpreter, static analysis, and RAG within Monte Carlo Tree Search for geospatial data processing, iteratively refining code generation for spatial analysis tasks with comprehensive error traceback mechanisms. GeoMap-Agent (Huang et al., 2025b) provides domain knowledge injection for geological map interpretation and question answering, consulting specialized expert agents (geologist, geographer, seismologist) who leverage tools from an extensible tool pool and access scientific databases alongside the K2 scientific model for geology-specific knowledge. MineAgent (Yu et al., 2024) focuses on remote-sensing mineral exploration that leverages hierarchical judging and decision-making modules to enhance multi-

modal large language models’ reasoning capabilities across multiple images and spatial-spectral integration. LLM-Find (Ning et al., 2025) implements autonomous geospatial data retrieval managing pre-defined scalable lists of data sources like OpenStreetMap and US Census data, with selfdebug modules correcting buggy code according to error information. GeoMinLM (Fu et al., 2025a) provides a specialized LLM for geological and mineral exploration in Yunnan Province, successfully developed by leveraging a proprietary dataset and integrating expert knowledge via a knowledge graph. GeoSim.AI (Bekele, 2025) employs RAGbased approaches with comprehensive geomechanics knowledge bases and data/tools bases to guide LLM translation of natural language into technical simulation inputs for geomechanical modeling, orchestrating simulation workflows while ensuring physical plausibility of parameters and configurations. PANGAEA GPT (Pantiukhin et al., 2025) accelerates geological research through multi-agent LLM-based agents, with transformative potential for improving scientists’ interaction with geoscientific data through intelligent data processing, natural language interfaces, and collaborative problemsolving in earth and environmental science. EarthAgent (Feng et al., 2025b) is the first agentic framework for Earth Observation (EO) that unifies RGB and spectral data, enabling cross-modal, multi-step, and quantitative spatiotemporal reasoning through a comprehensive tool ecosystem. ClimateGPT (Thulke et al., 2024) presents a climate domain LLM enhanced with RAG for climate science applications, enabling question answering and information retrieval from climate literature and datasets. These geospatial and environmental agents demonstrate capabilities in automating traditionally manual geological interpretation tasks, from map reading and spatial analysis to mineral resource assessment, making sophisticated geoscience analyses more accessible to non-experts while accelerating routine data processing for domain experts.

- 4.6 Machine Learning and Data Science


- 4.6.1 Automated Machine Learning Research


LLM agents are being deployed to automate ML research itself, conducting experiments, analyzing results, and generating scientific insights. AI Scientist (Lu et al., 2024a) and AI Scientist-v2 (Yamada

- et al., 2025) enable autonomous scientific exploration in computer science, generating novel re-


search ideas, implementing experiments, executing computational studies, analyzing results, writing full scientific papers, and conducting simulated peer review, with AI Scientist-v2 enhancing this through agentic tree search and VLM feedback for figure refinement, achieving acceptance of a fully AI-generated manuscript at an ICLR workshop. Agent Laboratory (Schmidgall et al., 2025) assists ML research via multi-agent autonomous scientific exploration through the entire research process, from literature review and experimentation to report writing, while enabling user feedback and achieving significant cost reductions and good performance in ML code generation. Similarly, MLR-Copilot (Li et al., 2024d) also leverages LLM agents to automate the entire machine learning research process, from generating new ideas and hypotheses to implementing and executing experiments with iterative refinement based on human and automated feedback. AIGS (Liu et al.,

- 2024c) provides a multi-agent system designed for full-process automated scientific discovery, emphasizing falsification through a dedicated FALSIFICATIONAGENT alongside DSL and multisampling strategies to enhance executability and creativity. CycleResearcher (Weng et al., 2025) improves automated research through iterative preference training, with CycleResearcher conducting research tasks and CycleReviewer simulating peer review providing feedback via reinforcement learning. These ML research agents demonstrate potential for AI systems to conduct autonomous research, from ideation through execution to publication, though current capabilities remain limited to well-defined computational domains with clear evaluation metrics.

4.6.2 Algorithm Discovery and Optimization

LLM agents excel at discovering and optimizing algorithms through evolutionary and searchbased approaches. AlphaEvolve (Novikov et al.,

- 2025) evolves code to discover and optimize algorithms across diverse domains including data center scheduling, matrix multiplication kernel optimization, hardware circuit design, and compilergenerated code improvement, using evolutionary approaches where LLMs propose code modifications evaluated through execution feedback, achieving provably correct novel algorithms and mathematical constructions. SciAgent (Ma et al., 2024b) provides tool-augmented scientific reasoning for general scientific tasks spanning mathe-


AI Scientist (Lu et al., 2024a), AI Scientist-v2 (Yamada et al., 2025), AIGS (Liu et al., 2024c), Agent Laboratory (Schmidgall et al., 2025), CycleResearcher (Weng et al., 2025), MLR-Copilot (Li et al., 2024d), etc

Automated Machine Learning Research

AlphaEvolve (Novikov et al., 2025), HyperGen (O’Neill et al., 2025), SciAgent (Ma et al., 2024b), VirSci (Su et al., 2024), etc

Machine Learning Math and Data Science

Algorithm Discovery and Optimization

CoT-Influx (Huang et al., 2024d), Flow-DPO (Deng and Mineiro, 2024), ReFT (Luong et al., 2024), STEP-DPO (Lai et al., 2024), ToRA (Gou et al., 2024), etc

Mathematical Reasoning and Formal Methods

Applications (Part III)

AI-Researcher (Tang et al., 2025a), CoI (Li et al., 2024b), InternAgent (Team et al., 2025a), PaSa (He et al., 2025), PiFlow (Pu et al., 2025), ResearchAgent (Baek et al., 2024), SciMON (Wang et al., 2024b), etc

Literature Analysis and Research Idea Generation

Scientific Literature Review and Meta-Research

AmadeusGPT (Ye et al., 2023b), FoodPuzzle (Huang et al., 2024c), MyCrunchGPT (Kumar et al., 2023), OLAF (Riffle et al., 2025), ORGANA (Darvish et al., 2025), etc

Specialized Domain Applications and Platforms

- Figure 14: Applications of representative LLM-based scientific agents (Part III): Machine Learning & Data Science; Scientific Literature Review & Meta-Research.


matics, physics, chemistry, and electrical engineering, integrating specialized tools to enhance LLM reasoning capabilities. HyperGen (O’Neill et al.,

- 2025) focuses on scientific hypothesis generation in computer science. VirSci (Su et al., 2024) implements multi-agent systems for scientific idea generation and refinement through iterative critique cycles. These algorithm-focused agents showcase LLM capabilities in computational creativity, proposing novel algorithmic approaches, optimizing implementations for efficiency, and discovering non-obvious solutions through systematic exploration of design spaces guided by automated evaluation feedback.


- 4.6.3 Mathematical Reasoning and Formal Methods


LLM agents are advancing mathematical reasoning through specialized architectures and training methods. ToRA (Gou et al., 2024) provides tool-integrated reasoning to solve complex mathematical problems, applying imitation learning on TORA-CORPUS and proposed output space shaping to refine reasoning behavior. ReFT (Luong

- et al., 2024) employs supervised learning and rein-


forcement learning for mathematical reasoning optimization by learning from automatically sampled reasoning paths and ground-truth answers. STEPDPO (Lai et al., 2024) introduces step-wise preference optimization for LLMs’ long-chain mathematical reasoning, improving multi-step problemsolving capabilities. CoT-Influx (Huang et al., 2024d) enhances mathematical reasoning by employing a reinforced coarse-to-fine context pruning strategy to maximize effective Chain-of-Thoughts (CoT) examples within the context window. FlowDPO (Deng and Mineiro, 2024) uses an online multi-agent learning Flow and Direct Preference Optimization with rollouts to generate high-quality reasoning traces, significantly improving LLM mathematical reasoning capabilities. These mathematical reasoning agents demonstrate progress toward reliable formal reasoning in LLMs, though challenges remain in ensuring correctness guarantees and handling complex multi-step proofs, with tool integration and verification mechanisms partially addressing these limitations by grounding reasoning in symbolic computation rather than pure neural generation.

- 4.7 Scientific Literature Review and Meta-Research


- 4.7.1 Literature Analysis and Research Idea Generation


LLM agents are revolutionizing how research is conducted from literature review to idea generation. PaSa (He et al., 2025) provides a comprehensive academic paper search system optimized through reinforcement learning to autonomously make a series of decisions, including invoking search tools, reading papers, and selecting relevant references, to ultimately obtain comprehensive and accurate results for complex scholar queries. Similarly, SciMON (Wang et al., 2024b) implements literaturegrounded novelty-optimizing idea generation, via an automated data collection methodology for past problems. CoI (Li et al., 2024b) implements automated generation of novel scientific research ideas through Chain-of-Ideas reasoning, iteratively refining broad concepts into specific testable hypotheses with novelty-checker agents evaluating against existing literature. ResearchAgent (Baek et al.,

- 2024) provides a multi-agent research pipeline that generates and refines novel scientific research ideas by integrating knowledge from academic graphs and entity-centric stores, and by iteratively incorporating feedback from LLM-based reviewing agents. InternAgent (Team et al., 2025a) delivers closed-loop multi-agents from hypothesis generation through experimental planning to verification, coordinating Survey Agents for literature review, Idea Innovation Agents for creative hypothesis generation, and Orchestration Agents for workflow management. AI-Researcher (Tang et al.,
- 2025a) successfully orchestrates the entire research pipeline from literature review to manuscript preparation with minimal human intervention, achieving remarkable implementation success rates and producing near human-quality papers. PiFlow (Pu


- et al., 2025) provides an information-theoretical framework that treats automated scientific discovery as a structured uncertainty reduction problem guided by scientific principles using multiagent collaboration and Min-Max optimization. These literature-focused and idea generation agents demonstrate AI’s potential to augment human creativity in scientific discovery, proposing novel hypotheses by identifying gaps in literature, combining concepts from disparate domains, and generating testable predictions, though human oversight remains critical for assessing novelty and value.


4.7.2 Specialized Domain Applications and Platforms

Beyond traditional domains, LLM agents are being applied to niche scientific areas and comprehensive platforms. FoodPuzzle (Huang et al., 2024c) explores autonomous flavor hypothesis generation and exploration in food science, combining incontext learning with RAG from scholarly articles, internet blogs, and FlavorDB to propose novel flavor combinations grounded in chemical principles and culinary precedents. AmadeusGPT (Ye et al., 2023b) provides a natural language interface for animal behavior analysis in neuroscience, translating behavioral pattern descriptions into executable analysis code using pose estimation libraries, enabling biologists to perform computational analysis without programming expertise through conversational interaction with dual-memory mechanisms bridging short-term chat history and long-term symbolbased retrieval. MyCrunchGPT (Kumar et al., 2023) provides a ChatGPT-assisted framework that integrates various stages of Scientific Machine Learning (SciML) to streamline scientific computing tasks, demonstrating its utility through 2D NACA airfoil design and optimization, and PINNbased fluid mechanics simulations. OLAF (Riffle et al., 2025) is an open-source software platform leveraging large language models to enable conversational bioinformatics, allowing life scientists to perform complex data analyses and lab automation tasks through natural language queries and automated code execution. ORGANA (Darvish et al., 2025) is an AI-driven robotic assistant that automates diverse chemistry experiments, allowing chemists to interact using natural language for planning and real-time updates, significantly reducing experimental time and physical effort through automated decision-making, perception tools, and parallel task execution. These specialized applications demonstrate the broad applicability of LLM agent architectures, adapting general agent frameworks to domain-specific challenges through appropriate tool integration, knowledge base curation, and workflow design, suggesting that the agent paradigm can be productively applied to virtually any scientific domain with sufficient computational infrastructure and domain knowledge encoding.

#### 4.8 Discussion

The above provides a wide range of applications for scientific agents powered by LLMs, demon-

strating their potential to transform research in fields such as biomedical analysis, materials science, etc. These applications showcase how LLMbased agents can enhance data interpretation, support complex decision-making, and generate novel hypotheses, thus accelerating scientific discovery.

Despite this, current applications face significant limitations. Many applications are domain-specific and lack the flexibility needed to generalize across diverse scientific disciplines. In several cases, the integration of scientific knowledge with agent reasoning is hampered by static models that do not adapt to real-time data or evolving research challenges. Moreover, there is often insufficient validation of the agents’ outputs against established scientific benchmarks, leading to concerns about reproducibility and reliability.

Looking ahead, future studies or products should focus on developing more generalized frameworks for scientific applications that integrate heterogeneous data sources and facilitate cross-disciplinary collaboration. Enhancements in real-time error detection, adaptive feedback mechanisms, and multimodal LLM architectures will be essential for improving the robustness of these systems. Collaborative efforts between domain experts and AI researchers are crucial to fine-tune the decisionmaking processes of scientific agents, ensuring that their outputs align closely with established scientific principles and practices.

### 5 Ethics

While LLM-based scientific agents excel technically and drive research innovation, they also raise profound ethical challenges. Bengio et al. (2025) warn that unchecked AI agency could endanger public safety and scientific integrity, arguing for a non-agentic “Scientist AI” design that prioritizes explanation and transparency over independent action. This concern is echoed in recent analyses of emerging “AI scientist” paradigms, where Tang et al. (2025c) argue that autonomy itself introduces systemic risks and that safeguarding must take priority over capability expansion. Complementary analyses by Pournaras (2023) and others examine epistemological and integrity risks in AImediated research, while high-level governance guidance from the International Science Council (Norori et al., 2025) calls for principled oversight, provenance-rich workflows, and transparent documentation throughout AI-supported scientific prac-

tice. Studies such as (Bano et al., 2023; Lin, 2024; Watkins, 2024; Limongi, 2024; Zhu et al., 2025; Sun et al., 2025; Fu et al., 2025b; Zhang et al., 2025c; Hartung, 2025; Resnik and Hosseini, 2025; Herron et al., 2025) highlight enduring issues of agency, transparency, bias, accountability, and ownership. Building on these foundations, this section synthesizes recent advances to outline how scientific agents can remain trustworthy, transparent, and aligned with human values.

#### 5.1 Agency and Autonomy

Scientific AI agents must function strictly as tools under human supervision, not autonomous actors. Without explicit constraints, agents may develop unintended goal persistence or deceptive behaviors that compromise research integrity (Pournaras, 2023; Lin, 2024). Hybrid frameworks that blend top-down ethical rules with continuous human feedback (Tennant et al., 2025) are emerging to maintain such control. Recent architectures, notably SafeScientist (Zhu et al., 2025), implement rulebased refusal policies and an embedded ethicalreviewer agent that monitors experimental planning. Its associated SciSafetyBench benchmark quantifies whether agents can detect and decline unsafe or unethical tasks, turning safety into an evaluated capability rather than an abstract goal. Echoing these efforts, Bengio et al. (2025) propose bounded, non-agentic “Scientist AI” systems as safer alternatives to open-ended, goal-seeking agents. Across these approaches, the consensus is clear: autonomy in science must be bounded in scope, tools, and time so that agents remain assistive collaborators governed by human oversight.

#### 5.2 Transparency and Explainability

Transparency is fundamental to scientific credibility. Watkins (2024) emphasize that reproducibility and accountability in LLM-based research require standardized documentation of every computational step. Structured internal logs and explanation frameworks (Bano et al., 2023; Banerjee et al., 2024) can expose the reasoning behind agent decisions and enable peer auditing. The ScienceBoard benchmark (Sun et al., 2025) demonstrates this principle by recording all agent interactions—queries, tool calls, code executions—allowing experiments to be replayed and verified. Such traceable workflows convert explanation from a narrative justification into empirical transparency. Consequently, effective explainabil-

ity in scientific agents extends beyond verbal rationales to include full operational traces: retrieval logs, execution scripts, and intermediate results, ensuring that conclusions are inspectable and reproducible under established scientific norms.

#### 5.3 Hallucinations and Reliability

LLMs can generate plausible but incorrect statements that, when embedded in scientific workflows, produce misleading conclusions. These hallucinations arise from insufficient data quality, ambiguous prompts, or over-generalization. Ge et al. (2025) show how manipulated prompts can elicit fabricated arguments that distort scientific reasoning, threatening credibility and public trust. To counter this, reliability must be embedded directly in architecture. Agents increasingly employ verifiers that cross-check claims against databases or simulation outputs before release. Processsupervision planners and iterative feedback loops strengthen factual consistency, while memory modules that store validated evidence reduce drift over long reasoning chains. Together, these mechanisms transform reliability from a passive metric into a self-regulating process.

#### 5.4 Vulnerability and Security

The openness of LLM-based agents introduces new attack surfaces. Adversarial prompt injections or model-extraction attempts can corrupt results or disseminate false scientific knowledge. Yang et al. (2024a) demonstrate that biomedical knowledge graphs can be intentionally poisoned to alter drug–disease relations, illustrating concrete research-level risks. Security benchmarks such as RAS-Eval (Fu et al., 2025b) have begun to expose these vulnerabilities in realistic tool-augmented environments. Similarly, SafeScientist (Zhu et al.,

- 2025) reports threats including memory poisoning, tool-response injection, and malicious collaborator agents. Chen and Madisetti (2024) adds that multi-agent communication itself can leak sensitive data or enable collusion, and it advocates encrypted audit trails and strict access controls to preserve research integrity. Countermeasures therefore combine capability firewalls that restrict unverified tool access, context sanitization of retrieved data, and cryptographic audit logs to trace every experiment or code execution. By embedding such protections into design, scientific agents can prevent misuse while preserving open scientific collaboration.


#### 5.5 Bias, Fairness, and Data Integrity

Bias in training data can translate directly into biased scientific inferences. Resnik and Hosseini (2025) emphasizes that transparency, data diversity, and reproducibility are moral as well as methodological imperatives for trustworthy science. Lin

- (2024) show that even highly capable models reproduce structural biases unless countered by diverse data and fairness-aware algorithms. Complementary studies (Bano et al., 2023) advocate systematic bias audits and transparent data provenance. To preserve fairness, emerging agents now maintain provenance-rich retrieval pipelines that record dataset versions, query parameters, and model checkpoints. Systems such as BioAgents (Mehandru et al., 2025) and ChemDFM (Zhao et al., 2025) exemplify this practice, coupling retrieval logs with validation layers to document evidence flow. Additional strategies—like counterfactual retrieval prompts that intentionally seek contradictory findings—can further reduce confirmation bias. Ensuring balanced data integrity is therefore inseparable from the ethical pursuit of unbiased scientific knowledge.

5.6 Accountability and Governance

As AI systems influence experimental outcomes and publications, accountability becomes central to research ethics. Bano et al. (2023) identify insufficient institutional readiness for responsible-AI oversight and urge more explicit audit mechanisms. Governance frameworks now increasingly embed oversight into architecture itself. The Multi-Agent Ethics Advocate model (Yamani et al., 2025) assigns reviewer and critic roles to evaluate planner outputs, mirroring human peer review. Likewise, SafeScientist integrates an ethical-reviewer component enforcing task refusals, and RAS-Eval (Fu et al., 2025b) offers standardized safety-testing procedures. These designs converge on multi-layered accountability: technical verifiers, human supervisors, and institutional policies working in concert. As emphasized by Limongi (2024) and Bengio et al.

- (2025), final moral responsibility must remain with humans, with agents functioning as auditable extensions of scientific labor rather than autonomous authors. This principle aligns with Hartung (2025), which stresses that human oversight is indispensable when agents control physical instruments and interpret empirical data in automated laboratories.


- 5.7 Intellectual Property and Research Integrity


LLM integration in research blurs traditional boundaries of authorship and ownership. Limongi (2024) discuss how AI-generated content complicates attribution and credibility, while Lin (2024) emphasize the importance of transparent contribution disclosure. Every AI-assisted artifact—datasets, code, or text—should include provenance metadata detailing model version, prompt template, contributing humans, and licensing terms. Repositories employing immutable records and digital signatures can safeguard both intellectual property and reproducibility. Clear disclosure policies and standardized reporting of AI involvement thus protect human creativity while legitimizing AI-assisted discoveries within ethical research practice.

### 6 Conclusion

This survey provides a mechanism-centric examination of LLM-based scientific agents, revealing that their effectiveness emerges from synergistic integration of four core mechanisms rather than individual component sophistication. Our analysis demonstrates that planners—whether prompt-native or learned—provide the strategic backbone for task decomposition; memory mechanisms enable iterative knowledge accumulation for hypothesis refinement; action spaces operationalize capabilities through tool integration, retrieval, code generation, and reasoning; and verification mechanisms ensure scientific rigor through self-correction, multi-agent critique, human oversight, and tool-based validation. This integrated perspective distinguishes scientific agents from general-purpose systems.

Beyond the architectural components, the survey delves into the benchmarks and real-world impact of these agents. The discussion on benchmarks highlights both the general reasoning ability and the domain-specific scientific competence required for successful application in research environments. The analysis of applications illustrates how these systems are deployed to drive innovations across multiple scientific disciplines, while the ethical discourse emphasizes the need for responsible AI practices that ensure reproducibility, transparency, and adherence to stringent research standards.

Overall, the advancements and challenges presented in this survey point to a promising future where continuous improvements in LLM-based sci-

entific agents could revolutionize scientific discovery. By bridging the gap between theoretical research and practical applications, these agents are set to catalyze new levels of interdisciplinary collaboration and innovation in science.

### A Classification of All Related Work

Table 4: Taxonomy for scientific agents (Part I: Chemistry and Materials Science).

Planner: Instructional / schema-driven planners (P1, ); Context-augmented planners (P2, ); Deliberative / reflective planners (P3, ); Search-based planners (P4, ); Role-interactive / multi-agent planners (P5, ); Programmatic planners (P6, ); Learned planners (SFT) (L1, ); Learned planners (RL/PO) (L2, ) Memory: Historical context memory (M1, ); External knowledge base (M2, ); Intrinsic / parametric memory (M3, ) Action: Tool use (T1, ); Search and retrieval (T2, ); Code generation & execution (T3, ); LLM reasoning actions (T4, ) Verifier: Self-correction (V1, ); Multi-agent critique (V2, ); Human-in-the-loop (V3, ); Tool-based validation (V4, )

###### Method Planner Memory Action Verifier Task Summary

AILA (Mandal et al., 2024) Automating microscopy experiments using LLM agents AccelMat (Kumbhar et al., 2025)

Hypothesis Generation for Materials Discovery and Design

AtomAgents (Ghafarollahi and Buehler, 2024a)

Alloy design and discovery through multi-agent AI.

Self-correcting multi-agent system for chemical experiment design ChatMOF (Kang and Kim,

AutoLabs (Panapitiya et al., 2025)

- 2024)

AI system for predicting and generating MOFs CheMatAgent (Wu et al.,

- 2025)


Enhancing LLMs for Chemistry and Materials Science ChemAgent (Tang et al.,

- 2025b)

Self-updating library improves chemical reasoning in LLMs.

ChemAgents (Song et al., 2025)

Multi-agent robotic AI chemist for autonomous chemical research

ChemCrow (Bran et al., 2024) LLM chemistry agent for diverse chemical tasks ChemDFM (Zhao et al., 2025) Developing LLM for Chemistry with Dialogue Capabilities ChemGraph (Pham et al., 2025)

Agentic framework for computational chemistry workflows automation ChemOrch (Huang et al.,

- 2025c)


Empowering LLMs with Chemical Intelligence via Synthetic Instructions ChemReasoner (Sprueill et al.,

- 2024)

AI-guided catalyst discovery using LLM and quantum-chemical feedback.

Chemist-X (Chen et al.) AI agent for reaction condition optimization Chemma (Zhang et al., 2025d) Accelerating organic chemistry synthesis with LLMs Coscientist (Boiko et al.,

- 2023)

Autonomous chemical research with large language models

El Agente (Zou et al., 2025) Autonomous agent for quantum chemistry with natural language. HoneyComb (Zhang et al.,

- 2024a)


LLM-based agent system for materials science

IR-Agent (Noh et al., 2025) Elucidating molecular structures from infrared spectra LLM-RDF (Ruan et al., 2024) Accelerated end-to-end chemical synthesis with LLMs LLMatDesign (Jia et al., 2024) Autonomous materials discovery using large language models MAPPS (Zhou et al., 2025) Autonomous materials discovery through unified planning and physics. MOOSE-Chem (Yang et al.,

- 2024c)

Discovering novel and valid chemistry hypotheses with LLMs.

MatChat (Chen et al., 2023) Predicting inorganic material synthesis pathways via LLM MatPilot (Ni et al., 2024) MatPilot: LLM-enabled AI materials scientist for human-machine

collaboration MatterChat Multi-modal LLM for material science MechAgents (Ni and Buehler,

- 2024)

LLM multi-agent systems solve mechanics problems autonomously

MetaAgent (Hu et al., 2025a) Autonomous metamaterial agent for EM wave control MolRL-MGPT (Hu et al.,

- 2024b)

De novo drug design using RL with GPT agents Multicrossmodal (Bazgir et al.,

- 2025)


Integrating diverse materials science data via LLM-agent. ORGANA (Darvish et al.,

- 2025)


Robotic assistant for automated chemistry experimentation and characterization

OSDA Agent (Hu et al., 2025b)

De novo design of organic structure directing agents

PriM (Lai and Pu, 2025) Principle-guided materials discovery using multi-agent AI SGA (Ma et al., 2024a) LLMs and simulations for physical scientific discovery SciMON (Wang et al., 2024b) Generate novel scientific ideas grounded in literature. dZiner (Ansari et al., 2024) Rational inverse design of materials with AI agents xChemAgents (Polat et al.,

- 2025)




Agentic AI for Explainable Quantum Chemistry

Table 5: Taxonomy for scientific agents (Part II: Life and Biomedical Sciences).

Method Planner Memory Action Verifier Task Summary

ADAM (Xia et al., 2025a) LLMs as AI Agents for Computational Biophysics AI co-scientist (Gottweis et al.,

AI co-scientist generates, debates, and evolves hypotheses AmadeusGPT (Ye et al.,

- 2025)


- 2023b)

Natural language interface for animal behavior analysis.

AstroAgents (Saeedi et al., 2025)

AI system for mass spectrometry hypothesis generation

AtlasAgent (Yin et al., 2025) Rapid, scalable single-cell integration evaluation with VLMs BIA (Xin et al., 2024) LLM-powered agent for autonomous bioinformatics analysis. BioAgents (Mehandru et al., 2025)

Democratizing bioinformatics analysis with multi-agent systems BioDiscoveryAgent (Roohani

- et al., 2024)

AI agent for designing genetic perturbation experiments

BioGPT (Luo et al., 2022) Generative Transformer for Biomedical Text Generation and Mining BioMaster (Su et al., 2025) Automated multi-agent system for bioinformatics workflows BioScientist Agent (Zhang

- et al., 2025a)


LLM-biomedical agents for drug repurposing and MoA.

BiomedRAG (Li et al., 2024c) Retrieval-augmented LLM for biomedical NLP tasks Biomni (Huang et al., 2025a) General-purpose biomedical AI agent for research tasks CACTUS (McNaughton et al.,

- 2024)

LLM-based agent for chemistry problem-solving using cheminformatics tools.

CRISPR-GPT (Huang et al.,

- 2024a)

Automating gene-editing experiment design with LLM agent

CellAgent (Xiao et al., 2024) LLM-driven multi-agent framework for single-cell data analysis CellForge (Tang et al., 2025d) Agentic Design of Virtual Cell Models CellVoyager (Alber et al.,

- 2025)


AI agent for biological data analysis.

DrugAgent (Inoue et al., 2024) Multi-agent LLM reasoning for DTI prediction. DrugAssist (Ye et al., 2023a) Interactive molecule optimization with large language models DrugPilot (Li et al., 2025a) LLM-based parameterized reasoning agent for drug discovery. GatorTronGPT (Peng et al., 2023)

Generative LLM for medical research and healthcare

GeneGPT (Jin et al., 2024) Augmenting LLMs with domain tools for biomedical information. K-Dense Analyst (Li et al.,

- 2025b)


Automated scientific analysis with a hierarchical multi-agent system

MedAgents (Tang et al., 2023) LLMs as collaborators for zero-shot medical reasoning MyCrunchGPT (Kumar et al., 2023)

ChatGPT-assisted framework for Scientific Machine Learning (SciML)

OLAF (Riffle et al., 2025) Open-source platform for conversational bioinformatics via LLMs. OriGene (Zhang et al., 2025e) Automating therapeutic target discovery with self-evolving AI. ProtAgents (Ghafarollahi and

- Buehler, 2024b)

Protein discovery via LLM multi-agent collaborations

Robin (Ghareeb et al., 2025) Automating scientific discovery through multi-agent system STELLA (Jin et al., 2025) Self-evolving AI agent for biomedical research SciAgents (Ghafarollahi and

- Buehler, 2024c)


Automating scientific discovery through multi-agent graph reasoning

Sparks (Ghafarollahi and Buehler, 2025)

AI discovers protein design principles autonomously.

TAIS (Liu et al., 2024a) Automating scientific discovery using AI scientists TransAgent (Zhang et al., 2025b)

AI agent for transcriptional regulation analysis

- Table 6: Taxonomy for scientific agents (Part III: Physics and Engineering (upper), Astronomy and Astrophysics (middle), Earth, Environmental, and Climate Sciences (lower)).

Method Planner Memory Action Verifier Task Summary

ASA (Liu et al., 2024b) Automated simulation research workflow through LLM prompt engineering. Foam-Agent (Yue et al., 2025) Automating CFD workflows from natural language inputs. MoRA (Jaiswal et al., 2024) Improving LLMs physics reasoning using refinement agents OpenFOAMGPT 2.0 (Feng et al., 2025a)

End-to-end CFD automation via multi-agent framework

OpenFOAMGPT (Pandey et al., 2025)

RAG-Augmented LLM agent for OpenFOAM CFD simulations

SciMARL (Bae and Koumoutsakos, 2022)

Scientific multi-agent reinforcement learning for wall models

k-agents (Cao et al., 2024) Agents for self-driving laboratories applied to quantum computing AI Cosmologist (Moss, 2025) Automate cosmological and astronomical data analysis workflows AstroMLab (de Haan et al.,

2025)

Astronomy Q&A with 70B domain-specialized reasoning model CosmoAgent (Xue et al.,

- 2024)

Simulating alien civilizations with LLM-based agents

LLMSat (Maranto, 2024) LLM-based agent for autonomous space exploration Mephisto (Sun et al., 2024b) Self-improving LLM-based agents for galaxy observations StarWhisper (Wang et al.,

- 2025a)


Automating end-to-end astronomical observations with AI.

ClimateGPT (Thulke et al.,

- 2024)

AI synthesizes interdisciplinary climate change research. Earth-Agent (Feng et al.,

- 2025b)


Agentic framework unifies RGB and spectral EO data

GeoAgent (Chen et al., 2024a) LLM agent for geospatial data analysis GeoMap-Agent (Huang et al., 2025b)

Holistic understanding of geologic maps with MLLMs.

GeoMinLM (Fu et al., 2025a) LLM for geology and mineral exploration in Yunnan. GeoSim.AI (Bekele, 2025) AI assistants for geomechanics numerical simulations MineAgent (Yu et al., 2024) Remote-sensing mineral exploration with MLLMs PANGAEA GPT (Pantiukhin et al., 2025)

Accelerating Earth Science Discovery via Multi-Agent LLMs

- Table 7: Taxonomy for scientific agents (Part IV: Machine Learning and Data Science (upper), Scientific Literature Review and Meta-Research (lower)).


Method Planner Memory Action Verifier Task Summary

AI Scientist (Lu et al., 2024a) Automated open-ended scientific discovery via LLMs AI Scientist-v2 (Yamada et al., 2025)

Automated Scientific Discovery via Agentic Tree Search

AIGS (Liu et al., 2024c) Automated scientific discovery through falsification. Agent Laboratory (Schmidgall et al., 2025)

LLM agents as research assistants

AlphaEvolve (Novikov et al., 2025)

Evolutionary coding agent for scientific and algorithmic discovery CoT-Influx (Huang et al.,

- 2024d)

Boosting LLM reasoning with reinforced context pruning CycleResearcher (Weng et al.,

- 2025)


Automating research and review using open-source LLMs

HyperGen (O’Neill et al., 2025)

Hypothesis generation using structured paper data

MLR-Copilot (Li et al., 2024d)

Autonomous machine learning research with LLM agents.

ReFT (Luong et al., 2024) Reinforced Fine-Tuning enhances LLM reasoning generalization. STEP-DPO (Lai et al., 2024) Step-wise Preference Optimization for LLMs Long-Chain Reasoning SciAgent (Ma et al., 2024b) Tool-augmented LLMs for scientific reasoning ToRA (Gou et al., 2024) Tool-integrated reasoning for mathematical problem solving VirSci (Su et al., 2024) Multi-agent system for scientific idea generation

AI-Researcher (Tang et al., 2025a)

Autonomous system for AI-driven scientific discovery and innovation.

CoI (Li et al., 2024b) Revolutionizing research via novel idea development with LLM agents FlowDPO Improving LLM mathematical reasoning using online multi-agent learning FoodPuzzle (Huang et al., 2024c)

LLM agents for flavor profile sourcing and understanding

InternAgent (Team et al., 2025a)

Autonomous Scientific Research from Hypothesis to Verification

LLM-Find (Ning et al., 2025) Framework for autonomous geospatial data retrieval PaSa (He et al., 2025) LLM agent for comprehensive academic paper search PiFlow (Pu et al., 2025) Principle-aware scientific discovery with multi-agent collaboration ResearchAgent (Baek et al., 2024)

AI system for iterative research idea generation

### References

Samuel Alber, Bowen Chen, Eric Sun, Alina Isakova, Aaron J Wilk, and James Zou. 2025. Cellvoyager: Ai compbio agent generates new insights by autonomously analyzing biological data. bioRxiv, pages 2025–06.

Rohan Anil, Andrew M Dai, Orhan Firat, Melvin Johnson, Dmitry Lepikhin, Alexandre Passos, Siamak Shakeri, Emanuel Taropa, Paige Bailey, Zhifeng Chen, et al. 2023. Palm 2 technical report. arXiv preprint arXiv:2305.10403.

Mehrad Ansari, Jeffrey Watchorn, Carla E Brown, and Joseph S Brown. 2024. dziner: Rational inverse design of materials with ai agents. arXiv preprint arXiv:2410.03963.

Daman Arora, Himanshu Singh, et al. 2023. Have llms advanced enough? a challenging problem solving benchmark for large language models. In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, pages 7527–7543.

H Jane Bae and Petros Koumoutsakos. 2022. Scientific multi-agent reinforcement learning for wallmodels of turbulent flows. Nature Communications, 13(1):1443.

Jinheon Baek, Sujay Kumar Jauhar, Silviu Cucerzan, and Sung Ju Hwang. 2024. Researchagent: Iterative research idea generation over scientific literature with large language models. arXiv preprint arXiv:2404.07738.

Soumya Banerjee et al. 2024. On the ethical considerations of generative agents. arXiv preprint arXiv:2411.19211.

Muneera Bano, Didar Zowghi, Pip Shea, and Georgina Ibarra. 2023. Investigating responsible ai for scientific research: an empirical study. arXiv preprint arXiv:2312.09561.

Adib Bazgir, Yuwen Zhang, et al. 2025. Multicrossmodal automated agent for integrating diverse materials science data. arXiv preprint arXiv:2505.15132.

Yared W Bekele. 2025. Geosim. ai: Ai assistants for numerical simulations in geomechanics. arXiv preprint arXiv:2501.14186.

Yoshua Bengio, Michael Cohen, Damiano Fornasiere, Joumana Ghosn, Pietro Greiner, Matt MacDermott, Sören Mindermann, Adam Oberman, Jesse Richardson, Oliver Richardson, et al. 2025. Superintelligent agents pose catastrophic risks: Can scientist ai offer a safer path? arXiv preprint arXiv:2502.15657.

Daniil A Boiko, Robert MacKnight, Ben Kline, and Gabe Gomes. 2023. Autonomous chemical research with large language models. Nature, 624(7992):570– 578.

Jonathan Bragg, Mike D’Arcy, Nishant Balepur, Dan Bareket, Bhavana Dalvi, Sergey Feldman, Dany Haddad, Jena D Hwang, Peter Jansen, Varsha Kishore, et al. 2025. Astabench: Rigorous benchmarking of ai agents with a scientific research suite. arXiv preprint arXiv:2510.21652.

Andres Bran, Sam Cox, Oliver Schilter, Carlo Baldassari, Andrew D. White, and Philippe Schwaller. 2024. Augmenting large language models with chemistry tools. Nature Machine Intelligence, 6(5):525–535.

Shuxiang Cao, Zijian Zhang, Mohammed Alghadeer, Simone D Fasciati, Michele Piscitelli, Mustafa Bakr, Peter Leek, and Alán Aspuru-Guzik. 2024. Agents for self-driving laboratories applied to quantum computing. arXiv preprint arXiv:2412.07978.

Jun Shern Chan, Neil Chowdhury, Oliver Jaffe, James Aung, Dane Sherburn, Evan Mays, Giulio Starace, Kevin Liu, Leon Maksin, Tejal Patwardhan, et al. 2024. Mle-bench: Evaluating machine learning agents on machine learning engineering. arXiv preprint arXiv:2410.07095.

Juan Manuel Zambrano Chaves, Eric Wang, Tao Tu, Eeshit Dhaval Vaishnav, Byron Lee, S Sara Mahdavi, Christopher Semturs, David Fleet, Vivek Natarajan, and Shekoofeh Azizi. 2024. Tx-llm: A large language model for therapeutics. arXiv preprint arXiv:2406.06316.

K Chen, J Li, K Wang, Y Du, J Yu, J Lu, L Li, J Qiu, J Pan, Y Huang, et al. Chemist-x: Large language model-empowered agent for reaction condition recommendation in chemical synthesis, arxiv, 2023. arXiv preprint arXiv:2311.10776.

Ying-Jung Chen and Vijay K Madisetti. 2024. Information security, ethics, and integrity in llm agent interaction. Journal of Information Security, 16(1):184– 196.

Yuxing Chen, Weijie Wang, Sylvain Lobry, and Camille Kurtz. 2024a. An llm agent for automatic geospatial data analysis. arXiv preprint arXiv:2410.18792.

Zi-Yi Chen, Fan-Kai Xie, Meng Wan, Yang Yuan, Miao Liu, Zong-Guo Wang, Sheng Meng, and Yan-Gang Wang. 2023. Matchat: A large language model and application service platform for materials science. Chinese Physics B, 32(11):118104.

Ziru Chen, Shijie Chen, Yuting Ning, Qianheng Zhang, Boshi Wang, Botao Yu, Yifei Li, Zeyi Liao, Chen Wei, Zitong Lu, Vishal Dey, Mingyi Xue, Frazier N. Baker, Benjamin Burns, Daniel Adu-Ampratwum, Xuhui Huang, Xia Ning, Song Gao, Yu Su, and Huan Sun. 2024b. Scienceagentbench: Toward rigorous assessment of language agents for data-driven scientific discovery. Preprint, arXiv:2410.05080.

Yuheng Cheng, Ceyao Zhang, Zhengwen Zhang, Xiangrui Meng, Sirui Hong, Wenhao Li, Zihao Wang, Zekai Wang, Feng Yin, Junhua Zhao, et al. 2024. Exploring large language model based intelligent agents:

Definitions, methods, and prospects. arXiv preprint arXiv:2401.03428.

Kourosh Darvish, Marta Skreta, Yuchi Zhao, Naruki Yoshikawa, Sagnik Som, Miroslav Bogdanovic, Yang Cao, Han Hao, Haoping Xu, Alán Aspuru-Guzik, et al. 2025. Organa: A robotic assistant for automated chemistry experimentation and characterization. Matter, 8(2).

Tijmen de Haan, Yuan-Sen Ting, Tirthankar Ghosal, Tuan Dung Nguyen, Alberto Accomazzi, Emily Herron, Vanessa Lama, Rui Pan, Azton Wells, and Nesar Ramachandra. 2025. Astromlab 4: Benchmarktopping performance in astronomy q&a with a 70b-parameter domain-specialized reasoning model. arXiv preprint arXiv:2505.17592.

Yihe Deng and Paul Mineiro. 2024. Flow-dpo: Improving llm mathematical reasoning through online multiagent learning. arXiv preprint arXiv:2410.22304.

Jingsen Feng, Ran Xu, and Xu Chu. 2025a. Openfoamgpt 2.0: end-to-end, trustworthy automation for computational fluid dynamics. arXiv preprint arXiv:2504.19338.

Peilin Feng, Zhutao Lv, Junyan Ye, Xiaolei Wang, Xinjie Huo, Jinhua Yu, Wanghan Xu, Wenlong Zhang, Lei Bai, Conghui He, et al. 2025b. Earth-agent: Unlocking the full landscape of earth observation with agents. arXiv preprint arXiv:2509.23141.

Yu Fu, Mingguo Wang, Chengbin Wang, Shuaixian Dong, Jianguo Chen, Jiyuan Wang, Hongping Yu, Jing Huang, Liheng Chang, and Bo Wang. 2025a. Geominlm: A large language model in geology and mineral survey in yunnan province. Ore Geology Reviews, page 106638.

Yuchuan Fu, Xiaohan Yuan, and Dongxia Wang. 2025b. Ras-eval: A comprehensive benchmark for security evaluation of llm agents in real-world environments. arXiv preprint arXiv:2506.15253.

Yubin Ge, Neeraja Kirtane, Hao Peng, and Dilek Hakkani-Tür. 2025. Llms are vulnerable to malicious prompts disguised as scientific language. arXiv preprint arXiv:2501.14073.

- Alireza Ghafarollahi and Markus J Buehler. 2024a. Atomagents: Alloy design and discovery through physics-aware multi-modal multi-agent artificial intelligence. arXiv preprint arXiv:2407.10022.
- Alireza Ghafarollahi and Markus J Buehler. 2024b. Protagents: protein discovery via large language model multi-agent collaborations combining physics and machine learning. Digital Discovery.
- Alireza Ghafarollahi and Markus J Buehler. 2024c. Sciagents: Automating scientific discovery through multi-agent intelligent graph reasoning. arXiv preprint arXiv:2409.05556.


Alireza Ghafarollahi and Markus J. Buehler. 2025. Sparks: Multi-agent artificial intelligence model discovers protein design principles. Preprint, arXiv:2504.19017.

Ali Essam Ghareeb, Benjamin Chang, Ludovico Mitchener, Angela Yiu, Caralyn J Szostkiewicz, Jon M Laurent, Muhammed T Razzak, Andrew D White, Michaela M Hinks, and Samuel G Rodriques. 2025. Robin: A multi-agent system for automating scientific discovery. arXiv preprint arXiv:2505.13400.

Elliot Glazer, Ege Erdil, Tamay Besiroglu, Diego Chicharro, Evan Chen, Alex Gunning, Caroline Falkman Olsson, Jean-Stanislas Denain, Anson Ho, Emily de Oliveira Santos, et al. 2024. Frontiermath: A benchmark for evaluating advanced mathematical reasoning in ai. arXiv preprint arXiv:2411.04872.

Juraj Gottweis, Wei-Hung Weng, Alexander Daryin, Tao Tu, Anil Palepu, Petar Sirkovic, Artiom Myaskovsky, Felix Weissenberger, Keran Rong, Ryutaro Tanno, et al. 2025. Towards an ai co-scientist. Preprint, arXiv:2502.18864.

Zhibin Gou, Zhihong Shao, Yeyun Gong, Yelong Shen, Yujiu Yang, Minlie Huang, Nan Duan, and Weizhu Chen. 2024. Tora: A tool-integrated reasoning agent for mathematical problem solving. In The Twelfth International Conference on Learning Representations, ICLR 2024, Vienna, Austria, May 7-11, 2024. OpenReview.net.

Mourad Gridach, Jay Nanavati, Christina Mack, Khaldoun Zine El Abidine, and Lenon Mendes. 2025. Agentic AI for scientific discovery: A survey of progress, challenges, and future directions. In Towards Agentic AI for Science: Hypothesis Generation, Comprehension, Quantification, and Validation.

Yu Gu, Yiheng Shu, Hao Yu, Xiao Liu, Yuxiao Dong, Jie Tang, Jayanth Srinivasa, Hugo Latapie, and Yu Su. 2024. Middleware for llms: Tools are instrumental for language agents in complex environments. arXiv preprint arXiv:2402.14672.

T Guo, X Chen, Y Wang, R Chang, S Pei, NV Chawla, O Wiest, and X Zhang. 2024. Large language model based multi-agents: A survey of progress and challenges. In 33rd International Joint Conference on Artificial Intelligence (IJCAI 2024). IJCAI; Cornell arxiv.

Thomas Hartung. 2025. Ai, agentic models and lab automation for scientific discovery–the beginning of scaince. Frontiers in Artificial Intelligence, 8:1649155.

Chaoqun He, Renjie Luo, Yuzhuo Bai, Shengding Hu, Zhen Thai, Junhao Shen, Jinyi Hu, Xu Han, Yujie Huang, Yuxiang Zhang, et al. 2024. Olympiadbench: A challenging benchmark for promoting agi with olympiad-level bilingual multimodal scientific problems. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 3828–3850.

Yichen He, Guanhua Huang, Peiyuan Feng, Yuan Lin, Yuchen Zhang, Hang Li, et al. 2025. Pasa: An llm agent for comprehensive academic paper search. arXiv preprint arXiv:2501.10120.

Emily Herron, Junqi Yin, and Feiyi Wang. 2025. Scitrust 2.0: A comprehensive framework for evaluating trustworthiness of large language models in scientific applications. arXiv preprint arXiv:2510.25908.

Shengguo Hu, Mingyi Li, Jiawen Xu, Hongrui Zhang, Shanghang Zhang, Tie Jun Cui, Philipp Del Hougne, and Lianlin Li. 2025a. Electromagnetic metamaterial agent. Light: Science & Applications, 14(1):12.

Sihao Hu, Tiansheng Huang, Fatih Ilhan, Selim Tekin, Gaowen Liu, Ramana Kompella, and Ling Liu. 2024a. A survey on large language model-based game agents. arXiv preprint arXiv:2404.02039.

Xiuyuan Hu, Guoqing Liu, Yang Zhao, and Hao Zhang. 2024b. De novo drug design using reinforcement learning with multiple gpt agents. Advances in Neural Information Processing Systems, 36.

Zhaolin Hu, Yixiao Zhou, Zhongan Wang, Xin Li, Weimin Yang, Hehe Fan, and Yi Yang. 2025b. Osda agent: Leveraging large language models for de novo design of organic structure directing agents. In The Thirteenth International Conference on Learning Representations.

Kaixuan Huang, Yuanhao Qu, Henry Cousins, William A Johnson, Di Yin, Mihir Shah, Denny Zhou, Russ Altman, Mengdi Wang, and Le Cong. 2024a. Crispr-gpt: An llm agent for automated design of gene-editing experiments. arXiv preprint arXiv:2404.18021.

Kexin Huang, Serena Zhang, Hanchen Wang, Yuanhao Qu, Yingzhou Lu, Yusuf Roohani, Ryan Li, Lin Qiu, Gavin Li, Junze Zhang, et al. 2025a. Biomni: A general-purpose biomedical ai agent. biorxiv.

Qian Huang, Jian Vora, Percy Liang, and Jure Leskovec. 2024b. Mlagentbench: Evaluating language agents on machine learning experimentation. Preprint, arXiv:2310.03302.

Tenghao Huang, Donghee Lee, John Sweeney, Jiatong Shi, Emily Steliotes, Matthew Lange, Jonathan May, and Muhao Chen. 2024c. Foodpuzzle: Developing large language model agents as flavor scientists. arXiv preprint arXiv:2409.12832.

Xijie Huang, Li Lyna Zhang, Kwang-Ting Cheng, Fan Yang, and Mao Yang. 2024d. Fewer is more: Boosting math reasoning with reinforced context pruning. In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, pages 13674–13695.

Yangyu Huang, Tianyi Gao, Haoran Xu, Qihao Zhao, Yang Song, Zhipeng Gui, Tengchao Lv, Hao Chen, Lei Cui, Scarlett Li, et al. 2025b. Peace: Empowering geologic map holistic understanding with mllms.

In Proceedings of the Computer Vision and Pattern Recognition Conference, pages 3899–3908.

Yue Huang, Zhengzhe Jiang, Xiaonan Luo, Kehan Guo, Haomin Zhuang, Yujun Zhou, Zhengqing Yuan, Xiaoqi Sun, Jules Schleinitz, Yanbo Wang, et al. 2025c. Chemorch: Empowering llms with chemical intelligence via synthetic instructions. arXiv preprint arXiv:2509.16543.

John B Ingraham, Max Baranov, Zak Costello, Karl W Barber, Wujie Wang, Ahmed Ismail, Vincent Frappier, Dana M Lord, Christopher Ng-Thow-Hing, Erik R Van Vlack, et al. 2023. Illuminating protein space with a programmable generative model. Nature, 623(7989):1070–1078.

Yoshitaka Inoue, Tianci Song, and Tianfan Fu. 2024. Drugagent: Explainable drug repurposing agent with large language model-based reasoning. arXiv preprint arXiv:2408.13378.

Raj Jaiswal, Dhruv Jain, Harsh Parimal Popat, Avinash Anand, Abhishek Dharmadhikari, Atharva Marathe, and Rajiv Ratn Shah. 2024. Improving physics reasoning in large language models using mixture of refinement agents. arXiv preprint arXiv:2412.00821.

Peter A. Jansen, Marc-Alexandre Côté, Tushar Khot, Erin Bransom, Bhavana Dalvi Mishra, Bodhisattwa Prasad Majumder, Oyvind Tafjord, and Peter Clark. 2024. Discoveryworld: A virtual environment for developing and evaluating automated scientific discovery agents. In Advances in Neural Information Processing Systems 38: Annual Conference on Neural Information Processing Systems 2024, NeurIPS 2024, Vancouver, BC, Canada, December 10 - 15, 2024.

Shuyi Jia, Chao Zhang, and Victor Fung. 2024. Llmatdesign: Autonomous materials discovery with large language models. arXiv preprint arXiv:2406.13163.

Zhihuan Jiang, Zhen Yang, Jinhao Chen, Zhengxiao Du, Weihan Wang, Bin Xu, and Jie Tang. 2024. Visscience: An extensive benchmark for evaluating k12 educational multi-modal scientific reasoning. Preprint, arXiv:2409.13730.

Qiao Jin, Yifan Yang, Qingyu Chen, and Zhiyong Lu. 2024. Genegpt: Augmenting large language models with domain tools for improved access to biomedical information. Bioinformatics, 40(2):btae075.

Ruofan Jin, Zaixi Zhang, Mengdi Wang, and Le Cong.

2025. Stella: Self-evolving llm agent for biomedical research. arXiv preprint arXiv:2507.02004.

Liqiang Jing, Zhehui Huang, Xiaoyang Wang, Wenlin Yao, Wenhao Yu, Kaixin Ma, Hongming Zhang, Xinya Du, and Dong Yu. 2024. Dsbench: How far are data science agents to becoming data science experts? Preprint, arXiv:2409.07703.

John Jumper, Richard Evans, Alexander Pritzel, Tim Green, Michael Figurnov, Olaf Ronneberger, Kathryn Tunyasuvunakool, Russ Bates, Augustin Žídek, Anna Potapenko, et al. 2021. Highly accurate protein structure prediction with alphafold. nature, 596(7873):583–589.

Samira Ebrahimi Kahou, Vincent Michalski, Adam Atkinson, Ákos Kádár, Adam Trischler, and Yoshua Bengio. 2018. Figureqa: An annotated figure dataset for visual reasoning. In 6th International Conference on Learning Representations, ICLR 2018, Vancouver, BC, Canada, April 30 - May 3, 2018, Workshop Track Proceedings. OpenReview.net.

Yeonghun Kang and Jihan Kim. 2024. Chatmof: an artificial intelligence system for predicting and generating metal-organic frameworks using large language models. Nature communications, 15(1):4705.

Yeonghun Kang, Hyunsoo Park, Berend Smit, and Jihan Kim. 2023. A multi-modal pre-training transformer for universal transfer learning in metal– organic frameworks. Nature Machine Intelligence, 5(3):309–318.

Varun Kumar, Leonard Gleyzer, Adar Kahana, Khemraj Shukla, and George Em Karniadakis. 2023. Mycrunchgpt: A llm assisted framework for scientific machine learning. Journal of Machine Learning for Modeling and Computing, 4(4).

Shrinidhi Kumbhar, Venkatesh Mishra, Kevin Coutinho, Divij Handa, Ashif Iquebal, and Chitta Baral. 2025. Hypothesis generation for materials discovery and design using goal-driven and constraint-guided llm agents. arXiv preprint arXiv:2501.13299.

Xin Lai, Zhuotao Tian, Yukang Chen, Senqiao Yang, Xiangru Peng, and Jiaya Jia. 2024. Step-dpo: Step-wise preference optimization for long-chain reasoning of llms. arXiv preprint arXiv:2406.18629.

Zheyuan Lai and Yingming Pu. 2025. Prim: Principleinspired material discovery through multi-agent collaboration. arXiv preprint arXiv:2504.08810.

Jon M. Laurent, Joseph D. Janizek, Michael Ruzo, Michaela M. Hinks, Michael J. Hammerling, Siddharth Narayanan, Manvitha Ponnapati, Andrew D. White, and Samuel G. Rodriques. 2024. Lab-bench: Measuring capabilities of language models for biology research. Preprint, arXiv:2407.10362.

Kun Li, Zhennan Wu, Shoupeng Wang, Jia Wu, Shirui Pan, and Wenbin Hu. 2025a. Drugpilot: Llm-based parameterized reasoning agent for drug discovery. arXiv preprint arXiv:2505.13940.

Lei Li, Yuqi Wang, Runxin Xu, Peiyi Wang, Xiachong Feng, Lingpeng Kong, and Qi Liu. 2024a. Multimodal arxiv: A dataset for improving scientific comprehension of large vision-language models. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), ACL 2024, Bangkok, Thailand, August

11-16, 2024, pages 14369–14387. Association for Computational Linguistics.

Long Li, Weiwen Xu, Jiayan Guo, Ruochen Zhao, Xingxuan Li, Yuqian Yuan, Boqiang Zhang, Yuming Jiang, Yifei Xin, Ronghao Dang, et al. 2024b. Chain of ideas: Revolutionizing research via novel idea development with llm agents. arXiv preprint arXiv:2410.13185.

Mingchen Li, Halil Kilicoglu, Hua Xu, and Rui Zhang. 2024c. Biomedrag: A retrieval augmented large language model for biomedicine. Preprint, arXiv:2405.00465.

Orion Li, Vinayak Agarwal, Summer Zhou, Ashwin Gopinath, and Timothy Kassis. 2025b. K-dense analyst: Towards fully automated scientific analysis. arXiv preprint arXiv:2508.07043.

Ruochen Li, Teerth Patel, Qingyun Wang, and Xinya Du. 2024d. Mlr-copilot: Autonomous machine learning research based on large language models agents. arXiv preprint arXiv:2408.14033.

Xinyi Li, Sai Wang, Siqi Zeng, Yu Wu, and Yi Yang. 2024e. A survey on llm-based multi-agent systems: workflow, infrastructure, and challenges. Vicinagearth, 1(1):9.

Zekun Li, Xianjun Yang, Kyuri Choi, Wanrong Zhu, Ryan Hsieh, HyeonJung Kim, Jin Hyuk Lim, Sungyoung Ji, Byungju Lee, Xifeng Yan, Linda Ruth Petzold, Stephen D. Wilson, Woosang Lim, and William Yang Wang. 2024f. Mmsci: A dataset for graduate-level multi-discipline multimodal scientific understanding. Preprint, arXiv:2407.04903.

Ricardo Limongi. 2024. The use of artificial intelligence in scientific research with integrity and ethics. Future Studies Research Journal: Trends and Strategies, 16(1):e845–e845.

Zhicheng Lin. 2024. Beyond principlism: practical strategies for ethical ai use in research practices. AI and Ethics, pages 1–13.

Haoyang Liu, Yijiang Li, Jinglin Jian, Yuxuan Cheng, Jianrong Lu, Shuyi Guo, Jinglei Zhu, Mianchen Zhang, Miantong Zhang, and Haohan Wang. 2024a. Toward a team of ai-made scientists for scientific discovery from gene expression data. arXiv preprint arXiv:2402.12391.

Yujie Liu, Zonglin Yang, Tong Xie, Jinjie Ni, Ben Gao, Yuqiang Li, Shixiang Tang, Wanli Ouyang, Erik Cambria, and Dongzhan Zhou. 2025. Researchbench: Benchmarking llms in scientific discovery via inspiration-based task decomposition. Preprint, arXiv:2503.21248.

Zhihan Liu, Yubo Chai, and Jianfeng Li. 2024b. Toward automated simulation research workflow through llm prompt engineering design. Journal of Chemical Information and Modeling, 65(1):114–124.

Zijun Liu, Kaiming Liu, Yiqi Zhu, Xuanyu Lei, Zonghan Yang, Zhenhe Zhang, Peng Li, and Yang Liu. 2024c. Aigs: Generating science from aipowered automated falsification. arXiv preprint arXiv:2411.11910.

Chris Lu, Cong Lu, Robert Tjarko Lange, Jakob Foerster, Jeff Clune, and David Ha. 2024a. The ai scientist: Towards fully automated open-ended scientific discovery. arXiv preprint arXiv:2408.06292.

Pan Lu, Hritik Bansal, Tony Xia, Jiacheng Liu, Chunyuan Li, Hannaneh Hajishirzi, Hao Cheng, Kai-Wei Chang, Michel Galley, and Jianfeng Gao. 2024b. Mathvista: Evaluating mathematical reasoning of foundation models in visual contexts. In The Twelfth International Conference on Learning Representations, ICLR 2024, Vienna, Austria, May 7-11, 2024. OpenReview.net.

Pan Lu, Ran Gong, Shibiao Jiang, Liang Qiu, Siyuan Huang, Xiaodan Liang, and Song-Chun Zhu. 2021. Inter-GPS: Interpretable geometry problem solving with formal language and symbolic reasoning. In Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers), pages 6774– 6786, Online. Association for Computational Linguistics.

Renqian Luo, Liai Sun, Yingce Xia, Tao Qin, Sheng Zhang, Hoifung Poon, and Tie-Yan Liu. 2022. Biogpt: generative pre-trained transformer for biomedical text generation and mining. Briefings in bioinformatics, 23(6):bbac409.

Ziming Luo, Zonglin Yang, Zexin Xu, Wei Yang, and Xinya Du. 2025. Llm4sr: A survey on large language models for scientific research. arXiv preprint arXiv:2501.04306.

Trung Quoc Luong, Xinbo Zhang, Zhanming Jie, Peng Sun, Xiaoran Jin, and Hang Li. 2024. Reft: Reasoning with reinforced fine-tuning. arXiv preprint arXiv:2401.08967.

Liuzhenghao Lv, Zongying Lin, Hao Li, Yuyang Liu, Jiaxi Cui, Calvin Yu-Chian Chen, Li Yuan, and Yonghong Tian. 2024. Prollama: A protein language model for multi-task protein language processing. arXiv preprint arXiv:2402.16445.

Pingchuan Ma, Tsun-Hsuan Wang, Minghao Guo, Zhiqing Sun, Joshua B. Tenenbaum, Daniela Rus, Chuang Gan, and Wojciech Matusik. 2024a. LLM and simulation as bilevel optimizers: A new paradigm to advance physical scientific discovery. In Forty-first International Conference on Machine Learning, ICML 2024, Vienna, Austria, July 21-27, 2024. OpenReview.net.

Yubo Ma, Zhibin Gou, Junheng Hao, Ruochen Xu, Shuohang Wang, Liangming Pan, Yujiu Yang, Yixin Cao, and Aixin Sun. 2024b. Sciagent: Toolaugmented language models for scientific reasoning.

In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, EMNLP 2024, Miami, FL, USA, November 12-16, 2024, pages 15701–15736. Association for Computational Linguistics.

Bodhisattwa Prasad Majumder, Harshit Surana, Dhruv Agarwal, Bhavana Dalvi Mishra, Abhijeetsingh Meena, Aryan Prakhar, Tirth Vora, Tushar Khot, Ashish Sabharwal, and Peter Clark. 2024. Discoverybench: Towards data-driven discovery with large language models. Preprint, arXiv:2407.01725.

Indrajeet Mandal, Jitendra Soni, Mohd Zaki, Morten M Smedskjaer, Katrin Wondraczek, Lothar Wondraczek, Nitya Nand Gosvami, and NM Krishnan. 2024. Autonomous microscopy experiments through large language model agents. arXiv preprint arXiv:2501.10385.

David Maranto. 2024. Llmsat: A large language modelbased goal-oriented agent for autonomous space exploration. arXiv preprint arXiv:2405.01392.

Andrew D McNaughton, Gautham Krishna Sankar Ramalaxmi, Agustin Kruel, Carter R Knutson, Rohith A Varikoti, and Neeraj Kumar. 2024. Cactus: Chemistry agent connecting tool usage to science. ACS omega, 9(46):46563–46573.

Nikita Mehandru, Amanda K Hall, Olesya Melnichenko, Yulia Dubinina, Daniel Tsirulnikov, David Bamman, Ahmed Alaa, Scott Saponas, and Venkat S Malladi. 2025. Bioagents: Democratizing bioinformatics analysis with multi-agent systems. arXiv preprint arXiv:2501.06314.

Grégoire Mialon, Clémentine Fourrier, Craig Swift, Thomas Wolf, Yann LeCun, and Thomas Scialom. 2023. Gaia: a benchmark for general ai assistants. Preprint, arXiv:2311.12983.

Henry E Miller, Matthew Greenig, Benjamin Tenmann, and Bo Wang. 2025. Bioml-bench: Evaluation of ai agents for end-to-end biomedical ml. bioRxiv, pages 2025–09.

Ludovico Mitchener, Jon M Laurent, Benjamin Tenmann, Siddharth Narayanan, Geemi P Wellawatte, Andrew White, Lorenzo Sani, and Samuel G Rodriques. 2025. Bixbench: a comprehensive benchmark for llm-based agents in computational biology. arXiv preprint arXiv:2503.00096.

Adam Moss. 2025. The ai cosmologist i: An agentic system for automated data analysis. arXiv preprint arXiv:2504.03424.

Bo Ni and Markus J Buehler. 2024. Mechagents: Large language model multi-agent collaborations can solve mechanics problems, generate new data, and integrate knowledge. Extreme Mechanics Letters, 67:102131.

Ziqi Ni, Yahao Li, Kaijia Hu, Kunyuan Han, Ming Xu, Xingyu Chen, Fengqi Liu, Yicong Ye, and Shuxin Bai. 2024. Matpilot: an llm-enabled ai materials scientist under the framework of human-machine collaboration. arXiv preprint arXiv:2411.08063.

Huan Ning, Zhenlong Li, Temitope Akinboyewa, and M Naser Lessani. 2025. An autonomous gis agent framework for geospatial data retrieval. International Journal of Digital Earth, 18(1):2458688.

Heewoong Noh, Namkyeong Lee, Gyoung S Na, Kibum Kim, and Chanyoung Park. 2025. Ir-agent: Expertinspired llm agents for structure elucidation from infrared spectra. arXiv preprint arXiv:2508.16112.

Natalia Norori, Denisse Albornoz, and Vanessa McBride. 2025. Data and ai for science-key considerations.

Alexander Novikov, Ngân V˜u, Marvin Eisenberger, Emilien Dupont, Po-Sen Huang, Adam Zsolt Wagner, Sergey Shirobokov, Borislav Kozlovskii, Francisco J. R. Ruiz, Abbas Mehrabian, M. Pawan Kumar, Abigail See, Swarat Chaudhuri, George Holland, Alex Davies, Sebastian Nowozin, Pushmeet Kohli, and Matej Balog. 2025. Alphaevolve: A coding agent for scientific and algorithmic discovery. Preprint, arXiv:2506.13131.

Charles O’Neill, Tirthankar Ghosal, Roberta R˘aileanu, Mike Walmsley, Thang Bui, Kevin Schawinski, and Ioana Ciuc˘a. 2025. Sparks of science: Hypothesis generation using structured paper data. Preprint, arXiv:2504.12976.

Gihan Panapitiya, Emily Saldanha, Heather Job, and Olivia Hess. 2025. Autolabs: Cognitive multi-agent systems with self-correction for autonomous chemical experimentation. arXiv preprint arXiv:2509.25651.

Sandeep Pandey, Ran Xu, Wenkang Wang, and Xu Chu. 2025. Openfoamgpt: a rag-augmented llm agent for openfoam-based computational fluid dynamics. arXiv preprint arXiv:2501.06327.

Dmitrii Pantiukhin, Boris Shapkin, Ivan Kuznetsov, Antonia Anna Jost, and Nikolay Koldunov. 2025. Accelerating earth science discovery via multi-agent llm systems. arXiv preprint arXiv:2503.05854.

Hyunsoo Park, Yeonghun Kang, and Jihan Kim. 2023. Enhancing structure–property relationships in porous materials through transfer learning and cross-material few-shot learning. ACS Applied Materials & Interfaces, 15(48):56375–56385.

Cheng Peng, Xi Yang, Aokun Chen, Kaleb E Smith, Nima PourNejatian, Anthony B Costa, Cheryl Martin, Mona G Flores, Ying Zhang, Tanja Magoc, et al. 2023. A study of generative large language model for medical research and healthcare. NPJ digital medicine, 6(1):210.

Roy H Perlis, Joseph F Goldberg, Michael J Ostacher, and Christopher D Schneck. 2024. Clinical decision support for bipolar depression using large language models. Neuropsychopharmacology, pages 1–5.

Thang D Pham, Aditya Tanikanti, and Murat Keçeli. 2025. Chemgraph: An agentic framework for computational chemistry workflows. arXiv preprint arXiv:2506.06363.

Long Phan, Alice Gatti, and etc. 2025. Humanity’s last exam. Preprint, arXiv:2501.14249.

Can Polat, Mehmet Tuncel, Mustafa Kurban, Erchin Serpedin, and Hasan Kurban. 2025. xchemagents: Agentic ai for explainable quantum chemistry. arXiv preprint arXiv:2505.20574.

Evangelos Pournaras. 2023. Science in the era of chatgpt, large language models and generative ai. KIKritik/AI Critique Volume 6, page 275.

Yingming Pu, Tao Lin, and Hongyu Chen. 2025. Piflow: Principle-aware scientific discovery with multi-agent collaboration. Preprint, arXiv:2505.15047.

Rafael Rafailov, Archit Sharma, Eric Mitchell, Christopher D Manning, Stefano Ermon, and Chelsea Finn. 2023. Direct preference optimization: Your language model is secretly a reward model. Advances in neural information processing systems, 36:53728–53741.

David Rein, Betty Li Hou, Asa Cooper Stickland, Jackson Petty, Richard Yuanzhe Pang, Julien Dirani, Julian Michael, and Samuel R Bowman. 2024. Gpqa: A graduate-level google-proof q&a benchmark. In First Conference on Language Modeling.

David B Resnik and Mohammad Hosseini. 2025. The ethics of using artificial intelligence in scientific research: new guidance needed for a new tool. AI and Ethics, 5(2):1499–1521.

Dylan Riffle, Nima Shirooni, Cody He, Manush Murali, Sovit Nayak, Rishikumar Gopalan, and Diego Gonzalez Lopez. 2025. Olaf: An open life science analysis framework for conversational bioinformatics powered by large language models. arXiv preprint arXiv:2504.03976.

Yusuf Roohani, Andrew Lee, Qian Huang, Jian Vora, Zachary Steinhart, Kexin Huang, Alexander Marson, Percy Liang, and Jure Leskovec. 2024. Biodiscoveryagent: An ai agent for designing genetic perturbation experiments. arXiv preprint arXiv:2405.17631.

Jiacheng Ruan, Dan Jiang, Xian Gao, Ting Liu, Yuzhuo Fu, and Yangyang Kang. 2025. Mme-sci: A comprehensive and challenging science benchmark for multimodal large language models. arXiv preprint arXiv:2508.13938.

Yixiang Ruan, Chenyin Lu, Ning Xu, Jian Zhang, Jun Xuan, Jianzhang Pan, Qun Fang, Hanyu Gao, Xiaodong Shen, Ning Ye, et al. 2024. Accelerated endto-end chemical synthesis development with large language models.

Daniel Saeedi, Denise Buckner, Jose C Aponte, and Amirali Aghazadeh. 2025. Astroagents: A multiagent ai for hypothesis generation from mass spectrometry data. arXiv preprint arXiv:2503.23170.

Samuel Schmidgall, Yusheng Su, Ze Wang, Ximeng Sun, Jialian Wu, Xiaodong Yu, Jiang Liu, Zicheng Liu, and Emad Barsoum. 2025. Agent laboratory: Using llm agents as research assistants. arXiv preprint arXiv:2501.04227.

John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. 2017. Proximal policy optimization algorithms. arXiv preprint arXiv:1707.06347.

Haiyang Shen, Yue Li, Desong Meng, Dongqi Cai, Sheng Qi, Li Zhang, Mengwei Xu, and Yun Ma. 2025. Shortcutsbench: A large-scale real-world benchmark for api-based agents. In The Thirteenth International Conference on Learning Representations.

Yongliang Shen, Kaitao Song, Xu Tan, Wenqi Zhang, Kan Ren, Siyu Yuan, Weiming Lu, Dongsheng Li, and Yueting Zhuang. 2024. Taskbench: Benchmarking large language models for task automation. Preprint, arXiv:2311.18760.

Zhuocheng Shen. 2024. Llm with tools: A survey. arXiv preprint arXiv:2409.18807.

Jinghang Shi, Xiao Yu Tang, Yang Hunag, Yuyang Li, Yanxia Zhang, Caizhan Yue, et al. 2025. Astrommbench: A benchmark for evaluating multimodal large language models capabilities in astronomy. arXiv preprint arXiv:2510.00063.

Zachary S Siegel, Sayash Kapoor, Nitya Nagdir, Benedikt Stroebl, and Arvind Narayanan. 2024. Core-bench: Fostering the credibility of published research through a computational reproducibility agent benchmark. arXiv preprint arXiv:2409.11363.

Simranjit Singh, Michael Fore, and Dimitrios Stamoulis. 2024. Evaluating tool-augmented agents in remote sensing platforms. arXiv preprint arXiv:2405.00709.

Tao Song, Man Luo, Xiaolong Zhang, Linjiang Chen, Yan Huang, Jiaqi Cao, Qing Zhu, Daobin Liu, Baicheng Zhang, Gang Zou, et al. 2025. A multiagent-driven robotic ai chemist enabling autonomous chemical research on demand. Journal of the American Chemical Society, 147(15):12534– 12545.

Henry W Sprueill, Carl Edwards, Khushbu Agarwal, Mariefel V Olarte, Udishnu Sanyal, Conrad Johnston, Hongbin Liu, Heng Ji, and Sutanay Choudhury. 2024. Chemreasoner: Heuristic search over a large language model’s knowledge space using quantum-chemical feedback. arXiv preprint arXiv:2402.10980.

Haoyang Su, Renqi Chen, Shixiang Tang, Xinzhe Zheng, Jingzhe Li, Zhenfei Yin, Wanli Ouyang, and Nanqing Dong. 2024. Two heads are better

than one: A multi-agent system has the potential to improve scientific idea generation. arXiv preprint arXiv:2410.09403.

Houcheng Su, Weicai Long, and Yanlin Zhang. 2025. Biomaster: Multi-agent system for automated bioinformatics analysis workflow. bioRxiv, pages 2025– 01.

Liangtai Sun, Yang Han, Zihan Zhao, Da Ma, Zhennan Shen, Baocai Chen, Lu Chen, and Kai Yu. 2024a. Scieval: A multi-level large language model evaluation benchmark for scientific research. In Thirty-Eighth AAAI Conference on Artificial Intelligence, AAAI 2024, Thirty-Sixth Conference on Innovative Applications of Artificial Intelligence, IAAI 2024, Fourteenth Symposium on Educational Advances in Artificial Intelligence, EAAI 2014, February 20-27, 2024, Vancouver, Canada, pages 19053–19061. AAAI Press.

Qiushi Sun, Zhoumianze Liu, Chang Ma, Zichen Ding, Fangzhi Xu, Zhangyue Yin, Haiteng Zhao, Zhenyu Wu, Kanzhi Cheng, Zhaoyang Liu, et al. 2025. Scienceboard: Evaluating multimodal autonomous agents in realistic scientific workflows. arXiv preprint arXiv:2505.19897.

Zechang Sun, Yuan-Sen Ting, Yaobo Liang, Nan Duan, Song Huang, and Zheng Cai. 2024b. Interpreting multi-band galaxy observations with large language model-based agents. arXiv preprint arXiv:2409.14807.

Jiabin Tang, Lianghao Xia, Zhonghang Li, and Chao Huang. 2025a. Ai-researcher: Autonomous scientific innovation. arXiv preprint arXiv:2505.18705.

Xiangru Tang, Tianyu Hu, Muyang Ye, Yanjun Shao, Xunjian Yin, Siru Ouyang, Wangchunshu Zhou, Pan Lu, Zhuosheng Zhang, Yilun Zhao, et al. 2025b. Chemagent: Self-updating library in large language models improves chemical reasoning. arXiv preprint arXiv:2501.06590.

Xiangru Tang, Qiao Jin, Kunlun Zhu, Tongxin Yuan, Yichi Zhang, Wangchunshu Zhou, Meng Qu, Yilun Zhao, Jian Tang, Zhuosheng Zhang, et al. 2025c. Risks of ai scientists: prioritizing safeguarding over autonomy. Nature Communications, 16(1):8317.

Xiangru Tang, Zhuoyun Yu, Jiapeng Chen, Yan Cui, Daniel Shao, Weixu Wang, Fang Wu, Yuchen Zhuang, Wenqi Shi, Zhi Huang, et al. 2025d. Cellforge: Agentic design of virtual cell models. arXiv preprint arXiv:2508.02276.

Xiangru Tang, Anni Zou, Zhuosheng Zhang, Ziming Li, Yilun Zhao, Xingyao Zhang, Arman Cohan, and Mark Gerstein. 2023. Medagents: Large language models as collaborators for zero-shot medical reasoning. arXiv preprint arXiv:2311.10537.

Yingheng Tang, Wenbin Xu, Jie Cao, Weilu Gao, Steve Farrell, Benjamin Erichson, Michael W Mahoney, Andy Nonaka, and Zhi Yao. 2025e. Matterchat: A multi-modal llm for material science. arXiv preprint arXiv:2502.13107.

NovelSeek Team, Bo Zhang, Shiyang Feng, Xiangchao Yan, Jiakang Yuan, Zhiyin Yu, Xiaohan He, Songtao Huang, Shaowei Hou, Zheng Nie, et al. 2025a. Internagent: When agent becomes the scientist – building closed-loop system from hypothesis to verification. arXiv preprint arXiv:2505.16938.

P Team, Xinrun Du, Yifan Yao, Kaijing Ma, Bingli Wang, Tianyu Zheng, Kang Zhu, Minghao Liu, Yiming Liang, Xiaolong Jin, Zhenlin Wei, Chujie Zheng, Kaixin Deng, Shian Jia, Sichao Jiang, Yiyan Liao, Rui Li, Qinrui Li, Sirun Li, Yizhi Li, Yunwen Li, Dehua Ma, Yuansheng Ni, Haoran Que, Qiyao Wang, Zhoufutu Wen, Siwei Wu, Tianshun Xing, Ming Xu, Zhenzhu Yang, Zekun Moore Wang, Junting Zhou, Yuelin Bai, Xingyuan Bu, Chenglin Cai, Liang Chen, Yifan Chen, Chengtuo Cheng, Tianhao Cheng, Keyi Ding, Siming Huang, Yun Huang, Yaoru Li, Yizhe Li, Zhaoqun Li, Tianhao Liang, Chengdong Lin, Hongquan Lin, Yinghao Ma, Tianyang Pang, Zhongyuan Peng, Zifan Peng, Qige Qi, Shi Qiu, Xingwei Qu, Shanghaoran Quan, Yizhou Tan, Zili Wang, Chenqing Wang, Hao Wang, Yiya Wang, Yubo Wang, Jiajun Xu, Kexin Yang, Ruibin Yuan, Yuanhao Yue, Tianyang Zhan, Chun Zhang, Jinyang Zhang, Xiyue Zhang, Xingjian Zhang, Yue Zhang, Yongchi Zhao, Xiangyu Zheng, Chenghua Zhong, Yang Gao, Zhoujun Li, Dayiheng Liu, Qian Liu, Tianyu Liu, Shiwen Ni, Junran Peng, Yujia Qin, Wenbo Su, Guoyin Wang, Shi Wang, Jian Yang, Min Yang, Meng Cao, Xiang Yue, Zhaoxiang Zhang, Wangchunshu Zhou, Jiaheng Liu, Qunshu Lin, Wenhao Huang, and Ge Zhang. 2025b. Supergpqa: Scaling llm evaluation across 285 graduate disciplines. Preprint, arXiv:2502.14739.

Elizaveta Tennant, Stephen Hailes, and Mirco Musolesi. 2025. Hybrid approaches for moral value alignment in ai agents: a manifesto. Preprint, arXiv:2312.01818.

David Thulke, Yingbo Gao, Petrus Pelser, Rein Brune, Rricha Jalota, Floris Fok, Michael Ramos, Ian van Wyk, Abdallah Nasir, Hayden Goldstein, et al. 2024. Climategpt: Towards ai synthesizing interdisciplinary research on climate change. arXiv preprint arXiv:2401.09646.

Minyang Tian, Luyu Gao, Shizhuo Dylan Zhang, Xinan Chen, Cunwei Fan, Xuefei Guo, Roland Haas, Pan Ji, Kittithat Krongchon, Yao Li, Shengyan Liu, Di Luo, Yutao Ma, Hao Tong, Kha Trinh, Chenyu Tian, Zihan Wang, Bohao Wu, Yanyu Xiong, Shengzhu Yin, Minhui Zhu, Kilian Lieret, Yanxin Lu, Genglin Liu, Yufeng Du, Tianhua Tao, Ofir Press, Jamie Callan, Eliu Huerta, and Hao Peng. 2024. Scicode: A research coding benchmark curated by scientists. Preprint, arXiv:2407.13168.

Cunshi Wang, Xinjie Hu, Yu Zhang, Xunhao Chen, Pengliang Du, Yiming Mao, Rui Wang, Yuyang Li, Ying Wu, Hang Yang, Yansong Li, Beichuan Wang, Haiyang Mu, Zheng Wang, Jianfeng Tian, Liang Ge, Yongna Mao, Shengming Li, Xiaomeng Lu, Jinhang Zou, Yang Huang, Ningchen Sun, Jie Zheng, Min He,

Yu Bai, Junjie Jin, Hong Wu, and Jifeng Liu. 2025a. Starwhisper telescope: Agent-based observation assistant system to approach ai astrophysicist. Preprint, arXiv:2412.06412.

Daoyu Wang, Mingyue Cheng, Qi Liu, Shuo Yu, Zirui Liu, and Ze Guo. 2025b. Paperarena: An evaluation benchmark for tool-augmented agentic reasoning on scientific literature. arXiv preprint arXiv:2510.10909.

Lei Wang, Chen Ma, Xueyang Feng, Zeyu Zhang, Hao Yang, Jingsen Zhang, Zhiyuan Chen, Jiakai Tang, Xu Chen, Yankai Lin, et al. 2024a. A survey on large language model based autonomous agents. Frontiers of Computer Science, 18(6):186345.

Qingyun Wang, Doug Downey, Heng Ji, and Tom Hope. 2024b. Scimon: Scientific inspiration machines optimized for novelty. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), ACL 2024, Bangkok, Thailand, August 11-16, 2024, pages 279– 299. Association for Computational Linguistics.

Xiaoxuan Wang, Ziniu Hu, Pan Lu, Yanqiao Zhu, Jieyu Zhang, Satyen Subramaniam, Arjun R. Loomba, Shichang Zhang, Yizhou Sun, and Wei Wang. 2024c. Scibench: Evaluating college-level scientific problem-solving abilities of large language models. In Forty-first International Conference on Machine Learning, ICML 2024, Vienna, Austria, July 21-27, 2024. OpenReview.net.

Xinming Wang, Jian Xu, Aslan H Feng, Yi Chen, Haiyang Guo, Fei Zhu, Yuanqi Shao, Minsi Ren, Hongzhu Yi, Sheng Lian, et al. 2025c. The hitchhiker’s guide to autonomous research: A survey of scientific agents.

Ryan Watkins. 2024. Guidance for researchers and peerreviewers on the ethical use of large language models (llms) in scientific research workflows. AI and Ethics, 4(4):969–974.

Jiaqi Wei, Yuejin Yang, Xiang Zhang, Yuhan Chen, Xiang Zhuang, Zhangyang Gao, Dongzhan Zhou, Guangshuai Wang, Zhiqiang Gao, Juntai Cao, Zijie Qiu, Xuming He, Qiang Zhang, Chenyu You, Shuangjia Zheng, Ning Ding, Wanli Ouyang, Nanqing Dong, Yu Cheng, Siqi Sun, Lei Bai, and Bowen Zhou. 2025. From ai for science to agentic science: A survey on autonomous scientific discovery. Preprint, arXiv:2508.14111.

Yixuan Weng, Minjun Zhu, Guangsheng Bao, Hongbo Zhang, Jindong Wang, Yue Zhang, and Linyi Yang. 2025. Cycleresearcher: Improving automated research via automated review. Preprint, arXiv:2411.00816.

Kevin E Wu, Kevin K Yang, Rianne van den Berg, Sarah Alamdari, James Y Zou, Alex X Lu, and Ava P Amini. 2024. Protein structure generation via folding diffusion. Nature communications, 15(1):1059.

Mengsong Wu, YaFei Wang, Yidong Ming, Yuqi An, Yuwei Wan, Wenliang Chen, Binbin Lin, Yuqiang Li, Tong Xie, and Dongzhan Zhou. 2025. Chematagent: Enhancing llms for chemistry and materials science through tree-search based tool learning. Preprint, arXiv:2506.07551.

Zhiheng Xi, Wenxiang Chen, Xin Guo, Wei He, Yiwen Ding, Boyang Hong, Ming Zhang, Junzhe Wang, Senjie Jin, Enyu Zhou, et al. 2023. The rise and potential of large language model based agents: A survey. arXiv preprint arXiv:2309.07864.

Yijie Xia, Xiaohan Lin, Zicheng Ma, Jinyuan Hu, Yanheng Li, Zhaoxin Xie, Hao Li, Li Yang, Zhiqiang Zhao, Lijiang Yang, et al. 2025a. Large language models as ai agents for digital atoms and molecules: Catalyzing a new era in computational biophysics. arXiv preprint arXiv:2505.00270.

Yingce Xia, Peiran Jin, Shufang Xie, Liang He, Chuan Cao, Renqian Luo, Guoqing Liu, Yue Wang, Zequn Liu, Yuan-Jyue Chen, et al. 2025b. Naturelm: Deciphering the language of nature for scientific discovery. arXiv preprint arXiv:2502.07527.

Yihang Xiao, Jinyi Liu, Yan Zheng, Xiaohan Xie, Jianye Hao, Mingzhi Li, Ruitao Wang, Fei Ni, Yuxiao Li, Jintian Luo, et al. 2024. Cellagent: An llm-driven multi-agent framework for automated single-cell data analysis. arXiv preprint arXiv:2407.09811.

Junlin Xie, Zhihong Chen, Ruifei Zhang, Xiang Wan, and Guanbin Li. 2024. Large multimodal agents: A survey. arXiv preprint arXiv:2402.15116.

Qi Xin, Quyu Kong, Hongyi Ji, Yue Shen, Yuqi Liu, Yan Sun, Zhilin Zhang, Zhaorong Li, Xunlong Xia, Bing Deng, et al. 2024. Bioinformatics agent (bia): Unleashing the power of large language models to reshape bioinformatics workflow. BioRxiv, pages 2024–05.

Wanghan Xu, Xiangyu Zhao, Yuhao Zhou, Xiaoyu Yue, Ben Fei, Fenghua Ling, Wenlong Zhang, and Lei Bai. 2025a. Earthse: A benchmark evaluating earth scientific exploration capability for large language models. arXiv preprint arXiv:2505.17139.

Wujiang Xu, Zujie Liang, Kai Mei, Hang Gao, Juntao Tan, and Yongfeng Zhang. 2025b. A-mem: Agentic memory for llm agents. arXiv preprint arXiv:2502.12110.

Xueqing Xu, Boris Bolliet, Adrian Dimitrov, Andrew Laverick, Francisco Villaescusa-Navarro, Licong Xu, and Íñigo Zubeldia. 2025c. Evaluating retrievalaugmented generation agents for autonomous scientific discovery in astrophysics. arXiv preprint arXiv:2507.07155.

Zhaoqian Xue, Beichen Wang, Suiyuan Zhu, Kai Mei, Hua Tang, Wenyue Hua, Mengnan Du, and Yongfeng Zhang. 2024. What if llms have different world views: Simulating alien civilizations with llm-based agents. arXiv preprint arXiv:2402.13184.

Yutaro Yamada, Robert Tjarko Lange, Cong Lu, Shengran Hu, Chris Lu, Jakob Foerster, Jeff Clune, and David Ha. 2025. The ai scientist-v2: Workshop-level automated scientific discovery via agentic tree search. arXiv preprint arXiv:2504.08066.

Asma Yamani, Malak Baslyman, and Moataz Ahmed. 2025. Muli-agent llms as ethics advocates for ai based systems. In 2025 IEEE 33rd International Requirements Engineering Conference Workshops (REW), pages 524–532. IEEE.

Junwei Yang, Hanwen Xu, Srbuhi Mirzoyan, Tong Chen, Zixuan Liu, Zequn Liu, Wei Ju, Luchen Liu, Zhiping Xiao, Ming Zhang, et al. 2024a. Poisoning medical knowledge using large language models. Nature Machine Intelligence, 6(10):1156–1168.

Zonglin Yang, Wanhao Liu, Ben Gao, Tong Xie, Yuqiang Li, Wanli Ouyang, Soujanya Poria, Erik Cambria, and Dongzhan Zhou. 2024b. Moosechem: Large language models for rediscovering unseen chemistry scientific hypotheses. arXiv preprint arXiv:2410.07076.

Zonglin Yang, Wanhao Liu, Ben Gao, Tong Xie, Yuqiang Li, Wanli Ouyang, Soujanya Poria, Erik Cambria, and Dongzhan Zhou. 2024c. Moosechem: Large language models for rediscovering unseen chemistry scientific hypotheses. Preprint, arXiv:2410.07076.

Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Tom Griffiths, Yuan Cao, and Karthik Narasimhan. 2023a. Tree of thoughts: Deliberate problem solving with large language models. Advances in neural information processing systems, 36:11809–11822.

Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao. 2023b. React: Synergizing reasoning and acting in language models. In International Conference on Learning Representations (ICLR).

Geyan Ye, Xibao Cai, Houtim Lai, Xing Wang, Junhong Huang, Longyue Wang, Wei Liu, and Xiangxiang Zeng. 2023a. Drugassist: A large language model for molecule optimization. arXiv preprint arXiv:2401.10334.

Shaokai Ye, Jessy Lauer, Mu Zhou, Alexander Mathis, and Mackenzie Mathis. 2023b. Amadeusgpt: a natural language interface for interactive animal behavioral analysis. Advances in neural information processing systems, 36:6297–6329.

Danqing Yin, Zhongmin Zhang, Xinci Liu, Ke Ni, Huidong Su, Nicolas Lin Li, Hongyu Dong, Qiuchen Zhao, Xinyi Lin, Luyi Tian, et al. 2025. Atlasagent: Vision language model and agent-guided framework for evaluation of atlas-scale single-cell integration. bioRxiv, pages 2025–07.

Beibei Yu, Tao Shen, Hongbin Na, Ling Chen, and Denqi Li. 2024. Mineagent: Towards remote-sensing mineral exploration with multimodal large language models. arXiv preprint arXiv:2412.17339.

Ling Yue, Nithin Somasekharan, Yadi Cao, and Shaowu Pan. 2025. Foam-agent: Towards automated intelligent cfd workflows. Preprint, arXiv:2505.04997.

Ruihong Zeng, Jinyuan Fang, Siwei Liu, and Zaiqiao Meng. 2024. On the structural memory of llm agents. arXiv preprint arXiv:2412.15266.

Fan Zhang, Yalong Zhao, Weihan Zhang, and Lipeng Lai. 2025a. Bioscientist agent: Designing llmbiomedical agents with kg-augmented rl reasoning modules for drug repurposing and mechanistic of action elucidation.

Guorui Zhang, Chao Song, Liyuan Liu, Qiuyu Wang, and Chunquan Li. 2025b. Transagent: Dynamizing transcriptional regulation analysis via multi-omicsaware ai agent. bioRxiv, pages 2025–04.

Huan Zhang, Yu Song, Ziyu Hou, Santiago Miret, and Bang Liu. 2024a. HoneyComb: A flexible LLMbased agent system for materials science. In Findings of the Association for Computational Linguistics: EMNLP 2024, pages 3369–3382, Miami, Florida, USA. Association for Computational Linguistics.

Jiaxin Zhang, Zhongzhi Li, Ming-Liang Zhang, Fei Yin, Cheng-Lin Liu, and Yashar Moshfeghi. 2024b. Geoeval: Benchmark for evaluating llms and multi-modal models on geometry problem-solving. In Findings of the Association for Computational Linguistics, ACL 2024, Bangkok, Thailand and virtual meeting, August 11-16, 2024, pages 1258–1276. Association for Computational Linguistics.

Yanbo Zhang, Sumeer A Khan, Adnan Mahmud, Huck Yang, Alexander Lavin, Michael Levin, Jeremy Frey, Jared Dunnmon, James Evans, Alan Bundy, et al. 2025c. Exploring the role of large language models in the scientific method: from hypothesis to discovery. npj Artificial Intelligence, 1(1):14.

Yu Zhang, Yang Han, Shuai Chen, Ruijie Yu, Xin Zhao, Xianbin Liu, Kaipeng Zeng, Mengdi Yu, Jidong Tian, Feng Zhu, Xiaokang Yang, Yaohui Jin, and Yanyan Xu. 2025d. Large language models to accelerate organic chemistry synthesis. Preprint, arXiv:2504.18340.

Zhongyue Zhang, Zijie Qiu, Yingcheng Wu, Shuya Li, Dingyan Wang, Zhuomin Zhou, Duo An, Yuhan Chen, Yu Li, Yongbo Wang, et al. 2025e. Origene: A self-evolving virtual disease biologist automating therapeutic target discovery. bioRxiv, pages 2025– 06.

Zihan Zhao, Da Ma, Lu Chen, Liangtai Sun, Zihao Li, Yi Xia, Bo Chen, Hongshen Xu, Zichen Zhu, Su Zhu, et al. 2025. Developing chemdfm as a large language foundation model for chemistry. Cell Reports Physical Science, 6(4).

Lianhao Zhou, Hongyi Ling, Keqiang Yan, Kaiji Zhao, Xiaoning Qian, Raymundo Arróyave, Xiaofeng Qian, and Shuiwang Ji. 2025. Toward greater autonomy in materials discovery agents: Unifying

planning, physics, and scientists. arXiv preprint arXiv:2506.05616.

Kunlun Zhu, Jiaxun Zhang, Ziheng Qi, Nuoxing Shang, Zijia Liu, Peixuan Han, Yue Su, Haofei Yu, and Jiaxuan You. 2025. Safescientist: Toward risk-aware scientific discoveries by llm agents. arXiv preprint arXiv:2505.23559.

Yunheng Zou, Austin H Cheng, Abdulrahman Aldossary, Jiaru Bai, Shi Xuan Leong, Jorge Arturo Campos-Gonzalez-Angulo, Changhyeok Choi, Cher Tian Ser, Gary Tom, Andrew Wang, et al. 2025. El agente: An autonomous agent for quantum chemistry. Matter, 8(7).

