# arXiv:2603.21846v1[cs.AI]23 Mar 2026

## Agentic Personas for Adaptive Scientific Explanations with Knowledge Graphs

Susana Nunes[0000−0002−0160−5875], Tiago Guerreiro[0000−0002−0333−5792], and Catia Pesquita[0000−0002−1847−9393]

LASIGE, Faculdade de Ciências da Universidade de Lisboa, Portugal {scnunes,tjguerreiro,clpesquita}@ciencias.ulisboa.pt

Abstract. AI explanation methods often assume a static user model, producing non-adaptive explanations regardless of expert goals, reasoning strategies, or decision contexts. Knowledge graph-based explanations, despite their capacity for grounded, path-based reasoning, inherit this limitation. In complex domains such as scientific discovery, this assumption fails to capture the diversity of cognitive strategies and epistemic stances among experts, preventing explanations that foster deeper understanding and informed decision-making. However, the scarcity of human experts limits the use of direct human feedback to produce adaptive explanations. We present a reinforcement learning approach for scientific explanation generation that incorporates agentic personas, structured representations of expert reasoning strategies, that guide the explanation agent towards specific epistemic preferences. In an evaluation of knowledge graph-based explanations for drug discovery, we tested two personas that capture distinct epistemic stances derived from expert feedback. Results show that persona-driven explanations match state-of-the-art predictive performance while persona preferences closely align with those of their corresponding experts. Adaptive explanations were consistently preferred over nonadaptive baselines (n = 22), and persona-based training reduces feedback requirements by two orders of magnitude. These findings demonstrate how agentic personas enable scalable adaptive explainability for AI systems in complex and high-stakes domains.

Keywords: Knowledge Graphs · Adaptive Explainable AI · Reinforcement Learning

### 1 Introduction

Explainability is critical for user trust, adoption, and effective decision-making in highstakes domains such as healthcare, finance, and scientific research [9]. Knowledge graphs have emerged as trustworthy sources to support explanations by explicitly modeling relations between entities and enabling path-based reasoning that aligns with existing knowledge [20,35,26]. Yet knowledge graph-based explanations mirror most explainable AI (XAI) systems and still assume a generic user model, overlooking the fact that explanations are inherently contextual and must adapt to users’ expertise and decision contexts, but also to the specific decision contexts in which they operate [22,34,12].

![image 1](Nunes et al._2026_Agentic Personas for Adaptive Scientific Explanations with Knowledge Graphs_images/imageFile1.png)

- Fig.1: Non-adaptive (REx) and adaptive (persona-conditioned) explanation examples for Fenofibrate treats Coronary Artery Disease.


In domains such as biomedicine, experts bring diverse backgrounds and interpretive strategies to the interpretation of AI-generated evidence [38]. Experts may differ in whether they prioritize mechanistic or causal reasoning [16,36], require evidence of scientific validity [25], or weigh uncertainty and domain knowledge differently [29,11]. Explanation needs may further vary with the task at hand, such as hypothesis generation versus clinical decision-making [30]. These multiple perspectives reflect distinct epistemic stances — the characteristic ways in which different users interpret evidence, construct understanding, and justify conclusions — which are overlooked by current XAI approaches.

To address this challenge, we propose an adaptive explainability framework that conditions explanation generation on distinct epistemic stances rather than static user attributes. Unlike conventional personalization, which adapts to stable attributes such as expertise level, adaptive explainability adapts to how users reason about evidence. However, a key obstacle is the scarcity of individual-level user data: experts are limited in availability, and extensive profiling is impractical. To overcome this constraint, we introduce agentic personas, structured representations of expert reasoning strategies derived from expert feedback and instantiated using large language models. Rather than encoding demographic or role-based profiles, each persona captures a coherent interpretive strategy, including how experts balance mechanistic detail, explanation complexity, and task relevance.

We integrate agentic personas into a reinforcement learning (RL) framework by incorporating a persona-aligned reward function that guides the selection and framing of knowledge graph-based explanations. This enables adaptation to diverse epistemic stances without requiring individual user tracking, while preserving scientific validity. Figure 1 contrasts a non-adaptive explanation, which includes peripheral paths such as side effects, with a persona-conditioned explanation that prioritizes mechanistic directness.

Our approach is grounded in an expert evaluation study conducted in the context of drug discovery, which provides the empirical basis for constructing and validating agentic personas. Expert judgments collected in this study are used both to derive persona-

specific evaluation criteria and to assess whether the resulting personas faithfully reflect expert reasoning. Drug discovery offers a compelling setting due to its reliance on multi-level reasoning across molecular mechanisms, biological pathways, and clinical outcomes, as well as its high-stakes decision-making context.

In a comparative user study (n = 22), persona-conditioned explanations are consistently preferred over non-adaptive baselines and closely align with expert assessments across dimensions such as scientific validity, relevance, and completeness. These results demonstrate how agentic personas can support scalable adaptive explainability for expert-facing AI systems in high-stakes domains.

Our contributions include: (1) a conceptual grounding of adaptive explainability; (2) a scalable method to develop agentic personas that model expert diversity; and (3) a reinforcement learning framework that integrates these personas to generate adaptive explanations.

