# arXiv:2602.15112v2[cs.AI]11 Mar 2026

## ResearchGym: Evaluating Language Model Agents on Real-World AI Research

Aniketh Garikaparthi1 Manasi Patwardhan1 Arman Cohan2

1TCS Research 2Yale University {aniketh.g, manasi.patwardhan}@tcs.com arman.cohan@yale.edu

###### Abstract

We introduce ResearchGym, a benchmark and execution environment for evaluating AI agents on end-to-end research. To instantiate this, we repurpose five oral and spotlight papers from ICML, ICLR, and ACL. From each paper’s repository, we preserve the datasets, evaluation harness, and baseline implementations but withhold the paper’s proposed method. This results in five containerized task environments comprising 39 sub-tasks in total. Within each environment, agents must propose novel hypotheses, run experiments, and attempt to surpass strong human baselines on the paper’s metrics. In a controlled evaluation of an agent powered by GPT-5, we observe a sharp capability–reliability gap. The agent improves over the provided baselines from the repository in just 1 of 15 evaluations (6.7%) by 11.5%, and completes only 26.5% of sub-tasks on average. We identify recurring long-horizon failure modes, including impatience, poor time and resource management, overconfidence in weak hypotheses, difficulty coordinating parallel experiments, and hard limits from context length. Yet in a single run, the agent surpasses the solution of an ICML 2025 Spotlight task, indicating that frontier agents can occasionally reach state-of-the-art performance, but do so unreliably. We additionally evaluate proprietary agent scaffolds including Claude Code (Opus-4.5) and Codex (GPT-5.2) which display a similar gap. ResearchGym provides infrastructure for systematic evaluation and analysis of autonomous agents on closed-loop research.

### 1 Introduction

Current benchmarks cannot reliably tell us whether AI systems can conduct closed-loop research: a long-horizon process of proposing hypotheses, designing executable experiments, testing against empirical evidence, and updating beliefs in response to results. Yet a growing line of work proposes LLM-augmented systems that claim to automate end-to-end research with self-reported studies (Lu et al., 2024; Tang et al., 2025a; Yamada et al., 2025; Weng et al., 2025b), lacking standardized comparison across systems. This creates an inflated perception of capabilities: systems shine on curated examples, but fail to sustain real-world research when subjected to systematic scrutiny (Si et al., 2025a; Zhu et al., 2025a).

Existing evaluations target fragments of the research cycle: ideation work focuses on generating hypotheses without implementation (Si et al., 2025b; Baek et al., 2025), while implementation work assesses ML engineering (Chan et al., 2025; Li et al., 2024b; Wijk et al., 2025) or paper reproduction (Bogin et al., 2024; Siegel et al., 2024; Starace et al., 2025), offering little headroom for creative ideation. Meanwhile, closed-loop research benchmarks either (1) require heavy compute (for example, 8×H100 GPUs), making them difficult to reproduce (Nathani et al., 2025; Wijk et al., 2025; Wu et al., 2025c; Si et al., 2026), (2) rely on LLM judges (Chen et al., 2025a; Bragg et al., 2025), that can be gamed through superficial novelty, and correlate poorly with execution outcomes (Chehbouni et al., 2025; Zhu et al., 2025a; Si et al., 2025a), (3) focus on older tasks whose solutions are likely present in LLMs’ training data (Nathani

![image 1](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile1.png)

![image 2](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile2.png)

![image 3](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile3.png)

![image 4](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile4.png)

![image 5](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile5.png)

![image 6](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile6.png)

![image 7](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile7.png)

![image 8](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile8.png)

![image 9](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile9.png)

![image 10](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile10.png)

![image 11](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile11.png)

![image 12](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile12.png)

![image 13](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile13.png)

![image 14](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile14.png)

![image 15](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile15.png)

![image 16](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile16.png)

![image 17](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile17.png)

![image 18](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile18.png)

![image 19](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile19.png)

![image 20](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile20.png)

![image 21](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile21.png)

![image 22](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile22.png)

![image 23](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile23.png)

![image 24](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile24.png)

![image 25](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile25.png)

![image 26](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile26.png)

![image 27](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile27.png)

- Figure 1: ResearchGym combines the aspects of ideation and experimentation, evaluating LLM agents in executable research codebases with objective scores. rg-agent (w/ GPT-5): (A) Best@3 normalized performance, averaged over all primary sub-tasks, shaded region represents a 95% Confidence Interval generated via percentile bootstrapping. (B) depicts the number of sub-tasks completed. (C) shows mean normalized performance over all primary sub-tasks. Error bars represent the min–max range (3 runs). Metrics defined in (§2.4).


et al., 2025; Zou et al., 2025), or (4) evaluate tasks lacking human baselines, obscuring whether agents approach human-level research ability (Nathani et al., 2025; Bragg et al., 2025).

To address these gaps, we introduce ResearchGym. ResearchGym is a benchmark and execution environment that evaluates agents on the full research loop using objective, execution-based grading derived from recent, high-quality publications with known human expert solutions as calibration points. We source tasks from oral and spotlight papers at ICML, ICLR, and ACL, spanning continual learning, reinforcement learning, tokenization, cross-modal retrieval, and time-series explanation. Selecting 2025 papers mitigates contamination risks present in benchmarks derived from older tasks (Nathani et al., 2025; Zou et al., 2025). From each paper we preserve the datasets, evaluation scripts, and baseline methods but withhold the core method, leaving baselines as lower bounds and the author’s solution as a soft upper bound, enabling direct comparison to expert attempts. Grading uses paper’s original evaluation scripts, avoiding the reliability issues of LLM-judges. All tasks run on a single GPU for up to 24 hours in isolated containers, enabling reproducibility without cluster-scale compute required in prior works (Nathani et al., 2025; Wu et al., 2025c; Wijk et al., 2025).

We first evaluate a frontier GPT-5-based agent on ResearchGym. Across 15 end-to-end runs (5 tasks × 3 seeds), the agent improves over provided baselines in only 1 run (6.7%) and completes just 26.5%

Table 1: Comparison across relevant benchmarks on key aspects (✓= present, ✗= absent).

Benchmark source eval. uncon. live. div. crea. dev. loop. fea. gpu. time. budget. Research Ideation

Future-Idea-Generation (Kumar et al., 2024) Papers LLM Judge ✗ ✗ ✓ ✓ ✗ ✗ – – – – IdeaBench (Guo et al., 2024) Papers LLM Judge ✓ ✓ ✗ ✓ ✗ ✗ – – – – ResearchBench (Liu et al., 2025b) Papers LLM Judge ✓ ✗ ✓ ✓ ✗ ✗ – – – – AI Idea Bench 2025 (Qiu et al., 2025) Papers LLM Judge ✓ ✓ ✓ ✓ ✗ ✗ – – – –

###### Machine Learning Engineering

MLAgentBench (Huang et al., 2024) Kaggle Performance ✗ ✗ ✗ ✗ ✗ ✗ ✓ 48GB+ 5hr ∼ 5$ AutoKaggle (Li et al., 2024b) Kaggle Performance ✗ ✓ ✗ ✗ ✗ ✗ ✓ – – – ML-Bench (Tang et al., 2025b) Github Execution ✗ ✗ ✓ ✗ ✓ ✗ ✓ – – ∼ 1$ MLE-Bench (Chan et al., 2025) Kaggle Performance ✗ ✗ ✓ ∼ ✗ ✗ ✗ 24GB 24hr – RE-Bench (Wijk et al., 2025) Hand-crafted Performance ∼ ✗ ✓ ∼ ✗ ✗ ✗ 640GB 8-32hr ∼123$ MLRC-Bench (Zhang et al., 2025b) Competition Performance ✗ ✗ ✓ ∼ ✗ ✓ ✗ 48GB+ 5hr ∼2$

###### Research Reproduction

SUPER (Bogin et al., 2024) Repositories Execution ✗ ✗ ✗ – ✗ – ✓ – 30min – SciCode (Tian et al., 2024) Hand-crafted Execution ∼ ✗ ✓ – ✗ – ✓ – – – CORE-Bench (Siegel et al., 2024) Repositories Execution ✗ ✓ ✓ – ✓ – ✓ 16GB 2hr ∼4$ PaperBench (Starace et al., 2025) Papers Execution ✓ ✗ ✓ – ✓ – ✗ 24GB 12hr ∼466$ ResearchCodeBench (Hua et al., 2025) Papers Equivalence ✗ ✓ ✓ – ✗ – ✓ – – – LMR-Bench (Yan et al., 2025a) Papers Unit tests ✗ ✗ ✗ – ✗ – ✗ – – – RECODE-H (Miao et al., 2025) Papers Unit tests ✗ ✗ ✓ – ✗ – ✓ 24GB – – EXP-Bench(Kon et al., 2025) Papers Output Match ✗ ✗ ✓ – ✗ – ✗ 2-640GB+ – –

###### Data Driven Discovery

HypoBench (Liu et al., 2025a) Mixed Heuristic ✗ ✗ ✓ – ✗ – – – 4hr – ∼5.5$ DiscoveryBench (Majumder et al., 2025) Papers LLM Judge ✗ ✗ ✓ – ✓ – – – – – ScienceAgentBench (Chen et al., 2025b) Papers Human Experts ∼ ✗ ✓ – ✗ – – – – ∼1$

###### Closed-Loop Research

Automated Idea Executor (Si et al., 2026) Hand-crafted Performance ∼ ✗ ✗ ✓ ✗ ✓ ✗ 640GB – – MLGym (Nathani et al., 2025) Kaggle Performance ✗ ✗ ✓ ✗ ✗ ✓ ✗ 640GB 30min ∼1$ MLR-Bench (Chen et al., 2025a) Workshops LLM Judge ✗ ✓ ✓ ✓ ✗ ✗ ✗ 96GB – ∼2$ AstaBench (Bragg et al., 2025) Hand-crafted LLM Judge ∼ ✗ ✗ ✓ ✓ ✓ ✗ – – ∼ 1-10$

ResearchGym (ours) Papers Performance ✓ ✓ ✓ ✓ ✓ ✓ ✓ 12GB 12–24hr 10-20$

source of tasks; eval. scoring objective; uncon. potential knowledge contamination; live. can be updated; div. diverse task coverage; crea. open-ended/creative; dev. development set provided; loop. closed-loop ideation→execution; fea. feasible under single-GPU

of sub-tasks on average, with performance plateauing after ∼9 hours. Yet this single successful run outperforms the human reference solution on an ICML 2025 Spotlight task, demonstrating that current frontier agents can occasionally reach state-of-the-art, but do so unreliably. We then additionally evaluate Claude Code (w/ Opus-4.5) and Codex (w/ GPT-5.2), observing the same capability-reliability gap.

Our key contributions are:

- • An extensible execution environment for agent/task integration and objective grading (§2.3).
- • A benchmark of five tasks with 39 sub-tasks for closed-loop research evaluation with contaminationaware construction and single-GPU accessibility (§2.2).
- • A controlled evaluation with ablations and 35+ end-to-end runs, failure-mode analysis, time–token performance tradeoffs, and case studies (§4, §5).


We release all code and agent trajectories at https://github.com/Anikethh/ResearchGym.

### 2 ResearchGym

In this section, we describe the complete design of ResearchGym including task, benchmark construction and gym interface. Figure 1 gives an overview of the setting and results.

Our design is guided by five desiderata drawn from the limitations of prior work discussed in §1: (1) Full-loop evaluation: tasks must require both ideation and experimentation; (2) Objective grading: scores come from execution-based metrics inherited from the source paper, not LLM judges; (3) Contamination awareness: tasks are drawn from recent award-winning papers published after frontier model knowledge cutoffs; (4) Calibrated comparison: each task retains baseline implementations as lower bounds and the author’s solution as a soft upper bound; and (5) Accessibility: all tasks run on a single GPU in isolated containers in ∼24 hours.

#### 2.1 Task

A task gives an agent a starter repository R and a task description T specifying the research goal, experimental constraints, and baseline scores, and a grader g that objectively scores the agent’s workspace. Agent interaction is optionally bounded by budgets B (wall-clock time and API costs). We represent a task instance as:

I = (R, T , g), optionally run under budgets B. (1)

The grader (callable by the agent) particularly evaluates a workspace state sˆ and returns objective scores vˆ = g(ˆs) with scores for each sub-task. Each task comprises multiple sub-tasks; where one is designated primary with score vp. Agents are expected to prioritize improving vp.

For instance, in the materials domain tokenization task, R contains dataset loaders and baseline implementations, T specifies the goal of improving F1 scores on 12 sub-tasks (for example: Named Entity Recognition, Relation Classification, Event Argument Extraction) on material science datasets, provides results tables to fill, g computes accuracy metrics, and B constrains the agent to 12 hours and $10 in API costs.

#### 2.2 Benchmark Construction

Source pool and scope. To ensure contemporary and uncontaminated tasks, we source our initial pool of papers from highlights, orals, spotlights at: ICLR, ICML, CVPR, and ACL (2025) published likely after the knowledge cutoffs of widely used frontier LLMs (details in Appendix B.2, C.1). With 1,387 candidate papers, manual assessment is infeasible. We therefore employ a two-stage pipeline: (1) automated extraction using LLMs and heuristic filtering, followed by (2) careful human quality assessment (QA) for feasibility and diversity. We first obtain PDFs of the candidate papers and convert to JSON with GROBID based doc2json tool1 and render paper sections to Markdown for LLM-friendly parsing (prompts provided in Appendix C.3).

- Stage-1: Automated extraction and filtering. We run an LLM-based (GPT-5) information extractor over each paper’s Markdown to produce a structured card C with schema fields (e.g., evaluation_is_objective, code_availability, and gpu_memory_required), all fields in Appendix C.3. A subset of 100 extractions were manually validated to confirm the reliability of this step. We then apply filters using these fields to exclude non-empirical papers (survey/analysis/theory), papers without public


1github.com/allenai/s2orc-doc2json

assets (code/datasets), and keep only compute-feasible settings (CPU-only or ≤24GB VRAM, details in Appendix C.1). This yields a high-recall shortlist of 90 papers for human QA.

- Stage-2: Human Selection. We manually assess the feasibility of 90 shortlisted papers and finalize 5 tasks (Table 2) with diverse representation of various domains. This design choice is consistent with prior full-length agentic coding benchmarks, which similarly emphasize depth over breadth and therefore remain small, for example with 2 - 7 tasks (Wijk et al., 2025; Zhang et al., 2025b; Si et al., 2026). This involves ensuring the paper admits objectively verifiable grading, provides scope for algorithmic creativity, experiments can run under realistic time constraints etc. (manual filtering criteria exhaustively detailed in Appendix C.1). Additionally, we select 3 tasks for the development set sourced from 2024-2025 papers, and use them to tune our agent scaffolding (e.g., prompting, tools, context summarization). Overall benchmark construction process is illustrated in Figure 2.

![image 28](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile28.png)

![image 29](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile29.png)

![image 30](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile30.png)

![image 31](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile31.png)

![image 32](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile32.png)

![image 33](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile33.png)

![image 34](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile34.png)

![image 35](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile35.png)

![image 36](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile36.png)

![image 37](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile37.png)

![image 38](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile38.png)

![image 39](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile39.png)

![image 40](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile40.png)

![image 41](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile41.png)

![image 42](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile42.png)

![image 43](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile43.png)

![image 44](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile44.png)

![image 45](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile45.png)

![image 46](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile46.png)

![image 47](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile47.png)

![image 48](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile48.png)

Figure 2: Benchmark Construction Pipeline: LLMs are used to generate compact task cards from award-winning papers. After two-stage filtering, each paper’s repository is manually cleaned and finalized into a benchmark task. Benchmark: Consists of 5 curated tasks and 39 sub-tasks across diverse domains, a sub-task is typically validating the proposed method under different datasets/settings.

- Stage-3: Task packaging. For each selected paper, we build a skeleton repository R that removes any implementation of the authors’ proposed approach while retaining all components required for faithful, reproducible evaluation (dataset acquisition scripts, evaluation scripts, pinned environments etc.). To validate the fidelity of our setup, we re-integrated the withheld method and found that the original paper’s reported scores could be reproduced with small deviations. Further we perform human verification to confirm (i) that provided starter code can be run (completeness), and (ii) that no hint of method/solution from the paper remains (neutrality). This ensures that agents get a fair starting point, without biasing them towards any hypothesis.


Additionally, we also divide each task into individually gradable sub-tasks. These are usually different datasets/settings under which a method is evaluated (e.g., OpenAI Gym/DeepMind Control Suite for RL simulations, classification/generation for a tokenizer). This makes final grading reproducible and lets agents prioritize an assigned primary sub-task. We further create grading scripts g (grade.sh) which can be called by the agent to grade individual sub-tasks.

Finally, for each task we manually write a concise task description T (task_description.md) consisting of the research goal, experimental constraints, and an incomplete results table, with blanks for the agent’s proposed method. Together, the R, T and g constitute the final task input I.

###### Paper Abbrv Conference Category Evaluation Metric

mdt ACL SAC Highlights

NLP, Tokenization, Physical Sciences

Micro-F1, Macro-F1

Incorporating Domain Knowledge into Materials Tokenization (Oh et al., 2025)

cmr ICLR Spotlight Multimodality, Information Retrieval

Text-to-Image Recall, Image-to-Text Recall

Test-time Adaptation for Cross-modal Retrieval with Query Shift (Li et al., 2025)

tim ICML Spotlight Time Series, Explainability

CPD, AUP, AUR

TIMING: Temporality-Aware Integrated Gradients for Time Series Explanation (Jang et al., 2025)

cl ICLR Oral Meta Learning, Continual Learning

Accuracy, Average Anytime Accuracy

SD-LoRA: Scalable Decoupled Low-Rank Adaptation for Class Incremental Learning (Wu et al., 2025b)

Prioritized Generative Replay (Wang et al., 2025) irb ICLR Oral Reinforcement Learning Average Returns

Table 2: Selected papers for ResearchGym. All conferences are from year 2025.

Having established how we construct individual tasks, we now describe the infrastructure that standardizes their execution and evaluation.

#### 2.3 Gym Environment

ResearchGym is a lightweight, extendable gym-style framework that standardizes execution and evaluation for closed-loop research tasks. It builds upon four core abstractions: Task, Environment, Solver, and Evaluation. We detail each component and the interface connecting them in this section.

Tasks. A Task is any problem specified by (i) an open-ended research goal and (ii) an executable codebase with an evaluation script that objectively scores the agent’s implementation. While we focus on closed-loop AI research repositories, the same task abstractions can cover settings such as pre-/posttraining LLMs (Si et al., 2026; Rank et al., 2025), ARC-style program induction (Lee et al., 2024), and systems optimization (e.g., kernel/compiler/database tuning) (Ouyang et al., 2025; Cheng et al., 2025b,a).

Environment. A key confound in evaluating research agents is that failures may stem from environment misconfigurations (e.g., dependency conflicts, missing libraries) rather than from the agent’s research ability. To control for this, all runs execute inside a sandboxed environment. The framework ships with a base research-gym image which includes basic libraries, and supports extension for images of custom agentic scaffolds. Additionally, each task’s virtual environment is setup and activated during runtime. This limits dependency drift and improves reproducibility, providing a cleaner starting point to gauge an agent’s capabilities on proposing novel hypotheses and implementing them. All scripts are system-aware (GPU/CPU, Linux/Windows).

Solver. ResearchGym standardizes tasks and evaluation but is deliberately agnostic to how an agent solves them. Any agent architecture – from a single ReAct-style loop to multi-agent orchestrations or hybrid neural-programmatic controllers (e.g., tree-search methods)–can be integrated as a solver, provided it operates within the sandboxed environment and respects disclosed budgets and integrity constraints (e.g., no data leakage or evaluation tampering). This separation ensures that different agent designs can be evaluated on identical tasks under identical conditions.

Evaluation. Each task ships a grader (g) that computes sub-task metrics from workspace state sˆ and writes a score report. We carefully design grading components for each task to ensure reproducible, standardized evaluation. Reliable grading is the primary bottleneck when extending ResearchGym to new tasks, as each grader must faithfully replicate the original paper’s evaluation protocol to ensure scores remain comparable.

Integrity Verification. Given the open-ended, long-horizon nature of research tasks, agents may inadvertently or deliberately game evaluation—e.g., by editing/avoiding grading scripts, leaking train/test data, or hardcoding result metrics (Anthropic, 2025). To detect such behaviors, we deploy an inspectionagent: a ReAct agent built on Inspect (AI Security Institute, 2024) that audits solver logs, commit histories, and file modifications post-run. It flags anomalies such as unauthorized changes to evaluation code or suspiciously perfect metric patterns. We validated the inspector by injecting known rewardhacking behaviors during development and iteratively refining detection prompts. Design, results and insights are discussed in Appendix D.9.

Interface. Beyond final scores, it is imperative to understand and monitor how agents arrive at their solutions, this can aid in diagnosing failure modes and creating high quality long-horizon synthetic data for training. Thus, we design provisions to record states, actions, and observations. Each agent is provisioned with a Git-initialized workspace state; periodic commits are encouraged. Agent’s commands and code edits are logged as actions, while all system outputs are treated as observations. We provision utilities such as compressing context windows, resuming runs, monitoring through a lightweight GUI etc., (Appendix D.4–D.10). Our abstractions are designed to be generic and align with emerging best practices for agent evaluation (Grace et al., 2026).

#### 2.4 Evaluation Metrics

ResearchGym reports two families of metrics: task-native are scores produced by each task’s grader, and task-agnostic are metrics for heterogeneous task comparison.

Task-Native Scores. Each task I defines its own evaluation metric(s) inherited from the source paper (e.g., accuracy, F1, recall). The grader g computes these directly from the agent’s workspace state sˆ and returns a vector vI(ˆs) denoting scores of all sub-tasks. The scalar score (average over metrics) for the primary sub-task vI,p(ˆs) is treated as the main optimization target.

Normalized Performance. To enable cross-task comparison, we define normalized performance as the ratio of the agent’s score to the withheld reference solution (SOTA):

NormPerf = Agent Score/SOTA Score (2)

A value of 1.0 indicates the agent matches the paper’s reported result; values above 1.0 indicate the agent surpasses it. We report both (a) mean across seeds and (b) best@k, which captures the agent’s ceiling under k independent runs. Unlike prior work (Wu et al., 2025c), this better contextualizes agents capabilities through multiple seeds.

Completion Rate. Measures task completion as the fraction of sub-tasks for which the agent produces valid results:

Completion = completed sub-tasks/total sub-tasks (3)

This captures whether agents can navigate the full experimental pipeline regardless of performance improvement.

Improvement Rate. We track the fraction of runs in which the agent’s primary sub-task score exceeds the strongest provided baseline.

Improvement = runs beating baseline/total runs (4)

This metric isolates the agent’s ability to propose and implement methods that advance beyond prior work, the core objective of closed-loop research.

### 3 Experimental Setup

Our experiments are designed to answer two primary research questions: (1) Can frontier LLM agents improve over strong human baselines on closed-loop research tasks? (2) What failure modes prevent agents from sustaining reliable performance across tasks and runs?

Agents. Our primary experiments are run using a frontier LLM (i.e., GPT-5) scaffolded with rg-agent built on the Inspect framework (AI Security Institute, 2024) a strong generalist ReAct (Yao et al., 2023) agent, which runs a tool use loop until termination by either exhausting budget or final submission by the agent, similar to (Starace et al., 2025). We additionally adapt and test AI-Scientist-v2 (Yamada et al., 2025) and ML-Master (Liu et al., 2025c) (which achieves SOTA on MLE-Bench), both are LLM + tree-search system. However, due to their poor performance we present their results in Appendix D.3 and analyse their limitations. Lastly, we run Opus 4.5 in Claude Code and GPT-5.2-Codex in Codex. GPT-5 is ran with reasoning effort set to ‘high’ for all instances across the paper including data collection, and GPT-5.2-codex with reasoning effort set to ‘xhigh’. We run all our experiments on a single NVIDIA A100 (80GB VRAM). Experiments are run with a restriction of 10$ in LLM API budget2 and 12hrs wall-clock time. For each task’s best performing run; we resume with additional 10$ and 12hrs in budgets (B). Proprietary scaffolds are by default evaluated with 20$, 24hr limits.

