arXiv:cond-mat/0104162v1[cond-mat.soft]10 Apr 2001

Evolution of the social network of scientiﬁc collaborations

A.L. Baraba´si1,2, H. Jeong1, Z. N´eda1,2,∗, E. Ravasz1, A. Schubert3, T. Vicsek2,4

1Department of Physics, University of Notre Dame, Notre Dame, IN 46556, USA 2 Collegium Budapest, Institute of Advanced Study, Budapest, Hungary 3 Bibliometric Service, Library of the Hungarian Academy of Sciences, Budapest, Hungary 4Department of Biological Physics, E¨otv¨os Lor´and University, Budapest, Hungary (Last revised November 26, 2024)

The co-authorship network of scientists represents a prototype of complex evolving networks. In addition, it oﬀers one of the most extensive database to date on social networks. By mapping the electronic database containing all relevant journals in mathematics and neuro-science for an eightyear period (1991-98), we infer the dynamic and the structural mechanisms that govern the evolution and topology of this complex system. Three complementary approaches allow us to obtain a detailed characterization. First, empirical measurements allow us to uncover the topological measures that characterize the network at a given moment, as well as the time evolution of these quantities. The results indicate that the network is scale-free, and that the network evolution is governed by preferential attachment, aﬀecting both internal and external links. However, in contrast with most model predictions the average degree increases in time, and the node separation decreases. Second, we propose a simple model that captures the network’s time evolution. In some limits the model can be solved analytically, predicting a two-regime scaling in agreement with the measurements. Third, numerical simulations are used to uncover the behavior of quantities that could not be predicted analytically. The combined numerical and analytical results underline the important role internal links play in determining the observed scaling behavior and network topology. The results and methodologies developed in the context of the co-authorship network could be useful for a systematic study of other complex evolving networks as well, such as the world wide web, Internet, or other social networks.

PACS numbers: 89.65.-s, 89.75.-k, 05.10.-a

I. INTRODUCTION

One of the most proliﬁc mathematicians of all time, Paul Erdo˝s has written over 1400 papers with over 500 co-authors. This unparalleled productivity inspired the concept of the Erdo˝s number, which is deﬁned to be one for his many co-authors, two for the co-authors of his co-authors and so on. The tightly interconnected nature of the scientiﬁc community is reﬂected by the conjecture that all publishing mathematicians, as well as many physicists and economists have rather small Erdo˝s numbers [1]. Besides the immediate interest for scientometrics, the co-authorship networks is of general interest for understanding the topological and dynamical laws governing complex networks [2–17], as it represents the largest publicly available computerized social network.

Social networks have been much studied in social sciences [18,19]. A general feature of these studies is that they are restricted to rather small systems, and often view networks as static graphs, whose nodes are individuals and links represent various quantiﬁable social interactions.

In contrast, recent approaches with methodology rooted in statistical physics focus on large networks, searching for universalities both in the topology of the web and in the dynamics governing it’s evolution. These combined theoretical and empirical results have opened

unsuspected directions for research and a wealth of applications in many ﬁelds ranging from computer science to biology [4,12–14,18,20–24]. Three important results seem to crystallize in this respect: First, most networks have the the so called small world property [2,19], which means that the average separation between the nodes is rather small, i.e. one can ﬁnd a short path along the links between most pairs of nodes. Second, real networks display a degree of clustering higher than expected for random networks [2,4]. Finally, it has been found that the degree distribution contains important information about the nature of the network, for many large networks following a scale-free power-law distribution, inspiring the study of scale-free networks [3,5–8,12–14,24].

In addition to uncovering generic properties of real networks, these studies signal the emergence of a new set of modeling tools that considerably enhance our ability to characterize and model complex interactive systems. To illustrate the power of this these advances we choose to investigate in detail the collaboration network of scientists.

Recently Newman has taken an important step towards applying modern network ideas to collaboration networks [10,11]. He studied several large database focusing on several ﬁelds of research over a ﬁve year period, establishing that collaboration networks have all the general ingredients of small world networks: they have a

surprisingly short node-to-node distance and a large clustering coeﬃcient [10], much larger than the one expected from a random Erdo˝s-R´enyi type network of similar size and average connectivity. Furthermore, the degree distribution appears to follow a power law [11].

Our study takes a diﬀerent, but complementary approach to collaboration networks than that followed by Newman. We view collaboration networks as prototype of evolving networks, where the accent is on dynamics and evolution. Indeed, the co-authorship network constantly expands by the addition of new authors to the database, as well as the addition of new internal links representing papers co-authored by authors that were already part of the database. The topological properties of these networks are determined by these dynamical and growth processes. Consequently, in order to understand their topology, we ﬁrst need to understand the dynamical process that determines their evolution. In this aspect Newman’s study focuses on the static properties of the collaboration graph, while our work investigates the dynamical properties of these networks. We show that such dynamical approach can explain many of the static topological features seen in the collaboration graph.

It is important to emphasize that the properties of the co-authorship network are not unique. The WWW is also a complex evolving network, where nodes and links are added (and removed) at a very high rate, the network topology being profoundly determined by these dynamical features [3,20,21,25]. The actor network of Hollywood is very similar to the co-authorship network, because it grows through the addition of new nodes (actors) and new links (movies linking existing actors) [2,4,14]. Similarly, the nontrivial scaling properties of many cellular [23], ecological [24] or business networks are all determined by dynamical processes that contributed to the emergence of these networks. So why single out the collaboration network as a case study? A number of factors have contributed to this choice. First we needed a network for which the dynamical evolution is explicitly available. That is, in addition to a map of the network topology, it is important to know the time at which the nodes and links have been added to the network, crucial for revealing the network dynamics. This requirement reduces the currently available databases to two systems: the actor network, where we can follow the dynamics by recording the year of the movie release, and the collaboration network for which the paper publication year allows us to track the time evolution. Of these two, the co-authorship data is closer to a prototypical evolving network than the Hollywood actor database for the following reasons: in the science collaboration network the co-authorship decision is made entirely by the authors, i.e. decision making is delegated to the level of individual nodes. In contrast, for actors the decision often lies with the casting director, a level higher than the node. While in the long run this diﬀerence is not particularly important, the collaboration network is still closer in spirit to a prototypical evolving network such as social systems or

the WWW.

Our work stands on three pillars. First, we use direct measurements on the available data to uncover the mechanism of network evolution. This implies determining the diﬀerent parameters and uncovering the various competing processes present in the system. Second, building on the mechanisms and parameters revealed by the measurements we construct a model that allows us to investigate the large scale topology the system, as well as its dynamical features. The predictions oﬀered by a continuum theory of the model allow us to explain some of the results that were uncovered by ours, as well Newman’s measurements. The third and ﬁnal step will involve computer simulations of the model, serving several purposes: (i) It allows us to investigate quantities that could not be extracted from the continuum theory; (ii) Veriﬁes the predictions of the continuum theory; (iii) Allows us to understand the nature of the measurements we can perform on the network, explaining some apparent discrepancies between the theoretical and the experimental results.

II. DATABASES: CO-AUTHORSHIP IN MATHEMATICS AND NEURO-SCIENCE

For each research ﬁeld whose practitioners collaborate in publications one can deﬁne a co-authorship network which is a reﬂection of the professional links between the scientists. In this network the nodes are the scientists and two scientists are linked if they wrote a paper together. In order to get information on the topology of a scientiﬁc co-authorship web one needs a complete dataset of the published papers, ideally from the birth of the discipline until today. However, computer databases cover at most the past several decades. Thus any study of this kind needs to be limited to only a recent segment of the database. This will impose unexpected challenges, that need to be addressed, since such limited data availability is a general feature of most networks.

