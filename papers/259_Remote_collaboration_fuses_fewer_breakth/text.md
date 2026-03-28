# Remote collaboration fuses fewer breakthrough ideas

Yiling Lin1, Carl Benedikt Frey2,3,4✉ & Lingfei Wu1,4✉

https://doi.org/10.1038/s41586-023-06767-1 Received: 21 June 2022 Accepted: 19 October 2023 Published online: 29 November 2023

Theories of innovation emphasize the role of social networks and teams as facilitators of breakthrough discoveries1–4. Around the world, scientists and inventors are more plentiful and interconnected today than ever before4. However, although there are more people making discoveries, and more ideas that can be reconfigured in new ways, research suggests that new ideas are getting harder to find5,6—contradicting recombinant growth theory7,8. Here we shed light on this apparent puzzle. Analysing 20 million research articles and 4 million patent applications from across the globe over the past half-century, we begin by documenting the rise of remote collaboration across cities, underlining the growing interconnectedness of scientists and inventors globally. We further show that across all fields, periods and team sizes, researchers in these remote teams are consistently less likely to make breakthrough discoveries relative to their on-site counterparts. Creating a dataset that allows us to explore the division of labour in knowledge production within teams and across space, we find that among distributed team members, collaboration centres on late-stage, technical tasks involving more codified knowledge. Yet they are less likely to join forces in conceptual tasks—such as conceiving new ideas and designing research—when knowledge is tacit9. We conclude that despite striking improvements in digital technology in recent years, remote teams are less likely to integrate the knowledge of their members to produce new, disruptive ideas.

Check for updates

![image 1](Lin et al._2023_Remote collaboration fuses fewer breakthrough ideas_images/imageFile1.png)

The past half-century has seen a marked increase in the scale and complexity of scientific research4, to which researchers have responded by lengthening their education and training10, specializing more narrowly11 and working in teams2,4,11. The last of these has been aided by recent advances in remote work technology, allowing researchers to form distributed teams to take advantage of complementary yet geographically dispersed knowledge and expertise12–16. A widely held view is that by permitting more specialization and better matching, the rise of remote collaboration promises larger “collective brains”3 and accelerated innovation7. Indeed, seen through the lens of recombinant growth theory7, a larger number of possible collaborations increases the number of possibilities for new discoveries. Yet, in contradiction to this promise, recent work has shown that “ideas are getting harder to find”5,6.

In this article, we show how the roles of team members change as scientists and inventors switch from on-site to remote collaboration. Analysing 20 million research articles from between 1960 and 2020 and 4 million patent applications from between 1976 and 2020 across the globe, we confirm that remote teams develop and on-site teams disrupt both in science and technology. Inspired by a recent study linking disruptive innovation to team structure22, we examine author contribution disclosures and find that despite striking advances in remote work technology, collaboration at a distance still centres on late-stage, technical project tasks rather than conceptual tasks. The tendency of remote teams to execute and not conceptualize is robust to controlling for a host of potential confounders, and seemingly associated with the continued importance of face-to-face interactions. We conclude by showing that established and emerging researchers are much less likely to jointly conceive new ideas when working remotely, reducing the exposure of new talent to disruptive discovery.

One possible explanation for this apparent puzzle is that although remote collaboration among specialized researchers permits more new combinations of knowledge, it also makes it harder for teams to integrate the pieces17. In the early stages of a project, when an idea is hard to articulate and knowledge is tacit, collaboration at a distance is particularly challenging18. However, when an idea crystallizes and knowledge becomes more codified, the comparative advantage of on-site teams is gradually diminished. It follows that scientists in on-site teams are better placed to fuse knowledge and conceive the next breakthrough idea12,19,20, whereas they tend to coordinate technical work and develop established ideas when switching to remote13,21.

Our article makes three key contributions to the existing literature. First and foremost, we shed new light on the deceleration of innovation, despite the rising number of possibilities for discovery and increased research efforts5. Shifting the research focus from the performance of individual scientists6,10,23,24 to their team roles, we show that although remote collaboration involves more people in science and technology, it does not necessarily engage them in the core task of conceiving research. In other words, the creative potential of many researchers, especially emerging scholars, has not been fully realized. Second,

1School of Computing and Information, The University of Pittsburgh, Pittsburgh, PA, USA. 2Oxford Internet Institute, University of Oxford, Oxford, UK. 3Oxford Martin School, University of Oxford, Oxford, UK. 4These authors jointly supervised this work: Carl Benedikt Frey, Lingfei Wu. ✉e-mail: carl.frey@oii.ox.ac.uk; liw105@pitt.edu

diminishing returns6. The intuition of the D score is straightforward: if subsequent work that cites a product also cites its references, the focal product can be seen as building on that previous knowledge. If the converse is true—future works cite a paper or patent but ignore its acknowledged forebears—those future works recognize that output as disruptive by eclipsing the old ones referenced. TheD score varies from −1 (developing) to 1 (disruptive) as it is calculated as the difference between the probabilities of observing these two types of subsequent citation pattern25. Thus, the D score allows us to uncover the distinct roles that research teams play in unfolding the advance of science and technology. For example, the 1953 paper on DNA by Watson and Crick30 is among the most disruptive works (D = 0.96, top 1%), whereas the 2001 paper on the human genome by the International Human Genome Sequencing Consortium31 is highly developing (D = −0.017, bottom 6%). For robustness, building on the intuition that radical innovation is typically accompanied by new terminology, we also complement our D-score measure with a variable identifying papers that proposed new scientific concepts (for example, time-evolving block decimation)32and patents introducing new technology codes (for example, Web-crawling techniques for indexing)33. We further outline the overall research design and our empirical strategies in the Methods.

although large teams have long been emphasized as a way of mobilizing greater collective knowledge to push the frontiers of science4,8, recent research shows that small teams and solo researchers are more likely to disrupt both in science and technology25. We add to this literature by analysing interactions within teams and their importance for fusing breakthrough ideas. Finally, although recent research has documented that remote work can increase productivity in routine activities, such as in call centres26, another set of studies shows that it hampers creative activities20,27,28. Reconciling these findings, we show how the comparative advantage of remote work shifts as a project progresses. Whereas on-site teams evolve early-stage ideas, remote teams extend established knowledge as it becomes more codified. Taken together, our results point to the critical role that in-person interaction plays in fusing disruptive discoveries and training the next generation of talent in science and technology, even in the age of remote work.

#### Research design

To compare the innovative performance of on-site teams (with all team members in the same city) and remote teams (with team members spread across two or more cities), we start by creating and analysing two large datasets representing the full spectrum of science and technology fields. The first dataset includes data for scientific research teams responsible for 20,134,803 papers published by 22,566,650 scientists across 3,562 cities between 1960 and 2020. The name-disambiguated authors and their respective institutions with latitude and longitude values were obtained from the archived version of Microsoft Academic Graph and were verified in two ways: by two human coders who manually checked a random sample of the data, and by comparing our sample against self-reported records in ORCID (Open Researcher and Contributor ID). The second dataset includes data for patenting teams responsible for 4,060,564 patents filed by 2,732,326 inventors across 87,937 cities between 1976 and 2020. The name-disambiguated inventors and their addresses with latitude and longitude values were obtained from PatentsView, an online data platform of the US Patent and Trademark Office, and verified by two human coders (Methods). These two datasets cover teams of different fields, periods and team sizes, which allows us to examine the robustness of the relationship between collaboration distance and inventive outcomes when these variables are accounted for. However, without information on what collaborators actually do within teams, it is hard to explain any observed correlation. To overcome this data limitation, we extend our analysis of scientific research teams by including data for self-reported author contributions. Doing so, we collect 89,575 author contribution disclosures published between 2003 and 2020 from the websites ofNature,Science, Proceedings of the National Academy of Sciences of the United States of America andPLOS ONE, and map them to the name-disambiguated scientists in our data. This allows us to provide the first quantitative evidence of how roles change when the same scientist switches from on-site to remote collaboration. We also probe the robustness of our key results in three ways. First, we trace the roles of the same scientists when they work either remotely or on-site. Second, we zoom in on teams that collaborate repeatedly to investigate how roles change when members split geographically as an event study. Third, using machine learning techniques that infer team roles for papers for which author contributions are not explicit, thereby increasing our sample size, we check that differences in team roles between on-site and remote teams hold more broadly. We turn to describe these robustness tests in greater detail in Methods.

