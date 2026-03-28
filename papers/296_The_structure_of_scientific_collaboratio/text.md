The structure of scientiﬁc collaboration networks

arXiv:cond-mat/0007214v1[cond-mat.stat-mech]12 Jul 2000

M. E. J. Newman

Santa Fe Institute, 1399 Hyde Park Road, Santa Fe, NM 87501

We investigate the structure of scientiﬁc collaboration networks. We consider two scientists to be connected if they have authored a paper together, and construct explicit networks of such connections using data drawn from a number of databases, including MEDLINE (biomedical research), the Los Alamos e-Print Archive (physics), and NCSTRL (computer science). We show that these collaboration networks form “small worlds” in which randomly chosen pairs of scientists are typically separated by only a short path of intermediate acquaintances. We further give results for mean and distribution of numbers of collaborators of authors, demonstrate the presence of clustering in the networks, and highlight a number of apparent diﬀerences in the patterns of collaboration between the ﬁelds studied.

I. INTRODUCTION

A social network is a collection of people, each of whom is acquainted with some subset of the others. Such a network can be represented as a set of points (or vertices) denoting people, joined in pairs by lines (or edges) denoting acquaintance. One could, in principle, construct the social network for a company or ﬁrm, for a school or university, or for any other community up to and including the entire world.

Social networks have been the subject of both empirical and theoretical study in the social sciences for at least ﬁfty years [1–4], partly because of inherent interest in the patterns of human interaction, but also because their structure has important implications for the spread of information and disease. It is clear for example that variation in just the average number of acquaintances which individuals have (also called the average degree of the network) might substantially inﬂuence the propagation of a rumor, a fashion, a joke, or this year’s ﬂu.

One of the ﬁrst empirical studies of the structure of social networks, conducted by Stanley Milgram [5], asked test subjects, chosen at random from a Nebraska telephone directory, to get a letter to a target subject in Boston, a stockbroker friend of Milgram’s. The instructions were that the letters were to be sent to their addressee (the stockbroker) by passing them from person to person, but that they could be passed only to someone whom the passer knew on a ﬁrst-name basis. Since it was not likely that the initial recipients of the letters were on a ﬁrst-name basis with a Boston stockbroker, their best strategy was to pass their letter to someone whom they felt was nearer to the stockbroker in some sense, either social or geographical: perhaps someone they knew in the ﬁnancial industry, or a friend in Massachusetts.

A moderate number of Milgram’s letters did eventually reach their destination, and Milgram discovered that the average number of steps taken to get there was only about six, a result which has since passed into folklore and was immortalized by John Guare in the title of his 1990 play Six Degrees of Separation [6]. Although there were certainly biases present in Milgram’s experiment—

letters which took a longer path were perhaps more likely to get lost or forgotten, for instance—Milgram’s result is usually taken as evidence of the “small world hypothesis,” that most pairs of people in a population can be connected by only a short chain of intermediate acquaintances, even when the size of the population is very large.

Milgram’s work, although cleverly conducted and in many ways revealing, does not however tell us much about the detailed structure of social networks, data that are crucial to the understanding of information or disease propagation. Many subsequent studies have addressed this problem. Discussions can be found in Refs. [2] and [4]. A number of investigations of real acquaintance networks have been performed. Foster et al. [7] and Fararo and Sunshine [8], for instance, both constructed maps of friendship networks among high-school students, and Bernard et al. did the same for communities of Utah Mormans, Native Americans, and Micronesian islanders [9]. Surveys or interviews were used to determine friendships. While these studies directly probe the structure of the relevant social network, they suffer from two substantial shortcomings which limit their usefulness. First, the studies are labor-intensive and the size of the network which can be mapped is therefore limited—typically to a few tens or hundreds of people. Second, these studies are highly sensitive to subjective bias on the part of interviewees; what is considered to be an “acquaintance” can diﬀer considerably from one person to another.

To avoid these issues, a number of researchers have studied networks for which there exist more numerous data and more precise deﬁnitions of connectedness. Examples of such networks are the electric power grid [10], the internet [11,12], and the pattern of air traﬃc between airports [13]. These networks however suﬀer from a different problem: although they may loosely be said to be social networks in the sense that their structure in some way reﬂects features of the society which built them, they do not directly measure actual contact between people. Many researchers are, of course, interested in these networks for their own sake, but to the extent that we want to know about human acquaintance patterns, power grids

