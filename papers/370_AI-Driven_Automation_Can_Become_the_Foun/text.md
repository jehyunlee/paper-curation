arXiv:2505.12039v1[cs.AI]17 May 2025

# AI-Driven Automation Can Become the Foundation of Next-Era Science of Science Research

#### Renqi Chen1,∗, Haoyang Su1,∗, Shixiang Tang1,6, Zhenfei Yin2, Qi Wu3, Hui Li3, Ye Sun4, Nanqing Dong1,5,†,

Wanli Ouyang1,6, Philip Torr2 1Shanghai Artificial Intelligence Laboratory. 2Department of Engineering Science, University of Oxford.

- 3Shanghai Institute for Science of Science.
- 4School of Mathematics, Southeast University. 5Shanghai Innovation Institute.


6Department of Information Engineering, Chinese University of Hong Kong.

Abstract The Science of Science (SoS) explores the mechanisms underlying scientific discovery, and offers valuable insights for enhancing scientific efficiency and fostering innovation. Traditional approaches often rely on simplistic assumptions and basic statistical tools, such as linear regression and rule-based simulations, which struggle to capture the complexity and scale of modern research ecosystems. The advent of artificial intelligence (AI) presents a transformative opportunity for the next generation of SoS, enabling the automation of large-scale pattern discovery and uncovering insights previously unattainable. This paper offers a forward-looking perspective on the integration of Science of Science with AI for automated research pattern discovery and highlights key open challenges that could greatly benefit from AI. We outline the advantages of AI over traditional methods, discuss potential limitations, and propose pathways to overcome them. Additionally, we present

∗Equal contributions. †Corresponding authors: Nanqing Dong (dongnanqing@pjlab.org.cn).

###### 1

a preliminary multi-agent system as an illustrative example to simulate research societies, showcasing AI’s ability to replicate real-world research patterns and accelerate progress in Science of Science research.

## 1 Introduction

Science of Science (SoS), a pivotal and rapidly evolving field, serves as a strategic compass for guiding the trajectory of scientific and technological progress. By analyzing the complex dynamics of research collaboration and scientific output across geographic and temporal scales, it sheds light on the factors that drive creativity and the emergence of scientific discoveries, with the goal of developing tools and policies to accelerate scientific advancement [1]. Unlike broader social sciences that examine societal structures, SoS delves deep into the mechanisms that fuel scientific breakthroughs [2– 4]—illuminating the hidden forces that propel discovery and transformation. Ultimately, SoS underscores that groundbreaking advancements are not solely the result of talented minds and quality data, but are profoundly shaped by effective resource allocation, supportive policies and well-designed organizational structures [5, 6].

In recent years, the deep fusion of AI and SoS has become more feasible and promising than ever before. First, the increasing availability of large-scale scholarly data—publications, funding records, and collaboration networks—provides unprecedented opportunities to gain deeper insights into the evolution of scientific progress. Second, rapid advancements in AI technologies, such as large language models (LLMs), along with improvements in computational power, have greatly enhanced our ability to analyze and interpret complex scientific information with unprecedented accuracy and scale. These technological breakthroughs mark a critical moment for integrating AI into SoS, paving the way for a more data-driven approach to understanding and guiding research pattern discovery. While some recent works have begun exploring autonomous scientific discovery, the field remains in its infancy, and there is still much progress to be made before realizing its full potential.

In this paper, we take a step forward by providing the first glimpse into the integration of AI and SoS for automated research pattern discovery. We take the position that AI has the potential to revolutionize SoS, enabling the next generation of research by not only automating traditional research processes but also providing a sandbox for SoS research, allowing scientists to observe research processes in action and validate their hypotheses. As illustrated in Fig. 1, traditional SoS methods have primarily relied on manual data processing, bibliometric-based data analysis, rule-based system simulations, and real-world pattern validation. In contrast, AI-driven SoS leverages automated techniques to assist scientists

4. Real-world pattern validation

4. Virtual-world pattern validation

![image 1](Chen et al._2025_AI-Driven Automation Can Become the Foundation of Next-Era Science of Science Research_images/imageFile1.png)

![image 2](Chen et al._2025_AI-Driven Automation Can Become the Foundation of Next-Era Science of Science Research_images/imageFile2.png)

![image 3](Chen et al._2025_AI-Driven Automation Can Become the Foundation of Next-Era Science of Science Research_images/imageFile3.png)

![image 4](Chen et al._2025_AI-Driven Automation Can Become the Foundation of Next-Era Science of Science Research_images/imageFile4.png)

3.Deep learning system simulation

system simulation

data processing

1.AI-assisted data processing

- 3.Rule-based


1.Manual

Human-Driven research process

AI-Driven research process

![image 5](Chen et al._2025_AI-Driven Automation Can Become the Foundation of Next-Era Science of Science Research_images/imageFile5.png)

![image 6](Chen et al._2025_AI-Driven Automation Can Become the Foundation of Next-Era Science of Science Research_images/imageFile6.png)

![image 7](Chen et al._2025_AI-Driven Automation Can Become the Foundation of Next-Era Science of Science Research_images/imageFile7.png)

2. Bibliometric-based data analysis

2. AI-based data analysis

- Figure 1: An illustration comparing human-driven and AI-driven research processes in the SoS, highlighting step-by-step differences across four key stages in order: data processing, data analysis, system simulation, and pattern validation.


in processing and analyzing data while offering more advanced and comprehensive systems for simulation and validation. This shift from human-driven to AI-driven methodologies unlocks the potential for more efficient, scalable, and data-driven analysis, ultimately providing deeper and more actionable insights into the mechanisms that shape scientific progress. Thus, we define AI for SoS (AI4SoS) as a cross-disciplinary field that not only focuses on facilitating each step within the research process but also aims to achieve fully automated SoS research to uncover the hidden forces driving scientific innovation. This distinguishes AI4SoS from existing AI for Science approaches, which focus on using AI tools to solve domain-specific scientific problems [7–9].

To consolidate our insights, we propose a forward-looking hierarchy of different levels of AI4SoS automation in Sec. 2.3, which outlines a possible step-by-step approach to achieving the goal of fully automated SoS discovery. Within each level, we describe the key differences compared to previous levels and provide related examples. In Sec. 3, we highlight critical open problems in SoS where AI offers advantages. Despite its promise, we discuss challenges such as data imbalance across disciplines in Sec. 4, overwhelming parameters in the simulation system of scientific societies, and the need for a reasonable evaluation system to validate the reliability of the simulation. We also propose possible pathways to overcome these challenges. Last but not least, we introduce a preliminary multi-agent system to simulate research societies in Sec. 5, illustrating AI’s capability to enable fully automated pattern discovery.

Table 1: Comparison between AI for Science and AI for Science of Science. Feature AI for Science AI for Science of Science Focus Solving domain-specific

Understanding mechanisms of scientific progress.

scientific problems.

Approach Direct application of AI to

Meta-level analysis to enhance the research process.

address scientific challenges.

Examples Predicting weather,

Studying research collaboration trends, analyzing innovation triggers, mapping knowledge growth.

designing new drugs, optimizing materials.

## 2 AI for Science of Science

### 2.1 Definition

AI for SoS (AI4SoS) refers to the application of AI techniques to analyze, simulate, and validate the pattern of scientific research. It aims to leverage AI to study key aspects of the scientific ecosystem, including research productivity (e.g. individual published paper count), citation pattern (e.g. frequency and manner of citations), collaboration network (e.g. interdisciplinary research collaboration), and the factors driving the advancement of scientific knowledge (e.g. funding and policy). Specifically, AI can drive the research process of SoS by automatically applying methods such as machine learning, data mining, and computational simulations, thereby uncovering scientific patterns.

### 2.2 Comparison between AI for Science and AI4SoS

Both AI for Science (AI4S) and AI4SoS aim to leverage AI to solve scientific problems. However, they differ in research goals. AI4S focuses on solving a particular scientific problem directly, such as weather prediction, drug discovery, and materials science. AI4SoS takes a meta-level approach, focusing on understanding the mechanisms of scientific progress to facilitate and accelerate research. More specifically, AI4SoS focuses on factors such as innovation drivers, research collaboration patterns, and the evolution of scientific knowledge, which are not bound to a single scientific problem.

### 2.3 Hierarchy of Automation Degree in AI4SoS

The integration of AI techniques into scientific research follows a progressive hierarchy, reflecting the increasing autonomy and sophistication of AI systems in advancing the SoS field. As illustrated in Fig. 2, we define five levels of autonomy, ranging from no AI involvement in pattern recognition and analysis to full autonomy in uncovering new scientific insights and guiding research strategies.

Research Process

|e.g., Social experiments|
|---|


|e.g., A simulated society for collaboration pattern discovery, …|
|---|


Pattern Validation

|e.g., Rule-based<br><br>simulation|
|---|


|e.g., Multi-agent systems for simulating specific research scenarios to propose hypotheses or<br><br>reproduce historical events, …|
|---|


System Simulation

|e.g., Machine learning models for predicting individual paper citation<br><br>counts, neural networks for forecasting research trends and generating unexpected ideas, …|
|---|


|e.g., Correlation analysis for variable relationships|
|---|


Data Analysis

|e.g., Manual data cleaning|
|---|


|e.g., Text-to-Embedding methods for mapping papers to vector space, named entity recognition for extracting key information from papers, …|
|---|


Data Processing

Level 0: Level 1: Level 2: Level 3: Level 4:

Autonomy Levels

Non-automated Assisted Partially Automated Highly Automated Fully Automated

