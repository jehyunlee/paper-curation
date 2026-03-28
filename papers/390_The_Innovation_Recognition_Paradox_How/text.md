#### arXiv:2603.20597v1[cs.DL]21 Mar 2026

##### The Innovation Recognition Paradox: How Science Undervalues the Boundary-Crossing Work Women Produce

###### Carolina Biliotti1, Massimo Riccaboni2,3, Jeffrey W. Lockhart4, and James A. Evans5,6

1Department of Economics, European University Institute, San Domenico di Fiesole (FI), Italy 2AXES, IMT School for Advanced Studies Lucca, Italy 3IUSS, Pavia, Italy

- 4Department of Sociology, University of California, Berkeley, USA
- 5Department of Sociology & Knowledge Lab, University of Chicago, Illinois, USA 6Santa Fe Institute, New Mexico, USA


###### ABSTRACT

Women and men pursue different but complementary forms of scientific innovation. Analyzing 261,452 solo-authored papers by U.S. scholars, with patterns confirmed by millions of multi-authored articles, we show that women more often bridge distant disciplines through novel reference combinations, while men more often recombine concepts within fields. Women’s interdisciplinary innovations prove more disruptive and more prescient—yet science penalizes them for it. For equally innovative work, women’s papers land in lower-prestige journals and tend to receive less downstream citation credit, though their disruptive impact is greater. These gaps narrow only at extreme levels of novelty, suggesting women must produce exceptionally surprising work to achieve parity. Men’s within-field concept innovations, by contrast, attract recognition from disciplinary gatekeepers who control careers. The asymmetry reveals not a deficit in women’s contributions but a reward structure that systematically undervalues the boundary-crossing work most likely to transform fields.

###### 1 Introduction

Scientific innovation requires novelty, ideas and insights that diverge from established knowledge1. Yet novelty itself is not monolithic. Innovation in science operates along two fundamental dimensions, each representing a distinct pathway to advancing knowledge. Content or concept novelty involves recombining concepts, methods, and findings within research domains2,3 – the kind of within-field advances that earn status and awards from disciplinary communities. Context or reference novelty connects disparate disciplines by drawing on literature from distant fields4,5 – the interdisciplinary bridging that originates from the periphery yet proves most disruptive to established paradigms2.

These represent fundamentally different innovation strategies with distinct implications for scientific progress. Content novelty reflects mastery within disciplinary boundaries, signaling deep expertise through new connections among ideas that disciplinary gatekeepers are most likely to recognize and reward2,6. Context novelty, by contrast, signals boundary-crossing that can read as lack of focus to traditional, disciplinary evaluators, even as it produces the disruptive insights that transform and spawn new fields7. Novel context combinations reflect violations of boundaries between fields and disciplines8,9, indicating interdisciplinary work10,11. Crucially, these two forms of innovation attract different audiences: content novelty garners citations from within a field, while context novelty draws attention from across disciplinary boundaries2. They also yield different impacts: content novelty advances within domains; context novelty reorganizes relationships between domains.

While both approaches to innovation may coexist in some work, separating these two kinds of innovation gives us a more complete picture of how innovation operates in scientific research2,12. If men and women differ in the strategies they pursue, and rewards favor one type over the other, persistent gender gaps may reflect institutional and cultural values rather than differences in productivity or quality, with implications for equality and fostering innovation.

Existing literature on gender and scientific innovation documents persistent disparities in the kinds of ideas pursued, the reception of those ideas, and the career returns to innovation. On average, men and women adopt different approaches to innovation13,14, influenced by gender expectations15 and fear of social backlash, which, under some circumstances, can lead women to avoid selection of overly unusual ideas16. Women’s novel contributions in science often experience lower uptake17,18, likely resulting in slower career advancement19,20 and under-representation in academic leadership21–24. Ill-structured reward systems may further reduce creativity, sometimes disproportionately for women25.

Much of the literature on gender gaps in innovation assesses aggregate indicators such as total citations26, disruption27, or

1

journal placement28,29, which can obscure heterogeneity in contributions. Evidence on novel content combinations is mixed: women show higher novelty in patents30 and U.S. PhD theses17, but lower rates in biomedical dissertations31. Other research examines novel combinations of references across fields9,32.

Some of these innovation measures are bespoke, and most research does not evaluate comparable forms. The most comprehensive prior attempt to link diversity, innovation, and scientific rewards is Hofstra et al.17, who analyzed ∼1.2 million U.S. doctoral dissertations and showed that underrepresented groups introduce novel concept pairs at higher rates, yet their innovations receive less uptake and yield lower career returns—a “diversity–innovation paradox.” This landmark finding established the broad phenomenon, but its design leaves critical questions unresolved. Hofstra et al. measure only one form of novelty—new concept co-occurrences extracted from dissertation abstracts—conflating what we distinguish as content and context innovation. Their measure of adoption is raw future co-occurrence counts, with a separate measure of how ‘distal’ those connections are, rather than a unified model-based estimate of how surprising a combination was relative to evolving scientific expectations. And their outcome is career attainment (continued publishing, becoming a PhD supervisor), not paper-level recognition, leaving open whether the paradox operates through journal placement, citation credit, disruptive impact on specific contributions, or some other pathway. As we show, distinguishing content from context novelty does not merely refine the paradox—it reverses one of its key premises: women do not uniformly innovate more than men. They innovate differently, contributing more boundary-spanning reference novelty while men contribute more within-field concept novelty. The reward asymmetry is thus not a blanket penalty for innovation by women but a structural devaluation of the specific kind of innovation women disproportionately produce.

###### 1.1 Our Framework

We analyze per-paper gender differences in investment and returns to scientific innovation by proposing a unified approach that seeks to address these limitations. First, we distinguish between two dimensions of novelty: content novelty that involves combining research concepts, versus context novelty that involves bridging disciplines by connecting distant venues. A published discovery involving a new combination of contents may surprise because it has never before succeeded, even if previously considered and attempted33,34. A discovery drawing upon a divergent combination of sources may surprise because it has neither been attempted nor imagined. Considering both offers a more complete picture of how innovation operates2,12. Prior work that measures only concept-level novelty17 necessarily attributes all innovation differences to a single dimension, obscuring the possibility that demographic groups specialize in complementary forms of novelty with different reward profiles.

Second, we consider the innovative influence of novel contributions, distinguishing between those that are merely surprising at the time of publication – introducing combinations that defy current trends in science2 – and those that prove prescient, driving or anticipating future directions of research. A paper is surprising to the extent it introduces connections between empirically distant concepts or journals in ways that differ from trajectories at time of publication. Surprising ideas may prove prescient by anticipating future research trends, either through their innovative influence on others or the foresight of their originators35. This distinction separates the adoption of ideas from citation-based credit, allowing for the possibility that the first people working on an idea may not be credited or even remembered when it is later popularized. It further allows us to distinguish between surprising research that is ephemeral from that which changes or anticipates the course of science. Surprise and prescience are illustrated both for novel contexts and contents in Figure 1.

By combining these dimensions, we can evaluate whether published papers by men and women differ in content and context novelty, whether their contributions to each are equally prescient, and whether they receive comparable rewards for similar levels of innovation.

###### 1.2 Why Innovation Approaches and Rewards May Be Gendered

Gender differences in investment and returns to novelty arise from multiple factors. Under some circumstances, women manifest greater risk-aversion than men36. Novel content combinations within a discipline are distinct from novel connections across disciplines37, and these two kinds of novelty may entail different risks, which could explain gendered differences in innovation investment. Social sanctions and cultural expectations framing creativity as masculine15,16 may discourage competition for unusual ideas within fields, whereas interdisciplinary work may avoid such disciplinary scrutiny and sanction38. Access to diverse scientific networks may further shape opportunities for women to pursue and be recognized for innovative research39.

In terms of scientific recognition, women consistently receive less credit for comparable work—across citations21,26,40, authorship22,41, journal placement28,29, and the adoption of ideas18. Team composition and network position can mitigate some gaps: higher shares of women in teams can boost disruption27,42, and women occupying structural holes benefit more when producing novel and disruptive work43. Yet innovative work remains particularly vulnerable to being overlooked or misattributed5,15,44, suggesting gender gaps may be amplified for highly novel contributions.

- a
- b


Prescient

Surprising Unsurprising

Surprising

Surprising

Unsurprising Unsurprising

###### Context (reference) Prescience

###### Content (concept) Prescience

neuromorphic computing

Physical Review Letters

(journals / conferences)

(keywords / phrases)

International Conference on Learning Representations (ICLR)

blockchain

high-energy density

Mathematical Genome Sociology

cosmology beyond standard model

miRNA

Biology

- Figure 1. Illustration describing and contrasting context and content prescience. a, Contrast between three papers (represented as hypergraphs), ha, hb, and hc. hc is unsurprising in the first time period, t0, but also in t1 because its components are close together in the manifold (Θ) and both are highly visible (R) to scientists in both periods. hb, by contrast, is surprising in t0 (its components are distant in Θ), but it becomes no less surprising in the next period. ha, on the other hand, is surprising in t0, but it changes the scientific world by t1 to make it normal or common; its components are distant in Θ at t0 but become close by t1. Only ha is prescient. b, Illustration of the difference between context prescience, which involves the shift from a surprising journal and conference combination within a paper’s reference list to a routine one, and content prescience, which involves the shift from divergent concepts or keywords to familiar ones over time.


- 1.3 Methods and Contributions We analyze 261,452 solo-authored papers published between 2000 and 2023 by 141,786 U.S.-based scholars, using data from OpenAlex45. Focusing on solo-authored work allows us to attribute innovation to individual scholars without ambiguity from team composition, collaboration norms, or gendered credit allocation46. Because no large-scale self-reported gender database exists, we impute gender from names using Genderize.io and follow best-practice recommendations by restricting to high-confidence cases and demographic groups where name–gender signals are most reliable (white and Hispanic authors in the U.S. context)47. In supplementary analyses, we relax these restrictions and include multi-authored papers. These findings remain broadly consistent, though interpretation requires caution given assumptions about author order and the well-documented tendency for men to receive disproportionate credit for team creativity48,49.


We examine women’s participation in surprising science, measured as how unlikely or unexpected a combination of concepts (i.e., content novelty) or cited sources (i.e., context novelty) is at the time of publication, given current trends2. Unlike novelty measures based only on whether something appears first or how it deviates from a random or typical work4,5, our approach accounts for the overall distance of ideas and the evolution of their relationships over time across the scientific literature. We use trained classifiers on hypergraphs of concepts and citations to dynamically learn what to expect in a given year’s publications from recent historical trends2.

This model-based approach to measuring surprise contrasts with approaches that identify novelty through first co-occurrences of concept pairs and measure adoption through raw reuse counts17. By estimating the probability of a combination given the evolving geometry of scientific knowledge, our surprise scores distinguish genuinely unexpected connections from merely rare ones, and our prescience scores capture whether ideas were ahead of their time rather than merely repeated. Moreover, we analyze published papers rather than dissertation abstracts, and measure paper-level recognition—journal placement, disruption, and downstream citation credit that illuminate prior work on career outcomes17.

We then examine the role of gender in prescient work, where scientists introduce ideas (concept or source combinations) before they become widely adopted. Such papers are ahead of their time, making connections unusual at publication but common in subsequent science50.

We assess the recognition received by women’s contributions to surprising and prescient publications using three metrics:

- (1) two-step citation credit, which measures the extent to which a paper continues to be credited not just by papers that cite it, but papers that cite those papers as well; (2) five-year disruption score51, which evaluates how well a focal paper overshadows prior literature; and (3) journal placement, assessed by the two-year journal impact factor. Together, these metrics capture both the ability of innovative research to displace prior work and the degree to which it retains credit over time. Our research design is summarized in Figure 2.


Data Collection (October 2023) Beyond Year +2

Publication Year 0 Publication Year + 2

Journal Impact Factor Two-step Credit

OpenAlex

focal paper

Prescience

Surprise

one-step citations (direct)

![image 1](The Innovation Recognition Paradox How Science Undervalues the Boundary-Crossing_images/imageFile1.png)

Time

![image 2](The Innovation Recognition Paradox How Science Undervalues the Boundary-Crossing_images/imageFile2.png)

two-step citation (downstream)

US single authors

###### Adoption Disruption

PredictRace + Genderize.io

Rosa G.

![image 3](The Innovation Recognition Paradox How Science Undervalues the Boundary-Crossing_images/imageFile3.png)

sources cited by focal paper

Time focal paper

Anna K. David H. Rosa G.

![image 4](The Innovation Recognition Paradox How Science Undervalues the Boundary-Crossing_images/imageFile4.png)

![image 5](The Innovation Recognition Paradox How Science Undervalues the Boundary-Crossing_images/imageFile5.png)

![image 6](The Innovation Recognition Paradox How Science Undervalues the Boundary-Crossing_images/imageFile6.png)

one-step citations (direct)

- Figure 2. Summary of empirical framework. We collect a snapshot of data from OpenAlex45 as of October 2023 on single-authored papers published by authors with affiliations in the US. Authors’ names in papers are used to select names that appear to be white/hispanic. We then employ Genderize.io to infer gender with high probability. We measure surprising science, "unexpected" at time of publication, and prescient contributions that drive the future or are "ahead of their time". A paper can propose innovative combinations of (i) concepts (level-three topics) or (ii) references. We evaluate gender differences in returns by considering (i) two-step credit, (ii) five-year disruption score, and (iii) journal impact factor.


Our study makes three significant contributions. First, we document per-paper gendered investments in different types of novelty: papers authored by women are more likely to bring together innovative combinations of sources in their reference lists, while men’s works are more likely to combine concepts within fields. Second, we examine the degree to which such work is prescient – driving or anticipating future research trends – and find gender variation in which ideas "catch on". Third, we assess whether equally innovative papers receive equal recognition, finding consistent evidence of gender disparities in returns to innovation.

Taken together, our analysis provides a unified framework for measuring scientific innovation and demonstrates how gender shapes both the production of innovative papers and the rewards they generate. By moving beyond within-field concept combinations alone, we show that women’s contributions to innovation through boundary-spanning reference combinations and

broader disciplinary integration would otherwise remain overlooked. We further demonstrate that gender differences persist even when comparing papers with comparable levels of innovation.

###### 2 Results

###### 2.1 Gendered Approaches in Innovation Strategies

We begin by examining whether solo-authored papers by men and women differ in scientific novelty, measured with surprise, and innovation, measured with prescience. Using paper-level regressions (equation 5, "Materials and Methods"), we examine how an author’s gender relates to these novelty measures while controlling for publication year and research field, as well as the author’s career stage and department size; novelty scores are normalized within fields to ensure comparability. Controlling for these covariates allows us to estimate gender gaps in novelty and scholarly rewards without conflating them with structural differences in field composition, academic age, institutional resources, or time trends in publishing52,53.

Focusing on solo-authored work ensures that the gender coefficient reflects paper-level differences between women and men. Standard errors are clustered at the author level for solo-authored papers, and heteroskedastic errors are used when comparing solo- and multi-authored work, where clustering is less appropriate.

Figure 3 reveals striking gender differences in innovation patterns. Women’s work tends to be more innovative in context novelty—producing reference combinations that are significantly more surprising (b=.0258, P<.001) and prescient (b=.0241, P<.001) than men’s. This means women’s solo-authored papers draw on combinations of sources across disciplines that are more unexpected at the time of publication and more likely to anticipate future interdisciplinary trends.

Conversely, papers by men are more likely to develop content novelty, producing concept combinations within fields that are more surprising (b=.00525, P<.001) and prescient (b=.00773, P<.001) than women’s work. This indicates men’s papers more successfully combine previously disconnected concepts in ways that presage future developments within their fields. See Table 4 of the SI file for full regression estimates.

This is not a deficit on either side—it represents divergent, complementary approaches to advancing science. This finding revises a central claim of the diversity–innovation paradox17: that underrepresented groups uniformly innovate at higher rates. When innovation is measured along a single dimension—concept novelty—men’s papers are, on average, more innovative. Women’s greater innovation emerges when we consider context novelty, the dimension that prior work did not measure. The paradox is thus not that women innovate more and benefit less, but that the form of innovation women disproportionately pursue is the form scientific fields most undervalue. Woman-authored papers are more likely to transgress disciplines, while man-authored papers remix concepts within them. And as we demonstrate next, these strategies face profoundly unequal recognition.

Overall, papers by women tend to entail combinations of sources that are more unexpected at the time of publication than papers from men. Further, women’s interdisciplinary innovations experience higher uptake in the future, foreshadowing emerging trends more than men’s innovations of the same kind. On the other hand, papers by men are more likely to combine concepts that were previously distant. In this kind of innovation, men’s papers are more likely to presage the future of the field. This finding extends to multi-authored papers, where the main variable of interest is the proportion of female authors (Table 28, Section I of the SI file). Testing how gender differently predicts surprise and prescience of new science among solo and multi-authored papers, the same pattern holds, although it is attenuated in multi-author work relative to solo author work (Sections J, Table 32).

###### Context (Reference) Combinations Content (Concept) Combinations Paper Counts by Gender

200k

0.555

| | | | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |


0.61

women

men

175k

0.60

0.550

150k

Predicted Score

0.59

0.545

women

125k

men

0.58

Count

100k

0.540

0.57

75k

0.535

0.56

50k

0.55

25k

0.530

0.54

0k

Surprise Prescience Surprise Prescience

Men Women

- Figure 3. Gender difference in innovation strategies for solo-authored papers, alongside 95% confidence intervals, and sample distribution of gender in counts (thousands), with clustered standard error at the author level (117 583 clusters). Women engage in more context novelty (first panel) – bridging disciplines through reference combinations – while men engage in more content novelty (second panel) – recombining concepts within fields. Both surprise (how unexpected at publication) and prescience (how much ideas catch on) show this gender difference in investment. Dots indicate predicted values, averaged over the observed distributions of covariates (career age, department size, publication year, and level-one research field). Solo-authored papers are disproportionately authored by men (third panel).


Gender differences in scientific novelty remain robust in unconditional models without covariates (Section D, SI) and when controlling individually for career age, department size, and field (Section E.1, SI), suggesting that these factors explain only a small portion of the observed gender differences in our solo-authored setting.

Novelty in women’s solo-authored papers benefits relatively more from an increasing proportion of women in their field (a "critical mass" effect;54, Section F.1, SI) and from larger department size (Section F.2, SI). Across career cohorts (Section F.3), women’s work leads in prescient and surprising references but lags in concept novelty, although gender differences in concept science shrink as careers progress. Fields such as economics, mathematics, and philosophy — where solo-authored work is highly valued and women face greater career penalties19,20,55,56 — do not show lower levels of innovation among women-authored papers (Section F.5).

While contributions by women may feature highly unusual idea combinations, potentially contributing to slower uptake17, gender differences in prescience diminish as the initial surprise of a solo-authored paper increases (Section G, Table 21). Reference novelty is more closely related to citations, whereas content novelty is associated with status and awards2. Using past citations as a proxy for author status, we find a positive and significant gender–status interaction for concept prescience (Section F.4), suggesting that women benefit relatively more from their reputation in terms of uptake when producing work in which they are typically underrepresented.

- 2.2 Content and Context Novelty Attract Different Forms of Recognition Before examining gender differences in rewards, we first establish that content and context novelty attract distinct forms of recognition, reflecting different innovation strategies within the prestige economy of science. Awards and community recognition tend to favor novel combinations of concepts from within disciplines, whereas novel reference combinations transgress disciplinary boundaries but lead to more outsized citations across the fields of science2. To examine this, we analyze how surprise scores relate to the share of citations coming from outside versus inside a paper’s field, using Web of Science subfield classifications.


Figure 4 shows linear predictions of outside-field citation shares by gender as a function of concept and context surprise. Context surprise attracts more outside-field citations, while content surprise draws attention predominantly from within-field peers. Across all levels of surprise, women’s papers receive a higher share of outside-field citations, whereas men’s papers receive more within-field citations (inside-field share = 1 - outside-field share). Because awards and prestige are largely conferred by disciplinary insiders, content novelty is more directly rewarded in academic evaluation systems, while context novelty may allow women to produce trans-discplinary and potentially disruptive work without equivalent recognition from disciplinary gatekeepers. These patterns suggest that equally innovative contributions may be rewarded differently by gender

(Section H, SI).

0.54

0.56

35

| |women men<br><br>mean<br><br>estimate<br><br>count| | | | | | | |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |


| |count<br><br>mean<br><br>estimate| | | | | | | |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |


20.0

0.52

0.54

30

17.5

0.50

0.52

25

Outside Subject Citation Share

Outside Subject Citation Share

15.0

0.48

0.50

Counts (thousands)

Counts (thousands)

20

12.5

0.46

0.48

10.0

14

0.44

0.46

7.5

10

0.42

0.44

5.0

5

0.40

0.42

2.5

0.38

0.40

0

0.0

0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0

Context (Reference) Surprise Content (Concept) Surprise

- Figure 4. Content and context novelty attract different audiences. Surprising reference combinations (context novelty, left) correlate with more outside-subject citations and fewer within-field citations. Surprising concept combinations (content novelty, right) show the opposite pattern. Women’s solo-authored work attracts more cross-field attention than men’s for both innovation types, while men’s work dominates within-field citations. The y axis traces the outside-subject citation share, computed as the number of citations from outside subject over total citations. Estimated relations are inverted for inside citation share, which is equal to (1−Outside Subject Citation Share). Predicted values are marginalized over the observed distribution of covariates (department size, career age, level-one field, open access status, and publication year). Lines represent fitted linear regression models with clustered standard errors at the author level, plotted over side-by-side histograms of surprise by gender (counts in thousands). Diamonds indicate the sample mean of scholarly rewards within each surprise interval, by gender.


- 2.3 Asymmetric Rewards for Equally Innovative Science Having established gender differences in innovation types and shown that these types attract different audiences, we now examine whether equally innovative contributions receive equal rewards. We estimate paper-level linear regression models with interactions between surprise or prescience scores and author gender, examining three measures of recognition: journal placement (log two-year journal impact factor), downstream citation credit (two-step credit), and disruptive impact (five-year disruption score) – see equation (6), and details in ‘Materials and Methods’.


- 2.3.1 Rewards to Surprising Science We begin by discussing gender differences in how surprise is related to rewards, with regression estimates reported in Table S5.


Journal placement tends to disadvantage women’s contributions. Reference surprise has no significant association with journal prestige (β=.004, P=.48), while concept surprise is negatively associated with journal impact (β=-.03, P<.001). Women’s papers secure lower journal placement than men’s for both reference (β=-.066, P<.001) and concept surprise (β=-.065, P<.001).

Nevertheless, women’s papers gain relatively more in journal prestige for increasing surprise of contributions: as reference or concept surprise rises, women’s work climbs in journal prestige faster than men’s (reference interaction β=.041, P<.001; concept interaction β=.046, P<.001). When papers are authored by women, the negative association between concept surprise and journal placement reverses (Figure 5, first row). This suggests that papers by women who commit to higher signaling efforts – as by producing more surprising science – can achieve parity in treatment57. Multi-authored patterns show that teams with higher proportions of women also end up in less impactful journals, with women’s contributions having lower marginal returns with increasing reference surprise (Section I, Table 31) – which differs from the solo-authored case. We address this difference later, in the Robustness and Sensitivity Analyses section.

Disruptive impact tells a different story. Both reference innovation (β=.006, P<.001) and concept innovation (β=.0018, P<.001) are more disruptive in papers authored by women. Disruption decreases with increasing reference surprise (β=-.0127, P<.001), however, with women-authored papers penalized more steeply (interaction β=-.0078, P<.001). For concept surprise, we find no significant effect on disruption at baseline (β = .00008, P = .8), but gender gaps in disruption narrow as reference surprise increases (interaction β=-.0014, P=.024) – papers by women start with higher disruption but converge with men’s at extreme novelty (Figure 5, second row). We find similar patterns in multi-authored papers (Section I, Table 30).

Two-step credit declines with increasing surprise in both references (β = -.012, P < .001) and concepts (β = -.0018, P = .001), showing that the effect is much stronger for reference (context) novelty. This indicates that highly unusual work is less likely to be cited two steps downstream, with context novelty particularly penalized. Women’s work earns significantly less credit than men’s for equal content novelty (β = -.0146, P = .026), but not for reference novelty (β = -.001, P = .20). Gender differences in downstream credit show no statistically significant interaction with content novelty (β = .0006, P = .55) or reference novelty (β = .001, P = .47). Figure 5 (third row) presents predicted two-step credit by surprise across genders. In multi-authored papers, a higher share of women is associated with lower downstream credit for equal concept novelty and reference novelty, similar to the solo-authored case, while simultaneously yielding significantly higher marginal returns for surprising reference combinations. These effects are larger for context than for content novelty, consistent with the solo-authored results (Section I, Table 29).

- 2.3.2 Rewards to Prescient Science


Next, we estimate the gender gap in how prescience in solo-authored papers gets rewarded in terms of two-step credit and five-year disruption (Table 6 of the SI file). We do not include journal impact factor, as its timing precedes prescience – prescience is computed considering how much less unexpected combinations become two years after publication, while journal impact factor reflects how papers cite past work in the journal at the year of publication.

Disruptive impact depends critically on innovation type (Figure 6, row one). Higher prescience in concepts increases disruption (β=.0012, P<.001), but higher prescience in references reduces it (β=-.012, P<.001). This latter effect is expected mechanically: papers with prescient combinations of sources by definition are followed by others repeating those combinations of sources, lowering disruption metrics but not the innovative value of the work.

Women’s solo-authored papers are more disruptive than comparable men’s work by both measures (references β=.0057, P<.001; concepts β=.0014, P=.001), but face a steeper decline in disruption as reference prescience rises (interaction β=-.0075, P<.001), narrowing the gender gap at high novelty levels. Instead, no significant gender difference emerges for concept prescience (interaction β=-.0006, P=.3). Multi-author teams with more women also experience greater disruption losses with increasing reference prescience (Section I, Table 30).

Two-step credit declines with prescience in both references (β = -.011, P < .001) and concepts (β = -.01, P < .001). This pattern is expected to some extent: when science follows new trends, attention tends to concentrate on the latest literature. However, it also indicates that early work on a popular innovation is less likely to receive credit than more incremental, "normal science". Across all levels of concept prescience, women’s papers are less likely to be cited two steps out (β = -.0024, P = .002), whereas no gender difference is observed for reference prescience (β = -.0003, P = .79). Once again, conditional gender differences in two-step credit show no statistically significant interaction with reference prescience (interaction β = -0.0007, P = .56) and are weakly significant when interacted with concept prescience (interaction β = .002, P = .052). Figure 6, second row, reports the predicted values of two-step credit by prescience. Papers by mixed-gender teams display patterns consistent with solo-authored papers (see Table S29).

1.4

1.4

| |women<br><br>men<br><br>mean<br><br>estimate<br><br>count| | | | | | | |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
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


Counts (thousands)

Counts (thousands)

20 15 10

###### Journal Impact

30

DisruptionJournal Impact2-Step Credit

1.3

1.3

20

1.2

1.2

10

1.1

1.1

5 0

0

1.0

1.0 0.004

40

0.030

Counts (thousands)Counts (thousands)

| | | | | | | | | |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |


| |women mean men<br><br>estimate<br><br>count| | | | | | | |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |


25 20 15 10

Counts (thousands)Counts (thousands)

Disruption

30

0.020

0.002

20

0.010

0.000

10

0.000

5 0

0 25 20 15 10

-0.010 0.055 0.050 0.045 0.040 0.035 0.030 0.025

-0.002 0.0425

12 10

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
| | | | | | | | | |
| | | | | | | | | |


0.0400 0.0375 0.0350 0.0325 0.0300

2-Step Credit

8 6 4 2 0

5 0

0.0 0.2 0.4 0.6 0.8 1.0

0.0 0.2 0.4 0.6 0.8 1.0

Context (Reference) Surprise

Content (Concept) Surprise

- Figure 5. Rewards to surprising science by gender in solo-authored papers, alongside 95% confidence intervals, with clustered standard errors at the author level. For equally surprising science, women’s work lands in lower-prestige journals (row 1) and receives less citation credit for concept combinations (row 3, right panel). Women’s work is more disruptive (row 2), but this advantage narrows as surprise increases. Gender gaps in journal placement narrow at high surprise levels, indicating women must produce exceptionally surprising work to achieve parity. Predicted outcomes are marginalized over the observed distribution of covariates (department size, career age, level-one field, open access status, and publication year – plus citations and JIF for disruption). Lines represent fitted linear regression models, plotted over side-by-side histograms of surprise by gender (counts in thousands). Diamonds indicate sample means.


0.004 0.003 0.002 0.001 0.000

0.025 0.020 0.015 0.010 0.005 0.000

| |women mean men<br><br>estimate<br><br>count| | | | | | | |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
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
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |


30

25

25

Counts (thousands)

###### Counts (thousands)Counts (thousands)

20

2-Step CreditDisruption

20

Disruption

15

15

10

10

- -0.001
- -0.002
- -0.003 0.055


- -0.005
- -0.010
- -0.015


5

5

0 20.0 17.5 15.0 12.5 10.0

0

0.050

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
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |


| |women<br><br>men<br><br>mean<br><br>estimate<br><br>count| | | | | | | |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |


12 10

0.050

0.045

Counts (thousands)

0.045

2-Step Credit

0.040

8 6 4 2 0

0.040

0.035

7.5 5.0 2.5 0.0

0.035

0.030

0.030

0.025

0.025

0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0

Context (Reference) Prescience

Content (Concept) Prescience

- Figure 6. Rewards to prescient science by gender in solo-authored papers, alongside 95% confidence intervals, with clustered standard errors at the author level. Women earn relatively more credit for increasing prescience in concept combinations (row 2, right panel), suggesting that women who commit to higher signaling efforts by investing in more surprising science can achieve treatment parity in areas where they are typically fewer. Women’s disruption advantage erodes as reference prescience increases (row 1, left panel). Predicted outcomes are marginalized over observed distribution of covariates (department size, career age, level-one field, open access status, and publication year – and 2-years citations and JIF for disruption). Lines represent fitted linear regression models, plotted over side-by-side histograms of prescience by gender (counts in thousands). Diamonds indicate sample means.


- 2.3.3 Robustness and Heterogeneity Analysis We conduct a series of robustness checks. Estimates of gender differences in returns to surprise and prescience in solo-authored papers are stable across alternative outcome measures, including three-year disruption and five-year journal impact (SI, Sections K–L), when conditioning on funding listed in papers or authors’ past citations (SI, Section M), and when considering both types of innovation simultaneously (Section N). Generalized additive models confirm that the linear specification captures most of the relationship between novelty, prescience, and rewards, but perhaps understates gender differences at the extremes (SI, Section P).