#### Remote teams produce fewer breakthroughs

Over the past half-century, research teams have expanded geographically across all sciences and technology fields (Fig. 1a–d). The average distance between team members has increased from 100 km to nearly 1,000 km in papers and from 250 km to 750 km in patents. In tandem, the fraction of extremely long-distance collaborations over 2,500 km, corresponding to the width of the south Atlantic from Brazil to Liberia, increased substantially from 2% to 15% for papers, and from 3% to 9% for patents (Fig. 2a–c). However, the contribution of remote teams to breakthrough innovation has been far less impressive. Across papers and patents, the probability of disruptionP(D > 0) falls from 28% to 22% for papers (P value < 0.001 for two-sided Student’st-test), and 67% to 55% for patents (P value < 0.001), as collaboration distance increases from 0 km to more than 600 km—approximately the distance between Paris and Frankfurt (Fig. 3a). In relative terms, the remote work penalty is around 3–4%, withP(D > 0) declining from 20.4% to 19.5% for papers (P value < 0.001 for two-sided Student’st-test), and 58.2% to 56.5% for patents (P value < 0.001), when we add our full set of controls, including fields, periods, team sizes, average career age, knowledge diversity and tie strength, as well as author fixed effects (Extended Data Fig. 1 and Extended Data Tables 1 and 2). This pattern is also robust against alternative measures of collaboration distance34 (Extended Data Fig. 2) and breakthrough discoveries (Extended Data Fig. 3). Inspired by previous studies on coordination challenges originating both from fewer in-person interactions owing to spatial separation and from more working schedule conflicts across time zones27,35, we disentangle these effects and observe a significant decline in the probability of disruption between local teams and remote teams across times zones as well as within a time zone (Fig. 3b,c). Overall, our findings consistently point to the continued value of geographic proximity for disruptive innovation.

#### On-site ideation; remote execution

With this in mind, we next turn to examine the core hypothesis of this paper: that although remote collaboration permits more new combinations of knowledge, it also makes it harder for teams to integrate the pieces. Indeed, if maintaining frequent, in-person communication is challenging when team members are spread across cities, and some activities rely more on in-person interaction than others, even the same scientists should change team roles when they switch from on-site to remote collaboration. To test precisely this, we analyse the roles of scientists in teams across four functional research activities,

For each paper or patent, we calculate a newly proposed yet extensively verified measure, ‘disruption’ or D score, which assesses to which extent an idea disrupts the state of science or technology6,25,29 (Methods). Distinguishing between disruptive discoveries and developing ones is crucial, as breakthroughs open up new avenues for progress, whereas incremental developing projects eventually run into

![image 2](Lin et al._2023_Remote collaboration fuses fewer breakthrough ideas_images/imageFile2.png)

![image 3](Lin et al._2023_Remote collaboration fuses fewer breakthrough ideas_images/imageFile3.png)

a

b

PapersPatents

![image 4](Lin et al._2023_Remote collaboration fuses fewer breakthrough ideas_images/imageFile4.png)

![image 5](Lin et al._2023_Remote collaboration fuses fewer breakthrough ideas_images/imageFile5.png)

c

d

- Fig. 1 | Mapping the global collaboration of scientists and inventors. a–d, Our dataset includes 20,134,803 papers published by scientists across 3,562 cities between 1960 and 2020 (a,b), as well as 4,060,564 patents filed by 2,732,326 inventors across 87,937 cities between 1976 and 2020 (c,d).a,c, We visualize the geographical distribution of these scientists (a) and inventors (c). Each dot is a city in our dataset. Note that although there are nearly an order of magnitude fewer patents than papers, there are still over an order of magnitude more patenting cities than paper-producing cities. The greater geographical span of patenting reflects that industry is more dispersed than academia. b,d, Building ona,c, we show where disruptive (D > 0) papers (b) and patents

(d) are produced. A dot represents all on-site teams based in that city, and an edge between two cities represents all remote teams with members in both cities37. The colours of dots and edges indicate whether disruptive work is observed at a higher (red) or lower (blue) probability relative to the population baseline. We analyse dots and edges that contain five or more teams to effectively calculate the probability of observing disruptive work, and find that on-site teams are more disruptive: 76% of cities in science (representing 58% on-site teams) and 48% of cities in patents (representing 76% on-site teams) are red. We also note that remote teams tend to be more developing: 71% of city pairs in science and 63% of city pairs in patents are blue.

Collaboration distance (km)

Collaboration distance (km)

Collaboration distance (km)

a b c

Year Year Year

Papers Patents

Papers Patents

Construction Humannecessities

Chemistry

Physics

Electricity

Cross-section Textiles Operation

Mechanical engineering

Artand humanity

Socialsciences

Scienceand engineering

1960 1970 1980 1990 2000 2010 2020 1960 1970 1980 1990 2000 2010 2020 1980 1990 2000 2010 2020

1,000

800

600

400

200

1,400

1,200

1,000

800

600

400

200

800

700

600

500

400

300

200

- Fig. 2 | The growth of collaboration distance across all sciences and technologies. We analysed the geographical distribution of scientists and inventors underlying 20,134,803 research papers published between 1960 and 2020, as well as 4,060,564 patent applications filed between 1976 and 2020.


including conceiving research, carrying out experiments, analysing data and writing the paper. We note that the probability of the same scientist contributing to conceiving research declines most markedly (from 63% to 51%, P value < 0.001) relative to all other activities (Fig. 4a). On average, scientists in remote teams are less likely to engage in conceptual tasks than their peers in on-site teams (48% versus 42%, P value < 0.001), including conceiving research or writing the paper, and correspondingly, more likely to contribute to technical tasks, such as carrying out experiments and analysing data (Fig. 4a inset). These patterns hold when we control for potential confounders, including research fields, periods and team sizes (Methods and Extended

(34%) barely changes with the difference in their citation impacts. However, in remote teams, this probability decreases markedly from 33%, when two authors have the same level of citations, to 23%, when one has four orders of magnitude more citations than the other (Fig. 4b). The least and most impactful authors, in other words, are much less likely to jointly conceive new ideas in remote teams than in on-site teams (Fig. 4b inset). This striking pattern, whereby on-site teams engage less established researchers in conceptual work, whereas remote teams merely assign them technical tasks, means that in the latter case, the opportunities for idea generation do not trickle down the hierarchy of citation impacts from established scholars to emerging ones. We conclude that on-site teams are particularly important as they serve as an escalator for new talent to co-lead in conceptualizing the next breakthrough.

- Data Table 3). In addition, when we switch our focus from the role of individual scientists to their interactions within the team, we find the same pattern: the relative probability of two authors joining forces in conceiving research declines from 34% to 28% (P value < 0.001) when they switch from on-site to remote collaboration (Extended
- Data Table 4). Our findings have implications for the future of scientific and techno-


#### Discussion

In this paper, we shed new light on one of the great puzzles of our time: why the connectivity brought by the Internet has not led to the upsurge in innovation that recombinant theory predicts. Our key finding is that although remote collaboration permits more new combinations of knowledge in principle, it also makes it harder for teams to integrate the pieces.

logical progress. Building on the result that on-site teams involve more talent in conceiving research, we turn to explore how this affects the next generation of researchers, distinguishing between team members by their citation impacts. Doing so, we find that among on-site teams, the probability of two authors joining forces in conceiving research

