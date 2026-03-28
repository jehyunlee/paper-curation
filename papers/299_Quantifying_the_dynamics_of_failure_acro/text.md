## arXiv:1903.07562v1[physics.soc-ph]18 Mar 2019

###### Quantifying dynamics of failure across science, startups, and security

Yian Yin,1,2 Yang Wang,1,3 James A. Evans,4,5 Dashun Wang1,2,3

1Northwestern Institute on Complex Systems, Northwestern University, Evanston, IL 60208, USA 2McCormick School of Engineering, Northwestern University, Evanston, IL 60208, USA 3Kellogg School of Management, Northwestern University, Evanston, IL 60208, USA 4Department of Sociology, University of Chicago, Chicago, IL 60637, USA 5Santa Fe Institute, Santa Fe, NM 87501, USA

Human achievements are often preceded by repeated attempts that initially fail, yet little is known about the mechanisms governing the dynamics of failure. Here, building on the rich literature on innovation1–10, human dynamics11–17 and learning18–25, we develop a simple one-parameter model that mimics how successful future attempts build on those past. Analytically solving this model reveals a phase transition that separates dynamics of failure into regions of stagnation or progression, predicting that near the critical threshold, agents who share similar characteristics and learning strategies may experience fundamentally different outcomes following failures. Below the critical point, we see those who explore disjoint opportunities without a pattern of improvement, and above it, those who exploit incremental reﬁnements to systematically advance toward success. The model makes several empirically testable predictions, demonstrating that those who eventually succeed and those who do not may be initially similar, yet are characterized by fundamentally distinct failure dynamics in

terms of the efﬁciency and quality of each subsequent attempt. We collected large-scale data from three disparate domains, tracing repeated attempts by (i) NIH investigators to fund their research, (ii) innovators to successfully exit their startup ventures, and (iii) terrorist organizations to post casualties in violent attacks, ﬁnding broadly consistent empirical support across all three domains, which systematically veriﬁes each prediction of our model. Together, our ﬁndings unveil identiﬁable yet previously unknown early signals that allow us to identify failure dynamics that will lead to ultimate victory or defeat. Given the ubiquitous nature of failures and the paucity of quantitative approaches to understand them, these results represent a crucial step toward deeper understanding of the complex dynamics beneath failures, the essential prerequisites for success.

Henry Ford went bankrupt twice before founding the Ford Motor Company; J.K. Rowling was rejected by twelve publishers before introducing Harry Potter to the world; Yet neither came close to Thomas Edison, who famously failed more than a thousand times before identifying the carbon ﬁlament for the light bulb. To understand the dynamics of failure, here we collected three large-scale datasets from widely disparate domains (SI S1). The ﬁrst dataset (D1) contains all R01 grant applications ever submitted to the National Institutes of Health (NIH), the world’s largest public funder for biomedical research26–28 (776,721 applications by 139,091 investigators from 1985 to 2015, SI S1.1). For each grant application, we obtained ground-truth information on whether or not it was funded, allowing us to reconstruct individual application histories and their repeated attempts to obtain funding. Our second dataset (D2) traces start-up investment records from VentureXpert, the ofﬁcial database for National Venture Capital Association29 (58,111 startup

companies involving 253,579 innovators, SI S1.2). Tracing every startup invested by VCs from

1970 to 2016, D2 allows us to reconstruct individual career histories counting successive ventures in which they are involved. Here we follow prior studies in the entrepreneurship literature30,31, and classify successful ventures as those that achieved initial public offering (IPO) or high value merger and acquisition (M&A), and correspondingly failed attempts as those that failed to obtain such an exit within ﬁve years after their ﬁrst VC investment. Going beyond traditional innovation domains, we collected our third dataset (D3) from the Global Terrorism Database32, recording 170,350 terrorist attacks by 3,178 terrorist organizations from 1970 to 2017 (SI S1.3). For each organization we trace their attack histories33,34, and classify success as fatal attacks that killed at least one person, and correspondingly failure as those that failed to claim casualties.

Chance35,36 and learning19,23 are two primary mechanisms explaining how failures may lead to success. If each attempt has a certain likelihood of success, the probability that multiple attempts all lead to failure decreases exponentially with each trial. The chance model therefore emphasizes the role of luck, suggesting that success eventually arises from an accumulation of independent trials. To test this, we compared the performance of the ﬁrst and penultimate attempt within failure streaks (SI S4.1), measured by NIH percentile score for a grant application (D1), investment size by VCs to a company (D2), and number of wounded individuals by an attack (D3). We ﬁnd that across all three datasets, the penultimate attempt shows systematically better performance than the initial attempt (Figs. 1c-e, Student’s t-test, p = 1.10×10−8 (D1), 6.01×10−2 (D2), 3.95×10−5 (D3)). Figure 1a rejects that success is simply driven by chance but lends support to the learning mechanism (Fig. 1b), which suggests that failure, and experience more generally, may teach valuable

lessons difﬁcult to learn otherwise18,19,23,24,37,38. Hence, the more you fail, the more you learn, and the better you perform. As such, learning reduces the number of failures required to achieve success, predicting that failure streaks should follow a narrower length distribution (Fig. 1g) than the exponential one predicted by chance (Fig. 1f). Yet in contrast, across all three domains, failure streak length follows a fat-tailed distribution (Figs. 1h-j, SI S4.2), indicating that despite performance improvement, failures are characterized by longer-than-expected streaks prior to the onset of success. Together, these observations demonstrate that neither chance nor learning alone can explain the empirical patterns underlying failures, suggesting that more complex dynamics may be at work. This raises an intriguing question: What if real settings lie between chance and learning?

To explore this interplay, we develop a simple one-parameter model that in two limiting cases naturally recovers the main predictions of chance and learning (Fig. 2, SI S3.1). To mimic how future attempts build on previous failures, we consider that each attempt consists of many distinct components. Take for example the submission of an NIH proposal. Components include constructing a biosketch, assembling a budget, writing a data management plan, adding preliminary data, outlining broad impacts, etc. To simplify our model, here we assume the components are independent and unweighted, with each component i being characterized by an evaluation score x(i) (Fig. 2a).

To formulate a new attempt, one goes through each component, and decides to either (1) create a new version (with probability p), or (2) reuse the best version x∗ among the previous k attempts (with probability 1 − p) (Fig. 2b). A new version is assigned a score drawn randomly

from a uniform distribution U[0,1], approximating the percentile of any score distributions that real systems follow. The decision to create a new version is often not random, but driven by the quality of prior versions. Indeed, given the best version x∗, 1−x∗ captures the potential to improve it 23,24. The higher this potential, the more likely one may create a new version, prompting us to consider a simple relationship, p = (1 − x∗)α, with α > 0 (SI S3.6). Creating a new version takes one unit of time with no certainty that its score will be higher or lower than the previous one. By contrast, reusing the best version from the past saves time, and allows the component to retain its best score x∗.

Here we explore a single parameter k for our model, measuring the number of previous attempts one considers when formulating a new one (Fig. 2b). Mathematically the dynamical process can be described as

 

U[0,1], w.p. p

(1)

xn =



x∗n, w.p. 1 − p

where x∗n = max{xn−k,··· ,xn−1}. We quantify the dynamics of the model by calculating (1) the quality of the n-th attempt, xn , which measures the average score of all components and (2) the efﬁciency after that attempt, tn , which captures the expected proportion of components updated in new versions. Let us ﬁrst consider the two extreme cases:

k = 0 means each attempt is independent from those past (SI S3.2). Here the model recovers the chance model, predicting that as n increases, both xn and tn stay constant (Figs. 2cf). That is, without considering past experience, failure does not lead to quality improvement. Nor is it

more efﬁcient to try again.

The other extreme (k → ∞) considers all past attempts. The model predicts a temporal scaling in failure dynamics (SI S3.3). That is, the time it takes to formulate a new attempt decays with n, asymptotically following a power law (Fig. 2h):

###### Tn ≡  tn / t1  ∼ n−γ, (2)

where γ = γ∞ = α/(α + 1) falls between 0 and 1. Besides an increased efﬁciency, new attempts also improve in quality, as the average potential for improvement decays following 1 − xn ∼ n−η∞, where η∞ = min{γ∞,1 − γ∞} (Fig. 2e). Therefore, in the limit of k → ∞, our model recovers the canonical result from the learning literature22,39–43, commonly known as Wright’s Law18,44,45. This is because, as experience accumulates, high-quality versions are preferentially retained, while their lower quality counterparts are more likely to receive updates. As fresh attempts improve in quality (Fig. 2d), they reduce the need to start anew, thus increasing the efﬁciency of future attempts (Fig. 2g).

These two limiting cases might lead one to suspect a gradual emergence of scaling behavior:

- as we learn from more failures, the scaling exponent γ might grow continuously from 0 to γ∞. On the contrary, as we tune parameter k, the scaling exponent follows a discontinuous pattern (Fig. 3a, SI S3.4), where γ only varies within a narrow interval of k∗ < k < k∗ + 1 (k∗ ≡ 1/α). Indeed, as we increase k, agents consider more past experiences. Yet, when k is small (k < k∗), the system converges back to the same asymptotic behavior as k = 0 (Fig. 3abe). In this region, although new versions build on past k attempts, k is not large enough to retain a good version


once it appears. As a result, while performance might improve slightly in the ﬁrst few attempts, it quickly saturates. In this region, agents reject prior attempts and thrash around for new versions, not gaining enough feedback to initiate a pattern of intelligent improvements, prompting us to call it the stagnation region. Once k passes the critical threshold k∗, however, scaling behavior emerges (Fig. 3acf), indicating that the system enters a region of progression, where failures lead to continuous improvement in both quality and efﬁciency. Nevertheless, with a single additional experience considered, the system quickly hits the second critical point k∗ + 1, beyond which the scaling exponent γ becomes independent of k (Fig. 3adg). This means, once k∗ + 1 number of prior failures are considered, the system is characterized by the same dynamical behavior as k → ∞. The second critical point indicates that k∗ + 1 attempts are sufﬁcient to recover the same rate of improvement as considering every failure from the past.

Most importantly, we show that the two critical points in our model can be mapped to phase transitions within a canonical ensemble consisting of three energy levels (Methods, SI S3.5). The uncovered phase transitions indicate that small variations at the microscopic level may lead to fundamentally different macroscopic behaviors. For example, two individuals near the critical point may initially appear identical in their learning strategy or other individual characteristics, yet depending on which region they inhabit, their outcomes following failures could differ dramatically (Figs. 3hi). In the progression region (k > k∗), agents exploit rapid reﬁnements to improve through past feedback. By contrast, those in the stagnation region (k < k∗) do not seem to proﬁt from failure, as their efforts stall in efﬁciency and saturate in quality. As such, the phase transitions we uncovered in our simple model make four distinct predictions, which we now test directly in the

contexts of science, startups, and security.

- Prediction A: Not all failures lead to success. While we tend to focus on examples that

eventually succeeded following failures, such as Ford, Rowling, and Edison, the stagnation region predicts that there exists a non-negligible fraction of cases that do not succeed following failures. We can test this prediction in our three datasets by measuring the number of failed cases that do not achieve eventual success. To eliminate the possibility that such individuals or organizations were simply in the process of formulating their next attempt, we focus on cases where it has been at least ﬁve years since their last failure. We ﬁnd that, across all three domains, members of the “non-success” group not only exist, but their size is of a similar order of magnitude as the success group (Figs. 4a-c inset). Interestingly, when we measure the number of consecutive failures for the non-success group, we ﬁnd that its distribution is statistically indistinguishable from that of the failure streaks (Figs. 4a-c, Kolmogorov-Smirnov test, p = 0.286 (D1), 0.175 (D2), 0.931 (D3)), indicating that people who ultimately succeeded did not try more or less than their non-successful counterparts.

- Prediction B: Early dynamical signals separate the success group from the non-success


group. The model predicts that the success group is characterized by power-law temporal scaling (Eq. 2), which is absent for the non-success group (Fig. 3h). Therefore, those who eventually succeed and those who do not may be initially similar but can follow fundamentally different failure dynamics distinguishable at an early stage. To test this prediction, we measure the average interevent time between two failures Tn as a function of the number of failures (SI S4.3). Figures 4d-f

unveil three important observations.

- (i) For the success group, Tn decays with n across all three domains, approximately following a power law, as captured by (2) (Fig. 4j, SI S4.3). The scaling exponents are within a similar range as those reported in learning curves18,21, further supporting the validity of power law scaling. Although the three datasets are among the largest in their respective domains, agents with a large number of failures are exceedingly rare, limiting the range of n that can be measured empirically. We therefore test if alternative functions may offer a better ﬁt, ﬁnding power law to be the consistently preferred choice (SI S5.2).
- (ii) The temporal scaling disappears, when we measure the same quantity for the non-success group (Figs. 4d-f), consistent with predictions of the stagnation region in our model. Regression analysis

further supports this observation, showing that the association between Tn and n is not statistically signiﬁcant.

- (iii) The two groups show clearly distinguishable failure dynamics as early as n = 2 (Student’s


t-test, p = 4.57×10−3 (D1), 7.73×10−3 (D2), 4.99×10−2 (D3)), demonstrating intriguing early signals that separate those who eventually succeed from those who do not.

The observations uncovered in Figs. 4d-f are intriguing for two main reasons. First, failures captured by the three datasets differ widely in their scope, scale, deﬁnition, and temporal resolution, yet despite these differences, they are characterized by remarkably similar dynamical patterns predicted by our simple model. Second, membership in the two groups appears to be determined by the last attempt only. For example, comparing agents who failed 10 times but succeeded on the 11th with those who gave up after 10 failures, one might expect that it was the

last attempt that separated the two cases. Yet, as the model predicts, the success and non-success group each follows their respective, highly predictable patterns, distinguishable long before the eventual outcome becomes apparent. Indeed, we use D1 to set up a prediction task (see Methods), to predict the ultimate victory or defeat using only the temporal features, yielding a substantial predictive power. Despite the ubiquity of power laws across a wide variety of settings13–16,46–48 and the foundational literature on learning curves18,20,22,40–45,49 (SI S2), none of the existing models, to our knowledge, anticipated the existence of such early signals (Table S1). To test if the observed patterns in Figs. 4d-f may simply reﬂect preexisting population differences, we take agents who experienced a large number of failures (large n, hence most different toward the end), and measure their performance during the ﬁrst attempt. We ﬁnd that for all three domains, the two populations were statistically indistinguishable in their initial performance (Figs. 4g-i), which leads us to the next prediction:

Prediction C: Diverging patterns of performance improvement. Although the two groups may have begun with similar performance, the model predicts that they experience different performance gains through failures (Fig. 3i). We therefore compared performance at ﬁrst and sec-

- ond attempts, ﬁnding signiﬁcant performance improvement for the success group (Figs. 4g-i,


p = 9.28 × 10−2 (D1), 4.18 × 10−2 (D2), 5.49 × 10−3 (D3)), which is absent for the non-success group (p = 0.492 (D1), 0.219 (D2), 0.824 (D3)). We further repeated our measurements by comparing the ﬁrst and penultimate attempt, and the ﬁrst and halfway attempt, and for both cases, we arrive at the same conclusion (SI S6.3, Fig. S28). This prediction explains the patterns observed in Figs. 1c-e, which leads us to the second puzzle raised by Fig. 1: if performance improves, why are

failure streaks longer than we expect?

One key difference between the success and non-success groups is their propensity to reuse past components. From the perspective of exploration vs. exploitation50,51, although reuse helps

- one to retain a good version when it appears, it could also keep one in a suboptimal position for longer. Indeed, we analytically calculate the streak length distribution predicted by our model, offering our ﬁnal prediction: Prediction D: The length of failure streaks follows a Weibull distribution (Fig. 4k):

P(N ≥ n) ∼ e−(n/λ)

β

, (3)

which explains its fat-tailed nature observed in Figs. 1h-j. Moreover, the shape parameter β is connected with the temporal scaling exponent γ through a scaling identity (SI S3.8)

β + γ = 1. (4)

This means, if we ﬁt the streak length distribution in Figs. 1h-j to obtain the shape parameter β (Fig. 4k), it should relate to the temporal scaling exponent γ (Fig. 4j), obtained from Figs. 4d-f. Comparing β and γ measured independently across all three datasets shows consistency between our data and the scaling identity (Eq. 4) (Fig. 4l).

We further test the robustness of our results along several dimensions (SI S6). We vary the

deﬁnitions of success group (S6.1) by excluding revisions in D1 (Fig. S20), changing the threshold

- of high-value M&As in D2 (Figs. S24-25), and restricting types of attacks in D3 (Fig. S26). We also vary the deﬁnition of non-success groups (S6.2, Figs. S14-19), and test other measures to ap-


proximate performance (S6.3-S6.4, Figs. S23,S27). Across all variations, our conclusions remain the same.

An alternative interpretation for the stalled efﬁciency of the non-success group is a hedging behavior against failures—their efﬁciency did not improve because they spent more effort elsewhere. The three professions we studied, ranging from NIH investigators to entrepreneurs to terrorists, involve varied levels of risk, exposure, and commitment, which renders this explanation less likely. Nevertheless, one irony suggested by our model is that agents in the stagnation region did not work less. Rather they made more, albeit unnecessary modiﬁcations to what were otherwise advantageous experiences.

The model also offers relevant insights for the understanding of learning curves. For example, the second critical point of the model suggests the existence of a minimum number of failures one needs to consider (k∗ + 1), indicating that it is not necessary to learn from all past experiences to achieve a maximal learning rate. This ﬁnding poses a potential explanation for the widespread nature of Wright’s law across a wide variety of domains, particularly given the fact that in many of those domains not all past experiences can be considered (SI S2).

The one-parameter model developed here represents a minimal model (SI S3.7), which can be further extended into richer frameworks with more ﬂexible assumptions. For example, α captures the propensity to change given feedback, and so can be leveraged to incorporate population heterogeneity into the model, pointing to promising future research that explores the interplay between α and k parameters. Further, the assumed relationship between p and (1−x∗) is not limited

to a power law but can be relaxed into its asymptotic form. Indeed, we show that, as long as the

∗) → α as x∗ → 1, the model offers the same predictions42 (SI S3.6). Lastly, as a simple model, it does not take into account many of the complexities in real settings that may affect failure dynamics, such as knowledge depreciation52, forgetting and transfer37 or vicarious learning from others53. Despite its simplicity, the model accurately predicts several fundamental patterns governing the dynamics of failure. As such, it also offers a theoretical basis, where additional factors can be incorporated, including individual and organizational characteristics that may affect eventual success and failure outcomes18,54.

