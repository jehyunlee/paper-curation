# arXiv:2502.05151v3[cs.CL]5 Mar 2026

## Transforming Science with Large Language Models: A Survey on AI-assisted Scientific Discovery, Experimentation, Content Generation, and Evaluation

STEFFEN EGER, University of Technology Nuremberg (UTN), Germany YONG CAO, University of Tübingen, Tübingen AI Center, Germany JENNIFER D’SOUZA, TIB Leibniz Information Centre for Science and Technology, Germany ANDREAS GEIGER, University of Tübingen, Tübingen AI Center, Germany CHRISTIAN GREISINGER, University of Technology Nuremberg (UTN), Germany STEPHANIE GROSS, Austrian Research Institute for Artificial Intelligence, Austria YUFANG HOU, IT:U Interdisciplinary Transformation University Austria, Austria BRIGITTE KRENN, Austrian Research Institute for Artificial Intelligence, Austria ANNE LAUSCHER, University of Hamburg, Germany YIZHI LI, University of Manchester, United Kingdom CHENGHUA LIN, University of Manchester, United Kingdom NAFISE SADAT MOOSAVI, University of Sheffield, United Kingdom WEI ZHAO, University of Aberdeen, United Kingdom TRISTAN MILLER, University of Manitoba, Canada

With the advent of large multimodal language models, science is now at a threshold of an AI-based technological transformation. An emerging ecosystem of models and tools aims to support researchers throughout the scientific lifecycle, including (1) searching for relevant literature, (2) generating research ideas and conducting experiments, (3) producing text-based content, (4) creating multimodal artifacts such as figures and diagrams, and (5) evaluating scientific work, as in peer review. In this survey, we provide a curated overview of literature representative of the core techniques, evaluation practices, and emerging trends in AI-assisted scientific discovery. Across the five tasks outlined above, we discuss datasets, methods, results, evaluation strategies, limitations, and ethical concerns, including risks to research integrity through the misuse of generative models. We aim for this survey to serve both as an

Authors’ Contact Information: Steffen Eger, steffen.eger@utn.de, University of Technology Nuremberg (UTN), Nuremberg, Germany; Yong Cao, yong.cao@uni-tuebingen.de, University of Tübingen, Tübingen AI Center, Tübingen, Germany; Jennifer D’Souza, jennifer.dsouza@tib.eu, TIB Leibniz Information Centre for Science and Technology, Hannover, Germany; Andreas Geiger, a.geiger@uni-tuebingen.de, University of Tübingen, Tübingen AI Center, Tübingen, Germany; Christian Greisinger, christian.greisinger@utn.de, University of Technology Nuremberg (UTN), Nuremberg, Germany; Stephanie Gross, stephanie.gross@ofai.at, Austrian Research Institute for Artificial Intelligence, Vienna, Austria; Yufang Hou, yufang.hou@it-u.at, IT:U Interdisciplinary Transformation University Austria, Linz, Austria; Brigitte Krenn, brigitte.krenn@ofai.at, Austrian Research Institute for Artificial Intelligence, Vienna, Austria; Anne Lauscher, anne.lauscher@uni-hamburg.de, University of Hamburg, Hamburg, Germany; Yizhi Li, yizhi.li-2@ manchester.ac.uk, University of Manchester, Manchester, United Kingdom; Chenghua Lin, chenghua.lin@manchester.ac.uk, University of Manchester, Manchester, United Kingdom; Nafise Sadat Moosavi, n.s.moosavi@sheffield.ac.uk, University of Sheffield, Sheffield, United Kingdom; Wei Zhao, wei. zhao@abdn.ac.uk, University of Aberdeen, Aberdeen, United Kingdom; Tristan Miller, Tristan.Miller@umanitoba.ca, University of Manitoba, Winnipeg, Manitoba, Canada.

Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for third-party components of this work must be honored. For all other uses, contact the owner/author(s).

© 2026 Copyright held by the owner/author(s). Manuscript submitted to ACM

Manuscript submitted to ACM 1

accessible, structured orientation for newcomers to the field, as well as a catalyst for new AI-based initiatives and their integration into future “AI4Science” systems.

CCS Concepts: • Social and professional topics → Assistive technologies; • Applied computing → Physical sciences and engineering; Life and medical sciences; Law, social and behavioral sciences; • Computing methodologies → Natural language processing; Artificial intelligence; • General and reference → Surveys and overviews.

Additional Key Words and Phrases: Language Language Models, Science, AI4Science, Search, Experimentation, Idea Generation, Multimodal Content Generation, Evaluation, Peer Review

##### ACM Reference Format:

Steffen Eger, Yong Cao, Jennifer D’Souza, Andreas Geiger, Christian Greisinger, Stephanie Gross, Yufang Hou, Brigitte Krenn, Anne Lauscher, Yizhi Li, Chenghua Lin, Nafise Sadat Moosavi, Wei Zhao, and Tristan Miller. 2026. Transforming Science with Large Language Models: A Survey on AI-assisted Scientific Discovery, Experimentation, Content Generation, and Evaluation. 1, 1 (March 2026), 46 pages. https://doi.org/XXXXXXX.XXXXXXX

### 1 Introduction

Throughout history, science has undergone a number of paradigm shifts, culminating in today’s era of data-intensive exploration [104]. Although new tools and frameworks have accelerated the pace of scientific discovery, its basic steps have remained unchanged for centuries. These include (1) conception of a research question or problem, typically arising from a gap in disseminated knowledge; (2) collection and study of existing literature or data relevant to the problem; (3) formulation of a falsifiable hypothesis; (4) design and execution of experiments to test this hypothesis; (5) analysis and interpretation of the resulting data; and (6) reporting on the findings, allowing for their exploitation in real-world applications or as a source of knowledge for a further iteration of the scientific cycle.

The advent of large multimodal foundation models, such as ChatGPT, Gemini, Qwen, and DeepSeek, is profoundly affecting many sectors of society, including scientific research. Empirical evidence suggests that this influence extends well beyond computer science: an analysis of approximately 148,000 papers from 22 non-CS disciplines has revealed a rapid increase in citations of large language models (LLMs) between 2018 and 2024 [202]. In parallel, a large global survey of researchers conducted by Wiley reported widespread expectations that use of AI will become mainstream in scientific practice in the next two years, despite its current use being often limited to writing assistance.1

While science has traditionally relied on human ingenuity and labor for generating research ideas, formulating hypotheses, searching for relevant literature, conducting experiments, and reporting results, recent AI systems have been promising support at every stage of this cycle. Examples include Elicit and ORKG ASK for literature search, The AI Scientist [177] for experimentation, and AutomaTikZ [20] and DeTikZify [21] for multimodal content generation. There is moreover growing interest in the use of AI for evaluating scientific outputs through automated peer review [300]. Collectively, these advancements suggest the emergence of an integrated AI-assisted research workflow with the potential to accelerate discovery and streamline the documentation and communication of results.2 The consolidation of a research community around AI-assisted science is evidenced by the establishment in 2024 and 2025 of dedicated venues such as the workshops on Natural Scientific Language Processing and Research Knowledge Graphs (NSLP) [216], Foundation Models for Science (FM4Science), AI & Scientific Discovery (AISD), Towards a Knowledge-grounded

- 1https://www.wiley.com/en-us/ai-study, https://www.nature.com/articles/d41586-025-00343-5
- 2The benefits could be particularly significant for non-native speakers of English and those with lower technical skills, potentially increasing diversity and inclusivity in research.


Scientific Research Lifecycle (AI4Research), AI Agents for Science (Agents4Science), and Human–LLM Collaboration for Ethical and Responsible Science Production (SciProdLLM) [310].

Despite the rapid progress in this area, existing surveys typically focus on specific domains, such as applications in the social sciences or physics [e.g., 287, 307], or on a relatively narrow set of research tasks and ethical concerns [e.g., 99, 179, 308]. To address this gap, the present survey adopts a workflow-centric perspective, providing a broad, crosscutting overview of five central aspects of AI support for the research cycle: (1) literature search and summarization (§3.1); (2) scientific experimentation and research idea generation (§3.2); (3) unimodal generation and refinement of textual content, including titles, abstracts, and citations (§3.3); (4) multimodal content generation and interpretation, including figures, tables, slides, and posters (§3.4); and (5) AI-assisted peer review (§3.5). Rather than aiming for comprehensive coverage within each area, we focus on representative approaches that capture core methodological ideas and allow meaningful comparison across tasks.

Ethical considerations are paramount in any discussion of AI in science. Current tools exhibit a number of problems and limitations, including “hallucination”, bias, limited reasoning abilities, and substantial environmental costs, and mechanisms for evaluating their output remain underdeveloped. Broader concerns include the risks of “fake science”, plagiarism, and erosion of research integrity through diminished human oversight. Recent policy guidance on the use of AI in science, such as that of the EU,3 emphasizes both the transformative potential of these technologies and the risks they pose if deployed without appropriate safeguards. In this survey, these ethical considerations are addressed alongside our treatment of the appertaining research tasks, as well as in a dedicated discussion in §4.

- As illustrated in Fig. 1, the remainder of this paper is structured as follows. In §2 we discuss the scope and method-

ological approach of our survey. The subsections of §3 review representative literature for individual tasks in the research lifecycle, presenting datasets, methods, evaluation practices, limitations and future directions, and connections across tasks. In §4 we address broader ethical and integrity concerns. In §5 we conclude with a synthesis of opportunities and challenges for AI-assisted scientific research. The paper’s appendix includes background material on the scientific discovery cycle, further elaboration on AI support for specific topics and tasks, and a list of abbreviations.

- At https://github.com/NL2G/TransformingScienceLLMs we maintain a periodically updated list of further resources relating to this survey.


### 2 Survey Scope and Methodology

This survey provides a broad, workflow-centric overview of AI methods and applications that support scientific research across the full research lifecycle. It is intended primarily for researchers in AI-related fields (e.g., natural language processing, computer vision, and machine learning) seeking a structured orientation to this rapidly evolving area, with clear entry points for deeper exploration. Some of the material will also be useful to policymakers, practitioners, and research collaborators in adjacent fields, including human–computer interaction, library and information science, communication studies, metascience, science journalism, and research ethics.

Given our topic’s wide scope, rapid progress, and dependence on knowledge and methods from different domains, we adopt a narrative rather than a systematic survey methodology. This approach is particularly well suited to synthesizing heterogeneous and evolving bodies of work, enabling connections to be drawn across domains and methodological traditions [28, 132, 197]. Rather than imposing rigid inclusion and exclusion criteria, the narrative approach allows the survey to emphasize conceptual coherence, methodological representativeness, and comparability across tasks. At the

###### 3 https://research-and-innovation.ec.europa.eu/document/download/2b6cf7e5-36ac-41cb-aab5-0d32050143dc_en?filename=ec_rtd_ai-guidelines.pdf

Research Question / Topic

Literature Seach (§3.1) Idea & Hypothesis Generation (§3.2) Auto Experimentation (§3.2)

- • Semantic Search & Paper Chat
- • Summarization & Personalization
- • Graph-based Analysis


- • Research Ideation
- • Hypothesis Generation
- • Iteration & Human Alignment


- • Experiment planning
- • Code & pipeline generation
- • Automated benchmarking


Mature tools and diverse function. Data quality and coverage gaps;

High novelty but low feasibility. Limited diversity and self-

Early-stage and lacks reliability. Often critical errors; hard to

![image 1](Eger et al._2025_Transforming Science with Large Language Models A Survey on AI-assisted Scientific Discovery, Exper_images/imageFile1.png)

![image 2](Eger et al._2025_Transforming Science with Large Language Models A Survey on AI-assisted Scientific Discovery, Exper_images/imageFile2.png)

![image 3](Eger et al._2025_Transforming Science with Large Language Models A Survey on AI-assisted Scientific Discovery, Exper_images/imageFile3.png)

bias; scalability; interdisciplinary collaboration.

evaluation failures; overly general and unvalidated ideas.

intergrate multi-modalities; struggle to identify flaws.

Ethical Concerns (§4)

| | |
|---|---|
| | |


Evaluation & Peer Review (§3.5) Multimodal Generation (§3.4) Text-based Generation (§3.3)

- • Title, Abstract, Long-text
- • Citation, Related Work
- • Proofreading, Paraphrasing & Style Transfer


- • Figure & Table Understanding
- • Figure & Table Generation
- • Scientific Slides & Poster Generation


- • Automated Review & Feedback Generation
- • Scientific Claim Verification
- • Meta-review & Review Analysis


High usability but concern on factuality.

Strong visual capabilities, but limited accuracy.

Promising for assistance, but unreliable as a standalone evaluator.

![image 4](Eger et al._2025_Transforming Science with Large Language Models A Survey on AI-assisted Scientific Discovery, Exper_images/imageFile4.png)

![image 5](Eger et al._2025_Transforming Science with Large Language Models A Survey on AI-assisted Scientific Discovery, Exper_images/imageFile5.png)

![image 6](Eger et al._2025_Transforming Science with Large Language Models A Survey on AI-assisted Scientific Discovery, Exper_images/imageFile6.png)

Factual consistency and truthfulness; ethichal issues such as authorship, plagiarism, etc.

Small dataset; weak performance; limited domains; struggle to evaluate performance.

Limited domains are studied; lack datasets; scientific rigor remains underexplored.

Paper Publication

Remaining Challenges: · Hallucination · Bias · Lack of reliable benchmarks · Human-in-the-loop · Evaluation gap · Ethical issues

Fig. 1. Overview of the AI-assisted scientific research workflow and remaining challenges, illustrating how AI support different stages of the research process. Each block summarizes the current status of AI capabilities ( ) and their limitations (▶) at that stage.

same time, it requires transparency about scope and limitations: the survey does not aim to be exhaustive, nor does it claim to capture every recent publication.

The papers and tools discussed in each subsection were selected by diverse co-author teams with domain expertise, using a common set of guiding principles. Initial pools of candidate works were typically assembled by combining (i) seed papers known to the co-authors for their technical depth or influence, expanded through forward and backward citation analysis, and (ii) targeted keyword searches in major scholarly databases such as Google Scholar. From these pools, works were selected on the basis of their relevance to the task under discussion, the maturity and clarity of their methodology, the reputation of the publication venue, and indicators of impact such as citation patterns relative to publication date. Preference was given to approaches that exemplify core techniques, employ well-defined evaluation protocols, or have served as reference points for subsequent work. This selection strategy was intended to foreground approaches that are representative of broader research trends, amenable to comparison, and likely to remain relevant at least in the near term, thereby supporting the survey’s integrative goals. Throughout §3, individual subsections use a common structure to highlight common evaluation dimensions, methodological trade-offs, and connections between tasks; this helps to situate individual contributions within a larger picture of AI-assisted scientific research and reduce any single-viewpoint bias inherent in our selection process.

3 AI Support for Individual Topics and Tasks 3.1 Literature Search, Summarization, and Comparison

The rapid growth of scientific literature presents a significant challenge for researchers to efficiently search, analyze, and summarize information. AI-powered tools are transforming these tasks by leveraging NLP, machine learning (ML), LLMs, citation and knowledge graphs (KGs) to automate the retrieval, extraction, and summarization of scientific information. This section surveys state-of-the-art AI-enhanced literature discovery tools, categorized according to their core functionality: (1) AI-enhanced search, which retrieves relevant literature from vast repositories; (2) graph-based systems, which map relationships between research concepts and publications; (3) paper chat and QA, which enable interactive exploration of scientific content; and (4) recommender systems, which suggest relevant papers based on user preferences. (We further discuss traditional search engines and benchmarks with leaderboards in Appendix B.1.)

- 3.1.1 Data. Scientific search engines rely on vast publisher databases to provide access to scientific literature. Understanding the classification of these repositories is essential for assessing search engines’ coverage, reliability, and effectiveness in evidence-based research. Repositories vary by access model, subject focus, and content type, each serving a distinct role in academic discovery and knowledge dissemination. By access model, repositories fall into open access repositories, which provide unrestricted access to research articles (e.g., PubMed Central, arXiv); subscription-based repositories, requiring institutional or individual subscriptions (e.g., ScienceDirect, SpringerLink); and hybrid repositories, offering both free and paywalled content (e.g., Taylor & Francis Online, Oxford Academic). By subject focus, repositories are either multidisciplinary, covering broad disciplines (e.g., Web of Science, Scopus), or subject-specific, specializing in fields such as medicine (PubMed), physics (INSPIRE-HEP), and social sciences (SSRN). By content type, institutional repositories archive research outputs from specific organizations (e.g., MIT DSpace, Harvard DASH); preprint repositories enable early dissemination of research before peer review (e.g., bioRxiv, chemRxiv); and government and public sector repositories provide access to publicly funded research (e.g., NASA ADS, OpenAIRE). Data repositories (e.g., Dryad, Zenodo) store research datasets, supporting transparency and reproducibility, while aggregator repositories (e.g., BASE, CORE) index content from multiple sources for broader searches. Lastly, grey literature repositories (e.g., OpenGrey, EThOS) provide access to non-traditional research outputs such as theses, reports, and white papers, which may not be available through conventional publisher platforms.

The structure of scientific repositories shapes AI-enhanced search. While broad AI-based search engines like Elicit and ORKG ASK query multiple publisher repositories, similar to Google Scholar, tools like NotebookLM focus on user-selected documents, and recommender systems such as Scholar Inbox rank new literature by relevance. AI-driven search enables customizable knowledge bases while optimizing discovery, retrieval, and personalization in research.

- 3.1.2 Methods and Results. Here, we discuss four types of state-of-the-art AI-enhanced search tools.


AI-enhanced Search. Platforms such as Elicit, Consensus, OpenScholar [9], and SciSpace leverage AI, including LLMs, to extend beyond traditional search by enabling semantic search, paper summarization, evidence synthesis, and trend analysis. Unlike conventional search engines that rely on keyword matching, these tools use NLP and machine learning to extract key insights, synthesize information to answer research queries [88], and generate structured summaries [102, 280, 309]. Their ability to quickly summarize and categorize findings—such as study outcomes, methodologies, and limitations—helps researchers efficiently compare and interpret literature.

Table 1. Overview of popular literature search, summarization, and comparison tools and their key features. ✓ indicates feature availability; empty cells indicate lack of features or publicly documented support.

Recommendations Collections Citation AnalysisTrending AnalysisAuthor Profiles Visualization Tools Paper Chat

Code RepositoriesLLM Integration Web API Personalization

Idea GenerationPaper WritingSummarizationPaper Review Datasets

Search

Cost Data Source

Platform

Elicit ✓ ✓ ✓ ✓ ✓ ✓ Freemium 125 million OpenScholar ✓ ✓ ✓ ✓ ✓ Free 45 million Undermind ✓ ✓ ✓ ✓ ✓ ✓ Premium over 200 million Perplexity ✓ ✓ ✓ ✓ ✓ ✓ Freemium Consensus ✓ ✓ ✓ ✓ ✓ ✓ Freemium over 200 million SciSpace ✓ ✓ ✓ ✓ ✓ ✓ ✓ Freemium scienceQA ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ Freemium 220 million PaperQA2 ✓ ✓ ✓ Free Paperguide ✓ ✓ ✓ ✓ ✓ ✓ ✓ Freemium HyperWrite ✓ ✓ ✓ ✓ ✓ ✓ ✓ Premium ResearchKick ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ Premium Bohrium ✓ ✓ ✓ ✓ ✓ Freemium 170 million Paperpal ✓ ✓ ✓ ✓ ✓ ✓ Freemium over 3 million Scholar Labs ✓ ✓ Freemium

AI-Enhanced Search

Connected Papers ✓ ✓ ✓ Freemium 214 million ScholarGPS ✓ ✓ ✓ ✓ ✓ Free over 200 million CiteSpace ✓ ✓ Freemium Sci2 ✓ Free NLP KG ✓ ✓ ✓ ✓ ✓ Free ORKG ASK ✓ ✓ ✓ ✓ Free 76 million Litmaps ✓ ✓ ✓ ✓ Freemium

Graph-Based

ChatGPT ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ Freemium 10 PDF files Claude ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ Freemium 5 PDF files Deepseek ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ Free Research ✓ ✓ ✓ ✓ ✓ ✓ Freemium 1 PDF file NotebookLM ✓ ✓ ✓ ✓ ✓ ✓ Freemium 50 PDF files Enago Read ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ Freemium 1 PDF file DocAnalyzer.AI ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ Premium few PDF files CoralAI ✓ ✓ ✓ ✓ ✓ ✓ Freemium 1 PDF file ExplainPaper ✓ ✓ ✓ ✓ ✓ Freemium 1 PDF file ChatPDF ✓ ✓ ✓ ✓ ✓ ✓ ✓ Premium 1 PDF file AnswerThis ✓ ✓ ✓ ✓ ✓ ✓ ✓ Freemium over 300 million

Paper Chat

Arxiv Sanity ✓ ✓ ✓ ✓ Free Scholar Inbox ✓ ✓ ✓ ✓ ✓ ✓ ✓ Free ResearchTrend.ai ✓ ✓ Freemium TrendingPapers ✓ ✓ ✓ ✓ ✓ ✓ Free Bytez ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ Freemium Notesum.ai ✓ ✓ ✓ ✓ ✓ ✓ Freemium Research Rabbit ✓ ✓ ✓ Free

Recommender

Graph-based Systems. Graph-based systems such as ORKG ASK [193] are designed to facilitate structured access to scientific knowledge. Unlike conventional paper search engines, they leverage a KG that organizes research contributions as structureddata ratherthan unstructured text. Such contributions are typically extracted from the abstract, introduction, and result sections [65, 201]. Those systems enable users to ask complex, domain-specific questions and receive answers synthesized from semantically structured scientific data. They typically use techniques such as KG-based reasoning and retrieval-augmented generation (RAG) to extract relevant information from the KG, providing more interpretable and verifiable answers compared to traditional LLM-based QA systems. CiteSpace and Sci2 are specialized bibliometric analysis and network analysis tools to study the structure and evolution of scientific research. CiteSpace focuses on identifying research trends, keyword co-occurrence networks, and citation bursts, using visual analytics to highlight emerging topics and influential papers using graphs. Sci2 is a more general-purpose tool designed for analyzing scholarly datasets, enabling users to perform network analysis, geospatial mapping, and temporal modeling of scientific literature

and collaboration patterns. Connected Papers is a visual literature exploration tool that maps papers related to a seed paper to provide an overview of a research field and support tasks such as bibliography construction and identification of prior and derivative work. Instead of building a direct citation tree, it organizes papers using similarity scores based primarily on bibliographic coupling and co-citation, typically via normalized overlap-based measures [130, 239]. The resulting weighted similarity graph visually clusters closely related papers and separates weaker ones, enabling interactive exploration of research clusters, and is powered by large-scale scholarly metadata (e.g., Semantic Scholar).

Paper Chat and QA. Paper chat and question-answering (QA) systems such as ChatGPT, Deepseek Chat, NotebookLM, ExplainPaper, ChatPDF, and DocAnalyzer.AI allow users to interact with scientific papers by asking questions and receiving responses based on the document’s content. They typically process a limited number of user-provided PDFs or text from specific websites. The core technology behind them is RAG [10, 125, 148], a technique that combines information retrieval with LLMs to improve accuracy and grounding. A typical RAG system first partitions the document into smaller sections and converts them into vector representations using embedding models. Upon a user query, the system retrieves the most relevant sections based on semantic similarity and passes them as context to an LLM, which then generates a response. This mechanism ensures that answers are directly grounded in the provided documents rather than relying solely on the model’s pre-trained knowledge, enhancing factual reliability and interpretability. Some systems incorporate LLM agents [29, 160, 254] that can reason over retrieved information, summarize findings, or extract key insights. These agents can follow multi-step reasoning strategies to provide more nuanced responses, such as synthesizing information from multiple sections or explaining technical terms in simpler language. By anchoring responses to document content, RAG-based systems mitigate hallucinations and make it easier for users to verify claims by checking the referenced passages. The effectiveness of these systems depends on the quality of document chunking, the efficiency of retrieval, and the model’s ability to integrate information into coherent, context-aware answers.

Recommender Systems. Scientific paper recommender systems such as Arxiv Sanity, Scholar Inbox, ResearchTrend.ai, and Research Rabbit leverage machine learning and information retrieval techniques to help researchers discover relevant literature. These systems generally fall into two main categories: content-based filtering, collaborative filtering and hybrid approaches. Content-based methods [5, 23] analyze the text of papers to build representations that capture their meaning. Traditional approaches rely on sparse abstract or document representations such as TF–IDF [241], which assigns importance to words based on their frequency and distinctiveness in a corpus. More advanced models, such as SPECTER [50] and GTE [161], use dense abstract or document embeddings derived from neural networks; they map papers into a high-dimensional vector space where similar documents are close to each other. The Massive Text Embedding Benchmark (MTEB) [189] ranks many state-of-the-art embedding models on a comprehensive benchmark comprising various different datasets and tasks. These embeddings enable fast similarity searches and improve over simple keyword matching. In contrast, collaborative filtering [17, 268] relies on user interactions, such as downloads, bookmarks, and citations, to recommend papers based on the behavior of similar users. One challenge of pure collaborative filtering is the cold start problem, where new papers or users lack sufficient data for recommendations. To mitigate this, many modern systems employ hybrid approaches, such as two-tower architectures [53, 296, 299]. These models learn separate representations for papers and users, combining textual embeddings with user interaction data to generate more personalized recommendations. State-of-the-art systems often use a mix of these techniques to balance relevance, novelty, and diversity. The effectiveness of these systems depends on the quality of embeddings, the availability of interaction data, and the efficiency of ranking algorithms that surface the most useful papers.

