SC24-W: Workshops of the International Conference for High Performance Computing, Networking, Storage and Analysis | 979-8-3503-5554-3/24/$31.00 ©2024 IEEE | DOI: 10.1109/SCW63240.2024.00017

# SciTrust: Evaluating the Trustworthiness of Large Language Models for Science

Emily Herron Oak Ridge National Laboratory Oak Ridge, Tennessee herronej@ornl.gov

Junqi Yin Oak Ridge National Laboratory Oak Ridge, Tennessee yinj@ornl.gov

Feiyi Wang Oak Ridge National Laboratory Oak Ridge, Tennessee fwang2@ornl.gov

Abstract—This work presents SciTrust, a comprehensive framework for assessing the trustworthiness of large language models (LLMs) in scientific contexts, with a focus on truthfulness, accuracy, hallucination, and sycophancy. The framework introduces four novel open-ended benchmarks in Computer Science, Chemistry, Biology, and Physics, and employs a multi-faceted evaluation approach combining traditional metrics with LLMbased evaluation. SciTrust was applied to five LLMs, including one general-purpose and four scientific models, revealing nuanced strengths and weaknesses across different models and benchmarks. The study also evaluated SciTrust’s performance and scalability on high-performance computing systems. Results showed varying performance across models, with Llama3-70BInstruct performing strongly overall, while Galactica-120B and SciGLM-6B excelled among scientific models. SciTrust aims to advance the development of trustworthy AI in scientific applications and establish a foundation for future research on model robustness, safety, and ethics in scientific contexts. We have open-sourced our framework, including all associated scripts and datasets, at https://github.com/herronej/SciTrust.

Index Terms—Trustworthy AI, Large Language Models for Science, High Performance Computing

I. INTRODUCTION

Large language models (LLMs) have revolutionized natural language processing, demonstrating sophisticated knowledge generation and understanding capabilities. These Transformerbased models, leveraging self-attention mechanisms to capture broad textual relationships, have garnered significant interest in both industrial and academic spheres. LLMs designed for scientific applications, pre-trained or fine-tuned on scientific publications and databases, can handle various data types, including text, graphs, images, molecules, and DNA sequences. They are being actively applied in scientific discovery processes such as brainstorming, idea generation, hypothesis formation, and peer review [1]. Despite their capabilities, LLMs face challenges related to trustworthiness, encompassing dimensions such as truthfulness, safety, fairness, privacy preservation, robustness, and accountability [2]–[4]. They may produce inaccurate or plausible yet factually incorrect outputs (hallucinations), struggle with logical reasoning, exhibit sycophancy, and face difficulties generalizing to outof-distribution data. To address these concerns, we introduce SciTrust, a framework for evaluating the trustworthiness of scientific LLMs, with a particular focus on truthfulness. Our framework evaluates truthfulness from four perspectives: resistance to misinformation, resistance to hallucination, ability to

produce logically sound outputs, and resistance to sycophantic responses. We incorporate existing multiple-choice and openended benchmarks, as well as novel synthetic open-ended benchmarks. Model outputs are assessed based on metrics such as accuracy, semantic and lexical similarity, and LLMbased scoring. We apply our evaluation framework to four general science LLMs and compare their results to those of Llama3-70B-Instruct. Additionally, we report and compare the latencies of multiple-choice and open-ended inference on both the Frontier exascale supercomputer and an H100 testbed for each model. Our contributions are as follows:

- • We outline an evaluation framework for assessing trustworthiness in large language models for science.
- • We present results evaluating the truthfulness of scientific large language models from the perspectives of misinformation resistance, logical reasoning, hallucination resistance, and sycophancy resistance.
- • We introduce four novel open-ended datasets designed for assessing scientific knowledge found in scientific publications from the domains of Computer Science, Chemistry, Biology, and Physics.
- • We evaluate open-ended datasets using both lexical (ROUGE scores [5]) and semantic methods (BERT [6] and BART [7] scores), as well as LLM-as-judge-based scoring. To our knowledge, this is the first trustworthiness evaluation framework that incorporates language modelbased evaluations.


II. RELATED WORK

Recent evaluations of trustworthiness in prominent large language models (LLMs) have provided valuable context for our work on evaluating the scientific trustworthiness of LLMs. Wang et al. [4] presented a thorough evaluation of LLM trustworthiness across eight perspectives, primarily focusing on GPT-3.5 and GPT-4. Their findings revealed that while GPT-4 outperforms GPT-3.5 across most trustworthiness metrics, both models showed susceptibility to carefully crafted prompts, privacy leakage, and bias. Huang et al. [3] offered a standardized framework for assessing the ethical implications of LLMs, focusing on toxicity, bias, and alignment with human values. Sun et al. [2] examined LLM trustworthiness through seven dimensions, concluding that trustworthiness strongly correlates with LLM utility and that proprietary LLMs generally outperform open-source LLMs in trustworthiness. Other

979-8-3503-5554-3/24/$31.00 ©2024 IEEE 72 DOI 10.1109/SCW63240.2024.00017

