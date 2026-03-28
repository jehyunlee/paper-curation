# arXiv:2510.09901v1[cs.AI]10 Oct 2025

## Autonomous Agents for Scientific Discovery: Orchestrating Scientists, Language, Code, and Physics

Lianhao Zhou1 Hongyi Ling1 Cong Fu1 Yepeng Huang2 Michael Sun3 Wendi Yu1 Xiaoxuan Wang4 Xiner Li1 Xingyu Su1 Junkai Zhang4 Xiusi Chen5 Chenxing Liang1

Xiaofeng Qian6,7,8 Heng Ji5 Wei Wang4 Marinka Zitnik2 Shuiwang Ji1,6,9∗

1Department of Computer Science and Engineering, Texas A&M University 2Department of Biomedical Informatics, Harvard Medical School 3Computer Science and Artificial Intelligence Laboratory, Massachusetts Institute of Technology 4Department of Computer Science, University of California, Los Angeles 5Siebel School of Computing and Data Science, University of Illinois Urbana Champaign

- 6Department of Materials Science and Engineering, Texas A&M University
- 7Department of Electrical and Computer Engineering, Texas A&M University 8Department of Physics and Astronomy, Texas A&M University


9J. Mike Walker ’66 Department of Mechanical Engineering, Texas A&M University

###### Abstract

Computing has long served as a cornerstone of scientific discovery. Recently, a paradigm shift has emerged with the rise of large language models (LLMs), introducing autonomous systems, referred to as agents, that accelerate discovery across varying levels of autonomy. These language agents provide a flexible and versatile framework that orchestrates interactions with human scientists, natural language, computer language and code, and physics. This paper presents our view and vision of LLM-based scientific agents and their growing role in transforming the scientific discovery lifecycle, from hypothesis discovery, experimental design and execution, to result analysis and refinement. We critically examine current methodologies, emphasizing key innovations, practical achievements, and outstanding limitations. Additionally, we identify open research challenges and outline promising directions for building more robust, generalizable, and adaptive scientific agents. Our analysis highlights the transformative potential of autonomous agents to accelerate scientific discovery across diverse domains.

###### 1 Introduction

Scientific discovery is fundamental to advancing human knowledge, driving innovations across diverse fields such as biology, chemistry, physics, and materials science, etc. [Zhang et al., 2025a, Wang et al., 2023a]. The pivotal role of computing in advancing discoveries across the natural sciences has long been recognized [Dirac, 1929], with impacts ranging from quantum mechanics [Landau and Lifshitz, 2013a, Tong, 2025a] to fluid dynamics [Landau and Lifshitz, 2013b, Tong, 2025b]. For many years, the process of scientific discovery has been predominantly dependent on human intuition, expertise, and iterative experimentation [Xu et al., 2023]. Nevertheless, human-driven discovery processes sometimes face challenges, including high costs, substantial time investments, potential cognitive biases, and limitations in exploring vast hypothesis spaces or complex data interactions systematically [Kitano, 2021]. Additionally, the increasing complexity and volume of data generated

∗Correspondence to: Shuiwang Ji <sji@tamu.edu>

Preprint.

in modern research demand novel approaches to efficiently analyze and interpret such extensive raw information [Miolane, 2025, Chitturi et al., 2024].

To mitigate these limitations, scientific agents have been developed to automate and accelerate critical aspects of scientific discovery [Gridach et al., 2025a]. Such agents are designed to systematically handle experimentation, hypothesis formulation, data acquisition, analysis, and interpretation, thereby potentially enhancing research efficiency and reducing human-induced errors or biases. Computational agents promise greater scalability and consistency in scientific exploration, opening doors to novel discoveries that might otherwise remain obscured [Szymanski et al., 2023, Ghafarollahi and Buehler, 2024a, Liu et al., 2024a, Chen et al., 2023a, Gottweis et al., 2025a].

Early computational scientific agents were often designed for specific, narrowly focused tasks, lacking the adaptability required to generalize across varying research areas or to handle unforeseen challenges [Beeler et al., 2024, Maurizi et al., 2024, Rajak et al., 2021, Dressler et al., 2018, Liang and Zhong, 2020]. These systems were effective for well-defined problems but were not equipped to engage in the broader, more flexible processes of scientific exploration. The need for a more adaptive and powerful approach was clear.

Recent breakthroughs in in large language models (LLMs) offer potential for scientific discovery by introducing unprecedented capabilities in reasoning, planning, and handling complex, multimodal contexts. After being trained on vast amounts of textual data, LLMs provide a unified framework capable of understanding and orchestrating diverse languages, including natural language, computer language, and even physical information (e.g. symbolic representations of physical phenomena) [Luo

- et al., 2022, Dunn et al., 2024, Huang et al., 2024a]. The integrative power of LLMs allows them to reason over scientific data in multiple modalities [Edwards et al., 2025], seamlessly interact with humans, computational tools, and physical instruments alike, fostering more intuitive, flexible, and efficient workflows in scientific discovery. For example, Zhang et al. [2024a] systematically reviews more than 260 scientific LLMs across general science, mathematics, physics, chemistry, materials science, biology, medicine, and geoscience. It introduces how LLMs are being used to augment the scientific discovery process. Reddy and Shojaee [2025] argues that, while LLMs excel at specific scientific tasks, integrated systems capable of supporting the full autonomous scientific discovery cycle are still lacking.


Fueled by advances in LLMs, research on scientific agents has grown rapidly, pointing toward a more autonomous paradigm for scientific discovery. This approach fully leverages the various capabilities of LLMs at every stage of the scientific discovery cycle. While several surveys provide broad overviews of general-purpose LLM agents [Wang et al., 2024a, Guo et al., 2024, Mialon et al., 2023], only a few have focused specifically on their roles in scientific research [Gao et al., 2024, Ren et al., 2025, Wei et al., 2025a, Zhang et al., Zheng et al., 2025, Luo et al., 2025a]. Gao et al. [2024] posits AI agents as the next frontier in scientific discovery, proposing a framework of autonomy levels based on their degree of participation in the scientific process. It introduces the core modules of agents that enable them to learn, plan, and engage in the scientific process. Ren et al. [2025] discusses related work on scientific agents by focusing on the different implementation methods for each of the core modules of agents. Wei et al. [2025a] primarily focuses the correspondence between different stages of the scientific discovery cycle and the capabilities of LLM agents. It organizes relevant scientific discovery tasks and agent-based research by four major fields, including life sciences, chemistry, physics, and materials science. Luo et al. [2025a] extends scientific research to include aspects such as paper writing and peer review. Zheng et al. [2025] proposes a similar framework of agent levels and stages of scientific discovery to previous works Gao et al. [2024], Wei et al. [2025a]. Moving beyond individual agents, Zhang et al. argues that multi-agent systems can achieve a collective intelligence that surpasses the capabilities of a single agent by emulating the collaborative dynamics of human research teams. The work also details the advantages, limitations, and future directions of multi-agent systems in multiple stages of scientific discovery.

Here, our work systematically examines how LLM-based agents operate across key stages of scientific discovery, including hypothesis discovery, experimental design and execution, and result analysis and refinement. Figure1 provides an overview of the three-phase workflow for AI-driven scientific discovery. We highlight the unique strengths of LLMs in enabling more adaptive, flexible, and capable scientific agents compared to traditional computational approaches. Furthermore, we critically assess existing methodologies, underscoring both their practical achievements and prevailing limitations. We develop a taxonomy of the methods used by scientific agents in each phase of scientific discovery

Phase 1: Hypothesis Discovery

Human Proposes High-Level Goal / Problem

Hypothesis Screening & Validation

Knowledge Extraction

Hypothesis Generation

Experimental Design

- Phase 2: Experimental Design & Execution
- Phase 3: Result Analysis & Refinement


Tool Use : AI generates code to call existing tools

Existing Tool Library (Simulators, Databases,Robots)

No

Detailed

New Tool Workﬂow Yes Needed?

Tool Creation : AI generates code for

New Scientiﬁc Tool /Algorithm

new algorithms/tools

Experimental Data

Automatic Self-Correction

![image 1](Zhou et al._2025_Autonomous Agents for Scientific Discovery Orchestrating Scientists, Language, Code, and Physics_images/imageFile1.png)

![image 2](Zhou et al._2025_Autonomous Agents for Scientific Discovery Orchestrating Scientists, Language, Code, and Physics_images/imageFile2.png)

| | | |
|---|---|---|
| | | |


Refinement

![image 3](Zhou et al._2025_Autonomous Agents for Scientific Discovery Orchestrating Scientists, Language, Code, and Physics_images/imageFile3.png)

External Evaluation &Feedback

Results Analysis

Loop Validated Findings

Human-in-the-Loop

- Figure 1: An overview of the three-phase workflow for AI-driven scientific discovery. The process begins with Phase 1: Hypothesis Discovery, where a high-level human goal is transformed through knowledge extraction and hypothesis generation into novel, verifiable scientific questions. In Phase 2: Experimental Design & Execution, these hypotheses are translated into detailed workflows which the agent executes by either using existing tools or creating new scientific tools to generate experimental data. Finally, Phase 3: Result Analysis & Refinement involves interpreting the data and entering an iterative refinement loop to progressively improve the process and arrive at validated findings.


and categorize the applications and achievements of scientific agents by domains (Figure 2). Finally, we identify open challenges and outline future research directions to advance the development of robust, generalizable, and highly adaptive LLM-driven scientific agents.

###### 2 Overview of Autonomous Agents for Scientific Discovery

###### 2.1 Overview of Scientific Discovery

To understand how LLM agents transform scientific discovery, we first revisit how scientific processes are typically structured across domains. Scientific discovery is the systematic pursuit of understanding and generating new knowledge or verifying hypotheses within scientific domains. It involves identifying meaningful questions, formulating hypotheses [Wang et al., 2024d], generating experiment procedures [Zhong et al., 2024], conducting experiments, and refining results iteratively to enhance understanding or achieve practical outcomes. While objectives differ across fields, such as identifying stable crystal structures in materials science, elucidating genetic mechanisms in biology, or systematically synthesizing therapeutic compounds in pharmacology, the discovery process shares common core components and phases across disciplines. We conceptualize the scientific discovery processes into three phases.

Hypothesis Discovery. This initial phase is a crucial creative process with the core objective of identifying and forming novel, verifiable scientific hypotheses from vast amounts of data and existing knowledge. It aims to accelerate the pace of discovery by revealing hidden connections that are difficult for human researchers to find on their own. A complete hypothesis discovery workflow is typically composed of three key stages, including Knowledge Extraction, Hypothesis Generation, and Hypothesis Screening and Validation. The goal is to systematically identify meaningful questions and formulate hypotheses that can be tested in subsequent stages.

###### Hypothesis Discovery

e.g., BioBERT [Lee et al., 2020], BioGPT [Luo et al., 2022], Galactica [Taylor et al., 2022], ether0 [Narayanan et al., 2025],ChemDFM [Zhao et al., 2025],LPMs [Barman et al., 2025]

Scientific Foundation Models

e.g., CLADD [Lee et al., 2025], CASSIA [Xie et al., 2024],FRAG [Gao et al., 2025a],CLEAR [Lopez et al., 2025]

###### Knowledge Extraction

RAG-based

e.g., ChemMiner [Chen et al., 2024a], ChartAssistant [Meng et al., 2024], GPT-4o [Hurst et al., 2024],MatViX [Khalighinejad et al., 2024],nanoMINER Odobesku et al. [2025]

Multimodal Knowledge Extraction

e.g., Biomedicine [Qi et al., 2023], General Science [Xiong et al., 2025] e.g., KG-CoI [Xiong et al., 2024], ResearchLink [Borrego et al., 2025] e.g., AI co-scientist [Gottweis et al., 2025a], ACCELMAT [Kumbhar et al., 2025a], VIRSCI [Su et al., 2024], AstroAgents [Saeedi et al., 2025] e.g., MOOSE-Chem [Yang et al., 2025], HypoAgents [Duan et al., 2025], MolLEO [Wang et al., 2024b]

Prompt-Based Knowledge-Grounded Multi-Agent Evolutionary AlgorithmBased

Hypothesis Generation

e.g., POPPER [Huang et al., 2025a], SCIMON [Wang et al., 2024c], MATDESIGN [Kumbhar et al., 2025b], HypoBench [Liu et al., 2025a], Logitbased Calibrated Prior [Gong and Fernandez, 2025]

Metric-Based Screening

Hypothesis Screening & Validation

e.g., ResearchAgent [Baek et al., 2024], Scientific Generative Agent (SGA) [Ma et al., 2024]

Agent-Based Validation

###### Experimental Design & Execution

e.g., Biomni [Huang et al., 2025b], TxAgent [Gao et al., 2025b], ChemistX [Chen et al., 2023a], CLADD [Lee et al., 2025]

RAG-based Planning

e.g., CRISPR-GPT [Qu et al., 2025], AI co-scientist [Gottweis et al., 2025a], Virtual Lab [Swanson et al., 2024]

Human High-Level Guidance

###### Experimental Design

e.g., k-agents [Cao et al., 2024], CRISPR-GPT [Qu et al., 2025], PerTurboAgent [Hao et al., 2025]

Templates & Predefined Actions

e.g., ChemToolAgent [Yu et al., 2024a], BioInformatics Agent [Xin et al.,

- 2024], BioDiscoveryAgent [Roohani et al., 2024], OSDA Agent [Hu et al.,
- 2025]


Post-Execution Feedback

e.g., OSDA Agent [Hu et al., 2025], LLMatDesign [Jia et al., 2024], MatLLMSearch [Gan et al., 2025], scBaseCount [Youngblut et al., 2025], Chemist-X [Chen et al., 2023a]

Embedded

e.g., AgentMD [Jin et al., 2024a], ChemCrow [M. Bran et al., 2024], scAgent [Mao et al., 2025], TxAgent [Gao et al., 2025b], GIS Copilot [Akinboyewa et al., 2025], SciToolAgent [Chen et al., 2025a]

Toolbox-Based

###### Tool Use

e.g., ChemToolAgent [Yu et al., 2024b], Biomni [Huang et al., 2025b], PerTurboAgent [Hao et al., 2025]

Reflective & Iterative

e.g., TAIS [Liu et al., 2024a], MedAgents [Tang et al., 2023], ChemAgents [Song et al., 2025], AtomAgent [Ghafarollahi and Buehler, 2024b], ProtAgents [Ghafarollahi and Buehler, 2024a], ChatGPT Research Group [Zheng et al., 2023], Virtual Lab [Swanson et al., 2024], kagents [Cao et al., 2024]

Hierarchical in MAS

e.g., ToolUniverse [Gao et al., 2025c], MAPPS [Zhou et al., 2025a], CodePDE [Li et al., 2025a], AlphaETool Creation volve [Novikov et al., 2025], TOOLMAKER [Wölflein et al., 2025], ShinkaEvolve Lange et al. [2025]

###### Result Analysis & Refinement

e.g., The AI Scientist-v2 [Yamada et al., 2025], PlotGen [Luo et al., 2024], ChartLlama [Han et al., 2023], ChartAssisstant [Meng et al., 2024]

Modality-Driven

e.g., ChemCrow [Bran et al., 2023], Coscientist [Boiko et al., 2023], Virtual Lab [Boeck et al., 2023]

###### Result Analysis

Tool-Augmented

e.g., Data Interpreter [Hong et al., 2024], LLM-SR [Kamienny et al., 2024], MOBLLM [Binbas et al., 2024]

Computation-Native

e.g., Self-Refine [Madaan et al., 2023], ChemAgent [Tang et al., 2025], SpatialAgent [Wang et al., 2025a], TAIS [Liu et al., 2024a], BioInformatics Agent [Xin et al., 2024]

Automatic Self-correction

###### Iterative Validation & Refinement

e.g., CRITIC [Gou et al., 2023], OSDA Agent [Hu et al., 2025], AI coscientist [Gottweis et al., 2025a], BioDiscoveryAgent [Roohani et al., 2024], SAMPLE [Rapp et al., 2024], Biomni [Huang et al., 2025b]

External Evaluation & Feedback

e.g., AI co-scientist [Gottweis et al., 2025a], ResearchAgent [Baek et al., 2024], MAPPS [Zhou et al., 2025a]

Human-in-the-Loop

###### Domain-Specific Scientific Agents

e.g., SpatialAgent [Wang et al., 2025a], TAIS [Liu et al., 2024a], CRISPR-GPT [Qu et al., 2025], BioDiscoveryAgent [Roohani et al., 2024], PerTurboAgent [Hao et al., 2025], BioAgents [Mehandru et al., 2025], BIA [Xin et al., 2024], scBaseCount [Youngblut et al., 2025], CellAgent [Xiao et al., 2024], CompBioAgent [Zhang et al., 2025b], scAgent [Mao et al., 2025], CASSIA [Xie et al., 2024]

Genomics

e.g., SAMPLE [Rapp et al., 2024], Virtual Lab [Swanson et al., 2024], ProtAgents [Ghafarollahi and Buehler,

- 2024a], Sparks [Ghafarollahi and Buehler, 2025], VibeGen [Ni and Buehler, 2025], AutoProteinEngine (AutoPE) [Liu et al., 2024b], ProChat [Huang et al., 2024b]

e.g., Biomni [Huang et al., 2025b], AI co-scientist [Gottweis et al., 2025b], TxAgent [Gao et al., 2025b],

BioResearcher [Luo et al., 2025b], STELLA [Jin et al., 2025a], CLADD [Lee et al., 2025], DrugAgent [Liu et al., 2024c], PharmAgents [Gao et al., 2025d], LIDDiA [Averly et al., 2025], AgentMD [Jin et al., 2024a], MedAgents [Tang et al., 2023], ClinicalGPT [Wang et al., 2023b], BehaveAgent [Aljovic et al., 2025]

e.g., Coscientist [Boiko et al., 2023], ChemCrow [M. Bran et al., 2024], ChemAgents [Song et al., 2025],

ChemReasoner [Sprueill et al., 2024], CACTUS [McNaughton et al., 2024], Chemist-X [Chen et al., 2023a], El Agente Q [Zou et al., 2025], LLM-RDF [Ruan et al., 2024], FROGENT [Pan et al., 2025], LARC [Baker et al.,

- 2025], FMG [Sun et al., 2025], MOOSE-Chem [Yang et al., 2024] e.g., A-Lab [Szymanski et al., 2023], ChatMOF [Kang and Kim, 2024], ChatGPT Research Group [Zheng


Protein

Medicine

Chemistry

- et al., 2023], MDAgent [Shi et al., 2025], HoneyComb [Zhang et al., 2024b], LLMatDesign [Jia et al., 2024], MatAgent [Bazgir et al., 2025a], MatSciAgent [Chaudhari et al., 2025], MatPilot [Ni et al., 2024], Materials Laws Multi-Agent Framework [Hu et al., 2024]

e.g., k-agents [Cao et al., 2024], AtomAgents [Ghafarollahi and Buehler, 2024c], Mephisto [Sun et al., 2024], QCopilot [Sha et al., 2025], OpenFOAMGPT [Pandey et al., 2025], MetaOpenFOAM [Chen et al., 2024b], AI-Scientist Framework [Xu et al., 2025a]

e.g., Autonomous GIS Agent [Ning et al., 2025], GIS Copilot [Akinboyewa et al., 2025], LP-COMDA [Liu

- et al., 2024d], ReAct agent for gas turbines [Song et al., 2024]


Materials

Physics

Others

- Figure 2: A comprehensive overview of the role of LLM-based agents in the scientific discovery lifecycle alongside a diverse collection of domain-specific scientific agents that organize various research systems and papers across fields such as Genomics, Protein, Medicine, Chemistry, Materials, Physics, and Others.


Experimental Design and Execution. Following hypothesis discovery, experimental design is a critical step that involves creating a structured plan to systematically test ideas and achieve research objectives. This process is a form of workflow generation where high-level scientific goals are translated into concrete, executable protocols. The execution stage serves as the crucial bridge that transforms abstract strategies into concrete actions and empirical evidence needed for generating insights. It involves complex tasks such as orchestrating computational resources, managing large datasets, interfacing with laboratory instruments or simulators, and continuously monitoring the workflow. It’s important to clarify that our definition of experiments includes both traditional wetlab experiments and computational simulations. While both are integral to the scientific process, current LLM-based scientific agents predominantly operate in the computational domain, focusing on simulation-based discovery. LLM-based agents accomplish this primarily through two interconnected capabilities, namely tool use and tool creation.

Result Analysis and Refinement. This phase begins with the analysis of experimental results, where autonomous agents interpret raw outputs to derive meaningful scientific insights. Since scientific discovery rarely concludes after a single iteration, this stage functions as a crucial iterative mechanism. It involves cycles of reviewing validated results, identifying discrepancies or unexpected findings, and then methodically refining the proposed hypotheses, experimental design, or computational tools to progressively enhance scientific outcomes.

Collectively, these stages encapsulate the iterative and cyclical nature of scientific inquiry, continuously refining and verifying insights to produce credible and innovative scientific knowledge.

###### 2.2 Overview of Scientific Agents

A scientific agent is a specialized AI system designed to simulate and autonomously execute aspects of the scientific research process. Unlike general-purpose LLM agents [OpenAI, 2023, Google, 2024, Anthropic, 2024], which are built for a wide array of tasks like conversation and text generation, scientific agents are highly domain-specific and task-oriented. Their primary goal is to accelerate scientific discovery by automating and augmenting the capabilities of human researchers, thereby allowing the navigation of the intricate landscape of modern science with greater speed and efficiency. Table 1 summarizes the key differences between scientific agents and general-purpose LLM agents.

Table 1: Comparison of Scientific AI Agents and General LLM Agents

|Feature|Scientific Agent|General LLM Agent|
|---|---|---|
|Primary Objective|To solve specific, complex scientific problems and generate new knowledge.|To understand and respond to a wide range of general user queries and commands.|
|Knowledge Base|Deeply integrated with specialized scientific databases, literature, and models.|Relies on broad, general knowledge acquired from vast, diverse training data.|
|Reasoning|Employs rigorous, multi-step logical deduction and inference based on scientific principles.|Utilizes common sense, associative, and heuristic reasoning for broad tasks.|
|Tool Use|Natively uses highly specialized software (e.g. simulators) and hardware (e.g. robots).|Interacts with general-purpose tools like web search engines and code interpreters.|
|Memory|Utilizes memory to accumulate domain knowledge and learn from experimental outcomes.|Memory is primarily used for maintaining conversational context and user preferences.|
|Evaluation Metrics|Success is measured by the accuracy, reproducibility, and novelty of the scientific results.|Success is measured by task completion, user satisfaction, and conversational quality.|


Reasoning and Planning. The core cognitive functions of an LLM-based scientific agent are its advanced reasoning and planning abilities, which serve as its intellectual engine. Its reasoning capabilities allow it to sift through vast amount of scientific literature and data to formulate novel hypotheses, identify patterns, and draw logical inferences [Ferrag et al., 2025, Zhang et al., 2024c]. This is coupled with a sophisticated planning module that can decompose a high-level research goal into a coherent sequence of actionable steps [Wei et al., 2025b, Huang et al., 2024c].

Tool Use. A defining characteristic of LLM-based scientific agents is their deep integration with a wide array of specialized tools [Jin et al., 2024b, Shen, 2024]. This capability serves as the bridge between the agent’s cognitive processes and the practical execution of research. These tools are not limited to software, such as domain-specific simulators, data analysis packages, and proprietary knowledge bases, but also extend to physical hardware. Through programmatic interfaces, scientific agents can operate laboratory automation systems, control sensor arrays, and manage other instrumentation, allowing them to directly interact with and conduct experiments in the physical world [Boiko et al., 2023].

