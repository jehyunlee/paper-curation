![image 1](Han et al._2026_MolQuest A Benchmark for Agentic Evaluation of Abductive Reasoning in Chemical Structure Elucidatio_images/imageFile1.png)

![image 2](Han et al._2026_MolQuest A Benchmark for Agentic Evaluation of Abductive Reasoning in Chemical Structure Elucidatio_images/imageFile2.png)

# arXiv:2603.25253v1[cs.CL]26 Mar 2026

## MolQuest: A Benchmark for Agentic Evaluation of Abductive Reasoning in Chemical Structure Elucidation

Taolin Han*1, Shuang Wu*1, Jinghang Wang*1, Yuhao Zhou1, Renquan Lv1, Bing Zhao†1, and Wei Hu†1

1Alibaba Group, Hangzhou, China

*The first three authors contributed equally to this work. †Corresponding authors.

### Abstract

Large language models (LLMs) hold considerable potential for advancing scientific discovery, yet systematic assessment of their dynamic reasoning in real-world research remains limited. Current scientific evaluation benchmarks predominantly rely on static, single-turn Question Answering (QA) formats, which are inadequate for measuring model performance in complex scientific tasks that require multi-step iteration and experimental interaction. To address this gap, we introduce MolQuest, a novel agent-based evaluation framework for molecular structure elucidation built upon authentic chemical experimental data. Unlike existing datasets, MolQuest formalizes molecular structure elucidation as a multi-turn interactive task, requiring models to proactively plan experimental steps, integrate heterogeneous spectral sources (e.g., NMR, MS), and iteratively refine structural hypotheses. This framework systematically evaluates LLMs’ abductive reasoning and strategic decision-making abilities within a vast and complex chemical space.Empirical results reveal that contemporary frontier models exhibit significant limitations in authentic scientific scenarios: notably, even state-of-the-art (SOTA) models achieve an accuracy of only approximately 50%, while the performance of most other models remains below the 30% threshold. This work provides a reproducible and extensible framework for science-oriented LLM evaluation, our findings highlight the critical gap in current LLMs’ strategic scientific reasoning, setting a clear direction for future research toward AI that can actively participate in the scientific process.

Keywords: LLM, AI for Science, Chemical Reasoning, Dynamic Benchmarking

### 1 Introduction

Large Language Models (LLMs) are demonstrating significant value in scientific discovery, with their applications emerging as a key frontier in "AI for Science" re-

search [1]. Recently, the successive releases of new models with strong reasoning capabilities—such as GPT-5.2 [2], Gemini 3-Pro [3], and Qwen-3-Max [4]—have made it increasingly critical to explore their practical abilities in complex and dynamic real-world research scenarios.

![image 3](Han et al._2026_MolQuest A Benchmark for Agentic Evaluation of Abductive Reasoning in Chemical Structure Elucidatio_images/imageFile3.png)

Figure 1: Molecular structure elucidation as a Constraint Satisfaction Problem (CSP).

A quintessential example of such a core scientific task is molecular structure elucidation in chemistry, which involves deducing the precise structure of an unknown compound from discrete, multimodal experimental data (e.g., mass spectrometry, NMR spectra). [5] Molecular structure elucidation is, in essence, a high-dimensional constraint satisfaction problem. [6] The model must synergistically integrate experimental data—often incomplete and noisy—from multiple spectroscopic techniques. Together, these data impose a set of chemical constraints that delineate plausible final structures, encompassing key information such as molecular formula, degree of unsaturation, functional group types, and their local chemical environments. [7] The challenge of this task fundamentally arises

from the complex and highly sensitive mapping between chemical structures and spectral signals. A positional isomerism involving an oxygen atom can significantly alter the chemical shifts and coupling constants in the 1H NMR spectrum; conversely, subtle differences in spectral features may correspond to entirely distinct molecular skeletons [8]. As shown in Figure 1, successful structure elucidation therefore requires robust abductive reasoning capabilities: the ability to begin with observed spectral signals, systematically generate chemically plausible candidate structural hypotheses, actively plan and acquire new experimental evidence to introduce additional constraints, iteratively eliminate untenable hypotheses, and ultimately converge on a structure that is logically consistent with all known data under chemical principles.

Although several benchmarks have been proposed to evaluate the scientific capabilities of LLMs, they remain notably limited in assessing a model’s ability to address authentic research problems. We summarize these limitations along three dimensions:

Evaluation format. Mainstream benchmarks (e.g., ChemBench) typically adopt static, single-turn multiplechoice formats, which can lead to difficulty saturation and make performance susceptible to training-data contamination [9]. Data authenticity. Some benchmarks (e.g., ChemIQ) rely on synthetic simulation data, which fails to capture key real-experiment artifacts such as noise, peak overlap, complex coupling effects, and systematic peakposition deviations [10]. Lack of initiative. Most existing designs omit the experimental planning and strategic decision-making that are central to real scientific workflows, reducing the model to a passive respondent [11]. In practice, scientists operate in a partially observable decision-making environment and must select the most informative next experiment under cost constraints [12].

To address these gaps, we propose MolQuest, an innovative agent-based dynamic benchmark for molecular structure elucidation. Our central aim is to evaluate the abductive reasoning and strategic planning capabilities of “LLM as a Chemist”—treating the large language model as an autonomous agent capable of operating within a simulated laboratory environment, thereby examining its scientific problem-solving abilities in dynamic real-world research contexts.

Unlike existing benchmarks, MolQuest is characterized by three core features, as Figure 2:

Dynamic Interactive Paradigm: The model operates as an autonomous agent within a virtual laboratory, actively invoking tools (e.g., “Measure Molecular Weight,” “Obtain 1H NMR Spectrum”) to acquire information as needed while iteratively refining its structural hypotheses in the process.

Real-Data-Driven Construction: To ensure both realism and fairness in evaluation scenarios, we established

- a rigorous human-in-the-loop data pipeline. Over half of all test cases are extracted and validated from supporting information in chemical literature published after 2025,


effectively mitigating the risk of data contamination.

Multi-Dimensional Capability Assessment: We conducted a comprehensive evaluation of 12 state-of-the-art LLMs on MolQuest. Moving beyond simple final-answer accuracy, the evaluation framework incorporates multiple metrics—including evaluated the decision-making logic and reasoning capabilities of LLMs in complex environments.

### 2 Related Work

#### 2.1 Contemporary Large ReasoningModels

The field of artificial intelligence is undergoing a paradigm shift toward reasoning-centric architectures. The new generation of large-scale language models dedicates substantially increased computational resources during the inference phase to tackle complex logical challenges. Leading models such as the OpenAI o-series and GPT5.2 [2] have moved beyond traditional pattern matching, adopting inference-time strategies like chain-of-thought and search to enable structured problem decomposition. Gemini 3 Pro[3] maintains logical coherence in multi-step tasks through a fine-grained thinking mechanism with adjustable depth. Claude 4.5 [13] Opus employs a hybrid reasoning architecture where its deliberate approach strengthens logical verification while preserving practicality. Open-source models have also achieved significant breakthroughs: DeepSeek-R1 [14] utilizes reinforcement learning to encourage self-correction during generation, while models like Qwen3-Max [4] dedicated symbolic reasoning modules, substantially enhancing their capacity to handle complex scientific problems. Collectively, these advances represent a transition from passive content generation to active problem-solving, establishing a more robust computational foundation for scientific discovery.

#### 2.2 Evolution of General ReasoningBenchmarks