- Figure 2: An overview of the five progressively advancing levels of autonomy in AI4SoS, with more green areas indicating that higher levels correspond to greater degrees of autonomy. Current research is primarily at Level 2 or below, with very limited work at Level 3, while fully automated SoS discovery remains in the prospective stage.


- Level 0: Non-automated SoS Discovery At this level, scientific pattern discovery is entirely human-driven and relies on traditional statistical methods. Researchers apply fundamental techniques such as probabilistic models, linear regression, and hypothesis testing to analyze scientific data and uncover patterns. AI is not involved in the process, and all tasks are conducted manually using well-established statistical procedures. Notable studies in this domain include the application of regression analysis to identify research trends [10], correlation analysis to examine relationships between variables [11], and statistical estimation methods to explain observed scientific phenomena [12, 13].
- Level 1: AI-Assisted SoS Discovery In Level 1, AI only supports scientific data processing. Specifically, AI methods are able to transform real-world scientific data into a more comprehensible form, including tasks such as completing and structuring bibliometric data, extracting key features such as author networks and institutional collaborations, and converting text information (e.g., papers, scientists) into embedding representations, thereby enhancing the efficiency and accuracy of data handling. However, AI’s role remains supplementary, with human researchers still conducting data analysis, understanding and prediction. From the perspective of AI4SoS, some related works include: utilizing text-to-embedding methods for mapping papers to vector space [14], extracting key information from papers using named entity recognition [15], and constructing networks for faculty mobility [16].
- Level 2: Partially Automated SoS Discovery In Level 2, AI techniques (e.g., supervised learning), play a central role in analyzing scientific data, enabling tasks such as predicting emerging trends, research hotspots and collaboration opportunities, based on historical patterns. This marks a shift from AI-assisted data processing to AI-driven data analysis. However, in this level, AI struggles to design and implement experiments automatically. For instance, a simulation environment that can automatically conduct scientific experiments is not available, therefore it is difficult to model hidden dynamic


- processes within the scientific ecosystem. Related works include the use of machine learning models to predict individual paper citation counts [17], neural networks for forecasting research trends and generating novel ideas [18], clustering publications based on citation relationships [19], and applying structural topic models to extract topics from scientific texts [20].
- Level 3: Highly Automated SoS Discovery In Level 3, AI not only drives the analysis but also designs and implements experiments to simulate scientific patterns in the real world. In this case, researchers can compare results generated by simulation systems and those in the real world to explore strategies in SoS for potential real-world applications. While AI can support automatic experiment conduction, human supervision is required to define the specific application scenarios and corresponding experimental parameters (e.g., scientist information, boundary conditions) based on system feedback. Consequently, the authenticity and rationality of the system depends on whether the researchers have considered all relevant factors, making the automatic pattern validation difficult. Research at this level is still in its early stages, including systems simulating specific research scenarios to propose hypotheses [21], AI predicting outcomes under different simulation conditions to provide insights into collaboration patterns [22]. and systems reproducing historical events based on specific environmental settings [23].
- Level 4: Fully Automated SoS Discovery Level 4, the ultimate stage, represents complete automatic discovery in SoS. An AI-based virtual research society is conducted for end-to-end SoS discovery, including pattern analysis, prediction, and validation. Compared to systems in Level 3, systems in Level


- 4 function with continuous AI-based feedback loops to autonomously assess research plans and results to dynamically adjust parameters such as experimental settings, enabling virtual-world pattern validation as an alternative to real-world social experiments that may be aggressive. At this stage, novel scientific insights can be uncovered without human intervention, and systems can adapt to new data and incorporate new insights in real time. Furthermore, ethical and governance frameworks are embedded, aligning the system’s actions with established guidelines for scientific integrity and accountability.


Currently, most research remains at Level 2 or below, with only limited progress observed at Level 3, while fully automated SoS discovery is still in the exploratory stage. Looking ahead, several potential tasks are envisioned, including automated discovery of new collaboration patterns within the simulated scientific community [22], systems capable of simulating and conducting experiments in real-world settings [24], and AI that continuously refines research directions based on emerging data [25].

## 3 Advantages of Automatic SoS Discovery

In this section, we delve into critical open problems within the SoS that stand to benefit substantially from AI-driven automation. These problems are categorized into two primary areas: Forecasting Trends in Technology and

Innovation and Understanding the Dynamics of Research Society. For each subproblem, we provide a brief background and outline key opportunities where AI offers advantages.

### 3.1 Forecasting Trends in Technology and Innovation

##### 3.1.1 Background of Problem

Accurately forecasting the trajectory of science and technology is a crucial aspect of SoS, as it informs decisions related to funding, policy-making, and research prioritization. Two major challenges are predicting technological trends and identifying interdisciplinary opportunities.

The Trend in Technological Development Technological development follows intricate and often non-linear trajectories, making prediction difficult. To predict these trends, it is essential to understand which technologies are gaining momentum, identify emerging breakthroughs, and anticipate when they will transition from research to real-world applications [26]. Traditional methods, such as historical data analysis, often fall short in scalability and struggle to keep pace with rapid advancements.

The Interdisciplinary Future of Innovation Interdisciplinary research, which often serves as the pivotal role for major breakthroughs, presents another significant challenge. With the rapid growth of scientific literature across diverse fields, manual identification of promising cross-disciplinary opportunities has become increasingly unfeasible [27]. The complexity and scale of this task call for automated solutions capable of discovering novel connections across fields.

##### 3.1.2 Advantages of AI4SoS

AI offers an opportunity for tackling challenges in the SoS by leveraging its capacity to process vast datasets and identify complex patterns beyond human discernment. In the context of forecasting technological development, AI models can analyze citation networks, research metadata, and publication trends to detect emerging technological trajectories with enhanced precision [28].

Moreover, AI-driven methods excel in uncovering interdisciplinary opportunities by representing scientific knowledge as graph structures and employing advanced similarity metrics. Graph neural networks, for instance, have demonstrated the ability to model intricate relationships across scientific literature, facilitating the discovery of latent connections and novel collaborations across disparate domains [29]. This capability empowers researchers to target high-potential interdisciplinary collaborations, fostering innovation at the convergence of fields.

### 3.2 Understanding the Dynamics of Research Society

##### 3.2.1 Background of Problem

The dynamics of research societies play a fundamental role in shaping scientific progress, which encompass how scientist research patterns evolve, how different team constructions influence the impact of research output, and how current research society influences scientists.

The Dynamics and Mechanics of Scientist Career The role of studying scientific careers is to provide personalized support to the academic community, thereby enhancing individual innovation capabilities, optimize team collaboration efficiency, and improving the allocation of research resources [1]. However, challenges include the highly individualized nature of career development paths, data scarcity and bias, and the complexity of external environmental factors [30].

The Dynamics and Mechanics of Research Team The composition and dynamics of scientific teams play a crucial role in improving research outcomes, with elements such as size, diversity, and collaboration patterns influencing team creativity and productivity [11, 31]. Over time, shifts in team structures and researcher mobility have reflected broader changes in the research landscape. Understanding these evolving dynamics presents challenges, as the relationships between team composition and research impact are multifaceted [32, 33].

The Dynamics and Mechanics of Research Society The organization and dynamics of research societies play a crucial role in shaping the progression and fairness of scientific endeavors. Studies have highlighted persistent inequalities in academic representation, participation, and recognition, both within and across nations [6, 34]. These disparities, influenced by systemic and structural factors, hinder the equitable generation and dissemination of knowledge. On a broader scale, imbalances in citation patterns and collaboration networks often reflect biases rooted in reputation and resources rather than research quality [35].

##### 3.2.2 Advantages of AI4SoS

AI offers potential for understanding and improving the dynamics of research societies. By analyzing large-scale historical datasets—such as collaboration patterns, research trajectories, and external influences—AI can uncover critical factors driving individual career development. This enables personalized researcher support and helps institutions optimize talent management. Techniques such as predictive modeling have proven effective in tracking and forecasting team member mobility patterns [36].

Moreover, AI-driven agents can simulate complex team dynamics, providing insights into how various factors, such as diversity and team size, influence research productivity and innovation. Taking this a step further, AI can simulate entire scientific societies, not only uncovering hidden patterns

and problems but also guiding the policymaking process by validating potential policies within the simulated environment. For instance, multi-agent systems have been employed to model team formation processes and predict collaboration outcomes under varying settings [22].

## 4 Challenges and Pathways

Achieving fully automated SoS discovery centers on effectively utilizing AI techniques to process scientific data. This endeavor involves addressing four key challenges: data-related issues, comprehensive system construction, robust system evaluation, and system explainability. For each of these challenges, we provide a detailed analysis along with potential pathways for resolution.

### 4.1 Data Issues

Challenges Data issues mainly include data imbalance across disciplines and training data bias. For the first issue, many disciplines, such as computer science and engineering, produce large volumes of well-structured data readily used by AI systems [37, 38]. However, other fields, such as social sciences or humanities, often suffer from smaller datasets, less structured data, or incomplete information, which makes it difficult for AI models to provide accurate predictions [39, 40]. This imbalance can lead to skewed results where AI predictions are disproportionately driven by well-represented fields, neglecting potentially valuable insights from underrepresented areas of research. Another issue is training data bias. When predicting reproducible patterns from data, machine learning models inevitably incorporate and perpetuate biases present in the data, often in opaque ways [41]. For example, the training data and alignment methods of LLMs (whether open-source or closed-source) are not fully disclosed [42–44], making it impossible to objectively assess their bias and fairness. Therefore, the fairness of machine learning becomes a heavily debated issue in applications ranging from the criminal justice system to hiring processes [45].