Memory. An LLM-based scientific agent’s memory mechanism is fundamental to its capacity for sustained research and cumulative learning [Xu et al., 2025b, Wu et al., 2025]. Acting as both a working memory for immediate tasks and a persistent knowledge base, it archives all past outcomes. By retaining successful protocols and failed inquiries, this long-term memory enables the agent to learn from experience. This ability to continuously reference its own history allows the agent to refine strategies, avoid repeating errors, and systematically drive the process of scientific discovery forward.

- 2.3 An Information-Theoretic Framework for Autonomous Scientific Discovery


- 2.3.1 Properties of Information in Autonomous Scientific Discovery


The transition from human-led research to autonomous scientific discovery can be understood through a formal analytical framework. The core of this framework is to examine three key aspects of the information processed by an intelligent agent in the scientific workflow. First, we view scientific discovery as an inherently dissipative process, characterized by uncertainty and the need for extensive trial-and-error exploration. Second, we use the mathematical measure of Information Entropy to quantify the root of this uncertainty. Finally, we examine Verifiability, which measures whether information can be tested against objective standards and is the ultimate goal of the research process.

Information Entropy is a mathematical measure from information theory that quantifies the uncertainty or the size of the hypothesis space of a given problem. A high-entropy state, such as the

Human Intent

Natural Language

Computer Language

###### V

e

r

i

ﬁ

- a
- b


y

- n

t

r

- o
- p


i

l

i

###### t

###### y

Physical Information

E

- Figure 3: An information-theoretic framework for autonomous scientific discovery, illustrating the inverse relationship between Information Entropy and Verifiability.


set of all possible scientific hypotheses, presents a vast and unstructured search space for an agent. A core task for the agent is therefore to perform Entropy Reduction—to systematically reduce the uncertainty of the problem through its operations [Yao, 2003]. Our notion of reducing information entropy is consistent with the Second Law of Thermodynamics, which states that the total entropy of an isolated system can never decrease [Borgnakke, 2024, Schroeder, 2020]. For an agent to achieve Information Entropy Reduction in scientific discovery, the system must be an open system, instead of an isolated one. This systematic decrease in internal informational uncertainty is driven by the necessary exchange of information with the physical world. The agent’s internal entropy reduction is fundamentally dependent on interactions with the physical world. The information required to constrain the hypothesis space cannot be generated internally. Instead, it must be obtained from real-world processes (e.g., performing experiments or analyzing raw data that originates from physical processes) to constrain uncertainty.

Verifiability is a property of a specific information object that measures its ability to be objectively tested against a formal, logical, or empirical standard [Patterson, 1978]. The ultimate goal of the scientific process is to transform an initial idea with low verifiability into an empirical fact with very high verifiability. The agent’s workflow, therefore, is also a process of progressively imparting verifiability to information.

Dissipation refers to the unavoidable computational cost and effort expended on unproductive paths during the exploration of a problem space. This cost encompasses the resources consumed in the formulation, execution, and verification of incorrect hypotheses and experiments that ultimately do not lead to a solution. In thermodynamics, a dissipative process is defined by the irreversible conversion of usable forms of energy (such as mechanical, electrical, or chemical) into unusable thermal energy [Borgnakke, 2024, Schroeder, 2020]. Landauer [Landauer, 1961] extended this concept into the Physics of Information. The Landauer’s Principle dictates that any irreversible information operation must be accompanied by a minimum energy dissipation. The dissipation defined here is an inherent and unavoidable cost in scientific discovery. The process of navigating a high-entropy space where the agent moves from many uncertain potential solutions to a single determined solution is necessarily dissipative, because this transition constitutes an irreversible information operation. According to Landauer’s Principle, the degree of dissipation is directly proportional to the number of non-solution paths that must be explored and subsequently discarded to find a valid one. This trial-and-error cost is a fundamental challenge in scientific discovery.

##### L

- s
- t


a

n

i

t

g

n

#### u

### e

Su m

###### a g e

i

c

c

iﬁ

e

t

Findings Guid

r

S

maries,

n

- t
- u


e

a

ci

er

S

Goal,

Lit

ted

,

Fee dba ck

s

ns

e

a

s

ul

a

e

l

m

P

h

ance,

t

r

h

po

o

c

F

ar

Hy

e

es

R

s

w

,

A

a

n

E xecut abl e

a

t

g

o

a

L

e

i

t

D

n

a

Progra F m u

,

r

t

- d

g

- e


- s
- t


O

w

e

r

c

h

a

R

owle

T oo l I n t er f a ce &

l

enta

n

K

nctio na li t i e s

lts

m

peri

esu

P h y s i c s

- d
- e


x

R

E

o

C

- Figure 4: An overview of autonomous agents for scientific discovery in which an agent orchestrates scientists, language, code, and physics. This figure illustrates the dynamic, closed-loop workflow of an LLM-based scientific agent as the coordinator orchestrating four key components, including scientists, language, code, and physics. The agent continuously interacts with human scientists, receiving goals, guidance, and feedback to direct research, and providing summaries and findings. Its interaction with language involves extracting knowledge from literature to formulate verifiable hypotheses and detailed research plans. The agent’s interface with code translates high-level plans into executable programs for simulations or instrument control by integrating tool functionalities. Finally, it interacts with physics by using raw data and laws to direct physical or simulated instruments, yielding experimental results. This cycle represents an iterative and autonomous discovery cycle, bridging human intent to empirical evidence.


Using these properties as an analytical lens, we can systematically analyze the transformation of different types of information as they flow through the autonomous discovery process.

###### 2.3.2 A Taxonomy of Information in Autonomous Scientific Discovery

In autonomous scientific discovery, information transforms through a hierarchical process, moving from high-entropy human intent to low-entropy, verifiable physical information. Figure 3 illustrates a series of transitions: from abstract Human Intent to structured Natural Language, then to formal Computer Language, and finally to verifiable Physical Information. Each step reduces entropy by resolving ambiguity and increases verifiability by making the information more precise and testable against reality. 4 illustrates the dynamic, closed-loop workflow of an LLM-based scientific agent as the coordinator orchestrating four other key components, including Scientists, Language, Code, and Physics. These four components serve as concrete instantiations of the four corresponding information levels: Human Intent, Natural Language, Computer Language, and Physical Information.

Human Intent serves as the origin point of the scientific process. It exists as an abstract hypothesis or goal within a vast, unstructured conceptual space. This state possesses the highest possible

Table 2: Information Analysis Across Autonomous Scientific Discovery Phases

|Scientific Phase|Human Intent|Natural Language|Computer Language|Physical Information|Overall Dissipation|
|---|---|---|---|---|---|
|Hypothesis Discovery|Very High Entropy<br><br>The intent is abstract and completely openended (e.g., "discover a novel research gap").|Very High Entropy<br><br>Requires the highest level of linguistic creativity to synthesize disparate concepts and articulate new ideas.|Medium Entropy<br><br>Primarily used for auxiliary tasks like knowledge graph construction or data mining, not the core creative act.|High Entropy<br><br>Historical data serves as inspiration; the volume is vast, unstructured, and the valuable signals are nonobvious.|High<br><br>Requires overcoming high entropy in creative thought, making it difficult to automate.|
|Experimental Design|High Entropy<br><br>The intent is creative and requires navigating a vast space of possibilities (e.g., "design a new experiment").|Medium Entropy<br><br>Involves creating a novel, precise, and unambiguous protocol from an abstract idea.|Medium Entropy<br><br>Requires selecting, configuring, and integrating from a vast library of existing tools.|Medium Entropy<br><br>Must predict and model real-world physical laws and constraints, which are inherently complex and uncertain.|Medium<br><br>Connects abstract hypotheses to the physical world, navigating a vast and constrained search space.|
|Tool Use|Low Entropy<br><br>The intent is highly specific and direct (e.g., "run this specific analysis tool").|Low Entropy<br><br>Typically consists of structured commands or simple instructions with low ambiguity.|Very Low Entropy<br><br>Involves calling predefined functions or APIs; the syntax and logic are deterministic.|Low Entropy<br><br>Input and output data formats are generally well-defined and structured, reducing uncertainty.|Very Low<br><br>The process is deterministic with low entropy, making it the easiest stage for AI to automate reliably.|
|Tool Creation|Very High Entropy<br><br>Requires defining and solving a problem for which no solution currently exists.|Very High Entropy<br><br>Needs to describe the principles, architecture, and logic of a novel, non-existent entity.|Very High Entropy<br><br>Involves designing and implementing new, complex algorithms and systems from scratch.|Very High Entropy<br><br>The new tool must reliably and robustly interact with the complex physical or computational world.|Very High<br><br>Combines the creative difficulty of hypothesis discovery with the engineering challenge of building a robust, functional system.|
|Results Analysis & Refinement|Low Entropy<br><br>The intent is more open than tool use (e.g., "find meaningful patterns in the data").|Low Entropy<br><br>Requires generating interpretations, summaries, and insights, allowing for more linguistic flexibility.|Low Entropy<br><br>Involves writing analysis scripts that are more complex than simple API calls but often rely on standard libraries.|Low Entropy<br><br>Raw experimental data often contains noise and artifacts, introducing uncertainty into the interpretation process.|Low<br><br>The task is constrained by the provided data, but requires sophisticated reasoning to interpret results and suggest refinements.|


Information Entropy, representing the profound uncertainty at the outset of any novel inquiry. As a pure, unarticulated concept, it is not a falsifiable proposition about the world; therefore, its Verifiability is almost zero.

Natural Language is the primary medium for structuring this high-entropy intent into a more tractable form. The properties of a natural language object are highly context-dependent. During creative phases like hypothesis generation, its Entropy is extremely high to allow for exploration. During planning or command phases, an agent’s task is to generate a low-entropy, unambiguous statement. The Verifiability of a natural language artifact, such as a research plan, is based on its logical consistency and can be assessed against an existing knowledge base.

Computer Language is the medium for formal, unambiguous representation and execution. The computer language discussed in this context is primarily presented as code. Generating a computer language object, such as a query, a simulation script, or a new tool, is a process of significant entropy reduction because it transforms the ambiguity of natural language into a deterministic form. A computer language artifact possesses a high degree of Verifiability; it can be formally tested against a specification to determine if its behavior is correct.

Physical Information is the raw, empirical data gathered directly from the physical world. It may include measurements, signals, and experimental observations, etc. This is different from physics information, which refers to theoretical knowledge and concepts within the discipline of physics itself. Such data plays a dual role in scientific discoveries in the sense that existing datasets serve as an input for generating hypotheses, while new experimental data provides the output for testing them. Although the physical process generating the data may have high entropy due to factors like random noise or complexity, the recorded data itself is a factual observation. Consequently, physical information possesses the highest degree of Verifiability, which is formally determined by statistical significance and reproducibility. This verifiable data constitutes the evidence required to evaluate the original hypothesis.

###### 2.3.3 An Analysis of Information Across Autonomous Scientific Discovery Phases

Using an information theory framework, we evaluate the entropy of different types of information, including human intent, natural language, computer language, and physical information within each phase, linking this to the difficulty of automation (dissipation). As shown in Table 2 and Figure 5 and 6, our findings reveal which phases are the most challenging to automate and which are the easiest.

Information Analysis Across Autonomous Scientific Discovery Phases

Very High

| |Very High|Very High|Medium|High|High|
|---|---|---|---|---|---|
| |High|Medium|Medium|Medium|Medium|
| |Low|Low|Very Low|Low|Very Low|
| |Very High|Very High|Very High|Very High|Very High|
| |Low|Low|Low|Low|Low|
| | | | | | |


Hypothesis Discovery

High

Entropy / Dissipation Level

Experimental Design

Medium

Tool Use

Tool Creation

Low

Results Analysis & Reﬁnement

Very Low Human Intent

Natural LanguageComputer LanguagePhysical InformationOverall Dissipation

- Figure 5: A heatmap representation of information analysis across autonomous scientific discovery phases.


We will delve into the unique challenges and information characteristics of each phase, providing a blueprint for building a fully autonomous scientific discovery system.

Hypothesis Discovery is characterized by high levels of uncertainty, exhibiting very high entropy in Human Intent and Natural Language. The initial intent is abstract and open-ended, requiring significant linguistic creativity to articulate novel concepts by synthesizing disparate ideas. Although the computer language used for auxiliary data mining is less complex, the reliance on vast, unstructured historical data also contributes to high entropy. The immense initial uncertainty and the need to sift through a vast space of possibilities to find a single valuable insight lead to high overall dissipation, making this a fundamentally creative and challenging phase to automate.

Experimental Design serves as a crucial bridge from abstract concepts to concrete actions. The entropy across all types of information is medium to high. The creative intent to design a novel experiment from numerous possibilities and the need to translate that into a precise natural language protocol contribute to this uncertainty. Furthermore, orchestrating existing computational tools for simulation and modeling the inherent uncertainties of real-world physical laws adds to the complexity. This effort to structure an abstract idea into a concrete plan involves navigating a large but constrained search space, leading to medium overall dissipation.

Tool Use represents the most structured and deterministic phase of the scientific workflow. It is defined by low or very low entropy across all information categories. The intent is highly specific, the natural language used is typically a simple command, and the computer language required is often a direct, deterministic API call or function. Because the process is predictable and the information involved is unambiguous, the overall dissipation is very low, making this the most straightforward phase to automate reliably.

Tool Creation stands as the pinnacle of complexity in this framework, exhibiting very high entropy across every information category. The process begins with the highly abstract intent to solve a problem for which no tool currently exists. It requires immense creativity to describe the principles of a novel system in natural language and to design and implement new, complex algorithms in computer language. The resulting tool must also reliably interact with the complex physical or computational world. This combination of high-entropy creative demands and rigorous engineering challenges results in very high overall dissipation, marking it as the most difficult phase to fully automate.

###### Information Analysis Across Autonomous Scientiﬁc Discovery Phases

###### Overall Dissipation

Very High

High

Medium

Low

Physical Information

Human Intent

(Entropy) (Entropy)

Very Low

Scientiﬁc Discovery Phases

Hypothesis Discovery Experimental Design Tool Use Tool Creation Results Analysis & Reﬁnement

| |
|---|


| |
|---|


| |
|---|


Computer Language

Natural Language

| |
|---|


| |
|---|


(Entropy) (Entropy)

- Figure 6: A radar chart representation of information analysis across autonomous scientific discovery phases.

Results Analysis and Refinement is a phase that operates under the strong constraints of the data generated from experiments. This grounding in data leads to low entropy across the information types involved. The intent is to find patterns within a defined dataset, and the natural language and computer language required are for interpreting and processing this data, not for open-ended creation. While this phase requires sophisticated reasoning to generate insights and suggest refinements, the task is one of inference within a bounded context rather than unconstrained exploration. This grounding in specific data results in low overall dissipation.

- 2.4 Different Levels of Autonomous Agents for Scientific Discovery


- Figure 7 illustrates a five-level framework for scientific agents, detailing a clear progression from human-centric research to full AI autonomy across five key dimensions: Hypothesis Discovery, Experimental Design, Tool Use, Tool Creation, and Analysis and Refinement.


The proposed five-level framework provides a more granular and clearly delineated model of AI autonomy in science compared to existing role-based classifications. Frameworks such as those by Zheng et al. [2025], Gao et al. [2024], Wei et al. [2025a] define levels based on the holistic role or overall capability of the AI system, making the boundaries between stages descriptive rather than precise.

In contrast, this new framework’s strength lies in grounding the progression of autonomy in the core information-processing challenges of scientific discovery. The transition through the levels can be understood as an agent’s increasing capacity to independently reduce information entropy, minimize dissipation, and systematically generate artifacts with high verifiability. This provides a more structured and measurable methodology for assessing an agent’s true capabilities.

- Level 1: Human-Led Model. At this foundational level, the agent’s role is purely instrumental, confined to the lowest-entropy and lowest-dissipation tasks where the workflow is predictable (e.g., Tool Use). Humans bear the full cognitive load of managing the immense information entropy inherent in creative processes like Hypothesis Discovery and Tool Creation. The human is the sole engine for reducing this initial uncertainty and driving the process toward a verifiable outcome.
- Level 2: AI-Augmented Model. The agent evolves into a supportive partner, beginning to assist in higher-entropy domains. While humans still lead, the AI collaborates in Hypothesis Discovery and


Experimental Design

Hypothesis Discovery

Result Analysis & Validation

Tool Creation

Tool Use

###### More Autonomy

Hypothesis Discovery

Result Analysis & Validation

Experimental Design

Tool Use

Tool Creation

Experimental Design

Hypothesis Discovery

Result Analysis & Validation

Tool Use

Tool Creation

Experimental Design

Result Analysis & Validation

Hypothesis Discovery

Tool Creation

Tool Use

Result Analysis & Validation

Hypothesis Discovery

Experimental Design

Tool Creation

Tool Use

Human Human-AI AI

Full AI Autonomy

AI-Led Hybrid Model

Full Human-AI Collaboration

AI-Augmented Model

Human-Led Model

- Figure 7: A five-level framework for classifying the autonomy of scientific agents. The framework progresses from a Human-Led Model (Level 1), where the agent is confined to simple, low-entropy tasks, to an AI-Augmented Model (Level 2) and a Full Human-AI Collaboration Model (Level 3), where the agent’s role expands to that of a supportive partner. A significant shift occurs in the AI-Led Hybrid Model (Level 4), where the agent takes the lead on most core scientific tasks, with humans collaborating on the most complex challenges. The final stage is Full AI Autonomy (Level 5), where the agent can manage the entire scientific process from abstract ideation to validated discovery, functioning as a truly autonomous researcher.


Experimental Design, helping to explore the large possibility spaces. However, it relies on human guidance to navigate the high dissipation (the cost of exploring unproductive paths) and converge on a viable research direction.

- Level 3: Full Human-AI Collaboration Model. This level is characterized by a comprehensive partnership where every task is performed collaboratively. The agent is now capable of functioning effectively across the entire entropy spectrum, from creative ideation to data analysis. It acts as a force multiplier, jointly tackling high-entropy challenges with the human. However, it does not yet possess the autonomy to lead the process or manage the most uncertain, dissipative phases on its own.
- Level 4: AI-Led Hybrid Model. A critical threshold is crossed as agents take lead in autonomously reducing entropy for core scientific tasks. It independently drives Hypothesis Discovery, Experimental Design, and Tool Use, demonstrating a sophisticated ability to navigate vast and unstructured information spaces. Human collaboration remains essential for the task with the absolute highest entropy and dissipation (Tool Creation) and for the final step of analysis and refinement, where human judgment ensures the ultimate verifiability of findings.
- Level 5: Full AI Autonomy Model. This represents the pinnacle of autonomous science. The agent possesses complete mastery over the entire information lifecycle. A Level 5 agent can independently manage the workflow from start to finish: confronting the maximum information entropy of an abstract scientific goal, navigating the extreme dissipation inherent in creating novel tools from scratch, and producing validated, high verifiability scientific facts. At this stage, the agent operates as a truly autonomous scientific researcher.


By defining the levels based on how an agent handles these fundamental properties of information, this framework moves beyond coarse role descriptions. The boundary between levels is marked by a concrete, observable shift in the agent’s ability to process uncertainty and create knowledge, offering a more robust and detailed methodology for measuring progress in the field of autonomous science.

Prompt-Based Knowledge-Grounded Multi-Agent-Based Evolutionary-Algorithm-Based

Hypothesis Generation

Passive Knowledge Injection Bottom-Up

Hypothesis Discovery Loop

Active Knowledge Acquisition Top-Down

###### LLM Agent

External Knowledge Base

Hypothesis Validation

Metric-Based Screening Agent-Based Validation

- Figure 8: The LLM-agent-driven workflow for Automated Hypothesis Discovery, centered around an iterative loop of generation and validation. The agent’s reasoning is informed by an external knowledge base through two distinct paradigms: a passive, bottom-up knowledge injection and an active, top-down knowledge acquisition. During the Hypothesis Generation phase, the agent employs one of four primary strategies: Prompt-Based, Knowledge-Grounded, Multi-Agent-Based, or Evolutionary-Algorithm-Based. The resulting ideas are then filtered and refined in the Hypothesis Validation phase, which utilizes either automated Metric-Based Screening or interactive Agent-Based Validation to produce a final set of verified hypotheses.


###### 3 Hypothesis Discovery

Hypothesis Discovery is a crucial creative process in scientific discovery, with the core objective of identifying and forming novel, verifiable scientific hypotheses from vast amounts of data and existing knowledge. This process aims to accelerate the pace of knowledge discovery by revealing hidden connections that are difficult for human researchers to find alone [Swanson, 1986]. With the rise of Large Language Models (LLMs), the level of automation and efficiency in hypothesis discovery has been enhanced to an unprecedented degree[He and Chen, 2025, Luo et al., 2025a]. A complete hypothesis discovery workflow typically includes the following three key stages: Knowledge Extraction, Hypothesis Generation, and Hypothesis Screening and Validation (Figure 8).

###### 3.1 Knowledge Extraction

Knowledge Extraction is the cornerstone of the hypothesis discovery pipeline. Its core task is to automatically identify, extract, and structure key information from large volumes of unstructured data, especially scientific literature, to lay the groundwork for subsequent hypothesis generation and validation.

Traditional knowledge extraction methods involve a labor-intensive, bottom-up pipeline using techniques like Named Entity Recognition (NER) and Relation Extraction (RE) to build static, structured Knowledge Graphs (KGs) from unstructured text [Nickel et al., 2015, Ji et al., 2021]. In contrast, modern paradigms leverage the vast implicit knowledge already embedded within Large Language Models (LLMs). This shift moves away from building fixed knowledge bases and instead focuses on dynamically activating and applying the LLM’s built-in reasoning capabilities. Crucially, this transition reframes the entire process: multi-step extraction tasks are now often reshaped into a single, end-to-end generative task, where the LLM directly generates the desired structured knowledge.

Scientific Foundation Models. To overcome the limitations of general models in specialized fields, expert models are created by training or fine-tuning them on vast, domain-specific scientific data [Gururangan et al., 2020, Pyzer-Knapp et al., 2025, Zhao et al., 2025, Subramanian et al., 2023, Barman et al., 2025, Narayanan et al., 2025]. For instance, models like BioBERT are pre-trained on biomedical texts, enabling them to more accurately extract specific entities like genes, diseases, and chemicals, as well as the relationships between them from research articles [Lee et al., 2020]. Similarly, generative models like BioGPT can not only extract but also summarize complex biological information coherently [Luo et al., 2022]. On a broader scale, models such as Galactica were designed

with the explicit goal of structuring and organizing scientific knowledge from papers, lecture notes, and textbooks, essentially performing knowledge extraction on a massive scale [Taylor et al., 2022]. By internalizing the nuances of a specific scientific language, these models serve as far more effective tools for building accurate and comprehensive knowledge bases from technical documents.

Retrieval-Augmented Generation (RAG). Retrieval-Augmented Generation (RAG) is a technique designed to address the critical issues of outdated knowledge and hallucination in LLMs by connecting the model to external knowledge sources [Lewis et al., 2020, Guu et al., 2020, Gao et al., 2023, Izacard et al., 2023, Fan et al., 2024]. In the context of knowledge extraction, its primary function is to transform vast, unstructured scientific literature into a verified and structured knowledge base [Garcia

- et al., 2024, Lopez et al., 2025, Feng et al., 2025a, Krotkov et al., 2025]. By retrieving relevant documents and using them as a direct source, RAG generates factually-grounded and traceable outputs, such as precise summaries or extracted entity-relationship pairs, which serve as the reliable foundation for subsequent analysis and discovery [Lee et al., 2025, Xie et al., 2024, Gao et al., 2025a].


