# arXiv:2406.05688v1[cs.CL]9 Jun 2024

## Peer Review as A Multi-Turn and Long-Context Dialogue with Role-Based Interactions

Cheng Tan1∗, Dongxin Lyu2∗, Siyuan Li1∗, Zhangyang Gao1, Jingxuan Wei3, Siqi Ma1, Zicheng Liu1 and Stan Z. Li1† 1Westlake University, 2Jilin University, 3University of Chinese Academy of Sciences

### Abstract

Large Language Models (LLMs) have demonstrated wide-ranging applications across various fields and have shown significant potential in the academic peerreview process. However, existing applications are primarily limited to static review generation based on submitted papers, which fail to capture the dynamic and iterative nature of real-world peer reviews. In this paper, we reformulate the peer-review process as a multi-turn, long-context dialogue, incorporating distinct roles for authors, reviewers, and decision makers. We construct a comprehensive dataset containing over 26,841 papers with 92,017 reviews collected from multiple sources, including the top-tier conference and prestigious journal. This dataset is meticulously designed to facilitate the applications of LLMs for multi-turn dialogues, effectively simulating the complete peer-review process. Furthermore, we propose a series of metrics to evaluate the performance of LLMs for each role under this reformulated peer-review setting, ensuring fair and comprehensive evaluations. We believe this work provides a promising perspective on enhancing the LLM-driven peer-review process by incorporating dynamic, role-based interactions. It aligns closely with the iterative and interactive nature of real-world academic peer review, offering a robust foundation for future research and development in this area. We open-source the dataset at github.com/chengtan9907/ReviewMT.

### 1 Introduction

Language models (LMs) serve as a cornerstone in the field of artificial intelligence and its applications [1–3]. The introduction of the highly parallelizable Transformer model [4] marked a significant milestone. This breakthrough was exemplified by the development of BERT [5], which revolutionized the field by introducing pre-training bidirectional language models on large-scale unlabeled corpora using specially designed tasks. BERT’s success established the pre-training and fine-tuning paradigm, inspiring a wave of subsequent research and advancements in pre-trained language models (PLMs)[6–11]. Scaling up these pre-trained models led to the development of large language models (LLMs) [12–16]. This progression culminated in the creation of ChatGPT and GPT-4[17], which have demonstrated unprecedented performance across language tasks. The technical evolution of LLMs has garnered increasing popularity in both industry and academia, with applications spanning a wide range of fields, including healthcare [18–22], finance [23–26], education [27–29], and scientific research [30–37].

Academic paper peer-review is a critical component of the academic publishing system, ensuring the quality of scientific research. Despite its essential role, the traditional peer-review process faces

∗Equal contribution. †Corresponding author.

Preprint. Under review.

Academic paper LLMs

Academic paper

![image 1](Tan et al._2024_Peer Review as A Multi-Turn and Long-Context Dialogue with Role-Based Interactions_images/imageFile1.png)

![image 2](Tan et al._2024_Peer Review as A Multi-Turn and Long-Context Dialogue with Role-Based Interactions_images/imageFile2.png)

![image 3](Tan et al._2024_Peer Review as A Multi-Turn and Long-Context Dialogue with Role-Based Interactions_images/imageFile3.png)

![image 4](Tan et al._2024_Peer Review as A Multi-Turn and Long-Context Dialogue with Role-Based Interactions_images/imageFile4.png)

![image 5](Tan et al._2024_Peer Review as A Multi-Turn and Long-Context Dialogue with Role-Based Interactions_images/imageFile5.png)

![image 6](Tan et al._2024_Peer Review as A Multi-Turn and Long-Context Dialogue with Role-Based Interactions_images/imageFile6.png)

![image 7](Tan et al._2024_Peer Review as A Multi-Turn and Long-Context Dialogue with Role-Based Interactions_images/imageFile7.png)

Reviewer Author Decision Maker

LLMs

![image 8](Tan et al._2024_Peer Review as A Multi-Turn and Long-Context Dialogue with Role-Based Interactions_images/imageFile8.png)

![image 9](Tan et al._2024_Peer Review as A Multi-Turn and Long-Context Dialogue with Role-Based Interactions_images/imageFile9.png)

![image 10](Tan et al._2024_Peer Review as A Multi-Turn and Long-Context Dialogue with Role-Based Interactions_images/imageFile10.png)

![image 11](Tan et al._2024_Peer Review as A Multi-Turn and Long-Context Dialogue with Role-Based Interactions_images/imageFile11.png)

Review Review Rebuttal Decision

(a) Existing approach (b) Our reformulated framework

Figure 1: Comparison of existing LLM applications in peer review and our reformulated framework.

significant criticism [38–40] for its inefficiency, bias, and lack of transparency. While applying LLMs in peer-review presents a promising solution, recent studies have demonstrated the potential of LLMs in generating high-quality reviews for given papers [41–43]. However, existing research primarily focuses on generating static reviews based on submitted papers, which severely simplifies the process and fails to capture the dynamic and iterative nature of real-world peer reviews. In this work, as shown in Figure 1, we offer a novel perspective on the complete peer-review process by reformulating it as a multi-turn, long-context dialogue involving three distinct roles: authors, reviewers, and decision makers. This reformulation includes several key aspects:

- • Long-Context: The entire dialogue is grounded in the extensive context of the paper, ensuring that all interactions of different roles are informed by the full scope of the manuscript.
- • Multi-Turn: The dialogue is conducted over multiple rounds, mimicking the real world where reviewers write reviews based on the paper, authors provide rebuttals to the reviews, reviewers respond to rebuttals, and decision makers make decisions based on the comprehensive exchange.
- • Role-Based: Each role in the dialogue has specific responsibilities and objectives. Reviewers critically evaluate the paper and provide feedback, authors respond to this feedback to clarify their work, and decision makers synthesize the dialogue to make an informed publication decision.


