arXiv:2506.05542v1[cs.LG]5 Jun 2025

# Agentomics-ML: Autonomous Machine Learning Experimentation Agent for Genomic and Transcriptomic Data

Vlastimil Martinek1,2 Andrea Gariboldi1,2 Dimosthenis Tzimotoudis1,2

Aitor Alberdi Escudero1,2 Edward Blake1,2 David Cechákˇ 3,4 Luke Cassar1,2

Alessandro Balestrucci1,2 Panagiotis Alexiou1,2 1Centre for Molecular Medicine and Biobanking, University of Malta, Msida, Malta 2Department of Applied Biomedical Science, Faculty of Health Sciences, University of Malta, Msida, Malta 3Central European Institute of Technology, Masaryk University, Brno, Czech Republic 4National Centre for Biomolecular Research, Faculty of Science, Masaryk University, Brno, Czech Republic

## Abstract

The adoption of machine learning (ML) and deep learning methods has revolutionized molecular medicine by driving breakthroughs in genomics, transcriptomics, drug discovery, and biological systems modeling. The increasing quantity, multimodality, and heterogeneity of biological datasets demand automated methods that can produce generalizable predictive models. Recent developments in large language model-based agents have shown promise for automating end-to-end ML experimentation on structured benchmarks. However, when applied to heterogeneous computational biology datasets, these methods struggle with generalization and success rates. Here, we introduce Agentomics-ML, a fully autonomous agentbased system designed to produce a classification model and the necessary files for reproducible training and inference. Our method follows predefined steps of an ML experimentation process, repeatedly interacting with the file system through Bash to complete individual steps. Once an ML model is produced, training and validation metrics provide scalar feedback to a reflection step to identify issues such as overfitting. This step then creates verbal feedback for future iterations, suggesting adjustments to steps such as data representation, model architecture, and hyperparameter choices. We have evaluated Agentomics-ML on several established genomic and transcriptomic benchmark datasets and show that it outperforms existing state-of-the-art agent-based methods in both generalization and success rates. While state-of-the-art models built by domain experts still lead in absolute performance on the majority of the computational biology datasets used in this work, Agentomics-ML narrows the gap for fully autonomous systems and achieves state-of-the-art performance on one of the used benchmark datasets. The code is available at https://github.com/BioGeMT/Agentomics-ML.

Preprint.

## 1 Introduction

High throughput -omics technologies, including genomics, transcriptomics, proteomics, metabolomics and epigenomics, have transformed molecular biology into a data driven science. A single high-throughput DNA/RNA sequencing run can generate gigabases of nucleotide data, while each single mass spectrometry experiment quantifies tens of thousands of proteins in parallel. Beyond pure volume, the complexity of molecular biology datasets makes them difficult to model and interpret (Bharti et al., 2024). Despite these issues, research on large molecular biology datasets is crucial for tasks ranging from sequence classification and annotation at the fundamental biology level, up to translational tasks in biomedical science such as disease prediction. Without algorithmic frameworks that can perform quality control, normalization, feature extraction, and other downstream tasks such as classification, these datasets remain collections of uninterpreted measurements rather than sources of biological insight (Xu and Jackson, 2019).

Genomic data production is increasing at an exponential rate, with sequencing throughput doubling approximately every seven months. These datasets are characterized by high dimensionality, complex missing value patterns and technical noise. Batch effects from different instrument runs or library preparations can obscure true biological signals (Yu et al., 2024b). Class imbalance is common in tasks such as regulatory element detection or rare variant analysis, in which relevant events may represent less than one percent of the data (Schubach et al., 2017). Combining heterogeneous data modalities such as sequence, expression and metabolite profiles further complicates analysis. As sequencing and detection costs decline the number of skilled analysts has increased only modestly, creating a bottleneck in the translation of raw data into actionable knowledge. The need for further automation of analytical steps is pressing (Wörheide et al., 2021).

In this study we present Agentomics-ML, an agentic system designed to function as a virtual machine learning expert for -omics data analysis. We demonstrate the use of Agentomics-ML on several classification tasks on genomic and transcriptomic data. The system can plan and self-reflect, allowing for decomposition of complex tasks into subtasks that it can iteratively complete and evaluate. We demonstrate that our system can successfully produce working ML code including trained models over 93% of the time, even in a more complex dataset where all other agentic state of the art systems tested fail to produce working code. Additionally, we offer a lightweight implementation that allows easy deployment and extension by bioinformaticians that may not be ML experts. Using minimal tool use, Agentomics-ML can perform end to end analysis without human intervention, and outperform both zero-shot LLM code, and all benchmarked state of the art agentic ML systems. The code in our experiments is provided in the supplementary materials under the MIT License.