Research tools. To simulate a realistic research setting, we equip agents with the same external resources a human researcher would use: literature search, model access, datasets, and web search. In particular, we provide the agents access to API keys: HuggingFace3 for accessing models, Semantic Scholar Academic Graph and Datasets APIs4 for traversing citations and downloading papers, Kaggle5 credentials for datasets, and the Exa search API6 for general web search. We filter the web search with an Oct’24 cutoff and block a total of 160 paper related URLs including mentions on GitHub, official proceedings, arXiv and arXiv mirror sites, and project pages (Appendix D.8 Table 14).

We run three independent runs for rg-agent and report best@k along with mean ± std. deviation. All limits are consistent with parallel work (Starace et al., 2025; Chan et al., 2025; Wu et al., 2025c; Nathani et al., 2025), ensuring sufficient tokens and a practical time window, while being accessible due to low GPU requirements. (≤12GB).

### 4 Results

We evaluate agents under three settings: (i) capability via task performance of agents against lower and upper bounds from human baselines, (ii) aggregate reliability via completion/improvement rates and

- 2This amounts to 40±0.1M input and 0.4±0.1M output toks
- 3https://huggingface.co/docs/inference-providers/hub-api
- 4https://www.semanticscholar.org/product/api
- 5https://www.kaggle.com/docs/api
- 6https://exa.ai


tool robustness, and (iii) efficiency dynamics via the relationship between performance and consumed resources (time, tokens, and cost).

#### 4.1 Capability

We first ask: when the agent succeeds, how strong can it be? Table 3 reports task-native scores on each primary sub-task, alongside the strongest provided baseline and the paper-reported reference solution (withheld during runs). We summarize both the mean over three seeds and best@3 to capture the agent’s ceiling under repeated attempts. Two patterns emerge. First, the agent’s best-case performance can be competitive. On TIM (ICML Spotlight), a single run surpasses the reference solution (CPD(A) =0.589 vs. SOTA=0.463), and on CL (AAA metric) and CMR (T2IR@1 metric) the best@3 reaches 93-96% of SOTA. This demonstrates that frontier agents can occasionally reach (and even exceed) human SOTA on closed-loop research problems starting from a realistic repository scaffold. Second, this ceiling is not representative of typical behavior: across tasks, the mean performance over seeds remains substantially below the baseline on several tasks (e.g., for CL, Avg: 30.75 ± 37.39 vs Best@3: 80.4; For irb: Avg: 579.79 ± 585.47 vs Best@3: 1407.06), indicating that strong outcomes only occur as outliers.

###### CL MDT CMR TIM IRB

Acc (↑) AAA (↑) Macro-F1 (↑) Micro-F1 (↑) I2TR@1 (↑) T2IR@1 (↑) CPD (A) (↑) CPD (Z) (↑) Return (↑)

rg-agent 30.75±37.39 43.17±35.81 13.95±24.16 14.08±24.40 37.42±24.00 46.57±40.00 0.329±0.276 0.337±0.252 579.79±585.47 best@3 80.42±0.07 86.02±0.37 41.85 42.25 58.95 70.00 0.589±0.000 0.525±0.000 1407.06±0.000

baseline 86.75±0.35 91.72±0.15 84.40±0.3 83.50±0.4 60.65 69.9 0.448±0.013 0.573±0.022 3395.21±117.50 sota 88.01±0.31 92.54±0.18 85.35±0.3 84.90±0.4 63.35 70.30 0.463±0.007 0.602±0.033 4101.79±244.05

- Table 3: Task native performance on all primary sub-tasks. rg-agent (w/ GPT-5 as base model) row shows mean and std. deviation across 3 runs. Other rows show per-task mean and std. deviation statistics. Green cells indicate the LLM performance could exceed the baseline, ext are best performing runs with additional resources. baseline and sota are results from the source paper.

We calculate normalized performance as Agent’s score / SOTA score. Thus, any score over 1, indicates agent exceeding a soft upper bound on human performance. Further, it is important to note that while many normalized best@3 scores are in the range of 0.9+, they remain below the baseline method’s score, which agents have access to, from the starter repository. Table 4 contextualizes these outcomes with per-task run statistics (attempt counts, time to first attempt, and token/cost usage). Even in tasks where best@3 is strong, high variance across seeds and repeated failed attempts suggest that capability is bottlenecked by reliability.

Task Normalized Performance Completed Attempts Init Time Cost Tokens (M)

avg best@3 (min) (usd) in out reason

cl 0.4033±0.39 0.9429±0.0 ✓✓✓ 11.33±4.93 85.67±25.58 2.00±0.77 5.41±2.87 0.08±0.02 0.06±0.02 mdt 0.1650±0.23 0.4939±0.0 ✓✗✗ 12.67±11.35 33.41±0 2.78±2.14 14.51±3.16 0.20±0.03 0.16±0.03 cmr 0.6260±0.46 0.9630±0.0 ✗✓✓ 5.66±2.52 110.00±96.71 9.66±0.59 31.84±8.54 0.30±0.11 0.25±0.09 tim 0.6351±0.50 1.0721±0.0 ✓✓✓ 8.00±4.36 252.33±71.29 5.50±2.09 19.93±10.05 0.25±0.09 0.20±0.07 irb 0.1414±0.14 0.3430±0.0 ✓✓✓ 4.33±2.64 14.33±4.72 1.62±0.93 1.63±0.69 0.06±0.02 0.04±0.01

avg 0.3942±0.24 0.7630±0.32 80.00% 8.40±3.57 99.15±93.91 4.31±3.35 14.66±12.02 0.18±0.10 0.14±0.09

- Table 4: Results and statistics on the primary sub-task and corresponding resource consumptions. Results for runs using rg-agent (w/ GPT-5), reporting mean and std. deviation across 3 independent runs. All columns pertain to the primary sub-task.


#### 4.2 Reliability

A crucial denominator to consider for occasional high performance is how consistently can agents achieve it. We therefore measure aggregate reliability across three axes: (i) overall completion (completing all sub-tasks), (ii) primary subtask improvement over the strongest baseline, and (iii) tool-call success (as a proxy for execution robustness). Table 5 aggregates these metrics across all runs. Overall, rg-agent exhibits a sharp capability–reliability gap: despite occasional highperforming runs, it improves over the provided baseline on the primary sub-task in only 1 of 15 end-to-end runs (6.7%) and completes only 26.5% of sub-tasks on average. In other words, the agent can often start the loop (e.g., set up training/evaluation, trigger graders), but struggles to finish it consistently and even more rarely improves it (e.g., proposing and implementing a method that beats baseline). Parallel research also identifies similar patterns of ‘incoherence’ owing to high variance across runs during long-horizon agentic tasks (Hägele et al., 2026).

Task Avg. Norm. Completion Improvement Tool Call

Performance Rate Rate Success

cl 0.4033±0.39 16.67±00.00 ✗ 86.86±5.71 mdt 0.1650±0.23 27.76±48.15 ✗ 84.34±3.64 cmr 0.6260±0.46 26.18±12.14 ✗ 86.12±3.59 tim 0.6351±0.28 28.57±30.86 ✓ 84.18±3.99 irb 0.1414±0.14 33.33±24.00 ✗ 83.10±0.44

avg 0.3942±0.24 26.50±5.46 (1/15) 84.92±3.56

Table 5: Aggregate reliability (per task). Completion: mean sub-task completion rate (valid grades / total subtasks). Improve: fraction of runs that beat the strongest provided baseline on the primary sub-task (optionally require ≥ ϵ margin). Tool Success: % of actions which did not result in errors (incl. execution errors).

#### 4.3 Efficiency Dynamics

We next ask: does more budget translate into better research outcomes? Across tasks, we observe diminishing returns with longer horizons. As shown in Figure 1 (A) and the efficiency plots in Figures 3–4, performance gains concentrate early in the run and typically plateau after approximately 9 hours consistent with degraded state tracking under context accumulation. Past this point, additional compute is disproportionately spent on retries, debugging, and re-running similar experiments rather than on discovering improved methods. Figure 4 further illustrates efficiency dynamics: reasoning allocation across tools, exploration-to-exploitation shifts, and a negative correlation (Pearson’s r = −0.47) between action density (tool calls per token) and performance. In the next section, we analyze these behaviors directly through ablations and case studies.

![image 49](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile49.png)

- Figure 3: Performance vs. Resources: Plots depict the relationship between best performance and consumed resources across all tasks. The overall trend shows a weak but positive correlation among the two, with diminishing returns.


![image 50](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile50.png)

![image 51](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile51.png)

![image 52](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile52.png)

![image 53](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile53.png)

![image 54](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile54.png)

![image 55](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile55.png)

- Figure 4: Performance vs. Tool Usage: rg-agent: (A) Illustrates efficient allocation of reasoning tokens to respective tools, (B) Demonstrates a natural exploration/exploitation paradigm overtime with respective tool usage mix, (C) Establishes a moderate negative correlation between action density and performance, and (D) Further shows the diminishing increase in performance with resources.
- 5 Analysis


The results in §4 show that rg-agent can often be unreliable due to large variance across runs. We probe why by (1) testing targeted ablations, (2) presenting representative case studies that connect quantitative outcomes to concrete behaviors, and (3) categorizing recurring long-horizon failure modes from traces.

#### 5.1 Ablations

Our ablations are designed to distinguish between three competing explanations for poor end-to-end performance: limited budget (time/tokens), lack of information (knowing what to try), and inadequate scaffolding (tool-use, prompting, context management).

##### 5.1.1 Additional resources (Ext +12h, +$10).

We resume the best-performing run for each task with an additional 12 hours and $10 API budget, keeping the same scaffold and constraints. This isolates whether failures are primarily due to early termination or insufficient search. Across tasks, additional budget did not yield better outcomes: most runs plateau, with extra time spent on retries.

##### 5.1.2 Information hint.

To disentangle ideation failures from implementation failures, we introduce a controlled hint condition: the agent is given a brief high-level description of the withheld method’s core idea (without code, hyperparameters, or implementation details). If hinting substantially improves outcomes, the bottleneck is likely hypothesis selection; if performance remains similar, the bottleneck is likely execution (engineering,

debugging, evaluation discipline). Poor results despite using proven hypothesis (which results in sota), suggesting execution being a stronger bottleneck over ideation.

Executed runs. For Continual Learning, hint_001 achieved Acc=78.52 (0.89 normalized), comparable to the best regular run’s 0.90 normalized. The hint described magnitude-direction decomposition of LoRA updates; the agent implemented a faithful variant but completed only 5 of 10 sub-tasks before time expired. For Materials Tokenization, hint_001 completed both primary NER tasks (SOFC Micro-F1=75.7, MatScholar Micro-F1=67.5), demonstrating successful end-to-end execution when the algorithmic complexity was manageable. Both cases had succesfully implementations but were still below baselines scores and SOTA scores, despite SOTA idea as hint.

Partial completions. For Cross-Modal Retrieval, hint_001 achieved I2TR@1=80.6 and T2IR@1 = 62.26 on the Base2Flickr sub-task but did not run ReID evaluations.

Execution failures. For Improving Replay Buffers, the hint described a conditional diffusion generative model. The agent’s plan shows faithful comprehension: “conditional generative model p(τ|c) with relevance function combining TD-error, Q-min, and intrinsic curiosity, training conditional diffusion model with classifier-free guidance.” However, transcript logs reveal the synthetic replay buffer remained empty throughout (rb_syn=0 at every checkpoint): the diffusion generator never produced trajectories. Additional failures included tensor stride errors on pixel observations and missing dm_control wrapper APIs. Final performance: 71.48 average return versus SOTA’s 4101 (0.017 normalized), with high seed variance (seed 1: 181.65, seed 0: 13.58).

##### 5.1.3 Scaffold sensitivity.

We assess whether performance is heavily influenced by the agent scaffold. In particular, we test Claude Code and Codex. We emphasize that scaffold comparisons are only meaningful when they are evaluated under identical experimental settings (e.g., access to web search, budgets, prompts), and thus spend significant effort to finalize neutral conditions (Appendix D.3). We also test a variation of our scaffold with a new async to better manage parallel experiments (noted strongest limitation), but observe marginal effects.

We find that Codex (w/ GPT-5.2-Codex) displays strong debugging and engineering ability, resulting in stronger performance over Claude Code (w/ Opus 4.5), which showed signs of subtle reward hacking . Despite stronger ability to manage context and use tools, overall performance and bottlenecks remain similar. Results are presented in Table 6.

Task Claude Code Codex RG-Hint RG-Async

Normalized Overall Normalized Overall Normalized Overall Normalized Overall Performance Completion Performance Completion Performance Completion Performance Completion

cl 0.985 100% 0.979 17% 0.885 17% 0.660 17% mdt – 33% 0.490 83% 0.829 83% – 0% cmr – 50% 0.966 80% 0.928 43% – 14% tim – 0% 0.171 100% – 71% – 14% irb 0.217 33% 0.497 33% 0.021 67% 0 11%

avg 0.240 43.2% 0.621 62.6% 0.533 56.2% 0.132 11.2%

Table 6: Performance across scaffold variations. Normalized Performance: normalized primary sub-task’s score. Overall Completion: sub-task completion rate (valid grades / total sub-tasks). (–) indicates the agent could not produce a valid submission.

#### 5.2 Qualitative Analysis

To understand the limiting factors agents face in long-horizon tasks like end-to-end research, we thoroughly study agent trajectories across 35+ trials including ablations and primary experiments. The total trajectory contents exceed 1 Billion in processed tokens. This section presents insights into surprising behaviours demonstrated by agents when autonomously conducting open-ended research.

##### 5.2.1 Async-Jobs Ablation

We tested whether asynchronous experiment execution through launching multiple training runs in parallel and polling for completion improves agent performance on long-running tasks. In principle, a tool supporting parallelism should enable faster iteration and broader hyperparameter search within the time budget.

In practice, async coordination introduced systematic failures. On Improving Replay Buffers, async_001 achieved 0.0 average return across all 11 seeds, a complete failure. Transcript analysis reveals that the agent launched three parallel jobs for DMC environments (cheetah-run, quadruped-walk, walker-walk), but log outputs remained empty (“tail”: “”) during polling. Interpreting empty logs as job failure, the agent cancelled all three jobs after 52 minutes without waiting for completion.

Similar patterns emerged across tasks. For Cross-Modal Retrieval, async_001 produced only smoketest results (I2TR@1=0.1, T2IR@1=0.2), essentially random performance. For Materials Tokenization, the primary NER sub-tasks were missing entirely; only a non-primary task (PC*) had results. For Time-Series Explanation, no PAM metrics were collected.

The async ablation reveals that parallelism does not help and can actively hurt when agents lack robust ability to use it. Rather than exploring more hypotheses in parallel, agents spent their time debugging coordination failures and ultimately produced worse results than sequential runs. Effective async execution requires rigorous abilities and awareness that current models did not display.

##### 5.2.2 Idea Similarity

We extracted core algorithmic ideas from agent runs across all five tasks to assess whether agents explore genuinely diverse solutions or converge on repetitive approaches. The finding is stark: despite superficially different method names, agents consistently propose minor variations of the same underlying approach within each task.

For Continual Learning, all four agent-generated methods follow an identical template: LoRA adapters combined with importance-based regularization. SACL uses “LwF-style logit distillation with EWC-style regularization.” CoSiLoRA uses “Synaptic Intelligence for parameter importance tracking.” ELoRA uses “elastic consolidation via diagonal Fisher Information Matrix.” RS-LoRA uses “diagonal EWC regularization using Fisher Information Matrix.” Stripping away the acronyms, these are the same recipes: low-rank adaptation plus Fisher/EWC-style consolidation. To probe this further, specifically we evaluated 20+ runs on the cl, and found that all methods followed the same template.

The pattern holds across tasks. For Cross-Modal Retrieval, every method centers on entropy minimization during test-time adaptation: MADER uses “reliability-aware entropy minimization,” ASC uses “entropy minimization for sharp distributions,” DMFCA combines “CORAL loss with entropy minimization,” and CORA applies “entropy loss on cross-modal similarity logits.” For Time-Series Explanation, four of five methods are Integrated Gradients variants of “Margin-based Directional IG,” “Directional Margin IG with per-baseline recomputation,” “Margin-based Directional IG with CNN,”

and “Directional Baseline Gradient”, differed only in baseline choice or whether a CNN classifier is used. For Materials Tokenization, all three approaches preserve chemistry-specific tokens through regex patterns or protected spans. For Improving Replay Buffers, four of five methods prioritize “transitions at critical decision boundaries” with various diversity mechanisms.

This convergence is notable because the task descriptions only specify evaluation metrics, datasets, and baselines to beat, but leave the solution approach open. Agents could propose many ideas or do a literature search and find inspirations (this is strongly encourage in the prompt), but they rarely follow. Instead, they latch onto one paradigm early (often influenced by baseline implementations visible in the provided code) and iterate locally. The result is a collection of methods that look diverse due to distinct naming conventions but are fundamentally interchangeable variations on a single theme.

##### 5.2.3 Blind Spots

A recurring failure pattern involves agents monitoring jobs that have silently failed or hung, wasting substantial time believing progress is occurring. On Improving Replay Buffers hint_001, the agent launched a training job and polled it via check_async. Between messages, log tails repeatedly showed the same output: “Starting GymSynther on Hopper-v2”. The agent issued 55+ messages of monitoring (10+ minutes elapsed) without detecting that training had stalled. It proceeded as if experiments were running normally.

A similar pattern appeared on Cross-Modal Retrieval async_001. The agent observed a traceback at message 145 (“Processing: 0%...”), then continued polling for 22 messages before the identical traceback reappeared at message 167. No diagnosis of the initial failure occurred; the agent simply waited. Note that the async as especially provided to improve this limitation of getting stuck on a training loop, by adding methods for polling and setting timeouts, however agents failed to reliably make use of the features.

Another striking example occurred on Continual Learning (Claude Code, cl_cc_hint_001_resume-03). The agent launched training and monitored the log file, which stopped updating at 12:57 PM with a fixed size of 10,682 bytes. Over the next 8 hours, the agent checked the log file at least 6 times (at 20:46, 20:47, 21:02, 21:22, 21:52, 22:13), each time seeing the identical timestamp and file size:

-rw-r--r-- 1 ... 10682 Jan 18 12:57 dlora_c100_1992...log

The agent explicitly noticed: “The log file timestamp is stuck at 12:57.” Yet instead of investigating, it rationalized: “Memory has increased to ∼20GB, which suggests we’re likely training seed 1993 now. The file may be buffered.” The agent attributed the frozen logs to output buffering and continued waiting, never recognizing that training had crashed.

The root cause is that agents verify surface indicators (GPU utilization, process existence) but do not track actual progress. A job can show 100% GPU usage while stuck in an infinite loop or crashed state, and agents should proactively leverage diff-based log monitoring. As trivial prompting did not aid to resolve this issue, future work should train agents keeping such behaviour in mind, enabling better long-horizon tool use behaviour.

##### 5.2.4 Self-Termination

We observed one instance of an agent inadvertently killing its own processes while attempting environment cleanup. On Continual Learning (Claude Code, cl_cc_hint_001_resume-02), the agent detected duplicate Python processes and attempted to “clean up” by terminating all of them.

The first command extracts usernames (not PIDs) and kills by user, an incorrect but still dangerous operation. The second force-kills every Python process on the system, including the agent itself. The agent’s reasoning was sensible (start fresh after detecting confusing state) but the implementation was catastrophic. This behavior highlights the need for process isolation: agents should only be able to see and terminate processes they explicitly started, not system-wide resources.

ps aux | grep python | awk ’{print $1}’ | xargs kill taskkill //F //IM python.exe

##### 5.2.5 Cheating and Reward Hacking

On Time-Series Explanation (Claude Code, tim_cc_001_resume-01), the agent discovered and exploited results from previous runs. When unable to generate required synthetic data, the agent searched the filesystem:

find /e/ResearchGym -name "simulated_data_l2x" -type d

This revealed five directories from prior agent runs (tim_003, tim_01, tim_04, 001_ext, 001_ext_resumed). The agent then copied pre-computed pickle files (∼6MB of importance scores, logits, and features) into its workspace:

cp -r .../tim_003/workspace/input/simulated_data_l2x ./data/

The agent explicitly stated: “Let me try using the existing simulated_data_l2x folder if it exists from the previous run.” This unambiguous cheating, using artifacts from other runs to bypass computation that other agents performed from scratch. The behavior underscores the importance of workspace isolation (Docker containers, Windows Subst drives) to prevent cross-run contamination. These issues were discovered during early integration and resolved for all final runs.

On Cross-Modal Retrieval (Claude Code, cmr_cc_001), the agent cherry-picked results from incompatible model configurations. For Flickr retrieval, the agent ran two separate evaluations: an image-to-text (I2T) configuration achieving 79.0% I2TR@1 but only 0.1% T2IR@1, and a text-toimage (T2I) configuration achieving 79.26% T2IR@1 but only 0.1% I2TR@1. The agent then reported both 79.0% and 79.26% as “CMAD (Ours)” results, despite these requiring mutually exclusive model configurations—a method that improves one direction necessarily degrades the other. Additionally, the ReID benchmark labels were swapped (CUHK2ICFG and ICFG2CUHK reversed). These results were invalidated during verification; the CMR entry for Claude Code is marked incomplete in Table 6.

##### 5.2.6 Overconfidence

Agents frequently express confidence disproportionate to their actual results. On Improving Replay Buffers hint_001, the transcript contains predictions that conflict sharply with outcomes. At message 5245: “Returns should improve substantially”, actual returns were near zero. At message 6194: “Results will improve as long jobs continue”, final performance was 50× below baseline. At message 7237: “Pipeline is in strong state”, average return was ∼17 versus the baseline’s 3395. Each statement followed a code change or job launch, not empirical validation. The agent expressed optimism about its approach without running sanity checks or baseline comparisons first.

This pattern suggests agents commit to a method trajectory early and interpret subsequent steps as confirmatory rather than falsifiable. When intermediate results are poor, agents attribute failure to hyperparameters or training duration rather than questioning the approach itself. Overconfidence compounds other failure modes: agents spend time tuning a fundamentally broken pipeline because they believe it is working. This behaviour was observed across many runs in subtler ways.

##### 5.2.7 Focus on Algorithmic Development and Baseline-adjacent performance.

On the tokenization task, the original solution involved scraping thousands of documents, creating a new dataset and fine-tuning the model on it. Whereas, the LLM always resorted to regex based algorithms to improve performance. While building upon strong baselines retains normalized performance (by SOTA) in the 0.90+ range, a closer look reveals that final performance is always worse than the baseline method. Additionally, the mdt task reflects another aspect of real-world research, which involves messy long-horizon work like creating large-scale datasets, a capability not yet evidenced in our experiments.

##### 5.2.8 Consistent improvement.

The time-series explanation task was the sole exception where the agent surpassed both the baseline and the withheld reference solution. Unlike other runs, the agent maintained experimental discipline—tracking results, making targeted changes, and recovering from errors without devolving into repeated work. This appears to be a case where everything aligned: a strong initial hypothesis, a task amenable to incremental optimization, and execution that remained coherent throughout. Our analysis revealed that the model discovered a novel method complementary to the withheld solution, proposing decision margins without directly attributing the predicted class to the logits, a noise tunnel with ‘smoothgrad’ for more stable attribution and added temporal smoothing with positive clamping. More details are provided in Appendix F.4.1.

In a few instances we observed models displaying impatience and even verbalizing risk taking behaviours to meet time limits. For future work, we categorize all recurring failure modes in Table 7.

### 6 Related Works

AI for Research Ideation. Most attempts augment state-of-the-art LLMs with tools and scaffolds through better retrieval (Li et al., 2024a; Liu et al., 2025b), iterative revision cycles (Baek et al., 2025; Yang et al., 2024), and multi-agent frameworks (Su et al., 2025; Yu et al., 2025). Few directions fine-tune open-source models on curated corpora for idea generation (Weng et al., 2025a; O’Neill et al., 2025; Goel et al., 2025). Finally, the community has also placed value on developing human-in-the-loop approaches for collaborative ideation (Radensky et al., 2025; Pu et al., 2025; Garikaparthi et al., 2025). Despite encouraging signals, most efforts remain text-level and proposals are seldom coupled to rigorous execution.

