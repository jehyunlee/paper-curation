# arXiv:1712.01804v2[physics.soc-ph]16 Jun 2018

## Hot Streaks in Artistic, Cultural, and Scientiﬁc Careers

Lu Liu,1,2,3 Yang Wang,1,2 Roberta Sinatra,4 C. Lee Giles,3,5 Chaoming Song,6 Dashun Wang1,2

1Northwestern Institute on Complex Systems, Northwestern University, Evanston, IL, USA 2Kellogg School of Management, Northwestern University, Evanston, IL, USA

- 3College of Information Sciences and Technology, Pennsylvania State University, State College, PA, USA
- 4Center for Network Science and Mathematics Department, Central European University, Budapest, Hungary
- 5Department of Computer Science and Engineering, Pennsylvania State University, State College, PA, USA
- 6Department of Physics, University of Miami, Coral Gables, FL, USA


The hot streak, loosely deﬁned as winning begets more winnings, highlights a speciﬁc period during which an individual’s performance is substantially higher than her typical performance. While widely debated in sports1–3, gambling4–7, and ﬁnancial markets8–10 over the past several decades, little is known if hot streaks apply to individual careers. Here, building on rich literature on lifecycle of creativity11–23, we collected large-scale career histories of individual artists, movie directors and scientists, tracing the artworks, movies, and scientiﬁc publications they produced. We ﬁnd that, across all three domains, hit works within a career show a high degree of temporal regularity, each career being characterized by bursts of high-impact works occurring in sequence. We demonstrate that these observations can be

explained by a simple hot-streak model we developed, allowing us to probe quantitatively the hot streak phenomenon governing individual careers, which we ﬁnd to be remarkably universal across diverse domains we analyzed: The hot streaks are ubiquitous yet unique across different careers. While the vast majority of individuals have at least one hot streak, hot streaks are most likely to occur only once. The hot streak emerges randomly within an individual’s sequence of works, is temporally localized, and is unassociated with any detectable change in productivity. We show that, since works produced during hot streaks garner signiﬁcantly more impact, the uncovered ho t streaks fundamentally drives the collective impact of an individual, ignoring which leads us to systematically over- or under-estimate the future impact of a career. These results not only deepen our quantitative understanding of patterns governing individual ingenuity and success, they may also have implications for decisions and policies involving predicting and nurturing individuals with lasting impact.

A creative career is often deﬁned by the sequence of works an individual produces at various stages14,15,20,22–25. According to the Matthew effect12,26–28, victories bring reputation and recognition that can translate into tangible assets which in turn help bring future victories. This school of thought supports the existence of hot streaks in a career, which is also consistent with the innovation literature showing that peak performance clusters in time, typically occurring around mid career11,14,24. Yet, on the other hand, the random impact rule uncovered in arts13,24 and sciences13,23 predicts the opposite: The best works occur randomly within a career, primarily driven by productivity. Following this school of thought, works after a major breakthrough are not affected by what preceded them, supporting the viewpoint of regression toward the mean. The two divergent

schools of thought, together with the consequential nature of this question to individual ingenuity and success, raise a fundamental question: Do hot streaks exist in creative careers?

To answer this question, we collected systematically large-scale datasets recording career histories of individual artists, movie directors and scientists (Supplementary Information S1), al-

lowing us to explore across three major domains involving human creativity. The ﬁrst dataset (D1) consists of auction records curated from online auction databases, allowing us to reconstruct career histories of 3,480 artists through the sequence of works they each produced, together with impacts of the artworks, approximated by hammer prices in auctions20. D2 contains proﬁles of 6,233 movie directors recorded in the IMDB database, each career being represented by the sequence of movies he/she directed. Since metrics that quantify impacts of a movie correlate closely with each other29, here we use the IMDB ratings to measure the goodness of a movie. Finally,

- our third dataset (D3) includes publication records of 20,040 individual scientists through a largescale name disambiguation effort that combined the Web of Science and Google Scholar datasets (Supplementary Information S1.3). The impact of each paper is measured by citations garnered


after 10 years of its publication17,21,23,30, C10. Since hammer price (D1) and C10 (D3) both follow fat-tailed distributions (Fig. S3), here we take the logarithmic of these measures, i.e., log(price) and log(C10) to approximate the goodness of an artwork and scientiﬁc publication.

Motivated by Merton’s theory of multiples12,31, we start by investigating the timing of the three most impactful works produced in each career. In a sequence of N works by an individual, we denote with N∗ the position of the highest impact work within a career, N∗∗ the second high-

est and N∗∗∗ the third. We ﬁnd each of the three highest impact works occurs randomly within a career (Fig. S4). That is, when it comes to any of the three most expensive artworks by an artist, three highest rated movies by a director, and three highest impact publications by a scientist, each of them is randomly distributed among all the works one produces. These results offer strong endorsement for the random impact rule13,23,24, hence supporting an unpredictable view of individual creativity.

Yet, as we show next, the random impact rule observed across creative careers is only apparent, because the timing between creative works follows highly predictable patterns. Indeed, we measure the correlation between the timing of the two biggest hits within a career (e.g., N∗ and N∗∗) by calculating the joint probability P(N∗,N∗∗), and compare it with a null hypothesis in which N∗ and N∗∗ each occurs at random. We ﬁnd that, the normalized joint probability, φ(N∗,N∗∗) = P(N∗,N∗∗)/(P(N∗)P(N∗∗)), is signiﬁcantly overrepresented along the diagonal elements of matrices (Figs. 1a–c), demonstrating that N∗ and N∗∗ are much more likely to colocate with each other than what we would expect from the random impact model. Moreover, the colocation pattern is universal across a wide range of careers we studied, including artists (Fig. 1a), movie directors (Fig. 1b) and scientists (Fig. 1c). The diagonal pattern disappears if we shufﬂe the order of works within each career, thereby breaking the temporal correlations between highest impact works while preserving the random impact rule (Figs. 1d–f, Fig. S6).

To quantify the temporal colocation of hits observed in Figs. 1a–c, we calculate the distance between two highest impact works for every individual, measured by the number of works

produced in between, ∆N = N∗−N∗∗. We compare P(∆NN ) of real careers with PS(∆NN ) of shufﬂed careers by deﬁning R(∆NN ) = P(∆NN )/PS(∆NN ). For artists, movie directors, and scientists, R(∆NN ) all exhibits a clear peak centering around zero and decays quickly as ∆N deviates from zero (Figs. 1j–l). Indeed, the two most important works of an artist is 1.48 times more likely to occur back-to-back than expected by chance (Fig. 1j). The same is true for movie directors (Fig. 1k) and scientists (Fig. 1l), where such colocation is 1.42 and 1.57 times more likely than their baseline occurrence rate, respectively. Also important to note is the interesting fact that R(∆NN ) is mostly symmetric around zero (Figs. 1j–l), indicating a comparable likelihood for the biggest hit to arrive before or after the second biggest for all three types of careers. This symmetry was also captured by Figs. 1a–c, where φ features a roughly even split across the diagonal. The colocation patterns documented in Figs. 1a–c and 1j–l are not limited to the two highest impact works within a career. Indeed, we repeated our analyses for other pairs of hit works, such as N∗ vs. N∗∗∗ and N∗∗ vs. N∗∗∗, uncovering the same colocation patterns (Figs. 1j–l and Fig. S5).

Do high impact works come in streaks within a career? To answer this question, we count the number of consecutive works whose goodness exceeds a certain threshold across various careers (Figs. 1m–o). Here we choose the median goodness of all works within a career as the threshold. We calculate the length of the longest streak L for each career, and measure the distribution of L across our user base in each of the three domains. We then shufﬂe the order of works within each career, and measure again their longest streaks Ls. We ﬁnd P(L) is characterized by a much longer tail, compared with P(Ls) (Figs. 1p–r), indicating real careers are characterized by long streaks of excellent works clustered together in sequence. Note that for the three types of careers,

the tail part of both P(L) and P(Ls) follows approximately an exponential function, meaning that the likelihood to observe a longer streak diminishes rather rapidly. Hence, the deviations observed between P(L) and P(Ls) are rather signiﬁcant (Fig. S11). To test the robustness of these results, we repeated our analyses by controlling for individual career length, and also varying our threshold used to calculate L, ﬁnding our conclusions remain the same (Supplementary Information S2.4 and

- S2.5).


Taken together, results presented in Fig. 1 paint a rather unexpected portrait of individual careers. Indeed, while the timing of high impact works each appears at random by itself, their relative timing, however, follows highly reproducible yet previously unknown patterns. As such, individual careers are far from being random, but characterized by bursts of high-impact works occurring in sequence. These fascinating empirical ﬁndings raise an important question: What are the mechanisms responsible for the temporal regularities observed across diverse career histories?

To unearth the fundamental mechanisms governing the patterns documented in Fig. 1, let us ﬁrst consider a null model in which the goodness of works produced in a career (i.e.. log(price)

for artists, ratings for directors, and log(C10) for scientists) is drawn from a normal distribution

N(Γi, σi2), ﬁxed for an individual. The average Γi characterizes typical impact of works produced by the individual, and σi captures the variance. This null model reproduces the fact that each hits occur randomly within a career13,23 and the differences in typical impact between careers (Supplementary Information S3.2, Figs. S25–S27). Yet it fails to capture any of the temporal correlations observed in Fig. 1. The main reason is illustrated in Figs. 2a–c, where we selected for

illustration purposes one individual from each of the three datasets and measure the dynamics of Γi during his/her career. We ﬁnd Γi is not constant throughout a career. Rather, it features deviations from a baseline performance (Γ0) at a certain point of a career (t↑), elevating to a higher value ΓH (ΓH > Γ0), which is then sustained for some time before falling back to a similar level as Γ0 (Figs. 2a–c):

 

ΓH t↑ ≤ t ≤ t↓

, (1)

Γ(t) =



Γ0 otherwise

This observation, combined with the shortcomings of the null model, raises an intriguing hypothesis: Could a simple model based on (1) explain the temporal anomalies documented in Fig. 1?

To test this hypothesis, we apply (1) to real productivity patterns of an individual, allowing us to generatively simulate impacts of the works produced by an individual (Supplementary Informa-

tion S3.3). As an individual’s baseline performance is captured by Γ0, during the period in which ΓH operates (t↑ ≤ t ≤ t↓), the individual seemingly performs at a higher level than her typical performance (Γ0), prompting us to call this model, the hot-streak model, and correspondingly, the ΓH period as the hot streak. Hence, in the hot-streak model, the goodness of works produced by an individual is drawn from two distributions N(Γ0, σ2) and N(ΓH, σ2), depending on whether the individual is within the hot streak. We introduce to each career one ho t streak that occurs at random with a ﬁxed duration and magnitude, and repeat our measurements in Fig. 1 on careers generated by the model. We ﬁnd, while equation (1) only introduces a simple temporal variation, surprisingly the hot-streak model is sufﬁcient in reproducing all empirical observations that existing modeling frameworks fail to account for from the temporal colocations among top hit works within a career

(Figs. 1g–i), to their temporal distances (Figs. 1j–l), to the occurrences of long streaks of excellent works (Figs. 1p–r). For full comparisons with existing models, see Supplementary Information S4. Equation (1) assumes implicitly each individual has one hot streak, a hypothesis that we test later. Given the myriad factors that can affect career impacts12–16,23,25,32,33, and the obvious diversity of careers we studied, the level of universality and accuracy demonstrated by the simple hot-streak model is rather unexpected.

The real value of the model arises, however, when we ﬁt the model to real careers to obtain the individual speciﬁc Γ0, ΓH, t↑ and t↓ parameters (Supplementary Information S3.4), allowing us to probe quantitatively the hot streak phenomenon underlying artistic, cultural, and scientiﬁc careers, and helping us reveal several fundamental patterns governing individual careers:

- 1. The hot streak is ubiquitous across careers, yet at the same time rather unique within a career. We ﬁnd, the vast majority of artists (91%, Fig. 2d), movie directors (82%, Fig. 2e) and scientists (90%, Fig. 2f) have at least one hot streak throughout their careers, documenting the practical relevance of the uncovered hot streak phenomenon. Yet, despite its ubiquity, the hot streak is most likely to be unique within a career. Indeed, we relax our ﬁtting algorithm to


allow for multiple hot streaks (up to three) with different values of ΓH, ﬁnding that, among those who have a hot streak, 64% of artists, 80% of directors, and 68% of scientists are best captured by one hot streak only (Figs. 2d–f), documenting the precious nature of hot streaks. Second acts may occur but less likely, particularly for movie directors. About 30% of artists and scientists have two hot streaks, but only 11% for directors. Occurrences of

more than two hot streaks are rare across all careers. We also ﬁnd that, between those who have one or two hot streaks, there is no detectable difference in terms of typical performance metrics, including impact, productivity and career length (Fig. S22), suggesting that hot streaks capture an orthogonal dimension to current metrics characterizing individual careers.

- 2. The hot streak occurs randomly within a career. We estimate the beginning of hot streaks

for artistic, cultural, and scientiﬁc careers. Denoting with N↑, the position of work produced when the hot streak starts (t↑), we ﬁnd that N↑ is randomly distributed in the sequence of N works within a career (Figs. 2g–i). This ﬁnding reconciles two seemingly divergent schools of thought12,13,23, providing a further explanation for the random impact rule: If the hot streak occurs randomly within a career, and the highest impact works are statistically more likely to appear within the hot streak, then the timing of the highest impact works would also appear random.

- 3. Across different domains, a hot streak lasts for a considerably shorter period comparing with the typical career length recorded in our database. We measure the duration distribution

of hot streaks (τH = t↑ − t↓), ﬁnding P(τH) peaks around 5.7 years for artists, 5.2 years for directors, and 3.7 years for scientists (Figs. 2j–l). Interestingly, the duration of a hot streak is independent of when it occurs within a career (early, mid or late career, Figs. 2j–l). The temporally localized nature of hot streaks is also captured by its proportion over career length τH/T (Figs. 2j–l, insets), whose median hovers around 20% (0.17 for artists, 0.23 for directors, and 0.20 for scientists).

- 4. How much does an individual deviate from her typical performance during hot streaks?


- Do people with higher Γ0 also experience more performance gain from hot streaks? To answer these questions, we explore correlations between Γ0 and ΓH, ﬁnding them to be well approximated by a linear relationship across three kinds of careers (Figs. 2m–o). Hence the better typical performance, the better individuals perform during their hot streaks. It is interesting to note that the coefﬁcients are slightly less than 1 (0.99 for artists, 0.85 for directors, and 0.9 for scientists, Figs. 2m–o). Hence ∆Γ ≡ ΓH − Γ0 decreases with Γ0 (Figs. 2m–o insets), suggesting individuals with smaller Γ0 beneﬁt more from hot streaks. These results are again independent of when hot streaks occur along a career (Figs. 2m–o).
- 5. Are individuals more productive during hot streaks? Surprisingly, the answer is no. We


measure the distribution of the total number of works produced during hot streaks P(NH). We then construct a null distribution, by randomly picking one work out of a career and designating its production year to be the start of the hot streak. We ﬁnd P(NH) measured in real careers well aligns with the null model’s predictions for all three kinds of careers (Figs. 2p–r). Therefore, individuals show no detectable change in productivity during hot streaks, despite the fact that their outputs during the period are signiﬁcantly better than typical, suggesting an endogenous shift in individual creativity when a hot streak occurs.

What is the impact of hot streaks on individual careers? To answer this question, we focus on scientiﬁc careers (D3), and measure the collective impact of a scientist, g(t), deﬁned as the total number of citations over time collected by all the papers one published. Brought to spotlight by popular websites such as Google Scholar (Fig. 3a), g(t) is playing an increasingly important

role in driving many critical decisions, from hiring, promotion and tenure to awarding of grants and rewards. Next we show the collective impact of an individual is fundamentally governed by the uncovered hot streak phenomenon, ignoring which would lead us to systematically under- or over-estimate the future impact of a scientist.

