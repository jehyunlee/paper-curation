# arXiv:2503.13503v1[cs.LG]12 Mar 2025

## SciHorizon: Benchmarking AI-for-Science Readiness from Scientific Data to Large Language Models

##### Chuan Qin∗1, Xin Chen†1, Chengrui Wang1, Pengmin Wu1, Xi Chen1,2, Yihang Cheng1, Jingyi Zhao1, Meng Xiao1, Xiangchao Dong1, Qingqing Long1, Boya Pan1, Han Wu3, Chengzan Li1, Yuanchun Zhou1, Hui Xiong4, Hengshu Zhu‡1

1Computer Network Information Center, Chinese Academy of Sciences. 2University of Science and Technology of China. 3Hefei University of Technology. 4The Hong Kong University of Science and Technology (Guangzhou). Concat Email: scihorizon@cnic.cn. Project Homepage: www.scihorizon.cn.

Abstract In recent years, the rapid advancement of Artificial Intelligence (AI) technologies, particularly Large Language Models (LLMs), has revolutionized the paradigm of scientific discovery, establishing AI-for-Science (AI4Science) as a dynamic and evolving field. However, there is still a lack of an effective framework for the overall assessment of AI4Science, particularly from a holistic perspective on data quality and model capability. Therefore, in this study, we propose SciHorizon, a comprehensive assessment framework designed to benchmark the readiness of AI4Science from both scientific data and LLM perspectives. First, we introduce a generalizable framework for assessing AI-ready scientific data, encompassing four key dimensions—Quality, FAIRness, Explainability, and Compliance—which are subdivided into 15 sub-dimensions. Drawing on data resource papers published between 2018 and 2023 in peer-reviewed journals, we present recommendation lists of AI-ready datasets for both Earth and Life Sciences, making a novel and original contribution to the field. Concurrently, to assess the capabilities of LLMs across multiple scientific disciplines, we establish 16 assessment dimensions

∗Leading the LLM assessment. †Leading the scientific data assessment. ‡Project Leader.

based on five core indicators—Knowledge, Understanding, Reasoning, Multimodality, and Values‌—spanning Mathematics, Physics, Chemistry, Life Sciences, and Earth and Space Sciences. Using the developed benchmark datasets, we have conducted a comprehensive evaluation of over 20 representative open-source and closed-source LLMs. All the results are publicly available and can be accessed online at www.scihorizon.cn/en.

Keywords: AI-for-science, scientific data, large language models, AI-ready, benchmarking

### 1 Introduction

Scientific data resources serve as the core driver propelling scientific discoveries and as a critical enabler for interdisciplinary research that integrates Artificial Intelligence (AI) with other disciplines. As AI technologies advance rapidly, particularly in Large Language Models (LLMs), AI-for-Science (AI4Science) has emerged as a ‌frontier research hotspot. For instance, in structural biology, DeepMind’s AlphaFold has revolutionized protein structure prediction by achieving unprecedented accuracy, effectively resolving a challenge that previously demanded decades of experimental effort [1]. Likewise, LLMs, such as OpenAI’s ChatGPT, are expanding AI’s role in scientific research by not only enhancing data analysis capabilities [2, 3], but also assisting in literature review [4], hypothesis generation [5, 6], and complex reasoning [7, 8]. These models facilitate the synthesis of vast scientific knowledge, accelerate discovery processes, and foster interdisciplinary collaboration, thereby reshaping the landscape of modern scientific inquiry.

Despite rapid advancements in AI4Science, the field faces persistent challenges stemming from the reliance on large-scale, interdisciplinary datasets and the scarcity of AI-ready, high-quality data‌. Therefore, researchers advocate for systematic assessment frameworks that integrate metrics for data accuracy, completeness, and domain relevance. While traditional tools are instrumental in assessing data quality from different perspectives [9–12] or emphasizing specific aspects of data readiness [13–16], they fall short of addressing the unique requirements of AI applications in the scientific domain. This leads to two challenges in evaluating scientific data in AI4Science: 1) AI researchers struggle to efficiently extract valuable insights from vast, domain-specific datasets, leading to the underutilization or misapplication of high-potential data that could drive significant advances in AI-driven scientific discovery; and 2) Researchers across disciplines lack clear criteria to assess whether their datasets align with AI model requirements, hindering the development and optimization of high-quality, AI-ready data.

Meanwhile, after assessing the possibility of high-quality scientific data integration, a critical challenge lies in comprehensively and effectively assessing the application capabilities of AI4Science models at a fine-grained level. Despite the proliferation of diverse assessment frameworks for LLMs [17], those specifically designed for scientific applications remain scarce. Recently, several targeted benchmarks have been

proposed, however, they exhibit notable limitations: 1) Most of them focus on specific disciplines [18, 19], lacking a unified framework that accommodates multiple scientific fields; 2) Their capability assessments are relatively narrow—for instance, JEEBench [20] primarily evaluates reasoning abilities related to basic computations, while MultiMedQA focuses on assessing clinical knowledge [19], both of which fall short of providing a more comprehensive and fine-grained evaluation; and 3) No existing framework assesses whether LLMs embody the correct scientific research values [21], which is crucial for the responsible adoption of AI techniques in scientific tasks.

To bridge these critical gaps, here we present SciHorizon—an integrated assessment framework that evaluates AI4Science readiness from both AI-ready data and LLM perspectives. For AI-ready scientific data, we propose a generalizable AI-readiness assessment framework, across four principal dimensions—Quality, FAIRness, Explainability, and Compliance—operationalized through 15 sub-dimensions. To demonstrate its applicability, we analyze approximately 1,500 datasets published between 2018 and 2023, primarily consisting of those published in data resource papers in peer-reviewed journals (e.g., Scientific Data and ESSD), identifying dataset recommendations for Earth and Life Sciences to support AI-driven scientific advancements. For the LLM capability on different disciplines, we develop a fine-grained assessment matrix spanning five core competencies—Knowledge, Understanding, Reasoning, Multimodality, and Values—granularized into 16 sub-dimensions. Our benchmark suite, covering Mathematics, Physics, Chemistry, Life Sciences, and Earth and Space Sciences, enables systematic comparison of more than 20 representative open-source and closedsource LLMs. All the results are publicly available and can be accessed online at www.scihorizon.cn/en 1.

### 2 Related Works

The related works of this paper can be grouped into two categories, namely Data AI-Readiness and LLM Benchmarking.

#### 2.1 Data AI-Readiness

The assessment of data AI-readiness has drawn more and more attention. Hiniduma et al. proposed a taxonomy of data readiness for AI metrics [23] and developed a quantitative assessment framework for data AI readiness [24]. They are mainly from a data modality perspective and lack of support and applicability for scientific data. Regarding to the scientific data, the FAIR principles (Findable, Accessible, Interoperable, Reusable) presented in 2016 have been widely recognized as basic characteristics for scientific data sharing [25]. The principles are also used for AI-readiness assessment for scientific data [26, 27]. Besides FAIRness evaluation, some further practices on AI-readiness assessment have also been carried out. ESIP Data Readiness Cluster published a checklist to examine AI-readiness for open environmental datasets [28], covering data quality, data documentation, data access, and data preparation. The checklist is much more a guidance than an evaluation and has less involvement in the

1The platform was initially launched on January 22, 2025 [22].

![image 1](Qin et al._2025_SciHorizon Benchmarking AI-for-Science Readiness from Scientific Data to Large Language Models_images/imageFile1.png)

![image 2](Qin et al._2025_SciHorizon Benchmarking AI-for-Science Readiness from Scientific Data to Large Language Models_images/imageFile2.png)

![image 3](Qin et al._2025_SciHorizon Benchmarking AI-for-Science Readiness from Scientific Data to Large Language Models_images/imageFile3.png)

a) SciHorizon Platform b) Scientific Data Assessment c) LLM Assessment

Fig. 1: Overview of the SciHorizon platform.

AI applications. NIH Bridge to Artificial Intelligence (Bridge2AI) Standards Working Group presented criteria and methods for assessing the AI-readiness of biomedical data [29], which is a good practice for a specific discipline. Although all these separate studies have been developed, comprehensive approaches for AI-readiness assessment for scientific data are still needed.

#### 2.2 LLM Benchmarking

With the rapid advancement of LLMs, numerous benchmarks have emerged to assess their performance across scientific disciplines. Early evaluations focused primarily on mathematical reasoning, such as GSM8K [18] and MATH [30]. Recently, specialized benchmarks such as TheoremQA [31] and MathVista [32] have been introduced to assess theorem-based reasoning and multimodal mathematical understanding. In addition to mathematics, researchers have developed broader scientific benchmarks to evaluate LLMs across multiple domains, such as ScienceQA [33], JEEBench [20], SciEval [34], AGIEval [35], and BIG-Bench [36]. Despite these advancements, existing benchmarks are still limited in scope. Most focus on isolated disciplines [37], without providing a unified framework for cross-disciplinary evaluation. Furthermore, many evaluations prioritize factual recall [38, 39], overlooking the need for fine-grained assessments of scientific problem-solving and advanced reasoning. More critically, no benchmark systematically evaluates whether LLMs adhere to fundamental scientific research values—such as academic integrity, fairness, and transparency—which are crucial for their responsible use in scientific workflows [21].

### 3 SciHorizon Framework

The framework of SciHorizon consists of two components: scientific data assessment and LLM assessment. Figure 1 presents an overview of the SciHorizon platform and its fine-grained assessment dimensions for both scientific data and LLMs.

#### 3.1 Scientific Data Assessment

To systematically assess the AI readiness of scientific datasets, we have developed a comprehensive evaluation framework based on four key dimensions: Quality, FAIRness, Explainability, and Compliance. The following sections provide a detailed overview of this assessment framework and its practices.

###### 3.1.1 Quality

This metric measures the Completeness, Accuracy, Consistency, and Timeliness of datasets to make sure the datasets are of high quality. We expand the traditional quality metrics by combining characteristics of scientific data.

- • Completeness refers to the thorough recording of data elements and the inclusion of all necessary documents. This encompasses not only the data entity itself but also the corresponding data description files or metadata.
- • Accuracy requires minimal noise and redundancy. Moreover, for reproduced data, the processing methods should be clearly documented or supplemented with an accuracy analysis.
- • Consistency refers to both internal coherence within a dataset and external alignment with related datasets, ensuring that the same labels are used for identical variables.
- • Timeliness refers to the prompt publication and continuous updating of data. For instance, time-sequenced data typically evolve over time. The timeliness metric evaluates whether datasets have been updated following their initial publication.


###### 3.1.2 FAIRness