- 3.1.3 Domains of Application. The tools discussed in this section are largely domain-agnostic and can be applied across scientific disciplines by adapting the underlying corpus and domain resources. For example, in medical and neuroscience research, Ben Ezzdine et al. [22] survey exercise and cognitive-training interventions for neurodegenerative disorders and discuss how AI methods are being used to support evidence synthesis and analysis. In ecology, LLMs have been evaluated for extracting structured ecological variables from the scientific literature to accelerate evidence synthesis [92]. In chemistry and materials science, NLP/LLM pipelines have been used to mine synthesis conditions and materialproperty records from papers to construct structured datasets [233, 314]. However, many benchmarks used to evaluate such systems remain concentrated in computer science and AI, reflecting current dataset availability.
- 3.1.4 Limitations and Future Directions. A primary challenge for scholarly search systems is data quality and coverage gaps: systems often struggle with incomplete, non-standard, or outdated data sources, which can lead to inaccuracies and inconsistencies in retrieved information. There is also the issue of model bias, where search and ranking algorithms adopt biases of their training data, potentially influencing the visibility of certain research areas and limiting the diversity of perspectives presented to users. Another major limitation lies in scalability and real-time processing—i.e., efficiently handling large-scale datasets while maintaining low latency and high retrieval accuracy. Finally, many AI-assisted research tools rely on proprietary data, closed APIs, or evolving LLM backends, which complicates strict reproducibility and long-term comparability. These limitations suggest several promising future directions. One potential avenue is enhanced personalization, which can be achieved by adapting search engines to user preferences, providing more tailored recommendations based on research interests and behavioral patterns. Fostering interdisciplinary collaboration through the integration of AI-powered search systems with other digital tools, such as data visualization platforms and research management software, could likewise facilitate more comprehensive and insightful research outcomes.


### 3.2 AI-Driven Scientific Discovery: Ideation, Hypothesis Generation, and Experimentation

Ideation focuses on proposing new tools and/or analyzing existing ones, while hypothesis generation involves formulating specific, testable questions that guide empirical or theoretical justifications. In today’s age of rapidly growing scientific literature, the effort of moving from literature review to idea or hypothesis formation has become increasingly time-consuming. Recently, LLMs have been employed to address this issue by making idea and hypothesis formation efficient: they are being leveraged both as generators (to autonomously produce ideas and hypotheses) and as evaluators (to assess their quality and select those that are meaningful, relevant, and novel). Experimentation adds further complexity, requiring careful methodological design, large-scale simulations, and in-depth results analysis. In this section, we first review ideation, hypothesis generation, and their (intrinsic and downstream) evaluation, then discuss how experimentation, framed as a form of downstream evaluation, can be automated through LLMs.

3.2.1 Data. Here we survey diverse datasets for evaluating LLMs in hypothesis generation, idea formation, and experimentation. These datasets, summarized in Table 2, were constructed from various scholarly sources representing a variety of scientific domains.

SciMON [31], a dataset for the idea generation task, is a subset of the Semantic Scholar Open Research Corpus (S2ORC) [176] focusing on abstracts of Association for Computational Linguistics (ACL) publications from 1952 to 2022. It contains 135,814 abstracts, divided into training (before 2021), validation (2021), and test (2022) sets. Each abstract was annotated using PL-Marker [295] and a structure classifier [49] that extract keywords and categorize

Table 2. Overview of datasets for idea and hypothesis generation and experimentation

##### Dataset Source Data Size Domain Time Span Task

SciMON [31] ACL Anthology 135,814 papers NLP 1952–2022 Idea Generation IDEA Challenge [67] University of Bristol 240 prototypes Engineering 2022 Idea Generation SPACE-IDEAS+ [81] COLING 1020 ideas Physics 2024 Idea Generation TOMATO-Chem [293] Nature and Science 51 papers Chemistry 2024 Hypothesis Generation LLM4BioHypoGen [209] PubMed 2,900 papers Medicine 2000–2024 Hypothesis Generation CSKG-600 [60] CSKG 600 hypotheses AI 2010–2017 Hypothesis Generation ScienceAgentBench [41] OSU NLP 44 papers Diverse 2024 Automated Experimentation SWE-bench [119] ICLR 2,294 issues SWE 2024 Automated Experimentation MLGym-Bench [190] Meta 13 tasks Diverse 2025 Automated Experimentation

sentences as providing background, research ideas, etc. The tools were evaluated on a human-curated subset, and only high-confidence annotations were retained; despite this, some annotations may be incorrect, and errors can propagate and affect ideation quality.

SPACE-IDEAS+ [81] releases two versions of datasets. The smaller one contains 176 ideas sampled from the Open Space Innovation Platform (OSIP), an online repository of publicly available ideas related to space innovation. All the ideas were manually annotated by human experts, where each sentence was labeled with one of five roles (Challenge, Proposal, Elaboration, Benefits, Context) by two human annotators. Meetings were conducted to resolve disagreements between annotators. The larger version contains 1,020 ideas that were annotated by having GPT-3.5-turbo adopt the same annotation guidelines. A subset of the generated annotations was evaluated by comparing with human annotations; the agreement of 50% indicates the mediocre quality of GPT annotations.

TOMATO-Chem [293] is a hypothesis generation dataset containing 51 chemistry and material science papers published in Nature or Science in 2024. To these papers experts applied annotations concerning the background, research questions, works that potentially inspired the paper, hypotheses, and experiments for hypothesis justification. Details concerning the annotation task (e.g., the number of annotators and their agreement) are unfortunately not reported.

LLM4BioHypoGen [209], another hypothesis generation dataset, consists of 2,900 medical publications sourced from PubMed, where 2,500 papers were used for the training set and 200 papers for validation set (both published before January 2023), with 200 papers in the test set (published after August 2023). Each paper was annotated by using GPT to construct background and hypothesis pairs; however, no human evaluation of these pairs was provided.

ScienceAgentBench [41] is an automated experimentation dataset comprised of 102 tasks derived from 44 peerreviewed publications across four disciplines: bioinformatics, computational chemistry, geographical information science, and psychology & cognitive neuroscience. Each task requires an agent to generate a self-contained Python program based on a natural language instruction, a dataset, and optional expert-provided knowledge. The benchmark employs multiple evaluation metrics, including the valid execution rate, success rate, CodeBERTScore, and API cost, to assess the generated programs’ correctness, execution, and efficiency.

SWE-bench [119] is a similar dataset containing 2,294 tasks derived from 12 popular open-source Python repositories in real-world software engineering. Each task requires the model to edit a full codebase based on an issue description, producing a patch that must apply cleanly and pass fail-to-pass tests. The benchmark features long, complex inputs, robust evaluation via real-world testing, and the ability to be continually updated with new issues. However the execution-based testing can be misleading as it does not assess criteria such as comprehensiveness, efficiency, or

Hypothesis Generation

Idea Generation Generate a novel AI research idea.

Evaluation Evaluate the novel AI research idea/hypothesis.

Automated Experimentation Formulate the task, implement, evaluate and iterate of the sample output from idea/hypothesis generation.

Task

Generate a hypothesis related to online consumer behavior.

Scientific Literature (Papers, Metaanalyses, Systematic Reviews)

Raw Data (Surveys, Sensors, Experiments)

Sample output from idea generation/hypothesis generation.

Web Data (Scientific Discussions, Social Media Forums)

Sample Input

Datasets (Open Databases, Government Statistics, Lab Datasets)

Computational Models & Simulations

Knowledge Graphs (Semantic Scholar, Microsoft Academic)

Feasibility Constraints (Resources, Ethics, Funding)

Iterative refinement [108, 204]

Multi-agent workflow [113, 174, 180, 258, 317]

Automatic evaluation [165, 209, 244]

Knowledge graph [84, 285]

Human alignment [154]

Human evaluation [292]

Methods

RAG [38, 293]

End-to-end systems [177, 289]

Tree search [46, 134, 228]

Simulation-based evaluation [143, 228] Real-world experimentation [236, 306]

Post-training LLMs [91, 208, 315]

Multi-agent systems [11, 247]

Iterative refinement [52, 273]

Direct evaluation for generated idea/hypothesis via automatic metrics and human evaluation.

A method that leverages memoryaugmented neural networks for knowledge acquisition in a lifelong scenario.

User-generated content (like unboxing videos and reviews) greatly influences blind box purchases among young consumers.

Task forumulation

Sample Output

Code

Evaluations

Downstream evaluation via simulation or real-world experimentation.

Refinements

Fig. 2. Examples of idea generation, hypothesis generation, evaluation, and automated experimentation follow a four-component structure: task, sample input, methods, and sample output. The task defines the goal of each process. For idea/hypothesis generation, sample input consists of benchmark datasets for each task, whereas evaluation uses its sample output. Automated experimentation uses sample output from idea/hypothesis generation for the task and raw data/computational models and simulation as sample input. Methods encompass a taxonomy of approaches. Sample output differs by process: idea/hypothesis generation and automated experimentation yield textual outputs (descriptions, explanations, or code), whereas evaluation produces quantitative scores.

readability. While there is an additional rubric-based human evaluation where final versions are revised by experts, these human annotators are mainly familiar with Python and tend to dismiss other languages.

3.2.2 Methods and Results. Here, we discuss state-of-the-art methods and results in hypotheses generation, idea formation, and automated experimentation. Figure 2 provides some examples for each approach.

Idea Generation. Several methods have been proposed to generate research ideas, variously using iterative refinement, human alignment, end-to-end autonomous systems, or multi-agent systems [11, 108, 117, 139, 154, 177, 211, 227, 247, 280, 289]. For iterative refinement, Hu et al. [108] introduce an iterative planning and search framework aimed at enhancing the novelty and diversity of ideas generated by LLMs. By systematically retrieving external knowledge, the approach addresses the limitations of existing models in producing simplistic or repetitive suggestions. Similarly, IdeaSynth [204] focus on iterative refinement by providing literature-grounded feedback. It represents research ideas as nodes on a canvas to facilitate the idea iteration and composition of different idea facets, enabling researchers to develop more detailed and diverse ideas. Work involving human alignment seeks to organize information in ways that mirror human research processes. Chain of Ideas (CoI) [154] proposes structuring literature into a chain to emulate the progressive development of research domains. This facilitates the identification of meaningful directions and has been shown to outperform existing methods in generating ideas comparable in quality to those produced by human researchers. Scideator [211], in contrast, focuses on recombining facets (e.g., purposes, mechanisms, and evaluations) from existing research papers to synthesize novel ideas. By incorporating automated novelty assessments, Scideator enables users to identify overlaps and refine their ideas. The AI Scientist [177] is a prominent example of an end-to-end autonomous system. It is a framework for automating the entire research pipeline, including idea generation, experiment execution, and paper writing. The AI Scientist-v2 [289] employs an agentic framework using tree search and iterative refinement. Among multi-agent systems, VirSci [247] employs an ensemble of virtual agents to

collectively generate, evaluate, and refine ideas. It outperforms individual LLMs, underscoring the potential of teamwork in enhancing scientific innovation. ResearchAgent [11] is another a multi-agent LLM framework that enables ideation by generating new research problems, methods, and experiments from existing literature and iteratively refining them through LLM-assisted peer review.

Hypothesis Generation. A considerable number of studies [1, 12, 16, 36, 38, 84, 91, 120, 171, 172, 188, 196, 208, 255, 256, 267, 285, 292, 293, 315, 315] have employed LLMs to generate hypotheses, all of which differ in their approaches. These can be broadly categorized as employing (a) knowledge graphs, (b) retrieval-augmented generation, and/or (c) post-training of LLMs. Among knowledge graph approaches is KG-CoI [285], which uses an external KG that grounds the model’s reasoning in structured knowledge, enhancing the quality of generated hypotheses and reducing hallucination during hypothesis generation. SciAgents [84] is a framework that combines KGs with multi-agent systems and LLMs; it organizes scientific concepts into a graph and enables agents to reason over this structure to generate and iteratively refine hypotheses. For RAG, MOOSE-Chem [293] is a retrieval-based system for the rediscovery of high-impact chemistry hypotheses given only a research background. It first retrieves relevant papers from a large corpus, then uses these papers together with the background to generate candidate hypotheses, and finally ranks the hypotheses by quality. Chemist-X [38] is retrieval-augmented agent for reaction condition discovery in chemical synthesis. It uses LLMs to retrieve information (e.g., reaction conditions and molecules) from chemical literature and molecular databases, helping to narrow the search space for plausible reaction conditions, which are then treated as candidate hypotheses about optimal experimental settings. Major strategies for post-training LLMs, include few-shot learning, fine-tuning, and iterative refinement. Qi et al. [208] find that hypotheses generated by few-shot learning are judged by humans as more testable than those generated in a zero-shot setup. They report that while fine-tuning improves the overall quality of hypotheses, the improvement is limited to the domain of training data; in unseen domains, fine-tuning harms hypothesis quality, particularly the novelty aspect. Zhou et al. [315] iteratively refine hypotheses through reinforcement learning, aiming to increase the similarity between a research problem and a generated hypothesis. The AI co-scientist [91] employs a multi-agent system relying on a generate–debate–evolve framework to iteratively enhance generated hypotheses.

Evaluation. The evaluation of generated ideas and hypotheses ensures that they are scientifically meaningful and feasible. Evaluation approaches [e.g., 31, 143, 209, 228, 236, 244, 270, 292, 293, 306] can be generally categorized as intrinsic (automatic or human evaluation) or downstream (simulation-based evaluation or real-world experimentation).

For automatic evaluation, metrics such as ROUGE [165] have been used to assess the quality of generated hypotheses (or ideas) by measuring their similarity to human-annotated ground truths [244]. Qi et al. [209] leverage LLMs-as-judge to evaluate hypotheses based on four scientific aspects: novelty, relevance to the given background, significance within the research community, and verifiability (i.e., testability). In human evaluation, domain experts are involved to assess the quality of generated ideas and hypotheses, especially when ground truth is unavailable. For instance, Yang et al. [292] invited social scientists to provide feedback on the LLM-generated hypothesis, “In collectivist cultures, individuals engage in more conspicuous consumption behaviors compared to individualistic cultures.” The social scientists found the hypothesis potentially novel and counterintuitive, as prior research suggests that collectivist cultures typically discourage conspicuous displays of personal wealth. Such expert feedback helps identify hypotheses that are meaningful and worth further investigation. LabBench [143] and AgentClinic [228] are examples of simulationbased evaluation, where generated hypotheses are evaluated in virtual laboratory environments. These tools simulate

laboratory conditions in materials science and biomedicine, allowing hypotheses to be tested cost-effectively. Realworld experimentation is employed by Zhang et al. [306], who evaluate candidate hypotheses (protein variants) within an automated biofoundry. Each variant is constructed and evaluated using instruments such as liquid handlers and thermocyclers, together with peripheral devices like plate sealers, shakers, and incubators, to measure enzymatic activity, protein yield, and success rates. Si et al. [236] invited 43 expert researchers to experiment with LLM-generated ideas. Each researcher spent over 100 hours implementing the assigned ideas and wrote a short paper to report the results. Ideas proposed by human researchers were also implemented as a control group. All the papers were then reviewed blindly by expert reviewers. Experimental results from LLM-generated ideas were judged by expert reviewers to be less novel, exciting, or effective compared to those from human ideas.

Automated Experimentation. Experimentation, which can serve as downstream evaluation for empirically validating AI-generated ideas and hypotheses, encompasses task formulation, implementation, evaluation, and iteration. Automated experimentation aims to streamline this workflow, with approaches like neural architecture search [70] and AutoML [101]. LLMs further enhance this by enabling automation through natural language prompts. AutoML-GPT [259] and MLcopilot [305] use LLMs for hyperparameter tuning, while MLAgentBench [113] benchmarks fundamental automation tasks. Recent work explores advanced frameworks incorporating multi-agent collaboration, tree search, and iterative refinement for scientific experimentation.

For multi-agent workflow, GVIM [180] enhances chemical research with domain-specific functions, while DrugAgent [174] employs LLMs for task planning in drug discovery. AutoML-Agent [258] integrates retrieval-augmented planning for AutoML tasks, and MLAgentBench [113] benchmarks LLM-driven agents in machine learning experimentation. The Agent-as-a-Judge framework [317] introduces structured agent evaluation. For tree search, AIDE [229] applies solution space tree search to refine solutions in Kaggle challenges. The Tree Search for Language Model Agents framework [135] enables LLM agents to plan multi-step interactions using best-first tree search, pruning less promising options. SELA [45] combines LLM-generated insights with Monte Carlo tree search, iteratively refining machine learning experiments by selecting promising configurations and executing them. For iterative refinement, APEx [51] automates LLM-based experimentation with an orchestrator, execution engine, benchmark generator, and model library. OpenHands [274] enables AI agents to interact with software, execute actions in a sandboxed runtime, and collaborate across tasks using predefined benchmarks.

- 3.2.3 Domains of Application. Studies have addressed ideation and hypothesis generation in NLP, engineering, physics, chemistry, the social sciences, and medicine. Work on automated experimentation has similarly relied on domain-specific datasets to guide the process of designing and testing experiments. However, the designs underlying these systems are typically domain-agnostic. For instance, iterative refinement, human alignment, multi-agent systems, and tree search are low-level methodologies that are applicable across multiple domains. Regarding evaluation, except for automatic evaluation, most evaluation approaches are limited to the domains for which they are designed: human evaluation relies on domain-specific evaluation guidelines, simulation-based evaluation requires domain-specific laboratory configurations, and infrastructure in which real-world experimentation is conducted may differ across domains.
- 3.2.4 Limitations and Future Directions. A large-scale study [237] comparing human researchers and LLMs finds that LLMs generate ideas judged to be more novel but slightly less feasible, highlighting challenges like limited diversity and self-evaluation failures. Additionally, given that ideas and hypotheses are theoretical and costly to validate, it is unclear whether they could lead to scientific discovery. Furthermore, previous methods lack due diligence through data,


and therefore generated ideas and hypotheses are often too general [293]. Moreover, LLMs may end up re-generating recently discovered ideas and hypotheses, since they lack access to recent scientific papers [172]. Their outputs are moreover very sensitive to the framing of input prompts [196]. Future work could focus on improving feasibility and diversity of ideas and hypotheses, consulting scientific papers in real time, and refining ideation and hypothesis generation through data inspection. LLM-automated experimentation has several additional challenges. First, LLMs’ propensity to hallucinate results or references disrupt the precise steps required for experimental workflows. They also struggle to integrate and align different modalities, such as video, audio, or sensory data, which are increasingly essential in modern scientific experimentation. Moreover, LLMs lack the critical analysis capabilities necessary to identify flaws or refine hypotheses during experimentation. Particularly in biology and chemistry, they may also struggle with precise reasoning and tool usage, which are vital for ensuring experimental success [214].

### 3.3 Text-based Content Generation

Generating scientific content includes generating texts of various types and lengths, each demanding different skills. In this section, we focus on selected subtasks to emphasize the varied challenges inherent in each. Titles of scientific papers need to reflect the content of a paper in a few catchy words, while abstracts are concise, stand-alone summaries. Approaches to generating long texts face challenges such as structuring arguments and maintaining factual consistency. Related work generation also requires text summarization skills, though in a more concise form. Generating bibliographic references depends on scientific discovery and literature research and has limited room for variation in phrasing, unlike in tasks such as proof-reading and paraphrasing. As we discuss, current generative models exhibit varying performance across these subtasks.

- 3.3.1 Data. Open access research articles are a valuable data source for text-based content generation. These include scientific publisher repositories offering at least some open access content (e.g., Nature portfolio, Taylor & Francis) as well as preprint repositories (e.g., arXiv, bioRxiv). These repositories can be leveraged to develop datasets with pairs of titles and abstracts or abstract and conclusion/future work pairs. Wang et al. [271], for example, extract from PumMed title to abstract pairs, abstract to conclusion and future work pairs, and conclusion and future work to title pairs. Annotated, task-specific datasets for scientific text generation are presented in Table 3.
- 3.3.2 Methods and Results. Here we survey approaches to generating textual content for scientific papers, such as titles, abstracts, related work sections, and bibliographies. An overview of these processes is given in Appendix B.3.


Title Generation. Generating appropriate titles for scientific papers is an important task because titles are the first access point of a paper and can attract substantial reader interest; titles can also influence the reception of a paper [147]. Consequently, several works have targeted generating titles automatically, often using paper abstracts as input. For example, Mishra et al. [184] use a pipeline of three modules, viz. generation by transformer based (GPT-2) models, selection (from multiple candidates) and refinement. Chen and Eger [40] also leverage transformers for title generation from abstracts, including humorous title generation. Their results show that none of the applied models (BART, GPT-2, T5, GPT-3.5) can adequately generate humorous titles. Sebo et al. [231] find that GPT-4o generated titles are preferred by human raters over human titles, given the abstract. Wang et al. [271] address the problem differently by drafting titles based on future work sections of previous related papers.

Table 3. Annotated or task-specific datasets for scientific text generation.

##### Dataset Size Sources Application

Abstract-title humor [40] 2,638 humor annotated titles ML and NLP domain Title generation PaperRobot [271] 27K title–abstract, 27K abstract–

PubMed Title, abstract, conclusion, and future work generation

conclusion/future work, 20K conclusion/ future work–title pairs

ScisummNet [294] 1,000 papers + 20 citation sentences each ACL Anthology Related work generation CORWA [157] 927 related work sections NLP domain Related work generation CiteBench [77] 358,765 documents + citations arXiv et al. Related work generation LongWriter [13] 6,000 texts (literature, academic writing,

Open datasets Long text generation

popular science, news)

LongWriter-Zero [284] 8,610 instruction tuning requiring outputs exceeding 10,000 words

Open datasets Long text generation

LongEval [282] 166 high-quality human-authored samples exceeding 2,000 words

arXiv, blogs, and Wikipedia

Long text generation

Casimir [122] 15,646 papers (consecutive versions) OpenReview Paraphrasing ParaRev [121] 48,203 paper paragraphs (consec. versions) OpenReview Paraphrasing

Abstract Generation. There are several approaches trying to assess the capabilities of LLMs to generate abstracts based on context information such as paper titles, journal names, keywords, or the full text of the paper. Hwang et al. [115] assess the ability of GPT-3.5 and -4 to generate abstracts based on a full text. The results are manually evaluated using the Consolidated Standards of Reporting Trials for abstracts, a standard that aims to enhance the overall quality of scientific abstracts [106]. While the readability of GPT-generated abstracts is rated higher, their overall quality is inferior to the originals. Wang et al. [271] generate abstracts from titles, leveraging transformers and knowledge bases. Gao et al. [79] collect 50 publications from five medical journals and use ChatGPT to generate abstracts based on their titles and journal names. Both original and generated abstracts are evaluated using AI output detectors and human reviewers. Human reviewers are able to identify 68% of the generated abstracts, but misclassified 14% of original abstracts as LLM-generated. Farhat et al. [71] evaluate the performance of ChatGPT generating abstracts based on three keywords, the name of a database (Scopus or Web of Science), and the task to analyze bibliographic data in the domain indicated by the keywords. Manually comparing the generated abstracts to original abstracts on the same topic, the authors conclude that at the time of the study, ChatGPT was not a trustworthy tool.

Long Text Generation. The AI Scientist [177, 289] produces complete scientific manuscripts by leveraging outputs from earlier stages of the scientific lifecycle, such as experimental results, intermediate analyses, and candidate citations. By conditioning on these intermediate outputs, the system drafts papers largely conforming to domain-specific conventions, including citation and disciplinary writing norms. However, the system does not explicitly address the challenge of maintaining global narrative coherence, nor does it provide principled mechanisms for modeling long-range logical dependencies and argument consistency across extended texts. Beyond end-to-end research automation frameworks, other work focuses more specifically on long-form text generation itself. LongWriter [13] addresses long-form text generation by targeting long-range coherence and structural consistency. The model introduces hierarchical attention mechanisms to enhance thematic consistency across extended texts and employs tailored fine-tuning strategies to better align generated outputs with user prompts. LongEval [282] provides a systematic evaluation of long-text generation under both direct and plan-based generation paradigms across academic, encyclopedic, and blog-style domains. The findings suggest that larger, general-purpose, instruction-tuned models often perform comparably to specialized, smaller

long-text models (e.g., LongWriter), raising questions about the marginal benefits of domain-specific fine-tuning for long-form generation. Motivated by the need for stronger structural control, recent work has increasingly moved beyond standard supervised fine-tuning (SFT) toward approaches based on reinforcement learning (RL). LongWriter-Zero [284] demonstrates that RL without SFT can enable ultra-long text generation (i.e., 10,000+ words). By employing composite reward models that jointly evaluate length, quality, and formatting constraints, LongWriter-Zero achieves competitive or even superior performance relative to proprietary models (i.e., Claude-Sonnet-4, Gemini-2.5-Pro) in long-form generation tasks. Similarly, LongReward [303] leverages RL with custom-designed reward signals that emphasize coherence, factual accuracy, and linguistic quality. These reward mechanisms are particularly relevant for scientific text generation, where accuracy and adherence to domain-specific conventions are crucial.