Multimodal Knowledge Extraction. With the advent of multimodal models and agents that can invoke analysis tools, knowledge extraction from scientific literature is no longer confined to text [Khalighinejad et al., 2024, Odobesku et al., 2025]. For instance, systems like ChemMiner leverage multimodal capabilities to extract chemical information from both text and diagrams within papers [Chen et al., 2024a], while ChartAssistant demonstrates the ability to reverse-engineer scientific charts by converting visual data back into structured tables [Meng et al., 2024]. Similarly, the use of Multimodal Models, such as GPT-4o, enables the processing of complex biomedical documents by integrating information across text, tables, and diagrams to answer questions [Hurst et al., 2024].

###### 3.2 Hypothesis Generation

Hypothesis generation is the core of hypothesis discovery, aiming to formulate plausible and testable statements that explain observed phenomena or predict outcomes under certain conditions. In scientific practice, it is a creative yet structured step that bridges observation and prediction. A good hypothesis should be grounded in existing knowledge and make predictions that can be empirically tested and potentially proven wrong. Traditionally, scientists generate hypotheses by identifying gaps or contradictions from previous literature, drawing analogies from other domains, and applying domain expertise to reason. Recent advancements are progressing beyond classic literature-based discovery (LBD) [Swanson, 1986] to develop dynamic, agentic systems capable of independently reading, reasoning, and iteratively proposing sophisticated, testable conjectures. This evolution in methodology can be categorized into four key approaches:

Prompt-Based Systems. At its most fundamental level, hypothesis generation using LLMs can be achieved through prompt-based methods. This approach directly leverages the extensive knowledge an LLM acquires during its pre-training phase. By formulating a carefully constructed prompt, a

- user can query the model to propose hypotheses in a zero-shot fashion [Qi et al., 2023, Zhou et al.,


- 2024]. Early evidence shows LLMs can act as zero-shot hypothesis proposers in biomedicine [Qi

et al., 2023], relying on their pre-trained knowledge alone to formulate ideas. The efficacy of this method is contingent upon the LLM’s internal representation of scientific concepts and relationships. While this allows for the exploration of a broad range of ideas, it also introduces a susceptibility to generating plausible but factually incorrect statements or restating known facts [Xiong et al., 2025].

Knowledge-Grounded Systems. To enhance the factual accuracy and novelty of generated hypotheses, knowledge-grounded methods have been developed. These techniques augment the LLM’s internal knowledge with external, authoritative information. One prominent technique is RetrievalAugmented Generation (RAG), which dynamically retrieves unstructured textual evidence from literature. By synthesizing information from multiple, potentially disparate sources, it enables the model to infer novel connections and propose innovative, evidence-backed hypotheses [Bazgir et al.,

- 2025b]. Another powerful technique involves the injection of structured knowledge, often from curated knowledge graphs (KGs). KG-CoI [Xiong et al., 2024], for example, utilizes structured knowledge sources such as knowledge graphs (KGs) to ground its hypotheses, improving the accuracy of its reasoning chains and reducing factual errors. ResearchLink [Borrego et al., 2025], for example, integrates graph embeddings, path-based features, and bibliometric data to generate cross-domain hypotheses with high precision. Moreover, a recent study [Tong et al., 2024] presents a novel framework that combines large language models (LLMs) with causal knowledge graphs to generate psychological hypotheses. By analyzing over 43,000 psychology articles, the approach


produced hypotheses on well-being that matched expert-level novelty and significantly outperformed LLM-only methods.

Multi-Agent Systems. To broaden the scope of hypothesis generation, multi-agent frameworks emulate collective brainstorming by leveraging diversity from multiple sources [Wu et al., 2023, Chase, 2022]. This approach generates a richer pool of initial ideas by either utilizing different foundation models as distinct agents or by assigning different roles and prompts to instances of the same model. These varied configurations steer the models to generate outputs from different conceptual angles by activating distinct generative distributions. By synthesizing ideas from these diverse agents, the framework effectively uncovers less obvious connections and produces a more comprehensive set of potential hypotheses than a monolithic approach could achieve alone [Chen et al., 2025b, Bazgir et al., 2025b]. For example, systems such as AI co-scientist [Gottweis et al., 2025a] employ a proposer-critic dynamic, where some agents generate initial ideas while others rigorously challenge their assumptions to refine them through interaction. This paradigm is implemented in specialized frameworks like ACCELMAT for materials science [Kumbhar et al., 2025a], which

- uses a structured, iterative loop of proposal and critique among multiple agents to progressively enhance the quality of novel material hypotheses. VIRSCI [Su et al., 2024] extends this by simulating scientific teams using real-world academic data, enabling agents to form collaborative research teams and generate novel ideas through inter- and intra-team discussion mechanisms. Similarly, AstroAgents [Saeedi et al., 2025] deploys domain-specific agents to interpret mass spectrometry data and hypothesize about prebiotic chemical pathways related to the origins of life, with more than 30% of hypotheses validated as scientifically plausible by expert reviewers.


Evolutionary Algorithm-Based Systems. For a dynamic and automated LLM-based approach to discovery, closed-loop systems apply principles from evolutionary algorithms to treat hypothesis generation as an optimization problem. An initial population of hypotheses undergoes iterative refinement using operators such as mutation and recombination, while a fitness function evaluates the quality of the hypothesis to guide the selection. This paradigm is exemplified by systems like MOOSE-Chem [Yang et al., 2025], which uses evolutionary search to guide different ways of associating inspirations and background to generate hypotheses. This combination ensures that generated hypotheses are not only optimized but also validated for novelty against the knowledge baseline established during the LLM’s pretraining. Similarly, HypoAgents [Duan et al., 2025] integrate Bayesian updating within an evolutionary loop: agents propose hypotheses, test them via RAG-informed evidence, update probabilities, and refine uncertain hypotheses in a continuous scientific feedback cycle. MolLEO [Wang et al., 2024b] leverages LLMs directly as mutation and recombination operators, prompted with text-based instructions and desirable target properties. LLMbased evolutionary systems show immense promise for navigating vast combinatorial spaces [Liu et al., 2025b] with textual information extraction or rich, semantic objectives, such as discovering new materials [Jia et al., 2024], mechanical structures [Jadhav and Farimani, 2024], molecules [Wang et al., 2024b] or macromolecules [Reinhart and Statt, 2024]. They also show potential for multi-objective numerical optimization [Liu et al., 2024e], which includes real-world problems like optimizing nozzle design, heat transfer or wind farm layout [Brahmachary et al., 2025].

###### 3.3 Hypothesis Screening and Validation

Rigorous screening and validation of automatically generated hypotheses rely on a clear set of evaluation axes, such as plausibility, novelty, feasibility, and cost [Alkan et al., 2025, Bazgir et al., 2025c]. This step is necessary to manage the large volume of generated ideas and requires transparent assessment methods to avoid over-claiming [Beel et al., 2025]. Methodologies for this stage can be broadly classified into two approaches: automated evaluation based on defined metrics and dynamic refinement through agent-based critique.

Metric-Based Screening. This approach focuses on developing automated, scalable, and objective criteria to evaluate hypotheses. Some frameworks implement formal statistical controls; for example, POPPER introduces an automated validation framework that achieves human-level accuracy at significantly greater speed by applying rigorous statistical checks [Huang et al., 2025a]. Other methods focus on specific metrics like novelty, where systems such as SCIMON explicitly compare new ideas against existing literature and revise them until they no longer resemble prior work [Wang et al.,

- 2024c]. To enhance external validity and enable consistent comparisons, standardized benchmarks are emerging. These include task-specific suites like MATDESIGN for materials science, which


introduces scalable quality metrics [Kumbhar et al., 2025b], and general platforms like HypoBench, which provides a main benchmark for hypothesis discovery across diverse tasks [Liu et al., 2025a]. Beyond these, recent approaches employ LLM-derived priors for automatic hypothesis assessment. In particular, the Logit-based Calibrated Prior technique [Gong and Fernandez, 2025] uses LLMgenerated expectations to quantify how surprising a correlation is, enabling ranking of hypotheses by novelty and relevance with high accuracy in real-world data. Meanwhile, Bayesian frameworks have been deployed for evaluating model capabilities [Xiao et al., 2025], treating performance assessment as a hypothesis testing task under uncertainty—an approach that introduces probabilistic robustness when sample sizes are limited.

Agent-Based Validation. This approach simulates the collaborative and critical processes of scientific inquiry, where agents interact to challenge and improve hypotheses. Frameworks like ResearchAgent facilitate an iterative dialogue between a proposal-generating agent and a panel of reviewer agents. This process mimics peer review, refining the hypothesis until it meets rigorous criteria [Baek et al., 2024]. Similarly, to ensure empirical testability, other systems close the loop between theory and evidence. The Scientific Generative Agent (SGA), for instance, combines an LLM acting as a theorist with scientific simulators that function as experimental systems. This allows the agent to immediately test and revise its hypotheses based on simulated experimental outcomes, ensuring ongoing refinement based on feedback [Ma et al., 2024].

###### 4 Experimental Design and Execution

In this section, we analyze the critical phases of Experimental Design and Execution within the autonomous scientific discovery process. As depicted in Figure 9, we first examine how LLM agents generate robust experimental plans by integrating high-level human guidance, leveraging external knowledge sources via Retrieval-Augmented Generation (RAG), and incorporating feedback from prior experiments. We then detail the Experimental Execution phase, focusing on the various strategies, from highly structured to dynamically collaborative, that agents use to interact with and manage external tools, bridging the gap between abstract plans and physical reality.

###### 4.1 Experimental Design

A critical step in scientific discovery, following hypothesis generation, is experimental design. This involves creating a structured plan to systematically test ideas and achieve research objectives. The process is fundamentally a form of workflow generation, where high-level scientific goals are translated into concrete, executable protocols. LLM-based scientific agents are increasingly used for this task, combining natural language reasoning with planning capabilities, often enhanced by retrieval tools and physical knowledge, to generate coherent and detailed experimental plans.

The core challenge for LLM agents in experimental design is navigating a nearly infinite space of possible action sequences to find a solution that is both scientifically sound and practically feasible. To address this, agents employ various strategies to effectively constrain and navigate this complex space.[Huang et al., 2025b, Zhou et al., 2025a, Cao et al., 2024, Yu et al., 2024a] These strategies can be grouped into four main categories: RAG for Grounded Planning, Human High-Level Guidance, Templates and Predefined Actions, Post-Execution Feedback.

Retrieval-Augmented Generation for Grounded Design. This strategy ensures that an agent’s plan is scientifically valid from the outset by grounding its reasoning in external, reliable knowledge sources. Instead of relying solely on its internal training, the agent uses a Retrieval-Augmented Generation (RAG) approach to query specialized tools, databases, and scientific literature. This allows the agent to build its experimental plan on a foundation of established facts and methods.

Biomni [Huang et al., 2025b] first creates a comprehensive action space by automatically mining tens of thousands of scientific papers for relevant tools and databases. When given a task, it retrieves the most pertinent tools from this space to construct its plan. TxAgent [Gao et al., 2025b] uses a specialized retrieval model called ToolRAG to select the most appropriate tools from its ToolUniverse of 211 clinical instruments, ensuring its therapeutic reasoning is based on evidence. Chemist-X [Chen

- et al., 2023a] leverages RAG to search literature and molecular databases to define a promising and constrained search space for reaction condition optimization before any physical experiments are run. CLADD [Lee et al., 2025] has a Planning Team which retrieves the most relevant resources from


Human Scientists

Domain Knowledge

Templates

Feedback

Action Pool

High Level Guidance Predeﬁned Components

Human in the loop

External Sources

Databases

RAG Experimental Design

Tools

Scientiﬁc Literature

Detailed Workﬂow

LLM Agent

Experimental Execution

Experimental Results

Tool Use Tool Creation

Embedded Toolbox-Based Reﬂective and Iterative Hierarchical

- Stage 1 LLM as Generator, Coder, Analyzer
- Stage 2 Hard-coded Tool Use


Description & Examples

Think & Plan

Agent 1 Toolbox 1

Reﬂection

Action

Tool 1

...

###### ...

Result

Agent N Toolbox N

Tool N

Observe

Tool Use

- Figure 9: An LLM-agent-driven workflow of automated Experimental Design and Execution. This workflow illustrates how an LLM agent orchestrates experimental design and execution. In the Experimental Design phase, the central agent generates a detailed workflow by integrating information from multiple inputs. It receives high-level guidance (domain knowledge, feedback) and predefined components (templates, action pools) from Human Scientists, leverages Retrieval-Augmented Generation (RAG) to pull in knowledge from External Sources, and incorporates Experimental Results from previous execution cycles as a critical feedback mechanism for refinement. For the Experimental Execution phase, the agent acts upon the detailed workflow, deciding between using existing instruments (Tool Use) or developing new ones (Tool Creation). Tool use can be implemented through four primary strategies for tool interaction: Embedded, Toolbox-Based, Reflective and Iterative, and Hierarchical.


databases and tools. The Molecule Understanding Team then generate structured reports based on these external sources which are synthesized by a Prediction Agent.

Human High-Level Guidance. For complex or novel scientific challenges, LLMs may struggle to generate a high-quality experimental design on its own. As noted in some studies [Zhou et al., 2025a, Qu et al., 2025], human expertise is often crucial to refining and validating the agent plan. In this collaborative model, the human scientist acts as a supervisor, providing high-level guidance and feedback to guide the agent’s decision-making process.

MAPPS [Zhou et al., 2025a] framework includes a Scientific Mediator module. This component allows human scientists to interact with the agent, providing feedback, offering guidance, and making corrections to the experimental plan, ensuring that the agent’s autonomous discovery process remains aligned with scientific principles and the researcher’s goals. AI co-scientist [Gottweis et al., 2025a] introduces a scientist-in-the-loop paradigm, where human scientists actively collaborate with agents throughout the research cycle. Human scientists interact with the system by specifying a research goal, suggesting their own ideas, providing feedback and reviews. In Virtual Lab [Swanson et al., 2024], The human researcher defines the Principal Investigator (PI) and Scientific Critic agents by

specifying their title, expertise, goal, and role, and sets the agenda for each meeting, which guides the agents to further design experiments and solutions.

Human-Provided Templates and Predefined Actions This is a more structured form of humanAI collaboration where humans define the fundamental building blocks of an experiment, and the LLM’s role is to assemble them into a coherent workflow. Humans may provide a set of allowed "meta-actions" in an action pool or create high-level workflow templates. The agent then fills in the specific parameters and details. This approach often involves modeling the experiment as a state machine, where the agent’s primary task is to establish the rules for transitioning between predefined experimental states.

The k-agents [Cao et al., 2024] framework exemplifies this by having an execution agent that decomposes a human-provided experimental procedure into a state machine. The agent then interacts with other knowledge agents to execute each state and uses the results to determine the next transition, enabling closed-loop control. CRISPR-GPT [Qu et al., 2025] utilizes expert-predefined meta-tasks as high-level templates, while its LLM planner decomposes the user’s high-level request and links it to corresponding state machines to assemble a complete, executable workflow. PerTurboAgent [Hao et al., 2025] operates using a predefined Action Pool containing high-level actions like predict, reflect, and refine. The agent designs its experiment by selecting and sequencing these actions to decide which genes to perturb in each round.

Post-Execution Feedback. This strategy does not require a perfect plan from the start. Instead, the agent’s design process is an exploratory one, where it learns and adapts by observing the results of its actions. This feedback can be used to make immediate, step-by-step corrections or to inform the design of the next major experimental cycle.

Agents like ChemToolAgent [Yu et al., 2024a] use the ReAct loop to solve chemistry problems by calling a tool, observing the output, and planning the subsequent action based on that result. BioInformatics Agent [Xin et al., 2024] uses a self-correction loop; if an analysis workflow’s initial output doesn’t meet user expectations, it modifies the entire workflow and re-executes it. BioDiscoveryAgent [Roohani et al., 2024] operates in a closed loop, using the results from one round of genetic perturbations to reason about which genes are most promising to test in the subsequent round. OSDA Agent [Hu et al., 2025] adopts an Actor-Evaluator-Reflection loop, where an LLMbased Actor generates candidate OSDA molecules, which are subsequently assessed by an Evaluator through chemical validity checks. A Self-reflector module then integrates this feedback to guide the iterative refinement of the Actor’s outputs.

###### 4.2 Experimental Execution

The experimental execution stage is a central phase in the scientific discovery process, serving as the crucial bridge that transforms abstract strategies into the concrete actions and empirical evidence needed for generating insights. It involves the systematic implementation of a designed workflow, which extends beyond simply running code to include a range of complex tasks: orchestrating computational resources, managing large datasets, interfacing with laboratory instruments or simulators, and continuously monitoring the workflow to ensure its correctness, efficiency, and reproducibility. LLM-based agents operate at the intersection of natural language instructions, computer language, and physical information, enabling a fluid transition from concept to execution. The execution of planned experiments by LLM agents is primarily achieved through two interconnected capabilities, namely tool use and tool creation.

###### 4.2.1 Tool Use

For LLM-based agents to be effective in science, the ability to use tools is essential. First, generalpurpose tools like search engines allow agents to survey the dynamic landscape of scientific research. This ensures their work is grounded in the most recent findings and established principles. More critically, since LLMs are fundamentally text-based models and lack the ability to directly interact with or measure the physical world, they must rely on domain-specific tools for analysis and exploration. By interfacing with chemical simulation software, data analysis pipelines, or robot lab equipment, agents can bridge the gap between text-based reasoning and empirical science. Over the past few years, several distinct strategies for integrating agents with external tools have emerged, representing a spectrum of autonomy from highly controlled pipelines to dynamic, collaborative systems.[Hu

- et al., 2025, Swanson et al., 2024, Jin et al., 2024a, Yu et al., 2024a, Huang et al., 2025b] To provide a structured view, we categorize these strategies into four representative models of tool use: Embedded Tool Use, Toolbox-based Tool Use, Reflective & Iterative Tool Use, and Hierarchical Tool Use in Multi-Agent Systems.


Embedded Tool Use. The Embedded Tool Use method represents a structured and highly controlled approach to integrating AI with scientific workflows. In this model, developers pre-define a complete research pipeline where specific tools are hard-coded to execute at particular stages. The Large Language Model (LLM) acts not as a decision-maker for tool selection, but rather as a component within the workflow. Its role is often confined to interpreting the output of a tool, generating code for a specific, predetermined step, or translating human instructions into parameters for the next tool in the sequence. This method ensures reliability and reproducibility, making it well-suited for routine, high-throughput analyses where the scientific process is already well-established.

For example, OSDA Agent [Hu et al., 2025] embeds the LLM into a fixed "Actor-Evaluator-Reflector" loop, where the LLM acts as a molecule generator and reflector, while a set of hard-coded computational chemistry tools serves as the evaluator to validate its output. LLMatDesign [Jia et al., 2024] adopts a pre-set iterative design loop, in which the LLM is responsible for proposing material modification plans and reflecting on the results, but the specific structure relaxation and property prediction are executed by hard-coded Machine Learning Force Field (MLFF) and Machine Learning Property Predictor (MLPP) tools. MatLLMSearch [Gan et al., 2025] embeds the LLM into a fixed evolutionary algorithm framework, where its role is confined to the stage to generate new crystal structure candidates, which are then passed to a preset evaluation pipeline composed of tools like MLFF and DFT. scBaseCount [Youngblut et al., 2025] embeds the LLM in a fixed pipeline for large-scale single-cell data retrieval, preprocessing, normalization and formatting, to create a unified repository for single-cell RNA-seq data. Chemist-X [Chen et al., 2023a] embeds the LLM to interact with pre-packaged API functions including CAD tools and ML models.

Toolbox-Based Tool Use. This method empowers the AI agent with significantly more autonomy. The agent is provided with a toolbox or a library of available functions. Each tool is accompanied by a natural language description of its purpose, inputs, and outputs. The LLM leverages its reasoning capabilities to interpret a user’s high-level goal, decompose it into smaller steps, and select the most appropriate tool from the toolbox to accomplish each step. This approach transforms the LLM from a simple component into a central coordinator, capable of orchestrating complex sequences of operations.

This approach is demonstrated in works such as AgentMD [Jin et al., 2024a] is a clinical agent that curates and applies medical risk calculators by selecting from 2,164 mined clinical tools. ChemCrow [M. Bran et al., 2024] bridges drug discovery and materials science using 18 expert-designed tools. scAgent [Mao et al., 2025] contains a tool hub offers over 30 plugins that centralizes diverse single-cell analysis methods into a unified interface. TxAgent [Gao et al., 2025b] leverages a broad Tool Universe, spanning drug databases, molecular analysis, and clinical resources, which allows the agent to dynamically select and integrate multiple tools for therapeutic reasoning. GIS Copilot [Akinboyewa et al., 2025] integrates Agent into QGIS to autonomously conduct spatial analysis. Equipped with comprehensive tool documentation and external libraries, it enables the agent to dynamically dynamically select, generate, and execute geospatial analysis workflows. SciToolAgent [Chen et al., 2025a] builds a Scientific Tool Knowledge Graph that maps the intricate relationships, dependencies, and compatibilities among a vast library of scientific tools , which allows an LLM to create an optimal Chain-of-Tools tailored for a specific scientific query. This graph-based toolbox overcomes the limitations of previous agents that struggled with integrating a large and diverse toolset.

Reflective and Iterative Tool Use. This approach moves beyond simple tool selection, enabling the agent to reflect on the results of each tool use and dynamically plan its next steps. This process mimics the human approach to problem-solving: try, observe, reflect, and then decide what to do next. The ReAct [Yao et al., 2023] (Reasoning and Acting) framework is a prime example of this methodology. It operates in a continuous loop of Thought-Action-Observation. Similarly, the CodeAct [Wang et al.,

- 2024e] framework is a specialized extension of ReAct. Here, the agent’s actions involve generating and executing code in a sandboxed environment. After execution, the agent observes the code’s output or any error messages. If the code fails, the agent reflects on the error, iteratively generates a corrected version, and tries again.


ChemToolAgent [Yu et al., 2024b] is a prime example, using the ReAct framework to orchestrate a suite of 29 different tools, from searching the PubChem database to predicting molecular properties. It can reason about a user’s chemistry question, call the right tool, and then analyze the output to decide the next logical step, like performing another calculation or synthesizing the results into a final answer. Biomni [Huang et al., 2025b] is a general-purpose biomedical AI agent that automates complex data analysis by leveraging the CodeAct framework. This code-based iterative method allows Biomni to navigate vast, interconnected knowledge domains with the flexibility of a virtual biologist, writing, running, observing, and debugging code to accomplish its goals. PerTurboAgent [Hao et al.,

- 2025] is an agent for sequential Perturb-seq. At each round, the agent integrates prior knowledge, perturbation-effect models, and past experimental results to reflect on outcomes, update predictions, and propose the next gene panel. This closed-loop process adaptively prioritizes perturbations with the highest phenotypic impact.


Hierarchical Tool Use in Multi-Agent Systems. As the complexity of scientific inquiry increases, a single agent may struggle to manage an overwhelmingly large and diverse toolbox. The hierarchical delegation method addresses this by employing a team of specialized AI agents. A high-level planner agent first deconstructs a complex problem into sub-tasks. These sub-tasks are then delegated to different expert agents, each equipped with its own smaller, specialized toolbox. This division of labor makes the tool selection process more manageable and robust, mirroring the structure of human scientific teams.