This metric measures the readiness of data for sharing by evaluating its FAIR principles, i.e., Findability, Accessibility, Interoperability, and Reusability. Given that these principles are well established within the research community, we do not reiterate the criteria here. However, our approach to measuring FAIRness differs from previous work in that we establish a recommended set of identifiers, vocabularies, formats, and standards, translating the principles into practical and actionable metrics.

###### 3.1.3 Explainability

This metric measures the application-oriented explainability of data, which is essential for scientific AI models. To ensure that data accurately reflect scientific facts and enhance model explainability, it is important to assess their Diversity, Unbias, Domain Applicability, and Task Applicability.

- • Diversity refers to the scale of dataset parameters and knowledge elements. Generally, the more parameters there are, the richer the knowledge information contained in the data.
- • Unbias assesses the coverage and representativeness of data across different parameters. When a dataset includes multiple classifications, the distribution of each


- category should be balanced or aligned with natural distributions. For instance, in Earth Science data, both temporal and spatial coverage should be assessed to ensure representativeness.
- • Domain Applicability is assessed based on the dataset’s usability with domainspecific tools and its suitability for field research. These aspects can be indicated through documented use cases and citation records.
- • Task Applicability refers to the suitability of data for AI tasks. Data should be structured and formatted in a way that aligns with the requirements of typical AI applications.


###### 3.1.4 Compliance

Model training on vast diverse data raises legal and ethical concerns. Provenance, Ethics, Safety, and Trustworthiness are important factors for ensuring the compliance of scientific AI models.

- • Provenance requires clear documentation of data sources, authorship, licensing, and other relevant metadata to ensure transparency and traceability.
- • Ethics & Safety requires adherence to scientific ethical standards. For instance, data related to Life Sciences should include appropriate documentation or materials for ethical review to ensure compliance with ethical guidelines.
- • Trustworthiness refers to compliance with national regulations and the sustainability of data services. Metadata standards and identifiers should align with national guidelines, and the repository where the data are deposited must be reliable and trustworthy.


###### 3.1.5 Assessment Practices

We set up an integrated framework for AI-Readiness evaluation combining qualitative and quantitative evaluation. To evaluate the ‌Quality, Explainability, and Compliance‌ of the data governance framework, we implemented a hybrid ‌human-in-the-loop‌ review mechanism integrating computational pre-screening and Delphi process of expert consensus. Initially, pre-trained expert models generated sub-dimensional numerical outputs for each metric. These outputs combined quantifiable parameters and modelinferred values derived from historical expert knowledge. Subsequently, we invited 10 domain experts in data governance engaged in the ‌Delphi iterative review‌: across multiple anonymized rounds, they critically evaluated the system-generated values, proposing adjustments to address semantic biases in explainability or recalibrate compliance weightings. This process continued until the system outputs and expert judgments converged to a unified consensus [40]. To evaluate the FAIRness of scientific data, we utilized an evaluation toolkit developed by the Computer Network Information Center of the Chinese Academy of Sciences [41]. This toolkit operationalized domain-specific FAIR principles through automated metadata validation and reproducibility tests, ensuring standardized and objective assessments of data assets across storage, sharing, and reuse workflows.

#### 3.2 LLM Assessment

Assessing LLMs in AI4Science applications requires a comprehensive framework that systematically examines multiple dimensions of model capabilities. Existing benchmarks are either too broad to capture scientific depth or too specialized to cover multiple disciplines. To address these limitations, we propose a multi-dimensional assessment framework specifically designed for AI4Science across various disciplines. Our benchmark assesses LLMs across five fundamental dimensions: Knowledge, Reasoning, Understanding, Multimodality, and Values. Each dimension represents a distinct yet complementary aspect of an LLM’s scientific competence, ensuring a rigorous and actionable assessment. The following sections detail the design and assessment criteria for each dimension.

###### 3.2.1 Knowledge

Knowledge aims to assesses an LLM’s ability to acquire and apply scientific knowledge across various domains. Traditional knowledge assessments primarily focus on factuality, often overlooking finer-grained aspects of knowledge application. To provide a more comprehensive assessment, we decompose knowledge into four key subdimensions: Factuality, Robustness, Externalization, and Helpfulness, as detailed below.

• Factuality: Factuality refers to the extent to which generated text is free from factual errors [42]. It serves as a fundamental criterion in knowledge assessment, ensuring that LLMs produce scientifically accurate responses to domain-specific questions.

We have extensively collected a large number of public datasets for scientific question answering, including AGIEval [35], C-Eval [43], CMB [44], CMMLU [45], Xiezhi [46], BB-GeoEval [47], and Replication [48]. Additionally, we engaged experts to organize, translate, and refine these datasets to ensure linguistic consistency and domain accuracy. This process resulted in a unified set of multiple-choice questions. The unified dataset serves as the foundation for the entire knowledge dimension assessment. To quantify factual accuracy, we calculate the score as: S1k = # Correct# QuestionsResponses, where # denotes the count. S1k measures the LLM’s ability to recognize domain-specific knowledge without reasoning or interpretation.

• Robustness: Robustness refers to an LLM’s ability to handle noisy input while maintaining accurate responses. To assess this capability, we introduce perturbations in the question text using word dropout, synonym replacement, and character swaps. The model is then required to denoise the input and generate the correct answer.

We quantify Robustness by computing the model’s accuracy on altered input,

denoted as S2k. A higher accuracy score indicates that the model effectively handles noisy or altered input while maintaining the ability to generate correct scientific answers.

• Externalization: Externalization refers to an LLM’s ability to articulate acquired scientific knowledge in a clear, logical, and coherent manner. This dimension assesses the model’s capacity to convey domain knowledge in a structured and comprehensible way.

To assess this capability, we prompt the model to generate competing explanations for hypotheses following IBE-Eval [49]. To enhance logical coherence and facilitate further analysis, the model’s responses are constrained to an If-Then format.

This approach ensures that the model generates structured and logically coherent knowledge. Since such knowledge is typically presented as long-form text with multiple sentences, we propose measuring sentence-level cohesion [50], which quantifies fluency and logical connectivity between sentences. Sentence-level cohesion is assessed by analyzing the perplexity of individual sentences using a GPT-based model:

S3k = |x1| |ix=1| PPL(1 x

i), where PPL(xi) is computed by GPT-Neo [51], x represents the generated knowledge, |x| denotes the total number of sentences in the generated text, and PPL(xi) represents the perplexity of sentence xi. A higher S3k indicates stronger externalization capabilities, meaning the model consistently produces sentences with lower perplexity. This ensures that scientific knowledge is not only accurate but also effectively communicated in AI4Science applications.

• Helpfulness: Helpfulness refers to an LLM’s ability to provide scientifically useful and relevant knowledge that aids in problem-solving. This dimension assesses whether the knowledge generated by the LLM is actionable and effective in guiding low-parameter LLMs in scientific question-answering and decision-making.

To assess Helpfulness, we employ a two-step assessment procedure. First, we generate domain-specific knowledge using the assessed LLM. Then, we inject generate knowledge into a low-parameter model, such as LLaMA3-8B [52], and assess its ability to utilize the provided information to answer a scientific multiple-choice question. Helpfulness is measured based on the accuracy of the low-parameter model in selecting the correct answer after receiving the additional knowledge, denoted as S4k. A higher Helpfulness score indicates that the knowledge provided by the LLM is both relevant and useful for guiding problem-solving. This ensures that AI4Science models generate practical and applicable scientific insights.

###### 3.2.2 Understanding

The assessment of Understanding in LLMs assesses their ability to comprehend and contextualize scientific content across diverse disciplines. The assessment primarily focuses on Scientific Fact Understanding tasks, which test the model’s ability to interpret and understand complex scientific concepts beyond factual memorization. Understanding is crucial to ensuring that LLMs are not merely capable of recalling information but can also demonstrate deep comprehension of scientific content.

To assess LLMs’ Understanding of scientific concepts across various disciplines, we curate domain-specific datasets for assessment. For Life Sciences, we use MedMCQA [53], MedQA [54], and GPT-3 Clinical Vignettes [55]. Chemistry assessment is conducted using ChEBI-20 [56], while Earth and Space Sciences are assessed with GeoBench [57]. For Mathematics, we employ MathBench [58], and for Physics, SciEval [34]. To ensure these datasets effectively measure comprehension rather than simple recall, we enlist experts to refine and transform them into multiple-choice questions that assess the model’s grasp of scientific content.

###### 3.2.3 Reasoning

The assessment of reasoning capabilities in LLMs is crucial for assessing their ability to process information, analyze data, and derive logical conclusions across various scientific disciplines. However, existing benchmarks primarily focus on numerical reasoning, which is often limited to elementary arithmetic operations such as addition, subtraction, multiplication, and exponentiation, such as MMLU [30] and AGIEval [35]. To address this gap, we propose a novel reasoning assessment that incorporates both numerical reasoning and deductive reasoning.

- • Numerical Reasoning: Numerical Reasoning assesses an LLM’s ability to perform arithmetic operations, interpret quantitative data, and solve mathematical problems within scientific contexts. To assess this capability, we employ a curated set of expert-filtered datasets spanning multiple scientific disciplines. For Life Sciences and Chemistry, we utilize GPQA [59], MMLU [30], SciEval [34], and ScienceQA [33]. The Earth and Space Sciences assessment is based on MMLU and ScienceQA, while Mathematics is assessed using AQuA [60], BigBench [36], MATHQA [61], and MMLU. Finally, Physics reasoning is tested using BigBench, GPQA, MMLU, SciEval, and ScienceQA. Each dataset consists of structured, multiple-choice numerical reasoning tasks covering mathematical modeling, quantitative estimation, and applied problemsolving in scientific contexts. Model performance is quantified by accuracy, denoted as S1r, which measures the correctness of the model’s responses.
- • Deductive Reasoning: Deductive Reasoning assesses an LLM’s ability to derive specific conclusions from general scientific principles or premises. This reasoning form is critical in scientific research, enabling models to formulate hypotheses, design experiments, and conduct theoretical analyses with logical consistency. For rigorous assessment, we employ experts to construct the datasets across different domains, adapting task formats to emphasize logical inference over computational ability.


Deductive Reasoning performance is measured by accuracy, denoted as S2r. By integrating numerical and deductive reasoning assessments, we define the reasoning metric as: Sr = 2i=1 Sir/2.

###### 3.2.4 Multimodality

The Multimodality dimension assesses LLMs based on their ability to comprehend and reason with multimodal scientific information. We define two primary sub-dimensions for assessing multimodal capabilities:

- • Scientific Chart Understanding: Assesses an LLM’s ability to extract factual information, analyze data trends, and identify categorical relationships and key insights from scientific visual representations, such as line graphs and bar charts.
- • Scientific Chart Reasoning: Assesses an LLM’s capacity for higher-order reasoning, drawing conclusions, and applying scientific knowledge to predict outcomes based on visual data. Unlike basic data comprehension, this dimension requires logical inference.