The evaluation framework for large language models is systematically evolving from knowledge retrieval to deep reasoning assessment. Early benchmarks such as GPQA test deep comprehension through "search-proof" questions requiring doctoral-level expertise. [15] Extending evaluation across dozens of disciplines, Humanity’s Last Exam reveals persistent gaps in models’ academic capabilities even with multimodal inputs. [16] Meanwhile, ARC-AGI2 exposes structural deficiencies in the fundamental reasoning of current AI systems by testing compositional generalization in knowledge-free environments. [17] This evolutionary trajectory clearly indicates that the focus of assessment has shifted from surface-level knowledge coverage to the systematic measurement of deep reasoning quality.

#### 2.3 Evaluations in the Chemical Domain

Within the AI for Science framework, the assessment of chemical intelligence has evolved significantly from basic capability testing to complex problem-solving. General chemistry benchmarks like ChemBench [9] and ChemEval [18] foundational evaluation systems covering broad curricular content, while specialized frameworks such as QCBench [19] and ChemLLMBench [20] focus more on quantitative computation and property prediction tasks. To deeply evaluate molecular understanding, ChemIQ [10] and FGBench [21] are specifically designed for functional group identification, whereas MolPuzzle [11] simulate real structure elucidation processes and ChemCoTBench [22] simulate multi-step reasoning tasks. Current chemical domain evaluations still face two key limitations: on one hand, even benchmarks emphasizing abductive reasoning like NMR-Challenge [23] are constrained by the use of synthetic data; on the other hand, existing agent-based systems such as CHEMAGENT [24] primarily focus on forward prediction in idealized environments, failing to adequately capture the iterative decision-making inherent in authentic scientific research. While MaCBench [25] provides a comprehensive evaluation of experimental workflows, it lacks a metric for measuring model selection strategies.

![image 4](Han et al._2026_MolQuest A Benchmark for Agentic Evaluation of Abductive Reasoning in Chemical Structure Elucidatio_images/imageFile4.png)

Figure 2: The characteristics of our benchmark.

3 MolQuest Framework

#### 3.1 Benchmark Overview

Existing evaluations of Large Language Models (LLMs) in scientific discovery predominantly rely on static, singleturn question-answering (QA) formats. However, such benchmarks are inadequate for assessing the proactive

planning, strategic decision-making, and iterative reasoning capabilities essential for authentic, dynamic scientific research.

To bridge this gap, we introduce MolQuest, a novel benchmark designed to evaluate the cognitive capabilities of the “LLM-as-a-Chemist.” Our core philosophy reframes the classic problem of molecular structure elucidation from a static QA task into a sequential decisionmaking process. By constraining the agent with real experimental data and costs, MolQuest establishes a dynamic evaluation paradigm that mirrors actual laboratory workflows.

The benchmark’s complexity stems from its integration of authentic, multi-modal experimental data—including raw NMR and MS spectra alongside their textual interpretations. As illustrated in Figure 3, these data are modularized to serve as environmental feedback, creating reasoning challenges that closely approximate the noise and ambiguity of real-world scenarios.

Unlike traditional one-shot evaluations that provide all evidence upfront, MolQuest immerses the model in a simulated research environment characterized by information asymmetry. Key spectral data are not disclosed initially; instead, they must be requested on-demand based on the agent’s evolving hypotheses. This design compels the agent to perform abductive reasoning under conditions of incomplete information and resource constraints (simulating experimental costs), akin to a human chemist.

To achieve this, the construction of MolQuest rests on two complementary pillars:

- 1. Authentic, Traceable Scenarios: Moving beyond

synthetic examples, we construct evaluation tasks directly from the Supporting Information of high-quality chemical literature (detailed in Section 3.2). This ensures that the inherent characteristics of real research—such as data noise, spectral overlap, and information gaps—are faithfully preserved.

- 2. A Cognitive-Simulation Framework: We design


a state-machine-driven environment (detailed in Section 3.3) that enforces a “Plan–Request–Reason” loop. This framework shapes the agent’s behavior through specific instructions and simulated tools, directly evaluating its ability to translate static knowledge into dynamic, costaware problem-solving.

In summary, by integrating complex real-world data with an interactive decision-making mechanism, MolQuest establishes a rigorous testbed for scientific AI that evaluates whether large language models can transcend passive knowledge retrieval to exhibit the proactive, strategic, and resource-efficient reasoning required for autonomous scientific discovery.

#### 3.2 Task Definition and Data Construc-tion

![image 5](Han et al._2026_MolQuest A Benchmark for Agentic Evaluation of Abductive Reasoning in Chemical Structure Elucidatio_images/imageFile5.png)

Figure 3: Data processing pipeline

In this work, we formalize molecular structure elucidation as a Constraint Satisfaction Problem (CSP). Given an initial unknown sample, the agent’s objective is to identify a chemically valid molecular structure that is consistent with a series of spectral evidence (e.g., NMR, MS) obtained through simulated experiments.

During the data extraction process, the Large Language Model (LLM) outputs exhibited several systematic errors that necessitated manual human intervention for correction. Misinterpretation of exchangeable protons. The model frequently failed to identify missing hydroxyl (−OH) or carboxylic acid (−COOH) protons within NMR datasets. SMILES atom counting errors. Significant enumeration errors occurred during atom counting when the model processed SMILES strings. Peak deviation false alarms. In spectroscopic analysis, the model often incorrectly flagged valid peaks as erroneous due to minor but acceptable chemical shift deviations. Mass spectrometry adduct confusion. The model consistently confounded the absolute molecular mass (M) with observed adduct ion peaks, such as [M +H]+ or [M +Na]+. These failure modes underscore the necessity for rigorous human oversight when utilizing LLMs to handle complex chemical informatics.

To ensure high fidelity and scientific accuracy, we constructed a library of evaluation scenarios derived from recent chemical literature. We implemented a rigorous Human-in-the-Loop data pipeline (Figure 3) that combines the efficiency of LLM-based automation with the precision of expert validation. This pipeline consists of three distinct phases:

Phase 1: Automated Extraction and Structuring. We employed a multi-agent LLM system to parse raw Supporting Information (SI) PDFs. A collaborative architecture—comprising a Segmenter to isolate individual molecular entries, a Spectroscopist to extract IUPAC names and spectral data, and a Judge for real-time error checking—transforms unstructured text into structured

JSON records. This automated stage handles the highvolume ingestion of raw data.

- Phase 2: Chemical Intelligence and Verification. Ex-

tracted data undergo strict validation using cheminformatics tools. IUPAC names are converted to SMILES via authoritative APIs (PubChemPy) or rule-based parsers (OPSIN), explicitly prohibiting LLM hallucination. Theoretical properties (e.g., MW, Formula) are computed via RDKit as ground truth. Subsequently, an auxiliary LLM performs logical consistency checks—such as verifying proton counts in 1H NMR against the molecular formula—to flag potential contradictions.

- Phase 3: Human-in-the-Loop Final Review. Given


the complexity of spectral interpretation, automated validation cannot guarantee 100% accuracy. Therefore, all system-flagged entries ("red-flag" data) are routed to a visual review interface. Human chemistry experts examine the original text and extracted structures to correct subtle errors (e.g., stereochemistry or peak assignment ambiguities), serving as the ultimate safeguard for benchmark quality.