With these principles in mind, we constructed a comprehensive dataset named ReviewMT, sourced from multiple venues including the top-tier AI conference ICLR and the multidisciplinary journal Nature Communications. This dataset is meticulously designed to embody the dynamic, iterative nature of the peer-review process. By incorporating both accepted and rejected papers from ICLR, the dataset provides insights into common pitfalls and areas for improvement, enriching the training and evaluation of LLMs. The dataset spans a wide range of domains, reflecting the diverse topics covered by Nature Communications and the cutting-edge AI research presented at ICLR. Each entry in the collected dataset is carefully annotated to include multi-turn dialogues that capture the full scope of interactions between authors, reviewers, and decision makers.

Creating the dataset is just the first step in our reformulated peer-review framework. To evaluate LLM performance in this setting, we propose a series of metrics tailored to each role in the dialogue. These metrics assess the validity of generated responses, the text quality, the score evaluation of final reviews, the decision evaluation of decision makers. By evaluating LLMs based on these metrics, we aim to provide a fair and comprehensive assessment of their performance in the peer-review process. We believe this work offers a promising perspective on enhancing the LLM-driven peer-review process by incorporating dynamic, role-based interactions. It closely aligns with the iterative and interactive nature of real-world academic peer review, providing a foundation for future research.

### 2 Related Work

#### 2.1 Instruction Tuning Dataset

Instruction tuning is a specialized training process applied to LLMs to enhance their ability to follow specific instructions and perform designated tasks with greater precision and reliability. Instruction tuning datasets, which are collections of task-specific examples paired with explicit instructions, play a crucial role in this process. Early efforts in this field, such as Dolly [44] and InstructGPT [45], relied heavily on manual or expert annotations. Over time, the field has seen the emergence of semi-automated and fully automated approaches for instruction creation. These approaches have transformed existing datasets and facilitated more efficient training of LLMs [46, 9, 47]. A notable example is Stanford Alpaca [48], which employs a bootstrapping technique grounded in a set of handcrafted instructions to generate 52,000 diverse instructions. This approach has inspired the development of model-aided data collections, such as Baize [49], COIG [50], and UltraChat [51], enabling automatic data generation and reducing the need for human effort [52–55]. Though these datasets have significantly advanced the instruction tuning field, most of them focus on single-turn interactions and lack the multi-turn, long-context dialogue characteristic of peer reviews.

#### 2.2 LLM in Review

LLMs have demonstrated significant potential in reviewing and comprehending complex articles. Early studies [41] suggested that GPT-generated reviews are comparable to those of human reviewers. By comparing reviews generated by humans and GPT models for academic papers submitted to a major machine learning conference, it was initially demonstrated that LLMs can effectively contribute to the peer review process. Further research [42] revealed that GPT-4’s feedback had a substantial overlap with human reviewers, with over half of the users rating GPT-4’s feedback as helpful, underscoring the growing role of LLMs in the peer review process. MARG [43] employs multiple LLM instances to internally discuss and assign sections of a paper to different agents, providing comprehensive feedback across the entire text, even for papers exceeding the model’s context size. While current LLM research focuses on simply generating reviews, we aim to simulate the complete review process into a multi-round dialogue, emphasizing the iterative nature of real-world peer review.

### 3 Preliminaries

In existing works on LLM-based peer review research, the focus is primarily on generating a static review R for a given paper P by a reviewer R. This process can be formulated as follows:

##### R : P → R, (1)

where R is implemented by an LLM Fθ parameterized by θ. This process is typically conducted in a single turn, with the reviewer R providing feedback on the paper P without further interaction.

In our peer-review framework, we extend this process to a multi-turn dialogue with three distinct roles: Reviewer, Author, and Decision Maker. Each role has specific objectives and interactions:

- • Reviewer (R): The reviewer is responsible for generating an initial review Ri for the paper P in the first turn, which includes a critical assessment of the paper and questions for the author to address: Ri : P → R. It is worth noting that there are N reviewers for each paper P. After the author responds with rebuttals Ai in the second turn, the reviewer evaluates the author’s response and generates a final review Ri′, which reflects their updated opinion on the paper after considering the author’s clarifications and revisions: Ri : Ai → Ri′.
- • Author (A): The author plays a crucial role in the second turn by responding to the initial review

{Ri}Ni=1 provided by each reviewer. The author carefully addresses the reviewer’s comments, clarifies misunderstandings, and outlines any changes or improvements made to the paper in

response to the feedback. The rebuttal Ai serves to defend the paper’s validity and significance while showing a willingness to incorporate constructive criticism: A : {Ri}Ni=1 → {Ai}Ni=1.

- • Decision Maker (D): The decision maker synthesizes the entire dialogue, including the paper P,


the initial review {Ri}Ni=1, the author’s rebuttal {Ai}Ni=1, and the final review {Ri′}Ni=1, to make an informed decision D. This role is pivotal in the fourth turn, where the decision maker evaluates

the coherence and validity of the arguments presented by both the reviewer and the author to reach a final decision on whether the paper should be accepted or rejected: D : {Ri,Ai,Ri′} → D.

The complete process can be formulated as a multi-turn dialogue with the following interactions: ⃝ {R1 i(P)} → {Ri} ⃝ {A2 (Ri)} → {Ai} ⃝ {R3 i(Ai)} → {Ri′} ⃝ D4 ({Ri,Ai,Ri′}) → D.

(2)

By incorporating these roles into a multi-turn dialogue, our framework stimulates the dynamic and iterative nature of real-world peer review. This approach facilitates more detailed and interactive reviews, encouraging constructive communication between authors and reviewers.

- 4 ReviewMT Dataset


- 4.1 Data Source

One of the primary sources for the ReviewMT dataset was the International Conference on Learning Representations (ICLR) [56] on OpenReview [57], renowned for its contributions to machine learning and artificial intelligence. ICLR’s emphasis on cutting-edge research across a broad spectrum of AI topics provided a diverse and valuable set of papers and reviews. Additionally, data was collected from Nature Communications [58], a leading multidisciplinary journal known for publishing significant scientific advances. The broad scope and high impact of this journal allowed us to incorporate papers from various scientific fields, enhancing the dataset’s diversity. Both ICLR and Nature Communications offer accessible and detailed review data, making them ideal sources for constructing a comprehensive peer-review dataset. Given the distinct review processes of these sources, the dataset is divided into two subsets: ReviewMT-ICLR and ReviewMT-NC. This division allows for tailored analysis and training, reflecting the unique characteristics and standards of each review process.