To assess the Multimodal dimension, we collect a large number of scientific charts and employ domain experts for the construction of a multimodal benchmark dataset.

The dataset consists of multiple-choice questions. Model performance is quantified by accuracy, denoted as S1m for understanding and S2m for reasoning, respectively.

###### 3.2.5 Values

The assessment of value alignment aims to assess an LLM’s adherence to ethical and moral standards, particularly in scientific contexts. We are the first to introduce the assessment in scientific research value. This dimension ensures that LLMs not only generate accurate outputs but also uphold integrity, fairness, and social responsibility in their applications.

Our value alignment framework is grounded in widely recognized ethical guidelines, including Compliance with Laws and Regulations, Academic Integrity, Commitment to Objective Truth, Respect for Humanity and Nature, Fairness and Justice, Privacy and Security Protection, and Transparency and Explainability. The details of seven ethical dimensions are as follows:

- • Compliance with Laws and Regulations: Ensuring that the decisions made are in accordance with relevant legal frameworks, such as data protection laws and intellectual property rights. This includes respecting the boundaries set by laws governing the research and application of AI.
- • Academic Integrity: Preventing unethical academic behaviors such as plagiarism, data manipulation, or fabrication. This involves making decisions that ensure transparency, honesty, and fairness in research, safeguarding the credibility of scientific work.
- • Adherence to Objective Truth: Prioritizing the use of accurate, unbiased data and scientific facts in decision-making. This value emphasizes the importance of avoiding distortion or misinformation in research findings, ensuring that only truthful and reliable data are used.
- • Respect for Humanity and Nature: Making decisions that respect human dignity, fundamental rights, and environmental sustainability. This value highlights the need to balance human welfare and ecological impact when making choices that affect society and the environment.
- • Maintenance of Fairness and Justice: Ensuring that decisions do not perpetuate biases related to gender, race, culture, or other demographic factors. Fairness and justice require that all individuals are treated equitably, and that decisions do not exacerbate existing societal inequalities.
- • Attention to Privacy and Security: Protecting personal data and ensuring that decisions respect privacy laws. This value underscores the importance of maintaining data security and preventing unauthorized access, breaches, or misuse of sensitive information.
- • Ensuring Transparency and Explainability: Making decisions that are transparent and explainable, with clear justifications that are accessible and understandable to users. Transparency and explainability ensure that the decision-making process is auditable and accountable, providing insight into how and why specific outcomes were reached.


To systematically assess Values in LLMs, we propose a GPT-based pipeline for constructing ethical assessment questions for each sub-dimension. This pipeline comprises four sequential steps:

- 1. Generating Research Scenarios We first create structured research contexts

for different scientific disciplines as follows:

Assume you are a researcher in {Primary Discipline}, specializing in {Secondary Discipline}. Provide a structured list of research directions and subtopics, following established disciplinary classification standards.

- 2. Expanding Subtopic Information For each identified research subtopic,

we generate a detailed description along with its hierarchical relationship to broader disciplines:

Given the subtopic {Subtopic Name}, which belongs to the hierarchy {Primary Discipline} → {Secondary Discipline} → {Research Direction}, describe its relationships with each category. Return the result in the JSON format:

- 3. Generating Ethical Guidelines Next, we derive discipline-specific ethical

guidelines aligned with predefined ethical principles:

Assume you are a researcher in {Discipline}, focusing on {Research Direction}. Identify relevant ethical guidelines and map them to the principles Target Ethical Principle: Definition of Ethical Principle

- 4. Generating Scenario-Based Ethical Questions Finally, we construct


multiple-choice questions to assess ethical adherence:

Assume you are conducting research in {Primary Discipline}, specializing in {Research Direction}. Create a multiple-choice question with a scenario-based setup to assess adherence to the ethical principle: {Target Ethical Principle}. Ensure the scenario includes specific time, location, individuals, and events and return the question in the following format:

Following the automatic generation of questions, domain experts review and filter them based on relevance, clarity, fairness, and validity as follows:

- • Relevance – Ensuring realistic and discipline-specific scenarios.
- • Clarity – Refining ambiguous or misleading phrasing.
- • Fairness – Avoiding biased or culturally sensitive framing.
- • Validity – Confirming that questions assess ethical principles rather than factual knowledge.


By implementing this structured pipeline, we establish a rigorous framework for assessing ethical alignment in LLMs. Model performance is measured by accuracy, denoted as Sv.

###### Table 1: Performance of evaluated data across Earth Science. The table reports thescores of each data in Quality (Q), FAIRness (F), Explainability (E), and Compliance(C).

Data Q F E C China meteorological forcing dataset (1979-2018) [62] 4.50 4.66 4.38 5.00 Bias-corrected CMIP6 global dataset for dynamical downscaling of the historical and future climate (1979–2100) [63]

4.90 4.36 4.25 5.00

The 30m annual land cover dataset and its dynamics in China from 1990 to 2019 [64] 4.90 4.46 4.25 4.00 High-resolution datasets of permafrost thermal state and hydrothermal zonation in the Northern Hemisphere [65]

4.40 4.66 4.19 5.00

A synthesis dataset of permafrost thermal state for the Qinghai-Tibet (Xizang) Plateau, China [66] 4.50 4.66 3.75 5.00 GLC FCS30: Global land-cover product with fine classification system at 30 m using time-series Landsat imagery [67]

4.30 4.46 4.25 4.00

A global dataset of annual urban extents (1992-2020) from harmonized nighttime lights [68] 4.40 4.38 4.12 4.00 Vectorized rooftop area data for 90 cities in China [69] 4.40 4.66 3.81 4.00 Global monthly distributions of atmospheric CO2 concentrations under the historical and future scenarios [70]

4.70 4.34 3.75 4.00 Depth-to-bedrock map of China at a spatial resolution of 100 meters [71] 4.30 3.73 4.12 4.00

###### Table 2: Performance of evaluated data across Life Sciences. The table reports thescores of each data in Quality (Q), FAIRness (F), Explainability (E), and Compliance(C).

Data Q F E C MedMNIST v2 - A large-scale lightweight benchmark for 2D and 3D biomedical image classification [72]

4.90 4.46 4.75 3.50

BioWordVec, improving biomedical word embeddings with subword information and MeSH [73]

4.50 4.38 4.75 3.50

gcType:Type Strains Genome Database [74] 4.50 4.38 4.38 4.00 A dataset of distribution and diversity of ticks in China [65] 4.40 4.38 4.00 4.00 The SUSTech-SYSU dataset for automatically segmenting and classifying corneal ulcers [75] 4.50 4.12 4.12 4.00 FIVES: A Fundus Image Dataset for Artificial Intelligence based Vessel Segmentation [76] 4.50 3.52 4.75 4.00 miRTarBase: The experimentally validated microRNA-target interactions database [77] 4.50 3.32 4.38 3.75 A multi-modal open dataset for mental-disorder analysis [78] 4.30 3.68 4.00 3.50 An ATAC-seq atlas of chromatin accessibility in mouse tissues [79] 4.50 2.75 4.38 3.75 Single-cell RNA sequencing of human kidney [80] 4.50 3.20 3.25 4.00

### 4 Results

Here we introduce and discuss the detailed assessment results of both scientific data and LLMs in the SciHorizon platform.

#### 4.1 Results of Scientific Data Assessment

Given that the concept of AI-ready scientific data is still evolving and subject to varying criteria and disciplines, we focus here on two typical natural science domains, namely Earth Science and Life Sciences.

As illustrated in Table 1, the study highlights that reusable scientific data products in the Earth Science field have laid a robust foundation for AI applications. By integrating multi-source data to tackle common scientific challenges, these products generate comprehensive datasets characterized by long-term temporal sequences, extensive spatial coverage, diverse feature elements, and rich semantic content. The primary data modalities consist of tabular and image data, which exhibit strong compatibility with AI model methodologies.

Table 3: Overall performance of evaluated LLMs across multiple scientific disciplines. The overall performance is computed as the average score across the dimensions of Knowledge, Understanding, Reasoning, and Values. The table reports the scores of each model in overall performance and five individual subject areas: Life Sciences (Life), Chemistry, Earth and Space Sciences (Earth), Mathematics, and Physics.

Discipline Overall Life Chemistry Earth Mathematics Physics

DeepSeek-V3 67.29 65.68 67.87 73.60 66.57 62.73 Claude-3.5-Sonnet-20241022 65.01 60.13 73.05 71.51 57.10 63.27 O1-Mini-20240912 64.58 60.89 60.46 66.30 71.69 63.56 Gemini-1.5-Pro-Latest 63.13 60.52 66.45 66.69 61.79 60.18 GPT-4o-20241120 61.99 64.96 66.15 68.46 51.82 58.54 Qwen-Plus 59.83 59.29 56.23 66.27 60.59 56.80 Llama3.1-70B-Instruct 59.20 61.27 61.65 67.73 49.88 55.46 Qwen2.5-72B-Instruct 58.57 56.98 55.27 64.49 59.53 56.59 Yi-Lightning 58.11 56.84 58.14 65.90 53.16 56.53 GLM-4-Plus 57.76 55.02 60.04 64.48 53.87 55.39 Doubao-Pro-32K 57.69 56.78 58.71 62.10 56.83 54.05 Llama-3.2-90B-Vision-Instruct 56.65 56.01 59.32 66.83 48.68 52.44 ERNIE-4.0-Turbo-8K-Latest 56.19 53.42 57.44 63.64 52.29 54.14 GLM-4v-Plus 56.15 54.82 54.81 59.18 49.77 62.19 InternLM3-8B-Instruct 54.58 55.71 54.89 59.30 48.65 54.33 InternLM2.5-20B-Chat 54.53 51.30 53.05 61.28 50.63 56.36 Pixtral-Large-Instruct-2411 54.00 52.32 54.60 63.39 47.84 51.86 Yi-34B-Chat 53.47 53.42 48.94 62.37 45.60 57.00 Mistral-Large-Instruct-2411 52.36 52.28 52.34 60.15 44.16 52.89 Moonshot-V1-32K 52.29 54.92 48.28 61.70 45.89 50.69 GPT-4o-Mini 52.24 54.01 49.60 62.39 45.11 50.07 MiniCPM3-4B 51.39 52.42 44.25 56.99 48.78 54.50 GLM-4-9B-Chat 50.93 49.80 47.90 57.35 46.11 53.50 Llama-3.2-11B-Vision-Instruct 50.66 51.47 51.46 59.10 42.61 48.66 Qwen2-VL-7B-Instruct 49.45 48.15 46.52 57.57 42.08 52.96 Yi-Vision-V2 48.91 47.96 49.85 56.58 44.38 45.76 Llama3.1-8B-Instruct 48.74 49.59 48.45 57.66 40.71 47.29 MiniCPM-V-2.6 46.53 45.53 46.59 54.05 36.87 49.63 Ministral-8B-Instruct-2410 46.34 48.36 46.59 52.70 37.26 46.81 Qwen2.5-7B-Instruct 45.76 45.17 41.23 55.73 42.67 44.00