benchmarks have evaluated the scientific reasoning capabilities of LLMs, though not specifically focused on trustworthiness. Sun et al. [8] assessed LLM performance on challenging scientific questions across four dimensions, while Cai et al. [9] evaluated LLM performance in analyzing scientific literature. Both frameworks demonstrated consistently good performance from GPT-4, but found that LLMs generally struggle with certain tasks, particularly those involving calculations and multimodal scientific content. These studies incorporated a mixture of objective and open-ended questions, with the latter being qualitatively, rather than automatically evaluated. Our framework, SciTrust, represents an extension of previous works on trustworthiness to the sciences. It evaluates the trustworthiness of open-source large language models in scientific applications, focusing primarily on truthfulness by assessing models’ susceptibility to misinformation, logical reasoning capabilities, degree of hallucination, and susceptibility to sycophantic prompts. We believe these attributes are particularly relevant when using LLMs in scientific applications. SciTrust incorporates novel open-ended benchmarks into the framework and evaluates the generated answers using a range of automatic metrics, addressing the limitations of previous studies and providing a more comprehensive assessment of LLM trustworthiness in scientific contexts.

III. SCIENTIFIC MODELS EVALUATED

We applied our evaluation framework to five open-source LLMs: four trained specifically on general-purpose scientific knowledge and one state-of-the-art generic model as a baseline. The models evaluated are:

- • FORGE-L-Instruct: A 25.6B parameter model developed at Oak Ridge National Laboratory, was trained on 257 billion tokens from scientific articles. It uses an optimized GPT-NeoX architecture and performs well on domain-specific tasks and scientific benchmarks [10].
- • SciGLM-6B: ChatGLM architecture, fine-tuned on diverse scientific data. It employs self-reflective annotation and instruction quality filtering, showing improved performance on scientific and mathematical reasoning benchmarks [11].
- • Darwin-7B: Part of the DARWIN series, a fine-tuned version of Llama2-7B focused on natural sciences. It uses Scientific Instruction Generation for training and demonstrates strong performance on various scientific tasks [12].
- • Galactica-120B: Developed by Meta, was trained on 120 billion tokens from various scientific sources. It uses a Transformer-based decoder-only architecture and covers multiple scientific domains. The model demonstrates strong performance in scientific question answering, mathematical reasoning, and chemical property prediction [13].
- • Llama3-70B-Instruct: Our baseline model, was trained on over 15 trillion tokens and fine-tuned using various techniques. It includes trust and safety features and focuses on improving reasoning and coding tasks [14].


![image 1](Herron et al._2024_SciTrust Evaluating the Trustworthiness of Large Language Models for Science_images/imageFile1.png)

Fig. 1. An example of the prompt used for the multiple-choice datasets. The prompt is shown in black and the correct answer is shown in red. This question and answer pair is found in our the MMLU College Computer Science dataset.

IV. TRUTHFULNESS EVALUATION

Our evaluation framework assesses the truthfulness of scientific LLMs by considering four key aspects: scientific accuracy and resistance to misinformation, logical reasoning capabilities, tendency to hallucinate, and resistance to sycophantic outputs.

A. Resistance to Misinformation

To assess a model’s resistance to misinformation, we employed both existing scientific multiple-choice benchmarks and novel open-ended benchmarks designed to evaluate a model’s ability to generate accurate scientific knowledge.

1) Multiple-Choice Questions: We incorporated several existing multiple-choice benchmarks to assess the scientific knowledge of language models:

- 1) SciQ: 13.7K crowd-sourced questions from 4th and 8th grade science textbooks [15].
- 2) GPQA-Diamond: 198 high-quality questions in biology, chemistry, and physics, answerable by experts but challenging for non-experts [16].
- 3) ARC-C: 2,590 ’hard’ science questions from 3rd through 9th grade exams [17].
- 4) MMLU (College Computer Science, Chemistry, Physics, and Biology Tests): College-level exam questions across various scientific disciplines [18].


We created custom prompts for each question following the format shown in Figure 1. Model performance was assessed using both 0-shot and 2-shot demonstrations, with a maximum output of 3 tokens. Accuracy was determined by an exact match of the correct answer choice letter in the output. We generated four separate outputs for each prompt and averaged the accuracies.

Results (Table I) show that Llama3-70B-Instruct consistently outperformed the scientific LLMs across all benchmarks. Among scientific models, Galactica-120B achieved the best accuracies on most benchmarks, with SciGLM-6B outperforming it on SciQ and GPQA-Diamond. This high performance might be attributed to training on data from textbooks and solution manuals.

For subject-specific MMLU datasets, Llama3-70B-Instruct performed best in Biology and Computer Science. Galactica120B and SciGLM-6B excelled in Biology and Chemistry. FORGE showed strength in Chemistry and Computer Science, while Darwin underperformed on most benchmarks.

TABLE I AVERAGE ACCURACIES OF GENERAL PURPOSE AND SCIENTIFIC LLMS ON VARIOUS MULTIPLE CHOICE SCIENTIFIC BENCHMARKS.

MMLU College Computer Science

MMLU College Chemistry

MMLU College Physics

MMLU College Biology

GPQA Diamond

SciQ

ARC-C