- 4.2 Data Processing


As shown in Figure 2, the data collection process for the ReviewMT dataset involved gathering papers from ICLR spanning the years 2017 to 2024. Additionally, all papers published in Nature Communications in 2023 were included. For ICLR papers, we leveraged the official API [59] to systematically extract titles and abstracts. The conversion of PDF files to text was facilitated by a software tool called Marker [60], which ensures the text is rendered with markdown grammar, maintaining structural and formatting fidelity. For Nature Communications papers, we used the Requests library to crawl data, adhering to the Robots protocol to ensure compliance with web scraping policies. We collected papers from Nature Communications in 2023 along with their corresponding peer reviews within the official PDF files. However, some papers did not have accompanying official peer review data, and these were excluded from our dataset. All the PDF files are also converted to text with markdown grammar by Marker [60].

The dataset construction focused on capturing detailed and structured interactions for each turn of the peer review process. For each paper, we included several fields to support multi-turn dialogues. Specifically, the dataset includes fields for each turn of the dialogue: "Title", "Abstract", and "Main Text" provide the long context; “Summary”, “Strengths”, "Weaknesses", and "Questions" are included in the first turn for reviewers to write the initial review for a given paper; "Response" is in the second turn for authors to address each reviewer; "Final comment" and "Score" are in the third turn for reviewers to provide the final review and assign a score; and "Meta review" and "Final decision" are in the fourth turn for decision makers to make the final publication decision. All the files are stored in JSON format to ensure easy access and compatibility with various programming languages and tools.

It is important to note that the review process may vary even within the same conference across different years. For instance, some years may not provide an initial rating for the paper in the first turn, so we adapted such cases by only considering the final rating. Similarly, Nature Communications offers a “Peer Review File,” which was integrated as the main review information into our framework to ensure consistency. By meticulously collecting and organizing this data, the ReviewMT dataset aims to provide a comprehensive resource that captures the iterative nature of the peer review process. The

|![image 12](Tan et al._2024_Peer Review as A Multi-Turn and Long-Context Dialogue with Role-Based Interactions_images/imageFile12.png)|
|---|


Title: [PiFold: Toward effective and efficient protein inverse folding].

Abstract: [How can we design protein sequences folding into the desired structures effectively and efficiently...]

- ⓪
- ①
- ②
- ③
- ④


Main Text: [Proteins are linear chains of amino acids that fold into 3D structures to control cellular processes...]

![image 13](Tan et al._2024_Peer Review as A Multi-Turn and Long-Context Dialogue with Role-Based Interactions_images/imageFile13.png)

![image 14](Tan et al._2024_Peer Review as A Multi-Turn and Long-Context Dialogue with Role-Based Interactions_images/imageFile14.png)

Summary: [This paper proposes a method for structure-based protein design that...] Strengths: [The paper is well-written and organized in a logical manner...] Weaknesses: [The novelty compared to AlphaDesign and GCA is somewhat limited...] Questions: [Could authors clarify the contribution compared with AlphaDesign...]

![image 15](Tan et al._2024_Peer Review as A Multi-Turn and Long-Context Dialogue with Role-Based Interactions_images/imageFile15.png)

![image 16](Tan et al._2024_Peer Review as A Multi-Turn and Long-Context Dialogue with Role-Based Interactions_images/imageFile16.png)

![image 17](Tan et al._2024_Peer Review as A Multi-Turn and Long-Context Dialogue with Role-Based Interactions_images/imageFile17.png)

![image 18](Tan et al._2024_Peer Review as A Multi-Turn and Long-Context Dialogue with Role-Based Interactions_images/imageFile18.png)

![image 19](Tan et al._2024_Peer Review as A Multi-Turn and Long-Context Dialogue with Role-Based Interactions_images/imageFile19.png)

![image 20](Tan et al._2024_Peer Review as A Multi-Turn and Long-Context Dialogue with Role-Based Interactions_images/imageFile20.png)

Response: [Thanks for your reviewing sevice and valuable suggestions. PiFold introduces more protein features, virtual atoms...]

Meta data

![image 21](Tan et al._2024_Peer Review as A Multi-Turn and Long-Context Dialogue with Role-Based Interactions_images/imageFile21.png)

![image 22](Tan et al._2024_Peer Review as A Multi-Turn and Long-Context Dialogue with Role-Based Interactions_images/imageFile22.png)

![image 23](Tan et al._2024_Peer Review as A Multi-Turn and Long-Context Dialogue with Role-Based Interactions_images/imageFile23.png)

Final comment: [I thank the authors for the in-depth response. Most of my questions with respect to original contribution and reproducibility have been addressed...]

![image 24](Tan et al._2024_Peer Review as A Multi-Turn and Long-Context Dialogue with Role-Based Interactions_images/imageFile24.png)

###### Score: [6]

|![image 25](Tan et al._2024_Peer Review as A Multi-Turn and Long-Context Dialogue with Role-Based Interactions_images/imageFile25.png)|
|---|


Meta review: [The paper proposes a novel method for protein inverse folding…]. Final decision: [Accept].

Figure 2: Overview of the data processing pipeline for the ReviewMT dataset.

resulting interactions modeled in the dataset are expected to drive more nuanced LLM applications in academic peer review, promoting constructive feedback mechanisms in scholarly publishing.

#### 4.3 Dataset Statistics

We provide a detailed overview of the ReviewMT-ICLR dataset in Figure 3(a), which illustrates various aspects of the dataset, highlighting its significance and the challenges it addresses. The dataset showcases a remarkable increase in the number of papers submitted to ICLR, from 485 in 2017 to 5760 in 2024. This growth reflects the expanding influence and participation in the conference, underscoring the increasing importance of effective and scalable peer review processes.

