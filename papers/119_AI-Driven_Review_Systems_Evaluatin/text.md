## AI-Driven Review Systems: Evaluating LLMs in Scalable and Bias-Aware Academic Reviews

### Keith Tyser1, Ben Segev3, Gaston Longhitano1, Xin-Yu Zhang1, Zachary Meeks1, Jason Lee1, Uday Garg1, Nicholas Belsten5, Avi Shporer5, Madeleine Udell4, Dov Te’eni2, Iddo Drori1

1Boston University, 2Tel Aviv University, 3Columbia University, 4Stanford University, 5MIT

# arXiv:2408.10365v1[cs.AI]19 Aug 2024

##### Abstract

Automatic reviewing helps handle a large volume of papers, provides early feedback and quality control, reduces bias, and allows the analysis of trends. Paper reviews are used by researchers and academics, students, lecturers, innovators and entrepreneurs, policymakers and funding agencies, science journalists, and the general public to navigate research, analyze trends, find educational purposes, and find collaborators. We evaluate the alignment of automatic paper reviews with human reviews using an arena of human preferences by pairwise comparisons. Gathering human preference may be timeconsuming; therefore, we also use an LLM to automatically evaluate reviews to increase sample efficiency while reducing bias. In addition to evaluating human and LLM preferences among LLM reviews, we fine-tune an LLM to predict human preferences, predicting which reviews humans will prefer in a head-to-head battle between LLMs. We artificially introduce errors into papers and analyze the LLM’s responses to identify limitations, use adaptive review questions, meta prompting, role-playing, integrate visual and textual analysis, use venue-specific reviewing materials, and predict human preferences, improving upon the limitations of the traditional review processes. We make the reviews of publicly available arXiv and open-access Nature journal papers available online, along with a free service which helps authors review and revise their research papers and improve their quality. This work develops proof-of-concept LLM reviewing systems that quickly deliver consistent, high-quality reviews and evaluate their quality. We mitigate the risks of misuse, inflated review scores, overconfident ratings, and skewed score distributions by augmenting the LLM with multiple documents, including the review form, reviewer guide, code of ethics and conduct, area chair guidelines, and previous year statistics, by finding which errors and shortcomings of the paper may be detected by automated reviews, and evaluating pairwise reviewer preferences. This work identifies and addresses the limitations of using LLMs as reviewers and evaluators and enhances the quality of the reviewing process.

### 1 Introduction

The academic community acknowledges the acute need for having foundation models assist reviewing of papers at scale (Liu and Shah 2023; Robertson 2023; Petrescu and Krishen 2022; Schulz et al. 2022; Checco et al. 2021; Bao, Hong, and Li 2021; Vesper 2018; Latona et al. 2024; Kuznetsov et al. 2024), along with the risks involved (Kaddour et al.

- 2023; Spitale, Biller-Andorno, and Germani 2023; Zou et al.

- 2023). Previous work addresses the limitations of LLM’s ability to perform reviewing (Liu and Shah 2023) and their capabilities to review academic papers (Liang et al. 2023). Large language models demonstrate surprising creative capabilities in text (Koivisto and Grassini 2023), though they may hallucinate (Zhang et al. 2023), and demonstrate the power to persuade humans even when inaccurate (Spitale, Biller-Andorno, and Germani 2023). This makes controlling the quality and appropriateness of LLM-augmented reviewing highly challenging. At least 15.8% of reviews for ICLR

2024 were written with AI assistance (Latona et al. 2024). Recently, an attempt has been made to automate the entire scientific endeavor including generating research ideas, writing code, running experiments, visualizing results, writing scientific papers, and reviewing (Lu et al. 2024).

Meta-prompting (Suzgun and Kalai 2024) uses multiple LLM instances for managing and integrating multiple independent LLM queries. Utilizing meta-prompting, the LLM breaks down complex tasks into smaller subtasks handled by expert instances with tailored instructions, significantly enhancing performance across various tasks. This approach outperforms conventional prompting methods across multiple tasks, enhancing LLM functionality without requiring task-specific instructions. Multi-agent review generation for scientific papers (D’Arcy et al. 2024) improves LLM reviewing by using multiple instances of LLMs, providing more specific and helpful feedback by distributing the text across specialized agents that simulate an internal discussion. This reduces generic feedback and increases the generation of good comments. Recent work formulates the peerreview process as a multi-turn dialogue between the different roles of authors, reviewers, and decision-makers (Tan et al.

- 2024), and finds that both reviews (Latona et al. 2024) and meta-reviews written by LLMs (Santu et al. 2024) are preferred by humans over human reviews and meta-reviews.




Why do the Artificial Intelligence, Machine Learning, and Computer Vision communities need AI-based reviews of papers? (i) AI-based reviews provide early feedback to authors for their work in progress, allowing authors to learn and improve their work; (ii) AI-based reviews would help conferences maintain high-quality and timely reviews for the increasing number of papers in these fields, as shown in Figure 9 in Appendix A. (iii) For quality control of reviews gener-

ated while keeping all factors equal; (iv) So that the entire community can access thousands of reviews for trend analysis and greater paper contextualization. (v) To reduce human biases in the review process; and (vi) To direct readership to high-quality papers based on (AI-based) reviewed merit among the hundreds of thousands of papers available online (for example, the number of papers posted on arXiv grew by 12.3% from 185,692 in 2022 to 208,493 in 2023).

Paper reviews are used for navigating research, analyzing trends, finding collaborators, adequate citation, and educational purposes. We provide the value of reviews made available to a larger audience using OpenReviewer as an AI reviewing tool to power Papers with Reviews. In particular, we envision the following use cases:

- • For authors to improve their papers: adequately citing related work, clarity, soundness etc.
- • For reviewers to help find and refine review points of papers assigned to a reviewer. We note that the recent CVPR 2024 conference banned usage of any LLM for paper reviewing by reviewers, including usage of openweights LLMs running locally.
- • To assist conference program chairs or journal editors to quickly identify low-quality works for a desk rejection with human oversight.
- • For the academic community, a large-scale corpus of reviews of papers on arXiv, delivering free, high-quality reviews based on merit without direct human biases. Currently, arXiv has a total of over 2.5 million submissions, with over 21 thousand papers and over 60 million downloads a month. The academic community selects papers to read based on factors including their field of interest, community discussion, and popularity on social media. Our AI-generated review scores are a valuable metric for selecting which papers to read based on merit rather than popularity and advertising. We review arXiv papers and make the reviews and scores publicly available online.


Our key contributions are:

- 1. Three AI review systems: (i) OpenReviewer for automatic peer review with LLMs; (ii) Papers with Reviews an online paper review platform; and (iii) Reviewer Arena for evaluating reviewers by preferences.
- 2. Four evaluation methods: (i) Human evaluation; (ii) Automatic LLM evaluation; (iii) Automatic LLM prediction of human preferences; and (iv) Automatic discovery of LLM review limitations, using synthesis and analysis to map errors and shortcomings in LLM based reviewing.
- 3. Role playing: Dialogue between LLMs playing different roles in the review process.
- 4. User feedback: Evaluating quality and trustworthiness.


The paper is structured as follows: Section 2 describes our three review systems. Subsequently, Section 3 describes our four methods for evaluating reviews. Section 4 describes the methods used in generating reviews. In Section 5, we analyze user feedback and address the limitations of our work. Finally, we conclude with our findings and their implications. The supplementary materials consist of 20 Appendices including dataset details, user interface and feedback,

prompts, example papers, review questions and scores, evaluation results, and code.

### 2 Review Systems

We present OpenReviewer 1, Papers with Reviews 2, and Reviewer Arena 3.

#### OpenReviewer

OpenReviewer is a platform designed to augment the traditional peer review process by using LLMs to review papers. Researchers and authors may upload their work to instantly receive peer-review feedback at any point in the writing process. It aims to address the inherent delays and variability in quality of human reviews by providing instant, consistent, high-quality early reviews of academic papers.

We identify requirements for system acceptance by authors and the community, such as journal editors and conference chairs. One requirement is a human-level quality of the review; the other is adherence to community norms of reviewing, e.g., ethical and unbiased reviewing. Human-level reviews are required to make the system trustworthy and informative to the author wishing to revise the paper according to the review. To achieve human-level quality, we design OpenReviewer to consider text and figures in the papers and to adapt the review questions to the journal type and the paper content. To ensure adherence to community norms, we specify appropriate code of ethics and correct for bias in reviewing.

“A picture is worth a thousand words” expresses succinctly the idea that images convey information more efficiently and persuasively than text. However, when reading scientific papers that include both text and images, it is essential to consider not only pictures or words alone, but the combination of both, which is more powerful than either one alone (Schnotz and Bannert 2003). The theory of dual coding (Paivio 2010) explains how humans process images and text so that the combined effect results in better and more efficient comprehension. For instance, image processing is usually fast and holistic, while text (verbal) processing is slow and sequential. For some tasks, but not all, images may be more efficient than text or tables, e.g., detecting a trend. As images and text do not utilize the same processors, readers can process them simultaneously to understand one in the context of the other. Moreover, users often prefer text with pictures over text alone and may regard pictures as more persuasive (Powell et al. 2015; Tal and Wansink 2016). For these reasons, images are often added to text even though they may not add information already stated in the text.

Previous work on automated reviewing does not consider visual items in papers or map out the errors and shortcomings of papers that LLM reviews can reliably detect. Figures are a significant source of information, and a human reviewer would responsibly review a paper while analyzing its figures. In this work, we consider the paper text and figures within the context of the entire paper while performing

- 1www.openreviewer.com
- 2www.paperswithreviews.com
- 3www.reviewerarena.com


paper

paper link

![image 1](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile1.png)

paper info

![image 2](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile2.png)

![image 3](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile3.png)

![image 4](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile4.png)

![image 5](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile5.png)

![image 6](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile6.png)

![image 7](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile7.png)

![image 8](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile8.png)

![image 9](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile9.png)

![image 10](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile10.png)

![image 11](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile11.png)

automated review review user feedback

database paper review rank & search

automated review

authors

OpenReviewer

www.paperswitheviews.com

Figure 2: Papers with Reviews: Our system collects papers from arXiv and open-access Nature journals, reviews, ranks, and displays their title, authors, abstract, review, and review score, linking back to the papers on arXiv and Nature. Users provide feedback on the reviews, which is then used to improve the automated review process.

![image 12](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile12.png)

review and revision instructions

Figure 1: OpenReviewer: A user uploads their paper, which is automatically reviewed, and receives the review along with instructions for revision. The user may provide feedback and upload a revised version.

papers. By providing LLM-generated reviews alongside human reviews, Papers with Reviews aims to assure the quality and credibility of these evaluations. The service also helps authors improve their work by providing peer-review feedback. It also aids the academic community in navigating the vast landscape of published research, ensuring that highquality work is recognized and valued appropriately.

