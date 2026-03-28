arXiv:2504.05496v1[cs.CL]7 Apr 2025

# A Survey on Hypothesis Generation for Scientiﬁc Discovery in the Era of Large Language Models

Atilla Kaan Alkan1,11, Shashwat Sourav2,11, Maja Jablonska3,11, Simone Astarita4,11,

Rishabh Chakrabarty5,11, Nikhil Garuda6,11, Pranav Khetarpal7,11, Maciej Pi´oro8,11,

Dimitrios Tanoglidis9,11, Kartheik G. Iyer10,11, Mugdha S. Polimera1,11, Michael J. Smith11,

Tirthankar Ghosal12,11, Marc Huertas-Company13,11, Sandor Kruk14,11,

Kevin Schawinski15,11 & Ioana Ciuca˘16,11

- 1 Center for Astrophysics, Harvard & Smithsonian, Cambridge, MA, USA
- 2 Washington University in St. Louis
- 3 Australian National University
- 4 European Commission, Joint Research Centre (JRC)
- 5 Intelligent Internet Inc.
- 6 University of Arizona
- 7 Indian Institute of Technology, Delhi
- 8 Institute of Fundamental Technological Research, Polish Academy of Sciences
- 9 Walgreens Boots Alliance AI Lab
- 10 Columbia University
- 11 UniverseTBD
- 12 Oak Ridge National Laboratory
- 13 Instituto de Astrof´ısica de Canarias
- 14 European Space Agency
- 15 Modulos AG
- 16 Stanford University


## Abstract

Hypothesis generation is a fundamental step in scientiﬁc discovery, yet it is increasingly challenged by information overload and disciplinary fragmentation. Recent advances in Large Language Models (LLMs) have sparked growing interest in their potential to enhance and automate this process. This paper presents a comprehensive survey of hypothesis generation with LLMs by (i) reviewing existing methods, from simple prompting techniques to more complex frameworks, and proposing a taxonomy that categorizes these approaches; (ii) analyzing techniques for improving hypothesis quality, such as novelty boosting and structured reasoning; (iii) providing an overview of evaluation strategies; and (iv) discussing key challenges and future directions, including multimodal integration and human-AI collaboration. Our survey aims to serve as a reference for researchers exploring LLMs for hypothesis generation.

## 1 Introduction

Hypothesis generation is a fundamental component of scientiﬁc discovery, enabling researchers to formulate testable predictions and uncover new insights. This process has tra-

ditionally relied on human intuition, experience, and domain expertise. However, as the volume of scientiﬁc literature grows drastically, researchers face challenges in assimilating relevant knowledge across disciplines. This information saturation creates bottlenecks that hinder the discovery of new insights.

From a philosophy of science perspective, a hypothesis can be deﬁned as a tentative explanation or prediction about a phenomenon, formulated in a way that allows for empirical testing and potential falsiﬁcation (Popper, 1959). Despite its crucial role in the scientiﬁc method, hypothesis generation remains constrained by disciplinary silos and cognitive overload. Traditional approaches struggle to integrate knowledge across ﬁelds, limiting researchers’ ability to identify interdisciplinary connections that may lead to groundbreaking discoveries.

In this context, generative Large Language Models (LLMs) such as GPT (Radford & Narasimhan, 2018), PaLM (Chowdhery et al., 2022), LLaMA (Touvron et al., 2023), and Mistral (Jiang et al., 2023) have emerged as promising systems to overcome these barriers. By leveraging vast repositories of scientiﬁc texts, LLMs can process, synthesize, and generate novel hypotheses, assisting human expertise and facilitating interdisciplinary research. Since the introduction of LLMs, there has been a growing research interest in hypothesis generation using these models, as illustrated in. The number of research papers on this topic has signiﬁcantly risen, highlighting the increasing recognition of LLMs’ potential in scientiﬁc exploration.