### 2 Related Work

#### 2.1 Knowledge Graph-based Explanations

Knowledge graphs enable mechanistic explanations by encoding biomedical entities and relationships [13], supporting hypothesis generation grounded in domain knowledge [10]. Reinforcement learning approaches such as DeepPath [37] and MINERVA [6] established path-based reasoning, forming the basis for explainable multi-hop inference. Recent work has improved explanatory quality: REx [24] jointly optimizes fidelity and relevance with ontological enrichment, while TxGNN [14] demonstrates that explanations can improve clinical decision accuracy. However, these systems produce non-adaptive explanations regardless of user expertise or reasoning strategy.

#### 2.2 Adaptive Explainability

Expert users bring distinct interpretive frameworks shaped by disciplinary training [36,34], yet most XAI systems assume a generic user model. Adaptive approaches face a data scarcity problem: individual-level profiling is costly in expert domains [5], while rolebased adaptation oversimplifies interpretive diversity [8].

Persona-based methods offer a middle ground. [31] showed that LLM-based synthesis of clustered behavioral data yields coherent user profiles, although [19] found that zero-shot LLM personas lack authenticity compared to data-grounded approaches. [23] reported limited benefits of personalization for lay users, but whether this extends to experts with established epistemic frameworks remains open. We address this gap by deriving agentic personas from clustered expert feedback and using them as reward models to guide explanation generation.

### 3 Problem Definition

We define a knowledge graph as G = (E,R,F), where E is the set of entities, R is the set of relations, and F ⊆ E × R × E is the set of triples denoted as (s,r,o) for subject, relation, and object. Building on [17,1,24] we establish the following definitions:

- Definition 1 (Hypothesis). A hypothesis is a predicted link between a subject s and an object o, h = (s,r,o), e.g., (fenofibrate, treats, coronary heart disease).
- Definition 2 (Explanation). Given a hypothesis h = (s,r,o), an explanation is a set of paths

X(h) = {p1,...,pm}

such that each path pj in G is selected by maximizing fidelity and relevance: pj ∈ arg max

p:s→o

α(p)β(p)

where α(p) and β(p) are the fidelity and relevance of p respectively.

Fidelity α indicates whether the explanatory path successfully connects s and o. Relevance β corresponds to the surprisal of a node appearing as a subject or object in a randomly sampled triple, ensuring that the explanation provides detailed insight (details in Supp. Materials).

However, there may be multiple paths connecting the subject and object of a hypothesis triple that fit the criteria of scientific explainability. Critically, it is established that experts even within the same field present a diversity of epistemic stances, and current explanation generation approaches are unable to capture them. Here, we propose adaptive explanations, i.e., explanations that are conditioned on particular epistemic stances.

- Definition 3 (Adaptive Explanation). Given a hypothesis h = (s,r,o) and an epistemic stance θ, an adaptive explanation is a set of paths

X(h | θ) = {p1,...,pm}

such that each path pj is selected by jointly maximizing fidelity, relevance, and epistemic alignment:

pj ∈ arg max p:s→o

f α(p),β(p), γ(p,θ) ,

where γ(p,θ) is the epistemic stance score of p under θ, and f is a multi-objective aggregation function.

- 4 Designing Adaptive Explanations


Adaptive explanations are predicated on capturing epistemic stances and using them to condition explanation generation. We adapt the knowledge-graph explanation framework proposed in [24], where explanatory paths are discovered via reinforcement learning.

To capture epistemic stances θ, we introduce agentic personas, structured representations of expert interpretive preferences that can be integrated into explanation generation. Inspired by reinforcement learning from human feedback (RLHF) [4], we condition explanation rewards on persona-based evaluation. Figure 2 presents our two-phase approach: (I) creating agentic personas from expert feedback, (II) training adaptive explanations via persona-conditioned reinforcement learning.

![image 2](Nunes et al._2026_Agentic Personas for Adaptive Scientific Explanations with Knowledge Graphs_images/imageFile2.png)

- Fig.2: Overview of the adaptive explainability approach. Phase I creates agentic personas through embedding, clustering, and LLM synthesis. Phase II uses persona-conditioned rewards in reinforcement learning.


#### 4.1 Creating Agentic Personas

We conducted an expert evaluation study with 11 biomedical experts assessing knowledge graph–based explanations across drug repurposing and drug–target interaction tasks. The purpose of this study was to identify systematic differences in expert interpretive preferences and to collect feedback necessary for persona construction.

Participants evaluated explanations generated from Hetionet [13], a heterogeneous biomedical knowledge graph integrating multiple data sources across drugs, genes, diseases, and biological processes. We presented ten hypotheses for two different tasks, drug repurposing prediction (DR) and drug-target interaction prediction (DTI). In each case, four explanations per hypothesis generated by different KG-based systems that prioritize different aspects were presented: MINERVA [6] (fidelity); PoLo [21] (fidelity and logic rules), REx [24] (fidelity and relevance), and RExLight (an ablated version of REx without ontological enrichment). Participants included PhD students, researchers, and professors with backgrounds in life sciences (n = 4), CS/AI with biomedical experience (n = 5), and hybrid computational biology (n = 2).

