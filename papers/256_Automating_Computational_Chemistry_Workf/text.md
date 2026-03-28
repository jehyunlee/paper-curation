## arXiv:2603.25522v1[physics.chem-ph]26 Mar 2026

# Automating Computational Chemistry Workflows via OpenClaw and Domain-Specific Skills

Mingwei Ding,†,‡,†† Chen Huang,†,‡,†† Yibo Hu,†,‡ Yifan Li,¶ Zitian Lu,†,‡ Xingtai Yu,§ Duo Zhang,∥,⊥,# Wenxi Zhai,@,△ Tong Zhu,∗,@,△ Qiangqiang Gu,∗,†,‡,∇ and Jinzhe Zeng∗,†,‡,∇

†School of Artificial Intelligence and Data Science, University of Science and Technology of China, Hefei 230026, P.R. China ‡Suzhou Institute for Advanced Research, University of Science and Technology of China, Suzhou 215123, P.R. China ¶Department of Chemistry, Princeton University, Princeton, NJ 08544, USA §Division of Life Sciences and Medicine, University of Science and Technology of China, Hefei 230026, P.R. China ∥AI for Science Institute, Beijing 100080, P.R. China ⊥DP Technology, Beijing 100080, P.R. China #Academy for Advanced Interdisciplinary Studies, Peking University, Beijing 100871, P.R. China @Shanghai Engineering Research Center of Molecular Therapeutics and New Drug Development, School of Chemistry and Molecular Engineering, East China Normal University, Shanghai 200062, P.R. China △Shanghai Innovation Institute, Shanghai 200003, P.R. China ∇Suzhou Big Data & AI Research and Engineering Center, Suzhou 215123, P.R. China ††These authors contributed equally to this work.

E-mail: tzhu@lps.ecnu.edu.cn; guqq@ustc.edu.cn; jinzhe.zeng@ustc.edu.cn

###### Abstract

Automating multistep computational chemistry tasks remains challenging because reasoning, workflow specification, software execution, and high-performance computing (HPC) execution are often tightly coupled. We demonstrate a decoupled agent-skill design for computational chemistry automation leveraging OpenClaw. Specifically, OpenClaw provides centralized control and supervision; schema-defined planning skills translate scientific goals into executable task specifications;domain skills encapsulate specific computational chemistry procedures;and DPDispatcher manages job execution across heterogeneous HPC environments. In a molecular dynamics (MD) case study of methane oxidation, the system completed cross-tool execution, bounded recovery from runtime failures, and reaction network extraction, illustrating a scalable and maintainable approach to multistep computational chemistry automation.

### Introduction

Computational chemistry has become an indispensable tool for probing, predicting, and rationalizing chemical and materials systems. In practice, however, the major bottleneck is often not the lack of computational methods themselves, but the difficulty of reliably coordinating heterogeneous software tools, data representations, and execution environments for multi-step research tasks. Real applications routinely require molecular structure preparation, input generation, parameter configuration, data-format conversion, remote job submission, monitoring, error recovery, and downstream analysis across multiple codes and platforms. Because these operations are strongly interdependent, automation depends not only on executing individual tools, but also on maintaining consistency across task specification, software invocation, intermediate data handoff, and HPC execution. As such tasks become increasingly multi-step and data-intensive, the central challenge is no longer simply to automate isolated calculations, but to achieve robust, reusable, and auditable end-to-end automation.1

One major line of prior work approaches this problem through workflow-based automation. Representative examples include general workflow infrastructures such as AiiDA,2,3 FireWorks,4 and QMflows,5 as well as domain-oriented workflow systems for specific scientific tasks. In artificial intelligence (AI)-driven atomistic simulation, for example, DP-GEN6 and NepTrain7 automate active-learning cycles for machine-learning potentials; CatFlow8 and DP-TI9 support free-energy and thermodynamic-integration workflows; ChecMatE,10 AutoSteper,11 APEX,12 and RiD-kit13 provide workflow support for machine-learning-potentialbased materials and molecular simulations; and mech2d14 and maptool15 illustrate highthroughput materials-screening workflows. These systems have proven highly effective for repetitive, well-defined, and high-throughput computational tasks by formalizing task dependencies, provenance tracking, data organization, and job execution across heterogeneous computing resources. However, workflow-based automation primarily relies on predefined task graphs and execution logic. Even when limited runtime dynamism is supported, these approaches become harder to extend when tasks require cross-software adaptation, contextdependent decision making, or recovery from unforeseen runtime failures.4,16

