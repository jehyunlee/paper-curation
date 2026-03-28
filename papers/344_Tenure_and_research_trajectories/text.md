Downloaded from https://www.pnas.org by Korea Institute of Science and Technology KIST on March 24, 2026 from IP address 161.122.238.28.

# RESEARCH ARTICLE |

APPLIED PHYSICAL SCIENCES SOCIAL SCIENCES

###### OPEN ACCESS

## Tenure and research trajectories

Giorgio Tripodia,b,c,d,1 , Xiang Zhenge,1 , Yifan Qiana,b,c,d,1 , Dakota Murrayf , Benjamin F. Jonesa,b,c,d,g,2 , Chaoqun Nie,2 , and Dashun Wanga,b,c,d,h,2

Affiliations are included on p. 11. Edited by Yu Xie, Princeton University, Princeton, NJ; received January 20, 2025; accepted June 7, 2025

Tenure is a cornerstone of the US academic system, yet its relationship to faculty research trajectories remains poorly understood. Conceptually, tenure systems may act as a selection mechanism, screening in high-output researchers; a dynamic incentive mechanism, encouraging high output prior to tenure but low output after tenure; and a creative search mechanism, encouraging tenured individuals to undertake high-risk work. Here, we integrate data from seven different sources to trace US tenure-line faculty and their research outputs at a remarkable scale and scope, covering over 12,000 researchers across 15 disciplines. Our analysis reveals that faculty publication rates typically increase sharply during the tenure track and peak just before obtaining tenure. Post-tenure trends, however, vary across disciplines: In lab-based fields, such as biology and chemistry, research output typically remains high post-tenure, whereas in non-lab-based fields, such as mathematics and sociology, research output typically declines substantially post-tenure. Turning to creative search, faculty increasingly produce novel, high-risk research after securing tenure. However, this shift toward novelty and risk-taking comes with a decline in impact, with post-tenure research yielding fewer highly cited papers. Comparing outcomes across common career ages but different tenure years or comparing research trajectories in tenure-based and non-tenure-based research settings underscores that breaks in the research trajectories are sharply tied to the individual’s tenure year. Overall, these findings provide an empirical basis for understanding the tenure system, individual research trajectories, and the shape of scientific output.

tenure | career trajectory | science of science | innovation | computational social science

Few labor contracts are as distinctive or consequential as academic tenure in the United States ( 1 ), which combines a fixed-term probationary period, a high-stakes “up-or-out” decision, and lifetime job security. Despite its central role in the US academic system and its widespread use, we lack a systematic understanding of how tenure shapes scientists’ productivity, impact, and research agendas. Understanding the relationship between tenure and research trajectories is important not only for academic institutions and individual researchers but also for the broader public, given the role of public funding in supporting university research and the role of scientific advances in propelling technological developments, rising standards of living, and improved human health, among other benefits ( 2 – 10 ).

Tenure, as a lifetime labor contract, may have a strong influence on researcher incentives, choices, and performance ( 11 – 14 ). On one dimension, tenure operates as an up-or-out contract, creating powerful incentives to produce substantial, high-impact research within a fixed probationary period ( 15 – 18 ). This high-stakes timeline may drive researchers to focus on achievable projects that demonstrate their productivity and potential. However, upon receiving tenure and its job security, the incentives to continue to produce high-quantity or high-impact research may weaken. This “moral hazard” problem may lead to reduced output or a shift toward incremental work. On the other hand, moral hazard considerations may be offset or overcome by a “screening” function of tenure ( 19 – 23 ). Here, the tenure process can be thought of as a difficult test that identifies individuals who, regardless of incentives, are willing and able to maintain high levels of research success throughout their careers. Further, despite the job security of tenure, scientific norms and incentives may encourage persistent effort as researchers seek continued achievements, funding, and status, whether through grant money, prizes, or the respect of their peers ( 9 13 24 ). These contrasting forces raise important questions about the overall effects of tenure on research productivity across disciplines and career stages.

Beyond the rate of research production, tenure may also influence the direction of research. Specifically, research projects are steps into the unknown, where failure is common ( 25 – 27 ), especially in more “exploratory” work where researchers investigate novel terrain and payoffs are highly uncertain ( 28 – 36 ). Indeed, even ultimately successful

#### Significance

Tenure is a defining feature of the US academic system with significant implications for research productivity and creative search. Yet the impact of tenure on faculty research trajectories remains poorly understood. We analyze the careers of 12,000 US faculty across 15 disciplines to reveal key patterns, pre- and post-tenure. Publication rates rise sharply during the tenure-track, peaking just before tenure. However, post-tenure trajectories diverge: Researchers in lab-based fields sustain high output, while those in non-lab-based fields typically exhibit a decline. After tenure, faculty produce more novel works, though fewer highly cited papers. These findings highlight tenure’s pivotal role in shaping scientific careers, offering insights into the interplay between academic incentives, creativity, and impact while informing debates about the academic system.

The authors declare no competing interest. This article is a PNAS Direct Submission.

Copyright © 2025 the Author(s). Published by PNAS. This open access article is distributed under Creative Commons Attribution-NonCommercial-NoDerivatives License 4.0 (CC BY-NC-ND).

- 1G.T., X.Z., and Y.Q. contributed equally to this work.
- 2To whom correspondence may be addressed. Email: bjones@kellogg.northwestern.edu, chaoqun.ni@wisc.edu, or dashun.wang@northwestern.edu.


This article contains supporting information online at https://www.pnas.org/lookup/suppl/doi:10.1073/pnas. 2500322122/-/DCSupplemental.

Published July 22, 2025.

Downloaded from https://www.pnas.org by Korea Institute of Science and Technology KIST on March 24, 2026 from IP address 161.122.238.28.

breakthrough ideas, from mRNA vaccines to AI, often follow years of failure or stagnation ( 25 – 27 ). Tenure, by offering job security, creates a rare contractual arrangement that may encourage researchers to take bigger bets in their creative search ( 12 13 ), attempting relatively novel inquiries in pursuit of transformative discoveries. However, while tenure’s role in encouraging risk-taking and exploration is often assumed, its actual effects on research trajectories remain unclear. Does tenure consistently foster exploratory work, or does it depend on disciplinary norms or institutional contexts? Do researchers across different disciplines respond differently to tenure? And how do the patterns observed in the US tenure system compare to other institutional settings, such as national laboratories or European universities, where different employment structures prevail?