For example, the Team of AI-made Scientists (TAIS) [Liu et al., 2024a] framework simulates a research team by assigning LLM agents specialized roles such as planner, data handler, and analyst. Similarly, MedAgents [Tang et al., 2023] uses a collaborative approach where distinct medical expert agents, each with specialized tools, iterate to reach a consensus diagnosis. In chemistry, ChemAgents [Song et al., 2025] employs a hierarchical system with five specialized agents, including a Literature Reader and Robot Operator. In materials, AtomAgent [Ghafarollahi and Buehler,

- 2024b] collaborate across knowledge retrieval, multimodal data analysis, and molecular simulations, autonomously orchestrating alloy design workflows and accelerating data-driven discovery of highperformance materials. For protein design, ProtAgents [Ghafarollahi and Buehler, 2024a] deploys multiple agents with distinct skills that dynamically collaborate on engineering tasks. The “ChatGPT Research Group” [Zheng et al., 2023] integrates seven specialized assistants for MOF/COF synthesis, with agents dedicated to planning, literature mining, and robot operation. In antiviral antibody design, Virtual Lab [Swanson et al., 2024] introduces a multi-agent system where a PI agent coordinates scientist agents using the protein language model (PLM) ESM [Lin et al., 2023], the protein folding model AlphaFold-Multimer [Abramson et al., 2024], and the computational biology software Rosetta [Boorla et al., 2023], generating 92 nanobody candidates and experimentally validating two with improved binding to SARS-CoV-2 variants. In physics, the k-agents framework [Cao et al., 2024] enables an autonomous quantum laboratory where agents plan and execute experiments on quantum processors.


###### 4.2.2 Tool Creation

While many AI agents demonstrate a remarkable ability to use existing software libraries and digital tools, a new frontier is emerging where their primary function shifts from application to invention. The most advanced scientific agents are transcending mere tool orchestration to create entirely new scientific tools and algorithms. This paradigm shift marks the evolution of AI from a digital assistant that follows a playbook to a creative partner capable of contributing novel methods and solutions to complex scientific problems.

At the forefront of the creative paradigm are agents that generate code not just to execute a workflow, but to discover new methods. ToolUniverse [Gao et al., 2025c] is designed to democratize the power of AI scientists by enabling LLM agents to not only execute workflows with a comprehensive suite of existing tools, but also autonomously invent, implement, and integrate new, reusable scientific algorithms, transforming agents from mere users to creative toolmakers. MAPPS [Zhou et al., 2025a] represents a powerful hybrid approach that blends the use of existing tools with the creation of new algorithms. Its code generation is twofold: it generates code to use established physics-based foundation models for analysis, but more importantly, it simultaneously invents and implements new algorithms tailored to discover novel materials more efficiently. CodePDE [Li et al., 2025a] iteratively generates, tests, and refines code to produce high-performance solvers for partial differential equations (PDEs). The final output is not just the solution to a single problem, but a robust, reusable solver that

constitutes a new and valuable scientific tool. AlphaEvolve [Novikov et al., 2025] takes this concept further by employing an evolutionary framework. It treats a population of algorithms as a gene pool and uses an LLM to “mutate” the code, iteratively evolving better solutions. This process has led to the discovery of entirely new algorithms that are more efficient than those designed by humans, showcasing code generation as a mechanism for pure algorithmic invention [Nagda et al., 2025]. ShinkaEvolve [Lange et al., 2025] similarly evolves programs, improving sample efficiency through exploration–exploitation-balanced parent selection, novelty-based program rejection sampling, and bandit-based, task-dependent LLM prioritization. TOOLMAKER [Wölflein et al., 2025] introduces an autonomous framework for transforming scientific code repositories into LLM-compatible tools, enabling agents to not only employ but also systematically generate new utilities, with cross-domain evaluations demonstrating substantially higher reliability than prior software-engineering agents.

###### 5 Result Analysis and Refinement

###### 5.1 Result Analysis

Experimental result analysis in scientific discovery is the critical process where autonomous agents interpret raw outputs—such as numerical data, plots, and images—to derive meaningful scientific insights [Gridach et al., 2025b]. This stage presents significant challenges, including the need to handle complex, multimodal data types and ensure the analysis is scientifically robust [Liu et al.,

- 2025c, Zhang et al., 2024d]. The approaches to this task are classified into distinct paradigms based on the core mechanism the agent uses to interact with and process the data.


The analysis of experimental results by AI agents can be categorized into three primary paradigms, distinguished by the agent’s core mechanism for interacting with and interpreting scientific data. These approaches are not mutually exclusive; rather, the most advanced systems often blend them to tackle complex, multi-faceted research problems. Table 3 presents a concise overview of three distinct approaches to analyzing and interpreting scientific results.

Modality-Driven Analysis. This paradigm is defined by its reliance on the advanced perceptual and interpretive capabilities of Multimodal Large Language Models (MLLMs) [Han et al., 2023, Meng

- et al., 2024, Hurst et al., 2024, Li et al., 2024a, Fu et al., 2024, Yan et al., 2024]. The core mechanism involves the direct processing of non-textual data formats, such as images, charts, videos, and even audio, to extract scientific insights. Instead of relying on structured numerical inputs, the agent "sees" the data as a human researcher would. This approach is critical for disciplines where visual evidence is paramount. Representative systems like The AI Scientist-v2 [Yamada et al., 2025] leverage a Vision-Language Model (VLM) in a feedback loop to critique and refine generated plots, ensuring they are not only accurate but also clearly interpretable. Other specialized work, such as PlotGen [Luo et al., 2024], focuses on deconstructing scientific charts into their semantic components—axes, legends, data points—to perform detailed analysis and verification.


However, this paradigm faces significant limitations. The inherent heterogeneity of scientific data (e.g., diverse chart types, microscopy images, spectral graphs) poses a major processing challenge. Furthermore, the ambiguity of visual information can lead to misinterpretations, and the high computational cost of training and running large-scale MLLMs remains a practical barrier.

Tool-Augmented Analysis. As the most prevalent and mature paradigm, tool-augmented analysis centers on the agent’s ability to interact with external, domain-specific resources, including software APIs, databases, and even physical hardware. This approach grounds the LLM’s reasoning process in the deterministic and validated outputs of specialized tools, mitigating the risk of factual hallucination and enabling highly technical operations. For instance, ChemCrow [Bran et al., 2023] is equipped with a suite of chemistry tools for tasks like predicting reaction outcomes and searching molecular databases. Coscientist [Boiko et al., 2023] has demonstrated the ability to not only use bioinformatics software but also control liquid handling robots to execute experiments. Similarly, Virtual Lab [Boeck

- et al., 2023] follows a computational pipeline of specialized tools for nanobody design.


The primary limitations of this paradigm include the reliability of the external tools themselves, the risk of error propagation through a chain of tool calls, and practical challenges like API costs, latency, and the lack of interface standardization across the scientific software ecosystem.

Computation-Native Analysis. This paradigm leverages the agent’s intrinsic ability to generate and execute code and perform symbolic reasoning. It treats data analysis as a computational task to be

Table 3: Comparison of Results Analysis Paradigms

|Paradigm|Core Mechanism|Primary Data Modality|Representative Systems|
|---|---|---|---|
|Modality-Driven Analysis|Visual/multimodal perception and interpretation|Images, charts, video, audio|ChartLlama [Han et al., 2023], ChartAssisstant [Meng et al., 2024], The AI Scientist-v2 [Yamada et al., 2025], PlotGen [Luo et al., 2024]|
|Tool-Augmented Analysis|Interaction with external APIs, software, or hardware|Domain-specific data formats|ChemCrow [Bran et al., 2023], Coscientist [Boiko et al., 2023], Virtual Lab [Boeck et al., 2023]|
|ComputationNative Analysis|General code generation/execution, symbolic reasoning|Tabular data, text, numerical arrays|Data Interpreter [Hong et al., 2024], LLM-SR [Kamienny et al., 2024], MOBLLM [Binbas et al., 2024]|


solved from first principles, rather than relying on pre-built tools. This grants the agent maximum flexibility, allowing it to handle a wide array of structured data formats like tabular data, text, and numerical arrays to perform bespoke analyses. For example, Data Interpreter translates natural language queries into Python scripts, using libraries like Pandas and Matplotlib within a secure code interpreter to execute a full data science workflow from cleaning to visualization [Hong et al., 2024]. In the realm of fundamental science, frameworks like LLM-SR and MOBLLM use the agent’s code generation capabilities to perform symbolic regression—discovering the underlying mathematical equations that describe experimental data [Kamienny et al., 2024, Binbas et al., 2024].

The key challenges here are technical and philosophical: the risk of "code hallucination" (generating incorrect or inefficient code), the difficulty of scaling logical reasoning for highly complex problems, and the fundamental question of verifying whether an agent is making a novel discovery versus merely recalling a similar solution from its vast training data.

###### 5.2 Iterative Result Validation and Refinement

Scientific discovery rarely concludes after a single iteration of experiments. The iterative result refinement and validation phase emerges as a crucial mechanism for enhancing scientific outcomes. This stage involves multiple iterative cycles, each focused on carefully reviewing the results from previous stages, identifying discrepancies or unexpected findings, and methodically refining experimental procedures, computational models, or analytical techniques. Activities such as debugging computational workflows to detect and correct errors and systematically verifying adherence to established experimental protocols are essential to this process. Each iteration provides valuable feedback that informs subsequent improvements, thereby progressively aligning experimental outcomes with original hypotheses and research objectives. Concurrently, validation rigorously compares results against established scientific knowledge, predefined benchmarks, and reproducibility standards, ensuring the reliability, accuracy, and integrity of the scientific conclusions drawn.

Refinement within LLM-based systems typically uses three major strategies: automatic selfcorrection, external evaluation and feedback, and human-in-the-loop approaches (Figure 10).

Automatic Self-correction. Automatic self-correction employs introspective and self-debugging strategies, prompting LLMs to iteratively evaluate and refine their own outputs. This method typically involves the use of specialized prompts that encourage models to critique and revise their responses based on internal reasoning. For example, the Self-Refine framework [Madaan et al., 2023] has shown significant improvements in reasoning tasks by enabling LLMs to critique and iteratively refine their responses. Additionally, frameworks such as those explored by Chen et al. [2023b] highlight how iterative introspection significantly enhances code-generation accuracy. Within scientific LLM agents, ChemAgent uses dynamic memory retrieval to self-correct and refine reasoning based on prior experiences [Tang et al., 2025]. SpatialAgent [Wang et al., 2025a] relies on chain-of-thought reasoning and self-reflection to iteratively refine plans to achieve specific goals. Team of AI-made Scientists (TAIS) [Liu et al., 2024a] uses multiple LLMs as distinct agents that provide feedback to one another, collaboratively refining and improving the overall results. BioInformatics Agent [Xin et al.,

- 2024] first summarizes and analyzes the results from the initial run, compares them with the user’s expected outcomes, and then modifies the entire workflow to better align with the user’s objectives.


Start Reﬁnement Cycle

External Evaluation and Feedback

Automatic Self-Correction

Human-in-the-Loop Approaches

Feedback Feedback Feedback

Continuous Reﬁnement Loop

Reﬁne Agent

Increasing Validation Difﬁculty

- Figure 10: A diagram of the scientific agent’s continuous refinement cycle, which employs a progressive validation strategy. The process escalates through three stages as the difficulty of verifying the results increases. It begins with internal Automatic Self-Correction, moves to validation against tools and data via External Evaluation and Feedback, and for the most challenging cases, incorporates expert judgment through Human-in-the-Loop Approaches.


Recent works incorporate self-verification and self-correction mechanisms into reinforcement learning training to improve the robustness and reasoning capabilities of large language models Zhang et al. [2025c], Jiang et al. [2025], Liu et al. [2025d]. However, self-correction methods alone are often insufficient due to inherent limitations in LLM self-assessment capabilities [Huang et al., 2023].

External Evaluation and Feedback. External evaluation and feedback strategies use tools and automated metrics external to the LLM to objectively validate and refine the model’s outputs. These external methods include computational assessments, fact-checking tools, or specialized domainspecific tools to guide iterative improvement. For instance, the CRITIC framework [Gou et al., 2023] systematically validates LLM outputs using external fact-checking, such as a search engine or a knowledge base. In scientific applications, OSDA Agent [Hu et al., 2025] uses computational chemistry tools to evaluate and iteratively refine molecular structure proposals. Similarly, MAPPS [Zhou et al., 2025a] integrates feedback from scientific computational tools and scientist insights to optimize experimental workflows and enhance discovery outcomes. Besides, the AI co-scientist [Gottweis et al., 2025a] employs an external multi-agent critique approach, facilitating peer-review-style evaluations that iteratively improve scientific hypotheses. BioDiscoveryAgent [Roohani et al., 2024] incorporates the phenotypic score from previous rounds in the prompt to help generate a better set of genes to experimentally perturb. SAMPLE [Rapp et al., 2024] connects with gene assembly, protein expression, and biochemical analysis systems, feeding the results back to refine the agent’s understanding in an iterative loop. Biomni [Huang et al., 2025b] iteratively refines its reasoning using feedback from tools and code execution results.

Human-in-the-Loop. Human-in-the-loop methods integrate direct human expertise and oversight into the LLM refinement process. These methods often involve structured iterative human evaluations, ensuring that outputs align closely with expert standards and real-world applicability. General research has extensively used reinforcement learning from human feedback (RLHF) to guide models toward behaviors reflecting expert evaluations. Within scientific contexts, AI co-scientist [Gottweis et al., 2025a] explicitly integrates human expertise within its iterative "generate, debate, and evolve" framework, ensuring robust scientific outcomes. ResearchAgent [Baek et al., 2024] similarly uses human-aligned reviewing agents to simulate structured peer review, significantly enhancing the feasibility and novelty of scientific research proposals. MAPPS [Zhou et al., 2025a] relies on human scientists to verify the generated workflow to ensure seamless materials discovery, leading to more robust results.

###### 6 Domain-Specific Scientific Agents

A new generation of scientific agents is being developed for fields as diverse as biology, chemistry, and materials science. By integrating and using advanced domain-specific tools, these agents are beginning to tackle challenging discovery tasks such as designing novel molecules, predicting protein structures, and discovering new materials with unprecedented speed.

In genomics, tools such as the UCSC Genome Browser [Kuhn et al., 2013], AlphaGenome [Avsec

- et al., 2025], and Evo2 [Brixi et al., 2025] provide powerful resources for genome annotation, regulatory function prediction, and large-scale genome modeling [Avsec et al., 2021, Nguyen et al.,


- 2024, Su et al., 2025a,b]. In single cell biology, Seurat [Hao et al., 2021] and Scanpy [Wolf et al., 2018] analyze large datasets. For proteomics, the AlphaFold family of models [Jumper and et al., 2021, Abramson et al., 2024] and ESM series [Lin et al., 2023, Hayes et al., 2025] predict protein structures and are increasingly applied in protein design workflows, while Rosetta [Leaver-Fay and et al., 2011, Watson et al., 2023, Dauparas et al., 2022] serves as a versatile library for protein modeling and design and has given rise to some of the most powerful deep learning models in the field. In chemistry, RDKit [Landrum, 2006] processes molecular data, and Q-Chem [Shao and et al., 2006] and Psi4 [Smith et al., 2020] perform quantum chemistry calculations. In materials science, ASE [Larsen and et al., 2017], VASP [Kresse and Furthmüller, 1996], and LAMMPS [Plimpton, 1995, Thompson et al., 2022] simulate molecular and materials behavior. Recently, machine learning is advancing molecular and materials simulation through Machine Learning Interatomic Potentials (MLIPs) and newer methods that directly predict quantum Hamiltonian matrices [Yu et al., 2023a,b,


- 2025]. In physics, tools like OpenFOAM [OpenCFD Ltd, 2024] for fluid dynamics and CIGALE [Noll et al., 2009] for galaxy evolution enable complex simulations. This diverse suite of tools highlights how specialized computational resources are driving scientific discovery forward.


Genomics. The biological sciences have seen explosive growth in autonomous agent development. SpatialAgent [Wang et al., 2025a] runs end-to-end spatial biology studies at scale, autonomously processing 2M+ cells across spatial transcriptomics and MERFISH pipelines to annotate tissue niches and map cell–cell interactions, demonstrating parity or gains against automated baselines while handling full projects with minimal human input. Team of AI-made Scientists (TAIS) [Liu et al.,

- 2024a] is a framework that simulates researchers’ works for genomics by assigning LLM agents specialized roles, including agents to plan the analysis, handle data selection and preprocessing, conduct biomedical research and analytical studies, analyze data statistics and interpret results, and review the quality of codes. Working together, these agents analyze gene expression datasets to identify disease-predictive genes, streamlining the pipeline of gene discovery (from raw data to insights) without human intervention. CRISPR-GPT [Qu et al., 2025] automates gene-editing experiment design—from system and gRNA selection to delivery and validation protocols—and reports successful real-world use translating agent-generated designs into wet-lab execution. BioDiscoveryAgent [Roohani et al., 2024] chooses genes to perturb to achieve a target phenotype, outperforming trained Bayesian-optimization baselines by +21% on average (and +46% on non-essential genes) across six datasets, and doubling the hit-rate for multi-gene combinations over random. PerTurboAgent [Hao et al., 2025] plans iterative Perturb-seq campaigns, predicting next-round gene panels and improving panel quality over static or heuristic baselines in retrospective/simulation studies, thereby shortening cycles in pooled genetic screens. BioAgents [Mehandru et al., 2025] delivers locally runnable, privacy-preserving bioinformatics workflows using multi-agent SLMs with RAG, achieving near-expert performance on conceptual genomics tasks while enabling on-premises customization with proprietary data. Single-cell genomics has also benefited greatly from multiple agent systems. BioInformatics Agent (BIA) [Xin et al., 2024] runs end-to-end scRNA-seq analyses (dimensionality reduction, clustering, DE, enrichment), producing ready-to-use figures and reports with minimal user intervention. scBaseCount [Youngblut et al., 2025] uses an agentic, hierarchical workflow to continuously mine, standardize, and expand a single-cell compendium now exceeding 230 million cells across 21 organisms and 72 tissues, giving downstream agents a harmonized data backbone. CellAgent [Xiao et al., 2024] automates scRNA-seq (and spatial) pipelines end-to-end via planner–executor–evaluator roles, delivering high-quality analyses without human steps and exportable narratives/plots for downstream interpretation. CompBioAgent [Zhang et al., 2025b] provides natural-language exploration of scRNA-seq cohorts, turning user queries into JSON plans and returning targeted summaries and visualizations that lower the barrier for non-computational users. scAgent [Mao et al., 2025] targets universal cell-type annotation and novel-type discovery; across 160 cell types in 35 tissues it reports state-of-the-art accuracy and generalization, including data-efficient


extension to unseen types. CASSIA [Xie et al., 2024] is a multi-agent annotator that produces interpretable cell-type calls with full reports and improves low-quality annotations by retrieving external evidence and consolidating tool outputs into audit-ready documentation. GeneAgent [Wang et al.,

- 2025b] performs gene-set analysis and queries expert-curated biological databases to cross-check its claims, reducing hallucinations and producing auditable rationales for functional descriptions. STAgent [Lin et al., 2025] couples perception, dynamic code generation, tool use, and literature grounding to deliver end-to-end spatial transcriptomics analyses and structured reports with minimal human input. MRAgent [Xu et al., 2025c] automates Mendelian randomization studies end-to-end by triaging literature for exposure–outcome pairs, selecting GWAS, executing MR pipelines, and producing standardized reports. Protein. The protein engineering domain has witnessed significant advances. SAMPLE [Rapp


- et al., 2024] delivers a full closed-loop, self-driving protein engineering pipeline that experimentally discovers thermostable enzyme variants, identifying GH1 hydrolases with ≥12 °C higher stability than the starting sequences via autonomous design–build–test cycles in a robotic lab, rather than manual mutagenesis campaigns. The Virtual Lab [Swanson et al., 2024] pushes from computation to wet-lab outcomes by designing 92 novel SARS-CoV-2 nanobodies and experimentally validating expression and binding across variants (with >90% expression in tested constructs), demonstrating that multi-agent pipelines can translate in-silico designs into viable binders. ProtAgents [Ghafarollahi and Buehler, 2024a] demonstrates de novo proteins tailored to mechanical targets, generating sequences that meet target vibrational-frequency profiles and structural specifications validated through structure prediction and physics-aware analyses—showing agentic design can hit property constraints, not just folds. Sparks [Ghafarollahi and Buehler, 2025] shows agentic discovery can move from instances to general principles, autonomously uncovering two protein-design rules: a length-dependent crossover where β-biased peptides surpass α-helical ones in unfolding force beyond ∼80 residues, and a chain-length/secondary-structure stability map with a high-variance “frustration zone” for α/β folds. VibeGen [Ni and Buehler, 2025] extends this to dynamics-aware design, where a designer–predictor duo produces de novo proteins whose all-atom MD trajectories reproduce prescribed normal-mode amplitudes, expanding beyond evolutionary templates toward motion-tuned biomolecules. AutoProteinEngine (AutoPE) [Liu et al., 2024b] lowers the barrier for biologists by automating model choice, HPO, and data handling; on two real protein-engineering tasks it shows substantial accuracy gains over zero-shot and manual fine-tuning, turning advanced DL pipelines into practical, conversational workflows. ProtChat [Huang et al., 2024b] further streamlines protein analysis tasks into a multiagent workflow by combining a high-level generalist LLM (e.g. GPT-4o) for task-planning, chatting and visualization, with specialized PLMs (e.g. ESM) for protein understanding. PRIME [Zhou
- et al., 2025b] interprets high-level goals and dynamically synthesizes computational workflows for protein engineering by reasoning over a curated library of 65+ validated protein tools, constructing customized pipelines end-to-end.


Medicine. A recent groundbreaking study is Biomni [Huang et al., 2025b], which functions as a general-purpose biomedical agent that actually completes end-to-end analyses—causal gene prioritization, drug repurposing, rare-disease workups, and multi-omics integration—by driving 150+ tools, 105 software packages, and 59 databases, returning ranked candidates with traceable evidence. AI co-scientist [Gottweis et al., 2025b] operationalizes hypothesis-driven research: a Gemini-2.0 multiagent system that turns literature + model feedback (e.g., structure prediction) into novel, testable hypotheses and study proposals with iterative review. TxAgent [Gao et al., 2025b] converts patient context into actionable therapy decisions, using 211 tools for up-to-date interaction checks, contraindications, and personalized regimen selection via multi-step tool-augmented reasoning. Beyond these, BioResearcher [Luo et al., 2025b] demonstrates dry-lab automation end-to-end—from goal → literature synthesis → executable analysis/protocol drafts → reviewer-style critiques—showing measurable gains on complex research objectives without manual “glue code.” STELLA [Jin et al., 2025a] targets the evidence-curation bottleneck in biomedicine with a self-evolving, multi-agent literature analysis workflow that structures large corpora into machine-navigable knowledge to support hypothesis generation/validation. In the domain of drug discovery, CLADD [Lee et al., 2025] coordinates collaborative agents with RAG to design/dock/triage while ingesting heterogeneous biochemical knowledge without fine-tuning, improving task performance over general LLMs and classical DL baselines. DrugAgent [Liu et al., 2024c] automates end-to-end ML programming for ADMET/repurposing tasks (data acquisition → training → evaluation), reporting strong case-study metrics (e.g., PAMPA absorption F1 ≈ 0.92). PharmAgents [Gao et al., 2025d] builds a “virtual pharma” where specialist agents span screening → modeling → triage, outputting prioritized leads with assay-ready