Model k=0 k=2 k=0 k=2 k=0 k=2 k=0 k=2 k=0 k=2 k=0 k=2 k=0 k=2

Llama3-70B-Instruct 98.79% 98.54% 40.28% 38.34% 94.17% 93.15% 55.25% 56.88% 64.00% 63.19% 57.11% 54.79% 90.80% 89.92% FORGE-L-Instruct 14.89% 26.15% 10.61% 22.33% 12.91% 25.64% 20.75% 27.50% 14.50% 27.50% 13.48% 20.12% 21.35% 17.54%

SciGLM-6B 86.86% 89.37% 13.26% 31.04% 87.04% 89.10% 29.75% 45.94% 28.50% 36.56% 16.18% 30.49% 66.49% 72.58% Darwin-7B 1.51% 0.80% 0.13% 0.76% 0.16% 0.61% 0.00% 0.00% 1.00% 0.00% 0.00% 0.00% 0.52% 0.00%

Galactica-120B 85.41% 79.72% 28.94% 26.81% 62.13% 61.69% 38.75% 38.13% 34.00% 34.69% 37.25% 31.71% 62.85% 59.68%

![image 2](Herron et al._2024_SciTrust Evaluating the Trustworthiness of Large Language Models for Science_images/imageFile2.png)

Fig. 2. The prompt used to generate our open-ended Computer Science, Chemistry, Biology, an Physics datasets given scientific journal articles using ChatGPT-4o.

2) Open-Ended Questions: Recognizing the limitations of multiple-choice benchmarks in assessing in-depth scientific understanding, we generated open-ended datasets for Computer Science, Chemistry, Biology, and Physics using GPT4o. We prompted the model to generate question-answer pairs based on journal articles using the prompt shown in Figure 2 combined with two example questions and answers.

The full texts of journal articles were accessed from the S2ORC training subset of the PES2O [19] dataset. We used the Semantic Scholar API to query metadata for each publication, allowing us to filter the text data by subject area and limit to journal articles with 500 or more citations published after 2005, ensuring high-quality content. Using these articles and our prompt, we generated a total of 500 questions for each of four scientific domains (Computer Science, Chemistry, Biology, and Physics).

Figure 3 shows an example question and answer pair from our generated Computer Science open-ended dataset, combined with the prompt we used for evaluating our models on the open-ended datasets. When evaluating the models on these datasets, we set the maximum number of new tokens to 300 and generated four separate outputs per prompt, as was the case with the multiple-choice datasets.

We evaluated the generated outputs for each open-ended dataset using both lexical (ROUGE scores) and semantic metrics (BERT and BART scores). Additionally, taking inspiration from [20], we used GPT-4o as a judge to rate the quality of the outputs on a scale of 0 to 10 based on the following the prompt shown in Figure 4.

![image 3](Herron et al._2024_SciTrust Evaluating the Trustworthiness of Large Language Models for Science_images/imageFile3.png)

- Fig. 3. An example of the prompt used to generate outputs given the openended datasets. The prompt is shown in black and the correct answer is shown in red. This question and answer pair are from our open-ended Computer Science dataset.

![image 4](Herron et al._2024_SciTrust Evaluating the Trustworthiness of Large Language Models for Science_images/imageFile4.png)

- Fig. 4. The prompt used for scoring outputs to open-ended datasets using ChatGPT-4o.


Tables II, III, V, and IV present the average scores for each metric across datasets and models. Consistent with the multiple-choice benchmarks, Llama3-70B-Instruct generally outperformed other models across all datasets. However, FORGE-L-Instruct showed comparable performance on semantic and lexical metrics, despite scoring significantly lower when evaluated by GPT-4o.

TABLE II AVERAGE AND STANDARD DEVIATION ROUGE-1 F1, ROUGE-L F1, BERT SCORE, BART SCORE, AND GPT-4O SCORES FOR OUTPUTS GENERATED FROM GENERAL PURPOSE AND SCIENTIFIC LLMS ON OUR OPEN-ENDED COMPUTER SCIENCE DATASET.

BERT Score F1

ROUGE-1 F1

ROUGE-L F1

BART Score

GPT-4o Score

Model

Llama3-70B-Instruct 0.35±0.12 0.21±0.07 0.59±0.09 0.92±0.10 4.12±2.35 FORGE-L-Instruct 0.32±0.08 0.19±0.05 0.58±0.05 0.93±0.04 2.36±1.81 SciGLM-6B 0.28±0.15 0.16±0.07 0.56±0.07 0.89±0.09 2.18±1.83

Darwin-7B 0.01±0.02 0.01±0.01 0.31±0.03 0.59±0.04 0.00±0.00 Galactica-120B 0.25±0.12 0.15±0.06 0.53±0.07 0.86±0.09 2.39±1.98

TABLE III AVERAGE AVERAGE AND STANDARD DEVIATION ROUGE-1 F1, ROUGE-L F1, BERT SCORE, BART SCORE, AND GPT-4O SCORES FOR OUTPUTS GENERATED FROM GENERAL PURPOSE AND SCIENTIFIC LLMS ON OUR OPEN-ENDED CHEMISTRY DATASET.

BERT Score F1

ROUGE-1 F1