For example, the China Meteorological Forcing Dataset (CMFD) performs well in terms of FAIRness assessment. It appropriately utilizes DOI and CSTR, provides machine-readable metadata, ensures open access, and supports metadata harvesting protocols. However, it lacks a data entity link in its metadata. The dataset also demonstrates excellent domain applicability, a quality fully acknowledged by domain experts. Additionally, CMFD offers seven meteorological elements with high resolution and continuous temporal coverage, reflecting strong diversity and balance. The rich feature set and standardized data organization indicate significant potential for future AI applications.

Table 4: Performance of LLMs on Knowledge assessment across multiple scientific disciplines.

Discipline Overall Life Chemistry Earth Mathematics Physics

DeepSeek-V3 53.17 58.61 46.36 54.92 58.32 47.64 Qwen2.5-72B-Instruct 51.01 57.87 47.91 53.51 51.16 44.62 Qwen-Plus 50.93 56.11 48.22 52.03 51.65 46.65 Doubao-Pro-32K 50.73 56.90 46.69 50.63 50.84 48.58 Claude-3.5-Sonnet-20241022 50.58 55.17 45.84 61.43 44.47 46.01 InternLM2.5-20B-Chat 49.10 58.23 45.50 49.94 48.07 43.74 Qwen2-VL-7B-Instruct 48.01 55.76 48.85 52.97 39.16 43.30 Yi-34B-Chat 47.33 54.36 44.28 49.27 42.35 46.38 MiniCPM3-4B 47.32 54.08 46.52 48.27 43.86 43.89 ERNIE-4.0-Turbo-8K-Latest 47.25 54.60 42.10 47.42 46.81 45.34 GLM-4-Plus 46.92 53.68 46.80 50.25 38.96 44.91 Llama3.1-70B-Instruct 46.23 56.02 44.77 45.17 43.09 42.13 GLM-4v-Plus 45.83 51.89 40.12 51.10 42.09 43.97 O1-Mini-20240912 45.07 48.89 38.84 48.80 49.67 39.14 Llama-3.2-90B-Vision-Instruct 44.79 54.15 39.57 48.74 40.20 41.28 Yi-Lightning 44.29 52.33 41.44 48.75 37.05 41.89 GPT-4o-20241120 43.01 53.47 36.09 47.70 36.33 41.46 InternLM3-8B-Instruct 42.33 50.97 43.97 44.05 35.12 37.57 Moonshot-V1-32K 41.61 49.86 37.26 46.29 38.91 35.72 GLM-4-9B-Chat 41.46 45.37 41.28 42.73 38.54 39.37 Gemini-1.5-Pro-Latest 40.30 46.25 37.28 39.71 39.65 38.62 Qwen2.5-7B-Instruct 39.53 40.59 43.63 42.93 41.58 28.92 Yi-Vision-V2 39.43 46.32 40.57 41.15 35.05 34.08 MiniCPM-V-2.6 38.08 44.37 42.41 44.14 25.77 33.73 Ministral-8B-Instruct-2410 37.38 41.29 37.16 37.20 34.93 36.32 Pixtral-Large-Instruct-2411 36.92 43.97 33.11 40.60 32.44 34.46 Mistral-Large-Instruct-2411 35.98 43.13 36.59 39.04 28.99 32.13 GPT-4o-Mini 35.38 43.04 33.27 39.61 33.50 27.50 Llama-3.2-11B-Vision-Instruct 34.70 43.38 36.00 37.64 28.90 27.57 Llama3.1-8B-Instruct 33.69 37.90 34.63 37.24 28.10 30.57

#### 4.2 Results of LLM Assessment

In this section, we present a comprehensive evaluation of a diverse range of LLMs for AI4Science, focusing on five core dimensions: Knowledge, Understanding, Reasoning, Multimodality, and Value, along with overall performance.

The evaluation dataset is constructed following the methodology outlined in Section 3.2. The evaluated LLMs encompass both closed-source and open-source models, with a specific focus on their multimodal and non-multimodal capabilities. Specifically, our evaluation includes SOTA proprietary models such as GPT-4o-20241120 [81], GPT-4o-Mini [81], O1-Mini-20240912 [82], ERNIE-4.0-Turbo8K-Latest [83], Claude-3.5-Sonnet-20241022 [84], Doubao-Pro-32K [85], Gemini1.5-Pro-Latest [86], GLM-4-Plus [87], GLM-4v-Plus [88], Moonshot-V1-32K [89], Qwen-Plus [90], Yi-Lightning [91], and Yi-Vision-V2 [92]. Among these, Claude3.5-Sonnet-20241022, Gemini-1.5-Pro-Latest, GLM-4v-Plus, GPT-4o-20241120, GPT4o-Mini, and Yi-Vision-V2 incorporate multimodal capabilities, enabling them to

###### Table 5: Performance of LLMs on Understanding assessment across multiple scientific disciplines.

Discipline Overall Life Chemistry Earth Mathematics Physics

DeepSeek-V3 73.48 64.38 85.00 72.00 82.00 64.00 GPT-4o-20241120 70.27 62.33 93.00 59.00 68.00 69.00 Claude-3.5-Sonnet-20241022 66.92 46.58 95.00 55.00 67.00 71.00 Gemini-1.5-Pro-Latest 66.81 52.05 77.00 59.00 81.00 65.00 O1-Mini-20240912 64.64 58.22 65.00 49.00 86.00 65.00 Qwen2.5-72B-Instruct 61.60 50.00 59.00 51.00 83.00 65.00 Yi-Lightning 61.20 50.00 66.00 55.00 68.00 67.00 Llama3.1-70B-Instruct 60.50 55.48 74.00 61.00 49.00 63.00 Qwen-Plus 60.33 48.63 59.00 57.00 78.00 59.00 Pixtral-Large-Instruct-2411 58.95 39.73 63.00 54.00 67.00 71.00 GLM-4-Plus 56.82 41.10 64.00 50.00 67.00 62.00 ERNIE-4.0-Turbo-8K-Latest 54.96 41.78 63.00 48.00 63.00 59.00 Doubao-Pro-32K 54.38 45.89 58.00 42.00 75.00 51.00 Llama-3.2-90B-Vision-Instruct 51.00 41.78 62.24 53.00 40.00 58.00 GPT-4o-Mini 50.79 47.95 48.00 53.00 48.00 57.00 InternLM3-8B-Instruct 49.15 39.73 45.00 47.00 60.00 54.00 GLM-4v-Plus 49.01 39.04 42.00 42.00 53.00 69.00 Mistral-Large-Instruct-2411 47.55 39.73 47.00 38.00 48.00 65.00 Llama-3.2-11B-Vision-Instruct 47.06 43.15 50.75 47.00 42.42 52.00 InternLM2.5-20B-Chat 46.86 36.30 42.00 47.00 54.00 55.00 Moonshot-V1-32K 45.71 36.99 32.00 54.55 52.00 53.00 Yi-34B-Chat 44.46 36.30 31.00 42.00 53.00 60.00 Llama3.1-8B-Instruct 43.78 45.89 39.00 46.00 38.00 50.00 MiniCPM3-4B 42.41 39.04 17.00 42.00 53.00 61.00 GLM-4-9B-Chat 41.72 35.62 25.00 44.00 46.00 58.00 MiniCPM-V-2.6 41.21 39.04 24.00 45.00 45.00 53.00 Ministral-8B-Instruct-2410 40.89 42.47 31.00 43.00 41.00 47.00 Yi-Vision-V2 40.26 36.30 36.00 40.00 45.00 44.00 Qwen2-VL-7B-Instruct 38.19 34.93 15.00 36.00 55.00 50.00 Qwen2.5-7B-Instruct 32.76 30.82 5.00 32.00 52.00 44.00

process both textual and visual inputs. Additionally, we evaluated a broad spectrum of open-source models, highlighting their accessibility and customizability for AI4Science applications. Our evaluation includes DeepSeek-V3 [93], GLM-4-9BChat [94], InternLM2.5-20B-Chat [95], InternLM3-8B-Instruct [96], Llama3.1-8BInstruct [97], Llama-3.2-11B-Vision-Instruct [98], Llama3.1-70B-Instruct [99], Llama-

- 3.2-90B-Vision-Instruct [100], MiniCPM3-4B [101], MiniCPM-V-2.6 [102], Mistral8B-Instruct-2410 [103], Mistral-Large-Instruct-2411 [104], Pixtral-Large-Instruct2411 [105], Qwen2.5-72B-Instruct [106], Qwen2.5-7B-Instruct [107], Qwen2-VL-7BInstruct [108], and Yi-34B-Chat [109]. Among these, Llama-3.2-11B-Vision-Instruct, Llama-3.2-90B-Vision-Instruct, MiniCPM-V-2.6, and Qwen2-VL-7B-Instruct exhibit multimodal capabilities, extending their usability beyond textual tasks.


By evaluating a diverse set of LLMs from both closed- and open-source domains, our study comprehensively assesses their scientific capabilities across five dimensions. The overall performance is calculated as the average of the Knowledge, Understanding, Reasoning, and Values dimensions, excluding Multimodality, as some LLMs lack

Table 6: Performance of LLMs on Reasoning assessment across multiple scientific disciplines.

Discipline Overall Life Chemistry Earth Mathematics Physics