from 250 km to nearly 750 km for patents during the investigated period. b,c, This increase in collaboration distance holds across all fields for papers

(b) and technology domains for patents (c). Inb,c, we show raw data (points) and also the moving average using a long, 16-year window (curves). The trends remain the same if alternative window sizes (for example, 2, 4 or 8 years) are used.

- a, The average distance between co-authors (collaboration distance) has increased markedly from less than 100 km to nearly 1,000 km for papers and


###### a b c

Papers Patents

1.10

1.10

1.10

Citations

10

5

Relative probability of disruption

Relative probability of disruption

Relative probability of disruption

0

0 400 600+ Distance (km)

1.00

1.00

1.00

0.90

0.90

0.90

Patents

Same time zone

Same time zone

Papers 0 200 400 600 600+ On-site Within a time zone

0.80

0.80

0.80

Across time zones

On-site Within a time zone

Across time zones

Collaboration distance (km)

Remote

Remote

- Fig. 3 | Remote teams produce fewer breakthrough innovations.We analysed the same datasets as in Fig. 2.a, We find that the probability of producing disruptive work (D > 0) declined from 28% to 22% for papers (P value < 0.001, n = 14,485,326) and 67% to 55% for patents (P value < 0.001,n = 3,411,366), respectively, as collaboration distance increased from 0 km to more than 600 km. In addition, the inset ofa shows that the average citation impact within


observe a substantial decline in the probability of disruption when moving from local to remote within a time zone (from 28% to 24% for papers and from 67% to 61% for patents), as well as when moving from remote within a time zone to across time zones (from 24% to 22% for papers and from 61% to 55% for patents), withP values < 0.001 in both comparisons. To facilitate the comparison between papers and patents, we show the relative probability of disruption, which is calculated as the ratio of disruption probability for the group of a given collaboration distance to the disruption probability of the entire population (grey dashed lines). In all panels, the error bars indicate a 95% bootstrap confidence interval centred at the mean. All statistical tests use a two-sided Student’st-test.

- 5 years after publication increases with collaboration distance for both papers and patents, confirming that our disruption measure is distinct from citations.


- b,c, We further distinguish between three groups of papers (b) and patents (c), including local teams as the first group, remote teams within a time zone as the second group, and remote teams across time zones as the third group. We


At a time when scientific talent is increasingly moving across the globe36, and workplaces are rethinking their remote work policies in the aftermath of the coronavirus disease 2019 pandemic, our results have important implications for both managers and policymakers. As we have shown, colocation still plays a key role in the fusion of radical ideas, suggesting that the post-pandemic shift towards remote work will probably favour incremental innovation at the expense of disruptive discoveries. From a managerial point of view, projects aiming at disruptive innovation are best allocated to on-site teams, whereas projects focusing on incremental improvements can be assigned to

their distributed counterparts. Our study also underlines an important trade off that policymakers face: although remote collaboration might allow for the effective exploitation of existing ideas in the short run, it might also curtail the kind of innovation breakthroughs that drive progress and productivity over the long run. Therefore, for policymakers interested in reviving productivity growth and innovation, physical infrastructure investment to reduce travel costs and make housing affordable where knowledge industries cluster should not take the backseat to the construction of digital infrastructure.

###### a

###### b

1.15

0.45

On-site teams Remote teams

Carrying out Analysing Writing Conceiving

Probability of co-conceive

1.00

0.35

Relative probability of

Relative probability of

| | | |
|---|---|---|
| | | |
| | | |


1.1 1.0 0.9 0.8

1.15

conceptual workers

co-conceiving

Relative ratio of

0.85

0.25

1.00

On-site Remote Between authors with the least and most citations

0.85

0 400 600+

Distance (km)

0.15

0.70

100 101 102 103 104

On-site teams

Remote teams

Citation difference between authors

Fig. 4 | On-site teams conceive; remote teams carry out.a, We analysed the contribution disclosures of 89,575 papers fromNature,Science,Proceedings of the National Academy of Sciences of the United States of America andPLOS ONE (2003–2020) and identified four research activities. In our sample, the probability of conceiving, writing and analysing decreased by 12% (from 63% to 51%), 11% (from 60% to 49%) and 8% (from 58% to 50%), respectively (with P values < 0.001,n = 21,373), when scientists switched from on-site to remote. Conversely, the probability of carrying out increased by 1% (from 42% to 43%; P value < 0.05,n = 21,373). To ease comparison, we show relative probabilities, or the probability ratio between what the same scientist does in on-site and remote teams. For robustness, we use a larger sample of 16,397,750 papers, utilizing machine learning models (Methods) to predict the distinct roles of conceptual workers (engaged in conceiving and writing) and technical workers (engaged in carrying out and analysing). Again, we find that scientists are more

likely to conceive in on-site teams and less likely to carry out technical work (inset).b, On the basis of the contribution statements, we find no relationship between two co-authors joining forces in conceiving research and their citation difference (calculated when their paper was published) among on-site teams (ordinary least squares regression indicated by the green line, coefficient = 0.0002,P value > 0.05,n = 155,842), which might partly reflect more student–adviser relationships. By contrast, among remote teams, the co-conceive probability declines, from 33% to 23%, when the citation difference increases from zero to four orders of magnitude (ordinary least squares regression indicated by the orange line, coefficient = −0.022,P value < 0.001, n = 296,861). When we consider only the co-authors with the least and most citations, we observe a similar decline (inset). In all figures, the 95% bootstrap confidence intervals are shown as error bars centred at the mean. All statistical tests use a two-sided Student’st-test.

- 20. Brucks, M. S. & Levav, J. Virtual communication curbs creative idea generation. Nature 605, 108–112 (2022).
- 21. Yang, L. et al. The effects of remote work on collaboration among information workers. Nat. Hum. Behav. 6, 43–54 (2022).
- 22. Xu, F., Wu, L. & Evans, J. Flat teams drive scientific innovation. Proc. Natl Acad. Sci. USA 119, e2200927119 (2022).
- 23. Dane, E. Reconsidering the trade-off between expertise and flexibility: a cognitive entrenchment perspective. Acad. Manage. Rev. 35, 579–603 (2010).
- 24. Azoulay, P., Fons-Rosen, C. & Zivin, J. S. G. Does science advance one funeral at a time? Am. Econ. Rev. 109, 2889–2920 (2019).
- 25. Wu, L., Wang, D. & Evans, J. A. Large teams develop and small teams disrupt science and technology. Nature 566, 378–382 (2019).
- 26. Bloom, N., Liang, J., Roberts, J. & Ying, Z. J. Does working from home work? Evidence from a Chinese experiment. Q. J. Econ. 130, 165–218 (2014).
- 27. Hinds, P. J. & Bailey, D. E. Out of sight, out of sync: understanding conflict in distributed teams. Organ. Sci. 14, 615–632 (2003).
- 28. Hinds, P. J. & Weisband, S. P. in Virtual Teams That Work: Creating Conditions for Virtual Team Effectiveness (eds Gibson, C. B. & Cohen, S. G.) 21–36 (Wiley, 2003).
- 29. Funk, R. J., & Owen-Smith, J. A dynamic network measure of technological change. Manage. Sci. 63, 791–817 (2017).
- 30. Watson, J. D. & Crick, F. H. Molecular structure of nucleic acids: a structure for deoxyribose nucleic acid. Nature 171, 737–738 (1953).
- 31. Lander, E. S. et al. Initial sequencing and analysis of the human genome. Nature 409, 860–921 (2001).
- 32. Orús, R. & Vidal, G. Infinite time-evolving block decimation algorithm beyond unitary evolution. Phys. Rev. B 78, 155117 (2008).
- 33. Tamano, M., Okuda, H., Yajima, H., Hirose, T. & Kagaya, N. Retrieval method using image information. US patent US5857199A (1999).
- 34. Waltman, L., Tijssen, R. J. W. & van Eck, N. J. Globalisation of science in kilometres. J. Informetr. 5, 574–582 (2011).
- 35. Kiesler, S. & Cummings, J. N. What do we know about proximity and distance in work groups? A legacy of research. Distributed Work 1, 57–80 (2002).
- 36. Van Noorden, R. Global mobility: science on the move. Nature 490, 326–329 (2012).
- 37. Holten, D. & van Wijk, J. J. Force-directed edge bundling for graph visualization. Comput. Graph. Forum 28, 983–990 (2009).