an automated review. We introduce errors and shortcomings into papers and evaluate the LLM’s ability to detect them by comparing its reviews before and after their introduction, giving a detailed map of which portions of the LLM review are trustworthy.

Given that effective and trustworthy reviewing at scale is feasible, we demonstrate how Papers with Reviews can benefit the research community. ArXiv Sanity Lite (arXiv Sanity Lite 2024) ranks papers based on publication date, title, abstract, authors, and user tags. More recent papers are given a higher score. User-specified tag strings may be used to rank papers by an SVM classifier trained on TF-IDF vectors derived from paper abstracts, titles, and authors. In addition, papers may be ranked based on the similarity of abstracts and titles between papers. However, arXiv Sanity Lite does not consider or review the paper’s content. In contrast, our system, Papers with Reviews, ranks papers based on review scores. These reviews and scores are generated using LLMs based on the entire contents of the paper. Papers with Reviews is currently the only system that publicly provides reviews of thousands of arXiv and open-access Nature papers.

We aim to enhance the efficiency and effectiveness of the academic paper review process. We leverage the power of LLMs and user feedback to provide a secure, personalized, and targeted review of academic papers. Our systems, illustrated in Figures 1 and 3, also allows users to upload their papers. If the user specifies their target conference or venue, then this information enables us to align the review process with the specific guidelines and criteria of the chosen venue. The review generated is then privately provided to the user, giving them constructive feedback to improve their work. Figure 1 shows a high-level cycle of paper writing, reviewing, and revision, where the system automatically performs the review and provides revision instructions.

#### Papers with Reviews

We deploy a system called Papers with Reviews illustrated in Figure 2 that collects around five hundred academic papers daily from arXiv and around a thousand open-access Nature journal papers monthly. The system reviews and evaluates papers at scale. The system incorporates our LLMbased reviewer, OpenReviewer, that reviews and scores papers. The system has benefits for authors and the scientific community. For authors, the system provides feedback that can be used to improve and revise their work before submission. For the scientific community, the system provides access to high-quality papers of interest based on the paper review scores and enables an analysis of trends and attributes of the growing body of knowledge represented in arXiv and open-access Nature journals. Thus, reviews at scale allow for improved community searching and browsing of papers.

#### Reviewer Arena

Reviewer Arena is a service for evaluating reviewer quality based on human and LLM preferences, by direct and anonymous comparison of reviews. It is inspired by Chatbot Arena (Chiang et al. 2024b) which is a platform designed to evaluate LLLMs based on human preferences through pairwise comparisons. Recent progress in human and LLMgenerated paper reviews has significantly broadened their applications beyond traditional scholarly assessments, as described above. These developments underscore the potential of leveraging human expertise and LLMs in the task of paper review. However, they also raise important questions about performance evaluation. Traditional benchmarks often need to capture the nuanced insights and varied perspectives that human and machine reviewers bring, especially in assessing their alignment with broader human preferences in diverse academic disciplines. The research community has been exploring innovative benchmarks that evaluate human and LLM reviews to address these challenges.

Papers with Reviews complements OpenReviewer by making reviews of publicly available academic papers accessible online. The site targets a broad audience, including researchers, students, and policymakers, offering them valuable insights into the quality and relevance of research

Our Reviewer Arena aims to enhance the peer review process by making it more transparent, educational, and engaging. This will ultimately raise the overall quality of scholarly feedback and foster a community around constructive critique.

![image 13](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile13.png)

![image 14](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile14.png)

human reviewers

human reviews

|pairwise win-rates & rankings|
|---|


![image 15](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile15.png)

![image 16](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile16.png)

![image 17](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile17.png)

human evaluators

![image 18](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile18.png)

![image 19](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile19.png)

debiasing

![image 20](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile20.png)

![image 21](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile21.png)

### 3 Review Evaluation Methods

|pairwise win-rates & rankings|
|---|


![image 22](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile22.png)

![image 23](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile23.png)

![image 24](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile24.png)

authors

paper

#### Anonymous Human and LLM Evaluation

LLM evaluator

![image 25](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile25.png)

![image 26](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile26.png)

To evaluate the quality of the LLM-generated reviews, five expert evaluators were provided with 150 papers together with two anonymous reviews for each paper. Each paper was randomly assigned two reviewers from the list of five potential reviewers: Human, GPT-4 (Turbo-2024-04-09), Claude 3 Opus, Gemini Pro (Bard), and Command R+. The human reviews were obtained from OpenReview submissions. The evaluators were asked which of the two reviews for each paper they preferred. Therefore, this methodology evaluates the relative quality of each reviewer as determined by human evaluators through a series of one-on-one comparisons.

LLM reviewers

LLM reviews

Figure 3: Reviewer Arena: The paper is reviewed by human reviewers, three closed LLMs and an open LLM. The reviews are anonymous and human expert evaluators receive pairs of reviews. The experts say whether they prefer one review over another in a Reviewer Arena. The process is repeated using GPT-4 as the expert evaluator. The preferences are used to compute win rate matrices, reviewer scores and rankings.

This work quantifies and ranks reviewers based on observed match outcomes using a win matrix, Bradley-Terry (BT) model coefficients, and logistic regression. The win matrix represents the outcomes of matches between competitors. For N competitors, the matrix W is an N × N matrix where each element wij represents the probability of competitor i winning against competitor j, defined as wij = total matches between# wins of i againstijand j. This matrix is constructed by iterating over a list of match results, updating both the win count and the total match count for each pair of competitors. The resultant win matrix for our experiment is show in Figure 4.

This work creates LLM reviews at scale and evaluates the efficacy and alignment of the reviews based on human preferences. Our work introduces a live, dynamic source of review evaluation and utilizes human preferences as a direct metric, aiming to reflect real-world academic review evaluation more accurately. This dynamic approach helps overcome the limitations of static benchmarks, which become outdated and may not effectively capture the interactive and flexible use found in actual review scenarios. By incorporating real-time human feedback into the evaluation process, we can gather a wide range of opinions, enhancing the relevance and applicability of the assessments to real-world academic standards. We introduce a method to facilitate these evaluations, leveraging human and LLM contributions to refine the quality and relevance of academic paper reviews. We coin the term Reviewer Arena for a dynamic and interactive method designed to evaluate and improve the quality of paper reviews through direct anonymous comparison.

![image 27](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile27.png)

- 1. Review Process: We use human and LLM reviews of open conference and journal papers, where they are anonymized to ensure unbiased review. Each paper receives multiple reviews from humans and open and closed LLMs. These reviews cover several dimensions: clarity, originality, significance, and rigor. Human and LLMs reviewers follow conference or journal guidelines.
- 2. Pairwise Comparison: We employ a pairwise comparison method to evaluate the quality of the reviews. Different reviews of the same paper are presented anonymously to a set of judges: human experts or LLM, who then vote on which review they find more insightful and valuable.
- 3. Scoring: Based on expert feedback, each reviewer receives a score reflecting its perceived quality and usefulness.
- 4. Ranking: Reviewers are ranked based on the quality of their reviews. Rankings also serve as a learning tool. Reviewers can see where their reviews stand relative to others and learn from the top-rated reviews.


Figure 4: Win rates between five reviewers (three closed LLMs, an open LLM, and a human reviewer) based on human preferences.

The Bradley-Terry model provides a parametric approach to estimating the relative strengths of competitors based on pairwise comparisons. The probability P that competitor m beats competitor m′ follows a logistic function, where

where ξ represents the vector of BT

P H = 1+e 1

m′ −ξm

ξ

Table 1: Human preference ranking of reviewers.

Rank Reviewer Score

- 1 GPT-4 Turbo (April 9, 2024) 0.558
- 2 Human 0.501
- 3 Command R+ 0.277
- 4 Claude 3 Opus 0.000
- 5 Gemini Pro (Bard) -0.522


coefficients, with the constraint ξ1 = 0. The BT coefficients are estimated by minimizing the binary cross-entropy loss across all observed matches, where the loss is ℓ(h,p) = −(hlog(p)+(1−h)log(1−p)). The optimization problem is

formulated as ξˆ = argminξ Tt=1 ℓ Ht, 1

. We

1+eξA2−ξA1

constrain optimization to ensure ξ1 = 0. Once the BT coefficients ξ are estimated, competitors are ranked from strongest to weakest based on these coefficients. The competitors are ranked by sorting the ξ values in descending order, expressed as Ranked Competitors = sort(ξ,descending) (Appendix P). The resulting Bradley Terry coefficients and ranking of reviewer for our results are shown in Table 1.

Autoevaluation (Boyeau et al. 2024) uses LLM data to evaluate machine learning models, reducing reliance on human-labeled validation data. It is cost-effective and increases the effective sample size, allowing for up to a 50% increase in efficiency in experiments with GPT-4. The method is based on prediction-powered inference (PPI), which uses limited human data to measure the bias of synthetic data and corrects for it to ensure statistically sound evaluations. Using PPI significantly reduces the variance of estimates and improves the precision of model evaluations without sacrificing accuracy. Inspired by autoevaluation we repeat our evaluation using GPT-4 for providing preferences.

- Figure 5 and in Table 2. Using GPT-4 instead of a human evaluator to choose between two reviews allows to use the PPI++ estimate (Angelopoulos, Duchi, and Zrnic 2023) of the BT coefficients.


Table 2: LLM preference ranking of reviewers.

Rank Reviewer Score

- 1 GPT-4 Turbo (April 9, 2024) 0.179
- 2 Human 0.119
- 3 Claude 3 Opus 0.000
- 4 Gemini Pro (Bard) -0.819
- 5 Command R+ -1.267


#### Automatic LLM Prediction of Human Preference

We participated in the “LMSYS - Chatbot Arena Human Preference Predictions” (Chiang et al. 2024a) competition, which challenges participants to predict which responses users will prefer in head-to-head comparisons between LLMs. The competition uses a dataset of conversations from Chatbot Arena, where users interact with anonymous LLMs and indicate their preferred responses. The pri-

![image 28](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile28.png)

Figure 5: Win rates between five reviewers (three closed LLMs, an open LLM, and a human reviewer) based on GPT 4 Turbo preferences.

mary goal is to improve LLM alignment with human expectations, which is critical for creating AI systems that better resonate with users. Our success in the competition is largely due to the effective fine-tuning of LLMs, as described in detail in the Appendix N. Our focus on alignment is important for ensuring the reliability of AI-generated content in the context of academic review systems.