and computer networks are a poor proxy for the real thing.

Perhaps the nearest that studies of this kind have come to looking at a true acquaintance network is in studies of the network of movie actors [10,13]. In this network, which has been thoroughly documented and contains nearly half a million people, two actors are considered connected if they have been credited with appearance in the same ﬁlm. However, while this is genuinely a network of people, it is far from clear that the appearance of two actors in the same movie implies that they are acquainted in any but the most cursory fashion, or that their acquaintance extends oﬀ-screen. To draw conclusions about patterns of every-day human interaction from the movies would, it seems certain, be a mistake.

In this paper, we present a study of a genuine network of human acquaintances which is both large—containing over a million people—and for which a precise deﬁnition of acquaintance is possible. That network is the network of scientiﬁc collaboration, as documented in the papers which scientists write.

II. SCIENTIFIC COLLABORATION NETWORKS

We study networks of scientists in which two scientists are considered connected if they have coauthored a paper together. This seems a reasonable deﬁnition of scientiﬁc acquaintance: most people who have written a paper together will know one another quite well. It is a moderately stringent deﬁnition, since there are many scientists who know one another to some degree but have never collaborated on the writing of a paper. Stringency however is not inherently a bad thing. A stringent condition of acquaintance is perfectly acceptable, provided, as in this case, that it can be applied consistently.

We have constructed collaboration graphs for scientists in a variety of ﬁelds. The data come from four databases: MEDLINE (which covers published papers on biomedical research), the Los Alamos e-Print Archive (preprints primarily in theoretical physics), SPIRES (published papers and preprints in high-energy physics), and NCSTRL (preprints in computer science). In each case, we examine papers which appeared in a ﬁve year window from 1995 to 1999 inclusive. The sizes of the databases range from 2 million papers for MEDLINE to 13 000 for NCSTRL.

The fact that some of the databases used contain unrefereed preprints should not be regarded negatively. Although unrefereed preprints may be of lower average scientiﬁc quality than papers in peer-reviewed journals, they are, as an indicator of social connection, every bit as good as their refereed counterparts.

The idea of constructing a scientiﬁc collaboration network from the publication record is not new, although no detailed study has previously been published. Among mathematicians the concept of the Erd¨s number has long been current. Paul Erdo¨s was an inﬂuential, but

itinerant, Hungarian mathematician, who apparently spent a large portion of his later life living out of a suitcase and writing papers with those of his colleagues willing to give him room and board. He published more papers during his life than any other mathematician in history (at least 1400). The Erdo¨s number measures a mathematician’s proximity, in bibliographical terms, to the great man. Those who have published a paper with Erdo¨s have an Erdo¨s number of 1. Those have published with a coauthor of Erdo¨s have an Erdo¨s number of 2. And so on. An exhaustive list exists of all mathematicians with Erdo¨s numbers of 1 and 2 [14].

There are in addition many other interesting quantities to be measured on collaboration networks, including the number of collaborators of scientists, the numbers of papers they write, and the degree of “clustering,” which is the probability that two of a scientist’s collaborators have themselves collaborated. All of these quantities and several others are considered in this paper.

III. RESULTS

Table I gives a summary of some of the results of

- our analysis of the databases described in the previ-
- ous section. In addition to results for the four complete databases, we also give results for three subjectspeciﬁc subsets of the Los Alamos Archive, covering astrophysics (denoted astro-ph), condensed matter physics (cond-mat), and theoretical high-energy physics (hep-th). In this section we highlight some of our results and discuss their implications.