The databases considered by us contain article titles and authors of all relevant journals in the ﬁeld of mathematics (M) and neuro-science (NS), published in the period 1991-98. We have chosen these two ﬁelds for several reasons. A ﬁrst factor was the size of the database: biological sciences or physics are orders of magnitude larger, too large to address their properties with reasonable computing resources. Second, the selected two ﬁelds oﬀer suﬃcient diversity by displaying diﬀerent publishing patterns: in NS collaboration is intense, while mathematics, although there is increasing tendency towards collaboration [26], is still a basically single investigator ﬁeld.

In mathematics our database contains 70,975 diﬀerent authors and 70,901 papers for an interval spanning eight years. In NS the number of diﬀerent authors is 209,293 and the number of published papers is 210,750. A complete statistics for the two considered database is summarized in Fig. 1, where we plot the cumulative number

of papers and authors for the period 1991-98. We consider ”new author” an author who was not present in the database from 1991 up to a given year.

the parameters that are crucial to the understanding of the processes which determine the network topology, offering input for the construction of an appropriate model.

### (a)

0.3

NS

2

0.2

NS

M

Np ()

5x10

0.1

| | | |
|---|---|---|
| | | |


t

1

M

0

1991

1992 1993 1994 1995 1996 1997 1998

t

(b)

0.4

2

NS

NS

0.2

M

N ()

5x10

t

1

M

0 1991 1992 1993 1994 1995 1996 1997 1998

t

FIG. 1. (a) Cumulative number of papers for the M and NS databases in the period 1991-98. The inset shows the number of papers published each year. (b) Cumulative number of authors (nodes) for the M and NS databases in the period 1991-98. The inset shows the number of new authors added each year.

Before proceeding we need to clarify a few methodological issues that aﬀect the data analysis. First, in the database the authors are represented by their surname and initials of ﬁrst and middle name, thus there is a source of error in distinguishing some of them. Two diﬀerent authors with the same initials and surname will appear to be the same node in the database. This error is important mainly for scientists of Chinese and Japanese descent. Second, seldom a given author uses one or two initials in diﬀerent publications, and in such cases he/she will appear as separate nodes. Newman [10] showed that the error introduced by those problems is of the order of a few percents. Our results are also aﬀected by these methodological limitations, but we do not expect that it will have a signiﬁcant impact on our results.

A. Degree distribution follows a power-law

A quantity that has been much studied lately for various networks is the degree distribution, P(k), giving the probability that a randomly selected node has k links. Networks for which P(k) has a power-law tail, are known as scale-free networks [3,13]. On the other hand, classical network models, including the Erdo˝s-R´enyi [27,28] and the Watts and Strogatz [4] models have an exponentially decaying P(k) and are collectively known as exponential networks. The degree distributions of both the M and NS data indicate that collaboration networks are scale-free. The power-law tail is evident from the raw, uniformly binned data (Fig. 2a,b), but the scaling regime is better seen on the plot that uses logarithmic binning, reducing the noise in the tail (Fig. 2c). The cumulative data with logarithmic binning indicates γM = 2.4 and γNS = 2.1 for the two databases [29].

- 100
- 101
- 102
- 103
- 104
- 105


- 100
- 101
- 102
- 103
- 104
- 105


(a) (b)

|1998 1993<br><br>slope −2<br><br>slope −3<br>|
|---|


|1998 1993<br><br>slope −2<br><br>slope −3<br>|
|---|


P(k)

###### M NS

100 101 102 103 k

100 101 102 103

#### (c)

10 0

10−2

NS

P(k)

10−4

M

10−6

10 0 10 1 10 2 10 3

k

FIG. 2. Degree distribution for the (a) M and (b) NS database, showing the data based on the cumulative results up to yeas 1993 (×) and 1998 (•). (c) Degree distribution shown with logarithmic binning computed from the full dataset cumulative up to 1998. The lines correspond do the best ﬁts, and have the slope 2.1 (NS, dotted) and 2.4 (M, dashed).

III. DATA ANALYSIS

In this section we investigate the topology and dynamics of the two databases, M and NS. Our goal is to extract

We will see in the coming sections that the data indicates the existence of two scaling regimes with two different scaling exponents. The combination of these two regimes could easily give the impression of an exponential

cutoﬀ in the P(k) for large k. Further analysis, oﬀered in sections V-VII, indicates that a consideration of two scaling regimes oﬀers a more accurate description.

B. Average separation decreases in time

The ability of two nodes, i and j, to communicate with each other depends on the length of the shortest path, lij, between them. The average of lij over all pairs of nodes is denoted by d = < lij >, and we call it the average separation of the network, characterizing the networks interconnectedness. Large networks can have surprisingly small separation, explaining the origin of the small-world concept [2,19]. Determining the average separation in a large network is a rather time-consuming procedure. Usually sampling a fraction of all nodes and determining their distance from all other points gives reasonable results. The results for the cumulative database are shown in Fig. 3.

20

| | |
|---|---|
| | |
| | |


18

M

16

| | |
|---|---|
| | |
| | |


14

| | |
|---|---|
| | |
| | |


12

| | |
|---|---|
| | |
| | |


d

| | |
|---|---|
| | |
| | |


10

NS

| | |
|---|---|
| | |


8

| | |
|---|---|
| | |


| | |
|---|---|
| | |


| | |
|---|---|
| | |


| | |
|---|---|
| | |


| | |
|---|---|
| | |


6

4

1991 1992 1993 1994 1995 1996 1997 1998

t

FIG. 3. Average separation in the M and NS databases. The separation is computed on the cumulative data up to the indicated year. The error bars indicate the standard deviation of the distances between all pairs of nodes.

The ﬁgure indicates that d decreases with time, which is highly surprising because all network models so far predict that the average separation should increase with system size [20,28]. The decreasing trend observed by us could have two diﬀerent origins. First, it is possible that indeed, the separation does decrease as internal links, i.e. papers written by authors that were previously part of the database, the increase interconnectivity,thus decreasing the diameter. Second, the decreasing diameter could be a consequence of the fact that we have no access to the full database, but only starting from year 1991. As we demonstrate in sect. VI, such incomplete dataset could result in an apparently decreasing separation even if otherwise for the full system the separation increases.

One can note the slow convergence of the diameter and the more connected nature of the NS ﬁeld expressed by a smaller separation. The slow convergence indicates that perhaps even longer time interval is needed to reach the

asymptotic limit, in which diﬀerent relevant quantities take up a stationary value. The smaller separation for the NS ﬁeld is expected, since mathematicians tend to work in smaller groups and write papers with fewer coauthors.

C. Clustering coeﬃcient decays with time

An important phenomena characterizing the deviation of real networks from the completely random ER model is clustering. The clustering coeﬃcient, a quantitative measure of this phenomena, C, can be deﬁned as follows [4]: pick a node, i that has links to ki other nodes in the system. If these ki nodes form a fully connected clique, there are ki(ki − 1)/2 links between them, but in reality we ﬁnd much fever. Let us denote by Ni the number of links that connect the selected ki nodes to each other. The clustering coeﬃcient for node i is then Ci = 2Ni/ki(ki − 1). The clustering coeﬃcient for the whole network is obtained by averaging Ci over all nodes in the system, i.e. C = < Ci >i. In simple terms the clustering coeﬃcient of a node in the co-authorship network tells us how much a node’s collaborators are willing to collaborate with each other, and it represents the probability that two of it’s collaborators wrote a paper together. The clustering coeﬃcient for the cumulative network as a function of time is shown in Fig. 4.

