https://doi.org/10.1038/s41586-024-07618-3

W

## Accelerated Article Preview

REVIE

# A Multimodal Generative AI Copilot for Human Pathology

P

Ming Y. Lu, Bowen Chen, Drew F. K. Williamson, Richard J. Chen, Melissa Zhao, Aaron K. Chow, Kenji Ikemura, Ahrong Kim, Dimitra Pouli, Ankush Patel, Amr Soliman, Chengkuan Chen, Tong Ding, Judy J. Wang, Georg Gerber, Ivy Liang, Long Phi Le, Anil V. Parwani, Luca L. Weishaupt & Faisal Mahmood

Received: 11 December 2023 Accepted: 28 May 2024 Accelerated Article Preview Published online xx xx xxxx Cite this article as: Lu, M. Y. et al. A Multimodal Generative AI Copilot for Human Pathology. Nature https://doi.org/ 10.1038/s41586-024-07618-3 (2024)

CLE

![image 1](Lu et al._2024_A multimodal generative AI copilot for human pathology_images/imageFile1.png)

This is a PDF file of a peer-reviewed paper that has been accepted for publication. Although unedited, the content has been subjected to preliminary formatting. Nature is providing this early version of the typeset paper as a service to our authors and readers. The text and figures will undergo copyediting and a proof review before the paper is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers apply.

RTI

A

D

RATE

CELE

C

A

Nature | www.nature.com

### A Multimodal Generative AI Copilot for Human Pathology

PREVIEW

Ming Y. Lu1,2,3,4,11, Bowen Chen1,2,11, Drew F. K. Williamson1,2,3,11, Richard J. Chen1,2,3, Melissa Zhao1,2, Aaron K. Chow5, Kenji Ikemura1,2, Ahrong Kim1,10, Dimitra Pouli1,2, Ankush Patel6, Amr Soliman5, Chengkuan Chen1, Tong Ding1,7, Judy J. Wang1, Georg Gerber1, Ivy Liang1,7, Long Phi Le2, Anil V. Parwani5, Luca L. Weishaupt1,8 , and Faisal Mahmood1,2,3,9†

- 1Department of Pathology, Brigham and Women’s Hospital, Harvard Medical School, Boston, MA, United States
- 2Department of Pathology, Massachusetts General Hospital, Harvard Medical School, Boston, MA, United States 3Cancer Program, Broad Institute of Harvard and MIT, Cambridge, MA, United States 4Electrical Engineering and Computer Science, Massachusetts Institute of Technology (MIT), Cambridge, MA, United States


- 5Department of Pathology, Wexner Medical Center, Ohio State University, Columbus, OH, United States
- 6Department of Laboratory Medicine and Pathology, Mayo Clinic, Rochester, MN, United States
- 7Harvard John A. Paulson School of Engineering and Applied Sciences, Harvard University, Cambridge, MA, United States
- 8Health Sciences and Technology, Harvard-MIT, Cambridge, MA, United States
- 9Harvard Data Science Initiative, Harvard University, Cambridge, MA, United States 10Department of Pathology, Pusan National University, South Korea 11These authors contributed equally: Ming Y. Lu, Bowen Chen, Drew F. K. Williamson †e-mail:faisalmahmood@bwh.harvard.edu


ARTICLE

The field of computational pathology[1, 2] has witnessed remarkable progress in the development of both task-specific predictive models and task-agnostic self-supervised vision encoders[3, 4]. However, despite the explosive growth of generative artificial intelligence (AI), there has been limited study on building general purpose, multimodal AI assistants and copilots[5] tailored to pathology. Here we present PathChat, a visionlanguage generalist AI assistant for human pathology. We build PathChat by adapting a foundational vision encoder for pathology, combining it with a pretrained large language model and finetuning the whole system on over 456,000 diverse visual language instructions consisting of 999,202 question-answer turns. We compare PathChat against several multimodal vision language AI assistants and GPT4V, which powers the commercially available multimodal general purpose AI assistant ChatGPT-4[7]. PathChat achieved state-of-theart performance on multiple-choice diagnostic questions from cases of diverse tissue origins and disease models. Furthermore, using open-ended questions and human expert evaluation, we found that overall PathChat produced more accurate and pathologist-preferable responses to diverse queries related to pathology. As an interactive and general vision-language AI Copilot that can flexibly handle both visual and natural language inputs, PathChat can potentially find impactful applications in pathology education, research, and human-in-the-loop clinical decision making.

ACCELERATED

##### Introduction

The field of computational pathology has witnessed a remarkable transformation in recent years, propelled by the convergence of several key trends including increased availability and institutional adoption of digital slide scanning, rapid progress in artificial intelligence (AI) research, increased accessibility of large datasets, and substantial highperformance computing resources[1, 2, 8]. With varying degrees of success, researchers have leveraged deep learning to address a diverse range of tasks, including cancer subtyping[9, 10] and grading[11, 12], metastasis detection[13], survival[14, 15, 16, 17, 18] and response-to-treatment prediction[19, 20], tumor site of origin prediction[21, 22], mutation prediction and biomarker screening[23, 24, 25], and more[26]. At the same time, general purpose vision encoder models[27], which are trained on vast datasets of unlabeled histopathology images and can serve as versatile task-agnostic model backbones[3, 4], are paving the way for further improvements across many tasks in computational pathology, both in performance and label efficiency.

PREVIEW

However, the aforementioned developments in computational pathology do not yet reflect the important roles of natural language in pathology – as a key to unlocking rich, diverse sources of accumulated human medical knowledge, a supervisory signal for model development, and a unified medium for facilitating intuitive interaction between powerful AI models and end users. Notably, in general machine learning, representative works[28, 29] demonstrated that largescale vision language representation learning can augment vision-only AI models with new capabilities including zeroshot image recognition and text-to-image retrieval. Depending on the architectural design and training data and objectives, visual language pretrained systems can also often be finetuned for tailored tasks ranging from visual question answering and image captioning to object detection and semantic segmentation. In medical imaging and computational pathology, researchers have recently begun to harness diverse sources[30, 31, 32, 33, 34] of paired biomedical images and captions or reports for visual language pretraining, including the development of CLIP[28]-like models tailored for specific domains such as pathology[31, 35, 36, 34] and radiology[37, 38, 39]. In computational pathology, a few works have shown promising zeroshot performance in select diagnostic and retrieval tasks[31, 35, 34], while other works also experimented with specialized models for biomedical visual question answering or captioning[40, 41, 42, 43, 44]. However, for pathologists, researchers using pathology image data, or pathology trainees alike, these models are not yet ready to serve as interactive companions (or copilots) that can follow diverse instructions and coherently and accurately answer complex open-ended questions in natural language.

ARTICLE

Following the rise of large language models[45, 46, 47, 48] (LLMs), rapid advances in multimodal large language models[49, 5, 50] (MLLMs) and the broader field of generative AI[51] are poised to open a new frontier for computational pathology, one which emphasizes natural language and human interaction as key components of AI model design and user experience, in addition to powerful visual processing capabilities. Multimodal generative AI products such as ChatGPT have demonstrated impressive capabilities on a wide range of routine, creative, as well as professional use cases[7, 52], including coding, writing, summarization, data analysis, question answering, translation, and even image generation, all while being accessible through an intuitive and interactive user interface. Though there have been attempts to investigate their performance on answering medicine-related queries, their capability to assist professionals and researchers in the highly specialized but important sub-field of anatomic pathology remains relatively unexplored[6, 53, 54, 55, 56, 57]. Yet, the potential applications of an interactive, multimodal AI copilot for pathology are immense. The ability to understand and respond to complex queries in natural language in theory could enable such a copilot for pathology to serve as a helpful companion across various stages of human-in-the-loop clinical decision making, education, and research. For instance, an AI copilot would be able to ingest a histopathology image, provide an initial assessment of the morphological appearance, and identify potential features of malignancy. Subsequently, the pathologist or trainee could provide additional context about the underlying case, such as clinical parameters of the patient and the tissue site, and ask the model to suggest a differential diagnosis. If deemed reasonable, the user could then request helpful suggestions for ancillary testing and immunohistochemical stains to narrow down the differential. Finally, the results of such tests could also be provided to the model to make a final deduction to arrive at the diagnosis. In research, a multimodal AI copilot that can summarize the morphological features of large cohorts of histopathology images would potentially enable automated quantification and interpretation of morphological markers in large data cohorts. In medical education, an accurate, on-demand interactive AI companion could help democratize access to expert-level guidance and training in pathology, thereby narrowing the gap between regional disparities in healthcare provision.

ACCELERATED

###### A multimodal generative AI copilot for human pathology

In this article, we develop PathChat, a multimodal generative AI copilot for human pathology powered by a custom, finetuned multimodal large language model (MLLM). To build a MLLM that can reason over both visual and natural language inputs, we begin with UNI[3], a state-of-the-art (SOTA) vision-only encoder pretrained on over 100 million histology image patches from over 100 thousand slides using self-supervised learning. We perform further vision

language pretraining on the UNI encoder with 1.18 million pathology image caption pairs to align its image representation space with that of pathology text[35]. The resulting vision encoder is subsequently connected to a 13 billion parameter, pretrained Llama 2 LLM[47] via the multimodal projector module to form the complete MLLM architecture (see PathChat model design and training section of Methods for more details). The MLLM is finally finetuned via a curated dataset of over 450 thousand instructions to build PathChat (Figure 1, Extended Data Figure 1), which can understand pathology images and text and respond to complex pathology-related queries. More information about data curation and model training can be found in PathChat dataset curation and PathChat model design and training section of Methods respectively, with additional details summarized in Supplementary Data Tables 1–4.

PREVIEW

We demonstrate the capabilities of PathChat in various applications including analysis of pathology cases from diverse organ sites and practices (Figures 2 and 3). Additionally, we curated a high quality open-ended pathology visual question answering benchmark suitable for evaluating the performance of multimodal large language models in pathology, which we curated with expert supervision (see an expert-curated pathology question-answering benchmark section of Methods for more details). We compare PathChat against both LLaVA[5], a state-of-the-art (SOTA) general domain open-source MLLM as well as LLaVA-Med[53], which has been tailored to the biomedical domain. We also compare against a SOTA commercial solution, ChatGPT-4 (powered by GPT4V), despite our model being significantly smaller and cheaper to serve.

ARTICLE

##### Results

