# arXiv:2411.05025v1[cs.CL]30 Oct 2024

## LLMs as Research Tools: A Large Scale Survey of Researchers’ Usage and Perceptions

ZHEHUI LIAO, University of Washington, US MARIA ANTONIAK, Pioneer Centre for Artificial Intelligence, University of Copenhagen, Denmark INYOUNG CHEONG, Princeton University, US EVIE YU-YEN CHENG, Allen Institute for Artificial Intelligence (Ai2), US AI-HENG LEE, Allen Institute for Artificial Intelligence (Ai2), US KYLE LO, Allen Institute for Artificial Intelligence (Ai2), US JOSEPH CHEE CHANG, Allen Institute for Artificial Intelligence (Ai2), US AMY X. ZHANG, University of Washington, US

The rise of large language models (LLMs) has led many researchers to consider their usage for scientific work. Some have found benefits using LLMs to augment or automate aspects of their research pipeline, while others have urged caution due to risks and ethical concerns. Yet little work has sought to quantify and characterize how researchers use LLMs and why. We present the first large-scale survey of 816 verified research article authors to understand how the research community leverages and perceives LLMs as research tools. We examine participants’ self-reported LLM usage, finding that 81% of researchers have already incorporated LLMs into different aspects of their research workflow. We also find that traditionally disadvantaged groups in academia (non-White, junior, and non-native English speaking researchers) report higher LLM usage and perceived benefits, suggesting potential for improved research equity. However, women, non-binary, and senior researchers have greater ethical concerns, potentially hindering adoption.

Additional Key Words and Phrases: LLMs, Large Language Models, Survey, Research Support Tools, Demographic, Research Community ACM Reference Format:

Zhehui Liao, Maria Antoniak, Inyoung Cheong, Evie Yu-Yen Cheng, Ai-Heng Lee, Kyle Lo, Joseph Chee Chang, and Amy X. Zhang. 2024. LLMs as Research Tools: A Large Scale Survey of Researchers’ Usage and Perceptions. 1, 1 (November 2024), 30 pages. https://doi.org/10.1145/nnnnnnn.nnnnnnn

### 1 Introduction

From Vannevar Bush’s hypothesized Memex in 1945 [13] to Apple’s vision of the Knowledge Navigator in 1987 [73], many have long envisioned tools that organize and interact with the sum of our knowledge to enable us to better conduct complex knowledge work and push the boundaries of what we know. Recent advancements in generative AI technologies that are trained on terabytes of text scraped from the internet [84] and fine-tuned to provide a chat

Authors’ Contact Information: Zhehui Liao, University of Washington, Seattle, US; Maria Antoniak, Pioneer Centre for Artificial Intelligence, University of Copenhagen, Copenhagen, Denmark; Inyoung Cheong, Princeton University, New York, US; Evie Yu-Yen Cheng, Allen Institute for Artificial Intelligence (Ai2), Seattle, US; Ai-Heng Lee, Allen Institute for Artificial Intelligence (Ai2), Seattle, US; Kyle Lo, Allen Institute for Artificial Intelligence (Ai2), Seattle, US; Joseph Chee Chang, Allen Institute for Artificial Intelligence (Ai2), Seattle, US; Amy X. Zhang, University of Washington, Seattle, US.

Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than the author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org.

© 2024 Copyright held by the owner/author(s). Publication rights licensed to ACM. Manuscript submitted to ACM

Manuscript submitted to ACM 1

interface [76] bring us one step closer to making this dream a reality. More directly, this technology has also sparked a surge of interest across research, industry funding, and startups to develop a new generation of research support tools [20, 25, 28, 59, 87, 88, 91].

In fact, the recent burst in popularity of widely available generative AI tools, such as ChatGPT,1 and findings from small-scale interview and survey studies with researchers [26, 72] suggest that many in the research community have already found benefits in incorporating current generative AI models into their research workflows. Adopting this new generation of knowledge tools has opened up many possibilities, such as improved efficiency, greater research equity, and inspiring novel ideas. At the same time, new tools both breathe new life into familiar research risks and ethical concerns — like transparency, reproducibility, plagiarism, and data fabrication — while introducing new dangers to the research process. It is possible that these tools could result in researchers losing essential skills [5, 52], the development of emerging social norms and associated reputational costs [37], and a decrease in research creativity, among other possibilities. Differences in perceptions about risks, ethics, and social acceptability across demographic groups and researcher backgrounds could also drive differences in adoption, so that any benefits accrue unevenly. This could potentially exacerbate existing structural barriers in academia due to biases and other factors [29].

While prior work has mostly focused on research domain-specific investigations [44, 47, 62, 78, 97] or small-scaled surveys or qualitative interviews [26, 72], we conducted a large scale survey with verified published authors. These authors were sourced from Semantic Scholar, a platform that maintains an open repository of published researchers from a wide range of research domains, demographic backgrounds, and research experiences. Our survey of these researchers was designed to explore the following research questions.

- • RQ1: What are the different ways researchers use2 LLMs in their research process today?
- • RQ2: How does the background3 of a researcher relate to the way they use LLMs?
- • RQ3: What are researchers’ perceptions4 of LLMs for usage in different parts of the research process?
- • RQ4: How does the way a researcher uses LLMs relate to their perceptions?
- • RQ5: How does the background of a researcher relate to their perceptions?
- • RQ6: How does the source5 of an LLM affect researchers’ perceptions and usage?


Our survey focused on better understanding how researchers are actually using LLM-based researcher tools in their own work today, and how they perceive the risks and benefits of leveraging LLMs for different research tasks. In particular, we were also interested in researchers’ perceptions not only of LLM usage but also about the acceptability of using these tools, and the possible differences in perception across demographic groups, leading us to recruit researchers across nationalities, languages, career stages, discipline, gender, age, etc. The differences we uncover between these groups reveal rapidly changing social norms around the usage of AI tools in research, highlighting important considerations around research equity and broader adoption.

In particular, we find around 81% of researchers we surveyed have used LLMs in one or more places in their research pipeline, with the tasks of Information Seeking and Editing reported most frequently and Data Analysis and Generation reported least frequently. We also find surprising differences between researchers of different demographic groups. Based

1The ChatGPT mobile app has more than 100 million downloads on the Android app store and more than 1 million ratings on the iPhone app store, as of September 2024. 2Usages of LLMs in the research process that we examine: information seeking, editing, ideation and framing, direct writing, data cleaning and analysis, data generation

- 3Researcher background characteristics that we examine: race, gender, native English speaker, research experience, field of research
- 4Researcher perceptions of LLMs that we examine: risks, benefits, ethics, and willingness to disclose to peers and reviewers 5Sources of LLMs that we examine: non-profit vs. for-profit entities


on self-reporting, we found that researchers who are non-White, non-native English speaking, and junior researchers both use LLMs more frequently and also perceive higher benefits and lower risks. As people with these demographics traditionally tend to face certain structural barriers, our findings suggest that LLMs can help with improving research equity. Meanwhile, women and non-binary researchers have greater ethical concerns, as do those with more years of research experience. In addition, while LLMs are broadly used across all fields, we see significantly greater comfort with disclosure of usage in computer science fields as well as lower ethical concerns compared to other disciplines. This suggests that to truly achieve broad adoption, ethical issues around LLMs must be confronted and social norms established within each field. Finally, we find that researchers overall prefer to use LLMs from open source/non-profit entities over for-profit entities due to a variety of concerns with models from the existing major for-profit corporations.

Our contributions include the following.

- • Large-scale survey results from 816 verified research paper authors, which we release to the public.6
- • Detailed quantitative and qualitative analyses of the survey results, revealing how researchers currently incorporate LLMs into their workflow, and how they perceive their risks and benefits.
- • Insights into LLM usage patterns and perceptions across demographic groups, revealing that while some traditionally disadvantaged groups in academia (non-White, non-native English speaking, and junior researchers) report higher usage and perceived benefits, other groups (women, non-binary, and senior researchers with more experience) express greater ethical concerns.
- • Lessons about researchers’ preferences for non-profit and open-source models versus commercial models, along with their rationales, which can inform future development and adoption strategies for LLMs in academia.


2 Related Work

- 2.1 LLMs as Research Support Tools: Current Practices and Benefits


Recent work has suggested that researchers have already begun to adopt LLMs into their research workflows across various disciplines. In early 2023, Morris [72] conducted in-depth interviews with 20 researchers of diverse backgrounds,7 focusing on the opportunities and potential concerns around the use of LLMs as research tools in their respective fields. This study, with many others, reveals that researchers across numerous disciplines are incorporating LLMs into different stages of research, including ideation, literature review, data creation, cleaning and analysis, programming, and, most commonly, writing or drafting research papers [10, 31, 70, 89, 93, 101].

Moreover, LLMs have been explored as a potential solution to challenges in the academic publishing process. Alvarez [7] suggests that LLMs could address the “overtaxed peer-review system”, a sentiment supported by Liang et al. [61], who found that over 80% of researchers considered ChatGPT-generated feedback more beneficial than feedback from at least some human reviewers. Separately, Koller et al. [53] advocated for the use of LLMs in conference submissions, arguing that these tools help researchers “contextualize their work, democratize knowledge, enhance data analysis, and produce better scientific output.” As a result, the increasing adoption of LLM assistance is evident in both scientific research articles [62] and peer reviews [78].

Beyond evidence of the research community adopting widely available LLM-based tools into their workflow, the AI and HCI research community have also devoted many resources in recent years to exploring the next generation of

- 6Link to survey results: https://github.com/allenai/llm-research-survey. All personally identifiable information in the responses, including all free-text responses have been removed. The study is approved by our university IRB, and the participants each gave explicit consent at the start of the survey for their data to be released.
- 7Notably, this study intentionally only covered researchers from non-computer science fields.


research tools powered by LLMs. Research has focused on all stages of the research workflow, from research ideation [28, 65, 94], paper reading [27, 68], literature review [38, 43, 59], writing [31, 48, 69], peer review support [22, 87], and more. Anecdotally, there has also been increased commercial interest in building LLM-based research support tools. For example, Meta released Galactica, an LLM model trained for general scientific tasks in 2022 [88]; Undermind allows users to converse with a chatbot that has access to research paper search results [91]; Elicit allows users build research paper comparison tables by extracting information across many papers [25]; and Consensus answers scientific questions by gathers confirming and opposing evidence across papers [20]. More recently, there have also been attempts to build fully autonomous end-to-end research agents based on LLMs. For example, Sakana AI built “The AI Scientist”, which aimed to conduct research in machine learning, from generating research ideas to executing experiments, to writing the paper, and reviewing the paper [14, 15]; and, similarly, FutureHouse launched a 10-year mission to automate biology research at scale [80].

Given this trend, there have been several recent work focused on a better understanding of how researchers leverage LLMs in their research workflow and the risks and benefits of doing so. Yet, many only focused on one specific research domain (e.g., HCI [44], psychology [47], machine learning [78], and management research [97]). More closely related to our work, there has also been a small scale survey (N=72) [26] and interview study (N=20) [72] that covered researchers across different domains. Our work represents the first large-scale survey (N=816) focusing on researchers’ use of LLMs across various disciplines. It provides empirical evidence for trends previously only speculated about in smaller qualitative studies [e.g., 72] or inferred from textual analysis of published papers [e.g., 51].

### 2.2 Risks and Ethical Implications of LLMs in Research

While LLMs have shown great promise for a future where novel AI capabilities can have significant positive impacts on science, the current implementations have faced many critiques from the community, including claims that LLMs have a popularity bias, contain a reductive view on how researchers learn their knowledge, and generate made-up articles completely [10, 34].

- 2.2.1 Lack of precision or “hallucination”. One of the primary concerns of the applications of LLMs to scientific research is their insufficient level of precision and accuracy [7]. LLMs have been observed to generate plausible-sounding but entirely fictional content, a phenomenon popularly referred to as “hallucination” [6]. For example, Galactica, an LLM trained on scientific papers [88], was taken down after producing convincing but false scientific articles [34]. Current LLMs struggle with tasks requiring precise calculations and logical reasoning [85]. In software development, studies indicate that developers often reject LLMs’ initial code suggestions [100] and face difficulties in understanding and debugging the generated code [60, 67, 92]. Without proper vetting, inaccurate content could contribute to the spread of misinformation and erode trust in research [31, 52]. In fields like medicine or engineering, where precision is crucial, LLM inaccuracies could have serious real-world consequences [8, 90]. Our results showed a similar phenomenon in using LLMs for science, where hallucination and misinformation were among the most frequently mentioned risks by our participants based on qualitative responses.
- 2.2.2 Undermined research integrity. The adoption of LLMs in academic research raises fundamental questions about diminished research integrity and originality. Researchers have expressed worry about the potential “proliferation of low-quality research” [10], as LLMs may facilitate the mass production of superficial or derivative work. This concern is corroborated by Kobiella et al. [52], who found that knowledge workers experienced a decreased sense of achievement when using LLMs, driven by reduced ownership, lack of challenge, and concerns about output quality. The


National Institutes of Health (NIH) has taken a strong stance against using LLMs for grant applications or reviews [75], cautioning that such practices undermine “the originality of thought” and lead to homogenization of ideas or even research misconduct [56]. Furthermore, the integration of LLMs into review writing may exacerbate existing issues of unpredictability and unfairness. Latona et al. [78] identified “AI Review Lottery” at ICLR 2024 where papers receiving AI-assisted reviews were more likely to be accepted, raising questions about the reliability of the peer review system.