#### Online content

Any methods, additional references, Nature Portfolio reporting summaries, source data, extended data, supplementary information, acknowledgements, peer review information; details of author contributions and competing interests; and statements of data and code availability are available at https://doi.org/10.1038/s41586-023-06767-1.

- 1. Burt, R. S. Structural holes and good ideas. Am. J. Sociol. 110, 349–399 (2004).
- 2. Jones, B. F. The rise of research teams: benefits and costs in economics. J. Econ. Perspect. 35, 191–216 (2021).
- 3. Muthukrishna, M. & Henrich, J. Innovation in the collective brain. Phil. Trans. R. Soc. B 371, 20150192 (2016).
- 4. Wuchty, S., Jones, B. F. & Uzzi, B. The increasing dominance of teams in production of knowledge. Science 316, 1036–1039 (2007).
- 5. Bloom, N., Jones, C. I., Van Reenen, J. & Webb, M. Are ideas getting harder to find? Am. Econ. Rev. 110, 1104–1144 (2020).
- 6. Park, M., Leahey, E. & Funk, R. J. Papers and patents are becoming less disruptive over time. Nature 613, 138–144 (2023).
- 7. Weitzman, M. L. Recombinant growth. Q. J. Econ. 113, 331–360 (1998).
- 8. Uzzi, B., Mukherjee, S., Stringer, M. & Jones, B. Atypical combinations and scientific impact. Science 342, 468–472 (2013).
- 9. Polanyi, M. The Tacit Dimension (Univ. Chicago Press, 1966).
- 10. Jones, B. F. The burden of knowledge and the ‘death of the renaissance man’: is innovation getting harder? Rev. Econ. Stud. 76, 283–317 (2009).
- 11. Leahey, E. & Reikowsky, R. C. Research specialization and collaboration patterns in sociology. Soc. Stud. Sci. 38, 425–440 (2008).
- 12. Cummings, J. N. & Kiesler, S. Collaborative research across disciplinary and organizational boundaries. Soc. Stud. Sci. 35, 703–722 (2005).
- 13. Freeman, R., Ganguli, I. & Murciano-Goroff, R. Why and Wherefore of Increased Scientific Collaboration Working Paper 19819 (NBER, 2014); https://doi.org/10.3386/w19819.
- 14. Fleming, L., Mingo, S. & Chen, D. Collaborative brokerage, generative creativity, and creative success. Adm. Sci. Q. 52, 443–475 (2007).
- 15. Lahiri, N. Geographic distribution of R&D activity: how does it affect innovation quality? Acad. Manage. J. 53, 1194–1209 (2010).
- 16. Maskell, P., Bathelt, H. & Malmberg, A. Building global knowledge pipelines: the role of temporary clusters. Eur. Plan. Stud. 14, 997–1013 (2006).
- 17. Cramton, C. D. The mutual knowledge problem and its consequences for dispersed collaboration. Organ. Sci. 12, 346–371 (2001).
- 18. Azoulay, P., Zivin, J. S. G. & Sampat, B. The Diffusion of Scientific Knowledge across Time and Space: Evidence from Professional Transitions for the Superstars of Medicine Working Paper 16683 (NBER, 2011); https://doi.org/10.3386/w16683.
- 19. Catalini, C. Microgeography and the direction of inventive activity. Manage. Sci. 64, 4348–4364 (2018).


Publisher’s noteSpringer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Springer Nature or its licensor (e.g. a society or other partner) holds exclusive rights to this article under a publishing agreement with the author(s) or other rightsholder(s); author self-archiving of the accepted manuscript version of this article is solely governed by the terms of such publishing agreement and applicable law.

© The Author(s), under exclusive licence to Springer Nature Limited 2023

### Methods

22% of the sample have a collaboration distance of 0–200 km, and 11%, 7% and 60% of the papers have a collaboration distance of 200–400 km, 400–600 km and more than 600 km, respectively.

###### Research design summary

We begin by tracing the change in collaboration distance, measured as the average geographical distance between the cities of team members, underlying all analysed papers and patents over the past half-century (Figs. 1 and 2). We then chart the probability of a team producing innovative breakthroughs, measured by disruption scores, against their collaboration distance (Fig. 3a). We control for a host of potential confounders, including fields, periods, team sizes, average career age, knowledge diversity and tie strength, as well as author fixed effects (Extended Data Fig. 1 and Extended Data Tables 1 and 2), and use alternative measures of collaboration distance and breakthrough innovation (Extended Data Figs. 2 and 3), for robustness. We also disentangle the effects of time and spatial separations to elucidate the disruption decline that directly corresponds to the increase in geographical distance within the same time zone, which points to fewer in-person interactions as a key hurdle to innovation (Fig. 3b,c). To understand why remote teams are less likely to disrupt more concretely, we further investigate how remote and on-site teams organize research activities differently (Extended Data Figs. 4 and 5), and find that the same scientists tend to lead conceptual tasks on-site, but deliver technical tasks remotely (Fig. 4a). This role change is robust when fields, periods and team sizes are accounted for (Extended Data Table 3) and holds broadly when we scale up our sample (Fig. 4a inset and Extended Data Fig. 6). We conclude by exploring how the interaction between team members changes from on-site teams to remote teams and find that new talent is much less likely to co-conceive research with established scholars remotely than on-site (Fig. 4b and Extended Data Table 4).

Patenting teams. PatentsView is a patent data-sharing initiative supported by the Office of the Chief Economist in the United States Patent and Trademark Office. It provides name-disambiguated authors of patents and their respective residences. The corresponding latitude and longitude values associated with the reported addresses are also provided by PatentsView. We conducted extensive entity matching work to disambiguate city names (for example, both Osaka-fu and Osaka are represented as Osaka, Japan) and merge different versions of geographic coordinates under the same city. This way, we obtain 87,937 cities of unique latitude and longitude values. Finally, we verify the quality of PatentsView’s name disambiguation of inventors as follows. We selected a random sample of 50 inventors who filed 1,975 patents. Two human coders then examined a random sample of 30 patents from the selected patents. All examined US Patent and Trademark Office patents are confirmed to be correctly assigned, giving us 100% accuracy. In the same way, we also verify the quality of PatentsView’s name disambiguation on residences and their geographical coordinates with 100% accuracy. No incorrect linkages were identified among the 98 inventor–location pairs across 30 patents.

The archived version of MAG we downloaded included 245,253,596 entities, among which 166,274,891 entities have known types, including journal articles (87,285,913), patents (58,972,869), theses (5,204,930), conference papers (4,803,560), books (4,373,655), book chapters (3,795,548), repositories (1,715,435) and datasets (122,981). We create our paper dataset by selecting the 87 million journal articles, the largest category of scientific papers. We did not combine them with conference papers or theses, as different categories might follow different citation practices that make the calculated disruption score hard to compare. We then select the papers that have two or more authors to focus on teamwork. This leaves us with 58 million papers. We also restrict our sample to papers for which all scientists have provided their affiliation information, so we can retrieve author cities and distinguish between on-site and remote teams. This leaves us with 22 million papers. Finally, we keep the papers for which each author provides only one affiliation to ensure that the retrieved location information is precise. We are left with 20 million papers.

###### Identifying on-site and remote teams underlying research articles and patent applications