Despite their promise, LLM-driven hypothesis generation presents several challenges. Evaluating generated hypotheses remains a complex issue, requiring novelty, relevance, feasibility, signiﬁcance, and clarity assessment. A major concern is ensuring that LLMs generate innovative hypotheses rather than paraphrasing existing knowledge. Furthermore, the quality and diversity of training data play a crucial role in the effectiveness of these models. Biases present in the datasets can inﬂuence the generated hypotheses, potentially reinforcing existing perspectives while overlooking unconventional or groundbreaking ideas. Furthermore, integrating LLMs into the scientiﬁc process requires addressing issues related to interpretability, reliability, and validation of machine-generated hypotheses.

In this paper, we aim to provide a comprehensive overview of the state of hypothesis generation using LLMs. We examine the current methodologies, categorize existing approaches into a structured taxonomy, and discuss the challenges and limitations inherent in this emerging ﬁeld. By addressing these aspects, we seek to outline key research directions for the community on the generation of LLM-based hypotheses.

## 2 Paper Collection Methodology

We employed a systematic literature retrieval strategy combining keyword-based search and manual curation to construct a comprehensive and historically grounded survey of computational approaches to scientiﬁc hypothesis generation. The primary objective was to capture studies spanning both pre-LLM methods (e.g., literature-based discovery (LBD) and early NLP techniques) and more recent approaches involving LLMs.

### 2.1 Search Strategy

We queried the arXiv API to retrieve relevant publications for this survey paper. No explicit time range was imposed on the queries; the retrieved papers span a publication range from 2005 to 2025. To ensure domain relevance, we restricted the search to papers categorized under Computer Science, speciﬁcally within the cs.CL (Computation and Language) category. We used a curated list of search terms designed to reﬂect the thematic scope of our study, covering core concepts, traditional approaches, and recent methods involving natural language processing and large language models. The full list of search terms is presented in Table 2.1.

![image 4](Alkan et al._2025_A Survey on Hypothesis Generation for Scientific Discovery in the Era of Large Language Models_images/imageFile4.png)

Core Concepts Recent Techniques Traditional Techniques hypothesis generation NLP for hypothesis

![image 5](Alkan et al._2025_A Survey on Hypothesis Generation for Scientific Discovery in the Era of Large Language Models_images/imageFile5.png)

Swanson hypothesis discovery

generation

open discovery system scientific discovery large language models

language models scientific discovery

scientific hypothesis generation

ABC model literature discovery

hypothesis generation

automated scientific discovery

knowledge graph hypothesis generation

semantic predications scientific discovery

question generation scientific research

semantic indexing hypothesis generation

literature based discovery

natural language processing scientific discovery

machine learning hypothesis generation automated reasoning for discovery discovery using LLMs

![image 6](Alkan et al._2025_A Survey on Hypothesis Generation for Scientific Discovery in the Era of Large Language Models_images/imageFile6.png)

Table 1: Search terms used for systematic retrieval, grouped by theme.

### 2.2 Inclusion Criteria

Since our search was conducted exclusively via the arXiv API, the articles retrieved are primarily pre-prints. However, many of these works may have subsequently appeared in peer-reviewed journals, conference proceedings, or workshop venues. We included all papers that satisﬁed at least one of the following criteria, regardless of their publication status at the time of retrieval:

- • The paper proposes or evaluates an automated or semi-automated method for scientiﬁc hypothesis generation;
- • The work addresses scientiﬁc discovery through natural language processing, knowledge graph mining, or large language models;
- • The paper contributes theoretical insights or historical perspectives on scientiﬁc discovery, particularly regarding the role of AI in hypothesis formulation.


### 2.3 Review Process

After initial ﬁltering based on titles and abstracts, the remaining set of papers was manually screened for relevance and categorized according to methodological paradigm (e.g., LBD, NLP, LLMs, hybrid systems), scientiﬁc domain (e.g., biomedicine, astrophysics, chemistry), and hypothesis representation. This classiﬁcation enabled us to trace the evolution of techniques and the shifts in hypothesis formalization over time.

## 3 Methods for Scientiﬁc Hypothesis Generation

In this section, we review the existing methods for generating scientiﬁc hypotheses. As illustrated in Figure 1, we present methods ranging from early approaches such as literaturebased discovery (LBD), text mining, and statistical learning methods to more recent techniques, including graph-based models and LLM.

### 3.1 Human-Centric