Alongside recent workflow centric automation frameworks for scientific model construction and training, which demonstrate the value of modular tool integration and iterative execution in domain specific settings,17 large language model based agent systems have opened a new direction for scientific automation. By interleaving natural language reasoning with external tool use, intermediate state inspection, and task level replanning, these systems can adapt to evolving execution contexts in ways that are difficult to hard code in predefined workflows.18–20 Recent agent studies related to computational chemistry automation, including ChemCrow21 and CACTUS,22 suggest that large language model based systems can support computational chemistry workflows by coordinating domain tools and scientific constraints during execution.23 This emerging direction is important because it moves automation beyond fixed procedural pipelines and toward execution strategies that can respond to intermediate results, tool outputs, and changing task context.21–23

Current approaches to computational chemistry automation occupy two largely separate design regimes. Workflow systems provide explicit execution structures and, in some cases, robust scheduler integration, but they typically rely on predefined control flow and limited recovery semantics.2,4,5,16 Computational chemistry focused agentic systems provide greater runtime flexibility through dynamic reasoning and tool selection, yet workflow structure, recovery logic, tool-routing policies, and execution-environment assumptions are often embedded directly within specialized agent stacks.21,22,24 As a result, extending capability may require redesigning agent-side orchestration rather than simply replacing an executable module. These contrasts can be examined in terms of workflow explicitness, recovery model, HPC grounding, module-replacement granularity, and dependence on computational chemistry specific design. In this view, the central limitation is not insufficient reasoning capability, but engineering entanglement: the tight coupling of reasoning, workflow specification, domain execution, and infrastructure adaptation, which prevents them from being independently replaced, extended, and maintained.

More broadly, current automation systems can be viewed along a spectrum from scripted workflows, to workflows with LLM-enabled nodes, to specialized agents whose task logic is largely embedded in prompts and tool-routing policies. Across this spectrum, reusable tool access does not by itself provide task-specific execution competence: a general agent may have access to broad capabilities through runtime-loaded tools or skills, yet still require an explicit task specification for how those capabilities should be combined to achieve a concrete computational task objective. At the same time, computational chemistry places unusual pressure on software-facing execution layers, because executable substrates change frequently across software packages, file formats, and HPC environments. These considerations motivate a decoupled design in which general-purpose control is separated from computational chemistry execution. Rather than embedding domain procedures directly into a specialized agent stack, we organize automation around a general-purpose agent that handles coordination, state tracking, and decision making, while delegating concrete scientific operations

to reusable skills. In such a formulation, new domain capabilities are introduced by adding or replacing executable skills rather than redesigning the agent itself, which is especially attractive for computational chemistry.

Here, we adopt this idea in the form of an OpenClaw-grounded decoupled agent-skill design for computational chemistry automation. OpenClaw25 provides the general-purpose control and coordination mechanism; schema-defined planning skills convert scientific goals into executable task specifications; domain skills encapsulate computational chemistry procedures and software-facing operations; and DPDispatcher26 supplies a scheduler-aware execution interface for heterogeneous HPC environments. In this way, new computational chemistry capabilities can be introduced, replaced, and reused at the skill level without redesigning the agent itself.

In this work, we demonstrate this design through a case study on methane oxidation reaction exploration, adapted from a prior neural network-based molecular dynamics study of combustion chemistry.27 Starting from a natural language instruction, the system constructs an explicit task specification and carries out molecular optimization, file format conversion, initial reactive system construction, molecular dynamics simulation, HPC dispatch and monitoring, failure recovery, and trajectory analysis. This case illustrates that computational chemistry procedures can be externalized into reusable skills, providing a practical basis for computational chemistry automation. To support reuse and reproducibility, we have also released an open-source library for computational chemistry skills, covering quantum chemistry, molecular dynamics, machine-learning potentials, and molecular representation.

### Methodology and Architecture

#### Design Principles and System Organization

Our design is motivated by a simple principle: computational chemistry automation should externalize not only reusable computational procedures, but also the task-specific

logic that determines how those procedures are organized and executed. In our formulation, reusable skills provide domain operations together with usage descriptions available at runtime, while a task manifest converts a computational chemistry task description into an explicit specification of which skills to combine, in what order, and under what conditions. Under this design, the agent does not require computational chemistry specific fine tuning or a deeply specialized internal policy. Instead, domain appropriate behavior emerges from the runtime combination of a general agent, reusable skills, and task specific guidance.

We instantiate this design using OpenClaw as the general agent framework, augmented with reusable skills for task coordination and computational chemistry execution, as shown in Figure 1. Rather than constructing a specialized computational chemistry agent from scratch, we build on a general agent framework maintained by a broader software community, thereby improving software sustainability while allowing domain experts to focus on task specific capabilities. At the same time, a general agent alone is insufficient for computational chemistry automation, because it does not natively encode scheduler semantics, scientific data formats, or software-specific execution procedures. We therefore place these scientific and execution related capabilities in skills that are loaded at runtime and can be revised independently of the core agent.