Performance on multiple-choice diagnostic questions We began by assessing the capability of our PathChat MLLM to directly make a diagnosis based on histology images. For this purpose, a board-certified pathologist manually selected salient regions of interest (ROIs) from routine H&E diagnostic whole slide images (WSIs) from both the TCGA and our in-house pathology archive (both of which are completely withheld from model pretraining or finetuning). In total, the questions cover 54 diagnoses from 11 different major pathology practices and organ sites (Supplementary Data Tables 5 and 6). For each organ system, the pathologist selected a set of 10 possible answers that encompasses the correct answers for all questions within that organ system as well as other relatively common diagnoses within that organ system (Supplementary Data Table 7). For each question, we consider two evaluation strategies. In the first (image only setting), the model is presented with only the image and the multiple-choice question as input. In the second (image with clinical context), the model with presented with additional clinical context to closely mimic a real-world diagnostic workflow, in which information such as patient age, sex, clinical history, and radiology findings are included with the histology image for the clinical case. In both settings, the model is assessed for its ability to accurately select the ground truth diagnosis from the set of possible options. We provide an illustrative example of the complete model input in Figure 2a. On all cases (denoted as “Combined” in Figure 2b), we compare PathChat against LLaVA 1.5, a SOTA general purpose visual language chatbot assistant, as well as LLaVA-Med, a specialized version of LLaVA finetuned for answering biomedical related queries. Additionally, on the subset of 52 cases derived from publicly available WSIs (denoted as “PathQABenchPublic”), in addition to LLavA 1.5 and LLaVA-Med, we also compare against GPT4V, which powers ChatGPT4, one of the current best in class, vision capability enabled commercial AI assistant developed by OpenAI. All models were evaluated “as is” without any additional task-specific finetuning, consistent with the paradigm of zero-shot transfer.

ACCELERATED

In both evaluation settings (image only and image with clinical context), PathChat convincingly outperforms the open-source baselines LLaVA 1.5 and LLaVA-Med in terms of diagnostic accuracy (Figure 2a, Supplementary Data Tables 8–10). In the image only evaluation setting, PathChat scored a 78.1% accuracy (+52.4% vs. LLaVA 1.5 and

+63.8% vs. LLaVA-Med, p < 0.001 for both) on the full combined benchmark. In line with expectation, the performance of PathChat further improves to 89.5% accuracy (+39.0% vs. LLaVA 1.5 and +60.9% vs. LLaVA-Med, p < 0.001 for both) when additional useful clinical context is provided. Specifically, we note that the addition of clinical context consistently improves the accuracy of PathChat both on the private in-house cases (PathQABench-Private, +11.3%) and the public TCGA cases (PathQABench-Public, +11.6%). On the other hand, when only the clinical context is provided (i.e. the corresponding image is not shown to the model), performance is substantially lower (Extended Data Figure 2), which suggests PathChat derives substantial predictive power from visual features and does not rely on the clinical context alone. Together, these findings suggest that PathChat can effectively and flexibly leverage multimodal information for more accurate diagnosis of histology images by simply providing such additional non-visual information in plain natural language without specialized data processing.

Additionally, using PathQABench-Public, which only contains cases from the publicly available TCGA WSIs, we also compare our model against the GPT-4Vision (GPT4V) model. Given that we do not know the extent that GPT4V has been trained on histopathology-specific data from the internet, our use of manually curated ROIs from WSIs for

evaluation helps minimize the likelihood of data contamination and ensure proper assessment of its performance on histopathology images. It is worth noting that guardrails appear to have been implemented into GPT4V to sometimes prevent it from addressing queries that require examination of medical images, and it will instead inform the user that it cannot provide a pathology interpretation and instead to consult a medical professional. In such cases, we make a maximum of 2 additional submissions for the same query for a total of up to 3 attempts (see Evaluation of GPT4V of the Methods section for more details). Following this evaluation protocol, we successfully queried GPT4V for 47 out of 52 PathQABench-Public images when clinical context is included (28 out of 52 questions for the image only setting). An ultimately unsuccessful query was treated as incorrect since the response did not address the question. We observe that while GPT4V is more accurate than the open-source MLLMs when clinical context is provided, our domain-specific PathChat MLLM is consistently better in both evaluation settings (90.5% vs. 63.5% by GPT4V with clinical context, +26.9%; 78.8% vs. 25% by GPT4V for image only, +53.8%; p < 0.001 for both). While a part of this difference may be explained by GPT4V’s guardrails, for a more comprehensive and transparent assessment, we also reported performance on only the subset of questions that GPT4V successfully answered (Supplementary Data Table 11), and found PathChat to still consistently outperform GPT4V by a relatively large margin (+21.3%, p = 0.003 on 47 questions with clinical context; +32.2%, p = 0.014 on 28 questions for the image only setting).

PREVIEW

Performance on open-ended question answering Beyond multiple-choice diagnostic questions, it is valuable to assess the ability of PathChat and other MLLMs to generate coherent, reasonable, and clinically relevant responses to open-ended pathology-related inquiries (see an expert-curated pathology question-answering benchmark section of Methods). Based on cases from PathQABenchPublic, a board-certified anatomic pathologist carefully curated open-ended questions targeting a broad spectrum of topics including microscopic image description, histologic grade and differentiation status, risk factors, prognosis, treatment, diagnosis, immunohistochemical (IHC) tests, molecular alterations, and other further testing. Similar to the multiple-choice evaluation, to mimic the real-world use case of a pathology AI assistant, each question is provided to models as is, without requiring any additional model or task-specific finetuning.

ARTICLE

Given the more subjective nature of evaluating responses to open-ended questions, our evaluation consists of two components. First, a total of 7 expert pathologists each ranked (from best to worst, ties allowed) responses of different models for all questions (Figure 3a) based on their relevance to the question, correctness, and whether it is supplemented with correct explanation or reasoning in a succinct manner (see MLLM evaluation section of Methods for more details and Extended Data Figures 3–5 for illustrative examples of ranked model responses). Throughout the ranking process, the pathologists, who have not had prior interaction with each model, were also blinded to which model produced which response and the responses were additionally randomly shuffled for each question to further minimize potential bias towards specific models. This part of the evaluation is aimed at capturing a wide range of expert judgment (including subjective human preference) on the responses.

ACCELERATED

Overall, we find that PathChat produces on average more preferable, higher ranked responses than all other MLLMs tested. When considering head-to-head records (e.g. PathChat vs. GPT4V) for model ranking judged by a human expert, a “win” for PathChat on a question equates to PathChat’s response being ranked strictly higher than its counterpart when considering their relative ranking. Similarly, a “tie” for PathChat means the two models received the same rank while a “lose” means PathChat was ranked strictly lower. Against the runner up GPT4V, PathChat had a favorable median win rate of 56.5% across 7 independent pathologist evaluators compared to a median lose rate of just 22.3% and a median tie rate of 21.2% of questions (Figure 3b, Supplementary Data Tables 12 and 13). Once again, we observe an even larger performance gap in favor of PathChat as compared to LLaVA 1.5 (median win rate of 67.7%, median lose rate of 11.2%, and median tie rate of 21.5%) and LLaVA-Med (median win rate of 74.2%, median lose rate of 10.0%, and median tie rate of 15.4%).

Additionally, in order to also establish a more objective metric for each model’s accuracy on the open-ended questions, two board-certified pathologists independently reviewed responses for each question to assign a binary label of correct vs. incorrect for each model (while remaining blinded to each model’s identity). To mitigate the extent of subjectivity, the two pathologists then discussed all questions where they disagreed in their assessment, in an attempt to reach a consensus. For 235 out of 260 questions, a complete agreement was reached for all models and we use the consensus as the ground truth to compute the accuracy for each model. Specifically, PathChat scored an overall accuracy of 78.7% on the subset of open-ended questions for which pathologists were able to reach a consensus (Figure 3c, Supplementary Data Table 14), which corresponds to a 26.4% improvement (p < 0.001) compared to the accuracy score of 52.3% achieved by the runner up, GPT4V. Compared to the publicly available general purpose MLLM LLaVA 1.5 (accuracy of 29.8%), and the biomedicine-specialized MLLM LLaVA-Med (accuracy of 30.6%), the margin of improvement is even more substantial, at +48.9% and +48.1% respectively (p < 0.001 for both). We further report the accuracy of each model as assessed by each pathologist on the full set of questions (including the remaining questions for which a disagreement remained) in Extended Data Figure 6.

These results demonstrate that overall, PathChat generates both more accurate as well as more preferable responses to diverse pathology-related queries. Additionally, in order to better understand relative strengths and weaknesses of different models, we further analyze the performance of different models in various subgroups of questions (described in Supplementary Data Tables 15 and 16 with examples provided in Extended Data Figure 7). In particular, the “Microscopy” category includes questions that test the ability of models to generate accurate and detailed morphological descriptions of histology microscopy images and assess clinically relevant features such as tumor differentiation and grade. Questions in the “Diagnosis” category test the ability of the models to directly suggest a reasonable diagnosis based on the histology image available and relevant clinical context (unlike in multiple choice questions where possible choices are provided). “Clinical” questions test the ability to retrieve clinically relevant background knowledge about the disease in question, including risk factors, prognosis and treatment. “Ancillary testing” questions test the ability of models to suggest additional testing such as IHCs and molecular in order confirm a specific diagnosis or inform prognosis and treatment. We observed that while GPT4V is the runner up to PathChat overall, PathChat’s responses are especially superior to GPT4V’s in the categories that require examination of the histology image (i.e. “Microscopy” and “Diagnosis”), where the accuracy on the consensus subset is 73.3% and 78.5% for PathChat respectively vs. 22.8% and 31.6% for GPT4V (Figure 3d, Supplementary Data Tables 17–19). Similarly, median head-to-head win rate against GPT4V reaches 70.6% and 71.3% on the two categories of questions respectively, compared to the average median win-rate of 57.4%. Coupled with a median lose rate against GPT4V of only 13.8% on both these categories, the results imply that PathChat is better than or as good as GPT4V in around 86% of queries that emphasize histology image examination (Extended Data Figures 8 and 9, Supplementary Data Tables 20–27). On the flip side, we found PathChat to lag somewhat behind GPT4V on “Clinical” and “Ancillary Testing”, where, for the consensus subset, PathChat achieved a respectable 80.3% accuracy score on both categories compared to GPT4V’s higher scores of 88.5% and 89.5% on the two categories respectively. It is worth noting that while PathChat convincingly outperform GPT4V in accuracy on the “Microscopy” and “Diagnosis” categories according to the consensus (p < 0.001 for both, n = 101 and 79 respectively), we did not find any statistical significance (p > 0.05) for the higher accuracy of GPT4V on the “Clinical” and “Ancillary Testing” categories: p = 0.291 for Clinical (n = 61), and p = 0.153 for Ancillary Testing (n = 76) according to the consensus, suggesting there may not be a meaningful difference in the model performance on these categories between PathChat and the runner up GPT4V. Similarly, according to the more subjective ranking-based evaluation, we found PathChat was comparable to and in fact slightly more preferred by the panel of pathologists compared to GPT4V (a median of 44.1% win rate and 33.8% lose rate vs. GPT4V for “Clinical” and a median of 44.8% win rate and 35.6% lose rate for “Ancillary Testing”) on these same categories. We note that we included “Clinical” and “Ancillary testing” questions in order to comprehensively assess the capabilities of AI assistant models to address pathology related queries. However, these questions frequently do not require actual examination of the histology image but instead mostly aim to test the model’s ability to recall background knowledge relevant to pathology (e.g. “What specific molecular alterations are commonly found in disease X, and how might they influence the prognosis or therapeutic options?”). As a result, it is not too surprising that even general purpose multimodal AI assistants such as LLaVA 1.5 can often adequately answer questions in these categories and GPT4V may especially excel here as it is presumably much larger and trained on more extensive knowledge of the internet than open-source models and PathChat. Since these queries can often readily be addressed through conventional means of querying such as internet searches or consulting a reference manual, we focus on the “Microscopy” and “Diagnosis” categories as main indicators for the utility of different models as vision language assistants for Pathology, given that the aforementioned conventional means of querying do not fill the need for AIassisted visual question answering based on pathology images. Further breakdown of model performance by subcategories are included in Supplementary Data Tables 28–38. We note that despite the fact that our open-ended question answering benchmark is specific to the domain of pathology, its size is around double the 140 questions used in an earlier work[58] for human expert evaluation of LLMs’ ability to encode general clinical knowledge.

