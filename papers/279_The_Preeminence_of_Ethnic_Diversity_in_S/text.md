ARTICLE

DOI: 10.1038/s41467-018-07634-8 OPEN

## The preeminence of ethnic diversity in scientiﬁc collaboration

Bedoor K. AlShebli 1, Talal Rahwan1,2 & Wei Lee Woon 1,3

1234567890():,;

Inspired by the social and economic beneﬁts of diversity, we analyze over 9 million papers and 6 million scientists to study the relationship between research impact and ﬁve classes of diversity: ethnicity, discipline, gender, afﬁliation, and academic age. Using randomized baseline models, we establish the presence of homophily in ethnicity, gender and afﬁliation. We then study the effect of diversity on scientiﬁc impact, as reﬂected in citations. Remarkably, of the classes considered, ethnic diversity had the strongest correlation with scientiﬁc impact. To further isolate the effects of ethnic diversity, we used randomized baseline models and again found a clear link between diversity and impact. To further support these ﬁndings, we use coarsened exact matching to compare the scientiﬁc impact of ethnically diverse papers and scientists with closely-matched control groups. Here, we ﬁnd that ethnic diversity resulted in an impact gain of 10.63% for papers, and 47.67% for scientists.

1Department of Computer Science, Masdar Institute, Khalifa University of Science and Technology, Abu Dhabi, P.O. Box 54224, UAE. 2Computer Science, New York University, Abu Dhabi, P.O. Box 129188, UAE. 3Expedia Inc., 333 108th AVE NE, Bellevue, WA 98004, USA. Correspondence and requests for materials should be addressed to B.K.A. (email: bedoor@deeplearn.net) or to T.R. (email: talal.rahwan@nyu.edu) or to W.L.W. (email: wlwoon@deeplearn.net)

# D

iversity is highly valued in modern societies1–6. Social cohesion, tolerance, and integration are linked to tangible beneﬁts including economic vibrancy7,8 and

innovativeness5,9–11. Far from being an abstract ideal, this conviction has guided many governmental and hiring policies and can have broad and long-lasting effects on society12,13. However, diversity is a complex issue, as groups can be diverse in terms of various attributes, such as ethnicity, gender, age, and socioeconomic background. It is also unclear if all forms of diversity are beneﬁcial. For instance, ethnic density has been associated with positive outcomes in terms of health14,15, while ethnic polarization has a negative effect on economic development16. Furthermore, diversity can be a divisive topic that is clouded by emotion, partisan loyalties, and political correctness, all of which can hinder impartial discussions17. The factors above strongly motivate an objective study on the value of diversity, and on whether more diverse groups achieve greater success.

One domain in which this question can be effectively addressed is academia18,19. The structure of academic collaboration is observable via co-authorships, which frequently involve scientists from different locations, disciplines and backgrounds20,21. Furthermore, academic output has an objective, widely accepted measure—citation count22,23. This amenability to analysis has already attracted attempts at identifying the factors which underlie success in academia, an enterprise known as the Science of Science24. Although many such factors have been studied, including gender25, academic age26, team size27, interdisciplinarity28, ethnicity29, and afﬁliation30,31, the study of these factors is extremely complex and many questions remain unanswered.

Our study seeks to address this shortcoming from a number of hitherto unexplored perspectives. Firstly, we compare homophily in scientiﬁc collaborations from the perspectives of age, gender, afﬁliation, and ethnicity. We ﬁnd clear signs of homophily in the cases of ethnicity, gender, and afﬁliation. However, in only one case, ethnicity, was homophily was found to be increasing steadily over time. Secondly, we examine the relationship between various classes of diversity and research impact at the level of scientiﬁc ﬁelds. Remarkably, we found that ethnic diversity is most strongly associated with scientiﬁc impact. Thirdly, we compare the beneﬁts of diversity on groups vs. individuals, and ﬁnd that the former outweighs the latter. Finally, we study the evolution and effect of diversity over time, team size, and number of collaborators, and verify that the above ﬁndings persist across all of these dimensions. The results of these multiple angles of analysis are combined to form a far richer picture of diversity than has been possible in the past.

Results