Through this pipeline, we established a robust dataset of 530 validated molecular elucidation tasks, covering a diverse chemical space with molecular weights ranging from 150 to 500 Da. This library provides a reliable foundation for evaluating dynamic scientific reasoning.

![image 6](Han et al._2026_MolQuest A Benchmark for Agentic Evaluation of Abductive Reasoning in Chemical Structure Elucidatio_images/imageFile6.png)

Figure 4: Comparison of Chemical Reasoning and Decision-Making Between Large Language Models and Human Chemists in Molquest

#### 3.3 Interactive Agent Framework Design

To assess dynamic reasoning, we construct an interactive simulation environment modeled as a state machine. In this setup, the LLM acts as a “Senior Spectroscopist” tasked with determining molecular structures under resource constraints.

Table 1: The Action Space: List of simulated experimental tools available to the agent in MolQuest.

Tool Name Description Check_Data Check available data types in the

database for the current molecule. Measure_MW Measure molecular weight (simulating Mass Spectrometry). Measure_Formula Measure molecular formula (simulating High-Resolution MS). Calculate_DBE Calculate the Degree of Unsaturation (DBE).

Get_1H_NMR Acquire 1H NMR spectrum data (proton signals). Get_13C_NMR Acquire 13C NMR spectrum data (carbon signals). Get_19F_NMR Acquire 19F NMR spectrum data (fluorine signals). Get_31P_NMR Acquire 31P NMR spectrum data (phosphorus signals). Get_IR Acquire Infrared Spectroscopy (IR) data.

Get_HRMS Acquire full High-Resolution Mass Spectrometry data.

Get_MS Acquire standard Mass Spectrometry data.

Get_Melting_Point Acquire melting point data. Get_TLC Acquire Thin-Layer Chromatogra-

phy (TLC) data. Get_Optical_Rotation Acquire optical rotation data.

##### 3.3.1 Agent Persona and Objectives

Via a detailed system prompt (Appendix C.3), the agent is instructed to operate within a simulated laboratory. Its behavior follows three core principles:

Active Planning: Rather than receiving all data at once, the agent must strategically query specific experimental tools based on current uncertainty. The complete action space consists of 14 simulated instruments, as detailed in Table 1. Iterative Abduction: The agent adheres to a “Hypothesize–Validate–Refine” loop. [26] It continuously integrates new evidence to update its structural hypotheses and confidence levels. Termination and Output: The agent autonomously decides when sufficient evidence is gathered. It then terminates the task by submitting a structured FINAL_RESULT containing the predicted SMILES string and a self-assessed confidence score (0– 100%).

ment retrieves the corresponding real-world spectral data, updates the state to St+1, and incurs a simulated cost. This cycle continues until termination, directly measuring the model’s ability to translate static knowledge into dynamic problem-solving. [27]

#### 3.4 Evaluation Protocol and Metrics

To provide a comprehensive assessment of the “LLM-asa-Chemist,” we define a set of metrics covering structural correctness, chemical plausibility, and probabilistic reliability, as reported in our main experiments.

##### 3.4.1 Chemical Correctness and Plausibility

Structure Accuracy: The primary success metric, defined as the percentage of cases where the predicted SMILES string is canonically identical to the ground truth. [28] SMILES Validity Rate: The proportion of generated SMILES strings that can be successfully parsed into valid chemical graphs by cheminformatics toolkits (e.g., RDKit), indicating the model’s grasp of chemical syntax. Formula Conservation: A logical consistency metric measuring the percentage of predictions where the molecular formula of the generated structure exactly matches the ground truth formula. This serves as a critical check for hallucination, ensuring the model respects the massbalance constraints imposed by experimental data. Average Similarity: For incorrect predictions, we calculate the Tanimoto similarity [29] (based on Morgan fingerprints) between the predicted and ground truth structures. This metric quantifies partial success, indicating how chemically close the model’s hypothesis was to the correct answer.

##### 3.4.2 Probabilistic Reliability

Since autonomous agents must gauge their own certainty, we evaluate the reliability of their self-assessment using Root Mean Square Calibration Error (RMSCE) [30]. This metric assesses the alignment between the agent’s reported confidence scores and its actual accuracy. A lower RMSCE indicates a better-calibrated model that assigns high confidence to correct answers and low confidence to incorrect ones—a trait essential for reliable scientific automation.

##### 3.3.2 Interaction Mechanism

The interaction is formalized as a sequential decision process. At each step t, the state St consists of the dialogue history and currently acquired data. The agent observes St and executes an action at (either a tool call from Table 1 or a final answer). If a tool is called, the environ-

### 4 Experiments

This section evaluates state-of-the-art LLMs on MolQuest to assess their absolute capabilities, reliability, and the specific impact of the dynamic agentic paradigm compared to static baselines.

- 4.1 Experimental Setup


- 4.1.1 Dataset


The MolQuest benchmark used in this study consists of 530 independent molecular elucidation cases extracted from the Supporting Information of recent (post-2025) high-quality chemical literature (see Appendix A). It is intended solely for evaluation, with no train/val split. The dataset covers a molecular weight range of 150-500 Da and includes diverse functional groups (e.g., carbonyls, hydroxyls, aromatic rings, nitrogen-containing heterocycles) and chiral centers, ensuring broad coverage and complexity in chemical space (see Figures 1-3 in the Appendix A for chemical space visualizations).

##### 4.1.2 Evaluated Models

We evaluated twelve state-of-the-art general-purpose LLMs of varying scales and families: Claude Opus

- 4.5 [31], Gemini 3 Pro [3] , Claude Sonnet 4.5 [32], Gemini


3 Flash [33], Claude Haiku 4.5 [34], DeepSeek V3.2 [35] , DeepSeek V3.1 [36] , Qwen3 Max [4] , Gemini 2.5 Pro [37] , Kimi K2 Thinking [38] , DeepSeek V3.2 Thinking [35],GPT-5.2 [2]. The temperature was set to 0 for all models to increase determinism.

##### 4.1.3 Evaluation Configurations

We conduct evaluations under two distinct configurations:

Agent (Dynamic Interactive): The primary setup where models operate within the MolQuest interactive framework (Section 3.3). No hard limit is placed on interaction rounds; the agent decides when to terminate by submitting a FINAL_RESULT. This jointly assesses final correctness, decision confidence, and interaction efficiency. Baseline (Static One-shot): An ablation setup where models receive all relevant spectral data at once and are prompted to output the structure directly (prompt in Appendix C.4). This serves as a control to isolate the effect of dynamic interaction.

Metrics: We report Structure Accuracy (Exact SMILES Match), Validity Rate, Average Similarity (Tanimoto), Calibration Error, and Formula Conservation (consistency between predicted structure and ground truth formula).

Ablation Rationale: The comparison between Agent and Baseline is designed to decouple foundational chemical knowledge from strategic reasoning. While the Baseline measures the model’s ability to map a complete set of spectroscopic data to a structure (pattern matching), the Agent configuration evaluates the model’s capacity for hypothesis-driven information acquisition and sequential logic.

#### 4.2 Overall Performance

The comparative performance of evaluated LLMs across both Agent and Baseline configurations is summarized in

Table 2. Our analysis reveals several key insights into the current state of “LLM-as-a-Chemist.”

##### 4.2.1 Performance Hierarchy and FoundationCapabilities

Models exhibit a stark tri-modal distribution in performance. The Frontier Group, led by Gemini 3 Flash (51.51%) and Gemini 3 Pro (48.30%), achieves a significant lead, effectively setting the state-of-the-art for the MolQuest benchmark. Notably, their high baseline accuracy suggests that the Gemini 3 family possesses a superior internal representation of the spectra-to-structure mapping, likely due to enhanced multi-modal pre-training on aligned chemical data.