PREVIEW

ARTICLE

ACCELERATED

Lastly, we note that similar to our observation in the multiple-choice evaluation, presumably due to guardrails implemented by GPT4V, 38 of 260 questions submitted to GPT4V obviously refused to answer (a maximum number of 3 attempts were made for each question, see Evaluation of GPT4V of the Methods section for more details). Consistent with assessing other models, all GPT4V responses, regardless of whether successful or not, were blinded / shuffled and presented to pathologists for evaluation without special treatment. However, for transparency, we record the number of ultimately unsuccessful queries for GPT4V in each question category (Supplementary Data Table 39) and also report performance on only the subset of questions that GPT4V successfully answered (Supplementary Data Tables 40–64), which saw PathChat still outperforming GPT4V by a margin of over 20% in accuracy (e.g. 81.2% vs. 59.9% for 202 questions with consensus, p < 0.001).

Demonstration of PathChat on diverse use cases In addition to evaluating PathChat on multiple choice-style questions and open-ended question answering, we attempted to conceptualize and explore potential use cases for PathChat as an AI copilot specialized for Pathology. We observed that PathChat can analyze and describe notable morphological details in histology images, and answer questions that require background knowledge in pathology and general biomedicine in addition to the visual input alone (Figure 4a–d). The ability to analyze visual features and flexibly combine them with additional clinical context and medical knowledge (simply specified via natural language), and interpret them in the context of specific diagnostic guidelines (e.g. Gleason grading) out of the box opens PathChat to a much wider range of applications compared to task-specific visual question answering or image captioning models finetuned on relatively small datasets with a limited scope[40, 41, 42, 43, 44]. Additionally, the support for interactive, multi-turn conversation enables PathChat to potentially serve as a consultant for human-in-the-loop differential diagnosis, where an initial AI-assisted assessment can be followed up with additional clinical context, test results that are subsequently generated to narrow the differential (Figure 4e, Extended Data Figure 10). This may be especially valuable in cases that involve more lengthy, complex workups such as cancers of unknown primary (CUPs) and in low-resource settings where access to experienced pathologists may be limited.

PREVIEW

##### Discussion

ARTICLE

The field of computational pathology has witnessed substantial progress over the years in developing increasingly accurate, task-specific predictive models based on image and/or genomics data. For histology images specifically, there has recently been growing interest in building foundational task-agnostic vision encoders pretrained with large amounts of unlabeled images, which can provide robust feature embeddings for diverse supervised and unsupervised downstream workflows. However, the explosive growth in generative AI technology and specifically MLLMs, as exemplified by the likes of ChatGPT, begins to open up a possible new frontier for both computational pathology research and real-world applications to the clinical practice of pathology. Generalist AI models equipped with natural language understanding can utilize text as a unified medium to both flexibly specify user intent (i.e., in the form of a tailored prompt) and to produce outputs of various levels of expressiveness (i.e., from single-word to binary or multiple choice responses to coherent sentences with reasoning steps) that perform diverse tasks (e.g., summarization, classification, captioning, retrieval, question answering, and more). For the field of pathology specifically, such a model can in theory have applications in a wide range of scenarios across education and research as well as human-in-theloop clinical decision making.

ACCELERATED

In this work, we provide a proof of concept for building an AI copilot tailored to human pathology. We also provide, to our best knowledge, the most extensive evaluation of such technology in the field of computational pathology by comparing our model, PathChat, against both publicly-available models developed for general machine learning and the larger domain of biomedical sciences, as well as a SOTA commercial solution, GPT4V. We created PathQABench, a high quality, expert-curated benchmark that aims to assess a diverse range of capabilities relevant to the practice of anatomic pathology, including morphological examination of histology microscopic images, making diagnoses based on both histology and clinical context, assessment of tumor grade and differentiation, suggesting further IHC/molecular testing, and understanding of risk factors, prognosis and treatment of the underlying disease. We assessed these skills through a combination of multiple-choice style diagnostic questions as well as open-ended questions and human expert evaluation. In both evaluation settings, we found PathChat to compare favorably to the current best in class commercial solution GPT4V (presumably much larger and expensive to serve than PathChat), as well as substantially outperforming the publicly available MLLMs tested in diagnostic accuracy and quality of response. Additionally, we demonstrated that the support for interactive, multi-turn conversation may enable PathChat to handle additional use cases such as complex diagnostic workups. Considering our findings, we hope PathChat can potentially find impactful applications in pathology education, research, as well as human-in-the-loop clinical decision making as the technology matures over time.

Further alignment with human intent using techniques such as reinforcement learning from human feedback (RLHF)[45] may lower hallucination in MLLM-based AI assistant models in general and also help them capture certain nuances specific to the practice of pathology, such as when to request additional contextual information or test results when it is not possible or is difficult to rule out certain morphologically similar diseases based on H&E histology alone, or to seek clarification on institutional-specific guidelines for diagnosis and treatment. For real-world deployment, additional improvement and validation are likely also warranted to ensure that the model can consistently and correctly identify invalid queries (e.g., non-pathology related or nonsensical inputs) and refrain from answering with unexpected or erroneous outputs.

Future research will likely further enhance the capabilities of PathChat and MLLM-based AI assistants by adding support for inputting an entire gigapixel WSI or multiple WSIs. This may extend their usefulness in the diagnosis of challenging and borderline entities by supplying valuable context beyond pre-selected, representative ROIs.

Additionally, due to training on retrospectively collected large scale datasets that inevitably contain outdated information, these models may reflect the “scientific consensus of the past” rather than today[58]. For example, as medical terminology and guidelines evolve, a model response that references the outdated term “glioblastoma multiforme” may result in factual inaccuracies. Besides continual training with fresh, up-to-date knowledge[59], other research directions may involve curating specific instructions that make the model aware of changes in terminology and guidelines or using retrieval augmented generation[60] with a continuously updated knowledge database. Lastly, to make these tools more useful to pathologists and researchers, it could be worthwhile to consider explicitly supporting specialized tasks such as precise counting or localization of objects (e.g. “how many lymphocytes are in this image?” or “provide the exact bounding box coordinates of mitotic figures”) and building integration of PathChat-like AI assistants with tools such as digital slide viewers or electronic health records.

PREVIEW

##### Main References

- [1] Andrew H Song et al. “Artificial intelligence for digital and computational pathology”. In: Nature Reviews Bioengineering (2023), pp. 1–20.
- [2] Artem Shmatko et al. “Artificial intelligence in histopathology: enhancing cancer research and clinical oncology”. In: Nature Cancer 3.9 (2022), pp. 1026–1038.
- [3] Richard J Chen et al. “Towards a general-purpose foundation model for computational pathology”. In: Nature Medicine 30.3 (2024), pp. 850–862.
- [4] Ozan Ciga, Tony Xu, and Anne Louise Martel. “Self supervised contrastive learning for digital histopathology”. In: Machine Learning with Applications 7 (2022), p. 100198.
- [5] Haotian Liu et al. “Visual Instruction Tuning”. In: NeurIPS. 2023.
- [6] Yuxuan Sun et al. “PathAsst: A Generative Foundation AI Assistant Towards Artificial General Intelligence of Pathology”. In: Proceedings of the AAAI Conference on Artificial Intelligence. Vol. 38. 5. 2024, pp. 5034–5042.
- [7] Josh Achiam et al. “Gpt-4 technical report”. In: arXiv preprint arXiv:2303.08774 (2023).
- [8] Jana Lipkova et al. “Artificial intelligence for multimodal data integration in oncology”. In: Cancer cell 40.10

(2022), pp. 1095–1110.

- [9] Nicolas Coudray et al. “Classification and mutation prediction from non–small cell lung cancer histopathology images using deep learning”. In: Nature medicine 24.10 (2018), pp. 1559–1567.
- [10] Ming Y Lu et al. “Data-efficient and weakly supervised computational pathology on whole-slide images”. In: Nature biomedical engineering 5.6 (2021), pp. 555–570.
- [11] Wouter Bulten et al. “Automated deep-learning system for Gleason grading of prostate cancer using biopsies: a diagnostic study”. In: The Lancet Oncology 21.2 (2020), pp. 233–241.
- [12] Wouter Bulten et al. “Artificial intelligence for diagnosis and Gleason grading of prostate cancer: the PANDA challenge”. In: Nature medicine 28.1 (2022), pp. 154–163.
- [13] Babak Ehteshami Bejnordi et al. “Diagnostic assessment of deep learning algorithms for detection of lymph node metastases in women with breast cancer”. In: Jama 318.22 (2017), pp. 2199–2210.
- [14] Andrew H Beck et al. “Systematic analysis of breast cancer morphology uncovers stromal features associated with survival”. In: Science translational medicine 3.108 (2011).
- [15] Richard J Chen et al. “Pan-cancer integrative histology-genomic analysis via multimodal deep learning”. In: Cancer Cell 40.8 (2022), pp. 865–878.
- [16] Y. Lee, J.H. Park, S. Oh, et al. “Derivation of prognostic contextual histopathological features from whole-slide images of tumours via graph deep learning”. In: Nat. Biomed. Eng (2022).
- [17] Mohamed Amgad et al. “A population-level digital histologic biomarker for enhanced prognosis of invasive breast cancer”. In: Nature Medicine (2023), pp. 1–13.
- [18] Pooya Mobadersany et al. “Predicting cancer outcomes from histology and genomics using convolutional networks”. In: Proceedings of the National Academy of Sciences 115.13 (2018), E2970–E2979.
- [19] Stephen-John Sammut et al. “Multi-omic machine learning predictor of breast cancer therapy response”. In: Nature 601.7894 (2022), pp. 623–629.


ARTICLE

ACCELERATED