Pathway To address issues of data imbalance and biases in training data, constructing a large and diverse dataset is essential to improve data representativeness, ensuring coverage across various domains, groups, and contexts. Several large-scale, cross-disciplinary academic datasets are currently available for SoS research, including the Microsoft Academic Graph (MAG) [46], Open Academic Graph (OAG)[47], and SciSciNet [48], where the statistical information of each dataset is summarized in Table 2. In the process of data auditing and filtering, it is crucial to examine data sources and mitigate any potential historical or socio-cultural biases to ensure the dataset is free from implicit biases [49]. Additionally, employing multi-annotator strategies, conducting group balance checks, and performing fairness evaluations can further ensure the fairness and diversity of the dataset [50]. These measures not only enhance the model’s generalization ability but also reduce unfairness stemming from data biases.

Table 2: Summary table of large-scale cross-discipline academic datasets. Datasets MAG OAG SciSciNet Due 2020 2023 2021 Domain Art, Biology,

Art, Biology, Business, Chemistry, Computer Science, Economics, Engineering, Environmental Science, Geography, Geology, History, Materials Science, Mathematics, Philosophy, Physics, Political Science, Psychology, Sociology

Art, Biology, Business, Chemistry, Computer Science, Economics, Engineering, Environmental Science, Geography, Geology, History, Materials Science, Mathematics, Medicine, Philosophy, Physics, Political Science, Psychology, Sociology

Business, Chemistry, Computer Science, Economics, Engineering, Environmental Science, Geography, Geology, History, Materials Science, Mathematics, Philosophy, Physics, Political Science, Psychology, Sociology

Author 261,445,825 35,774,510 134,197,162 Paper 247,389,875 130,710,733 134,129,188 Affiliation 25,811 143,749 26,998

### 4.2 Comprehensive System Construction

Challenges Simulating a research society using AI for fully automated SoS discovery, particularly through an agent-based system, presents numerous challenges. Each scientist-agent requires detailed modeling of their research expertise, career trajectory, and collaborative networks, which are often too complex to be fully captured in the simulation system [51, 52]. Critical but unobservable factors, such as internal cognitive processes and informal discussions that drive real-world decision-making, remain challenging to replicate accurately. These limitations inevitably make simulations discrete and less representative of actual societal dynamics. Moreover, the simulation process itself introduces complexities. Aligning the simulated timeline with real-world events necessitates careful calibration; for instance, determining how many simulation epochs correspond to a year in reality [53]. Determining the appropriate size of the simulated society is also crucial; an overly small-scale model risks failing to capture the emergent behaviors of a real research ecosystem, while an overly large model may become impractical to manage and analyze [54, 55]. Another pressing challenge lies in bias amplification when designing AI systems—a concern that builds on the broader implications of how AI interacts

with societal structures. Since AI systems are often designed to optimize based on historical data of SoS, they risk perpetuating existing paradigms, funding trends, and citation networks. This aligns with the well-documented “rich get richer” effect in citation and funding dynamics [56–58]. If an AI system prioritizes high-impact metrics, it may inadvertently favor mainstream topics and established researchers, further marginalizing unconventional or disruptive ideas. Without explicit mechanisms to value novelty and diversity, such systems could unintentionally confine the scientific community to existing trends, hindering pathways to groundbreaking innovation. Lastly, the system must account for unexpected exceptions to ensure the simulation operates smoothly and continuously for fully automated scientific discovery. Striking a balance between realism and feasibility remains a persistent and fundamental challenge in these simulations.

Pathway Several potential pathways can help address these complexities. With the continuous advancement of LLMs’ comprehensive capabilities, handling complex multi-level modeling is becoming increasingly feasible. By defining agent models with distinct roles and appropriately assigning tasks, the behaviors of scientists at various levels can be more accurately simulated [59]. Fine-tuning LLMs on extensive academic datasets can further optimize the behavioral patterns of agents [60], enhancing their adaptability to reflect realworld research dynamics. One solution for timeline alignment is to build flexible, dynamic calibration techniques that adjust the simulation’s temporal parameters based on context and event-driven data [23]. In determining the appropriate scale for the simulated society, agent-based sampling methods (random or rule-based) or dynamic population expansion techniques can be utilized [22]. When addressing bias in AI systems, it is crucial to consider the nature of SoS, a discipline dedicated to analyzing historical data and uncovering biases or patterns within the scientific community. To ensure alignment between simulations and real-world dynamics, it is essential to incorporate these biases into SoS studies, as AI designed for this field seeks to enhance and advance SoS research. At the same time, such biases can be mitigated through targeted adjustments to system parameters. For instance, to counteract the “rich get richer” effect in citations, one effective approach could involve reducing the likelihood of citing highly cited papers when an agent selects a reference. Instead, assigning higher probabilities to less-cited, more novel papers can help promote diversity in citation practices and encourage the exploration of unconventional ideas. Moreover, the system can integrate robust anomaly detection and recovery mechanisms to handle unexpected situations. Using unsupervised learning techniques (such as clustering), the model can identify deviations from expected behaviors and adjust simulation parameters accordingly to ensure stability and continuity [61]. These potential solutions try to strike a balance between realism and operational feasibility, providing a technological foundation for research society simulations.

### 4.3 Comprehensive System Evaluation

Challenges Evaluating the validity of outputs generated by AI systems in the field of SoS is a complex and multifaceted challenge. SoS research addresses a broad range of problems and lacks unified evaluation standards, with different tasks often necessitating tailored metrics [41]. Moreover, innovation—a key attribute of AI outputs—is inherently subjective and context-dependent, making it difficult to quantify accurately using traditional methods [22, 62]. Validity assessments also heavily rely on specific domain contexts. However, the interdisciplinary nature of SoS compounds the complexity, requiring the integration of knowledge and evaluation standards from diverse fields. Additionally, the dynamic nature and long-term implications of AI-generated outputs present further challenges, as their true impact on scientific progress often cannot be evaluated in the short term [63]. Addressing this requires advanced tools, such

- as time-series analysis and virtual scientist simulations, to facilitate longitudinal tracking. Furthermore, AI-generated scientific recommendations may raise ethical issues and have far-reaching consequences for scientific communities and research practices [64]. Therefore, a comprehensive and adaptable evaluation framework is necessary, integrating scientometric methodologies, multidisciplinary expert reviews, dynamic analytical approaches, and stringent ethical guidelines. Pathway To address these challenges, appropriate solutions can be implemented. First, collaborating with domain experts to define task-specific evaluation metrics is essential, and then quantitative evaluation methods based on scientometrics should be developed. For instance, citation counts can be used as a measure of influence when evaluating the impact of system outputs, and they can also track knowledge flow [41]. In simulating a scientist’s career, individual impact metrics such as the h-index, which reflects both productivity and impact, can be applied. Additionally, to assess output novelty, feasible approaches include large model-based peer-review scoring [22, 65] or calculating the Z-score for each pairing of referenced journals [62]. With the ongoing expansion of LLMs’ expertise and improved reasoning capabilities, interdisciplinary testing and long-term large-scale simulations have become increasingly feasible. Moreover, LLMs are now being employed in social simulations [23], assuming role-based agents. In terms of ethical and social impacts, aligning model preferences and improving transparency can partially address ethical concerns and enhance user trust, while ethical benchmarks [66, 67] can be used to test the validity of system outputs. By integrating these strategies, a multidimensional evaluation framework can be established.


### 4.4 Explainability and Causal Inference

Challenges While the AI framework emphasizes automated discovery and evaluation, it lacks mechanisms to explain the causal pathways behind AIgenerated outputs [68, 69]. This limitation makes it difficult for researchers and policymakers to trust and adopt AI-driven insights, as they may not

fully understand the underlying logic or relationships. Moreover, the complex and interdisciplinary nature of SoS often involves interactions between numerous variables, such as collaborations, funding patterns, and citation networks [1, 70], which cannot be adequately captured through correlationbased approaches. Without explicit causal explanations, it is challenging to ensure the auditability, accountability, and interpretability of the system, undermining its credibility and ethical alignment.

Pathway To address these challenges, it is crucial to introduce causal modeling [71, 72] and explainable AI (XAI) [73, 74] techniques to assist in interpreting and validating simulation results. Approaches such as Counterfactual Analysis can clarify the logical origins of AI-driven recommendations or discoveries, making the reasoning process more transparent. Relevant methods in the SoS domain include causal inference techniques like Propensity Score Matching (PSM) and Coarsened Exact Matching (CEM), which are useful for identifying causal relationships in complex systems [75, 76]. Additionally, causal graphical models and structural equation modeling (SEM) can be applied to analyze scientific impact by modeling the flow of influence across variables such as collaboration networks or funding distributions [77–79]. These tools provide a robust foundation for explaining AI-generated outputs.

## 5 Proof-of-Concept Studies

In this section, we present case studies to illustrate a practical application scenarios in AI4SoS. Specifically, by constructing a simplified preliminary multi-agent system to replicate phenomena observed in real-world scientific societies and uncover underlying patterns in SoS, we aim to demonstrate the possibility of automated pattern discovery.

### 5.1 Environment Construction

We construct a preliminary multi-agent system to simulate a society-level scientific collaboration through an end-to-end pipeline, including collaborator selection, topic discussion, idea generation, novelty assessment, abstract generation, and peer review, inspired by [22, 65, 80]. Existing studies primarily focus on simulating individual scientists or small research teams within specific fields (e.g., computer science) and are often constrained to isolated settings that do not capture the broader research ecosystem. In contrast, our work enhances the system’s complexity by incorporating realistic factors such as multidisciplinary data, a review and indexing system, and scalable simulation across multiple research teams. The overview of our system is shown in Fig. 3. Multidisciplinary Data We use the OAG 3.11 as the initial database for our system, which developed from the Open Academic Graph [47]. This data set includes 35,774,510 authors and 130,710,733 papers as of 2023, spanning diverse domains such as physics, chemistry, and computer science. In Table 3, we present the disciplines and fields of paper in the Open Academic Graph,

