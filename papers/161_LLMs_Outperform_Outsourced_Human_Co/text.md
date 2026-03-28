# LLMs outperform outsourced human coders on complex textual analysis

Vicente J. Bermejo*, Andrés Gago†, Ramiro H. Gálvez‡, Nicolás Harari§ 24 December 2024

Abstract. This paper evaluates the effectiveness of large language models (LLMs) in extracting complex information from text data. Using a corpus of Spanish news articles, we compare the performance of various LLMs with that of outsourced human coders on ﬁve natural language processing tasks, ranging from named entity recognition to identifying nuanced political criticism in news articles. We ﬁnd that LLMs consistently outperform outsourced human coders, especially in tasks requiring deep contextual understanding. These ﬁndings suggest that current LLM technology provides researchers without programming expertise a cost-effective alternative for sophisticated text analysis.

Keywords: Large Language Models; Text Analysis; Human Annotation; Natural Language

Processing; News Media JEL Codes: C80; C83; C88

*ESADE Business School †Universidad Torcuato Di Tella ‡Universidad Torcuato Di Tella §Boston University

• We thank Francisco Olivero for excellent research assistance. We also thank Ruben Durante, Konstantina Zacharaki and participants at WU’s Socioeconomic Research Seminar for their help and comments.

Text data has become increasingly relevant in social and behavioral sciences research (Barberá et al., 2021; Rathje et al., 2024), enabling the study of phenomena that are challenging to capture using traditional structured, tabular data (see Gentzkow et al., 2019a). However, while analyzing large volumes of text data holds signiﬁcant potential, processing such data at scale presents considerable challenges (Rathje et al., 2024). To address these challenges, researchers have employed several methodological approaches, each with distinct advantages and limitations.

A ﬁrst approach involves human readers manually coding text content. Although this method is popular among social and behavioral scientists, it can be costly both in terms of time and money, and does not scale well to the massive text corpora now available (Ash and Hansen, 2023).1 Another simple approach involves dictionary methods, which count words from speciﬁc pre-deﬁned categories.2 While more scalable, they often fall short of the accuracy achieved by manual annotators, frequently necessitating manual review of the results (e.g., Ang, 2023; Couttenier et al., 2024). Moreover, their success is typically limited to straightforward natural language processing (NLP) tasks, such as categorizing the sentiment of a text or determining whether it covers a certain topic — cases where predeﬁned word categories may align well with the concepts being measured. Although newer and more sophisticated supervised machine learning (SML) methods, such as BERT-like models (Devlin et al., 2019), overcome many of these limitations, they have two key drawbacks: they typically require high coding proﬁciency and depend on manually annotated training texts (Gilardi et al., 2023).3 These two factors present signiﬁcant barriers for social scientists seeking to utilize advanced SML methods.4

In this study, we evaluate a novel approach: using generative large language models (LLMs) as zero-shot learners.5 Concretely, we benchmark the performance of different LLMs on NLP tasks requiring deep semantic and contextual knowledge, comparing their performance with that of outsourced human coders on the same tasks.6 We analyze a corpus of 210 Spanish-language news articles, a random sample from the 21,627 news articles analyzed in Bermejo et al. (2023), which cover a nationwide ﬁscal consolidation program affecting more than 3,000 Spanish municipalities. For each news article, we make separate application programming interface (API) calls to different LLMs (GPT-3.5-turbo, GPT-4-turbo, Claude 3 Opus, and Claude 3.5 Sonnet). In each call, we request the respective model to complete ﬁve tasks using a zero-shot learn-

- 1See, for example, Ellison (2002); Romer and Romer (2010); Ferrara et al. (2012); Cloyne (2013); Benoit et al. (2016a); Fryer Jr (2019); Davis et al. (2019); Esposito et al. (2023); Naef (2024); Cloyne et al. (2025).
- 2See, for example, Gentzkow et al. (2011, 2014, 2015); Zhang (2016); Brady et al. (2017); Buehlmaier and Whited (2018); Shapiro and Wilson (2022). 3Note that if multiple NLP tasks need to be performed, a separate set of labeled data must be generated and a distinct model must be trained for each task. 4For a review on how different NLP strategies can be used in economics research, see Ash et al. (2024). 5Zero-shot learning refers to a model’s ability to perform tasks without any task-speciﬁc training examples, where LLMs leverage their pre-trained knowledge to understand and respond to novel prompts. This capability stems from the models’ exposure to diverse text during pre-training and their ability to generalize across contexts (see Kojima et al., 2022). 6For a comprehensive review of generative AI applications across economics research, see Korinek


(2023).

ing approach: (T1) list all municipalities mentioned in the article, (T2) indicate the total number of municipalities mentioned, (T3) determine if the article contains criticisms of municipal performance, (T4) identify the source of the criticism — if any, and (T5) identify the speciﬁc target of the criticism — if any. In addition, we recruit university students (primarily Spanish) to complete the same tasks in an incentivized online study and compare their performance with that of LLMs. Following Song et al. (2020), we compare the answers from the different methods against a set of gold standard labels created by expert human coders who followed a careful and systematic approach, engaging in thorough deliberation to determine the most appropriate answer for each question (see Section 2.3.1).

Our results reveal a signiﬁcant performance gap between LLMs and outsourced human coders. While human coders performed above chance across all tasks, LLMs consistently outperformed them across the board. The superior performance of LLMs is so pronounced that they achieve better results when analyzing complex, lengthy articles than human coders achieve with simpler, shorter ones (see Section B.2 for a discussion on our criteria for classifying an article as “difﬁcult” for a given task). We also ﬁnd that LLM responses exhibit higher internal consistency than those of human coders. When we keep only those human coders whose competence is above the median, we ﬁnd that LLMs are still a better alternative than the best human coders. This is especially the case for the more advanced LLMs, which attain higher performance levels than older LLMs, suggesting that future advancements may lead to even more accurate and nuanced text analysis capabilities.7

These ﬁndings indicate that LLMs are a highly cost-effective alternative to outsourced coders for extracting complex information from text data. Our results demonstrate that LLMs’ superior performance over outsourced coders extends to tasks requiring sophisticated reasoning and contextual knowledge, such as T4 and T5 — an important dimension not extensively explored in previous research (see Section 1). Notably, this superior performance is achieved through straightforward API calls that neither require advanced coding skills nor rely on human-labeled training data, unlike modern SML models. These advantages position LLMs as a powerful tool for researchers analyzing large text corpora, enabling research questions previously constrained by methodological limitations.

## 1 Related work

In recent years, the growing availability and diversity of text data have enabled researchers to explore an unprecedented range of topics. Social media posts have been

7As documented in Huang et al. (2023b), the training data for current LLMs is predominantly in English. Consequently, these models typically demonstrate superior performance in English compared to other languages (see Etxaniz et al., 2024). Given this linguistic bias, our results, which are based on multilingual LLMs processing Spanish documents, should not be interpreted as an upper bound. In fact, one would expect even larger performance advantages over outsourced human coders when applying these models to English-language documents.

used to examine phenomena ranging from emotional contagion (e.g., Kramer et al., 2014) and inﬂation expectations (e.g., Angelico et al., 2022) to electoral dynamics and political polarization (e.g., Allcott and Gentzkow, 2017; Brady et al., 2017; Simchon et al., 2022; González-Bailón et al., 2023; Guess et al., 2023a,b). Building on the narrative approach pioneered by Romer and Romer (1989), researchers have leveraged central bank communications and government statements to conduct causal analyses within macroeconomic general equilibrium models.8 Legislative records, such as ﬂoor speeches and committee hearings, have been analyzed to understand political processes (e.g., Quinn et al., 2010; Grimmer and King, 2011; Gentzkow et al., 2019b), while media content, including movie scripts and subtitles, has been used to study social phenomena like gender stereotypes (e.g., Ferrara et al., 2012; Gálvez et al., 2019; Bertsch et al., 2022; Martinez et al., 2022).

Among various types of text data, news articles have received particular attention in social science research, serving both as an object of analysis (see, for example, Gentzkow and Shapiro, 2010; Vos and Aelst, 2018; Capozza et al., 2022) and as a means to understand broader phenomena. News content analysis has been used for policy impact evaluation (e.g., Ramey and Shapiro, 1998; Ramey, 2011; Gunter et al., 2021; García-Uribe, 2023), to examine the effects of bank runs (Jalil, 2015), to understand how expectations inﬂuence diverse outcomes (Larsen and Thorsrud, 2019; Aromi, 2020; García-Uribe et al., 2024; Baker et al., 2024), and to improve economic forecasting (Barbaglia et al., 2023). Research has also demonstrated that media coverage can shape political outcomes and government decisions (Eisensee and Strömberg, 2007; Snyder Jr and Strömberg, 2010; Durante and Zhuravskaya, 2018; Enikolopov et al., 2018; Djourelova and Durante, 2022; Caprini, 2023), and that news content can enhance stock market price predictability (Tetlock, 2007; Dougal et al., 2012; Garcia, 2013; Lopez-Lira and Tang, 2024). Given their richness and complexity, which demand sophisticated and sometimes contextual understanding, we use news articles to benchmark the performance of both LLMs and human coders on complex NLP tasks.

This paper relates with ongoing work demonstrating the high performance of LLMs in NLP tasks traditionally addressed through conventional SML strategies (see, for example, Huang et al., 2023a; Lopez-Lira and Tang, 2024; Rathje et al., 2024; Mu et al., 2024; Ziems et al., 2024; Chang et al., 2024; Leiter et al., 2024). The study most similar to ours in benchmarking LLMs against human coders is Gilardi et al. (2023), which analyzes corpora of tweets and news articles. Their results show that GPT-3.5-turbo outperforms crowd workers by approximately 25 percentage points on various content moderation annotation tasks in social media.

Our paper extends previous literature in several ways. First, it considers a broader range of NLP tasks, including named entity recognition (NER) — an NLP task not previously explored in the related literature. Second, and more importantly, it evaluates

8See, for example, Barro and Redlick (2011); Mertens and Ravn (2011, 2012, 2013, 2014); Guajardo et al.

(2014); Nguyen et al. (2021); Demirel (2021).

tasks requiring extensive contextual knowledge.9 For example, determining whether an article includes criticisms to the municipal government of Barcelona (an example of T3), requires distinguishing if the criticisms directed at the government of Barcelona refer to: the government of the city of Barcelona, or the government of the province of Barcelona. Such distinction can sometimes be inferred from the text if one has contextual knowledge (recognizing a politician afﬁliated with the city hall or knowing that the criticized service is a municipal responsibility), but may be otherwise not apparent. Finally, we evaluate tasks that require sophisticated analysis of complete texts rather than isolated excerpts. For instance, in T4 and T5, identifying the source and target of criticism often demands understanding the broader narrative and context of the entire article. Together, these features distinguish our work from previous LLM performance studies, demonstrating unprecedented accuracy in complex text analysis tasks that better reﬂect real-world research challenges.

## 2 Materials and methods

- 2.1 News articles sample


News articles serve as an ideal document type for benchmarking LLMs’ performance on complex text analysis tasks. These documents are information-rich, substantial in length, and cover topics that require contextual knowledge for accurate interpretation. Given these considerations, we chose to analyze a subset of the articles collected in Bermejo et al. (2023), which focus on articles referencing Spanish municipalities and the Supplier Payment Program.10