O1-Mini-20240912 85.25 80.50 77.65 95.97 87.09 85.05 DeepSeek-V3 79.66 78.86 79.62 92.46 64.92 82.45 Gemini-1.5-Pro-Latest 79.07 77.72 82.88 92.99 62.68 79.07 Claude-3.5-Sonnet-20241022 74.89 74.65 78.33 95.17 53.20 73.09 GPT-4o-20241120 72.36 80.78 73.79 97.08 41.05 69.11 Qwen-Plus 72.18 71.71 71.89 87.58 55.89 73.84 Qwen2.5-72B-Instruct 72.13 70.07 72.80 91.66 53.25 72.87 Llama3.1-70B-Instruct 71.06 76.00 71.59 90.29 46.95 70.49 Doubao-Pro-32K 70.81 67.28 75.15 87.63 51.72 72.27 GLM-4-Plus 69.24 68.93 71.29 92.77 45.91 67.29 Llama-3.2-90B-Vision-Instruct 69.12 69.77 70.61 90.56 51.03 63.63 ERNIE-4.0-Turbo-8K-Latest 67.01 65.85 69.85 91.71 41.54 66.09 Mistral-Large-Instruct-2411 66.66 67.43 70.38 93.84 38.96 62.69 Yi-Lightning 66.23 70.00 63.56 89.49 45.96 62.13 Moonshot-V1-32K 65.77 72.72 70.68 80.31 41.05 64.09 GLM-4v-Plus 65.74 66.86 72.58 77.61 39.46 72.22 GPT-4o-Mini 65.19 72.86 66.06 86.25 35.09 65.71 Pixtral-Large-Instruct-2411 65.07 70.38 69.47 94.10 35.44 55.95 InternLM2.5-20B-Chat 64.93 61.28 66.37 80.84 52.27 63.89 InternLM3-8B-Instruct 64.79 72.78 71.06 77.55 41.05 61.51 Llama-3.2-11B-Vision-Instruct 62.58 61.95 64.08 84.17 43.75 58.98 Yi-34B-Chat 61.94 65.22 60.83 92.24 27.95 63.49 GLM-4-9B-Chat 61.17 61.57 67.65 73.78 43.13 59.71 Llama3.1-8B-Instruct 60.61 58.78 65.76 81.73 43.47 53.31 MiniCPM3-4B 60.44 60.71 60.53 77.07 44.37 59.51 Ministral-8B-Instruct-2410 60.31 63.50 69.47 79.29 31.96 57.31 Yi-Vision-V2 58.81 56.00 61.44 78.18 43.33 55.11 Qwen2.5-7B-Instruct 57.66 53.64 67.95 81.95 31.62 53.11 Qwen2-VL-7B-Instruct 55.49 49.79 63.94 77.61 27.40 58.71 MiniCPM-V-2.6 54.52 53.22 60.53 67.89 32.45 58.54

multimodal support. This evaluation offers valuable insights into the strengths and limitations of contemporary LLMs in AI4Science, guiding future research in LLM-driven scientific intelligence.

###### 4.2.1 Overall Performance

Table 3 presents the overall performance of each model across multiple scientific disciplines. Among all models, the Chinese open-source model DeepSeek-V3 achieves the highest overall score of 67.29, demonstrating a well-balanced capability across various knowledge domains. Claude-3.5-Sonnet (65.01) and O1-Mini (64.58) closely follow, highlighting their competitive performance. Additionally, the open-source model Llama3.1-70B and the closed-source model GLM-4-Plus also rank among the topperforming models. Among other domestic models, Qwen-Plus and Doubao-Pro-32K exhibit strong performance, reflecting their balanced and comprehensive capabilities.

###### Table 7: Performance of LLMs on Multimodality assessment across multiple scientific disciplines.

Discipline Overall Life Chemistry Earth Mathematics Physics

Claude-3.5-Sonnet-20241022 58.93 60.00 61.93 69.55 55.95 47.22 Gemini-1.5-Pro-Latest 56.88 60.05 48.87 65.33 64.25 45.88 GLM-4v-Plus 54.09 50.00 48.71 57.20 67.50 47.05 Llama-3.2-90B-Vision-Instruct 51.40 57.60 54.47 55.03 56.50 33.43 GPT-4o-20241120 50.19 45.10 37.96 51.47 70.00 46.41 MiniCPM-V-2.6 48.72 48.04 42.80 44.55 59.75 48.44 Qwen2-VL-7B-Instruct 40.76 34.07 50.95 48.20 33.75 36.84 Llama-3.2-11B-Vision-Instruct 40.72 46.08 38.69 36.95 47.75 34.12 GPT-4o-Mini 37.44 37.26 37.29 35.86 44.00 32.79 Yi-Vision-V2 35.89 19.61 31.41 37.39 62.75 28.32

From a disciplinary perspective, DeepSeek-V3 achieves the highest scores in Life Sciences (65.68) and Earth and Space Sciences (73.60), demonstrating strong domain knowledge in Life Sciences as well as spatial reasoning and map-based knowledge comprehension.O1-Mini excels in Mathematics (71.69) and Physics (63.56), demonstrating superior numerical and physical reasoning. However, its performance in other subjects is comparatively weaker. Meanwhile, Claude-3.5-Sonnet exhibits the strongest Chemistry understanding (73.05), outperforming all other models in this domain. These results highlight the diverse strengths of different LLMs, with DeepSeek-V3 excelling in Life and Earth sciences, O1-Mini in quantitative reasoning, and Claude-

- 3.5-Sonnet in Chemistry, showcasing distinct model specializations in AI4Science applications.

To further analyze model performance across different evaluation dimensions, Figure 2 presents radar charts depicting the capabilities of the top-performing LLMs in five key dimensions: Knowledge, Understanding, Reasoning, Multimodality, and Values along with the overall performance. The visualization highlights how LLMs vary in strengths across disciplines and dimensions, providing deeper insights into their specialization. Notably, DeepSeek-V3 exhibits consistently high scores across most dimensions, particularly excelling in Understanding and Reasoning. Claude-3.5Sonnet outperforms other models in Values and Chemistry-related tasks, reinforcing its strong domain-specific alignment. O1-Mini, despite leading in numerical disciplines such as Mathematics and Physics, shows comparatively lower scores in other areas. Additionally, multimodal models such as GPT-4o and Gemini-1.5-Pro demonstrate competitive performance in disciplines that require cross-modal information integration. These radar charts illustrate the varying trade-offs among LLMs, emphasizing their domain-specific capabilities and the importance of tailored model selection for different AI4Science applications.

- 4.2.2 Knowledge Evaluation


We evaluated the ability of LLM to acquire and apply key knowledge in different disciplines (Table 4). DeepSeek-V3 achieves the highest knowledge score (53.17), excelling in Life Sciences (58.61) and Mathematics (58.32). Qwen2.5-72B-Instruct (51.01) and

Table 8: Performance of LLMs on Values assessment across multiple scientific disciplines.

Discipline Overall Life Chemistry Earth Mathematics Physics

Claude-3.5-Sonnet-20241022 67.67 64.12 73.04 74.46 63.75 62.99 Gemini-1.5-Pro-Latest 66.33 66.07 68.64 75.04 63.85 58.03 GLM-4v-Plus 64.03 61.48 64.56 66.01 64.54 63.57 O1-Mini-20240912 63.36 55.95 60.36 71.44 64.02 65.04 DeepSeek-V3 62.86 60.89 60.50 75.02 61.06 56.83 GPT-4o-20241120 62.31 63.27 61.70 70.07 61.92 54.59 InternLM3-8B-Instruct 62.03 59.35 59.54 68.59 58.42 64.26 Llama-3.2-90B-Vision-Instruct 61.71 58.33 64.85 75.02 63.48 46.85 Yi-Lightning 60.74 55.02 61.58 70.37 61.62 55.10 Yi-34B-Chat 60.14 57.82 59.66 65.98 59.12 58.13 GLM-4-9B-Chat 59.37 56.63 57.68 68.87 56.78 56.91 Mistral-Large-Instruct-2411 59.27 58.84 55.38 69.71 60.70 51.73 Llama3.1-70B-Instruct 59.00 57.57 56.24 74.47 60.48 46.24 Llama-3.2-11B-Vision-Instruct 58.29 57.40 55.00 67.57 55.38 56.10 GLM-4-Plus 58.06 56.38 58.05 64.92 63.60 47.35 GPT-4o-Mini 57.58 52.21 51.07 70.70 63.86 50.08 InternLM2.5-20B-Chat 57.22 49.40 58.35 67.33 48.19 62.83 Yi-Vision-V2 57.12 53.23 61.37 66.99 54.13 49.86 Llama3.1-8B-Instruct 56.88 55.78 54.40 65.67 53.25 55.29 Qwen2-VL-7B-Instruct 56.14 52.12 58.29 63.70 46.75 59.82 Moonshot-V1-32K 56.09 60.12 53.18 65.64 51.59 49.95 Qwen-Plus 55.90 60.71 45.80 68.45 56.81 47.71 ERNIE-4.0-Turbo-8K-Latest 55.53 51.44 54.83 67.41 57.82 46.14 MiniCPM3-4B 55.38 55.87 52.96 60.62 53.87 53.60 Pixtral-Large-Instruct-2411 55.07 55.19 52.84 64.84 56.48 46.01 Doubao-Pro-32K 54.86 57.06 54.99 68.13 49.78 44.35 Qwen2.5-7B-Instruct 53.08 55.61 48.33 66.04 45.47 49.95 MiniCPM-V-2.6 52.31 45.49 59.42 59.17 44.24 53.24 Qwen2.5-72B-Instruct 49.55 50.00 41.38 61.80 50.70 43.88 Ministral-8B-Instruct-2410 46.79 46.17 48.74 51.31 41.15 46.59

Qwen-Plus (50.93) also perform well, suggesting that domestic open-source models can compete effectively in knowledge retention. Notably, Claude-3.5-Sonnet outperforms all models in Chemistry (61.43), highlighting its domain-specific factual accuracy in molecular sciences. DeepSeek-V3 leads in Physics (47.64), suggesting better recall of fundamental scientific principles.

###### 4.2.3 Understanding Evaluation

We evaluated the ability of LLM to understand scientific facts (Table 5). DeepSeek-V3 (73.48) continues to lead, particularly excelling in Chemistry (85.00) and Mathematics (82.00). GPT-4o (70.27) ranks second overall, showing strong performance in Physics (69.00) and Life Sciences (62.33), highlighting its generalized reasoning ability. Claude-3.5-Sonnet (66.92) ranks third, achieving the highest Chemistry score (95.00), indicating superior contextual knowledge application in scientific disciplines. Interestingly, O1-Mini achieves the best performance in Mathematics (86.00), demonstrating

Claude-3.5-Sonnet-20241022

Doubao-Pro-32K

GLM-4-9B-Chat

GPT-4o-20241120

Gemini-1.5-Pro-Latest

DeepSeek-V3

ERNIE-4.0-Turbo-8K-Latest

GLM-4v-Plus

GPT-4o-Mini

###### Overall

###### Knowledge

###### Understanding

Chemistry

Chemistry

Chemistry

Geography

Geography

Geography

102030405060

80

60

60

40

40

20

20

Biology

Biology

Biology

Mathematics

Mathematics

Mathematics

Physics

Physics

Physics

###### Reasoning

###### MultiModal

Value

Chemistry

Chemistry

Chemistry

Geography

Geography

Geography

60

80

60

60

40

40

40

20

20

20

Biology

Biology

Biology

Mathematics

Mathematics

Mathematics

Physics

Physics

Physics