Controlling for baseline surprise, gender differences in rewards to prescience vanish for the most unexpected science but emerge for papers with low to moderate initial surprise, across both reference and concept novelty (SI, Section G). As surprise and prescience increase, women’s work receives relatively lower marginal returns in direct citations, measured by two-year forward counts, except for surprise in concept combinations, where no citation penalty is evident (SI, Section O).

Prior work suggests that estimating gender effects requires accounting for differences in academic age, research field, and other compositional factors, because aggregated apples-to-oranges comparisons can differ substantially from comparisons of similar researchers in similar contexts52,53,58. In our data, unconditional estimates of gender differences in journal placement and disruption closely match the fully specified model (SI, Section D, Tables S8 and S10), and controlling for individual covariates -— career age, time trends, department size, or research field —- does not alter these results (SI, Section E.2, Tables S12–S13).

By contrast, gender gaps in downstream citations are sensitive to specification: conditioning on field effects alone reverses

the unconditional gender coefficient, reflecting women’s greater representation in lower-citation-intensity fields, while fully specified models recover a negative gender coefficient, indicating aggregate disadvantages that outweigh within-field effects (Sections D–E.2, SI; Tables 9 and 14).

Finally, gender gaps in journal placement and disruption narrow more rapidly with increasing surprise and prescience in solo-authored than in multi-authored work (Section J), consistent with collaboration-related penalties55. Considering genderhomogeneous teams and non-linear effects of women’s shares in multi-authored papers, all-women papers earn higher marginal returns in journal prestige to increasing surprise than all-men papers, consistent with patterns observed in solo-authored work; other outcomes are discussed in the SI (SI, Section Q).

###### 3 Discussion

Our findings reveal a troubling paradox at the heart of scientific reward systems. Women and men tend to pursue differentbut equally valuable—innovation strategies, yet face profoundly asymmetric rewards. Women’s works engage in more discipline-spanning work that proves most disruptive to established knowledge. Men’s papers tend more to recombine content within-domains, which earns recognition from disciplinary gatekeepers. For equally innovative contributions, women’s works land in lower-prestige journals, tend to receive less downstream citation credit, while manifesting greater disruptive impact—especially at lower levels of novelty where gender gaps are widest.

Critically, these gaps tend to narrow—sometimes even reverse—at the highest levels of surprise and prescience, suggesting that extreme signals of innovation can override gender penalties. The appropriate interpretation is not that women succeed at the highest levels, but rather that their contributions persistently face disadvantage at all other levels representing the vast majority of scientific production.

- 3.1 Differences Reflect Structural Position The patterns we document likely do not reflect innate differences in capability or preference, but rather structural biases in how innovation is recognized and how scientists are positioned within knowledge networks. Content novelty aligns with traditional markers of disciplinary mastery and signals belonging within a field’s intellectual tradition. Context novelty, while potentially more transformative, signals outsider status and can be read as a lack of focus by evaluators embedded in single disciplines7.

Women’s greater investment in context novelty likely stems from multiple, mutually reinforcing mechanisms. Women may have restricted access to central network positions within disciplines39, making cross-boundary connections more feasible than deep within-field integration. Women may face exclusion from within-field status hierarchies, reducing returns to within-domain innovation38. They may strategically avoid highly unusual ideas within their home field due to risks of social backlash16, finding it safer to import legitimated ideas from other fields. Gender expectations about creativity itself may code within-field innovation as more masculine15. Instead, interdisciplinary research may attract women, as cross-field scientific contributions are rarely constrained by established social structures or scientific communities, as with domain publications38.

Regardless of origin, the consequence is clear: the work women disproportionately produce—disruptive, interdisciplinary, prescient context-bridging innovation—is the work science most undervalues. Context novelty attracts cross-field citations but not the within-field recognition that determines careers. Indeed, women’s solo-authored papers receive a higher share of citations from outside their field at every level of surprise (Figure 4), a pattern that aligns with—but is not mechanically entailed by—their greater investment in field-bridging reference novelty. This cross-field attention, while reflecting genuine impact, falls outside the within-field recognition systems that determine tenure, promotion, and awards. Women’s prescient innovations that draw ideas from multiple disciplines, anticipating interdisciplinary trends, go under-credited as later adopters receive the recognition they deserve.

- 3.2 Self-Selection Cannot Explain Asymmetric Rewards Could self-selection explain these patterns? Women pursuing context-spanning work might be concentrated in lower-prestige positions, which could affect recognition. We find this explanation unlikely. Variations in department size, past citations, and career stage do not eliminate gender gaps in novelty or prescience (SI Sections D–F). If self-selection were driving the results, we would expect similar patterns across all women’s work. Instead, we observe penalties specifically for context novelty and convergence at extreme levels of surprise. Gender differences also vary by outcome. Women’s papers gain relatively more journal prestige from concept surprise than men’s (Figure 5, row 1), contrary to what a general self-selection account would predict. Moreover, self-selection into lower-citation fields is unlikely to drive our results, as we control for field differences and normalize novelty and prescience scores to ensure comparability across disciplines. Solo-authored patterns align with multi-authored work, indicating that results are not confined to specific team structures (Section I, SI).


Gendered preferences alone are unlikely to explain these patterns. Women’s content novelty increases disproportionately with department size and with women’s share in the field. For indicators of status and experience (career age and prior citations),

effects are not statistically significant (Section F, SI). As women accumulate seniority, status, and institutional resources, they tend to engage more in within-field novelty, consistent with an account acknowledging agency and institutional positioning.

Overall, the patterns we observe are more consistent with the devaluation of boundary-crossing innovations than with individual sorting. Evaluators appear to respond differently to observably identical innovations based on author gender and innovation type, discounting the interdisciplinary, boundary-crossing work in which women disproportionately invest energy.

- 3.3 Implications for Understanding Gender Inequality in Science Our unified framework clarifies conflicting findings in prior literature. Studies that focus solely on concept-based novelty miss women’s substantial contributions to context-bridging innovation—precisely the work that proves most transformative for science. Studies examining only aggregate citations or journal placements would overlook the undervaluation of interdisciplinary work. By distinguishing content from context novelty and measuring both surprise and prescience, we uncover gendered patterns in innovation strategies and the asymmetry in how these contributions are rewarded.

The narrowing of gender gaps at extreme novelty levels helps explain why some studies find gender parity among elite scientists: those studies examine only the most exceptional work, where women have overcome disadvantage through extraordinary innovation17. Our findings also clarify why Hofstra et al. observed a blanket innovation premium for underrepresented groups: their single novelty dimension—new concept pairs in dissertation abstracts—blends what we show are two distinct phenomena with opposite gender associations. By separating content from context novelty, we reveal that the diversity–innovation paradox is more precisely a diversity–recognition paradox: women’s boundary-crossing innovations are not merely discounted in aggregate but are structurally undervalued by the disciplinary gatekeepers who allocate prestige, such as journal placement and editorial access. Furthermore, by analyzing paper-level outcomes rather than career trajectories, we identify the specific mechanisms—lower journal placement, reduced two-step credit at baseline, and steeper penalties in disruptive impact for increasing novelty—through which the paradox operates on individual contributions. The paradox is thus sharper and more actionable than previously understood: it is not simply that innovative outsiders have worse careers, but that specific papers producing specific kinds of innovation receive less recognition, paper by paper, systematically.

Conditioning on initial surprise, men’s and women’s highly unexpected, prescient papers receive similar recognition, indicating that gender matters less for the most innovative work. We find no evidence that gender differences are concentrated in fields. Instead, larger departments and critical mass enhance novelty and uptake of women’s papers, and past citation-based prestige encourages investment in concept-based innovation.

Evaluators may interpret surprising work differently across genders due to uncertainty and hindsight bias59, and prior studies suggest women face harsher scrutiny60,61. Future research should develop measures to assess how conflicting prior evidence affects evaluations of solo-authored work by men and women.

- 3.4 Policy Implications Our findings suggest several concrete interventions. First, evaluation criteria should explicitly value interdisciplinary impactcitations from outside one’s field, disruption scores, cross-boundary influence—not only within-field recognition. Tenure and promotion committees should be trained to recognize that context-bridging work may not accumulate traditional prestige markers even when highly influential62.

Second, because gender gaps narrow at extreme surprise, perhaps double-anonymous review or requirements for "novelty impact statements" could help evaluators focus on work quality rather than author identity. Anonymization alone is insufficient if evaluators systematically discount interdisciplinary work regardless of author, however, or if other signals, such as writing style, correlate with both gender and scientific rewards63.

Third, journals and funding agencies could track and report their own patterns of gender bias in recognizing different innovation types. Making institutions accountable for whether they systematically undervalue context-bridging work could catalyze reform.

Fourth, mentoring and advising should acknowledge the distinct challenges discipline-bridging work faces. Rather than coaching women toward more "recognized" innovation styles (i.e. those typical of men), we should reform reward structures to appropriately value the interdisciplinary work women already produce.

- 3.5 Strong Warning Against Discriminatory Measurement We caution strongly against interpreting these findings as grounds for creating gender-specific "novelty accounting systems". Some might propose adjusting how we measure women’s contributions to account for differences in approaches and strategies in novelty —for example, weighting interdisciplinary citations more heavily for women’s works or using different evaluation criteria by gender. This would be misguided.


The problem is not that we are measuring the wrong things – it is that we are valuing the wrong things. Context-bridging innovation drives paradigm shifts, reorganizes relationships between fields, and produces long-term impact that within-field citations fail to capture. These contributions should be valued equally regardless of who produces them. Similarly, most

scientific work is not radical innovation, but normal science contributions64 to a robust knowledge base. This work is also systematically undervalued when authored by women. Creating separate evaluation systems by gender would institutionalize rather than remedy discrimination, implicitly accepting that women’s work deserves different (lesser) treatment.

The appropriate response is to reform reward structures for all scientists, explicitly recognizing that multiple pathways to innovation exist and that interdisciplinary, boundary-crossing work merits equal recognition to within-field advances. Any policy response must center on changing how science values different types of innovation, not on adjusting measurements to account for gender differences in what gets produced.

- 3.6 Limitations and Future Directions In order to have high confidence in our results, given the dangers of imputation over heterogeneous populations47, we focus on solo-authored papers from U.S. institutions with high-certainty gender inference. This emphasis on quality introduces sampling bias that limits generalization. To improve external validity, we relax our constraints and find that patterns remain consistent when extending to multi-authored papers and across multiple robustness checks, suggesting that the findings are not artifacts of sample restrictions. We cannot rule out all confounding influences, but the pattern of interactions provides strong evidence against simple omitted variable explanations. Moreover, defining novelty as surprise in the combination of contents and contexts poses limits what is identified as novelty, failing to capture novelty that builds incrementally, or appears elsewhere in a paper (e.g., a dataset or dataset combination65). Finally, our study focuses on gender differences in novelty, prescience, and rewards at the paper level, meaning we do not examine how these factors translate into long-term career trajectories or cumulative scientific influence.

Future research should investigate mechanisms of innovation production and evaluation more deeply. Do evaluators consciously discount interdisciplinary work, or does the structure of peer review disadvantage context-bridging innovations? Do women’s peripheral network positions limit their ability to cite and be cited by central figures? How do gender expectations about what constitutes "serious" versus "peripheral" science shape evaluations of novelty? How do race, ethnicity, institutional prestige, and other dimensions of marginalization interact with gender14?

- 3.7 Conclusion Women-authored papers are more likely to bridge disciplines through context-spanning innovation; men’s production is more likely to advance within domains through content-recombining innovation. Both strategies advance science, but they are not given equal recognition. The work women disproportionately produce—disruptive, interdisciplinary, prescient—is undervalued by existing reward structures across contexts, even as it drives paradigm shifts and long-term impact. Women must produce exceptionally surprising or prescient work to overcome this disadvantage, and even then, they can face discounting in journal placement and allocation of credit at the paper level.


These patterns reveal more than gender gaps—they expose fundamental tensions in how science recognizes innovation. Our institutions reward disciplinary mastery over boundary-crossing6, within-field status over cross-field influence34, and conventional markers of prestige over disruptive impact. As science grows increasingly specialized and interconnected, this misalignment between what we value and what drives progress will become more consequential2.

Reforming these structures requires more than addressing explicit bias. It demands rethinking what counts as a valuable scientific contribution, how we measure impact, and whose work we center in narratives of innovation. Until reward systems appropriately value multiple pathways to advancing knowledge, gender inequality in science will persist—not despite women’s contributions, but because of them.

###### References

- [1] Yi Zhao and Chengzhi Zhang. “A review on the novelty measurements of academic papers”. In: ArXiv abs/2501.17456

(2025). URL: https://api.semanticscholar.org/CorpusID:275954035.

- [2] Feng Shi and James Evans. “Surprising combinations of research contents and contexts are related to impact and emerge with scientific outsiders from distant disciplines”. In: Nature Communications 14 (Mar. 2023). DOI: 10.1038/s41467023-36741-4.
- [3] ALEXANDER M. PETERSEN. “EVOLUTION OF BIOMEDICAL INNOVATION QUANTIFIED VIA BILLIONS OF DISTINCT ARTICLE-LEVEL MeSH KEYWORD COMBINATIONS”. In: Advances in Complex Systems 25.01

(2022), p. 2150016. DOI: 10.1142/S0219525921500168. eprint: https://doi.org/10.1142/S0219525921500168. URL: https://doi.org/10.1142/S0219525921500168.

- [4] Brian Uzzi, Satyam Mukherjee, Michael Stringer, and Ben Jones. “Atypical Combinations and Scientific Impact”. In: Science 342.6157 (2013), pp. 468–472. DOI: 10.1126/science.1240474. eprint: https://www.science.org/doi/pdf/10.1126/ science.1240474. URL: https://www.science.org/doi/abs/10.1126/science.1240474.


- [5] Jian Wang, Reinhilde Veugelers, and Paula Stephan. “Bias against novelty in science: A cautionary tale for users of bibliometric indicators”. In: Research Policy 46.8 (2017), pp. 1416–1436. ISSN: 0048-7333. DOI: https://doi.org/10. 1016/j.respol.2017.06.006. URL: https://www.sciencedirect.com/science/article/pii/S0048733317301038.
- [6] Michael Szell, Yifang Ma, and Roberta Sinatra. “A Nobel opportunity for interdisciplinarity”. In: Nature Physics 14.11

(2018), pp. 1075–1078.

- [7] Jacob Gates Foster, Feng Shi, and James Evans. “Surprise! Measuring Novelty as Expectation Violation”. In: 2021. URL: https://api.semanticscholar.org/CorpusID:242436797.
- [8] You-Na Lee, John P. Walsh, and Jian Wang. “Creativity in scientific teams: Unpacking novelty and impact”. In: Research Policy 44.3 (2015), pp. 684–697. ISSN: 0048-7333. DOI: https://doi.org/10.1016/j.respol.2014.10.007. URL: https://www.sciencedirect.com/science/article/pii/S0048733314001826.
- [9] Yang Yang, Tanya Y. Tian, Teresa K. Woodruff, Benjamin F. Jones, and Brian Uzzi. “Gender-diverse teams produce more novel and higher-impact scientific ideas”. In: Proceedings of the National Academy of Sciences 119.36 (2022), e2200841119. DOI: 10.1073/pnas.2200841119. eprint: https://www.pnas.org/doi/pdf/10.1073/pnas.2200841119. URL: https://www.pnas.org/doi/abs/10.1073/pnas.2200841119.
- [10] Henrique Pinheiro, Matt Durning, and David Campbell. “Do women undertake interdisciplinary research more than men, and do self-citations bias observed differences?” In: Quantitative Science Studies 3.2 (June 2022), pp. 363–392. ISSN: 2641-3337. DOI: 10.1162/qss_a_00191. eprint: https://direct.mit.edu/qss/article-pdf/3/2/363/2031908/qss\_a\_00191.pdf. URL: https://doi.org/10.1162/qss%5C_a%5C_00191.
- [11] Erin Leahey, Christine M. Beckman, and Taryn L. Stanko. “Prominent but Less Productive: The Impact of Interdisciplinarity on Scientists’ Research*”. In: Administrative Science Quarterly 62.1 (2017), pp. 105–139. DOI: 10. 1177/0001839216665364. eprint: https://doi.org/10.1177/0001839216665364. URL: https://doi.org/10.1177/ 0001839216665364.
- [12] Xuanmin Ruan, Weiyi Ao, Dongqing Lyu, Ying Cheng, and Jiang Li. “Effect of the topic-combination novelty on the disruption and impact of scientific articles: Evidence from PubMed”. In: Journal of Information Science 0.0

(2023). DOI: 10.1177/01655515231161133. eprint: https://doi.org/10.1177/01655515231161133. URL: https: //doi.org/10.1177/01655515231161133.

- [13] Mathias Wullum Nielsen, Jens Peter Andersen, Londa Schiebinger, and Jesper W. Schneider. “One and a half million medical papers reveal a link between author gender and attention to gender and sex analysis”. In: Nature Human Behaviour 1.11 (Nov. 2017), pp. 791–796. DOI: 10.1038/s41562-017-0235-x. URL: https://ideas.repec.org/a/nat/nathum/ v1y2017i11d10.1038_s41562-017-0235-x.html.
- [14] Diego Kozlowski, Vincent Larivière, Cassidy R. Sugimoto, and Thema Monroe-White. “Intersectional inequalities in science”. In: Proceedings of the National Academy of Sciences 119.2 (2022), e2113067119. DOI: 10.1073/pnas.

2113067119. eprint: https://www.pnas.org/doi/pdf/10.1073/pnas.2113067119. URL: https://www.pnas.org/doi/abs/10. 1073/pnas.2113067119.

- [15] Snehal Hora, G. James Lemoine, Ning Xu, and Christina E. Shalley. “Unlocking and closing the gender gap in creative performance: A multilevel model”. In: Journal of Organizational Behavior 42.3 (2021), pp. 297–312. DOI: https://doi.org/10.1002/job.2500. eprint: https://onlinelibrary.wiley.com/doi/pdf/10.1002/job.2500. URL: https://onlinelibrary.wiley.com/doi/abs/10.1002/job.2500.
- [16] Mengzi Jin and Roy Chua. “Which Idea to Pursue? Gender Differences in Novelty Avoidance During Creative Idea Selection”. In: Organization Science 35.6 (2024), pp. 2223–2248. DOI: 10.1287/orsc.2022.16176. eprint: https: //doi.org/10.1287/orsc.2022.16176. URL: https://doi.org/10.1287/orsc.2022.16176.
- [17] Bas Hofstra, Vivek V. Kulkarni, Sebastian Munoz-Najar Galvez, Bryan He, Dan Jurafsky, and Daniel A. McFarland. “The Diversity–Innovation Paradox in Science”. In: Proceedings of the National Academy of Sciences 117.17 (2020), pp. 9284–9291. DOI: 10.1073/pnas.1915378117. eprint: https://www.pnas.org/doi/pdf/10.1073/pnas.1915378117. URL: https://www.pnas.org/doi/abs/10.1073/pnas.1915378117.
- [18] Wei Cheng and Bruce Weinberg. “Marginalized and Overlooked? Minoritized Groups and the Adoption of New Scientific Ideas”. In: Journal of Labor Economics 43.1 (2025), pp. 83–119. DOI: 10.1086/725551. eprint: https: //doi.org/10.1086/725551. URL: https://doi.org/10.1086/725551.
- [19] Donna K. Ginther and Shulamit Kahn. “Women in Economics: Moving Up or Falling Off the Academic Career Ladder?” In: Journal of Economic Perspectives 18 (2004), pp. 193–214. URL: https://api.semanticscholar.org/CorpusID:154803018.


- [20] Ramin A. Skibba. “Women in physics”. In: Nature Reviews Physics 1 (2019), pp. 298–300. URL: https : / / api . semanticscholar.org/CorpusID:188491266.
- [21] Junming Huang, Alexander J. Gates, Roberta Sinatra, and A L Barabasi. “Historical comparison of gender inequality in scientific careers across countries and disciplines”. In: Proceedings of the National Academy of Sciences of the United States of America 117 (2019), pp. 4609–4616.
- [22] Marc J Lerchenmueller, Olav Sorenson, and Anupam B Jena. “Gender differences in how scientists present the importance of their research: observational study”. In: BMJ 367 (2019). DOI: 10.1136/bmj.l6573. eprint: https: //www.bmj.com/content/367/bmj.l6573.full.pdf. URL: https://www.bmj.com/content/367/bmj.l6573.
- [23] Erin Hengel. “Publishing While Female: are Women Held to Higher Standards? Evidence from Peer Review”. In: The Economic Journal 132.648 (May 2022), pp. 2951–2991. ISSN: 0013-0133. DOI: 10.1093/ej/ueac032. eprint: https://academic.oup.com/ej/article-pdf/132/648/2951/46859083/ueac032\_online\_appendix.pdf. URL: https: //doi.org/10.1093/ej/ueac032.
- [24] Michael H. K. Bendels, Eileen M. Wanke, Norman Schöffel, Jan Bauer, David Quarcoo, and David Alexander Groneberg. “Gender equality in academic research on epilepsy—a study on scientific authorships”. In: Epilepsia 58 (2017).
- [25] Wei Wei, Paola Criscuolo, and Bárbara Larrañeta. “Inventors’ Expected Rewards for Ownership Transfer of Their Ideas and Gender Effects on Creativity”. In: Academy of Management Proceedings 2024.1 (2024), p. 13477. DOI: 10.5465/AMPROC.2024.12bp. eprint: https://doi.org/10.5465/AMPROC.2024.12bp. URL: https://doi.org/10.5465/ AMPROC.2024.12bp.
- [26] Matthew Ross, Britta Glennon, Raviv Murciano-Goroff, Enrico Berkes, Bruce Weinberg, and Julia Lane. “Women are Credited Less in Science than are Men”. In: Nature 608 (June 2022), pp. 1–2. DOI: 10.1038/s41586-022-04966-w.
- [27] Ming-Ze Zhang, Tang-Rong Wang, Peng-Hui Lyu, Qi-Mei Chen, Ze-Xia Li, and Eric W.T. Ngai. “Impact of gender composition of academic teams on disruptive output”. In: Journal of Informetrics 18.2 (2024), p. 101520. ISSN: 1751-

1577. DOI: https://doi.org/10.1016/j.joi.2024.101520. URL: https://www.sciencedirect.com/science/article/pii/ S1751157724000336.

- [28] Luke Holman, Devi Stuart-Fox, and Cindy E. Hauser. “The gender gap in science: How long until women are equally represented?” In: PLOS Biology 16.4 (Apr. 2018), pp. 1–20. DOI: 10.1371/journal.pbio.2004956. URL: https: //doi.org/10.1371/journal.pbio.2004956.
- [29] Michael H. K. Bendels, Ruth Müller, Doerthe Brueggmann, and David A. Groneberg. “Gender disparities in high-quality research revealed by Nature Index journals”. In: PLOS ONE 13.1 (Jan. 2018), pp. 1–21. DOI: 10.1371/journal.pone.

0189136. URL: https://doi.org/10.1371/journal.pone.0189136.

- [30] Jieshu Wang and Andrew Maynard. “Gender disparity in U.S. patenting”. English (US). In: Humanities and Social Sciences Communications 12.1 (Dec. 2025). Publisher Copyright: © The Author(s) 2025. ISSN: 2055-1045. DOI: 10.1057/s41599-025-06038-6.
- [31] Meijun Liu, Zihan Xie, Alex Jie Yang, Chao Yu, Jian Xu, Ying Ding, and Yi Bu. “The prominent and heterogeneous gender disparities in scientific novelty: Evidence from biomedical doctoral theses”. In: Information Processing & Management 61.4 (2024), p. 103743. ISSN: 0306-4573. DOI: https://doi.org/10.1016/j.ipm.2024.103743. URL: https://www.sciencedirect.com/science/article/pii/S0306457324001031.
- [32] Alex J. Yang, Ying Ding, and Meijun Liu. “Female-led teams produce more innovative ideas yet receive less scientific impact”. In: Quantitative Science Studies 5.4 (Nov. 2024), pp. 861–881. ISSN: 2641-3337. DOI: 10.1162/qss_a_00335. eprint: https://direct.mit.edu/qss/article-pdf/5/4/861/2482658/qss_a_00335.pdf. URL: https://doi.org/10.1162/qss_a_ 00335.
- [33] Andrey Rzhetsky, Jacob G Foster, Ian T Foster, and James A Evans. “Choosing experiments to accelerate collective discovery”. In: Proceedings of the National Academy of Sciences 112.47 (2015), pp. 14569–14574.
- [34] Jacob G Foster, Andrey Rzhetsky, and James A Evans. “Tradition and innovation in scientists’ research strategies”. In: American sociological review 80.5 (2015), pp. 875–908.
- [35] Paul Vicinanza, Amir Goldberg, and Sameer B. Srivastava. “A deep-learning model of prescient ideas demonstrates that they emerge from the periphery”. In: PNAS Nexus 2 (2022). URL: https://api.semanticscholar.org/CorpusID:254429423.
- [36] Julie A. Nelson. “Are women really more risk-averse than men? A re-analysis of the literature using expanded methods”. en. In: Journal of Economic Surveys 29.3 (July 2015), pp. 566–585. ISSN: 0950-0804, 1467-6419. DOI: 10.1111/joes.


12069. URL: https://onlinelibrary.wiley.com/doi/10.1111/joes.12069 (visited on 08/18/2025).

- [37] Magda Fontana, Martina Iori, Fabio Montobbio, and Roberta Sinatra. “New and atypical combinations: An assessment of novelty and interdisciplinarity”. In: Research Policy 49.7 (2020), p. 104063. ISSN: 0048-7333. DOI: https://doi.org/10. 1016/j.respol.2020.104063. URL: https://www.sciencedirect.com/science/article/pii/S0048733320301414.
- [38] Diana Rhoten and Stephanie Pfirman. “Women in interdisciplinary science: Exploring preferences and consequences”. In: Research Policy 36.1 (2007), pp. 56–75. ISSN: 0048-7333. DOI: https://doi.org/10.1016/j.respol.2006.08.001. URL: https://www.sciencedirect.com/science/article/pii/S0048733306001338.
- [39] Adrián A. Díaz-Faes, Paula Otero-Hermida, Müge Ozman, and Pablo D’Este. “Do women in science form more diverse research networks than men? An analysis of Spanish biomedical scientists”. In: PLOS ONE 15.8 (Aug. 2020), pp. 1–21. DOI: 10.1371/journal.pone.0238229. URL: https://doi.org/10.1371/journal.pone.0238229.
- [40] Vincent Larivière, Étienne Vignola-Gagné, Christian Villeneuve, Pascal Gélinas, and Yves Gingras. “Sex differences in research funding, productivity and impact: an analysis of Québec university professors”. In: Scientometrics 87 (2011), pp. 483–498. URL: https://api.semanticscholar.org/CorpusID:18916353.
- [41] Giovanni Filardo, Briget da Graca, Danielle M Sass, Benjamin D Pollock, Emma B Smith, and Melissa Ashley-Marie Martinez. “Trends and comparison of female first authorship in high impact medical journals: observational study (1994-2014)”. In: BMJ 352 (2016). DOI: 10.1136/bmj.i847. eprint: https://www.bmj.com/content/352/bmj.i847.full.pdf. URL: https://www.bmj.com/content/352/bmj.i847.
- [42] Nazha Gali. “Team Gender Composition Impact on the Production of Disruptive Research”. In: Academy of Management Proceedings 2022.1 (2022), p. 10167. DOI: 10.5465/AMBPP.2022.10167abstract. eprint: https://doi.org/10.5465/ AMBPP.2022.10167abstract. URL: https://doi.org/10.5465/AMBPP.2022.10167abstract.
- [43] Yue Wang, Ning Li, Bin Zhang, Qian Huang, Jian Wu, and Yang Wang. “The effect of structural holes on producing novel and disruptive research in physics”. In: Scientometrics 128 (2023), pp. 1801–1823. ISSN: 1588-2861. DOI: 10.1007/s11192-023-04635-3. URL: https://doi.org/10.1007/s11192-023-04635-3.
- [44] Wayne Johnson and Devon Proudfoot. “Greater Variability in Judgments of the Value of Novel Ideas”. In: SSRN Electronic Journal (2024). URL: https://api.semanticscholar.org/CorpusID:269391142.
- [45] Jason Priem, Heather Piwowar, and Richard Orr. OpenAlex: A fully-open index of scholarly works, authors, venues, institutions, and concepts. 2022. arXiv: 2205.01833 [cs.DL].
- [46] Margaret W. Rossiter. “The Matthew Matilda Effect in Science”. en. In: Social Studies of Science 23.2 (May 1993), pp. 325–341. ISSN: 0306-3127. (Visited on 11/29/2018).
- [47] Jeffrey W. Lockhart, Molly M. King, and Christin L. Munsch. “Name-based demographic inference and the unequal distribution of misrecognition”. In: Nature Human Behaviour (2023), pp. 1–12. URL: https://api.semanticscholar.org/ CorpusID:258188890.
- [48] Devon Proudfoot, Aaron C. Kay, and Christy Z. Koval. “A Gender Bias in the Attribution of Creativity: Archival and Experimental Evidence for the Perceived Association Between Masculinity and Creative Thinking”. In: Psychological Science 26.11 (2015). PMID: 26386015, pp. 1751–1761. DOI: 10.1177/0956797615598739. eprint: https://doi.org/10. 1177/0956797615598739. URL: https://doi.org/10.1177/0956797615598739.
- [49] Aleksandra Luksyte, Kerrie L. Unsworth, and Derek R. Avery. “Innovative work behavior and sex-based stereotypes: Examining sex differences in perceptions and evaluations of innovative work behavior”. In: Journal of Organizational Behavior 39.3 (2018), pp. 292–305. DOI: https://doi.org/10.1002/job.2219. eprint: https://onlinelibrary.wiley.com/doi/ pdf/10.1002/job.2219. URL: https://onlinelibrary.wiley.com/doi/abs/10.1002/job.2219.
- [50] Jeffrey W. Lockhart, Jamshid Sourati, Feng Shi, and James Evans. “China leads scientific trends; the West launches new ones”. In: (2025). arXiv: 2603.01117. URL: http://arxiv.org/abs/2603.01117.
- [51] Russell J. Funk and Jason Owen-Smith. “A Dynamic Network Measure of Technological Change”. In: Management Science 63.3 (2017), pp. 791–817. DOI: 10.1287/mnsc.2015.2366.
- [52] Chunhai Gao, Sabika Khalid, NGUYEN Van Thang, and Endale Tadesse. “Comparing Apples With Apples: Women Faculty Research Productivity in Vietnamese Higher Education”. In: Sage Open 13.3 (2023), p. 21582440231184847. DOI: 10.1177/21582440231184847. eprint: https://doi.org/10.1177/21582440231184847. URL: https://doi.org/10.1177/ 21582440231184847.