Scientific research teams.Microsoft Academic Graph (MAG) provides name-disambiguated authors (22,566,650) and institutions (22,679) of papers, utilizing verified machine learning models38. The latitude and longitude values of these institutions are also provided, such as the University of Pittsburgh (latitude 40.4445648, longitude −79.95328) or Carnegie Mellon University” (latitude 40.44332, longitude −79.94358). However, we also verify the quality of MAG’s name disambiguation of scientists. Specifically, we selected a random sample of 50 researchers who published 873 papers. Then, two human coders were used to examine a random sample of 30 papers. All examined papers are confirmed to be correctly assigned, implying 100% accuracy. We also compared all of the 873 papers against self-reported publication records downloaded from ORCID and calculated the average recall across 50 scientists as 84%. Again, we used two human coders to verify the quality of MAG’s name disambiguation on institutions and their geographical coordinates, indicating 99% accuracy on the same dataset. Only one incorrect linkage was identified from 131 author–location pairs across 30 papers; the author was assigned to the right research institution but the wrong local branch.

We also experimented with four different versions of the distance threshold to distinguish between on-site teams (that is, teams with a collaboration distance equalling or below the threshold) and remote teams (with a collaboration distance above the threshold), including 0 km, 1 km, 5 km and 10 km. Specifically, we consistently map scientists to cities before calculating the geographical distance between them. Therefore, these different distance thresholds apply to the distance between cities. We find that the reduced disruption in remote teams is robust across these thresholds. For simplicity, we use the 0 km measure, meaning that all team members are in the same location. We use this definition of on-site teams throughout the paper unless specified otherwise. We note that although there are nearly an order of magnitude fewer patents than papers, there are more than an order of magnitude more patenting cities than paper-producing cities. The main reason why the patent dataset contains less teamwork but more cities is that paper authors are highly concentrated in universities, which cluster in large cities or campus towns. By contrast, the greater geographical span of patenting reflects that industry is more dispersed than academia. To ensure the quality of both datasets, we verified that the identified 87,937 patenting cities are all unique addresses—which excludes the possibility that their total number is incorrectly inflated owing to repeated records. We also find that the patenting cities span not only most (95%) of the large cities and campus towns included in the 3,562 paper-producing cities, but also many other smaller towns that are not included (for example, in Central Africa). Of the patents