Fig. 2: Radar charts of top LLMs’ performance across disciplines. This figure illustrates the top 5 LLMs’ capabilities in six evaluation dimensions: Overall, Knowledge, Understanding, Reasoning, Multimodality, and Value. Each chart displays performance across five disciplines: Mathematics, Physics, Chemistry, Life Sciences (Life), and Earth and Space Sciences (Earth).

strong numerical comprehension. These results suggest that while DeepSeek-V3 and GPT-4o offer balanced generalization, some models (e.g., Claude-3.5-Sonnet, O1-Mini) specialize in specific domains.

###### 4.2.4 Reasoning Evaluation

For the Reasoning (Table 6), O1-Mini (85.25) outperforms all models, demonstrating SOTA reasoning capabilities, especially in Mathematics (87.09) and Physics (85.05). DeepSeek-V3 (79.66) and Gemini-1.5-Pro-Latest (79.07) also perform well, with DeepSeek-V3 excelling in Earth and Space Sciences (92.46). GPT-4o (72.36) and Claude-3.5-Sonnet (74.89) rank among the top models, confirming their robust logical inference abilities. These results highlight that reasoning ability varies significantly across models, with O1-Mini and DeepSeek-V3 excelling in mathematical and spatial logic, while Claude-3.5-Sonnet and GPT-4o demonstrate strong general reasoning across multiple subjects.

###### 4.2.5 Multimodality Evaluation

For different LLMs’ abilities in understanding and reasoning about scientific charts (Table 7), Claude-3.5-Sonnet (58.93) ranks highest, particularly excelling in Chemistry (61.93) and Earth and Space Sciences (69.55). Gemini-1.5-Pro-Latest (56.88) and GLM-4v-Plus (54.09) also demonstrate strong multimodality capabilities. These results indicate that multimodality learning remains an evolving challenge, with closedsource models (e.g., Claude, Gemini) maintaining a significant advantage in integrating visual and textual reasoning.

###### 4.2.6 Values Evaluation

For assessing whether different LLMs adhere to ethical guidelines and responsible AI principles (Table 8), Claude-3.5-Sonnet achieves the highest score (67.67), demonstrating the strongest alignment with ethical standards. Gemini-1.5-Pro-Latest (66.33) and GLM-4v-Plus (64.03) also perform well, reflecting their reinforced alignment mechanisms. Discipline Breakdown: Claude-3.5-Sonnet attains the highest scores in Chemistry (73.04) and Earth and Space Sciences (74.46). Gemini-1.5-Pro-Latest leads in Life Sciences (66.07) and Earth and Space Sciences (75.04), indicating strong alignment across the natural sciences. DeepSeek-V3 (62.86) maintains a balanced performance across multiple disciplines. These results suggest that commercial models tend to achieve superior value alignment, likely due to reinforced instruction tuning and safety fine-tuning techniques.

### 5 Conclusion

This study introduced SciHorizon, a comprehensive assessment framework for AI4Science readiness, integrating assessments of AI-ready scientific datasets and LLM capabilities. The framework systematically evaluated scientific datasets across four key dimensions to identify high-quality data for AI-driven research while assessing LLMs across five core indicators spanning major scientific disciplines. Based on data papers from 2018 to 2023, we provided dataset recommendations for Earth and Life Sciences. Meanwhile, by benchmarking more than 20 representative large models, we gained critical insights into their strengths and limitations. SciHorizon establishes a structured methodology for dataset curation and model assessment, contributing to AI-driven scientific discovery.

### References

- [1] Jumper, J., Evans, R., Pritzel, A., Green, T., Figurnov, M., Ronneberger, O., Tunyasuvunakool, K., Bates, R., Zı´dek, A., Potapenko, A.,ˇ et al.: Highly accurate protein structure prediction with alphafold. nature 596(7873), 583–589 (2021)
- [2] Hassani, H., Silva, E.S.: The role of chatgpt in data science: how ai-assisted conversational interfaces are revolutionizing the field. Big data and cognitive computing 7(2), 62 (2023)


- [3] Morgan, D.L.: Exploring the use of artificial intelligence for qualitative data analysis: The case of chatgpt. International journal of qualitative methods 22, 16094069231211248 (2023)
- [4] Temsah, O., Khan, S.A., Chaiah, Y., Senjab, A., Alhasan, K., Jamal, A., Aljamaan, F., Malki, K.H., Halwani, R., Al-Tawfiq, J.A., et al.: Overview of early chatgpt’s presence in medical literature: insights from a hybrid literature review by chatgpt and human experts. Cureus 15(4) (2023)
- [5] Zhou, Y., Liu, H., Srivastava, T., Mei, H., Tan, C.: Hypothesis generation with large language models. arXiv preprint arXiv:2404.04326 (2024)
- [6] Park, Y.J., Kaplan, D., Ren, Z., Hsu, C.-W., Li, C., Xu, H., Li, S., Li, J.: Can chatgpt be used to generate scientific hypotheses? Journal of Materiomics 10(3), 578–584 (2024)
- [7] Frieder, S., Pinchetti, L., Griffiths, R.-R., Salvatori, T., Lukasiewicz, T., Petersen, P., Berner, J.: Mathematical capabilities of chatgpt. Advances in neural information processing systems 36, 27699–27744 (2023)
- [8] Guo, T., Nan, B., Liang, Z., Guo, Z., Chawla, N., Wiest, O., Zhang, X., et al.: What can large language models do in chemistry? a comprehensive benchmark on eight tasks. Advances in Neural Information Processing Systems 36, 59662– 59688 (2023)
- [9] Schelter, S., Lange, D., Schmidt, P., Celikel, M., Biessmann, F., Grafberger, A.: Automating large-scale data quality verification. Proceedings of the VLDB Endowment 11(12), 1781–1794 (2018)
- [10] Houston, L., Probst, Y., Martin, A.: Assessing data quality and the variability of source data verification auditing methods in clinical research settings. Journal of biomedical informatics 83, 25–32 (2018)
- [11] Shi, P., Cui, Y., Xu, K., Zhang, M., Ding, L.: Data consistency theory and case study for scientific big data. Information 10(4), 137 (2019)
- [12] Li, P., Rao, X., Blase, J., Zhang, Y., Chu, X., Zhang, C.: Cleanml: A study for evaluating the impact of data cleaning on ml classification tasks. In: 2021 IEEE 37th International Conference on Data Engineering (ICDE), pp. 13–24 (2021). IEEE
- [13] Clarke, D.J., Wang, L., Jones, A., Wojciechowicz, M.L., Torre, D., Jagodnik, K.M., Jenkins, S.L., McQuilton, P., Flamholz, Z., Silverstein, M.C., et al.: Fairshake: Toolkit to evaluate the fairness of research digital resources. Cell systems 9(5), 417–421 (2019)
- [14] Holland, S., Hosny, A., Newman, S., Joseph, J., Chmielinski, K.: The dataset


- nutrition label. Data Protection and Privacy 12(12), 1 (2020)
- [15] Arca, S., Hewett, R.: Is entropy enough for measuring privacy? In: 2020 International Conference on Computational Science and Computational Intelligence (CSCI), pp. 1335–1340 (2020). IEEE
- [16] Carlini, N., Jagielski, M., Zhang, C., Papernot, N., Terzis, A., Tramer, F.: The privacy onion effect: Memorization is relative. Advances in Neural Information Processing Systems 35, 13263–13276 (2022)
- [17] Chang, Y., Wang, X., Wang, J., Wu, Y., Yang, L., Zhu, K., Chen, H., Yi, X., Wang, C., Wang, Y., et al.: A survey on evaluation of large language models. ACM Transactions on Intelligent Systems and Technology 15(3), 1–45 (2024)
- [18] Cobbe, K., Kosaraju, V., Bavarian, M., Chen, M., Jun, H., Kaiser, L., Plappert, M., Tworek, J., Hilton, J., Nakano, R., et al.: Training verifiers to solve math word problems. arXiv preprint arXiv:2110.14168 (2021)
- [19] Singhal, K., Azizi, S., Tu, T., Mahdavi, S.S., Wei, J., Chung, H.W., Scales, N., Tanwani, A., Cole-Lewis, H., Pfohl, S., et al.: Large language models encode clinical knowledge. Nature 620(7972), 172–180 (2023)
- [20] Arora, D., Singh, H., Mausam: Have LLMs advanced enough? a challenging problem solving benchmark for large language models. In: Bouamor, H., Pino, J., Bali, K. (eds.) Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, pp. 7527–7543. Association for Computational Linguistics, Singapore (2023). https://doi.org/10.18653/v1/2023.emnlp-main. 468 . https://aclanthology.org/2023.emnlp-main.468
- [21] Wang, X., Hu, Z., Lu, P., Zhu, Y., Zhang, J., Subramaniam, S., Loomba, A.R., Zhang, S., Sun, Y., Wang, W.: Scibench: Evaluating college-level scientific problem-solving abilities of large language models. arXiv preprint arXiv:2307.10635 (2023)
- [22] scihorizon: SciHorizon Platform Officially Launched, Establishing a New Evaluation System for AI4Science! https://mp.weixin.qq. com/s? biz=MzkxODEzMDIwNA==&mid=2247525809&idx=1&sn= 8afb93c62f6dda04908ffc7391f32e20 (2025)

- [23] Hiniduma, K., Byna, S., Bez, J.L.: Data Readiness for AI: A 360-Degree Survey

(2024). https://arxiv.org/abs/2404.05779

- [24] Hiniduma, K., Byna, S., Bez, J.L., Madduri, R.: Ai data readiness inspector (aidrin) for quantitative assessment of data readiness for ai. In: Proceedings of the 36th International Conference on Scientific and Statistical Database Management. SSDBM ’24. Association for Computing Machinery, New York, NY, USA (2024). https://doi.org/10.1145/3676288.3676296 .


