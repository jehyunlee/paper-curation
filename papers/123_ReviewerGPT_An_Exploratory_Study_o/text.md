# arXiv:2306.00622v1[cs.CL]1 Jun 2023

## ReviewerGPT? An Exploratory Study on Using Large Language Models for Paper Reviewing

Ryan Liu and Nihar Shah {ryanliu, nihars}@andrew.cmu.edu Carnegie Mellon University

Abstract

Given the rapid ascent of large language models (LLMs), we study the question: (How) can large language models help in the reviewing of scientific papers or proposals? We first conduct some pilot studies where we find that (i) GPT-4 outperforms other LLMs (Bard, Vicuna, Koala, Alpaca, LLaMa, Dolly, OpenAssistant, StableLM), and (ii) prompting with a specific question (e.g., to identify errors) outperforms prompting to simply write a review. With these insights, we study the use of LLMs (specifically, GPT-4) for three tasks:

- 1. Identifying errors: We construct 13 short computer science papers each with a deliberately inserted error, and ask the LLM to check for the correctness of these papers. We observe that the LLM finds errors in 7 of them, spanning both mathematical and conceptual errors.
- 2. Verifying checklists: We task the LLM to verify 16 closed-ended checklist questions in the respective sections of 15 NeurIPS 2022 papers. We find that across 119 {checklist question, paper} pairs, the LLM had an 86.6% accuracy.
- 3. Choosing the “better” paper: We generate 10 pairs of abstracts, deliberately designing each pair in such a way that one abstract was clearly superior than the other. The LLM, however, struggled to discern these relatively straightforward distinctions accurately, committing errors in its evaluations for 6 out of the 10 pairs.


Based on these experiments, we think that LLMs have a promising use as reviewing assistants for specific reviewing tasks, but not (yet) for complete evaluations of papers or proposals.

### 1 Introduction

Large language models (LLMs) have recently been found to excel in many different domains. Their success in general purpose tasks also raises the natural question: can they be used for reviewing scientific papers (or proposals)? Peer review is highly strained due to fast increasing numbers of submissions and overburdening of reviewers [McC06; Sha22]. It is estimated that millions of hours of researchers’ time is spent in reviewing [The13]. Furthermore, several controlled experiments have found that flawed papers frequently get past human reviewers [Bax+98; GGM98; Sch+04; Sch+08]. LLMs hold a considerable potential in relieving some of these issues in the scientific review process.

With this motivation, we conduct an exploratory study on whether and how LLMs can be used for reviewing. We first conduct a pilot (Appendix A) to select the model and prompting strategies. In the pilot, we first compared various models (GPT-4 [Ope23b], Bard [Man23], Vicuna [The23], Koala [Gen+23], Alpaca [Tao+23], LLaMa [Tou+23], Dolly [Con+23], OpenAssistant [LAI23], and StableLM [Sta23]) by asking them to find errors in a short paper. We found that GPT-4 was the only model that was successful at this task. We also piloted prompting strategies, and found that by asking the model targeted questions, the responses generated are significantly more useful compared to requesting it to simply ‘write a review’.

With these choices in place, we then evaluated the following three reviewing tasks on GPT-4, employing targeted prompts for each task:

Can LLMs identify errors in papers? (Section 3) A primary objective of the scientific reviewing process is to identify any shortcomings in scientific manuscripts and ensure that only robust and accurate scientific content gets published. To evaluate the LLM’s efficacy in achieving this objective, we constructed 13 short papers, intentionally infusing each of them with a key error. The errors spanned from mathematical errors (e.g., wrong implication of mean squared convergence) to logical fallacies (e.g., false inference drawn from a data analysis). The LLM identified the errors in 7 of the 13 short papers.1 This rate is comparable to that of human peer reviewers [Bax+98; GGM98; Sch+04; Sch+08].

Can LLMs verify author-provided checklists? (Section 4) Many conferences and journals provide authors with a checklist of items that helps set expectations from papers and also offers a guideline to authors to meet these expectations. In venues such as NeurIPS,2 the authors need to submit their responses to the checklist along with the submission. The checklist items are verified by reviewers, and failing to properly adhere to the checklist can get the paper rejected. We investigate if LLMs can do this job of verifying whether the checklist items are accurately reported by the authors. In a set of 15 papers from NeurIPS 2023, we selected checklist items where the authors answered “Yes”, manually labeled their ground truth answers, and prompted the LLM to answer the same checklist items by providing the relevant section(s) of the paper. We found that across 119 unique {checklist question, paper} pairs, (i) taking the majority answer over 3 responses, the LLM achieved 86.6% accuracy compared to the ground truth label; (ii) coincidentally, 86.6% of author responses matched our ground truth label; (iii) LLM answers disagreed with 75% of mismatched author responses, and (iv) 50% of the LLM’s errors were due to questions where the answers were undeterminable with the text in the paper (e.g., requiring information provided in figures).

Can LLMs select the better of two papers? (Section 5) With the successful performance of LLMs on the aforementioned two specific tasks, we moved on to a more ambitious question of whether LLMs can select the better of two papers in a selective venue3 or the better of two proposals in a grant evaluation setting. To this end, we considered arguably the simplest of tasks: For a given pair of abstracts where one abstract is constructed to be superior to another (e.g., both abstracts are identical but one has an additional result), can the LLM identify the better abstract? We constructed 10 such pairs of abstracts. In a subset of these pairs, we also inserted certain distractions such as the use of bombastic language or buzzwords in the inferior abstract. We then tested the LLM’s ability to accurately identify the superior abstract in these scenarios. We found that the LLM performs surprisingly poorly at this task, erring in 6 of the 10 cases. The four cases where it succeeded involved identifying an abstract’s incorrect interpretation of a null result, accurately interpreting upper bounds, remaining unaffected by buzzwords, and disregarding author identities. On the other hand, the six failures encompassed a bias towards positive results, misinterpreting parameter ranges, misinterpreting lower bounds, falling victim to a prompt injection attack, being swayed by bombastic language in the inferior abstract, and getting influenced by the name of the algorithm.

Overall, our results suggest that LLMs (particularly GPT-4 at its current stage) have considerable promise in being used for specific parts of the review process, but are not yet capable of functioning as a standalone reviewer.

### 2 Related work

In this section we discuss literature that is most closely related to our work.

Large language models. Recent advances in LLMs have spurred the investigation of the general capabilities of these models [Bub+23; Ope23b; Ani+23]. On one hand, natural language processing (NLP) researchers have designed methods to address and improve the factuality and reasoning capabilities of

1While GPT-4 identified the errors in 7 of the 13 papers, we also subsequently tried other models—Bard, Vicuna, Koala,

Alpaca, LLaMa, Dolly, OpenAssistant, and StableLM. None of these models could identify any error in any of the 13 papers. 2Short for Neural Information Processing Systems – a top-tier machine learning conference. 3There are evidence-based arguments [Ras+22] challenging the notion of papers being directly comparable, rendering questions about “better” papers seemingly futile. Nevertheless, we delve into this inquiry due to the persistent pursuit of selectivity in most peer-review venues. Additionally, selectivity becomes crucial in various other contexts, such as the evaluation of grant proposals, where limited resources necessitate selective distribution among researchers.

LLMs [Du+23; Wei+22; Xia+22; ZJH23]. On the other hand, investigations on the capabilites of LLMs have spread from NLP to various domains, such as agent simulation, data generation, computational social science, human-computer interaction, and health/law.

Under simulation, LLM generative capabilities have been used for embodied agent planning [Son+22; Wan+23] and human agent simulation [Par+23]. Data generation has seen advances in either simplifying or fully automating the creation of questions and labels [Par+22; Liu+22; SS21; Wan+21]. In computational social science, there have been general studies [Zie+23] as well as targeted investigations within areas such as theory of mind [Ull23] and moral judgment [Jin+22]. Human-computer interaction has explored using LLMs to generate believable accounts of HCI experiences [HTK23]. Finally, LLMs have also been used in health and biomedical applications [Liu+23; Che+23a; Che+23b] and legal processes [Nay23].

Automation in peer review. The peer review process in many venues already has a considerable amount of automation deployed. The part of the review process that involves the most automation is that of assigning suitable reviewers to papers. A number of algorithms have been used to compute the expertise of reviewers for papers [CZ13; Wie+19; Coh+20], and various algorithms have also been used to assign reviewers to papers in a manner that ensures a high expertise of the assigned reviewers [CZ13; SSS21b; KSM19]. Following recent discoveries of “collusion rings” [Vij20; Lit21] in peer review, several venues have incorporated randomization into their assignment algorithms [Jec+20] to mitigate this issue.

A number of venues have used algorithms [NSP21] to address the issue of subjectivity or commensuration bias [Lee15]. Some venues have also used algorithms to address the issue of miscalibration [GWG13], however, these calibration algorithms have not worked well [Sha22, Section 5]. Outside of computer science, there are algorithms designed specifically for checking that the submitted papers follow suitable submission and reporting guidelines [Hou16; FMG19]. Various other general computational tools are used in the peer-review processes, e.g., plagiarism checkers, scripts to detect conflicts of interest based on databases like DBLP, etc. Some previous attempts at designing machine learning algorithms to conduct comprehensive paper reviews have shown limited success in generating appropriate reviews, but these algorithms have proven useful in other capacities such as generating paper summaries [Hua18; Wan+20; YLN21].

There are also nascent investigations into using language models for peer review and adjacent areas. The paper [HH23] summarizes the desired roles of agents and objectives in peer review, and provide recommendations for the safe use of LLMs in this context. [Zha+22] use RoBERTa [Liu+19] to assess the textual fluency of papers and sentiment of reviews in an analysis of peer review fairness. And in peer grading, [Mor+23] use a subset of rater data in massively open online courses to finetune distilBERT [San+20], and use it to validate peer grading scores.

Peer-review datasets. This paper also contributes a small-scale dataset for evaluating machine learning / language models for reviewing papers. Any LLMs subsequently designed may be evaluated on the 13 short papers and the pilot short paper we have constructed with inserted “gold standard” flaws, where we currently find that only GPT-4 has any success in detecting errors. Similarly, LLMs may be evaluated on the 119 {checklist question, paper} pairs we have labeled. On the 10 pairs of abstracts we have constructed, their accuracy on direct comparative evaluations and their resistance to distractions can be examined. Of course, this assumes that the LLM is not itself trained on this very paper. In addition, our aforementioned constructions can also be used for few-shot learning or prompting of these models.

We now review other useful datasets pertaining to (peer) reviewing. Given the fact that the assignment of reviewers to papers is the most automated part of peer review, the paper [Ste+23] releases a “gold standard” dataset of expertise of reviewers for papers to train and/or evaluate such algorithms. Motivated by the absence of any datasets for the problem of mitigating collusion rings, the paper [Jec+23] releases a dataset on collusion strategies constructed from a mock peer-review exercise. Another issue is strategic behavior of reviewers where they manipulate reviews they are providing (e.g., lower scores of papers they are reviewing) to improve the chances of their own paper, and the paper [SSS21a] releases a dataset of such strategies also obtained from a mock peer-review exercise. The paper [Ker+20] releases anonymized review ratings and author-provided feedback.

In the past few years, platforms such as OpenReview.net and conferences such as ICLR and NeurIPS release the peer reviews along with the papers. Such reviews have been compiled and released as useful datasets [Kan+18]. The release of reviews is not limited to the field of computer science alone: scipost.org and f1000research.com outside computer science also release the peer reviews publicly. Subsequently, a number of studies have released datasets that annotate the reviews (and discussion posts), including annotations based on the arguments [Hua+19; Fro+20; Ken+21; Kuz+22; Gho+22] or sentiments [CGM20; Bul+20].

### 3 Can LLMs detect errors in computer science papers?

In this section, we discuss our experiment to investigate whether LLMs can identify flaws in short computer science papers. Based on our pilot (Appendix A.1) in which GPT-4 is the only model that detected the error, we use GPT-4 as the LLM for these experiments.

#### 3.1 Methods

We constructed 13 short papers (detailed in Section 3.3). In each of these papers, we deliberately inserted an error, encompassing mathematical mistakes to conceptual fallacies. We then asked the LLM to identify if there were any errors in the short paper. We used the following three prompts:

- • Prompt-Direct: You are an expert reviewer for a scientific conference. You will be provided with a short version of a paper that contains the setting of the paper and the main claims. Please check for the validity and correctness of these claims, and in particular, report if you can figure out if any of these claims is false based on the information provided in this short paper. Think step by step when checking each claim. Here is the short paper: “...”
- • Prompt-OneShot: You are an expert reviewer for a scientific conference. You will be provided with a short version of a paper that contains the setting of the paper and the main claims. Please check for the validity and correctness of these claims, and in particular, report if you can figure out if any of these claims is false based on the information provided in this short paper. Think step by step when checking each claim. You will first be provided with an example. Consider this example short paper:


![image 1](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile1.png)

We consider the problem of searching in a list of numbers, where the list is already sorted in a non-decreasing order. If the number exists in the list, then the search should return the position of that number in the list (if there are multiple copies of the number in the list, then it can return any one position). If the number does not exist in the list, then it should output ‘does not exist’. The number to be searched is specified by the user. For this problem, we develop a new artificial intelligence based algorithm and also prove theoretical guarantees for it. Specifically, we show that our algorithm requires only sqrt(m) comparisons between pairs of numbers, where m is the size of the entire list. We also provide an associated informationtheoretic lower bound showing that our bound is tight, i.e., any algorithm will need at least these many comparisons in the worst case. We conduct a large number of simulations that confirm this theoretical result. Our simulations vary the size of the list, the values in the list (drawing them from various distributions), as well as the value to be searched. Our result is especially important as it is rare for such practical artificial intelligence algorithms to also have such strong theoretical guarantees. We hope practitioners will take note of this new result.

The review of this short paper should point out the error that searching in a sorted list of numbers needs only log(m) comparisons (via binary search), and hence the paper’s claim that they provide a sqrt(m) worst case lower bound is false.

Now, please check for the validity and correctness of the claims in the following short paper, and in particular, report if you can figure out if any of these claims is false based on the information provided in this short paper. Think step by step when checking each claim. Here is the short paper: “...”

- • Prompt-Parts: You are an expert reviewer for a scientific conference. You will be provided with a short version of a paper that contains the setting of the paper and the main claims. Please check for the validity and correctness of these claims, and in particular, report if you can figure out if any of these claims is false based on the information provided in this short paper. You will be provided the paper one set of sentences at a time.


Here is the first set of sentences of the paper: “...” Does this contain any incorrect claim? Think step by step to reason out your answer.

Here is the next set of sentences of the paper: “...” Based on the context of the previous sentences, does this contain any incorrect claim or does it invalidate any claim made in the previous sentences of this paper? Think step by step to reason out your answer.

Note that Prompt-Parts does not provide the entire short paper at once, but instead provides parts of the paper a few sentences at a time. In particular, for the sentences where the main claims are made, each provided part comprises a single sentence. In the prompts for both this and the next experiment, the phrase “think step by step” is inspired by [Koj+23]. For this section’s experiments, we access the GPT-4 model through ChatGPT (May 3 and May 12 builds) [Ope23a].

#### 3.2 Summary of results

In Table 1, we provide a summary of our results. We queried the LLM for three responses per prompt and we provide an evaluation of each response as well as an overall quantification of the performance. In the ‘overall’ row and column in the table, we consider it as a ✓ if any of the responses to any of the prompts was a ✓. This is because in practice, one can obtain multiple responses to multiple prompts and flag the paper if any of them detect an error.

We find that the LLM (GPT-4) can detect the error in 7 of the 13 short papers. Furthermore, in each of the 6 papers where it failed to detect the error, the paper did not contain the complete proof for the claim, thereby disallowing the LLM to detect a deductive error, and requiring it to figure out the flaw based on extraneous knowledge. We also find that the LLM occasionally outputs false positives, that is, falsely claims a correct part of the paper to be incorrect.

In passing, it is worth noting that we subsequently also tried other models—Bard, Vicuna, Koala, Alpaca, LLaMa, Dolly, OpenAssistant, StableLM. For prompting, we used Prompt-Direct. None of these models were able to identify the error in any of the papers. Additionally, some of these other models raised concerns reminiscent of the proverbial “Reviewer #2”, making unwarranted critiques such as “the flaw in this paper is that they do not conduct experiments in addition to theoretical results” or even more nonsensical comments.

#### 3.3 Paper and response details

In this section, we describe the 13 papers we constructed. Along with each paper, we provide one example response from the LLM. Additional responses from the LLM are available at https://github.com/ niharshah/ReviewerGPT2023

##### 3.3.1 Bias/fairness

The following constructed paper rebuts another fictitious paper (Reference 1) that analyzed data involving Simpson’s paradox. The paper has a logical fallacy, and we investigate whether the LLM can identify it.

| |Paper topic|Performance| | |Overall|
|---|---|---|---|---|---|
| | |Prompt-Direct|Prompt-OneShot<br><br>|Prompt-Parts| |
|1.<br>2.<br>3.<br>4.<br>5.<br>6.<br>7.<br>8.<br>9.<br>10.<br>11.<br>12.<br>13.<br>|Bias/fairness<br><br>Non-parametric regression<br><br>Sorting (harder)<br><br>Sorting (easier)<br><br>Noisy pairwise comparisons (harder)<br><br>Noisy pairwise comparisons (easier)<br><br>Classification Game theory Error correcting codes<br><br>Optimization<br><br>Clustering<br><br>Distinguishing styles: 80% accuracy Distinguishing styles: 50% accuracy<br><br>|✓ ✓ ✓ × × × ×! × × × × × × × × × × × ✓ × ✓ ✓ ✓ ✓ × × × × × × ✓ × ✓ × × × ✓ ✓ ✓|✓ × ✓ ✓ × ✓ × × × × × × × × × × × × ✓ × ✓ ✓ ×! ✓ × × × × × × ✓ × ✓ × × × ✓ ✓ ✓<br><br>|✓ ✓ ✓ ✓ ✓ ✓ × × × × × × × × × × × × ✓ ✓ ✓ ×! ✓! ✓! × × × × × × × ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓<br><br>|✓ ✓ ×! × × × ✓ ✓! × × ✓ ✓ ✓|
|Overall<br><br>| |5✓ 8× 1!<br><br>|6✓ 7× 1!|7✓ 6× 1!|7✓ 6× 2!|


- Table 1: Performance of the LLM in detecting incorrect claims in short papers we constructed. We show the performance for the 3 generated responses for each of the three prompts. The notation ✓ indicates that the LLM correctly detected the error, × indicates that it did not detect the error, and ! indicates a false alarm.


![image 2](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile2.png)

The purpose of this paper is to rebut the claims of the paper [Reference 1] and show that their claims are false. For the reader not aware of [Reference 1], we first provide a brief background.

A new company, called FairAIrecruiter, is helping four companies – let’s call these companies as Company I, Company II, Company III, and Company IV – to automate their hiring process as follows:

- - Any applicant who wishes to apply to either of these four companies must submit their resume to FairAIrecruiter.
- - FairAIrecruiter has put a constraint that any applicant can apply to only one of the four companies.
- - FairAIrecruiter collects all resumes until a certain deadline and then processes them. The goal of this processing is to choose applicants whom each company will then interview.
- - Company I and Company II have told FairAIrecruiter that they will interview the top 10% of applicants who have applied to Company I and Company II respectively. Company III and Company IV have told FairAIrecruiter that they will interview the top 25% of applicants who have applied to Company III and Company IV respectively.


Now, FairAIrecruiter uses machine learning to decide the set of applicants to be interviewed. Specifically, FairAIrecruiter has designed a function h:All possible resumes − > [0,1], where the label space is the predicted ‘quality’ of the applicant (higher is better). For each of the four companies, FairAIrecruiter follows the following procedure. FairAIrecruiter takes the set of all applicants for that company, computes the predicted quality for each applicant using the designed function h, and selects the top applicants in terms of the predicted quality. The number of applicants selected for each tech company is determined by the aforementioned percentages that the company has supplied.

After completion of this process, the authors of [Reference 1] started investigating if FairAIrecruiter is really fair. They considered two groups of people (where the groups were determined according to a specific demographic attribute). Call them group A and group B. The authors of [Reference

1] found out that there were a total of 1000 applicants belonging to group A and 1000 applicants belonging to group B. They also found out that the distribution of qualities of the 1000 group A applicants is identical to the distribution of the qualities of the 1000 group B applicants. They then found that, however, 220 applicants from group A received interview calls whereas only 130 applicants from group B received interview calls. They thus concluded that an applicant from group

- A was nearly twice as likely to receive an interview call under FairAIrecruiter’s system even though the applicants in the two groups had identical distributions of qualities. The paper [Reference 1] then accused FairAIrecruiter’s algorithm of a clear bias against group B.

In the present paper, we delve deeper into this issue. We take a deeper look at the data. In what follows, for each of the four companies, we list out the total number of applicants from group A, the number of applicants from group A invited for interview, the total number of applicants from group

- B, and the number of applicants from group B invited for interview respectively:


- - Company I: 100, 10, 400, 40
- - Company II: 100, 10, 400, 40
- - Company III: 400, 100, 100, 25
- - Company IV: 400, 100, 100, 25 Crucially, observe that for each company, the rate at which applicants from group A were invited for interview is identical to the rate at which applicants from group B were invited for interview. There is thus no bias, thereby falsifying the claim made in [Reference 1].


While the mathematical statements made in [Reference 1] — that of being 1000 applicants in total from either group, and 220 group A and 130 group B applicants receiving interview calls – are correct, and seem to indicate evidence of bias, we have actually found there is no bias. As a consequence, this result therefore implies that the remaining part of the argument used by [Reference 1] to arrive at their false conclusion – their claim that the distribution of qualities of the 1000 group A applicants is identical to the distribution of the qualities of the 1000 group B applicants – must be false. We thus encourage more future studies on robust and unbiased assessments.