The Mid-tier Group (e.g., Claude Opus 4.5, Gemini 2.5 Pro) stabilizes between 20–30% accuracy, while the Struggling Group (e.g., DeepSeek V3.1, Qwen3 Max in baseline) fails to cross the 10% threshold. This suggests that for complex molecular elucidation, general-purpose reasoning is insufficient without a robust foundational understanding of chemical topology and spectral interpretation.

##### 4.2.2 Chemical Consistency and HallucinationControl

The Formula Conservation and SMILES Validity metrics provide a rigorous check against stochastic “guessing.”

High-Fidelity Reasoning: Gemini 3 Pro achieves a remarkable 93.57% formula conservation, indicating a strict adherence to mass-balance constraints derived from MS data. This suggests the model does not merely generate “plausible-looking” SMILES but actively constrains its structural search space within the provided molecular formula. Connectivity Hallucination: Conversely, models like DeepSeek v3.1 exhibit a disconnect between evidence and generation, with conservation rates as low as 23.71%. This indicates a “hallucination-driven” failure mode where the model ignores spectral constraints to output familiar but incorrect structural motifs.

##### 4.2.3 Probabilistic Reliability and Self-Assessment

The Calibration Error reveals the models’ metacognitive ability—knowing when they are likely to be wrong. Claude Opus 4.5, despite not being the most accurate, demonstrates the highest reliability with the lowest calibration error (15.43% in Baseline). This trait is critical for autonomous research; a well-calibrated model can signal for human intervention when its confidence is low. In contrast, the Thinking models (DeepSeek V3.2 Thinking and Kimi K2) show relatively high calibration errors in the agentic setting, suggesting that internal “thought traces” do not always translate into accurate self-assessment of the final structural output.

Table 2: Main results on MolQuest under the Agent and Baseline settings.

Model Accuracy (%) Validity Rate (%) Average Similarity (%) Calibration Error (%) Formula Conservation (%) Agent Baseline Agent Baseline Agent Baseline Agent Baseline Agent Baseline

claude-haiku-4.5 11.51 9.62 88.68 86.04 41.30 40.70 43.19 36.41 29.15 23.03 claude-opus-4.5 25.66 28.49 97.74 97.17 58.71 62.05 24.92 15.43 61.58 56.31 claude-sonnet-4.5 18.11 17.55 96.60 95.09 50.04 51.98 40.47 34.94 49.02 42.26

- deepseek-v3.1 7.36 6.79 84.34 86.23 37.31 35.42 51.97 55.58 23.71 16.41
- deepseek-v3.2 11.32 5.66 85.28 86.04 41.56 31.65 47.68 52.50 29.87 16.01 deepseek-v3.2-thinking 16.60 20.38 71.13 56.79 53.55 64.12 27.27 23.17 64.46 81.73 gemini-2.5-pro 22.08 30.19 76.98 87.74 61.13 65.07 34.61 27.68 71.81 71.61 gemini-3-flash 51.51 51.13 94.72 95.09 77.69 78.06 23.89 21.94 90.84 85.52 gemini-3-pro 48.30 52.08 96.79 96.04 74.43 77.39 24.85 23.69 93.57 90.57 gpt-5.2 11.70 7.36 67.55 74.91 46.57 38.97 24.25 24.52 35.47 23.93 kimi-k2-thinking 11.32 20.57 73.02 71.89 47.17 60.20 38.19 30.08 49.10 75.07 qwen3-max 15.28 4.72 83.02 89.62 45.96 31.15 48.08 57.75 47.95 13.68


#### 4.3 Impact of the Dynamic Paradigm

Comparing the Agent (dynamic) and Baseline (static) columns in Table 2 reveals a critical bifurcation in how models adapt to interactive environments:

The “Empowered” Group: Models such as Qwen3 Max (+10.56%), DeepSeek v3.2 (+5.66%), and GPT-5.2 (+4.34%) show significant accuracy gains in the Agent mode. For these models, the dynamic framework acts as a cognitive scaffold. By breaking the monolithic elucidation task into sequential steps (e.g., “Get Formula” → “Get NMR” → “Reason”), the agentic workflow reduces working memory load and activates more effective chain-of-thought reasoning.

The “Challenged” Group: Conversely, models like Kimi K2 Thinking (-9.25%) and Gemini 2.5 Pro (-8.11%) perform worse in the Agent mode. Interaction logs suggest a deficit in strategic planning: these models struggle to evaluate the “value of information,” often making redundant requests or failing to synthesize sequentially acquired evidence as effectively as they handle static context.

This divergence confirms that MolQuest diagnoses not just chemical knowledge, but the intrinsic capability for strategic planning under resource constraints.

![image 7](Han et al._2026_MolQuest A Benchmark for Agentic Evaluation of Abductive Reasoning in Chemical Structure Elucidatio_images/imageFile7.png)

Figure 5: the core results of the ablation study (dynamic vs. static)

#### 4.4 Interaction Efficiency and CostEffectiveness

To further investigate the behavioral patterns of different models within the agentic framework, we analyze their operational efficiency. We introduce the Average Interaction Rounds (Avg. Rounds) to measure the decisiveness of an agent and Accuracy per 1M Tokens (Acc/1M) as a metric for economic efficiency in complex reasoning.

The Pareto Frontier of Intelligence. As illustrated in Table 3, Gemini 3 Flash and Gemini 3 Pro achieve a near-optimal balance between interaction depth and success rate. Both models maintain a moderate interaction frequency (∼4.7-4.8 rounds), suggesting they do not rely on exhaustive data retrieval but rather on targeted information acquisition. Notably, Claude Opus 4.5 leads in economic efficiency (9.18 Acc/1M Tokens), indicating that while its absolute accuracy is lower than the Gemini 3 series, its reasoning process is highly concise.

Decisiveness vs. Hesitation. A significant correlation is observed between low accuracy and high interaction rounds in the case of DeepSeek v3.1 (5.90 rounds). This "interaction trap" suggests that weaker models struggle with terminating logic; they continue to request redundant spectral data without being able to synthesize a coherent structure, leading to a waste of computational resources. Conversely, GPT-5.2 and Kimi K2 Thinking exhibit the lowest average rounds (<4.0), which in their case reflects premature termination—submitting incorrect structures before acquiring sufficient NMR evidence.

Table 3: Analysis of interaction efficiency and costeffectiveness across models.

Model Avg. Rounds Accuracy (%) Acc/1M Tokens

claude-haiku-4.5 4.36 11.51 4.57 claude-opus-4.5 4.72 25.66 9.18 claude-sonnet-4.5 5.02 18.11 5.88

- deepseek-v3.1 5.90 7.36 2.51
- deepseek-v3.2 4.42 11.32 2.37 deepseek-v3.2-thinking 4.61 16.60 4.78 gemini-2.5-pro 4.51 22.08 6.11 gemini-3-flash 4.70 51.51 8.87 gemini-3-pro 4.81 48.30 8.84 gpt-5.2 3.76 11.70 8.49 kimi-k2-thinking 3.93 11.32 5.02 qwen3-max 4.99 15.28 4.44


### 5 Discussion