After these verifications, we map the 22,679 institutions to 3,562 cities using the GeoPy API (https://github.com/geopy/geopy). We calculate the geographic distance between co-authors using the geographic coordinates of cities instead of institutions, so that we identify team members from the same city as on-site, regardless of city size and the distance between institutions within the city. This way, the collaboration distance between a scientist from the University of Pittsburgh and another from Carnegie Mellon University is 0 km, as both institutions are located in Pittsburgh, PA. By contrast, the collaboration distance between a scientist from the University of Pittsburgh and a team member from the Massachusetts Institute of Technology is 916 km, representing the geographic distance between the centres of Pittsburgh, PA, and Cambridge, MA. Of the papers studied, 68% of authors are in the same city, and 32% are distributed across cities. Among remote teams,

examined, 25% of authors are in the same city, and 75% are distributed across cities. Among remote teams, 70% of our sample have a collaboration distance of 0–200 km, and 7%, 3% and 20% of the patents have a collaboration distance of 200–400 km, 400–600 km and more than 600 km, respectively.

nineteen top-level MAG field-of-study labels such as Mathematics, Biology and Chemistry, if they have published three or more papers over half of which are within a single field of study. We then distinguish monodisciplinary teams, for which all team members are from the same home discipline, from interdisciplinary teams, for which team members are from different disciplines. Across the 7,883,633 research teams for which this variable was constructed, we find that the probability of interdisciplinary collaboration is higher in remote teams than in on-site teams (35.6% versus 28.9%). Leveraging the Cooperative Patent Classification classification, we apply the same computational method to patent applications and construct disciplinary and interdisciplinary labels for 1,752,307 innovating teams. Again, remote teams outperform on-site teams in interdisciplinary collaboration (19.3% versus 19.2%). These findings support the view that remote teams are more heterogeneous than on-site teams1,14,16.

###### CalculatingD scores

Subsequent research can reference the primary work in three ways: (i) citing only the focal work, (j) citing both the focal work and its references, or (k) citing only the references. The ‘disruption’ orD score of a focal paper, denoted asD, can be quantified by analysing the divergence between two categories of subsequent papers:

D= pi − pj = (ni − nj)/(ni + nj + nk)

in whichpiis the proportion of papers solely referencing the focal paper without including its references, and pj is the proportion of papers that reference both the focal paper and its associated references. A paper may disrupt earlier research by introducing new ideas that come to be recognized independently from the previous work (0 < D < 1), develop existing research by providing supportive evidence or extensions that come to be recognized as incremental additions to previous work (−1 < D < 0), or remain neutral, meaning that the disruptive and developmental character of its contribution balances out (D = 0).

###### Quantifying tie strength within research and innovation teamwork

We construct a social network comprising 22,566,650 scientists and 67,226,924 co-authoring relationships using our dataset of research articles. Following a recent study40, we calculate the strength of the tie between two scientists as the ratio of their common collaborators to their total collaborators. This measure, in other words, defines tie strength as the extent to which two scientists share their collaborators. However, one limitation of this approach is that it may overrate the tie strength between pairs of scientists who published only one or two papers with the same set of co-authors. To address this issue (and for consistency with our analysis of knowledge diversity), we focus on scientists who published three or more papers, over half of which are within a single field of study, when calculating the tie strength. We then distinguish weak ties (below the median) from strong ties (above the median). If a team contains one or more weak ties between co-authors, we label this team as a weak-tie collaboration. Doing so, we find that the probability of weak-tie collaboration is higher in remote teams than in on-site teams (94.4% versus 82.1%). Leveraging the same computational model, we calculate tie strength on the social network comprising 2,732,326 inventors and 10,476,225 co-authoring relationships using our dataset of patent applications. Again, the probability of weak-tie collaboration is higher for remote teams than on-site teams (76.4% versus 73.1%). These observations support the view that remote teams include more knowledge brokers and weak ties than on-site teams1,14.

###### Quantifying time-zone differences underlying inventive teamwork

For 20,273,444 papers and 3,709,940 patents, we map the time zone of each team member from the latitude and longitude values of their respective cities using PYTZ, a Python API (pytz.sourceforge.net/). We then calculate the hour differences between these time zones. For each team, we calculate the average time-zone difference between all pairs of team members as a proxy for the underlying temporal separation.

###### Identifying the fields of study for research articles and patent applications

Research articles. We rely on the scientific taxonomy published by the MAG team, consisting of a six-level hierarchy. The level-zero labels cover 19 research fields, such as Mathematics, Biology and Chemistry, the level-one labels cover 292 subfields, and level-two to level-five labels contain 543,454 unique keywords or phrases. Each MAG paper is linked to one or more labels through a machine learning model developed and verified by the MAG team39. Within a paper, each label is also associated with a probability value between zero and one that reflects the confidence level of machine prediction. In our analysis, we use the level-zero label of each paper, and if a paper has two or more labels, we select the one with the highest confidence level.

###### Evaluating the robust, negative relationship between remote teams and disruption

We run several regressions to evaluate the negative relationship between remote teams and disruption. From our dataset of scientific teams, we selected 7,681,669 scientists who published two or more papers. These scientists have published 13,711,470 papers between 1960 and 2020, which yields 45,078,179 paper–author records. We use this dataset to build stepwise regression models and explore the relationship between remote collaboration (the value equals one if the team members are spread across cities, and zero otherwise) and disruption, starting from a model without any control variables or fixed effects. We then add controls for team size, period, average career age, knowledge diversity, tie strength, the field of study and author fixed effects. These linear models, inspired by previous studies41, confirm that remote teams are consistently less disruptive than on-site teams for papers (Extended Data Table 1). From our dataset of patenting teams, we selected 1,253,090 inventors who filed two or more patents. These inventors have filed 2,903,964 patents between 1976 and 2020, which yields 9,031,126 patent–author records. We use this dataset to build stepwise regression models in the same way as mentioned above. Among patents, we confirm a robust, negative relationship between remote teams and disruption when control variables and author fixed effects are included (Extended Data Table 2). Finally, we show that the

Patent applications. The technological taxonomy included in the PatentsView data is the Cooperative Patent Classification, a four-level classification system. The level-zero labels have nine sections, including, for example, “Mechanical Engineering; Lighting; Heating; Weapons; Blasting” in Section F and “Performing Operations; Transporting” in Section B. Under these nine sections, the Cooperative Patent Classification also provides 128 subsections, 666 groups and 229,109 subgroups. Each patent has several labels that may span across these four levels. For each patent, we first assign all labels to one of the nine section labels at level zero and then select the most popular section label.

###### Quantifying knowledge diversity of inventive teamwork

We calculate the interdisciplinarity of team members and use it as a proxy for the diversity of knowledge to which the team has access. This allows us to account for team heterogeneity in our regression analysis (Extended Data Tables 1 and 2). To construct this measure for research articles, we first identify the ‘home discipline’ of a scientist from the

lower innovative performance of remote teams is robust against the interaction between the remote collaboration and periods.

author; contribution to topics, defined as the overlap between MAG topic keywords for the focal paper and all keywords across previously published papers for each author; contribution to leading the research, defined as the probability of being the first author(s); contribution to managing correspondence and presentation, defined as the probability of being the corresponding author(s); career age, defined as the number of years from the first publication to the publication of the focal paper for a given author; citation impact, defined as the total number of citations an author has received to all previous publications; topic diversity, defined as the total number of unique MAG topic keywords across previous publications; and publication productivity, defined as the total number of previous papers until the publication of the focal paper. The missing papers did not have these variables for all authors. The machine learning model gives a precision of 0.79 and a recall of 0.793 in predicting author roles. The predicted and empirical values of the fraction of conceptual workers in ground-truth data are highly correlated (Pearson correlation coefficient 0.66,P value < 0.001). Analysing these inferred author roles, we find that remote team members are less likely to contribute to conceptual work than their peers in on-site teams (42% versus 48%) and, correspondingly, more likely to contribute to technical work.

###### Identifying author contributions to scientific papers

Our author contribution data cover 89,575 contribution disclosures collected from the website of four journals, includingNature,Science, Proceedings of the National Academy of Sciences of the United States of America and PLOS ONE, between 2003 and 2020. Following existing studies22,42, we identify four functional research activities from contribution statements using natural language processing techniques, including conceiving research, writing the paper, carrying out experiments and analysing data. We then link authors with their contributions classified into these four categories. We also note that these four categories cohere into two broad roles, including: conceptual work leaders, who conceive research and write papers; and technical work supporters, who carry out experiments and analyse data.

###### Evaluating the robust, negative relationship between remote teams and conceiving research

To investigate how scientists interact differently when the collaboration distance between them increases, we compare the team role of the same scientists when in on-site and remote teams. For 21,373 scientists who published both on-site and remote team papers, their average probability of contributing to conceiving research is 63% in on-site teams and 51% in remote teams. We confirm that this decline is statistically significant (P value < 0.001 for the Student’s t-test). For comparison, their probability of writing the paper and analysing data decreased by 11% (from 60% to 49%, P value < 0.001) and 8% (from 58% to 50%, P value < 0.001), respectively, whereas the probability of carrying out experiments increased by 1% (from 42% to 43%, P value < 0.05), when switching from on-site to remote collaboration.

###### Examining alternative explanations for the reduced disruption of remote teams

We also consider several alternative explanations for the negative relationship between collaboration distance and idea disruptiveness.

Team size effect. Previous work has shown that large teams are less likely to make disruptive discoveries22,25. This finding raises the concern that systematic size differences between remote and on-site teams might drive our results, not least if remote teams have grown faster over the investigated period. In response to this concern, we first compare the size of remote and on-site teams over time and confirm that the size of remote teams has grown faster than on-site teams for both papers and patents. Specifically, the average team size increased by 100% (from 2.6 to 5.2) among remote teams but only by 65% among on-site teams (from 2.6 to 4.3) in papers. The same pattern holds for patents: the average team size increased by 40% (from 2.7 to 3.9) among remote teams, but it only increased by 32% among on-site teams (from 2.5 to 3.3). However, we also find that accounting for both team size and periods in our regression models does not alter the negative coefficient of remote teams (Extended Data Tables 1 and 2). These findings lead us to conclude that the difference in average team size or growth rate is unlikely to fully explain the observed differences in inventive output between on-site and remote teams.

We next verify the relationship between this role shift—from leading conceptual tasks to delivering technical tasks—and collaboration distance in three ways. First, among the 21,373 scientists who worked in both on-site and remote teams, our regression analysis confirms the robustness of their role change when fields, periods and team sizes are accounted for (Extended Data Table 3). Doing so, we note that the reduced engagement in conceptual tasks in remote teams cannot be explained by their larger team size, distinct research fields or time periods.

Second, to assess the impact of collaboration distance on team roles, we conducted a team-split analysis of the same group of scientists who repeatedly collaborated before and after team members moved. For 15,294 pairs of scientists, across all team sizes, who collaborated in both on-site and remote teams, their probability of jointly contributing to conceiving research decreases from 33.5% in on-site teams to 28.3% in remote teams (P value < 0.001). The reduction in co-conceiving probability is robust when fields, periods and team sizes are accounted for (Extended Data Table 4). For 2,343 groups of three or more scientists who published in both on-site and remote teams, their probability of contributing to conceiving research is 21.6% in on-site teams and 17.8% in remote teams (P value < 0.01).

Team composition effect.Remote teams might also differ from on-site teams in their composition of diverse expertise. Previous research has suggested that remote teams might be more heterogeneous, as geographically distant ties serve as channels for diverse knowledge1,14,16. From this perspective, the reduced disruptiveness of remote teams could simply reflect the challenge of integrating more diverse knowledge, regardless of distance. To address this concern, we calculate team member interdisciplinarity and use it as a proxy for diverse knowledge to which the team members have access. We confirm that remote teams are more heterogeneous than on-site teams1,14,16. We then include the constructed variable in our regression models and find that the negative impact of remote teams on disruption remains intact (Extended Data Tables 1 and 2). We conclude that differences in team heterogeneity are unlikely to explain the observed difference between on-site and remote teams.

Third, we build machine learning models that effectively infer team roles for papers with implicit author contributions to examine whether the difference in team roles between on-site and remote teams holds in a much larger sample. Specifically, using our data of author contributions, we train a neural network to infer the two distinct author roles of interest—that is, leading conceptual tasks and delivering technical tasks—across 16,397,750 papers. These papers are selected from the 20,134,803 papers in our sample, with the criteria for selection being that each selected paper contains variables that are used in the machine learning model. Specifically, we use eight different variables to predict the dichotomy of author roles, including the following: contribution to references, defined as the overlap between references of the focal paper and all references across previously published papers for each

Age effect. Previous research has associated the innovation performance of scientists with their age. On the one hand, if acquiring a certain amount of knowledge is a prerequisite for a breakthrough10, then age

and working experience are likely to contribute towards more important discoveries. On the other hand, ageing scholars might experience ‘cognitive entrenchment’23, and established scholars could become gatekeepers against new ideas24,43. In both scenarios, the age differences between remote and on-site teams present a potential cofounder against collaboration distance underlying the reduced disruptiveness of remote teams. Consistent with this reasoning, on-site team members have lower career ages than remote team members on average (9.6 versus 11.8), possibly reflecting a greater prominence of student–adviser relationships among on-site teams. However, when we include career age in our regression analysis, the negative impact of remote teams on disruption remains unchanged. We conclude that the age structure of remote and on-site teams cannot account for our key findings.

diverse knowledge through weak ties, they fail to exchange, fuse and integrate that knowledge to generate disruptive ideas.

###### Reporting summary

Further information on research design is available in the Nature Portfolio Reporting Summary linked to this article.

#### Data availability

The datasets used in this paper are available at https://lyl010.github.io/ and https://doi.org/10.6084/m9.figshare.21295725. Source data are provided with this paper.

#### Code availability

Selection bias. Another possibility is that more creative scientists are part of on-site teams rather than remote teams. If this is true, the observed reduced disruptiveness of remote teams originates from differences in individual characteristics rather than from individuals interacting and collaborating in different ways in remote and on-site teams. To that end, we note that the same scientists act differently across team contexts—they are more likely to conceive research and write papers in on-site teams, and more likely to carry out experiments and analyse data in remote teams, as Fig. 4a shows. Second, to further mitigate concerns over selection bias, we run author fixed effects regressions and confirm that the negative impact of remote teams is still statistically significant (Extended Data Tables 1 and 2), although the magnitude of the coefficient is reduced, possibly because less disruptive scholars end up at more marginal universities, where they benefit more from the opportunities for remote collaboration. We conclude that selection or individual differences cannot fully explain the observed difference between on-site and remote teams.

All code is available at https://lyl010.github.io/.

- 38. Wang, K. et al. Microsoft Academic Graph: when experts are not enough. Quant. Sci. Stud. 1, 396–413 (2020).
- 39. Shen, Z., Ma, H. & Wang, K. A Web-scale system for scientific knowledge exploration. In Proc. ACL 2018, System Demonstrations 87–92 (Association for Computational Linguistics, 2018); https://aclanthology.org/P18-4015/.
- 40. Rajkumar, K., Saint-Jacques, G., Bojinov, I., Brynjolfsson, E. & Aral, S. A causal test of the strength of weak ties. Science 377, 1304–1310 (2022).
- 41. Kaltenberg, M., Jaffe, A. B. & Lachman, M. The Age of Invention: Matching Inventor Ages to Patents Based on Web-Scraped Sources Working Paper 28768 (NBER, 2021); https://www. nber.org/papers/w28768.
- 42. Haeussler, C. & Sauermann, H. Division of labor in collaborative knowledge production: the role of team size and interdisciplinarity. Res. Policy 49, 103987 (2020).
- 43. Cui, H., Wu, L. & Evans, J. A. Aging scientists and slowed advance. Preprint at https://arxiv. org/abs/2202.04044 (2022).
- 44. Granovetter, M. S. The strength of weak ties. Am. J. Sociol. 78, 1360–1380 (1973).
- 45. Mors, M. L. & Waguespack, D. M. Fast success and slow failure: the process speed of dispersed research teams. Res. Policy 50, 104222 (2021).
- 46. Correia, S. Correia S. reghdfe: Estimating linear models with multi-way fixed effects. 2016 Stata Conference https://econpapers.repec.org/paper/bocscon16/24.htm (2016).


Weak-tie effect.Remote teams are likely to include more distant, weak ties44 between team members than on-site teams. However, the impact of these weak ties on innovative performance remains unclear. On the one hand, brokers (that is, people with diverse and distant contacts) tend to contribute to team innovation because they have access to more diverse knowledge14,40. On the other hand, these brokers also tend to do worse in gathering the support or interest of their colleagues in delivering innovative ideas1. To explore the role of weak ties in team innovation, we quantified tie strength in both publishing and patenting teams and confirmed that remote teams include more weak ties than on-site teams1,14. We then include a binary variable of weak-tie collaboration in our regression model and confirm that although weak ties are associated with more disruptive discoveries, the negative relationship between distance and disruption remains intact (Extended Data Tables 1 and 2). Hence, even although remote teams have access to more

AcknowledgementsWe thank F. Xu, J. A. Evans, F. Neffke, J. Huang, G. Presidente, H. Youn, Y. Lin,

M. Frank and S. Bana for helpful comments or discussions. We are grateful for support from Citi, the Dieter Schwarz Foundation (C.B.F.), the Richard King Mellon Foundation, the Alfred P. Sloan Foundation and the National Science Foundation grant SOS:DCI 2239418 (L.W.).

Author contributionsY.L., C.B.F. and L.W. collaboratively conceived and designed the study, contributed to the interpretation of data, and drafted, revised and edited the manuscript. Y.L. analysed the data and implemented the models.

Competing interestsThe authors declare no competing interests.

Additional information Supplementary informationThe online version contains supplementary material available at https://doi.org/10.1038/s41586-023-06767-1. Correspondence and requests for materials should be addressed to Carl Benedikt Frey or Lingfei Wu. Peer review information Nature thanks Melanie Brucks and the other, anonymous, reviewer(s) for their contribution to the peer review of this work. Reprints and permissions informationis available at http://www.nature.com/reprints.

![image 6](Lin et al._2023_Remote collaboration fuses fewer breakthrough ideas_images/imageFile6.png)

- Extended Data Fig. 1 | The robust, negative relationship between collaboration distance and disruption probability against team sizes, periods, and fields. For 20,134,803 research papers published between 1960 and 2020, and 4,060,564 patent applications filed between 1976 and 2020, we show that the negative association between collaboration distance and the probability of producing disruptive work (D > 0) is robust against team sizes (a,d), team periods (b,e), and fields of study (c,f). For each value of the controlled variable (e.g., team size equals two for the blue curve in Panel a), the gray dotted line marks the average disruption probability across all distances. We then


display the relative probability of disruption (colored curves), calculated as the ratio of disruption probability for the group of given collaboration distance to the average probability across all distances. The plotted curves have been normalized by dividing their raw values by the group mean, so that the intercepts are not meaningful. We note that Panels b and e appear to show that the remote penalty has strengthened after 2000. However, this effect is confounded by the increase in team size over this time period. See Extended Data Table 1–2 for the effect of distance on innovation when a host of control variables are accounted for.

![image 7](Lin et al._2023_Remote collaboration fuses fewer breakthrough ideas_images/imageFile7.png)

- Extended Data Fig. 2 | Verifying the lower performance of remote teams using alternative measures of collaboration distance. For 20,134,803 research papers published between 1960 and 2020, and 4,060,564 patent applications filed between 1976 and 2020, we calculate three different, alternative measures of collaboration distance other than our main specification—the average geographic distance between team members. These include the maximum distance between team members34 (a); the average distance between the unique cities where team members are located (b); and a colocation index varying from zero to one, which measures the


probability that a randomly selected pair of team members are in the same location45 (c). This colocation index is a continuous variable that complements the binary measures of onsite and remote teams, as it captures boundary cases where some but not all members of a remote team are onsite. In Panela–c, the gray dotted lines mark the average disruption probability for papers and patents across all distances. The colored curves (or bars) mark the relative probability of disruption, calculated as the ratio of disruption probability for the analyzed group to the average probability across all distances.

![image 8](Lin et al._2023_Remote collaboration fuses fewer breakthrough ideas_images/imageFile8.png)

- Extended Data Fig. 3 | Verifying the lower performance of remote teams using alternative measures of innovation. For 20,134,803 research papers published between 1960 and 2020, and 4,060,564 patent applications filed between 1976 and 2020, we calculate two alternative measures of innovation and find that remote teams are consistently less likely to disrupt science and technology than onsite teams. The percentile of the averageD-score falls from 89 to 84 for papers (a) and from 76 to 67 for patents (b) across the full sample.


The probability of proposing new scientific concepts decreases from 0.40% to 0.32% for papers and the probability of introducing new technology codes decreases from 3.33% to 3.22% for patents, when switching from onsite to remote (c). The gray dotted line marks the probability of introducing new concepts or code for an average paper (0.37%) or patent (3.24%). The color bars show the relative probability, calculated as the ratio of probability for the analyzed group relative to the population’s average probability.

![image 9](Lin et al._2023_Remote collaboration fuses fewer breakthrough ideas_images/imageFile9.png)

- Extended Data Fig. 4 | Onsite teams conceive, and remote teams perform. We analyzed 89,575 author contribution disclosures underlying papers across four journals, includingNature,Science,PNAS, andPLOS ONE, between 2003 and 2020. We associate authors with their contribution to four research activities, including “conceiving research,” “performing experiments,” “analyzing data,” and “writing the paper.” For each of the 21,373 scientists who worked in both onsite and remote teams, we track the distribution of their contributions across four activities within each paper and average this distribution within the onsite-team and remote-team papers they published, respectively. This way, we obtained two distributions for each scientist. We then averaged these two distributions across all the 21,373 scientists in our sample. Finally, we displayed the obtained distributions using the Gaussian kernel density estimate. We observe that the key contribution of the same scientist, marked by the peak of the density curves, shifted from “conceiving research” to “performing experiments” when they switched from onsite to remote. These two distributions are significantly different from each other (Chi-squared test statistic = 3188, p-value < 0.001).


![image 10](Lin et al._2023_Remote collaboration fuses fewer breakthrough ideas_images/imageFile10.png)

- Extended Data Fig. 5 | Different scaling patterns of conceptual and technical activities. Our author contribution data covers disclosures from PNAS (18,354),Nature (9,364),Science (1,176), andPLOS ONE (60,681) between 2003 and 2020. We select PNAS (a) andPLOS ONE (b), which have the most observations, and explore the distinct scalability of engagement across research activities. We group four research activities into two broad categories according


to their different scalability, including 1) conceptual tasks that contain conceiving and writing, which scale up slowly with team size (red curves), and 2) technical tasks comprising performing and analyzing, which scale up fast with team size (blue curves). As shown in the insets, while the fraction of performing members stabilizes at 0.6 as the team size increases from two to ten, the fraction of conceiving members even decreases from 0.9 to 0.4.