a. Number of authors Estimating the true number of distinct authors in a database is complicated by two problems. First, two authors may have the same name. Second, an author may identify themselves in diﬀerent ways on diﬀerent papers, e.g., using ﬁrst initial only, using all initials, or using full name. In order to estimate the size of the error introduced by these eﬀects, all analyses reported here have been carried out twice. The ﬁrst time we use all initials of each author. This will rarely confuse two diﬀerent authors for the same person (although this will still happen occasionally), but sometimes misidentiﬁes the same person as two diﬀerent people, thereby overestimating the total number of authors. The second analysis is carried out using only the ﬁrst initial of each author, which will ensure that diﬀerent publications by the same author are almost always identiﬁed as such, but will with some regularity confuse distinct authors for the same person. Thus these two analyses give upper and lower bounds on the number of authors, and hence also of many other quantities that we are interested in. In Table I we quote both estimates of the number of authors for each database. For some other quantities we quote only an error estimate based on the separation of the upper and lower bounds.

![image 1](The structure of scientific collaboration networks_images/imageFile1.png)

![image 2](The structure of scientific collaboration networks_images/imageFile2.png)

![image 3](The structure of scientific collaboration networks_images/imageFile3.png)

![image 4](The structure of scientific collaboration networks_images/imageFile4.png)

![image 5](The structure of scientific collaboration networks_images/imageFile5.png)

![image 6](The structure of scientific collaboration networks_images/imageFile6.png)

Los Alamos e-Print Archive MEDLINE complete astro-ph cond-mat hep-th SPIRES NCSTRL

![image 7](The structure of scientific collaboration networks_images/imageFile7.png)

![image 8](The structure of scientific collaboration networks_images/imageFile8.png)

![image 9](The structure of scientific collaboration networks_images/imageFile9.png)

![image 10](The structure of scientific collaboration networks_images/imageFile10.png)

![image 11](The structure of scientific collaboration networks_images/imageFile11.png)

![image 12](The structure of scientific collaboration networks_images/imageFile12.png)

![image 13](The structure of scientific collaboration networks_images/imageFile13.png)

![image 14](The structure of scientific collaboration networks_images/imageFile14.png)

![image 15](The structure of scientific collaboration networks_images/imageFile15.png)

![image 16](The structure of scientific collaboration networks_images/imageFile16.png)

total papers 2156769 98502 22029 22016 19085 66652 13169 total authors 1388989 52909 16706 16726 8361 56627 11994

![image 17](The structure of scientific collaboration networks_images/imageFile17.png)

![image 18](The structure of scientific collaboration networks_images/imageFile18.png)

![image 19](The structure of scientific collaboration networks_images/imageFile19.png)

![image 20](The structure of scientific collaboration networks_images/imageFile20.png)

![image 21](The structure of scientific collaboration networks_images/imageFile21.png)

![image 22](The structure of scientific collaboration networks_images/imageFile22.png)

![image 23](The structure of scientific collaboration networks_images/imageFile23.png)

![image 24](The structure of scientific collaboration networks_images/imageFile24.png)

ﬁrst initial only 1006412 45685 14303 15451 7676 47445 10998

![image 25](The structure of scientific collaboration networks_images/imageFile25.png)

![image 26](The structure of scientific collaboration networks_images/imageFile26.png)

![image 27](The structure of scientific collaboration networks_images/imageFile27.png)

![image 28](The structure of scientific collaboration networks_images/imageFile28.png)

mean papers per author 5.5(4) 5.1(2) 4.8(2) 3.65(7) 4.8(1) 11.6(5) 2.55(5) mean authors per paper 2.966(2) 2.530(7) 3.35(2) 2.66(1) 1.99(1) 8.96(18) 2.22(1) collaborators per author 14.8(1.1) 9.7(2) 15.1(3) 5.86(9) 3.87(5) 173(6) 3.59(5)

![image 29](The structure of scientific collaboration networks_images/imageFile29.png)

![image 30](The structure of scientific collaboration networks_images/imageFile30.png)

![image 31](The structure of scientific collaboration networks_images/imageFile31.png)

![image 32](The structure of scientific collaboration networks_images/imageFile32.png)

![image 33](The structure of scientific collaboration networks_images/imageFile33.png)

![image 34](The structure of scientific collaboration networks_images/imageFile34.png)

![image 35](The structure of scientific collaboration networks_images/imageFile35.png)

![image 36](The structure of scientific collaboration networks_images/imageFile36.png)

![image 37](The structure of scientific collaboration networks_images/imageFile37.png)