ROUGE-L F1

BART Score

GPT-4o Score

Model

Llama3-70B-Instruct 0.35±0.17 0.22±0.07 0.61±0.09 0.92±0.11 4.36±2.34 FORGE-L-Instruct 0.34±0.16 0.20±0.05 0.60±0.05 0.94±0.05 3.06±2.04 SciGLM-6B 0.24±0.24 0.15±0.08 0.57±0.09 0.87±0.10 2.16±1.76

Darwin-7B 0.01±0.02 0.01±0.02 0.33±0.03 0.61±0.04 0.00±0.02 Galactica-120B 0.25±0.21 0.16±0.07 0.53±0.08 0.88±0.10 2.54±2.09

For the Computer Science and Physics datasets, Galactica120B performed on par with or better than FORGE-L-Instruct in terms of GPT-4o scores. The strong performance of these two models on these datasets may be attributed to their training on scientific publications.

Each model demonstrated varying strengths across different domains. Llama3-70B-Instruct achieved its best overall results on the Chemistry dataset, FORGE-L-Instruct performed best on Chemistry and Biology, SciGLM excelled in Chemistry and Computer Science, Darwin showed strongest performance in Computer Science, and Galactica-120B demonstrated highest proficiency in Chemistry and Physics.

- B. Logical Reasoning


In addition to assessing scientific knowledge, we included both multiple-choice and open-ended benchmarks to evaluate the models’ logical reasoning capabilities. Large language models can capture some logic from natural language samples, but often struggle with complex logic and are not always reliable in generating logically sound output. Training on

TABLE V AVERAGE AND STANDARD DEVIATIONROUGE-1 F1, ROUGE-L F1, BERT SCORE, BART SCORE, AND GPT-4O SCORES FOR OUTPUTS GENERATED FROM GENERAL PURPOSE AND SCIENTIFIC LLMS ON OUR OPEN-ENDED PHYSICS DATASET.

BERT Score F1

ROUGE-1 F1

ROUGE-L F1

BART Score

GPT-4o Score

Model

Llama3-70B-Instruct 0.37±0.17 0.23±0.07 0.60±0.08 0.92±0.10 4.10±2.36 FORGE-L-Instruct 0.33±0.17 0.20±0.05 0.56±0.05 0.93±0.05 2.50±1.81 SciGLM-6B 0.25±0.22 0.15±0.08 0.56±0.08 0.87±0.10 1.54±1.45 Darwin-7B 0.01±0.02 0.01±0.01 0.32±0.03 0.59±0.04 0.00±0.00 Galactica-120B 0.29±0.19 0.18±0.06 0.55±0.07 0.89±0.08 2.61±2.08

TABLE VI AVERAGE ACCURACIES OF GENERAL PURPOSE AND SCIENTIFIC LLMS ON TWO MULTIPLE CHOICE LOGICAL INFERENCE BENCHMARKS.

LogiQA ReClor Model k=0 k=2 k=0 k=2

Llama3-70B-Instruct 61.11% 62.57% 84.70% 85.17% FORGE-L-Instruct 11.29% 25.95% 13.05% 24.95%

SciGLM-6B 50.21% 50.54% 54.84% 56.47% Darwin-7B 0.43% 0.34% 0.18% 0.15%

Galactica-120B 33.65% 35.83% 34.34% 36.94%

natural language corpora alone is insufficient for learning formal and higher-order logical representations. Addressing this limitation may require incorporating logical structures into training data and developing new methods for representing logical structures in LLMs [21].

For multiple-choice benchmarks, we used the LogiQA and ReClor datasets. LogiQA was designed to test language models for logical reasoning capabilities in reading comprehension. It covers multiple types of deductive reasoning, including categorical, conditional, disjunctive, and conjunctive reasoning, sourced from logical exams for civil servants [22]. ReClor is another dataset for assessing logical reasoning through reading comprehension, sourced from standardized graduate admissions exams such as GMAT and LSAT [23].

For open-ended logical reasoning evaluation, we used the LOGICINFERENCE dataset, which is a synthetically generated dataset developed to assess models’ ability to perform logical inference. It covers propositional logic and a subset of first-order logic, including problems in semi-formal logic notation and natural language [24].

We used the same prompts and generation parameters described in the previous section for both benchmark types.

TABLE IV AVERAGE AND STANDARD DEVIATION ROUGE-1 F1, ROUGE-L F1, BERT SCORE, BART SCORE, AND GPT-4O SCORES FOR OUTPUTS GENERATED FROM GENERAL PURPOSE AND SCIENTIFIC LLMS ON OUR OPEN-ENDED BIOLOGY DATASET.

BERT Score F1

ROUGE-1 F1

ROUGE-L F1

BART Score

GPT-4o Score

Model

Llama3-70B-Instruct 0.35±0.11 0.22±0.07 0.61±0.09 0.92±0.01 4.15±2.37 FORGE-L-Instruct 0.34±0.15 0.20±0.05 0.60±0.05 0.94±0.03 2.93±1.95 SciGLM-6B 0.22±0.23 0.14±0.07 0.56±0.08 0.87±0.09 1.93±1.68