function satisﬁes ln(1ln−px

Together, these results support the hypothesis that if future attempts systematically build on past failures, the dynamics of repeated failures may reveal statistical signatures discernible at an early stage. Traditionally the main distinction between ultimate victory and defeat following failure has been attributed to differences in luck, learning strategies or individual characteristics, but here our model offers an important new explanation with crucial implications: Even in the absence of distinguishing initial characteristics, agents may experience fundamentally different outcomes. Indeed, Thomas Edison once said, ‘Many of life’s failures are people who did not realize how close they were to success when they gave up.’ Our results unveil identiﬁable early signals that help us predict and anticipate the eventual victory or defeat to which failures lead. Together, they not only deepen our understanding of the complex dynamics beneath failure, they also hold lessons for individuals and organizations that experience failure and the institutions that aim to facilitate or hinder their eventual breakthrough.

###### Methods

Phase transitions. To understand the nature of two transition points of our model, we consider a

canonical ensemble of N particles (N → ∞) and three energy states Ea(h) = 1, Eb(h) = (2h − 1)2, and Ec(h) = 1, where h denotes the external ﬁeld. We can write down the partition function of the system Z = e−NE

c(h), and calculate its free energy density f = lnZ/N. In this system, it can be shown that the magnetization density m = dhdf is discontinuous at the boundary of two energy states Ea(h) = Eb(h) and Eb(h) = Ec(h), characterized by two phase transitions at h = 0 and h = 1, respectively.

a(h) +e−NE

b(h) +e−NE

We notice that the canonical ensemble considered above has a one-to-one mapping to our model. Indeed, denoting with Γ ≡ k∗γ/(1−γ) and K ≡ k −k∗, we can rescale the system as Γ =

min{max{Γa(K),Γb(K)},Γc(K)}, where Γa(K) = 0, Γb(K) = K, and Γc(K) = 1, allowing us to map the two systems through f → (2Γ − 1)2, N → lnn, h → K, and Ei(h) = [2Γ2i(K) − 1]2 (Fig. S8).

To understand the origin of the two transition points, we can calculate the expected life span of a high-quality version, obtaining u(x)  ∼  (1−x)−min{k/k∗,1/k∗+1} (SI S3.4). The ﬁrst critical point k∗ occurs when the ﬁrst moment u diverges. Indeed, when k is small (k < k∗), u is ﬁnite, indicating high-quality versions can only be reused for a limited period. Once k passes the critical point k∗, however, u diverges, offering the possibility for a high-quality version to be retained for an unlimited period of time. The second critical point arises due to the competition between two dynamical forces: (a) whether the current best version gets forgotten after k consecutive attempts

in creating new versions (dominated by the k/k∗ term); or (b) it is substituted by an even better version (dominated by the 1/k∗ + 1 term).

Predicting ultimate success. We use a simple logistic model to predict whether one may achieve

success following N previously failed attempts in D1, using only temporal features tn (1 ≤ n ≤ N − 1) as predictors. To evaluate prediction accuracy, we calculate the AUC curve over 10-fold cross validation. We ﬁnd that, by observing timing of the ﬁrst three failures alone, our simple temporal feature yields high accuracy in predicting the eventual outcome with an AUC close to

- 0.7, signiﬁcantly higher than random guessing (Mann-Whitney rank test, p < 10−180, SI S5.1,

Fig. S10a). We repeated the same prediction task on D2 and D3, arriving at similar conclusions (SI

- S5.1, Fig. S10). The predictive power documented here is somewhat unexpected. Indeed, there are a large number of documented factors that affect the outcome of a grant application27,55–58, ranging from prior success rate to publication and citation records to race and ethnicity of the applicant. Yet here we have blatantly ignored these factors, using only features pertaining to temporal scaling as prescribed by our model. This suggests that this predictive power represents a lower-bound, which could be further improved and leveraged by incorporating additional factors.


- 1. Fortunato, S. et al. Science of science. Science 359, eaao0185 (2018).
- 2. Azoulay, P. et al. Toward a more scientiﬁc science. Science 361, 1194–1197 (2018).
- 3. Harford, T. Adapt: Why success always starts with failure (Farrar, Straus and Giroux, 2011).
- 4. Fleming, L. Recombinant uncertainty in technological search. Management science 47, 117–


- 132 (2001).
- 5. Wuchty, S., Jones, B. F. & Uzzi, B. The increasing dominance of teams in production of knowledge. Science 316, 1036–1039 (2007).
- 6. Jones, B. F. The burden of knowledge and the death of the renaissance man: Is innovation getting harder? The Review of Economic Studies 76, 283–317 (2009).
- 7. Petersen, A. M., Riccaboni, M., Stanley, H. E. & Pammolli, F. Persistence and uncertainty in the academic career. Proceedings of the National Academy of Sciences 109, 5213–5218

(2012).

- 8. Clauset, A., Arbesman, S. & Larremore, D. B. Systematic inequality and hierarchy in faculty hiring networks. Science advances 1, e1400005 (2015).
- 9. Sinatra, R., Wang, D., Deville, P., Song, C. & Barab´asi, A.-L. Quantifying the evolution of individual scientiﬁc impact. Science 354, aaf5239 (2016).
- 10. Liu, L. et al. Hot streaks in artistic, cultural, and scientiﬁc careers. Nature 559, 396 (2018).
- 11. Jara-Figueroa, C., Jun, B., Glaeser, E. L. & Hidalgo, C. A. The role of industry-speciﬁc, occupation-speciﬁc, and location-speciﬁc knowledge in the growth and survival of new ﬁrms. Proceedings of the National Academy of Sciences 115, 12646–12653 (2018).
- 12. Hidalgo, C. Why information grows: The evolution of order, from atoms to economies (Basic Books, 2015).


- 13. Barabasi, A.-L. The origin of bursts and heavy tails in human dynamics. Nature 435, 207–211

(2005).

- 14. Gonzalez, M. C., Hidalgo, C. A. & Barabasi, A.-L. Understanding individual human mobility patterns. Nature 453, 779–782 (2008).
- 15. Brockmann, D., Hufnagel, L. & Geisel, T. The scaling laws of human travel. Nature 439, 462–465 (2006).
- 16. Castellano, C., Fortunato, S. & Loreto, V. Statistical physics of social dynamics. Reviews of modern physics 81, 591 (2009).
- 17. Malmgren, R. D., Stouffer, D. B., Campanharo, A. S. & Amaral, L. A. N. On universality in human correspondence activity. Science 325, 1696–1700 (2009).
- 18. Argote, L. & Epple, D. Learning curves in manufacturing. Science 247, 920 (1990).
- 19. Sitkin, S. B. Learning through failure: the strategy of small losses. Research in organizational behavior 14, 231–266 (1992).
- 20. Yelle, L. E. The learning curve: Historical review and comprehensive survey. Decision sciences 10, 302–328 (1979).
- 21. Dutton, J. M. & Thomas, A. Treating progress functions as a managerial opportunity. Academy of management review 9, 235–247 (1984).
- 22. Shrager, J., Hogg, T. & Huberman, B. A. A graph-dynamic model of the power law of practice and the problem-solving fan-effect. Science 242, 414–416 (1988).


- 23. Levitt, B. & March, J. G. Organizational learning. Annual review of sociology 14, 319–338

(1988).

- 24. Huber, G. P. Organizational learning: The contributing processes and the literatures. Organization science 2, 88–115 (1991).
- 25. Edmondson, A. Psychological safety and learning behavior in work teams. Administrative science quarterly 44, 350–383 (1999).
- 26. Gross, C. P., Anderson, G. F. & Powe, N. R. The relation between funding by the national institutes of health and the burden of disease. New England Journal of Medicine 340, 1881– 1887 (1999).
- 27. Ginther, D. K. et al. Race, ethnicity, and nih research awards. Science 333, 1015–1019 (2011).
- 28. Li, D. & Agha, L. Big names or big ideas: Do peer-review panels select the best science proposals? Science 348, 434–438 (2015).
- 29. Kaplan, S. N. & Lerner, J. Venture capital data: Opportunities and challenges. In Measuring Entrepreneurial Businesses: Current Knowledge and Challenges (University of Chicago Press, 2016).
- 30. Eggers, J. & Song, L. Dealing with failure: Serial entrepreneurs and the costs of changing industries between ventures. Academy of Management Journal 58, 1785–1803 (2015).
- 31. Gompers, P., Kovner, A., Lerner, J. & Scharfstein, D. Performance persistence in entrepreneurship. Journal of Financial Economics 96, 18–32 (2010).


- 32. National Consortium for the Study of Terrorism and Responses to Terrorism (START). Global Terrorism Database [Data ﬁle] (2018).
- 33. Clauset, A. & Gleditsch, K. S. The developmental dynamics of terrorist organizations. PloS one 7, e48633 (2012).
- 34. Johnson, N. et al. Pattern in escalations in insurgent and terrorist activity. Science 333, 81–84

(2011).

- 35. Durrett, R. Probability: theory and examples (Cambridge university press, 2010).
- 36. Bass, R. F. Stochastic processes, vol. 33 (Cambridge University Press, 2011).
- 37. Argote, L. Organizational learning: Creating, retaining and transferring knowledge (Springer Science & Business Media, 2012).
- 38. Dahlin, K. B., Chuang, Y.-T. & Roulet, T. J. Opportunity, motivation, and ability to learn from failures and errors: Review, synthesis, and ways to move forward. Academy of Management Annals 12, 252–277 (2018).
- 39. Levy, F. K. Adaptation in the production process. Management Science 11, B–136 (1965).
- 40. Newell, A. & Rosenbloom, P. S. Mechanisms of skill acquisition and the law of practice. Cognitive skills and their acquisition 1, 1–55 (1981).
- 41. Anderson, J. R. Acquisition of cognitive skill. Psychological review 89, 369 (1982).
- 42. Muth, J. F. Search theory and the manufacturing progress function. Management Science 32, 948–962 (1986).


- 43. McNerney, J., Farmer, J. D., Redner, S. & Trancik, J. E. Role of design complexity in technology improvement. Proceedings of the National Academy of Sciences 108, 9008–9013 (2011).
- 44. Wright, T. P. Factors affecting the cost of airplanes. Journal of the aeronautical sciences 3, 122–128 (1936).
- 45. Snoddy, G. S. Learning and stability: a psychophysiological analysis of a case of motor learning with clinical applications. Journal of Applied Psychology 10, 1 (1926).
- 46. Clauset, A., Shalizi, C. R. & Newman, M. E. Power-law distributions in empirical data. SIAM review 51, 661–703 (2009).
- 47. Barab´asi, A.-L. & Albert, R. Emergence of scaling in random networks. Science 286, 509–512

(1999).

- 48. Bettencourt, L. M., Lobo, J., Helbing, D., K¨uhnert, C. & West, G. B. Growth, innovation, scaling, and the pace of life in cities. Proceedings of the national academy of sciences 104, 7301–7306 (2007).
- 49. Ritter, F. E. & Schooler, L. J. The learning curve. International encyclopedia of the social and behavioral sciences 13, 8602–8605 (2001).
- 50. March, J. G. Exploration and exploitation in organizational learning. Organization science 2, 71–87 (1991).
- 51. Foster, J. G., Rzhetsky, A. & Evans, J. A. Tradition and innovation in scientists research strategies. American Sociological Review 80, 875–908 (2015).


- 52. Arbesman, S. The half-life of facts: Why everything we know has an expiration date (Penguin, 2013).
- 53. Madsen, P. M. & Desai, V. Failing to learn? The effects of failure and success on organizational learning in the global orbital launch vehicle industry. Academy of Management Journal 53, 451–476 (2010).
- 54. Cannon, M. D. & Edmondson, A. C. Failing to learn and learning to fail (intelligently): How great organizations put failure to work to innovate and improve. Long range planning 38, 299–319 (2005).
- 55. Boudreau, K. J., Guinan, E. C., Lakhani, K. R. & Riedl, C. Looking across and looking beyond the knowledge frontier: Intellectual distance, novelty, and resource allocation in science. Management Science 62, 2765–2783 (2016).
- 56. Bromham, L., Dinnage, R. & Hua, X. Interdisciplinary research has consistently lower funding success. Nature 534, 684 (2016).
- 57. Banal-Estanol, A., Macho-Stadler, I. & P´erez Castrillo, D. Key success drivers in public research grants: Funding the seeds of radical innovation in academia? (2016).
- 58. Ma, A., Mondrag´on, R. J. & Latora, V. Anatomy of funded research in science. Proceedings of the National Academy of Sciences 112, 14760–14765 (2015).


Acknowledgements The authors wish to thank Chaoming Song, Brain Uzzi, and Eli Finkel for help-

ful discussions. This paper makes use of restricted access data from the National Institutes of Health,

protected by the Privacy Act of 1974 as amended (5 U.S.C. 552a). De-identiﬁed data necessary to re-

produce all plots and statistical analyses will be made freely available. Those wishing to access the raw

data may apply for access following the procedures outlined in the NIH Data Access Policy document avail-

able at http://report.nih.gov/pdf/DataAccessPolicy.pdf. The VentureXpert database is available via Thomson

Reuters. The Global Terrorism Database is publicly available at https://www.start.umd.edu/gtd/. This work

is supported by the Air Force Ofﬁce of Scientiﬁc Research under award number FA9550-15-1-0162 and

FA9550-17-1-0089, National Science Foundation grant SBE 1829344, and Northwestern University Data

Science Initiative. This work does not reﬂect the position of NIH.

Competing Interests The authors declare that they have no competing ﬁnancial interests.

Correspondence Correspondence and requests for materials should be addressed to D.W.

(email: dashun.wang@northwestern.edu).

###### Figure captions

- Figure 1: The mechanisms of chance and learning. We compare theoretical predictions and empirical measurements for performance changes (a-r) as well as the length distribution of failure streaks (f-j). The chance model predicts no performance change (a), with failure streak length following an exponential distribution (f). The learning hypothesis predicts improved performance

- (b), with shorter failure streaks than expected by the chance model, corresponding to a fasterthan-exponential distribution (g). Both hypotheses are contested by empirical patterns observed across all three datasets. We measured the performance of an attempt based on NIH percentile


scores (D1), investment sizes (D2), and number of wounded individuals (D3). To ensure that performance metrics are comparable across data and models, we standardized performance measures according to their underlying distribution (SI S4.1). We ﬁnd that failures in real data are characterized improved performance between the ﬁrst and penultimate attempt (c-e). Yet at the same time, failure streaks are characterized by a fat-tailed length distribution, indicating that failure streaks in real data are longer than expected by chance (h-j).

- Figure 2: The k model. (a) Here we treat each attempt as a combination of independent compo-


nents (c(i)). For an attempt j, each component i is characterized by an evaluation score x(ji), which falls between 0 and 1. The score for a new version is often unknown until attempted, hence a new version is assigned a score, drawn randomly from [0,1], which approximates the percentile of any score distribution that real systems follow. (b) To formulate a new attempt, one can either create a new version (with probability p, green arrow in a), or reuse an existing version by choosing the best one among past versions x∗ (with probability 1 − p, red arrow in a). Reusing the existing

best version allows the particular component to retain its score x∗ and avoids incurring additional time cost. Creating a new version costs one unit of time but generates a new score x. Of the many factors that may inﬂuence p, one key factor is the quality of existing versions, suggesting that p should be a function of x∗. Indeed, consider the two extreme cases. If x∗ → 0, existing versions of this component have among the worst scores and, hence, a high potential for improvement with a new version. Therefore the likelihood of creating a new version is high, i.e., p → 1. On the other hand, x∗ → 1 corresponds to a near-perfect version, yielding a decreased incentive to create a new version (p → 0). Therefore, P(x ≥ x∗) = 1 − x∗ captures the potential to improve on prior versions, prompting us to assume p = (1 − x∗)α, where α > 0 characterizes an agent’s propensity to create new versions given the quality of existing ones. (c-h) Simulation results from the model (α = 0.6) for the cases of k = 0 (c,f) and k → ∞ (d,g) in terms of the average quality (c-e) and efﬁciency (f-h) of each attempt. k = 0 recovers the chance model, predicting a constant quality (c) and efﬁciency (f). k → ∞ predicts a temporal scaling characterizing the dynamics of failure (g) with an improved quality (d), recovering the predictions from learning curves and Wright’s Law.

- Figure 3: Phase diagram of the model. (a) Analytical solution of the model reveals that the system is separated into three regimes by two critical points k∗ and k∗ +1. The solid line shows an extended solution space of our analytical results. (b-g) Simulations results of the model (α = 0.6) for quality (b-d) and efﬁciency (e-g) trajectories for different k parameters, showing distinctive dynamical behavior in different regions separated by the two critical points. All results are based on simulations over 104 times. (h,i) Phase transition around k∗ predicts the coexistence of stagnation (k = 1, orange) and progression (k = 2, blue) groups.


- Figure 4: Testing model predictions. (a-c) Complementary cumulative distribution (CCDF) of the number of consecutive failures prior to the last attempt for the success (blue) and non-success groups (orange). In each of our three datasets, two distributions are statistically indistinguishable (Kolmogorov-Smirnov test for samples with at least one failures). (Inset) The sample size of success and non-success group, showing their size is of a similar order of magnitude. (d-f) Early temporal signals separate success and non-success groups. For each group we measure the average


inter-event time between two failures Tn ≡ tn/t1 as a function of the number of attempts. Dots and shaded areas show the mean and standard errors of the mean measured from data (SI S4.3). All success groups manifest power law scaling Tn ∼ n−γ, with γ reported in Table 1. This temporal scaling is absent for non-success groups. (g-i) Performance at ﬁrst attempt is indistinguishable between the success and non-success groups, but becomes distinguishable from the second attempt. Whereas performance improves for the success group, this improvement is absent for the nonsuccess group. (j-l) Parameter estimates (mean±standard error). γ corresponds to the temporal scaling exponent uncovered in (2) (j) and β is the shape parameter of the Weibull distribution, characterizing the length distribution of failure streaks (k). Statistical tests indicate that none of the three datasets can reject the validity of the scaling identity β + γ = 1 (l).

###### Performance Failure Streak

- a f
- b g
- c h
- d i
- e j


0.6

| | | | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |


|Hypotheis Exponential| | | |
|---|---|---|---|
| | | | |


100

Performance

###### StartupsNIH GrantsChanceLearningTerrorist Attacks

10−2

###### CCDF

0.5

10−4

10−6

0.4

0 10 20

First Penultimate

Number of failures

0.6

| | | | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |


|Hypotheis Exponential| | | |
|---|---|---|---|
| | | | |


100

Performance

10−2

###### CCDF

0.5

10−4

10−6

0.4

0 10 20

First Penultimate

Number of failures

0.8

| |***| | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |


|Data Exponential Model| | | |
|---|---|---|---|
| | | | |


100

Evaluationscore

0.7

10−2

###### CCDF

10−4

0.6

10−6

0.5

0 10 20

First Penultimate

Number of failures

0.4

| |*| | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |


|Data Exponential Model| | |
|---|---|---|
| | | |


100

Investmentamount

0.3

10−2

###### CCDF

10−4

0.2

10−6

0.1

0 10

First Penultimate

Number of failures

0.6

| |***| | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |


|Data Exponential Model| | | |
|---|---|---|---|
| | | | |


Woundedindividuals

100

0.5

10−1

###### CCDF

0.4

0.3

10−2

0.2

10−3

0.1

0 10 20

First Penultimate

Number of failures

Figure 1: The mechanisms of chance and learning.

![image 1](Quantifying the dynamics of failure across science startups and security_images/imageFile1.png)

![image 2](Quantifying the dynamics of failure across science startups and security_images/imageFile2.png)

![image 3](Quantifying the dynamics of failure across science startups and security_images/imageFile3.png)

![image 4](Quantifying the dynamics of failure across science startups and security_images/imageFile4.png)

![image 5](Quantifying the dynamics of failure across science startups and security_images/imageFile5.png)

![image 6](Quantifying the dynamics of failure across science startups and security_images/imageFile6.png)

![image 7](Quantifying the dynamics of failure across science startups and security_images/imageFile7.png)

![image 8](Quantifying the dynamics of failure across science startups and security_images/imageFile8.png)

![image 9](Quantifying the dynamics of failure across science startups and security_images/imageFile9.png)

a b

![image 10](Quantifying the dynamics of failure across science startups and security_images/imageFile10.png)

![image 11](Quantifying the dynamics of failure across science startups and security_images/imageFile11.png)

![image 12](Quantifying the dynamics of failure across science startups and security_images/imageFile12.png)

Repeated attempts j

xn-k

xn-

xn

![image 13](Quantifying the dynamics of failure across science startups and security_images/imageFile13.png)

![image 14](Quantifying the dynamics of failure across science startups and security_images/imageFile14.png)

![image 15](Quantifying the dynamics of failure across science startups and security_images/imageFile15.png)

![image 16](Quantifying the dynamics of failure across science startups and security_images/imageFile16.png)

![image 17](Quantifying the dynamics of failure across science startups and security_images/imageFile17.png)

![image 18](Quantifying the dynamics of failure across science startups and security_images/imageFile18.png)

![image 19](Quantifying the dynamics of failure across science startups and security_images/imageFile19.png)

![image 20](Quantifying the dynamics of failure across science startups and security_images/imageFile20.png)

![image 21](Quantifying the dynamics of failure across science startups and security_images/imageFile21.png)

![image 22](Quantifying the dynamics of failure across science startups and security_images/imageFile22.png)

![image 23](Quantifying the dynamics of failure across science startups and security_images/imageFile23.png)

![image 24](Quantifying the dynamics of failure across science startups and security_images/imageFile24.png)

![image 25](Quantifying the dynamics of failure across science startups and security_images/imageFile25.png)

……

1

![image 26](Quantifying the dynamics of failure across science startups and security_images/imageFile26.png)

![image 27](Quantifying the dynamics of failure across science startups and security_images/imageFile27.png)

![image 28](Quantifying the dynamics of failure across science startups and security_images/imageFile28.png)

![image 29](Quantifying the dynamics of failure across science startups and security_images/imageFile29.png)

![image 30](Quantifying the dynamics of failure across science startups and security_images/imageFile30.png)

![image 31](Quantifying the dynamics of failure across science startups and security_images/imageFile31.png)

![image 32](Quantifying the dynamics of failure across science startups and security_images/imageFile32.png)

![image 33](Quantifying the dynamics of failure across science startups and security_images/imageFile33.png)

![image 34](Quantifying the dynamics of failure across science startups and security_images/imageFile34.png)

![image 35](Quantifying the dynamics of failure across science startups and security_images/imageFile35.png)

0.28 0.74 0.74 0.53 ... 0.74

![image 36](Quantifying the dynamics of failure across science startups and security_images/imageFile36.png)

![image 37](Quantifying the dynamics of failure across science startups and security_images/imageFile37.png)

![image 38](Quantifying the dynamics of failure across science startups and security_images/imageFile38.png)

![image 39](Quantifying the dynamics of failure across science startups and security_images/imageFile39.png)

![image 40](Quantifying the dynamics of failure across science startups and security_images/imageFile40.png)

- c(1)

...

- c(2)


Recent k failures Best

Random

Componentsi

![image 41](Quantifying the dynamics of failure across science startups and security_images/imageFile41.png)

![image 42](Quantifying the dynamics of failure across science startups and security_images/imageFile42.png)

![image 43](Quantifying the dynamics of failure across science startups and security_images/imageFile43.png)

![image 44](Quantifying the dynamics of failure across science startups and security_images/imageFile44.png)

![image 45](Quantifying the dynamics of failure across science startups and security_images/imageFile45.png)

![image 46](Quantifying the dynamics of failure across science startups and security_images/imageFile46.png)

![image 47](Quantifying the dynamics of failure across science startups and security_images/imageFile47.png)

![image 48](Quantifying the dynamics of failure across science startups and security_images/imageFile48.png)

![image 49](Quantifying the dynamics of failure across science startups and security_images/imageFile49.png)

![image 50](Quantifying the dynamics of failure across science startups and security_images/imageFile50.png)

![image 51](Quantifying the dynamics of failure across science startups and security_images/imageFile51.png)

![image 52](Quantifying the dynamics of failure across science startups and security_images/imageFile52.png)

![image 53](Quantifying the dynamics of failure across science startups and security_images/imageFile53.png)

![image 54](Quantifying the dynamics of failure across science startups and security_images/imageFile54.png)

![image 55](Quantifying the dynamics of failure across science startups and security_images/imageFile55.png)

![image 56](Quantifying the dynamics of failure across science startups and security_images/imageFile56.png)

![image 57](Quantifying the dynamics of failure across science startups and security_images/imageFile57.png)

Step 1

![image 58](Quantifying the dynamics of failure across science startups and security_images/imageFile58.png)

![image 59](Quantifying the dynamics of failure across science startups and security_images/imageFile59.png)

![image 60](Quantifying the dynamics of failure across science startups and security_images/imageFile60.png)

![image 61](Quantifying the dynamics of failure across science startups and security_images/imageFile61.png)

![image 62](Quantifying the dynamics of failure across science startups and security_images/imageFile62.png)

![image 63](Quantifying the dynamics of failure across science startups and security_images/imageFile63.png)

0.13 0.61 0.53 0.61 ... 0.79

![image 64](Quantifying the dynamics of failure across science startups and security_images/imageFile64.png)

![image 65](Quantifying the dynamics of failure across science startups and security_images/imageFile65.png)

![image 66](Quantifying the dynamics of failure across science startups and security_images/imageFile66.png)

![image 67](Quantifying the dynamics of failure across science startups and security_images/imageFile67.png)

![image 68](Quantifying the dynamics of failure across science startups and security_images/imageFile68.png)

![image 69](Quantifying the dynamics of failure across science startups and security_images/imageFile69.png)

![image 70](Quantifying the dynamics of failure across science startups and security_images/imageFile70.png)

![image 71](Quantifying the dynamics of failure across science startups and security_images/imageFile71.png)

Create

![image 72](Quantifying the dynamics of failure across science startups and security_images/imageFile72.png)

- Step 2a
- Step 2b


x

![image 73](Quantifying the dynamics of failure across science startups and security_images/imageFile73.png)

![image 74](Quantifying the dynamics of failure across science startups and security_images/imageFile74.png)

x*

![image 75](Quantifying the dynamics of failure across science startups and security_images/imageFile75.png)

![image 76](Quantifying the dynamics of failure across science startups and security_images/imageFile76.png)

![image 77](Quantifying the dynamics of failure across science startups and security_images/imageFile77.png)

![image 78](Quantifying the dynamics of failure across science startups and security_images/imageFile78.png)

![image 79](Quantifying the dynamics of failure across science startups and security_images/imageFile79.png)

![image 80](Quantifying the dynamics of failure across science startups and security_images/imageFile80.png)

![image 81](Quantifying the dynamics of failure across science startups and security_images/imageFile81.png)

![image 82](Quantifying the dynamics of failure across science startups and security_images/imageFile82.png)

![image 83](Quantifying the dynamics of failure across science startups and security_images/imageFile83.png)

![image 84](Quantifying the dynamics of failure across science startups and security_images/imageFile84.png)

![image 85](Quantifying the dynamics of failure across science startups and security_images/imageFile85.png)

Probability p, tn ← tn+1

![image 86](Quantifying the dynamics of failure across science startups and security_images/imageFile86.png)

![image 87](Quantifying the dynamics of failure across science startups and security_images/imageFile87.png)

![image 88](Quantifying the dynamics of failure across science startups and security_images/imageFile88.png)

![image 89](Quantifying the dynamics of failure across science startups and security_images/imageFile89.png)

![image 90](Quantifying the dynamics of failure across science startups and security_images/imageFile90.png)

![image 91](Quantifying the dynamics of failure across science startups and security_images/imageFile91.png)

![image 92](Quantifying the dynamics of failure across science startups and security_images/imageFile92.png)

![image 93](Quantifying the dynamics of failure across science startups and security_images/imageFile93.png)

![image 94](Quantifying the dynamics of failure across science startups and security_images/imageFile94.png)

![image 95](Quantifying the dynamics of failure across science startups and security_images/imageFile95.png)

0.69 0.83 0.41 0.83 ... 0.83

![image 96](Quantifying the dynamics of failure across science startups and security_images/imageFile96.png)

![image 97](Quantifying the dynamics of failure across science startups and security_images/imageFile97.png)

![image 98](Quantifying the dynamics of failure across science startups and security_images/imageFile98.png)

![image 99](Quantifying the dynamics of failure across science startups and security_images/imageFile99.png)

![image 100](Quantifying the dynamics of failure across science startups and security_images/imageFile100.png)

p=[1-x*]α

![image 101](Quantifying the dynamics of failure across science startups and security_images/imageFile101.png)

![image 102](Quantifying the dynamics of failure across science startups and security_images/imageFile102.png)

OR

![image 103](Quantifying the dynamics of failure across science startups and security_images/imageFile103.png)

![image 104](Quantifying the dynamics of failure across science startups and security_images/imageFile104.png)

Reuse

x*

![image 105](Quantifying the dynamics of failure across science startups and security_images/imageFile105.png)

Probability 1-p, tn ← tn

Attempt 1 Attempt 2 Attempt 3 Attempt 4 N

###### k = 0 k = ∞

0

0

10

10

0

0

e

c d

| |k = 0<br><br>k = ∞|
|---|---|
| | |
| | |
| | |
| | |


|![image 106](Quantifying the dynamics of failure across science startups and security_images/imageFile106.png)| |
|---|---|
| | |
| | |
| | |
| | |
| | |
| | |
| | |


|![image 107](Quantifying the dynamics of failure across science startups and security_images/imageFile107.png)| |
|---|---|
| | |
| | |
| | |
| | |
| | |
| | |
| | |


![image 108](Quantifying the dynamics of failure across science startups and security_images/imageFile108.png)

![image 109](Quantifying the dynamics of failure across science startups and security_images/imageFile109.png)

- 2 × 10−1
- 3 × 10−1
- 4 × 10−1


10

10

###### QualityEfficiency

Components

Components

−1xn

20

20

−1xn

−1xn

− 4

− 4

10

10

30

30

40

40

− 8

− 8

50

50

10

10

100 101 102

0 10 20 30 40 50

0 10 20 30 40 50

Attempts

Attempts

n

0

0

- 0
- 1


- 0
- 1


![image 110](Quantifying the dynamics of failure across science startups and security_images/imageFile110.png)

![image 111](Quantifying the dynamics of failure across science startups and security_images/imageFile111.png)

|k = 0<br><br>k = ∞|
|---|


100

h

f g

10

10

6 × 10−1

Components

Components

20

20

- 2 × 10−1
- 3 × 10−1
- 4 × 10−1


tn

Tn

tn

30

30

40

40

50

50

100 101 102

0 10 20 30 40 50

0 10 20 30 40 50

Attempts

Attempts

n

Figure 2: The k model.

a

γ-10*（）+1k

###### Stagnation Progression

k* k*+ 1

k

b c d

| |
|---|


| |
|---|


| |
|---|


100

100

100

EfficiencyQuality

−1xn

−1xn

−1xn

10−1

10−1

10−1

10−2

10−2

10−2

100

101 102 103 104

100

101 102 103 104

100

101 102 103 104

n

n

n

| |
|---|


| |
|---|


| |
|---|


e f g

100

100

100

10−1

10−1

10−1

Tn

Tn

Tn

10−2

10−2

10−2

100

101 102 103 104

100

101 102 103 104

100

101 102 103 104

n

n

n

2 × 100

100

h i

|= k = 1 k 2<br><br>|
|---|


|= k = 1 k 2<br><br>|
|---|


Predictions

6 × 10−1

100

Model

- 2 × 10−1
- 3 × 10−1
- 4 × 10−1


−1xn

Tn

6 × 10−1

- 2 × 10−1
- 3 × 10−1
- 4 × 10−1


10−1

100

101 102

100

101 102

n

n

###### Figure 3: Phase diagram of the model.

###### NIH Grants Terrorist Attacks

###### Startups

a

b

c

1.0

1.0

1.0

0.8

0.8

0.8

- 100
- 101
- 102
- 103
- 104


- 100
- 101
- 102
- 103
- 104
- 105
- 106


- 100
- 101
- 102
- 103
- 104
- 105
- 106


0.6

0.6

0.6

###### CDF

###### CDF

###### CDF

Sample size

Sample size

Sample size

0.4

0.4

0.4

0.2

0.2

0.2

Success Non-success

Success Non-success

Success Non-success

0.0

0.0

0.0

5 10 15

5 10 15 20

5 10 15 20

Number of failures

Number of failures

Number of failures

d

e

f

| |
|---|


| |
|---|


| |
|---|


100

100

100

Tn

Tn

Tn

10−1

10−1

10−1

100 2× 100 3× 1004× 100 6× 100

100 2× 100 3× 100 4× 100

100 101

n

n

n

g

h

i

0.9

0.6

0.8

| |NS<br><br>***<br><br>***<br><br>NS| | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |


| |NS<br><br>***<br><br>**<br><br>NS| | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |


| |NS **<br><br>*<br><br>NS| | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |


0.7

0.5

Woundedindividuals

0.8

0.6

Investmentamount

Evaluationscore

0.4

0.5

0.7

0.4

0.3

0.3

0.2

0.6

0.2

0.1

0.1

0.0

0.0

0.5

First failure Second failure

First failure Second failure

First failure Second failure

- j

β = 0.666±0.017 β = 0.566±0.086 β = 0.143±0.039

γ = 0.361±0.010 γ = 0.509±0.036 γ = 0.668±0.143

p = 0.176 p = 0.421 p = 0.200

- k
- l


Figure 4: Testing model predictions.

###### Supplementary Information for Quantifying dynamics of failure across science, startups, and security

Yian Yin,1,2 Yang Wang,1,3 James A. Evans,4,5 Dashun Wang1,2,3

1Northwestern Institute on Complex Systems, Northwestern University, Evanston, IL 60208, USA 2McCormick School of Engineering, Northwestern University, Evanston, IL 60208, USA 3Kellogg School of Management, Northwestern University, Evanston, IL 60208, USA 4Department of Sociology, University of Chicago, Chicago, IL 60637, USA 5Santa Fe Institute, Santa Fe, NM 87501, USA

###### Contents

###### S1 Data description 3

- S1.1 NIH grant application dataset . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
- S1.2 VentureXpert investment dataset . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
- S1.3 GTD terrorism attack dataset . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
- S1.4 Data limitations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7


###### S2 Related work and models 8

- S2.1 Learning literature . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
- S2.2 Stochastic models with memory . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
- S2.3 Adaptation models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
- S2.4 Search models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
- S2.5 Individual learning models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
- S2.6 Urn models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
- S2.7 Other models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18


###### S3 Modeling failure dynamics 21

- S3.1 The k model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
- S3.2 Independent model (k = 0) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
- S3.3 Learning from all failures (k → ∞) . . . . . . . . . . . . . . . . . . . . . . . . . 23
- S3.4 Solving the general model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
- S3.5 Connections with canonical ensembles . . . . . . . . . . . . . . . . . . . . . . . . 31
- S3.6 Functional forms of ρ(x) and p(x) . . . . . . . . . . . . . . . . . . . . . . . . . . 34
- S3.7 Null models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
- S3.8 Failure streak length . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38


###### S4 Empirical measurements 42

- S4.1 Quantifying performance dynamics . . . . . . . . . . . . . . . . . . . . . . . . . . 42
- S4.2 Length distribution of failure streaks . . . . . . . . . . . . . . . . . . . . . . . . . 44
- S4.3 Measuring failure dynamics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44


###### S5 Prediction task 46

- S5.1 Predicting ultimate success . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
- S5.2 Testing power law model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48


###### S6 Robustness checks 49

- S6.1 Deﬁnition of successes and failures . . . . . . . . . . . . . . . . . . . . . . . . . . 49
- S6.2 Threshold for being inactive in the system . . . . . . . . . . . . . . . . . . . . . . 49
- S6.3 Comparing ﬁrst failures versus halfway/penultimate failures . . . . . . . . . . . . 50
- S6.4 Other checks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50


###### S1 Data description

In this project, we compiled a comprehensive database consisting of three large-scale datasets

across three different domains: Dataset D1 contains submission histories of individual scientists in the US National Institutes of Health (NIH) grant system. D2 contains proﬁles of innovators together with their startup ventures recorded in the VentureXpert investment database. D3 records terrorist organizations and attacks retrieved from the Global Terrorism Database.

###### S1.1 NIH grant application dataset

Our ﬁrst dataset contains all R01 grant applications (776,721 in total) that have been ever submitted by 139,091 scientists to NIH from 1985 to 2015. For each grant application, we obtained its evaluation score (if reviewed on a panel), a unique identiﬁer for the PI, the PI’s name, and the application outcome (funded/not funded).

The NIH grant application dataset represents an excellent setting to study dynamics of failure for several reasons. First, it contains ground-truth information for both successes and failures. Second, as the world’s largest public funder for biomedical research, NIH is the dominant funding source for biomedical scientists in the US28,50. Indeed we tracked funding acknowledgment information cited within biomedical research papers, ﬁnding among all PubMed papers published in the US (2008 to 2015), NIH indeed represents the majority of funding sources (81% out of top 10 agencies) (Fig. S1a).

R01 is the most common research funding mechanism within the NIH26–28, accounting for the majority of the total funding. To compare the dynamical pattern between R01 and other granting mechanisms, we downloaded successful NIH grants from other mechanisms from NIH Research Portfolio Online Reporting Tools (RePORT), ﬁnding R01 grants are uniformly distributed within all NIH grants one obtains throughout a career (Fig. S1b).

Here we extract all new grant applications (excluding renewals, revisions and resubmissions) to reconstruct sequences of attempts (Fig. S2a). We truncate each sequence if (i) the individual gets one grant (success group, Fig. S2b); or (ii) the individual has been inactive for a long period (nonsuccess group). Here we show results using all failure samples in main text. We also repeated our results using just the ﬁrst sequence of failures—failure streak without prior success, ﬁnding our conclusions remain the same (Fig. S21,S22). We also ﬁnd that the observed patterns are not affected by any potential periodicity of grant applications, and the results are robust against such variants. Indeed, we ﬁnd the results remain the same if we add to timestamp of each attempt an artiﬁcial random noise at the scale of review cycles (∼ 120 days).

###### S1.2 VentureXpert investment dataset

Our second dataset traces start-up investment records from the VentureXpert (SDC Platinum) database, including 58,111 startup companies and 163,106 investment rounds from 1970 to 2016. For each investment we obtained information on investment amount, funding date, company name and a full list of innovators involved. We then link these records with company information on

Initial Public Offering and Merge & Acquisitions as outcome variables. Following deﬁnitions in entrepreneurship literature30,31,51, we match individual entrepreneurs and startup ventures by linking each company with people listed as executives or board members at the ﬁrst funding round. One advantage of this dataset is that 98.7% records have complete information of ﬁrst and last names rather than initials, allowing us to construct career trajectories of 253,579 innovators.

Among the existing datasets capturing startups, the VentureXpert database, the ofﬁcial database

of the National Venture Capital Association is among the most comprehensive and authoritative databases29. To further explore the coverage of the database, we compare the number of IPOs within our data versus US total counts, ﬁnding our dataset captures a signiﬁcant fractions of IPOs, with the ratio between the two statistics remaining stable across time (Fig. S3), documenting the reliability of this dataset. We also cross-validated individual entrepreneurs coverage with Crunchbase, an online platform of business information. We select top 1000 serial executives and board members ranked by the number of different jobs in Crunchbase, ﬁnding more than 70% of the proﬁles are included in VentureXpert as well. Overall, these statistics document that our dataset has excellent coverage through various validation efforts.

Another challenge in modeling dynamics of failure in startup datasets is the ambiguity of ‘failures’52, which could include bankruptcy, termination to prevent future losses, and deviation from desired results. Recognizing the complexity of this issue, here we closely follow existing literature on venture capital and serial entrepreneurship30,31. We focus on all portfolio companies that have received at least one round of funding, and deﬁne those who went public or get acquired

or merged at high values (percentile as compared with all M&As in the same year) as successes. We performed different variants of measurements by changing the percentile threshold (1% and 5%) and also by only including IPO (Figs. S24,S25). We ﬁnd our results remain the same. If a company obtained its ﬁrst investment but did not succeed within a certain period, this venture is marked as a failure. In this dataset we treat each new venture as an attempt, starting at the date of ﬁrst round investment. Similar to D1, sequences of attempts by each individual are collected into a sequence, where the stopping criterion is deﬁned by (i) the individual has one company that eventually achieved IPO or high-value M&As (success-group); (ii) the individual has been inactive for a long period without success (non-success group).

###### S1.3 GTD terrorism attack dataset

Our third dataset contains 170,350 terrorist attacks by 3,178 organizations from 1970 to 2017, collected by the Global Terrorism Database, one of the most systematic databases on domestic and transnational terrorist events32. For each attack we obtain information on its date, type, location, and consequences in terms of the number of people killed and wounded. Some records in this corpus are based on speculation or dubious claims of responsibility, which are discarded in our analysis to ensure the data quality.

There lacks a clear deﬁnition of ‘success’ for terrorist attacks, partly due to their diverse intents and consequences. To be consistent with our empirical steps in D1 and D2, here we treat an attack as successful if it killed at least one victim. One potential concern of this deﬁnition

is that goals of terrorism attacks differ, and not all attacks are aimed at killing victims. This concern is somewhat alleviated, however, as 84.7% the attacks are indeed targeted at human beings (i.e. assassination, bombing/explosion and assault). We further performed robustness checks by focusing on these types of attacks (Fig. S26), ﬁnding our results remain the same. Therefore we collected sequences of attacks of each terrorist organization. We classify the samples if (i) the organization killed at least one people (success group); (ii) the organization has been inactive for a long period without success (non-success group).

###### S1.4 Data limitations

Our data are not without limitations. For example, as agents who failed may change their goals and subsequently transfer to other systems, it is difﬁcult to obtain the full coverage of all attempts. For example, one might apply for grants from other funding agencies, found startup ventures without VC investments, or stop launching terrorist attacks for other activities. While our systematic validation efforts in S1.1-S1.3 have not uncovered any potential biases, readers should keep in mind of the existence of such factors. Nevertheless, despite these potential limitations, it is important to note that the three data sources are among the largest in their respective domains, hence representing the state-of-art empirical corpora to understand failures.

- S2 Related work and models


- S2.1 Learning literature

This paper is closely related to the rich literature on learning and failures. Canonical frameworks in understanding how people react to failures19,38,52–56 have identiﬁed several key factors that could impact learning, including individual characteristics and organizational structures and strategies. These ﬁndings have also prompted quantitative studies using failure records across different industries, ranging from entrepreneurship30,31 to commercial banking57, from healthcare58 to coal mining59 to trains60, and airlines61 to orbital launch vehicles62.

Another relevant line of inquiry is in psychology and organization behavior, which concerns learning curves from both theoretical18–23,33,34,37–39,42,43,63–65 and empirical21,37–40,44,66 perspectives, quantifying how performance and efﬁciency improve with experience. One key result is the famous Wright’s law44, i.e. the power law form of cost reduction.

Next we review a series of major models and compare key predictions with our empirical results. We summarize all these models in Table S1.

- S2.2 Stochastic models with memory


One school of thought can be viewed as modeling the dependence structure among failures. Indeed, the failure of the chance model suggests that non-trivial dependence may be essential for modeling

the fat-tailed length distribution of failure streaks, which raises an important question: Could other stochastic processes (Markov process, random walk, autoregressive model, etc.) account for our observations? Indeed, if we consider a general framework of ﬁxed dependence as follows

Sn = fn(S1,S2,··· ,Sn−1), (S1) where Sn denotes the performance at the n-th attempt and fn can be a deterministic or stochastic non-decreasing mapping. This framework covers a wide range of stochastic processes, e.g. fn(S1,··· ,Sn−1) = fn(Sn−1) for a discrete space of Sn leads to Markov process, fn(S1,··· ,Sn−1) = Sn−1 + ϵn leads to random walk, fn(S1,··· ,Sn−1) =

∑p

i=1 ϕiSn−i + ϵn leads to autoregressive model. We note that if this is true, we can obtain

Sn = fn(S1,f1(S1),··· ,fn−1(S1,f1(S1),···)) ≡ gn(f1,··· ,fn)(S1) (S2) Hence, Sn can be formulated as a non-decreasing function of S1, indicating that there should be detectable ‘ﬁtness’ differences in the ﬁrst attempt. Indeed, these results indicate that if there exists no difference in the dependency structure fn, the differences in outcomes should be at least partly contributed by performance at the ﬁrst attempt, which contradicts with our data. This hypothesis also cannot explain the fat-tail length distribution of failure streaks (S3.8).

###### S2.3 Adaptation models

The evolutionary perspective for individual and organizational learning assumes that the agent improves through updating information and belief on different alternatives. Here we discuss three representative models, each assuming a ﬁnite pool of available options.

###### S2.3.1 Crossman’s model

Crossman’s model, ﬁrst proposed in67, aims to explain the temporal scaling observed in individual

tasks. The model suggests a process from r methods Mi (1 ≤ i ≤ r), each with a time cost ti. The individual improves operation strategy through changing probabilities for using different methods, i.e. pi where

∑r

i=1 pi = 1. At the n-th trial, the expected time cost can be formulated as

∑r

tipi(n) (S3)

T(n) =

i=1

The change of probability for choosing method Mi is proportional to the difference between its time cost and current average time cost, i.e.

pi(n + 1) − pi(n) = −k(ti − T(n)) (S4)

Therefore, the time cost decays as

T(n + 1) = T(n) − k

∑r

pi(ti − T(n))2 (S5)

i=1

###### S2.3.2 NK model

NK model, initially proposed by Kauffman68 is a canonical model in organizational learning69.

Consider a rugged ﬁtness space of N dimensions X = (x1,··· ,xN), where xi ∈ {0,1}. The ﬁtness score of each possibility is the summation of interaction among K adjacent dimensions, that writes

∑N

ϕi(xi,··· ,xi+K) (S6)

ϕ(x) =

i=1

One heuristic searching strategy in this rugged landscape concerns two options:

- (1) Local search, i.e., walk to a neighbor, y, which satisﬁes |y − x| = 1.
- (2) Global search, i.e., jump to a new node randomly.


###### S2.3.3 Denrell and March’s model

Denrell and March proposed a simple adaptation model to understand the interplay between information and adaptation, explaining why people have bias against novel and risky choices70. In this model, Pt, deﬁned as the probability for the ﬁrst option to be chosen at time t, depends on its past probability Pt−1 and current performance. If the option leads to better outcome compared with the other, one updates

otherwise,

###### Pt+1 = Pt + a(1 − Pt) (S7)

###### Pt+1 = (1 − a)Pt (S8)

All three models presented here can mimic speciﬁc performance or efﬁciency trajectory as one tries repeatedly. The main issue with these models is that they all base on a ﬁnite space of possible options, which leads to a limit in performance and efﬁciency improvement that one cannot overcome, which contradicts with our data.

###### S2.4 Search models

Search models assume an iterative process, where one decides whether to use existing components or try new ones based on component quality. Such models are often characterized by an improvement in the objective performance function because of the extreme values theory, i.e. as one always selects the best version from experimentation, she will eventually arrive at the version that is reasonably good.

###### S2.4.1 Roberts’ model

Robert proposed a model based on greedy algorithms64. To understand the universal learning process, the model assumes production efﬁciency p as lognormal, following

x = blnp (S9)

where x follows the standard normal distribution N(0,1). Each time the agent randomly selects a sample x′ and compares it with current efﬁciency x, adopting the new method when x′ < x − a. The model predicts

lnp ∼ lnN/ab (S10)

###### S2.4.2 Muth’s model

Muth’s model42 builds on a simple assumption: the individual tries a new method at each trial and uses the new method if it costs less. The model further assumes appropriate regularity conditions

for the cdf of cost F, e.g.

F(x) (x − x0)k

= c (S11)

lim

x→x0

- where x0 is the limiting cost of production. The model predicts the expected cost E[Xn] of the n-th production as


E[Xn] = x0 + Γ(1 + 1/k)(cn)−1/k (S12) Muth’s model is an elegant model explaining the emergence of power law scaling and can be extended to dependent component cases.

###### S2.4.3 McNerney’s model

McNerney et al further extended Muth’s model by assuming a power law distribution of costs of

each component (f(ci) ∼ xiγ−1) and using design structure matrix to characterize the dependency among different components43. The model predicts the cost y decreases as a function of productions n following

∗

y(n) ∼ n−1/γd

where d∗ is the design complexity and equals to 1 when all components are independent.

(S13)

Search models successfully explain the emergence of power-law scaling in repeated attempts and serve as the basis of our frameworks (e.g. k → ∞ limit). Yet they cannot account for the coexistence of two groups and their diverging patterns.

###### S2.5 Individual learning models

There has also been an active line of inquiry in explaining practice curves in individual tasks40,41,45,71. These models use psychology models as well as cognitive theories to explain ‘practice makes perfect’.

###### S2.5.1 Newell and Rosenbloom’s chunking model

To explain the power-law scaling observed in human task performance, e.g. inverted text reading and ten-ﬁnger game, Newell and Rosenbloom modeled the learning process using chunking theory40. In this model, there is a tree structure for goal hierarchies of height H and the speed-up of task completing is due to the emergence of higher-order chunks. The current highest order of chunk is denoted as η, leading to

dT dN

dT dη

dη dN

(S14) The model further assumes each non-terminal goal has β non-terminal subgoals and ω terminal subgoals. As one constructs chunks of higher levels, the corresponding time to perform a new attempt decreases exponentially following

=

###### dT dη ∼ βH−η (S15)

If we also assume the chunking rate is linear with respect to time and the birth of a single level-h chunk requires time s(h), we have

dη dN ∼

βη−H s(η)

T (S16)

Therefore, if s(η), the number of possible states for goals at level η (complexity at this level), takes an exponential form as s(η) ∼ eαη, which is consistent with the tree structure, we have

(T + E)−x T

dT dN ∼

(S17)

which follows a power law scaling. Hence, by combining two exponential forms in a tree structure, the authors successfully derive the power law scaling.

###### S2.5.2 Anderson’s model

Based on ACT’s strengthening process, Anderson developed a model explaining cost decay41. The model assumes the amount of practice as S and the production execution in ACT takes the form

###### T = c + aS−1 (S18)

The amount of past practice also decays as a power law of practice time:

Therefore, we have

P∑−1

s(i,P) ∼

S =

i=0

∑P

i−d ∼ P1−d (S19)

i=1

T = C′ + A′Pd−1 (S20) The two models are very relevant to our settings and can predict power law temporal scaling in the success group. They represent two fundamental classes of cognitive architectures in related studies: ACT and Soar (and their variants)49, highlighting the role of memory and chunks in learning process. Yet such mechanisms are more appropriate for modeling simple tasks rather than complex innovative ones and cannot account for the co-emergence of success and non-success groups.

###### S2.6 Urn models

Urn model and its variants are among the canonical models in social physics as well as innovation process72. This model family is closely related to the famous Heaps’ law73, originally predicting that the number of distinct words S in a paragraph of length n scales as

###### S(n) ∼ nβ, 0 < β ≤ 1 (S21)

Note that if we assume generating a new word costs unit time, we know the expected time spent on the n-th ‘word’ follows

tn ∼ nβ−1 ≡ n−γ, 0 < γ ≤ 1 (S22) which recovers our empirical ﬁndings. Here we review several generative models explaining this scaling.

###### S2.6.1 Simon’s model

Simon’s model is among the earliest frameworks modeling ‘cumulative advantages’74. It assumes that (1) There is always constant probability p for an agent to take a new word for the next element; (2) Otherwise (with probability 1−p) the agent reuses past words based on frequency, i.e. randomly select a word from the past sequence. This model predicts a linear scaling between S and n i.e. β = 1, which can only explain the emergence of the non-success group.

###### S2.6.2 Tria’s model

By extending studies on urn model, Tria et al75 assume an urn U of ideas and a sequence of S to generate. Every time an element is sampled from U to S, ρ copies are put back to U. Further, if this sampled idea is new in S, it triggers ν adjacent new ideas, hence the number of different ideas in a sequence follows the master equation

dD dt ≈

νD ρt + (ν + 1)D

(S23) The solution reveals that D grows linearly with t for ν > ρ, but follows Heaps’ law D ∼ tν/ρ for ν < ρ. These predictions are similar to the ﬁrst phase transition point k∗ in our model.

###### S2.6.3 Iacopini’s model

To further document the impact of past transition sequence in innovative attempts, a recent paper76 proposed a network-based model, where ideas are represented as nodes, and one can travel from one idea to another when they are linked by a weight. The process is set to be a weighted random walk on networks, following

wijt ∑

Pt(i → j) =

k wikt

When a speciﬁc path i → j is traveled, the weight of this edge is updated

(S24)

###### wijt+1 = wijt + δw (S25)

Depending on different network structures, the model can lead to scaling S ∼ nβ with varying β.

While this class of models does not capture the performance dynamics underlying failures,

they are highly relevant to our study in that their predictions are consistent with the temporal patterns observed in our data.

- S2.7 Other models


- S2.7.1 Levy’s model

Levy modeled the improvement of productivity based on the limited range of output denoted as P39. Given the current rate of production after producing q items, Q(q), the improvement of production rate is proportional to the amount that the process can improve, i.e.

dQ(q) dq

= µ[P − Q(q)] (S26)

leading to

Q(q) = P[1 − ea+µq] (S27) Levy’s model captures a kind of production process where the ﬁnal plateau part is signiﬁcant, but it fails to predict the power-law form of productivity improvement.

- S2.7.2 Shrager’s model


By collecting and analyzing data of path length in the bit game, Shrager et al developed a graphdynamic model for route-ﬁnding in ER networks G(n,p)22. The authors proposed a strategy where the individual randomly selects an edge after deleting the ones moving away from the destination with probability r. The number of trials increases the network density p linearly and the cost is the

path length of the whole process s. For r near 0, the model predicts

s ∼

while for r near 1, the model predicts

2 p

(1 − r)lnn/ln(np) (S28)

s ∼ lnn/ln(np) (S29)

###### S2.7.3 Sahal’s model

Sahal explains the progress function in industry productions through probabilistic and deterministic models63. The model assumes different manpower levels and X(s,t) to be the number of product quantities requiring s amount of manpower at time t. If we assume the improvement across u manpower levels does not depend on the current level and can be formulated as p(u), yielding

X(s,t + 1) =

∑1

X(s − u,t)p(u) (S30)

u=−n

If we deﬁne X(s) = limt→∞ X(s,t), the solution of this equation can be formulated as

###### X(s) = bs, 0 < b < 1 (S31)

The model further assumes levels manpower are distributed on a logarithmic scale with width h, obtaining

###### F(Y ) ∼ Y −logb/h (S32)

where F(Y ) is the number of product quantities requiring manpower greater than Y .

###### S2.7.4 Johnson’s model

Johnson et al reported a similar scaling from the time interval of terrorist attacks and other human confrontations34. An illustrative model for this scenario considers confrontation between ‘Red Queen’ and ‘Blue King’, and the advantage of Red Queen after n events, R(n), can be formulated as

∑n

xi (S33) where xi takes value +d or −d with probability 1/2. Depending on the auto-correlation of xi, one can get

R(n) =

i=1

R(n) ∼ nbd,0 ≤ b ≤ 1 (S34)

Taking the inverse of the advantage, we get the attack rate scales as a negative power law of n, i.e.

τn ∼ n−b,0 ≤ b ≤ 1 (S35)

###### S2.7.5 Clauset’s model

Clauset’s model33 also aims at understanding the temporal pattern of terrorist attacks, but in a very different way from Johnson’s model34. Indeed, it is found that the size of terrorism organizations scales linearly with its past attacks, i.e.

###### s(n + 1) = s(n) + η (S36)

The model further assumes a new takes time as the inverse of organization size, i.e.

###### ∆t ∼ 1/s (S37)

Taken together, we have

∆t ∼ 1/n (S38) Therefore, this model only applied to group dynamics and the exponent of power law is restricted to be -1.

One commonality among these models is that they lack predictions of the interplay between performance and time. By contrast, our data show that the temporal scaling cannot be simply

explained by agents optimizing time cost tn since the performance also improves for the success group. These models also cannot explain the co-existence of success and non-success groups observed in our data.

- S3 Modeling failure dynamics


- S3.1 The k model


In order to formulate a new attempt, the individual needs to go through every component, and decide what to do next. For a past attempt j, each component i is characterized by an evaluation score x(ji), which falls between 0 and 1. The agent can either create a new version (with probability p), or with probability 1 − p reuse an old one by choosing among past versions. The main cost of creating a new version is time. Here we assume each new version takes one unit of time, and upon creation takes up an evaluation score, drawn randomly from a ﬁxed distribution ρ(x). Real systems are likely to differ in their speciﬁc score distributions. Here for simplicity, we assume ρ(x) follows a uniform distribution on [0,1], approximating the percentile of any underlying score

distributions real systems may follow. One difference between our model and canonical learning curve models43 is that one has little information on the new versions until it gets implemented and evaluated, hence new versions are not guaranteed to increase or decrease their score.

Of the many factors that may inﬂuence p, one key factor is the quality of existing versions. Denoting with x∗ the best score among past versions, we expect p to be a function of x∗. Indeed, consider the two extreme cases. If x∗ → 0, existing versions of this component have among the worst scores hence a high potential to be improved upon with a new version. Therefore the likelihood of creating a new version is high, i.e., p → 1. On the other hand, x∗ → 1 indicates an already excellent version, corresponding to a decreased incentive to create a new one (p → 0). Reusing the existing best version allows the particular component to retain its score x∗ and also avoids incurring additional time cost the individual can avoid spending time working on. To this end, considering P(x ≥ x∗) = 1 − x∗ as the potential to improve on existing versions, we assume p = (1 − x∗)α, where α > 0 characterizes an individual’s propensity to create new versions given the quality of existing versions. The higher this potential, the more likely one may create a new version70.

The dynamics of quality score, xn, can be captured by a higher-order Markov process of memory length k, following

x∗n = max{xn−k,··· ,xn−1} (S39)

 

U[0,1], w.p. (1 − x∗n)α

(S40)

xn ∼



δ(x∗n), w.p. 1 − (1 − x∗n)α

where we assume xn = 0 for all n < 0. Directly solving the model is extremely difﬁcult, given the increasing complexity brought by the higher-order dependencies as well as the continuous state space, which eventually lead to the rich mathematical phenomenon documented in Fig. 3. We can, however, ﬁrst look at two extreme cases that are more tractable.

###### S3.2 Independent model (k = 0)

Here we ﬁrst consider a simple case when k = 0, i.e. there lacks any reusable materials in memory as one tries again. In this case, one creates a new version every time, hence for all n we have

and

xn ∼ U[0,1] (S41)

tn ≡ 1 (S42)

###### S3.3 Learning from all failures (k → ∞)

We now turn to another extreme: learn from all past failures. We can rewrite the process as

x∗n = max{x0,··· ,xn−1} (S43)

 

U[0,1], w.p. (1 − x∗n)α

(S44)

xn ∼



δ(x∗n), w.p. 1 − (1 − x∗n)α

Here we focus on the dynamics of x∗, obtaining

 

U[0,x∗n], w.p. (1 − x∗n)α+1

x∗n+1 ∼

(S45)



δ(x∗n), w.p. 1 − (1 − x∗n)α+1

where x∗1 ∼ U[0,1]. To this end, let us denote fn as the probability density function of x∗n, we obtain

fn+1(x) = fn(x)(1 − (1 − x)α+1) + ∫ x

fn(y)(1 − y)αdy (S46)

0

with f1(x) ≡ 1 for x ∈ [0,1]. By induction we obtain

###### fn(x) ∼ [1 − (1 − xα+1)]n−1 (S47)

The normalization constant equals to ∫ 1 0

(1−xα+1)n−1dx = ∫ 1

[1−(1−x)α+1]n−1dx = ∫ 1

x−α(1−xα+1)n−1dxα+1/(α+1) = B(n,1/(α+1))/(α+1)

0

0

Therefore we have

tn = ∫01(1 − x)αfn(x)dx ∫01 fn(x)dx

B(n,1) B(n,1/(α + 1)) ∼

=

Γ(1)n−1 Γ(1/(α + 1))n−1/(α+1) ∼ Γ(

)−1 n−

1 α + 1

α α+1

###### (S48)

and

1 − xn = ∫01{(1 − x)[1 − (1 − x)α)] + (1 − x)α/2}fn(x)dx ∫01 fn(x)dx