## 2 Related work

### 2.1 Auto-ML

Traditional Automated Machine Learning (AutoML) systems, such as AutoSklearn (Feurer et al., 2022), represent an established approach to automating ML workflows. These systems typically operate by performing automated feature engineering, hyperparameter optimization, and model ensembling, primarily demonstrating strong performance on well-structured tabular data. However, their operational model assumes that input data are already adequately represented and they possess limited inherent capabilities to incorporate domain-specific knowledge or complex user requirements. A key limitation is their general inability to design novel or highly complex model architectures, such as those required for deep learning applications (Azevedo et al., 2024), which restricts their utility for challenging biological datasets where custom architectures are often essential for achieving sufficient performance. While these tools require minimal code, a human is still necessary to write code and provide preprocessed data (Sun et al., 2023).

### 2.2 Zero-shot LLMs

Large Language Models (LLMs) have enabled an alternative modality for ML task automation through their capacity for zero-shot code generation. In this approach, the LLM is provided with a task specification via a prompt, and it generates a code block intended for external execution to train an ML model. This method offers substantial flexibility and can integrate domain knowledge or user requirements expressed in the prompt. However, such systems fundamentally lack the intrinsic ability

to directly execute or validate the generated code, nor can they autonomously refine their proposed solutions based on runtime feedback or errors. Consequently, human oversight and intervention are typically required to ensure the correctness and successful execution of the generated code.

### 2.3 Agents

LLM Agents extend LLMs by providing them with tools such as code execution or retrieval. By interacting with the environment through tools they react to errors and intermediate observations, thereby enabling a more iterative and autonomous ML development process (Sun et al., 2024). Some agentic frameworks are designed for human-in-the-loop operation, where user guidance directs the agent’s actions. Others, like DS-Agent, aim for end-to-end automation but may depend on a curated database of solutions to similar past tasks for optimal performance. For instance, SELA (Hong et al., 2024b) conceptualizes ML pipeline development as a search problem, employing a Monte Carlo Tree Search guided by an LLM to explore and refine data preprocessing, feature engineering, model selection, and hyperparameter configurations, using validation metrics as feedback. Data Interpreter constructs a hierarchical task graph to decompose complex analytical problems, dynamically invoking external tools for sub-tasks like model training and statistical analysis, and incorporates mechanisms for consistency checking and backtracking. AIDE (Jiang et al., 2025) adopts a tree-search methodology, treating each potential ML solution as a node and iteratively refining promising candidates using tools for file management and script evaluation, achieving notable results on benchmarks including MLE-Bench.

### 2.4 Benchmarks

Despite these advancements, current agentic ML systems commonly face significant challenges in evaluation and deployment. Evaluations are frequently confined to Kaggle-style tabular benchmarks, which may not adequately represent the complexities of domain-specific -omics datasets. While initiatives like MLAgentBench (Huang et al., 2024a) and MLE-Bench (Chan et al., 2025) are expanding evaluation to diverse tasks, the extensive prior exploration of some benchmark datasets may influence LLM decisions if their training data includes existing solutions. A critical issue is the robust prevention of test set information leakage; many systems lack strict programmatic abstraction of the test data from the LLM during the development phase, potentially inflating reported performance metrics. Furthermore, existing solutions often do not produce fully reproducible training environments or production-ready inference scripts without considerable manual postprocessing. These gaps underscore the need for domain-aware agentic frameworks. To this end, curated resources like Genomic Benchmarks (Grešová et al., 2023) provide standardized datasets for genomic sequence classification, and miRBench (Sammut et al., 2025) offers novel, bias-corrected datasets for microRNA binding site prediction, facilitating rigorous and fair benchmarking critical for advancing ML in specialized biological domains

## 3 Methodology

Agentomics-ML is an agentic system constructed to automate machine learning experimentation for -omics data, balancing a structured high-level workflow with significant agent autonomy to produce a suitable machine learning model. Requiring only training data file and optional data description, the system outputs an inference script including all necessary artifacts, enabling immediate inference on external data like a test set. Additionally, our system outputs a training script that contains the training code, ensuring reproducibility.

### 3.1 Pre-defined steps