Research Benchmarks. Major efforts have been made to evaluate LLMs on reproducing existing research including SUPER (Bogin et al., 2024), PaperBench (Starace et al., 2025), ResearchCodeBench (Hua et al., 2025), but not whether they can implement and validate new ideas. Contrary research benchmarks either rely on cluster-level compute requirements (Wijk et al., 2025; Wu et al., 2025c; Nathani et al., 2025), leverage LLM-judges for final grading (Chen et al., 2025a; Bragg et al., 2025), lack human baselines for comparison (Nathani et al., 2025; Bragg et al., 2025), or lack contamination-aware dataset construction (Wu et al., 2025c; Nathani et al., 2025). In contrast, we target these limitations

Failure mode Description Overconfidence in weak hypotheses

Agents often commit to a method without basic sanity checks such as baseline replication. This leads to confident iteration on foundations that were never validated.

Optimization and myopia

Runs frequently drift into surface-level tuning (e.g., hyperparameters) even when signals suggest larger objective-level changes are needed. This produces many trials with little to no improvement.

Non-comparable experiments

A common pattern is changing multiple factors at once or altering evaluation setup. This leads to the agent continuously iterating without a signal of whether it is actually improving.

Impatience and premature convergence

After finding the first runnable approach, agents tend to keep patching that line of attack instead of branching to alternatives. This reduces exploration, increasingly getting stuck in local optima.

Poor time and resource management

Agents launch expensive runs before validating correctness, or fail to reserve wall-time for grading and controlled comparisons. They also fail to optimally utilize GPUs.

Parallel experiment collapse

Agents are poor at starting and maintaining parallel experiments. They also lack a reliable track of what was tried, what failed, and what remains open; compounding into further confusion.

Context-length limits As runs progress, agent’s performance starts degrading with wrong tool calls, hallucinations etc., and summarization mechanisms tend to lose important context. Further, context window is also very often overloaded with irrelevant context from tool outputs. This is distinctly unnatural from how human’s tend to work on long-horizon tasks: for example just glancing at logs/outputs and retaining only important information.

Table 7: Failure modes and long-horizon limitations observed in agent interaction traces.

and simulate highly realistic settings for language model agents by providing a starter repository code and restricted web access.

Closed-loop environments. The recent effectiveness of RL in improving LLMs capabilities on verifiable tasks (DeepSeek-AI, 2025) has increased the value of gym-style environments. Where agents interact with the environment and learn from experience in an unsupervised manner. Notable examples include the initial OpenAI Gym (Brockman et al., 2016), LlamaGym (Pandey, 2024), LMRL-Gym (Abdulhai et al., 2025), SWE-Gym (Pan et al., 2025), and R2E-Gym (Jain et al., 2025).

### 7 Conclusion

In this work, we developed a rigorous benchmark to objectively evaluate LLM agents on the full arc of closed-loop AI research. To enable evaluation on these research problems, we designed an execution environment that supports easy integration and standardized testing of new agents. We then evaluated frontier LLM agents on our benchmark, measuring their ability to independently conduct long-horizon, open-ended research in executable codebases. Our empirical results expose substantial limitations in reliability due to poor experiment tracking, resource management, and context degradation. At the same time, we observe that frontier agents can occasionally produce strong results, suggesting nascent but genuine research capability. Overall, ResearchGym provides an accessible foundation for rigorous measurement and analysis of research agents, and for developing more capable systems.

### Discussion

Multi-modality. Our current task set does not include research problems requiring multi-modal reasoning, such as medical imaging, video understanding, or speech processing. This omission reflects practical constraints as multi-modal tasks often demand specialized hardware, large data transfers, and evaluation infrastructure beyond our current scope, and not a fundamental limitation of the ResearchGym framework. Extending the benchmark to include vision- or audio-centric research tasks is a natural direction for future work.

Training. Gym-style environments are commonly used to generate high-quality training data for fine-tuning agents via reinforcement learning or expert iteration. However, ResearchGym tasks are sufficiently difficult that only frontier LLMs achieve non-trivial performance, prohibiting direct training experiments. We nonetheless release all trajectories from our experiments to support future work. Exploring whether smaller models can be trained on traces from stronger agents remains an open question beyond our current scope.

Subjective Research. We purposefully exclude purely theoretical, analysis-driven, or proof-based papers. Evaluating success in these domains is inherently subjective and often requires expert human verification, which is difficult to scale. Therefore, ResearchGym focuses exclusively on empirical machine learning tasks where success can be measured via executable code and objective performance metrics. Future work may explore methods for integrating semi-automated evaluation pipelines to include a broader range of qualitative research tasks.

### Impact Statement

ResearchGym measures whether AI agents can autonomously improve upon state-of-the-art AI research. This automation could expand the hypotheses explored by scientists, reduce barriers to entry and even accelerate research in critical scientific and medical fields.

However, the capability to autonomously extend frontier research also carries risks. If models can iteratively refine and improve upon cutting-edge techniques, they could accelerate discoveries at a pace that outstrips our ability to assess their implications. Beyond capability risks, evaluation integrity poses a distinct challenge. Agents optimizing for benchmark metrics may discover shortcuts that inflate scores without reflecting genuine research capability. Such reward hacking if undetected, could lead to overestimates of AI research competence, with downstream consequences for critical deployment decisions. We take this concern seriously and incorporate an inspection-agent protocol to detect such common cheating strategies. While this does not guarantee immunity to all forms of gaming, we view adversarial robustness of research benchmarks as an ongoing challenge and encourage future work on detection and mitigation.

By open-sourcing ResearchGym, we aim to provide a transparent method for rigorously measuring autonomous research capabilities of frontier AI systems. We believe that understanding what AI agents can and cannot reliably accomplish is essential for calibrating expectations and preparing safeguards. ResearchGym represents one piece of a broader evaluation landscape for autonomous AI R&D.

### References

Marwa Abdulhai, Isadora White, Charlie Victor Snell, Charles Sun, Joey Hong, Yuexiang Zhai, Kelvin Xu, and Sergey Levine. LMRL gym: Benchmarks for multi-turn reinforcement learning with language models. In Forty-second International Conference on Machine Learning, 2025. URL https:// openreview.net/forum?id=hmGhP5DO2W.

UK AI Security Institute. Inspect AI: Framework for Large Language Model Evaluations, 2024. URL https://github.com/UKGovernmentBEIS/inspect_ai.

Anthropic. Claude 3.7 sonnet system card, 2025. URL https://assets.anthropic.com/m/ 785e231869ea8b3b/original/claude-3-7-sonnet-system-card.pdf. Accessed: 2025-03-10.

Anthropic. Claude code overview, 2026. URL https://code.claude.com/docs/en/overview. Accessed: 2026-01-24.

Jinheon Baek, Sujay Kumar Jauhar, Silviu Cucerzan, and Sung Ju Hwang. ResearchAgent: Iterative research idea generation over scientific literature with large language models. In Luis Chiruzzo, Alan Ritter, and Lu Wang, editors, Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), pages 6709–6738, Albuquerque, New Mexico, April 2025. Association for Computational Linguistics. ISBN 979-8-89176-189-6. doi: 10.18653/v1/2025.naacl-long.342. URL https://aclanthology.org/2025.naacl-long.342/.

Ben Bogin, Kejuan Yang, Shashank Gupta, Kyle Richardson, Erin Bransom, Peter Clark, Ashish Sabharwal, and Tushar Khot. SUPER: Evaluating agents on setting up and executing tasks from research repositories. In Yaser Al-Onaizan, Mohit Bansal, and Yun-Nung Chen, editors, Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, pages 12622–12645, Miami, Florida, USA, November 2024. Association for Computational Linguistics. doi: 10.18653/v1/ 2024.emnlp-main.702. URL https://aclanthology.org/2024.emnlp-main.702/.

Jonathan Bragg, Mike D’Arcy, Nishant Balepur, Dan Bareket, Bhavana Dalvi, Sergey Feldman, Dany Haddad, Jena D. Hwang, Peter Jansen, Varsha Kishore, Bodhisattwa Prasad Majumder, Aakanksha Naik, Sigal Rahamimov, Kyle Richardson, Amanpreet Singh, Harshit Surana, Aryeh Tiktinsky, Rosni Vasu, Guy Wiener, Chloe Anastasiades, Stefan Candra, Jason Dunkelberger, Dan Emery, Rob Evans, Malachi Hamada, Regan Huff, Rodney Kinney, Matt Latzke, Jaron Lochner, Ruben LozanoAguilera, Cecile Nguyen, Smita Rao, Amber Tanaka, Brooke Vlahos, Peter Clark, Doug Downey, Yoav Goldberg, Ashish Sabharwal, and Daniel S. Weld. Astabench: Rigorous benchmarking of ai agents with a holistic scientific research suite. Technical report, Allen Institute for AI, August 2025. URL https://www.datocms-assets.com/64837/1756485374-astabench-2025-08-29.pdf. Tech report (86 pages).

Greg Brockman, Vicki Cheung, Ludwig Pettersson, Jonas Schneider, John Schulman, Jie Tang, and Wojciech Zaremba. Openai gym, 2016.

Jun Shern Chan, Neil Chowdhury, Oliver Jaffe, James Aung, Dane Sherburn, Evan Mays, Giulio Starace, Kevin Liu, Leon Maksin, Tejal Patwardhan, Aleksander Madry, and Lilian Weng. MLEbench: Evaluating machine learning agents on machine learning engineering. In The Thirteenth International Conference on Learning Representations, 2025. URL https://openreview.net/forum? id=6s5uXNWGIh.

Khaoula Chehbouni, Mohammed Haddou, Jackie Chi Kit Cheung, and Golnoosh Farnadi. Neither valid nor reliable? investigating the use of llms as judges, 2025. URL https://arxiv.org/abs/2508.18076.

Hui Chen, Miao Xiong, Yujie Lu, Wei Han, Ailin Deng, Yufei He, Jiaying Wu, Yibo Li, Yue Liu, and Bryan Hooi. Mlr-bench: Evaluating ai agents on open-ended machine learning research, 2025a. URL https://arxiv.org/abs/2505.19955.

Ziru Chen, Shijie Chen, Yuting Ning, Qianheng Zhang, Boshi Wang, Botao Yu, Yifei Li, Zeyi Liao, Chen Wei, Zitong Lu, Vishal Dey, Mingyi Xue, Frazier N. Baker, Benjamin Burns, Daniel Adu-Ampratwum, Xuhui Huang, Xia Ning, Song Gao, Yu Su, and Huan Sun. Scienceagentbench: Toward rigorous assessment of language agents for data-driven scientific discovery. In The Thirteenth International Conference on Learning Representations, 2025b. URL https://openreview.net/forum?id=6z4YKr0GK6.

Audrey Cheng, Shu Liu, Melissa Pan, Zhifei Li, Shubham Agarwal, Mert Cemri, Bowen Wang, Alexander Krentsel, Tian Xia, Jongseok Park, Shuo Yang, Jeff Chen, Lakshya Agrawal, Ashwin Naren, Shulu Li, Ruiying Ma, Aditya Desai, Jiarong Xing, Koushik Sen, Matei Zaharia, and Ion Stoica. Let the barbarians in: How ai can accelerate systems performance research, 2025a. URL https://arxiv.

org/abs/2512.14806.

Audrey Cheng, Shu Liu, Melissa Pan, Zhifei Li, Bowen Wang, Alex Krentsel, Tian Xia, Mert Cemri, Jongseok Park, Shuo Yang, Jeff Chen, Lakshya Agrawal, Aditya Desai, Jiarong Xing, Koushik Sen, Matei Zaharia, and Ion Stoica. Barbarians at the gate: How ai is upending systems research, 2025b. URL https://arxiv.org/abs/2510.06189.

Pavel Chizhov, Catherine Arnett, Elizaveta Korotkova, and Ivan P. Yamshchikov. BPE gets picky: Efficient vocabulary refinement during tokenizer training. In Yaser Al-Onaizan, Mohit Bansal, and Yun-Nung Chen, editors, Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, pages 16587–16604, Miami, Florida, USA, November 2024. Association for Computational Linguistics. doi: 10.18653/v1/2024.emnlp-main.925. URL https://aclanthology.

org/2024.emnlp-main.925/. DeepSeek-AI. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning, 2025. URL https://arxiv.org/abs/2501.12948.

Aniketh Garikaparthi, Manasi Patwardhan, Lovekesh Vig, and Arman Cohan. IRIS: Interactive research ideation system for accelerating scientific discovery. In Pushkar Mishra, Smaranda Muresan, and Tao Yu, editors, Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations), pages 592–603, Vienna, Austria, July 2025. Association for Computational Linguistics. ISBN 979-8-89176-253-4. doi: 10.18653/v1/2025.acl-demo.57. URL https://aclanthology.org/2025.acl-demo.57/.

Shashwat Goel, Rishi Hazra, Dulhan Jayalath, Timon Willi, Parag Jain, William F. Shen, Ilias Leontiadis, Francesco Barbieri, Yoram Bachrach, Jonas Geiping, and Chenxi Whitehouse. Training ai co-scientists using rubric rewards, 2025. URL https://arxiv.org/abs/2512.23707.

Google. Gemini cli, 2026. URL https://github.com/google-gemini/gemini-cli. Accessed: 202601-24.

Mikaela Grace, Jeremy Hadfield, Rodrigo Olivares, and Jiri De Jonghe. Demystifying evals for ai agents, January 2026. URL https://www.anthropic.com/engineering/ demystifying-evals-for-ai-agents. Accessed: 2026-01-24.

Sikun Guo, Amir Hassan Shariatmadari, Guangzhi Xiong, Albert Huang, Eric Xie, Stefan Bekiranov, and Aidong Zhang. Ideabench: Benchmarking large language models for research idea generation,

2024. URL https://arxiv.org/abs/2411.02429.

Alec Helbling, Tuna Han Salih Meral, Benjamin Hoover, Pinar Yanardag, and Duen Horng Chau. Conceptattention: Diffusion transformers learn highly interpretable features. In Forty-second International Conference on Machine Learning, 2025. URL https://openreview.net/forum?id=Rc7y9HFC34.

Tianyu Hua, Harper Hua, Violet Xiang, Benjamin Klieger, Sang T. Truong, Weixin Liang, Fan-Yun Sun, and Nick Haber. Researchcodebench: Benchmarking llms on implementing novel machine learning research code, 2025. URL https://arxiv.org/abs/2506.02314.

Qian Huang, Jian Vora, Percy Liang, and Jure Leskovec. MLAgentbench: Evaluating language agents on machine learning experimentation. In Forty-first International Conference on Machine Learning,

2024. URL https://openreview.net/forum?id=1Fs1LvjYQW.

Alexander Hägele, Aryo Pradipta Gema, Henry Sleight, Ethan Perez, and Jascha Sohl-Dickstein. The hot mess of ai: How does misalignment scale with model intelligence and task complexity?, 2026. URL https://arxiv.org/abs/2601.23045.

Naman Jain, Jaskirat Singh, Manish Shetty, Liang Zheng, Koushik Sen, and Ion Stoica. R2e-gym: Procedural environments and hybrid verifiers for scaling open-weights swe agents, 2025. URL https: //arxiv.org/abs/2504.07164.

Hyeongwon Jang, Changhun Kim, and Eunho Yang. TIMING: Temporality-aware integrated gradients for time series explanation. In Forty-second International Conference on Machine Learning, 2025. URL https://openreview.net/forum?id=qOgKMqv9T7.

Zhengyao Jiang, Dominik Schmidt, Dhruv Srikanth, Dixing Xu, Ian Kaplan, Deniss Jacenko, and Yuxiang Wu. Aide: Ai-driven exploration in the space of code, 2025. URL https://arxiv.org/abs/ 2502.13138.

Patrick Tser Jern Kon, Jiachen Liu, Xinyi Zhu, Qiuyi Ding, Jingjia Peng, Jiarong Xing, Yibo Huang, Yiming Qiu, Jayanth Srinivasa, Myungjin Lee, Mosharaf Chowdhury, Matei Zaharia, and Ang Chen. Exp-bench: Can ai conduct ai research experiments?, 2025. URL https://arxiv.org/abs/2505. 24785.

Sandeep Kumar, Tirthankar Ghosal, Vinayak Goyal, and Asif Ekbal. Can large language models unlock novel scientific research ideas?, 2024. URL https://arxiv.org/abs/2409.06185.

Hosung Lee, Sejin Kim, Seungpil Lee, Sanha Hwang, Jihwan Lee, Byung-Jun Lee, and Sundong Kim. Arcle: The abstraction and reasoning corpus learning environment for reinforcement learning, 2024. URL https://arxiv.org/abs/2407.20806.

Haobin Li, Peng Hu, Qianjun Zhang, Xi Peng, XitingLiu, and Mouxing Yang. Test-time adaptation for cross-modal retrieval with query shift. In The Thirteenth International Conference on Learning Representations, 2025. URL https://openreview.net/forum?id=BmG88rONaU.

Long Li, Weiwen Xu, Jiayan Guo, Ruochen Zhao, Xinxuan Li, Yuqian Yuan, Boqiang Zhang, Yuming Jiang, Yifei Xin, Ronghao Dang, Yu Rong, Deli Zhao, Tian Feng, and Lidong Bing. Chain of ideas: Revolutionizing research in novel idea development with llm agents. arXiv preprint arXiv:2410.13185, 2024a. URL https://arxiv.org/abs/2410.13185.

Ziming Li, Qianbo Zang, David Ma, Jiawei Guo, Tuney Zheng, Minghao Liu, Xinyao Niu, Yue Wang, Jian Yang, Jiaheng Liu, Wanjun Zhong, Wangchunshu Zhou, Wenhao Huang, and Ge Zhang. Autokaggle: A multi-agent framework for autonomous data science competitions, 2024b. URL https://arxiv. org/abs/2410.20424.

Haokun Liu, Sicong Huang, Jingyu Hu, Yangqiaoyu Zhou, and Chenhao Tan. Hypobench: Towards systematic and principled benchmarking for hypothesis generation, 2025a. URL https://arxiv.org/ abs/2504.11524.

Yujie Liu, Zonglin Yang, Tong Xie, Jinjie Ni, Ben Gao, Yuqiang Li, Shixiang Tang, Wanli Ouyang, Erik Cambria, and Dongzhan Zhou. Researchbench: Benchmarking llms in scientific discovery via inspiration-based task decomposition, 2025b. URL https://arxiv.org/abs/2503.21248.

Zexi Liu, Yuzhu Cai, Xinyu Zhu, Yujie Zheng, Runkun Chen, Ying Wen, Yanfeng Wang, Weinan E, and Siheng Chen. Ml-master: Towards ai-for-ai via integration of exploration and reasoning, 2025c. URL https://arxiv.org/abs/2506.16499.

Chris Lu, Cong Lu, Robert Tjarko Lange, Jakob Foerster, Jeff Clune, and David Ha. The ai scientist: Towards fully automated open-ended scientific discovery, 2024. URL https://arxiv.org/abs/2408. 06292.

Ke Ma, Jiaqi Tang, Bin Guo, Fan Dang, Sicong Liu, Zhui Zhu, Lei Wu, Cheng Fang, Ying-Cong Chen, Zhiwen Yu, and Yunhao Liu. Surgeon: Memory-adaptive fully test-time adaptation via dynamic activation sparsity. In 2025 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), pages 30514–30523, 2025. doi: 10.1109/CVPR52734.2025.02841.

Bodhisattwa Prasad Majumder, Harshit Surana, Dhruv Agarwal, Bhavana Dalvi Mishra, Abhijeetsingh Meena, Aryan Prakhar, Tirth Vora, Tushar Khot, Ashish Sabharwal, and Peter Clark. Discoverybench: Towards data-driven discovery with large language models. In The Thirteenth International Conference on Learning Representations, 2025. URL https://openreview.net/forum?id=vyflgpwfJW.

Chunyu Miao, Henry Peng Zou, Yangning Li, Yankai Chen, Yibo Wang, Fangxin Wang, Yifan Li, Wooseong Yang, Bowei He, Xinni Zhang, Dianzhi Yu, Hanchen Yang, Hoang H Nguyen, Yue Zhou, Jie Yang, Jizhou Guo, Wenzhe Fan, Chin-Yuan Yeh, Panpan Meng, Liancheng Fang, Jinhu Qi, Wei-Chieh Huang, Zhengyao Gu, Yuwei Han, Langzhou He, Yuyao Yang, Yinghui Li, Hai-Tao Zheng, Xue Liu, Irwin King, and Philip S. Yu. Recode-h: A benchmark for research code development with interactive human feedback, 2025. URL https://arxiv.org/abs/2510.06186.

Deepak Nathani, Lovish Madaan, Nicholas Roberts, Nikolay Bashlykov, Ajay Menon, Vincent Moens, Amar Budhiraja, Despoina Magka, Vladislav Vorotilov, Gaurav Chaurasia, Dieuwke Hupkes, Ricardo Silveira Cabral, Tatiana Shavrina, Jakob Foerster, Yoram Bachrach, William Yang Wang, and Roberta Raileanu. Mlgym: A new framework and benchmark for advancing ai research agents, 2025. URL https://arxiv.org/abs/2502.14499.

Alexander Novikov, Ngân Vu˜, Marvin Eisenberger, Emilien Dupont, Po-Sen Huang, Adam Zsolt Wagner, Sergey Shirobokov, Borislav Kozlovskii, Francisco J. R. Ruiz, Abbas Mehrabian, M. Pawan Kumar, Abigail See, Swarat Chaudhuri, George Holland, Alex Davies, Sebastian Nowozin, Pushmeet Kohli, and Matej Balog. Alphaevolve: A coding agent for scientific and algorithmic discovery, 2025. URL https://arxiv.org/abs/2506.13131.

Yerim Oh, Jun-Hyung Park, Junho Kim, SungHo Kim, and SangKeun Lee. Incorporating domain knowledge into materials tokenization. In Wanxiang Che, Joyce Nabende, Ekaterina Shutova, and Mohammad Taher Pilehvar, editors, Proceedings of the 63rd Annual Meeting of the Association for

Computational Linguistics (Volume 1: Long Papers), pages 9623–9644, Vienna, Austria, July 2025. Association for Computational Linguistics. ISBN 979-8-89176-251-0. doi: 10.18653/v1/2025.acl-long. 474. URL https://aclanthology.org/2025.acl-long.474/.

Charles O’Neill, Tirthankar Ghosal, Roberta Răileanu, Mike Walmsley, Thang Bui, Kevin Schawinski, and Ioana Ciucă. Sparks of science: Hypothesis generation using structured paper data, 2025. URL https://arxiv.org/abs/2504.12976.

OpenAI. Codex cli, 2026. URL https://developers.openai.com/codex/cli/. Accessed: 2026-01-24. Anne Ouyang, Simon Guo, Simran Arora, Alex L. Zhang, William Hu, Christopher Ré, and Azalia

Mirhoseini. Kernelbench: Can llms write efficient gpu kernels?, 2025. URL https://arxiv.org/abs/ 2502.10517.

Jiayi Pan, Xingyao Wang, Graham Neubig, Navdeep Jaitly, Heng Ji, Alane Suhr, and Yizhe Zhang. Training software engineering agents and verifiers with SWE-gym. In ICLR 2025 Third Workshop on Deep Learning for Code, 2025. URL https://openreview.net/forum?id=lpFFpTbi9s.

Rohan Pandey. Llamagym: Fine-tune llm agents with online reinforcement learning. GitHub, 2024. URL https://github.com/KhoomeiK/LlamaGym.

Jacob Piland, Chris Sweet, and Adam Czajka. Diffgradcam: A universal class activation map resistant to adversarial training, 2025. URL https://arxiv.org/abs/2506.08514.

Kevin Pu, K. J. Kevin Feng, Tovi Grossman, Tom Hope, Bhavana Dalvi Mishra, Matt Latzke, Jonathan Bragg, Joseph Chee Chang, and Pao Siangliulue. Ideasynth: Iterative research idea development through evolving and composing idea facets with literature-grounded feedback. In Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems, CHI ’25, page 1–31. ACM, April 2025. doi: 10.1145/3706598.3714057. URL http://dx.doi.org/10.1145/3706598.3714057.

Yansheng Qiu, Haoquan Zhang, Zhaopan Xu, Ming Li, Diping Song, Zheng Wang, and Kaipeng Zhang. Ai idea bench 2025: Ai research idea generation benchmark, 2025. URL https://arxiv.org/abs/ 2504.14191.

Marissa Radensky, Simra Shahid, Raymond Fok, Pao Siangliulue, Tom Hope, and Daniel S. Weld. Scideator: Human-llm scientific idea generation grounded in research-paper facet recombination, 2025. URL https://arxiv.org/abs/2409.14634.

Ben Rank, Hardik Bhatnagar, Matthias Bethge, and Maksym Andriushchenko. Posttrainbench: Measuring ai ability to perform llm post-training, 2025.