Related Work Generation. There has been a substantial body of work on related work generation through text summarization, with variances in the approach (extractive or abstractive) and the citation text length (sentence- or paragraph-level). Extractive approaches focus on selecting sentences from cited papers and reordering them to form a paragraph of related work. For instance, Hoang and Kan [105] propose an extractive summarization approach that selects sentences describing the cited papers. Subsequent extractive approaches differ from this approach in how they order the extracted sentences: while Wang et al. [269] assume that the sentence order is given, Hu and Wan [110] and Deng et al. [58] take advantage of an automatic approach to reorder sentences based on topic coherence. Most abstractive approaches are based on language models and focus on generating either a single sentence from a single reference, or a single paragraph from multiple references. Typically, the abstractive process is repeated until a related work section is complete. AbuRa’ed et al. [2] introduce an abstractive summarization approach to generate citation sentences in a single-reference setup. Their approach has been trained on the ScisummNet corpus [294] with paper abstracts as inputs and citation sentences as outputs. Li et al. [157] further extend this idea to a multiple-reference setup, namely generating a paragraph of citation sentences from various cited papers. Their approach has been trained on the CORWA corpus [157] to generate both citation and transition sentences. Recently, several works have explored LLMs for related work generation. For instance, Şahinuç et al. [220] use instruction promoting with LLMs, an alternative to extractive and abstractive approaches, to generate citation sentences. Martin-Boyle et al. [182] employ a citation graph coupled with LLMs to produce a related work section. Li and Ouyang [159] use LLM prompting to extract features that capture relationships between citing and cited papers; these features are then composed into a new prompt that enables the LLM to generate a related work section. Şahinuç et al. [219] introduce a multi-turn evaluation framework for assessing the quality of AI-generated related work sections. The framework uses expert preferences to align with human judgment, and iteratively evaluates section drafts and generates natural-language feedback for revision. Overall, extractive approaches, while factual, often lack fluency and coherence. In contrast, abstractive approaches and instruction prompting, which are based on (large) language models, do not struggle with these issues, however, they suffer from factual errors, known as hallucination.

Citation Generation. Bibliographic references are important for ensuring the scientific integrity of a paper. However, in many cases, cited references generated by LLMs such as ChatGPT are reported not to exist—that is, they are hallucinated or incorrect [71, 112, 158]. Most studies on this phenomenon are case studies presenting one or more examples. In a study by Walters and Wilder [265], GPT-3.5 and -4 are used to generate 84 literature reviews containing 636 bibliographic citations. 55% of the GPT-3.5 citations were fabricated, compared to 18% of GPT-4’s. Additionally, 43% of non-fabricated GPT-3.5 citations contain substantive citation errors, compared to 24% for GPT-4. Despite this notable improvement, issues with citation fabrication and errors persist. In ScholarPilot [275], retrieval tokens are generated to

query citation databases and the retrieved references are directly fed into the model to augment the text generation process. The model is based on Qwen-2.5-7B and fine-tuned on a corpus of 500K arXiv papers. It outperforms other Qwen-2.5 variants according to model-based evaluation using GPT-4o.

Proof-reading and Paraphrasing. LLMs have been reported to provide useful assistance for scientific writing tasks, such as proof-reading, or providing suggestions for improving the writing style [222]. Additionally, some authors emphasize that LLMs can be helpful especially for non-native English speakers with regards to grammar, sentence structure, vocabulary and even translation, effectively serving as an English editing service [30, 131]. Most papers on this topic are case studies, with results qualitatively evaluated by a human expert. Jourdan et al. [122] introduce Casimir, a dataset of 15,646 OpenReview articles with sentence-level paired revisions. A later extension, ParaRev [121], provides paragraph-level pairs, with a subset manually annotated with revision instructions. Experiments show that detailed instructions substantially improve automated revision quality under both statistical and model-based evaluations.

Evaluation. Generated scientific texts are evaluated both with task-specific methods and those general to LLMs. Traditional reference-based metrics, such as BLEU [194] or ROUGE [165], require associated reference output as a ground truth and have shown low correlation with human judgments [170]. With the rise of deep learning and LLMs, model-based approaches are gaining increasing importance [80, 149]. Although not exclusive to scientific texts, they focus on highly relevant dimensions such as coherence, consistency, and fluency [145, 175]. In a more domainspecific approach, Huang et al. [114] propose PaperEval, a multi-agent system powered by LLMs to assess scientific paper quality across various dimensions (question, method, result, and conclusion). Its feasibility and effectiveness in distinguishing high-quality from low-quality papers have been tested on three evaluation datasets across four scientific fields (mathematics, physics, chemistry, and medicine).

- 3.3.3 Domains of Application. Text-based content generation is relevant for all scientific domains. Liang et al. [163] conduct a large-scale analysis across 1M papers published between January 2020 and September 2024 to measure the prevalence of LLM-modified content over time. The papers they investigated were from a variety of disciplines and published on arXiv, bioRxiv, or Nature portfolio. Their results show the largest and fastest growth in computer science, with up to 22% of the papers containing LLM-modified content; mathematics had the lowest prevalence (up to 9%). According to arXiv’s September 2024 Natural Language Learning & Generation report [146], top-cited papers show notably fewer markers of AI-generated content as compared to random samples.
- 3.3.4 Limitations and Future Directions. LLMs and LLM applications demonstrate strong capabilities in tasks such as proofreading and paraphrasing, but still exhibit notable limitations for other tasks, making human-in-the-loop approaches essential. In particular, factual consistency, truthfulness, and bibliographic citations require human oversight. Rapid advances in LLMs further complicate evaluation, quickly rendering existing methods outdated and hindering reproducibility. Evaluating AI-generated text remains challenging: statistical metrics like BLEU and ROUGE lack semantic depth, model-based evaluations can be unreliable, and many tasks depend on small-scale human evaluations due the scarcity of appropriate benchmarks. Consequently, future research must prioritize robust benchmarks and datasets for scientific text generation. Beyond technical challenges, ethical concerns, including authorship, plagiarism, bias, and truthfulness, underscore the need for trustworthy and responsible AI systems.


### 3.4 Multimodal Content Generation and Understanding

Multimodal content generation in the scientific domain refers to generating multimodal scientific content such as figures and tables in scientific papers, or slides and posters in a post-publication process. Automating such tasks via AI is important for multiple reasons: (i) generating high-quality figures, tables, slides and posters is costly in terms of effort and time; (ii) high-quality multimodal content in a paper can positively influence citation or acceptance decisions [144]; (iii) tables, figures, posters, and slides make scientific content more accessible and compact. Multimodal content understanding refers to interpreting scientific images and tables, a prerequisite for answering questions about them or providing captions or summaries. These tasks are likewise effortful and time-consuming for human authors, pointing to a role for AI assistance.

3.4.1 Data. In this section we detail datasets and benchmarks for selected multimodal tasks. Further tasks, including table understanding and generation, can be found in Appendix B.4, along with an overview table.

Scientific Figure Understanding. Scientific figure understanding benchmarks typically contain summaries or QA pairs for scientific figures. Kembhavi et al. [128] provide a dataset with over 5K richly annotated diagrams and over 15K questions and answers. FigureQA [123] is a synthetic dataset of over 100K scientific-style (dot-)line plots, vertical and horizontal bar graphs, and pie charts, along with 1M associated questions generated using 15 different templates. Later research focuses on more challenging and realistic QA pairs. ChartQA [183], for instance, provides complex reasoning questions concerning charts from various science-related sources. CharXiv [276] is a manually curated dataset of descriptive and reasoning questions about 2.3K “natural, challenging, and diverse” charts from aXiv papers. ArXivQA [153], a dataset of 35K scientific figures sourced from arXiv, contains 100K GPT-4o-generated, manually filtered QA pairs. SPIQA [203] is a dataset of 270K manually and automatically created QA pairs that interpret complex scientific figures and tables. Xu et al. [286] treat the problem of chart summarization with a 190K-instance dataset that builds on ChartSumm [212], itself containing more than 84K charts along with their metadata and descriptions.

Scientific Figure Generation. Several datasets for scientific figure generation have been proposed. DaTikZ [19–21] provides captions of scientific figures as instructions along with corresponding TikZ code, sourced from the TEX Stack Exchange and arXiv submissions. A later and larger version [94] improves the data quality through VLM-generated descriptions instead of noisy captions. For the task of converting sketches into scientific figures, the SketchFig [21] benchmark provides 549 figure–sketch pairs sourced from the TEX Stack Exchange. DiagramGenBenchmark [278] contains 6,713 training and 270 testing samples for diagram generation, and 1,400 training and 200 testing samples for diagram editing, sourced from freely licensed DOT and TikZ diagrams in VGQA and DaTikZ. Plot2XML [54] includes 247 complex diagrams sourced from conference papers spanning multiple domains. ChartMimic [234] is a manually curated benchmark of 1,000 triplets of (instruction, code, figure) instances for chart generation across various domains, including physics and economics. The data comes from human annotators writing Python code for prototype charts. ScImage [304] contains targeted template instructions focusing on different comprehension dimensions (spatial, numeric, attribute); for a subset of the data, the authors also provide reference figures that were manually evaluated as being of high quality. In contrast to the other benchmarks, ScImage also contains instructions in languages other than English. SciDoc2DiagramBench [185] is a benchmark comprised of 1,000 diagrams extracted from the presentation slides of 89 ACL papers, along with human-written “intents”. The intents describe how the content from each paper can be translated into the diagrams for presentation purposes. nvBench [178], a benchmark of

25K tuples of natural language queries and corresponding visualizations, is drawn from 153 databases and contains more than 7K visualizations across seven chart types. nvBench is synthesized from natural language to SQL benchmarks.

Scientific Slide and Poster Generation. Early efforts at automating the generation of presentation slides from scientific papers relied on relatively small datasets for development and evaluation. For example, Sravanthi et al. [242] generate presentations from a modest collection of eight papers. Similarly, Hu and Wan [109] and Wang et al. [273] use 1,200 and 175 paper–slide pairs, respectively. For scientific poster generation, Qiang et al. [210] collect 25 pairs of scientific papers and their corresponding posters. Such early datasets are often inaccessible due to various restrictions on distribution.

Two free-content datasets, DOC2PPT [76] and SciDuet [249], have since emerged as widely used resources for scientific slide generation. The former consists of 5,873 scientific documents and their associated presentation slide decks, totalling around 100K slides, drawn from three research communities: computer vision, natural language processing, and machine learning. SciDuet has 1,088 papers and 10,034 slides from conferences such as ICML, NeurIPS, and the ACL Anthology. More recently, SlidesBench [83] has provided 7K training and 585 test examples, each containing 20 slides on average, sourced from the web and covering ten broad domains (art, marketing, environment, technology, etc.).

3.4.2 Methods and Results. Here we survey approaches to multimodal content generation and understanding; a summary table, along with additional related works, is provided in Appendix B.4.

Scientific Figure Understanding. Scientific figure understanding is typically framed in terms of (visual) QA—e.g., whether models are able to adequately answer questions on a given input figure [128]. Several recent studies train baseline models such as transformers or relation networks [123, 183], such as relation networks or apply recent LLMs to benchmarks [153, 276]. They generally show large gaps between proprietary models like GPT-4o and the strongest open models, and between all models and human performance. For chart summarization, Rahman et al. [212] find that older pre-trained language models such as BART and T5 suffer from hallucination and disregard important data points. Xu et al. [286] propose ChartAdapter, a lightweight transformer module that can be combined with LLMs for improved modeling of chart summarization. Evaluation of scientific figure understanding benchmarks tends to employ automatic metrics, many of which are now considered outdated or unreliable. For example, Xu et al. [286] use BLEU and ROUGE. By contrast, Pramanick et al. [203] report both human and automatic evaluation, the latter including not just traditional QA metrics such as METEOR, ROUGE, and BERTScore, but also novel LLM-based metrics.

Scientific Figure Generation. Although work on automating visualization for science dates back to the 1980s at least, most recent work, including that covered here, involves multimodal LLMs. AutomaTikZ [20] and TikZero [19] fine-tune custom LLMs on DaTikZ for the text-to-TikZ task. TikZilla [94] extends this line of work by applying reinforcement learning using a custom image encoder for more semantically meaningful rewards. VisCoder [192] uses Python libraries for visualization code generation. DeTikZify [21] reconstructs scientific figures in TikZ from sketches or images. Draw with Thought [54] uses multimodal LLMs for a preliminary coarse-to-fine planning approach, followed by structure-aware code generation with a self-refine mechanism for reconstruction. DiagramAgent [278] combines generation, reconstruction, and editing by introducing AI agents (plan, code, diagram-to-code, check). Shi et al. [234] aim to generate Python code from instructions and/or images, specifically focusing on charts. They evaluate three proprietary and 11 open-weight LLMs on their ChartMimic benchmark, finding that even the best models (GPT-4 and Claude-3-opus) have substantial room for improvement. Zhang et al. [304] provide a template-based approach to evaluate various multimodal LLMs in generating scientific images. They explore those that generate TikZ and

Python code for images, as well as those that generate images directly,4 and also consider different input languages (English, German, Chinese, Farsi). They find that, except for GPT-4o, most models struggle substantially in generating adequate scientific images. Zala et al. [301] explore the diagram generation task where LLMs first generate diagram plans and then the diagrams themselves. Mondal et al. [185] explore the same task with an additional refinement—namely, feedback from multiple critic models—to enhance factual correctness. Evaluation uses automatic metrics including DreamSim [75] for image similarity, Crystal BLEU [68] for code similarity, and CLIPScore [103] for text–image similarity, as well as manual evaluation by domain experts. The former are typically reported to have low or medium correlation with the latter, establishing the need for domain-specific evaluation in future work.

Scientific Slide and Poster Generation. Early work on scientific slide generation [109, 150, 242, 273] used extractive approaches, copying text from papers to serve as slide content. Later systems explored abstractive approaches to generate the textual content of slides, such as with sequence-to-sequence models [76, 249]. Researchers are now exploring (multimodal) LLMs for generating slides using natural language prompts [15, 181, 186]. AutoPresent [83], for example, fine-tunes an LLM using SlidesBench to generate slides from detailed natural language instructions with images, detailed instructions only, or high-level instructions. However, modern systems still take an extractive approach to multimodal content, copying images or tables directly from the original papers instead of generating new ones [15, 76, 186, 242, 249]. The task of poster generation has received less attention, with studies mainly exploring ML-based methods for generating key content and panel layouts [210, 288]. Evaluation of slide generation has involved both human judgments and automatic metrics (most commonly ROUGE). Fu et al. [76] introduce some novel metrics: Longest Common Figure Subsequence, which measures the quality of figures in the generated slides; Text–Figure Relevance, which assesses the similarity between the text of the ground truth slide and the generated slide containing the same figure; and Mean Intersection over Union, which evaluates layout quality. Recent studies have also used LLMs to assess the quality of generated slides [15, 181]. For scientific poster generation, in addition to conducting user studies, Qiang et al. [210] measure the mean squared error (MSE) of the panel parameters such as panel size and aspect ratio.

- 3.4.3 Domains of Application. Many recent datasets for multimodal content generation and understanding are drawn from arXiv and more generally the STEM domain. Models such as DeTikZify and AutomaTikZ have also been fine-tuned on such data. This indicates a limitation both in terms of application scenarios and model assessments, as these may perform worse when applied in cross-domain scenarios.
- 3.4.4 Limitations and Future Directions. Limitations common to the approaches we have discussed include (1) the comparatively small datasets for fine-tuning models; (2) sub–human-level performance on recent benchmarks, particularly for non-proprietary models; (3) over-representation of arXiv and STEM domains in training and evaluation; (4) models’ lack of reasoning abilities; and (5) lack of reliable, task-specific evaluation methods, particularly for generative tasks. Some problems are task-specific: for example, for table generation, the input text may be very long, which constitutes a problem for many current LLMs; for slide generation, there are no approaches that can generate slides from multiple documents (e.g., for tutorials) or that generate content beyond that contained in a reference paper (which may be necessary for including relevant background material); for figure generation, models like AutomaTikZ are trained on captions, which are often not appropriate for generating the corresponding figure (e.g., a caption may simply be “Proof


4Most scientific figure generation approaches are based on code generation, while direct image generation approaches are rare. The likely reason is that code generation methods usually work better (e.g., allowing higher precision when plotting numeric inputs) and their output is easier for users to post-edit. Within code generation, those employing general-purpose languages like Python seem to perform better than those targeting specialized drawing languages like TikZ, though current comparisons are restricted to individual use cases [304].

Analysis of Peer Reviews

| | |
|---|---|
| | |


| | |
|---|---|
| | |


Analysis

![image 7](Eger et al._2025_Transforming Science with Large Language Models A Survey on AI-assisted Scientific Discovery, Exper_images/imageFile7.png)

Scientific Rigour

Meta Review Generation

Research Manuscripts

Paper Feedback / Automatic Reviewing

| | |
|---|---|
| | |


Review

###### AI / LLMs Reviewer

Scientific Claim Verification

Fig. 3. Process of AI-enhanced peer review. In the analysis step, the LLM reviewer examines research manuscripts and evaluates peer reviews to assess scientific rigor. The review step involves providing feedback on the paper and verifying scientific claims. Finally, the gathered information is synthesized to generate a final meta-review.

of Theorem X”). Reproducibility is hampered by some studies’ use of datasets that are not freely distributable—for example, one study [94] reports that only a third of all arXiv-harvested papers are permissively licensed.

### 3.5 Peer Review

The highest standard in scientific quality control is peer reviewing. In this process, authors present their scientific arguments (e.g., the findings of a study, or a grant proposal) in form of a manuscript to their peers, who then assess its scientific validity and quality. Often this process has multiple stages, as shown in Fig. 3. For instance, in the ACL Rolling Review (ARR) system, reviewers write detailed assessments whose arguments and questions the authors may then rebut and clarify to convince the reviewers to raise their scores. A meta-reviewer then evaluates this discussion and submits to the program chairs an acceptance/rejection recommendation, which may or may not be adopted. During this process, multiple (potentially multi-modal) artifacts are processed and created—mainly the manuscript under review, the written reviews, the author–reviewer discussion, and the meta-review. In general, peer review is considered a challenging, subjective process, where reviewers are prone to unfair biases like sexism and racism, and often rely on expedient heuristics [215, 246]. In some fields, these problems are compounded by an exploding number of submissions [140], pushing review systems to their limits. To counteract this situation, researchers have addressed various several problems under the umbrella of AI-supported peer review. Related overviews on the topic, or on some of its aspects, point to its importance and timeliness [35, 63, 137, 141, 166, 245]. Here, we focus on approaches to the most established tasks related to peer review, following the same structure as in previous sections.

- 3.5.1 Data. Peer reviewing data is scarce: few scientific communities publish reviewing artifacts at all, let alone under permissive licenses. Exceptions include PeerRead [124], which collects review data from various sources (e.g., ACL, ICRL), and CiteTracked [200], which also contains citation information. NLPeer [66], a model for how larger-scale open publishing of raw peer reviewing data could work, uses a corpus of ARR reviews where the consent of the respective actors was explicitly obtained. Several annotated datasets support tasks in peer review analysis, an overview of which is provided in Table 4. Recent curated resources have focused on complex tasks such as understanding the effect of peer review feedback on manuscript revisions [56] or identifying the attitudes underlying specific criticisms in reviews [207].
- 3.5.2 Methods and Results. Pre-LLM approaches [e.g., 86] were mostly based on traditional ML methods, targeting simpler analyses involving sentence classification tasks. Later, deep learning approaches [e.g., 111] (including those


Table 4. Annotated and/or task-specific datasets for analyzing peer reviewing.

##### Dataset Size Sources Application

HedgePeer [86] 2,966 documents ICLR 2018 Uncertainty detection PolitePeer [24] 2,500 sentences ICLR et al. Politeness analysis COMPARE [238] 1,800 sentences ICLR Comparison analysis ReAct [46] 1,250 comments ICLR Actionability analysis MReD [232] 7,089 meta-reviews ICLR Meta-review analysis and generation CiteTracked [200] 3,427 papers, 12K reviews NeurIPS Citation prediction MOPRD [167] 6,578 papers PeerJ Review comment generation Revise and Resubmit [142] 5.4K papers F1000Research Tagging, linking, version alignment ORB [253] 92,879 reviews OpenReview, SciPost Acceptance prediction ARIES [56] 3.9K comments OpenReview Feedback–edits alignment, revision generation DISAPERE [129] 506 review–rebuttal pairs ICLR Review action analysis, polarity prediction, re-

view aspect

PeerReviewAnalyze [85] 1,199 reviews ICLR Review paper section correspondence, paper aspect category detection, review statement role prediction, review statement significance detection, meta-review generation

JitsuPeer [207] 9,946 review and 11,103 rebuttal sentences

ICLR argumentation analysis, canonical rebuttal scoring, review description generation, end2end canonical rebuttal generation

based on pre-trained language models) and more complex analyses (e.g., of argumentation) defined the state of the art in computational peer review processing. Researchers have now started exploring LLMs in prompting-based frameworks, for complex tasks like peer review generation and meta-review generation [e.g., 173]. Below we provide an overview of the methods and results for the most common tasks under the umbrella of peer reviewing. Information on related tasks, such as scientific claim verification, can be found in Appendix B.5.

Analysis of Peer Reviews. Prior works have analyzed peer reviews for a multitude of aspects, like uncertainty [86], politeness [24], and sentiment [32]. However, given that science as a whole and especially peer review relies to a large extent on convincing peers, large efforts have been spent on understanding arguments or argument-related aspects (e.g., substantiation of arguments) in peer review artifacts [e.g., 74, 111]. Here, most approaches have used pre-trained language models. For instance, Hua et al. [111] work on mining the arguments in peer reviews using conditional random fields, LSTMs, and BERT. In contrast, Guo et al. [95] and Fromm et al. [74] fully rely on (domain-adjusted) pre-trained language models for argument mining: SciBERT, ArgBERT, and PeerBERT. Cheng et al. [43] leverage multi-task learning approaches based on LSTMs and BERT. In a similar vein, Purkayastha et al. [207] study the generation of rebuttals for author–reviewer discussions based on jiu-jitsu argumentation, a specific argumentation theory.

Paper Feedback and Automatic Reviewing. Several works have explored methods to provide general feedback on scientific publications to fully or partially automate peer reviews. For instance, Li et al. [152] propose a multi-task learning approach for peer review score prediction, where different aspect score prediction tasks (e.g., novelty) can inform each other. Ghosal et al. [87] leverage the concept of sentiment to predict scores based on review texts. In a similar vein, Bharti et al. [25] leverage paper–review interactions to predict final decisions of a review process. Wang et al. [272] focus on explainability during review score prediction for several review categories by constructing knowledge graphs (e.g., representing the background of a paper). More recent works have included generation of feedback texts into the problem setup. Bartoli and Medvet [18] frame the problem as exploring the potential of GPT-2

for conducting academic fraud by generating fake reviews. In contrast, Yuan et al. [300] ask whether it would be possible to automate reviewing leveraging targeted summarization models, a recently trending topic. Liu and Shah [173] explore prompting-based review generation with various LLMs, finding that GPT-4 performs best and that task granularity matters. Robertson [217] similarly finds GPT-4 to be “slightly” helpful for peer reviewing, and Liang et al. [162] demonstrate in a comparative study that users of a GPT-4–based peer review system found the feedback to be (very) helpful more than half the time. D’Arcy et al. [55] show a multi-agent approach with LLMs that engage in a discussion to produce better results than a single model.

Meta Review Generation. Kumar et al. [138] tackle meta-review generation using a multi-encoder transformer network, and Li et al. [155] use a multi-task learning approach for refining pre-trained language models for the task. Stappen et al. [243] explore the aggregation of reviews for providing additional computational decision support to editors based on uncertainty-aware methods like soft labeling. Both Zeng et al. [302] and Santu et al. [223] rely on LLMs, which they specifically prompt for the task. In contrast, Purkayastha et al. [206] propose a conversational agent that interactively supports meta-reviewers in their decision-making.

- 3.5.3 Domains of Application. Peer review setups vary in the aspects to review for, scoring schemes, expected review length, and the stages and dynamics of the reviewer–author and reviewer–reviewer discussions. Thus, while none of the studies presented above targets a problem unique to any scientific discipline, the particularities will likely be very different for each specific community and existing systems must be evaluated or adapted before deployment.
- 3.5.4 Limitations and Future Directions. The variety of scientific domains whose peer review has been studied is still limited. Most work relies on data from OpenReview, a platform used primarily by the representation learning and NLP communities; other disciplines may be wholly unrepresented in existing peer review datasets. Even within communities, there can be great variance in how peer reviews are conducted, which limits the comparability of approaches. Scientific rigor in particular remains unexplored, despite being a critical aspect of peer review; most existing studies rely on predefined rigor checklists that are not easily scalable or transferable across domains. Given these gaps, future research could benefit from exploring new domains of peer review, developing domain adaptation approaches, and advancing models for assessing scientific rigor. Reproducibility studies and larger benchmarks could further advance the field. Additionally, ethical concerns demand the prioritization of research on trustworthy AI support for peer review, ensuring that human experts retain autonomy in the process.


### 4 Ethical Concerns

There is by now a growing body of work addressing major ethical concerns related to generative AI. Baldassarre et al. [14], for instance, present a systematic literature review regarding the social impact of generative AI, especially taking into account 71 papers on ChatGPT. They identify privacy, inequality, bias, discrimination, and stereotypes as areas of concern. Another literature review on ethics and generative AI [96] identifies jailbreaking, hallucination, alignment, harmful content, copyright, private data leakage, and impacts on human creativity as topics of increasing interest. This review furthermore identifies 19 distinct clusters of ethics topics, with fairness/bias being the most frequently mentioned, followed by safety, harmful content/toxicity, hallucination, privacy, interaction risks, security/robustness on ranks two to six, with writing/research on rank 18. Ali and Aysan [3] review 364 recent papers on generative AI and ethics published from 2022 to 2024 in different domains including the use of generative AI in scientific research. Topics identified as critical to academia are authenticity, intellectual property, and academic integrity. Sun et al. [251] argue

that in application areas such as scientific research, ensuring the trustworthiness of LLMs is crucial. Dergaa et al. [59] find the use of AI chatbots in academic research heavily associated with stigma and propose mitigation strategies.