Agentomics-ML follows pre-defined steps of a machine learning experimentation process as shown in Figure 1: data exploration, choosing data representation and model architecture, producing training and inference scripts, and training a model. After the first data exploration step, the agent is able to use acquired knowledge like descriptive statistics and domain information from data description to decide on non-random data splitting strategy to better estimate generalization during model development (Catania et al., 2022). We opted for a step-based approach instead of elaborate prompt engineering to

![image 1](Martinek et al._2025_Agentomics-ML Autonomous Machine Learning Experimentation Agent for Genomic and Transcriptomic Data_images/imageFile1.png)

Figure 1: Architecture of Agentomics-ML: Agent follows pre-defined steps of an ML development pipeline, gradually completing sequential steps to eventually output a working ML model. File output steps are validated for correct syntax and format, forcing the agent to retry failed steps. After each iteration both scalar and verbal feedback is collected to guide decision during future iterations.

avoid unnecessary agent planning (Xie et al., 2024) as we consider these high-level steps essential in the machine learning experimentation process.

### 3.2 Validation of output

To complete a step, our agent repeatedly uses available tools for bash commands execution, writing python files, and executing python files. Taking actions like installing conda packages and writing helper scripts, the agent eventually outputs either text describing design decisions, acquired knowledge to be used by future steps, or files that are programmatically validated using the Pydantic AI framework

- 1. For example, when outputting an inference script, the script is run with dummy data to immediately validate the required script arguments and output format of the produced predictions. The agent is triggered to retry and is not able to advance to the next step unless the output passes this programmatic validation. Due to the security risk of providing our agent with a general bash tool and code execution ability, all agent operations occur within a secure, isolated Docker container.


### 3.3 Feedback mechanism

Our agent can run in multiple iterations. Due to the effectiveness for error-correcting capability in complex tasks (Huang et al., 2024b; Shinn et al., 2023), we use a reflection step. Processing the whole iteration context and scalar feedback from validation and train set metrics, the agent takes a reflection step producing verbal feedback that is used to guide decisions of the next iteration agent. Verbal feedback is stored together with metrics and additionally used by reflection steps during next

1https://ai.pydantic.dev/

iterations. This iterative process allows the system to reflect on outcomes, identify issues such as overfitting by observing validation performance, and progressively improve the model.

### 3.4 Evaluation

At the very end of this multi-iteration process, we fall back to the model version that achieved the best performance on the validation metric. To prevent data leakage, the agentic system is programmatically abstracted from the held-out test set throughout its development cycle. Only the final, agent-produced inference script is used to report performance on the test set. When comparing Agentomics-ML against other methods, including existing agentic systems and zero-shot LLM approaches, we require that all tested methods are fully automatable and adhere to the same strict test set abstraction to ensure fair and leakage-free evaluation.

### 3.5 Datasets

For benchmarking various methods, we prioritized tasks with existing published state-of-the-art models for comparison (Qiao et al., 2024; Yu et al., 2024a; Thoutam and Ellsworth, 2024). We selected classification datasets from Genomic Benchmarks (Grešová et al., 2023) that contain genomic sequences for various tasks including detecting enhancers and promoters. Some datasets contain variable-length sequences, a common trait of bioinformatic sequence datasets. Further, we select a classification dataset from miRBench (Sammut et al., 2025) that requires modeling of the interaction of two RNA sequences with variable lengths.

## 4 Experiments

- 4.1 Success rates


- 4.1.1 LLM zero-shots

The first baseline of attempting to classify genomic datasets using a non-agentic system is direct use of widely available LLMs with zero-shot prompts. We have selected to evaluate 8 of the most widely used LLMs: OpenAI’s gpt-4.1 and o4-mini, Anthropic’s claude-3.7-sonnet, Google’s gemini2.5-pro-preview, Alibaba’s qwen3-32b, Deepseek’s deepseek-r1 and deepseek-chat, and Meta’s llama-4-maverick. All models are run with the same prompt (link to supplement) which includes basic data format description and instructions to produce a complete executable solution in a single interaction. The returned code is programmatically parsed, saved, and executed in a controlled environment, without any tool use or environmental interaction by the model. Each model was prompted 5 times, and runs evaluated independently. Success rates for these runs are aggregated per model in Table 1. As expected, standalone LLMs fail to consistently produce viable code. Best of class is openAI/o4-mini with a 56.66% success rate over all datasets. On the other end, qwen/qwen3-32b barely manages to produce working code with a success rate of 6.66% over all datasets.

- 4.1.2 Agentic systems