1https://open.aminer.cn/open/article?id=65bf053091c938e5025a31e2

Goal: Analysis of Science of Science

Goal:

![image 8](Chen et al._2025_AI-Driven Automation Can Become the Foundation of Next-Era Science of Science Research_images/imageFile8.png)

![image 9](Chen et al._2025_AI-Driven Automation Can Become the Foundation of Next-Era Science of Science Research_images/imageFile9.png)

![image 10](Chen et al._2025_AI-Driven Automation Can Become the Foundation of Next-Era Science of Science Research_images/imageFile10.png)

Analysis of Science of Science Scientist Society

Include Collaborator Selection Author Information

Name/Affiliation/

Ethnicity/Citation…

Topic Discussion

|Include|Title/Abstract/Year/<br><br>Author/Citation…<br><br>|
|---|---|
| | |


Large Fail?

Idea Generation Reference Database

Novelty Assessment

- 1. Record new published paper
- 2. Update the citation of cited papers


Abstract Generation Peer Review

Small Fail?

Multi-Agent System

- Figure 3: The overview of our preliminary multi-agent system for scientific collaboration simulation. We place the simulation within a community of scientists. After a scientist leads his/her team in submitting a paper, it undergoes peer review. If accepted, it is added to the reference database and can be cited by other scientists in subsequent epochs. Due to varying author information, the citation count of the final research output differs, then we can analyze the correlation between them—understanding the dynamics of research organizations, which is important in the field of SoS.


Table 3: Summary table of disciplines and fields [11]. Field Discipline Humanities, Literature & Arts [Art, History, Philosophy, Psychology] Life Science & Earth Sciences [Biology, Environmental Science, Geogra-

phy, Geology]

Business, Economics & Management

[Business, Economics]

Engineering & Computer Science

[Computer Science, Engineering]

Chemical & Material Sciences [Chemistry, Materials Science] Physics & Mathematics [Mathematics, Physics] Health & Medical Sciences [Medicine] Social Sciences [Political Science, Sociology]

which is used to analyze the potential different patterns in various areas. We use papers from 2002 to 2009 as the reference database and papers from 2010 to 2011 as the validation database. To address missing author ethnicity and paper field information—key elements for validating SoS findings—we employ several data completion strategies. Specifically, we adopt corresponding approaches for the various pieces of author information and paper information in this dataset for our simulation, shown in Table 4 and 5.

regarding authors.

Field Name

Strategy Example

Author Information Name Use the anonymization technique Scientist 1 Ethnicity Use the name ethnicity classifier [81] British Affiliation Retain the original content [King’s College

London]

Affiliation Ranking

Use THE World University Rankings 2025 1

36

Citation Extract the author’s published papers between 2010 to 2020 and calculate the total number of citations for the papers; In the simulation, it will be updated if his/her paper is cited

1800

Co-author Extract the author’s published papers between 2010 to 2020 and record the collaborators in the papers; In the simulation, it will be updated if there are new collaborators

[Scientist 10, Scientist 201, Scientist 1002,

...]

Discipline Extract the author’s published papers between 2010 to 2020 and assign the author’s discipline as the one that appears most frequently

Psychology

Research topic

Extract the author’s published papers between 2010 to 2020 and record the keywords in the papers; Use GPT-4 to summarize these keywords into research topics

[Neuropsychology, Cognitive flexibility, Attentional bias, ...]

1 https://www.timeshighereducation.com/world-university-rankings/latest /world-ranking

Review and Indexing System To better simulate and reveal the patterns of scientific collaboration mechanisms, we introduce a review and indexing system. Papers written by scientist teams are peer-reviewed and scored (ranging from 1 to 10), and those that exceed the acceptance threshold (with score larger than 5) are added to the reference paper database as newly published papers. The peer review criteria are discussed in Appx. B, considering that the outcomes are cross-disciplinary. Besides, the indexing system allows agents to retrieve published papers as references, and the citation count of referenced papers is updated accordingly, which is later used for metric evaluation.

regarding papers.

Field Name

Strategy Example

Paper Information Title Retain the original content Linkages of plant traits to soil properties ...

Abstract Retain the original content Global change is likely to alter plant community

...

Year The year of the papers in the initial database is set to -1, while the papers published by the agent are assigned the epoch when the review is accepted

-1

Citation In the initial database, the citation count of the papers is the original citation value plus the number of times they are cited during the simulation, while the citation count of the papers written by the agent is the number of times they are cited during the simulation

82

Authors Retain the original content [Scientist 124, Scientist 7923,

...]

Cited Paper

The papers in the initial database have None for this information due to its absence, while the papers published by the agent contain the names of the cited papers

None

Discipline Use GPT-4 to classify the papers into disciplines based on their keywords and titles. Refer to Table 3 for all the disciplines used

Environmental Science

Scalable Simulation To better replicate the phenomenon of free collaboration in real scientific cooperation, we implement an adaptive concurrent distributed system based on the OASIS [23]. The system’s asynchronous mechanism achieves concurrent processing by queuing multiple requests from agents in an inference channel and then distributing them to different ports for sending and receiving, where each port has deployed an LLM responsible for chatting or embedding. Furthermore, to reduce CPU load, we set the channel

175

150

TimeCost(Hour)

125

100

75

50

25

0

1060 320 1000

Number of Agents (Thousand)

###### Figure 4: The time taken for a complete scientific collaboration with agentsof different scales. A simulation of a million-agent society takes only one week.

allocation wait time based on the number of pending requests in the channel, thereby enabling long-term large-scale asynchronous simulation. This mechanism serves the two purposes: 1. Enabling scientist agents from different teams to communicate simultaneously, including both intra-team and cross-team collaboration, and 2. Accelerating the simulation process to enable large-scale simulations at the million-agent level. We test the time cost of our simulation system under different number of agents, illustrated in Fig. 4. It could be found that we realize a fast large-scale agent system, where a simulation of a million agent society takes only one week.

- 5.2 Experiments


Implementation Details We implement our system on 32 NVIDIA A100 GPUs, with 4 ports deployed on each GPU, and each port running the LLaMA3.1-8b model. We allow each agent to create up to 3 teams simultaneously, with team sizes following an exponential distribution. This is because we analyze the team sizes of papers published between 2002 and 2009 in the OAG (over 1,000,000 papers), as shown in Fig. 5. The red fitting line indicates that the team sizes in the real data follow an exponential distribution. Therefore, in our simulation, the team size of each agent is also modeled using an exponential distribution.

In idea generation and novelty assessment, each agent can cite up to 9 references per speech, where the retrieval results are obtained based on the similarity between the embeddings of the query terms and the embeddings of the papers in the database. The model used for embedding is mxbai-embedlarge. To avoid storage issues, each agent’s memory retains a maximum of

###### 5 entries. Each paper undergoes peer review by 3 reviewers. In terms of the

0.35

| |Fit: 0.339 * np.exp(-0.335 * (x-3)) + 0.002| | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |


0.30

0.25

Probability

0.20

0.15

0.10

0.05

0.00

3 8 13 18 23 28 33 38 43

Team Size

- Figure 5: The statistics of team sizes for papers published between 2002 and 2009 in the OAG, with the red fitting line revealing that the distribution follows an exponential pattern.


timeline, each epoch allows for 1 action, meaning a complete scientific collaboration can be completed in 6 epochs if the team progresses without any delays or interruptions. In our final experiment, the size of our society is maintained

- at 1 million agents, with a total of 40 epochs. Involved Metrics Following the settings of [11, 30, 82], we measure the impact of scientific output by the number of citations a paper receives. In the simulation, the citation counts are updated each time a paper is retrieved during the idea generation phase. For validation, we analyze the citation counts of agent-generated papers to assess whether the system can replicate patterns observed in real-world data from the years 2010 to 2011. To evaluate AI’s potential in pattern discovery, we examine the influence of three key factors on citation counts: ethnicity diversity, affiliation diversity, and average university ranking. Specifically, we measure diversity using Shannon entropy. For instance, the ethnicity diversity deth of paper s is calculated as:


deth = −

k

pi(s)lnpi(s), (1)

i=1

where k represents the total number of ethnicity categories, and pi(s) is the proportion of authors from the i-th ethnicity category in paper s.

### 5.3 Simulation Results

The experimental results presented in Fig. 6 compare real-world data in 2010 with the outcomes generated by our preliminary LLM-based multi-agent system. Both the real-world and simulated data show that higher citation counts are positively correlated with greater ethnicity diversity, which aligns with

![image 11](Chen et al._2025_AI-Driven Automation Can Become the Foundation of Next-Era Science of Science Research_images/imageFile11.png)

- Figure 6: Comparison of real-world (2010) and AI-simulated scientific research patterns. The scatter plots illustrate the relationships between Ethnicity Diversity, Affiliation Diversity, and Affiliation Ranking with Citation Count in both real-world (top row) and simulated (bottom row) data. Strong correlations observed in real data are partially reproduced by the AI-driven multi-agent system, demonstrating its potential to uncover meaningful patterns in scientific research and support automated SoS studies.

![image 12](Chen et al._2025_AI-Driven Automation Can Become the Foundation of Next-Era Science of Science Research_images/imageFile12.png)