Amid ongoing debates about tenure’s advantages and drawbacks ( 11 37 – 39 ), existing empirical studies have mainly focused on specific disciplines and selected faculty groups ( 40 – 43 ), with systematic assessments limited by the lack of comprehensive longitudinal faculty data across scientific disciplines. In this paper, we integrate seven different data sources to assemble the largest and most comprehensive database of faculty rosters and research outputs to date. The core of these data is sourced from the Academic Analytics Research Center (AARC) [D1], which captures a census of about 300K faculty from 362 Ph.D.-granting institutions in the United States. The dataset covers the time period between 2011 and 2020 and spans all scientific disciplines, allowing us to systematically identify tenure-line faculty members and examine how an individual’s research evolves before and after tenure. We focus on faculty members who experience a transition from a tenure track to a tenured position between 2012 and 2015, allowing us to follow their careers for at least 5 y before and after their promotion. In addition, this time window ensures that our results are not affected by the COVID-19 pandemic, which had a significant impact on scientific careers, tenure clocks, and research production ( 44 – 46 ). We complement AARC data [D1] with two additional databases [D2 and D3] that trace the entire faculty rosters of two different large research universities in the United States, covering all faculty members who were promoted over the past 20 y. These data allow us to test the generalizability of the findings from the first dataset [D1] over longer time spans. We further integrate D1 to D3 with large-scale datasets that offer information related to publications, citations, funding, and other relevant research measures, including SciSciNet [D4] ( 47 ), Scopus [D5], and Dimensions [D6]. Finally, we integrate dissertation data from ProQuest [D7] with D1 to D6, allowing us to develop a peer group of researchers who graduated from similar PhD programs in the same years as the faculty members we study. Overall, we trace the research outputs of 12,611 faculty members across the sciences, engineering, and social sciences (see Materials and Methods and SI Appendix for further details on the descriptions of the datasets and additional validations).

#### Results

Tenure and Research Output. We first focus on the relationship between tenure and publication rates. We evaluate outcomes over an 11-year span, including the 5 y before and after tenure. We find that, on average, the publication rate rises steeply and steadily through the tenure track, typically peaking the year before tenure (Fig. 1A). After tenure, the average publication rate shows remarkable stability, settling near the peak achieved right before tenure (Fig. 1A). We further test whether this pattern may be influenced by the research environment, such as university rank (48–50), finding the same distinctive patterns at different

university ranks (Fig. 1B). Overall, publications feature a highly reproducible pattern, with a sharp break occurring around the tenure year, suggesting that the timing of tenure substantially conditions individual output, irrespective of university rank (Fig. 1B).

However, this pattern might also be a function of career age, as output rates shift over the life cycle ( 51 – 57 ). To test this, we separate our analyses by grouping scientists with different career ages when attaining tenure. More specifically, we measure the number of years elapsed between the doctoral degree and tenure (i.e., “career age at tenure”) for each scientist and then consider the publication pattern around tenure for researchers with different career ages ( Fig. 1C ). Strikingly, regardless of career age, average publication rate follows the same distinctive pattern. The tenure transition manifests itself whether the researchers are as few as 6 y past their PhD or as many as 14 y past their PhD. The sharp transitions in publication rates thus do not appear related to career age but rather closely follow the specific tenure timing.

The pattern documented in Fig. 1 is rather unexpected, considering two lines of evidence in prior literature. First, research on the lifecycle of creative output consistently shows a smooth, curvilinear relationship, with no sharp breaks in publication growth ( 51 – 56 ). By contrast, when lining publication rates up against individual-specific tenure timing, our analysis instead reveals a sharp transition in output growth, timed to the individual’s change in the labor contract. Second, research on economics and finance professors indicates falling publication counts after tenure ( 43 ). By contrast, our results show relatively sustained output levels post-tenure when looking at all fields together. This suggests potentially substantial disciplinary differences in how researchers behave after tenure, which we explore next.

Field-level heterogeneity. We classify scientists into 15 different disciplines based on their publications (Materials and Methods and SI Appendix, Fig. S3). This discipline-level analysis reveals heterogeneity, with two broad patterns (Fig. 2). For business, economics, mathematics, sociology, and political science, the average trend in research output follows a rise-and-fall pattern (51–54). Yet for all other disciplines, publication rates sustain after tenure rather than decline. In sum, publication rates rise sharply during the tenure track for all disciplines and peak around the year of tenure. Following the peak, disciplines diverge, with some showing declining publication rates while others show rates that stabilize at high levels. Overall, beneath the overall trends observed in Fig. 1 lies a striking disciplinary heterogeneity (see SI Appendix, Fig. S2 for a field-normalized version of Fig. 1). While tenure is a universal feature across disciplines, these results unveil great disciplinary variation in output patterns after tenure.

Amidst the many factors that may underpin such disciplinary variations, one notable distinction lies in laboratory approaches to research ( 58 59 ). Disciplines that follow rise-and-stabilize patterns are generally organized through a laboratory model of scientific production, whereas the rise-and-fall disciplines—business, economics, mathematics, sociology, and political science—do not traditionally use this laboratory model. The laboratory model is characterized by reliance on grant funding and substantial teamwork, often in a hierarchy where the principal investigator recruits and collaborates extensively with PhD students and postdoctoral researchers. To quantify these distinctions, we measure the median team size per paper for each discipline (SI Appendix, Fig. S4 and section S4 ), the fraction of solo-authored papers (SI Appendix, Fig. S5 and section S4 ), the share of papers coauthored with early career researchers (SI Appendix, Fig. S6 and section S4 ), and the amount of funding garnered by each faculty (SI Appendix, Fig. S7 and section S4 ). Across all these measures, we consistently see the

Downloaded from https://www.pnas.org by Korea Institute of Science and Technology KIST on March 24, 2026 from IP address 161.122.238.28.

A B

Mean publications per year

Mean publications per year

Relative time to tenure (years)

Relative time to tenure (years)

C

Mean publications per year (difference wrt. tenure year)

Years since Ph.D.

Fig. 1. Tenure and publication rates. (A) Articles published per year, averaged across researchers for each year before and after tenure. (B) Articles published per year, averaged across researchers, by university rank. (C) Articles published with respect to tenure year, by career age. Career age is defined as the number of years from Ph.D. to tenure; 85% of the academics in the total sample reach tenure between 6 and 14 y after completing a Ph.D. (SI Appendix, Fig. S1). Error bars are 95% CIs. This figure is based on datasets D1 and D4.

split between the two classes of disciplines (SI Appendix, section S4 ). We further confirm that the rise-and-stabilize patterns persist when considering only the lead-author papers by faculty in laboratory disciplines (SI Appendix, Fig. S8 ) or different university ranks (SI Appendix, Fig. S9 ).

Individual-level heterogeneity. Individual scientists may follow varied research trajectories (60, 61) or respond differently to incentives such as tenure (62, 63). To examine individual-level heterogeneity, we compare publications per year before and after tenure for each scientist and calculate the share of faculty members whose publication rate increases or decreases. Specifically, we group individual researchers into four categories according to their average publication rate after tenure: i) zero (the individual stops producing papers after tenure); ii) lower (the annual publication rate declines); iii) higher (the annual publication rate grows between 0 and 100%); and iv) more than double (the annual publication rate grows more than 100%). Fig. 3 summarizes these results. We find that across all disciplines, only a tiny fraction of

faculty ceases production entirely after tenure. Further, a substantial fraction of faculty significantly increases their average publication rate after tenure, with many even doubling their research output. The two classes of disciplines in Fig. 2 prove germane again when considering individual heterogeneity. In the rise-and-stabilize disciplines, the majority of researchers see increased publication rates post-tenure. In the rise-and-fall disciplines, the majority of faculty see decreased publication rates post-tenure.