- [20] Zhi Huang et al. “Artificial intelligence reveals features associated with breast cancer neoadjuvant chemotherapy responses from multi-stain histopathologic images”. In: NPJ Precision Oncology 7.1 (2023), p. 14.
- [21] Ming Y Lu et al. “AI-based pathology predicts origins for cancers of unknown primary”. In: Nature 594.7861

(2021), pp. 106–110.

- [22] Fei Tian et al. “Prediction of tumor origin in cancers of unknown primary origin with cytology-based deep learning”. In: Nature Medicine (2024), pp. 1–11.
- [23] Jakob Nikolas Kather et al. “Pan-cancer image-based detection of clinically actionable genetic alterations”. In: Nature cancer 1.8 (2020), pp. 789–799.
- [24] Yu Fu et al. “Pan-cancer computational histopathology reveals mutations, tumor composition and prognosis”. In: Nature cancer 1.8 (2020), pp. 800–810.
- [25] Sophia J Wagner et al. “Transformer-based biomarker prediction from colorectal cancer histology: A large-scale multicentric study”. In: Cancer Cell 41.9 (2023), pp. 1650–1661.
- [26] Simon Graham et al. “One model is all you need: multi-task learning enables simultaneous histology image segmentation and classification”. In: Medical Image Analysis 83 (2023), p. 102685.
- [27] Maxime Oquab et al. “DINOv2: Learning Robust Visual Features without Supervision”. In: Transactions on Machine Learning Research (2023).
- [28] Alec Radford et al. “Learning transferable visual models from natural language supervision”. In: International conference on machine learning. PMLR. 2021, pp. 8748–8763.
- [29] Jiasen Lu et al. “Vilbert: Pretraining task-agnostic visiolinguistic representations for vision-and-language tasks”. In: Advances in neural information processing systems 32 (2019).
- [30] Andrew J Schaumberg et al. “Interpretable multimodal deep learning for real-time pan-tissue pan-disease pathology search on social media”. In: Modern pathology 33.11 (2020), pp. 2169–2185.
- [31] Zhi Huang et al. “A visual–language foundation model for pathology image analysis using medical twitter”. In: Nature medicine 29.9 (2023), pp. 2307–2316.
- [32] Sheng Zhang et al. “BiomedCLIP: a multimodal biomedical foundation model pretrained from fifteen million scientific image-text pairs”. In: arXiv preprint arXiv:2303.00915 (2023).
- [33] Jevgenij Gamper and Nasir Rajpoot. “Multiple instance captioning: Learning representations from histopathology textbooks and articles”. In: Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 2021, pp. 16549–16559.
- [34] Wisdom Ikezogwo et al. “Quilt-1m: One million image-text pairs for histopathology”. In: Advances in Neural Information Processing Systems 36 (2024).
- [35] Ming Y Lu et al. “A visual-language foundation model for computational pathology”. In: Nature Medicine 30.3

(2024), pp. 863–874.

- [36] Ming Y Lu et al. “Visual Language Pretrained Multiple Instance Zero-Shot Transfer for Histopathology Images”. In: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2023, pp. 19764– 19775.
- [37] Ekin Tiu et al. “Expert-level detection of pathologies from unannotated chest X-ray images via self-supervised learning”. In: Nature Biomedical Engineering 6.12 (2022), pp. 1399–1406.
- [38] Yuhao Zhang et al. “Contrastive learning of medical visual representations from paired images and text”. In: Machine Learning for Healthcare Conference. PMLR. 2022, pp. 2–25.
- [39] Benedikt Boecking et al. “Making the most of text semantics to improve biomedical vision–language processing”. In: European conference on computer vision. Springer. 2022, pp. 1–21.
- [40] Heyu Zhang et al. “PathNarratives: Data annotation for pathological human-AI collaborative diagnosis”. In: Frontiers in Medicine 9 (2023), p. 1070072.
- [41] Masayuki Tsuneki and Fahdi Kanavati. “Inference of captions from histopathological patches”. In: International Conference on Medical Imaging with Deep Learning. PMLR. 2022, pp. 1235–1250.
- [42] Renyu Zhang et al. “Evaluating and interpreting caption prediction for histopathology images”. In: Machine Learning for Healthcare Conference. PMLR. 2020, pp. 418–435.


PREVIEW

ARTICLE

ACCELERATED

- [43] Usman Naseem, Matloob Khushi, and Jinman Kim. “Vision-language transformer for interpretable pathology visual question answering”. In: IEEE Journal of Biomedical and Health Informatics 27.4 (2022), pp. 1681–1690.
- [44] Xuehai He. “Towards Visual Question Answering on Pathology Images.” In: Proceedings of the 59th annual meeting of the association for computational linguistics and the 11th international joint conference on natural language processing. Vol. 2. 2021.
- [45] Long Ouyang et al. “Training language models to follow instructions with human feedback”. In: Advances in Neural Information Processing Systems 35 (2022), pp. 27730–27744.
- [46] Tom Brown et al. “Language models are few-shot learners”. In: Advances in neural information processing systems 33 (2020), pp. 1877–1901.
- [47] Hugo Touvron et al. “Llama 2: Open foundation and fine-tuned chat models”. In: arXiv preprint arXiv:2307.09288

(2023).

- [48] Aakanksha Chowdhery et al. “Palm: Scaling language modeling with pathways”. In: Journal of Machine Learning Research 24.240 (2023), pp. 1–113.
- [49] Chunyuan Li et al. “Multimodal foundation models: From specialists to general-purpose assistants”. In: arXiv preprint arXiv:2309.10020 (2023).
- [50] Jean-Baptiste Alayrac et al. “Flamingo: a visual language model for few-shot learning”. In: Advances in Neural Information Processing Systems 35 (2022), pp. 23716–23736.
- [51] Michael Moor et al. “Foundation models for generalist medical artificial intelligence”. In: Nature 616.7956 (2023), pp. 259–265.
- [52] S´ebastien Bubeck et al. “Sparks of artificial general intelligence: Early experiments with gpt-4”. In: arXiv preprint arXiv:2303.12712 (2023).
- [53] Chunyuan Li et al. “Llava-med: Training a large language-and-vision assistant for biomedicine in one day”. In: Advances in Neural Information Processing Systems 36 (2024).
- [54] Tao Tu et al. “Towards generalist biomedical ai”. In: NEJM AI 1.3 (2024), AIoa2300138.
- [55] Chaoyi Wu et al. “Can gpt-4v (ision) serve medical applications? case studies on gpt-4v for multimodal medical diagnosis”. In: arXiv preprint arXiv:2310.09909 (2023).
- [56] Ming Liang Oon et al. “Bridging bytes and biopsies: A comparative analysis of ChatGPT and histopathologists in pathology diagnosis and collaborative potential”. In: Histopathology (2023).
- [57] Mehmet Saygin Seyfioglu et al. “Quilt-LLaVA: Visual Instruction Tuning by Extracting Localized Narratives from Open-Source Histopathology Videos”. In: arXiv preprint arXiv:2312.04746 (2023).
- [58] Karan Singhal et al. “Large language models encode clinical knowledge”. In: Nature 620.7972 (2023), pp. 172– 180.
- [59] Xisen Jin et al. “Lifelong Pretraining: Continually Adapting Language Models to Emerging Corpora”. In: Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies. 2022, pp. 4764–4780.
- [60] Patrick Lewis et al. “Retrieval-augmented generation for knowledge-intensive nlp tasks”. In: Advances in Neural Information Processing Systems 33 (2020), pp. 9459–9474.


PREVIEW

ARTICLE

ACCELERATED

##### Online Methods

PathChat dataset curation We curated a dataset of 456,916 instructions with a total of 999,202 question answer turns for training PathChat to respond to pathology-specific queries. The instructions are roughly categorized by “conversation” (n = 132,563), “description” (n = 168,440), “multiple choice” (n = 42,445), “free response” (n = 21,686), “textonly” (n = 83,232) and “guardrail” (n = 8,550). An illustrative example of each category is shown in Extended Data Figure 1. Mass General Brigham Institutional Review Board approved the retrospective analysis of pathology images and corresponding reports. No sample size calculations were performed. All data were deidentified prior to To ensure PathChat can generalize to a diverse range of instructions, the data encompasses several different instruction formats, including open-ended multi-turn dialogue, detailed image

description, short-answer questions, multiple choice questions, and textonly questions. A diverse set of data sources were used to generate the instruction dataset, spanning image captions, educational articles from PubMed Open Access (PMC-OA), pathology case reports and regions of interests extracted from WSIs, which were sourced from multiple institutions. Data from the TCGA was not used for training and were held out as part of our downstream evaluation. Data filtering was performed for each source individually to ensure quality and relevance for training a pathology-specific vision language assistant. Examples of frequently used heuristics for filtering include the removal of image captions that are overly short (e.g. < 12 words) or uninformative and overly generic (e.g. “An H&E image of tumor.”). We also removed captions or passages related to animal pathology (keywords include: “rat”, “pig”, etc.) and experimental studies (keywords include: “experimental”, “positive control”, etc.) using regex pattern matching. Lastly, we include basic guardrail instruction examples, where given image-specific instructions such as “Describe this histology image of a lung mass” when no image is provided, the model is expected to output the response of “Sorry, I cannot assist you since you have not uploaded any image.” Additionally, when given an image not related to pathology (sampled from MS COCO[61]), the model is trained to output “Sorry I can only assist you with queries related to pathology.” For some unstructured data formats, we prompt open-source general purpose LLMs[46, 62] to structure the original source text into a structured format automatically. Instructions were then manually created from the structured data with continual input from several board-certified pathologists. The Mass General Brigham institutional review board approved the retrospective analysis of pathology slides and corresponding pathology reports. All pathology images were de-identified before computational analysis and model development.

PREVIEW

ARTICLE

PathChat model design and training Compared to text-only large language models (LLMs), a multimodal large language model (MLLM) is trained to understand and respond to user instructions in the form of natural language queries that may additionally contain inputs from other modalities such as images. The support for multi-modality is essential for the domain of histopathology since examining and interpreting visual information in high resolution microscopic images (in conjunction with other clinical information) remains the cornerstone of the discipline and extends to many aspects of disease diagnosis and management in modern medicine.

Inspired by LLaVA[5, 63], our MLLM, PathChat, consists of three key components: the vision encoder, the multimodal projector module and the large language model. The vision encoder is responsible for encoding the image from the original high-dimensional RGB pixel space into a low-dimensional feature representation suitable for processing by the downstream modules. The multimodal projector connects the outputs of the vision encoder to the large language model (LLM) by projecting the visual tokens to the same dimension as the LLM’s embedding space for text tokens. The LLM takes the natural language instruction as input (after it has been tokenized by a tokenizer), combines the embedded text tokens and the image token output from the multimodal projector to form the full sequence of input tokens, and predicts the desirable response via auto-regressive next word prediction. The produced response is finally decoded by the tokenizer back into natural language and presented to the end user.