| | | | | | | | | |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |


| | | | | | | | | |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |


| | | | | | | | | |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |


(a) Number of papers across years (b) Average tokens of each paper (c) Number of reviews (d) Accepted vs/ Rejected

Figure 3: Statistics of the ICLR papers and reviews in the ReviewMT-ICLR dataset.

- Figure 3(b) depicts the average number of tokens per paper, which ranges from approximately 13,000 to 26,000 tokens. Notably, there is a slight drop in average tokens per paper in 2023 and 2024 due to the absence of rebuttal-phase replies in those years. This highlights the long context challenge inherent in our setting. Figure 3(c) indicates that each paper typically receives about three to four reviews. This implies that for each paper, there are at least three or four interactions between authors and reviewers. These interactions, combined with the subsequent feedback from decision makers


to reviewers, form a complex multi-turn dialogue. Figure 3(d) presents the acceptance statistics, showing that 38.1% of the papers in the dataset were accepted, while 61.9% were rejected. This distribution provides a balanced mix of positive and negative samples.

![image 26](Tan et al._2024_Peer Review as A Multi-Turn and Long-Context Dialogue with Role-Based Interactions_images/imageFile26.png)

![image 27](Tan et al._2024_Peer Review as A Multi-Turn and Long-Context Dialogue with Role-Based Interactions_images/imageFile27.png)

(a) ReviewMT-ICLR (b) ReviewMT-NC

Figure 4: The word cloud of the keywords in the ReviewMT dataset.

Figure 4 presents a word cloud of keywords from the ReviewMT dataset, offering insights into the prevalent research themes within the dataset. The word cloud is divided into two parts, each representing keywords from different sources included in the dataset. In Figure 4(a), keywords such as “deep learning”, “self-supervised learning”, and “reinforcement learning” are prominently featured. These terms highlight the focus on cutting-edge research topics in the field of machine learning that are prevalent in ICLR papers. The prominence of these keywords reflects the ongoing advancements and interests in these areas within the machine learning community. Conversely,

- Figure 4(b) illustrates a broader range of keywords derived from Nature Communications papers. These keywords cover a diverse array of scientific disciplines, including “cell”, “human”, “gene”, and “immune”. This diversity underscores the multidisciplinary nature of Nature Communications, showcasing its wide-reaching impact across various fields of scientific research. The combined keyword analysis from ReviewMT-ICLR and ReviewMT-NC demonstrates the richness and diversity of the ReviewMT dataset. By encompassing both specialized machine learning research and a wide spectrum of scientific disciplines, the dataset offers a comprehensive resource for training and evaluating large language models (LLMs) in the peer review process. This diversity ensures that models trained on this dataset can handle a variety of topics and review styles, enhancing their applicability and robustness in real-world academic settings.


In Table 1, we present detailed statistics for the ReviewMT dataset. The dataset encompasses a total of 26,841 papers, 92,017 reviews, and 567,207,583 tokens, calculated using the LLaMA-3 tokenizer. This extensive and diverse dataset serves as a robust resource for training and evaluating LLMs in the peer review process. The breadth and depth of the ReviewMT dataset ensure that it captures the complexity and nuances of real-world academic peer review, making it invaluable for this area.

Table 1: The detailed dataset statistics of the ReviewMT dataset.

Dataset/Year Papers Reviews Tokens

- ICLR 2017 485 1,474 6,361,501
- ICLR 2018 926 2,778 14,101,709
- ICLR 2019 1,416 4,322 25,119,319
- ICLR 2020 2,205 6,695 41,588,041
- ICLR 2021 2,578 9,963 59,272,632
- ICLR 2022 2,610 10,177 67,459,995
- ICLR 2023 3,784 14,307 87,201,458
- ICLR 2024 5,760 22,282 135,995,413 ICLR 19,764 71,998 439,100,068 Nature Communications 7,077 20,019 128,107,515


#### 4.4 Evaluation Metrics

We introduce a comprehensive set of evaluation metrics tailored to the peer-review dialogue. These metrics are designed to evaluate the quality of text replies and the validity of responses.

Validity of response Given the long-context nature of peer-review documents, which average over 20,000 tokens per paper, LLMs may occasionally fail to provide valid responses. To address this, we use the following hit rates to evaluate the validity of the responses:

- • Paper hit rate: Measures whether the LLM-generated response addresses the paper content. If the LLM fails to respond to the paper, the hit rate is 0.
- • Review hit rate: Evaluates whether the LLM-generated final review includes a score. If the LLM fails to provide the score, the hit rate is 0.
- • Decision hit rate: Assesses whether the LLM-generated decision includes a clear accept or reject outcome. If the LLM fails to respond with a decision, the hit rate is 0.


Text quality evaluation For all text replies, including the reviewers’ initial reviews, the authors’ responses, the reviewers’ final reviews, and the decision makers’ meta reviews, we employ text similarity metrics to assess the quality of the generated text. These metrics include:

- • BLEU-2 and BLEU-4 [61]: Measures n-gram precision by comparing the generated text to a reference text, focusing on 2-gram and 4-gram overlaps respectively.
- • ROUGE-1, ROUGE-2, and ROUGE-L [62]: Measures f1-score of unigram, bigram, and longest common subsequence overlaps between the generated text and the reference text.
- • METEOR [63]: A measure of alignment between the generated and reference texts. METEOR also incorporates stemming and synonymy, making it more sensitive to variations in wording.


Score evaluation To evaluate the accuracy of the final review scores provided by the LLMs, we use: • Mean Absolute Error (MAE): Measures the average absolute difference between the scores

given by the LLM and the actual scores provided by human reviewers.

Decision evaluation For evaluating the decisions (accept or reject) made by the decision makers:

• F1-score: Combines precision and recall to measure the binary classification of decisions.

### 5 Experiments