An important added value of agentic systems is their ability to execute code and correct their trajectories based on feedback from the environment, increasing the rate of producing properly running inference scripts. We proceed with benchmarking two state of the art agentic systems that have been developed for producing machine learning models with inference code on arbitrary datasets. Both systems are tested using their publicly available implementations with default settings across all datasets. To ensure comparability, all methods were provided with the standard user prompt, with minimal adjustments to increase method success rates. Similarly to the zero-shot LLM experiments, each agentic system was run 5 times on each dataset, and success rates were calculated and aggregated as before (Table 1). The Data Interpreter (DI) agentic system (Hong et al., 2024a) was run with all used LLM models as a backbone. Surprisingly, the success rate of the LLMs did not always improve when used through DI. For the deepseek family of models, DI brought the success rate down to almost zero. On the other hand, OpenAI’s gpt-4.1 model has shown performance improvement.

The second agentic system tested was AIDE (Jiang et al., 2025). AIDE was configured to use the standard user prompt and was run using gpt-4.1 as the coding model. The success rate was 10% over

all datasets, with 4/6 datasets producing no working inference code in any of the 5 runs. This was primarily due to AIDE scripts containing programming errors, and not producing necessary scripts or artifacts for inference. Importantly, none of the zero-shot LLMs or the agentic systems benchmarked managed to produce any workable code for the most complex of used datasets AGO2_CLASH_Hejret. This dataset consists of two sequences per sample, one of which having variable length. Each of these sequences independently has no predictive value, but their interaction is biologically important. All benchmarked methods have 0% success rate on this dataset, showcasing the failure of such models as soon as moderately complex datasets are introduced.

### 4.1.3 Agentomics-ML

We proceeded with benchmarking our proposed agentic system on the same datasets. Again, the system is run 5 times per dataset, using the same prompt instructions as before, on the same hardware. We notice a significant improvement in success rates, with 100% success rate for five out of six datasets, including the more complex AGO2_CLASH_Hejret dataset. On the sixth dataset we achieve a 60% success rate, bringing the overall success rate over all datasets to 93.33%. These results showcase that our solution can consistently produce workable machine learning code and models, even on datasets with a more complex nature. This is an important first step in the development of end to end automated scientific discovery systems in computational biology.

- Table 1: Percentage of successfull runs for each dataset-method combination. Method that failed produce any valid solution are assigned 0%. Best per dataset are marked in bold.


Method AGO2 DE HEC HEE NTP OCRE Agentomics-ML: gpt-4.1 (no feedback) 100% 100% 100% 100% 60% 100% Agentomics-ML: gpt4_1 100% 100% 100% 100% 60% 100% AIDE: gpt-4.1 0% 0% 0% 0% 40% 20% DI: claude-3.7-sonnet 0% 0% 20% 0% 20% 0% DI: deepseek-chat 0% 0% 0% 0% 20% 0% DI: deepseek-r1 0% 0% 0% 0% 0% 0% DI: llama-4-maverick 0% 20% 0% 20% 60% 0% DI: gpt4.1 0% 0% 20% 40% 40% 0% DI: qwen3-32b 0% 0% 0% 0% 0% 0% zero_shot: claude-3.7-sonnet 0% 20% 20% 20% 20% 0% zero_shot: deepseek-chat 0% 20% 20% 40% 40% 100% zero_shot: deepseek-r1 0% 40% 20% 40% 20% 20% zero_shot: llama-4-maverick 0% 20% 0% 0% 0% 20% zero_shot: gpt-4.1 0% 20% 0% 0% 0% 0% zero_shot: o4-mini 0% 100% 40% 80% 60% 60% zero_shot: qwen3-32b 0% 0% 0% 20% 0% 20%

### 4.2 Model performance

We proceed to evaluate the performance of all benchmarked methods across datasets in Table 2. We compare models produced from zero-shot LLMs and DI paired with several models,and AIDE and Agentomics-ML paired with gpt-4.1. We report the best run performance metric for each method on each dataset, as evaluated on a left-out test set (Table 2). We also report the mean (Table 3) and standard deviation (Table 5) for the average performance metric over all runs. Missing values denote cases where the method did not produce any successful code over 5 tries. We also compare all methods against Human State of the Art (Human SOTA), those being published methodologies produced by domain experts, and we use metrics reported by those publications to allow for a fair comparison. All experiments were run using one NVIDIA A40 or A4000 GPU, 64 CPU cores and 32GB of RAM.