B(n,2/(α + 1)) − B(n,1 + 1/(α + 1)) + B(n,1)/2 B(n,1/(α + 1)) ∼

=

(S49)

Γ(2/(α + 1))n−2/(α+1) − Γ(1 + 1/(α + 1))n−1−1/(α+1) + Γ(1)n−1/2 Γ(1/(α + 1))n−1/(α+1) ∼ Γ(

)Γ(

)−1 n−

1 + min{α,1} α + 1

1 α + 1

min{α,1} α+1

Hence, both efﬁciency and quality scales with n, following γ = 1−1/(α+1) and η = min{γ,1− γ}.

###### S3.4 Solving the general model

We note that the previous two cases are tractable because either xn or x∗n can be formulated into a simple Markov process without higher-order dependencies. However, such techniques cannot be directly applied to general cases. As will be shown below, by using renewal process theories36, we can successfully obtain accurate values of scaling exponents (Fig. S7). We ﬁrst note that

|{n1 ≤ n ≤ n2 : xn = x∗m}| ≤ n2 − n1 + 1 (S50)

[(n2−∑n1)/k]−1

∑k−1

|{n1 ≤ n ≤ n2 : xn = x∗m}| ≥

1+ki+j = x∗n

1+ki+i) ≥ [(n2 − n1)/k] (S51)