We further quantify differences in publication rates across individual researchers using the Gini index and examine how this evolves pre- and post-tenure (SI Appendix, Figs. S10 and S11 ). We find the publication rate differences across faculty members decrease as junior faculty approach tenure, reaching their lowest point in the year before tenure, before rising again after tenure. We repeat our analyses by measuring the coefficient of variation in publication rates, observing similar patterns (SI Appendix, Fig. S12 ). Notably, this convergence-then-divergence pattern applies to all disciplines, with the transition occurring in the year

Downloaded from https://www.pnas.org by Korea Institute of Science and Technology KIST on March 24, 2026 from IP address 161.122.238.28.

political science

business economics mathematics sociology

1.6

1.8

- 1.8

- 3
- 4
- 5


- 2
- 3
- 4


1.2

1.6

1.4

1.6

1.4

1.0

1.2

1.4

1.2

- 1.6

- 1.8
- 2.0

2.2

- 3
- 4
- 5
- 6


- 3
- 4
- 5




1.0

1.2

0.8

1.0

1.4

0.8

- -5-4-3-2-10 1 2 3 4 5 -5-4-3-2-10 1 2 3 4 5 -5-4-3-2-10 1 2 3 4 5 -5-4-3-2-10 1 2 3 4 5 -5-4-3-2-10 1 2 3 4 5

- -5-4-3-2-10 1 2 3 4 5 -5-4-3-2-10 1 2 3 4 5 -5-4-3-2-10 1 2 3 4 5 -5-4-3-2-10 1 2 3 4 5 -5-4-3-2-10 1 2 3 4 5

- -5-4-3-2-10 1 2 3 4 5 -5-4-3-2-10 1 2 3 4 5 -5-4-3-2-10 1 2 3 4 5 -5-4-3-2-10 1 2 3 4 5 -5-4-3-2-10 1 2 3 4 5


computer science

Mean publications per year

chemistry biology medicine psychology

2.75

4.0

2.50

2.4

3.5

2.25

2.0

3.0

2.00

2.5

1.6

1.75

2.0

environmental science

materials science

geoscience

engineering physics

3.5

5.0

3.0

- 2
- 3


4.5

4.0

2.5

3.5

2.0

3.0

1.5

Relative time to tenure (years)

Fig. 2. Cross-disciplinary variations in publication patterns. Each panel shows the average number of papers published by authors in a particular discipline. Disciplines are colored to distinguish two types of trends: those where publications rise and decline (purple), and those where they rise and stabilize (orange). These trends roughly correspond to non-lab-based and lab-based disciplines, respectively. Shaded areas represent 95% CIs. This figure is based on datasets D1 and D4.

right before tenure. The tenure timing again marks a sharp shift in behavior.

Together, these findings deepen our empirical and theoretical understanding of how institutional incentives and organizational settings interact with publication rates in an increasingly collaborative research environment. First, we document a sharp break in publication rates around tenure rather than a gradual shift over time—a pattern that persists irrespective of career age, university rank, or individual differences. This finding challenges the conventional view of a smooth productivity curve over time ( 51 – 56

64 – 66 ), showing that the timing of tenure sharply conditions the rate of scientific outputs. Second, the scale of our data enables analysis across disciplines, revealing striking variations between lab-based and non-lab-based fields that were not visible in prior single-discipline or smaller-scale studies ( 40 – 43 ). Finally, our results offer a more nuanced perspective on the incentives tied to tenure. Rather than a uniform decline in productivity ( 43 ), we find that post-tenure trajectories vary in relation to how scientific work is organized, suggesting the importance of team structure, collaboration dynamics, and field-specific norms to understandings of how tenure shapes research careers.

Research impact. Publication impact, beyond publication counts, is also central to understanding researcher output, prompting us to examine the production of high-impact papers before and after tenure. Since the impact of papers is time- and field-dependent (67), we measure hit papers, defined as those in the top 5% of the distribution of citations across all papers in the same publication

year and subfield (SI Appendix, section S6). Fig. 4A shows the pooled hit rate, computed as the ratio of the total number of hit papers over the total number of articles in the given year before or after tenure. The hit rate is found to be higher before tenure than after tenure, with a downward trend that generalizes across the diverse disciplines we consider. While the proportion of high-impact papers generally declines after tenure (SI Appendix, Figs. S15A and S26–S28), to better characterize post-tenure dynamics, it is important to distinguish between proportional and absolute changes in high-impact output. Accordingly, we also analyze the average number of hit papers per year across fields.

- As shown in SI Appendix, Fig. S13, the absolute number of highimpact publications also generally declines following tenure, mirroring the patterns observed in the proportion-based analysis.

We also investigate the timing of the highest-impact paper each researcher produces in the 11-year span and compare the position with a null model where impacts are distributed randomly within a career ( 56 ) (Materials and Methods and SI Appendix, section S7 ).

- At this individual level, researchers tend to produce their most-cited paper (again, normalized according to the field and year) during the tenure track rather than after tenure ( Fig. 4B ). To ensure that the exceptional impact in pre-tenure years is not driven by collaborations, especially those with prior advisors, we repeat the analysis by considering papers published as the last author, and we arrive at the same conclusions (SI Appendix, Fig. S14 ). This pattern is particularly notable given the literature, which suggests that the timing of a scholar’s most-cited work is


Downloaded from https://www.pnas.org by Korea Institute of Science and Technology KIST on March 24, 2026 from IP address 161.122.238.28.

Fig. 3. Fields and individual heterogeneity. Share of faculty who increase or decrease their average number of publications per year after tenure by field. Note that we exclude a negligible fraction of faculty who did not publish any paper in the 5 y before tenure. This figure is based on datasets D1 and D4.

randomly distributed within the publication sequence ( 56 57 ). To assess this further, we replicate the approach from Sinatra et al. ( 56 ), comparing our tenure-line sample to several “control groups” composed of researchers not specifically on a tenure line. For all control samples, the highest-impact paper indeed occurs randomly within the sequence of work they produce, highlighting the robustness of findings in the prior literature. In contrast, among tenure-line scholars (i.e., our sample), we observe a systematic departure from the random impact rule, as the most-cited work tends to appear earlier in their publication history (SI Appendix, Figs. S16 and S17 and section S7 ). This finding again illustrates the importance of considering tenure, which is a major career milestone, and the institutional context when studying careers, as it reveals otherwise hidden dynamics and offers insights into individual career trajectories.

Overall, these results are consistent with conceptualizations where tenure, as an up-or-out contract design, brings out an individual’s peak performance during the tenure track.

Tenure and Exploration. A perceived advantage of tenure is that job security encourages professors to take bigger risks in their research projects and explore novel ideas. This pursuit of novelty can take two distinct forms.

In one form, scholars try directions that are new to them personally—a new agenda that extends their focus and skills. In the second form, scholars try directions that are novel for science as a whole—research orientations that appear unusual within the scope of prior science. Here, we operationalize measures for both types of novelty and explore the nature of pre- to post-tenure transitions.

We first group the papers of each faculty member into topics, applying a community detection method to the coreference network of these papers (see Materials and Methods and SI Appendix, section S8 for detailed methods) ( 28 68 ). Fig. 5A shows an illustrative example, where nodes represent the faculty member’s papers, and two papers are connected if they share common