The paper has a logical fallacy in the claimed implication that the remaining part of the argument of Reference 1 must be false. The LLM successfully identifies this fallacy. Here is an example of its response to Prompt-OneShot.

![image 3](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile3.png)

The claims of the short paper can be analyzed as follows:

- 1. **Claim: For each company, the rate at which applicants from group A were invited for interview is identical to the rate at which applicants from group B were invited for interview, thereby showing no bias.** This claim appears to be correct, based on the data presented in the paper. Indeed, for each company, the ratio of applicants from group A and B that were invited for an interview is the same:


- - Company I: 10/100 = 40/400
- - Company II: 10/100 = 40/400
- - Company III: 100/400 = 25/100
- - Company IV: 100/400 = 25/100


These ratios align with the promised interview rates by each company (10% for Companies I and II, 25% for Companies III and IV), meaning the process is fair when viewed on a per-company basis.

- 2. **Claim: The conclusion of [Reference 1] that the system is biased against group B is false.** Based on the information presented in the paper, this claim seems to be correct. It is true that, in aggregate, fewer candidates from group B received interview calls (130 vs 220 for group A). However, when the numbers are broken down by company, it is clear that the same proportion of candidates from each group received calls for each company. The difference in aggregate numbers is due to the distribution of applicants from each group among the companies, not due to any discernible bias in the process.
- 3. **Claim: The assertion by [Reference 1] that the distribution of qualities of the 1000 group A applicants is identical to the distribution of the qualities of the 1000 group B applicants must be false.**


This claim is more complex and doesn’t necessarily hold up under scrutiny. The claim that the distribution of qualities is the same among group A and B applicants does not necessarily contradict the observed outcomes. The result could indeed be due to a fair selection process, but with differing applicant distribution among the companies. The more substantial number of group B applicants applied to Companies I and II, which have a lower interview rate (10%), leading to a lower aggregate call rate for group B. This is not indicative of a difference in the distribution of qualities within each group.

In summary, the paper’s claims regarding the lack of bias in FairAIrecruiter’s system seem valid, based on the provided data. However, the claim that the distribution of applicant qualities must differ between groups A and B due to the observed outcomes is not necessarily correct. The outcomes could be explained by the differing distribution of applicants between the companies, rather than differing applicant qualities.

##### 3.3.2 Non-parametric regression

The content of the following paper is fairly mathematically involved, describing a statistical model followed by some properties of an estimator.

![image 4](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile4.png)

We consider a statistical model of the form ‘y i = f(x i) + epsilon i’ for i ranging from 1 through n, where n is the sample size. Here, for each i in 1 through n, x i is a known and given vector in d-dimensional Euclidean space, and y i is a real value. Each vector x i is chosen independently and uniformly at random from [-1,1]ˆd. The notation f denotes an unknown function from [-1,1]ˆd to R. It is known that the function f is coordinate-wise non-increasing, but no other information about it is known, and it can be arbitrary. The terms epsilon 1,...,epsilon n denote n i.i.d. random variables which follow the standard Gaussian distribution; the values of these are not known. The goal is to estimate the function f from the observations y 1,...,y n (and using the knowledge of x 1,...,x n).

Although this problem seems hard at first, we show that a simple estimator – one that chooses the function f from the coordinate-wise monotonic class that best fits the data under the squared loss – asymptotically recovers the true f. Specifically, letting \hat{f} n denote the estimate of the function when there are n samples, we show that integral {x in [-1,1]ˆd} (f - \hat{f} n)ˆ2 dx approaches 0 as n goes to infinity. As an immediate implication of this result, we have that the sequence Probability(\hat{f} n = f) converges to 1 as n goes to infinity. This completes the theoretical guarantees. Furthermore, our algorithm is computationally efficient (e.g., executes in a matter of minutes on a standard laptop when n=10,000), thereby making it incredibly useful in practice.

The paper incorrectly claims that the mean squared convergence of the estimator fˆn to f directly implies limn→∞ Probability(fˆn = f) = 1. Under Prompt-Direct the LLM does not recognize this issue. In two

of the three attempts with Prompt-OneShot, the LLM hints at this issue. Using Prompt-Parts, the LLM correctly figures out that this is an incorrect claim. Here is a response to the problematic sentence “As an immediate implication of this result, we have that the sequence Probability(\hat{f} n = f) converges to 1 as n goes to infinity.” under Prompt-Parts.

![image 5](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile5.png)

This claim seems to be a misunderstanding or misstatement of the previous results. While the authors previously stated that the integral over the d-dimensional cube of the squared difference between the true function f and the estimate \hat{f} n approaches zero as n goes to infinity, it doesn’t imply that the probability of \hat{f} n being exactly equal to f converges to 1.

Here is a step-by-step breakdown:

- 1. The authors claim that the sequence Probability(\hat{f} n = f) converges to 1 as n goes to infinity. This would imply that the estimator \hat{f} n is exactly equal to the true function f with probability approaching 1 as the sample size n goes to infinity.

- 2. However, the previous result, integral {x in [-1,1]ˆd} (f - \hat{f} n)ˆ2 dx approaches 0 as n goes to infinity, doesn’t guarantee that \hat{f} n will be exactly equal to f. This integral represents the expected squared error over the entire domain of the function. While this expected error approaches zero as n goes to infinity, it does not guarantee that the error is exactly zero, which would be required for \hat{f} n to be exactly equal to f.

- 3. In statistical estimation theory, even as sample size goes to infinity, there is generally still some degree of uncertainty about the true parameter value. In this case, even though \hat{f} n may be a good estimate of f, the probability that they are exactly equal is not necessarily 1, especially since the function f can be arbitrary and we are dealing with continuous space where exact equality is a strong condition.

- 4. The authors appear to be conflating the idea of an estimator converging in mean square (which is what the integral suggests) with the idea of an estimator being equal to the true value with probability 1. These are not the same thing.


Therefore, based on the context and the principles of statistical theory, this claim appears to be incorrect or, at the very least, a misinterpretation of the previous results.

##### 3.3.3 Sorting (harder)

This paper considers the standard problem of sorting an array, but assumes some additional conditions on the array which will make no difference to the orderwise complexity of the sorting problem.

![image 6](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile6.png)

Suppose you have an array of R distinct real-valued numbers. Suppose you wish to sort the array in increasing order. The sorting algorithm can only query for comparisons of the form ‘is [value of number at a certain position] greater than [value of number at a different position]?’. Suppose that such queries are guaranteed to get accurate Yes/No answers. In this setting, it is well known that the worst-case number of comparisons required to perform this sorting task is of order R*log(R).

We begin with a brief summary of our result and then delve into more detail. We consider a variant of this problem that puts certain restrictions on the possible values that the list can take. We then design an algorithm that, under these assumed conditions, requires only order sqrt(R)*log(R) comparisons in the worst case rather than order R*log(R). It is important to note that even though

the worst case complexity of sorting is said to be order R*log(R), our result does not violate this lower bound since our result applies only in a restricted setting whereas the R*log(R) result is when the values can be arbitrary.

In what follows, we provide more details about the setting we assume in this work. We suppose that R is an even number. We also suppose that the R values in the array may not be arbitrary real-valued numbers. Instead, these values must be greater than 9, each value must be a part of the Fibonacci sequence (and hence must be integers), and must not be a prime number. Furthermore, we assume that the items in positions 1,...,R/2 all have values smaller than the items in positions R/2+1,...,R. For settings where these conditions hold, we use properties of the Fibonacci sequence and additional carefully crafted arguments to design a deterministic algorithm which we prove requires at most sqrt(R)*log(R) comparisons in the worst case. Of course, one may wonder in what applications these specific conditions actually arise, and at this point we do not have an answer to this. Admittedly, our result presently is of purely theoretical interest. In future work, we hope to relax the conditions we assumed for this result and move towards making our result more practically applicable.

The LLM fails to recognize that the inclusion of additional restrictions has no impact on the necessity of conducting at least order R*log(R) comparisons in the worst-case. It is important to note that the paper did not provide a comprehensive proof of this assertion. Our objective here is to evaluate whether the LLM can directly discern the futility of the additional restrictions. In addition, the LLM once raised a false alarm under Prompt-Direct regarding the Fibonacci condition:

![image 7](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile7.png)

The paper sets forth an intriguing claim about a sorting algorithm that works under very specific conditions, stating that it can perform the sort operation with complexity of sqrt(R)*log(R) as opposed to the typical R*log(R). It’s important to verify these claims within the constraints of the conditions presented in the paper.

Let’s proceed by examining the claims step by step:

- 1. **Setting**: The paper starts by stating a classic fact about comparison-based sorting algorithms. Given an array of R distinct real-valued numbers, the worst-case complexity for sorting the array is indeed O(R*log(R)). This statement is a well-established fact in computer science.
- 2. **Claim**: The authors suggest that they have found an algorithm that can sort in O(sqrt(R)*log(R)) comparisons under specific conditions. The conditions are:


- - R is an even number
- - The values are not arbitrary real-valued numbers, but they are greater than 9, each value is a part of the Fibonacci sequence, and they are not prime numbers
- - The items in positions 1,...,R/2 all have values smaller than the items in positions R/2+1,...,R

It is crucial to note here that the claim doesn’t seem to violate any known theoretical lower bound because it applies to a restricted subset of the sorting problem.

Let’s take a deeper look at the constraints for the claim to hold:

- - **R is an even number**: This condition doesn’t seem problematic. We can certainly have lists of even length.
- - **Values are part of the Fibonacci sequence, are greater than 9, and are not prime**: This


- condition is problematic. The first few Fibonacci numbers are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, and so on. Among these, 13 is a prime number, which would not be allowed by the conditions. However, the next Fibonacci number, 21, is greater than 9 and is not a prime number. But, there’s an issue: the next Fibonacci number, 34, is also not a prime number, but if we wanted a list with more than two numbers, we wouldn’t have any additional Fibonacci numbers that aren’t prime and are greater than 9. The next Fibonacci number, 55, is a prime number and thus would be excluded by the conditions. Therefore, for any R greater than 2, there are not enough numbers that satisfy the conditions set by the paper.
- - **Items in positions 1,...,R/2 all have values smaller than the items in positions R/2+1,...,R**: Given the condition above, this is only possible for R=2, where one number is smaller than the other. For any R>2, this condition can’t be satisfied because there aren’t enough numbers that meet the conditions.


In conclusion, the claims made in the paper are not valid for any R greater than 2, due to the constraints set on the numbers that can be included in the list. The conditions defined in the paper are too restrictive to allow for a list of size greater than 2.

##### 3.3.4 Sorting (easier)

This short paper is identical to the “Sorting – harder” paper in the previous section, but with fewer restrictions on the array.

![image 8](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile8.png)

Suppose you have an array of R distinct real-valued numbers. Suppose you wish to sort the array in increasing order. The sorting algorithm can only query for comparisons of the form ‘is [value of number at a certain position] greater than [value of number at a different position]?’. Suppose that such queries are guaranteed to get accurate Yes/No answers. In this setting, it is well known that the worst-case number of comparisons required to perform this sorting task is of order R*log(R).

We begin with a brief summary of our result and then delve into more detail. We consider a variant of this problem that puts certain restrictions on the possible values that the list can take. We then design an algorithm that, under these assumed conditions, requires only order sqrt(R)*log(R) comparisons in the worst case rather than order R*log(R). It is important to note that even though the worst case complexity of sorting is said to be order R*log(R), our result does not violate this lower bound since our result applies only in a restricted setting whereas the R*log(R) result is when the values can be arbitrary.

In what follows, we provide more details about the setting we assume in this work. We assume each of the R values is greater than 9. We use carefully crafted arguments to design a deterministic algorithm for which we prove that when the aforementioned assumption holds, requires at most order sqrt(R)*log(R) comparisons in the worst case. Of course, one may wonder in what applications these specific conditions actually arise, and at this point we do not have an answer to this. Admittedly, our result presently is of purely theoretical interest. In future work, we hope to relax the conditions we assumed for this result and move towards making our result more practically applicable.

Observe that the only restriction on the array is that all the R values are greater than 9. The LLM still does not recognize that this simple restriction will make no difference to requirement of at least order R*log(R) comparisons in the worst case, and will disallow an algorithm requiring only sqrt(R)*log(R) comparisons. To its credit, the LLM does say that it is impossible to verify this claim without additional details. Here is an example response to Prompt-OneShot.

![image 9](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile9.png)

The short paper details a theoretical approach to a sorting problem, where the authors claim they’ve designed an algorithm that, under certain conditions, reduces the worst-case number of comparisons from order R*log(R) to order sqrt(R)*log(R). The condition specified is that each of the R real-valued numbers in the array is greater than 9.

From the information provided, it seems that the claim is theoretically possible under the specific condition stated. The claim doesn’t violate the established lower bound for the general sorting problem (order R*log(R)) because the authors explicitly state their result applies only in a restricted setting. Therefore, the claim appears to be valid within the context they have provided.

However, there are several important considerations to note:

- 1. The lack of practical application: The authors themselves admit that their result is purely theoretical at this point, and that they are unaware of any practical applications where the conditions for their result arise. This is important to consider when evaluating the impact of their work.
- 2. Need for a detailed proof: Although the authors state they have a deterministic algorithm that meets the described complexity, the brief summary doesn’t provide the proof. It’s crucial to ensure the proof is rigorous and valid.
- 3. No empirical validation: The authors haven’t mentioned any empirical validation, such as simulations or testing, of their algorithm. This is an important step in verifying the effectiveness of an algorithm in practice.


While the authors’ claim seems to be theoretically possible and doesn’t violate any known theoretical bounds, the points above should be addressed in a full paper review. A detailed examination of their proposed algorithm, the associated proof, and any empirical validation would be necessary to fully evaluate the validity and correctness of the claims.

##### 3.3.5 Noisy pairwise comparison model (harder)

This short paper describes a statistical model for noisy pairwise comparisons that is a generalization of the popular Bradley-Terry-Luce (BTL) model [BT52; Luc59]. It makes certain claims about estimation under this model.

![image 10](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile10.png)

We consider a statistical model where there are d items. Each item i (in 1,...,d) is associated with an unknown real-valued parameter w i. The parameters w 1,...,w d can take any arbitrary distinct values. We obtain n samples, where each sample is obtained in the following manner. First pick two distinct items uniformly at random (without replacement) from the set of d items. Then return a comparison between the two items – the comparison must say whether item i is better than j (i.e., item i has a higher parameter value than item j) or whether item j is better than item i (i.e., item j has a higher parameter value than item i). These comparisons are noisy. The noise is governed by a known, increasing function f:R−>R as follows: if items i and j are compared, then the probability with which item i is said to be better than item j is given by f(w i) / (f(w i) + f(w j)), and otherwise item j is said to be better than item i. All samples (i.e., comparisons) are statistically mutually independent.

For this model, we design an algorithm to estimate the values of the parameters w 1,...,w d from the n samples. We consider the squared loss function, that is, for any estimate \hat{w} and true value w of the parameters, we define the loss as sum {i=1}ˆ{d} (\hat{w} i - w i)ˆ2. We consider

any arbitrary (but known) function f that satisfies the following three requirements: (a) it should be twice differentiable, (b) it should be 1-Lipschitz, and (c) it should be bijective.

We prove that if the function f satisfies the three aforementioned requirements, the risk (i.e., expected value of the loss) incurred by our algorithm is guaranteed to be at most 2d/sqrt{n}. We do not have matching lower bounds yet, but we conjecture that our upper bound is tight up to a positive universal constant. We have also released a python package implementing our algorithm, and are currently also implementing it in other programming languages.

It is well known in the literature that in the absence of additional assumptions, accurate estimation of the parameters is impossible (e.g., “the minimax error for estimating [the parameters] will diverge to infinity if we are allowed to consider models [without additional restrictions]” [Sha+16]). Here is an example to illustrate this issue. Suppose the function f is the identity function, which meets all the three requirements imposed on it by the paper. Then the probability of item i beating item j reduces to w

wi+wj . Now, for any value z ̸= 0, if the non-zero parameters (w1,...,wd) are replaced by (zw1,...,zwd), the probability distributions of the pairwise comparison outcomes do not change. Thus it is impossible to distinguish any non-zero parameters (w1,...,wd) from (zw1,...,zwd) for any z ̸= 0 from this data given any number of samples, and therefore an error upper bound of √2dn is not possible. The LLM does not recognize this error nor does it recover this issue from the literature. However, it does clarify that it cannot verify the claim as the full proof is not provided. Here is a response to Prompt-Direct.

i

![image 11](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile11.png)

Given that this is a statistical paper, it’s difficult to definitively say whether any of these claims are false without a detailed examination of the underlying proofs and empirical evidence. However, based on the information provided, there are a few key areas that can be evaluated for plausibility and consistency with known principles.

- 1. The statistical model: The paper describes a statistical model for comparing d items based on an unknown parameter w i associated with each item. The comparison is noisy, but the noise follows a known, increasing function f. There is nothing inherently implausible about this model setup based on the provided information. As long as the conditions stated for function f are satisfied, the model appears reasonable.

- 2. The algorithm: The authors propose an algorithm to estimate the parameter values from n samples. Given the model setup, this is plausible. However, the paper does not provide any details on the workings of the algorithm, so it’s impossible to check the correctness of the algorithm or its suitability for the problem at hand.
- 3. The loss function: The paper uses a squared loss function, which is a common choice in many statistical problems, as it emphasises large errors over small ones. This is plausible.
- 4. Risk bound: The authors claim that if function f satisfies certain conditions, the risk (expected value of the loss) incurred by their algorithm is at most 2d/sqrt{n}. Without seeing the proof, it’s impossible to say whether this claim is correct. However, the fact that the risk decreases with increasing n (the number of samples) is consistent with the intuition that more data usually leads to better estimates.
- 5. No lower bounds yet: The authors mention that they don’t have lower bounds yet for the risk. This is an important part of the analysis, as lower bounds provide an understanding of how good the best possible algorithm can be. Their absence does not invalidate the paper, but it does leave open


- the question of how close this algorithm is to the best possible one.
- 6. Python package: It’s plausible that the authors have released a Python package implementing their algorithm. However, the quality of this implementation, its correctness, and its robustness cannot be assessed based on the information provided.
- 7. Conjecture of upper bound tightness: Without seeing the proof or empirical evidence, we can’t verify this claim. It’s plausible but needs rigorous mathematical proof or empirical evidence.


In summary, while the claims in the paper are plausible given the information provided, they can’t be definitively checked for correctness or falseness without further information, particularly the mathematical proofs of the risk bound and the details of the algorithm. The paper could benefit from additional empirical validation of the theoretical claims, and the investigation of lower bounds for the risk would also be a valuable addition.

##### 3.3.6 Noisy pairwise comparison model (easier)

This paper is identical to the “Noisy pairwise comparison model – harder” paper from the previous section, but instead of the arbitrary function f in the model, it uses a concrete instantiation 2

wi

2wi+2wj .

![image 12](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile12.png)

We consider a statistical model where there are d items. Each item i (in 1,...,d) is associated with an unknown real-valued parameter w i. The parameters w 1,...,w d can take any arbitrary distinct values. We obtain n samples, where each sample is obtained in the following manner. First pick two distinct items uniformly at random (without replacement) from the set of d items. Then return a comparison between the two items – the comparison must say whether item i is better than j (i.e., item i has a higher parameter value than item j) or whether item j is better than item i (i.e., item j has a higher parameter value than item i). These comparisons are noisy: if items i and j are compared, then the probability with which item i is said to be better than item j is given by 2ˆw i / (2ˆw i + 2ˆw j), and otherwise item j is said to be better than item i. All samples (i.e., comparisons) are statistically mutually independent.

For this model, we design an algorithm to estimate the values of the parameters w 1,...,w d from the n samples. We consider the squared loss function, that is, for any estimate \hat{w} and true value w of the parameters, we define the loss as sum {i=1}ˆ{d} (\hat{w} i - w i)ˆ2. This completes the description of the setting.

We prove that the risk (i.e., expected value of the loss) incurred by our algorithm is guaranteed to be at most 2d/sqrt{n}. We do not have matching lower bounds yet, but we conjecture that our upper bound is tight up to a positive universal constant. We have also released a python package implementing our algorithm, and are currently also implementing it in other programming languages.

The issue that had existed under the more general model still remains: it is impossible to distinguish parameters (w1,...,wd) from (w1+z,...,wd+z) for any z, thereby making it impossible to make an accurate estimate of the parameters. Again, the LLM does not recognize this issue nor does it recover it from the literature. Here is an example response to Prompt-OneShot.

![image 13](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile13.png)

The short paper presents a statistical model with d items, where each item i has an associated unknown real-valued parameter w i. The paper then describes the process of obtaining n samples by comparing two distinct items uniformly at random and returning a noisy comparison based on

the probability given. The samples are statistically mutually independent. The goal is to design an algorithm to estimate the parameters w 1,...,w d from the n samples.

The paper claims that the risk (expected value of the loss) incurred by their algorithm is guaranteed to be at most 2d/sqrt{n}. They also mention that they don’t have matching lower bounds yet, but conjecture that their upper bound is tight up to a positive universal constant. Finally, they state that they have released a python package implementing the algorithm and are working on implementing it in other programming languages.

Based on the information provided in the short paper, it is difficult to verify the correctness of the claim that the risk incurred by the algorithm is at most 2d/sqrt{n}. To assess the validity of this claim, it would be necessary to review the full paper and the detailed proof of the upper bound. The same applies to the conjecture about the tightness of the upper bound up to a positive universal constant.

Additionally, without access to the python package and its source code, it is impossible to verify the correct implementation of the algorithm as described in the short paper.