Human-centric methods are based on researchers’ expertise, intuition, and theoretical and practical knowledge. In this approach, individual insights gained through years of research

Human-CentricLBD

| | |
|---|---|
| | |
| | |
| | |
| | |


Text-Mining

Supervised Learning

SHG

Graph Based

Prompting

| | |
|---|---|
| | |
| | |
| | |


LLM-Driven

Fine-Tuning

RAG

Knowledge Graphs

Figure 1: Taxonomy of Methods for Scientiﬁc Hypothesis Generation (SHG).

and practical exposure play an important role in forming new hypotheses. Researchers engage in brainstorming sessions and discussions, where their knowledge and observational skills help identify new trends and anomalies (Swanson, 1986a; Nonaka, 2009). This method takes into account the ability of an individual to grasp context-speciﬁc nuances and reinterpret existing information. However, this method can have cognitive biases and the risk of overreliance on conventional paradigms, which may limit the exploration of less familiar or interdisciplinary ideas.

### 3.2 Literature-based Discovery

Literature-based discovery (LBD) leverages computational tools to mine the vast scientiﬁc literature for implicit or previously overlooked connections between concepts not directly linked in published research. The foundational idea of LBD introduced by Swanson (1986b), relies on the notion of ”undiscovered public knowledge”—information that exists in the literature but remains unconnected due to disciplinary silos or the overwhelming volume of publications. The author’s seminal study, which identiﬁed a potential link between ﬁsh oil and Raynaud’s syndrome by connecting disparate literature, remains a landmark example of this approach. Over time, LBD has evolved to incorporate advances in text mining, natural language processing (NLP), and semantic analysis, enabling the automated discovery of hidden relationships at scale (Smalheiser, 2017). Several systems have been devel-

oped to operationalize LBD. One of the earliest tools, ARROWSMITH (Smalheiser & Swanson, 1998), identiﬁes intermediate terms (B) that link two disjoint sets of articles (A and C), thereby suggesting novel hypotheses. More recent systems have expanded the methodological toolkit. MOLIERE (Sybrandt et al., 2017), for example, builds semantic networks from MEDLINE and other biomedical data using topic modelling techniques such as Latent Dirichlet Allocation (Blei et al., 2003) and phrase mining to uncover latent themes and suggest short conceptual paths between topics. KnIT (Spangler et al., 2014) is another sys-

- tem that extracts factual statements from the literature, represents them in a queryable network and applies information diffusion algorithms to generate hypotheses, such as discovering novel kinases that phosphorylate p53. Other approaches rely on structured vocabularies like the Medical Subject Headings (MeSH, (Lipscomb, 2000)) to build proﬁlebased representations of concepts and identify indirect links between them. Systems like DiseaseConnect (Liu et al., 2014) and BrainSCANr (Voytek & Voytek, 2012) also apply text mining to biomedical abstracts to uncover latent semantic features and generate novel associations. LBD remains especially valuable in information-rich domains, where human researchers may miss non-obvious connections across disciplines. By systematically surfacing these links, LBD tools support cross-domain discovery and can help accelerate hypothesis formulation in complex scientiﬁc landscapes.


Supervised Learning Statistical computing methods are robust and data-driven for the hypothesis generation task. This set of methods uses statistical tools such as regression, clustering and Bayesian inference. On the other hand, computational approaches, including machine learning algorithms and network analysis, extend these tools by handling higher dimensional data and investigating complex, multivariate relations that may exist in the data. Some of the recent works (Breiman, 2003).

### 3.3 LLM-Driven

Large Language Models (LLMs) have recently emerged as powerful tools for scientiﬁc hypothesis generation. Figure 2 summarizes the pipeline and the common techniques used to generate hypothesis Their capacity to process vast corpora of scientiﬁc texts and synthesize information makes them particularly well-suited to this task. The literature reveals many methods that leverage LLMs to assist in or fully automate the generation of scientiﬁc hypotheses. These methods can be categorized as follows:

Direct and Adversarial Prompting Direct prompting involves formulating clear and concise instructions to perform hypothesis generation directly using an LLM. In this method, users design a prompt explicitly asking the model to propose potential explanations or predictions based on a given context. One can ask the LLM a question or give it direct instruction about a topic, and it responds with possible ideas or explanations. This approach beneﬁts from its simplicity and ease of implementation, allowing researchers to quickly gauge the model’s capacity for innovative reasoning (Radford & Narasimhan, 2018). However, the output quality highly depends on the prompt’s clarity and the model’s inherent understanding of the subject matter. The adversarial prompting approach is designed to make the LLM go beyond its standard response patterns by introducing counterfactual or challenging scenarios. By deliberately framing prompts in a way that exposes the model to unconventional perspectives, researchers can encourage the generation of hypotheses that diverge from common assumptions. This method can involve contrasting ideas or setting up dilemmas that force the model to explore unexplored paths of reasoning. Adversarial prompting not only tests the robustness of the LLM but also helps in detecting biases inherent in its training data, ultimately leading to more diversiﬁed and potentially groundbreaking insights (Chowdhery et al., 2023).

Fine-tuning Rather than relying solely on prompting, this method involves ﬁne-tuning an LLM on domain-speciﬁc datasets containing both foundational knowledge and corresponding hypotheses extracted from the literature. This tuning process enables the model to learn the patterns and context typically associated with hypothesis formulation. In one

study, a temporally split biomedical dataset was used to test the model’s capacity to generate plausible hypotheses after ﬁne-tuning.

Knowledge Integration Some methods incorporate structured knowledge from scientiﬁc knowledge graphs to improve relevance and reduce hallucinations. These graphs encode entities and their relationships, which serve as grounding information for the LLM. A representative approach, KG-CoI (Knowledge-Grounded Chain of Ideas), uses graphs for context retrieval, chain-of-thought generation, and hallucination detection, improving the reliability of generated hypotheses (Xiong et al., 2024). Integrating knowledge in this form can help overcome some shortcomings of classical text-based RAG (Retrieval-Augumented Generation), such as the potential omission of rare but crucial information. Graph structures can also capture causal relationships between concepts and prove useful when generating hypotheses bridging selected concepts, as demonstrated by Tong et al. (2024).

Multi-Agent System This approach introduces multiple LLM agents with different roles -such as analyst, scientist, or critic - that interact to collaboratively generate and evaluate hypotheses. Through dialogue and feedback between agents, this framework aims to produce more innovative and better-grounded scientiﬁc ideas.

Research Problem / Input

LLM Core

Direct & Adversarial Prompting

Knowledge Integration

Fine-Tuning

Multi-Agent System

Generated Hypotheses

Figure 2: Pipeline of LLM-Driven Hypothesis Generation. The process begins with a research problem, which is processed by the LLM core. Various methodological branches (e.g., Direct & Adversarial Prompting, Fine-Tuning, and Knowledge Integration) contribute to a multi-agent framework that converges to generate hypotheses.

## 4 Evaluation Methodologies

Evaluating systems for scientiﬁc hypothesis generation is a complex task. Unlike traditional NLP evaluation, hypothesis generation aims to produce novel, plausible, and testable scientiﬁc ideas—often in domains where ground truth is incomplete or nonexistent. This open-endedness renders standard evaluation metrics insufﬁcient and necessitates a multi-faceted approach combining human expertise, automated metrics, multimodal integration, and domain-speciﬁc validation. In this section, we ﬁrst review established methodologies before outlining promising directions for future research.

### 4.1 Human Expert Evaluation

Expert Assessment Protocols Evaluations conducted by domain experts remain the most reliable method for assessing the relevance, originality, and scientiﬁc merit of machinegenerated hypotheses. Over time, these assessments have become more structured and methodologically rigorous. Recent protocols have involved large panels of experts from diverse academic backgrounds to evaluate hypotheses along dimensions such as clarity, innovation potential, and expected impact. Comparative studies have shown that, when supported by LLMs, researcherscan generate more compelling and diverse ideas than with traditional search-based workﬂows. Such ﬁndings suggest that expert-in-the-loop systems not only support hypothesis reﬁnement but can also enhance ideation itself.