Participants rated explanations on three dimensions derived from the explanatory virtues of scientific theories [17]: relevance (whether the explanation highlights causal mechanisms informative for the prediction), completeness (balance between sufficient causal detail and parsimony), and validity (consistency with established biomedical principles). Responses used 5-point Likert scales.

We also collected extensive qualitative feedback for each explanation (see Supp. Materials) to inform the construction of agentic personas.

Persona Generation Our methodology draws from [31], who compare multiple approaches for persona generation and find that LLM-based summarization of clustered behavioral data yields the most coherent and actionable results. We adopt a three-stage process: semantic embedding of expert feedback, unsupervised clustering, and LLMbased narrative synthesis.

Recognizing the risks of persona essentialization [2], we specifically design our personas as epistemic stance proxies rather than user representations. Our approach: (i) captures explanatory preferences from observed expert rationales, not demographics;

- (ii) maintains traceability to cluster-level evidence with transparency documentation;


- (iii) focuses on task-specific evaluative language, minimizing identity descriptors; and
- (iv) validates persona credibility against aggregated expert ratings before deployment.


Input Representation and Embedding The expert evaluation study (n = 11) yielded 15 written responses (9 DR, 6 DTI), which included formal ratings and 125 statements providing rich explanatory feedback suitable for clustering.

Prior to embedding, all free-text comments were manually curated to ensure consistency and anonymity. We reformulated each statement into a standardized format using first-person declaratives such as “I prefer explanations that...” or “I avoid explanations where...”. This normalization preserved the subjective tone of the original feedback while enabling semantic alignment across responses. We removed references to explanation IDs or system names. Each curated response was aggregated into a single text block and encoded into a 768-dimensional dense vector using Sentence-BERT [27] (all-mpnet-base-v2 [33]). Embeddings were L2-normalized.

Clustering and Profile Discovery User response embeddings were clustered using three strategies: centroid-based (K-Means), hierarchical (Agglomerative), and densitybased (HDBSCAN) [15]. We evaluated cluster quality using Silhouette Score [28], Davies–Bouldin Index [7], Calinski–Harabasz Index [3], and Inertia. Candidate solutions ranged from k = 2 to k = 5, and final clusters were selected based on convergence across metrics and agreement between algorithms, balancing interpretability with internal consistency (see Section 6.1).

Narrative Generation via LLM To translate clusters into actionable personas, we prompted

an instruction-tuned LLM (OpenAI o3-pro) with all user records belonging to a given cluster, including curated preference statements, background metadata1, and structured analytical instructions (prompt template in Supp. Materials). The prompt guided the model to identify explanatory themes by frequency, distinguishing core traits (>40% of participants), secondary traits (25–40%), and weak signals (<25%); generate a naturalistic character profile; and produce an evidence summary documenting for each trait: (i) the number of participants who expressed it, (ii) the percentage of the cohort, and (iii) the disciplinary backgrounds of those participants.

#### 4.2 Adaptive Explanations

Persona-Conditioned Reward Epistemic stances are implemented as part of the RL reward mechanism. At the end of each RL rollout, the persona that captures the selected epistemic stance for training rates each path (prompt template in Supp. Materials) on validity (v), completeness (c), and relevance (r). The persona reward is a weighted combination normalized to [0,1]:

##### Rpersona = wv · v + wc · cˆ+ wr · r

1 Each participant’s background was classified into: Life Sciences, Computer Science/AI, Hybrid Computational Biology, CS/AI-heavy with Biomedical Experience, and Social Sciences/Legal (Other).

For reproducibility, we use equal weights wv = wc = wr = 1/3, ensuring no dimension dominates while allowing fair comparison across personas.

LLM-based Persona Evaluation To operationalize personas, we employ GPT-4omini prompted with the persona narrative. Each KG-based explanation is rendered as human-readable text showing the sequence of entities and relations, along with query context explaining the drug-disease relationship. GPT-4o-mini was selected empirically for its balance between cost efficiency and reasoning capability; this can be configured via environment variables to use other models.

Curriculum Learning Full persona evaluation for every path is unnecessary and costly. We adopt a self-paced curriculum that gradually raises requirements for invoking persona scoring: only paths achieving fidelity and exceeding a relevance threshold (τ) are evaluated by the persona. This threshold increases during training, letting the agent first master path-finding under lenient criteria before targeting higher-quality paths for persona alignment (reproducibility details in Supp. Materials). At inference, we fix the threshold to the value from the best-performing validation model, ensuring consistency between training and testing.

The reward for path pi and training step t is given by:

 

Rpersona(pi), if β(pi) > τrelevance(t), 0.25, if 0.5 ≤ β(pi) ≤ τrelevance(t), 0.10, if β(pi) < 0.5.

R(pi,t) = α(pi) ·



where small fixed rewards are assigned to medium and low relevance paths to avoid premature collapse.

### 5 Evaluation

#### 5.1 Agentic Personas