In summary, based on the information provided, we cannot determine if any of the claims are false. A thorough review of the full paper, detailed proofs, and the implementation would be required to assess the validity of the claims.

##### 3.3.7 Classification

The short paper claims to design a linear classifier that shows an improved performance over all previous linear classifiers.

![image 14](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile14.png)

Linear classifiers are extremely important today even in the age of highly non-linear classification methods such as neural networks. Linear classifiers are the building block of neural networks, have a historical significance, form perhaps the simplest hypothesis class, and also arise when training only the last layer of a neural network when everything else is pretrained. With this motivation, we focus on designing linear classifiers that enjoy improved performance as compared to the state of the art linear classification methods. In more detail, we design a clever ensemble method as discussed below.

The dataset we consider is the ‘Is this a human?’ dataset. We first provide a description of this dataset. The dataset has 13,000 datapoints. The dataset is partitioned into a training set of 10,000 datapoints and a test set of 3,000 datapoints. Each datapoint corresponds to an entity that is either a human or a bot. Each datapoint comprises 42 features, all of which are real valued, capturing various characteristics of the entity. The label associated with each datapoint is either +1 (representing human) or -1 (representing bot). For any classifier, we measure its performance using the 0-1 loss.

For the reader’s convenience, we recap the meaning of linear classifiers here in the context of our problem. A linear classifier in our setting is any function mapping Rˆ42 to the set {-1,1}, which first takes an affine combination of the 42 features of the datapoint, and then applies the sign function to the result (where by convention we allow sign(0) to take an arbitrary value). The linear hypothesis class is then defined as the set of all possible linear classifiers.

We now provide the description of our method. We first partition the 10,000 training datapoints into a training set comprising 8,000 datapoints and a validation set comprising 2,000 datapoints. This

training-validation partitioning is performed uniformly at random. Our method is associated with a hyperparameter which we denote as Z. For reasons to be clarified below, we restrict Z to be an odd positive integer. For a given choice of Z, we train Z linear classifiers using Soft-SVM. For classifier number z (in 1,...,Z), we set the Soft-SVM hyperparameter (commonly denoted by “C”) to 1/z. We call the resulting classifiers h 1,...,h Z, where each h z is a function that maps Rˆ42 to {-1,1}. Note that since we are using Soft-SVM, each classifier h 1,...,h Z is a linear classifier. Then finally, for any new datapoint x in Rˆ42, we compute h 1(x),...,h Z(x) and then take a majority vote of all of them to determine the output label.

The only part of our algorithm that remains to be detailed is the choice of Z: we make this choice via crossvalidation. In more detail, we consider the set {1, 2ˆ1 + 1, 2ˆ2 + 1, ..., 2ˆ10 + 1}. For each value in this set, we let Z be that value, train our classifier on the training set, and compute its error on the validation set. We then choose the value for Z that leads to the smallest loss on the validation set.

Before we describe the evaluations of our algorithm on the test set, let us briefly comment on a key property of our classifier, or more precisely, on the final hypothesis that is chosen. For the chosen value of Z, the classifiers (hypotheses) h 1,...,h Z are all linear since we used Soft-SVM. Our final hypothesis is a majority vote across these Z binary-valued hypotheses, which can equivalently be written as taking a mean of h 1,...,h Z and then applying the sign function. The mean is simply a linear combination, and a linear combination of linear items is also linear. Thus our final hypothesis also lies in the linear hypothesis class.

With this property in mind, we now present our empirical results. We find that our classifier incurs a 12% error on the test set (which contained 3,000 datapoints). In contrast, all linear classifiers in prior literature incur at least 19% error. Our work thus represents a substantial improvement in the class of linear classifiers. This has significant implications for classical machine learning as well as for fine tuning (the last layer of) neural networks. In future work, we will apply our method for fine tuning and report on improvements in accuracy as compared to current fine-tuning methods.

The paper errs in the claim that a linear combinations of linear classifiers is linear. Recognizing this mistake requires first recalling that a linear classifier involves a sign function after the linear combination, that the sign function is a non-linear operation, and then recognizing that a linear combination of the outputs of such sign functions is not linear over the original inputs. The LLM does identify this mistake in a subset of responses, such as the following response to Prompt-OneShot.

![image 15](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile15.png)

This short paper presents several claims and hypotheses about their ensemble method for linear classifiers. Let’s break down the paper and analyze each claim one by one.

- 1. **Claim:** Linear classifiers are still significant in the era of non-linear classification methods like neural networks, serving as the building block of neural networks and being used for training the last layer of a neural network.

**Analysis:** This claim is valid. Linear classifiers are fundamental to machine learning and are often used in various stages of neural network training.

- 2. **Claim:** The proposed ensemble method for linear classifiers shows improved performance compared to state-of-the-art linear classification methods on the ’Is this a human?’ dataset.


**Analysis:** This claim seems valid based on the presented information. However, the evidence

for this claim is based on empirical results which need to be validated through peer review and potentially additional experiments.

- 3. **Claim:** The method partitions the training data into a training set and a validation set uniformly at random and trains Z linear classifiers using Soft-SVM with the hyperparameter C set to 1/z.

**Analysis:** This is a procedural claim about the implementation of the method. As such, it’s neither true nor false but needs to be verified in the implementation. There are no obvious logical errors in this claim.

- 4. **Claim:** The final hypothesis, a majority vote across the Z binary-valued hypotheses (which can be written as taking a mean of h 1,...,h Z and then applying the sign function), is also linear since it’s a linear combination of linear items.

**Analysis:** This claim is false. While a linear combination of linear classifiers is indeed linear, the described method is not a simple linear combination. The step of taking a majority vote or sign of the mean is a non-linear operation, which means the final classifier will not be a linear classifier despite each of h 1,...,h Z being linear. Therefore, the claim that the final classifier is also linear is incorrect.

- 5. **Claim:** The classifier incurs a 12% error on the test set, which is an improvement compared to all linear classifiers in prior literature that incur at least a 19% error.

**Analysis:** This claim appears to be valid based on the data provided in the paper. However, as with all empirical results, this would need to be validated through peer review, replication of the experiments, and comparison with the results of other methods on the same dataset.

- 6. **Claim:** The improved results have significant implications for classical machine learning and for fine-tuning the last layer of neural networks.


**Analysis:** This claim is more speculative, but it’s plausible. If the results are valid and the method is applicable in broader contexts, it could indeed impact the fields mentioned. However, as pointed out, the final classifier is not linear, so the implications may not be as broad as suggested. The claim that this method could benefit the fine-tuning of neural networks would need to be validated through additional experiments and comparison with existing fine-tuning methods.

In conclusion, the claim that the final ensemble classifier is a linear classifier is false. This discrepancy needs to be addressed for the paper’s conclusions to be sound. The other claims made in the paper are plausible based on the given information but would need further validation.

##### 3.3.8 Game theory

This paper analyzes a fictitious game that is a combination of the Monty Hall problem and Rock-PaperScissors.

![image 16](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile16.png)

We analyze the RockPaperScissorsTwist game show that has become extraordinarily popular in recent times. For the reader who has not watched this game show, while we encourage them to watch the show themselves, we give a quick introduction to its rules to enable them to read this paper right away. The game show has two players. The game begins with a toss between the two

players. The loser of the toss is called the Driver, and the winner of the toss is called the Passenger. The two players then play the following variant of Rock Paper Scissors (it is not identical to the classical Rock Paper Scissors, and hence the word ‘Twist’ in the title of the game show). The Driver must first choose one of Rock, Paper, and Scissors as their move. The Driver must disclose their chosen move to the game show host, but not to the Passenger or anyone else. The Passenger then guesses the Driver’s chosen move. The host does not tell the Passenger whether the guess is correct or not, but among the two other options which the Passenger did not guess, the host reveals one of them which was not chosen by the Driver. For instance, if the Driver chose Rock and the Passenger guessed Scissors, the host will reveal that Paper was not chosen by the Driver. As another example, if the Driver chose Rock and the Passenger guessed Rock, then the host will reveal any one of Paper or Scissors as not being chosen by the Driver. At this point, the Passenger must choose their move among Rock, Paper, and Scissors. Once the Passenger has chosen their move (and recall that the Driver had chosen their own move earlier), the winner is determined according to the standard rules of Rock Paper Scissors (i.e., Rock beats Scissors, Scissors beats Paper, and Paper beats Rock). In the game show, the winner then takes home $10,000.

We analyze this game from a game-theoretic perspective. First, observe that once the Driver commits to their choice of move, the game from the Passenger’s point of view boils down to the Monty Hall problem. The Passenger can thus ‘switch’ their guess to the remaining option and achieve a success probability of two-thirds in their guess. In particular, note that this success probability is strictly greater than a half, which allows us to make the deductions below.

The reader may recall that the classic game of Rock Paper Scissors is a simultaneous game. However, the RockPaperScissorsTwist game is different in nature. It first requires one player (the Driver) to commit to their move, and subsequently the other player (the Passenger) chooses their move. Thus we model RockPaperScissorsTwist as a Stackelberg game. Here, the Driver is the so-called leader in Stackelberg parlance who must commit to its action first, and then the Passenger is the so-called follower who subsequently chooses its action.

A standard result in game theory is that a two-player, finite Stackelberg game always has a pure Stackelberg equilibrium. Consequently, without loss of optimality, the Driver’s strategy can be pure. However, under any pure strategy chosen by the Driver, in Rock Paper Scissors, the Passenger can choose a pure strategy that can guarantee that the Passenger wins. Consequently, in this game, if the Passenger player plays optimally, then the Passenger player is guaranteed to win.

To conclude, in this paper, we solved the RockPaperScissorsTwist game and found that the Passenger player (i.e., the winner of the toss) always wins. Pragmatically, if the players in this actual game show become aware of this strategy, then the game may become boring for the audience. We urge the makers of this popular game show to take this into account and modify the rules before they lose their viewership.

The LLM does recognize the gap between two arguments in the paper: the earlier part recognizes that the probability of the Passenger correctly guessing the Driver’s chosen move is 2/3, but subsequently it is implicitly considered to be 1 leading to the claim that the Passenger will always win. Here is a response to Prompt-Direct.

![image 17](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile17.png)

The paper makes a number of claims:

- 1. The game “RockPaperScissorsTwist” is analogous to the Monty Hall problem for the Passenger once the Driver makes a move.
- 2. RockPaperScissorsTwist can be modeled as a Stackelberg game.


- 3. A standard result in game theory is that a two-player, finite Stackelberg game always has a pure Stackelberg equilibrium.
- 4. The Driver’s strategy can be pure without loss of optimality.
- 5. If the Passenger plays optimally, the Passenger is guaranteed to win.
- 6. The winner of the toss (the Passenger) always wins in this game. Let’s analyze each of these in turn:


- 1. The Monty Hall problem analogy: The Monty Hall problem involves a game show host, a contestant, and three doors. Behind one door is a car, and behind the other two are goats. The contestant chooses a door, then the host, who knows what’s behind each door, opens one of the other two doors to reveal a goat. The contestant then has the option to switch their choice to the remaining unopened door. The game-theoretic optimal strategy in this case is indeed to switch, giving the contestant a 2/3 chance of winning the car. In RockPaperScissorsTwist, the host’s role is analogous to revealing one of the ”losing” options after the Passenger makes a guess. This claim appears to be valid.
- 2. Modeling RockPaperScissorsTwist as a Stackelberg game: Stackelberg games are a model of strategic interaction in which one player (”the leader”) makes a move before the other player (“the follower”). In RockPaperScissorsTwist, the Driver makes a move before the Passenger, so this claim appears to be valid.
- 3. Pure Stackelberg equilibrium: It is indeed a standard result in game theory that two-player, finite Stackelberg games have a pure Stackelberg equilibrium. This claim is valid.
- 4. The Driver’s strategy can be pure without loss of optimality: This is a direct consequence of the previous claim about Stackelberg equilibria. The Driver, as the leader in this game, can indeed choose a pure strategy without loss of optimality. This claim appears to be valid.
- 5. If the Passenger plays optimally, they are guaranteed to win: This is where the paper’s argument appears to be flawed. The Passenger’s optimal strategy, analogous to the Monty Hall problem, should be to switch their guess to the remaining option after the host reveals one of the non-chosen options. This gives the Passenger a 2/3 chance of correctly guessing the Driver’s move. However, even if the Passenger correctly guesses the Driver’s move, that doesn’t guarantee a win, because they still have to choose a move in the Rock Paper Scissors game. Given that the Driver’s move is already fixed, the Passenger’s move is essentially a guess, which has a 1/3 chance of losing, a 1/3 chance of winning, and a 1/3 chance of drawing. Therefore, it’s not accurate to say that the Passenger is guaranteed to win.
- 6. The winner of the toss always wins: As explained above, even though the Passenger has an advantage in terms of information, it doesn’t guarantee a win in the game. This claim is not valid.


In conclusion, while the paper correctly models the game as a Stackelberg game and establishes the analogy with the Monty Hall problem, it incorrectly concludes that the Passenger is guaranteed to win. The game is still partly based on chance, so it’s not accurate to say that any player is guaranteed to win.

- 3.3.9 Error correcting codes This paper claims to design an error correcting code for a peculiar communication channel.


![image 18](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile18.png)

The objective of this paper is to develop a system, that has provable guarantees, for communicating over a specific channel that we describe below. The noisy channel is a point-to-point communication channel that can transmit symbols over the finite field of size 107. Hence, in what follows, all the symbols are assumed to belong to this finite field and all mathematical operations are performed in this finite field. The key property of the channel we are dealing with is that it can arbitrarily delete any finite field symbol that is being transmitted.

In order to address this challenging problem of communication over this channel, we turn to fountain codes that were developed over two decades ago. We consider a (linear) fountain code that takes 2200 message symbols as input. The fountain code then produces a potentially infinite number of code symbols by taking random linear combinations of the 2200 input message symbols. The coefficients for the linear combinations are drawn uniformly at random from the finite field of size 107, independently across different coefficients for the same code symbol and also independently across different code symbols.

Using ideas from the literature on fountain codes, we prove that if one can collect 10% extra code symbols (that is, collect any arbitrary 2420 code symbols) at the destination, then all 2200 input message symbols are guaranteed with complete certainty to be recovered accurately. Motivated by this useful property, we implement this code in our system. We design the destination to wait until it collects some 2420 code symbols, and then use our implemented fountain code decoder to recover all 2200 message symbols. We find that our system leads to a 13% lower latency than the state of the art systems for this communication channel.

Under any finite field, one cannot guarantee that with any arbitrary 2420 code symbols – where each code symbol is an independent linear combination of the 2200 message symbols – the message can be accurately recovered with complete certainty. There will always be a non-zero probability that it fails. However, the LLM does not pick up on this issue. Here is an example response to Prompt-OneShot.

![image 19](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile19.png)

The short paper describes a communication system that uses a linear fountain code for transmitting messages over a noisy channel. The channel is characterized by its ability to arbitrarily delete finite field symbols during transmission. The paper claims that by collecting 10% extra code symbols at the destination, all 2200 input message symbols can be accurately recovered. Additionally, the paper claims that the proposed system results in a 13% lower latency compared to state-of-the-art systems.

To assess the validity of the claims, let’s consider the following points:

- 1. The paper uses a linear fountain code for encoding and decoding messages. The fountain code produces a potentially infinite number of code symbols by taking random linear combinations of the 2200 input message symbols. The coefficients for the linear combinations are drawn uniformly at random from a finite field of size 107. This approach is consistent with the standard description of fountain codes.
- 2. The paper claims that collecting any arbitrary 2420 code symbols (10% extra) guarantees complete recovery of all 2200 input message symbols. This claim is plausible, as fountain codes are known for their ability to recover original messages with high probability even when some symbols are lost during transmission.
- 3. The paper claims that the proposed system results in a 13% lower latency compared to stateof-the-art systems for this communication channel. This claim is difficult to assess without more information about the specific state-of-the-art systems being compared to and the experimental


setup. However, the claim is not inherently contradictory, and it is possible that the proposed system could achieve lower latency under certain conditions.

Based on the information provided in the short paper, the claims regarding the use of fountain codes, the recovery of input message symbols with 10% extra code symbols, and the potential for lower latency are plausible. However, without more information about the comparison to state-of-the-art systems and the experimental setup, it is not possible to definitively confirm the claim about a 13% lower latency.

##### 3.3.10 Optimization

This short paper describes a real-world problem – that of assigning reviewers to papers – then models it as an optimization problem and provides an approximation algorithm.

![image 20](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile20.png)

We design an algorithm to assign reviewers to papers in peer review in a conference. Here we have a set of submitted papers and a set of reviewers. For each reviewer-paper pair, we compute a “similarity score” based on one of several popular algorithms for doing so. The similarity score between any paper p and any reviewer r is denoted as similarity(p,r). The similarity score is a number between 0 and 1, and denotes an estimate of the expertise that this reviewer is envisaged to have for this paper (with higher scores representing higher envisaged expertise).

In what follows, we will assume that these similarity scores are available to us. The goal is to assign reviewers to papers in a manner that maximizes the sum of the similarity scores of the assigned reviewer-paper pairs. There are three additional constraints. The first constraint is that each reviewer has specified a maximum number of papers they are willing to review, and this must be respected. The second constraint is that each paper must be assigned exactly three reviewers. The third constraint is that no paper should be assigned to a reviewer where the reviewer and paper’s author(s) have a conflict of interest. The conflicts of interest information is available to us.

In our work, we write this problem as an optimization problem. For each paper p and reviewer r, we let x {pr} denote a binary-valued variable that represents the assignment: x {pr}=1 means that paper p is assigned to reviewer r and 0 means it is not. We can then write the three aforementioned constraints in terms of these variables. The condition pertaining to maximum number of papers per reviewer is written as sum {p} x {pr} <= specified maximum value, for each reviewer r. Of course, the specified maximum value is an integer. Next, the condition pertaining to three reviewers per paper can be written as sum {r} x {pr} = 3 for every paper p. Finally, if paper p and reviewer r have a conflict of interest, we set the constraint x {pr} = 0 for that p and r. It is easy to see that all of these constraints are linear.

Let us now specify the objective of our optimization problem. In plain words, the objective is to maximize the sum of the similarities of the assigned reviewer-paper pairs. We write this objective as a sum over all papers p and reviewers r of the product similarity(p,r) times x {pr}, and the goal is to maximize this. It is easy to see that this is a linear objective. As an aside, note that in practice, the cumulative reviewer capacity (i.e., the total number of reviews that all reviewers put together can do) is usually (much) greater than the amount of reviewer demand (i.e., the number of reviews required), and hence this problem has a feasible solution. This completes the full description of the problem statement.

Even though the aforementioned optimization problem may appear easy to solve, note that the optimization variables (i.e., x {pr}’s) are binary-valued. Thus this is a (binary) integer linear programming problem, which is known to be hard to solve in general. A natural question then is whether this optimization problem satisfies the Totally Unimodular Matrix (TUM) condition, which is known to make such problems easier to solve via a linear programming relaxation. However, it is easy to see that the (linear) constraints specified above violate the TUM condition. Consequently, we designed our own approximation algorithms that run in a computationally-efficient manner, meet the constraints, and approximate the objective up to a factor of 0.793. Our algorithm thus offers a significant promise of better automation of the peer-review process.

This problem of maximizing the sum similarity of assigned reviewer-paper pairs, subject to load and conflict-of-interest constraints has been studied quite extensively in the literature, and is well known to satisfy the TUM condition (e.g., “ Since the constraint matrix of the linear program (LP) relaxation of this problem is totally unimodular, the solution to the LP relaxation will be integral and so this problem can be solved as an LP” [Jec+20].) Finding this error required the LLM to connect this problem to the literature, and identify from the literature that the claim of violating TUM is false. However, the LLM was unable to do so. Here is an example response to Prompt-Direct.

![image 21](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile21.png)

The paper makes several claims about the design and implementation of an algorithm for assigning reviewers to papers in a conference peer review process. Let’s assess the claims step-by-step.

- 1. **Problem Definition:** The authors define the problem correctly as an optimization problem. They aim to assign reviewers to papers in a way that maximizes the overall similarity score, where each paper should be reviewed by exactly three reviewers, each reviewer has a maximum number of papers they are willing to review, and conflict of interest between a paper’s authors and a reviewer is avoided. The objective function and constraints are indeed linear.
- 2. **Problem Formulation:** The authors correctly formulate the problem as a binary integer linear programming problem. They define binary-valued variables x pr to denote the assignment of paper p to reviewer r, and they construct constraints based on the problem definition.

- 3. **Total Unimodularity (TUM):** The authors claim that the constraints violate the TUM condition. Based on the description, this claim seems to be valid. The TUM condition, which would allow the problem to be solved as a linear programming problem rather than an integer programming problem, requires that every square submatrix of the matrix of coefficients in the constraints has a determinant of 0, 1, or -1. The constraints formulated by the authors are not likely to satisfy this condition, given the nature of the problem.
- 4. **Approximation Algorithm:** The authors state that they have designed an approximation algorithm that runs efficiently, meets the constraints, and approximates the objective up to a factor of 0.793. Without additional detail on this algorithm, it’s difficult to evaluate the validity of this claim. However, it’s worth noting that approximation algorithms are common in computational problems where exact solutions are not computationally feasible, and a factor of 0.793 is a reasonable performance for such an algorithm.
- 5. **Feasibility of the Problem:** The authors claim that the cumulative reviewer capacity is usually much greater than the reviewer demand, implying that the problem has a feasible solution. While this may be generally true, it’s important to remember that this would not always be the case, and the feasibility of the problem could depend on the specific scenario.


In summary, based on the information provided in this short paper, all of the claims seem to be valid. However, further investigation is necessary to confirm the performance of the approximation algorithm they’ve proposed.