In the Drosophila_enhancers_stark dataset, Agentomics-ML outperforms all other methods (0.72 accuracy) as well as the Human SOTA from the original publication (Grešová et al., 2023) (0.59 accuracy). In the Human_enhancers_cohn dataset, Agentomics-ML without iterative feedback produces 0.72 accuracy, while the system using iterative feedback loop outperforms the other LLM-based methods with 0.74 accuracy. Similarly, for Human_enhancers_ensembl, Human_nontata_promoters,

and Human_ocr_ensembl datasets, where the Agentomics-ML model with iterative feedback outperforms all LLM-based methods. In the AGO2_CLASH_Hejret dataset the iterative feedback loop improves the average precision score metric from 0.72 to 0.78. No other LLM-based methods managed to produce workable code for this dataset. We perform a t-test and find that the feedback loop statistically improves performance compared to non-feedback agent on 2 out of 6 datasets (4). We find that models produced after iterative feedback obtain better test set metrics 80% of the time and outperform no-feedback models relatively on-average by 3.8%. This consistent improvement positions Agentomics-ML as the unanimous leader in automated machine learning on all tested genomic and transcriptomic datasets. It is possible that extending the number of iterations beyond what was tested, or adjusting the reflection mechanism, could push the benefits of the feedback loop even further.

- Table 2: Test set performance metrics for each dataset-method combination displaying maximum value of 5 separate runs. Accuracy is used for all except AGO2 where average precision score is used. Best overall is marked as underlined and bold. Best LLM-based method is marked in bold.


Method AGO2 DE HEC HEE NTP OCRE Agentomics-ML: gpt-4.1 (no feedback) 0.724 0.716 0.716 0.864 0.897 0.786 Agentomics-ML: gpt4_1 0.778 0.736 0.743 0.885 0.925 0.816 AIDE: gpt-4.1 N/A N/A N/A N/A 0.920 0.758 DI: claude-3.7-sonnet N/A N/A 0.724 N/A 0.839 N/A DI: deepseek-chat N/A N/A N/A N/A 0.871 N/A DI: deepseek-r1 N/A N/A N/A N/A N/A N/A DI: llama-4-maverick N/A 0.500 N/A 0.738 0.874 N/A DI: gpt4.1 N/A N/A 0.500 0.752 0.873 N/A DI: qwen3-32b N/A N/A N/A N/A N/A N/A zero_shot: claude-3.7-sonnet N/A 0.650 0.728 0.864 0.901 N/A zero_shot: deepseek-chat N/A 0.680 0.681 0.811 0.897 0.666 zero_shot: deepseek-r1 N/A 0.700 0.621 0.568 0.874 0.458 zero_shot: llama-4-maverick N/A 0.661 N/A N/A N/A 0.651 zero_shot: gpt-4.1 N/A 0.703 N/A N/A N/A N/A zero_shot: o4-mini N/A 0.708 0.728 0.848 0.885 0.506 zero_shot: qwen3-32b N/A N/A N/A 0.850 N/A 0.662 Human SOTA 0.860 0.586 0.747 0.933 0.974 0.825

## 5 Limitations

### 5.1 Potential pre-training data leakage

As the training datasets of mainstream closed-source LLMs are not publicly disclosed by the providers, we cannot determine whether the datasets used for benchmarking in this study were part of the LLMs pre-training corpora. The same uncertainty applies to state-of-the-art approaches evaluated on these benchmarks, potentially raising concerns about data leakage and the integrity of comparative results.

### 5.2 Reproducibility

We used various available large language models for our experiments, including closed-source models that are available only through API calls. This brings a risk of a closed-source model being replaced or removed by the provider, limiting reproducibility of the results.

### 5.3 Datasets scope and generalizability

Our evaluation is limited to a set of datasets from genomics and transcriptomics, selected for their accessibility and relevance. These datasets represent only a small subset of the computational biology landscape, and are solely focused on nucleotide sequence classification tasks. Computational biology ML tasks are much more varied, ranging from function or structure prediction, correlation of sequences and protein or transcript levels, value imputation, clustering, and many others. A future

direction for this field is the exploration of different types of datasets and tasks. We believe that using our method offers better chances of generalizability, as seen in the AGO2_CLASH_Hejret dataset that had an atypical structure. Our approach had produced working code 100% of the time, while no other approach managed to produce a single working model for this dataset.

### 5.4 Prompt engineering and evaluation bias