In highly specialized ﬁelds such as biomedicine, structured evaluations have been designed to focus on clinical relevance and biological plausibility. Frameworks developed for this purpose often involve expert reviews centred on real-world applicability and potential translational impact. Some benchmark efforts have incorporated expert assessments across multiple research tasks, offering a broader view of how LLMs contribute to domainspeciﬁc scientiﬁc workﬂows.

Blind Review and Pairwise Comparison To reduce bias and ensure fair evaluation, blind review protocols are increasingly employed. In these settings, experts are unaware whether a human or an AI system has generated a hypothesis. This approach has revealed that, in many cases, AI-generated hypotheses can be as highly rated—or even surpass—those written by human researchers regarding novelty and scientiﬁc interest. Building on this principle, some recent evaluation strategies employ direct pairwise comparisons in tournamentstyle formats, where hypotheses compete against each other and are ranked based on expert preference. These structured comparison schemes offer a scalable and interpretable method for evaluating generative systems.

Multi-Rater Reliability One of the persistent challenges in expert-based evaluation is achieving consistency across annotators. Scientiﬁc hypothesis assessment often involves subjective judgment, leading to variability in ratings. Earlier studies have highlighted relatively low agreement levels among reviewers, emphasizing the complexity of the task. However, newer frameworks are addressing this by introducing more formalized scoring rubrics, multiple rounds of review, and collaborative assessment protocols. These improvements have contributed to more stable and reproducible evaluation outcomes, reﬂecting a growing understanding of effectively integrating human judgment into validating AIgenerated scientiﬁc content.

### 4.2 Automated Evaluation

Text-based Relevance Initial efforts to evaluate LLM outputs relied heavily on surfacelevel metrics such as BLEU and ROUGE, which measure word overlap between generated and reference hypotheses. However, such metrics often fall short of capturing the semantic depth and scientiﬁc value of an idea. As a result, more sophisticated evaluation tools have been developed that incorporate semantic precision and recall, as well as hybrid scores that combine symbolic and neural representations. These allow for a more meaningful assessment of whether a hypothesis is contextually appropriate and scientiﬁcally relevant.

Additionally, some benchmarks now include domain-speciﬁc metrics tailored to the complexity and requirements of particular research tasks, such as code execution or model reproducibility.

Model-Based Metrics Recent evaluation frameworks have increasingly turned to large language models as evaluators of generated hypotheses. When ﬁne-tuned or provided with structured prompts, these models can approximate human-level assessments across dimensions such as plausibility, novelty, and relevance. Some systems now rely on LLMs to score hypotheses using composite metrics that account not only for internal coherence but also for broader scientiﬁc context. For instance, measures have been developed to quantify how dissimilar a proposed idea is from past knowledge and how closely it aligns with emerging literature trends, thus reﬂecting historical uniqueness and prospective impact.

Novelty Assessment Measuring novelty remains one of the central goals in hypothesis evaluation. Automated approaches have evolved to estimate the originality of ideas by analyzing their semantic distance from existing publications. This often involves embeddingbased comparisons using pre-trained scientiﬁc language models combined with ranking strategies that assess the rarity or innovation of proposed connections. Some systems build structured citation graphs or ideation chains to contextualize a hypothesis within a broader intellectual lineage, enabling more informed judgments about its uniqueness.

Domain-Speciﬁc Evaluation Evaluation strategies tailored to speciﬁc scientiﬁc ﬁelds are increasingly recognized as essential due to the varied standards of evidence, feasibility, and validation across disciplines. In biomedical research, hypothesis evaluation often relies on alignment with curated clinical databases or known gene-disease associations, enabling automated cross-referencing against structured biomedical knowledge. In the chemical sciences, evaluation protocols typically focus on structural validity and chemical plausibility, incorporating techniques such as molecular simulation or synthesis pathway prediction. Astronomy and astrophysics present unique challenges, where hypothesis evaluation may involve the integration of large-scale observational datasets or comparing generated hypotheses with complex knowledge graphs. Social science domains, on the other hand, prioritize theoretical grounding and temporal context, often requiring evaluation of whether a hypothesis is consistent with existing paradigms or predictive of future trends. These domain-speciﬁc practices underscore the importance of aligning evaluation methodologies with disciplinary norms, highlighting the need for adaptable frameworks that can accommodate the epistemological diversity of modern science.