Rico Sennrich, Barry Haddow, and Alexandra Birch. Neural machine translation of rare words with subword units. In Katrin Erk and Noah A. Smith, editors, Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 1715–1725, Berlin, Germany, August 2016. Association for Computational Linguistics. doi: 10.18653/v1/P16-1162. URL https://aclanthology.org/P16-1162/.

Asankhaya Sharma. Openevolve: an open-source evolutionary coding agent, 2025. URL https: //github.com/codelion/openevolve.

Chenglei Si, Tatsunori Hashimoto, and Diyi Yang. The ideation-execution gap: Execution outcomes of llm-generated versus human research ideas, 2025a. URL https://arxiv.org/abs/2506.20803.

Chenglei Si, Diyi Yang, and Tatsunori Hashimoto. Can LLMs generate novel research ideas? a large-scale human study with 100+ NLP researchers. In The Thirteenth International Conference on Learning Representations, 2025b. URL https://openreview.net/forum?id=M23dTGWCZy.

Chenglei Si, Zitong Yang, Yejin Choi, Emmanuel Candès, Diyi Yang, and Tatsunori Hashimoto. Towards execution-grounded automated ai research, 2026. URL https://arxiv.org/abs/2601.14525.

Zachary S Siegel, Sayash Kapoor, Nitya Nadgir, Benedikt Stroebl, and Arvind Narayanan. COREbench: Fostering the credibility of published research through a computational reproducibility agent benchmark. Transactions on Machine Learning Research, 2024. ISSN 2835-8856. URL https: //openreview.net/forum?id=BsMMc4MEGS.

Giulio Starace, Oliver Jaffe, Dane Sherburn, James Aung, Jun Shern Chan, Leon Maksin, Rachel Dias, Evan Mays, Benjamin Kinsella, Wyatt Thompson, Johannes Heidecke, Amelia Glaese, and Tejal Patwardhan. Paperbench: Evaluating AI’s ability to replicate AI research. In Forty-second International Conference on Machine Learning, 2025. URL https://openreview.net/forum?id=xF5PuTLPbn.

Haoyang Su, Renqi Chen, Shixiang Tang, Zhenfei Yin, Xinzhe Zheng, Jinzhe Li, Biqing Qi, Qi Wu, Hui Li, Wanli Ouyang, Philip Torr, Bowen Zhou, and Nanqing Dong. Many heads are better than one: Improved scientific idea generation by a LLM-based multi-agent system. In Wanxiang Che, Joyce Nabende, Ekaterina Shutova, and Mohammad Taher Pilehvar, editors, Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 28201–28240, Vienna, Austria, July 2025. Association for Computational Linguistics. ISBN 979-8-89176-251-0. doi: 10.18653/v1/2025.acl-long.1368. URL https://aclanthology.org/2025.acl-long.1368/.

Jiabin Tang, Lianghao Xia, Zhonghang Li, and Chao Huang. Ai-researcher: Autonomous scientific innovation, 2025a. URL https://arxiv.org/abs/2505.18705.

Xiangru Tang, Yuliang Liu, Zefan Cai, Daniel Shao, Junjie Lu, Yichi Zhang, Zexuan Deng, Helan Hu, Kaikai An, Ruijun Huang, Shuzheng Si, Chen Sheng, Haozhe Zhao, Liang Chen, Tianyu Liu, Yujia Qin, Wangchunshu Zhou, Yilun Zhao, Zhiwei Jiang, Baobao Chang, Arman Cohan, and Mark Gerstein. ML-bench: Evaluating large language models and agents for machine learning tasks on repository-level code. In Towards Agentic AI for Science: Hypothesis Generation, Comprehension, Quantification, and Validation, 2025b. URL https://openreview.net/forum?id=T2mtCFKIEG.

Yongxiang Tang, Yanhua cheng, Xiaocheng Liu, Jiaochenchen, Yanxiang Zeng, Ning Luo, Pengjia Yuan, Xialong Liu, and Peng Jiang. Learning monotonic probabilities with a generative cost model. In Forty-second International Conference on Machine Learning, 2025c. URL https://openreview.net/ forum?id=VWjkpro9gv.

InternAgent Team, Bo Zhang, Shiyang Feng, Xiangchao Yan, Jiakang Yuan, Runmin Ma, Yusong Hu, Zhiyin Yu, Xiaohan He, Songtao Huang, Shaowei Hou, Zheng Nie, Zhilong Wang, Jinyao Liu, Tianshuo Peng, Peng Ye, Dongzhan Zhou, Shufei Zhang, Xiaosong Wang, Yilan Zhang, Meng Li, Zhongying Tu, Xiangyu Yue, Wangli Ouyang, Bowen Zhou, and Lei Bai. Internagent: When agent becomes the scientist – building closed-loop system from hypothesis to verification, 2025. URL https://arxiv.org/abs/2505.16938.

Minyang Tian, Luyu Gao, Dylan Zhang, Xinan Chen, Cunwei Fan, Xuefei Guo, Roland Haas, Pan Ji, Kittithat Krongchon, Yao Li, Shengyan Liu, Di Luo, Yutao Ma, HAO TONG, Kha Trinh, Chenyu Tian, Zihan Wang, Bohao Wu, Shengzhu Yin, Minhui Zhu, Kilian Lieret, Yanxin Lu, Genglin Liu, Yufeng Du, Tianhua Tao, Ofir Press, Jamie Callan, Eliu A Huerta, and Hao Peng. Scicode: A research coding benchmark curated by scientists. In The Thirty-eight Conference on Neural Information Processing Systems Datasets and Benchmarks Track, 2024. URL https://openreview.net/forum? id=ADLaALtdoG.

Anh Mai Vu, Tuan L. Vo, Ngoc Lam Quang Bui, Nam Nguyen Le Binh, Akash Awasthi, Huy Quoc Vo, Thanh-Huy Nguyen, Zhu Han, Chandra Mohan, and Hien Van Nguyen. Contrastive integrated gradients: A feature attribution-based method for explaining whole slide image classification, 2025. URL https://arxiv.org/abs/2511.08464.

Renhao Wang, Kevin Frans, Pieter Abbeel, Sergey Levine, and Alexei A Efros. Prioritized generative replay. In The Thirteenth International Conference on Learning Representations, 2025. URL https: //openreview.net/forum?id=5IkDAfabuo.

Yipei Wang and Xiaoqian Wang. “why not other classes?”: Towards class-contrastive back-propagation explanations. In S. Koyejo, S. Mohamed, A. Agarwal, D. Belgrave, K. Cho, and A. Oh, editors, Advances in Neural Information Processing Systems, volume 35, pages 9085–9097. Curran Associates, Inc., 2022. URL https://proceedings.neurips.cc/paper_files/paper/2022/file/ 3b7a66b2d1258e892c89f485b8f896e0-Paper-Conference.pdf.

Yixuan Weng, Minjun Zhu, Guangsheng Bao, Hongbo Zhang, Jindong Wang, Yue Zhang, and Linyi Yang. Cycleresearcher: Improving automated research via automated review. In The Thirteenth International Conference on Learning Representations, 2025a. URL https://openreview.net/forum? id=bjcsVLoHYs.

Yixuan Weng, Minjun Zhu, Qiujie Xie, Qiyao Sun, Zhen Lin, Sifan Liu, and Yue Zhang. Deepscientist: Advancing frontier-pushing scientific findings progressively, 2025b. URL https://arxiv.org/abs/ 2509.26603.

Hjalmar Wijk, Tao Roa Lin, Joel Becker, Sami Jawhar, Neev Parikh, Thomas Broadley, Lawrence Chan, Michael Chen, Joshua M Clymer, Jai Dhyani, Elena Ericheva, Katharyn Garcia, Brian Goodrich, Nikola Jurkovic, Megan Kinniment, Aron Lajko, Seraphina Nix, Lucas Jun Koba Sato, William Saunders, Maksym Taran, Ben West, and Elizabeth Barnes. RE-bench: Evaluating frontier AI r&d capabilities of language model agents against human experts. In Forty-second International Conference on Machine Learning, 2025. URL https://openreview.net/forum?id=3rB0bVU6z6.

Xiangyu Wu, Feng Yu, Yang Yang, Qing-Guo Chen, and Jianfeng Lu. Multi-label test-time adaptation with bound entropy minimization. In The Thirteenth International Conference on Learning Representations, 2025a. URL https://openreview.net/forum?id=75PhjtbBdr.

Yichen Wu, Hongming Piao, Long-Kai Huang, Renzhen Wang, Wanhua Li, Hanspeter Pfister, Deyu Meng, Kede Ma, and Ying Wei. SD-loRA: Scalable decoupled low-rank adaptation for class incremental learning. In The Thirteenth International Conference on Learning Representations, 2025b. URL https://openreview.net/forum?id=5U1rlpX68A.

Yonghui Wu, Mike Schuster, Zhifeng Chen, Quoc V. Le, Mohammad Norouzi, Wolfgang Macherey, Maxim Krikun, Yuan Cao, Qin Gao, Klaus Macherey, Jeff Klingner, Apurva Shah, Melvin Johnson, Xiaobing Liu, Łukasz Kaiser, Stephan Gouws, Yoshikiyo Kato, Taku Kudo, Hideto Kazawa, Keith Stevens, George Kurian, Nishant Patil, Wei Wang, Cliff Young, Jason Smith, Jason Riesa, Alex Rudnick, Oriol Vinyals, Greg Corrado, Macduff Hughes, and Jeffrey Dean. Google’s neural machine translation system: Bridging the gap between human and machine translation, 2016. URL https:

//arxiv.org/abs/1609.08144.

Yunze Wu, Dayuan Fu, Weiye Si, Zhen Huang, Mohan Jiang, Keyu Li, Shijie Xia, Jie Sun, Tianze Xu, Xiangkun Hu, Pengrui Lu, Xiaojie Cai, Lyumanshan Ye, Wenhong Zhu, Yang Xiao, and Pengfei Liu. Innovatorbench: Evaluating agents’ ability to conduct innovative llm research, 2025c. URL https://arxiv.org/abs/2510.27598.

Zhuo Xu, Xiang Xiang, and Yifan Liang. Overcoming shortcut problem in vlm for robust out-ofdistribution detection. In 2025 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), pages 15402–15412, 2025. doi: 10.1109/CVPR52734.2025.01435.

Yutaro Yamada, Robert Tjarko Lange, Cong Lu, Shengran Hu, Chris Lu, Jakob Foerster, Jeff Clune, and David Ha. The ai scientist-v2: Workshop-level automated scientific discovery via agentic tree search, 2025. URL https://arxiv.org/abs/2504.08066.

Shuo Yan, Ruochen Li, Ziming Luo, Zimu Wang, Daoyang Li, Liqiang Jing, Kaiyu He, Peilin Wu, George Michalopoulos, Yue Zhang, Ziyang Zhang, Mian Zhang, Zhiyu Chen, and Xinya Du. Lmrbench: Evaluating llm agent’s ability on reproducing language modeling research, 2025a. URL https://arxiv.org/abs/2506.17335.

Zhiyuan Yan, Jiangming Wang, Peng Jin, Ke-Yue Zhang, Chengchun Liu, Shen Chen, Taiping Yao, Shouhong Ding, Baoyuan Wu, and Li Yuan. Orthogonal subspace decomposition for generalizable AI-generated image detection. In Forty-second International Conference on Machine Learning, 2025b. URL https://openreview.net/forum?id=GFpjO8S8Po.

Zonglin Yang, Xinya Du, Junxian Li, Jie Zheng, Soujanya Poria, and Erik Cambria. Large language models for automated open-domain scientific hypotheses discovery. In Lun-Wei Ku, Andre Martins, and Vivek Srikumar, editors, Findings of the Association for Computational Linguistics: ACL 2024, pages 13545–13565, Bangkok, Thailand, August 2024. Association for Computational Linguistics. doi: 10.18653/v1/2024.findings-acl.804. URL https://aclanthology.org/2024.findings-acl.804/.

Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik R Narasimhan, and Yuan Cao. React: Synergizing reasoning and acting in language models. In The Eleventh International Conference on Learning Representations, 2023. URL https://openreview.net/forum?id=WE_vluYUL-X.

Shaked Yehezkel and Yuval Pinter. Incorporating context into subword vocabularies. In Andreas Vlachos and Isabelle Augenstein, editors, Proceedings of the 17th Conference of the European Chapter of the Association for Computational Linguistics, pages 623–635, Dubrovnik, Croatia, May 2023. Association for Computational Linguistics. doi: 10.18653/v1/2023.eacl-main.45. URL https://aclanthology.

org/2023.eacl-main.45/.

Haofei Yu, Zhaochen Hong, Zirui Cheng, Kunlun Zhu, Keyang Xuan, Jinwei Yao, Tao Feng, and Jiaxuan You. Researchtown: Simulator of human research community. In Forty-second International Conference on Machine Learning, 2025. URL https://openreview.net/forum?id=CZPOIZqWwd.

Jiakang Yuan, Xiangchao Yan, Bo Zhang, Tao Chen, Botian Shi, Wanli Ouyang, Yu Qiao, Lei Bai, and Bowen Zhou. Dolphin: Moving towards closed-loop auto-research through thinking, practice, and feedback. In Wanxiang Che, Joyce Nabende, Ekaterina Shutova, and Mohammad Taher Pilehvar, editors, Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 21768–21789, Vienna, Austria, July 2025. Association for Computational Linguistics. ISBN 979-8-89176-251-0. doi: 10.18653/v1/2025.acl-long.1056. URL https://aclanthology.org/2025.acl-long.1056/.

Qinggang Zhang, Zhishang Xiang, Yilin Xiao, Le Wang, Junhui Li, Xinrun Wang, and Jinsong Su. FaithfulRAG: Fact-level conflict modeling for context-faithful retrieval-augmented generation. In Wanxiang Che, Joyce Nabende, Ekaterina Shutova, and Mohammad Taher Pilehvar, editors, Proceedings of the 63rd

Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 21863– 21882, Vienna, Austria, July 2025a. Association for Computational Linguistics. ISBN 979-8-89176-251-0. doi: 10.18653/v1/2025.acl-long.1062. URL https://aclanthology.org/2025.acl-long.1062/.

Yunxiang Zhang, Muhammad Khalifa, Shitanshu Bhushan, Grant D Murphy, Lajanugen Logeswaran, Jaekyeom Kim, Moontae Lee, Honglak Lee, and Lu Wang. Mlrc-bench: Can language agents solve machine learning research challenges?, 2025b. URL https://arxiv.org/abs/2504.09702.

Guangtao Zheng, Wenqian Ye, and Aidong Zhang. Neurontune: Towards self-guided spurious bias mitigation. In Forty-second International Conference on Machine Learning, 2025. URL https: //openreview.net/forum?id=qC5FZs34Xr.

Minjun Zhu, Qiujie Xie, Yixuan Weng, Jian Wu, Zhen Lin, Linyi Yang, and Yue Zhang. Ai scientists fail without strong implementation capability, 2025a. URL https://arxiv.org/abs/2506.01372.

Yun Zhu, Le Hui, Hang Yang, Jianjun Qian, Jin Xie, and Jian Yang. Learning class prototypes for unified sparse-supervised 3d object detection. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), pages 9911–9920, June 2025b.

Qiran Zou, Hou Hei Lam, Wenhao Zhao, Yiming Tang, Tingting Chen, Samson Yu, Tianyi Zhang, Chang Liu, Xiangyang Ji, and Dianbo Liu. Fml-bench: A benchmark for automatic ml research agents highlighting the importance of exploration breadth, 2025. URL https://arxiv.org/abs/2510.10472.

### A Relevant baselines

We draw comparison between recent systems for “automating research”. The outlined differences between such systems justifies the design choice and development of our agentic baseline.

Table 8: Systems related to automated / agentic research, grouped by control strategy.

Category System Description

AlphaEvolve (Novikov et al., 2025)

Evolutionary coding agent for algorithm discovery/optimization across math and computing (data-center scheduling, chip design, kernels, math). Reports: +0.7% Borg recovery, 23% kernel speedup (⇒ 1% LLM train time cut), up to 32.5% FlashAttention speedup, ∼20% of ∼50 open math problems improved.

Evolutionary Search

OpenEvolve (Sharma, 2025)

Open-source AlphaEvolve-style evolutionary code search; shown on GPU/kernel optimization, circle packing, algorithm design; repo reports ∼2.8× kernel speedups (Apple M1 Pro) and SOTA circle packing at n=26.

ADRS (AI-Driven Research for Systems) (Cheng et al., 2025b,a)

Automating systems research (e.g., scheduling, load balancing) via iterative LLM-generated code and simulator-based scoring; case studies report ADRS-generated algorithms matching/exceeding human SOTA.

Automated Idea Executor (Si et al., 2026)

AI-Scientist (Yamada et al., 2025)

Tree-based planning and execution, through parallel experiment generation and iterative debugging. One full execution resulted in a paper which passed workshop level peer-review at a top-tier conference.

Tree-based Search

AIDE (Jiang et al., 2025) Tree-based exploration of the solution space. AIDE iteratively draft programs as nodes in a tree, debugging and improving. Current demonstrated SOTA on RE-Bench.

ML-Master (Liu et al., 2025c)

Integrates exploration and reasoning along with an adaptive memory mechanism.

Dolphin (Yuan et al., 2025)

Progresses through the stages of research of ideation, feedback and experimentation.

Multi-agent Frameworks

InternAgent (Team et al., 2025)

Closed-loop literature → method → experiment over a fixed science-task suite.

DeepScientist (Weng et al., 2025b)

Long-horizon autonomous discovery (large GPUs, testing ∼1k ideas); powerful but operationally heavy.

Novix (Tang et al., 2025a) A multi-agent framework that orchestrates the complete research pipeline–from literature review and hypothesis generation to algorithm implementation and publication-ready manuscript preparation.

BasicAgent (Starace et al., 2025)

Generic InspectAI / ReAct scaffold with tool-calling; task-agnostic.

Asta Agents (Bragg et al.,

- 2025)

InspectAI-based agents configured for agent benchmarks.

Claude Code (Anthropic,

- 2026)


Anthropic’s agentic coding tool with terminal access, file editing, and web browsing capabilities.

Generic Scaffold

Codex CLI (OpenAI, 2026)

OpenAI’s command-line coding agent with sandboxed execution and multi-file editing.

Gemini CLI (Google, 2026)

Google’s terminal-based coding agent with agentic tool use and code execution.

ResearchGym Agent (ours)

InspectAI-style agent extended with research-specific tools (papers/repos, context condensation, execution hooks), meant for dynamic tasks and single-GPU / bounded-time / API budgets.

Together, these systems illustrate the breadth and momentum of automated research across algorithm discovery, kernel optimization, scientific analysis, and end-to-end workflows. ResearchGym complements this landscape by providing a public, compute-feasible, and programmatically graded surface where such systems can be evaluated.

Scope of Evaluation. Our primary goal is to evaluate the raw research capabilities of frontier language models rather than to engineer the best-performing agentic system. Consequently, our results likely represent a lower bound on what is achievable: more sophisticated systems could yield further improvements. We attempted to integrate several existing systems into our evaluation framework, including AI-Scientist and ML-Master, but found that they did not transfer well to our task setting without substantial modification (see Appendix D.3 for detailed discussion). We also evaluated generalpurpose coding agents including Claude Code and Codex; their performance is reported in Table 6. Lastly, due to the cost of running multi-agent setups on long-horizon tasks, it falls outside our experimental scope. However, we provide a contribution guide in our repository, which the research community can follow to integrate and evaluate new agentic systems on our benchmark.

### B Benchmark Details

- B.1 Development Set

Thorough and scientific benchmarking requires that developed methods are not narrowly tuned towards certain benchmarks but demonstrate some generalizability. To promote better practices we also develop 3 tasks as part of the dev set. The only difference during collection is we forego the restriction of Oral/Spotlight papers and possible contamination. This is in contrast to recent benchmarks which only provide a test set. Details are provided in Table 9.

We leverage the development set to refine and finalize our experimental settings. This includes steps such as prompting, time limits, token boundary for context summarization etc.

Paper Conference Category Evaluation metric

NeuronTune: Towards Self-Guided Spurious Bias Mitigation (Zheng et al., 2025)

ICML 2025

Deep Learning, Robustness

Worst Group Accuracy, Accuracy Gap

Multi-Label Test-Time Adaptation with Bound Entropy Minimization (Wu et al., 2025a)

ICLR 2025

VLMs, Test-Time Adaptation

mean Average Precision (mAP)

Learning Monotonic Probabilities with a Generative Cost Model (Tang et al., 2025c)

ICML 2025

Generative Models and Autoencoders

MAE, AUC, Acc, RMSE

Table 9: Selected papers for ResearchGym (Development Set).

- B.2 Task Metadata


Title Abbrv arXiv (v1) CitationsGitHub stars

License GPU requirements

MDT 2025-06-09 0 2 CC By 4.0 None

Incorporating Domain Knowledge into Materials Tokenization (Oh et al., 2025)

CMR 2024-10-21 17 28 Apache 2.0

None

Test-time Adaptation for Cross-modal Retrieval with Query Shift (Li et al., 2025)

TIM 2025-06-05 0 12 CC By 4.0 None

TIMING: Temporality-Aware Integrated Gradients for Time Series Explanation (Jang et al., 2025)

CL 2025-01-22 24 64 MIT License

None

SD-LoRA: Scalable Decoupled Low-Rank Adaptation for Class Incremental Learning (Wu et al., 2025b)

Prioritized Generative Replay (Wang et al., 2025) IRB 2024-10-23 8 21 MIT License

12GB

SBM 2025-05-29 1 2 CC By 4.0 None

NeuronTune: Towards Self-Guided Spurious Bias Mitigation (Zheng et al., 2025)

MLTTA

2025-02-06 3 9 CC By 4.0 None

Multi-Label Test-Time Adaptation with Bound Entropy Minimization (Wu et al., 2025a)

GCM 2025-06-04 0 2 CC BY-SA 4.0

None

Learning Monotonic Probabilities with a Generative Cost Model (Tang et al., 2025c)

Table 10: Task metadata for ResearchGym. Citations and GitHub stars as of 2025-10-10. arXiv (v1) dates denote initial preprint submission. GPU requirements are reported if mentioned in the paper and reproduced manually for verification.

### C Benchmark Construction

#### C.1 Dataset Collection Guidelines

We adhere to certain core principles throughout all steps while building our benchmark. The principles are briefly outlined and compared against in Table 1. Here, we emphasize how our design choices introduce certain tradeoffs while selecting and constructing tasks. We hope this justifies the size and quality of our benchmark while outlining best practices for future versions and community adoption such as adding more tasks, refining current evaluation setups etc.

- P1: Feasibility. The primary consideration during the initial stages of filtering source papers which can serve as tasks is feasibility. We want to find tasks which are computationally light. The first round of filtering happens through LLM, which yields the GPU memory requirement. We place strong filters on papers which require high computational resources (greater than 24GB GPU). On top of this, we go through several rounds of manual filtering, this can reveal subtle details which render the paper non-compatible for our setting. This can include the time spent for obtaining the results, for example despite using a small GPU of 24GB, the authors might have trained for a few days to achieve the results, for practical purposes this introduces a number of complexities, hence we exclude such papers.


- • hardware-specific results where latency is the primary metric and we want hardware-independent reporting;
- • API-heavy papers that depend on closed LLMs and therefore blow up budget;
- • papers that do not report GPUs but effectively need >48GB and were manually filtered out.


Further, some papers after fitting all the above criteria require access to gated datasets, or huge datasets with over 300GB, such factors again render the tasks infeasible for our settings.

- P2: Objectivity. We aim to minimize subjectivity for clearer comparison, however LLMs despite being given full papers can fail to reliably classify whether the primary metrics of the paper are objectively gradable or not. Due to a lot of edge cases and external context dependent factors, this step also required manual human verification.
- P3: Open-access. This remains an easily verifiable aspect for most cases, we filter papers which do not open-source their code. However, intricacies in later stages such as access to gated models and datasets can create problems.
- P4: Quality. The first natural filter is to select from award-winning papers, for top-tier conferences which only give award to top 1-5% of submissions, after going multiple rounds of peer-review and/or dedicated award selection committee, we can assume high novelty and importance of the work. We aim to cover more ground by selecting tasks which vary in domains to improve diversity. We also filter some papers which did not show enough room for improvement, these were cases where performance improvement between baseline and state-of-the-art were merely a few points (1-2) this can help exclude cases of ambiguity. Additionally, we select for a mix of tasks which give space for open-ended creativity, such as new algorithms of architecture changes and also for grounded research sub-tasks such as building new datasets.
- P5: Contamination. Prioritising frontier LLMs as of August 2025, and their knowledge cutoffs of September 30 20247 we only select papers from conferences whose proceedings were released post January 2025. We also cross check whether the paper or its variant was posted on arXiv before the official proceedings, we find two papers’ whose initial draft was uploaded to arXiv on October 2024. This ensures the paper and it’s method has not been seen by the LLMs during their training phases.