metadata. LIDDiA [Averly et al., 2025] is an autonomous, language-driven discovery agent that generates molecules meeting pharmaceutical criteria on many targets and surfaces promising EGFR candidates, emphasizing low-cost adaptability. AgentMD [Jin et al., 2024a] automatically selects and executes from 2,164 curated clinical calculators (RiskCalcs) to return risk estimates with formula provenance, substantially outperforming strong prompting baselines on RiskQA. MedAgents [Tang

- et al., 2023] delivers multi-specialist deliberation in zero-shot settings to reach consensus diagnoses/plans across standard medical QA suites. ClinicalGPT [Wang et al., 2023b] is a domain LLM for clinical tasks; EHR-integrated agentic examples include EHRAgent, which auto-generates/executes code against EHR data to answer complex patient queries and compute scores. BehaveAgent [Aljovic et al., 2025] provides turn-key cross-species behavior analysis from raw video—planning the analysis, tracking/pose estimation, sequence labeling, and report generation—without retraining across paradigms.

Chemistry. Chemistry has emerged as a particularly fertile ground for autonomous agents. For instance, the agent Coscientist [Boiko et al., 2023] tackled the overarching problem of autonomously designing and executing complex physical experiments from high-level prompts, demonstrating its capability by successfully performing Nobel Prize-winning palladium-catalyzed cross-coupling reactions in under 4 minutes. To broaden the utility of LLMs in chemistry, ChemCrow [M. Bran

- et al., 2024] addressed the challenge of equipping them with specialized knowledge by integrating 18 expert-designed tools, successfully performing autonomous planning and multi-tool analysis across organic synthesis, drug discovery, and materials science. For managing highly complex workflows, ChemAgents [Song et al., 2025] solved the need for distributed expertise by deploying a hierarchical multi-agent system where a manager agent coordinates specialized agents for tasks ranging from literature analysis to robotic operation. Bridging linguistic reasoning with quantum mechanics, ChemReasoner [Sprueill et al., 2024] focused on the difficult task of catalyst discovery by creating a synergistic loop between LLM-driven hypothesis generation and rapid feedback from DFT simulations, thereby accelerating the materials design cycle. To improve accessibility, CACTUS [McNaughton et al., 2024] solved the user-interface problem for complex computational chemistry tools, acting as an intelligent conversational assistant that accurately translates natural language questions into the proper tool calls for property prediction, similarity searches, and toxicity estimation. In the domain of experimental optimization, Chemist-X [Chen et al., 2023a] focused on automating the tedious process of refining reaction conditions, achieving a fully automated, closed-loop system that uses retrieval-augmented generation to propose conditions and then directs a robotic platform for wet-lab validation. In computational chemistry, El Agente Q [Zou et al., 2025] tackled the manual, error-prone steps in computational chemistry, demonstrating how its cognitive architecture could autonomously handle an entire workflow—from file preparation to cluster submission and result parsing—based on a simple natural language prompt. To empower bench chemists, LLM-RDF [Ruan


- et al., 2024] aimed to provide a fully automated synthesis workflow for users without coding expertise, successfully enabling an end-to-end process from literature search to product purification through its conversational, six-agent framework. In the pharmaceutical space, FROGENT [Pan et al., 2025] addressed the complex, end-to-end process of drug design, showing superior performance on multistep discovery benchmarks by integrating diverse biochemical databases and predictive models into a unified framework. LARC [Baker et al., 2025] solved the critical challenge of applying practical, real-world constraints to retrosynthesis planning, employing an Agent-as-a-Judge mechanism to generate more feasible routes and achieving a near-human-level success rate on diverse tasks. FMG [Sun et al., 2025] demonstrates expert-level molecular design can be achieved by adopting graph representations and rendering them as images, highlighting multiple modalities can enable deeper understanding. Finally, addressing the core of scientific inquiry, MOOSE-Chem [Yang et al., 2024] aimed to automate the creative process of hypothesis generation by mimicking human cognition, successfully rediscovering the core innovations from recent high-impact chemistry papers without any prior knowledge of their content.


Materials. The application of scientific agents in materials science has led to innovative solutions for long-standing research challenges, spanning from discovery to synthesis and analysis. The A-Lab [Szymanski et al., 2023] of Lawrence Berkeley National Laboratory represents a fully autonomous materials synthesis facility. Using three robotic arms, box furnaces, and X-ray diffractometers, it synthesized 41 novel compounds from 58 targets over 17 days of continuous operation, achieving a 71% success rate. ChatMOF [Kang and Kim, 2024] addresses the complex scientific problem of discovering novel Metal-Organic Frameworks (MOFs), a process that requires navigating vast chemical databases, predicting properties of hypothetical structures, and generating new candidates.

Its primary scientific contribution is a unified, autonomous workflow that orchestrates these disparate tools, successfully translating high-level goals into a concrete series of actions to accelerate the identification of promising materials for applications like gas storage. Similarly, the “ChatGPT Research Group” [Zheng et al., 2023] tackles the resource-intensive, iterative process of optimizing experimental synthesis conditions for advanced materials. Its achievement is a collaborative multiagent system that mimics a human research team, dividing labor among specialized LLM agents to significantly accelerate the experimental optimization cycle and make the discovery-to-production pipeline more systematic. In the computational domain, MDAgent [Shi et al., 2025] confronts the efficiency bottleneck in Molecular Dynamics (MD) simulations, which are critical for understanding material behavior but require significant user expertise. It automates the entire MD workflow from code generation to execution, achieving a notable scientific result by reducing the total task time for thermodynamic calculations by over 40% and lowering the barrier to entry for performing these complex simulations. To address the limitations of general-purpose LLMs, HoneyComb [Zhang et al.,

- 2024b] solves the problem of their lack of deep, domain-specific knowledge and reliability in scientific computations. It contributes a robust agent framework grounded with a curated materials knowledge base and a hub of validated scientific tools, resulting in significantly higher accuracy in both reasoning and computation. Addressing the grand challenge of inverse design, LLMatDesign [Jia et al., 2024] introduces a framework for autonomous materials discovery, particularly in low-data regimes. Its key scientific achievement is a self-reflection mechanism that allows the agent to learn from computational outcomes and adapt its strategy, enabling the effective discovery of materials with specific, userdefined properties. Meanwhile, MatAgent [Bazgir et al., 2025a] targets the fragmentation and lack of reproducibility in typical materials discovery workflows. It provides an integrated, human-in-theloop multi-agent framework that streamlines the research process, fostering an AI-guided, adaptive laboratory workflow that enhances both the speed and reproducibility of materials research. For managing multi-faceted research projects, MatSciAgent [Chaudhari et al., 2025] solves the challenge of orchestrating diverse computational tasks. It achieves this with a modular architecture where a master agent interprets high-level goals and delegates tasks to specialized sub-agents, creating an extensible and robust system for complex research questions. To better integrate human expertise, MatPilot [Ni et al., 2024] demonstrates a powerful human-machine collaborative framework. It resolves the challenge of seamlessly combining human intuition with AI’s computational power by using multi-agent LLMs for hypothesis generation while allowing human experts to guide the overall strategy, enabling a continuous learning loop. Materials Laws Multi-Agent Framework [Hu et al.,


- 2024] tackles the fundamental scientific goal of distilling complex data into simple, interpretable physical laws. Its major scientific result was the successful use of LLM agents to perform symbolic regression, deriving a low-complexity, highly accurate formula for predicting glass-forming ability in metallic glasses and showcasing the potential of AI to automate scientific law discovery.

Physics. Scientific agents are increasingly being applied to solve complex problems in physics and engineering, demonstrating capabilities ranging from controlling physical hardware to automating sophisticated simulations. In quantum computing, the k-agents framework [Cao et al., 2024] addresses the scientific challenge of automating quantum experiment design and execution, a process that typically requires deep human expertise. Its significant scientific achievement was the creation of a fully autonomous laboratory where LLM agents successfully planned and executed experiments on superconducting quantum processors to produce entangled states at a performance level equivalent to human experts. In materials physics, AtomAgents [Ghafarollahi and Buehler, 2024c] tackles the complex, multi-factorial problem of designing new alloys with specific properties. It contributes a physics-aware, multi-agent framework that successfully integrates knowledge retrieval with physicsbased simulations in an iterative loop, enabling the system to autonomously propose, simulate, and refine alloy compositions to meet performance targets. In astrophysics, Mephisto [Sun et al., 2024] solves the complex inverse problem of interpreting multi-band galaxy observations to determine their physical properties. Its key result is a multi-agent framework that automates this by calling the CIGALE astrophysics code as a tool, successfully proposing and testing hypotheses against observational data in an iterative reasoning loop. In quantum instrumentation, QCopilot [Sha et al.,

- 2025] confronts the challenge of designing and diagnosing highly sensitive quantum sensors, a process that involves time-consuming manual parameter tuning. It achieved a remarkable 100-fold speedup over manual procedures by autonomously performing modeling, optimization, and anomaly detection in atom cooling experiments. In computational fluid dynamics (CFD), OpenFOAMGPT [Pandey


- et al., 2025] solves the problem of the steep learning curve and tedious setup process associated with complex simulation software like OpenFOAM. It successfully automates the entire workflow,


from case setup to iterative correction, significantly lowering the barrier to entry for advanced CFD. MetaOpenFOAM [Chen et al., 2024b] further addresses the need for robust and generalized CFD automation by using a multi-agent system to decompose complex natural language instructions, achieving strong performance across a diverse range of flow simulations. Finally, to address the critical need for interpretability in scientific AI, the AI-Scientist Framework [Xu et al., 2025a] introduces a multi-agent system that structures LLM outputs into transparent, executable models. Its main contribution is enhancing systematic validation and human-AI collaboration by making the agent’s reasoning process physically grounded and verifiable.

Other Science and Engineering. Beyond the foundational scientific disciplines, scientific agents are driving significant advancements in a range of other scientific and engineering fields. The Autonomous GIS Agent [Ning et al., 2025] and its successor GIS Copilot [Akinboyewa et al., 2025] address the accessibility barrier in geospatial science, where answering spatial questions often requires specialized programming skills. They successfully automated workflows from data retrieval to the generation of maps and statistics by translating natural language requests into executable programs, making advanced geospatial analysis more accessible. For complex engineering systems, the domain-specific ReAct agent for gas turbines [Song et al., 2024] tackles the challenge of modeling and analyzing the thermodynamics of multi-component systems. It successfully integrated expert knowledge with predefined tools to perform iterative gas path analysis, demonstrating a viable path for AI-driven diagnostics in power engineering. LP-COMDA [Liu et al., 2024d] extends agent applications to power electronics, solving the challenge of designing complex and error-prone modulation strategies for power converters. It successfully automated this process with a physics-informed planner, accelerating design time by over 30x while reducing errors by over 60%.

###### 7 Discussions

###### 7.1 From LLM Reasoning to Agentic Reasoning via Reinforcement Learning

The advent of Large Language Models (LLMs) has brought the promise of automating complex tasks, but Reinforcement Learning (RL) plays a crucial role in transitioning from passive text generation to active decision-making and discovery. While Supervised Fine-Tuning (SFT) can enhance domain knowledge and change model behaviors, it is fundamentally a form of imitation learning, limiting a model’s ability to generalize to new domains [Chu et al., 2025] and explore more optimal or diverse problem-solving strategies. Reinforcement Learning, particularly from verifiable rewards, provides a fundamental solution [Parashar et al., 2025, Su et al., 2025c, Li et al., 2024b,

- 2025b] to elicit generalizable reasoning ability from the base policy model. Work exemplified by DeepSeek-R1 [Guo et al., 2025] demonstrates that models can learn complex reasoning behaviors, including self-verification and self-correction, by being rewarded solely from final answer correctness. These emergent capabilities reveal RL’s potential for transforming LLMs from passive knowledge repositories into active problem solvers.


The agentic RL paradigm extends model behaviors from pure reasoning to actionable interactions with environments, where agents learn to dynamically interleave reasoning and tool execution. Through RL, agents optimize not just what to think, but when and how to act. Code interpreters enhance mathematical abilities [Feng et al., 2025b, Mai et al., 2025] of agents, with agents learning through RL to optimize reasoning trajectories via multi-turn real-time code execution. Search engines enable agents to acquire external knowledge and up-to-date information, where RL helps agents generate effective search queries as part of their reasoning process [Jin et al., 2025b, Chen et al., 2025c]. Beyond augmenting capabilities, agentic RL also enables models to operate in complex, dynamic environments. Web browsing agents [Wei et al., 2025c, Qi et al., 2025] and GUI agents [Qin et al.,

- 2025, Agashe et al., 2024] position models in human-like scenarios, requiring them to interact with environments where states change in response to their actions. Agentic RL foster the model capability in handling continuous perception, decision-making, and action execution in response to environmental feedback. Beyond a single tool, RL also trains agents to coordinate multiple tools concurrently to solve harder tasks like deep research [Geng et al., 2025, Li et al., 2025c].


Applying the successful Agentic RL methods to scientific discovery is a promising way for realizing an AI-driven scientific revolution. However, the unique nature of the scientific domain presents challenges that far exceed those in existing work.

The Environment Problem. The environment for a Science Agent is an unavoidably heterogeneous hybrid. The system parses outputs from diverse digital tools with non-standard interfaces (e.g., command-line software, database APIs, graphical user interfaces) and interacts directly with physical laboratory equipment such as robotic arms and chemical synthesizers. The introduction of the physical world brings with it latency, noise, irreversible actions, and the risk of hardware damage—challenges that purely digital agents have never faced.

The Action Problem. The action space for a Science Agent, however, is enormous and non-standard, as the actions to control a mass spectrometer are entirely different from those to call a data analysis library. More importantly, an advanced Science Agent is expected not only to use tools, but also to create new ones by writing code. This expands the action space from a finite set to the near-infinite space of all possible programs, posing a massive challenge for exploration-based RL. While the Agent RL Scaling Law study reveals that performance scales with the number of interactions, the astronomical number of interactions required to effectively explore the explosive action space of a Science Agent is practically infeasible.

The Observation Problem. A Science Agent needs to process mixed-modality observations, including experimental images, mass spectrometry data, simulation curves, structured data like SMILES chemical formulas, and unstructured text from scientific papers. Furthermore, research projects have long durations, requiring the agent to possess long-term memory capabilities to connect a serendipitous finding from months ago to a current problem. This far exceeds the capacity of existing agents that primarily rely on short-term context for decision-making and places extreme demands on the model’s memory and retrieval systems.

The Reward Problem. All successful Agent RL works rely on a clear, sparse, but definitive final reward signal, such as whether a math problem is correct, a web task is completed, or a question is answered correctly [Jin et al., 2025b, Wei et al., 2025c, Chen et al., 2025d]. This paradigm almost completely breaks down in scientific discovery. The reward is highly sparse, as a true discovery can take years, and the outcome of a single experiment does not serve as an effective reward signal [Uehara et al., 2025a,b]. The objective of success is also ambiguous. Designing a reward function that can measure novelty, impact, or reproducibility is a major, unresolved problem. Although the self-evolving curriculum proposed in WebRL offers a promising direction by generating easier sub-tasks from failures, it is still confined to tasks with clear success criteria. For open-ended scientific exploration, defining and calculating the reward remains the most central obstacle on the path to a general-purpose Science Agent.

###### 7.2 The Leap from LLMs to Agents in Autonomous Scientific Discovery

LLMs are primarily seen as powerful reasoning engines, like our human brain. Trained on vast amounts of data, they excel at processing, analyzing, and verifying existing human knowledge. However, even if an LLM could propose a novel, unconventional hypothesis, it lacks the ability to physically interact with the world to verify its own ideas. It is not able to design experiments, conduct tests, or observe real-world results, which are essential steps for turning a hypothesis into a validated discovery. This limitation is visually depicted in the Figure 11, where the LLM is trapped inside the Humanity’s Knowledge Closure. It performs efficient reasoning within the existing circle of knowledge but struggles to cross this boundary to reach New Discoveries.

To overcome this challenge, the LLM needs to evolve from a passive reasoning engine into an active scientific agent. As Kambhampati [2025] emphasizes, human can interact with the world and explore new knowledge, and a complete scientific agent should also possess this ability. From an information-theoretic perspective, as detailed in Section 2.3.1, the agent’s internal entropy reduction is fundamentally dependent on irreversible interactions with the physical world. The necessary constraining information cannot be generated internally but must be obtained from real-world processes to truly reduce the hypothesis space.

A scientific agent can not only process data but also design and execute experiments, actively exploring unknown domains. They can acquire new data through trial and error, observation, and hands-on actions, much like a human scientist, rather than solely relying on existing information. A scientific agent is no longer a passive recipient of information; it can translate its internal knowledge (explicit facts, procedural models, etc.) into concrete actions in the real world. This action-feedback

New Discoveries Inferable Knowledge

t

n

e

g

A

c

ﬁ

i

t

n

e

i

LLM LLM

c

S

Humanity’s Collective Knowledge

LLM

LLM

(Explicit Facts, Procedural Models and Veriﬁers)

Humanity’s Knowledge Closure

- Figure 11: A conceptual model illustrating the limitation of a Large Language Model (LLM) compared to the potential of a Scientific Agent. An LLM, acting purely as a reasoning engine, is fundamentally confined within Humanity’s Knowledge Closure. It excels at processing and making connections within the space of existing and Inferable Knowledge but struggles to generate truly novel insights that lie outside this boundary. In contrast, a Scientific Agent is designed to overcome this limitation. By actively interacting with the world—designing experiments, executing actions, and employing exploration strategies—it can break through the knowledge closure to produce genuinely New Discoveries, thereby expanding the frontier of human understanding. This discussion was motivated by and adapted from Kambhampati [2025], and the figure is expanded and recreated with permission.


loop allows the agent to continuously break through the boundaries of inferable knowledge, gradually expanding the circle of human knowledge.

In this way, an LLM-driven scientific agent will no longer be merely an extension of human thought but can become an independent, exploratory pioneer. It can assist humans in efficiently exploring the frontiers of inferable knowledge and may even, through a chance deviation, help humanity discover entirely new insights and groundbreaking discoveries that truly lie beyond the current knowledge closure.

###### 7.3 Role of Serendipity in Discovery

An essential aspect of scientific discovery is the inherent unpredictability and the role that chance and unexpected findings play in significant breakthroughs. Historical milestones, such as the discovery of penicillin, cosmic microwave background radiation, and graphene, highlight how serendipitous findings are pivotal in driving scientific advancement. This phenomenon underscores a crucial gap between human-driven scientific inquiry and current capabilities of LLM-based science agents.

LLMs are trained to maximize likelihood based on extensive historical data, inherently optimizing towards predictable and probable outcomes. Such a training objective inadvertently constrains the models’ abilities to venture into the realms of randomness and serendipity that frequently yield novel insights in human science. Major historical scientific breakthroughs, such as the discovery of penicillin [Fleming, 1929], cosmic microwave background radiation [Penzias and Wilson, 1965], and graphene [Novoselov et al., 2004], often originated from chance or unexpected observations that break free from the confines of pure logical deduction. Consequently, purely likelihood-driven agents might overlook unconventional hypotheses or unexpected patterns that do not align closely

with existing data distributions. To bridge this gap, specific mechanisms or design principles could be integrated into LLM-based science agents to better accommodate chance and unexpected discoveries. For instance, stochastic exploration strategies could be employed to occasionally deviate from the highest probability outputs, thereby simulating the conditions under which human scientists encounter serendipitous results.

###### 8 Summary and Outlook

The emergence of LLM-based agents represents a substantial step forward in the automation and acceleration of scientific discovery. By addressing critical limitations inherent to traditional humandriven approaches and reinforcement learning-based computational agents, LLM-driven methods provide a unified and highly flexible framework capable of operating seamlessly across human intent, natural language, computer language, and physical information. This unified capacity significantly enhances the adaptability, scalability, and generalizability of scientific agents, enabling dynamic engagement across all stages of the discovery lifecycle.

As scientific inquiry continues to confront increasingly complex challenges and larger volumes of data, the continued development and refinement of LLM-based scientific agents become essential. Future research should focus on overcoming existing limitations, such as better understanding physical laws, integrating robust mechanisms for using physical tools, and designing sophisticated interactions with experimental environments and physical instrumentation. Such advancements will further strengthen the capabilities of scientific agents, promoting deeper collaboration between humans and computational intelligence. Ultimately, the ongoing evolution of LLM-based agents holds the promise of revolutionizing scientific discovery, enabling unprecedented efficiency, adaptability, and creativity in generating novel, transformative insights across all scientific disciplines.

###### Acknowledgments

The authors thank Ms. Xiaomeng Fu for the professional graphic design support. S.J. gratefully acknowledges support from the National Science Foundation under grants IIS-2243850, MOMS2331036, and CNS-2328395; the Advanced Research Projects Agency for Health under grant 1AY1AX000053; and the National Institutes of Health under grant U01AG070112. Additional support to S.J. was provided by the Texas A&M Institute of Data Science, the Truchard Family Endowed Chair, the Presidential Impact Fellowship, and the Chancellor EDGES Fellowship at Texas A&M University. W.W. gratefully acknowledges support from the National Science Foundation under grants 2106859, 2119643, 2200274, 2202693, 2312501; the National Institute of Health under grants U54OD036472, U54HG012517, U24DK097771, OT2OD038003; the United States Department of Agriculture under grant 13434200; as well as support from Amazon, NEC, and Optum AI. X.Q. gratefully acknowledges support from the National Science Foundation under grants CMMI-2226908, DMR-2103842, and DMR-1753054; the Air Force Office of Scientific Research under grant FA9550-24-1-0207; and partial support by the donors of ACS Petroleum Research Fund under grant #65502-ND10.

###### References

Xuan Zhang, Limei Wang, Jacob Helwig, Youzhi Luo, Cong Fu, Yaochen Xie, ..., and Shuiwang Ji. Artificial intelligence for science in quantum, atomistic, and continuum systems. Foundations and Trends in Machine Learning, 18(4):385–912, 2025a.

Hanchen Wang, Tianfan Fu, Yuanqi Du, Wenhao Gao, Kexin Huang, Ziming Liu, Payal Chandak, Shengchao Liu, Peter Van Katwyk, Andreea Deac, et al. Scientific discovery in the age of artificial intelligence. Nature, 620(7972):47–60, 2023a.

Paul Adrien Maurice Dirac. Quantum mechanics of many-electron systems. Proceedings of the Royal Society of London. Series A, 123(792):714–733, 1929.

Lev Davidovich Landau and Evgenii Mikhailovich Lifshitz. Quantum mechanics: non-relativistic theory, volume 3. Elsevier, 2013a.

David Tong. Quantum Mechanics. Lectures on Theoretical Physics. Cambridge University Press, 2025a. ISBN 9781009594820.

Lev Davidovich Landau and Evgenii Mikhailovich Lifshitz. Fluid mechanics: course of theoretical physics, volume 6. Elsevier, 2013b.

David Tong. Fluid Mechanics. Lectures on Theoretical Physics. Cambridge University Press, 2025b. ISBN 9781009594691.

Yongjun Xu, Fei Wang, Zhulin An, Qi Wang, and Zhao Zhang. Artificial intelligence for sciencebridging data to wisdom. Innovation, 4(6):100525, 2023. doi: 10.1016/j.xinn.2023.100525.

Hiroaki Kitano. Nobel turing challenge: creating the engine for scientific discovery. npj Systems Biology and Applications, 7:29, 2021. doi: 10.1038/s41540-021-00189-3.

Nina Miolane. The fifth era of science: Artificial scientific intelligence. PLoS Biology, 23(6): e3003230, 2025. doi: 10.1371/journal.pbio.3003230.