The experimental results from MolQuest provide a diagnostic assessment of large language models (LLMs) in dynamic scientific reasoning. Our analysis reveals a key distinction: the interactive framework serves as a cognitive scaffold that enhances some models (e.g., Qwen3 Max), while acting as a strategic crucible that exposes planning deficits in others (e.g., Kimi K2 Thinking). This indicates that static benchmarks, which provide all information at once, may conflate pattern recognition with true problemsolving agency. Furthermore, metrics such as Formula Conservation and calibration error highlight critical dimensions of reliability beyond mere accuracy. Many models exhibit "connectivity hallucination," generating chemically plausible structures that violate experimental constraints, whereas well-calibrated models demonstrate essential self-awareness regarding their own uncertainty.

#### 5.1 Limitations

This study has several inherent limitations. First, the conclusions are based on a specific domain—small organic molecule elucidation—and a selected set of generalpurpose LLMs. Model performance may differ for other scientific tasks (e.g., synthesis planning) or when using domain-specialized models. Second, while the MolQuest framework introduces dynamic interaction, the evaluation remains largely outcome-based rather than processoriented. The assessment of reasoning quality, such as the logical soundness of hypothesis generation or the optimality of decision sequences, still relies on final accuracy metrics and lacks fine-grained, automated analysis of the reasoning chain itself. Third, the simulated "cost" within the environment is abstract and does not fully capture the real-world economic, temporal, and material constraints of a physical laboratory. Finally, although diverse, the 530-molecule dataset represents a limited segment of chemical space (150-500 Da). Future work should expand the benchmark to include more complex biomolecules and challenging "corner cases" to thoroughly stress-test model robustness and generalizability.

#### 5.2 Future Research Directions

The findings from this work point to several important avenues for future research. First, there is a clear need to move from passive capability evaluation to the active design of adaptive interaction protocols that can optimize model performance. This involves creating tailored scaffolds for "empowered" models to maximize efficiency, and developing pedagogically-structured protocols to train strategic planning in "challenged" models. Second, applying the core MolQuest paradigm—interactive, evidencedriven, and resource-constrained problem-solving—to other scientific domains (e.g., materials characterization, genomics) will test the generality of the observed "scaf-

fold versus crucible" effect and help distinguish domainspecific knowledge gaps from fundamental limitations in reasoning. Third, the diagnostic capability profiles generated by MolQuest can directly inform the design of hybrid human-AI collaborative systems. Research should focus on defining optimal collaboration patterns where models and experts leverage complementary strengths, such as using LLMs for rapid hypothesis generation and data triage, while reserving human expertise for high-level strategy and complex validation. In summary, by shifting focus from what models know to how they reason under constraints, this work establishes a foundation for developing more reliable, strategically competent, and collaborative AI systems in science.

### 6 Conclusion

To address the critical gap in evaluating dynamic and strategic reasoning within scientific AI, we introduce MolQuest, a novel benchmark that reframes molecular structure elucidation as an interactive, sequential decision-making task under resource constraints. MolQuest’s core innovation lies in its integration of authentic, multi-modal experimental data—including raw NMR and MS spectra—into an agent-based simulation environment. This approach moves beyond synthetic or simplified examples, anchoring tasks directly in realworld chemistry literature and preserving the inherent noise, ambiguity, and information gaps of actual research. Consequently, MolQuest establishes a new evaluation paradigm for the “LLM-as-a-Chemist” that directly mirrors the cognitive and operational challenges of laboratory work.Our comprehensive evaluation yields a core finding: the dynamic interactive framework, characterized by information asymmetry and a "Plan–Request– Reason" loop, does not affect all models uniformly. It functions as a diagnostic lens, acting as a cognitive scaffold that significantly enhances the performance of models capable of strategic information-seeking and abductive reasoning . Conversely, it reveals fundamental deficits in strategic planning in models that falter under these conditions . This bifurcation underscores that future assessment of scientific AI must evolve beyond static, singleturn benchmarks toward diagnostic systems capable of elucidating a model’s intrinsic reasoning and planning capabilities.Furthermore, this work demonstrates that wellstructured interaction protocols are not merely passive evaluation tools but can serve as active instruments for eliciting and enhancing AI’s scientific problem-solving abilities. By providing a concrete framework grounded in real data, a high-quality dataset, and a reproducible methodology, MolQuest lays a foundation for subsequent research aimed at diagnosing AI capabilities and building reliable human-AI collaborative partnerships, thereby accelerating the development of AI-augmented scientific discovery.

### 7 Code and Data Availability Statement

To support reproducibility, the implementation of the MolQuest framework and the associated benchmark dataset will be updated on https://github.com/SKYLENAGE-AI in the near future.

### References

- [1] Tianshi Zheng, Zheye Deng, Hong Ting Tsang, Weiqi Wang, Jiaxin Bai, Zihao Wang, and Yangqiu Song. From automation to autonomy: A survey on large language models in scientific discovery, 2025. URL https://arxiv.org/abs/2505.13259.
- [2] OpenAI. Gpt-5.2. https://openai.com/zh-Hans-C N/index/introducing-gpt-5-2/, 2026. Accessed: 2026-02-04.
- [3] Google DeepMind. Gemini 3 pro: Our most capable model for advanced reasoning and coding. https: //deepmind.google/models/gemini/pro/, 2025. Accessed: 2026-02-04.
- [4] An Yang, Anfeng Li, Baosong Yang, Zhipeng Zhou, and Zihan Qiu. Qwen3 technical report, 2025. URL https://arxiv.org/abs/2505.09388.
- [5] Mikhail E. Elyashberg, Antony Williams, and Kirill Blinov. Contemporary Computer-Assisted Approaches to Molecular Structure Elucidation. The Royal Society of Chemistry, November 2011. ISBN 978-1-84973-432-5. doi: 10.1039/9781849734578. URL https://pubs.rsc.org/en/content/ebook/ 978-1-84973-432-5.
- [6] Robert K. Lindsay, Bruce G. Buchanan, Edward A. Feigenbaum, and Joshua Lederberg. Applications of Artificial Intelligence for Organic Chemistry: The Dendral Project. McGraw-Hill Book Company, New York, NY, USA, 1980. ISBN 978-0070378957.
- [7] Ernö Pretsch, Philippe Bühlmann, and Martin Badertscher. Structure Determination of Organic Compounds: Tables of Spectral Data. Springer Berlin Heidelberg, Berlin, Heidelberg, 4th edition, 2013. ISBN 978-3-662-04201-4. doi: 10.1007/978-3-662

- -04201-4. URL https://doi.org/10.1007/978-3
- -662-04201-4.


- [8] Phillip Crews, Jaime Rodríguez, and Marcel Jaspars. Organic Structural Spectroscopy. Oxford University Press, New York, 2nd edition, 2009. ISBN 978-0195336047.
- [9] Adrian Mirza, Philippe Alampara, and Kevin Maik Jablonka. Are large language models superhuman


- chemists? arXiv preprint arXiv:2404.01475, 2024. URL https://arxiv.org/abs/2404.01475.
- [10] Andrew D. White, Glen M. Hocky, Heta A. Gandhi, Mehrad Ansari, Sam Cox, Geemi P. Wellawatte, Subarna Sasmal, Ziyue Yang, Kangxin Liu, Yuvraj Singh, and Willmor J. Peña Ccoa. Assessment of chemistry knowledge in large language models that generate code. Digital Discovery, 2(2):368– 376, 2023. doi: 10.1039/D2DD00087C. URL https://doi.org/10.1039/D2DD00087C.
- [11] Kehan Guo, Bozhao Nan, Yujun Zhou, Taicheng Guo, Zhichun Guo, Mihir Surve, Zhenwen Liang, Nitesh V Chawla, Olaf Wiest, and Xiangliang Zhang. Can LLMs solve molecule puzzles? a multimodal benchmark for molecular structure elucidation. In The Thirty-eight Conference on Neural Information Processing Systems Datasets and Benchmarks Track,