To make the decoupled skill architecture practical for computational chemistry automation, the execution layer must support isolated deployment and reproducible tool invocation. Most skills in our ecosystem are therefore built around the uv toolchain. In particular, uvx invokes tools in temporary isolated environments without requiring global installation, which reduces dependency conflicts and keeps the host system clean. This allows each skill to be represented as an executable command together with its required packages, so that dependencies can be resolved at runtime while remaining modular at the skill level. Because uv also caches previously built dependencies, subsequent executions can reuse local packages, improving deployment efficiency and supporting reproducible workflow execution. Skills can further constrain tool resolution to specific packages or explicit versions, thereby improving

consistency across runs. Taken together, these features provide isolated and reproducible execution environments for skills without entangling dependency management with the core agent.

The role of skills is not to make decisions or act autonomously, but to serve as structured capability packages containing instructions, templates, and validation logic. When a request matches a skill, OpenClaw loads its content into the model context. The language model then reasons over the user goal, the current state, the loaded skills, and the execution feedback to determine the next action, which OpenClaw then executes. Tool outputs, generated files, and external program feedback are returned to this central control loop to inform the next decision step. Consequently, high level planning, HPC submission, and computational chemistry operations are all orchestrated by OpenClaw rather than performed independently by isolated modules. The skills, in turn, contribute capability descriptions and procedures that the central loop can invoke, inspect, and revise.

From this perspective, our architecture is best described as one general agent framework with an extensible skill ecosystem. Some skills focus on workflow coordination, some on execution grounding, and some on domain operations, but they all enter the system through the same mechanism of context loading, model reasoning, tool execution, and feedback. This design combines the maintainability of a general agent framework with the task specificity required for computational chemistry.

![image 1](Ding et al._2026_Automating Computational Chemistry Workflows via OpenClaw and Domain-Specific Skills_images/imageFile1.png)

- Figure 1: Architecture of the OpenClaw-based decoupled agent-skill framework for computational chemistry automation.


#### OpenClaw Control Loop and Skill Invocation

At runtime, OpenClaw maintains session context that includes the user request, tool access, and state tracking across long tasks. For each step, it first reads the current conversation state together with the outputs of previous actions. The language model then produces the next action, which may involve loading a skill that matches the current need, asking the user a question, calling a tool, generating a workflow artifact, or executing a domain-specific script. OpenClaw validates and executes that action, captures standard output, error output, generated files, and tool results, and appends them to the active context for the next turn. This loop continues until the task is completed or human intervention is required. This process is illustrated schematically in Figure 2a.

The detailed logical flow of the automated execution engine is shown in Figure 2b. Upon task initiation, the system identifies and retrieves the necessary skill sets. This is followed by a task-planning phase in which the LLM decomposes the high-level request into a series of executable jobs. During the execution stage, the system handles job submission to the remote environment and monitors its status. A key feature of this workflow is the autonomous error-recovery loop: when execution does not reach a successful state, the agent retries by

![image 2](Ding et al._2026_Automating Computational Chemistry Workflows via OpenClaw and Domain-Specific Skills_images/imageFile2.png)

- Figure 2: (a) Schematic of the LLM-based decision-making process; (b) Workflow of the automated computational task execution process.


analyzing execution logs and, if necessary, requesting user guidance to resolve the bottleneck. This cycle repeats for each sequential task within the workflow manifest until all dependencies are satisfied, ultimately generating a final summary of the research outputs.

Progressive skill loading is particularly advantageous in computational chemistry; it keeps the context window focused on the immediate task, thereby avoiding the overhead of processing documentation for every supported software package simultaneously. This modularity also facilitates system expansion, as integrating new software typically requires only adding or updating specific skills rather than modifying the core agent logic. Such decoupling motivates the adoption of a general-purpose agent framework over an architecture tailored exclusively to computational chemistry. Under this design, the core infrastructure leverages broader software maintenance and community development, while scientific expertise remains concentrated within reusable, domain-specific skills.

#### The Agent Taskboard Manifest and the DPDispatcher Skill

Two skills are especially important in our implementation. The first converts an openended computational task description into an explicit, executable workflow representation, thereby bridging the gap between broad capability access and task-specific execution competence, whereas the second grounds long-running tasks in real execution environments.