Truthfulness—i.e., the accurate representation of information, facts and results—is a particularly essential challenge for LLMs. Benchmarks and datasets developed to evaluate different aspects of it include TruthfulQA [168], HaluEval [151], and FELM [39], for identifying hallucinations; SelfAware [297] for assessing awareness of knowledge limitations; FreshQA [263] and Pinocchio [297] for exploring adaptability to rapidly evolving information; and TrustLLM [251], which incorporates existing and new datasets not just on truthfulness but also safety, fairness, robustness, privacy, and machine ethics. Evaluations with TrustLLM show that proprietary LLMs generally outperform open-source LLMs in trustworthiness, Llama2 [257] being a notable exception. However, proprietary LLMs (including Llama2) often struggle to provide truthful responses when relying solely on internal knowledge. Their performance does improve significantly with additional external knowledge, and there exists a positive correlation between trustworthiness and the functional effectiveness of the model in downstream tasks.

Editors of scientific publications are particularly challenged by the increasing proportion of AI-generated text in manuscripts [42, 93, 134, 164] and by its potential use in peer reviewing (cf. §3.5). The editors of the Journal of Information Technology have elaborated on the limitations and risks of using generative AI in the production of scientific publications [225], referring to an eight-point “Artificial Imperfections” test to illustrate current limitations of generative AI: AI is (1) brittle, (2) opaque, (3) greedy, (4) shallow and tone-deaf, (5) manipulative and hackable, (6) biased, (7) invasive, (8) “faking it” [281, p.107]. Nevertheless, they conclude that although AI should not be forbidden, authors must take full responsibility for its output and adhere to the “scientific principle of transparency” by giving full and transparent disclosure of their usage of AI, and moreover that “it is then up to the reviewers and editors to assess and make decisions on the specific use of that generative AI in a specific piece of research.” Guidelines proposed by the editors of iMeta similarly hold authors fully responsible for the integrity of their manuscripts, and for addressing ethical concerns and ensuring the accuracy and fairness of AI-generated content, complying with data protection and privacy laws, and considering the relevant copyright and intellectual property issues [205]. They furthermore state that AI-assisted technologies cannot be recognized as authors, that the use of generative AI must be transparently disclosed (including the prompts and specific versions of the tools used), that AI-generated images and multimedia should be accepted only when specifically allowed, and that the use of AI in the reviewing process is expressly prohibited.

### 5 Conclusion

In this paper, we surveyed approaches in the area of AI4Science, with a particular focus on recent large language model-based methods. We examined five key aspects of the research cycle: (1) search, (2) experimentation and research idea generation, (3) text-based content production, (4) multimodal content production, and (5) peer review. For each topic, we discussed relevant datasets, methods, and results, including evaluation strategies, while highlighting limitations and avenues for future research. Ethical concerns featured prominently in our survey, given the potential for misuse and challenges in maintaining scientific integrity in the face of AI-assisted content generation.

Overall, while recent advances suggest that AI systems can meaningfully support certain components of the scientific workflow, their current capabilities remain limited and uneven. Many methods rely on narrow benchmarks, struggle with generalization, or require substantial human oversight to avoid errors, bias, or misinterpretation. Consequently, AI4Science should presently be viewed as a complementary set of tools rather than a transformative replacement for human expertise. We hope that this survey inspires new initiatives in AI4Science, driving faster, more efficient, and more inclusive scientific discovery, experimentation, reporting and content synthesis—while upholding the highest

ethical standards. As the ultimate goal of science is to serve humanity, we hope these advancements will accelerate knowledge creation and enhance the accessibility and reliability of research, leading to improved healthcare, medical treatments, economic processes, among a myriad of other societal benefits.

### Acknowledgments

Yong Cao was supported by a VolkswagenStiftung Momentum grant. Jennifer D’Souza was supported by the SCINEXT project (BMBF, German Federal Ministry of Education and Research, Grant ID: 01lS22070). The NLLG Lab at UTN gratefully acknowledges support from the Federal Ministry of Education and Research (BMBF) via the research grant “Metrics4NLG” and the German Research Foundation (DFG) via the Heisenberg Grant EG 375/5-1. The work of Anne Lauscher is supported by the Excellence Strategy of the German Federal Government and the Federal States. Our AI use cases are documented in the supplemental material.

### References

- [1] Abbi Abdel-Rehim, Hector Zenil, Oghenejokpeme Orhobor, Marie Fisher, Ross J Collins, Elizabeth Bourne, Gareth W Fearnley, Emma Tate, Holly X Smith, Larisa N Soldatova, et al. 2025. Scientific hypothesis generation by large language models: laboratory validation in breast cancer treatment. J. Royal Soc. Interface 22, 227 (2025), 20240674.
- [2] Ahmed AbuRa’ed, Horacio Saggion, Alexander Shvets, and Àlex Bravo. 2020. Automatic related work section generation: experiments in scientific document abstracting. Scientometrics 125 (2020), 3159–3185.
- [3] Hassnian Ali and Ahmet Faruk Aysan. 2024. Ethical dimensions of generative AI: A cross-domain analysis using machine learning structural topic modeling. Int. J. Ethics Syst. 41, 1 (2024), 3–34.
- [4] Signe Altmäe, Alberto Sola-Leyva, and Andres Salumets. 2023. Artificial intelligence in scientific writing: a friend or a foe? Reproductive BioMedicine Online 47, 1 (2023), 3–9.
- [5] Maha Amami, Gabriella Pasi, Fabio Stella, and Rim Faiz. 2016. An lda-based approach to scientific paper recommendation. In Nat. Lang. Process. Inf. Syst. 21st Int. Conf. on Appl. Nat. Lang. to Inf. Syst. NLDB 2016. Springer, 200–210.
- [6] Isaac Ampomah, James Burton, Amir Enshaei, and Noura Al Moubayed. 2022. Generating Textual Explanations for Machine Learning Models Performance: A Table-to-Text Task. In Proc. 13th Lang. Resour. Eval. Conf., Nicoletta Calzolari, Frédéric Béchet, Philippe Blache, Khalid Choukri, Christopher Cieri, Thierry Declerck, Sara Goggi, Hitoshi Isahara, Bente Maegaard, Joseph Mariani, Hélène Mazo, Jan Odijk, and Stelios Piperidis (Eds.). 3542–3551.
- [7] Nash Anderson, Daniel L. Belavy, Stephen M. Perle, Sharief Hendricks, Luiz Hespanhol, Evert Verhagen, and Aamir R. Memon. 2023. AI did not write this manuscript, or did it? Can we trick the AI text detector into generated texts? The potential future of ChatGPT and AI in Sports & Exercise Medicine manuscript generation. BMJ Open Sport & Exerc. Med. 9, 1 (2023), e001568.
- [8] Ewa Andrejczuk, Julian Eisenschlos, Francesco Piccinno, Syrine Krichene, and Yasemin Altun. 2022. Table-to-text generation and pre-training with TabT5. In Find. Assoc. for Comput. Linguist. EMNLP 2022, Yoav Goldberg, Zornitsa Kozareva, and Yue Zhang (Eds.). 6758–6766.
- [9] Akari Asai, Jacqueline He, Rulin Shao, Weijia Shi, Amanpreet Singh, Joseph Chee Chang, Kyle Lo, Luca Soldaini, Sergey Feldman, Tian, D’arcy Mike, David Wadden, Matt Latzke, Minyang, Pan Ji, Shengyan Liu, Hao Tong, Bohao Wu, Yanyu Xiong, Luke Zettlemoyer, Dan Weld, Graham Neubig, Doug Downey, Wen-tau Yih, Pang Wei Koh, and Hannaneh Hajishirzi. 2024. OpenScholar: Synthesizing Scientific Literature with Retrieval-Augmented Language Models. arXiv:2411.14199
- [10] Akari Asai, Zeqiu Wu, Yizhong Wang, Avirup Sil, and Hannaneh Hajishirzi. 2024. Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection. In The Twelfth Int. Conf. on Learn. Represent..
- [11] Jinheon Baek, Sujay Kumar Jauhar, Silviu Cucerzan, and Sung Ju Hwang. 2025. ResearchAgent: Iterative research idea generation over scientific literature with large language models. In Proc. 2025 Conf. Nations Am. Chapter Assoc. for Comput. Linguist.. 6709–6738.
- [12] Jiaxin Bai, Yicheng Wang, Tianshi Zheng, Yue Guo, Xin Liu, and Yangqiu Song. 2024. Advancing Abductive Reasoning in Knowledge Graphs through Complex Logical Hypothesis Generation. In Proc. 62nd Annu. Meet. Assoc. for Comput. Linguist., Vol. 1. 1312–1329.
- [13] Yushi Bai, Jiajie Zhang, Xin Lv, Linzhi Zheng, Siqi Zhu, Lei Hou, Yuxiao Dong, Jie Tang, and Juanzi Li. 2024. LongWriter: Unleashing 10,000+ Word Generation from Long Context LLMs. In The Thirteen. Int. Conf. on Learn. Represent..
- [14] Maria Teresa Baldassarre, Danilo Caivano, Berenice Fernandez Nieto, Domenico Gigante, and Azzurra Ragone. 2023. The social impact of generative AI: An analysis on ChatGPT. In Proc. 2023 ACM Conf. on Inf. Technol. for Soc. Good. 363–373.
- [15] Sambaran Bandyopadhyay, Himanshu Maheshwari, Anandhavelu Natarajan, and Apoorv Saxena. 2024. Enhancing Presentation Slide Generation by LLMs with a Multi-Staged End-to-End Approach. In Proc. 17th Int. Nat. Lang. Gener. Conf.. 222–229.
- [16] Sachin Banker, Promothesh Chatterjee, Himanshu Mishra, and Arul Mishra. 2024. Machine-assisted social psychology hypothesis generation. Am. Psychol. 79, 6 (2024), 789.


- [17] Trapit Bansal, David Belanger, and Andrew McCallum. 2016. Ask the GRU: Multi-task learning for deep text recommendations. In Proc. 10th ACM Conf. on Recomm. Syst.. 107–114.
- [18] Alberto Bartoli and Eric Medvet. 2020. Exploring the Potential of GPT-2 for Generating Fake Reviews of Research Papers. In Proc. FSDM 2020, Antonio J. Tallón-Ballesteros (Ed.). 390–396.
- [19] Jonas Belouadi, Eddy Ilg, Margret Keuper, Hideki Tanaka, Masao Utiyama, Raj Dabre, Steffen Eger, and Simone Ponzetto. 2025. TikZero: Zero-shot text-guided graphics program synthesis. In Proc. IEEE/CVF Int. Conf. on Comput. Vis.. 17793–17806.
- [20] Jonas Belouadi, Anne Lauscher, and Steffen Eger. 2024. AutomaTikZ: Text-Guided Synthesis of Scientific Vector Graphics with TikZ. In Proc. Twelfth Int. Conf. on Learn. Represent..
- [21] Jonas Belouadi, Simone Paolo Ponzetto, and Steffen Eger. 2024. DeTikZify: Synthesizing Graphics Programs for Scientific Figures and Sketches with TikZ. In The Thirty-eighth Annu. Conf. on Neural Inf. Process. Syst..
- [22] Lamia Ben Ezzdine, Wissem Dhahbi, Ismail Dergaa, Halil İbrahim Ceylan, Noomen Guelmami, Helmi Ben Saad, Karim Chamari, Valentina Stefanica, and Abdelfatteh El Omri. 2025. Physical activity and neuroplasticity in neurodegenerative disorders: a comprehensive review of exercise interventions, cognitive training, and AI applications. Front. Neurosci. 19 (2025), 1502417.
- [23] Chandra Bhagavatula, Sergey Feldman, Russell Power, and Waleed Ammar. 2018. Content-Based Citation Recommendation. In Proc. 2018 Conf. North Am. Chapter Assoc. for Comput. Linguist., Marilyn Walker, Heng Ji, and Amanda Stent (Eds.). 238–251.
- [24] Prabhat Bharti, Meith Navlakha, Mayank Agarwal, and Asif Ekbal. 2023. PolitePEER: Does peer review hurt? A dataset to gauge politeness intensity in the peer reviews. Lang. Resour. Eval. (2023), 1–23.
- [25] Prabhat Kumar Bharti, Shashi Ranjan, Tirthankar Ghosal, Mayank Agrawal, and Asif Ekbal. 2021. PEERAssist: Leveraging on Paper-Review Interactions to Predict Peer Review Decisions. In Towards Open Trust. Digit. Soc.. 421–435.
- [26] Christine L. Borgman. 2007. Scholarship in the Digital Age: Information, Infrastructure, and the Internet. MIT Press.
- [27] Lutz Bornmann, Robin Haunschild, and Rüdiger Mutz. 2021. Growth Rates of Modern Science: a Latent Piecewise Growth Curve Approach to Model Publication Numbers from Established and New Literature Databases. Humanit. Soc. Sci. Commun. 8, 224 (2021).
- [28] Jennifer A. Byrne. 2016. Improving the Peer Review of Narrative Literature Reviews. Res. Integr. Peer Rev. 1, 12 (2016).
- [29] Fengyu Cai, Xinran Zhao, Tong Chen, Sihao Chen, Hongming Zhang, Iryna Gurevych, and Heinz Koeppl. 2024. MixGR: Enhancing Retriever Generalization for Scientific Domain through Complementary Granularity. In Proc. 2024 Conf. on Empir. Methods Nat. Lang. Process.. 10369–10391.
- [30] Andres Castellanos-Gomez. 2023. Good practices for scientific article writing with ChatGPT and other artificial intelligence language models. Nanomanufacturing 3, 2 (2023), 135–138.
- [31] Miaosen Chai, Emily Herron, Erick Cervantes, and Tirthankar Ghosal. 2024. Exploring Scientific Hypothesis Generation with Mamba. In Proc. 1st Workshop on NLP for Sci.. 197–207.
- [32] Souvic Chakraborty, Pawan Goyal, and Animesh Mukherjee. 2020. Aspect-based Sentiment Analysis of Scientific Reviews. In Proc. ACM/IEEE Jt. Conf. on Digit. Libr. 2020. 207–216.
- [33] Iain Chalmers, Larry V. Hedges, and Harris Cooper. 2002. A Brief History of Research Synthesis. Eval. & Health Prof. 25, 1 (2002), 12–37.
- [34] Chu Sern Joel Chan, Aakanksha Naik, Matthew Akamatsu, Hanna Bekele, Erin Bransom, Ian Campbell, and Jenna Sparks. 2024. Overview of the Context24 Shared Task on Contextualizing Scientific Claims. In Proc. Fourth Workshop on Sch. Document Process.. 12–21.
- [35] A. Checco, L. Bracciale, P. Loreti, S. Pinfield, and G. Bianchi. 2021. AI-assisted peer review. Humanit. Soc. Sci. Commun. 8, 1 (January 2021), 1–11.
- [36] Chen Chen, Ayman Maqsood, Zhuang Zhang, Xiaobing Wang, Linrui Duan, Huanhuan Wang, Tianyang Chen, Siyu Liu, Qiutong Li, Jingshan Luo, et al. 2024. The use of ChatGPT to generate experimentally testable hypotheses for improving the surface passivation of perovskite solar cells. Cell Reports Phys. Sci. (2024).
- [37] Hong Chen, Hiroya Takamura, and Hideki Nakayama. 2021. SciXGen: A Scientific Paper Dataset for Context-Aware Text Generation. In Find. Assoc. for Comput. Linguist. EMNLP 2021, Marie-Francine Moens, Xuanjing Huang, Lucia Specia, and Scott Wen-tau Yih (Eds.). 1483–1492.
- [38] Kexin Chen, Jiamin Lu, Junyou Li, Xiaoran Yang, Yuyang Du, Kunyi Wang, Qiannuan Shi, Jiahui Yu, Lanqing Li, Jiezhong Qiu, et al. 2023. Chemist-X: Large language model-empowered agent for reaction condition recommendation in chemical synthesis. arXiv:2311.10776
- [39] Shiqi Chen, Yiran Zhao, Jinghan Zhang, I-Chun Chern, Siyang Gao, Pengfei Liu, and Junxian He. 2023. FELM: Benchmarking Factuality Evaluation of Large Language Models. In Adv. Neural Inf. Process. Syst. 36, Alice Oh, Tristan Naumann, Amir Globerson, Kate Saenko, Moritz Hardt, and Sergey Levine (Eds.).
- [40] Yanran Chen and Steffen Eger. 2023. Transformers Go for the LOLs: Generating (Humourous) Titles from Scientific Abstracts End-to-End. In Proc. 4th Workshop on Eval. Comp. NLP Syst., Daniel Deutsch, Rotem Dror, Steffen Eger, Yang Gao, Christoph Leiter, Juri Opitz, and Andreas Rücklé (Eds.). 62–84.
- [41] Ziru Chen, Shijie Chen, Yuting Ning, Qianheng Zhang, Boshi Wang, Botao Yu, Yifei Li, Zeyi Liao, Chen Wei, Zitong Lu, Vishal Dey, Mingyi Xue, Frazier N. Baker, Benjamin Burns, Daniel Adu-Ampratwum, Xuhui Huang, Xia Ning, Song Gao, Yu Su, and Huan Sun. 2024. ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery. arXiv:2410.05080
- [42] Huzi Cheng, Bin Sheng, Aaron Lee, Varun Chaudhary, Atanas G Atanasov, Nan Liu, Yue Qiu, Tien Yin Wong, Yih-Chung Tham, and Ying-Feng Zheng. 2024. Have AI-Generated Texts from LLM Infiltrated the Realm of Scientific Writing? A Large-Scale Analysis of Preprint Platforms. bioRxiv

(2024), 2024–03.

- [43] Liying Cheng, Lidong Bing, Qian Yu, Wei Lu, and Luo Si. 2020. APE: Argument Pair Extraction from Peer Review and Rebuttal via Multi-task Learning. In Proc. 2020 Conf. on Empir. Methods Nat. Lang. Process.. 7000–7011.


- [44] Zhoujun Cheng, Haoyu Dong, Zhiruo Wang, Ran Jia, Jiaqi Guo, Yan Gao, Shi Han, Jian-Guang Lou, and Dongmei Zhang. 2022. HiTab: A Hierarchical Table Dataset for Question Answering and Natural Language Generation. In Proc. 60th Annu. Meet. Assoc. for Comput. Linguist., Smaranda Muresan, Preslav Nakov, and Aline Villavicencio (Eds.). 1094–1110.
- [45] Yizhou Chi, Yizhang Lin, Sirui Hong, Duyi Pan, Yaying Fei, Guanghao Mei, Bangbang Liu, Tianqi Pang, Jacky Kwok, Ceyao Zhang, et al. 2024. SELA: Tree-Search Enhanced LLM Agents for Automated Machine Learning. arXiv:2410.17238
- [46] Gautam Choudhary, Natwar Modani, and Nitish Maurya. 2021. ReAct: A Review Comment Dataset for Actionability (and more). In Web Inf. Syst. Eng. – WISE 2021. 336–343.
- [47] John Clement. 1989. Learning via Model Construction and Criticism: Protocol Evidence on Sources of Creativity in Science. In Handbook of Creativity: Assessment, Theory and Research, John A. Glover, Royce R. Ronning, and Cecil R. Reynolds (Eds.). Plenum, 341–381.
- [48] John J. Clement. 2022. Multiple Levels of Heuristic Reasoning Processes in Scientific Model Construction. Front. Psychol. 13 (2022).
- [49] Arman Cohan, Iz Beltagy, Daniel King, Bhavana Dalvi, and Daniel S Weld. 2019. Pretrained language models for sequential sentence classification. arXiv:1909.04054
- [50] Arman Cohan, Sergey Feldman, Iz Beltagy, Doug Downey, and Daniel Weld. 2020. SPECTER: Document-level Representation Learning using Citation-informed Transformers. In Proc. 58th Annu. Meet. Assoc. for Comput. Linguist., Dan Jurafsky, Joyce Chai, Natalie Schluter, and Joel Tetreault (Eds.). 2270–2282.
- [51] Alessandro Conti, Enrico Fini, Paolo Rota, Yiming Wang, Massimiliano Mancini, and Elisa Ricci. 2024. Automatic benchmarking of large multimodal models via iterative experiment programming. arXiv:2406.12321
- [52] Cristina Cornelio, Sanjeeb Dash, Vernon Austel, Tyler R. Josephson, Joao Goncalves, Kenneth L. Clarkson, Nimrod Megiddo, Bachir El Khadir, and Lior Horesh. 2023. Combining Data and Theory for Derivable Scientific Discovery with AI-Descartes. Nat. Commun. 14, 1777 (2023).
- [53] Paul Covington, Jay Adams, and Emre Sargin. 2016. Deep neural networks for YouTube recommendations. In Proc. 10th ACM Conf. on Recomm. Syst.. 191–198.
- [54] Zhiqing Cui, Jiahao Yuan, Hanqing Wang, Yanshu Li, Chenxu Du, and Zhenglong Ding. 2025. Draw with Thought: Unleashing Multimodal Reasoning for Scientific Diagram Generation. In Proc. 33rd ACM Int. Conf. on Multimed.. 5050–5059.
- [55] Mike D’Arcy, Tom Hope, Larry Birnbaum, and Doug Downey. 2024. MARG: Multi-Agent Review Generation for Scientific Papers. arXiv:2401.04259
- [56] Mike D’Arcy, Alexis Ross, Erin Bransom, Bailey Kuehl, Jonathan Bragg, Tom Hope, and Doug Downey. 2023. ARIES: A Corpus of Scientific Paper Edits Made in Response to Peer Reviews. arXiv:2306.12587
- [57] Zheye Deng, Chunkit Chan, Weiqi Wang, Yuxi Sun, Wei Fan, Tianshi Zheng, Yauwai Yim, and Yangqiu Song. 2024. Text-Tuple-Table: Towards Information Integration in Text-to-Table Generation via Global Tuple Extraction. In Proc. 2024 Conf. on Empir. Methods Nat. Lang. Process.. 9300–9322.
- [58] Zekun Deng, Zixin Zeng, Weiye Gu, Jiawen Ji, and Bolin Hua. 2021. Automatic Related Work Section Generation by Sentence Extraction and Reordering. In Proc. 1st Workshop on AI + Informetrics.
- [59] Ismail Dergaa, Feten Fekih-Romdhane, Jordan M Glenn, Mohamed Saifeddin Fessi, Karim Chamari, Wissem Dhahbi, Makram Zghibi, Nicola Luigi Bragazzi, Mohamed Ben Aissa, Noomen Guelmami, et al. 2023. Moving beyond the stigma: understanding and overcoming the resistance to the acceptance and adoption of artificial intelligence chatbots. New Asian J. Med. 1, 2 (2023), 29–36.
- [60] Danilo Dessí, Francesco Osborne, Diego Reforgiato Recupero, Davide Buscaldi, and Enrico Motta. 2022. CS-KG: A large-scale knowledge graph of research entities and claims in computer science. In Int. Semantic Web Conf.. 678–696.
- [61] Alphaeus Dmonte, Roland Oruche, Marcos Zampieri, Prasad Calyam, and Isabelle Augenstein. 2024. Claim Verification in the Age of Large Language Models: A Survey. arXiv:2408.14317
- [62] Haoyu Dong, Mengkang Hu, Qinyu Xu, Haochen Wang, and Yue Hu. 2024. OpenTE: Open-Structure Table Extraction From Text. In IEEE Int. Conf. on Acoust. Speech Signal Process. ICASSP 2024. IEEE, 10306–10310.
- [63] Iddo Drori and Dov Te’eni. 2024. Human-in-the-Loop AI Reviewing: Feasibility, Opportunities, and Risks. J. Assoc. for Inf. Syst. 25, 1 (2024), 98–109.
- [64] John A. Drozdz and Michael R. Ladomery. 2024. The Peer Review Process: Past, Present, and Future. Br. J. Biomed. Sci. 81 (2024).
- [65] Jennifer D’Souza, Sören Auer, and Ted Pedersen. 2021. SemEval-2021 Task 11: NLPContributionGraph - Structuring Scholarly NLP Contributions for a Research Knowledge Graph. In Proc. 15th Int. Workshop on Semantic Eval. (SemEval-2021), Alexis Palmer, Nathan Schneider, Natalie Schluter, Guy Emerson, Aurelie Herbelot, and Xiaodan Zhu (Eds.). 364–376.
- [66] Nils Dycke, Ilia Kuznetsov, and Iryna Gurevych. 2023. NLPeer: A Unified Resource for the Computational Study of Peer Review. In Proc. 61st Annu. Meet. Assoc. for Comput. Linguist., Anna Rogers, Jordan Boyd-Graber, and Naoaki Okazaki (Eds.), Vol. 1. 5049–5073.
- [67] Daniel Nygård Ege, Mark Goudswaard, James Gopsill, Ben Hicks, and Martin Steinert. 2024. IDEA Challenge 2022 Dataset: Prototypes from a Design Hackathon. Data Brief 54 (2024), 110363. doi:10.1016/j.dib.2024.110363
- [68] Aryaz Eghbali and Michael Pradel. 2023. CrystalBLEU: Precisely and Efficiently Measuring the Similarity of Code. In Proc. 37th IEEE/ACM Int. Conf. on Autom. Softw. Eng.. Article 28.
- [69] Holly Else. 2023. Abstracts written by ChatGPT fool scientists. Nature 613 (2023), 423.
- [70] Thomas Elsken, Jan Hendrik Metzen, and Frank Hutter. 2019. Neural architecture search: A survey. J. Mach. Learn. Res. 20, 55 (2019), 1–21.
- [71] Faiza Farhat, Shahab Saquib Sohail, and Dag Øivind Madsen. 2023. How trustworthy is ChatGPT? The case of bibliometric analyses. Cogent Eng. 10, 1 (2023), 2222988.
- [72] Ronald A. Fisher. 1925. Statistical Methods for Research Workers. Oliver and Boyd.