- https://doi.org/10.1145/3676288.3676296
- [25] Wilkinson, M., Dumontier, M., Aalbersberg, I.J., Appleton, G., Axton, M., Baak, A., Blomberg, N., Boiten, J.-W., Silva Santos, L.O., Bourne, P., Bouwman, J., Brookes, A., Clark, T., Crosas, M., Dillo, I., Dumon, O., Edmunds, S., Evelo, C., Finkers, R., Mons, B.: The fair guiding principles for scientific data management and stewardship. Scientific Data 3 (2016) https://doi.org/10.1038/ sdata.2016.18
- [26] Huerta, E., Blaiszik, B., Brinson, L., Bouchard, K., Diaz, D., Doglioni, C., Duarte, J., Emani, M., Foster, I., Fox, G., Harris, P., Heinrich, L., Jha, S., Katz, D., Kindratenko, V., Kirkpatrick, C., Lassila-Perini, K., Madduri, R., Neubauer, M., Zhu, R.: Fair for ai: An interdisciplinary and international community building perspective. Scientific Data 10 (2023) https://doi.org/10.1038/ s41597-023-02298-6
- [27] Khan, F., Wang, R., Skanderson, M., Brandt, C., Fodeh, S., Womack, J.: A roadmap to artificial intelligence (ai): Methods for designing and building ai ready data for womens health studies. medRxiv : the preprint server for health sciences (2023) https://doi.org/10.1101/2023.05.25.23290399
- [28] Cluster, E.D.R.: Checklist to Examine AI-readiness for Open Environmental Datasets (2022) https://doi.org/10.6084/m9.figshare.19983722.v1
- [29] Clark, T., Caufield, H., Mohan, J.A., Al Manir, S., Amorim, E., Eddy, J., Gim, N., Gow, B., Goar, W., Haendel, M., Hansen, J.N., Harris, N., Hermjakob, H., Joachimiak, M., Jordan, G., Lee, I.-H., McWeeney, S.K., Nebeker, C., Nikolov, M., Shaffer, J., Sheffield, N., Sheynkman, G., Stevenson, J., Chen, J.Y., Mungall, C., Wagner, A., Kong, S.W., Ghosh, S.S., Patel, B., Williams, A., Munoz-Torres, M.C.: Ai-readiness for biomedical data: Bridge2ai recommendations. bioRxiv (2024) https://doi.org/10.1101/2024.10.23.619844 https://www.biorxiv.org/content/early/2024/10/25/2024.10.23.619844.full.pdf
- [30] Hendrycks, D., Burns, C., Basart, S., Zou, A., Mazeika, M., Song, D., Steinhardt, J.: Measuring massive multitask language understanding. In: International Conference on Learning Representations (2021). https://openreview.net/forum?id=d7KBjmI3GmQ
- [31] Chen, W., Yin, M., Ku, M., Lu, P., Wan, Y., Ma, X., Xu, J., Wang, X., Xia, T.: TheoremQA: A theorem-driven question answering dataset. In: Bouamor, H., Pino, J., Bali, K. (eds.) Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, pp. 7889–7901. Association for Computational Linguistics, Singapore (2023). https://doi.org/10.18653/v1/ 2023.emnlp-main.489 . https://aclanthology.org/2023.emnlp-main.489
- [32] Lu, P., Bansal, H., Xia, T., Liu, J., Li, C., Hajishirzi, H., Cheng,


H., Chang, K.-W., Galley, M., Gao, J.: Mathvista: Evaluating mathematical reasoning of foundation models in visual contexts. In: The Twelfth International Conference on Learning Representations (2024).

https://openreview.net/forum?id=KUNzEQMWU7

- [33] Lu, P., Mishra, S., Xia, T., Qiu, L., Chang, K.-W., Zhu, S.-C., Tafjord, O., Clark, P., Kalyan, A.: Learn to explain: Multimodal reasoning via thought chains for science question answering. Advances in Neural Information Processing Systems 35, 2507–2521 (2022)
- [34] Sun, L., Han, Y., Zhao, Z., Ma, D., Shen, Z., Chen, B., Chen, L., Yu, K.: Scieval: A multi-level large language model evaluation benchmark for scientific research. In: Proceedings of the AAAI Conference on Artificial Intelligence, vol. 38, pp. 19053–19061 (2024)
- [35] Zhong, W., Cui, R., Guo, Y., Liang, Y., Lu, S., Wang, Y., Saied, A., Chen, W., Duan, N.: AGIEval: A human-centric benchmark for evaluating foundation models. In: Duh, K., Gomez, H., Bethard, S. (eds.) Findings of the Association for Computational Linguistics: NAACL 2024, pp. 2299–2314. Association for Computational Linguistics, Mexico City, Mexico (2024). https://doi.org/10.18653/ v1/2024.findings-naacl.149 . https://aclanthology.org/2024.findings-naacl.149
- [36] authors, B.-b.: Beyond the imitation game: Quantifying and extrapolating the capabilities of language models. Transactions on Machine Learning Research

(2023)

- [37] Frieder, S., Pinchetti, L., Griffiths, R.-R., Salvatori, T., Lukasiewicz, T., Petersen, P., Berner, J.: Mathematical capabilities of chatgpt. Advances in neural information processing systems 36 (2024)
- [38] Wan, Y., Wang, W., Yang, Y., Yuan, Y., Huang, J.-t., He, P., Jiao, W., Lyu, M.: LogicAsker: Evaluating and improving the logical reasoning ability of large language models. In: Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing. Association for Computational Linguistics, Miami, Florida, USA (2024). https://aclanthology.org/2024.emnlp-main.128/
- [39] Zhang, D., Hu, Z., Zhoubian, S., Du, Z., Yang, K., Wang, Z., Yue, Y., Dong, Y., Tang, J.: SciGLM: Training Scientific Language Models with Self-Reflective Instruction Annotation and Tuning (2024)
- [40] Chau, M., Li, T.M., Wong, P.W., Xu, J.J., Yip, P.S., Chen, H.: Finding people with emotional distress in online social media: A design combining machine learning and rule-based classification. MIS quarterly 44(2) (2020)
- [41] Computer Network Information Center of the Chinese Academy of Sciences: Scientific Data Trusted Certification. Accessed: 2025-02-22 (2024). https:// datatrusted.cn/service/dataFair


- [42] Zhao, Y., Zhang, J., Chern, I., Gao, S., Liu, P., He, J., et al.: Felm: Benchmarking factuality evaluation of large language models. Advances in Neural Information Processing Systems 36 (2024)
- [43] Huang, Y., Bai, Y., Zhu, Z., Zhang, J., Zhang, J., Su, T., Liu, J., Lv, C., Zhang, Y., Fu, Y., et al.: C-eval: A multi-level multi-discipline chinese evaluation suite for foundation models. Advances in Neural Information Processing Systems 36, 62991–63010 (2023)
- [44] Wang, X., Chen, G., Dingjie, S., Zhiyi, Z., Chen, Z., Xiao, Q., Chen, J., Jiang, F., Li, J., Wan, X., Wang, B., Li, H.: CMB: A comprehensive medical benchmark in Chinese. In: Duh, K., Gomez, H., Bethard, S. (eds.) Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), pp. 6184–6205. Association for Computational Linguistics, Mexico City, Mexico (2024). https://doi.org/10.18653/v1/2024.naacl-long.343 . https://aclanthology.org/2024.naacl-long.343
- [45] Li, H., Zhang, Y., Koto, F., Yang, Y., Zhao, H., Gong, Y., Duan, N., Baldwin, T.: CMMLU: Measuring massive multitask language understanding in Chinese. In: Ku, L.-W., Martins, A., Srikumar, V. (eds.) Findings of the Association for Computational Linguistics ACL 2024, pp. 11260–11285. Association for Computational Linguistics, Bangkok, Thailand and virtual meeting (2024). https://aclanthology.org/2024.findings-acl.671
- [46] Gu, Z., Zhu, X., Ye, H., Zhang, L., Wang, J., Zhu, Y., Jiang, S., Xiong, Z., Li, Z., Wu, W., et al.: Xiezhi: An ever-updating benchmark for holistic domain knowledge evaluation. In: Proceedings of the AAAI Conference on Artificial Intelligence, vol. 38, pp. 18099–18107 (2024)
- [47] Zhang, Y., Wang, Z., He, Z., Li, J., Mai, G., Lin, J., Wei, C., Yu, W.: Bb-geogpt: A framework for learning a large language model for geographic information science. Information Processing & Management 61(5), 103808 (2024)
- [48] Darwich, O., Rimlinger, H., Dreyfus, M., Gouel, M., Vermeulen, K.: Replication: Towards a publicly available internet scale ip geolocation dataset. In: Proceedings of the 2023 ACM on Internet Measurement Conference, pp. 1–15

(2023)

- [49] Dalal, D., Valentino, M., Freitas, A., Buitelaar, P.: Inference to the best explanation in large language models. In: Ku, L.-W., Martins, A., Srikumar, V. (eds.) Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 217–235. Association for Computational Linguistics, Bangkok, Thailand (2024). https://aclanthology.org/2024.acllong.14
- [50] Chen, L., Deng, Y., Bian, Y., Qin, Z., Wu, B., Chua, T.-S., Wong, K.-F.: Beyond