The corpus comprises 24,134 articles retrieved from Factiva, an international news database produced by Dow Jones that aggregates content from over 30,000 sources across more than 200 countries. The retrieval ﬁlters selected articles written in Spanish or Catalan, published between 2011 and 2013, that referenced both Spanish municipalities and the Supplier Payment Program. For each article, Factiva provides its title, a snippet (a brief extract or summary of the article’s content), and its main text. For further details on the selection process, refer to Appendix A.1.

For the current study, we sampled 210 Spanish-written news articles from the Factiva corpus.11 This represents approximately 1% of the articles considered in Bermejo et al. (2023) and constitutes a sample size manageable for annotation by human coders. In

- 9In contrast, the tasks in Gilardi et al. (2023) can be answered primarily by analyzing the content within the documents themselves, without requiring external context.
- 10The Great Recession of 2008–2009 caused a sharp deterioration in the ﬁnancial health of Spanish municipalities. During the subsequent years, regional and local governments accumulated arrears owed to thousands of ﬁrms. In 2012, the Spanish government launched the Supplier Payment Program (Plan de Pago a Proveedores) to address these arrears. Under this program, suppliers with outstanding local government payments dated prior to 2012 could receive payment through the state-owned Ofﬁcial Credit Institute (Instituto de Crédito Oﬁcial). The total volume of arrears amounted to €30 billion (equivalent to


###### 3% of Spanish GDP) and affected more than 130,000 suppliers.11Before drawing our sample of 210 articles, we excluded 330 articles that exceeded GPT-3.5-turbo’s max-

imum token limit of 4,097 tokens. This threshold affected only 1.5% of the articles from the original sample. Additionally, we removed 53 articles for which GPT-3.5-turbo encountered an error (typically a

- Appendix A.2, we provide one article as an example. The average article length in our subsample is 508.14 words, with the 10th, 50th, and 90th percentiles being 185.7, 478, and 887.3 words respectively.12 The articles vary in both complexity and topical coverage.


### 2.2 Tasks description

We analyze the same ﬁve tasks used in Bermejo et al. (2023), which we brieﬂy summarize below (see Appendix B.1 for detailed descriptions):

- • T1: List the names of all the municipalities mentioned in the article.
- • T2: Indicate how many municipalities are mentioned.
- • T3: Specify whether the municipal government is criticized in the article.
- • T4: If there are any criticisms, specify who makes them, choosing from a list of options.
- • T5: If there are any criticisms, specify towards whom they are directed, choosing from a list of options.


Note that each successive task involves increasing complexity and requires greater contextual knowledge for accurate completion. The ﬁrst two tasks are closely related:

- T1 requires identifying municipalities mentioned in the text (a form of NER), while T2 simply involves counting these identiﬁed municipalities.


- T3 requires not only understanding the text but also forming an opinion about it. Since it only requires a “yes” or “no” answer, it can be interpreted as a binary classiﬁcation problem in the context of NLP tasks. T4 and T5 have the highest level of complexity, as they require inferring the direction of criticisms, if present. It is important to note that the article may only mention the name of the person issuing the criticism. Identifying, for example, that the criticism is coming from the opposition would involve recognizing that the person issuing it belongs to a party opposing the one being criticized, which requires substantial contextual knowledge.
- T4 and T5 are unique in that they may have multiple correct options. For example, an article might include criticisms from different parties, making both options 4 and
- 5 correct (see Appendix B.1). Alternatively, an article might mention criticism issued by a councilor from the ruling party and speciﬁcally identify the party, in which case option 2 would be correct, along with options 4 or 5 (see Appendix B.1). In NLP, these tasks are treated as multi-label classiﬁcation problems, where multiple class labels can be assigned to a single document. Section 2.4 details how we evaluate tagging performance across all tasks.


timeout) during the analysis in Bermejo et al. (2023). If a sampled article was written in Catalan, classiﬁed as a commentary, or deemed excessively short, it was replaced through resampling.

- 12These calculations use the word counts provided by Factiva, which sum the total number of words in an article’s title, snippet, and body. Note that words as humans understand them do not map directly to tokens (which LLMs take as input), where a token typically represents about 4 characters in English.


### 2.3 Coding strategies

In this section, we describe the strategies used to accomplish the previously outlined tasks.

#### 2.3.1 High-skill coders (gold standard labels)

A primary strategy involved having highly skilled coders complete all ﬁve tasks for each article. Following the recommendations of Song et al. (2020), we implemented rigorous quality assurance measures throughout the coding process. Consequently, we consider these labels our gold standard for evaluating alternative content analysis methods.

To achieve this, we followed the procedure outlined below. First, all authors deliberated on the appropriate answer for each task, reaching consensus on what should be considered correct. Second, one author carefully read all 210 news articles and completed each task for each article. Third, each article, along with its initial answers, was redistributed either to a trained research assistant (RA) or to a second author. Articles were redistributed so that those presumed more challenging were assigned to authors rather than the RA. Fourth, each article was read once more by the assigned author or the RA and each task was coded again. Most initial answers remained unchanged and were considered ﬁnal. However, when the second coder’s answer differed from the original, successive authors evaluated the article, deliberating until reaching consensus. This process could either conﬁrm the original answer or establish a new one.

Inter-coder agreement, measured as the percentage of agreement with the initial tagging, was consistently high across all tasks: 83.81% for T1, 81.9% for T2, 91.43% for T3, 84.29% for T4, and 84.29% for T5. For T4 and T5, agreement dropped to 72.73% when considering only articles where the municipal government was criticized (i.e., when

- T3 was coded as “yes”), suggesting these tasks were more challenging than the ﬁrst three. Nevertheless, all results exceeded the 70% agreement threshold commonly considered acceptable in the literature (see Graham et al., 2012), indicating that the initial tagging already met satisfactory quality standards. Appendix B.2 provides descriptive statistics of the ﬁnal answers for each task.


#### 2.3.2 LLMs as coders

To assess the performance of LLMs on the proposed tasks, we utilized several popular state-of-the-art commercial models. Speciﬁcally, we employed two models from OpenAI and two from Anthropic, both leading companies in the development of advanced language models. From OpenAI, we utilized GPT-3.5-turbo, which powered the free tier of ChatGPT at the time of our analysis, and GPT-4-turbo, OpenAI’s most advanced model at that time. From Anthropic, we used Claude 3 Opus and Claude 3.5 Sonnet, the two highest-performing models available from Anthropic during our analysis period, with the latter considered the more powerful of the two. Both An-

thropic models were reported to surpass OpenAI’s models in public benchmarks at the time of analysis.

For each of these models, we made two independent API calls per news article, totaling 1,680 API calls (210 news articles × 4 models × 2 calls per article per model). In

- Appendix B.3, we provide the template used to prompt the different LLMs to complete the proposed tasks for each news article. Note that, in a single call, we requested all ﬁve tasks to be completed for a given news article. Thus, for each news article, task, and model, we have two independent observations. In all cases, the “temperature” parameter was set to 0, with lower values intended to make the outputs more deterministic. However, this does not guarantee fully deterministic behavior. Taking this into consideration, we will evaluate and compare the internal consistency of each model across repeated trials.


We spent US$0.20 to obtain all answers from GPT-3.5 (April 2024), US$3.46 from GPT-

- 4 (April 2024), US$8.53 from Claude 3 Opus (June 2024), and US$2.28 from Claude 3.5 Sonnet (July 2024). In each case, we received the complete set of answers within minutes. For comparison, in Bermejo et al. (2023), processing ∼22,000 news articles took less than two days using GPT-3.5-turbo at a cost of US$96 (October 2023).


Importantly, for tasks T4 and T5, we prompted the LLMs to provide a single answer encoded as an integer, even when multiple correct answers were possible. We chose this approach based on preliminary results indicating it produced more accurate responses. As we will described in Section 2.4, we consider selecting at least one of the correct answers as the desired outcome.13

#### 2.3.3 Outsourced human coders

To evaluate the performance of LLMs against more traditional, less scalable, and typically costlier alternatives, we conducted an online study. Students from ESADE, a Spanish university in Barcelona, Catalonia, completed the proposed tasks on a subset of 210 news articles used in this paper. This approach, commonly referred to as crowdsourcing — obtaining input from a large group of people, often via online platforms — has been validated as a reliable strategy for labeling text data in several studies (see, for example, Benoit et al., 2016b).

Students completed the study online using Qualtrics, a web-based software platform for creating surveys and collecting data. Each participant was asked to read three news articles and to complete the ﬁve associated tasks while reading each of them. To maintain parallelism with what we requested from the LLMs, Qualtrics only allowed a single answer for T4 and T5.

Our initial goal was to have each article read by two students, targeting a total of 140 participants. Recruitment was conducted via an open online platform accessible to

- 13This approach aligns with the methodology in Bermejo et al. (2023), where answers for these two tasks were re-coded based on correctly identifying one option associated with the governing party or one option associated with the opposition party.


all ESADE students, with participants receiving course credit for their involvement.14 To ensure response quality and reliability, the questionnaire included two attention check questions with clear, correct answers, explicitly communicated to students (see Hauser et al., 2019). At the start of the survey, students were informed that failing these checks could result in no course credit. Additionally, per ESADE’s course credit policy, students understood that incomplete participation (i.e., not answering all three news articles) would also forfeit credit. This approach incentivized participants to complete all tasks accurately.

If a participant failed an attention check or did not complete all the requested tasks, we excluded all their responses and reassigned their articles to a new participant a few days later.15 The ﬁnal sample included 146 participants and was collected over approximately 98 days. The sample is balanced by gender, with 48.6% self-identifying

- as female and 48.6% as male. The average age was 19.3 years (SD = 0.9), with the vast majority being undergraduate students and only one graduate student. Of the 146 participants, 126 (86.3%) were Spanish citizens. The remaining 20 participants were of various nationalities, with 90% of these foreign participants having lived in Spain for at least one year. The median completion time for all three news items was 17.43 minutes, with approximately 90% completing the task in 33.38 minutes or less.


Compared to online platforms like MTurk or Proliﬁc, our subject pool is presumably more educated and familiar with the (Spanish) context. We selected ESADE students because it is a top-ranked university in Spain and is commonly used by economics and business school researchers to recruit research assistants. This pool offers a signiﬁcant advantage for tasks requiring sophistication and contextual knowledge.

### 2.4 Performance metrics

As described in Section 2.3, the tasks assigned to LLMs and outsourced human coders correspond to various NLP task families. T1 corresponds to a NER problem, for which we use the macro-averaged F1 score as the performance metric. This score is the arithmetic mean of article-level F1 scores, where each article’s F1 score is the harmonic mean of precision and recall. Precision represents the proportion of municipalities identiﬁed by a coder (LLM or human) that appear in the gold standard labels. Recall represents the proportion of municipalities in the gold standard labels that are correctly identiﬁed by the coder.16 All these metrics range from 0 to 1, with larger values indicating better performance.

During data collection, we requested two answers for every news article, resulting in 420 responses. This approach was applied consistently for both the outsourced human coders and each LLM tested. Considering this, we calculated the macro-averaged F1

14See Appendix Figure D1. 15Out of an original sample of 140 subjects, 9 failed one or more attention checks, and 23 left the survey

incomplete. All additional subjects recruited to substitute them completed the survey and passed all attention checks.

16Before calculating precision and recall, we ﬁrst correct any misspellings in the text provided by the coders.

score over these 420 responses. The obtained value should thus be interpreted as the estimated performance for a randomly selected news article and tagger. A similar approach is followed for calculating the performance metrics for the remaining tasks.

- T2 corresponds to a regression problem, for which we use the mean absolute error (MAE) between coders’ values and gold standard labels as the performance metric (lower values indicate better performance). T3 is akin to a binary classiﬁcation problem (with “yes” and “no” labels), where coders could also answer “unsure” (99 for LLMs). We measure accuracy as the proportion of correct answers in the 420 responses, treating “unsure” responses as incorrect.17

- T4 and T5 represent multi-label classiﬁcation problems. While such tasks typically evaluate both correct and incorrect identiﬁcations across all possible labels, our requirement of a single label per article demands a different approach. We measure accuracy as the proportion of responses identifying any correct label, where “the answer does not ﬁt into any of the previous strategies” (code 98 for LLMs) is considered valid, and “unsure” (code 99 for LLMs) is treated as incorrect.18


- 3 Results


In this section, we present our main results. Section 3.1 analyzes the overall performance of alterntative coding strategies. Section 3.2 examines how article characteristics affect coders’ performance. Section 3.3 validates the quality of outsourced human coders’ work. Finally, Section 3.4 evaluates the internal consistency across coding strategies.

### 3.1 Overall performance

- Figure 1 illustrates the performance of outsourced human coders and LLMs across all tasks (see Appendix Table D1 for detailed values). Higher values indicate better performance in all panels except for T2, where lower MAE values reﬂect better performance. The ﬁnal panel (“All correct”) shows the proportion of news articles where coders successfully completed all ﬁve tasks.


Visual inspection of Figure 1 reveals several notable patterns. First, all LLMs outperform outsourced coders across all tasks. Second, while GPT-3.5-turbo outperforms outsourced humans, it lags behind other LLM models. Third, Claude 3.5 Sonnet achieves the highest scores across tasks, though often only marginally surpassing GPT-4-turbo. This last result suggests that as LLMs continue to grow more powerful, the performance gap between them and outsourced human coders will only expand. We conﬁrm these patterns in the regression analysis we present in Appendix C.1 (see Appendix Table C1).

- 17In no instance was “unsure” assigned in the gold standard labels.
- 18In no instance was “unsure” assigned in the gold standard labels, but for some articles “the answer does not ﬁt into any of the previous strategies” was the correct answer in the gold standard labels.


Figure 1: Overall performance, across tasks and coding strategies

T1: Cities names (Macro F1)

T2: Named cities count (MAE)

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


| | | | | |
|---|---|---|---|---|
| | | | | |


Outsourced humans

GPT-3.5-turbo

GPT-4-turbo

Claude 3 Opus

Claude 3.5 Sonnet

0.0 0.2 0.4 0.6 0.8 1.0

0.0 0.2 0.4 0.6 0.8 1.0

T3: Presence of criticism (Accuracy)

T4: Source of criticism (Accuracy)

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


| | | | | |
|---|---|---|---|---|
| | | | | |


Outsourced humans

GPT-3.5-turbo

GPT-4-turbo

Claude 3 Opus

Claude 3.5 Sonnet

0.0 0.2 0.4 0.6 0.8 1.0

0.0 0.2 0.4 0.6 0.8 1.0

T5: Target of criticism (Accuracy)

All correct (Proportion)

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


| | | | | |
|---|---|---|---|---|
| | | | | |


Outsourced humans

GPT-3.5-turbo

GPT-4-turbo

Claude 3 Opus

Claude 3.5 Sonnet

0.0 0.2 0.4 0.6 0.8 1.0

0.0 0.2 0.4 0.6 0.8 1.0

- Note: Figure 1 displays the overall performance across all tasks and coding strategies. For T1, the ﬁgure


shows the Macro F1 score; for T2, the Mean Absolute Error (MAE); and for T3, T4, and T5, it shows the accuracy. For T2, a lower number denotes better performance, while for the remaining tasks, higher numbers indicate better performance. The “All correct” panel indicates the proportion of news articles for which all tasks were completed entirely correctly, broken down by coding strategy.

### 3.2 Factors inﬂuencing coders’ performance

#### 3.2.1 Task difﬁculty

- Figure 2 replicates Figure 1, presenting outcomes by task difﬁculty for each article (see Table D2 for detailed results). We classify a task as difﬁcult if at least two authors initially disagreed on the correct answer during the elaboration of the gold standard. In the “All correct” panel, an article is categorized as difﬁcult if any of its tasks are classiﬁed as difﬁcult.


- Figure 2 shows that performance declines with task difﬁculty across all tasks, with GPT-3.5-turbo and GPT-4-turbo in T3 being the only exceptions to this pattern. Moreover, visual inspection of Figure 2 shows that state-of-the-art models, such as Claude 3.5 Sonnet and GPT-4-turbo, generally perform better on the difﬁcult tasks than outsourced human coders do on the easier ones.


Examining GPT-3.5-turbo’s performance in T4 and “All correct” — the two cases where it did not signiﬁcantly outperform human coders in the full sample (see Figure 1 and Table C1) — reveals that it still achieves higher accuracy than human outsourced coders on difﬁcult articles (see Appendix Table C2). This ﬁnding suggests that even

Figure 2: Performance by article difﬁculty, across tasks and coding strategies

T1: Cities names (Macro F1)

T2: Named cities count (MAE)

Outsourced humans

GPT-3.5-turbo

GPT-4-turbo

Claude 3 Opus

Claude 3.5 Sonnet

0.0 0.2 0.4 0.6 0.8 1.0

0.0 0.5 1.0 1.5 2.0

T3: Presence of criticism (Accuracy)

T4: Source of criticism (Accuracy)

Outsourced humans

GPT-3.5-turbo

GPT-4-turbo

Claude 3 Opus

Claude 3.5 Sonnet

0.0 0.2 0.4 0.6 0.8 1.0

0.0 0.2 0.4 0.6 0.8 1.0

T5: Target of criticism (Accuracy)

All correct (Proportion)

Outsourced humans

GPT-3.5-turbo

GPT-4-turbo

Claude 3 Opus

Claude 3.5 Sonnet

0.0 0.2 0.4 0.6 0.8 1.0

0.0 0.2 0.4 0.6 0.8 1.0

Regular Difficult

- Note: Figure 2 displays the overall performance across all tasks and coding strategies classiﬁed by task


difﬁculty. For T1, the ﬁgure shows the Macro F1 score; for T2, the Mean Absolute Error (MAE); and for T3, T4, and T5, it shows the accuracy. For T2, a lower number denotes better performance, while for the remaining tasks, higher numbers indicate better performance. The “All correct” panel indicates the proportion of news articles for which all tasks were completed entirely correctly, broken down by coding strategy.

the lowest-performing LLM in our analysis surpasses human coders’ accuracy on more challenging tasks.

#### 3.2.2 Text length

Text length has been identiﬁed as an important factor affecting LLM performance. For instance, LLMs are known to exhibit the “lost-in-the-middle” effect (An et al., 2024), where information appearing in the middle of the input tends to receive less attention than content at the beginning or end. Similarly, human readers generally ﬁnd longer texts more challenging to process than shorter ones. For this reason, in

- Figure 3 we replicate Figure 1, but with outcomes separated based on the length of the


news articles (see Table D3 for detailed results). We deﬁne an article as “long” if its word count (as provided by Factiva) is larger than the 90th percentile calculated over our sample of 210 news articles analyzed, and “regular” otherwise.

Figure 3: Performance by article length, across tasks and coding strategies

T1: Cities names (Macro F1)

T2: Named cities count (MAE)

Outsourced humans

GPT-3.5-turbo

GPT-4-turbo

Claude 3 Opus

Claude 3.5 Sonnet

0.0 0.2 0.4 0.6 0.8 1.0

0.0 0.5 1.0 1.5 2.0

T3: Presence of criticism (Accuracy)

T4: Source of criticism (Accuracy)

Outsourced humans

GPT-3.5-turbo

GPT-4-turbo

Claude 3 Opus

Claude 3.5 Sonnet

0.0 0.2 0.4 0.6 0.8 1.0

0.0 0.2 0.4 0.6 0.8 1.0

T5: Target of criticism (Accuracy)

All correct (Proportion)

Outsourced humans

GPT-3.5-turbo

GPT-4-turbo

Claude 3 Opus

Claude 3.5 Sonnet

0.0 0.2 0.4 0.6 0.8 1.0

0.0 0.2 0.4 0.6 0.8 1.0

Regular Long

- Note: Figure 3 displays the overall performance across all tasks and coding strategies classiﬁed by article


length. For T1, the ﬁgure shows the Macro F1 score; for T2, the Mean Absolute Error (MAE); and for T3, T4, and T5, it shows the accuracy. For T2, a lower number denotes better performance, while for the remaining tasks, higher numbers indicate better performance. The “All correct” panel indicates the proportion of news articles for which all tasks were completed entirely correctly, broken down by coding strategy.

Both Figure 3 and the long-article dummy in Appendix Table C1 indicate that longer articles pose greater challenges for both human coders and LLMs. In all tasks except T1, a marked decline in performance is observed for long articles relative to shorter ones. Notably, visual inspection of the ﬁgure shows that LLMs achieve higher performance on long articles than human coders achieve on shorter ones.

### 3.3 Analysis of the outsourced human coders’ performance

The results presented above demonstrate that LLMs consistently outperform human coders in the tasks conducted in this study. However, one might question whether this superior performance is due to outsourced human coders failing to comply with the study’s requirements. In this section, we present results which suggest that 1) outsourced human coders performed in a competent way, and 2) even when restricting our analysis to a subset of high-performing outsourced human coders, the main results presented in this study hold.

