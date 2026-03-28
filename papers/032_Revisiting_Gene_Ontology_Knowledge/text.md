# arXiv:2603.20132v1[cs.LG]20 Mar 2026

## Revisiting Gene Ontology Knowledge Discovery with Hierarchical Feature Selection and Virtual Study Group of AI Agents

##### Cen Wan1* and Alex A. Freitas2

1*School of Computing and Mathematical Sciences, Birkbeck, University of London, London, United Kingdom. 2School of Computing, University of Kent, Canterbury, United Kingdom.

*Corresponding author(s). E-mail(s): Cen.Wan@bbk.ac.uk; Contributing authors: A.A.Freitas@kent.ac.uk;

Abstract Large language models have achieved great success in multiple challenging tasks, and their capacity can be further boosted by the emerging agentic AI techniques. This new computing paradigm has already started revolutionising the traditional scientific discovery pipelines. In this work, we propose a novel agentic AI-based knowledge discovery-oriented virtual study group that aims to extract meaningful ageingrelated biological knowledge considering highly ageing-related Gene Ontology terms that are selected by hierarchical feature selection methods. We investigate the performance of the proposed agentic AI framework by considering four different model organisms’ ageing-related Gene Ontology terms and validate the biological findings by reviewing existing research articles. It is found that the majority of the AI agentgenerated scientific claims can be supported by existing literatures and the proposed internal mechanisms of the virtual study group also play an important role in the designed agentic AI-based knowledge discovery framework.

Keywords: Large language models, Agentic AI, Knowledge extraction and discovery, Ageing Biology, Gene Ontology, Hierarchical feature selection

### 1 Introduction

The success of large language models (LLMs) and the emerging agentic AI techniques have already started revolutionalising the traditional scientific discovery paradigm. One of the most well-known examples is the agentic AI-based virtual lab [1], where real nanobody binders were successfully designed by AI agents autonomously. This achievement not only validated the feasibility of agentic AI-based scientistic research pipelines, but also boosted the research in exploring agentic AI’s possibilities in other research areas.

As one of the core topics in scientific research, knowledge extraction and discovery play a fundamental role yet remain a major challenge in almost all research subjects like ageing biology, which aims to explore extremely complex theories involving enormously unrevealed biological mechanisms. Thanks to the efforts made by the community, new progress has been recently made by AI researchers who predict novel knowledge about ageing. For example, Alsaggaf, et al (2024) [2] developed novel contrastive learning algorithms to successfully predict novel ageing-related genes using protein-protein interaction networks, whilst Paz-Ruza, et al (2024) [3] also predicted novel dietary restriction-related genes by using positive-unlabelled learning algorithms and human gene-pathway associations information. However, the limited knowledge about ageing processes remains a bottleneck of any predictive models that need to exploit sufficient information to obtain reliable performance.

Large language models have recently demonstrated strong capacity in handling complicated tasks (e.g. automatic computer programming code generation [4]), but their own shortcomings due to the well-known hallucination issues and lack of model interpretability still lead to concerns about its application in knowledge discovery tasks. The capacity of LLMs can be further enhanced by integrating the agentic AI approach

![image 1](Wan and Freitas_2026_Revisiting Gene Ontology Knowledge Discovery with Hierarchical Feature Selection and Virtual Study G_images/imageFile1.png)

![image 2](Wan and Freitas_2026_Revisiting Gene Ontology Knowledge Discovery with Hierarchical Feature Selection and Virtual Study G_images/imageFile2.png)

Fig. 1 An example of hierarchical feature selection-based Gene Ontology knowledge discovery pipeline.

to handle more challenging tasks (e.g. strategic planning for auctions [5]). Hence, LLM-based agentic AI frameworks that allow multiple LLMs to mimic human interactions would be a feasible research direction aiming to alleviate the problems of a single LLM-based knowledge discovery method. In this work, we propose a novel LLM-based agentic AI framework that simulates a type of human study group mechanism for extracting meaningful ageing-related biological knowledge according to informative Gene Ontology terms selected by hierarchical feature selection methods.

### 2 Background

#### 2.1 Gene Ontology Database

Gene Ontology database [6] provides a type of universal vocabulary, i.e. Gene Ontology terms, to describe functions of genes and gene products. All GO terms are organised as a type of hierarchical structure, where GO terms that are located in higher positions denote more generic definitions and those are located in lower positions denote more specific definitions. As shown in the example GO hierarchy in Figure 1, GO:0050789 that denotes regulation of biological process is located in the highest position, while other GO terms, e.g. GO:0009894 (regulation of catabolic process), are located in lower positions, denoting more specific definitions of GO:0050789. Therefore, with considering genes and their corresponding Gene Ontology annotations, we are able to use a set of GO terms to describe those genes’ biological processes, molecular functions and cellular components. In addition, due to the hierarchical relationships between GO terms, when conducting biological knowledge interpretation, those GO terms bearing more specific definitions are more informative than the ones bearing more generic definitions. However, note that those GO terms bearing more specific definitions are usually independent to other GO terms that also denote specific definitions, leading to a challenge to discover associations between multiple GO terms bearing specific biological definitions. For example, as shown in Figure 1, GO:0009892 (negative regulation of metabolic process) and GO:0009889 (regulation of biosynthetic process) that denote two different specific biological processes have no interconnections according to the predefined hierarchy. Therefore, it will be difficult to find the interaction of the biological definitions denoted by those two GO terms, when some genes are simultaneously annotated by both of them.

#### 2.2 Hierarchical Feature Selection

Hierarchical feature selection [7–15] is a type of dimensionality reduction methods that aim to remove redundant and irrelevant features with considering pre-defined hierarchical dependencies. Wan & Freitas firstly proposed a family of hierarchical feature selection methods including HIP (Select Hierarchical InformationPreserving features) [9], MR (Select Most Relevant features) [9] and HIP-MR (the hybrid of HIP and MR methods) [7] that were used to deal with the Gene Ontology database, where GO terms were considered as features. With the help of the proposed methods, a set of the most informative GO terms associated with ageing-related genes [16] were selected and ranked as a table, which provided a knowledge source for biological interpretations. For example, as shown in Figure 1, with considering four different sets of genes that have been found as being relevant to ageing processes, hierarchical feature selection methods like HIP can

derive a table showing the most informative GO terms for different model organisms. In terms of Caenorhabditis elegans, the most informative GO term is GO:0045202 (synapse), followed by the second top-ranked GO term GO:0000003 (reproduction). Note that, both GO:0045202 and GO:0000003 have the same frequencies of selection. Therefore, I used frequency in edges as a tie-breaking criterion, i.e. tree-augmented naive Bayes [17] was used to learn a tree for each instance by using the corresponding selected GO terms. Analogously, in terms of Drosophila melanogaster, the top-ranked GO terms are GO:0009055 (electron carrier activity) and GO:0005576 (extracellular region). In this work, I use the table reported in Wan & Freitas (2018) [18] that was generated by the HIP method as an example to evaluate the proposed AI agent-based virtual study group.

#### 2.3 Large Language Models for Knowledge Extraction

Large Language Models are a type of AI intelligent system trained by using massive and complex data with advanced language model architectures and techniques. One of the most impressive properties of LLMs is the so-called knowledge emergence phenomenon [19, 20] that allows LLMs to convert multi-dimensional and multi-scale data into their capacity to conduct advanced activities, e.g. programming code generation [4, 21, 22], logical reasoning inference [23–25], and strategic planning [5, 26, 27]. Due to this unique property, LLMs have demonstrated great potential in knowledge extraction tasks. For example, Dagdelen, et al. (2024) [28] successfully adopted LLMs to extract a type of structured information consisting of entities and their relationships from raw text. Analogously, Balasubramanian, et al. (2025) [29] adopted LLMs to successfully extract knowledge that was presented as a set of features from pathology reports. Builtjes, et al. (2025) [30] also proposed a LLM-based framework for extracting information from clinical texts. However, note that, all those above works are quite different with the Gene Ontology terms-based knowledge interpretation tasks we discuss in this work. Also, due to the well-known shortcomings of existing LLMs, e.g. the hallucination issue, it is unclear whether LLMs are able to derive reliable biological knowledge that usually involves complex theories.

#### 2.4 Agentic AI for Scientific Research

Agentic AI is a type of intelligent system that evolves from the conventional multi-agent systems [31] can autonomously conduct activities to achieve pre-defined goals. Compared with the conventional multi-agent systems, agentic AI systems are more powerful, due to the superbo capacities of large language models that are used as cores. An agentic AI system usually consists of multiple AI agents, which form a virtual team where each agent plays a role allowing them to cooperate with each other by passing information and calling different tools until the pre-defined goal is achieved. Recently, multiple agentic AI systems have been developed for scientific discovery tasks. For example, Ruan, et al. (2024) [32] developed a LLM-agent-based end-to-end chemical synthesis development platform that successfully conducts multiple chemical research steps including literature search, reaction kinetics study, and product purification. More recently, Swanson, et al. (2025) [1] proposed an AI agent-based virtual lab to successfully design nanobody binders. Within the virtual lab, multiple agents simulate human-like scientific discovery activities including group discussion, computational tools implementation and computational experiment results analysis. Analogously, Schmidgall, et al. (2025) [33] also developed an agent-based virtual lab that autonomously executes a completed research pipeline. Given a research idea, the proposed virtual lab can autonomously conduct literature review, research plan generation, programming code generation and results analysis, leading to a great decrease in research expense. It has also been found that the agentic AI paradigm can alleviate the hallucination issue. For example, Gosmar and Dahl (2025) [34] proposed a multi-layer framework, where agents in higher layers aim to remove hallucination information in the statements made by agents in lower layer. In this work, we also propose a multi-layer agent framework, which aims to exploit multiple agents to process LLM-generated biological knowledge by using a type of critical reviewing mechanisms to extract meaningful ageing-related knowledge considering certain biological processes and molecular functions.