Sathya R. Chitturi, Akash Ramdas, Yue Wu, Willie Neiswanger, Daniel Ratner, et al. Targeted materials discovery using bayesian algorithm execution. npj Computational Materials, 10:156,

2024. doi: 10.1038/s41524-024-01326-2.

Mourad Gridach, Jay Nanavati, Khaldoun Zine El Abidine, Lenon Mendes, and Christina Mack. Agentic ai for scientific discovery: A survey of progress, challenges, and future directions. arXiv preprint arXiv:2503.08979, 2025a.

Nathan J Szymanski, Bernardus Rendy, Yuxing Fei, Rishi E Kumar, Tanjin He, David Milsted, Matthew J McDermott, Max Gallant, Ekin Dogus Cubuk, Amil Merchant, et al. An autonomous laboratory for the accelerated synthesis of novel materials. Nature, 624(7990):86–91, 2023.

Alireza Ghafarollahi and Markus J Buehler. Protagents: protein discovery via large language model multi-agent collaborations combining physics and machine learning. Digital Discovery, 3(7): 1389–1409, 2024a.

Haoyang Liu, Yijiang Li, Jinglin Jian, Yuxuan Cheng, Jianrong Lu, Shuyi Guo, Jinglei Zhu, Mianchen Zhang, Miantong Zhang, and Haohan Wang. Toward a team of ai-made scientists for scientific discovery from gene expression data. arXiv preprint arXiv:2402.12391, 2024a.

Kexin Chen, Junyou Li, Kunyi Wang, Yuyang Du, Jiahui Yu, Jiamin Lu, Lanqing Li, Jiezhong Qiu, Jianzhang Pan, Yi Huang, et al. Chemist-x: large language model-empowered agent for reaction condition recommendation in chemical synthesis. arXiv preprint arXiv:2311.10776, 2023a.

Juraj Gottweis, Wei-Hung Weng, Alexander Daryin, Tao Tu, Anil Palepu, Petar Sirkovic, Artiom Myaskovsky, Felix Weissenberger, Keran Rong, Ryutaro Tanno, Khaled Saab, Dan Popovici, Jacob Blum, Fan Zhang, Katherine Chou, Avinatan Hassidim, Burak Gokturk, Amin Vahdat, Pushmeet Kohli, Yossi Matias, Andrew Carroll, Kavita Kulkarni, Nenad Tomasev, Yuan Guan, Vikram Dhillon, Eeshit Dhaval Vaishnav, Byron Lee, Tiago R D Costa, José R Penadés, Gary Peltz, Yunhan Xu, Annalisa Pawlosky, Alan Karthikesalingam, and Vivek Natarajan. Towards an ai co-scientist, 2025a. URL https://arxiv.org/abs/2502.18864.

Chris Beeler, Sriram Ganapathi Subramanian, Kyle Sprague, Mark Baula, Nouha Chatti, Amanuel Dawit, Xinkai Li, Nicholas Paquin, Mitchell Shahen, Zihan Yang, et al. Chemgymrl: A customizable interactive framework for reinforcement learning for digital chemistry. Digital Discovery, 3 (4):742–758, 2024.

Marco Maurizi, Derek Xu, Yu-Tong Wang, Desheng Yao, David Hahn, Mourad Oudich, Anish Satpati, Mathieu Bauchy, Wei Wang, Yizhou Sun, et al. Inverse designing metamaterials with programmable nonlinear functional responses in graph space. arXiv preprint arXiv:2408.06300, 2024.

Pankaj Rajak, Aravind Krishnamoorthy, Ankit Mishra, Rajiv Kalia, Aiichiro Nakano, and Priya Vashishta. Autonomous reinforcement learning agent for chemical vapor deposition synthesis of quantum materials. npj Computational Materials, 7(1):108, 2021.

Oliver J Dressler, Philip D Howes, Jaebum Choo, and Andrew J deMello. Reinforcement learning for dynamic microfluidic control. ACS omega, 3(8):10084–10091, 2018.

Tung-Che Liang and Zhanwei Zhong. Adaptive droplet routing in digital microfluidic biochips using deep reinforcement learning. In Proceedings of the 37th International Conference on Machine Learning, 2020.

Renqian Luo, Liai Sun, Yingce Xia, Tao Qin, Sheng Zhang, Hoifung Poon, and Tie-Yan Liu. Biogpt: Generative pre-trained transformer for biomedical text generation and mining, 2022.

Alexander Dunn, Bernardino Romera-Paredes, Pushmeet Kohli, et al. Foundational models for scientific discovery. Nature, 633(8031):772–784, 2024.

Yue Huang, Lichao Sun, Haoran Wang, Siyuan Wu, Qihui Zhang, Yuan Li, Chujie Gao, Yixin Huang, Wenhan Lyu, Yixuan Zhang, et al. Trustllm: Trustworthiness in large language models. arXiv preprint arXiv:2401.05561, 2024a.

Carl Edwards, Chi Han, Gawon Lee, Thao Nguyen, Chetan Kumar Prasad, Sara Szymkuc, Bartosz A. Grzybowski, Bowen Jin, Ying Diao, Jiawei Han, Ge Liu, Hao Peng, Martin D. Burke, and Heng Ji. mclm: A function-infused and synthesis-friendly modular chemical language model. In arxiv, 2025.

Yu Zhang, Xiusi Chen, Bowen Jin, Sheng Wang, Shuiwang Ji, Wei Wang, and Jiawei Han. A comprehensive survey of scientific large language models and their applications in scientific discovery. In Conference on Empirical Methods in Natural Language Processing, pages 8783– 8817, 2024a.

Chandan K Reddy and Parshin Shojaee. Towards scientific discovery with generative ai: Progress, opportunities, and challenges. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 39, pages 28601–28609, 2025.

Lei Wang, Chen Ma, Xueyang Feng, Zeyu Zhang, Hao Yang, Jingsen Zhang, Zhiyuan Chen, Jiakai Tang, Xu Chen, Yankai Lin, et al. A survey on large language model based autonomous agents. Frontiers of Computer Science, 18(6):186345, 2024a.

Taicheng Guo, Xiuying Chen, Yaqi Wang, Ruidi Chang, Shichao Pei, Nitesh V Chawla, Olaf Wiest, and Xiangliang Zhang. Large language model based multi-agents: A survey of progress and challenges. arXiv preprint arXiv:2402.01680, 2024.

Grégoire Mialon, Roberto Dessì, Maria Lomeli, Christoforos Nalmpantis, Ram Pasunuru, Roberta Raileanu, Baptiste Rozière, Timo Schick, Jane Dwivedi-Yu, Asli Celikyilmaz, et al. Augmented language models: a survey. arXiv preprint arXiv:2302.07842, 2023.

Shanghua Gao, Ada Fang, Yepeng Huang, Valentina Giunchiglia, Ayush Noori, Jonathan Richard Schwarz, Yasha Ektefaie, Jovana Kondic, and Marinka Zitnik. Empowering biomedical discovery with AI agents. Cell, 187(22):6125–6151, 2024.

Shuo Ren, Pu Jian, Zhenjiang Ren, Chunlin Leng, Can Xie, and Jiajun Zhang. Towards scientific intelligence: A survey of LLM-based scientific agents. arXiv preprint arXiv:2503.24047, 2025.

Jiaqi Wei, Yuejin Yang, Xiang Zhang, Yuhan Chen, Xiang Zhuang, Zhangyang Gao, Dongzhan Zhou, Guangshuai Wang, Zhiqiang Gao, Juntai Cao, et al. From ai for science to agentic science: A survey on autonomous scientific discovery. arXiv preprint arXiv:2508.14111, 2025a.

Terry Jingchen Zhang, Yongjin Yang, Yinya Huang, Sirui Lu, Bernhard Schölkopf, and Zhijing Jin. Collective intelligence: On the promise and reality of multi-agent systems as a key catalyst for ai-driven scientific discovery.

Tianshi Zheng, Zheye Deng, Hong Ting Tsang, Weiqi Wang, Jiaxin Bai, Zihao Wang, and Yangqiu Song. From automation to autonomy: A survey on large language models in scientific discovery. arXiv preprint arXiv:2505.13259, 2025.

Ziming Luo, Zonglin Yang, Zexin Xu, Wei Yang, and Xinya Du. Llm4sr: A survey on large language models for scientific research. arXiv preprint arXiv:2501.04306, 2025a.

Jinhyuk Lee, Wonjin Yoon, Sungdong Kim, Donghyeon Kim, Sunkyu Kim, Chan Ho So, and Jaewoo Kang. Biobert: a pre-trained biomedical language representation model for biomedical text mining. Bioinformatics, 36(4):1234–1240, 2020.

Ross Taylor, Marcin Kardas, Guillem Cucurull, Thomas Scialom, Anthony Hartshorn, Elvis Saravia, Andrew Paster, Oana-Eugen Ganea, Peter Gray, and Murali Kambadur. Galactica: A large language model for science, 2022.

Siddharth M Narayanan, James D Braza, Ryan-Rhys Griffiths, Albert Bou, Geemi Wellawatte, Mayk Caldas Ramos, Ludovico Mitchener, Samuel G Rodriques, and Andrew D White. Training a scientific reasoning model for chemistry. arXiv preprint arXiv:2506.17238, 2025.

Zihan Zhao, Da Ma, Lu Chen, Liangtai Sun, Zihao Li, Yi Xia, Bo Chen, Hongshen Xu, Zichen Zhu, Su Zhu, et al. Developing chemdfm as a large language foundation model for chemistry. Cell Reports Physical Science, 6(4), 2025.

Kristian G Barman, Sascha Caron, Emily Sullivan, Henk W de Regt, Roberto Ruiz de Austri, Mieke Boon, Michael Färber, Stefan Fröse, Tobias Golling, Luis G Lopez, et al. Large physics models: towards a collaborative approach with large language models and foundation models. The European Physical Journal C, 85(9):1066, 2025.

Namkyeong Lee, Edward De Brouwer, Ehsan Hajiramezanali, Tommaso Biancalani, Chanyoung Park, and Gabriele Scalia. Rag-enhanced collaborative llm agents for drug discovery. arXiv preprint arXiv:2502.17506, 2025.

Elliot Xie, Lingxin Cheng, Jack Shireman, Yujia Cai, Jihua Liu, Chitrasen Mohanty, Mahua Dey, and Christina Kendziorski. Cassia: a multi-agent large language model for reference free, interpretable, and automated cell annotation of single-cell rna-sequencing data. bioRxiv, pages 2024–12, 2024.

Zengyi Gao, Yukun Cao, Hairu Wang, Ao Ke, Yuan Feng, Xike Xie, and S Kevin Zhou. Frag: A flexible modular framework for retrieval-augmented generation based on knowledge graphs. arXiv preprint arXiv:2501.09957, 2025a.

Ivan Lopez, Akshay Swaminathan, Karthik Vedula, Sanjana Narayanan, Fateme Nateghi Haredasht, Stephen P Ma, April S Liang, Steven Tate, Manoj Maddali, Robert Joseph Gallo, et al. Clinical entity augmented retrieval for clinical information extraction. npj Digital Medicine, 8(1):45, 2025.

Kexin Chen, Hanqun Cao, Junyou Li, Yuyang Du, Menghao Guo, Xin Zeng, Lanqing Li, Jiezhong Qiu, Pheng Ann Heng, and Guangyong Chen. An autonomous large language model agent for chemical literature data mining. arXiv preprint arXiv:2402.12993, 2024a.

Fanqing Meng, Wenqi Shao, Quanfeng Lu, Peng Gao, Kaipeng Zhang, Yu Qiao, and Ping Luo. Chartassisstant: A universal chart multimodal language model via chart-to-table pre-training and multitask instruction tuning. arXiv preprint arXiv:2401.02384, 2024.

Aaron Hurst, Adam Lerer, Adam P Goucher, Adam Perelman, Aditya Ramesh, Aidan Clark, AJ Ostrow, Akila Welihinda, Alan Hayes, Alec Radford, et al. Gpt-4o system card. arXiv preprint arXiv:2410.21276, 2024.

Ghazal Khalighinejad, Sharon Scott, Ollie Liu, Kelly L Anderson, Rickard Stureborg, Aman Tyagi, and Bhuwan Dhingra. Matvix: Multimodal information extraction from visually rich articles. arXiv preprint arXiv:2410.20494, 2024.

- R Odobesku, K Romanova, S Mirzaeva, O Zagorulko, R Sim, R Khakimullin, J Razlivina, A Dmitrenko, and V Vinogradov. Agent-based multimodal information extraction for nanomaterials. npj Computational Materials, 11(1):194, 2025.


Biqing Qi, Kaiyan Zhang, Haoxiang Li, Kai Tian, Sihang Zeng, Zhang-Ren Chen, and Bowen Zhou. Large language models are zero shot hypothesis proposers. arXiv preprint arXiv:2311.05965, 2023.

Guangzhi Xiong, Eric Xie, Corey Williams, Myles Kim, Amir Hassan Shariatmadari, Sikun Guo, Stefan Bekiranov, and Aidong Zhang. Toward reliable scientific hypothesis generation: Evaluating truthfulness and hallucination in large language models. arXiv preprint arXiv:2505.14599, 2025.

Guangzhi Xiong, Eric Xie, Amir Hassan Shariatmadari, Sikun Guo, Stefan Bekiranov, and Aidong Zhang. Improving scientific hypothesis generation with knowledge grounded large language models. arXiv preprint arXiv:2411.02382, 2024.

Agustín Borrego, Danilo Dessì, Daniel Ayala, Inma Hernández, Francesco Osborne, Diego Reforgiato Recupero, Davide Buscaldi, David Ruiz, and Enrico Motta. Research hypothesis generation over scientific knowledge graphs. Knowledge-Based Systems, 315:113280, 2025.

Shrinidhi Kumbhar, Venkatesh Mishra, Kevin Coutinho, Divij Handa, Ashif Iquebal, and Chitta Baral. Hypothesis generation for materials discovery and design using goal-driven and constraint-guided llm agents, 2025a. URL https://arxiv.org/abs/2501.13299.

Haoyang Su, Renqi Chen, Shixiang Tang, Zhenfei Yin, Xinzhe Zheng, Jinzhe Li, Biqing Qi, Qi Wu, Hui Li, Wanli Ouyang, et al. Many heads are better than one: Improved scientific idea generation by a llm-based multi-agent system. arXiv preprint arXiv:2410.09403, 2024.

Daniel Saeedi, Denise Buckner, Jose C Aponte, and Amirali Aghazadeh. Astroagents: A multi-agent ai for hypothesis generation from mass spectrometry data. arXiv preprint arXiv:2503.23170, 2025.

Zonglin Yang, Wanhao Liu, Ben Gao, Tong Xie, Yuqiang Li, Wanli Ouyang, Soujanya Poria, Erik Cambria, and Dongzhan Zhou. Moose-chem: Large language models for rediscovering unseen chemistry scientific hypotheses, 2025. URL https://arxiv.org/abs/2410.07076.

Shiyang Duan, Yuan Tian, Qi Bing, and Xiaowei Shao. Bayes-entropy collaborative driven agents for research hypotheses generation and optimization. arXiv preprint arXiv:2508.01746, 2025.

Haorui Wang, Marta Skreta, Cher-Tian Ser, Wenhao Gao, Lingkai Kong, Felix Strieth-Kalthoff, Chenru Duan, Yuchen Zhuang, Yue Yu, Yanqiao Zhu, et al. Efficient evolutionary search over chemical space with large language models. arXiv preprint arXiv:2406.16976, 2024b.

Kexin Huang, Ying Jin, Ryan Li, Michael Y. Li, Emmanuel Candès, and Jure Leskovec. Automated hypothesis validation with agentic sequential falsifications, 2025a. URL https://arxiv.org/ abs/2502.09858.

Qingyun Wang, Doug Downey, Heng Ji, and Tom Hope. Scimon: Scientific inspiration machines optimized for novelty. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 279–299, 2024c.

Shrinidhi Kumbhar, Venkatesh Mishra, Kevin Coutinho, Divij Handa, Ashif Iquebal, and Chitta Baral. Hypothesis generation for materials discovery and design using goal-driven and constraint-guided llm agents. arXiv preprint arXiv:2501.13299, 2025b.

Haokun Liu, Sicong Huang, Jingyu Hu, Yangqiaoyu Zhou, and Chenhao Tan. Hypobench: Towards systematic and principled benchmarking for hypothesis generation. arXiv preprint arXiv:2504.11524, 2025a.

Yue Gong and Raul Castro Fernandez. Exploiting llms for automatic hypothesis assessment via a logit-based calibrated prior. arXiv preprint arXiv:2506.03444, 2025.

Jinheon Baek, Sujay Kumar Jauhar, Silviu Cucerzan, and Sung Ju Hwang. Researchagent: Iterative research idea generation over scientific literature with large language models. arXiv preprint arXiv:2404.07738, 2024.

Pingchuan Ma, Tsun-Hsuan Wang, Minghao Guo, Zhiqing Sun, Joshua B Tenenbaum, Daniela Rus, Chuang Gan, and Wojciech Matusik. Llm and simulation as bilevel optimizers: A new paradigm to advance physical scientific discovery. arXiv preprint arXiv:2405.09783, 2024.

Kexin Huang, Serena Zhang, Hanchen Wang, Yuanhao Qu, Yingzhou Lu, Yusuf Roohani, Ryan Li, Lin Qiu, Junze Zhang, Yin Di, et al. Biomni: A general-purpose biomedical ai agent. bioRxiv, pages 2025–05, 2025b.

Shanghua Gao, Richard Zhu, Zhenglun Kong, Ayush Noori, Xiaorui Su, Curtis Ginder, Theodoros Tsiligkaridis, and Marinka Zitnik. Txagent: An ai agent for therapeutic reasoning across a universe of tools. arXiv preprint arXiv:2503.10970, 2025b.

Yuanhao Qu, Kaixuan Huang, Ming Yin, Kanghong Zhan, Dyllan Liu, Di Yin, Henry C. Cousins, William A. Johnson, Xiaotong Wang, Mihir Shah, Russ B. Altman, Denny Zhou, Mengdi Wang, and Le Cong. Crispr-gpt for agentic automation of gene-editing experiments. Nature Biomedical Engineering, page 1–14, July 2025. ISSN 2157-846X. doi: 10.1038/s41551-025-01463-z. URL https://www.nature.com/articles/s41551-025-01463-z.

Kyle Swanson, Wesley Wu, Nash L Bulaong, John E Pak, and James Zou. The virtual lab: Ai agents design new sars-cov-2 nanobodies with experimental validation. bioRxiv, pages 2024–11, 2024.

Shuxiang Cao, Zijian Zhang, Mohammed Alghadeer, Simone D Fasciati, Michele Piscitelli, Mustafa Bakr, Peter Leek, and Alán Aspuru-Guzik. Agents for self-driving laboratories applied to quantum computing. arXiv preprint arXiv:2412.07978, 2024.

Minsheng Hao, Yongju Lee, Hanchen Wang, Gabriele Scalia, and Aviv Regev. Perturboagent: A self-planning agent for boosting sequential perturb-seq experiments. bioRxiv, pages 2025–05, 2025.

Botao Yu, Frazier N Baker, Ziru Chen, Garrett Herb, Boyu Gou, Daniel Adu-Ampratwum, Xia Ning, and Huan Sun. Chemtoolagent: The impact of tools on language agents for chemistry problem solving. arXiv preprint arXiv:2411.07228, 2024a.

Qi Xin, Quyu Kong, Hongyi Ji, Yue Shen, Yuqi Liu, Yan Sun, Zhilin Zhang, Zhaorong Li, Xunlong Xia, Bing Deng, et al. Bioinformatics agent (bia): Unleashing the power of large language models to reshape bioinformatics workflow. BioRxiv, pages 2024–05, 2024.

Yusuf Roohani, Andrew Lee, Qian Huang, Jian Vora, Zachary Steinhart, Kexin Huang, Alexander Marson, Percy Liang, and Jure Leskovec. Biodiscoveryagent: An ai agent for designing genetic perturbation experiments. arXiv preprint arXiv:2405.17631, 2024.

Zhaolin Hu, Yixiao Zhou, Zhongan Wang, Xin Li, Weimin Yang, Hehe Fan, and Yi Yang. OSDA agent: Leveraging large language models for de novo design of organic structure directing agents. In The Thirteenth International Conference on Learning Representations, 2025. URL https: //openreview.net/forum?id=9YNyiCJE3k.

Shuyi Jia, Chao Zhang, and Victor Fung. Llmatdesign: Autonomous materials discovery with large language models, 2024.

Jingru Gan, Peichen Zhong, Yuanqi Du, Yanqiao Zhu, Chenru Duan, Haorui Wang, Carla P. Gomes, Kristin A. Persson, Daniel Schwalbe-Koda, and Wei Wang. Large language models are innate crystal structure generators, 2025.

Nicholas D Youngblut, Christopher Carpenter, Jaanak Prashar, Chiara Ricci-Tam, Rajesh Ilango, Noam Teyssier, Silvana Konermann, Patrick D Hsu, Alexander Dobin, David P Burke, et al. scbasecount: an ai agent-curated, uniformly processed, and continually expanding single cell data repository. bioRxiv, pages 2025–02, 2025.

Qiao Jin, Zhizheng Wang, Yifan Yang, Qingqing Zhu, Donald Wright, Thomas Huang, W John Wilbur, Zhe He, Andrew Taylor, Qingyu Chen, et al. Agentmd: Empowering language agents for risk prediction with large-scale clinical tool learning. arXiv preprint arXiv:2402.13225, 2024a.

Andres M. Bran, Sam Cox, Oliver Schilter, Carlo Baldassari, Andrew D White, and Philippe Schwaller. Augmenting large language models with chemistry tools. Nature Machine Intelligence, 6(5):525–535, 2024.

Yuren Mao, Yu Mi, Peigen Liu, Mengfei Zhang, Hanqing Liu, and Yunjun Gao. scagent: Universal single-cell annotation via a llm agent. arXiv preprint arXiv:2504.04698, 2025.

Temitope Akinboyewa, Zhenlong Li, Huan Ning, and M Naser Lessani. Gis copilot: Towards an autonomous gis agent for spatial analysis. International Journal of Digital Earth, 18(1):2497489, 2025.

Huajun Chen, Keyan Ding, Jing Yu, Junjie Huang, Yuchen Yang, and Qiang Zhang. Scitoolagent: A knowledge graph-driven scientific agent for multi-tool integration. 2025a.

Botao Yu, Frazier N Baker, Ziru Chen, Garrett Herb, Boyu Gou, Daniel Adu-Ampratwum, Xia Ning, and Huan Sun. Tooling or not tooling? the impact of tools on language agents for chemistry problem solving. arXiv preprint arXiv:2411.07228, 2024b.

Xiangru Tang, Anni Zou, Zhuosheng Zhang, Ziming Li, Yilun Zhao, Xingyao Zhang, Arman Cohan, and Mark Gerstein. Medagents: Large language models as collaborators for zero-shot medical reasoning. arXiv preprint arXiv:2311.10537, 2023.

Tao Song, Man Luo, Xiaolong Zhang, Linjiang Chen, Yan Huang, Jiaqi Cao, Qing Zhu, Daobin Liu, Baicheng Zhang, Gang Zou, et al. A multiagent-driven robotic ai chemist enabling autonomous chemical research on demand. Journal of the American Chemical Society, 147(15):12534–12545, 2025.