ACCELERATED

For the LLM, we adopt the 13 billion parameter variant from the widely used Meta Llama 2[47] family of state of the art open-source LLMs, which is a decoder-only transformer-based auto-regressive language model with 40 Transformer layers, each with 40 attention heads, an embedding dimension of 5,120, a hidden dimension of 13,824 and uses rotary positional encodings, natively supporting a maximum context length of 4,096. Similar to LLaVa 1.5, we use a vision encoder based on the standard ViT-Large (ViT-L) architecture consisting of 24 Transformer multi-headed attention blocks, each with 16 attention heads, an embedding dimension of 1,024 and a feed-forward hidden dimension of 4,096. The token size is 16 × 16 and we add learned absolute positional encoding to each token. The multimodal projector consists of an attention pooling layer followed by a 2-layer multi-layer perceptron (MLP). The attention pooling layer (also known as a Perceiver Resampler in some works[50, 64, 65]) uses a set of 128 learned latent queries and multiheaded cross-attention to reduce the last layer feature map of the encoder backbone into a fixed length sequence of image tokens with an initial dimension of 768 for increased training and inference efficiency, as well as to prevent the total sequence length of tokens from potentially exceeding the context window size of the LLM. The subsequent MLP follows the design used in LLava 1.5, and consists of a single hidden layer and GeLU activation, projecting the image tokens up to the embedding dimension of the LLM (i.e., 5,120 for the Llama 2 13B model). We initialize weights of the vision encoder backbone from UNI[3], a SOTA vision-only SSL-pretrained general purpose encoder for H&E pathology and continue finetuning the encoder backbone together with the attention pooling module on an expanded dataset of 1.18 paired images and captions from CONCH[35] and the CoCa visual language pretraining recipe[66](see Supplementary Data Table 1 for detailed hyperparameters).

We follow the MLLM training recipe of LLaVa 1.5, which involves two stages of training. In the first, pretraining stage, the LLM weights are kept frozen and only the multimodal projector receives parameter updates to learn a

suitable projection from the space of image tokens to the shared embedding space of the text tokens used by the LLM. For this simple purpose, the MLLM is supervised to simply predict the caption corresponding each image using roughly 100K image-caption pairs sampled from our previous dataset[35], without needing to use any curated instruction data. In the second, instruction finetuning stage, both the LLM and projector are trained end-to-end to generate responses to diverse instructions that include both natural language and visual inputs, as described in the Dataset curation section. Specifically, given an instruction Xinstruct, the reference answer Xans and the image Ximg, each represented as a sequence of tokenized inputs, we maximize the likelihood of each token in Xans, indexed by 1,...,L, under the chatbot (viewed as an autoregressive language model):

PREVIEW

𝐿𝐿

𝐿𝐿𝑐𝑐𝑐𝑐𝑐𝑐(𝜃𝜃𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝,𝜃𝜃𝑙𝑙𝑙𝑙𝑙𝑙) =

𝑙𝑙𝑝𝑝𝑙𝑙 𝑙𝑙𝑝𝑝𝑙𝑙 𝑝𝑝( 𝑋𝑋𝑎𝑎𝑎𝑎𝑎𝑎,𝑖𝑖| 𝑋𝑋𝑎𝑎𝑎𝑎𝑎𝑎,1: 𝑖𝑖 − 1,𝑋𝑋𝑖𝑖𝑎𝑎𝑎𝑎𝑝𝑝𝑝𝑝𝑖𝑖𝑝𝑝𝑝𝑝,𝑋𝑋𝑖𝑖𝑙𝑙𝑙𝑙;𝜃𝜃𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝,𝜃𝜃𝑙𝑙𝑙𝑙𝑙𝑙)

𝑖𝑖=1

This instruction tuning objective easily extends to multi-turn instruction data by conditioning on all previous turns of instruction and reference answer. For instructions where there is no image present, Ximg is not defined and removed from the conditioning sequence. Similarly, if multiple images accompany a given instruction, we simply concatenate their respective image tokens, with the newline (“\n”) token inserted in-between as a separator, and treat the full sequence as Ximg. Both pretraining and finetuning were performed using an 8 × NVIDIA A100 80GB GPU node. We refer readers to Supplementary Data Tables 2 and 3 for detailed hyperparameters used in the training process.

ARTICLE

An expert-curated pathology question-answering benchmark The evaluation of powerful multimodal visual language AI models in histopathology is an outstanding challenge, and there is currently a lack of publicly available, high quality, expert curated, histopathology-centric QA benchmark to the best of our knowledge. One possible candidate is PathVQA[44], which has been used in the literature to demonstrate and evaluate the pathology image understanding capabilities of various AI models. However, our manual audit revealed numerous types of low-quality examples in the benchmark, likely due to the lack of expert review and the automated nature of the data curation workflow used by PathVQA. As motivated, we curate a new high quality QA benchmark suitable for evaluating cutting-edge multimodal large language models for pathology, described in detail below.

To evaluate PathChat, we curated a QA benchmark, named PathQABench, using high resolution, representative image ROIs hand-selected by a board certified pathologist from 105 H&E WSI cases using the open-source QuPath digital viewer [67]. These cases have been held-out from all stages of training of PathChat. Of the 105 image ROIs, 53 ROIs are curated from private sources in-house at the Brigham & Women’s Hospital for the study, while the other 52 ROIs are selected from WSIs in the public TCGA repository. In total, the WSIs cover 11 tissue sites and 54 diagnoses (see Supplementary Data Tables 5 and 6). This design choice enables us to use the subset of questions based on publicly available WSIs, referred to as PathQABench-Public, to evaluate the SOTA commercial solution GPT4V (powering ChatGPT-4 with vision capabilities) via API requests, without risk of violating institutional guidelines for handling patient data. Accordingly, the subset of questions based on private WSIs, referred to as PathQABenchPrivate, are only used to evaluate other publicly available MLLM solutions that we can run locally inside the hospital without transmitting the data to an external server. To select the ROIs, the board-certified pathologist manually reviewed WSIs related to each diagnosis and distilled a single ROI for each WSI wherein relevant morphologic features of the diagnosis were evident. The diagnosis from these WSIs was then transferred to that of the image ROIs and subsequently used in the evaluation, both for the open-ended questions and the multiple choice questions. These diagnoses were made originally by separate pathologists who had examined the cases clinically, with full access to any additional slides in the case and the patient’s medical record, and were able to order and interpret IHC as required to work-up the case. To accommodate the diversity of diagnoses included in our evaluation, the selected ROIs vary in magnification and dimension. Across all of PathQABench, the selected magnifications of the ROIs range from 3× to 34.4× with a median of 13.3×. The widths vary from 859px to 2388px with a median of 1201px while the heights vary from 861px to 2390px with a median of 1191px. Next, for each case, the pathologist invents a short clinical summary statement based on the ground truth diagnosis, which includes an appropriately devised patient age, sex and clinical symptoms and radiology findings where applicable. The summary statement is referred to as the clinical context for the corresponding case henceforth. An example of clinical context is shown in Figure 2a. We then created both closeended multiple choice style diagnostic questions as well as open-ended questions that aim to assess the models capabilities in assisting with diverse pathology-related queries, which cover a range of topics that include but not limited to just diagnosis (Extended Data Figure 7, Supplementary Data Table 15).

ACCELERATED

A total of 105 multiple choice questions are created using the salient ROIs (one question per ROI). In the multiple choice-style question evaluation setting, for each organ system, a board-certified pathologist selected a set of 10 possible answers that encompasses the correct answers for all questions within that organ system as well as other

relatively common diagnoses within that organ system (Supplementary Data Table 7). For each multiple choice question, we consider two evaluation strategies. In the first image-only setting, the model is presented with only the image and the multiple choice question as input. In the second, image + clinical context setting that is designed to more closely mimic a real-world diagnostic workflow, the clinical context is additionally provided together with the histology image. In both settings, the model is assessed based on its ability to accurately select the ground truth diagnosis from the set of possible options.

PREVIEW

In the open-ended question answering evaluation setting, we use the 52 cases from PathQABench-Public to curate 5 questions per case for a total of 260 questions. The questions can be categorized broadly under “Microscopy”, “Diagnosis”, “Clinical”, and “Ancillary testing”, as described in Supplementary Data Table 15. The “Microscopy” and “Diagnosis” questions in particular focus on targeting diagnosis and morphological examination using the histology images and additional relevant context (where applicable), which are essential skills for the practice of anatomic pathology. On the other hand, “Clinical”, and “Ancillary testing” are often text-only questions that do not require visual examination of the image to answer, covering topics such as how to use IHCs to confirm the diagnosis and background knowledge pertaining to the underlying condition. We note that despite the fact that our open-ended question answering benchmark is specific to the domain of pathology, its size is substantially larger than the 140 questions used in an earlier work[58] for human expert evaluation of LLMs’ ability to encode general clinical knowledge.

ARTICLE

MLLM evaluation We compare PathChat against the general purpose SOTA MLLM LLaVA 1.5[63] as well as the medically-focused MLLM LLaVA-Med[53] using the full PathQABench dataset, and only evaluate the performance of GPT4V on cases from PathQABench-Public. The precise pretrained checkpoints for these models are specified in the Code availability section and the reporting summary. We use the default image processor implemented by each model and use greedy decoding during inference time when possible (not currently supported for the GPT4V API where we instead used the default arguments set by OpenAI). The evaluation of GPT4V also requires a more involved protocol due to guardrails implemented by OpenAI, which we detail in the next section (Evaluation of GPT4V). For all models, the maximum length of each generated response is capped to 1,024 new tokens generated.

For multiple choice questions, we observed that both PathChat, LLaVA 1.5 and GPT4V can output the predicted choice in a consistent and desirable format (e.g. “A” or “A. Lung adenocarcinoma”) which can be directly used in our evaluation pipeline to compute the accuracy score. However, we found LLaVA-Med could not follow the instruction to answer in a concise and consistent format appropriate for multiple choice questions and instead would always output a full sentence. Therefore, for LLaVA-Med, a board-certified pathologist first manually reviewed each model response, extracted the predicted diagnosis, assessed its correctness against the ground truth and then computed the accuracy score.

ACCELERATED

For the open-ended questions, we gather the prediction for each model and present them to a panel of 7 pathologists for ranking-based human expert evaluation. For each question, when the model responses are presented, their order is randomly shuffled and the pathologist is blinded to which model produced which response. The responses were ranked based on, in order of importance, 1. prompt following (whether the response correctly addressed the instruction), 2. completeness of the answer, 3. succinctness and 4. use of accepted pathology terminology. Ties of two (or more) responses were allowed. This part of the evaluation is aimed at capturing a wide range of expert judgment (including subjective human preference) on the responses. The model responses on all open-ended questions can be viewed in Supplementary Materials.