## 5 Challenges and Future Research Directions

Despite substantial progress in developing LLM-based systems for scientiﬁc hypothesis generation, several critical challenges remain unresolved. One of the most pressing concerns is the issue of factual accuracy. LLMs are known to produce outputs that, while syntactically coherent and contextually plausible, can include erroneous or fabricated claims. This phenomenon, often referred to as hallucination, poses signiﬁcant risks in scientiﬁc settings. Closely related is the challenge of interpretability. Most LLMs function as black-box systems, making it difﬁcult to understand or trace the rationale behind speciﬁc hypotheses. This lack of transparency undermines trust and complicates the validation process, especially when hypotheses are intended to serve as the foundation for empirical research.

Bias is another persistent issue. Given that LLMs are trained on large, heterogeneous corpora, they tend to reproduce—and occasionally amplify—preexisting societal biases. These biases can inﬂuence the direction and framing of generated hypotheses, potentially skewing research priorities and excluding underrepresented perspectives. At the same time, the computational cost of training and deploying these models remains prohibitive for many institutions. The high energy and hardware requirements not only limit accessibility but also raise concerns about environmental sustainability. Domain adaptation poses additional hurdles. While ﬁne-tuning on specialized datasets can enhance performance in speciﬁc ﬁelds, it often introduces the risk of overﬁtting, compromising the model’s ability

- to generalize across topics. Furthermore, the ethical implications of AI-generated hypotheses—from questions of authorship and accountability to the potential misuse of misleading hypotheses—remain largely unaddressed, necessitating the development of robust governance mechanisms.


To overcome these limitations, new methodological directions are emerging. Retrievalaugmented generation, which integrates LLMs with external scientiﬁc databases, offers a promising approach to grounding outputs in veriﬁable knowledge and reducing hallucinations. Another direction involves incorporating chain-of-thought reasoning or rationale tracing mechanisms, enabling models to generate not only hypotheses but also the reasoning pathways that led to their formulation. This increased transparency can help researchers evaluate the internal coherence and plausibility of generated ideas. Multi-agent collaborative frameworks are also gaining traction. Inspired by the collaborative nature of scientiﬁc inquiry, these systems simulate peer review or debate among virtual agents to reﬁne and evaluate hypotheses dynamically. In the realm of ﬁne-tuning, meta-learning and cross-domain transfer techniques are being explored to better balance specialization and generalization, allowing models to adapt ﬂexibly to a variety of scientiﬁc domains without sacriﬁcing rigour.

From a computational perspective, advances in model compression and energy-efﬁcient architectures are expected to democratize access to LLM-based tools, making them more practical for research institutions with limited resources. At the same time, methodological co-design with ethicists, legal scholars, and domain experts is increasingly recognized as essential to developing socially responsible AI tools. Future systems should embed ethical safeguards, including bias detection, provenance tracking, and clear attribution protocols, directly into their design.

Complementing these methodological innovations, the ﬁeld must adopt more sophisticated evaluation frameworks. Traditional metrics such as BLEU and ROUGE fall short of capturing hypotheses’ semantic depth and scientiﬁc merit. In response, several novel evaluation paradigms are being developed. Scientiﬁc veriﬁability benchmarks, for instance, aim to assess whether generated hypotheses can be empirically tested or veriﬁed in realworld research. Temporal evaluation methods propose tracking the evolution of ideas over time—through citations, modiﬁcations, or integrations into published work—to assess long-term scientiﬁc impact. Evaluating the diversity and redundancy of generated hypotheses has also become a key area of interest, as the capacity to propose a broad range of novel ideas is a fundamental indicator of exploratory potential.

Another promising direction involves multi-modal evaluation, where hypotheses are assessed not just through text-based metrics but also through visualizations, structured knowledge graphs, or experimental data. Human-in-the-loop evaluation protocols are likewise gaining prominence. These frameworks involve iterative collaboration between researchers and models, enabling dynamic reﬁnement and contextual validation of hypotheses. Finally, developing interdisciplinary evaluation standards is increasingly necessary as hypothesis-generation systems are deployed across various scientiﬁc domains. These standards must be ﬂexible enough to accommodate domain-speciﬁc norms while preserving core principles such as novelty, relevance, veriﬁability, and scientiﬁc integrity.