- [73] Ronald A. Fisher. 1935. The Design of Experiments. Oliver and Boyd.
- [74] Michael Fromm, Evgeniy Faerman, Max Berrendorf, Siddharth Bhargava, Ruoxia Qi, Yao Zhang, Lukas Dennert, Sophia Selle, Yang Mao, and Thomas Seidl. 2021. Argument Mining Driven Analysis of Peer-Reviews. Proc. AAAI Conf. on Artif. Intell. 35, 6 (2021), 4758–4766.
- [75] Stephanie Fu, Netanel Tamir, Shobhita Sundaram, Lucy Chai, Richard Zhang, Tali Dekel, and Phillip Isola. 2023. DreamSim: Learning New Dimensions of Human Visual Similarity using Synthetic Data. In Adv. Neural Inf. Process. Syst. 36, Alice Oh, Tristan Naumann, Amir Globerson, Kate Saenko, Moritz Hardt, and Sergey Levine (Eds.).
- [76] Tsu-Jui Fu, William Yang Wang, Daniel J. McDuff, and Yale Song. 2021. DOC2PPT: Automatic Presentation Slides Generation from Scientific Documents. In AAAI Conf. on Artif. Intell..
- [77] Martin Funkquist, Ilia Kuznetsov, Yufang Hou, and Iryna Gurevych. 2023. CiteBench: A Benchmark for Scientific Citation Text Generation. In Proc. 2023 Conf. on Empir. Methods Nat. Lang. Process.. 7337–7353.
- [78] Timur Galimzyanov, Sergey Titov, Yaroslav Golubev, and Egor Bogomolov. 2025. Drawing pandas: A benchmark for llms in generating plotting code. In 2025 IEEE/ACM 22nd Int. Conf. on Min. Softw. Repos.. IEEE, 503–507.
- [79] Catherine A. Gao, Frederick M. Howard, Nikolay S Markov, Emma C. Dyer, Siddhi Ramesh, Yuan Luo, and Alexander T. Pearson. 2023. Comparing scientific abstracts generated by ChatGPT to real abstracts with detectors and blinded human reviewers. NPJ Digit. Med. 6, 1 (2023), 75.
- [80] Mingqi Gao, Xinyu Hu, Xunjian Yin, Jie Ruan, Xiao Pu, and Xiaojun Wan. 2025. LLM-based NLG evaluation: Current status and challenges. Comput. Linguist. (2025), 1–27.
- [81] Andres Garcia-Silva, Cristian Berrio, and Jose Manuel Gomez-Perez. 2024. SPACE-IDEAS: A Dataset for Salient Information Detection in Space Innovation. In Proc. 2024 Jt. Int. Conf. on Comput. Linguist. Lang. Resour. Eval.. 15087–15092.
- [82] Eugene Garfield. 1955. Citation Indexes for Science. Science 122, 3159 (1955), 108–111.
- [83] Jiaxin Ge, Zora Zhiruo Wang, Xuhui Zhou, Yi-Hao Peng, Sanjay Subramanian, Qinyue Tan, Maarten Sap, Alane Suhr, Daniel Fried, Graham Neubig, et al. 2025. Autopresent: Designing structured visuals from scratch. In Proc. Comput. Vis. Pattern Recognit. Conf.. 2902–2911.
- [84] Alireza Ghafarollahi and Markus J Buehler. 2025. SciAgents: automating scientific discovery through bioinspired multi-agent intelligent graph reasoning. Adv. Mater. 37, 22 (2025), 2413523.
- [85] Tirthankar Ghosal, Sandeep Kumar, Prabhat Kumar Bharti, and Asif Ekbal. 2022. Peer review analyze: A novel benchmark resource for computational analysis of peer reviews. PLOS One 17, 1 (01 2022), 1–29.
- [86] Tirthankar Ghosal, Kamal Kaushik Varanasi, and Valia Kordoni. 2022. HedgePeer: A dataset for uncertainty detection in peer reviews. In Proc. 22nd ACM/IEEE Jt. Conf. on Digit. Libr.. 1–5.
- [87] Tirthankar Ghosal, Rajeev Verma, Asif Ekbal, and Pushpak Bhattacharyya. 2019. DeepSentiPeer: Harnessing Sentiment in Review Texts to Recommend Peer Review Decisions. In Proc. 57th Annu. Meet. Assoc. for Comput. Linguist.. 1120–1130.
- [88] Hamed Babaei Giglou, Jennifer D’Souza, and Sören Auer. 2024. LLMs4Synthesis: Leveraging Large Language Models for Scientific Synthesis. In 2024 ACM/IEEE Jt. Conf. on Digit. Libr.. 1–12.
- [89] Max Glockner, Yufang Hou, Preslav Nakov, and Iryna Gurevych. 2024. Grounding Fallacies Misrepresenting Scientific Publications in Evidence. arXiv:2408.12812
- [90] Max Glockner, Yufang Hou, Preslav Nakov, and Iryna Gurevych. 2024. MISSCI: Reconstructing Fallacies in Misrepresented Science. In Proc. 62nd Annu. Meet. Assoc. for Comput. Linguist.. 4372–4405.
- [91] Juraj Gottweis, Wei-Hung Weng, Alexander Daryin, Tao Tu, Anil Palepu, Petar Sirkovic, Artiom Myaskovsky, Felix Weissenberger, Keran Rong, Ryutaro Tanno, et al. 2025. Towards an AI co-scientist. arXiv:2502.18864
- [92] Andrew V Gougherty and Hannah L Clipp. 2024. Testing the reliability of an AI-based large language model to extract ecological information from the scientific literature. npj Biodivers. 3, 1 (2024), 13.
- [93] Andrew Gray. 2024. ChatGPT “contamination”: estimating the prevalence of LLMs in the scholarly literature. arXiv:2403.16887
- [94] Christian Greisinger and Steffen Eger. 2026. TikZilla: Scaling Text-to-TikZ with High-Quality Data and Reinforcement Learning. In Proc. Fourteenth Int. Conf. on Learn. Represent.. In press.
- [95] Yanzhu Guo, Guokan Shang, Virgile Rennard, Michalis Vazirgiannis, and Chloé Clavel. 2023. Automatic Analysis of Substantiation in Scientific Peer Reviews. In Find. Assoc. for Comput. Linguist. EMNLP 2023. 10198–10216.
- [96] Thilo Hagendorff. 2024. Mapping the ethics of generative AI: A comprehensive scoping review. arXiv:2402.08323
- [97] James Hartley. 2008. Academic Writing and Publishing: A Practical Handbook. Routledge.
- [98] Zahra Hashemi, Zhiqiang Zhong, Jun Pang, and Wei Zhao. 2026. Malicious Repurposing of Open Science Artefacts by Using Large Language Models. arXiv:2601.18998
- [99] Janna Hastings. 2023. AI for Scientific Discovery. CRC PRess.
- [100] Jiyan He, Weitao Feng, Yaosen Min, Jingwei Yi, Kunsheng Tang, Shuai Li, Jie Zhang, Kejiang Chen, Wenbo Zhou, Xing Xie, et al. 2023. Control risk for potential misuse of artificial intelligence in science. arXiv:2312.06632
- [101] Xin He, Kaiyong Zhao, and Xiaowen Chu. 2021. AutoML: A survey of the state-of-the-art. Knowledge-based Syst. 212 (2021), 106622.
- [102] Yichen He, Guanhua Huang, Peiyuan Feng, Yuan Lin, Yuchen Zhang, Hang Li, and Weinan E. 2025. PaSa: An LLM Agent for Comprehensive Academic Paper Search. In Proc. 63rd Annu. Meet. Assoc. for Comput. Linguist., Wanxiang Che, Joyce Nabende, Ekaterina Shutova, and Mohammad Taher Pilehvar (Eds.). 11663–11679.


- [103] Jack Hessel, Ari Holtzman, Maxwell Forbes, Ronan Le Bras, and Yejin Choi. 2021. CLIPScore: A Reference-free Evaluation Metric for Image Captioning. In Proc. 2021 Conf. on Empir. Methods Nat. Lang. Process., Marie-Francine Moens, Xuanjing Huang, Lucia Specia, and Scott Wen-tau Yih (Eds.). 7514–7528.
- [104] Tony Hey, Stewart Tansley, and Kristin Tolle. 2009. Jim Gray on eScience: a Transformed Scientific Method. In The Fourth Paradigm: Data-Intensive Scientific Discovery, Tony Hey, Stewart Tansley, and Kristin Tolle (Eds.). Microsoft Research.
- [105] Cong Duy Vu Hoang and Min-Yen Kan. 2010. Towards Automated Related Work Summarization. In COLING 2010: Posters, Chu-Ren Huang and Dan Jurafsky (Eds.). 427–435.
- [106] Sally Hopewell, Mike Clarke, David Moher, Elizabeth Wager, Philippa Middleton, Douglas G. Altman, Kenneth F. Schulz, and Consort Group. 2008. CONSORT for reporting randomized controlled trials in journal and conference abstracts: explanation and elaboration. PLoS medicine 5, 1 (2008), e20.
- [107] Yufang Hou, Charles Jochim, Martin Gleize, Francesca Bonin, and Debasis Ganguly. 2019. Identification of Tasks, Datasets, Evaluation Metrics, and Numeric Scores for Scientific Leaderboards Construction. In Proc. 57th Annu. Meet. Assoc. for Comput. Linguist., Anna Korhonen, David Traum, and Lluís Màrquez (Eds.). 5203–5213.
- [108] Xiang Hu, Hongyu Fu, Jinge Wang, Yifeng Wang, Zhikun Li, Renjun Xu, Yu Lu, Yaochu Jin, Lili Pan, and Zhenzhong Lan. 2024. Nova: An Iterative Planning and Search Approach to Enhance Novelty and Diversity of LLM Generated Ideas. arXiv:2410.14255
- [109] Yue Hu and Xiaojun Wan. 2013. PPSGen: Learning to Generate Presentation Slides for Academic Papers. In Int. Jt. Conf. on Artif. Intell..
- [110] Yue Hu and Xiaojun Wan. 2014. Automatic generation of related work sections in scientific papers: an optimization approach. In Proc. 2014 Conf. on Empir. Methods Nat. Lang. Process.. 1624–1633.
- [111] Xinyu Hua, Mitko Nikolov, Nikhil Badugu, and Lu Wang. 2019. Argument Mining for Understanding Peer Reviews. In Proc. 2019 Conf. North Am. Chapter Assoc. for Comput. Linguist.. 2131–2137.
- [112] Jie Huang and Kevin Chen-Chuan Chang. 2023. Citation: A key to building responsible and accountable large language models. arXiv:2307.02185
- [113] Qian Huang, Jian Vora, Percy Liang, and Jure Leskovec. 2024. MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation. In Forty-first Int. Conf. on Mach. Learn..
- [114] Shengzhi Huang, Qicong Wang, Wei Lu, Lingyu Liu, Zhenzhen Xu, and Yong Huang. 2025. PaperEval: A universal, quantitative, and explainable paper evaluation method powered by a multi-agent system. Inf. Process. & Manag. 62, 6 (2025), 104225.
- [115] Taesoon Hwang, Nishant Aggarwal, Pir Zarak Khan, Thomas Roberts, Amir Mahmood, Madlen M Griffiths, Nick Parsons, and Saboor Khan. 2024. Can ChatGPT assist authors with abstract writing in medical journals? Evaluating the quality of scientific abstracts generated by ChatGPT and original abstracts. Plos one 19, 2 (2024), e0297701.
- [116] Joseph James, Chenghao Xiao, Yucheng Li, and Chenghua Lin. 2024. On the Rigour of Scientific Writing: Criteria, Analysis, and Insights. In Find. Assoc. for Comput. Linguist. EMNLP 2024. 6523–6538.
- [117] Peter Jansen, Oyvind Tafjord, Marissa Radensky, Pao Siangliulue, Tom Hope, Bhavana Dalvi, Bodhisattwa Prasad Majumder, Daniel S Weld, and Peter Clark. 2025. Codescientist: End-to-end semi-automated scientific discovery with code-based experimentation. In Find. Assoc. for Comput. Linguist. ACL 2025. 13370–13467.
- [118] Peiwen Jiang, Xinbo Lin, Zibo Zhao, Ruhui Ma, Yvonne Jie Chen, and Jinhua Cheng. 2024. TKGT: Redefinition and A New Way of Text-to-Table Tasks Based on Real World Demands and Knowledge Graphs Augmented LLMs. In Proc. 2024 Conf. on Empir. Methods Nat. Lang. Process.. 16112–16126.
- [119] Carlos E Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, and Karthik R Narasimhan. 2024. SWE-bench: Can Language Models Resolve Real-world Github Issues?. In The Twelfth Int. Conf. on Learn. Represent..
- [120] Xia Jing, James J Cimino, Vimla L Patel, Yuchun Zhou, Jay H Shubrook, Chang Liu, and Sonsoles De Lacalle. 2024. Data-Driven Hypothesis Generation in Clinical Research: What We Learned from a Human Subject Study? Med. Res. Arch. 12, 2 (2024).
- [121] Léane Jourdan, Florian Boudin, Richard Dufour, Nicolas Hernandez, and Akiko Aizawa. 2025. ParaRev: Building a dataset for Scientific Paragraph Revision annotated with revision instruction. In Proc. First Workshop on Writ. Aids at Crossroads AI, Cogn. Sci. NLP. 35–44.
- [122] Léane Isabelle Jourdan, Florian Boudin, Nicolas Hernandez, and Richard Dufour. 2024. CASIMIR: A Corpus of Scientific Articles Enhanced with Multiple Author-Integrated Revisions. In Proc. 2024 Jt. Int. Conf. on Comput. Linguist. Lang. Resour. Eval., Nicoletta Calzolari, Min-Yen Kan, Veronique Hoste, Alessandro Lenci, Sakriani Sakti, and Nianwen Xue (Eds.). 2883–2892.
- [123] Samira Ebrahimi Kahou, Adam Atkinson, Vincent Michalski, Ákos Kádár, Adam Trischler, and Yoshua Bengio. 2018. FigureQA: An Annotated Figure Dataset for Visual Reasoning. arXiv:1710.07300
- [124] Dongyeop Kang, Waleed Ammar, Bhavana Dalvi, Madeleine van Zuylen, Sebastian Kohlmeier, Eduard Hovy, and Roy Schwartz. 2018. A Dataset of Peer Reviews (PeerRead): Collection, Insights and NLP Applications. In Proc. 2018 Conf. North Am. Chapter Assoc. for Comput. Linguist.. 1647–1661.
- [125] SeongKu Kang, Yunyi Zhang, Pengcheng Jiang, Dongha Lee, Jiawei Han, and Hwanjo Yu. 2024. Taxonomy-guided Semantic Indexing for Academic Paper Search. In Proc. 2024 Conf. on Empir. Methods Nat. Lang. Process.. 7169–7184.
- [126] Wei-Yu Kao and An-Zi Yen. 2024. How We Refute Claims: Automatic Fact-Checking through Flaw Identification and Explanation. In Companion Proc. ACM on Web Conf. 2024. 758–761.
- [127] Marcin Kardas, Piotr Czapla, Pontus Stenetorp, Sebastian Ruder, Sebastian Riedel, Ross Taylor, and Robert Stojnic. 2020. AxCell: Automatic Extraction of Results from Machine Learning Papers. In Proc. 2020 Conf. on Empir. Methods Nat. Lang. Process., Bonnie Webber, Trevor Cohn, Yulan He, and Yang Liu (Eds.). 8580–8594.


- [128] Aniruddha Kembhavi, Mike Salvato, Eric Kolve, Minjoon Seo, Hannaneh Hajishirzi, and Ali Farhadi. 2016. A Diagram is Worth a Dozen Images. In Comput. Vision: ECCV 2016. 235–251.
- [129] Neha Nayak Kennard, Tim O’Gorman, Rajarshi Das, Akshay Sharma, Chhandak Bagchi, Matthew Clinton, Pranay Kumar Yelugam, Hamed Zamani, and Andrew McCallum. 2022. DISAPERE: A Dataset for Discourse Structure in Peer Review Discussions. In Proc. NAACL. 1234–1249.
- [130] M. M. Kessler. 1963. Bibliographic coupling between scientific papers. Am. Documentation 14, 1 (1963), 10–25.
- [131] Seong-Gon Kim. 2023. Using ChatGPT for language editing in scientific articles. Maxillofac. Plast. Reconstr. Surg. 45, 1 (2023), 13.
- [132] William R. King and Jun He. 2005. Understanding the Role and Methods of Meta-Analysis in IS Research. Commun. Assoc. for Inf. Syst. 16 (2005), 665–686.
- [133] Roger E. Kirk. 2009. Experimental Design. In The SAGE Handbook of Quantitative Methods in Psychology, Roger E. Millsap and Alberto MaydeuOlivares (Eds.). 23–45.
- [134] Dmitry Kobak, Rita González-Márquez, Emőke-Ágnes Horvát, and Jan Lause. 2024. Delving into ChatGPT usage in academic writing through excess vocabulary. arXiv:2406.07016
- [135] Jing Yu Koh, Stephen McAleer, Daniel Fried, and Ruslan Salakhutdinov. 2024. Tree Search for Language Model Agents. arXiv:2407.01476
- [136] Buse Sibel Korkmaz and Antonio Del Rio Chanona. 2024. Integrating Table Representations into Large Language Models for Improved Scholarly Document Comprehension. In Proc. Fourth Workshop on Sch. Document Process.. 293–306.
- [137] Kayvan Kousha and Mike Thelwall. 2024. Artificial intelligence to support publishing and peer review: A summary and review. Learn. Publ. 37, 1

(2024), 4–12.

- [138] Asheesh Kumar, Tirthankar Ghosal, and Asif Ekbal. 2021. A Deep Neural Architecture for Decision-Aware Meta-Review Generation. In 2021 ACM/IEEE Jt. Conf. on Digit. Libr.. 222–225.
- [139] Shrinidhi Kumbhar, Venkatesh Mishra, Kevin Coutinho, Divij Handa, Ashif Iquebal, and Chitta Baral. 2025. Hypothesis generation for materials discovery and design using goal-driven and constraint-guided LLM agents. arXiv:2501.13299
- [140] Nino Künzli, Anke Berger, Katarzyna Czabanowska, Raquel Lucas, Andrea Madarasova Geckova, Sarah Mantwill, and Olaf von Dem Knesebeck.

2022. «I Do Not Have Time» - Is This the End of Peer Review in Public Health Sciences? Public Health Rev. 43 (2022).

- [141] Ilia Kuznetsov, Osama Mohammed Afzal, Koen Dercksen, Nils Dycke, Alexander Goldberg, Tom Hope, Dirk Hovy, Jonathan K Kummerfeld, Anne Lauscher, Kevin Leyton-Brown, et al. 2024. What Can Natural Language Processing Do for Peer Review? arXiv:2405.06563
- [142] Ilia Kuznetsov, Jan Buchmann, Max Eichler, and Iryna Gurevych. 2022. Revise and Resubmit: An Intertextual Model of Text-based Collaboration in Peer Review. Comput. Linguist. 48, 4 (12 2022), 949–986.
- [143] Jon M. Laurent, Joseph D. Janizek, Michael Ruzo, Michaela M. Hinks, Michael J. Hammerling, Siddharth Narayanan, Manvitha Ponnapati, Andrew D White, and Samuel G. Rodriques. 2024. Lab-bench: Measuring capabilities of language models for biology research. arXiv:2407.10362
- [144] Po-Shen Lee, Jevin D. West, and Bill Howe. 2016. Viziometrics: Analyzing Visual Information in the Scientific Literature. IEEE Trans. on Big Data 4

(2016), 117–129.

- [145] Yukyung Lee, Joonghoon Kim, Jaehee Kim, Hyowon Cho, Jaewook Kang, Pilsung Kang, and Najoung Kim. 2025. Checkeval: A reliable llm-as-a-judge framework for evaluating text generation using checklists. In Proc. 2025 Conf. on Empir. Methods Nat. Lang. Process.. 15782–15809.
- [146] Christoph Leiter, Jonas Belouadi, Yanran Chen, Ran Zhang, Daniil Larionov, Aida Kostikova, and Steffen Eger. 2024. NLLG Quarterly arXiv Report 09/24: What are the most influential current AI Papers? arXiv:2412.12121
- [147] Adrian Letchford, Helen Susannah Moat, and Tobias Preis. 2015. The Advantage of Short Paper Titles. Royal Soc. Open Sci. 2, 8 (2015).
- [148] Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, et al. 2020. Retrieval-augmented generation for knowledge-intensive NLP tasks. In Proc. NeurIPS, Vol. 33. 9459–9474.
- [149] Dawei Li, Bohan Jiang, Liangjie Huang, Alimohammad Beigi, Chengshuai Zhao, Zhen Tan, Amrita Bhattacharjee, Yuxuan Jiang, Canyu Chen, Tianhao Wu, et al. 2025. From generation to judgment: Opportunities and challenges of LLM-as-a-judge. In Proc. 2025 Conf. on Empir. Methods Nat. Lang. Process.. 2757–2791.
- [150] Da-Wei Li, Danqing Huang, Tingting Ma, and Chin-Yew Lin. 2021. Towards Topic-Aware Slide Generation For Academic Papers With Unsupervised Mutual Learning. In AAAI Conf. on Artif. Intell..
- [151] Junyi Li, Xiaoxue Cheng, Xin Zhao, Jian-Yun Nie, and Ji-Rong Wen. 2023. HaluEval: A Large-Scale Hallucination Evaluation Benchmark for Large Language Models. In Proc. 2023 Conf. on Empir. Methods Nat. Lang. Process., Houda Bouamor, Juan Pino, and Kalika Bali (Eds.). 6449–6464.
- [152] Jiyi Li, Ayaka Sato, Kazuya Shimura, and Fumiyo Fukumoto. 2020. Multi-task Peer-Review Score Prediction. In Proc. First Workshop on Sch. Document Process.. 121–126.
- [153] Lei Li, Yuqi Wang, Runxin Xu, Peiyi Wang, Xiachong Feng, Lingpeng Kong, and Qi Liu. 2024. Multimodal ArXiv: A Dataset for Improving Scientific Comprehension of Large Vision-Language Models. In Proc. 62nd Annu. Meet. Assoc. for Comput. Linguist., Vol. 1. 14369–14387.
- [154] Long Li, Weiwen Xu, Jiayan Guo, Ruochen Zhao, Xingxuan Li, Yuqian Yuan, Boqiang Zhang, Yuming Jiang, Yifei Xin, Ronghao Dang, et al. 2024. Chain of Ideas: Revolutionizing Research Via Novel Idea Development with LLM Agents. arXiv:2410.13185
- [155] Miao Li, Eduard Hovy, and Jey Lau. 2023. Summarizing Multiple Documents with Conversational Structure for Meta-Review Generation. In Find. Assoc. for Comput. Linguist. EMNLP 2023. 7089–7112.
- [156] Shujie Li, Liang Li, Ruiying Geng, Min Yang, Binhua Li, Guanghu Yuan, Wanwei He, Shao Yuan, Can Ma, Fei Huang, and Yongbin Li. 2024. Unifying Structured Data as Graph for Data-to-Text Pre-Training. Trans. Assoc. for Comput. Linguist. 12 (2024), 210–228.