I(xn

i=0

j=0

Hence to calculate the length of a sequence, we only need to estimate the number of versions that

are once baseline versions (i.e. n such that xn = x∗m for some n + 1 ≤ m ≤ n + k).

Denote zm = 1 − x∗n as all such baseline scores. We now calculate for a speciﬁc zm to be taken by a new one, the number of attempts it takes. Indeed, given a score zm and assuming that it

has been reused as zm = zm−1, we have



kα m (1−zm)k](1−zmα )

zm w.p. [1−z

1−zmα(1−zm) ∼ O(1)



(S52)

kα m (1−zm)k]zmα+1

zm+1 =

U[0,zm] w.p. [1−z

1−zmα(1−zm) ∼ O(zmα+1)



min{U1[0,1],··· ,Uk[0,1]} w.p. zmkα(1 − zm)k ∼ O(zmkα)

Here we use the big-O notation to ﬁnd the asymptotic case for zm → 0, the only limit that could possibly exist divergence leading to emergence of scaling and phase transitions. This equation shows two important insights:

- (1) If we calculate the number of iterations that zm gets reused, it should be in the order of

- O(zm−min{kα,α+1}), leading to two cases that will be discussed in detail.


- (2) There exist two different mechanisms driving the substitution of baseline versions: Qual-


ity (w.p. O(zkα)) and Recency (w.p. O(zα+1)). For kα < α + 1, the recency mechanism takes the majority for small z, i.e. produces a worse succeeding score. Hence, it keeps an equilibrium of score as n increases. However, once kα > α + 1, quality mechanism takes over for small z, characterizing a continuous path of getting better and better.

Here, we ﬁrst derive our results for the regime kα < α + 1, and extend the obtained results to the other regime.

###### S3.4.1 Case 1: kα < α + 1

When zm+1 ̸= zm, our previous results show that with high probability, zm is the extreme value among k i.i.d. random variables on U[0,1], hence the pdf of zm, f(zm) ∼ const as zm → 0. Below we offer a more rigorous proof: Here we take all the different zm as z˜ and consider a limiting distribution of f(˜z), we have

f(˜z) ∼ ∫ 1

f(˜z′)O(1)dz˜′ + ∫ 1

f(˜z′)O(˜z′α+1−kα)/z˜′dz˜′ (S53)

0

z˜

Assuming f(˜z) ∼ z˜β

1 and consider z˜ → 0 one gets

β1 = min{0,1,β1 + α + 1 − kα} = min{0,β1 + α + 1 − kα} (S54) Since kα < α + 1, we get β1 = 0. Hence, as we generate a new baseline score satisfying zm ̸= zm−1, we approximate the number of iterations it will be retained as u ∼ z−kα. Let zm = zm+1 = ··· = zm+u, while for zm+u+1 we take a new random variable from a ﬁxed distribution on [0,1] whose probability density not diverge near 0. If we consider the change of baseline scores as a ‘jump’ and number of iterations of repeated reuse as the length of this jump (u), we eventually arrive at a Levy ﬂight.

Deﬁne ui ≡ zi−kα, following asymptotically power law pdf P(u) ∼ u−1/kα−1 ≡ u−µ−1,

deﬁne m(N) = minm{u1 + ···um ≥ N}. Next we solve ⟨umλ (N)⟩ for some λ. We ﬁrst calculate

- P(um(N)), which equals to


P(um(N) = u) = P(u)∫ N

∑∞

Pk(v)dv

max{N−u,0}

k=0

= P(u)∫ N

G(v)dv

max{N−u,0}

(S55)

###### where Pk(v) ≡ P(v1 + ··· + vk = v) and G(v) ≡ ∑∞

k=0 Pk(v). Pk can be analytically obtained by induction, following

 

Pk−1 ◦ P, k ≤ 1

(S56)

Pk =



δ(0), k = 0

Hence we have

∑∞

Pk = G ◦ P + δ(0) (S57)

G =

k=0

Taking the Laplace transformation we obtain

###### G˜ = G˜P˜ + 1 (S58)

leading to

1 1 − P˜

G˜ =

(S59)

The quantity of interest, M(N) ≡ ⟨uλm(N)⟩, can be formulated as

###### M(N) = ∫ ∞

P(um(N) = u)uλ

0

= ∫ N

P(u)uλ ∫ N

G(v)dvdu + ∫ ∞

P(u)uλ ∫ N

G(v)dvdu

N−u

0

N

0

= ∫ N

Q(u)[H(N) − H(N − u)]du + ∫ ∞

(S60)

Q(u)H(N)du

0

N

Q(u)du − ∫ N

= H(N)∫ ∞

Q(u)H(N − u)du

0

0

= H(N)∫ ∞

Q(u)du − (Q ◦ H)(N)

0

∫0N G(v)dv and Q(u) = uλP(u). Let us again perform the Laplace transforma-

where H(N) =

tion, obtaining

Assuming

we obtain

###### M˜ = H˜(∫ ∞

Q(u)du − Q˜)