The Agent Taskboard Manifest skill addresses a key limitation of purely tool-augmented general agents. While dynamic skill loading endows the model with a wide range of executable capabilities, tool access alone does not specify how those capabilities should be ordered and combined to fulfill a concrete computational task description. In traditional dedicated agents, such task-specific execution competence is typically embedded directly in the agent through carefully engineered prompt constraints that channel the model along a fixed procedural path. To retain generality without compromising execution rigor, we instead implement workflow coordination as a specialized skill. This skill serves as a meta-prompting layer that generates task-guidance prompts and execution constraints dynamically at runtime.

Specifically, it translates the user-provided computational task description into a structured task specification that explicitly defines stages, dependencies, required inputs, expected outputs, and validation conditions. To control reasoning complexity and manage the language model context window, the resulting workflow description adopts a lazy-loading strategy in which only the currently active subtask is introduced into the agent context. This explicit and modular representation improves inspectability, facilitates state-dependent recovery, and provides a general agent with the targeted procedural constraints that are otherwise hardcoded in dedicated expert systems. Because the coordination mechanism is dynamically loaded at runtime in the same manner as other skills, it remains replaceable and can be refined without modifying the underlying OpenClaw runtime.

The DPDispatcher skill implements execution grounding. DPDispatcher, which we developed with collaborators as an open-source package, generates job scripts, submits jobs,

monitors their status, and retrieves result files across local and remote environments.26 In our framework, the corresponding skill translates agent intent into validated DPDispatcher descriptors, including machine settings, resource requests, file-transfer specifications, and task commands. This design shields the core agent from scheduler-specific syntax while still exposing the operational choices that matter for scientific execution. Through DPDispatcher, the same agent can target local shell execution, Slurm,28 the Portable Batch System (PBS),29,30 and Load Sharing Facility (LSF)31 through a unified interface. Queueing, waiting, monitoring, and result collection are therefore treated as normal workflow states rather than as ad hoc shell-side bookkeeping. This point is important in computational science, where the practical bottleneck is often not a single command, but the full life cycle of remote execution.

#### Computational Chemistry Agent Skills

Our domain capabilities are further organized as computational chemistry Agent Skills. We have released an open-source library for computational chemistry Agent Skills under the LGPL-3.0 license at https://github.com/jinzhezenggroup/computational-che mistry-agent-skills. The repository provides reusable skills for common computational chemistry operations and serves as a public starting point for community extension. A further point is that skills are not in one-to-one correspondence with software packages. A single skill may coordinate several programs for one task, and one software package may be exposed through multiple skills that target different operations or levels of abstraction. For this reason, Table 1 summarizes related software in the current repository rather than implying a one-skill-per-software mapping. At the time of writing, the repository spans agent workflow, analysis, atomistic workflows, data processing, machine-learning potentials, molecular dynamics, molecular representation, quantum chemistry, and tools. We aim for broad coverage, but the current skill set remains incomplete and should therefore be viewed as a growing ecosystem rather than a complete collection.

Table 1: Current category-level view of the skill repository. The current list is not exhaustive, and each category may contain multiple skills and software interfaces.

Category Related Software Analysis Phonopy,32 ReacNetGenerator33 Atomistic workflows ASE34 Data processing Open Babel,35 dpdata,36 Packmol,37 pymatgen38 Machine-learning potentials DeePMD-kit39,40 Molecular dynamics Amber,41,42 LAMMPS43 Molecular representation RDKit,44 Uni-Mol45 Quantum chemistry ABINIT,46 CP2K,47 DFTB+,48 Gaussian,49 GPAW,50

Quantum ESPRESSO,51,52 SIESTA,53 VASP54 Tools DPDispatcher26

### Case Study: Methane Oxidation Reactive MD Automation

To evaluate the practical feasibility of the proposed architecture for computational chemistry workflows, we apply it to a case study involving reactive molecular dynamics simulation of methane oxidation and subsequent extraction of reaction pathways from the resulting trajectories, as shown in Figure 3. This task is adapted from a prior molecular dynamics study of combustion chemistry based on a neural network potential,27 and is used here to examine whether a general agent equipped with reusable planning and domain skills can orchestrate the corresponding workflow in an explicit, traceable, and recoverable manner. The case is suitable for this purpose because it requires coordination across multiple interdependent stages, including molecular structure preparation, quantum chemical optimization, mixedsystem construction, reactive molecular dynamics simulation, and trajectory analysis, while also depending on interoperability across heterogeneous software packages and execution environments.

In this case, we submit a natural-language request to OpenClaw, with GPT-5.2 (xhigh) or GPT-5.4 (xhigh) serving as the reasoning engine. The request defines a multistep methane