Many factors are known to inﬂuence the collective impact of a career, ranging from productivity15,22,34 to citation disparity and dynamics17,18,21,25,27,35 to temporal inhomogeneities along a career14,22–25,36. Since our goal is to understand impact, here we bypass the need to evaluate the inhomogeneous nature of productivity22,23 by rearranging publication time of each paper, such that an individual produces a constant number of papers each year, denoted by n (Figs. 3b–c). To calculate g(t) analytically, we need to incorporate papers’ citation patterns into our hot-streak model (1). A recent study21 suggests that citation dynamics of a paper published at time t0 can be approximated by

C(t,t0) = m eλΦ

ln(t−t0)−µ σ

− 1 ≡ m eΓ(t0)Φ

ln(t−t0)−µ σ

###### − 1 , (2)

where m is a global parameter describing the typical number of references a paper contains, and Φ(·) is the cumulative normal function, characterized by µ and σ, which capture the typical citation life cycle of a paper. The paper’s impact is ultimately determined by its ﬁtness21, λ. To adapt this model into our framework, we replace λ with Γ(t0), and for simplicity assume µ and σ are ﬁxed for different papers published by an individual. The resulting model, combining (1) and (2), can be solved analytically (Supplementary Information S5.1–S5.4), allowing us to express g(t) in terms

of hot-streak parameters (Γ0, ΓH, t↑, t↓):



0 t < t↑

0Φ(ln(t)−µ

g(t) = nm(eΓ

σ

g0(t)



nm(ΓH − Γ0)Φ ln(t−σt↑)−µ C(t,t↑) t↑ ≤ t < t↓

) − 1)

+

nm(ΓH − Γ0)[Φ ln(t−σt↑)−µ C(t,t↑)−

. (3)



Φ ln(t−σt↓)−µ C(t,t↓)] t ≥ t↓

∆g(t)

Equation (3) consists of two terms. g0(t) captures a career’s collective impact in the absence of hot streaks (i.e. Γ(t) = Γ0). Contributions from hot streaks are encoded in ∆g(t), driven by both the timing and magnitude of hot streaks (t↑, t↓, ΓH, and ΓH − Γ0). Varying hot streak parameters signiﬁcantly alters the collective impact of a career (Fig. 3d).

We adopt two measures to quantify the accuracy of our model (3). To account for the inherently noisy career trajectories, we ﬁrst assign an impact envelope to each individual, explicitly quantifying the uncertainty of model predictions (Fig. 3e, Supplementary Information S5.6). We measure the fraction of g(t) that fall within the envelope, ﬁnding the distribution across individuals peaks close to 1 (Fig. 3f), indicating most career trajectories are well encapsulated within the predicted envelopes. The superior accuracy of our model is also captured by the Mean Absolute Percentage Error (MAPE) (Fig. 3g), with improvement being most pronounced for an early onset of a hot streak (Fig. 3g), which is also correctly predicted by our model. Hence the hot-streak model captures a wide range of trajectories that collective impacts of scientiﬁc careers follow (Fig. 3h).

The observed accuracy prompts us to ask whether the hot-streak model is unique in its ability

to capture the impact of individual careers across diverse domains. There are several alternative hypotheses capturing different hot streak dynamics (Supplementary Information S6), each associated with possible origins of the uncovered hot streak phenomena: (A) A right trapezoid (Fig. S32b) captures a sudden onset of the hot streak with a more gradual decline, as innovators may stumble upon a groundbreaking idea, which manifests itself in the forms of multiple artworks, movies, and publications. Hence from an evolutionary perspective, the duration of hot streaks may characterize time it takes for the temporary competitive advantage to dissipate. (B) An isosceles trapezoid model (Fig. S32c) captures a hot streak that evolves and dissolves gradually over time, which may approximate social tie dynamics, as one individual’s hot streak could be the result of a fruitful, repeated collaboration32,37. (C) Furthermore, individual performance may peak at a certain point of a career, prompting us to test inverted-U shape (Fig. S32d) and tent functions (Fig. S32e). Lastly (D) a left trapezoid function (Fig. S32f) captures a gradual startup period with a sharp cutoff, corresponding to career opportunities that can augment impact but last for a ﬁxed duration.

We tested hypotheses A–D systematically to describe real careers (Supplementary Information S6). Of all hypotheses considered, the proposed hot-streak model is the simplest and least ﬂexible. Yet, surprisingly, it is the only model whose predictions are consistent with real careers (Fig. S32). The fact that none of the alternative hypotheses alone can fully account for empirical observations demonstrates the hot streak phenomena uncovered in creative careers may not be driven by one particular factor but a combination of multiple factors. Identifying its true origin requires additional experimentation and goes beyond the scope of this work. As such, hot streaks uncovered in this paper should be treated in a metaphorical sense, highlighting an intriguing period

of outstanding performance tracing individual careers without implying any associated drivers for the phenomena. Yet, crucially, the ﬁndings presented in this paper hold the same, regardless of the underlying drivers.

The analytical framework presented here not only offers a new theoretical basis for our quantitative understanding of dynamical patterns governing individual career impact, it also has policy implications for comparing and evaluating scientists (Fig. S30). Indeed, for individuals whose hot streaks are yet to come, ignoring hot streaks may lead to underestimating their impacts (Figs. S30a– b), especially given the ubiquitous nature of hot streaks (Fig. 2f). On the other hand, an early onset of hot streaks leads to a high impact that peaks early but may not sustain unless a second act occurs (Fig. S30c). Given that individuals improve substantially during hot streaks, the uncovered hot streak phenomenon can be particularly crucial for decisions and policies concerning long-term impact of a career.

- 1. Gilovich, T., Vallone, R. & Tversky, A. The hot hand in basketball: On the misperception of random sequences. Cognitive Psychology 17, 295–314 (1985).
- 2. Bar-Eli, M., Avugos, S. & Raab, M. Twenty years of hot hand research: Review and critique. Psychology of Sport and Exercise 7, 525–553 (2006).
- 3. Miller, J. B. & Sanjurjo, A. Surprised by the gambler’s and hot hand fallacies? A truth in the law of small numbers. IGIER Working Paper No. 552 (2016).
- 4. Ayton, P. & Fischer, I. The hot hand fallacy and the gambler’s fallacy: Two faces of subjective


- randomness? Memory & Cognition 32, 1369–1378 (2004).
- 5. Croson, R. & Sundali, J. The gambler’s fallacy and the hot hand: Empirical data from casinos. Journal of Risk and Uncertainty 30, 195–209 (2005).
- 6. Rabin, M. & Vayanos, D. The gambler’s and hot-hand fallacies: Theory and applications. The Review of Economic Studies 77, 730–778 (2010).
- 7. Xu, J. & Harvey, N. Carry on winning: The gamblers’ fallacy creates hot hand effects in online gambling. Cognition 131, 173–180 (2014).
- 8. Hendricks, D., Patel, J. & Zeckhauser, R. Hot hands in mutual funds: Short-run persistence of relative performance, 1974–1988. The Journal of Finance 48, 93–130 (1993).
- 9. Jagannathan, R., Malakhov, A. & Novikov, D. Do hot hands exist among hedge fund managers? An empirical evaluation. The Journal of Finance 65, 217–255 (2010).
- 10. Kahneman, D. & Riepe, M. W. Aspects of investor psychology. The Journal of Portfolio Management 24, 52–65 (1998).
- 11. Lehman, H. C. Age and achievement (Princeton, NJ, 1953).
- 12. Merton, R. K. The matthew effect in science. Science 159, 56–63 (1968).
- 13. Simonton, D. K. Age and outstanding achievement: What do we know after a century of research? Psychological Bulletin 104, 251 (1988).
- 14. Jones, B. F. & Weinberg, B. A. Age dynamics in scientiﬁc creativity. Proceedings of the National Academy of Sciences 108, 18910–18914 (2011).


- 15. Petersen, A. M., Jung, W.-S., Yang, J.-S. & Stanley, H. E. Quantitative and empirical demonstration of the matthew effect in a study of career longevity. Proceedings of the National Academy of Sciences 108, 18–23 (2011).
- 16. Petersen, A. M. et al. Reputation and impact in academic careers. Proceedings of the National Academy of Sciences 111, 15316–15321 (2014).
- 17. Stringer, M. J., Sales-Pardo, M. & Amaral, L. A. N. Effectiveness of journal ranking schemes as a tool for locating information. PLoS One 3, e1683 (2008).
- 18. Radicchi, F., Fortunato, S. & Castellano, C. Universality of citation distributions: Toward an objective measure of scientiﬁc impact. Proceedings of the National Academy of Sciences 105, 17268–17272 (2008).
- 19. Ke, Q., Ferrara, E., Radicchi, F. & Flammini, A. Deﬁning and identifying sleeping beauties in science. Proceedings of the National Academy of Sciences 112, 7426–7431 (2015).
- 20. Galenson, D. W. Old masters and young geniuses: The two life cycles of artistic creativity (Princeton University Press, 2011).
- 21. Wang, D., Song, C. & Barab´asi, A.-L. Quantifying long-term scientiﬁc impact. Science 342, 127–132 (2013).
- 22. Way, S. F., Morgan, A. C., Clauset, A. & Larremore, D. B. The misleading narrative of the canonical faculty productivity trajectory. Proceedings of the National Academy of Sciences


(2017).

- 23. Sinatra, R., Wang, D., Deville, P., Song, C. & Barab´asi, A.-L. Quantifying the evolution of individual scientiﬁc impact. Science 354, aaf5239 (2016).
- 24. Simonton, D. K. Scientiﬁc genius: A psychology of science (Cambridge University Press, 1988).
- 25. Duch, J. et al. The possible role of resource requirements and academic career-choice risk on gender differences in publication rate and impact. PloS One 7, e51332 (2012).
- 26. Merton, R. K. The matthew effect in science, ii: Cumulative advantage and the symbolism of intellectual property. Isis 79, 606–623 (1988).
- 27. Price, D. d. S. A general theory of bibliometric and other cumulative advantage processes. Journal of the Association for Information Science and Technology 27, 292–306 (1976).
- 28. Barab´asi, A.-L. & Albert, R. Emergence of scaling in random networks. Science 286, 509–512

(1999).

- 29. Wasserman, M., Zeng, X. H. T. & Amaral, L. A. N. Cross-evaluation of metrics to estimate the signiﬁcance of creative works. Proceedings of the National Academy of Sciences 112, 1281–1286 (2015).
- 30. Uzzi, B., Mukherjee, S., Stringer, M. & Jones, B. Atypical combinations and scientiﬁc impact. Science 342, 468–472 (2013).
- 31. Merton, R. K. Singletons and multiples in scientiﬁc discovery: A chapter in the sociology of science. Proceedings of the American Philosophical Society 105, 470–486 (1961).


- 32. Wuchty, S., Jones, B. F. & Uzzi, B. The increasing dominance of teams in production of knowledge. Science 316, 1036–1039 (2007).
- 33. Clauset, A., Arbesman, S. & Larremore, D. B. Systematic inequality and hierarchy in faculty hiring networks. Science Advances 1, e1400005 (2015).
- 34. Shockley, W. On the statistics of individual variations of productivity in research laboratories. Proceedings of the IRE 45, 279–290 (1957).
- 35. Redner, S. Citation statistics from 110 years of physical review. Physics Today 58, 49 (2005).
- 36. Moreira, J. A., Zeng, X. H. T. & Amaral, L. A. N. The distribution of the asymptotic number of citations to sets of publications by a researcher or from an academic department are consistent with a discrete lognormal model. PloS One 10, e0143108 (2015).
- 37. Palla, G., Barab´asi, A.-L. & Vicsek, T. Quantifying social group evolution. Nature 446, 664–667 (2007).


Acknowledgements The authors thank A.-L. Barabasi, B. Uzzi, W. Ocasio, J. Chown, C. Jin, Y. Yin, and

all members of Northwestern Institute on Complex Systems (NICO) for invaluable comments. This work

is supported by the Air Force Ofﬁce of Scientiﬁc Research under award number FA9550-15-1-0162 and

FA9550-17-1-0089, and Northwestern University’s Data Science Initiative.

Correspondence Correspondence and requests for materials should be addressed to D.W.

(email: dashun.wang@northwestern.edu).

###### Figure captions

- Figure 1: The hot streak phenomenon in artistic, cultural and scientiﬁc careers. a–c, φ(N∗,N∗∗), color coded, measures the joint probability of the top two highest impact works within a career for a artists, b directors, and c scientists. φ(N∗,N∗∗) > 1 indicates two hits are more likely to colocate than random. d–f, we shufﬂe the order of each work in a career while keeping their impact intact, allowing us to measure the null hypothesis of φ(N∗,N∗∗) across three domains, where N∗ and N∗∗ each occurs at random. The diagonal patterns in a–c disappear for shufﬂed careers. g–i, φ(N∗,N∗∗) predicted by the hot-streak model successfully recovers the diagonal patterns observed


in a–c. j–l, R(∆NN ) measures the temporal distance between highest impact works relative to null model’s prediction. Red dots denote measurements from data, showing a clear peak around 0. Solid lines in red are predictions by the hot-streak model. Different shades of red correspond to different pairs of hit works. Blue dots denote the same measurement but on shufﬂed careers, and blue lines are predictions from shufﬂed careers generated by our model. m–o, Deﬁnitions of the longest streak L within a career for m artists, n directors and o scientists. L measures as the maximum number of consecutive works whose impacts are above the median impact of a career (horizontal dashed line denoting the threshold). Above the threshold, dots are colored in orange, and blue for below the threshold. L in the lower panel highlights the longest streak in a career. p–r, The distribution of the length of streaks P(L) for real careers and P(Ls) for shufﬂed careers, for p artists, q directors and r scientists. Red dots capture empirical observations, whereas blue dots correspond to shufﬂed careers. Our hot-streak model (red lines) closely reproduces P(L) observed in data, demonstrating the model’s validity to capture the impact beyond top three highest impact

works across different domains. The shufﬂed version of our model (blue lines) also well captures shufﬂed careers.

- Figure 2: The Hot-streak Model. a–c, Γ(N) for one a artist, b movie director and c scientist, selected from our data for illustration purposes. Γ(N) is calculated by the moving average of impact with a window length = 0.1 × N. d–f, The histogram of the number of hot streaks for


d artists, e directors, and f scientists. g–i, N↑/N measures the position of the work when a hot

streak occurs, among N works in a career. Their cumulative distributions P(≥ NN↑) for g artists, h directors and i scientists are shown in blue dots. The red line captures the cumulative distribution when the start of a hot streak N↑ is distributed randomly among N works. j–l, The duration distribution of the hot streak P(τH) for j artists, k directors and l scientists. Dots are measurements from data. Red lines are log-normal ﬁts as guide to the eye. The median τH are 7.3 years for artists, 7.0 years for directors, and 4.8 years for scientists, respectively. Inset, relative duration distribution P(τH/T) for individuals in three domains, where T is the career length of each individual. Solid lines are lognormal ﬁts as guide to the eye. m–o, The relationship between ΓH and Γ0 for m artists, n directors and o scientists, where the blue background denotes kernel density of data, dots represent binning results of data, and the red line depicts the linear ﬁt. Within each domain, ΓH and Γ0 for individuals with early, middle, and late hot streaks can be well approximated by a linear relationship. Inset, the relationship between ∆Γ (= ΓH − Γ0) and Γ0 for each domain. p–r, The distribution of the number of works produced during hot streaks P(NH), compared with a null distribution, where we randomly pick one work as the start of the hot streak (p artists, q directors, and

r scientists.) We use the Kolmogorov-Smirnov (KS) measure to compare P(NH) of data with the null distribution, ﬁnding that we cannot reject the hypothesis that the two distributions are drawn from the same distribution (p > 0.05).

- Figure 3: Hot streaks govern the collective impact of scientiﬁc careers. a, Screenshot of Albert Einstein’s Google Scholar proﬁle. b, Collective impact of a randomly selected scientist