#### 3.3.1 Outsourced coders’ competence and task performance

- Figure 4 provides evidence indicating that outsourced human responses were indeed competent. First, for tasks T1 through T5, we present the extent to which the overall performance of human-provided answers differs from what would be expected by pure chance. Speciﬁcally, for each task’s performance metric, we conducted a permutation test and calculated the upper conﬁdence interval at the 97.5th percentile. A result was considered signiﬁcant at the 5% level if the observed value exceeded this upper threshold (plotted as a black vertical line), except for T2, where it is considered signiﬁcant if it is below the threshold (see Appendix Table D4 for detailed results).19 Second, if participants became fatigued or bored as the task progressed, we would expect lower scores on the ﬁnal task compared to the ﬁrst. To investigate whether this occurred, we analyze the performance trends across tasks based on the order in which participants reviewed the news articles (recall that each participant provided responses for three news articles in sequence, see Appendix Table D5 for detailed results).


19This permutation test evaluates the signiﬁcance of a performance metric between actual values (y) and predicted values (yˆ) as follows: yˆ is permuted 2,000 times, and the metric is computed for each permutation, generating a null distribution. The observed metric is deemed signiﬁcant if it surpasses the 97.5th percentile of this distribution.

Figure 4: Human coders’ performance, statistical signiﬁcance, and task progression

T1: Cities names (Macro F1)

T2: Named cities count (MAE)

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


| | | | | |
|---|---|---|---|---|
| | | | | |


Overall

First article

Second article

Third article

0.0 0.2 0.4 0.6 0.8 1.0

0.0 0.5 1.0 1.5 2.0

T3: Presence of criticism (Accuracy)

T4: Source of criticism (Accuracy)

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


| | | | | |
|---|---|---|---|---|
| | | | | |


Overall

First article

Second article

Third article