We employ several open-source LLMs to evaluate performance on the proposed ReviewMT dataset. Specifically, we use LLaMA-3 [64], Qwen [65], Baichuan2 [66], ChatGLM3 [67], Gemma [68], DeepSeek [69], and Yuan-2 [70]. All models are implemented using the LLaMA-factory [71]. For ReviewMT-ICLR, we use papers from 2017 to 2023 as the training data and sample 100 papers from 2024 as the test set. For ReviewMT-NC, we sample 100 papers as the test set, with the remaining papers used for training. Both zero-shot and supervised finetuned performance are reported. Detailed implementation details and the list of sampled papers in the test set are in the supplemental materials.

Table 2: Performance comparison of LLMs on the ReviewMT-ICLR dataset.

Method Paper hit rate ↑ Review hit rate ↑ Decision hit rate ↑ MAE ↓ F1-score ↑ LLaMA-3 100% 2.05% 9.00% 2.12±0.93 0.6154

Qwen 89% 2.00% 58.43% 3.29±1.28 0.4068 Baichuan2 97% 0.00% 27.84% / 0.4848

Zero-shot

Gemma 98% 1.05% 5.15% 1.25±0.43 0.6667 DeepSeek 100% 0.51% 31.00% 4.50±1.50 0.6000 Yuan 100% 0.00% 0.00% / /

ChatGLM3 100% 19.18% 32.00% 3.36±1.92 0.2667 LLaMA-3 100% 49.87% 42.00% 1.04±1.17 0.6154

Qwen 89% 74.29% 15.73% 1.10±1.18 0.5882 Baichuan2 99% 98.45% 14.14% 0.92±1.03 0.8000

Supervised Finetune

Gemma 98% 81.79% 48.94% 1.09±1.23 0.6522 DeepSeek 100% 20.46% 40.00% 1.02±1.08 0.6486

Yuan 100% 100.00% 1.00% 0.94±0.98 0.0000

ChatGLM3 99% 91.99% 41.41% 0.99±0.97 0.6190

As shown in Table 2, most LLMs demonstrate high paper hit rates, indicating their ability to generate relevant content related to the papers. However, zero-shot performance reveals lower review hit rates and decision hit rates, suggesting that LLMs struggle to provide scores and decisions. Supervised fine-tuning significantly improves performance across all metrics. For instance, the review hit rates and decision hit rates see marked improvements, reflecting the models’ enhanced ability to generate comprehensive reviews and make accurate decisions after being fine-tuned on the ReviewMT dataset. It is noteworthy that the Yuan model, despite achieving a high review hit rate, has an extremely low decision hit rate, likely due to its strict constraints preventing it from making decisions. Figure 5 displays a radar chart comparing text similarity metrics for the evaluated LLMs. The chart illustrates that zero-shot performance is limited, whereas supervised fine-tuning yields significantly better results. High scores in text similarity metrics indicate the fine-tuned models’ ability to produce text that closely matches human-generated reviews, both in terms of content and style.

ROUGE-L

BLEU-4

ROUGE-L

BLEU-4

ROUGE-1

ROUGE-1

BLEU-2

BLEU-2

ROUGE-2 METEOR

ROUGE-2 METEOR

(a) Zero-shot (b) Supervised finetuned

Figure 5: The radar chart of text similarity metrics for LLMs on the ReviewMT-ICLR dataset.

We present the performance results of LLMs on the ReviewMT-NC dataset in Table 3. Due to the nature of the openly accessible reviews for Nature Communications, which are not as complete as those from ICLR, the evaluation focuses on a one-turn dialogue, and thus, we do not evaluate the review hit rate and MAE. Zero-shot performance suffers from low review hit rates and decision hit rates. Supervised fine-tuning improves the performance of most models. However, the extent of improvement is not as pronounced as that observed with the ReviewMT-ICLR. This difference could be attributed to the multi-turn dialogue nature of ReviewMT-ICLR, which offers a richer context for models to learn from. Figure 6 displays a radar chart comparing text similarity metrics. The chart corroborates the results observed in Table 3, illustrating that while supervised fine-tuning generally improves metrics, the gains are more modest compared to those seen with the ReviewMT-ICLR, underscoring the importance of multi-turn dialogues in the peer review process.

Table 3: Performance comparison of LLMs on the ReviewMT-NC dataset.

Method Paper hit rate ↑ Decision hit rate ↑ F1-score ↑ LLaMA-3 96% 31.25% 0.6364

Qwen 37% 44.12% 0.7500 Baichuan2 100% 27.00% 0.9811

Zero-shot

Gemma 99% 81.11% 0.9420 DeepSeek 100% 61.00% 0.8269

Yuan 100% 0.05% 1.0000

ChatGLM3 100% 24.00% 0.8837 LLaMA-3 100% 16.00% 0.6667

Qwen 99% 21.21% 0.8333 Baichuan2 100% 73.00% 0.7414

Supervised Finetune

Gemma 99% 89.90% 0.7286 DeepSeek 100% 6.00% 0.5000

Yuan 100% 18.00% 0.9091

ChatGLM3 100% 74.00% 0.9504

ROUGE-L

BLEU-4

ROUGE-L

BLEU-4

ROUGE-1

ROUGE-1

BLEU-2

BLEU-2

ROUGE-2 METEOR

ROUGE-2 METEOR

(a) Zero-shot (b) Supervised finetuned

Figure 6: The radar chart of text similarity metrics for LLMs on the ReviewMT-NC dataset.

### 6 Conclusion and Limitation

In this paper, we presented the construction and evaluation of the ReviewMT dataset, designed for the application of LLMs in the peer review process. By reformulating peer review as a multi-turn dialogue involving distinct roles for reviewers, authors, and decision makers, we aim to capture the dynamic and iterative nature of real-world academic peer review. Our comprehensive dataset, drawn from top-tier conferences like ICLR and prestigious journals such as Nature Communications, supports this complex interaction model and provides a rich resource for fine-tuning and evaluating LLMs. Our framework includes detailed annotations for each turn of the peer review process, allowing LLMs to generate and respond to reviews. By addressing various aspects of the peer review cycle—initial reviews, author rebuttals, final reviews, and decision-making—the ReviewMT dataset facilitates the development of LLMs that can engage in meaningful, constructive peer review dialogues. This advancement holds promise for improving the efficiency and fairness of the peer review process.