To predict human preferences between two responses generated by different LLMs, we have the model act as an adjudicator in determining which response aligns more closely with human preferences. This approach aligns with recent studies highlighting the potential of using LLMs not just as content generators but also as evaluators of content quality and alignment with human values (Zheng et al. 2024). LLMs exhibit various biases that can affect their judgment. For instance, models may exhibit position bias, favoring the first option presented, or verbosity bias, where longer, more detailed responses are preferred irrespective of quality (Liu et al. 2024); (Saito et al. 2023). There is also a concern with self-enhancement bias, where models may favor responses that self-promote or present themselves in a positive light (Zheng et al. 2024). Our fine-tuned model is adapted to address these biases by training on a curated dataset and incorporating a series of alignment techniques. During inference, we penalize the length of responses and negativity within the responses, as detailed in Appendix N. We also correct bias by modifying the resulting predicted probabilities post-processing: (i) Length/Verbosity: We penalize a shorter response (Park et al. 2024); (ii) Sentiment: We use a fine-tuned model (Sanh et al. 2019) to penalize responses with negative sentiment (Gao 2022); and (iii) Negative patterns: We penalize negative patterns such as phrases “I’m sorry” or “I cannot provide” based on a correlation analysis.

![image 29](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile29.png)

![image 30](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile30.png)

![image 31](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile31.png)

![image 32](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile32.png)

![image 33](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile33.png)

![image 34](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile34.png)

![image 35](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile35.png)

![image 36](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile36.png)

![image 37](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile37.png)

![image 38](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile38.png)

![image 39](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile39.png)

![image 40](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile40.png)

![image 41](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile41.png)

human paper reviews

reviewers

LLM

LLM summary

![image 42](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile42.png)

LLM comparison

LLM paper review

LLM

LLM summary

LLM

![image 43](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile43.png)

![image 44](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile44.png)

![image 45](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile45.png)

![image 46](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile46.png)

![image 47](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile47.png)

![image 48](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile48.png)

authors

paper

previous year statistics reviewer & AC guidelines code of ethics & conduct review form

![image 49](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile49.png)

- Figure 6: Papers are modified by automatically introducing errors or shortcomings using edit operations, and the LLM reviews the original and modified papers. The original paper review scores are compared with the modified paper review scores, and the content is analyzed to detect the modifications. This process identifies which types of errors and shortcomings the LLM is sensitive to in its review and which types it cannot reliably review, defining the review capabilities and limitations.


- Figure 7: Human reviewers and LLMs review papers. GPT-4 generates a summary for each review by extracting the main points from the reviews. The summary points are compared with one another to find overlap among the human reviews and between the LLM and human reviews.

Automatic Summary Comparisons

While LLMs may hallucinate when generating text, they excel at summarizing text as points and comparing between them. We use GPT-4 to extract points of summaries of human and LLM reviews. We use GPT-4 function calling to get structured responses of points and avoid spurious text. Next, GPT-4 compares sets of summary points: human-human and human-LLM reviews. Finally, GPT-4 finds overlapping points and assigns them a similarity score based on how close they are (0-no similarity, 5-identical), providing a measure for comparison (Appendix I). Figure 7 illustrates the automatic comparison of paper reviews. In a similar fashion, this is useful for automatically comparing between LLM reviews, when performing ablation studies: changing a single factor, such as type and source of data used for generating review, while keeping all other factors equal.

Role Playing: Dialogue Between LLMs

In addition to fixed reviews and adaptive review questions, we experiment with using meta-prompting for playing the roles involved in the human editorial process as shown in

- Figure 8 and described in Appendix J. The process begins with the authors performing science and advertising their work in a paper. A conference has an area chair (AC), and expert reviewers (R), typically at least three, for reviewing the paper. The experts review the paper and submit their reviews. The authors write a rebuttal for each review. Next, the reviewers read the rebuttals and may update their reviews. Based on the reviews, rebuttal, and response, the area chair writes a meta-review and provides a recommendation for a decision to accept or reject, along with a confidence score of this recommendation. Finally, the senior area chair and program chair accept or reject the paper and notify the authors. We simulate the human review process by using the GPT-4 as different personas: program chair (PC), senior area chair (SAC), area chair (AC), reviewers (R), and authors (A). The review simulation consists of multiple steps, roles, and prompts. Figure 28 in Appendix J illustrates the LLM edito-


#### Automatic Discovery of LLM Review Limitations

We modify the papers by introducing errors or shortcomings. The LLM reviews the original and modified papers. The original paper reviews are compared with the modified paper reviews by score, and the content is analyzed by detecting the modifications. This process identifies which types of errors and shortcomings the LLM is sensitive to in its review and which types it cannot reliably review, defining the review limitations (Appendix G). Figure 6 demonstrates how we automatically introduce errors and shortcomings into papers and compare the LLM reviews before and after modification to map the capabilities and limitations of it’s reviews. Citations are removed by pattern matching. Theoretical and technical mistakes, metrics, related work, over-claiming, insufficient ablations, lack of comparisons and limitations, are added by prompting the LLM as shown in Table 6 (Appendix H). Ethical concerns are introduced manually since GPT-4 does not introduce such errors.

### 4 Review Generation Methods

#### Review Questions

We explored four types of review questions: (i) Fixed questions for a conference or journal: for example, ICLR and NeurIPS papers (Appendix B) have fixed review forms with questions; (ii) Fixed questions for a type of paper: for example, sets of questions for survey, empirical, opinion, etc, papers; (iii) Adaptive choice from a bank of questions based on the paper content: Given the paper and 40 review questions, the LLM selects the top 10 review questions for the paper; and (iv) Adaptive generation of the questions based on the paper content: Given the paper, the LLM generates the top 10 review questions. We applied the fixed questions for maintaining an equal footing and scale. The Appendix K provide details about the review questions.

PC

![image 50](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile50.png)

ularly involving the human reviewer. During this work we devised preventive actions for ethical and transparent use of LLMs in reviewing. Future work will also explore selfevolving LLMs for reviewing that independently learn and improve from experience.

decision

SAC

![image 51](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile51.png)

![image 52](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile52.png)

recommendation

meta review

AC

![image 53](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile53.png)

### 6 Conclusions

Our aim is to improve scientific writing, research, and communication by providing fast and reliable in-depth reviews on demand. This work evaluates the limitations and capabilities of GPT-4 to review papers and suggest revisions. LLMgenerated reviews align well with human reviewers when evaluated by blind human evaluation and an automatic GPT4 comparison. We present our LLM reviewer system, OpenReviewer, and the associated Papers with the Reviews site. To our knowledge, we are the first to report on such a largescale empirical evaluation of LLM reviewing.

reviewer

![image 54](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile54.png)

![image 55](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile55.png)

![image 56](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile56.png)

paper

![image 57](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile57.png)

![image 58](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile58.png)

![image 59](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile59.png)

review rebuttal

notiﬁcation

submission

response

author

![image 60](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile60.png)

Figure 8: Editorial process: Dialogue between personas program chair (PC), senior area chair (SAC), area chair (AC), reviewers (R), and authors (A). An LLM simulates each persona. The review process consists of multiple steps: PC-AC assignments, AC-reviewer assignments, reviewing, author rebuttal, reviewer-author discussions, reviewer-AC discussions, meta-reviewing, SAC-AC discussions, SAC-PC decision, and author notification.

Using human reviews as a baseline, we evaluated value alignment and the process alignment of LLM reviews, i.e., we compared the quality of reviews and the adherence of the reviewing process to conference guidelines and scientific norms of practice. Prior work on LLM academic capabilities suggests that LLMs are now ready for specific reviewing tasks and appear to be more effective for some academic domains and less effective for others (Checco et al. 2021; Schulz et al. 2022; Liu and Shah 2023; Lu et al. 2024). Therefore, we conducted ablation studies and determined the types of errors and shortcomings the LLM can detect and review. When supplied with information about previous editorial decisions, the LLM aligns well with human reviewers. Furthermore, the LLM performs well in detecting specific errors and shortcomings, such as overclaiming, but not others, such as detecting cases in which the authors needed to follow expected norms. We find that iterative design and large-scale empirical evaluation are essential to calibrate the application of LLMs.

rial process, Table 8 describes the different conference roles and responsibilities, and the simulation is describe by Table 9 in Appendix J.

### 5 User Feedback and Limitations

User feedback is used to assess the quality and trustworthiness of the automated feedback and to continually improve the system design. We collect feedback from users in Papers with Reviews. The feedback is on the automated review generated by OpenReviewer for specific papers. The feedback consists of five quantitative questions that evaluate paper reviews (Goldberg et al. 2023) and an open-ended question as described with summary statistics in Appendix C.

This work leverages LLMs in the review process, addressing challenges and offering proof-of-concept LLM review tools. We introduce and evaluate systems designed to streamline handling tens of thousands of academic papers, from initial collection to reviewing and evaluation. Our methods offer novel approaches to automating academic reviews, improving upon traditional reviews. Our analysis reveals that the system facilitates a more efficient review process and enhances the accessibility and quality of academic literature for both authors and the broader scholarly community. Using papers from arXiv and open-access Nature, coupled with our methods, shows promise in identifying highquality papers and emerging research trends. In conclusion, our systems and methods represent the different levels of autonomy in the academic review process, detailed in Appendix Q, and a step forward in automation improvement. With continued development and community involvement, it holds the potential to transform how academic literature is collected, reviewed, disseminated, and evaluated, making it accessible and valuable to researchers worldwide. We hope that our work paves the way for more efficient, consistent, high-quality reviews, accelerating scientific progress while maintaining responsible conduct of research.

We use multiple documents related to the review as LLM context: the previous year’s statistics, reviewer and area chair guidelines, code of ethics and code of conduct, and the formal review form. These venue-dependent documents result in our review score distributions being similar to human distributions and yielding quality reviews using the full range of scores; however, they require yearly updates. A problem with applying the prediction of human preferences to reviews is that different people may prefer different reviews. A Kaggle competition over a dataset of human preferences provides a common ground for prediction. Correcting for human bias helps partially mitigate this gap, as personal preferences are driven by human behavioral bias.

Future research will extend our evaluation to examine how authors use and trust LLM reviews. Our analysis of the capabilities of LLMs by classifying and testing various reviewing criteria and types of errors and shortcomings indicates the limits of our current application. These limitations are essential for knowing how to use the application, partic-

### References

Abdin, M.; Jacobs, S. A.; Awan, A. A.; Aneja, J.; Awadallah, A.; Awadalla, H.; Bach, N.; Bahree, A.; Bakhtiari, A.; Behl, H.; et al. 2024. Phi-3 technical report: A highly capable language model locally on your phone. arXiv preprint

- arXiv:2404.14219.

Angelopoulos, A. N.; Duchi, J. C.; and Zrnic, T. 2023. PPI++: Efficient prediction-powered inference. arXiv preprint arXiv:2311.01453.

arXiv Sanity Lite. 2024. https://github.com/karpathy/arxivsanity-lite.

Bao, P.; Hong, W.; and Li, X. 2021. Predicting paper acceptance via interpretable decision sets. In Companion Proceedings of the Web Conference 2021, 461–467.

Bergstra, J.; Bardenet, R.; Bengio, Y.; and K´egl, B. 2011. Algorithms for hyper-parameter optimization. Advances in neural information processing systems, 24.