0.0 0.2 0.4 0.6 0.8 1.0

0.0 0.2 0.4 0.6 0.8 1.0

T5: Target of criticism (Accuracy)

All correct (Proportion)

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


| | | | | |
|---|---|---|---|---|
| | | | | |


Overall

First article

Second article

Third article

0.0 0.2 0.4 0.6 0.8 1.0

0.0 0.2 0.4 0.6 0.8 1.0

- Note: Figure 4 shows the performance distribution by task order for the outsourced human coders. For


T1, the ﬁgure shows the Macro F1 score; for T2, the Mean Absolute Error (MAE); and for T3, T4, and T5, it shows the accuracy. For T2, a lower number denotes better performance, while for the remaining tasks, higher numbers indicate better performance. The “All correct” panel indicates the proportion of news articles for which all tasks were completed entirely correctly. For T1, T3, T4, and T5, observed values above the black line indicate performance signiﬁcantly better than random chance in the permutation tests (5% level), while for T2, observed values below the line indicate signiﬁcantly better performance.

For all tasks, human coders performed signiﬁcantly above random chance. Their accuracy peaked when coding the second news article, surpassing both their ﬁrst and last article performance, suggesting a pattern of initial learning followed by fatigue (see Appendix Table C3). This contrasts with LLMs, which maintain consistent performance regardless of the number of articles processed, as they are unaffected by fatigue.

#### 3.3.2 Analysis of high-performing coders’ results

To validate that our ﬁndings reﬂect the superior performance of LLMs rather than potential limitations of outsourced human coders, we conducted additional analysis focusing on high-performing coders. For each human coder, we calculated an aggregate performance score based on the proportion of tasks they completed correctly.20

20Recall that most outsourced human coders were tasked with reading three news articles and completing ﬁve tasks per article, totaling 15 tasks.

Using these scores, we replicated the analysis presented in Figure 1, restricting it to coders who achieved above-median performance (i.e., the top 50% of coders).21

The results, shown in Figure D2, reveal that while high-performing human coders achieved accuracy comparable to or occasionally exceeding GPT-3.5-turbo, their performance remained consistently below that of more advanced LLMs. This ﬁnding is particularly noteworthy given that our full sample of outsourced coders likely possesses higher capabilities than typical workers from popular crowdsourcing platforms. Thus, the analysis demonstrates that current LLMs perform at least as well as (in the case of GPT-3.5-turbo) or better than (for all other LLMs) the top performers in this already capable population.

### 3.4 Internal consistency

A desirable property of a coding strategy is its consistent reliability. Table 1 evaluates the internal consistency of each method by comparing paired responses. Recall that we obtained two responses per article from both human coders and each LLM. In this analysis, for each article and task, we treat the second response as the true label and compute the performance metrics described in Section 2.4, using the ﬁrst response as the prediction. Note that a coding strategy with high internal consistency should yield performance metrics approaching their theoretical maximum.

Table 1: Internal consistency by tagging strategy and task

T3 (Accuracy)

T5 (Accuracy)

T1 (Macro F1)

T2 (MAE)

T4 (Accuracy)

Coding strategy

Outsourced humans 0.672 0.786 0.581 0.367 0.352 GPT-3.5-turbo 0.985 0.048 0.971 0.924 0.938 GPT-4-turbo 0.995 0.024 0.976 0.971 0.967 Claude 3 Opus 0.999 0.014 1.000 0.995 0.990 Claude 3.5 Sonnet 0.997 0.010 1.000 0.986 0.986

Note: Each row represents a coding strategy and each column a task. Cell values measure consistency by comparing how well the ﬁrst draw replicates the value obtained in the second draw (which we treat as the true label), using each task’s performance metric. Higher consistency is indicated by values close to 1 for T1, T3, T4, and T5, and by values close to 0 for T2.

Table 1 shows that all LLMs demonstrate high internal consistency, aligned with their minimum temperature setting. While this consistency is not perfect, it substantially exceeds that of human coders.22

- 21It is worth noting that strong performance may reﬂect both the coder’s skill and the relative difﬁculty of their assigned articles. To ensure a fair comparison, we recalculated the LLMs’ performance considering the exact same articles analyzed by these high-performing coders.
- 22In Appendix C.2, we examine GPT-3.5-turbo’s temporal consistency by comparing responses generated


- at different times, as model behavior can change with updates. Our analysis reveals higher consistency between responses generated within this study than between these responses and those from Bermejo et al. (2023), indicating that even minimal temperature settings cannot prevent variations across model updates. Moreover, as shown in Table C5, these updates did not generally improve performance, with notable declines in T3, T4, and T5. These ﬁndings align with Chen et al. (2023), who documented performance declines in both GPT-3.5 and GPT-4 across several tasks between March and June 2023.


## 4 Conclusions

The analysis of text sources has become an important element in researchers’ toolbox. For example, analyzing patents and research articles sheds light on how innovation works (Tseng et al., 2007; Kelly et al., 2021; Galiani et al., 2024), open-ended surveys enhance our understanding of diverse phenomena (see Haaland et al., 2024, for a review), and news content can help us understand migration beliefs (Keita et al., 2024). In this paper, we show the potential of modern generative LLMs as a tool that greatly facilitates this type of analysis, benchmarking their performance against that of outsourced human coders.

We show that, even when outsourced coders’ performance is far better than that expected by pure chance, LLMs outperform them on every task analyzed. Additionally, we document several factors affecting both LLMs’ and outsourced human coders’ performance, demonstrating that even with difﬁcult and longer texts, LLMs maintain their superior performance. Notably, our results also show that LLMs’ answers demonstrate higher internal consistency than those of outsourced coders and that newest LLMs perform better than the best outsourced human coders.

These ﬁndings have important practical implications, suggesting that current NLP technology has reached a development stage that allows researchers without programming expertise or technical background to easily incorporate sophisticated text analysis into their work as a highly cost-effective alternative. The observed pattern of improved performance in newer LLM generations suggests this advantage will likely strengthen over time.

## Bibliography

Allcott, H. and Gentzkow, M. (2017). Social media and fake news in the 2016 election. Journal of economic perspectives, 31(2):211–236.

An, S., Ma, Z., Lin, Z., Zheng, N., and Lou, J.-G. (2024). Make your llm fully utilize the context. Ang, D. (2023). The birth of a nation: Media and racial hate. American Economic Review,

113(6):1424–1460. Angelico, C., Marcucci, J., Miccoli, M., and Quarta, F. (2022). Can we measure inﬂation expectations using twitter? Journal of Econometrics, 228(2):259–277. Aromi, J. D. (2020). Linking words in economic discourse: Implications for macroeconomic forecasts. International Journal of Forecasting, 36(4):1517–1530. Ash, E. and Hansen, S. (2023). Text algorithms in economics. Annual Review of Economics, 15(Volume 15, 2023):659–688. Ash, E., Hansen, S., and Muvdi, Y. (2024). Large language models in economics. CEPR Discussion Paper, (19479). https://cepr.org/publications/dp19479. Baker, S. R., Bloom, N., and Terry, S. J. (2024). Using disasters to estimate the impact of uncertainty. Review of Economic Studies, 91(2):720–747. Barbaglia, L., Consoli, S., and Manzan, S. (2023). Forecasting with economic news. Journal of Business & Economic Statistics, 41(3):708–719. Barberá, P., Boydstun, A. E., Linn, S., McMahon, R., and Nagler, J. (2021). Automated text classiﬁcation of news articles: A practical guide. Political Analysis, 29(1):1942. Barro, R. J. and Redlick, C. J. (2011). Macroeconomic effects from government purchases and taxes. The Quarterly Journal of Economics, 126(1):51–102.

- Benoit, K., Conway, D., Lauderdale, B. E., Laver, M., and Mikhaylov, S. (2016a). Crowdsourced text analysis: Reproducible and agile production of political data. American Political Science Review, 110(2):278–295.
- Benoit, K., Conway, D., Lauderdale, B. E., Laver, M., and Mikhaylov, S. (2016b). Crowdsourced text analysis: Reproducible and agile production of political data. American Political Science Review, 110(2):278–295.


Bermejo, V. J., Gago, A., Abad, J., and Carozzi, F. (2023). Government Turnover and External Financial Assistance.

Bertsch, A., Oh, A., Natu, S., Gangu, S., Black, A. W., and Strubell, E. (2022). Evaluating gender bias transfer from ﬁlm data. In Hardmeier, C., Basta, C., Costa-jussà, M. R., Stanovsky, G., and Gonen, H., editors, Proceedings of the 4th Workshop on Gender Bias in Natural Language Processing (GeBNLP), pages 235–243, Seattle, Washington. Association for Computational Linguistics.

Brady, W. J., Wills, J. A., Jost, J. T., Tucker, J. A., and Bavel, J. J. V. (2017). Emotion shapes the diffusion of moralized content in social networks. Proceedings of the National Academy of Sciences, 114(28):7313–7318.

Buehlmaier, M. M. and Whited, T. M. (2018). Are ﬁnancial constraints priced? evidence from textual analysis. The Review of Financial Studies, 31(7):2693–2728. Capozza, F., Haaland, I., Roth, C., and Wohlfart, J. (2022). Recent advances in studies of news consumption. Working Paper 10021, CESifo. Caprini, G. (2023). Does candidates media exposure affect vote shares? evidence from pope breaking news. Journal of Public Economics, 220:104847.

Chang, Y., Wang, X., Wang, J., Wu, Y., Yang, L., Zhu, K., Chen, H., Yi, X., Wang, C., Wang, Y., Ye, W., Zhang, Y., Chang, Y., Yu, P. S., Yang, Q., and Xie, X. (2024). A survey on evaluation of large language models. ACM Trans. Intell. Syst. Technol., 15(3).

Chen, L., Zaharia, M., and Zou, J. (2023). How is chatgpt’s behavior changing over time? Cloyne, J. (2013). Discretionary tax changes and the macroeconomy: new narrative evidence

from the united kingdom. American Economic Review, 103(4):1507–1528. Cloyne, J., Dimsdale, N., and Hürtgen, P. (2025). Are tax cuts contractionary at the zero lower bound? evidence from a century of data. Journal of Political Economy, 0(0):000–000. Couttenier, M., Hatte, S., Thoenig, M., and Vlachos, S. (2024). Anti-muslim voting and media coverage of immigrant crimes. Review of Economics and Statistics, 106(2):576–585. Davis, D. R., Dingel, J. I., Monras, J., and Morales, E. (2019). How segregated is urban consumption? Journal of Political Economy, 127(4):1684–1738. Demirel, U. D. (2021). The short-term effects of tax changes: The role of state dependence. Journal of Monetary Economics, 117:918–934.

Devlin, J., Chang, M.-W., Lee, K., and Toutanova, K. (2019). BERT: Pre-training of deep bidirectional transformers for language understanding. In Burstein, J., Doran, C., and Solorio, T., editors, Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers), pages 4171–4186, Minneapolis, Minnesota. Association for Computational Linguistics.

Djourelova, M. and Durante, R. (2022). Media attention and strategic timing in politics: Evidence from us presidential executive orders. American Journal of Political Science, 66(4):813–834.