0

= G˜(∫ ∞

Q(u)du − Q˜)/s

0

= ∫0∞ Q(u)du − Q˜ s(1 − P˜)

(S61)

###### P(x) = µx−µ−1I(x ≥ 1) (S62)

P˜(s) = µsµΓ(−µ,s) (S63)

Q˜(s) = µsµ−λΓ(λ − µ,s) (S64) ∫ ∞

µ µ − λ

(S65)

Q(u)du =

0

∫s∞ ta−1e−tdt is the upper incomplete Gamma function. Inserting these results into the previous function we arrive at

where Γ(a,s) =

µ/(µ − λ) − µsµ−λΓ(λ − µ,s) s[1 − µsµΓ(−µ,s)]

M˜ =

(S66)

To obtain asymptotic results for M(N) as N → ∞, we approximate M˜ (s) as s → 0+. Here we use the following expansion

sa a

Γ(a,s) = Γ(a) −

+

sa+1 a + 1

+ O(sa+2) (S67)

The previous equation hence writes

µ/(µ − λ) − µsµ−λΓ(µ − λ) + µsµ−λsλ−µ/(λ − µ) − µsµ−λsλ−µ+1/(λ − µ + 1) s[1 − µsµΓ(µ) + µsµs−µ/(−µ) − µsµs−µ+1/(1 − µ)]

M˜ ≈

= −µsµ−λΓ(µ − λ) − µs/(λ − µ + 1) s[−µsµΓ(µ) − µsµs−µ+1/(1 − µ)]

sµ−λΓ(µ − λ) + s/(λ − µ + 1) s[sµΓ(µ) + s/(1 − µ)] ∼ smin{µ−λ,1}−min{µ,1}−1

=

Hence we obtain

(S68)

M = L−1(M˜ ) ∼ n−min{µ−λ,1}+min{µ,1} (S69)

Let us consider the two speciﬁc cases:

- Case 1: λ = −1/k, we have M ∼ nmin{1/(kα),1}−1, hence

⟨(1 − x∗)α⟩ ≈ M =

 



const., kα ≤ 1

n−1+1/(kα), kα > 1

(S70)

- Case 2: λ = −1/(kα), we have M ∼ nmin{1/(kα),1}−min{2/(kα),1}, hence




const., kα ≤ 1



⟨1 − x∗⟩ ≈ M =

n−1+1/(kα), 1 < kα ≤ 2



n−1/(kα), kα > 2

This eventually leads to

(S71)

⟨1−x⟩ = ⟨z⟩ = ⟨z∗+z∗α/2−z∗(α+1)⟩ ≈ ⟨z∗+z∗α/2⟩ ∼ n−min{1,kα−1}/kα ∼ n−min{γ,1−γ} (S72)

###### S3.4.2 Case 2: kα > α + 1

As we solved previously, in this regime the quality dynamics is dominated by the second mechanism, which does not depend on k any more, and should be asymptotically the same as learning

from all failures model (k = ∞). Indeed, if we expand our solution and take k → (1 + 1/α)−, we obtain γ = 1 − 1/(kα) → α/(α + 1) and η = min{γ,1 − γ} → min{1,α}/(α + 1), which are the same as k = ∞. Hence, the regime lying between k = 1 + 1/α and k = ∞ should have the same scaling behaviors.

Taken together, we obtain

γ =

where k∗ = 1/α.



- 0, k < k∗
- 1 − k∗/k, k∗ ≤ k < k∗ + 1




(S73)



1/(k∗ + 1), k ≥ k∗ + 1

η = min{γ,1 − γ} (S74)

###### S3.5 Connections with canonical ensembles

The piecewise function in our solutions raises an interesting question: What characterizes the discontinuous pattern at k = k∗ and k = k∗ + 1? In this section, we establish a mapping between our model and a canonical ensemble system, showing that the observed critical points can be phenomenologically linked to phase transitions (Fig. S8).

For simplicity, we rescale this system through

K = k − k∗

Γ = k∗γ/(1 − γ)

(S75)

K = k − k∗ and Γ = k∗γ/(1 − γ), obtaining



- Γa(K) ≡ 0, K < 0
- Γb(K) ≡ K, 0 ≤ K < 1
- Γc(K) ≡ 1, K ≥ 1




(S76)

Γ =



Note that all smoothness conditions are preserved since the transformations in S75 are inﬁnitely differentiable. Here we consider a system with three different states a,b,c with corresponding energy density Ea(h),Eb(h),Ec(h). Its partition function can be written as

###### Z = e−NE

a(h) + e−NE

b(h) + e−NE

c(h) (S77)

where N is the total number of particles and h is external ﬁeld. We further assume that Ea(h) = (2ϵh − 1)2, Eb(h) = (2h − 1)2, and Ec(h) = [2ϵ(1 − h) − 1]2 where ϵ → 0+. The introduction of ϵ is to distinguish state a from state c, and we approximate this with limiting condition Ea(h) = Ec(h) = 1.

Next, we map f → (2Γ − 1)2, N → lnn, h → K, and Ei(h) = [2Γi(K) − 1]2. Hence, the two transition points k∗ and k∗ + 1 corresponds to h = 0 and 1 in the canonical ensemble systems. To explore the nature of discontinuity at k∗ and k∗+1, we now turn back to the analytical solutions of the mapped system.

Indeed, as N → ∞, the free energy density f = lnZ/N tends to converge to the minimal energy f = min(Ea(h),Eb(h),Ec(h)). Hence, the magnetization density m = dhdf is noncontinuous at the boundary of two Ei(h). In particular, the differences across the boundary is caused

by changes of base states, i.e. the mechanisms that dominate the current system. Therefore, there

exists phase transitions at h∗ if Ei(h∗) = Ej(h∗) for i ̸= j. Hence, we obtain phase transition at

- h∗ = 0 and h∗ = 1 respectively. To sum up, we successfully recover the two transition points at k∗ and k∗ + 1.


To unveil the origin of the transitions, here we inspect u(z), deﬁned as the number of attempts where a version of high score x → 1 (i.e. potential z ≡ 1−x → 0) is retained. We can analytically derive its asymptotic distribution as

Pz(u) ∼ {

}−Au ∼ [1 − zmin{k/k

(1 − z1/k∗)[1 − zk/k∗(1 − z)k] 1 − z1/k∗(1 − z)

∗,1/k∗+1}]−Au (S78) where A is a constant independent of z and u. Eq (5) enables us to calculate the expected life span of a high-quality version ⟨u(z)⟩ ∼ ⟨z−min{k/k∗,1/k∗+1}⟩. The ﬁrst critical point k = k∗ hence corresponds to the ﬁniteness of this ﬁrst moment ⟨u⟩. When k is small (k < k∗), ⟨u⟩ is ﬁnite. In this region, although new versions build on past k attempts, good versions will only be reused for a limited number of attempts. This is similar to an asymmetric (super-)diffusive random walk where the step size has ﬁnite expectation (renewal process), predicting a linear relationship between number of attempts and time cost. Once k passes the critical threshold k∗, we ﬁnd ⟨u⟩ = ∞, hence a good version may be retained for an unlimited long period. This is similar to a ballistic random walk where the step size has inﬁnite expectation, where the scaling behavior between steps (time cost) and distance (number of attempts) begins to emerge. The second phase transition originates from the competition between two dynamical forces: (a) the k/k∗ term represents the chance that the current best version gets forgotten due to k consecutive attempts in creating new versions; (b) the 1/k∗ + 1 term captures the chance that the current best version is substituted by a