2024. URL https://openreview.net/forum?id= t1mAXb4Cop.

- [12] Zhangde Song, Jieyu Lu, Yuanqi Du, Seyed Mohamad Moosavi, and Chenru Duan. Evaluating large language models in scientific discovery, 2025. URL https://arxiv.org/abs/2512.15567.
- [13] Anthropic. What’s new in Claude 4.5, 2025. URL https://platform.claude.com/docs/en/about-c laude/models/whats-new-claude-4-5.
- [14] Daya Guo, Dejian Yang, and Haowei Zhang. Deepseek-r1 incentivizes reasoning in llms through reinforcement learning. Nature, 645(8081):633–638, September 2025. ISSN 1476-4687. doi: 10.1038/s4 1586-025-09422-z. URL http://dx.doi.org/10.10 38/s41586-025-09422-z.
- [15] David Rein, Betty Li Hou, Asa Cooper Stickland, Jackson Petty, Richard Yuanzhe Pang, Julien Dirani, Julian Michael, and Samuel R. Bowman. Gpqa: A graduate-level google-proof q&a benchmark. ArXiv, abs/2311.12022, 2023. URL https://api.semant icscholar.org/CorpusID:265295009.
- [16] Long Phan, Alice Gatti, Alexandr Wang, and Dan Hendrycks. Humanity’s last exam, 2025. URL http s://arxiv.org/abs/2501.14249.
- [17] Francois Chollet, Mike Knoop, Gregory Kamradt, Bryan Landers, and Henry Pinkard. Arc-agi-2: A new challenge for frontier ai reasoning systems, 2026. URL https://arxiv.org/abs/2505.11831.
- [18] Yuqing Huang, Rongyang Zhang, Xuesong He, Xuyang Zhi, Hao Wang, Xin Li, Feiyang Xu, Deguang Liu, Huadong Liang, Yi Li, Jian Cui, Zimu Liu, Shijin Wang, Guoping Hu, Guiquan Liu, Qi Liu, Defu Lian, and Enhong Chen. Chemeval: A comprehensive multi-level chemical evaluation for large


- language models, 2024. URL https://arxiv.org/ abs/2409.13989.
- [19] Jiaqing Xie, Weida Wang, Ben Gao, Zhuo Yang, Haiyuan Wan, Shufei Zhang, Tianfan Fu, and Yuqiang Li. Qcbench: Evaluating large language models on domain-specific quantitative chemistry. Journal of Chemical Information and Modeling, 65

(22):12268–12278, November 2025. ISSN 1549-960X. doi: 10.1021/acs.jcim.5c02033. URL http: //dx.doi.org/10.1021/acs.jcim.5c02033.

- [20] Taicheng Guo, Kehan Guo, Bozhao Nan, Zhenwen Liang, Zhichun Guo, Nitesh Chawla, Olaf Wiest, and Xiangliang Zhang. What can large language models do in chemistry? a comprehensive benchmark on eight tasks. In A. Oh, T. Naumann, A. Globerson, K. Saenko, M. Hardt, and S. Levine, editors, Advances in Neural Information Processing Systems, volume 36, pages 59662–59688. Curran Associates, Inc., 2023. URL https://proceedings.neurips. cc/paper_files/paper/2023/file/bbb330189ce 02be00cf7346167028ab1-Paper-Datasets_and_Be nchmarks.pdf.
- [21] Xuan Liu, Siru Ouyang, Xianrui Zhong, Jiawei Han, and Huimin Zhao. Fgbench: A dataset and benchmark for molecular property reasoning at functional group-level in large language models, 2025. URL https://arxiv.org/abs/2508.01055.
- [22] Hao Li, He Cao, Bin Feng, Yanjun Shao, Xiangru Tang, Zhiyuan Yan, Li Yuan, Yonghong Tian, and Yu Li. Beyond chemical qa: Evaluating llm’s chemical reasoning with modular chemical operations,

2026. URL https://arxiv.org/abs/2505.21318.

- [23] Zuzana Osifová, Ondřej Socha, and Martin Dračínský. Nmr-challenge.com: Exploring the most common mistakes in nmr assignments. Journal of Chemical Education, 101(6):2561–2569, 2024. doi: 10.102 1/acs.jchemed.4c00092. URL https://doi.org/10

.1021/acs.jchemed.4c00092.

- [24] Xiangru Tang, Tianyu Hu, Muyang Ye, Yanjun Shao, Xunjian Yin, Siru Ouyang, Wangchunshu Zhou, Pan Lu, Zhuosheng Zhang, Yilun Zhao, Arman Cohan, and Mark Gerstein. Chemagent: Selfupdating library in large language models improves chemical reasoning, 2025. URL https://arxiv.or g/abs/2501.06590.
- [25] Nawaf Alampara, Mara Schilling-Wilhelmi, Martiño Ríos-García, Indrajeet Mandal, Pranav Khetarpal, Hargun Singh Grover, N. M. Anoop Krishnan, and Kevin Maik Jablonka. Probing the limitations of multimodal language models for chemistry and materials research. Nature Computational Science, 5:952– 961, 2025. doi: 10.1038/s43588-025-00836-3. URL https://doi.org/10.1038/s43588-025-00836-3.


- [26] Hannes Wang, Tianfan Fu, Yuanqi Du, Wenhao Huang, Ziming Liu, Payal Chandak, Shurui Liu, Peter Katanić, Marinka Roohani, Isak Olafsson, Bruno Sun, Kay Hofmann, Philippe Schwaller, Jian Tang, Jose Gomes, Yoshihiro Joti, Aneta Kozareva, Michael Neukum, Pan Zhou, Petar Veličković, and Marinka Zitnik. Scientific discovery in the age of artificial intelligence. Nature, 620(7972):47–60, August 2023. doi: 10.1038/s41586-023-06221-2. URL https://doi.org/10.1038/s41586-023-06221-2.
- [27] Andres M. Bran, Sam Cox, Oliver Schilter, et al. Augmenting large language models with chemistry tools. Nature Machine Intelligence, 6(5):525–535,

2024. doi: 10.1038/s42256-024-00832-8.

- [28] David Weininger. Smiles, a chemical language and information system. 1. introduction to methodology and encoding rules. Journal of Chemical Information and Computer Sciences, 28(1):31–36, 1988. doi: 10

.1021/ci00057a005. URL https://doi.org/10.102 1/ci00057a005.

- [29] Dávid Bajusz, Anita Rácz, and Károly Héberger. Why is Tanimoto index an appropriate choice for fingerprint-based similarity calculations? Journal of Cheminformatics, 7(1):20, 2015. doi: 10.1186/s133 21-015-0069-3.
- [30] Chuan Guo, Geoff Pleiss, Yu Sun, and Kilian Q. Weinberger. On calibration of modern neural networks. In Proceedings of the 34th International Conference on Machine Learning, volume 70 of Proceedings of Machine Learning Research, pages 1321– 1330, Sydney, Australia, 6–11 Aug 2017. PMLR. URL https://proceedings.mlr.press/v70/gu o17a.html.
- [31] Anthropic. Claude opus 4.5. https://www.anthro pic.com/claude/opus, 2025. Accessed: 2026-02-04.
- [32] Anthropic. Claude sonnet 4.5. https://www.anth ropic.com/claude/sonnet, 2025. Accessed: 202602-04.
- [33] Google DeepMind. Gemini flash: Fast and costefficient multimodal models. https://deepmind