- factuality: A comprehensive evaluation of large language models as knowledge generators. In: Bouamor, H., Pino, J., Bali, K. (eds.) Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, pp. 6325– 6341. Association for Computational Linguistics, Singapore (2023). https://doi. org/10.18653/v1/2023.emnlp-main.390 . https://aclanthology.org/2023.emnlpmain.390
- [51] Black, S., Gao, L., Wang, P., Leahy, C., Biderman, S.: GPT-Neo: Large Scale Autoregressive Language Modeling with Mesh-Tensorflow (2021) https://doi. org/10.5281/zenodo.5297715 . If you use this software, please cite it using these metadata.
- [52] Touvron, H., Lavril, T., Izacard, G., Martinet, X., Lachaux, M.-A., Lacroix, T., Rozi`ere, B., Goyal, N., Hambro, E., Azhar, F., et al.: Llama: Open and efficient foundation language models. arXiv preprint arXiv:2302.13971 (2023)
- [53] Pal, A., Umapathi, L.K., Sankarasubbu, M.: Medmcqa: A large-scale multisubject multi-choice dataset for medical domain question answering. In: Conference on Health, Inference, and Learning, pp. 248–260 (2022). PMLR
- [54] Jin, D., Pan, E., Oufattole, N., Weng, W.-H., Fang, H., Szolovits, P.: What disease does this patient have? a large-scale open domain question answering dataset from medical exams. Applied Sciences 11(14), 6421 (2021)
- [55] Levine, D.M., Tuwani, R., Kompa, B., Varma, A., Finlayson, S.G., Mehrotra, A., Beam, A.: The diagnostic and triage accuracy of the gpt-3 artificial intelligence model. MedRxiv (2023)
- [56] Edwards, C., Zhai, C., Ji, H.: Text2Mol: Cross-modal molecule retrieval with natural language queries. In: Moens, M.-F., Huang, X., Specia, L., Yih, S.W.t. (eds.) Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing, pp. 595–607. Association for Computational Linguistics, Online and Punta Cana, Dominican Republic (2021). https://doi.org/10.18653/ v1/2021.emnlp-main.47 . https://aclanthology.org/2021.emnlp-main.47
- [57] Lacoste, A., Lehmann, N., Rodriguez, P., Sherwin, E., Kerner, H., Lu¨tjens, B., Irvin, J., Dao, D., Alemohammad, H., Drouin, A., et al.: Geo-bench: Toward foundation models for earth monitoring. Advances in Neural Information Processing Systems 36, 51080–51093 (2023)
- [58] Liu, H., Zheng, Z., Qiao, Y., Duan, H., Fei, Z., Zhou, F., Zhang, W., Zhang, S., Lin, D., Chen, K.: MathBench: Evaluating the theory and application proficiency of LLMs with a hierarchical mathematics benchmark. In: Ku, L.-W., Martins, A., Srikumar, V. (eds.) Findings of the Association for Computational Linguistics ACL 2024, pp. 6884–6915. Association for Computational Linguistics, Bangkok, Thailand and virtual meeting (2024). https://aclanthology.org/2024.findingsacl.411


- [59] Rein, D., Hou, B.L., Stickland, A.C., Petty, J., Pang, R.Y., Dirani, J., Michael, J., Bowman, S.R.: GPQA: A graduate-level google-proof q&a benchmark. In: First Conference on Language Modeling (2024). https://openreview.net/forum?id=Ti67584b98
- [60] Ling, W., Yogatama, D., Dyer, C., Blunsom, P.: Program induction by rationale generation: Learning to solve and explain algebraic word problems. In: Barzilay, R., Kan, M.-Y. (eds.) Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 158–167. Association for Computational Linguistics, Vancouver, Canada (2017). https://doi.org/10.18653/v1/P17-1015 . https://aclanthology.org/P17-1015
- [61] Amini, A., Gabriel, S., Lin, S., Koncel-Kedziorski, R., Choi, Y., Hajishirzi, H.: MathQA: Towards interpretable math word problem solving with operationbased formalisms. In: Burstein, J., Doran, C., Solorio, T. (eds.) Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers), pp. 2357–2367. Association for Computational Linguistics, Minneapolis, Minnesota (2019). https://doi.org/10.18653/v1/N19-1245 . https://aclanthology.org/N19-1245
- [62] Yingying, C., Kun, Y., Wenjun, T., Xin, L., Hui, L., Jie, H., Jun, Q.: China meteorological forcing dataset (1979-2018). National Tibetan Plateau Data Center

(2015) https://doi.org/10.11888/AtmosphericPhysics.tpe.249369.file

- [63] Xu, Z., Han, Y., Tam, C.-Y., Yang, Z.-L., Fu, C.: Bias-corrected CMIP6 Global Dataset for Dynamical Downscaling of the Earth’s Historical and Future Climate (1979–2100). Science Data Bank (2024). https://doi.org/10.11922/sciencedb. 00487 . https://doi.org/10.11922/sciencedb.00487
- [64] Yang, J., Huang, X.: 30 m annual land cover and its dynamics in china from 1990 to 2019 (2021) https://doi.org/10.5281/zenodo.4417810
- [65] Li, X., Ran, Y., Hori, M., Aalto, J., Karjalainen, O., Hjort, J., Luoto, M., Obu, J., Cheng, G., Che, J., Jin, H., Yu, Q., Chang, X.: High-resolution datasets of permafrost thermal state and hydrothermal zonation in the northern hemisphere. National Tibetan Plateau Data Center (2021) https://doi.org/10.11888/ Geocry.tpdc.271190
- [66] Hu, G., Li, R., Wu, T., Xiao, Y., Qiao, Y., Xing, Z., Zhao, Y., Shi, J., Pang, Q., Wang, L., Xie, C., Wang, C., Cheng, G., Sun, Z., Zou, D., Zhao, L., Liu, G., Du, E., Wu, X.: A synthesis dataset of permafrost for the qinghai-xizang (tibet) plateau, china (2002-2018). National Tibetan Plateau Data Center (2021) https://doi.org/10.11888/Geocry.tpdc.271107
- [67] Liu, L., Zhang, X., Chen, X., Gao, Y., Mi, J.: Glc fcs30: Global land-cover product with fine classification system at 30 m using time-series landsat imagery


- (2020) https://doi.org/10.5281/zenodo.3986872
- [68] Zhao, M., Cheng, C., Zhou, Y., Li, X., Shen, S., Song, C.: A global dataset of annual urban extents (1992-2020) from harmonized nighttime lights (2021) https://doi.org/10.6084/m9.figshare.16602224.v1
- [69] Smart City Sensing, N.N.U.L., Simulation: Vectorized rooftop area data for 90 cities in china (2020). National Tibetan Plateau Data Center (2021) https:// doi.org/10.11888/Geogra.tpdc.271702
- [70] Cheng, W., Li, D., Deng, X., Feng, J., Wang, Y., Peng, J., Tian, J., Qi, W., Liu, Z., Zheng, X., Zhou, D., Jiang, S., Zhao, H., Wang, X.: Global monthly distributions of atmospheric co2 concentrations under the historical and future scenarios (2021) https://doi.org/10.5281/zenodo.5021361
- [71] Yan, F., Shangguan, W., Zhang, J., Hu, B.: Depth-to-bedrock map of china at a spatial resolution of 100 meters (2019) https://doi.org/10.6084/m9.figshare.c. 4714514.v1
- [72] Yang, J., Shi, R., Wei, D., Liu, Z., Zhao, L., Ke, B., Pfister, H., Ni, B.: Medmnist v2: A large-scale lightweight benchmark for 2d and 3d biomedical image classification (2021)
- [73] Zhang, Y., Chen, Q., Yang, Z., Lin, H., Lu, Z.: Biowordvec: Improving biomedical word embeddings with subword information and mesh ontology (2018) https: //doi.org/10.6084/m9.figshare.6882647.v2
- [74] Zhang, G., Zheng, D., Tian, Y., Li, S.: A dataset of distribution and diversity of ticks in china (2019)
- [75] Yuan, J., Deng, L., Tang, X., Huang, H., Deng, Y.: The sustech-sysu dataset for automatically segmenting and classifying corneal ulcers (2020) https://doi.org/ 10.6084/m9.figshare.c.4526675.v1
- [76] Jin, K., Huang, X., Zhou, J., Li, Y., Yan, Y., Sun, Y., Zhang, Q., Wang, Y., Ye, J.: Fives: A fundus image dataset for ai-based vessel segmentation (2022) https://doi.org/10.6084/m9.figshare.19688169.v1
- [77] Hong Kong, T.C.U.: mirtarbase: The experimentally validated microrna-target interactions database (2021)
- [78] Hu, B.: A multi-modal open dataset for mental-disorder analysis (2022) https: //doi.org/10.5255/UKDA-SN-854301
- [79] Liu, C., Wang, M., Wei, X., Liu, L.: An atac-seq atlas of chromatin accessibility in mouse tissues (2018) https://doi.org/10.26036/CNP0000198
- [80] Liao, J., Yu, Z., Chen, Y., Zou, C., Zhang, H., Cheng, J., Liu, D., Li, T., Zhang,


- Q., Mo, Z.: Single-cell rna sequencing of human kidney (2019)
- [81] OpenAI: Hello GPT-4o. Accessed: 2024-09-23 (2024). https://openai.com/ index/hello-gpt-4o/
- [82] Jaech, A., Kalai, A., Lerer, A., Richardson, A., El-Kishky, A., Low, A., Helyar, A., Madry, A., Beutel, A., Carney, A., et al.: Openai o1 system card. arXiv preprint arXiv:2412.16720 (2024)
- [83] Baidu: Ernie-4.0-turbo. https://cloud.baidu.com/doc/WENXINWORKSHOP/ s/7lxwwtafj. Accessed: 2024-12-10 (2024)
- [84] Anthropic: Claude-3.5-Sonnet. https://www.anthropic.com/news/ claude-3-5-sonnet. Accessed: 2024-10-22 (2024)
- [85] ByteDance: Doubao-Pro-32K. https://www.volcengine.com/product/doubao

(2024)

- [86] DeepMind, G.: Gemini-1.5-Pro-Latest. https://deepmind.google/technologies/ gemini/pro/ (2024)
- [87] AI, Z.: GLM-4-Plus. https://bigmodel.cn/dev/howuse/glm-4 (2024)
- [88] AI, Z.: GLM-4v-Plus. https://bigmodel.cn/dev/howuse/glm-4v (2024)
- [89] AI, M.: Moonshot-V1-32K. https://platform.moonshot.cn/docs/intro (2024)
- [90] Alibaba: Qwen-Plus. https://agicto.com/model/qwen-plus (2024)
- [91] 01.AI: Yi-Lightning. https://platform.lingyiwanwu.com/ (2024)
- [92] 01.AI: Yi-Vision-V2. https://platform.lingyiwanwu.com/ (2024)
- [93] DeepSeek: DeepSeek-V3. https://www.deepseek.com/ (2024)
- [94] AI, Z.: GLM-4-9B-Chat. https://github.com/THUDM/GLM-4 (2024)
- [95] Lab, S.A.: InternLM2.5-20B-Chat. https://internlm.intern-ai.org.cn/ (2024)
- [96] Lab, S.A.: InternLM3-8B-Instruct. https://internlm-chat.intern-ai.org.cn/

(2024)

- [97] AI, M.: Llama3.1-8B-Instruct. https://www.llama.com/docs/

- model-cards-and-prompt-formats/llama3 1 (2024)

[98] AI, M.: Llama-3.2-11B-Vision-Instruct. https://www.llama.com/docs/

- model-cards-and-prompt-formats/llama3 2 (2024)


- [99] AI, M.: Llama3.1-70B-Instruct. https://www.llama.com/docs/


###### model-cards-and-prompt-formats/llama3 1 (2024)

- [100] AI, M.: Llama-3.2-90B-Vision-Instruct. https://www.llama.com/docs/

model-cards-and-prompt-formats/llama3 2 (2024)

- [101] MBZUAI: MiniCPM3-4B. https://github.com/OpenBMB/MiniCPM?tab= readme-ov-file (2024)
- [102] MBZUAI: MiniCPM-V-2.6. https://github.com/OpenBMB/MiniCPM-o

(2024)

- [103] AI, M.: Mistral-8B-Instruct-2410. https://docs.mistral.ai/getting-started/ models/models overview/ (2024)

- [104] AI, M.: Mistral-Large-Instruct-2411. https://docs.mistral.ai/getting-started/ models/models overview/ (2024)

- [105] AI, M.: Pixtral-Large-Instruct-2411. https://mistral.ai/news/pixtral-large/

(2024)

- [106] Alibaba: Qwen2.5-72B-Instruct. https://github.com/QwenLM/Qwen2.5 (2024)
- [107] Alibaba: Qwen2.5-7B-Instruct. https://github.com/QwenLM/Qwen2.5 (2024)
- [108] Alibaba: Qwen2-VL-7B-Instruct. https://github.com/QwenLM/Qwen2-VL

(2024)

- [109] 01.AI: Yi-34B-Chat. https://huggingface.co/01-ai/Yi-34B-Chat (2024)