references. To explore linkages with tenure, we further categorize each detected community into one of four types: continued topic (present both before and after tenure); new topic (emerging only after tenure); abandoned topic (present only before tenure); or isolated topic (not connected to any other papers). Fig. 5B continues the example in Fig. 5A but with the publication year for each paper lined up against the faculty member’s tenure timing. In this example, the faculty member abandoned one topic (red), explored one new topic (gold), and continued one pre-tenure research topic (black).

Applying these methods to each individual in our data, Fig. 5C investigates whether and how faculty members reorganize their research portfolio after tenure. Our analysis indicates that faculty do tend to shift their directions: Approximately two-thirds of faculty engage with at least one new topic in the 5 y after tenure, and approximately one-third of faculty members abandon at least one topic, depending on the discipline. Notably, virtually all faculty continue working on at least one topic they focused on before tenure. In other words, faculty almost never exhibit a complete switch in research directions following tenure but rather exhibit a portfolio approach in creative search.

Overall, faculty members balance ongoing connections with their established research agenda (exploitation) with the pursuit of new directions (exploration), which is consistent with the “ambidexterity” literature on organizations ( 69 ), but here applied to individual behavior. These patterns echo prior findings on major scientific awards, which show that after receiving prestigious prizes such as the Nobel Prize ( 70 ) or Fields Medal ( 71 ), researchers often pivot toward new topics that are less familiar to themselves. While tenure and major prizes differ in important ways, both represent inflection points that may confer greater autonomy or access to resources, facilitating exploration.

To understand the relative focus on exploration and exploitation, we divide faculty members’ research outputs into continuations of pre-tenure topics vs. investigations of a new topic that was not studied before tenure. Whereas the average publication rate tends

Downloaded from https://www.pnas.org by Korea Institute of Science and Technology KIST on March 24, 2026 from IP address 161.122.238.28.

### A

political science

business economics mathematics sociology

24%

22%

40%

30%

21%

20%

28%

35%

18%

- 24%

28%

20%

- 25%


18%

26%

30%

24%

15%

16%

20%

25%

22%

- -5-4-3-2-1012345 -5-4-3-2-1012345 -5-4-3-2-1012345 -5-4-3-2-1012345 -5-4-3-2-1012345
- -5-4-3-2-1012345 -5-4-3-2-1012345 -5-4-3-2-1012345 -5-4-3-2-1012345 -5-4-3-2-1012345
- -5-4-3-2-1012345 -5-4-3-2-1012345 -5-4-3-2-1012345 -5-4-3-2-1012345 -5-4-3-2-1012345


computer science

chemistry biology medicine psychology

Hit rate - pooled

- 14.0%
- 15.0%
- 16.0%
- 17.0%
- 18.0%
- 19.0%


- 11.0%
- 12.0%
- 13.0%
- 14.0%
- 15.0%


17.5%

20.0%

15.0%

17.5%

12.5%

15.0%

10.0%

materials science

environmental science

engineering physics

geoscience

20%

22.5%

30%

24%

25%

20.0%

18%

25%

22%

17.5%

20%

20%

16%

15.0%

20%

15%

Relative time to tenure (years)

### B Not significant Significant

political science

business economics mathematics sociology

1.6

1.4

1.2

1.4

1.50

1.4

1.2

1.1

1.2

1.25

1.2

1.0

1.0

1.00

1.0

1.0

0.8

0.9

0.75

0.8

0.8

Most cited paper - Odds ratio

- -5-4-3-2-1012345 -5-4-3-2-1012345 -5-4-3-2-1012345 -5-4-3-2-1012345 -5-4-3-2-1012345

- -5-4-3-2-1012345 -5-4-3-2-1012345 -5-4-3-2-1012345 -5-4-3-2-1012345 -5-4-3-2-1012345

- -5-4-3-2-1012345 -5-4-3-2-1012345 -5-4-3-2-1012345 -5-4-3-2-1012345 -5-4-3-2-1012345


computer science

chemistry biology medicine psychology

1.6

1.75

2.0

1.4

1.50

1.4

1.50

1.2

1.5

1.2

1.25

1.25

1.0

1.0

1.0

1.00

1.00

0.8

0.8

environmental science

materials science

geoscience

engineering physics

2.0

1.50

2.0

2.0

1.2

1.25

1.5

1.5

1.5

1.0

1.00

1.0

1.0

1.0

0.75

0.8

0.5

Relative time to tenure (years)

Fig. 4. Impact. (A) Pooled hit rate (number of hit papers over the total number of articles published by faculty in each year before and after tenure). Different versions of the hit rates, confirming the same trends, can be found in SI Appendix, Fig. S15A. (B) Share of faculty who produce their most-cited paper over our time window (ratio with respect to null model) by field. Significance at 95% CI. This figure is based on datasets D1 and D4.

to follow two broad classes across the disciplines, here we find that when we only count papers that continue the pre-tenure agenda (black dashed line), all disciplines follow the rise-and-fall pattern

( Fig. 6 ). This suggests that new agendas post-tenure (shaded areas in Fig. 6 ) appear to be a key feature sustaining output rates for the rise-and-stabilize patterns observed in Fig. 2 (SI Appendix, Fig. S34 ).

Downloaded from https://www.pnas.org by Korea Institute of Science and Technology KIST on March 24, 2026 from IP address 161.122.238.28.

A B

Paper degree

Relative time to tenure (years)

C

Share of faculty

Fig. 5. Tenure and research portfolio. (A) A stylized example of a coreference network and community detection for a single scholar. (B) Scatter plot of topic exploration before and after tenure for a single faculty member. (C) Share of scholars who reorganize their research portfolio after tenure (New = start a new agenda; Keep = maintain parts of the “old” agenda; Abandon = abandon some topics explored before tenure). This figure is based on datasets D1 and D4.

The second form of novelty we consider is whether faculty increasingly engage in novel research, not compared to their own work, but compared to prior science as a whole. Specifically, and following prior literature ( 6 72 73 ), we measure novelty as capturing atypical combinations of prior work ( 33 ) (Materials and Methods and SI Appendix, section S6 ). As we did for impact, we compute the pooled novelty rate and the position of the most novel paper in the 11-year sequence compared with a null model. Fig. 7A shows that the pooled novelty rate tends to increase, indicating a higher propensity of faculty to be involved in novel-to-science projects after tenure. Further, the most novel paper within the period tends to appear after tenure ( Fig. 7B ). Notably, these findings contrast with the impact results ( Fig. 4 ): Whereas the share of hit papers goes down with time, the novelty of the papers tends to go up. To account

for potential temporal trends, we include a robustness check using a year- and subfield-normalized measure of novelty, arriving at the same conclusions (SI Appendix, Figs. S18 and S35 and section S6 ). Note that these analyses are correlational: They document a robust association between the tenure phase and higher novelty, but they do not establish a causal effect of tenure per se. Nevertheless, these patterns are consistent with more exploratory work post-tenure. While there is no obvious sharp break at tenure, we do see a shift toward more novelty and lower success rates, largely consistent with a key motivating idea of tenure in encouraging higher-risk search.

To quantify the balance between exploration and exploitation in the context of creative search behavior, we further compute the hit and novelty rates by research agenda (i.e., new vs. continuing) before and after tenure. These comparisons are