![image 38](The structure of scientific collaboration networks_images/imageFile38.png)

![image 39](The structure of scientific collaboration networks_images/imageFile39.png)

![image 40](The structure of scientific collaboration networks_images/imageFile40.png)

cutoﬀ zc 7300(2700) 52.9(4.7) 49.0(4.3) 15.7(2.4) 9.4(1.3) 1200(300) 10.7(1.6) exponent τ 2.5(1) 1.3(1) 0.91(10) 1.1(2) 1.1(2) 1.03(7) 1.3(2)

![image 41](The structure of scientific collaboration networks_images/imageFile41.png)

![image 42](The structure of scientific collaboration networks_images/imageFile42.png)

![image 43](The structure of scientific collaboration networks_images/imageFile43.png)

![image 44](The structure of scientific collaboration networks_images/imageFile44.png)

![image 45](The structure of scientific collaboration networks_images/imageFile45.png)

![image 46](The structure of scientific collaboration networks_images/imageFile46.png)

![image 47](The structure of scientific collaboration networks_images/imageFile47.png)

![image 48](The structure of scientific collaboration networks_images/imageFile48.png)

size of giant component 1193488 44337 14845 13861 5835 49002 6396 ﬁrst initial only 892193 39709 12874 13324 5593 43089 6706 as a percentage 87.3(7)% 85.4(8)% 89.4(3) 84.6(8)% 71.4(8)% 88.7(1.1)% 57.2(1.9)%

![image 49](The structure of scientific collaboration networks_images/imageFile49.png)

![image 50](The structure of scientific collaboration networks_images/imageFile50.png)

![image 51](The structure of scientific collaboration networks_images/imageFile51.png)

![image 52](The structure of scientific collaboration networks_images/imageFile52.png)

![image 53](The structure of scientific collaboration networks_images/imageFile53.png)

![image 54](The structure of scientific collaboration networks_images/imageFile54.png)

![image 55](The structure of scientific collaboration networks_images/imageFile55.png)

![image 56](The structure of scientific collaboration networks_images/imageFile56.png)

![image 57](The structure of scientific collaboration networks_images/imageFile57.png)

![image 58](The structure of scientific collaboration networks_images/imageFile58.png)

![image 59](The structure of scientific collaboration networks_images/imageFile59.png)

![image 60](The structure of scientific collaboration networks_images/imageFile60.png)

2nd largest component 56 18 19 16 24 69 42 mean distance 4.4(2) 5.9(2) 4.66(7) 6.4(1) 6.91(6) 4.0(1) 9.7(4) maximum distance 21 20 14 18 19 19 31 clustering coeﬃcient C 0.072(8) 0.43(1) 0.414(6) 0.348(6) 0.327(2) 0.726(8) 0.496(6)

![image 61](The structure of scientific collaboration networks_images/imageFile61.png)

![image 62](The structure of scientific collaboration networks_images/imageFile62.png)

![image 63](The structure of scientific collaboration networks_images/imageFile63.png)

![image 64](The structure of scientific collaboration networks_images/imageFile64.png)

![image 65](The structure of scientific collaboration networks_images/imageFile65.png)

![image 66](The structure of scientific collaboration networks_images/imageFile66.png)

![image 67](The structure of scientific collaboration networks_images/imageFile67.png)

![image 68](The structure of scientific collaboration networks_images/imageFile68.png)

![image 69](The structure of scientific collaboration networks_images/imageFile69.png)

![image 70](The structure of scientific collaboration networks_images/imageFile70.png)

![image 71](The structure of scientific collaboration networks_images/imageFile71.png)

![image 72](The structure of scientific collaboration networks_images/imageFile72.png)

![image 73](The structure of scientific collaboration networks_images/imageFile73.png)

![image 74](The structure of scientific collaboration networks_images/imageFile74.png)

TABLE I. Summary of results of the analysis of seven scientiﬁc collaboration networks. Numbers in parentheses are standard errors on the least signiﬁcant ﬁgures.

- b. Mean papers per author and authors per paper Au-