Exploring homophily. A natural starting point for our study of diversity is to establish the extent to which homophily32 exists in academia—i.e., whether scientists tend to collaborate more frequently with similar others—which would lead to an overall lack of diversity in scientiﬁc collaborations. We use the Microsoft Academic Graph dataset (available at: https://www. microsoft.com/en-us/research/project/microsoft-academic-graph/ ), and analyze 1,045,401 multi-authored papers (see Supplementary Figure 1 for the distribution of papers by year), written by 1,529,279 scientists, spanning eight main ﬁelds and 24 subﬁelds of science. We analyzed diversity in terms of these ﬁve attributes: ethnicity (eth), discipline (dsp), gender (gen), afﬁliation (aff), and academic age (age); see Supplementary Note 1. Here, the abbreviations in parentheses are used in subsequent mathematical expressions to indicate the associated attribute. These attributes reﬂect many technical and social factors that

inﬂuence teamwork and collaboration. Afﬁliation indicates the geographic location, and may even reﬂect the way collaborative work is carried out—from the style and culture of collaboration to its mundane details, such as the medium used to collaborate, e.g., face-to-face interactions vs. telecommunication or email. Academic age is not only indicative of the amount of experience that a scientist has, but is also typically associated with actual age. Discipline may reﬂect a scientist’s substantive knowledge and his/ her acquired skills through training, as well as the culture in which collaborative work is carried out. Finally, ethnicity and gender may play a role in shaping scientists’ social identities, knowledge, and biases. To quantify diversity in terms of any of the aforementioned attributes, we use the Gini Impurity33, resulting in the following group diversity indices, dethG , dageG , dgenG , ddspG and daffG (an alternative diversity measure was also considered; see Supplementary Note 2 and Supplementary Figure 2).

To explore homophily, we generate different randomized baseline models whereby a particular attribute—be it ethnicity, gender, afﬁliation, or academic age—is shufﬂed. For example, in the case of ethnicity, this process is akin to creating a universe in which ethnicity is disregarded in the selection of co-authors, while retaining other criteria. To preserve the conditional distributions of the ethnicities, the shufﬂing process is constrained to only occur between authors of papers that have the same subﬁeld, publication year, and number of authors; for full details, see Supplementary Note 3. This way, for every paper p in the real dataset, there exists a matching paper p′ in the randomized dataset that may differ from p in terms of ethnic diversity, but is identical to p in terms of gender, afﬁliation, academic age, citations, publication year, and number of authors per paper. Importantly, while such a baseline model may produce homogeneous groups, the emergence of such groups is purely the result of random chance rather than homophily. As such, by comparing the real dataset with this baseline model, we can determine whether homophily exists, and if so, quantify the degree to which it is spread across academia. Figure 1a compares our real dataset with the randomized baseline model in terms of the cumulative distributions of dxG : x 2 feth;age;gen;affg. As can be seen, for x ∈ {eth, gen, aff}, groups with low dxG are more common in reality than would be expected by random chance, highlighting the fact that homophily does indeed exist in academia in terms of ethnicity, gender, and afﬁliation. However, for x = age, the opposite was observed (see Supplementary Figures 3–6 for subﬁeld-speciﬁc distributions). These observations persist, regardless of the publication year (Fig. 1b), and the number of authors per paper (Fig. 1c). The temporal trends observed in Fig. 1b are particularly intriguing. For dethG , while the population of scientists is becoming more ethnically diverse (see the steady increase in the red line), this trend is not reﬂected in the actual coauthor groupings, implying that ethnic homophily is steadily increasing. For dageG , the actual level of diversity is greater than would be expected by random chance; this pattern is regularly observed in academia, e.g., consider the many publications resulting from advisor–advisee collaborations. For dgenG , although gender homophily continues to exist, it steadily decreases over time, suggesting that women are playing an ever greater role in scientiﬁc endeavors. Finally, for daffG , there is a marked decrease in afﬁliation homophily around the 1990s; this is consistent with the jump in multi-university collaborations in the 1990s due to the widespread of the Internet and other technologies that facilitate collaboration across geographically distant scientists30.

The link between diversity and scientiﬁc impact. Having explored homophily in academia, we now study the effects of

- a
- b
- c


1.0 0.8 0.6

1.0 0.8 0.6

1.0 0.8 0.6

1.0 0.8 0.6

| | |
|---|---|
| | |


GCumulativeP(d)age

GCumulativeP(d)gen

GCumulativeP(d)eth

GCumulativeP(d)aff

0.4 0.2 0.0

0.4 0.2 0.0

0.4 0.2 0.0

0.4 0.2 0.0

0.2 0.4 Group ethnic diversity index, dGeth 0.6 0.8

0.0

0.0 0.1 0.2 0.3 0.4

0.6 0.8 0.0 0.2 0.4 0.6 0.8

0.0 0.2 0.4 Group age diversity index, dGage Group gender diversity index, dGgen Group affiliation diversity index, dGaff

0.6

0.6

0.6

0.6

0.4

0.4

0.4

0.4

G〉〈dege

G〉〈dgen

G〉〈daff

G〈〉deth

0.2

0.2

0.2

0.2

0.0 1960 1980 2000

0.0

0.0 1960 1980 2000

0.0 1960 1980 2000

1960 1980 2000 Year of publication

Year of publication

Year of publication

Year of publication

0.8

0.8

0.8

0.8

0.6

0.6

0.6

0.6

G〉〈dege

G〉〈dgen

G〉〈daff

G〈〉deth

0.4

0.4

0.4

0.4

0.2 2 3 4 5 6 7 8 9 10 No. authors/paper

0.2

0.2

0.2

2 3 4 5 6 7 8 9 10 No. authors/paper

2 3 4 5 6 7 8 9 10 No. authors/paper

2 3 4 5 6 7 8 9 10 No. authors/paper

|Real data Randomized|
|---|


Fig. 1 Exploring homophily in real vs. randomized data. Each column corresponds to a different class of diversity, and each row presents the results of

- a speciﬁc set of experiments whereby dGx : x 2 feth;age; gen; affg in real data is compared against randomized data. a Cumulative distributions of dGx .
- b Change in mean diversity hdGx i over time. c Mean diversity hdGx i for papers with different number of authors


homophily (and diversity) on research impact, measured by the number of citations received within 5 years of publication, denoted by cG5 (see Supplementary Note 4 and Supplementary Figure 7). Using the same dataset and notation described earlier, we study the relationship between a subﬁeld’s diversity and its academic impact. Here, we distinguish between two notions of diversity. The ﬁrst is where the unit of analysis is a paper’s set of authors, while the second is where the unit of analysis is an individual scientist’s entire set of collaborators. We refer to the former as group diversity, and to the latter as individual diversity; see Fig. 2 for an illustration comparing the two notions.

For each subﬁeld, Fig. 3a depicts the mean group diversity indices, hdxGi : x 2 feth;age;gen;dsp;affg, against the mean 5year citation count, hcG5 i, taken over papers in that subﬁeld (notation summary and formal deﬁnitions are in Supplementary Table 1 and Supplementary Note 2, respectively). Remarkably, we ﬁnd that a subﬁeld’s ethnic diversity is the most strongly correlated with impact (r = 0.77); the positive correlation persists even when the subﬁelds are studied in isolation (Supplementary Figures 8 and Supplementary Table 2), regardless of the number of authors per paper (Supplementary Figure 9). These ﬁndings are further supported by the regression analysis in Table 1. While these ﬁndings do not imply causation, it is still suggestive that one can largely predict scientiﬁc impact based solely on average ethnic diversity, especially given that ethnicity is arguably unrelated to technical competence.

Having studied group diversity, we now move our attention to individual diversity. Here, we analyze scientists with at least 10 collaborators each, amounting to a total of 5,103,877 collaborators over 9,472,439 papers (see Supplementary Table 3 for a

A paper with high dxG A paper with low dxG

A B

A scientist with high dxI A scientist with low dxI

C D

Fig. 2 Group vs. individual diversity. For any given class of diversity, x ∈

{eth, age, gen, dsp, aff}, differences in color represent differences in terms of x. The group diversity index dGx of Paper A is higher than that of Paper B. The individual diversity index of Scientist C is higher than that of Scientist D

##### a Group diversity indices against impact

60

60

60

| |r = 0.77, p = 1.01e–5| | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


| |r = 0.65, p = 4.23e–4| | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |


| |r = 0.45, p = 0.02| | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


50

50

40

40

〉〈Gc5

50

〉〈〉〈GGcc55

30

30

20

20

10

10

40

0

0

0.2 0.3 0.4 0.5 0.6

0.05 0.10 0.15 0.20 0.25 0.30

〈〉Gc5

G age〉 Mean group gender diversity, 〈d

G gen〉

Mean group age diversity, 〈d

30

60

60

| |r = 0.41, p = 0.046| | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |


| |r = 0.28, p = 0.19| | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |


20

50

50

40

40

〈〉〉〈GIcc55

30

30

10

20

20

10

10

0

0

0

0.25 0.30 0.35 0.40 0.45 0.50 0.55 0.60

0.1 0.2 0.3 0.4 0.5 0.6 0.7

0.50 0.55 0.60 0.65 0.70 0.75 0.80

G eth〉 Mean group discipline diversity, 〈d

G dsp〉 Mean group affiliation diversity, 〈d

G aff〉

Mean group ethnic diversity, 〈d

##### b Individual diversity indices against impact

60

60

60

| |r = 0.55, p = 0.005| | | | | | | |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |


| |r = 0.48, p = 0.017| | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


| |r = 0.43, p = 0.03| | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |


50

50

40

40

50

〉〈〉〈IIcc55

30

30

20

20

10

10

40

0

0

0.50 0.55 0.60 0.65 0.70 0.75

0.15 0.20 0.25 0.30 0.35 0.40 0.45

Mean individual age diversity, 〈d

I age〉 Mean individual gender diversity, 〈d

I gen〉

〈〉Ic5

30

60

60

| |r = 0.18, p = 0.39| | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |


| |r = 0.17, p = 0.41| | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


20

50

50

40

40

〉〈Ic5

30

30

10

20

20

10

10

0

0

0

0.2 0.3 0.4 0.5 0.6 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9

0.30 0.35 0.40 0.45 0.50 0.55 0.60 0.65 0.70

###### Mean group affiliation diversity, 〈d

I aff〉

###### Mean individual discipline diversity, 〈d

I dsp〉

Mean individual ethnicity diversity, 〈d

I eth〉

Eng & Comp Sci Health & Med Sci

Bus, Econ & Mgmnt Hum, Lit & Arts

Physics & Math Social Sci

Chem & Mat Sci Earth Sci & Life Sci

- Fig. 3 Group and individual diversity vs. impact in each subﬁeld. In each subplot, the points correspond to subﬁelds, the color indicates the main ﬁeld, while the solid line and the shaded area represent the regression line and the 95% conﬁdence interval, respectively. Each regression has also been annotated


with the corresponding Pearson’s r and p values. a For each subﬁeld, the subplots depict the mean group diversity indices, hdGethi, hdGagei, hdGgeni, hdGdspi and hdGaffi, against the mean 5-year citation count, hcG5 i, taken over papers in that subﬁeld. b For each subﬁeld, the subplots depict the mean individual diversity indices, hdIethi, hdIagei, hdIgeni, hdIdspi and hdIaffi, against the mean 5-year citation count, hcI5i, taken over scientists in that subﬁeld

summary of all ﬁlters applied on the dataset). For each subﬁeld, Fig. 3b depicts the mean individual diversity indices, hdxIi : x 2 feth;age;gen;dsp;affg, against the mean 5-year citation count, hcI5i, taken over scientists in that subﬁeld. As can be seen, a subﬁeld’s ethnic diversity is again the most strongly correlated with impact (r = 0.55), even when the subﬁelds are studied in isolation (Supplementary Figure 10 and Supplementary Table 4).

The above results highlight a potential dysfunction. While homophily was observed for ethnicity, afﬁliation and gender, the only attribute for which it was found to be increasing over time was ethnicity, which seems strange given the apparent preeminence of ethnic diversity. Motivated by this observation, we further explore the relationship between ethnic diversity and scientiﬁc impact in the randomized universe used earlier in Fig. 1. Recall that, in such a universe, ethnicity is excluded as a criterion for selecting co-authors while the other factors are preserved. Hence, it stands to reason that any differences in impact between the randomized and real datasets can be attributed to ethnic diversity. To examine these differences, we partitioned the papers

into two categories, labeled as diverse dethG >d~ethG and nondiverse dethG d~ethG , where the tilde denotes the median. The scientists were similarly partitioned into diverse dethI >d~ethI and non-diverse dethI d~ethI . We ﬁnd that the diverse consistently outperforms the non-diverse, regardless of the year of publication (Fig. 4e), the number of authors per paper (Fig. 4g), and the number of collaborators per scientist (Fig. 4i). We replicated these plots using the randomized, instead of the real, dataset (Fig. 4f, h and j). As can be seen, the performance gap between the diverse and non-diverse almost entirely disappears in the randomized dataset, suggesting that the observed impact gains in the real dataset could indeed be attributed to ethnic diversity. Note that, in the real dataset, a large proportion of papers have dethG ¼ 0 (see Fig. 4a), and a large proportion of scientists have dethI ¼ 0 (see Fig. 4c). As such, the observed performance gap between the diverse and the non-diverse could be predominantly due to these papers and scientists being less impactful than their counterparts

|Table 1 Regression analyses of diversity classes on academic impact<br><br>Citation count, cG5 Engineering & computer science<br><br>Health & medical sciences<br><br>Business, economics & management<br><br>Humanities, literature & arts<br><br>Physics & mathematics<br><br>Social sciences<br><br>Chemical & material sciences<br><br>Life sciences & earth sciences<br><br>(A) Group ethnic diversity<br><br>dGeth 7.40*** 3.00*** 5.21*** 4.77*** 8.04** 4.39** 4.29** 3.94*** (2.44) (0.64) (1.64) (1.79) (3.30) (1.89) (1.95) (1.45)<br><br>University ranking −1.22*** −1.08*** −0.60** −0.52** −0.16 −0.55* −0.35 −1.35***<br><br>(0.39) (0.08) (0.24) (0.26) (0.46) (0.29) (0.29) (0.23) Author’s prior impact 0.62*** 1.24*** 1.52*** 1.61*** 0.72*** 1.51*** 1.60*** 1.53***<br><br>(0.01) (0.01) (0.01) (0.01) (0.02) (0.01) (0.01) (0.01) Year of publication 0.20 0.24*** 0.07 0.48*** 0.13 0.37** 0.24 0.24*** (0.21) (0.01) (0.10) (0.10) (0.16) (0.17) (0.17) (0.01) Number of authors 0.00 0.59*** 0.23 0.27 1.06 0.46** 0.51*** 0.69*** (0.27) (0.15) (0.17) (0.18) (1.03) (0.19) (0.19) (0.11) Const 2221.02*** 598.55*** 1081.71*** 1085.84*** 1289.91*** 2142.17*** 1813.42*** 2750.75***<br><br>(270.36) (22.94) (114.27) (124.13) (230.16) (194.14) (188.89) (144.35) R2 0.11 0.24 0.33 0.35 0.19 0.34 0.35 0.39 N 139705 288827 38938 47141 146574 158479 88300 137437<br><br>(B) Group age diversity<br><br>dGage 0.59 8.45*** 15.06*** 19.82*** 10.92*** 23.23*** 11.41*** 11.28*** (3.41) (0.71) (1.52) (2.73) (3.37) (3.38) (2.44) (1.95)<br><br>University ranking −1.41*** −1.04*** −0.60** −0.51** −0.10 −0.55* −0.34 −1.31***<br><br>(0.39) (0.08) (0.24) (0.26) (0.46) (0.29) (0.30) (0.23) Author’s prior impact 0.62*** 1.24*** 1.52*** 1.61*** 0.72*** 1.51*** 1.60*** 1.53***<br><br>(0.01) (0.01) (0.01) (0.01) (0.02) (0.01) (0.01) (0.01) Year of publication 0.22 0.28*** 0.38*** 0.04 0.08 0.42* 0.14* 1.09*** (0.21) (0.01) (0.09) (0.07) (0.16) (0.23) (0.09) (0.11) Number of authors 0.18 0.24 0.17*** −0.02 0.74 0.00 0.63 0.56*** (0.28) (0.15) (0.06) (0.76) (1.04) (0.21) (0.49) (0.12) Const 2221.02*** 598.55*** 1081.71*** 1085.84*** 1289.91*** 2142.17*** 1813.42*** 2750.75***<br><br>(270.36) (22.94) (114.27) (124.13) (230.16) (194.14) (188.89) (144.35) R2 0.11 0.24 0.32 0.31 0.19 0.34 0.32 0.38 N 139,705 288,827 38,938 47,141 146,574 158,479 88,300 137,437<br><br>(C) Group gender diversity<br><br>dGgen −6.34 −0.93 0.57 1.54 1.55 −0.24 6.34** −0.85 (4.48) (1.38) (1.67) (3.38) (4.41) (2.60) (2.93) (2.09)<br><br>University ranking −0.75 −0.69*** 0.06 −1.72*** −0.11 −0.68** −1.11*** −0.92*** (0.56) (0.12) (0.19) (0.41) (0.59) (0.29) (0.35) (0.29)<br><br>Author’s rior impact 1.33*** 1.67*** 0.92*** 1.53*** 0.65*** 1.47*** 1.06*** 1.61*** (0.02) (0.02) (0.01) (0.04) (0.03) (0.01) (0.05) (0.01)<br><br>Year of publication 0.70** 0.22*** 0.34*** 0.07 0.02 0.22 0.05 1.04***<br><br>(0.35) (0.03) (0.10) (0.08) (0.21) (0.23) (0.10) (0.15)<br><br>Number of authors −0.13 0.79*** 0.38*** 1.44* 1.75 1.12*** 1.13** 0.76***<br><br>(0.36) (0.19) (0.06) (0.78) (1.27) (0.19) (0.51) (0.13)<br><br><br>Const 946.57** 541.77*** 2617.85*** 468.14*** 1579.15*** 2669.66*** 784.17*** 2787.59***<br><br>(409.64) (41.14) (104.67) (116.18) (304.95) (235.49) (133.25) (183.41) R2 0.16 0.29 0.32 0.31 0.17 0.39 0.26 0.41 N 58,288 188,249 14,904 8911 36,949 30,420 50,887 71,630 (D) Group afﬁliation diversity dGaff −2.85 2.93*** 2.45** 0.85 9.88*** 5.77*** 0.43 3.89***<br><br>(2.35) (0.60) (0.97) (2.70) (3.35) (1.97) (2.26) (1.36)<br><br>University ranking −1.35*** −1.16*** −0.12 −1.29*** −0.26 −0.59** −0.79*** −1.42*** (0.39) (0.08) (0.18) (0.36) (0.46) (0.30) (0.30) (0.24)<br><br>Author’s prior impact 0.62*** 1.23*** 0.92*** 1.49*** 0.72*** 1.60*** 1.04*** 1.53*** (0.01) (0.01) (0.01) (0.03) (0.02) (0.01) (0.04) (0.01)<br><br>Year of publication 0.14 0.25*** 0.28*** 0.13* 0.10 0.58** 0.06 1.04*** (0.21) (0.01) (0.09) (0.07) (0.16) (0.23) (0.09) (0.11)<br><br>Number of authors 0.26 0.55*** 0.35*** 1.59** 0.71 0.31 1.24** 0.64*** (0.28) (0.15) (0.06) (0.77) (1.05) (0.21) (0.49) (0.12) Const 2240.33*** 622.76*** 2370.64*** 327.82*** 1336.28*** 2319.30*** 793.64*** 2721.82***<br><br>(275.40) (23.59) (91.50) (97.70) (230.77) (231.07) (117.89) (144.24) R2 0.11 0.24 0.32 0.30 0.20 0.35 0.25 0.39 N 38,236 35,925 4736 2738 61,898 6431 25,656 32,279 (E) Group discipline diversity dGdsp 7.39 15.08*** 6.92 31.35*** 24.35*** 7.00 25.05*** 15.77***<br><br>(9.91) (1.66) (5.47) (6.68) (7.37) (13.70) (7.08) (3.42) University ranking −2.46*** −1.01*** −0.49 −1.36*** −0.96 0.28 −0.85* −1.75***<br><br>(0.55) (0.10) (0.30) (0.51) (0.64) (0.53) (0.48) (0.32) Author’s prior impact 0.62*** 1.35*** 0.91*** 1.45*** 0.69*** 1.80*** 0.96*** 1.55***<br><br>(0.01) (0.01) (0.01) (0.04) (0.03) (0.02) (0.05) (0.01)<br><br>Year of publication 0.15 0.28*** 0.29*** 0.01 −0.01 0.71*** 0.19** 1.13*** (0.22) (0.02) (0.09) (0.08) (0.18) (0.25) (0.10) (0.11)<br><br><br><br><br><br><br>Number of authors 0.02 0.05*** 0.02*** 0.24* 0.28 0.10*** 0.17*** 0.04*** (0.02) (0.02) (0.01) (0.14) (0.20) (0.03) (0.05) (0.01) Const −253.60 566.42*** 598.47*** 24.34 76.50 −1412.96*** 387.01** 2278.47***<br><br>(446.69) (32.93) (182.43) (161.50) (352.32) (502.55) (190.31) (226.61) R2 0.10 0.25 0.26 0.29 0.18 0.35 0.21 0.38 N 104,088 141,917 20,801 12,238 100,839 24,773 65,607 98,006<br><br>The regression tables below present the effect of each of the ﬁve group diversity indices, dGx : x 2 feth;age;gen;aff;dspg, on the paper’s impact, cG5. Along with each class of diversity, the following predictor variables were used: university ranking, author’s prior impact, year of publication, and number of authors. Here, university rankings are based on the 2017 Academic Ranking of World<br><br>Universities, also known as the Shanghai Ranking, whereas an author’s prior impact is measured as the annual number of citations that he/she accumulated prior to the year in which the paper was published. The columns correspond to papers from different ﬁelds. Of the ﬁve classes of diversity studied, ethnic diversity (A) was the only one for which all coefﬁcients in the ﬁrst row dGeth are positive and signiﬁcant. Standard errors in parentheses<br><br>*p < 0.1; **p < 0.05; and ***p < 0.01|
|---|


#### a b c d

Real, dGeth

Randomized, dGeth Real, dIeth Randomized, dIeth

10

4

~I

~I

~G eth d ~G

GP(d)eth

IP(d)eth

IP(d)eth

I)P(deth

d

eth d

d

2

eth

5

5

2

eth

0

0

0

0

0.0 0.2 0.4 0.6 0.8 1.0 dGeth dGeth dIeth dIeth

0.0 0.2 0.4 0.6 0.8 1.0

0.0 0.2 0.4 0.6 0.8 1.0

0.0 0.2 0.4 0.6 0.8 1.0

Publication year against impact

e f

Real

Randomized

60

60

|dGeth > d<br><br>~G<br><br>eth dGeth ≤ d<br><br>~G<br><br>eth|
|---|


|dGeth > d<br><br>~G<br><br>eth dGeth ≤ d<br><br>~G<br><br>eth|
|---|


50

50

40

40

G〈〉c5

G〈〉c5

30

30

20

20

10

10

1980 1985 1990 1995 2000 2005 2010

1980 1985 1990 1995 2000 2005 2010

Year of publication

Year of publication

No. authors per paper against impact

g h

Randomized

Real

45

45

|dGeth > d<br><br>~G<br><br>eth dGeth ≤ d<br><br>~G<br><br>eth|
|---|


|dGeth > d<br><br>~G<br><br>eth dGeth ≤ d<br><br>~G<br><br>eth|
|---|


40

40

G〈〉c5

G〉〈c5

35

35

30

30

25

25

3 4 5 6 7 8 9 10 3 4 5 6 7 8 9 10 No. authors/paper

No. authors/paper

No. collaborators per author against impact

i j

Real

Randomized

40

40

|dIeth > d<br><br>~I<br><br>eth dIeth ≤ d<br><br>~I<br><br>eth|
|---|


|dIeth > d<br><br>~I<br><br>eth dIeth ≤ d<br><br>~I<br><br>eth|
|---|


35

35

I〈〉c5

I〉〈c5

30

30

25

25

20

20

10 20 30 40 50 60 70 No.collaborators/author

10 20 30 40 50 60 70 No.collaborators/author

Fig. 4 The relationship between ethnic diversity and impact. a Distribution of dGeth in real data. Papers were partitioned into two categories: diverse (highlighted in the darker tones, with dGeth>~dGeth) and non-diverse (highlighted in the lighter tones, with dGeth ~dGeth), where the tilde denotes the median.

###### b The same as (a), but for randomized data. c and d The same as (a, b), respectively, but with dIeth instead of dGeth. e hcG5 i against publication year in real

data. f The same as (e), but for randomized data. g hcG5 i against number of authors per paper in real data. h The same as (g), but for randomized data. i hcI5i against number of collaborators per scientist in real data. j The same as (i), but for randomized data

whose dethG >0 and dethI >0, respectively. To determine whether this is the case, we replicated the analysis of papers but after excluding

Supplementary Figure 11. As can be seen, even after this exclusion, the diverse mostly outperform the non-diverse, regardless of publication year, number of authors per paper, and number of collaborators per scientist.

those with dethG ¼ 0, and likewise replicated the analysis of scientists but after excluding those with dethI ¼ 0; see

Inferring causality. To provide further evidence of the link between ethnic diversity and scientiﬁc impact, we use coarsened exact matching34, a technique typically used to infer causality in observational studies35. Speciﬁcally, it matches the control and treatment populations with respect to the confounding factors identiﬁed, thereby eliminating the effect of these factors on the phenomena under investigation. In our case, when studying group ethnic diversity, the treatment set consists of papers for

which dethG >P100 i dethG , and the control set of papers for which dethG Pi dethG , where Pi dethG denotes the ith percentile of dethG . This process is repeated using i = 10, 20, 30, 40, 50, corresponding to progressively larger gaps in ethnic diversity between the two populations. Thus, if ethnic diversity is indeed associated with increased scientiﬁc impact, we would expect to ﬁnd a signiﬁcant difference in impact between the two populations, and expect this difference to increase in tandem with the aforementioned gap in diversity. The confounding factors identiﬁed were the year of publication, number of authors, ﬁeld of study, authors’ impact prior to publication, and university ranking. The same process was carried out for individual ethnic diversity, for which the confounding factors were academic age, number of collaborators, discipline, and university ranking; see Supplementary Note 5 and Supplementary Figures 12 and 13 for more details, and Supplementary Figure 14 for an illustration of how this process works on a given collection of papers. The results for group and individual ethnic diversities are summarized in Tables 2 and 3, respectively. As can be seen, increasing the diversity gap between the control and treatment populations is

often accompanied by a greater difference in scientiﬁc impacts between the two populations. Remarkably, in the case of papers and scientists above the 90th percentile, the difference in scientiﬁc impact reaches 10.63% and 47.67%, respectively, compared to their counterparts below the 10th percentile. Clearly, these results do not suggest that diversity is the only causal factor. For example, one may argue that highly ranked universities tend to attract students from around the world and are more ethnically diverse as a result; indeed we veriﬁed that this was the case (see Supplementary Note 6 and Supplementary Figures 15 and 16). In such situations, coarsened exact matching is particularly useful precisely because it allows us to establish causality despite such effects.

Interplay between group and individual ethnic diversity. Finally, we investigate the interplay between group ethnic diver-

sity, dethG , and individual ethnic diversity, dethI . To this end, for each of the 1,045,401 papers in our dataset, we calculate dethI averaged over the authors in that paper; we denote this as dethI paper. This allows us to study the ways in which the two notions of diversity vary in the same paper. Indeed, as illustrated in Fig. 5, a paper can have high dethG and at the same time have low dethI paper, and vice versa. With this in mind, we studied the impact, cG5 , of papers falling in different ranges of dethG and dethI paper; see the matrix at the bottom-right corner of Fig. 5. Here, if we denote this matrix by A, and label the bottom row and leftmost column as 1, we ﬁnd

|Table 2 Coarsened exact matching of group ethnic diversity<br><br>|T| |C| |T′| |C′| L1 δ CI0.95 p<br><br>T : dGeth>P90ðdGethÞ C : dGeth P10ðdGethÞ<br><br>17,802 45,710 13,530 16,008 0.39 10.63 [8.10, 12.38] 0.003<br><br>T : dGeth>P80ðdGethÞ C : dGeth P20ðdGethÞ<br><br>24,827 45,710 18,965 16,165 0.38 10.22 [8.12, 12.02] 0.0009<br><br>T : dGeth>P70ðdGethÞ C : dGeth P30ðdGethÞ<br><br>56,662 58,889 51,782 39,216 0.27 4.93 [3.74, 5.97] 0.008<br><br>T : dGeth>P60ðdGethÞ C : dGeth P40ðdGethÞ<br><br>63,129 78,340 57,279 58,199 0.29 5.14 [4.12, 6.17] 0.003<br><br>T : dGeth>P50ðdGethÞ C : dGeth P50ðdGethÞ<br><br>63,129 127,629 58,292 70,627 0.27 3.37 [2.45, 4.25] 0.018<br><br>T and C are the treatment and control populations respectively; T′ and C′ are the populations of matched treatment and matched control papers, respectively; L1 is the multivariate imbalance statistic34; δ is the relative impact gain of T′ over C′, i.e., δ ¼ 100´ cG5 T′ cG5 C′ = cG5 C′. A t-test shows that δ is statistically signiﬁcant; see the resulting p-values. Since the academic impact hcG5i is sensitive to extremal values, we bootstrap a 95% conﬁdence interval (CI0.95). Here, university ranking corresponds to the average rank of all universities in the paper, as opposed to the highest ranked university in the paper, which is the case in Supplementary Table 5. For more details, see Supplementary Note 6.|
|---|


|Table 3 Coarsened exact matching of individual ethnic diversity<br><br>|T| |C| |T′| |C′| L1 δ CI0.95 p<br><br>T : dIeth>P90ðdIethÞ C : dIeth P10ðdIethÞ<br><br>113,883 68,563 16,512 20,599 0.47 47.67 [44.49, 49.92] 2.04e−39<br><br>T : dIeth>P80ðdIethÞ C : dIeth P20ðdIethÞ<br><br>139,015 136,837 65,412 50,240 0.35 43.54 [42.61, 45.05] 1.50e−156<br><br>T : dIeth>P70ðdIethÞ C : dIeth P30ðdIethÞ<br><br>223,747 205,686 128,001 117,560 0.32 28.75 [28.10, 29.46] 1.65e−211<br><br>T : dIeth>P60ðdIethÞ C : dIeth P40ðdIethÞ<br><br>280,514 274,209 184,749 143,683 0.29 23.86 [22.86, 23.98] 5.96e−218<br><br>T : dIeth>P50ðdIethÞ C : dIeth P50ðdIethÞ<br><br>356,564 329,066 242,123 240,237 0.28 15.77 [15.21, 15.95] 3.23e−158<br><br>The notation is as per Table 2.|
|---|


Paper A: High dGeth

Paper B: Low dGeth

Low 〈dIeth〉paper

Low 〈dIeth〉paper

A B

C D

Paper D: High dGeth

Paper C: Low dGeth

High 〈dIeth〉paper

High 〈dIeth〉paper

Group ethnic diversity index, dGeth

High dGeth

Low dGeth

Individual ethnic diversity index, dIeth

High dIeth Low dIeth

1

![image 1](The Preeminence of Ethnic Diversity in Scientific Collaboration_images/imageFile1.png)

75 60 45 30 15 0

G〈〉Avg. citation count,c5

Mean individual ethnic

I〉〈paperdiversity,deth

0.75

0.50

0.25

0

0 0.25 0.50 0.75 1 Mean group ethnic diversity, 〈dGeth〉

- Fig. 5 The interplay between group and individual ethnic diversity. The top part of the ﬁgure illustrates an example of 4 papers. The authors of paper A have


different ethnicities, but each has ethnically homogeneous collaborators. Then, one could argue that paper A has high dGeth but low dIeth paper. Similarly, paper B has low dGeth and low dIeth paper, paper C has low dGeth and high dIeth paper, and paper D has high dGeth and high dIeth paper. The matrix at the bottomright corner represents the mean citation counts, cG5 , of papers falling in different ranges of dGeth and dIeth paper

that P4i¼1 Ai;1<P4i¼1 A1;i and P4i¼1 Ai;4>P4i¼1 A4;i. Hence, while it appears that both group and individual diversities can be valuable, the former seems to have a greater effect on scientiﬁc impact. In other words, having co-authors who are inclined to collaborate across ethnic lines (i.e., co-authors whose individual ethnic diversity is high) appears to be not as important as the mere presence of co-authors of different ethnicities (i.e., co-authors whose group ethnic diversity is high).

Discussion

To summarize, this study is the ﬁrst to cover ﬁve different classes of diversity, which allowed us to illuminate many interesting connections between diversity and scientiﬁc collaboration. It was also important to establish the occurrence of homophily, and this was achieved via a set of randomized baseline models. These were used to compare observed collaborations with simulated data where the attribute of interest was randomized while controlling for the relevant confounding variables. These comparisons revealed clear and consistent patterns of homophily in the cases of ethnicity, gender, and afﬁliation, and also revealed that ethnicity was the only attribute for which homophily is increasing over time. In the case of academic age, inverse homophily was found, i.e., scientists seem to prefer collaborating with individuals from different age groups, a possible reﬂection of the widely held practice of research students being mentored by, and collaborating with, more senior academics.

Armed with these results, we shifted our focus to the effect of homophily (and diversity) on scientiﬁc impact. This analysis was conducted using a number of different analytical tools, including regression analysis, randomized baseline models, and coarsened exact matching. Broadly, we found that diversity was positively correlated with impact, though the statistical signiﬁcance of the observed effect varied signiﬁcantly depending on the class of diversity and ﬁeld of study. Overall, discipline and afﬁliation diversity were the least correlated with impact, a surprising ﬁnding given the apparent importance of these attributes. Conversely, ethnic diversity had the strongest correlation, which is especially surprising since ethnicity is not as related to technical competence as the other classes mentioned.

These ﬁndings have signiﬁcant implications. For one, recruiters should always strive to encourage and promote ethnic diversity, be it by recruiting candidates who complement the ethnic composition of existing members, or by recruiting candidates with proven track records in collaborating with people of diverse ethnic backgrounds. Another implication is that, while collaborators with different skill sets are often required to perform complex tasks, multidisciplinarity should not be an end in of itself; bringing together individuals of different ethnicities—with the attendant differences in culture and social perspectivescould ultimately produce a large payoff in terms of performance and impact. To put it differently, intangible factors, such as team cohesion and a sense of esprit de corps should be considered in addition to technical alignment.

The underlying message is an inclusive and uplifting one. In an era of increasing polarization and identity politics, our ﬁndings may positively contribute to the societal conversation and reinforce the conviction that good things happen when people of different backgrounds, cultures, and ethnicities come together to work towards shared goals and the common good.

Data availability The details of all data and methods used are given in Supplementary Note 1.

Received: 31 May 2018 Accepted: 12 November 2018

![image 2](The Preeminence of Ethnic Diversity in Scientific Collaboration_images/imageFile2.png)

References

- 1. Wagner, C. S. & Jonkers, K. Open countries have strong science. Nature 550, 32–33 (2017).
- 2. Puritty, C. et al. Without inclusion, diversity initiatives may not be enough. Science 357, 1101–1102 (2017).
- 3. Page, S. E. The Difference: How the Power of Diversity Creates Better Groups, Firms, Schools, and Societies (Princeton University Press, Princeton, 2008).
- 4. Ager, P. & Brückner, M. Cultural diversity and economic growth: evidence from the US during the age of mass migration. Eur. Econ. Rev. 64, 76–97

(2013).

- 5. Lee, N. Migrant and ethnic diversity, cities and innovation: ﬁrm effects or city effects? J. Econ. Geogr. 15, 769–796 (2014).
- 6. Suedekum, J., Wolf, K. & Blien, U. Cultural diversity and local labour markets. Reg. Stud. 48, 173–191 (2014).
- 7. Levine, S. S. et al. Ethnic diversity deﬂates price bubbles. Proc. Natl Acad. Sci. USA 111, 18524–18529 (2014).
- 8. Herring, C. Does diversity pay?: race, gender, and the business case for diversity. Am. Sociol. Rev. 74, 208–224 (2009).
- 9. Paulus, P. B., van der Zee, K. I. & Kenworthy, J. Cultural diversity and team creativity. In The Palgrave Handbook of Creativity and Culture Research, 57–76 (Palgrave Macmillan, London, 2016).
- 10. Parrotta, P., Pozzoli, D. & Pytlikova, M. The nexus between labor diversity and ﬁrms innovation. J. Popul. Econ. 27, 303–364 (2014).
- 11. Østergaard, C. R., Timmermans, B. & Kristinsson, K. Does a different view create something new? the effect of employee diversity on innovation. Res. Policy 40, 500–509 (2011).
- 12. Brown, G. K. & Langer, A. Does afﬁrmative action work: lessons from around the world. Foreign Aff. 94, 49 (2015).
- 13. Arcidiacono, P., Lovenheim, M. & Zhu, M. Afﬁrmative action in undergraduate education. Annu. Rev. Econ. 7, 487–518 (2015).
- 14. Alvarez, K. J. & Levy, B. R. Health advantages of ethnic density for african american and mexican american elderly individuals. Am. J. Public Health 102, 2240–2242 (2012).
- 15. Das-Munshi, J., Becares, L., Dewey, M. E., Stansfeld, S. A. & Prince, M. J. Understanding the effect of ethnic density on mental health: multi-level investigation of survey data from england. BMJ 341, c5367 (2010).
- 16. Montalvo, J. G. & Reynal-Querol, M. Ethnic diversity and economic development. J. Dev. Econ. 76, 293–323 (2005).
- 17. Galinsky, A. D. et al. Maximizing the gains and minimizing the pains of diversity: a policy perspective. Perspect. Psychol. Sci. 10, 742–748 (2015).
- 18. Woolley, A. W., Chabris, C. F., Pentland, A., Hashmi, N. & Malone, T. W. Evidence for a collective intelligence factor in the performance of human groups. Science 330, 686–688 (2010).
- 19. Hong, L. & Page, S. E. Groups of diverse problem solvers can outperform groups of high-ability problem solvers. Proc. Natl Acad. Sci. USA 101, 16385–16389 (2004).
- 20. Jia, T., Wang, D. & Szymanski, B. K. Quantifying patterns of research-interest evolution. Nat. Hum. Behav. 1, 0078 (2017).
- 21. Deville, P. et al. Career on the move: geography, stratiﬁcation, and scientiﬁc impact. Scientiﬁc Rep. 4, 4770 (2014).
- 22. Sinatra, R., Wang, D., Deville, P., Song, C. & Barabási, A.-L. Quantifying the evolution of individual scientiﬁc impact. Science 354, aaf5239 (2016).
- 23. Wang, D., Song, C. & Barabási, A.-L. Quantifying long-term scientiﬁc impact. Science 342, 127–132 (2013).
- 24. Fortunato, S. et al. Science of science. Science 359, eaao0185 (2018).
- 25. Nielsen, M. W. et al. Opinion: gender diversity leads to better science. Proc. Natl Acad. Sci. USA 114, 1740–1742 (2017).
- 26. Jones, B. F. & Weinberg, B. A. Age dynamics in scientiﬁc creativity. Proc. Natl Acad. Sci. USA 108, 18910–18914 (2011).
- 27. Wuchty, S., Jones, B. F. & Uzzi, B. The increasing dominance of teams in production of knowledge. Science 316, 1036–1039 (2007).
- 28. Uzzi, B., Mukherjee, S., Stringer, M. & Jones, B. Atypical combinations and scientiﬁc impact. Science 342, 468–472 (2013).
- 29. Freeman, R. B. & Huang, W. Collaborating with people like me: ethnic coauthorship within the united states. J. Labor Econ. 33, S289–S318

(2015).

- 30. Jones, B. F., Wuchty, S. & Uzzi, B. Multi-university research teams: Shifting impact, geography, and stratiﬁcation in science. Science 322, 1259–1262

(2008).

- 31. Adams, J. Collaborations: the fourth age of research. Nature 497, 557–560


(2013).

- 32. McPherson, M., Smith-Lovin, L. & Cook, J. M. Birds of a feather: homophily in social networks. Annu. Rev. Sociol. 27, 415–444 (2001).
- 33. Bishop, B. CM: Pattern Recognition and Machine Learning. J. Electron. Imag. 16, 140–155 (2013).
- 34. Iacus, S. M., King, G. & Porro, G. Causal inference without balance checking: coarsened exact matching. Polit. Anal. 20, 1–24 (2012).
- 35. Catalini, C., Lacetera, N. & Oettl, A. The incidence and role of negative citations in science. Proc. Natl Acad. Sci. USA 112, 13823–13826 (2015).
- 36. Ambekar, A., Ward, C., Mohammed, J., Male, S. & Skiena, S. Name-ethnicity classiﬁcation from open sources. In Proc. 15th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 49–58 (ACM, 2009).
- 37. Ye, J. et al. Nationality classiﬁcation using name embeddings. In Proc. 2017 ACM on Conference on Information and Knowledge Management, 1897–1906 (ACM, 2017).


Acknowledgements

We thank Steven Skiena and his team for providing access to their Name Ethnicity Classiﬁer tool36,37. We also thank Kinga Makovi for suggesting the use of coarsened exact matching for causal inference.

Author contributions

B.K.A., T.R., and W.L.W. conceived and designed the experiments. B.K.A. and W.L.W. performed the coding of the experiments. B.K.A., T.R., and W.L.W. wrote the manuscript. B.K.A. and T.R. produced the ﬁgures and tables.

Additional information

Supplementary Information accompanies this paper at https://doi.org/10.1038/s41467018-07634-8.

Competing interests: The authors declare no competing interests.

Reprints and permission information is available online at http://npg.nature.com/ reprintsandpermissions/

Publisher’s note: Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional afﬁliations.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing,

adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org/ licenses/by/4.0/.

© The Author(s) 2018