- [53] Philip Ball, T. Benjamin Britton, Erin Hengel, Philip Moriarty, Rachel A. Oliver, Gina Rippon, Angela Saini, and Jessica Wade. “Gender issues in fundamental physics: Strumia’s bibliometric analysis fails to account for key confounders and confuses correlation with causation”. In: Quantitative Science Studies 2.1 (Apr. 2021), pp. 263–272. ISSN: 2641-3337. DOI: 10.1162/qss_a_00117. eprint: https://direct.mit.edu/qss/article-pdf/2/1/263/1906537/qss_a_00117.pdf. URL: https://doi.org/10.1162/qss_a_00117.
- [54] Derek J. de Solla Price. Little science, big science ... and beyond. eng. New York, NY: Columbia Univ. Pr., 1986. ISBN: 978-0-231-04956-6 978-0-231-04957-3. URL: http://www.andreasaltelli.eu/file/repository/Little_science_big_science_ and_beyond.pdf.
- [55] Heather Sarsons. “Recognition for Group Work: Gender Differences in Academia”. In: American Economic Review 107.5 (May 2017), pp. 141–45. DOI: 10.1257/aer.p20171126. URL: https://www.aeaweb.org/articles?id=10.1257/aer. p20171126.
- [56] Ming-Te Wang and Jessica L Degol. “Gender Gap in Science, Technology, Engineering, and Mathematics (STEM): Current Knowledge, Implications for Practice, Policy, and Future Directions”. In: Educational Psychology Review 29

(2017), pp. 119–140. URL: https://api.semanticscholar.org/CorpusID:207122445.

- [57] Denis Trapido. “The Female Penalty for Novelty and the Offsetting Effect of Alternate Status Characteristics”. In: Academy of Management Proceedings 2021.1 (2021), p. 10557. DOI: 10.5465/AMBPP.2021.10557abstract. eprint: https://doi.org/10.5465/AMBPP.2021.10557abstract. URL: https://doi.org/10.5465/AMBPP.2021.10557abstract.
- [58] José Ignacio Conde-Ruiz, Miguel Díaz-Salazar, Juan José Ganuza, and Manu García. “Citation gender gaps in top economics journals”. In: SERIEs (2025). URL: https://api.semanticscholar.org/CorpusID:280042129.
- [59] David Tan. “The Road Not Taken: Technological Uncertainty and the Evaluation of Innovations”. In: Organization Science 34.1 (2023), pp. 156–175. DOI: 10.1287/orsc.2021.1567. eprint: https://doi.org/10.1287/orsc.2021.1567. URL: https://doi.org/10.1287/orsc.2021.1567.
- [60] Corinne A. Moss-Racusin, John F. Dovidio, Victoria L. Brescoll, Mark J. Graham, and Jo Handelsman. “Science faculty’s subtle gender biases favor male students”. In: Proceedings of the National Academy of Sciences 109.41 (2012), pp. 16474–16479. DOI: 10.1073/pnas.1211286109. eprint: https://www.pnas.org/doi/pdf/10.1073/pnas.1211286109. URL: https://www.pnas.org/doi/abs/10.1073/pnas.1211286109.
- [61] Monica Biernat and Kathleen Fuegen. “Shifting Standards and the Evaluation of Competence: Complexity in GenderBased Judgment and Decision Making”. In: Journal of Social Issues 57.4 (2001), pp. 707–724. DOI: https://doi.org/ 10.1111/0022-4537.00237. eprint: https://spssi.onlinelibrary.wiley.com/doi/pdf/10.1111/0022-4537.00237. URL: https://spssi.onlinelibrary.wiley.com/doi/abs/10.1111/0022-4537.00237.
- [62] Aaron Gerow, Yuening Hu, Jordan Boyd-Graber, David M Blei, and James A Evans. “Measuring discursive influence across scholarship”. In: Proceedings of the national academy of sciences 115.13 (2018), pp. 3308–3313.
- [63] Marc J. Lerchenmueller, Olav Sorenson, and Anupam B. Jena. “Gender differences in how scientists present the importance of their research: observational study”. en. In: BMJ 367 (Dec. 2019). ISSN: 1756-1833. DOI: 10.1136/bmj. l6573. URL: https://www.bmj.com/content/367/bmj.l6573 (visited on 12/20/2019).
- [64] Thomas S Kuhn. The structure of scientific revolutions. Vol. 962. University of Chicago press Chicago, 1997.
- [65] Yulin Yu and Daniel M Romero. “Does the use of unusual combinations of datasets contribute to greater scientific impact?” In: Proceedings of the National Academy of Sciences 121.41 (2024), e2402802121.
- [66] Konstantinos Tzioumis. “Demographic aspects of first names”. In: Scientific Data 5 (2018).
- [67] Dean Keith Simonton. “Taking the U.S. Patent Office Criteria Seriously: A Quantitative Three-Criterion Creativity Definition and Its Implications”. In: Creativity Research Journal 24.2-3 (2012), pp. 97–106. DOI: 10.1080/10400419.2012.

676974. eprint: https://doi.org/10.1080/10400419.2012.676974. URL: https://doi.org/10.1080/10400419.2012.676974.

- [68] Satyam Mukherjee, Brian Uzzi, Ben Jones, and Michael Stringer. “A New Method for Identifying Recombinations of Existing Knowledge Associated with High-Impact Innovation”. In: Journal of Product Innovation Management 33.2

(2016), pp. 224–236. DOI: https://doi.org/10.1111/jpim.12294. eprint: https://onlinelibrary.wiley.com/doi/pdf/10.1111/ jpim.12294. URL: https://onlinelibrary.wiley.com/doi/abs/10.1111/jpim.12294.

- [69] Stephen F. Altschul, Thomas L. Madden, Alejandro A. Schäffer, Jinghui Zhang, Zheng Zhang, Webb Miller, and David J. Lipman. “Gapped BLAST and PSI-BLAST: a new generation of protein database search programs”. In: Nucleic Acids Research 25.17 (Sept. 1997), pp. 3389–3402. ISSN: 0305-1048. DOI: 10.1093/nar/25.17.3389. eprint: https: //academic.oup.com/nar/article-pdf/25/17/3389/3639509/25-17-3389.pdf. URL: https://doi.org/10.1093/nar/25.17.3389.


- [70] Xavier Sala-i-Martin. “The World Distribution of Income: Falling Poverty and ... Convergence, Period”. In: The Quarterly Journal of Economics 121.2 (2006), pp. 351–397. URL: https://EconPapers.repec.org/RePEc:oup:qjecon:v: 121:y:2006:i:2:p:351-397..
- [71] Mark R. Rosenzweig. “Thinking Small: Poor Economics: A Radical Rethinking of the Way to Fight Global Poverty: Review Essay”. In: Journal of Economic Literature 50.1 (Mar. 2012), pp. 115–27. DOI: 10.1257/jel.50.1.115. URL: https://www.aeaweb.org/articles?id=10.1257/jel.50.1.115.
- [72] Henry Etzkowitz, Carol Kemelgor, Michael Neuschatz, Brian Uzzi, and Joseph Alonzo. “The Paradox of Critical Mass for Women in Science”. In: Science (New York, N.Y.) 266 (Nov. 1994), pp. 51–4. DOI: 10.1126/science.7939644.


###### 4 Materials and Methods

- 4.1 Data collection and gender inference We collect data from OpenAlex45 on single authored papers published by authors with affiliation in the US, using a snapshot of the data as of October 2023 (1,774,303 unique authors).

We obtain accurate disambiguation of authors by using the OpenAlex identification codes of the OpenAlex v2 Author Name Disambiguation (AND) System.1 We employ the Genderize API to assign genders to first and middle names of authors. We infer the ethnicity of first names and surnames of authors using R package predictrace66. Then, we select the subset of authors from the US with an ethnicity where we know the Genderize error rates are low – white and latin/hispanic47. We are left with a subset of 1,105,268 unique authors, with 3,444 unique first names and 30,087 unique middle names.

Following the need for a conservative test, we consider an inferred gender reliable if the associated name is of high confidence, that is, if either the Genderize count is higher than 100, or the Genderize probability of assignment is above 0.90. We identify 22,747 first names of low confidence and a total of 460,902 middle names with low confidence. These names are set as missing. The distribution of Genderize counts and probabilities for first and middle names are reported in the SI file, Section A.

Next, we remove names given by single characters or initials, for which Genderize produces unreliable inferences. Middle names given by initials are also set as missing. Disagreeing cases of different inferred genders for first and middle are dropped from the sample. Authors whose first and middle names both resulted in missing values after the conservative processing procedure described above are also removed from the sample. We are left with a cleaned, reliable sample of 1,074,062 authors.

After merging the data on solo-authored papers, we obtain a sample of 713,684 solo-authored papers by 301,585 authors. In order to compare estimates of the gender differences on innovation and recognition on comparable samples, we focus exclusively on papers for which we observe all four measures of innovation – surprise and prescience in concepts and references – we are left with a final solo-authored sample of 226,208 unique papers by 141,786 unique authors (31% women and 69% men). Section B.1 of the SI file reports paper-level sample statistics.

Sample statistics at the author level indicate that men dominate mid- to late-career solo-authored contributions, whereas women are relatively well-represented in multi-authored work, particularly at early-career stages (SI file B.2, Figures 7–8). Solo-authors tend to come from smaller departments and, on average, have longer career experience than team-authors (SI file B.2, Figure 10). Because solo-authored papers are concentrated among mid- to late-career researchers and women are underrepresented in this group, analyses of gender differences in solo-authored work should account for career age. Conditioning on career stage ensures that observed differences in outcomes reflect gender rather than experience.

Solo-authors publish across all disciplines, with Biology, Medicine, and Computer Science as the main publication areas for both solo- and multi-authoring scholars (SI file B.2, Figure 9). As expected, solo-authorship is relatively more common in the humanities and social sciences, and the pattern of differences between solo and multi-authorship is similar for men and women (SI file B.2, Figure 10). Overall, these patterns underscore the importance of covariate adjustment to isolate gender-specific differences.

- 4.2 Surprise and Prescience Measures In OpenAlex, scientific topics of papers are not chosen by authors, as OpenAlex assigns topics to publications using an automated system, providing a fine-grained representation of concepts and identifying research at different levels: from broader fields like art, computer science, or economics (level-zero concepts), to more specific fields, such as machine learning, visual arts or ecology (level-one), and even more fine-grained topics resembling concepts, such as social identity theory, ecosystem services, biodiversity hotspot, or social benefits (level-three concepts). The higher the level, the more fine-grained the concept is.


We look at novelty of a paper in terms of combinations of (i) journals in its reference list (contexts), or (ii) concepts as fine-grained concepts of level three (contents).

1For more information, see https://github.com/ourresearch/openalex-name-disambiguation/tree/main/V2.

###### Formal Model of Surprise and Prescience

We construct a dynamic hypergraph Gt at each year t, in which hypernodes are either scientific concepts (level-three OpenAlex topics) or publication venues (journals), and hyperedges are papers, each connecting the set of concepts or venues co-occurring within it. For content novelty, nodes are concepts; for context novelty, nodes are cited journals.

Latent embedding and salience. For each node i, the model learns a latent vector θ(it) ∈ RD, where each entry θid(t) ≥ 0 and ∑d θid(t) = 1, representing the probability that node i belongs to latent dimension d at time t. These dimensions naturally recover scientific fields or disciplinary communities2. The model additionally assigns each node a scalar salience parameter ri(t) > 0, capturing its cognitive accessibility to scientists through cumulative frequency in the literature. The embedding is estimated from the sequence of hypergraphs {Gt′}t′≤t, allowing the latent space to evolve as the structure of science changes.

Expected propensity of a combination. Given a paper h (a hyperedge connecting a set of concept or venue nodes), the model’s expected propensity for that combination to appear in newly published work is:

λh(t) = ∑

###### ∏

θid(t)

i∈h

d

coherence

###### ×∏

ri(t)

, (1)

i∈h

salience

where the coherence term measures the probability that all nodes in h load onto the same latent scientific dimension, and the salience term captures the joint cognitive accessibility of those nodes to working scientists. The number of publications realizing

combination h in year t is modeled as a Poisson random variable with mean λh(t), and model parameters are estimated by maximum likelihood over the observed hypergraph. Across biomedical science, physics, and patents, this model distinguishes a

combination that appeared in a real publication from a randomly drawn combination in more than 95% of cases (AUC > 0.95)2. Surprise. The surprise of paper h at time t is the negative log-coherence of its combination:

S(t)(h) =−log∑

###### ∏

θid(t). (2)

i∈h

d

A high value of S(t)(h) indicates that the combination was improbable given the prevailing geometry of scientific knowledge—a low-probability event in the information-theoretic sense2. The salience term ∏iri(t) is excluded from the surprise score to isolate the structural improbability of the combination from the mere obscurity of its constituent nodes; rare nodes that are unsurprisingly paired yield low surprise, while common nodes combined across distant conceptual territory yield high surprise. We compute two distinct surprise scores for each paper: content surprise, Scon(t) (h), using combinations of level-three concept nodes, and context surprise, Sctx(t)(h), using combinations of cited journal nodes. These two scores are empirically uncorrelated, confirming that they capture orthogonal dimensions of novelty.

Prescience. Prescience measures the degree to which a paper’s combination, surprising at publication, became routine in subsequent science. We compute two surprise scores for each paper: one using the embedding from the publication year t0 and one using the embedding from two years later, t0 +2. Prescience is then defined as the decrease in surprisal over this interval:

Pcon(h) = Scon(t0)(h)−Scon(t0+2)(h), (3) Pctx(h) = Sctx(t0)(h)−Sctx(t0+2)(h). (4)

A large positive value of P(h) indicates that the paper was ahead of its time: its combination was unusual at publication but became predictable as subsequent science reorganized around it50. Crucially, prescience reflects the uptake of the ideas proposed in h, not citation-based credit accruing to h itself. Early contributions to a popular direction may receive little downstream citation even as their combinations become routine—precisely the dynamic motivating our separate examination of prescience and scholarly credit.

As this measure captures what is expected and what is unexpected based on current trends, surprising combinations are those unlikely to occur in the given year of publication, according to the model2. In other words, a surprising work is a publication that makes ’weird’, or improbable, combinations of contents or contexts.

Because the model can capture the improbability of published combinations each year, we can measure the change in papers’ surprise scores after publication. A decrease in surprise scores between the year of publication and two years after defines prescience scores – our second measure of interest. A prescient publication is one that was unusual at the time of publication

but becomes less unlikely and more commonly used, expected, or even assumed over time50. Importantly, prescience does not automatically imply the uptake of the paper, but rather reflects the uptake of ideas proposed in the paper. Ideas may become popular in the future, but prescient papers that drove or anticipated this evolution may receive different levels of adoption and credit.

As indicated by37, previous measures of innovation derived from average or random combinations of references may dangerously blur the lines between novelty and interdisciplinarity of a given paper. The measure of surprise in combinations of references we use in this paper captures how ideas distinctively connect diverging contexts in unexpected ways. Surprising science may well capture creativity and non-conventionality67, as the more surprising an idea is, the more it perceived as creative in its embedded context and therefore less conventional. This suggests that surprise blends novelty with unconventionality, or non-obviousness (as described by59), instead of blending novelty and conventionality to reflect innovative science4,68. This allows us to capture how combinations of references are non-obvious and surprising, rather than merely serving as a proxy for interdisciplinarity (i.e., the distance between connected fields) or merely capturing new or rare connections.

The two measures of surprise reflect different dimensions: reference and concept surprise show no correlation, and the same holds for prescience in concept and source combinations — see Figure 5 in the SI file.2 report69 as an example in which context and content surprise diverge, as the paper introduced a computer system to search DNA and protein databases, proposing an innovative tool used across computational and biomedical sciences, rather than producing a discovery in the biomedical or the computational science – achieving high surprise in references (97th percentile) but low in concepts (15th percentile). Surprise scores are capable of distinguishing creative science from dissemination and reviews that share the same topics:70 significantly influenced the study of global income distribution and poverty, with a surprise score in the top of the distribution (99th percentile of reference surprise), while71 provides a review of existing literature on global poverty and poverty economics, and is associated with very low surprise (10th percentile of reference surprise) – as expected.

After computing these scores, papers as concept (references) combinations will have one raw surprise score (at time of publication) and one raw prescience score (two years after the year of publication). But papers touch on multiple topics and multiple fields (i.e., fine-grained concepts of level one), and different research areas have different normal ranges of surprise scores. As every paper has multiple fields, it will have a rank in surprise with respect to each field that it belongs to. For example, if the focal paper is related to both sociology and computer science, that paper’s novelty score would put it in a different spot in each field’s ranking. To allow for comparison of novelty score across fields, we compute within-field percentile ranks of novelty scores for papers in our analysis.2 The percentile-ranked version of scores forces them between 0 and 1 – so the lowest observed surprise (prescience) value within a field will be 0.

As each paper has multiple novelty scores—one for each scientific field (level-one concepts) it addresses—we take the maximum surprise score and the maximum prescient score for the paper. This means that each paper will be uniquely identified by one surprise score and one prescient score, each corresponding to the paper’s maximal rank within related fields. The variables Surprise (References) and Prescience (References) denote the maximum surprise and prescience scores, respectively, with respect to the combination of journals in the reference list of the focal paper. Surprise (concepts) and Prescience (concepts) indicate the maximum surprise and prescience scores in the contents of the paper, using fine-grained concepts of level-three as contents.

We compute prescience as the change in a paper’s raw surprise score between its publication year and two years later. As a result, papers with very different initial surprise can have the same prescience score if their change in surprise places them similarly within the field-specific distribution. Converting prescience into percentile ranks allows us to compare papers across fields and provides insight into how papers by men and women are rewarded in science, as they occupy equal ranks within their distributions. Nevertheless, equal prescience ranks could reflect different initial surprise. To account for this, we examine gender differences in prescience conditional on increasing ranks of initial surprise (SI, Section G). In future work, we plan to explore this further, including extending the time horizon beyond two years to compute prescience.

- 4.3 Rewards Measures For each publication, we collect information regarding the research areas of interest as concepts fine-grained of level one, and disciplines related to the paper (concepts fine-grained of level zero), public accessibility of the paper, number of publications from the institution in the same field and year as the focal paper (Department Size)3, year and journal of publication, journal impact factor, and number of citations. We compute Career Age of an author as the number of years between the focal publication and the author’s first publication. It is set to missing if the career age exceeds 60 or if they have only one paper in their lifetime, as both are usually due to author disambiguation errors.


- 2The percentiles in each field are computed considering the full snapshot of OpenAlex data from October 2023 (more than 80 million unique papers), including non-US and multi-authored papers.
- 3As papers belong to multiple fields, we compute the number of publications from the institution in the same fields as the focal paper and we take the maximal value across fields.


Following51, we compute paper-level disruption scores, calculated five years after publication. Disruption varies between -1 and 1, where 1 indicates that the paper completely overshadows the previous literature, while a value equal to -1 indicates that the paper is only cited alongside the literature on which it builds.

We also compute the two-step credit, which is obtained as the ratio between the number of papers two-steps out that directly cite the focal paper and the number of papers that cite a paper that cites the focal paper. We compute the two-step credit from citation information collected up until October 2023. Two-step credit in the citation network is fairly difficult to secure (mean = .036, median = .025, 75th percentile = .043). As being able to retain credit down the citation cascade and building saliency is less obvious, we compute two-step credit for papers with more than five two-step citations. Two-step credit reflects how much future publication building on the focal paper will disrupt the focal paper: a value close to zero means that future work is overshadowing the contribution of the focal paper, a value close to one means that the paper is still being cited two-steps out in the citation network alongside the literature building upon it.

Finally, we retrieve the two-year impact factor, which reflects how papers today (i.e., at the time of publication of the focal paper) view the journal, considering citations to the journal’s publications from two years prior. This means it will not have citations to our focal paper, but represent how other scholars treat the journal in the same year that the focal paper is being published, considering publications in the journal from two years prior.

- 4.4 Multi-authored sample To quantify gender gaps in investment and rewards to surprising and prescient science by teams with varying female membership, we compute, for each paper, the share of women on the team. Because we can confidently infer the gender only for a subset of the authors (US with high confidence), we compute the share of women among team members with high-confidence inferred gender. Rather than identifying the overall female share in teams using low-confidence inferred genders, we focus on those team members for which gender is identified with higher confidence, i.e., for which an assumption on binary gender classes can be more easily formed. In other words, we interpret this measure as an indicator of how strongly teams signal a clear and unequivocal female presence to readers approaching the publication. For example, a publishing team whose members are John, Sam and Leslie (where both Leslie and Sam are common names for men and women in the US) has a much more vague female presence with respect to a team composed by Anna, Barbara and Sam. We compute the average department size and average career age of clearly gender-coded male and female authors within each publishing team.

In the SI file, we extend and compare the findings among solo-authored papers with a sample of multi-authored papers – 4085543 unique multi-authored papers from 2000 onwards – but the interpretation of these findings is limited by strong assumptions of a bi-univocal relation between the share of women as authors and women’s contribution to novelty, without accounting for authorship order. We find 246 observations with more than a 1000 authors – this is a negligible quantity to influence the regression estimates. Table 2 in the SI file reports the summary sample statistics for the multi-authored sample of papers.

- 4.5 Regression Models To estimate gender differences in surprising and prescient science, we use cross-sections of papers observed over time and linearly regress innovation scores on the author’s gender for solo-authored papers:


NoveltyScorei =α+βFemalei+∑

δjxi,j +γyear(i) +εi (5)

j

where NoveltyScorei denotes one of four combination-based innovation scores for paper i: reference (concept) surprise and reference (concept) prescience. Femalei is a binary indicator for the gender of the author of paper i.

The vector xi,j represents paper- and author-level controls: year of publication, author’s department size (i.e., number of publications from the institution in the same field as the focal paper), research area (concepts at fine-grained level 1, capturing scientific fields within disciplines, such as economic policy or biochemistry), and career age. Year effects capture temporal shifts in creativity and gender participation; department size captures variations in institutional environment, resources, and prestige, accounting for differences across institutions without requiring numerous institution-level controls that would reduce degrees of freedom. Research field controls for disciplinary differences in innovation practices. Career age accounts for compositional differences in experience and career stage, which are correlated with both gender and scholarly recognition21. Unconditional estimates reported in Section D of the SI show that including these covariates does not substantially alter observed gender differences in novelty or prescience. We estimate four separate regressions, one for each innovation measure, treating each solo-authored paper as a distinct observation. Standard errors are clustered at the author level to account for within-author correlation in residuals. To ensure comparability across disciplines, novelty scores are normalized by within-field percentile ranks.

For science that is equally unexpected at the time of publication or equally ’ahead of its time’, women and men-authored papers may receive different returns in terms of credit and recognition within scientific academia. To investigate gender differences in the scholarly returns to surprising and prescient science, we estimate the following model on cross-sections of papers observed over time:

ScholarlyRewardi =α+βFemalei+γyear(i)+λNoveltyScorei+τ(Femalei×NoveltyScorei)+∑

δjxi,j +εi (6)

j

where ScholarlyRewardi represents one of our measures of credit and recognition for paper i: two-step credit, journal placement (natural logarithm of two-year Journal Impact Factor), or five-year disruption score. NoveltyScorei indicates one of the four combination-based innovation measures of paper i: context surprise, context prescience, content surprise, and content prescience. The interaction term between gender and novelty captures differences in the returns to surprising or prescient science.

Across all models, we include a common set of controls—year of publication, department size, career age, open-access status, and scientific field—to ensure that observed gender differences in scholarly rewards are not driven by differences in institutional context, disciplinary composition, or career stage. For the disruption model, we additionally include two-year citations and the journal’s two-year impact factor, to account for variation in journal placement and early citations that could influence both uptake and disruptiveness. We consider the log-transformation of two-year journal impact to approximate normality. Because prescience reflects changes in surprise occurring after publication — and therefore after journal placement is determined — we do not analyze gender gaps in the relationship between prescience and journal placement, and focus solely on surprise at the time of publication. Standard errors are clustered at the author level.

- 5 Supporting Information


- A Genderize inference results on first and middle names


###### b

###### a

0.40

0.35

0.35

0.30

0.30

0.25

First Name counts - Male First Name counts - Female Probability

0.25

0.20

0.20

0.15

0.15

0.10

0.10

0.05

0.05

0.00

0.00

0.0 0.2 0.4 0.6 0.8 1.0 1.2 106 0.0 0.1 0.2 0.3 0.4 0.5 0.6 106

Figure S7. Sample distribution of counts of first names for (a) Male and (b) Female assigned genders.

###### a

###### b

1.0

0.8

0.8

0.6

0.6

Probability

0.4

0.4

0.2

0.2

0.0

0.0

0.90 0.92 0.94 0.96 0.98 1.00

0.90 0.92 0.94 0.96 0.98 1.00

First Name probabilities - Female

First Name probabilities - Male

Figure S8. Sample distribution of probabilities for first names, for (a) Male and (b) Female assigned genders.

###### a b

0.40

0.6

0.35

0.5

0.30

###### Probability

0.4

0.25

0.20

0.3

0.15

0.2

0.10

0.1

0.05

0.0

6 0.00

0.0 0.2 0.4 0.6 0.8 1.0 1.2 10 0.0 0.1 0.2 0.3 0.4 0.5 0.6 106

Middle Name counts - Male Middle Name counts - Female

Figure S9. Sample distribution of counts of middle names for (a) Male and (b) Female assigned genders.

###### a

###### b

0.8

0.8

0.6

0.6

Probability

0.4

0.4

0.2

0.2

0.0

0.0

0.90 0.92 0.94 0.96 0.98 1.00

0.90 0.92 0.94 0.96 0.98 1.00

Middle Name probabilities - Female

Middle Name probabilities - Male

Figure S10. Sample distribution of probabilities for middle names, for (a) male and (b) female assigned genders.

###### B Descriptive statistics

###### B.1 Paper level statistics

Context Surprise (References)

Content Surprise (Concepts)

Context Prescience (References)

Content Prescience (Concepts)

Context Prescience

Content Prescience

Context Surprise

Content Surprise

(References)

(References)

(Concepts)

(Concepts)

Figure S11. Correlation Plot of sample surprise and prescience in references and concepts.

Table S1. Summary statistics of variables in our sample of solo-authored papers (226208 publications).

Mean Standard Deviation 25th perc. 50th perc. 75th perc. Min value Max value

Surprise (References) .5878723 .3068257 .321875 .636409 .8734216 0 1 Prescience (References) .5501471 .3054902 .2816802 .5752494 .8305932 7.27e-06 1 Surprise (concepts) .5345609 .288986 .284888 .5426767 .7905379 .0000121 1 Prescience (concepts) .5501005 .28599 .3087056 .5652289 .8025451 .0000314 1 Female .2721257 .4450552 0 0 1 0 1

- two-year Journal Impact Factor 4.190875 4.214197 2.084337 3.038461 4.621324 0 132.6792 ln(two-year Journal Impact Factor) 1.189344 .6338853 .7375989 1.113365 1.531683 0 4.887935

- five-year Journal Impact Factor 4.552189 4.447293 2.287671 3.355212 5 1 134.672 ln(five-year Journal Impact Factor) 1.273767 .631945 .8275344 1.210515 1.609438 0 4.902842 Two-Step Credit Score .0369705 .0480954 .0132538 .0232558 .0419287 .0003139 .9090909 Three-Years Disruption Score -.0009666 .0386683 -.0045317 -.0006285 0 -1 1 five-year Disruption Score -.0004151 .0372708 -.0043263 -.0006929 .0001977 -1 1 Publication Year 2009.975 6.028572 2005 2010 2015 2000 2021 two-year citations 7.029358 17.41921 1 3 7 0 1523 Department Size 1512.716 2746.692 140 586 1687 1 40865 Career Age 23.73893 15.14362 11 22 35 0 60 Open Access .334913 .4719611 0 0 1 0 1 Career Cohort 4.318967 1.979498 3 5 6 1 7 Past citations 2149.849 5860.528 38 367 1827 0 178215 WomenShare (Surprise References) .3081784 .0963309 .2341253 .3006158 .3766001 .0761015 .6301304 WomenShare (Prescience References) .3111562 .0995479 .2328184 .3075731 .3835366 .0761015 .6301304 WomenShare (Surprise concepts) .362081 .1065606 .2815366 .3617006 .4400461 .0714286 .6301304 WomenShare (Prescience concepts) .3566239 .1079178 .2783941 .3567669 .4350593 .0761015 .6301304

- Table S2. Summary statistics of all (gender-homogeneous and mixed) multi-authored papers (4085543 publications).


Mean Standard Deviation 25th perc. 50th perc. 75th perc. Min value Max value

Surprise (References) .6412111 .2666128 .4491986 .6975946 .8695936 0 1 Prescience (References) .5821974 .2787709 .3576885 .6131484 .827352 0 1 Surprise (concepts) .5673799 .2859917 .3346121 .5972016 .8191983 0 1 Prescience (concepts) .6020616 .2761986 .3832973 .6380665 .8456904 0 1 Female Share .2981608 .3441279 0 .2 .5 0 1

two-year Journal Impact Factor 5.097368 4.224422 2.927757 4.120163 5.832447 0 467.3684 ln(two-year Journal Impact Factor) 1.447362 .5671963 1.075355 1.416447 1.763747 0 6.147118

- five-year Journal Impact Factor 5.459966 4.297991 3.177496 4.456612 6.209934 1 265.071 ln(five-year Journal Impact Factor) 1.518399 .5645669 1.156093 1.494389 1.82615 0 5.579998 Two-Step Credit Score .0368914 .0400584 .0156028 .0255755 .0434132 .0001316 .9 Three-Years Disruption Score -.0048742 .0251893 -.0067568 -.0017637 -.0000682 -1 1 five-year Disruption Score -.0045224 .0242881 -.006507 -.0017301 -.0001398 -1 1 Publication Year 2012.145 6.08752 2007 2013 2017 2000 2021 two-year Citations 11.66267 40.0359 2 6 13 0 40291 Department Size 3505.908 5086.406 696 1750 4033 1 49445 Career Age 22.22036 11.59788 14 21.33333 29 0 60 Open Access .5414223 .4982813 0 1 1 0 1 Team Size 6.140079 20.43644 3 5 7 2 3222 Num Gender Unknown 3.108408 20.11316 1 2 4 0 3221