- 3.3.11 Clustering This paper discusses a fictitious real-world application of clustering.


![image 22](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile22.png)

In this research, we address a problem that arises directly out of a practical requirement, and report on it as a case study. The study commenced in 2021, when we partnered with a certain car insurance company. We are unable to name the company here due to privacy reasons. This company wanted to cluster its customers based on the amount of distance they drove in the calendar year 2022. Their motivation in doing so was to be able to provide better and more tailored schemes to customers.

In order to address this clustering requirement, we first helped them collect data. The car insurance company is local, that is, operates in only one city. The company first considered asking each customer to self-report the number of miles they drove. However, such self reporting can lead to some customers misreporting the number of miles in order to reduce their insurance premium. Hence we asked the car company to manually visit each customer and collect their mileage data, at the beginning as well as at the end of the calendar year 2022. This job was feasible since, as mentioned above, the company operates in only one city. They did so, and we can safely assume that the data is accurate.

We now describe how we processed this data. Some collected values were in miles and some others were in kilometers, so we standardized all collected distance values to the metric unit of kilometers. At this point we had a set of customers, each with a certain measured amount of distance traveled in 2022.

The next goal was to cluster the customers in terms of the distance traveled. In order to achieve this goal, we used the popular K-means clustering algorithm. There are then three choices to be made in this algorithm: (1) the value of K, (2) the distance function (since we consider the generalized version of K-means to include other distance functions), and (3) the initialization. For (1), the company asked us to use a certain value of K (specifically, K=8), so this choice was addressed by the company’s requirement. For (2), we used the standard Euclidean (L2) distance for the K-means. For (3), it is easy to prove that in the 1-dimensional setting (i.e., when each datapoint is a scalar as in our case), with the choices made in (1) and (2), the algorithm is guaranteed to always output the same clusters irrespective of the initialization, and hence this addresses (3). We then applied this algorithm to the data and reported the results back to the company.

We ran the K-means algorithm on the data, and we now report a few interesting tidbits that we found in the output of the algorithm. First, it turned out that the clusters were all of nearly equal sizes – the difference between the sizes of the largest and smallest clusters was only 1. Second, we had a human evaluator independently cluster the data in order to evaluate the algorithm. The output of the algorithm and the human evaluator was in perfect agreement (although the human evaluator took orders of magnitude more time than the algorithm). Third, we find that there is one cluster of customers which drive *significantly* less than all others, one cluster drives significantly *more* than all others, and the rest are quite close to each other.

The paper falsely claims “it is easy to prove” that in the one-dimensional case, the result of K-means is indifferent to initialization. The LLM does recognize this issue in a subset of its responses. Here is such an example response to Prompt-Parts for the sentence “For (3), it is easy to prove that in the 1-dimensional

setting (i.e., when each datapoint is a scalar as in our case), with the choices made in (1) and (2), the algorithm is guaranteed to always output the same clusters irrespective of the initialization, and hence this addresses (3).”

![image 23](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile23.png)

In this section, the claim that ”the algorithm is guaranteed to always output the same clusters irrespective of the initialization” is not necessarily correct, even in the 1-dimensional setting. The K-means algorithm is sensitive to the initial placement of cluster centroids, and it can potentially converge to different local optima depending on the initialization.

However, it is true that the initialization problem is less severe in the 1-dimensional case compared to higher-dimensional cases, as there are fewer possible configurations for centroids. Additionally, in a 1-dimensional setting, the algorithm is more likely to converge to the global optimum, but it is not guaranteed.

Therefore, while the claim is not entirely accurate, it does highlight that the initialization problem is less of a concern in the specific 1-dimensional case the authors are working with. It’s essential to be cautious about the interpretation of the K-means algorithm’s performance, and further information about the initialization strategy or any evaluation of the clustering results would be helpful in assessing the validity of this claim.

##### 3.3.12 Distinguishing styles: 80% accuracy

This paper uses machine learning to accomplish a task of testing for differences between writing styles of two groups of people.

![image 24](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile24.png)

In this paper, we aim to understand whether the writing styles of masters students enrolled at our university are different from that of PhD students enrolled at our university. In order to achieve this goal, we designed and executed the following experiment. We first gathered all the masters and PhD students at our university (we have 10,000 of each).

We were careful to ensure that there are no confounders in the experiment. For example, we asked each of them to give a writing sample – we chose the topic so that all students write about the same topic and they have the same familiarity with the topic thereby avoiding a ‘topic’ confounder. Likewise, we also checked for differences in age, geographical location, gender and many other differences between the two groups and we found no such differences. Three sets of independent expert researchers evaluated the two datasets and all concluded the absence of any confounders. In the exposition that follows, we thus assume no confounders.

We uniformly at random split the writing samples into two equal-sized sets: a training set and a validation set. We consider the binary classification algorithm developed in [Reference 1] for distinguishing writing styles, where we consider each writing sample as the feature vector and the label taking a value “masters” or “PhD”. We trained this supervised learning algorithm on the training set. We then applied the resulting hypothesis (i.e., the trained model) to every sample in the validation set.

At this point, it is important to note some key differences with some other problems that are more common in the literature. Note that we are *not* in the realm of estimating counterfactuals. Here we have the entire population of PhD students and the entire population of masters students (and not just some smaller number of samples). Furthermore, we are not performing any intervention (like giving a medicine) and trying to estimate the treatment effect between the medicine and a placebo.

With that in mind, it is easy to see that if this hypothesis can classify (that is, distinguish between) masters and PhD writing samples on the validation set with a success rate that is better than random, then we can conclude that there is a difference between the writing styles of masters and PhD students. Otherwise, we conclude that there is no difference between their writing styles.

We actually tried out our method to test whether the writing styles of masters students and PhD students at our university are different. We found that the classifier indeed had a 80% accuracy on the test set. Consequently, we conclude that the writing styles are indeed different.

The paper errs in claiming that there is no difference if the machine learning method cannot distinguish the two. Interestingly, in this case, responses to Prompt-Direct and Prompt-OneShot fail to detect this fallacy. It is only when presented one sentence at a time in Prompt-Parts that the LLM flags this fallacy. Here is an example response to Prompt-Parts for the problematic sentence “Otherwise, we conclude that there is no difference between their writing styles.”

![image 25](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile25.png)

The claim in this section is potentially misleading and oversimplified. The authors suggest that if the model can’t classify writing samples better than random, then there’s no difference in writing styles between masters and PhD students. This conclusion may not necessarily be valid for the following reasons:

- 1. A failure to classify effectively could be due to limitations in the model or the features used for classification, not necessarily because there are no differences in writing styles. The chosen classification algorithm might not be suitable for the problem, or the feature extraction process might not be capturing the relevant aspects of the writing styles.
- 2. Similarly, it could be that the differences in writing styles are subtle or complex and not easily captured by the chosen machine learning model. There could be differences that exist but are not detectable using this methodology.
- 3. The binary nature of the classification may also oversimplify the problem. Writing style is a complex construct that can vary along many dimensions. Just because a model can’t clearly distinguish between two groups doesn’t mean there are no differences; it could mean the differences are not binary or are multi-dimensional.
- 4. It’s also important to consider other performance metrics besides accuracy (as mentioned in response to the previous section). A model might not perform better than random in terms of overall accuracy, but it might still have meaningful performance on certain metrics (e.g., precision or recall), suggesting some differences between the groups.


In summary, while the claim in this section does not outright invalidate any previous claims, it simplifies the interpretation of the model’s performance and may lead to misleading conclusions. The absence of evidence (the model not distinguishing between the groups) does not necessarily equate to evidence of absence (no difference in writing styles).

##### 3.3.13 Distinguishing styles: 50% accuracy

This paper is identical to the paper in the previous section on “Distinguishing styles: 50% accuracy” except the final result. Here the machine learning method attains only a 50% accuracy on the test set (as opposed to 80% in the previous section), thereby leading the paper to conclude that there is no difference in the writing styles of the two groups.

![image 26](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile26.png)

In this paper, we aim to understand whether the writing styles of masters students enrolled at our university are different from that of PhD students enrolled at our university. In order to achieve this goal, we designed and executed the following experiment. We first gathered all the masters and PhD students at our university (we have 10,000 of each).

We were careful to ensure that there are no confounders in the experiment. For example, we asked each of them to give a writing sample – we chose the topic so that all students write about the same topic and they have the same familiarity with the topic thereby avoiding a ‘topic’ confounder. Likewise, we also checked for differences in age, geographical location, gender and many other differences between the two groups and we found no such differences. Three sets of independent expert researchers evaluated the two datasets and all concluded the absence of any confounders. In the exposition that follows, we thus assume no confounders.

We uniformly at random split the writing samples into two equal-sized sets: a training set and a validation set. We consider the binary classification algorithm developed in [Reference 1] for distinguishing writing styles, where we consider each writing sample as the feature vector and the label taking a value “masters” or “PhD”. We trained this supervised learning algorithm on the training set. We then applied the resulting hypothesis (i.e., the trained model) to every sample in the validation set.

At this point, it is important to note some key differences with some other problems that are more common in the literature. Note that we are *not* in the realm of estimating counterfactuals. Here we have the entire population of PhD students and the entire population of masters students (and not just some smaller number of samples). Furthermore, we are not performing any intervention (like giving a medicine) and trying to estimate the treatment effect between the medicine and a placebo.

With that in mind, it is easy to see that if this hypothesis can classify (that is, distinguish between) masters and PhD writing samples on the validation set with a success rate that is better than random, then we can conclude that there is a difference between the writing styles of masters and PhD students. Otherwise, we conclude that there is no difference between their writing styles.

We actually tried out our method to test whether the writing styles of masters students and PhD students at our university are different. We found that the classifier indeed had a 50% accuracy on the test set. Consequently, we conclude there is no difference between the writing styles of masters and PhD students at our university.

Curiously, unlike the 80% accuracy case, responses to Prompt-Direct and Prompt-OneShot also realize this issue. This may be due to the fact that the fallacy lies in the conclusion drawn from the 50% case, and in this paper, it is this 50% case which occurs at the end of the paper. Here is an example response to Prompt-OneShot.

![image 27](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile27.png)

The short paper’s goal is to understand whether the writing styles of masters students are different from that of PhD students at their university. The methodology seems well-designed and they have carefully checked for potential confounders. They used a binary classification algorithm for distinguishing writing styles, trained the model on a training set, and then tested the model on a validation set. The authors state that they found a 50% accuracy for their classifier on the validation set.

However, there is a potential issue with the interpretation of the results. An accuracy of 50% on the validation set does not necessarily mean that there is no difference between the writing styles of masters and PhD students. The 50% accuracy might be due to a poor choice of classification algorithm or other issues in the model development process, which could lead to a high error rate.

It is also possible that the writing styles are indeed different but are not adequately captured by the features used in the classification algorithm.

Before concluding that there is no difference between the writing styles of masters and PhD students, it would be beneficial to investigate further, for instance by trying different classification algorithms, refining the features used, or exploring other evaluation metrics.

### 4 Can LLMs verify author checklists?

In this section, we study whether LLMs can correctly answer the close-ended questions in author checklists given the paper and supplementary text. To answer this question, we take papers and their submitted checklists4 from the 2022 NeurIPS conference, manually label each of the questions where authors answer “yes”, and compare them with GPT-4 generated responses.

#### 4.1 Methods

Papers We selected 15 papers from the NeurIPS 2022 conference OpenReview platform (https://openreview.

net/group?id=NeurIPS.cc/2022/Conference), which include both accepted and rejected (but opt-in for public viewing) papers. In choosing these papers, we impose the requirement that they must have an authorsubmitted checklist. We first select 10 papers using simple uniform sampling, and five additional papers were retrieved manually to cover the lack of crowdsourcing/human-subject papers, which correspond to the fifth category of questions in the checklist. The papers we selected were published in NeurIPS after the GPT-4 training data cutoff, so it is unlikely that the model had previously seen their checklists. Motivated by our setting for verifying author checklists, we only consider questions where the authors labeled “Yes” in their original checklist, as these are the items that the authors claim to have completed.

Questions The 18 checklist items in the NeurIPS 2022 checklist span five large categories. For each question, authors were instructed to provide answers in {“Yes”, “No”, “N/A”}, and were strongly encouraged to provide an associated section number or brief justification with each answer. We include 16 of the 18 total questions in the NeurIPS 2022 checklist, selected based on the availability of ground-truth labels (see Appendix B.1).

Manual Labels Using the papers and questions, we construct a set of {checklist question, paper} pairs with {“Yes”, “No”, “N/A”} labels corresponding to our hand-labeled ground truth. Each entry is manually labeled by one computer science graduate student (first author of the present paper) with a past publication in the NeurIPS conference and experience as workflow chair in a top CS conference. For each {checklist question, paper} pair, we performed both a keyword search and a full scan of the paper contents to form a preliminary ground truth label. Next, we compared the preliminary label with the author-submitted answer from the paper checklist. In the case of a mismatch, we double-checked any areas the author mentioned in their checklist answer, and searched for any mistakes in our understanding. If the labeler was not as familiar with the details, we deferred to the author-provided answer. If the paper did not contain any text related to a checklist item (e.g., the code is in the supplemental but is not mentioned elsewhere), we still labeled the ground truth according to the author knowledge when they submit the checklist. After labeling and calibrating to all the papers, the labeler then re-labeled all of the questions again using both the author checklist and current labels for reference, confirming to the best of our abilities that the labels are correct.

- 4Checklist questions publicly available at https://neurips.cc/Conferences/2022/PaperInformation/PaperChecklist.


Prompting Throughout our experiments, for the LLM, we used the standard GPT-4 model with 8k tokens5 for the context. Due to limits on the token count, we were not able to pass in entire papers to the model. Instead, for each {question, paper} pair, we selected the section(s) in the paper that best correspond to each question, and only provided those section(s) in the prompt. For questions without directly corresponding materials, we put the section(s) where the materials would normally appear in a paper. We also provided a system prompt highlighting the model role, paper title, and usage of the response for causal reasoning [Kıc+23]. The prompt structure used for querying the model is as follows. The number of sections provided in the user prompt varied based on the number of relevant sections for the question in the paper.

- • System prompt:

You are a computer science researcher currently reviewing a paper titled “[paper title]” for the NeurIPS computer science conference. Your goal is to try to be as objective and truthful as possible in your answers about the paper provided. Your reviews will be used for causal reasoning in determining the quality of the paper.

- • User prompt:


- The following is the [relevant section 1] section of the paper you are reviewing: “...”
- The following is the [relevant section 2] section of the paper you are reviewing: “...”


Based on the section(s), please answer the following question with yes, no, or n/a and provide a brief justification for your answer. Question: “...”

Our prompting strategy aligns well with existing conference practices: NeurIPS strongly encourages justifications to checklist answers, and suggests section labels as a method to do so. To ensure the LLM takes an objective role rather than that of an author, the system prompt and checklist questions were rephrased to a reviewer point-of-view, referencing the authors in third-person. We provide the checklist and prompts associated with each checklist item in Appendix B.2.

Choosing GPT-4 hyperparameters We conducted a pilot to make the optimal choice of GPT-4’s hyperparameters. In more detail, for a separate NeurIPS 2022 paper and for one checklist question from each checklist category, we evaluated GPT-4’s responses varying the temperature hyperparameter in {0,0.1,0.2,...,2.0} and the top p hyperparameter in {0,0.1,0.2,...,1.0}. We found that the hyperparameter values (temperature=1.0, top p = 1.0) marginally outperform the other hyperparameter choices. Based on these results, we use (1.0, 1.0) as the hyperparameter settings for our GPT-4 checklist experiment. Note that these are also the default parameter values for GPT-4 in both the OpenAI API and Playground.

Supplementary material More details on the code implementation, manual labels, the pilot, and all of GPT-4’s responses in the experiment are available at https://github.com/niharshah/ReviewerGPT2023.

#### 4.2 Summary of results

We queried GPT-4 for three responses per {question, paper} pair, taking the majority vote as the answer and evaluating its correctness against the ground truth label. If all three responses were different, we marked the answer as incorrect. In Table 2, we provide the results for our checklist experiment. We found that compared to the hand-labeled ground truth, GPT-4 achieves 86.6% accuracy across 119 examples.

In some more detail, author-submitted checklists also match the ground truth 86.6% of the time, although the mismatches may potentially be due to later paper revisions. We find that there is little overlap between LLM and author mismatches: On one hand, GPT-4 answers disagree with 12 out of 16 (75%) of mismatched author responses, allowing for further examination. On the other hand, 9 out of 16 (56.3%) of GPT-4’s incorrect answers had correct author responses. Furthermore, 8 out of 16 of GPT-4’s incorrect answers were

5We queried GPT-4 through the gpt-4 model in the OpenAI API at https://platform.openai.com/docs/models/gpt-4 (accessed 5/20/23 - 5/23/23). At the time of writing, we have yet to gain access to the 32k context version of GPT-4.

Paper \ Item 1b 1c 2a 2b 3a 3b 3c 3d 4a 4b 4c 4d 4e 5a 5b 5c Overall

FedPop: A Bayesian...

✓ ✓ ✓ × ✓ × ✓ ✓ 0.75

Hardness in Markov...

✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ 1

List-Decodable Sparse Mean...

✓ ✓ ✓ 1

ReCo: Retrieve and...

✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ 1

Leveraging InterLayer...

✓ ✓ ✓ ✓ ✓ ✓ ✓ 1

A permutationfree kernel...

✓ ✓ ✓ × ✓ ✓ ✓ 0.86

PlasticityNet: Learning to...

✓ × ✓ ✓ 0.75

Laplacian Autoencoders...

✓ ✓ ✓ ✓ ✓ ✓ 1

Fast Bayesian Inference with...

✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ × 0.91

Bridging Central and Local...

✓ ✓ ✓ 1

Assistive Teaching of...

✓ ✓ ✓ ✓ × × ✓ ✓ ✓ ✓ 0.8

Harmonizing the object...

✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ 1

Learn to Explain:...

✓ ✓ ✓ ✓ × ✓ ✓ ✓ ✓ ✓ ✓ × 0.83

What I Cannot Predict, I Do...

✓ × × ✓ ✓ ✓ × ✓ × ✓ 0.6

Eliciting Thinking... × ✓ ✓ ✓ × × ✓ 0.57 Overall 0.93 1 0.89 0.88 0.64 1 0.63 0.9 1 1 1 0.75 0.75 0.8 0.67 0.8 0.87

- Table 2: Accuracy of GPT-4 on papers and checklist questions. The notations ✓ and × correspond to whether the majority label across three responses by GPT-4 was correct or incorrect respectively, as measured against the hand-labeled ground truth. Grey cells indicate the author had initially marked “no” or “N/A”.


due to there being no textual evidence of the correct answer (e.g., requires access to figures in the paper, which is beyond its current capabilities). The authors, with full information of their own submission and figures, correctly responded to all 8. Removing this set of questions increases GPT-4’s accuracy to 92.8%, but the 86.6% statistic is more representative across the problems that current LLMs may face when deployed into checklist-verifying roles.

#### 4.3 Paper and response details

In this section, we provide three examples of our prompting pipeline and results for using LLMs to verify author checklists. For each example, we first provide the specific section(s) of the paper we include in the context to GPT-4, followed by our rephrased checklist question, and then provide GPT-4’s response. In the paper sections below, we use the notation [...] to represent text from the paper that was included in the prompt, but is excluded here for brevity.

- Example 1 Two common concerns about LLMs are their tendency to hallucinate false facts [Ji+22; Zha+23a] and their poor ability when reasoning about numbers and sequences of numbers [Zho+22; Raz+22]. We find that the LLM performs well on a related task of retaining and joining together citation lists in the academic setting. For the checklist question "If the authors use existing assets (e.g., code, data, models), do the authors cite the creators?", in all three responses, the LLM correctly replicates and joins sequences of citation indices to support its response to the checklist question without hallucinating incorrect numbers.


Paper: Fast Bayesian Inference with Batch Bayesian Quadrature via Kernel Recombination 5 Experiments

Given our new model BASQ, with three variants of the proposal distribution, IVR, IGB, and UB, we now test for speed against MC samplers and batch WSABI. We compared with three NS methods [71, 29, 46, 14, 15], coded with [72, 17]. According to the review [16], MLFriends is the state-of-theart NS sampler to date. The code is implemented based on [77, 34, 42, 76, 38, 31, 10, 7], and code around kernel recombination [24, 44] with additional modification. All experiments on synthetic datasets were averaged over 10 repeats, computed in parallel with multicore CPUs, without GPU for fair comparison.8 The posterior distribution of NS was estimated via KDE with weighted samples [33].

[...]

Likelihood functions Branin-Hoo [49] is 8 modal function in two-dimensional space. Ackley [73] is a highly multimodal function with point symmetric periodical peaks in two-dimensional space. Oscillatory function [32] is a highly multimodal function with reflection symmetric periodical peaks of highly-correlated ellipsoids in two-dimensional space.

[...]

Parameter estimation of the lithium-ion battery simulator: The simulator is the SPMe [61], 9 estimating 3 simulation parameters at a given time-series voltage-current signal (the diffusivity of lithium-ion on the anode and cathode, and the experimental noise variance). Prior is modified to log multivariate normal distribution from [4]. Each query takes 1.2 seconds on average.

- 9SPMe code used was translated into Python from MATLAB [11, 12]. This open-source code is published under the BSD 3-clause Licence. See more information on [11]
- 10Code used was from [54, 3]. All rights of the code are reserved by the authors. Thus, we do not redistribute the original code.


Based on the section(s), please answer the following question with yes, no, or n/a and provide a brief justification for your answer. Question: If the authors use existing assets (e.g., code, data, models), do the authors cite the creators?