in our dataset D3. The publication dates are rearranged such as one produces a constant number of papers each year (lower panel). Vertical lines in the lower panel depict when each paper is published after the rearrangement. The color indicates the order of publications, showing that the sequence of papers published in each career remains intact. The solid line indicates that the paper has been published for at least 10 years (dashed line, otherwise) c, For the same scientist as (b), citation patterns of each papers are shown with corresponding colors denoted in the lower panel. The collective impact of a career represents the sum of citation dynamics of all papers published by the individual. d, g(t) modelled by (3) given different hot streak parameters (red lines). Here we use µ = 7.0, σ = 1.0, Γ0 = 1.0, and τH = 3 years but vary t↑ and t↓. Varying hot-streak parameters of g(t) allows us to reproduce a wide variety of career dynamics that cannot be captured by the null model (blue line). Inset decomposes contributions to g(t) in terms of g0(t) and ∆g(t). e, The uncertainty envelope of g(t) for an individual in our dataset, where blue dots denote data, the red line is the ﬁtting result of equation (3), and the shaded area illustrates the predicted uncertainty measured in one standard deviation. f The fraction of g(t) falling within the envelop P(fraction) for the null model (blue area) and our hot-streak model (red area). Fraction = 1.0 indi-

cates the whole g(t) trajectory falls within the envelope. Our model outperforms the null model in capturing individual collective impact as P(fraction) peaks close to 1.0. g, The average MAPE of our hot-streak model and the null model for individuals with early, mid and late onset of hot streaks. The difference between the two models is the largest for individuals with early hot streak and smallest for late ones. h, g(t) of 50 randomly selected individuals in our dataset whose careers started between 1960 and 1995. Color corresponds to the year when a career started, dots denote collective impact of real careers, and solid lines capture the predictions from the hot-streak model.

### Artists Directors Scientists

a b c

![image 1](Hot streaks in artistic cultural and scientific careers_images/imageFile1.png)

![image 2](Hot streaks in artistic cultural and scientific careers_images/imageFile2.png)

![image 3](Hot streaks in artistic cultural and scientific careers_images/imageFile3.png)

Empirical

d e f

![image 4](Hot streaks in artistic cultural and scientific careers_images/imageFile4.png)

![image 5](Hot streaks in artistic cultural and scientific careers_images/imageFile5.png)

![image 6](Hot streaks in artistic cultural and scientific careers_images/imageFile6.png)

Shuffled

g h i

Hot-streak Model

![image 7](Hot streaks in artistic cultural and scientific careers_images/imageFile7.png)

![image 8](Hot streaks in artistic cultural and scientific careers_images/imageFile8.png)

![image 9](Hot streaks in artistic cultural and scientific careers_images/imageFile9.png)

j k l

m n o

p q r

23

Figure 1:

#### Artists Directors Scientists

a b c

Hot-streak model Hot-streak model Hot-streak model

d e f

# of hot streaks # of hot streaks # of hot streaks

g h i

j k l

m n o

p q r

24

Figure 2:

![image 10](Hot streaks in artistic cultural and scientific careers_images/imageFile10.png)

b c

a b c

![image 11](Hot streaks in artistic cultural and scientific careers_images/imageFile11.png)

| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|


| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|


e g

d f

Hot-streak model Hot-streak model

h

Figure 3:

25

## Supplementary Information for Hot Streaks in Artistic, Cultural, and Scientiﬁc Careers

Lu Liu,1,2,3 Yang Wang,1,2 Roberta Sinatra,4 C. Lee Giles,3,5 Chaoming Song,6 Dashun Wang1,2∗

1Northwestern Institute on Complex Systems, Northwestern University, Evanston, IL, USA 2Kellogg School of Management, Northwestern University, Evanston, IL, USA

- 3College of Information Sciences and Technology, Pennsylvania State University, State College, PA, USA
- 4Center for Network Science and Mathematics Department, Central European University, Budapest, Hungary
- 5Department of Computer Science and Engineering, Pennsylvania State University, State College, PA, USA
- 6Department of Physics, University of Miami, Coral Gables, FL, USA


*Correspondence should be addressed to D.W. (dashun.wang@northwestern.edu)

## Contents

###### S1 Data Description 4

- S1.1 Artists D1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
- S1.2 Movie directors D2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
- S1.3 Scientists D3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
- S1.4 Data Limitations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10


###### S2 Empirical Measurements 12

- S2.1 Impact distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
- S2.2 Random impact rule . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
- S2.3 Φ for other pairs of hit works . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
- S2.4 Measurement under different career length . . . . . . . . . . . . . . . . . . . . . . 14
- S2.5 P(L) under different threshold . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
- S2.6 Difference between P(L) and P(LS) . . . . . . . . . . . . . . . . . . . . . . . . . 15


###### S3 Hot-streak Model 16

- S3.1 Hot streak studies in the literature . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
- S3.2 Null model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
- S3.3 Generative hot-streak model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
- S3.4 Estimation of hot streaks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
- S3.5 Model validation: Fitting performance . . . . . . . . . . . . . . . . . . . . . . . . 19
- S3.6 Model validation: Impact before and after a hot streak . . . . . . . . . . . . . . . . 20
- S3.7 Individuals with different number of hot streaks . . . . . . . . . . . . . . . . . . . 21
- S3.8 The correlation between Γ0 and ΓH . . . . . . . . . . . . . . . . . . . . . . . . . . 22
- S3.9 Discussion on scientiﬁc disciplines . . . . . . . . . . . . . . . . . . . . . . . . . . 22


###### S4 Relationship with Existing Models 23

- S4.1 Compare Γ and Q parameter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
- S4.2 Q-model validation for scientists . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
- S4.3 Q-model validation for artists and directors . . . . . . . . . . . . . . . . . . . . . . 26


- S5 Model for Individual Collective Impact 28 S5.1 g(t) deﬁnition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28 S5.2 Modulate paper citation with Γ(t) . . . . . . . . . . . . . . . . . . . . . . . . . . 29 S5.3 g(t) under the null model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30 S5.4 g(t) under hot-streak model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31 S5.5 Parameter estimation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33 S5.6 Model validation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
- S6 Testing Alternative Hypotheses 34


###### S1 Data Description

In this project, we compiled a comprehensive database consisting of three large-scale datasets of

individual careers across three different domains: Dataset D1 contains proﬁles of artists obtained from online auction databases. Dataset D2 contains proﬁles of movie directors recorded in the IMDB database. Dataset D3 contains the publication and citation records of individual scientists, obtained by combining Google Scholar and Web of Science. In this section we describe in detail how we collected and reconstructed individual career histories for the three datasets.

- S1.1 Artists D1 Among the three domains we analyzed, the success of artists is probably the most difﬁcult to quantify, hence unsurprisingly the least studied. Indeed, apriori, it may seem that the success of an artist is inherently unquantiﬁable. Yet more recent developments start to suggest that several measures have the potential to be systematically collected and can be used to measure and compare the impact of artworks20. The various measures include auction hammer prices, being selected as illustrations in art textbooks, retrospective exhibitions, museum collections and exhibitions. Just like citations—which have by now been commonly adopted to quantify success of a paper and scientist, despite the fact that they offer at best an incomplete measure of impact that is inherently multi-faceted—these measures of artistic success each capture at best a singular dimension that is to certain degree correlated with the overall “goodness” of an artwork, with their associated limitations (Sec. S1.4). Among all measures, hammer prices are the most commonly used to quantify artistic success20, perhaps because they reﬂect the values of artworks judged by art professionals and art markets, serving as a proxy for the impact of artworks. While there are


studies showing the career trajectories of artists are rather robust against different measurement choices20,38, here to ensure our ﬁndings are consistent with the state of art, we seek to collect systematically hammer prices of artworks from different sources to reconstruct artistic careers.

We collected information on artistic careers from online art market databases, Artprice1 and Findartinfo2. Both websites offer a comprehensive list of auction records for each artists, with complementary information on various kinds of ﬁne arts ranging from old masters to contemporary art. Indeed, auction records on Artprice offer several useful information that can help quantify artistic careers, including, for each artwork, its auction date, title, year of production, medium, and the price rank among all hammer prices of artworks produced by an artist. Findartinfo contains information on auction date, title, medium, and the actual hammer price for each auction. In this study, we combined the two data sources, allowing us to extract the most comprehensive information tracing individual artistic careers.

Artworks can go through multiple auctions. Artprice website contains auction records from 1983 up to now, helping us ensure that we analyze the latest sales of each artwork. Findartinfo also offers auction records from 2001 till 2015, including the actual hammer price for each record, allowing for cross check and references. Both databases are excellent in their longitudinality, containing artworks produced dating back to the Middle Ages.

In total, we collected 31,101 individual proﬁles from Artprice and 283,839 proﬁles from

- 1www.artprice.com
- 2www.ﬁndartinfo.com


Findartinfo. Artprice indexed a large number of artists, but here we focused on the top ones with more than 50 records. We conducted a comprehensive entity linking process between the two databases, aiming to match each artist in Artprice with the corresponding proﬁle in Findartinfo. We ignore proﬁles from the two databases noted as “attributed to” or “attrib.”, since these notions suggest sellers are not clear about the authorship of these artworks. We then cluster remaining proﬁles with the same last name together in each database, allowing us to match artists within a small subset for computational efﬁciency. We compare each artist’s proﬁle in Artprice with each proﬁle in Findartinfo with the same last name. Two artists are considered to be the same if they satisfy the following criteria: 1) Initials of the ﬁrst names are the same. If full names are available for both artists, they have to be identical; 2) They have at least one artwork with an identical title; 3) If more than one artists meet criteria 1) and 2), we pick the one with most matched titles. By applying this entity resolution procedure, we end up with a total of 5,352 matched artists. To evaluate the accuracy of our algorithm in linking the two databases, we compare the number of works for all matched artists in Findartinfo and Artprice in the same period (2001–2015), ﬁnding the number of works in the two databases to be similar (Fig. S1).

After linking the two databases, we reconstruct the career histories of artists based on the production year of each work and its hammer price during most recent auction. If an artwork is included in the original Findartinfo dataset, the actual hammer price is used to measure the impact of the artwork. If an artwork is only included in the Artprice dataset, we know the price rank of the artwork among all artworks by the artist. Hence if we need to compute the actual hammer price, we can convert sales rank using rank-to-score conversion given the price distribution measured

in Findartinfo39. Note that, the uncovered hot streaks documented in the main text (Fig. 1) are independent of whether we use price or rank because the choice does not affect the measurements of relative positions between hit works within each individual. When an artwork was produced during several years, we use the last year as its year of production, corresponding to the year in which the work was ﬁnalized. For our ﬁnal dataset, we selected artists with at least 15 works and 10 years of career length, resulting in 3,480 artists, with careers dating back to as far as 1460.

- S1.2 Movie directors D2 The Internet Movie Database (IMDB)3 is the largest movie database around the world, containing information about over one million movies, spanning over 20 genres from 1874 to present. Each movie in the database includes detailed information such as title, release time, casts, crews, an average user rating and the number of votes. IMDB also contains over eight million personal proﬁles with unique identiﬁers, each containing personal information, a list of works she was involved in, and speciﬁc roles in these works, such as being a director, editor, writer, actress, etc. Although a movie is inherently a product of complex collaborative efforts often involving a large number of individuals, the director of the movie is commonly considered to play a prominent role in cinematic creativity40,41.


To this end, we gathered 513,306 movie records and proﬁles of 20,592 directors from IMDB, including those who serve as an assistant director and art director. IMDB provides a rating system for each movie that ranges from one to ten, reﬂecting the “crowd wisdom” of users, adjusted by the weighting algorithms developed by IMDB to avoid vote stufﬁng. Previous work has found

3http://www.imdb.com/interfaces/

that metrics quantifying the impact of a movie largely correlate with each other30. Here, we use the IMDB rating to approximate the impact of a movie, and construct the sequence of works with their impacts for each director in our dataset. We focused on movies released before 2017 with more than 5 votes. To select directors with long enough career histories, we focused on those who have at least 15 movies and 10 years of career length, resulting in a total of 6,233 directors, whose careers dating back to as far as 1890 (D2).

- S1.3 Scientists D3 For studies on scientiﬁc careers, automated name disambiguation in largescale scholarly datasets remains a challenging problem42,43. In this study we perform a large-scale disambiguation effort by combining two large datasets, Google Scholar (GS) and Web of Science (WoS). Google offers scholar proﬁle services for individuals scientists to create, maintain, and update their own publication records, assisted by its disambiguation algorithms. Users can adjust the publication records recommended by Google, further ensuring the accuracy and reliability of each proﬁle. Hence, GS offers a comprehensive dataset of individual scientiﬁc proﬁles across different domains that should be at least as accurate as the state of the art, with additional two levels of assurance. As such it has the potential to catalyze more and more research on scientiﬁc careers23,44,45.


To this end, we crawled over 240,000 public proﬁles from GS in summer 2015. Each GS proﬁle contains the publication records of a scientist, including for each paper its title, publication year, journal, author(s) and cumulative citation count within GS database calculated up to the point when the data was collected. GS encourages users to enter other information including afﬁliation,

research interest, homepage, and collaborators. Users with veriﬁed academic email address are noted in their GS pages. Here, we choose those with veriﬁed email address and co-authors as they are considered well-maintained. We further remove individuals with more than 1,000 publications in GS, ﬁnding most of them have Asian names which are the most difﬁcult to disambiguate. Here again the goal is to follow closely the same procedures used by existing studies in this area23,44,45, so that every ﬁnding in our paper is immediately comparable with previous literature to ensure our results are consistent hence new ﬁndings reliable given the existing literature.

Since GS only provides the cumulative citation count of each paper by the time of data collection, to study the dynamical impact of each scientist we linked GS with the WoS dataset, which provides comprehensive citation records of around 46 million journal papers published after 1900. For each scientist, we match each publication in her GS proﬁle with the corresponding paper in WoS. We conducted a comprehensive linkage process that takes into account not only the author name and paper title, but also the metadata available for each publication. For each scientist in GS we ﬁrst consider a pool of WoS papers having an author with the same last name. Then for each publication in her GS proﬁle, we calculated the cosine similarity between the title of each GS record and each WoS paper in the subset. We then consider a record in GS proﬁle matched with a WoS publication if the following criteria are met: 1) The WoS paper was published within ±2 years of the GS publication year; 2) There is at least one co-author sharing the same last name in GS and WoS if the paper has more than one authors; 3) The cosine similarity between titles is higher than 0.5 after removing stop words. If there are multiple papers, we choose the one with the most similar title (highest cosine similarity). If, using these criteria, we could not ﬁnd a

corresponding paper in WoS, we consider the GS record is not matched to ensure the quality of the resulting dataset. We choose scientists with at least 15 papers and 20 years of career length, resulting in 20,040 proﬁles for our analyses (D3).

To approximate the impact of each paper, we follow recent studies17,21,23 to calculate the number of citations the paper received after 10 years of publication C10. Previous studies have shown that for WoS dataset the average citation counts of a paper increase over time18,23,46, which we veriﬁed to be the case for our dataset (Fig. S2). To make sure our results are not affected by this temporal effect, we follow previous studies18,23 and use a rescaled C10, deﬁned as C10/ C10 y, to gauge the impact of a paper, where C10 y is the average impact of all papers in WoS published in the same year y. We report in S2 and Fig. 1 the results based on the rescaled C10. We ﬁnd the use of raw or rescaled C10 does not alter our conclusions.

- S1.4 Data Limitations Although the datasets curated in our study are among the largest collections of individual careers, our data are not without limitations. While auction data are most commonly used to quantify impact of an artwork, it is important to understand a potential bias involved in using auction data to measure and compare the relative value of an artwork20. This issue is of particular relevance for famous artists, whose work is eagerly sought after by museums. While museums sometimes take part in auctions, they are in general less likely to sell a collection. The “museum bias” may also affect works differently. For example, if we consider the probability that an oil painting may be owned by a museum, late paintings tend to have a higher probability than early paintings. Also museums may not take paintings randomly from a career, but are rather