### 3 Problem Definition

In this paper, we focus on interpreting ageing-related biological knowledge from a set of informative Gene Ontology terms that are selected by hierarchical feature selection methods. Given a list of selected Gene Ontology terms according to gene annotations for four different model organisms, an agentic AI system is required to generate a report describing biological findings about each individual model organism and common patterns across those organisms.

More specifically, we define the tasks as shown below.

- • Evaluate the correctness of GO term-based biological knowledge interpretations generated by LLMs.
- • Evaluate the usefulness of the proposed agentic AI-based virtual study group mechanisms for biological knowledge discovery.


The input GO terms and the tasks assigned to different AI agents are shown below. In this work, we consider the GO terms selection table reported in our previous work [18]. In terms of the GO terms used in this work, we select the ones with high selection frequency and bear more generic biological definitions which would be feasible to be validated by existing literatures.

###### • Worm:

- – Input GO terms: {GO:0000003 (reproduction), GO:0016209 (antioxidant activity)}
- – Tasks: Investigate the associations between reproduction, antioxidant activity and ageing processes in Caenorhabditis elegans.
- – Remarks: both two terms are top-ranked GO terms that are selected by the HIP hierarchical feature selection method for all 572 ageing-related worm genes in the given dataset. The two GO terms have no connections in the GO hierarchy and belong to different domains, i.e. the former belongs to the Biological Process domain, and the latter belongs to the Molecular Function domain.


###### • Fruit fly:

- – Input GO terms: {GO:0009055 (electron carrier activity), GO:0005198 (structural molecule activity)}
- – Tasks: Investigate the associations between electron carrier activity, structural molecule activity and ageing processes in Drosophila melanogaster.
- – Remarks: both two terms are top-ranked GO terms that are selected by the HIP hierarchical feature selection method for ageing-related fruit fly genes in the given dataset. The two GO terms have no connections in the GO hierarchy, though both belong to the Molecular Function domain.


###### • Mouse:

- – Input GO terms: {GO:0005198 (structural molecule activity), GO:0016209 (antioxidant activity)}
- – Tasks: Investigate the associations between structural molecule activity, antioxidant activity and ageing processes in Mus musculus.
- – Remarks: both two terms are top-ranked GO terms that are selected by the HIP hierarchical feature selection method for ageing-related mouse genes in the given dataset. The two GO terms have no connections in the GO hierarchy, though both belong to the Molecular Function domain.


###### • Yeast:

- – Input GO terms: {GO:0004872 (receptor activity), GO:0022414 (reproductive process)}
- – Tasks: Investigate the associations between receptor activity, reproductive process and ageing processes in Saccharomyces cerevisiae.
- – Remarks: both two terms are top-ranked GO terms that are selected by the HIP hierarchical feature selection method for ageing-related yeast genes in the given dataset. The two GO terms have no connections in the GO hierarchy and belong to different domains, i.e. the former belongs to the Molecular Function domain, and the latter belongs to the Biological Process domain.


Virtual Principal Investigator

| | |
|---|---|
| | |
| | |


| | | |
|---|---|---|
| | | |
| | | |


Virtual Senior Researcher in Saccharomyces cerevisiae

Virtual Senior Researcher in Caenorhabditis elegans

Virtual Senior Researcher in Drosophila melanogaster

Virtual Senior Researcher in Mus musculus

| | | |
|---|---|---|
| | | |
| | | |


A list of selected GO terms for Caenorhabditis elegans genes

A list of selected GO terms for Caenorhabditis elegans genes

A list of selected GO terms for Drosophila melanogaster genes

A list of selected GO terms for Drosophila melanogaster genes

GO:0009055: electron carrier activity GO:0005198: structural molecule activity

GO:0009055: electron carrier activity GO:0005198: structural molecule activity

GO:0000003: reproduction GO:0016209: antioxidant activity

GO:0000003: reproduction GO:0016209: antioxidant activity

Virtual Junior Researchers in Caenorhabditis elegans

Virtual Junior Researchers in Mus musculus

Virtual Junior Researchers in Saccharomyces cerevisiae

Virtual Junior Researchers in Drosophila melanogaster

……

……

……

……

GO:0009055: electron carrier activity

GO:0009055: electron carrier activity

GO:0030234: enzyme regulator activity

GO:0030234: enzyme regulator activity

###### A list of selected GO terms for

###### A list of selected GO terms for

###### A list of selected GO terms for

###### A list of selected GO terms for

###### A list of selected GO terms for

###### A list of selected GO terms for

###### A list of selected GO terms for

###### A list of selected GO terms for

|Caenorhabditis el|egansCaenorhabditgenes|is elegans genes|
|---|---|---|
|GO:0000003: reprodu|ctionGO:0000003: re|production|
|GO:0016209: antioxid|ant activityGO:0016209: an|tioxidant activity|
|……| |……|


|Drosophila melano|gasterDro|genessophila meM|us muslanoga|sterculusgenesgenesMus m|uscu|lus genes|
|---|---|---|---|---|---|---|
|GO:0009055: electron|carrier aGO:000|ctivity9055: elecGO:00051|98: structron carr|tural molecule aier activityGO:0005198: s|ctivitytructur|al molecule activity|
|GO:0005198: structura|l molecuGO:00|05198: strule activityGO:00162|ctural mo09: antio|xidant activitylecule activityGO:0016209: a|ntioxid|ant activity|
|……| | |…… …|…|……| |


|Saccharomyces c|erevisiaeSaccharomycesgenes|cerevisiae genes|
|---|---|---|
|GO:0004872: recept|or activityGO:0004872: rece|ptor activity|
|GO:0022414: reprod|uctive processGO:0022414: repro|ductive process|
|……|…|…|


GO:0009055: electron carrier activity

GO:0009055: electron carrier activity

GO:0031012: extracellular matrix

GO:0031012: extracellular matrix

GO:0030234: enzyme regulator activity

GO:0030234: enzyme regulator activity

GO:0030234: enzyme regulator activity

GO:0030234: enzyme regulator activity

- Fig. 2 The hierarchical structure of the proposed AI agents-based virtual study group framework.


###### A list of selected GO terms for

###### A list of selected GO terms for

###### A list of selected GO terms for

###### A list of selected GO terms for

|Mus musculu|s genes Mus mus|culus genes|
|---|---|---|
|GO:0005198: structura4|l molecule activityGO:0005198: struPropo|ctural molecule activitysed|
|GO:0016209: antioxida|nt activityGO:0016209: antio|xidant activity|
|……We|propose a|……n AI|


|Saccharomyces cer|evisiaeSaccharomycegenes|s cerevisiae genes|
|---|---|---|
|GO:0004872: receptor|activityGO:0004872: rec|eptor activity|
|GO:0022414: reprodu|ctive processGO:0022414: rep|roductive process|
|Virtual……S|tudy Grou|……p (VSG)|


### Methods

agents-based framework, where the biological interpretations of the Gene Ontology terms selected by hierarchical feature selection methods can be extracted automatically. The proposed VSG framework is composed by several agents, which play different roles in a hierarchically organised virtual organization. In order to extract a general summary with considering all GO terms’ biological definitions, we propose a bottom-up structure that is used to coordinate the actions of multiple agents. As shown in Figure 2, in the first layer, multiple virtual junior researchers that mimic early year PhD students are in charge of investigating the associations between different GO terms and ageing processes. As we have four model organisms in this case, VSG uses four virtual junior researchers which have certain academic background on the corresponding model organims. For example, one virtual early-year PhD student (i.e. Virtual Junior Researcher A) whose academic background is mainly about worm will be assigned to conduct early investigations on the associations between certain GO terms and worm-related ageing processes. In addition, for each of the virtual junior researcher, we assign another virtual junior researcher (i.e. Virtual Junior Researcher B) whose duty is to criticise the findings discovered by Virtual Junior Researcher A. The second layer consists of four virtual senior researchers mimicking post-doctoral research associates, who are in charge of summarising the findings and the corresponding critics made by two virtual junior researchers (Virtual Junior Researcher A and Virtual Junior Researcher B) for one model organism. After obtaining the reports made by four virtual senior researchers, a virtual principal investigator that mimic an ageing professor will provide a final report with considering the findings about all four model organisms.

GO:0031012: extracellular matrix

GO:0030234: enzyme regulator activity

GO:0031012: extracellular matrix

GO:0030234: enzyme regulator activity

We implement the proposed VSG system using CrewAI [35] and four different open-source large language models that are held by Ollama [36]. As shown in Figure 3, we use deepseek-r1 [37] and qwen3-vl [38] as the cores for Virtual Junior Researcher A and Virtual Junior Researcher B, respectively. gpt-oss [39] and glm-4.7-flash [40] are used as the cores for Virtual Senior Researchers and Virtual Principal Investigator, respectively.

###### LLM Name Background Task

Investigating associations between certain biological processes and ageing processes in one specific model organism.

Junior Researcher in one specific model organism

An early-year PhD student

deepseek-r1

Reviewing the findings made by another junior researcher and making critical comments in one specific model organism.

Junior Researcher in one specific model organism

An early-year PhD student

qwen3-vl

Summarising the findings and the critical comments made by two different junior researchers.

Senior Researcher in one specific model organism

| | |
|---|---|
| | |


A postdoctoral researcher

gpt-oss

| | |
|---|---|
| | |
| | |


Summarising the reports made by four senior researchers regarding the findings of certain biological processes and ageing processes in four different model organisms.

A professor in ageing research