thors typically wrote about four papers in the ﬁve year period covered by this study. The average paper had about three authors. Notable exceptions are in theoretical high-energy physics and computer science in which smaller collaborations are the norm (average two people), and the SPIRES high-energy physics database with an average of 9 authors per paper. The reason for this last impressive ﬁgure is that the SPIRES database contains data on experimental as well as theoretical work. High-energy experimental collaborations can run to hundreds or thousands of people, the largest author list in the SPIRES database giving the names of a remarkable 1681 authors on a single paper.

- c. Number of collaborators The striking diﬀerence in


collaboration patterns in high-energy physics is further highlighted by the results on the average number of collaborators of an author. This is the average total number of people with whom a scientist collaborates during the period of study—the average degree, in the graph theorist’s language. For purely theoretical databases such as the hep-th subset of the Los Alamos Archive (covering high-energy physics theory) and NCSTRL (computer science), this number is low, on the order of four. For partly or wholly experimental databases (condensed matter physics and astrophysics at Los Alamos and MEDLINE (biomedicine)), the degree is signiﬁcantly higher, as high as 15 for astrophysics. But high-energy experiment easily takes the prize, with an average of 173 collaborators per author.

There is more to the story of numbers of collaborators however. In Fig. 1 we show histograms of the numbers of collaborators of scientists in four of the smaller databases. There has been a signiﬁcant amount of recent discussion of this distribution for a variety of networks in the liter-

frequency()[arb. units]pz

- 100
- 101
- 102
- 103
- 104
- 105
- 106
- 107


10−1

astrophysics condensed matter

| |
|---|


high−energy

computer science

1 10 100 number of collaborators z

FIG. 1. Histograms of the number of collaborators of scientists in four of the databases studied here. The solid lines are least-squares ﬁts to Eq. (1).

ature. A number of authors [11,12,15] have pointed out that if one makes a similar plot for the number of connections (or “links”) z to or from sites on the World Wide Web, the resulting distribution closely follows a power law: P(z) ∼ p−τ, where τ is a constant exponent with (in that case) a value of about 2.5. Barabasi and Albert have suggested [16] that a similar power-law result may apply to all or at least most other networks of interest, including social networks. Others have presented a variety of evidence to the contrary [13]. Our data do not follow a power-law form perfectly. If they did, the curves in Fig. 1 would be straight lines on the logarithmic scales

used. However, our data are well ﬁtted by a power-law form with an exponential cutoﬀ:

P(z) ∼ p−τe−z/z

, (1)

c

where τ and zc are constants. Fits to this form are shown as the solid lines in the ﬁgure. In each case the ﬁt has an R2 of better than 0.99 and p-values for both power-law and exponential terms of less than 10−3.

This form is commonly seen in physical systems, and implies an underlying degree distribution which follows a power-law, but with some imposed constraint that places a limit on the maximum value of z. One possible explanation of this cutoﬀ in the present case is that it arises as a result of the ﬁnite (5 year) window of data used. If this were the case, we would expect the cutoﬀ to increase with increasing window size. But even in the (impractical) limit of inﬁnite window size, a cutoﬀ would still be imposed by the ﬁnite working lifetime of a professional scientist (about 40 years).

The values of τ and zc are given in the table for each database. The value of the cutoﬀ size zc, varies considerably. For the mostly theoretical condensed matter, highenergy theory, and computer science databases it takes small values on the order of 10, indicating that theorists rarely had more than this many collaborators during the ﬁve-year period. In other cases, such as SPIRES and MEDLINE it takes much larger values. In the case of SPIRES this is clearly again because of the presence of very large experimental collaborations in the data. MEDLINE is more interesting. A number of people have suggested to the author that the presence of individuals with very large numbers of collaborators in the biomedical community may be the result of the practice in that community of laboratory directors signing their name to all papers emerging from their laboratories. One can well imagine that this would produce individuals with a very high apparent number of collaborators.