| |Share Women Share Men| | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |


0.0 0.2 0.4 0.6 0.8 1.00

Solo - Authored

| | | | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |


0.0 0.2 0.4 0.6 0.8 1.00

Multi - Authored

- Figure S12. Sample share of papers authored by women (orange) and men (blue) in (a) solo-authored, and (b) multi-authored papers by discipline (level-zero fields). The share is computed as the number of papers in discipline j by women (men) divided by the total number of papers in discipline j. Disciplines are ordered by sample share of solo- (multi-) authored papers in each field (in parenthesis). Multi and solo-authored papers display similar gap in the distribution of male and female authors – with women publishing less papers than men across all disciplines.


###### B.2 Author level statistics

- Table S3. Summary statistics of solo-authors (141786 unique authors), multi-authors (1878225 unique authors), all authors (1909424 unique authors), and authors of both solo and multi-authored papers (110587 unique authors). Women represent 44% of al authors in our data collections on solo and multi-authored papers (All Authors). In solo-authored papers, men are more prominent authors, publishing roughly 2 solo-papers each (mean 1.99, sd 2.54, min 1, max 206), where women solo-authors have on average 1.5 solo-papers (mean 1.52, sd 1.387, min 1, max 67); 71% (=31988/44976) of solo-women publish both as solo-author and in multi-authored papers, while 81% (=78599/96810) of solo-men publish as both. Women in our solo-authored sample are publishing less papers than men – both alone and in research teams. Solo-authors are much more productive authors in number of multi-authored papers published with respect to the baseline of people who usually publish the same kind of paper. The sample features 73% (=32833/44976) of women with just one solo-authored paper, and 62% (60023/96810) of men with just one solo-authored work.


Mean Standard Deviation 25th perc. 50th perc. 75th perc. Min value Max value Solo-authors

Publications as multi-author count 28.84956 45.46335 4 12 35 1 925 Women’s share as authors .3172104 .4653918 0 0 1 0 1 Female solo-authors Publications count (total authors: 44976) 1.52 1.38 1 1 2 1 67 Male solo-authors Publications count (total authors: 96810) 1.99 2.55 1 1 2 1 206

Multi-authors

Publications as multi-author count 6.720795 17.08841 1 2 5 1 925 Publications as solo-author count 2.005308 2.488205 1 1 2 1 206 Women’s share as authors .4445192 .4969125 0 0 1 0 1 Female multi-authors Publications count (total authors: 834907) 4.982 11.84 1 2 4 1 740 Male multi-authors Publications count (total authors: 1043318) 8.112 20.228 1 2 6 1 925

All authors

Number of multi-authored papers 6.720795 17.08841 1 2 5 1 925 Average share of women in teams .3771454 .2912426 .1333333 .3333333 .5740741 0 1 Women’s share as authors .444058 .4968608 0 0 1 0 1 Female multi-authored Publications count (total authors: 834907) 4.98 11.83 1 2 4 1 740 Female solo-authored Publications count (total authors: 44976) 1.518 1.387 1 1 2 1 67 Male multi-authored Publications count (total authors: 1043318) 8.112 20.228 1 2 6 1 925 Male solo-authored Publications count (total authors: 96810) 1.9953 2.5482 1 1 2 1 206

Sample of authors in both solo and multi-authored papers

Number of Publications as multi-author 28.84956 45.46335 4 12 35 1 925 Number of Publications as solo-author 2.005308 2.488205 1 1 2 1 206 Women’s share as authors .2892564 .4534192 0 0 1 0 1 Number of multi-authored Publications for women (total authors: 31988) 21.504 34.805 3 8 26 1 680 Number of solo-authored Publications for women (total counts: 31988) 1.648 1.5728 1 1 2 1 67 Number of multi-authored Publications for men (total authors: 78599) 31.838 48.828 4 14 39 1 925 Number of solo-authored Publications for men (total authors: 78599) 2.150 2.7624 1 1 2 1 206 Number of Multi-authored Publications by women with one solo-authored paper (total authors: 21948) 17.063 28.0429 2 7 20 1 1578 Number of Multi-authored Publications by men with one solo-authored paper (total authors: 46001) 24.247 37.587 3 11 30 1 745

###### a b

Distribution of Department Size by Gender Distribution of Career Age by Gender

0.6

0.25

0.5

women

0.20

0.4

Probability

0.15

0.3

men

0.10

0.2

0.05

0.1

0.00

0.0

0 10000 20000 30000 40000 50000 0 10 20 30 40 50 60

Department Size Career Age

- Figure S13. Sample distribution of (a) average author’s department size, and (b) average author’s career age, of unique US authors in multi-authored papers.


###### a b

Distribution of Department Size by Gender Distribution of Career Age by Gender

0.7

0.08

0.6

0.5

men

0.06

Probability

0.4

0.04

0.3

women

0.2

0.02

0.1

0.00

0.0

0 5000 10000 15000 20000 25000 30000 350000 40000 0 10 20 30 40 50 60

Department Size Career Age

###### Figure S14. Sample distribution of (a) average author’s department size, and (b) average author’s career age of unique USauthors in solo-authored papers.

- a
- b


| |Share Women Share Men| | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |


0.0 0.2 0.4 0.6 0.8 1.00

Solo - Authored

| | | | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |


0.0 0.2 0.4 0.6 0.8 1.00

Multi - Authored

- Figure S15. Sample share of authors in disciplines by gender in (a) solo-authored and (b) multi-authored papers. We consider unique authors in our sample. The numerator is number of unique women (men) authors in a given discipline, the denominator is the total number of unique authors in a given discipline. Next to disciplines, we report the sample share of authors in each discipline.


###### a b

Covariate Balance (Women authors) Covariate Balance (Men authors)

| | | | |
|---|---|---|---|


| | | | |
|---|---|---|---|


Avg Dept Size Chemistry Materials science Medicine

Avg Dept Size

Biology Chemistry

Medicine Materials science Geology Environmental science

Biology Engineering

Environmental science Geology

Physics Engineering Geography

Physics Geography

Art Computer science

Mathematics Business History

Business Psychology History Mathematics Economics

Art Economics

Computer science Psychology Philosophy

Sociology Philosophy

Avg. Career Age (years)

Political science Avg. Career Age (years)

Sociology Political science

-0.4 -0.2 0.0 0.2 0.4

-0.30 -0.15 0.00 0.15 0.30

Standardized Mean Difference

Standardized Mean Difference

- Figure S16. Standardized covariate mean differences between authors of solo-papers and multi-authored papers, considering (a) women US authors and (b) men US authors, alongside a 0.1 threshold. Discipline variables indicate the average share of publications of across disciplines – for an author j, the numerator is the number of papers published in a given discipline by author j, the denominator is the total number number of publications by author j. A positive standardized mean difference indicates a higher sample average among multi-authored papers.


###### C Solo-authored papers: Main Models Regression Tables

In this section, we report the tables with the linear regression estimates of equation (1) of the main text, as well as those examining the relationship of surprise and prescience with scholarly rewards by gender in solo-authored papers – corresponding to the model in equation (2) of the main text. The tables are discussed in the main text.

- Table S4. Linear regression estimates of eq. (1) (main text) for content and context surprise and prescience scores in solo-authored papers by gender, with author-level clustered standard errors. Research field fixed effects and dummies for publishing year are omitted.


(1) (2) (3) (4) Surprise (References) Prescience (References) Surprise (concepts) Prescience (concepts) Female=1 0.0258∗∗∗ 0.0241∗∗∗ −0.00525∗∗ −0.00773∗∗∗

(13.13) (12.66) (−3.24) (−4.65)

DepSize −0.00000158∗∗∗ −0.000000757∗ 0.000000221 0.00000212∗∗∗

(−4.55) (−2.28) (0.80) (7.21)

CareerAge −0.00131∗∗∗ −0.00128∗∗∗ −0.000166∗∗∗ −0.000349∗∗∗

(−22.44) (−22.66) (−3.47) (−7.06)

Constant 0.547∗∗∗ 0.556∗∗∗ 0.487∗∗∗ 0.547∗∗∗

(140.10) (142.04) (128.83) (148.65) Observations 226208 226208 226208 226208

t statistics in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

- Table S5. Linear regression estimates of eq. (2) (main text) for two-step credit score, five-year disruption scores, and two-year journal impact factor on surprise score by gender in solo-authored papers. We compute author-level clustered standard errors. We control for career age, average number of citations from institution of author in year of publication and in same field of paper, publication year with 2020 as baseline year (omitted), open access, and dummy variables for level-one fields (omitted). For disruption, we include additional controls given by the two-year journal impact factor, two-year citations.


(1) (2) (3) (4) (5) (6)

TwoStepsCreditScore TwoStepsCreditScore 5-year Disruption 5-year Disruption ln(2-year Journal Impact Factor) ln(2-year Journal Impact Factor) Female=1 −0.00151 −0.00146∗ 0.00618∗∗∗ 0.00179∗∗∗ −0.0665∗∗∗ −0.0656∗∗∗

(−1.28) (−2.23) (8.35) (4.47) (−7.26) (−10.15) Surprise (References) −0.0121∗∗∗ −0.0127∗∗∗ 0.00415

(−16.85) (−25.62) (0.70)

Female=1 × Surprise (References) 0.00102 −0.00778∗∗∗ 0.0410∗∗∗

(0.72) (−8.41) (3.42)

DepSize −0.00000137∗∗∗ −0.00000137∗∗∗ −4.85e−08∗ −2.89e−08 0.0000261∗∗∗ 0.0000261∗∗∗

(−18.88) (−18.99) (−2.06) (−1.22) (33.48) (33.53)

CareerAge −0.000127∗∗∗ −0.000115∗∗∗ 0.0000345∗∗∗ 0.0000534∗∗∗ 0.00226∗∗∗ 0.00225∗∗∗

- (−9.76) (−8.85) (5.61) (8.56) (21.37) (21.25)

OpenAccess −0.00328∗∗∗ −0.00330∗∗∗ −0.000553∗∗ −0.000415∗ 0.147∗∗∗ 0.146∗∗∗

- (−10.08) (−10.10) (−3.17) (−2.37) (45.14) (45.08)


Surprise (Concepts) −0.00180∗∗ 0.0000814 −0.0298∗∗∗

###### (−3.27) (0.25) (−5.59)

Female=1 × Surprise (Concepts) 0.000602 −0.00141∗ 0.0461∗∗∗

(0.59) (−2.25) (4.76) impact_factor_2y −0.000167∗∗∗ −0.0000618∗

###### (−5.86) (−2.20)

2y_cites −0.0000128 −0.0000585∗∗∗

###### (−0.86) (−4.00)

Constant 0.0399∗∗∗ 0.0334∗∗∗ 0.00542∗∗∗ −0.00162∗∗ 0.911∗∗∗ 0.928∗∗∗

(46.87) (48.05) (8.03) (−2.68) (108.58) (115.02) Observations 96513 96513 212916 212916 212402 212402

t statistics in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

- Table S6. Linear regression model estimates of eq. (2) (main text) for two-step credit score, five-year disruption scores on prescience score by gender in solo-authored papers. We compute author-level clustered standard errors. We control for career age, average number of citations from institution of author in year of publication and in same field of paper, publication year with 2020 as baseline year (omitted), open access, and dummy variables for level-one fields (omitted). For disruption, we include additional controls given by the two-year journal impact factor, two-year citations.


(1) (2) (3) (4)

TwoStepsCreditScore TwoStepsCreditScore 5-year Disruption 5-year Disruption Female=1 −0.000286 −0.00243∗∗ 0.00568∗∗∗ 0.00142∗∗

(−0.26) (−3.15) (8.31) (3.27) Prescience (References) −0.0114∗∗∗ −0.0120∗∗∗

(−16.94) (−26.05)

Female=1 × Prescience (References) −0.000783 −0.00755∗∗∗

(−0.58) (−8.43)

DepSize −0.00000138∗∗∗ −0.00000135∗∗∗ −3.59e−08 −3.05e−08

(−19.02) (−18.84) (−1.53) (−1.29)

CareerAge −0.000127∗∗∗ −0.000119∗∗∗ 0.0000364∗∗∗ 0.0000539∗∗∗

(−9.82) (−9.18) (5.92) (8.63)

OpenAccess −0.00337∗∗∗ −0.00319∗∗∗ −0.000520∗∗ −0.000422∗

(−10.33) (−9.79) (−2.98) (−2.41)

Prescience (Concepts) −0.0105∗∗∗ 0.00126∗∗∗

(−16.56) (3.51)

Female=1 × Prescience (Concepts) 0.00213 −0.000687

(1.93) (−1.02)

impact_factor_2y −0.000151∗∗∗ −0.0000620∗

(−5.33) (−2.21)

2y_cites −0.0000186 −0.0000600∗∗∗

(−1.27) (−4.09)

Constant 0.0395∗∗∗ 0.0384∗∗∗ 0.00519∗∗∗ −0.00224∗∗∗

(48.02) (51.30) (7.79) (−3.63) Observations 96513 96513 212916 212916

t statistics in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

###### D Unconditional model estimates

We estimate the unconditional model (1) and model (2) from the main text. To account for sample variation, we restrict the estimation to the subsample of solo-authored papers that would be used once controls are included – that is, we consider only observations without missing values on any control variables. This ensures that unconditional gender differences and conditional gender s are estimated on the same sample, making them directly comparable. We find that unconditional estimates of gender differences are in line with the results of the conditional models, indicating that our set of control variables do not absorb gender differences. Differences in significance of estimates between the conditional and unconditional models may reflect just noise, or variance inflation from adding controls. Previous works suggest caution in interpreting aggregate results, as they compare apples to oranges and may prove misleading52.

- Table S7. Linear regression estimates of eq. (1) (main text) for content and context surprise and prescience scores in solo-authored papers by gender, with author-level clustered standard errors.

(1) (2) (3) (4) Surprise (References) Prescience (References) Surprise (concepts) Prescience (concepts) Female=1 0.0416∗∗∗ 0.0368∗∗∗ −0.00813∗∗∗ −0.0176∗∗∗

(20.67) (19.29) (−5.28) (−10.31)

Constant 0.577∗∗∗ 0.540∗∗∗ 0.537∗∗∗ 0.555∗∗∗

(478.56) (483.11) (613.70) (565.93) Observations 226208 226208 226208 226208

t statistics in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

- Table S8. Linear regression estimates of eq. (2) (main text) for log fo two-step credit score, five-year disruption scores, and two-year journal impact factor on surprise score by gender in solo-authored papers. We compute author-level clustered standard errors.


(1) (2) ln(2-year Journal Impact Factor) ln(2-year Journal Impact Factor) Female=1 −0.120∗∗∗ −0.140∗∗∗

(−10.03) (−18.14) Surprise (References) 0.0327∗∗∗

(4.76)

Female=1 × Surprise (References) 0.0237

(1.51)

Surprise (Concepts) −0.0220∗∗∗

###### (−3.55)

Female=1 × Surprise (Concepts) 0.0670∗∗∗

(5.85)

Constant 1.199∗∗∗ 1.230∗∗∗

(237.48) (291.69) Observations 212402 212402

t statistics in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

- Table S9. Linear regression estimates of eq. (2) (main text) for two-step credit score on surprise score by gender in solo-authored papers. We compute author-level clustered standard errors.


(1) (2) (3) (4) TwoStepsCreditScore TwoStepsCreditScore TwoStepsCreditScore TwoStepsCreditScore Female=1 −0.00370∗∗ −0.00110 −0.00140 −0.00439∗∗∗

(−2.72) (−0.84) (−1.83) (−4.86) Surprise (References) −0.0229∗∗∗

(−26.65)

Female=1 × Surprise (References) 0.00384∗

(2.37)

Prescience (References) −0.0225∗∗∗

(−27.09)

Female=1 × Prescience (References) 0.000230

(0.14)

Surprise (Concepts) −0.00232∗∗∗

###### (−3.47)

Female=1 × Surprise (Concepts) −0.00116

###### (−0.96)

Prescience (Concepts) −0.0219∗∗∗

(−29.18)

Female=1 × Prescience (Concepts) 0.00362∗∗

(2.80)

Constant 0.0529∗∗∗ 0.0518∗∗∗ 0.0388∗∗∗ 0.0502∗∗∗

(74.16) (77.02) (88.07) (91.27) Observations 96513 96513 96513 96513

t statistics in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

- Table S10. Linear regression model estimates of eq. (2) (main text) five-year disruption scores on prescience score by gender in solo-authored papers. We compute author-level clustered standard errors.


(1) (2) (3) (4) 5-year Disruption 5-year Disruption 5-year Disruption 5-year Disruption

Female=1 0.00890∗∗∗ 0.00833∗∗∗ 0.00364∗∗∗ 0.00414∗∗∗

(11.75) (11.89) (9.12) (9.65) Surprise (References) −0.0120∗∗∗

(−26.14)

Female=1 × Surprise (References) −0.00883∗∗∗

(−9.28)

Prescience (References) −0.0112∗∗∗

(−26.35)

Female=1 × Prescience (References) −0.00861∗∗∗

(−9.34)

Surprise (Concepts) −0.000420

- (−1.27)

Female=1 × Surprise (Concepts) −0.00127∗

- (−2.00)


Prescience (Concepts) 0.000222

(0.64)

Female=1 × Prescience (Concepts) −0.00217∗∗

(−3.19)

Constant 0.00554∗∗∗ 0.00466∗∗∗ −0.00119∗∗∗ −0.00154∗∗∗

(15.43) (14.47) (−5.85) (−6.75) Observations 212916 212916 212916 212916

t statistics in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

###### E Assessing the role of individual controls

To explore how individual covariates relate to observed gender differences, we estimate regression models (1) and (2) from the main text by including one control at a time.

###### E.1 Gender differences in approach to novelty and uptake

Overall, the results are consistent with the fully specified models (Table S4).

- Table S11. Linear regression estimates of gender differences in content and context surprise and prescience scores in solo-authored papers, with author-level clustered standard errors, conditioning on controls separately.


(1) (2) (3) (4) Surprise (References) Prescience (References) Surprise (Concepts) Prescience (Concepts)

Department Size Female=1 0.0415∗∗∗ 0.0368∗∗∗ −0.00812∗∗∗ −0.0176∗∗∗

(20.69) (19.29) (−5.28) (−10.36)

DepSize −0.00000388∗∗∗ −0.00000470∗∗∗ 8.20e−08 0.00000763∗∗∗

(−10.38) (−14.40) (0.34) (26.06)

Constant 0.582∗∗∗ 0.547∗∗∗ 0.537∗∗∗ 0.543∗∗∗

(482.85) (470.27) (566.32) (522.47) Career Age

Female=1 0.0319∗∗∗ 0.0265∗∗∗ −0.00984∗∗∗ −0.0165∗∗∗

(15.94) (13.72) (−6.27) (−9.43)

CareerAge −0.00143∗∗∗ −0.00153∗∗∗ −0.000254∗∗∗ 0.000174∗∗∗

(−21.96) (−25.31) (−5.35) (3.30)

Constant 0.613∗∗∗ 0.579∗∗∗ 0.543∗∗∗ 0.550∗∗∗

(356.46) (342.62) (377.11) (345.65) Research Field Dummies (omitted)

Female=1 0.0305∗∗∗ 0.0261∗∗∗ −0.00492∗∗ −0.00784∗∗∗

(15.54) (13.73) (−3.11) (−4.82)

Constant 0.490∗∗∗ 0.461∗∗∗ 0.468∗∗∗ 0.505∗∗∗

(213.37) (204.34) (219.92) (237.55) Publication Year (omitted)

Female=1 0.0469∗∗∗ 0.0457∗∗∗ −0.00701∗∗∗ −0.0138∗∗∗

(23.31) (24.11) (−4.55) (−8.06)

Constant 0.605∗∗∗ 0.603∗∗∗ 0.553∗∗∗ 0.593∗∗∗

(184.09) (184.52) (175.13) (190.97) Observations 226208 226208 226208 226208

t statistics in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

###### E.2 Gender differences in returns to innovation

We include covariates one at a time to show how estimates of gender differences in returns to novelty and uptake change when conditioning on key dimensions individually. Estimates remain broadly consistent with the full models for disruption (Table S13) and journal impact (Table S12).

When estimating the effect of novelty on two-step credit scores, the average gender difference shifts from negative to positive once only field dummies are included as covariates, except for equally concept prescience (Table S14). This suggests that women’s field choices partially account for gender differences in citation outcomes. This result complements existing literature52,53. Controlling for research fields is particularly important when examining the relationship between novelty and scholarly rewards, as innovation and citation patterns vary substantially across disciplines. At the same time, women may self-select into less recognized fields, affecting citation outcomes.

Nevertheless, research fields do not appear to strongly mediate gender differences in the returns to novelty: the sign and magnitude of estimated gender gap in the marginal effect of novelty on citations remains consistent with the fully specified model. Notably, field dummies absorb much of the gender differences in how reference surprise gets rewarded in downstream citations. The conditional specification of the models still more appropriate, as it shows whether novelty translates differently in rewards by gender for similar people across relevant dimensions – e.g. at the same career stage, within similar institution in size, in the same field and year of publication.

- Table S12. Linear regression estimates of two-year journal impact factor on content and context surprise scores by gender in solo-authored papers, conditioning on controls separately, with clustered standard errors at the author level. The table continues in the next page.


(1) (2) ln(2-year Journal Impact Factor) ln(2-year Journal Impact Factor)

Department Size Female=1 −0.118∗∗∗ −0.134∗∗∗

(−9.89) (−17.98) Surprise (References) 0.0534∗∗∗

(8.04)

Female=1 × Surprise (References) 0.0203

(1.29)

Surprise (Concepts) −0.0203∗∗∗

###### (−3.35)

Female=1 × Surprise (Concepts) 0.0592∗∗∗

(5.32)

DepSize 0.0000522∗∗∗ 0.0000520∗∗∗

(55.91) (55.73)

Constant 1.106∗∗∗ 1.148∗∗∗

(221.61) (274.04) Career Age

Female=1 −0.0705∗∗∗ −0.0960∗∗∗

(−5.93) (−12.55) Surprise (References) 0.0590∗∗∗

(8.67)

Female=1 × Surprise (References) 0.0111

(0.72)

Surprise (Concepts) −0.0172∗∗

###### (−2.79)

Female=1 × Surprise (Concepts) 0.0640∗∗∗

(5.67)

CareerAge 0.00627∗∗∗ 0.00617∗∗∗

(48.56) (47.81)

Constant 1.022∗∗∗ 1.068∗∗∗

(174.12) (212.14) Research Field Dummies (omitted)

Female=1 −0.0770∗∗∗ −0.0737∗∗∗

(−8.00) (−10.94) Surprise (References) −0.0467∗∗∗

###### (−7.64)

Female=1 × Surprise (References) 0.0491∗∗∗

(3.88)

Surprise (Concepts) −0.0409∗∗∗

###### (−7.42)

Female=1 × Surprise (Concepts) 0.0479∗∗∗

(4.74)

Constant 1.243∗∗∗ 1.239∗∗∗

(209.24) (227.11) Observations 212402 212402

t statistics in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

Table S12 continued.

(1) (2) ln(2-year Journal Impact Factor) ln(2-year Journal Impact Factor)

Publication Year (omitted) Female=1 −0.135∗∗∗ −0.154∗∗∗

(−11.36) (−20.08) Surprise (References) 0.0585∗∗∗

(8.66)

Female=1 × Surprise (References) 0.0247

(1.59)

Surprise (Concepts) −0.0170∗∗

###### (−2.76)

Female=1 × Surprise (Concepts) 0.0694∗∗∗

(6.13) (6.13)

Constant 1.001∗∗∗ 1.046∗∗∗

(121.56) (132.57) Open Access

Female=1 −0.106∗∗∗ −0.121∗∗∗

(−9.58) (−16.49) Surprise (References) 0.0455∗∗∗

(6.81)

Female=1 × Surprise (References) 0.0260

(1.79)

OpenAccess 0.297∗∗∗ 0.296∗∗∗

(83.21) (82.84)

Surprise (Concepts) −0.0216∗∗∗

###### (−3.59)

Female=1 × Surprise (Concepts) 0.0616∗∗∗

(5.58)

OpenAccess 0.297∗∗∗ 0.296∗∗∗

(83.21) (82.84)

Constant 1.086∗∗∗ 1.124∗∗∗

(218.27) (270.56) Observations 212402 212402

t statistics in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

- Table S13. Linear regression estimates of five-year disruption on content and context surprise and prescience scores by gender in solo-authored papers, conditioning on controls separately. We compute author-level clustered standard errors. The table continues in the next page.


(1) (2) (3) (4) 5-year Disruption 5-year Disruption 5-year Disruption 5-year Disruption

Department Size Female=1 0.00894∗∗∗ 0.00836∗∗∗ 0.00380∗∗∗ 0.00431∗∗∗

(11.81) (11.93) (9.47) (10.01) Surprise (References) −0.0121∗∗∗

(−26.27)

- Female=1 × Surprise (References) −0.00882∗∗∗ (−9.28)

DepSize −0.000000292∗∗∗ −0.000000295∗∗∗ −0.000000241∗∗∗ −0.000000238∗∗∗

(−13.11) (−13.18) (−11.08) (−10.99)

CareerAge 0.00000631 0.00000737 0.0000258∗∗∗ 0.0000263∗∗∗

(1.03) (1.19) (4.14) (4.22) Prescience (References) −0.0113∗∗∗

(−26.41)

Female=1 × Prescience (References) −0.00858∗∗∗

(−9.31)

Surprise (Concepts) −0.000408

(−1.23)

Female=1 × Surprise (Concepts) −0.00125∗

(−1.96)

Prescience (Concepts) 0.000380

(1.09)

Female=1 × Prescience (Concepts) −0.00216∗∗

(−3.17)

Constant 0.00589∗∗∗ 0.00499∗∗∗ −0.00149∗∗∗ −0.00193∗∗∗

(14.69) (13.44) (−5.71) (−7.03) Observations 212916 212916 212916 212916

Career Age Female=1 0.00890∗∗∗ 0.00834∗∗∗ 0.00379∗∗∗ 0.00430∗∗∗

(11.75) (11.90) (9.43) (10.00)

CareerAge −0.000000307 0.000000726 0.0000202∗∗ 0.0000208∗∗∗

(−0.05) (0.12) (3.28) (3.37) Surprise (References) −0.0120∗∗∗

(−26.16)

- Female=1 × Surprise (References) −0.00883∗∗∗ (−9.28)


Prescience (References) −0.0112∗∗∗

(−26.33)

Female=1 × Prescience (References) −0.00861∗∗∗

###### (−9.34)

Surprise (Concepts) −0.000404

###### (−1.22)

Female=1 × Surprise (Concepts) −0.00128∗

###### (−2.02)

Prescience (Concepts) 0.000219

(0.63)

Female=1 × Prescience (Concepts) −0.00221∗∗

###### (−3.24)

Constant 0.00555∗∗∗ 0.00464∗∗∗ −0.00172∗∗∗ −0.00207∗∗∗

(14.14) (12.82) (−6.66) (−7.57) Research Field Dummies (omitted)

Female=1 0.00595∗∗∗ 0.00541∗∗∗ 0.00153∗∗∗ 0.00110∗

(8.04) (7.91) (3.84) (2.55) Surprise (References) −0.0127∗∗∗

(−28.39)

Female=1 × Surprise (References) −0.00772∗∗∗

###### (−8.31)

Prescience (References) −0.0118∗∗∗

(−28.72)

Female=1 × Prescience (References) −0.00749∗∗∗

###### (−8.34)

Surprise (Concepts) −0.0000976

###### (−0.30)

Female=1 × Surprise (Concepts) −0.00139∗

###### (−2.23)

Prescience (Concepts) 0.000822∗

(2.34)

Female=1 × Prescience (Concepts) −0.000565

###### (−0.84)

Constant 0.00509∗∗∗ 0.00434∗∗∗ −0.000940∗∗ −0.00138∗∗∗

(11.86) (10.68) (−2.86) (−3.96) Observations 212916 212916 212916 212916

t statistics in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

(1) (2) (3) (4) 5-year Disruption 5-year Disruption 5-year Disruption 5-year Disruption

Publication Year (omitted) Female=1 0.00884∗∗∗ 0.00832∗∗∗ 0.00351∗∗∗ 0.00403∗∗∗

(11.66) (11.86) (8.79) (9.38) Surprise (References) −0.0119∗∗∗

(−25.83)

Female=1 × Surprise (References) −0.00879∗∗∗

###### (−9.25)

Prescience (References) −0.0112∗∗∗

(−25.86)

Female=1 × Prescience (References) −0.00857∗∗∗

###### (−9.30)

Surprise (Concepts) −0.000390

###### (−1.18)

Female=1 × Surprise (Concepts) −0.00124

###### (−1.94)

Prescience (Concepts) 0.000361

(1.03)

Female=1 × Prescience (Concepts) −0.00217∗∗

###### (−3.19)

Constant 0.00489∗∗∗ 0.00452∗∗∗ −0.00217∗∗∗ −0.00259∗∗∗

(8.18) (7.74) (−4.17) (−4.86)

Open Access Female=1 0.00878∗∗∗ 0.00817∗∗∗ 0.00349∗∗∗ 0.00394∗∗∗

(11.60) (11.67) (8.75) (9.19) Surprise (References) −0.0121∗∗∗

(−26.35)

Female=1 × Surprise (References) −0.00885∗∗∗

###### (−9.31)

OpenAccess −0.00263∗∗∗ −0.00276∗∗∗ −0.00236∗∗∗ −0.00234∗∗∗

(−15.41) (−16.04) (−13.80) (−13.76) Prescience (References) −0.0114∗∗∗

(−26.75)

Female=1 × Prescience (References) −0.00856∗∗∗

###### (−9.30)

Surprise (Concepts) −0.000424

###### (−1.29)

Female=1 × Surprise (Concepts) −0.00123

###### (−1.94)

Prescience (Concepts) 0.000361

(1.04)

Female=1 × Prescience (Concepts) −0.00203∗∗

###### (−2.98)

Constant 0.00655∗∗∗ 0.00576∗∗∗ −0.000347 −0.000777∗∗

(17.53) (16.99) (−1.60) (−3.28) Observations 212916 212916 212916 212916

t statistics in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

(1) (2) (3) (4) 5-year Disruption 5-year Disruption 5-year Disruption 5-year Disruption

Two-year journal impact Female=1 0.00881∗∗∗ 0.00820∗∗∗ 0.00349∗∗∗ 0.00401∗∗∗