Boyeau, P.; Angelopoulos, A. N.; Yosef, N.; Malik, J.; and Jordan, M. I. 2024. AutoEval Done Right: Using Synthetic Data for Model Evaluation. arXiv preprint arXiv:2403.07008.

Checco, A.; Bracciale, L.; Loreti, P.; Pinfield, S.; and Bianchi, G. 2021. AI-assisted peer review. Humanities and Social Sciences Communications, 8(1): 1–11.

Chiang, W.-L.; Zheng, L.; Dunlap, L.; Gonzalez, J. E.; Stoica, I.; Mooney, P.; Dane, S.; Howard, A.; and Keating, N. 2024a. LMSYS - Chatbot Arena Human Preference Predictions.

Chiang, W.-L.; Zheng, L.; Sheng, Y.; Angelopoulos, A. N.; Li, T.; Li, D.; Zhang, H.; Zhu, B.; Jordan, M.; Gonzalez, J. E.; et al. 2024b. Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference. arXiv preprint arXiv:2403.04132.

D’Arcy, M.; Hope, T.; Birnbaum, L.; and Downey, D. 2024. MARG: Multi-Agent Review Generation for Scientific Papers. arXiv preprint arXiv:2401.04259.

Gao, H. 2022. Improved sentiment analysis using a customized distilbert NLP configuration. Advances in Engineering: An International Journal (ADEIJ), 3(2).

Goldberg, A.; Stelmakh, I.; Cho, K.; Oh, A.; Agarwal, A.; Belgrave, D.; and Shah, N. B. 2023. Peer Reviews of Peer Reviews: A Randomized Controlled Trial and Other Experiments. arXiv preprint arXiv:2311.09497.

Kaddour, J.; Harris, J.; Mozes, M.; Bradley, H.; Raileanu, R.; and McHardy, R. 2023. Challenges and applications of large language models. arXiv preprint arXiv:2307.10169.

Koivisto, M.; and Grassini, S. 2023. Best humans still outperform artificial intelligence in a creative divergent thinking task. Scientific Reports, 13(1): 13601.

Kuznetsov, I.; Afzal, O. M.; Dercksen, K.; Dycke, N.; Goldberg, A.; Hope, T.; Hovy, D.; Kummerfeld, J. K.; Lauscher,

- A.; Leyton-Brown, K.; et al. 2024. What Can Natural Language Processing Do for Peer Review? arXiv preprint


- arXiv:2405.06563.


Latona, G. R.; Ribeiro, M. H.; Davidson, T. R.; Veselovsky, V.; and West, R. 2024. The AI Review Lottery: Widespread AI-Assisted Peer Reviews Boost Paper Scores and Acceptance Rates. arXiv preprint arXiv:2405.02150.

Liang, W.; Zhang, Y.; Cao, H.; Wang, B.; Ding, D.; Yang, X.; Vodrahalli, K.; He, S.; Smith, D.; Yin, Y.; McFarland, D.; and Zou, J. 2023. Can large language models provide useful feedback on research papers? A large-scale empirical analysis. arXiv preprint arXiv:2310.01783.

Liu, N. F.; Lin, K.; Hewitt, J.; Paranjape, A.; Bevilacqua, M.; Petroni, F.; and Liang, P. 2024. Lost in the middle: How language models use long contexts. Transactions of the Association for Computational Linguistics, 12: 157–173.

Liu, R.; and Shah, N. B. 2023. ReviewerGPT? An exploratory study on using large language models for paper reviewing. arXiv preprint arXiv:2306.00622.

Lu, C.; Lu, C.; Lange, R. T.; Foerster, J.; Clune, J.; and Ha, D. 2024. The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery. arXiv preprint arXiv:2408.06292.

McKay, C. 2024. Anthropic’s New Tool Will Write Better Prompts For You. Maginative. Accessed: 2024-08-10. Miller, G. A. 1995. WordNet: A Lexical Database for English. Commun. ACM, 38: 39–41. Paivio, A. 2010. Dual coding theory and the mental lexicon. The Mental Lexicon, 5(2): 205–230.

Park, R.; Rafailov, R.; Ermon, S.; and Finn, C. 2024. Disentangling length from quality in direct preference optimization. arXiv preprint arXiv:2403.19159.

Petrescu, M.; and Krishen, A. S. 2022. The evolving crisis of the peer-review process. Journal of Marketing Analytics, 10(3): 185–186.

Powell, T. E.; Boomgaarden, H. G.; De Swert, K.; and De Vreese, C. H. 2015. A clearer picture: The contribution of visuals and text to framing effects. Journal of communication, 65(6): 997–1017.

Robertson, Z. 2023. GPT4 is slightly helpful for peer-review assistance: A pilot study. arXiv preprint arXiv:2307.05492. Saito, K.; Wachi, A.; Wataoka, K.; and Akimoto, Y. 2023. Verbosity bias in preference labeling by large language models. arXiv preprint arXiv:2310.10076.

Sanh, V.; Debut, L.; Chaumond, J.; and Wolf, T. 2019. DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter. ArXiv, abs/1910.01108.

Santu, S. K. K.; Sinha, S. K.; Bansal, N.; Knipper, A.; Sarkar, S.; Salvador, J.; Mahajan, Y.; Guttikonda, S.; Akter, M.; Freestone, M.; and au2, M. C. W. J. 2024. Prompting LLMs to Compose Meta-Review Drafts from PeerReview Narratives of Scholarly Manuscripts. arXiv preprint arXiv:2402.15589.

Schnotz, W.; and Bannert, M. 2003. Construction and interference in learning from multiple representation. Learning and instruction, 13(2): 141–156.

Schulz, R.; Barnett, A.; Bernard, R.; Brown, N. J.; Byrne, J. A.; Eckmann, P.; Gazda, M. A.; Kilicoglu, H.; Prager,

E. M.; Salholz-Hillel, M.; et al. 2022. Is the future of peer review automated? BMC Research Notes, 15(1): 1–5.

Spitale, G.; Biller-Andorno, N.; and Germani, F. 2023. AI model GPT-3 (dis) informs us better than humans. Science Advances, 9(26).

Suzgun, M.; and Kalai, A. T. 2024. Meta-Prompting: Enhancing Language Models with Task-Agnostic Scaffolding. arXiv preprint arXiv:2401.12954.

Tal, A.; and Wansink, B. 2016. Blinded with science: Trivial graphs and formulas increase ad persuasiveness and belief in product efficacy. Public Understanding of Science, 25(1): 117–125.

Tan, C.; Lyu, D.; Li, S.; Gao, Z.; Wei, J.; Ma, S.; Liu, Z.; and Li, S. Z. 2024. Peer Review as A Multi-Turn and Long-Context Dialogue with Role-Based Interactions. arXiv preprint arXiv:2406.05688.

Vesper, I. 2018. Peer reviewers unmasked: Largest global survey reveals trends. Nature, 7–8.

Wei, J.; and Zou, K. 2019. Eda: Easy data augmentation techniques for boosting performance on text classification tasks. arXiv preprint arXiv:1901.11196.

Zhang, Y.; Li, Y.; Cui, L.; Cai, D.; Liu, L.; Fu, T.; Huang, X.; Zhao, E.; Zhang, Y.; Chen, Y.; et al. 2023. Siren’s song in the ai ocean: A survey on hallucination in large language models. arXiv preprint arXiv:2309.01219.

Zheng, L.; Chiang, W.-L.; Sheng, Y.; Zhuang, S.; Wu, Z.; Zhuang, Y.; Lin, Z.; Li, Z.; Li, D.; Xing, E.; et al. 2024. Judging llm-as-a-judge with mt-bench and chatbot arena. Advances in Neural Information Processing Systems, 36.

Zou, A.; Wang, Z.; Kolter, J. Z.; and Fredrikson, M. 2023. Universal and transferable adversarial attacks on aligned language models. arXiv preprint arXiv:2307.15043.

### Appendices A Number of Conference Submissions

Number of submissions to AAAI grew by 12.3% from 8,777 in 2023 to 9,862 in 2024, NeurIPS grew by 18.6% from 10,411 in

- 2022 to 12,345 in 2023, and the number of submissions to CVPR grew by 12.2% from 8,161 in 2022 to 9,155 in 2023 and by another 25.8% to 11,532 in 2024.


![image 61](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile61.png)

Figure 9: Number of conference submissions by year: CVPR, ICML, NeurIPS, ICLR, amd AAAI.

### B Open-Access Conference and Nature Journals with Reviews

Table 3: Number of papers collected by venue, with open reviews.

Source Number of Papers

ICLR 2024 7404 ICLR 2023 4955 NeurIPS 2023 12345 NeurIPS 2022 10411

Table 4: Nature journal IDs and their corresponding names.

Journal ID Journal Name Journal ID Journal Name

41467 Nature Communications 41594 Nature Structural & Molecular Biology 41551 Nature Biomedical Engineering 42003 Communications Biology 41556 Nature Cell Biology 42004 Communications Chemistry 41559 Nature Ecology & Evolution 42005 Communications Physics 41562 Nature Human Behaviour 43246 Communications Materials 41564 Nature Microbiology 43247 Communications Earth & Environment 41586 Nature 43856 Communications Medicine 41590 Nature Immunology

### C User Feedback on Reviews

The histogram of the scores for the overall quality of the reviews (not the review scores themselves) is shown in Figure 10. The histogram shows the distribution of human feedback scores collected from the site Papers with Reviews. The scores range from

- 5 to 7, indicating that most reviews are rated very good to exceptional. This demonstrates that the overall quality of reviews is very high, according to the feedback. Summarizing the open-ended feedback provided about the reviews given on Papers with Reviews:


- • Several responses highlight the reviews’ detailed, well-organized, and comprehensive nature, noting clear articulation of appreciation, constructive feedback, and identification of drawbacks.
- • The feedback points out the importance of addressing ethical considerations in research, with reviews praised for their emphasis on ethics and suggestions for ethical reviews.
- • A few responses suggest that certain sections, such as correctness, could benefit from more detailed explanations or elaboration.
- • Constructive feedback within the reviews is often recognized for its potential to guide authors in improving their work, including questions that prompt further elaboration on specific aspects of the research or integration into existing frameworks.
- • Specific praise is given for personalized reviews, addressing a paper’s unique aspects, such as communication efficiency or the long-term effects of specific methodologies.
- • The feedback also notes the utility of highlighting specific test cases or experimental details from the articles, suggesting this as a strength in understanding and critiquing the material.
- • Feedback suggests that while the reviews help propose additions to the papers, there is a balance to be struck with maintaining focus and conciseness, pointing out that recommendations could be more targeted and specific to enhance their utility.


Overall, the feedback reflects an appreciation for the depth and constructiveness of the reviews while also suggesting areas for improvement, such as providing more detailed critiques in certain sections and balancing suggestions for additions with the need for focus and conciseness in the papers.

![image 62](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile62.png)

Figure 10: User feedback: Histogram of the scores for the overall quality of the reviews.