1

0.9

NS

0.8

C

0.7

M

0.6

0.5 1991 1992 1993 1994 1995 1996 1997 1998

t

FIG. 4. Clustering coeﬃcient of the M and NS database, determined for the cumulative data up to the year indicated on the t axis.

The results, in agreement with the separation measurements, suggest a stronger interconnectedness for the NS compared with M, and a slow convergence in time to an asymptotic value.

D. Relative size of the largest cluster increases

It is important to realize that the collaboration network is fragmented in many clusters. There are several reasons for this. First, in every ﬁeld there are scientists

that do not collaborate at all, that is they are the only authors of all papers on which their name appears. This is more frequent in mathematics, which despite an increasing tendency toward collaboration [26], is still more fragmented than physics or neural science. Second, and most important, the database contains papers published only after 1990. Thus there is a possibility that two authors co-authored a paper before 1990, but in our database they appear as disconnected.

If we look only at a single year, we see many isolated clusters of authors. The cumulative dataset containing several years develops a giant cluster, that contains a large fraction of the authors. To investigate the emergence of this giant connected component we measured the relative size of the largest cluster, r, giving the ratio between the number of nodes in the largest cluster and the total number of nodes in the system. A cluster is deﬁned as a subset of nodes interconnected by links. Results from our cumulative co-authorship networks are presented in Fig. 5. As expected, in M the fraction of clustered researchers is considerably smaller than in NS.

1

0.8

NS

0.6

r

M

0.4

0.2

0 1991 1992 1993 1994 1995 1996 1997 1998

t

FIG. 5. Relative size of the largest cluster for the M and NS database. Results are computed on the cumulative data up to the given year.

The continuous increase in r may appear as the scenario commonly described as percolation [30] or the much studied emergence of the giant component in random networks [28]. However, the process leading to this giant cluster is fundamentally diﬀerent from these much studied phenomena. In most research ﬁelds, apart from a very small fraction of authors that do not collaborate, all authors belong to a single giant cluster from the very early stages of the ﬁeld. That is, the system is almost fully connected from the very ﬁrst moment. The only reason why the giant cluster in our case grows so dramatically in the ﬁrst several years is that we are missing the information on the network topology before 1991. A good example is the actor network, where the huge majority of the actors are part of the large cluster at any stage of the network, starting from early 1900’s until today. However, if we would start recording collaborations only after 1990 for example, the data would indicate, incorrectly, that many actors are disconnected. The increasing r indicates only

the fact that we are reconstructing the already existing giant cluster, and it is only a partial measure of it’s emergence.

Finally, the fast convergence of the NS cluster size to an approximately stationary value around 0.9 indicates that after 1994 the network reached a roughly stationary topology, i.e. the basic alliances are uncovered. This does not seems to be the case for M, where after ten years r still increases, perhaps due to smaller publication and collaboration rate in the ﬁeld.

E. Average degree increases

With time the number of nodes in our co-authorship network increases due to arrival of new authors. The total number of links also increases through the connections made by new authors with old ones and by new connections between old authors. A quantity characterizing the network’s interconnectedness is the average degree < k >, giving the average number of links per author. The time dependence of < k > for the cumulative network is shown in Fig. 6, indicating an approximately linear increase of < k > with time.

12

## NS

10

8

<k>

6

M

4

2

0 1991 1992 1993 1994 1995 1996 1997 1998

t

FIG. 6. Average number of links per node (< k >) for the M and NS database. Results are computed on the cumulative data up to the given year.

This is a rather important deviation from the majority of currently existing evolving network models, that assume a constant < k > as the network expands. As expected, the average degree for M is much smaller than for NS.

F. Node selection is governed by preferential attachment

Classical network models assume complete randomness, i.e. the nodes are connected to each other independent of the the number of links they already had [2,27,28]. The discovery of the power-law connectivity distribution required the development of new modeling

paradigms. A much used assumption is that in scalefree networks nodes link with higher probability to those nodes that already have a larger number of links, a phenomena labeled as preferential attachment [3,13]. Implicitly or explicitly, preferential attachment is part of all network models that aim to explain the emergence of the inhomogeneous network structure and power law connectivity distribution [5–8]. The availability of dynamic data on the network development allows us to investigate its presence in the co-authorship network. For this network preferential attachment appears at two levels, that we discuss separately.

(i) New nodes: For a new author, that appears for the ﬁrst time on a publication, preferential attachment has a simple meaning: it is more likely that the ﬁrst paper will be co-authored with somebody that already has a large number of co-authors (links) that with somebody less connected. As a result ”old” authors with more links will increase their number of co-authors at a higher rate than those with fever links. To investigate this process in quantitative terms we determined the probability that an old author with connectivity k is selected by a new author for co-authorship. This probability deﬁnes the Π(k) distribution function. Calling ”old authors” those present up to the last year, and ”new author” those who were added during the last year, we determine the change in the number of links, ∆k, for an old author that at the beginning of the last year had k links. Plotting ∆k as a function of k gives the function Π(k), describing the nature of preferential attachment. Since the measurements are limited to only a ﬁnite (∆T = 1 year) interval, we improve the statistics by plotting the integral of Π(k):

κ(k) =

k

Π(k′)dk′. (1)

1

If preferential attachment is absent, Π(k) should be independent of k, as each node grows independently of it’s degree, and κ(k) is expected to be linear. As Fig. 7 shows, we ﬁnd that κ(k) is nonlinear, increasing as κ(k) ∼ kν+1, where the best ﬁt gives ν ≃ 0.8 for M and ν ≃ 0.75 for NS. This implies that Π(k) ∼ kν, where ν is diﬀerent from 1 [31]. As simulations have shown, such nonlinear dependence generates deviations from a power law P(k) [31]. This was supported by analytical calculations [8], that demonstrated that the degree distribution follows a power law only for ν = 1. The consequence of this nonlinearity will be discussed below.

- 100
- 101
- 102
- 103


106

|slope 1 1999 1997 1995<br><br>| |
|---|
<br><br>|
|---|


|slope 1 1998 1996 1994<br><br>| |
|---|
<br><br>|
|---|


| | |
|---|---|
| | |
| | |


104

102

∆k

100

10−1

M NS

10−2

10−2

100 101 102 103 k

100 101 102 103 104

FIG. 7. Cumulated preferential attachment (κ(k)) of incoming new nodes for the M and NS database. Results computed by considering the new nodes coming in the speciﬁed year, and the network formed by nodes already present up to this year. In the absence of preferential attachment κ(k) ∼ k, shown as continuous line on the ﬁgures.

(ii) Internal links: A large number of new links appear between old nodes as the network evolves, representing papers written by authors that were part of the network, but did not collaborate before. Such internal links are known to eﬀect both the topology and dynamics of the network [5]. These internal links are also subject to preferential attachment. We studied the probability Π(k1,k2) that an old author with k1 links forms a new link with another old author with k2 links. The Π(k1,k2) probability map can be calculated by dividing N(k1,k2), the number of new links between authors with k1 and k2 links, with the D(k1,k2), number of pairs of nodes with connectivities k1 and k2 present in the system:

N(k1,k2) D(k1,k2)

Π(k1,k2) =

. (2)

![image 1](Evolution of the social network of scientific collaborations_images/imageFile1.png)

The three dimensional plot of Π(k1,k2) is shown in Fig.8, the overall behavior indicating preferential attachment:

Π(k1,k2) increases with as either k1 or k2’s increase.

M NS

0

10

0 −2

10 10 10

10 10 10

−2

−4

−4

−6

−6

10

1000 100

10000

1000

1 10

1

100 10

10

k2 k1

10

k

100

100

2

1000

k

1

10000 1

1000

1

FIG. 8. Internal preferential attachment for the M and NS database, 3D plots: ∆k as a function of k1 and k2. Results computed on the cumulative data in the last considered year.

A natural hypothesis is to assume that Π(k1,k2) factorizes into the product k1k2. As Fig. 9 shows, we indeed ﬁnd that

κ(k1k2) =

k1k2

Π(k1′ k2′ )d(k1′ k2′ ) (3)

1

can be well approximated with a slope 2 as a function of k1k2, indicating that for internal links the preferential attachment is linear in the degree.

106

10000

|slope 1 1999<br><br>|
|---|


|slope 1 1998<br><br>|
|---|


104

100

###### M NS

|κ(kk)∆k12|
|---|


102

κ(kk)12

∆k

- 0
- 1


100

10−2

10−4

0

102 103 104 105 106 107

10 100 1000 10000 100000 k1k2

FIG. 9. Cumulated internal preferential attachment (κ(k)) for the M and NS database, scaling as a function of the k1k2 product. Results computed on the cumulative data in the last considered year. The straight lines have slope 1, expected for κ(k1k2) if there would be no preferential attachment.

IV. MODELING THE WEB OF SCIENCE

In this section we use the obtained numerical results to construct a simple model for the evolution of the coauthorship network. It is important to emphasize that the purpose of the model is to capture the main mechanisms that aﬀect the evolution and the scaling of the network, and not to incorporate every numerical detail of the measured web. However, the advantage of the proposed model is its ﬂexibility: features, neglected here, can be incorporated into the current modeling framework.

We denote by ki(t) the number of links node i has at time t; by T(t) and N(t) the total number of links and total number of nodes at time t, respectively. We assume that all nodes present in the system are active, i.e. they can author further papers. This is a reasonable assumption as the time-span over which data is available to us is shorter than the professional lifetime of a scientist. In agreement with Fig. 1, we consider that new researchers join the ﬁeld at a constant rate, leading to

N(t) = βt. (4)

The average number of links per node in the system at time t is thus given by:

T(t) N(t)

< k > =

. (5)

![image 2](Evolution of the social network of scientific collaborations_images/imageFile2.png)

Fig. 9 suggests, that the probability to create a new internal link between two existing nodes is proportional with the product of their connectivities. Consequently, denoting by a the number of newly created internal links per

node in unit time, we write the probability that between node i and j a new internal link is created as

kikj

Πij =

N(t)a, (6)

![image 3](Evolution of the social network of scientific collaborations_images/imageFile3.png)

′ s,m kskm

where the prime sign indicates that the summation is done for s = m values.

The measurements also indicated (Fig. 7) that new nodes link to the existing nodes with preferential attachment, Π(k) follows kν with ν ≃ 0.75 − 0.8. Aiming to obtain an analytically solvable model, at this point we neglect this nonlinearity and we approximate Π(k) with a linear k dependence. The eﬀect of the nonlinearities will be discussed in sect. VII. Thus, if node i has ki links, the probability that an incoming node will connect to it is given by

ki j kj

Πi = b

, (7)

![image 4](Evolution of the social network of scientific collaborations_images/imageFile4.png)

where b is the average number of new links that an incoming node creates.

We have thus formulated the dynamical rules that govern our evolving network model, capturing the basic mechanism governing the evolution of the co-authorship network:

- 1. Nodes join the network at a constant rate.
- 2. Incoming nodes link to the already present nodes following preferential attachment (7).
- 3. Nodes already present in the network form new internal links following preferential attachment (6).
- 4. We neglect the aging of nodes, and assume that all nodes and links present in the system are active, able to initiate and receive new links.


In the model we assume that the number of authors on a paper is constant. In reality m is a stochastic variable, as the number of authors varies from paper to paper. However, for the scale-free model the exponent γ is known to be independent of m, thus making m a stochastic variable is not expected to change the scaling behavior.

V. CONTINUUM THEORY

Taking into account that new links join the system with a constant rate, β, the continuum equation for the evolution of the number of links node i has can be written as:

dki dt

=

![image 5](Evolution of the social network of scientific collaborations_images/imageFile5.png)

bβki j kj

+ N(t)a

![image 6](Evolution of the social network of scientific collaborations_images/imageFile6.png)

j

′ kikj ′ s,m kskm

. (8)

![image 7](Evolution of the social network of scientific collaborations_images/imageFile7.png)

The ﬁrst term on the right hand side describes the contribution due to new nodes (7) and the second term gives

the new links created with already existing nodes (6). The total number of links at time t can be computed taking into account the internal and external preferential attachment rules:

i

ki = T(t) =

t

2 [N(t′)a + bβ]dt′ = tβ(at + 2b).

0

(9)

Consequently the average number of links per node increases linearly in time,

< k > = at + 2b, (10)

in agreement with our measurements on the collaboration network (Fig. 6). The master equation (8) can be solved if we approximate the double sum in the second term. Taking into account that we are interested in the asymptotic limit where the total number of nodes is large relative to the connectivity of the nodes, we can write:

′

kskm =

s,m

s

ks

m

km −

m

km2 ≈

i

ki

2

. (11)

We have used here the fact that T(t)2 depends on N2, while i ki2 depends only linearly on N (we investigate the N → ∞ limit). Using (11) equation (8) now becomes:

dki dt

bki t(at + 2b)

kia at + 2b

=

+

. (12)

![image 8](Evolution of the social network of scientific collaborations_images/imageFile8.png)

![image 9](Evolution of the social network of scientific collaborations_images/imageFile9.png)

![image 10](Evolution of the social network of scientific collaborations_images/imageFile10.png)

Introducing the notation α = a/b, we obtain:

- tα + 1

![image 11](Evolution of the social network of scientific collaborations_images/imageFile11.png)

- tα + 2


ki t

dki dt

=

. (13)

![image 12](Evolution of the social network of scientific collaborations_images/imageFile12.png)

![image 13](Evolution of the social network of scientific collaborations_images/imageFile13.png)

This diﬀerential equation is separable, the general solution having the form

√

t√2 + αt. (14)

![image 14](Evolution of the social network of scientific collaborations_images/imageFile14.png)

![image 15](Evolution of the social network of scientific collaborations_images/imageFile15.png)

ki(t) = Ci

The Ci integration constant can be determined from the initial conditions for node i. Since node i joins the system

at time ti, we have ki(ti) = b, leading to

ki(t) = b

![image 16](Evolution of the social network of scientific collaborations_images/imageFile16.png)

t ti

![image 17](Evolution of the social network of scientific collaborations_images/imageFile17.png)

![image 18](Evolution of the social network of scientific collaborations_images/imageFile18.png)

2 + αt 2 + αti

. (15)

![image 19](Evolution of the social network of scientific collaborations_images/imageFile19.png)