In summary, while LLM-based systems have demonstrated considerable potential in augmenting scientiﬁc discovery, their limitations call for caution and innovation. Addressing persistent challenges such as factual inaccuracy, opacity, and domain sensitivity will require a coordinated effort across AI, domain science, and ethics. At the same time, the emergence of new methodological and evaluation paradigms offers a promising path toward developing robust, transparent, and impactful hypothesis-generation tools that align with the evolving standards of scientiﬁc research.

## 6 Conclusion

While Large Language Models have revolutionized the domain of automated text generation, their application in scientiﬁc hypothesis generation is still in its nascent stages and

ﬁlled with challenges. Issues such as factual inaccuracies, lack of interpretability, inherent biases, and high computational demands underscore the need for continued research and innovation. This paper has reviewed the state-of-the-art methods for LLM-driven hypothesis generation and critically examined the accompanying limitations. Future research must prioritize the development of more transparent, efﬁcient, and ethically sound models that can reliably support scientiﬁc inquiry. By addressing these challenges through interdisciplinary collaboration and methodological advances, the scientiﬁc community can unlock the full potential of LLMs, ultimately paving the way for transformative breakthroughs in knowledge discovery.

## References

David M. Blei, Andrew Y. Ng, and Michael I. Jordan. Latent dirichlet allocation. J. Mach. Learn. Res., 3(null):993–1022, March 2003. ISSN 1532-4435.

Leo Breiman. Statistical modeling: The two cultures. Quality control and applied statistics, 48

(1):81–82, 2003.

Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung, Charles Sutton, Sebastian Gehrmann, Parker Schuh, Kensen Shi, Sasha Tsvyashchenko, Joshua Maynez, Abhishek Rao, Parker Barnes, Yi Tay, Noam M. Shazeer, Vinodkumar Prabhakaran, Emily Reif, Nan Du, Ben Hutchinson, Reiner Pope, James Bradbury, Jacob Austin, Michael Isard, Guy Gur-Ari, Pengcheng Yin, Toju Duke, Anselm Levskaya, Sanjay Ghemawat, Sunipa Dev, Henryk Michalewski, Xavier Garc´ıa, Vedant Misra, Kevin Robinson, Liam Fedus, Denny Zhou, Daphne Ippolito, David Luan, Hyeontaek Lim, Barret Zoph, Alexander Spiridonov, Ryan Sepassi, David Dohan, Shivani Agrawal, Mark Omernick, Andrew M. Dai, Thanumalayan Sankaranarayana Pillai, Marie Pellat, Aitor Lewkowycz, Erica Moreira, Rewon Child, Oleksandr Polozov, Katherine Lee, Zongwei Zhou, Xuezhi Wang, Brennan Saeta, Mark D´ıaz, Orhan Firat, Michele Catasta, Jason Wei, Kathleen S. Meier-Hellstern, Douglas Eck, Jeff Dean, Slav Petrov, and Noah Fiedel. Palm: Scaling language modeling with pathways. ArXiv, abs/2204.02311, 2022. URL https://api.semanticscholar.org/CorpusID:247951931.

Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung, Charles Sutton, Sebastian Gehrmann, et al. Palm: Scaling language modeling with pathways. Journal of Machine Learning Research, 24(240):1–113, 2023.

Albert Qiaochu Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris Bamford, Devendra Singh Chaplot, Diego de Las Casas, Florian Bressand, Gianna Lengyel, Guillaume Lample, Lucile Saulnier, L’elio Renard Lavaud, Marie-Anne Lachaux, Pierre Stock, Teven Le Scao, Thibaut Lavril, Thomas Wang, Timoth´ee Lacroix, and William El Sayed. Mistral 7b. ArXiv, abs/2310.06825, 2023. URL https://api.semanticscholar.org/CorpusID:263830494.

C.E. Lipscomb. Medical Subject Headings (MeSH). Bulletin of the Medical Library Association, 88(3):265, 2000.