Downloaded from https://www.pnas.org by Korea Institute of Science and Technology KIST on March 24, 2026 from IP address 161.122.238.28.

Fig. 6. Post-tenure diversification and research trajectories. Average number of papers by type/topic. The black dashed line indicates the average number of papers adhering to the old agenda. The solid line indicates the average number of papers, considering papers that belong to both “continuing” and “new” communities. This figure is based on datasets D1 and D4.

only feasible for faculty who start a new agenda after tenure (~5K scholars); hence, the results should be interpreted as conditional on successfully starting a new agenda post-tenure. We find that papers published before tenure in the “old” agenda (i.e., the topics faculty members keep after tenure) show the highest hit rate ( Fig. 8A ). However, post-tenure papers within this preexisting agenda are substantially less impactful than pre-tenure papers. Interestingly, papers that belong to the new agenda (i.e., exploration) have a greater impact than new papers that continue the pre-tenure agenda (i.e., exploitation). Taken together, we see that new agendas for a faculty member tend to outperform continuations of the old agendas. This is consistent with faculty expanding into new areas as their prior areas deliver diminishing returns.

Turning to novelty, we indeed find that papers on new topics post-tenure are also more novel in science as a whole ( Fig. 8B ). We confirm these trends by considering continuous outcome variables (avg. citation and avg. novelty, SI Appendix, Fig. S19 and section S6 ) and fields with and without the laboratory model (SI Appendix, Fig. S20 and section S4 ). Moreover, by simultaneously examining topic exploration and novelty rates, we also reveal that after tenure, scholars introduce novel ideas not only when exploring new topics but also when continuing established research agendas ( Fig. 8B – continuing after tenure, SI Appendix, Figs. S21 and S22 and Table S2 ). In sum, these results indicate that in the post-tenure period, faculty tend to undertake agendas that are both new to them and relatively novel in science, a potentially riskier behavior that extends the reach of science as a whole but produces fewer hits. This shift appears in comparisons of post-tenure with pre-tenure periods, highlighting evolving research directions over time.

Institutional Comparisons. One key question is whether the patterns we observe are specific to tenure, given that other factors may be at play. To further interrogate the role of tenure, we compare patterns between individual researchers in the tenure-line context with alternative “control groups” of researchers in different institutional contexts. First, we use dissertation data to identify graduates who were in similar US PhD programs and graduated in the same year but were not tenured by the end of our time window (SI Appendix, Fig. S23). Second, using a similar matching strategy, we identify individuals from the same PhD program and graduation year who moved to Europe upon graduation (where labor contracts are organized differently than in the US tenure system, SI Appendix, Fig. S24A). Third, we identify the graduates of these similar US PhD programs who joined government organizations in the United States, such as national labs, and we compare their research trajectories with our tenure-line faculty sample (SI Appendix, Fig. S24B). Fourth, leveraging the internal HR data from two large R1 universities (D2 and D3), we identify faculty members employed in the same university in the same period but separate them based on tenure eligibility, comparing their research trajectories (SI Appendix, Figs. S25 and S26).

Across all these control groups, we find that the control researchers do not exhibit the characteristic publication rate shifts that we observe at tenure for the tenure sample. Rather, output measures tend to move in a smooth manner when studying research trajectories among these various control groups. Note that these controls do not imply causal relationships between tenure and research trajectories, especially to the extent that researchers who enter the US tenure track are a selected sample, and in general, it is difficult to deploy experimental or quasi-experimental

Downloaded from https://www.pnas.org by Korea Institute of Science and Technology KIST on March 24, 2026 from IP address 161.122.238.28.

### A

political science

business economics mathematics sociology

60%

40%

20%

computer science

chemistry biology medicine psychology

Novelty rate - pooled

60%

40%

20%

materials science

environmental science

engineering physics

geoscience

60%

40%

20%

-5-4-3-2-10 1 2 3 4 5 -5-4-3-2-10 1 2 3 4 5 -5-4-3-2-10 1 2 3 4 5 -5-4-3-2-10 1 2 3 4 5 -5-4-3-2-10 1 2 3 4 5

Relative time to tenure (years)

### B Not significant Significant

political science

business economics mathematics sociology

1.75

1.4

1.2

1.3

1.4

1.50

1.2

1.2

1.1

1.1

1.25

1.0

1.0

1.0

0.9

1.00

0.8

0.8

0.9

0.75

Most novel paper - Odds ratio

- -5-4-3-2-1012345 -5-4-3-2-1012345 -5-4-3-2-1012345 -5-4-3-2-1012345 -5-4-3-2-1012345

- -5-4-3-2-1012345 -5-4-3-2-1012345 -5-4-3-2-1012345 -5-4-3-2-1012345 -5-4-3-2-1012345

- -5-4-3-2-1012345 -5-4-3-2-1012345 -5-4-3-2-1012345 -5-4-3-2-1012345 -5-4-3-2-1012345


computer science

chemistry biology medicine psychology

1.4

1.4

1.2

2.00

1.6

1.3

1.75

1.4

1.1

1.2

1.2

1.50

1.2

1.0

1.1

1.25

1.0

1.0

1.0

1.00

0.9

0.8

0.9

0.75

0.8

environmental science

materials science

geoscience

engineering physics

1.50

1.5

2.5

1.50

1.50

1.25

2.0

1.3

1.25

1.25

1.00

1.5

1.1

1.00

1.00

0.75

1.0

0.9

0.75

0.50

0.5

0.75

Relative time to tenure (years)

Fig. 7. Novelty. (A) Pooled novelty rate by field (number of novel papers over the total number of articles published by faculty in our sample each year). A different version of the novelty rates, confirming the same trends, can be found in SI Appendix, Fig. S15B. (B) Share of faculty who produce their most novel paper over our time window (ratio with respect to null model) by field. Significance at 95% CI. This figure is based on datasets D1 and D4.

approaches to the tenure system. Nevertheless, the results from these numerous control exercises further inform the distinctiveness of the shifts we see in research trajectories across tenure within US

academic institutions. Overall, the sharp break in output appears unique to tenure timing, whether in comparisons among US tenure-line academics ( Fig. 1 ) or in comparison to individual

Downloaded from https://www.pnas.org by Korea Institute of Science and Technology KIST on March 24, 2026 from IP address 161.122.238.28.

Paper type continuing new

### B

|16%<br><br>18%<br><br>20%<br><br>| | |
|---|---|
| | |
| | |
| | |
<br><br>before after<br><br>Hit rate<br><br>A<br><br>Relative time to tenure|
|---|


62%

Novelty rate

60%

Hit rate

58%

56%

before after

Relative time to tenure

Fig. 8. Post-tenure diversification, impact, and novelty. (A) Hit rate by paper type for scholars with a new agenda. (B) Novelty rate by paper type for scholars with a new agenda. Error bars are 95% CIs. This figure is based on datasets D1 and D4.

research trajectories in different institutional contexts (SI Appendix, Figs. S23–S26 ).