Additionally, we attempt to assign a more objective binary correct vs. incorrect outcome for each response. For this task, we first asked two board-certified pathologists to independently assess each response to each question (in terms of correct vs. incorrect for each model), where both pathologists were blinded to which model produced which response. For questions with a single best answer (e.g., “What is the most likely diagnosis?”), the responses were labeled as incorrect if the single best answer was not provided. For open ended questions (e.g., “What IHC stains would be useful in working up a glioblastoma?”), responses were labeled as incorrect if any portion of the response was hallucinated or if the response did not answer the question at all. Correct and incorrect labels were mutually exclusive and every response was labeled as correct or incorrect. Overall, across all models and all questions, the two experts agreed 92.6% of the time in their assessment with a corresponding Cohen’s kappa score of 0.852, indicating substantial inter-observer agreement, which is expected given the more objective nature of this part of the evaluation. To establish a consensus, we further asked the two experts to discuss their assessments for questions on which they disagreed originally. Following this discussion, they ultimately agreed completely on 235 of the 260 questions for all models. In the results section, we report the performance on this subset of questions where a consensus was reached (using the consensus as the ground truth) as well as report the performance according to each individual expert’s assessment for all questions.

Evaluation of GPT4V Evaluation of GPT4V was performed using the official API access provided by OpenAI. All API calls were made during February 2024 for gpt-4-vision-preview (the default, most up-to-date vision-enabled GPT-4 model available at the time of the study). We observed that guardrails appear to have been implemented into GPT4V to often prevent it from addressing queries that require examination of histopathology images. In such instances, it may inform the user that it cannot provide an interpretation of the pathology image and he or she should instead consult a trained medical professional. Queries for which the response returned by GPT4V obviously refused to address the given instructions were deemed “unsuccessful”. In such instances, we make a maximum of 2 additional re-submissions for the same query up to a total of 3 attempts. Following this evaluation protocol, we recorded 28 out of 52 successful queries in the multiple choice diagnostic assessment evaluation of PathQABench-Public cases when no additional clinical context is provided as part of each question while 47 out of 52 queries were eventually successful when the clinical context is included. Using an analogous protocol, in the open-ended QA evaluation section of PathQABench-Public, we counted 222 out of 260 successful queries. All final responses, regardless of successful or unsuccessful were presented to pathologists for evaluation without special treatment and subjected to the same blinding and shuffling protocol as for other models (see MLLM evaluation). A breakdown of successful queries by category is provided in Supplementary Data Table 39.

PREVIEW

ARTICLE

Statistical analysis We used nonparametric bootstrapping (n = 1,000 replicates) to estimate 95% confidence intervals for reported metrics. Observed differences in performance for a pair of models were tested for statistical significance via a two-sided paired permutation test (n = 1,000 permutations), with the null hypothesis being there is no difference in the performance of the two models. In each permutation, independent pairs of prediction outcomes of the two models are randomly swapped to obtain a new difference in model performance. The p-value corresponds to the proportion of differences in model performance with a greater absolute value than the observed difference.

Computing hardware and software We used Python (version 3.10.13) for all experiments and analyses in the study. For all model training, we used 8×80GB NVIDIA A100 GPUs configured for multi-GPU training using the popular open-source deep learning framework PyTorch (version 2.0.1, CUDA 11.8). All inference jobs were performed using 24GB NVIDIA 3090 GPUs. We use the implementation of MLLM training and inference provided by LLaVA (version 1.1.3) and incorporate our own custom vision encoder and multimodal projector implemented in Timm (version 0.9.2) and Pytorch. Pillow (version 10.1.0) is used for image processing. Flash Attention (version 2.3.3) and DeepSpeed (version 0.9.5) were used to enable accelerated training of PathChat MLLM. We used images from PathQABench and other real world cases not used for model training. Matplotlib (version 3.7.1) and Seaborn (version 0.12.2) were used to create plots and figures. Other miscellaneous libraries used are listed in the Reporting Summary. For training, UNI, the pretrained foundational vision encoder was trained for 32 hours on 32 80GB NVIDIA A100 GPUs in a 4 node (8 GPUs per node) distributed setup. The vision encoder used in PathChat is finetuned from UNI using a single node of 8 80GB NVIDIA A100 GPUs for 21.5 hours. Lastly, the combined system of PathChat (including the vision encoder, the multimodal projector and the large language model) are jointly trained for a total of 17 hours and 18 minutes (includes both pretraining and finetuning) on a single node of 8 80GB NVIDIA A100 GPUs to produce the final model. For inference, the PathChat model is run on 2 24GB NVIDIA RTX 3090 GPUs which yielded an average time of 9.75s (std: 7.71s) per response on the 260 open-ended questions.

ACCELERATED