Dougal, C., Engelberg, J., Garcia, D., and Parsons, C. A. (2012). Journalists and the stock market. The Review of Financial Studies, 25(3):639–679. Durante, R. and Zhuravskaya, E. (2018). Attack when the world is not watching? us news and the israeli-palestinian conﬂict. Journal of Political Economy, 126(3):1085–1133. Eisensee, T. and Strömberg, D. (2007). News droughts, news ﬂoods, and us disaster relief. The Quarterly Journal of Economics, 122(2):693–728. Ellison, G. (2002). The slowdown of the economics publishing process. Journal of political Economy, 110(5):947–993. Enikolopov, R., Petrova, M., and Sonin, K. (2018). Social media and corruption. American Economic Journal: Applied Economics, 10(1):150–174. Esposito, E., Rotesi, T., Saia, A., and Thoenig, M. (2023). Reconciliation narratives: The birth of a nation after the us civil war. American Economic Review, 113(6):1461–1504.

Etxaniz, J., Azkune, G., Soroa, A., Lacalle, O., and Artetxe, M. (2024). Do multilingual language models think better in English? In Duh, K., Gomez, H., and Bethard, S., editors, Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 2: Short Papers), pages 550–564, Mexico City, Mexico. Association for Computational Linguistics.

Ferrara, E. L., Chong, A., and Duryea, S. (2012). Soap operas and fertility: Evidence from brazil. American Economic Journal: Applied Economics, 4(4):1–31. Fryer Jr, R. G. (2019). An empirical analysis of racial differences in police use of force. Journal of Political Economy, 127(3):1210–1261.

Galiani, S., Gálvez, R. H., and Nachman, I. (2024). Specialization trends in economics research: A large-scale study using natural language processing and citation analysis. Economic Inquiry, Forthcoming.

Gálvez, R. H., Tiffenberg, V., and Altszyler, E. (2019). Half a century of stereotyping associ-

ations between gender and intellectual ability in ﬁlms. Sex Roles, 81(9):643–654. Garcia, D. (2013). Sentiment during recessions. The journal of ﬁnance, 68(3):1267–1300. García-Uribe, S. (2023). The effects of tax changes on economic activity: a narrative approach

to frequent anticipations. The Economic Journal, 133(650):706–727. García-Uribe, S., Mueller, H., and Sanz, C. (2024). Economic uncertainty and divisive politics: evidence from the dos españas. The Journal of Economic History, 84(1):40–73. Gentzkow, M., Kelly, B., and Taddy, M. (2019a). Text as data. Journal of Economic Literature, 57(3):53574.

Gentzkow, M., Petek, N., Shapiro, J. M., and Sinkinson, M. (2015). Do newspapers serve the state? incumbent party inﬂuence on the us press, 1869–1928. Journal of the European Economic Association, 13(1):29–61.

Gentzkow, M. and Shapiro, J. M. (2010). What drives media slant? evidence from u.s. daily newspapers. Econometrica, 78(1):35–71. Gentzkow, M., Shapiro, J. M., and Sinkinson, M. (2011). The effect of newspaper entry and exit on electoral politics. American Economic Review, 101(7):2980–3018. Gentzkow, M., Shapiro, J. M., and Sinkinson, M. (2014). Competition and ideological diversity: Historical evidence from us newspapers. American Economic Review, 104(10):3073–3114.

Gentzkow, M., Shapiro, J. M., and Taddy, M. (2019b). Measuring group differences in high-dimensional choices: method and application to congressional speech. Econometrica, 87(4):1307–1340.

Gilardi, F., Alizadeh, M., and Kubli, M. (2023). Chatgpt outperforms crowd workers for textannotation tasks. Proceedings of the National Academy of Sciences, 120(30):e2305016120.

González-Bailón, S., Lazer, D., Barberá, P., Zhang, M., Allcott, H., Brown, T., Crespo-Tenorio, A., Freelon, D., Gentzkow, M., Guess, A. M., et al. (2023). Asymmetric ideological segregation in exposure to political news on facebook. Science, 381(6656):392–398.

Graham, M., Milanowski, A. T., and Miller, J. (2012). Measuring and Promoting Inter-Rater Agreement of Teacher and Principal Performance Ratings. ERIC Clearinghouse, [S.l.]. Electronic resource.

Grimmer, J. and King, G. (2011). General purpose computer-assisted clustering and conceptualization. Proceedings of the National Academy of Sciences, 108(7):2643–2650. Guajardo, J., Leigh, D., and Pescatori, A. (2014). Expansionary austerity? international evidence. Journal of the European Economic Association, 12(4):949–968.

Guess, A. M., Malhotra, N., Pan, J., Barberá, P., Allcott, H., Brown, T., Crespo-Tenorio, A., Dimmery, D., Freelon, D., Gentzkow, M., et al. (2023a). How do social media feed algorithms affect attitudes and behavior in an election campaign? Science, 381(6656):398–404.

Guess, A. M., Malhotra, N., Pan, J., Barberá, P., Allcott, H., Brown, T., Crespo-Tenorio, A., Dimmery, D., Freelon, D., Gentzkow, M., et al. (2023b). Reshares on social media amplify political news but do not detectably affect beliefs or opinions. Science, 381(6656):404–408. Gunter, S., Riera-Crichton, D., Vegh, C. A., and Vuletin, G. (2021). Non-linear effects of tax changes on output: The role of the initial level of taxation. Journal of International Economics, 131:103450.

Haaland, I. K., Roth, C., Stantcheva, S., and Wohlfart, J. (2024). Measuring what is top of mind. Technical report, National Bureau of Economic Research.

Hauser, D., Paolacci, G., and Chandler, J. (2019). Common concerns with mturk as a participant pool: Evidence and solutions. In Handbook of research methods in consumer psychology, pages 319–337. Routledge.

Huang, F., Kwak, H., and An, J. (2023a). Is chatgpt better than human annotators? potential and limitations of chatgpt in explaining implicit hate speech. In Companion Proceedings of the ACM Web Conference 2023, WWW ’23 Companion, page 294297, New York, NY, USA. Association for Computing Machinery.

Huang, H., Tang, T., Zhang, D., Zhao, X., Song, T., Xia, Y., and Wei, F. (2023b). Not all languages are created equal in LLMs: Improving multilingual capability by cross-lingualthought prompting. In Bouamor, H., Pino, J., and Bali, K., editors, Findings of the Association for Computational Linguistics: EMNLP 2023, pages 12365–12394, Singapore. Association for Computational Linguistics.

Jalil, A. J. (2015). A new history of banking panics in the united states, 1825–1929: construction and implications. American Economic Journal: Macroeconomics, 7(3):295–330. Keita, S., Renault, T., and Valette, J. (2024). The usual suspects: Offender origin, media reporting and natives attitudes towards immigration. The Economic Journal, 134(657):322–362. Kelly, B., Papanikolaou, D., Seru, A., and Taddy, M. (2021). Measuring technological innovation over the long run. American Economic Review: Insights, 3(3):30320.

Kojima, T., Gu, S. S., Reid, M., Matsuo, Y., and Iwasawa, Y. (2022). Large language models are zero-shot reasoners. In Koyejo, S., Mohamed, S., Agarwal, A., Belgrave, D., Cho, K., and Oh, A., editors, Advances in Neural Information Processing Systems, volume 35, pages 22199–22213. Curran Associates, Inc.

Korinek, A. (2023). Generative ai for economic research: Use cases and implications for economists. Journal of Economic Literature, 61(4):12811317.

Kramer, A. D. I., Guillory, J. E., and Hancock, J. T. (2014). Experimental evidence of massivescale emotional contagion through social networks. Proceedings of the National Academy of Sciences, 111(24):8788–8790.

Larsen, V. H. and Thorsrud, L. A. (2019). The value of news for economic developments. Journal of Econometrics, 210(1):203–218. Annals Issue in Honor of John Geweke Complexity and Big Data in Economics and Finance: Recent Developments from a Bayesian Perspective.

Leiter, C., Zhang, R., Chen, Y., Belouadi, J., Larionov, D., Fresen, V., and Eger, S. (2024). Chatgpt: A meta-analysis after 2.5 months. Machine Learning with Applications, 16:100541. Lopez-Lira, A. and Tang, Y. (2024). Can chatgpt forecast stock price movements? return predictability and large language models. Martinez, V. R., Somandepalli, K., and Narayanan, S. (2022). Boys dont cry (or kiss or dance): A computational linguistic lens into gendered actions in ﬁlm. PLOS ONE, 17(12):1–23.

- Mertens, K. and Ravn, M. O. (2011). Understanding the aggregate effects of anticipated and unanticipated tax policy shocks. Review of Economic dynamics, 14(1):27–54.
- Mertens, K. and Ravn, M. O. (2012). Empirical evidence on the aggregate effects of anticipated and unanticipated us tax policy shocks. American Economic Journal: Economic Policy, 4(2):145–181.


- Mertens, K. and Ravn, M. O. (2013). The dynamic effects of personal and corporate income tax changes in the united states. American economic review, 103(4):1212–1247.
- Mertens, K. and Ravn, M. O. (2014). A reconciliation of svar and narrative estimates of tax multipliers. Journal of Monetary Economics, 68:S1–S19.


Mu, Y., Wu, B. P., Thorne, W., Robinson, A., Aletras, N., Scarton, C., Bontcheva, K., and Song, X. (2024). Navigating prompt complexity for zero-shot classiﬁcation: A study of large language models in computational social science. In Calzolari, N., Kan, M.-Y., Hoste, V., Lenci, A., Sakti, S., and Xue, N., editors, Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024), pages 12074–12086, Torino, Italia. ELRA and ICCL.

Naef, A. (2024). Blowing against the wind? a narrative approach to central bank foreign exchange intervention. Journal of International Money and Finance, 146:103129. Nguyen, A. D., Onnis, L., and Rossi, R. (2021). The macroeconomic effects of income and consumption tax changes. American Economic Journal: Economic Policy, 13(2):439–466.

Quinn, K. M., Monroe, B. L., Colaresi, M., Crespin, M. H., and Radev, D. R. (2010). How to analyze political attention with minimal assumptions and costs. American Journal of Political Science, 54(1):209–228.

Ramey, V. A. (2011). Identifying government spending shocks: It’s all in the timing. The Quarterly Journal of Economics, 126(1):1–50.

Ramey, V. A. and Shapiro, M. D. (1998). Costly capital reallocation and the effects of government spending. In Carnegie-Rochester conference series on public policy, volume 48, pages 145–194. Elsevier.

Rathje, S., Mirea, D.-M., Sucholutsky, I., Marjieh, R., Robertson, C. E., and Bavel, J. J. V. (2024). Gpt is an effective tool for multilingual psychological text analysis. Proceedings of the National Academy of Sciences, 121(34):e2308950121.

Romer, C. D. and Romer, D. H. (1989). Does monetary policy matter? a new test in the spirit of friedman and schwartz. NBER macroeconomics annual, 4:121–170. Romer, C. D. and Romer, D. H. (2010). The macroeconomic effects of tax changes: estimates based on a new measure of ﬁscal shocks. American economic review, 100(3):763–801.

Shapiro, A. H. and Wilson, D. J. (2022). Taking the fed at its word: A new approach to estimating central bank objectives using text analysis. The Review of Economic Studies, 89(5):2768–2805.

Simchon, A., Brady, W. J., and Van˘aBavel, J. J. (2022). Troll and divide: the language of online polarization. PNAS Nexus, 1(1):pgac019. Snyder Jr, J. M. and Strömberg, D. (2010). Press coverage and political accountability. Journal of political Economy, 118(2):355–408.