Tests with Alternative Data. We further examine the main analyses using alternative data and additional regression methods. Specifically, while our main analyses use publication data via Microsoft Academic Graph and SciSciNet [D4], we reconsider the main findings with Scopus [D5], using that database’s publication records and field encodings. The results prove robust to these alternative data (SI Appendix, Figs. S27–S38 and sections S1, S3, and S6). Further, we consider the main findings for publication rate, hit rate, and novelty rate in regressions that include individual researcher fixed effects and numerous paper-level controls, finding consistent results (Materials and Methods and SI Appendix, Figs. S39–S43 and section S11).

Tests with Alternative Samples. We also investigate the sensitivity of our results to the choices made in constructing our main sample. To do so, we consider alternative approaches to filtering raw data and creating faculty samples, and we test whether such choices affect the main findings. We find that our results remain robust across all these alternative analyses (SI Appendix, sections S1 and S10 and Figs. S44–S48).

#### Discussion

Integrating seven different large-scale data sources, this work reveals central facts about research trajectories before and after tenure, demonstrating widespread turning points for individual scientists. Interestingly, although tenure represents a universal milestone across fields, post-tenure trajectories diverge in notable ways. On average, some disciplines experience declining publication rates, while others sustain high rates of research output. Moreover, receipt of tenure is associated with a shift toward more novel but less impactful work. The results prove robust across different datasets, controls, and assumptions. The distinctiveness of tenure patterns also appears when comparing tenure-line researchers with individual researchers working under different contracts or in different types of research institutions.

The findings speak to conceptual views of tenure’s potential effects, both in the rate and direction of research activities, while also revealing important heterogeneity across disciplines and individuals. Viewed as a screening mechanism, tenure does tend to select on individuals who maintain robust research agendas. Viewed as a moral hazard problem, theories that emphasize weak incentives to sustain research output post-tenure do not appear

to describe the sciences or researchers on average. In many disciplines, publication rates tend to stabilize at high levels. Further, the cessation of publishing upon tenure is exceedingly rare, whereas individuals doubling their pre-tenure rate of research output is far more common. At the same time, outside the laboratory sciences, we do see a tendency for declining publication rates after tenure. The disciplinary heterogeneity suggests the incentive aspects of tenure may be important yet are overcome by other forces in many fields. Unpacking the forces that support continued research output beyond tenure is an important area for future work.

Other theoretical viewpoints emphasize that tenure, through the job security it provides, encourages exploratory, higher-risk research. The empirical evidence indicates that faculty do indeed tend to shift toward more novel research after tenure, but with declining hit rates, consistent with higher-risk research allocations. Digging deeper into research portfolios, nearly all faculty continue at least one pre-tenure research agenda, while more than half of faculty add a new agenda. The new agendas further exhibit greater novelty for science. It is thus common to see shifts toward research that is not just new to the individual but new to science as a whole.

Overall, given the central role of tenure in the US academic system, this paper establishes an important empirical basis for understanding faculty research trajectories both before and after tenure. While the focus of this paper is on research outputs, tenure is a pivotal point in a career that often marks shifts in many other dimensions, including service, mentoring, administrative duties, and more. Weighing the broader activities of scientists is a key area for future work. Moreover, while our analyses examined changes in individual research trajectories before and after tenure, future work may include those who did not attain tenure, examine longer-run career trajectories, and further investigate research trajectories in alternative institutional contexts, enabling researchers to answer a range of new questions. Given the prominence of research universities in generating fundamental knowledge and innovations that drive human progress, understanding how tenure systems influence research outcomes is important not only for the academic community but also for advancing discoveries that benefit the broader society.

#### Materials and Methods

Data. This study integrates data from seven sources: AARC faculty rosters [D1], covering 314,141 tenured and tenure-track scholars at 393 U.S. Ph.D.-granting institutions from 2011 to 2020; internal HR records from two large R1 universities [D2, D3], spanning 2000–2017; SciSciNet (47) [D4], a data lake based on Microsoft Academic Graph (MAG), containing metadata on 134 million publications; Scopus

Downloaded from https://www.pnas.org by Korea Institute of Science and Technology KIST on March 24, 2026 from IP address 161.122.238.28.

[D5], a large citation database maintained by Elsevier; Dimensions [D6], a comprehensive bibliometric database curated by Digital Science; and ProQuest [D7], a comprehensive repository of U.S. Ph.D. dissertations. For a more extensive description of each data source see SI Appendix, section S1.

Main Sample Construction. We identify tenure transitions by analyzing faculty title changes in AARC [D1], coding promotions from assistant to associate professor in consecutive years. To ensure complete observation windows and avoid COVID-19 potential bias (44–46), the main sample is restricted to scholars tenured between 2012 and 2015. Scholars are linked to publication records from D4, retaining only those with at least one publication within 5 y before and after tenure and classified into a single discipline (excluding humanities and particle physics that may follow different incentives and atypical career patterns). The main D1 to D4 matched sample includes 12,611 scholars across 15 disciplines (seeSI Appendix, section S2 for additional details). For the construction of control groups, supplementary dataset integration, and alternative samples, please refer to SI Appendix, section S10.

Article-Level Metrics. We assess research outcomes and direction using two primary metrics: citation-based impact and novelty. Impact is measured by identifying “hit papers,” defined as those in the top 5% of the citation distribution within a given subfield and year (67) (see SI Appendix, section S6 for additional details). Novelty is measured using two approaches. First, we use the atypicality score, where papers with a 10th-percentile z-score below zero—based on Uzzi et al. (33)—are considered novel, relative to the whole scientific community. Second, to capture novelty with respect to individual research agendas, we apply a community detection approach (28, 68) using the Louvain algorithm (74) on each scholar’s cociting network over an 11-year window. In these networks, papers are nodes connected by weighted links based on shared references, and communities represent distinct research topics (SI Appendix, section S8). Robustness checks include alternative novelty measures (e.g., normalized novelty scores), alternative samples, and continuous indicators such as average normalized citations and novelty scores (SI Appendix, sections S6, S8, and S10).

Null Model and Regression Analysis. To analyze the timing of high-impact or novel work, we identify each scholar’s most cited and most novel paper within the 11-y window around tenure, ranking publications by normalized citations (67) (CF), or atypicality score (33). We then calculate the share of scholars whose top paper occurs in each year relative to tenure and compare these distributions to a null model in which impact or novelty is randomly shuffled within individual careers (56). This approach is extended using different data and normalized

novelty percentiles (see SI Appendix, section S7 for more details). To account for individual heterogeneity, we estimate fixed-effects regressions for publication count (Poisson), hit rate, and novelty rate (logistic), including paper-level covariates such as team size, number of references, lead author’s prior productivity, and publication type. Robustness checks include alternative specifications using OLS with normalized citation or novelty percentiles as outcomes (seeSI Appendix, section S11 for model specifications and additional details).

Data, Materials, and Software Availability. Some study data are available. Dataset D1, a licensed research dataset from the Academic Analytics Research Center (AARC), is accessible by contacting AARC directly at https://aarcresearch. com. Datasets D2 and D3, internal human resources datasets from two U.S. R1 universities, require a data use agreement with the universities; interested researchers should contact the authors for further information. Dataset D4 is a publicly available dataset (47) hosted on Figshare at https://doi.org/10.6084/ m9.figshare.c.6076908.v1. Datasets D5 and D6 are bibliometric databases from Scopus (https://www.scopus.com) and Dimensions (https://www.dimensions.ai), respectively. Dataset D7, licensed data from ProQuest (https://www.proquest. com), is accessible by contacting ProQuest directly.