(11.64) (11.72) (8.74) (9.35) Surprise (References) −0.0121∗∗∗

(−26.30)

Female=1 × Surprise (References) −0.00888∗∗∗

###### (−9.35)

impact_factor_2y −0.000281∗∗∗ −0.000291∗∗∗ −0.000246∗∗∗ −0.000245∗∗∗

(−12.06) (−12.35) (−10.38) (−10.36) Prescience (References) −0.0114∗∗∗

(−26.63)

Female=1 × Prescience (References) −0.00861∗∗∗

###### (−9.36)

Surprise (Concepts) −0.000472

###### (−1.43)

Female=1 × Surprise (Concepts) −0.00121

###### (−1.91)

Prescience (Concepts) 0.000533

(1.54)

Female=1 × Prescience (Concepts) −0.00214∗∗

###### (−3.14)

Constant 0.00682∗∗∗ 0.00602∗∗∗ −0.0000973 −0.000648∗

(17.56) (16.88) (−0.40) (−2.57) Two-year citations

Female=1 0.00891∗∗∗ 0.00832∗∗∗ 0.00357∗∗∗ 0.00411∗∗∗

(11.75) (11.85) (8.93) (9.58) Surprise (References) −0.0116∗∗∗

(−23.43)

Female=1 × Surprise (References) −0.00894∗∗∗

###### (−9.42)

2y_cites −0.0000360∗∗ −0.0000427∗∗ −0.0000756∗∗∗ −0.0000765∗∗∗

(−2.66) (−3.17) (−5.48) (−5.49) Prescience (References) −0.0108∗∗∗

(−23.83)

Female=1 × Prescience (References) −0.00871∗∗∗

###### (−9.46)

Surprise (Concepts) −0.000172

###### (−0.52)

Female=1 × Surprise (Concepts) −0.00133∗

###### (−2.08)

Prescience (Concepts) 0.000780∗

(2.17)

Female=1 × Prescience (Concepts) −0.00229∗∗∗

###### (−3.36)

Constant 0.00559∗∗∗ 0.00477∗∗∗ −0.000746∗∗∗ −0.00126∗∗∗

(15.62) (14.85) (−3.44) (−5.42) Observations 212916 212916 212916 212916

t statistics in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

- Table S14. Linear regression estimates of two-step credit score on content and context surprise and prescience scores by gender in solo-authored papers, conditioning on controls separately. We compute author-level clustered standard errors. The table continues in the next page.


(1) (2) (3) (4) TwoStepsCreditScore TwoStepsCreditScore TwoStepsCreditScore TwoStepsCreditScore

Department Size Female=1 −0.00369∗∗ −0.00110 −0.00145 −0.00452∗∗∗

(−2.73) (−0.85) (−1.90) (−5.01) Surprise (References) −0.0225∗∗∗

(−26.39)

Female=1 × Surprise (References) 0.00382∗

(2.37)

DepSize −0.00000124∗∗∗ −0.00000134∗∗∗ −0.00000132∗∗∗ −0.00000113∗∗∗

(−17.28) (−18.32) (−18.07) (−15.96) Prescience (References) −0.0226∗∗∗

(−27.30)

Female=1 × Prescience (References) 0.000257

(0.16)

Surprise (Concepts) −0.00211∗∗

###### (−3.17)

Female=1 × Surprise (Concepts) −0.00104

###### (−0.86)

Prescience (Concepts) −0.0212∗∗∗

(−28.34)

Female=1 × Prescience (Concepts) 0.00390∗∗

(3.02)

Constant 0.0545∗∗∗ 0.0537∗∗∗ 0.0406∗∗∗ 0.0514∗∗∗

(74.71) (77.51) (88.95) (91.82) Career Age

Female=1 −0.00543∗∗∗ −0.00293∗ −0.00283∗∗∗ −0.00596∗∗∗

(−4.03) (−2.26) (−3.68) (−6.59) Surprise (References) −0.0233∗∗∗

(−27.19)

Female=1 × Surprise (References) 0.00433∗∗

(2.69)

CareerAge −0.000219∗∗∗ −0.000231∗∗∗ −0.000207∗∗∗ −0.000204∗∗∗

(−14.30) (−15.12) (−13.35) (−13.27) Prescience (References) −0.0233∗∗∗

(−28.07)

Female=1 × Prescience (References) 0.000800

(0.51)

Surprise (Concepts) −0.00241∗∗∗

###### (−3.62)

Female=1 × Surprise (Concepts) −0.000966

###### (−0.80)

Prescience (Concepts) −0.0219∗∗∗

(−29.33)

Female=1 × Prescience (Concepts) 0.00410∗∗

(3.18)

Constant 0.0588∗∗∗ 0.0582∗∗∗ 0.0442∗∗∗ 0.0555∗∗∗

(73.05) (75.12) (76.06) (82.90) Research Field Dummies (omitted)

Female=1 0.000515 0.00233∗ 0.000669 −0.00111

(0.41) (1.98) (0.95) (−1.32) Surprise (References) −0.0120∗∗∗

(−15.68)

Female=1 × Surprise (References) 0.00102

(0.69)

Prescience (References) −0.0144∗∗∗

(−19.78)

Female=1 × Prescience (References) −0.00153

###### (−1.06)

Surprise (Concepts) −0.00189∗∗

###### (−3.20)

Female=1 × Surprise (Concepts) 0.000312

(0.28)

Prescience (Concepts) −0.0123∗∗∗

(−17.94)

Female=1 × Prescience (Concepts) 0.00325∗∗

(2.73)

Constant 0.0468∗∗∗ 0.0477∗∗∗ 0.0405∗∗∗ 0.0463∗∗∗

(60.10) (64.32) (68.20) (69.59) Observations 96513 96513 96513 96513

t statistics in parentheses

∗ p<0.05,∗∗ p<0.01,∗∗∗ p<0.001 42/87

Table S14 continued.

(1) (2) (3) (4) TwoStepsCreditScore TwoStepsCreditScore TwoStepsCreditScore TwoStepsCreditScore

Publication Year (omitted) Female=1 −0.00483∗∗∗ −0.00272∗ −0.00290∗∗∗ −0.00505∗∗∗

(−3.67) (−2.18) (−4.00) (−5.98) Surprise (References) −0.0230∗∗∗

(−27.77)

Female=1 × Surprise (References) 0.00353∗

(2.26)

Prescience (References) −0.0196∗∗∗

(−24.85)

Female=1 × Prescience (References) 0.000481

(0.32)

Surprise (Concepts) −0.00235∗∗∗

(−3.70)

Female=1 × Surprise (Concepts) −0.000892

(−0.78)

Prescience (Concepts) −0.0208∗∗∗

(−29.25)

Female=1 × Prescience (Concepts) 0.00248∗

(2.03)

Constant 0.0402∗∗∗ 0.0378∗∗∗ 0.0262∗∗∗ 0.0375∗∗∗

(53.82) (52.66) (48.32) (61.55) Open Access

Female=1 −0.00338∗ −0.000809 −0.00112 −0.00394∗∗∗

(−2.49) (−0.62) (−1.47) (−4.37) Surprise (References) −0.0229∗∗∗

(−26.68)

Female=1 × Surprise (References) 0.00371∗

(2.29)

OpenAccess 0.00431∗∗∗ 0.00372∗∗∗ 0.00430∗∗∗ 0.00493∗∗∗

(11.16) (9.68) (11.02) (12.69) Prescience (References) −0.0222∗∗∗

(−26.79)

Female=1 × Prescience (References) 0.0000631

(0.04)

Surprise (Concepts) −0.00242∗∗∗

(−3.64)

Female=1 × Surprise (Concepts) −0.00126

(−1.04)

Prescience (Concepts) −0.0223∗∗∗

(−29.61)

Female=1 × Prescience (Concepts) 0.00327∗

(2.53)

Constant 0.0513∗∗∗ 0.0502∗∗∗ 0.0372∗∗∗ 0.0485∗∗∗

(72.43) (75.04) (83.44) (90.17) Observations 96513 96513 96513 96513

t statistics in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

###### F Heterogeneity of gender difference in novelty and prescience in solo-authored papers

We augment model (1) of the main text by interacting our variable of interest, Female, with regression covariates, such as career age, department size, and other relevant sources of variations, like women’s share in field of publication, disciplines, or past citations of authors.

###### F.1 Women’s share in field of publication

The share of women in a field may influence women’s approaches to novelty, as critical mass affects innovation opportunities and the prevalence of gender discrimination54,72. For each paper, we measure women’s share in a field as the proportion of solo-authored publications by women in the scientific fields where the paper attains its highest surprise or prescience, computed separately for concepts and references. These shares are calculated using solo-authored publications in each field up to the year of the paper’s publication.

We model a paper’s novelty – measured as surprise or prescience in concepts or references —- as a function of the author’s gender, the share of women in the relevant field, and the interaction between the two, while controlling for publication year, career age, department size, and research field. This allows us to examine whether women’s investment in novelty varies with the proportion of women active in the field.

Figure S17 shows predicted surprise and prescience by women’s share in the field. Reference surprise and prescience decline as the share of women increases, with men’s novelty decreasing more sharply – Fig. S17 (a-b). Content surprise rises with women’s presence. Concept prescience also declines with women’s share, but women experience less reduction than men – Fig. S17 (c-d).

Regression estimates (Table S15, which include indicators for female authorship and women’s field share as both main effects and interactions) show that the association between women’s field share and novelty differs by author gender. In particular, the interaction between female authorship and women’s share of solo-authored papers in a field is positive for both surprise and prescience, indicating that gender differences in novelty vary systematically with women’s representation in the field.

At the same time, columns (1) and (2) show that, holding women’s field share and other covariates constant, women’s papers are on average less surprising or prescient in their combinations of references. This baseline gap is attenuated – and eventually reversed – at higher levels of women’s representation among solo authors in the field. This pattern is consistent with the idea that women’s papers tend to become more creative in their use of sources as women’s participation in solo-authored research within a field increases.

###### a b

Context (Reference) Surprise Context (Reference) Prescience

0.8

1.0

0.6

Linear predictionLinear prediction

0.5

Female = 1

0.4

0.0

0.2

Female = 0

0.0

-0.5

###### c d

Content (Concept) Surprise Content (Concept) Prescience

0.65

1.0

0.60

0.8

0.55

0.6

0.50

0.4

0.45

0.4

0.2

0 .1 .2 .3 .4 .5 .6 .7 .8 .9 1 0 .1 .2 .3 .4 .5 .6 .7 .8 .9 1

Share of Women in Field Share of Women in Field

- Figure S17. Predicted values of surprise and prescience of science by share of women in the field, for women and men’s solo authored papers, marginalized over the observed distribution of covariates (year of publication, department size, level-one field of publication, career age).


- Table S15. Linear Regression model estimates of surprise and prescience score by genders and women’s share of the topic of maximal surprise (prescience) of solo-authored papers, with author-level clustered standard errors. Research field fixed effects and dummies for publishing year are omitted.


(1) (2) (3) (4) Surprise (References) Prescience (References) Surprise (concepts) Prescience (concepts) Female=1 -0.0321∗∗∗ -0.0215∗∗∗ -0.0420∗∗∗ -0.0362∗∗∗

(-5.87) (-3.98) (-7.31) (-6.24) WomenShare (Surprise References) -1.026∗∗∗

(-79.87) Female=1 × WomenShare (Surprise References) 0.182∗∗∗ (10.92)

DepSize -0.00000105∗∗ -0.000000367 2.24e-08 0.00000220∗∗∗ (-3.05) (-1.10) (0.08) (7.49)

CareerAge -0.00122∗∗∗ -0.00123∗∗∗ -0.000184∗∗∗ -0.000341∗∗∗

(-21.38) (-22.09) (-3.86) (-6.92) WomenShare (Prescience References) -0.714∗∗∗

(-56.64) Female=1 × WomenShare (Prescience References) 0.141∗∗∗

(8.73)

WomenShare (Surprise Concepts) 0.403∗∗∗ (37.38)

Female=1 × WomenShare (Surprise Concepts) 0.0910∗∗∗ (6.50)

WomenShare (Prescience Concepts) -0.182∗∗∗ (-17.53)

Female=1 × WomenShare (Prescience Concepts) 0.0760∗∗∗ (5.26)

Constant 0.844∗∗∗ 0.765∗∗∗ 0.368∗∗∗ 0.602∗∗∗

(160.26) (144.22) (73.53) (124.02) Observations 226208 226208 226208 226208

t statistics in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

###### F.2 Department size

We examine how the size of the author’s institution – proxied by the number of publications from the institution within the relevant field – interacts with gender of solo-authors, and the joint trend in surprise and prescience. For papers associated with multiple fields, we use the largest department size.

In Figure S18, predicted patterns show that larger departments are generally associated with lower reference-based surprise and prescience. However, women’s solo-authored papers are less affected by these declines: they maintain higher reference surprise and experience increasing reference prescience as department size grows. From Table S16, column (3), content-based surprise and prescience also tend to rise with department size for women. Overall, women appear to benefit relatively more from larger departments in terms of novelty, while men’s novelty scores show weaker or negative effects with department size.

a Context (Reference) Surprise b Context (Reference) Prescience

.45.5.6.65.55

.45.5.6.65.55

Female = 1

Linear prediction

Female = 0

- c Content (Concept) Surprise d Content (Concept) Prescience


.55.6.65.7.5

.52.54.56.58.6.5

Linear prediction

0 10000 20000 30000 40000

0 10000 20000 30000 40000

Department Size Department Size

- Figure S18. Predicted values of surprise and prescience by department size for women and men’s solo authored papers, marginalized over the observed distribution of covariates (year of publication, level-one field of publication, career age).


- Table S16. Linear regression model estimates for content and context surprise and prescience scores, with author-level clustered standard errors. Research field fixed effects and dummies for publishing year are omitted.


(1) (2) (3) (4) Surprise (References) Prescience (References) Surprise (concepts) Prescience (concepts) Female=1 0.0234∗∗∗ 0.0202∗∗∗ -0.00699∗∗∗ -0.00982∗∗∗

(10.61) (9.57) (-3.86) (-5.29) DepSize -0.00000199∗∗∗ -0.00000145∗∗∗ -8.77e-08 0.00000175∗∗∗ (-4.89) (-3.73) (-0.28) (5.07) Female=1 × DepSize 0.00000148∗ 0.00000248∗∗∗ 0.00000111∗ 0.00000132∗ (2.26) (4.01) (2.11) (2.40) CareerAge -0.00131∗∗∗ -0.00128∗∗∗ -0.000166∗∗∗ -0.000350∗∗∗ (-22.45) (-22.68) (-3.48) (-7.07)

Constant 0.547∗∗∗ 0.557∗∗∗ 0.487∗∗∗ 0.548∗∗∗ (139.77) (142.04) (128.69) (148.42)

Observations 226208 226208 226208 226208 Observations 226208 226208 226208 226208

t statistics in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

###### F.3 Career age

We examine how gender differences in novelty vary across career age cohorts for solo-authored papers by interacting gender with career age intervals, ranging from 0–5 up to 40–60 years since first publication.

Predicted patterns show that women’s solo-authored papers maintain higher reference-based surprise and prescience than men’s across most career stages, with peaks at late stages (>40 years). For content-based novelty, men-authored solo-papers are ahead of women’s across all career stages, with the gender gap narrowing as careers progress. Instead, for content-based prescience, women’s works starts below men’s, and the gender gap in prescience widens mid-career (5–20 years) before virtually disappearing in later stages. Regression estimates are reported in Table S17.

- Table S17. Linear regression model estimates for content and context surprise and prescience scores, with author-level clustered standard errors. Research field fixed effects and dummies for publishing year are omitted.


(1) (2) (3) (4) Surprise (References) Prescience (References) Surprise (concepts) Prescience (concepts) Female=1 0.0171∗∗∗ 0.0118∗∗ -0.0112∗∗ -0.00903∗

(4.46) (3.18) (-3.06) (-2.47)

- career_cohort=2 0.0238∗∗∗ 0.0198∗∗∗ -0.00134 0.00723∗ (7.03) (5.99) (-0.41) (2.18)
- career_cohort=3 0.00724∗ 0.00405 -0.00148 0.00917∗∗ (2.04) (1.16) (-0.44) (2.71)
- career_cohort=4 -0.00313 -0.00568 -0.00514 0.00593 (-0.86) (-1.59) (-1.49) (1.73)
- career_cohort=5 -0.0223∗∗∗ -0.0261∗∗∗ -0.00724∗ -0.00259 (-6.83) (-8.16) (-2.38) (-0.84)
- career_cohort=6 -0.0399∗∗∗ -0.0409∗∗∗ -0.00972∗∗ -0.00667∗ (-11.61) (-12.19) (-3.14) (-2.12)
- career_cohort=7 -0.0500∗∗∗ -0.0533∗∗∗ -0.00858∗∗ -0.0142∗∗∗ (-13.55) (-15.21) (-2.69) (-4.29)


- Female=1 × career_cohort=2 -0.00264 -0.000708 0.00750 -0.00715 (-0.51) (-0.14) (1.48) (-1.42)
- Female=1 × career_cohort=3 0.00521 0.00751 0.00324 -0.00563 (0.91) (1.35) (0.61) (-1.07)
- Female=1 × career_cohort=4 0.00154 0.00346 0.00363 -0.00278

- (0.26) (0.59) (0.65) (-0.51)

Female=1 × career_cohort=5 0.00945 0.0148∗∗ 0.00774 0.00435

- (1.80) (2.86) (1.56) (0.88)

Female=1 × career_cohort=6 0.0170∗ 0.0208∗∗∗ 0.00879 0.00488

- (2.52) (3.29) (1.62) (0.90)


- Female=1 × career_cohort=7 0.0338∗∗∗ 0.0446∗∗∗ 0.0102 0.0175∗∗ (4.79) (6.64) (1.74) (2.89)


DepSize -0.00000161∗∗∗ -0.000000791∗ 0.000000215 0.00000209∗∗∗ (-4.63) (-2.38) (0.78) (7.12)

Constant 0.532∗∗∗ 0.545∗∗∗ 0.489∗∗∗ 0.540∗∗∗

(120.87) (124.58) (113.12) (127.73) Observations 226208 226208 226208 226208

t statistics in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

a Context (Reference) Surprise b Context (Reference) Prescience

- .5

.52

.54

.56

.58

- .6


.64

.62

Female = 1

Linear prediction

.6

.58

Female = 0

.56

.54

c Content (Concept) Surprise d Content (Concept) Prescience

- .53

- .54

- .55

- .56

- .57


.545

- .52

.525

- .53

.535

- .54


Linear prediction

[0,5] (5, 10] (10,15] (15, 20] (20,30] (30, 40] (40, 60]

[0,5] (5, 10] (10,15] (15, 20] (20,30] (30, 40] (40, 60]

Career Age Cohort Career Age Cohort

- Figure S19. Predicted reference surprise and prescience (row one) and concept surprise and prescience (row two) by gender across career age cohorts, marginalized over the observed distribution of covariates (year of publication, department size, level-one field of publication).


###### F.4 Past citations

We check whether the differences in novelty production in solo-authored papers by genders derives from reputation of the author, as more prominent scientists could inherently have higher prescience because of their status, or produce more surprising papers. We proxy status within science with past citations of the solo-authors up until the year of publication of the focal paper.

Higher past citations are associated with lower surprise and prescience in reference combinations, as well as lower conceptbased surprise, but with higher prescience in concept combinations—an outcome in which men’s work tends to be more prescient. However, increases in past citations are more strongly associated with uptake of women’s concept combinations than men’s. By contrast, women’s reference-based novelty shows no differential association with prior reputation (Table S18).

a Context (Reference) Surprise b Context (Reference) Prescience

.3.4.5.6.2

Female = 1

.3.4.6.2.5

Female = 0

Linear prediction

Predictive margins of Female with 95% CIs

c Content (Concept) Surprise d Content (Concept) Prescience

.6.811.2.4

.5.6.7.8.4

Linear prediction

0 50000 100000 150000 200000

0 50000 100000 150000 200000

Past Citations

Past Citations

- Figure S20. Predicted values of surprise and prescience by past citations of women and men in solo authored papers, marginalized over the observed distribution of covariates (year of publication, department size, level-one field of publication, career age).


- Table S18. Linear Regression model estimates of surprise and prescience scores by gender and past citations of solo-authored papers, with author-level clustered standard errors. Research field fixed effects and dummies for publishing year are omitted.


(1) (2) (3) (4) Surprise (References) Prescience (References) surprise (concepts) Prescience (concepts) Female=1 0.0254∗∗∗ 0.0222∗∗∗ -0.00644∗∗∗ -0.00866∗∗∗

(12.37) (11.27) (-3.86) (-5.03) PastCitations -0.000000981∗∗∗ -0.00000133∗∗∗ -0.000000310∗ 0.000000733∗∗∗ (-3.79) (-4.25) (-2.33) (4.93) Female=1 × PastCitations -0.000000372 0.000000631 0.000000760 0.00000127∗∗ (-0.65) (1.08) (1.80) (2.63) CareerAge -0.00121∗∗∗ -0.00116∗∗∗ -0.000147∗∗ -0.000440∗∗∗ (-19.34) (-18.91) (-2.98) (-8.53) DepSize -0.00000123∗∗∗ -0.000000335 0.000000291 0.00000181∗∗∗ (-3.49) (-1.01) (1.04) (6.03) Constant 0.546∗∗∗ 0.555∗∗∗ 0.487∗∗∗ 0.548∗∗∗

(139.49) (141.63) (128.61) (148.64) Observations 226208 226208 226208 226208

t statistics in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

###### F.5 Discipline

We examine whether gender differences in solo-authored novelty vary across disciplines (level-zero concepts). We estimate linear regression models including interactions between the gender indicator and dummy variables for each discipline (for a total of 19 disciplines), which allows the gender gap in surprise and prescience to differ across fields.

Table S19 reports the interactions between female authorship and discipline for solo-authored papers. Positive interaction coefficients indicate that the gender difference in novelty is relatively larger in that discipline, whereas negative coefficients indicate a smaller gender difference. For reference-based novelty, interactions are positive in computer science, medicine, and philosophy, and negative in art, business, and political science. For concept-based novelty, interactions are positive in biology and medicine.

Estimates for the full multi-authored sample are consistent with solo-authored papers: increasing women’s share in teams is positively and significantly associated to innovation in computer science, economics, environmental science, geology, materials science, and philosophy. Conversely, women’s participated multi-authored contributions in political science, psychology, and sociology are generally less innovative.

- Table S19. Linear regression model estimates for content and context surprise and prescience scores by discipline (level zero field) in solo-authored papers. We compute author-level clustered standard errors. Research field fixed effects and dummies for publishing year are omitted.


(1) (2) (3) (4) Surprise (References) Prescience (References) Surprise (concepts) Prescience (concepts) Female=1 0.0211∗∗∗ 0.0226∗∗∗ -0.0165∗∗∗ -0.0168∗∗∗

(4.50) (5.02) (-4.01) (-4.07) Art=1 0.0287∗∗ 0.0336∗∗∗ -0.0216∗ 0.0109 (3.12) (3.79) (-2.54) (1.27)

Biology=1 0.0196∗∗∗ -0.000388 -0.0239∗∗∗ -0.0428∗∗∗

(6.86) (-0.14) (-8.99) (-16.78) Business=1 -0.00728 -0.00450 -0.0104∗ -0.00463

(-1.63) (-1.04) (-2.54) (-1.10) Chemistry=1 -0.0166∗∗∗ -0.0260∗∗∗ -0.0170∗∗∗ -0.0513∗∗∗ (-4.68) (-7.27) (-5.20) (-16.23) Computer science=1 0.0448∗∗∗ 0.0122∗∗∗ -0.0265∗∗∗ -0.0125∗∗∗ (16.14) (4.40) (-9.98) (-4.69) Economics=1 0.0144∗∗∗ 0.0141∗∗∗ -0.00792∗ 0.0134∗∗∗ (3.95) (3.96) (-2.27) (3.86) Engineering=1 0.0343∗∗∗ 0.0118∗ -0.0111∗ -0.00435

(6.69) (2.38) (-2.44) (-0.94) Environmental science=1 0.0157∗ 0.0408∗∗∗ -0.00370 0.0130∗

- (2.51) (6.82) (-0.65) (2.31) Geography=1 0.0137∗∗ 0.0178∗∗∗ -0.0202∗∗∗ 0.00694 (2.79) (3.72) (-4.46) (1.51) Geology=1 -0.0259∗∗∗ -0.0214∗∗ -0.0198∗∗ -0.0478∗∗∗ (-3.59) (-3.17) (-3.15) (-7.76) History=1 -0.0452∗∗∗ -0.0347∗∗∗ -0.0236∗∗∗ 0.00698 (-7.54) (-5.89) (-4.11) (1.22) Materials science=1 -0.0113 0.00108 -0.0143∗ -0.00955 (-1.75) (0.17) (-2.30) (-1.63) Mathematics=1 0.00818∗ 0.0116∗∗ -0.00595 0.00644 (2.17) (3.19) (-1.60) (1.77) Medicine=1 -0.0490∗∗∗ -0.0229∗∗∗ -0.0593∗∗∗ -0.0327∗∗∗ (-16.29) (-7.74) (-21.56) (-11.94) Philosophy=1 0.00707 0.0105∗ 0.0117∗ 0.0208∗∗∗ (1.36) (2.09) (2.41) (4.24) Physics=1 0.0172∗∗∗ 0.0394∗∗∗ -0.0146∗∗∗ -0.00853∗ (4.53) (10.51) (-3.91) (-2.40) Political science=1 -0.0379∗∗∗ -0.0313∗∗∗ -0.0186∗∗ 0.0192∗∗ (-5.18) (-4.43) (-2.78) (2.72) Psychology=1 0.0270∗∗∗ 0.0305∗∗∗ -0.0274∗∗∗ -0.0238∗∗∗ (8.26) (9.69) (-9.17) (-7.82) Sociology=1 0.0124∗∗∗ 0.00962∗∗ 0.000168 -0.00156
- (3.56) (2.84) (0.05) (-0.48) Female=1 × Art=1 -0.0221∗∗ -0.0265∗∗∗ -0.00315 -0.0143 (-2.72) (-3.33) (-0.41) (-1.88)


Female=1 × Biology=1 0.000534 0.00131 0.00799∗ 0.00960∗∗ (0.14) (0.36) (2.38) (2.91)

Female=1 × Business=1 -0.0192∗∗ -0.0193∗∗ 0.00772 0.00466 (-3.09) (-3.14) (1.43) (0.82)

Female=1 × Chemistry=1 -0.0129∗∗ -0.00746 0.0118∗∗ 0.00808 (-2.61) (-1.53) (2.62) (1.82)

Female=1 × Computer science=1 0.0135∗∗∗ 0.00192 0.00724∗ -0.00786∗ (3.77) (0.55) (2.14) (-2.30)

Female=1 × Economics=1 0.00584 0.0104∗ -0.00134 0.00273 (1.34) (2.44) (-0.33) (0.67)

Female=1 × Engineering=1 0.00544 0.00159 -0.00860 -0.0205∗∗∗

(1.05) (0.31) (-1.78) (-4.21) Female=1 × Environmental science=1 0.0126 0.0132 0.0208∗ 0.0219∗

(1.07) (1.19) (2.03) (2.15) Female=1 × Geography=1 0.00959 0.00604 -0.0000779 -0.00886 (1.51) (0.98) (-0.01) (-1.50) Female=1 × Geology=1 -0.00473 -0.0140 0.00581 0.00868 (-0.42) (-1.33) (0.56) (0.90)

Female=1 × History=1 -0.00115 -0.00352 -0.00347 -0.0127 (-0.15) (-0.49) (-0.48) (-1.77)

Female=1 × Materials science=1 0.00312 0.00211 0.00837 0.0229∗∗ (0.33) (0.22) (0.98) (2.64)

Female=1 × Mathematics=1 -0.000606 -0.00257 -0.00261 0.00655 (-0.12) (-0.54) (-0.55) (1.39)

Female=1 × Medicine=1 0.00814∗ 0.00926∗ 0.0124∗∗∗ 0.0154∗∗∗

- (1.98) (2.37) (3.60) (4.45)

Female=1 × Philosophy=1 0.00872∗ 0.0133∗∗∗ 0.00835∗ 0.00179

- (2.13) (3.32) (2.13) (0.45)


Female=1 × Physics=1 0.00119 0.00323 -0.00299 -0.00927∗ (0.26) (0.73) (-0.69) (-2.14)

Female=1 × Political science=1 -0.00861∗ -0.00658 0.00241 0.00632 (-2.14) (-1.69) (0.64) (1.65)

Female=1 × Psychology=1 -0.00182 -0.00688 -0.00472 -0.00878∗ (-0.47) (-1.84) (-1.35) (-2.44)

Female=1 × Sociology=1 -0.00166 -0.00854∗ -0.000169 0.00735 (-0.40) (-2.11) (-0.04) (1.89)

DepSize -0.00000149∗∗∗ -0.000000677∗ 0.000000205 0.00000212∗∗∗ (-4.31) (-2.04) (0.74) (7.23)

CareerAge -0.00127∗∗∗ -0.00125∗∗∗ -0.000132∗∗ -0.000324∗∗∗ (-21.86) (-22.24) (-2.77) (-6.59)

Constant 0.548∗∗∗ 0.554∗∗∗ 0.514∗∗∗ 0.566∗∗∗

(131.33) (133.00) (128.22) (144.32) Observations 226208 226208 226208 226208

t statistics in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

###### 52/87

- Table S20. Linear regression model estimates for gender differences on content and context surprise and prescience scores by discipline (level zero field) in multi-authored papers. We compute White-robust standard errors. Research field fixed effects and dummies for publishing year are omitted.


(1) (2) (3) (4) Surprise (References) Prescience (References) Surprise (concepts) Prescience (concepts) Female Share 0.0189∗∗∗ 0.0102∗∗∗ -0.00849∗∗∗ -0.0144∗∗∗

(18.64) (9.47) (-7.47) (-13.37) Art=1 0.0373∗∗∗ 0.0512∗∗∗ 0.0135∗ 0.0711∗∗∗ (5.60) (8.20) (1.98) (10.36) Biology=1 0.0438∗∗∗ 0.00401∗∗∗ 0.00267∗∗∗ -0.0198∗∗∗

(83.39) (7.13) (4.53) (-35.47) Business=1 -0.0205∗∗∗ -0.00840∗∗∗ -0.0162∗∗∗ -0.00306