Song, H., Tolochko, P., Eberl, J.-M., Eisele, O., Greussing, E., Heidenreich, T., Lind, F., Galyga, S., and Boomgaarden, H. G. (2020). In validations we trust? the impact of imperfect human annotations as a gold standard on the quality of validation of automated content analysis. Political Communication, 37(4):550–572.

Tetlock, P. C. (2007). Giving content to investor sentiment: The role of media in the stock market. The Journal of ﬁnance, 62(3):1139–1168. Tseng, Y.-H., Lin, C.-J., and Lin, Y.-I. (2007). Text mining techniques for patent analysis. Information Processing & Management, 43(5):1216–1247. Patent Processing.

Vos, D. and Aelst, P. V. (2018). Does the political system determine media visibility of politicians? a comparative analysis of political functions in the news in sixteen countries. Political Communication, 35(3):371–392.

Zhang, L. (2016). reﬂexive expectations in eu–china relations: a media analysis approach. JCMS: Journal of Common Market Studies, 54(2):463–479.

Ziems, C., Held, W., Shaikh, O., Chen, J., Zhang, Z., and Yang, D. (2024). Can large language models transform computational social science? Computational Linguistics, 50(1):237–291.

## Appendix A. News dataset

### A.1 Selection of news in Bermejo et al. (2023)

For the analysis in Bermejo et al. (2023), the authors downloaded a subset of news from Factiva. In particular, any news articles in Catalan or Spanish fulﬁlling the two following criteria:

- 1. News published in Spain during the period 2011-2013.
- 2. News containing references to any Spanish local government along with references to the SPP or to any adjustment plan. This includes news containing the following terms (in Spanish):


- • Terms related to local governments: “munici*” or “ayuntamiento” or “alcalde*”.23
- • Terms related to the SPP or any ﬁscal consolidation program: “plan de pagos” or “plan de proveedores” or “mecanismo de pago” or “plan de pago a proveedores” or “programa de consolidación ﬁscal” or “plan de consolidación ﬁscal” or “plan de ajuste”.


This yielded a total of 2,307 articles in 2011, 14,154 articles in 2012 and 7,673 in 2013.24

### A.2 News articles example

This is an example of the news articles that we analyze, ﬁrst in Spanish and then English.

#### Original article in Qualtrics

Here we provide the original article in Spanish in the same format that it is displayed to ESADE students in Qualtrics.

23The asterisk (*) is used to keep the root of a word and allows for any ending of the word. 24Later, in their analysis of the news content, Bermejo et al. (2023) restrict their attention only to articles

published in 2012 and 2013.

22/10/24, 12:05 Qualtrics Survey | Qualtrics Experience Management

![image 1](Bermejo et al._2024_LLMs Outperform Outsourced Human Coders on Complex Textual Analysis_images/imageFile1.png)

##### El varapalo del TSJA a Sevilla Global costará unos 800.000 € a las arcas públicas; Condena a pagar los salarios de tramitación de 43 despedidos

Sevilla - El varapalo del Tribunal Superior de Justicia de Andalucía (TSJA) a la empresa municipal Sevilla Global costará unos 800.000 euros a las arcas municipales. Ésta es la cifra que el Ayuntamiento de Sevilla tendrá que pagar a los 43 trabajadores afectados por un expediente de regulación de empleo (ERE) que el Alto Tribunal ha anulado en una sentencia en la que ordena la reincorporación a sus puestos de trabajo y el pago de los salarios de tramitación desde que se hicieron efectivos los despidos, el 13 de noviembre de 2012.El gobierno municipal, a priori, no prevé recurrir este fallo judicial, aunque sí tiene claro que seguirá adelante con la disolución y liquidación de Sevilla Global.

Para ello, ha solicitado a la Sala de lo Social del TSJA una "aclaración" sobre determinados aspectos de la sentencia que le permita aplicar la fórmula correcta para despedir a los trabajadores de la empresa.El delegado y responsable de Sevilla Global, Gregorio Serrano, explicó ayer que con esta "aclaración" pretende que el Alto Tribunal determine si el Ayuntamiento hispalense, declarado como "empleador real" en la sentencia, debe participar en la negociación del ERE "con un concejal o a través de la asesoría jurídica". Serrano defendió que el TSJA "da la razón a la empresa en cuanto a la liquidación", con lo que insistió en que van a "seguir adelante con la disolución de Sevilla Global con toda seguridad".Si, ﬁnalmente, el gobierno municipal descarta recurrir el fallo judicial, tendrá que acatar la condena e incorporar a los 43 trabajadores y abonarles los salarios de tramitación de los últimos seis meses. Este nuevo gasto para las arcas municipales ascendería a unos 800.000 euros aproximadamente, algo menos de las mitad del presupuesto de 2012 –el último antes de iniciar el proceso de liquidación– destinado a personal (2.381.543 euros).Sevilla Global se encuentra en proceso de liquidación al exceder sus pérdidas de la mitad del capital social, una situación ﬁnanciera que ha obligado al Ayuntamiento hispalense a disolverla al acogerse al plan de pago a proveedores impulsado por el Gobierno central. Una decisión que, no obstante, aliviará las cuentas municipales, ya que su cierre supondrá un ahorro anual de más de 3,4 millones de euros.Así lo estima la delegación de Hacienda y Administración Pública y así está recogido en el plan de ajuste. De este modo, y en cifras globales, Juan Ignacio Zoido habrá ahorrado al ﬁnal de su primer mandato más de 10,2 millones con el cierre de Sevilla Global.La sentencia del TSJA no pone en duda la necesidad de liquidar esta empresa municipal. De hecho, la caliﬁca como una entidad "artiﬁciosamente creada para realizar actividades municipales sin control" y precisa que desde el año 2000 ha recibido 30,5 millones en transferencias realizadas por el Ayuntamiento.Y es que, como ya publicó este periódico, IU triplicó en los últimos tres años el número de empleados de Sevilla Global. De los 23 trabajadores que tenía en 2003 se pasó a 68 en 2010, con un coste de más de tres millones de euros. La mayor parte de estas contrataciones se realizaron en el último mandato, entre 2007 y 2009, cuando se pasó de 28 empleados a 68, y los gastos de la plantilla se triplicaron.

https://esade.eu.qualtrics.com/jfe/preview/previewId/1efc8d06-3751-400c-b8e8-b80229898f10/SV_8p5JXIil0bq60MS?Q_CHL=preview&Q_Surve… 1/3

#### English translation of the selected article

This is an English translation of the original article:

The TSJA’s blow to Sevilla Global will cost e800,000 in public funds; It ordered to pay salaries during dismissal processing for 43 laid-off employees

Sevilla − The blow dealt by the Superior Court of Justice of Andalusia (TSJA) to the municipal company Sevilla Global will cost local public funds e800,000. This is the amount that Sevilla’s City Council will have to pay to the 43 workers affected by a collective dismissal regulation process (ERE) that the Superior Court nulliﬁed in a ruling requiring the municipality to reinstate them to their positions and pay them for the time they were out of work in November 13 of 2012. The municipal government has announced that it will not appeal the ruling, clarifying that it will proceed with the dissolution and liquidation of Sevilla Global.

For this purpose, it has requested that the Social Chamber of the TSJA issue a "clariﬁcation" on speciﬁc aspects of the ruling that would allow the council to use the correct approach to dismiss these employees after reinstating them. The delegate and Head of Sevilla Global, Gregorio Serrano, explained that this "clariﬁcation" aims for the Superior Court to determine if the Town Hall, declared as the "actual employer" in the ruling, may initiate a new collective dismissal process to negotiate with each employee or through judicial channels. Serrano argued that the TSJA "supports the company regarding the liquidation," and thus emphasized that they are going to "proceed with the dissolution of Sevilla Global with full assurance." If, ultimately, the municipal government decides not to appeal the ruling, it will have to comply with the judgment and reinstate the 43 employees, paying them processing wages for the past six months. This new expense for municipal funds would amount to approximately e800,000, just under half of the 2012 budget − the last before starting the liquidation process − allocated to personnel (e2,381,543). Sevilla Global is currently in the process of liquidation after surpassing losses of more than half its share capital, a ﬁnancial situation that has forced the Sevilla Town Hall to dissolve it as part of the supplier payment plan promoted by the central government. This decision will, however, relieve the municipal accounts, as its closure will result in an annual savings of more than e3.4 million. This is the estimation of the Public Finance and Administration Department, and it is recorded in the adjustment plan. In overall terms, Juan Ignacio Zoido will have saved over e10.2 million by the end of his ﬁrst term with the closure of Sevilla Global. The TSJA ruling does not question the necessity of liquidating this municipal company. In fact, it describes it as an entity "artiﬁcially created to carry out municipal activities without oversight" and notes that since 2000 it has received e30.5 million in transfers from the Municipality. As previously reported by this newspaper, IU tripled the number of employees at Sevilla Global over the past three years. From the 23 workers it had in 2003, the company grew to 68 in 2010, with costs exceeding three million euros. Most of these hires took place in the last term, between 2007 and 2009, when the workforce increased from 28 to 68 employees, and staff expenses tripled.

## Appendix B. Labelling tasks

### B.1 Full task description

Bellow we provide the entire original tasks (in English):

- • T1: List all the names of municipalities mentioned in this news separated by a comma. If no municipalities are mentioned in the news, respond with “0”. If you are not sure, reply “I am not sure”.
- • T2: How many names of municipalities are mentioned in the news? If you are not sure, reply “I am not sure”.
- • T3: In this news, is the municipal government criticized? If you are not sure, reply “I am not sure”.
- • T4: In this news, who issues the criticism? Please select one of the following alternatives:

1. The criticism was made by an opposition councilor. 2. The criticism was made by a councilor from the ruling party. 3. The criticism was made by the mayor. 4. The criticism was made by the Popular Party (PP). 5. The criticism was made by the Socialist Party (PSOE). 6. There are no critics to the municipal management. 7. The answer does not ﬁt into any of the previous categories. 8. I am not sure.

- • T5: In this news, who is the criticism directed at? Please select one of the following alternatives: 1. The criticism is directed at the current municipal government. 2. The criticism is directed at the previous municipal government. 3. The criticism is directed at the national government. 4. The criticism is directed at the municipal opposition. 5. The criticism is directed at the Popular Party (PP). 6. The criticism is directed at the Socialist Party (PSOE). 7. There are no critics to the municipal management. 8. The answer does not ﬁt into any of the previous categories. 9. I am not sure.


### B.2 Gold standard labels

The average number of municipalities named in the articles, as per the gold standard labels, was 1.95, with a standard deviation of 2.95, a minimum of 0, a maximum of 24 and a median of 1 (T1 and T2). The most frequently mentioned municipality is Madrid (n = 35), followed by Sevilla (n = 14), Málaga (n = 10), and Valencia (n = 8). A total of 183 municipalities are mentioned in only one article. Additionally, 26 articles do not name any municipality, which can occur, for example, when an article refers to the Province of Granada but not the city itself.

A 41.9% of articles contain criticism to the municipal management (T3). In T4, answers are divided as follows: 17.62% of the articles contain criticism made by an opposition councilor, 4.29% contain criticisms made by a councilor from the ruling party, 15.24% contain criticisms made by the mayor, 8.57% contain criticisms made by the Popular Party (PP), 12.38% contain criticisms made by the Socialist Party (PSOE), in 46.67%

