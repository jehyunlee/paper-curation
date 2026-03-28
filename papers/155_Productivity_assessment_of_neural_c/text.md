![image 1](Ziegler et al._2022_Productivity assessment of neural code completion_images/imageFile1.png)

# Productivity Assessment of Neural Code Completion

Albert Ziegler

wunderalbert@github.com GitHub, Inc. San Francisco, USA

Eirini Kalliamvakou

ikaliam@github.com GitHub, Inc. San Francisco, USA

X. Alice Li

xalili@github.com GitHub, Inc. San Francisco, USA

Andrew Rice

acr31@github.com GitHub, Inc. San Francisco, USA

Devon Rifkin

drifkin@github.com GitHub, Inc. San Francisco, USA

Shawn Simister

narphorium@github.com GitHub, Inc. San Francisco, USA

Ganesh Sittampalam

hsenag@github.com GitHub, Inc. San Francisco, USA

Abstract

Neural code synthesis has reached a point where snippet generation is accurate enough to be considered for integration into human software development worklows. Commercial products aim to increase programmers’ productivity, without being able to measure it directly. In this case study, we asked users of GitHub Copilot about its impact on their productivity, and sought to ind a relection of their perception in directly measurable user data. We ind that the rate with which shown suggestions are accepted, rather than more speciic metrics regarding the persistence of completions in the code over time, drives developers’ perception of productivity.

CCS Concepts: · Software and its engineering → Automatic programming; · Information systems → Language models.

Keywords: codesynthesis, codecompletion, neuralnetworks, productivity

ACM Reference Format:

Albert Ziegler, Eirini Kalliamvakou, X. Alice Li, Andrew Rice, Devon Rifkin, Shawn Simister, Ganesh Sittampalam, and Edward Aftandilian. 2022. Productivity Assessment of Neural Code Completion. In Proceedings of the 6th ACM SIGPLAN International Symposium on Machine Programming (MAPS ’22), June 13, 2022, San Diego, CA, USA. ACM, New York, NY, USA, 9 pages. htps://doi.org/10.1145/ 3520312.3534864

![image 2](Ziegler et al._2022_Productivity assessment of neural code completion_images/imageFile2.png)

This work is licensed under a Creative Commons Attribution 4.0 International License.

MAPS ’22, June 13, 2022, San Diego, CA, USA © 2022 Copyright held by the owner/author(s). ACM ISBN 978-1-4503-9273-0/22/06. htps://doi.org/10.1145/3520312.3534864

Edward Aftandilian

eatan@github.com GitHub, Inc. San Francisco, USA

1 Introduction

Code completion systems that ofer suggestions to a developer on the basis of contextual information from the IDE have been shown to be by far the most frequently used kind of programmer assistance [1]. One common example is that of proposing a list of method names based on the type of a variable. Neural code synthesis approaches to code completion generate suggestions by using a language model to predict what the user might type next (the completion) from the context of what they are working on at the moment (the prompt) [2]. Rather than focusing on a particular task (such as suggesting a method to call), neural code synthesis predicts arbitrary sections of code, and rather than generating single tokens, these systems might predict multiple lines of code at once.

The potential beneits of generating large sections of code automatically are huge, but evaluating these systems is challenging. Oline evaluation where the system is shown a partial snippet of code and then asked to complete it is diicult not least because for longer completions there are many acceptable alternatives and no straightforward mechanism for labeling them automatically [5]. An additional step taken by some researchers [3, 12, 19] is to use online evaluation and track the frequency of real users accepting suggestions, assuming that the more contributions a system makes to the developer’s code, the higher its beneit. The validity of this assumption is not obvious when considering issues such as whether two short completions are more valuable than one long one or other human factors such as whether reviewing suggestions is detrimental to programming low.

Neural synthesis tools such as GitHub Copilot, Kite, and TabNine suggest code snippets within an IDE with the explicitly stated intention to increase a user’s productivity. Developer productivity has many aspects, and a recent study has shown that tools like these are helpful in ways that are only partially relected by measures like completion times for

standardized tasks [14]. Alternatively, we can leverage the developers themselves as expert assessors of their own productivity. This meshes well with current thinking in software engineering research which suggests measuring productivity on multiple dimensions and using self-reported data [6]. We will thus focus on studying perceived productivity.