To understand whether agentic personas can capture expertise diversity and effectively serve as proxies for epistemic stances, we compared personas’ ratings for the same 40 explanations per task (DR and DTI) with the original assessment by human experts. The automated scoring presented explanations from all four systems together, mirroring how experts naturally compare alternatives. Persona ratings were compared against aggregated expert scores.

#### 5.2 Adaptive Explanations

We recruited 22 participants with biomedical backgrounds, including PhD students, postdocs, and researchers from both academic and industry settings (68.2% life sciences, 18.2% hybrid computational-biology, 13.6% CS/AI with biomedical experience).

Participants were primarily early-career researchers with strong molecular biology expertise (72.7% Competent or Expert) but limited KG/AI specialization, reflecting our target population of domain experts evaluating scientific explanations (demographics in Supp. Materials).

We selected drug repurposing as the evaluation setting because it is an interpretively demanding task, requiring reasoning across heterogeneous biomedical entities. Each participant evaluated ten hypotheses, viewing two explanations per hypothesis (20 total evaluations): one standard REx (non-adaptive) and one persona-conditioned (adaptive). We chose REx as the non-adaptive baseline to ensure a controlled comparison under identical architecture and training conditions. Both non-adaptive and adaptive explanations were generated by the models that achieved the best validation performance. Presentation order was randomized.

Persona Assignment. Participants were assigned to personas via three single-choice questions derived from each persona’s expert feedback (Figure 3). These questions captured discriminative characteristics between Elena and Leo: preferences for mechanistic detail (detailed step-by-step vs. streamlined), explanation complexity (direct mechanistic links vs. high-level ontological context), and predicate specificity (specific relations like “binds” vs. broader terms like “causes”). Each question offered two response options, each aligned to a persona. A detailed table mapping user quotes to questions is provided in Supp. Materials. Participants were assigned to the persona matching the majority of their responses (Elena: n = 10; Leo: n = 12). Both question and response order were randomized.

![image 3](Nunes et al._2026_Agentic Personas for Adaptive Scientific Explanations with Knowledge Graphs_images/imageFile3.png)

- Fig.3: Profiling questionnaire used to match participants to personas. For each question, the first response option (purple) aligns with Elena’s preferences, while the second option (green) aligns with Leo’s preferences. Response order was randomized for ordering effects.


Explanation Evaluation. For each explanation, participants rated validity, relevance, and completeness, then selected their preferred explanation with free-text justification. Graph-based explanations were accompanied by textual verbalizations generated via GPT-4o-mini (Figure 1). The verbalization system (prompt template in Supp. Materials) produced paragraph-style descriptions capturing pathways and relationships with-

out generic summarization; for adaptive explanations, verbalization incorporated the persona profile to reflect that persona’s interpretive priorities.

Predictive Performance. We also compared link prediction performance on the drug repurposing task between our adaptive explanation model and state-of-the-art approaches [6,21,24] to ensure predictive power was not sacrificed.

### 6 Results and Discussion

#### 6.1 Agentic Personas

Following the embedding process in Phase I, we applied three clustering algorithms and visualized results using PCA and t-SNE projections. The cohort exhibited optimal clustering at k = 2 with remarkable stability across all three algorithms (details in Supplementary Materials). The resulting clusters (n = 15 responses) yielded Elena (n = 13) and Leo (n = 2) (Figure 4). Additional mixture and stability checks revealed no consistent subclusters; all participants were directly assigned to clusters with no noise or singletons.

![image 4](Nunes et al._2026_Agentic Personas for Adaptive Scientific Explanations with Knowledge Graphs_images/imageFile4.png)

- Fig.4: t-SNE projection of expert response embeddings with Agglomerative clustering (k = 2). Clusters correspond to Elena (n = 13, light blue) and Leo (n = 2, dark blue).


The two personas represent distinct epistemic stances (example of narrative profile in Figure 5, with full narrative profiles and evidence summaries in Supp. Materials).

Elena reflects mechanistic rigor, demanding biologically grounded, mechanistically explicit explanations and rejecting vague predicates or loosely connected paths. Participants emphasized multiple evidence layers: “I prefer explanations that combine therapeutic, genetic, adverse-effect, and ontological information for maximal scientific validity.” Her cluster displayed near-unanimous preferences for clear relation types (e.g., “inhibits”, “upregulates”) and ontological layers only when directly relevant. Leo reflects

###### Persona Narrative: Elena

Tagline: Trusts nothing but rock-solid mechanistic logic. Profile: Elena weighs every therapeutic claim against hard mechanistic evidence. She expects an explanation to start with a clinically proven drug–disease link or a well-documented mode of action—microtubule inhibition, T-cell suppression, a binding IC50 in hand. Side-effect coincidences, vague “causes” predicates, or generic class labels make her skeptical unless an ontological note shows exactly why that class matters biologically. She welcomes extra layers—genetic markers, adverse-effect profiles, ontology tags—only when they tie directly to the core mechanism and keep the path lean. Superficial complexity or redundant paths lose her attention; a handful of well-justified edges beats a tangled web every time. Also values... Occasional ontological expansions that rescue an otherwise hidden mechanistic clue, provided they do not swamp the narrative. Background note: Elena’s community is split between bench researchers and AI modelers, and she holds both to the same rigorous standard of scientific plausibility.