- Figure 7: Comparison of real-world (2011) and AI-simulated scientific research patterns.


existing findings in SoS literature [11], although the correlations are slightly weaker in the simulation. Additionally, the negative correlation between affiliation ranking and citation counts is also reproduced in the simulated data, suggesting that institutions with higher rankings may achieve higher citation counts per research output.

A similar comparison using real-world data from 2011 and the simulated result is provided in Fig. 7. The statistical analysis of the 2011 data exhibits similar trends to those observed in Fig. 6, which presents the comparison using 2010 data. The positive correlation between citation counts and ethnicity

diversity, as well as the negative correlation between affiliation ranking and citation counts, are consistently reflected in both years. However, minor variations in correlation strength are observed, highlighting the dynamic nature of scientific collaboration trends over time.

However, while both real-world and simulated data indicate a positive correlation between citation counts and affiliation diversity, the pattern observed in the simulation is not statistically significant, with a p-value greater than 0.05. These results suggest that the preliminary AI-driven simulations have the potential to replicate and uncover key patterns in scientific research, but there remains significant room for improvement. For instance, the current system lacks several critical components, such as comprehensive modeling of individual research trajectories and realistic funding and policy influences. These limitations contribute to the preliminary nature of our approach, as the absence of such factors restricts the system’s ability to fully capture the complexity of real-world scientific ecosystems. Developing a more comprehensive and sophisticated simulation framework will enhance the system’s capability to automatically model complex scientific dynamics with greater accuracy and reliability.

## 6 Alternative Views

The application of AI in SoS is often seen as transformative, promising to accelerate discovery. However, critics highlight significant limitations and risks, questioning its unqualified benefits. These concerns focus on systemic issues and unintended consequences [83–85]. Key counterarguments include: (1) Reinforcement of Existing Inequalities: AI systems rely heavily on historical data, which often mirror long-standing inequities within the scientific community. For instance, datasets may disproportionately represent well-established disciplines, regions, or researchers, thereby perpetuating an imbalanced view of scientific contributions. Critics argue that this could stifle innovation by overlooking emerging fields and underrepresented groups, ultimately reinforcing the leading trend rather than fostering diversity. (2) Overreliance on Traditional Metrics: Academic evaluation metrics, such as citation counts and journal impact factors, are central to many AI applications in SoS. These metrics have been criticized for prioritizing mainstream research while marginalizing unconventional or nascent ideas. Opponents caution that AIdriven analyses might amplify this bias, narrowing the scope of scientific discovery and undervaluing novel contributions.

While these critiques highlight significant challenges, they underscore the importance of addressing fairness, and inclusivity in AI applications for SoS [86–88]. To mitigate these concerns, the following strategies can be adopted: (1) Promoting Diversity in Data and Metrics: Expanding data curation efforts to include a wider range of disciplines, regions, and research communities is critical for minimizing biases. Additionally, developing diversified scientific impact metrics beyond citation counts can ensure a more

equitable evaluation of research contributions. (2) Incorporating Bias Mitigation Techniques: Embedding bias detection and correction mechanisms in AI systems can help identify and address inequities in the data and algorithms. These techniques should be complemented by rigorous validation to ensure fairness and reliability.

## 7 Outlook

As AI4SoS progresses toward full autonomy, we envision a future where scientific discovery itself becomes a more self-reflective, adaptive, and strategically guided process. In this envisioned landscape, AI agents are trained on vast corpora of scholarly data and historical innovation patterns, which will not only map the contours of scientific fields but also anticipate emerging disciplines and recommend actionable research agendas.

Automated SoS systems will continuously monitor the evolving structure of scientific collaboration, offering dynamic guidance to policymakers, institutions, and individual researchers. Research teams may be formed or optimized based on predicted synergy and complementary expertise, while funding strategies could adapt in real time to maximize long-term innovation impact. Moreover, AI4SoS could democratize scientific foresight, making sophisticated analyses accessible to a broader range of stakeholders, from early-career researchers to global research organizations. The resulting ecosystem would be one where science is not only accelerated but also made more transparent, inclusive, and responsive to societal needs.

To enhance real-world applicability, we also envision deployment scenarios in which AI4SoS integrates directly with existing scientific ecosystems. For instance, it could serve as a sandbox environment for evaluating national research policies, allowing simulated assessments before implementation. Within academic institutions, AI4SoS could support internal research strategy formulation, identifying growth areas and optimizing resource allocation. Additionally, it could assist governmental and funding bodies in planning emerging discipline layouts and national innovation agendas. These integration pathways would significantly boost the practical value, societal impact, and credibility of AI4SoS.

Achieving this vision will demand sustained interdisciplinary collaboration, ethical oversight, and robust infrastructure, but the potential payoff is immense: a future in which the SoS is not just studied, but actively shaped by intelligent systems.

## 8 Conclusion

This paper presents a forward-looking perspective on the future of AI4SoS, proposing a five-level autonomy framework for understanding the progression toward automated SoS discovery. We emphasize the importance of AI4SoS by demonstrating its potential in two critical domains: forecasting trends in

technology and innovation, and analyzing the evolution of research communities. Furthermore, we discuss key challenges and future directions, supporting our vision with literature reviews and proof-of-concept studies that showcase early applications. Ultimately, AI4SoS holds the promise of enabling automated SoS discovery, thereby enhancing scientific efficiency and promoting interdisciplinary innovation.

## Impact Statement

We believe that sustained collaboration between AI researchers and SoS scholars is essential for advancing our understanding of complex scientific processes. This study leverages the complementary expertise of both fields to address key SoS challenges, improving scientific efficiency and fostering interdisciplinary innovation.

However, from an ethical perspective, the integration of AI with SoS research may present several concerns. First, accountability: When AI participates in scientific decision-making, it is crucial to clarify responsibility. For instance, if an AI-generated prediction leads to errors, should developers bear full responsibility? We suggest enhancing AI system transparency (e.g., recording decision-making pathways) and explainability (e.g., providing reasoning behind decisions) to help researchers and regulators delineate accountability more clearly. Second, fairness and bias: AI systems rely on training data, which may contain inherent biases related to gender, geography, or economic disparities. These biases can lead to unjust scientific conclusions. Therefore, AI development and application should include rigorous data preprocessing and incorporate fairness constraints within algorithms to mitigate the risk of bias propagation. Finally, public trust: AI-driven automation tools, due to their complexity, may create a sense of detachment among the public. When AI decision-making processes are opaque, concerns about the credibility of scientific findings may arise. To foster trust, it is essential to develop more interpretable AI models and ensure human oversight in scientific processes.

From a societal perspective, the complexity of SoS demands innovative approaches. Conventional statistical studies, which depend largely on historical data, frequently struggle to uncover causal mechanisms. In contrast, agentbased AI provides a dynamic, causality-driven alternative. By elucidating the mechanisms behind the evolution of scientific knowledge, these methods can clarify how government policies influence research funding, academic publishing, and interdisciplinary collaboration. As AI4SoS advances, it will foster more effective knowledge exchange among academia, industry, and government, accelerating technological and theoretical innovation. Through intelligent analysis and predictive modeling, researchers can more precisely identify scientific challenges, significantly enhancing the efficiency of discovery.

## Acknowledgements

This work is supported by Shanghai Artificial Intelligence Laboratory.

## References

- [1] Fortunato, S., Bergstrom, C.T., B¨rner, K., Evans, J.A., Helbing, D., Milojevic´, S., Petersen, A.M., Radicchi, F., Sinatra, R., Uzzi, B., et al.: Science of science. Science 359(6379), 0185 (2018)
- [2] Bettencourt, L.M., Kaiser, D.I., Kaur, J.: Scientific discovery and topological transitions in collaboration networks. Journal of Informetrics 3(3), 210–221 (2009)
- [3] Shi, F., Foster, J.G., Evans, J.A.: Weaving the fabric of science: Dynamic network models of science’s unfolding structure. Social Networks 43, 73–85 (2015)
- [4] Klavans, R., Boyack, K.W.: Which type of citation analysis generates the most accurate taxonomy of scientific and technical knowledge? Journal of the Association for Information Science and Technology 68(4), 984–998

(2017)

- [5] Wang, D., Liu, L.: The science of science. In: Proceedings of the ACM/IEEE Joint Conference on Digital Libraries in 2020, pp. 563–564

(2020)

- [6] Wapman, K.H., Zhang, S., Clauset, A., Larremore, D.B.: Quantifying hierarchy and dynamics in us faculty hiring and retention. Nature 610(7930), 120–127 (2022)
- [7] Gao, B., Qiang, B., Tan, H., Jia, Y., Ren, M., Lu, M., Liu, J., Ma, W.-Y., Lan, Y.: Drugclip: Contrasive protein-molecule representation learning for virtual screening. Advances in Neural Information Processing Systems 36 (2024)
- [8] Abramson, J., Adler, J., Dunger, J., Evans, R., Green, T., Pritzel, A., Ronneberger, O., Willmore, L., Ballard, A.J., Bambrick, J., et al.: Accurate structure prediction of biomolecular interactions with alphafold

3. Nature, 1–3 (2024)

- [9] Chang, J., Ye, J.C.: Bidirectional generation of structure and properties through a single molecular foundation model. Nature Communications 15(1), 2323 (2024)
- [10] Rzhetsky, A., Foster, J.G., Foster, I.T., Evans, J.A.: Choosing experiments to accelerate collective discovery. Proceedings of the National Academy of Sciences 112(47), 14569–14574 (2015)
- [11] AlShebli, B.K., Rahwan, T., Woon, W.L.: The preeminence of ethnic diversity in scientific collaboration. Nature communications 9(1), 5163