- 2.2.3 Unexplainability and obscurity. The complexity of LLMs makes it difficult to understand or explain why they come to certain output, which in turn affects the reliability and interpretation of research results assisted by LLMs [83]. The obscurity issue restricts access to model’s internal workings and training data, thereby hindering research transparency and verifiability [98]. This issue is particularly concerning because many researchers, particularly those lacking technical expertise or computational resources predominantly rely on commercial closed models [90, 98]. Sallou et al. [79] asserts that software engineering research faces threats to validity from the prevalent use of closed-source models, potential data leakage and reproducibility issues due to output variability and time-based drift, all of which can compromise the reliability and generalizability of research findings. While open models offer greater transparency, compared to closed models, by offering access to code and weights, many still fall short of full disclosure, commonly withholding elements like training datasets or fine-tuning processes [45, 63]. In this work, we ask survey participants to discuss their preferences for the predominantly closed models offered by industry versus open source and non-profit alternatives.


### 2.3 Demographic Influences on LLM Perception and Adoption

In addition to the high-level benefits and risks of LLMs, individual perceptions and usage patterns of LLMs are shaped by various factors, including personality traits, age, gender, and educational background [41]. For instance, in the realm of personality and age, research has shown that people with a high level of agreeability and younger people tend to have more positive views of AI, while those susceptible to conspiracy theories often have more negative perceptions [86]. A notable gender gap has been observed in LLM adoption, with male users outnumbering female users, which could be mitigated through technology-related education [24]. In the field of scientific research, structural biases have long led to disparities in academic publishing, citations, and career advancement along the lines of gender, race, economic status, and more [29, 36]. Despite some progress in recent decades, projections indicate that gender gaps in STEMM (Science, Technology, Engineering, Mathematics, and Medicine) fields may persist for generations without significant systemic reform [35]. Interestingly, LLMs present an opportunity to reduce certain inequities in research and publishing. They can lower barriers for non-native English speakers [72] and provide high-quality reviews to novice researchers who may struggle to obtain feedback from peers [16].

While LLMs show promises and challenges in academic settings, a significant gap exists in our understanding of their impact across diverse demographic groups. Quantitative research examining how LLM usage patterns and perceptions vary among different populations within academia is notably scarce. To address this gap, we conducted a large-scale survey of researchers from a wide range of backgrounds. Our aim was to explore the nuanced and potentially differential impacts of LLMs on various demographic groups within the academic community. This approach recognizes that understanding the risks and opportunities presented by LLMs is important not only for the research community as a whole but also for specific demographic subgroups who may experience unique challenges or benefits. Our findings indicate that LLMs have a disproportionate effect on researchers with different identities, suggesting both challenges and opportunities for using these tools to address longstanding inequities in the research ecosystem.

### 3 Methods

Drawing insights from prior literature, we designed a questionnaire to study researchers’ usage and perception of LLMs, and recruited participants among verified published authors. We initially collected 1,226 responses and ended up with 816 responses after filtering to ensure completeness and quality. Different from prior work that only reported participants’ fields of study in small-scale surveys and interviews [26, 72], we additionally collected fine-grained demographic information in our survey. We transformed the dataset to generate the final demographic groups in which some of the response options were grouped to form coarser buckets (e.g., years of research experience), and free responses (e.g., fields of study) were manually coded and discretized for analysis. The survey collected both multiple-choice responses and free-text responses. We used linear mixed-effects models to test the relationships between researchers’ LLM usage and perception, as well as between researchers’ background and usage and perception. For free-text responses, we conducted an iterative open thematic analysis to gain a deeper qualitative understanding of participants’ perceptions of LLMs [11, 19].

### 3.1 Survey Design, Participant Recruitment, and Data Collection

- 3.1.1 Design and recruitment. When designing the questionnaire in the survey, we used the four following approaches: First, for inspiration, we looked to recent literature on using LLMs as a productivity tool for research [10, 71, 72, 78, 95] and other scenarios [60, 66], which included qualitative interviews and survey results. Second, we reviewed historic papers on how the research community had adopted new tools in the past, specifically around the use of crowdsourcing for data collection, user studies, and other productivity tasks [49, 50, 57]. Third, we publicized an anonymous formative survey on X/Twitter targeted towards researchers with open-ended questions about whether and how they use LLMs for research in order to help define initial categories of usage that we later refined. Finally, we shared early drafts of the questionnaire with other researchers in our own institutions for feedback and iteration. In the end, we classified LLM usage for research into six broad categories, each with more specific use cases under them: information seeking, editing, ideation & framing, directing writing, data cleaning & analysis, and data generation. We provide the full set of final survey questions in the Supplementary Materials.
- 3.1.2 Data collection. We collected survey responses from participants who have published at least one research paper in the past. To ensure participants were published authors, we partnered with Semantic Scholar for targeted recruitment of researchers who are listed as an author of at least one published paper on the platform. Semantic Scholar maintains a large-scale academic knowledge graph of researchers (i.e., authors) and papers, and provides a freely available web service to browse them as author profile pages.8 Researchers can claim their author profile pages and send corrections to Semantic Scholar, which in turn employs a quality assurance team for verifying the claims and corrections. A survey recruitment email was sent to 107,346 verified claimed authors, and the click-through rate was around 1.6%. After click-through, 71.6% of the participants signed the consent form to start the survey, of which 60.6% completed the survey. We collected 1,226 unfiltered survey responses, which we subsequently filtered to exclude those from participants who did not progress past the first page or spent fewer than 2 seconds on each question. In total, this resulted in 𝑛 = 816 survey responses that we used for our analysis. The survey contained a mix of optional and required questions. For example, participants could choose not to disclose their demographic information, such as gender or race. The study was reviewed and exempted by the University of Washington IRB.


8https://www.semanticscholar.org/

- 3.1.3 Limitations. Since we recruited from verified authors listed on Semantic Scholar, we could have tied the survey responses to participants’ author metadata from Semantic Scholar to obtain high-precision demographic information (such as a list of publications, years of experiences, institutions, pronouns, etc.). However, for privacy concerns, we only used their email addresses for targeted recruitment of verified published authors. We instead relied on self-reporting using optional survey questions for demographic information, and did not tie survey responses to their author metadata. While Semantic Scholar covers a wide range of fields of study, we did find more participants to be in the field of computer science (40%), but other fields such as social sciences, biology, medicine, and natural sciences were also represented. There were also more men who responded to the survey (79%), which may partly reflect the existing imbalances in these fields of study. The detailed distributions are reported in §4. Finally, the survey responses were collected in batches of recruitment emails over a six-month period from November 2023 to April 2024, with the bulk of the responses received in January 2024. The uses and perceptions of researchers may change over time as LLM tools continue to evolve, but we hope this survey can give the readers a snapshot of the current state of the community and support informed decisions


- as we continue to build consensus and norms around the use of LLMs for research.


### 3.2 Quantitative Analysis of Survey Responses

- 3.2.1 Preparing the demographic groups. Out of the 816 responses, 644 provided demographic information. We focused on five demographic categories collected in the survey for later analysis: gender, race, years of research experience, native language, and field of study. The first four were collected as answers to multiple-choice questions and further consolidated into broader categories during analysis. For example, to balance our analysis given a large proportion of men participants, we collapsed all responses from women, non-binary, and other participants into a single category. Field of study was collected as free response and manually classified into four categories by the authors (more details on this process can be found in Appendix B). Answers that did not fit into any categories, such as “Prefer Not to Answer” or “Prefer to Self-Describe” were filtered out from demographic-specific analysis. We ended up with 611 responses with gender identity, 527 with racial identity, 644 with years of research experience and native language information, and 635 with field of study information. The final distributions of demographic groups are:


- • Gender: Man (79%); Woman, Non-Binary, Other (21%)
- • Race: White (61%); Non-White (39%)
- • Years of Research Experience: 11+ (57%); 4-10 (32%); 0-3 (11%)
- • Native Language: Native English (62%); Non-Native English (38%)
- • Field of Study: Computer Science (40%); Social Science & Humanities (24%); Natural Science & Engineering (21%); Biology & Medicine (15%)


Finally, we inspected our demographic data for correlation between certain demographic groups. For example, are a majority of the male participants also white? Given the demographic variables are categorical, we conduct a series of Chi-square tests of independence in R (chisq.test) between all pairs of the five demographic groups, with multiple comparisons 𝑝-value correction using Holm-Bonferroni (p.adjust). Results of the Chi-square tests can be found in Table 5 in Appendix A.9

We found that most variables appear independent, except for three pairs with significant 𝑝-values: race and years of experience, gender and field of study, and years of experience and field of study. In Table 1, we present contingency tables

9We previously also had another variable representing researcher experience—number of publications—but found that it was highly correlated with Years of research experience (Chisq Independence test; p-value = 3.3E-15).

Man Woman, Non-

Binary, Other White 243 74

Non-White 168 34

𝑝 = 0.7578 (a) Race and Gender

0-3 4-10 11+

White 27 96 198 Non-White 31 81 94

𝑝 = 0.0101 (b) Race and Years of Experience

CS Bio Nat.Sci Soc.Sci

Man 194 65 113 110 Woman, NonBinary, Other

48 22 12 40

𝑝 = 0.0008 (c) Gender and Years of Experience

CS Bio Nat.Sci Soc.Sci

0-3 37 6 11 12 4-10 102 30 39 35 11+ 118 58 82 105

𝑝 = 0.0030 (d) Years of Experience and Field of Study

Table 1. Contingency tables of participant counts for different demographic pairs. 𝑝-values from Chi-square tests of independence.

for these three demographic pairs alongside a fourth pair, race and gender, which appear un-associated. Interpreting these results, our dataset appears to have: (1) a high proportion of more senior white researchers; (2) more researchers who identified as men in the Natural Science & Engineering field, and (3) fewer senior researchers in the Computer Science field. These could be a combination of sampling bias or existing imbalance in these respective fields, as discussed in the limitations (section 3.1.3).

3.2.2 Statistical methods. Figure 1 provides a simplified diagram of an example of how our data looks per participant after completing all filtering and transformations. Each participant is labeled with (up to) five demographic categories. Each participant contributes (up to) 36 Likert ratings (an LLM Usage Frequency question and five LLM Perception questions, each repeated for six LLM Usage Types).

To address potentially correlated measurements arising from the same participants contributing multiple ratings, known as repeated measures, we employ linear mixed effects models to test the association between participant ratings (e.g., LLM usage frequency or perceptions) and participant demographic fixed-effects, while controlling for participantspecific effects. Such models are widely used in medicine [18] and behavioral sciences [21] for regression analysis with repeated measures and have also seen adoption in HCI research [9, 17, 32, 33]. In this work, we primarily use linear models of the form:

Rating ∼ Demographic + UsageType + (1|ParticipantID) (1)

For example, to measure the association between race and LLM usage, we regress participant usage (Rating) onto the race binary variable (Demographic), including additional control terms for the type of LLM usage (UsageType) as well as a random intercept term (1|ParticipantID) to capture participant-specific effects, such as when an individual has a tendency to give systematically higher or lower ratings. We can repeat this process for other demographic variables, for example swapping out race for gender or years of experience, to obtain different linear model fits.10 We fit

10In practice, we always attempt a second model fit that includes an interaction term between Usage Type and Demographic. We conduct a likelihood ratio test using anova() in R between each model against a null model which has no demographic variable (i.e., the null hypothesis of no demographic effects) and choose the interaction model if the interaction term is statistically significant; otherwise, we defer to the simpler model without an interaction term. In our analysis, we find that rarely is the interaction term needed.