The exponent τ of the power-law distribution is also interesting. We note that in all the “hard sciences,” this exponent takes values close to 1. In the MEDLINE (biomedicine) database however, its value is 2.5, similar to that noted for the World Wide Web. The value τ = 2 forms a dividing line between two fundamentally diﬀerent behaviors of the network. For τ < 2, the average properties of the network are dominated by the few individuals who have a large number of collaborators, while graphs with τ > 2 are dominated by the little people—the ones with few collaborators. Thus, one ﬁnds that in biomedical research the highly connected individuals do not determine the average characteristics of their ﬁeld, despite their names appearing on a lot of papers. In physics and computer science, on the other hand, it appears that they do.

In Fig. 2 we show histograms of the number of papers which authors have written in the same four databases. As the ﬁgure shows, the distribution of papers follows a similar form to the distribution of collaborators. The

- 100
- 101
- 102
- 103
- 104
- 105
- 106


astrophysics condensed matter

| |
|---|


high−energy

computer science

frequency[arb. units]

10−1

10−2

1 10 100 number of papers

FIG. 2. Histograms of the number of papers written by scientists in four of the databases. As with Fig. 1, the solid lines are least-squares ﬁts to Eq. (1).

solid lines are again ﬁts to Eq. (1), and again match the data well in all cases.

d. The giant component In all social networks there is the possibility of a percolation transition [17]. In networks with very small numbers of connections between individuals, all individuals belong only to small islands of collaboration or communication. As the total number of connections increases, however, there comes a point at which a giant component forms—a large group of individuals who are all connected to one another by paths of intermediate acquaintances. It appears that all the databases considered here are connected in this sense. Measuring the size of groups of connected authors in each database, we ﬁnd (see table) that in most of the databases the largest such group occupies around 80 or 90 percent of all authors: almost everyone in the community is connected to almost everyone else by some path (probably many paths) of intermediate coauthors. In high-energy theory and computer science the fraction is smaller but still more than half the total size of the network. (These two databases may, it appears, give a less complete picture of their respective ﬁelds than the others, owing to the existence of competing databases with overlapping coverage. The small size of the giant component may in part be attributable to this.)

We have also calculated the size of the second-largest group of connected authors for each database. In each case this group is far smaller than the largest. This is a characteristic signature of networks which are well inside the percolating regime. In other words, it appears that scientiﬁc collaboration networks are not on the borderline of connectedness—they are very highly connected and in no immediate danger of fragmentation. This is a good thing. Science would probably not work at all if scientiﬁc communities were not densely interconnected.

mean distance between scientists

10

8

6

4

MEDLINE

arxiv.org (all subjects)

2

arxiv.org (individual subjects)

SPIRES

NCSTRL

0

0 2 4 6 8 10 log N/log z

FIG. 3. Average distance between pairs of scientists in the various communities, plotted against the average distance on a random graph of the same size and average coordination number. The dotted line is the best ﬁt to the data which also passes through the origin.

e. Average degrees of separation We have calculated exhaustively the minimum distance, in terms of numbers of intermediate acquaintances, between all pairs of scientists in the databases studied. We ﬁnd that the typical distance between a pair of scientists is about six; there are six degrees of separation in science, just as there are in the larger world of human acquaintance. Even in very large communities, such as the biomedical research community documented by MEDLINE, it takes an average of only six steps to reach a randomly chosen scientist from any other, out of the more than one million who have published. We conjecture that this has a profound eﬀect on the way in which the scientiﬁc community operates. Despite the importance of written communication in science as a document and archive of work carried out, and of scientiﬁc conferences as a broadcast medium for summary results, it is probably safe to say that the majority of scientiﬁc communication takes place by private conversation. Clearly, news of important discoveries and scientiﬁc information can circulate far faster in a world where the typical separation of two scientists is six, than it can in one where it is a thousand, or a million.

The variation of average vertex–vertex distances from one database to another also shows interesting behavior. The simplest model of a social network is the random graph—a network in which people are connected to one another uniformly at random [18]. For a given number N of scientists with a given mean number z of collaborators, the average vertex–vertex distance on a random graph scales logarithmically with N according to log N/ logz. Social networks are measurably different from random graphs [4], but the random graph nonetheless provides a useful benchmark for comparing