better one. Comparing the dominance of the two mechanisms points to the second transition point k∗ + 1, beyond which k plays no major role.

###### S3.6 Functional forms of ρ(x) and p(x)

Two important quantities in our model are ρ(x), the score distribution for a new version, and p(x), the probability to create a new version given reference score x. For simplicity we assume ρ(x) ≡ 1 and p(x) = (1−x)α in main text. Here we show that similar results can be obtained as we consider a general class of functional forms of ρ(x) and p(x).

Indeed, since both quantities depend on the scoring system, we may ﬁx one to a speciﬁc form. Consider two score systems x and y that can be derived through y = c(x). We can derive the transformations as

ρX(x) = ρY (c(x))c′(x) (S79)

pX(x) = pY (c(x)) (S80)

Combining the two equations we ﬁnd the quantities can be connected through

###### ρX/(p−Y1 ◦ pX)′ = ρY ◦ p−Y1 ◦ pX (S81)

Indeed, selecting appropriate transformations one can apply the derived protocols for other existing models in learning curve studies. To demonstrate this, let us consider a selection model

documented in42. Here we deﬁne ρX = xβ−1,ρY = 1,pX = 1, we obtain c(x) = xβ/β and pY = 1

(i.e. α = 0), assuming k = ∞ we have

###### ⟨xn⟩ ∼ ⟨yn∗(1/β)|k = ∞,α = 0⟩ ∼ n−1/β (S82)

In this way we arrive at a system y that is mathematically equivalent to existing model systems42, where one has power law cost distribution, try new versions at every attempt and learns from all past experiences. Hence our approach is also able to recover this n−1/β scalings (n−1/k using notations in original paper42) documented in learning curve models through mathematical transformations. For following discussions we always assume ρ ≡ 1 and consider different forms of p(x).

Our previous results have shown solutions for p(x) = (1 − x)α, prompting us to consider a more general form using expansion

ln(p(x∗) − p(1)) = α ln(1 − x∗) + o(ln(1 − x∗)), x → 1 (S83)

ln p(x∗)

where α ≡ limx∗→1

ln(1−x∗) ≥ 0 captures the asymptomatic behavior of p near x∗ → 1. If p(1) > 0, there is certain positive probability that one will create a new one, no matter how good

she did, which will cause both tn and xn converging to positive limit. On the other hand, when p(1) = 0, we can approximate p(x∗) ∼ (1 − x∗)α, hence we should observe the same scaling as p(x∗) ∼ (1 − x∗)α. Indeed, all our previous derivations only rely on the power law tail of x−kα rather than a precise power law form.

Despite its simplicity, the assumption enables us to work with a broad range of functions, including all functions that are analytic at x∗ = 1 (e.g. p = ec(1−x∗) − 1 ∼ c(1 − x∗)) as well

- as many that are not (e.g. p = (1 − x∗)c with non-integer c) through a single parameter α. Note that this relaxation in the functional form of p(x) is again closely related to the relaxation in ρ(x) documented in42 due to the relationship between the two quantities we discussed before.


###### S3.7 Null models

Our model demonstrates that both experience and evaluations play an important role in dynamics of failure. To verify that both ingredients are necessary, we investigate two variants of the model.

To understand the role of experience, we explore a model (a) assuming that an individual

does not reuse past versions. We ﬁnd model (a) reduces to the case of k = 0, where each attempt is made independently. Again, we recover results from S3.2, predicting constant efﬁciency tn = 1 and quality xn = 0.5.

We then keep the experience mechanism, but eliminate the role of evaluations by assuming that one chooses to reuse past version regardless of its score. In other words, model (b) assumes that the probability to create a new version, p, is constant, independent of past scores. This allows us to write the master equation as

 

U[0,1], w.p. p

x∗n+1 ∼

(S84)



δ(x∗n), w.p. 1 − p

By induction one has xn ∼ U[0,1] for any n, again predicting constant efﬁciency tn = p and quality xn = 0.5. This indicates that in the absence of evaluations the model fails to reproduce the observed scaling behavior. Indeed, the improvement in the original model is mainly driven by

reuse preference towards version with higher-scores, explaining why it does not exist in this null model.

Together, the predictions of these two alternative models indicate that a combination of the two ingredients is essential for the emergence of scaling observed in Fig. 4. One may also hypothesize that the uncovered patterns are affected if we deﬁne the ﬁnite capacity using the unit of time (t) rather than trials (n), prompting us to consider a model (c): Here we assume that individuals

- at time t consider all past failures that occurred during a time window τ, i.e. individuals at time t consider all past failures that occurred during a time interval (t − τ,t], where the window size τ, instead of our previous parameter k, measures how long one looks back upon past failures. We further assume that the number of components equals to one for simplicity. The previous master equation can be written as


x∗n = max

{xm} (S85)

tm+···+tn≤τ

 

U[0,1], w.p. (1 − x∗n)α

(S86)

xn ∼



δ(x∗n), w.p. 1 − (1 − x∗n)α

To solve this model, we note that the following equations hold.

|{n1 ≤ n ≤ n2 : xn = x∗m}| ≤ n2 − n1 + 1 (S87)

[(n2−n1∑)/(τ+1)]−1

∑τ

|{n1 ≤ n ≤ n2 : xn = x∗m}| ≥

1+(τ+1)i+j = x∗n

1+(τ+1)i+i) ≥ [(n2−n1)/(τ+1)]

I(xn

i=0

j=0

(S88) This is because, if we consider τ +1 versions (xi,··· ,xi+τ), we should ﬁnd (1) at least two of the versions are the same or (2) these are τ + 1 different versions. If (1) is true, i.e. xj = xk for some

- i ≤ j < k ≤ i + τ, we have xj = x∗k, i.e. the duplicated version is a baseline version. Otherwise,


(2) means that there are at least τ new versions, covering all versions over the last τ time units.

###### Hence we have x∗i+τ+1 ∈ {xi,··· ,xi+τ}.

Using the notations in previous derivations, we can also recover the master equation as



τα m (1−zm)τ](1−zmα )

zm w.p. [1−z

1−zmα(1−zm) ∼ O(1)



(S89)

τα m (1−zm)τ]zmα+1

zm+1 =

U[0,zm] w.p. [1−z

1−zmα(1−zm) ∼ O(zmα+1)



min{U1[0,1],··· ,Uτ[0,1]} w.p. zmτα(1 − zm)τ ∼ O(zmτα)

To this end, we ﬁnd that this variant is asymptotically similar to our original model, with τ∗ = k∗ = 1/α. Indeed, when a baseline version is out of date and gets replaced, the recency mechanism happens after k∗ (τ∗) new versions have been created without reuse, explaining why τ∗, the critical number of different versions to look back, equals to k∗, the critical number of versions to look back.

###### S3.8 Failure streak length

To explain the fat-tailed distribution documented in Fig. 1, let us consider a single-component case of our model for simplicity. We assume that q, the probability for a new version to success, is independent of its score. We denote N as the number of failures before success.

Assume N ≥ n, i.e. one has not achieved success in the ﬁrst n attempts. For one to succeed in the (n + 1)-th attempt, she needs to (1) create a new version at this time, corresponding to

probability tn ∼ n−γ and (2) succeed for this new version, which has probability q. Together we obtain

P(N = n|N ≥ n) ∼ qn−γ (S90) Note that this form is closely related with Lindy’s law77,78. Here the right hand side of the equation is decreasing, since a long failure streak indicates the existence of an (unsuccessful) version that has been used for a long period. Therefore, the same version is more likely reused again in the future, reducing the chance to create a new, successful version at the next step.

If we deﬁne the survival function S(n) = P(N ≥ n), this equation is equivalent to

###### 1 − S(n + 1)/S(n) ∼ qn−γ (S91)

Using a continuous approximation we obtain

dS S ∼ qn−γdn (S92)

−

leading to the solution

1−γ

P(N ≥ n) = S(n) ∼ e−cn

(S93)

Hence, it predicts that the length distribution follows the well-known Weibull distribution.

To further understand the Weibull form, here we point out that it is closely related to Heaps’ law73 caused by the reuse mechanism. Indeed, given that one needs to create M different versions before success, the distribution can be formulated as an exponential model

###### P(M ≥ m) = (1 − q)m (S94)

However, repeated reuse leads to a sub-linear scaling between N and M, following the Heaps’ law with exponent 1 − γ:

∑N

∑N

n−γ ∼ N1−γ (S95)

tn ∼

M(N) =

n=1

n=1

Combining the two equations one can obtain the same Weibull model

1−γ

P(N ≥ n) = S(n) ∼ e−cn

(S96)

The completely random assumption is not necessary. Indeed, we can relax it by considering success probability q as a function of evaluation score x. As long as (1) q(x) is non-decreasing with x, hence a better score corresponds to a higher probability of success. (2) q(x) < 1 all x, characterizing an uncertain world where there is no guaranteed success. Now we have

q(x)dx)m (S97)