Alireza Ghafarollahi and Markus J. Buehler. Atomagents: Alloy design and discovery through physics-aware multi-modal multi-agent artificial intelligence, 2024b. URL https://arxiv.org/ abs/2407.10022.

Zhiling Zheng, Oufan Zhang, Ha L Nguyen, Nakul Rampal, Ali H Alawadhi, Zichao Rong, Teresa Head-Gordon, Christian Borgs, Jennifer T Chayes, and Omar M Yaghi. Chatgpt research group for optimizing the crystallinity of mofs and cofs. ACS Central Science, 9(11):2161–2170, 2023.

Shanghua Gao, Richard Zhu, Pengwei Sui, Zhenglun Kong, Sufian Aldogom, Yepeng Huang, Ayush Noori, Reza Shamji, Krishna Parvataneni, Theodoros Tsiligkaridis, et al. Democratizing ai scientists using tooluniverse. arXiv preprint arXiv:2509.23426, 2025c.

Lianhao Zhou, Hongyi Ling, Keqiang Yan, Kaiji Zhao, Xiaoning Qian, Raymundo Arróyave, Xiaofeng Qian, and Shuiwang Ji. Toward greater autonomy in materials discovery agents: Unifying planning, physics, and scientists, 2025a. URL https://arxiv.org/abs/2506.05616.

Shanda Li, Tanya Marwah, Junhong Shen, Weiwei Sun, Andrej Risteski, Yiming Yang, and Ameet Talwalkar. Codepde: An inference framework for llm-driven pde solver generation, 2025a. URL https://arxiv.org/abs/2505.08783.

Alexander Novikov, Ngân V˜u, Marvin Eisenberger, Emilien Dupont, Po-Sen Huang, Adam Zsolt Wagner, Sergey Shirobokov, Borislav Kozlovskii, Francisco J. R. Ruiz, Abbas Mehrabian, M. Pawan Kumar, Abigail See, Swarat Chaudhuri, George Holland, Alex Davies, Sebastian Nowozin, Pushmeet Kohli, and Matej Balog. Alphaevolve: A coding agent for scientific and algorithmic discovery, 2025.

Georg Wölflein, Dyke Ferber, Daniel Truhn, Ognjen Arandjelovi´c, and Jakob Nikolas Kather. Llm agents making agent tools. arXiv preprint arXiv:2502.11705, 2025.

Robert Tjarko Lange, Yuki Imajuku, and Edoardo Cetin. Shinkaevolve: Towards open-ended and sample-efficient program evolution. arXiv preprint arXiv:2509.19349, 2025.

Yutaro Yamada, Robert Tjarko Lange, Cong Lu, Shengran Hu, Chris Lu, Jakob Foerster, Jeff Clune, and David Ha. The ai scientist-v2: Workshop-level automated scientific discovery via agentic tree search. arXiv preprint arXiv:2504.08066, 2025.

Yancheng Luo, Zihan Wang, Jingwen Li, Ziqi Min, Kexin Xiao, Howard Liu, and Zijie J. Wang. PlotGen: A New Era of LLM-Based Multi-Agent Framework for Scientific Visualization Generation, 2024.

Yucheng Han, Chi Zhang, Xin Chen, Xu Yang, Zhibin Wang, Gang Yu, Bin Fu, and Hanwang Zhang. Chartllama: A multimodal llm for chart understanding and generation. arXiv preprint arXiv:2311.16483, 2023.

Andres M Bran, Sam Cox, Oliver Schilter, Carlo Baldassari, Andrew D White, and Philippe Schwaller. Chemcrow: Augmenting large-language models with chemistry tools. arXiv preprint arXiv:2304.05376, 2023.

Daniil A Boiko, Robert MacKnight, Ben Kline, and Gabe Gomes. Autonomous chemical research with large language models. Nature, 624(7992):570–578, 2023.

Florian Boeck, Mogens Jørgensen, Jesper Jørgensen, and Nikolaj and-others Båk. A multi-agent llm framework for accelerating materials design. arXiv preprint arXiv:2310.09133, 2023.

Sirui Hong, Yizhang Lin, Bang Liu, Bangbang Liu, Binhao Wu, Ceyao Zhang, Chenxing Wei, Danyang Li, Jiaqi Chen, Jiayi Zhang, et al. Data interpreter: An llm agent for data science. arXiv preprint arXiv:2402.18679, 2024.

Pierre-Alexandre Kamienny, Stéphane D’Ascoli, Guillaume Lample, and François Charton. LLM-SR: A framework for discovering scientific equations with large language models, 2024.

Boran Binbas, Meng-Chen Hsieh, Alán Aspuru-Guzik, Florian E. Futschik, and Mario Krenn. Autonomous scientific discovery with large language models, 2024.

Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, et al. Self-refine: Iterative refinement with self-feedback. Advances in Neural Information Processing Systems, 36:46534–46594, 2023.

Xiangru Tang, Tianyu Hu, Muyang Ye, Yanjun Shao, Xunjian Yin, Siru Ouyang, Wangchunshu Zhou, Pan Lu, Zhuosheng Zhang, Yilun Zhao, Arman Cohan, and Mark Gerstein. Chemagent: Self-updating library in large language models improves chemical reasoning, 2025. URL https: //arxiv.org/abs/2501.06590.

Hanchen Wang, Yichun He, Paula P Coelho, Matthew Bucci, Abbas Nazir, Bob Chen, Linh Trinh, Serena Zhang, Kexin Huang, Vineethkrishna Chandrasekar, et al. Spatialagent: An autonomous ai agent for spatial biology. bioRxiv, pages 2025–04, 2025a.

Zhibin Gou, Zhihong Shao, Yeyun Gong, Yelong Shen, Yujiu Yang, Nan Duan, and Weizhu Chen. Critic: Large language models can self-correct with tool-interactive critiquing. arXiv preprint arXiv:2305.11738, 2023.

Jacob T Rapp, Bennett J Bremer, and Philip A Romero. Self-driving laboratories to autonomously navigate the protein fitness landscape. Nature chemical engineering, 1(1):97–107, 2024.

Nikita Mehandru, Amanda K Hall, Olesya Melnichenko, Yulia Dubinina, Daniel Tsirulnikov, David Bamman, Ahmed Alaa, Scott Saponas, and Venkat S Malladi. Bioagents: Democratizing bioinformatics analysis with multi-agent systems. arXiv preprint arXiv:2501.06314, 2025.

Yihang Xiao, Jinyi Liu, Yan Zheng, Xiaohan Xie, Jianye Hao, Mingzhi Li, Ruitao Wang, Fei Ni, Yuxiao Li, Jintian Luo, et al. Cellagent: An llm-driven multi-agent framework for automated single-cell data analysis. arXiv preprint arXiv:2407.09811, 2024.

Haotian Zhang, Yu H Sun, Wenxing Hu, Xu Cui, Zhengyu Ouyang, Derrick Cheng, Xinmin Zhang, and Baohong Zhang. Compbioagent: An llm-powered agent for single-cell rna-seq data exploration. bioRxiv, pages 2025–03, 2025b.

Alireza Ghafarollahi and Markus J Buehler. Sparks: Multi-agent artificial intelligence model discovers protein design principles. arXiv preprint arXiv:2504.19017, 2025.

Bo Ni and Markus J Buehler. Agentic end-to-end de novo protein design for tailored dynamics using a language diffusion model. arXiv preprint arXiv:2502.10173, 2025.

Yungeng Liu, Zan Chen, Yu Guang Wang, and Yiqing Shen. Autoproteinengine: A large language model driven agent framework for multimodal automl in protein engineering. arXiv preprint arXiv:2411.04440, 2024b.

Huazhen Huang, Xianguo Shi, Hongyang Lei, Fan Hu, and Yunpeng Cai. Protchat: An ai multi-agent for automated protein analysis leveraging gpt-4 and protein language model. Journal of Chemical Information and Modeling, 65(1):62–70, 2024b.

Juraj Gottweis, Wei-Hung Weng, Alexander Daryin, Tao Tu, Anil Palepu, Petar Sirkovic, Artiom Myaskovsky, Felix Weissenberger, Keran Rong, Ryutaro Tanno, et al. Towards an ai co-scientist. arXiv preprint arXiv:2502.18864, 2025b.

Yi Luo, Linghang Shi, Yihao Li, Aobo Zhuang, Yeyun Gong, Ling Liu, and Chen Lin. From intention to implementation: automating biomedical research via llms. Science China Information Sciences, 68(7):1–18, 2025b.

Ruofan Jin, Zaixi Zhang, Mengdi Wang, and Le Cong. Stella: Self-evolving llm agent for biomedical research. arXiv preprint arXiv:2507.02004, 2025a.

Sizhe Liu, Yizhou Lu, Siyu Chen, Xiyang Hu, Jieyu Zhao, Yingzhou Lu, and Yue Zhao. Drugagent: Automating ai-aided drug discovery programming through llm multi-agent collaboration. arXiv preprint arXiv:2411.15692, 2024c.

Bowen Gao, Yanwen Huang, Yiqiao Liu, Wenxuan Xie, Wei-Ying Ma, Ya-Qin Zhang, and Yanyan Lan. Pharmagents: Building a virtual pharma with large language model agents. arXiv preprint arXiv:2503.22164, 2025d.

Reza Averly, Frazier N Baker, Ian A Watson, and Xia Ning. Liddia: Language-based intelligent drug discovery agent. arXiv preprint arXiv:2502.13959, 2025.

Guangyu Wang, Guoxing Yang, Zongxin Du, Longjun Fan, and Xiaohu Li. Clinicalgpt: large language models finetuned with diverse medical data and comprehensive evaluation. arXiv preprint arXiv:2306.09968, 2023b.

Almir Aljovic, Zuwan Lin, Wenbo Wang, Xinhe Zhang, Arnau Marin-Llobet, Ningyue Liang, Bradley Canales, Jaeyong Lee, Jongmin Baek, Ren Liu, et al. An autonomous ai agent for universal behavior analysis. bioRxiv, pages 2025–05, 2025.

Henry W Sprueill, Carl Edwards, Khushbu Agarwal, Mariefel V Olarte, Udishnu Sanyal, Conrad Johnston, Hongbin Liu, Heng Ji, and Sutanay Choudhury. Chemreasoner: Heuristic search over a large language model’s knowledge space using quantum-chemical feedback. arXiv preprint arXiv:2402.10980, 2024.

Andrew D McNaughton, Gautham Krishna Sankar Ramalaxmi, Agustin Kruel, Carter R Knutson, Rohith A Varikoti, and Neeraj Kumar. Cactus: Chemistry agent connecting tool usage to science. ACS omega, 9(46):46563–46573, 2024.

Yunheng Zou, Austin H Cheng, Abdulrahman Aldossary, Jiaru Bai, Shi Xuan Leong, Jorge Arturo Campos-Gonzalez-Angulo, Changhyeok Choi, Cher Tian Ser, Gary Tom, Andrew Wang, et al. El Agente: An autonomous agent for quantum chemistry. Matter, 8(7), 2025.

Yixiang Ruan, Chenyin Lu, Ning Xu, Yuchen He, Yixin Chen, Jian Zhang, Jun Xuan, Jianzhang Pan, Qun Fang, Hanyu Gao, et al. An automatic end-to-end chemical synthesis development platform powered by large language models. Nature communications, 15(1):10160, 2024.

Qihua Pan, Dong Xu, Jenna Xinyi Yao, Lijia Ma, Zexuan Zhu, and Junkai Ji. Frogent: An end-to-end full-process drug design agent. arXiv preprint arXiv:2508.10760, 2025.

Frazier N Baker, Daniel Adu-Ampratwum, Reza Averly, Botao Yu, Huan Sun, and Xia Ning. Larc: Towards human-level constrained retrosynthesis planning through an agentic framework. arXiv preprint arXiv:2508.11860, 2025.

Michael Sun, Weize Yuan, Gang Liu, Wojciech Matusik, and Jie Chen. Foundation molecular grammar: Multi-modal foundation models induce interpretable molecular graph languages. arXiv preprint arXiv:2505.22948, 2025.

Zonglin Yang, Wanhao Liu, Ben Gao, Tong Xie, Yuqiang Li, Wanli Ouyang, Soujanya Poria, Erik Cambria, and Dongzhan Zhou. Moose-chem: Large language models for rediscovering unseen chemistry scientific hypotheses. arXiv preprint arXiv:2410.07076, 2024.

Yeonghun Kang and Jihan Kim. Chatmof: an artificial intelligence system for predicting and generating metal-organic frameworks using large language models. Nature communications, 15

(1):4705, 2024.

Zhuofan Shi, Chunxiao Xin, Tong Huo, Yuntao Jiang, Bowen Wu, Xingyue Chen, Wei Qin, Xinjian Ma, Gang Huang, Zhenyu Wang, et al. A fine-tuned large language model based molecular dynamics agent for code generation to obtain material thermodynamic parameters. Scientific Reports, 15(1):10295, 2025.

Huan Zhang, Yu Song, Ziyu Hou, Santiago Miret, and Bang Liu. Honeycomb: A flexible llm-based agent system for materials science. arXiv preprint arXiv:2409.00135, 2024b.

Adib Bazgir, Yuwen Zhang, et al. Matagent: A human-in-the-loop multi-agent llm framework for accelerating the material science discovery cycle. In AI for Accelerated Materials Design-ICLR 2025, 2025a.

Akshat Chaudhari, Janghoon Ock, and Amir Barati Farimani. Modular large language model agents for multi-task computational materials science. ChemRxiv, 2025.

Ziqi Ni, Yahao Li, Kaijia Hu, Kunyuan Han, Ming Xu, Xingyu Chen, Fengqi Liu, Yicong Ye, and Shuxin Bai. Matpilot: an llm-enabled ai materials scientist under the framework of human-machine collaboration. arXiv preprint arXiv:2411.08063, 2024.

Bo Hu, Siyu Liu, Beilin Ye, Yun Hao, and Tongqi Wen. A multi-agent framework for materials laws discovery. arXiv preprint arXiv:2411.16416, 2024.

Alireza Ghafarollahi and Markus J Buehler. Atomagents: Alloy design and discovery through physics-aware multi-modal multi-agent artificial intelligence. arXiv preprint arXiv:2407.10022, 2024c.

Zechang Sun, Yuan-Sen Ting, Yaobo Liang, Nan Duan, Song Huang, and Zheng Cai. Interpreting multi-band galaxy observations with large language model-based agents. arXiv preprint arXiv:2409.14807, 2024.

Rong Sha, Binglin Wang, Jun Yang, Xiaoxiao Ma, Chengkun Wu, Liang Yan, Chao Zhou, Jixun Liu, Guochao Wang, Shuhua Yan, et al. Llm-based multi-agent copilot for quantum sensor. arXiv preprint arXiv:2508.05421, 2025.

Sandeep Pandey, Ran Xu, Wenkang Wang, and Xu Chu. Openfoamgpt: A retrieval-augmented large language model (llm) agent for openfoam-based computational fluid dynamics. Physics of Fluids, 37(3), 2025.

Yuxuan Chen, Xu Zhu, Hua Zhou, and Zhuyin Ren. Metaopenfoam: an llm-based multi-agent framework for cfd. arXiv preprint arXiv:2407.21320, 2024b.

Yinggan Xu, Hana Kimlee, Yijia Xiao, and Di Luo. Advancing ai-scientist understanding: Making llm think like a physicist with interpretable reasoning. arXiv preprint arXiv:2504.01911, 2025a.

Huan Ning, Zhenlong Li, Temitope Akinboyewa, and M Naser Lessani. An autonomous gis agent framework for geospatial data retrieval. International Journal of Digital Earth, 18(1):2458688, 2025.

Junhua Liu, Fanfan Lin, Xinze Li, Kwan Hui Lim, and Shuai Zhao. Physics-informed llm-agent for automated modulation design in power electronics systems. arXiv preprint arXiv:2411.14214, 2024d.

Tao Song, Yuwei Fan, Chenlong Feng, Keyu Song, Chao Liu, and Dongxiang Jiang. Domain-specific react for physics-integrated iterative modeling: A case study of llm agents for gas path analysis of gas turbines. arXiv preprint arXiv:2406.07572, 2024.

Qingyun Wang, Doug Downey, Heng Ji, and Tom Hope. Scimon: Scientific inspiration machines optimized for novelty. In Proc. The 62nd Annual Meeting of the Association for Computational Linguistics (ACL2024), 2024d.

Xianrui Zhong, Yufeng Du, Siru Ouyang, Ming Zhong, Tingfeng Luo, Qirong Ho, Hao Peng, Heng Ji, and Jiawei Han. Actionie: Action extraction from scientific literature with programming languages. In Proc. The 62nd Annual Meeting of the Association for Computational Linguistics (ACL2024), 2024.

OpenAI. Chatgpt. https://openai.com/chatgpt, 2023. Google. Gemini. https://deepmind.google/technologies/gemini/, 2024. Anthropic. Claude. https://www.anthropic.com/product/claude, 2024. Mohamed Amine Ferrag, Norbert Tihanyi, and Merouane Debbah. From llm reasoning to autonomous

ai agents: A comprehensive review. arXiv preprint arXiv:2504.19678, 2025.

Yadong Zhang, Shaoguang Mao, Tao Ge, Xun Wang, Adrian de Wynter, Yan Xia, Wenshan Wu, Ting Song, Man Lan, and Furu Wei. Llm as a mastermind: A survey of strategic reasoning with large language models. arXiv preprint arXiv:2404.01230, 2024c.

Hui Wei, Zihao Zhang, Shenghua He, Tian Xia, Shijia Pan, and Fei Liu. Plangenllms: A modern survey of llm planning capabilities. arXiv preprint arXiv:2502.11221, 2025b.

Xu Huang, Weiwen Liu, Xiaolong Chen, Xingmei Wang, Hao Wang, Defu Lian, Yasheng Wang, Ruiming Tang, and Enhong Chen. Understanding the planning of llm agents: A survey. arXiv preprint arXiv:2402.02716, 2024c.

Haolin Jin, Linghan Huang, Haipeng Cai, Jun Yan, Bo Li, and Huaming Chen. From llms to llmbased agents for software engineering: A survey of current, challenges and future. arXiv preprint arXiv:2408.02479, 2024b.

Zhuocheng Shen. Llm with tools: A survey. arXiv preprint arXiv:2409.18807, 2024. Wujiang Xu, Kai Mei, Hang Gao, Juntao Tan, Zujie Liang, and Yongfeng Zhang. A-mem: Agentic

memory for llm agents. arXiv preprint arXiv:2502.12110, 2025b.

Yaxiong Wu, Sheng Liang, Chen Zhang, Yichao Wang, Yongyue Zhang, Huifeng Guo, Ruiming Tang, and Yong Liu. From human memory to ai memory: A survey on memory mechanisms in the era of llms. arXiv preprint arXiv:2504.15965, 2025.

YY Yao. Information-theoretic measures for knowledge discovery and data mining. Entropy measures,

maximum entropy principle and emerging applications, pages 115–136, 2003. Claus Borgnakke. Fundamentals of Thermodynamics. Wiley, Hoboken, NJ, 11th edition, 2024. Daniel V Schroeder. An Introduction to Thermal Physics. Oxford University Press, 2020. Colin Patterson. Verifiability in systematics. Systematic Zoology, 27(2):218–222, 1978. Rolf Landauer. Irreversibility and heat generation in the computing process. IBM journal of research

and development, 5(3):183–191, 1961. Don R Swanson. Undiscovered public knowledge. The Library Quarterly, 56(2):103–118, 1986. Kaiyu He and Zhiyu Chen. From reasoning to learning: A survey on hypothesis discovery and rule

learning with large language models. arXiv preprint arXiv:2505.21935, 2025. Maximilian Nickel, Kevin Murphy, Volker Tresp, and Evgeniy Gabrilovich. A review of relational machine learning for knowledge graphs. Proceedings of the IEEE, 104(1):11–33, 2015.

Shaoxiong Ji, Shirui Pan, Erik Cambria, Pekka Marttinen, and Philip S Yu. A survey on knowledge graphs: Representation, acquisition, and applications. IEEE transactions on neural networks and learning systems, 33(2):494–514, 2021.

Suchin Gururangan, Ana Marasovi´c, Swabha Swayamdipta, Kyle Lo, Iz Beltagy, Doug Downey, and Noah A. Smith. Don’t stop pretraining: Adapt language models to domains and tasks. In Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, 2020.

Edward O Pyzer-Knapp, Matteo Manica, Peter Staar, Lucas Morin, Patrick Ruch, Teodoro Laino, John R Smith, and Alessandro Curioni. Foundation models for materials discovery–current state and future directions. Npj Computational Materials, 11(1):61, 2025.

Shashank Subramanian, Peter Harrington, Kurt Keutzer, Wahid Bhimji, Dmitriy Morozov, Michael W Mahoney, and Amir Gholami. Towards foundation models for scientific machine learning: Characterizing scaling and transfer behavior. Advances in Neural Information Processing Systems, 36: 71242–71262, 2023.

Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, et al. Retrieval-augmented generation for knowledge-intensive nlp tasks. In Advances in Neural Information Processing Systems, volume 33, pages 9459–9474, 2020.

Kelvin Guu, Kenton Lee, Zora Tung, Panupong Pasupat, and Mingwei Chang. Retrieval augmented language model pre-training. In International conference on machine learning, pages 3929–3938. PMLR, 2020.

Yunfan Gao, Yun Xiong, Xinyu Gao, Kangxiang Jia, Jinliu Pan, Yuxi Bi, Yixin Dai, Jiawei Sun, Haofen Wang, and Haofen Wang. Retrieval-augmented generation for large language models: A survey. arXiv preprint arXiv:2312.10997, 2(1), 2023.

Gautier Izacard, Patrick Lewis, Maria Lomeli, Lucas Hosseini, Fabio Petroni, Timo Schick, Jane Dwivedi-Yu, Armand Joulin, Sebastian Riedel, and Edouard Grave. Atlas: Few-shot learning with retrieval augmented language models. Journal of Machine Learning Research, 24(251):1–43, 2023.

Wenqi Fan, Yujuan Ding, Liangbo Ning, Shijie Wang, Hengyun Li, Dawei Yin, Tat-Seng Chua, and Qing Li. A survey on rag meeting llms: Towards retrieval-augmented large language models. In Proceedings of the 30th ACM SIGKDD conference on knowledge discovery and data mining, pages 6491–6501, 2024.

Gabriel Lino Garcia, Joao Renato Ribeiro Manesco, Pedro Henrique Paiola, Lucas Miranda, Maria Paola de Salvo, and Joao Paulo Papa. A review on scientific knowledge extraction using large language models in biomedical sciences. arXiv preprint arXiv:2412.03531, 2024.

Yichun Feng, Jiawei Wang, Ruikun He, Lu Zhou, and Yixue Li. A retrieval-augmented knowledge mining method with deep thinking llms for biomedical research and clinical support. GigaScience, 14:giaf109, 2025a.

Nikita A Krotkov, Dmitrii A Sbytov, Anna A Chakhoyan, Polina I Kornienko, Anna A Starikova, Maxim G Stepanov, Anastasiia O Piven, Timur A Aliev, Tetiana Orlova, Mushegh S Rafayelyan, et al. Nanostructured material design via a retrieval-augmented generation (rag) approach: Bridging laboratory practice and scientific literature. Journal of Chemical Information and Modeling, 2025.

Yangqiaoyu Zhou, Haokun Liu, Tejes Srivastava, Hongyuan Mei, and Chenhao Tan. Hypothesis generation with large language models. arXiv preprint arXiv:2404.04326, 2024.