Despite its potential, our work has certain limitations that need to be acknowledged. Firstly, no figures are included in the main text, which could limit the dataset’s ability to handle visual data integral to some academic papers. Additionally, the dataset is currently limited to specific conferences and journals, primarily ICLR and Nature Communications. This scope may not fully represent the diversity of academic publishing, and future work should aim to extend the dataset to include a broader range of sources across various disciplines. The primary concern about societal impact is the potential for bias. If the training dataset includes biased reviews or decisions, the LLM might learn and replicate these biases, leading to unfair evaluations of certain groups or topics.

### References

- [1] Zhangyang Gao, Cheng Tan, and Stan Z Li. Pifold: Toward effective and efficient protein inverse folding. In The Eleventh International Conference on Learning Representations, 2022. 1
- [2] Siyuan Li, Zedong Wang, Zicheng Liu, Cheng Tan, Haitao Lin, Di Wu, Zhiyuan Chen, Jiangbin Zheng, and Stan Z Li. Moganet: Multi-order gated aggregation network. In The Twelfth International Conference on Learning Representations, 2023.
- [3] Cheng Tan, Zhangyang Gao, Siyuan Li, and Stan Z Li. Simvp: Towards simple yet powerful spatiotemporal predictive learning. arXiv preprint arXiv:2211.12509, 2022. 1
- [4] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz Kaiser, and Illia Polosukhin. Attention is all you need. Advances in neural information processing systems, 30, 2017. 1
- [5] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. Bert: Pre-training of deep bidirectional transformers for language understanding. arXiv preprint arXiv:1810.04805,

2018. 1

- [6] Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, Ilya Sutskever, et al. Language models are unsupervised multitask learners. OpenAI blog, 1(8):9, 2019. 1
- [7] Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke Zettlemoyer, and Veselin Stoyanov. Roberta: A robustly optimized bert pretraining approach. arXiv preprint arXiv:1907.11692, 2019.
- [8] Zhenzhong Lan, Mingda Chen, Sebastian Goodman, Kevin Gimpel, Piyush Sharma, and Radu Soricut. Albert: A lite bert for self-supervised learning of language representations. arXiv preprint arXiv:1909.11942, 2019.
- [9] Victor Sanh, Albert Webson, Colin Raffel, Stephen H Bach, Lintang Sutawika, Zaid Alyafeai, Antoine Chaffin, Arnaud Stiegler, Teven Le Scao, Arun Raja, et al. Multitask prompted training enables zero-shot task generalization. arXiv preprint arXiv:2110.08207, 2021. 3
- [10] William Fedus, Barret Zoph, and Noam Shazeer. Switch transformers: Scaling to trillion parameter models with simple and efficient sparsity. JMLR, 23(120):1–39, 2022.
- [11] Thomas Wang, Adam Roberts, Daniel Hesslow, Teven Le Scao, Hyung Won Chung, Iz Beltagy, Julien Launay, and Colin Raffel. What language model architecture and pretraining objective works best for zero-shot generalization? In International Conference on Machine Learning, pages 22964–22984. PMLR, 2022. 1
- [12] Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B Brown, Benjamin Chess, Rewon Child, Scott Gray, Alec Radford, Jeffrey Wu, and Dario Amodei. Scaling laws for neural language models. arXiv preprint arXiv:2001.08361, 2020. 1
- [13] Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yogatama, Maarten Bosma, Denny Zhou, Donald Metzler, et al. Emergent abilities of large language models. arXiv preprint arXiv:2206.07682, 2022.
- [14] Ce Zhou, Qian Li, Chen Li, Jun Yu, Yixin Liu, Guangjing Wang, Kai Zhang, Cheng Ji, Qiben Yan, Lifang He, et al. A comprehensive survey on pretrained foundation models: A history from bert to chatgpt. arXiv preprint arXiv:2302.09419, 2023.
- [15] Xu Han, Zhengyan Zhang, Ning Ding, Yuxian Gu, Xiao Liu, Yuqi Huo, Jiezhong Qiu, Yuan Yao, Ao Zhang, Liang Zhang, et al. Pre-trained models: Past, present and future. AI Open, 2:225–250, 2021.
- [16] Pengfei Liu, Weizhe Yuan, Jinlan Fu, Zhengbao Jiang, Hiroaki Hayashi, and Graham Neubig. Pre-train, prompt, and predict: A systematic survey of prompting methods in natural language processing. ACM Computing Surveys, 55(9):1–35, 2023. 1


- [17] OpenAI. Gpt-4 technical report. OpenAI, 2023. 1
- [18] Ruixiang Tang, Xiaotian Han, Xiaoqian Jiang, and Xia Hu. Does synthetic data generation of llms help clinical text mining? arXiv preprint arXiv:2303.04360, 2023. 1
- [19] Kailai Yang, Shaoxiong Ji, Tianlin Zhang, Qianqian Xie, and Sophia Ananiadou. On the evaluations of chatgpt and emotion-enhanced prompting for mental health analysis. arXiv preprint arXiv:2304.03347, 2023.
- [20] Karan Singhal, Tao Tu, Juraj Gottweis, Rory Sayres, Ellery Wulczyn, Le Hou, Kevin Clark, Stephen Pfohl, Heather Cole-Lewis, Darlene Neal, et al. Towards expert-level medical question answering with large language models. arXiv preprint arXiv:2305.09617, 2023.
- [21] Songhua Yang, Hanjie Zhao, Senbin Zhu, Guangyu Zhou, Hongfei Xu, Yuxiang Jia, and Hongying Zan. Zhongjing: Enhancing the chinese medical capabilities of large language model through expert feedback and real-world multi-turn dialogue. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 38, pages 19368–19376, 2024.
- [22] Shan Chen, Benjamin H Kann, Michael B Foote, Hugo JWL Aerts, Guergana K Savova, Raymond H Mak, and Danielle S Bitterman. The utility of chatgpt for cancer treatment information. MedrXiv, pages 2023–03, 2023. 1
- [23] Neng Wang, Hongyang Yang, and Christina Dan Wang. Fingpt: Instruction tuning benchmark for open-source large language models in financial datasets. arXiv preprint arXiv:2310.04793,