![image 11](Lin et al._2023_Remote collaboration fuses fewer breakthrough ideas_images/imageFile11.png)

- Extended Data Fig. 6 | Inferring conceptual and technical activities. Using the ground-truth dataset mentioned in Extended Data Fig. 5, we train a neural-network model to infer these two author roles within 16,397,750 papers where author contributions are not explicit. This machine learning model uses eight different variables to predict the dichotomy of author roles, including


1) contribution to references, defined as the overlap between references of the focal paper and all references across previously published papers for each author; 2) contribution to topics, defined as the overlap between MAG topic keywords for the focal paper and all keywords across previously published papers for each author; 3) contribution to leading the research, defined as the probability of being the first author(s); 4) contribution to managing correspondence and presentation, defined as the probability of being the corresponding author(s); 5) career age, defined as the number of years from the first publication to the publication of the focal paper for a given author,

- 6) citation impact, defined as the total number of citations an author has received to all previous publications; 7) topic diversity, defined as the total number of unique MAG topic keywords across previous publications, and finally; 8) publication productivity, defined as the total number of previous papers until the publication of the focal paper. The machine learning model gives a precision of 0.790 and a recall of 0.793. The predicted and empirical values of the fraction of conceptual workers are highly correlated (Pearson correlation coefficient 0.66, P-value < 0.001). The eight predictors and their contribution to the prediction are displayed. The figure is reproduced from our earlier research22.