Fig.5: Example of a persona narrative profile.

focused clarity, valuing concise relations that highlight a single anchoring connection. Participants called for bounded completeness: “I prefer explanations that offer multiple paths for completeness while limiting their number to avoid excessive complexity.” Leo participants penalized over-expansion, emphasizing that explanations should be simple yet sufficient.

Persona Credibility. Table 1 presents expert ratings from the expert evaluation study, which serves as ground truth for persona validation. Expert ratings showed high variance (SD 0.9–1.4) even for top-performing systems, reflecting the interpretive diversity that personas aim to capture.

As shown in Figure 6, persona ratings correlate significantly with expert ratings (all p < .001, n = 40 explanations per task). Elena demonstrated strong alignment for DR (r = 0.74–0.80) but weaker correlation for DTI (validity: r = 0.56; completeness: r = 0.62; relevance: r = 0.73). This task-dependent variation suggests that translating preferences into consistent scoring across biomedical contexts remains challenging despite unanimous agreement within her constituent group (n = 13; 8 DR, 5 DTI). Leo showed consistent correlations across both tasks (r = 0.71–0.91). Despite being derived from only two users (1 DR, 1 DTI), this persona captured preferences that generalized well, though this should be interpreted cautiously given the minimal sample size. These results suggest persona credibility is influenced by both size and heterogeneity of the constituent group.

#### 6.2 Adaptive Explanations

Ratings Evaluation The profiling instrument assigned 12 participants to Leo’s profile and 10 to Elena’s Profile. Figure 7 reveals higher ratings for adaptive explanations over the non-adaptive baseline across all three evaluation criteria and both personas. For relevance, Leo’s explanations achieved the highest average score of 4.02, compared to

- Table 1: Expert evaluation average ratings by system and task (means ± SD on 1–5 scale).


(a) Drug Repurposing (DR)

###### System Validity Relevance Completeness

MINERVA 3.1 ± 1.20 2.7 ± 1.07 2.6 ± 1.29 PoLo 2.9 ± 1.22 2.5 ± 1.11 2.5 ± 1.30 RExLight 3.7 ± 0.93 3.7 ± 0.92 3.9 ± 1.26 REx 4.0 ± 0.90 4.0 ± 0.93 3.9 ± 1.26

(b) Drug–Target Interaction (DTI)

###### System Validity Relevance Completeness

MINERVA 2.6 ± 1.36 2.3 ± 1.10 2.4 ± 1.33 PoLo 2.6 ± 1.35 2.4 ± 1.15 2.5 ± 1.39 RExLight 3.3 ± 1.11 3.3 ± 1.17 3.6 ± 1.17 REx 3.5 ± 1.11 3.6 ± 1.19 3.7 ± 1.18

non-adaptive explanations at 3.44. Elena’s explanations also outperformed non-adaptive ones with 3.77. Validity showed similar patterns, with Leo averaging 4.06 and Elena

- 3.81 versus non-adaptive at 3.50. The completeness criterion showed Elena achieving the largest gain with 3.88 compared to 3.45 for non-adaptive explanations, while Leo showed modest improvement at 3.55. Statistical analysis using Wilcoxon signed-rank tests confirmed these improvements (see details in Supp. Materials).


The improvements across metrics were strongly interrelated. Spearman correlation analysis revealed that improvements in relevance correlated to validity (rs = 0.699,p < .001) and completeness (rs = 0.548,p < .001). Validity and completeness improvements were moderately correlated (rs = 0.383,p < .001), suggesting that adaptive explanations provided coherent benefits across multiple dimensions of explanation quality.

Hypothesis-level analysis reveals substantial variation across different drug-disease pairs. For completeness, some hypotheses showed dramatic improvements with persona alignment: H1 increased from 2.55 (non-adaptive) to 4.40 (Elena), and H10 rose from

![image 5](Nunes et al._2026_Agentic Personas for Adaptive Scientific Explanations with Knowledge Graphs_images/imageFile5.png)

Fig.6: Pearson correlations (r) between persona and expert ratings. All p < .001.

- 4.09 to 4.60. Participants’ justifications illuminate these improvements, with one noting for H1 that the non-adaptive explanation “is too complex, as it considers a lot of similar drugs...the links are sometimes confusing,” while Elena was praised for being “simpler and it is enough for understanding the hypothesis”. However, for H3, the non-adaptive baseline remained competitive at 4.09, exceeding both Leo (3.00) and Elena (3.20). Validity improvements were particularly strong for H6, where scores increased from 3.32 (non-adaptive) to 4.33 (Leo), and H3, rising from 3.73 to 4.50. While individual hypotheses showed varying degrees of improvement, a Kruskal-Wallis test found no statistically significant differences in improvement magnitudes across hypotheses (H = 7.01,p = .636), suggesting that persona benefits, though variable in magnitude, were relatively consistent across different drug-disease pairs.


To assess how consistently experts applied each criterion, we examined inter-annotator