While we standardized user prompts to ensure fair comparisons, the iterative process of LLM-based development creates risks of unintentional overfitting. Iterative adjustments to hyperparameters, such as the number of loop iterations and temperature, or refinements of prompts based on observed performance can artificially inflate evaluation metrics. To mitigate this issue, we only used one dataset as a prototype (human_nontata_promoters), did not create per-dataset prompts, and used default hyperparameters where possible. All other datasets used the same prompt and hyperparameters that were never changed after testing. That said, it should be an important future task for an independent researcher to perform a benchmarking exercise in this field, ideally with never before published datasets.

## 6 Conclusion

The advancement of high-throughput -omics technologies presents substantial analytical challenges due to data volume and complexity. Here, we introduce Agentomics-ML, a fully autonomous agentbased system that can automate machine learning experimentation for -omics classification tasks. A significant contribution is Agentomics-ML’s high success rate (over 93%) in generating executable machine learning code and trained models, notably on complex datasets, where other benchmarked agentic systems failed to produce working code. Our system demonstrates superior generalization and operational success compared to zero-shot LLM code generation and other evaluated agentic frameworks.

Agentomics-ML operates via a predefined, iterative workflow, autonomously executing sequential stages including data exploration, representation, model architecture design, training, and inference script generation, primarily utilizing a bash shell interface for file system interaction and tools to write and execute python code. A key feature is its reflection loop, where training and validation metrics inform subsequent iterations, facilitating model refinement and ensuring the generation of reproducible artifacts. While state-of-the-art models developed by domain experts currently achieve superior absolute performance in most datasets, Agentomics-ML substantially reduces this disparity for fully autonomous systems and outperforms human state-of-the-art on one dataset. Moreover, the average cost of one agent run is less than 2$. Future work will focus on extending Agentomics-ML’s applicability to a broader array of biological data modalities and computational tasks. Agentomics-ML underscores the considerable potential of autonomous agent-based systems to advance data-driven discovery in molecular biology.

## References

Kelly Azevedo, Luigi Quaranta, Fabio Calefato, and Marcos Kalinowski. A multivocal literature review on the benefits and limitations of automated machine learning tools, 2024. URL https: //arxiv.org/abs/2401.11366.

Mahesh Kumar Bharti, Deepika Chandra, R.A. Siddique, K. Ranjan, and Pankaj Kumar. Recent advancement in high-throughput “omics” technologies, page 343–355. Elsevier, 2024. ISBN

9780443216251. doi: 10.1016/b978-0-443-21625-1.00023-3. URL http://dx.doi.org/10. 1016/B978-0-443-21625-1.00023-3.

Carlos Catania, Jorge Guerra, Juan Manuel Romero, Gabriel Caffaratti, and Martin Marchetta. Beyond random split for assessing statistical model performance, 2022. URL https://arxiv. org/abs/2209.03346.

Jun Shern Chan, Neil Chowdhury, Oliver Jaffe, James Aung, Dane Sherburn, Evan Mays, Giulio Starace, Kevin Liu, Leon Maksin, Tejal Patwardhan, Lilian Weng, and Aleksander Ma˛dry. Mlebench: Evaluating machine learning agents on machine learning engineering, 2025. URL https: //arxiv.org/abs/2410.07095.

Matthias Feurer, Katharina Eggensperger, Stefan Falkner, Marius Lindauer, and Frank Hutter. Autosklearn 2.0: hands-free automl via meta-learning. J. Mach. Learn. Res., 23(1), January 2022. ISSN 1532-4435.

Katarína Grešová, Vlastimil Martinek, David Cechák, Petr Šimeˇˇ cek, and Panagiotis Alexiou. Genomic benchmarks: a collection of datasets for genomic sequence classification. BMC Genomic Data, 24(1), May 2023. ISSN 2730-6844. doi: 10.1186/s12863-023-01123-8. URL http://dx.doi.org/10.1186/s12863-023-01123-8.

Sirui Hong, Yizhang Lin, Bang Liu, Bangbang Liu, Binhao Wu, Ceyao Zhang, Chenxing Wei, Danyang Li, Jiaqi Chen, Jiayi Zhang, Jinlin Wang, Li Zhang, Lingyao Zhang, Min Yang, Mingchen Zhuge, Taicheng Guo, Tuo Zhou, Wei Tao, Xiangru Tang, Xiangtao Lu, Xiawu Zheng, Xinbing Liang, Yaying Fei, Yuheng Cheng, Zhibin Gou, Zongze Xu, and Chenglin Wu. Data interpreter: An llm agent for data science, 2024a. URL https://arxiv.org/abs/2402.18679.