Adib Bazgir, Yuwen Zhang, et al. Proteinhypothesis: A physics-aware chain of multi-agent rag llm for hypothesis generation in protein science. In Towards Agentic AI for Science: Hypothesis Generation, Comprehension, Quantification, and Validation, 2025b.

Song Tong, Kai Mao, Zhen Huang, Yukun Zhao, and Kaiping Peng. Automating psychological hypothesis generation with ai: when large language models meet causal graph. Humanities and Social Sciences Communications, 11(1):1–14, 2024.

Qingyun Wu, Gagan Bansal, Jie Zhang, Yiran Wu, Shaokun Li, Erkang Zhu, Li Jiang, Xiaoyun Zhang, Chi Wang, and Song Han. Autogen: Enabling next-gen llm applications via multi-agent conversation. In Thirty-seventh Conference on Neural Information Processing Systems, 2023. URL https://arxiv.org/abs/2308.08155.

Harrison Chase. Langchain, 10 2022. URL https://github.com/langchain-ai/langchain. Nuo Chen, Yicheng Tong, Jiaying Wu, Minh Duc Duong, Qian Wang, Qingyun Zou, Bryan Hooi,

and Bingsheng He. Beyond brainstorming: What drives high-quality scientific ideas? lessons from multi-agent collaboration. arXiv preprint arXiv:2508.04575, 2025b.

Fei Liu, Xi Lin, Shunyu Yao, Zhenkun Wang, Xialiang Tong, Mingxuan Yuan, and Qingfu Zhang. Large language model for multiobjective evolutionary optimization. In International Conference on Evolutionary Multi-Criterion Optimization, pages 178–191. Springer, 2025b.

Yayati Jadhav and Amir Barati Farimani. Large language model agent as a mechanical designer. arXiv preprint arXiv:2404.17525, 2024.

Wesley F Reinhart and Antonia Statt. Large language models design sequence-defined macromolecules via evolutionary optimization. npj Computational Materials, 10(1):262, 2024.

Shengcai Liu, Caishun Chen, Xinghua Qu, Ke Tang, and Yew-Soon Ong. Large language models as evolutionary optimizers. In 2024 IEEE Congress on Evolutionary Computation (CEC), pages 1–8. IEEE, 2024e.

Shuvayan Brahmachary, Subodh M Joshi, Aniruddha Panda, Kaushik Koneripalli, Arun Kumar Sagotra, Harshil Patel, Ankush Sharma, Ameya D Jagtap, and Kaushic Kalyanaraman. Large language model-based evolutionary optimizer: Reasoning with elitism. Neurocomputing, 622: 129272, 2025.

Atilla Kaan Alkan, Shashwat Sourav, Maja Jablonska, Simone Astarita, Rishabh Chakrabarty, Nikhil Garuda, Pranav Khetarpal, Maciej Pióro, Dimitrios Tanoglidis, Kartheik G Iyer, et al. A survey on hypothesis generation for scientific discovery in the era of large language models. arXiv preprint arXiv:2504.05496, 2025.

Adib Bazgir, Yuwen Zhang, et al. Agentichypothesis: A survey on hypothesis generation using llm systems. Towards Agentic AI for Science: Hypothesis Generation, Comprehension, Quantification, and Validation, 2025c.

Joeran Beel, Min-Yen Kan, and Moritz Baumgart. Evaluating sakana’s ai scientist for autonomous research: Wishful thinking or an emerging reality towards’ artificial research intelligence’(ari)? arXiv preprint arXiv:2502.14297, 2025.

Xiao Xiao, Yu Su, Sijing Zhang, Zhang Chen, Yadong Chen, and Tian Liu. Confidence in large language model evaluation: A bayesian approach to limited-sample challenges. arXiv preprint arXiv:2504.21303, 2025.

Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao. React: Synergizing reasoning and acting in language models. In International Conference on Learning Representations (ICLR), 2023.

Xingyao Wang, Yangyi Chen, Lifan Yuan, Yizhe Zhang, Yunzhu Li, Hao Peng, and Heng Ji. Executable code actions elicit better llm agents. In Forty-first International Conference on Machine Learning, 2024e.

Zeming Lin, Halil Akin, Roshan Rao, Brian Hie, Zhongkai Zhu, Wenting Lu, Nikita Smetanin, Robert Verkuil, Ori Kabeli, Yaniv Shmueli, et al. Evolutionary-scale prediction of atomic-level protein structure with a language model. Science, 379(6637):1123–1130, 2023.

Josh Abramson, Jonas Adler, Jack Dunger, Richard Evans, Tim Green, Alexander Pritzel, Olaf Ronneberger, Lindsay Willmore, Andrew J Ballard, Joshua Bambrick, et al. Accurate structure prediction of biomolecular interactions with alphafold 3. Nature, 630(8016):493–500, 2024.

Veda Sheersh Boorla, Ratul Chowdhury, Ranjani Ramasubramanian, Brandon Ameglio, Rahel Frick, Jeffrey J Gray, and Costas D Maranas. De novo design and rosetta-based assessment of high-affinity antibody variable regions (fv) against the sars-cov-2 spike receptor binding domain (rbd). Proteins: Structure, Function, and Bioinformatics, 91(2):196–208, 2023.

Ansh Nagda, Prabhakar Raghavan, and Abhradeep Thakurta. Reinforced generation of combinatorial structures: Applications to complexity theory. arXiv preprint arXiv:2509.18057, 2025.

M. Gridach, L. Chen, Y. Li, S. Wang, and X. Zhang. Agentic ai for scientific discovery: A survey of progress, challenges, and future directions. arXiv preprint arXiv:2503.08979, 2025b.

- J. Liu, X. Cen, C. Yi, W. Huang, and H. Wang. Challenges in ai-driven biomedical multimodal data fusion and analysis. Genomics, Proteomics & Bioinformatics, 23(1):qzaf011, 2025c. doi: 10.1093/gpbjnl/qzaf011.


Q. Zhang, L. Wang, P. Liu, and M. Zhao. Robust multimodal perception in autonomous systems: a comprehensive review and enhancement strategies. ResearchGate, 2024d.

Xiner Li, Limei Wang, Youzhi Luo, Carl Edwards, Shurui Gui, Yuchao Lin, Heng Ji, and Shuiwang Ji. Geometry informed tokenization of molecules for language model generation. arXiv preprint arXiv:2408.10120, 2024a.

Cong Fu, Xiner Li, Blake Olson, Heng Ji, and Shuiwang Ji. Fragment and geometry aware tokenization of molecules for structure-based drug design using language models. arXiv preprint arXiv:2408.09730, 2024.

Keqiang Yan, Xiner Li, Hongyi Ling, Kenna Ashen, Carl Edwards, Raymundo Arróyave, Marinka Zitnik, Heng Ji, Xiaofeng Qian, Xiaoning Qian, and Shuiwang Ji. Invariant Tokenization of Crystalline Materials for Language Model Enabled Generation. Advances in Neural Information Processing Systems, 37:125050–125072, 2024.

Xinyun Chen, Maxwell Lin, Nathanael Schärli, and Denny Zhou. Teaching large language models to self-debug. arXiv preprint arXiv:2304.05128, 2023b.

Xiaoying Zhang, Hao Sun, Yipeng Zhang, Kaituo Feng, Chao Yang, and Helen Meng. Critiquegrpo: Advancing llm reasoning with natural language and numerical feedback. arXiv preprint arXiv:2506.03106, 2025c.

Yuhua Jiang, Yuwen Xiong, Yufeng Yuan, Chao Xin, Wenyuan Xu, Yu Yue, Qianchuan Zhao, and Lin Yan. Pag: Multi-turn reinforced llm self-correction with policy as generative verifier. arXiv preprint arXiv:2506.10406, 2025.

Xiaoyuan Liu, Tian Liang, Zhiwei He, Jiahao Xu, Wenxuan Wang, Pinjia He, Zhaopeng Tu, Haitao Mi, and Dong Yu. Trust, but verify: A self-verification approach to reinforcement learning with verifiable rewards. arXiv preprint arXiv:2505.13445, 2025d.

Jie Huang, Xinyun Chen, Swaroop Mishra, Huaixiu Steven Zheng, Adams Wei Yu, Xinying Song, and Denny Zhou. Large language models cannot self-correct reasoning yet. arXiv preprint arXiv:2310.01798, 2023.

Robert M Kuhn, David Haussler, and W James Kent. The ucsc genome browser and associated tools. Briefings in bioinformatics, 14(2):144–161, 2013.

Žiga Avsec, Natasha Latysheva, Jun Cheng, Guido Novati, Kyle R Taylor, Tom Ward, Clare Bycroft, Lauren Nicolaisen, Eirini Arvaniti, Joshua Pan, et al. Alphagenome: advancing regulatory variant effect prediction with a unified dna sequence model. bioRxiv, pages 2025–06, 2025.

Garyk Brixi, Matthew G Durrant, Jerome Ku, Michael Poli, Greg Brockman, Daniel Chang, Gabriel A Gonzalez, Samuel H King, David B Li, Aditi T Merchant, et al. Genome modeling and design across all domains of life with evo 2. BioRxiv, pages 2025–02, 2025.

Žiga Avsec, Vikram Agarwal, Daniel Visentin, Joseph R Ledsam, Agnieszka Grabska-Barwinska, Kyle R Taylor, Yannis Assael, John Jumper, Pushmeet Kohli, and David R Kelley. Effective gene expression prediction from sequence by integrating long-range interactions. Nature methods, 18 (10):1196–1203, 2021.

Eric Nguyen, Michael Poli, Matthew G Durrant, Brian Kang, Dhruva Katrekar, David B Li, Liam J Bartie, Armin W Thomas, Samuel H King, Garyk Brixi, et al. Sequence modeling and design from molecular to genome scale with evo. Science, 386(6723):eado9336, 2024.

Xingyu Su, Haiyang Yu, Degui Zhi, and Shuiwang Ji. Learning to discover regulatory elements for gene expression prediction. arXiv preprint arXiv:2502.13991, 2025a.

Xingyu Su, Xiner Li, Yuchao Lin, Ziqian Xie, Degui Zhi, and Shuiwang Ji. Language models for controllable dna sequence design. arXiv preprint arXiv:2507.19523, 2025b.

Y. Hao, S. Hao, J.T. Andersen, and et al. Integrated analysis of multimodal single-cell data. Cell, 184

(13):3573–3587, 2021. F.A. Wolf, P. Angerer, and F.J. Theis. Scanpy: large-scale single-cell gene expression data analysis. Genome Biology, 19(1):15, 2018. John Jumper and et al. Highly accurate protein structure prediction with AlphaFold. Nature, 596

(7873):583–589, 2021.

Thomas Hayes, Roshan Rao, Halil Akin, Nicholas J Sofroniew, Deniz Oktay, Zeming Lin, Robert Verkuil, Vincent Q Tran, Jonathan Deaton, Marius Wiggert, et al. Simulating 500 million years of evolution with a language model. Science, 387(6736):850–858, 2025.

Andrew Leaver-Fay and et al. Rosetta3: an object-oriented software suite for macromolecular modeling and design. Methods in Enzymology, 487:515–575, 2011.

Joseph L Watson, David Juergens, Nathaniel R Bennett, Brian L Trippe, Jason Yim, Helen E Eisenach, Woody Ahern, Andrew J Borst, Robert J Ragotte, Lukas F Milles, et al. De novo design of protein structure and function with rfdiffusion. Nature, 620(7976):1089–1100, 2023.

Justas Dauparas, Ivan Anishchenko, Nathaniel Bennett, Hua Bai, Robert J Ragotte, Lukas F Milles, Basile IM Wicky, Alexis Courbet, Rob J de Haas, Neville Bethel, et al. Robust deep learning–based protein sequence design using proteinmpnn. Science, 378(6615):49–56, 2022.

Greg Landrum. RDKit: Open-source cheminformatics. Journal of Cheminformatics, 1(1):10, 2006. Yihan Shao and et al. Advances in molecular quantum chemistry contained in the Q-Chem 3.0

program package. Physical Chemistry Chemical Physics, 8(27):3172–3191, 2006. Daniel G.A. Smith, L.A. Burns, D.A. Sirianni, and et al. Psi4: an open-source ab initio electronic structure program. The Journal of Chemical Physics, 152(18):184108, 2020. Ask Larsen and et al. The Atomic Simulation Environment–A Python library for working with atoms. Journal of Physics: Condensed Matter, 29(27):273002, 2017. Georg Kresse and Jürgen Furthmüller. Efficiency of ab-initio total energy calculations for metals and

semiconductors using a plane-wave basis set. Computational Materials Science, 6(1):15–50, 1996. Steve Plimpton. Fast parallel algorithms for short-range molecular dynamics. Journal of Computa-

tional Physics, 117(1):1–19, 1995.

A. P. Thompson, H. M. Aktulga, R. Berger, D. S. Bolintineanu, W. M. Brown, P. S. Crozier, P. J. in ’t Veld, A. Kohlmeyer, S. G. Moore, T. D. Nguyen, R. Shan, M. J. Stevens, J. Tranchida, C. Trott, and S. J. Plimpton. LAMMPS - a flexible simulation tool for particle-based materials modeling at the atomic, meso, and continuum scales. Comp. Phys. Comm., 271:108171, 2022. doi: 10.1016/j.cpc.2021.108171.

Haiyang Yu, Zhao Xu, Xiaofeng Qian, Xiaoning Qian, and Shuiwang Ji. Efficient and Equivariant Graph Networks for Predicting Quantum Hamiltonian. In International Conference on Machine Learning, pages 40412–40424. PMLR, 2023a.

Haiyang Yu, Meng Liu, Youzhi Luo, Alex Strasser, Xiaofeng Qian, Xiaoning Qian, and Shuiwang Ji. QH9: A Quantum Hamiltonian Prediction Benchmark for QM9 Molecules. Advances in Neural Information Processing Systems, 36:40487–40503, 2023b.

Haiyang Yu, Yuchao Lin, Xuan Zhang, Xiaofeng Qian, and Shuiwang Ji. Efficient prediction of SO(3)-equivariant Hamiltonian matrices via SO(2) local frames. arXiv preprint arXiv:2506.09398, 2025.

OpenCFD Ltd. OpenFOAM: The Open Source Computational Fluid Dynamics Toolbox. https:

//www.openfoam.com, 2024. Accessed: 2024-08-25.

- S. Noll, D. Burgarella, E. Giovannoli, V. Buat, D. Marcillac, and J. C. Muñoz-Mateos. CIGALE, a code for galaxy evolution: a new version with improved features. Astron. Astrophys., 507: 1793–1804, 2009.


Zhizheng Wang, Qiao Jin, Chih-Hsuan Wei, Shubo Tian, Po-Ting Lai, Qingqing Zhu, Chi-Ping Day, Christina Ross, Robert Leaman, and Zhiyong Lu. Geneagent: self-verification language agent for gene-set analysis using domain databases. Nature Methods, 22(8):1677–1685, August 2025b. ISSN 1548-7105. doi: 10.1038/s41592-025-02748-6. URL https://www.nature.com/ articles/s41592-025-02748-6.

Zuwan Lin, Wenbo Wang, Arnau Marin-Llobet, Qiang Li, Samuel D. Pollock, Xin Sui, Almir Aljovic, Jaeyong Lee, Jongmin Baek, Ningyue Liang, Xinhe Zhang, Connie Kangni Wang, Jiahao Huang, Mai Liu, Zihan Gao, Hao Sheng, Jin Du, Stephen J. Lee, Brandon Wang, Yichun He, Jie Ding, Xiao Wang, Juan R. Alvarez-Dominguez, and Jia Liu. Spatial transcriptomics ai agent charts hpsc-pancreas maturation in vivo. bioRxiv, DOI:10.1101/2025.04.01.646731, 2025.

Wei Xu, Gang Luo, Weiyu Meng, Xiaobing Zhai, Keli Zheng, Ji Wu, Yanrong Li, Abao Xing, Junrong Li, Zhifan Li, Ke Zheng, and Kefeng Li. Mragent: an llm-based automated agent for causal knowledge discovery in disease via mendelian randomization. Briefings in Bioinformatics, 26(2):bbaf140, March 2025c. ISSN 1467-5463, 1477-4054. doi: 10.1093/bib/bbaf140. URL https://academic.oup.com/bib/article/doi/10.1093/bib/bbaf140/8107848.

Yuyang Zhou, Jin Su, Jiawei Zhang, Wangyang Hu, Tianli Tao, Guanqi Li, Xibin Zhou, Li Fan, and Fajie Yuan. Prime: A multi-agent environment for orchestrating dynamic computational workflows in protein engineerings. bioRxiv, DOI:10.1101/2025.09.22.677756, 2025b. URL http://biorxiv.org/lookup/doi/10.1101/2025.09.22.677756.

Tianzhe Chu, Yuexiang Zhai, Jihan Yang, Shengbang Tong, Saining Xie, Dale Schuurmans, Quoc V Le, Sergey Levine, and Yi Ma. Sft memorizes, rl generalizes: A comparative study of foundation model post-training. arXiv preprint arXiv:2501.17161, 2025.

Shubham Parashar, Shurui Gui, Xiner Li, Hongyi Ling, Sushil Vemuri, Blake Olson, Eric Li, Yu Zhang, James Caverlee, Dileep Kalathil, et al. Curriculum reinforcement learning from easy to hard tasks improves llm reasoning. arXiv preprint arXiv:2506.06632, 2025.

Xingyu Su, Xiner Li, Masatoshi Uehara, Sunwoo Kim, Yulai Zhao, Gabriele Scalia, Ehsan Hajiramezanali, Tommaso Biancalani, Degui Zhi, and Shuiwang Ji. Iterative distillation for rewardguided fine-tuning of diffusion models in biomolecular design. arXiv preprint arXiv:2507.00445, 2025c.

Xiner Li, Yulai Zhao, Chenyu Wang, Gabriele Scalia, Gokcen Eraslan, Surag Nair, Tommaso Biancalani, Shuiwang Ji, Aviv Regev, Sergey Levine, et al. Derivative-free guidance in continuous and discrete diffusion models with soft value-based decoding. arXiv preprint arXiv:2408.08252, 2024b.

Xiner Li, Masatoshi Uehara, Xingyu Su, Gabriele Scalia, Tommaso Biancalani, Aviv Regev, Sergey Levine, and Shuiwang Ji. Dynamic search for inference-time alignment in diffusion models. arXiv preprint arXiv:2503.02039, 2025b.

Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, et al. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning. arXiv preprint arXiv:2501.12948, 2025.

Jiazhan Feng, Shijue Huang, Xingwei Qu, Ge Zhang, Yujia Qin, Baoquan Zhong, Chengquan Jiang, Jinxin Chi, and Wanjun Zhong. Retool: Reinforcement learning for strategic tool use in llms, 2025b. URL https://arxiv.org/abs/2504.11536.

Xinji Mai, Haotian Xu, Xing Wu, Weinong Wang, Yingying Zhang, and Wenqiang Zhang. Agent rl scaling law: Spontaneous code execution for mathematical problem solving, 2025. URL https://arxiv.org/abs/2505.07773.

Bowen Jin, Hansi Zeng, Zhenrui Yue, Jinsung Yoon, Sercan Ö. Arık, Dong Wang, Hamed Zamani, and Jiawei Han. Search-r1: Training llms to reason and leverage search engines with reinforcement learning, 2025b. URL https://arxiv.org/abs/2503.09516.

Mingyang Chen, Tianpeng Li, Haoze Sun, Yijie Zhou, Chenzheng Zhu, Haofen Wang, Jeff Z. Pan, Wen Zhang, Huajun Chen, Fan Yang, Zenan Zhou, and Weipeng Chen. Research: Learning to reason with search for llms via reinforcement learning, 2025c. URL https://arxiv.org/abs/ 2503.19470.

Zhepei Wei, Wenlin Yao, Yao Liu, Weizhi Zhang, Qin Lu, Liang Qiu, Changlong Yu, Puyang Xu, Chao Zhang, Bing Yin, Hyokun Yun, and Lihong Li. Webagent-r1: Training web agents via endto-end multi-turn reinforcement learning, 2025c. URL https://arxiv.org/abs/2505.16421.

Zehan Qi, Xiao Liu, Iat Long Iong, Hanyu Lai, Xueqiao Sun, Wenyi Zhao, Yu Yang, Xinyue Yang, Jiadai Sun, Shuntian Yao, Tianjie Zhang, Wei Xu, Jie Tang, and Yuxiao Dong. Webrl: Training llm web agents via self-evolving online curriculum reinforcement learning, 2025. URL https://arxiv.org/abs/2411.02337.

Yujia Qin, Yining Ye, Junjie Fang, Haoming Wang, Shihao Liang, Shizuo Tian, Junda Zhang, Jiahao Li, Yunxin Li, Shijue Huang, et al. Ui-tars: Pioneering automated gui interaction with native agents. arXiv preprint arXiv:2501.12326, 2025.

Saaket Agashe, Jiuzhou Han, Shuyu Gan, Jiachen Yang, Ang Li, and Xin Eric Wang. Agent s: An open agentic framework that uses computers like a human. arXiv preprint arXiv:2410.08164, 2024.

Xinyu Geng, Peng Xia, Zhen Zhang, Xinyu Wang, Qiuchen Wang, Ruixue Ding, Chenxi Wang, Jialong Wu, Yida Zhao, Kuan Li, et al. Webwatcher: Breaking new frontier of vision-language deep research agent. arXiv preprint arXiv:2508.05748, 2025.

Xiaoxi Li, Jiajie Jin, Guanting Dong, Hongjin Qian, Yutao Zhu, Yongkang Wu, Ji-Rong Wen, and Zhicheng Dou. Webthinker: Empowering large reasoning models with deep research capability. arXiv preprint arXiv:2504.21776, 2025c.

Xiusi Chen, Gaotang Li, Ziqi Wang, Bowen Jin, Cheng Qian, Yu Wang, Hongru Wang, Yu Zhang, Denghui Zhang, Tong Zhang, et al. Rm-r1: Reward modeling as reasoning. arXiv preprint arXiv:2505.02387, 2025d.

Masatoshi Uehara, Yulai Zhao, Chenyu Wang, Xiner Li, Aviv Regev, Sergey Levine, and Tommaso Biancalani. Inference-time alignment in diffusion models with reward-guided generation: Tutorial and review. arXiv preprint arXiv:2501.09685, 2025a.

Masatoshi Uehara, Xingyu Su, Yulai Zhao, Xiner Li, Aviv Regev, Shuiwang Ji, Sergey Levine, and Tommaso Biancalani. Reward-guided iterative refinement in diffusion models at test-time with applications to protein and dna design. arXiv preprint arXiv:2502.14944, 2025b.

Subbarao Kambhampati. Neither LLMs nor LRMs have the ability to go beyond humanity’s knowledge closure–which is needed for true discoveries, 2025. URL https://www.linkedin. com/feed/update/urn:li:activity:7351769291123314688/.

Alexander Fleming. On the antibacterial action of cultures of a penicillium, with special reference to their use in the isolation of b. influenzae. British Journal of Experimental Pathology, 10:226–236, 1929.

A. A. Penzias and R. W. Wilson. A measurement of excess antenna temperature at 4080 mc/s. The Astrophysical Journal, 142(1):419–421, 1965.

- K. S. Novoselov, A. K. Geim, S. V. Morozov, D. Jiang, Y. Zhang, S. V. Dubonos, I. V. Grigorieva, and A. A. Firsov. Electric field effect in atomically thin carbon films. Science, 306(5696):666–669,


###### 2004. doi: 10.1126/science.1102896. URL https://www.science.org/doi/abs/10.1126/ science.1102896.