- [157] Xiangci Li, Biswadip Mandal, and Jessica Ouyang. 2022. CORWA: A Citation-Oriented Related Work Annotation Dataset. In Proc. 2022 Conf. North Am. Chapter Assoc. for Comput. Linguist., Marine Carpuat, Marie-Catherine de Marneffe, and Ivan Vladimir Meza Ruiz (Eds.). 5426–5440.
- [158] Xiangci Li and Jessica Ouyang. 2024. Related Work and Citation Text Generation: A Survey. In Proc. 2024 Conf. on Empir. Methods Nat. Lang. Process.. 13846–13864.
- [159] Xiangci Li and Jessica Ouyang. 2025. Explaining relationships among research papers. In Proc. 31st Int. Conf. on Comput. Linguist.. 1080–1105.
- [160] Yutong Li, Lu Chen, Aiwei Liu, Kai Yu, and Lijie Wen. 2025. ChatCite: LLM Agent with Human Workflow Guidance for Comparative Literature Summary. In Proc. 31st Int. Conf. on Comput. Linguist.. 3613–3630.
- [161] Zehan Li, Xin Zhang, Yanzhao Zhang, Dingkun Long, Pengjun Xie, and Meishan Zhang. 2023. Towards general text embeddings with multi-stage contrastive learning. arXiv:2308.03281
- [162] Weixin Liang, Yuhui Zhang, Hancheng Cao, Binglu Wang, Daisy Ding, Xinyu Yang, Kailas Vodrahalli, Siyu He, Daniel Smith, Yian Yin, et al. 2023. Can large language models provide useful feedback on research papers? A large-scale empirical analysis. arXiv:2310.01783
- [163] Weixin Liang, Yaohui Zhang, Zhengxuan Wu, Haley Lepp, Wenlong Ji, Xuandong Zhao, Hancheng Cao, Sheng Liu, Siyu He, Zhi Huang, et al. 2025. Quantifying large language model usage in scientific papers. Nat. Hum. Behav. (2025), 1–11.
- [164] Weixin Liang, Yaohui Zhang, Zhengxuan Wu, Haley Lepp, Wenlong Ji, Xuandong Zhao, Hancheng Cao, Sheng Liu, Siyu He, Zhi Huang, Diyi Yang, Christopher Potts, Christopher D Manning, and James Y. Zou. 2024. Mapping the Increasing Use of LLMs in Scientific Papers. In Proc. COLM.
- [165] Chin-Yew Lin. 2004. ROUGE: A Package for Automatic Evaluation of Summaries. In Text Summ. Branches Out. 74–81.
- [166] Jialiang Lin, Jiaxin Song, Zhangping Zhou, Yidong Chen, and Xiaodong Shi. 2023. Automated scholarly paper review: Concepts, technologies, and challenges. Inf. Fusion 98 (2023), 101830.
- [167] Jialiang Lin, Jiaxin Song, Zhangping Zhou, Yidong Chen, and Xiaodong Shi. 2023. MOPRD: A multidisciplinary open peer review dataset. Neural Comput. Appl. 35, 34 (Sept. 2023), 24191–24206.
- [168] Stephanie Lin, Jacob Hilton, and Owain Evans. 2021. TruthfulQA: Measuring how models mimic human falsehoods. arXiv:2109.07958
- [169] Cencen Liu, Yi Xu, Wen Yin, and Dezhang Zheng. 2023. Structure-aware Table-to-Text Generation with Prefix-tuning. In Proc. 2023 4th Int. Conf. on Control. Robotics Intell. Syst.. 135–140.
- [170] Chia-Wei Liu, Ryan Lowe, Iulian Serban, Mike Noseworthy, Laurent Charlin, and Joelle Pineau. 2016. How NOT To Evaluate Your Dialogue System: An Empirical Study of Unsupervised Evaluation Metrics for Dialogue Response Generation. In Proc. 2016 Conf. on Empir. Methods Nat. Lang. Process., Jian Su, Kevin Duh, and Xavier Carreras (Eds.). 2122–2132.
- [171] Haokun Liu, Sicong Huang, Jingyu Hu, Yangqiaoyu Zhou, and Chenhao Tan. 2025. Hypobench: Towards systematic and principled benchmarking for hypothesis generation. arXiv:2504.11524
- [172] Quanliang Liu, Maciej P Polak, So Yeon Kim, MD Shuvo, Hrishikesh Shridhar Deodhar, Jeongsoo Han, Dane Morgan, and Hyunseok Oh. 2024. Beyond designer’s knowledge: Generating materials design hypotheses via large language models. arXiv:2409.06756
- [173] Ryan Liu and Nihar B. Shah. 2023. ReviewerGPT? An Exploratory Study on Using Large Language Models for Paper Reviewing. arXiv:arXiv:2306.00622
- [174] Sizhe Liu, Yizhou Lu, Siyu Chen, Xiyang Hu, Jieyu Zhao, Tianfan Fu, and Yue Zhao. 2024. DrugAgent: Automating AI-aided Drug Discovery Programming through LLM Multi-Agent Collaboration. arXiv:2411.15692
- [175] Yang Liu, Dan Iter, Yichong Xu, Shuohang Wang, Ruochen Xu, and Chenguang Zhu. 2023. G-Eval: NLG Evaluation using Gpt-4 with Better Human Alignment. In Proc. 2023 Conf. on Empir. Methods Nat. Lang. Process., Houda Bouamor, Juan Pino, and Kalika Bali (Eds.). 2511–2522.
- [176] Kyle Lo, Lucy Lu Wang, Mark Neumann, Rodney Kinney, and Dan S Weld. 2019. S2ORC: The semantic scholar open research corpus. arXiv:1911.02782
- [177] Chris Lu, Cong Lu, Robert Tjarko Lange, Jakob Foerster, Jeff Clune, and David Ha. 2024. The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery. arXiv:2408.06292
- [178] Yuyu Luo, Jiawei Tang, and Guoliang Li. 2021. nvBench: A Large-Scale Synthesized Dataset for Cross-Domain Natural Language to Visualization Task. arXiv:2112.12926
- [179] Ziming Luo, Zonglin Yang, Zexin Xu, Wei Yang, and Xinya Du. 2025. LLM4SR: A Survey on Large Language Models for Scientific Research. arXiv:2501.04306
- [180] Kangyong Ma. 2025. AI agents in chemical research: GVIM – An intelligent research assistant system. Digit. Discov. (2025).
- [181] Himanshu Maheshwari, Sambaran Bandyopadhyay, Aparna Garimella, and Anandhavelu Natarajan. 2024. Presentations are not always linear! GNN meets LLM for Text Document-to-Presentation Transformation with Attribution. In Find. Assoc. for Comput. Linguist. EMNLP 2024. 15948–15962.
- [182] Anna Martin-Boyle, Aahan Tyagi, Marti A Hearst, and Dongyeop Kang. 2024. Shallow synthesis of knowledge in GPT-generated texts: A case study in automatic related work composition. arXiv:2402.12255
- [183] Ahmed Masry, Xuan Long Do, Jia Qing Tan, Shafiq Joty, and Enamul Hoque. 2022. ChartQA: A Benchmark for Question Answering about Charts with Visual and Logical Reasoning. In Find. Assoc. for Comput. Linguist. ACL 2022, Smaranda Muresan, Preslav Nakov, and Aline Villavicencio (Eds.). 2263–2279.
- [184] Prakhar Mishra, Chaitali Diwan, Srinath Srinivasa, and Gopalakrishnan Srinivasaraghavan. 2021. Automatic title generation for text with pre-trained transformer language model. In 2021 IEEE 15th Int. Conf. on Semantic Comput.. IEEE, 17–24.
- [185] Ishani Mondal, Zongxia Li, Yufang Hou, Anandhavelu Natarajan, Aparna Garimella, and Jordan Lee Boyd-Graber. 2024. SciDoc2Diagrammer-MAF: Towards Generation of Scientific Diagrams from Documents guided by Multi-Aspect Feedback Refinement. In Find. Assoc. for Comput. Linguist. EMNLP 2024. 13342–13375.


- [186] Ishani Mondal, Shwetha S, Anandhavelu Natarajan, Aparna Garimella, Sambaran Bandyopadhyay, and Jordan Boyd-Graber. 2024. Presentations by the Humans and For the Humans: Harnessing LLMs for Generating Persona-Aware Slides from Documents. In Proc. EACL. 2664–2684.
- [187] Nafise Moosavi, Andreas Rücklé, Dan Roth, and Iryna Gurevych. 2021. SciGen: a Dataset for Reasoning-Aware Text Generation from Scientific Tables. In Proc. Neural Inf. Process. Syst. Track on Datasets Benchmarks, Vol. 1.
- [188] Rajiv Movva, Kenny Peng, Nikhil Garg, Jon Kleinberg, and Emma Pierson. 2025. Sparse autoencoders for hypothesis generation. arXiv:2502.04382
- [189] Niklas Muennighoff, Nouamane Tazi, Loic Magne, and Nils Reimers. 2023. MTEB: Massive Text Embedding Benchmark. In Proc. 17th Conf. Eur. Chapter Assoc. for Comput. Linguist.. 2014–2037.
- [190] Deepak Nathani, Lovish Madaan, Nicholas Roberts, Nikolay Bashlykov, Ajay Menon, Vincent Moens, Amar Budhiraja, Despoina Magka, Vladislav Vorotilov, Gaurav Chaurasia, Dieuwke Hupkes, Ricardo Silveira Cabral, Tatiana Shavrina, Jakob Foerster, Yoram Bachrach, William Yang Wang, and Roberta Raileanu. 2025. MLGym: A New Framework and Benchmark for Advancing AI Research Agents. arXiv:2502.14499
- [191] Benjamin Newman, Yoonjoo Lee, Aakanksha Naik, Pao Siangliulue, Raymond Fok, Juho Kim, Daniel S Weld, Joseph Chee Chang, and Kyle Lo. 2024. ArxivDIGESTables: Synthesizing Scientific Literature into Tables using Language Models. In Proc. 2024 Conf. on Empir. Methods Nat. Lang. Process.. 9612–9631.
- [192] Yuansheng Ni, Ping Nie, Kai Zou, Xiang Yue, and Wenhu Chen. 2025. VisCoder: Fine-Tuning LLMs for Executable Python Visualization Code Generation. arXiv:2506.03930
- [193] Allard Oelen, Mohamad Yaser Jaradeh, and Sören Auer. 2025. Introducing ORKG ASK: An AI-Driven Scholarly Literature Search and Exploration System Taking a Neuro-Symbolic Approach. In Int. Conf. on Web Eng.. 11–25.
- [194] Kishore Papineni, Salim Roukos, Todd Ward, and Wei-Jing Zhu. 2002. BLEU: a Method for Automatic Evaluation of Machine Translation. In Proc. 40th Annu. Meet. Assoc. for Comput. Linguist., Pierre Isabelle, Eugene Charniak, and Dekang Lin (Eds.). 311–318.
- [195] Ankur Parikh, Xuezhi Wang, Sebastian Gehrmann, Manaal Faruqui, Bhuwan Dhingra, Diyi Yang, and Dipanjan Das. 2020. ToTTo: A Controlled Table-To-Text Generation Dataset. In Proc. 2020 Conf. on Empir. Methods Nat. Lang. Process., Bonnie Webber, Trevor Cohn, Yulan He, and Yang Liu (Eds.). 1173–1186.
- [196] Yang Jeong Park, Daniel Kaplan, Zhichu Ren, Chia-Wei Hsu, Changhao Li, Haowei Xu, Sipei Li, and Ju Li. 2024. Can ChatGPT be used to generate scientific hypotheses? J. Materiomics 10, 3 (2024), 578–584.
- [197] Guy Paré, Marie-Claude Trudel, Mirou Jaana, and Spyros Kitsiou. 2015. Synthesizing Information Systems Knowledge: a Typology of Literature Reviews. Inf. & Manag. 52 (2015), 183–199.
- [198] Dominic Petrak, Nafise Sadat Moosavi, and Iryna Gurevych. 2023. Arithmetic-Based Pretraining Improving Numeracy of Pretrained Language Models. In Proc. 12th Jt. Conf. on Lexical Comput. Semant., Alexis Palmer and Jose Camacho-collados (Eds.). 477–493.
- [199] Nicky Phillips. 2017. Online software spots genetic errors in cancer papers. Nature 551, 7681 (2017).
- [200] Barbara Plank and Reinard van Dalen. 2019. CiteTracked: A longitudinal dataset of peer reviews and citations. In Proc. 4th Jt. Workshop on Bibliometric-enhanced Inf. Retr. Nat. Lang. Process. for Digit. Libr.. 116–122.
- [201] Aniket Pramanick, Yufang Hou, Saif M. Mohammad, and Iryna Gurevych. 2024. The Nature of NLP: Analyzing Contributions in NLP Papers. arXiv:2409.19505
- [202] Aniket Pramanick, Yufang Hou, Saif M. Mohammad, and Iryna Gurevych. 2024. Transforming Scholarly Landscapes: Influence of Large Language Models on Academic Fields beyond Computer Science. arXiv:2409.19508
- [203] Shraman Pramanick, Rama Chellappa, and Subhashini Venugopalan. 2024. SPIQA: A Dataset for Multimodal Question Answering on Scientific Papers. In Adv. Neural Inf. Process. Syst. 38, Amir Globersons, Lester Mackey, Danielle Belgrave, Angela Fan, Ulrich Paquet, Jakub M. Tomczak, and Cheng Zhang (Eds.).
- [204] Kevin Pu, KJ Feng, Tovi Grossman, Tom Hope, Bhavana Dalvi Mishra, Matt Latzke, Jonathan Bragg, Joseph Chee Chang, and Pao Siangliulue.

2024. IdeaSynth: Iterative Research Idea Development Through Evolving and Composing Idea Facets with Literature-Grounded Feedback. arXiv:2410.04025

- [205] Zhongji Pu, Chun-Lin Shi, Che Ok Jeon, Jingyuan Fu, Shuang-Jiang Liu, Canhui Lan, Yanlai Yao, Yong-Xin Liu, and Baolei Jia. 2024. ChatGPT and generative AI are revolutionizing the scientific community: A Janus-faced conundrum. iMeta 3, 2 (2024), e178.
- [206] Sukannya Purkayastha, Nils Dycke, Anne Lauscher, and Iryna Gurevych. 2025. Decision-Making with Deliberation: Meta-reviewing as a Document-grounded Dialogue. arXiv:2508.05283
- [207] Sukannya Purkayastha, Anne Lauscher, and Iryna Gurevych. 2023. Exploring Jiu-Jitsu Argumentation for Writing Peer Review Rebuttals. In Proc. 2023 Conf. on Empir. Methods Nat. Lang. Process.. 14479–14495.
- [208] Biqing Qi, Kaiyan Zhang, Haoxiang Li, Kai Tian, Sihang Zeng, Zhang-Ren Chen, and Bowen Zhou. 2023. Large language models are zero shot hypothesis proposers. arXiv:2311.05965
- [209] Biqing Qi, Kaiyan Zhang, Kai Tian, Haoxiang Li, Zhang-Ren Chen, Sihang Zeng, Ermo Hua, Hu Jinfang, and Bowen Zhou. 2024. Large Language Models as Biomedical Hypothesis Generators: A Comprehensive Evaluation. arXiv:2407.08940
- [210] Yuting Qiang, Yanwei Fu, Yanwen Guo, Zhi-Hua Zhou, and Leonid Sigal. 2016. Learning to Generate Posters of Scientific Papers. In AAAI Conf. on Artif. Intell..
- [211] Marissa Radensky, Simra Shahid, Raymond Fok, Pao Siangliulue, Tom Hope, and Daniel S Weld. 2024. Scideator: Human-LLM Scientific Idea Generation Grounded in Research-Paper Facet Recombination. arXiv:2409.14634


- [212] Raian Rahman, Rizvi Hasan, Abdullah Al Farhad, Md Tahmid Rahman Laskar, Md. Hamjajul Ashmafee, and Abu Raihan Mostofa Kamal. 2023. ChartSumm: A Comprehensive Benchmark for Automatic Chart Summarization of Long and Short Summaries. arXiv:2304.13620
- [213] Pritika Ramu, Aparna Garimella, and Sambaran Bandyopadhyay. 2024. Is This a Bad Table? A Closer Look at the Evaluation of Table Generation from Text. In Proc. 2024 Conf. on Empir. Methods Nat. Lang. Process.. 22206–22216.
- [214] Chandan K Reddy and Parshin Shojaee. 2024. Towards Scientific Discovery with Generative AI: Progress, Opportunities, and Challenges. arXiv:2412.11427
- [215] Isabelle Régner, Catherine Thinus-Blanc, Agnès Netter, Toni Schmader, and Pascal Huguet. 2019. Committees with implicit biases promote fewer women when they do not believe gender bias exists. Nat. Hum. Behav. 3, 11 (2019), 1171–1179.
- [216] Georg Rehm, Stefan Dietze, Sonja Schimmler, and Frank Krüger. 2024. Natural Scientific Language Processing and Research Knowledge Graphs: First International Workshop, NSLP 2024. Springer.
- [217] Zachary Robertson. 2023. GPT-4 is Slightly Helpful for Peer-Review Assistance: A Pilot Study. arXiv:2307.05492
- [218] Helmi Ben Saad, Ismail Dergaa, Hatem Ghouili, Halil İbrahim Ceylan, Karim Chamari, and Wissem Dhahbi. 2025. The Assisted Technology Dilemma: A Reflection on AI Chatbots Use and Risks While Reshaping the Peer Review Process in Scientific Research. AI Soc. 40, 7 (2025), 5649–5656.
- [219] Furkan Şahinuç, Subhabrata Dutta, and Iryna Gurevych. 2025. Expert Preference-based Evaluation of Automated Related Work Generation. arXiv:2508.07955
- [220] Furkan Şahinuç, Ilia Kuznetsov, Yufang Hou, and Iryna Gurevych. 2024. Systematic Task Exploration with LLMs: A Study in Citation Text Generation. In Proc. 62nd Annu. Meet. Assoc. for Comput. Linguist., Vol. 1. 4832–4855.
- [221] Furkan Şahinuç, Thy Thy Tran, Yulia Grishina, Yufang Hou, Bei Chen, and Iryna Gurevych. 2024. Efficient Performance Tracking: Leveraging Large Language Models for Automated Construction of Scientific Leaderboards. In Proc. 2024 Conf. on Empir. Methods Nat. Lang. Process.. 7963–7977.
- [222] Michele Salvagno, Fabio Silvio Taccone, and Alberto Giovanni Gerli. 2023. Can artificial intelligence help for scientific writing? Crit. care 27, 1

(2023), 75.

- [223] Shubhra Kanti Karmaker Santu, Sanjeev Kumar Sinha, Naman Bansal, Alex Knipper, Souvika Sarkar, John Salvador, Yash Mahajan, Sri Guttikonda, Mousumi Akter, Matthew Freestone, and Matthew C. Williams Jr. 2024. Prompting LLMs to Compose Meta-Review Drafts from Peer-Review Narratives of Scholarly Manuscripts. arXiv:2402.15589
- [224] Laurie A. Schintler, Connie L. McNeely, and James Witte. 2023. A Critical Examination of the Ethics of AI-Mediated Peer Review. arXiv:2309.12356
- [225] Daniel Schlagwein and Leslie Willcocks. 2023. ‘ChatGPT et al.’: The ethics of using (generative) artificial intelligence in research and science. J. Inf. Technol. 38, 3 (2023), 232–238.
- [226] Michael Schlichtkrull, Nedjma Ousidhoum, and Andreas Vlachos. 2023. The Intended Uses of Automated Fact-Checking Artefacts: Why, How and Who. In Find. Assoc. for Comput. Linguist. EMNLP 2023, Houda Bouamor, Juan Pino, and Kalika Bali (Eds.). 8618–8642.
- [227] Samuel Schmidgall, Yusheng Su, Ze Wang, Ximeng Sun, Jialian Wu, Xiaodong Yu, Jiang Liu, Zicheng Liu, and Emad Barsoum. 2025. Agent laboratory: Using LLM agents as research assistants. arXiv:2501.04227
- [228] Samuel Schmidgall, Rojin Ziaei, Carl Harris, Eduardo Reis, Jeffrey Jopling, and Michael Moor. 2024. AgentClinic: a multimodal agent benchmark to evaluate AI in simulated clinical environments. arXiv:2405.07960
- [229] Dominik Schmidt, Zhengyao Jiang, and Yuxiang Wu. 2024. Introducing Weco AIDE. https://www.weco.ai/blog/technical-report.
- [230] SciScore. 2024. The best methods review tool for scientific research. https://sciscore.com/.
- [231] Paul Sebo, Bing Nie, and Ting Wang. 2025. Can ChatGPT write better scientific titles? A comparative evaluation of human-written and AI-generated titles. F1000Research 14 (2025), 1470.
- [232] Chenhui Shen, Liying Cheng, Ran Zhou, Lidong Bing, Yang You, and Luo Si. 2022. MReD: A Meta-Review Dataset for Structure-Controllable Text Generation. In Find. Assoc. for Comput. Linguist. ACL 2022. 2521–2535.
- [233] Pranav Shetty, Arunkumar Chitteth Rajan, Chris Kuenneth, Sonakshi Gupta, Lakshmi Prerana Panchumarti, Lauren Holm, Chao Zhang, and Rampi Ramprasad. 2023. A general-purpose material property data extraction pipeline from large polymer corpora using natural language processing. npj Comput. Mater. 9, 1 (2023), 52.
- [234] Chufan Shi, Cheng Yang, Yaxin Liu, Bo Shui, Junjie Wang, Mohan Jing, Linran Xu, Xinyu Zhu, Siheng Li, Yuxiang Zhang, Gongye Liu, Xiaomei Nie, Deng Cai, and Yujiu Yang. 2024. ChartMimic: Evaluating LMM’s Cross-Modal Reasoning Capability via Chart-to-Code Generation. arXiv:2406.09961
- [235] Haoxiang Shi, Jiaan Wang, Jiarong Xu, Cen Wang, and Tetsuya Sakai. 2024. CT-Eval: Benchmarking Chinese Text-to-Table Performance in Large Language Models. arXiv:2405.12174
- [236] Chenglei Si, Tatsunori Hashimoto, and Diyi Yang. 2025. The Ideation-Execution Gap: Execution Outcomes of LLM-Generated versus Human Research Ideas. arXiv:2506.20803
- [237] Chenglei Si, Diyi Yang, and Tatsunori Hashimoto. 2024. Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers. arXiv:2409.04109
- [238] Shruti Singh, Mayank Singh, and Pawan Goyal. 2021. COMPARE: A Taxonomy and Dataset of Comparison Discussions in Peer Reviews. arXiv:2108.04366
- [239] Henry Small. 1973. Co-citation in the scientific literature: A new measure of the relationship between two documents. J. Am. Soc. for Inf. Sci. 24, 4


(1973), 265–269.

- [240] Wael Soliman and Mikko Siponen. 2022. What Do We Really Mean by Rigor in Information Systems Research?. In Proc. 55th Hawaii Int. Conf. on Syst. Sci..
- [241] Karen Spärck Jones. 1972. A statistical interpretation of term specificity and its application in retrieval. J. Documentation 28, 1 (1972), 11–21.
- [242] M. Sravanthi, C. Ravindranath Chowdary, and P. Sreenivasa Kumar. 2009. SlidesGen: Automatic Generation of Presentation Slides for a Technical Paper Using Summarization. In The Fla. AI Res. Soc..
- [243] Lukas Stappen, Georgios Rizos, Madina Hasan, Thomas Hain, and Björn W Schuller. 2020. Uncertainty-aware machine support for paper reviewing on the Interspeech 2019 submission corpus. In Proc. Interspeech 2020. 1808–1812.
- [244] Andrew Starnes and Clayton Webster. 2024. Mamba for Scalable and Efficient Personalized Recommendations. arXiv:2409.17165
- [245] Moritz Staudinger, Wojciech Kusa, Florina Piroi, and Allan Hanbury. 2024. An Analysis of Tasks and Datasets in Peer Reviewing. In Proc. Fourth Workshop on Sch. Document Process.. 257–268.
- [246] Dana Strauss, Sophia Gran-Ruaz, Muna Osman, Monnica T. Williams, and Sonya C. Faber. 2023. Racism and censorship in the editorial and peer review process. Front. Psychol. 14 (2023).
- [247] Haoyang Su, Renqi Chen, Shixiang Tang, Xinzhe Zheng, Jingzhe Li, Zhenfei Yin, Wanli Ouyang, and Nanqing Dong. 2024. Two Heads Are Better Than One: A Multi-Agent System Has the Potential to Improve Scientific Idea Generation. arXiv:2410.09403
- [248] Lya Hulliyyatus Suadaa, Hidetaka Kamigaito, Kotaro Funakoshi, Manabu Okumura, and Hiroya Takamura. 2021. Towards Table-to-Text Generation with Numerical Reasoning. In Proc. 59th Annu. Meet. Assoc. for Comput. Linguist. 11th Int. Jt. Conf. on Nat. Lang. Process., Chengqing Zong, Fei Xia, Wenjie Li, and Roberto Navigli (Eds.). 1451–1465.
- [249] Edward Sun, Yufang Hou, Dakuo Wang, Yunfeng Zhang, and Nancy X. R. Wang. 2021. D2S: Document-to-Slide Generation Via Query-Based Text Summarization. In Proc. NAACL. 1405–1418.
- [250] Kexuan Sun, Zhiqiang Qiu, Abel Salinas, Yuzhong Huang, Dong-Ho Lee, Daniel Benjamin, Fred Morstatter, Xiang Ren, Kristina Lerman, and Jay Pujara. 2022. Assessing Scientific Research Papers with Knowledge Graphs. In SIGIR ’22: The 45th Int. ACM SIGIR Conf. on Res. Dev. Inf. Retr., Enrique Amigó, Pablo Castells, Julio Gonzalo, Ben Carterette, J. Shane Culpepper, and Gabriella Kazai (Eds.). 2467–2472.
- [251] Lichao Sun, Yue Huang, Haoran Wang, Siyuan Wu, Qihui Zhang, Chujie Gao, Yixin Huang, Wenhan Lyu, Yixuan Zhang, Xiner Li, et al. 2024. TrustLLM: Trustworthiness in large language models. arXiv:2401.05561
- [252] Anirudh Sundar, Christopher Richardson, and Larry Heck. 2024. gTBLS: Generating Tables from Text by Conditional Question Answering. arXiv:2403.14457
- [253] Jaroslaw Szumega, Lamine Bougueroua, Blerina Gkotse, Pierre Jouvelot, and Federico Ravotti. 2023. The Open Review-Based (ORB) dataset: Towards Automatic Assessment of Scientific Papers and Experiment Proposals in High-Energy Physics. arXiv:2312.04576
- [254] Neset Tan, Trung Nguyen, Josh Bensemann, Alex Peng, Qiming Bao, Yang Chen, Mark Gahegan, and Michael Witbrock. 2023. Multi2Claim: Generating Scientific Claims from Multi-Choice Questions for Scientific Fact-Checking. In Proc. 17th Conf. Eur. Chapter Assoc. for Comput. Linguist.. 2652–2664.
- [255] Liyan Tang, Yifan Peng, Yanshan Wang, Ying Ding, Greg Durrett, and Justin Rousseau. 2023. Less Likely Brainstorming: Using Language Models to Generate Alternative Hypotheses. In Find. Assoc. for Comput. Linguist. ACL 2023, Anna Rogers, Jordan Boyd-Graber, and Naoaki Okazaki (Eds.). 12532–12555.
- [256] Song Tong, Kai Mao, Zhen Huang, Yukun Zhao, and Kaiping Peng. 2024. Automating Psychological Hypothesis Generation with AI: Large Language Models Meet Causal Graph. arXiv:2402.14424
- [257] Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, et al. 2023. Llama 2: Open foundation and fine-tuned chat models. arXiv:2307.09288
- [258] Patara Trirat, Wonyong Jeong, and Sung Ju Hwang. 2024. AutoML-Agent: A Multi-Agent LLM Framework for Full-Pipeline AutoML. arXiv:2410.02958
- [259] Yun-Da Tsai, Yu-Che Tsai, Bo-Wei Huang, Chun-Pai Yang, and Shou-De Lin. 2023. AutoML-GPT: Large language model for AutoML. arXiv:2309.01125
- [260] Juraj Vladika and Florian Matthes. 2023. Scientific Fact-Checking: A Survey of Resources and Approaches. In Find. Assoc. for Comput. Linguist. ACL 2023, Anna Rogers, Jordan Boyd-Graber, and Naoaki Okazaki (Eds.). 6215–6230.
- [261] Henrik Voigt, Kai Lawonn, and Sina Zarrieß. 2024. Plots Made Quickly: An Efficient Approach for Generating Visualizations from Natural Language Queries. In Proc. 2024 Jt. Int. Conf. on Comput. Linguist. Lang. Resour. Eval.. 12787–12793.
- [262] Dario von Wedel, Rico A. Schmitt, Moritz Thiele, Raphael Leuner, Denys Shay, Simone Redaelli, and Maximilian S. Schaefer. 2024. Affiliation Bias in Peer Review of Abstracts by a Large Language Model. JAMA 331, 3 (01 2024), 252–253.
- [263] Tu Vu, Mohit Iyyer, Xuezhi Wang, Noah Constant, Jerry Wei, Jason Wei, Chris Tar, Yun-Hsuan Sung, Denny Zhou, Quoc Le, et al. 2023. FreshLLMs: Refreshing large language models with search engine augmentation. arXiv:2310.03214
- [264] David Wadden, Kyle Lo, Bailey Kuehl, Arman Cohan, Iz Beltagy, Lucy Lu Wang, and Hannaneh Hajishirzi. 2022. SciFact-Open: Towards opendomain scientific claim verification. In Find. Assoc. for Comput. Linguist. EMNLP 2022, Yoav Goldberg, Zornitsa Kozareva, and Yue Zhang (Eds.). 4719–4734.
- [265] William H. Walters and Esther Isabelle Wilder. 2023. Fabrication and errors in the bibliographic citations generated by ChatGPT. Sci. Reports 13, 1