biased toward the best works. Hence the hits we observed in some careers may represent a lower bound of the real number of hits. But thankfully, we ﬁnd our results are rather robust when we vary the threshold for hits. Despite these limitations, one possible reason why auction prices remain the best measures to quantify the importance of artworks is rooted in the fact that they are signiﬁcantly better than alternatives. For example, other measures like museum exhibitions mainly focus on masterpieces of famous artists, limiting the scope and data availability for quantitative analysis.

Datasets about movies and scientiﬁc publications are more frequently studied quantitatively than artworks, hence the metrics used in those cases are better deﬁned. But it is still important to remember that similar biases also exist. For example, the IMDB rating could be biased toward the judgement of general audience, whereas professional ﬁlm critics may have different opinions. Papers could be highly cited for many reasons. There are many scientiﬁc discoveries that are ground-breaking but have few citations.

Lastly, for any study regarding individual careers, name disambiguation is always an issue that should not be overlooked. For the three domains analyzed here, name disambiguation issues may potentially affect results regarding artists and scientists, but less so for movie directors, as they are associated with unique identiﬁers. Another issue when studying individual careers is that, as we need enough records to study each individual, the insights obtained are inherently biased towards productive individuals who have produced much with long enough careers.

Amid all the limitations described in this section, it should be clear, however, that these limitations are by no means unique to our study; Rather, they apply to most, if not all studies in

this domain. In many ways, research progress on individual careers is hindered by the inherent difﬁculties to collect and curate high-resolution individual career histories from diverse domains. Hence another contribution of our paper is to make available to broad research communities the comprehensive datasets we collected in this paper. By doing so, the hope is that these datasets could be an important asset for researchers from many different disciplines as they signiﬁcantly improve the data-scarce situation, allowing researchers to build and develop new ﬁndings. To this end, we created a dedicated website to host datasets and descriptions, with the hope to update them as they develop. The website can be access here http://personal.psu.edu/ lpl5107/data/data/data/.

###### S2 Empirical Measurements

- S2.1 Impact distribution We use auction hammer price, IMDB rating, and paper citation in 10


years C10, to approximate the impact of works for artists, movie directors, and scientists, respectively.. To study the work impact across three domains, we measure the distribution of hammer prices, IMDB ratings and paper citation count in our datasets, ﬁnding they follow quite different distributions. The hammer price for all artworks in our dataset can be approximated by a lognormal distribution (Fig. S3a) following

1 x√2πσ

P(x) =

(log x−µ)2

e−

2σ2 (S1)

We ﬁt Eq. S1 to P(price) measured from data, and obtain the estimated parameters µ = 7.91 and

σ = 1.55. Similarly, we ﬁnd the distribution for both raw and rescaled C10 in our dataset also follows a log-normal distribution (Figs. S3c–d), which is consistent with previous studies17,18,23. In contrast, the IMDB rating follows a normal distribution ranging between 1 and 10 (Fig. S3b).

Hence, to study the impact across three domains, we deﬁne a goodness parameter Γ for artists,

directors and scientists as log(price), IMDB ratings and log(C10), respectively.

- S2.2 Random impact rule One school of thought on the lifecycle of creative careers suggests a hit work within individual career is largely driven by chance, having a constant probability to appear in unit of works within each career13,23,47,48. To verify this hypothesis in our dataset, we study the position Ni of each top i highest-impact work in the sequence of N works within each career, and measure the complementary cumulative distribution function P(≥ Ni/N) within the sequence of works produced by individuals in different domains. We ﬁnd for each of the top 3 hit works in an artistic career, P(≥ Ni/N) decreases linearly as (Ni/N)−1, corresponding to a uniform P(Ni/N) (Fig. S4a), suggesting the most expensive works of an artists is randomly distributed within her career. Similarly, we ﬁnd the same pattern of P(≥ Ni/N) for directors and scientists (Figs. S4b–c), suggesting the highest rated movies and the most cited papers also appear randomly within each career. Hence, random impact rule applies across three domains.
- S2.3 Φ for other pairs of hit works In the main text, we observed the normalized joint probability Φ(N∗,N∗∗) is overrepresented along the diagonal for artists, directors and scientists, suggesting the colocation of the top two hit works within a career. To study if the colocation applies to other pairs of hit works, we calculate the normalized joint probability Φ(N∗,N∗∗∗) for the highest and third highest impact works, and Φ(N∗∗,N∗∗∗) for the second and third highest impact works within each career across three domains. We ﬁrst measure Φ(N∗,N∗∗∗) and Φ(N∗∗,N∗∗∗) in real careers (Fig. S5), ﬁnding a similar diagonal pattern for Φ(N∗,N∗∗∗) and Φ(N∗∗,N∗∗∗), indicating


- the temporal collocation applies to other pairs of hit works. Φ(N∗,N∗∗∗) and Φ(N∗∗,N∗∗∗) both feature an even split across the diagonal, suggesting the equal probability of each hit to appear before or after another hit. We ﬁnd the colocation of other pairs of hit works is less signiﬁcant than the top two hits (lighter color along the diagonal), which is also consistent with the lower peak value of R(∆N/N) in Figs. 1j–l. However, if we shufﬂe the order of works within each career while keeping their impact intact, the diagonal pattern of Φ(N∗,N∗∗∗) and Φ(N∗∗,N∗∗∗) disappears across three domains (Fig. S6), suggesting the colocation of any pair of hit works observed in data cannot be explained by the random impact rule.
- S2.4 Measurement under different career length The empirical observations in Fig. 1 are based on artists and directors with at least 10 years of career length, and scientists with at least 20 years of career length. To study if the random impact rule and the temporal correlation of hit works is inﬂuenced by the career length we measured, we selected two groups of individuals with longer career length in each domain: artists with at least 20 and 30 years of career length, directors with at least 20 and 30 years of career length, and scientists with at least 30 and 40 years of career length, and repeated the empirical measurements on the random impact rule and the temporal colocation for the two groups of individuals in each domain. First, we ﬁnd the P(≥ Ni/N) still follows a uniform distribution given different career length for artists, directors and scientists (Fig. S7), suggesting the random impact rule is independent of the career length we measured. Second, we calculate the temporal distance R(∆N∗/N) for the hit and second hit within a career, where ∆N∗ is deﬁned as N∗ − N∗∗. We ﬁnd R(∆N∗/N) peaks around zero featuring a symmetric split along the x-axis (Fig. S8), suggesting the colocation of hit works is not inﬂuenced by career length.


- Third, we ﬁnd the tail of both P(L) and P(LS) follows an exponential distribution. P(L) features a much wider than P(LS) (Fig. S9), suggesting the long streaks sustain in careers of different length.
- S2.5 P(L) under different threshold We have studied the streak of works above the median impact within a career in Fig. 1, ﬁnding P(L) observed in real careers has a longer tail than that of shufﬂed careers. To test if the conclusion is robust to different choices of impact threshold, we changed the threshold to the mean impact and geometric mean of impact within each career for

artists, directors, and scientists. We ﬁnd similar results for P(L) and P(LS) given different impact threshold.

- S2.6 Difference between P(L) and P(LS) To quantify the different probabilities to observe streaks for real and shufﬂed careers (Figs. 1p–r), we measured P(L)/P(LS), capturing how more likely it is to observe streaks than random at different streak length. Since we care about the prob-


ability of long streaks, we focus on the tail of P(L) and P(LS), and ﬁt their tails to an exponential distribution. We then compare the tail difference of P(L) and P(LS) based on the ﬁtting results across three domains (Fig. S11). We ﬁnd for artists and scientists, the probability for an individual to produce consecutive 20 high impact works above the median impact within a career, is around 20 times more likely than shufﬂed careers. The probability is over 100 times more likely for directors.

###### S3 Hot-streak Model

- S3.1 Hot streak studies in the literature The debate on hot streaks dates back to 1985, when Gilovich et al. presented that the hot-hand belief on basketball players is merely a cognitive bias of random process1 . Since then, hot hand has been widely studied in sports, ﬁnancial markets and gambling. These studies tried to answer two fundamental questions: 1) the statistical evidence on whether the hot hand exists1–3, and 2) the psychological origin of the hot hand belief1,49–52. Here we conduct a comprehensive review of the existing literature related to the ﬁrst question. Table S1 reviews selected empirical studies of whether hot hand exists. Table S2 reviews different mathematical models to detect hot hand. Hot hand has been measured and reported by independent research groups, each using different datasets and statistical models mainly in sports, ﬁnancial markets and gambling. In this study, we extend the analyses on hot hand to different domains, focusing on individual creative careers.


- S3.2 Null model To uncover the regularities behind the empirical observations, we ﬁrst introduce a null model motivated by the random impact rule. That is, we assume each individual i produces a sequence of N works whose impact (i.e.. log(price) for artists, ratings for directors,


and log(C10) for scientists) is randomly chosen from an impact distribution P(Γ) = N(Γi, σi2), where Γi is a constant goodness parameter speciﬁc to each individual, and σi reﬂects the impact ﬂuctuation within each career. For simplicity, we assume σi to be the same for each individual in a domain. The null model allows us to simulate impacts of the works produced by an individual. For each individual, we use real productivity N as input, and assume Γi as the average impact

measured from each individual, and σi = 1.0 is a constant for all the individuals. We repeated the measurements of P(≥ Ni/N) and Φ to verify its prediction on the random impact rule and the temporal correlation, ﬁnding the null model can reproduce the random impact rule of the top three hit works across three domains (Fig. S12), while it fails to capture any temporal clustering among hits (Fig. S13), suggesting that there are other factors affecting individual careers.

- S3.3 Generative hot-streak model The failure of the null model prompts us to abandon our


hypothesis that Γi is constant with each career. Each hit work is random while their relative position is not, indicating the presence of a period of outstanding performance (ΓH) that appears randomly with a career. Using real productivity N as input, the hot-streak model allows us to generatively simulate the impacts of the works produced by an individual. For each individual i, the impact of a work is randomly drawn from a normal distribution N(ΓH, σi2) if it is produced during hot streaks, or N(Γ0, σi2) otherwise. To deﬁne a random hot streak in each career, we randomly pick one work out of the sequence of N works she produced, and denote its year of production as t↑, marking the start of the hot streak. For simplicity, we assume Γ0, ΓH, σi, and τH = t↑ − t↓ to be the same for each individual in a domain. The result reported in Fig. 1 is based on the following parameters: Γ0 = 6.9, σ = 1.1 and τH = 6 years for artists; Γ0 = 6.5, σ = 1.1 and τH = 6 years for directors; and Γ0 = 3.0, σ = 1.3 and τH = 4 years for scientists, with ΓH = Γ0 + 1.0 for individuals in all three domains. Although it is a simple generative model with four parameters, our hot-streak model can reproduce all the empirical ﬁndings measured from a variety of individual careers.

- S3.4 Estimation of hot streaks In order to test how well our hot-streak model matches empirical data, we need to estimate the model parameters for each individual. We show in this section that the impact of works within a career can be captured by a time-dependent variable Γ(N), deﬁned


as the average of impact calculated by rolling a window of size ∆N = max(5,0.1NT) over an individuals sequence of works, where NT is the total number of works produced by an individual. In order to capture the average performance during a period, we assume the window size to account for 10% of all the works one produced, and set the lower bound of ∆N as 5 in order to calculate Γ(N) based on enough works. In order to remove any potential boundary effect, we calculate Γ(N) from ∆N/2, whose value is deﬁned by the average Γ between 0 and ∆N, and then move the sliding window one work per step until NT − ∆N/2. Γ(N) reﬂects the average impact of works between N−∆N/2 and N+∆N/2. Γ(N) is calculate from log(price) for artists, IMDB ratings for directors, and the raw log(C10) sequence for scientists. We ﬁnd for scientists calculating the raw or the rescaled C10 does not alter the trend of Γ(N) (Fig. S14a). Indeed, we measure the Pearson correlation between the Γ(N) sequence calculated from raw log(C10) and rescaled log(C10) for each individual, ﬁnding the distribution of correlation coefﬁcient P(ρ) peaks around 1 with mean value 0.93 (Fig. S14b), suggesting the two sequences are highly correlated and the rescale does not change the trend of Γ(N) in general. Since the raw log(C10) is easier to interpret, we report results related to Γ(N) based on the raw log(C10).

For each individual in our dataset, we use a piecewise function to ﬁt the sequence of Γ(N) measured from real careers. Speciﬁcally, we relax the number of hot streaks to at most three, and

allow the ΓH of each hot streak to be different. We used ordinary least square (OLS), and adopted

scipy.optimize package to ﬁt the piecewise function to data. Besides, to overcome the over-ﬁtting problem, we added the L1 regularization term to the cost function that penalizes the number of hot streaks. For each individual, we repeated the ﬁtting procedures for 20 realizations, and selected the results with the smallest cost. We show more ﬁtting results for individuals across three domains in Figs. S15–S17. To deﬁne the hot streak in each career, we assume the smallest ﬁtted Γ(N) as Γ0 for an individual. To make sure the ﬁtted hot streak reﬂects a substantial period of improved performance, we set a threshold for both the duration and the intent of each hot streak. Speciﬁcally, for any Γ larger than Γ0, if the difference between the two is larger than the inherent noise within a career (standard deviation of Γ(N)), we then deﬁne it as a hot streak. Besides, we assume ΓH should at least last for 5 works, otherwise we think the duration is too short, and regard it an outlier of normal performance.

- S3.5 Model validation: Fitting performance To systematically evaluate the goodness of ﬁtting for the procedure proposed above, we measure the difference between ﬁtted and real Γ(N) by calculating the coefﬁcient of determination R2. To study if R2 between ﬁtted and real Γ(N) can be explained by the inherent noise of Γ(N) sequence, we calculate the expected value of R2 generated by the inherent noise of the impact sequence. To do so, we use ﬁtted Γ(N) as input, and simulate the impacts of works within a career for each individual, by assuming the impact of each work is


randomly selected from a normal distributions N(ΓH, σs2) if it was produced during hot streaks, or from N(Γ0, σs2) otherwise. We assume σs to be the same for all individuals in a domain.

To determine the value of σs, we calculate the difference σ between the real Γ(N) and ﬁtted

Γ(N), and measure the distribution P(σ) for all individuals in each domain. We ﬁnd P(σ) follows a normal distribution that peaks around zero for artists, directors and scientists (Fig. S18). The standard deviation for P(σ) is 0.186 for artists, 0.229 for directors, and 0.189 for scientists. We approximate the standard deviation for P(σ) as the noise in each domain, respectively. Using these numbers as input, we simulated the impacts of works within a career for 1000 realizations, allowing us to calculate a distribution P(R2) for each individual. To study if R2 of real and ﬁtted Γ(N) can be explained by noise, we deﬁne a baseline R2 that is the lowest 5% of all simulated R2 (p-value = 0.05). If the R2 of data and ﬁtted Γ(N) is larger than the baseline R2, we assume the error is mainly generated by noise, and Γ(N) is well captured by our hot-streak model (Fig. S19). We ﬁnd for individuals in our dataset, over 69% artists, 80% directors and 75% scientists have R2 larger than the baseline R2, suggesting our hot-streak model captures the majority of individuals in our dataset.

We also compared the ﬁtting performance of our hot-streak model with the null model by calculating adjusted R2 and Bayesian information criterion (BIC), both penalizing the number of parameters in the model. Compared with the null model, we ﬁnd our hot-streak model has systematically larger adjusted R2 and smaller BIC for individuals across three domains (Fig. ??), suggesting out hot-streak model better captures the dynamics of Γ(N) than the null model.

- S3.6 Model validation: Impact before and after a hot streak Our hot-streak model assumes that after a hot streak, the individual performance returns back to her normal performance. To test this assumption, we measure for each individual the average impact of all works produced during