Principal Investigator

glm-4.7-flash

- Fig. 3 Further information regarding different LLM-based agents.


### 5 Experimental Results

#### 5.1 The majority of the claims made by virtual junior researchers aresupported by known biological knowledge.

We report the original outputs made by different AI agents and highlight any claims that can be validated by existing biological knowledge through conducting literature reviews on existing research articles published in decent academic journals. The phrases that are highlighted in green backgrounds denote the scientific claims that are supported by at least one existing research article, whilst the phrases in yellow backgrounds denote the scientific claims that are not supported by any existing research articles.

In general, the generated reports by AI agents include both objective claims and subjective opinions. In terms of Virtual Junior Worm Researcher A and Virtual Junior Worm Researcher B, the majority of the scientific and objective claims are correct and can be validated by existing research articles. For example, Virtual Junior Worm Researcher A successfully points out that superoxide dismutase (SOD) and catalase (CAT) play a crucial role in antioxidant defense systems that are tightly associated with ageing. Virtual Junior Worm Researcher B also successfully further mentions the role of sod-3 in hypodermis in terms of age-related regulations. Analogously, Virtual Junior Fruit Fly Researcher A mentions the associations between electron carriers and mitochondrial function, and Virtual Junior Fruit Fly Researcher B further explains the role of UPRmt in ageing processes. In terms of Virtual Junior Mouse Researcher A, it successfully points out the associations between laminopathies and progeria, whilst Virtual Junior Mouse Researcher B further mentions the role of nuclear instability in mouse’s ageing processes. Finally, in terms of Virtual Junior Yeast Researcher A, the well-known associations between mating pheromones and yeast ageing processes are successfully revealed, whilst Virtual Junior Yeast Researcher B further points out the role of quiescent cell metabolism, which is highly associated with yeast ageing processes. However, note that Virtual Junior Yeast Researcher B claims

that ‘Hog1 deletion mutants maintain near-normal chronological lifespan in standard conditions’. This claim is not supported and an opposite conclusion was made by one existing research article.

#### 5.2 Contrary views between virtual junior researchers are successfully observedand senior researchers made fair points.

In terms of the subjective opinions, the Virtual Junior Worm Researcher A, Virtual Junior Fruit Fly Researcher A, Virtual Junior Mouse Researcher A and Virtual Junior Yeast Researcher A all use a natural tone of certainty to summarise the biological knowledge findings by providing the corresponding objective evidence. On the contrary, the Virtual Junior Worm Researcher B, Virtual Junior Fruit Fly Researcher B, Virtual Junior Mouse Researcher B and Virtual Junior Yeast Researcher B all criticise the opinions made by their counterparts and also show corresponding objective evidence. For example, some commonly used terms are oversimplifies, overstates, and overgeneralizes, suggesting a type of critical context.

In terms of those senior researchers for the four model organisms, all of them tend to agree with the criticisms made by the corresponding virtual junior researchers B by rephrasing the content provided by virtual junior researchers A and B. In addition, those virtual senior researchers all suggest that more research needs to be conducted to further investigate the ageing mechanisms for different model organisms.

The comments made by the virtual ageing professor are also interesting. To begin with, it successfully points out that perhaps the more valuable direction would be related to the generalisability of the worm-based knowledge in terms of extending to mammals due to the complexity of the latter. Moreover, it acknowledges and reiterates the importance of Reactive Oxygen Species and their related biological pathways in ageing processes, but also points out the challenges of future research in this direction. Furthermore, it mentions that the discussions about the associations between reproduction and ageing need to be further expanded from evolutionary perspectives.

- • Agent: Virtual Junior Worm Researcher A
- • Task: Investigate the associations between reproduction, antioxidant activity and ageing processes in Caenorhabditis elegans.


###### AI Agent Outputs:

Reproduction in *C. elegans* is a critical determinant of lifespan, largely occurring during a specific reproductive period. This reproductive activity, particularly within the germline,

|supported by [41]|
|---|


is associated with increased production of reactive oxygen species (ROS)

, a form of cellular damage linked to aging. Consequently, the efficiency of antioxidant defense systems, which include enzymes like superoxide dismutase (SOD) and catalase (CAT), becomes crucial.

|supported by [42]|
|---|


Reduced antioxidant activity or impaired antioxidant pathways, such as those regulated by the DAF-16/FOXO transcription factor downstream of the insulin/IGF-1 signaling (IIS) pathway, can accelerate aging and reduce lifespan.

|supported by [43, 44]|
|---|


Conversely, enhanced antioxidant capacity can promote longevity. The relationship is complex, involving trade-offs; reproductive investment might influence resource allocation to maintenance pathways, including antioxidant defenses. Mutants with defects in reproduction or longevity pathways (e.g., *clk-1*

|supported by [45]|
|---|


,

|supported by [46]|
|---|


) often exhibit altered oxidative stress levels , highlighting the intertwined nature of reproduction, antioxidant status, and the aging process in worms.

*germline-less*

|* Authors’ comments: the generated report can be validated by existing research articles.|
|---|


- • Agent: Virtual Junior Worm Researcher B
- • Task: Provide critical comments against the report made by Virtual Junior Worm Researcher A.


###### AI Agent Outputs:

The received information oversimplifies the relationship between reproduction, oxidative stress, and aging in *C. elegans* by framing reactive oxygen species (ROS) as universally detrimental without acknowledging their dual role as signaling molecules that regulate stress responses and longevity pathways. Specifically, it erroneously implies that germline-derived ROS universally accelerate aging, while empirical evidence from *germline-less* mutants (e.g., *glp-1* RNAi) demonstrates that

|supported by [46, 47]|
|---|


*reducing* germline activity extends lifespan *despite* elevated systemic ROS

,

contradicting the assertion that reproductive investment directly increases oxidative damage. Furthermore, the text conflates correlation with causation by attributing altered oxidative stress in mutants like *clk-1* solely to reproductive defects, whereas

*clk-1* primarily affects mitochondrial function and metabolism independently of germline activity, and its lifespan extension is linked to reduced ROS in somatic tissues – not germline-specific trade-offs

|supported by [48, 49]|
|---|


. The discussion of antioxidant defense efficiency overlooks tissue-

|supperted by [50]|
|---|


specific dynamics, such as the critical role of *sod-3* in hypodermis

or

|support not found|
|---|


, which are not equally impacted by reproductive status. Additionally, the claim that DAF-16/FOXO activation consistently suppresses ROS ignores context-dependent mechanisms, as DAF-16 can induce *sod-3* in certain conditions but not others

*cat-1* in neurons

|supported by [51]|
|---|


, and

|supported by [52]|
|---|


. Crucially, the text neglects that ROS production in the germline serves essential functions (e.g., meiotic recombination)

germline removal activates DAF-16 independently of IIS in *germline-less* adults

|supported by [53]|
|---|


, and the described “trade-off” model fails to account for com-

|supported by [54]|
|---|


pensatory pathways, such as the role of mitochondrial retrograde signaling

or

|supported by [55]|
|---|


|supported by [56]|
|---|


) that modulate both reproduction and oxidative stress without direct germline involvement. This oversimplification risks misrepresenting the complexity of aging mechanisms and underestimates the need for nuanced, tissue-resolved analysis in future studies.

dietary interventions

(e.g., rapamycin

|* Authors’ comments: the criticisms are sensible and the majority of the scientific claims can be validated|
|---|


|by existing research articles.|
|---|


- • Agent: Virtual Senior Worm Researcher
- • Task: Provide critical comments against the reports made by Virtual Junior Worm Researcher A and Virtual Junior Worm Researcher B.


###### AI Agent Outputs:

The received analysis overstates the deleterious nature of ROS by treating them as uniformly harmful, ignoring the well-documented signaling roles that ROS play in activating stress-responsive and longevity pathways in *C. elegans*; for instance,

|supported by [46, 47]|
|---|


, contradicting the claim that reproductive investment inevitably raises oxidative damage, and suggesting instead a complex reallocation of resources that can enhance systemic antioxidant defenses; the discussion also mistakenly equates altered oxidative stress in *clk-1* mutants with reproductive defects, whereas *clk-1* primarily

germline-less *glp-1* mutants extend lifespan despite elevated systemic ROS

perturbs mitochondrial biogenesis and metabolism, and its lifespan extension is linked to reduced somatic ROS rather than germline trade-offs

|supported by [48, 49]|
|---|


; tissue-specific nuances are over-

|supperted by [50]|
|---|


looked, such as the pivotal role of *sod-3* in the hypodermis

and

|supperted not found|
|---|


, which are differentially regulated by germline status and cannot be generalized across the organism; moreover, the assertion that DAF-16/FOXO activation uniformly suppresses ROS is inaccurate, as DAF-16 can induce *sod-3* only under certain conditions and germline removal activates DAF-16 via IIS-independent mechanisms

*cat-1* in neurons

|supported by [51]|
|---|


|supported by [52]|
|---|


, indicating context-dependent pathways; the critique also neglects the essential germline functions of ROS in meiotic

|supported by [53]|
|---|


|supported by [57]|
|---|


recombination

and chromosomal segregation

, and it fails to

|supported by [54]|
|---|


account for compensatory mechanisms such as mitochondrial retrograde signaling

or

|supported by [58]|
|---|


|supported by [59]|
|---|


) that modulate both reproductive output and oxidative stress independently of germline activity; overall, the simplified model presented risks misguiding future research by underappreciating the multi-layered, tissue-resolved interactions between reproduction, oxidative stress, and longevity in *C. elegans* and highlights the need for nuanced, experimentally dissected analyses rather than broad generalizations.

dietary interventions