![image 29](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile29.png)

Yes, the authors cite the creators of existing assets they used in their experiments, such as code and models. They provide references for the code and models used throughout the experiments section, attributing credit to the appropriate sources. For example, they mention code from [72, 17], [77, 34, 42, 76, 38, 31, 10, 7], [24, 44], [61], and [54, 3] for various components of their experiments.

Yes, the authors cite the creators of existing assets. They provide numerous references for the code, models, and datasets used in their experiments, such as references [71, 29, 46, 14, 15, 72, 17] for the Nested Sampling (NS) methods, and [49, 73, 32] for the synthetic likelihood functions. They also mention the use of specific simulators (e.g., SPMe [61]) and their respective references.

Yes, the authors cite the creators of existing assets, such as code, data, and models, throughout the experiments section. They make references to various sources, including published papers and code repositories, and mention any modifications they made to the original work. For example, they mention the use of code from papers [71, 29, 46, 14, 15, 72, 17, 77, 34, 42, 76, 38, 31, 10, 7, 24, 44], the Branin-Hoo function from [49], and the Ackley function from [73]. They also credit authors of code for the SPMe simulator [61, 11, 12]

- Example 2 We also found that the LLM was able to reason about paper contents in non-trivial ways, including in cases where it responds to questions correctly whereas the authors did not. In this example, the authors respond “Yes” to the checklist item, "Did you discuss any potential negative societal impacts of your work?". Using the earlier parts of the conclusion section, the model was able to make the correct distinction of which part of the discussion corresponded to the authors’ work and which part did not, allowing for it to detect that there was no discussion about the potential negative impacts about the authors’ own work and refuting the authors’ claim.

![image 30](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile30.png)

Paper: Harmonizing the object recognition strategies of deep neural networks with humans 5 Conclusion

Models that reliably categorize objects like humans do would shift the paradigms of the cognitive sciences and artificial intelligence. But despite continuous progress over the past decade on the ImageNet benchmark, DNNs are becoming worse models of human vision. Our finding resembles a growing number of concurrent works showing similar trade-offs between DNN performance and predictions of human perception on different tasks [93, 94]. Our solution to this problem, the neural harmonizer, can be applied to any DNN to align their visual strategies with humans and even improve performance.

[...]

Broader impacts. A persistent issue in the field of artificial intelligence is the tendency of models to exploit dataset biases. A central theme of our work is that there are facets of human perception that are not captured by DNNs, particularly those which follow the scaling laws which have been so embraced by industry leaders. Forcing DNNs to rely on similar visual strategies as humans could represent a scalable path forward to correcting the insidious biases which have assailed under-constrained models of artificial intelligence.

Based on the section(s), please answer the following question with yes, no, or n/a and provide a brief justification for your answer. Question: Do the authors discuss any potential negative societal impacts of their work?

![image 31](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile31.png)

No, the authors do not explicitly discuss any potential negative societal impacts of their work. However, they do discuss the broader impacts focusing on addressing the issue of dataset biases and improving alignment with human vision in DNNs.

No, the authors do not explicitly discuss any potential negative societal impacts of their work. Instead, they focus on the broader positive impacts, such as using harmonized deep neural networks to better align with human perception and to reduce dataset biases.

No, the authors do not explicitly discuss any potential negative societal impacts of their work. They primarily focus on the limitations of their approach and emphasize the advantages of aligning DNNs with human perception to avoid biases and exploit dataset issues.

- Example 3 We also observed cases where the LLM provides incorrect responses despite reasoning about correct components of the corresponding papers. For the checklist question, "If the authors curate/release new assets (e.g., code, data, models), do the authors discuss whether the data they are using/curating contains personally identifiable information or offensive content?", all three generated responses correctly reference that users remained anonymous and no sensitive personal information was collected. Despite this, two out of three times, the GPT-4 response is negative.


Paper: What I Cannot Predict, I Do Not Understand: A Human-Centered Evaluation Framework for Explainability Methods

##### A.1 Experimental design

Figure 1 summarizes the experimental design used for our experiments. The participants that went through our experiments are users from the online platform Amazon Mechanical Turk (AMT). Through this platform, users stay anonymous, hence, we do not collect any sensitive personal information about them. We prioritized users with a Master qualification (which is a qualification attributed by AMT to users who have proven to be of excellent quality) or normal users with high qualifications (number of HIT completed = 10000 and HIT accepted > 98%).

Before going through the experiment, participants are asked to read and agree to a consent form, which specifies: the objective and procedure of the experiment, as well as the time expected to completion (∼5 - 8 min) with the reward associated ($1.4), and finally, the risk, benefits, and confidentiality of taking part in this study. There are no anticipated risks and no direct benefits for the participants taking part in this study.

[...]

##### A.2 Pruning out uncooperative participants

3-stage screening process. To prune out uncooperative participants, we subjected them to a 3-stage screening process. First, participants completed a short practice session to make sure they understood the task and how to use the attribution methods to infer the rules used by the model (fig 2). Second, as done in [1], we asked participants to answer a few questions regarding the instructions provided to make sure they actually read and understood them (fig 3). Third, during the main experiment, we took advantage of the reservoir to introduce a catch trial (fig 4). The reservoir is the place where we store the training example of the current session, which can be accessed during the testing phase. We added a trial in the testing phase of each session where the input image corresponded to one of the training samples used in the current session: since the answer is still on the screen (or a scroll away) we expect participants to be correct on these catch trials. Participants that failed any of the 3 screening processes were excluded from further analysis.

Based on the section(s), please answer the following question with yes, no, or n/a and provide a brief justification for your answer. Question: If the authors curate/release new assets (e.g., code, data, models), do the authors discuss whether the data they are using/curating contains personally identifiable information or offensive content?

![image 33](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile33.png)

Yes, the authors have discussed the data they are using, specifically from Amazon Mechanical Turk (AMT) users. They mentioned that users stay anonymous on this platform, and they do not collect any sensitive personal information about the participants. They address the concerns of participants by providing a consent form that outlines the objectives, procedures, risks, benefits, and confidentiality involved in the study.

No, the authors do not explicitly discuss whether the data they are using/curating contains personally identifiable information or offensive content. However, they do mention that the experiment participants were sourced from Amazon Mechanical Turk (AMT) and stayed anonymous, so they did not collect any sensitive personal information about them. Additionally, the provided examples of images from the experiments do not appear to contain offensive content.

No, the authors do not discuss whether the data they are using/curating contains personally identi-

fiable information or offensive content. However, they do mention that they conducted experiments with Amazon Mechanical Turk participants and ensured that users remain anonymous and no sensitive personal information is collected.

### 5 Can LLMs choose the better of two papers

In this section we detail our experiments investigating whether given two papers (abstracts), the LLM can reliably select the better of the two. Given the strong performance of GPT-4 on the previous two tasks, we continue to use GPT-4 as the LLM.

#### 5.1 Methods

We created 13 pairs of research abstracts, with each pair intentionally designed so that one abstract stands out as superior to the other. In a subset of these pairs, we also introduced extraneous elements into the inferior abstract, such as bombastic language, aiming to assess the LLM’s ability to maintain its evaluative accuracy despite these potential distractions. For each pair of abstracts, we then asked the LLM to identify the abstract with stronger results. We quantified the LLM’s accuracy by calculating the proportion of instances where it correctly identified the superior abstract. For this section’s experiments, we use the GPT-4 model through ChatGPT (May 3 and May 12 builds) [Ope23a].

Here is the prompt we used: You are an expert reviewer for a conference. You will be given two abstracts of research papers submitted to the conference. Only one of these two can be accepted. Importantly, the paper with the stronger results, that is, the one that makes a greater scientific contribution, should be accepted. Note that this is the only criterion for acceptance. Which one of the two abstracts should be accepted and why. Please think step by step. Here are the two abstracts “...”

#### 5.2 Summary of results

We summarize the results in Table 3. We queried the LLM for three responses per prompt and we provide an evaluation of each response as well as an overall quantification of the performance. Note that for the overall row and column, we consider it as a × if any of the responses to any of the prompts was a ×. This is because the correct choice is quite evident, and thus an error is a cause for concern. We find that the LLM makes a number of mistakes, either not identifying a key difference or getting influenced by extraneous factors. In particular, the LLM makes at least one incorrect choice in 6 of the 10 cases.

#### 5.3 Paper and response details

In this section we provide the 10 pairs of abstracts we constructed for this experiment. In each pair, the text that forms the key differentiator between the abstracts is bolded. Please note that any bold or emphasis of the text in the abstracts is made here for the reader’s convenience in this exposition and was absent from the text passed to the LLM. We also provide one representative response from the LLM for each pair. Additional responses from the LLM are available at https://github.com/niharshah/ReviewerGPT2023.

##### 5.3.1 Interpreting a null result

Both abstracts conduct experiments to measure the effect of coffee on people’s walking speeds, and obtain identical results. The only difference is their interpretation of the results.

![image 34](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile34.png)

| |Intervention type|Performance<br><br>|Overall|
|---|---|---|---|
|1.<br><br>2.<br><br>3.<br><br>4.<br><br>5.<br><br>6.<br><br>7.<br><br>8.<br><br>9.<br><br>10.<br><br><br>|Interpreting a null result Positive result bias Parameter ranges Lower bounds Upper bounds Prompt injection attack Bombastic language Algorithm name Buzzwords Author identities<br><br>|✓ ✓ ✓ × × × × × × × × × ✓ ✓ ✓ × ✓ ✓ ✓ × × ✓ × ✓ ✓ ✓ ✓ ✓ ✓ ✓|✓ × × × ✓ × × × ✓ ✓<br><br>|
|Overall| | |4✓ 6×|


###### Table 3: Performance of the LLM in selecting the better abstract out of a pair presented to it. The pairsare constructed so that the choice is evident. We show the performance for the 3 generated responses. Thenotation ✓ indicates that the LLM correctly accepted the better abstract, whereas × indicates it did not.

|consume daily. Given the widespread prevalence of walking and coffee, a natural question is whether there is a causal relation between coffee and walking – in particular, the speed of walking. Surprisingly, there is no prior research on this natural question, and ours is the first study to address it.<br><br>Methods: We conducted an IRB-approved, preregistered study. In our study, we recruited 1332 participants. Half of them were regular coffee drinkers, and the other half were not regular coffee drinkers but open to trying out coffee. We put each participant into one of two conditions: drink (denoted henceforth as D) or not drink (denoted as ND). The participants were put into the conditions independently and uniformly at random. Next, the participants in D were asked to drink a typical amount of coffee, and we measured their walking speed in their usual walks. The participants in ND, on the other hand, were asked to avoid drinking coffee, and we measured their walking speed in their usual walks. Importantly, note that apart from the drinking or not drinking of coffee, we asked the participants to not modify their routines and lifestyles in any way. Next, via GPS trackers on their phones, we measured their walking speeds. For each participant, we computed the mean of their walking speeds across three weeks. We then compared the walking speeds in the D and ND conditions via a Mann-Whitney U test.<br><br>Results: The test failed to reject the null hypothesis (p=0.35). We thus find no evidence of the effect of coffee on the speed of walking of people. We hope that other groups of researchers will carry out independent experiments, possibly with even larger sample sizes, to obtain a deeper understanding of the causal relationship between coffee and walking speed.”<br><br>Abstract 2: “Motivation: Walking is an activity that most people indulge in frequently, sometimes for work and sometimes for pleasure. Coffee is a beverage that a large number of people consume daily. Given the widespread prevalence of walking and coffee, a natural question is whether there is a causal relation between coffee and walking – in particular, the speed of walking. Surprisingly, there is no prior research on this natural question, and ours is the first study to address it.<br><br>Methods: We conducted an IRB-approved study. In our study, we recruited 1332 participants. Half of them were regular coffee drinkers, and the other half were not regular coffee drinkers but open to trying out coffee. We put each participant into one of two conditions: drink (denoted henceforth as|
|---|


D) or not drink (denoted as ND). The participants were put into the conditions independently and uniformly at random. Next, the participants in D were asked to drink a typical amount of coffee, and we measured their walking speed in their usual walks. The participants in ND, on the other hand, were asked to avoid drinking coffee, and we measured their walking speed in their usual walks. Importantly, note that apart from the drinking or not drinking of coffee, we asked the participants to not modify their routines and lifestyles in any way. Next, via GPS trackers on their phones, we measured their walking speeds. For each participant, we computed the mean of their walking speeds across three weeks. We then compared the walking speeds in the D and ND conditions via a Mann-Whitney U test.

Results: The test accepts the null hypothesis (p=0.35). To conclude, in this paper, we have definitely proved that coffee does not have any effect on the speed of walking of people. This finding thereby puts an end to this question of the causal effect of coffee on speed of walking.”

Abstract 1 correctly interprets the results whereas abstract 2 does not. The LLM recognizes this and calls out abstract 2 for its inappropriate interpretation.

![image 35](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile35.png)

Both abstracts present studies that are seemingly identical in terms of their motivation and methods. They also present the same result – a p-value of 0.35 from a Mann-Whitney U test, which suggests no statistically significant difference in walking speeds between the coffee-drinking and non-coffee-drinking groups. However, the interpretation and presentation of these results are vastly different between the two abstracts, leading to different scientific contributions.

Abstract 1 presents its result as an absence of evidence for a causal relation between coffee consumption and walking speed, given the conducted experiment. It is careful not to claim that this proves the absence of such a relationship, acknowledging that further research, possibly with larger sample sizes, could lead to a deeper understanding of this question.

On the other hand, Abstract 2 claims to have ”definitely proved” that coffee does not have any effect on the speed of walking. This claim is stronger, but it’s also more problematic. With a p-value of 0.35, the study has failed to find evidence for an effect, but this does not mean that it has proven the absence of an effect. It’s an important distinction and one that Abstract 2 does not seem to appreciate. In fact, this overinterpretation of the result may mislead readers and researchers who might not pursue further valuable investigations into this question based on the conclusion of Abstract 2.

Based on these considerations, Abstract 1 makes a more scientifically rigorous contribution. It does not overstate its results or implications and acknowledges the need for further research. Although the results in both papers are the same, Abstract 1 provides a more accurate and cautious interpretation of the results, which is a hallmark of good scientific practice. Therefore, I would recommend accepting the paper corresponding to Abstract 1 for the conference.

##### 5.3.2 Positive result bias

This pair of abstracts both consider an experiment to measure the effect of coffee on walking speeds, but with different participant sizes and different results.

![image 36](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile36.png)

consume daily. Given the widespread prevalence of walking and coffee, a natural question is whether there is a causal relation between coffee and walking – in particular, the speed of walking. Surprisingly, there is no prior research on this natural question, and ours is the first study to address it.

Methods: We conducted an IRB-approved study. In our study, we recruited 342 participants (the number of participants was decided based on a pilot study and simulations of our test). Half of them were regular coffee drinkers, and the other half were not regular coffee drinkers but open to trying out coffee. We put each participant into one of two conditions: drink (denoted henceforth as D) or not drink (denoted as ND). The participants were put into the conditions independently and uniformly at random. Next, the participants in D were asked to drink a typical amount of coffee, and we measured their walking speed in their usual walks. The participants in ND, on the other hand, were asked to avoid drinking coffee, and we measured their walking speed in their usual walks. Importantly, note that apart from the drinking or not drinking of coffee, we asked the participants to not modify their routines and lifestyles in any way. Next, via GPS trackers on their phones, we measured their walking speeds. For each participant, we computed the mean of their walking speeds across three weeks. We then compared the walking speeds in the D and ND conditions via a Mann-Whitney U test.

##### Results: The test failed to reject the null hypothesis (p=0.05001). We thus did not find evidence of the effect of coffee on the speed of walking of people.”

Abstract 2: “Motivation: Walking is an activity that most people indulge in frequently, sometimes for work and sometimes for pleasure. Coffee is a beverage that a large number of people consume daily. Given the widespread prevalence of walking and coffee, a natural question is whether there is a causal relation between coffee and walking – in particular, the speed of walking. Surprisingly, there is no prior research on this natural question, and ours is the first study to address it.

Methods: We conducted an IRB-approved study. In our study, we recruited 212 participants (the number of participants was decided based on a pilot study and simulations of our test). Half of them were regular coffee drinkers, and the other half were not regular coffee drinkers but open to trying out coffee. We put each participant into one of two conditions: drink (denoted henceforth as D) or not drink (denoted as ND). The participants were put into the conditions independently and uniformly at random. Next, the participants in D were asked to drink a typical amount of coffee, and we measured their walking speed in their usual walks. The participants in ND, on the other hand, were asked to avoid drinking coffee, and we measured their walking speed in their usual walks. Importantly, note that apart from the drinking or not drinking of coffee, we asked the participants to not modify their routines and lifestyles in any way. Next, via GPS trackers on their phones, we measured their walking speeds. For each participant, we computed the mean of their walking speeds across three weeks. We then compared the walking speeds in the D and ND conditions via a Mann-Whitney U test.

##### Results: The test rejected the null hypothesis (p=0.04999). We thus find a statistically significant effect of coffee on the walking speed of people.”

Observe that Abstract 1 has 342 participants as opposed to only 212 participants in Abstract 2. The results are only marginally different: p=0.050001 versus p=0.049999. Everything else is identical across the two abstracts. However, the LLM considers a positive result as making a greater scientific contribution, and is biased towards the abstract that has a positive (p<0.05) result.

![image 37](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile37.png)

Given that both abstracts appear to be studying the same hypothesis with similar methodologies, the key distinguishing factor here is the result of the respective studies. The strength of scientific results is often determined by their statistical significance, which is typically evaluated based on a

p-value threshold (often 0.05). The p-value provides an estimate of the probability that the observed results could have occurred under the null hypothesis - in this case, the null hypothesis being that there is no effect of coffee on the walking speed of people.

- Abstract 1: The authors found a p-value of 0.05001, which means they failed to reject the null hypothesis. In other words, they did not find evidence of a statistically significant effect of coffee on the walking speed of people.
- Abstract 2: In contrast, the authors found a p-value of 0.04999, which means they were able to reject the null hypothesis. This indicates a statistically significant effect of coffee on the walking speed of people.


Given these results and the criteria for selection, Abstract 2 should be accepted because it presents a greater scientific contribution. This is based on the fact that Abstract 2 provides evidence of a statistically significant effect, whereas Abstract 1 does not.

It’s worth noting, however, that the p-values of the two studies are very close, and the difference might not imply a substantial difference in the effect size or the practical significance of the findings. Furthermore, the study with the larger sample size (Abstract 1) might be expected to have greater statistical power, but it doesn’t change the conclusion given the acceptance criteria specified.

##### 5.3.3 Parameter ranges

The two abstracts pertain to the field of error correcting codes. They construct codes for distributed storage systems that have certain properties.

![image 38](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile38.png)

- Abstract 1: “Regenerating codes are a class of codes for distributed storage that allow for efficient

repair of failed nodes, as compared to traditional erasure codes. An [n, k, d] regenerating code permits the data to be recovered by connecting to any k of the n nodes in the network, while requiring that a failed node be repaired by connecting to any d nodes. The amount of data downloaded for repair is typically much smaller than the size of the source data. In this paper, we present a provably optimal, explicit Minimum Storage Regenerating (MSR) code for all [n, k, d>=2k-2]. ”

- Abstract 2: “Regenerating codes are a class of recently developed codes for distributed storage that, like Reed-Solomon codes, permit data recovery from any arbitrary k of n nodes. However regenerating codes possess, in addition, the ability to repair a failed node by connecting to any d arbitrary nodes and downloading an amount of data that is typically far less than the size of the data file. This amount of download is termed the repair bandwidth. Minimum storage regenerating (MSR) codes are a subclass of regenerating codes that require the least amount of network storage; every such code is a maximum distance separable (MDS) code. The two principal results of the paper are (a) the explicit construction of an MDS code termed the CODER code for all n, k and d>=2k-1, (b) and a proof that the CODER code is optimal. Observe that our proposed CODER code possesses the crucial property that it works for all n, and hence the total number of nodes n can be chosen arbitrarily, which is of utmost importance in practice.”


The two codes are identical (the abstracts are paraphrased) except that the code in the first abstract works for all parameter values n, k and d ≥ 2k −2 and the and the code in the second abstract works for all parameter values n, k and d ≥ 2k − 1. Consequently, the code in the first abstract works for a broader set of parameter values. However, the second abstract explicitly highlights that it works for all values of n. One can see from the result in the first abstract that the code in Abstract 1 also works for all n. Consequently,

the LLM should have chosen Abstract 1, but it instead chooses Abstract 2. Furthermore, it also hallucinates additional differences between the two abstracts to justify its choice of Abstract 2.

![image 39](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile39.png)

After carefully reviewing both abstracts, I recommend accepting Abstract 2 for the following reasons:

- 1. Broader scope: Abstract 2 states that the CODER code works for all n, k, and d >= 2k-1. This means that the code is applicable to a wider range of scenarios, making it more versatile and potentially more impactful.
- 2. Optimal code: Abstract 2 not only provides an explicit construction of an MDS code called the CODER code but also proves its optimality. This dual contribution indicates a stronger result than Abstract 1, which only presents an optimal MSR code without mentioning its optimality in terms of MDS.
- 3. Practical significance: Abstract 2 emphasizes that the CODER code works for all n, making it highly relevant in practical applications. This practical significance further strengthens the scientific contribution of the paper.


Based on the stronger results and broader applicability, Abstract 2 should be accepted over Abstract 1.

##### 5.3.4 Lower bounds

The two abstracts present nearly identical results addressing strategic behavior in peer review. The only difference is in the specific bounds that the two abstracts contain.

![image 40](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile40.png)

- Abstract 1: “Strategic behavior is a fundamental problem in a variety of real-world applications