This implies that for large times (t → ∞) the connectivity of the node scales linearly with time, i.e. k(t) ∼ t.

A quantity of major interest is the degree distribution, P(k). The nodes join the system randomly at a constant rate, which implies that the ti values are uniformly distributed in time between 0 and t. The distribution function for the ti in the [0,t] interval is simply ρ(t) = 1/t. Using (15), P(k) can be obtained after determining the ti(ki) dependence from (15), giving

dti dki k

P(k) = −ρ(t)

![image 20](Evolution of the social network of scientific collaborations_images/imageFile20.png)

= b2(2/α + t)

= (16)

1 k2

1 k2 + b2t(2 + αt)

. (17)

![image 21](Evolution of the social network of scientific collaborations_images/imageFile21.png)

![image 22](Evolution of the social network of scientific collaborations_images/imageFile22.png)

![image 23](Evolution of the social network of scientific collaborations_images/imageFile23.png)

An immediate consequence of this result is that the connectivity distribution depends both on the observation time t and on the range of k values we explore. In the asymptotic limit t → ∞ we obtain

1 k2

P(k) ∝

, (18)

![image 24](Evolution of the social network of scientific collaborations_images/imageFile24.png)

predicting a scale-free behavior with exponent γ = 2. At short times, however, the exponent is diﬀerent, the network exhibiting a scale-free behavior similar to the scale-free model [3,13]:

P(k) ∝

1 k3

. (19)

![image 25](Evolution of the social network of scientific collaborations_images/imageFile25.png)

Thus the model predicts that the degree distribution of the collaboration network displays a crossover between two scaling regimes. In general, scaling is controlled by the time dependent crossover connectivity, given by

![image 26](Evolution of the social network of scientific collaborations_images/imageFile26.png)

kc = b2t(2 + αt). (20)

For k ≪ kc the degree distribution scales with an exponent γ = 2, while for k ≫ kc the degree distribution scales with γ = 3. The crossover connectivity, kc, increases linearly in time for t ≫ 2/α, which implies that in the asymptotic limit (t → ∞) only the γ = 2 exponent is observable.

Note that this result predicts that the degree distribution has two scaling regimes, one with γ = 2 for small k, followed by a crossover to γ = 3 for large k. This crossover towards a larger exponent can be easily approximated with an exponential cutoﬀ, which is why we believe that in [10] the power law with an exponential cutoﬀ gave a reasonable ﬁt. However, as [11] and our results show, for datasets with better statistics the scaling regimes can be distinguished. Indeed, the crossover is visible in Fig. 2 as well, in particular for the degree distribution of NS. The degree distribution taken in 1993 has a clear γ = 3 tail, as for the studied short time-frame (3 years) kc is expected to be low. This γ = 3 tail all but disappears, however, in 1998, being replaced with a γ = 2 exponent, as predicted by (18) for the limit t → ∞. The M database shows similar characteristics, albeit the crossover is masked by a higher spread in the data point thanks to the weaker statistics.

Plotting instead of P(k) two diﬀerently cumulated values, the γ = 2 and γ = 3 scaling regimes are more evident. Let us denote by F(k) the primitive function of P(k), deﬁning:

Φ(k) = −F(1) −

k

P(k′)dk′. (21)

1

Φ(k) can be determined numerically by integrating P(k) between 1 and k and subtracting the constant at which the integral converges. For small k the function Φ(k) should scale as

Φ(k) ∝ k−1, (22)

assuming that P(k) scales as given by (18). As Fig. 10a shows, we indeed ﬁnd that for large t (1998) the measured Φ(k) function converges to a k−1 behavior, which is less apparent on the small t curves (1993 and 1995).

To investigate the large k behavior of P(k) we measured the τ(k) function deﬁned as:

τ(k) =

∞

P(k′)dk′, (23)

k

which captures the scaling of the tail. According to (19) for large k and small t one should observe

τ(k) ∝ k−2. (24)

As Fig. 10 shows, we indeed ﬁnd that for NS for small t (1993) the large k scaling follows the prediction (23), and, as predicted, the scaling increasingly deviates from it as time increases.

- 102
- 103
- 104
- 105
- 106


a. b.

105

Φ(k)

τ(k)

103

|slope −1<br><br>1998 1995 1993<br><br>| |
|---|
<br><br>|
|---|


|slope −2<br><br>1998 1995 1993<br><br>| |
|---|
<br><br>|
|---|


- 100 101 102 k

- 101


100 101 k 102 103

FIG. 10. Scaling of Φ(k) (a) and of τ(k) (b) for the NS database, demonstrating the trends in the small and large k behavior of the degree distribution (see text).

VI. MONTE CARLO SIMULATIONS

While the continuum theory discussed in the previous section predicts the connectivity distribution in agreement with the empirical data, there are other quantities, such as the node separation and clustering coeﬃcient, that cannot be calculated using this method at this point. To investigate the behavior of these measures of the network topology next we study the model proposed in Sect. IV using Monte Carlo simulations.

Due to memory and computing time limitations we investigated relatively small networks, with total number of nodes N < 4000. While these networks are considerably smaller than the real networks, their scaling and topological features should be representative. In order to form a reasonable number of internal links, we

increased the parameter a in Eq. (6). For comparison purposes we note that in the real system we have aM = 0.31/year ≃ 10−4/simulation step and aNS = 0.98/year ≃ 3.684 · 10−5/simulation step, numbers that can be derived from the data shown in Fig. 6 and Fig. 1b.

The advantage of the modeling eﬀorts, including the Monte Carlo simulations, is that they reproduce the network dynamics from the very ﬁrst node. In contrast, the database we studied records nodes and links only after 1991, when much of the networks structure was already in place. By collecting data over several years we gradually discovered the underlying structure. We expect that after a quite long measurement time the structure revealed by the collected data will be statistically indistinguishable from the full collaboration network. However, the dynamics we measure during this process for the relevant quantities (diameter, average connectivity, clustering coeﬃcient) might diﬀer from those characterizing the full network, since all of them are computed on the incomplete network (revealed by the available data). However, Monte Carlo simulations allow us to investigate the effect of the data incompleteness on the relevant network measures.

We investigated the time dependence of the average connectivity, the diameter and the clustering coeﬃcient, using the parameters Nmax = 1000, a = 0.001, β = 1 and b = 2. In order to increase the statistics, the results were averaged over 10 independent conﬁgurations.

Average degree: As Fig. 11 indicates, asymptotically the average connectivity increases linearly, in agreement with both our measurements (see Fig. 6) and the continuum theory (see Eq. (5)).

- 3

- 3.5
- 4


- 4.5
- 5


###### <k>

0 200 400 600 800 1000

N

FIG. 11. Computer simulated dynamics of the average connectivity in the proposed model. (Nmax = 1000, a = 0.001, β = 1 and b = 2)

Average separation: The empirical results indicated (see Fig. 3) that the average separation decreases with time for both databases. In contrast, our simulations show a monotonically increasing d, in apparent disagreement with the real system.

15

|real diameter<br><br>apparent diameter|
|---|


10

##### d

5

0

0 200 400 600 800 1000

N

FIG. 12. Computer simulated dynamics for the real and apparently measured diameter value. (Nmax = 1000, a = 0.001, β = 1, b = 2 and Ns = 200)