In this paper we investigate whether usage measurements of developer interactions with GitHub Copilot can predict perceived productivity as reported by developers. We analyze 2,631 survey responses from developers using GitHub Copilot and match their responses to measurements collected from the IDE. We consider acceptance counts and more detailed measures of contribution such as the amount of code contributed by GitHub Copilot, and persistence of accepted completions in the code. We ind that acceptance rate of shown suggestions is a better predictor of perceived productivity than the alternative measures. We also ind that acceptance rate varies signiicantly over our developer population as well as over time, and present a deeper dive into some of these variations.

Our results support the principle that acceptance rate can be used for coarse-grained monitoring of the performance of a neural code synthesis system. In particular, the ratio of shown suggestions being accepted correlates better than more detailed measures of contribution. However, other approaches remain necessary for ine-grained investigation due to the many human factors involved.

2 Background

Oline evaluation of code completion can have shortcomings even in tractable circumstances where completions can be labeled for correctness. For example, a study of 15,000 completions by 66 developers in Visual Studio found significant diferences between synthetic benchmarks used for model evaluation and real-world usage [7]. The evaluation of context-aware API completion for Visual Studio IntelliCode considered Recall@5Ðthe proportion of completions for which the correct method call was in the top 5 suggestions. This metric fell from 90% in oline evaluation to 70% when used online [12].

Due to the diversity of potential solutions to a multi-line completion task, researchers have used software testing to evaluate the behaviour of completions. Competitive programming sites have been used as a source of such data [8, 9] as well as hand-written programming problems [5]. Yet it is unclear how well performance on programming competition data generalizes to interactive development in an IDE.

In this work we deine acceptance rate as the fraction of completions shown to the developer that are subsequently accepted for inclusion in the source ile. The IntelliCode Compose system uses the term CTR (Click Through Rate) for this and reports a value of 10% in online trials [11]. An

alternative measure is that of DCPU (Daily Completions accepted Per User) for which a value of around 20 has been reported [3, 19]. To calculate acceptance rate one must, of course, normalize DCPU by the time spent coding each day. For context, in our study GitHub Copilot has an acceptance rate of 27% and a mean DCPU in excess of 31. These differences are presumably due to diferences in the kinds of completion ofered, or perhaps to user interface choices. We discuss later how developer objectives, choice of programming language and even time of day seem to afect our data. Such discrepancies highlight the diiculty in using acceptance rate to understand the value of a system.

There is some evidence that acceptance rate (and indeed correctness) might not tell the whole story. One survey of developers considered the use of AI to support translation between programming languages and found indications that developers tolerated, and in some cases valued, erroneous suggestions from the model [16].

Measuring developer productivity through activity counts over time (a typical deinition of productivity borrowed from economics) disregards the complexity of software development as they account for only a subset of developer outputs. A more holistic picture is formed by measuring perceived productivity through self-reported data across various dimensions [6], and supplementing it with automatically measured data [4]. In our investigation we used the SPACE framework [6] to design a survey that captures self-reported productivity, and paired the self-reported data with usage telemetry.

To the best of our knowledge, this is the irst study of code suggestion tools establishing a clear link between usage measurements and developer productivity or happiness. A previous study comparing GitHub Copilot against IntelliCode with 25 participants found no signiicant correlation between task completion times and survey responses [13]. Another study considered the beneits of using a plugin converting natural language prompts to code [18]. It found no statistically signiicant improvements in task completion time or task correctness despite positive qualitative survey results (possibly due to small sample size).

3 Data and Methodology

3.1 Usage Measurements

GitHub Copilot provides code completions using OpenAI Codex [5] , which is a version of GPT-3 that has been tuned on publicly available source code. It runs within the IDE and at appropriate points sends a completion request to a cloudhosted instance of the neural model. Completion requests contain a prompt drawn from the code currently in the IDE. GitHub Copilot can generate completions at arbitrary points in code rather than (say) only being triggered when a developer types a period for invoking a method on an object. We use a variety of rules to determine appropriate points to

![image 3](Ziegler et al._2022_Productivity assessment of neural code completion_images/imageFile3.png)

Figure 1. GitHub Copilot’s code completion funnel.

request a completion; to abandon requests if the developer has moved on before the model is ready with a completion; and to determine how much of the response from the model to surface as a completion.

Wemake usagemeasurements foreachdeveloperbycounting the events shown in Table 1, collected for all users of GitHub Copilot according to our terms of usage.1

Our measures of persistence go further than existing work which stops at acceptance. The intuition here is that a completion which is accepted into the source ile but then subsequently turns out to be incorrect con be considered to have wasted developer time both in reviewing it and then having to go back and delete it again. We also record mostly unchanged completions, reasoning that a large completion requiring a few edits might still be a positive contribution. It is not clear how long after acceptance one should conirm persistence and so we consider a range of options.