- (2018)
- [12] Liu, L., Wang, Y., Sinatra, R., Giles, C.L., Song, C., Wang, D.: Hot streaks in artistic, cultural, and scientific careers. Nature 559(7714), 396–399 (2018)
- [13] Yin, Y., Wang, Y., Evans, J.A., Wang, D.: Quantifying the dynamics of failure across science, startups and security. Nature 575(7781), 190–194

(2019)

- [14] Shi, F., Evans, J.: Surprising combinations of research contents and contexts are related to impact and emerge with scientific outsiders from distant disciplines. Nature Communications 14, 1641 (2023)
- [15] Weston, L., Tshitoyan, V., Dagdelen, J., Kononova, O., Trewartha, A., Persson, K.A., Ceder, G., Jain, A.: Named entity recognition and normalization applied to large-scale information extraction from the materials science literature. Journal of chemical information and modeling 59(9), 3692–3702 (2019)
- [16] Clauset, A., Arbesman, S., Larremore, D.B.: Systematic inequality and hierarchy in faculty hiring networks. Science advances 1(1), 1400005

(2015)

- [17] Xiao, S., Yan, J., Li, C., Jin, B., Wang, X., Yang, X., Chu, S.M., Zha, H.: On modeling and predicting individual paper citation count over time. In: Ijcai, pp. 2676–2682 (2016)
- [18] Krenn, M., Zeilinger, A.: Predicting research trends with semantic and neural networks with an application in quantum physics. Proceedings of the National Academy of Sciences 117(4), 1910–1916 (2020)
- [19] Van Eck, N.J., Waltman, L.: Citation-based clustering of publications using citnetexplorer and vosviewer. Scientometrics 111, 1053–1070

(2017)

- [20] Hofstra, B., Kulkarni, V.V., Munoz-Najar Galvez, S., He, B., Jurafsky, D., McFarland, D.A.: The diversity–innovation paradox in science. Proceedings of the National Academy of Sciences 117(17), 9284–9291

(2020)

- [21] Ghafarollahi, A., Buehler, M.J.: Sciagents: Automating scientific discovery through multi-agent intelligent graph reasoning. arXiv preprint

- arXiv:2409.05556 (2024)


- [22] Su, H., Chen, R., Tang, S., Zheng, X., Li, J., Yin, Z., Ouyang, W., Dong, N.: Two heads are better than one: A multi-agent system


has the potential to improve scientific idea generation. arXiv preprint

- arXiv:2410.09403 (2024)


- [23] Yang, Z., Zhang, Z., Zheng, Z., Jiang, Y., Gan, Z., Wang, Z., Ling, Z., Chen, J., Ma, M., Dong, B., et al.: Oasis: Open agents social interaction simulations on one million agents. arXiv preprint arXiv:2411.11581

(2024)

- [24] Li, Z., Song, P., Li, G., Han, Y., Ren, X., Bai, L., Su, J.: Ai energized hydrogel design, optimization and application in biomedicine. Materials Today Bio, 101014 (2024)
- [25] Ofosu-Ampong, K.: Artificial intelligence research: A review on dominant themes, methods, frameworks and future research directions. Telematics and Informatics Reports, 100127 (2024)
- [26] Iacopini, I., Milojevi´c, S., Latora, V.: Network dynamics of innovation processes. Physical review letters 120(4), 048301 (2018)
- [27] Bolt, T., Nomi, J.S., Bzdok, D., Uddin, L.Q.: Educating the future generation of researchers: A cross-disciplinary survey of trends in analysis methods. PLoS biology 19(7), 3001313 (2021)
- [28] B¨rner, K., Rouse, W.B., Trunfio, P., Stanley, H.E.: Forecasting innovations in science, technology, and education. Proceedings of the National Academy of Sciences 115(50), 12573–12581 (2018)
- [29] Zhou, J., Cui, G., Hu, S., Zhang, Z., Yang, C., Liu, Z., Wang, L., Li, C., Sun, M.: Graph neural networks: A review of methods and applications. AI open 1, 57–81 (2020)
- [30] Wang, Y., Jones, B.F., Wang, D.: Early-career setback and future career impact. Nature communications 10(1), 4331 (2019)
- [31] Wu, L., Wang, D., Evans, J.A.: Large teams develop and small teams disrupt science and technology. Nature 566, 378–382 (2019)
- [32] Wuchty, S., Jones, B.F., Uzzi, B.: The increasing dominance of teams in production of knowledge. Science 316(5827), 1036–1039 (2007)
- [33] Yang, Y., Tian, T.Y., Woodruff, T.K., Jones, B.F., Uzzi, B.: Genderdiverse teams produce more novel and higher-impact scientific ideas. Proceedings of the National Academy of Sciences 119(36), 2200841119

(2022)

- [34] Liu, F., Rahwan, T., AlShebli, B.: Non-white scientists appear on fewer


- editorial boards, spend more time under review, and receive fewer citations. Proceedings of the National Academy of Sciences 120(13), 2215324120 (2023)
- [35] Gomez, C.J., Herman, A.C., Parigi, P.: Leading countries in global science increasingly receive more citations than other countries doing similar research. Nature Human Behaviour 6(7), 919–929 (2022)
- [36] Guimera, R., Uzzi, B., Spiro, J., Amaral, L.A.N.: Team assembly mechanisms determine collaboration network structure and team performance. Science 308(5722), 697–702 (2005)
- [37] Fern´ndez, A., del Rı´o, S., Chawla, N.V., Herrera, F.: An insight into imbalanced big data classification: outcomes and challenges. Complex & Intelligent Systems 3, 105–120 (2017)
- [38] Kaur, H., Pannu, H.S., Malhi, A.K.: A systematic review on imbalanced data challenges in machine learning: Applications and solutions. ACM computing surveys (CSUR) 52(4), 1–36 (2019)
- [39] Leevy, J.L., Khoshgoftaar, T.M., Bauder, R.A., Seliya, N.: A survey on addressing high-class imbalance in big data. Journal of Big Data 5(1), 1–30 (2018)
- [40] Johnson, J.M., Khoshgoftaar, T.M.: Survey on deep learning with class imbalance. Journal of big data 6(1), 1–54 (2019)
- [41] Liu, L., Jones, B.F., Uzzi, B., Wang, D.: Data, measurement and empirical methods in the science of science. Nature human behaviour 7(7), 1046–1058 (2023)
- [42] Achiam, J., Adler, S., Agarwal, S., Ahmad, L., Akkaya, I., Aleman, F.L., Almeida, D., Altenschmidt, J., Altman, S., Anadkat, S., et al.: Gpt-4 technical report. arXiv preprint arXiv:2303.08774 (2023)
- [43] Dubey, A., Jauhri, A., Pandey, A., Kadian, A., Al-Dahle, A., Letman, A., Mathur, A., Schelten, A., Yang, A., Fan, A., et al.: The llama 3 herd of models. arXiv preprint arXiv:2407.21783 (2024)
- [44] Yang, A., Yang, B., Zhang, B., Hui, B., Zheng, B., Yu, B., Li, C., Liu, D., Huang, F., Wei, H., et al.: Qwen2. 5 technical report. arXiv preprint arXiv:2412.15115 (2024)
- [45] Mehrabi, N., Morstatter, F., Saxena, N., Lerman, K., Galstyan, A.: A survey on bias and fairness in machine learning. ACM computing surveys (CSUR) 54(6), 1–35 (2021)


- [46] Sinha, A., Shen, Z., Song, Y., Ma, H., Eide, D., Hsu, B.-J., Wang, K.: An overview of microsoft academic service (mas) and applications. In: Proceedings of the 24th International Conference on World Wide Web, pp. 243–246 (2015)
- [47] Zhang, F., Liu, X., Tang, J., Dong, Y., Yao, P., Zhang, J., Gu, X., Wang, Y., Kharlamov, E., Shao, B., et al.: Oag: Linking entities across largescale heterogeneous knowledge graphs. IEEE Transactions on Knowledge and Data Engineering 35(9), 9225–9239 (2022)
- [48] Lin, Z., Yin, Y., Liu, L., Wang, D.: Sciscinet: A large-scale open data lake for the science of science research. Scientific Data 10(1), 315 (2023)
- [49] Scatiggio, V.: Tackling the issue of bias in artificial intelligence to design ai-driven fair and inclusive service systems. how human biases are breaching into ai algorithms, with severe impacts on individuals and societies, and what designers can do to face this phenomenon and change for the better (2020)
- [50] Prabhakaran, V., Davani, A.M., Diaz, M.: On releasing annotator-level labels and information in datasets. arXiv preprint arXiv:2110.05699

(2021)

- [51] Norling, E., Edmonds, B., Meyer, R.: Informal approaches to developing simulation models. Simulating Social Complexity: A Handbook, 61–79

(2017)

- [52] Gao, C., Lan, X., Li, N., Yuan, Y., Ding, J., Zhou, Z., Xu, F., Li, Y.: Large language models empowered agent-based modeling and simulation: A survey and perspectives. Humanities and Social Sciences Communications 11(1), 1–24 (2024)
- [53] Khaleghian, S., Neema, H., Sartipi, M., Tran, T., Sen, R., Dubey, A.: Calibrating real-world city traffic simulation model using vehicle speed data. In: 2023 IEEE International Conference on Smart Computing (SMARTCOMP), pp. 303–308 (2023). IEEE
- [54] Schulze, J., Mu¨ller, B., Groeneveld, J., Grimm, V.: Agent-based modelling of social-ecological systems: achievements, challenges, and a way forward. Journal of Artificial Societies and Social Simulation 20(2)