(e.g., rapamycin

|* Authors’ comments: the report mainly agrees with the criticisms made by Virtual Junior Worm|
|---|


|Researcher B.|
|---|


- • Agent: Virtual Junior Fruit Fly Researcher A
- • Task: Investigate the associations between electron carrier activity, structural molecule activity and ageing processes in Drosophila melanogaster.


###### AI Agent Outputs:

The investigation into the associations between electron carrier activity (e.g., components of the electron transport chain such as Complex I-III, cytochrome c) and structural molecule activity (e.g., proteins like actin, tubulin, lamin involved in maintaining cellular architecture) and the ageing processes in *Drosophila melanogaster* reveals a complex interplay.

Electron carriers are central to mitochondrial function and energy metabolism, and their efficiency directly impacts metabolic rate and the production of reactive oxygen species (ROS), a key factor in cellular damage and ageing. Reduced activity or dysfunction in these carriers can impair ATP production, increase ROS leakage, and accelerate age-related decline

|supported by [60]|
|---|


, although

compensatory pathways may exist. Structural molecules provide the physical integrity necessary for organelle and nuclear positioning, and their activity is crucial for cellular maintenance and repair mechanisms. Deficits in structural protein synthesis or stability can lead to cellular fragility and impaired tissue function over time

|supported by [61]|
|---|


. Furthermore, the relationship between reproduction and ageing in flies involves potential trade-offs; reproductive investment might divert resources away from somatic maintenance pathways

|supported by [62, 63]|
|---|


,

|supported by [64]|
|---|


including those supporting efficient electron carrier function or structural protein integrity

, thereby influencing overall organismal ageing.

|* Authors’ comments: the generated report can be validated by existing research articles.|
|---|


- • Agent: Virtual Junior Fruit Fly Researcher B
- • Task: Provide critical comments against the report made by Virtual Junior Fruit Fly Researcher A.


###### AI Agent Outputs:

The conclusion overgeneralizes the mechanistic interplay between electron carriers and structural molecules in *Drosophila* ageing, presenting a monolithic narrative that neglects critical nuances. While mitochondrial electron transport chain (ETC) dysfunction and ROS are well-established contributors to ageing, the assertion that reduced electron carrier activity *directly* accelerates ageing overlooks tissue-specific compensatory mechanisms – such as the mitochondrial unfolded protein response (UPRmt)

|supported by [65]|
|---|


|supported by [66]|
|---|


– which can mitigate ROS damage in flies. Furthermore, the text oversimplifies structural molecule roles, ignoring fly-specific cytoskeletal dynamics (e.g., septins and shotgun anillin in ovarian aging

or glycolytic adaptations in fat body tissue

|support not found|
|---|


) and the fact that lamin mutations primarily impact nuclear integrity in specific tissues (e.g., germline stem cells)

|supported by|
|---|


|[67]|
|---|


, not systemic ageing. Crucially, the reproductive trade-off argument conflates resource allocation with direct physiological consequences; while reproduction *can* accelerate ageing in certain contexts (e.g.,

|supported by [68]|
|---|


), it does not universally divert resources from somatic maintenance in all tissues or life stages. Methodologically, the conclusion fails to address how these pathways are measured (e.g., electron carrier activity via spectrophotometry vs. *in vivo* imaging) or acknowledge that most ageing studies use short-lived laboratory strains (*w1118*) that lack physiological relevance to natural fly lifespan. Finally, it ignores key evidence that specific ETC components (e.g., Complex I) decline with age but do not *causally* drive ageing – demonstrated by studies where Complex I inhibition extends lifespan via HIF-1α-mediated metabolic shifts

egg-laying-induced oxidative stress in ovaries

|supported by [69]|
|---|


|supported by [70]|
|---|


– undermining the proposed “direct impact” claim. This narrative risks reducing complex ageing biology to a simplistic linear model without sufficient mechanistic or contextual specificity.

|* Authors’ comments: the criticisms are sensible and the majority of the scientific claims can be validated|
|---|


|by existing research articles.|
|---|


- • Agent: Virtual Senior Fruit Fly Researcher
- • Task: Provide critical comments against the reports made by Virtual Junior Fruit Fly Researcher A and Virtual Junior Fruit Fly Researcher B.


The assertion that a linear, direct causal relationship exists between diminished electron carrier function, loss of structural molecule integrity, and accelerated ageing in *Drosophila* is untenable, as it glosses over a host of tissue-specific and compensatory mechanisms that have been repeatedly demonstrated in the literature. First, the mitochondrial unfolded protein response (UPRmt)

|supported by [65]|
|---|


and metabolic rewiring towards glycolysis, especially in fat-body and muscle, can buffer the deleterious effects of ETC decline

|supported by [71]|
|---|


|supported not found|
|---|


; indeed, controlled Complex I inhibition in flies can extend lifespan through HIF-1α-mediated pathways

without invoking an inevitable ROS-driven senescence

|supported by [70]|
|---|


, illustrating that ETC dysfunction is not intrinsically age-driving. Second, the functional roles of cytoskeletal components and nuclear lamins are highly context dependent:

|supported by [67]|
|---|


septin loss or lamin mutations primarily perturb germline stem cell niche architecture rather than systemic organ integrity, and many studies implicate tissue-specific cytoskeletal plasticity (e.g., anillin/shotgun in ovarian ageing

|support not found|
|---|


) rather than a universal loss of actin or tubulin function. Third, the claim that reproductive investment necessarily diverts resources from somatic maintenance across all tissues and life stages fails to consider evidence that

|supported by [68]|
|---|


, with no consistent global trade-off in longevity. Fourth, methodological oversights – such as relying on spectrophotometric assays of isolated mitochondria or using short-lived laboratory strains (e.g., *w1118*) with altered stress responses – undermine the generalizability of the conclusions. Collectively, these points expose the proposal as an overreaching simplification that ignores critical nuances of mitochondrial plasticity, cytoskeletal dynamics, and resource allocation in the ageing *Drosophila* system.

egg-laying-induced oxidative stress is largely confined to ovaries

|* Authors’ comments: the report mainly agrees with the criticisms made by Virtual Junior Fruit Fly|
|---|


|Researcher B|
|---|


.

- • Agent: Virtual Junior Mouse Researcher A
- • Task: Investigate the associations structural molecule activity, antioxidant activity and ageing processes in Mus musculus.


In Mus musculus, the intricate relationship between structural molecule activity, antioxidant defenses, and the aging process is governed by complex interdependencies. Structural proteins, including cytoskeletal components (actin, tubulin, lamin) and matrix molecules (collagen, fibronectin), are fundamental for maintaining cellular and tissue integrity. Their degradation or dysfunction, often observed in aging (e.g., laminopathies contributing to progeria

|supported by [72]|
|---|


|supported by [73]|
|---|


or cytoskeletal alterations in neurodegeneration

), directly compromises tissue function and contributes to age-related decline. This structural integrity is critically dependent on efficient cellular maintenance pathways, including those counteracting oxidative stress.

Antioxidant activity, orchestrated by enzymes like superoxide dismutase (SOD) and catalase (CAT), along with transcription factors such as Nrf2, forms a crucial defense system against reactive oxygen species (ROS)

|supported by [74, 75]|
|---|


. The efficiency of these antioxidant pathways is essential; their decline, often linked to genetic factors (e.g.,

|supported by [76]|
|---|


in certain mouse strains) or environmental influences, exacerbates oxidative damage, accelerating cellular and organismal aging. Furthermore, there exists a potential trade-off where resources allocated towards

mutations in IGF-1/FOXO axis components like *Foxo3a*

|supported by [77]|
|---|


, including both structural protein synthesis and antioxidant enzyme production. The dual nature of ROS, acting as cellular signaling molecules but also as damaging agents, adds another layer of complexity, with tissue-specific responses (e.g., *Sod-3* expression in hypodermis

reproduction might impact somatic maintenance pathways

|supported by [78]|
|---|


or *Cat-1* in

|supported by [79]|
|---|


influencing the aging trajectory. Consequently, the maintenance of structural molecule integrity and robust antioxidant activity are paramount for mitigating age-related deterioration in mice, highlighting a network of interconnected pathways rather than isolated factors.

neurons)

|* Authors’ comments: the generated report can be validated by existing research articles.|
|---|


- • Agent: Virtual Junior Mouse Researcher B
- • Task: Provide critical comments against the report made by Virtual Junior Mouse Researcher A.


The text presents a compelling but oversimplified framework for understanding aging in mice, with critical gaps that require scrutiny. While structural proteins like

lamin and cytoskeletal components are indeed implicated in age-related pathologies such as progeria or neurodegeneration

|supported by [80]|
|---|


|supported by [73]|
|---|


, the assertion that their *degradation or dysfunction is fundamentally governed by interdependencies with antioxidant defenses* significantly misrepresents the causal hierarchy. Progeroid mouse models (e.g.,

|supported by [80]|
|---|


*Lmna* mutants) primarily demonstrate accelerated aging through nuclear instability

,

not as a direct consequence of antioxidant failure – rather, oxidative stress *emerges as a downstream consequence* of structural collapse in these specific contexts. Furthermore, the text conflates general antioxidant decline (e.g., reduced SOD/CAT activity) with the *primary driver* of aging, neglecting that Nrf2-dependent antioxidant pathways are often intact in wild-type mice until late

|support not found|
|---|


; the observed decline in these enzymes is frequently a *symptom* of cumulative damage (e.g., from mitochondrial dysfunction), not the root cause. The claimed “trade-off” between reproduction and somatic maintenance is unsubstantiated in standard mouse aging models; while resources may shift with reproductive investment, no evidence links this

senescence

|supported by [81]|
|---|


, and recent studies (e.g., *Nature Aging* 2021

directly to *reduced* structural protein synthesis or antioxidant capacity in wild-type mice

|reference not found|
|---|


) show no consistent correlation between reproductive timing and somatic maintenance pathways

|supported by [82]|
|---|


.

Finally, the dual nature of ROS is acknowledged but inadequately contextualized – tissue-specific expression of *Sod-3* or *Cat-1* does not inherently alter aging trajectories; instead, localized ROS

dysregulation (e.g., in neurons) is often a *result* of impaired mitochondrial function or protein homeostasis, not an independent driver

|support not found|
|---|


. The conclusion that structural integrity and antioxidant activity are “paramount for mitigating age-related deterioration” overstates their role, as aging manifests through interconnected network failures where structural deterioration, oxidative damage, and proteostasis loss are all consequences of deeper systemic decline rather than isolated, interdependent targets.

|* Authors’ comments: the criticisms are sensible and the majority of the scientific claims can be validated|
|---|


|by existing research articles.|
|---|


- • Agent: Virtual Senior Mouse Researcher
- • Task: Provide critical comments against the reports made by Virtual Junior Mouse Researcher A and Virtual Junior Mouse Researcher B.


The critique admirably de-emphasizes the na¨ıve causal chain that “loss of structural proteins causes antioxidant failure,” and it rightly underscores that oxidative stress in progeroid models such as *Lmna* mutants is largely a downstream effect of nuclear instability rather than a primary driver. However, by positioning antioxidant decline as merely a “symptom” it may underplay the evidence that sustained activation of Nrf2 and other redox-sensing pathways can delay aging phenotypes in wild-type mice and in long-lived mutants (e.g., *IGF-1*

|not supported by [83] but with an exemption of [84]|
|---|


|supported|
|---|


or *FOXO3a* overexpressors

|by [85]|
|---|


. Moreover, the argument that reproduction has no measurable trade-off with

somatic maintenance is too restrictive; recent studies of reproductive senescence in mice with altered IGF-1 signalling demonstrate that energy allocation can indeed down-regulate protein homeostasis and antioxidant capacity in a tissue-specific manner

|supported by [86, 87]|
|---|


. Finally, while the critique correctly states that tissue-specific ROS dysregulation is often a consequence rather than a cause of mitochondrial dysfunction, it overlooks the mounting data that

local ROS production can act as a signaling hub to trigger adaptive stress responses, which in turn modulate systemic proteostasis and longevity

|supported by [88]|
|---|


. In sum, the critique provides a valuable corrective lens, but it may over-simplify the reciprocal relationship between structural integrity, redox homeostasis, and reproductive biology, thereby obscuring the nuanced, bidirectional network that underlies murine aging.

|*Authors’ comments: the report mainly agrees with the criticisms made by Virtual Junior Mouse|
|---|


|Researcher B.|
|---|


- • Agent: Virtual Junior Yeast Researcher A
- • Task: Investigate the associations between receptor activity, reproductive process and ageing processes in Saccharomyces cerevisiae.


Investigating the associations between receptor activity, reproductive processes, and aging in *Saccharomyces cerevisiae* involves examining specific signaling pathways triggered by mating pheromones,

which utilize G-protein coupled receptors (GPCRs) like the α-factor receptor. Activation of these receptors initiates a cascade leading to cell cycle arrest and mating

|supported by [89]|
|---|


,

|supported by [90]|
|---|


processes heavily influenced by nutrient availability

and

|supported by [91]|
|---|


stress signaling pathways

, including the Target of Rapamycin (TOR) pathway

|supported by [90]|
|---|


and nutrient sensing mechanisms

. These pathways are known to intersect

with aging determinants. For instance, nutrient-sensing pathways like TOR are conserved across eukaryotes and implicated in regulating lifespan; conditions mimicking nutrient limitation can extend yeast chronological lifespan

|supported by [92]|
|---|


. The reproductive process itself, particularly the energy demands and potential trade-offs with maintenance pathways, may influence aging. Studies suggest that mating can impact chronological lifespan through effects on stress response pathways, such as the Hog1 MAPK pathway involved in osmotic stress, which also plays roles in

|supported by [93]|
|---|


. Furthermore, the activity of specific receptors or their downstream effectors might influence the efficiency of cellular maintenance processes crucial for longevity, although the precise molecular links between specific receptor signaling, reproductive investment, and the conserved aging pathways (like those involving Sir2 family proteins/sirtuins

chronological aging

|supported by [94]|
|---|


|supported by [95]|
|---|


) require further detailed investigation to fully elucidate the complex interplay between mating, cellular signaling, and aging in yeast.

and mitochondrial function

|* Authors’ comments: the generated report can be validated by existing research articles.|
|---|


- • Agent: Virtual Junior Yeast Researcher B
- • Task: Provide critical comments against the report made by Virtual Junior Yeast Researcher A.


The provided text presents several critical oversimplifications and unsupported causal claims regarding receptor-mediated reproductive processes and aging in *S. cerevisiae*. Crucially, while the text correctly identifies that mating pheromone signalling through

|supported by [89]|
|---|


, it erroneously conflates mating-induced stress responses with general nutrient stress responses in the context of aging. Specifically, the assertion that mating “impacts chronological lifespan through effects on stress response pathways, such as the Hog1 MAPK pathway” is problematic;

GPCRs (e.g., Ste2) induces cell cycle arrest and mating

|supported by [96]|
|---|


Hog1 activation during mating is transient and primarily regulates osmotic stress

,

but its role in chronological aging is context-dependent and not universally required for lifespan extension under nutrient limitation, as evidenced by studies showing

|argued by [97]|
|---|


. Furthermore, the text makes a significant leap by suggesting “specific receptor activity or downstream effectors might influence the efficiency of cellular maintenance processes crucial for longevity” without providing concrete evidence linking α-factor receptor signaling directly to sirtuin activity (e.g., Sir2) or mitochondrial function – these are mechanistically distinct pathways where receptor signaling is not established as a primary regulator. The conclusion that “mating can impact chronological lifespan through effects on stress response pathways” is overly generalized, as mating itself is not the

Hog1 deletion mutants maintain near-normal chronological lifespan in standard conditions

|supported by [98]|
|---|


|supported by [99]|
|---|


; the text fails to adequately distinguish between the effects of mating *as an event* versus the downstream consequences of the nutrient-stress signaling crosstalk that accompanies it. Finally, the text neglects the well-established paradigm that chronological aging in yeast is primarily driven by quiescent cell metabolism

direct cause but rather a correlated event with nutrient sensing

|supported by [100]|
|---|


|supported by [101]|
|---|


, with mating pheromone signaling being a secondary factor at best, and does not sufficiently address the potential confounding role of cell-type heterogeneity (e.g., α-cell vs. a-cell differentiation) in these aging assays. The proposed “complex interplay” remains largely speculative without targeted genetic or proteomic evidence resolving these specific molecular links.

and mitochondrial respiration

|supported by [102]|
|---|


|* Authors’ comments: the criticisms are sensible and the majority of the scientific claims can be validated|
|---|


|by existing research articles.|
|---|


- • Agent: Virtual Senior Yeast Researcher
- • Task: Provide critical comments against the reports made by Virtual Junior Yeast Researcher A and Virtual Junior Yeast Researcher B.


The analysis highlights that the original narrative substantially overstates the influence of α-factor GPCR signaling on chronological lifespan in *S. cerevisiae*, conflating mating-induced, transient Hog1 activation with the broader, nutrient-sensing pathways that truly govern longevity; it ignores the fact that Hog1 deletion does not abolish lifespan extension under nutrient limitation

|supported by [97]|
|---|


,

thereby weakening the claim that mating-driven stress responses drive aging; it also fails to provide concrete mechanistic evidence linking receptor activity to sirtuin function

|supported by [98]|
|---|


or

|supported by [95]|
|---|


mitochondrial maintenance

), treating these distinct pathways as if they were directly

|supported by [100]|
|---|


coupled; furthermore, it neglects the dominant role of quiescent cell metabolism

|supported by [101]|
|---|


and mitochondrial respiration in chronological aging

, and disregards the confounding

|supported by [102]|
|---|


impact of cell-type heterogeneity (α- vs. a-cells) on aging assays

– overall, the proposed “complex interplay” remains speculative without targeted genetic or proteomic validation to establish the precise molecular bridges between mating pheromone signaling, maintenance pathways, and longevity.

|* Authors’ comments: the report mainly agrees with the criticisms made by Virtual Junior Yeast|
|---|


|Researcher B.|
|---|


- • Agent: Virtual Ageing Professor
- • Task: Provide critical comments against the reports made by Virtual Senior Worm Researcher, Virtual Senior Fruit Fly Researcher, Virtual Senior Mouse Researcher, and Virtual Senior Yeast Researcher.


Based on the text provided, here are critical comments regarding the arguments presented:

- **1. Generalizability to Mammals** The text relies heavily on findings from *Caenorhabditis elegans* (nematodes). While *C. elegans* is an invaluable model for understanding aging due to its short lifespan and genetic tractability, its physiology differs significantly from mammals. In mammals, aging is regulated by complex systemic factors, including the hypothalamus

|supported by [103]|
|---|


, endocrine systems

|supported by [104]|
|---|


, and

immune responses

|supported by [105]|
|---|


that nematodes lack. Therefore, while the argument that mitochondrial dysfunction is a “signaling hub” is compelling in *C. elegans*, its direct application to human aging is limited without further validation in mammalian models.

- **2. The Signaling vs. Damage Balance** The text correctly identifies Reactive Oxygen Species (ROS) as signaling molecules that activate adaptive

repair pathways (like the NRF2 pathway)

|supported by [106]|
|---|


. However, it arguably risks downplaying the

cumulative “vicious cycle” of mitochondrial damage

|supported by [107]|
|---|


. Even as ROS signals for repair,

chronic oxidative stress inevitably damages mitochondrial DNA (mtDNA) and lipids

|supported by [108]|
|---|


,

leading to loss of membrane potential and cellular senescence

|supported by [107]|
|---|


. The text frames dysfunction primarily as a regulatory signal, whereas in later stages of aging, the “damage” aspect often overwhelms the signaling capability.

- **3. Causality of Reproductive Decline** The text argues that reduced reproduction is a *consequence* of somatic aging rather than a genetic “trade-off.” While the data suggests that the *ability* to reproduce declines because the body is aging, evolutionary biology often suggests the reverse – that reproduction actively *causes*


|supported by [109]|
|---|


aging through resource allocation ( the “Disposable Soma” theory

). Therefore, the reduced reproduction could still be viewed as a trade-off where somatic maintenance is sacrificed to support reproduction. The text presents a correlation (reproduction stops because the body breaks down) without fully exploring the evolutionary cost of diverting resources to reproduction.

|* Authors’ comments: the report reveals crucial future research directions, e.g. transferring the knowledge|
|---|


|from worm to mammals and investigating the ageing theories from evolutionary perspectives.|
|---|


### 6 Discussions

Although the computational results suggest that the proposed VSG framework successfully extracts meaningful ageing-related biological knowledge from the given GO terms and the functionality of the multi-layer knowledge extraction mechanisms can be observed, there still exist limitations that need to be further addressed. To begin with, the hallucination issue still needs to be considered when consulting the knowledge generated by AI agents. For example, in the report generated by Virtual Junior Yeast Researcher B, the claim about Hog1 deletion mutants is argued by an existing research article. Also, there exists an unreal citation in the report generated by Virtual Junior Mouse Researcher B. Those two observations suggest a sign of hallucination-related issues, though the majority of the claims made by AI agents are genuine and correct. Moreover, the capacity of the proposed VSG framework for handling GO terms bearing more specific biological definitions still needs to be further evaluated. All of the GO terms investigated in this work are located in higher positions in the GO hierarchy, suggesting more generic biological definitions. However, validating those GO terms bearing more specific definitions would also be difficult, due to the lack of existing research, though the discovered knowledge might simultaneously provide new insights or hypotheses on future ageing research.

### 7 Conclusions and Future Directions

In this work, we propose a novel agentic AI-based knowledge discovery framework that successfully extracts meaningful ageing-related biological knowledge based on certain Gene Ontology terms selected by a well-known hierarchical feature selection method. Future research directions would be focused on extending the capacity of AI agents to further explore the possibility of discovering unknown ageing-related biological knowledge.

### References

- [1] Swanson, K., Wu, W., Bulaong, N.L., Pak, J.E., Zou, J.: The virtual lab of AI agents designs new SARS-CoV-2 nanobodies. Nature 646, 716–723 (2025)
- [2] Alsaggaf, I., Freitas, A.A., Wan, C.: Predicting the pro-longevity or anti-longevity effect of model organism genes with enhanced gaussian noise augmentation-based contrastive learning on protein-protein interaction networks. NAR Genomics and Bioinformatics 6, 153 (2024)
- [3] Paz-Ruza, J., Freitas, A.A., Alonso-Betanzos, A., Guijarro-Berdin˜as, B.: Positive-unlabelled learning for identifying new candidate dietary restriction-related genes among ageing-related genes. Computers in Biology and Medicine 180, 108999 (2024)
- [4] Gong, L., Elhoushi, M., Cheung, A.: AST-T5: structure-aware pretraining for code generation and understanding. In: The 41st International Conference on Machine Learning, pp. 15839–15853 (2024)
- [5] Chen, J., Yuan, S., Ye, R., Majumder, B.P., Richardson, K.: Put your money where your mouth is: Evaluating strategic planning and execution of LLM agents in an auction arena. arXiv, 2310–05746

(2024)

- [6] The Gene Ontology Consortium: Gene Ontology: tool for the unification of biology. Nature Genetics 25(1), 25–29 (2000)
- [7] Wan, C., Freitas, A.: Prediction of the pro-longevity or anti-longevity effect of caenorhabditis elegans genes based on bayesian classification methods. In: 2013 IEEE International Conference on Bioinformatics and Biomedicine, pp. 373–380 (2013)
- [8] Ristoski, P., Paulheim, H.: Feature selection in hierarchicalfeature spaces. In: 2014 International Conference on Discovery Science, pp. 288–300 (2014)
- [9] Wan, C., Freitas, A.A., De Magalh˜es, J.P.: Predicting the pro-longevity or anti-longevity effect of model organism genes with new hierarchical feature selection methods. IEEE/ACM Transactions on Computational Biology and Bioinformatics 12(2), 262–275 (2015)
- [10] Wan, C.: Hierarchical feature selection for knowledge discovery: Application of data mining to the biology of ageing (2019)


- [11] Da Silva, P.N., Plastino, A., Freitas, A.A.: Novel genetic algorithm for feature selection in hierarchical feature spaces. In: 2018 SIAM International Conference on Data Mining, pp. 738–746 (2018)
- [12] Da Silva, P.N., Plastino, A., Freitas, A.A.: Prioritizing positive feature values: a new hierarchical feature selection method. Applied Intelligence 50, 4412–4433 (2020)
- [13] Li, D., Wu, Q., Zhou, M., Luo, F.: HHFS: A hybridhierarchical feature selection method for ageing gene classification. IEEE Transactions on Cognitive and Developmental Systems 15, 690–699 (2022)
- [14] Wan, C., Barton, C.: A novel hierarchy-based knowledge discovery framework for elucidating human aging-related phenotypic abnormalities. In: 39th ACM/SIGAPP Symposium On Applied Computing, pp. 515–522 (2024)
- [15] Lu, J., Li, D., Wu, Q., Shao, J.: HFS-CSR: A hierarchical feature selection method based on correlation and structural redundancy. Expert Systems with Applications 262, 125660 (2025)
- [16] De Magalh˜es, J.P., Costa, J., Toussaint, O.: HAGR: the human ageing genomic resources. Nucleic Acids Research 33, 537–543 (2005)
- [17] Friedman, N., Geiger, D., Goldszmidt, M.: Bayesian network classifiers. Machine Learning 29, 131–163

(1997)

- [18] Wan, C., Freitas, A.A.: An empirical evaluation of hierarchical feature selection methods for classification in bioinformatics datasets with Gene Ontology-based features. Artificial Intelligence Review 50(2), 201– 240 (2018)
- [19] Wei, J., Tay, Y., Bommasani, R., et al.: Emergent abilities of large language models. arXiv, 2206–07682

(2022)

- [20] Zhao, W.X., Zhou, K., Li, J., et al.: A survey of large language models. arXiv, 2303–18223 (2026)
- [21] Jiang, J., Wang, F., Shen, J., Kim, S., Kim, S.: A survey on large language models for code generation. arXiv, 2406–00515 (2024)
- [22] Ahmad, W., Chakraborty, S., Ray, B., Chang, K.-W.: Unified pre-training for program understanding and generation. In: 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, pp. 2655–2668 (2021)
- [23] Xu, F., Hao, Q., Zong, Z., et al.: Towards large reasoning models: A survey of reinforced reasoning with large language models. arXiv, 2501–09686 (2025)
- [24] Lightman, H., Kosaraju, V., Burda, Y., Edwards, H., Baker, B., Lee, T., Leike, J., Schulman, J., Sutskever, I., Cobbe, K.: Let’s verify step by step. arXiv, 2305–200501 (2023)
- [25] Besta, M., Blach, N., Kubicek, A., Gerstenberger, R., Podstawski, M., Gianinazzi, L., Gajda, J., Lehmann, T., Niewiadomski, H., Nyczyk, P., Hoefler, T.: Graph of thoughts: Solving elaborate problems with large language models. arXiv, 2308–096874 (2024)
- [26] Wei, H., Zhang, Z., He, S., Xia, T., Pan, S., Liu, F.: PlanGenLLMs: A modern survey of llm planning capabilities. arXiv, 2502–11221 (2025)
- [27] Chen, Z., Chen, D., Sun, R., Liu, W., Gan, C.: Scaling autonomous agents via automatic reward modeling and planning. arXiv, 2502–12130 (2025)
- [28] Dagdelen, J., Dunn, A., Lee, S., Walker, N., Rosen, A.S., Ceder, G., Persson, K.A., Jain, A.: Structured information extraction from scientific text with large language models. Nature Communications 15, 1418 (2024)
- [29] Balasubramanian, J.B., Adams, D., Roxanis, I., De Gonzalez, A.B., Coulson, P., Almeida, J.S., Garc´ıaClosas, M.: Leveraging large language models for structured information extraction from pathology reports. Journal of Pathology Informatics 19, 100521 (2025)


- [30] Builtjes, L.B., Bosma, J., Prokop, M., Van Ginneken, B., Hering, A.: Leveraging open-source large language models for clinical information extraction in resource-constrained settings. Journal of the American Medical Informatics Association Open 8, 109 (2025)
- [31] Wooldridge, M.: An Introduction to MultiAgent Systems. John Wiley & Sons, Chichester (2009)
- [32] Ruan, Y., Lu, C., Xu, N., He, Y., Chen, Y., Zhang, J., Xuan, J., Pan, J., Fang, Q., Gao, H., Shen, X., Ye, N., Zhang, Q., Mo, Y.: An automatic end-to-end chemical synthesis development platform powered by large language models. Nature Communications, 10160 (2024)
- [33] Schmidgall, S., Su, Y., Wang, Z., Sun, X., Wu, J., Yu, X., Liu, J., Michael, M., Liu, Z., Barsoum, E.: Agent laboratory: Using LLM agents as research assistants. In: Findings of the Association for Computational Linguistics: EMNLP 2025, pp. 5977–6043 (2025)
- [34] Gosmar, D., Dahl, D.A.: Hallucination mitigation using agentic AI natural language-based frameworks. arXiv, 2501–139461 (2025)
- [35] CrewAI: CrewAI Repositories. https://github.com/crewAIInc/crewAI [Accessed: 2026-03-04] (2023)
- [36] Ollama: Ollama Repositories. https://github.com/ollama/ollama [Accessed: 2026-03-04] (2023)
- [37] Guo, D., Yang, D., Zhang, H., et al.: Deepseek-R1 incentivizes reasoning in LLMs through reinforcement learning. Nature 645, 633–638 (2025)
- [38] Bai, S., Cai, Y., Chen, R., et al.: Qwen3-VL technical report. arXiv, 2511–21631 (2025)
- [39] OpenAI: Introducing gpt-oss. https://openai.com/index/introducing-gpt-oss/ [Accessed: 2026-03-04]

(2025)

- [40] AI, Z.: GLM-4.7-Flash. https://huggingface.co/zai-org/GLM-4.7-Flash [Accessed: 2026-03-04] (2026)
- [41] De Henau, S., Tilleman, L., Vangheel, M., Luyckx, E., Trashin, S., Pauwels, M., Germani, F., Vlaeminck, C., Vanfleteren, J.R., Bert, W., Pesce, A., Nardini, M., Bolognesi, M., De Wael, K., Moens, L., Dewilde, S., Braeckman, B.P.: A redox signalling globin is essential for reproduction in Caenorhabditis elegans. Nature Communications 6, 8782 (2015)
- [42] Melov, S., Ravenscroft, J., Malik, S., Gill, M.S., Walker, D.W., Clayton, P.E., Wallace, D.C., Malfroy, B., Doctrow, S.R., Lithgow, G.J.: Extension of life-span with superoxide dismutase/catalase mimetics. Science 289, 5484 (2000)
- [43] Martins, R., Lithgow, G.J., Link, W.: Long live FOXO: unraveling the role of FOXO proteins in aging and longevity. Aging Cell 15, 196–207 (2015)
- [44] Bansal, A., Kwon, E.-S., Darryl, C., Liu, H., Gilchrist, M.J., MacNeil, L.T., Tissenbaum, H.A.: Transcriptional regulation of Caenorhabditis elegans FOXO/DAF-16 modulates lifespan. Longevity and Healthspan 3, 5 (2014)
- [45] Felkai, S., Ewbank, J.J., Lemieux, J., Labb´e, J., Brown, G.G., Hekimi, S.: CLK-1 controls respiration, behavior and aging in the nematode Caenorhabditis elegans. The EMBO Journal 18, 1783–1792 (1999)
- [46] Wei, Y., Kenyon, C.: Roles for ROS and hydrogen sulfide in the longevity response to germline loss in Caenorhabditis elegans. Proceedings of the National Academy of Sciences 113, 2832–2841 (2016)
- [47] Arantes-Oliveira, N., Apfeld, J., Dillin, A., Cynthia, K.: Regulation of life-span by germ-line stem cells in Caenorhabditis elegans. Science 295, 502–505 (2002)
- [48] Liu, J.-L., Yee, C., Wang, Y., Hekimi, S.: A single biochemical activity underlies the pleiotropy of the aging-related protein CLK-1. Scientific Reports 7 (2017)
- [49] Wang, Y., Hekimi, S.: Mitochondrial dysfunction and longevity in animals: Untangling the knot. Science 350, 1204–1207 (2015)


- [50] Budovskaya, Y.V., Wu, K., Southworth, L.K., Jiang, M., Tedesco, P., Johnson, T.E., Kim, S.K.: An elt-3/elt-5/elt-6 GATA transcription circuit guides aging in C. elegans. Cell 134, 291–303 (2016)
- [51] Tullet, J.M.A., Araiz, C., Sanders, M.J., Au, C., Benedetto, A., Papatheodorou, I., Clark, E., Kathrin, S., Jones, D., Schuster, E.F., Thornton, J.M., Gems, D.: DAF-16/FoxO directly regulates an atypical amp-activated protein kinase gamma isoform to mediate the effects of insulin/IGF-1 signaling on aging in Caenorhabditis elegans. PLoS Genetics 10, 1004109 (2014)
- [52] Uno, M., Nishida, E.: Lifespan-regulating genes in C. elegans. npj Aging and Mechanisms of Disease 2, 16010 (2016)
- [53] Demarco, R.S., Jones, D.L.: Redox signaling as a modulator of germline stem cell behavior: Implications for regenerative medicine. Free Radical Biology and Medicine 166, 67–72 (2022)
- [54] Butow, R.A., Avadhani, N.G.: Mitochondrial signaling: The retrograde response. Molecular Cell 14, 1–15 (2004)
- [55] Walker, G., Houthoofd, K., Vanfleteren, J.R., Gems, D.: Dietary restriction in C. elegans: From rateof-living effects to nutrient sensing pathways. Mechanisms of Ageing and Development 126, 929–937

(2005)

- [56] Zhang, A., Meecham-Garcia, G., Hong, C.N., Xie, P., Kern, C.C., Zhang, B., Chapman, H., Gems, D.: Characterization of effects of mTOR inhibitors on aging in Caenorhabditis elegans. The Journals of Gerontology: Series A 74, 196 (2024)
- [57] Kniazeva, M., Ruvkun, G.: Rhizobium induces DNA damage in Caenorhabditis elegans intestinal cells. Proceedings of the National Academy of Sciences 116, 3784–3792 (2019)
- [58] Lee, G.D., Wilson, M.A., Zhu, M., Wolkow, C.A., Cabo, R., Ingram, D.K., Zou, S.: Dietary deprivation extends lifespan in Caenorhabditis elegans. Aging Cell 5, 515–524 (2008)
- [59] Longo, V.D., Fontana, L.: Intermittent supplementation with rapamycin as a dietary restriction mimetic. Aging (Albany NY) 3, 1039–1040 (2011)
- [60] Ferguson, M., Mockett, R.J., Shen, Y., Orr, W.C., Sohal, R.S.: Age-associated decline in mitochondrial respiration and electron transport in Drosophila melanogaster. Biochemical Journal 390, 501–511 (2005)
- [61] Brandt, T., Mourier, A., Tain, L.S., Partridge, L., Larsson, N.-G., Ku¨hlbrandt, W.: Changes of mitochondrial ultrastructure and function during ageing in mice and Drosophila. eLife 6, 24662 (2017)
- [62] Rodrigues, M.A., Flatt, T.: Endocrine uncoupling of the trade-off between reproduction and somatic maintenance in eusocial insects. Current Opinion in Insect Science 16, 1–8 (2016)
- [63] Fredriksson, ˚A., Krogh, E.J., Hernebring, M., Pettersson, E., Javadi, A., Almstedt, A., Nystr¨m, T.: Effects of aging and reproduction on protein quality control in soma and gametes of Drosophila melanogaster. Ageing Cell 11, 634–643 (2012)
- [64] H¨lzl, H., Kapelari, B., Kellermann, J., Seemu¨ller, E., S¨umegi, M., Udvardy, A., Medalia, O., Sperling, J., Mu¨ller, S.A., Engel, A., Baumeister, W.: The regulatory complex of Drosophila melanogaster 26s proteasomes. Journal of Cell Biology 150, 119–130 (2000)
- [65] Jensen, M.B., Qi, Y., Riley, R., Rabkina, L., Jasper, H.: PGAM5 promotes lasting FoxO activation after developmental mitochondrial stress and extends lifespan in Drosophila. eLife 6, 26952 (2017)
- [66] Rodrı´guez-V´zquez, M., Falconi, J., Heron-Milhavet, L., Lassus, P., G´eminard, C., Djiane, A.: Fat body glycolysis defects inhibit mtor and promote distant muscle disorganization through TNF-α/egr and ImpL2 signaling in Drosophila larvae. EMBO Reports 25, 4410–4432 (2024)
- [67] Barton, L.J., Duan, T., Ke, W., Luttinger, A., Lovander, K.E., Soshnev, A.A., Geyer, P.K.: Nuclear lamina dysfunction triggers a germline stem cell checkpoint. Nature Communications 9 (2018)
- [68] Salmon, A.B., Marx, D.B., Harshman, L.G.: A cost of reproduction in Drosophila melanogaster: stress


- susceptibility. Evolution 5, 1600–1608 (2001)
- [69] Qiu, S., Xiao, C., Robertson, R.M.: Different age-dependent performance in Drosophila wild-type Canton-S and the white mutant w1118 flies. Comparative Biochemistry and Physiology Part A: Molecular and Integrative Physiology 206, 17–23 (2017)
- [70] Lin, X.-W., Tang, L., Yang, J., Xu, W.-H.: HIF-1 regulates insect lifespan extension by inhibiting cMyc-TFAM signaling and mitochondrial biogenesis. Biochimica et Biophysica Acta (BBA) - Molecular Cell Research 1863, 2594–2603 (2016)
- [71] Morris, O., Deng, H., Tam, C., Jasper, H.: Warburg-like metabolic reprogramming in aging intestinal stem cells contributes to tissue hyperplasia. Cell Reports 33, 108423 (2020)
- [72] Gonzalo, S., Kreienkamp, R., Askjaer, P.: Hutchinson-Gilford progeria syndrome: a premature aging disease caused by LMNA gene mutations. Ageing Research Reviews 33, 18–29 (2018)
- [73] Eira, J., Silva, C.S., Sousa, M.M., Liz, M.A.: The cytoskeleton as a novel therapeutic target for old neurodegenerative disorders. Progress in Neurobiology 141, 61–82 (2016)
- [74] Jena, A.B., Samal, R.R., Bhol, N.K., Duttaroy, A.K.: Cellular Red-Ox system in health and disease: The latest update. Biomedicine and Pharmacotherapy 162, 114606 (2023)
- [75] Osburn, W.O., Wakabayashi, N., Misra, V., Nilles, T., Biswal, S., Trush, M.A., Kensler, T.W.: Nrf2 regulates an adaptive response protecting against oxidative damage following diquat-mediated formation of superoxide anion. Archives of Biochemistry and Biophysics 454, 7–15 (2006)
- [76] Olmos, Y., Valle, I., Borniquel, S., Tierrez, A., Soria, E., Lamas, S., Monsalve, M.: Mutual dependence of foxo3a and PGC-1α in the induction of oxidative stress genes. Journal of Biological Chemistry 284, 14476–14484 (2009)
- [77] Mitchell, S.E., Simpson, M., Coulet, L., Gouedard, S., Hambly, C., Morimoto, J., Allison, D.B., Speakman, J.R.: Reproduction has immediate effects on female mortality, but no discernible lasting physiological impacts: A test of the disposable soma theory. Proceedings of the National Academy of Sciences 121, 2408682121 (2024)
- [78] Lee, M.J., Agrahari, G., Kim, H.-Y., An, E.-J., Chun, K.-H., Kang, H., Kim, Y.-S., Bang, C.W., Tak, L.J., Kim, T.-Y.: Extracellular superoxide dismutase prevents skin aging by promoting collagen production through the activation of AMPK and Nrf2/HO-1 cascades. Journal of Investigative Dermatology 141, 2344–23537 (2021)
- [79] Huang, Y., Kang, B.N., Tian, J., Liu, Y., Luo, H.R., Hester, L., Snyder, S.H.: The cationic amino acid transporters CAT1 and CAT3 mediate NMDA receptor activation-dependent changes in elaboration of neuronal processes via the mammalian target of Rapamycin mTOR pathway. Journal of Neuroscience 27, 449–458 (2007)
- [80] Earle, A.J., Kirby, T.J., Fedorchak, G.R., Isermann, P., Patel, J., Iruvanti, S., Moore, S.A., Bonne, G., Wallrath, L.L., Lammerding, J.: Mutant lamins cause nuclear envelope rupture and DNA damage in skeletal muscle cells. Nature Materials 19, 464–473 (2020)
- [81] Garratt, M., Vasilaki, A., Stockley, P., McArdle, F., Jackson, M., Hurst, J.L.: Is oxidative stress a physiological cost of reproduction? An experimental test in house mice. Proceedings of the Royal Society B: Biological Sciences 278, 1098–1106 (2011)
- [82] Templeman, N.M., Murphy, C.T.: Regulation of reproduction and longevity by nutrient-sensing pathways. Journal of Cell Biology 217, 93–106 (2018)
- [83] Berryman, D.E., Christiansen, J.S., Johannsson, G., Thorner, M.O., Kopchick, J.J.: Role of the GH/IGF1 axis in lifespan and healthspan: lessons from animal models. Growth Hormone and IGF Research 18, 455–471 (2008)
- [84] Li, Q., Ren, J.: Influence of cardiac-specific overexpression of insulin-like growth factor 1 on lifespan


- and aging-associated changes in cardiac intracellular Ca2+ homeostasis, protein damage and apoptotic protein expression. Aging Cell 6, 799–806 (2007)
- [85] Inci, G., Warkad, M.S., Kang, B.-G., Kim, S.-O., Lee, N.-K., Heo, J.-I., Park, S.-H., Kim, J.-H., Kang, H.J., Kim, C.-H., Kim, B.-H., Park, S.-J., Suh, J.G., Kim, S.-C., Lim, S.S., Lee, J.-Y.: FOXO3a upregulates DNA repair activities by transcriptional activation of target genes and provides the resistance to gamma radiation and the extension of lifespan in mouse. Biogerontology 26, 196 (2025)
- [86] Wang, X., Hu, Z., Hu, J., Du, J., Mitch, W.E.: Insulin resistance accelerates muscle protein degradation: Activation of the ubiquitin-proteasome pathway by defects in muscle cell signaling. Endocrinology 147, 4160–4168 (2006)
- [87] James, H.A., O’Neill, B.T., Nair, K.S.: Insulin regulation of proteostasis and clinical implications. Cell Metabolism 26, 310–323 (2021)
- [88] Ristow, M., Schmeisser, K.: Mitohormesis: Promoting health and lifespan by increased levels of reactive oxygen species (ROS). Dose Response 12, 288–341 (2014)
- [89] Bardwell, L.: A walk-through of the yeast mating pheromone response pathway. Peptides 26, 339–350

(2011)

- [90] Vallejo, B., Matallana, E., Aranda, A.: Saccharomyces cerevisiae nutrient signaling pathways show an unexpected early activation pattern during winemaking. Microbial Cell Factories 19 (2020)
- [91] Garrington, T.P., Johnson, G.L.: Organization and regulation of mitogen-activated protein kinase signaling pathways. Current Opinion in Cell Biology 11, 211–218 (1999)
- [92] Evans, D.S., Kapahi, P., Hsueh, W.-C., Kockel, L.: TOR signaling never gets old: aging, longevity and TORC1 activity. Ageing Research Reviews 10, 225–237 (2011)
- [93] Chen, K., Shen, W., Zhang, Z., Xiong, F., Ouyang, Q., Luo, C.: Age-dependent decline in stress response capacity revealed by proteins dynamics analysis. Scientific Reports 10, 15211 (2020)
- [94] Lu, S.-P., Lin, S.-J.: Regulation of yeast sirtuins by NAD+ metabolism and calorie restriction. Biochimica et Biophysica Acta (BBA) - Proteins and Proteomics 1804, 1567–1575 (2009)
- [95] Hughes, A.L., Gottschling, D.E.: An early age increase in vacuolar pH limits mitochondrial function and lifespan in yeast. Nature 492, 1261–1265 (2012)
- [96] Nagiec, M.J., Dohlman, H.G.: Checkpoints in a yeast differentiation pathway coordinate signaling during hyperosmotic stress. PLoS Genetics 8, 1002437 (2012)
- [97] Masumura, K., Matsukami, S., Yonekita, K., Kanai, M., Kume, K., Hirata, D., Mizunuma, M.: SKO1 deficiency extends chronological lifespan in Saccharomyces cerevisiae. Bioscience, Biotechnology, and Biochemistry 83, 1473–1476 (2019)
- [98] Pozniakovsky, A.I., Knorre, D.A., Markova, O.V., Hyman, A.A., Skulachev, V.P., Severin, F.F.: Role of mitochondria in the pheromone- and amiodarone-induced programmed death of yeast. Journal of Cell Biology 168, 257–269 (2005)
- [99] Conrad, M., Schothorst, J., Kankipati, H.N., Van Zeebroeck, G., Rubio-Texeira, M., Thevelein, J.M.: Nutrient sensing and signaling in the yeast Saccharomyces cerevisiae. FEMS Microbiology Reviews 38, 254–299 (2014)
- [100] Cao, L., Tang, Y., Quan, Z., Zhang, Z., Oliver, S.G., Zhang, N.: Chronological lifespan in yeast is dependent on the accumulation of storage carbohydrates mediated by Yak1, Mck1 and Rim15 kinases. PLoS Genetics 12, 1006458 (2016)
- [101] Ocampo, A., Liu, J., Schroeder, E.A., Shadel, G.S., Barrientos, A.: Mitochondrial respiratory thresholds regulate yeast chronological life span and its extension by caloric restriction. Cell Metabolism 16, 55–67


(2012)

- [102] Hanson, S.J., Wolfe, K.H.: An evolutionary perspective on yeast mating-type switching. Genetics 206, 9–32 (2017)
- [103] Hajdarovic, K.H., Yu, D., Webb, A.E.: Understanding the aging hypothalamus, one cell at a time. Trends in Neurosciences 45, 942–954 (2022)
- [104] Chahal, H.S., Drake, W.M.: The endocrine system and ageing. The Journal of Pathology 211, 173–180

(2007)

- [105] Terekhova, M., Bohacova, P., Artyomov, M.N.: Human immune aging. Immunity 58, 2646–2669 (2025)
- [106] Almeida, A.J.P.O., Oliveira, J.C.P.L., Silva Pontes, L.V., Souza J´unior, J.F., Gon¸calves, T.A.F., Dantas, S.H., Almeida Feitosa, M.S., Silva, A.O., Medeiros, I.A.: ROS: Basic concepts, sources, cellular signaling, and its implications in aging pathways. Oxidative Medicine and Cellular Longevity, 1225578 (2022)
- [107] Xu, X., Pang, Y., Fan, X.: Mitochondria in oxidative stress, inflammation and aging: from mechanisms to therapeutic advances. Signal Transduction and Targeted Therapy 10 (2025)
- [108] Wang, X., Wang, W., Li, L., Perry, G., Lee, H.-g., Zhu, X.: Oxidative stress and mitochondrial dysfunction in Alzheimer’s disease. Biochimica et Biophysica Acta (BBA) - Molecular Basis of Disease 1842, 1240–1247 (2014)
- [109] Kirkwood, T.B.L.: The disposable soma theory. In: Shefferson, R.P., Jones, O.R., Salguero-G´mez, R. (eds.) The Evolution of Senescence in the Tree of Life, pp. 23–39. Cambridge University Press, Cambridge


(2017)