Darwin-7B 0.01±0.02 0.01±0.02 0.33±0.03 0.60±0.04 0.00±0.00 Galactica-120B 0.25±0.20 0.16±0.07 0.56±0.08 0.88±0.09 2.38±1.99

TABLE VII AVERAGE ROUGE-1 F1, ROUGE-L F1, BERT SCORE, BART SCORE, AND GPT-4O SCORES FOR OUTPUTS GENERATED FROM GENERAL PURPOSE AND SCIENTIFIC LLMS ON THE LOGICINFERENCE DATASET.

BERT Score F1

GPT-4o Score Llama3-70B-Instruct 0.31 0.25 0.61 0.86 3.81

ROUGE-1 F1

ROUGE-L F1

BART Score

Model

FORGE-L-Instruct 0.23 0.18 0.56 0.84 0.82 SciGLM-6B 0.19 0.16 0.49 0.74 1.80

Darwin-7B 0.03 0.03 0.37 0.58 0.07 Galactica-120B 0.23 0.19 0.55 0.82 1.23

TABLE VIII AVERAGE PERCENT HALLUCINATED ANSWERS PREDICTED BY SELFCHECKNLI USING A THRESHOLD OF 0.35 FOR VARIOUS OPEN-ENDED DATASETS.

Biology QA

Physics QA

Chemistry QA

Computer Science QA

LOGICINFERNCE Llama3-70B-Instruct 61.81% 60.58% 64.03% 65.49% 56.38%

Model

FORGE-L-Instruct 70.31% 69.98% 70.22% 74.07% 74.23% SciGLM-6B 71.12% 67.71% 74.16% 73.74% 78.07% Darwin-7B 70.76% 64.99% 69.85% 69.90% 82.33% Galactica-120B 72.33% 67.96% 71.10% 73.56% 84.91%

TABLE IX AVERAGE PERCENT HALLUCINATED ANSWERS PREDICTED BY THE LYNX HALLUCINATION EVALUATION LLM FOR VARIOUS OPEN-ENDED DATASETS.

Biology QA

Physics QA

Chemistry QA

Computer Science QA

LOGICINFERENCE Llama3-70B-Instruct 75.65% 70.53% 72.25% 70.36% 69.80%

Model

FORGE-L-Instruct 94.23% 93.00% 91.95% 92.82% 77.50% SciGLM-6B 85.65% 89.73% 82.85% 87.99% 72.00% Darwin-7B 98.09% 98.73% 98.04% 98.87% 93.85% Galactica-120B 76.10% 78.77% 75.95% 78.71% 69.15%

Consistent with previous experiments, Llama3 achieved the best performance on each of these benchmarks and metrics. Among the scientific models, SciGLM achieved the highest overall scores on the multiple-choice benchmarks and on the open-ended benchmark when judged by GPT-4o. However, FORGE and Galactica performed best on the open-ended dataset in terms of lexical and semantic metrics. This discrepancy suggests that lexical and semantic metrics alone may be insufficient for adequately evaluating logical reasoning tasks.

- C. Hallucination


We evaluated the outputs of each model for hallucinations using two distinct approaches: Self-Check NLI and Lynx. These methods provide complementary insights into the models’ tendencies to generate inaccurate or fabricated information. The first method, SelfCheckGPT with Natural Language Inference (NLI), generates multiple stochastic samples from the same prompt. It then uses a pre-trained NLI model (DeBeRTa-v3-large fine-tuned on the MNLI dataset) to classify the relationship between each sample (premise) and the original LLM output (hypothesis) as entailment, contradiction, or neutral. The final score, representing the average contradiction probability across samples, indicates the likelihood of hallucination or inaccurate information [25]. Our second approach employed Lynx-8B, an open-source LLM fine-tuned on HaluBench, a comprehensive multi-domain hallucination evaluation benchmark. We used the standard prompts provided by the authors, using the correct answers as contexts, to judge whether the outputs of each model were hallucinated [26].

Tables VIII and IX present the results of our hallucination analyses. Llama3 consistently achieved the lowest hallucination percentages across both metrics, demonstrating its superior performance in generating accurate information. Among the scientific models, Darwin tended to have the lowest hallucination scores on the self-contained SelfCheckNLI for subject-specific benchmarks, while FORGE hallucinated the least on LOGICINFERENCE. Interestingly, the Lynx-based

![image 5](Herron et al._2024_SciTrust Evaluating the Trustworthiness of Large Language Models for Science_images/imageFile5.png)

Fig. 5. Example of a prompt used for assessing model sycophancy on multiple-choice datasets. The prompt is shown in black, the correct answer in red, and the line triggering a sycophantic response in blue. This questionanswer pair is from the MMLU College Computer Science dataset.

evaluation, which uses a model-based approach, yielded different results. Galactica exhibited the lowest hallucination rates among the scientific models, even outperforming Llama3 on the LOGICINFERENCE dataset. Conversely, Darwin showed the highest hallucination rates across all benchmarks when evaluated by Lynx.

These contrasting outcomes highlight the differences between self-contained and model-based hallucination detection methods. They underscore the complexity of evaluating hallucination in language models and suggest that a multifaceted approach to hallucination detection may provide a more comprehensive understanding of model performance.