(2017)

- [55] An, L., Grimm, V., Sullivan, A., Turner Ii, B., Malleson, N., Heppenstall, A., Vincenot, C., Robinson, D., Ye, X., Liu, J., et al.: Challenges, tasks, and opportunities in modeling agent-based complex systems. Ecological Modelling 457, 109685 (2021)


- [56] Ebadi, A., Schiffauerova, A.: How to receive more funding for your research? get connected to the right people! PloS one 10(7), 0133061

(2015)

- [57] Ronda-Pupo, G.A., Pham, T.: The evolutions of the rich get richer and the fit get richer phenomena in scholarly networks: The case of the strategic management journal. Scientometrics 116(1), 363–383 (2018)
- [58] Katz, Y., Matter, U.: Metrics of inequality: The concentration of resources in the us biomedical elite. Science as Culture 29(4), 475–502

(2020)

- [59] Qian, C., Liu, W., Liu, H., Chen, N., Dang, Y., Li, J., Yang, C., Chen, W., Su, Y., Cong, X., Xu, J., Li, D., Liu, Z., Sun, M.: Chatdev: Communicative agents for software development. In: Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics, pp. 15174–15186 (2024)
- [60] Guo, T., Chen, X., Wang, Y., Chang, R., Pei, S., Chawla, N.V., Wiest, O., Zhang, X.: Large language model based multi-agents: A survey of progress and challenges. arXiv preprint arXiv:2402.01680 (2024)
- [61] Aldrich, C., Auret, L.: Unsupervised Process Monitoring and Fault Diagnosis with Machine Learning Methods vol. 16. Springer, ??? (2013)
- [62] Chen, Q., Ho, Y.-J.I., Sun, P., Wang, D.: The philosopher’s stone for science–the catalyst change of ai for scientific creativity. Pin and Wang, Dashun, The Philosopher’s Stone for Science–The Catalyst Change of AI for Scientific Creativity (March 5, 2024) (2024)
- [63] Balasubramaniam, S., Chirchi, V., Kadry, S., Agoramoorthy, M., Gururama, S.P., Satheesh, K.K., Sivakumar, T.: The road ahead: Emerging trends, unresolved issues, and concluding remarks in generative ai—a comprehensive review. International Journal of Intelligent Systems 2024

(2024)

- [64] Lissack, M., Meagher, B.: Navigating the future of large language models in scientific research: Opportunities, challenges, and ethical considerations. Challenges, and Ethical Considerations (September 02, 2024)

(2024)

- [65] Lu, C., Lu, C., Lange, R.T., Foerster, J., Clune, J., Ha, D.: The ai scientist: Towards fully automated open-ended scientific discovery. arXiv preprint arXiv:2408.06292 (2024)
- [66] Meadows, G.I., Lau, N.W.L., Susanto, E.A., Yu, C.L., Paul, A.: Localvaluebench: A collaboratively built and extensible benchmark for evaluating


- localized value alignment and ethical safety in large language models. arXiv preprint arXiv:2408.01460 (2024)
- [67] Ji, J., Chen, Y., Jin, M., Xu, W., Hua, W., Zhang, Y.: Moralbench: Moral evaluation of llms. arXiv preprint arXiv:2406.04428 (2024)
- [68] Hassija, V., Chamola, V., Mahapatra, A., Singal, A., Goel, D., Huang, K., Scardapane, S., Spinelli, I., Mahmud, M., Hussain, A.: Interpreting black-box models: a review on explainable artificial intelligence. Cognitive Computation 16(1), 45–74 (2024)
- [69] Reddy, C.K., Shojaee, P.: Towards scientific discovery with generative ai: Progress, opportunities, and challenges. In: Proceedings of the AAAI Conference on Artificial Intelligence, vol. 39, pp. 28601–28609 (2025)
- [70] Sonnenwald, D.H.: Scientific collaboration. Annu. Rev. Inf. Sci. Technol. 41(1), 643–681 (2007)
- [71] Petersen, M.L., van der Laan, M.J.: Causal models and learning from data: integrating causal modeling and statistical estimation. Epidemiology 25(3), 418–426 (2014)
- [72] Feuerriegel, S., Frauen, D., Melnychuk, V., Schweisthal, J., Hess, K., Curth, A., Bauer, S., Kilbertus, N., Kohane, I.S., van der Schaar, M.: Causal machine learning for predicting treatment outcomes. Nature Medicine 30(4), 958–968 (2024)
- [73] Dwivedi, R., Dave, D., Naik, H., Singhal, S., Omer, R., Patel, P., Qian, B., Wen, Z., Shah, T., Morgan, G., et al.: Explainable ai (xai): Core ideas, techniques, and solutions. ACM Computing Surveys 55(9), 1–33

- (2023)

[74] Longo, L., Brcic, M., Cabitza, F., Choi, J., Confalonieri, R., Del Ser, J., Guidotti, R., Hayashi, Y., Herrera, F., Holzinger, A., et al.: Explainable artificial intelligence (xai) 2.0: A manifesto of open challenges and interdisciplinary research directions. Information Fusion 106, 102301

- (2024)


- [75] King, G., Nielsen, R., Coberley, C., Pope, J.E., Wells, A.: Comparative effectiveness of matching methods for causal inference. Unpublished manuscript, Institute for Quantitative Social Science, Harvard University, Cambridge, MA (2011)
- [76] Imbens, G.W., Rubin, D.B.: Causal Inference in Statistics, Social, and Biomedical Sciences. Cambridge university press, ??? (2015)


- [77] De Carvalho, J., Chima, F.O.: Applications of structural equation modeling in social sciences research. American International Journal of Contemporary Research 4(1), 6–11 (2014)
- [78] Khan, G.F., Sarstedt, M., Shiau, W.-L., Hair, J.F., Ringle, C.M., Fritze, M.P.: Methodological research on partial least squares structural equation modeling (pls-sem) an analysis based on social network approaches. Internet Research 29(3), 407–429 (2019)
- [79] Leist, A.K., Klee, M., Kim, J.H., Rehkopf, D.H., Bordas, S.P., MunizTerrera, G., Wade, S.: Mapping of machine learning approaches for description, prediction, and causal inference in the social and health sciences. Science Advances 8(42), 1942 (2022)
- [80] Qi, B., Zhang, K., Tian, K., Li, H., Chen, Z.-R., Zeng, S., Hua, E., Jinfang, H., Zhou, B.: Large language models as biomedical hypothesis generators: A comprehensive evaluation. arXiv preprint arXiv:2407.08940

(2024)

- [81] Ambekar, A., Ward, C., Mohammed, J., Male, S., Skiena, S.: Nameethnicity classification from open sources. In: Proceedings of the 15th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, pp. 49–58 (2009)
- [82] Li, W., Aste, T., Caccioli, F., Livan, G.: Early coauthorship with top scientists predicts success in academic careers. Nature communications 10(1), 5170 (2019)
- [83] Binns, R.: Fairness in machine learning: Lessons from political philosophy. In: Conference on Fairness, Accountability and Transparency, pp. 149–159 (2018). PMLR
- [84] Raji, I.D., Buolamwini, J.: Actionable auditing: Investigating the impact of publicly naming biased performance results of commercial ai products. In: Proceedings of the 2019 AAAI/ACM Conference on AI, Ethics, and Society, pp. 429–435 (2019)
- [85] Messeri, L., Crockett, M.: Artificial intelligence and illusions of understanding in scientific research. Nature 627(8002), 49–58 (2024)
- [86] Holstein, K., Wortman Vaughan, J., Daume´ III, H., Dudik, M., Wallach, H.: Improving fairness in machine learning systems: What do industry practitioners need? In: Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems, pp. 1–16 (2019)
- [87] Schwartz, R., Down, L., Jonas, A., Tabassi, E.: A proposal for identifying and managing bias in artificial intelligence. Draft NIST Special


- Publication 1270 (2021)
- [88] Schwartz, R., Schwartz, R., Vassilev, A., Greene, K., Perine, L., Burt, A., Hall, P.: Towards a Standard for Identifying and Managing Bias in Artificial Intelligence vol. 3. US Department of Commerce, National Institute of Standards and Technology, ??? (2022)
- [89] Van Noorden, R., Perkel, J.M.: Ai and science: what 1,600 researchers think. Nature 621(7980), 672–675 (2023)
- [90] G´rriz, J.M., Ramı´rez, J., Ortiz, A., Martinez-Murcia, F.J., Segovia, F., Suckling, J., Leming, M., Zhang, Y.-D., Alvarez-S´nchez,´ J.R., Bologna, G., et al.: Artificial intelligence within the interplay between natural and artificial computation: Advances in data science, trends and applications. Neurocomputing 410, 237–270 (2020)
- [91] Verganti, R., Vendraminelli, L., Iansiti, M.: Innovation and design in the age of artificial intelligence. Journal of product innovation management 37(3), 212–227 (2020)
- [92] Madanchian, M., Taherdoost, H.: Ai-powered innovations in high-tech research and development: From theory to practice. Computers, Materials & Continua 81(2) (2024)
- [93] Wallach, I., Dzamba, M., Heifets, A.: Atomnet: a deep convolutional neural network for bioactivity prediction in structure-based drug discovery. arXiv preprint arXiv:1510.02855 (2015)
- [94] Staszak, M., Staszak, K., Wieszczycka, K., Bajek, A., Roszkowski, K., Tylkowski, B.: Machine learning in drug design: Use of artificial intelligence to explore the chemical structure–biological activity relationship. Wiley Interdisciplinary Reviews: Computational Molecular Science 12(2), 1568 (2022)
- [95] Suh, C., Fare, C., Warren, J.A., Pyzer-Knapp, E.O.: Evolving the materials genome: How machine learning is fueling the next generation of materials discovery. Annual Review of Materials Research 50(1), 1–25