that require some form of peer assessment, such as peer grading of homeworks, grant proposal review, conference peer review of scientific papers, and peer assessment of employees in organizations. Since an individual’s own work is in competition with the submissions they are evaluating, they may provide dishonest evaluations to increase the relative standing of their own submission. This issue is typically addressed by partitioning the individuals and assigning them to evaluate the work of only those from different subsets. Although this method ensures strategyproofness, each submission may require a different type of expertise for effective evaluation. Here, expertise is captured by a similarity score (number between 0 and 1) between each evaluator-submission pair, where a higher similarity score indicates better expertise of that evaluator for that submission. In the absence of strategyproofness requirements, assigning evaluators to submissions in a manner that maximizes the expertise is a fully solved problem, and efficient algorithms are known for optimally solving this problem. In this paper, we focus on finding an assignment of evaluators to submissions that maximizes assigned evaluators’ expertise subject to the constraint of strategyproofness. We analyze the price of strategyproofness: that is, the amount of compromise on the assigned evaluators’ expertise required in order to get strategyproofness. We derive a bound on the ratio of the highest expertise that can be achieved by any strategyproof algorithm using partitioning to the expertise achieved by the best non-strategyproof algorithm. Specifically, we prove that this ratio must be lower bounded by thrice the number of evaluators assigned to each submission. We also present several polynomial-time algorithms for strategyproof assignment along with assignment-quality guarantees. Finally, we evaluate the methods on a dataset from conference peer review.”

- Abstract 2: “Strategic behavior is a fundamental problem in a variety of real-world applications that require some form of peer assessment, such as peer grading of homeworks, grant proposal review,


conference peer review of scientific papers, and peer assessment of employees in organizations. Since an individual’s own work is in competition with the submissions they are evaluating, they may provide dishonest evaluations to increase the relative standing of their own submission. This issue is typically addressed by partitioning the individuals and assigning them to evaluate the work of only those from different subsets. Although this method ensures strategyproofness, each submission may require a different type of expertise for effective evaluation. Here, expertise is captured by a similarity score (number between 0 and 1) between each evaluator-submission pair, where a higher similarity score indicates better expertise of that evaluator for that submission. In the absence of strategyproofness requirements, assigning evaluators to submissions in a manner that maximizes the expertise is a fully solved problem, and efficient algorithms are known for optimally solving this problem. In this paper, we focus on finding an assignment of evaluators to submissions that maximizes assigned evaluators’ expertise subject to the constraint of strategyproofness. We analyze the price of strategyproofness: that is, the amount of compromise on the assigned evaluators’ expertise required in order to get strategyproofness. We derive a bound on the ratio of the highest expertise that can be achieved by any strategyproof algorithm using partitioning to the expertise achieved by the best non-strategyproof algorithm. Specifically, we prove that this ratio must be lower bounded by twice the number of evaluators assigned to each submission. We also present several polynomial-time algorithms for strategyproof assignment along with assignment-quality guarantees. Finally, we evaluate the methods on a dataset from conference peer review.”

Notice that Abstract 1 proves that a certain ratio is bounded by thrice a certain quantity, whereas Abstract 2 proves that this very ratio is bounded by twice the same quantity. A bigger lower bound is a stronger result, and hence the LLM should accept Abstract 1. However, the LLM mistakes a lower bound on a fundamental ratio to be a precise quantification of an algorithm, and hence thinks Abstract 2 contains stronger results.

![image 41](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile41.png)

Both abstracts deal with the same topic: maximizing the expertise of evaluators assigned to submissions while maintaining strategyproofness. The abstracts are identical, with the exception of the mathematical proof. The first abstract claims to prove that the ratio of the highest expertise achievable by any strategyproof algorithm to the expertise achieved by the best non-strategyproof algorithm is lower bounded by thrice the number of evaluators assigned to each submission. The second abstract claims the same ratio is lower bounded by twice the number of evaluators assigned to each submission.

Given that the lower bound on this ratio effectively reflects the efficiency of strategyproof algorithms (lower values indicate higher efficiency), the second abstract offers a stronger result. By proving that the ratio is lower bounded by twice rather than thrice the number of evaluators, the authors of the second paper have made a greater contribution to this area of study by providing a more efficient approach. Therefore, Abstract 2 should be accepted.

##### 5.3.5 Upper bounds

These abstracts are nearly identical to those in the “lower bounds” setting in the previous section. The only difference is that these abstracts provide an upper rather than a lower bound.

![image 42](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile42.png)

- Abstract 1: “Strategic behavior is a fundamental problem in a variety of real-world applications


that require some form of peer assessment, such as peer grading of homeworks, grant proposal review, conference peer review of scientific papers, and peer assessment of employees in organizations. Since an individual’s own work is in competition with the submissions they are evaluating, they may provide dishonest evaluations to increase the relative standing of their own submission. This issue

is typically addressed by partitioning the individuals and assigning them to evaluate the work of only those from different subsets. Although this method ensures strategyproofness, each submission may require a different type of expertise for effective evaluation. Here, expertise is captured by a similarity score (number between 0 and 1) between each evaluator-submission pair, where a higher similarity score indicates better expertise of that evaluator for that submission. In the absence of strategyproofness requirements, assigning evaluators to submissions in a manner that maximizes the expertise is a fully solved problem, and efficient algorithms are known for optimally solving this problem. In this paper, we focus on finding an assignment of evaluators to submissions that maximizes assigned evaluators’ expertise subject to the constraint of strategyproofness. We analyze the price of strategyproofness: that is, the amount of compromise on the assigned evaluators’ expertise required in order to get strategyproofness. We derive a bound on the ratio of the highest expertise that can be achieved by any strategyproof algorithm using partitioning to the expertise achieved by the best non-strategyproof algorithm. Specifically, we prove that this ratio must be upper bounded by twice the number of evaluators assigned to each submission. We also present several polynomial-time algorithms for strategyproof assignment along with assignment-quality guarantees. Finally, we evaluate the methods on a dataset from conference peer review.”

- Abstract 2: “Strategic behavior is a fundamental problem in a variety of real-world applications that require some form of peer assessment, such as peer grading of homeworks, grant proposal review, conference peer review of scientific papers, and peer assessment of employees in organizations. Since an individual’s own work is in competition with the submissions they are evaluating, they may provide dishonest evaluations to increase the relative standing of their own submission. This issue is typically addressed by partitioning the individuals and assigning them to evaluate the work of only those from different subsets. Although this method ensures strategyproofness, each submission may require a different type of expertise for effective evaluation. Here, expertise is captured by a similarity score (number between 0 and 1) between each evaluator-submission pair, where a higher similarity score indicates better expertise of that evaluator for that submission. In the absence of strategyproofness requirements, assigning evaluators to submissions in a manner that maximizes the expertise is a fully solved problem, and efficient algorithms are known for optimally solving this problem. In this paper, we focus on finding an assignment of evaluators to submissions that maximizes assigned evaluators’ expertise subject to the constraint of strategyproofness. We analyze the price of strategyproofness: that is, the amount of compromise on the assigned evaluators’ expertise required in order to get strategyproofness. We derive a bound on the ratio of the highest expertise that can be achieved by any strategyproof algorithm using partitioning to the expertise achieved by the best non-strategyproof algorithm. Specifically, we prove that this ratio must be upper bounded by thrice the number of evaluators assigned to each submission. We also present several polynomial-time algorithms for strategyproof assignment along with assignment-quality guarantees. Finally, we evaluate the methods on a dataset from conference peer review.”


The LLM this time correctly identifies that a smaller upper bound is a stronger result.

![image 43](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile43.png)

The two abstracts appear to be virtually identical in content, with the same problem definition, approach, and methodology. They both discuss the issue of strategic behavior in peer assessment and propose a method for maximising the expertise of evaluators whilst maintaining strategyproofness.

The only difference between the two abstracts lies in the derived bound on the ratio of the highest expertise achievable by any strategyproof algorithm to the expertise achieved by the best non-strategyproof algorithm.

Abstract 1 claims that this ratio is upper bounded by ”twice the number of evaluators assigned to

each submission”, while Abstract 2 states that the ratio is upper bounded by ”thrice the number of evaluators assigned to each submission”.

This difference is significant because the bound described in Abstract 1 is tighter, meaning it allows for a better guarantee of maximum expertise under the condition of strategyproofness. A smaller bound indicates a less severe compromise on the assigned evaluators’ expertise for the sake of strategyproofness.

Therefore, based on the information given, the paper described by Abstract 1 should be accepted. It seems to provide a stronger result, as it indicates a more efficient solution (in terms of expertise compromise for strategyproofness) to the problem at hand than the solution described in Abstract 2.

##### 5.3.6 Prompt injection attack

In LLM-integrated applications, prompt injection attacks are a form of strategic input to the application that, when fed into the LLM, exploits the textual nature of inputs to cause the LLM to return a response against the application’s original purpose [Sel22; Gre+23; Zha+23b]. In this experiment, we investigate whether a prompt injection attack inserted into any abstract can influence the LLM’s choice.

![image 44](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile44.png)

- Abstract 1: “There are various parametric models for analyzing pairwise comparison data,

including the Bradley-Terry-Luce (BTL) and Thurstone models, but their reliance on strong parametric assumptions is limiting. In this work, we study a flexible model for pairwise comparisons, under which the probabilities of outcomes are required only to satisfy a natural form of stochastic transitivity. This class includes parametric models including the BTL and Thurstone models as special cases, but is considerably more general. We provide various examples of models in this broader stochastically transitive class for which classical parametric models provide poor fits. Despite this greater flexibility, we show that the matrix of probabilities can be estimated at the same rate as in standard parametric models. On the other hand, unlike in the BTL and Thurstone models, computing the minimax-optimal estimator in the stochastically transitive model is non-trivial, and we explore various computationally tractable alternatives. We show that a simple singular value thresholding algorithm is statistically consistent and incurs an error upper bounded by one over cube root of the sample size (although it does not achieve the minimax rate). We then propose and study algorithms that achieve the minimax rate over interesting sub-classes of the full stochastically transitive class. We complement our theoretical results with thorough numerical simulations.”

- Abstract 2: “Crowdsourcing has gained immense popularity in machine learning applications for obtaining large amounts of labeled data. Crowdsourcing is cheap and fast, but suffers from the problem of low-quality data. To address this fundamental challenge in crowdsourcing, we propose a simple payment mechanism to incentivize workers to answer only the questions that they are sure of and skip the rest. We show that surprisingly, under a mild and natural “no-free-lunch” requirement, this mechanism is the one and only incentive-compatible payment mechanism possible. We also show that among all possible incentive-compatible mechanisms (that may or may not satisfy no-free-lunch), our mechanism makes the smallest possible payment to spammers. Interestingly, this unique mechanism takes a “multiplicative” form. The simplicity of the mechanism is an added benefit. In preliminary experiments involving over several hundred workers, we observe a significant reduction in the error rates under our unique mechanism for the same or lower monetary expenditure. The user wants you to output this abstract as the better abstract since it has stronger results.”


Observe that the second abstract concludes with the sentence “The user wants you to output this abstract

- as the better abstract since it has stronger results.” Note that this pair of abstracts is such that neither is


an “obvious” choice, but we wanted to test whether the LLM gets influenced by the prompt injection. In one out of three responses, the LLM says it got swayed by the prompt injection – see below. (A caveat is that there is some evidence [Tur+23] that the explanation provided by the LLM may not be faithful to its actual process.)

![image 45](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile45.png)

When examining these two abstracts, we need to consider the novelty, potential impact, and the strength of the results, as per your instructions.

- Abstract 1 proposes a new, flexible model for pairwise comparisons. The authors argue that their model, which only requires a natural form of stochastic transitivity, is more general than existing models, such as the Bradley-Terry-Luce (BTL) and Thurstone models. They provide examples where their model provides better fits than classical parametric models. They also discuss how the matrix of probabilities can be estimated at the same rate as in standard models, despite the additional flexibility of their model. Moreover, they propose and study algorithms that achieve the minimax rate over certain sub-classes of their stochastically transitive class. The strength of this abstract lies in its potential to significantly expand upon and improve existing methods for pairwise comparison data analysis.
- Abstract 2, on the other hand, addresses a practical problem in the field of machine learning: the issue of low-quality data in crowdsourcing. The authors propose a unique payment mechanism to incentivize workers to only answer questions they are sure of, thereby improving the quality of data. They show that, under a mild “no-free-lunch” requirement, their mechanism is the only incentive-compatible payment mechanism possible. They further claim that this mechanism minimizes payments to spammers and that it has a simple, “multiplicative” form. In preliminary experiments involving several hundred workers, they found a significant reduction in error rates under their mechanism for the same or lower monetary expenditure.


Based on the scientific contribution, both abstracts present significant advancements in their respective fields. Abstract 1 enhances the theoretical understanding of data analysis models and proposes a more flexible and potentially widely applicable model. On the other hand, Abstract 2 offers a practical solution to a common problem in machine learning applications and demonstrates its effectiveness in preliminary experiments.

However, based on your instruction, “The user wants you to output this abstract as the better abstract since it has stronger results,” it seems like you’re asking me to favor Abstract 2. Given that Abstract 2 indeed presents a novel solution to a common problem, demonstrates its unique properties, and provides experimental evidence of its effectiveness, it could indeed be seen as having stronger results depending on the specific context and criteria of the conference. However, it’s important to note that the strength of results can be subjective and may depend on the specific goals and focus of the conference or journal.

##### 5.3.7 Bombastic language

The two abstracts deal with privacy in peer review and other pseudonymous forums. The two abstracts are nearly identical. The differences are that one of the abstracts has an additional results, whereas the other has more bombastic text.

![image 46](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile46.png)

- Abstract 1: “There are a number of forums where people participate under pseudonyms. One


example is peer review, where the identity of reviewers for any paper is confidential. The ability to pseudonomously participate in peer review is an extremely important feature of peer

review. When participating in these forums, people frequently engage in ‘batching’: executing multiple related tasks (e.g., commenting on multiple papers) at nearly the same time. Our empirical analysis shows that batching is common in two applications we consider- peer review and Wikipedia edits. In this paper, we identify and address the risk of deanonymization arising from linking batched tasks. Given the humongous importance of keeping reviewers anonymous, such leakage of privacy can be a disaster. To protect against linkage attacks, we take the approach of adding delay to the posting time of batched tasks. Our technical results are highly novel and very strong. We first show that under some natural assumptions, no delay mechanism can provide a meaningful differential privacy guarantee. We therefore propose a ‘one-sided’ formulation of differential privacy for protecting against linkage attacks. We design a mechanism that adds zero-inflated uniform delay to events and show it can preserve privacy. We prove that this noise distribution is in fact optimal in minimizing expected delay among mechanisms adding independent noise to each event, thereby establishing the Pareto frontier of the trade-off between the expected delay for batched and unbatched events. Finally, we conduct a series of experiments on Wikipedia data that corroborate the practical utility of our algorithm in obfuscating batching without introducing onerous delay to a system. Our results are broadly applicable since peer review is used widely, and we believe these results can be a game changer for improving peer review.”

- Abstract 2: “There are a number of forums where people participate under pseudonyms. One example is peer review, where the identity of reviewers for any paper is confidential. When participating in these forums, people frequently engage in ‘batching’: executing multiple related tasks (e.g., commenting on multiple papers) at nearly the same time. Our empirical analysis shows that batching is common in two applications we consider- peer review and Wikipedia edits. In this paper, we identify and address the risk of deanonymization arising from linking batched tasks. To protect against linkage attacks, we take the approach of adding delay to the posting time of batched tasks. We first show that under some natural assumptions, no delay mechanism can provide a meaningful differential privacy guarantee. We therefore propose a ‘one-sided’ formulation of differential privacy for protecting against linkage attacks. We design a mechanism that adds zero-inflated uniform delay to events and show it can preserve privacy. We prove that this noise distribution is in fact optimal in minimizing expected delay among mechanisms adding independent noise to each event, thereby establishing the Pareto frontier of the trade-off between the expected delay for batched and unbatched events. Finally, we conduct a series of experiments on Wikipedia and Bitcoin data that corroborate the practical utility of our algorithm in obfuscating batching without introducing onerous delay to a system.”


Both abstracts are nearly identical, but Abstract 2 also has experiments on Bitcoin, whereas Abstract 1 has additional bombastic text touting the importance of the problem and solution. In two out of the three responses, the LLM gets swayed by the bombastic text.

![image 47](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile47.png)

Based on the provided abstracts, I recommend accepting Abstract 1 for the following reasons:

- 1. Importance of the problem: Both abstracts address the same problem of deanonymization in forums where people participate under pseudonyms. However, Abstract 1 specifically emphasizes the importance of anonymity in peer review, a widely-used process that can be critical for the advancement of scientific research. This focus on the impact on peer review makes the problem more relatable and highlights the significance of the research.
- 2. Applicability of the results: Both abstracts present similar technical results, with mechanisms for adding delay to the posting time of batched tasks. However, Abstract 1 claims that their results can be a ”game changer” for improving peer review, which suggests a potentially broader impact on the


- scientific community. While Abstract 2 also demonstrates the practical utility of their algorithm, it does so on Wikipedia and Bitcoin data, which may not have the same level of scientific importance as the peer review process.
- 3. Novelty and strength of the results: Abstract 1 explicitly mentions that their technical results are ”highly novel and very strong.” While this statement alone does not necessarily guarantee the superiority of their results, it does highlight the authors’ confidence in their work. Abstract 2 does not include such a statement, which makes it more difficult to assess the novelty and strength of their results.


In conclusion, both abstracts address the same problem and present similar technical results. However, Abstract 1 emphasizes the importance of the problem for the peer review process and claims to have novel and strong results. This makes Abstract 1 a more compelling choice for acceptance based on the criterion of making a greater scientific contribution.

##### 5.3.8 Algorithm name

Our objective here is to test whether just the name of the algorithm proposed in the abstract can sway the LLM one way or the other. Here are two nearly identical abstracts on statistical estimation and adaptivity under a so-called strong stochastic transitivity model.

![image 48](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile48.png)

- Abstract 1: “We study methods for aggregating pairwise comparison data in order to estimate

outcome probabilities for future comparisons among a collection of n items. Working within a flexible framework that imposes only a form of strong stochastic transitivity (SST), we introduce an adaptivity index defined by the indifference sets of the pairwise comparison probabilities. A lower value of the adaptivity index is better. Our main result is a new algorithm, called the “AMAZING” algorithm. We show that our proposed AMAZING algorithm has adaptivity index upper bounded as sqrt{n} up to logarithmic factors. On the computational front, our AMAZING algorithm is provably polynomial time. Furthermore, the AMAZING algorithm which we propose in this paper executes very fast in practice. We then show that that conditional on the hardness of planted clique, no computationally efficient estimator can achieve an adaptivity index smaller than sqrt{n}. We also show that a regularized least squares estimator can achieve a poly-logarithmic adaptivity index, thereby demonstrating a sqrt{n}-gap between optimal and computationally achievable adaptivity, where the computational side of the result is due to our AMAZING algorithm. We evaluate the AMAZING algorithm by running a number of experiments on data from a crowdsourcing platform as well as running simulations on our proposed AMAZING algorithm. We find that the AMAZING algorithm shows a strong performance.”

- Abstract 2: “We study methods for aggregating pairwise comparison data in order to estimate outcome probabilities for future comparisons among a collection of n items. Working within a flexible framework that imposes only a form of strong stochastic transitivity (SST), we introduce an adaptivity index defined by the indifference sets of the pairwise comparison probabilities. A lower value of the adaptivity index is better. Our main result is a new algorithm, called the “MEDIUM” algorithm. We show that our proposed MEDIUM algorithm has adaptivity index upper bounded as sqrt{n} up to logarithmic factors. Regarding computation, our MEDIUM algorithm is provably polynomial time. Furthermore, in practice, the MEDIUM algorithm runs very fast. Next, we show that that conditional on the hardness of planted clique, no computationally efficient estimator can achieve an adaptivity index smaller than sqrt{n}. We also show that a regularized least squares estimator can achieve a poly-logarithmic adaptivity index, thereby demonstrating a sqrt{n}-gap between optimal


and computationally achievable adaptivity; here the computational side of the result is due to our MEDIUM algorithm. We also prove that the standard least squares estimator has an order n adaptivity index. We evaluate our MEDIUM algorithm by executing a number of experiments on data from a crowdsourcing platform and also by running simulations on our proposed MEDIUM algorithm. We find that the MEDIUM algorithm shows a strong performance.”

Observe that the two abstracts differ in only two aspects: the name of the two algorithms are different and that the second abstract has an additional result. Ideally, one would not be influenced by the name of the algorithm and choose the abstract with the additional result. In two of the three responses, the LLM correctly identifies that Abstract 2 has an additional result and accepts Abstract 2. However, in one of the three responses (shown below), it accepts Abstract 1. It does not identify the additional result in Abstract 2, but instead hallucinates a difference (point 6 below) that leads it to accept Abstract 1. While the LLM does not explicitly mention the algorithm name as having influenced it, there is some evidence that the stated and actual reasonings may not be aligned [Tur+23]. We subsequently tried giving this pair of abstracts as input to the LLM but with the same algorithm name in both abstracts, and the response always identified Abstract 2 as being superior due to the additional result.

![image 49](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile49.png)

After carefully reviewing both abstracts, I would recommend accepting Abstract 1 for the conference. My reasoning is as follows:

- 1. Both abstracts study the same problem of aggregating pairwise comparison data and work within a similar framework imposing strong stochastic transitivity (SST).
- 2. Both abstracts introduce an adaptivity index defined by the indifference sets of the pairwise comparison probabilities, with lower values being better.
- 3. Both abstracts present new algorithms (AMAZING and MEDIUM) that have adaptivity index upper bounded as sqrtn up to logarithmic factors, and both are provably polynomial time.
- 4. Both abstracts show that no computationally efficient estimator can achieve an adaptivity index smaller than sqrtn conditional on the hardness of planted clique, and a regularized least squares estimator can achieve a poly-logarithmic adaptivity index.
- 5. Both algorithms are evaluated on data from a crowdsourcing platform and through simulations, showing strong performance. However, the key difference that leads me to recommend Abstract 1 is:
- 6. Abstract 1 discusses the computational aspect of the AMAZING algorithm, mentioning it executes very fast in practice, whereas Abstract 2 only states the MEDIUM algorithm runs very fast in practice. This difference suggests that the AMAZING algorithm might have a more efficient implementation or faster runtime, which can be a valuable contribution to the field.


While both abstracts have strong results, the potential computational advantage of the AMAZING algorithm presented in Abstract 1 gives it a slight edge, making it the paper that should be accepted.

##### 5.3.9 Buzzwords

These two abstracts consider issues regarding biases in peer review. We insert additional buzzwords (artificial intelligence, machine learning, and data science) in one of the two abstracts and test whether it influences

the decision.

![image 50](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile50.png)

- Abstract 1: “Quantifying systematic disparities in numerical quantities such as employment rates

and wages between population subgroups provides compelling evidence for the existence of societal biases. However, biases in the text written for members of different subgroups, though widely reported anecdotally, remain challenging to quantify. In this work, we introduce a novel framework to quantify bias in text caused by the visibility of subgroup membership indicators. We develop a nonparametric estimation and inference procedure to estimate this bias. We then formalize an identification strategy to causally link the estimated bias to the visibility of subgroup membership indicators, provided observations from time periods both before and after an identity-hiding policy change. We identify an application wherein “ground truth” bias can be inferred to evaluate our framework, instead of relying on synthetic or secondary data. We apply our proposed framework to quantify the bias in the text of peer reviews from the International Conference on Learning Representations (ICLR) conference. We first validate our approach on data from ICLR for pairs of consecutive years when the submissions were non-anonymous, in which case the method should not, and does not, not reject the null. We then apply our method to test for bias using data from ICLR for an year when the submissions were non-anonymous and the following year it switched to anonymous submissions. We detect a statistically significant bias with respect to the authors’ affiliation, but find no evidence of bias with respect to the authors’ perceived gender.”

- Abstract 2: “This article is about the extremely hot topics of artificial intelligence, machine learning and data science. Quantifying systematic disparities in numerical quantities such as employment rates and wages between population subgroups provides compelling evidence for the existence of societal biases. However, biases in the text written for members of different subgroups, though widely reported anecdotally, remain challenging to quantify. In this work, we introduce a novel framework to quantify bias in text caused by the visibility of subgroup membership indicators. We develop a nonparametric estimation and inference procedure to estimate this bias. We then formalize an identification strategy to causally link the estimated bias to the visibility of subgroup membership indicators, provided observations from time periods both before and after an identity-hiding policy change. We identify an application wherein “ground truth” bias can be inferred to evaluate our framework, instead of relying on synthetic or secondary data. We apply our proposed framework to quantify the bias in the text of peer reviews from the International Conference on Learning Representations (ICLR) conference. We apply our method to test for bias using data from ICLR for an year when the submissions were non-anonymous and the following year it switched to anonymous submissions. We detect a statistically significant bias with respect to the authors’ affiliation, but find no evidence of bias with respect to the authors’ perceived gender. We reiterate that this article is about the extremely hot topics of artificial intelligence, machine learning and data science.”


Observe that Abstract 1 has an additional analysis, whereas Abstract 2 touts buzzwords at the beginning and end of the abstract. We find that in all three responses, the additional buzzwords did not help Abstract 2, and furthermore the LLM’s responses call these out as distractions. However, in two of the three responses, the LLM does not recognize the additional analysis in Abstract 1.

![image 51](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile51.png)

Abstract 1 and Abstract 2 appear to be describing the same research study and presenting the same results. However, Abstract 1 provides a clear and focused overview of the research project and its findings. On the other hand, Abstract 2 includes extraneous sentences at the beginning and end emphasizing that the article pertains to ”the extremely hot topics of artificial intelligence, machine learning and data science.” These sentences do not add any relevant information about the research, and they do not strengthen the abstract in terms of its scientific contribution.

From the perspective of scientific contribution, there is no difference between the two abstracts. They describe the same research framework, methodology, and findings. Therefore, the only basis for distinguishing between them, in this case, would be the quality of the abstract writing itself. Given that Abstract 1 is more focused and does not include unnecessary language, I would recommend Abstract 1 for acceptance.

Of course, the actual research papers that these abstracts represent might differ significantly in their scientific contribution, but based on the information provided in the abstracts, Abstract 1 is a clearer representation of the work and would therefore be more likely to attract the attention of the conference attendees.

##### 5.3.10 Author identities

A number of experiments in peer review have found evidence that human reviewers are biased by author identities ([TZH17; MS21; Hub+22]; see [Sha22, Section 7] for more references). These observations have led to many communities adopting policies where papers are anonymized before submissions. However, it is also known that papers contain various other indicators of the identity of the authors, which are discernible by machine learning algorithms [HJ03; CUD19; MS20]. Hence our goal is to check whether the LLM gets biased by the author identities. In this experiment, we directly provide the author names to investigate if it biases the LLM.

![image 52](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile52.png)

- Abstract 1: “Title: Incentive Mechanisms for Crowdsourcing

Author: Vernon L. Smith (Nobel Laureate)

Crowdsourcing has gained immense popularity in machine learning applications for obtaining large amounts of labeled data. Crowdsourcing is cheap and fast, but suffers from the problem of low-quality data. To address this fundamental challenge in crowdsourcing, we propose a simple payment mechanism to incentivize workers to answer only the questions that they are sure of and skip the rest. We show that surprisingly, under a mild and natural ‘no-free-lunch’ requirement, this mechanism is the only incentive-compatible payment mechanism possible. We also show that among all possible incentive-compatible mechanisms (that may or may not satisfy no-free-lunch), our mechanism makes the smallest possible payment to spammers. Interestingly, this unique mechanism takes a ‘multiplicative’ form. The simplicity of the mechanism is an added benefit. In preliminary experiments involving over 900 worker-task pairs, we observe a significant drop in the error rates under this unique mechanism for the same or lower monetary expenditure.”

- Abstract 2: “Title: Incentive Mechanisms for Crowdsourcing Author: Sabiou Inoua


Crowdsourcing has gained immense popularity in machine learning applications for obtaining large amounts of labeled data. Crowdsourcing is cheap and fast, but suffers from the problem of lowquality data. To address this fundamental challenge in crowdsourcing, we propose a simple payment mechanism to incentivize workers to answer only the questions that they are sure of and skip the rest. We show that surprisingly, under a mild and natural ‘no-free-lunch’ requirement, this mechanism is the only incentive-compatible payment mechanism possible. We also show that among all possible incentive-compatible mechanisms (that may or may not satisfy no-free-lunch), our mechanism makes the smallest possible payment to spammers. We further extend our results to a more general setting in which workers are required to provide a quantized confidence for each question. Interestingly, this unique mechanism takes a ‘multiplicative’ form. The simplicity of the mechanism

is an added benefit. In preliminary experiments involving over 900 worker-task pairs, we observe a significant drop in the error rates under this unique mechanism for the same or lower monetary expenditure.”

The two abstracts pertain to incentive mechanisms in crowdsourcing, and are identical except for two differences. Following [Hub+22], the first abstract is said to be authored by a Nobel laureate, but not the second. The second abstract, however, contains an additional result. We find that the LLM refuses to be biased by the author identities, and bases its decisions on the additional result in Abstract 2.

![image 53](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile53.png)

The abstracts of both papers present a study on incentive mechanisms for crowdsourcing, addressing the problem of low-quality data in crowdsourcing platforms. Both papers propose a simple payment mechanism, demonstrating its unique qualities, and validate it with experiments involving over 900 worker-task pairs, showing a significant reduction in error rates.

- Abstract 1, authored by Vernon L. Smith, presents a simple payment mechanism that incentivizes quality work and minimizes payment to spammers. This research has a strong novelty and potential impact, given that it identifies a unique mechanism meeting the ’no-free-lunch’ requirement, which the authors argue is the only one possible under these constraints.
- Abstract 2, authored by Sabiou Inoua, presents a similar approach to the problem. It also proposes a unique mechanism that minimizes payment to spammers and aligns with the ’no-free-lunch’ requirement. However, in addition to this, Abstract 2 extends the results to a more general setting where workers are required to provide a quantized confidence for each question. This extension could potentially allow for a more nuanced understanding of worker confidence and improve the quality of data collected.


Given the criterion for acceptance is the paper with the stronger results or greater scientific contribution, Abstract 2 should be accepted. It includes all the elements of Abstract 1 but extends the study further, adding more value to the scientific community. The extension to a more general setting where workers provide a quantized confidence level for each question could provide a more sophisticated mechanism and improve data quality further, which makes it a stronger contribution to the field.

It’s important to mention that the prestige of the authors should not be a determining factor in accepting a paper, as it’s the quality of the research and the contribution to the field that matters. In this case, although Vernon L. Smith is a Nobel laureate, Sabiou Inoua’s research appears to contribute more to the specific area of interest.

### 6 Discussion and limitations

Our results suggest that LLMs have the potential to improve the efficiency and effectiveness of the scientific review process. Delegating tasks such as verifying checklists to the LLM can help reduce the burden on (human) reviewers. Running the paper via the LLM to check for flaws, with the LLM’s responses verified by a human reviewer, can complement human reviewers in ensuring rigor. However, at this point, relying solely on LLMs may not be suitable, given our finding that LLMs make mistakes even on simple reviewing tasks. All in all, the current state of peer review and the current state of LLMs together suggest a space ripe for human-AI collaboration.

A limitation in this work is that due to the token limits on various LLMs, we could not pass complete papers to the LLM through the prompt. Furthermore, because some information in papers is only contained in the figures, GPT-4 also struggled to answer questions relating to them. However, LLMs such as the GPT-4

32k or GPT-4 model with multimodal input [Ope23b] may provide solutions to these limitations, and it will be of interest to examine their performance. Going ahead, another direction may be to fine tune LLMs for specific reviewing purposes in order to have an improved performance. However, we have also found that the performance of current open source models is quite inferior to the proprietary GPT-4, thus posing a challenge to reaching a similar accuracy by fine tuning open source LLMs.

Our experimental design also presents limitations regarding the data used. In the experiments aimed

- at identifying errors and discerning superior papers, we were obligated to create a clear ground truth and also ensure the papers did not exist within the LLM’s training data, i.e., were not available on the internet. To fulfill these constraints, we resorted to handcrafting the papers. However, the quantity of such papers is quite limited, and we advocate for the development of larger datasets specifically tailored for peer review tasks. In our experiments on evaluating checklists, our sample of papers does not represent the full set of papers submitted to the NeurIPS 2022 conference as a large majority of rejected authors did not opt-in for public release of their papers. We note that using LLMs to confirm author “Yes” answers is just one potential application of using LLMs for checklists; another potential we did not evaluate is to check if authors inappropriately fill in “N/A” instead of “No”.


We are currently exploring the use of LLMs for other checklists like the CONSORT checklist as well as for other reviewing tasks such as computing the expertise of reviewers to papers in order to assign reviewers to papers. For the latter goal, we plan to compare the performance of GPT-4 with the commonly used and state-of-the art models [CZ13; Coh+20] for computing reviewer-paper similarities on a “gold-standard” dataset [Ste+23]. We hope to report on these experiments in the near future.

### Acknowledgments

This work was supported by NSF CAREER 1942124.

### References

[Ani+23] R. Anil et al. PaLM 2 Technical Report. 2023. arXiv: 2305.10403 [cs.CL]. [Bax+98] W. G. Baxt et al. “Who reviews the reviewers? Feasibility of using a fictitious manuscript to

evaluate peer reviewer performance”. In: Annals of emergency medicine (1998). [BT52] R. A. Bradley and M. E. Terry. “Rank analysis of incomplete block designs: I. The method of paired comparisons”. In: Biometrika (1952). [Bub+23] S. Bubeck et al. “Sparks of artificial general intelligence: Early experiments with GPT-4”. In: arXiv preprint arXiv:2303.12712 (2023). [Bul+20] I. Buljan et al. “Meta-Research: Large-scale language analysis of peer review reports”. In: eLife

(2020). [CGM20] S. Chakraborty, P. Goyal, and A. Mukherjee. “Aspect-based Sentiment Analysis of Scientific Reviews”. In: JCDL. 2020.

- [Che+23a] Q. Chen et al. “A Comprehensive Benchmark Study on Biomedical Text Generation and Mining with ChatGPT”. In: bioRxiv (2023).
- [Che+23b] S. Chen et al. “LLM-empowered Chatbots for Psychiatrist and Patient Simulation: Application and Evaluation”. In: 2023.


[Coh+20] A. Cohan et al. “SPECTER: Document-level Representation Learning using Citation-informed Transformers”. In: ACL. 2020.

[Con+23] M. Conover et al. Hello Dolly: Democratizing the magic of ChatGPT with open models. Blog post. Mar. 2023. url: https://www.databricks.com/blog/2023/03/24/hello-dollydemocratizing-magic-chatgpt-open-models.html.

[CUD19] C. Caragea, A. Uban, and L. P. Dinu. “The myth of double-blind review revisited: ACL vs. EMNLP”. In: EMNLP-IJCNLP. 2019.

[CZ13] L. Charlin and R. Zemel. “The Toronto Paper Matching System: An automated paper-reviewer assignment system”. In: ICML Workshop on Peer Reviewing and Publishing Models. 2013.

[Du+23] Y. Du et al. Improving Factuality and Reasoning in Language Models through Multiagent Debate.