P(M ≥ m) = (1 − ∫ 1

0

Using the sub-linear scaling between M and N, the failure streak length is still captured by the Weibull distribution. An interesting insight from these results is that all quantities of interest exhibit scale-free properties. This means if we consider different criteria of success that are organized into hierarchal structures, our results are robust against the selection of criterion.

Another possibility that can lead to fat-tailed distributions is ﬁtness heterogeneity16. Indeed, since different individuals may have different ﬁtness, it might be possible that the fat tail of failure streaks can emerge without the reuse mechanism. To test if this is sufﬁcient for modeling dynamics of failure, here we compare it with other observations, ﬁnding the ﬁtness hypothesis cannot account for the observed patterns for a series of reasons:

- 1. Initial performance fails to predict eventual outcome. One direct prediction of the ﬁtness hypothesis is the predictive power of initial performance for the eventual outcome. However, as shown in Figs. 4g-i, we ﬁnd that for large n, the success and non-success group show no statistical differences at the ﬁrst attempt, which is in strong contrast with our prediction.
- 2. Weak correlation between initial performance and failure streak. Assuming performance dynamics is mostly driven by ﬁtness heterogeneity, those who succeeded with fewer failures should show better performance at the very beginning. Hence, one would expect a strong correlation between initial performance and failure streak. However, we ﬁnd that across the three datasets, the correlation between the two is weak (Fig. S13a-c).
- 3. Fat tail remains as we control ﬁtness. If the fat-tail is caused by a broad distribution of ﬁtness, we should observe a narrower tail as we control the ﬁtness through conditioning on initial performance. Our results show that, as we conditional on samples with top/bottom performance at the beginning, P(N) still distinguishes from the exponential model (Fig. S13d-f).
- 4. Failure dynamics. Most importantly, the ﬁtness hypothesis states that success and nonsuccess groups lie on a continuous spectrum, hence we should not expect fundamental differences in their temporal patterns. To this end, it fails to account for the observed patterns documented in Figs. 4d-f.


- S4 Empirical measurements


- S4.1 Quantifying performance dynamics


Here we leverage our three datasets and compile three different measurements for performance.

For the NIH grant application dataset, we make use of the percentile scores assigned by NIH review panels. NIH uses a two-step peer review mechanism: Roughly half of the proposals are selected for the second round discussion, where each proposal is given a percentile score based on their percentile ranking among its peers. Percentile score has been widely used to measure the quality of R01 grant applications27,79, reﬂecting judgment of expert reviewers. Although reviewers score are necessarily imperfect, there is growing evidence for strong correlations between percentile score and subsequent successes of the project50,80. One disadvantage of using the percentile score is that undiscussed proposals (those get rejected in the ﬁrst round) do not have such scores. Moreover, since there exist differences concerning the discussion rate, applications lying on the boundary of discussion can have either marginal scores or no scores. Indeed, here we calculate the proportion of having a percentile score around 57% and plot the score distribution. We ﬁnd as score exceeds 50, there are much fewer samples, since many proposals at this rank did not even get discussed and assigned a score (Fig. S4). To avoid discrimination across study sections, here we take score below 50 and regard the remaining proposals as undiscussed. We also vary the threshold to 55, ﬁnding results remain the same. Lower percentile scores indicate better performance. To be consistent with other measures (higher the better) we rescale the percentile scores using 1-0.01×original score, so the values reported in main text are bigger the better.

To measure the performance in startup ventures, we leverage the investment amount in the ﬁrst funding round as a proxy. Although there are a series of ﬁrm-level statistics that could potentially measure the quality of a venture, investment amount stands out as a preferred choice of representing investor evaluations. This deﬁnition does not account for geographical and industrial factors, as such information is not available to us, but it serves as a reasonable index of startup companies potentials in achieving their eventual goals (IPO or high-value M&As).

Similar to other frequently used measures in economics, investment amount follows a fattailed distribution and exhibits time-dependent properties. To address the two challenges, we take logarithmic of the investment amount and calculate z-score within each year. Denoting the amount of all investments made in year t as {st1,··· ,stn}, here we rescale the values into the performance score z through

log(sti) − E[log(st)]

zit =

√

Var[log(st)]

Once rescaled, we ﬁnd zit approximately follow the standard normal distribution N(0,1) independent from t, allowing us to directly compare attempts made in different years (Fig. S5a). We then compare ﬁrst-round investment amounts for successful and failed attempts, ﬁnding the two samples are clearly separated (Fig. S5b).

Similarly, for terrorist attacks, one measure for performance is the number of individuals wounded. To this end, we collect wound statistics as our performance measure. As shown in Fig. S6b, fatal (successful) attacks also lead to a higher number of wounded individuals than others, validating the effectiveness of using wounded statistics as performance measurements. Re-

lated studies of terrorist attacks suggest the outcome of attacks follow a power law distribution (Fig. S6a), which is also conﬁrmed in our dataset. To this end, we rescale the original values by log(wounded + 1) in our analysis.

###### S4.2 Length distribution of failure streaks

The length distribution of the failure streak, deﬁned as the number of failures before success, is measured directly from data and ﬁtted using maximum likelihood estimation techniques 46. We ﬁt empirical data with discrete versions of exponential and Weibull (stretched exponential) forms using maximum likelihood estimation with parameters xmin = 2. We compare the ﬁtting results from alternative results, i.e. lognormal, power law, and truncated power law using likelihood ratio test46, ﬁnding that Weibull distribution is consistently among the best functional forms (Table S2). To quantify the uncertainty of parameter estimations, we performed bootstrapping technique (100 times) to calculate optimal estimation for each round, and obtained standard error of parameter estimators. We also repeated the results for xmin = 3, obtaining β1 = 0.596 ± 0.032, β2 = 0.540 ± 0.175, and β3 = 0.178 ± 0.057, which again statistically supports β + γ = 1.

###### S4.3 Measuring failure dynamics

Given the highly skewed distributions of N and tn, to measure Tn = tn/t1 we ﬁrst performed log transformation to calculate the mean and variance of log(Tn) from

###### E[log(Tn)] = ⟨log(tn/t1)⟩ (S98)

Var[log(Tn)] = ⟨[log(tn/t1)]2⟩ − ⟨log(tn/t1)⟩2 (S99) As the number of samples decreases dramatically with n, here we focus on n ≤ 10 for D1, n ≤ 7 for D2, and n ≤ 4 for D3.

The two equations immediately give us mean E[log(Tn)] and standard error of the mean √

Var[log(Tn)]/sample size, as plotted in Fig. 4. The divergence between the two groups can be detected as early as the second attempt. Although T1 ≡ 1 by construction, Student’s t-test rejects the hypothesis that T2 between success and non-success groups are the same (P = 0.000457, 0.00773, and 0.0499, respectively).

To calculate the temporal scaling exponent γ, here we run linear regressions between log(n)

and log(Tn) and take the negative slope as γ, i.e.

###### log(tn/t1) = −γ log(n) + c, (S100)

yielding γ1 = 0.361 ± 0.010, γ2 = 0.509 ± 0.036 and γ3 = 0.668 ± 0.143 for success group, with P < 0.001 for all three datasets. We also performed individual ﬁxed effect linear models using the same data, i.e.

log(tn,j) = −γ log(n) + cj + ϵn,j, (S101) where j is the index for different samples and cj is the ﬁxed effect term for each agent j. We obtain similar results γ1 = 0.369 ± 0.015, γ2 = 0.408 ± 0.054 and γ3 = 0.414 ± 0.171. For non-success group there exists no signiﬁcant relationships between log(n) and log(Tn) since the second failure (i.e. excluding T1), with P = 0.450, P = 0.884 and P = 0.823 respectively. Together, these results offer strong empirical support for the diverging temporal patterns predicted by our model.

- S5 Prediction task


- S5.1 Predicting ultimate success


Our model uncovers time as an early signal for predicting eventual success and failure. This prediction is unexpected, since individuals through failures are aimed at improving their performance, rather than saving the time, hence we should expect the two groups have identical temporal patterns. To test this, we use D1 to set up a simple prediction task (Fig. S10a). The goal of this task is not to design state-of-art classiﬁers for predicting success. Rather, to test the predictive power of temporal regularity. As such, our results offer a lower bound for the predictability of failure dynamics.

To this end, here we ﬁrst assume a logistic classiﬁcation model (Model 1) to predict the eventual success following N consecutive failed attempts. For each N, we collect positive samples

- as individuals succeeded after N failures versus negative samples as individuals dropped out after


the same number of consecutive failures. Each sample has a N − 1-dimensional predictor tn (1 ≤ n ≤ N − 1). The classiﬁer writes as

N∑−1

log(success) 1 − log(success)

βn log(tn) (S102) To evaluate the performance of our predictions, we calculate the AUC curve (average area under the receiver operating characteristic) over 10-fold cross validation for different N.

= β0 +

n=1

Our model further predicts that the inter-event time sequence follows a power law decay. If this is true, we should be able to further simplify the prediction model without losing a large frac-

tion of accuracy. Indeed, the power-law form means that we can rescale the N − 1-dimensional feature (log(t1),··· ,log(tn−1)) into two simple parameters by calculating the slope −γ and intercept θ in the log-log plot, i.e.

log(tn) = −γ log(n) + θ (S103) Our prediction model 2 is based on the two variables γ and θ to train a simpler classiﬁer for eventual success, following

log(success) 1 − log(success)

= β0 + β1γ + β2θ (S104) This simpliﬁcation is expected to be inaccurate since it reduces a feature with high dimensions to data points into a 2-dimension feature. However, we surprisingly ﬁnd that a similar prediction accuracy can be achieved as the previous model 1 across different N (Fig. S10), accounting for more than 95% of accuracy in terms of additional predictive power (AUC-0.5).

Deeper studies in Model 2 offer additional evidence that is consistent with model predictions (Fig. S11). First, the coefﬁcient for γ, β1 remains positive (Fig. S11a), demonstrating that escalations in failures are related to eventual success. Our previous results also suggest that the membership of two groups are mainly determined by the learning process (different k) rather than the initial advantage (score/time at the ﬁrst attempt). If so, we would expect the increasing majority of predictive power coming from information encoded in the parameter γ, especially for individuals with large N. To test this hypothesis, we apply an ad-hoc approach for variable importance in logistic regressions. We calculate the ratio coefﬁcient for normalized input, i.e.

R = |β1|[var(γ)]1/2 |β2|[var(θ)]1/2

(S105)

- R measures the ratio of coefﬁcients once the two variables are normalized to have identical variance. We ﬁnd that R increases systematically with n (Fig. S11b), concluding that the variable γ contributes an increasing part of predictive powers as one fails more, supporting the hypothesis that the dynamic process itself, rather than the starting point, has larger impact on the eventual outcome following failures.


###### S5.2 Testing power law model

Despite long history in using power law forms to model learning curves, the literature has also suggested other functional forms49. One of the frequently used alternatives is exponential function, predicting

tn ∼ ab−n (S106) Indeed, recent studies have also suggested that the observed power law could be an artifact by average different samples and individuals should be characterized by an exponential decay81.

The difﬁculty of testing different hypotheses in our datasets comes from small sample sizes: in contrast to industrial production or simple individual tasks, it is almost impossible to observe large number of failures from a single individual. Hence directly comparing the ﬁtting of different models would suffer from overﬁtting issues. To this end, here for each individual sample, we take all but last one inter-event time for model ﬁtting, comparing model predictions for the last interevent time. This out-of-sample testing technique helps to rule out the possibility of overﬁtting.

Using this method we compare the performance of power law, exponential and linear models

in characterizing tn for each individual, measuring their prediction error (Fig. S9). We ﬁnd that across the three datasets, the power law model yields minimum error in more cases.

- S6 Robustness checks


- S6.1 Deﬁnition of successes and failures


We vary our deﬁnition of successes and failures across different datasets. For D1 we remove all renewal/resubmission successes and only focus on new applications, ﬁnding our results are not dominated by resubmissions(Fig. S21). For D2 we vary the deﬁnition of success for a startup. Previously we have considered IPO and high-value M&A as success. Similar with hit papers deﬁned in science of science, we deﬁne high-value M&As as those with transaction value ranking top 1% among all transactions in the same year. We vary this deﬁnition to top 5% transactions (Fig. S24) or exclude all M&As (Fig. S25), ﬁnding our conclusions still hold. For D3 we also tried restricting attack types to be aimed at human beings (Fig. S26), including assassinations, bombing/explosions and assaults, which also yield similar results.

###### S6.2 Threshold for being inactive in the system

The deﬁnition of non-success group depends on the threshold for inactive in the system. In main text we set up the threshold as 5 years, i.e. if one does not appear in the system for the last 5 years, we consider she as drop-out samples. To test the effect of this threshold, here we repeat our main results for 2 years (Figs. S14,S16,S18) and 8 years (Figs. S15,S17,S19), respectively. We ﬁnd all

our results are robust as we tune this criterion.

###### S6.3 Comparing ﬁrst failures versus halfway/penultimate failures

Figure 4 showed the performance divergence patterns in two groups using ﬁrst and second failures. Here we also compares the ﬁrst failures versus halfway failures or penultimate failures, ﬁnding the same patterns exist (Fig. S28).

###### S6.4 Other checks

For D1 we further conﬁrmed that only focusing on failures before the ﬁrst success yield similar results. Indeed, as we further plot Tn for samples with and without prior success, we ﬁnd the dynamical patterns remain the same (Fig. S20). Lastly, we check the threshold of discussion score, considering original percentile score higher 55, rather than 50, as undiscussed. All these variants show results consistent with Fig. 1 and Fig. 4 (Fig. S23).

For D3 we also check our deﬁnition of terrorist organizations. To this end, we downloaded additional information from GTD website, obtaining a ﬁltered list of perpetrator groups. We ﬁnd our results remain similar as we limit our analysis within groups on the list (Fig. S27).

- 1. Fortunato, S. et al. Science of science. Science 359, eaao0185 (2018).
- 2. Azoulay, P. et al. Toward a more scientiﬁc science. Science 361, 1194–1197 (2018).
- 3. Harford, T. Adapt: Why success always starts with failure (Farrar, Straus and Giroux, 2011).


- 4. Fleming, L. Recombinant uncertainty in technological search. Management science 47, 117– 132 (2001).
- 5. Wuchty, S., Jones, B. F. & Uzzi, B. The increasing dominance of teams in production of knowledge. Science 316, 1036–1039 (2007).
- 6. Jones, B. F. The burden of knowledge and the death of the renaissance man: Is innovation getting harder? The Review of Economic Studies 76, 283–317 (2009).
- 7. Petersen, A. M., Riccaboni, M., Stanley, H. E. & Pammolli, F. Persistence and uncertainty in the academic career. Proceedings of the National Academy of Sciences 109, 5213–5218

(2012).

- 8. Clauset, A., Arbesman, S. & Larremore, D. B. Systematic inequality and hierarchy in faculty hiring networks. Science advances 1, e1400005 (2015).
- 9. Sinatra, R., Wang, D., Deville, P., Song, C. & Barab´asi, A.-L. Quantifying the evolution of individual scientiﬁc impact. Science 354, aaf5239 (2016).
- 10. Liu, L. et al. Hot streaks in artistic, cultural, and scientiﬁc careers. Nature 559, 396 (2018).
- 11. Jara-Figueroa, C., Jun, B., Glaeser, E. L. & Hidalgo, C. A. The role of industry-speciﬁc, occupation-speciﬁc, and location-speciﬁc knowledge in the growth and survival of new ﬁrms. Proceedings of the National Academy of Sciences 115, 12646–12653 (2018).
- 12. Hidalgo, C. Why information grows: The evolution of order, from atoms to economies (Basic Books, 2015).


- 13. Barabasi, A.-L. The origin of bursts and heavy tails in human dynamics. Nature 435, 207–211

(2005).

- 14. Gonzalez, M. C., Hidalgo, C. A. & Barabasi, A.-L. Understanding individual human mobility patterns. Nature 453, 779–782 (2008).
- 15. Brockmann, D., Hufnagel, L. & Geisel, T. The scaling laws of human travel. Nature 439, 462–465 (2006).
- 16. Castellano, C., Fortunato, S. & Loreto, V. Statistical physics of social dynamics. Reviews of modern physics 81, 591 (2009).
- 17. Malmgren, R. D., Stouffer, D. B., Campanharo, A. S. & Amaral, L. A. N. On universality in human correspondence activity. Science 325, 1696–1700 (2009).
- 18. Argote, L. & Epple, D. Learning curves in manufacturing. Science 247, 920 (1990).
- 19. Sitkin, S. B. Learning through failure: the strategy of small losses. Research in organizational behavior 14, 231–266 (1992).
- 20. Yelle, L. E. The learning curve: Historical review and comprehensive survey. Decision sciences 10, 302–328 (1979).
- 21. Dutton, J. M. & Thomas, A. Treating progress functions as a managerial opportunity. Academy of management review 9, 235–247 (1984).
- 22. Shrager, J., Hogg, T. & Huberman, B. A. A graph-dynamic model of the power law of practice and the problem-solving fan-effect. Science 242, 414–416 (1988).


- 23. Levitt, B. & March, J. G. Organizational learning. Annual review of sociology 14, 319–338

(1988).

- 24. Huber, G. P. Organizational learning: The contributing processes and the literatures. Organization science 2, 88–115 (1991).
- 25. Edmondson, A. Psychological safety and learning behavior in work teams. Administrative science quarterly 44, 350–383 (1999).
- 26. Gross, C. P., Anderson, G. F. & Powe, N. R. The relation between funding by the national institutes of health and the burden of disease. New England Journal of Medicine 340, 1881– 1887 (1999).
- 27. Ginther, D. K. et al. Race, ethnicity, and nih research awards. Science 333, 1015–1019 (2011).
- 28. Li, D. & Agha, L. Big names or big ideas: Do peer-review panels select the best science proposals? Science 348, 434–438 (2015).
- 29. Kaplan, S. N. & Lerner, J. Venture capital data: Opportunities and challenges. In Measuring Entrepreneurial Businesses: Current Knowledge and Challenges (University of Chicago Press, 2016).
- 30. Eggers, J. & Song, L. Dealing with failure: Serial entrepreneurs and the costs of changing industries between ventures. Academy of Management Journal 58, 1785–1803 (2015).
- 31. Gompers, P., Kovner, A., Lerner, J. & Scharfstein, D. Performance persistence in entrepreneurship. Journal of Financial Economics 96, 18–32 (2010).


- 32. National Consortium for the Study of Terrorism and Responses to Terrorism (START). Global Terrorism Database [Data ﬁle] (2018).
- 33. Clauset, A. & Gleditsch, K. S. The developmental dynamics of terrorist organizations. PloS one 7, e48633 (2012).
- 34. Johnson, N. et al. Pattern in escalations in insurgent and terrorist activity. Science 333, 81–84

(2011).

- 35. Durrett, R. Probability: theory and examples (Cambridge university press, 2010).
- 36. Bass, R. F. Stochastic processes, vol. 33 (Cambridge University Press, 2011).
- 37. Argote, L. Organizational learning: Creating, retaining and transferring knowledge (Springer Science & Business Media, 2012).
- 38. Dahlin, K. B., Chuang, Y.-T. & Roulet, T. J. Opportunity, motivation, and ability to learn from failures and errors: Review, synthesis, and ways to move forward. Academy of Management Annals 12, 252–277 (2018).
- 39. Levy, F. K. Adaptation in the production process. Management Science 11, B–136 (1965).
- 40. Newell, A. & Rosenbloom, P. S. Mechanisms of skill acquisition and the law of practice. Cognitive skills and their acquisition 1, 1–55 (1981).
- 41. Anderson, J. R. Acquisition of cognitive skill. Psychological review 89, 369 (1982).
- 42. Muth, J. F. Search theory and the manufacturing progress function. Management Science 32, 948–962 (1986).


- 43. McNerney, J., Farmer, J. D., Redner, S. & Trancik, J. E. Role of design complexity in technology improvement. Proceedings of the National Academy of Sciences 108, 9008–9013 (2011).
- 44. Wright, T. P. Factors affecting the cost of airplanes. Journal of the aeronautical sciences 3, 122–128 (1936).
- 45. Snoddy, G. S. Learning and stability: a psychophysiological analysis of a case of motor learning with clinical applications. Journal of Applied Psychology 10, 1 (1926).
- 46. Clauset, A., Shalizi, C. R. & Newman, M. E. Power-law distributions in empirical data. SIAM review 51, 661–703 (2009).
- 47. Barab´asi, A.-L. & Albert, R. Emergence of scaling in random networks. Science 286, 509–512

(1999).

- 48. Bettencourt, L. M., Lobo, J., Helbing, D., K¨uhnert, C. & West, G. B. Growth, innovation, scaling, and the pace of life in cities. Proceedings of the national academy of sciences 104, 7301–7306 (2007).
- 49. Ritter, F. E. & Schooler, L. J. The learning curve. International encyclopedia of the social and behavioral sciences 13, 8602–8605 (2001).
- 50. Stephan, P. E. How economics shapes science, vol. 1 (Harvard University Press Cambridge, MA, 2012).
- 51. Paik, Y. Serial entrepreneurs and venture survival: Evidence from us venture-capital-ﬁnanced semiconductor ﬁrms. Strategic Entrepreneurship Journal 8, 254–268 (2014).


- 52. Walsh, G. S., Cunningham, J. A. et al. Business failure and entrepreneurship: emergence, evolution and future research. Foundations and Trends⃝R in Entrepreneurship 12, 163–285

(2016).

- 53. McGrath, R. G. Falling forward: Real options reasoning and entrepreneurial failure. Academy of Management review 24, 13–30 (1999).
- 54. Edmondson, A. C. Strategies for learning from failure. Harvard business review 89, 48–55

(2011).

- 55. Shepherd, D. A. Learning from business failure: Propositions of grief recovery for the selfemployed. Academy of management Review 28, 318–328 (2003).
- 56. Denrell, J. Vicarious learning, undersampling of failure, and the myths of management. Organization Science 14, 227–243 (2003).
- 57. Kim, J.-Y. & Miner, A. S. Vicarious learning from the failures and near-failures of others: Evidence from the us commercial banking industry. Academy of Management Journal 50, 687–714 (2007).
- 58. Edmondson, A. C. Learning from mistakes is easier said than done: Group and organizational inﬂuences on the detection and correction of human error. The Journal of Applied Behavioral Science 40, 66–90 (2004).
- 59. Madsen, P. M. These lives will not be lost in vain: Organizational learning from disaster in us coal mining. Organization Science 20, 861–875 (2009).


- 60. Baum, J. A. & Dahlin, K. B. Aspiration performance and railroads patterns of learning from train wrecks and crashes. Organization Science 18, 368–385 (2007).
- 61. Haunschild, P. R. & Sullivan, B. N. Learning from complexity: Effects of prior accidents and incidents on airlines’ learning. Administrative science quarterly 47, 609–643 (2002).
- 62. Madsen, P. M. & Desai, V. Failing to learn? The effects of failure and success on organizational learning in the global orbital launch vehicle industry. Academy of Management Journal 53, 451–476 (2010).
- 63. Sahal, D. A theory of progress functions. AIIE Transactions 11, 23–29 (1979).
- 64. Roberts, P. A theory of the learning process. Journal of the Operational Research Society 34, 71–79 (1983).
- 65. Kluger, A. N. & DeNisi, A. The effects of feedback interventions on performance: A historical review, a meta-analysis, and a preliminary feedback intervention theory. Psychological bulletin 119, 254 (1996).
- 66. Asher, H. Cost-quantity relationships in the airframe industry. Ph.D. thesis, The Ohio State University (1956).
- 67. Crossman, E. A theory of the acqusition of speed-skill. Ergonomics 2, 153–166 (1959).
- 68. Kauffman, S. & Levin, S. Towards a general theory of adaptive walks on rugged landscapes. Journal of theoretical Biology 128, 11–45 (1987).
- 69. Levinthal, D. A. Adaptation on rugged landscapes. Management science 43, 934–950 (1997).


- 70. Denrell, J. & March, J. G. Adaptation as information restriction: The hot stove effect. Organization Science 12, 523–538 (2001).
- 71. Laird, J., Rosenbloom, P. & Newell, A. Universal subgoaling and chunking: The automatic generation and learning of goal hierarchies, vol. 11 (Springer Science & Business Media, 2012).
- 72. Loreto, V., Servedio, V. D., Strogatz, S. H. & Tria, F. Dynamics on expanding spaces: modeling the emergence of novelties. In Creativity and universality in language, 59–83 (Springer, 2016).
- 73. Heaps, H. S. Information retrieval, computational and theoretical aspects (Academic Press, 1978).
- 74. Simon, H. A. On a class of skew distribution functions. Biometrika 42, 425–440 (1955).
- 75. Tria, F., Loreto, V., Servedio, V. D. P. & Strogatz, S. H. The dynamics of correlated novelties. Scientiﬁc reports 4, 5890 (2014).
- 76. Iacopini, I., Milojevi´c, S. & Latora, V. Network dynamics of innovation processes. Physical review letters 120, 048301 (2018).
- 77. Mandelbrot, B. B. The fractal geometry of nature, vol. 1 (WH freeman New York, 1982).
- 78. Taleb, N. N. The black swan: The impact of the highly improbable, vol. 2 (Random house, 2007).


- 79. Jacob, B. A. & Lefgren, L. The impact of research grant funding on scientiﬁc productivity. Journal of public economics 95, 1168–1177 (2011).
- 80. Li, D., Azoulay, P. & Sampat, B. N. The applied value of public investments in biomedical research. Science 356, 78–81 (2017).
- 81. Heathcote, A., Brown, S. & Mewhort, D. The power law repealed: The case for an exponential law of practice. Psychonomic bulletin & review 7, 185–207 (2000).


|Category|Reference<br><br>|Time|Performance|Power law|Coexistence<br><br>|
|---|---|---|---|---|---|
|Adaptation|Crossman67<br><br>| | | | |
| |Kauffman & Levin68<br><br>| | | | |
| |Denrell & March70| | | | |
|Search|Roberts64<br><br>| | | | |
| |Muth42| | | | |
| |Mcnerney et al43| | | | |
|Individual learning<br><br>|Newell et al40| | | | |
| |Anderson41<br><br>| | | | |
|Urn|Simon74<br><br>| | | | |
| |Tria et al75| | | | |
| |Iacopini et al76| | | | |
|Other<br><br>|Levy39| | | | |
| |Shrager et al22<br><br>| | | | |
| |Sahal63<br><br>| | | | |
| |Johnson et al34<br><br>| | | | |
| |Clauset & Gleditsch33| | | | |


- Table S1: Literature review of relevant models. We test whether the models listed can predict (1) Time: time reduction; (2) Performance: performance improvement (or reduction in any cost other than time); (3) Power law: analytical form of power law scaling;


(4) Coexistence: coexistence of two groups with different dynamics (success and nonsuccess groups in this paper). We ﬁnd that none of the existing models can predict all the observations in our paper.

60

| | |Exponential<br><br>|Lognormal<br><br>|Power law|Truncated power law|
|---|---|---|---|---|---|
|NIH grants| |***|N.S.<br><br>|***<br><br>|***|
|Startups| |***|N.S.<br><br>|***|N.S.<br><br>|
|Terrorist attacks| |***|N.S.<br><br>|N.S.<br><br>|N.S.|


- Table S2: Comparing different functional forms of distributions with Weibull distributions. All signiﬁcant terms denote the degree that Weibull distribution is preferred over the other. Among all alternatives, only lognormal models show comparable ﬁtting performance. Yet lognormal model uses two free parameters while the shape parameter of Weibull distribution is constrained by the scaling identity (Eq. 4 in main text). ***: p < 0.01, N.S.: p > 0.1.


- a
- b


| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


- Figure S1: Data coverage test for D1. (a) Coverage of NIH grants in biomedical research, according to WOS acknowledgment data. NIH represents the majority of funding sources (81% out of top 10 agencies). (b) Fraction of all grants versus R01 grants through individual careers are almost the same. Hence R01 grant application data represents as an unbiased sampling of the NIH landscape.


# a

| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |


2000 2010

# b

- Figure S2: Time series of R01 applications in NIH grant systems. (a) Visualization of one scientist’s application history Orange lines show failed applications, while blue lines show succeeded applications. Length of orange lines show NIH evaluation scores, shorter lines correspond to better performance as evaluated by review panels. (b) Subsequence in (a) of all attempts until the ﬁrst success. Some applications do not have precise submission date, particularly those submitted before 2001, but their submission time can be inferred from proposed project end date of each application. For grants submitted after 2001, we compared the inferred and actual submission date, ﬁnding nearly perfect consistency between the two (Pearson correlation r = 0.98).


|VentureXpert<br><br>US total| | | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |


###### NumberofIPOs

- 101
- 102


1990 1995 2000 2005 2010 2015

Year

- Figure S3: Data coverage test for D2. Comparison of IPOs recorded in VentureXpert versus US market total. Our dataset captures a signiﬁcant fractions of IPOs, with the ratio between the two statistics remaining stable across time, indicating our data source represents as an unbiased sampling of the whole US market.


##### a b

1.0

| | |
|---|---|


0.04

0.8

0.03

0.6

CDF

PDF

0.02

0.4

0.01

0.2

0.0

0.00

0 25 50 75 100

Evaluation score

Success

Failure

0 25 50 75 100

Evaluation score

- Figure S4: Distribution of evaluation score for D1. (a) We ﬁnd the distribution of evaluation score is uniform between [0,50], but begins to truncate between [50,60], where the probability of getting a score lies around 57%. (b) Here we measure the evaluation scores for successful and failed attempts, ﬁnding the distributions are well separated.


0.6

### a b

| |
|---|


Success

10−5

Failure

0.5

10−7

0.4

10−9

###### PDF

PDF

0.3

0.2

10−11

0.1

10−13

0.0

103 105 107 109 1011

− 5.0 − 2.5 0.0 2.5 5.0

First investment amount

zamount

- Figure S5: Distribution of ﬁrst investment amount for D2. (a) The amount of ﬁrst investment follows a fat-tailed distribution and increases with year, prompting us to compare amount within year to account for such growth. (b) Here we measure the ﬁrst investment amount for successful and failed attempts, ﬁnding the distributions are well separated. To account for fat tails and temporal changes we use z-score of log(amount) within a year.


#### a b

|kill+1<br><br>wound+1|
|---|


10−1

10−3

###### PDF

PDF

10−5

10−7

100 101 102 103 104

Killed/Wounded individuals

|Success<br><br>Failure|
|---|


10−1

10−3

10−5

10−7

100 101 102 103 104

Wounded individuals

- Figure S6: Distribution of killed and wounded individuals for D3. (a) The number of killed and wounded individuals follow power law distributions, prompting us to take log(wounded + 1) as our performance measure. (b) Here we measure the number of wounded individuals for successful and failed attempts, ﬁnding the distributions are well separated.


###### xn zm

0.73 0.37 0.73 0.73 0.46 0.82 0.82 0.24 0.82 0.69 0.05 0.31

0.27 0.27 0.27 0.18 0.18 0.18 0.69

~z 0.27 0.18 0.69

um 5 6 …

- Figure S7: Illustration of model solutions. Here we visualize the notations used for solving the


model. xn denotes the score for the n-th attempt, zm ≡ 1 − xn corresponds to the potential given the best scoring among past k failures. z˜consists of all different zm as they ﬁrst appear. u measures the distance between two z˜-s, following a power law distribution as derived.

a b

- 0

- 1


ΓC() =K) =1 1