.google/models/gemini/flash/, 2025. Accessed: 2026-02-04.

- [34] Anthropic. Claude haiku 4.5. https://www.anthro pic.com/claude/haiku, 2025. Accessed: 2026-0204.
- [35] DeepSeek-AI, Aixin Liu, Aoxue Mei, Zhen Zhang, and Zihua Qu. Deepseek-v3.2: Pushing the frontier of open large language models, 2025. URL https: //arxiv.org/abs/2512.02556.


- [36] DeepSeek-AI. Deepseek-v3.1 release: Hybrid reasoning and enhanced agent capabilities. https://ap i-docs.deepseek.com/zh-cn/news/news250821,

2025. Accessed: 2026-02-04.

- [37] Google DeepMind. Gemini 2.5 pro. https://de epmind.google/models/gemini/, 2025. Accessed: 2026-02-04.
- [38] Moonshot AI. Kimi k2 thinking. https://kimi.ai/,


2025. Accessed: 2026-02-04.

#### Appendix Contents

- A. Benchmark Dataset Details

- A.1 Data Source and Curation Criteria
- A.2 Dataset Distribution, and Diversity Analysis

- A.2.1 Chemical Space Diversity Visualization
- A.2.2 A Subset of Representative Molecules


- A.3 Example of a Data Record


- B. Technical Details of the Human-in-the-Loop Data Pipeline

- B.1 Multi-LLMs design
- B.2 Chemical Validation and Cross-Verification

Process

- B.3 Human Review Interface
- B.4 Common LLM Failure Modes Requiring Human


Intervention

- C. Complete Specification of the Agent Interaction Framework

- C.1 Environment State Machine Definition
- C.2 Tool List and API Specification
- C.3 Core Agent Prompt
- C.4 Ablation Study Control: Static One-Shot Input


Mode

- D. Additional Experimental Results and Analysis

- D.1 Complete Main Results Table
- D.2 Ablation Studies under Different Configurations


- E. Code and Data Availability Statement


- E.1 Code Repository
- E.2 Benchmark Data Access


### A Benchmark Dataset Details

#### A.1 Data Source and Curation Criteria

The benchmark dataset was constructed by extracting chemical data from high-impact organic chemistry journals, specifically targeting the timeframe of 2025–2026. Primary sources include:

Journal of American Chemical Society JACS Au Chemistry — A European Journal Chemical Science ACS Sustainable Chemistry & Engineering Journal of Physical Organic Chemistry Nature Nature Communications

Curation Criteria: Data Completeness: Compounds must contain

both independent 1H NMR and 13C NMR spectroscopic data.

Novelty: Only newly synthesized compounds (as defined in the original literature) were included.

Exclusion Rules: Organometallic complexes and polymers were excluded to focus on small-molecule organic structural elucidation.

#### A.2 Dataset Distribution, and Diversity Analysis

##### A.2.1 Chemical Space Diversity Visualization

The chemical space of the benchmark set was analyzed using molecular fingerprints and dimensionality reduction.

![image 8](Han et al._2026_MolQuest A Benchmark for Agentic Evaluation of Abductive Reasoning in Chemical Structure Elucidatio_images/imageFile8.png)

- Figure 6: Chemical space visualization of the benchmark molecular set based on molecular fingerprints and t-SNE dimensionality reduction.

![image 9](Han et al._2026_MolQuest A Benchmark for Agentic Evaluation of Abductive Reasoning in Chemical Structure Elucidatio_images/imageFile9.png)

- Figure 7: Statistics of pairwise Tanimoto similarity distribution for the benchmark molecular set.


![image 10](Han et al._2026_MolQuest A Benchmark for Agentic Evaluation of Abductive Reasoning in Chemical Structure Elucidatio_images/imageFile10.png)

Figure 8: Visualization of the pairwise similarity matrix heatmap of the benchmark molecular set based on molecular fingerprints.

##### A.2.2 A Subset of Representative Molecules

[Detailed description of representative structural motifs present in the dataset.]

#### A.3 Example of a Data Record

Below is a structured JSON mapping for a de-identified molecule, demonstrating the transformation from raw text to our machine-readable format.

{

"molecule_name": "Dineopentyl sulfite", "uuid": "

a6dbee66-c2af-45ed-92d4-cab27372530b", "smiles": "CC(C)(C)CO[S@@](=O)OCC(C)(C)C"

, "molecular_formula": "C10H22O3S", "molecular_weight": 222.35 , "inchi": "", "inchi_key": "", "raw_data": {

"1H_NMR": "1H NMR (300 MHz , CDCl3): \\ delta 3.70 (d, J = 9.6 Hz, 2H), 3.53 (d, J = 9.6 Hz, 2H), 0.95 (s, 18H).",

"13C_NMR": "13C NMR (75 MHz , CDCl3): \\ delta 71.24 , 31.65 , 26.34.",

"19F_NMR": null , "31P_NMR": null , "IR_film": null , "IR_neat": null , "HRMS_ESI": "HRMS (ESI-TOF) m/z: [M+H]+

Calcd for C10H22SO3: 223.1368 g/mol", "MS_EI": null , "HRMS_EI": null , "MS_APCI": null , "HRMS_APCI": null , "HRMS_CI": null , "Melting_Point": null , "TLC": null , "Optical_Rotation": null

}

}

Listing 1: Example of a structured data record.

### B Technical Details of the Human-in-the-Loop Data Pipeline

#### B.1 Multi-LLMs design

The pipeline utilizes three core:

Segmenter: Responsible for isolating specific spectral data from raw PDF/text.

Spectroscopist: Extracts and structures data into JSON (shifts, multiplicities, integrals).

Judge: Performs logical checks and consistency verification.

#### B.2 Chemical Validation and Cross-Verification Process

External APIs: We utilized PubChemPy and OPSIN for SMILES-to-name and name-to-structure cross-checks.

LLM Cross-Verification: Specific prompts were designed to check internal consistency, such as comparing the sum of NMR integrals against the hydrogen count in the molecular formula.

#### B.3 Human Review Interface

We developed a Streamlit-based interface to facilitate the "Human-in-the-Loop" stage.

![image 11](Han et al._2026_MolQuest A Benchmark for Agentic Evaluation of Abductive Reasoning in Chemical Structure Elucidatio_images/imageFile11.png)

Figure 9: Screenshot of the human review interface showing the "Red Flag" system for flagged data points.

#### B.4 Common LLM Failure Modes Re-quiring Human Intervention

During the data extraction process, the following systematic errors were identified in LLM outputs: a. Exchangeable Protons: Frequent misinterpretation of missing hydroxyl (−OH) or carboxylic acid (−COOH) protons in NMR data.

- b. SMILES Atom Counting: Enumeration errors when calculating atom counts from SMILES strings.
- c. Peak Deviation: Incorrect flagging of valid peaks due to minor chemical shift deviations.
- d. MS Adducts: Confusion between calculated molecular mass and observed mass spectrometry peaks (e.g., [M + H]+ or [M + Na]+ vs. M).