(-12.19) (-5.09) (-9.47) (-1.75) Chemistry=1 0.0182∗∗∗ -0.00364∗∗∗ -0.0216∗∗∗ -0.0255∗∗∗ (34.97) (-6.20) (-35.51) (-44.11) Computer science=1 0.0434∗∗∗ 0.0168∗∗∗ -0.0191∗∗∗ 0.000157 (62.83) (23.54) (-25.47) (0.22) Economics=1 0.00146 0.0109∗∗∗ -0.0235∗∗∗ 0.0309∗∗∗ (1.14) (8.48) (-17.27) (23.13) Engineering=1 0.0294∗∗∗ 0.00675∗∗∗ -0.0115∗∗∗ 0.00299∗∗ (27.94) (6.41) (-10.54) (2.86) Environmental science=1 0.0289∗∗∗ 0.0517∗∗∗ -0.00130 -0.0106∗∗∗ (24.63) (44.21) (-1.02) (-8.55) Geography=1 0.0183∗∗∗ 0.0269∗∗∗ -0.0161∗∗∗ 0.0262∗∗∗ (14.85) (21.81) (-11.79) (19.88) Geology=1 0.00123 -0.00698∗∗∗ -0.00904∗∗∗ -0.0345∗∗∗ (1.00) (-5.65) (-6.70) (-26.68) History=1 -0.0150∗∗∗ 0.00650∗∗ -0.000927 0.0605∗∗∗ (-5.97) (2.64) (-0.34) (23.24) Materials science=1 -0.00382∗∗∗ 0.0189∗∗∗ -0.0204∗∗∗ -0.0197∗∗∗ (-4.65) (21.62) (-22.18) (-22.71) Mathematics=1 0.00776∗∗∗ 0.0136∗∗∗ -0.0197∗∗∗ 0.0102∗∗∗ (7.89) (13.78) (-18.68) (10.08) Medicine=1 -0.0186∗∗∗ 0.00819∗∗∗ -0.0325∗∗∗ -0.0230∗∗∗ (-32.81) (13.59) (-51.61) (-38.42) Philosophy=1 0.0190∗∗∗ 0.0231∗∗∗ 0.0157∗∗∗ 0.0667∗∗∗ (5.73) (7.14) (4.59) (19.17) Physics=1 0.0152∗∗∗ 0.0347∗∗∗ -0.0132∗∗∗ -0.00325∗∗∗ (20.88) (45.68) (-16.43) (-4.25) Political science=1 -0.00592 0.00853∗∗ -0.0279∗∗∗ 0.0417∗∗∗ (-1.93) (2.85) (-9.30) (13.32) Psychology=1 0.0472∗∗∗ 0.0464∗∗∗ 0.00807∗∗∗ 0.0216∗∗∗ (58.90) (56.03) (8.83) (25.17) Sociology=1 0.0260∗∗∗ 0.0256∗∗∗ -0.00450∗ 0.00937∗∗∗ (15.80) (15.72) (-2.54) (5.34) Art=1 × Female Share 0.00661 0.000918 -0.0149∗∗ -0.0402∗∗∗ (1.42) (0.21) (-3.01) (-8.36) Biology=1 × Female Share -0.00651∗∗∗ -0.00257∗∗ 0.00517∗∗∗ 0.0000634 (-7.69) (-2.89) (5.48) (0.07) Business=1 × Female Share -0.0409∗∗∗ -0.0268∗∗∗ 0.00508∗ 0.00676∗∗ (-17.79) (-11.91) (2.13) (2.79) Chemistry=1 × Female Share -0.00358∗∗∗ -0.00638∗∗∗ 0.00308∗∗ 0.00800∗∗∗ (-3.92) (-6.34) (2.93) (7.98) Computer science=1 × Female Share 0.0258∗∗∗ 0.0120∗∗∗ 0.00135 -0.00780∗∗∗ (23.94) (10.80) (1.13) (-6.74) Economics=1 × Female Share 0.00452∗∗ 0.0108∗∗∗ 0.00651∗∗∗ 0.00533∗∗∗ (3.02) (7.21) (3.99) (3.41) Engineering=1 × Female Share 0.0186∗∗∗ 0.00379∗∗ -0.00900∗∗∗ -0.0144∗∗∗ (13.59) (2.69) (-6.04) (-9.96) Environmental science=1 × Female Share 0.0196∗∗∗ 0.0111∗∗∗ 0.00152 0.0252∗∗∗ (8.59) (4.83) (0.60) (10.17) Geography=1 × Female Share 0.000114 0.00241 0.00648∗∗ 0.000649 (0.06) (1.19) (2.90) (0.30) Geology=1 × Female Share 0.00989∗∗∗ 0.00575∗∗ 0.00492∗ 0.00605∗∗ (4.86) (2.76) (2.11) (2.74) History=1 × Female Share 0.0130∗∗ 0.0267∗∗∗ -0.0278∗∗∗ -0.0326∗∗∗ (3.17) (6.83) (-6.16) (-7.56) Materials science=1 × Female Share 0.00811∗∗∗ 0.0250∗∗∗ 0.00927∗∗∗ 0.0176∗∗∗ (5.51) (15.96) (5.55) (11.01) Mathematics=1 × Female Share 0.00182 0.00157 -0.000425 0.0102∗∗∗ (1.34) (1.14) (-0.28) (7.14) Medicine=1 × Female Share -0.00592∗∗∗ -0.00346∗∗∗ 0.00143 0.0115∗∗∗ (-7.07) (-3.84) (1.51) (12.73) Philosophy=1 × Female Share 0.0146∗∗∗ 0.0150∗∗∗ 0.0117∗∗∗ -0.0135∗∗∗ (8.52) (8.64) (6.27) (-7.34) Physics=1 × Female Share -0.000536 0.00564∗∗∗ -0.00356∗∗ -0.00353∗∗ (-0.48) (4.92) (-2.86) (-2.99) Political science=1 × Female Share -0.0115∗∗∗ -0.00671∗∗∗ -0.00552∗∗ 0.00868∗∗∗ (-6.97) (-4.16) (-3.23) (5.03) Psychology=1 × Female Share 0.00714∗∗∗ 0.00296∗ -0.00990∗∗∗ -0.0141∗∗∗ (6.22) (2.55) (-7.54) (-11.43) Sociology=1 × Female Share -0.00482∗∗∗ -0.00304∗ -0.0138∗∗∗ -0.0136∗∗∗ (-3.55) (-2.22) (-9.01) (-9.56) DepartmentSize 0.00000159∗∗∗ 0.00000124∗∗∗ 0.000000326∗∗∗ 0.00000192∗∗∗ (54.42) (38.99) (9.85) (60.43) CareerAge -0.000174∗∗∗ -0.000554∗∗∗ -0.000139∗∗∗ -0.000450∗∗∗ (-15.60) (-46.56) (-11.24) (-38.42) TeamSize 0.00139∗∗∗ 0.000694∗∗∗ 0.00102∗∗∗ 0.00273∗∗∗ (25.73) (13.01) (17.99) (34.73) TeamSize2 -0.000000421∗∗∗ -0.000000380∗∗∗ -0.000000162∗∗∗ -0.000000433∗∗∗ (-32.45) (-28.76) (-16.00) (-28.38) Num Gender Unknown -0.000308∗∗∗ 0.000265∗∗∗ -0.000589∗∗∗ -0.00159∗∗∗

(-4.80) (4.17) (-9.25) (-17.65) Constant 0.527∗∗∗ 0.529∗∗∗ 0.536∗∗∗ 0.591∗∗∗ (531.52) (509.80) (493.17) (573.93) Observations 4085543 4085543 4085543 4085543

t statistics in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

###### 53/87

###### G Prescience conditional on initial surprise

We examine how prescience varies with initial surprise of solo-authored papers across genders. We consider increasing thresholds of initial surprise (0.1 to 0.9, in 0.2 increments), and re-estimate the model on each subsample.

For reference combinations (Table S21), the gender gap in uptake decreases as initial surprise increases. For concept combinations (Table S22), women’s papers initially receive less uptake, but the gap is no longer statistically distinguishable from zero for papers above the 0.9 percentile. Table S23 shows no significant gender difference in two-step credit score for equally prescient reference combinations, no matter the initial level of surprise. Instead, Table S24 reports significant gender differences in downstream credit for concept combinations with mid-to-low initial surprise (0.1–0.5), with the gap becoming statistically indistinguishable from zero at higher surprise levels (>0.7).

For equally prescient works, women’s are on average more disruptive than men’s, with gender differences diminishing with increasing initial level of surprise, until they become insignificant at higher initial surprise values (>0.5 for concepts, >0.7 for references) – see Tables S25 and S26.

Overall, we find that gender is no longer significantly impacting recognition when reference or concept combinations are highly unexpected or surprise at their time of publication – i.e., with highest surprise scores in our sample.

- Table S21. Linear regression model estimates for prescience in reference combinations conditional on increasing thresholds of initial surprise score in solo-authored papers. We include author-level clustered standard errors. Research field fixed effects and dummies for publication year are omitted.

Prescience (References) Surprise (References) Score: >=0.1 >=0.3 >=0.5 >=0.7 >=0.9 Female=1 0.0201∗∗∗ 0.0145∗∗∗ 0.00909∗∗∗ 0.00536∗∗∗ 0.00274∗

(11.32) (8.84) (5.95) (3.84) (2.24)

DepSize −0.000000369 0.000000863∗ 0.000000976∗∗ 0.00000123∗∗∗ 0.000000809∗∗

(−1.10) (2.50) (2.80) (3.81) (2.71)

CareerAge −0.000975∗∗∗ −0.000536∗∗∗ −0.000212∗∗∗ −0.0000367 0.0000984∗

(−17.79) (−10.38) (−4.33) (−0.79) (2.40)

Constant 0.585∗∗∗ 0.665∗∗∗ 0.742∗∗∗ 0.826∗∗∗ 0.925∗∗∗

(150.19) (181.29) (213.16) (258.72) (332.68) Observations 208503 173387 138600 99842 47982

t statistics in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

- Table S22. Linear regression model estimates for prescience in concept combinations conditional on increasing thresholds of initial surprise score (higher than 0.1, 0.3, 0.5, 0.7, 0.9) in solo-authored papers. We include author-level clustered standard errors. Research field fixed effects and dummies for publication year are omitted.


Prescience (concepts) Surprise (concepts) Score: >=0.1 >=0.3 >=0.5 >=0.7 >=0.9 Female=1 −0.00755∗∗∗ −0.00773∗∗∗ −0.00536∗∗ −0.00477∗ −0.00167

(−4.28) (−4.29) (−2.86) (−2.27) (−0.60)

DepSize 0.00000275∗∗∗ 0.00000230∗∗∗ 0.00000182∗∗∗ 0.00000147∗∗∗ 0.00000140∗∗

(8.91) (7.67) (5.97) (4.38) (2.91)

CareerAge −0.000310∗∗∗ −0.000353∗∗∗ −0.000364∗∗∗ −0.000334∗∗∗ −0.000307∗∗∗

(−5.92) (−6.66) (−6.55) (−5.44) (−3.76)

Constant 0.557∗∗∗ 0.663∗∗∗ 0.734∗∗∗ 0.807∗∗∗ 0.889∗∗∗

(140.62) (168.57) (180.71) (177.39) (145.95) Observations 209293 166188 122332 78118 29309

t statistics in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

- Table S23. Linear regression model estimates for Two-step credit score in solo-authored papers in prescience in reference combinations conditional on increasing thresholds of initial surprise score (higher than 0.1, 0.3, 0.5, 0.7, 0.9). We include author-level clustered standard errors. Research field fixed effects and dummies for publication year are omitted.

Two-step Credit Score

Surprise (References) Score: >=0.1 >=0.3 >=0.5 >=0.7 >=0.9 Female=1 −0.000215 0.00115 0.00196 0.00228 0.00831

(−0.20) (0.95) (1.37) (1.17) (1.52)

Prescience (References) −0.0110∗∗∗ −0.0103∗∗∗ −0.0102∗∗∗ −0.0101∗∗∗ −0.0144∗∗∗

(−16.37) (−14.26) (−11.94) (−8.75) (−5.10)

Female=1 × Prescience (References) −0.000874 −0.00259 −0.00346∗ −0.00376 −0.00975

(−0.67) (−1.76) (−2.05) (−1.70) (−1.65)

DepSize −0.00000132∗∗∗ −0.00000119∗∗∗ −0.00000108∗∗∗ −0.000000916∗∗∗ −0.000000698∗∗∗

(−18.48) (−16.49) (−14.64) (−11.31) (−7.33)

CareerAge −0.000127∗∗∗ −0.000119∗∗∗ −0.000111∗∗∗ −0.000104∗∗∗ −0.0000643∗∗∗

- (−9.96) (−9.48) (−8.67) (−7.85) (−4.22)

OpenAccess −0.00324∗∗∗ −0.00271∗∗∗ −0.00245∗∗∗ −0.00189∗∗∗ −0.00159∗∗∗

- (−10.11) (−8.61) (−7.76) (−5.76) (−4.09)


Constant 0.0388∗∗∗ 0.0375∗∗∗ 0.0362∗∗∗ 0.0346∗∗∗ 0.0366∗∗∗

(47.39) (44.98) (38.80) (28.85) (13.63) Observations 93182 83988 71914 55443 29378

t statistics in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

- Table S24. Linear regression model estimates for Two-step Credit Score in solo-authored papers in prescience of concept combinations conditional on increasing thresholds of initial surprise score (higher than 0.1, 0.3, 0.5, 0.7, 0.9). We include author-level clustered standard errors. Research field fixed effects and dummies for publication year are omitted.


Two-step Credit Score

Surprise (concepts) Score: >=0.1 >=0.3 >=0.5 >=0.7 >=0.9 Female=1 −0.00225∗∗ −0.00305∗∗ −0.00329∗ −0.00327 0.00409

(−2.91) (−2.97) (−2.38) (−1.54) (0.71)

Prescience (Concepts) −0.0106∗∗∗ −0.0124∗∗∗ −0.0139∗∗∗ −0.0146∗∗∗ −0.0136∗∗∗

(−16.41) (−14.80) (−13.29) (−10.10) (−4.84)

Female=1 × Prescience (Concepts) 0.00191 0.00295∗ 0.00335 0.00315 −0.00494

(1.73) (2.13) (1.90) (1.24) (−0.75)

DepSize −0.00000136∗∗∗ −0.00000129∗∗∗ −0.00000127∗∗∗ −0.00000127∗∗∗ −0.00000110∗∗∗

(−18.20) (−15.84) (−14.58) (−12.64) (−6.59)

CareerAge −0.000121∗∗∗ −0.000122∗∗∗ −0.000116∗∗∗ −0.000130∗∗∗ −0.000154∗∗∗

- (−8.96) (−8.39) (−7.40) (−6.69) (−5.20)

OpenAccess −0.00325∗∗∗ −0.00355∗∗∗ −0.00325∗∗∗ −0.00272∗∗∗ −0.00319∗∗∗

- (−9.51) (−9.60) (−7.95) (−5.28) (−3.89)


Constant 0.0388∗∗∗ 0.0404∗∗∗ 0.0423∗∗∗ 0.0435∗∗∗ 0.0445∗∗∗

(50.19) (42.17) (36.64) (27.29) (15.07) Observations 89747 72941 55085 35954 13760

t statistics in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

###### Table S25. Linear regression model estimates for five-year disruption score in solo-authored papers in prescience referencecombinations, conditional on increasing thresholds of initial surprise score (higher than 0.1, 0.3, 0.5, 0.7, 0.9). We includeauthor-level clustered standard errors. Research field fixed effects and dummies for publication year are omitted.

5-year Disruption

Surprise (References) Score: >=0.1 >=0.3 >=0.5 >=0.7 >=0.9 Female=1 0.00443∗∗∗ 0.00266∗∗∗ 0.00119∗∗∗ 0.000240 0.000429

(7.54) (5.19) (3.30) (0.60) (0.61)

Prescience (References) −0.00716∗∗∗ −0.00244∗∗∗ −0.000669∗ 0.000187 0.00161∗∗∗

(−18.20) (−8.58) (−2.54) (0.64) (3.62)

Female=1 × Prescience (References) −0.00581∗∗∗ −0.00325∗∗∗ −0.00133∗∗ −0.000212 −0.000586

(−7.53) (−4.98) (−3.03) (−0.45) (−0.75)

DepSize −3.36e−09 1.60e−08 3.32e−09 −1.30e−08 −1.75e−08

(−0.22) (1.20) (0.25) (−0.91) (−1.01)

CareerAge 0.0000222∗∗∗ 0.0000182∗∗∗ 0.0000123∗∗∗ 0.00000844∗∗ −0.00000258

(4.43) (4.80) (4.14) (3.04) (−0.84)

OpenAccess −0.000582∗∗∗ −0.000553∗∗∗ −0.000641∗∗∗ −0.000607∗∗∗ −0.000460∗∗∗

(−4.39) (−5.13) (−7.28) (−7.08) (−4.74)

impact_factor_2y −0.000143∗∗∗ −0.000126∗∗∗ −0.000117∗∗∗ −0.000100∗∗∗ −0.0000849∗

(−8.47) (−6.92) (−5.39) (−3.82) (−2.38)

2y_cites −0.0000680∗∗∗ −0.000102∗∗∗ −0.000107∗∗∗ −0.000115∗∗∗ −0.000118∗∗∗

(−7.98) (−11.88) (−11.60) (−10.84) (−8.94)

Constant 0.00211∗∗∗ −0.00220∗∗∗ −0.00372∗∗∗ −0.00486∗∗∗ −0.00614∗∗∗

(3.58) (−4.95) (−8.98) (−13.45) (−11.45) Observations 196587 164114 131648 95175 45725

t statistics in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

###### Table S26. Linear regression model estimates for five-year disruption score in solo-authored papers in prescience in conceptsconditional on increasing thresholds of initial surprise score (higher than 0.1, 0.3, 0.5, 0.7, 0.9). We include author-levelclustered standard errors. Research field fixed effects and dummies for publication year are omitted.

5-year Disruption

Surprise (concepts) Score: >=0.1 >=0.3 >=0.5 >=0.7 >=0.9 Female=1 0.00140∗∗∗ 0.00149∗∗ 0.0000178 −0.0000154 −0.00101

(3.31) (2.61) (0.02) (−0.01) (−0.43)

Prescience (Concepts) 0.00134∗∗∗ 0.00171∗∗∗ 0.00164∗∗ 0.00163∗ 0.000701

(3.62) (3.83) (2.88) (2.27) (0.45)

Female=1 × Prescience (Concepts) −0.000689 −0.000881 0.000981 0.000688 0.00185

(−1.04) (−1.06) (0.98) (0.52) (0.67)

DepSize −3.59e−08 −4.42e−08 −3.13e−08 −1.83e−08 5.25e−08

(−1.41) (−1.56) (−0.99) (−0.50) (0.79)

CareerAge 0.0000562∗∗∗ 0.0000593∗∗∗ 0.0000549∗∗∗ 0.0000555∗∗∗ 0.0000712∗∗∗

(8.66) (8.10) (6.70) (5.50) (4.48)

OpenAccess −0.000288 −0.000269 −0.000388 −0.000670∗ −0.00127∗∗

- (−1.57) (−1.33) (−1.71) (−2.41) (−2.67)

impact_factor_2y −0.0000733∗ −0.0000656 −0.0000621 −0.0000385 −0.0000667

- (−2.38) (−1.87) (−1.50) (−0.66) (−0.89)

2y_cites −0.0000542∗∗∗ −0.0000522∗∗ −0.0000597∗∗ −0.0000653∗∗ −0.0000668∗∗

- (−3.52) (−3.12) (−3.14) (−2.81) (−3.21)

Constant −0.00259∗∗∗ −0.00389∗∗∗ −0.00387∗∗∗ −0.00364∗∗∗ −0.00339

- (−4.15) (−6.13) (−5.01) (−3.62) (−1.80)


Observations 196922 156476 114957 73406 27446

t statistics in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

H Outside subject citation share

###### Table S27 reports the model coefficient estimates behind Figure 4 of the main text.

- Table S27. Linear Regression model estimates of outside- and inside-subject citation share on surprise and prescience score by authors’ gender in solo-authored papers. Outside citation share is equal to 1−InsideSubjectCitationShare. Research field fixed effects and dummies for publishing year are omitted. Standard errors are clustered at the author level.


(1) (2) outside_subject_share inside_subject_share Female=1 0.0304∗∗∗ −0.0304∗∗∗

(5.78) (−5.78)

Surprise (References) 0.0750∗∗∗ −0.0750∗∗∗

(23.66) (−23.66)

Female=1 × Surprise (References) −0.0232∗∗∗ 0.0232∗∗∗

(−3.89) (3.89)

Surprise (Concepts) −0.0196∗∗∗ 0.0196∗∗∗

(−6.75) (6.75)

Female=1 × Surprise (Concepts) −0.00236 0.00236

(−0.43) (0.43)

DepSize 0.00000163∗∗∗ −0.00000163∗∗∗

(4.83) (−4.83)

CareerAge 0.000555∗∗∗ −0.000555∗∗∗

(9.69) (−9.69)

OpenAccess=1 0.0146∗∗∗ −0.0146∗∗∗

(8.65) (−8.65)

Constant 0.344∗∗∗ 0.656∗∗∗

(74.31) (141.91) Observations 189701 189701

t statistics in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

###### I Multi-authored papers

We examine how the share of women among authors in multi-authored papers relates to novelty. We estimate models (1) and

- (2) of the main text with a continuous variable for female share within teams, FemaleSharei, measuring the proportion of clearly-coded women (U.S., white and Hispanic) among the authors of a paper. Controls include average department size of team members (matched with the paper’s field), year of publication, fine-grained research area dummies (level 1), average career age of team members, team size and squared team size, and the number of authors with unknown gender (Gender Num Unknown).


Table S28 reports the regression coefficients, and Figure S21 shows predicted novelty outcomes by women share, with 95% confidence intervals. Predicted outcomes indicate that increasing the share of women among authors is associated with higher reference surprise and reference prescience, but lower concept surprise and prescience. These patterns are broadly consistent with results for solo-authored papers.

We further examine how women’s share in teams relates to scholarly rewards (two-step credit, disruption, and journal impact factor). Regression results are reported in Tables S29–S31, and predicted outcomes in Figures S22 and S23. For equally surprising or prescient science, teams with a higher share of clearly coded women tend to receive lower two-step citation credit and are placed in lower-impact journals, but produce more disruptive contributions – consistent with patterns observed for solo-authored work.

Teams with a higher share of women experience a smaller penalty in downstream citation credit as prescience increases, for both concept and reference combinations (Table S29).

Reference surprise is negatively associated with disruption, and this decline is steeper for teams with more women, again reflecting patterns observed in solo-authored papers, while gender gaps in disruption remain stable as novelty increases (Table S30). Teams with a higher share of women also face lower marginal returns to journal prestige as surprise increases (Table S31). This contrasts with the solo-authored case, where women exhibit a steeper positive relationship between novelty and journal

impact factor. As discussed in the main text, this difference disappears when we model the non-linear association between gender composition and journal placement, comparing all-women and all-men teams (Section Q).

# a b

###### Context (Reference) Combinations Content (Concept) Combinations

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |


| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


Surprise

# c d

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |


| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |


Prescience

Share of Women in Field

Share of Women in Field

- Figure S21. Predicted values of surprise and prescience by women share in multi-authored papers, alongside 95% confidence intervals, marginalized over observed distribution of covariates.


| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


2-Step CreditDisruptionImpact Factor

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


% Women

Context (Reference) Surprise Content (Concept) Surprise

- Figure S22. Rewards to Surprise by women share in multi-authored papers, alongside 95% confidence intervals. The solid lines and shaded areas show the estimated margins and their confidence intervals for each level of the share of women in the team, marginalized over observed distribution of covariates.


| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


Disruption2-Step Credit

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


% Women

Context (Reference) Prescience Content (Concept) Prescience

- Figure S23. Rewards to Prescience by women share in multi-authored papers, alongside 95% confidence intervals. The solid lines and shaded areas show the estimated margins and their confidence intervals for each level of the share of women in the team, marginalized over observed distribution of covariates.


- Table S28. Linear regression model estimates of content and context surprise and prescience scores by gender shares in multi-authored papers. We include White standard errors. Research field fixed effects and dummies for publishing year are omitted.


(1) (2) (3) (4) Surprise (References) Prescience (References) Surprise (concepts) Prescience (concepts) Female Share 0.0205∗∗∗ 0.0133∗∗∗ -0.00658∗∗∗ -0.00963∗∗∗

(52.48) (31.97) (-15.08) (-23.25) DepartmentSize 0.00000154∗∗∗ 0.00000117∗∗∗ 0.000000394∗∗∗ 0.00000196∗∗∗ (52.64) (37.03) (11.91) (61.88) CareerAge -0.000160∗∗∗ -0.000548∗∗∗ -0.000153∗∗∗ -0.000468∗∗∗ (-14.24) (-45.96) (-12.37) (-39.95) TeamSize 0.00142∗∗∗ 0.000716∗∗∗ 0.000993∗∗∗ 0.00267∗∗∗ (26.12) (13.41) (17.56) (34.39) TeamSize2 -0.000000427∗∗∗ -0.000000374∗∗∗ -0.000000161∗∗∗ -0.000000423∗∗∗ (-32.51) (-28.53) (-15.98) (-28.22) Num Gender Unknown -0.000326∗∗∗ 0.000223∗∗∗ -0.000557∗∗∗ -0.00155∗∗∗

(-5.02) (3.51) (-8.79) (-17.42) Constant 0.542∗∗∗ 0.539∗∗∗ 0.523∗∗∗ 0.578∗∗∗ (579.17) (551.90) (510.95) (596.49) Observations 4085543 4085543 4085543 4085543

t statistics in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

- Table S29. Linear regression model estimates of 2-steps credit score for surprise and prescience scores in multi-authored papers. We include White standard errors. Research field fixed effects and dummies for publishing year are omitted.


(1) (2) (3) (4) TwoStepsCreditScore TwoStepsCreditScore TwoStepsCreditScore TwoStepsCreditScore Female Share -0.00161∗∗∗ -0.00157∗∗∗ -0.000325∗ -0.000820∗∗∗

(-6.32) (-7.92) (-2.01) (-4.30) Surprise (References) -0.0141∗∗∗

(-99.01) Female Share× Surprise (References) 0.00222∗∗∗ (6.94) DepartmentSize -0.000000420∗∗∗ -0.000000425∗∗∗ -0.000000424∗∗∗ -0.000000405∗∗∗ (-53.59) (-54.29) (-54.12) (-51.96) CareerAge -0.0000140∗∗∗ -0.0000172∗∗∗ -0.0000113∗∗∗ -0.0000169∗∗∗ (-6.62) (-8.10) (-5.33) (-7.96) OpenAccess -0.00240∗∗∗ -0.00278∗∗∗ -0.00287∗∗∗ -0.00270∗∗∗ (-47.86) (-55.36) (-56.80) (-53.68) TeamSize -0.000285∗∗∗ -0.000283∗∗∗ -0.000268∗∗∗ -0.000244∗∗∗ (-22.53) (-22.42) (-22.14) (-21.19) TeamSize2 1.73e-08∗∗∗ 1.80e-08∗∗∗ 1.92e-08∗∗∗ 1.60e-08∗∗∗ (11.64) (12.08) (12.88) (11.08) Num Gender Unknown 0.000236∗∗∗ 0.000232∗∗∗ 0.000214∗∗∗ 0.000199∗∗∗

(17.22) (16.96) (16.29) (15.89) Prescience (References) -0.0118∗∗∗

(-98.59) Female Share× Prescience (References) 0.00222∗∗∗ (8.34) Surprise (concepts) -0.00272∗∗∗ (-25.49) Female Share× Surprise (concepts) -0.00000244 (-0.01)

Prescience (concepts) -0.0122∗∗∗ (-104.79)

Female Share× Prescience (concepts) 0.000642∗ (2.47)

Constant 0.0354∗∗∗ 0.0339∗∗∗ 0.0287∗∗∗ 0.0345∗∗∗ (239.56) (249.38) (224.02) (255.70)

Observations 2451029 2451029 2451029 2451029

t statistics in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

- Table S30. Linear regression model estimates of disruption score of publication on surprise and prescience scores by gender in multi-authored papers, with White standard errors. Research field fixed effects and dummies for publishing year are omitted.


(1) (2) (3) (4) (5) (6) (7) (8) 3-years Disruption 3-years Disruption 3-years Disruption 3-years Disruption 5-year Disruption 5-year Disruption 5-year Disruption 5-year Disruption

Female Share 0.00124∗∗∗ 0.000915∗∗∗ 0.000496∗∗∗ 0.000600∗∗∗ 0.00104∗∗∗ 0.000775∗∗∗ 0.000423∗∗∗ 0.000553∗∗∗

(6.24) (6.12) (5.85) (6.07) (5.39) (5.36) (5.13) (5.76) Surprise (References) −0.00127∗∗∗ −0.00257∗∗∗

###### (−9.55) (−20.53)

Female Share× Surprise (References) −0.00113∗∗∗ −0.000886∗∗∗

###### (−4.45) (−3.59)

DepartmentSize −2.40e−08∗∗∗ −2.41e−08∗∗∗ −2.51e−08∗∗∗ −2.72e−08∗∗∗ −2.01e−08∗∗∗ −2.06e−08∗∗∗ −2.22e−08∗∗∗ −2.44e−08∗∗∗

###### (−8.04) (−8.10) (−8.32) (−9.13) (−7.20) (−7.39) (−7.85) (−8.72)

CareerAge −0.00000769∗∗∗ −0.00000819∗∗∗ −0.00000728∗∗∗ −0.00000662∗∗∗ −0.00000628∗∗∗ −0.00000698∗∗∗ −0.00000550∗∗∗ −0.00000480∗∗∗

###### (−6.52) (−6.92) (−6.18) (−5.60) (−5.56) (−6.16) (−4.86) (−4.24)

OpenAccess −0.000606∗∗∗ −0.000634∗∗∗ −0.000666∗∗∗ −0.000693∗∗∗ −0.000552∗∗∗ −0.000608∗∗∗ −0.000658∗∗∗ −0.000687∗∗∗

(−19.83) (−20.62) (−21.35) (−22.43) (−18.92) (−20.76) (−22.17) (−23.30)

TeamSize −0.000141∗∗∗ −0.000142∗∗∗ −0.000141∗∗∗ −0.000144∗∗∗ −0.000129∗∗∗ −0.000129∗∗∗ −0.000128∗∗∗ −0.000131∗∗∗