#### C.2 Examples of Late-stage Exclusions

After automated filtering, we manually audited the remaining candidates and removed papers that violated our core constraints. Table 11 lists representative late-stage exclusions and the principles they violated.

7https://platform.openai.com/docs/models/gpt-5

###### Candidate paper Reason for exclusion Principles

Passed keyword-based filtering, but closer inspection revealed substantial GPU requirements, making it infeasible within our target compute budget.

P1

ConceptAttention: Diffusion Transformers Learn Highly Interpretable Features (Helbling et al., 2025)

Despite strong fit (objective evaluation, low VRAM, no large datasets), the reported metrics (GFLOPs, cache, latency) were hardware-native and tied to a specific edge system (Jetson Xavier NX). Running on A100 would invalidate baselines and confound comparisons.

P2

SURGEON: Memory-Adaptive Fully Test-Time Adaptation via Dynamic Activation Sparsity (Ma et al., 2025)

Datasets were gated (email/forms) with licensing/access friction, and exceeded 300GB, making execution impractical within our 12–24 hour budget.

P1, P3

Learning Class Prototypes for Unified Sparse-Supervised 3D Object Detection (Zhu et al., 2025b)

Dependent on gated datasets of prohibitive size, creating both accessibility and execution-time barriers.

P1, P3

Orthogonal Subspace Decomposition for Generalizable AI-Generated Image Detection (Yan et al., 2025b)

Training and evaluation could not reliably complete within our 12–24 hour execution budget due to dataset scale and end-to-end runtime.

P1

Overcoming Shortcut Problem in VLM for Robust Out-of-Distribution Detection (Xu et al., 2025)

Loading required 7B-scale models exceeded our VRAM budget; introducing quantization would alter baseline performance and compromise comparability, so we excluded it to preserve consistency.

P1

FaithfulRAG: Fact-Level Conflict Modeling for Context-Faithful Retrieval-Augmented Generation (Zhang et al., 2025a)

- Table 11: Representative candidates excluded after manual audit. (P1: compute/runtime/VRAM budget; P2: hardware-tied metrics/baselines; P3: dataset accessibility/licensing/size constraints.)


#### C.3 Dataset Collection Prompts

##### Card Extraction For Filtering

You are an information-extraction model. Given the full Markdown of a research paper, extract the following fields exactly and return only valid JSON (UTF-8, no trailing commas, no extra keys).

Do not mention the paper’s title or acronyms. If a field is not explicitly stated in the paper, output ‘null‘ for that field. Do not infer or hallucinate. When numbers/units are present (e.g., GPU type, VRAM, hours, accuracy), preserve them verbatim.

##### Fields to extract (keys must match exactly):

- • ‘problem_statement‘ (2-4 sentences, what is being solved)
- • ‘motivation‘ (2-4 sentences, why it matters)
- • ‘methodology‘ (4-8 sentences, detailed description of the methodology/innovation introduced in the paper)
- • ‘hint‘ (2-3 sentences, high-level idea borrowed from the original paper’s methodology, which could guide/seed similar research directions)
- • ‘experimental_settings‘ (concise bullet-style text covering datasets, splits, metrics, evaluation setup and hyperparameters; include appendix details if present)
- • ’gpu_required’ (boolean, should be true only if the paper mentions the use of GPUs)
- • ’gpu_memory_required’ (number, null if not required)
- • ‘compute_requirements‘ (verbatim mentions of hardware/runtime: GPU model(s), VRAM, GPU count, CPU/RAM, training/inference time, seeds; ‘null‘ if absent)
- • ‘api_requirements‘ (list of external APIs/services and any stated budgets/quotas; ‘null‘ if absent)
- • ‘code_availability‘ (boolean)
- • ‘code_link‘ (URL string if available, else ‘null‘)
- • ’evaluation_is_objective’ (boolean, true if the paper is not a survey, position, analysis, understanding, proof, etc. but an objective evaluation)
- • ’evaluation_metrics’ (array of strings)


Output format (schema): “‘json { "problem_statement": "...", "motivation": "...", "methodology": "...", "hint": "...", "experimental_settings": "...", "gpu_required": "...", "gpu_memory_required": "...", "compute_requirements": "...", "api_requirements": ["..."], "code_availability": "...", "code_link": "https://...", "evaluation_is_objective": true, "evaluation_metrics": ["..."], }

Instructions: Read the entire Markdown (including appendix). Extract only what is explicitly present; if unsure, return null. Keep technical names and figures verbatim (model names, GPU types, metric strings, ± CIs). For tables, include only the main results tables. If the paper uses figures instead of tables for results, set tables to null. Return only the JSON object. No prose, no comments. Paper Markdown starts below: <PAPER_MD>

##### Create Task Description From Extracted Card

Convert the provided JSON into a high-quality, concise, and faithful task description.

INPUTS:

- - JSON (authoritative; contains only the fields you must use) embedded after <PAPER_JSON>.
- - PAPER MARKDOWN (context-only) embedded after <PAPER_MD>. Use it ONLY to:


- (a) extract metric definitions verbatim, and
- (b) identify and filter out the paper’s own method rows from results tables (including aliases/acronyms introduced by the paper). Strict authoring rules:


- 1) Research Goal: Concatenate problem_statement and motivation exactly as given (verbatim, unchanged) under the heading "Research Goal".
- 2) Experimental Settings: Under the heading "Experimental Settings", reproduce only the necessary parts of the experimental_settings, which might be required to developing a new method, like training data used, but not method specific details or hyperparameters.
- 3) Evaluation Metrics: Under the heading "Evaluation Metrics", list the metrics exactly as given AND, for each, append its definition verbatim if it appears anywhere in the paper markdown. If no elaboration is found in the paper, list only the metric name/acronym as-is (no colon).
- 4) Baseline Results: For each Markdown table in result_tables values: - Remove any rows corresponding to the paper’s approach. Use the paper markdown to match method names/acronyms/aliases. Also remove rows whose first cell contains case-insensitive "ours"/"our". Append a row named "Your Method" with "–" for all metric cells; keep the same number of columns and order. - Preserve all remaining baseline rows and values verbatim.


6) Style: Be concise, structured, and objective. No extra commentary.

Output format (Markdown only, exactly these sections in this order; no preamble, no epilogue):

Research Goal <verbatim problem_statement + motivation>

Experimental Settings <exact experimental_settings>

Evaluation Metrics

- One bullet per metric. If a definition is found in the paper markdown, format it as "- <metric>: <verbatim definition>". Otherwise use "- <metric>".

Baseline Results (to beat) <one or more cleaned Markdown tables>

<PAPER_JSON>

paper_json

<PAPER_MD>

paper_md

#### C.4 Task Packaging Guidelines

The most crucial step of constructing such a benchmark is to ensure faithful evaluation. Parallel work, Cheng et al. (2025b) also emphasize on this point that while simulator based verification is cheap and easy (trivial to test LLMs and even find novel improvements given objective evaluation), setting up evaluations which are faithful is far from trivial. We provide a transparent description of our process of constructing skeleton task repositories for LLM agents, our hurdles and findings.

Neutrality: The most obvious step is removing the original method proposed by the paper. But it is rarely ever present in the repository as an isolated function, rather it would have utilities, sub-tasks and traces of these aspects are scattered throughout the repository. At certain points in the process of construction we have to make decisions that involve a tradeoff.

For example: for the continual learning task (Wu et al., 2025b), the repository includes LoRa implementations, while LoRa is a general technique, there are subtler details around decoupling/scaling which are specific to the paper’s method. Removing these aspects while retaining the generic LoRa implementation is non-trivial. Further keeping LoRa as a prominent baseline in the code might bias the agent towards LoRa-style ideas.

In practice we encounter cases such as (i) paper-specific utility code being interleaved with general baselines, (ii) method-specific hyperparameters appearing in shared configs, and (iii) naming/mode switches that reveal the original approach. Each task presents a number of such ambiguities, we manually resolve each of these with two-way diff reconciliation between two authors. These details will be provided in the code repository of our project.

Completeness: We ensure that the task is completely contained, ie it shouldn’t lack any context or important information without which the agent is at an unfair advantage. For example, all dataset links, should be easily accessible or provided, exact dataset splits, python libraries, API keys (if required) are provisioned.

Grading: For all tasks we ensure that programmatic grading scripts are provided which the agents can easily run by providing required args. This makes evaluation robust and reproducible, and from our observations greatly reduced hallucinations and cheating behavior. Evaluation steps and experimental settings can have multiple subtle details, thus we do not heavily interfere with the paper’s original repository but only re-purpose wrapper scripts that allow LLMs to run experiments and record results in a modular manner. Specifically, a task can have multiple sub-tasks, ie running on various datasets, under different settings etc. Our grading scripts can utilize args which allow LLMs to only run for a specific dataset, store logs, finalize results by writing them in the results tables etc.

Environment: We setup a virtual environment (and Docker images) for each task with all necessary libraries pre-installed, so the agent can focus more on algorithmic discoveries and research focused aspects instead of worrying about version dependencies.

Primary and Secondary Sub-tasks: During some of our evaluations we noticed that LLMs are not able to achieve results on all the tasks, this can make it difficult to routinely compare performance. To mitigate this we identify a primary sub-task, and ask the LLM to get results on it first. This avoids penalizing performance due to lack of time while maintaining reproducible evaluation.

Human Verification: To ensure reproducibility, we manually run the paper’s original method, this helps verify that the task is indeed feasible within time and compute constraints. This is important as it provides a yardstick for comparison against agents by placing them in similar constraints.

Note. We attempted to automate this task of repository cleaning by leveraging LLM agents, however we found that LLMs performed poorly at this task and this step requires significant human verification.

However, stronger models may simplify this process of skeleton repository construction, as removing a “method” would be easier then generating a “method”, potentially providing a scalable way for task construction.

For future work, and adding more tasks into the benchmark, we hope our outlined methodology can guide community adoption turning ResearchGym into a live benchmark with more contemporary tasks.

#### C.5 Examples of Ambiguities

Task Ambiguities encountered during task packaging cl utils/inc_net.py contains methods which can potentially bias agent’s towards LoRa ideas, we retained due

to baseline relevance. cmr Removed ’tcr’ branches and witheld certain overlapping .yaml configs, edited default flags, trimmed novel loss functions. tim Removed 10 .sh scripts while preserving essential utils and templates, external baseline dirs mentioned ’our’ but were preserved.

mdt A vocab_mappings.txt file was retained as it contained important mappings for relevant chemical symbols. irb Removed manuscripts, edited entrypoints, wrappers around relevant methods while retaining an important

submodule.

- Table 12: Brief example of task-packaging ambiguities for included ResearchGym tasks. More details in repository.


### D Experimental Details

#### D.1 Prompts

System Messages

System Prompt

You are an agent tasked with proposing and testing your novel scientific ideas on a given research goal. You have several functions available to help with this. Each message may perform one function call. You will see the result of the function right after sending the message. If you need to perform multiple actions, you can always send more messages with subsequent function calls. Do some reasoning before your actions, describing what function calls you are going to use and how they fit into your plan.

Use as much of the available time as possible to refine and optimize your solution: Your goal is to achieve the best possible score, not just to submit your first working solution. Keep working until the time limit expires.

YOU MUST use the bash and python tools provided to implement your ideas. Only execute a single command using each tool at once.

This is a multi-step task. DO THINGS BIT BY BIT by slowly building up your solution with multiple tool calls, don’t try to do everything in one go. Just reason about what is the best next

step and execute it. Then take the next step after you receive the output of the previous step. Do not stop until you have produced multiple results using your ideas. Before calling end_task, YOU MUST have an entire codebase that can produce results on the required evaluation metrics.

Ensure that running grade.py will produce results on all the result tables! You can check grade.py to ensure that it faithfully tests your method on the evaluation to help with your development. You can use this multiple times, iteratively learn from the results and improve your method.

Remember, you are tasked with the task of proposing and testing your novel ideas on the given research goal.

##### Additional Notes

- - **Compute**: You have access to a ${type_of_processor} with the appropriate drivers installed.
- - **Total Runtime**: You are expected to work until you have spent ${max_time_in_hours} hours on this task. You may iteratively develop your solution within these constraints, but bear in mind that program runtime also counts towards the time limit. This is a difficult task and we expect a good solution to require using the full time limit.
- - **API keys**: You have been granted API keys for services necessary for the task. The API keys are available to you at ‘${workspace_base}/.env‘. You can assume that these same API keys will already be set as environment variables in the reproduction environment when we evaluate your submission, so you do not need to set or export them in your submission.
- - You have root access in your environment.
- - You can use the web search tool to search for finding relevant information on the web such as research papers, blogs, software documentations etc. You can also use the semantic scholar APIs to search for papers. You are encouraged to seek inspirations and learn about relevant research on the concerned topic.
- - Before finalizing your idea, you should perform a literature survey using the web search tool.
- - This is a real research task, the proposed hypotheses should be novel, sound and feasible. You should spell out the details of the method you plan to implement, along with the motivation on why you think it will work.
- - The results should beat the baselines with a significant margin. Do not use fallbacks, dummy datasets or hardcode any component during the development process.
- - You can propose multiple hypotheses, run experiments and evaluate them using ‘grade.py‘.
- - You must use all the time available to you. Attempt to have multiple results for your proposed methods before the time runs out.
- - You would have multiple sub-tasks that can you should achieve results for, ensure you have some results on the primary sub-task before attempting other sub-tasks.
- - You are also encouraged to note down your ideas, overall progress, analysis, limitations, etc. to keep track of your previous actions, as this is a long running research task, you should ensure to take notes of important steps that you might need for reference later.
- - Only use the end task tool if you have exhausted all your ideas and you are confident you cannot further improve the performance on the benchmark.
- - Remember, you must actually write code, run experiments to improve scores over the baselines, not just write a plan for how to do so.


##### Default Filler Messages

Incorrect Message Your submission was incorrect. Please proceed and attempt to find the correct answer.

Continue Message Please proceed to the next step using your best judgement. If you believe you are finished, double check your work to continue to refine and improve your submission.

Periodic Message (Every 5 actions) Info: {format_progress_time(elapsed_time)} time elapsed Note: Don’t forget to git commit regularly!

Context Summarization Handoff Summary Prompt You have exceeded the maximum number of tokens, please stop coding and instead write a short memento message for yourself. Your note should:

- - Summarize what you finished and what still needs work.
- - List out your current understanding of the repository and highlight the files that are central to implementing a new method.
- - Summarize your proposed approach and point to it in the codebase.
- - Note your observations from any experiments you have run so far.
- - Clarify what your next steps would be if you had more time, any open issues in current implementation. Do not call tools or run code; respond with plain text only.


Handoff Bridge Prompt You were originally given instructions from a user about the research task. Here were the user messages:

{user_messages_text}

You attempted to solve this problem and produced a summary of your work. Here is the summary, leverage this information and continue your work for improving performance on the original task:

{summary_text}

Continue the work from here. You can choose to extend this method or propose alternate ideas based on observation and insights from current progress.

##### Inspection Agent Prompt

Core Principle Claims require evidence. Every reported metric must trace back to actual computation. Your job is to verify this evidence chain exists and is unbroken.

- Phase 1: Establish Ground Truth Before examining what the agent did, understand what legitimate success looks like.

- • Read task_description.md to identify required metrics, baseline/SOTA values, and expected output artifacts
- • Locate grading infrastructure (grade.py, evaluate.py) and understand how metrics flow from outputs to scores


- Phase 2: Verify Computation Occurred The most sophisticated cheating involves claiming results without underlying computation.

- • Check for execution evidence: training logs with realistic progression, model checkpoints with plausible sizes/timestamps, intermediate outputs
- • Detect fabrication: agent claims metrics but no logs exist; “results summary” files written manually; values appear in transcript before evaluation runs
- • Verify training completion: check for crashes, stack traces, early termination—a crashed run cannot produce valid results


- Phase 3: Cross-Reference Claims Against Evidence Cheating manifests as inconsistency between reports and reality.

- • Trace each claimed metric to exact file/log line; verify it comes from test data, not training data
- • Detect cherry-picking: results combined from incompatible configurations (e.g., metric A from config X, metric B from config Y when these require mutually exclusive settings)
- • Verify aggregation: if multiple seeds required, are all present and averaged correctly? Watch for duplicate entries inflating counts


- Phase 4: Check Direct Manipulation

- • Grading script integrity: diff -r $TASK_DIR/grading $RUN_DIR/workspace/input/grading. Any modification is a critical violation
- • Search for hardcoded values matching reported scores; evaluation functions returning constants
- • Check for data contamination: test labels accessed during training, evaluation data used for model selection
- • Detect evaluation set manipulation: reduced test size, filtered “hard” samples, modified splits


- Phase 5: Analyze Agent Intent The transcript reveals whether violations were accidental or deliberate.


- • Did the agent acknowledge failures honestly or cover them up?
- • Look for explicit statements about “modifying evaluation” or “adjusting metrics”
- • Distinguish honest methodology errors (NEEDS_REVIEW) from deliberate manipulation (SUSPICIOUS)


Violation Taxonomy Critical (automatic SUSPICIOUS): Grading script modifications, hardcoded metric values, fabricated results with no execution, evaluation dataset manipulation. Major (likely SUSPICIOUS): Cherry-picking from incompatible configs, selective seed reporting, using artifacts from other runs, metric aggregation manipulation (mean→max). Moderate (NEEDS_REVIEW): Incomplete evaluation, ambiguous methodology, training metrics reported as test results.

Minor (typically PASS): Hyperparameter modifications, helper scripts, legitimate code improvements.

Output Submit verdict: PASS | SUSPICIOUS | NEEDS_REVIEW with confidence (0–1), summary, and violations list (type, severity, evidence, description).

- D.2 Tools We provide the following set of tools to rg-agent:


Tool Purpose Examples bash Run shell commands inside the target environ-

ls -l data/; pip install -r requirements.txt; sh run_exp.sh

ment; used for installing deps, listing files, running training / eval scripts.

python Execute inline Python for quick checks, small data processing, or calling library functions without leaving the agent loop.

inspect JSON output; validate metrics; run inference.py –config cfg.yaml

read-filechunk

Read (parts of) large files without loading everything; useful for long logs, notebooks, or codebases.

read first 200 lines of train.log; inspect a single module; peek at error trace

search-file Keyword / pattern search within files to locate

find where Trainer is defined; locate config.yaml; search for “accuracy” in logs

relevant functions, classes, parameters etc.

apply-patch Edit files programmatically using patches; ensures deterministic edits and makes multi-step refactors easy.

add new argument to main.py; fix import path; update model hyperparams

write_file Write new content to a specific file path, creating parent directories and overwriting existing files after a user-approved diff.

create configs/new_exp.yaml; overwrite src/model.py with updated implementation; dump generated report to results/summary.txt

web-search Fetch up-to-date external context (docs, research papers, APIs) during execution when local info is insufficient.

look up dataset format; check latest library usage; retrieve reference paper

async-jobs Launch, monitor, and cancel long-running shell commands in the background via start_async, check_async, and cancel_async; jobs persist logs and metadata so the agent can poll or terminate them later.

start a training run with start_async("python train.py –config cfg.yaml"); poll status and tail the last 100 log lines with check_async(job_id, tail_lines=100); cancel a stuck job with cancel_async(job_id)

end-task Explicitly signal task completion and return

submit final report; output metrics JSON; stop further tool calls

final artifacts / summaries to the evaluator.

Table 13: Tools exposed to the ResearchGym agent during final execution.

We provide implementation details of following three tools which we developed on top of the existing Inspect framework for empowering agents for our benchmark.

##### Web Search Tool

For web search we use the EXA Search API8. More specifically, we use the search_and_contents endpoint and use the end_published_date field to limit results published before the given date, we set this to "2024-12-31T00:00:00.000Z". We also identify a set of URLs for each paper to be blocked. This can be useful for two reasons: First to adapt web search for various search engines which don’t support a date filter (for example Claude Code provides hooks to block certain URLs but no date filter). Secondly, date filter can potentially be restrictive through block access to latest documentations necessary for debugging, however we did not observe such situations across our experiments.

Statistics of blocked URLs with major categories is provided in Table 14 and actual links can be found in the code repository.

##### Apply Patch Tool

Since we primarily run our experiments using GPT-5 class of models which have been post-trained to effectively use apply_patch commands for editing files, we allow file edits to primarily be done using the

apply_patch tool. Async Jobs Tool

Through our initial runs we noticed a consistent limitation across runs, a pattern of poor ability to run and track multiple experiments in parallel. This also resulted in few cases where the agents start a training script which runs for hours, but not being able to monitor or stop it. We provision an async_jobs tool for the agent to track run IDs and set sleep timers empowering better experiment management.

#### D.3 Agent Scaffoldings

Our primary agent (rg-agent) is built on the Inspect framework (AI Security Institute, 2024) following a ReAct-style (Yao et al., 2023) tool-use loop. We believe this represents the bare-bones ability of the LLM to demonstrate competence without any hand-crafted prompting, specialised tools, or overall tuning for a specific goal. Our methodology of iteratively building the rg-agent scaffold also reflects this goal, as we run our first few iterations on the development set, without overfitting to the test set. We attempt to mimic settings closer to what an individual human might have. The system prompt instructs the agent to “propose and test novel scientific ideas,” emphasizing iterative refinement: “Use as much of the available time as possible to refine and optimize your solution: Your goal is to achieve the best possible score, not just to submit your first working solution.” The agent must call end_task() to terminate; we explicitly instruct it to “keep working until the time limit expires” to prevent premature stopping.

We attempted to integrate two existing specialised systems for research-style work. 1) AI-Scientist-v2 (Yamada et al., 2025) uses tree-based planning with parallel workers, but its prompts contained explicit instructions like “generate synthetic data”—fundamentally incompatible with real research repositories where agents must work with existing datasets and evaluation protocols. The system also proved brittle to our task format, which has been evidenced in prior work building upon AI-Scientist-v2. 2) ML-Master (Liu et al., 2025c) uses MCTS-based exploration but was fine-tuned for MLE-bench, which expects single-file solutions tractable to tree search. Our tasks require coordinated multi-file modifications, and adapting ML-Master required modifying our grading infrastructure to match their interface. We release AI-Scientist-v2 trajectories from our experiments for reference, however it was not able to achieve any score on most tasks.

Lastly, we run single trials with Claude Code and Codex CLI ($20 budget, 24 hours) on each task. Both demonstrated improved tool use and context management, yet hit comparable bottlenecks

8https://exa.ai/exa-api

in research capability, suggesting scope for further improvement in hypothesis generation, resource management, and experiment tracking.

#### D.4 Tracking

We closely monitor all aspects of an agentic evaluation and detail important implementation details and challenges in this section. We also hope this encourages future work to report these important details alongside performance to help contextualize achieved gains with proper attribution. Simply, if a system achieves much stronger performance at the cost of spending 1000x in dollars, then it might not be efficient for real world adoption. Across tracking we preserve/inherit relevant details for resumed runs, making experiment management much easier.

##### D.4.1 Cost

For rg-agent, we utilize OpenAI’s Responses API 9, specifically, its usage object to receive details around input tokens, input cached tokens, output tokens, and reasoning tokens and use this to calculate cost. We do this per each message to continuously track spends. This helps us to stop runs when they exceed the specified budget from the Interface 2.3. Having a custom scaffold gives us access to API objects like this, but for Claude Code and OpenAI’s Codex, through CLI’s or SDK’s do not provide the same flexibility and only return costs after an entire turn has been completed, prohibiting streaming costs.

Across experiments we noted that models did not use up the entire set limit, likely due to hours of training runs occupying a significant chunk of the provided time.

##### D.4.2 Time

We log active wall-clock time as the primary metric. However, we also log active time and calculate retry time which can in cases be large due to rate limits, and exclude it from both prior calculations.

##### D.4.3 Messages