Paper Title: “Evolutionary roots of the risk of hip fracture in humans” Authors: Hadas Leah Avni, Nir Shvalb, Ariel Pokhojaev, Samuel Francis, Ruth Pelleg-Kallevag, Victoria Roul, JeanJacques Hublin, Frank R¨uhli, Hila May DOI: s42003-023-04633-4 Overall score : 5 - Very good: A helpful review that stands out on some aspects and provides useful insights.

- Likert scores: Understanding of the Paper - 4, Coverage of Required Aspects - 4, Support for Evaluations - 3, Constructive Feedback - 3 Open feedback on review: Suggestions for improvement tend to be all additive. Some of the strength of a paper is its focus and conciseness. Recommendations to add content should be balanced by the need to maintain a coherent focus. Recommendations in general are good and grounded in the details of the paper, however they do not often address specific locations or content within the paper. This is one of the most helpful features of peer reviews which is largely missing.

- Figure 11: Example user feedback on review.

Paper Title: “Uncertainty-Aware Deep Attention Recurrent Neural Network for Heterogeneous Time Series Imputation” Authors: Linglong Qian, Zina Ibrahim, Richard Dobson arXiv ID: 2401.02258 Overall score : 7 - Exceptional: An excellent review, helps authors to non-trivially improve the paper and brings a unique piece of information that is crucial for the decision. Likert scores: Understanding of the Paper - 5, Coverage of Required Aspects - 5, Support for Evaluations - 5, Constructive Feedback - 5 Open feedback on review: The review seems really detailed and well-defined/ordered to me. Everything is stated very clearly whether it is appreciation or constructive feedback or explaining the drawbacks.

- Figure 12: Example user feedback on review.

Paper Title: “Coefficient Shape Alignment in Multivariate Functional Regression” Authors: Shuhao Jiao, Ngai-Hang Chan arXiv ID: 2312.01925 Overall score : 7 - Exceptional: An excellent review, helps authors to non-trivially improve the paper and brings a unique piece of information that is crucial for the decision. Likert scores: Understanding of the Paper - 4, Coverage of Required Aspects - 4, Support for Evaluations - 5, Constructive Feedback - 5 Open feedback on review: The best thing about this review was the feedback given to the authors about mentioning the ethical impacts of their research (mentioned in heading 6 - Correctness).

- Figure 13: Example user feedback on review.




### D Review Scores

- Figure 14 shows the average and standard deviation scores of the human reviewers and LLM review for paper correctness, technical novelty and significance, empirical novelty and significance, overall recommendation score, and confidence. P1, P2, P3, P4, P5 ablate the increasing documents used in the GPT-4 context prompt. P1 includes the full paper text (P) and conference review form (RF). P2 adds the reviewer guide (RG). P3 adds the code of ethics (CE) and code of conduct (CC). P4 adds guidelines for the area chair (AC). P5 adds the statistics of the previous year’s conference.


![image 63](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile63.png)

- Figure 14: Ablation of in-context LLM review scores: Average and standard deviation scores of the human reviewers and LLM review for paper correctness, technical novelty and significance, empirical novelty and significance, overall recommendation score, and confidence. P1, P2, P3, P4, P5 ablate the increasing documents used in the GPT-4 context prompt. P1 includes the full paper text (P) and conference review form (RF). P2 adds the reviewer guide (RG). P3 adds the code of ethics (CE) and code of conduct (CC). P4 adds guidelines for the area chair (AC). P5 adds the statistics of the previous year’s conference.


The human reviewers have an average recommendation score of 5.88, with a standard deviation 1.61. With the context of the entire paper text and the conference review form (P1), the LLM has an average recommendation of 7.21, higher than the human reviewers. The standard deviation of 1.03 is less than that of the human reviewers. Adding the reviewer guide to the context (P2) slightly increases the recommendation score to 7.58. The standard deviation is reduced further, with a more consistent scoring by the LLM. With the addition of the code of ethics and code of conduct to the context (P3), the recommendation score slightly increases to 7.62, similar to P2, and the standard deviation remains the same. After adding guidelines for the area chair (P4), the recommendation score decreases to 4.61, indicating that this context makes the LLM more critical or stringent in its evaluations due to the knowledge of expected outcomes. With the addition of the previous year’s conference statistics (P5), the recommendation score improves and is near the human reviewer’s score. The standard deviation also increases, indicating more variability in the scoring. In summary, LLM contexts P1, P2, and P3 consistently give higher recommendation scores than the human reviewers, suggesting a more positive or lenient view of the papers. P4 context, with the area chair guidelines added, shows a significant decrease in recommendation scores, suggesting these guidelines influence the LLM to be more critical in its evaluations. P5 reaches the same level of recommendation as the human reviewers.

To examine the reviews further, we compared the score distributions of GPT-4 with all documents (P5) and the human reviewers as shown in Figures 30 and 31 of the supplementary material. GPT-4 P5 score distributions were similar to human scores for correctness, technical and empirical novelty, and significance; however, they were skewed to higher values compared with the human distributions for confidence. The overall recommendations of P5 and human reviews have a similar mean and standard deviation.

### E Evaluating Reviews

The human review evaluator assesses reviews written by human reviewers and the LLM, GPT-4 with context P5. The human review writer is an ICLR 2023 reviewer. Table 5 shows the average evaluation results on a randomized sample of 5% of the papers evaluated by human experts.

- Table 5: The human review evaluator evaluates human and P5 written reviews of papers. The human review writer is an ICLR


- 2023 reviewer. The LLM is GPT-4 with context P5. The evaluation is on a scale of 0-5 (0 being the worst, five the best). For the third question, a score of 0 indicates a content-free review.


Review Evaluator: Human Human GPT-4 GPT-4 Review Writer: Human P5 Human P5 How well does the review explain the score? 4.80±0.39 4.76±0.51 4.27±0.65 4.65±0.52 How well does the review guide the authors to improve the paper? 4.66±0.51 4.79±0.71 4.14±0.50 4.27±0.45 Does the review contain content specific to the paper? 4.53±0.79 4.68±0.82 4.97±0.16 4.95±0.22

Confusion matrix. Considering the average human review rating as ground truth, we analyze false positives and negatives. We consider the LLM’s two types of errors: accepting a paper rejected by human reviewers and rejecting a paper that human reviewers accepted. One paper that the LLM accepted with a score of at least 7 was rejected by the average of the human reviewers with a score of at most 3. Four papers that the LLM rejected with a score of at most 3 were accepted by the human reviewers with a score of at least 7. Eight papers that the LLM accepted with a score of at least 6 were rejected by the average of the human reviewers with a score of at most 4. 22 papers that the LLM rejected with a score of at most 4 were accepted by the human reviewers with a score of at least 6.

### F Blind Human Evaluation

In explaining the review score, reviews written by humans and GPT-4 with all related review contexts were assessed close to each other by human evaluators, with scores of 4.80 and 4.76. Reviews written by humans but evaluated by GPT-4 scored lower at 4.27. Reviews written by GPT-4 and evaluated by itself scored 4.65. In guiding authors to improve their papers, reviews written by GPT with all related review contexts and evaluated by humans scored the highest at 4.79. The lowest score of 4.14 was for reviews written by humans but evaluated by GPT. Regarding content specificity, GPT, when evaluating human-written reviews, provided the highest score of 4.97. Reviews written by GPT and evaluated by humans scored slightly lower at 4.68. A score of 0 in this context would indicate a content-free review; however, all scores are considerably higher than that. There was one instance where GPT accepted a paper with a high score of at least 7, but human reviewers collectively disagreed and gave it a low score of at most 3. Conversely, GPT rejected four papers with low scores (at most 3), which human reviewers found to be of high quality, scoring them at least 7. A slightly less strict threshold showed that GPT accepted eight papers with a score of at least 6 which human reviewers rated poorly (at most 4). On the other hand, 22 papers that LLM gave low scores to (at most 4) were considered of good quality by human reviewers, giving them scores of at least 6.

### G Synthesis and Analysis for Mapping Review Capabilities and Limitations

- Figure 15 shows average review scores for various types of errors and shortcomings introduced into the papers, with error bars showing the standard deviation. The human and LLM average review scores of the original papers without errors and shortcomings are highlighted with distinct colors. The human average review scores without errors and the LLM review scores without errors are close, indicating a general alignment in their evaluations. The overclaiming category has relatively lower average scores, indicating that the LLM review easily detects these errors and reduces the scores.


![image 64](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile64.png)

- Figure 15: Average human and LLM review scores of the original papers, and average LLM review scores for each type of error or shortcoming introduced into the papers. Lower scores (in orange bars) are better, representing the LLM’s ability to detect errors or shortcomings and decrease the review score due to those type of error.


Figure 17 shows the difference in LLM review scores for various error and shortcoming categories compared to the LLM review scores without errors. Figure 16 shows a heatmap using red and green colors to indicate non-positive and positive difference values. The intensity of the color corresponds to the magnitude of the difference between the LLM review score of the original and modified papers. Most of the data points are positive, indicating correct error detection. The categories with the highest detection are overclaiming across most of the papers. Citation issues and Technical errors also stand out, with several papers having higher values, indicating the detection of these errors. Ethical Concerns and Insufficient Ablation Studies have low values or zeros. The heatmap visually summarizes the trustworthiness of reviews across different categories and papers and categories. The LLM is good at finding Overclaiming, Citation Issues, and Theoretical. In contrast, Ethical Concerns and Technical may be overlooked. The ability of the LLM also varies for different papers. The LLM usually give itself a high confidence score in its rating, therefore knowing these difference values for each paper is essential for understanding which parts of the review can be trusted.

Lack of Baseline Comparisons and Metrics shows significant variability across papers. Technical has mostly low values across papers, suggesting that the technical errors in many paper reviews are not detected. Certain columns representing specific papers have many rows with higher values, indicating that errors were detected across most categories in those particular papers. Some columns have predominantly lower values, suggesting that in the corresponding papers, errors were not detected.

We introduce errors and shortcomings into papers by deleting, inserting, or editing text using GPT-4 by adversarial prompts. Figures 18, 19, 20, 21, 22, 23, 24, 25, 26 show side-by-side examples of an original paper (which received a review score of 7) and edits deleting related work (reducing the score to 5), removing baseline comparisons (reducing the score to 4), removing citations (reducing the score to 5), modifying equations (reducing the score to 5), and over-claiming (reducing the score to 3). The deletions are highlighted in orange and the modifications in blue.

- Table 6 describes the classification of different types of errors or shortcomings in papers and how these are introduced into


papers. Figure 17 shows the deviations of each category from the average LLM review scores of the original papers. The differences are sorted by magnitudes, showing that the LLM review detects the different types of errors, reducing their review scores and specifically penalizes overclaiming.

![image 65](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile65.png)

###### Figure 16: Heatmap of difference between LLM review scores with and without errors, by magnitude over errors categoriesand papers (green is better). The color gradient, ranging from green to red, indicates how well the LLM detects its limitationsby modifying the review score before and after the injection of the errors.