- the normal performance before and after each hot streak, where the normal performance and the hot streak is deﬁned by the ﬁtted Γ(N). We calculate the distribution of the difference between average impact before and after the hot streak P(∆ Γ ) that ∆ Γ = Γ after −  Γ before, ﬁnding P(∆ Γ ) follows a normal distribution peaks around zero (Fig. S20) for individuals across three domains, suggesting there is no systematic different between the average impact before and after a hot streak.
- S3.7 Individuals with different number of hot streaks In this section, we discuss if there is any difference among individuals with zero, one and more than one hot streaks across three domains. We ﬁrst compare the distribution of average impact P(Γ), the number of works P(N), and the career length P(T) for individuals with and without hot streaks, ﬁnding there is no signiﬁcant difference in terms of impact, productivity and career length between the two groups of people


(Fig. S21). However, we observe differences in the distribution of Γ0 and ΓH for individuals with different number of hot streaks. Indeed, for scientists and directors, P(Γ0) is smaller for individuals with one hot streak than without hot streaks (Figs. S22b–c), and P(ΓH) is higher for individuals with more than one hot streaks (Figs. S22e–f), reﬂecting the inherent variance of impact within a career for directors and scientists. While we ﬁnd for artists the distribution P(Γ0) and P(ΓH) is the same for those who different number of hot streaks. The difference between artists and the other two domains is probably due to the relation between Γ0 and ΓH, that it is more difﬁcult for individuals with high Γ0 to gain better performance during hot streaks for directors and scientists. Hence, the number of hot streaks with a career captures an orthogonal dimension to current metrics characterizing individual careers.

- S3.8 The correlation between Γ0 and ΓH To avoid potential bias that our results in Figs. 3M–O are affected by the underlying distribution of Γ0 and ΓH, we repeated our analysis on the relation of Γ0 and ΓH by using the their percentile, ﬁnding the linear relationship between Γ0 and ΓH remains the same for individuals across three domains (Fig. S23), suggesting our conclusion is insensitive

to the distribution of Γ0 and ΓH.

To test the signiﬁcance of the correlation between Γ0 and ΓH observed in data, we propose a null model that assumes they are uncorrelated. Speciﬁcally, we assume for the null model that

ΓH and Γ0 follow the same distribution. For a given Γ0, ΓH is calculated as the expectation of P(Γ) ranging from Γ0 to inﬁnity under the null model. We ﬁnd the null model prediction of ΓH for a given Γ0 is much higher than the real ΓH, suggesting the impact during hot streaks of each individual cannot be explained by chance, but largely depends on her normal performance.

- S3.9 Discussion on scientiﬁc disciplines To compare the hot-streak properties for scientists from different disciplines, we identify each scientist her discipline by using the scientiﬁc journal


categories provided by WoS18. The publications collected in D3 belong to journals from 145 different categories in WoS ranging from Acoustic to Zoology. For each scientist, we count the number of papers published in each of the 145 categories. Since a journal may belong to multiple categories, and each category includes a list of journals, we count each paper multiple times in all related categories. We consider the category with the most publications within a scientiﬁc career as her research discipline. Hence, each scientist in our dataset can be only assigned to one discipline. Here we study the top 30 disciplines with the most scientists in our datasets. We ﬁnd the ratio of

scientists with one hot streak to be stable across disciplines, accounting for roughly 60% within each discipline (Fig. S24a), where the ratio is highest (up to 70%) for scientists from oncology, and the lowest (around 50%) for scientists from ophthalmology. We also calculate the average duration of the hot streak τH for scientists from 30 disciplines (Fig. S24b), ﬁnding scientists from geophysics have on average the longest hot streak (around 7.5 years), whereas scientists from chemistry have the shortest hot streak on average (around 3 years). The robustness across different disciplines indicates the generalizability of the hot-streak model.

###### S4 Relationship with Existing Models

In this section, we discuss the relationship between the proposed hot-streak model with previ-

- ous studies on the individual impact. Here we will focus on the most recent model, namely the Q-model23. Different from the assumption that scientists with similar productivity have indistinguishable impact, the Q-model suggests the existence of a hidden parameter Q unique to each individual. Although the hot-streak model builds upon a similar conceptual basis to the Q-model, the main ﬁndings of our model demonstrate that the Q-model is not sufﬁcient to capture the impact dynamics within each career. The reason is simple: the Q-model is mainly designed to capture the impact differences across individuals, focusing on the overall performance of an individual rather than the how impact changes within a career, which is the focus of our paper. Next we show in this section the mathematical consistency between our hot-streak model and the Q-model. As such, the hot-streak model not only helps us explain the temporal regularities documented in the main text not anticipated by the Q-model, but is also able to reproduce all the predictions the Q-model


makes on individual careers.

- S4.1 Compare Γ and Q parameter The Q-model models the citation after 10 years C10 of a paper α for a scientist i as the multiplication of two parts23:


###### C10,iα = Qipα, (S2)

where Qi is a individual-speciﬁc parameter, and pα is the luck component that is same for every individual. The Q-model assumes Qi to be a constant over time for each individual, and pα follows a log-normal distribution that P(log p) = N(µp,σp) same to all scientists. Hence, we can take the logarithms of Eq. S2 that log(C10,iα) = log(Qi) + log(pα). Noting that C10, pα and Qi all follow a log-normal distribution, the impact of a paper produced by a scientist i is randomly drawn from a normal distribution that

P(log C10,iα) = N(µp + log Qi,σp), (S3) whose mean value is modulated by the individual-speciﬁc Qi parameter. Comparing Eq. S3 with the deﬁnition of Γ parameter in S2.1, we ﬁnd our Γ parameter can be expressed as

###### Γiα = log(Qi) + µα. (S4)

Hence, the Γ parameter combines the two parts in the Q-model, reﬂecting both the individual differences and the luck component.

The hot-streak model contains all the ingredients of the Q-model, while it also captures the temporal colocation of hit works within a career by introducing a temporal variation of Γ, allowing

an individual to improve her typical performance (Γ0) to a higher level (ΓH) for a while. With this

simple modiﬁcation, we show, for the ﬁrst time, that the dynamics of impact within an individual

career is characterized by a remarkable degree of regularity. The idea behind changing Γ0 to ΓH is the improvement of individual skill from Qi to a higher value. It is also worth noting that the duration of a hot streak is relatively short compared to the career length we measured, usually lasting for 5 years or accounting for 20% works produced by a scientist. Hence, our hot-streak model can be approximated as the Q-model in the long run. In sum, our hot-streak model is consistent with the Q-model, in terms of the deﬁnition of Γ parameter, and the generative process of impacts within a career.

- S4.2 Q-model validation for scientists In this section, we validate the Q-model for scientists in our dataset. We also demonstrate the hot-streak model successfully reproduces all the Q-model predictions on the impact across scientists. To validate the Q-model in our dataset, we ﬁrst cal-


culated the distribution of impact and productivity, ﬁnding P(log(C10)) and P(N) both follow a log-normal distribution that meets the assumption of the Q-model (Fig. S3c, Fig. S25a). We then used the maximum likelihood method to estimate the parameters µ and Σ of the trivariate normal distribution P(log p,log Q,log N) ∼ N(µ,Σ) in the Q-model. The estimated parameters for the joint probability P(log p,log Q,log N) is

µ = (µp,µQ,µN) = (1.39,0.72,3.43)









σp2 σp,Q σp,N σp,Q σQ2 σQ,N σp,N σQ,N σN2

1.67 0.009 0.002

Σ =

=

0.009 0.56 0.11 0.002 0.11 0.77

 

 

 

 

(S5)

The matrix Eq. S5 is consistent with the Q-model that σp,Q = σp,N ≈ 0. The estimated Q parameter also follows a log-normal distribution (Fig. S25b).

The Q-model successfully explains the impact differences across individual scientists by capturing the scaling of C10∗ with productivity N and with the logarithm of the average impact without the hit C10−∗ 23. To validate the Q-model in our dataset, we calculated the predictions of the Q-model by using Eq. S5, and compared them with the empirical observations, ﬁnding the results of the Q-model are aligned with data for the relationship between C10∗ and N, C10∗ and

C10−∗ (Figs. S25c–d). Besides, to test if our hot-streak model can capture the predictions made by the Q-model, we simulated the impacts of each scientists using the generative hot-streak model

described in Sec. S3.3, and repeated the analyses for C10∗ between N and C10−∗ . We ﬁnd our hot-streak model can also capture these the empirical observation on the impact differences across scientists (Figs. S25c–d), suggesting our hot-streak model is consistent with the Q-model when comparing impact across different scientists.

- S4.3 Q-model validation for artists and directors To study if the Q-model can be used to model the impacts of works for artists and movie directors, we repeated the procedures to estimate the Q-model parameters similar to scientists. Assume the auction price of each work is generated from the joint probability of p(p,N,Q), where p is the global distribution of price. To obtain the parameters for p(p,N,Q), we ﬁrst measured the distribution of auction price P(price) for all works, and productivity P(N) for all artists in our datasets, ﬁnding they both follow a log-normal distribution (Fig. S3a, Fig. S26a). The maximum-likelihood estimation allows us to calculate the


parameters for the joint probability of p(ˆp,N,ˆ Qˆ), where pˆ = log p,Nˆ = log N, and Qˆ = log Q. Similarly, we ﬁnd p(ˆp,N,ˆ Qˆ) follows a trivariate normal distribution whose

µ = (µp,µQ,µN) = (6.5,1.8,4.03),









σp2 σp,Q σp,N σp,Q σQ2 σQ,N σp,N σQ,N σN2

1.43 0.28 0.52 0.28 1.26 0.25 0.52 0.25 1.41

(S6)

Σ =

=

 

 

 

 

Notice that different from scientists, Q and N, N and p have positive correlations. The estimated Q parameter follows a log-normal distribution as well (Fig. S26b), suggesting the validity of the Qmodel for artists. Besides, the Q-model predictions for artists are in agreement with data in terms of the correlation between N and log price∗, and the correlation between log price−∗ and log price∗ (Figs. S26c–d). Hence for artists, the Q parameter can be calculated as Q = e<logprice>−µ

price,

###### where uprice = 6.5.

Similarly, we repeated the same procedures for movie directors. We ﬁnd P(rating) follows a normal distribution and P(N) follows a log-normal distribution (Fig. S3b, Fig. S27a), allowing us to calculate the parameters for the joint probability p(p,N,ˆ Qˆ), where Nˆ = log N, and Qˆ = log Q, where p is the global distribution for ratings. p(p,N,ˆ Qˆ) follows a trivariate normal distribution whose

µ = (µp,µQ,µN) = (5.9,0.9,2.8)









σp2 σp,Q σp,N σp,Q σQ2 σQ,N σp,N σQ,N σN2

1.3 0.25 0.38 0.25 0.8 0.22 0.38 0.22 1.0

Σ =

=

 

 

 

 

(S7)

The estimated Q parameter follows a log-normal distribution as well (Fig. S27b). The Q-model predictions for directors slightly deviate from data in terms of the correlation between Rating∗ and N, and the correlation between Rating−∗ and Rating∗ (Figs. S27c–d), which overestimates Rating∗ given the same N and Rating−∗ . We ﬁnd it is probably due to the upper bound of the IMDB rating system.

###### S5 Model for Individual Collective Impact

- S5.1 g(t) deﬁnition Individual collective impact, g(t), is deﬁned as the sums of citations to all her publications at each year that


N(t)

ci(t − ti), (S8)

g(t) =

i=1

where t measures the career stage, deﬁned by the number of years after her ﬁrst publication, N(t)

is the total number of papers published up to time t, and ti is the publication time of her ith paper, whose yearly citations are denoted as ci. g(t) is driven by the interplay of three factors: productivity N(t), the citation dynamics of each publication ci, and how publications and their impacts are distributed within a career. Due to the non-uniform nature of productivity, we bypass the need to control for N(t) to measure the career stage in unit of publications. That is, we keep the total number of publications in 20 years NT (T = 20) of each scientist, but rearrange the publishing process, such that a scientist produces the same number of papers every year. After this procedure, a scientist publishes constant n papers per year, and g(t) is deﬁned as

g(t) =

NT

i NT

ci(t −  

i=1

T ), (S9)

where means rounding down and Ni

T denotes the publication year of the ith paper. As a result, papers published in the late career may be shifted to early career stage, whose citation records are not long enough to cover the rest of the time. Hence, to remove the boundary effect, we only consider g(t) until the career stage that is not inﬂuenced by the boundary effect. The shortest career length after adjusting the boundary effect is 16 years.

T

- S5.2 Modulate paper citation with Γ(t) Next, we build a mathematical model for g(t) by incorporating our hot-streak model with paper citation dynamics. We combine Γ(t) with a previous model describing the citation dynamics, namely the WSB model21, allowing us to model how publications and their impacts are distributed within a career. The WSB model captures the cumulative


citation of a paper Ci(t) by three parameters: ﬁtness λi, immediacy σi, and longevity µi that

C(t,ti) = m eλiΦ

ln(t−ti)−µi σi

− 1 , (S10)

where t and ti are deﬁned as Eq. S8. Φ(ξ) is the cumulative normal distribution that follows

1 √2π

Φ(ξ) =

ξ

φ(x)dx, (S11)

−∞

which illustrates the aging effect of a paper characterized by µi and σi. The constant m denotes the average number of references a paper contains. Here we assume m = 30 to be consistent with previous studies21. By replacing ﬁtness λi with Γ(ti), Eq S10 can be expressed as

C(t,ti) = m eΓ(ti)Φ

ln(t−ti)−µi σi

− 1 , (S12)

where Γ(ti) represents the goodness parameter when a paper was published that can be measured from log(C10) t

, where  · ti

means the average around ti. The replacement is consistent with the

i

WSB model that Γ(ti) in Eq. S12 reﬂect the ﬁtness λi in the WSB model: The ultimate citation of a paper follows C∞ = m(eλ

− 1)21 that can be approximated by C1023, allowing us to get Γ(ti) = log(C10) t

i

, where log(m) is a constant whose value does not change the results of WSB model21. Hence, Eq. S12 captures both the paper impact and

i ≈ log(C∞) t

i ≈ log(m) + λ t

i

how impact distributes within career by incorporating Γ(ti) into the WSB model.

- S5.3 g(t) under the null model We ﬁrst discuss the null model prediction, g0(t), that assumes Γ remains constant across a career (Γ(t) ≡ Γ0). The integral of Eq. S12 over t allows us to get the cumulative individual citation G0(t) that


NT

G0(t) =

Ci(t,ti)

i=1

t

≈ NT

C(t,t )P(µ ,σ )dt dµ dσ

0 µ ,σ

t

nC(t,t )δ(µ )δ(σ )dt dµ dσ ,

=

0 µ ,σ

t

ln(t−t )−µ σ

m eΓ0Φ

− 1 dt

=

0

(S13)

where NT = 0t ndt and n is the publication rate at each time stamp, t denotes the career stage of a scientist, t is the time when each paper was published, and C(t,t ) is the total paper citation that follows Eq. S12. For simplicity we assume in Eq. S13 that each scientist has constant µ and σ for all her publications. Hence, g0(t) can be expressed as

d dt

g0(t) =

= n

G0(t)

d dt

t

m eΓ0Φ

0

ln(t−t )−µ σ

0Φ(ln(t)−µ

) − 1 .

= nm eΓ

σ

− 1 dt

(S14)

g0(t) follows an S curve continuously increasing over time (Fig. 3d, Fig. S28) that is unable to capture a variety of g(t) observed in real careers (Fig. 3d). Eq. S14 suggests g0(t) is captured by Γ0 and two aging effect parameters µ and σ. Comparing Eq. S12 with Eq. S14 we ﬁnd g0(t) is the cumulative citation of papers published at t = 0.

- S5.4 g(t) under hot-streak model Next we calculate g(t) under the hot-streak model by incorporating a time series Γ(t) following Eq. 1 that


d dt

g(t) = n

d dt

= n

= n

t

0

= nm

= nm

G(t)

t

m eΓ(t )Φ

0

ln(t−t )−µ σ

− 1 dt

∂ ∂t

ln(t−t )−µ σ

meΓ(t )Φ

t

ln(t−t )−µ σ

eΓ(t )Φ

Φ

0

t