D. Sycophancy

Many LLMs are susceptible to producing sycophantic outputs that agree with the user, regardless of correctness. This behavior jeopardizes the model’s ability to produce consistently truthful answers and may correlate with susceptibility to adversarial prompts [2]. To test each model’s susceptibility to sycophancy, we modified the prompts for the SciQ, ARC-C, and GPQA-Diamond datasets by adding a line suggesting that the user believes an incorrect answer choice is true. Figure 5 shows an example of a sycophantic system prompt.

Figure 6 illustrates the impact of sycophantic prompts on model accuracy. Galactica and SciGLM showed the greatest reductions in accuracy, especially pronounced with the SciQ and ARC-C datasets. The effect was less significant for GPQA-Diamond, possibly due to differences in benchmark difficulty. Llama3 and SciGLM exhibited comparable percent reductions in accuracy. Galactica and Llama3 showed noticeably larger reductions in accuracy for 0-shot prompts compared to 2-shot versions. Other models displayed the reverse trend, with greater reductions in 2-shot scenarios.

The varying responses to sycophantic prompts across models and datasets highlight the complex nature of this issue. The difference in behavior between 0-shot and 2-shot scenarios for Galactica and Llama3 might be explained by the specific instruction tuning procedures used in fine-tuning these models.

V. HARDWARE AND LATENCY EVALUATIONS

Our evaluation benchmarks were deployed on two distinct computing environments: Frontier, the first exascale supercomputer, and Holly, our H100 testbed. Frontier, an HPE Cray

![image 6](Herron et al._2024_SciTrust Evaluating the Trustworthiness of Large Language Models for Science_images/imageFile6.png)

Fig. 6. Average percentage reductions in accuracy given sycophantic prompts on multiple-choice benchmarks.

TABLE X AVERAGE PER-SAMPLE INFERENCE TIMES (S) ON THE MULTIPLE-CHOICE SCIQ DATASET (TRAINING SUBSET 11,679 SAMPLES) AND OPEN-ENDED COMPUTER SCIENCE QA DATASET (500 SAMPLES) FOR VARIOUS LARGE LANGUAGE MODELS

SciQ Computer Science QA

Model 1 Frontier Node 8 H100 GPUs 1 Frontier Node 8 H100 GPUs Llama3-70B-Instruct 2.23 0.50 99.06 12.94 FORGE-L-Instruct 0.52 0.21 27.77 6.02

SciGLM-6B 0.14 0.06 4.97 2.25 Darwin-7B 0.20 0.07 18.06 5.06

Galactica-120B 2.66 1.00 96.41 23.81

EX supercomputer, comprises 9,400 nodes, each equipped with four AMD Instinct MI250X GPUs and a third-generation EPYC CPU. The system is unified by a Slingshot-11 interconnect and features the Orion parallel file system [10], [27]. Holly consists of a single Supermicro server with eight NVIDIA H100 GPUs.

We compared inference latencies by generating outputs for 1% of samples in the multiple-choice SciQ and openended CSQA datasets with each model, then extrapolated total runtimes. For Frontier, we adjusted calculations to account for parallel processing across multiple nodes. Results in Tables X and XI show that average per-sample inference times were 2 to 5 times higher on a single Frontier node compared to Holly’s 8 H100 GPUs. However, when leveraging Frontier’s parallelism across 100 nodes, total inference times were reduced by 20 to 50 times compared to Holly. A positive correlation was found between latency and the number of parameters in each model across both platforms. These findings demonstrate the scalability of our framework on highly parallelized systems like Frontier, which allows for a systematic evaluation of LLMs for science.

VI. CONCLUSION AND FUTURE WORK

In this work, we introduced SciTrust, a framework for evaluating the trustworthiness of scientific large language models (LLMs). Our framework assesses four open-source scientific LLMs based on their ability to produce outputs that are free of misinformation, logically sound, minimally hallucinated, and resistant to sycophantic prompts. We utilized a collection of scientific benchmarks, including existing multiple-choice tests and novel open-ended synthetic datasets,

TABLE XI ESTIMATED TOTAL LATENCIES (S) ON THE MULTIPLE-CHOICE SCIQ DATASET (TRAINING SUBSET 11,679 SAMPLES) AND OUR OPEN-ENDED COMPUTER SCIENCE QA DATASET (500 SAMPLES) FOR VARIOUS LARGE LANGUAGE MODELS

SciQ Computer Science QA

Model 100 Frontier Nodes 8 H100 GPUs 100 Frontier Nodes 8 H100 GPUs Llama3-70B-Instruct 260.10 5867.20 495.28 6470.04

FORGE-L-Instruct 60.31 2399.33 138.86 3008.71 SciGLM-6B 15.91 745.28 24.87 1126.51 Darwin-7B 23.56 821.50 90.28 2528.43

Galactica-120B 311.02 11687.73 482.07 11904.31