Note that an increasing diameter agrees with measurements done on other models, including scale-free and exponential networks, that all predict an approximately logarithmic increase with the number of nodes, d ∝ ln(N) [28,32]. This contradiction between the models and our empirical data is rooted in the incomplete data we have for the ﬁrst years of our measurements. To show this we perform the following simulation. We construct a network of N = 1000 nodes. However, we will record the apparent diameter of the network made of nodes that have been added only after a predeﬁned time, mimicking the fact that the data available for us gives d only for publications after 1991. We ﬁnd that the separation of this incomplete network has a decreasing tendency, slowly converging to the real value (Fig. 12), in agreement with the decrease observed in the empirical measurements (Fig. 3). This result underlies the importance of simulations in understanding the dynamics of complex networks, and resolves the conﬂict between the simulation and the empirical data. It also indicates that most likely the diameter of the M and NS database does increase in time, but such increase can be observed only if much longer time intervals will be available for study.

- 0

- 0.5
- 1


- 1.5
- 2


- 5
- 6
- 7
- 8


a=0 a=0.00025 a=0.00050 a=0.00075

lnNmin

| | | |
|---|---|---|
| | | |


| | | |
|---|---|---|
| | | |


|y=−1.887331 − 1.144328 *xa=0.00200|
|---|


−9 −8 −7 −6 ln a

C

0 1000 2000 3000 N

FIG. 13. Clustering coeﬃcient for diﬀerent values of the a parameter as a function of the system size N. (Nmax = 1000, β = 1 and b = 2, values of a are 0 (•), 0.00025 (+), 0.0005 (△), 0.00075 (∗), 0.002 (▽).) The inset shows the scaling of the Nmin value as a function of the a parameter. (Nmax = 1000, β = 1 and b = 2, the line shows a ﬁt ln Nmin = −1.887 − 1.144 · ln a.)

Clustering coeﬃcient. The clustering coeﬃcient predicted by our simulations is shown on Fig. 13. As the ﬁgure indicates, C depends strongly on the value of the parameter a. For a = 0 we have essentially the scalefree model [3] and the clustering coeﬃcient has a monotonically decreasing tendency. For a > 0 however, the clustering coeﬃcient decreases at the beginning and after reaching a minimum at Nmin changes its course, asymptotically increasing with time. Thus, for all a > 0, we expect that in the asymptotic limit the clustering coefﬁcient should increase, in agreement with our measurements on the collaboration network (see Fig. 4). The Nmin position where the clustering coeﬃcient has a minimum scales as power of the a parameter, as shown as the inset in Fig. 13.

We conclude thus that the decreasing C observed for our database, shown in Fig. 4, does not represent the asymptotic behavior. The observed behavior also indicates that one should view the values for C reported in the literature, and measured for ﬁnite time-frames (maximum 5 years) with caution, as they might not represent asymptotic values.

Degree distribution: The simulations provide P(k) as well, allowing us to check the validity of the predictions of the continuum theory. Although the considered system sizes are rather small (Nmax = 3500) compared to the N → ∞ approximation used in the analytical calculation and the NM = 70,975, NNS = 209,750 for the empirical data, the behavior of P(k), shown in Fig. 14 agrees with our continuum model and measurements. For small k we observe the γ = 2 scaling, while for large k P(k) converges to the predicted γ = 3 exponent.

0

−2

−4

ln P(k)

|N=3500 N=1400 N=700<br><br>slope −3 slope −2<br><br>|
|---|


−6

−8

−10

0 1 2 3 4 5 ln k

FIG. 14. Connectivity distributions as predicted by numerical simulation for diﬀerent stages of evolution of the network (a = 0.001, β = 1 and b = 2).

VII. NONLINEAR EFFECTS

An issue that remained unresolved up to this pont concerns the eﬀect of the nonlinear preferential attachment. We have seen in sect. IIIF that for the incoming links we have

kiν j kjν

Πi = b

, (25)

![image 27](Evolution of the social network of scientific collaborations_images/imageFile27.png)

with ν ≈ 0.8. On the other hand, for such preferential attachment Krapivsky et al have shown that the degree distribution follows a stretched exponential, i.e. the power law is absent [8]. This would indicate that P(k) for the co-authorship network should follow a stretched exponential, which disagrees with our and Newman’s ﬁndings (we have explicitly checked that a stretched exponential is not a good ﬁt for our data). What could then override the known eﬀect of the ν < 1 nonlinear behavior? Next we propose a possible explanation: the linearity of the internal preferential attachment can restore the power law nature of P(k).

For non integer ν values the diﬀerential equation (8) governing the evolution of the connectivity is not analytically solvable. However, in the extreme case ν = 0 (no preferential attachment for new nodes) the equation is again analytically tractable. Equation (8) in this case has the form

dki dt

=

![image 28](Evolution of the social network of scientific collaborations_images/imageFile28.png)

bβ N(t)

+ N(t)a

![image 29](Evolution of the social network of scientific collaborations_images/imageFile29.png)

j

kikj s,m kskm

. (26)

![image 30](Evolution of the social network of scientific collaborations_images/imageFile30.png)

Using N(t) = βt and <k> = at + 2b, which are valid in this case as well, following the steps described in sect. V, we obtain the diﬀerential equation:

dki dt

b t

a ki at + 2b

=

+

. (27)

![image 31](Evolution of the social network of scientific collaborations_images/imageFile31.png)

![image 32](Evolution of the social network of scientific collaborations_images/imageFile32.png)

![image 33](Evolution of the social network of scientific collaborations_images/imageFile33.png)

The general solution of this equation has the form:

ki(t) = (2b + at)Ci +

- 1

![image 34](Evolution of the social network of scientific collaborations_images/imageFile34.png)

- 2


(2b + at)log

t 2b + at

![image 35](Evolution of the social network of scientific collaborations_images/imageFile35.png)

, (28)

where Ci is an integration constant which can be determined using the ki(ti) = b initial condition. We thus obtain:

2b + at 2b + ati

ki(t) = b

+

![image 36](Evolution of the social network of scientific collaborations_images/imageFile36.png)

- 1

![image 37](Evolution of the social network of scientific collaborations_images/imageFile37.png)

- 2


(2b + at)log

t(2b + ati) ti(2b + at)

![image 38](Evolution of the social network of scientific collaborations_images/imageFile38.png)

(29)

The degree distribution cannot be determined analytically, since the ti(ki) function is not analytical. However, taking the {t,ti} → ∞ limit, i.e. focusing on the network’s long time evolution we obtain

ki(t) ≈ b

t ti

, (30)

![image 39](Evolution of the social network of scientific collaborations_images/imageFile39.png)

which again predicts a power-law degree distribution:

P(k) ∝

1 k2

. (31)

![image 40](Evolution of the social network of scientific collaborations_images/imageFile40.png)

Consequently, we obtain that in the asymptotic limit for ν = 0 the scale-free degree distribution has the same tail as we obtained for ν = 1. This result suggests that the linearity in the internal preferential attachment determines the asymptotic form of the degree distribution. The real exponent ν = 0.8 is between the two asymptotically solvable cases ν = 0 and ν = 1, but, based on the limiting behavior of the two extremes we expect that independently of the value of 0 ≤ ν ≤ 1, in the asymptotic limit the degree distribution should converge to a power-law with γ = 2. On the other hand, we expect that the nonlinear ν = 1 behavior would have a considerable eﬀect on the non-asymptotic behavior, which is not accessible analytically at this point.