ln(t−t )−µ σ

eΓ(t )Φ

Φ

0

dt

ln(t − t ) − µ σ

ln(t − t ) − µ σ

d dt

Γ(t )dt −

t

∂ ∂t

eΓ(t )Φ

0

ln(t−t )−µ σ

dt

d dt

0Φ(ln(t)−µ

) − 1 .

Γ(t )dt + nm eΓ

σ

(S15)

Similarly, we assume a constant µ and σ for each scientist. Eq. S15 assumes each individual has one hot streak. The second term in Eq. S15 is g0(t) under the null model prediction. The derivatives of Eq. 1 can be expressed as

d dt

Γ(t ) =

d dt

[Γ0 + (ΓH − Γ0)[H(t − t↑) − H(t − t↓)]

= (ΓH − Γ0)[δ(t − t↑) − δ(t − t↓))].

(S16)

By replacing Γ(t ) in Eq. S15 with Eq. 1 and incorporating Eq. S16, we can get the expression of the ﬁrst term in Eq. S15, denoted as ∆g(t), that follows



0 t < t↑



ln(t−t↑)−µ

nm(ΓH − Γ0)Φ ln(t−σt↑)−µ eΓHΦ

∆g(t) =

σ t↑ ≤ t < t↓

ln(t−t↑)−µ

ln(t−t↓)−µ

nm(ΓH − Γ0) Φ ln(t−σt↑)−µ eΓHΦ

σ − Φ ln(t−σt↓)−µ eΓHΦ

###### σ t ≥ t↓



(S17) Hence, g(t) under the hot-streak model can be expressed as



0 t < t↑

ln(t−t↑)−µ

nm(ΓH − Γ0)Φ ln(t−σt↑)−µ eΓHΦ



σ t↑ ≤ t < t↓

0Φ(ln(t)−µ

) − 1)

