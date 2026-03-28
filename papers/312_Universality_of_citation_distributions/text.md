arXiv:0806.0974v2[physics.soc-ph]27 Oct 2008

Universality of citation distributions: towards an objective measure of scientiﬁc impact.

Filippo Radicchi and Santo Fortunato

Complex Networks Lagrange Laboratory (CNLL), ISI Foundation, Torino, Italy

Claudio Castellano

SMC, INFM-CNR, and Dipartimento di Fisica, “Sapienza” Universita` di Roma, Piazzale A. Moro 2, 00185 Roma, Italy

We study the distributions of citations received by a single publication within several disciplines, spanning broad areas of science. We show that the probability that an article is cited c times has large variations between diﬀerent disciplines, but all distributions are rescaled on a universal curve when the relative indicator cf = c/c0 is considered, where c0 is the average number of citations per article for the discipline. In addition we show that the same universal behavior occurs when citation distributions of articles published in the same ﬁeld, but in diﬀerent years, are compared. These ﬁndings provide a strong validation of cf as an unbiased indicator for citation performance across disciplines and years. Based on this indicator, we introduce a generalization of the h-index suitable for comparing scientists working in diﬀerent ﬁelds.

I. INTRODUCTION

Citation analysis is a bibliometric tool that is becoming increasingly popular to evaluate the performance of diﬀerent actors in the academic and scientiﬁc arena, ranging from individual scholars [1, 2, 3], to journals, departments, universities [4] and national institutions [5] up to whole countries [6]. The outcome of such analysis often plays a crucial role to decide which grants are awarded, how applicants for a position are ranked, even the fate of scientiﬁc institutions. It is then crucial that citation analysis is carried out in the most precise and unbiased way.

Citation analysis has a very long history and many potential problems have been identiﬁed [7, 8, 9], the most critical being that often a citation does not – nor it is intended to – reﬂect the scientiﬁc merit of the cited work (in terms of quality or relevance). Additional sources of bias are, to mention just a few, self-citations, implicit citations, the increase in the total number of citations with time or the correlation between the number of authors of an article and the number of citations it receives [10].

In this work we consider one of the most relevant factors that may hamper a fair evaluation of scientiﬁc performance: ﬁeld variation. Publications in certain disciplines are typically cited much more or much less than in others. This may happen for several reasons, including uneven number of cited papers per article in diﬀerent ﬁelds or unbalanced cross-discipline citations [11]. A paradigmatic example is provided by mathematics: the highest 2006 impact factor (IF) [12] for journals in this category (Journal of the American Mathematical Society) is 2.55, whereas this ﬁgure is ten times larger or even more in other disciplines (for example, New England Journal of Medicine has 2006 IF 51.30, Cell has IF 29.19, Nature and Science have IF 26.68 and 30.03, respectively).

The existence of this bias is well-known [8, 10, 12] and it is widely recognized that comparing bare citation num-

bers is inappropriate. Many methods have been proposed to alleviate this problem [13, 14, 15, 16, 17]. They are based on the general idea of normalizing citation numbers with respect to some properly chosen reference standard. The choice of a suitable reference standard, that can be a journal, all journals in a discipline or a more complicated set [14] is a delicate issue [18]. Many possibilities exist also in the detailed implementation of the standardization procedure. Some methods are based on ranking articles (scientists, research groups) within one ﬁeld and comparing relative positions across disciplines. In many other cases relative indicators are deﬁned, i.e. ratios between the bare number of citations c and some average measure of the citation frequency in the reference standard. A simple example is the Relative Citation Rate of a group of articles [13], deﬁned as the total number of citations they received, divided by the weighted sum of impact factors of the journals where the articles were published.

The use of relative indicators is widespread, but empirical studies [19, 20, 21] have shown that distributions of article citations are very skewed, even within single disciplines. One may wonder then whether it is appropriate to normalize by the average citation number, that gives only very limited characterization of the whole distribution. We address this issue in this article.

The problem of ﬁeld variation aﬀects the evaluation of performance at many possible levels of detail: publications, individual scientists, research groups, institutions. Here we consider the simplest possible level, the evaluation of citation performance of single publications. When considering individuals or research groups, additional sources of bias (and of arbitrariness) exist, that we do not tackle here. As reference standard for an article, we consider the set of all papers published in journals that are classiﬁed in the same Journal of Citation Report scientiﬁc category of the journal where the publication appears (see details in Sec. VI). We take as normalizing quantity for citations of articles belonging to a given sci-

100

100

10-1

10-1

|Agricultural Economics & Policy<br><br>Allergy<br><br>Anesthesiology<br><br>Astronomy & Astrophysics<br><br>Biology<br><br>Computer Science, Cybernetics<br><br>Developmental Biology<br><br>Engineering, Aerospace<br><br>Hematology<br><br>Mathematics Microbiology Neuroimaging<br><br>Physics, Nuclear<br><br>Tropical Medicine<br><br>|
|---|


#### cP(c, c)00

10-2

10-2

# P(c, c)0

10-3

- 10-2 10-1 10cf0 101 102

10-5

10-4

- 10-3


10-4

|Engineering, Aerospace c0=5.65 Biology c0=14.60<br><br>Astronomy & Astrophysics c0=23.77<br><br>Hematology c0=30.61<br><br>Developmental Biology c0=38.67<br><br>|
|---|


10-5

10-6

100 101 c 102 103

Figure 2: Rescaled probability distribution c0P(c, c0) of the relative indicator cf = c/c0, showing that the universal scaling holds for all scientiﬁc disciplines considered (see table I). The dashed line is a lognormal ﬁt with σ2 = 1.3.

Figure 1: Normalized histogram of the number of articles P(c, c0) published in 1999 and having received c citations. We plot P(c, c0) for several scientiﬁc disciplines with diﬀerent average number c0 of citations per article.

entiﬁc ﬁeld the average number c0 of citations received by all articles in that discipline published in the same year. We perform an empirical analysis of the distribution of citations for publications in various disciplines and we show that the large variability in the number of bare citations c is fully accounted for when cf = c/c0 is considered. The distribution of this relative performance index is the same for all ﬁelds. No matter whether, for instance, Developmental Biology, Nuclear Physics or Aerospace Engineering are considered, the chance of having a particular value of cf is the same. Moreover, we show that cf allows to properly take into account the diﬀerences, within a single discipline, between articles published in diﬀerent years. This provides a strong validation of the use of cf as an unbiased relative indicator of scientiﬁc impact for comparison across ﬁelds and years.

II. VARIABILITY OF CITATION STATISTICS IN DIFFERENT DISCIPLINES

First of all we show explicitly that the distribution of the number of articles published in some year and cited a certain number of times strongly depends on the discipline considered. In Fig. 1 we plot the normalized distributions of citations to articles that appeared in 1999 in all journals belonging to several diﬀerent disciplines according to the Journal of Citation Reports classiﬁcation.

From this ﬁgure it is apparent that the chance of a publication to be cited strongly depends on the category the article belongs to. For example a publication with 100 citations is approximately 50 times more common in “Developmental Biology” than in “Engineering, Aerospace”. This has obvious implications in the evaluation of outstanding scientiﬁc achievements: the simple count of the number of citations is patently misleading to assess whether an article in Developmental Biology is

more successful than one in Aerospace Engineering.

III. DISTRIBUTION OF THE RELATIVE INDICATOR cf

A ﬁrst step toward properly taking into account ﬁeld variations is to recognize that the diﬀerences in the bare citation distributions are essentially not due to speciﬁc discipline-dependent factors, but are instead related to the pattern of citations in the ﬁeld, as measured by the average number of citations per article c0. It is natural then to try to factor out the bias induced by the diﬀerence in the value of c0 by considering a relative indicator, i.e. measuring the success of a publication by the ratio cf = c/c0 between the number of citations received and the average number of citations received by articles published in its ﬁeld in the same year. Fig. 2 shows that this procedure leads to a very good collapse of all curves for diﬀerent values of c0 onto a single shape. The distribution of the relative indicator cf seems then universal for all categories considered and resembles a lognormal distribution. In order to make these observations more quantitative, we have ﬁtted each curve in Fig. 2 for cf ≥ 0.1 with a lognormal curve

1 σcf√2π

f)−µ)2/2σ2, (1)

e−(log(c

F(cf) =

![image 1](Universality of citation distributions Toward an objective measure of scientific_images/imageFile1.png)

![image 2](Universality of citation distributions Toward an objective measure of scientific_images/imageFile2.png)

where the relation σ2 = −2µ, due to the fact that the expected value of the variable cf is 1, reduces the number of ﬁtting parameters to one. All ﬁtted values of σ2, reported in Table I, are compatible within two standard deviations, except for one (Anesthesiology) that is in any case within three standard deviations of all the others. Values of χ2 per degree of freedom, also reported in Table I, indicate that the ﬁt is good. This allows to conclude that, rescaling the distribution of citations for publications in a scientiﬁc discipline by their average number, a

Index Subject Category year Np c0 cmax σ2 χ2/df

![image 3](Universality of citation distributions Toward an objective measure of scientific_images/imageFile3.png)

![image 4](Universality of citation distributions Toward an objective measure of scientific_images/imageFile4.png)

![image 5](Universality of citation distributions Toward an objective measure of scientific_images/imageFile5.png)

![image 6](Universality of citation distributions Toward an objective measure of scientific_images/imageFile6.png)

![image 7](Universality of citation distributions Toward an objective measure of scientific_images/imageFile7.png)

- 1 Agricultural Economics & Policy 1999 266 6.88 42 1.0(1) 0.007

![image 8](Universality of citation distributions Toward an objective measure of scientific_images/imageFile8.png)

![image 9](Universality of citation distributions Toward an objective measure of scientific_images/imageFile9.png)

![image 10](Universality of citation distributions Toward an objective measure of scientific_images/imageFile10.png)

![image 11](Universality of citation distributions Toward an objective measure of scientific_images/imageFile11.png)

![image 12](Universality of citation distributions Toward an objective measure of scientific_images/imageFile12.png)

![image 13](Universality of citation distributions Toward an objective measure of scientific_images/imageFile13.png)

![image 14](Universality of citation distributions Toward an objective measure of scientific_images/imageFile14.png)

![image 15](Universality of citation distributions Toward an objective measure of scientific_images/imageFile15.png)

![image 16](Universality of citation distributions Toward an objective measure of scientific_images/imageFile16.png)

![image 17](Universality of citation distributions Toward an objective measure of scientific_images/imageFile17.png)

- 2 Allergy 1999 1530 17.39 271 1.4(2) 0.012

![image 18](Universality of citation distributions Toward an objective measure of scientific_images/imageFile18.png)

![image 19](Universality of citation distributions Toward an objective measure of scientific_images/imageFile19.png)

![image 20](Universality of citation distributions Toward an objective measure of scientific_images/imageFile20.png)

![image 21](Universality of citation distributions Toward an objective measure of scientific_images/imageFile21.png)

![image 22](Universality of citation distributions Toward an objective measure of scientific_images/imageFile22.png)

![image 23](Universality of citation distributions Toward an objective measure of scientific_images/imageFile23.png)

![image 24](Universality of citation distributions Toward an objective measure of scientific_images/imageFile24.png)

![image 25](Universality of citation distributions Toward an objective measure of scientific_images/imageFile25.png)

![image 26](Universality of citation distributions Toward an objective measure of scientific_images/imageFile26.png)

![image 27](Universality of citation distributions Toward an objective measure of scientific_images/imageFile27.png)

- 3 Anesthesiology 1999 3472 13.25 282 1.8(2) 0.009

![image 28](Universality of citation distributions Toward an objective measure of scientific_images/imageFile28.png)

![image 29](Universality of citation distributions Toward an objective measure of scientific_images/imageFile29.png)

![image 30](Universality of citation distributions Toward an objective measure of scientific_images/imageFile30.png)

![image 31](Universality of citation distributions Toward an objective measure of scientific_images/imageFile31.png)

![image 32](Universality of citation distributions Toward an objective measure of scientific_images/imageFile32.png)

![image 33](Universality of citation distributions Toward an objective measure of scientific_images/imageFile33.png)

![image 34](Universality of citation distributions Toward an objective measure of scientific_images/imageFile34.png)

![image 35](Universality of citation distributions Toward an objective measure of scientific_images/imageFile35.png)

![image 36](Universality of citation distributions Toward an objective measure of scientific_images/imageFile36.png)

![image 37](Universality of citation distributions Toward an objective measure of scientific_images/imageFile37.png)

- 4 Astronomy & Astrophysics 1999 7399 23.77 1028 1.1(1) 0.003

![image 38](Universality of citation distributions Toward an objective measure of scientific_images/imageFile38.png)

![image 39](Universality of citation distributions Toward an objective measure of scientific_images/imageFile39.png)

![image 40](Universality of citation distributions Toward an objective measure of scientific_images/imageFile40.png)

![image 41](Universality of citation distributions Toward an objective measure of scientific_images/imageFile41.png)

![image 42](Universality of citation distributions Toward an objective measure of scientific_images/imageFile42.png)

![image 43](Universality of citation distributions Toward an objective measure of scientific_images/imageFile43.png)

![image 44](Universality of citation distributions Toward an objective measure of scientific_images/imageFile44.png)

![image 45](Universality of citation distributions Toward an objective measure of scientific_images/imageFile45.png)

![image 46](Universality of citation distributions Toward an objective measure of scientific_images/imageFile46.png)

![image 47](Universality of citation distributions Toward an objective measure of scientific_images/imageFile47.png)

- 5 Biology 1999 3400 14.6 413 1.3(1) 0.004

![image 48](Universality of citation distributions Toward an objective measure of scientific_images/imageFile48.png)

![image 49](Universality of citation distributions Toward an objective measure of scientific_images/imageFile49.png)

![image 50](Universality of citation distributions Toward an objective measure of scientific_images/imageFile50.png)

![image 51](Universality of citation distributions Toward an objective measure of scientific_images/imageFile51.png)

![image 52](Universality of citation distributions Toward an objective measure of scientific_images/imageFile52.png)

![image 53](Universality of citation distributions Toward an objective measure of scientific_images/imageFile53.png)

![image 54](Universality of citation distributions Toward an objective measure of scientific_images/imageFile54.png)

![image 55](Universality of citation distributions Toward an objective measure of scientific_images/imageFile55.png)

![image 56](Universality of citation distributions Toward an objective measure of scientific_images/imageFile56.png)

![image 57](Universality of citation distributions Toward an objective measure of scientific_images/imageFile57.png)

- 6 Computer Science, Cybernetics 1999 704 8.49 100 1.3(1) 0.004

![image 58](Universality of citation distributions Toward an objective measure of scientific_images/imageFile58.png)

![image 59](Universality of citation distributions Toward an objective measure of scientific_images/imageFile59.png)

![image 60](Universality of citation distributions Toward an objective measure of scientific_images/imageFile60.png)

![image 61](Universality of citation distributions Toward an objective measure of scientific_images/imageFile61.png)

![image 62](Universality of citation distributions Toward an objective measure of scientific_images/imageFile62.png)

![image 63](Universality of citation distributions Toward an objective measure of scientific_images/imageFile63.png)

![image 64](Universality of citation distributions Toward an objective measure of scientific_images/imageFile64.png)

![image 65](Universality of citation distributions Toward an objective measure of scientific_images/imageFile65.png)

![image 66](Universality of citation distributions Toward an objective measure of scientific_images/imageFile66.png)

![image 67](Universality of citation distributions Toward an objective measure of scientific_images/imageFile67.png)

- 7 Developmental Biology 1999 2982 38.67 520 1.3(3) 0.002

![image 68](Universality of citation distributions Toward an objective measure of scientific_images/imageFile68.png)

![image 69](Universality of citation distributions Toward an objective measure of scientific_images/imageFile69.png)

![image 70](Universality of citation distributions Toward an objective measure of scientific_images/imageFile70.png)

![image 71](Universality of citation distributions Toward an objective measure of scientific_images/imageFile71.png)

![image 72](Universality of citation distributions Toward an objective measure of scientific_images/imageFile72.png)

![image 73](Universality of citation distributions Toward an objective measure of scientific_images/imageFile73.png)

![image 74](Universality of citation distributions Toward an objective measure of scientific_images/imageFile74.png)

![image 75](Universality of citation distributions Toward an objective measure of scientific_images/imageFile75.png)

![image 76](Universality of citation distributions Toward an objective measure of scientific_images/imageFile76.png)

![image 77](Universality of citation distributions Toward an objective measure of scientific_images/imageFile77.png)

- 8 Engineering, Aerospace 1999 1070 5.65 95 1.4(1) 0.003

![image 78](Universality of citation distributions Toward an objective measure of scientific_images/imageFile78.png)

![image 79](Universality of citation distributions Toward an objective measure of scientific_images/imageFile79.png)

![image 80](Universality of citation distributions Toward an objective measure of scientific_images/imageFile80.png)

![image 81](Universality of citation distributions Toward an objective measure of scientific_images/imageFile81.png)

![image 82](Universality of citation distributions Toward an objective measure of scientific_images/imageFile82.png)

![image 83](Universality of citation distributions Toward an objective measure of scientific_images/imageFile83.png)

![image 84](Universality of citation distributions Toward an objective measure of scientific_images/imageFile84.png)

![image 85](Universality of citation distributions Toward an objective measure of scientific_images/imageFile85.png)

![image 86](Universality of citation distributions Toward an objective measure of scientific_images/imageFile86.png)

![image 87](Universality of citation distributions Toward an objective measure of scientific_images/imageFile87.png)

- 9 Hematology 1990 4423 41.05 1424 1.5(1) 0.002

![image 88](Universality of citation distributions Toward an objective measure of scientific_images/imageFile88.png)

![image 89](Universality of citation distributions Toward an objective measure of scientific_images/imageFile89.png)

![image 90](Universality of citation distributions Toward an objective measure of scientific_images/imageFile90.png)

![image 91](Universality of citation distributions Toward an objective measure of scientific_images/imageFile91.png)

![image 92](Universality of citation distributions Toward an objective measure of scientific_images/imageFile92.png)

![image 93](Universality of citation distributions Toward an objective measure of scientific_images/imageFile93.png)

![image 94](Universality of citation distributions Toward an objective measure of scientific_images/imageFile94.png)

![image 95](Universality of citation distributions Toward an objective measure of scientific_images/imageFile95.png)

![image 96](Universality of citation distributions Toward an objective measure of scientific_images/imageFile96.png)

![image 97](Universality of citation distributions Toward an objective measure of scientific_images/imageFile97.png)

- 10 Hematology 1999 6920 30.61 966 1.3(1) 0.004

![image 98](Universality of citation distributions Toward an objective measure of scientific_images/imageFile98.png)

![image 99](Universality of citation distributions Toward an objective measure of scientific_images/imageFile99.png)

![image 100](Universality of citation distributions Toward an objective measure of scientific_images/imageFile100.png)

![image 101](Universality of citation distributions Toward an objective measure of scientific_images/imageFile101.png)

![image 102](Universality of citation distributions Toward an objective measure of scientific_images/imageFile102.png)

![image 103](Universality of citation distributions Toward an objective measure of scientific_images/imageFile103.png)

![image 104](Universality of citation distributions Toward an objective measure of scientific_images/imageFile104.png)

![image 105](Universality of citation distributions Toward an objective measure of scientific_images/imageFile105.png)

![image 106](Universality of citation distributions Toward an objective measure of scientific_images/imageFile106.png)

![image 107](Universality of citation distributions Toward an objective measure of scientific_images/imageFile107.png)

- 11 Hematology 2004 8695 15.66 1014 1.3(1) 0.003

![image 108](Universality of citation distributions Toward an objective measure of scientific_images/imageFile108.png)

![image 109](Universality of citation distributions Toward an objective measure of scientific_images/imageFile109.png)

![image 110](Universality of citation distributions Toward an objective measure of scientific_images/imageFile110.png)

![image 111](Universality of citation distributions Toward an objective measure of scientific_images/imageFile111.png)

![image 112](Universality of citation distributions Toward an objective measure of scientific_images/imageFile112.png)

![image 113](Universality of citation distributions Toward an objective measure of scientific_images/imageFile113.png)

![image 114](Universality of citation distributions Toward an objective measure of scientific_images/imageFile114.png)

![image 115](Universality of citation distributions Toward an objective measure of scientific_images/imageFile115.png)

![image 116](Universality of citation distributions Toward an objective measure of scientific_images/imageFile116.png)

![image 117](Universality of citation distributions Toward an objective measure of scientific_images/imageFile117.png)

- 12 Mathematics 1999 8440 5.97 191 1.3(4) 0.001

![image 118](Universality of citation distributions Toward an objective measure of scientific_images/imageFile118.png)

![image 119](Universality of citation distributions Toward an objective measure of scientific_images/imageFile119.png)

![image 120](Universality of citation distributions Toward an objective measure of scientific_images/imageFile120.png)

![image 121](Universality of citation distributions Toward an objective measure of scientific_images/imageFile121.png)

![image 122](Universality of citation distributions Toward an objective measure of scientific_images/imageFile122.png)

![image 123](Universality of citation distributions Toward an objective measure of scientific_images/imageFile123.png)

![image 124](Universality of citation distributions Toward an objective measure of scientific_images/imageFile124.png)

![image 125](Universality of citation distributions Toward an objective measure of scientific_images/imageFile125.png)

![image 126](Universality of citation distributions Toward an objective measure of scientific_images/imageFile126.png)

![image 127](Universality of citation distributions Toward an objective measure of scientific_images/imageFile127.png)

- 13 Microbiology 1999 9761 21.54 803 1.0(1) 0.005

![image 128](Universality of citation distributions Toward an objective measure of scientific_images/imageFile128.png)

![image 129](Universality of citation distributions Toward an objective measure of scientific_images/imageFile129.png)

![image 130](Universality of citation distributions Toward an objective measure of scientific_images/imageFile130.png)

![image 131](Universality of citation distributions Toward an objective measure of scientific_images/imageFile131.png)

![image 132](Universality of citation distributions Toward an objective measure of scientific_images/imageFile132.png)

![image 133](Universality of citation distributions Toward an objective measure of scientific_images/imageFile133.png)

![image 134](Universality of citation distributions Toward an objective measure of scientific_images/imageFile134.png)

![image 135](Universality of citation distributions Toward an objective measure of scientific_images/imageFile135.png)

![image 136](Universality of citation distributions Toward an objective measure of scientific_images/imageFile136.png)

![image 137](Universality of citation distributions Toward an objective measure of scientific_images/imageFile137.png)

- 14 Neuroimaging 1990 444 25.26 518 1.1(1) 0.004

![image 138](Universality of citation distributions Toward an objective measure of scientific_images/imageFile138.png)

![image 139](Universality of citation distributions Toward an objective measure of scientific_images/imageFile139.png)

![image 140](Universality of citation distributions Toward an objective measure of scientific_images/imageFile140.png)

![image 141](Universality of citation distributions Toward an objective measure of scientific_images/imageFile141.png)

![image 142](Universality of citation distributions Toward an objective measure of scientific_images/imageFile142.png)

![image 143](Universality of citation distributions Toward an objective measure of scientific_images/imageFile143.png)

![image 144](Universality of citation distributions Toward an objective measure of scientific_images/imageFile144.png)

![image 145](Universality of citation distributions Toward an objective measure of scientific_images/imageFile145.png)

![image 146](Universality of citation distributions Toward an objective measure of scientific_images/imageFile146.png)

![image 147](Universality of citation distributions Toward an objective measure of scientific_images/imageFile147.png)

- 15 Neuroimaging 1999 1073 23.16 463 1.4(1) 0.003

![image 148](Universality of citation distributions Toward an objective measure of scientific_images/imageFile148.png)

![image 149](Universality of citation distributions Toward an objective measure of scientific_images/imageFile149.png)

![image 150](Universality of citation distributions Toward an objective measure of scientific_images/imageFile150.png)

![image 151](Universality of citation distributions Toward an objective measure of scientific_images/imageFile151.png)

![image 152](Universality of citation distributions Toward an objective measure of scientific_images/imageFile152.png)

![image 153](Universality of citation distributions Toward an objective measure of scientific_images/imageFile153.png)

![image 154](Universality of citation distributions Toward an objective measure of scientific_images/imageFile154.png)

![image 155](Universality of citation distributions Toward an objective measure of scientific_images/imageFile155.png)

![image 156](Universality of citation distributions Toward an objective measure of scientific_images/imageFile156.png)

![image 157](Universality of citation distributions Toward an objective measure of scientific_images/imageFile157.png)

- 16 Neuroimaging 2004 1395 12.68 132 1.1(1) 0.005

![image 158](Universality of citation distributions Toward an objective measure of scientific_images/imageFile158.png)

![image 159](Universality of citation distributions Toward an objective measure of scientific_images/imageFile159.png)

![image 160](Universality of citation distributions Toward an objective measure of scientific_images/imageFile160.png)

![image 161](Universality of citation distributions Toward an objective measure of scientific_images/imageFile161.png)

![image 162](Universality of citation distributions Toward an objective measure of scientific_images/imageFile162.png)

![image 163](Universality of citation distributions Toward an objective measure of scientific_images/imageFile163.png)

![image 164](Universality of citation distributions Toward an objective measure of scientific_images/imageFile164.png)

![image 165](Universality of citation distributions Toward an objective measure of scientific_images/imageFile165.png)

![image 166](Universality of citation distributions Toward an objective measure of scientific_images/imageFile166.png)

![image 167](Universality of citation distributions Toward an objective measure of scientific_images/imageFile167.png)

- 17 Physics, Nuclear 1990 3670 13.75 387 1.4(1) 0.001

![image 168](Universality of citation distributions Toward an objective measure of scientific_images/imageFile168.png)

![image 169](Universality of citation distributions Toward an objective measure of scientific_images/imageFile169.png)

![image 170](Universality of citation distributions Toward an objective measure of scientific_images/imageFile170.png)

![image 171](Universality of citation distributions Toward an objective measure of scientific_images/imageFile171.png)

![image 172](Universality of citation distributions Toward an objective measure of scientific_images/imageFile172.png)

![image 173](Universality of citation distributions Toward an objective measure of scientific_images/imageFile173.png)

![image 174](Universality of citation distributions Toward an objective measure of scientific_images/imageFile174.png)

![image 175](Universality of citation distributions Toward an objective measure of scientific_images/imageFile175.png)

![image 176](Universality of citation distributions Toward an objective measure of scientific_images/imageFile176.png)

![image 177](Universality of citation distributions Toward an objective measure of scientific_images/imageFile177.png)

- 18 Physics, Nuclear 1999 3965 10.92 434 1.4(4) 0.001

![image 178](Universality of citation distributions Toward an objective measure of scientific_images/imageFile178.png)

![image 179](Universality of citation distributions Toward an objective measure of scientific_images/imageFile179.png)

![image 180](Universality of citation distributions Toward an objective measure of scientific_images/imageFile180.png)

![image 181](Universality of citation distributions Toward an objective measure of scientific_images/imageFile181.png)

![image 182](Universality of citation distributions Toward an objective measure of scientific_images/imageFile182.png)

![image 183](Universality of citation distributions Toward an objective measure of scientific_images/imageFile183.png)

![image 184](Universality of citation distributions Toward an objective measure of scientific_images/imageFile184.png)

![image 185](Universality of citation distributions Toward an objective measure of scientific_images/imageFile185.png)

![image 186](Universality of citation distributions Toward an objective measure of scientific_images/imageFile186.png)

![image 187](Universality of citation distributions Toward an objective measure of scientific_images/imageFile187.png)

- 19 Physics, Nuclear 2004 4164 6.94 218 1.4(1) 0.001

![image 188](Universality of citation distributions Toward an objective measure of scientific_images/imageFile188.png)

![image 189](Universality of citation distributions Toward an objective measure of scientific_images/imageFile189.png)

![image 190](Universality of citation distributions Toward an objective measure of scientific_images/imageFile190.png)

![image 191](Universality of citation distributions Toward an objective measure of scientific_images/imageFile191.png)

![image 192](Universality of citation distributions Toward an objective measure of scientific_images/imageFile192.png)

![image 193](Universality of citation distributions Toward an objective measure of scientific_images/imageFile193.png)

![image 194](Universality of citation distributions Toward an objective measure of scientific_images/imageFile194.png)

![image 195](Universality of citation distributions Toward an objective measure of scientific_images/imageFile195.png)

![image 196](Universality of citation distributions Toward an objective measure of scientific_images/imageFile196.png)

![image 197](Universality of citation distributions Toward an objective measure of scientific_images/imageFile197.png)

- 20 Tropical Medicine 1999 1038 12.35 126 1.1(1) 0.017


![image 198](Universality of citation distributions Toward an objective measure of scientific_images/imageFile198.png)

![image 199](Universality of citation distributions Toward an objective measure of scientific_images/imageFile199.png)

![image 200](Universality of citation distributions Toward an objective measure of scientific_images/imageFile200.png)

![image 201](Universality of citation distributions Toward an objective measure of scientific_images/imageFile201.png)

![image 202](Universality of citation distributions Toward an objective measure of scientific_images/imageFile202.png)

![image 203](Universality of citation distributions Toward an objective measure of scientific_images/imageFile203.png)

![image 204](Universality of citation distributions Toward an objective measure of scientific_images/imageFile204.png)

![image 205](Universality of citation distributions Toward an objective measure of scientific_images/imageFile205.png)

![image 206](Universality of citation distributions Toward an objective measure of scientific_images/imageFile206.png)

Table I: List of all scientiﬁc disciplines considered in this article. For each category we report the total number of articles Np, the average number of citations c0, the maximum number of citations cmax, the value of the ﬁtting parameter σ2 in Eq. (1) and the corresponding χ2 per degree of freedom. Data refer to articles published in journals listed by Journal of Citation Reports under a speciﬁc subject category.

universal curve is found, independent of the speciﬁc discipline. Fitting a single curve for all categories, a lognormal distribution with σ2 = 1.3 is found, that is reported in Figure 2.

Interestingly, a similar universality for the distribution of the relative performance is found, in a totally diﬀerent context, when the number of votes received by candidates in proportional elections is considered [22]. In that case, the scaling curve is also well-ﬁtted by a lognormal with parameter σ2 ≈ 1.1. For universality in the dynamics of academic research activities see also [23].

The universal scaling obtained provides a solid grounding for comparison between articles in diﬀerent ﬁelds. To make this even more visually evident, we have ranked all articles belonging to a pool of diﬀerent disciplines (spanning broad areas of science) according either to c and to cf. We have then computed the percentage of publications of each discipline that appear in the top z% of the global rank. If the ranking is fair the percentage for each discipline should be around z% with small ﬂuctuations. Fig. 3 clearly shows that when articles are ranked according to the unnormalized number of citations c there are wide variations among disciplines. Such variations are dramatically reduced instead when the relative indicator cf is used. This occurs for various choices of the percentage z. More quantitatively, assuming that articles of the various disciplines are scattered uniformly along the rank

axis, one would expect the average bin height in Fig. 3 to be z% with a standard deviation

σz =

![image 207](Universality of citation distributions Toward an objective measure of scientific_images/imageFile207.png)

Nc

1 Ni

z (100 − z) Nc

, (2)

![image 208](Universality of citation distributions Toward an objective measure of scientific_images/imageFile208.png)

![image 209](Universality of citation distributions Toward an objective measure of scientific_images/imageFile209.png)

i=1

where Nc is the number of categories and Ni the number of articles in the i-th category. When the ranking is performed according to cf = c/c0 we ﬁnd (Table II) a very good agreement with the hypothesis that the ranking is unbiased, while strong evidence that the ranking is biased is found when c is used. For example, for z = 20%, σz = 1.15% for cf-based ranking, while σz = 12.37% if c is used, as opposed to the value σz = 1.09% in the hypothesis of unbiased ranking. Figures 2 and 3 allow to conclude that cf is an unbiased indicator for comparing the scientiﬁc impact of publications in diﬀerent disciplines. For the normalization of the relative indicator, we have considered the average number c0 of citations per article published in the same year and in the same ﬁeld. This is a very natural choice, giving to the numerical value of cf the direct interpretation as relative citation performance of the publication. In the literature this quantity is also indicated as the “item oriented ﬁeld normalized citation score” [24], an analogue for a single publication of the popular CWTS (Centre for Science and Technology Studies, Leiden) ﬁeld normalized cita-

Top 5%

15

% papers

10

5

0

- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 8


- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 8


10

- 12
- 13 15


18

10

- 12
- 13 15


18

20

20

Top 10%

25

20

% papers

15

10

5

0

- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 8


- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 8


10

- 12
- 13 15


18

10

- 12
- 13 15


18

20

20

Top 20%

40

30

% papers

20

10

0

- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 8


- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 8


10

- 12
- 13 15


18

10

- 12
- 13 15


18

20

20

Top 40%

60

50

% papers

40

30

20

10

0

- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 8


- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 8


10

- 12
- 13 15


18

10

- 12
- 13 15


18

20

20

- Figure 3: We rank all articles according to the bare number


of citations c and the relative indicator cf. We then plot the percentage of articles of a particular discipline present in the top z% of the general ranking, for the rank based on the number of citations ( histograms on the left in each panel) and based on the relative indicator cf (histograms on the right). Diﬀerent values of z (diﬀerent panels) lead to very similar pattern of results. The average values and the standard deviations of the bin heights shown are also reported in Table II. The numbers identify the disciplines as they are indicated in Table I.

![image 210](Universality of citation distributions Toward an objective measure of scientific_images/imageFile210.png)

![image 211](Universality of citation distributions Toward an objective measure of scientific_images/imageFile211.png)

![image 212](Universality of citation distributions Toward an objective measure of scientific_images/imageFile212.png)

![image 213](Universality of citation distributions Toward an objective measure of scientific_images/imageFile213.png)

![image 214](Universality of citation distributions Toward an objective measure of scientific_images/imageFile214.png)

![image 215](Universality of citation distributions Toward an objective measure of scientific_images/imageFile215.png)

![image 216](Universality of citation distributions Toward an objective measure of scientific_images/imageFile216.png)

z σz(theor) z(c) σz(c) z(cf) σz(cf) 5 0.59 4.38 4.73 5.14 0.51 10 0.81 8.69 7.92 10.07 0.67 20 1.09 17.68 12.37 20.03 1.15 40 1.33 35.67 17.48 39.86 2.58

![image 217](Universality of citation distributions Toward an objective measure of scientific_images/imageFile217.png)

![image 218](Universality of citation distributions Toward an objective measure of scientific_images/imageFile218.png)

![image 219](Universality of citation distributions Toward an objective measure of scientific_images/imageFile219.png)

![image 220](Universality of citation distributions Toward an objective measure of scientific_images/imageFile220.png)

![image 221](Universality of citation distributions Toward an objective measure of scientific_images/imageFile221.png)

![image 222](Universality of citation distributions Toward an objective measure of scientific_images/imageFile222.png)

![image 223](Universality of citation distributions Toward an objective measure of scientific_images/imageFile223.png)

![image 224](Universality of citation distributions Toward an objective measure of scientific_images/imageFile224.png)

![image 225](Universality of citation distributions Toward an objective measure of scientific_images/imageFile225.png)

![image 226](Universality of citation distributions Toward an objective measure of scientific_images/imageFile226.png)

![image 227](Universality of citation distributions Toward an objective measure of scientific_images/imageFile227.png)

![image 228](Universality of citation distributions Toward an objective measure of scientific_images/imageFile228.png)

![image 229](Universality of citation distributions Toward an objective measure of scientific_images/imageFile229.png)

![image 230](Universality of citation distributions Toward an objective measure of scientific_images/imageFile230.png)

![image 231](Universality of citation distributions Toward an objective measure of scientific_images/imageFile231.png)

![image 232](Universality of citation distributions Toward an objective measure of scientific_images/imageFile232.png)

![image 233](Universality of citation distributions Toward an objective measure of scientific_images/imageFile233.png)

![image 234](Universality of citation distributions Toward an objective measure of scientific_images/imageFile234.png)

![image 235](Universality of citation distributions Toward an objective measure of scientific_images/imageFile235.png)

![image 236](Universality of citation distributions Toward an objective measure of scientific_images/imageFile236.png)

![image 237](Universality of citation distributions Toward an objective measure of scientific_images/imageFile237.png)

![image 238](Universality of citation distributions Toward an objective measure of scientific_images/imageFile238.png)

![image 239](Universality of citation distributions Toward an objective measure of scientific_images/imageFile239.png)

![image 240](Universality of citation distributions Toward an objective measure of scientific_images/imageFile240.png)

![image 241](Universality of citation distributions Toward an objective measure of scientific_images/imageFile241.png)

![image 242](Universality of citation distributions Toward an objective measure of scientific_images/imageFile242.png)

![image 243](Universality of citation distributions Toward an objective measure of scientific_images/imageFile243.png)

![image 244](Universality of citation distributions Toward an objective measure of scientific_images/imageFile244.png)

![image 245](Universality of citation distributions Toward an objective measure of scientific_images/imageFile245.png)

Table II: Average and standard deviation for the bin heights in Fig. 3. Comparison between the values expected theoretically for unbiased ranking (ﬁrst two columns), and those obtained empirically when articles are ranked according to c (third and fourth columns) and according to cf (last two columns).

tion score or “crown indicator” [25]. In agreement with the ﬁndings of Ref. [11] c0 shows very little correlation with the overall size of the ﬁeld, as measured by the total number of articles.

The previous analysis compares distributions of citations to articles published in a single year, 1999. It is known that diﬀerent temporal patterns of citations exist, with some articles starting soon to receive citations, while others (“sleeping beauties”) go unnoticed for a long time, after which they are recognized as seminal and begin to attract a large number of citations [26, 27]. Other diﬀerences exist between disciplines, with noticeable ﬂuctuations in the cited half-life indicator across ﬁelds. It is then natural to wonder whether the universality of distributions for articles published in the same year extends longitudinally in time so that the relative indicator allows comparison of articles published in diﬀerent years. For this reason, in Fig. 4 we compare the plot of c0P(c,c0) vs cf for publications in the same scientiﬁc discipline appeared in three diﬀerent years. The value of c0 obviously grows as older publications are considered, but the rescaled distribution remains conspicuously the same.

IV. A GENERALIZED H-INDEX

Since its introduction in 2005, the h-index [1] has enjoyed a spectacularly quick success [28]: it is now a well established standard tool for the evaluation of the scientiﬁc performance of scientists. Its popularity is partly due to its simplicity: the h-index of an author is h if h of his N articles have at least h citations each, and the other N − h articles have at most h citations each. Despite its success, as all other performance metrics the h-index has some shortcomings, as already pointed out by Hirsch himself. One of them is the diﬃculty to compare authors in diﬀerent disciplines. The identiﬁcation of the relative indicator cf as the correct metrics to compare articles in diﬀerent disciplines naturally suggests its use in a generalized version of the h-index taking properly into account diﬀerent citation patterns across disciplines. However, just ranking articles according to cf, instead of on the basis of the bare citation number c, is not enough. A crucial ingredient of the h-index is the number of articles

100

10-1

## cP(c, c)00

10-2

|Hematology 1990 c0=41.05 Hematology 1999 c0=30.61 Hematology 2004 c0=15.66<br><br>Neuroimaging 1990 c0=25.26 Neuroimaging 1999 c0=23.16 Neuroimaging 2004 c0=12.68<br><br>Physics, Nuclear 1990 c0=13.76 Physics, Nuclear 1999 c0=10.92 Physics, Nuclear 2004 c0=6.94<br><br>|
|---|


- 10-2 10-1 10cf0 101 102

10-5

10-4

- 10-3


- Figure 4: Rescaled probability distribution c0P(c, c0) of the relative indicator cf = c/c0 for three disciplines (“Hematology”, “Neuroimaging”, and ”Physics, Nuclear”) for articles published in diﬀerent years (1990, 1999 and 2004). In spite

of the natural variation of c0 (c0 grows as a function of the elapsed time), the universal scaling observed over diﬀerent disciplines naturally holds also for articles published in diﬀerent periods of time. The dashed line is a lognormal ﬁt with σ2 = 1.3.

100 101

N

10-6

10-4

10-2

100

P(N, N)0

100 101

N/N0

10-6

10-5

10-4

10-3

10-2

10-1

100

NP(N, N)00

|Engineering, Aerospace N0=1.19<br><br>Microbiology N0=1.36<br><br>Hematolgy N0=1.43<br><br>Computer Science, Cybernetics N0=1.71<br><br>Astronomy & Astrophysics N0=2.27<br><br>|
|---|


- Figure 5: Inset: distributions of the number of articles N published by an author during 1999 in several disciplines. Main: the same distributions rescaled by the average num-


ber N0 of publications per author in 1999 in the diﬀerent disciplines. The dashed line is a power-law with exponent −3.5.

published by an author. As Fig. 5 shows, such a quantity also depends on the discipline considered: in some disciplines the average number of articles published by an author in a year is much larger than in others. But also in this case this variability is rescaled away if the number N of publications in a year by an author is divided by the average value in the discipline N0. Interestingly, the universal curve is ﬁtted reasonably well over almost two decades by a power-law behavior P(N,N0) ≈ (N/N0)−δ with δ = 3.5(5).

This universality allows one to deﬁne a generalized hindex, hf, that factors out also the additional bias due to diﬀerent publication rates, thus allowing comparisons among scientists working in diﬀerent ﬁelds. To compute the index for an author, his/her articles are ordered according to cf = c/c0 and this value is plotted versus the reduced rank r/N0 with r being the rank. In analogy with the original deﬁnition by Hirsch, the generalized index is then given by the last value of r/N0 such that the corresponding cf is larger than r/N0. For instance, if an author has published 6 articles with values of cf equal to 4.1, 2.8, 2.2, 1.6, 0.8 and 0.4 respectively, and the value of N0 in his discipline is 2.0, his hf-index is equal to 1.5. This because the third best article has r/N0 = 1.5 < 2.2 = cf, while the fourth has r/N0 = 2.0 > 1.6 = cf. We plan to present the results of the application of this generalized index to practical cases in a forthcoming publication.

V. CONCLUSIONS

In this article we have presented strong empirical evidence that the widely scattered distributions of citations for publications in diﬀerent scientiﬁc disciplines are rescaled upon the same universal curve when the relative indicator cf is used. We have also seen that the universal curve is remarkably stable over the years. The analysis presented here justiﬁes the use of relative indicators to compare in a fair manner the impact of articles across diﬀerent disciplines and years. This may have strong and unexpected implications. For instance, Figure 2 leads to the counterintuitive conclusion that an article in Aerospace Engineering with only 20 citations (cf ≈ 3.54) is more successful than an article in Developmental Biology with 100 citations (cf ≈ 2.58). We stress that this does not imply that the article with larger cf is necessarily more “important” than the other. In an evaluation of importance, other ﬁeld-related factors may play a role: an article with an outstanding value of cf in a very narrow specialistic ﬁeld may be less ”important” (for science in general or for the society) than a publication with smaller cf in a highly competitive discipline with potential implications in many areas.

Since we consider single publications, the smallest possible entities whose scientiﬁc impact can be measured, our results must always be taken into account when tackling other, more complicated tasks, like the evaluation of performance of individuals or research groups. For example, in situations where the simple count of the mean number of citations per publication is deemed to be important, one should compute the average of cf (and not of c) to evaluate impact independently of the scientiﬁc discipline. For what concerns the assessment of single authors’ performance we have deﬁned a generalized hindex [1] that allows a fair comparison across disciplines taking into account also the diﬀerent publication rates.

Our analysis deals with two of the main sources of

bias aﬀecting comparisons of publication citations. It would be interesting to tackle, along the same lines, other potential sources of bias, as for example the number of authors, that is known to correlate with higher number of citations [10]. It is natural to deﬁne a relative indicator, the number of citations per author. Is this normalization the correct one that leads to a universal distribution, for any number of authors?

Finally, from a more theoretical point of view, an interesting goal for future work is to understand the origin of the universality found and how its precise functional form comes about. An attempt to investigate what mechanisms are relevant for understanding citation distributions is in Ref. [29]. Further activity in the same direction would be deﬁnitely interesting.

VI. METHODS

Our empirical analysis is based on data from Thomson Scientiﬁc’s Web of Science (WOS, www.isiknowledge.com) database, where the number of citations is counted as the total number of times an article appears as a reference of a more recent published article. Scientiﬁc journals are divided in 172 categories, from “Acoustics” to “Zoology”. Within a single category a list of journals is provided. We consider articles published in each of these journals to be part of the category. Notice that the division in categories is not mutually exclusive: for example Physical Review D belongs both to the “Astronomy & Astrophysics” and to the “Physics, particles & ﬁelds” categories. For

consistency, among all records contained in the database we consider only those classiﬁed as “article” and “letter”, thus excluding reviews, editorials, comments and other published material likely to have an uncommon citation pattern. A list of the categories considered, with the relevant parameters that characterize them, is reported in Table I. The category ”Multidisciplinary sciences” does not ﬁt perfectly into the universal picture found for other categories, because the distribution of the number of citations is a convolution of the distributions corresponding to the single disciplines represented in the journals. However, if one restricts only to the three most important multidisciplinary journals (Nature, Science, Proc. Natl. Acad. Sci. USA) also this category ﬁts very well into the global universal picture.

Our calculations neglect uncited articles; we have veriﬁed however that their inclusion just produces a small shift in c0, which does not aﬀect the results of our analysis. In the plots of the citation distributions, data have been grouped in bins of exponentially growing size, so that they are equally spaced along a logarithmic axis. For each bin, we count the number of articles with citation count within the bin and divide by the number of all potential values for the citation count that fall in the bin (i.e. all integers). This holds as well for the distribution of the normalized citation count cf, as the latter is just determined by dividing the citation count by the constant c0, so it is a discrete variable just like the original citation count. The resulting ratios obtained for each bin are ﬁnally divided by the total number of articles considered, so that the histograms are normalized to 1.

![image 246](Universality of citation distributions Toward an objective measure of scientific_images/imageFile246.png)

![image 247](Universality of citation distributions Toward an objective measure of scientific_images/imageFile247.png)

![image 248](Universality of citation distributions Toward an objective measure of scientific_images/imageFile248.png)

![image 249](Universality of citation distributions Toward an objective measure of scientific_images/imageFile249.png)

- [1] Hirsch JE (2005) An index to quantify an individual’s scientiﬁc research output. Proc Nat Acad Sci USA 102:16569-16572.
- [2] Egghe L (2006) Theory and practise of the g-index. Scientometrics 69:131-152.
- [3] Hirsch JE (2007) Does the h index have predictive power? Proc. Nat. Acad. Sci. USA 104:19193-19198.
- [4] Evidence Report (2007) http://bookshop.universitiesuk.ac.uk/downloads/bibliometrics.pdf
- [5] Kinney AL (2007) National scientiﬁc facilities and their science impact on nonbiomedical research. Proc Nat Acad Sci USA 104: 17943-17947.
- [6] King DA (2004) The scientiﬁc impact of nations. Nature 430:311-316.
- [7] Brooks TA (1986) Evidence of complex citer motivations. J Am Soc Inf Sci 37:34-36.
- [8] Egghe L, Rousseau R (1990) in Introduction to Informetrics: quantitative methods in library, documentation and information science (Elsevier, Amsterdam).
- [9] Adler R, Ewing J, Taylor P (2008) Citation Statistics. IMU Report http://www.mathunion.org/Publications/Report/CitationStatistics
- [10] Bornmann L, Daniel H-D (2008) What do citation counts measure? A review of studies on citing behavior. J


- Docum 64:45-80.
- [11] Althouse BM, West JD, Bergstrom T, Bergstrom CT

(2008) Diﬀerences in Impact Factor Across Fields and Over Time. arxiv 0804.3116.

- [12] Garﬁeld E (1979) in Citation Indexing. Its Theory and Applications in Science, Technology, and Humanities (Wiley, New York).
- [13] Schubert A, Braun T (1986) Relative indicators and relational charts for comparative-assessment of publication output and citation impact. Scientometrics 9:281-291.
- [14] Schubert A, Braun T (1996) Cross-ﬁeld normalization of scientometric indicators. Scientometrics 36:311-324.
- [15] Vinkler P (1996) Model for quantitative selection of relative scientometric impact indicators. Scientometrics 36:223-236.
- [16] Vinkler P (2003) Relations of relative scientometric indicators. Scientometrics 58:687-694.
- [17] Iglesias JE, Pecharroman C (2007) Scaling the h-index for diﬀerent scientiﬁc ISI ﬁelds. Scientometrics 73:303-320.
- [18] Zitt M, Ramanana-Rahary S, Bassecoulard E (2005) Relativity of citation performance and excellence measures: From cross-ﬁeld to cross-scale eﬀects of ﬁeldnormalisation. Scientometrics 63:373-401.
- [19] Redner S (1998) How popular is your paper? Eur Phys


- J B 4:131-134.
- [20] Naranan S (1971) Power law relations in science bibliography: a self-consistent interpretation. J Docum 27:8397.
- [21] Seglen PO (1992) The skewness of science. J Am Soc Inf Sci 43:628-638.
- [22] Fortunato S, Castellano C (2007) Scaling and Universality in Proportional Elections. Phys Rev Lett 99:138701.
- [23] Plerou V, Nunes Amaral LA, Gopikrishnan P, Meyer M, Stanley HE (1999) Similarities between the growth dynamics of university research and of competitive economic activities. Nature 400:433-437.
- [24] Lundberg J (2007) Lifting the crowncitation z-score. J Informetrics 1:145-154.


- [25] Moed HF, Debruin RE, Vanleeuwen TN (1995) New bibliometric tools for the assessment of national research performance - database description, overview of indicators and ﬁrst applications. Scientometrics 33:381-422.
- [26] Van Raan AF (2004) Sleeping Beauties in Science. Scientometrics 59:461-466.
- [27] Redner S (2005) Citation statistics from 110 years of Physical Review. Phys Today 58:49-54.
- [28] Ball P (2005) Index aims for fair ranking of scientists Nature 436:900-900.
- [29] Van Raan AF (2001) Competition amongst scientists for publication status: toward a model of scientiﬁc publication and citation distributions. Scientometrics 51:347357.