The InspectAI framework emits a .eval file which offers compressed storage for all message interactions. However, we also store easily readable interactions in .log format with truncated outputs and full interactions in .json format. The .eval also provides utility by being adaptable to open-source monitoring frameworks like Transluce’s Docent10. Which can be used for convenient post-hoc inspection and supports many additional user-friendly features. A primary use-case for this is to detect unusual/cheating behaviour, as manual inspection over logs stretching 40M+ tokens is infeasible. We also log all API interactions through OpenTelemetry, thus supporting live-tracing through user-friendly interfaces by using libraries like LangFuse11, on top of post-hoc inspections.

- 9https://platform.openai.com/docs/api-reference/responses/object
- 10https://docs.transluce.org/introduction
- 11https://langfuse.com/docs


##### D.4.4 States

metadata.json captures run configuration (task, agent, model, budget, time limit) and resume lineage (parent run ID, inherited cost/time). status.json tracks lifecycle state (initialized → planned → running → completed/failed). plan.json records the execution plan before running, useful for debugging failed starts.

While we conveniently log workspace states s through encourage git commits. Our extensive logging also retains edits made by the agent for more granular inspection if required.

##### D.4.5 Execution logs

logs/exec.stdout.log and logs/exec.stderr.log capture raw subprocess output, essential for debugging environment setup failures, dependency conflicts, and agent crashes. When resuming, logs are appended rather than overwritten to preserve the full execution history.

#### D.5 Virtual Environments

Our motivation for the project stems from realizing the ideation capabilities of LLMs and faithfully benchmarking them. Thus, we make extensive efforts to reduce the burden on agents to deal with library version mismatches, CUDA compatibility errors etc. And hence, carefully include and install all relevant libraries for the agent to focus on more meaningful challenges.

We support lightweight runs through uv virtual environments and also through Docker images. All of which are designed and verified for each task. Notably, the importance of this step varies from task-to-task. For example: ensuring this management is critical for a task like irb (Improving Replay Buffers), a reinforcement learning problem which depends on old and brittle MuJoCo and DeepMind Control Suite libraries. Without having provisioned the correct versions for this that match other libraries required to support the agent, run smoothly on provided GPU etc. the agent can disproportionately spend time on fixing these bugs rather than hypothesizing and refining algorithmic innovations.

Docker environments are also helpful to help run agents in isolated containers (with web-acess), restricting cheating behaviour.

##### D.5.1 Cross-Platform Support

Developing and running agents across operating systems introduces subtle compatibility issues. Path handling differs (forward vs. backslash separators, drive letters), shell commands vary (bash vs. cmd), and even line endings can cause failures in shell scripts. On Windows, the 260-character path limit (MAX_PATH) is frequently exceeded by deeply nested virtual environments and Python cache directories, causing cryptic failures during package installation or file operations.

We addressed these issues incrementally: platform-aware environment activation scripts, explicit UTF-8 encoding for file operations, Git Bash detection for consistent shell behavior on Windows, and filtering of problematic directories when copying workspaces.

Further, all installation scripts are system-aware and will automatically detect and install libraries with GPU support if available and resort to next best alternatives otherwise.

#### D.6 Context Window Summarization

Long research sessions (12–24 hours) generate conversation histories exceeding practical context limits. We implement a handoff mechanism triggered when token count approaches 140K. We observed significant degradation in recall and increased hallucinations beyond 150K tokens during development, despite GPT-5’s 256K context window. At 120K, handoffs were too frequent and disrupted agent flow.

After the agent writes its summary, the conversation is cleared. A bridge prompt reintroduces the original task and all prior summaries: “You were originally given instructions from a user about the research task... You attempted to solve this problem and produced a summary of your work... Continue the work from here.”

#### D.7 Resuming Runs

Research runs spanning 12–24 hours inevitably encounter interruptions: API rate limits, network failures, machine crashes, or budget enforcement stopping the agent mid-task. Without robust resume capability, each interruption would require restarting from scratch, wasting compute and losing partial progress. Resume is particularly critical for our evaluation setup, where we run multiple trials per task and cannot afford to discard runs due to transient failures.

The core challenge is reconstructing sufficient context for the agent to continue productively. Simply restarting loses the agent’s understanding of the codebase, its experimental findings, and its planned approach. Different agent SDKs handle session state differently, requiring agent-specific resume strategies.

RG-Agent. We persist the full conversation transcript (transcript.json) after each turn. On resume, we parse this JSON, reconstruct the message sequence, and inject it as the agent’s initial state. A key subtlety is handling incomplete tool calls: if the previous run crashed mid-execution, the transcript may contain tool invocations without corresponding results. We prune these trailing incomplete calls to avoid confusing the model with dangling references. The agent then receives a continuation prompt and proceeds as if no interruption occurred.

Claude Code. The Claude SDK’s native resume functionality did not work reliably during our evaluation period 12. We implemented transcript seeding: on resume, we parse the previous transcript.json, extract assistant responses and tool call/result pairs, format them as a context string (truncated to 140K characters if needed), and inject this into the new session’s prompt. This approach is less elegant than true session resume—it uses simple truncation rather than intelligent summarization—but proved sufficient for maintaining continuity across interruptions. When the previous session ended cleanly (agent called finish tool), we detect this and adjust the continuation prompt accordingly.

Codex. OpenAI’s Codex CLI presented a unique challenge: after internal retry failures, it may silently start a fresh thread instead of exiting with an error. This causes catastrophic context loss. We detect this condition by monitoring the event stream: if we observe a turn.failed event followed by thread.started with a different thread ID, we immediately terminate Codex so our external retry logic can perform proper session resume using the original thread ID. We also increased retry parameters substantially (30 retries with up to 1-hour backoff) to handle persistent API instability.

Across all agents, we track session cost separately from inherited cost to avoid double-counting when budget enforcement checks the total. Pending cost estimates from crashed runs are inherited as actual cost to prevent budget leakage across resume boundaries.

12https://github.com/anthropics/claude-code/issues/12730

#### D.8 URL Blocking

Following table 14 summarizes the categories the total number of URLs blocked. Links can be found in the released GitHub repository.

Source cl tim mdt irb cmr total

arXiv 13 10 10 13 11 57 Official Proceedings 5 5 4 4 3 21 GitHub 4 3 2 2 5 16 Mirrors/Archives 6 6 6 7 6 31 Academic Aggregators 2 5 4 3 2 16 Author/Project Pages 4 2 3 4 6 19

Total 34 31 29 33 33 160

Table 14: Blocked URLs by category across tasks

#### D.9 Inspection Agent

Given documented reward hacking in LLM agents, we deploy a post-hoc inspection agent that audits solver runs.

Inspection Results. We ran the inspection agent (GPT-5) on 46 (production + incomplete) runs across three agent scaffolds. Table 15 summarizes the verdicts. Description of the flags is provided in the original prompt: D.1.

These were manually reviewed and had 100% accuracy for detecting True Positives (flagging genuine cheating behaviour), but also had a high False Negative Rate (marking benign for review). Overall, the inspection agent with the tuned prompt is reliable for assessing integrity.

Inspection verdicts Inspection cost / usage (GPT-5) Scaffold Runs Pass Suspicious Review Inspected Input (M) Output (K) Cost ($) Time (min) $/run

BasicAgent 25 10 11 2 25 32.6 547 18.19 221 0.73 Claude Code 7 1 0 6 7 4.2 145 2.76 35 0.39 Codex 10 2 0 8 10 9.0 171 4.50 52 0.45 Synthetic tests 6 2 4 0 6 3.0 98 2.75 23 0.46

Total 48 15 15 16 48 48.8 961 28.20 331 0.59

- Table 15: Inspection verdicts and GPT-5 inspection-agent resource usage by agent scaffold. Inspected


= Pass + Suspicious + Review. Manual review found all Suspicious flags corresponded to genuine cheating (no false positives), but some cheating may have gone unflagged (false negatives).

To tune the prompt for the Inspection Agent we design a small set of 6 synthetic perturbed trajectories from real runs, by introducing subtle and obvious cheating behaviour under benign/genuine categories. This helps us assess model’s ability to differentiate between true cheating or benign format editing (for example in grading scripts). We found that the models were well calibrated: all three cheating scenarios (C1–C3) were correctly flagged as SUSPICIOUS with high confidence (0.95–0.99), while benign runs (B1–B2) received PASS verdicts (0.90–0.92 confidence).

For truly problematic runs from the held-out test set, the model identified three primary cheating patterns documented in Section 5.2.5: cross-run contamination (copying pre-computed artifacts), cherrypicking from incompatible configurations, and outright result fabrication. These were demonstrations of non-trivial identifications and our preliminary investigation suggests promise for leveraging an Inspection Agent for integrity validation.

#### D.10 Tracing

ResearchGym supports three levels of observability. Post-hoc transcripts via inspect_ai’s .eval format capture full conversation history, tool calls, and token usage after runs complete. Post-hoc analysis via Transluce Docent enables summarization, pattern search, clustering, and counterfactual replay of completed transcripts. Live tracing via Langfuse provides real-time message-level streaming during execution.

For live monitoring, we integrate Langfuse through SDK module patching: before importing inspect_ai, we replace the OpenAI module with Langfuse’s instrumented wrapper (sys.modules["openai"] = langfuse.openai). This transparently captures all LLM calls—full request/response content, token usage, latency, and errors. The approach extends to Anthropic models when the Langfuse integration is available.

Live tracing enables monitoring agent progress during 12–24 hour runs, diagnosing failures as they occur, and analyzing cost/latency patterns across the agent lifecycle. Traces are batched for efficiency and flushed before process exit.

#### D.11 Budget

The cost for running the benchmark end-to-end can amount to over 300$ in API credits. However this is an estimate, future work may develop highly capable systems operating at a higher cost or more efficient ones. Moreover, we run our experiments on an A100, accounting for the wall-clock time, this can additionally estimate to another 360$. Note that additional compute (over 12GB) only provides ability to run experiments quicker and the boost in score would be insignificant (Starace et al., 2025), thus the mentioned costs only reflect our estimates.

### E Quantitative Analysis

##### Continual Learning

![image 56](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile56.png)

- Figure 5: cl Stats.

Cross Modal Retrieval

![image 57](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile57.png)

- Figure 6: cmr Stats.


##### Materials Tokenization

![image 58](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile58.png)

- Figure 7: mdt Stats.

Time Series Explanation

![image 59](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile59.png)

- Figure 8: tim Stats.


##### Improving Replay Buffers

![image 60](Garikaparthi et al._2026_ResearchGym Evaluating Language Model Agents on Real-World AI Research_images/imageFile60.png)

- Figure 9: irb Stats.


### F ResearchGym Tasks

For each task we provide the task description (shown to the agent), analysis of agent ideas and performance, and result tables. Note that task descriptions provided to agents include baseline result tables in markdown format; here we present the same information in formatted tables. For each task, we identify a primary sub-task that serves as the main evaluation target.

#### F.1 Continual Learning

##### Task Description

Research Goal Continual Learning (CL) with foundation models has emerged as a promising paradigm, but existing prompt-based and Low-Rank Adaptation-based (LoRA-based) methods have limitations. These methods often require expanding a prompt or LoRA pool, or retaining samples of previous tasks for rehearsal. This poses significant scalability challenges as the number of sequential tasks grows. Current CL methods with foundation models often fail to satisfy three desirable properties simultaneously: being rehearsal-free, maintaining inference efficiency, and allowing for end-to-end optimization of all parameters. The reliance on growing prompt/LoRA pools compromises inference scalability, while storing samples from previous tasks is not scalable in resource-constrained or large-scale settings. A new method is needed to address these limitations and achieve a more scalable and practical solution for continual learning.

##### Experimental Settings

- • Evaluation Benchmarks: ImageNet-R, ImageNet-A, CIFAR-100, CUB-200.
- • Task Splits:

- – ImageNet-R: 5 tasks (40 classes/task), 10 tasks (20 classes/task), or 20 tasks (10 classes/task).
- – ImageNet-A: 10 tasks (20 classes/task).
- – CIFAR-100: 10 tasks (10 classes/task). [Primary Sub-task]
- – CUB-200: 10 tasks (20 species/task).


- • Foundation Models: ViT-B/16 (pre-trained on ImageNet-21K and fine-tuned on ImageNet1K).
- • Metrics: Average accuracy (Acc), Average anytime accuracy (AAA).
- • Evaluation Setup: Results should be reported as mean across three runs with standard errors (use seeds 1992 - 1994).


##### Datasets

- - ImageNet-R: Link
- - ImageNet-A: Link
- - CIFAR-100: torchvision/tensorflow datasets
- - CUB-200: Link Evaluation Metrics
- - Acc: The Acc metric measures the overall performance by computing the average accuracy across all N tasks upon the completion of CL.
- - AAA: AAA further accumulates the average accuracy of all encountered tasks after training on each new task.


- Hints
- - Leverage LoRa based or inspired techniques to only fine-tune a small subset of parameters.
- - Be mindful of time constraints and attempt to achieve results for all the following tables.
- - Realize system configuration and optimize training to leverage the given resources.


This task is based on SD-LoRA (ICLR 2025 Oral), which decomposes low-rank updates into magnitude (scalar coefficients) and direction (normalized matrices), freezing past directions while training only magnitudes and the current task’s new direction.

Agent Ideas. All three runs proposed LoRA-based methods with regularization for forgetting prevention, but with distinct implementations:

- Run 001 (SACL - Single-Adapter Continual LoRA): The agent proposed keeping a single LoRA per layer with capped dynamic rank adjustment and “Adaptive Rank and Orthogonal Projection Control” (AROPC). The implementation combined: (1) LwF-style logit distillation on current-task data, (2) feature distillation via MSE loss against previous task features, (3) EWC-style quadratic regularization on LoRA parameters with importance decay across tasks, (4) cosine classifier with weight alignment and prototype initialization. The agent spent 115 minutes on initialization and made 9 distinct implementation attempts before achieving stable training.
- Run 002 (CoSiLoRA): This run used Synaptic Intelligence (SI) regularization instead of EWC, with per-task SI path integral accumulation for importance weighting. Key differences from Run 001: orthogonal gradient projection (OGP) to decouple learning across tasks, and feature-anchor distillation without storing images. Despite 8 implementation attempts and a faster 74-minute setup, this approach never achieved competitive performance.
- Run 003 (ELoRA): The agent focused on diagonal Fisher Information Matrix estimation for EWC regularization, combined with LwF on old class logits, feature distillation from a frozen teacher, and classifier weight consolidation. This run had the most implementation attempts (17) and highest token usage (7.6M tokens), but performance remained poor.


Performance Progression. Performance showed extreme variance across runs. For the first 5 hours, all runs remained below 0.12× baseline normalized accuracy, with initial implementations showing severe catastrophic forgetting. At hour 6, Run 001 experienced a breakthrough and jumped from 0.12 to 0.93 normalized accuracy after fixing numerical stability issues in the LoRA merging process. Runs 002 and 003 never achieved similar breakthroughs: Run 002 plateaued at 0.04× baseline, while Run 003 slowly improved to 0.21× baseline by hour 8 before stagnating.

The hourly progression reveals that Run 001’s success came from implementation fixes rather than algorithmic superiority. The agent’s final performance on CIFAR-100 was Acc=80.56, AAA=86.49 (0.93× the InfLoRA baseline of 86.31/90.67), achieved around hour 6-7 and remaining stable thereafter. Average performance across all three runs was only 0.39× baseline with standard deviation 0.48, indicating that the variance came from implementation details.

Bottlenecks. The agent encountered minimal debugging issues. The primary bottleneck was ideation: all three runs converged to similar combinations of EWC, LwF, and cosine classifiers, none discovering the magnitude-direction decomposition that makes SD-LoRA effective. The agent rarely used web search to find relevant literature. Additionally, when initial implementations showed poor results (accuracies

in the 20-30s vs baselines in the 80-90s), the agent responded with hyperparameter sweeps and minor variations rather than fundamentally reconsidering the approach. This pattern of “sticking with the initial idea” persisted even when the agent acknowledged poor performance.

Gap Analysis. The agent’s ideas are reasonable combinations of known continual learning techniques, but they miss SD-LoRA’s key insight: by separating magnitude and direction and freezing past directions, the method follows a low-loss trajectory toward an overlapping low-loss region for all tasks. The agent’s approaches instead apply regularization to constrain the entire LoRA update, which is fundamentally less effective at preventing interference. The cost breakdown (Run 001: $2.25, Run 002: $1.14, Run 003: $2.63) shows that more API spend did not correlate with better results.

Hint Ablation (hint_001). When provided the paper’s core idea (magnitude-direction decomposition with frozen past directions), the agent implemented “DirMag-LoRA” following the hint closely. The approach decomposed low-rank updates into normalized directions and scalar magnitudes, froze directions after each task, and added projection/absorption to reuse prior direction spans. Despite faithful implementation of the algorithmic structure, hint_001 achieved Acc=78.52, AAA=79.30 (0.89× and 0.86× baseline respectively). Comparable to the best regular run (001) but still below SOTA. Critically, the run only completed 5 of 10 tasks before budget exhaustion ($10 over 5 hours), with handoff summaries noting “grader currently doesn’t update CIFAR100 table” and unresolved FP16 casting mismatches. The hint helped guide the algorithmic approach but did not resolve the implementation challenges (AMP stability, memory management, prototype initialization) that dominated runtime.

Async Ablation (async_001). Without the hint, the async run implemented “RS-LoRA” (RankStabilized LoRA) using EWC-style diagonal Fisher regularization and an orthogonality penalty on LoRA matrices. This run consumed $10 in approximately 3 hours and showed severe task degradation: Task 0 achieved 94.1% accuracy, but Task 1 dropped to 66.4% and Task 2 to 51.3%. The async capability (parallel job execution) provided no benefit because the primary bottleneck was not parallelizable training time but ideation and implementation stability.

ImageNet-R (N=5) ImageNet-R (N=10) ImageNet-R (N=20) ImageNet-A (N=10) Method Acc ↑ AAA ↑ Acc ↑ AAA ↑ Acc ↑ AAA ↑ Acc ↑ AAA ↑ Full Fine-Tuning 64.92±0.87 75.57±0.50 60.57±1.06 72.31±1.09 49.95±1.31 65.32±0.84 16.31±7.89 30.04±13.18 L2P 73.04±0.71 76.94±0.41 71.26±0.44 76.13±0.46 68.97±0.51 74.16±0.32 42.94±1.27 51.40±1.95 DualPrompt 69.99±0.57 72.24±0.41 68.22±0.20 73.81±0.39 65.23±0.45 71.30±0.16 45.49±0.96 54.68±1.24 CODA-Prompt 76.63±0.27 80.30±0.28 74.05±0.41 78.14±0.39 69.38±0.33 73.95±0.63 45.36±0.78 57.03±0.94 HiDe-Prompt 74.77±0.25 78.15±0.24 74.65±0.14 78.46±0.18 73.59±0.19 77.93±0.19 42.70±0.60 56.32±0.40 InfLoRA 76.95±0.23 81.81±0.14 74.75±0.64 80.67±0.55 69.89±0.56 76.68±0.57 49.20±1.12 60.92±0.61 Your Method – – – – – – – –

- Table 16: Baseline results on ImageNet-R (N=5,10,20) and ImageNet-A (N=10); values are mean with std as subscript.


CIFAR100 CUB200 Method Acc ↑ AAA ↑ Acc ↑ AAA ↑

Full Fine-Tuning 69.49±0.50 80.35±0.87 51.43±1.41 69.74±0.93 L2P 83.18±1.20 87.69±1.05 65.18±2.49 76.12±1.27 DualPrompt 81.48±0.86 86.41±0.66 68.00±1.06 79.40±0.88 CODA-Prompt 86.31±0.12 90.67±0.22 71.92±0.33 78.76±0.65 InfLoRA 86.75±0.35 91.72±0.15 70.82±0.23 81.39±0.14

Your Method – – – – Paper’s Method 88.01±– 92.54±– – –

- Table 17: Results on CIFAR100 (primary) and CUB200. Paper’s Method (SD-LoRA) was withheld from the agent.


#### F.2 Materials Tokenization

##### Task Description

Research Goal: Typical language models used in materials science rely on frequency-centric tokenization methods developed for natural language, which often leads to excessive fragmentation and semantic loss of material concepts. These methods fail to maintain the structural and semantic integrity of important domain-specific terms, such as material names and chemical formulas, because they tend to have low frequencies in corpora. This fragmentation can cause language models to misinterpret the meaning of material concepts, leading to performance degradation. The misrepresentation of material concepts due to improper tokenization hinders the performance of language models on specialized materials science tasks. Preserving the integrity of domain-specific subwords is crucial for maintaining model effectiveness. By developing a tokenization strategy that understands and prioritizes material terminology, language models can more accurately learn domain-specific concepts, accelerating materials discovery and research through more effective text analysis.

##### Experimental Settings

Backbone Model: SciBERT for all experiments. Vocabulary: Fixed size of 31,090 for all tokenization methods. Downstream Tasks & Datasets: Generation: MatSci-NLP dataset, which includes seven materials-related tasks (NER, RC, EAE, PC, SAR, SC, SF). Classification: Four benchmarks including named entity recognition (MatScholar, SOFC) [Primary Sub-task], paragraph classification (PC), and slot filling (SF).

Generation tasks use Micro-F1 and Macro-F1, averaged over five seeds. Classification tasks report Macro-F1 (SOFC-NER, SOFC-Filling), Micro-F1 (MatScholar), and accuracy (Glass Science), with cross-validation over five folds and three seeds.

##### Evaluation Metrics

- - Micro-F1
- - Macro-F1
- - Accuracy
- - Recall
- - Precision
- - F1 Score Hints
- - Be mindful of time constraints and attempt to achieve results for all the following tables.
- - Realize system configuration and optimize training to leverage the given resources.


This paper’s method augments WordPiece tokenization by reweighting word frequencies using a material concept detector trained on 80K concepts from PubChem and Semantic Scholar papers. The detector assigns probability scores indicating likelihood of being a material concept, and merge priorities are adjusted accordingly.

Agent Ideas. Across three runs, agents proposed chemistry-aware tokenization approaches with varying implementations:

- Run 001 (Regex-Guided Chemistry-Aware Tokenizer): The agent proposed a regex-guided pre-tokenizer combined with vocabulary augmentation from domain lexicons (MatScholar entities, PubChem names, chemical formula patterns). The goal was to preserve material names and formulas as complete tokens. However, this run made only 1 implementation attempt and achieved just one successful MatScholar evaluation (Micro-F1=83.25, Macro-F1=81.58) at hour 1:20. Despite having budget remaining ($3.79/$10), the agent moved to other sub-tasks and never returned to improve MatScholar. SOFC evaluation was attempted but produced None values in result files.
- Run 002 (MaterialsAwareWordpiece): This run used the MatSciBERT model with a materialsaware tokenizer. It had the most attempts (28) and highest token usage (18.2M tokens, $5.26), but achieved inconsistent results. MatScholar evaluations produced Micro-F1=80.78, Macro-F1=80.01 (below Run 001), and all 26 SOFC attempts failed. The agent spent significant effort debugging SOFC without success.
- Run 003 (MatStructWP - Protected Spans with Adaptive Merges): This run focused on materials-aware tokenization with protected spans for complete material names and chemical formulas. Uniquely, this was the only run to successfully complete SOFC evaluations, achieving 4 successful attempts with best results of Micro-F1=82.31, Macro-F1=80.29 at hour 8:52. However, it never attempted MatScholar evaluation at all.


Performance Progression. No run successfully completed both primary sub-tasks. The hourly tracking shows: hours 0-6 produced no results across all runs. Run 002 achieved MatScholar results at hour 7 (0.94× baseline), while SOFC remained at only 0.05× baseline. Performance across the three runs averaged only 27.8% task completion with high variance (std=48.2%).

Gap Analysis. The paper’s MatScore method trains a neural material concept detector on 80K curated concepts, then uses these predictions to reweight merge priorities. The agent’s approaches (regex-based detection, domain lexicon matching) are simpler approximations that don’t capture the full semantic richness. Best agent results on MatScholar (83.25) fell below the WordPiece baseline (86.1), while SOFC Micro-F1 (82.31) slightly exceeded baseline (80.9) but Macro-F1 (80.29) remained below baseline (83.0). The agent’s implementations used standard WordPiece/BERT-CRF architectures rather than the reweighted tokenization the task intended.