g(t) = nm(eΓ

+

###### ,

σ

ln(t−t↑)−µ σ

nm(ΓH − Γ0) Φ ln(t−σt↑)−µ eΓHΦ

g0(t)

ln(t−t↓)−µ

−Φ ln(t−σt↓)−µ eΓHΦ



σ t ≥ t↓

∆g(t)

(S18) Eq. S18 is composed of two parts: g0(t) captures the cumulative citation of papers published when Γ(ti) = Γ0, and ∆g(t) to captures the citations contributed by papers published during hot streaks when Γ(ti) = ΓH. Fig. 4d illustrates the inﬂuence of the hot streak on individual citation: Before the hot streak, ∆g(t) has no impact on individual citation and g(t) = g0(t). During the hot streak, g(t) experiences rapid growth due to ΓH, and the trend continues for a while to reach its peak even after the end of the hot streak. Eq. S18 allows us to model a wide range of g(t) that cannot be expected by the null model (Fig. 3d, Fig. 3h, Fig. S29, Fig. S30). g(t) is determined by the timing of the hot streak (t↑ and t↓), the level of performance (Γ0 and ΓH), and the aging effect parameters

(µ and σ).

- S5.5 Parameter estimation In order to test how well Eq. S18 matches empirical data, we need

to estimate the parameters Γ0 and ΓH, t↑ and t↓, and the aging effect parameters (µ and σ) for each scientist given her g(t). Here we assume each individual has only one hot streak, and relax all the six individual-speciﬁc parameters. For each individual in our dataset, we used ordinary least square (OLS) and ﬁtted to Eq. S18 the g(t) measured from real career by minimizing the mean squared error (MSE) between data and the model result. To make sure the ﬁtted parameters are meaningful, we also set constraints when optimizing the error function that t↑ > 0, t↓ > 0, 0 < Γ0 ≤ ΓH ≤ 10, 0 ≤ µ ≤ 8.5 and σ > 0. We assume ΓH cannot exceed 10, otherwise the average citation per paper during hot streaks is C10  ≈ 22026.

- S5.6 Model validation To systematically evaluate the accuracy of our model, we generate an uncertainty envelop of g(t) for each individual for both the hot-streak model and the null model. Speciﬁcally, we simulate g(t) by assigning a Gaussian noise N(0, σ2) to the ﬁtted Γ. The standard deviation σ is calculated from data (Fig. S18), representing the inherent noise of the Γ(N)


sequence. Hence, for each paper i we randomly generate a Γi parameter from a normal distribution with mean as Γ0 if the paper is published during the normal performance or ΓH during hot streaks. We assume µ and σ to be the same as the ﬁtting result. We simulated each individual for 1000 realizations, allowing us to get a distribution of g(t) at each time step. The envelop at each time t is deﬁned as one standard deviation of all the values of g(t) at t . Then we measure the model performance by calculating the fraction of g(t) falling within the envelope. We repeated the procedures

for the null model to calculate the uncertainty envelope as well. Our hot-streak model outperforms the null model as more data fall within the envelop (Fig. 3f). We also compare the distribution of the Mean Absolute Percentage Error (MAPE) between data and model predictions, ﬁnding our hot-streak model has systematically smaller error compared with the null model (Fig. S31).

###### S6 Testing Alternative Hypotheses

Our hot-streak model is the simplest function to approximate impacts of works within a career. The accuracy of the hot-streak model prompts us to ask whether it is unique in its ability to capture the impacts of individual careers across different domains. We therefore seek other models corresponding to different dynamics of hot streaks. In this section we test the validity of four alternative hypotheses (A–D) proposed in the main text (Figs. S34a–f), by comparing each model prediction on the relative timing of the top six hit works within a carer with empirical observations. Indeed, the symmetric patterns of normalized joint probability Φ and R(∆N/N) for any pair of the top three hits, suggests one hit is equal likely to appear before or after another hit among the top three highest impact works within a career across three domains. We ﬁnd such randomness on the relative position among hits is not just limited to the top three. We measured the position of the top three hits N˜ relative to the top six hits of the career. For each of the three hits, we compute P(N˜) for artists, directors, and scientists, ﬁnding a lack of predictive patterns for P(N˜) across three domains, suggesting the relative order among the top six hits in real careers are random (Figs. S34gnu).

To test if hypotheses A–D can reproduce the randomness among top six hits within a career, we then compare P(N˜) predicted by each hypothesis with the corresponding distributions measured from real careers. For our hot-streak model and each alternative hypothesis, we simulate a sequence of work impact for each individual. We use real productivity N, and the mean impact of each individual as input, and assumes for each individual a period of outstanding performance that randomly appears within a career. We assume Γ0 for each individual as the mean impact within a career measured from data, and ΓH = Γ0 + 1.0. Since the average length of hot streaks usually accounts for 20% of total N works, and the alternative model only changes how the hot streak emerges and diminishes, here we assume for each individual a ﬁxed length of ΓH period (0.2N) for right trapezoid, left trapezoid, and isosceles trapezoid model. We also assume the hypotenuses of each trapezoid model to be 0.2N, ensuring the impact can gradually change between Γ0 and ΓH under different hypotheses. To keep the duration of hot streaks to be the same for different hypotheses, we assume a 0.4N length of hot streaks for hypothesis C and our hot-streak model, respectively. We assume ΓH as the peak value for the quadratic and tent function of each individual. The impact of each work is then generated from a normal distribution N(Γ(N),σ), where the mean value Γ(N) is deﬁned by each model, and the standard deviation σ is measured from data (Fig. S18).

We calculated P(N˜) of each hypothesis, ﬁnding P(N˜) for hypotheses A–D shows predictive trends on the relative position of top six hits (Figs. S34h–m). For example, the top two hits of isosceles trapezoid, quadratic, and tent model always appear in the middle of the top six hits, and their probability decreases when deviating from the middle (Figs. S34j–l). For the right trapezoid

model, the top three hits always appear before the other hits (Fig. S34i); whereas the case reverses for the left trapezoid model (Fig. S34m). Among these hypotheses, only our hot-streak model can reproduce the randomness of the top six hits (Fig. S34h). To quantify the different between data and each model prediction, we performed the Kolmogorov-Smirnov test to measure whether we can reject the hypothesis that predictions and data are drawn from the same distribution. We used the R package ‘dgof’ to conduct the discrete Goodness-of-Fit test, ﬁnding P(N˜) for hypotheses A–D is statistically different from empirical observations (Figs. S34i–m). Our hot-streak model is the only one that captures the randomness of the top six hits within a career (Fig. S34h). The results reported in Figs. S34h–m are based on the simulations using artists’ proﬁles as input. To make sure the conclusion is robust to the other two domains, we repeated the procedure using proﬁles of directors (Figs. S34o–t) and scientists (Figs. S34v–aa) as input, ﬁnding the conclusion remains the same for other domains.

###### Table S1: Empirical evidence of whether hot hand exists

|Year|Paper<br><br>|Field|Hot hand<br><br>|Data|
|---|---|---|---|---|
|1985<br><br>|Gilovich et al. (1985)1|Basketball<br><br>|No|Field goal data for 9 NBA player during the 1980 –1981 season, free-throw data for 9 NBA players during 1980–1982 seasons, a controlled shooting experiment with 26 Cornell students|
|1989<br><br>|Larkey et al. (1989)53|Basketball<br><br>|Yes<br><br>|18 players in 39 NBA games in 1987–1988 season|
|1993<br><br>|Albright (1993)54|Baseball|No<br><br>|40 MLB players in 1987–1990 seasons|
|1993|Albert (1993)55<br><br>|Baseball|Yes|Same as Albright (1993)54|
|1994<br><br>|Frohlich (1994)56|Baseball<br><br>|No|MLB No-hit games in 1989–1993<br><br>|
|1995|Wardrop (1995)57<br><br>|Basketball<br><br>|Inconclusive|Free throw data for 9 members of the Boston Celtics during 1980 1982 seasons|
|1999<br><br>|Wardrop (1999)58|Basketball|Yes<br><br>|A shooting experiment for a member on the UW-Madison women’s varsity basketball team|
|2000|Vergin (2000)59<br><br>|Basketball, Baseball|No<br><br>|29 NBA team wins and losses in 1996–1998 seasons, 28 MLB team wins and losses in 1996 season|
|2001<br><br>|Albert and Williamson (2001)60|Basketball, Baseball|Yes<br><br>|Same as Wardrop (1999)58, hitting data for Javy Lopez for the 1998 MLB season|
|2001|Klaassen and Magnus (2001)61<br><br>|Tennis|Yes<br><br>|Point-to-point data from Wimbledon singles in 1992–1995|
|2003<br><br>|Koehler and Conley (2003)62|Basketball<br><br>|No|NBA long distance shootout contest in 1994–1997|
|2003<br><br>|Smith (2003)63|Horse Pitching|Yes<br><br>|62 pitchers in 2000–2001 World Championships|
|2004<br><br>|Dorsey-Palmateer and Smith (2004)64|Bowling|Yes<br><br>|43 players from PBA in 2002–2003 season|
|2005|Clark (2005)65<br><br>|Golf<br><br>|Yes|Hole-to-hole scores from PGA tour in 1997–1998|
|2008<br><br>|Bocskocsky et al. (2008)66|Basketball|Yes<br><br>|83,000 shots from the 2012–2013 NBA season|
|2008|Albert (2008)67<br><br>|Baseball<br><br>|Yes<br><br>|All regular baseball players during the 2005 MBL season|
|2010<br><br>|Arkes (2010)68|Basketball|Yes<br><br>|Free throw data during the 2005–06 NBA season|
|2011<br><br>|Yaari and Eisenmann (2011)69|Basketball<br><br>|Yes|Free throws of ﬁve NBA regular seasons from 2005 to 2009|
|2012|Yaari and David (2012)70<br><br>|Bowling<br><br>|Yes<br><br>|Frame by frame games for 100 top players in PBA from 2002 to 2011|
|2012|Aharoni and Sarig (2012)71<br><br>|Basketball<br><br>|Yes|1218 games in 2004–2005 NBA season|
|2012|Raab and Gula (2012)72<br><br>|Volleyball|Yes<br><br>|26 top players’ offensive performance in Germany s ﬁrst-division volleyball league|
|2012|Gabel and Redner (2012)73|Basketball<br><br>|No|6087 games from the 2006/07 – 2009/10 seasons of NBA|
|2014|Miller and Sanjurjo (2014)74<br><br>|Basketball|Yes|Controlled shooting experiment for players from the semi-professional basketball team Santo Domingo de Betanzos|
|2014<br><br>|Csapo and Raab (2014)75|Basketball<br><br>|Yes|666 NBA games from the 2011-12 to 2013-14 seasons|
|2015<br><br>|Miller and Sanjurjo (2015)76<br><br>|Basketball|Yes<br><br>|NBA Three-Point Contest|
|2015<br><br>|Rosenqvist and Skans (2015)77|Golf|Yes<br><br>|Male European PGA tournaments in 2000–2012|
|2015<br><br>|Parsons and Rohde (2015)78|Football/Soccer|Yes<br><br>|20 teams from EPL in 2010–2013 seasons|


|2015<br><br>|Miller and Sanjurjo (2015)76|Baseball|Yes<br><br>|NBA Three point shooting contest in 1986–2005|
|---|---|---|---|---|
|2016|Miller and Sanjurjo (2016)3<br><br>|Basketball|Yes<br><br>|Same as Miller and Sanjurjo (2014)74|
|2017<br><br>|Green and Zwiebel (2017)79|Baseball|Yes<br><br>|MLB players’ batter|


|1993<br><br>|Hendricks (1993)8|Mutual funds<br><br>|Yes<br><br>|Risk-adjusted mutual-fund returns in 1975-1988|
|---|---|---|---|---|
|1995<br><br>|Malkiel (1995)80<br><br>|Equity mutual funds|Inconclusive<br><br>|All risk-adjusted mutual-fund returns in 1971–1991|
|1997<br><br>|Carhart (1997)81|Equity mutual funds<br><br>|No|All risk-adjusted equity mutual-fund returns in 1962–1993<br><br>|
|2008|Huij et al. (2008)82<br><br>|Bond funds|Yes<br><br>|Risk-adjusted bond fund returns in 1990–2003|
|2010|Jagannathan et al. (2010)9<br><br>|Hedge funds|Yes<br><br>|Risk-adjusted hedge fund returns in 1996–2005|


###### Table S2: Statistical methods to detect hot hand

|Method<br><br>|Paper|
|---|---|
|Conditional probablity<br><br>|Gilovich et al. (1985)1, Larkey et al. (1989)53, Wardrop (1995)57, Koehler and Conley (2003), Smith (2003)63, Koehler and Conley (2003)62, Dorsey-Palmateer and Smith (2004)64, Clark (2005)65, Albert (2008)67, Yaari and Eisenmann (2011)69, Aharoni and Sarig (2012)71, Raab and Gula (2012)72, Csapo and Raab (2014)75, Miller and Sanjurjo (2016)3, Malkiel (1995)80|
|Serial correlation|Gilovich et al. (1985)1, Larkey et al. (1989)53, Wardrop (1999)58, Klaassen and Magnus (2001)61, Smith<br><br>(2003)63, Raab and Gula (2012)72, Gabel and Redner (2012)73, Green and Zwiebel (2017)79, Hendricks (1993)8|
|Number of runs|Gilovich et al. (1985)1, Wardrop (1999)58, Albright (1993)54, Vergin (2000)59, Koehler and Conley (2003)62, Smith (2003)63, Albert (2008)67, Raab and Gula (2012)72, Csapo and Raab (2014)75, Miller and Sanjurjo<br><br>(2014)74, Parsons and Rohde (2015)78, Miller and Sanjurjo (2015)76<br><br>|
|Stationary of successful rate|Gilovich et al. (1985)1, Frohlich (1994)56, Wardrop (1999)58, Albert (2008)67, Yaari and Eisenmann (2011)69, Yaari and David (2012)70, Gabel and Redner (2012)73<br><br>|
|hidden Markov model<br><br>|Albright (1993)54, Albert (1993)55, Albert and Williamson (2001)60, Albert (2008)67, Wetzels et al.(2016)83|
|Long streaks|Larkey et al. (1989)53, Vergin (2000)59, Frohlich (1994)56,Dorsey-Palmateer and Smith (2004)64, Albert<br><br>(2008)67, Aharoni and Sarig (2012), Csapo and Raab (2014)75, Miller and Sanjurjo (2014)74, Miller and Sanjurjo<br><br>(2015)76<br><br>|
|Regression|Albright (1993)54, Bocskocsky et al. (2008)66, Arkes (2010)68, Aharoni and Sarig (2012)71, Csapo and Raab<br><br>(2014)75, Parsons and Rohde (2015)78, Hendricks (1993)8, Carhart (1997)81, Huij et al. (2008)82, Jagannathan et al. (2010)9|
|Time interval between scoring event<br><br>|Gabel and Redner (2012)73|
|Regression discontinuity design|Rosenqvist and Skans (2015)77|


###### References

- 1. Gilovich, T., Vallone, R. & Tversky, A. The hot hand in basketball: On the misperception of random sequences. Cognitive Psychology 17, 295–314 (1985).
- 2. Bar-Eli, M., Avugos, S. & Raab, M. Twenty years of hot hand research: Review and critique. Psychology of Sport and Exercise 7, 525–553 (2006).
- 3. Miller, J. B. & Sanjurjo, A. Surprised by the gambler’s and hot hand fallacies? A truth in the law of small numbers. IGIER Working Paper No. 552 (2016).
- 4. Ayton, P. & Fischer, I. The hot hand fallacy and the gambler’s fallacy: Two faces of subjective randomness? Memory & Cognition 32, 1369–1378 (2004).
- 5. Croson, R. & Sundali, J. The gambler’s fallacy and the hot hand: Empirical data from casinos. Journal of Risk and Uncertainty 30, 195–209 (2005).
- 6. Rabin, M. & Vayanos, D. The gambler’s and hot-hand fallacies: Theory and applications. The Review of Economic Studies 77, 730–778 (2010).
- 7. Xu, J. & Harvey, N. Carry on winning: The gamblers’ fallacy creates hot hand effects in online gambling. Cognition 131, 173–180 (2014).
- 8. Hendricks, D., Patel, J. & Zeckhauser, R. Hot hands in mutual funds: Short-run persistence of relative performance, 1974–1988. The Journal of Finance 48, 93–130 (1993).
- 9. Jagannathan, R., Malakhov, A. & Novikov, D. Do hot hands exist among hedge fund managers? An empirical evaluation. The Journal of Finance 65, 217–255 (2010).


- 10. Kahneman, D. & Riepe, M. W. Aspects of investor psychology. The Journal of Portfolio Management 24, 52–65 (1998).
- 11. Lehman, H. C. Age and achievement (Princeton, NJ, 1953).
- 12. Merton, R. K. The matthew effect in science. Science 159, 56–63 (1968).
- 13. Simonton, D. K. Age and outstanding achievement: What do we know after a century of research? Psychological Bulletin 104, 251 (1988).
- 14. Jones, B. F. & Weinberg, B. A. Age dynamics in scientiﬁc creativity. Proceedings of the National Academy of Sciences 108, 18910–18914 (2011).
- 15. Petersen, A. M., Jung, W.-S., Yang, J.-S. & Stanley, H. E. Quantitative and empirical demonstration of the matthew effect in a study of career longevity. Proceedings of the National Academy of Sciences 108, 18–23 (2011).
- 16. Petersen, A. M. et al. Reputation and impact in academic careers. Proceedings of the National Academy of Sciences 111, 15316–15321 (2014).
- 17. Stringer, M. J., Sales-Pardo, M. & Amaral, L. A. N. Effectiveness of journal ranking schemes as a tool for locating information. PLoS One 3, e1683 (2008).
- 18. Radicchi, F., Fortunato, S. & Castellano, C. Universality of citation distributions: Toward an objective measure of scientiﬁc impact. Proceedings of the National Academy of Sciences 105, 17268–17272 (2008).


- 19. Ke, Q., Ferrara, E., Radicchi, F. & Flammini, A. Deﬁning and identifying sleeping beauties in science. Proceedings of the National Academy of Sciences 112, 7426–7431 (2015).
- 20. Galenson, D. W. Old masters and young geniuses: The two life cycles of artistic creativity (Princeton University Press, 2011).
- 21. Wang, D., Song, C. & Barab´asi, A.-L. Quantifying long-term scientiﬁc impact. Science 342, 127–132 (2013).
- 22. Way, S. F., Morgan, A. C., Clauset, A. & Larremore, D. B. The misleading narrative of the canonical faculty productivity trajectory. Proceedings of the National Academy of Sciences

(2017).

- 23. Sinatra, R., Wang, D., Deville, P., Song, C. & Barab´asi, A.-L. Quantifying the evolution of individual scientiﬁc impact. Science 354, aaf5239 (2016).
- 24. Simonton, D. K. Scientiﬁc genius: A psychology of science (Cambridge University Press, 1988).
- 25. Hirsch, J. E. An index to quantify an individual’s scientiﬁc research output. Proceedings of the National academy of Sciences 102, 16569–16572 (2005).
- 26. Duch, J. et al. The possible role of resource requirements and academic career-choice risk on gender differences in publication rate and impact. PloS One 7, e51332 (2012).
- 27. Merton, R. K. The matthew effect in science, ii: Cumulative advantage and the symbolism of intellectual property. Isis 79, 606–623 (1988).


- 28. Price, D. d. S. A general theory of bibliometric and other cumulative advantage processes. Journal of the Association for Information Science and Technology 27, 292–306 (1976).
- 29. Barab´asi, A.-L. & Albert, R. Emergence of scaling in random networks. Science 286, 509–512

(1999).

- 30. Wasserman, M., Zeng, X. H. T. & Amaral, L. A. N. Cross-evaluation of metrics to estimate the signiﬁcance of creative works. Proceedings of the National Academy of Sciences 112, 1281–1286 (2015).
- 31. Merton, R. K. Singletons and multiples in scientiﬁc discovery: A chapter in the sociology of science. Proceedings of the American Philosophical Society 105, 470–486 (1961).
- 32. Wuchty, S., Jones, B. F. & Uzzi, B. The increasing dominance of teams in production of knowledge. Science 316, 1036–1039 (2007).
- 33. Clauset, A., Arbesman, S. & Larremore, D. B. Systematic inequality and hierarchy in faculty hiring networks. Science Advances 1, e1400005 (2015).
- 34. Shockley, W. On the statistics of individual variations of productivity in research laboratories. Proceedings of the IRE 45, 279–290 (1957).
- 35. Redner, S. Citation statistics from 110 years of physical review. Physics Today 58, 49 (2005).
- 36. Moreira, J. A., Zeng, X. H. T. & Amaral, L. A. N. The distribution of the asymptotic number of citations to sets of publications by a researcher or from an academic department are consistent with a discrete lognormal model. PloS One 10, e0143108 (2015).


- 37. Palla, G., Barab´asi, A.-L. & Vicsek, T. Quantifying social group evolution. Nature 446, 664–667 (2007).
- 38. Galenson, D. W. & Lenzu, S. Pricing genius: the market evaluation of innovation. Journal of Applied Economics 19, 219–248 (2016).
- 39. Blumm, N. et al. Dynamics of ranking processes in complex systems. Physical Review Letters 109, 128701 (2012).
- 40. Zickar, M. J. & Slaughter, J. E. Examining creative performance over time using hierarchical linear modeling: An illustration using ﬁlm directors. Human Performance 12, 211–230 (1999).
- 41. Simonton, D. K. Group artistic creativity: Creative clusters and cinematic success in feature ﬁlms. Journal of Applied Social Psychology 34, 1494–1520 (2004).
- 42. Han, H., Zha, H. & Giles, C. Name disambiguation spectral in author citations using a Kway clustering method. In Proceedings of the 5TH ACM/IEEE Joint Conference on Digital Libraries, 334–343 (IEEE, 2005).
- 43. Treeratpituk, P. & Giles, C. L. Disambiguating authors in academic publications using random forests. In Proceedings of the 9th ACM/IEEE-CS Joint Conference on Digital Libraries, 39–48 (ACM, 2009).
- 44. Radicchi, F. & Castellano, C. Analysis of bibliometric indicators for individual scholars in a large data set. Scientometrics 97, 627–637 (2013).


- 45. Guevara, M. R., Hartmann, D., Aristar´an, M., Mendoza, M. & Hidalgo, C. A. The research space: Using career paths to predict the evolution of the research output of individuals, institutions, and nations. Scientometrics 109, 1695–1709 (2016).
- 46. Pan, R. K., Petersen, A. M., Pammolli, F. & Fortunato, S. The memory of science: Inﬂation, myopia, and the knowledge network. arXiv preprint arXiv:1607.05606 (2016).
- 47. Dennis, W. Creative productivity between the ages of 20 and 80 years. Journal of Gerontology 21, 1–8 (1966).
- 48. Simonton, D. K. Creative productivity: A predictive and explanatory model of career trajectories and landmarks. Psychological Review 104, 66 (1997).
- 49. Wilke, A. & Barrett, H. C. The hot hand phenomenon as a cognitive adaptation to clumped resources. Evolution and Human Behavior 30, 161–169 (2009).
- 50. Sun, Y. & Wang, H. Gambler’s fallacy, hot hand belief, and the time of patterns. Judgment and Decision Making 5, 124 (2010).
- 51. Oskarsson, A. T., Van Boven, L., McClelland, G. H. & Hastie, R. What’s next? Judging sequences of binary events. Psychological Bulletin 135, 262 (2009).
- 52. Alter, A. L. & Oppenheimer, D. M. From a ﬁxation on sports to an exploration of mechanism: The past, present, and future of hot hand research. Thinking & Reasoning 12, 431–444 (2006).
- 53. Larkey, P. D., Smith, R. A. & Kadane, J. B. It’s okay to believe in the hot hand. Chance 2, 22–30 (1989).


- 54. Albright, S. C. A statistical analysis of hitting streaks in baseball. Journal of the American Statistical Association 88, 1175–1183 (1993).
- 55. Albert, J. A statistical analysis of hitting streaks in baseball - comment. Journal of the American Statistical Association 88, 1184–1188 (1993).
- 56. Frohlich, C. Baseball: Pitching no-hitters. Chance 7, 24–30 (1994).
- 57. Wardrop, R. L. Simpson’s paradox and the hot hand in basketball. The American Statistician 49, 24–28 (1995).
- 58. Wardrop, R. L. Statistical tests for the hot-hand in basketball in a controlled setting. American Statistician 1, 1–20 (1999).
- 59. Vergin, R. Winning streaks in sports and the mispreception of momentum. Journal of Sport Behavior 23, 181 (2000).
- 60. Albert, J. & Williamson, P. Using model/data simulations to detect streakiness. The American Statistician 55, 41–50 (2001).
- 61. Klaassen, F. J. & Magnus, J. R. Are points in tennis independent and identically distributed? Evidence from a dynamic binary panel data model. Journal of the American Statistical Association 96, 500–509 (2001).
- 62. Koehler, J. J. & Conley, C. A. The hot hand myth in professional basketball. Journal of Sport and Exercise Psychology 25, 253–259 (2003).
- 63. Smith, G. Horseshoe pitchers hot hands. Psychonomic Bulletin & Review 10, 753–758 (2003).


- 64. Dorsey-Palmateer, R. & Smith, G. Bowlers’ hot hands. The American Statistician 58, 38–45

(2004).

- 65. Clark III, R. D. Examination of hole-to-hole streakiness on the PGA tour. Perceptual and Motor Skills 100, 806–814 (2005).
- 66. Bocskocsky, A., Ezekowitz, J. & Stein, C. The hot hand: A new approach to an old fallacy. In 8th Annual Mit Sloan Sports Analytics Conference (2014).
- 67. Albert, J. Streaky hitting in baseball. Journal of Quantitative Analysis in Sports 4 (2008).
- 68. Arkes, J. Revisiting the hot hand theory with free throw data in a multivariate framework. Journal of Quantitative Analysis in Sports 6, 2 (2010).
- 69. Yaari, G. & Eisenmann, S. The hot (invisible?) hand: Can time sequence patterns of success/failure in sports be modeled as repeated random independent trials? PloS One 6, e24532

(2011).

- 70. Yaari, G. & David, G. “Hot Hand” on strike: Bowling data indicates correlation to recent past results, not causality. PLoS One 7, e30112 (2012).
- 71. Aharoni, G. & Sarig, O. H. Hot hands and equilibrium. Applied Economics 44, 2309–2320

(2012).

- 72. Raab, M., Gula, B. & Gigerenzer, G. The hot hand exists in volleyball and is used for allocation decisions. Journal of Experimental Psychology: Applied 18, 81 (2012).


- 73. Gabel, A. & Redner, S. Random walk picture of basketball scoring. Journal of Quantitative Analysis in Sports 8 (2012).
- 74. Miller, J. B. & Sanjurjo, A. A cold shower for the hot hand fallacy. IGIER Working Paper 518

(2014).

- 75. Csapo, P. & Raab, M. “Hand down, man down.” Analysis of defensive adjustments in response to the hot hand in basketball using novel defense metrics. PloS one 9, e114184 (2014).
- 76. Miller, J. B. & Sanjurjo, A. Is it a fallacy to believe in the hot hand in the NBA three-point contest? IGIER Working Paper 548 (2015).
- 77. Rosenqvist, O. & Skans, O. N. Conﬁdence enhanced performance? The causal effects of success on future performance in professional golf tournaments. Journal of Economic Behavior & Organization 117, 281–295 (2015).
- 78. Parsons, S. & Rohde, N. The hot hand fallacy re-examined: New evidence from the English Premier League. Applied Economics 47, 346–357 (2015).
- 79. Green, B. & Zwiebel, J. The hot-hand fallacy: Cognitive mistakes or equilibrium adjustments? Evidence from Major League Baseball. Management Science (2017).
- 80. Malkiel, B. G. Returns from investing in equity mutual funds 1971 to 1991. The Journal of Finance 50, 549–572 (1995).
- 81. Carhart, M. M. On persistence in mutual fund performance. The Journal of ﬁnance 52, 57–82


(1997).

###### 82. Huij, J. & Derwall, J. “Hot hands” in bond funds. Journal of banking & ﬁnance 32, 559–572

(2008).

###### 83. Wetzels, R. et al. A bayesian test for the hot hand phenomenon. Journal of MathematicalPsychology 72, 200–209 (2016).

![image 12](Hot streaks in artistic cultural and scientific careers_images/imageFile12.png)

###### Figure S1: Entity linking result of two auction databases. The relationship of the number of

auction records in Findartinfo and Artprice for matched artists in log-log scale, where Nfindartinfo is the number of records in Findartinfo and Nartprice is the number of records in Artprice. Blue dots denote data, red dots denote the logarithmic binning of the scattered data, and the dashed grey line indicates y = x.

![image 13](Hot streaks in artistic cultural and scientific careers_images/imageFile13.png)

###### Figure S2: Citation inﬂation in WoS. The average impact of papers published in the same year,quantiﬁed with number of citations 10 years after publication, steadily grows as a function of thepublication year ranging from 1900 to 2004.

![image 14](Hot streaks in artistic cultural and scientific careers_images/imageFile14.png)

- Figure S3: Impact distribution. (a) The distribution of auction price P(Price) for artists. Blue dots denote data, and the red line is a log-normal distribution with average µ = 8.0 and standard deviation σ = 2.15. (b) The distribution of movie rating P(Rating) for directors. The red line is a normal distribution with average µ = 6.8 and standard deviation σ = 1.19. (c–d), The distribution


of (c) raw and (d) rescaled C10 for scientists. The red line is a log-normal distribution, with µ = 2.7 and σ = 1.18 for (c) and µ = 0.1 and σ = 1.42 for (d).

![image 15](Hot streaks in artistic cultural and scientific careers_images/imageFile15.png)

- Figure S4: Random impact rule. P(≥ Ni/N) of the top three hit works within a career for (a) artists, (b) directors, and (c) scientists. Ni denotes the order of the ith hit work within a career. The color denotes different hit works, and the dashed grey line denotes P(≥ Ni/N) for a uniform distribution.


![image 16](Hot streaks in artistic cultural and scientific careers_images/imageFile16.png)

###### Figure S5: Φ for other pairs of hit works. (a–c), Φ(N∗,N∗∗∗) of real careers for (a) artists, (b)directors, and (c) scientists. (d–f), Φ(N∗∗,N∗∗∗) of real careers for (d) artists, (e) directors, and (f)scientists. We ﬁnd the same patterns along the diagonal for Φ(N∗,N∗∗∗) and Φ(N∗∗,N∗∗∗).

![image 17](Hot streaks in artistic cultural and scientific careers_images/imageFile17.png)

- Figure S6: Φ for shufﬂed careers. (a–c), Φ(N∗,N∗∗∗) of shufﬂed careers for (a) artists, (b) directors, and (c) scientists. (d–f), Φ(N∗∗,N∗∗∗) of shufﬂed careers for (d) artists, (e) directors, and (f) scientists. We ﬁnd for shufﬂed careers the patterns along the diagonal for Φ(N∗,N∗∗∗) and Φ(N∗∗,N∗∗∗) disappear.


![image 18](Hot streaks in artistic cultural and scientific careers_images/imageFile18.png)

- Figure S7: Random impact rule under different career length. P(≥ Ni/N) for individuals under different career length: Artists with at least (a) 20 years and (d) 30 years of career length, directors with at least (b) 20 years and (e) 30 years of career length, and scientists with at least (c) 30 years and (f) 40 years of career length. Ni denotes the order of the ith hit work within a career. The color denotes different hit works, and the dashed grey line denotes P(≥ Ni/N) for a uniform distribution.


![image 19](Hot streaks in artistic cultural and scientific careers_images/imageFile19.png)

- Figure S8: R(∆N∗/N) under different career length. R(∆N∗/N) for individuals under different career length: Artists with at least (a) 20 years and (d) 30 years of career length, directors with at least (b) 20 years and (e) 30 years of career length, and scientists with at least (c) 30 years and (f) 40 years of career length, where ∆N∗ = N∗ − N∗∗. Red dots denote data and blue dots denote shufﬂed careers. We ﬁnd the R(∆N∗/N) still peaks around zero for individuals with different career length.


![image 20](Hot streaks in artistic cultural and scientific careers_images/imageFile20.png)

- Figure S9: Streak length under the different career length. P(L) for individuals under different career length: Artists with at least (a) 20 years and (d) 30 years of career length, directors with at least (b) 20 years and (e) 30 years of career length, and scientists with at least (c) 30 years and (f) 40 years of career length. Red dots denote data and blue dots denotes shufﬂed careers. We ﬁnd the P(L) of data has exponential tail that is wider than the shufﬂed careers for individuals with different career length.


![image 21](Hot streaks in artistic cultural and scientific careers_images/imageFile21.png)

- Figure S10: Streak length under different thresholds. (a–c), P(L) and P(LS) when the threshold is the mean of impact within a career for (a) artists, (b) directors and (c) scientists. (d–f)


P(L) and P(LS) when the threshold is the geometric mean of impact within a career for individuals across three domains.

![image 22](Hot streaks in artistic cultural and scientific careers_images/imageFile22.png)

###### Figure S11: The difference of P(L) and P(LS). (a–c), P(L)/P(LS) for (a) artists, (b) director,and (c) scientists in semi-log scale. The vertical line denotes L = 20, and the red star denotes theprobability difference when L = 20.

![image 23](Hot streaks in artistic cultural and scientific careers_images/imageFile23.png)

###### Figure S12: Random impact rule in the null model. P(≥ Ni/N) under the null modelprediction for (a) artists, (b) directors, and (c) scientists. The null model can reproduce therandomness of the top three highest impact works in a career.

![image 24](Hot streaks in artistic cultural and scientific careers_images/imageFile24.png)

- Figure S13: Φ(N∗,N∗∗) predicted by the null model. The normalized joint probability Φ(N∗,N∗∗) for the top two hit works within a career under the null model prediction for (a) artists, (b) directors, and (c) scientists. The null model cannot reproduce the temporal colocation of the two highest impact works within a career.


![image 25](Hot streaks in artistic cultural and scientific careers_images/imageFile25.png)

- Figure S14: Comparison of Γ(N) calculated from raw and rescale log C10. (a) The Γ(N) sequence for a scientist in our dataset calculated from raw C10 (blue dots) and rescaled C10 (red dots). (b) The distribution of Pearson correlation P(ρ) for Γ(N) sequence calculated from the


raw C10 and rescaled C10. P(ρ) peaks around 1.0, with mean value 0.93.

![image 26](Hot streaks in artistic cultural and scientific careers_images/imageFile26.png)

###### Figure S15: The ﬁtting results of 20 randomly selected artists. Each subplot denotes the Γ(N)sequence of an individual in our dataset, where blue dots denote data and red lines denote the bestﬁtting result of each individual.

![image 27](Hot streaks in artistic cultural and scientific careers_images/imageFile27.png)

###### Figure S16: The ﬁtting results for 20 randomly selected directors. Each subplot denotes theΓ(N) sequence of an individual in our dataset, where blue dots denote data and red lines denotethe best ﬁtting result of each individual.

![image 28](Hot streaks in artistic cultural and scientific careers_images/imageFile28.png)

###### Figure S17: The ﬁtting results for 20 randomly selected scientists. Each subplot denotes theΓ(N) sequence of an individual in our dataset, where blue dots denote data and red lines denotethe best ﬁtting result of each individual.

![image 29](Hot streaks in artistic cultural and scientific careers_images/imageFile29.png)

- Figure S18: Measuring the noise of Γ(N). The distribution P(σ) for (a) artists, (b) directors, and (c) scientists, where σ is the difference between real and ﬁtted Γ(N) sequence for all points in a domain. The blue dots denote data and the red line is a normal distribution. P(σ) peaks around zero for the three domains. The standard deviation for the normal distribution is 0.186 for artists, 0.229 for directors, and 0.189 for scientists, respectively.


![image 30](Hot streaks in artistic cultural and scientific careers_images/imageFile30.png)

- Figure S19: An illustration of R2 distribution. The distribution P(R2) of simulated careers for an individual in our dataset. The blue dots denote P(R2) calculated from 1000 simulated careers, the vertical blue line denotes R2 between data and ﬁtted Γ(N), and the dashed grey line is the R2 when p-value is 0.05.


![image 31](Hot streaks in artistic cultural and scientific careers_images/imageFile31.png)

- Figure S20: Impact before and after hot hand. The distribution of P(∆ Γ ) for (a) artists, (b) directors, and (c) scientists, where ∆ Γ measures the average impact difference before and after a hot streak. The blue dots denote data, and the red line is a normal distribution. The mean value of the normal distribution is 0.01 for artists, -0.02 for directors, and 0.02 for scientists, respectively.


![image 32](Hot streaks in artistic cultural and scientific careers_images/imageFile32.png)

- Figure S21: Individuals with one and more than one hot streaks. (a–c) The distribution of average impact for individuals with one, and more than one hot streaks for (a) artists, (b) directors, and (c) scientist. (d–f), The distribution of number of works P(N) within a career for individuals with one and more than one hot streaks across three domains. (g–i), The distribution of career length P(τ) for individuals with one and more than one hot streaks across three domains. The blue dot denotes individuals with one hot streak, and the orange dot denote the ones with at least two hot streaks.


![image 33](Hot streaks in artistic cultural and scientific careers_images/imageFile33.png)

- Figure S22: Γ for individuals with different number of hot streaks. (a–c), P(Γ0) of individuals with (≥ 1) and without hot streaks. P(Γ0) for artists is the same for the two population, while P(Γ0) is smaller for individuals with hot streaks for directors and scientists. (d–f), P(ΓH) of individuals with one and more than one hot streak. P(ΓH) for artists is the same for the two population. While for directors and scientists, individuals with more than one hot streaks have


smaller P(ΓH).

![image 34](Hot streaks in artistic cultural and scientific careers_images/imageFile34.png)

- Figure S23: Γ0 and ΓH in percentile. (a–c), The relationship between Γ0 and ΓH in percentile for (a) artists, (b) directors, and (c) scientists. The blue area denotes the kernal dentisy of data. The colored dots are the logarithmic binning of the data, where the color corresponds to different timing of hot streaks. The red line is a linear curve. The blue dot denotes the null model


prediction. Γ0 and ΓH follows a linear relationship measured in percentile.

![image 35](Hot streaks in artistic cultural and scientific careers_images/imageFile35.png)

###### Figure S24: Hot streaks for different scientiﬁc disciplines. (a) The proportion of scientists with

one hot streak in each discipline. (b) The average duration τH for scientists within each discipline.

![image 36](Hot streaks in artistic cultural and scientific careers_images/imageFile36.png)

- Figure S25: Q model validation for scientists. (a) The distribution P(N) for scientists, where dots denote data, and the red line corresponds to a log-normal function with average µ = 3.9 and standard deviation σ = 0.84. (b) The distribution P(Q) for scientists. The red line corresponds to


- a log-normal function with µ = 0.8 and σ = 0.58 (c) The highest impact log C10∗ versus the number of works N within a career. Each grey dot corresponds to an artist. The black circles are the logarithmic binning of the scattered data. The blue and red circles represent the prediction of


the Q-model and the hot-streak model, respectively. (d) log C10∗ versus log C10−∗) . Each grey dot corresponds to an artist, where log C10−∗) is the average impact within a career without log C10∗ .