(2020)

- [96] Kim, H., Choi, H., Kang, D., Lee, W.B., Na, J.: Materials discovery with extreme properties via reinforcement learning-guided combinatorial chemistry. Chemical Science (2024)
- [97] Light, J., Cai, M., Shen, S., Hu, Z.: Avalonbench: Evaluating llms playing the game of avalon. In: NeurIPS 2023 Foundation Models for Decision Making Workshop (2023)


- [98] Du, Z., Qian, C., Liu, W., Xie, Z., Wang, Y., Dang, Y., Chen, W., Yang, C.: Multi-agent software development through cross-team collaboration. arXiv preprint arXiv:2406.08979 (2024)
- [99] Raffel, C., Shazeer, N., Roberts, A., Lee, K., Narang, S., Matena, M., Zhou, Y., Li, W., Liu, P.J.: Exploring the limits of transfer learning with a unified text-to-text transformer. Journal of machine learning research 21(140), 1–67 (2020)
- [100] OpenAI: GPT-4 technical report. CoRR (2023)
- [101] Dubey, A., Jauhri, A., Pandey, A., Kadian, A., Al-Dahle, A., Letman, A., Mathur, A., Schelten, A., Yang, A., Fan, A., et al.: The llama 3 herd of models. arXiv preprint arXiv:2407.21783 (2024)
- [102] Kenton, J.D.M.-W.C., Toutanova, L.K.: Bert: Pre-training of deep bidirectional transformers for language understanding. In: Proceedings of naacL-HLT, vol. 1, p. 2 (2019). Minneapolis, Minnesota
- [103] Ji, Y., Zhou, Z., Liu, H., Davuluri, R.V.: Dnabert: pre-trained bidirectional encoder representations from transformers model for dna-language in genome. Bioinformatics 37(15), 2112–2120 (2021)
- [104] Zhang, D., Liu, W., Tan, Q., Chen, J., Yan, H., Yan, Y., Li, J., Huang, W., Yue, X., Zhou, D., et al.: Chemllm: A chemical large language model. arXiv preprint arXiv:2402.06852 (2024)
- [105] Liu, J., Zhou, P., Hua, Y., Chong, D., Tian, Z., Liu, A., Wang, H., You, C., Guo, Z., Zhu, L., et al.: Benchmarking large language models on cmexam-a comprehensive chinese medical exam dataset. Advances in Neural Information Processing Systems 36 (2024)
- [106] Zhang, J., Xu, X., Zhang, N., Liu, R., Hooi, B., Deng, S.: Exploring collaboration mechanisms for LLM agents: A social psychology view. In: Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics, pp. 14544–14607 (2024)
- [107] Nogueira, R., Cho, K.: Passage re-ranking with bert. arXiv preprint arXiv:1901.04085 (2019)
- [108] Mars, M.: From word embeddings to pre-trained language models: A state-of-the-art walkthrough. Applied Sciences 12(17), 8805 (2022)
- [109] Alsayat, A.: Improving sentiment analysis for social media applications using an ensemble deep learning language model. Arabian Journal for Science and Engineering 47(2), 2499–2511 (2022)


###### [110] Petukhova, A., Matos-Carvalho, J.P., Fachada, N.: Text clustering withllm embeddings. arXiv preprint arXiv:2403.15112 (2024)

## A Related Work

- A.1 AI for Science

In recent years, AI has become increasingly common in science and is expected to become the center of research practice [89]. AI has demonstrated great potential to accelerate experimental design, data analysis, optimization problem solving, and discovery of new theories [90–92]. Specifically, deep neural networks are used to predict the relationship between molecular structures and biological activity [93, 94], reinforcement learning is used to discover unknown materials with superior properties [95, 96], and agent-based systems are introduced to simulate social science scenarios [97, 98]. In addition, as a subfield of science, AI has undergone some preliminary explorations in the SoS [11, 14, 22], revealing promising results.

- A.2 Large Language Models


The role of large language models (LLMs) can be articulated from two perspectives: chat (T5 [99], GPT-4 [100], and LLaMA3.1 [101]) and embedding (BERT [102] and DNABERT [103]) generation. First, the capability of dialogue generation enables LLMs to understand user input in natural language and generate contextually relevant responses in various conversational contexts such as knowledge testing, game play, and software programming [98, 104– 106]. Additionally, embedding generation allows LLMs to convert input text into fixed-dimensional vector representations, which effectively capture the semantic information of the text and can be used for tasks such as text similarity computation, information retrieval, and sentiment analysis [107–110]. Therefore, the capabilities of LLMs in both text generation and embedding generation make them applications spanning from natural language processing tasks to more complex domains such as SoS, where they can assist in understanding research dynamics, scientific discovery, and scientific collaboration.

## B Review and Indexing System

In Table 6 and 7, we present the peer review criteria used in our simulation system, which is based on the modified Neural Information Processing Systems review guidelines 2 considering that the papers produced by cross-discipline agents are not all in the field of computer science. Although this criteria comes from a computer science conference, the basic evaluation metrics can be applied in multiple areas.

2https://neurips.cc/Conferences/2024/ReviewerGuidelines

Table 6: Prompt Tailored for Multidisciplinary Reviewers

- Prompt Tailored for Multidisciplinary Reviewers (1/2)


You are a researcher from a multidisciplinary background reviewing a paper that has been submitted to a venue that involves multiple scientific disciplines. Be critical and cautious in your decision-making. If the paper has significant weaknesses or you are uncertain about its quality, provide lower scores and recommend rejection. Below are the questions you will be asked on the review form for each paper and some guidelines on what to consider when answering these questions. Reviewer Guidelines for Multidisciplinary Paper Review:

- 1. Summary: Provide a brief summary of the paper and its contributions. This is not the place to critique the paper. The authors should generally agree with a well-written summary, which reflects an accurate understanding of their work from a multidisciplinary perspective.
- 2. Strengths and Weaknesses: Please provide a thorough assessment of the strengths and weaknesses of the paper, touching on each of the following dimensions:

- - Originality: Are the tasks or methods novel within each of the relevant disciplines? Does the work represent an innovative combination of techniques or concepts from different fields? Is it clear how this work distinguishes itself from previous contributions in each discipline involved?
- - Quality: Is the submission technically sound in each of the relevant fields? Are claims well-supported by evidence (e.g., theoretical analysis or experimental results)? Are the methods used appropriately for each discipline involved? Is this a complete piece of work, or still a work in progress? Are the authors transparent and honest in evaluating both the strengths and weaknesses of their work?
- - Clarity: Is the paper written in a way that is accessible to readers from multiple disciplines? Is it well-organized, with clear explanations of concepts across different fields? If not, please suggest improvements for clarity. Does it provide sufficient detail for an expert in each relevant field to understand the methodology and reproduce results?
- - Significance: Are the results important? Are others (researchers or practitioners) likely to use the ideas or build on them? Does the submission address a difficult task in a better way than previous work? Does it advance the state of the art in a demonstrable way? Does it provide unique data, unique conclusions about existing data, or a unique theoretical or experimental approach?


- 3. Questions: Please list any questions or suggestions that could help clarify the paper’s limitations or improve its quality. Responses from the authors could change your opinion or address areas of confusion. This feedback can be critical for the rebuttal and discussion phase with the authors.


Table 7: Prompt Tailored for Multidisciplinary Reviewers

- Prompt Tailored for Multidisciplinary Reviewers (2/2)


- 4. Ethical Concerns: Flag any ethical concerns, particularly those that may arise from interdisciplinary collaboration. Ensure any ethical issues related to research design, data usage, or broader implications are addressed.
- 5. Overall Score: Provide a final score based on the paper’s strengths and weaknesses. Use the following scale:


- - 10: Award Quality: A technically flawless paper with groundbreaking impact across one or more disciplines, with exceptionally strong evaluation, reproducibility, and resources, and no unaddressed ethical concerns.
- - 9: Very Strong Accept: A technically flawless paper with groundbreaking impact in at least one area and strong impact on multiple areas, with flawless evaluation, resources, and reproducibility, and no unaddressed ethical concerns.
- - 8: Strong Accept: A technically strong paper with novel ideas, significant impact on at least one discipline or moderate-to-high impact on multiple areas, with excellent evaluation, resources, and reproducibility, and no unaddressed ethical concerns.
- - 7: Accept: A technically solid paper with moderate-to-high impact in one or more subfields, good-to-excellent evaluation, reproducibility, and resources, and no unaddressed ethical concerns.
- - 6: Weak Accept: A solid paper with moderate impact, no major concerns in terms of evaluation, reproducibility, and ethical considerations.
- - 5: Borderline Accept: A technically solid paper where reasons to accept outweigh reasons to reject, e.g., limited evaluation. Use sparingly.
- - 4: Borderline Reject: A technically solid paper where reasons to reject outweigh reasons to accept, e.g., limited evaluation. Use sparingly.
- - 3: Reject: A paper with technical flaws, weak evaluation, inadequate reproducibility, or incompletely addressed ethical concerns.
- - 2: Strong Reject: A paper with major technical flaws, poor evaluation, limited impact, poor reproducibility, or mostly unaddressed ethical considerations.
- - 1: Very Strong Reject: A paper with trivial results, poor evaluation, or unaddressed ethical issues.