them against. Watts and Strogatz [10] deﬁned a social network as being “small” if typical distances were comparable with those on a random graph. This implies that such networks should also have typical distances which grow roughly logarithmically in N, and indeed some authors (e.g., Ref. [13]) have used this logarithmic growth as the deﬁning criterion for a “small world.” In Fig. 3 we show the average distance between all pairs of scientists for each of the networks studied here, including separate calculations for the subject divisions of the Los Alamos Archive, of which there are nine. In total there are 12 points, which we have plotted against log N/ logz, using the appropriate values of N and z from Table I. As the ﬁgure shows, there is a strong correlation (R2 = 0.83) between the measured distances and the expected log N behavior, indicating that distances do indeed scale logarithmically with the number of scientists in a community.

We also quote in Table I ﬁgures for the maximum separation of pairs of scientists in each database, which tells us the greatest distance we will ever have to go to connect two people together. This quantity is often referred to as the diameter of the network. For all the networks examined here, it is on the order of 20; there is a chain of at most about 20 acquaintances connecting any two scientists. (This result of course excludes pairs of scientists who are not connected at all, as will often be the case for the 10 or 20 percent who fall outside the giant component.)

f. Clustering Watts and Strogatz [10] have pointed out another important property of social networks which is absent from many network models which have been employed by social scientists and epidemiologists. Real networks are clustered, meaning that they possess local communities in which a higher than average number of people know one another. A laboratory or university department might form such a community in science, as might the set of researchers who work in a particular subﬁeld. Watts and Strogatz also proposed a way of probing for the existence of such clustering in real network data. They deﬁned a clustering coeﬃcient C, which for our purposes is the average fraction of pairs of a person’s collaborators who have also collaborated with one another. Thus for example a person with z = 10 collaborators has

- 1

![image 75](The structure of scientific collaboration networks_images/imageFile75.png)

- 2z(z − 1) = 45 pairs of collaborators. If, say, 20 of those pairs have also collaborated on a paper, then the clustering coeﬃcient for that person is 20/45 = 0.44. The same quantity calculated for the entire network is the quantity we call C. Values are given in Table I, and show that there is a very strong clustering eﬀect in the scientiﬁc community: two scientists typically have a 30 percent or greater probability of collaborating if they have both collaborated with another third scientist. A number of explanations of this result are possible. To some extent it is certainly the result of the appearance of papers with three or more authors: such papers clearly contain trios of scientists who have all collaborated with one another. However, the values measured here cannot be entirely accounted for in this way, and indicate also that scien-


tists either introduce their collaborators to one another, thereby engendering new collaborations, or perhaps that institutions bring sets of collaborators together to form a variety of new collaborations.

The MEDLINE database is interesting in that it possess a much lower value of the clustering coeﬃcient than the “hard science” databases. This appears to indicate that it is signiﬁcantly less common in biological research for scientists to broker new collaborations between their acquaintances than it is in physics or computer science.

the few people with many.

The work reported in this paper represents, inevitably, only a ﬁrst look at the collaboration networks described. Many theoretical measures have been described, in addition to the distances and clustering studied here, which reﬂect socially important structure in such networks. We hope that academic collaboration networks will prove a reliable and copious source of data for testing out such theories, as well as being interesting in their own right, especially to ourselves, the scientists whom they describe.

IV. CONCLUSIONS

ACKNOWLEDGEMENTS

We have analyzed the collaboration networks of scientists from biology and medicine, various sub-disciplines of physics, and computer science, using the author attributions from papers or preprints appearing in those areas over a ﬁve year period from 1995 to 1999. We ﬁnd a number of interesting properties of these networks. In all cases, scientiﬁc communities seem to constitute a “small world” in which the average distance between scientists via a line of intermediate collaborators scales logarithmically with the size of the relevant community. Typically we ﬁnd that only about ﬁve or six steps are necessary to get from one randomly chosen scientist in a community to another. We conjecture that this smallness is a crucial feature of a functional scientiﬁc community.

We also ﬁnd that the networks are highly clustered, meaning that two scientists are much more likely to have collaborated if they have a third common collaborator than are two scientists chosen at random from the community. This may indicate that the processes of scientists introducing their collaborators to one another is an important one in the development of scientiﬁc communities.