oxidation workflow that includes generating isolated-molecule structures with Open Babel,35 optimizing CH4 and O2 at the B3LYP55/6–31G(d,p)56,57 level of theory, converting the optimized structures into standardized molecular files with dpdata,36 packing a bulk system containing 50 CH4 and 100 O2 molecules at a target density of 0.25 g/cm3 using Packmol,37 and generating a LAMMPS-readable data file. For the reactive molecular dynamics stage, the agent receives as external input a pretrained Deep Potential58 model for the methane oxidation system, here taken from Ref. 59, and incorporates it into LAMMPS43 through DeePMD-kit.39,40 It then performs short structural relaxation or low-temperature pre-equilibration to remove unfavorable local contacts, heats the system to 3000 K under the NVT ensemble with the Nose–Hoover thermostat, and runs a 1 ns reactive molecular dynamics simulation with a time step of 0.1 fs while recording key simulation parameters, thermodynamic outputs, and atomic trajectories. Finally, ReacNetGenerator33 analyzes the trajectory to track CH4, O2, radical intermediates, and oxidation products, and to extract the dominant methane oxidation pathways and key intermediates.

Rather than mapping this computational task description directly to a fixed procedure, the framework invokes a schema-defined task-planning skill to externalize the objective into an explicit workflow manifest. Rather than serving as a simple step list, this manifest encodes stage dependencies, completion criteria, validation conditions, and execution constraints in a form that can be interpreted at runtime. For the present case, the resulting computational workflow comprises six stages: molecular preparation, geometry optimization, file format conversion, reactive system construction, molecular dynamics simulations, and trajectory analysis. Pre-flight validation, scheduler submission, and runtime monitoring. Throughout this process, OpenClaw maintains the global task state and orchestrates the execution flow, while reusable domain skills provide the computational chemistry procedures required at each stage. As a result, execution is governed by validated intermediate outputs rather than by a fixed linear script.

![image 3](Ding et al._2026_Automating Computational Chemistry Workflows via OpenClaw and Domain-Specific Skills_images/imageFile3.png)

Figure 3: Workflow of the methane oxidation MD simulation.

Before intensive execution, the framework performs pre-flight checks on executables, dependencies, scheduler access, and required file paths, thereby reducing failures arising from environmental mismatches. Reactive MD execution is then grounded in the target HPC environment through the DPDispatcher26 skill, which translates the planned task into schedulercompatible job descriptors. In this way, the orchestration environment and the scientific execution environment remain explicitly connected while operationally separated.

During execution, task advancement is state-driven rather than purely sequential. Stage transitions occur only after the required intermediate outputs have been produced and validated. If an individual stage fails, the framework inspects the current execution state and applies stage-appropriate bounded recovery actions—such as parameter repair, retry, or rollback—before proceeding. When recovery conditions are not satisfied, execution halts, thereby preventing unbounded deviation from the intended task procedure.

We successfully executed the entire workflow in repeated end-to-end demonstrations. Owing to the inherent stochasticity of LLMs, individual runs exhibited variations in the dialogue trajectories, the generated action plans, and the specific errors encountered. In these demonstrations, the system leveraged error feedback to resolve such issues and complete the assigned tasks.

### Conclusions

This work demonstrates an OpenClaw-grounded decoupled agent–skill design for multistep computational chemistry automation. OpenClaw provides general-purpose task co-

ordination and supervision, planning skills externalize scientific goals into executable task specifications, the DPDispatcher-based submission skill grounds computation in real HPC environments, and domain skills provide software-specific procedures and result-handling logic within the agent control loop. Through the methane-oxidation reactive MD case study, we show that this framework can organize multistage computational chemistry tasks, coordinate cross-tool execution, and support bounded recovery from runtime failures without relying on a fully pre-encoded workflow. These results suggest that general-purpose agents, coupled with modular skill ecosystems, offer a scalable and maintainable path toward practical automation across computational chemistry and materials science. Future work will focus on expanding the reusable skill ecosystem to support a broader range of computational tasks—such as high-throughput materials screening, periodic solid-state computations, and active-learning potential generation—while fostering community contributions to maintain the library. Furthermore, integrating the agent with rigorous provenance-tracking databases and enabling closed-loop autonomous workflows remain important directions for scientific discovery.

### Acknowledgement

This work is supported by Advanced Materials - National Science and Technology Major Project (No. 2025ZD0618700 to J.Z.) and USTC Bihe Youth Program for Interdisciplinary Innovation (BH-202520 to C.H.). Q. G. acknowledges the support from the National Natural Science Foundation of China (Grant No. 12504285) and Natural Science Foundation of Jiangsu Province (Grant No. BK20250472). Computing resources are provided by the Supercomputing Center of University of Science and Technology of China and the Open Source Supercomputing Center of S-A-I. J.Z. thanks members of the linux.do community forum for helpful discussions on large language models and OpenClaw.