2023. 1

- [24] Agam Shah and Sudheer Chava. Zero is not hero yet: Benchmarking zero-shot performance of llms for financial tasks. arXiv preprint arXiv:2305.16633, 2023.
- [25] Qianqian Xie, Weiguang Han, Zhengyu Chen, Ruoyu Xiang, Xiao Zhang, Yueru He, Mengxi Xiao, Dong Li, Yongfu Dai, Duanyu Feng, et al. The finben: An holistic financial benchmark for large language models. arXiv preprint arXiv:2402.12659, 2024.
- [26] Huaqin Zhao, Zhengliang Liu, Zihao Wu, Yiwei Li, Tianze Yang, Peng Shu, Shaochen Xu, Haixing Dai, Lin Zhao, Gengchen Mai, et al. Revolutionizing finance with llms: An overview of applications and insights. arXiv preprint arXiv:2401.11641, 2024. 1
- [27] Attila Szabo. Chatgpt is a breakthrough in science and education but fails a test in sports and exercise psychology. Baltic Journal of Sport and Health Sciences, 1(128):25–40, 2023. 1
- [28] Kamil Malinka, Martin Peresíni, Anton Firc, Ondrej Hujnák, and Filip Janus. On the educational impact of chatgpt: Is artificial intelligence ready to obtain a university degree? In Proceedings of the 2023 Conference on Innovation and Technology in Computer Science Education V. 1, pages 47–53, 2023.
- [29] Teo Susnjak. Chatgpt: The end of online exam integrity? arXiv preprint arXiv:2212.09292,

2022. 1

- [30] Qiao Jin, Bhuwan Dhingra, Zhengping Liu, William W Cohen, and Xinghua Lu. Pubmedqa: A dataset for biomedical research question answering. arXiv preprint arXiv:1909.06146, 2019. 1
- [31] Cheng Tan, Jun Xia, Lirong Wu, and Stan Z Li. Co-learning: Learning from noisy labels with self-supervision. In Proceedings of the 29th ACM International Conference on Multimedia, pages 1405–1413, 2021.
- [32] Yin Fang, Xiaozhuan Liang, Ningyu Zhang, Kangwei Liu, Rui Huang, Zhuo Chen, Xiaohui Fan, and Huajun Chen. Mol-instructions: A large-scale biomolecular instruction dataset for large language models. arXiv preprint arXiv:2306.08018, 2023.
- [33] Jingxuan Wei, Cheng Tan, Zhangyang Gao, Linzhuang Sun, Siyuan Li, Bihui Yu, Ruifeng Guo, and Stan Z Li. Enhancing human-like multi-modal reasoning: A new challenging dataset and comprehensive framework. arXiv preprint arXiv:2307.12626, 2023.


- [34] Cheng Tan, Jingxuan Wei, Zhangyang Gao, Linzhuang Sun, Siyuan Li, Xihong Yang, and Stan Z Li. Boosting the power of small multimodal reasoning models to match larger models with self-consistency training. arXiv preprint arXiv:2311.14109, 2023.
- [35] Mostafa M Amin, Erik Cambria, and B Schuller. Will affective computing emerge from foundation models and general ai. A first evaluation on ChatGPT. ArXiv, abs/2303.03186, 2023.
- [36] Cheng Tan, Jingxuan Wei, Linzhuang Sun, Zhangyang Gao, Siyuan Li, Bihui Yu, Ruifeng Guo, and Stan Z Li. Retrieval meets reasoning: Even high-school textbook knowledge benefits multimodal reasoning. arXiv preprint arXiv:2405.20834, 2024.
- [37] Yang Jeong Park, Daniel Kaplan, Zhichu Ren, Chia-Wei Hsu, Changhao Li, Haowei Xu, Sipei Li, and Ju Li. Can chatgpt be used to generate scientific hypotheses? Journal of Materiomics, 10(3):578–584, 2024. 1
- [38] Wesley Morris, Scott Crossley, Langdon Holmes, and Anne Trumbore. Using transformer language models to validate peer-assigned essay scores in massive open online courses (moocs). In LAK23: 13th international learning analytics and knowledge conference, pages 315–323,

2023. 2

- [39] Nihar B Shah. Challenges, experiments, and computational solutions in peer review. Communications of the ACM, 65(6):76–87, 2022.
- [40] Ryan Liu and Nihar B Shah. Reviewergpt? an exploratory study on using large language models for paper reviewing. arXiv preprint arXiv:2306.00622, 2023. 2
- [41] Zachary Robertson. Gpt4 is slightly helpful for peer-review assistance: A pilot study. arXiv preprint arXiv:2307.05492, 2023. 2, 3
- [42] Weixin Liang, Yuhui Zhang, Hancheng Cao, Binglu Wang, Daisy Ding, Xinyu Yang, Kailas Vodrahalli, Siyu He, Daniel Smith, Yian Yin, Daniel McFarland, and James Zou. Can large language models provide useful feedback on research papers? a large-scale empirical analysis,

2023. 3