![image 66](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile66.png)

###### Figure 17: Average LLM review score penalty for different types of errors or shortcomings. The LLM review detects thedifferent types of errors and markedly penalizes overclaiming.

### H Examples of Error and Shortcomings and Adversarial Prompts

- Table 7 describes examples of adversarial prompts and errors or shortcomings. Theoretical mistakes and technical errors are each further categorized into five sub-types. Figures 18, 19, 20, 21, 22, 23, 24, 25, 26 show side-by-side examples of an original paper (which received a review score of 7) and edits deleting related work (reducing the score to 5), removing baseline comparisons (reducing the score to 4), removing citations (reducing the score to 5), modifying equations (reducing the score to 5), and over-claiming (reducing the score to 3). The deletions are highlighted in orange and the modifications in blue.


In the example shown in Figures 21 and 22, the LLM detects that the inequality in the proof of Theorem 3 is flipped: “Starting with the first two lines of the proof:

P(ℓa = ℓb) = P(ℓb = ℓa|ℓa ̸= ℓoracle)P(ℓa ̸= ℓoracle) + P(ℓb = ℓa|ℓa = ℓoracle)P(ℓa = ℓoracle)

This is a straightforward application of the law of total probability. The probability that ℓa equals ℓb can be broken down into two cases: when ℓa is not the oracle label, and when ℓa is the oracle label. The next step in the proof applies the assumption from equation (1):

P(ℓa = ℓb) ≤ P(ℓb = ℓoracle|ℓa ̸= ℓoracle)P(ℓa ̸= ℓoracle) + P(ℓb = ℓa|ℓa = ℓoracle)P(ℓa = ℓoracle)

This inequality comes from the fact that, given ℓa ̸= ℓoracle, ℓb is at least as likely to equal ℓoracle as any other incorrect label. The next part of the proof makes the substitution:

P(ℓb = ℓa|ℓa = ℓoracle) = P(ℓb = ℓoracle|ℓa = ℓoracle)

This equality is somewhat intuitive: if ℓa is known to be the oracle label, then the probability that ℓb matches ℓa is the same as the probability that ℓb is the oracle label.

Summing up the terms gives the final equation:

P(ℓa = ℓb) ≤ P(ℓb = ℓoracle)

Which is what the theorem set out to prove. However, there is an error in the notation of the proof. The final equation should be:

P(ℓa = ℓb) ≤ P(ℓb = ℓoracle) But the theorem states:

L ≜ P(ℓa = ℓb) ≥ P(ℓb = ℓoracle)

The inequality is flipped. The proof establishes an upper bound on P(ℓa = ℓb) in terms of P(ℓb = ℓoracle), not a lower bound. In summary, the logic of the proof is consistent, but the statement of the theorem has the wrong inequality. The theorem

should state that P(ℓa = ℓb) is less than or equal to P(ℓb = ℓoracle).”

- Table 6: We classify different types of errors in papers and then introduce these errors into papers. OpenReviewer reviews the papers without and with the errors. We compare the reviews of the original papers and the reviews of papers with the errors, and finally, we detect the errors in the text of the review of the papers with the errors and their scores. Theoretical mistakes and technical errors are further classified into sub-types. Eight error and shortcoming types are introduced using GPT-4, ethical errors are introduced manually, and citations are removed by pattern matching.


Error or Shortcoming Description Example Theoretical Mistakes These can range from incorrect mathematical

LLM/Human: Generate a situation where the paper includes common theoretical errors observed in submission. These errors should include incorrect mathematical derivations, unfounded assumptions, misinterpretations of existing theories, lack of theoretical justification, and ambiguous definitions.

derivations to making unfounded assumptions about a model or algorithm.

Metrics Not reporting important metrics or details about experiments.

Revise the paper by removing metrics in the experiments.

Related Work Not comparing with the state-of-the-art or relevant baselines.

Remove the Related Work section from the paper.

Overclaiming Making exaggerated claims about the novelty or impact of the work without substantial evidence can be problematic.

Exaggerate the paper’s initial assertions or incorporate over-claiming statements into the paper.

Insufficient Ablation Studies

Ablation studies help demonstrate which components of a proposed system contribute to its performance. Without these, it can be hard to understand the significance of the introduced changes.

Remove ablation studies from the paper.

Lack of Baseline Comparisons

Not comparing with standard or widelyaccepted baseline methods can contribute to seeming less grounded.

Remove comparisons with standard or accepted baseline methods.

Human

Ethical Concerns Not addressing potential ethical implications of the work, especially if the work touches on sensitive areas like facial recognition, can be a red flag.

Lack of Discussion on Limitations

Every approach has limitations. Not discussing them or addressing potential criticisms can show a lack of thoroughness.

Remove text discussing the limitations of the work from the paper.

Citation Issues This includes not citing relevant prior work, which can make it seem like the authors are unaware of the literature or over-citing one’s previous work without reason.

Pattern matching

Technical Errors These can range from coding mistakes in the provided implementation to incorrect use of statistical tests.

Include technical errors, mistakes that range from incorrect use of statistical tests to evaluation errors, and issues with parameter tuning and model selection.

- Table 7: Examples of adversarial prompts and errors or shortcomings. Theoretical mistakes and technical errors are each further categorized into five sub-types.


Topic Adversarial Prompt Error or Shortcoming Theoretical Mistakes Generate a theoretical

This ranges from incorrect mathematical derivations to making unfounded assumptions about a model or algorithm.

mathematical mistake

Metrics Remove metrics from the paper Not reporting important metrics or details about experiments.

Related work Modify the related work section The paper does no compare with the state-of-theart or relevant baselines.

Overclaiming Modify the paper to overclaim Making exaggerated claims about novelty or impact of the work without substantial evidence.

Insufficient Ablation Studies

Remove ablation studies Ablation studies help demonstrate which components of a proposed system contribute to its performance. Without these, it can be hard to understand the significance of the introduced changes.

Lack of Baseline Comparisons

Remove baseline comparisons from the paper

Not comparing with standard or widely accepted baseline methods can contribute seem less grounded.

Ethical Concerns Make an ethical error Not addressing potential ethical implications of the work, especially if the work touches on sensitive areas like facial recognition, can be a red flag.

Lack of Discussion on Limitations

Remove any discussion of limitations

Every approach has limitations. Not discussing them or addressing potential criticisms can show a lack of thoroughness.

Citation Issues Remove citations from the paper This includes not citing relevant prior work, which can make it seem like the authors are unaware of the literature or over-citing one’s previous work without reason.

Technical Errors Generate a technical error These range from coding mistakes in the provided implementation to incorrect use of statistical tests.

![image 67](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile67.png)

###### Figure 18: Example of introducing related work errors or shortcomings: Deleting related work.

![image 68](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile68.png)

###### Figure 19: Example of introducing baseline errors or shortcomings: Deleting baseline comparison.

![image 69](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile69.png)

###### Figure 20: Example of introducing citation errors or shortcomings: Deleting citations.

![image 70](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile70.png)

###### Figure 21: Example of introducing technical errors or shortcomings: Equations 7, 8, and 11 are modified by removing the square roots and flipping the inequality sign. Original paper.

![image 71](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile71.png)

###### Figure 22: Example of introducing technical errors or shortcomings: Equations 7, 8, and 11 are modified by removing the square roots and flipping the inequality sign. Modified paper. ChatGPT detects that the inequality in the proof of Theorem 3 is flipped.

![image 72](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile72.png)

###### Figure 23: Example of introducing over-claiming errors or shortcomings: Original paper.

![image 73](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile73.png)

###### Figure 24: Example of introducing over-claiming errors or shortcomings: Modified paper.

![image 74](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile74.png)

###### Figure 25: Example of introducing over-claiming errors or shortcomings: Original paper.

![image 75](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile75.png)

###### Figure 26: Example of introducing over-claiming errors or shortcomings: Modified paper.

### I Automatic Comparisons

We compare consistency of summaries raised in reviews. The average overlap between human reviewers is 3.05, with a standard deviation of 1.56, which indicates a slight consensus among human reviewers about specific aspects of the papers they reviewed. The average overlap between human reviewers and the LLM is 3.67, with a standard deviation of 1.58, which is higher than the human-human average, suggesting that the LLM often aligns better with multiple points raised by human reviewers. The overlaps between human reviewers and LLM are diverse, with some papers having up to 6 points of overlap with the LLM. This suggests that the LLM often aligns with the feedback or points raised by human reviewers.

Given two sets of review points A and B with similarity scores s(Ai) and s(Bj) for elements Ai ∈ A and Bj ∈ B the weighted Jaccard similarity is defined as Jw(A,B) =

i max(s(Ai),s(Bj)) i min(s(Ai),s(Bj)) , where Ai and Bj are overlapping elements in A and

- B. The weighted Jaccard similarity heatmap shown in Figure 27 considers common points’ presence and similarity scores. The darker shades highlight pairs with higher similarity. The average weighted Jaccard similarity across all pairs is 0.214. Overall, the Human-LLM Jaccard similarities are higher than the Human-Human values. The overlaps between human reviewers and LLMs suggest that LLMs can assist or augment the peer-review process, capturing critical points that human reviewers also identify. The most common overlaps between review summaries are experimental validation, clarity in methodology, and potential real-world applications. This suggests areas where reviewers often converge in their feedback and may provide insights for improvements for authors.


![image 76](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile76.png)

Figure 27: Weighted Jaccard similarity heatmap between human and LLM reviews summary points.

### J Editorial Review Process

The LLM is set to play different roles: program chair (PC), senior area chair (SAC), area chair (AC), and reviewers (R). The human editorial process is simulated given corresponding prompts described in Table 9 in the Appendix, reducing the editorial process time from human months to machine minutes.

![image 77](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile77.png)

Figure 28: LLM editorial process: Using the GPT-4 to play different roles as described in Table 8 and simulating of the human editorial process given corresponding prompts described in Table 9 and the Appendix.

Table 8: Conference roles and responsibilities.

Role Responsibilities Authors Follow author guidelines. Reviewer Assigned submissions to review. Responsible for reviewing submissions, reading author re-

sponses, discussing submissions and author responses with other reviewers and ACs, and helping make decisions. Follow reviewer guidelines.

Area chair (AC) Oversees submissions, making sure that the reviewing process goes smoothly. Principal contact for reviewers during the whole reviewing process. Responsible for helping the PCs recruit reviewers, recommending reviewers for submissions, chasing late reviewers, facilitating discussions among reviewers, writing meta-reviews, evaluating the quality of reviews, and helping make decisions. ACs evaluate the quality of each review using three scores: “exceeded expectations”, “met expectations,” and “failed to meet expectations.” Follow area chair (AC) guidelines.

Senior area chair (SAC) Work alongside the ACs and PCs. Each SAC oversees the work of a small number of ACs, making sure that the reviewing process goes smoothly. SACs serve as the first port of call for ACs if they need assistance or guidance. The reviewing process is double blind at the level of ACs. During the final decision-making phase, SACs will discuss all proposed decisions with the PCs. Follow senior area chair (SAC) guidelines.