agreement using the Intraclass Correlation Coefficient ICC(3,k), a two-way mixedeffects consistency model [32], following [18] guidelines (ICC < 0.5: poor; 0.5–0.75: moderate; > 0.75: good). Expert agreement was moderate for non-adaptive explanations but diverged for adaptive conditions (Table 2): experts showed poor agreement across all metrics for Leo, but maintained moderate agreement for relevance and validity with Elena. Leo’s limited foundation (two users) may explain why different participants applied their own interpretive frameworks, whereas Elena’s larger user base achieved more consistent evaluation. This prompted a posterior credibility analysis where we assessed correlation between Leo ratings and the 12 participants assigned to it, confirming that Leo captures a meaningful interpretive stance: despite its small original formative base, Leo shows statistically significant correlations (p < 0.05) with aggregate expert ratings on validity (r = 0.56, p = .01), completeness (r = 0.47, p = .038), and relevance (r = 0.50, p = .024).

Preference Analysis Participants showed a clear preference for adaptive explanations (Figure 8). Leo and Elena users chose adaptive options 63.3% (binomial test, p = .005)

![image 6](Nunes et al._2026_Agentic Personas for Adaptive Scientific Explanations with Knowledge Graphs_images/imageFile6.png)

Fig.7: Average ratings by system across evaluation criteria. REx is the non-adaptive baseline; Leo and Elena are persona-conditioned.

- Table 2: Inter-annotator agreement (ICC(3,k)) by condition. Moderate agreement (≥ 0.5) in bold. Condition Relevance Completeness Validity

Non-adaptive (n=22) 0.64 0.71 0.64 Leo (n=12) -1.40 0.03 -0.17 Elena (n=10) 0.51 0.25 0.55

and 76.0% (p < .001) of the time, respectively. An analysis of participants’ freetext justifications revealed systematic persona differences. Leo participants cited nonadaptive explanations as “too complex” and “overwhelming”, preferring explanations that were “concise while retaining essential components” and excluded irrelevant information. Elena participants tolerated complexity when justified, valuing “a complete overview” without interpretive overload. A recurring paradox emerged: non-adaptive explanations were “overly detailed” yet “failing to provide necessary information”. Leo resolved this through conciseness and Elena through selective depth.

![image 7](Nunes et al._2026_Agentic Personas for Adaptive Scientific Explanations with Knowledge Graphs_images/imageFile7.png)

Fig.8: Participant preferences between adaptive and non-adaptive explanations.

Predictive Performance Table 3 indicates that persona-conditioned rewards guide the agent toward higher-quality paths without sacrificing fidelity to the underlying prediction task.

- Table 3: Performance comparison of various methods for the drug repurposing task on Hits@k and MRR metrics.


Method Hits@1 Hits@3 MRR MINERVA 0.264 0.409 0.370 PoLo 0.314 0.428 0.402 REx 0.338 0.461 0.427 Adaptive Explanations 0.358 0.483 0.438

Scalability Our reinforcement learning cycles required several thousand interaction steps to reach stable convergence, and we estimate that 5,000 expert-validated interactions would be needed to replace persona-based rewards entirely, a scale that is infeasible for domain experts. Figure 9 illustrates how a full training with human feedback would require approximately 250 hours (10.4 days) of expert time, whereas personabased training completes in 1.34 hours, a 187× speedup. At the single-evaluation level, persona feedback of a single explanation (2.1 seconds) is 86× faster than expert feedback (3 minutes).

![image 8](Nunes et al._2026_Agentic Personas for Adaptive Scientific Explanations with Knowledge Graphs_images/imageFile8.png)

Fig.9: Estimated feedback collection time for training explanation policies under different supervision conditions. Persona-based feedback reduces evaluation time by up to two orders of magnitude.

### 7 Conclusions

Our findings reveal a fundamental tension in explainable AI for scientific discovery: while experts share core requirements for explanatory quality, they diverge sharply in how they interpret specific explanation features. Instead, experts operate from distinct epistemic stances that transcend professional boundaries and tasks.

Moreover, adaptive explanations were strongly preferred by experts (63.3–76.0%). Importantly, agentic personas not only mirror expert feedback faithfully but also enable the training of adaptive explanation models without requiring extensive human feedback.

We introduce agentic personas as a scalable mechanism for adaptive explainability, enabling RL models to generate explanations conditioned on particular epistemic stances captured from expert feedback. Agentic personas and their role in adaptive explanations were evaluated in two critical and well-established drug development tasks based on biomedical knowledge graphs. Persona explanation ratings achieved high correlations (0.56–0.91) with those of human experts, demonstrating that LLM-synthesized profiles can capture genuine interpretive patterns. Moreover, adaptive explanations were strongly preferred by experts (63.3–76.0%). Importantly, agentic personas not only mir-

ror expert feedback faithfully but also enable the training of adaptive explanation models without requiring extensive human feedback.

A natural extension is the evaluation of adaptive explanations in other domains where interpretive diversity shapes decision-making, such as legal reasoning, educational assessment, or climate modeling. Nevertheless, this work provides a foundation for systems that recognize interpretive diversity in expert reasoning: a key step toward trustworthy human-AI collaboration in high-stakes domains.