ACKNOWLEDGMENTS. We thank all members of the Center for Science of Science and Innovation (CSSI) at Northwestern University, the audiences at ICSSI 2024 and IC2S2 2024 for thoughtful discussions, and A. Freilich for editing. We thank A. Olejniczak and the Academic Analytics Research Center for sharing the data. X.Z. and C.N. thank the International Center for the Study of Research Lab of Elsevier for sharing Scopus data and computation resources. This work is supported by the NSF 2404035, the Future Wanxiang Foundation, the Wisconsin Alumni Research Foundation, the Vilas Life Cycle Professorships, and the Institute for Humane Studies under grant no. IHS018809.

Author affiliations: aCenter for Science of Science and Innovation, Northwestern University, Evanston, IL 60208; bKellogg School of Management, Northwestern University, Evanston, IL 60208; cRyan Institute on Complexity, Northwestern University, Evanston, IL 60208; dNorthwestern Innovation Institute, Northwestern University, Evanston, IL 60208; eInformation School, University of Wisconsin–Madison, Madison, WI 53706; fNetwork Science Institute, Northeastern University, Boston, MA 02115; gNational Bureau of Economic Research, Cambridge, MA 02138; and hMcCormick School of Engineering, Northwestern University, Evanston, IL 60208

Author contributions: B.F.J., C.N., and D.W. designed research; G.T., X.Z., Y.Q., D.M., B.F.J., C.N., and D.W. performed research; G.T., X.Z., and Y.Q. analyzed data; G.T., X.Z., and Y.Q. collected data; G.T., X.Z., Y.Q., D.M., B.F.J., C.N., and D.W. interpreted results; G.T., X.Z., Y.Q., D.M., B.F.J., C.N., and D.W. edited the manuscript; and G.T., B.F.J., C.N., and D.W. wrote the paper.

- 1. AAUP, 1940 Statement of principles on academic freedom and tenure (2006). https://www.aaup. org/report/1940-statement-principles-academic-freedom-and-tenure.
- 2. B. Disraeli,Inaugural Address Delivered to the University of Glasgow Nov. 19, 1873; by Benjamin Disraeli. 2d Ed., Including the Occasional Speeches at Glasgow, Authorised Ed., Corr. by the Author (London Longmans, Green, 1873).
- 3. V. Bush, R. D. Holt,Science, the Endless Frontier (Princeton University Press, 2021).
- 4. D. Wang, A.-L. Barabási,The Science of Science (Cambridge University Press, 2021).
- 5. B. F. Jones, “Science and innovation: The under-fueled engine of prosperity” in Rebuilding the PostPandemic Economy, M. S. Kearney, A. Ganz, Eds. (Aspen Institute Press, Washington D.C., 2021). https://www.economicstrategygroup.org/publication/jones/.
- 6. S. Fortunato et al., Science of science.Science 359, eaao0185 (2018).
- 7. R. R. Nelson, The simple economics of basic scientific research.J. Polit. Econ. 67, 297–306 (1959).
- 8. J. Mokyr,The Gifts of Athena (Princeton University Press, 2002).
- 9. R. K. Merton,The Sociology of Science: Theoretical and Empirical Investigations (University of Chicago Press, Chicago, IL, 1979).
- 10. Y. Wang, Y. Qian, X. Qi, N. Cao, D. Wang, Innovationinsights: A visual analytics approach for understanding the dual frontiers of science and technology.IEEE Trans. Vis. Comput. Graph. 30, 518–528 (2024).
- 11. M. S. McPherson, M. O. Schapiro, Tenure issues in higher education.J. Econ. Perspect. 13, 85–98

(1999).

- 12. G. Manso, Motivating innovation.J. Finance 66, 1823–1860 (2011).
- 13. P. Azoulay, J. S. Graff Zivin, G. Manso, Incentives and creativity.RAND J. Econ. 42, 527–554 (2011).
- 14. W. B. MacLeod, M. Urquiola, Why does the United States have the best research universities? Incentives, resources, and virtuous circles.J. Econ. Perspect. 35, 185–206 (2021).
- 15. C. Kahn, G. Huberman, Two-sided uncertainty and ‘up-or-out’ contracts.J. Labor Econ. 6, 423–444

(1988).

- 16. M. Waldman, Up-or-out contracts: A signaling perspective.J. Labor Econ. 8, 230–250 (1990).
- 17. H. L. Carmichael, Incentives in academics: Why is there tenure? J. Polit. Econ. 96, 453–472 (1988).
- 18. A. Siow, Tenure and other unusual personnel practices in academia.J. Law Econ. Organ. 14, 152–173 (1998).


- 19. B. O’Flaherty, A. Siow, On the job screening, up or out rules, and firm growth.Can. J. Econ. Rev. Can. Econ. 25, 346–368 (1992).
- 20. B. O’Flaherty, A. Siow, Up-or-out rules in the market for lawyers.J. Labor Econ. 13, 709–735 (1995).
- 21. J. M. Malcomson, Work incentives, hierarchy, and internal labor markets.J. Polit. Econ. 92, 486–507

(1984).

- 22. L. Carmichael, Firm-specific human capital and promotion ladders.Bell J. Econ. 14, 251–258

(1983).

- 23. E. P. Lazear, S. Rosen, Rank-order tournaments as optimum labor contracts.J. Polit. Econ. 89, 841–864 (1981).
- 24. W. B. MacLeod, E. Riehl, J. E. Saavedra, M. Urquiola, The big sort: College reputation and labor market outcomes.Am. Econ. J. Appl. Econ. 9, 223–261 (2017).
- 25. S. B. Sitkin, Learning through failure - The strategy of small losses.Res. Organ. Behav. 14, 231–266

(1992)

- 26. Y. Wang, B. F. Jones, D. Wang, Early-career setback and future career impact.Nat. Commun. 10, 4331 (2019).
- 27. Y. Yin, Y. Wang, J. A. Evans, D. Wang, Quantifying the dynamics of failure across science, startups and security.Nature 575, 190–194 (2019).
- 28. L. Liu, N. Dehmamy, J. Chown, C. L. Giles, D. Wang, Understanding the onset of hot streaks across artistic, cultural, and scientific careers.Nat. Commun. 12, 5392 (2021).
- 29. R. Hill et al., The pivot penalty in research.Nature 642, 999–1006 (2025).
- 30. Q. Ke, E. Ferrara, F. Radicchi, A. Flammini, Defining and identifying sleeping beauties in science. Proc. Natl. Acad. Sci. U.S.A. 112, 7426–7431 (2015).
- 31. M. Ahmadpoor, B. F. Jones, The dual frontier: Patented inventions and prior scientific advance. Science 357, 583–587 (2017).
- 32. R. K. Merton, Singletons and multiples in scientific discovery: A chapter in the sociology of science. Proc. Am. Philos. Soc. 105, 470–486 (1961).
- 33. B. Uzzi, S. Mukherjee, M. Stringer, B. Jones, Atypical combinations and scientific impact.Science 342, 468–472 (2013).
- 34. J. Wang, R. Veugelers, P. Stephan, Bias against novelty in science: A cautionary tale for users of bibliometric indicators.Res. Policy 46, 1416–1436 (2017).