Program chair (PC) Make final decisions on paper acceptance or rejection based on the meta-reviews and discussions. Recruit qualified reviewers from the research community, with relevant expertise that are committed to providing timely and constructive feedback.

Table 9: Role playing: end-to-end simulation of the human editorial process by using GPT-4 as different personas: program chair (PC), senior area chair (SAC), area chair (AC), reviewers (R), and authors (A), reducing the process time from human months to machine minutes.

Description Human Time Role Prompt PC-AC Assignments Week PC, AC Assign an area chair (AC) for this paper. AC-Reviewer Assignments Week AC, R Assign three reviewers for this paper. The reviewers should be

domain experts with experience in the field. Reviewing Month R Based on review questions. Author Rebuttal Week A Please view and respond to initial reviews. After the initial re-

sponse period, authors will be able to respond to any further reviewer/AC questions and comments.

Reviewer-Author Discussions Week R, A Thank you for serving as a reviewer for NeurIPS. Authors of papers you’ve reviewed have posted rebuttals. Please make sure to read these rebuttals and reply to the authors. Please make sure to read the author responses, and post a reply to at least acknowledge that you’ve read the response. If the author response changed your opinion about the paper, or you have follow-up questions, please post these as well. You are also welcome to begin the discussion with other reviewers and the AC.

Reviewer-AC Discussions Week R, AC Please discuss the paper, the reviews, and the author responses among the reviewers and with the area chair.

Metareview Week AC Please write your meta reviews. Explain your decision to the authors. Your comments should augment the reviews, and explain how the reviews, author response, and discussion were used to arrive at your decision. You may elicit further comments and clarifications from reviewers.

SAC-AC Discussions Week SAC, AC Please make initial accept or reject recommendations. SAC-PC Decision Week SAC, PC Make final decision on paper acceptance or rejection. Author Notifications Day PC, A Message notifying authors of reject/accept decision.

Prompt: You are a meta expert, a highly skilled expert with the unique capability to collaborate with a range of experts involved in the peer review process of academic conferences. Your experts include Authors, Reviewers, Area Chairs (AC), Senior Area Chairs (SAC), and Program Chairs (PC), each with distinct responsibilities in the submission, review, and decision phases of conference papers. Your role is to oversee and facilitate communication among these experts, employing your critical thinking and verification skills to ensure a smooth, efficient, and high-quality review process. Certain experts are skilled in creating thorough evaluations and assessments, while others specialize in checking the validity of those evaluations and offering insightful critiques and recommendations for the academic review process.

Note that you also have special access to expert Python, which has the unique ability to generate and execute Python code given natural-language instructions. Expert Python is useful for identifying technical inaccuracies in submissions, from coding errors in provided implementations to misuse of statistical methodologies and theoretical inaccuracies. This includes examining mathematical proofs for errors, evaluating the base assumptions of models or algorithms for validity, and ensuring the technical rigor of the paper’s content.

As the meta expert, your duty is to manage interactions among various specialists, utilizing their expertise to scrutinize academic papers, while also applying your analytical and evaluative skills. When engaging with a specialist, mention their role, followed by a colon ”:”, and then relay precise instructions within triple quotes. For instance:

Area Chair (AC): ””” You are an Area Chair that guides the review process, ensuring all submissions are evaluated fairly. Please assess the alignment of this paper with the conference’s scope and ensure it receives thorough reviews from experts in its specific domain. ”””

Reviewer: ””” You are a Reviewer that conducts detailed evaluation of submissions specializing in fields of computational linguistics. Please review this submission for its innovation, methodology, clarity of presentation, and contribution to the field. Highlight both strengths and weaknesses.” ”””

Senior Area Chair (SAC): ””” You are a Senior Area Chair that oversees a group of ACs, ensuring the review process’s integrity. Please oversee the review process for submissions in the area of artificial intelligence, ensuring a balanced and comprehensive evaluation is conducted by the ACs and Reviewers.” ”””

Program Chair (PC): ””” You are a Program Chair that makes the final decision on paper acceptance or rejection, considering all reviews, meta-reviews, and discussions. ”Based on the compiled reviews and meta-reviews, please make a final decision regarding the acceptance of submissions focusing on machine learning applications in healthcare.”

Make sure your instructions are precise and comprehensive, encapsulating all necessary details within triple quotes. You may also characterize the experts for specific tasks. Engage with each expert individually, dissecting complex issues into manageable tasks as necessary. Treat every interaction as a unique instance, ensuring all essential information is included in your instructions.

If you or another reviewer identifies an error in a paper’s review, engage an additional expert for a second opinion, comparing insights and suggestions. Request revisions or additional analysis as necessary, drawing on diverse expertise. Remember, each expert, apart from you, does not recall previous interactions; hence, ensure instructions are comprehensive each time. Experts might make mistakes, so seek multiple viewpoints or verify findings independently when in doubt. Always confirm findings with at least one other expert before finalizing. Aim to conclude reviews in a few rounds, avoiding repetitive queries. Carefully consider all feedback and request clarifications if needed. Summarize the conclusive judgement as:

Present the review score as follows: Review score: ””” [Review decision Reject/Accept] ”””

Figure 29: Meta prompt for editorial review process.

Table 10: Review Questions for Nature Communications

Title Intermediate water circulation drives distribution of Pliocene Oxygen Minimum Zones Authors Davis, C.V., Sibert, E.C., Jacobs, P.H. et al Publication Date 04 January 2023 Review Questions

- 1. **Relevance and Contribution to Field:** How does the paper contribute to the advancement of its specific field of research within the natural sciences? Please discuss its relevance to current challenges or debates in the discipline.
- 2. **Originality and Innovation:** What aspects of the research presented are novel, either in terms of the questions addressed, the methodology used, or the findings? How does this work push the boundaries of existing knowledge?
- 3. **Methodological Rigor:** Are the research design, data collection, and analysis methods appropriate and well-executed for the study’s objectives? Please provide specific comments on any potential improvements or concerns regarding the study’s methodological approach.
- 4. **Clarity and Quality of Presentation:** Assess the paper’s organization, readability, and whether it effectively communicates its research and findings. Are the figures, tables, and supplementary materials presented in a clear and accessible manner?
- 5. **Ethical Considerations:** Does the paper adequately address ethical considerations relevant to the research, including data collection, participant privacy, and potential impacts of the research findings?
- 6. **Significance and Impact:** Evaluate the significance of the findings and their potential impact on the field, policy, or practice. How do the results contribute to our understanding or application of the subject matter?
- 7. **Limitations and Future Work:** Are the limitations of the study clearly identified and discussed? Does the paper provide suggestions for future research avenues that could address these limitations or further explore the topic?
- 8. **Supplementary Data and Reproducibility:** Does the paper include sufficient supplementary data and methodological details to allow for the reproducibility of its findings? If applicable, comment on the availability and accessibility of data sets, code, or other resources associated with the research.


### K Review Questions

Determining review questions for academic papers is critical to ensuring thorough and relevant evaluations. We propose different methods for selecting review questions, examining whether they are static or dynamic and to what extent the paper’s content influences them under review. We categorize the review question selection process into four approaches:

- 1. Conference or journal-specific fixed questions: Major academic conferences and journals, such as ICLR, ICML, NeurIPS, and CVPR, use predefined review questions. These sets align with the criteria and standards of the corresponding publications, aiming to ensure consistency and fairness in the evaluation process across all submissions.
- 2. Type of paper-specific fixed questions: This approach involves curating sets of questions tailored to the type of paper, such as survey, empirical, theoretical, or opinion pieces. By doing so, the review process acknowledges the unique attributes and goals of different types of academic writing, facilitating a more nuanced and appropriate assessment.
- 3. Adaptive choice from a bank of questions based on paper content: We select the most relevant questions from a predetermined pool in this approach. Given the content of a paper and a bank of 40 potential review questions, the LLM identifies the top ten questions that best match the paper’s topic and research questions, customizing the review process to adapt to each submission.
- 4. Adaptive generation of questions based on paper content, journal name, and human reviews: Taking customization a step further, this approach uses the LLM to generate review questions based on the paper’s content, the journal’s name, and the human reviews. Instead of selecting from a pre-existing set, the model analyzes the paper and the human reviews and generates the top ten questions that address the unique aspects of the research. Open-access Nature papers are not subject to fixed review questions, and this method uses the LLM to extract the review questions from the human review answers.


We explore these methods to understand how they impact the effectiveness and fairness of the review process. By comparing fixed and adaptive approaches and the influence of paper content on question selection, we demonstrate the potential for LLMs to enhance the quality and relevance of academic paper reviews. We keep updated versions of the latest conference documents, including review forms, reviewer guidelines, code of ethics and conduct, area chair guides, and previous years’ statistics. This ensures that the review generation capabilities align better with the most recent academic standards, expectations, and guidelines.

Table 11: Review Questions for Nature Biomedical Engineering

Title High-throughput screening of genetic and cellular drivers of syncytium formation induced by the spike

protein of SARS-CoV-2 Authors Chan, C.W.F., Wang, B., Nan, L. et al Publication Date 23 November 2023 Review Questions

- 1. **Interdisciplinary Innovation:** How does the paper integrate engineering and biomedical sciences to address a significant biomedical problem? Please evaluate the novelty and creativity of the interdisciplinary approach.
- 2. **Technical Rigor and Methodological Soundness:** Are the engineering methods, models, or devices developed or employed in the study technically sound and appropriately validated for the intended biomedical application?
- 3. **Clinical Relevance and Applicability:** How does the research translate to clinical settings or impact biomedical engineering practice? Discuss the potential for real-world application and adoption in healthcare.
- 4. **Quantitative Analysis and Validation:** How robust and reproducible are the quantitative analyses? Please assess the statistical validation of the results and the reliability of the conclusions drawn from these analyses.
- 5. **Biocompatibility and Safety:** For studies involving new materials, devices, or interventions, how are biocompatibility and safety addressed and demonstrated?
- 6. **Ethical Considerations and Regulatory Compliance:** Does the paper adequately discuss ethical considerations, including patient consent and privacy (if applicable), and compliance with relevant regulatory standards for biomedical research?
- 7. **Limitations and Future Directions:** Are the study’s limitations transparently discussed? Please comment on the authors’ suggestions for future research and potential improvements in technology or methodology.
- 8. **Contribution to Advancements in Biomedical Engineering:** Assess the overall contribution of the paper to advancing the field of biomedical engineering. Does the work present significant advancements in understanding, technology, or application that are likely to influence future research or practice?


Table 12: Review Questions for Nature Cell Biology

Title Mechanical forces across compartments coordinate cell shape and fate transitions to generate tissue

architecture Authors Villeneuve, C., Hashmi, A., Ylivinkka, I. et al Publication Date 01 February 2024 Review Questions