The events pertaining to completions form a funnel which we show quantitatively in Table 1. We include a summary of all data in Appendix A2.

We normalize these measures against each other and write X_per_Y to indicate we have normalized metric X by metric Y. For example: accepted_per_hour is calculated as the total number of accepted events divided by the total number of (active) hour events.

Table 2 deines the a core set of metrics which we feel have a natural interpretation in this context. We note that there are other alternatives here and we incorporate these in our discussion where relevant.

3.2 Productivity Survey

To understand users’ experience with GitHub Copilot, we emailed 17,420 users providing them with a link to complete

1htps://docs.github.com/en/github/copilot/github-copilot-telemetryterms 2Appendices can be found in the arXiv version htps://arxiv.org/pdf/2205. 06537.pdf.

![image 4](Ziegler et al._2022_Productivity assessment of neural code completion_images/imageFile4.png)

Figure 2. Demographic composition of survey respondents.

an online survey. These were participants of the unpaid technical preview using GitHub Copilot with their everyday programming tasks. The only selection criterion was having previously opted in to receive communications. Between 10th February 2022 and 6th March 2022, we received 2,047 responses we could match to usage measurements during the 4 week period leading up to February 12th March 2022. We focus on usage data from this period, since the vast majority (> 80%) of survey users had illed out their survey by then.

The survey questions contained multiple choice questions, in particular regarding demographic information (shown in Figure 2) and Likert-style questions about diferent aspects of productivity, which were randomized in their order of appearance to the user. Figure 2 shows the demographic composition of our respondents. We note the signiicant proportion of professional programmers who responded.

The SPACE framework [6] deines 5 dimensions of productivity: Satisfaction and well-being, Performance, Activity, Communication and Collaboration, Eiciency and Flow. We use 4 of these (S,P,C,E) since self reporting on (A) is generally considered inferior to direct measurement. We included 11 statements covering these 4 dimensions in addition to a single statement łI am more productive when using GitHub Copilotž. For each self-reported productivity measure, we encoded its ive ordinal response values to numeric labels (1 = Strongly Disagree, . . ., 5 = Strongly Agree). We include the full list of questions and their coding to the SPACE framework in Appendix C.