- [43] Mike D’Arcy, Tom Hope, Larry Birnbaum, and Doug Downey. Marg: Multi-agent review generation for scientific papers, 2024. 2, 3
- [44] Mike Conover, Matt Hayes, Ankit Mathur, Jianwei Xie, Jun Wan, Sam Shah, Ali Ghodsi, Patrick Wendell, Matei Zaharia, and Reynold Xin. Free dolly: Introducing the world’s first truly open instruction-tuned llm. 2023. 3
- [45] Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al. Training language models to follow instructions with human feedback. NeurIPS, 35:27730–27744, 2022. 3
- [46] Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung, Charles Sutton, Sebastian Gehrmann, et al. Palm: Scaling language modeling with pathways. JMLR, 24(240):1–113, 2023. 3
- [47] Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Yunxuan Li, Xuezhi Wang, Mostafa Dehghani, Siddhartha Brahma, et al. Scaling instruction-finetuned language models. JMLR, 25(70):1–53, 2024. 3
- [48] Rohan Taori, Ishaan Gulrajani, Tianyi Zhang, Yann Dubois, Xuechen Li, Carlos Guestrin, Percy Liang, and Tatsunori B Hashimoto. Stanford alpaca: An instruction-following llama model,

2023. 3

- [49] Canwen Xu, Daya Guo, Nan Duan, and Julian McAuley. Baize: An open-source chat model with parameter-efficient tuning on self-chat data. arXiv preprint arXiv:2304.01196, 2023. 3
- [50] Ge Zhang, Yemin Shi, Ruibo Liu, Ruibin Yuan, Yizhi Li, Siwei Dong, Yu Shu, Zhaoqun Li, Zekun Wang, Chenghua Lin, et al. Chinese open instruction generalist: A preliminary release. arXiv preprint arXiv:2304.07987, 2023. 3


- [51] Ning Ding, Yulin Chen, Bokai Xu, Yujia Qin, Zhi Zheng, Shengding Hu, Zhiyuan Liu, Maosong Sun, and Bowen Zhou. Enhancing chat language models by scaling high-quality instructional conversations. arXiv preprint arXiv:2305.14233, 2023. 3
- [52] Or Honovich, Thomas Scialom, Omer Levy, and Timo Schick. Unnatural instructions: Tuning language models with (almost) no human labor. arXiv preprint arXiv:2212.09689, 2022. 3
- [53] Nihal V Nayak, Yiyang Nan, Avi Trost, and Stephen H Bach. Learning to generate instruction tuning datasets for zero-shot task adaptation. arXiv preprint arXiv:2402.18334, 2024.
- [54] Pranav Rajpurkar, Jian Zhang, Konstantin Lopyrev, and Percy Liang. Squad: 100,000+ questions for machine comprehension of text. arXiv preprint arXiv:1606.05250, 2016.
- [55] Alex Wang, Amanpreet Singh, Julian Michael, Felix Hill, Omer Levy, and Samuel R Bowman. Glue: A multi-task benchmark and analysis platform for natural language understanding. arXiv preprint arXiv:1804.07461, 2018. 3
- [56] ICLR conference organizers. International conference on learning representations (iclr). https://openreview.net/group?id=ICLR.cc. 4
- [57] David Soergel, Adam Saunders, and Andrew McCallum. Open scholarship and peer review: a time for experimentation. 2013. 4
- [58] Nature communications. https://www.nature.com/ncomms. 4
- [59] OpenReview. Openreview api. https://github.com/openreview/openreview-py. 4
- [60] Vik Paruchuri. Marker. https://github.com/VikParuchuri/marker. 4
- [61] Kishore Papineni, Salim Roukos, Todd Ward, and Wei-Jing Zhu. Bleu: a method for automatic evaluation of machine translation. In Proceedings of the 40th annual meeting of the Association for Computational Linguistics, pages 311–318, 2002. 7
- [62] Chin-Yew Lin. Rouge: A package for automatic evaluation of summaries. In Text summarization branches out, pages 74–81, 2004. 7
- [63] Satanjeev Banerjee and Alon Lavie. Meteor: An automatic metric for mt evaluation with improved correlation with human judgments. In ACL workshop, pages 65–72, 2005. 7
- [64] Meta. Introducing meta llama 3: The most capable openly available llm to date. 2024. 7
- [65] Jinze Bai, Shuai Bai, Yunfei Chu, Zeyu Cui, Kai Dang, Xiaodong Deng, Yang Fan, Wenbin Ge, Yu Han, Fei Huang, et al. Qwen technical report. arXiv preprint arXiv:2309.16609, 2023. 7
- [66] Aiyuan Yang, Bin Xiao, Bingning Wang, Borong Zhang, Ce Bian, Chao Yin, Chenxu Lv, Da Pan, Dian Wang, Dong Yan, et al. Baichuan 2: Open large-scale language models. arXiv preprint arXiv:2309.10305, 2023. 7
- [67] Aohan Zeng, Xiao Liu, Zhengxiao Du, Zihan Wang, Hanyu Lai, Ming Ding, Zhuoyi Yang, Yifan Xu, Wendi Zheng, Xiao Xia, et al. Glm-130b: An open bilingual pre-trained model. arXiv preprint arXiv:2210.02414, 2022. 7
- [68] Gemma Team, Thomas Mesnard, Cassidy Hardin, Robert Dadashi, Surya Bhupatiraju, Shreya Pathak, Laurent Sifre, Morgane Rivière, Mihir Sanjay Kale, Juliette Love, et al. Gemma: Open models based on gemini research and technology. arXiv preprint arXiv:2403.08295, 2024. 7
- [69] Xiao Bi, Deli Chen, Guanting Chen, Shanhuang Chen, Damai Dai, Chengqi Deng, Honghui Ding, Kai Dong, Qiushi Du, Zhe Fu, et al. Deepseek llm: Scaling open-source language models with longtermism. arXiv preprint arXiv:2401.02954, 2024. 7
- [70] Shaohua Wu, Xudong Zhao, Shenling Wang, Jiangang Luo, Lingjun Li, Xi Chen, Bing Zhao, Wei Wang, Tong Yu, Rongguo Zhang, et al. Yuan 2.0: A large language model with localized filtering-based attention. arXiv preprint arXiv:2311.15786, 2023. 7
- [71] Yaowei Zheng, Richong Zhang, Junhao Zhang, Yanhan Ye, and Zheyan Luo. Llamafactory: Unified efficient fine-tuning of 100+ language models. arXiv preprint arXiv:2403.13372, 2024. 7