Sirui Hong, Mingchen Zhuge, Jonathan Chen, Xiawu Zheng, Yuheng Cheng, Jinlin Wang, Ceyao Zhang, Zili Wang, Steven Ka Shing Yau, Zijuan Lin, Liyang Zhou, Chenyu Ran, Lingfeng Xiao, Chenglin Wu, and Jürgen Schmidhuber. MetaGPT: Meta programming for a multi-agent collaborative framework. In The Twelfth International Conference on Learning Representations, 2024b. URL https://openreview.net/forum?id=VtmBAGCN7o.

Qian Huang, Jian Vora, Percy Liang, and Jure Leskovec. Mlagentbench: Evaluating language agents on machine learning experimentation, 2024a. URL https://arxiv.org/abs/2310.03302.

Xu Huang, Weiwen Liu, Xiaolong Chen, Xingmei Wang, Hao Wang, Defu Lian, Yasheng Wang, Ruiming Tang, and Enhong Chen. Understanding the planning of llm agents: A survey, 2024b. URL https://arxiv.org/abs/2402.02716.

Zhengyao Jiang, Dominik Schmidt, Dhruv Srikanth, Dixing Xu, Ian Kaplan, Deniss Jacenko, and Yuxiang Wu. Aide: Ai-driven exploration in the space of code, 2025. URL https://arxiv.org/ abs/2502.13138.

Lifeng Qiao, Peng Ye, Yuchen Ren, Weiqiang Bai, Chaoqi Liang, Xinzhu Ma, Nanqing Dong, and Wanli Ouyang. Model decides how to tokenize: Adaptive dna sequence tokenization with mxdna,

#### 2024. URL https://arxiv.org/abs/2412.13716.

Stephanie Sammut, Katarina Gresova, Dimosthenis Tzimotoudis, Eva Marsalkova, David Cechak, and Panagiotis Alexiou. mirbench: novel benchmark datasets for microrna binding site prediction that mitigate against prevalent microrna frequency class bias. bioRxiv, 2025. doi: 10.1101/ 2024.11.14.623628. URL https://www.biorxiv.org/content/early/2025/01/31/2024.

#### 11.14.623628.

Max Schubach, Matteo Re, Peter N. Robinson, and Giorgio Valentini. Imbalance-aware machine learning for predicting rare and common disease-associated non-coding variants. Scientific Reports, 7(1), June 2017. ISSN 2045-2322. doi: 10.1038/s41598-017-03011-5. URL http://dx.doi. org/10.1038/s41598-017-03011-5.

Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao. Reflexion: Language agents with verbal reinforcement learning, 2023. URL https://arxiv.org/abs/2303.11366.

Maojun Sun, Ruijian Han, Binyan Jiang, Houduo Qi, Defeng Sun, Yancheng Yuan, and Jian Huang. A survey on large language model-based agents for statistics and data science, 2024. URL https://arxiv.org/abs/2412.14222.

Yuan Sun, Qiurong Song, Xinning Gui, Fenglong Ma, and Ting Wang. Automl in the wild: Obstacles, workarounds, and expectations. In Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems, CHI ’23, page 1–15. ACM, April 2023. doi: 10.1145/3544548.3581082. URL http://dx.doi.org/10.1145/3544548.3581082.

Vishrut Thoutam and Dina Ellsworth. MSAMamba: Adapting subquadratic models to long-context DNA MSA analysis. In ICML 2024 Workshop on Theoretical Foundations of Foundation Models,

#### 2024. URL https://openreview.net/forum?id=PogdVDgGFT.

Maria A. Wörheide, Jan Krumsiek, Gabi Kastenmüller, and Matthias Arnold. Multi-omics integration in biomedical research – a metabolomics-centric review. Analytica Chimica Acta, 1141:144–162, January 2021. ISSN 0003-2670. doi: 10.1016/j.aca.2020.10.038. URL http://dx.doi.org/10. 1016/j.aca.2020.10.038.

Jian Xie, Kexun Zhang, Jiangjie Chen, Siyu Yuan, Kai Zhang, Yikai Zhang, Lei Li, and Yanghua Xiao. Revealing the barriers of language agents in planning, 2024. URL https://arxiv.org/ abs/2410.12409.