Early in our analysis we found that the usage metrics we describe in Section 3.1 below corresponded similarly to each of the measured dimensions of productivity, and in turn these dimensions were highly correlated to each other (for details see Figure 3 and Appendix B. We therefore added an aggregate productivity score calculated as the mean of all

Table 1. Developer usage events collected by GitHub Copilot. opportunity a heuristic-baseddetermination by theIDE andthe plugin that a completion might be appropriate

at this point in the code (e.g. the cursor is not in the middle of a word) shown completion shown to the developer accepted completion accepted by the developer for inclusion in the source ile accepted_char the number of characters in an accepted completion mostly_unchanged_X completion persisting in source code with limited modiications (Levenshtein distance less than

33%) after X seconds, where we consider a duration of 30, 120, 300, and 600 seconds unchanged_X completion persisting in source code unmodiied after X seconds. (active) hour an hour during which the developer was using their IDE with the plugin active

Table 2. The core set of measurements considered in this paper.

|Natural name|Explanation|Deinition|
|---|---|---|
|Shown rate|Ratio of completion opportunities that resulted|shown_per_opportunity|
| |in a completion being shown to the user| |
|Acceptance rate|Ratio of shown completions accepted by the|accepted_per_shown|
| |user| |
|Persistence rate|Ratio of accepted completions unchanged after|unchanged_X_per_accepted|
| |30, 120, 300, and 600 seconds| |
|Fuzzy persistence rate|Ratio of accepted completions mostly un-|mostly_unchanged_X_per_accepted|
| |changed after 30, 120, 300, and 600 seconds| |
|Eiciency|Ratio of completion opportunities that resulted|accepted_X_per_opportunity,|
| |in a completion accepted and unchanged after|unchanged_X_per_opportunity|
| |30, 120, 300, and 600 seconds| |
|Contribution speed|Number of characters in accepted completions|accepted_char_per_hour|
| |per distinct, active hour| |
|Acceptance frequency|Number of accepted completions per distinct,|accepted_per_hour|
| |active hour| |
|Persistence frequency|Number of unchanged completions per distinct,|unchanged_X_per_hour|
| |active hour| |
|Total Volume|Total number of completions shown to the user|shown|
|Loquaciousness|Number of shown completions per distinct, ac-|shown_per_hour|
| |tive hour| |
|Eagerness|Number of shown completions per opportunity|shown_per_opportunity|


12 individual measures (excluding skipped questions). This average can only serve as a rough proxy for the much more complex concept of productivity, but facilitates recognition of overall trends, which may be less discernible on individual variables due to higher statistical variation.

For reproducibility and transparency, the full data set of these aggregate productivity scores together with the usage measurements considered in this article is available at htps: //github.com/wunderalbert/prod-neural-materials.

- 4 What Drives Perceived Productivity?


To examine the relationship between objective measurements of user behavior and self-reported perceptions of productivity, we used our set of core usage measurements (Table 2). We then calculated Pearson’s R correlation coeicient and the corresponding p-value of the F-statistic between

each pair of usage measurement and perceived productivity metric. Next, we computed a PLS regression from all usage measurements jointly. Finally, we perform incremental feature selection by analyzing the signiicance of a univariate model where each usage measurement seeks to predict the residuals of a model it with varying numbers of other metrics; this allows us to more directly rank each metric.

We summarize these results in Figure 3 showing the correlation coeicients between all measures and survey questions. The full table of all results is included in Appendix B.

Across all three analyses, we ind acceptance rate (accepted_per_shown) most positively predicts users’ perception of productivity, although, given the confounding and human factors, there is still notable unexplained variance.

![image 5](Ziegler et al._2022_Productivity assessment of neural code completion_images/imageFile5.png)

Figure 3. Correlation between metrics.

Metrics are ordered by similarity based on distance in the correlation matrix, except for manually ixing the aggregate productivity and acceptance rate at the end for visibility.

Of all usage measurements, acceptance rate correlates best with aggregate productivity (𝜌 = 0.24, 𝑃 < 0.0001). This measurement is also the best performing for at least one survey question in each of the SPACE dimensions. This correlation is high conidence but leaves considerable unexplained variance. Below we explore improvements from combining multiple usage measurements together.

Looking at the more detailed metrics around persistence, we see that persistence over shorter time periods is generally better than over longer periods. This is intuitive in the sense

that shorter periods move the measure closer to acceptance rate. We also expect that at some point after accepting the completion it becomes simply part of the code and so any changes (or not) after that point will not be attributed to GitHub Copilot. All persistence measures were less well correlated than acceptance rate.

In order to assess the diferent metrics in a single model in a way that is still robust against their strong collinearity and unafected by the decision whether or not to include highly similar metrics, we ran a regression using projection on

Table 3. Incremental beneit of additional metrics.

p-value univ. coef.

accepted_per_shown <0.0001 0.13 + shown_per_hour 0.04 +0.03 + accepted_char_per_hour 0.04 +0.03 + shown_per_opportunity 0.04 +0.03 + accepted_per_hour 0.05 +0.02

accepted_per_opportunity <0.0001 0.12 + accepted_char_per_hour <0.0001 +0.04 + accepted_per_hour 0.01 +0.03 + unchanged_30_per_hour 0.01 +0.03 + accepted_per_shown 0.02 +0.03

Figure 4. Diferent metrics clustering in latent structures predicting perceived productivity. We color the following groups: lawless suggestions (anything counting the number of unchanged suggestions), persistence rate (ratio of accepted suggestions that are unchanged), and fuzzy persistence rate (ratio of accepted suggestions that are mostly unchanged).

latent structures (PLS), which captures the common variation of these variables as is linearly connected to the aggregate productivity [17]. The irst component, to which every metric under consideration contributes positively, explains 43.2% of the variance. The second component captures the acceptance rate / change rate dichotomy; it explains a further 13.1%.

The results of both the individual correlations as well as the PLS strongly point to acceptance rate being the most immediate indicator of perceived productivity.

But what about combinations of metrics? We aim to quantify the extra information provided by one metric over a set of others. In the vein of incremental feature selection, we it an additional predictor to the residual of a model represented by already selected metrics. Starting from the best single predictors, Table 3 shows the next most useful predictors that predict the residual of the acceptance rate model at p < 0.05. Given a model it to acceptance rate, adding the shown frequency or rate, as well as either amount of accepted characters or accepted completions per hour each further improve predictive ability at statistically signiicant levels. No other additions were statistically signiicant for further iterations.

So even if acceptance rate may be the best of the metrics we considered, it is beneicial to combine with others to get a fuller picture.

- 5 What Drives Acceptance Rate?


- 5.1 Language Use


We are aware that there are signiicant diferences for how GitHub Copilot performs for diferent programming languages. The most common languages among our user base

are TypeScript (24.7% of all shown completions in the observed time frame, 21.9% for users in survey), JavaScript (21.3%, 24.2%), and Python (14.1%, 14.5%). The latter two enjoy higher acceptance rates, possibly hinting at a relative strength of neural tooling versus deductive tooling for untyped languages. Regardless of language, survey participants had a slightly higher acceptance rate than the whole user base.

![image 7](Ziegler et al._2022_Productivity assessment of neural code completion_images/imageFile7.png)

Figure 5. Programming language use by survey participants vs. all users.

This diference in language acceptance can not explain away the efects from Section 4: when considering the linear regression for perceived productivity from acceptance rate, only 17% of the explained variance can be attributed to language. On the other hand, however, 38% of the variance of the diferent levels for the languages’ average perceived productivity can be explained by the acceptance rates in Figure 5 above (using a linear model factoring through acceptance rate).

![image 9](Ziegler et al._2022_Productivity assessment of neural code completion_images/imageFile9.png)

Figure 7. Acceptance rate depending on whether the user is mostly active on weekdays / typical work hours (x-axis), and whether it is actually a weekday / typical oice hour (color).

Table 4. Acceptance rate depending on time factors.

Figure 6. Average acceptance rate for hour-long time buckets during the week. Each point represents the average for such a bucket, whereas the shaded ribbon represents the min-max variation for single hours during the observed 4 week period.

coef p-value t-value

weekend user -0.035 <0.001 -24.5 on a weekday -0.004 0.004 -2.9 usual day for user 0.021 <0.001 11.3

work hour user -0.036 <0.001 -22.3 during work hours -0.001 0.578 -0.6 usual time for user 0.019 <0.001 11.5

- 5.2 Circadian and Weekly Rhythms


For coherence in the meaning of timestamps and weekdays, all data in this section was restricted to users from the United States (whether in the survey or not). We used the same time frame as for the investigation in Section 4.

Results of linear regressions of acceptance rate from: 1. user’s percentile value for of how much their activity is concentrated on weekdays (during typical work hours), 2. a categorical variable describing whether the suggestion is actually made on a weekday (during typical work hours), and 3. the proportion of this user’s contributions during the same time range.

We observe strong regular patterns in overall acceptance rate (Figure 6). These lead us to distinguish three diferent time regimes, all of which are statistically signiicantly distinct at p < 0.001% (using bootstrap re-sampling):

- • The weekend: Saturdays and Sundays (day boundaries taken from PST), where the average acceptance rate is comparatively high at 23.5%.
- • Typical non-working hours during the week: evenings after 4 pm PST until mornings 7 am PST, where the average acceptance rate is also rather high at 23%.
- • Typical working hours during the week from 7 am PST to 4 pm PST, where the average acceptance rate is much lower at 21.2%.


Users’ inclination to accept more suggestions outside of standard working hours could be attributed either to regular changes in the users’ behavior (e.g. accepting more solutions because they are more relaxed), or to changes in the underlying distribution of who is coding and what they are working on (e.g. personal projects being easier to suggest code for).

To distinguish between these two explanations, we trained a model to predict a user’s acceptance rate for a particular time bucket from their usual contribution times (Table 4). Unexpectedly to us, we found that the actual time bucket mattered very little ś but what did matter was whether it lay in the user’s usual time regime. That means a user normally active only during the week accepts fewer solutions on the rare occasions they do code on a weekend, and a user whose

activity is normally restricted to working hours accepts fewer solutions when they do venture outside that time range.

6 Threats To Validity

The principal challenge to this work is that we have only been able to investigate correlation and not causation. We hope to have mitigated this to some extent by selecting łsensiblež metrics that could plausibly capture a causal relationship with productivity. Nor do we claim that these metrics themselves directly impact productivity (a developer with a faulty tab-key that accidentally accepts 80% of suggestions without user intention will probably not be extra productive because of it), but only that these metrics are a good indicator of an underlying quality that predicts productivity.

We did not set out to accurately predict a survey participant’s answers, but to ind a signal between perceived productivity and usage metrics. Still, we must highlight that our best performing metric has a Pearson coeicient of 0.24, leaving a considerable amount of unexplained variance.

User-perceived productivity is also not necessarily actual productivity:maximisingacceptance_per_shownmight satisfy an individual developer without reducing the amount of time it takes them to solve a task. And indeed one study

looking at the beneits of GitHub Copilot over IntelliCode found no measurable impact on task completion time despite notably positive feedback from developers [13]. On the other hand, one drawback of task-oriented studies is of how representative the chosen tasks are of real workloads whereas online studies (such as ours) capture authentic activity.

Another substantial caveat is that we only considered a single completion system, in particular with a single ixed neural engine. Alternatives could be diferent in many aspects that could afect developer attitudes. Factors might include average quality and the latency of completions, their length and even the user interface used to present them.

7 Conclusion

Neural code completion systems have the potential to hugely improve developer productivity through their ability to assimilate contextual information about the developer’s current activity and then generate substantial completions in response. In this paper we investigated ways of connecting the productivity beneit of GitHub Copilot to usage measurements from developer activity. Our approach was to seek correlations between our measurements and user-reported productivity from survey results.

In common with prior work we collected measurements about the acceptance of completions, but we also developed measures of persistence. This was based on the idea that for longer completions a developer might have to take more action after accepting a completion such as deleting or correcting an erroneous one.

We were surprised to ind that acceptance rate (number of acceptances normalized by the number of shown completions) was better correlated with reported productivity than our measures of persistence.

But in hindsight, this makes sense. Coding is not typing, and GitHub Copilot’s central value lies not in being the way the user enters the highest possible number of lines of code. Instead, it lies in helping the user to make the best progress towards their goals. A suggestion that serves as a useful template to tinker with may be as good or better than a perfectly correct (but obvious) line of code that only saves the user a few keystrokes.

This suggests that a narrow focus on the correctness of suggestions would not tell the whole story for these kinds of tooling. Instead one could view code suggestions inside an IDE to be more akin to a conversation with a chatbot. We see anecdotal evidence of this in comments posted about GitHub Copilot online (see Appendix E for examples) in which users talk about sequences of interactions. A conversation turn in this context consists of the prompt in the completion request and the reply as the completion itself. The developer’s response to the completion arises from the subsequent changes which are incorporated in the next prompt to the model. And there are clear programming parallels to factors such as

speciicity and repetition that have been identiied to afect human judgements of conversation quality [10]. Researchers have already investigated the beneits of natural language feedback to guide program synthesis [2] and so ours is not a radical proposal. But neither is it one we have seen followed.

In future work, we wish to further explore this analogy, borrowing ideas [15] from the evaluation of chatbots and natural language text generation.

8 Broader Impact

A detailed impact analysis of the model that underlies GitHub Copilot may be found in the appendix of [5]. In this section, we focus more speciically on the potential impact of using the metrics we have described in this paper to evaluate the success of neural code completion systems.

First, focusing on a single top-level metric such as acceptance rate may bias a tool toward the most popular use cases Ð the most popular programming languages, natural languages, IDEs, locations, etc. Users in underrepresented groups may see lower quality results. We can mitigate this by slicing our data along the lines described above, and avoiding shipping changes that improve the top-level metric but degrade performance for other slices of the data.

Second, to compute these metrics, we must collect telemetry from users, exposing users to potential security and privacy concerns. We mitigate this by enacting strict access controls to user data and collaborating with organization and industry experts at protecting user data.

Third, blindly optimizing for a proxy (acceptance rate) for a desired property (usefulness) encourages artiicial changes that improve only that proxy. For example, cutting code suggestions into half and suggesting both parts consecutively would likely transform one accepted suggestion into two, while not substantially increasing the number of rejections. Thus it would likely increase acceptance rate without substantially increasing, and maybe even while decreasing, user beneit. We can thus not recommend acceptance rate as singular and ultimate criterion of quality ś it will be useful for many applications, e.g. comparing incremental changes to the code generating model, but its validity is limited in other cases, especially those involving signiicantly changed operational parameters.

Acknowledgments

We thank the GitHub Copilot team for their help, and in particular Krzysztof Cieslak and Johan Rosenkilde for implementing the highly complex telemetry of suggestion fate, including calculating edit distances for fuzzy matches. We thank the SAINTes team at Microsoft Research for their advisement; Nicole Forsgren and Denae Ford Robinson for advising on questions capturing perceived productivity with the SPACE framework, and Tom Zimmermann and Christian Bird for recommending more time intervals to consider

for suggestion fate monitoring. We thank Rahul Pandita for LATEXsupport and proofreading. Finally, we are grateful to GitHub Incorporated for supporting this research.

References

- [1] Sven Amann, Sebastian Proksch, Sarah Nadi, and Mira Mezini. 2016. A Study of Visual Studio Usage in Practice. In IEEE 23rd International Conference on Software Analysis, Evolution, and Reengineering, SANER 2016, Suita, Osaka, Japan, March 14-18, 2016 - Volume 1. IEEE Computer Society, 124ś134. htps://doi.org/10.1109/SANER.2016.39
- [2] Jacob Austin, Augustus Odena, Maxwell Nye, Maarten Bosma, Henryk Michalewski, David Dohan, Ellen Jiang, Carrie J. Cai, Michael Terry, Quoc V. Le, and Charles Sutton. 2021. Program Synthesis with Large Language Models. CoRR abs/2108.07732 (2021). arXiv:2108.07732 htps://arxiv.org/abs/2108.07732
- [3] Gareth Ari Aye, Seohyun Kim, and Hongyu Li. 2021. Learning Autocompletion from Real-World Datasets. In 43rd IEEE/ACM International Conference on Software Engineering: Software Engineering in Practice, ICSE (SEIP) 2021, Madrid, Spain, May 25-28, 2021. IEEE, 131ś

139. htps://doi.org/10.1109/ICSE-SEIP52600.2021.00022

- [4] Moritz Beller, Vince Orgovan, Spencer Buja, and Thomas Zimmermann. 2020. Mind the gap: on the relationship between automatically measured and self-reported productivity. IEEE Software 38, 5 (2020), 24ś31.
- [5] Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde de Oliveira Pinto, Jared Kaplan, Harrison Edwards, Yuri Burda, Nicholas Joseph, Greg Brockman, Alex Ray, Raul Puri, Gretchen Krueger, Michael Petrov, Heidy Khlaaf, Girish Sastry, Pamela Mishkin, Brooke Chan, Scott Gray, Nick Ryder, Mikhail Pavlov, Alethea Power, Lukasz Kaiser, Mohammad Bavarian, Clemens Winter, Philippe Tillet, Felipe Petroski Such, Dave Cummings, Matthias Plappert, Fotios Chantzis, Elizabeth Barnes, Ariel Herbert-Voss, William Hebgen Guss, Alex Nichol, Alex Paino, Nikolas Tezak, Jie Tang, Igor Babuschkin, Suchir Balaji, Shantanu Jain, William Saunders, Christopher Hesse, Andrew N. Carr, Jan Leike, Joshua Achiam, Vedant Misra, Evan Morikawa, Alec Radford, Matthew Knight, Miles Brundage, Mira Murati, Katie Mayer, Peter Welinder, Bob McGrew, Dario Amodei, Sam McCandlish, Ilya Sutskever, and Wojciech Zaremba. 2021. Evaluating Large Language Models Trained on Code. CoRR abs/2107.03374 (2021). arXiv:2107.03374 htps://arxiv.org/abs/2107.03374
- [6] Nicole Forsgren, Margaret-Anne Storey, Chandra Maddila, Thomas Zimmermann, Brian Houck, and Jenna Butler. 2021. The SPACE of Developer Productivity: There’s more to it than you think. Queue 19, 1 (2021), 20ś48.
- [7] Vincent J. Hellendoorn, Sebastian Proksch, Harald C. Gall, and Alberto Bacchelli. 2019. When code completion fails: a case study on realworld completions. In Proceedings of the 41st International Conference on Software Engineering, ICSE 2019, Montreal, QC, Canada, May 25-31, 2019, Joanne M. Atlee, Tevik Bultan, and Jon Whittle (Eds.). IEEE / ACM, 960ś970. htps://doi.org/10.1109/ICSE.2019.00101
- [8] Dan Hendrycks, Steven Basart, Saurav Kadavath, Mantas Mazeika, Akul Arora, Ethan Guo, Collin Burns, Samir Puranik, Horace He, Dawn Song, and Jacob Steinhardt. 2021. Measuring Coding Challenge Competence With APPS. CoRR abs/2105.09938 (2021). arXiv:2105.09938 htps://arxiv.org/abs/2105.09938
- [9] Sumith Kulal, Panupong Pasupat, Kartik Chandra, Mina Lee, Oded Padon, Alex Aiken, and Percy Liang. 2019. SPoC: Search-based Pseudocode to Code. In Advances in Neural Information Processing Systems 32: Annual Conference on Neural Information Processing Systems 2019, NeurIPS 2019, December 8-14, 2019, Vancouver, BC, Canada, Hanna M. Wallach, Hugo Larochelle, Alina Beygelzimer, Florence d’Alché-Buc, Emily B. Fox, and Roman Garnett (Eds.). 11883ś11894. htps://proceedings.neurips.cc/paper/2019/hash/


- 7298332f04ac004a0ca44cc69ecf6f6b-Abstract.html
- [10] Abigail See, Stephen Roller, Douwe Kiela, and Jason Weston. 2019. What makes a good conversation? How controllable attributes afect human judgments. In Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, NAACL-HLT 2019, Minneapolis, MN, USA, June 2-7, 2019, Volume 1 (Long and Short Papers), Jill Burstein, Christy Doran, and Thamar Solorio (Eds.). Association for Computational Linguistics, 1702ś1723. htps://doi.org/10.18653/v1/n19-1170
- [11] Alexey Svyatkovskiy, Shao Kun Deng, Shengyu Fu, and Neel Sundaresan. 2020. IntelliCode compose: code generation using transformer. In ESEC/FSE ’20: 28th ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering, Virtual Event, USA, November 8-13, 2020, Prem Devanbu, Myra B. Cohen, and Thomas Zimmermann (Eds.). ACM, 1433ś1443. htps://doi.org/10.1145/3368089.3417058
- [12] Alexey Svyatkovskiy, Sebastian Lee, Anna Hadjitoi, Maik Riechert, Juliana Vicente Franco, and Miltiadis Allamanis. 2021. Fast and MemoryEicient Neural Code Completion. In 18th IEEE/ACM International Conference on Mining Software Repositories, MSR 2021, Madrid, Spain, May 17-19, 2021. IEEE, 329ś340. htps://doi.org/10.1109/MSR52588. 2021.00045
- [13] Priyan Vaithilingam, Tianyi Zhang, and Elena Glassman. 2022. Expectation vs. Experience: Evaluating the Usability of Code Generation Tools Powered by Large Language Models. In CHI ’22 Late-Breaking Work: Proceedings of the 2022 Conference on Human Factors in Computing Systems.
- [14] Priyan Vaithilingam, Tianyi Zhang, and Elena L. Glassman. 2022. Expectation vs. Experience: Evaluating the Usability of Code Generation Tools Powered by Large Language Models. In CHI Conference on Human Factors in Computing Systems Extended Abstracts (New Orleans, LA, USA) (CHI EA ’22). Association for Computing Machinery, New York, NY, USA, Article 332, 7 pages. htps://doi.org/10.1145/3491101. 3519665
- [15] Chris van der Lee, Albert Gatt, Emiel van Miltenburg, Sander Wubben, and Emiel Krahmer. 2019. Best practices for the human evaluation of automatically generated text. In Proceedings of the 12th International Conference on Natural Language Generation, INLG 2019, Tokyo, Japan, October 29 - November 1, 2019, Kees van Deemter, Chenghua Lin, and Hiroya Takamura (Eds.). Association for Computational Linguistics, 355ś368. htps://doi.org/10.18653/v1/W19-8643
- [16] Justin D. Weisz, Michael J. Muller, Stephanie Houde, John T. Richards, Steven I. Ross, Fernando Martinez, Mayank Agarwal, and Kartik Talamadupula. 2021. Perfection Not Required? Human-AI Partnerships in Code Translation. In IUI ’21: 26th International Conference on Intelligent User Interfaces, College Station, TX, USA, April 13-17, 2021, Tracy Hammond, Katrien Verbert, Dennis Parra, Bart P. Knijnenburg, John O’Donovan, and Paul Teale (Eds.). ACM, 402ś412. htps://doi.org/10.1145/3397481.3450656
- [17] Svante Wold, Michael Sjöström, and Lennart Eriksson. 2001. PLSregression: a basic tool of chemometrics. Chemometrics and Intelligent Laboratory Systems 58, 2 (2001), 109ś130. htps://doi.org/10.1016/ S0169-7439(01)00155-1 PLS Methods.
- [18] Frank F. Xu, Bogdan Vasilescu, and Graham Neubig. 2021. In-IDE Code Generation from Natural Language: Promise and Challenges. CoRR abs/2101.11149 (2021). arXiv:2101.11149 htps://arxiv.org/abs/ 2101.11149
- [19] Wen Zhou, Seohyun Kim, Vijayaraghavan Murali, and Gareth Ari Aye.


2021. Improving Code Autocompletion with Transfer Learning. CoRR abs/2105.05991 (2021). arXiv:2105.05991 htps://arxiv.org/abs/2105. 05991