comparing the answers from each scientific model to those produced by Llama3-70B-Instruct. Our findings indicate that Llama3, our baseline model, generally produced the most desirable outputs across all trustworthiness criteria. Among the scientific models, Galactica-120B typically performed best, followed by SciGLM-6B. Our assessment revealed varying model performances across different benchmark types. For instance, FORGE-L-Instruct performed better on open-ended benchmarks than on multiple-choice tests, while SciGLM showed the opposite trend. This highlights the importance of using diverse metrics to evaluate scientific knowledge in language models.

In logical reasoning evaluations, SciGLM-6B displayed strong performance, followed by Galactica-120B. Hallucination results varied based on the metric used, with Darwin7B performing well on self-contained metrics and Galactica120B showing the lowest percentages of hallucinated answers in LLM-based evaluations. Regarding sycophancy, Galactica120B and SciGLM-6B were most prone to sycophantic prompts, while Llama3-70B-Instruct struggled more on this criterion than any other model. We also reported the performance and scalabilty of SciTrust in terms of inference latencies on the Frontier supercomputer and an NVIDIA H100 testbed.

Future work will entail verifying results from our openended datasets and expanding the framework to include additional aspects of trustworthiness. We plan to enlist subject matter experts to ensure the quality of our synthetic datasets and expand our evaluation to include dimensions such as adversarial and out-of-distribution robustness, safety, ethics, and bias from a scientific perspective. This comprehensive approach will provide a more nuanced assessment of scientific LLM trustworthiness, addressing the unique challenges and requirements of scientific applications. By refining and expanding our evaluation framework, we aim to contribute to the development of more reliable, ethical, and effective language models for scientific research and communication.

VII. ACKNOWLEDGEMENTS

This research used resources of the Oak Ridge Leadership Computing Facility (OLCF), which is a DOE Office of Science User Facility at the Oak Ridge National Laboratory supported by the U.S. Department of Energy under Contract No. DEAC05-00OR22725.

REFERENCES

- [1] Y. Zhang, X. Chen, B. Jin, S. Wang, S. Ji, W. Wang, and J. Han, “A comprehensive survey of scientific large language models and their applications in scientific discovery,” 2024. [Online]. Available: https://arxiv.org/abs/2406.10833
- [2] L. Sun, Y. Huang, H. Wang, S. Wu, Q. Zhang, Y. Li, C. Gao, Y. Huang, W. Lyu, Y. Zhang, X. Li, Z. Liu, Y. Liu, Y. Wang, Z. Zhang, B. Vidgen, B. Kailkhura, C. Xiong, C. Xiao, C. Li, E. Xing, F. Huang, H. Liu, H. Ji, H. Wang, H. Zhang, H. Yao, M. Kellis, M. Zitnik, M. Jiang, M. Bansal, J. Zou, J. Pei, J. Liu, J. Gao, J. Han, J. Zhao, J. Tang, J. Wang, J. Vanschoren, J. Mitchell, K. Shu, K. Xu, K.-W. Chang, L. He, L. Huang, M. Backes, N. Z. Gong, P. S. Yu, P.-Y. Chen, Q. Gu, R. Xu, R. Ying, S. Ji, S. Jana, T. Chen, T. Liu, T. Zhou, W. Wang, X. Li, X. Zhang, X. Wang, X. Xie, X. Chen, X. Wang, Y. Liu, Y. Ye, Y. Cao, Y. Chen, and Y. Zhao, “Trustllm: Trustworthiness in large language models,” 2024. [Online]. Available: https://arxiv.org/abs/2401.05561
- [3] Y. Huang, Q. Zhang, P. S. Y, and L. Sun, “Trustgpt: A benchmark for trustworthy and responsible large language models,” 2023. [Online]. Available: https://arxiv.org/abs/2306.11507
- [4] B. Wang, W. Chen, H. Pei, C. Xie, M. Kang, C. Zhang, C. Xu, Z. Xiong, R. Dutta, R. Schaeffer, S. T. Truong, S. Arora, M. Mazeika, D. Hendrycks, Z. Lin, Y. Cheng, S. Koyejo, D. Song, and B. Li, “Decodingtrust: A comprehensive assessment of trustworthiness in gpt models,” 2024. [Online]. Available: https://arxiv.org/abs/2306.11698
- [5] C.-Y. Lin, “ROUGE: A package for automatic evaluation of summaries,” in Text Summarization Branches Out. Barcelona, Spain: Association for Computational Linguistics, Jul. 2004, pp. 74–81. [Online]. Available: https://aclanthology.org/W04-1013
- [6] T. Zhang, V. Kishore, F. Wu, K. Q. Weinberger, and Y. Artzi, “Bertscore: Evaluating text generation with bert,” 2020. [Online]. Available: https://arxiv.org/abs/1904.09675
- [7] W. Yuan, G. Neubig, and P. Liu, “Bartscore: Evaluating generated text as text generation,” 2021. [Online]. Available: https://arxiv.org/abs/ 2106.11520
- [8] L. Sun, Y. Han, Z. Zhao, D. Ma, Z. Shen, B. Chen, L. Chen, and K. Yu, “Scieval: A multi-level large language model evaluation benchmark for scientific research,” 2023. [Online]. Available: https: //arxiv.org/abs/2308.13149
- [9] H. Cai, X. Cai, J. Chang, S. Li, L. Yao, C. Wang, Z. Gao, H. Wang, Y. Li, M. Lin, S. Yang, J. Wang, M. Xu, J. Huang, F. Xi, J. Zhuang, Y. Yin, Y. Li, C. Chen, Z. Cheng, Z. Zhao, L. Zhang, and G. Ke, “Sciassess: Benchmarking llm proficiency in scientific literature analysis,” 2024. [Online]. Available: https://arxiv.org/abs/2403.01976
- [10] J. Yin, S. Dash, F. Wang, and M. Shankar, “Forge: Pre-training open foundation models for science,” in Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis, ser. SC ’23. New York, NY, USA: Association for Computing Machinery, 2023. [Online]. Available: https://doi.org/10.1145/3581784.3613215
- [11] D. Zhang, Z. Hu, S. Zhoubian, Z. Du, K. Yang, Z. Wang, Y. Yue, Y. Dong, and J. Tang, “Sciglm: Training scientific language models with self-reflective instruction annotation and tuning,” 2024. [Online]. Available: https://arxiv.org/abs/2401.07950
- [12] T. Xie, Y. Wan, W. Huang, Z. Yin, Y. Liu, S. Wang, Q. Linghu, C. Kit, C. Grazian, W. Zhang, I. Razzak, and B. Hoex, “Darwin series: Domain specific large language models for natural science,” 2023. [Online]. Available: https://arxiv.org/abs/2308.13565
- [13] R. Taylor, M. Kardas, G. Cucurull, T. Scialom, A. Hartshorn, E. Saravia, A. Poulton, V. Kerkez, and R. Stojnic, “Galactica: A large language model for science,” 2022. [Online]. Available: https://arxiv.org/abs/2211.09085
- [14] “Introducing Meta Llama 3: The most capable openly available LLM to date — ai.meta.com,” https://ai.meta.com/blog/meta-llama-3/, [Accessed 09-08-2024].
- [15] J. Welbl, N. F. Liu, and M. Gardner, “Crowdsourcing multiple choice science questions,” 2017. [Online]. Available: https://arxiv.org/abs/1707. 06209
- [16] D. Rein, B. L. Hou, A. C. Stickland, J. Petty, R. Y. Pang, J. Dirani, J. Michael, and S. R. Bowman, “Gpqa: A graduate-level google-proof qa benchmark,” 2023. [Online]. Available: https://arxiv.org/abs/2311.12022
- [17] F. Chollet, “On the measure of intelligence,” 2019. [Online]. Available: https://arxiv.org/abs/1911.01547