Chunming Xu and Scott A. Jackson. Machine learning and complex biological data. Genome Biology, 20(1), April 2019. ISSN 1474-760X. doi: 10.1186/s13059-019-1689-0. URL http: //dx.doi.org/10.1186/s13059-019-1689-0.

Tong Yu, Lei Cheng, Ruslan Khalitov, Erland Brandser Olsson, and Zhirong Yang. Self-distillation improves dna sequence inference, 2024a. URL https://arxiv.org/abs/2405.08538.

Ying Yu, Yuanbang Mai, Yuanting Zheng, and Leming Shi. Assessing and mitigating batch effects in large-scale omics studies. Genome Biology, 25(1), October 2024b. ISSN 1474-760X. doi: 10.1186/s13059-024-03401-9. URL http://dx.doi.org/10.1186/s13059-024-03401-9.

## A Supplementary Tables

- Table 3: Test set performance metrics for each dataset-method combination displaying mean value of

- 5 separate runs. Accuracy is used for all except AGO2 where average precision score is used. Best overall is marked as underlined and bold. Best LLM-based method is marked in bold.


Method AGO2 DE HEC HEE NTP OCRE Agentomics: gpt4_1 (no feedback) 0.698 0.673 0.698 0.796 0.881 0.758 Agentomics: gpt4_1 0.726 0.715 0.729 0.827 0.899 0.787 AIDE: gpt-4.1-2025-04-14 N/A N/A N/A N/A 0.905 0.757 DI: claude-3.7-sonnet N/A N/A 0.724 N/A 0.839 N/A DI: deepseek-chat N/A N/A N/A N/A 0.871 N/A DI: deepseek-r1 N/A N/A N/A N/A N/A N/A DI: llama-4-maverick N/A 0.5 N/A 0.738 0.801 N/A DI: gpt-4.1-2025-04-14 N/A N/A 0.5 0.706 0.872 N/A DI: qwen3-32b N/A N/A N/A N/A N/A N/A zero_shot: claude-3.7-sonnet N/A 0.650 0.728 0.864 0.901 N/A zero_shot: deepseek-chat N/A 0.680 0.681 0.797 0.882 0.639 zero_shot: deepseek-r1 N/A 0.700 0.621 0.765 0.874 0.458 zero_shot: llama-4-maverick N/A 0.661 N/A N/A N/A 0.651 zero_shot: gpt-4.1-2025-04-14 N/A 0.703 N/A N/A N/A N/A zero_shot: o4-mini N/A 0.694 0.719 0.800 0.868 0.609 zero_shot: qwen3-32b N/A N/A N/A 0.850 N/A 0.662

- Table 4: P-values for a t-test comparing Agentomics-ML with and without feedback mechanism. Dataset p_value

human_ocr_ensembl 0.022 AGO2_CLASH_Hejret2023 0.356 human_nontata_promoters 0.187 human_enhancers_cohn 0.011 drosophila_enhancers_stark 0.068 human_enhancers_ensembl 0.200

- Table 5: Test set performance metrics for each dataset-method combination displaying variance between the 5 separate runs. Accuracy is used for all except AGO2 where average precision score is used.


Method AGO2 DE HEC HEE NTP OCRE Agentomics: gpt4_1_no_feedback 0.030 0.036 0.030 0.039 0.014 0.019 Agentomics: gpt_1 0.033 0.019 0.016 0.045 0.023 0.023 AIDE: gpt-4.1 N/A N/A N/A N/A 0.021 N/A DI: claude-3.7-sonnet N/A N/A N/A N/A N/A N/A DI: deepseek-chat N/A N/A N/A N/A N/A N/A DI: deepseek-r1 N/A N/A N/A N/A N/A N/A DI: llama-4-maverick N/A N/A N/A N/A 0.103 N/A DI: gpt-4.1-2025-04-14 N/A N/A N/A 0.065 0.001 N/A DI: qwen3-32b N/A N/A N/A N/A N/A N/A zero_shot claude-3.7-sonnet N/A N/A N/A N/A N/A N/A zero_shot: deepseek-chat N/A N/A N/A 0.020 0.022 0.042 zero_shot: deepseek-r1 N/A 0.000 N/A 0.004 N/A N/A zero_shot: llama-4-maverick N/A N/A N/A N/A N/A N/A zero_shot: gpt-4.1-2025-04-14 N/A N/A N/A N/A N/A N/A zero_shot: o4-mini N/A 0.014 0.014 0.032 0.019 0.107 zero_shot: qwen3-32b N/A N/A N/A N/A N/A N/A