ΓC(K

Failure Dynamics

ΓB(K) = K

Phase transitions

###### Γ

0 1

K

−Γ2E=(21)

ΓA(K) = 0

h=K

0 1

K

c d

EC(h) = 1

- 0

- 1


EB(h) = (2h − 1)2

f

0 1

Canonical Ensembles

h

EA(h) = 1

0 1

h

###### Figure S8: Illustration of mapping between failure dynamics (a,b) and canonical ensembles

- (c,d). The canonical system is characterized by three different states a,b,c with corresponding


energy density Ea(h),Eb(h),Ec(h). We further assume that Ea(h) = (2ϵh−1)2, Eb(h) = h−h2, and Ec(h) = [2ϵ(1 − h) − 1]2 where ϵ → 0+. The introduction of ϵ is to distinguish state a from state c, and we approximate this with limiting condition Ea(h) = Ec(h) = 0. We map f → (2Γ − 1)2, N → lnn, h → K, and Ei(h) = [2Γi(K) − 1]2. Hence, the two transition points k∗ and k∗ + 1 corresponds to h = 0 and 1 in the canonical ensemble systems.

###### NIH Grants

###### Startups

###### Terrorist Attacks

###### a b c

| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |


| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |


| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |


40

50

30

%ofpopulation

%ofpopulation

%ofpopulation

30

40

20

30

20

20

10

10

10

0

0

0

Power law Exponential Linear

Power law Exponential Linear

Power law Exponential Linear

- Figure S9: Comparison of different models of temporal dynamics. We calculate the frequency that each model reaches minimum error among all three forms. Power law model offers consistently better predictions.


###### NIH Grants Startups

###### Terrorist Attacks

0.80

0.80

0.80

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
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |


| | | | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |


###### a b c

0.75

0.75

0.75

0.70

0.70

0.70

###### AUC

AUC

AUC

0.65

0.65

0.65

0.60

0.60

0.60

0.55

0.55

0.55

0.50

0.50

0.50

2 4 6 8

2 4 6

2 3

Number of failures

Number of failures

Number of failures

- Figure S10: Area Under the curve of the Receiver Operating Characteristic (AUROC) across three datasets. Green lines denote results from prediction model 1, red lines denote results from prediction model 2. Values are obtained from 10-fold cross validation across 50 randomized iterations.


- a
- b


|2 failures<br><br>3 failures<br><br>4 failures<br><br>5 failures<br><br>6 failures<br><br>7 failures<br><br>8 failures<br>| | | |
|---|---|---|---|
| | | | |


30

20

PDF

10

0

0.0 0.5 1.0 1.5 2.0

Coefficient

1.4

1.2

Ratio

1.0

0.8

0.6

2 4 6 8

Number of failures

- Figure S11: Analysis of prediction task. (a) Distribution of coefﬁcient β1 from prediction model 2 from D1. We ﬁnd that consistent with model predictions, β1 is positive across different N. (b) Variance importance ratio for prediction task on D1. Calculating variance importance ratio R for our prediction model 2, we ﬁnd an increasing proportion of uncovered predictive power contributed by γ, the slope of power law scaling.


- a d
- b e


1.0

1.0

###### Terrorist AttacksStartupsNIH Grants

0.8

0.8

0.6

0.6

CDF

CDF

0.4

0.4

0.2

0.2

P = 0.016

P = 0.443

0.0

0.0

0.6 0.8 1.0

0.6 0.8 1.0

Evaluation score

Evaluation score

1.0

1.0

0.8

0.8

0.6

0.6

CDF

CDF

0.4

0.4

0.2

0.2

P = 0.464

P = 0.011

0.0

0.0

− 5.0 − 2.5 0.0 2.5

− 5 0

Investment amount

Investment amount

c f

1.0

1.0

0.8

0.8

0.6

0.6

CDF

CDF

0.4

0.4

0.2

0.2

P = 0.998

P = 0.094

0.0

0.0

0 2 4

0 1 2 3

Wounded individuals

Wounded individuals

###### Figure S12: Performance dynamics of failure. Here we test performance dynamics using KStest. a-c show no signiﬁcant differences for success and non-success group at the ﬁrst attempt,while d-f show they are well separated at the second attempt.

- a d

- b e

- c f


![image 112](Quantifying the dynamics of failure across science startups and security_images/imageFile112.png)

- Figure S13: Testing ﬁtness hypothesis. The correlation between length of failure streak and initial


performance is weak (a-c, r = −0.05,−0.01,−0.13 respectively, not signiﬁcant for D2). We also ﬁnd the length of failure streak still follows fat-tailed distributions conditional on bottom 25% initial performance samples (d-f, KS test between sample and exponential distribution rejects the two distributions to be identical with p-value < 0.01).

| | | | |
|---|---|---|---|
| | | | |


| |
|---|


10−6

10−1

100 101

0 10 20

Number of failures

n

###### c d

1.0

0.80

| |NS **<br><br>**<br><br>NS| | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |


| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


0.75

- 0.5 First failure Second failure
- 0.6
- 0.7
- 0.8
- 0.9


Evaluationscore

0.70

AUC

0.65

0.60

0.55

0.50

2 4 6 8

| | | | |
|---|---|---|---|
| | | | |


| |
|---|


10−6

10−1

100 101

0 10 20

Number of failures

n

###### c d

1.0

0.80

| |NS *<br><br>*<br><br>NS| | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |


| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


0.75

0.9

Evaluationscore

0.70

0.8

AUC

0.65

0.7

0.60

0.6

0.55

0.5 First failure Second failure

0.50

2 4 6 8

| | | | |
|---|---|---|---|
| | | | |


| |
|---|


10−6

10−1

100 2× 100 3× 1040× 100 6× 100

0 5 10

Number of failures

n

###### c d

0.8

0.80

| |NS<br><br>***<br><br>**<br><br>NS| | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |


| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |


0.75

Investmentamount

0.6

0.70

AUC

0.4

0.65

0.60

0.2

0.55

0.0 First failure Second failure

0.50

2 4 6

| | | | |
|---|---|---|---|
| | | | |


| |
|---|


10−6

10−1

100 2× 100 3× 1040× 100 6× 100

0 5 10

Number of failures

n

###### c d

0.8

0.80

| |NS<br><br>***<br><br>**<br><br>NS| | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |


| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |


0.75

Investmentamount

0.6

0.70

AUC

0.4

0.65

0.60

0.2

0.55

0.0 First failure Second failure

0.50

2 4 6

| | | | |
|---|---|---|---|
| | | | |


| |
|---|


10−3

10−1

100 2× 100 3× 100 4× 100

0 10 20

Number of failures

n

###### c d

0.8

0.80

| |NS<br><br>***<br><br>***<br><br>NS| | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |


| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |


0.75

Woundedindividuals

0.6

0.70

AUC

0.4

0.65

0.60

0.2

0.55

0.0 First failure Second failure

0.50

2.0 2.5 3.0

| | | | |
|---|---|---|---|
| | | | |


| |
|---|


10−3

10−1

100 2× 100 3× 100 4× 100

0 10 20

Number of failures

n

###### c d

0.8

0.80

| |NS<br><br>***<br><br>***<br><br>NS| | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |


| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |


0.75

Woundedindividuals

0.6

0.70

AUC

0.4

0.65

0.60

0.2

0.55

0.0 First failure Second failure

0.50

2.0 2.5 3.0

| | | |
|---|---|---|
| | | |


| |
|---|


###### a b

100

10−1

100

10−2

###### CCDF

Tn

10−3

10−4

10−5

10−6

10−1

100 101

0 10 20

Number of failures

n

1.0

0.80

| |NS **<br><br>*<br><br>NS| | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |


| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


###### c d

0.75

- 0.5 First failure Second failure
- 0.6
- 0.7
- 0.8
- 0.9


Evaluationscore

0.70

AUC

0.65

0.60

0.55

0.50

2 4 6 8

Number of failures

- Figure S20: Robustness checks on D1 only excluding revisions as successes. We repeat analysis on length distribution of failure streak (a), temporal patterns (b), performance divergence at the early stage (c) and predictability of eventual success (d), ﬁning all these results still hold.


| | | |
|---|---|---|
| | | |


| |
|---|


###### a b

100

10−1

100

10−2

###### CCDF

Tn

10−3

10−4

10−5

10−6

10−1

100 2× 100 3× 1040 × 100 6× 100

0 10 20

Number of failures

n

1.0

0.80

| |NS ***<br><br>***<br><br>NS| | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |


| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |


###### c d

0.75

0.9

Evaluationscore

0.70

0.8

AUC

0.65

0.7

0.60

0.6

0.55

0.5 First failure Second failure

0.50

2 4 6

Number of failures

- Figure S21: Robustness checks on D1 only focusing on samples before one’s ﬁrst R01 success. We repeat analysis on length distribution of failure streak (a), temporal patterns (b), performance divergence at the early stage (c) and predictability of eventual success (d), ﬁning all these results still hold.


2 × 100

2 × 100

| |
|---|


| |
|---|


###### a b

100

100

Tn

Tn

6 × 10− 1

6 × 10− 1

- 2 × 10− 1
- 3 × 10− 1
- 4 × 10− 1


- 2 × 10− 1
- 3 × 10− 1
- 4 × 10− 1


100 2× 10

0 3 × 100 4 × 100 6 × 100

100 2× 10

0 3 × 100 4 × 100 6 × 100

n

n

- Figure S22: Robustness checks on D1 with respect to prior successes. Here we measure samples with (a) and without (b) prior success, ﬁnding they show similar temporal patterns.


| | | |
|---|---|---|
| | | |


| |
|---|


###### a b

100

10−1

100

10−2

###### CCDF

Tn

10−3

10−4

10−5

10−6

10−1

100 101

0 10 20

Number of failures

n

1.0

0.80

| |NS ***<br><br>*<br><br>NS| | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |


| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


###### c d

0.75

0.9

Evaluationscore

0.70

0.8

AUC

0.65

0.7

0.60

0.6

0.55

0.5 First failure Second failure

0.50

2 4 6 8

Number of failures

- Figure S23: Robustness checks on D1 as we change the discuss score threshold to 55. We repeat analysis on length distribution of failure streak (a), temporal patterns (b), performance divergence


- at the early stage (c) and predictability of eventual success (d), ﬁning all these results still hold.


| | | | |
|---|---|---|---|
| | | | |


| |
|---|


10−6

10−1

100 2× 100 3× 1040× 100 6× 100

0 5 10

Number of failures

n

0.8

0.80

###### c d

| |NS<br><br>***<br><br>**<br><br>NS| | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |


| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |


0.75

Investmentamount

0.6

0.70

AUC

0.4

0.65

0.60

0.2

0.55

0.0 First failure Second failure

0.50

2 4 6

Number of failures

- Figure S24: Robustness checks on D2 as we change the threshold of ‘high-value M&As’ as M&As that values ranking top 5% in the same year. We repeat analysis on length distribution of failure streak (a), temporal patterns (b), performance divergence at the early stage (c) and predictability of eventual success (d), ﬁning all these results still hold.


| | | | |
|---|---|---|---|
| | | | |


| |
|---|


10−6

10−1

100 2× 100 3× 1040× 100 6× 100

0 5 10

Number of failures

n

0.8

0.80

###### c d

| |NS<br><br>***<br><br>**<br><br>NS| | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |


| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |


0.75

Investmentamount

0.6

0.70

AUC

0.4

0.65

0.60

0.2

0.55

0.0 First failure Second failure

0.50

2 4 6

Number of failures

- Figure S25: Robustness checks on D2 as we exclude all M&As and restrict success as companies that went public. We repeat analysis on length distribution of failure streak (a), temporal patterns (b), performance divergence at the early stage (c) and predictability of eventual success


- (d), ﬁning all these results still hold.


| | | | |
|---|---|---|---|
| | | | |


| |
|---|


10−4

10−1

100 2× 100 3× 100 4× 100

0 10 20

Number of failures

n

1.0

0.80

| |NS<br><br>***<br><br>**<br><br>NS| | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |


| | | | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |


###### c d

0.75

Woundedindividuls

0.8

0.70

0.6

AUC

0.65

0.4

0.60

0.2

0.55

0.0 First failure Second failure

0.50

2 3

Number of failures

- Figure S26: Robustness checks on D3 as we restrict the attack type to be aimed at human beings. We repeat analysis on length distribution of failure streak (a), temporal patterns (b), performance divergence at the early stage (c) and predictability of eventual success (d), ﬁning all these results still hold.


| | | | |
|---|---|---|---|
| | | | |


| |
|---|


10−4

10−1

100 2× 100 3× 100 4× 100

0 10 20

Number of failures

n

1.0

0.80

| |NS<br><br>**<br><br>**<br><br>NS| | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |


| | | | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |


###### c d

0.75

Woundedindividuals

0.8

0.70

0.6

AUC

0.65

0.4

0.60

0.2

0.55

0.0 First failure Second failure

0.50

2 3

Number of failures

- Figure S27: Robustness checks on D3 as we restrict our samples to be within in perpetrator group list. We repeat analysis on length distribution of failure streak (a), temporal patterns (b), performance divergence at the early stage (c) and predictability of eventual success (d), ﬁning all these results still hold.


a b c

0.90

- 0.0 First failure Halfway failure
- 0.1
- 0.2
- 0.3
- 0.4
- 0.5
- 0.6


- 0.0 First failure Halfway failure
- 0.1
- 0.2
- 0.3
- 0.4
- 0.5
- 0.6
- 0.7
- 0.8


| |NS ***<br><br>***<br><br>NS| | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |


| |NS<br><br>***<br><br>*<br><br>NS| | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |


| |NS<br><br>***<br><br>***<br><br>NS| | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |


0.85

Woundedindividuals

Investmentamount

0.80

Evaluationscore

0.75

0.70

0.65

0.60

0.55

0.50 First failure Halfway failure

- d e f


0.90

- 0.0 First failure Penultimate failure
- 0.1
- 0.2
- 0.3
- 0.4
- 0.5
- 0.6


- 0.0 First failure Penultimate failure
- 0.1
- 0.2
- 0.3
- 0.4
- 0.5
- 0.6
- 0.7
- 0.8


| |NS ***<br><br>***<br><br>NS| | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |


| |NS<br><br>***<br><br>*<br><br>NS| | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |


| |NS<br><br>***<br><br>***<br><br>NS| | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |


0.85

Woundedindividuals

Investmentamount

0.80

Evaluationscore

0.75

0.70

0.65

0.60

0.55

0.50 First failure Penultimate failure

###### Figure S28: Robustness checks for different failures. Here we compare the performance dy-namics between the ﬁrst and halfway (a-c) and penultimate (d-f) failures across the three datasets,ﬁnding our results are broadly consistent with Fig. 4.