To test further the potential eﬀect of the nonlinearities, we have simulated the model discussed in sect. VI with ν = 0.75, otherwise all parameters being unchanged. We show on Fig. 15 the degree distribution for the linear (ν = 1) and the nonlinear (ν = 0.75) case.

|linear preferential attachment<br><br>nonlinear preferential attachment<br><br>slope −3|
|---|


−3

ln P(k)

−8

−13

0.5 1.5 2.5 3.5 4.5 5.5 ln k

FIG. 15. Connectivity distribution generated by the numerical simulations for linear (ν = 1) and nonlinear (ν = 0.75) preferential attachment (Nmax = 3500, a = 0.0005, β = 1 and b = 2).

As one can see, the ν = 1 and ν = 0.75 case can be hardly distinguished. This could have two origins. First, the simulations are limited to t = 3500 simulation steps, due to the discussed running time limitations. Thus we are hardly in the asymptotic regime. On the other hand, the agreement indicates that the nonlinear eﬀect has hardly distinguishable eﬀect on P(k), again the internal attachment dominating the system behavior.

In summary, the domination of the internal attachment aﬀects are expected to be even more dominant for the real network. Indeed, in the collaboration network the fraction of the links created as internal links is much higher than those created by the incoming nodes, as an author qualiﬁes for a new incoming link only on his ﬁrst paper. Most scientists contribute for a considerable time to the same ﬁled, publishing numerous subsequent papers, and these later links will all appear as internal links. Thus typically the number of internal links is much higher than the number of new links, the network’s topology is much more driven by the internal links then by the external ones. This is one possible reason why the eﬀect of the nonlinear behavior, while clearly present, cannot be detected in the functional form of P(k).

VIII. DISCUSSION

In the last two years we witnessed considerable advances in addressing the topology and the dynamics of complex networks. Along this road a number of quantities have been measured and calculated, aiming to characterize the network topology. However most of these studies are fragmented, focusing on one or a few characteristics of the network at a time. Here we presented a detailed study of a network of high interest to the scientiﬁc community, the collaboration network of scientists, which also represents a prototype example of a complex evolving network. This study allows us to investigate to which degree can we use various known measures to characterize a given network. A ﬁrst and important result of our investigation is that we need to be careful at distinguishing between the asymptotic and the intermediate behavior. In particular, most quantities used to characterize the network are time dependent. For example, the diameter, the clustering coeﬃcient, as well as the average degree of the nodes are often used as basic time independent network characteristics. Our empirical results show that many of these key quantities are time dependent, without a tendency to saturate within the available time-frame. Thus their value at a given moment tells us little about the network. They can be used, however, at any moment, to show that the network has small world properties, i.e. it has a small average separation, and a clustering coeﬃcient that is larger than one expected for a random network.

A quantity that is often believed to oﬀer a stationary measure of the network is the degree distribution. Our

empirical data, together with the analytic solution of the model shows that this is true only asymptotically for the co-authorship network: we uncover a crossover behavior between two diﬀerent scaling regimes. We tend to believe that the model’s predictions are not limited to the collaboration network: as on the WWW and for the actor collaboration network similar basic processes take place, chances are that similar crossovers could appear there as well.

A third important conclusion of the study regards the understanding that the measurements done on incomplete databases could oﬀer trends that are opposite compared to that seen in the full system. An example is the node separation: we ﬁnd that the empirically observed decreasing tendency is an artifact of the incomplete data. However, our simulations show that one can, with careful modeling, uncover such inconsistencies. But this also oﬀers an important warning: for any network, before attempting to model it, we need to fully understand the limitations of the data collection process, and test their eﬀect on the quantities of interest for us.

The model presented here represents only the starting point toward a complete modeling of collaborations in science. As we discussed thorough the paper, we have made several important approximations, sacriﬁcing certain known network features for an analytical solution. For example, we neglected in our modeling eﬀort the potential eﬀect of aging [6,12], reﬂecting the fact that scientists retire and stop publishing papers. In the long run such aging eﬀects will, undoubtedly, introduce exponential cutoﬀs in P(k), as there are inherent limits on how many papers a researcher can write. Those eﬀects, however, are not visible in our datasets. There are several potential reasons for this. Probably the most important is that even the eight years available to us for study is much shorter than the professional life of a scientist. Such aging induced cutoﬀs are expected to be visible only when time-frames of length of several time the scientist’s professional life are studied. Data availability so far does not permit such studies.

A second simpliﬁcation is that we assumed that each paper has exactly m authors. That is far from being so, as the numbers of co-authors varies greatly between papers. However, it is hard to imagine that the inclusion of a stochastic component in m would fundamentally aﬀect our results. It is clear that such stochastic component will not aﬀect P(k), and we feel that the eﬀect on d or C is also negligible, but we lack at this point results to support this latter claim.

A surprising result of our study is the power law character of P(k), despite the fact that Π(k) is nonlinear. We have shown that the existence of a linear internal attachment rule is able to restore the power law P(k). Considering the fact that the largest fraction of links appear as internal links, compared with links created by new authors, it is fair to expect that the scaling determined by this internal linking process will dominate. The fact that for the two limits of the internal linking exponents,

ν = 0 and ν = 1, we obtained power law P(k) despite the nonlinear external Π(k), suggests that such power law might appear for nonlinear, ν = 0,1 internal Π(k) as well. Solving this problem is a formidable challenge, but it is perhaps worth the eﬀort.

Finally, a more detailed modeling of the co-authorship network would involve the construction of bipartite graphs [33], in which we directly simulate the publishing of papers by several co-authors, which are all connected to each other. In such a model the basic unit is a paper, that involves several ”old” and ”new” authors. In such a framework one can simultaneously study the evolution of the co-authorship network (in which nodes are scientists linked by joint publications) and the publication network (in which nodes are papers linked by joint authors). One can imagine that coupled continuum equations could be formulated for such bipartite network as well, which would eventually predict the network’s dynamics and topology. Undoubtedly including such detail in the modeling eﬀort would increase the ﬁdelity of the model. While challenging, following such path is beyond our goals here.

In summary, the modeling eﬀorts presented here are only the starting point for a systematic investigation of the evolution of social networks. It is important to note that such modeling is open ended: more details can be incorporated, that could undoubtedly improve the agreement between the empirical data and theory. And such improvements might not be in vain: they could point towards a better understanding of the evolution of not only the co-authorship graph, but complex networks in general.

IX. ACKNOWLEDGMENTS

This work has been done during a collaboration at the Collegium Budapest Institute of Advanced Study, Hungary. We gratefully acknowledge the inspiring and professionally motivating atmosphere, and the fellowships oﬀered by Collegium Budapest in supporting this study. We thank M. Newman and I. Der´enyi for discussions and comments on this topic.

![image 41](Evolution of the social network of scientific collaborations_images/imageFile41.png)

∗ on leave from: Babes-Bolyai University, Dept. of Theoretical Physics, Str. Kogalniceanu 1, RO-3400, ClujNapoca, Romania.

- [1] http://www.oakland.edu/∼grossman/erdoshp.html
- [2] D. J. Watts, Small World (Princeton University Press, Princeton, 1999).
- [3] A. L. Barab´asi and R. Albert, Science 286, 509 (1998).
- [4] D. J. Watts and S. H. Strogatz, Nature 393, 440 (1998).