there are no criticisms of any kind and in 13.81% the answer does not ﬁt into any of the previous categories. We never marked an answer to T4 with a “not sure.” In T5, answers are divided as follows: In 29.05% of the articles the criticism is directed at the current municipal government, in 14.76% of the articles it is directed at the previous municipal government, in 4.76% of the articles it is directed at the national government, in 4.29% of the articles it is directed at the municipal opposition, in 9.52% of the articles it is directed at the PP, in 6.19% of the articles the criticism is directed at the PSOE, in 46.67% there are no criticisms of any kind and in 6.67% of the articles the answer does not ﬁt into any of the previous categories. Like in T4, we never marked an answer as “not sure” in the gold standard labels.

Notice that while the number of articles containing criticisms in T3 is 41.9%, the number of articles containing criticisms is 53.33% in T4 and T5. This apparent contradiction is explained because T3 literally refers to criticism targeted at the municipal government, while T4 and T5 inquire about the origin/destination of any criticism that is featured in the news (including for example critics directed to the national government). Likewise, in T4 and T5 the sum of the categories could be above 100%, as categories are not mutually exclusive. For example, the same politician from the opposition might be referred in different parts of the article as a member of the opposition or as a councilor from PP. In such cases, we marked both alternatives as correct in the Gold Standard.

### B.3 Example of an API call

Below, we provide the template we used for the API calls to the different models analyzed in this study (in Spanish). These API calls ask the different LLMs the same questions we describe in Appendix B.1.

Usted es un asistente de investigación. Su trabajo es leer una noticia y responder preguntas sobre su contenido. Dé su respuesta en un diccionario de Python estructurado de la siguiente manera: Q1: respuesta a la pregunta 1, Q2: respuesta a la pregunta 2, ... No agregue ninguna explicación adicional a su respuesta. No deje ninguna pregunta sin responder. <News> Here the news text is inserted </News>

- Q1: Enumere todos los nombres de municipios mencionados en esta noticia separados por una coma. Si en la noticia no se menciona ningún municipio, responda con “0”. Si no está seguro, responda con “99”.
- Q2: ¿Cuántos nombres de municipios están mencionados en la noticia? Si no esta seguro, responda con “99”.
- Q3: En esta noticia, ¿se critica la gestión municipal? Si la respuesta es aﬁrmativa, responda con “1”. Si la respuesta es negativa, responda con “0”. Si no esta seguro, responda con “99”.


- Q4: En esta noticia, ¿quién emite la crítica? Por favor, seleccione una de las siguientes alternativas: Si la critica fue hecha por un concejal de la oposición, responda con “1”. Si la crítica fue hecha por un concejal del partido del gobierno, responde con “2”. Si la crítica fue hecha por el alcalde, responda con “3”. Si la crítica fue hecha por el Partido Popular (PP), responda con “4”. Si la critica fue hecha por el Partido Socialista (PSOE), responda con “5”. Si en la noticia no hay críticas a la gestión municipal, responda con “0”. Si su respuesta no encaja en ninguna de las categorías anteriores, responda “98”. Si no esta seguro, responda con “99”.
- Q5: En esta noticia, ¿a quién van dirigidas las críticas? Por favor, seleccione una de las siguientes alternativas: Si se critica al gobierno municipal actual, responda con “1”. Si se critica al gobierno municipal anterior, responda con “2”. Si se critica al gobierno nacional, responda con “3”. Si se critica a la oposición municipal, responda con “4”. Si se critica al Partido Popular (PP), responda con “5”. Si se critica al Partido Socialista (PSOE), responda con “6”. Si no hay críticas, responda con “0”. Si su respuesta no encaja en ninguna de las categorías anteriores, responda “98”. Si no esta seguro, responda con “99”.


## Appendix C. Additional empirical analysis

### C.1 Regression analysis

Here, we present three regressions that further explore the data. First, we run the OLS featured in Equation 1 :

Scorem,i = α+∑βmDm +γ Xi +ui,m (1)

where Scorem,i represents method m’s score on article i, Dm is a dummy variable equal to 1 for method m (with outsourced human coders as the omitted category), and Xi includes dummies for long and difﬁcult articles. Standard errors are clustered at the article level.

The results in Table C1 show that LLMs outperform outsourced human coders in all tasks, with the exception of GPT-3.5-turbo in T4. Moreover, when considering the proportion of news articles where all tasks are performed correctly (column 6), LLMs demonstrate superior performance compared to outsourced human coders, except for GPT-3.5-turbo. The p-values at the bottom of the table test for equality between different models’ coefﬁcients. We ﬁnd that GPT-4-turbo outperforms its predecessor (GPT3.5-turbo) in all tasks except T1, Claude 3 Opus outperforms GPT-3.5-turbo in all tasks except T1, and GPT-4-turbo and Claude 3.5 Sonnet perform similarly across all tasks except T1, where Sonnet demonstrates superior performance.

In Equation 2, we further explore GPT-3.5-turbo’s performance in T4, the only task where it does not outperform outsourced human coders. We estimate the following OLS speciﬁcation:

Table C1: Task score across methods

(1) (2) (3) (4) (5) (6)

T1 (F1) T2 (MAE) T3 (Acc) T4 (Acc) T5 (Acc) All (Prop) GPT-3.5-turbo 0.0921*** -0.188** 0.0643** 0.0238 0.0881** 0.0381

(0.0249) (0.0759) (0.0320) (0.0371) (0.0350) (0.0301) GPT-4-turbo 0.114*** -0.305*** 0.186*** 0.267*** 0.264*** 0.329*** (0.0223) (0.0703) (0.0274) (0.0330) (0.0328) (0.0331) Claude 3 Opus 0.106*** -0.305*** 0.183*** 0.240*** 0.240*** 0.255*** (0.0209) (0.0682) (0.0263) (0.0332) (0.0310) (0.0316) Claude 3.5 Sonnet 0.164*** -0.336*** 0.207*** 0.274*** 0.283*** 0.324*** (0.0209) (0.0746) (0.0258) (0.0333) (0.0315) (0.0312) Difﬁcult -0.102** 0.724*** -0.0409 -0.0953 -0.0917 -0.153***

(0.0436) (0.162) (0.0707) (0.0670) (0.0651) (0.0476) Long 0.0167 0.541*** -0.0916 -0.149* -0.179** -0.166**

(0.0462) (0.204) (0.0787) (0.0840) (0.0769) (0.0734) Constant 0.731*** 0.446*** 0.667*** 0.525*** 0.549*** 0.271***

(0.0252) (0.0584) (0.0265) (0.0288) (0.0290) (0.0296) Observations 2,100 2,100 2,100 2,100 2,100 2,100

p-val: βGPT−3.5−turbo = βGPT−4−turbo .235 .082 0 0 0 0 p-val: βGPT−3.5−turbo = βClaude 3 Opus .409 .062 0 0 0 0 p-val: βGPT−4−turbo = βClaude 3.5 Sonnet .016 .39 .266 .711 .46 .858

Note: Each column shows the OLS regression of the score in one task on a set of dummy variable indicators that denote the different labeling methods (outsourced human coders is the omitted category). The regression also includes dummy variables controlling for difﬁcult news and for news with a length above the 90th percentile. Errors are clustered at the article level. For each coefﬁcient, *, **, and *** represent 10%, 5%, and 1% signiﬁcance levels, respectively. At the bottom of the table we show the p-value for different tests of equality of coefﬁcients.

Scorei,m = α + βDm + γ1Dif ficulti + γ2Longi + θDm · Dif ficulti + ui,m (2)

where Dm equals 1 for GPT-3.5-turbo responses and 0 for outsourced human coders’ responses in Qualtrics. Standard errors are clustered at the article level.

Table C2: GPT-3.5-turbo performance by news difﬁculty

(1) (2) T4 (Acu) All (Prop) GPT-3.5-turbo -0.00282 0.00360

(0.0414) (0.0391) Difﬁcult -0.173*** -0.122***

(0.0618) (0.0389) Long -0.0444 -0.0802

(0.0796) (0.0588) GPT-3.5-turbo#Difﬁcult 0.169* 0.102*

(0.0871) (0.0594) Constant 0.527*** 0.252***

(0.0306) (0.0303) Observations 840 840

Note: The ﬁrst column shows the OLS regression of the score in T4 on a dummy variable taking value one when we use GPT-3.5-turbo and value zero when we use outsourced human coders, on a dummy taking value one for difﬁcult news and value zero for the rest, and on the interaction of these two dummies. We also include a dummy variable that controls for articles whose length is above the 90th percentile. The second column shows the results of the same regression changing the dependent variable for a dummy that takes value one when all the tasks in an article where performed correctly and value zero otherwise. Errors are clustered at the article level. *, **, and *** represent 10%, 5%, and 1% signiﬁcance levels, respectively.

Table C2 shows the results. We ﬁnd no performance differences in T4 for non-difﬁcult articles, but the interaction term reveals that GPT-3.5-turbo outperforms outsourced human coders when analyzing difﬁcult articles. This result conﬁrms that every LLM, also GPT-3.5-turbo, is superior to outsourced human coders in every task, at least in some relevant dimension.

Finally, in Equation 3, we analyze how the order in which outsourced human coders read the articles affects their performance. We estimate the following OLS speciﬁcation:

Scorei = α + β1Secondi + β2Thirdi + γ Xi + ui (3)

where Secondi and Thirdi are dummy variables indicating whether the article was read second or third, respectively, and Xi includes controls for article length and difﬁculty. Standard errors are clustered at the participant level. In column (2), we additionally include participant ﬁxed effects.

Table C3: Outsourced human coders performance by news order

(1) (2) All (Prop) All (Prop) Second Article 0.159*** 0.149***

(0.0528) (0.0486) Third Article -0.0127 -0.0250

(0.0431) (0.0459) Difﬁcult -0.121*** -0.122**

(0.0380) (0.0499) Long -0.107** -0.114*

(0.0504) (0.0671)

Observations 420 420 Participant FE NO YES

Note: OLS of a dummy variable that takes value one when all the tasks in an article are done correctly by an outsourced human coder, on a dummy variable that takes value one when that article was read in the second place and value zero otherwise, and a on dummy variable that takes value one when that article war read in the third place and value zero otherwise (ﬁrst place is the omitted category). We also include a dummy variable that controls for articles whose length is above the 90th percentile and a dummy that controls for difﬁcult articles. The second column includes ﬁxed effects for each outsource human coder (who reads three articles). Errors are clustered at the article level. *, **, and *** represent 10%, 5%, and 1% signiﬁcance levels, respectively.

The results in Table C3 indicate that participants perform better on the second article, displaying a U-shaped pattern that suggests an interplay between learning and fatigue effects. This pattern remains robust when including participant ﬁxed effects.

### C.2 Intertemporal consistency

Here, we examine the intertemporal consistency of GPT-3.5-turbo by comparing its answers as time passes by. Concretely, we ﬁrst evaluate the internal consistency of the two sets of answers generated for this paper (recall that for each news article we obtained two answers). To do this, we treat the second answer as the ground truth and the ﬁrst answer as the predicted value, with the expectation that a tagging strategy

exhibiting high internal consistency will yield performance metrics close to their theoretical maximum (note that these values are identical to the ones shown in the second row of Table 1). Subsequently, we assess the consistency when using the responses from Bermejo et al. (2023) as the predicted values while maintaining the second answer obtained for this article as the ground truth. The resulting metrics are displayed in Table C4, where we refer to the consistency metrics between the two answers obtained for this study as “October 2023” and to those using the responses from Bermejo et al. (2023) as “April 2023.”