(2023), 14045.

- [266] Fei Wang, Zhewei Xu, Pedro Szekely, and Muhao Chen. 2022. Robust (Controlled) Table-to-Text Generation with Structure-Aware Equivariance Learning. In Proc. 2022 Conf. North Am. Chapter Assoc. for Comput. Linguist., Marine Carpuat, Marie-Catherine de Marneffe, and Ivan Vladimir Meza Ruiz (Eds.). 5037–5048.


- [267] Fuchun Wang, Xian Zhou, Wenpeng Hu, Zhunchen Luo, Wei Luo, and Xiaoying Bai. 2024. LLM Assists Hypothesis Generation and Testing for Deliberative Questions. In CCF Int. Conf. on Nat. Lang. Process. Chin. Comput.. Springer, 424–436.
- [268] Hao Wang and Wu-Jun Li. 2014. Relational collaborative topic regression for recommender systems. IEEE Trans. on Knowl. Data Eng. 27, 5 (2014), 1343–1355.
- [269] Pancheng Wang, Shasha Li, Haifang Zhou, Jintao Tang, and Ting Wang. 2019. ToC-RWG: Explore the Combination of Topic Model and Citation Information for Automatic Related Work Generation. IEEE Access 8 (2019), 13043–13055.
- [270] Qingyun Wang, Doug Downey, Heng Ji, and Tom Hope. 2024. Scimon: Scientific inspiration machines optimized for novelty. In Proc. 62nd Annu. Meet. Assoc. for Comput. Linguist.. 279–299.
- [271] Qingyun Wang, Lifu Huang, Zhiying Jiang, Kevin Knight, Heng Ji, Mohit Bansal, and Yi Luan. 2019. PaperRobot: Incremental Draft Generation of Scientific Ideas. In Proc. 57th Annu. Meet. Assoc. for Comput. Linguist., Anna Korhonen, David Traum, and Lluís Màrquez (Eds.). 1980–1991.
- [272] Qingyun Wang, Qi Zeng, Lifu Huang, Kevin Knight, Heng Ji, and Nazneen Fatema Rajani. 2020. ReviewRobot: Explainable Paper Review Generation based on Knowledge Synthesis. In Proc. 13th Int. Conf. on Nat. Lang. Gener.. 384–397.
- [273] Sida Wang, Xiaojun Wan, and Shikang Du. 2017. Phrase-Based Presentation Slides Generation for Academic Papers. In AAAI Conf. on Artif. Intell..
- [274] Xingyao Wang, Boxuan Li, Yufan Song, Frank F Xu, Xiangru Tang, Mingchen Zhuge, Jiayi Pan, Yueqi Song, Bowen Li, Jaskirat Singh, et al. 2024. OpenHands: An Open Platform for AI Software Developers as Generalist Agents. arXiv:2407.16741
- [275] Yubo Wang, Xueguang Ma, Ping Nie, Huaye Zeng, Zhiheng Lyu, Yuxuan Zhang, Benjamin Schneider, Yi Lu, Xiang Yue, and Wenhu Chen. 2025. ScholarCopilot: Training large language models for academic writing with accurate citations. arXiv:2504.00824
- [276] Zirui Wang, Mengzhou Xia, Luxi He, Howard Chen, Yitao Liu, Richard Zhu, Kaiqu Liang, Xindi Wu, Haotian Liu, Sadhika Malladi, Alexis Chevalier, Sanjeev Arora, and Danqi Chen. 2024. CharXiv: Charting Gaps in Realistic Chart Understanding in Multimodal LLMs. In Adv. Neural Inf. Process. Syst. 38, Amir Globersons, Lester Mackey, Danielle Belgrave, Angela Fan, Ulrich Paquet, Jakub M. Tomczak, and Cheng Zhang (Eds.).
- [277] Alexander Wei, Nika Haghtalab, and Jacob Steinhardt. 2023. Jailbroken: How does LLM safety training fail? Adv. Neural Inf. Process. Syst. 36 (2023), 80079–80110.
- [278] Jingxuan Wei, Cheng Tan, Qi Chen, Gaowei Wu, Siyuan Li, Zhangyang Gao, Linzhuang Sun, Bihui Yu, and Ruifeng Guo. 2025. From Words to Structured Visuals: A Benchmark and Framework for Text-to-Diagram Generation and Editing. In Proc. Comput. Vis. Pattern Recognit. Conf.. 13315–13325.
- [279] Ann C. Weller. 2001. Editorial Peer Review: Its Strengths and Weaknesses. American Society for Information Science and Technology.
- [280] Yixuan Weng, Minjun Zhu, Guangsheng Bao, Hongbo Zhang, Jindong Wang, Yue Zhang, and Linyi Yang. 2025. CycleResearcher: Improving Automated Research via Automated Review. In The Thirteen. Int. Conf. on Learn. Represent..
- [281] Leslie P. Willcocks, John Hindle, Matt Stanton, and John Smith. 2023. Maximizing Value with Automation and Transformation: A Realist’s Guide. Palgrave Macmillan.
- [282] Siwei Wu, Yizhi Li, Xingwei Qu, Rishi Ravikumar, Yucheng Li, Tyler Loakman Shanghaoran Quan Xiaoyong Wei, Riza Batista-Navarro, and Chenghua Lin. 2025. LongEval: A Comprehensive Analysis of Long-Text Generation Through a Plan-based Paradigm. arXiv:2502.19103
- [283] Siwei Wu, Yizhi Li, Kang Zhu, Ge Zhang, Yiming Liang, Kaijing Ma, Chenghao Xiao, Haoran Zhang, Bohao Yang, Wenhu Chen, Wenhao Huang, Noura Al Moubayed, Jie Fu, and Chenghua Lin. 2024. SciMMIR: Benchmarking Scientific Multi-modal Information Retrieval. In Find. Assoc. for Comput. Linguist. ACL 2024. 12560–12574.
- [284] Yuhao Wu, Yushi Bai, Zhiqiang Hu, Roy Ka-Wei Lee, and Juanzi Li. 2025. LongWriter-Zero: Mastering Ultra-Long Text Generation via Reinforcement Learning. arXiv:2506.18841
- [285] Guangzhi Xiong, Eric Xie, Amir Hassan Shariatmadari, Sikun Guo, Stefan Bekiranov, and Aidong Zhang. 2024. Improving Scientific Hypothesis Generation with Knowledge Grounded Large Language Models. arXiv:2411.02382
- [286] Peixin Xu, Yujuan Ding, and Wenqi Fan. 2024. ChartAdapter: Large Vision-Language Model for Chart Summarization. arXiv:2412.20715
- [287] Ruoxi Xu, Yingfei Sun, Mengjie Ren, Shiguang Guo, Ruotong Pan, Hongyu Lin, Le Sun, and Xianpei Han. 2024. AI for social science and social science of AI: A survey. Inf. Process. & Manag. 61, 3 (2024), 103665.
- [288] Sheng Xu and Xiaojun Wan. 2022. PosterBot: A System for Generating Posters of Scientific Papers with Neural Models. In AAAI Conf. on Artif. Intell..
- [289] Yutaro Yamada, Robert Tjarko Lange, Cong Lu, Shengran Hu, Chris Lu, Jakob Foerster, Jeff Clune, and David Ha. 2025. The AI Scientist-v2: Workshop-level automated scientific discovery via agentic tree search. arXiv:2504.08066
- [290] Hidekazu Yanagimoto, Iroha Kisaku, and Kiyota Hashimoto. 2024. Table-to-Text Using Pre-trained Large Language Model and LoRA. In 2024 16th IIAI Int. Congr. on Adv. Appl. Informatics. 91–96.
- [291] Bohao Yang, Yingji Zhang, Dong Liu, André Freitas, and Chenghua Lin. 2025. Does table source matter? Benchmarking and improving multimodal scientific table understanding and reasoning. arXiv:2501.13042
- [292] Zonglin Yang, Xinya Du, Junxian Li, Jie Zheng, Soujanya Poria, and Erik Cambria. 2023. Large language models for automated open-domain scientific hypotheses discovery. arXiv:2309.02726
- [293] Zonglin Yang, Wanhao Liu, Ben Gao, Tong Xie, Yuqiang Li, Wanli Ouyang, Soujanya Poria, Erik Cambria, and Dongzhan Zhou. 2024. MOOSE-Chem: Large Language Models for Rediscovering Unseen Chemistry Scientific Hypotheses. arXiv:2410.07076
- [294] Michihiro Yasunaga, Jungo Kasai, Rui Zhang, Alexander R. Fabbri, Irene Li, Dan Friedman, and Dragomir R. Radev. 2019. ScisummNet: A Large Annotated Corpus and Content-Impact Models for Scientific Paper Summarization with Citation Networks. In The Thirty-Third AAAI Conf. on Artif.


- Intell. AAAI 2019, The Thirty-First Innov. Appl. Artif. Intell. Conf. IAAI 2019, The Ninth AAAI Symp. on Educ. Adv. Artif. Intell. EAAI 2019. 7386–7393.
- [295] Deming Ye, Yankai Lin, Peng Li, and Maosong Sun. 2021. Packed levitated marker for entity and relation extraction. arXiv:2109.06067
- [296] Xinyang Yi, Ji Yang, Lichan Hong, Derek Zhiyuan Cheng, Lukasz Heldt, Aditee Kumthekar, Zhe Zhao, Li Wei, and Ed Chi. 2019. Sampling-biascorrected neural modeling for large corpus item recommendations. In Proc. 13th ACM Conf. on Recomm. Syst.. 269–277.
- [297] Zhangyue Yin, Qiushi Sun, Qipeng Guo, Jiawen Wu, Xipeng Qiu, and Xuanjing Huang. 2023. Do Large Language Models Know What They Don’t Know?. In Find. Assoc. for Comput. Linguist. ACL 2023, Anna Rogers, Jordan Boyd-Graber, and Naoaki Okazaki (Eds.). 8653–8665.
- [298] Larry D. Yore, Brian M. Hand, and Marilyn K. Florence. 2004. Scientists’ Views of Science, Models of Writing, and Science Writing Practices. J. Res. Sci. Teach. 41, 4 (2004), 338–369.
- [299] Yantao Yu, Weipeng Wang, Zhoutian Feng, and Daiyue Xue. 2021. A dual augmented two-tower model for online large-scale recommendation. In Proc. DLP-KDD.
- [300] Weizhe Yuan, Pengfei Liu, and Graham Neubig. 2022. Can We Automate Scientific Reviewing? J. Artif. Intell. Res. 75 (2022).
- [301] Abhay Zala, Han Lin, Jaemin Cho, and Mohit Bansal. 2024. DiagrammerGPT: Generating Open-Domain, Open-Platform Diagrams via LLM Planning. In COLM.
- [302] Qi Zeng, Mankeerat Sidhu, Hou Pong Chan, Lu Wang, and Heng Ji. 2023. Meta-review Generation with Checklist-guided Iterative Introspection. arXiv:2305.14647
- [303] Jiajie Zhang, Zhongni Hou, Xin Lv, Shulin Cao, Zhenyu Hou, Yilin Niu, Lei Hou, Yuxiao Dong, Ling Feng, and Juanzi Li. 2024. LongReward: Improving Long-context Large Language Models with AI Feedback. arXiv:2410.21252
- [304] Leixin Zhang, Steffen Eger, Yinjie Cheng, Weihe Zhai, Jonas Belouadi, Christoph Leiter, Simone Paolo Ponzetto, Fahimeh Moafian, and Zhixue Zhao. 2024. ScImage: How Good Are Multimodal Large Language Models at Scientific Text-to-Image Generation? arXiv:2412.02368
- [305] Lei Zhang, Yuge Zhang, Kan Ren, Dongsheng Li, and Yuqing Yang. 2023. Mlcopilot: Unleashing the power of large language models in solving machine learning tasks. arXiv:2304.14979
- [306] Qiang Zhang, Wanyi Chen, Ming Qin, Yuhao Wang, Zhongji Pu, Keyan Ding, Yuyue Liu, Qunfeng Zhang, Dongfang Li, Xinjia Li, et al. 2025. Integrating protein language models and automatic biofoundry for enhanced protein evolution. Nat. Commun. 16, 1 (2025), 1553.
- [307] Xuan Zhang, Limei Wang, Jacob Helwig, Youzhi Luo, Cong Fu, Yaochen Xie, Meng Liu, Yu-Ching Lin, Zhao Xu, Keqiang Yan, Keir Adams, Maurice Weiler, Xiner Li, and etc. 2023. Artificial Intelligence for Science in Quantum, Atomistic, and Continuum Systems. arXiv:2307.08423
- [308] Yu Zhang, Xiusi Chen, Bowen Jin, Sheng Wang, Shuiwang Ji, Wei Wang, and Jiawei Han. 2024. A Comprehensive Survey of Scientific Large Language Models and Their Applications in Scientific Discovery. In Proc. 2024 Conf. on Empir. Methods Nat. Lang. Process.. 8783–8817.
- [309] Yunyi Zhang, Ruozhen Yang, Siqi Jiao, SeongKu Kang, and Jiawei Han. 2025. Scientific Paper Retrieval with LLM-Guided Semantic-Based Ranking. In Find. Assoc. for Comput. Linguist. EMNLP 2025, Christos Christodoulopoulos, Tanmoy Chakraborty, Carolyn Rose, and Violet Peng (Eds.). 2049–2060.
- [310] Wei Zhao, Jennifer D’Souza, Steffen Eger, Anne Lauscher, Yufang Hou, Nafise Sadat Moosavi, Tristan Miller, and Chenghua Lin (Eds.). 2025. Proceedings of the First Workshop on Human–LLM Collaboration for Ethical and Responsible Science Production (SciProdLLM).
- [311] Xueliang Zhao, Tingchen Fu, Lemao Liu, Lingpeng Kong, Shuming Shi, and Rui Yan. 2023. SORTIE: Dependency-Aware Symbolic Reasoning for Logical Data-to-text Generation. In Find. Assoc. for Comput. Linguist. ACL 2023, Anna Rogers, Jordan Boyd-Graber, and Naoaki Okazaki (Eds.). 11247–11266.
- [312] Yilun Zhao, Zhenting Qi, Linyong Nan, Lorenzo Jaime Flores, and Dragomir Radev. 2023. LoFT: Enhancing Faithfulness and Diversity for Table-to-Text Generation via Logic Form Control. In Proc. 17th Conf. Eur. Chapter Assoc. for Comput. Linguist., Andreas Vlachos and Isabelle Augenstein (Eds.). 554–561.
- [313] Tianyu Zheng, Ge Zhang, Tianhao Shen, Xueling Liu, Bill Yuchen Lin, Jie Fu, Wenhu Chen, and Xiang Yue. 2024. OpenCodeInterpreter: Integrating code generation with execution and refinement. arXiv:2402.14658
- [314] Zhiling Zheng, Oufan Zhang, Christian Borgs, Jennifer T Chayes, and Omar M Yaghi. 2023. ChatGPT chemistry assistant for text mining and the prediction of MOF synthesis. J. Am. Chem. Soc. 145, 32 (2023), 18048–18062.
- [315] Yangqiaoyu Zhou, Haokun Liu, Tejes Srivastava, Hongyuan Mei, and Chenhao Tan. 2024. Hypothesis Generation with Large Language Models. arXiv:2404.04326
- [316] Yujun Zhou, Jingdong Yang, Yue Huang, Kehan Guo, Zoe Emory, Bikram Ghosh, Amita Bedar, Sujay Shekar, Zhenwen Liang, Pin-Yu Chen, et al.

2026. Benchmarking large language models on safety risks in scientific laboratories. Nat. Mach. Intell. (2026), 1–12.

- [317] Mingchen Zhuge, Changsheng Zhao, Dylan Ashley, Wenyi Wang, Dmitrii Khizbullin, Yunyang Xiong, Zechun Liu, Ernie Chang, Raghuraman Krishnamoorthi, Yuandong Tian, Yangyang Shi, Vikas Chandra, and Jürgen Schmidhuber. 2024. Agent-as-a-Judge: Evaluate Agents with Agents. arXiv:2410.10934


### A Historical Context and Background

Throughout history, science has undergone a number of paradigm shifts, culminating in today’s era of data-intensive exploration [104]. Although new tools and frameworks have accelerated the pace of scientific discovery, its basic steps have remained unchanged for centuries. As visualized in Fig. 4, these include (1) conception of a research question or problem, typically arising from a gap in disseminated knowledge; (2) collection and study of existing literature or data relevant to the problem; (3) formulation of a falsifiable hypothesis; (4) design and execution of experiments to test this hypothesis; (5) analysis and interpretation of the resulting data; and (6) reporting on the findings, allowing for their exploitation in real-world applications or as a source of knowledge for a further iteration of the scientific cycle.

With respect to the first two of these steps, a major challenge for any scholar is achieving, and then maintaining, sufficient familiarity with existing research on a given topic to be able to identify new research questions or to discover the knowledge required to answer them. Before the 20th century, it was often feasible to keep abreast of developments in a specialty simply by reading all the relevant books and journals as they were published. In modern times, however, the number of scientific publications has been doubling every 17 years [27], making this exhaustive approach unworkable. The need to sift through large quantities of scholarly knowledge spurred the specialization of simple library catalogs (in use since ancient times) into abstracting journals, bibliographic indexes, and citation indexes. By the 1960s and 1970s, many of these resources were being produced with standardized control principles and technologies, and could be queried interactively using automated information retrieval systems [26, pp.88–91]. These technical developments have enabled the widespread adoption of more principled approaches to the exploration of scientific knowledge, such systematic reviews [33] and citation analysis [82].

How experts propose hypotheses to explain observed phenomena has been extensively discussed in the philosophy and psychology of science, albeit with little empirical work until relatively recently [47, 48]. Contrary to the idealized notion of scientific reasoning, hypotheses rarely come about solely through induction (i.e., the abstraction of a general principle from a set of empirical observations). Rather, case studies employing think-aloud protocols suggest that hypotheses are generated through a process of successive refinement. These processes may involve non-inductive heuristics (analogies, simplifications, imagistic reasoning, etc.) that often fail individually, but may lead to valid explanatory models after “repeated cycles of generation, evaluation, and modification or rejection” [47, 48].

Experimentation and analysis aim to establish a causal relationship between the independent and dependent variables germane to a given scientific hypothesis. The metascientific literature abounds with practical advice on the design and execution of experiments, much of it discipline-specific. However, the general ideas at play can be traced to Ronald Fisher, whose seminal works on statistical methods [72] and experimental design [73] popularized the principles of randomization (assigning experimental subjects by chance), replication (observing different experimental subjects under the same conditions), and blocking (eliminating undesired sources of variation). Besides these considerations, experimental design involves the determination of the (statistical) analysis that will be performed, and is often constrained by the availability of resources such as the time, effort, or cost to gather and analyze observations or data [133].

Question Study Hypothesize Experiment Analyze Report

Fig. 4. Scientific discovery cycle, after [52]

Table 5. Overview of additional literature search engines and benchmarks. ✓ indicates feature availability; empty cells indicate lack of features or publicly documented support.

Recommendations Collections Citation AnalysisTrending AnalysisAuthor Profiles Visualization Tools Paper Chat Idea GenerationPaper WritingSummarizationPaper Review Datasets Code RepositoriesLLM Integration Web API Personalization

Search

Platform

Cost Data Size

Google Scholar ✓ ✓ ✓ ✓ ✓ ✓ Free Semantic Scholar ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ Free 214M Baidu Scholar ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ Freemium 680M BASE ✓ ✓ ✓ Free 415M Internet Archive Scholar ✓ ✓ Free 35M Scilit ✓ ✓ ✓ ✓ Free 172M The Lens ✓ ✓ ✓ ✓ Freemium 284M Science.gov ✓ ✓ Free 200M Academia.eu ✓ ✓ ✓ Freemium 55M OpenAlex ✓ ✓ ✓ Freemium AceMap ✓ ✓ ✓ ✓ ✓ ✓ Free 260M PubTator3 ✓ ✓ ✓ ✓ Free 6M

Search Engines

Papers with Code ✓ ✓ ✓ Free 154K ScienceAgentBench ✓ ✓ ✓ ✓ Free ORKG Benchmarks ✓ ✓ ✓ Free Huggingface ✓ ✓ ✓ ✓ ✓ Freemium

Benchm.

The final step in the scientific cycle, reporting, encompasses the dissemination of research findings, typically but not exclusively to the wider scientific community through articles, books, and presentations. The practice of scientific communication has itself attracted scientific study, leading to descriptive and pedagogical treatments of its various processes and strategies [e.g., 97, 298]. The essential role of peer review [279] has attracted special attention, albeit more on its high-level processes, its efficacy and reliability, and its objectivity and bias rather than on how reviewers go about evaluating manuscripts and communicating this evaluation. Accordingly, technological developments in the peer review workflow have until very recently tended to focus on managing or streamlining the review process for the benefit of the editor and publisher, or on supporting open or collaborative reviewing [64, 279].

B Supplementary Material on AI Support for Specific Topics and Tasks B.1 Literature Search, Summarization, and Comparison

Search Engines. Traditional academic search engines such as Google Scholar, Semantic Scholar, Baidu Scholar, Science.gov, and BASE, as shown in Table 5, are characterized by their broad literature coverage, citation tracking capabilities, and keyword-based search functionality. Their primary advantages include extensive indexing of scholarly content, which involves aggregating and organizing vast amounts of academic documents from various sources such as publisher websites, institutional repositories, and open-access archives. This comprehensive indexing spans multiple disciplines and document types, ensuring that users can access a diverse set of resources. Additionally, these platforms offer citation analysis features that allow researchers to track citation counts, measure the impact of publications, and explore citation networks to identify influential works and emerging trends within a given field. Another significant advantage is their free access to a wide range of academic resources, such as peer-reviewed journal articles, conference papers, preprints, theses and dissertations, technical reports, books and book chapters, as well as grey literature like

white papers, government reports, and institutional research outputs. However, these search engines have certain limitations, such as limited filtering options and relatively basic relevance ranking mechanisms compared to more advanced AI-enhanced search tools.

Benchmarks and Leaderboards. Code and dataset-focused search engines include platforms such as Huggingface (which in 2025 absorbed Papers with Code) and ScienceAgentBench, which are specifically designed to bridge the gap between academic publications and practical implementation by linking research papers with associated code and datasets. These platforms facilitate reproducibility and practical application of research findings by aggregating code repositories, enabling researchers and practitioners to easily explore implementations, compare results, and benchmark their models. A key feature of such platforms is their provision of dataset discovery tools, which allow users to identify relevant datasets for specific research problems, fostering collaboration, and accelerating experimentation cycles. These search engines are particularly valuable for machine learning practitioners, as they facilitate quick access to ready-to-use codebases, helping them implement cutting-edge research more efficiently. Based on these community-curated leaderboards, some studies have proposed models for constructing leaderboards directly from scientific papers [107, 127, 221].

Ethical Concerns. The use of AI in scientific search, summarization, and comparison raises ethical considerations, particularly in ensuring transparency, accountability, and equity. AI can significantly accelerate the pace of discovery, automate search tasks, and uncover patterns that may elude human researchers, but it also introduces risks and biases. Existing dynamics such as the Matthew effect, where well-known researchers receive disproportionate attention, might be algorithmically reinforced, intensifying inequalities. We believe that research should follow a human-centric approach, in which the human researcher is provided with advanced tools but remains fully responsible for executing the research and summarizing the results in research papers. It is also important to develop algorithms to reduce biases by recommending relevant work to researchers based on the content of the research, independent of the popularity of the authors. Tools that are able to uncover gaps in the existing literature might even lead to a more uniform allocation of researchers to topics, reducing the bias towards overpopulated areas.

### B.2 AI-Driven Scientific Discovery: Ideation, Hypothesis Generation, and Experimentation