Downloaded from https://www.pnas.org by Korea Institute of Science and Technology KIST on March 24, 2026 from IP address 161.122.238.28.

- 35. J. N. Lane et al., Conservatism gets funded? A field experiment on the role of negative information in novel project evaluation.Manag. Sci. 68, 4478–4495 (2022).
- 36. S. Arts, L. Fleming, Paradise of novelty—or loss of human capital? Exploring new fields and inventive output.Organ. Sci. 29, 1074–1092 (2018).
- 37. T. P. Clement, How can we reform the STEM tenure system for the 21st Century? Proc. Natl. Acad. Sci. U.S.A. 119, e2207098119 (2022).
- 38. R. G. Carter et al., Innovation, entrepreneurship, promotion, and tenure.Science 373, 1312–1314

(2021).

- 39. A. Dance, Is it time for tenure to evolve? Nature 620, 453–455 (2023).
- 40. J. W. Holley, Tenure and research productivity.Res. High. Educ. 6, 181–192 (1977).
- 41. S. Li, H. Ou-Yang, Explicit incentives, implicit incentives, and performance: Evidence from academic tenure. SSRN Scholarly Paper (2010), 10.2139/ssrn.399240.
- 42. A. H. Yoon, Academic tenure.J. Empir. Leg. Stud. 13, 428–453 (2016).
- 43. J. Brogaard, J. Engelberg, E. Van Wesep, Do economists swing for the fences after tenure? J. Econ. Perspect. 32, 179–194 (2018).
- 44. K. R. Myers et al., Unequal effects of the COVID-19 pandemic on scientists.Nat. Hum. Behav. 4, 880–883 (2020).
- 45. M. Htun, Tenure and promotion after the pandemic.Science 368, 1075–1075 (2020).
- 46. J. Gao, Y. Yin, K. R. Myers, K. R. Lakhani, D. Wang, Potentially long-lasting effects of the pandemic on scientists.Nat. Commun. 12, 6188 (2021).
- 47. Z. Lin, Y. Yin, L. Liu, D. Wang, SciSciNet: A large-scale open data lake for the science of science research.Sci. Data 10, 315 (2023).
- 48. K. H. Wapman, S. Zhang, A. Clauset, D. B. Larremore, Quantifying hierarchy and dynamics in US faculty hiring and retention.Nature 610, 120–127 (2022).
- 49. A. Clauset, S. Arbesman, D. B. Larremore, Systematic inequality and hierarchy in faculty hiring networks.Sci. Adv. 1, e1400005 (2015).
- 50. E. Lee, A. Clauset, D. B. Larremore, The dynamics of faculty hiring networks.EPJ Data Sci.10, 1–25 (2021).
- 51. W. Dennis, Age and productivity among scientists.Science 123, 724–725 (1956).
- 52. S. M. Oster, D. S. Hamermesh, Aging and productivity among economists.Rev. Econ. Stat. 80, 154–156 (1998).
- 53. S. G. Levin, P. E. Stephan, Research productivity over the life cycle: Evidence for academic scientists. Am. Econ. Rev. 81, 114–132 (1991).
- 54. Y. Gingras, V. Larivière, B. Macaluso, J.-P. Robitaille, The effects of aging on researchers’ publication and citation patterns.PLoS One 3, e4048 (2008).
- 55. B. F. Jones, The burden of knowledge and the “death of the renaissance man”: Is innovation getting harder? Rev. Econ. Stud. 76, 283–317 (2009).


- 56. R. Sinatra, D. Wang, P. Deville, C. Song, A.-L. Barabási, Quantifying the evolution of individual scientific impact.Science 354, aaf5239 (2016).
- 57. L. Liu et al., Hot streaks in artistic, cultural, and scientific careers.Nature 559, 396–399 (2018).
- 58. S. Zhang, K. H. Wapman, D. B. Larremore, A. Clauset, Labor advantages drive the greater productivity of faculty at elite universities.Sci. Adv. 8, eabq7056 (2022).
- 59. M. Andalón, C. de Fontenay, D. K. Ginther, K. Lim, The rise of teamwork and career prospects in academic science.Nat. Biotechnol. 42, 1314–1319 (2024).
- 60. S. F. Way, A. C. Morgan, A. Clauset, D. B. Larremore, The misleading narrative of the canonical faculty productivity trajectory.Proc. Natl. Acad. Sci. U.S.A. 114, E9216–E9223 (2017).
- 61. S. Zhang, N. LaBerge, S. F. Way, D. B. Larremore, A. Clauset, Scientific productivity as a random walk. arXiv [Preprint] (2023). http://arxiv.org/abs/2309.04414 (Accessed 10 May 2024).
- 62. U. Gneezy, S. Meier, P. Rey-Biel, When and why incentives (don’t) work to modify behavior.J. Econ. Perspect. 25, 191–210 (2011).
- 63. D. Checchi, G. De Fraja, S. Verzillo, Incentives and careers in academia: Theory and empirical analysis.Rev. Econ. Stat. 103, 786–802 (2021).
- 64. S. Cole, Age and scientific performance.Am. J. Sociol. 84, 958–977 (1979).
- 65. P. D. Allison, J. A. Stewart, Productivity differences among scientists: Evidence for accumulative advantage.Am. Sociol. Rev. 39, 596–606 (1974).
- 66. P. D. Allison, J. S. Long, T. K. Krauze, Cumulative advantage and inequality in science.Am. Sociol. Rev. 47, 615–625 (1982).
- 67. F. Radicchi, S. Fortunato, C. Castellano, Universality of citation distributions: Toward an objective measure of scientific impact. Proc. Natl. Acad. Sci. U.S.A. 105, 17268–17272 (2008).
- 68. A. Zeng et al., Increasing trend of scientists to switch between topics.Nat. Commun. 10, 3439

(2019).

- 69. O. Kassotaki, Review of organizational ambidexterity research.Sage Open 12, 21582440221082127 (2022).
- 70. J. Li, Y. Yin, S. Fortunato, D. Wang, Scientific elite revisited: Patterns of productivity, collaboration, authorship and impact.J. R. Soc. Interface 17, 20200135 (2020).
- 71. G. J. Borjas, K. B. Doran, Prizes and productivity: How winning the Fields Medal affects scientific output.J. Hum. Resour. 50, 728–758 (2015).
- 72. L. Liu, B. F. Jones, B. Uzzi, D. Wang, Data, measurement and empirical methods in the science of science.Nat. Hum. Behav. 7, 1046–1058 (2023).
- 73. Y. Yang, T. Y. Tian, T. K. Woodruff, B. F. Jones, B. Uzzi, Gender-diverse teams produce more novel and higher-impact scientific ideas. Proc. Natl. Acad. Sci. U.S.A. 119, e2200841119 (2022).
- 74. V. D. Blondel, J.-L. Guillaume, R. Lambiotte, E. Lefebvre, Fast unfolding of communities in large networks.J. Stat. Mech. Theory Exp. 2008, P10008 (2008).