Table C4: Intertemporal consistency of GPT-3.5-turbo

Task October 2023 April 2024

- T1 (Macro F1) 0.898 0.985
- T2 (MAE) 0.262 0.048
- T3 (Accuracy) 0.857 0.971
- T4 (Accuracy) 0.652 0.924
- T5 (Accuracy) 0.643 0.938


Note: Each row represents contemporaneous answers from different runs at the same point in time, and each column corresponds to a task. Cell values measure consistency by evaluating how well the ﬁrst answer replicates the value obtained in the second answer (treated as the true label) according to each tasks performance metric. Higher consistency is indicated by values close to 1 for T1, T3, T4, and T5, and by values close to 0 for T2. Intertemporal consistency metrics assess this performance within GPT3.5-turbo, with the ﬁrst set of metrics reﬂecting answers generated in October 2023 and the second set representing answers from April 2024.

Table 1 demonstrates that consistency is higher among contemporaneous answer sets than between the answers from Bermejo et al. (2023) and the second set generated for this study. This suggests that even when an LLM’s temperature is set to its lowest value, responses may still vary signiﬁcantly due to model updates. Considering this, one might question whether such variability necessarily corresponds to improved performance in newer versions of the LLM. To explore this, Table C5 presents the performance metrics derived from the answers in Bermejo et al. (2023) (labeled as “October 2023”) and those generated for this study (labeled as “April 2024”). Note that the latter correspond to those shown in Figure 1.

Notably, Table C5 shows mixed results, which does not clearly point toward improved performance in newer versions of the LLM.25

25In fact, in three out of ﬁve tasks, including T4 and T5 (the ones deemed as more challenging), the point estimate for the average performance dropped from October 2023 to April 2024, translating into a drop in the proportion of articles answered entirely correctly. These results align with the ﬁndings reported in Chen et al. (2023), which document a decline in ChatGPT’s performance across several tasks between March 2023 and June 2023.

Table C5: GPT-3.5-turbo performance across time

Task October 2023 April 2024

- T1 (Macro F1) 0.782 0.808
- T2 (MAE) 0.533 0.443
- T3 (Accuracy) 0.771 0.719
- T4 (Accuracy) 0.567 0.519
- T5 (Accuracy) 0.652 0.605 All correct (Proportion) 0.271 0.240


Note: Each row represents contemporaneous answers from different runs at the same point in time, and each column corresponds to a task. Cell values measure consistency by evaluating how well the ﬁrst answer replicates the value obtained in the second answer (treated as the true label) according to each tasks performance metric. Higher consistency is indicated by values close to 1 for T1, T3, T4, and T5, and by values close to 0 for T2. Intertemporal consistency metrics assess this performance within GPT3.5-turbo, with the ﬁrst set of metrics reﬂecting answers generated in October 2023 and the second set representing answers from April 2024.

## Appendix D. Additional tables & ﬁgures

Table D1: Overall performance, across tasks and coding strategies

|Coding Strategy<br><br>|T1 (Macro F1)|T2 (MAE)|T3 (Acc)<br><br>|T4 (Acc)|T5 (Acc)<br><br>|All (Prop)|
|---|---|---|---|---|---|---|
|Outsourced humans GPT-3.5-turbo GPT-4-turbo Claude 3 Opus Claude 3.5 Sonnet|0.716 0.808 0.830 0.821 0.880<br><br>|0.631 0.443 0.326 0.326 0.295<br><br>|0.655 0.719 0.840 0.838 0.862|0.495 0.519 0.762 0.736 0.769<br><br>|0.517 0.605 0.781 0.757 0.800<br><br>|0.202 0.240 0.531 0.457 0.526|


Note: The table displays the overall performance across all tasks and coding strategies. For T1, it shows the Macro F1 score; for T2, the Mean Absolute Error (MAE); and for T3, T4, and T5, it shows the accuracy. For T2, a lower number denotes better performance, while for the remaining tasks, higher numbers indicate better performance. The “All (Prop)” column indicates the proportion of news articles for which all tasks were completed entirely correctly, broken down by coding strategy.

Table D2: Performance by article difﬁculty, across tasks and coding strategies

|Coding Strategy<br><br>|T1 (Macro F1)|T2 (MAE)|T3 (Acc)<br><br>|T4 (Acc)|T5 (Acc)<br><br>|All (Prop)|
|---|---|---|---|---|---|---|
|Regular| | | | | | |
|Outsourced humans GPT-3.5-turbo GPT-4-turbo Claude 3 Opus Claude 3.5 Sonnet<br><br>|0.732 0.824 0.850 0.839 0.891|0.401 0.282 0.230 0.230 0.189<br><br>|0.672 0.708 0.839 0.849 0.865<br><br>|0.523 0.520 0.768 0.746 0.802|0.534 0.619 0.797 0.774 0.822<br><br>|0.245 0.248 0.586 0.532 0.615|
|Difﬁcult| | | | | | |
|Outsourced humans GPT-3.5-turbo GPT-4-turbo Claude 3 Opus Claude 3.5 Sonnet<br><br>|0.633 0.727 0.724 0.728 0.826|1.671 1.171 0.763 0.763 0.776<br><br>|0.472 0.833 0.861 0.722 0.833|0.348 0.515 0.727 0.682 0.591<br><br>|0.424 0.530 0.697 0.667 0.682<br><br>|0.120 0.225 0.423 0.310 0.352|


Note: The table displays the overall performance across all tasks and coding strategies classiﬁed by task difﬁculty. For T1, it shows the Macro F1 score; for T2, the Mean Absolute Error (MAE); and for T3, T4, and T5, it shows the accuracy. For T2, a lower number denotes better performance, while for the remaining tasks, higher numbers indicate better performance. The “All (Prop)” column indicates the proportion of news articles for which all tasks were completed entirely correctly, broken down by coding strategy.

Table D3: Performance by article length, across tasks and coding strategies

|Coding Strategy<br><br>|T1 (Macro F1)<br><br>|T2 (MAE)|T3 (Acc)<br><br>|T4 (Acc)|T5 (Acc)<br><br>|All (Prop)|
|---|---|---|---|---|---|---|
|Regular| | | | | | |
|Outsourced humans GPT-3.5-turbo GPT-4-turbo Claude 3 Opus Claude 3.5 Sonnet|0.715 0.816 0.825 0.816 0.884<br><br>|0.513 0.349 0.288 0.294 0.265<br><br>|0.661 0.725 0.849 0.847 0.878|0.508 0.516 0.788 0.759 0.786<br><br>|0.537 0.622 0.810 0.772 0.815|0.214 0.246 0.558 0.476 0.553<br><br>|
|Long| | | | | | |
|Outsourced humans GPT-3.5-turbo GPT-4-turbo Claude 3 Opus Claude 3.5 Sonnet<br><br>|0.722 0.732 0.871 0.867 0.851|1.690 1.286 0.667 0.619 0.571<br><br>|0.595 0.667 0.762 0.762 0.714<br><br>|0.381 0.548 0.524 0.524 0.619|0.333 0.452 0.524 0.619 0.667<br><br>|0.095 0.190 0.286 0.286 0.286|


Note: The table displays the overall performance across all tasks and coding strategies classiﬁed by article length. For T1, it shows the Macro F1 score; for T2, the Mean Absolute Error (MAE); and for T3, T4, and T5, it shows the accuracy. For T2, a lower number denotes better performance, while for the remaining tasks, higher numbers indicate better performance. The “All (Prop)” column indicates the proportion of news articles for which all tasks were completed entirely correctly, broken down by coding strategy.

Table D4: Detailed results of permutation tests

|Task|Observed value<br><br>|Null mean|Null 2.5th perc<br><br>|Null 97.5th perc|
|---|---|---|---|---|
|T1 (Macro F1)<br>T2 (MAE)<br>T3 (Acc)<br>T4 (Acc)<br>T5 (Acc)<br>|0.716 0.631 0.655 0.495 0.517<br><br>|0.042 1.932 0.464 0.228 0.260<br><br>|0.026 1.821 0.419 0.193 0.224<br><br>|0.059 2.026 0.510 0.262 0.295|


Note: The table displays task performance for each metric alongside null statistics obtained from a permutation test. For T1, it shows the Macro F1 score; for T2, the Mean Absolute Error (MAE); and for T3, T4, and T5, it shows the accuracy. For T2, a lower number denotes better performance, while for the remaining tasks, higher numbers indicate better performance.accuracy.

Table D5: Human coders’ performance by task order

|Coding Strategy|T1 (Macro F1)<br><br>|T2 (MAE)|T3 (Acc)<br><br>|T4 (Acc)|T5 (Acc)<br><br>|All (Prop)|
|---|---|---|---|---|---|---|
|Overall First article Second article Third article<br><br>|0.716 0.778 0.776 0.602<br><br>|0.631 0.609 0.518 0.760<br><br>|0.655 0.632 0.674 0.658|0.495 0.459 0.582 0.445<br><br>|0.517 0.444 0.624 0.479<br><br>|0.202 0.150 0.312 0.144|


Note: The table shows the performance trends across tasks based on the order in which participants reviewed the news articles. For T1, it shows the Macro F1 score; for T2, the Mean Absolute Error (MAE); and for T3, T4, and T5, it shows the accuracy. For T2, a lower number denotes better performance, while for the remaining tasks, higher numbers indicate better performance.

Figure D1: ESADE recruiting platform

![image 2](Bermejo et al._2024_LLMs Outperform Outsourced Human Coders on Complex Textual Analysis_images/imageFile2.png)

Note: Screenshot of the ESADE Decision Lab Participation System, where we recruited our subject sample.

Figure D2: Overall performance comparison between LLMs and high-performing human coders

T1: Cities names (Macro F1)

T2: Named cities count (MAE)

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


| | | | | |
|---|---|---|---|---|
| | | | | |


Outsourced humans

GPT-3.5-turbo

GPT-4-turbo

Claude 3 Opus

Claude 3.5 Sonnet

0.0 0.2 0.4 0.6 0.8 1.0

0.0 0.2 0.4 0.6 0.8 1.0

T3: Presence of criticism (Accuracy)

T4: Source of criticism (Accuracy)

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


| | | | | |
|---|---|---|---|---|
| | | | | |


Outsourced humans

GPT-3.5-turbo

GPT-4-turbo

Claude 3 Opus

Claude 3.5 Sonnet

0.0 0.2 0.4 0.6 0.8 1.0

0.0 0.2 0.4 0.6 0.8 1.0

T5: Target of criticism (Accuracy)

All correct (Proportion)

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


| | | | | |
|---|---|---|---|---|
| | | | | |


Outsourced humans

GPT-3.5-turbo

GPT-4-turbo

Claude 3 Opus

Claude 3.5 Sonnet

0.0 0.2 0.4 0.6 0.8 1.0

0.0 0.2 0.4 0.6 0.8 1.0

Notes: This ﬁgure compares the performance of high-performing human coders (above median aggregate performance) against LLMs across all tasks and coding strategies. For T1, the ﬁgure shows the Macro F1 score; for T2, the Mean Absolute Error (MAE); and for T3, T4, and T5, it shows the accuracy. For T2, a lower number denotes better performance, while for the remaining tasks, higher numbers indicate better performance. The “All correct” panel indicates the proportion of news articles for which all tasks were completed entirely correctly, broken down by coding strategy.