![image 37](Hot streaks in artistic cultural and scientific careers_images/imageFile37.png)

- Figure S26: Q model validation for artists. (a) The distribution P(N) for artists, where dots denote data, and the red line corresponds to a log-normal function with average µ = 3.6 and standard deviation σ = 0.90. (b) The distribution P(Q) for artists. The red line corresponds to a log-normal function with µ = 1.1 and σ = 1.21 (c) The highest impact log(price∗) versus the number of works N within a career. Each grey dot corresponds to an artist. The black circles are the logarithmic binning of the scattered data. The blue circles represent the prediction of the Q-model. (d) log(price∗) versus log(price−∗) . Each grey dot corresponds to an artist, where


log(price−∗) is the average impact within a career without log(price∗).

![image 38](Hot streaks in artistic cultural and scientific careers_images/imageFile38.png)

- Figure S27: Q model validation for directors. (a) The distribution P(N) for directors, where dots denote data, and the red line corresponds to a log-normal function with average µ = 3.1 and standard deviation σ = 0.42. (b) The distribution P(Q) for directors. The red line corresponds to


- a log-normal function with µ = 0.9 and σ = 0.56 (c) The highest rating Rating∗ versus the number of works N within a career. Each grey dot corresponds to a director. The black circles are the logarithmic binning of the scattered data. The blue circles represent the prediction of the Q-model. (d) Rating∗ versus Rating−∗ . Each grey dot corresponds to a director, where


Rating−∗ is the average ratings within a career without Rating∗.

a b c

- Figure S28: g(t) under the null model. (a–c), The behaviour of g0(t) under the null model prediction with different (a) Γ0, (b) µ, and (c) σ parameters. We use Γ0 = 3.0, µ = 7.0, and σ = 1.0 as input.

a b c d

- Figure S29: g(t) under the hot-streak model. (a–d), g(t) under the hot-streak model prediction


with different (a) Γ0, (b) ∆Γ, (c) µ, and (d) σ parameters. For (a–c) we use ΓH = 4.0, Γ0 = 3.0, µ = 7.0, σ = 1.0, t↑ = 10 years and t↓ = 12 years as input. We use ΓH = Γ0 + 1.0 for (a).

a b c d

- Figure S30: Policy implications of g(t). (a–c) Individuals in our dataset with (a) mid, (b) late, and (c) early onset of the hot streak. Red dots denote data, the blue line is the null model’s prediction based on early performance, and the red line captures the predictions from the hot-streak model, with dashed grey lines denoting the start and end of hot streaks. (d) The difference ∆g(t) between our hot-streak model and the null model for each individual, where dashed lines with corresponding color denotes the start of a hot streak. (d) illustrates the systematic discrepancies in predicting individual’s future impact, if we ignore the uncovered hot streak phenomenon.


Hot-streak model

- Figure S31: The performance of different models. The distribution of P(MAPE) for the null model (orange dots) and our hot-streak model (blue dots). Compared with the null model, our hot-streak model has systematically smaller error.


##### Artists Directors

##### Scientists

g n u

Data

- a ah

Left trapezoid

- b
- c
- d
- e
- f


- o

- s

p

r

- t


- q


- v

- z

w

y

- aa


- x


0.4

0.4

QuadraticHot-handmodelRighttrapezoidIsoscelestrapezoidTent

- Hit 1

- Hit 2

- Hit 3


- Hit 1

- Hit 2

- Hit 3


0.3

0.3

˜N)P(

˜N)P(

0.2

0.2

0.1

0.1

0.0

0.0

1 2 3 4 5 6

1 2 3 4 5 6

HypothesisD

N˜

N˜

- i

k

m

- j


0.4

0.4

- Hit 1

- Hit 2

- Hit 3


- Hit 1

- Hit 2

- Hit 3


0.3

0.3

˜N)P(

˜N)P(

0.2

0.2

0.1

0.1

0.0

0.0

1 2 3 4 5 6

1 2 3 4 5 6

N˜

N˜

0.4

0.4

- Hit 1

- Hit 2

- Hit 3


- Hit 1

- Hit 2

- Hit 3


0.3

0.3

˜NP()

˜N)P(

0.2

0.2

0.1

0.1

0.0

0.0

1 2 3 4 5 6

1 2 3 4 5 6

N˜

N˜

0.4

0.4

- Hit 1

- Hit 2

- Hit 3


- Hit 1

- Hit 2

- Hit 3


0.3

0.3

˜N)P(

˜N)P(

0.2

0.2

0.1

0.1

0.0

0.0

1 2 3 4 5 6

1 2 3 4 5 6

N˜

N˜

l

0.4

0.4

- Hit 1

- Hit 2

- Hit 3


- Hit 1

- Hit 2

- Hit 3


0.3

0.3

˜N)P(

˜N)P(

0.2

0.2

0.1

0.1

0.0

0.0

1 2 3 4 5 6

1 2 3 4 5 6

N˜

N˜

0.4

0.4

- Hit 1

- Hit 2

- Hit 3


- Hit 1

- Hit 2

- Hit 3


0.3

0.3

˜N)P(

˜N)P(

0.2

0.2

0.1

0.1

0.0

0.0

1 2 3 4 5 6

1 2 3 4 5 6

N˜

N˜

- Figure S32: Alternative models of hot streaks. (a–f), An illustration of Γ(N) for the (a) hot-streak model, (b) right trapezoid function, (c) isosceles trapezoid function, (d) quadratic function, (e) tent function, and (f) left trapezoid function. (g), The distribution of the relative position P(N˜) of the top three hit works among the top six hits within a career for artists. The shades of color correspond to different hits.The relative position N˜ = 1 means the hit paper appears ﬁrst among the top six hit, whereas N˜ = 6 means the last one to appear. The relative order among the top six hits are random. The conclusion remains the same for (n) directors and (u) scientists. (h-m), P(N˜) predicted by corresponding model shown in (a–f) using artists’ proﬁles as input. We again use shades to color different hits. We measure the statistical difference between data and the model’s predictions, using the p-value of KS test for discrete distributions. We color the bars green if we cannot reject the hypothesis that data and model’s prediction come from the same distributions (p-value ≥ 0.05), and color them red otherwise. Among all alternative models considered, the hot-streak model turns out to be the only model that successfully reproduces the randomness observed in the top six hit works in (a). While the alternative functions show different trend of probability, contradicting to the randomness measured from data. We repeated the analyses using (o–t) directors’ proﬁles and (v–aa) scientists’ proﬁles as input, ﬁnding our results are robust to different domains.