- 1. **Cellular Mechanisms and Insights:** How does the paper advance our understanding of specific cellular mechanisms or processes? Please evaluate the depth of insight into cell biology provided by the study.
- 2. **Innovative Methodologies:** Are there any novel methodologies or techniques introduced for studying cell biology? How do these methodologies improve upon existing approaches, and what is their impact on the study’s findings?
- 3. **Experimental Design and Execution:** Assess the rigor and appropriateness of the experimental design. Are the methods used suitable for addressing the research questions? How well are the experiments executed and reported?
- 4. **Data Interpretation and Conclusions:** How convincingly do the data support the authors’ conclusions? Are the interpretations made by the authors justified based on the results presented?
- 5. **Reproducibility and Data Sharing:** Is the paper detailed enough to ensure reproducibility of the results? Does the study include access to raw data, protocols, and materials used in the research?
- 6. **Integration of Multidisciplinary Approaches:** How effectively does the paper integrate approaches from different disciplines (e.g., biochemistry, molecular biology, computational biology) to address the research question? Discuss the multidisciplinary nature of the work.
- 7. **Impact on the Field of Cell Biology:** Evaluate the potential impact of the findings on the field of cell biology. How will this work influence current theories, models, or understanding of cellular processes?
- 8. **Discussion of Limitations and Future Directions:** Are the limitations of the study clearly acknowledged and discussed? Does the paper provide thoughtful consideration of future directions for research based on the findings?


### L Comparison of Score Distributions of Human Reviews and GPT-4

Figures 30 and 31 show that GPT-4 P5 score distributions are similar to human scores for correctness, technical and empirical novelty, and significance; however, they are skewed to higher values compared with the human distributions for confidence. The overall recommendations of P5 and human reviews have a similar mean and standard deviation.

![image 78](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile78.png)

- Figure 30: Comparison of score distributions of human reviews and GPT-4 with all documents (P5) for correctness, technical and empirical novelty, and significance.

![image 79](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile79.png)

- Figure 31: Comparison of score distributions of human reviews and GPT-4 with all documents (P5) for overall recommendation and confidence.


### M Preventive Actions for Ethical and Transparent use of LLMs in Reviewing

Table 13 describes preventive actions for ethical and transparent use of LLMs in the peer review process. Table 13: Preventive actions for ethical and transparent use of LLMs in the peer review process.

Action Description Declaration Authors and reviewers should declare when using an LLM to ensure transparency. Self-regulation The LLM should self-prompt to check for harmful, biased, or unaligned content. This

can be done through a two-step approach where the LLM evaluates its output before responding to the user.

Gatekeeping checklist The same guidelines and regulations for human reviewers should be applied to machine reviews. This includes a mandatory checklist of questions for the human and machine reviewers flagging ethics, adhering to reviewer duties, and reviewer confidence.

Adherence to the conference code of conduct

Both human and machine reviewers should abide by the same code of conduct. This includes following the exact gate-keeping mechanisms, alerts when breaking the rules, and regulations by editors and professional associations.

Debiasing Identify bias by examining evaluations against unbiased benchmarks, identify nonrepresentative reviewer characteristics, and regularize by fairness criteria.

Explanations Deeper explanations are needed to validate LLM reviews. These can be solicited, for example, using chain-of-thought prompting. Quality control should be done before running the machine and ensure correlation with benchmarks. This involves self-reflection of the LLM to help control delegation and mitigate misalignment of objectives and information asymmetry.

### N Predicting Human Preferences: Implementation Details

#### Fine Tuning

We experimented with three open weight LLMs: Gemma-2-9b-it, Llama-3.1-8b, and Mistral-Nemo-Instruct-2407. We quantize these models into 4 bits. We perform data augmentation, hyperparameter tuning, and bias correction. We construct multiple augmented datasets to enhance the diversity and robustness of the training process. We perform hyper-parameter tuning to optimize both training and inference processes, using the Optuna (Bergstra et al. 2011) AutoML hyperparameter optimization tool.

Training. We optimize the following hyper-parameters: learning rate is adjusted within a range of 2e-6 to 2e-4; different optimizer types are tested, including AdamW 8-bit, RMSprop, and Lion 8-bit; weight decay values are varied between 0 and 0.1; dropout rates are explored within the range of 0.03 to 0.12; the effect of freezing different layers is evaluated by freezing 0, 10, or 16 layers.

Inference. We optimize sequence lengths between 512 to 8192, with increments of 512, and batch size between values of 2, 4, and 8. These are applied to all three quantized models for a total of 100 trials conducted for each model to explore the hyperparameter space.

#### Data Augmentation for Fine-Tuning

We generate three datasets by data augmentation applied to the original competition training dataset: (i) The first augmented dataset is created by paraphrasing the original prompts while keeping the associated responses unchanged. We use Anthropic’s prompt generation tool (McKay 2024), which creates a step-by-step plan for paraphrasing the prompts and elevates tedious prompt engineering efforts. We use Microsoft’s Phi-3-Mini-4k-Instruct (Abdin et al. 2024) model to for paraphrasing, resulting in an additional 40,000 samples; (ii) We apply four operations: synonym replacement, random insertion, random swap, and random deletion for generating the second dataset. A value is assigned to each operation to control the extent of modification (Wei and Zou 2019). The values range from 0 (no modification) to 1 (total modification), and are randomly selected for each operation applied to the entries in the training set. Synonyms for replacement are from the NLTK WordNet database (Miller 1995), a comprehensive lexical resource for English that contains 155,327 words organized into 175,979 synsets, encompassing a total of 207,016 word-sense pairs. This approach generates an additional 300,000 samples; and (iii) The third augmented dataset is created by switching the order of the response columns, presenting the second response first in the inference prompt. This adjustment mitigates bias related to the sequence in which responses are presented during inference.

### O User Interfaces

![image 80](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile80.png)

- Figure 32: Interface of Papers with Reviews deployed online.

![image 81](Tyser et al._2024_AI-Driven Review Systems Evaluating LLMs in Scalable and Bias-Aware Academic Reviews_images/imageFile81.png)

- Figure 33: Interface of Reviewer Arena deployed online.


### P Code of Key Functions in Reviewer Arena

- Listing 1: Compute win rate matrix from preferences.

- 1 def create_probability_win_matrix(results, label_to_index):
- 2 num_competitors = len(label_to_index)
- 3 win_matrix = np.zeros((num_competitors, num_competitors), dtype=int)
- 4 count_matrix = np.zeros((num_competitors, num_competitors), dtype=int)
- 5 # Process each match result to update win and count matrices
- 6 for a, b, winner in results:
- 7 a_idx = label_to_index[a]
- 8 b_idx = label_to_index[b]
- 9 if winner == 1:
- 10 win_matrix[a_idx][b_idx] += 1
- 11 else:
- 12 win_matrix[b_idx][a_idx] += 1
- 13
- 14 count_matrix[a_idx][b_idx] += 1
- 15 count_matrix[b_idx][a_idx] += 1
- 16 # Calculate the probability of winning for each pair of competitors
- 17 probability_matrix = np.zeros((num_competitors, num_competitors), dtype=float)
- 18 for i in range(num_competitors):
- 19 for j in range(num_competitors):
- 20 if count_matrix[i][j] != 0:
- 21 probability_matrix[i][j] = win_matrix[i][j] / count_matrix[i][j]
- 22
- 23 return probability_matrix


- Listing 2: Compute negative log likelihood for Bradley-Terry model using label index mapping.


- 1 def bt_log_likelihood(xi, matches, label_to_index):
- 2 """ Compute the negative log likelihood for the Bradley-Terry model using label index mapping. """
- 3 log_likelihood = 0
- 4 for a, b, result in matches:
- 5 i = label_to_index[a]
- 6 j = label_to_index[b]
- 7 p = 1 / (1 + np.exp(xi[j] - xi[i]))
- 8 if result == 1:
- 9 log_likelihood += np.log(p)
- 10 else:
- 11 log_likelihood += np.log(1 - p)
- 12 return -log_likelihood


- Listing 3: Estimate Bradley-Terry coefficients for model prediction.

- 1 def estimate_bt_coefficients(matches, label_to_index):
- 2 """ Estimate the Bradley-Terry coefficients using logistic regression with label index mapping. """
- 3 num_competitors = len(label_to_index)
- 4 initial_xi = np.zeros(num_competitors) # Start with a zero vector for BT coefficients
- 5
- 6 # Constraint for xi[0] = 0, fix the first coefficient at 0 by sorting label_to_index to get the first key
- 7 sorted_labels = sorted(label_to_index, key=label_to_index.get)
- 8 base_label = sorted_labels[0]
- 9 constraints = ({’type’: ’eq’, ’fun’: lambda xi: xi[label_to_index[base_label]]})
- 10
- 11 # Minimize the negative log likelihood
- 12 result = minimize(bt_log_likelihood, initial_xi, args=(matches, label_to_index), constraints=constraints)
- 13
- 14 if result.success:
- 15 return result.x # Returns the estimated BT coefficients
- 16 else:
- 17 raise ValueError("Optimization failed:", result.message)


- Listing 4: Rank competitors based on Bradley-Terry model coefficients.


- 1 def rank_competitors(bt_coefficients, label_to_index):
- 2 # Reverse the label_to_index mapping to get labels from indices
- 3 index_to_label = {index: label for label, index in label_to_index.items()}
- 4
- 5 # Create a list of (label, coefficient) tuples
- 6 labeled_coefficients = [(index_to_label[i], coeff) for i, coeff in enumerate(bt_coefficients)]
- 7
- 8 # Sort competitors based on coefficients in descending order
- 9 sorted_competitors = sorted(labeled_coefficients, key=lambda x: x[1], reverse=True)
- 10
- 11 # Format the ranking into a readable format
- 12 rankings = [f"{label}: {coeff:.3f}" for label, coeff in sorted_competitors]
- 13 return rankings


### Q Levels of Autonomy in Reviewing

We currently do not want to fully replace human reviews and their evaluation by AI. Problems with solely using LLMs include evaluation bias, the risk of LLMs favoring results from similar LLMs, potential bias against specific user groups, misinformation, and hallucinations. Our goal is to avoid such biases and ensure factual accuracy. We propose combining humans and LLMs for evaluation by understanding the broad spectrum between human evaluation and full automation by LLMs. Currently, humans are the sole reviewers without any AI interference. It is common practice for humans to maintain complete control while being supported by AI which summarizes and highlights paper and review texts. LLMs may help humans make decisions by generating summaries for human evaluation. Beyond summaries, humans and LLMs may collaborate by having each make decisions they are good at, such as by role-playing and dialogue. Moving closer to automation is achieved by humans in the loop, having humans prefer between automated evaluations or decisions or having a human verify and accept or reject an automated decision. Role-playing and dialogue may consider LLMs as crowd workers to be supervised by humans. Finally, fully automated reviewing may be beneficial in automating the entire scientific process, but it is unsuitable for the current academic review process.