Acknowledgments. Anonymous. This work was supported by FCT through the fellowship https://doi.org/10.54499/2023.00653.BD, and the LASIGE Research Unit, ref. UID/00408/2025. It was also partially supported by the KATY project, which has received funding from the European Union’s Horizon 2020 research and innovation program under grant agreement No 101017453, and by the CancerScan project by the EU’s HORIZON Europe research and innovation program under grant agreement No 101186829. It was also partially supported by the CancerScan project which received funding from the European Union’s Horizon Europe Research and Innovation Action (EIC Pathfinder Open) under grant agreement No. 101186829. Views and opinions expressed are however those of the author(s) only and do not necessarily reflect those of the European Union or the European Innovation Council and SMEs Executive Agency. Neither the European Union nor the granting authority can be held responsible for them.

###### Supplemental Material Statement Source. All resources will be available at GitHub.

Disclosure of Interests. The authors have no competing interests.

Declaration of use of Generative AI. The authors have not employed any Generative AI tools.

### References

- 1. Akujuobi, U., Kumari, P., Choi, J., Badreddine, S., Maruyama, K., Palaniappan, S.K., Besold, T.R.: Link prediction for hypothesis generation: an active curriculum learning infused temporal graph-based approach. Artificial Intelligence Review 57(9), 244 (2024)
- 2. Cabrero, D.G., Winschiers-Theophilus, H., Abdelnour-Nocera, J.: A critique of personas as representations of" the other" in cross-cultural technology design. In: Proceedings of the First African Conference on Human Computer Interaction. pp. 149–154 (2016)
- 3. Cali´nski, T., Harabasz, J.: A dendrite method for cluster analysis. Communications in Statistics-theory and Methods 3(1), 1–27 (1974)
- 4. Christiano, P.F., Leike, J., Brown, T., Martic, M., Legg, S., Amodei, D.: Deep reinforcement learning from human preferences. Advances in neural information processing systems 30

(2017)

- 5. Conati, C., Barral, O., Putnam, V., Rieger, L.: Toward personalized xai: A case study in intelligent tutoring systems. Artificial intelligence 298, 103503 (2021)
- 6. Das, R., Dhuliawala, S., Zaheer, M., Vilnis, L., Durugkar, I., Krishnamurthy, A., Smola, A., McCallum, A.: Go for a walk and arrive at the answer: Reasoning over paths in knowledge bases using reinforcement learning. arXiv preprint arXiv:1711.05851 (2017)
- 7. Davies, D.L., Bouldin, D.W.: A cluster separation measure. IEEE transactions on pattern analysis and machine intelligence (2), 224–227 (2009)


- 8. Delaunay, J., Largouët, C., Galárraga, L., Van Berkel, N.: Adaptation of ai explanations to users’ roles. In: HCXAI 2023-Workshop on Human-Centered Explainable AI. pp. 1–7 (2023)
- 9. Doshi-Velez, F., Kim, B.: Towards a rigorous science of interpretable machine learning. arXiv preprint arXiv:1702.08608 (2017)
- 10. Durán, J.M.: Dissecting scientific explanation in ai (sxai): A case for medicine and healthcare. Artificial Intelligence 297, 103498 (2021)
- 11. Gaube, S., Suresh, H., Raue, M., Merritt, A., Berkowitz, S.J., Lermer, E., Coughlin, J.F., Guttag, J.V., Colak, E., Ghassemi, M.: Do as ai say: susceptibility in deployment of clinical decision-aids. NPJ digital medicine 4(1), 31 (2021)
- 12. Haque, A.B., Islam, A.N., Mikalef, P.: Explainable artificial intelligence (xai) from a user perspective: A synthesis of prior literature and problematizing avenues for future research. Technological Forecasting and Social Change 186, 122120 (2023)
- 13. Himmelstein, D.S., Lizee, A., Hessler, C., Brueggeman, L., Chen, S.L., Hadley, D., Green, A., Khankhanian, P., Baranzini, S.E.: Systematic integration of biomedical knowledge prioritizes drugs for repurposing. Elife 6, e26726 (2017)
- 14. Huang, K., Chandak, P., Wang, Q., Havaldar, S., Vaid, A., Leskovec, J., Nadkarni, G.N., Glicksberg, B.S., Gehlenborg, N., Zitnik, M.: A foundation model for clinician-centered drug repurposing. Nature Medicine 30(12), 3601–3613 (2024)
- 15. Jain, A.K.: Data clustering: 50 years beyond k-means. Pattern recognition letters 31(8), 651– 666 (2010)
- 16. Jiménez-Luna, J., Grisoni, F., Schneider, G.: Drug discovery with explainable artificial intelligence. Nature Machine Intelligence 2(10), 573–584 (2020)
- 17. Keas, M.N.: Systematizing the theoretical virtues. Synthese 195(6), 2761–2793 (2018)
- 18. Koo, T.K., Li, M.Y.: A guideline of selecting and reporting intraclass correlation coefficients for reliability research. Journal of chiropractic medicine 15(2), 155–163 (2016)
- 19. Lazik, C.K., Katins, C., Kauter, C., Jakob, J., Jay, C., Grunske, L., Kosch, T.: The impostor is among us: Can large language models capture the complexity of human personas? In: Proceedings of the Mensch Und Computer 2025. p. 434–451. MuC ’25, Association for Computing Machinery, New York, NY, USA (2025). https://doi.org/10.1145/ 3743049.3743057, https://doi.org/10.1145/3743049.3743057
- 20. Lecue, F.: On the role of knowledge graphs in explainable ai. Semantic Web 11(1), 41–51