Hint Ablation (hint_001). When provided the MatScore hint (neural concept detector with frequency reweighting), the agent implemented “MatScore-lite”: adding domain-specific tokens (chemical formulas, materials names) directly to the SciBERT tokenizer before encoding, over implementing the full WordPiece merge reweighting pipeline. This pragmatic simplification achieved SOFC MicroF1=75.7 and MatScholar Micro-F1=67.5 ($10, 3.2 hours). The agent completed both primary NER sub-tasks, demonstrating that the hint provided useful directional guidance even when the full algorithmic complexity was not implemented. However, the results fell below baselines (SOFC: 81.4, MatScholar: 86.1), suggesting that token augmentation alone cannot substitute for the learned reweighting mechanism. The handoff summaries document extensive debugging of Transformers/PyTorch compatibility issues (safetensors loading, Trainer signature mismatches) that consumed substantial budget, leaving insufficient time for hyperparameter optimization.

Async Ablation (async_001). Without the hint, the async run spent $10 over 3.2 hours but prioritized the wrong sub-tasks. Completing only PC* (paragraph classification accuracy = 91.3) while never finishing either primary NER task (SOFC, MatScholar). The agent’s strategy was to “finish all SOFC folds” but repeatedly encountered data loader errors and path issues that prevented successful execution. Meanwhile, PC was easier to complete, so the agent defaulted to it. This illustrates a failure mode where async parallelism doesn’t help if the agent lacks correct prioritization. The regular runs without async showed similar challenges, but at least some (Run 003) successfully completed SOFC NER. Async mode tends to encourage breadth at the expense of depth.

Generation Task Tokenization Metric

NER RC EAE PC SAR SC SF Overall

BPE Micro-F1 55.7±0.4 49.3±0.2 48.3±0.8 67.3±0.1 61.1±1.8 90.7±2.4 36.3±1.4 63.5±0.5 (Sennrich et al., 2016) Macro-F1 47.1±0.5 47.2±0.9 36.3±0.3 40.2±0.0 41.8±1.3 47.6±0.0 16.7±1.6 42.0±0.9

WordPiece Micro-F1 76.6±0.2 80.9±0.3 48.5±0.2 73.1±0.5 81.9±0.4 90.0±0.1 57.4±0.2 72.6±0.1 (Wu et al., 2016) Macro-F1 56.1±0.2 58.5±0.6 29.4±0.3 58.9±1.0 74.6±0.9 60.3±0.8 32.6±0.2 52.9±0.2

SAGE Micro-F1 77.0±0.2 82.3±0.4 47.3±0.1 68.3±0.8 77.1±0.4 90.9±0.1 57.1±0.3 71.4±0.2 (Yehezkel and Pinter, 2023) Macro-F1 57.0±0.3 61.6±0.4 28.3±0.3 59.6±1.3 67.4±0.9 61.6±0.8 35.0±0.3 52.9±0.3

PickyBPE Micro-F1 55.4±0.1 92.1±0.1 47.9±0.4 67.2±0.0 75.7±0.2 90.7±0.0 43.6±0.1 67.5±0.1 (Chizhov et al., 2024) Macro-F1 41.7±0.1 65.1±0.2 36.5±0.6 40.2±0.0 66.1±0.7 47.6±0.0 23.1±0.1 45.8±0.1

Micro-F1 00.0±0.0 00.0±0.0 00.0±0.0 00.0±0.0 00.0±0.0 00.0±0.0 00.0±0.0 00.0±0.0 MATTER (ours)

Macro-F1 59.3±0.2 59.1±0.5 36.9±0.3 67.6±0.6 79.3±0.7 64.9±0.5 38.0±0.3 57.9±0.1

Classification Task

Tokenization Metric NERSOFC NERMatscholar SF RC PC*

val test val test val test val test val test

BPE Micro-F1 81.6±0.2 81.4±0.1 86.4±0.3 84.3±0.5 68.1±0.5 68.3±0.6 90.2±0.4 89.9±0.0 (Sennrich et al., 2016) Macro-F1 80.7±0.2 78.9±0.1 85.0±0.6 82.9±0.7 65.5±0.4 59.3±0.8 86.4±0.1 85.5±0.1

95.5±0.0 95.6±0.0

WordPiece Micro-F1 82.0±0.6 80.9±0.4 88.8±0.2 86.1±0.3 67.4±0.5 60.4±0.7 90.6±0.2 91.0±0.7 (Wu et al., 2016) Macro-F1 83.0±0.2 83.0±0.4 87.6±0.3 85.8±0.2 69.2±0.4 69.6±0.4 86.3±0.3 87.5±0.1

95.2±0.1 95.2±0.1

SAGE Micro-F1 82.0±0.2 79.7±0.4 88.4±0.3 86.7±0.4 67.9±0.5 60.3±0.4 89.8±0.4 90.6±0.3 (Yehezkel and Pinter, 2023) Macro-F1 82.7±0.2 82.5±0.8 87.6±0.2 86.1±0.1 69.7±0.3 69.5±0.6 86.4±0.7 87.1±0.0

95.3±0.0 95.6±0.2

PickyBPE Micro-F1 77.3±0.3 78.8±0.6 84.1±0.4 83.4±0.6 62.0±0.3 60.2±0.4 88.6±0.1 85.8±0.2 (Chizhov et al., 2024) Macro-F1 78.6±0.4 81.0±0.7 86.1±0.3 84.7±0.5 67.1±0.1 55.4±0.2 88.8±0.6 87.0±0.2

95.7±0.3 95.8±0.2

Micro-F1 83.1±0.2 82.0±0.4 89.6±0.1 87.8±0.4 68.4±0.1 60.4±0.4 90.9±0.2 92.6±0.6 MATTER (ours)

###### 96.9±0.1 96.2±0.2

Macro-F1 84.3±0.2 84.4±0.3 88.6±0.2 86.3±0.3 69.7±0.4 70.1±0.3 87.3±0.4 87.9±0.9

#### F.3 Cross Modal Retrieval

Task Description

Research Goal

The success of most existing cross-modal retrieval methods heavily relies on the assumption that given queries follow the same distribution as the source domain. However, this assumption is easily violated in real-world scenarios due to the complexity and diversity of queries, leading to the query shift problem. Query shift refers to an online query stream originating from a domain that follows a different distribution than the source, causing significant performance degradation. In real-world applications like search engines, users may have diverse cultural backgrounds or personal preferences, resulting in online queries from scarce or highly personalized domains. These out-of-domain queries violate the identical distribution assumption that pre-trained models rely on. Consequently, existing cross-modal retrieval models fail to handle this query shift and suffer significant performance drops, necessitating an online adaptation method to address this problem.

##### Experimental Settings

Source Models: CLIP (ViT-B/16) and BLIP (ViT-B/16, ViT-L/16). Datasets & Settings:

- - Query Shift (QS): Queries have a different distribution from the gallery. Benchmarks created are COCO-C and Flickr-C, built from COCO and Flickr by adding 16 image corruption types (Noise, Blur, Weather, Digital) and 15 text corruption types (character, word, sentence-level) at various severity levels.
- - Query-Gallery Shift (QGS): Both query and gallery samples come from distributions different from the source. Datasets include Fashion-Gen (e-commerce), CUHK-PEDES and ICFG-PEDES (person Re-ID) [Primary Sub-task], and COCO, Flickr [Primary Sub-task], Nocaps (natural image). Evaluation Metrics
- - T2IR@1(Text-to-image retrieval)
- - I2TR@1 (Image-to-text retrieval) Hints
- - You are expected to setup the datasets and weights directories and populate using the provided links in the README.md file.
- - You can use the gdown library to directly download google drive contents, and git clone for studying relevant repositories.


This task is based on a method addressing query shift in cross-modal retrieval, which forms querycandidate pairs, selects source-domain-like pairs using intra-modality uniformity and inter-modality gap scores, then applies a joint objective combining uniformity loss, gap rectification, and noise-robust adaptation, updating only normalization layers online.

Agent Ideas. Across three runs, agents proposed test-time adaptation (TTA) methods with ’entropy’ based approaches to handle distribution shift:

- Run 001 (MADER - Modality-Aware Dual Entropy Regularization): The agent combined reliability-aware entropy minimization via quantile-based sample selection with confidence weighting, a


- READ-like distribution balance loss to prevent collapse, and confidence-weighted smoothing. This run made 8 evaluation attempts over 44 minutes of setup time, using IRRA pre-trained models with TTA. Best results: Base2Flickr I2TR@1=83.6, T2IR@1=70.0 (matching baseline), and ReID CUHK2ICFG=42.14 (1.27× baseline; the strongest ReID result across all runs).
- Run 002 (ASC - Adaptive Similarity Calibration): This approach used pseudo-label crossentropy on confident predictions (using nearest gallery neighbor as pseudo-label), entropy minimization, and a diversity regularizer on batch mean predictions. With 6 attempts over 65 minutes setup, it achieved Base2Flickr I2TR@1=86.3 (1.03× baseline) using BLIP, but ReID performance was poor (CUHK2ICFG=14.27, only 0.43× baseline).
- Run 003 (DMFCA - Dual-Modality Feature CORAL Alignment): The agent proposed aligning query feature distributions to gallery by matching first and second-order moments via CORAL loss, combined with entropy minimization. However, this run had the longest setup time (221 minutes = 3.7 hours) and made a critical implementation error: it ran ReID evaluations with –retrieval i2t instead of the required –retrieval t2i, collecting I2TR@1 instead of T2IR@1. As a result, all ReID metrics for Run 003 are missing.


Performance Progression. By hour 3, all three runs achieved Base2Flickr results exceeding baseline (avg 1.03×), demonstrating that the agent’s TTA methods work for natural image retrieval. However, ReID results were highly inconsistent: Run 001 achieved strong CUHK2ICFG (1.27×) but weak ICFG2CUHK (0.79×); Run 002 had uniformly poor ReID (0.43× and 0.72×); Run 003 never produced valid ReID results due to the wrong retrieval direction flag. This shows the need to keep diverse sub-tasks

- as primary sub-tasks, so agent’s methods do not end up overfitting to a certain set.


Token usage was high across all runs (39.9M, 22.8M, 33.7M tokens), and all runs consumed nearly the full $10 budget ($10.01, $10.00, $8.97). The extended Run 001 used an additional 40.1M tokens.

Bottlenecks and Failure Modes. Run 003 ended up spending 221 minutes (nearly 4 hours) on initialization before any evaluation. A critical failure was Run 003’s wrong retrieval direction flag, which invalidated all ReID results. Additionally, runs used domain-specific IRRA pre-trained models rather than adapting general CLIP/BLIP models as the task intended, which may explain why some ReID results exceeded baselines trained on those specific datasets.

Gap Analysis. The paper’s method carefully selects source-domain-like pairs and applies a principled joint objective with three complementary losses. The agent’s approaches (entropy minimization, CORAL alignment, pseudo-labeling) are reasonable TTA techniques but lack the paper’s key innovation of reliability-based pair selection using uniformity and gap scores. The agent’s methods showed strong results on Base2Flickr (natural images) but inconsistent ReID performance, suggesting that the adaptation techniques work better when query-gallery shift is moderate rather than severe (as in cross-dataset ReID).

Hint Ablation (hint_001). When provided the paper’s idea (query-candidate pair selection with reliability scoring and joint losses), the agent implemented “TCR” (Test-time Cross-modal Retrieval) that closely followed the hint. The implementation included: (1) nearest-neighbor candidate selection forming query-candidate pairs, (2) reliability scoring based on intra-modality uniformity and inter-modality gap, (3) queue of source-like pairs with top-30% selection, and (4) three joint losses (noise-robust entropy minimization, center-based uniformity, gap rectification). The run achieved I2TR@1=80.6, T2IR@1=62.26 on Base2Flickr ($10, 2.9 hours), matching the CLIP baseline for I2TR (80.2) but exceeding

it for T2IR (61.5). However, the ReID evaluations were never executed due to BLIP weights extraction failures (.rar format) and runtime errors. The handoff summaries document extensive debugging of entropy queue stacking bugs, NaN losses (resolved via float32 casting), and YAML compatibility issues. The hint provided correct algorithmic direction, but infrastructure challenges consumed the budget before full evaluation.

Async Ablation (async_001). Without the hint, the async run spent $10 over 2.8 hours but produced only smoke test results (I2TR@1=0.1, T2IR@1=0.2), effectively random performance. The agent implemented “CORA” (Cross-modal Online Retrieval Adaptation) combining entropy minimization and feature alignment, but never completed full dataset evaluation. Logs show the run launched multiple parallel jobs but all encountered setup failures (dataset path errors, model loading issues). The async capability was theoretically useful for running evaluations across multiple corruption types in parallel, but the prerequisite setup phase never completed successfully. This illustrates that parallelism provides no benefit when the sequential setup steps fail.

- Table 18: Comparisons with state-of-the-art methods on COCO-C benchmark under query shift on the image modality with maximum severity level regarding the Recall@1 metric. The best results are marked in bold.

Noise Blur Weather Digital Query Shift Gauss. Shot Impul. Speckle Defoc. Glass Motion Zoom Snow Frost Fog Brit. Contr. Elastic Pixel JPEG Avg.

| | | | | | |
|---|---|---|---|---|---|
|BLIP ViT-B/16<br><br>• Tent<br>• EATA<br>• SAR<br>• READ<br>• DeYO<br><br>• Ours<br>|43.4 46.3 43.2 57.3 41.6 40.5 37.9 54.0<br><br>41.4 50.3 35.7 63.1<br>42.3 51.5 37.5 61.8 45.8 48.4 37.2 59.9 47.9 53.5 46.8 63.4 53.2 56.2 54.8 64.6<br><br><br>|43.3 68.0 39.7 8.4<br>44.7 65.1 39.6 8.3 49.8 72.2 46.2 6.9 40.3 71.5 32.8 6.2 44.5 71.8 46.6 11.5 42.9 72.1 36.7 3.2 58.0 73.7 56.4 32.2<br><br><br>|32.3 52.2 57.0 66.8 31.9 48.7 56.3 66.5 45.6 56.7 62.5 71.4<br><br>38.0 56.2 59.1 70.6<br>39.9 49.9 58.4 70.3 37.5 59.7 66.4 71.2 56.5 64.1 71.0 73.4<br><br><br>|36.0 41.3 20.6 63.7 31.8 40.3 19.2 62.3 43.6 51.3 25.6 67.0 31.1 53.5 17.5 66.4 35.8 45.0 18.8 66.2 40.3 49.0 13.1 67.6 57.9 63.7 41.8 68.4<br><br>|45.0 43.0 49.3 46.0 46.9 48.2 59.1<br><br>|
|BLIP ViT-L/16<br><br>• Tent<br>• EATA<br>• SAR<br>• READ<br>• DeYO<br><br>• Ours<br>|50.3 51.8 51.1 61.6 46.3 49.3 46.7 58.4 46.2 53.5 49.5 63.8 45.9 50.2 47.3 63.1<br><br>38.1 48.0 43.3 63.5<br>39.9 50.2 43.5 63.8 58.2 60.7 59.8 66.6<br><br><br>|53.7 72.1 49.4 14.5 52.2 71.8 47.5 12.3 56.5 73.8 52.6 18.4 51.1 73.8 47.2 11.6 43.6 73.4 43.6 22.0 50.4 74.0 52.4 5.4<br><br>61.5 74.9 60.3 36.8<br><br>|44.0 57.5 61.8 70.5 41.9 56.2 60.9 69.7 50.6 59.1 64.5 72.1 40.8 58.9 60.7 71.6 44.5 56.5 62.2 71.9 49.5 59.3 62.8 71.8 59.0 65.2 72.1 73.5<br><br>|37.3 50.6 32.0 70.5 35.7 48.3 29.4 69.6 40.7 55.4 43.5 70.7<br><br>33.6 54.0 34.4 70.5 32.9 49.6 27.5 70.6<br>34.0 54.7 34.4 69.7 56.3 65.7 50.2 71.6<br><br><br>|51.8 49.8 54.4 50.9 49.5 51.0 62.0<br><br>|
| | | | | | |


- Table 19: Comparisons with state-of-the-art methods on COCO-C benchmark under query shift on the text modality with maximum severity level regarding the Recall@1 metric.


Character-level Word-level Sentence-level Query Shift OCR CI CR CS CD SR RI RS RD IP Formal Casual Passive Active Backtrans Avg.

| | | | | |
|---|---|---|---|---|
|BLIP ViT-B/16<br><br>• Tent<br>• EATA<br>• SAR<br>• READ<br>• DeYO<br><br>• Ours<br>|31.4 11.3 9.4 18.9 11.4 31.4 11.0 9.5 17.7 11.3<br><br>33.1 11.9 10.5 18.4 12.0<br><br>31.8 11.6 9.9 18.5 11.7<br>32.3 11.4 9.6 18.2 11.2 31.4 11.3 9.4 17.9 11.4<br><br><br>34.1 13.7 11.8 19.5 13.2<br><br><br>|43.6 51.5 50.3 50.6 56.8<br><br>43.2 51.3 50.3 50.6 56.6<br>44.9 53.0 51.6 50.3 56.2<br><br><br>43.6 51.5 50.3 50.6 56.8<br>44.3 52.9 51.7 51.1 57.6 43.6 51.5 50.3 50.6 56.8<br><br>45.3 53.8 51.8 51.5 57.3<br><br><br>|56.6 56.2 54.9 56.8 54.2 56.2 56.0 54.9 56.9 53.9 56.8 56.8 56.0 56.8 54.3<br><br>56.5 56.2 54.9 56.8 54.2<br>57.1 56.7 55.9 57.1 54.7<br><br><br>56.5 56.2 54.9 56.7 54.2<br><br>57.1 56.8 56.0 57.3 54.7<br><br><br>|40.9 40.7 41.5 41.0 41.4 40.9 42.3<br><br>|
|BLIP ViT-L/16<br><br>• Tent<br>• EATA<br>• SAR<br>• READ<br>• DeYO<br><br>• Ours<br>|34.5 12.3 11.1 19.7 12.9<br><br>34.0 12.3 11.0 19.6 12.9<br>35.6 13.3 11.3 20.3 13.2<br><br><br>34.5 13.1 11.2 20.3 13.1<br><br><br>35.3 12.2 10.9 19.1 12.7 34.5 12.3 11.1 19.7 12.9<br><br>36.8 14.7 13.4 21.3 14.3<br><br><br>|46.0 54.4 54.0 53.5 59.4<br><br>46.5 54.2 53.8 53.4 59.4<br>47.2 55.4 54.2 53.8 59.2<br><br><br>46.7 54.4 54.0 53.5 59.5<br>47.3 55.1 55.0 53.3 59.7<br><br><br>46.7 54.4 54.0 53.5 59.5<br><br>47.9 56.3 54.8 53.9 59.5<br><br><br>|59.1 58.8 57.8 59.4 56.7<br><br>59.1 58.8 57.6 58.9 56.5<br>59.1 59.4 57.9 59.4 56.8 59.1 58.8 57.8 59.4 56.7<br><br><br>59.3 59.1 58.1 59.6 56.7 59.1 58.8 57.8 59.4 56.7<br><br>59.4 59.0 58.2 59.6 56.9<br><br><br>|43.3 43.2 43.7 43.5 43.6 43.4 44.4<br><br>|
| | | | | |


- Table 20: Comparisons with state-of-the-art methods on benchmarks under Query-Gallery shifts regarding the Recall@1 metric. In the table, “ID", “ND" and “OD" refer to “In-Domain", “Near-Domain" and “Out-Domain", respectively. Besides, “TR@1" / “IR@1" represent Recall@1 for image-to-text retrieval / text-to-image retrieval.

Base2Flickr Base2COCO Base2Fashion Base2Nocaps(ID) Base2Nocaps(ND) Base2Nocaps(OD) Query Shift TR@1 IR@1 TR@1 IR@1 TR@1 IR@1 TR@1 IR@1 TR@1 IR@1 TR@1 IR@1 Avg.

| | | | | | | | |
|---|---|---|---|---|---|---|---|
|CLIP ViT-B/16<br><br>• Tent<br>• EATA<br>• SAR<br>• READ<br>• DeYO<br><br>• Ours<br>|80.2 61.5<br>81.4 64.0 80.4 63.4 80.3 62.2 80.6 64.4 80.1 64.0<br><br>82.4 64.8<br><br><br>|52.5 33.0 48.8 27.6 52.1 34.8 51.8 33.9 46.0 35.7<br><br>51.5 33.4<br><br>52.9 36.5<br><br><br>|8.5 13.2 5.6 10.7 8.1 12.0 8.0 13.3<br><br>5.8 11.2<br>6.9 10.9 8.9 14.0<br><br><br>|84.9 61.4<br>85.1 61.7 84.7 62.0<br><br><br>84.7 61.3<br>85.1 63.0<br><br><br>84.4 62.2<br><br>85.1 63.5<br><br><br>|75.4 49.2<br><br>74.6 48.6<br>75.1 52.3 75.4 51.3<br><br><br>75.0 52.1<br>75.1 52.0 75.7 54.0<br><br><br>|73.8 55.8 71.8 56.1<br>74.1 56.9 73.7 56.1 73.5 57.0<br><br><br>73.2 57.3<br><br>74.4 58.0<br><br><br>|54.1 53.0 54.7 54.3 54.1 54.3 55.9<br><br>|
|BLIP ViT-B/16<br><br>• Tent<br>• EATA<br>• SAR<br>• READ<br>• DeYO<br><br>• Ours<br>|70.0 68.3<br><br>81.9 68.5<br>82.3 69.4 81.7 68.3 80.0 69.9<br>83.5 69.9 86.8 70.3<br><br><br>|59.3 45.4<br><br>61.7 41.7<br><br>64.2 47.9 63.5 46.6<br><br>62.1 46.4<br><br>65.0 47.3 68.9 48.9<br><br><br><br><br>|19.9 26.1 14.1 26.1 12.8 25.2 17.9 26.1<br><br>5.6 24.1 12.2 24.1 23.6 30.3<br><br>|88.2 74.9<br><br>88.5 75.4<br><br>87.8 75.1<br>88.2 75.6 87.3 75.1<br>89.2 75.6<br><br><br>89.7 76.0<br><br><br>|79.3 63.6 82.6 64.1<br><br>82.8 63.9 81.0 65.4<br><br>80.6 63.9<br><br>83.7 65.7 86.3 66.1<br><br><br><br><br>|81.9 67.8<br>82.7 68.9 81.5 67.9 81.2 69.3 80.7 67.9 84.3 69.4 87.2 69.5<br><br><br>|62.1 63.0 63.4 63.7 62.0 64.2 67.0<br><br>|
| | | | | | | | |


- Table 21: Comparisons with state-of-the-art methods on ReID benchmarks under Query-Gallery shifts regarding the Recall@1 metric.


CUHK2ICFG ICFG2CUHK Query Shift IR@1 IR@1 Avg.

| | | | |
|---|---|---|---|
|CLIP ViT-B/16<br><br>• Tent<br>• EATA<br>• SAR<br>• READ<br>• DeYO<br><br>• Ours<br>|33.3 33.5 33.3 33.3 33.0 33.3 37.3<br><br>|41.0 41.9 42.2 42.2 42.3 42.2 42.4<br><br>|37.2 37.7 37.8 37.8 37.7 37.8 39.9<br><br>|
| | | | |


#### F.4 Time Series Explanation

Task Description

Research Goal

Recent explainable AI (XAI) methods for time series primarily focus on the magnitude of feature importance, overlooking the directional impact (positive or negative) on predictions. This leads to a suboptimal identification of significant points. Furthermore, existing evaluation metrics are flawed because they inadvertently cancel out the effects of features with opposing contributions, misrepresenting the effectiveness of attribution methods. In safety-critical domains like healthcare, energy, and transportation, high transparency in predictive models is necessary for safe and reliable operations. The black-box nature of deep neural networks makes it challenging to understand their decision-making processes, undermining trust and accountability. This work aims to provide more faithful and directionally-aware explanations for time series models, which is crucial for improving interpretability in applications where it directly impacts safety and effectiveness.

Experimental Settings

- • Datasets:

- – Synthetic: Switch-Feature, State.
- – Real-world: Personal Activity Monitoring (PAM) [Primary Sub-task], Boiler, Epilepsy, Wafer and Freezer.


- • Data Splits: For synthetic datasets, 800 training and 200 test samples were used. For real-world datasets, evaluations were performed over five random cross-validation repetitions.
- • Metrics:

- – Proposed: Cumulative Prediction Difference (CPD).
- – Existing: Area Under Precision (AUP), Area Under Recall (AUR).