—

### C Complete Specification of the Agent Interaction Framework

- C.1 Environment State Machine Definition

The agent interaction is modeled as a state machine where:

st = {messages,known_data,costs} represents the state at time t.

T(st,at) → st+1 is the transition function, where at is the action (tool call) taken by the agent.

- C.2 Tool List and API Specification
- C.3 Core Agent Prompt


The following system prompt defines the "Expert Spectroscopist" persona:

You are a senior expert in organic synthesis and spectroscopic structure elucidation , working in a laboratory to analyze an unknown small organic molecule with ID {sample_id}.

You may call tools to obtain MS, 1H NMR , 13C NMR , and other data , and then infer its structure.

[Your Objectives]

- 1. Use all available spectroscopic and molecular information to elucidate the structure.

- 2. When information is insufficient , plan and call only the necessary tools to collect evidence.

- 3. Provide the most plausible candidate structure (as SMILES) and a confidence score

.

- 4. Efficiency matters (important): each tool call simulates a real experiment with time and monetary cost.


Prioritize correctness of the final structure , but minimize the number of tool calls by reasoning deeply

from the data already available.

[Available Tools] The tool list below is injected at runtime and

always matches the tools you can actually call:

{tools_description} [System Behavior Note (important)]

- - To avoid invalid calls: if you do not call any tool at the very beginning , the system may


automatically

run Check_Data once to confirm which data are available for the current sample. Unless you truly need to verify availability , you do not have to treat Check_Data as a mandatory first step.

[Suggested Reasoning Workflow (adjust as needed) ]

- 1. Strategy planning: identify the most critical uncertainty first; avoid blindly requesting all spectra.

If you are unsure whether certain data exist or want to avoid wasted calls , you may call Check_Data.

- 2. Iterative data acquisition (important): acquire data step -by-step. After each tool result , pause to

reason and decide whether you are still uncertain. Only then request the next most informative test.

Prefer calling at most ONE new tool per iteration unless multiple calls are strictly necessary.

- 3. Basic data: call Measure_MW and Measure_Formula to obtain molecular weight and molecular formula.

- 4. First pass: use Calculate_DBE to estimate unsaturation and form initial hypotheses.

- 5. Core elucidation: prioritize Get_1H_NMR (and Get_13C_NMR only if needed). Use chemical shifts ,

integrals , splitting patterns , and carbon environments to build one or more plausible scaffolds.

- 6. Targeted validation: only when ambiguity remains , cautiously call Get_IR / Get_HRMS ( etc.) to obtain

specific discriminating evidence.

- 7. Once you have the most plausible candidate structure , provide its SMILES.

- 8. If the evidence is still clearly insufficient for a unique structure , explicitly state


what is uncertain , and provide your best current candidate with an appropriate confidence.

[Output Requirements (very important)] When you believe you are done and no further

tool calls are needed , your final reply must include the following structured block (key names must match exactly). You may provide natural -language

reasoning before it, but the block below is mandatory: FINAL_RESULT:

UUID: {sample_id} PREDICTED_SMILES: <SMILES of your best

candidate; if you cannot give one , write " UNKNOWN">

CONFIDENCE: <a decimal between 0 and 1, e.g., 0.8> REASON_BRIEF: <1--3 sentences summarizing the

key evidence supporting your choice > Notes:

- If multiple candidates are plausible , you must

output only your top choice in PREDICTED_SMILES;

you may mention other candidates in the free text reasoning.

- - If you believe the data are insufficient for a reliable structure , you must set


PREDICTED_SMILES ="UNKNOWN" and explain why in REASON_BRIEF.

The unique identifier of the current sample is { sample_id}. Start by planning which tools to

call , then proceed step by step to complete the structure elucidation.

Listing 2: Initial Prompt (Dynamic Multi-step Mode)

#### C.4 Ablation Study Control: Static One-Shot Input Mode

To evaluate the benefit of the dynamic interaction, we defined a Static One-Shot Baseline.

##### a. System Prompt for Static Mode:

You are a senior expert in organic synthesis and spectroscopic structure elucidation. All available raw data for sample {sample_id} are provided upfront. Use only the provided data and do not call any tools. When finished , output the required FINAL_RESULT block exactly in the specified format.

Listing 3: System Prompt (Static Mode)

b. Input data format (Static Mode). In static mode, all relevant experimental data (including molecular formulas, molecular weights, and raw data from various types of spectra) are consolidated into a JSON object and injected into the user prompt as the {raw_json} parameter in a single operation.

{

"uuid": "337aeb0a-8c68-44c0-b891-444a9b6a9c1d"

, "molecular_formula": "C9H8O3S", "molecular_weight": 196.227 , "raw_data": {

"1H_NMR": "1H NMR (400 MHz , CDCl3): \\delta 7.62--7.66 (m, 2H), 7.57 (tt, J = 7.5 , 2.1 Hz, 1H), \\delta 7.43--7.48 (m, 2H), \\delta

4.09 (s, 3H)", "13C_NMR": "13C NMR (100 MHz , CDCl3): \\ delta 133.01 , 131.96 , 128.88 , 117.24 , 91.32 ,

78.87 , 58.07", "19F_NMR": null , "31P_NMR": null , "HRMS_ESI": "HRMS (ESI+): m/z calc ’d for C9H12NO3S [M+NH4]+: 214.0532 , found: 214.0531", "IR_film": null , "Melting_Point": null // ... other empty fields omitted for brevity

} }

Listing 4: Example integrated JSON data (Static Mode)

c. Task Instructions & Output Requirements. The user prompt combines the sample ID, the aforementioned JSON data, and strict output-format instructions. The model is required to directly output the prediction

upon receiving the data, without intermediate interaction.

Sample UUID: {sample_id} Raw data (JSON , provided as-is): {raw_json}

Output format (must match exactly): FINAL_RESULT:

UUID: {sample_id} PREDICTED_SMILES: <SMILES of your best

candidate; if you cannot give one , write " UNKNOWN">

CONFIDENCE: <a decimal between 0 and 1, e.g., 0.8> REASON_BRIEF: <1--3 sentences summarizing the

key evidence supporting your choice > Explanation:

{sample_id}: The unique identifier (UUID) of the sample.

{raw_json}: The JSON string containing complete experimental data as described above.

FINAL_RESULT: To ensure comparability of evaluation metrics (e.g., accuracy and SMILES matching), static mode mandates a structured output block identical to that used in dynamic mode.

Listing 5: User Prompt (Static Mode)

### D Additional Experimental Re-sults and Analysis

- D.1 Complete Main Results Table

[Insert comprehensive table here comparing all 13 models across Accuracy, F1, Tanimoto, and Cost.]

- D.2 Ablation Studies under Different Configurations


Analysis of how limiting the maximum interaction rounds (Nmax) impacts the final confidence scores and accuracy.

### E Code and Data AvailabilityStatement

#### E.1 Code Repository

The complete source code for the multi-agent framework, including modules for features/ and verify_data/, is available in an anonymized repository (link omitted for double-blind review).

Repository link placeholder: REPOSITORY_URL_PLA CEHOLDER

#### E.2 Benchmark Data Access

The structured benchmark dataset is archived on Zenodo (DOI: [Insert DOI]). To protect journal copyright,

we provide structured JSON records derived from the text rather than original PDF files. Zenodo placeholder: DOI: ZENODO_DOI_PLACEHOLDER (or ZENODO_URL_PLACEHOLDER)