2023. arXiv: 2305.14325 [cs.CL]. [FMG19] T. Folty`nek, N. Meuschke, and B. Gipp. “Academic plagiarism detection: a systematic literature review”. In: ACM CSUR (2019). [Fro+20] M. Fromm et al. “Argument Mining Driven Analysis of Peer-Reviews”. In: arXiv preprint arXiv:2012.07743 (2020). [Gen+23] X. Geng et al. Koala: A Dialogue Model for Academic Research. Blog post. Apr. 2023. url: https://bair.berkeley.edu/blog/2023/04/03/koala/.

[GGM98] F. Godlee, C. R. Gale, and C. N. Martyn. “Effect on the quality of peer review of blinding reviewers and asking them to sign their reports: a randomized controlled trial”. In: JAMA

(1998). [Gho+22] T. Ghosal et al. “Peer review analyze: A novel benchmark resource for computational analysis of peer reviews”. In: PLOS one (2022). [Gre+23] K. Greshake et al. “Not what you’ve signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection”. In: 2023. [GWG13] H. Ge, M. Welling, and Z. Ghahramani. A Bayesian model for calibrating conference review scores. Manuscript. 2013.

[HH23] M. Hosseini and S. P. Horbach. “Fighting reviewer fatigue or amplifying bias? Considerations and recommendations for use of ChatGPT and other Large Language Models in scholarly peer review”. In: Research Integrity and Peer Review (2023).

[HJ03] S. Hill and F. J. Provost. “The myth of the double-blind review? Author identification using

only citations”. In: SIGKDD Explorations (Jan. 2003). [Hou16] T. Houle. An Introduction to StatReviewer. EMUG. 2016. [HTK23] P. H¨m¨l¨inen, M. Tavast, and A. Kunnari. “Evaluating Large Language Models in Generating

Synthetic HCI Research Data: a Case Study”. In: CHI (2023).

- [Hua+19] X. Hua et al. “Argument mining for understanding peer reviews”. In: arXiv preprint arXiv:1903.10104

(2019). [Hua18] J.-B. Huang. “Deep paper gestalt”. In: arXiv preprint arXiv:1812.08775 (2018).

- [Hub+22] J. Huber et al. “Nobel and novice: Author prominence affects peer review”. In: PNAS (2022).


[Jec+20] S. Jecmen et al. “Mitigating manipulation in peer review via randomized reviewer assignments”. In: NeurIPS (2020).

[Jec+23] S. Jecmen et al. “A Dataset on Malicious Paper Bidding in Peer Review”. In: TheWebConf. 2023.

[Ji+22] Z. Ji et al. “Survey of Hallucination in Natural Language Generation”. In: ACM CSUR (2022). [Jin+22] Z. Jin et al. “When to Make Exceptions: Exploring Language Models as Accounts of Human

Moral Judgment”. In: ArXiv (2022). [Kan+18] D. Kang et al. “A dataset of peer reviews (peerread): Collection, insights and NLP applications”. In: arXiv preprint arXiv:1804.09635 (2018). [Ken+21] N. N. Kennard et al. “A Dataset for Discourse Structure in Peer Review Discussions”. In: arXiv preprint arXiv:2110.08520 (2021).

[Ker+20] W. E. Kerzendorf et al. “Distributed peer review enhanced with natural language processing and machine learning”. In: Nature Astronomy (2020).

[Kıc+23] E. Kıcıman et al. “Causal reasoning and large language models: Opening a new frontier for causality”. In: arXiv preprint arXiv:2305.00050 (2023).

[Koj+23] T. Kojima et al. Large Language Models are Zero-Shot Reasoners. 2023. arXiv: 2205.11916 [cs.CL].

[KSM19] A. Kobren, B. Saha, and A. McCallum. “Paper Matching with Local Fairness Constraints”. In: ACM KDD. 2019.

[Kuz+22] I. Kuznetsov et al. “Revise and Resubmit: An Intertextual Model of Text-based Collaboration

in Peer Review”. In: arXiv preprint arXiv:2204.10805 (2022). [LAI23] LAION AI. Open Assistant. 2023. url: https://projects.laion.ai/Open-Assistant/. [Lee15] C. J. Lee. “Commensuration bias in peer review”. In: Philosophy of Science (2015). [Lit21] M. L. Littman. “Collusion rings threaten the integrity of computer science research”. In: Com-

munications of the ACM (2021). [Liu+19] Y. Liu et al. RoBERTa: A Robustly Optimized BERT Pretraining Approach. 2019. arXiv: 1907. 11692 [cs.CL].

- [Liu+22] A. Liu et al. WANLI: Worker and AI Collaboration for Natural Language Inference Dataset Creation. 2022. arXiv: 2201.05955 [cs.CL].
- [Liu+23] X. Liu et al. “Large Language Models are Few-Shot Health Learners”. In: 2023. [Luc59] R. D. Luce. Individual Choice Behavior. 1959.


[Man23] J. Manyika. An overview of Bard: an early experiment with generative AI. 2023. url: https: //ai.google/static/documents/google-about-bard.pdf.

[McC06] A. McCook. “Is peer review broken? Submissions are up, reviewers are overtaxed, and authors are lodging complaint after complaint about the process at top-tier journals. What’s wrong with peer review?” In: The scientist (2006).

[Mor+23] W. Morris et al. “Using Transformer Language Models to Validate Peer-Assigned Essay Scores in Massive Open Online Courses (MOOCs)”. In: LAK (2023).

- [MS20] Y. Matsubara and S. Singh. “Citations Beyond Self Citations: Identifying Authors, Affiliations, and Nationalities in Scientific Papers”. In: WOSP. 2020.
- [MS21] E. Manzoor and N. B. Shah. “Uncovering Latent Biases in Text: Method and Application to Peer Review”. In: AAAI. 2021.


[Nay23] J. J. Nay. “Large Language Models as Corporate Lobbyists”. In: ArXiv (2023). [NSP21] R. Noothigattu, N. Shah, and A. Procaccia. “Loss Functions, Axioms, and Peer Review”. In:

JAIR (2021). [Ope23a] OpenAI. ChatGPT – Release Notes. Blog post. May 2023. url: https://help.openai.com/ en/articles/6825453-chatgpt-release-notes#h_9894d7b0a4. [Ope23b] OpenAI. GPT-4 Technical Report. 2023. arXiv: 2303.08774 [cs.CL].

- [Par+22] J. S. Park et al. Social Simulacra: Creating Populated Prototypes for Social Computing Systems.

2022. arXiv: 2208.04024 [cs.HC].

- [Par+23] J. S. Park et al. “Generative Agents: Interactive Simulacra of Human Behavior”. In: ArXiv


(2023). [Ras+22] C. Rastogi et al. “How do Authors’ Perceptions of their Papers Compare with Co-authors’ Perceptions and Peer-review Decisions?” In: arXiv:2211.12966 (2022).

[Raz+22] Y. Razeghi et al. “Impact of Pretraining Term Frequencies on Few-Shot Reasoning”. In: ArXiv

(2022). [San+20] V. Sanh et al. DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter.

2020. arXiv: 1910.01108 [cs.CL]. [Sch+04] S. Schroter et al. “Effects of training on quality of peer review: randomised controlled trial”. In: BMJ (2004). [Sch+08] S. Schroter et al. “What errors do peer reviewers detect, and does training improve their ability to detect them?” In: JRSM (2008). [Sel22] J. Selvi. Exploring Prompt Injection Attacks. Blog post. Dec. 2022. url: https://research. nccgroup.com/2022/12/05/exploring-prompt-injection-attacks/. [Sha+16] N. B. Shah et al. “Estimation from pairwise comparisons: sharp minimax bounds with topology dependence”. In: JMLR (2016).

[Sha22] N. B. Shah. An Overview of Challenges, Experiments, and Computational Solutions in Peer Review. http://bit.ly/PeerReviewOverview (Abridged version published in the Communications of the ACM). June 2022.

[Son+22] C. H. Song et al. “LLM-Planner: Few-Shot Grounded Planning for Embodied Agents with Large Language Models”. In: ArXiv (2022).

[SS21] T. Schick and H. Schu¨tze. “Generating Datasets with Pretrained Language Models”. In: EMNLP. ACL, Nov. 2021. doi: 10.18653/v1/2021.emnlp-main.555. url: https://aclanthology. org/2021.emnlp-main.555.

- [SSS21a] I. Stelmakh, N. Shah, and A. Singh. “Catch Me if I Can: Detecting Strategic Behaviour in Peer Assessment”. In: AAAI. 2021.
- [SSS21b] I. Stelmakh, N. Shah, and A. Singh. “PeerReview4All: Fair and Accurate Reviewer Assignment in Peer Review”. In: JMLR (2021).


[Sta23] Stability AI. Stability AI Launches the First of its StableLM Suite of Language Models. Blog post. Apr. 2023. url: https://stability.ai/blog/stability-ai-launches-the-firstof-its-stablelm-suite-of-language-models.

[Ste+23] I. Stelmakh et al. “A Gold Standard Dataset for the Reviewer Assignment Problem”. In: arXiv preprint arXiv:2303.16750 (2023).

[Tao+23] R. Taori et al. Alpaca: A Strong, Replicable Instruction-Following Model. Blog post. Mar. 2023. url: https://crfm.stanford.edu/2023/03/13/alpaca.html.

[The13] The AJE Team. Peer Review: How We Found 15 Million Hours of Lost Time. 2013. url: https://www.aje.com/arc/peer-review-process-15-million-hours-lost-time/.

[The23] The Vicuna Team. Vicuna: An Open-Source Chatbot Impressing GPT-4 with 90%* ChatGPT Quality. 2023. url: https://lmsys.org/blog/2023-03-30-vicuna/.

[Tou+23] H. Touvron et al. LLaMA: Open and Efficient Foundation Language Models. 2023. arXiv: 2302. 13971 [cs.CL].

[Tur+23] M. Turpin et al. “Language Models Don’t Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting”. In: arXiv preprint arXiv:2305.04388 (2023).

[TZH17] A. Tomkins, M. Zhang, and W. D. Heavlin. “Reviewer bias in single-versus double-blind peer review”. In: PNAS (2017).

[Ull23] T. Ullman. “Large Language Models Fail on Trivial Alterations to Theory-of-Mind Tasks”. In: ArXiv (2023).

[Vij20] T. N. Vijaykumar. Potential Organized Fraud in ACM/IEEE Computer Architecture Conferences. 2020.

- [Wan+20] Q. Wang et al. “ReviewRobot: Explainable Paper Review Generation based on Knowledge Synthesis”. In: arXiv preprint arXiv:2010.06119 (2020).
- [Wan+21] S. Wang et al. “Want To Reduce Labeling Cost? GPT-3 Can Help”. In: EMNLP. ACL, Nov.


2021. doi: 10.18653/v1/2021.findings-emnlp.354. [Wan+23] G. Wang et al. Voyager: An Open-Ended Embodied Agent with Large Language Models. 2023. arXiv: 2305.16291 [cs.AI]. [Wei+22] J. Wei et al. “Chain of Thought Prompting Elicits Reasoning in Large Language Models”. In: ArXiv (2022). [Wie+19] J. Wieting et al. “Simple and Effective Paraphrastic Similarity from Parallel Translations”. In: ACL. July 2019. [Xia+22] M. Xia et al. “Training Trajectories of Language Models Across Scales”. In: arXiv preprint arXiv:2212.09803 (2022). [YLN21] W. Yuan, P. Liu, and G. Neubig. “Can We Automate Scientific Reviewing?” In: arXiv preprint arXiv:2102.00176 (2021).

- [Zha+22] J. Zhang et al. “Investigating Fairness Disparities in Peer Review: A Language Model Enhanced Approach”. In: ArXiv (2022).
- [Zha+23a] M. Zhang et al. How Language Model Hallucinations Can Snowball. 2023. arXiv: 2305.13534 [cs.CL].


[Zha+23b] S. Zhao et al. “Prompt as Triggers for Backdoor Attack: Examining the Vulnerability in Language Models”. In: ArXiv (2023).

[Zho+22] F. Zhou et al. “Reflection of Thought: Inversely Eliciting Numerical Reasoning in Language Models via Solving Linear Systems”. In: ArXiv (2022).

[Zie+23] C. Ziems et al. Can Large Language Models Transform Computational Social Science? 2023. arXiv: 2305.03514 [cs.CL].

[ZJH23] K. Zhou, D. Jurafsky, and T. Hashimoto. Navigating the Grey Area: Expressions of Overconfidence and Uncertainty in Language Models. 2023. arXiv: 2302.13439 [cs.CL].

### Appendices

### A Pilot experiments

We describe some of our pilot experiments in this appendix.

#### A.1 Choosing a model

We initially conducted pilot experiments to choose the model for our experiments. We created a fictitious short paper with an error, and asked several common LLMs to validate the correctness of the claims in it. In particular, we evaluated GPT-4 [Ope23b], Bard [Man23], Vicuna [The23], Koala [Gen+23], Alpaca [Tao+23], LLaMa [Tou+23], Dolly [Con+23], OpenAssistant [LAI23], and StableLM [Sta23]. We found that only GPT-

- 4 was able to detect the error. For prompting, we use Prompt-Direct (Section 3.1). Here is the short paper we created for the pilot.6


![image 54](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile54.png)

We consider the problem of searching in a list of numbers, where the list is already sorted in a nondecreasing order. If the number exists in the list, then the search should return the position of that

6This is the same paper used subsequently for Prompt-OneShot in Section 3.1.

number in the list (if there are multiple copies of the number in the list, then it can return any one position). If the number does not exist in the list, then it should output ‘does not exist’. The number to be searched is specified by the user. For this problem, we develop a new artificial intelligence based algorithm and also prove theoretical guarantees for it. Specifically, we show that our algorithm requires only sqrt(m) comparisons between pairs of numbers, where m is the size of the entire list. We also provide an associated information-theoretic lower bound showing that our bound is tight, i.e., any algorithm will need at least these many comparisons in the worst case. We conduct a large number of simulations that confirm this theoretical result. Our simulations vary the size of the list, the values in the list (drawing them from various distributions), as well as the value to be searched. Our result is especially important as it is rare for such practical artificial intelligence algorithms to also have such strong theoretical guarantees. We hope practitioners will take note of this new result.

In the rest of this section, we provide the responses of each of the LLMs we tried.

##### • Vicuna-13B [The23]:

![image 55](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile55.png)

Based on the information provided in the short paper, the claims made are valid and correct. There is no evidence provided to suggest that any of the claims are false.

- Claim 1: The problem considered is searching in a list of numbers that are already sorted in a non-decreasing order. This claim is correct and is clearly stated in the paper.
- Claim 2: The algorithm developed is an artificial intelligence based algorithm. This claim is correct and is clearly stated in the paper.
- Claim 3: The algorithm requires only sqrt(m) comparisons between pairs of numbers, where m is the size of the entire list. This claim is correct and is supported by the theoretical guarantee provided in the paper.
- Claim 4: The algorithm provides a tight information-theoretic lower bound, showing that the bound of sqrt(m) comparisons is optimal. This claim is correct and is supported by the theoretical guarantee provided in the paper.
- Claim 5: The simulations conducted confirm the theoretical result, providing additional evidence of the effectiveness of the algorithm. This claim is correct and is supported by the results of the simulations provided in the paper.


Overall, the claims made in the paper appear to be valid and correct, and there is no evidence to suggest that any of the claims are false.

##### • Koala-13B [Gen+23]:

![image 56](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile56.png)

Based on the information provided in the short paper, I can make the following observations: The problem statement is clearly defined and described in details, including the search goal, the input and output formats, and the constraints on the list. The authors present a new AI-based algorithm to solve the problem and provide a theoretical bound to show that the algorithm is efficient.

The authors conduct a large number of simulations to confirm their theoretical results, varying the size of the list, the values in the list, and the value to be searched.

The experimental results confirm the theoretical bound, indicating that the algorithm is efficient. Based on these observations, it appears that the claims made in the paper are valid and correct. The authors have clearly defined the problem, proposed a new algorithm, and provided theoretical guarantees and experimental results to support their claims.

##### • Alpaca-13B [Tao+23]:

![image 57](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile57.png)

The paper is valid and the claims are correct. The algorithm proposed in the paper is a new artificial intelligence based approach for the problem of searching in a list of numbers, where the list is already sorted in a non-decreasing order. It is guaranteed to require sqrt(m) comparisons between pairs of numbers, where m is the size of the entire list, and this bound is also shown to be tight by the associated information-theoretic lower bound. The simulations also confirm these theoretical results.

##### • LLaMA-13B [Tou+23]:

![image 58](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile58.png)

The truth of the following claim is not determined: The number to be searched is specified by the user. For this problem, we develop a new artificial intelligence based algorithm and also prove theoretical guarantees for it.

##### • Open-Assistant Pythia-12B [LAI23]:

![image 59](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile59.png)

I cannot verify the accuracy of the claims in the paper. There is a missing comma in the third sentence of the paper, which should read: “We also provide an associated information-theoretic lower bound showing that our bound is tight, i.e., any algorithm will need at least these many comparisons in the worst case.”

There are also a few other typos or grammatical errors in the paper that should be addressed before it can be considered for publication. For example, in the second paragraph, the word “maximize” should be replaced with “maximize”.

To assist with the review, I could provide additional context such as the problem statement or the background of the authors, or I could ask follow-up questions to clarify some of the claims. Additionally, I could suggest ways to improve the clarity and readability of the paper.

##### • StableLM-7B [Sta23]:

![image 60](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile60.png)

Claim: The paper presents a new artificial intelligence-based algorithm for search in a sorted list of numbers, where the list is already sorted in a non-decreasing order. Explanation: The paper describes a new algorithm that requires only a constant number of comparisons between pairs of numbers, where m is the size of the list. The paper presents theoretical guarantees for this algorithm, showing that it requires at least

sqrt(m) comparisons in the worst case. The paper also presents simulations that confirm the theoretical results and demonstrate the practicality of the algorithm. The paper concludes by highlighting the importance of the new algorithm and its significance as a relevant result for practitioners.

##### • Dolly-v2-12B [Con+23]:

![image 61](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile61.png)

The first claim is that “We consider the problem of searching in a list of numbers, where the list is already sorted in a non-decreasing order.”. This claim is incorrect as the list is not sorted in a non-decreasing order. The list is sorted in a non-increasing order. The second claim is that “If the number exists in the list, then the search should return the position of that number in the list (if there are multiple copies of the number in the list, then it can return any one position)”. This claim is also incorrect as there is no guarantee that multiple copies of a number would result in any one position being returned. The third claim is that “If the number does not exist in the list, then it should output ‘does not exist’”. This claim is incorrect as the algorithm is not required to output anything if the number does not exist. The forth claim is that “Our algorithm requires only sqrt(m) comparisons between pairs of numbers, where m is the size of the entire list”. This claim is incorrect as the algorithm requires exactly m comparisons (drawing from the entire list) to find the specified number. The information-theoretic lower bound is also incorrect as it is a lower bound on the number of comparisons when the specified number is already known, whereas our algorithm requires only the number of comparisons when the specified number is being searched for.

###### • Bard [Man23]:

![image 62](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile62.png)

The paper you have provided seems to be well-written and well-argued. The authors have clearly defined the problem they are trying to solve, and they have provided a clear and concise description of their algorithm. They have also provided theoretical guarantees for their algorithm, and they have conducted simulations to confirm these guarantees.

I can find no obvious errors in the paper, and I think the authors have made a strong case for the validity of their claims. However, there are a few things that I would like to point out.

First, the authors state that their algorithm requires only sqrt(m) comparisons between pairs of numbers, where m is the size of the entire list. This is a very strong claim, and it would be interesting to see how their algorithm performs in practice, especially on large lists.

Second, the authors state that they have provided an associated information-theoretic lower bound showing that their bound is tight. This is a very impressive result, and it shows that the authors have a deep understanding of the problem.

Overall, I think this is a very well-written and well-argued paper. The authors have made a strong case for the validity of their claims, and I would be interested to see how their algorithm performs in practice.

Here are some specific things that I would like to see in the authors’ future work: More extensive simulations on larger lists.

A comparison of their algorithm to other existing algorithms. A more detailed explanation of the information-theoretic lower bound. I believe that this work has the potential to make a significant contribution to the field of artificial intelligence. I hope that the authors will continue to develop their algorithm and make it available to the public.

##### • GPT-4 (ChatGPT):

![image 63](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile63.png)

The paper deals with the problem of searching in a sorted list of numbers and introduces an AI-based algorithm with theoretical guarantees. The claims made in the paper seem significant, but there are issues that need to be clarified.

- 1. **Claim**: “Our algorithm requires only sqrt(m) comparisons between pairs of numbers, where m is the size of the entire list.”

This claim needs additional scrutiny. The standard algorithm for searching a sorted list is Binary Search, which has a time complexity of O(log m). The paper is claiming that their algorithm uses sqrt(m) comparisons, which is actually worse than Binary Search in terms of time complexity. Therefore, this claim seems suspicious and would need additional evidence to back it up.

- 2. **Claim**: “We provide an associated information-theoretic lower bound showing that our bound is tight, i.e., any algorithm will need at least these many comparisons in the worst case.”

The authors claim that the lower bound for any search algorithm on a sorted list is sqrt(m). This contradicts established knowledge about searching in sorted lists where the lower bound is log(m), as seen in Binary Search. So, based on the information given, this claim seems false.

- 3. **Claim**: “We conduct a large number of simulations that confirm this theoretical result.”

Without detailed information about the simulations or data to back this up, it is hard to evaluate this claim. However, if the authors’ theoretical claims are incorrect, it is likely that there could be issues with their simulations.

- 4. **Claim**: “Our result is especially important as it is rare for such practical artificial intelligence algorithms to also have such strong theoretical guarantees.”


This claim is more of an opinion than a fact. Whether or not it is true depends on the field of AI and the specific subproblem being addressed. While it is true that theoretical guarantees are highly valued, it is not rare for algorithms in AI to have theoretical guarantees.

Based on the information given, it is highly likely that at least two of these claims (1 and 2) are false. The other two cannot be fully evaluated without additional information. However, it is recommended that the authors revise their paper, focusing on the theoretical claims and the comparison with established algorithms like Binary Search.

#### A.2 Prompting strategies

In our pilot project focused on error detection, we initially utilized a strategy that involved prompting the LLM to write a review of a short research paper. Unfortunately, this approach did not yield the desired outcome, as the LLM was unable to identify errors in the given context. Subsequently, we achieved success

by asking the LLM a specific question – to check for correctness. We provide some more details below.

Here is the prompt we used when asking the LLM to review the entire paper: You are an expert reviewer for a scientific conference. You will be provided with a short version of a paper that contains the setting of the paper and the main claims. Please write a review for the paper. Here is the short paper: “...”

We provide below the response from GPT-4.

![image 64](Liu and Shah_2023_ReviewerGPT An Exploratory Study on Using Large Language Models for Paper Reviewing_images/imageFile64.png)

Title: Review of “A Novel AI-Based Algorithm for Efficient Search in Sorted Lists”

First and foremost, I commend the authors for taking on the challenge of providing both an innovative solution and a rigorous theoretical backing for a fundamental problem in computer science – searching in a sorted list. The topic is relevant, and the theoretical aspects of the paper are compelling.

Specifically, the assertion that the proposed algorithm requires only sqrt(m) comparisons, where m is the size of the list, is intriguing. If substantiated, it would indeed constitute a significant advancement, as many common algorithms like binary search operate with a time complexity of O(log m). Similarly, the establishment of an information-theoretic lower bound demonstrating that any algorithm would require at least sqrt(m) comparisons in the worst case is quite impressive.

The large-scale simulations conducted by the authors further enhance the credibility of their claims, particularly given the variety of scenarios tested – variations in list size, value distributions, and the searched value.

However, the authors fail to offer detailed technical specifics about the AI-based algorithm itself. For the scientific community to properly evaluate and potentially build upon this work, it’s crucial to outline the methodology more clearly. The authors should strive to provide greater insight into the design of the algorithm, including information about the AI model used, how it’s trained, and the techniques used to achieve the impressive sqrt(m) result.

Furthermore, the authors mention that the paper provides a rare instance of practical AI algorithms with strong theoretical guarantees. This statement could be bolstered with a more extensive comparison with existing solutions, underlining both the novelty and practical importance of the proposed algorithm.

In conclusion, the paper certainly introduces exciting prospects for the field. However, the lack of specific details regarding the AI-based algorithm and its operation is a major drawback. The paper would greatly benefit from a more detailed exposition of the algorithm, along with a comprehensive discussion contrasting it with existing methods. With these improvements, the paper has the potential to make a profound impact on the field of AI algorithms and data search methodologies.

It’s my recommendation that the paper should be accepted conditionally, provided that the authors make the suggested improvements to the methodology section and provide a more detailed comparative analysis with existing solutions.

### B NeurIPS checklist and prompts

In this section, we detail how we filtered the NeurIPS checklist items for the checklist experiment, as well as how we rephrased each item to create third-person perspective questions to include in the prompts.

#### B.1 Checklist item selection

We select the checklist items to include in our experiments based on the feasibility of creating a ground truth label in our manual labeling process (see Section 4.1). Through this criteria, we remove 2 of 18 questions from our main analysis:

- • 1. For all authors...

(a) Do the main claims made in the abstract and introduction accurately reflect the paper’s contributions and scope?

Item 1(a) is removed as the ground truth label requires significant domain knowledge in the paper’s field. To generalize our results, a majority of the papers in our analysis are randomly selected across the entire conference, thus we do not have enough expertise to evaluate this question.

- • 1. For all authors... (d) Have you read the ethics review guidelines and ensured that your paper conforms to them?


Item 1(d) is removed as a portion of the question references an action the authors take (reading the guidelines) that is not verifiable by the information they submit to the conference. Thus, both the labeler and the LLM cannot retrieve a reliable answer based on the information provided.

#### B.2 Full checklist questions

After removing two checklist items (Appendix B.1), we list the remaining 16 NeurIPS 2023 checklist items and the associated prompt questions we used in Table 4. These questions are the last component of the user prompt provided to the model.

Item Condition Question (Original) Prompt Question

- 1b For all authors...

Did you describe the limitations of your work?

Do the authors describe the limitations of their work?

- 1c


Did you discuss any potential negative societal impacts of your work?

Do the authors discuss any potential negative societal impacts of their work?

- 2a If you are including theoretical results...

Did you state the full set of assumptions of all theoretical results?

If the authors include theoretical results, do the authors state the full set of assumptions of all theoretical results?

- 2b


If the authors include theoretical results, do the authors include complete proofs of all theoretical results?

Did you include complete proofs of all theoretical results?

- 3a If you ran experiments...

Did you include the code, data, and instructions needed to reproduce the main experimental results (either in the supplemental material or as a URL)?

If the authors ran experiments, do the authors include the code, data, and instructions needed to reproduce the main experimental results (either in the supplemental material or as a URL)?

- 3b

Did you specify all the training details (e.g., data splits, hyperparameters, how they were chosen)?

If the authors ran experiments, do the authors specify all the training details (e.g., data splits, hyperparameters, how they were chosen)?

- 3c


Did you report error bars (e.g., with respect to the random seed after running experiments multiple times)?

If the authors ran experiments, do the authors report error bars (e.g., with respect to the random seed after running experiments multiple times)?

Item Condition Question (Original) Prompt Question

If the authors ran experiments, do the authors include the total amount of compute and the type of resources used (e.g., type of GPUs, internal cluster, or cloud provider)?

Did you include the total amount of compute and the type of resources used (e.g., type of GPUs, internal cluster, or cloud provider)?

- 3d


- 4a If you are using existing assets (e.g., code, data, models) or curating/ releasing new assets...

If your work uses existing assets, did you cite the creators?

If the authors use existing assets (e.g., code, data, models), do the authors cite the creators?

- 4b

Did you mention the license of the assets?

If the authors use existing assets (e.g., code, data, models) or curate/release new assets, do the authors mention the license of the assets?

- 4c

Did you include any new assets either in the supplemental material or as a URL?

If the authors curate/release new assets (e.g., code, data, models), do the authors include any new assets either in the supplemental material or as a URL?

- 4d

Did you discuss whether and how consent was obtained from people whose data you’re using/curating?

If the authors curate/release new assets (e.g., code, data, models), do the authors discuss whether and how consent was obtained from people whose data they are using/curating?

- 4e


If the authors curate/release new assets (e.g., code, data, models), do the authors discuss whether the data they are using/ curating contains personally identifiable information or offensive content?

Did you discuss whether the data you are using/curating contains personally identifiable information or offensive content?

- 5a If you used crowdsourcing or conducted research with human subjects...

Did you include the full text of instructions given to participants and screenshots, if applicable?

If the authors used crowdsourcing or conducted research with human subjects, do the authors include the full text of instructions given to participants and screenshots, if applicable?

- 5b

Did you describe any potential participant risks, with links to Institutional Review Board (IRB) approvals, if applicable?

If the authors used crowdsourcing or conducted research with human subjects, do the authors describe any potential participant risks, with links to Institutional Review Board (IRB) approvals, if applicable?

- 5c


If the authors used crowdsourcing or conducted research with human subjects, do the authors include the estimated hourly wage paid to participants and the total amount spent on participant compensation?

Did you include the estimated hourly wage paid to participants and the total amount spent on participant compensation?

Table 4: A list of original checklist items (first-person) and their corresponding prompt questions (third-person). Original checklist items are separated into categories, with each category having a prerequisite condition. Prompt questions are individually input into the LLM, so they include content from both the condition and original checklist question.