Methods. Figure 5 provides a broad overview of the methods applied in hypothesis generation, idea generation, and automated experimentation. Most works in hypothesis generation focus on reducing hallucinations, handling long contexts, and iteratively refining outputs. To reduce hallucinations, an initial hypothesis is validated against a knowledge base for refinement. For long-context inputs, different contexts are summarized and integrated, while refinement strategies iteratively improve the hypothesis until it meets a satisfactory level. A similar iterative refinement strategy is also applied in idea generation. Additionally, alignment strategies are employed to make generated ideas more thoughtful and feasible. In multi-agent systems, multiple agents collaborate to enhance the idea generation process. In contrast, automated experimentation often relies on tree search for selecting optimal examples, multi-agent workflows where LLMs collaborate on distinct tasks, and iterative refinement to improve task performance. While hypothesis and idea generation leverage diverse sources such as scientific literature, web data, and datasets, automated experimentation operates on predefined ideas and requires access to computational models, simulations, and raw data.

Ethical Concerns. In the area of idea generation, there is a risk of reinforcing established research paradigms. LLMs trained on the basis of existing literature may favor popular paths and neglect underrepresented research directions.

###### Automated Experimentation

![image 8](Eger et al._2025_Transforming Science with Large Language Models A Survey on AI-assisted Scientific Discovery, Exper_images/imageFile8.png)

![image 9](Eger et al._2025_Transforming Science with Large Language Models A Survey on AI-assisted Scientific Discovery, Exper_images/imageFile9.png)

![image 10](Eger et al._2025_Transforming Science with Large Language Models A Survey on AI-assisted Scientific Discovery, Exper_images/imageFile10.png)

###### Hypothesis Generation

###### Idea Generation

Hallucination:

Iterative refinement:

Multi-agent workflow:

|Task 1|
|---|


|Agent 1| |
|---|---|
| | |


|Refine Hypothesis|
|---|


|Validate via Knowledge Base/Evidence Search|
|---|


No

Idea good enough?

|Task 2|
|---|


Refine Idea

Agent 2

Initial Hypothesis

|Agent 3| |
|---|---|
| | |


|Task 3|
|---|


Long context input:

Human alignment:

Tree search:

|R: Root Ai: Task 1 Bi: Task 2|
|---|


|Summary Context 1|
|---|


R

Yes

Align via Model/Metrics

|Summary Context 2|
|---|


|Generate Hypothesis|
|---|


Misalignment?

A1 A2

|Summary Context 3|
|---|


B1 B2

Refinement strategies:

Multi-agent systems:

Iterative refinement:

Agent 1

No

Task 1 good enough?

Refine Task 1

No

|Update Ideas|
|---|


Hypothesis good enough?

Refine Hypothesis

Agent 2

No

Task 2 good enough?

Agent 3

Refine Task 2

Scientific Literature (Papers, Metaanalyses, Systematic Reviews)

Web Data (Scientific Discussions, Social Media Forums)

Raw Data (Surveys, Sensors, Experiments)

Datasets (Open Databases, Government Statistics, Lab Datasets)

Computational Models & Simulations

Knowledge Graphs (Semantic Scholar, Microsoft Academic)

Feasibility Constraints (Resources, Ethics, Funding)

Fig. 5. Visualization of the hypothesis generation, idea generation, and automated experimentation process.

As a result, unconventional ideas may be unintentionally marginalized. For example, an AI might repeatedly suggest incremental improvements in a dominant field rather than proposing entirely new lines of research, thereby limiting the diversity of scientific thinking. LLM-generated hypotheses may also lack transparency, making it difficult to assess their validity or underlying assumptions, which could lead to flawed experiments. For example, an LLM might identify a statistical correlation in its training data and propose hypotheses without clearly revealing the underlying assumptions or data sources, making it difficult for researchers to verify its scientific soundness or hold anyone accountable if the hypotheses proves misleading. Additionally, LLMs that ideation and hypothesis generation systems rely on are not safe by design [277]. These systems may be jailbroken by malicious users to produce harmful ideas—for instance, re-purposing open science artefacts for malicious ends [98], and suggesting toxic molecular designs [100]. Zhou et al. [316] show that these systems may suggest unsafe experimental procedures (e.g., improper equipment use, unsafe chemical handling, or failure to recognize experimental hazards), which is problematic without human oversight.

### B.3 Text-based Content Generation

Methods. Figure 6 illustrates the content generation process for academic papers, covering title, abstract, related work, and bibliography generation, with their respective methods. Title generation methods include abstract-totitle, content-to-title, and future work-to-title mappings. Abstract generation typically involves title-to-abstract and keywords-to-abstract techniques. Related work generation follows either extractive methods (reordering extracted

![image 11](Eger et al._2025_Transforming Science with Large Language Models A Survey on AI-assisted Scientific Discovery, Exper_images/imageFile11.png)

![image 12](Eger et al._2025_Transforming Science with Large Language Models A Survey on AI-assisted Scientific Discovery, Exper_images/imageFile12.png)

![image 13](Eger et al._2025_Transforming Science with Large Language Models A Survey on AI-assisted Scientific Discovery, Exper_images/imageFile13.png)

Extractive

📑 📑

Extract &Reorder 📑

|1.) Title|
|---|


Abstract

- 2.) Abstract

- 3.) Introduction
- 4.) Related Work

- 5.) Methodology
- 6.) Results

- 7.) Conclusion


Paper Content

📑

Rewrite & Reconstruct

Future Work

📑

📑

Abstractive

![image 14](Eger et al._2025_Transforming Science with Large Language Models A Survey on AI-assisted Scientific Discovery, Exper_images/imageFile14.png)

![image 15](Eger et al._2025_Transforming Science with Large Language Models A Survey on AI-assisted Scientific Discovery, Exper_images/imageFile15.png)

Non-Parametric (Pre-Hoc)

🌐

Title

Yes

|8.) Bibliography|
|---|


Paper Content

Citation?

🤖

Parametric

Keywords Non-Parametric

📑

(Post-Hoc)

Fig. 6. Visualization of the content generation process for academic papers.

sentences) or abstractive methods (rewriting content from multiple papers). Bibliography generation is categorized into non-parametric methods (retrieving references from external sources) and parametric methods (LLMs generating references from preexisting knowledge without retrieval). Non-parametric methods are further divided into pre-hoc (determining citation needs before text generation and retrieving references beforehand) and post-hoc (checking for citations after text generation and appending retrieved references as needed).

Ethical Concerns. In scientific work, the issues of authorship and plagiarism in AI-generated texts are major concerns. In general, it is hard to distinguish between AI- and human-generated texts. Although there are a number of tools that purport to detect AI-generated text (e.g., GPTZero and Hive), Anderson et al. [7] show that they can be fooled by applying automatic paraphrasing. Studies have also found that ChatGPT-generated texts easily pass automated plagiarism detectors [4, 69].

B.4 Multimodal Content Generation and Understanding B.4.1 Data. Table 3 provides an overview of datasets for multimodal content generation and understanding.

Scientific Table Understanding. Table understanding often comes as table-to-text generation, which focuses on producing accurate textual descriptions that reflect table content. SciGen [187] and numericNLG [248] are benchmarks specifically focused on scientific table reasoning, both emphasizing arithmetic reasoning over numerical tables. Each dataset contains 1.3K expert-annotated tables. The annotations include the tables and parts of the scientific papers that describe the corresponding findings of the annotated tables. A specific subtask of these benchmarks is explored in Ampomah et al. [6], which focuses on generating textual explanations for tables reporting ML model performance metrics. This dataset pairs numerical tables of classification performance (e.g., precision, recall, and accuracy) with expert-written textual explanations that analyze and interpret the metrics. Datasets like HiTab [44] tackle the complexity of hierarchical tables commonly found in statistical reports, introducing numerical reasoning tasks that require models

Table 6. Multimodal content generation and understanding datasets.

##### Dataset Size Data Sources

Scientific Figure Understanding arXivCap [153] 6.4M images and 3.9M captions from 572K papers arXiv FigureQA [123] > 100K scientific-style figures Synthetic ChartQA [183] 4.8K charts, 9.6K QA pairs statista.com, pewresearch.com, etc. CharXiv [276] 2.3K charts with descriptive and reasoning questions arXiv arXivQA [153] 35K figures with 100K QA pairs arXiv SPIQA [203] 152K figures with 270K QAs 19 top-tier academic conferences ChartSumm [286] 84K charts Knoema SciMMIR [283] 530K figures and tables image–text pairs arXiv

Scientific Figure Generation DaTikZ (V1-V3) [19–21] 118–456K pairs of captions/TikZ code arXiv, TEX Stack Exchange DaTikZ V4 [94] 2M pairs of VLM descriptions/TikZ code arXiv, GitHub, TEX Stack Exchange DiagramGenBench [278] 6713 train/270 test for coding/generation, 1400 train/

VGQA and DaTikZ licensed under CC BY 4.0 or MIT

200 test for editing

Plot2XML [54] 247 complex diagrams Conference papers PandasPlotBench [78] 175 visualizations Matplotlib gallery VisCode-200K [192] 200K supervised examples Open-source Python repositories, Code–

Feedback dataset [313] ScImage [304] 404 instructions and 3K generated scientific images Manual (template) construction SciDoc2DiagramBench [185]

1,080 extrapolated diagrams in the format “<paper(s), intent of diagram, gold diagram>”

ACL Anthology

ChartMimic [234] 1000 triplets of (figure, instruction, code) instances Physics, Computer Science, Economics, etc. Scientific Table Understanding SciGen [187] 1.3K pairs of scientific tables and their descriptions arXiv (especially cs.CL and cs.LG) NumericNLG [248] 1.3K pairs of scientific tables and their descriptions ACL Anthology SciXGen [37] 484K tables from 205K papers arXiv

##### Scientific Table Generation

arXivDigestTables [191] 2,228 literature review tables extracted from arXiv papers that synthesize a total of 7,542 research paper

literature review tables from arXiv papers from April 2007 to November 2023

Scientific Slides and Poster Generation SciDuet [249] 1,088 papers and 10,034 slides by their authors NeurIPS/ICML/ACL Anthology DOC2PPT [76] 5,873 papers and 98,856 slides by their authors CV (CVPR, ECCV, BMVC), NLP (ACL,

NAACL, EMNLP), ML (ICML, NeurIPS, ICLR) Persona-Aware-D2S [186] 75 papers from SciDuet, and 300 slides ACL Anthology SlidesBench [83] 7K training and 585 test Web (Art, Marketing, Environment, Technol-

ogy, etc.)

to account for implicit relationships and hierarchical indexing within tables. SciXGen [37] broadens the scope of table-to-text generation with context-aware scientific text generation. By drawing from over 200K scientific papers, SciXGen requires models to generate descriptions for tables, figures, and algorithms, grounded in the surrounding body text. Recent work further shows that scientific table performance depends strongly on the table source/modality (e.g., PDF-rendered images vs. LATEX/HTML tables), and introduces dedicated multimodal scientific table benchmarks to evaluate and improve numerical reasoning [291].

Scientific Table Generation. Table generation often comes in the form of text-to-table generation [57, 118, 235], the process of converting unstructured textual information into structured tabular formats. This process is particularly valuable for scientific domains where textual data often contains detailed experimental results, observations, or findings

1.) Input Types

- 2.) Black-Box System
- 3.) Code


4.) Rendered Images

- - AutomaTikZ
- - DeTikZify


![image 16](Eger et al._2025_Transforming Science with Large Language Models A Survey on AI-assisted Scientific Discovery, Exper_images/imageFile16.png)

|![image 17](Eger et al._2025_Transforming Science with Large Language Models A Survey on AI-assisted Scientific Discovery, Exper_images/imageFile17.png)|
|---|


![image 18](Eger et al._2025_Transforming Science with Large Language Models A Survey on AI-assisted Scientific Discovery, Exper_images/imageFile18.png)

![image 19](Eger et al._2025_Transforming Science with Large Language Models A Survey on AI-assisted Scientific Discovery, Exper_images/imageFile19.png)

![image 20](Eger et al._2025_Transforming Science with Large Language Models A Survey on AI-assisted Scientific Discovery, Exper_images/imageFile20.png)

|![image 21](Eger et al._2025_Transforming Science with Large Language Models A Survey on AI-assisted Scientific Discovery, Exper_images/imageFile21.png)|
|---|


- ...

![image 22](Eger et al._2025_Transforming Science with Large Language Models A Survey on AI-assisted Scientific Discovery, Exper_images/imageFile22.png)

![image 23](Eger et al._2025_Transforming Science with Large Language Models A Survey on AI-assisted Scientific Discovery, Exper_images/imageFile23.png)

![image 24](Eger et al._2025_Transforming Science with Large Language Models A Survey on AI-assisted Scientific Discovery, Exper_images/imageFile24.png)

![image 25](Eger et al._2025_Transforming Science with Large Language Models A Survey on AI-assisted Scientific Discovery, Exper_images/imageFile25.png)

![image 26](Eger et al._2025_Transforming Science with Large Language Models A Survey on AI-assisted Scientific Discovery, Exper_images/imageFile26.png)

|![image 27](Eger et al._2025_Transforming Science with Large Language Models A Survey on AI-assisted Scientific Discovery, Exper_images/imageFile27.png)|
|---|


![image 28](Eger et al._2025_Transforming Science with Large Language Models A Survey on AI-assisted Scientific Discovery, Exper_images/imageFile28.png)

|![image 29](Eger et al._2025_Transforming Science with Large Language Models A Survey on AI-assisted Scientific Discovery, Exper_images/imageFile29.png)|
|---|


|![image 30](Eger et al._2025_Transforming Science with Large Language Models A Survey on AI-assisted Scientific Discovery, Exper_images/imageFile30.png)|
|---|


|Neural network with four inputs, one output and one hidden layer.|
|---|


Fig. 7. Overview of the scientific figure generation process. Various input types including sketches, screenshots, and text can be used to generate TikZ code with tools such as AutomaTikZ [20] and DeTikZify [21]. The generated code is then rendered into high-quality vector graphics images.

that need transformation into structured tables. In the scientific domain, ArXivDIGESTables [191] addresses the specific challenge of automating the creation of literature review tables. Rows in these tables represent individual papers, while columns capture comparative aspects such as methods, datasets, and results. ArXivDIGESTables supports the generation of literature review tables by leveraging additional grounding context, such as captions and in-text references.

B.4.2 Methods and Results. Table 7 provides a summary of representative approaches for multimodal content generation and understanding methods, and Fig. 7 illustrates the process of scientific figure generation. The remainder of this section presents the methods for the tasks of table understanding and generation introduced above, and extends the discussion of scientific slide and poster generation methods from §3.4.

Scientific Slide and Poster Generation. For scientific slide generation, early works typically relied on heuristic rulebased approaches. For instance, Sravanthi et al. [242] develop a rule-based system to generate slides for each section and subsection of a paper, with the textual content of the slides coming from a query-based extractive summarization system. Later, researchers began to leverage machine learning approaches to extract key phrases and their corresponding important sentences. Hu and Wan [109] use a support vector regression (SVR) model to learn the importance of each sentence in a paper. The slides are then generated using an integer linear programming (ILP) model to select and align key phrases and sentences. Wang et al. [273] propose a system to generate slides for each section of a given paper, focusing on creating two-layer bullet points. The authors first extract key phrases from the paper using a parser and then use a random forest classifier to predict the hierarchical relationships between pairs of phrases. Li et al. [150] develop two sentence extractors—a neural-based model and a log-linear model—within a mutual learning framework to extract relevant sentences from papers. These sentences are used to generate draft slides for four topics: contribution, dataset, baseline, and future work.

It is important to note that all the aforementioned works focus on extracting sentences or phrases from the given paper to serve as the slide text content. In contrast, Fu et al. [76] and Sun et al. [249] take a different approach by training sequence-to-sequence models to generate sentences for the slide text content. This distinction is analogous to

Table 7. Multimodal content generation and understanding approaches.

Task Input Output Dataset Method Evaluation Scientific Figure Understanding

Question Answering [128]

Synthetic, scientificstyle figures and questions

Answers FigureQA Fine-tuning Accuracy

Chart Summarization [212]

Chart images with metadata

Chart summaries ChartSumm Fine-tuning Automatic evalua-

tion

Caption Figure Retrieval

Figure or caption Caption or figure SciMMIR Fine-tuning Ranking Metrics

##### Scientific Figure Generation

Caption/Instructionto-code generation [20, 261]

(Extended) scientific caption or instruction

Compilable (TikZ, Vega, etc.) code of scientific figure

AutomaTikZ, DaTikZ

Fine-tuning Human & various metrics [20]

Description-to-image generation [304]

Description/instruction Scientific image ScImage Prompting Human

Sketch/Image-toimage generation

Scientific (raster) image or sketch

Compilable TikZ code of scientific figure

DaTikZ-v2 Fine-tuning & MCTS

Human & various metrics

Scientific diagram generation [185]

Scientific paper(s) + intent

Diagram SciDoc2-

Two-stage pipeline

Human & various metrics

DiagramBench

##### Scientific Table Understanding

Table description [187]

Tables from scientific articles

Table description SciGen Fine-tuning Automatic & hu-

man evaluation

Numerical reasoning [248]

Tables from scientific papers

Numerical descriptions

NumericNLG Fine-tuning Automatic & hu-

##### man evaluation Scientific Table Generation

Literature review table generation [191]

A list of papers Table schema +

ArXivDigest Tables

Prompting Automatic & hu-

##### man evaluation Scientific Slide and Poster Generation

values

Single slide generation [249]

Paper + slide title Slide content SciDuet Two-step

ROUGE and human evaluation

method

Slide deck generation [76]

Paper A deck of slides DOC2PPT Hierarchical generative model

Automatic & human evaluation

Personalized slide deck generation [186]

Paper + target audience (technical or nontechnical)

A deck of slides PersonaAware-D2S

Fine-tuning Automatic & human evaluation

the difference between extractive and abstractive summaries in text summarization. More specifically, Fu et al. [76] design a hierarchical recurrent sequence-to-sequence architecture to encode the input document, including sentences and images, and generate a slide deck. In contrast, Sun et al. [249] assume that slide titles would be provided by end users, and use these titles to retrieve relevant and engaging text, figures, and tables from a given paper using a dense retrieval model. They then summarize the retrieved content into bullet points with a fine-tuned long-form question answering system based on BART.

With recent advancements in LLMs and vision–language models (VLMs), researchers have started using these technologies for generating scientific presentation slides. Mondal et al. [186] propose a system to generate personaaware presentation slides by fine-tuning LLMs such as text-davinci-003 and gpt-3.5-turbo with a small training dataset containing personalized slide decks for each paper. Maheshwari et al. [181], focusing solely on generating text content, develop an approach that combines graph neural networks (GNNs) with LLMs to capture non-linearity in presentation generation, attributing source paragraphs to each generated slide within the presentation. Bandyopadhyay et al. [15] design a bird’s-eye view document representation to generate an outline, map slides to sections, and then create textual content for each slide individually using LLMs. The approach then extracts images from the original papers by identifying text–image similarity in a shared subspace through a VLM.

Generating posters from scientific papers has received less attention compared to scientific slide generation. Qiang et al. [210] introduce a graphical model to infer key content, panel layouts, and the attributes of each panel from data. The poster generator demo system of Xu and Wan [288] first identifies important sections of a paper using a trained classifier, then employs a summarization model to extract key sentences and related graphs from each section to construct corresponding panels. Finally, the system generates a LATEX document for the poster based on a template selected by the user.

Scientific Table Understanding. Table-to-text generation encompasses a range of methodologies designed to transform structured tabular data into coherent and accurate textual descriptions. These techniques process, reason over, and utilize tabular structures to address challenges such as logical reasoning, content fidelity, and domain-specific adaptation. Serialization is a foundational approach where tables are linearized into sequences compatible with transformer-based language models. In this method, tables are converted into linear text sequences using special characters to delineate structure [8, 187, 195]. Structure-aware methods explicitly model the inherent relationships and hierarchies within tables to enhance reasoning and generation fidelity. These include intermediate representations [156, 311, 312], structure-aware pretraining [136, 198, 290], and structure-aware self-attention mechanisms [169, 266]. For evaluation, common (if flawed) metrics like BLEU and BARTScore are widely used to evaluate the fluency and relevance of generated text against reference outputs. However, ensuring faithfulness to the source table remains a significant challenge, often requiring human evaluation for accurate assessment [187, 198].

Scientific Table Generation. While no existing approach to table generation focuses specifically on scientific data, several methodologies present promising directions. The gTBLS (Generative Tables) approach [252] proposes a two-stage table generation process. The first stage infers the table structure from input text, while the second stage generates table content by formulating table-guided questions; this enhances syntactic validity and logical coherence of generated tables. In the context of open-structure table extraction, OpenTE [62] tackles the task of extracting tables with intrinsic semantic, calculational, and hierarchical structure from unstructured text. OpenTE introduces a three-step pipeline that identifies semantic and relational connections among table columns, extracts structured data, and grounds the output by aligning extracted data with the source text and table structure. Evaluation of text-to-table generation for science should focus on structural accuracy, value fidelity, and semantic coherence. TabEval [213] provides a promising direction by introducing a decomposition-based framework that breaks tables into atomic statements and evaluates them using entailment-based measures, though comprehensive evaluation still requires further advancements.

B.4.3 Ethical Concerns. Tools for figure, table, slide, and poster generation are technically limited by the relatively small sizes of datasets for training and testing. For example, AutomaTikZ [20] and its extensions contain only several hundred

thousand pairs of textual descriptions and corresponding code snippets, while general-purpose image generation datasets are often orders of magnitudes larger. There is also a misalignment problem of image captions and the corresponding images/code [94], increasing the risk of hallucinations. These tools can therefore easily produce incorrect scientific figures, particularly when their users overlook, ignore, or maliciously abuse their limitations.

### B.5 Peer Review

Assessment of Scientific Rigor. Several attempts have been made to computationally analyze the rigor of scientific papers. Soliman and Siponen [240], for example, investigated how researchers use the word “rigor” in information system literature and discovered that the exact meaning was ambiguous in current research. Nonetheless, various automated tools have been proposed to assess the rigor of academic papers. Phillips [199] develop an online software that spots genetic errors in cancer papers, and Sun et al. [250] use knowledge graphs to assess the credibility of papers based on metadata such as publication venue, affiliation, and citations. However, these methods are neither domain-specific, nor do they provide sufficient guidance for authors to improve their narrative and writing. In contrast, SciScore [230] uses language models to produce rigor reports for paper drafts with the aim of helping authors identify weaknesses in their presentation. More recently, James et al. [116] propose a bottom-up, data-driven framework that automates the identification and definition of rigor criteria while assessing their relevance in scientific texts. Their framework integrates three key components: rigor keyword extraction, detailed definition generation, and the identification of salient criteria. Additionally, its domain-agnostic design allows for flexible adaptation across different fields.

Scientific Claim Verification. The increasing volume of scientific literature has created a demand for automated methods for verifying the validity and reliability of research claims. Scientific fact verification, which aims to assess the accuracy of scientific statements, often relies on external knowledge to support or refute claims [61, 260]. Several datasets have been developed to address this, including SciFact-Open [264], which provides scientific claims and supporting evidence from abstracts. However, it is limited to the use of abstracts as the primary source of evidence. As the statements in abstract can also be inaccurate or misleading, it is important to corroborate them with evidence from the main body of the paper. To this end, Glockner et al. [89, 90] propose a theoretical argumentation model to reconstruct fallacious reasoning of false claims that misrepresent scientific publications. The need to contextualize claims with supporting evidence is also highlighted by Chan et al. [34], who introduce a dataset of claims extracted from lab notes. Unlike other datasets, this resource is claimed to be “actually in use”, providing a more realistic understanding of how researchers interact with scientific findings. The authors annotate claims with links to figures, tables, and methodological details, and develop associated tasks to improve retrieval. While this provides valuable resources for context-based verification, it primarily focuses on factual verification and does not evaluate the potential for overstatement. Beyond factual correctness, there is a growing recognition for the need to analyze how researchers present their findings, rather than their mere factuality. This includes the detection of overstatements, where authors exaggerate their achievements, and understatements, where the true impact of the research is downplayed [126]. Schlichtkrull et al. [226] present a qualitative analysis of how intended uses of fact verification are described in highly-cited NLP papers, particularly focusing on the introductions of the papers, to understand how these elements are framed. The work suggests that claims should be supported by relevant prior work and empirical results.

Ethical Concerns. Given the critical role of scientific peer review for science, and, accordingly, for society as a whole, ethical considerations around AI-supported peer review are of utmost importance. As the general concerns around unfair biases in AI and the resulting harms apply [141], research on safe peer-reviewing support needs to be prioritized.

For instance, von Wedel et al. [262] recently showed that LLMs exhibit affiliation biases when reviewing abstracts. In this context, any AI support for peer reviewing needs to be critically evaluated [224], and solutions that target only a particular aspect in a collaborative environment that leaves the scientific autonomy to the human expert may be preferable to end-to-end reviewing systems. A recent discussion on specific risks of using LLMs in peer reviewing is also provided by Saad et al. [218], which highlights the risk of diminished engagement and critical thinking of reviewers and call for the creation of ethical standards to balance AI’s capabilities with human expertise.

### C This Paper as an AI Use Case

The preparation of this survey paper itself involved the use of AI tools to support specific aspects of the research workflow. For retrieving, selecting, and categorizing the literature and resources described in the various task subsections of §3, many of us relied not only on traditional information retrieval tools such as Google Search and Google Scholar, but also on tools incorporating generative AI, such as NotebookLM, ChatGPT, and Scholar Inbox. LLMs also assisted some co-authors with grammar and spell checking, as well as generating LATEX code for formatting tables.