(−13.97) (−14.01) (−13.89) (−14.10) (−13.99) (−14.05) (−13.84) (−14.07)

TeamSize2 1.12e−08∗∗∗ 1.12e−08∗∗∗ 1.16e−08∗∗∗ 1.21e−08∗∗∗ 9.39e−09∗∗∗ 9.56e−09∗∗∗ 1.03e−08∗∗∗ 1.07e−08∗∗∗

(7.66) (7.70) (7.88) (8.18) (7.02) (7.16) (7.54) (7.86)

2-year Journal Impact Factor −0.000270∗∗∗ −0.000273∗∗∗ −0.000274∗∗∗ −0.000277∗∗∗ −0.000268∗∗∗ −0.000273∗∗∗ −0.000276∗∗∗ −0.000279∗∗∗

(−12.95) (−13.08) (−12.93) (−12.94) (−15.13) (−15.43) (−15.12) (−15.09)

two-year citations −0.0000156 −0.0000155 −0.0000159 −0.0000164 −0.0000108 −0.0000107 −0.0000114 −0.0000118

###### (−1.83) (−1.82) (−1.85) (−1.87) (−1.50) (−1.49) (−1.55) (−1.58)

Num Gender Unknown 0.000115∗∗∗ 0.000116∗∗∗ 0.000114∗∗∗ 0.000115∗∗∗ 0.000107∗∗∗ 0.000107∗∗∗ 0.000105∗∗∗ 0.000106∗∗∗

(12.98) (13.00) (12.83) (12.93) (12.87) (12.87) (12.55) (12.66) Prescience (References) −0.00133∗∗∗ −0.00226∗∗∗

(−11.69) (−21.52)

Female Share× Prescience (References) −0.000722∗∗∗ −0.000573∗∗

###### (−3.60) (−2.95)

Surprise (concepts) −0.0000978 −0.0000791

###### (−1.44) (−1.23)

Female Share× Surprise (concepts) −0.0000564 −0.0000346

###### (−0.45) (−0.28)

Prescience (concepts) 0.00142∗∗∗ 0.00150∗∗∗

(15.27) (17.61)

Female Share× Prescience (concepts) −0.000206 −0.000230

###### (−1.46) (−1.67)

Constant −0.00626∗∗∗ −0.00620∗∗∗ −0.00684∗∗∗ −0.00769∗∗∗ −0.00501∗∗∗ −0.00515∗∗∗ −0.00630∗∗∗ −0.00718∗∗∗

(−38.07) (−39.57) (−49.53) (−52.49) (−32.63) (−35.33) (−48.69) (−52.64) Observations 3864378 3864378 3864378 3864378 3864455 3864455 3864455 3864455

t statistics in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

- Table S31. Linear regression model estimates of log of journal impact factor on surprise on multi-authored papers, with White standard errors. Research field fixed effects and dummies for publishing year are omitted.


(1) (2) (3) (4)

ln(2-year Journal Impact Factor) ln(2-year Journal Impact Factor) ln(5y Impact Factor) ln(5y Impact Factor) Female Share -0.0228∗∗∗ -0.0476∗∗∗ -0.0227∗∗∗ -0.0408∗∗∗

(-10.86) (-28.85) (-10.75) (-24.48) Surprise (References) 0.246∗∗∗ 0.263∗∗∗

(176.43) (186.42) Female Share× Surprise (References) -0.0408∗∗∗ -0.0341∗∗∗ (-14.12) (-11.72) DepartmentSize 0.0000117∗∗∗ 0.0000120∗∗∗ 0.0000120∗∗∗ 0.0000122∗∗∗ (166.48) (169.24) (170.81) (173.70) CareerAge 0.00101∗∗∗ 0.000950∗∗∗ 0.00105∗∗∗ 0.000989∗∗∗

(43.81) (40.94) (45.31) (42.20) OpenAccess 0.184∗∗∗ 0.193∗∗∗ 0.178∗∗∗ 0.187∗∗∗ (302.79) (316.54) (290.15) (304.83) TeamSize 0.0178∗∗∗ 0.0179∗∗∗ 0.0182∗∗∗ 0.0183∗∗∗

(39.46) (39.60) (39.44) (39.58) TeamSize2 -0.00000157∗∗∗ -0.00000165∗∗∗ -0.00000151∗∗∗ -0.00000160∗∗∗ (-31.31) (-31.79) (-31.15) (-31.70) Num Gender Unknown -0.0137∗∗∗ -0.0136∗∗∗ -0.0143∗∗∗ -0.0142∗∗∗ (-28.24) (-27.88) (-28.90) (-28.53) Surprise (concepts) 0.0495∗∗∗ 0.0501∗∗∗ (40.85) (40.97) Female Share× Surprise (concepts) 0.00387 0.000319 (1.53) (0.13)

Constant 0.966∗∗∗ 1.075∗∗∗ 1.002∗∗∗ 1.119∗∗∗ (426.11) (480.65) (439.84) (498.09)

Observations 3861357 3861357 3864495 3864495

t statistics in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

###### J Heterogeneity between solo and mixed multi-authored papers

Tables S33–S35 report estimates of how gender gaps in the rewards to innovation differ between solo-authored and multiauthored papers (including both mixed-gender and gender-homogeneous teams). We find that gender gaps in disruption and journal impact factor narrow more rapidly with increasing surprise or prescience for solo-authored papers – particularly for work that combines references —- than for multi-authored papers.

- Table S32. Linear regression model estimates for content and context surprise and prescience scores comparing gender differences between solo- and multi-authored papers, with White robust standard errors. Research field fixed effects and dummies for publishing year are omitted.


(1) (2) (3) (4) Surprise (References) Prescience (References) Surprise (concepts) Prescience (concepts) Female Share 0.0205∗∗∗ 0.0137∗∗∗ -0.00634∗∗∗ -0.00920∗∗∗

(52.63) (32.96) (-14.60) (-22.30) DummySolo=1 -0.0523∗∗∗ -0.0475∗∗∗ -0.0200∗∗∗ -0.0267∗∗∗ (-67.10) (-60.87) (-26.27) (-36.56) DummySolo=1 × Female Share 0.00607∗∗∗ 0.00548∗∗∗ -0.00182 -0.00485∗∗∗ (4.22) (3.83) (-1.29) (-3.57) DepartmentSize 0.00000154∗∗∗ 0.00000120∗∗∗ 0.000000389∗∗∗ 0.00000194∗∗∗ (52.90) (38.04) (11.88) (61.87) CareerAge -0.000261∗∗∗ -0.000604∗∗∗ -0.000164∗∗∗ -0.000449∗∗∗ (-24.00) (-52.56) (-13.91) (-39.91) TeamSize 0.00146∗∗∗ 0.000716∗∗∗ 0.00105∗∗∗ 0.00263∗∗∗ (26.63) (13.42) (18.47) (34.29) TeamSize2 -0.000000436∗∗∗ -0.000000377∗∗∗ -0.000000167∗∗∗ -0.000000418∗∗∗ (-32.71) (-28.70) (-16.39) (-28.13) Num Gender Unknown -0.000339∗∗∗ 0.000235∗∗∗ -0.000600∗∗∗ -0.00152∗∗∗

(-5.19) (3.69) (-9.42) (-17.32) Constant 0.547∗∗∗ 0.544∗∗∗ 0.522∗∗∗ 0.578∗∗∗ (599.22) (573.48) (528.65) (616.09) Observations 4311751 4311751 4311751 4311751

t statistics in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

- Table S33. Linear regression model estimates for log of journal impact factor on differential between solo and multi-authored papers in content and context surprise scores by gender, with White standard errors. Research field fixed effects and dummies for publishing year are omitted.


(1) (2) (3) (4) ln(2y Impact Factor) ln(2y Impact Factor) ln(5y Impact Factor) ln(5y Impact Factor) Female Share -0.0239∗∗∗ -0.0471∗∗∗ -0.0238∗∗∗ -0.0402∗∗∗

(-11.39) (-28.58) (-11.25) (-24.17) DummySolo=1 0.0944∗∗∗ -0.0107∗∗ 0.0954∗∗∗ -0.0115∗∗∗ (26.10) (-3.25) (26.19) (-3.45) DummySolo=1 × Female Share -0.0467∗∗∗ -0.0280∗∗∗ -0.0491∗∗∗ -0.0282∗∗∗

(-6.57) (-4.70) (-6.86) (-4.66) Surprise (References) 0.245∗∗∗ 0.262∗∗∗

(175.51) (185.79) Female Share× Surprise (References) -0.0392∗∗∗ -0.0325∗∗∗

(-13.58) (-11.18) DummySolo=1 × Surprise (References) -0.228∗∗∗ -0.235∗∗∗ (-43.75) (-44.66)

DummySolo=1 × Female Share× Surprise (References) 0.0822∗∗∗ 0.0903∗∗∗ (8.21) (8.92)

DepartmentSize 0.0000118∗∗∗ 0.0000121∗∗∗ 0.0000121∗∗∗ 0.0000123∗∗∗ (169.27) (171.91) (173.42) (176.21)

CareerAge 0.00118∗∗∗ 0.00112∗∗∗ 0.00120∗∗∗ 0.00114∗∗∗

(52.94) (50.06) (53.66) (50.49) OpenAccess 0.182∗∗∗ 0.190∗∗∗ 0.175∗∗∗ 0.185∗∗∗ (305.72) (319.17) (292.41) (306.77) TeamSize 0.0175∗∗∗ 0.0176∗∗∗ 0.0179∗∗∗ 0.0180∗∗∗

(39.57) (39.71) (39.55) (39.69) TeamSize2 -0.00000154∗∗∗ -0.00000162∗∗∗ -0.00000148∗∗∗ -0.00000157∗∗∗ (-31.29) (-31.77) (-31.11) (-31.66) Num Gender Unknown -0.0135∗∗∗ -0.0133∗∗∗ -0.0141∗∗∗ -0.0140∗∗∗ (-28.29) (-27.93) (-28.99) (-28.60) Surprise (concepts) 0.0489∗∗∗ 0.0495∗∗∗ (40.38) (40.56) Female Share× Surprise (concepts) 0.00323 -0.000333 (1.28) (-0.13) DummySolo=1 × Surprise (concepts) -0.0747∗∗∗ -0.0811∗∗∗ (-14.40) (-15.44) DummySolo=1 × Female Share× Surprise (concepts) 0.0523∗∗∗ 0.0564∗∗∗ (5.38) (5.72)

Constant 0.955∗∗∗ 1.064∗∗∗ 0.992∗∗∗ 1.110∗∗∗ (430.81) (487.76) (445.04) (505.92)

Observations 4073759 4073759 4077428 4077428

t statistics in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

- Table S34. Linear regression model estimates for 2-steps out credit on differential between solo and multi-authored papers in content and context surprise and prescience scores by gender. We include White standard errors. Research field fixed effects and dummies for publishing year are omitted.


(1) (2) (3) (4) TwoStepsCreditScore TwoStepsCreditScore TwoStepsCreditScore TwoStepsCreditScore Female Share -0.00155∗∗∗ -0.00154∗∗∗ -0.000313 -0.000797∗∗∗

(-6.10) (-7.76) (-1.94) (-4.18) DummySolo=1 0.000336 0.00160∗∗ 0.000228 0.00103∗ (0.61) (3.24) (0.65) (2.43) DummySolo=1 × Female Share 0.0000495 0.00139 -0.000922 -0.00158∗

(0.04) (1.30) (-1.43) (-2.08) Surprise (References) -0.0140∗∗∗

(-98.65) Female Share× Surprise (References) 0.00214∗∗∗ (6.70) DummySolo=1 × Surprise (References) 0.0000868 (0.13) DummySolo=1 × Female Share× Surprise (References) -0.00105 (-0.75) DepartmentSize -0.000000431∗∗∗ -0.000000436∗∗∗ -0.000000435∗∗∗ -0.000000416∗∗∗ (-55.38) (-56.06) (-55.90) (-53.76) CareerAge -0.0000223∗∗∗ -0.0000253∗∗∗ -0.0000192∗∗∗ -0.0000245∗∗∗ (-10.69) (-12.11) (-9.15) (-11.74) OpenAccess -0.00243∗∗∗ -0.00280∗∗∗ -0.00287∗∗∗ -0.00270∗∗∗ (-48.82) (-56.18) (-57.46) (-54.34) TeamSize -0.000276∗∗∗ -0.000273∗∗∗ -0.000258∗∗∗ -0.000235∗∗∗ (-22.28) (-22.17) (-21.83) (-20.83) TeamSize2 1.69e-08∗∗∗ 1.76e-08∗∗∗ 1.88e-08∗∗∗ 1.57e-08∗∗∗ (11.43) (11.86) (12.65) (10.89) Num Gender Unknown 0.000227∗∗∗ 0.000223∗∗∗ 0.000205∗∗∗ 0.000190∗∗∗

(16.96) (16.70) (15.97) (15.53) Prescience (References) -0.0117∗∗∗

(-98.21) Female Share× Prescience (References) 0.00218∗∗∗ (8.17) DummySolo=1 × Prescience (References) -0.00181∗∗ (-2.84) DummySolo=1 × Female Share× Prescience (References) -0.00306∗ (-2.30) Surprise (concepts) -0.00268∗∗∗ (-25.11) Female Share× Surprise (concepts) -0.00000786 (-0.03) DummySolo=1 × Surprise (concepts) 0.000394 (0.72) DummySolo=1 × Female Share× Surprise (concepts) 0.000126 (0.12)

Prescience (concepts) -0.0121∗∗∗ (-103.90)

Female Share× Prescience (concepts) 0.000624∗ (2.40)

DummySolo=1 × Prescience (concepts) -0.00143∗ (-2.37)

DummySolo=1 × Female Share× Prescience (concepts) 0.00118 (1.07)

Constant 0.0355∗∗∗ 0.0341∗∗∗ 0.0288∗∗∗ 0.0346∗∗∗ (241.26) (251.70) (226.48) (257.62)

Observations 2547542 2547542 2547542 2547542

t statistics in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

- Table S35. Linear regression model estimates for five-year disruption score of publication on for differential between solo and multi-authored papers in content and context surprise and prescience scores by gender, with White standard errors. Research field fixed effects and dummies for publishing year are omitted.


(1) (2) (3) (4) 5y Disruption 5y Disruption 5y Disruption 5y Disruption Female Share 0.00105∗∗∗ 0.000791∗∗∗ 0.000441∗∗∗ 0.000552∗∗∗

- (5.46) (5.46) (5.34) (5.74) DummySolo=1 0.00821∗∗∗ 0.00739∗∗∗ 0.00273∗∗∗ 0.00284∗∗∗ (23.96) (24.23) (13.55) (12.72) DummySolo=1 × Female Share 0.00520∗∗∗ 0.00486∗∗∗ 0.00114∗∗ 0.000912∗
- (6.98) (7.12) (2.84) (2.13) Surprise (References) -0.00257∗∗∗


(-20.58) Female Share× Surprise (References) -0.000887∗∗∗ (-3.60) DummySolo=1 × Surprise (References) -0.00982∗∗∗ (-22.19) DummySolo=1 × Female Share× Surprise (References) -0.00708∗∗∗ (-7.52) DepartmentSize -1.70e-08∗∗∗ -1.71e-08∗∗∗ -2.02e-08∗∗∗ -2.23e-08∗∗∗ (-6.09) (-6.13) (-7.11) (-7.95) CareerAge -0.00000307∗∗ -0.00000354∗∗ -0.000000793 -0.000000108 (-2.69) (-3.10) (-0.69) (-0.09) OpenAccess -0.000541∗∗∗ -0.000590∗∗∗ -0.000640∗∗∗ -0.000667∗∗∗ (-18.55) (-20.16) (-21.53) (-22.62) TeamSize -0.000127∗∗∗ -0.000129∗∗∗ -0.000129∗∗∗ -0.000131∗∗∗ (-13.89) (-14.00) (-13.76) (-14.00) TeamSize2 9.13e-09∗∗∗ 9.30e-09∗∗∗ 1.02e-08∗∗∗ 1.07e-08∗∗∗ (6.84) (6.97) (7.44) (7.76) Num Gender Unknown 0.000107∗∗∗ 0.000107∗∗∗ 0.000105∗∗∗ 0.000107∗∗∗ (12.85) (12.91) (12.56) (12.67) two-year Journal Impact Factor -0.000263∗∗∗ -0.000267∗∗∗ -0.000266∗∗∗ -0.000269∗∗∗ (-15.42) (-15.63) (-14.92) (-14.89) 2y_cites -0.0000109 -0.0000109 -0.0000121 -0.0000125

(-1.53) (-1.52) (-1.62) (-1.65) Prescience (References) -0.00230∗∗∗

(-21.88) Female Share× Prescience (References) -0.000573∗∗ (-2.95) DummySolo=1 × Prescience (References) -0.00895∗∗∗ (-21.89) DummySolo=1 × Female Share× Prescience (References) -0.00707∗∗∗ (-7.82) Surprise (concepts) -0.0000748 (-1.16) Female Share× Surprise (concepts) -0.0000252 (-0.21) DummySolo=1 × Surprise (concepts) -0.000144 (-0.45) DummySolo=1 × Female Share× Surprise (concepts) -0.00127∗ (-2.01) Prescience (concepts) 0.00149∗∗∗ (17.35) Female Share× Prescience (concepts) -0.000189 (-1.37) DummySolo=1 × Prescience (concepts) -0.000279

- (-0.82)

DummySolo=1 × Female Share× Prescience (concepts) -0.000843

- (-1.24)


Constant -0.00482∗∗∗ -0.00491∗∗∗ -0.00613∗∗∗ -0.00701∗∗∗

(-31.72) (-34.07) (-48.02) (-51.95) Observations 4077371 4077371 4077371 4077371

t statistics in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

###### 68/87

###### K Three-year disruption in solo-authored papers

- Table S36 reports the coefficient estimates of model in eq. (2) of the main file on disruption in solo-authored papers, changing the reference period from five-year (as in the main analysis) to the three- years disruption score – measuring how well papers are able to distance themselves from their literature three-years after publication. We see that the results are in line with the model estimates of the main model in Section C.


- Table S36. Linear regression model estimates for three-years disruption scores of publication on surprise and prescience scores by gender in solo-authored papers, with author-level clustered standard errors. Research field dummies and year of publication are omitted.


(1) (2) (3) (4) 3-years Disruption 3-years Disruption 3-years Disruption 3-years Disruption

Female=1 0.00595∗∗∗ 0.00181∗∗∗ 0.00552∗∗∗ 0.00155∗∗∗

(7.67) (4.41) (7.69) (3.38) Surprise (References) −0.0109∗∗∗

(−21.39)

Female=1 × Surprise (References) −0.00739∗∗∗

(−7.61)

DepartmentSize −4.79e−08∗ −3.09e−08 −3.69e−08 −3.25e−08

(−1.97) (−1.27) (−1.52) (−1.33)

CareerAge 0.0000264∗∗∗ 0.0000429∗∗∗ 0.0000280∗∗∗ 0.0000434∗∗∗

(4.16) (6.66) (4.40) (6.73)

OpenAccess −0.000640∗∗∗ −0.000520∗∗ −0.000612∗∗∗ −0.000527∗∗

(−3.62) (−2.93) (−3.46) (−2.98)

impact_factor_2y −0.000158∗∗∗ −0.0000657∗ −0.000144∗∗∗ −0.0000660∗

(−5.35) (−2.25) (−4.92) (−2.27)

2y_cites −0.0000303∗ −0.0000702∗∗∗ −0.0000351∗ −0.0000717∗∗∗

(−2.04) (−4.71) (−2.38) (−4.79) Surprise (Concepts) 0.000145

(0.43)

Female=1 × Surprise (Concepts) −0.00133∗

(−2.05)

Prescience (References) −0.0104∗∗∗

(−21.91)

Female=1 × Prescience (References) −0.00722∗∗∗

(−7.67)

Prescience (Concepts) 0.00135∗∗∗

(3.69)

Female=1 × Prescience (Concepts) −0.000800

(−1.12)

Constant 0.00377∗∗∗ −0.00233∗∗∗ 0.00362∗∗∗ −0.00296∗∗∗

(5.62) (−3.91) (5.46) (−4.87) Observations 212883 212883 212883 212883

t statistics in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

###### L Five-year Journal Impact Factor in solo-authored papers

We report regression estimates from Eq. (2) in the main text, using the natural logarithm of the five-year journal impact factor as the outcome instead of the two-year measure in Table S37. Results are in line with the model estimates of the main model in Section C.

- Table S37. Linear regression model estimates of log of five-year journal impact factor on solo-authored papers’ surprise score, with author-level clustered standard errors. We control for career age, average number of citations from institution of author in year of publication and in same field of paper (Department Size), publication year with 2020 as baseline year (omitted), open access, and dummy variables for field of publication (omitted).


ln(2-year Journal Impact Factor) ln(5y Impact Factor) Female=1 -0.0685∗∗∗ -0.0592∗∗∗

(-7.31) (-8.98) Surprise (References) 0.0183∗∗

- (3.03)

Female=1 × Surprise (References) 0.0557∗∗∗

- (4.51)


DepartmentSize 0.0000260∗∗∗ 0.0000259∗∗∗ (33.20) (33.27)

CareerAge 0.00211∗∗∗ 0.00208∗∗∗

(19.66) (19.33) OpenAccess 0.138∗∗∗ 0.138∗∗∗ (41.75) (41.67)

Surprise (Concepts) -0.0353∗∗∗ (-6.53)

Female=1 × Surprise (Concepts) 0.0478∗∗∗ (4.86)

Constant 0.962∗∗∗ 0.990∗∗∗

(114.68) (123.02) Observations 212933 212933

t statistics in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

###### M Robustness Check: Returns to Novelty and Prescience Controlling for Grants, andPrior Citations

We re-estimate the baseline regression models on solo-authored papers from the main text, while conditioning on author visibility and prestige, proxied by (i) the number of grants acknowledged in a paper and (ii) authors’ prior citations. Variation in the number of grants or in authors’ past citations does not account for the average gender differences we observe. Estimates of the baseline gender coefficient and of the returns to novelty and prescience remain consistent with those reported in the main model (Section C). This indicates that our results are not solely capturing compositional differences in prestige or status.

- Table S38. Linear regression model estimates for two-step citation score on solo-authored papers in content and context surprise and prescience scores by gender, controlling for number of awarded grants listed in a paper. We compute author-level clustered standard errors. Research field fixed effects and dummies for publishing year are omitted.


(1) (2) (3) (4) TwoStepsCreditScore TwoStepsCreditScore TwoStepsCreditScore TwoStepsCreditScore Female=1 −0.00148 −0.000264 −0.00143∗ −0.00241∗∗

(−1.26) (−0.24) (−2.20) (−3.13) Surprise (References) −0.0120∗∗∗

(−16.70)

Female=1 × Surprise (References) 0.000991

(0.70)

NGrants −0.00199∗∗∗ −0.00208∗∗∗ −0.00227∗∗∗ −0.00230∗∗∗

###### (−4.93) (−5.14) (−5.56) (−5.64)

DepSize −0.00000137∗∗∗ −0.00000138∗∗∗ −0.00000137∗∗∗ −0.00000135∗∗∗

(−18.86) (−19.01) (−18.98) (−18.82)

CareerAge −0.000126∗∗∗ −0.000127∗∗∗ −0.000115∗∗∗ −0.000119∗∗∗

###### (−9.72) (−9.79) (−8.83) (−9.15)

OpenAccess −0.00315∗∗∗ −0.00323∗∗∗ −0.00315∗∗∗ −0.00304∗∗∗

(−9.70) (−9.94) (−9.68) (−9.36) Prescience (References) −0.0113∗∗∗

(−16.83)

Female=1 × Prescience (References) −0.000797

###### (−0.59)

Surprise (Concepts) −0.00179∗∗

###### (−3.25)

Female=1 × Surprise (Concepts) 0.000591

(0.58)

Prescience (Concepts) −0.0105∗∗∗

(−16.59)

Female=1 × Prescience (Concepts) 0.00213

(1.93)

Constant 0.0398∗∗∗ 0.0394∗∗∗ 0.0333∗∗∗ 0.0384∗∗∗

(46.75) (47.92) (47.99) (51.26) Observations 96513 96513 96513 96513

t statistics in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

- Table S39. Linear regression model estimates for five-year disruption score on solo-authored papers in content and context surprise and prescience scores by gender, controlling for number of awarded grants listed in a paper. We computte author-level clustered standard errors. Research field fixed effects and dummies for publishing year are omitted.


(1) (2) (3) (4) 5y Disruption 5y Disruption 5y Disruption 5y Disruption

Female=1 0.00618∗∗∗ 0.00568∗∗∗ 0.00179∗∗∗ 0.00143∗∗

(8.35) (8.31) (4.49) (3.28) Surprise (References) −0.0127∗∗∗

(−25.60)

Female=1 × Surprise (References) −0.00778∗∗∗

###### (−8.41)

NGrants −0.0000322 −0.000220 −0.000646∗∗∗ −0.000647∗∗∗

###### (−0.19) (−1.34) (−4.07) (−4.07)

DepSize −4.84e−08∗ −3.55e−08 −2.76e−08 −2.92e−08

###### (−2.06) (−1.51) (−1.17) (−1.23)

CareerAge 0.0000345∗∗∗ 0.0000364∗∗∗ 0.0000534∗∗∗ 0.0000539∗∗∗

(5.62) (5.92) (8.56) (8.64)

OpenAccess −0.000550∗∗ −0.000504∗∗ −0.000369∗ −0.000376∗

###### (−3.14) (−2.87) (−2.09) (−2.14)

impact_factor_2y −0.000167∗∗∗ −0.000151∗∗∗ −0.0000624∗ −0.0000625∗

###### (−5.86) (−5.33) (−2.22) (−2.23)

2y_cites −0.0000128 −0.0000185 −0.0000580∗∗∗ −0.0000595∗∗∗

(−0.86) (−1.26) (−3.97) (−4.06) Prescience (References) −0.0120∗∗∗

(−26.02)

Female=1 × Prescience (References) −0.00754∗∗∗

###### (−8.43)

Surprise (Concepts) 0.0000902

(0.27)

Female=1 × Surprise (Concepts) −0.00141∗

###### (−2.25)

Prescience (Concepts) 0.00126∗∗∗

(3.51)

Female=1 × Prescience (Concepts) −0.000686

###### (−1.02)

Constant 0.00542∗∗∗ 0.00518∗∗∗ −0.00165∗∗ −0.00226∗∗∗

(8.01) (7.76) (−2.72) (−3.66) Observations 212916 212916 212916 212916

t statistics in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

- Table S40. Linear regression model estimates for log of two-year journal impact factor on solo-authored papers in content and context surprise and prescience scores by gender, controlling for number of awarded grants listed in a paper. We compute author-level clustered standard errors. Research field fixed effects and dummies for publishing year are omitted.


(1) (2) ln(2-year Journal Impact Factor) ln(2-year Journal Impact Factor) Female=1 −0.0665∗∗∗ −0.0659∗∗∗

(−7.25) (−10.20) Surprise (References) 0.00149

(0.25)

Female=1 × Surprise (References) 0.0407∗∗∗

(3.38)

NGrants 0.0317∗∗∗ 0.0325∗∗∗

(10.41) (10.60)

DepSize 0.0000261∗∗∗ 0.0000261∗∗∗

(33.47) (33.52)

CareerAge 0.00226∗∗∗ 0.00225∗∗∗

(21.36) (21.28)

OpenAccess 0.144∗∗∗ 0.144∗∗∗

(44.29) (44.21)

Surprise (Concepts) −0.0304∗∗∗

###### (−5.69)

Female=1 × Surprise (Concepts) 0.0461∗∗∗

(4.76)

Constant 0.914∗∗∗ 0.930∗∗∗

(108.90) (115.19) Observations 212402 212402

t statistics in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

- Table S41. Linear regression model estimates for two-step citation score on solo-authored papers in content and context surprise and prescience scores by gender, controlling for past citations of authors. We compute author-level clustered standard errors. Research field fixed effects and dummies for publishing year are omitted.


(1) (2) (3) (4) TwoStepsCreditScore TwoStepsCreditScore TwoStepsCreditScore TwoStepsCreditScore Female=1 −0.00200 −0.00110 −0.00200∗∗ −0.00264∗∗∗

(−1.70) (−1.00) (−3.07) (−3.43) Surprise (References) −0.0124∗∗∗

(−17.33)

Female=1 −0.00200 −0.00110 −0.00200∗∗ −0.00264∗∗∗

(−1.70) (−1.00) (−3.07) (−3.43) Surprise (References) −0.0124∗∗∗

(−17.33)

Female=1 × Surprise (References) 0.000886

(0.63)

PastCitations −0.000000616∗∗∗ −0.000000621∗∗∗ −0.000000602∗∗∗ −0.000000592∗∗∗

(−16.45) (−16.50) (−16.42) (−16.27)

DepSize −0.00000113∗∗∗ −0.00000113∗∗∗ −0.00000113∗∗∗ −0.00000111∗∗∗

(−15.63) (−15.75) (−15.82) (−15.68)

CareerAge −0.0000599∗∗∗ −0.0000602∗∗∗ −0.0000496∗∗∗ −0.0000545∗∗∗

###### (−4.35) (−4.38) (−3.59) (−3.96)

OpenAccess −0.00293∗∗∗ −0.00302∗∗∗ −0.00296∗∗∗ −0.00285∗∗∗

(−9.05) (−9.31) (−9.10) (−8.81) Prescience (References) −0.0119∗∗∗

(−17.73)

Female=1 × Prescience (References) −0.000440

###### (−0.32)

Surprise (Concepts) −0.00183∗∗∗

###### (−3.33)

Female=1 × Surprise (Concepts) 0.000547

(0.54)

Prescience (Concepts) −0.0101∗∗∗

(−16.01)

Female=1 × Prescience (Concepts) 0.00151

(1.38)

Constant 0.0395∗∗∗ 0.0392∗∗∗ 0.0328∗∗∗ 0.0376∗∗∗

(46.72) (48.04) (47.44) (50.42) Observations 96513 96513 96513 96513

Standard errors in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

- Table S42. Linear regression model estimates for five-year disruption score on solo-authored papers in content and context surprise and prescience scores by gender, controlling for past citations of authors. We compute author-level clustered standard errors. Research field fixed effects and dummies for publishing year are omitted.


(1) (2) (3) (4) 5-year Disruption 5-year Disruption 5-year Disruption 5-year Disruption

Female=1 0.00619∗∗∗ 0.00570∗∗∗ 0.00182∗∗∗ 0.00144∗∗∗