Data availability The PubMed Central-OA dataset can be accessed from the NIH PubMed Central website (https://www.ncbi.nlm.nih.gov/pmc/tools/openftlist/). The TCGA WSIs and associated clinical metadata are available from the NIH genomic data commons (https://portal.gdc.cancer.gov ). The curated PathQABench-Public benchmark is released for research use and can be accessed through: https://github.com/fedshyvana/pathology_mllm_training. Patient data used in this project was curated with institutional permission through IRB approval for the current study and thus cannot be made publicly available in compliance with patient privacy obligations. All requests for processed data curated internally will be evaluated based on institutional and departmental policies to determine whether the data requested is subject to intellectual property or patient privacy obligations. Data that can be transferred will require a material or data transfer agreement between the institutions and will limit the utility of the data to non-commercial academic research purposes. The exact timeline will depend on the execution of such agreements. Please email all requests to the corresponding author (and also include M.Y.L., mlu16@bwh.harvard.edu)

Code availability Code used to train PathChat is made publicly available for non-commercial academic use and can be accessed here: https://github.com/fedshyvana/pathology_mllm_training[68]. We have documented all technical deep learning methods and software libraries used in the study, with hyperparameters detailed in Supplementary Data Table 1 – 3. Pathology MLLM weights trained on proprietary internal patient text data are subject to patient privacy and intellectual property obligations and cannot be made available. The code for LLaVA can be accessed here: https://github.com/haotianliu/LLaVA. The code for LLaVA-Med can be accessed here: https://github.com/microsoft/LLaVA-Med.

PREVIEW

![image 2](Lu et al._2024_A multimodal generative AI copilot for human pathology_images/imageFile2.png)

![image 3](Lu et al._2024_A multimodal generative AI copilot for human pathology_images/imageFile3.png)

Author contributions M.Y.L. and F.M. conceived the study and designed the experiments. M.Y.L., B.C., D.F.K.W, R.J.C., L.W., K.I., I.L., C.C., T.D. F.M. and J.J.W. performed data collection and processing. M.Y.L and B.C. developed the model. M.Y.L., B.C., D.F.K.W., M.Z., A.K.C., R.J.C., K.I., A.K., D.P., A.P., F.M., and A.S. performed experimental analysis and interpreted the results. R.J.C., K.I., G.G., I.L., T.D., L.P.L and A.V.P. provided feedback on the analysis. M.Y.L., B.C., D.F.K.W. and F.M. prepared the manuscript with input from all co-authors. F.M. supervised the research.

##### Acknowledgements

ARTICLE

This work was supported in part by the BWH president’s fund, BWH & MGH Pathology. R.J.C. was also supported by the NSF Graduate Fellowship. We thank Timothy Janicki, Richard Kenny, Abe Ahmed and the system administration staff at the MGB Enterprise Research Infrastructure & Services (ERIS) Research Computing Core for their dedicated support in providing and maintaining access to NVIDIA A100 computing resources. This work was supported by the Massachusetts Life Sciences Center infrastructure award.

##### Competing interests

A patent corresponding to this work has been filed by Mass General Brigham (Application 63/608,671). The tools, processes and models associated with PathChat have been exclusively licensed to ModellaAI . L.P.L., M.Y.L., R.J.C., B.C., F.M., D.F.K.W and J.J.W. hold equity interests in ModellaAI.

ACCELERATED

##### Figure Legends

- Figure 1

- Figure 1: Instruction-following dataset curation and PathChat overview. a. We curated the currently largest instruction finetuning dataset specialized for the domain of pathology, consisting of 456,916 instructions and corresponding responses covering various formats (e.g. multi-turn conversations, multiple-choice questions, short answers; see Extended Data Figure 1 for complete examples) from diverse sources. b. To build an MLLM-based vision language AI assistant that can reason over visual and natural language inputs, we begin with a SOTA vision-only self-supervised pretrained foundation encoder model, UNI, and perform further vision language pretraining analogous to CONCH. The resulting vision encoder is subsequently connected to a 13 billion parameter, pretrained Llama 2 LLM via a multimodal projector module (not shown) to form the complete MLLM architecture. The MLLM is finetuned via the curated instructionfollowing dataset to build PathChat, a visual language AI assistant specialized for human pathology. More details about data curation and model training can be found in PathChat dataset curation and PathChat model design and training section of Methods respectively. Scale bars are 200 µm.
- Figure 2


- Figure 2: Multiple choice evaluation of PathChat. a. Illustrative example of a multiple-choice style diagnostic question. The input always includes a salient histology image ROI selected by a board-certified anatomic pathologist and the instruction to select the most likely diagnosis from a set of possible choices. In the image + clinical context evaluation setting that is designed to more closely mimic a real-world diagnostic workflow, additional relevant clinical context (designed by the pathologist, shown in blue) is provided together with the histology image and prepended to the original question. b. Accuracy of MLLMs on multiple choice-style diagnostic questions. Combined (n = 105 questions), PathQABench-Public (n = 52), PathQABench-Private (n = 53). Note that we only compare against GPT4V on questions based on publicly available cases (PathQABench-Public). Error bars represent 95% confidence intervals, and the centers represent the computed accuracy. Scale bar is 200 µm.


- Figure 3

- Figure 3: Open response evaluation of PathChat and reader study from a panel of seven pathologists. a. Evaluation workflow for ranking model outputs for open-ended questions. A panel of 7 pathologists were recruited to assess the model responses on the 260 open-ended questions. The ordering of responses by the 4 AI assistant models were randomly shuffled for each question and each pathologist independently ranked them for all questions while blinded to which model produced which response (see MLLM evaluation of Methods for more details). b. Headto-head records on open-ended questions for PathChat v.s. other MLLMs evaluated by 7 pathologists independently. Win: PathChat is ranked higher than the model; Tie: PathChat is tied with the model in ranking; Lose: said model is ranked higher than PathChat. Vertical bars represent median win rate (dark green) across all 7 pathologists and median win+tie rate (light green). c. Accuracy of MLLMs on a subset (n = 235 questions) of open-ended questions for which two pathologist reached consensus after discussing independent evaluations of model responses. Error bars represent 95% confidence intervals, and the centers represent the computed accuracy. d. Accuracy on different categories of questions on the consensus subset. Microscopy (n = 101), Diagnosis (n = 79), Clinical (n = 61), Ancillary Testing (n = 76). Each question may belong to more than one category. Scale bar is 200 µm.
- Figure 4


- Figure 4: Exploring additional use cases of PathChat. Beyond evaluating PathChat on multiple choice-style questions and single turn open-ended question answering, we explore additional use cases and demonstrate examples that involve follow-up from users in the form of interactive, multi-turn conversations. These examples are illustrative in nature and intended to complement our quantitative evaluation on PathQABench. a PathChat can summarize key morphological features in the histology image and based on additional clinical context, can reasonably infer the primary origin of the tumor. b. PathChat is familiar with different cell markers and can help potentially guide IHC interpretations. c. PathChat understands and can attempt to follow well-known guidelines on tumor grading, in this case, the Gleason grade system for prostate adenocarcinoma. d. PathChat can describe tumor tissue and cell morphology, infer the diagnosis, and correctly suggest potential IHC findings grounded in relevant background knowledge about the suspected malignancy. e. PathChat can potentially be consulted to perform human-in-the-loop differential diagnosis that may require multiple rounds of IHC workup. Scale bars are 200 µm.


PREVIEW

ARTICLE

ACCELERATED

##### Extended Data Figure Legends

- Extended Data Figure 1

- Extended Data Figure 1: Examples of instructions for finetuning MLLM. An example of each of six different types of instructions to develop PathChat via instruction finetuning is illustrated. Bolded texts represent instructions provided to the model while italicized texts represent the reference outputs the model is expected to output during training. More details on dataset curation are provided in the PathChat dataset curation section of Methods. Scale bars are 200 µm.
- Extended Data Figure 2

- Extended Data Figure 2: Utilization of visual input and clinical context in multiple choice diagnostic questions. On the multiple choice diagnostic benchmarks (Combined, n = 105 questions; PathQABench-Private, n = 53; PathQABench-Public, n = 52), we investigated whether PathChat can effectively leverage both unstructured clinical context in the form of natural language as well as visual features in the image ROI instead of deriving its answer solely based on either input alone. In the context only setting, the clinical context is provided to the model but the image is not provided (see Figure 2a for an example multiple choice question that contains the clinical context, the choices, and the image). On the flip side, in the image only setting, the clinical context is not provided, and the model is asked to infer the correct diagnosis from the possible choices based solely on the image. We observed that PathChat achieves maximum performance when both clinical context and the image are provided. Error bars represent 95% confidence intervals, and the centers represent the computed accuracy.
- Extended Data Figure 3


- Extended Data Figure 3: Comparing model outputs on open-ended question answering, example 1. An example question in PathQABench-Public regarding uveal melanoma, for which the response by PathChat is ranked higher (considered more preferable by expert pathologists) than other models as it clearly, correctly, and fully addresses the




query. The other models give incorrect locations that the image is from, give an incorrect description of the image, or are so general as to be unhelpful. Scale bar is 200 µm.

- Extended Data Figure 4

- Extended Data Figure 4: Comparing model outputs on open-ended question answering, example 2. An example question in PathQABench-Public regarding glioblastoma for which the responses by all models were considered to be of roughly comparable quality by expert pathologists for all producing a reasonable and reasonably accurate response to the query, though with some variation between them. Scale bar is 200 µm.
- Extended Data Figure 5

- Extended Data Figure 5: Comparing model outputs on open-ended question answering, example 3. An example question in PathQABench-Public regarding lung adenocarcinoma where all four models performed poorly. None of the four models accurately describe the image or produce the correct diagnosis. Scale bar is 200 µm.
- Extended Data Figure 6


- Extended Data Figure 6: Individual pathologist evaluation of open response performance. a. Accuracy of MLLMs on open-ended questions (n = 260) as evaluated by two pathologists. See Figure 3c,d for accuracy on the subset of open-ended questions for which the two pathologists reached a consensus. See MLLM evaluation in Methods for details. Error bars represent 95% confidence intervals, and the centers represent the computed accuracy. b. Accuracy on different categories of questions as rated by two pathologists. Microscopy (n = 109), Diagnosis (n = 87), Clinical (n = 68), Ancillary Testing (n = 87). Each question may belong to more than one category.
- Extended Data Figure 7

- Extended Data Figure 7: Example questions from PathQABench-Public. PathQABench contains 260 high quality, expert reviewed, open-ended questions created using cases from PathQABench-Public, aimed at assessing a wide range of skills relevant to the practice of pathology. Each question is assigned one or more broad and sub-category based on the topics and skills that it aims to assess. The broad categories are “Microscopy”, “Diagnosis”, “Clinical” and “Ancillary testing”. A detailed description of each category is included in Supplementary Data Table 15. Scale bars are 200 µm.
- Extended Data Figure 8


- Extended Data Figure 8: Performance on PathQABench open-ended questions stratified by broad categories. We analyze the head-to-head performance of PathChat against other MLLMs in each broad category of questions evaluated by 7 pathologists independently. For each competing model (LLaVA 1.5, LLaVA-Med, GPT4V), we compute the win/tie/lose rate of PathChat against said model. Win (dark green): PathChat is ranked higher than the model; Tie (light green): PathChat is tied with the model in ranking; Lose (red): PathChat is ranked lower than the model. Vertical bars represent median win rate (dark green) across all 7 pathologists and median win+tie rate (light green).
- Extended Data Figure 9

- Extended Data Figure 9: Performance on PathQABench open-ended questions stratified by sub-categories. We further analyze the head-to-head performance of PathChat against other MLLMs in each sub-category of questions evaluated by 7 pathologists independently. For each competing model (LLaVA 1.5, LLaVA-Med, GPT4V), we compute the win/tie/lose rate of PathChat against said model. Win (dark green): PathChat is ranked higher than the model; Tie (light green): PathChat is tied with the model in ranking; Lose (red): PathChat is ranked lower than the model. Vertical bars represent median win rate (dark green) across all 7 pathologists and median win+tie rate (light green).
- Extended Data Figure 10


- Extended Data Figure 10: Example of human-in-the-loop differential diagnosis with PathChat in a case of cancer of unknown primary. PathChat can potentially be used to help the user perform human-in-the-loop differential diagnosis that combines a representative histology image, relevant clinical context, as well as follow-up IHC results. Note that in this example, PathChat erroneously implies that cervical cancers should be positive for CK7 and CK20 IHC when in fact, cervical cancers are usually positive for CK7 but negative for CK20. Scale bar is 200 µm.




PREVIEW

ARTICLE

ACCELERATED

##### Methods References

- [61] Tsung-Yi Lin et al. “Microsoft coco: Common objects in context”. In: Computer Vision–ECCV 2014: 13th European Conference, Zurich, Switzerland, September 6-12, 2014, Proceedings, Part V 13. Springer. 2014, pp. 740–755.
- [62] Jinze Bai et al. “Qwen technical report”. In: arXiv preprint arXiv:2309.16609 (2023).
- [63] Haotian Liu et al. “Improved baselines with visual instruction tuning”. In: arXiv preprint arXiv:2310.03744 (2023).
- [64] Yan Zeng et al. “What Matters in Training a GPT4-Style Language Model with Multimodal Inputs?” In: arXiv preprint arXiv:2307.02469 (2023).
- [65] Andrew Jaegle et al. “Perceiver: General perception with iterative attention”. In: International conference on machine learning. PMLR. 2021, pp. 4651–4664.
- [66] Jiahui Yu et al. “CoCa: Contrastive Captioners are Image-Text Foundation Models”. In: Transactions on Machine Learning Research (2022). issn: 2835-8856. url: https://openreview.net/forum?id=Ee277P3AYC.
- [67] Peter Bankhead et al. “QuPath: Open source software for digital pathology image analysis”. In: Scientific reports 7.1 (2017), pp. 1–7.
- [68] Ming Y. Lu et al. Code for pathology MLLM training. Version 0.1. Apr. 2024. url: https://github.com/ fedshyvana/pathology_mllm_training.


PREVIEW

ARTICLE

ACCELERATED

PREVIEW

###### a

ARTICLE

Instruction dataset (n=456,916)

![image 4](Lu et al._2024_A multimodal generative AI copilot for human pathology_images/imageFile4.png)

|Q:<br><br>A:<br><br>What is the key histopathological feature observed in the image of breast tissue?<br><br>In the image, the most notable histopathological feature is the presence of…<br><br>|![image 5](Lu et al._2024_A multimodal generative AI copilot for human pathology_images/imageFile5.png)|
|---|
|
|---|


|Q:<br><br>A:<br><br>Based on the image from the uterus. What is the most likely diagnosis? Uterine Leiomyoma<br><br>Uterine clear cell carcinoma<br><br>Uterine carcinosarcoma<br><br>Uterine carcinosarcoma<br><br>|![image 6](Lu et al._2024_A multimodal generative AI copilot for human pathology_images/imageFile6.png)|
|---|
|
|---|


|Q: A:<br><br>Q:<br><br>A:<br><br>Could you describe the key morphological features observed in Sertoli-Leydig cell tumors (SLCT)…? Sertoli-Leydig cell tumors exhibit…<br><br>…<br><br>How would you diﬀerentiate a SLCT with…? Immunohistochemistry plays a crucial role in distinguishing…|
|---|


WSI Regions

|![image 7](Lu et al._2024_A multimodal generative AI copilot for human pathology_images/imageFile7.png)|
|---|


![image 8](Lu et al._2024_A multimodal generative AI copilot for human pathology_images/imageFile8.png)

Image Captions

Free response Multiple choice

Text only

|Q: A: Q: A:<br><br>What is the primary architectural pattern…?<br><br>The primary architectural patterns are…<br><br>What type of epithelial cells are observed in this tumor?<br><br>The epithelial cells observed in this tumor are described as…<br><br>…<br><br>|![image 9](Lu et al._2024_A multimodal generative AI copilot for human pathology_images/imageFile9.png)|
|---|
|
|---|


|Q: A:<br><br>What is shown in this image?<br><br>Upon examining the image… several key ﬁndings are observed…the most likely diagnosis is a…<br><br>|![image 10](Lu et al._2024_A multimodal generative AI copilot for human pathology_images/imageFile10.png)|
|---|
|
|---|


|Q:<br><br>A:<br><br>Based on the information provided, what is the most likely diagnosis for this liver biopsy?<br><br>Sorry, as an AI assistant specialized in pathology, I cannot assist you with nonpathology related inquiries.<br><br>|![image 11](Lu et al._2024_A multimodal generative AI copilot for human pathology_images/imageFile11.png)|
|---|
|
|---|


Case Reports

ACCELERATED

Educational Notes

###### …

Guardrails

Conversation Description

###### b

Vision-only SSL pretraining

PathChat MLLM 456,916 Instructions (999,202 turns)

Visual-language pretraining

![image 12](Lu et al._2024_A multimodal generative AI copilot for human pathology_images/imageFile12.png)

![image 13](Lu et al._2024_A multimodal generative AI copilot for human pathology_images/imageFile13.png)

Large Language Model

~100 million patches from ~100 thousand slides

#### +

Vision Encoder

1.18 million imagecaption pairs

|![image 14](Lu et al._2024_A multimodal generative AI copilot for human pathology_images/imageFile14.png)|
|---|


PREVIEW

- a
- b


ContextPrompt

A 63-year-old male presents with chronic cough and unintentional weight loss over the past 5 months. Chest X-ray shows a dense, spiculated 3 cm mass. What is the most likely diagnosis?

PathChat

|![image 15](Lu et al._2024_A multimodal generative AI copilot for human pathology_images/imageFile15.png)|
|---|


A. Lung adenocarcinoma

LLaVA-Med

ARTICLE

- A. Lung adenocarcinoma
- B. Typical carcinoid tumor
- C. Atypical carcinoid tumor
- D. Hamartoma of lung
- E. Meningothelial-like nodule
- F. Pneumocytoma
- G. Small cell carcinoma
- H. Large cell carcinoma
- I. Lung squamous cell carcinoma
- J. Large cell neuroendocrine carcinoma Answer with the option's letter from the given choices directly.


I. Lung squamous cell carcinoma

MLLM

LLaVA 1.5

J. Large cell neuroendocrine carcinoma

*

*

GPT4V

Image

A. Lung adenocarcinoma

| |PathChat LLaVA-Med LLaVA 1.5 GPT4V<br><br>|
|---|---|
| | |
| | |
| | |
| | |


1.0

ACCELERATED

0.75

Accuracy

0.5

0.25

0.0

PathQABench -Private

PathQABench -Private w/ Context

Combined Combined w/ Context

PathQABench -Public

PathQABench -Public w/ Context

PREVIEW

a Shuﬄed and de-identiﬁed responses

Panel of 7 pathologists

ranked by each expert …

![image 16](Lu et al._2024_A multimodal generative AI copilot for human pathology_images/imageFile16.png)

![image 17](Lu et al._2024_A multimodal generative AI copilot for human pathology_images/imageFile17.png)

![image 18](Lu et al._2024_A multimodal generative AI copilot for human pathology_images/imageFile18.png)

Win / tie / lose record of PathChat

Expert rankings

|![image 19](Lu et al._2024_A multimodal generative AI copilot for human pathology_images/imageFile19.png)|
|---|


Question #5: Describe the cellular morphology visible in the image from a patient presenting with uterine bleeding and a lower abdominal mass.

![image 20](Lu et al._2024_A multimodal generative AI copilot for human pathology_images/imageFile20.png)

![image 21](Lu et al._2024_A multimodal generative AI copilot for human pathology_images/imageFile21.png)

![image 22](Lu et al._2024_A multimodal generative AI copilot for human pathology_images/imageFile22.png)

ARTICLE

- P1
- P2


+

Q#5: 1 > 3 = 4 > 2

4 AI assistant models

###### <Response 1>

| |
|---|


Q#5: 1 > 3 = 4 = 2

| |
|---|


| |
|---|


LLaVA 1.5 GPT4V

PathChat LLaVA-Med

- <Response 2>
- <Response 3>
- <Response 4>


| |
|---|


| |
|---|


…

…

+

| |
|---|


Enter your ranking here:

P7

260 open-ended questions

![image 23](Lu et al._2024_A multimodal generative AI copilot for human pathology_images/imageFile23.png)

Q#5: 3 > 1 > 4 > 2

![image 24](Lu et al._2024_A multimodal generative AI copilot for human pathology_images/imageFile24.png)

b PathChat d

###### c

ACCELERATED

1.0 Accuracy

Win Tie Lose

| | |
|---|---|
| | |


1.0

LLaVA 1.5

| |LLaVA-Med<br><br>GPT4V|
|---|---|
| | |
| | |
| | |


d

0.5

LLaVA 1.5

0.75

PathChatvs.

Microscopy

Diagnosis

Accuracy

LLaVA Med

0.5

1.0

| | |
|---|---|
| | |


Accuracy

0.25

0.5

GPT4V

0.0 0.25 0.5 0.75 1.0 Ratio

0.0

Ancillary Testing

Clinical

PathQABench

PREVIEW

###### d

a

|![image 25](Lu et al._2024_A multimodal generative AI copilot for human pathology_images/imageFile25.png)|
|---|


|![image 26](Lu et al._2024_A multimodal generative AI copilot for human pathology_images/imageFile26.png)|
|---|


HumanHuman

###### Human

Describe the tumor in this image in detail.

What morphological features are present in this image?

PathChatPathChat

The tumor in this image appears to be a high-grade serous carcinoma. It is characterized by a complex papillary architecture, which means that the tumor cells are arranged in a papillary pattern with multiple branching structures. The cells within the tumor are high-grade, indicating a high level of cellular atypia and aggressive behavior.

PathChatPathChat

The image shows a tumor composed of spindle cells, which are elongated and have a fusiform shape. These cells are arranged in fascicles, which are bundles or groups of cells aligned in a parallel or whorled pattern. Additionally, there are scattered melanincontaining cells within the tumor.

Human

What do you think IHC for p53 would show in this case?

This tumor was found in the liver of a patient. Is it a primary tumor or a metastasis?

ARTICLE

Given the high-grade nature of this serous carcinoma, it is likely that the p53 immunohistochemistry (IHC) would show abnormal p53 protein expression. High-grade serous carcinomas often have TP53 mutations, which can result in aberrant p53 protein accumulation. Therefore, the p53 IHC staining may show strong and diffuse nuclear staining, indicating abnormal p53 orotein expression.

Based on the information provided, this tumor is most likely a metastasis rather than a primary tumor. The presence of spindle cells and melanin-containing cells further supports the possibility of a metastatic melanoma. The liver is a common site for metastasis of melanoma, especially when it has spread from the skin.

e

###### b

|![image 27](Lu et al._2024_A multimodal generative AI copilot for human pathology_images/imageFile27.png)|
|---|


|![image 28](Lu et al._2024_A multimodal generative AI copilot for human pathology_images/imageFile28.png)|
|---|


Human

This is an image of a lung core needle biopsy from a patient with a mass in their left lung. What are some diagnoses this could be and what IHC should I do to work up this case?

Human

There are some cells in this IHC image staining red for CD3. What cell type are they?

PathChat

Based on the image, the differential diagnoses could include primary lung adenocarcinoma, metastatic adenocarcinoma from another primary site, or a poorly differentiated squamous cell carcinoma. To further narrow down the diagnosis, you can perform immunohistochemistry (IHC) staining for TTF-1, Napsin A, and p40. TTF-1 and Napsin A are markers commonly expressed in primary lung adenocarcinoma, while p40 is a marker for squamous cell carcinoma. The expression pattern of these markers will help differentiate between these possibilities.

PathChatPathChat

ACCELERATED

The cells staining red for CD3 are T lymphocytes. CD3 is a marker for T cells, which are a type of white blood cell involved in the immune response.

Human

What IHC would be helpful in distinguishing them from B lymphocytes and macrophages?

CD20 is a marker commonly used to distinguish B lymphocytes from T lymphocytes. B lymphocytes are typically CD20 positive, while T lymphocytes are CD20 negative. Additionally, CD68 is a marker that can be used to identify macrophages. Macrophages are CD68 positive, while T lymphocytes are CD68 negative.

Human

I did TTF-1, p40, and synaptophysin and all stains were negative. What should I do next?

PathChat

The negative staining for TTF-1, p40, and synaptophysin makes it more challenging to determine the exact diagnosis. TTF-1 and p40 are commonly used markers for lung adenocarcinoma and squamous cell carcinoma, respectively. Synaptophysin is a marker for neuroendocrine tumors. The negative staining for these markers suggests that the tumor is not of lung origin or is not a neuroendocrine tumor. In this case, it would be helpful to perform additional IHC stains to further characterize the tumor. Some additional markers to consider include CK7, CK20, and CDX2, which can help differentiate between primary lung adenocarcinoma and metastatic adenocarcinoma from other sites. Additionally, performing a panel of markers speciﬁc to other primary sites (e.g., PSA for prostate, ER for breast, etc.) can help identify the primary site of the tumor. It is also important to consider the clinical history and radiological ﬁndings to guide the workup. If there is a known history of malignancy or suspicion of metastatic disease, further investigation into the primary site may be warranted.

###### c

|![image 29](Lu et al._2024_A multimodal generative AI copilot for human pathology_images/imageFile29.png)|
|---|


###### Human

Assess the tissue morphology in this prostate resection. What Gleason patterns are present?

PathChat

The tissue morphology in this prostate resection reveals a combination of two distinct Gleason patterns. The ﬁrst pattern is characterized by the presence of small, well-formed glands, which is indicative of Gleason pattern 3. The second pattern is characterized by the presence of fused glands, which is indicative of Gleason pattern 4. The presence of both patterns within the same tissue sample suggests a Gleason score of 7 (3+4), which is a moderately aggressive form of prostate cancer.

PREVIEW

![image 30](Lu et al._2024_A multimodal generative AI copilot for human pathology_images/imageFile30.png)

ARTICLE

ACCELERATED

- Extended Data Fig. 1


PREVIEW

ARTICLE

![image 31](Lu et al._2024_A multimodal generative AI copilot for human pathology_images/imageFile31.png)

ACCELERATED

- Extended Data Fig. 2


PREVIEW

![image 32](Lu et al._2024_A multimodal generative AI copilot for human pathology_images/imageFile32.png)

ARTICLE

ACCELERATED

- Extended Data Fig. 3


PREVIEW

![image 33](Lu et al._2024_A multimodal generative AI copilot for human pathology_images/imageFile33.png)

ARTICLE

ACCELERATED

PREVIEW

![image 34](Lu et al._2024_A multimodal generative AI copilot for human pathology_images/imageFile34.png)

ARTICLE

ACCELERATED

PREVIEW

ARTICLE

![image 35](Lu et al._2024_A multimodal generative AI copilot for human pathology_images/imageFile35.png)

ACCELERATED

Extended Data Fig. 6

PREVIEW

![image 36](Lu et al._2024_A multimodal generative AI copilot for human pathology_images/imageFile36.png)

ARTICLE

ACCELERATED

PREVIEW

ARTICLE

![image 37](Lu et al._2024_A multimodal generative AI copilot for human pathology_images/imageFile37.png)

ACCELERATED

Extended Data Fig. 8

PREVIEW

![image 38](Lu et al._2024_A multimodal generative AI copilot for human pathology_images/imageFile38.png)

ARTICLE

ACCELERATED

PREVIEW

![image 39](Lu et al._2024_A multimodal generative AI copilot for human pathology_images/imageFile39.png)

ARTICLE

ACCELERATED

![image 40](Lu et al._2024_A multimodal generative AI copilot for human pathology_images/imageFile40.png)