- [18] D. Hendrycks, C. Burns, S. Basart, A. Zou, M. Mazeika, D. Song, and J. Steinhardt, “Measuring massive multitask language understanding,”

2021. [Online]. Available: https://arxiv.org/abs/2009.03300

- [19] L. Soldaini and K. Lo, “peS2o (Pretraining Efficiently on S2ORC) Dataset,” Allen Institute for AI, Tech. Rep., 2023, oDC-By, https: //github.com/allenai/pes2o.
- [20] L. Zheng, W.-L. Chiang, Y. Sheng, S. Zhuang, Z. Wu, Y. Zhuang, Z. Lin, Z. Li, D. Li, E. P. Xing, H. Zhang, J. E. Gonzalez, and

I. Stoica, “Judging llm-as-a-judge with mt-bench and chatbot arena,”

2023. [Online]. Available: https://arxiv.org/abs/2306.05685

- [21] R. Friedman, “Large language models and logical reasoning,” Encyclopedia, vol. 3, no. 2, pp. 687–697, 2023. [Online]. Available: https://www.mdpi.com/2673-8392/3/2/49
- [22] J. Liu, L. Cui, H. Liu, D. Huang, Y. Wang, and Y. Zhang, “Logiqa: A challenge dataset for machine reading comprehension with logical reasoning,” 2020. [Online]. Available: https://arxiv.org/abs/2007.08124
- [23] W. Yu, Z. Jiang, Y. Dong, and J. Feng, “Reclor: A reading comprehension dataset requiring logical reasoning,” 2020. [Online]. Available: https://arxiv.org/abs/2002.04326
- [24] S. Ontanon, J. Ainslie, V. Cvicek, and Z. Fisher, “Logicinference: A new dataset for teaching logical inference to seq2seq models,” 2022. [Online]. Available: https://arxiv.org/abs/2203.15099
- [25] P. Manakul, A. Liusie, and M. J. F. Gales, “Selfcheckgpt: Zero-resource black-box hallucination detection for generative large language models,”

2023. [Online]. Available: https://arxiv.org/abs/2303.08896

- [26] S. S. Ravi, B. Mielczarek, A. Kannappan, D. Kiela, and R. Qian, “Lynx: An open source hallucination evaluation model,” 2024. [Online]. Available: https://arxiv.org/abs/2407.08488
- [27] “Frontier supercomputer debuts as world&x2019;s fastest, breaking exascale barrier — ORNL — ornl.gov,” https://www.ornl.gov/news/ frontier-supercomputer-debuts-worlds-fastest-breaking-exascale-barrier, [Accessed 30-07-2024].