(2020)

- 21. Liu, Y., Hildebrandt, M., Joblin, M., Ringsquandl, M., Raissouni, R., Tresp, V.: Neural multihop reasoning with logical rules on biomedical knowledge graphs. In: European Semantic Web Conference. pp. 375–391. Springer (2021)
- 22. Miller, T.: Explanation in artificial intelligence: Insights from the social sciences. Artificial intelligence 267, 1–38 (2019)
- 23. Nimmo, R., Constantinides, M., Zhou, K., Quercia, D., Stumpf, S.: User characteristics in explainable ai: The rabbit hole of personalization? In: Proceedings of the 2024 CHI Conference on Human Factors in Computing Systems. pp. 1–13 (2024)
- 24. Nunes, S., Badreddine, S., Pesquita, C.: Rewarding explainability in drug repurposing with knowledge graphs. In: Kwok, J. (ed.) Proceedings of the Thirty-Fourth International Joint Conference on Artificial Intelligence, IJCAI-25. pp. 4624–4632. International Joint Conferences on Artificial Intelligence Organization (8 2025). https://doi.org/10. 24963/ijcai.2025/515, https://doi.org/10.24963/ijcai.2025/515, main Track
- 25. Ponzoni, I., Páez Prosper, J.A., Campillo, N.E.: Explainable artificial intelligence: A taxonomy and guidelines for its application to drug discovery. Wiley Interdisciplinary Reviews: Computational Molecular Science 13(6), e1681 (2023)
- 26. Rajabi, E., Etminani, K.: Knowledge-graph-based explainable ai: A systematic review. Journal of information science 50(4), 1019–1029 (2024)


- 27. Reimers, N., Gurevych, I.: Sentence-bert: Sentence embeddings using siamese bertnetworks. In: Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing. Association for Computational Linguistics (11 2019), https:// arxiv.org/abs/1908.10084
- 28. Rousseeuw, P.J.: Silhouettes: a graphical aid to the interpretation and validation of cluster analysis. Journal of computational and applied mathematics 20, 53–65 (1987)
- 29. Schaffer, J., O’Donovan, J., Michaelis, J., Raglin, A., Höllerer, T.: I can do better than your ai: expertise and explanations. In: Proceedings of the 24th international conference on intelligent user interfaces. pp. 240–251 (2019)
- 30. Schoonderwoerd, T., Jorritsma, W., Neerincx, M., Bosch, K.: Human-centered xai: Developing design patterns for explanations of clinical decision support systems. International Journal of Human-Computer Studies 154, 102684 (06 2021). https://doi.org/10. 1016/j.ijhcs.2021.102684
- 31. Shin, J., Hedderich, M.A., Rey, B.J., Lucero, A., Oulasvirta, A.: Understanding human-ai workflows for generating personas. In: Proceedings of the 2024 ACM Designing Interactive Systems Conference. pp. 757–781 (2024)
- 32. Shrout, P.E., Fleiss, J.L.: Intraclass correlations: uses in assessing rater reliability. Psychological bulletin 86(2), 420 (1979)
- 33. Song, K., Tan, X., Qin, T., Lu, J., Liu, T.Y.: Mpnet: Masked and permuted pre-training for language understanding. Advances in Neural Information Processing Systems 33, 16857– 16867 (2020)
- 34. Suresh, H., Gomez, S.R., Nam, K.K., Satyanarayan, A.: Beyond expertise and roles: A framework to characterize the stakeholders of interpretable machine learning and their needs. In: Proceedings of the 2021 CHI conference on human factors in computing systems. pp. 1– 16 (2021)
- 35. Tiddi, I., Schlobach, S.: Knowledge graphs as tools for explainable machine learning: A survey. Artificial Intelligence 302, 103627 (2022)
- 36. Wu, Z., Chen, J., Li, Y., Deng, Y., Zhao, H., Hsieh, C.Y., Hou, T.: From black boxes to actionable insights: a perspective on explainable artificial intelligence for scientific discovery. Journal of Chemical Information and Modeling 63(24), 7617–7627 (2023)
- 37. Xiong, W., Hoang, T., Wang, W.Y.: Deeppath: A reinforcement learning method for knowledge graph reasoning. arXiv preprint arXiv:1707.06690 (2017)
- 38. Yu, F., Moehring, A., Banerjee, O., Salz, T., Agarwal, N., Rajpurkar, P.: Heterogeneity and predictors of the effects of ai assistance on radiologists. Nature Medicine 30(3), 837–849


(2024)