![image 1](Liao et al._2024_LLMs as Research Tools A Large Scale Survey of Researchers' Usage and Perceptions_images/imageFile1.png)

Fig. 1. An example of data we collected per participant from sections of the survey that relate to our statistical modeling. Each participant provides answers to (up to) five demographic questions and (up to) 36 Likert ratings in response to questions about LLM usage frequency, perceptions, and usage types. Participants are not required to report on every question. In this example, the gender information is missing from the participant.

linear mixed effects models using lme4 in R, which also gives us 𝑝-values for significance tests on the estimated fixed effects associated with each demographic variable; we correct 𝑝-values for multiple comparisons across all these model fits using Holm-Bonferroni with p.adjust. Each of these models was fit on thousands of participant ratings, even accounting for missing data removal due to survey answers like “Unsure/Don’t Know” and “I haven’t used an LLM for this type of activity”; the final number of answers used in these regressions can be found in Table 3 in Appendix A. The significance tests from this analysis are used to address RQ2 (§4.2; Rating is for LLM Usage) and RQ3 (§4.3; Rating is for LLM Perception). For RQ4 (§4.4), we still fit a linear mixed effects model but use LLM Usage as the response variable and replace Demographic with LLM Perception.

While linear mixed effects models can help us test whether a given demographic is significantly associated with higher/lower LLM Usage or a certain LLM perception, we also want to know how individual levels within each demographic variable (e.g., White versus non-White) relate to the response variable. To do this, we conduct post hoc analyses of any significant model fit using emmeans() in R to measure and test pairwise differences in average Rating between levels in a Demographic variable holding all other variables (e.g., UsageType) constant. These pairwise comparison tests are used to address RQ5 (§4.5).

### 3.3 Qualitative Analysis of Free-Text Responses

To collect deeper insights beyond pre-defined multiple choices, several of the questions in our survey (Q64, 65, and 66) were paired with an optional free-text response question in which participants could elaborate and provide the reasoning behind their multiple-choice answers. To analyze these responses, we followed an iterative open thematic analysis approach [11, 19]. Specifically, three of the paper authors read through and coded the same subset of the responses into thematic categories independently. Then, the three authors meet with the entire research team to compare their codes and discuss their findings to settle on a final set of themes. Using the final set of themes, the three authors coded

![image 2](Liao et al._2024_LLMs as Research Tools A Large Scale Survey of Researchers' Usage and Perceptions_images/imageFile2.png)

- Fig. 2. Overview of Usage Frequency Divided by LLM Usage Type (N=816). The left diverging bar chart displays the distribution of usage frequency across different types of LLM usage, with each type represented by a separate row. The frequency levels, from left to right, are: Very Rarely, Rarely, Occasionally, Frequently, and Very Frequently, with the midpoint of the chart centered at "Occasionally." The grey bar chart on the right indicates the percentage of responses that report "Never" using LLMs for each corresponding type. From this plot, we can tell that researchers report using LLMs for Information Seeking and Editing most frequently, and for Data Cleaning & Analysis and Data Generation the least frequently.

![image 3](Liao et al._2024_LLMs as Research Tools A Large Scale Survey of Researchers' Usage and Perceptions_images/imageFile3.png)

- Fig. 3. LLM Usage Breakdown Under Each Usage Type (N=816). Each bar chart shows the number of participants who reported using LLMs for tasks that were subcategories of each usage type. Every participant could select multiple subcategories. The total number next to each title shows the number of participants who indicated using LLMs for the broad usage type.

the full of responses independently without replications (each response was annotated by one author). The full set of themes (one set per question), with definitions and examples, can be found in Appendix C.

- 4 Results 4.1 RQ1: What are the different ways researchers use LLMs in their research process today?


We asked participants to mark how frequently they used LLMs for each of six broad categories of research tasks. When considering their answers across all six categories, we find that LLMs are now a common tool for researchers, with a total of 80.88% (660 out of 816) of respondents adopting the use of LLMs somewhere in their research process. However, most usage today is still concentrated around tasks that have some connection to manuscript preparation,

from ideation and framing of arguments, to editing and writing of text, to gathering information for literature review. Still, some participants found many uses for LLMs; one prolific user reported using LLMs for “paper writing, analysis of data, results visualization, setting up new pipelines, ‘someone’ to talk to for methods development and when I’m stuck - I have found myself doing all of the same work but getting through my todo list much faster.”

Figure 2 shows the frequency of usage across all the respondents of our survey for our six high-level categories of LLM usage sorted by decreasing usage from left to right. As can be seen, there are major differences in usage across categories. 49% and 45% of our participants use LLMs for Information Seeking and Editing at least occasionally, respectively, while for categories related to data, such as Data Cleaning & Analysis and Data Generation, most respondents (69% and 73%, respectively) stated they never used LLMs for these tasks.

We also see differences in usage within each of these categories when we break down the ways LLMs can be used. We tally the number of people who selected if they have ever used LLMs to perform various tasks within each of the top-level categories and present the counts in Figure 3. The total referenced in each category is the number of respondents who stated they used LLMs for any of the tasks in the category, as well as an open-ended ‘Other’ option. Respondents were able to select multiple options within each category. More than a quarter of all respondents used LLMs for every one of the tasks under our Information Seeking category. However, by far the most frequent usage of LLMs is for rewriting text to fix grammar or awkward phrasings, as used by almost half of all respondents, under the Editing category. For the Data-related categories of usage, we see more usage in tasks relating to analysis and less usage in tasks related to simulation and synthetic data generation.

### 4.2 RQ2: How does the background of a researcher relate to the way they use LLMs?

Our second research question asks how usage varies according to the demographics, background, and other contextual factors related to the researcher. In Figure 4, the first column of heatmaps shows LLM usage frequency for each high-level category of LLM usage broken down by the five background characteristics that we surveyed.

Across all the LLM usage categories, we find that researchers’ racial identity significantly influenced the usage of LLMs, with Non-White researchers (𝜇 = 2.68, 𝜎 = 1.73) reporting more frequent usage of LLMs than White researchers

- (𝜇 = 2.06, 𝜎 = 1.52; 𝐸𝑠𝑡𝑖𝑚𝑎𝑡𝑒 = 0.616, 𝑝 < .0001). Finally, we note that for the specific category of using LLMs for editing, we see significantly greater usage by NNES (Non-native English-speaking) researchers (𝐸𝑠𝑡𝑖𝑚𝑎𝑡𝑒 = 0.5069,𝑝 < .0001), though this difference was not found for other categories of LLM usage, including using LLMs for direct writing.


### 4.3 RQ3: What are researchers’ perceptions of LLMs for usage in different parts of the research process?

We ask participants their perceptions of the benefits and risks of LLM usage, how acceptable they perceive the use LLMs to be (i.e., ethics), and their comfort with disclosing LLM usage to peers and reviewers for each category of LLM usage using Likert rating questions. We also asked participants to elaborate on their answers via open-ended free-response questions. In the final row of columns 2–6 of Figure 4, we present the average Likert rating given by participants to different questions of perceptions broken down by category of LLM usage.

- 4.3.1 Perceptions of LLM benefits. Overall, as seen in Figure 4, participants found greater benefits from LLM usage categories of Information Seeking (𝜇 = 3.2) and Editing (𝜇 = 3.4) compared to the remaining four categories (𝜇 ≤ 2.6). When we asked participants to elaborate on what specific benefits and usefulness they found, our analysis unveiled the following themes: language equity, other equity, efficiency, routine task assistance, search, literature review, editing, overcoming writer’s block, broadening perspectives, programming, and brainstorming. Most frequently mentioned


![image 4](Liao et al._2024_LLMs as Research Tools A Large Scale Survey of Researchers' Usage and Perceptions_images/imageFile4.png)

Fig. 4. Overview of our survey results (𝑁 is shown in Table 3), broken apart by demographic characteristics. Each heat map square represents the average rating of this demographic group on the usage frequency or perception for the particular type of LLM usage. The stars (***) are the significance levels of the differences indicated by p values from regression results. The brackets on the left indicate this difference is significant across all types of usage whereas the lines between squares indicate this difference is only significant for certain types of usage.

were editing, literature review, efficiency, and language equity. All of the themes are listed, along with descriptions and example quotations, in Table 7 in Appendix C.

Respondents stated they preferred using LLMs for smaller and routine tasks such as editing (“mostly rephrasing, rewriting, condensation, bulleting”) and programming (“basically code using CoPilot + GPT now, often for research glue code.”). These low-level uses were especially highlighted in the context of researchers facing systemic barriers, such as non-native English speakers, junior scholars, and researchers without much programming experience (“I am not a native English speaker, so LLMs help me with the language barrier.”). Overall, equity was a large theme in respondents’ discussions of the benefits of LLMs (“For honest researchers in resource-constrained developing countries, with little to no research funding, availability and use of LLMs is a game-changer leveling the playing field with other researchers in more fortunate climes.”).

Higher-level tasks were discussed by some users. For example, brainstorming (“LLMs are a great tool to help you create hypotheses, as a way to brainstorm, where there really are no wrong ideas and therefore you cannot suffer with any potential misleading information, as you are expected to have domain expertise anyway.”) and overcoming writer’s block (“The major benefit of using LLMs comes in action when we are stuck, for example not knowing the exact word or term, or not finding the answer to some of the ideas about how it can be used or how it can be applied.”). At the same time, such mentions were usually followed by caveats, such as: “You have to check everything it tells you, but it can be a useful starting place”.

- 4.3.2 Perceptions of LLM risks and ethical concerns. While LLMs have risks related to the quality of research conducted, researchers could also have ethical concerns separate from issues of quality. In order to distinguish risks from ethics, we first asked participants to rate on a Likert scale their perception of risks (1: not risky at all – 5: extremely risky), given known issues with LLMs today. Next, we asked their perception of the acceptability (1: Unacceptable


– 5: Acceptable) of using LLMs given a future where LLMs can prevent hallucinations and can always attribute any copyrighted text (if generated) to the original sources (i.e., their perception of the ethics of using LLMs).

Overall, as seen in Figure 4, we find that researchers perceive using LLMs for Editing as not risky (𝜇 = 2.5), Direct Writing as moderately risky (𝜇 = 3), and the remaining categories as very to extremely risky (𝜇 ≥ 3.2). In contrast when it came to ethics, researchers find Ideation & Framing (𝜇 = 2.9) and Data Cleaning & Analysis (𝜇 = 2.96) to be more on the unacceptable side, while the remaining categories were found to be more acceptable (𝜇 ≥ 3.4).

We asked one free-response question which gave participants the option to elaborate on risks and ethics together. Our thematic analysis of responses unveiled the following themes: hallucination and misinformation, inaccuracy, biases, lack of disclosure, plagiarism, disrespecting authorship, fabrication, decreasing creativity, pollution of the research ecosystem, decreasing diligence, and deskilling. Most frequently mentioned were hallucination and misinformation, plagiarism, fabrication, and decreasing diligence. All of the themes are listed, along with descriptions and example quotations, in Table 8 in Appendix C.

Qualitatively, based on the optional free-text responses, we found that our respondents have strong opinions about the risks and ethics of LLMs for research. They frequently use strong language to describe their positions (“LLMs are tools for automated plagiarism and data fabrication that pose an existential threat to the network of trust essential for the integrity of academic work and the proper attribution of credit”). While many point to specific risks like data fabrication (“the risk of reporting ‘results’ based on synthetic data without actually having conducted any experiment”) and plagiarism (“blind trust in a system that is hard to understand which could lead to accidental plagiarism”), others draw attention to higher level concerns that could affect all of academic research, such as pollution of the research ecosystem with low-quality work (“We need better judgment, slower science, and more thoughtful and ambitious work right now, not the opposite. Otherwise, we risk ridding science of its most special attributes just to crank out more papers.”).

Many respondents worried about future generations of researchers whose skills, diligence, and creativity might be impacted by over-reliance on LLMs (“The main general risk is to flatten on ‘average’, which is the worst thing that may happen for a researcher (and it is already happening for arts such music, since this would block innovation.”). Researchers also worried about exacerbating existing problems, such as overwhelming numbers of papers needing review (“I fear for a deluge of AI-‘assisted’ (in the best case) papers that read somewhat fluently but are shallow, unoriginal, uninteresting, wrong in the details. This will overwhelm the peer review system”).

- 4.3.3 Comfort with disclosure. Finally, we asked participants to rate on a Likert scale their comfort with disclosing the use of LLMs along different LLM usage categories (1: uncomfortable – 5: comfortable). Overall, as seen in Figure 4,


![image 5](Liao et al._2024_LLMs as Research Tools A Large Scale Survey of Researchers' Usage and Perceptions_images/imageFile5.png)

Fig. 5. Overview of the relation between usage frequency and perceptions of LLM. Each heatmap represents one type of perception, and each cell represents the number of responses (log scaled) that fall under this level of frequency of perception. The Kendall’s tau coefficient on the bottom indicates how strong the correlation is between the usage frequency and the perception of that usage. All perceptions are significantly correlated with usage (𝑝 < .0001). Tests performed using cor.test in R and corrected with p.adjust.

participants were comfortable with disclosing to both peers and reviewers across all LLM usage categories (disclose to peers: 𝜇 ≥ 3.4, disclose to reviewers: 𝜇 ≥ 3.2).

When it came to our qualitative results, participants’ opinions on the disclosure of LLM usage and proper attribution were discussed across multiple survey questions and our extracted themes, though respondents particularly discussed disclosure in response to the question about risks and ethical considerations. One respondent mentioned “academic shame” as a reason researchers might not disclose LLM usage. Other respondents highlighted the costs to the research community of not disclosing LLM usage: “[If researchers don’t disclose using LLM-generated text], I fear that researchers can get lazy, and we start having a lot of ‘repeated text’ in articles... and eventually researchers may just ask LLMs to generate the whole paper.” Some respondents listed this as their main concern with model-assisted research, and as long as LLM usage was disclosed, they found that usage acceptable: “The same sort of disclosure of use [as with human assistance] should be sufficient. The same responsibility for the integrity of work applies whether part of the effort was provided by a human assistant or an LLM.” Finally, one user called for better processes to support disclosure: “...universities have totally different policies. It would be good if there was a generic system of how to indicate that editing or drafting tools were used.”

### 4.4 RQ4: How does the way a researcher uses LLMs relate to their perceptions?

We find that people’s perceptions of risks, benefits, and ethics and their willingness to disclose usage of LLMs to the community all had a significant impact on their stated usage of LLMs (𝑝 < .0001). Figure 5 presents heatmaps showing the number of responses (log scaled) for each level of usage frequency and perception level. These values are summed across all six categories of LLM usage, i.e., each respondent is represented six times in each heatmap if they answered all questions about usage and perceptions. In addition, Table 4 in Appendix A presents the correlation between perceptions and frequency of LLM usage broken down by type of LLM usage.

Overall, as expected, we see that greater perceived risks and greater perceived ethical concerns are associated with lower usage, and greater perceived benefits are associated with higher usage. However, perceived benefits has the strongest correlation to usage (0.62, 𝑝 < .0001). As shown in Figure 5’s heatmaps, some who find few risks or ethical concerns with certain categories of usage still choose to use LLMs for them infrequently or not at all, potentially because they find little benefit. Indeed, when looking at Table 4 in the Appendix, we can see overall a weaker relationship between risk and frequency (-0.401, 𝑝 < .0001) and ethics and frequency (0.389, 𝑝 < .0001) compared to benefits. While this is also true for every category of LLM usage, in certain categories, risks and ethics have a stronger relationship with (non-)usage, such as Direct Writing.

ManWoman, Non-binary, Other 𝑝

Non-WhiteWhite 𝑝

11+ years0-3 years 𝑝

Benefit (1-5) 0.420 <.0001 -0.4187 0.0004 Ethics (1-5) 0.351 0.0017

Bio-CS 𝑝 CS-Soc.Sci 𝑝

Disclosure-Peers (1-5) -0.644 0.0001 0.513 0.0002 Disclosure-Reviewers (1-5) -0.622 0.0007 0.451 0.0043

Table 2. Post-hoc tests for significant pairwise differences in LLM perception ratings between demographic groups (Gender, Race, and Year on the first row, and Field of Study on the second), across all LLM usage types. This table reports the rating differences between demographic levels and associated 𝑝-values from emmeans. For example, in the column for race and the row for Benefit, the result shows that Non-White researchers, on average, report 0.42 points higher ratings than White researchers on the perceived benefits of LLM usage. Only statistically significant results are included in the table.

We find a weaker but positive relationship between comfort with disclosure and frequency of LLM usage. Looking

- at the heat maps, we see that the majority of researchers feel comfortable disclosing LLM usage to both their peers and reviewers regardless of their usage level, with the exception of those who never used LLMs for a given category, where a sizeable portion expressed discomfort. This suggests greater discomfort with disclosure, or more broadly lack of social norms around usage, could be one reason why some researchers do not wish to use LLMs for one or more categories of research.


### 4.5 RQ5: How does the background of a researcher relate to their perceptions?

In Figure 4, columns 2–6 show heat maps related to respondents’ perceptions of using LLMs across all six usage categories and broken down by respondents’ background. Table 2 also presents results of significance tests for differences.

- 4.5.1 Differences in perceptions of LLM benefits. We find that across all LLM usage categories, a researcher’s race and years of experience have a significant effect on their perception of the benefits of LLMs. Non-White researchers


- (𝜇 = 3.14, 𝜎 = 1.31) perceive more benefits in using LLMs for research than White researchers (𝜇 = 2.67, 𝜎 = 1.35), while junior researchers (𝜇 = 3.20, 𝜎 = 1.29) with 0–3 years of experience perceive more benefits than senior researchers (𝜇 = 2.76, 𝜎 = 1.38) with 11+ years of experience. Given our results regarding usage frequency across backgrounds (RQ2) and correlation between perceptions and usage (RQ3), this suggests that perceived utility is a primary driver of greater usage for non-White researchers and junior researchers. Similarly, we find that NNES researchers perceive greater benefits in using LLMs for Editing than native English-speaking researchers (𝐸𝑠𝑡𝑖𝑚𝑎𝑡𝑒 = 0.4187,𝑝 = 0.0004), in addition to actually using LLMs for Editing significantly more as well.

In general, the groups who reported perceiving more benefits are some of the groups who are traditionally less advantaged in the research community: non-White researchers, non-native English speakers, and researchers with the least experience. These findings support arguments that LLM usage can potentially play a role in improving research equity, echoing our qualitative results.

- 4.5.2 Differences in perceptions of LLM risks. Overall, there were few significant differences in how people of different backgrounds perceived the risks of LLMs across all the LLM usage categories. One exception was between White and non-White researchers, where non-White researchers perceive fewer risks in using LLMs for Data Cleaning & Analysis (𝐸𝑠𝑡𝑖𝑚𝑎𝑡𝑒 = −0.573,𝑝 < .0001), and Data Generation (𝐸𝑠𝑡𝑖𝑚𝑎𝑡𝑒 = −0.274,𝑝 = 0.0352) than White researchers. This


suggests that a perception of heightened risk may be what depresses White respondents’ usage of LLMs for these categories in addition to lower perceived benefits.

- 4.5.3 Differences in perceptions of the ethics of using LLMs. We find that across all LLM usage categories, a researcher’s gender has a significant effect on their perception of the ethics of using LLMs. Overall, researchers who identify as women, non-binary, and other genders (𝜇 = 3.24,𝜎 = 1.58) perceive LLM usage in research as less acceptable than those who identify as men (𝜇 = 3.6,𝜎 = 1.47) as shown in Table 2. This suggests that ethical concerns are a major driver for lower LLM usage for women and non-binary researchers compared to men, though the differences there in terms of usage were not significant.

We also find differences in ethical concerns across backgrounds according to specific LLM usage categories. Similarly to perceptions of risk, we find that non-White researchers perceive fewer ethical concerns compared to White researchers for the two LLM usage categories related to data (Data Cleaning & Analysis: 𝐸𝑠𝑡𝑖𝑚𝑎𝑡𝑒 = 0.4059,𝑝 = 0.0027, Data Generation: 𝐸𝑠𝑡𝑖𝑚𝑎𝑡𝑒 = 0.3066,𝑝 = 0.0230) as well as for Direct Writing (𝐸𝑠𝑡𝑖𝑚𝑎𝑡𝑒 = 0.3391,𝑝 = 0.0098). This suggests that differences in ethical concerns along with perceptions of risk and benefits may contribute to differences in White and non-White researchers’ LLM usage.

We also see differences in ethical concerns between more junior (4–10 years of experience) and more senior researchers (11+ years of experience) for the categories of Editing (𝐸𝑠𝑡𝑖𝑚𝑎𝑡𝑒 = 0.3385,𝑝 = 0.0215) and Data Cleaning & Analysis (𝐸𝑠𝑡𝑖𝑚𝑎𝑡𝑒 = 0.4578,𝑝 = 0.0013), where senior researchers have greater ethical concerns. This suggests that in addition to differences in perceptions of benefits, differences in ethical concerns may drive what differences there are in LLM usage between more junior and senior researchers, though the usage differences we find are not significant.

Finally, we find significant differences in perception of ethics across research fields for some LLM categories of usage. Computer science researchers on the whole have fewer ethical concerns than researchers in other fields. In particular, computer science researchers perceive using LLMs for Editing as more acceptable than social science & humanities researchers (𝐸𝑠𝑡𝑖𝑚𝑎𝑡𝑒 = 0.5706,𝑝 = 0.0008), and they also perceive Data Generation as more acceptable than natural science & engineering researchers (𝐸𝑠𝑡𝑖𝑚𝑎𝑡𝑒 = 0.5279,𝑝 = 0.0075). Despite not seeing greater usage of LLMs by computer scientists than researchers in other fields, it is possible that usage may yet be more normalized in computer science due to LLMs being a major topic of active research.

- 4.5.4 Differences in comfort with disclosure. We find that a researcher’s field of research has a significant effect on their comfort with disclosing usage of LLMs to peers and reviewers. In particular, computer scientists (To peers: 𝜇 = 4.07,𝜎 = 1.39; To reviewers: 𝜇 = 3.91,𝜎 = 1.47) are more comfortable disclosing LLM usage than social science & humanities (To peers: 𝜇 = 3.52,𝜎 = 1.57; To reviewers: 𝜇 = 3.42,𝜎 = 1.58) or biology & medicine researchers (To peers: 𝜇 = 3.37,𝜎 = 1.61; To reviewers: 𝜇 = 3.21,𝜎 = 1.65). This finding echoes our findings related to ethical concerns, which taken together further suggests greater acceptance in the computer science research community around the use of LLMs compared to other fields. Interestingly, we see no significant differences across other aspects of researcher background with regards to comfort with disclosure; indeed as mentioned earlier, people are mostly comfortable with disclosure to both peers and reviewers across all LLM categories of usage.


### 4.6 RQ6: How does the source of the LLM affect researchers’ perception and usage?

Participants were split on whether the source of an LLM, (i.e., non-profit versus pro-profit entities), impacted their perception of benefits and risks. 54.81% of participants (359) reported that their perception would change depending on the source of LLM while 45.19% (296) reported no difference. We also asked participants to optionally elaborate on their

selection in an open-ended question. From manual coding of responses, we found that 59.07% (228) of respondents expressed a preference for LLMs from open source/non-profit entities,11 while only 2.85% (11) stated they preferred LLMs from for-profit corporations, and 38.08% (147) did not express a preference either way in their free-response answer.

We also qualitatively coded responses for themes regarding why people preferred non-profit or for-profit entities behind LLMs; full results are shown in Table 6 in Appendix C. The top reasons participants preferred non-profit include the incentives of the organization, the transparency of the model, and ethical considerations for LLMs. These participants were skeptical of the incentives of commercial corporations, and worried that they would “exploit user input, manipulate LLM outputs for financial gain.” They also expressed concerns about monopolization, injecting bias to maximize profits, and other ethical issues. They favored non-profit entities because of the transparency in open-source models, increasing accountability and users’ trust.

From the few participants who actually favored LLMs from commercial corporations, they stated as a rationale that they believed those models were of higher quality due to the resources available to companies and their responsibility towards supporting customer issues. For participants who perceived no difference in the source of the LLMs, some held a neutral attitude that “the technology is the same” no matter which organization provided it. Some expressed that they cared more about the quality of the model, and they would use the model with the best quality regardless of its source. Finally, other participants questioned the boundary between for-profit and non-profit entities: “as we have seen with OpenAI, non-profits can easily become commercial.”

For some respondents, whether the model itself is open-source was more important than whether the LLM was created by a non-profit or for-profit entity. Other respondents expressed skepticism with the open-source label: “No LLM is really open source. Most of them owe their existence to big commercial corporations, and even if they share the weights, we don’t really know all the details about the training data. They are essentially black boxes.”

### 5 Discussion

Results from our survey showed widespread adoption of LLMs in the research community and provided detailed insights into the different ways researchers leverage LLMs in their workflows. We found that while LLMs offer the potential for enhancing equity and productivity, particularly benefiting those less advantaged in the research community, they also raise concerns about research integrity, quality, and potential homogenization of scholarly output. The varying levels of LLM usage and comfort levels with disclosure across disciplines and career stages highlight the ongoing negotiation of new social norms in academia.

### 5.1 Deep and Pervasive Integration of LLMs in Research

Our work revealed that many researchers have already found benefits in incorporating widely available LLM-based tools into their current workflow, from literature review to data analysis to writing assistance. This confirms and expands upon prior assumptions about the prevalence of LLM usage in academia [10, 31, 51, 53, 72]. While we did not set out to explore how researchers describe their relations with LLM-based research support tools, many in the free-form responses explicitly describe these tools with varying levels of autonomy and agency. More specifically, the ways participants described LLMs ranged from direct manipulation [81] (“just another tool in the toolbox”) to data sources (“a custom Wikipedia page”) to human-AI teaming [99] (“a useful research collaborator or assistant,”) to fully autonomous

11In the free response, some participants use open source and non-profit interchangeably. Thus, for the seek of labeling, we create a higher-level label of open source/non-profit to capture that opinion.

agents [82] (“an end-to-end AI researcher”), pointing to a wide design space of future LLM-based research support tools and user interfaces [58]. As researchers across AI and HCI domains continue to devote resources to developing new tooling [22, 27, 28, 31, 38, 43, 48, 59, 65, 68, 69, 87, 94], we may see increasing benefits in adopting LLM-based research support tools and a potential paradigm shift in how research is conducted in the future.

### 5.2 “A Game-changer Leveling the Field”: Equity Benefits of LLMs

An unexpected finding was the frequent mention of equity as one of the main benefits of using LLMs for research. Most frequently, non-native English speakers described how LLMs allowed them to “level the playing field” by cutting down “tedious and time-consuming editing tasks” to “more freely and precisely express ideas in another language [English].” Our quantitative findings in Section 4.2 also reveal that groups traditionally disadvantaged in research [64] (nonWhite, junior, non-native English speakers) find LLMs more beneficial and, in some cases, use them more frequently. Additionally, equity was mentioned in other contexts such as enabling researchers without technical programming training to generate code for data cleaning, improving understanding of technical papers and papers from less familiar fields, or replacing high-cost editing and proofreading services. For example, one neurodivergent participant pointed to how writing with LLMs allowed them to write more confidently and productively. This impact suggests that LLMs are beneficial for researchers from various marginalized backgrounds, helping them overcome systemic barriers including “knowledge abysses” and neo-colonial dynamics in research [29] — and gain deserved visibility in the global research community.

However, ethical concerns surrounding LLMs could potentially hinder their broader adoption, particularly among certain demographic groups. From the results in Section 4.5, we find that women and non-binary participants in our study expressed greater ethical concerns about LLM use and tend to use them less frequently (though not statistically significant). This pattern is particularly noteworthy given that women and non-binary researchers are traditionally disadvantaged groups in academia. If these researchers abstain from using LLMs due to ethical concerns and thus lose out on potential benefits or are shut out of potential collaborations, this could further exacerbate inequities. Future work should examine more deeply the specific ethical and other concerns expressed by traditionally disadvantaged groups and strive to address these concerns in future development of LLM-based research tools. For instance, given prior research showing women scientists often struggle to receive appropriate credit for their work [74, 77], women may be wary of using LLMs or attributing some aspect of their work to them. In our survey, we did not see definitive evidence of gender playing a role in LLM usage or comfort with disclosure, though future work could go beyond self-report data and personal perceptions to examine observational data or impacts of LLM attribution.

### 5.3 Productivity vs. Research Integrity

Despite claimed benefits in research productivity and equity, our survey also reveals significant concerns about the risks associated with LLM use in research. Hallucinations and misinformation were among the most frequently mentioned risks. Some participants used strong language, such as plagiarism and data fabrication, and others expressed fundamental concerns about the impact of LLMs on future generations of researchers, potentially affecting their skills, diligence, and creativity, which might result in the proliferation of low-quality research [10]. These concerns are reflected by academic organizations and funding agencies; for example, the NIH has cautioned against using LLMs for applications or reviews because it sacrifices the “originality of thought” and leads to homogenization of ideas or even research misconduct, subject to the severe penalty [56].

Interestingly, our survey showed that while disadvantaged groups are more likely to discuss benefits of LLMs, as discussed earlier, we observe few significant differences in perceptions of risks across different backgrounds. This suggests that the perception of risks appears to be more uniformly distributed across demographics. For example, the problem of hallucinations in LLM outputs appears to be an equally significant concern for all researchers. This shared understanding indicates a collective awareness of LLMs’ limitations and suggests the possibility of developing uniform standards for LLM use that can be broadly agreed upon, irrespective of people’s demographic characteristics.

### 5.4 Emerging Norms and Guidelines

Scholarly venues and research funding agencies have begun discussing the ban of LLMs in research or peer reviews [30, 42]. However, the ban on LLMs in research has been criticized as undesirable given its potential benefits and was unenforceable due to undisclosed use of LLMs [37]. The more realistic approach might be establishing guidelines about the ethical use of LLMs in scientific research. Several articles have proposed such guidelines. Watkins [96] created a peer-reviewers’ checklist for the use of LLM agents. Hosseini et al. [37] advocates for transparent disclosure of LLM use, including specific citation details, and inclusion of LLM interactions as supplementary material for reproducibility. Koller et al. [53] elicits best practices for using LLMs in various knowledge work scenarios such as viewing LLMs as aids rather than collaborators and engaging in post-processing of LLM-generated content to maintain a sense of ownership and control. In the context of software development research, Sallou et al. [79] outlines guidelines including providing reproducibility metadata and assessing output variability by performing multiple runs. These growing norms aim to promote transparency, reproducibility, and thoughtful integration of LLM as research tools while maintaining high standards of scientific rigor.

### 5.5 Weighing the Impacts of Mandatory LLM Disclosure in Academia

One of the most common approaches to establishing norms on LLMs in research is to increase transparency. Many conferences, publishers, and funding agencies have started to implement guidelines and restrictions for LLM use, and/or require researchers to disclose how LLM-based tools were used during research or grant writing [1–4, 40, 55, 75]. Our survey findings generally align with this trend, revealing that participants are broadly comfortable with disclosing LLM use to both peers and reviewers across all categories of usage. While we do not observe major differences in usage across fields, our study uncovered nuanced variations in comfort levels. Computer scientists reported significantly higher comfort with disclosure compared to researchers in social sciences & humanities or biology & medicine. This disparity reflects the evolving and unsettled nature of LLM use in research across different academic fields. While some disciplines may be moving towards accepting LLMs as standard research tools, others are still grappling with how to integrate these technologies into their established practices. The mention of “academic shame” by one respondent as a potential reason for non-disclosure highlights the ongoing stigmatization of LLM use in some research communities. The lack of standardized policies across institutions further complicates this landscape, creating additional burdens for individual researchers who must navigate varying expectations and norms. This suggests that the academic community is still collectively negotiating the norms of acceptable LLM use, and continued discussion is crucial to fully leverage new technologies to improve science while avoiding potential pitfalls.

### 5.6 Open-Source vs. Closed-Source LLMs

The debate between open-source and commercial LLMs adds another layer of complexity to their use in research. Our survey revealed that while commercial models are perceived to offer higher quality and better user support,

they also raise significant concerns about transparency, reproducibility, and more fundamentally, the misalignment of incentives between commercial entities and the research community. Many researchers, particularly those lacking technical expertise or computational resources, predominantly rely on commercial closed models [39, 90, 98]. However, this reliance comes with risks. For example, companies deprecating earlier versions of their hosted models12 could potentially render many thousands of published research papers significantly less reproducible [46]. This risk aligns with a growing consensus in the research community that open-source LLMs offer significant advantages for scientific work. Many researchers argue that the use of open-source models enhances the validity and integrity of research by allowing for greater scrutiny of research data and output [79, 90]. This stands in strong contrast to closed-source models that can be obscured behind opaque APIs; one notable example being the recent release of GPT-o1 model that hides parts of its generations from users.13 These concerns should be carefully examined in high-stakes research areas such as medicine, bioengineering, law, and public policy, which can have direct, real-world impacts [90]. In these fields, reproducibility and transparency are paramount, as they ensure the reliability of findings and provide necessary justification for decisions that affect people’s lives.

### 5.7 “Not Me, But Them”: Self vs. Peer Perceptions Discrepancy

Our study reveals an interesting discrepancy in how researchers perceive their own use of LLMs versus that of other scholars. Researchers appear to trust their own judgment in using LLMs for limited, low-risk tasks, while expressing concerns about more extensive or inappropriate use by others. This mismatch between stated fears and reported personal usage is exemplified by responses such as, “I’m afraid other people will use models to write papers but I only report using it for editing.” This phenomenon aligns with established concepts in social psychology and media studies: the “above-average effect” [54], where individuals tend to view themselves as superior to their peers, and the “third-person effect” [23], which describes how people often believe they are less susceptible to media influence than others. This perception might facilitate the establishment of community-wide norms for LLM use as researchers may be more receptive to stricter guidelines, believing that while they have already implemented self-regulation, others in the community require more oversight.

### 6 Conclusion

In this study, we ran a large-scale survey of diverse groups of researchers, soliciting information about their usage of LLMs for their work as well as their perceptions of LLM usage by other researchers. Our study provides lessons about the changing social norms across different academic disciplines and demographic groups, and we found significant differences in responses between these groups. Researchers reported widespread adoption of LLMs in their work, with 80.9% of surveyed researchers using them, primarily for information seeking and editing tasks. Non-White researchers, junior scholars, and non-native English speakers reported using LLMs more frequently and perceiving greater benefits, suggesting LLMs may help level the academic playing field. However, researchers who identified as women, non-binary, or other genders expressed greater ethical concerns about LLM usage. While perceived benefits strongly correlate with usage frequency, researchers also acknowledge significant risks, including hallucinations, misinformation, plagiarism, and potential long-term impacts on research quality and creativity. The majority of respondents prefer LLMs from open-source and non-profit entities, citing better incentive structures, transparency, and ethical considerations.

- 12“As we launch safer and more capable models, we regularly retire older models. Software relying on OpenAI models may need occasional updates to keep working.” https://platform.openai.com/docs/deprecations
- 13“Each completion has an upper limit on the maximum number of output tokens—this includes both the invisible reasoning tokens and the visible completion tokens.” https://platform.openai.com/docs/guides/reasoning


Collectively, our work suggests that the research community is at a critical juncture, grappling with upholding fundamental values of originality, rigor, and ethical conduct in academia. As Brinkmann et al. [12] terms it, we are currently shaping “Machine Culture,” where technologies like LLMs serve as cultural mediators and generators, capable of transforming cultural evolutionary processes. As we continue to progress on both the capability of LLMs and LLM-based research support tools to provide greater benefits, the integration of LLMs into research practices is also likely to continue to increase in both depth and breadth. This represents a significant shift in this cultural evolution, with the potential to pose risks to research integrity and the development of critical thinking skills among researchers or, if carefully managed, contribute to a more productive, diverse and inclusive global research community. Our findings underscore the need to better understand the implications of LLM use across various research contexts. We should explore not only the technical aspects of LLM integration but also its sociological, ethical, and epistemological impacts on different disciplines and researchers’ demographic backgrounds. We call for studies that examine the long-term effects of LLM use on research quality, creativity, and the development of research skills as well as investigations into the potential of LLMs to increase fairness and representation in academia.

### Acknowledgments

The authors would like to thank our many anonymous survey respondents who provided long and thoughtful opinions and insights in the optional free-text survey questions. These responses enabled our qualitative analysis and showcased that many researchers are actively contemplating and engaging in conversations around the use of LLMs as a research support tool today.

### References

- [1] 2023. Writing the rules in AI-assisted writing. Nature Machine Intelligence 5 (2023), 469 – 469. https://api.semanticscholar.org/CorpusID:258846433
- [2] AAAI. 2024. Policy on use of AI systems in producing AAAI or AAAI-related publications. Retrieved September 6, 2024 from https://aaai.org/aaaipublications/aaai-publication-policies-guidelines/
- [3] ACL. 2024. ACL 2023 Policy on AI Writing Assistance. Retrieved September 6, 2024 from https://2023.aclweb.org/blog/ACL-2023-policy/
- [4] ACM. 2024. ACM Policy on Authorship. Retrieved September 6, 2024 from https://www.acm.org/publications/policies/frequently-asked-questions
- [5] Sayed Fayaz Ahmad, Heesup Han, Muhammad Mansoor Alam, Mohd. Khairul Rehmat, Muhammad Irshad, Marcelo Arraño-Muñoz, and Antonio Ariza-Montes. 2023. Impact of artificial intelligence on human loss in decision making, laziness and safety in education. Humanities and Social Sciences Communications 10, 1 (June 2023), 311. https://doi.org/10.1057/s41599-023-01787-8
- [6] Hussam Alkaissi and Samy I McFarlane. 2023. Artificial hallucinations in ChatGPT: implications in scientific writing. Cureus 15, 2 (2023).
- [7] Amanda Alvarez, Aylin Caliskan, MJ Crockett, Shirley S Ho, Lisa Messeri, and Jevin West. 2024. Science communication with generative AI. Nature Human Behaviour 8, 4 (2024), 625–627.
- [8] Maria Antoniak, Aakanksha Naik, Carla S. Alvarado, Lucy Lu Wang, and Irene Y. Chen. 2024. NLP for Maternal Healthcare: Perspectives and Guiding Principles in the Age of LLMs. In Proceedings of the 2024 ACM Conference on Fairness, Accountability, and Transparency (FAccT ’24). Association for Computing Machinery, New York, NY, USA, 1446–1463. https://doi.org/10.1145/3630106.3658982
- [9] Tal August, Lucy Lu Wang, Jonathan Bragg, Marti A. Hearst, Andrew Head, and Kyle Lo. 2023. Paper Plain: Making Medical Research Papers Approachable to Healthcare Consumers with Natural Language Processing. ACM Transactions of Computer-Human Interaction (TOCHI) (2023). https://doi.org/10.1145/3589955
- [10] Christopher A. Bail. 2024. Can Generative AI improve social science? Proceedings of the National Academy of Sciences 121, 21 (2024), e2314021121.
- [11] Richard E. Boyatzis. 1998. Transforming Qualitative Information: Thematic Analysis and Code Development.
- [12] Levin Brinkmann, Fabian Baumann, Jean-François Bonnefon, Maxime Derex, Thomas F. Müller, Anne-Marie Nussberger, Agnieszka Czaplicka, Alberto Acerbi, Thomas L. Griffiths, Joseph Henrich, Joel Z. Leibo, Richard McElreath, Pierre-Yves Oudeyer, Jonathan Stray, and Iyad Rahwan. 2023. Machine culture. Nature Human Behaviour 7, 11 (Nov. 2023), 1855–1868. https://doi.org/10.1038/s41562-023-01742-2
- [13] Vannevar Bush. 1945. As we may think. Atlantic Monthly, July (1945).
- [14] Davide Castelvecchi. 2024. Researchers built an ‘AI Scientist’ — what can it do? Nature News (2024). https://doi.org/10.1038/d41586-024-02842-3
- [15] Davide Castelvecchi. 2024. Researchers built an’AI Scientist’-what can it do? Nature (2024).
- [16] Eric Chamoun, Michael Schlichtkrull, and Andreas Vlachos. 2024. Automated Focused Feedback Generation for Scientific Writing Assistance. In Findings of the Association for Computational Linguistics ACL 2024, Lun-Wei Ku, Andre Martins, and Vivek Srikumar (Eds.). Association for


- Computational Linguistics, Bangkok, Thailand and virtual meeting, 9742–9763. https://aclanthology.org/2024.findings-acl.580
- [17] Joseph Chee Chang, Amy X Zhang, Jonathan Bragg, Andrew Head, Kyle Lo, Doug Downey, and Daniel S Weld. 2023. Citesee: Augmenting citations in scientific papers with persistent and personalized historical context. In Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems. 1–15.
- [18] Avital Cnaan, Nan M. Laird, and Peter Slasor. 1997. Using the general linear mixed model to analyse unbalanced repeated measures and longitudinal data. Statistics in medicine 16 20 (1997), 2349–80. https://api.semanticscholar.org/CorpusID:262990589
- [19] Lynne M. Connelly. 2013. Grounded theory. Medsurg nursing : official journal of the Academy of Medical-Surgical Nurses 22 2 (2013), 124, 127.
- [20] Consensus. 2024. Consensus - AI Powered Academic Search Engine. Retrieved September 6, 2024 from https://consensus.app/
- [21] Robert A. Cudeck. 1996. Mixed-effects Models in the Study of Individual Differences with Repeated Measures Data. Multivariate behavioral research 31 3 (1996), 371–403. https://api.semanticscholar.org/CorpusID:23954316
- [22] Mike D’Arcy, Tom Hope, Larry Birnbaum, and Doug Downey. 2024. Marg: Multi-agent review generation for scientific papers. arXiv preprint arXiv:2401.04259 (2024).
- [23] W. Phillips Davison. 1983. The Third-Person Effect in Communication. Public Opinion Quarterly 47, 1 (Jan. 1983), 1–15. https://doi.org/10.1086/268763
- [24] Fiona Draxler, Daniel Buschek, Mikke Tavast, Perttu Hämäläinen, Albrecht Schmidt, Juhi Kulshrestha, and Robin Welsch. 2023. Gender, Age, and Technology Education Influence the Adoption and Appropriation of LLMs. arXiv:2310.06556 [cs.CY] https://arxiv.org/abs/2310.06556
- [25] Elicit. 2024. Elicit - The AI Research Assistant. Retrieved September 6, 2024 from https://elicit.com/
- [26] Benedikt Fecher, Marcel Hebing, Melissa Laufer, Jörg Pohle, and Fabian Sofsky. 2023. Friend or Foe? Exploring the Implications of Large Language Models on the Science System. ArXiv abs/2306.09928 (2023). https://api.semanticscholar.org/CorpusID:259187647
- [27] Raymond Fok, Joseph Chee Chang, Tal August, Amy X Zhang, and Daniel S Weld. 2023. Qlarify: Bridging scholarly abstracts and papers with recursively expandable summaries. arXiv preprint arXiv:2310.07581 (2023).
- [28] Katy Ilonka Gero, Vivian Liu, and Lydia Chilton. 2022. Sparks: Inspiration for science writing using language models. In Proceedings of the 2022 ACM Designing Interactive Systems Conference. 1002–1019.
- [29] David Rodríguez Goyes and May-Len Skilbrei. 2023. Rich scholar, poor scholar: inequalities in research capacity, “knowledge” abysses, and the value of unconventional approaches to research. Crime, Law and Social Change (2023). https://api.semanticscholar.org/CorpusID:259644345
- [30] Jack Grove. 2023. Science journals overturn ban on ChatGPT-authored papers. Times Higher Education (THE) (Nov. 2023). https://www. timeshighereducation.com/news/science-journals-overturn-ban-chatgpt-authored-papers
- [31] Dritjon Gruda. 2024. Three ways ChatGPT helps me in my academic writing. Nature (April 2024). https://doi.org/10.1038/d41586-024-01042-3 Bandiera_abtest: a Cg_type: Career Column publisher: Nature Publishing Group Subject_term: Careers, Machine learning, Authorship, Peer review, Publishing.
- [32] Andrew Head, Kyle Lo, Dongyeop Kang, Raymond Fok, Sam Skjonsberg, Daniel S. Weld, and Marti A. Hearst. 2021. Augmenting Scientific Papers with Just-in-Time, Position-Sensitive Definitions of Terms and Symbols. In CHI. https://doi.org/10.1145/3411764.3445648
- [33] Marti A. Hearst, Emily Pedersen, Lekha Priya Patil, Elsie Lee, Paul Laskowski, and Steven L. Franconeri. 2019. An Evaluation of Semantically Grouped Word Cloud Designs. IEEE Transactions on Visualization and Computer Graphics 26 (2019), 2748–2761. https://api.semanticscholar.org/CorpusID: 78094946
- [34] Will Douglas Heaven. 2022. Why Meta’s latest large language model survived only three days online. MIT Technology Review (Nov. 2022). https://www.technologyreview.com/2022/11/18/1063487/meta-large-language-model-ai-only-survived-three-days-gpt-3-science/
- [35] Luke Holman, Devi Stuart-Fox, and Cindy E. Hauser. 2018. The gender gap in science: How long until women are equally represented? PLOS Biology 16, 4 (04 2018), 1–20. https://doi.org/10.1371/journal.pbio.2004956
- [36] Allison L. Hopkins, James W. Jawitz, Christopher McCarty, Alex Goldman, and Nandita B. Basu. 2013. Disparities in publication patterns by gender, race and ethnicity based on a survey of a random sample of authors. Scientometrics 96 (2013), 515–534. https://api.semanticscholar.org/CorpusID: 13821749
- [37] Mohammad Hosseini, David B Resnik, and Kristi Holmes. 2023. The ethics of disclosing the use of artificial intelligence tools in writing scholarly manuscripts. Research Ethics 19, 4 (Oct. 2023), 449–465. https://doi.org/10.1177/17470161231180449
- [38] Chao-Chun Hsu, Erin Bransom, Jenna Sparks, Bailey Kuehl, Chenhao Tan, David Wadden, Lucy Lu Wang, and Aakanksha Naik. 2024. CHIME: LLMAssisted Hierarchical Organization of Scientific Studies for Literature Review Support. arXiv:2407.16148 [cs.CL] https://arxiv.org/abs/2407.16148
- [39] Zak Hussain, Marcel Binz, Rui Mata, and Dirk U. Wulff. 2023. A tutorial on open-source large language models for behavioral science. OSF (Dec. 2023). https://doi.org/10.31234/osf.io/f7stn
- [40] IEEE. 2024. IEEE Guidelines for Generative AI Usage. Retrieved September 6, 2024 from https://www.ieee-ras.org/publications/guidelines-forgenerative-ai-usage
- [41] Maurice Jakesch, Zana Buçinca, Saleema Amershi, and Alexandra Olteanu. 2022. How Different Groups Prioritize Ethical Values for Responsible AI. In Proceedings of the 2022 ACM Conference on Fairness, Accountability, and Transparency (Seoul, Republic of Korea) (FAccT ’22). Association for Computing Machinery, New York, NY, USA, 310–323. https://doi.org/10.1145/3531146.3533097
- [42] Jocelyn Kaiser. 2023. Science funding agencies say no to using AI for peer review. Science (July 2023). https://www.science.org/content/article/ science-funding-agencies-say-no-using-ai-peer-review
- [43] Hyeonsu B Kang, Tongshuang Wu, Joseph Chee Chang, and Aniket Kittur. 2023. Synergi: A Mixed-Initiative System for Scholarly Synthesis and Sensemaking. In Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology. 1–19.


- [44] Shivani Kapania, Ruiyi Wang, Toby Jia-Jun Li, Tianshi Li, and Hong Shen. 2024. " I’m categorizing LLM as a productivity tool": Examining ethics of LLM use in HCI research practices. arXiv preprint arXiv:2403.19876 (2024).
- [45] Sayash Kapoor, Rishi Bommasani, Kevin Klyman, Shayne Longpre, Ashwin Ramaswami, Peter Cihon, Aspen Hopkins, Kevin Bankston, Stella Biderman, Miranda Bogen, Rumman Chowdhury, Alex Engler, Peter Henderson, Yacine Jernite, Seth Lazar, Stefano Maffulli, Alondra Nelson, Joelle Pineau, Aviya Skowron, Dawn Song, Victor Storchan, Daniel Zhang, Daniel E. Ho, Percy Liang, and Arvind Narayanan. 2024. On the Societal Impact of Open Foundation Models. arXiv:2403.07918 (Feb. 2024). https://doi.org/10.48550/arXiv.2403.07918 arXiv:2403.07918 [cs].
- [46] Sayash Kapoor and Arvind Narayanan. 2023. OpenAI’s policies hinder reproducible research on language models. AI Snake Oil (March 2023). https://www.aisnakeoil.com/p/openais-policies-hinder-reproducible
- [47] Luoma Ke, Song Tong, Peng Cheng, and Kaiping Peng. 2024. Exploring the Frontiers of LLMs in Psychological Applications: A Comprehensive Review. ArXiv abs/2401.01519 (2024). https://api.semanticscholar.org/CorpusID:266741775
- [48] Jeongyeon Kim, Sangho Suh, Lydia B Chilton, and Haijun Xia. 2023. Metaphorian: leveraging large language models to support extended metaphor creation for science writing. In Proceedings of the 2023 ACM Designing Interactive Systems Conference. 115–135.
- [49] Aniket Kittur, Ed H Chi, and Bongwon Suh. 2008. Crowdsourcing user studies with Mechanical Turk. In Proceedings of the SIGCHI conference on human factors in computing systems. 453–456.
- [50] Aniket Kittur, Jeffrey V Nickerson, Michael Bernstein, Elizabeth Gerber, Aaron Shaw, John Zimmerman, Matt Lease, and John Horton. 2013. The future of crowd work. In Proceedings of the 2013 conference on Computer supported cooperative work. 1301–1318.
- [51] Dmitry Kobak, Rita González-Márquez, Emőke-Ágnes Horvát, and Jan Lause. 2024. Delving into ChatGPT usage in academic writing through excess vocabulary. arXiv:2406.07016 (July 2024). https://doi.org/10.48550/arXiv.2406.07016 arXiv:2406.07016 [cs].
- [52] Charlotte Kobiella, Yarhy Said Flores López, Franz Waltenberger, Fiona Draxler, and Albrecht Schmidt. 2024. “If the Machine Is As Good As Me, Then What Use Am I?” – How the Use of ChatGPT Changes Young Professionals’ Perception of Productivity and Accomplishment. In Proceedings of the CHI Conference on Human Factors in Computing Systems (CHI ’24). Association for Computing Machinery, New York, NY, USA, 1–16. https://doi.org/10.1145/3613904.3641964
- [53] Daphne Koller, Andrew Beam, Arjun Manrai, Euan Ashley, Xiaoxuan Liu, Judy Gichoya, Chris Holmes, James Zou, Noa Dagan, Tien Y Wong, et al.

2023. Why we support and encourage the use of large language models in NEJM AI submissions. , AIe2300128 pages.

- [54] Arie W Kruglanski and Ofra Mayseless. 1990. Classic and current social comparison research: Expanding the perspective. Psychological bulletin 108, 2 (1990), 195.
- [55] Jethro C. C. Kwong, Serena C. Y. Wang, Grace Nickel, Giovanni E. Cacciamani, and Joseph C. Kvedar. 2024. The long but necessary road to responsible use of large language models in healthcare research. NPJ Digital Medicine 7 (2024). https://api.semanticscholar.org/CorpusID:270972690
- [56] Mike Lauer, Stephanie Constant, and Amy Wernimont. 2023. Using AI in Peer Review Is a Breach of Confidentiality. NIH Extramural Nexus (June 2023). https://nexus.od.nih.gov/all/2023/06/23/using-ai-in-peer-review-is-a-breach-of-confidentiality/
- [57] Edith Law, Krzysztof Z Gajos, Andrea Wiggins, Mary L Gray, and Alex Williams. 2017. Crowdsourcing as a tool for research: Implications of uncertainty. In Proceedings of the 2017 ACM conference on computer supported cooperative work and social computing. 1544–1561.
- [58] Mina Lee, Katy Ilonka Gero, John Joon Young Chung, Simon Buckingham Shum, Vipul Raheja, Hua Shen, Subhashini Venugopalan, Thiemo Wambsganss, David Zhou, Emad A. Alghamdi, Tal August, Avinash Bhat, Madiha Zahrah Choksi, Senjuti Dutta, Jin L.C. Guo, Md Naimul Hoque, Yewon Kim, Simon Knight, Seyed Parsa Neshaei, Antonette Shibani, Disha Shrivastava, Lila Shroff, Agnia Sergeyuk, Jessi Stark, Sarah Sterman, Sitong Wang, Antoine Bosselut, Daniel Buschek, Joseph Chee Chang, Sherol Chen, Max Kreminski, Joonsuk Park, Roy Pea, Eugenia Ha Rim Rho, Zejiang Shen, and Pao Siangliulue. 2024. A Design Space for Intelligent and Interactive Writing Assistants. In Proceedings of the CHI Conference on Human Factors in Computing Systems (Honolulu, HI, USA) (CHI ’24). Association for Computing Machinery, New York, NY, USA, Article 1054, 35 pages. https://doi.org/10.1145/3613904.3642697
- [59] Yoonjoo Lee, Hyeonsu B Kang, Matt Latzke, Juho Kim, Jonathan Bragg, Joseph Chee Chang, and Pao Siangliulue. 2024. PaperWeaver: Enriching Topical Paper Alerts by Contextualizing Recommended Papers with User-collected Papers. In Proceedings of the CHI Conference on Human Factors in Computing Systems. 1–19.
- [60] Jenny T. Liang, Chenyang Yang, and Brad A. Myers. 2024. A Large-Scale Survey on the Usability of AI Programming Assistants: Successes and Challenges. In Proceedings of the IEEE/ACM 46th International Conference on Software Engineering (Lisbon, Portugal) (ICSE ’24). Association for Computing Machinery, New York, NY, USA, Article 52, 13 pages. https://doi.org/10.1145/3597503.3608128
- [61] Weixin Liang, Yuhui Zhang, Hancheng Cao, Binglu Wang, Daisy Yi Ding, Xinyu Yang, Kailas Vodrahalli, Siyu He, Daniel Scott Smith, Yian Yin, Daniel A. McFarland, and James Zou. 2024. Can Large Language Models Provide Useful Feedback on Research Papers? A Large-Scale Empirical Analysis. NEJM AI 1, 8 (July 2024), AIoa2400196. https://doi.org/10.1056/AIoa2400196
- [62] Weixin Liang, Yaohui Zhang, Zhengxuan Wu, Haley Lepp, Wenlong Ji, Xuandong Zhao, Hancheng Cao, Sheng Liu, Siyu He, Zhi Huang, Diyi Yang, Christopher Potts, Christopher D. Manning, and James Y. Zou. 2024. Mapping the Increasing Use of LLMs in Scientific Papers. ArXiv abs/2404.01268

(2024). https://api.semanticscholar.org/CorpusID:268857142

- [63] Andreas Liesenfeld and Mark Dingemanse. 2024. Rethinking open source generative AI: open-washing and the EU AI Act. In Proceedings of the 2024 ACM Conference on Fairness, Accountability, and Transparency (Rio de Janeiro, Brazil) (FAccT ’24). Association for Computing Machinery, New York, NY, USA, 1774–1787. https://doi.org/10.1145/3630106.3659005
- [64] Sebastian Linxen, Christian Sturm, Florian Brühlmann, Vincent Cassau, Klaus Opwis, and Katharina Reinecke. 2021. How weird is CHI?. In Proceedings of the 2021 chi conference on human factors in computing systems. 1–14.


- [65] Yiren Liu, Si Chen, Haocong Cheng, Mengxia Yu, Xiao Ran, Andrew Mo, Yiliu Tang, and Yun Huang. 2024. How AI Processing Delays Foster Creativity: Exploring Research Question Co-Creation with an LLM-based Agent. In Proceedings of the CHI Conference on Human Factors in Computing Systems (Honolulu, HI, USA) (CHI ’24). Association for Computing Machinery, New York, NY, USA, Article 17, 25 pages. https: //doi.org/10.1145/3613904.3642698
- [66] Yihe Liu, Anushk Mittal, Diyi Yang, and Amy Bruckman. 2022. Will AI console me when I lose my pet? Understanding perceptions of AI-mediated email writing. In Proceedings of the 2022 CHI conference on human factors in computing systems. 1–13.
- [67] Zhijie Liu, Yutian Tang, Xiapu Luo, Yuming Zhou, and Liang Feng Zhang. 2024. No Need to Lift a Finger Anymore? Assessing the Quality of Code Generation by ChatGPT. IEEE Transactions on Software Engineering 50, 6 (2024), 1548–1584. https://doi.org/10.1109/TSE.2024.3392499
- [68] Kyle Lo, Joseph Chee Chang, Andrew Head, Jonathan Bragg, Amy X Zhang, Cassidy Trier, Chloe Anastasiades, Tal August, Russell Authur, Danielle Bragg, et al. 2023. The semantic reader project: Augmenting scholarly documents through ai-powered interactive reading interfaces. arXiv preprint arXiv:2303.14334 (2023).
- [69] Tao Long, Dorothy Zhang, Grace Li, Batool Taraif, Samia Menon, Kynnedy Simone Smith, Sitong Wang, Katy Ilonka Gero, and Lydia B Chilton.

2023. Tweetorial hooks: generative AI tools to motivate science on social media. arXiv preprint arXiv:2305.12265 (2023).

- [70] Benjamin S. Manning, Kehang Zhu, and John J. Horton. 2024. Automated Social Science: Language Models as Scientist and Subjects. SSRN Electronic Journal (2024). https://api.semanticscholar.org/CorpusID:269214124
- [71] Lisa Messeri and MJ Crockett. 2024. Artificial intelligence and illusions of understanding in scientific research. Nature 627, 8002 (2024), 49–58.
- [72] Meredith Ringel Morris. 2023. Scientists’ Perspectives on the Potential for Generative AI in their Fields. arXiv preprint arXiv:2304.01420 (2023).
- [73] Amanda K Newendorp, Mohammadamin Sanaei, Arthur J Perron, Hila Sabouni, Nikoo Javadpour, Maddie Sells, Katherine Nelson, Michael Dorneich, and Stephen B Gilbert. 2024. Apple’s Knowledge Navigator: Why Doesn’t that Conversational Agent Exist Yet?. In Proceedings of the CHI Conference on Human Factors in Computing Systems. 1–14.
- [74] Chaoqun Ni, Elise Smith, Haimiao Yuan, Vincent Larivière, and Cassidy R Sugimoto. 2021. The gendered nature of authorship. Science advances 7, 36 (2021), eabe4639.
- [75] National Institutes of Health. 2024. The Use of Generative Artificial Intelligence Technologies is Prohibited for the NIH Peer Review Process. Retrieved September 11, 2024 from https://grants.nih.gov/grants/guide/notice-files/NOT-OD-23-149.html
- [76] Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, John Schulman, Jacob Hilton, Fraser Kelton, Luke Miller, Maddie Simens, Amanda Askell, Peter Welinder, Paul Christiano, Jan Leike, and Ryan Lowe. 2022. Training language models to follow instructions with human feedback. arXiv:2203.02155 [cs.CL] https://arxiv.org/abs/2203.02155
- [77] Matthew B Ross, Britta M Glennon, Raviv Murciano-Goroff, Enrico G Berkes, Bruce A Weinberg, and Julia I Lane. 2022. Women are credited less in science than men. Nature 608, 7921 (2022), 135–145.
- [78] Giuseppe Russo, Manoel Horta Ribeiro, Tim R. Davidson, Veniamin Veselovsky, and Robert West. 2024. The AI Review Lottery: Widespread AIAssisted Peer Reviews Boost Paper Scores and Acceptance Rates. ArXiv abs/2405.02150 (2024). https://api.semanticscholar.org/CorpusID:269587773
- [79] June Sallou, Thomas Durieux, and Annibale Panichella. 2024. Breaking the Silence: the Threats of Using LLMs in Software Engineering. In Proceedings of the 2024 ACM/IEEE 44th International Conference on Software Engineering: New Ideas and Emerging Results (ICSE-NIER’24). Association for Computing Machinery, New York, NY, USA, 102–106. https://doi.org/10.1145/3639476.3639764
- [80] FutureHouse. Sam Rodriques. 2024. FutureHouse - Announcing FutureHouse. Retrieved September 9, 2024 from https://www.futurehouse.org/ articles/announcing-future-house
- [81] Ben Shneiderman. 1982. The future of interactive systems and the emergence of direct manipulation. Behaviour & Information Technology 1, 3

(1982), 237–256.

- [82] Ben Shneiderman and Pattie Maes. 1997. Direct manipulation vs. interface agents. Interactions 4, 6 (nov 1997), 42–61. https://doi.org/10.1145/ 267505.267514
- [83] Chandan Singh, Jeevana Priya Inala, Michel Galley, Rich Caruana, and Jianfeng Gao. 2024. Rethinking Interpretability in the Era of Large Language Models. arXiv:2402.01761 (Jan. 2024). https://doi.org/10.48550/arXiv.2402.01761 arXiv:2402.01761 [cs].
- [84] Luca Soldaini, Rodney Kinney, Akshita Bhagia, Dustin Schwenk, David Atkinson, Russell Authur, Ben Bogin, Khyathi Chandu, Jennifer Dumas, Yanai Elazar, et al. 2024. Dolma: An open corpus of three trillion tokens for language model pretraining research. arXiv preprint arXiv:2402.00159

(2024).

- [85] Pragya Srivastava, Manuj Malik, Vivek Gupta, Tanuja Ganu, and Dan Roth. 2024. Evaluating LLMs’ Mathematical Reasoning in Financial Document Question Answering. In Findings of the Association for Computational Linguistics ACL 2024, Lun-Wei Ku, Andre Martins, and Vivek Srikumar (Eds.). Association for Computational Linguistics, Bangkok, Thailand and virtual meeting, 3853–3878. https://aclanthology.org/2024.findings-acl.231
- [86] Jan-Philipp Stein, Tanja Messingschlager, Timo Gnambs, Fabian Hutmacher, and Markus Appel. 2024. Attitudes towards AI: measurement and associations with personality. Scientific Reports 14 (2024). https://api.semanticscholar.org/CorpusID:267498881
- [87] Lu Sun, Stone Tao, Junjie Hu, and Steven P Dow. 2024. MetaWriter: Exploring the Potential and Perils of AI Writing Support in Scientific Peer Review. Proceedings of the ACM on Human-Computer Interaction 8, CSCW1 (2024), 1–32.
- [88] Ross Taylor, Marcin Kardas, Guillem Cucurull, Thomas Scialom, Anthony Hartshorn, Elvis Saravia, Andrew Poulton, Viktor Kerkez, and Robert Stojnic. 2022. Galactica: A Large Language Model for Science. arXiv:2211.09085 (Nov. 2022). https://doi.org/10.48550/arXiv.2211.09085 arXiv:2211.09085 [cs, stat].


- [89] Nga Than, Leanne Fan, Tina Law, Laura K. Nelson, and Leslie McCall. 2024. Updating “The Future of Coding”: Comparing Generative Large Language Models to Other Text Analysis Methods. (Aug. 2024). https://doi.org/10.31235/osf.io/wg82k
- [90] Augustin Toma, Senthujan Senkaiahliyan, Patrick R. Lawler, Barry Rubin, and Bo Wang. 2023. Generative AI could revolutionize health care — but not if control is ceded to big tech. Nature 624, 7990 (Dec. 2023), 36–38. https://doi.org/10.1038/d41586-023-03803-y Bandiera_abtest: a Cg_type: Comment publisher: Nature Publishing Group Subject_term: Machine learning, Health care, Medical research, Technology.
- [91] Undermind. 2024. Undermind - AI Powered Scientific Research Assistant. Retrieved September 6, 2024 from https://undermind.ai/
- [92] Priyan Vaithilingam, Tianyi Zhang, and Elena L. Glassman. 2022. Expectation vs.&nbsp;Experience: Evaluating the Usability of Code Generation Tools Powered by Large Language Models. In Extended Abstracts of the 2022 CHI Conference on Human Factors in Computing Systems (New Orleans, LA, USA) (CHI EA ’22). Association for Computing Machinery, New York, NY, USA, Article 332, 7 pages. https://doi.org/10.1145/3491101.3519665
- [93] Veniamin Veselovsky, Manoel Horta Ribeiro, Akhil Arora, Martin Josifoski, Ashton Anderson, and Robert West. 2023. Generating Faithful Synthetic Data with Large Language Models: A Case Study in Computational Social Science. arXiv:2305.15041 (May 2023). https://doi.org/10.48550/arXiv. 2305.15041 arXiv:2305.15041 [cs].
- [94] Qingyun Wang, Doug Downey, Heng Ji, and Tom Hope. 2024. SciMON: Scientific Inspiration Machines Optimized for Novelty. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), Lun-Wei Ku, Andre Martins, and Vivek Srikumar (Eds.). Association for Computational Linguistics, Bangkok, Thailand, 279–299. https://aclanthology.org/2024.acl-long.18
- [95] Skyler Wang, Ned Cooper, Margaret Eby, and Eun Seo Jo. 2023. From human-centered to social-centered artificial intelligence: Assessing ChatGPT’s impact through disruptive events. arXiv preprint arXiv:2306.00227 (2023).
- [96] Ryan Watkins. 2023. Guidance for researchers and peer-reviewers on the ethical use of Large Language Models (LLMs) in scientific research workflows. (May 2023). https://doi.org/10.1007/s43681-023-00294-5
- [97] Nigel Williams, Stanislav Ivanov, and Dimitrios Buhalis. 2023. Algorithmic Ghost in the Research Shell: Large Language Models and Academic Knowledge Creation in Management Research. ArXiv abs/2303.07304 (2023). https://api.semanticscholar.org/CorpusID:257496621
- [98] Dirk U. Wulff, Zak Hussain, and Rui Mata. 2024. The Behavioral and Social Sciences Need Open LLMs. OSF (Sept. 2024). https://doi.org/10.31219/ osf.io/ybvzs
- [99] Rui Zhang, Nathan J. McNeese, Guo Freeman, and Geoff Musick. 2021. "An Ideal Human": Expectations of AI Teammates in Human-AI Teaming. Proc. ACM Hum.-Comput. Interact. 4, CSCW3, Article 246 (jan 2021), 25 pages. https://doi.org/10.1145/3432945
- [100] Albert Ziegler, Eirini Kalliamvakou, X. Alice Li, Andrew Rice, Devon Rifkin, Shawn Simister, Ganesh Sittampalam, and Edward Aftandilian. 2022. Productivity assessment of neural code completion. In Proceedings of the 6th ACM SIGPLAN International Symposium on Machine Programming (San Diego, CA, USA) (MAPS 2022). Association for Computing Machinery, New York, NY, USA, 21–29. https://doi.org/10.1145/3520312.3534864
- [101] Caleb Ziems, William Held, Omar Shaikh, Jiaao Chen, Zhehao Zhang, and Diyi Yang. 2024. Can Large Language Models Transform Computational Social Science? Computational Linguistics 50, 1 (March 2024), 237–291. https://doi.org/10.1162/coli_a_00502


- A Survey Statistics

Gender Race Language Years Field All

RQ2 Frequency 3666 3162 3864 3864 3810 4896

- RQ5.1 Risk 2973 2597 3110 3110 3066 3410
- RQ5.2 Benefits 2315 2016 2440 2440 2403 2738 RQ5 3 Ethics 3191 2744 3354 3354 3314 3665 RQ5.4 Disclosure to Peers 3061 2631 3207 3207 3168 3493 RQ5.4 Disclosure to Reviewers 3028 2637 3177 3177 3139 3450


- Table 3. Number of answers to survey questions across all participants, broken out by demographic and question. Each question (row) had six sub-questions; participants did not have to answer all questions.

Type of Usage Risk Benefit Ethics Disclosure to Peers Disclosure to Reviewers

Information Seeking -0.303 0.513 0.261 0.127 (0.0005) 0.078 (0.041) Editing -0.276 0.557 0.282 0.171 0.073 (0.041) Ideation & Framing -0.372 0.651 0.385 0.197 0.177 Direct Writing -0.401 0.575 0.409 0.184 0.136 (0.0004) Data Cleaning & Analysis -0.437 0.68 0.335 0.229 0.186 Data Generation -0.45 0.665 0.383 0.262 0.245

Overall Usage -0.401 0.62 0.389 0.232 0.183

- Table 4. Kendall’s tau correlation between the frequency of LLM usage and the perception of that usage. Each cell includes the tau coefficient with the Holm-Bonferroni corrected 𝑝-value in parenthesis. Coefficients not followed by parenthesis all had 𝑝<.0001.

Gender Race Year Language Field

Gender / 0.7578 1.0000 0.1433 0.0008 Race / 0.0101 1.0000 1.0000 Year / 1.0000 0.0030 Publication 0.8043 1.0000 Language / 1.0000 Field /

- Table 5. 𝑝-values from Chisquare tests of independence between demographic groups. All𝑝-values were corrected via Holm-Bonferroni. Significant values (𝑝 < 0.05) are in bold and indicate dependence between pairs of variables.


- B Quantitative Method


Creating the Field Demographics Categories

We collected the research fields that our participants studied in the form of free responses. Out of the 816 responses, 644 (79%) responses included field information. We classified 635 free responses into four field categories: computer science, social science & humanities, natural science & engineering, and biology & medicine, and 9 responses were classified as other and excluded from the analysis. Computer science group had 257 participants, and also included interdisciplinary

fields with computer science, such as education technology, except biotechnology. Social science & humanities had 152 participants, and included psychology, behavioral science, education, sociology, and more. Natural science & engineering had 132 participants, and included math, chemistry, physics, environmental science, electrical engineering, and more. Biology & medicine had 94 responses, and included cognitive science, bioinformatics, biotechnology, public health, neuroscience, and more.

### C Qualitative Themes

Theme Description Example Reproducibility Whether research is repro-

“Because research should be reproducible, and this is only possible with the use of open-source LLMs.” “...an open-source model/data could be used and verified by external researchers and, hence, be more trustworthy.”

ducible/replicable/verifiable by other researchers

Transparency Whether the model release is transparent, including code, training dataset, evaluation dataset, etc.

“Greater transparency on the models and training data would increase my confidence in the models’ accuracy.” “As researchers, it is not just sufficient to use the service as a black box. I would like to know more about how the models were trained and what data went into it. It builds trust and expands the knowledge.”

Availability Whether the model is widely available, released to the public, and has no/low barriers for researchers to access

“World don’t have similar access to AI that might result in systemic discrimination.” “...Using for-profit solutions produces costs that require funding, but open-source options are typically less ‘ready-to-use’ and often require setup and potentially also local/available computing resources.”

Accountability Who should be responsible/accountable

“I don’t think it makes a difference whether I’m using os tech or ChatGPT, it’s still my responsibility to diligently check the outputs and the responsibility for any risks is on me as the user.” “A paid, close-source product could be less reliable, but there is someone to sue if things go awry.”

for the model and its use

Privacy Whether data is kept private and stored

“Open-source entities are more reliable, and transparent. The risk of using copyrighted data is less. The risk of stealing my personal sensitive data is less.” “I trust open-source software more than proprietary/commercial corp if I have to handle personal/sensitive data.”

securely

Incentives What kinds of incentives drive the cre-

“LLMs are fundamentally dependent on using people’s actual creative and artistic work without their consent. The motives of the LLM’s creator have no effect on that. Motives similarly have no effect on LLMs’ unreliability. Motives do not change whether LLMs are accountable for their mistakes, because LLMs cannot be accountable.” “I can’t trust the objectives and implementations of a closed commercial corporation.”

ation and release of the model

Neutrality Whether tools are considered neutral and who created/owns the tool does not matter

“The technology is the same (whether it’s provided by a commercial or an open source entity), so my perceptions are the same.” “I don’t know enough about what’s going on (or not) ‘behind the scenes’ in LLMs regardless of where they’re from—my perception of them remains that they’re unethical and not useful.”

Ethics & Bias Whether the model is biased or uses un-

“...a for-profit company might produce models which are favouring a certain kind of opinion, line of thought, or products. These might be equivalently good/bad to a non-profit model, but poses this inherent bias by whomever is currently financially invested into the entity” “The fundamental issues of bias, hallucination, ethical issues of invention, the need for review, etc. will not change whether the LLM is open-source or closed.”

ethical methods and data

Quality Whether the model has good performance (outputs are useful and of high quality)

“I´d rather use open-source LLMs, but I acknowledge that their performance is still behind commercial models which makes it difficult to use them.” “I would be concerned that the commercial aspects would affect the results served. Perhaps we would be directed more to paid sources.”

Table 6. Themes found in Q64: Would your perceptions of the benefits and risks of using LLMs be affected by whether the LLM is part of an open-source or non-profit entity versus a commercial corporation? Why or why not?

Language Equity Bridging language gaps to support non-

“I am not a native English speaker, so LLMs help me with the language barrier. ” “Because I’m not Native American, I’ve received a number of negative comments from reviewers, and I’ve always wondered how I can write like a Native American if I’m not one. Today, with the LLM tools, I can understand the terms I use that aren’t Native American, and I’m able to improve my writing.”

native English speakers

Other Equity Removing barriers for researchers (not language), such as supporting neurodivergent researchers, researchers with limited resources, or researchers without programming experience

“For researchers without programming skills, LLMs allow data analysis without programming. What they need to learn is how to make good natural language prompts.” “Improve understandability for non-specialists” “For honest researchers in resource-constrained developing countries, with little to no research funding, availability and use of LLMs is a game-changer leveling the playing field with other researchers in more fortunate climes. ”

Efficiency Saving time and resources during the re-

“Enhancing work efficiency and the capability of information gathering and extraction, thereby enabling researchers to focus more energy on creative tasks.” “Speeding up the academic writing/reading will speed up the research cycle of the community.”

search process

Completing routine or repetitive tasks, freeing the researcher to focus on higher level tasks

Routine Task Assistance

“I think the main benefit could be saving time that would otherwise have to be spent on relatively ’mechanical’ tasks, such as literature search, writing code for data cleaning and analysis, creating nice figures for publication and similar.” “Anything repetitive would benefit from LLMs”

Search Search and information retrieval tasks,

“Information seeking actions (like search) seem to often depend on serial reformulations of concepts, rephrasings, etc. to try to find the right thing. Even if LLMs hallucinate sources, this can be very helpful in those intermediary steps that are part of searching for things. There’s just too much out there.” “LLMs can give you enough information to continue searching online.”

which might include literature review

Literature Review Helping with literature-related tasks, such as finding related work, writing literature reviews, and summarizing literature

“Easing the otherwise time-consuming and burdensome processes in research. Tasks like lit searching, reading through content to determine study strengths/weaknesses/biases, extracting data from pubs...” “The internet is one big pile of noise. Publications are a somewhat less noisy, but still rather noisy pile of information. LLM’s cut through that to some degree.”

Editing Editing tasks, such as rephrasing sen-

“Mostly rephrasing, rewriting, condensation, bulleting” “Editing and language perfection, something like an advanced Grammarly.”

tences

Helping researchers to begin writing (to put something on the blank page)

Overcoming Writer’s Block

“The major benefit of using LLMs comes in action when we are stuck, for example not knowing the exact word or term, or not finding the answer to some of the ideas about how it can be used or how it can be applied.” “...loosing the fear of a blank sheet of paper when you don‘t know how to start your article...”

Helping researchers discover perspectives and diversify their sources

Broadening Perspectives

“LLM are remarkable important as they reduce generic data and improve novelty of work” “Always available ”colleague” to discuss ideas with and get feeback from.”

Programming Supporting programming tasks, includ-

“I basically code using CoPilot + GPT now, often for research glue code.” “Definitely saves time on coding applications where I’m not aware of certain routines or packages (for example python packages that already exist). Very helpful to get syntax correctly. Get feedback on coding errors...”

ing debugging and writing new code

Brainstorming Helping brainstorm, organize ideas, and

“LLMs are a great tool to help you create hypotheses, as a way to brainstorm, where there really are no wrong ideas and therefore you cannot suffer with any potential misleading information, as you are expected to have domain expertise anyway.” “Having an always available writing companion to help with ideation, divergent thinking, encouragement, and general advice.”

get feedback on ideas

Table 7. Themes found in Q65: Given your ratings above on the benefits/usefulness of these different ways of using LLMs, can you explain what you see to be the main benefits/usefulness for the academic community and for you as a researcher?

Production and spread of incorrect information invented by the model

Hallucination & Misinformation

“Sometimes it creates so complicated hallucinations so that even an expert can think that what it writes it true although it is not.” “Putting more falsehoods into [the internet’s] shared memory is a crime.”

Inaccuracy Incorrect conclusions and anal-

“There is a risk of less experienced scientists using these technologies as they are unable to check if the outputs are correct as easily as someone with more experience/intuition.” “The risks are proportional to prior knowledge of the subject.”

yses

Biases Model’s outputs could contain

“Promotions of some papers more than others - further marginalizing voices of those who are already less discovered and less cited despite similar quality of papers.” “I worry about biased LLMs influencing the research directions we choose and the conclusions we draw.”

biases and stereotypes

Lack of Disclosure Attribution or disclosure of

“Not acknowledging the use of the AI - universities have totally different policies.” “The advancement of this technology will make these models a kind of co-author, to the point where we will not know the real contribution of the human component.”

LLM usage

Plagiarism Risks of plagiarism when using models to generate paper text

“Blind trust in a system that is hard to understand which could lead to accidental plagiarism as it’s not easy to understand which information LLMs base their outputs on.” “plagiarism at scale, the community doesn’t have enough time to check all the existing papers”

Copyright and other concerns related to ownership of training data and model outputs

Disrespecting Authorship

“...its use to profit off of text whose authors weren’t compensated is pretty fucked up.” “There are issues of integrity where the data that is trained on doesn’t necessarily belong to the model makers, and the model’s output doesn’t belong to the user.”

Fabrication Using LLMs to fabricate data

“The risk of reporting ‘results’ based on synthetic data without actually having conducted any experiment.” “LLMs are tools for automated plagiarism and data fabrication that pose an existential threat to the network of trust essential for the integrity of academic work and the proper attribution of credit.”

and research results

Effects of model use on the creativity and originality of research work

Decreasing Creativity

“...llms are going to make people less creative over time. this needs of course more thinking and evidence, but to me, ppl may not start thinking or collaborating human to human to find valuable H2H collaborative ideas, but rather M2H ideas, which might miss the human touch.” “The main general risk is to flatten on "average", which is the worst thing that may happen for a researcher (and it is already happening for arts such music, since this would block innovation.”

Decreasing quality of research that leads to overall pollution of information and community

Pollution of Research Ecosystem

“The huge number of poor quality papers out there are already making science more difficult, and I can see LLMs making this much worse.” “We need better judgment, slower science, and more thoughtful and ambitious work right now, not the opposite. Otherwise, we risk ridding science of its most special attributes just to crank out more papers.”

Over-reliance on and trust in models leading to decreasing diligence of researchers

Decreasing Diligence

“Speed, copy/paste attitude, less research propositions, less reading of the full article, not enough training...” “The main risks are related to human tendency to be lazy and appreciate convenience too much. It would be easy to overtrust LLM output the inherent opacity of the technology invites people to do so. It is hard to check why particular output is produced and people have a natural talent to explain and justify things, even completely wrong things when it is more convenient.”

Deskilling Loss of research skills due to

“...sort of like with self-driving cars which, if we ever get ones that work a bit, people will stop learning how to drive, which will be bad when the things actually get confused and hand you the wheel!” “Learning how to relay information is an important skill that must be cultivated throughout ones career. The process of writing the information gives you the way to check whether what you have done actually makes sense and provides value.”

reliance on models

Table 8. Themes found in Q66: Given your ratings above on the risks/ethical considerations of these different ways of using LLMs, can you explain what you see to be the main risks/ethical considerations for the academic community and for you as a researcher?