We have studied the distributions of both the number of collaborators of scientists and the numbers of papers they write. In both cases we ﬁnd these distributions are well ﬁt by power-law forms with an exponential cutoﬀ. This cutoﬀ may be due to the ﬁnite time window used in the study.

We ﬁnd a number of signiﬁcant statistical diﬀerences between diﬀerent scientiﬁc communities. Some of these are obvious: experimental high-energy physics, for example, which is famous for the staggering size of its collaborations, has a vastly higher average number of collaborators per author than any other ﬁeld examined. Other differences are less obvious however. Biomedical research, for example, shows a much lower degree of clustering than any of the other ﬁelds examined. In other words it is less common in biomedicine for two scientists to start a collaboration if they have another collaborator in common. Biomedicine is also the only ﬁeld in which the exponent of the distribution of numbers of collaborators is greater than 2, implying that the average properties of the collaboration network are dominated by the many people with few collaborators, rather than, as in other ﬁelds, by

The author is indebted to Paul Ginsparg and Geoffrey West (Los Alamos e-Print Archive), Carl Lagoze (NCSTRL), Oleg Khovayko, David Lipman and Grigoriy Starchenko (MEDLINE), and Heath O’Connell (SPIRES), for making available the publication data used for this study. The author would also like to thank Dave Alderson, Paul Ginsparg, Laura Landweber, Steve Strogatz, and Duncan Watts for illuminating conversations. This work was funded in part by a grant from Intel Corporation to the Santa Fe Institute Network Dynamics Program. The NCSTRL digital library was made available through the DARPA/CNRI test suites program funded under DARPA grant N66001–98–1–8908.

![image 76](The structure of scientific collaboration networks_images/imageFile76.png)

- [1] Kochen, M., The Small World. Ablex, Norwood, NJ

(1989).

- [2] Wasserman, S. and Faust, K., Social Network Analysis. Cambridge University Press, Cambridge (1994).
- [3] Valente, T., Network Models of the Diﬀusion of Innovations. Hampton Press, Cresskill, NJ (1995).
- [4] Watts, D. J., Small Worlds. Princeton University Press, Princeton (1999).
- [5] Milgram, S., The small world problem. Psychology Today 2, 60–67 (1967).
- [6] Guare, J., Six Degrees of Separation: A Play. Vintage, New York (1990).
- [7] Foster, C. C., Rapoport, A., and Orwant, C. J., A study of a large sociogram: Elimination of free parameters. Behavioural Science 8, 56–65 (1963).
- [8] Fararo, T. J. and Sunshine, M., A study of a biased friendship network. Syracuse University Press, Syracuse, NY (1964).
- [9] Bernard, H. R., Kilworth, P. D., Evans, M. J., McCarty, C., and Selley, G. A., Studying social relations cross-culturally. Ethnology 2, 155–179 (1988).
- [10] Watts, D. J. and Strogatz, S. H., Collective dynamics of “small-world” networks. Nature 393, 440–442

(1998).

- [11] Albert, R., Jeong, H. and Barabasi,´ A.-L., Diameter of the world-wide web. Nature 401, 130–131 (1999).


- [12] Broder, A., Kumar, R., Maghoul, F., Raghavan, P., Rajagopalan, S., Stata, R., Tomkins, A., and Wiener, J., Graph structure of the web. Preprint, IBM Almaden (2000).
- [13] Amaral, L. A. N., Scala, A., Barth´el´emy. M., and Stanley, H. E., Classes of behavior of small-world networks. cond-mat/0001458.
- [14] J. W. Grossman and P. D. F. Ion, On a portion of the well-known collaboration graph. Congressus Numerantium 108, 129–131 (1995).
- [15] Faloutsos, M., Faloutsos, P. and Faloutsos, C., On Power-Law Relationships of the Internet Topology. Comp. Comm. Rev. 29, 251–262 (1999).
- [16] Barabasi,´ A. L. and Albert, R., Emergence of scaling in random networks. Science 286, 509–512 (1999).
- [17] D. Stauffer and A. Aharony, Introduction to Percolation Theory, 2nd edition. Taylor and Francis, London

(1991).

- [18] B. Bollobas,´ Random Graphs. Academic Press, New York (1985).