- [5] S. N. Dorogovtsev and J. F. F. Mendes, Europhys. Lett. 52, 33 (2000).
- [6] S. N. Dorogovtsev and J. F. F. Mendes, Phys. Rev. E 62, 1842 (2000).
- [7] S. N. Dorogovtsev and J. F. F. Mendes, Europhys. Lett. 50, 1 (2000); cond-mat/ 0009065 (2000); S. N. Dorogovtsev, J. F. F. Mendes and A. N. Samukhin, Phys. Rev. Lett. 85, 4633 (2000); cond-mat/0009090 (2000); cond-mat/0011077 (2000);
- [8] P. L. Krapivsky, S. Redner and F. Leyvraz, Phys. Rev. Lett 85, 4629 (2000); P. L. Krapivsky and S. Redner, cond-mat/0011094 (2000).
- [9] S. Redner, Euro. Phys. Journ. B 4, 131 (1998).
- [10] M. E. J. Newman, Proc. Nat. Acad. Sci. USA 98, 404

(2001).

- [11] M. E. J. Newman, cond-mat/0011144 (2000).
- [12] L. A. N. Amaral, A. Scala, M. Barthe´le´my and H. E. Stanley, Proc. Nat. Acad. Sci. USA 97, 11149 (2000).
- [13] A. L. Barab´asi, R. Albert and H. Jeong, Physica A 272, 173 (1999).
- [14] R. Albert and A. L. Barab´asi, Phys. Rev. Lett. 85, 5234

(2000).

- [15] R. Cohen, K. Erez, D. ben-Avraham and S. Havlin, Phys. Rev. Lett. 85, 4626 (2000).
- [16] L. Kullmann and J. Kerte´sz, cond-mat/0012410 (2000).
- [17] R. Pastor-Satorras and A. Vespignani, Phys. Rev. Lett. 86, 3200 (2001).
- [18] S. Wasserman and K. Faust, Social Network Analysis (Cambridge Univ. Press, Cambridge, 1994).
- [19] M. Kochen (ed.) The Small World (Ablex, Norwood, NJ, 1989).
- [20] R. Albert, H. Jeong and A.L. Barab´asi, Nature 400, 130

(1999).

- [21] S. Lawrence and C. L. Giles, Nature 400 107 (1999).
- [22] B. A. Huberman and L. A. Adamic, Nature 401 131

(1999); M. Faloutsos, P. Faloutsos and C. Faloutsos, Proc. ACM SIGCOMM, Comput. Commun. Rev. 29, 251 (1999); A. Broder, R. Kumar, F. Maghoul, P. Raghavan, S. Rajalopagan, R. Stata, A. Tomkins and J. Wiener, in Proceedings of the Ninth International World-Wide Web Conference (2000).

- [23] H. Jeong, B. Tombor, R. Albert, Z. N. Oltvai and A.L. Barab´asi, Nature 407, 651 (2000); D. A. Fell and A. Wagner, in Animating the cellular map, edited by J.-H. S. Hofmeyr, J. M. Rohwer and J. L. Snoep (Stellenbosch University Press, Stellenbosch. 2000), p. 79. Tech. Rep. 00-07-041, Santa Fe Institute (2000).
- [24] R. V. Sole´ and J. M. Montoya, cond-mat/0011196 (2000); J. M. Montoya and R. V. Sole´, cond-mat/0011195 (2000).
- [25] S. Lawrence, C. L. Giles, Science 280, 98 (1998).
- [26] J. W., P. D. F. Grossman, Jon, Congressus Numerantium, Vol. 108 129-131 (1995).
- [27] P. Erd˝os and A. Re´nyi, Publ. Math. Debrecen 6, 290

(1959).

- [28] B. Bollob´as, Random Graphs (Academic Press, London)

(1985).

- [29] Note that such skewed distributions have been already modeled, from a diﬀerent perspective, in scientometrics, see, e.g. A. Schubert, W. Glanzel, Scientometrics 6(3), 149 (1984).


- [30] A. Bunde, S. Havlin, Fractals and Disordered Systems, 2nd Ed. (Springer-Verlag, Berlin Heidelberg New York, 1996).
- [31] A-L. Barab´asi, R. Albert and H. Jeong, Physica A 281, 69 (2000).
- [32] R. Albert, H. Jeong and A.L. Barab´asi, Nature 406, 378

(2000).

- [33] M. E. J. Newman, S. H. Strogatz and D. J. Watts, condmat/0007253 (2000).


Figure Captions: Fig. 1 (a) Cumulative number of papers for the M and NS databases in the period 1991-98. The inset shows the number of papers published each year. (b) Cumulative number of authors (nodes) for the M and NS databases in the period 1991-98. The inset shows the number of new authors added each year.

Fig. 2 Degree distribution for the (a) M and (b) NS database, showing the data based on the cumulative results up to yeas 1993 (×) and 1998 (•). (c) Degree distribution shown with logarithmic binning computed from the full dataset cumulative up to 1998. The lines correspond do the best ﬁts, and have the slope 2.1 (NS, dotted) and 2.4 (M, dashed).

- Fig. 3 Average separation in the M and NS databases.

The separation is computed on the cumulative data up to the indicated year.

- Fig. 4 Clustering coeﬃcient of the M and NS database,

determined for the cumulative data up to the year indicated on the t axis.

- Fig. 5 Relative size of the largest cluster for the M and

NS database. Results are computed on the cumulative data up to the given year.

- Fig. 6 Average number of links per node (< k >) for


the M and NS database. Results are computed on the cumulative data up to the given year.

Fig 7 Cumulated preferential attachment (κ(k)) of incoming new nodes for the M and NS database. Results computed by considering the new nodes coming in the speciﬁed year, and the network formed by nodes already present up to this year. In the absence of preferential attachment κ(k) ∼ k, shown as continuous line on the ﬁgures.

- Fig. 8 Internal preferential attachment for the M and

NS database, 3D plots: ∆k as a function of k1 and k2. Results computed on the cumulative data in the last considered year.

- Fig. 9 Cumulated internal preferential attachment

(κ(k)) for the M and NS database, scaling as a function of the k1k2 product. Results computed on the cumulative data in the last considered year. The straight lines have slope 1, expected for κ(k1k2) if there would be no preferential attachment.

- Fig. 10 Scaling of Φ(k) (a) and of τ(k) (b) for the

NS database, demonstrating the trends in the small and large k behavior of the degree distribution (see text).

- Fig. 11 Computer simulated dynamics of the average


connectivity in the proposed model. (Nmax = 1000, a =

0.001, β = 1 and b = 2)

- Fig. 12 Computer simulated dynamics for the real and

apparently measured diameter value. (Nmax = 1000, a = 0.001, β = 1, b = 2 and Ns = 200)

- Fig. 13 Clustering coeﬃcient for diﬀerent values of


the a parameter as a function of the system size N. (Nmax = 1000, β = 1 and b = 2, values of a are 0 (•), 0.00025 (+), 0.0005 (△), 0.00075 (∗), 0.002 (▽).) The inset shows the scaling of the Nmin value as a function of the a parameter. (Nmax = 1000, β = 1 and b = 2, the line shows a ﬁt lnNmin = −1.887 − 1.144 · lna.

- Fig. 14 Connectivity distributions as predicted by nu-

merical simulation for diﬀerent stages of evolution of the network (a = 0.001, β = 1 and b = 2).

- Fig. 15 Connectivity distribution generated by the


numerical simulations for linear (ν = 1) and nonlinear (ν = 0.75) preferential attachment (Nmax = 3500, a = 0.0005, β = 1 and b = 2).