Chun-Chi Liu, Yu-Ting Tseng, Wenyuan Li, Chia-Yu Wu, Ilya Mayzus, Andrey Rzhetsky, Fengzhu Sun, Michael Waterman, Jeremy J. W. Chen, Preet M. Chaudhary, Joseph Loscalzo, Edward Crandall, and Xianghong Jasmine Zhou. Diseaseconnect: a comprehensive web server for mechanism-based disease–disease connections. Nucleic Acids Research, 42(W1):W137–W146, 06 2014. ISSN 0305-1048. doi: 10.1093/nar/gku412. URL https://doi.org/10.1093/nar/gku412.

Ikujiro Nonaka. The knowledge-creating company. In The economic impact of knowledge, pp. 175–187. Routledge, 2009.

Karl R. Popper. The Logic of Scientiﬁc Discovery. Routledge, London, 1959. ISBN 0415278449.

Alec Radford and Karthik Narasimhan. Improving language understanding by generative pre-training. 2018. URL https://api.semanticscholar.org/CorpusID:49313245.

Neil R Smalheiser. Rediscovering don swanson: The past, present and future of literaturebased discovery. Journal of Data and Information Science, 2(4), 2017.

Neil R Smalheiser and Don R Swanson. Using arrowsmith: a computerassisted approach to formulating and assessing scientiﬁc hypotheses. Computer Methods and Programs in Biomedicine, 57(3):149–153, 1998. ISSN 0169-2607. doi: https://doi.org/10.1016/S0169-2607(98)00033-9. URL https://www.sciencedirect.com/science/article/pii/S0169260798000339.

Scott Spangler, Angela D. Wilkins, Benjamin J. Bachman, Meena Nagarajan, Tajhal Dayaram, Peter Haas, Sam Regenbogen, Curtis R. Pickering, Austin Comer, Jeffrey N. Myers, Ioana Stanoi, Linda Kato, Ana Lelescu, Jacques J. Labrie, Neha Parikh, Andreas Martin Lisewski, Lawrence Donehower, Ying Chen, and Olivier Lichtarge. Automated hypothesis generation based on mining scientiﬁc literature. In Proceedings of the 20th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, KDD ’14, pp. 1877–1886, New York, NY, USA, 2014. Association for Computing Machinery. ISBN 9781450329569. doi: 10.1145/2623330.2623667. URL https://doi.org/10.1145/2623330.2623667.

Don R Swanson. Fish oil, raynaud’s syndrome, and undiscovered public knowledge. Perspectives in biology and medicine, 30(1):7–18, 1986a.

Don R Swanson. Undiscovered public knowledge. The Library Quarterly, 56(2):103–118, 1986b.

Justin Sybrandt, Michael Shtutman, and Ilya Safro. Moliere: Automatic biomedical hypothesis generation system, 2017. URL https://arxiv.org/abs/1702.06176.

Song Tong, Kai Mao, Zhen Huang, Yukun Zhao, and Kaiping Peng. Automating psychological hypothesis generation with ai: when large language models meet causal graph. Humanities and Social Sciences Communications, 11(1):896, July 2024. ISSN 2662-9992. doi: 10.1057/s41599-024-03407-5.

Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timoth´ee Lacroix, Baptiste Rozi`ere, Naman Goyal, Eric Hambro, Faisal Azhar, Aur´elien Rodriguez, Armand Joulin, Edouard Grave, and Guillaume Lample. Llama: Open and efﬁcient foundation language models. ArXiv, abs/2302.13971, 2023. URL https://api.semanticscholar.org/CorpusID:257219404.

Jessica B. Voytek and Bradley Voytek. Automated cognome construction and semiautomated hypothesis generation. Journal of Neuroscience Methods, 208(1):92–100, 2012. ISSN 0165-0270. doi: https://doi.org/10.1016/j.jneumeth.2012.04.019. URL https://www.sciencedirect.com/science/article/pii/S0165027012001513.

Guangzhi Xiong, Eric Xie, Amir Hassan Shariatmadari, Sikun Guo, Stefan Bekiranov, and Aidong Zhang. Improving scientiﬁc hypothesis generation with knowledge grounded large language models, 2024. URL https://arxiv.org/abs/2411.02382.