### References

- (1) Wu, T.; Sun, M.; Huang, B. A Review of Automated Workflow Pipelines for Computational Chemists. Small Methods 2025, 9, e2500308.
- (2) Pizzi, G.; Cepellotti, A.; Sabatini, R.; Marzari, N.; Kozinsky, B. AiiDA: automated interactive infrastructure and database for computational science. Comput. Mater. Sci. 2016, 111, 218–230.
- (3) Uhrin, M.; Huber, S. P.; Yu, J.; Marzari, N.; Pizzi, G. Workflows in AiiDA: Engineering a high-throughput, event-based engine for robust and modular computational workflows. Comput. Mater. Sci. 2021, 187, 110086.
- (4) Jain, A.; Ong, S. P.; Chen, W.; Medasani, B.; Qu, X.; Kocher, M.; Brafman, M.; Petretto, G.; Rignanese, G.; Hautier, G.; Gunter, D.; Persson, K. A. FireWorks: a dynamic workflow system designed for high-throughput applications. Concurr. Comput. 2015, 27, 5037–5059.
- (5) Zapata, F.; Ridder, L.; Hidding, J.; Jacob, C. R.; Infante, I.; Visscher, L. QMflows: A Tool Kit for Interoperable Parallel Workflows in Quantum Chemistry. J. Chem. Inf. Model. 2019, 59, 3191–3197.
- (6) Zhang, Y.; Wang, H.; Chen, W.; Zeng, J.; Zhang, L.; Han, W.; E, W. DP-GEN: A concurrent learning platform for the generation of reliable deep learning based potential energy models. Comput. Phys. Commun. 2020, 253, 107206.
- (7) Chen, C.; Li, Y.; Zhao, R.; Liu, Z.; Fan, Z.; Tang, G.; Wang, Z. NepTrain and NepTrainKit: Automated active learning and visualization toolkit for neuroevolution potentials. Comput. Phys. Commun. 2025, 317, 109859.
- (8) Liu, Y.-P.; Fan, Q.-Y.; Gong, F.-Q.; Cheng, J. CatFlow: An Automated Workflow for


- Training Machine Learning Potentials to Compute Free Energies in Dynamic Catalysis. J. Phys. Chem. C 2025, 129, 1089–1102.
- (9) DeepModeling DPTI. 2025; https://github.com/deepmodeling/dpti, GitHub repository. Accessed: 2026-03-23.
- (10) Guo, Y.-X.; Zhuang, Y.-B.; Shi, J.; Cheng, J. ChecMatE: A workflow package to automatically generate machine learning potentials and phase diagrams for semiconductor alloys. J. Chem. Phys. 2023, 159, 094801.
- (11) Liu, M.; Han, Y.; Cheng, Y.; Zhao, X.; Zheng, H. Exploring exohedral functionalization of fullerene with automation and Neural Network Potential. Carbon 2023, 213, 118180.
- (12) Li, Z.; Wen, T.; Zhang, Y.; Liu, X.; Zhang, C.; Pattamatta, A. S. L. S.; Gong, X.; Ye, B.; Wang, H.; Zhang, L.; Srolovitz, D. J. APEX: an automated cloud-native material property explorer. npj Comput. Mater 2025, 11, 88.
- (13) Fan, J.; Wang, Y.; Wang, D.; Zhang, L. RiD-kit: software package designed to do enhanced sampling using reinforced dynamics. BMC Methods 2025, 2, 14.
- (14) Wang, H.; Li, T.; Liu, X.; Zhu, W.; Chen, Z.; Li, Z.; Yang, J. mech2d: An Efficient Tool for High-Throughput Calculation of Mechanical Properties for Two-Dimensional Materials. Mol. (Basel Switz.) 2023, 28, 4337.
- (15) Wang, H.; Feng, Q.; Li, X.; Yang, J. High-Throughput Computational Screening for Bipolar Magnetic Semiconductors. Res. (Washington D.C.) 2022, 2022, 9857631.
- (16) Ganose, A. M. et al. Atomate2: modular workflows for materials science. Digit. Discov. 2025, 4, 1944–1973.
- (17) Chen, C.; Li, Y.; Zhao, R.; Liu, Z.; Fan, Z.; Tang, G.; Wang, Z. NepTrain and NepTrainKit: Automated Active Learning and Visualization Toolkit for Neuroevolution Potentials. arXiv 2025, 2506.01868.