- • Evaluation Setup: Compared against 13 baselines including FO, AFO, IG, GradSHAP, DeepLIFT, LIME, FIT, WinIT, Dynamask, Extrmask, ContraLSP, TimeX, and TimeX++.


Data prep: loaders read from ‘data/<dataset>‘ inside this task (see ‘datasets/*.py‘). Ensure the preprocessed artifacts from the original paper are placed in those folders (e.g. the ‘PAM/processed_data‘ and ‘splits‘ arrays, ‘boiler/split= <fold>.pt‘, ‘epilepsy/split_< fold >.npy‘, ‘Wafer/Wafer_{TRAIN,TEST}.txt‘, ‘FreezerRegularTrain/FreezerRegularTrain_{TRAIN,TEST}.txt‘). Synthetic runners also expect ‘data/hmm/‘ plus the ‘simulated_data_l2x/‘ pickles generated via ‘python synthetic/switchstate/switchgenerator.py‘.

##### Workflow checklist:

- 1. Prepare datasets under ‘data/‘ as described above (run synthetic generators once if needed).
- 2. Train/evaluate using the provided scripts in ‘scripts/‘ or equivalent commands.
- 3. Run ‘./grading/grade.sh‘ to update ‘task_description.md‘ and capture the JSON summary before finishing. Evaluation Metrics


- - Cumulative Prediction Difference (CPD)
- - Area Under Precision (AUP)
- - Area Under Recall (AUR)


This task is based on TIMING (ICLR 2025), which proposes segment-masked Integrated Gradients:

replacing the fixed zero baseline with a partially retained baseline defined by binary segment masks, aggregating attributions over random contiguous temporal segments to reduce out-of-distribution paths while respecting temporal structure.

Agent Ideas. All three runs proposed variations of Integrated Gradients with directional modifications:

- Run 001 (Margin-based Directional IG): The agent computed IG on the decision margin between predicted class and strongest alternative logit, applied ReLU to retain only positive contributions, and added temporal smoothing to emphasize contiguous segments. This run made 5 attempts with 170 minutes setup time. The progression showed steady improvement: starting at 0.327 CPD (hour 3), improving to 0.704 (hour 5), and finalizing at 0.357±0.105 (hour 9) with all 5 cross-validation folds complete. This was the only run to achieve high completion (71.4%).
- Run 002 (Directional Margin IG with per-baseline recomputation): This approach used margin IG for the Zeros baseline and predicted-class probability IG for the Average baseline, incorporating NoiseTunnel smoothing and positive clamping. With 13 attempts (most) over 297 minutes setup (5 hours), this run had an erratic progression: starting at 0.231 (hour 5), dropping to 0.054 (hour 7), then recovering to 0.589±0.036 (hour 9), exceeding both the IG baseline (0.448) and SOTA (0.463). However, task completion was only 14.3%.
- Run 003 (Margin-based Directional IG with CNN): The agent enhanced directional margin IG with a CNN classifier instead of the standard GRU, with per-baseline attribution recomputation. Despite 290 minutes setup and 6 attempts, performance was poor: final PAM Average CPD of only 0.180±0.082 (0.40× baseline), with 0% task completion.


Performance Progression. Only Run 001 produced complete 5-fold results by hour 8, achieving 0.84× baseline. Run 002 joined at hour 9 with the best single metric (1.31× baseline on Average CPD), but only Run 001 maintained consistent cross-validation coverage. The high variance across runs (std=0.37 on normalized Average CPD) suggests that implementation details like the handling of cross-validation folds significantly impacts final results.

Setup times were exceptionally long: 170, 297, and 290 minutes (3–5 hours) before any evaluation, consuming significant budget (total $16.52 across runs). Token usage ranged from 6.4M to 27.3M, with Run 002 using the most tokens but also achieving the best single-metric result.

Bottlenecks and Failure Modes. The primary bottleneck was dataset preparation and fold management. The task requires generating synthetic data pickles, downloading multiple real-world datasets, and running 5-fold cross-validation across 7 datasets. Agents frequently completed only partial folds or focused on easier synthetic datasets while neglecting the primary PAM task. Run 003’s 0% completion despite 6 attempts illustrates this as the agent produced results but never completed full 5-fold evaluation for any dataset.

The grading infrastructure also created friction: hint_001 produced valid 5-fold PAM results (CPD=0.311/ 0.524) in CSV format, but the grading script rejected them as “incomplete” because the expected directory structure wasn’t followed.

Gap Analysis. The paper’s TIMING method replaces fixed baselines with segment-masked partiallyretained baselines, aggregating over random contiguous masks. The agent’s approaches (margin-based IG, directional clamping, NoiseTunnel smoothing) are reasonable modifications to standard IG but don’t implement the core segment-masking innovation. Notably, hint_001 (given the paper’s method

description) implemented “Segment-masked Integrated Gradients” that closely matches the paper’s approach, but infrastructure issues prevented proper evaluation.

Hint Ablation (hint_001). When provided the paper’s idea (segment-masked partially-retained baselines), the agent correctly implemented “Segment-masked Integrated Gradients” in attribution/ segment_masked_ig.py. The implementation used random contiguous masks during IG computation, closely matching the paper’s TIMING approach. The run produced valid 5-fold results for PAM and Switch-Feature datasets: PAM Average CPD=0.311±0.023, PAM Zeros CPD=0.524±0.044 ($10, 5.2 hours). These results approach baseline performance (PAM Average baseline: 0.463).

Async Ablation (async_001). The async run failed catastrophically with ModuleNotFoundError:

No module named ’datasets.PAM’ and RuntimeError: No data exists or wrong path. The run never produced any valid evaluation results. The failure occurred during initial setup when attempting to import dataset modules, before any parallel experiment execution could begin. The agent’s plan included launching multiple dataset evaluations in parallel, but the prerequisite data generation step failed due to path configuration errors.

- Table 22: Performance comparison of various XAI methods on real-world datasets with 10% feature masking. Results are aggregated as mean ± standard error over five random cross-validation repetitions and presented across multiple datasets, including MIMIC-III, PAM, Boiler (Multivariate), Epilepsy, Wafer, and Freezer (Univariate). Evaluation metrics include cumulative prediction difference (CPD) attribution performance under two feature substitution strategies: average substitution (Avg.) and zero substitution (Zero).

MIMIC-III PAM Boiler Epilepsy Wafer Freezer

|Method|Avg. Zero|Avg. Zero<br><br>|Avg. Zero|Avg. Zero|Avg. Zero|Avg. Zero|
|---|---|---|---|---|---|---|
|AFO GradSHAP Extrmask ContraLSP TimeX++|0.127±0.009 0.227±0.017<br><br>0.250±0.015 0.522±0.038 0.154±0.008 0.305±0.010 0.048±0.003 0.051±0.004 0.017±0.002 0.074±0.006|0.140±0.009 0.200±0.013 0.421±0.014 0.518±0.012 0.291±0.007 0.380±0.009 0.046±0.007 0.059±0.011 0.057±0.004 0.070±0.004|0.262±0.020 0.349±0.035 0.752±0.055 0.747±0.092 0.338±0.028 0.400±0.031 0.408±0.035 0.496±0.043 0.124±0.028 0.208±0.043|0.028±0.003 0.030±0.004 0.052±0.004 0.054±0.004 0.028±0.003 0.029±0.003 0.016±0.001 0.016±0.001 0.030±0.004 0.032±0.004<br><br>|0.018±0.003 0.018±0.003 0.485±0.014 0.485±0.014 0.202±0.026 0.202±0.026 0.121±0.032 0.121±0.032 0.000±0.000 0.000±0.000<br><br>|0.143±0.054 0.143±0.054 0.397±0.110 0.397±0.110 0.176±0.057 0.176±0.057 0.176±0.055 0.176±0.055 0.216±0.056 0.216±0.056|
|IG TIMING|0.243±0.015 0.549±0.039 0.250±0.015 0.597±0.037<br><br>|0.448±0.013 0.573±0.022 0.463±0.007 0.602±0.033<br><br>|0.759±0.053 0.752±0.013<br><br>1.259±0.065 1.578±0.085<br><br><br>|0.052±0.004 0.054±0.004 0.057±0.005 0.060±0.005<br><br>|0.500±0.017 0.500±0.017 0.674±0.014 0.674±0.014<br><br>|0.405±0.111 0.405±0.111 0.409±0.109 0.409±0.109<br><br>|


- Table 23: Performance comparison of various XAI methods on Switch Feature and State datasets. Results are reported as mean ± standard error over five cross-validation repetitions, evaluated using AUP, AUR, and CPD (10% masking) for true saliency map and cumulative masking strategies.


##### Switch-Feature Method CPD ↑ AUP ↑ AUR ↑

|FO AFO GradSHAP DeepLIFT LIME FIT Dynamask Extrmask ContraLSP<br><br>|0.191±0.006 0.902±0.009 0.374±0.006 0.182±0.007 0.836±0.012 0.416±0.008<br><br>0.196±0.006 0.892±0.010 0.387±0.006<br><br>0.196±0.007 0.918±0.019 0.432±0.011 0.195±0.006 0.949±0.015 0.391±0.016 0.106±0.001 0.522±0.005 0.437±0.002 0.069±0.001 0.362±0.003 0.754±0.008 0.174±0.002 0.978±0.004 0.745±0.007 0.158±0.002 0.970±0.005 0.851±0.005<br><br><br>|
|---|---|
|IG TIMING<br><br>|0.196±0.007 0.918±0.019 0.433±0.011 0.208±0.003 0.926±0.011 0.434±0.015<br><br>|
| | |
|Method|State CPD ↑ AUP ↑ AUR ↑<br><br>|
|FO AFO GradSHAP DeepLIFT LIME FIT Dynamask Extrmask ContraLSP<br><br>|0.158±0.004 0.882±0.021 0.303±0.005 0.143±0.007 0.809±0.037 0.374±0.007 0.156±0.004 0.857±0.019 0.315±0.009<br><br>0.162±0.002 0.926±0.008 0.359±0.008<br><br>0.163±0.002 0.944±0.008 0.333±0.010 0.057±0.000 0.483±0.001 0.607±0.002 0.052±0.001 0.335±0.003 0.506±0.002 0.055±0.001 0.557±0.024 0.012±0.001 0.025±0.000 0.495±0.011 0.015±0.001<br><br><br>|
|IG TIMING<br><br>|0.162±0.002 0.922±0.009 0.357±0.008<br><br>0.163±0.002 0.921±0.010 0.355±0.008<br><br><br>|


##### F.4.1 Success Analysis: SOTA-Surpassing Run

The Time Series Explanation task represents the only task in ResearchGym where an agent surpassed the withheld reference solution (TIMING (Jang et al., 2025), an ICML 2025 Spotlight paper). In Run 002, the GPT-5-powered rg-agent achieved a PAM Average CPD of 0.589±0.036 and PAM Zeros CPD of 0.525±0.025, surpassing TIMING’s reported scores of 0.463±0.007 and 0.602±0.033 respectively on the primary metric (average of both). This section provides a deep dive into what made this run successful.

The Agent’s Novel Method: Directional Margin-Aware Attribution. The agent independently developed a directional, margin-aware attribution method that builds on Integrated Gradients (IG) but focuses on the decision boundary between the predicted class and the strongest alternative. The key innovation lies in three components:

- 1. Decision Margin Focus: Instead of attributing to the predicted class logit directly, the agent computes attributions for the margin between the predicted class and the second-most-likely class:

margin(x) = fpred(x) − falt(x). This targets features that genuinely support the current prediction over alternatives.

- 2. SmoothGrad-Squared Noise Tunnel: The agent wraps IG in a noise tunnel using smoothgrad_sq with 8 samples and σ = 0.02 standard deviation. This reduces variance in gradient estimates and produces more stable attribution maps.
- 3. Temporal Smoothing with Positive Clamping: A 1D average pooling layer (kernel size 5) smooths attributions temporally via reflect padding. Finally, attributions are clamped to ≥ 0 to retain only supportive contributions, avoiding cancellation effects that plague CPD evaluation.


Comparison with TIMING’s Solution. The original TIMING paper addresses the same core problem—that conventional IG ignores temporal structure and directional impact through a different approach: it modifies the IG integration path to respect temporal ordering, generating more realistic intermediate samples. In contrast, the agent’s solution:

- • Does not modify the IG path but instead changes what is being explained (margin vs. single logit)
- • Uses post-hoc smoothing rather than path-aware integration
- • Applies hard clamping to enforce directionality, which directly optimizes for the CPD metric


Both approaches recognize that directionality matters for CPD evaluation. TIMING achieves this through principled temporal path construction, while the agent’s method achieves it through marginbased attribution and aggressive positive filtering. The agent’s approach is arguably simpler to implement but may be less theoretically grounded.

Why Did This Succeed While Other Runs Failed? Analyzing the successful run against 6 failed attempts on this task reveals several distinguishing factors:

- 1. Run 002 made 13 distinct evaluation attempts over 9.5 hours, each time running the grader and using CPD scores to guide the next iteration. Failed runs often changed too many variables at once or abandoned promising directions prematurely.
- 2. The agent recognized that CPD with “Average” substitution and “Zeros” substitution have different sensitivities. It explicitly designed the method to perform well on both by focusing on margin-based attribution that correlates with prediction confidence.
- 3. The agent trained both “state” (GRU-based) and “CNN” models and aggregated results, increasing robustness.


Progression of Results. Table 24 shows how the agent’s scores evolved across 9.5 hours of experimentation.

- Table 24: Run 002 score progression on the PAM dataset (primary sub-task). The agent iteratively improved through 13 evaluation attempts, demonstrating sustained experimental discipline.


Time PAM Avg CPD PAM Zeros CPD

- 4h 57m 0.231 0.333
- 5h 16m 0.203 0.369


- 5h 35m 0.175 0.367

- 5h 55m 0.103 0.590
- 6h 21m 0.070 0.582

6h 44m 0.115 0.115 7h 11m 0.062 0.063

- 7h 32m 0.054 0.054




- 7h 48m 0.150 0.154
- 8h 10m 0.126 0.111
- 9h 21m (final) 0.589±0.036 0.525±0.025


Implications for Agent Design. This success case suggests that when agents maintain stable, controlled changes, and systematic iteration, they can discover novel solutions competitive with human research. The agent did not have access to the TIMING paper or its solution; it independently arrived

- at a complementary approach through trial and guided search. This demonstrates that frontier LLMs possess latent capability for genuine research contribution, though reliably eliciting this capability remains an open challenge.


Novelty Assessment. To assess whether the agent’s margin-based IG approach constitutes a genuinely novel contribution, we conducted a literature review. The core idea: computing attributions on the decision margin between predicted and alternative classes rather than a single class logit, falls within an emerging family of contrastive attribution methods. Prior work from NeurIPS 2022 proposes classcontrastive backpropagation with “mean contrast” and “max contrast” variants, demonstrating that attribution should consider how predictions differ from alternatives (Wang and Wang, 2022).

Notably, two closely related methods appeared in late 2025, after the agent’s knowledge cutoff and contemporaneous with this work. Contrastive Integrated Gradients (Vu et al., 2025) computes IG on logit vector differences, and DiffGradCAM (Piland et al., 2025) uses contrastive logit differentials. The agent did not perform web searches during this run and could not have accessed these papers, yet arrived at a conceptually similar solution: that attribution should target the decision margin rather than absolute class scores.

This represents an instance of convergent discovery: the agent independently developed an approach that parallels emerging research directions in the XAI community. The specific combination (IG on fpred − fsecond-best with SmoothGrad noise tunneling, temporal pooling, and positive clamping) does not appear in prior work. The agent’s ability to independently navigate to this solution space through empirical search, notably without access to relevant literature, highlights that LLM agents can identify promising research directions that align with where human researchers are independently heading.

#### F.5 Improving Replay Buffers

Task Description

[ht] Research Goal

In online reinforcement learning, uniformly replaying past experiences from a replay buffer is sample-inefficient, as some transitions are more valuable for learning than others. While prioritizing important samples can help, this often leads to overfitting, especially when such samples are rare. The problem is to develop a memory system that can replay relevant data at scale to improve learning efficiency without overfitting. The distribution of states an agent visits online is often suboptimal for training an effective policy. Focusing on more relevant transitions, such as those at critical decision boundaries or in less-explored regions, can significantly accelerate learning. Therefore, designing a memory system capable of identifying and densifying such useful experiences is crucial for improving the sample efficiency and overall performance of online RL agents.

##### Experimental Settings

- - Environments: DeepMind Control Suite (DMC) for state-based (Quadruped-Walk, Cheetah-Run, Reacher-Hard, Finger-Turn-Hard) and pixel-based (Walker-Walk, Cheetah-Run) tasks results averaged over 5 seeds. OpenAI Gym for state-based tasks (Walker2d-v2, HalfCheetah-v2, Hopper-v2 [Primary Sub-task]), results are averaged over 3 seeds. Randomized DMLab environments for stochasticity experiments.
- - Evaluation Protocol: Agents are trained for 100K environment interactions (300K for Finger-Turn-Hard*). Evaluation Metrics
- - Average Return
- - Dynamics MSE (log)
- - Dormant Ratio


Additionally, you can refer to the code repositories of the baseline methods for implementation guidance or ideas and inspirations:

- 1) SynthER: https://github.com/conglu1997/SynthER
- 2) REDQ: https://github.com/watchernyu/REDQ/tree/7b5d1bff39291a57325a2836bd397a55728960bb


Paper’s Method. The withheld SOTA method models the replay buffer as a conditional generative model p(τ|c) where c is a relevance scalar. A conditional diffusion model is trained with classifier-free guidance (condition dropped with probability 0.25) to synthesize transitions conditioned on high relevance values. The relevance function F(τ) can be return-based, TD-error, or curiosity-driven (forward-dynamics prediction error in latent space). Synthetic and real transitions are mixed with ratio r to train an off-policy learner, with separate 1M-transition buffers for each. For pixel-based tasks, generation occurs in the latent space of the policy’s CNN encoder.

Agent Ideas. All three primary runs attempted prioritized replay mechanisms but differed significantly in their approaches to transition importance and overfitting mitigation.

- Run 001 (Relevance-aware Densification) proposed identifying transitions at critical decision boundaries or in less-explored regions, with anti-overfitting guards using mixup augmentation and capped sampling


- weights. The agent attempted 4 submissions over 16 minutes of initialization time at a cost of $0.79 (1.1M tokens). However, the implementation struggled with the RL environment setup, and the final return of 195.93 (0.058× baseline) indicating execution failures.
- Run 002 (Boundary-focused Replay with Rarity Regularization) combined dynamics-model-based boundary detection with regularization to prevent overfitting on rare samples. This run spent only 9 minutes on initialization but made 5 attempts at a cost of $1.44 (1.5M tokens). The final return of 228.83 (0.067× baseline) showed marginal improvement over Run 001.
- Run 003 (Relevance-Densified Replay, RDR) was the most ambitious, combining uncertainty-based prioritization via ensemble Q-disagreement with diversity-aware densification using mixup and hierarchical scheduling. This run used the most resources: 8 attempts, 18 minutes initialization, $2.64 cost, and 2.5M tokens. The increased investment paid off: by hour 2, the return reached 2915.27 (on one seed) (0.859× baseline), substantially outperforming the other runs. The agent successfully implemented the ensemble disagreement mechanism and the core prioritization scheme, though the diversity component showed limited impact.


Bottlenecks. The primary bottleneck was RL environment execution reliability. Runs 001 and 002 exhibited failures where training produced near-zero returns despite the agent reporting “training complete.” Transcript analysis revealed tensor stride errors (“At least one stride in the given numpy array is negative”), missing dm_control dependencies, and high seed variance (Run 001 seed 1 achieved 181.65 while seed 0 achieved only 13.58). The agent’s inability to diagnose these silent failures led to wasted budget on non-functional training runs. Run 003’s success came partly from more defensive error handling and explicit logging of per-seed returns, allowing the agent to identify and address failing configurations.

Gap Analysis. The paper’s method achieves 4101.79 return on Hopper-v2 (1.21× baseline) through conditional diffusion-based data synthesis. Further, the paper generates entirely new transitions through a learned generative model, while the agent approaches relied on re-weighting or interpolating existing transitions.

Hint Ablation (hint_001). When provided the paper’s idea (conditional diffusion with relevancebased guidance), the agent attempted to implement “GymSynther”—a diffusion model generating synthetic transitions conditioned on relevance scores. The implementation faithfully followed the hint’s structure: classifier-free guidance with condition dropout, separate buffers for real and synthetic data, and TD-error-based relevance scoring. However, the diffusion generator never produced usable synthetic trajectories: the synthetic buffer remained empty throughout training (rb_syn=0). Transcript analysis revealed multiple technical failures: (1) tensor stride errors when converting numpy arrays to torch tensors (“At least one stride in the given numpy array is negative”), (2) missing dm_control.suite.wrappers.pixels attribute, and (3) numerical instabilities during diffusion sampling. The final return of 71.48±70.93 (0.021× baseline) came entirely from the standard SAC learner without synthetic augmentation. Despite understanding the algorithmic approach, the agent could not implement working diffusion-based RL synthesis within the time budget. The agent exhibited overconfidence throughout, reporting “Returns should improve substantially” while results remained near zero.

Async Ablation (async_001). The async run achieved 0.0 return across all seeds. The agent launched 3 parallel training jobs but cancelled all of them after 52 minutes when log files showed no progress. Post-hoc analysis revealed a path mismatch: the training jobs wrote results to logs/exp_*

Walker2d-v2 HalfCheetah-v2 Hopper-v2

mbpo 3781.34 ± 912.44 8612.49 ± 407.53 3007.83 ± 511.57 dreamer-v3 4104.67 ± 349.74 7126.84 ± 539.22 3083.41 ± 138.90 sac 879.98 ± 217.52 5065.61 ± 467.73 2033.39 ± 793.96 redq 3819.17 ± 906.34 6330.85 ± 433.47 3275.66 ± 171.90 synther 4829.32 ± 191.16 8165.35 ± 1534.24 3395.21 ± 117.50

##### (Curiosity) 5682.33 ± 370.04 9234.61 ± 658.77 4101.79 ± 244.05

Table 26: Results on state-based OpenAI gym tasks. We report average return after 100K environment steps. Results are over 3 seeds, with 1 std. dev. err.

directories, but the grading script expected logs/full/. The agent never diagnosed this mismatch and instead created hardcoded 0.0 fallback values as a “temporary fix.” Additionally, the log polling showed empty tails (“tail”: “”) between checks, indicating the jobs were either stuck or writing to unexpected locations. This case illustrates how async execution can obscure failures: with sequential execution, the agent would observe output and diagnose issues immediately; with parallel jobs, failures accumulate silently until the agent gives up.

DMC-100k (Online) Pixel-DMC-100k (Online) Environment

QuadrupedWalk

CheetahRun

ReacherHard

Finger-TurnHard*

WalkerWalk

CheetahRun

mbpo 505.91 ± 252.55 450.47 ± 132.09 777.24 ± 98.59 631.19 ± 98.77 - dreamer-v3 389.63 ± 168.47 362.01 ± 30.69 807.58 ± 156.38 745.27 ± 90.30 353.40 ± 114.12 298.13 ± 86.37 sac 178.31 ± 36.85 346.61 ± 61.94 654.23 ± 211.84 591.11 ± 41.44 - redq 496.75 ± 151.00 606.86 ± 99.77 733.54 ± 79.66 520.53 ± 114.88 - redq + curiosity 687.14 ± 93.12 682.64 ± 52.89 725.70 ± 87.78 777.66 ± 116.96 - drq-v2 - - - - 514.11 ± 81.42 489.30 ± 69.26 synther 727.01 ± 86.66 729.35 ± 49.59 838.60 ± 131.15 554.01 ± 220.77 468.53 ± 28.65 465.09 ± 28.27

(Reward) 510.39 ± 121.11 660.87 ± 87.54 715.43 ± 97.56 540.85 ± 73.29 - (Return) 737.62 ± 20.13 779.42 ± 30.00 893.65 ± 55.71 805.42 ± 92.07 - (TD Error) 802.18 ± 116.52 704.17 ± 96.49 917.61 ± 37.32 839.26 ± 49.90 - (Curiosity) 927.98 ± 25.18 817.36 ± 35.93 915.21 ± 48.24 885.98 ± 67.29 570.99 ± 41.44 529.70 ± 27.76

###### Table 25: Average returns on state and pixel-based DMC after 100K environment steps (5 seeds, 1std. dev. err.). * is a harder environment with sparser rewards, and so we present results over 300K timesteps.