(8.37) (8.33) (4.55) (3.30) Surprise (References) −0.0127∗∗∗

(−25.48)

Female=1 × Surprise (References) −0.00779∗∗∗

###### (−8.42)

PastCitations 1.58e−08 1.50e−08 3.93e−08∗ 3.88e−08∗

(1.01) (0.95) (2.54) (2.51)

DepSize −5.30e−08∗ −4.02e−08 −4.02e−08 −4.16e−08

###### (−2.19) (−1.66) (−1.65) (−1.71)

CareerAge 0.0000330∗∗∗ 0.0000350∗∗∗ 0.0000497∗∗∗ 0.0000502∗∗∗

(5.11) (5.41) (7.56) (7.63)

OpenAccess −0.000559∗∗ −0.000526∗∗ −0.000430∗ −0.000437∗

###### (−3.21) (−3.01) (−2.46) (−2.50)

impact_factor_2y −0.000170∗∗∗ −0.000154∗∗∗ −0.0000688∗ −0.0000688∗

###### (−6.01) (−5.47) (−2.46) (−2.47)

2y_cites −0.0000133 −0.0000192 −0.0000598∗∗∗ −0.0000613∗∗∗

(−0.89) (−1.30) (−4.04) (−4.13) Prescience (References) −0.0120∗∗∗

(−25.87)

Female=1 × Prescience (References) −0.00756∗∗∗

###### (−8.44)

Surprise (Concepts) 0.0000886

(0.27)

Female=1 × Surprise (Concepts) −0.00141∗

###### (−2.26)

Prescience (Concepts) 0.00125∗∗∗

(3.48)

Female=1 × Prescience (Concepts) −0.000659

###### (−0.98)

Constant 0.00544∗∗∗ 0.00521∗∗∗ −0.00156∗∗ −0.00217∗∗∗

(8.07) (7.83) (−2.58) (−3.52) Observations 212916 212916 212916 212916

Standard errors in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

- Table S43. Linear regression model estimates for two-year journal impact factor on solo-authored papers in content and context surprise scores by gender, controlling for past citations of authors. We compute author-level clustered standard errors. Research field fixed effects and dummies for publishing year are omitted.


(1) (2) ln(2-year Journal Impact Factor) ln(2-year Journal Impact Factor) Female=1 −0.0515∗∗∗ −0.0521∗∗∗

(−5.63) (−8.16) Surprise (References) 0.0105

(1.80)

Female=1 × Surprise (References) 0.0364∗∗

(3.03)

PastCitations 0.0000143∗∗∗ 0.0000142∗∗∗

(15.79) (15.82)

DepSize 0.0000215∗∗∗ 0.0000215∗∗∗

(26.36) (26.40)

CareerAge 0.000852∗∗∗ 0.000830∗∗∗

(6.63) (6.45)

OpenAccess 0.139∗∗∗ 0.139∗∗∗

(42.81) (42.74)

Surprise (Concepts) −0.0281∗∗∗

(−5.35)

Female=1 × Surprise (Concepts) 0.0438∗∗∗

(4.57)

Constant 0.921∗∗∗ 0.941∗∗∗

(110.39) (116.88) Observations 212402 212402

Standard errors in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

###### N Global effect of surprise and prescience on rewards by gender

In this section, we report the predicted average rewards by genders when both surprise (prescience) in reference and concepts effects are considered within the same regression model on solo-authored papers:

Scholarly Rewardi = α +βFemalei +γReferenceSurprisei +δConceptsurprisei+ τ(Femalei ×ReferenceSurprisei)+η(Femalei ×Conceptsurprisei)+ ∑δjcontrolsi,j+εi

(7)

Standard errors are clustered at the author level. Figure S24 reports the predicted average rewards by gender estimated from model (7), and show that women’s works tend to have significantly lower journal impact, but higher disruption. Figures S25-S27 show the average marginal effect of reference and concept surprise (prescience) on scholarly rewards by gender: marginal returns in disruption to increasing surprise (or prescience) of sourceare relatively higher for men’s works, while women earn marginall more in journal impact. The results are in line with the baseline models discussed in the main text.

### a b

### c

| | | | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |


Predicted Two-step Citation Score

Predicted Disruption

Predicted Log (JIF)

Men

Women

Surprise Prescience Surprise

Surprise Prescience

- Figure S24. Predicted average rewards in solo-authored papers by gender by author’s gender in solo-authored papers, conditional at mean values of surprise or prescience. We control for career age, department size, year of publication, open access, and level-one fields.

a b

Women

Context (Reference) Combinations Content (Concept) Combinations

Men

Predicted score

Surprise Prescience Surprise Prescience

- Figure S25. Average marginal effect of surprise and prescience on two-step credit score by author’s gender in solo-authored papers. We control for career age, department size, year of publication, open access, and level-one fields.


## a b

###### Context (Reference) Combinations Content (Concept) Combinations

Men

Predicted value

Women

Surprise Prescience Surprise Prescience

- Figure S26. Average marginal effect of surprise and prescience on disruption by author’s gender in solo-authored papers. We control for career age, department size, year of publication, open access, and level-one fields.

a b

Women

Context (Reference) Surprise Content (Concept) Surprise

Men

Predicted value

- Figure S27. Average marginal effect of surprise on the log of journal impact factor by author’s gender in solo-authored papers. We control for career age, department size, year of publication, open access, and level-one fields.


###### O Two-year forward citation count

We extend our analysis to forward citations counts of papers, to evaluate and study gender differences in how additional investments in surprise and prescience generate benefits in terms of direct citations. We consider the two-year citations count – i.e, the total number of citations to a focal paper after two years of publication. Below, we report model estimates on citations counts in solo and multi-authored papers (mixed and gender-homogeneous) relying on a negative binomial regression model for overly dispersed count data.

Among solo-authored papers (Table S44), greater prescience and surprise are associated with higher citation counts, with men’s work performing better on average. Women’s contributions exhibit significantly lower marginal returns to prescience (for both reference- and concept-based measures) and to reference surprise, while there is no significant gender difference in the marginal returns to concept surprise.

In Table S45, which reports results for multi-authored papers, a higher share of women is consistently associated with lower citation outcomes across all measures. However, teams with a higher women’s share earn relatively higher marginal returns to investing in more surprising concept combinations.

- Table S44. Negative binomial regression model estimates for two-year forward citation counts of solo-authored papers in content and context surprise and prescience scores by gender. We include author-level clustered standard errors. Research field fixed effects and dummies for publishing year are omitted.


(1) (2) (3) (4) TwoYearsForwardCitations TwoYearsForwardCitations TwoYearsForwardCitations TwoYearsForwardCitations Female=1 -0.0152 -0.0368 -0.0512∗ 0.0150

(-0.49) (-1.27) (-2.20) (0.61) Surprise (References) 1.319∗∗∗

(69.76) Female=1 × Surprise (References) -0.133∗∗

(-3.23) DepSize 0.0000431∗∗∗ 0.0000432∗∗∗ 0.0000436∗∗∗ 0.0000422∗∗∗ (18.03) (17.39) (17.09) (17.15) CareerAge 0.00836∗∗∗ 0.00825∗∗∗ 0.00686∗∗∗ 0.00702∗∗∗

(23.87) (23.58) (19.81) (20.57) OpenAccess 0.298∗∗∗ 0.304∗∗∗ 0.319∗∗∗ 0.311∗∗∗

(29.19) (29.54) (30.24) (29.65) Prescience (References) 1.162∗∗∗

(62.69) Female=1 × Prescience (References) -0.0973∗ (-2.47)

Surprise (Concepts) 0.335∗∗∗ (19.36)

Female=1 × Surprise (Concepts) -0.0364 (-1.06)

Prescience (Concepts) 0.596∗∗∗ (31.89)

Female=1 × Prescience (Concepts) -0.143∗∗∗ (-3.78)

Constant 0.589∗∗∗ 0.684∗∗∗ 1.225∗∗∗ 1.051∗∗∗

(23.01) (26.54) (44.76) (39.47) Observations 226208 226208 226208 226208 lnalpha 0.271∗∗∗ 0.291∗∗∗ 0.362∗∗∗ 0.352∗∗∗

(41.96) (45.40) (60.91) (59.43)

t statistics in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

- Table S45. Negative binomial regression model estimates for two-year forward citation counts in multi-authored papers in content and context surprise and prescience scores by gender. We include White standard errors. Research field fixed effects and dummies for publishing year are omitted.


(1) (2) (3) (4) TwoYearsForwardCitations TwoYearsForwardCitations TwoYearsForwardCitations TwoYearsForwardCitations Female Share -0.0864∗∗∗ -0.107∗∗∗ -0.160∗∗∗ -0.132∗∗∗

(-5.92) (-7.36) (-16.99) (-11.39) Surprise (References) 0.887∗∗∗

(136.19) Female Share × Surprise (References) -0.0813∗∗∗ (-3.31) DepartmentSize 0.0000214∗∗∗ 0.0000214∗∗∗ 0.0000218∗∗∗ 0.0000206∗∗∗ (40.02) (39.15) (36.88) (33.42) CareerAge 0.00276∗∗∗ 0.00304∗∗∗ 0.00273∗∗∗ 0.00303∗∗∗

(21.28) (23.05) (19.44) (20.95) OpenAccess=1 0.313∗∗∗ 0.334∗∗∗ 0.343∗∗∗ 0.332∗∗∗ (118.48) (123.63) (128.24) (123.65) TeamSize 0.0583∗∗∗ 0.0585∗∗∗ 0.0555∗∗∗ 0.0543∗∗∗

(95.09) (95.03) (88.19) (84.69) TeamSize_squared -0.0000118∗∗∗ -0.0000118∗∗∗ -0.0000119∗∗∗ -0.0000113∗∗∗ (-29.04) (-29.10) (-27.89) (-27.55) num_unknown -0.0230∗∗∗ -0.0230∗∗∗ -0.0199∗∗∗ -0.0204∗∗∗

(-26.46) (-26.15) (-21.63) (-21.83) Prescience (References) 0.756∗∗∗

(128.45) Female Share × Prescience (References) -0.0418

(-1.66)

Surprise (concepts) 0.239∗∗∗ (46.91)

Female Share × Surprise (concepts) 0.0685∗∗ (3.06)

Prescience (concepts) 0.627∗∗∗

(120.77) Female Share × Prescience (concepts) 0.0263

(1.53) Constant 1.299∗∗∗ 1.385∗∗∗ 1.694∗∗∗ 1.441∗∗∗

(160.07) (175.50) (234.89) (188.56) Observations 4085543 4085543 4085543 4085543 lnalpha 0.0566∗∗∗ 0.0600∗∗∗ 0.0884∗∗∗ 0.0685∗∗∗

(23.31) (24.37) (35.89) (26.32)

t statistics in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

###### P GAM model estimates in solo-authored papers

We use a semi-parametric GAM model to examine non-linear associations between surprise or prescience and scholarly rewards by gender of solo-authored papers, while including linear controls and a gender-specific intercept shift. To ease computations in R, we choose to compute non-robust standard errors. Figures S28–S30 show predicted rewards across 0.1 intervals of novelty. Journal impact exhibits a U-shaped pattern for reference surprise among women, while linear approximations capture mid-range novelty for men and extreme novelty for women (Figure S28). Reference surprise and prescience display slight non-linearities for disruption at low values, but linear predictions align with GAM confidence intervals across most of the observed range (Figure S29, row 1). Two-step credit shows similar alignment between linear and GAM predictions (Figure S30), as does disruption from concept-based novelty (Figure S29, row 2).

GAM versus Linear Predictions by Gender with Sample Means

###### a b

1.3

Model

GAM Linear

Female=0

1.3

Journal Impact

1.2

1.2

Female=1

1.1

1.1

0.00 0.25 0.50 0.75 1.00

0.00 0.25 0.50 0.75 1.00

Content (Concept) Surprise

Context (Reference) Surprise

- Figure S28. Average fitted two-year journal impact by gender within 0.1 bins of surprise with GAM models. The models include a gender intercept shift and smooth functions of surprise interacted with gender, while conditioning linearly on all controls. Solid lines report the averaged GAM predictions with 95% confidence intervals shown as shaded bands, dashed lines the corresponding linear regression margins, and points represent the observed sample means within 0.1 bins of the predictors.


GAM versus Linear Predictions by Gender with Sample Means

###### a b

0.03

0.03

Model

GAM Linear

0.02

0.02

Disruption

0.01

0.01

Female=1

0.00

0.00

Female=0

-0.01

-0.01

0.00 0.25 0.50 0.75 1.00 0.00 0.25 0.50 0.75 1.00

###### c d

Context (Reference) Prescience

Context (Reference) Surprise

0.0050

0.0050

0.0025

Disruption

0.0025

0.0000

0.0000

-0.0025

-0.0025

0.00 0.25 0.50 0.75 1.00 0.00 0.25 0.50 0.75 1.00

Content (Concept) Surprise Content (Concept) Prescience

- Figure S29. Average fitted five-year disruption by gender within 0.1 bins of surprise (row 1) and prescience (row 2) with GAM models. The models include a gender intercept shift and smooth functions of surprise or prescience interacted with gender, while conditioning linearly on all controls. Solid lines report the averaged GAM predictions with 95% confidence intervals shown as shaded bands, dashed lines the corresponding linear regression margins, and points represent the observed sample means within 0.1 bins of the predictors.


GAM versus Linear Predictions by Gender with Sample Means

a b

0.050

| | | | | |Mode|l| | | |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | |GAM Linear| | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |


| | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | |Female=|0| | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | |Female=|1| | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |


0.050

0.045

0.045

2-Step Credit

0.040

0.040

0.035

0.035

0.030

0.030

0.00 0.25 0.50 0.75 1.00 0.00 0.25 0.50 0.75 1.00

Context (Reference) Surprise Context (Reference) Prescience

c d

| | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |


| | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |


0.0425

0.050

0.0400

0.045

2-Step Credit

0.0375

0.040

0.0350

0.035

0.030

0.0325

0.025

0.00 0.25 0.50 0.75 1.00 0.00 0.25 0.50 0.75 1.00

Content (Concept) Surprise Content (Concept) Prescience

- Figure S30. Average fitted two-step credit score by gender within 0.1 bins of surprise (row 1) and prescience (row 2) with GAM models. The models include a gender intercept shift and smooth functions of surprise or prescience interacted with gender, while conditioning linearly on all controls. Solid lines report the averaged GAM predictions with 95% confidence intervals shown as shaded bands, dashed lines the corresponding linear regression margins, and points represent the observed sample means within 0.1 bins of the predictors.


###### Q Non-linearity of gender in mixed multi-authored papers

We estimate linear regression models on multi-authored papers, including women’s share (FemaleShare) and its square (FemaleShare2), and a dummy for gender-homogeneous teams (GenderHomogeneousTeams, coded one for all-women, zero for all-men teams with high-confidence gender identification). To capture team-specific effects, we interact the dummy with female share (GenderHomogeneousTeam × FemaleShare). The dummy is largely collinear with the squared female share because mixed-team values are pushed toward the extremes.

Table S46 shows that gender differences in surprise and prescience of source combinations (columns 1–2) primarily occur in gender-homogeneous teams (GenderHomogeneousTeam × FemaleShare). For concept-based innovations, the relationship with female share is non-linear. Concept surprise is concave, with diminishing marginal effects at higher female shares (FemaleShare2 < 0), while prescience is convex: the negative effect at low female share diminishes as the share increases (FemaleShare2 > 0).

Next, Table S47 reports two-step credit scores. For reference combinations (columns 1-2), higher female share (FemaleShare) is associated with increased downstream citations in mixed-gender teams, but lower values in gender-homogeneous teams (GenderHomogeneousTeam × FemaleShare). For concept combinations (columns 3-4), increasing female share corresponds to lower two-step credit, particularly in all-women teams. Non-linear terms suggest that the relationship between female share and novelty is not strictly linear and varies across the range of female representation.

Turning to disruption (Table S48), higher women’s presence is associated with greater disruption for source-based novelty primarily in mixed-gender teams (FemaleShare). For concept-based novelty, increased disruption is concentrated in all-women teams GenderHomogeneousTeam × FemaleShare, while the squared terms for female share are not significant, indicating no clear non-linear effects. These results suggest that the contribution of women to disruptive science is linear in team composition.

Finally, Table S49 shows patterns in journal placement. All-women teams exhibit a steeper increase in journal impact with rising concept surprise compared to all-men teams (GenderHomogeneousTeam × FemaleShare × Surprise), consistent with the solo-authored results in the main text. Non-linear effects of female share are generally modest, suggesting that the three-way interactions with gender-homogeneous teams and surprise primarily drive the observed journal placement patterns.

- Table S46. Linear regression model estimates for gender differences on content and context surprise and prescience scores, on multi-authored papers. We include White standard errors. Research field fixed effects and dummies for publishing year are omitted.


(1) (2) (3) (4) Surprise (References) Prescience (References) Surprise (concepts) Prescience (concepts) GenderHomogeneousTeam=1 -0.00794∗∗∗ -0.00122 0.000134 -0.0140∗∗∗

(-6.40) (-0.90) (0.09) (-9.48) Female Share 0.00335 -0.000637 0.000752 -0.0678∗∗∗ (0.62) (-0.11) (0.12) (-10.99) GenderHomogeneousTeam=1 × Female Share 0.00696∗∗∗ 0.00362∗∗ 0.00791∗∗∗ 0.0105∗∗∗ (5.48) (2.66) (5.41) (7.64) Female Share_square 0.00994 0.0120 -0.0144∗ 0.0498∗∗∗ (1.73) (1.93) (-2.17) (7.65) DepSize 0.00000154∗∗∗ 0.00000117∗∗∗ 0.000000395∗∗∗ 0.00000196∗∗∗ (52.75) (37.00) (11.94) (61.91) CareerAge -0.000158∗∗∗ -0.000550∗∗∗ -0.000153∗∗∗ -0.000469∗∗∗ (-14.05) (-46.14) (-12.39) (-40.06) num_authors 0.00112∗∗∗ 0.000925∗∗∗ 0.00101∗∗∗ 0.00262∗∗∗ (17.93) (14.40) (15.00) (26.33) num_authors_squared -0.000000431∗∗∗ -0.000000368∗∗∗ -0.000000160∗∗∗ -0.000000419∗∗∗ (-32.49) (-28.24) (-15.80) (-27.95) num_unknown -0.0000126 -0.00000114 -0.000581∗∗∗ -0.00151∗∗∗

(-0.17) (-0.02) (-7.81) (-13.62) Constant 0.550∗∗∗ 0.541∗∗∗ 0.523∗∗∗ 0.592∗∗∗ (350.75) (321.46) (293.83) (324.31) Observations 4085543 4085543 4085543 4085543

t statistics in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

- Table S47. Linear regression model estimates for 2-steps-out credit score for surprise and prescience scores in multi-authored papers. We include White standard errors. Research field fixed effects and dummies for publishing year are omitted.


(1) (2) (3) (4) TwoStepsCreditScore TwoStepsCreditScore TwoStepsCreditScore TwoStepsCreditScore GenderHomogeneousTeam=1 0.00566∗∗∗ 0.00627∗∗∗ -0.00118∗ -0.000844

(7.99) (11.64) (-2.40) (-1.41) Female Share 0.00888∗∗ 0.00973∗∗∗ -0.0104∗∗∗ -0.0132∗∗∗ (2.66) (3.82) (-4.56) (-4.69) GenderHomogeneousTeam=1 × Female Share -0.00425∗∗∗ -0.00517∗∗∗ -0.00307∗∗∗ -0.00508∗∗∗

(-4.78) (-7.60) (-5.26) (-7.10) Surprise (References) -0.00571∗∗∗

(-6.33) GenderHomogeneousTeam=1 × Surprise (References) -0.00936∗∗∗ (-10.24) Female Share × Surprise (References) -0.0241∗∗∗ (-5.57) GenderHomogeneousTeam=1 × Female Share × Surprise (References) 0.00223 (1.95) Female Share_square -0.00515 -0.00503 0.0132∗∗∗ 0.0175∗∗∗

(-1.39) (-1.77) (5.21) (5.63) Female Share_square × Surprise (References) 0.0225∗∗∗

(4.71) Prescience (References) -0.00174∗ (-2.37) GenderHomogeneousTeam=1 × Prescience (References) -0.0114∗∗∗ (-15.28) Female Share × Prescience (References) -0.0286∗∗∗ (-8.06) GenderHomogeneousTeam=1 × Female Share × Prescience (References) 0.00395∗∗∗ (4.21) Female Share_square × Prescience (References) 0.0251∗∗∗ (6.37) Surprise (concepts) -0.00358∗∗∗ (-5.21) GenderHomogeneousTeam=1 × Surprise (concepts) 0.000828 (1.19) Female Share × Surprise (concepts) 0.00469 (1.42) GenderHomogeneousTeam=1 × Female Share × Surprise (concepts) 0.000277 (0.32) Female Share_square × Surprise (concepts) -0.00508 (-1.39) Prescience (concepts) -0.0125∗∗∗ (-16.24) GenderHomogeneousTeam=1 × Prescience (concepts) -0.0000244 (-0.03) Female Share × Prescience (concepts) 0.00752∗

- (2.03)

GenderHomogeneousTeam=1 × Female Share × Prescience (concepts) 0.00359∗∗∗

- (3.69)


Female Share_square × Prescience (concepts) -0.0107∗∗ (-2.58)

DepSize -0.000000419∗∗∗ -0.000000424∗∗∗ -0.000000424∗∗∗ -0.000000405∗∗∗ (-53.51) (-54.13) (-54.19) (-52.05)

CareerAge -0.0000140∗∗∗ -0.0000176∗∗∗ -0.0000116∗∗∗ -0.0000172∗∗∗ (-6.61) (-8.29) (-5.47) (-8.13)

OpenAccess=1 -0.00242∗∗∗ -0.00279∗∗∗ -0.00287∗∗∗ -0.00269∗∗∗ (-48.14) (-55.63) (-56.78) (-53.65)

num_authors -0.000266∗∗∗ -0.000261∗∗∗ -0.000249∗∗∗ -0.000228∗∗∗ (-17.10) (-16.95) (-16.81) (-16.15)

num_authors_squared 1.77e-08∗∗∗ 1.86e-08∗∗∗ 1.94e-08∗∗∗ 1.63e-08∗∗∗

- (11.81) (12.35) (12.92) (11.17)

num_unknown 0.000216∗∗∗ 0.000208∗∗∗ 0.000194∗∗∗ 0.000182∗∗∗

- (12.92) (12.60) (12.20) (11.99)


Constant 0.0305∗∗∗ 0.0286∗∗∗ 0.0300∗∗∗ 0.0356∗∗∗ (42.87) (52.27) (59.57) (58.96)

###### 85/87

Observations 2451029 2451029 2451029 2451029

t statistics in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

###### Table S48. Linear regression model estimates for disruption score of publication on surprise and prescience scores by genderin multi-authored papers, with White standard errors. Research field fixed effects and dummies for publishing year are omitted.

(1) (2) (3) (4) 5-year Disruption 5-year Disruption 5-year Disruption 5-year Disruption

GenderHomogeneousTeam=1 0.00350∗∗∗ 0.00223∗∗∗ 0.00000510 0.0000722

(6.03) (5.38) (0.02) (0.23)

Female Share 0.00732∗∗ 0.00423∗ 0.00123 0.00136

(2.78) (2.23) (1.09) (0.99)

GenderHomogeneousTeam=1 × Female Share −0.0000199 0.0000890 0.000721∗∗ 0.000769∗

(−0.03) (0.19) (2.76) (2.51) Surprise (References) 0.000807

(1.08)

GenderHomogeneousTeam=1 × Surprise (References) −0.00426∗∗∗

###### (−5.62)

Female Share × Surprise (References) −0.00654

###### (−1.90)

GenderHomogeneousTeam=1 × Female Share × Surprise (References) 0.000270

(0.32)

Female Share_square −0.00514 −0.00271 −0.00149 −0.00149

(−1.83) (−1.32) (−1.26) (−1.04) Female Share_square × Surprise (References) 0.00383

(1.04)

Prescience (References) −0.000432

###### (−0.77)

GenderHomogeneousTeam=1 × Prescience (References) −0.00251∗∗∗

###### (−4.41)

Female Share × Prescience (References) −0.00179

###### (−0.69)

GenderHomogeneousTeam=1 × Female Share × Prescience (References) 0.000112

(0.17)

Female Share_square × Prescience (References) −0.000144

###### (−0.05)

Surprise (concepts) −0.00135∗∗∗

###### (−3.61)

GenderHomogeneousTeam=1 × Surprise (concepts) 0.00141∗∗∗

(3.73)

Female Share × Surprise (concepts) 0.00369∗

(2.19)

GenderHomogeneousTeam=1 × Female Share × Surprise (concepts) −0.00115∗∗

###### (−2.91)

Female Share_square × Surprise (concepts) −0.00255

###### (−1.43)

Prescience (concepts) 0.000368

(0.85)

GenderHomogeneousTeam=1 × Prescience (concepts) 0.00123∗∗

(2.87)

Female Share × Prescience (concepts) 0.00333

(1.75)

GenderHomogeneousTeam=1 × Female Share × Prescience (concepts) −0.00118∗∗

###### (−2.68)

Female Share_square × Prescience (concepts) −0.00245

###### (−1.23)

DepSize −1.93e−08∗∗∗ −2.00e−08∗∗∗ −2.23e−08∗∗∗ −2.45e−08∗∗∗

###### (−6.90) (−7.16) (−7.91) (−8.75)

CareerAge −0.00000617∗∗∗ −0.00000714∗∗∗ −0.00000565∗∗∗ −0.00000494∗∗∗

###### (−5.46) (−6.31) (−5.00) (−4.36)

OpenAccess=1 −0.000562∗∗∗ −0.000611∗∗∗ −0.000653∗∗∗ −0.000682∗∗∗

(−19.23) (−20.80) (−21.96) (−23.09)

num_authors −0.000109∗∗∗ −0.000107∗∗∗ −0.000105∗∗∗ −0.000108∗∗∗

###### (−10.04) (−9.94) (−9.69) (−9.87)

num_authors_squared 9.76e−09∗∗∗ 9.98e−09∗∗∗ 1.06e−08∗∗∗ 1.11e−08∗∗∗

(7.33) (7.50) (7.81) (8.13)

num_unknown 0.0000863∗∗∗ 0.0000842∗∗∗ 0.0000806∗∗∗ 0.0000818∗∗∗

(8.53) (8.34) (7.99) (8.06)

impact_factor_2y −0.000269∗∗∗ −0.000273∗∗∗ −0.000276∗∗∗ −0.000279∗∗∗

(−15.20) (−15.43) (−15.12) (−15.10)

2y_cites −0.0000107 −0.0000106 −0.0000114 −0.0000118

###### (−1.50) (−1.49) (−1.55) (−1.58)

Constant −0.00794∗∗∗ −0.00699∗∗∗ −0.00639∗∗∗ −0.00732∗∗∗

(−13.55) (−16.24) (−22.27) (−21.34) Observations 3864455 3864455 3864455 3864455

t statistics in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

###### Table S49. Linear regression model estimates for log of journal impact factor on surprise on multi-authored papers, withWhite standard errors. Research field fixed effects and dummies for publishing year are omitted.

(1) (2) (3) (4)

ln(2-year Journal Impact Factor) ln(2-year Journal Impact Factor) ln(5y Impact Factor) ln(5y Impact Factor) GenderHomogeneousTeam=1 -0.0182∗ -0.0152∗ -0.0171∗ -0.0160∗

(-2.27) (-2.17) (-2.13) (-2.27) Female Share 0.00549 0.000454 0.00680 -0.00108 (0.17) (0.02) (0.20) (-0.04) GenderHomogeneousTeam=1 × Female Share 0.0447∗∗∗ 0.0801∗∗∗ 0.0441∗∗∗ 0.0733∗∗∗

(6.39) (14.56) (6.32) (13.32) Surprise (References) 0.281∗∗∗ 0.303∗∗∗

(29.58) (31.71) GenderHomogeneousTeam=1 × Surprise (References) -0.0363∗∗∗ -0.0413∗∗∗ (-3.78) (-4.28) Female Share × Surprise (References) -0.142∗∗ -0.161∗∗∗ (-3.28) (-3.72) GenderHomogeneousTeam=1 × Female Share × Surprise (References) 0.0782∗∗∗ 0.0682∗∗∗

(7.92) (6.92) Female Share_square × Surprise (References) 0.0347 0.0694 (0.76) (1.53)

DepSize 0.0000118∗∗∗ 0.0000120∗∗∗ 0.0000120∗∗∗ 0.0000123∗∗∗ (167.38) (170.28) (171.76) (174.79)

CareerAge 0.00102∗∗∗ 0.000962∗∗∗ 0.00106∗∗∗ 0.00100∗∗∗

(44.82) (41.94) (46.36) (43.23) OpenAccess=1 0.184∗∗∗ 0.193∗∗∗ 0.177∗∗∗ 0.187∗∗∗ (309.22) (323.28) (296.51) (311.53) num_authors 0.0163∗∗∗ 0.0164∗∗∗ 0.0167∗∗∗ 0.0167∗∗∗

(28.68) (28.79) (28.65) (28.77) num_authors_squared -0.00000158∗∗∗ -0.00000166∗∗∗ -0.00000152∗∗∗ -0.00000161∗∗∗ (-31.08) (-31.58) (-30.92) (-31.48) num_unknown -0.0122∗∗∗ -0.0120∗∗∗ -0.0127∗∗∗ -0.0126∗∗∗ (-20.06) (-19.77) (-20.55) (-20.24) Surprise (concepts) 0.0943∗∗∗ 0.0973∗∗∗ (11.14) (11.45) GenderHomogeneousTeam=1 × Surprise (concepts) -0.0486∗∗∗ -0.0509∗∗∗ (-5.68) (-5.92) Female Share × Surprise (concepts) -0.150∗∗∗ -0.167∗∗∗ (-3.92) (-4.34) GenderHomogeneousTeam=1 × Female Share × Surprise (concepts) 0.0299∗∗∗ 0.0293∗∗∗ (3.46) (3.39) Female Share_square × Surprise (concepts) 0.125∗∗ 0.139∗∗∗ (3.11) (3.45)

Constant 0.983∗∗∗ 1.090∗∗∗ 1.018∗∗∗ 1.135∗∗∗ (112.74) (139.34) (115.59) (143.27)

Observations 3861357 3861357 3864495 3864495

t statistics in parentheses ∗ p < 0.05, ∗∗ p < 0.01, ∗∗∗ p < 0.001