- (18) Karpas, E. et al. MRKL Systems: A modular, neuro-symbolic architecture that combines large language models, external knowledge sources and discrete reasoning. arXiv 2022, 2205.00445.
- (19) Yao, S.; Zhao, J.; Yu, D.; Du, N.; Shafran, I.; Narasimhan, K.; Cao, Y. ReAct: Synergizing Reasoning and Acting in Language Models. arXiv 2023, 2210.03629.
- (20) Schick, T.; Dwivedi-Yu, J.; Dessı`, R.; Raileanu, R.; Lomeli, M.; Zettlemoyer, L.; Cancedda, N.; Scialom, T. Toolformer: Language Models Can Teach Themselves to Use Tools. arXiv 2023, 2302.04761.
- (21) M Bran, A.; Cox, S.; Schilter, O.; Baldassari, C.; White, A. D.; Schwaller, P. Augmenting large language models with chemistry tools. Nat. Mach. Intell. 2024, 6, 525–535.
- (22) McNaughton, A. D.; Sankar Ramalaxmi, G. K.; Kruel, A.; Knutson, C. R.; Varikoti, R. A.; Kumar, N. CACTUS: Chemistry Agent Connecting Tool Usage to Science. Acs Omega 2024, 9, 46563–46573.
- (23) Xiao, K.; Zhang, H.; Mao, R.; Li, H.; Chen, Z. X. Towards LLM-enabled autonomous combustion research: A literature-aware agent for self-corrective modeling workflows. arXiv 2026, 2601.01357.
- (24) Zou, Y. et al. El Agente: An autonomous agent for quantum chemistry. Matter 2025, 8, 102263.
- (25) Steinberger, P. OpenClaw. GitHub repository, 2025; https://github.com/openclaw/ openclaw, Accessed 2026-03-23.
- (26) Yuan, F. et al. DPDispatcher: Scalable HPC Task Scheduling for AI-Driven Science. J. Chem. Inf. Model. 2025, 65, 12155–12160.
- (27) Zeng, J.; Cao, L.; Xu, M.; Zhu, T.; Zhang, J. Z. H. Complex reaction processes in


- combustion unraveled by neural network- based molecular dynamics simulation. Nat. Commun. 2020, 11, 5713.
- (28) Yoo, A. B.; Jette, M. A.; Grondona, M. SLURM: Simple Linux Utility for Resource Management. In Lecture Notes in Computer Science; 2003; pp 44–60.
- (29) Jones, J. P. PBS: Portable Batch System. In Beowulf Cluster Computing with Linux; 2001; pp 369–390.
- (30) Nitzberg, B.; Schopf, J. M.; Jones, J. P. PBS Pro: Grid Computing and Scheduling Attributes. In Grid Resource Management; 2004; pp 183–190.
- (31) Zhou, S.; Zheng, X.; Wang, J.; Delisle, P. Utopia: A load sharing facility for large, heterogeneous distributed computer systems. Softw Pr. Exp 1993, 23, 1305–1336.
- (32) Togo, A.; Chaput, L.; Tadano, T.; Tanaka, I. Implementation strategies in phonopy and phono3py. J. Phys., Condens. Matter: Inst. Phys. J. 2023, 35, 353001.
- (33) Zeng, J.; Cao, L.; Chin, C.-H.; Ren, H.; Zhang, J. Z. H.; Zhu, T. ReacNetGenerator: an automatic reaction network generator for reactive molecular dynamics simulations. Phys. Chem. Chem. Phys. 2020, 22, 683–691.
- (34) Hjorth Larsen, A. et al. The atomic simulation environment–a Python library for working with atoms. J. Phys. Condens. Matter 2017, 29, 273002.
- (35) O’Boyle, N. M.; Banck, M.; James, C. A.; Morley, C.; Vandermeersch, T.; Hutchison, G. R. Open Babel: An open chemical toolbox. J Cheminform 2011, 3, 33.
- (36) Zeng, J. et al. dpdata: A Scalable Python Toolkit for Atomistic Machine Learning Data Sets. J. Chem. Inf. Model. 2025, 65, 11497–11504.
- (37) Martı´nez, L.; Andrade, R.; Birgin, E. G.; Martı´nez, J. M. PACKMOL: a package for building initial configurations for molecular dynamics simulations. J. Comput. Chem. 2009, 30, 2157–64.


- (38) Ong, S. P.; Richards, W. D.; Jain, A.; Hautier, G.; Kocher, M.; Cholia, S.; Gunter, D.; Chevrier, V. L.; Persson, K. A.; Ceder, G. Python Materials Genomics (pymatgen): A robust, open-source python library for materials analysis. Comput. Mater. Sci. 2013, 68, 314–319.
- (39) Zeng, J. et al. DeePMD-kit v2: A software package for deep potential models. J. Chem. Phys. 2023, 159, 054801.
- (40) Zeng, J. et al. DeePMD-kit v3: A Multiple-Backend Framework for Machine Learning Potentials. J. Chem. Theory Comput. 2025, 21, 4375–4385.
- (41) Case, D. A. et al. AmberTools. J. Chem. Inf. Model. 2023, 63, 6183–6191.
- (42) Case, D. A. et al. Recent Developments in Amber Biomolecular Simulations. J. Chem. Inf. Model. 2025, 65, 7835–7843.
- (43) Thompson, A. P.; Aktulga, H. M.; Berger, R.; Bolintineanu, D. S.; Brown, W. M.; Crozier, P. S.; in ’t Veld, P. J.; Kohlmeyer, A.; Moore, S. G.; Nguyen, T. D.; Shan, R.; Stevens, M. J.; Tranchida, J.; Trott, C.; Plimpton, S. J. LAMMPS - a flexible simulation tool for particle-based materials modeling at the atomic, meso, and continuum scales. Comput. Phys. Commun. 2022, 271, 108171.
- (44) http://www.rdkit.org RDKit: Open-source cheminformatics.
- (45) Zhou, G.; Gao, Z.; Ding, Q.; Zheng, H.; Xu, H.; Wei, Z.; Zhang, L.; Ke, G. UniMol: A Universal 3D Molecular Representation Learning Framework. The Eleventh International Conference on Learning Representations. 2023.
- (46) Verstraete, M. J. et al. Abinit 2025: New capabilities for the predictive modeling of solids and nanomaterials. J. Chem. Phys. 2025, 163, 164126.
- (47) Ku¨hne, T. D. et al. CP2K: An electronic structure and molecular dynamics software


- package - Quickstep: Efficient and accurate electronic structure calculations. J. Chem. Phys. 2020, 152, 194103.
- (48) Hourahine, B. et al. DFTB+, a software package for efficient approximate density functional theory based atomistic simulations. J. Chem. Phys. 2020, 152, 124101.
- (49) Frisch, M. J. et al. Gaussian 16 Revision A.03. 2016; Gaussian Inc. Wallingford CT.
- (50) Mortensen, J. J. et al. GPAW: An open Python package for electronic structure calculations. J. Chem. Phys. 2024, 160, 092503.
- (51) Giannozzi, P. et al. QUANTUM ESPRESSO: a modular and open-source software project for quantum simulations of materials. J. Phys., Condens. Matter: Inst. Phys. J. 2009, 21, 395502.
- (52) Giannozzi, P. et al. Advanced capabilities for materials modelling with Quantum ESPRESSO. J. Phys., Condens. Matter: Inst. Phys. J. 2017, 29, 465901.
- (53) Garcı´a, A. et al. Siesta: Recent developments and applications. J. Chem. Phys. 2020, 152, 204108.
- (54) Kresse, G.; Hafner, J. Ab initiomolecular dynamics for liquid metals. Phys. Rev. B 1993, 47, 558–561.
- (55) Stephens, P. J.; Devlin, F. J.; Chabalowski, C. F.; Frisch, M. J. Ab Initio Calculation of Vibrational Absorption and Circular Dichroism Spectra Using Density Functional Force Fields. J. Phys. Chem. 1994, 98, 11623–11627.
- (56) Hehre, W. J.; Ditchfield, R.; Pople, J. A. Self—Consistent Molecular Orbital Methods. XII. Further Extensions of Gaussian—Type Basis Sets for Use in Molecular Orbital Studies of Organic Molecules. J. Chem. Phys. 1972, 56, 2257–2261.
- (57) Hariharan, P. C.; Pople, J. A. The influence of polarization functions on molecular orbital hydrogenation energies. Theor., Chim, Acta 1973, 28, 213–222.


- (58) Zhang, L.; Han, J.; Wang, H.; Saidi, W.; Car, R.; E, W. End-to-end Symmetry Preserving Inter-atomic Potential Energy Model for Finite and Extended Systems. In Advances in Neural Information Processing Systems 31; Bengio, S., Wallach, H., Larochelle, H., Grauman, K., Cesa-Bianchi, N., Garnett, R., Eds.; Curran Associates, Inc., 2018; pp 4436–4446.
- (59) Zeng, J.; Cao, L.; Zhu, T. Neural network potentials. In Quantum Chemistry in the Age of Machine Learning; 2023; pp 279–294.