##### Extended Data Table 1 | Assessing the robustness of declined disruption with increased collaboration distance in science

![image 12](Lin et al._2023_Remote collaboration fuses fewer breakthrough ideas_images/imageFile12.png)

From our dataset of scientific teams, we selected 7,681,669 scientists who published two or more papers. These scientists have published 13,711,470 papers between 1960 and 2020, yielding 45,078,179 paper-author records. We use this dataset to build stepwise regression models and explore the robustness of the relationship between remote collaboration (the value equals one if team members spread across cities, zero otherwise) and disruption, starting from a model without any controls, and then adding team size, time period, average career age, knowledge diversity, tie strength, the field of study, author fixed effects, and finally, an interaction term between time and remote. We note that the remote work penalty—the negative relationship between remote collaboration and disruption—is robust across all specifications. When teams move from 0 km to more than 600 km collaboration distance, for example, the predicted disruption probability, holding other variables constant, declines from 20.4% to 19.5% (p-value < 0.001 for two-side Student’s t-test), or 4.4% in relative terms. Note: All statistical tests are two-sided t-test and no adjustments were made for multiple comparisons. For Model 5-7, standard errors (in parentheses) are clustered at the author level. * p < 0.05;

** p-value < 0.01; *** p-value < 0.001. We used the REGHDFE package in STATA1646 to implement the fixed-effects regressions.

##### Extended Data Table 2 | Assessing the robustness of declined disruption with increased collaboration distance intechnology

![image 13](Lin et al._2023_Remote collaboration fuses fewer breakthrough ideas_images/imageFile13.png)

From our dataset of patenting teams, we selected 1,253,090 inventors who filed two or more patents. These inventors have filed 2,903,964 patents between 1976 and 2020, yielding 9,031,126 patent-author records. We use this dataset to build stepwise regression models in the same way as for scientific teams. We note that the remote work penalty—the negative relationship between remote collaboration and disruption—is robust across all specifications. When teams move from 0 km to more than 600 km collaboration distance, for example, the predicted disruption probability, holding other variables constant, declines from 58.2% to 56.5% (p-value < 0.001), or 2.9% in relative terms. Note: All statistical tests are two-sided t-test and no adjustments were made for multiple comparisons. For Model 5-7, standard errors (in parentheses) are clustered at the inventor level.

* p < 0.05; ** p-value < 0.01; *** p-value < 0.001. We used the REGHDFE package in STATA1646 to implement the fixed-effects regressions.

##### Extended Data Table 3 | Assessing the robustness of the reduced probability of conceiving research for the same scientistwhen switching from onsite to remote

![image 14](Lin et al._2023_Remote collaboration fuses fewer breakthrough ideas_images/imageFile14.png)

From our dataset of author contributions, we select 21,373 scientists who worked in both onsite and remote teams. These authors published 31,815 papers in total, which gives us 65,143 paper-author records. Using author-fixed effect regressions41,46, we find that the same scientist is less likely to conceive research and more likely to perform experiments when switching from onsite to remote, when fields, periods, and team sizes are accounted for. Note: All statistical tests are two-sided t-test and no adjustments were made for multiple comparisons. For Model 1-2, standard errors (in parentheses) are clustered at the author level. * p < 0.05;

** p-value < 0.01; *** p-value < 0.001. We used the REGHDFE package in STATA1646 to implement the fixed-effects regressions.

##### Extended Data Table 4 | Assessing the robustness of the reduced probability of co-conceiving research for the same pair ofscientists when switching from onsite to remote

![image 15](Lin et al._2023_Remote collaboration fuses fewer breakthrough ideas_images/imageFile15.png)

From our dataset of author contributions, we select 15,294 pairs of scientists who collaborate in both onsite and remote teams. These pairs of authors published 11,313 papers in total, which leaves us with 36,253 paper-author-pair records. Using fixed effect regressions to control the difference between author pairs41,46, we confirm that the same pair of scientists are less likely to co-conceive research and more likely to co-perform experiments when switching from onsite to remote, when fields, periods, and team sizes are accounted for. Note: All statistical tests are two-sided t-test and no adjustments were made for multiple comparisons. For Model 1-2, standard errors (in parentheses) are clustered at the author-pair level.

* p < 0.05; ** p-value < 0.01; *** p-value < 0.001. We used the REGHDFE package in STATA1646 to implement the fixed-effects regressions.

![image 16](Lin et al._2023_Remote collaboration fuses fewer breakthrough ideas_images/imageFile16.png)

