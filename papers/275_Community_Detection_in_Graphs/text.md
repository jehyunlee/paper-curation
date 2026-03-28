#### arXiv:0906.0612v2[physics.soc-ph]25 Jan 2010

###### Community detection in graphs

Santo Fortunato∗

Complex Networks and Systems Lagrange Laboratory, ISI Foundation, Viale S. Severo 65, 10133, Torino, I-ITALY.

The modern science of networks has brought signiﬁcant advances to our understanding of complex systems. One of the most relevant features of graphs representing real systems is community structure, or clustering, i. e. the organization of vertices in clusters, with many edges joining vertices of the same cluster and comparatively few edges joining vertices of diﬀerent clusters. Such clusters, or communities, can be considered as fairly independent compartments of a graph, playing a similar role like, e. g., the tissues or the organs in the human body. Detecting communities is of great importance in sociology, biology and computer science, disciplines where systems are often represented as graphs. This problem is very hard and not yet satisfactorily solved, despite the huge eﬀort of a large interdisciplinary community of scientists working on it over the past few years. We will attempt a thorough exposition of the topic, from the deﬁnition of the main elements of the problem, to the presentation of most methods developed, with a special focus on techniques designed by statistical physicists, from the discussion of crucial issues like the signiﬁcance of clustering and how methods should be tested and compared against each other, to the description of applications to real networks.

###### Contents

- I. Introduction 2
- II. Communities in real-world networks 4
- III. Elements of Community Detection 8

- A. Computational complexity 9
- B. Communities 9

- 1. Basics 9
- 2. Local deﬁnitions 10
- 3. Global deﬁnitions 11
- 4. Deﬁnitions based on vertex similarity 12


- C. Partitions 13


- 1. Basics 13
- 2. Quality functions: modularity 14


- IV. Traditional methods 16

- A. Graph partitioning 16
- B. Hierarchical clustering 19
- C. Partitional clustering 19
- D. Spectral clustering 20


- V. Divisive algorithms 23

- A. The algorithm of Girvan and Newman 23
- B. Other methods 25


- VI. Modularity-based methods 27

- A. Modularity optimization 27

- 1. Greedy techniques 27
- 2. Simulated annealing 29
- 3. Extremal optimization 29
- 4. Spectral optimization 30
- 5. Other optimization strategies 33


- B. Modiﬁcations of modularity 34
- C. Limits of modularity 38


- VII. Spectral Algorithms 41
- VIII. Dynamic Algorithms 43 A. Spin models 43


∗Electronic address: fortunato@isi.it

- B. Random walk 45
- C. Synchronization 47


- IX. Methods based on statistical inference 48

- A. Generative models 49
- B. Blockmodeling, model selection and information theory 52


- X. Alternative methods 54
- XI. Methods to ﬁnd overlapping communities 58

- A. Clique percolation 58
- B. Other techniques 60


- XII. Multiresolution methods and cluster hierarchy 62

- A. Multiresolution methods 63
- B. Hierarchical methods 65


- XIII. Detection of dynamic communities 66
- XIV. Signiﬁcance of clustering 70
- XV. Testing Algorithms 73

- A. Benchmarks 74
- B. Comparing partitions: measures 77
- C. Comparing algorithms 79


- XVI. General properties of real clusters 82
- XVII. Applications on real-world networks 85

- A. Biological networks 85
- B. Social networks 86
- C. Other networks 88


- XVIII. Outlook 90


A. Elements of Graph Theory 92

- 1. Basic Deﬁnitions 92
- 2. Graph Matrices 94
- 3. Model graphs 94


References 96

###### I. INTRODUCTION

The origin of graph theory dates back to Euler’s solution of the puzzle of K¨nigsberg’s bridges in 1736 (Euler, 1736). Since then a lot has been learned about graphs and their mathematical properties (Bollobas, 1998). In the 20th century they have also become extremely useful as representation of a wide variety of systems in diﬀerent areas. Biological, social, technological, and information networks can be studied as graphs, and graph analysis has become crucial to understand the features of these systems. For instance, social network analysis started in the 1930’s and has become one of the most important topics in sociology (Scott, 2000; Wasserman and Faust, 1994). In recent times, the computer revolution has provided scholars with a huge amount of data and computational resources to process and analyze these data. The size of real networks one can potentially handle has also grown considerably, reaching millions or even billions of vertices. The need to deal with such a large number of units has produced a deep change in the way graphs are approached (Albert and Barab´si, 2002; Barrat et al.,

- 2008; Boccaletti et al., 2006; Mendes and Dorogovtsev, 2003; Newman, 2003; Pastor-Satorras and Vespignani,

- 2004). Graphs representing real systems are not regular like,


e. g., lattices. They are objects where order coexists with disorder. The paradigm of disordered graph is the random graph, introduced by P. Erd¨s and A. Re´nyi (Erd¨s and R´enyi, 1959). In it, the probability of having an edge between a pair of vertices is equal for all possible pairs (see Appendix). In a random graph, the distribution of edges among the vertices is highly homogeneous. For instance, the distribution of the number of neighbours of a vertex, or degree, is binomial, so most vertices have equal or similar degree. Real networks are not random graphs, as they display big inhomogeneities, revealing a high level of order and organization. The degree distribution is broad, with a tail that often follows a power law: therefore, many vertices with low degree coexist with some vertices with large degree. Furthermore, the distribution of edges is not only globally, but also locally inhomogeneous, with high concentrations of edges within special groups of vertices, and low concentrations between these groups. This feature of real networks is called community structure (Girvan and Newman, 2002), or clustering, and is the topic of this review (for earlier reviews see Refs. (Danon et al., 2007; Fortunato and Castellano, 2009; Newman, 2004a; Porter et al.,

- 2009; Schaeﬀer, 2007)). Communities, also called clusters or modules, are groups of vertices which probably share common properties and/or play similar roles within the graph. In Fig. 1 a schematic example of a graph with communities is shown.


Society oﬀers a wide variety of possible group organizations: families, working and friendship circles, villages, towns, nations. The diﬀusion of Internet has also led to the creation of virtual groups, that live on the Web,

FIG. 1 A simple graph with three communities, enclosed by the dashed circles. Reprinted ﬁgure with permission from Ref. (Fortunato and Castellano, 2009). c 2009 by Springer.

like online communities. Indeed, social communities have been studied for a long time (Coleman, 1964; Freeman, 2004; Kottak, 2004; Moody and White, 2003). Communities also occur in many networked systems from biology, computer science, engineering, economics, politics, etc. In protein-protein interaction networks, communities are likely to group proteins having the same speciﬁc function within the cell (Chen and Yuan, 2006; Rives and Galitski, 2003; Spirin and Mirny, 2003), in the graph of the World Wide Web they may correspond to groups of pages dealing with the same or related topics (Dourisboure et al., 2007; Flake et al., 2002), in metabolic networks they may be related to functional modules such as cycles and pathways (Guimer` and Amaral, 2005; Palla et al., 2005), in food webs they may identify compartments (Krause et al., 2003; Pimm, 1979), and so on.

Communities can have concrete applications. Clustering Web clients who have similar interests and are geograﬁcally near to each other may improve the performance of services provided on the World Wide Web, in that each cluster of clients could be served by a dedicated mirror server (Krishnamurthy and Wang, 2000). Identifying clusters of customers with similar interests in the network of purchase relationships between customers and products of online retailers (like, e. g., www.amazon.com) enables to set up eﬃcient recommendation systems (Reddy et al., 2002), that better guide customers through the list of items of the retailer and enhance the business opportunities. Clusters of large graphs can be used to create data structures in order to eﬃciently store the graph data and to handle naviga-

tional queries, like path searches (Agrawal and Jagadish, 1994; Wu et al., 2004). Ad hoc networks (Perkins, 2001), i. e. self-conﬁguring networks formed by communication nodes acting in the same region and rapidly changing (because the devices move, for instance), usually have no centrally maintained routing tables that specify how nodes have to communicate to other nodes. Grouping the nodes into clusters enables one to generate compact routing tables while the choice of the communication paths is still eﬃcient (Steenstrup, 2001).

Community detection is important for other reasons, too. Identifying modules and their boundaries allows for a classiﬁcation of vertices, according to their structural position in the modules. So, vertices with a central position in their clusters, i. e. sharing a large number of edges with the other group partners, may have an important function of control and stability within the group; vertices lying at the boundaries between modules play an important role of mediation and lead the relationships and exchanges between diﬀerent communities (alike to Csermely’s “creative elements” (Csermely, 2008)). Such classiﬁcation seems to be meaningful in social (Burt, 1976; Freeman, 1977; Granovetter, 1973) and metabolic networks (Guimer` and Amaral, 2005). Finally, one can study the graph where vertices are the communities and edges are set between clusters if there are connections between some of their vertices in the original graph and/or if the modules overlap. In this way one attains a coarsegrained description of the original graph, which unveils the relationships between modules 1. Recent studies indicate that networks of communities have a diﬀerent degree distribution with respect to the full graphs (Palla et al.,

- 2005); however, the origin of their structures can be explained by the same mechanism (Pollner et al., 2006).


Another important aspect related to community structure is the hierarchical organization displayed by most networked systems in the real world. Real networks are usually composed by communities including smaller communities, which in turn include smaller communities, etc. The human body oﬀers a paradigmatic example of hierarchical organization: it is composed by organs, organs are composed by tissues, tissues by cells, etc. Another example is represented by business ﬁrms, who are characterized by a pyramidal organization, going from the workers to the president, with intermediate levels corresponding to work groups, departments and management. Herbert A. Simon has emphasized the crucial role played by hierarchy in the structure and evolution of complex

- 1 Coarse-graining a graph generally means mapping it onto a smaller graph having similar properties, which is easier to handle. For this purpose, the vertices of the original graph are not necessarily grouped in communities. Gfeller and De Los Rios have proposed coarse-graining schemes that keep the properties of dynamic processes acting on the graph, like random walks (Gfeller and De Los Rios, 2007) and synchronization (Gfeller and De Los Rios, 2008).


systems (Simon, 1962). The generation and evolution of a system organized in interrelated stable subsystems are much quicker than if the system were unstructured, because it is much easier to assemble the smallest subparts ﬁrst and use them as building blocks to get larger structures, until the whole system is assembled. In this way it is also far more diﬃcult that errors (mutations) occur along the process.

The aim of community detection in graphs is to identify the modules and, possibly, their hierarchical organization, by only using the information encoded in the graph topology. The problem has a long tradition and it has appeared in various forms in several disciplines. The ﬁrst analysis of community structure was carried out by Weiss and Jacobson (Weiss and Jacobson, 1955), who searched for work groups within a government agency. The authors studied the matrix of working relationships between members of the agency, which were identiﬁed by means of private interviews. Work groups were separated by removing the members working with people of diﬀerent groups, which act as connectors between them. This idea of cutting the bridges between groups is at the basis of several modern algorithms of community detection (Section V). Research on communities actually started even earlier than the paper by Weiss and Jacobson. Already in 1927, Stuart Rice looked for clusters of people in small political bodies, based on the similarity of their voting patterns (Rice, 1927). Two decades later, George Homans showed that social groups could be revealed by suitably rearranging the rows and the columns of matrices describing social ties, until they take an approximate block-diagonal form (Homans, 1950). This procedure is now standard. Meanwhile, traditional techniques to ﬁnd communities in social networks are hierarchical clustering and partitional clustering (Sections IV.B and IV.C), where vertices are joined into groups according to their mutual similarity.

Identifying graph communities is a popular topic in computer science, too. In parallel computing, for instance, it is crucial to know what is the best way to allocate tasks to processors so as to minimize the communications between them and enable a rapid performance of the calculation. This can be accomplished by splitting the computer cluster into groups with roughly the same number of processors, such that the number of physical connections between processors of diﬀerent groups is minimal. The mathematical formalization of this problem is called graph partitioning (Section IV.A). The ﬁrst algorithms for graph partitioning were proposed in the early 1970’s.

In a seminal paper appeared in 2002, Girvan and Newman proposed a new algorithm, aiming at the identiﬁcation of edges lying between communities and their successive removal, a procedure that after some iterations leads to the isolation of the communities (Girvan and Newman, 2002). The intercommunity edges are detected according to the values of a centrality measure, the edge betweenness, that expresses the importance of the role

of the edges in processes where signals are transmitted across the graph following paths of minimal length. The paper triggered a big activity in the ﬁeld, and many new methods have been proposed in the last years. In particular, physicists entered the game, bringing in their tools and techniques: spin models, optimization, percolation, random walks, synchronization, etc., became ingredients of new original algorithms. The ﬁeld has also taken advantage of concepts and methods from computer science, nonlinear dynamics, sociology, discrete mathematics.

In this manuscript we try to cover in some detail the work done in this area. We shall pay a special attention to the contributions made by physicists, but we shall also give proper credit to important results obtained by scholars of other disciplines. Section II introduces communities in real networks, and is supposed to make the reader acquainted with the problem and its relevance. In Section III we deﬁne the basic elements of community detection, i. e. the concepts of community and partition. Traditional clustering methods in computer and social sciences, i. e. graph partitioning, hierarchical, partitional and spectral clustering are reviewed in Section IV. Modern methods, divided into categories based on the type of approach, are presented in Sections V to X. Algorithms to ﬁnd overlapping communities, multiresolution and hierarchical techniques, are separately described in Sections XI and XII, respectively, whereas Section XIII is devoted to the detection of communities evolving in time. We stress that our categorization of the algorithms is not sharp, because many algorithms may enter more categories: we tried to classify them based on what we believe is their main feature/purpose, even if other aspects may be present. Sections XIV and XV are devoted to the issues of deﬁning when community structure is signiﬁcant, and deciding about the quality of algorithms’ performances. In Sections XVI and XVII we describe general properties of clusters found in real networks, and speciﬁc applications of clustering algorithms. Section XVIII contains the summary of the review, along with a discussion about future research directions in this area. The review makes use of several concepts of graph theory, that are deﬁned and explained in the Appendix. Readers not acquainted with these concepts are urged to read the Appendix ﬁrst.

###### II. COMMUNITIES IN REAL-WORLD NETWORKS

In this section we shall present some striking examples of real networks with community structure. In this way we shall see what communities look like and why they are important.

Social networks are paradigmatic examples of graphs with communities. The word community itself refers to a social context. People naturally tend to form groups, within their work environment, family, friends.

In Fig. 2 we show some examples of social networks. The ﬁrst example (Fig. 2a) is Zachary’s network of karate

club members (Zachary, 1977), a well-known graph regularly used as a benchmark to test community detection algorithms (Section XV.A). It consists of 34 vertices, the members of a karate club in the United States, who were observed during a period of three years. Edges connect individuals who were observed to interact outside the activities of the club. At some point, a conﬂict between the club president and the instructor led to the ﬁssion of the club in two separate groups, supporting the instructor and the president, respectively (indicated by squares and circles). The question is whether from the original network structure it is possible to infer the composition of the two groups. Indeed, by looking at Fig. 2a one can distinguish two aggregations, one around vertices 33 and 34 (34 is the president), the other around vertex 1 (the instructor). One can also identify several vertices lying between the two main structures, like 3, 9, 10; such vertices are often misclassiﬁed by community detection methods.

Fig. 2b displays the largest connected component of a network of collaborations of scientists working at the Santa Fe Institute (SFI). There are 118 vertices, representing resident scientists at SFI and their collaborators. Edges are placed between scientists that have published at least one paper together. The visualization layout allows to distinguish disciplinary groups. In this network one observes many cliques, as authors of the same paper are all linked to each other. There are but a few connections between most groups.

In Fig. 2c we show the network of bottlenose dolphins living in Doubtful Sound (New Zealand) analyzed by Lusseau (Lusseau, 2003). There are 62 dolphins and edges were set between animals that were seen together more often than expected by chance. The dolphins separated in two groups after a dolphin left the place for some time (squares and circles in the ﬁgure). Such groups are quite cohesive, with several internal cliques, and easily identiﬁable: only six edges join vertices of diﬀerent groups. Due to this natural classiﬁcation Lusseau’s dolphins’ network, like Zachary’s karate club, is often used to test algorithms for community detection (Section XV.A).

Protein-protein interaction (PPI) networks are subject of intense investigations in biology and bioinformatics, as the interactions between proteins are fundamental for each process in the cell (Zhang, 2009). Fig. 3 illustrates a PPI network of the rat proteome (Jonsson et al., 2006). Each interaction is derived by homology from experimentally observed interactions in other organisms. In our example, the proteins interact very frequently with each other, as they belong to metastatic cells, which have a high motility and invasiveness with respect to normal cells. Communities correspond to functional groups, i. e. to proteins having the same or similar functions, which are expected to be involved in the same processes. The modules are labeled by the overall function or the dominating protein class. Most communities are associated to cancer and metastasis, which indirectly shows how im-

23

Zig

15

27

10

Ripplefluke

16 30 34

Wave

|13|
|---|


|20|
|---|


MN23

31

|14|
|---|


Quasi

DN21

|4|
|---|


Feather

|5|
|---|


21 9

DN16

- a
- b


|6|
|---|


33

Gallatin

Mus

|17|
|---|


Jet

19

|3|
|---|


|1|
|---|


Web

|2|
|---|


|7|
|---|


24

Number1 Notch

TR82

29

|11|
|---|


Upbang

SN90

28

|8|
|---|


|22|
|---|


|18|
|---|


Knit

32

26

Beescratch

|12|
|---|


25

DN63

c

SN89

PL

SN100

Oscar

Zap

Agent-based

TR77

Models

SN9

Double

Beak

MN60

Haecksel

Mathematical

Kringel

Ecology

| | |
|---|---|
| | |


SN96

TR99

SN4

TSN103

| | |
|---|---|
| | |


| | |
|---|---|
| | |
| | |


CCL Bumper

Topless

Vau

Fish

Thumper

SN63

Trigger

Zipfel

Grin

Scabs Shmuddel

Statistical Physics

Jonah

Hook

Cross

Whitetip

Fork

Patchback

MN83

MN105

Stripes

Five

TSN83

Structure of RNA

SMN5

TR88

TR120

- FIG. 2 Community structure in social networks. a) Zachary’s karate club, a standard benchmark in community detection. The colors correspond to the best partition found by optimizing the modularity of Newman and Girvan (Section VI.A). Reprinted ﬁgure with permission from Ref. (Donetti and Mu˜noz, 2004). c 2004 by IOP Publishing and SISSA. b) Collaboration network between scientists working at the Santa Fe Institute. The colors indicate high level communities obtained by the algorithm of Girvan and Newman (Section V.A) and correspond quite closely to research divisions of the institute. Further subdivisions correspond to smaller research groups, revolving around project leaders. Reprinted ﬁgure with permission from Ref. (Girvan and Newman, 2002). c 2002 by the National Academy of Science of the USA. c) Lusseau’s network of bottlenose dolphins. The colors label the communities identiﬁed through the optimization of a modiﬁed version of the modularity of Newman and Girvan, proposed by Arenas et al. (Arenas et al., 2008b) (Section XII.A). The partition matches the biological classiﬁcation of the dolphins proposed by Lusseau. Reprinted ﬁgure with permission from Ref. (Arenas et al., 2008b). c 2008 by IOP Publishing.


portant detecting modules in PPI networks is.

Relationships/interactions between elements of a system need not be reciprocal. In many cases they have a precise direction, that needs to be taken into account to understand the system as a whole. As an example we can cite predator-prey relationships in food webs. In Fig. 4 we see another example, taken from technology. The system is the World Wide Web, which can be seen as a graph by representing web pages as vertices and the hyperlinks that make users move from one page to another as edges (Albert et al., 1999). Hyperlinks are directed: if one can move from page A to page B by clicking on a

hyperlink of A, one usually does not ﬁnd on B a hyperlink taking back to A. In fact, very few hyperlinks (less than 10%) are reciprocal. Communities of the web graph are groups of pages having topical similarities. Detecting communities in the web graph may help to identify the artiﬁcial clusters created by link farms in order to enhance the PageRank (Brin and Page, 1998) value of web sites and grant them a higher Google ranking. In this way one could discourage this unfair practice. One usually assumes that the existence of a hyperlink between two pages implies that they are content-related, and that this similarity is independent of the hyperlink direction.

Transcription regulation

Proteasome

Nucleocytoplasm transport

Endo/exonuclease

Vascular endothelial growth factors VEGF

Intracellular signalling cascade

Actinin

Karyopherin docking complex

Myosin

EGF-like domains

Mitotic spindle checkpoint

Laminin

Cell cycle regulation

Breast cancer anti-estrogen resistance

Casein kinase

JAK/STAT cascade

Tubulin

NF-kappaB regulation

Hypoxia inducable factor

TGF-β

Matrix metalloprotease

Nuclear hormone Serpins receptors

Cell cycle / cytokinesis

Peroxisomal proteins

ATP transporter proteins

- FIG. 3 Community structure in protein-protein interaction networks. The graph pictures the interactions between proteins in cancerous cells of a rat. Communities, labeled by colors, were detected with the Clique Percolation Method by Palla et al. (Section XI.A). Reprinted ﬁgure with permission from Ref. (Jonsson et al., 2006). c 2006 by PubMed Central.


Therefore it is customary to neglect the directedness of the hyperlinks and to consider the graph as undirected, for the purpose of community detection. On the other hand, taking properly into account the directedness of the edges can considerably improve the quality of the partition(s), as one can handle a lot of precious information about the system. Moreover, in some instances neglecting edge directedness may lead to strange results (Leicht

and Newman, 2008; Rosvall and Bergstrom, 2008). Developing methods of community detection for directed graphs is a hard task. For instance, a directed graph is characterized by asymmetrical matrices (adjacency matrix, Laplacian, etc.), so spectral analysis is much more complex. Only a few techniques can be easily extended from the undirected to the directed case. Otherwise, the problem must be formulated from scratch.

- FIG. 4 Community structure in technological networks. Sample of the web graph consisting of the pages of a web site and their mutual hyperlinks, which are directed. Communities, indicated by the colors, were detected with the algorithm of Girvan and Newman (Section V.A), by neglecting the directedness of the edges. Reprinted ﬁgure with permission from Ref. (Newman and Girvan, 2004). c 2004 by the American Physical Society.


Edge directedness is not the only complication to deal with when facing the problem of graph clustering. In many real networks vertices may belong to more than one group. In this case one speaks of overlapping communities and uses the term cover, rather than partition, whose standard deﬁnition forbids multiple memberships of vertices. Classical examples are social networks, where an individual usually belongs to diﬀerent circles at the same time, from that of work colleagues to family, sport associations, etc.. Traditional algorithms of community detection assign each vertex to a single module. In so doing, they neglect potentially relevant information. Vertices belonging to more communities are likely to play an important role of intermediation between diﬀerent compartments of the graph. In Fig. 5 we show a network of word association derived starting from the word “bright”. The network builds on the University of South Florida Free Association Norms (Nelson et al., 1998). An edge between words A and B indicates that some people associate B to the word A. The graph clearly dis-

|![image 1](Community Detection in Graphs_images/imageFile1.png)<br><br>Scientist<br><br>Science Astronomy<br><br>Earth<br><br>Space<br><br>Moon<br><br>Star<br><br>Ray<br><br>Intelligent<br><br>Golden<br><br>Glare<br><br>Sun<br><br>Sky Moonlight<br><br>Eyes<br><br>Light Sunshine<br><br>Lit<br><br>Dark<br><br>Brown<br><br>Tan<br><br>Orange<br><br>Yellow Blue<br><br>Color<br><br>Gray<br><br>Black<br><br>Race<br><br>White<br><br>Green<br><br>Red Crayon<br><br>Pink<br><br>Velvet<br><br>Flaslight<br><br>Glow<br><br>Dim<br><br>Gifted<br><br>Genius<br><br>Smart<br><br>Inventor<br><br>Einstein<br><br>Brilliant<br><br>Shine<br><br>Laser<br><br>Telescope Horizon<br><br>Sunset<br><br>Ribbon<br><br>Violet<br><br>Purple<br><br>Beam<br><br>Night<br><br>Intelligence<br><br>Astronomy<br><br>BRIGHT<br><br>Light<br><br>Colors|
|---|


FIG. 5 Overlapping communities in a network of word association. The groups, labeled by the colors, were detected with the Clique Percolation Method by Palla et al. (Section XI.A). Reprinted ﬁgure with permission from Ref. (Palla et al., 2005). c 2005 by the Nature Publishing Group.

plays four communities, corresponding to the categories Intelligence, Astronomy, Light and Colors. The word “bright” is related to all of them by construction. Other words belong to more categories, e.g. “dark” (Colors and Light). Accounting for overlapping communities introduces a further variable, the membership of vertices in diﬀerent communities, which enormously increases the number of possible covers with respect to standard partitions. Therefore, searching for overlapping communities is usually much more computationally demanding than detecting standard partitions.

So far we have discussed examples of unipartite graphs. However, it is not uncommon to ﬁnd real networks with diﬀerent classes of vertices, and edges joining only vertices of diﬀerent classes. An example is a network of scientists and papers, where edges join scientists and the papers they have authored. Here there is no edge between any pair of scientists or papers, so the graph is bipartite. For a multipartite network the concept of community does not change much with respect to the case of unipartite graphs, as it remains related to a large density of edges between members of the same group, with the only diﬀerence that the elements of each group be-

8 9

1

6

- 4 5

6

7

8

9

10

|11|
|---|


|12|
|---|


13

|14|
|---|


|15|
|---|


- 16
- 17


18

1

2

3

4

- 5


3

11

|12|
|---|


2

|13|
|---|


|10|
|---|


|14|
|---|


7

- FIG. 6 Community structure in multipartite networks. This bipartite graph refers to the Southern Women Event Participation data set. Women are represented as open symbols with black labels, events as ﬁlled symbols with white labels. The illustrated vertex partition has been obtained by maximizing a modiﬁed version of the modularity by Newman and Girvan, tailored on bipartite graphs (Barber, 2007) (Section VI.B). Reprinted ﬁgure with permission from Ref. (Barber, 2007).


- c 2007 by the American Physical Society.


long to diﬀerent vertex classes. Multipartite graphs are usually reduced to unipartite projections of each vertex class. For instance, from the bipartite network of scientists and papers one can extract a network of scientists only, who are related by coauthorship. In this way one can adopt standard techniques of network analysis, in particular standard clustering methods, but a lot of information gets lost. Detecting communities in multipartite networks can have interesting applications in, e.g., marketing. Large shopping networks, in which customers are linked to the products they have bought, allow to classify customers based on the types of product they purchase more often: this could be used both to organize targeted advertising, as well as to give recommendations about future purchases (Adomavicius and Tuzhilin, 2005). The problem of community detection in multipartite networks is not trivial, and usually requires ad hoc methodologies. Fig. 6 illustrates the famous bipartite network of Southern Women studied by Davis et al. (Davis et al., 1941). There are 32 vertices, representing 18 women from the area of Natchez, Mississippi, and 14 social events. Edges represent the participation of the women in the events. From the ﬁgure one can see that the network has a clear community structure.

In some of the previous examples, edges have (or can have) weights. For instance, the edges of the collaboration network of Fig. 2b could be weighted by the number of papers coauthored by pairs of scientists. Similarly,

the edges of the word association network of Fig. 5 are weighted by the number of times pairs of words have been associated by people. Weights are precious additional information on a graph, and should be considered in the analysis. In many cases methods working on unweighted graphs can be simply extended to the weighted case.

###### III. ELEMENTS OF COMMUNITY DETECTION

The problem of graph clustering, intuitive at ﬁrst sight, is actually not well deﬁned. The main elements of the problem themselves, i. e. the concepts of community and partition, are not rigorously deﬁned, and require some degree of arbitrariness and/or common sense. Indeed, some ambiguities are hidden and there are often many equally legitimate ways of resolving them. Therefore, it is not surprising that there are plenty of recipes in the literature and that people do not even try to ground the problem on shared deﬁnitions.

It is important to stress that the identiﬁcation of structural clusters is possible only if graphs are sparse, i. e. if the number of edges m is of the order of the number of nodes n of the graph. If m n, the distribution of edges among the nodes is too homogeneous for communities to make sense2. In this case the problem turns into something rather diﬀerent, close to data clustering (Gan et al., 2007), which requires concepts and methods of a diﬀerent nature. The main diﬀerence is that, while communities in graphs are related, explicitly or implicitly, to the concept of edge density (inside versus outside the community), in data clustering communities are sets of points which are “close” to each other, with respect to a measure of distance or similarity, deﬁned for each pair of points. Some classical techniques for data clustering, like hierarchical, partitional and spectral clustering will be discussed later in the review (Sections IV.B, IV.C and IV.D), as they are sometimes adopted for graph clustering too. Other standard procedures for data clustering include neural network clustering techniques like, e. g., self-organizing maps and multi-dimensional scaling techniques like, e. g., singular value decomposition and principal component analysis (Gan et al., 2007).

In this section we shall attempt an ordered exposition of the fundamental concepts of community detection. After a brief discussion of the issue of computational complexity for the algorithms, we shall review the notions of community and partition.

2 This is not necessarily true if graphs are weighted with a heterogeneous distribution of weights. In such cases communities may still be identiﬁed as subgraphs with a high internal density of weight.

A. Computational complexity

The massive amount of data on real networks currently available makes the issue of the eﬃciency of clustering algorithms essential. The computational complexity of an algorithm is the estimate of the amount of resources required by the algorithm to perform a task. This involves both the number of computation steps needed and the number of memory units that need to be simultaneously allocated to run the computation. Such demands are usually expressed by their scalability with the size of the system at study. In the case of a graph, the size is typically indicated by the number of vertices n and/or the number of edges m. The computational complexity of an algorithm cannot always be calculated. In fact, sometimes this is a very hard task, or even impossible. In these cases, it is however important to have at least an estimate of the worst-case complexity of the algorithm, which is the amount of computational resources needed to run the algorithm in the most unfavorable case for a given system size.

The notation O(nαmβ) indicates that the computer time grows as a power of both the number of vertices and edges, with exponents α and β, respectively. Ideally, one would like to have the lowest possible values for the exponents, which would correspond to the lowest possible computational demands. Samples of the Web graph, with millions of vertices and billions of edges, cannot be tackled by algorithms whose running time grows faster than O(n) or O(m).

Algorithms with polynomial complexity form the class P. For some important decision and optimization problems, there are no known polynomial algorithms. Finding solutions of such problems in the worst-case scenario may demand an exhaustive search, which takes a time growing faster than any polynomial function of the system size, e.g. exponentially. Problems whose solutions can be veriﬁed in a polynomial time span the class NP of non-deterministic polynomial time problems, which includes P. A problem is NP-hard if a solution for it can be translated into a solution for any NP-problem. However, a NP-hard problem needs not be in the class NP. If it does belong to NP it is called NP-complete. The class of NP-complete problems has drawn a special attention in computer science, as it includes many famous problems like the Travelling Salesman, Boolean Satisﬁability (SAT), Linear Programming, etc. (Garey and Johnson, 1990; Papadimitriou, 1994). The fact that NP problems have a solution which is veriﬁable in polynomial time does not mean that NP problems have polynomial complexity, i. e., that they are in P. In fact, the question of whether NP=P is the most important open problem in theoretical computer science. NP-hard problems need not be in NP (in which case they would be NPcomplete), but they are at least as hard as NP-complete problems, so they are unlikely to have polynomial complexity, although a proof of that is still missing.

Many clustering algorithms or problems related to

clustering are NP-hard. In this case, it is pointless to use exact algorithms, which could be applied only to very small systems. Moreover, even if an algorithm has a polynomial complexity, it may still be too slow to tackle large systems of interest. In all such cases it is common to use approximation algorithms, i. e. methods that do not deliver an exact solution to the problem at hand, but only an approximate solution, with the advantage of a lower complexity. Approximation algorithms are often non-deterministic, as they deliver diﬀerent solutions for the same problem, for diﬀerent initial conditions and/or parameters of the algorithm. The goal of such algorithms is to deliver a solution which diﬀers by a constant factor from the optimal solution. In any case, one should give provable bounds on the goodness of the approximate solution delivered by the algorithm with respect to the optimal solution. In many cases it is not possible to approximate the solution within any constant, as the goodness of the approximation strongly depends on the speciﬁc problem at study. Approximation algorithms are commonly used for optimization problems, in which one wants to ﬁnd the maximum or minimum value of a given cost function over a large set of possible system conﬁgurations.

B. Communities

1. Basics

The ﬁrst problem in graph clustering is to look for a quantitative deﬁnition of community. No deﬁnition is universally accepted. As a matter of fact, the deﬁnition often depends on the speciﬁc system at hand and/or application one has in mind. From intuition and the examples of Section II we get the notion that there must be more edges “inside” the community than edges linking vertices of the community with the rest of the graph. This is the reference guideline at the basis of most community deﬁnitions. But many alternative recipes are compatible with it. Moreover, in most cases, communities are algorithmically deﬁned, i. e. they are just the ﬁnal product of the algorithm, without a precise a priori deﬁnition.

Let us start with a subgraph C of a graph G, with |C| = nc and |G| = n vertices, respectively. We deﬁne the internal and external degree of vertex v ∈ C, kvint and kvext, as the number of edges connecting v to other vertices of C or to the rest of the graph, respectively. If kvext = 0, the vertex has neighbors only within C, which is likely to be a good cluster for v; if kvint = 0, instead, the vertex is disjoint from C and it should better be assigned to a diﬀerent cluster. The internal degree kintC of C is the sum of the internal degrees of its vertices. Likewise, the external degree kextC of C is the sum of the external degrees of its vertices. The total degree kC is the sum of the degrees of the vertices of C. By deﬁnition, kC = kintC + kextC .

We deﬁne the intra-cluster density δint(C) of the subgraph C as the ratio between the number of internal edges of C and the number of all possible internal edges, i. e.

# internal edges of C nc(nc − 1)/2

δint(C) =

. (1)

Similarly, the inter-cluster density δext(C) is the ratio between the number of edges running from the vertices of C to the rest of the graph and the maximum number of inter-cluster edges possible, i. e.

# inter-cluster edges of C nc(n − nc)

δext(C) =

. (2)

For C to be a community, we expect δint(C) to be appreciably larger than the average link density δ(G) of G, which is given by the ratio between the number of edges of G and the maximum number of possible edges n(n − 1)/2. On the other hand, δext(C) has to be much smaller than δ(G). Searching for the best tradeoﬀ between a large δint(C) and a small δext(C) is implicitly or explicitly the goal of most clustering algorithms. A simple way to do that is, e. g., maximizing the sum of the diﬀerences δint(C) − δext(C) over all clusters of the partition3 (Mancoridis et al., 1998).

A required property of a community is connectedness. We expect that for C to be a community there must be a path between each pair of its vertices, running only through vertices of C. This feature simpliﬁes the task of community detection on disconnected graphs, as in this case one just analyzes each connected component separately, unless special constraints are imposed on the resulting clusters.

With these basic requirements in mind, we can now introduce the main deﬁnitions of community. Social network analysts have devised many deﬁnitions of subgroups with various degrees of internal cohesion among vertices (Moody and White, 2003; Scott, 2000; Wasserman and Faust, 1994). Many other deﬁnitions have been introduced by computer scientists and physicists. We distinguish three classes of deﬁnitions: local, global and based on vertex similarity. Other deﬁnitions will be given in the context of the algorithms for which they were introduced.

- 2. Local deﬁnitions

Communities are parts of the graph with a few ties with the rest of the system. To some extent, they can be considered as separate entities with their own autonomy. So, it makes sense to evaluate them independently

- 3 In Ref. (Mancoridis et al., 1998) one actually computes the intercluster density by summing the densities for each pair of clusters.


Therefore the function to minimize is not exactly C[δint(C) − δext(C)], but essentially equivalent.

of the graph as a whole. Local deﬁnitions focus on the subgraph under study, including possibly its immediate neighborhood, but neglecting the rest of the graph. We start with a listing of the main deﬁnitions adopted in social network analysis, for which we shall closely follow the exposition of Ref. (Wasserman and Faust, 1994). There, four types of criteria were identiﬁed: complete mutuality, reachability, vertex degree and the comparison of internal versus external cohesion. The corresponding communities are mostly maximal subgraphs, which cannot be enlarged with the addition of new vertices and edges without losing the property which deﬁnes them.

Social communities can be deﬁned in a very strict sense as subgroups whose members are all “friends” to each other (Luce and Perry, 1949) (complete mutuality). In graph terms, this corresponds to a clique, i. e. a subset whose vertices are all adjacent to each other. In social network analysis, a clique is a maximal subgraph, whereas in graph theory it is common to call cliques also non-maximal subgraphs. Triangles are the simplest cliques, and are frequent in real networks. But larger cliques are less frequent. Moreover, the condition is really too strict: a subgraph with all possible internal edges except one would be an extremely cohesive subgroup, but it would not be considered a community under this recipe. Another problem is that all vertices of a clique are absolutely symmetric, with no diﬀerentiation between them. In many practical examples, instead, we expect that within a community there is a whole hierarchy of roles for the vertices, with core vertices coexisting with peripheral ones. We remark that vertices may belong to more cliques simultaneously, a property which is at the basis of the Clique Percolation Method of Palla et al. (Palla et al., 2005) (see Section XI.A). From a practical point of view, ﬁnding cliques in a graph is an NP-complete problem (Bomze et al., 1999). The BronKerbosch method (Bron and Kerbosch, 1973) runs in a time growing exponentially with the size of the graph.

It is however possible to relax the notion of clique, deﬁning subgroups which are still clique-like objects. A possibility is to use properties related to reachability, i. e. to the existence (and length) of paths between vertices. An n-clique is a maximal subgraph such that the distance of each pair of its vertices is not larger than n (Alba, 1973; Luce, 1950). For n = 1 one recovers the deﬁnition of clique, as all vertices are adjacent, so each geodesic path between any pair of vertices has length 1. This definition, more ﬂexible than that of clique, still has some limitations, deriving from the fact that the geodesic paths need not run on the vertices of the subgraph at study, but may run on vertices outside the subgraph. In this way, there may be two disturbing consequences. First, the diameter of the subgraph may exceed n, even if in principle each vertex of the subgraph is less than n steps away from any of the others. Second, the subgraph may be disconnected, which is not consistent with the notion of cohesion one tries to enforce. To avoid these problems, Mokken (Mokken, 1979) has suggested two possible al-

ternatives, the n-clan and the n-club. An n-clan is an n-clique whose diameter is not larger than n, i. e. a subgraph such that the distance between any two of its vertices, computed over shortest paths within the subgraph, does not exceed n. An n-club, instead, is a maximal subgraph of diameter n. The two deﬁnitions are quite close: the diﬀerence is that an n-clan is maximal under the constraint of being an n-clique, whereas an n-club is maximal under the constraint imposed by the length of the diameter.

Another criterion for subgraph cohesion relies on the adjacency of its vertices. The idea is that a vertex must be adjacent to some minumum number of other vertices in the subgraph. In the literature on social network analysis there are two complementary ways of expressing this. A k-plex is a maximal subgraph in which each vertex is adjacent to all other vertices of the subgraph except at most k of them (Seidman and Foster, 1978). Similarly, a k-core is a maximal subgraph in which each vertex is adjacent to at least k other vertices of the subgraph (Seidman, 1983). So, the two deﬁnitions impose conditions on the minimal number of absent or present edges. The corresponding clusters are more cohesive than n-cliques, just because of the existence of many internal edges. In any graph there is a whole hierarchy of cores of diﬀerent order, which can be identiﬁed by means of a recent eﬃcient algorithm (Batagelj and Zaversnik, 2003). A k-core is essentially the same as a p-quasi complete subgraph, which is a subgraph such that the degree of each vertex is larger than p(k − 1), where p is a real number in [0,1] and k the order of the subgraph (Matsuda et al., 1999). Determining whether a graph includes a 1/2-quasi complete subgraph of order at least k is NP-complete.

As cohesive as a subgraph can be, it would hardly be a community if there is a strong cohesion as well between the subgraph and the rest of the graph. Therefore, it is important to compare the internal and external cohesion of a subgraph. In fact, this is what is usually done in the most recent deﬁnitions of community. The ﬁrst recipe, however, is not recent and stems from social network analysis. An LS-set (Luccio and Sami, 1969), or strong community (Radicchi et al., 2004), is a subgraph such that the internal degree of each vertex is greater than its external degree. This condition is quite strict and can be relaxed into the so-called weak deﬁnition of community (Radicchi et al., 2004), for which it suﬃces that the internal degree of the subgraph exceeds its external degree. An LS-set is also a weak community, while the converse is not generally true. Hu et al. (Hu et al.,

- 2008) have introduced alternative deﬁnitions of strong and weak communities: a community is strong if the internal degree of any vertex of the community exceeds the number of edges that the vertex shares with any other community; a community is weak if its total internal degree exceeds the number of edges shared by the community with the other communities. These deﬁnitions are in the same spirit of the planted partition model (Section XV). An LS-set is a strong community also in the


sense of Hu et al.. Likewise, a weak community according to Radicchi et al. is also a weak community for Hu et al.. In both cases the converse is not true, however. Another deﬁnition focuses on the robustness of clusters to edge removal and uses the concept of edge connectivity. The edge connectivity of a pair of vertices in a graph is the minimal number of edges that need to be removed in order to disconnect the two vertices, i. e. such that there is no path between them. A lambda set is a subgraph such that any pair of vertices of the subgraph has a larger edge connectivity than any pair formed by one vertex of the subgraph and one outside the subgraph (Borgatti et al., 1990). However, vertices of a lambda-set need not be adjacent and may be quite distant from each other.

Communities can also be identiﬁed by a ﬁtness measure, expressing to which extent a subraph satisﬁes a given property related to its cohesion. The larger the ﬁtness, the more deﬁnite is the community. This is the same principle behind quality functions, which give an estimate of the goodness of a graph partition (see Section III.C.2). The simplest ﬁtness measure for a cluster is its intra-cluster density δint(C). One could assume that a subgraph C with k vertices is a cluster if δint(C) is larger than a threshold, say ξ. Finding such subgraphs is an NP-complete problem, as it coincides with the NP-complete Clique Problem when the threshold ξ = 1 (Garey and Johnson, 1990). It is better to ﬁx the size of the subgraph because, without this conditions, any clique would be one of the best possible communities, including trivial two-cliques (simple edges). Variants of this problem focus on the number of internal edges of the subgraph (Asahiro et al., 2002; Feige et al., 2001; Holzapfel et al., 2003). Another measure of interest is the relative density ρ(C) of a subgraph C, deﬁned as the ratio between the internal and the total degree of C. Finding subgraphs of a given size with ρ(C) larger than a threshold is NP-complete (Sı´maˇ and Schaeﬀer, 2006). Fitness measures can also be associated to the connectivity of the subgraph at study to the other vertices of the graph. A good community is expected to have a small cut size (see Section A.1), i. e. a small number of edges joining it to the rest of the graph. This sets a bridge between community detection and graph partitioning, which we shall discuss in Section IV.A.

3. Global deﬁnitions

Communities can also be deﬁned with respect to the graph as a whole. This is reasonable in those cases in which clusters are essential parts of the graph, which cannot be taken apart without seriously aﬀecting the functioning of the system. The literature oﬀers many global criteria to identify communities. In most cases they are indirect deﬁnitions, in which some global property of the graph is used in an algorithm that delivers communities at the end. However, there is a class of proper deﬁnitions, based on the idea that a graph has community structure

if it is diﬀerent from a random graph. A random graph ` la Erd¨s-Re´nyi (Section A.3), for instance, is not expected to have community structure, as any two vertices have the same probability to be adjacent, so there should be no preferential linking involving special groups of vertices. Therefore, one can deﬁne a null model, i. e. a graph which matches the original in some of its structural features, but which is otherwise a random graph. The null model is used as a term of comparison, to verify whether the graph at study displays community structure or not. The most popular null model is that proposed by Newman and Girvan and consists of a randomized version of the original graph, where edges are rewired at random, under the constraint that the expected degree of each vertex matches the degree of the vertex in the original graph (Newman and Girvan, 2004). This null model is the basic concept behind the deﬁnition of modularity, a function which evaluates the goodness of partitions of a graph into clusters. Modularity will be discussed at length in this review, because it has the unique privilege of being at the same time a global criterion to deﬁne a community, a quality function and the key ingredient of the most popular method of graph clustering. In the standard formulation of modularity, a subgraph is a community if the number of edges inside the subgraph exceeds the expected number of internal edges that the same subgraph would have in the null model. This expected number is an average over all possible realizations of the null model. Several modiﬁcations of modularity have been proposed (Section VI.B). A general class of null models, including modularity as a special case, has been designed by Reichardt and Bornholdt (Reichardt and Bornholdt, 2006a) (Section VI.B).

- 4. Deﬁnitions based on vertex similarity


It is natural to assume that communities are groups of vertices similar to each other. One can compute the similarity between each pair of vertices with respect to some reference property, local or global, no matter whether they are connected by an edge or not. Each vertex ends up in the cluster whose vertices are most similar to it. Similarity measures are at the basis of traditional methods, like hierarchical, partitional and spectral clustering, to be discussed in Sections IV.B, IV.C and IV.D. Here we discuss some popular measures used in the literature.

If it is possible to embed the graph vertices in an ndimensional Euclidean space, by assigning a position to them, one could use the distance between a pair of vertices as a measure of their similarity (it is actually a measure of dissimilarity because similar vertices are expected to be close to each other). Given the two data points A = (a1,a2,...,an) and B = (b1,b2,...,bn), one could use any norm Lm, like the Euclidean distance (L2-norm),

n

dEAB =

k=1

(ak − bk)2, (3)

the Manhattan distance (L1-norm)

dMAB =

n

|ak − bk|, (4)

k=1

and the L∞-norm d∞AB = max

|ak − bk|. (5)

k∈[1,n]

Another popular spatial measure is the cosine similarity, deﬁned as

###### a · b

ρAB = arccos

, (6)

n k=1 a2k nk=1 b2k

where a·b is the dot product of the vectors a and b. The variable ρAB is deﬁned in the range [0,π).

If the graph cannot be embedded in space, the similarity must be necessarily inferred from the adjacency relationships between vertices. A possibility is to deﬁne a distance (Burt, 1976; Wasserman and Faust, 1994) between vertices like

dij =

(Aik − Ajk)2, (7)

k=i,j

where A is the adjacency matrix. This is a dissimilarity measure, based on the concept of structural equivalence (F.Lorrain and White, 1971). Two vertices are structurally equivalent if they have the same neighbors, even if they are not adjacent themselves. If i and j are structurally equivalent, dij = 0. Vertices with large degree and diﬀerent neighbours are considered very “far” from each other. Alternatively, one could measure the overlap between the neighborhoods Γ(i) and Γ(j) of vertices i and j, given by the ratio between the intersection and the union of the neighborhoods, i. e.

ωij = |Γ(i) ∩ Γ(j)| |Γ(i) ∪ Γ(j)|

. (8)

Another measure related to structural equivalence is the Pearson correlation between columns or rows of the adjacency matrix,

(Aik − µi)(Ajk − µj) nσiσj

Cij = k

, (9)

where the averages µi = ( j Aij)/n and the variances σi = j(Aij − µi)2/n.

An alternative measure is the number of edge- (or vertex-) independent paths between two vertices. Independent paths do not share any edge (vertex), and their number is related to the maximum ﬂow that can be conveyed between the two vertices under the constraint that each edge can carry only one unit of ﬂow (max-ﬂow/mincut theorem (Elias et al., 1956)). The maximum ﬂow can be calculated in a time O(m), for a graph with m

edges, using techniques like the augmenting path algorithm (Ahuja et al., 1993). Similarly, one could consider all paths running between two vertices. In this case, there is the problem that the total number of paths is inﬁnite, but this can be avoided if one performs a weighted sum of the number of paths. For instance, paths of length l can be weighted by the factor αl, with α < 1. Another possibility, suggested by Estrada and Hatano (Estrada and Hatano, 2008, 2009), is to weigh paths of length l with the inverse factorial 1/l!. In both cases, the contribution of long paths is strongly suppressed and the sum converges.

Another important class of measures of vertex similarity is based on properties of random walks on graphs. One of this properties is the commute-time between a pair of vertices, which is the average number of steps needed for a random walker, starting at either vertex, to reach the other vertex for the ﬁrst time and to come back to the starting vertex. Saerens and coworkers (Fouss and Renders, 2007; Saerens et al., 2004; Yen et al., 2007,

- 2009) have extensively studied and used the commutetime (and variants thereof) as (dis)similarity measure: the larger the time, the farther (less similar) the vertices. The commute-time is closely related (Chandra et al.,


1989) to the resistance distance introduced by Klein and Randic (Klein and Randic, 1993), expressing the eﬀective electrical resistance between two vertices if the graph is turned into a resistor network. White and Smyth (White and Smyth, 2003) and Zhou (Zhou, 2003a) used instead the average ﬁrst passage time, i. e. the average number of steps needed to reach for the ﬁrst time the target vertex from the source. Harel and Koren (Harel and Koren, 2001) proposed to build measures out of quantities like the probability to visit a target vertex in no more than a given number of steps after it leaves a source vertex4 and the probability that a random walker starting at a source visits the target exactly once before hitting the source again. Another quantity used to deﬁne similarity measures is the escape probability, deﬁned as the probability that the walker reaches the target vertex before coming back to the source vertex (Palmer and Faloutsos, 2003; Tong et al., 2008). The escape probability is related to the eﬀective conductance between the two vertices in the equivalent resistor network. Other authors have exploited properties of modiﬁed random walks. For instance, the algorithm by Gori and Pucci (Gori and Pucci, 2007) and that by Tong et al. (Tong et al., 2008) used similarity measures derived from Google’s PageRank process (Brin and Page, 1998).

- 4 In the clustering method by Latapy and Pons (Latapy and Pons,


- 2005) (discussed in Section VIII.B) and in a recent analysis by Nadler et al. (Nadler et al., 2006), one deﬁned a dissimilarity measure called “diﬀusion distance”, which is derived from the probability that the walker visits the target after a ﬁxed number of steps.


###### C. Partitions

1. Basics

A partition is a division of a graph in clusters, such that each vertex belongs to one cluster. As we have seen in Section II, in real systems vertices may be shared among diﬀerent communities. A division of a graph into overlapping (or fuzzy) communities is called cover.

The number of possible partitions in k clusters of a graph with n vertices is the Stirling number of the second kind S(n,k) (Andrews, 1976). The total number of possible partitions is the n-th Bell number Bn =

n k=0 S(n,k) (Andrews, 1976). In the limit of large n,

Bn has the asymptotic form (Lov´sz, 1993)

Bn ∼

1 √n

[λ(n)]n+1/2eλ(n)−n−1, (10)

where λ(n) = eW(n) = n/W(n), W(n) being the Lambert W function (P´lya and Szeg¨, 1998). Therefore, Bn grows faster than exponentially with the graph size n, which means that an enumeration and/or evaluation of all partitions of a graph is impossible, unless the graph consists of very few vertices.

Partitions can be hierarchically ordered, when the graph has diﬀerent levels of organization/structure at diﬀerent scales. In this case, clusters display in turn community structure, with smaller communities inside, which may again contain smaller communities, and so on (Fig. 7). As an example, in a social network of children living in the same town, one could group the children according to the schools they attend, but within each school one can make a subdivision into classes. Hierarchical organization is a common feature of many real networks, where it is revealed by a peculiar scaling of the clustering coeﬃcient for vertices having the same degree k, when plotted as a function of k (Ravasz and Barab´si, 2003; Ravasz et al., 2002). A natural way to represent the hierarchical structure of a graph is to draw a dendrogram, like the one illustrated in Fig. 8. Here, partitions of a graph with twelve vertices are shown. At the bottom, each vertex is its own module (the “leaves” of the tree). By moving upwards, groups of vertices are successively aggregated. Mergers of communities are represented by horizontal lines. The uppermost level represents the whole graph as a single community. Cutting the diagram horizontally at some height, as shown in the ﬁgure (dashed line), displays one partition of the graph. The diagram is hierarchical by construction: each community belonging to a level is fully included in a community at a higher level. Dendrograms are regularly used in sociology and biology. The technique of hierarchical clustering, described in Section IV.B, lends itself naturally to this kind of representation.

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


| | |
|---|---|
| | |
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


| | |
|---|---|
| | |
| | |


- FIG. 7 Schematic example of a hierarchical graph. Sixteen modules with 32 vertices each clearly form four larger clusters. All vertices have degree 64. Reprinted ﬁgure with permission from Ref. (Lancichinetti et al., 2009). c 2009 by IOP Publishing.

- FIG. 8 A dendrogram, or hierarchical tree. Horizontal cuts correspond to partitions of the graph in communities. Reprinted ﬁgure with permission from Ref. (Newman and Girvan, 2004). c 2004 by the American Physical Society.


portant impossibility theorem. Given a set S of points, a distance function d is deﬁned, which is positive deﬁnite and symmetric (the triangular inequality is not explicitly required). One wishes to ﬁnd a clustering f based on the distances between the points. Kleinberg showed that no clustering satisﬁes at the same time the three following properties:

- 1. Scale-invariance: given a constant α, multiplying any distance function d by α yields the same clustering.
- 2. Richness: any possible partition of the given point set can be recovered if one chooses a suitable distance function d.
- 3. Consistency: given a partition, any modiﬁcation of the distance function that does not decrease the distance between points of diﬀerent clusters and that does not increase the distance between points of the same cluster, yields the same clustering.


2. Quality functions: modularity

Reliable algorithms are supposed to identify good partitions. But what is a good clustering? In order to distinguish between “good” and “bad” clusterings, it would be useful to require that partitions satisfy a set of basic properties, intuitive and easy to agree upon. In the wider context of data clustering, this issue has been studied by Jon Kleinberg (Kleinberg, 2002), who has proved an im-

The theorem cannot be extended to graph clustering because the distance function cannot be in general deﬁned for a graph which is not complete. For weighted complete graphs, like correlation matrices (Tumminello et al., 2008), it is often possible to deﬁne a distance function. On a generic graph, except for the ﬁrst property, which

does not make sense without a distance function5, the other two are quite well deﬁned. The property of richness implies that, given a partition, one can set edges between the vertices in such a way that the partition is a natural outcome of the resulting graph (e.g., it could be achieved by setting edges only between vertices of the same cluster). Consistency here implies that deleting inter-cluster edges and adding intra-cluster edges yields the same partition.

Many algorithms are able to identify a subset of meaningful partitions, ideally one or just a few, whereas some others, like techniques based on hierarchical clustering (Section IV.B), deliver a large number of partitions. That does not mean that the partitions found are equally good. Therefore it is helpful (sometimes even necessary) to have a quantitative criterion to assess the goodness of a graph partition. A quality function is a function that assigns a number to each partition of a graph. In this way one can rank partitions based on their score given by the quality function. Partitions with high scores are “good”, so the one with the largest score is by deﬁnition the best. Nevertheless, one should keep in mind that the question of when a partition is better than another one is ill-posed, and the answer depends on the speciﬁc concept of community and/or quality function adopted.

A quality function Q is additive if there is an elementary function q such that, for any partition P of a graph

Q(P) =

q(C), (11)

C∈P

where C is a generic cluster of partition P. Eq. 11 states that the quality of a partition is given by the sum of the qualities of the individual clusters. The function q(C) could be any of the cluster ﬁtness functions discussed

- in Section III.B.2, for instance. Most quality functions used in the literature are additive, although it is not a necessary requirement.


An example of quality function is the performance P, which counts the number of correctly “interpreted” pairs of vertices, i. e. two vertices belonging to the same community and connected by an edge, or two vertices belonging to diﬀerent communities and not connected by an edge. The deﬁnition of performance, for a partition P, is

P(P) = |{(i,j) ∈ E,Ci = Cj}| + |{(i,j) ∈/ E,Ci = Cj}| n(n − 1)/2

.

(12) By deﬁnition, 0 ≤ P(P) ≤ 1. Another example is coverage, i. e. the ratio of the number of intra-community edges by the total number of edges: by deﬁnition, an ideal cluster structure, where the clusters are disconnected from each other, yields a coverage of 1, as all edges of the graph fall within clusters.

- 5 The traditional shortest-path distance between vertices is not suitable here, as it is integer by deﬁnition.


The most popular quality function is the modularity of Newman and Girvan (Newman and Girvan, 2004). It is based on the idea that a random graph is not expected to have a cluster structure, so the possible existence of clusters is revealed by the comparison between the actual density of edges in a subgraph and the density one would expect to have in the subgraph if the vertices of the graph were attached regardless of community structure. This expected edge density depends on the chosen null model, i. e. a copy of the original graph keeping some of its structural properties but without community structure. Modularity can then be written as follows

- 1

- 2m ij


Q =

(Aij − Pij)δ(Ci,Cj), (13)

where the sum runs over all pairs of vertices, A is the adjacency matrix, m the total number of edges of the graph, and Pij represents the expected number of edges between vertices i and j in the null model. The δ-function yields one if vertices i and j are in the same community (Ci = Cj), zero otherwise. The choice of the null model graph is in principle arbitrary, and several possibilities exist. For instance, one could simply demand that the graph keeps the same number of edges as the original graph, and that edges are placed with the same probability between any pair of vertices. In this case (Bernoulli random graph), the null model term in Eq. 13 would be a constant (i. e. Pij = p = 2m/[n(n − 1)], ∀i,j). However this null model is not a good descriptor of real networks, as it has a Poissonian degree distribution which is very diﬀerent from the skewed distributions found in real networks. Due to the important implications that broad degree distributions have for the structure and function of real networks (Albert and Barab´si, 2002; Barrat et al., 2008; Boccaletti et al., 2006; Dorogovtsev and Mendes, 2002; Newman, 2003; Pastor-Satorras and Vespignani, 2004), it is preferable to go for a null model with the same degree distribution of the original graph. The standard null model of modularity imposes that the expected degree sequence (after averaging over all possible conﬁgurations of the model) matches the actual degree sequence of the graph. This is a stricter constraint than merely requiring the match of the degree distributions, and is essentially equivalent 6 to the conﬁguration model, which has been subject of intense investigations in the recent literature on networks ( Luczak, 1992; Molloy and Reed, 1995). In this null model, a vertex could be attached to any other vertex of the graph and the probability that vertices i and j, with degrees ki and kj, are connected,

6 The diﬀerence is that the conﬁguration model maintains the same degree sequence of the original graph for each realization, whereas in the null model of modularity the degree sequence of a realization is in general diﬀerent, and only the average/expected degree sequence coincides with that of the graph at hand. The two models are equivalent in the limit of inﬁnite graph size.

can be calculated without problems. In fact, in order to form an edge between i and j one needs to join two stubs (i. e. half-edges), incident with i and j. The probability pi to pick at random a stub incident with i is ki/2m, as there are ki stubs incident with i out of a total of 2m. The probability of a connection between i and j is then given by the product pipj, since edges are placed independently of each other. The result is kikj/4m2, which yields an expected number Pij = 2mpipj = kikj/2m of edges between i and j. So, the ﬁnal expression of modularity reads

- 1

- 2m ij


Q =

kikj 2m

Aij −

δ(Ci,Cj). (14)

Since the only contributions to the sum come from vertex pairs belonging to the same cluster, we can group these contributions together and rewrite the sum over the vertex pairs as a sum over the clusters

nc

Q =

c=1

lc m −

dc 2m

2

. (15)

Here, nc is the number of clusters, lc the total number of edges joining vertices of module c and dc the sum of the degrees of the vertices of c. In Eq. 15, the ﬁrst term of each summand is the fraction of edges of the graph inside the module, whereas the second term represents the expected fraction of edges that would be there if the graph were a random graph with the same expected degree for each vertex.

- A nice feature of modularity is that it can be equiva-


lently expressed both in terms of the intra-cluster edges,

- as in Eq. 15, and in terms of the inter-cluster edges (Djidjev, 2007). In fact, the maximum of modularity can be expressed as


nc

Qmax = maxP

c=1

nc

1 m

=

maxP

c=1

1 m

= −

minP −

lc m −

dc 2m

2

lc − Ex(lc)

nc

c=1

lc − Ex(lc) , (16)

where maxP and minP indicates the maximum and the minimum over all possible graph partitions P and

Ex(lc) = d2c/4m indicates the expected number of links in cluster c in the null model of modularity. By adding and subtracting the total number of edges m of the graph one ﬁnally gets

1 m

Qmax = −

1 m

= −

nc

minP m −

lc − m −

c=1

nc

Ex(lc)

c=1

minP(|CutP| − ExCutP). (17)

In the last expression |CutP| = m− nc=1c lc is the number of inter-cluster edges of partition P, and ExCutP = m −

nc c=1 Ex(lc) is the expected number of inter-cluster edges

of the partition in modularity’s null model.

According to Eq. 15, a subgraph is a module if the corresponding contribution to modularity in the sum is positive. The more the number of internal edges of the cluster exceeds the expected number, the better deﬁned the community. So, large positive values of the modularity indicate good partitions7. The maximum modularity of a graph generally grows if the size of the graph and/or the number of (well-separated) clusters increase (Good et al., 2009). Therefore, modularity should not be used to compare the quality of the community structure of graphs which are very diﬀerent in size. The modularity of the whole graph, taken as a single community, is zero, as the two terms of the only summand in this case are equal and opposite. Modularity is always smaller than one, and can be negative as well. For instance, the partition in which each vertex is a community is always negative: in this case the sum runs over n terms, which are all negative as the ﬁrst term of each summand is zero. This is a nice feature of the measure, implying that, if there are no partitions with positive modularity, the graph has no community structure. On the contrary, the existence of partitions with large negative modularity values may hint to the existence of subgroups with very few internal edges and many edges lying between them (multipartite structure) (Newman, 2006a). Holmstr¨m et al. (Holmstr¨m et al., 2009) have shown that the distribution of modularity values across the partitions of various graphs, real and artiﬁcial (including random graphs with no apparent community structure), has some stable features, and that the most likely modularity values correspond to partitions in clusters of approximately equal size.

Modularity has been employed as quality function in many algorithms, like some of the divisive algorithms of Section V. In addition, modularity optimization is itself a popular method for community detection (see Section VI.A). Modularity also allows to assess the stability of partitions (Massen and Doye, 2006) (Section XIV), it can be used to design layouts for graph visualization (Noack, 2009) and to perform a sort of renormalization of a graph, by transforming a graph into a smaller one with the same community structure (Arenas et al., 2007).

IV. TRADITIONAL METHODS

A. Graph partitioning

The problem of graph partitioning consists in dividing the vertices in g groups of predeﬁned size, such that the

7 This is not necessarily true, as we will see in Section VI.C.

- FIG. 9 Graph partitioning. The dashed line shows the solution of the minimum bisection problem for the graph illustrated, i. e. the partition in two groups of equal size with minimal number of edges running between the groups. Reprinted ﬁgure with permission from Ref. (Fortunato and Castellano, 2009). c 2009 by Springer.


number of edges lying between the groups is minimal. The number of edges running between clusters is called cut size. Fig. 9 presents the solution of the problem for a graph with fourteen vertices, for g = 2 and clusters of equal size.

Specifying the number of clusters of the partition is necessary. If one simply imposed a partition with the minimal cut size, and left the number of clusters free, the solution would be trivial, corresponding to all vertices ending up in the same cluster, as this would yield a vanishing cut size. Specifying the size is also necessary, as otherwise the most likely solution of the problem would consist in separating the lowest degree vertex from the rest of the graph, which is quite uninteresting. This problem can be actually avoided by choosing a diﬀerent measure to optimize for the partitioning, which accounts for the size of the clusters. Some of these measures will be brieﬂy introduced at the end of this section.

Graph partitioning is a fundamental issue in parallel computing, circuit partitioning and layout, and in the design of many serial algorithms, including techniques to solve partial diﬀerential equations and sparse linear systems of equations. Most variants of the graph partitioning problem are NP-hard. There are however several algorithms that can do a good job, even if their solutions are not necessarily optimal (Pothen, 1997). Many algorithms perform a bisection of the graph. Partitions into more than two clusters are usually attained by iterative bisectioning. Moreover, in most cases one imposes the constraint that the clusters have equal size. This problem is called minimum bisection and is NP-hard.

The Kernighan-Lin algorithm (Kernighan and Lin, 1970) is one of the earliest methods proposed and is still

frequently used, often in combination with other techniques. The authors were motivated by the problem of partitioning electronic circuits onto boards: the nodes contained in diﬀerent boards need to be linked to each other with the least number of connections. The procedure is an optimization of a beneﬁt function Q, which represents the diﬀerence between the number of edges inside the modules and the number of edges lying between them. The starting point is an initial partition of the graph in two clusters of the predeﬁned size: such initial partition can be random or suggested by some information on the graph structure. Then, subsets consisting of equal numbers of vertices are swapped between the two groups, so that Q has the maximal increase. The subsets can consist of single vertices. To reduce the risk to be trapped in local maxima of Q, the procedure includes some swaps that decrease the function Q. After a series of swaps with positive and negative gains, the partition with the largest value of Q is selected and used as starting point of a new series of iterations. The KernighanLin algorithm is quite fast, scaling as O(n2 log n) (n being as usual the number of vertices), if only a constant number of swaps are performed at each iteration. The most expensive part is the identiﬁcation of the subsets to swap, which requires the computation of the gains/losses for any pair of candidate subsets. On sparse graphs, a slightly diﬀerent heuristic allows to lower the complexity to O(n2). The partitions found by the procedure are strongly dependent on the initial conﬁguration and other algorithms can do better. It is preferable to start with a good guess about the sought partition, otherwise the results are quite poor. Therefore the method is typically used to improve on the partitions found through other techniques, by using them as starting conﬁgurations for the algorithm. The Kernighan-Lin algorithm has been extended to extract partitions in any number of parts (Suaris and Kedem, 1988), however the run-time and storage costs increase rapidly with the number of clusters.

Another popular technique is the spectral bisection method (Barnes, 1982), which is based on the properties of the spectrum of the Laplacian matrix. Spectral clustering will be discussed more thoroughly in Section IV.D, here we focus on its application to graph partitioning.

Every partition of a graph with n vertices in two groups can be represented by an index vector s, whose component si is +1 if vertex i is in one group and −1 if it is in the other group. The cut size R of the partition of the graph in the two groups can be written as

1 4

sTLs, (18)

R =

where L is the Laplacian matrix and sT the transpose of vector s. Vector s can be written as s = i aivi, where vi, i = 1,...,n are the eigenvectors of the Laplacian. If s is properly normalized, then

R =

i

a2iλi, (19)

where λi is the Laplacian eigenvalue corresponding to eigenvector vi. It is worth remarking that the sum contains at most n−1 terms, as the Laplacian has at least one zero eigenvalue. Minimizing R equals to the minimization of the sum on the right-hand side of Eq. 19. This task is still very hard. However, if the second lowest eigenvector λ2 is close enough to zero, a good approximation of the minimum can be attained by choosing s parallel to the corresponding eigenvector v2, which is called Fiedler vector (Fiedler, 1973): this would reduce the sum to λ2, which is a small number. But the index vector cannot be perfectly parallel to v2 by construction, because all its components are equal in modulus, whereas the components of v2 are not. The best choice is to match the signs of the components. So, one can set si = +1 (−1) if v2i > 0 (< 0). It may happen that the sizes of the two corresponding groups do not match the predeﬁned sizes one wishes to have. In this case, if one aims at a split in n1 and n2 = n−n1 vertices, the best strategy is to order the components of the Fiedler vector from the lowest to the largest values and to put in one group the vertices corresponding to the ﬁrst n1 components from the top or the bottom, and the remaining vertices in the second group. This procedure yields two partitions: the better solution is naturally the one that gives the smaller cut size.

The spectral bisection method is quite fast. The ﬁrst eigenvectors of the Laplacian can be computed by using the Lanczos method (Lanczos, 1950). The time required to compute the ﬁrst k eigenvectors of a matrix with the Lanczos method depends on the size of the eigengap |λk+1 − λk| (Golub and Loan, 1989). If the eigenvalues λk+1 and λk are well separated, the running time of the algorithm is much shorter than the time required to calculate the complete set of eigenvectors, which scales as O(n3). The method gives in general good partitions, that can be further improved by applying the Kernighan-Lin algorithm.

The well known max-ﬂow min-cut theorem by Ford and Fulkerson (Ford and Fulkerson, 1956) states that the minimum cut between any two vertices s and t of a graph,

- i. e. any minimal subset of edges whose deletion would topologically separate s from t, carries the maximum ﬂow that can be transported from s to t across the graph. In this context edges play the role of water pipes, with a given carrying capacity (e.g. their weights), and vertices the role of pipe junctions. This theorem has been used to determine minimal cuts from maximal ﬂows in clustering algorithms. There are several eﬃcient routines to compute maximum ﬂows in graphs, like the algorithm of Goldberg and Tarjan (Goldberg and Tarjan, 1988). Flake et al. (Flake et al., 2000; Flake et al., 2002) have recently used maximum ﬂows to identify communities in the graph of the World Wide Web. The web graph is directed but for the purposes of the calculation Flake et


- at. treated the edges as undirected. Web communities are deﬁned to be “strong” (LS-sets), i. e. the internal degree of each vertex must not be smaller than its external


degree (Radicchi et al., 2004). An artiﬁcial sink t is added to the graph and one calculates the maximum ﬂows from a source vertex s to the sink t: the corresponding minimum cut identiﬁes the community of vertex s, provided s shares a suﬃciently large number of edges with the other vertices of its community, otherwise one could get trivial separations and meaningless clusters.

Other popular methods for graph partitioning include level-structure partitioning, the geometric algorithm, multilevel algorithms, etc. A good description of these algorithms can be found in Ref. (Pothen, 1997).

Graphs can be also partitioned by minimizing measures that are aﬃne to the cut size, like conductance (Bollobas, 1998). The conductance Φ(C) of the subgraph C of a graph G is deﬁned as

c(C,G \ C) min(kC,kG\C)

Φ(C) =

, (20)

where c(C,G \C) is the cut size of C, and kC, kG\C are the total degrees of C and of the rest of the graph G\C, respectively. Cuts are deﬁned only between non-empty sets, otherwise the measure would not be deﬁned (as the denominator in Eq. 20 would vanish). The minimum of the conductance is obtained in correspondence of low values of the cut size and of large values for the denominator in Eq. 20, which peaks when the total degrees of the cluster and its complement are equal. In practical applications, especially on large graphs, close values of the total degrees correspond to clusters of approximately equal size. The problem of ﬁnding a cut with minimal conductance is NP-hard (Sı´maˇ and Schaeﬀer, 2006). Similar measures are the ratio cut (Wei and Cheng, 1989) and the normalized cut (Shi and Malik, 1997, 2000). The ratio cut of a cluster C is deﬁned as

c(C,G \ C) nCnG\C

ΦC(C) =

, (21)

where nC and nG\C are the number of vertices of the two subgraphs. The normalized cut of a cluster C is

c(C,G \ C) kC

ΦN(C) =

, (22)

where kC is again the total degree of C. As for the conductance, minimizing the ratio cut and the normalized cut favors partitions into clusters of approximately equal size, measured in terms of the number of vertices or edges, respectively. On the other hand, graph partitioning requires preliminary assumptions on the cluster sizes, whereas the minimization of conductance, ratio cut and normalized cut does not. The ratio cut was introduced for circuit partitioning (Wei and Cheng, 1989) and its optimization is an NP-hard problem (Matula and Shahrokhi, 1990). The normalized cut is frequently used in image segmentation (Blake and Zisserman, 1987) and its optimization is NP-complete (Shi and Malik, 2000). The cut ratio and the normalized cut can be quite well

minimized via spectral clustering (Chan et al., 1993; Hagen and Kahng, 1992) (Section IV.D).

Algorithms for graph partitioning are not good for community detection, because it is necessary to provide

- as input the number of groups and in some cases even their sizes, about which in principle one knows nothing. Instead, one would like an algorithm capable to produce this information in its output. Besides, from the methodological point of view, using iterative bisectioning to split the graph in more pieces is not a reliable procedure. For instance, a split into three clusters is necessarily obtained by breaking either cluster of the original bipartition in two parts, whereas in many cases a minimum cut partition is obtained if the third cluster is a merger of parts of both initial clusters.


- B. Hierarchical clustering


In general, very little is known about the community structure of a graph. It is uncommon to know the number of clusters in which the graph is split, or other indications about the membership of the vertices. In such cases clustering procedures like graph partitioning methods can hardly be of help, and one is forced to make some reasonable assumptions about the number and size of the clusters, which are often unjustiﬁed. On the other hand, the graph may have a hierarchical structure, i. e. may display several levels of grouping of the vertices, with small clusters included within large clusters, which are in turn included in larger clusters, and so on. Social networks, for instance, often have a hierarchical structure

- (Section III.C.1). In such cases, one may use hierarchical clustering algorithms (Hastie et al., 2001), i. e. clustering techniques that reveal the multilevel structure of the graph. Hierarchical clustering is very common in social network analysis, biology, engineering, marketing, etc.


The starting point of any hierarchical clustering method is the deﬁnition of a similarity measure between vertices. After a measure is chosen, one computes the similarity for each pair of vertices, no matter if they are connected or not. At the end of this process, one is left with a new n×n matrix X, the similarity matrix. In Sec-

- tion III.B.4 we have listed several possible deﬁnitions of similarity. Hierarchical clustering techniques aim at identifying groups of vertices with high similarity, and can be classiﬁed in two categories:


- 1. Agglomerative algorithms, in which clusters are iteratively merged if their similarity is suﬃciently high;
- 2. Divisive algorithms, in which clusters are iteratively split by removing edges connecting vertices with low similarity.


The two classes refer to opposite processes: agglomerative algorithms are bottom-up, as one starts from the vertices as separate clusters (singletons) and ends up with

the graph as a unique cluster; divisive algorithms are top-down as they follow the opposite direction. Divisive techniques have been rarely used in the past (meanwhile they have become more popular, see Section V), so we shall concentrate here on agglomerative algorithms.

Since clusters are merged based on their mutual similarity, it is essential to deﬁne a measure that estimates how similar clusters are, out of the matrix X. This involves some arbitrariness and several prescriptions exist. In single linkage clustering, the similarity between two groups is the minimum element xij, with i in one group and j in the other. On the contrary, the maximum element xij for vertices of diﬀerent groups is used in the procedure of complete linkage clustering. In average linkage clustering one has to compute the average of the xij.

The procedure can be better illustrated by means of dendrograms (Section III.C.1), like the one in Fig. 8. Sometimes, stopping conditions are imposed to select a partition or a group of partitions that satisfy a special criterion, like a given number of clusters or the optimization of a quality function (e.g. modularity).

Hierarchical clustering has the advantage that it does not require a preliminary knowledge on the number and size of the clusters. However, it does not provide a way to discriminate between the many partitions obtained by the procedure, and to choose that or those that better represent the community structure of the graph. The results of the method depend on the speciﬁc similarity measure adopted. The procedure also yields a hierarchical structure by construction, which is rather artiﬁcial in most cases, since the graph at hand may not have a hierarchical structure at all. Moreover, vertices of a community may not be correctly classiﬁed, and in many cases some vertices are missed even if they have a central role in their clusters (Newman, 2004a). Another problem is that vertices with just one neighbor are often classiﬁed as separated clusters, which in most cases does not make sense. Finally, a major weakness of agglomerative hierarchical clustering is that it does not scale well. If points are embedded in space, so that one can use the distance as dissimilarity measure, the computational complexity is O(n2) for single linkage, O(n2 log n) for the complete and average linkage schemes. For graph clustering, where a distance is not trivially deﬁned, the complexity can become much heavier if the calculation of the chosen similarity measure is costly.

C. Partitional clustering

Partitional clustering indicates another popular class of methods to ﬁnd clusters in a set of data points. Here, the number of clusters is preassigned, say k. The points are embedded in a metric space, so that each vertex is a point and a distance measure is deﬁned between pairs of points in the space. The distance is a measure of dissimilarity between vertices. The goal is to separate the points in k clusters such to maximize/minimize a given

cost function based on distances between points and/or from points to centroids, i. e. suitably deﬁned positions in space. Some of the most used functions are listed below:

- • Minimum k-clustering. The cost function here is the diameter of a cluster, which is the largest distance between two points of a cluster. The points are classiﬁed such that the largest of the k cluster diameters is the smallest possible. The idea is to keep the clusters very “compact”.
- • k-clustering sum. Same as minimum k-clustering, but the diameter is replaced by the average distance between all pairs of points of a cluster.
- • k-center. For each cluster i one deﬁnes a reference point xi, the centroid, and computes the maximum di of the distances of each cluster point from the centroid. The clusters and centroids are selfconsistently chosen such to minimize the largest value of di.
- • k-median. Same as k-center, but the maximum distance from the centroid is replaced by the average distance.


The most popular partitional technique in the literature is k-means clustering (MacQueen, 1967). Here the cost function is the total intra-cluster distance, or squared error function

k

||xj − ci||2, (23)

i=1 xj∈Si

where Si indicates the subset of points of the i-th cluster and ci its centroid. The k-means problem can be simply solved with the Lloyd’s algorithm (Lloyd, 1982). One starts from an initial distribution of centroids such that they are as far as possible from each other. In the ﬁrst iteration, each vertex is assigned to the nearest centroid. Next, the centers of mass of the k clusters are estimated and become a new set of centroids, which allows for a new classiﬁcation of the vertices, and so on. After a small number of iterations, the positions of the centroids are stable, and the clusters do not change any more. The solution found is not optimal, and it strongly depends on the initial choice of the centroids. Nevertheless, Lloyd’s heuristic has remained popular due to its quick convergence, which makes it suitable for the analysis of large data sets. The result can be improved by performing more runs starting from diﬀerent initial conditions, and picking the solution which yields the minimum value of the total intra-cluster distance. Extensions of k-means clustering to graphs have been proposed by some authors (Hlaoui and Wang, 2004; Rattigan et al., 2007; Schenker et al., 2003).

Another popular technique, similar in spirit to k-means clustering, is fuzzy k-means clustering (Bezdek, 1981; Dunn, 1974). This method accounts for the fact that a point may belong to two or more clusters at the same

time and is widely used in pattern recognition. The associated cost function is

n

Jm =

i=1

k

umij||xi − cj||2, (24)

j=1

where uij is the membership matrix, which measures the degree of membership of point i (with position xi) in cluster j, m is a real number greater than 1 and cj is the center of cluster j

n i=1 umijxi

. (25)

cj =

n i=1 umij

The matrix uij is normalized so that the sum of the memberships of every point in all clusters yields 1. The membership uij is related to the distance of point i from the center of cluster j, as it is reasonable to assume that the larger this distance, the lower uij. This can be expressed by the following relation

1

uij =

. (26)

2 m−1

||xi−cj|| ||xi−cl||

- k
- l=1


The cost function Jm can be minimized by iterating Eqs. 25 and 26. One starts from some initial guess for uij and uses Eq. 25 to compute the centers, which are then plugged back into Eqs. 26, and so on. The process stops when the corresponding elements of the membership matrix in consecutive iterations diﬀer from each other by less than a predeﬁned tolerance. It can be shown that this procedure indeed delivers a local minimum of the cost function Jm of Eq. 24. This procedure has the same problems of Lloyd’s algorithm for k-means clustering, i. e. the minimum is a local minimum, and depends on the initial choice of the matrix uij.

The limitation of partitional clustering is the same as that of the graph partitioning algorithms: the number of clusters must be speciﬁed at the beginning, the method is not able to derive it. In addition, the embedding in a metric space can be natural for some graphs, but rather artiﬁcial for others.

D. Spectral clustering

Let us suppose to have a set of n objects x1,x2,...,xn with a pairwise similarity function S deﬁned between them, which is symmetric and non-negative (i. e., S(xi,xj) = S(xj,xi) ≥ 0, ∀i,j = 1,..n). Spectral clustering includes all methods and techniques that partition the set into clusters by using the eigenvectors of matrices, like S itself or other matrices derived from it. In particular, the objects could be points in some metric space, or the vertices of a graph. Spectral clustering consists of a transformation of the initial set of objects into a set of points in space, whose coordinates are elements of eigenvectors: the set of points is then clustered via standard

techniques, like k-means clustering (Section IV.C). One may wonder why it is necessary to cluster the points obtained through the eigenvectors, when one can directly cluster the initial set of objects, based on the similarity matrix. The reason is that the change of representation induced by the eigenvectors makes the cluster properties of the initial data set much more evident. In this way, spectral clustering is able to separate data points that could not be resolved by applying directly k-means clustering, for instance, as the latter tends to deliver convex sets of points.

The ﬁrst contribution on spectral clustering was a paper by Donath and Hoﬀmann (Donath and Hoﬀman, 1973), who used the eigenvectors of the adjacency matrix for graph partitions. In the same year, Fiedler (Fiedler, 1973) realized that from the eigenvector of the second smallest eigenvalue of the Laplacian matrix it was possible to obtain a bipartition of the graph with very low cut size, as we have explained in Section IV.A. For a historical survey see Ref. (Spielman and Teng, 1996). In this Section we shall follow the nice tutorial by von Luxburg (von Luxburg, 2006), with a focus on spectral graph clustering. The concepts and methods discussed below apply to both unweighted and weighted graphs.

The Laplacian is by far the most used matrix in spectral clustering. In Section A.2 we see that the unnormalized Laplacian of a graph with k connected components has k zero eigenvalues. In this case the Laplacian can be written in block-diagonal form, i. e. the vertices can be ordered in such a way that the Laplacian displays k square blocks along the diagonal, with (some) entries diﬀerent from zero, whereas all other elements vanish. Each block is the Laplacian of the corresponding subgraph, so it has the trivial eigenvector with components (1,1,1,...,1,1). Therefore, there are k degenerate eigenvectors with equal non-vanishing components in correspondence of the vertices of a block, whereas all other components are zero. In this way, from the components of the eigenvectors one can identify the connected components of the graph. For instance, let us consider the n×k matrix, whose columns are the k eigenvectors above mentioned. The i-th row of this matrix is a vector with k components representing vertex i of the graph. Vectors representing vertices in the same connected component of the graph coincide, and their tip lies on one of the axes of a k-dimensional system of coordinates (i. e. they are all vectors of the form (0,0,...0,1,0,...,0,0)). So, by drawing the vertex vectors one would see k distinct points, each on a diﬀerent axis, corresponding to the graph components.

If the graph is connected, but consists of k subgraphs which are weakly linked to each other, the spectrum of the unnormalized Laplacian will have one zero eigenvalue, all others being positive. Now the Laplacian cannot be put in block-diagonal form: even if one enumerates the vertices in the order of their cluster memberships (by listing ﬁrst the vertices of one cluster, then the vertices of another cluster, etc.) there will always be some

non-vanishing entries outside of the blocks. However, the lowest k − 1 non-vanishing eigenvalues are still close to zero, and the vertex vectors of the ﬁrst k eigenvectors should still enable one to clearly distinguish the clusters in a k-dimensional space. Vertex vectors corresponding to the same cluster are now not coincident, in general, but still rather close to each other. So, instead of k points, one would observe k groups of points, with the points of each group localized close to each other and far from the other groups. Techniques like k-means clustering (Section IV.C) can then easily recover the clusters.

The scenario we have described is expected from perturbation theory (Bhatia, 1997; Stewart and Sun, 1990). In principle all symmetric matrices that can be put in block-diagonal form have a set of eigenvectors (as many as the blocks), such that the elements of each eigenvector are diﬀerent from zero on the vertices of a block and zero otherwise, just like the Laplacian. The adjacency matrix itself has the same property, for example. This is a necessary condition for the eigenvectors to be successfully used for graph clustering, but it is not suﬃcient. In the case of the Laplacian, for a graph with k connected components, we know that the eigenvectors corresponding to the k lowest eigenvalues come each from one of the components. In the case of the adjacency matrix A (or of its weighted counterpart W), instead, it may happen that large eigenvalues refer to the same component. So, if one takes the eigenvectors corresponding to the k largest eigenvalues8, some components will be overrepresented, while others will be absent. Therefore, using the eigenvectors of A (or W) in spectral graph clustering is in general not reliable. Moreover, the elements of the eigenvectors corresponding to the components should be suﬃciently far from zero. To understand why, suppose that we take a (symmetric, block-diagonal) matrix, and that one or more elements of one of the eigenvectors corresponding to the connected components are very close to zero. If one perturbs the graph by adding edges between diﬀerent components, all entries of the perturbed eigenvectors will become non-zero and some may have comparable values as the lowest elements of the eigenvectors on the blocks. Therefore distinguishing vertices of diﬀerent components may become a problem, even when the perturbation is fairly small, and misclassiﬁcations are likely. On the other hand, the non-vanishing elements of the (normalized) eigenvectors of the unnormalized Laplacian, for instance, are all equal to 1/√ni, where ni is the number of vertices in the i-th component. In this way, there is a gap between the lowest element (here they are all equal for the same eigenvector) and zero. This holds as well for the normalized Laplacian Lrw (Section A.2). For the other normalized Laplacian Lsym (Section A.2), the

8 Large eigenvalues of the adjacency matrix are the counterpart of the low eigenvalues of the Laplacian, since L = D − A, where D is the diagonal matrix whose elements are the vertex degrees.

non-zero elements of the eigenvectors corresponding to the connected components are proportional to the square root of the degree of the corresponding vertex. So, if degrees are very diﬀerent from each other, and especially if there are vertices with very low degree, some eigenvector elements may be quite small. As we shall see below, in the context of the technique by Ng et al. (Ng et al., 2001), a suitable normalization procedure is introduced to alleviate this problem.

Now that we have explained why the Laplacian matrix is particularly suitable for spectral clustering, we proceed with the description of three popular methods: unnormalized spectral clustering and two normalized spectral clustering techniques, proposed by Shi and Malik (Shi and Malik, 1997, 2000) and by Ng et al. (Ng et al., 2001), respectively.

Unnormalized spectral clustering uses the unnormalized Laplacian L. The inputs are the adjacency matrix A (W for weighted graphs) and the number k of clusters to be recovered. The ﬁrst step consists in computing the eigenvectors corresponding to the lowest k eigenvalues of L. Then, one builds the n × k matrix V, whose columns are the k eigenvectors. The n rows of V are used to represent the graph vertices in a k-dimensional Euclidean space, through a Cartesian system of coordinates. The points are then grouped in k clusters by using k-means clustering or similar techniques (Section IV.C). Normalized spectral clustering works in the same way. In the version by Shi and Malik (Shi and Malik, 1997, 2000), one uses the eigenvectors of the normalized Laplacian Lrw (Section A.2). In the algorithm by Ng et al. (Ng et al., 2001) one adopts the normalized Laplacian Lsym (Section A.2). Here, however, the matrix V is normalized by dividing the elements of each row by their sum, obtaining a new matrix U, whose rows are then used to represent the vertices in space, as in the other methods. By doing so, it is much more unlikely that eigenvector components for a well-separated cluster are close to zero, a scenario which would make the classiﬁcation of the corresponding vertices problematic, as we have said above. However, if the graph has some vertices with low degree, they may still be misclassiﬁed.

Spectral clustering is closely related to graph partitioning. Relaxed versions of the minimization of ratio cut and normalized cut (see Section IV.A) can be turned into spectral clustering problems, by following similar procedures as in spectral graph partitioning. The measure to minimize can be expressed in matrix form, obtaining similar expressions as for the cut size (see Eq. 18), with index vectors deﬁning the partition of the graph in groups through the values of their entries. For instance, for the minimum cut bipartition of Section IV.A, there is only one index vector s, whose components equal ±1, where the signs indicate the two clusters. The relaxation consists in performing the minimization over all possible vectors s, allowing for real-valued components as well. This version of the problem is exactly equivalent to spectral clustering. The relaxed minimization of ratio cut

for a partition in k clusters yields the n k-dimensional vertex vectors of unnormalized spectral clustering (von Luxburg, 2006); for normalized cut one obtains the n kdimensional vertex vectors of normalized spectral clustering, with the normalized Laplacian Lrw (Shi and Malik, 1997). The problem is then to turn the resulting vectors into a partition of the graph, which can be done by using techniques like k-means clustering, as we have seen above. However, it is still unclear what is the relation between the original minimum cut problem over actual graph partitions and the relaxed version of it, in particular how close one can come to the real solution via spectral clustering.

Random walks on graphs are also related to spectral clustering. In fact, by minimizing the number of edges between clusters (properly normalized for measures like, e. g., ratio cut and normalized cut) one forces random walkers to spend more time within clusters and to move more rarely from one cluster to another. In particular, unnormalized spectral clustering with the Laplacian Lrw has a natural link with random walks, because Lrw = I − D−1A (Section A.2), where D−1A is the transfer matrix T. This has interesting consequences. For instance, Meil˘ and Shi have proven that the normalized cut for a bipartition equals the total probability that a random walker moves from one of the clusters to the other in either sense (Meila and Shi, 2001). In this way, minimizing the normalized cut means looking for a partition minimizing the probability of transitions between clusters.

Spectral clustering requires the computation of the ﬁrst k eigenvectors of a Laplacian matrix. If the graph is large, an exact computation of the eigenvectors is impossible, as it would require a time O(n3). Fortunately there are approximate techniques, like the power method or Krylov subspace techniques like the Lanczos method (Golub and Loan, 1989), whose speed depends on the size of the eigengap |λk+1 − λk|, where λk and λk+1 are the k-th and (k + 1)-th smallest eigenvalue of the matrix. The larger the eigengap, the faster the convergence. In fact, the existence of large gaps between pairs of consecutive eigenvalues could suggest the number of clusters of the graph, an information which is not delivered by spectral clustering and which has to be given as input. We know that, for a disconnected graph with k components, the ﬁrst k eigenvalues of the Laplacian matrix (normalized or not) are zero, whether the (k + 1)-th is non-zero. If the clusters are weakly connected to each other, one expects that the ﬁrst k eigenvalues remain close to zero, and that the (k + 1)-th is clearly diﬀerent from zero. By reversing this argument, the number of clusters of a graph could be derived by checking whether there is an integer k such that the ﬁrst k eigenvalues are small and the (k+1)-th is relatively large. However, when the clusters are very mixed with each other, it may be hard to identify signiﬁcant gaps between the eigenvalues.

The last issue we want to point out concerns the choice of the Laplacian matrix to use in the applications. If the

graph vertices have the same or similar degrees, there is no substantial diﬀerence between the unnormalized and the normalized Laplacians. If there are big inhomogeneities among the vertex degrees, instead, the choice of the Laplacian considerably aﬀects the results. In general, normalized Laplacians are more promising because the corresponding spectral clustering techniques implicitly impose a double optimization on the set of partitions, such that the intracluster edge density is high and, at the same time, the intercluster edge density is low. On the contrary, the unnormalized Laplacian is related to the intercluster edge density only. Moreover, unnormalized spectral clustering does not always converge, and sometimes yields trivial partitions in which one or more clusters consist of a single vertex. Of the normalized Laplacians, Lrw is more reliable than Lsym because the eigenvectors of Lrw corresponding to the lowest eigenvalues are cluster indicator vectors, i. e., they have equal non-vanishing entries in correspondence of the vertices of each cluster, and zero elsewhere, if the clusters are disconnected. The eigenvectors of Lsym, instead, are obtained by (left-) multiplying those of Lrw by the matrix D1/2: in this way, eigenvector components corresponding to vertices of the same cluster are no longer equal, in general, a complication that may induce artefacts in the spectral clustering procedure.

###### V. DIVISIVE ALGORITHMS

A simple way to identify communities in a graph is to detect the edges that connect vertices of diﬀerent communities and remove them, so that the clusters get disconnected from each other. This is the philosophy of divisive algorithms. The crucial point is to ﬁnd a property of intercommunity edges that could allow for their identiﬁcation. Divisive methods do not introduce substantial conceptual advances with respect to traditional techniques, as they just perform hierarchical clustering on the graph at study (Section IV.B). The main diﬀerence with divisive hierarchical clustering is that here one removes inter-cluster edges instead of edges between pairs of vertices with low similarity and there is no guarantee a priori that inter-cluster edges connect vertices with low similarity. In some cases vertices (with all their adjacent edges) or whole subgraphs may be removed, instead of single edges. Being hierarchical clustering techniques, it is customary to represent the resulting partitions by means of dendrograms.

A. The algorithm of Girvan and Newman

The most popular algorithm is that proposed by Girvan and Newman (Girvan and Newman, 2002; Newman and Girvan, 2004). The method is historically important, because it marked the beginning of a new era in the ﬁeld of community detection and opened this topic to physi-

FIG. 10 Edge betweenness is highest for edges connecting communities. In the ﬁgure, the edge in the middle has a much higher betweenness than all other edges, because all shortest paths connecting vertices of the two communities run through it. Reprinted ﬁgure with permission from Ref. (Fortunato and Castellano, 2009). c 2009 by Springer.

cists. Here edges are selected according to the values of measures of edge centrality, estimating the importance of edges according to some property or process running on the graph. The steps of the algorithm are:

- 1. Computation of the centrality for all edges;
- 2. Removal of edge with largest centrality: in case of ties with other edges, one of them is picked at random;
- 3. Recalculation of centralities on the running graph;
- 4. Iteration of the cycle from step 2.


Girvan and Newman focused on the concept of betweenness, which is a variable expressing the frequency of the participation of edges to a process. They considered three alternative deﬁnitions: geodesic edge betweenness, random-walk edge betweenness and current-ﬂow edge betweenness. In the following we shall refer to them as edge betweenness, random-walk betweenness and current-ﬂow betweenness, respectively.

Edge betweenness is the number of shortest paths between all vertex pairs that run along the edge. It is an extension to edges of the popular concept of site betweenness, introduced by Freeman in 1977 (Freeman, 1977) and expresses the importance of edges in processes like information spreading, where information usually ﬂows through shortest paths. Historically edge betweenness was introduced before site betweenness in a never published technical report by Anthonisse (Anthonisse, 1971). It is intuitive that intercommunity edges have a large value of the edge betweenness, because many shortest paths connecting vertices of diﬀerent communities will pass through them (Fig. 10). As in the calculation of site betweenness, if there are two or more geodesic paths with the same endpoints that run through an edge, the contribution of each of them to the betweenness of the edge must be divided by the multiplicity of the paths, as one assumes that the signal/information propagates equally along each geodesic path. The betweenness of all edges of the graph can be calculated in a time that scales as O(mn), or O(n2) on a sparse graph, with techniques

based on breadth-ﬁrst-search (Brandes, 2001; Newman and Girvan, 2004; Zhou et al., 2006).

In the context of information spreading, one could imagine that signals ﬂow across random rather than geodesic paths. In this case the betweenness of an edge is given by the frequency of the passages across the edge of a random walker running on the graph (random-walk betweenness). A random walker moving from a vertex follows each adjacent edge with equal probability. A pair of vertices is chosen at random, s and t. The walker starts

- at s and keeps moving until it hits t, where it stops. One computes the probability that each edge was crossed by the walker, and averages over all possible choices for the vertices s and t. It is meaningful to compute the net crossing probability, which is proportional to the number of times the walk crossed the edge in one direction. In this way one neglects back and forth passages that are accidents of the random walk and tell nothing about the centrality of the edge. Calculation of random-walk betweenness requires the inversion of an n × n matrix (once), followed by obtaining and averaging the ﬂows for all pairs of nodes. The ﬁrst task requires a time O(n3), the second O(mn2), for a total complexity O[(m+n)n2], or O(n3) for a sparse matrix. The complete calculation requires a time O(n3) on a sparse graph.


Current-ﬂow betweenness is deﬁned by considering the graph a resistor network, with edges having unit resistance. If a voltage diﬀerence is applied between any two vertices, each edge carries some amount of current, that can be calculated by solving Kirchoﬀ’s equations. The procedure is repeated for all possible vertex pairs: the current-ﬂow betweenness of an edge is the average value of the current carried by the edge. It is possible to show that this measure is equivalent to random-walk betweenness, as the voltage diﬀerences and the random walks net ﬂows across the edges satisfy the same equations (Newman, 2005). Therefore, the calculation of current-ﬂow betweenness has the same complexity O[(m + n)n2], or O(n3) for a sparse graph.

Calculating edge betweenness is much faster than current-ﬂow or random walk betweenness [O(n2) versus

- O(n3) on sparse graphs]. In addition, in practical applications the Girvan-Newman algorithm with edge betweenness gives better results than adopting the other centrality measures (Newman and Girvan, 2004). Numerical studies show that the recalculation step 3 of Girvan-Newman algorithm is essential to detect meaningful communities. This introduces an additional factor m in the running time of the algorithm: consequently, the edge betweenness version scales as O(m2n), or O(n3) on a sparse graph. On graphs with strong community structure, that quickly break into communities, the recalculation step needs to be performed only within the connected component including the last removed edge (or the two components bridged by it if the removal of the edge splits a subgraph), as the edge betweenness of all other edges remains the same. This can help saving some computer time, although it is impossible to give estimates


of the gain since it depends on the speciﬁc graph at hand. Nevertheless, the algorithm is quite slow, and applicable to sparse graphs with up to n ∼ 10000 vertices, with current computational resources. In the original version of Girvan-Newman’s algorithm (Girvan and Newman, 2002), the authors had to deal with the whole hierarchy of partitions, as they had no procedure to say which partition is the best. In a successive reﬁnement (Newman and Girvan, 2004), they selected the partition with the largest value of modularity (see Section III.C.2), a criterion that has been frequently used ever since. The method can be simply extended to the case of weighted graphs, by suitably generalizing the edge betweenness. The betweenness of a weighted edge equals the betweenness of the edge in the corresponding unweighted graph, divided by the weight of the edge (Newman, 2004). There have been countless applications of the Girvan-Newman method: the algorithm is now integrated in well known libraries of network analysis programs.

Tyler et al. proposed a modiﬁcation of the GirvanNewman algorithm, to improve the speed of the calculation (Tyler et al., 2003; Wilkinson and Huberman, 2004). The gain in speed was required by the analysis of graphs of gene co-occurrences, which are too large to be analyzed by the algorithm of Girvan and Newman. Algorithms computing site/edge betweenness start from any vertex, taken as center, and compute the contribution to betweenness from all paths originating at that vertex; the procedure is then repeated for all vertices (Brandes, 2001; Newman and Girvan, 2004; Zhou et al., 2006). Tyler et al. proposed to calculate the contribution to edge betweenness only from a limited number of centers, chosen at random, deriving a sort of Monte Carlo estimate. Numerical tests indicate that, for each connected subgraph, it suﬃces to pick a number of centers growing as the logarithm of the number of vertices of the component. For a given choice of the centers, the algorithm proceeds just like that of Girvan and Newman. The stopping criterion is diﬀerent, though, as it does not require the calculation of modularity on the resulting partitions, but relies on a particular deﬁnition of community. According to such deﬁnition, a connected subgraph with n0 vertices is a community if the edge betweenness of any of its edges does not exceed n0 − 1. Indeed, if the subgraph consists of two parts connected by a single edge, the betweenness value of that edge would be greater than or equal to n0 − 1, with the equality holding only if one of the two parts consists of a single vertex. Therefore, the condition on the betweenness of the edges would exclude such situations, although other types of cluster structures might still be compatible with it. In this way, in the method of Tyler et al., edges are removed until all connected components of the partition are “communities” in the sense explained above. The Monte Carlo sampling of the edge betweenness necessarily induces statistical errors. As a consequence, the partitions are in general diﬀerent for diﬀerent choices of the set of center vertices. However, the authors showed that, by repeating the calculation

many times, the method gives good results on a network of gene co-occurrences (Wilkinson and Huberman, 2004), with a substantial gain of computer time. The technique has been also applied to a network of people corresponding via email (Tyler et al., 2003). In practical examples, only vertices lying at the boundary between communities may not be clearly classiﬁed, and be assigned sometimes to a group, sometimes to another. This is actually a nice feature of the method, as it allows to identify overlaps between communities, as well as the degree of membership of overlapping vertices in the clusters they belong to. The algorithm of Girvan and Newman, which is deterministic, is unable to accomplish this9. Another fast version of the Girvan-Newman algorithm has been proposed by Rattigan et al. (Rattigan et al., 2007). Here, a quick approximation of the edge betweenness values is carried out by using a network structure index, which consists of a set of vertex annotations combined with a distance measure (Rattigan et al., 2006). Basically one divides the graph into regions and computes the distances of every vertex from each region. In this way Rattigan et al. showed that it is possible to lower the complexity of the algorithm to O(m), by keeping a fair accuracy in the estimate of the edge betweenness values. This version of the Girvan-Newman algorithm gives good results on the benchmark graphs proposed by Brandes et al. (Brandes

- et al., 2003) (see also Section XV.A), as well as on a collaboration network of actors and on a citation network.


Chen and Yuan have pointed out that counting all possible shortest paths in the calculation of the edge betweenness may lead to unbalanced partitions, with communities of very diﬀerent size, and proposed to count only non-redundant paths, i. e. paths whose endpoints are all diﬀerent from each other: the resulting betweenness yields better results than standard edge betweenness for mixed clusters on the benchmark graphs of Girvan and Newman (Chen and Yuan, 2006). Holme et al. have used a modiﬁed version of the algorithm in which vertices, rather than edges, are removed (Holme et al., 2003). A centrality measure for the vertices, proportional to their site betweenness, and inversely proportional to their indegree, is chosen to identify boundary vertices, which are then iteratively removed with all their edges. This modiﬁcation, applied to study the hierarchical organization of biochemical networks, is motivated by the need to account for reaction kinetic information, that simple site betweenness does not include. The indegree of a vertex is solely used because it indicates the number of substrates to a metabolic reaction involving that vertex; for the purpose of clustering the graph is considered undirected, as usual.

9 It may happen that, at a given iteration, two or more edges of the graph have the same value of maximal betweenness. In this case one can pick any of them at random, which may lead in general to (slightly) diﬀerent partitions at the end of the computation.

The algorithm of Girvan and Newman is unable to ﬁnd overlapping communities, as each vertex is assigned to a single cluster. Pinney and Westhead have proposed a modiﬁcation of the algorithm in which vertices can be split between communities (Pinney and Westhead, 2006). To do that, they also compute the betweenness of all vertices of the graph. Unfortunately the values of edge and site betweenness cannot be simply compared, due to their diﬀerent normalization, but the authors remarked that the two endvertices of an inter-cluster edge should have similar betweenness values, as the shortest paths crossing one of them are likely to reach the other one as well through the edge. So they take the edge with largest betweenness and remove it only if the ratio of the betweenness values of its endvertices is between α and 1/α, with α = 0.8. Otherwise, the vertex with highest betweenness (with all its adjacent edges) is temporarily removed. When a subgraph is split by vertex or edge removal, all deleted vertices belonging to that subgraph are “copied” in each subcomponent, along with all their edges. Gregory (Gregory, 2007) has proposed a similar approach, named CONGA (Cluster Overlap NewmanGirvan Algorithm), in which vertices are split among clusters if their site betweenness exceeds the maximum value of the betweenness of the edges. A vertex is split by assigning some of its edges to one of its duplicates, and the rest to the other. There are several possibilities to do that, Gregory proposed to go for the split that yields the maximum of a new centrality measure, called split betweenness, which is the number of shortest paths that would run between two parts of a vertex if the latter were split. The method has a worst-case complexity O(m3), or O(n3) on a sparse graph, like the algorithm of Girvan and Newman. The code can be found at http://www.cs.bris.ac.uk/∼steve/networks/index. html.

B. Other methods

Another promising track to detect inter-cluster edges is related to the presence of cycles, i. e. closed nonintersecting paths, in the graph. Communities are characterized by a high density of edges, so it is reasonable to expect that such edges form cycles. On the contrary, edges lying between communities will hardly be part of cycles. Based on this intuitive idea, Radicchi et al. proposed a new measure, the edge clustering coeﬃcient, such that low values of the measure are likely to correspond to intercommunity edges (Radicchi et al., 2004). The edge clustering coeﬃcient generalizes to edges the notion of clustering coeﬃcient introduced by Watts and Strogatz for vertices (Watts and Strogatz, 1998) (Fig. 11). The clustering coeﬃcient of a vertex is the number of triangles including the vertex divided by the number of possible triangles that can be formed (Section A.1). The

![image 2](Community Detection in Graphs_images/imageFile2.png)

![image 3](Community Detection in Graphs_images/imageFile3.png)

![image 4](Community Detection in Graphs_images/imageFile4.png)

![image 5](Community Detection in Graphs_images/imageFile5.png)

![image 6](Community Detection in Graphs_images/imageFile6.png)

![image 7](Community Detection in Graphs_images/imageFile7.png)

![image 8](Community Detection in Graphs_images/imageFile8.png)

![image 9](Community Detection in Graphs_images/imageFile9.png)

![image 10](Community Detection in Graphs_images/imageFile10.png)

![image 11](Community Detection in Graphs_images/imageFile11.png)

![image 12](Community Detection in Graphs_images/imageFile12.png)

![image 13](Community Detection in Graphs_images/imageFile13.png)

![image 14](Community Detection in Graphs_images/imageFile14.png)

![image 15](Community Detection in Graphs_images/imageFile15.png)

- FIG. 11 Schematic illustration of the edge clustering coefﬁcient introduced by Radicchi et al. (Radicchi et al., 2004). The two grey vertices have ﬁve and six other neighbors, respectively. Of the ﬁve possible triangles based on the edge connecting the grey vertices, three are actually there, yielding an edge clustering coeﬃcient C3 = 3/5. Courtesy by F. Radicchi.


edge clustering coeﬃcient is deﬁned as

zi,j(g) + 1 s(i,jg)

C˜i,j(g) =

, (27)

where i and j are the extremes of the edge, zi,j(g) the number of cycles of length g built upon edge ij and s(i,jg) the possible number of cycles of length g that one could build based on the existing edges of i, j and their neighbors. The number of actual cycles in the numerator is augmented by 1 to enable a ranking among edges without cycles, which would all yield a coeﬃcient C˜i,j(g) equal to zero, independently of the degrees of the extremes

- i and j and their neighbors. Usually, cycles of length g = 3 (triangles) or 4 are considered. The measure is (anti)correlated with edge betweenness: edges with low edge clustering coeﬃcient usually have high betweenness and vice versa, although the correlation is not perfect. The method works as the algorithm by Girvan and Newman. At each iteration, the edge with smallest clustering coeﬃcient is removed, the measure is recalculated again, and so on. If the removal of an edge leads to a split of a subgraph in two parts, the split is accepted only if both clusters are LS-sets (“strong”) or “weak” communities (see Section III.B.2). The veriﬁcation of the community condition on the clusters is performed on the full adjacency matrix of the initial graph. If the condition were satisﬁed only for one of the two clusters, the initial subgraph may be a random graph, as it can be easily seen that by cutting a random graph ´ la Erd¨s and R´enyi in two parts, the larger of them is a strong (or weak) community with very high probability, whereas the smaller part is not. Enforcing the community condition on both clusters, it is more likely that the subgraph to


be split indeed has a cluster structure. Therefore, the algorithm stops when all clusters produced by the edge removals are communities in the strong or weak sense, and further splits would violate this condition. The authors suggested to use the same stopping criterion for the algorithm of Girvan and Newman, to get structurally welldeﬁned clusters. Since the edge clustering coeﬃcient is a local measure, involving at most an extended neighborhood of the edge, it can be calculated very quickly. The running time of the algorithm to completion is O(m4/n2), or O(n2) on a sparse graph, if g is small, so it is much shorter than the running time of the Girvan-Newman method. The recalculation step becomes slow if g is not so small, as in this case the number of edges whose coeﬃcient needs to be recalculated may reach a sizeable fraction of the edges of the graph; likewise, counting the number of cycles based on one edge becomes lengthier. If g ∼ 2d, where d is the diameter of the graph (which is usually a small number for real networks), the cycles span the whole graph and the measure becomes global and no more local. The computational complexity in this case exceeds that of the algorithm of Girvan and Newman, but it can come close to it for practical purposes even at lower values of g. So, by tuning g one can smoothly interpolate between a local and a global centrality measure. The software of the algorithm can be found in http://filrad.homelinux.org/Data/. In a successive paper (C. Castellano et al., 2004) the authors extended the method to the case of weighted networks, by modifying the edge clustering coeﬃcient of Eq. 27,

in that the number of cycles zi,j(g) is multiplied by the weight of the edge ij. The deﬁnitions of strong and

weak communities can be trivially extended to weighted graphs by replacing the internal/external degrees of the vertices/clusters with the corresponding strengths. More recently, the method has been extended to bipartite networks (Zhang et al., 2007), where only cycles of even length are possible (g = 4, 6, 8, etc.). The algorithm by Radicchi et al. may give poor results when the graph has few cycles, as it happens in some social and many nonsocial networks. In this case, in fact, the edge clustering coeﬃcient is small and fairly similar for most edges, and the algorithm may fail to identify the bridges between communities.

An alternative measure of centrality for edges is information centrality. It is based on the concept of efﬁciency (Latora and Marchiori, 2001), which estimates how easily information travels on a graph according to the length of shortest paths between vertices. The eﬃciency of a network is deﬁned as the average of the inverse distances between all pairs of vertices. If the vertices are “close” to each other, the eﬃciency is high. The information centrality of an edge is the relative variation of the eﬃciency of the graph if the edge is removed. In the algorithm by Fortunato et al. (Fortunato et al., 2004), edges are removed according to decreasing values of information centrality. The method is analogous to that of Girvan and Newman. Computing the informa-

tion centrality of an edge requires the calculation of the distances between all pairs of vertices, which can be done with breadth-ﬁrst-search in a time O(mn). So, in order to compute the information centrality of all edges one requires a time O(m2n). At this point one removes the edge with the largest value of information centrality and recalculates the information centrality of all remaining edges with respect to the running graph. Since the procedure is iterated until there are no more edges in the network, the ﬁnal complexity is O(m3n), or O(n4) on a sparse graph. The partition with the largest value of modularity is chosen as most representative of the community structure of the graph. The method is much slower than the algorithm of Girvan and Newman. Partitions obtained with both techniques are rather consistent, mainly because information centrality has a strong correlation with edge betweenness. The algorithm by Fortunato et al. gives better results when communities are mixed, i. e. with a high degree of interconnectedness, but it tends to isolate leaf vertices and small loosely bound subgraphs.

A measure of vertex centrality based on loops, similar to the clustering coeﬃcient by Watts and Strogatz (Watts and Strogatz, 1998), has been introduced by Vragoviˆc and Louis (Vragovi´c and Louis, 2006). The idea is that neighbors of a vertex well inside a community are “close” to each other, even in the absence of the vertex, due to the high density of intra-cluster edges. Suppose that j and k are neighbors of a vertex i: djk/i is the length of a shortest path between j and k, if i is removed from the graph. Naturally, the existence of alternative paths to j − i − k implies the existence of loops in the graph. Vragoviˆc and Louis deﬁned the loop coeﬃcient of i as the average of 1/djk/i over all pairs of neighbors of i, somewhat reminding of the concept of information centrality used in the method by Fortunato et al. (Fortunato

- et al., 2004). High values of the loop coeﬃcient are likely to identify core vertices of communities, whereas low values correspond to vertices lying at the boundary between communities. Clusters are built around the vertices with highest values of the loop coeﬃcient. The method has time complexity O(nm); its results are not so accurate, as compared to popular clustering techniques.


###### VI. MODULARITY-BASED METHODS

Newman-Girvan modularity Q (Section III.C.2), originally introduced to deﬁne a stopping criterion for the algorithm of Girvan and Newman, has rapidly become an essential element of many clustering methods. Modularity is by far the most used and best known quality function. It represented one of the ﬁrst attempts to achieve a ﬁrst principle understanding of the clustering problem, and it embeds in its compact form all essential ingredients and questions, from the deﬁnition of community, to the choice of a null model, to the expression of the “strength” of communities and partitions. In this section we shall focus on all clustering techniques that require

modularity, directly and/or indirectly. We will examine fast techniques that can be used on large graphs, but which do not ﬁnd good optima for the measure (Blondel et al., 2008; Clauset et al., 2004; Danon et al., 2006; Du et al., 2007; Mei et al., 2009; Newman, 2004b; Noack and Rotta, 2009; Pujol et al., 2006; Schuetz and Caﬂisch, 2008a,b; Wakita and Tsurumi, 2007; Xiang et al., 2009); more accurate methods, which are computationally demanding (Guimer` et al., 2004; Massen and Doye, 2005; Medus et al., 2005); algorithms giving a good tradeoﬀ between high accuracy and low complexity (Duch and Arenas, 2005; Lehmann and Hansen, 2007; Newman, 2006b; Ruan and Zhang, 2007; White and Smyth, 2005). We shall also point out other properties of modularity, discuss some extensions/modiﬁcations of it, as well as highlight its limits.

A. Modularity optimization

By assumption, high values of modularity indicate good partitions10. So, the partition corresponding to its maximum value on a given graph should be the best, or at least a very good one. This is the main motivation for modularity maximization, by far the most popular class of methods to detect communities in graphs. An exhaustive optimization of Q is impossible, due to the huge number of ways in which it is possible to partition a graph, even when the latter is small. Besides, the true maximum is out of reach, as it has been recently proved that modularity optimization is an NP-complete problem (Brandes et al., 2006), so it is probably impossible to ﬁnd the solution in a time growing polynomially with the size of the graph. However, there are currently several algorithms able to ﬁnd fairly good approximations of the modularity maximum in a reasonable time.

1. Greedy techniques

The ﬁrst algorithm devised to maximize modularity was a greedy method of Newman (Newman, 2004b). It is an agglomerative hierarchical clustering method, where groups of vertices are successively joined to form larger communities such that modularity increases after the merging. One starts from n clusters, each containing a single vertex. Edges are not initially present, they are added one by one during the procedure. However, the modularity of partitions explored during the procedure is always calculated from the full topology of the graph, as we want to ﬁnd the modularity maximum on the space of partitions of the full graph. Adding a ﬁrst edge to the set of disconnected vertices reduces the number of groups from n to n−1, so it delivers a new partition of the graph.

10 This is not true in general, as we shall discuss in Section VI.C.

The edge is chosen such that this partition gives the maximum increase (minimum decrease) of modularity with respect to the previous conﬁguration. All other edges are added based on the same principle. If the insertion of an edge does not change the partition, i. e. the edge is internal to one of the clusters previously formed, modularity stays the same. The number of partitions found during the procedure is n, each with a diﬀerent number of clusters, from n to 1. The largest value of modularity in this subset of partitions is the approximation of the modularity maximum given by the algorithm. At each iteration step, one needs to compute the variation ∆Q of modularity given by the merger of any two communities of the running partition, so that one can choose the best merger. However, merging communities between which there are no edges can never lead to an increase of Q, so one has to check only the pairs of communities which are connected by edges, of which there cannot be more than m. Since the calculation of each ∆Q can be done in constant time, this part of the calculation requires a

- time O(m). After deciding which communities are to be


merged, one needs to update the matrix eij expressing the fraction of edges between clusters i and j of the running partition (necessary to compute Q), which can be done in a worst-case time O(n). Since the algorithm requires n − 1 iterations (community mergers) to run to completion, its complexity is O((m + n)n), or O(n2) on a sparse graph, so it enables one to perform a clustering analysis on much larger networks than the algorithm of Girvan and Newman (up to an order of 100000 vertices with current computers). In a later paper (Clauset et al.,

- 2004), Clauset et al. pointed out that the update of the


matrix eij in Newman’s algorithm involves a large number of useless operations, due to the sparsity of the adjacency matrix. This operation can be performed more efﬁciently by using data structures for sparse matrices, like max-heaps, which rearrange the data in the form of binary trees. Clauset et al. maintained the matrix of modularity variations ∆Qij, which is also sparse, a max-heap containing the largest elements of each row of the matrix ∆Qij as well as the labels of the corresponding communities, and a simple array whose elements are the sums of the elements of each row of the old matrix eij. The optimization of modularity can be carried out using these three data structures, whose update is much quicker than in Newman’s technique. The complexity of the algorithm is O(mdlog n), where d is the depth of the dendrogram describing the successive partitions found during the execution of the algorithm, which grows as log n for graphs with a strong hierarchical structure. For those graphs, the running time of the method is then O(nlog2 n), which allows to analyse the community structure of very large graphs, up to 106 vertices. The greedy optimization of Clauset et al. is currently one of the few algorithms that can be used to estimate the modularity maximum on such large graphs. The code can be freely downloaded from http://cs.unm.edu/∼aaron/research/fastmodulari ty.htm.

This greedy optimization of modularity tends to form quickly large communities at the expenses of small ones, which often yields poor values of the modularity maxima. Danon et al. suggested to normalize the modularity variation ∆Q produced by the merger of two communities by the fraction of edges incident to one of the two communities, in order to favor small clusters (Danon et al., 2006). This trick leads to better modularity optima as compared to the original recipe of Newman, especially when communities are very diﬀerent in size. Wakita and Tsurumi (Wakita and Tsurumi, 2007) have noticed that, due to the bias towards large communities, the fast algorithm by Clauset et al. is ineﬃcient, because it yields very unbalanced dendrograms, for which the relation d ∼ log n does not hold, and as a consequence the method often runs at its worst-case complexity. To improve the situation they proposed a modiﬁcation in which, at each step, one seeks the community merger delivering the largest value of the product of the modularity variation ∆Q times a factor (consolidation ratio), that peaks for communities of equal size. In this way there is a tradeoﬀ between the gain in modularity and the balance of the communities to merge, with a big gain in the speed of the procedure, that enables the analysis of systems with up to 107 vertices. Interestingly, this modiﬁcation often leads to better modularity maxima than those found with the version of Clauset et al., at least on large social networks. The code can be found at http://www.is.titech.ac.jp/∼wakita/en/software /community-analysis-software/. Another trick to avoid the formation of large communities was proposed by Schuetz and Caﬂisch and consists in allowing for the merger of more community pairs, instead of one, at each iteration (Schuetz and Caﬂisch, 2008a,b). This generates several “centers” around which communities are formed, which grow simultaneously so that a condensation into a few large clusters is unlikely. This modiﬁed version of the greedy algorithm is combined with a simple reﬁnement procedure in which single vertices are moved to the neighboring community that yields the maximum increase of modularity. The method has the same complexity of the fast optimization by Clauset et al., but comes closer to the modularity maximum. The software is available at http://www.biochem-caflisch.uzh.ch/public/5/net work-clusterization-algorithm.html. The accuracy of the greedy optimization can be signiﬁcantly improved if the hierarchical agglomeration is started from some reasonable intermediate conﬁguration, rather than from the individual vertices (Du et al., 2007; Pujol et al., 2006). Xiang et al. suggested to start from a conﬁguration obtained by merging the original isolated vertices into larger subgraphs, according to the values of a measure of topological similarity between subgraphs (Xiang et al., 2009). A similar approach has been described by Ye et al. (Ye et al., 2008): here the initial partition is such that no single vertex can be moved from its cluster to another without decreasing Q. Higher-quality modularities can be also achieved by

applying reﬁnement strategies based on local search at various steps of the greedy agglomeration (Noack and Rotta, 2009). Such reﬁnement procedures are similar to the technique proposed by Newman to improve the results of his spectral optimization of modularity ((Newman, 2006b) and Section VI.A.4). Another good strategy consists in alternating greedy optimization with stochastic perturbations of the partitions (Mei et al., 2009).

- A diﬀerent greedy approach has been introduced by


Blondel et al. (Blondel et al., 2008), for the general case of weighted graphs. Initially, all vertices of the graph are put in diﬀerent communities. The ﬁrst step consists of a sequential sweep over all vertices. Given a vertex i, one computes the gain in weighted modularity (Eq. 35) coming from putting i in the community of its neighbor

- j and picks the community of the neighbor that yields the largest increase of Q, as long as it is positive. At the end of the sweep, one obtains the ﬁrst level partition. In the second step communities are replaced by supervertices, and two supervertices are connected if there is at least an edge between vertices of the corresponding communities. In this case, the weight of the edge between the supervertices is the sum of the weights of the edges between the represented communities at the lower level. The two steps of the algorithm are then repeated, yielding new hierarchical levels and supergraphs (Fig. 12). We remark that modularity is always computed from the initial graph topology: operating on supergraphs enables one to consider the variations of modularity for partitions of the original graph after merging and/or splitting of groups of vertices. Therefore, at some iteration, modularity cannot increase anymore, and the algorithm stops. The technique is more limited by storage demands than by computational time. The latter grows like O(m), so the algorithm is extremely fast and graphs with up to 109 edges can be analyzed in a reasonable time on current computational resources. The software can be found at http://findcommunities.googlepages.com/. The modularity maxima found by the method are better than those found with the greedy techniques by Clauset et al. (Clauset et al., 2004) and Wakita and Tsurumi (Wakita and Tsurumi, 2007). However, closing communities within the immediate neighborhood of vertices may be inaccurate and yield spurious partitions in practical cases. So, it is not clear whether some of the intermediate partitions could correspond to meaningful hierarchical levels of the graph. Moreover, the results of the algorithm depend on the order of the sequential sweep over the vertices.


We conclude by stressing that, despite the improvements and reﬁnements of the last years, the accuracy of greedy optimization is not that good, as compared with other techniques.

- 2. Simulated annealing

Simulated annealing (Kirkpatrick et al., 1983) is a probabilistic procedure for global optimization used in diﬀerent ﬁelds and problems. It consists in performing an exploration of the space of possible states, looking for the global optimum of a function F, say its maximum. Transitions from one state to another occur with probability 1 if F increases after the change, otherwise with a probability exp(β∆F), where ∆F is the decrease of the function and β is an index of stochastic noise, a sort of inverse temperature, which increases after each iteration. The noise reduces the risk that the system gets trapped in local optima. At some stage, the system converges to a stable state, which can be an arbitrarily good approximation of the maximum of F, depending on how many states were explored and how slowly β is varied. Simulated annealing was ﬁrst employed for modularity optimization by Guimer` et al. (Guimer` et al., 2004). Its standard implementation (Guimer` and Amaral, 2005) combines two types of “moves”: local moves, where a single vertex is shifted from one cluster to another, taken at random; global moves, consisting of mergers and splits of communities. Splits can be carried out in several distinct ways. The best performance is achieved if one optimizes the modularity of a bipartition of the cluster, taken as an isolated graph. This is done again with simulated annealing, where one considers only individual vertex movements, and the temperature is decreased until it reaches the running value for the global optimization. Global moves reduce the risk of getting trapped in local minima and they have proven to lead to much better optima than using simply local moves (Massen and Doye, 2005; Medus et al., 2005). In practical applications, one typically combines n2 local moves with n global ones in one iteration. The method can potentially come very close to the true modularity maximum, but it is slow. The actual complexity cannot be estimated, as it heavily depends on the parameters chosen for the optimization (initial temperature, cooling factor), not only on the graph size. Simulated annealing can be used for small graphs, with up to about 104 vertices.

- 3. Extremal optimization


Extremal optimization (EO) is a heuristic search procedure proposed by Boettcher and Percus (Boettcher and Percus, 2001), in order to achieve an accuracy comparable with simulated annealing, but with a substantial gain in computer time. It is based on the optimization of local variables, expressing the contribution of each unit of the system to the global function at study. This technique was used for modularity optimization by Duch and Arenas (Duch and Arenas, 2005). Modularity can be indeed written as a sum over the vertices: the local modularity of a vertex is the value of the corresponding term in this sum. A ﬁtness measure for each vertex is obtained by

![image 16](Community Detection in Graphs_images/imageFile16.png)

- FIG. 12 Hierarchical optimization of modularity by Blondel et al. (Blondel et al., 2008). The diagram shows two iterations of the method, starting from the graph on the left. Each iteration consists of a step, in which every vertex is assigned to the (local) cluster that produces the largest modularity increase, followed by a successive transformation of the clusters into vertices of a smaller (weighted) graph, representing the next higher hierarchical level. Reprinted ﬁgure with permission from Ref. (Blondel


- et al., 2008). c 2008 by IOP Publishing and SISSA.


dividing the local modularity of the vertex by its degree, as in this case the measure does not depend on the degree of the vertex and is suitably normalized. One starts from a random partition of the graph in two groups with the same number of vertices. At each iteration, the vertex with the lowest ﬁtness is shifted to the other cluster. The move changes the partition, so the local ﬁtnesses of many vertices need to be recalculated. The process continues until the global modularity Q cannot be improved any more by the procedure. This technique reminds one of the Kernighan-Lin (Kernighan and Lin, 1970) algorithm for graph partitioning (Section IV.A), but here the sizes of the communities are determined by the process itself, whereas in graph partitioning they are ﬁxed from the beginning. After the bipartition, each cluster is considered as a graph on its own and the procedure is repeated, as long as Q increases for the partitions found. The procedure, as described, proceeds deterministically from the given initial partition, as one shifts systematically the vertex with lowest ﬁtness, and is likely to get trapped in local optima. Better results can be obtained if one introduces a probabilistic selection, in which vertices are ranked based on their ﬁtness values and one picks the vertex of rank q with the probability P(q) ∼ q−τ (τ-EO,

(Boettcher and Percus, 2001)). The algorithm ﬁnds very good estimates of the modularity maximum, and performs very well on the benchmark of Girvan and Newman (Girvan and Newman, 2002) (Section XV.A) . Ranking the ﬁtness values has a cost O(nlog n), which can be reduced to O(n) if heap data structures are used. Choosing the vertex to be shifted can be done with a binary search, which amounts to an additional factor O(log n). Finally, the number of steps needed to verify whether the running modularity maximum can be improved or not is also O(n). The total complexity of the method is then O(n2 log n). We conclude that EO represents a good tradeoﬀ between accuracy and speed, although the use of recursive bisectioning may lead to poor results on large networks with many communities.

4. Spectral optimization

Modularity can be optimized using the eigenvalues and eigenvectors of a special matrix, the modularity matrix B, whose elements are

kikj 2m

Bij = Aij −

. (28)

Here the notation is the same used in Eq. 14. Let s be the vector representing any partition of the graph in two clusters A and B: si = +1 if vertex i belongs to A, si = −1 if i belongs to B. Modularity can be written as

- 1

- 2m ij


kikj 2m

Aij −

Q =

δ(Ci,Cj)

1 4m ij

kikj 2m

Aij −

=

(sisj + 1)

1 4m ij

1 4m

sTBs. (29)

=

Bijsisj =

The last expression indicates standard matrix products. The vector s can be decomposed on the basis of eigenvectors ui (i = 1,...,n) of the modularity matrix B: s = i aiui, with ai = uTi · s. By plugging this expression of s into Eq. 29 one ﬁnally gets

1 4m i

Q =

aiuTi B

j

1 4m

ajuj =

n

(uTi · s)2βi, (30)

i=1

where βi is the eigenvalue of B corresponding to the eigenvector ui. Eq. 30 is analogous to Eq. 19 for the cut size of the graph partitioning problem. This suggests that one can optimize modularity on bipartitions via spectral bisection (Section IV.A), by replacing the Laplacian matrix with the modularity matrix (Newman, 2006a,b). Like the Laplacian matrix, B has always the trivial eigenvector (1,1,...,1) with eigenvalue zero, because the sum of the elements of each row/column of the matrix vanishes. From Eq. 30 we see that, if B has no positive eigenvalues, the maximum coincides with the trivial partition consisting of the graph as a single cluster (for which Q = 0), i. e. it has no community structure. Otherwise, one has to look for the eigenvector of B with largest (positive) eigenvalue, u1, and group the vertices according to the signs of the components of u1, just like

- in Section IV.A. Here, however, one does not need to specify the sizes of the two groups: the vertices with positive components are all in one group, the others in the other group. If, for example, the component of u1 corresponding to vertex i is positive, but we set si = −1, the modularity is lower than by setting si = +1. The values of the components of u1 are also informative, as they indicate the level of the participation of the vertices to their communities. In particular, components whose values are close to zero lie at the border between the two clusters and can be well considered as belonging to both of them. The result obtained from the spectral bipartition can be further improved by shifting single vertices from one community to the other, such to have the highest increase (or lowest decrease) of the modularity of the resulting graph partition. This reﬁnement technique, similar to the Kernighan-Lin algorithm (Section IV.A), can be also applied to improve the results of other optimization techniques (e.g. greedy algorithms, extremal optimization, etc.). The procedure is repeated for each


of the clusters separately, and the number of communities increases as long as modularity does. At variance with graph partitioning, where one needs to ﬁx the number of clusters and their size beforehand, here there is a clear-cut stopping criterion, represented by the fact that cluster subdivisions are admitted only if they lead to a modularity increase. We stress that modularity needs to be always computed from the full adjacency matrix of the original graph11. The drawback of the method is similar as for spectral bisection, i. e. the algorithm gives the best results for bisections, whereas it is less accurate when the number of communities is larger than two. Recently, Sun et al. (Sun et al., 2009) have added a step after each bipartition of a cluster, in that single vertices can be moved from one cluster to another and even form the seeds of new clusters. We remark that the procedure is diﬀerent from the Kernighan-Lin-like reﬁning steps, as here the number of clusters can change. This variant, which does not increase the complexity of the original spectral optimization, leads to better modularity maxima. Moreover, one does not need to stick to bisectioning, if other eigenvectors with positive eigenvalues of the modularity matrix are used. Given the ﬁrst p eigenvectors, one can construct n p-dimensional vectors, each corresponding to a vertex, just like in spectral partitioning (Section IV.D). The components of the vector of vertex i are proportional to the p entries of the eigenvectors in position i. Then one can deﬁne community vectors, by summing the vectors of vertices in the same community. It is possible to show that, if the vectors of two communities form an angle larger that π/2, keeping the communities separate yields larger modularity than if they are merged (Fig. 13). In this way, in a p-dimensional space the modularity maximum corresponds to a partition in at most p + 1 clusters. Community vectors were used by Wang et al. to obtain high-modularity partitions into a number of communities smaller than a given maximum (Wang et al., 2008). In particular, if one takes the eigenvectors corresponding to the two largest eigenvalues, one can obtain a split of the graph in three clusters: in a recent work, Richardson et al. presented a fast technique to obtain graph tripartitions with large modularity along these lines (Richardson et al., 2009). The eigenvectors with the most negative eigenvalues can also be used to extract useful information, like the presence of a possible multipartite structure of the graph, as they give the most relevant contribution to the modularity minimum.

The spectral optimization of modularity is quite fast. The leading eigenvector of the modularity matrix can be computed with the power method, by repeatedly multiplying B by an arbitrary vector (not orthogonal to

11 Richardson et al. (Richardson et al., 2009) have actually shown that if one instead seeks the optimization of modularity for each cluster, taken as an independent graph, the combination of spectral bisectioning and the post-processing technique may yield better results for the ﬁnal modularity optima.

graph G. A partition of G in k clusters can be described through an n × k assignment matrix X, where xic = 1 if vertex i belongs to cluster c, otherwise xic = 0. It can be easily shown that, up to a multiplicative constant, modularity can be rewritten in terms of the matrix X as

| | | | | | | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | |


- FIG. 13 Spectral optimization of modularity by Newman (Newman, 2006a,b). By using the ﬁrst two eigenvectors of the modularity matrix, vertices can be represented as points on a plane. By cutting the plane with a line passing through the origin (like the dashed line in the ﬁgure) one obtains bipartitions of the graph with possibly high modularity values. Reprinted ﬁgure with permission from Ref. (Newman,


- 2006a). c 2006 by the American Physical Society.


u1). The number of required iterations to reach convergence is O(n). Each multiplication seems to require a

- time O(n2), as B is a complete matrix, but the peculiar form of B allows for a much quicker calculation, taking time O(m + n). So, a graph bipartition requires a time O[n(m + n)], or O(n2) on a sparse graph. To ﬁnd the modularity optimum one needs a number of subsequent bipartitions that equals the depth d of the resulting hierarchical tree. In the worst-case scenario, d = O(n), but in practical cases the procedure usually stops much before reaching the leaves of the dendrogram, so one could go for the average value d ∼ log n, for a total complexity of O(n2 log n). The algorithm is faster than extremal optimization and it is also slightly more accurate, especially for large graphs. The modularity matrix and the corresponding spectral optimization can be trivially extended to weighted graphs.


- A diﬀerent spectral approach had been previously pro-


posed by White and Smyth (White and Smyth, 2005). Let W indicate the weighted adjancency matrix of a

Q ∝ tr[XT(W − D)X] = −tr[XTLQX], (31)

where W is a diagonal matrix with identical elements, equal to the sum of all edge weights, and the entries of D are Dij = kikj, where ki is the degree of vertex i. The matrix LQ = D − W is called the Q-Laplacian. Finding the assignment matrix X that maximizes Q is an NPcomplete problem, but one can get a good approximation by relaxing the constraint that the elements of X have to be discrete. By doing so Q becomes a sort of continuous functional of X and one can determine the extremes of Q by setting its ﬁrst derivative (with respect to X) to zero. This leads to the eigenvalue problem

###### LQX = XΛ. (32)

Here Λ is a diagonal matrix. Eq. 32 turns modularity maximization into a spectral graph partitioning problem (Section IV.D), using the Q-Laplacian matrix. A nice feature of the Q-Laplacian is that, for graphs which are not too small, it can be approximated (up to constant factors) by the transition matrix W˜, obtained by normalizing W such that the sum of the elements of each row equals one. Eq. 32 is at the basis of the algorithms developed by White and Smyth, which search for partitions with at most K clusters, where K is a predeﬁned input parameter that may be suggested by preliminary information on the graph cluster structure. The ﬁrst K −1 eigenvectors of the transition matrix W˜ (excluding the trivial eigenvector with all equal components) can be computed with a variant of the Lanczos method (Demmel et al., 2000). Since the eigenvector components are not integer, the eigenvectors do not correspond directly to a partition of the graph in clusters. However, as usual in spectral graph partitioning, the components of the eigenvectors can be used as coordinates of the graph vertices in an Euclidean space and k-means clustering is applied to obtain the desired partition. White and Smyth proposed two methods to derive the clustering after embedding the graph in space. Both methods have a worstcase complexity O(K2n + Km), which is essentially linear in the number of vertices of the graph if the latter is sparse and K n. However, on large and sparse graphs, K could scale with the number of vertices n, so the procedure might become quite slow. In order to speed up calculations without losing much accuracy in the ﬁnal estimates of the maximum modularity, Ruan and Zhang (Ruan and Zhang, 2007) have proposed an algorithm, called Kcut, that applies recursively the method by White and Smyth, in a slightly modiﬁed form: after a ﬁrst application to the full graph, in the next iteration the method is applied to all clusters of the ﬁrst partition, treated as independent networks, and so on. The procedure goes on as long as the modularity of the resulting

partitions keeps growing. The advantage of Kcut is that one can play with low values for the (maximal) number of clusters at each iteration; if partitions are balanced, after a levels of recursions, the number of clusters of the partition is approximately K = a. Therefore the complexity of Kcut is O[(n+m)log K] for a ﬁnal partition in (at most) K clusters, which is much lower than the complexity of the algorithm by White and Smyth. Ruan and Zhang tested Kcut on artiﬁcial graphs generated with the planted -partition model (Section XV), and on real networks including Zachary’s karate club (Zachary, 1977), the American college football network (Girvan and Newman, 2002) and two collaboration networks of Jazz musicians (Gleiser and Danon, 2003) and physicists (Newman,

- 2001): the accuracy of Kcut is comparable to that of the algorithm by White and Smyth, though generally lower.


- 5. Other optimization strategies


Agarwal and Kempe have suggested to maximize modularity within the framework of mathematical programming (Agarwal and Kempe, 2008). In fact, modularity optimization can be formulated both as a linear and as a quadratic program. In the ﬁrst case, the variables are deﬁned on the links: xij = 0 if i and j are in the same cluster, otherwise xij = 1. The modularity of a partition, up to a multiplicative constant, can then be written as

Q ∝

ij

Bij(1 − xij), (33)

where B is the modularity matrix deﬁned by Newman (see Section VI.A.4). Eq. 33 is linear in the variables {x}, which must obey the constraint xij ≤ xik +xkj, because, if i and j are in the same cluster, and so are i and

- k, then j and k must be in that cluster too. Maximizing the expression in Eq. 33 under the above constraint is NP-hard, if the variables have to be integer as required. However, if one relaxes this condition by using real-valued {x}, the problem can be solved in polynomial time (Karloﬀ, 1991). On the other hand, the solution does not correspond to an actual partition, as the x variables are fractional. To get clusters out of the {x} one needs a rounding step. The values of the x variables are used as sort of distances in a metric space (the triangular inequality is satisﬁed by construction): clusters of vertices “close” enough to each other (i. e. whose mutual


- x variables are close to zero) are formed and removed until each vertex is assigned to a cluster. The resulting partition is further reﬁned with the same post-processing technique used by Newman for the spectral optimization of modularity, i. e. by a sequence of steps similar to those of the algorithm by Kernighan and Lin (see Sec-


- tion VI.A.4). Quadratic programming can be used to get bisections of graphs with high modularity, that can be iterated to get a whole hierarchy of partitions as in Newman’s spectral optimization. One starts from one of


the identities in Eq. 29

1 4m ij

Q =

Bij(1 + sisj), (34)

where si = ±1, depending on whether the vertex belongs to the ﬁrst or the second cluster. Since the optimization of the expression in Eq. 34 is NP-complete, one must relax again the constraint on the variables s being integer. A possibility is to transform each s into an n-dimensional vector s and each product in the scalar product between vectors. The vectors are normalized so that their tips lie on the unit-sphere of the n-dimensional space. This vector problem is polynomially solvable, but one needs a method to associate a bipartition to the set of n vectors of the solution. Any (n − 1)-dimensional hyperplane centered at the origin cuts the space in two halves, separating the vectors in two subsets. One can then choose multiple random hyperplanes and pick the one which delivers the partition with highest modularity. As in the linear program, a post-processing technique a´ la Newman (see Section VI.A.4) is used to improve the results of the procedure. The two methods proposed by Agarwal and Kempe are strongly limited by their high computational complexity, due mostly to the large storage demands, making graphs with more than 104 vertices intractable. On the other hand, the idea of applying mathematical programming to graph clustering is promising. The code of the algorithms can be downloaded from http://www-scf.usc.edu/∼gaurava/. In a recent work (G. Xu et al., 2007), Xu et al. have optimized modularity using mixed-integer mathematical programming, with both integer and continuous variables, obtaining very good approximations of the modularity optimum, at the price of high computational costs. Chen et al. have used integer linear programming to transform the initial graph into an optimal target graph consisting of disjoint cliques, which eﬀectively yields a partition (Chen et al., 2008). Berry et al. have formulated the problem of graph clustering as a facility location problem (Hillier and Lieberman, 2004), consisting in the minimization of a cost function based on a local variation of modularity (Berry et al., 2007).

Lehmann and Hansen (Lehmann and Hansen, 2007) optimized modularity via mean ﬁeld annealing (Peterson and Anderson, 1987), a deterministic alternative to simulated annealing (Kirkpatrick et al., 1983). The method uses Gibbs probabilities to compute the conditional mean value for the variable of a vertex, which indicates its community membership. By making a mean ﬁeld approximation on the variables of the other vertices in the Gibbs probabilities one derives a self-consistent set of non-linear equations, that can be solved by iteration in a time O[(m + n)n]. The method yields better modularity maxima than the spectral optimization by Newman (Section VI.A.4), at least on artiﬁcial graphs with builtin community structure, similar to the benchmark graphs by Girvan and Newman (Section XV.A).

Genetic algorithms (Holland, 1992) have also been used to optimize modularity. In a standard genetic algorithm one has a set of candidate solutions to a problem, which are numerically encoded as chromosomes, and an objective function to be optimized on the space of solutions. The objective function plays the role of biological ﬁtness for the chromosomes. One usually starts from a random set of candidate solutions, which are progressively changed through manipulations inspired by biological processes regarding real chromosomes, like point mutation (random variations of some parts of the chromosome) and crossing over (generating new chromosomes by merging parts of existing chromosomes). Then, the ﬁtness of the new pool of candidates is computed and the chromosomes with the highest ﬁtness have the greatest chances to survive in the next generation. After several iterations only solutions with large ﬁtness survive. In a work by Tasgin et al. (Tasgin et al., 2007), partitions are the chromosomes and modularity is the ﬁtness function. With a suitable choice of the algorithm parameters, like the number of chromosomes and the rates of mutation and crossing over, Tasgin et al. could obtain results of comparative quality as greedy modularity optimization on Zachary’s karate club (Zachary, 1977), the college football network (Girvan and Newman, 2002) and the benchmark by Girvan and Newman (Section XV.A). Genetic algorithms were also adopted by Liu et al. (Liu et al., 2007). Here the maximum modularity partition is obtained via successive bipartitions of the graph, where each bipartition is determined by applying a genetic algorithm to each subgraph (starting from the original graph itself), which is considered isolated from the rest of the graph. A bipartition is accepted only if it increases the total modularity of the graph.

In Section III.C.2 we have seen that the modularity maximum is obtained for the partition that minimizes the diﬀerence between the cut size and the expected cut size of the partition (Eq. 17). In the complete weighted graph Gw such that the weight wij of an edge is 1 − kikj/2m, if i and j are connected in G, and −kikj/2m if they are not, the diﬀerence |CutP| − ExCutP is simply the cut size of partition P. So, maximizing modularity for G is equivalent to the problem of ﬁnding the partition with minimal cut size of the weighted graph Gw, i. e. to a graph partitioning problem. The problem can then be eﬃciently solved by using existing software for graph partitioning (Djidjev, 2007).

- B. Modiﬁcations of modularity


In the most recent literature on graph clustering several modiﬁcations and extensions of modularity can be found. They are usually motivated by speciﬁc classes of clustering problems and/or graphs that one may want to analyze.

Modularity can be easily extended to graphs with weighted edges (Newman, 2004). One needs to replace

the degrees ki and kj in Eq. 14 with the strengths si and sj of vertices i and j. We remind that the strength of a vertex is the sum of the weights of edges adjacent to the vertex (Section A.1). For a proper normalization, the number of edges m in Eq. 14 has to be replaced by the sum W of the weights of all edges. The product sisj/2W is now the expected weight of the edge ij in the null model of modularity, which has to be compared with the actual weight Wij of that edge in the original graph. This can be understood if we consider the case in which all weights are multiples of a unit weight, so they can be rewritten as integers. The weight of the connection between two nodes can then be replaced by as many edges between the nodes as expressed by the number of weight units. For the resulting multigraph we can use the same procedure as in the case of unweighted graphs, which leads to the formally identical expression

- 1

- 2W ij


Qw =

sisj 2W

Wij −

δ(Ci,Cj), (35)

which can be also written as a sum over the modules

nc

Q =

c=1

Wc W −

Sc 2W

2

, (36)

where Wc is the sum of the weights of the internal edges of module c and Sc is the sum of the strengths of the vertices of c. If edge weights are not mutually commensurable, one can always represent them as integers with good approximation, provided a suﬃciently small weight unit is adopted, so the expressions for weighted modularity of Eqs. 35, 36 are generally valid. In principle, weights can be assigned to the edges of an undirected graph, by using any measure of similarity/correlation between the vertices (like, e. g., the measures introduced in Section III.B.4). In this way, one could derive the corresponding weighted modularity and use it to detect communities, with a potentially better exploitation of the structural information of the graph as compared to standard modularity (Feng et al., 2007; Ghosh and Lerman, 2008).

Modularity has also a straightforward extension to the case of directed graphs (Arenas et al., 2007; Leicht and Newman, 2008). If an edge is directed, the probability that it will be oriented in either of the two possible directions depends on the in- and out-degrees of the endvertices. For instance, taken two vertices A and B, where

- A (B) has a high (low) indegree and low (high) outdegree, in the null model of modularity an edge will be much more likely to point from B to A than from A to
- B. Therefore, the expression of modularity for directed graphs reads


1 m ij

Qd =

kioutkjin m

Aij −

δ(Ci,Cj), (37)

where the factor 2 in the denominator of the second summand has been dropped because the sum of the indegrees

- FIG. 14 Problem of the directed modularity introduced by Arenas et al. (Arenas et al., 2007). The two situations illustrated are equivalent for modularity, as vertices A and A , as well as B and B , have identical indegrees and outdegrees. In this way, the optimization of directed modularity is not able to distinguish a situation in which there is directed ﬂow (top) or not (bottom). Reprinted ﬁgure with permission from Ref. (Kim et al., 2009).


(outdegrees) equals m, whereas the sum of the degrees of the vertices of an undirected graph equals 2m; the factor 2 in the denominator of the prefactor has been dropped because the number of non-vanishing elements of the adjacency matrix is m, not 2m as in the symmetric case of an undirected graph. If a graph is both directed and weighted, formulas 35 and 37 can be combined as

1 W ij

Qgen =

souti sinj W

Wij −

δ(Ci,Cj), (38)

which is the most general (available) expression of modularity (Arenas et al., 2007). Kim et al. (Kim et al., 2009) have remarked that the directed modularity of Eq. 37 may not properly account for the directedness of the edges (Fig. 14), and proposed a diﬀerent deﬁnition based on diﬀusion on directed graphs, inspired by Google’s PageRank algorithm (Brin and Page, 1998). Rosvall and Bergstrom raised similar objections (Rosvall and Bergstrom, 2008).

If vertices may belong to more clusters, it is not obvious how to ﬁnd a proper generalization of modularity. In fact, there is no unique recipe. Shen et al. (Shen et al., 2009), for instance, suggested the simple deﬁnition

- 1

- 2m ij


Q =

1 OiOj

kikj 2m

Aij −

δ(Ci,Cj). (39)

Here Oi is the number of communities including vertex i. The contribution of each edge to modularity is then the

smaller, the larger the number of communities including its endvertices. Nicosia et al. (Nicosia et al., 2009) have made some more general considerations on the problem of extending modularity to the case of overlapping communities. They considered the case of directed unweighted networks, starting from the following general expression

nc

1 m

Qov =

c=1 i,j

kioutkjin m

rijcAij − sijc

, (40)

where kiin and kjout are the indegree and outdegree of vertices i and j, the index c labels the communities and rijc, sijc express the contributions to the sum corresponding to the edge ij in the network and in the null model, due to the multiple memberships of i and j. If there is no overlap between the communities, rijc = sijc = δc

icjc, where ci and cj correspond to the communities of i and j. In this case, the edge ij contributes to the sum only if ci = cj, as in the original deﬁnition of modularity. For overlapping communities, the coeﬃcients rijc, sijc must depend on the membership coeﬃcients αi,c, αj,c of vertices i and j. One can assume that rijc = F(αi,c,αj,c), where F is some function. The term sijc is related to the null model of modularity, and it must be handled with care. In modularity’s original null model edges are formed by joining two random stubs, so one needs to deﬁne the membership of a random stub in the various communities. If we assume that there is no correlation a priori between the membership coeﬃcients of any two vertices, we can assign to a stub originating from a vertex i in community c the average membership corresponding to all edges which can be formed with i. On a directed graph we have to distinguish between outgoing and incoming stubs, so one has

βiout→,c = j F(αi,c,αj,c)

, (41)

n

βiin←,c = j F(αj,c,αi,c)

, (42)

n

and one can write the following general expression for modularity

nc

1 m

Qov =

c=1 i,j

βiout→,ckioutβjin←,ckjin m

rijcAij −

. (43)

The question now concerns the choice of the function F(αi,c,αj,c). If the formula of Eq. 43 is to be an extension of modularity to the case of overlapping communities, it has to satisfy some general properties of classical modularity. For instance, the modularity value of a cover consisting of the whole network as a single cluster should be zero. It turns out that a large class of functions yield an expression for modularity that fulﬁlls this requirement. Otherwise, the choice of F is rather arbitrary and good choices can be only tested a posteriori,

based on the results of the optimization. Membership coeﬃcients are also present in an extension of modularity to overlapping communities proposed by Shen et al. (Shen

- et al., 2009). Here the membership coeﬃcient of vertex v in community c is a sum over the edges of v belonging to c, where each edge has a weight proportional to the number of maximal cliques of c containing the edge.


Gaertler et al. have introduced quality measures based on modularity’s principle of the comparison between a variable relative to the original graph and the corresponding variable of a null model (Gaertler et al., 2007). They remark that modularity is just the diﬀerence between the coverage of a partition and the expected coverage of the partition in the null model. We remind that the coverage of a partition is the ratio between the number of edges within clusters and the total number of edges

- (Section III.C.2). Based on this observation, Gaertler et al. suggest that the comparison between the two terms can be done with other binary operations as well. For instance, one could consider the ratio


nc c=1 lc/m

Scov÷ =

, (44)

nc c=1(dc/2m)2

where the notation is the same as in Eq. 15. This can be done as well for any variable other than coverage. By using performance, for instance, (Section III.C.2) one obtains two new quality functions Sperf− and Sperf÷ , corresponding to taking the diﬀerence or the ratio between performance and its null model expectation value, respectively. Gaertler et al. compared the results obtained with the four functions Scov− = Q, Scov÷ , Sperf− and Sperf÷ , on a class of benchmark graphs with built-in cluster structure (Section XV.A) and social networks. They found that the “absolute” variants Scov− and Sperf− are better than the “relative” variants Scov÷ and Sperf÷ on the artiﬁcial benchmarks, whereas Sperf÷ is better on social networks12. Furthermore Sperf− is better than the standard modularity Scov− .

Modiﬁcations of modularity’s null model have been introduced by Massen and Doye (Massen and Doye, 2005) and Muﬀ et al. (Muﬀ et al., 2005). Massen and Doye’s null model is still a graph with the same expected degree sequence as the original, and with edges rewired at random among the vertices, but one imposes the additional constraint that there can be neither multiple edges between a pair of vertices nor edges joining a vertex with itself (loops or self-edges). This null model is more realistic, as multiple edges and loops are usually absent in real graphs. The maximization of the corresponding modiﬁed modularity yields partitions with smaller average cluster size than standard modularity. The latter tends to disfavor small communities, because the actual densities of

- 12 The comparison was done by computing the values of signiﬁcance indices like coverage and performance on the ﬁnal partitions.


edges inside small communities hardly exceed the null model densities, which are appreciably enhanced by the contributions from multiple connections and loops. Muﬀ et al. proposed a local version of modularity, in which the expected number of edges within a module is not calculated with respect to the full graph, but considering just a portion of it, namely the subgraph including the module and its neighbouring modules. Their motivation is the fact that modularity’s null model implicitly assumes that each vertex could be attached to any other, whereas in real cases a cluster is usually connected to few other clusters. On a directed graph, their localized modularity LQ reads

nc

LQ =

c=1

dinc doutc L2c

lc Lc

−

n

n

. (45)

In Eq. 45 lc is the number of edges inside cluster c, dinc (doutc ) the total internal (external) degree of cluster c and Lc

the total number of edges in the subgraph comprising cluster c and its neighbor clusters. The localized modularity is not bounded by 1, but can take any value. Its maximization delivers more accurate partitions than standard modularity optimization on a model network describing the social interactions between children in a school (school network) and on the metabolic and protein-protein interaction networks of E. coli.

n

Reichardt and Bornholdt have shown that it is possible to reformulate the problem of community detection as the problem of ﬁnding the ground state of a spin glass model (Reichardt and Bornholdt, 2006a). Each vertex i is labeled by a Potts spin variable σi, which indicates the cluster including the vertex. The basic principle of the model is that edges should connect vertices of the same class (i. e. same spin state), whereas vertices of diﬀerent classes (i. e. diﬀerent spin states) should be disconnected (ideally). So, one has to energetically favor edges between vertices in the same class, as well as non-edges between vertices in diﬀerent classes, and penalize edges between vertices of diﬀerent classes, along with non-edges between vertices in the same class. The resulting Hamiltonian of the spin model is

H({σ}) = −

Jijδ(σi,σj) = −

J(Aij−γpij)δ(σi,σj),

i<j

i<j

(46) where J is a constant expressing the coupling strength, Aij are the elements of the adjacency matrix of the graph, γ > 0 a parameter expressing the relative contribution to the energy from existing and missing edges, and pij is the expected number of links connecting i and j for a null model graph with the same total number of edges m of the graph considered. The system is a spin glass (Mezard et al., 1987), as the couplings Jij between spins are both ferromagnetic (on the edges of the graph, provided γpij < 1) and antiferromagnetic (between disconnected vertices, as Aij = 0 and Jij = −Jγpij < 0). The multiplicative costant J is irrelevant for practical

purposes, so in the following we set J = 1. The range of the spin-spin interaction is inﬁnite, as there is a non-zero coupling between any pair of spins. Eq. 46 bears a strong resemblance with the expression of modularity of Eq. 14. In fact, if γ = 1 and pij = kikj/2m we recover exactly modularity, up to a factor −1/m. In this case, ﬁnding the spin conﬁguration for which the Hamiltonian is minimal is equivalent to maximizing modularity. Eq. 46 is much more general than modularity, though, as both the null model and the parameter γ can be arbitrarily chosen. In particular, the value of γ determines the importance of the null model term pij in the quality function. Eq. 46 can be rewritten as

H({σ}) = −

s

###### =

s<r

###### ls − γ(ls)p

ij

###### lrs − γ(lrs)p

ij

###### = −

css

s=1

###### =

ars. (47)

s<r

Here, the sums run over the clusters: ls and lrs indicate the number of edges within cluster s and between clusters r and s, respectively; (ls)p

###### and (lrs)p

are the corresponding null model expectation values. Eq. 47 deﬁnes the coeﬃcients css of cohesion and ars of adhesion. If a subset of a cluster s has a larger coeﬃcient of adhesion with another cluster r than with its complement in

ij

ij

- s, the energy can be reduced by merging the subset with cluster r. In the particular case in which the coeﬃcient of adhesion of a subset G of a cluster s with its complement in the cluster exactly matches the coeﬃcient of adhesion of G with another cluster r, the partitions in which G stays within s or is merged with r have the same energy. In this case one can say that clusters r and s are overlapping. In general, the partition with minimum energy has the following properties: 1) every subset of each cluster has a coeﬃcient of adhesion with its complement in the cluster not smaller than with any other cluster;


- 2) every cluster has non-negative coeﬃcient of cohesion;
- 3) the coeﬃcient of adhesion between any two clusters is non-positive.


By tuning the parameter γ one can vary the number of clusters in the partition with minimum energy, going from a single cluster comprising all vertices (γ = 0), to n clusters with a single vertex (γ → ∞). So, γ is a resolution parameter that allows to explore the cluster structure of a graph at diﬀerent scales (see Section VI.C). The authors used single spin heatbath simulated annealing algorithms to ﬁnd the ground state of the Hamiltonian of Eq. 46.

Another generalization of modularity was recently suggested by Arenas et al. (Arenas et al., 2008a). They remarked that the fundamental unit to deﬁne modularity is the edge, but that high edge densities inside clusters usually imply the existence of long-range topological correlations between vertices, which are revealed by the presence of motifs (Milo et al., 2002), i. e. connected undirected subgraphs, like cycles (Section A.1). For instance, a high edge density inside a cluster usually means that there are also several triangles in the cluster, and compara-

tively few between clusters, a criterion that has inspired on its own popular graph clustering algorithms (Palla et al., 2005; Radicchi et al., 2004). Modularity can then be simply generalized by comparing the density of motifs inside clusters with the expected density in modularity’s null model (motif modularity). As a particular case, the triangle modularity of a partition C reads

Aij(C)Ajk(C)Aki(C)

nij(C)njk(C)nki(C)

Q (C) = ijk

− ijk

AijAjkAki

nijnjknki

ijk

ijk

(48) where Aij(C) = Aijδ(Ci,Cj) (Ci is the label of the cluster i belongs to), nij = kikj (ki is the degree of vertex i) and nij(C) = nijδ(Ci,Cj). If one chooses as motifs paths with even length, and removes the constraint that all vertices of the motif/path should stay inside the same cluster, maximizing motif modularity could reveal the existence of multipartite structure. For example, if a graph is bipartite, one expects to see many 2-paths starting from one vertex class and returning to it from the other class. Motif modularity can be trivially extended to the case of weighted graphs.

Several graphs representing real systems are built out of correlation data between elements. Correlation matrices are very common in the study of complex systems: well-known examples are the correlations of price returns, which are intensively studied by economists and econophysicists (Mantegna and Stanley, 2000). Correlations may be positive as well as negative, so the corresponding weighted edges indicate both attraction and repulsion between pairs of vertices. Usually the correlation values are ﬁltered or otherwise transformed such to eliminate the weakest correlations and anticorrelations and to maintain strictly positive weights for the edges, yielding graphs that can be treated with standard techniques. However, ignoring negative correlations means to give up useful information on the relationships between vertices. Finding clusters in a graph with both positive and negative weights is called correlation clustering problem (Bansal et al., 2004). According to intuition, one expects that vertices of the same cluster are linked by positive edges, whereas vertices of diﬀerent clusters are linked by negative edges. The best cluster structure is the partition that maximizes the sum of the strengths (in absolute value) of positive edges within clusters and negative edges between clusters, or, equivalently, the partition that minimizes the sum of the strengths (in absolute value) of positive edges between clusters and negative edges within clusters. This can be formulated by means of modularity, if one accounts for the contribution of the negative edges. A natural way to proceed is to create two copies of the graph at study: in one copy only the weights of the positive edges are kept, in the other only the weights of the negative edges (in absolute value). By applying Eq. 35 to the same partition of both graphs, one derives the contributions Q+ and

Q− to the modularity of that partition for the original graph. G´mez et al. deﬁne the global modularity as a linear combination of Q+ and Q−, that accounts for the relative total strengths of positive and negative edge weights (Go´mez et al., 2009). Kaplan and Forrest (Kaplan and Forrest, 2008) have proposed a similar expression, with two important diﬀerences. First, they have used the total strength of the graph, i. e. the sum of the absolute values of all weights, to normalize Q+ and Q−; G´mez et al. instead have used the positive and the negative strengths, for Q+ and Q−, respectively, which seems to be the more natural choice looking at Eq. 35. Second, Kaplan and Forrest have given equal weight to the contributions of Q+ and Q− to their ﬁnal expression of modularity, which is just the diﬀerence Q+ − Q−. In another work, Traag and Bruggeman (Traag and Bruggeman, 2009) have introduced negative links in the general spin glass formulation of modularity of Reichardt and Bornholdt (Reichardt and Bornholdt, 2006a). Here the relative importance of the contribution of positive and negative edge weights is a free parameter, the tuning of which allows to detect communities of various sizes and densities of positive/negative edges.

Some authors have pointed out that the original expression of modularity is not ideal to detect communities in bipartite graphs, which describe several real systems, like food webs (Williams and Martinez, 2000), scientiﬁc (Newman, 2001) and artistic (Gleiser and Danon, 2003) collaboration networks, etc.. Expressions of modularity for bipartite graphs were suggested by Guimer` et al. (Guimer` et al., 2007) and Barber (Barber, 2007; Barber et al., 2008). Guimer` et al. call the two classes of vertices actors and teams, and indicate with ti the degree of actor i and ma the degree of team a. The null model graphs are random graphs with the same expected degrees for the vertices, as usual. The bipartite modularity MB(P) for a partition P (of the actors) has the following expression

nc

i=j∈c cij a ma(ma − 1) − i=j∈c

titj ( a ma)2

MB(P) =

. (49)

c=1

Here, cij is the number of teams in which actors i and

- j are together and the sum a ma(ma − 1) gives the number of ordered pairs of actors in the same team. The second ratio of each summand is the null model term, indicating the expected (normalized) number of teams for pairs of actors in cluster c. The bipartite modularity can also be applied to (unipartite) directed graphs: each vertex can be duplicated and assigned to both classes, based on its twofold role of source and target for the edges.


Another interesting alternative was introduced by Barber (Barber, 2007; Barber et al., 2008) and is a simple extension of Eq. 14. Let us suppose that the two vertex classes (red and blue) are made out of p and q vertices, respectively. The degree of a red vertex i is indicated with ki, that of a blue vertex j with dj. The adjacency matrix A of the graph is in block oﬀ-diagonal form, as there

are edges only between red and blue vertices. Because of that, Barber assumes that the null model matrix P, whose element Pij indicates as usual the expected number of edges between vertices i and j in the null model, also has the block oﬀ-diagonal form

Op×p P˜p×q P˜Tq×p Oq×q

P =

, (50)

where the O are square matrices with all zero elements and P˜ij = kidj/m, as in the null model of standard modularity (though other choices are possible). The modularity maximum can be computed through the modularity matrix B = A − P, as we have seen in Section VI.A.4. However, spectral optimization of modularity gives excellent results for bipartitions, while its performance worsens when the number of clusters is unknown, as it is usually the case. Barber has proposed a diﬀerent optimization technique, called Bipartite Recursively Induced Modules (BRIM), based on the bipartite nature of the graph. The algorithm is based on the special expression of modularity for the bipartite case, for which once the partition of the red or the blue vertices is known, it is easy to get the partition of the other vertex class that yields the maximum modularity. Therefore, one starts from an arbitrary partition in c clusters of, say, the blue vertices, and recovers the partition of the red vertices, which is in turn used as input to get a better partition of the blue vertices, and so on until modularity converges. BRIM does not predict the number of clusters c of the graph, but one can obtain good estimates for it by exploring diﬀerent values with a simple bisection approach. Typically, for a given c the algorithm needs a few steps to converge, each step having a complexity O(m). An expression of the number of convergence steps in terms of n and/or m still needs to be derived.

C. Limits of modularity

In this Section we shall discuss some features of modularity, which are crucial to identify the domain of its applicability and ultimately to assess the issue of the reliability of the measure for the problem of graph clustering.

An important question concerns the value of the maximum modularity Qmax for a graph. We know that it must be non-negative, as there is always at least a partition with zero modularity, consisting in a single cluster with all vertices (Section III.C.2). However, a large value for the modularity maximum does not necessarily mean that a graph has community structure. Random graphs are supposed to have no community structure, as the linking probability between vertices is either constant or a function of the vertex degrees, so there is no bias a priori towards special groups of vertices. Still, random graphs may have partitions with large modularity values (Guimer` et al., 2004; Reichardt and Bornholdt, 2006a). This is due to ﬂuctuations in the distribution of

edges in the graph, which in many graph realizations is not homogeneous even if the linking probability is constant, like in Erd¨s-R´enyi graphs. The ﬂuctuations determine concentrations of links in some subsets of the graph, which then appear like communities. According to the deﬁnition of modularity, a graph has community structure with respect to a random graph with equal size and expected degree sequence. Therefore, the modularity maximum of a graph reveals a signiﬁcant community structure only if it is appreciably larger than the modularity maximum of random graphs of the same size and expected degree sequence. The signiﬁcance of the modularity maximum Qmax for a graph can be estimated by calculating the maximum modularity for many realizations of the null model, obtained from the original graph by randomly rewiring its edges. One then computes the average Q NM and the standard deviation σQNM of the results. The statistical signiﬁcance of Qmax is indicated by the distance of Qmax from the null model average

Q NM in units of the standard deviation σQNM, i. e. by the z-score

Qmax −  Q NM σQNM

z =

. (51)

If z 1, Qmax indicates strong community structure. Cutoﬀ values of 2 − 3 for the z-scores are customary. This approach has problems, though. It can generate both false positives and false negatives: a few graphs that most people would consider without a signiﬁcant community structure have a large z-score; on the other hand, some graphs that are agreed to display cluster structure have very low values for the z-score. Besides, the distribution of the maximum modularity values of the null model, though peaked, is not Gaussian. Therefore, one cannot attribute to the values of the z-score the signiﬁcance corresponding to a Gaussian distribution, and one would need instead to compute the statistical signiﬁcance for the right distribution.

Reichardt and Bornholdt have studied the issue of the modularity values for random graphs in some depth (Reichardt and Bornholdt, 2006b, 2007), using their general spin glass formulation of the clustering problem (Sec-

- tion VI.B). They considered the general case of a random graph with arbitrary degree distribution P(k) and without degree-degree correlations. They set γ = 1, so that the energy of the ground state coincides with modularity (up to a constant factor). For modularity’s null model graphs, the modularity maximum corresponds to an equipartition of the graph, i. e. the magnetization of the ground state of the spin glass is zero, a result conﬁrmed by numerical simulations (Reichardt and Bornholdt, 2006b, 2007). This is because the distribution of the couplings has zero mean, and the mean is only coupled to magnetization (Fu and Anderson, 1986). For a partition of any graph with n vertices and m edges in q clusters with equal numbers of vertices, there is a simple linear relation between the cut size Cq of the partition and its modularity Qq: Cq = m[(q − 1)/q − Qq]. We


remind that the cut size Cq is the total number of intercluster edges of the partition (Section IV.A). In this way, the partition with maximum modularity is also the one with minimum cut size, and community detection becomes equivalent to graph partitioning. Reichardt and Bornholdt derived analytically the ground state energy for Ising spins (q = 2), which corresponds to the following expression of the expected maximum modularity Qmax2 for a bipartition (Reichardt and Bornholdt, 2007)

k1/2 k

Qmax2 = U0J

. (52)

Here kα = P(k)kαdk and U0 is the ground state energy of the Sherrington-Kirkpatrick model (Sherrington and Kirkpatrick, 1975). The most interesting feature of Eq. 52 is the simple scaling with k1/2 / k . Numerical calculations show that this scaling holds for both Erd¨sR´enyi and scale-free graphs (Section A.3). Interestingly, the result is valid for partitions in q clusters, where q is left free, not only for q = 2. The number of clusters of the partition with maximum modularity decreases if the average degree k increases, and tends to 5 for large values of k , regardless of the degree distribution and the size of the graph. From Eq. 52 we also see that the expected maximum modularity for a random graph increases when

k decreases, i. e. if the graph gets sparser. So it is particularly hard to detect communities in sparse graphs by using modularity optimization. As we shall see in Section XIV, the sparsity of a graph is generally a serious obstacle for graph clustering methods, no matter if one uses modularity or not.

A more fundamental issue, raised by Fortunato and Barth´elemy (Fortunato and Barth´elemy, 2007), concerns the capability of modularity to detect “good” partitions. If a graph has a clear cluster structure, one expects that the maximum modularity of the graph reveals it. The null model of modularity assumes that any vertex i “sees” any other vertex j, and the expected number of edges between them is pij = kikj/2m. Similarly, the expected number of edges between two clusters A and B with total degrees KA and KB, respectively, is PAB = KAKB/2m. The variation of modularity determined by the merger of A and B with respect to the partition in which they are separate clusters is ∆QAB = lAB/m − KAKB/2m2, with lAB number of edges connecting A to B. If lAB = 1, i. e. there is a single edge joining A to B, we expect that the two subgraphs will often be kept separated. Instead, if KAKB/2m < 1, ∆QAB > 0. Let us suppose for simplicity that KA ∼ KB = K, i. e. that the two subgraphs are of about the same size, measured in terms of edges. We conclude that, if K <∼

√2m and the two subgraphs A and B are connected, modularity is greater if they are in the same cluster (Fortunato and Barth´elemy, 2007). The reason is intuitive: if there are more edges than expected between A and B, there is a strong topological correlation between the subgraphs. If the subgraphs are suﬃciently small (in degree), the expected number of edges for the null model can be smaller than one, so

![image 17](Community Detection in Graphs_images/imageFile17.png)

![image 18](Community Detection in Graphs_images/imageFile18.png)

![image 19](Community Detection in Graphs_images/imageFile19.png)

![image 20](Community Detection in Graphs_images/imageFile20.png)

Kl

Kl

![image 21](Community Detection in Graphs_images/imageFile21.png)

Kl

![image 22](Community Detection in Graphs_images/imageFile22.png)

Kl

![image 23](Community Detection in Graphs_images/imageFile23.png)

![image 24](Community Detection in Graphs_images/imageFile24.png)

Kl

![image 25](Community Detection in Graphs_images/imageFile25.png)

![image 26](Community Detection in Graphs_images/imageFile26.png)

![image 27](Community Detection in Graphs_images/imageFile27.png)

Kl

![image 28](Community Detection in Graphs_images/imageFile28.png)

Kl

![image 29](Community Detection in Graphs_images/imageFile29.png)

![image 30](Community Detection in Graphs_images/imageFile30.png)

![image 31](Community Detection in Graphs_images/imageFile31.png)

Kl

Kl Kl

![image 32](Community Detection in Graphs_images/imageFile32.png)

- FIG. 15 Resolution limit of modularity optimization. The natural community structure of the graph, represented by the individual cliques (circles), is not recognized by optimizing modularity, if the cliques are smaller than a scale depending on the size of the graph. In this case, the maximum modularity corresponds to a partition whose clusters include two or more cliques (like the groups indicated by the dashed contours). Reprinted ﬁgure with permission from Ref. (Fortunato and Barth´elemy, 2007). c 2007 from the National Academy of Science of the USA.


even the weakest possible connection (a single edge) sufﬁces to keep the subgraphs together. Interestingly, this result holds independently of the structure of the subgraphs. In particular it remains true if the subgraphs are cliques, which are the subgraphs with the largest possible density of internal edges, and represent the strongest possible communities. In Fig. 15 a graph is made out of nc identical cliques, with l vertices each, connected by single edges. It is intuitive to think that the clusters of the best partition are the individual cliques: instead, if nc is larger than about l2, modularity would be higher for partitions in which the clusters are groups of cliques (like the clique pairs indicated by the dashed lines in the ﬁgure).

The conclusion is striking: modularity optimization has a resolution limit that may prevent it from detecting clusters which are comparatively small with respect to the graph as a whole, even when they are well deﬁned communities like cliques. So, if the partition with maximum modularity includes clusters with total degree of the order of √m or smaller, one cannot know a priori whether the clusters are single communities or combinations of smaller weakly interconnected communities. This resolution problem has a large impact in practical applications.

Real graphs with community structure usually contain communities which are very diverse in size (Clauset et al., 2004; Danon et al., 2005; Guimer` et al., 2003; Palla et al., 2005), so many (small) communities may remain undetected. Besides, modularity is extremely sensitive to even individual connections. Many real graphs, in biology and in the social sciences, are reconstructed through experiments and surveys, so edges may occasionally be false positives: if two small subgraphs happen to be connected by a few false edges, modularity will put them in the same cluster, inferring a relationship between entities that in reality may have nothing to do with each other.

The resolution limit comes from the very deﬁnition of modularity, in particular from its null model. The weak point of the null model is the implicit assumption that each vertex can interact with every other vertex, which implies that each part of the graph knows about everything else. This is however questionable, and certainly wrong for large systems like, e.g., the Web graph. It is certainly more reasonable to assume that each vertex has a limited horizon within the graph, and interacts just with a portion of it. However, nobody knows yet how to deﬁne such local territories for the graph vertices. The null model of the localized modularity of Muﬀ et al. (Section VI.B) is a possibility, since it limits the horizon of a vertex to a local neighborhood, comprising the cluster of the vertex and the clusters linked to it by at least one edge (neighboring clusters). However, there are many other possible choices. In this respect, the null model of Girvan and Newman, though unrealistic, is the simplest one can think of, which partly explains its success. Quality functions that, like modularity, are based on a null model such that the horizon of vertices is of the order of the size of the whole graph, are likely to be aﬀected by a resolution limit (Fortunato, 2007). The problem is more general, though. For instance, Li et al. (Li et al., 2008b) have introduced a quality function, called modularity density, which consists in the sum over the clusters of the ratio between the diﬀerence of the internal and external degrees of the cluster and the cluster size. The modularity density does not require a null model, and delivers better results than modularity optimization (e. g. it correctly recovers the natural partition of the graph in Fig. 15 for any number/size of the cliques). However, it is still aﬀected by a resolution limit. To avoid that, Li et al. proposed a more general deﬁnition of their measure, including a tunable parameter that allows to explore the graph at diﬀerent resolutions, in the spirit of the methods of Section XII.

A way to go around the resolution limit problem could be to perform further subdivisions of the clusters obtained from modularity optimization, in order to eliminate possible artiﬁcial mergers of communities. For instance, one could recursively optimize modularity for each single cluster, taking the cluster as a separate entity (Fortunato and Barth´elemy, 2007; Ruan and Zhang, 2008). However, this is not a reliable procedure, for two reasons: 1) the local modularities used to ﬁnd partitions

within the clusters have diﬀerent null models, as they depend on the cluster sizes, so they are inconsistent with each other; 2) one needs to deﬁne a criterion to decide when one has to stop partitioning a cluster, but there is no obvious prescription, so any choice is necessarily based on arbitrary assumptions13.

Resolution limits arise as well in the more general formulation of community detection by Reichardt and Bornholt (Kumpula et al., 2007b). Here the limit scale for the undetectable clusters is √γm. We remind that γ weighs the contribution of the null model term in the quality function. For γ = 1 one recovers the resolution limit of modularity. By tuning the parameter γ it is possible to arbitrarily vary the resolution scale of the corresponding quality function. This in principle solves the problem of the resolution limit, as one could adjust the resolution of the method to the actual scale of the communities to detect. The problem is that usually one has no information about the community sizes, so it is not possible to decide a priori the proper value(s) of γ for a speciﬁc graph. In the most recent literature on graph clustering quite a few multiresolution methods have been introduced, addressing this problem in several ways. We will discuss them in some detail in Section XII.

The resolution limit can be easily extended to the case of weighted graphs. In a recent paper (Berry et al., 2009), Berry et al. have considered the special case in which intracluster edges have weight 1, whereas intercluster edges have weight . By repeating the same procedure as in Ref. (Fortunato and Barthe´lemy, 2007), they conclude that clusters with internal strength (i. e. sum of all weights of internal edges) ws may remain undetected if ws < W /2− , where W is the total strength of the graph. So, the resolution limit decreases when

decreases. Berry et al. use this result to show that, by properly weighting the edges of a given unweighted graph, it becomes possible to detect clusters with very high resolution by still using modularity optimization.

Very recently, Good et al. (Good et al., 2009) have made a careful analysis of modularity and its performance. They discovered that the modularity landscape is characterized by an exponential number of distinct states/partitions, whose modularity values are very close to the global maximum (Fig. 16). This problem is particularly dramatic if a graph has a hierarchical community structure, like most real networks. Such enormous num-

- 13 Ruan and Zhang (Ruan and Zhang, 2008) propose a stopping criterion based on the statistical signiﬁcance of the maximum modularity values of the subgraph. The maximum modularity of a subgraph is compared with the expected maximum modularity for a random graph with the same size and expected degree sequence of the subgraph. If the corresponding z-score is suﬃciently high, the subgraph is supposed to have community structure and one accepts the partition in smaller pieces. The procedure stops when none of the subgraphs of the running partitions has signiﬁcant community structure, based on modularity.


![image 33](Community Detection in Graphs_images/imageFile33.png)

FIG. 16 Low-dimensional visualization of the modularity landscape for the metabolic network of the spirochete Treponema pallidum. The big degeneracy of suboptimal highmodularity partitions is revealed by the plateau (whose shape is detailed in the inset), which is large and very irregular. Modularity values in the plateau are very close to the absolute maximum, although they may correspond to quite diﬀerent partitions. Reprinted ﬁgure with permission from Ref. (Good et al., 2009).

ber of solutions explains why many heuristics are able to come very close to modularity’s global maximum, but it also implies that the global maximum is basically impossible to ﬁnd. In addition, high-modularity partitions are not necessarily similar to each other, despite the proximity of their modularity scores. The optimal partition from a topological point of view, which usually does not correspond to the modularity maximum due to the resolution limit, may however have a large modularity score. Therefore the optimal partition is basically indistinguishable from a huge number of high-modularity partitions, which are in general structurally dissimilar from it. The large structural inhomogeneity of the high-modularity partitions implies that one cannot rely on any of them, at least in principle, in the absence of additional information on the particular system at hand and its structure.

###### VII. SPECTRAL ALGORITHMS

In Sections IV.A and IV.D we have learned that spectral properties of graph matrices are frequently used to ﬁnd partitions. A paradigmatic example is spectral graph clustering, which makes use of the eigenvectors of Laplacian matrices (Section IV.D). We have also seen that Newman-Girvan modularity can be optimized by using the eigenvectors of the modularity matrix (Section VI.A.4). Most spectral methods have been introduced and developed in computer science and generally focus on data clustering, although applications to graphs

are often possible as well. In this section we shall review recent spectral techniques proposed mostly by physicists explicitly for graph clustering.

Early works have shown that the eigenvectors of the transfer matrix T (Section A.2) can be used to extract useful information on community structure. The transfer matrix acts as a time propagator for the process of random walk on a graph. Given the eigenvector cα of the transposed transfer matrix T†, corresponding to the eigenvalue λα, cαi is the outgoing current ﬂowing from vertex i, corresponding to the eigenmode α. The participation ratio (PR)

χα =

n

(cαi )4

i=1

−1

(53)

indicates the eﬀective number of vertices contributing to eigenvector cα. If χα receives contributions only from vertices of the same cluster, i. e. eigenvector cα is “localized”, the value of χα indicates the size of that cluster (Eriksen et al., 2003; Simonsen et al., 2004). The signiﬁcance of the cluster can be assessed by comparing χα with the corresponding participation ratio for a random graph with the same expected degree sequence as the original graph. Eigenvectors of the adjacency matrix may be localized as well if the graph has a clear community structure (Slanina and Zhang, 2005). A recent comprehensive analysis of spectral properties of modular graphs has been carried out by Mitrovi´c and Tadic´ (Mitrovic´ and Tadi´c, 2009).

Donetti and Mun˜oz have devised an elegant method based on the eigenvectors of the Laplacian matrix (Donetti and Mun˜oz, 2004). The idea is the same

- as in spectral graph clustering (Section IV.D): since the values of the eigenvector components are close for vertices in the same community, one can use them as coordinates, such that vertices turn into points in a metric space. So, if one uses M eigenvectors, one can embed the vertices in an M-dimensional space. Communities appear as groups of points well separated from each other, as illustrated in Fig. 17. The separation is the more visible, the larger the number of dimensions/eigenvectors M. The originality of the method consists in the procedure to group the points and to extract the partition. Donetti and Mun˜oz used hierarchical clustering (see Section IV.B), with the constraint that only pairs of clusters which have at least one interconnecting edge in the original graph are merged. Among all partitions of the resulting dendrogram, the one with largest modularity is chosen. For the similarity measure between vertices, Donetti and Mun˜oz used both the Euclidean distance and the angle distance. The angle distance between two points is the angle between the vectors going from the origin of the M-dimensional space to either point. Tests on the benchmark by Girvan and Newman (Section XV.A) show that the best results are obtained with complete-linkage clustering. The most computationally expensive part of the algorithm is the calculation of the Laplacian eigenvectors. Since a few


a

0.15

0.1

0.05

0

−0.05

−0.1

b

0.15

| | | |
|---|---|---|
| | | |


0.1

0.05

| | |
|---|---|
| | |
| | |
| | |


0

−0.05

−0.1

−0.1 −0.05 0 0.05 0.1 0.15

FIG. 17 Spectral algorithm by Donetti and Mu˜noz. Vertex i is represented by the values of the ith components of Laplacian eigenvectors. In this example, the graph has an ad-hoc division in four communities, indicated by the colours. The communities are better separated in two dimensions (b) than in one (a). Reprinted ﬁgure with permission from Ref. (Donetti and Mu˜noz, 2004). c 2004 by IOP Publishing and SISSA.

eigenvectors suﬃce to get good partitions, one can determine them with the Lanczos method (Lanczos, 1950). The number M of eigenvectors that are needed to have a clean separation of the clusters is not known a priori, but one can compute a number M0 > 1 of them and search for the highest modularity partition among those delivered by the method for all 1 ≤ M ≤ M0. In a related work, Simonsen has embedded graph vertices in space by using as coordinates the components of the eigenvectors of the right stochastic matrix (Simonsen, 2005).

Eigenvalues and eigenvectors of the Laplacian matrix have been used by Alves to compute the eﬀective conductances for pairs of vertices in a graph, assuming that the latter is an electric network with edges of unit resistance (Alves, 2007). The conductances enable one to compute the transition probabilities for a random walker moving on the graph, and from the transition probabilities one builds a similarity matrix between vertex pairs. Hierarchical clustering is applied to join vertices in groups. The method can be trivially extended to the case of weighted graphs. The algorithm by Alves is rather slow, as one needs to compute the whole spectrum of the Laplacian, which requires a time O(n3). Moreover, there is no criterion to select which partition(s) of the dendrogram is (are) the best.

Capocci et al. (Capocci et al., 2005) used eigenvector components of the right stochastic matrix R (Section A.2), that is derived from the adjacency matrix by dividing each row by the sum of its elements. The right stochastic matrix has similar properties as the Laplacian. If the graph has g connected components, the largest g

- 16
- 17


0

18

15

1 2

13 14

3

- 8
- 9 10


6 7

4

5

12 11

0.4

0.2

0

- xi


−0.2

−0.4

0 5 10 15 20 i

- FIG. 18 Basic principle of the spectral algorithm by Capocci et al. (Capocci et al., 2005). The bottom diagram shows the values of the components of the second eigenvector of the right stochastic matrix for the graph drawn on the top. The three plateaus of the eigenvector components correspond to the three evident communities of the graph. Reprinted ﬁgures with permission from Ref. (Capocci et al., 2005). c 2005 by Elsevier.


eigenvalues are equal to 1, with eigenvectors characterized by having equal-valued components for vertices belonging to the same component. In this way, by listing the vertices according to the connected components they belong to, the components of any eigenvector of R, corresponding to eigenvalue 1, display a step-wise proﬁle, with plateaus indicating vertices in the same connected component. For connected graphs with cluster structure, one can still see plateaus, if communities are only loosely connected to each other (Fig. 18). Here the communities can be immediately deducted by an inspection of the components of any eigenvector with eigenvalue 1. In practical cases, plateaus are not clearly visible, and one eigenvector is not enough. However, one expects that there should be a strong correlation between eigenvector components corresponding to vertices in the same cluster. Capocci et al. derived a similarity matrix, where the similarity between vertices i and j is the Pearson correlation coeﬃcient between their corresponding eigenvector

components, averaged over a small set of eigenvectors. The eigenvectors can be calculated by performing a constrained optimization of a suitable cost function. The method can be extended to weighted and directed graphs. It is useful to estimate vertex similarities, however it does not provide a well-deﬁned partition of the graph.

Yang and Liu (Yang and Liu, 2008) adopted a recursive bisectioning procedure. Communities are subgraphs such that the external degree of each vertex does not exceed the internal degree (strong communities or LS-sets, see Section III.B.2). In the ﬁrst step of the algorithm, the adjacency matrix of the graph is put in approximately block-diagonal form. This is done by computing a new centrality measure for the vertices, called clustering centrality. This measure is similar to Bonacich’s eigenvector centrality (Bonacich, 1972, 1987), which is given by the eigenvector of the adjacency matrix corresponding to the largest eigenvalue. The clustering centrality of a vertex basically measures the probability that a random walker starting at that vertex hits a given target. Such probability is larger if the origin and the target vertices belong to the same cluster than if they do not. If the graph has well-separated communities, the values of the clustering centrality would be similar for vertices in the same cluster. In this way, one can rearrange the original adjacency matrix by listing the vertices in non-decreasing order of their clustering centralities, and blocks would be visible. The blocks are then identiﬁed by iterative bisection: each cluster found at some step is split in two as long as the resulting parts are still communities in the strong sense, otherwise the procedure stops. The worst-case complexity of the method is O[Kt(nlog n + m)], where K is the number of clusters of the ﬁnal partition and t the (average) number of iterations required to compute the clustering centrality with the power method (Golub and Loan, 1989). Since t is fairly independent of the graph size, the method scales quite well on sparse graphs [O(nlog n)]. The main limit of this technique is the assumption that communities are deﬁned in the strong sense, which is too restrictive. On the other hand, one could think of using alternative deﬁnitions.

###### VIII. DYNAMIC ALGORITHMS

This Section describes methods employing processes running on the graph, focusing on spin-spin interactions, random walks and synchronization.

A. Spin models

The Potts model is among the most popular models in statistical mechanics (Wu, 1982). It describes a system of spins that can be in q diﬀerent states. The interaction is ferromagnetic, i. e. it favours spin alignment, so at zero temperature all spins are in the same state. If antiferromagnetic interactions are also present, the ground

state of the system may not be the one where all spins are aligned, but a state where diﬀerent spin values coexist, in homogeneous clusters. If Potts spin variables are assigned to the vertices of a graph with community structure, and the interactions are between neighbouring spins, it is likely that the structural clusters could be recovered from like-valued spin clusters of the system, as there are many more interactions inside communities than outside. Based on this idea, inspired by an earlier paper by Blatt et al. (Blatt et al., 1996), Reichardt and Bornholdt proposed a method to detect communities that maps the graph onto a zero-temperature q-Potts model with nearest-neighbour interactions (Reichardt and Bornholdt, 2004). The Hamiltonian of the model, i. e. its energy, reads

H = −J

q

Aijδ(σi,σj) + γ

s=1

i,j

ns(ns − 1) 2

, (54)

where Aij is the element of the adjacency matrix, δ is Kronecker’s function, ns the number of spins in state s, J and γ are coupling parameters. The energy H is the sum of two competing terms: the ﬁrst is the classical ferromagnetic Potts model energy, and favors spin alignment; the second term instead peaks when the spins are homogeneously distributed. The ratio γ/J expresses the relative importance of the two terms: by tuning γ/J one can explore diﬀerent levels of modularity of the system, from the whole graph seen as a single cluster to clusters consisting of individual vertices. If γ/J is set to the value δ(G) of the average density of edges of the graph G, the energy of the system is smaller if spins align within subgraphs such that their internal edge density exceeds δ(G), whereas the external edge density is smaller than δ(G), i. e. if the subgraphs are clusters (Section III.B.1). The minimization of H is carried out via simulated annealing ((Kirkpatrick et al., 1983) and Section VI.A.2), starting from a conﬁguration where spins are randomly assigned to the vertices and the number of states q is very high. The procedure is quite fast and the results do not depend on q (provided q is suﬃciently high). The method also allows to identify vertices shared between communities, from the comparison of partitions corresponding to global and local energy minima. The Hamiltonian H can be rewritten as

H =

δ(σi,σj)(γ − Aij), (55)

i<j

which is the energy of an inﬁnite-range Potts spin glass,

- as all pairs of spins are interacting (neighboring or not) and there may be both positive and negative couplings. The method can be simply extended to the analysis of weighted graphs, by introducing spin couplings proportional to the edge weights, which amounts to replacing the adjacency matrix A with the weight matrix W in Eq. 54. Ispolatov et al. (Ispolatov et al., 2006) have adopted a similar Hamiltonian as in Eq. 54, with a tunable antiferromagnetic term interpolating between the


corresponding term of Eq. 54 and the entropy term (proportional to ns log ns) of the free energy, whose minimization is equivalent to ﬁnding the states of the ﬁnitetemperature Potts model used by Blatt et al. (Blatt et al., 1996). Eq. 55 is at the basis of the successive generalization of modularity with arbitrary null models proposed by Reichardt and Bornholdt, that we have discussed in Section VI.B.

In another work (S.-W. Son et al., 2006), Son et al. have presented a clustering technique based on the Ferromagnetic Random Field Ising Model (FRFIM). Given a weighted graph with weight matrix W, the Hamiltonian of the FRFIM on the graph is

- 1

- 2 i,j


H = −

Wijσiσj −

i

Biσi. (56)

In Eq. 56 σi = ±1 and Bi are the spin and the random magnetic ﬁeld of vertex i, respectively. The FRFIM has been studied to understand the nature of the spin glass phase transition (Middleton and Fisher, 2002) and the disorder-driven roughening transition of interfaces in disordered media (Noh and Rieger, 2001, 2002). The behavior of the model depends on the choice of the magnetic ﬁelds. Son et al. set to zero the magnetic ﬁelds of all vertices but two, say s and t, for which the ﬁeld has inﬁnite strength and opposite signs. This amounts to ﬁx the spins of s and t to opposite values, introducing frustration in the system. The idea is that, if s and t are central vertices of diﬀerent communities, they impose their spin state to the other community members. So, the state of minimum energy is a conﬁguration in which the graph is polarized into a subgraph with all positive spins and a subgraph with all negative spins, coinciding with the communities, if they are well deﬁned. Finding the minimum of H is equivalent to solving a maximumﬂow/minimum-cut problem, which can be done through well known techniques of combinatorial optimization, like the augmenting path algorithm (Ahuja et al., 1993). For a given choice of s and t, many ground states can be found. The vertices that end up in the same cluster in all ground states represent the cores of the clusters, which are called coteries. Possible vertices not belonging to the coteries indicate that the two clusters overlap. In the absence of information about the cluster structure of the graph, one needs to repeat the procedure for any pair of vertices s and t. Picking vertices of the same cluster, for instance, would not give meaningful partitions. Son et al. distinguish relevant clusters if they are of about the same size. The procedure can be iteratively applied to each of the detected clusters, considered as a separate graph, until all clusters have no community structure any more. On sparse graphs, the algorithm has complexity O(n2+θ), where θ ∼ 1.2, so it is very slow and can be currently used for graphs of up to few thousands vertices. If one happens to know which are the important vertices of the clusters, e.g. by computing appropriate centrality values (like degree or site betweenness (Freeman, 1977)), the choices for s and t are constrained and the complexity

can become as low as O(nθ), which enables the analysis of systems with millions of vertices. Tests on Barab´siAlbert graphs (Section A.3) show that the latter have no community structure, as expected.

- B. Random walk


Random walks (Hughes, 1995) can also be useful to ﬁnd communities. If a graph has a strong community structure, a random walker spends a long time inside a community due to the high density of internal edges and consequent number of paths that could be followed. Here we describe the most popular clustering algorithms based on random walks. All of them can be trivially extended to the case of weighted graphs.

Zhou used random walks to deﬁne a distance between pairs of vertices (Zhou, 2003a): the distance dij between i and j is the average number of edges that a random walker has to cross to reach j starting from i. Close vertices are likely to belong to the same community. Zhou deﬁnes a “global attractor” of a vertex i to be a closest vertex to i (i. e. any vertex lying at the smallest distance from i), whereas the “local attractor” of i is its closest neighbour. Two types of communities are deﬁned, according to local or global attractors: a vertex

- i has to be put in the same community of its attractor and of all other vertices for which i is an attractor. Communities must be minimal subgraphs, i. e. they cannot include smaller subgraphs which are communities according to the chosen criterion. Applications to real networks, like Zachary’s karate club (Zachary, 1977) and the college football network compiled by Girvan and Newman (Girvan and Newman, 2002) (Section XV.A), along with artiﬁcial graphs like the benchmark by Girvan and Newman (Girvan and Newman, 2002) (Section XV.A), show that the method can ﬁnd meaningful partitions. The method can be reﬁned, in that vertex i is associated to its attractor j only with a probability


proportional to exp(−βdij), β being a sort of inverse temperature. The computation of the distance matrix requires solving n linear-algebra equations (as many

- as the vertices), which requires a time O(n3). On the other hand, an exact computation of the distance matrix is not necessary, as the attractors of a vertex can be identiﬁed by considering only a localized portion of the graph around the vertex; therefore the method can be applied to large graphs as well. In a successive paper (Zhou, 2003b), Zhou introduced a measure of dissimilarity between vertices based on the distance deﬁned above. The measure resembles the deﬁnition of distance based on structural equivalence of Eq. 7, where the elements of the adjacency matrix are replaced by the corresponding distances. Graph partitions are obtained with a divisive procedure that, starting from the graph as a single community, performs successive splits based on the criterion that vertices in the same cluster must be less dissimilar than a running threshold,


which is decreased during the process. The hierarchy of partitions derived by the method is representative of actual community structures for several real and artiﬁcial graphs, including Zachary’s karate club (Zachary, 1977), the college football network (Girvan and Newman, 2002) and the benchmark by Girvan and Newman (Girvan and Newman, 2002) (Section XV.A). The time complexity of the procedure is again O(n3). The code of the algorithm can be downloaded from http://www.mpikg-golm.mpg.de/theory/people/zhou /networkcommunity.html.

In another work (Zhou and Lipowsky, 2004), Zhou and Lipowsky adopted biased random walkers, where the bias is due to the fact that walkers move preferentially towards vertices sharing a large number of neighbours with the starting vertex. They deﬁned a proximity index, which indicates how close a pair of vertices is to all other vertices. Communities are detected with a procedure called NetWalk, which is an agglomerative hierarchical clustering method (Section IV.B), where the similarity between vertices is expressed by their proximity. The method has a time complexity O(n3): however, the proximity index of a pair of vertices can be computed with good approximation by considering just a small portion of the graph around the two vertices, with a considerable gain in time. The performance of the method is comparable with that of the algorithm of Girvan and Newman (Section V.A).

A diﬀerent distance measure between vertices based on random walks was introduced by Latapy and Pons (Latapy and Pons, 2005). The distance is calculated from the probabilities that the random walker moves from a vertex to another in a ﬁxed number of steps. The number of steps has to be large enough to explore a signiﬁcant portion of the graph, but not too long, as otherwise one would approach the stationary limit in which transition probabilities trivially depend on the vertex degrees. Vertices are then grouped into communities through an agglomerative hierarchical clustering technique based on Ward’s method (Ward, 1963). Modularity (Section III.C.2) is used to select the best partition of the resulting dendrogram. The algorithm runs to completion in a time O(n2d) on a sparse graph, where d is the depth of the dendrogram. Since d is often small for real graphs [O(log n)], the expected complexity in practical computations is O(n2 log n). The software of the algorithm can be found at http://www-rp.lip6.fr/∼latapy/PP/walktrap.html.

Hu et al. (Hu et al., 2008) designed a graph clustering technique based on a signaling process between vertices, somewhat resembling diﬀusion. Initially a vertex s is assigned one unit of signal, all the others have no signal. In the ﬁrst step, the source vertex s sends one unit of signal to each of its neighbors. Next, all vertices send as many units of signals they have to each of their neighbors. The process is continued until a given number of iterations T is reached. The intensity of the signal at vertex i, normalized by the total amount of signal, is the i-th entry of a vector us, representing the source vertex s. The proce-

dure is then repeated by choosing each vertex as source. In this way one can associate an n-dimensional vector to each vertex, which correspons to a point in an Euclidean space. The vector us is actually the s-th column of the matrix (I + A)T, where I and A are the identity and adjacency matrix, respectively. The idea is that the vector us describes the inﬂuence that vertex s exerts on the graph through signaling. Vertices of the same community are expected to have similar inﬂuence on the graph and thus to correspond to vectors which are “close” in space. The vectors are ﬁnally grouped via fuzzy k-means clustering (Section IV.C). The optimal number of clusters corresponds to the partition with the shortest average distance between vectors in the same community and the largest average distance between vectors of diﬀerent communities. The signaling process is similar to diﬀusion, but with the important diﬀerence that here there is no ﬂow conservation, as the amount of signal at each vertex is not distributed among its neighbors but transferred entirely to each neighbor (as if the vertex sent multiple copies of the same signal). The complexity of the algorithm is O[T( k +1)n2], where k is the average degree of the graph. Like in the previous algorithm by Latapy and Pons (Latapy and Pons, 2005), ﬁnding an optimal value for the number of iterations T is non-trivial.

Delvenne et al. (Delvenne et al., 2008) have shown that random walks enable one to introduce a general quality function, expressing the persistence of clusters in time. A cluster is persistent with respect to a random walk after

- t time steps if the probability that the walker escapes the cluster before t steps is low. Such probability is computed


via the clustered autocovariance matrix Rt, which, for a partition of the graph in c clusters, is deﬁned as

Rt = HT(ΠMt − πTπ)H. (57) Here, H is the n × c membership matrix, whose element Hij equals one if vertex i is in cluster j, zero otherwise; M is the transition matrix of the random walk; Π the diagonal matrix whose elements are the stationary probabilities of the random walk, i. e. Πii = ki/2m, ki being the degree of vertex i; π is the vector whose entries are the diagonal elements of Π. The element (Rt)ij expresses the probability for the walk to start in cluster i and end up in cluster j after t steps, minus the stationary probability that two independent random walkers are in i and

- j. In this way, the persistence of a cluster i is related to


the diagonal element (Rt)ii. Delvenne et al. deﬁned the stability of the clustering

r(t;H) = min

0≤s≤t

c

(Rs)ii = min

trace[Rs]. (58)

0≤s≤t

i=1

The aim is then, for a given time t, ﬁnding the partition with the largest value for r(t;H). For t = 0, the most stable partition is that in which all vertices are their own clusters. Interestingly, for t = 1, maximizing stability is equivalent to maximizing Newman-Girvan modularity (Section III.C.2). The cut size of the partition (Sec-

- tion IV.A) equals [r(0) − r(1)], so it is also a one-step


measure. In the limit t → ∞, the most stable partition coincides with the Fiedler partition (Fiedler, 1973, 1975), i. e. the bipartition where vertices are put in the same class according to the signs of the corresponding component of the Fiedler eigenvector (Section IV.A). Therefore, the measure r(t;H) is very general, and gives a unifying interpretation in the framework of the random walk of several measures that were deﬁned in diﬀerent contexts. In particular, modularity has a natural interpretation in this dynamic picture (Lambiotte et al., 2008). Since the size of stable clusters increases with t, time can be considered as a resolution parameter. Resolution can be ﬁne tuned by taking time as a continuous variable (the extension of the formalism is straightforward); the linearization of the stability measure at small (continuous) times delivers multiresolution versions of modularity (Arenas et al., 2008b; Reichardt and Bornholdt, 2006a) (Section XII.A).

In a method by Weinan et al. (Weinan et al., 2008), the best partition of a graph in k clusters is such that the Markov chain describing a random walk on the metagraph, whose vertices are the clusters of the original graph, gives the best approximation of the full random walk dynamics on the whole graph. The quality of the approximation is given by the distance between the left stochastic matrices of the two processes, which thus needs to be minimized. The minimization is performed by using a variant of the k-means algorithm (Section IV.C), and the result is the best obtained out of l runs starting from diﬀerent initial conditions, a strategy that considerably improves the quality of the optimum. The time complexity is O[tlk(n + m)], where t is the number of steps required to reach convergence. The optimal number of clusters could in principle be determined by analyzing how the quality of the approximation varies with k, but the authors do not give any general recipe. The method is rather accurate on the benchmark by Girvan and Newman (Girvan and Newman, 2002) (Section XV.A) and on Zachary’s karate club network. The algorithm by Weinan et al. is asymptotically equivalent to spectral graph partitioning (Section IV.D) when the Markov chain describing the random walk presents a sizeable spectral gap between some of the largest eigenvalues of the transfer matrix (Section A.2), approximately equal to one, and the others.

We conclude this section by describing the Markov Cluster Algorithm (MCL), which was invented by Van Dongen (Dongen, 2000a). This method simulates a peculiar process of ﬂow diﬀusion in a graph. One starts from the transfer matrix of the graph T (Section A.2). The element Tij of the transfer matrix gives the probability that a random walker, sitting at vertex j, moves to i. The sum of the elements of each column of T is one. Each iteration of the algorithm consists of two steps. In the ﬁrst step, called expansion, the transfer matrix of the graph is raised to an integer power p (usually p = 2). The entry Mij of the resulting matrix gives the probability that a random walker, starting from vertex j, reaches i

in p steps (diﬀusion ﬂow). The second step, which has no physical counterpart, consists in raising each single entry of the matrix M to some power α, where α is now realvalued. This operation, called inﬂation, enhances the weights between pairs of vertices with large values of the diﬀusion ﬂow, which are likely to be in the same community. Next, the elements of each column must be divided by their sum, such that the sum of the elements of the column equals one and a new transfer matrix is recovered. After some iterations, the process delivers a stable matrix, with some remarkable properties. Its elements are either zero or one, so it is a sort of adjacency matrix. Most importantly, the graph described by the matrix is disconnected, and its connected components are the communities of the original graph. The method is really simple to implement, which is the main reason of its success:

- as of now, the MCL is one of the most used clustering algorithms in bioinformatics. The code can be downloaded from http://www.micans.org/mcl/. Due to the matrix multiplication of the expansion step, the algorithm should scale as O(n3), even if the graph is sparse, as the running matrix becomes quickly dense after a few steps of the algorithm. However, while computing the matrix multiplication, MCL keeps only a maximum number k of non-zero elements per column, where k is usually much smaller than n. So, the actual worst-case running time of the algorithm is O(nk2) on a sparse graph. A problem of the method is the fact that the ﬁnal partition is sensitive to the parameter α used in the inﬂation step. Therefore several diﬀerent partitions can be obtained, and it is not clear which are the most meaningful or representative.


- C. Synchronization


Synchronization (Pikovsky et al., 2001) is an emergent phenomenon occurring in systems of interacting units and is ubiquitous in nature, society and technology. In a synchronized state, the units of the system are in the same or similar state(s) at every time. Synchronization has also been applied to ﬁnd communities in graphs. If oscillators are placed at the vertices, with initial random phases, and have nearest-neighbour interactions, oscillators in the same community synchronize ﬁrst, whereas a full synchronization requires a longer time. So, if one follows the time evolution of the process, states with synchronized clusters of vertices can be quite stable and longlived, so they can be easily recognized. This was ﬁrst shown by Arenas, Dı´az-Guilera and P´erez-Vicente (Arenas et al., 2006). They used Kuramoto oscillators (Kuramoto, 1984), which are coupled two-dimensional vectors endowed with a proper frequency of oscillations. In the Kuramoto model, the phase θi of oscillator i evolves according to the following dynamics

dθi dt

= ωi +

j

K sin(θj − θi), (59)

where ωi is the natural frequency of i, K the strength of the coupling between oscillators and the sum runs over all oscillators (mean ﬁeld regime). If the interaction coupling exceeds a threshold, depending on the width of the distribution of natural frequencies, the dynamics leads to synchronization. If the dynamics runs on a graph, each oscillator is coupled only to its nearest neighbors. In order to reveal the eﬀect of local synchronization, Arenas et al. introduced the local order parameter

ρij(t) = cos[θi(t) − θj(t)] , (60)

measuring the average correlation between oscillators i and j. The average is computed over diﬀerent initial conditions. By visualizing the correlation matrix ρ(t) at a given time t, one may distinguish groups of vertices that synchronize together. The groups can be identiﬁed by means of the dynamic connectivity matrix Dt(T), which is a binary matrix obtained from ρ(t) by thresholding its entries. The dynamic connectivity matrix embodies information about both the synchronization dynamics and the underlying graph topology. From the spectrum of Dt(T) it is possible to derive the number of disconnected components at time t. By plotting the number of components as a function of time, plateaus may appear at some characteristic time scales, indicating structural scales of the graph with robust communities (Fig. 19). Partitions corresponding to long plateaus are characterized by high values of the modularity of Newman and Girvan (Section III.C.2) on graphs with homogeneous degree distributions, whereas such correlation is poor in the presence of hubs (Arenas and Dı´az-Guilera, 2007). Indeed, it has been proven that the stability (Eq. 58) of the dynamics associated to the standard Laplacian matrix, which describes the convergence towards synchronization of the Kuramoto model with equal intrinsic frequencies, coincides with modularity only for graphs whose vertices have the same degree (Lambiotte et al., 2008). The appearance of plateaus at diﬀerent time scales hints to a hierarchical organization of the graph. After a suﬃciently long t all oscillators are synchronized and the whole system behaves as a single component. Interestingly, Arenas et al. found that the structural scales revealed by synchronization correspond to groups of eigenvalues of the Laplacian matrix of the graph, separated by gaps (Fig. 19).

Based on the same principle, Boccaletti et al. designed a community detection method based on synchronization (Boccaletti et al., 2007). The synchronization dynamics is a variation of Kuramoto’s model, the opinion changing rate (OCR) model (Pluchino et al., 2005). Here the interaction coupling between adjacent vertices is weighted by a term proportional to a (negative) power of the betweenness of the edge connecting the vertices (Section V.A), with exponent α. The evolution equations of the model are solved by decreasing the value of α during the evolution of the dynamics, starting from a conﬁguration in which the system is fully synchronized (α = 0). The graph tends to get split into clusters of synchronized elements, because the interaction strengths

100

100

13-4

15-2

i

i

10

10

time 100

time 100

100

100

|13-4<br><br>|
|---|


15-2

i

i

10

10

0.1 1 1/λi

0.1 1 1/λi

- FIG. 19 Synchronization of Kuramoto oscillators on graphs with two hierarchical levels of communities. (Top) The number of diﬀerent synchronized components is plotted versus time for two graphs with diﬀerent densities of edges within the clusters. (Bottom) The rank index of the eivenvalues of the Laplacian matrices of the same two graphs of the upper panels is plotted versus the inverse eigenvalues (the ranking goes from the largest to the smallest eigenvalue). The two types of communities are revealed by the plateaus. Reprinted ﬁgure with permission from Ref. (Arenas et al., 2006). c 2006 by the American Physical Society.


across inter-cluster edges get suppressed due to their high betweenness scores. By varying α, diﬀerent partitions are recovered, from the graph as a whole until the vertices

- as separate communities: the partition with the largest value of modularity is taken as the most relevant. The algorithm scales in a time O(mn), or O(n2) on sparse graphs, and gives good results in practical examples, including Zachary’s karate club (Zachary, 1977) and the benchmark by Girvan and Newman (Girvan and Newman, 2002) (Section XV.A). The method can be reﬁned by homogeneizing the natural frequencies of the oscillators during the evolution of the system. In this way, the system becomes more stable and partitions with higher modularity values can be recovered.


In a recent paper by Li et al. (Li et al., 2008a), it was

shown that synchronized clusters in modular networks are characterized by interfacial vertices, whose oscillation frequency is intermediate between those of two or more clusters, so that they do not belong to a speciﬁc community. Li et al. used this result to devise a technique able to detect overlapping communities.

Synchronization-based algorithms may not be reliable when communities are very diﬀerent in size; tests in this direction are still missing.

###### IX. METHODS BASED ON STATISTICAL INFERENCE

Statistical inference (Mackay, 2003) aims at deducing properties of data sets, starting from a set of observa-

tions and model hypotheses. If the data set is a graph, the model, based on hypotheses on how vertices are connected to each other, has to ﬁt the actual graph topology. In this section we review those clustering techniques attempting to ﬁnd the best ﬁt of a model to the graph, where the model assumes that vertices have some sort of classiﬁcation, based on their connectivity patterns. We mainly focus on methods adopting Bayesian inference (Winkler, 2003), in which the best ﬁt is obtained through the maximization of a likelihood (generative models), but we also discuss related techniques, based on blockmodeling (Doreian et al., 2005), model selection (Burnham and Anderson, 2002) and information theory (Mackay, 2003).

- A. Generative models


Bayesian inference uses observations to estimate the probability that a given hypothesis is true. It consists of two ingredients: the evidence, expressed by the information D one has about the system (e.g., through measurements); a statistical model with parameters {θ}. Bayesian inference starts by writing the likelihood P(D|{θ}) that the observed evidence is produced by the model for a given set of parameters {θ}. The aim is to determine the choice of {θ} that maximizes the posterior distribution P({θ}|D) of the parameters given the model and the evidence. By using Bayes’ theorem one has

P({θ}|D) =

1 Z

P(D|{θ})P({θ}), (61)

where P({θ}) is the prior distribution of the model parameters and

Z = P(D|{θ})P({θ})dθ. (62)

Unfortunately, computing the integral 62 is a major challenge. Moreover, the choice of the prior distribution

- P({θ}) is non-obvious. Generative models diﬀer from each other by the choice of the model and the way they address these two issues.


Bayesian inference is frequently used in the analysis and modeling of real graphs, including social (Handcock et al., 2007; Koskinen and Snijders, 2007; Rhodes and Keefe, 2007) and biological networks (Berg and L¨ssig,

- 2006; Rowicka and Kudlicki, 2004). Graph clustering can be considered a speciﬁc example of inference problem. Here, the evidence is represented by the graph structure (adjacency or weight matrix) and there is an additional ingredient, represented by the classiﬁcation of the vertices in groups, which is a hidden (or missing) information that one wishes to infer along with the parameters of the model which is supposed to be responsible for the classiﬁcation. This idea is at the basis of several recent papers, which we discuss here. In all these works, one essentially maximizes the likelihood P(D|{θ}) that the


model is consistent with the observed graph structure, with diﬀerent constraints. We specify the set of parameters {θ} as the triplet ({q},{π},k), where {q} indicates the community assignment of the vertices, {π} the model parameters, and k the number of clusters. In the following we shall stick to the notation of the papers, so the variables above may be indicated by diﬀerent symbols. However, to better show what each method speciﬁcally does we shall refer to our general notation at the end of the section.

Hastings (Hastings, 2006) chooses as a model of network with communities the planted partition model (Section XV). In it, n vertices are assigned to q groups: vertices of the same group are linked with a probability pin, while vertices of diﬀerent groups are linked with a probability pout. If pin > pout, the model graph has a built-in community structure. The vertex classiﬁcation is indicated by the set of labels {qi}. The probability that, given a graph, the classiﬁcation {qi} is the right one according to the model is14

p({qi}) ∝ {exp[−

ij

iqj −

Jδq

iqj/2]}−1, (63)

J δq

i=j

where J = log{[pin(1 − pout)]/[pout(1 − pin)]}, J = log[(1−pin)/(1−pout)] and the ﬁrst sum runs over nearest neighboring vertices. Maximizing p({qi}) is equivalent to minimizing the argument of the exponential, which is the Hamiltonian of a Potts model with short- and longrange interactions. For pin > pout, J > 0 and J < 0, so the model is a spin glass with ferromagnetic nearestneighbor interactions and antiferromagnetic long-range interactions, similar to the model proposed by Reichardt and Bornholdt to generalize Newman-Girvan modularity (Reichardt and Bornholdt, 2006a) (Section VI.B). Hastings used belief propagation (Gallager, 1963) to ﬁnd the ground state of the spin model. On sparse graphs, the complexity of the algorithm is expected to be O(nlogα n), where α needs to be estimated numerically. In principle one needs to input the parameters pin and pout, which are usually unknown in practical applications. However, it turns out that they can be chosen rather arbitrarily, and that bad choices can be recognized and corrected.

Newman and Leicht (Newman and Leicht, 2007) have recently proposed a similar method based on a mixture model and the expectation-maximization technique (Dempster et al., 1977). The method bears some resemblance with an a posteriori blockmodel previously introduced by Snijders and Nowicki (Nowicki and Snijders, 2001; Snijders and Nowicki, 1997). They start from a directed graph with n vertices, whose vertices fall into c classes. The group of vertex i is indicated by gi, πr the

14 The actual likelihood includes an additional factor expressing the a priori probability of the community sizes. Hastings assumes that this probability is constant.

fraction of vertices in group r, and θri the probability that there is a directed edge from vertices of group r to

vertex i. By deﬁnition, the sets {πi} and {θri} satisfy the normalization conditions cr=1 πr = 1 and ni=1 θri = 1. Apart from normalization, the probabilities {θri} are assumed to be independent of each other. The best classiﬁcation of the vertices corresponds to the maximum of the average log-likelihood L¯ that the model, described by the values of the parameters {πi} and {θri} ﬁts the adjacency matrix A of the graph. The expression of the average log-likelihood L¯ requires the deﬁnition of the probability qir = Pr(gi = r|A,π,θ), that vertex i belongs to group r. By applying Bayes’ theorem the probabilities {qir} can be computed in terms of the {πi} and the {θri}, as

πr j θrjAij s πs j θsjAij

qir =

, (64)

while the maximization of the average log-likelihood L¯, under the normalization constraints of the model variables {πi} and {θri}, yields the relations

Aijqir i kiqir

1 n i

qir, θrj = i

πr =

, (65)

where ki is the outdegree of vertex i. Equations 64 and 65 are self-consistent, and can be solved by iterating them to convergence, starting from a suitable set of initial conditions. Convergence is fast, so the algorithm could be applied to fairly large graphs, with up to about 106 vertices.

The method, designed for directed graphs, can be easily extended to the undirected case, whereas an extension to weighted graphs is not straightforwad. A nice feature of the method is that it does not require any preliminary indication on what type of structure to look for; the resulting structure is the most likely classiﬁcation based on the connectivity patterns of the vertices. Therefore, various types of structures can be detected, not necessarily communities. For instance, multipartite structure could be uncovered, or mixed patterns where multipartite subgraphs coexist with communities, etc.. In this respect, it is more powerful than most methods of community detection, which are bound to focus only on proper communities, i. e. subgraphs with more internal than external edges. In addition, since partitions are deﬁned by assigning probability values to the vertices, expressing the extent of their membership in a group, it is possible that some vertices are not clearly assigned to a group, but to more groups, so the method is able to deal with overlapping communities. The main drawback of the algorithm is the fact that one needs to specify the number of groups c at the beginning of the calculation, a number that is typically unknown for real networks. It is possible to derive this information self-consistently by maximizing the probability that the data are reproduced by partitions with a given number of clusters. But this procedure involves some degree of approximation, and the results are often not good.

![image 34](Community Detection in Graphs_images/imageFile34.png)

![image 35](Community Detection in Graphs_images/imageFile35.png)

###### a)c)

![image 36](Community Detection in Graphs_images/imageFile36.png)

![image 37](Community Detection in Graphs_images/imageFile37.png)

![image 38](Community Detection in Graphs_images/imageFile38.png)

![image 39](Community Detection in Graphs_images/imageFile39.png)

![image 40](Community Detection in Graphs_images/imageFile40.png)

![image 41](Community Detection in Graphs_images/imageFile41.png)

![image 42](Community Detection in Graphs_images/imageFile42.png)

![image 43](Community Detection in Graphs_images/imageFile43.png)

![image 44](Community Detection in Graphs_images/imageFile44.png)

![image 45](Community Detection in Graphs_images/imageFile45.png)

![image 46](Community Detection in Graphs_images/imageFile46.png)

![image 47](Community Detection in Graphs_images/imageFile47.png)

![image 48](Community Detection in Graphs_images/imageFile48.png)

![image 49](Community Detection in Graphs_images/imageFile49.png)

![image 50](Community Detection in Graphs_images/imageFile50.png)

![image 51](Community Detection in Graphs_images/imageFile51.png)

![image 52](Community Detection in Graphs_images/imageFile52.png)

![image 53](Community Detection in Graphs_images/imageFile53.png)

![image 54](Community Detection in Graphs_images/imageFile54.png)

![image 55](Community Detection in Graphs_images/imageFile55.png)

###### b)

![image 56](Community Detection in Graphs_images/imageFile56.png)

![image 57](Community Detection in Graphs_images/imageFile57.png)

![image 58](Community Detection in Graphs_images/imageFile58.png)

![image 59](Community Detection in Graphs_images/imageFile59.png)

![image 60](Community Detection in Graphs_images/imageFile60.png)

![image 61](Community Detection in Graphs_images/imageFile61.png)

![image 62](Community Detection in Graphs_images/imageFile62.png)

![image 63](Community Detection in Graphs_images/imageFile63.png)

![image 64](Community Detection in Graphs_images/imageFile64.png)

![image 65](Community Detection in Graphs_images/imageFile65.png)

![image 66](Community Detection in Graphs_images/imageFile66.png)

![image 67](Community Detection in Graphs_images/imageFile67.png)

FIG. 20 Problem of method by Newman and Leicht. By applying the method to the illustrated complete bipartite graph (colors indicate the vertex classes) the natural group structure

###### c) is not recovered; instead, the most likely classiﬁcations area) and b). Reprinted ﬁgure with permission from Ref. (Ra-masco and Mungan, 2008). c 2008 by the American PhysicalSociety.

In a recent study it has been shown that the method by Newman and Leicht enables one to rank vertices based on their degree of inﬂuence on other vertices, which allows to identify the vertices responsible for the group structure and its stability (Mungan and Ramasco, 2008). A very similar technique has also been applied by V´zquez (Vazquez, 2008) to the problem of population stratiﬁcation, where animal populations and their attributes are represented as hypergraphs (Section A.1). V´zquez also suggested an interesting criterion to decide the optimal number of clusters, namely picking the number c¯ whose solution has the greatest similarity with solutions obtained at diﬀerent values of c. The similarity between two partitions can be estimated in various ways, for instance by computing the normalized mutual information (Section XV). In a successive paper (Vazquez, 2008), V´zquez showed that better results are obtained if the classiﬁcation likelihood is maximized by using Variational Bayes (Beal, 2003; Jordan et al., 1999).

Ramasco and Mungan (Ramasco and Mungan, 2008) remarked that the normalization condition on the probabilities {θri} implies that each group r must have nonzero outdegree and that therefore the method fails to detect the intuitive group structure of (directed) bipartite graphs (Fig. 20). To avoid this problem, they proposed a modiﬁcation, that consists in introducing three sets for the edge probabilities {θri}, relative to edges going from group r to vertex i (as before), from i to r and in both directions, respectively. Furthermore, they used the average entropy of the classiﬁcation Sq = −( i,r qir ln qir)/n, where the qir are the analogs of the probabilities in Eq. 64, to infer the optimal number of groups, that the method of Newman and Leicht is

unable to provide. Another technique similar to that by Newman and Leicht has been designed by Ren et al. (Ren et al., 2009). The model is based on the group fractions {πi}, deﬁned as above, and a set of probabilities {βr,i}, expressing the relevance of vertex i for group r; the basic assumption is that the probability that two vertices of the same group are connected by an edge is proportional to the product of the relevances of the two vertices. In this way, there is an explicit relation between group membership and edge density, and the method can only detect community structure. The community assignments are recovered through an expectation-maximization procedure that closely follows that by Newman and Leicht.

Maximum likelihood estimation has been used by Copiˇcˇ et al. to deﬁne an axiomatization of the problem of graph clustering and its related concepts (Copiˇcˇ

- et al., 2005). The starting point is again the planted partition model (Section XV), with probabilities pin and pout. A novelty of the approach is the introduction of the size matrix S, whose element Sij indicates the maximum strength of interaction between vertices i and j. For instance, in a graph with unweighted connections, all elements of S equal 1. In this case, the probability that the graph conceals a community structure coincides with the expression (63) by Hastings. Copiˇcˇ et al. used this probability as a quality function to deﬁne rankings between graph partitions (likelihood rankings). The authors show that the likelihood rankings satisfy a number of general properties, which should be satisﬁed by any reasonable ranking. They also propose an algorithm to ﬁnd the maximum likelihood partition, by using the auxiliary concept of pseudo-community structure, i. e. a grouping of the graph vertices in which it is speciﬁed which pairs of vertices stay in the same community and which pairs instead stay in diﬀerent communities. A pseudo-community may not be a community because the transitive property is not generally valid, as the focus is on pairwise vertex relationships: it may happen that i and j are classiﬁed in the same group, and that j and


- k are classiﬁed in the same group, but that i and k are not classiﬁed as belonging to the same group. We believe that the work by Copiˇcˇ et al. is an important ﬁrst step towards a more rigorous formalization of the problem of graph clustering.


Zanghi et al. (Zanghi et al., 2008) have designed a clustering technique that lies somewhat in between the method by Hastings and that by Newman and Leicht. As in Ref. (Hastings, 2006), they use the planted partition model to represent a graph with community structure; as in Ref. (Newman and Leicht, 2007), they maximize the classiﬁcation likelihood using an expectationmaximization algorithm (Dempster et al., 1977). The algorithm runs for a ﬁxed number of clusters q, like that by Newman and Leicht; however, the optimal number of clusters can be determined by running the algorithm for a range of q-values and selecting the solution that maximizes the Integrated Classiﬁcation Likelihood introduced by Biernacki et al. (Biernacki et al., 2000). The

time complexity of the algorithm is O(n2).

Hofman and Wiggins have proposed a general Bayesian approach to the problem of graph clustering (Hofman and Wiggins, 2008). Like Hastings (Hastings, 2006), they model a graph with community structure as in the planted partition problem (Section XV), in that there are two probabilities θc and θd that there is an edge between vertices of the same or diﬀerent clusters, respectively. The unobserved community structure is indicated by the set of labels  σ for the vertices; πr is again the fraction of vertices in group r. The conjugate prior distributions p(θ) and p( π) are chosen to be Beta and Dirichlet distributions. The most probable number of clusters K∗ maximizes the conditional probability p(K|A) that there are K clusters, given the matrix A. Like Hastings, Hofman and Wiggins assume that the prior probability p(K) on the number of clusters is a smooth function, therefore maximizing p(K|A) amounts to maximizing the Bayesian evidence p(A|K) ∝ p(K|A)/p(K), obtained by integrating the joint distribution p(A, σ| π,θ,K), which is factorizable, over the model parameters θ and  π. The integration can be performed exactly only for small graphs. Hofman and Wiggins used Variational Bayes (Beal, 2003; Jordan et al., 1999), in order to compute controlled approximations of p(A|K). The complexity of the algorithm was estimated numerically on synthetic graphs, yielding O(nα), with α = 1.44. In fact, the main limitation comes from high memory requirements. The method is more powerful than the one by Hastings (Hastings, 2006), in that the edge probabilities θ are inferred by the procedure itself and need not be speciﬁed (or guessed) at the beginning. It also includes the expectation-maximization approach by Newman and Leicht (Newman and Leicht, 2007) as a special case, with the big advantage that the number of clusters need not be given as an input, but is an output of the method. The software of the algorithm can be found at http://www.columbia.edu/∼chw2/.

We conclude with a brief summary of the main techniques described above, coming back to our notation at the beginning of the section. In the method by Hastings, one maximizes the likelihood P(D|{q},{π},k) over the set of all possible community assignments {q}, given the number of clusters k and the model parameters (i. e. the linking probabilities pin and pout). Newman and Leicht maximize the likelihood P(D|{q},{π},k) for a given number of clusters, over the possible choices for the model parameters and community assignments, by deriving the optimal choices for both variables with a self-consistent procedure. Hofman and Wiggins maximize the likelihood PHW(k) =

{q} P(D|{q},{π},k)P({q}|{π})P({π})dπ over the possible choices for the number of clusters.

- B. Blockmodeling, model selection and information theory


Block modeling is a common approach in statistics and social network analysis to decompose a graph in classes of vertices with common properties. In this way, a sim-

- pler description of the graph is attained. Vertices are usually grouped in classes of equivalence. There are two main deﬁnitions of topological equivalence for vertices: structural equivalence (F.Lorrain and White, 1971) (Section III.B.4), in which vertices are equivalent if they have the same neighbors15; regular equivalence (Everett and Borgatti, 1994; White and Reitz, 1983), in which vertices of a class have similar connection patterns to vertices of the other classes (ex. parents/children). Regular equivalence does not require that ties/edges are restricted to speciﬁc target vertices, so it is a more general concept than structural equivalence. Indeed, vertices which are structurally equivalent are also regularly equivalent, but the inverse is not true. The concept of structural equivalence can be generalized to probabilistic models, in which one compares classes of graphs, not single graphs, characterized by a set of linking probabilities between the vertices. In this case, vertices are organized in classes such that the linking probabilities of a vertex with all other vertices of the graph are the same for vertices in the same class, which are called stochastically equivalent (Fienberg and Wasserman, 1981; Holland et al., 1983).


A thorough discussion of blockmodeling is beyond the scope of this review: we point the reader to Ref. (Doreian et al., 2005). Here we discuss a recent work by Reichardt and White (Reichardt and White, 2007). Let us suppose to have a directed graph with n vertices and m edges. A classiﬁcation of the graph is indicated by the set of labels {σ}, where σi = 1,2,...,q is the class of vertex i. The corresponding blockmodel, or image graph, is expressed by a q×q adjacency matrix B: Bq

1q2 = 1 if edges between classes q1 and q2 are allowed, otherwise it is zero. The aim is ﬁnding the classiﬁcation {σ} and the matrix B that best ﬁts the adjacency matrix A of the graph. The goodness of the ﬁt is expressed by the quality function

1 m i=j

QB({σ}) =

iσj +bij(1−Aij)(1−Bσ

[aijAijBσ

iσj)],

(66) where aij (bij) reward the presence (absence) of edges between vertices if there are edges (non-edges) between the corresponding classes, and m is the number of edges of the graph, as usual. Eq. 66 can be rewritten as a sum over the classes

QB({σ}) =

- q
- r,s


(ers − [ers])Brs, (67)

15 More generally, if they have the same ties/edges to the same vertices, as in a social network there may be diﬀerent types of ties/edges.

js and [ers] = (1/m) i=j bijδσ

by setting ers = (1/m) i=j(aij + bij)Aijδσ

irδσ

js. If one sets aij = 1 − pij and bij = pij, pij can be interpreted as the linking probability between i and j, in some null model. Thereof, ers becomes the number of edges running between vertices of class r and s, and [ers] the expected number of edges in the null model. Reichardt and White set pij = kioutkjin/m, which deﬁnes the same null model of Newman-Girvan modularity for directed graphs (Section VI.B). In fact, if the image graph has only selfedges, i. e. Brs = δrs, the quality function QB({σ}) exactly matches modularity. Other choices for the image graph are possible, however. For instance, a matrix Brs = 1 − δrs describes the classes of a q-partite graph (Section A.1). From Eq. 67 we see that, for a given classiﬁcation {σ}, the image graph that yields the largest value of the quality function QB({σ}) is that in which Brs = 1 when the term ers − [ers] is non-negative, and Brs = 0 when the term ers − [ers] is non-positive. So, the best classiﬁcation is the one maximizing the quality function

irδσ

- 1

- 2


Q∗({σ}) =

- q
- r,s


||ers − [ers]||, (68)

where all terms of the sum are taken in absolute value. The function Q∗({σ}) is maximized via simulated annealing. The absolute maximum Qmax is obtained by construction when q matches the number q∗ of structural equivalence classes of the graph. However, the absolute maximum Qmax does not have a meaning by itself, as one can achieve fairly high values of Q∗({σ}) also for null model instances of the original graph, i. e. if one randomizes the graph by keeping the same expected indegree and outdegree sequences. In practical applications, the optimal number of classes is determined by comparing the ratio Q∗(q)/Qmax [Q∗(q) is the maximum of Q∗({σ}) for q classes] with the expected ratio for the null model. Since classiﬁcations for diﬀerent q-values are not hierarchically ordered, overlaps between classes may be detected. The method can be trivially extended to the case of weighted graphs.

Model selection (Burnham and Anderson, 2002) aims at ﬁnding models which are at the same time simple and good at describing a system/process. A basic example of a model selection problem is curve ﬁtting. There is no clear-cut recipe to select a model, but a bunch of heuristics, like Akaike Information Criterion (AIC) (Akaike, 1974), Bayesian Information Criterion (BIC) (Schwarz, 1978), Minimum Description Length (MDL) (Gru¨nwald et al., 2005; Rissanen, 1978), Minimum Message Length (MML) (Wallace and Boulton, 1968), etc..

The modular structure of a graph can be considered as a compressed description of the graph to approximate the whole information contained in its adjacency matrix. Based on this idea, Rosvall and Bergstrom (Rosvall and Bergstrom, 2007) envisioned a communication process in which a partition of a graph in communities represents a

synthesis Y of the full structure that a signaler sends to a receiver, who tries to infer the original graph topology X from it (Fig. 21). The same idea is at the basis of an earlier method by Sun et al. (Sun et al., 2007), which was originally designed for bipartite graphs evolving in time and will be described in Section XIII. The best partition corresponds to the signal Y that contains the most information about X. This can be quantitatively assessed by the minimization of the conditional information H(X|Y ) of X given Y ,

 

 , (69)

q

ni(ni − 1)/2 lii i>j

ninj lij

H(X|Y ) = log

i=1

where q is the number of clusters, ni the number of vertices in cluster i, lij the number of edges between clusters i and j. We remark that, if one imposes no constraints on q, H(X|Y ) is minimal in the trivial case in which

- X = Y (H(X|X) = 0). This solution is not acceptable because it does not correspond to a compression of information with respect to the original data set. One has to look for the ideal tradeoﬀ between a good compression and a small enough information H(X|Y ). The Minimum Description Length (MDL) principle (Gr¨unwald et al., 2005; Rissanen, 1978) provides a solution to this problem, which amounts to the minimization of a function given by H(X|Y ) plus a function of the number n of vertices, m of edges and q of clusters. The optimization is performed by simulated annealing, so the method is rather slow and can be applied to graphs with up to about 104 vertices. However, faster techniques may in principle be used, even if they imply a loss in accuracy. The method appears superior than modularity optimization, especially when communities are of diﬀerent sizes. This comes from tests performed on the benchmark of Girvan and Newman (Girvan and Newman, 2002) (Section XV.A), both in its original version and in asymmetric versions, proposed by the authors, where the clusters have diﬀerent sizes or diﬀerent average degrees. In addition, it can detect other types of vertex classiﬁcations than communities, as in Eq. 69 there are no constraints on the relative importance of the edge densities within communities with respect to the edge densities between communities. The software of the algorithm can be found


- at http://www.tp.umu.se/∼rosvall/code.html. In a recent paper (Rosvall and Bergstrom, 2008), Ros-


vall and Bergstrom pursued the same idea of describing a graph by using less information than that encoded in the full adjacency matrix. The goal is to optimally compress the information needed to describe the process of information diﬀusion across the graph. Random walk is chosen as a proxy of information diﬀusion. A twolevel description, in which one gives unique names to important structures of the graph and to vertices within the same structure, but the vertex names are recycled among diﬀerent structures, leads to a more compact description than by simply coding all vertices with diﬀerent names. This is similar to the procedure usually adopted

in geographic maps, where the structures are cities and one usually chooses the same names for streets of different cities, as long as there is only one street with a given name in the same city. Huﬀman coding (Huﬀman, 1952) is used to name vertices. For the random walk, the above-mentioned structures are communities, as it is intuitive that walkers will spend a lot of time within them, so they play a crucial role in the process of information diﬀusion. Graph clustering turns then into the following coding problem: ﬁnding the partition that yields the minimum description length of an inﬁnite random walk. Such description length consists of two terms, expressing the Shannon entropy of the random walk within and between clusters. Every time the walker steps to a diﬀerent cluster, one needs to use the codeword of that cluster in the description, to inform the decoder of the transition16. Clearly, if clusters are well separated from each other, transitions of the random walker between clusters will be unfrequent, so it is advantageous to use the map, with the clusters as regions, because in the description of the random walk the codewords of the clusters will not be repeated many times, while there is a considerable saving in the description due to the limited length of the codewords used to denote the vertices. Instead, if there are no well-deﬁned clusters and/or if the partition is not representative of the actual community structure of the graph, transitions between the clusters of the partition will be very frequent and there will be little or no gain by using the two-level description of the map. The minimization of the description length is carried out by combining greedy search with simulated annealing. In a successive paper (Rosvall et al., 2009), the authors adopted the fast greedy technique designed by Blondel et al. for modularity optimization (Blondel et al., 2008), with some reﬁnements. The method can be applied to weighted graphs, both undirected and directed. In the latter case, the random walk process is modiﬁed by introducing a teleportation probability τ, to guarantee ergodicity, just like in Google’s PageRank algorithm (Brin and Page, 1998). The partitions of directed graphs obtained by the method diﬀer from those derived by optimizing the directed version of Newman-Girvan modularity (Section VI.B): this is due to the fact that modularity focuses on pairwise relationships between vertices, so it does not capture ﬂows. The code of the method is available at http://www.tp.umu.se/∼rosvall/code.html.

Chakrabarti (Chakrabarti, 2004) has applied the MDL principle to put the adjacency matrix of a graph into the (approximately) block diagonal form representing the best tradeoﬀ between having a limited number of blocks, for a good compression of the graph topology, and having very homogeneous blocks, for a compact description

16 Instead, for a one-level description, in which all vertices have diﬀerent names, it is enough to specify the codeword of the vertex reached at every step to completely deﬁne the process, but this may be costly.

##### X Y Z

|Actual| |Encoder|Signal|Decoder| |Network|
|---|---|---|---|---|---|---|
|network| | | | | |estimates|


k

s

n

l

l

l

n

n l

l

l

FIG. 21 Basic principle of the method by Rosvall and Bergstrom (Rosvall and Bergstrom, 2007). An encoder sends to a decoder a compressed information about the topology of the graph on the left. The information gives a coarse description of the graph, which is used by the decoder to deduce the original graph structure. Reprinted ﬁgure with permission from Ref. (Rosvall and Bergstrom, 2007). c 2007 by the National Academy of Science of the USA.

of their structure. The total encoding cost T includes the information on the total number of vertices of the graph, on the number of blocks and the number of vertices and edges in each block, along with the adjacency matrices of the blocks. The minimization of T is carried out by starting from the partition in which the graph is a single cluster. At each step, one operates a bipartition of the cluster of the partition with the maximum Shannon entropy per vertex. The split is carried out in order to remove from the original cluster those vertices carrying the highest contribution to the entropy per vertex of the cluster. Then, starting from the resulting partition, which has one more cluster than the previous one, T is optimized among those partitions with the same number of clusters. The procedure continues until one reaches a number of clusters k , for which T cannot be further decreased. The method by Chakrabarti has complexity O[I(k )2m], where I is the number of iterations required for the convergence of the optimization for a given number of clusters, which is usually small (I ≤ 20 in the experiments performed by the author). Therefore the algorithm can be applied to fairly large graphs.

Information theory has also been used to detect communities in graphs. Ziv et al. (Ziv et al., 2005) have designed a method in which the information contained in the graph topology is compressed such to preserve some predeﬁned information. This is the basic principle of the information bottleneck method (Tishby et al., 1999). To understand this criterion, we need to introduce an important measure, the mutual information I(X,Y ) (Mackay,

- 2003) of two random variables X and Y . It is deﬁned as


I(X,Y ) =

x y

P(x,y) P(x)P(y)

P(x,y)log

, (70)

where P(x) indicates the probability that X = x (similarly for P(y)) and P(x,y) is the joint probability of X and Y , i. e. P(x,y) = P(X = x,Y = y). The measure I(X,Y ) tells how much we learn about X if we know Y , and viceversa. If X is the input variable, Z the variable specifying the partition and Y the variable encoding the information we want to keep, which is called relevant variable, the goal is to minimize the mutual information between X and Z (to achieve the largest possible data compression), under the constraint that the information on Y extractable from Z be accurate. The optimal tradeoﬀ between the values of I(X,Z) and I(Y,Z) (i. e. compression versus accuracy) is expressed by the minimization of a functional, where the relative weight of the two contributions is given by a parameter playing the role of a temperature. In the case of graph clustering, the question is what to choose as relevant information variable. Ziv et al. proposed to adopt the structural information encoded in the process of diﬀusion on the graph. They also introduce the concept of network modularity, which characterizes the graph as a whole, not a speciﬁc partition like the modularity by Newman and Girvan (Section III.C.2). The network modularity is deﬁned as the area under the information curve, which essentially represents the relation between the extent of compression and accuracy for all solutions found by the method and all possible numbers of clusters. The software of the algorithm by Ziv et al. can be found at http://www.columbia.edu/∼chw2/.

###### X. ALTERNATIVE METHODS

In this section we describe some algorithms that do not ﬁt in the previous categories, although some overlap

is possible.

Raghavan et al. (Raghavan et al., 2007) have designed a simple and fast method based on label propagation. Vertices are initially given unique labels (e.g. their vertex labels). At each iteration, a sweep over all vertices, in random sequential order, is performed: each vertex takes the label shared by the majority of its neighbors. If there is no unique majority, one of the majority labels is picked at random. In this way, labels propagate across the graph: most labels will disappear, others will dominate. The process reaches convergence when each vertex has the majority label of its neighbors. Communities are deﬁned as groups of vertices having identical labels

- at convergence. By construction, each vertex has more neighbors in its community than in any other community. This resembles the strong deﬁnition of community we have discussed in Section III.B.2, although the latter is stricter, in that each vertex must have more neighbors in its community than in the rest of the graph. The algorithm does not deliver a unique solution. Due to the many ties encountered along the process it is possible to derive diﬀerent partitions starting from the same initial condition, with diﬀerent random seeds. Tests on real graphs show that all partitions found are similar to each other, though. The most precise information that one can extract from the method is contained by aggregating the various partitions obtained, which can be done in various ways. The authors proposed to label each vertex with the set of all labels it has in diﬀerent partitions. Aggregating partitions enables one to detect possible overlapping communities. The main advantage of the method is the fact that it does not need any information on the number and the size of the clusters. It does not need any parameter, either. The time complexity of each iteration of the algorithm is O(m), the number of iterations to convergence appears independent of the graph size, or growing very slowly with it. So the technique is really fast and could be used for the analysis of large systems. In a recent paper (Tib´ely and Kert´esz, 2008), Tibe´ly and Kert´esz showed that the method is equivalent to ﬁnding the local energy minima of a simple zero-temperature kinetic Potts model, and that the number of such energy minima is considerably larger than the number of vertices of the graph. Aggregating partitions as Raghavan et al. suggest leads to a fragmentation of the resulting partition in clusters that are the smaller, the larger the number of aggregated partitions. This is potentially a serious problem of the algorithm by Raghavan et al., especially when large graphs are investigated. In order to eliminate undesired solutions, Barber and Clark introduced some constraints in the optimization process (Barber and Clark, 2009). This amounts to adding some terms to the objective function H whose maximization is equivalent to the original label propagation algorithm17. Interestingly,


- 17 H = 1/2 ij Aijδij, where A is the adjacency matrix of the


if one imposes the constraint that partitions have to be balanced, i. e. that clusters have similar total degrees, the objective function becomes formally equivalent to Newman-Girvan modularity Q (Section III.C.2), so the corresponding version of the label propagation algorithm is essentially based on a local optimization of modularity. Leung et al. have found that the original algorithm by Raghavan et al., applied on online social networks, often yields partitions with one giant community together with much smaller ones (Leung et al., 2009). In order to avoid this disturbing feature, which is an artefact of the algorithm, Leung et al. proposed to modify the method by introducing a score for the labels, which decreases as the label propagates far from the vertex to which the label was originally assigned. When choosing the label of a vertex, the labels of its neighbors are weighted by their scores, therefore a single label cannot span too large portions of the graph (as its weight fades away with the distance from the origin), and no giant communities can be recovered. Tests of the modiﬁed algorithm on the LFR benchmark (Lancichinetti et al., 2008) (Section XII.A) give good results and encourage further investigations.

Bagrow and Bollt designed an agglomerative technique, called L-shell method (Bagrow and Bollt, 2005). It is a procedure that ﬁnds the community of any vertex, although the authors also presented a more general procedure to identify the full community structure of the graph. Communities are deﬁned locally, based on a simple criterion involving the number of edges inside and outside a group of vertices. One starts from a vertex-origin and keeps adding vertices lying on successive shells, where a shell is deﬁned as a set of vertices at a ﬁxed geodesic distance from the origin. The ﬁrst shell includes the nearest neighbours of the origin, the second the next-to-nearest neighbours, and so on. At each iteration, one calculates the number of edges connecting vertices of the new layer to vertices inside and outside the running cluster. If the ratio of these two numbers (“emerging degree”) exceeds some predeﬁned threshold, the vertices of the new shell are added to the cluster, otherwise the process stops. The idea of closing a community by expanding a shell has been previously introduced by Costa (da Fontoura Costa, 2004), in which shells are centered on hubs. However, in this procedure the number of clusters is preassigned and no cluster can contain more than one hub. Because of the local nature of the process, the L-shell method is very fast and can identify communities very quickly. Unfortunately the method works well only when the source vertex is approximately equidistant from the boundary of its community. To overcome this problem, Bagrow and Bollt suggested to repeat the process starting from every vertex and derive a membership

graph and δ is Kronecker’s function. It is just the negative of the energy of a zero-temperature Potts model, as found by Tib´ely and Kerte´sz (Tib´ely and Kert´esz, 2008)

matrix M: the element Mij is one if vertex j belongs to the community of vertex i, otherwise it is zero. The membership matrix can be rewritten by suitably permutating rows and columns based on their mutual distances. The distance between two rows (or columns) is deﬁned as the number of entries whose elements diﬀer. If the graph has a clear community structure, the membership matrix takes a block-diagonal form, where the blocks identify the communities. The method enables one to detect overlaps between communities as well (Porter et al.,

- 2007). Unfortunately, the rearrangement of the matrix requires a time O(n3), so it is quite slow. A variant of the algorithm by Bagrow and Bollt, in which boundary vertices are examined separately and both ﬁrst and second nearest neighbors of the running community are simultaneously investigated, was suggested by Rodrigues et al. (Rodrigues et al., 2007).


A recent methodology introduced by Papadopoulos et al. (Papadopoulos et al., 2009), called Bridge Bounding, is similar to the L-shell algorithm, but here the cluster around a vertex grows until one “hits” the boundary edges. Such edges can be recognized from the values of various measures, like betweenness (Girvan and Newman,

- 2002) or the edge clustering coeﬃcient (Radicchi et al.,


- 2004). The problem is that there are often no clear gaps in the distributions of the values of such measures, so one is forced to set a threshold to automatically identify the boundary edges from the others, and there is no obvious way to do it. The best results of the algorithm are obtained by using a measure consisting of a weighted sum of the edge clustering coeﬃcient over a wider neighborhood of the given edge. This version of the method has a time complexity O( k 2m+ k n), where k is the average degree of the graph.


In another algorithm by Clauset, local communities are discovered through greedy maximization of a local modularity measure (Clauset, 2005). Given a community C, the boundary B is the set of vertices of C with at least one neighbor outside C (Fig. 22). The local modularity R by Clauset is the ratio of the number of edges having both endpoints in C (but at least one in B), with the number of edges having at least one endpoint in B. It is a measure of the sharpness of the community boundary. Its optimization consists of a local exploration of the community starting from a source vertex: at each step the neighboring vertex yielding the largest increase (smallest decrease) of R is added, until the community has reached a predeﬁnite size nc. This greedy optimization takes a time O(n2c k ), where k is the average degree of the graph. The local modularity R has been used in a paper by Hui et al. (Hui et al., 2007), where methods to ﬁnd communities in networks of mobile devices are designed.

Another method, where communities are deﬁned based on a local criterion, was presented by Eckmann and Moses (Eckmann and Moses, 2002). The idea is to use the clustering coeﬃcient (Watts and Strogatz, 1998) of a vertex as a quantity to distinguish tightly connected groups of vertices. Many edges mean many loops inside

U

B

### C

B

U

FIG. 22 Schematic picture of a community C used in the deﬁnition of local modularity by Clauset (Clauset, 2005). The black area indicates the subgraph of C including all vertices of C, whose neighbors are also in C. The boundary B entails the vertices of C with at least one neighbor outside the community. Reprinted ﬁgure with permission from Ref. (Clauset, 2005).

c 2005 by the American Physical Society.

a community, so the vertices of a community are likely to have a large clustering coeﬃcient. The latter can be related to the average distance between pairs of neighbours of the vertex. The possible values of the distance are 1 (if neighbors are connected) or 2 (if they are not), so the average distance lies between 1 and 2. The more triangles there are in the subgraph, the shorter the average distance. Since each vertex always has distance 1 from its neighbours, the fact that the average distance between its neighbours is diﬀerent from 1 reminds what happens when one measures segments on a curved surface. Endowed with a metric, represented by the geodesic distance between vertices/points, and a curvature, the graph can be embedded in a geometric space. Communities appear as portions of the graph with a large curvature. The algorithm was applied to the graph representation of the World Wide Web, where vertices are web pages and edges are the hyperlinks that take users from a page to the other. The authors found that communities correspond to web pages dealing with the same topic.

Long et al. have devised an interesting technique that is able to detect various types of vertex groups, not necessarily communities (Long et al., 2007). The method is based on graph approximation, as it tries to match the original graph topology onto a coarse type of graph, the community prototype graph, which has a clear group structure (block-diagonal for clusters, block-oﬀ-diagonal for classes of multipartite graphs, etc.). The goal is to determine the community prototype graph that best ap-

proximates the graph at study, where the goodness of the approximation is expressed by the distance between the corresponding matrices. In this way the original problem of ﬁnding graph subsets becomes an optimization problem. Long et al. called this procedure Community Learning by Graph Approximation (CLGA). Sometimes the minimization of the matrix distance can be turned into the maximization of the trace of a matrix. Measures like cut size or ratio cut can be also formulated as the trace of matrices (see for instance Eq. 18). In fact, CLGA includes traditional graph partitioning as a special case (Section IV.A). Long et al. designed three algorithms for CLGA: two of them seek for divisions of the graph into overlapping or non-overlapping groups, respectively; in the third one an additional constraint is introduced to produce groups of comparable size. The complexity of these algorithms is O(tn2k), where t is the number of iterations until the optimization converges and k the number of groups. The latter has to be given as an input, which is a serious limit of CLGA.

A fast algorithm by Wu and Huberman identiﬁes communities based on the properties of resistor networks (Wu and Huberman, 2004). It is essentially a method for partitioning graphs in two parts, similar to spectral bisection, although partitions in an arbitrary number of communities can be obtained by iterative applications. The graph is transformed into a resistor network where each edge has unit resistance. A unit potential diﬀerence is set between two randomly chosen vertices. The idea is that, if there is a clear division in two communities of the graph, there will be a visible gap between voltage values for vertices at the borders between the clusters. The voltages are calculated by solving Kirchoﬀ’s equations: an exact solution would be too time consuming, but it is possible to ﬁnd a reasonably good approximation in a linear time for a sparse graph with a clear community structure, so the more time consuming part of the algorithm is the sorting of the voltage values, which takes time O(nlog n). Any possible vertex pair can be chosen to set the initial potential diﬀerence, so the procedure should be repeated for all possible vertex pairs. The authors showed that this is not necessary, and that a limited number of sampling pairs is suﬃcient to get good results, so the algorithm scales as O(nlog n) and is very fast. An interesting feature of the method is that it can quickly ﬁnd the natural community of any vertex, without determining the complete partition of the graph. For that, one uses the vertex as source voltage and places the sink

- at an arbitrary vertex. The same feature is present in an older algorithm by Flake et al. (Flake et al., 2002), where one uses max-ﬂow instead of current ﬂow (Section IV.A). An algorithm by Orponen and Schaeﬀer (Orponen and Schaeﬀer, 2005) is based on the same principle, but it does not need the speciﬁcation of target sources as it is based on diﬀusion in an unbounded medium. The limit of such methods is the fact that one has to give as input the number of clusters, which is usually not known beforehand.


Ohkubo and Tanaka (Ohkubo and Tanaka, 2006) pointed out that, since communities are rather compact structures, they should have a small volume, where the volume of a community is deﬁned as the ratio of the number of vertices by the internal edge density of the community. Ohkubo and Tanaka assumed that the sum Vtotal of the volumes of the communities of a partition is a reliable index of the goodness of the partition. So, the most relevant partition is the one minimizing Vtotal. The optimization is carried out with simulated annealing.

Zarei and Samani (Zarei and Samani, 2009) remarked that there is a symmetry between community structure and anti-community (multipartite) structure, when one considers a graph and its complement, whose edges are the missing edges of the original graph. In fact, if a graph has a well identiﬁed communities, the same groups of vertices would be strong anti-communities in the complement graph, i. e. they should have a few intracluster edges and many inter-cluster edges. Based on this remark, the communities of a graph can be identiﬁed by looking for anticommunities in the complement graph, which can sometimes be easier. Zarei and Samani devised a spectral method using matrices of the complement graph. The results of this technique appear good as compared to other spectral methods on artiﬁcial graphs generated with the planted -partition model (Condon and Karp, 2001), as well as on Zachary’s karate club (Zachary, 1977), Lusseau’s dolphins’ network (Lusseau, 2003) and a network of protein-protein interactions. However, the authors have used very small graphs for testing. Communities make sense on sparse graphs, but the complements of large sparse graphs would not be sparse, but very dense, and their community (multipartite) structure basically invisible.

Gudkov and Montealegre detected communities by means of dynamical simplex evolution (Gudkov et al., 2008). Graph vertices are represented as points in an (n − 1)-dimensional space. Each point initially sits on the n vertices of a simplex, and then moves in space due to forces exerted by the other points. If vertices are neighbors, the mutual force acting on their representative points is attractive, otherwise it is repulsive. If the graph has a clear community structure, the corresponding spatial clusters repel each other because of the few connections between them (repulsion dominates over attraction). If communities are more mixed with each other, clusters are not well separated and they could be mistakenly aggregated in larger structures. To avoid that, Gudkov and Montealegre deﬁned clusters as groups of points such that the distance between each pair of points does not exceed a given threshold, which can be arbitrarily tuned, to reveal structures at diﬀerent resolutions (Section XII.A). The algorithm consists in solving ﬁrst-order diﬀerential equations, describing the dynamics of mass points moving in a viscous medium. The complexity of the procedure is O(n2). Diﬀerential equations are also at the basis of a recent method designed by Krawczyk and Kul akowski (Krawczyk, 2008; Krawczyk

and Kulakowski, 2007). Here the equations describe a dynamic process, in which the original graph topology evolves to a disconnected graph, whose components are the clusters of the original graph.

Despite the signiﬁcant improvements in computational complexity, it is still problematic to apply clustering algorithms to many large networks available today. Therefore Narasimhamurthy et al. (Narasimhamurthy et al.,

- 2008) proposed a two-step procedure: ﬁrst, the graph


- at study is decomposed in smaller pieces by a fast graph partitioning technique; then, a clustering method is applied to each of the smaller subgraphs obtained [Narasimhamurthy et al. used the Clique Percolation Method (Section XI.A)]. The initial decomposition of the graph is carried out through the multilevel method by Dhillon et al. (Dhillon et al., 2007). It is crucial to verify that the initial partitioning does not split the communities of the graph among the various subgraphs of the decomposition. This can be done by comparing, on artiﬁcial graphs, the ﬁnal clusters obtained with the two-step method with those detected by applying the chosen clustering technique to the entire graph.


###### XI. METHODS TO FIND OVERLAPPINGCOMMUNITIES

Most of the methods discussed in the previous sections aim at detecting standard partitions, i. e. partitions in which each vertex is assigned to a single community. However, in real graphs vertices are often shared between communities (Section II), and the issue of detecting overlapping communities has become quite popular in the last few years. We devote this section to the main techniques to detect overlapping communities.

A. Clique percolation

The most popular technique is the Clique Percolation Method (CPM) by Palla et al. (Palla et al., 2005). It is based on the concept that the internal edges of a community are likely to form cliques due to their high density. On the other hand, it is unlikely that intercommunity edges form cliques: this idea was already used in the divisive method of Radicchi et al. (Section V.B). Palla et al. use the term k-clique to indicate a complete graph with k vertices18. Notice that a k-clique is diﬀerent from the n-clique (see Section III.B.2) used in social science. If it were possible for a clique to move on a graph, in some way, it would probably get trapped inside its original community, as it could not cross the bottleneck formed by the intercommunity edges. Palla et al. introduced a number of concepts to implement this

- 18 In graph theory the k-clique by Palla et al. is simply called clique, or complete graph, with k vertices (Section A.1).


![image 68](Community Detection in Graphs_images/imageFile68.png)

FIG. 23 Clique Percolation Method. The example shows communities spanned by adjacent 4-cliques. Overlapping vertices are shown by the bigger dots. Reprinted ﬁgure with permission from Ref. (Palla et al., 2005). c 2005 by the Nature Publishing Group.

idea. Two k-cliques are adjacent if they share k − 1 vertices. The union of adjacent k-cliques is called k-clique chain. Two k-cliques are connected if they are part of a k-clique chain. Finally, a k-clique community is the largest connected subgraph obtained by the union of a k-clique and of all k-cliques which are connected to it. Examples of k-clique communities are shown in Fig. 23. One could say that a k-clique community is identiﬁed by making a k-clique “roll” over adjacent k-cliques, where rolling means rotating a k-clique about the k −1 vertices it shares with any adjacent k-clique. By construction, k-clique communities can share vertices, so they can be overlapping. There may be vertices belonging to nonadjacent k-cliques, which could be reached by diﬀerent paths and end up in diﬀerent clusters. Unfortunately, there are also vertices that cannot be reached by any kclique, like, e. g. vertices with degree one (“leaves”). In order to ﬁnd k-clique communities, one searches ﬁrst for maximal cliques. Then a clique-clique overlap matrix O is built (Everett and Borgatti, 1998), which is an nc × nc matrix, nc being the number of cliques; Oij is the number of vertices shared by cliques i and j. To ﬁnd k-cliques, one needs simply to keep the entries of O which are larger than or equal to k − 1, set the others to zero and ﬁnd the connected components of the resulting matrix. Detecting maximal cliques is known to require a running time that grows exponentially with the size of the graph. However, the authors found that, for the real networks they analyzed, the procedure is quite fast, due to the fairly limited number of cliques, and that (sparse) graphs with up to 105 vertices can be analyzed

in a reasonably short time. The actual scalability of the algorithm depends on many factors, and cannot be expressed in closed form. An interesting aspect of k-clique communities is that they allow to make a clear distinction between random graphs and graphs with community structure. This is a rather delicate issue: we have seen in Section VI.C that Newman-Girvan modularity can attain large values on random graphs. Der´enyi et al. (Der´enyi

- et al., 2005) have studied the percolation properties of k-cliques on random graphs, when the edge probability

- p varies. They found that the threshold pc(k) for the emergence of a giant k-clique community, i. e. a community occupying a macroscopic portion of the graph, is


pc(k) = [(k−1)n]−1/(k−1), n being the number of vertices of the graph, as usual. For k = 2, for which the k-cliques reduce to edges, one recovers the known expression for the emergence of a giant connected component in Erd¨sR´enyi graphs (Section A.3). This percolation transition is quite sharp: if the edge probability p < pc(k), k-clique communities are rather small; if p > pc(k) there is a giant component and many small communities. To assess the signiﬁcance of the clusters found with the CPM, one can compare the detected cover19 with the cover found on a null model graph, which is random but preserves the expected degree sequence of the original graph. The modularity of Newman and Girvan is based on the same null model (Section III.C.2). The null models of real graphs seem to display the same two scenarios found for Erd¨s-R´enyi graphs, characterized by the presence of very small k-clique communities, with or without a giant cluster. Therefore, covers with k-clique communities of large or appreciable size can hardly be due to random ﬂuctuations. Palla and coworkers (Adamcsek

- et al., 2006) have designed a software package implementing the CPM, called CFinder, which is freely available (www.cfinder.org).


The algorithm has been extended to the analysis of weighted, directed and bipartite graphs. For weighted graphs, in principle one can follow the standard procedure of thresholding the weights, and apply the method on the resulting graphs, treating them as unweighted. Farkas et al. (Farkas et al., 2007) proposed instead to threshold the weight of cliques, deﬁned as the geometric mean of the weights of all edges of the clique. The value of the threshold is chosen slightly above the critical value at which a giant k-clique community emerges, in order to get the richest possible variety of clusters. On directed graphs, Palla et al. deﬁned directed k-cliques as complete graphs with k vertices, such that there is an ordering among the vertices, and each edge goes from a vertex with higher order to one with lower order. The ordering is determined from the restricted outdegree of the vertex, expressing the fraction of outgoing edges point-

- 19 We remind that cover is the equivalent of partition for overlapping communities.


ing to the other vertices of the clique versus the total outdegree. The method has been extended to bipartite graphs by Lehmann et al. (Lehmann et al., 2008). In this case one uses bipartite cliques, or bicliques: a subgraph Ka,b is a biclique if each of a vertices of one class are connected with each of b vertices of the other class. Two cliques Ka,b are adjacent if they share a clique Ka−1,b−1, and a Ka,b clique community is the union of all Ka,b cliques that can be reached from each other through a path of adjacent Ka,b cliques. Finding all Nc bicliques of a graph is an NP-complete problem (Peeters, 2003), mostly because the number of bicliques tends to grow exponentially with the size of the graph. The algorithm designed by Lehmann et al. to ﬁnd biclique communities is similar to the original CPM, and has a total complexity of O(Nc2). On sparse graphs, Nc often grows linearly with the number of edges m, yielding a time complexity O(m2). Bicliques are also the main ingredients of BiTector, a recent algorithm to detect community structure in bipartite graphs (Du et al., 2008).

Kumpula et al. have developed a fast implementation of the CPM, called Sequential Clique Percolation algorithm (SCP) (Kumpula et al., 2008). It consists in detecting k-clique communities by sequentially inserting the edges of the graph at study, one by one, starting from an initial empty graph. Whenever a new edge is added, one checks whether new k-cliques are formed, by searching for (k − 2)-cliques in the subset of neighboring vertices of the endpoints of the inserted edge. The procedure requires to build a graph Γ∗, in which the vertices are (k−1)-cliques and edges are set between vertices corresponding to (k − 1)-cliques which are subgraphs of the same k-clique. At the end of the process, the connected components of Γ∗ correspond to the searched k-clique communities. The technique has a time complexity which is linear in the number of k-cliques of the graph, so it can vary a lot in practical applications. Nevertheless, it turns out to be much faster than the original implementation of the CPM. The big advantage of the SCP, however, consists of its implementation for weighted graphs. By inserting edges in decreasing order of weight, one recovers in a single run the community structure of the graph for all possible weight thresholds, by storing every cover detected after the addition of each edge. The standard CPM, instead, needs to be applied once for each threshold. If, instead of edge weight thresholding, one performs k-clique weight thresholding, as prescribed by Farkas et al. (Farkas et al., 2007), the SCP remains much faster than the CPM, if one applies a simple modiﬁcation to it, consisting in detecting and storing all k-cliques on the full graph, sorting them based on their weights, and ﬁnding the communities by sequentially adding the k-cliques in decreasing order of weight.

The CPM has the same limit as the algorithm of Radicchi et al. (Radicchi et al., 2004) (Section V.B): it assumes that the graph has a large number of cliques, so it may fail to give meaningful covers for graphs with just a few cliques, like technological networks and some social net-

works. On the other hand, if there are many cliques, the method may deliver trivial community structure, like a cover consisting of the whole graph as a single cluster.

- A more fundamental issue is the fact that the method does not look for actual communities, consistent with the shared notion of dense subgraphs, but for subgraphs “containing” many cliques, which may be quite diﬀerent objects than communities (for instance, they could be “chains” of cliques with low internal edge density). Another big problem is that on real networks there is a considerable fraction of vertices that are left out of the communities, like leaves. One could think of some postprocessing procedure to include them in the communities, but for that it is necessary to introduce a new criterion, outside the framework that inspired the method. Furthermore it is not clear a priori which value of k one has to choose to identify meaningful structures. Finally, the criterion to choose the threshold for weighted graphs and the deﬁnition of directed k-cliques are rather arbitrary.
- B. Other techniques


One of the ﬁrst methods to ﬁnd overlapping communities was designed by Baumes et al. (Baumes et al.,

- 2005b). A community is deﬁned as a subgraph which locally optimizes a given function W, typically some measure related to the edge density of the cluster20. Diﬀerent overlapping subsets may all be locally optimal, so vertices can be shared between communities. Detecting the cluster structure of a graph amounts to ﬁnding the set of all locally optimal clusters. Two eﬃcient heuristics are proposed, called Iterative Scan (IS) and Rank Removal (RaRe). IS performs a greedy optimization of the function W. One starts from a random seed vertex/edge and adds/deletes vertices one by one as long as W increases. Then another seed is randomly picked and the procedure is repeated. The algorithm stops when, by picking any seed, one recovers a previously identiﬁed cluster. RaRe consists in removing important vertices such to disconnect the graphs in small components representing the cores of the clusters. The importance of vertices is determined by their centrality scores (e.g. degree, betweenness centrality (Freeman, 1977)), PageRank (Brin and Page, 1998)). Vertices are removed until one fragments the graph into components of a given size. After that, the removed vertices are added again to the graph, and are associated to those clusters for which doing so increases the value of the function W. The complexity of IS and RaRe is O(n2) on sparse graphs. The best performance is achieved by using IS to reﬁne results obtained from RaRe. In a successive paper (Baumes et al., 2005a), Baumes et al. further improved such two-step procedure, in that the


- 20 Community deﬁnitions based on local optimization are adopted in other algorithms as well, like that by Lancichinetti et al. (Lancichinetti et al., 2009) (Section XII.A).


removed vertices in RaRe are reinserted in decreasing order of their centrality scores, and the optimization of W in IS is only extended to neighboring vertices of the running cluster. The new recipe maintains time complexity O(n2), but on sparse graphs it requires a time lower by an order of magnitude than the old one, while the quality of the detected clustering is comparable.

A diﬀerent method, combining spectral mapping, fuzzy clustering and the optimization of a quality function, has been presented by Zhang et al. (Zhang et al., 2007). The membership of vertex i in cluster k is expressed by uik, which is a number between 0 and 1. The sum of the uik over all communities k of a cover is 1, for every vertex. This normalization is suggested by the fact that the entry uik can be thought of as the probability that i belongs to community k, so the sum of the uik represents the probability that the vertex belongs to any community of the cover, which is necessarily 1. If there were no overlaps, uik = δk

ik, where ki represents the unique community of vertex i. The algorithm consists of three phases: 1) embedding vertices in Euclidean space; 2) grouping the corresponding vertex points in a given number nc of clusters; 3) maximizing a modularity function over the set of covers found in step 2), corresponding to diﬀerent values of nc. This scheme has been used in other techniques as well, like in the algorithm of Donetti and Mun˜oz (Donetti and Mun˜oz, 2004) (Section VII). The ﬁrst step builds upon a spectral technique introduced by White and Smyth (White and Smyth, 2005), that we have discussed in Section VI.A.4. Graph vertices are embedded in a d-dimensional Euclidean space by using the top d eigenvectors of the right stochastic matrix W (Section A.2), derived from the adjacency matrix A by dividing each element by the sum of the elements of the same row. The spatial coordinates of vertex i are the i-th components of the eigenvectors. In the second step, the vertex points are associated to nc clusters by using fuzzy k-means clustering (Bezdek, 1981; Dunn, 1974) (Section IV.C). The number of clusters nc varies from 2 to a maximum K, so one obtains K − 1 covers. The best cover is the one that yields the largest value of the modularity Qzhov, deﬁned as

nc

Qzhov =

c=1

W¯c W −

S¯c 2W

2

, (71)

where

and

uic + ujc 2

W¯c =

wij, (72)

i,j∈Vc

uic + (1 − ujc) 2

S¯c = W¯c +

wij. (73)

i∈Vc,j∈V \Vc

The sets Vc and V include the vertices of module c and of the whole network, respectively. Eq. 71 is an extension of the weighted modularity in Eq. 36, obtained by weighing

the contribution of the edges’ weights to the sums in Wc and Sc by the (average) membership coeﬃcients of the vertices of the edge. The determination of the eigenvectors is the most computationally expensive part of the method, so the time complexity is the same as that of the algorithm by White and Smyth (see Section VI.A.4), i. e. O(K2n+Km), which is essentially linear in n if the graph is sparse and K n.

Nepusz et al. proposed a diﬀerent approach based on vertex similarity (Nepusz et al., 2008). One starts from the membership matrix U, deﬁned as in the previous method by Zhang et al. From U a matrix S is built, where sij = nk=1c uikujk, expressing the similarity between vertices (nc is the number of clusters). If one assumes to have information about the actual vertex similarity, corresponding to the matrix S˜, the best cover is obtained by choosing U such that S approximates as closely as possible S˜. This amounts to minimize the function

n

DG(U) =

i=1

n

wij(˜sij − sij)2, (74)

j=1

where the wij weigh the importance of the approximation for each entry of the similarity matrices. In the absence of any information on the community structure of the graph, one sets wij = 1, ∀i,j (equal weights) and S˜ equal to the adjacency matrix A, by implicitly assuming that vertices are similar if they are neighbors, dissimilar otherwise. On weighted graphs, one can set the wij equal to the edge weights. Minimizing DG(U) is a nonlinear constrained optimization problem, that can be solved with a gradient-based iterative optimization method, like simulated annealing. The optimization procedure adopted by Nepusz et al., for a ﬁxed number of clusters nc, has a time complexity O(n2nch), where h is the number of iterations leading to convergence, so the method can only be applied to fairly small graphs. If nc is unknown, as it usually happens, the best cover is the one corresponding to the largest value of the modularity

- 1

- 2m ij


Q =

kikj 2m

Aij −

sij. (75)

Eq. 75 is very similar to the expression of NewmanGirvan modularity (Eq. 13): the diﬀerence is that the Kronecker’s δ is replaced by the vertices’ similarity, to account for overlapping communities. Once the best cover is identiﬁed, one can use the entries of the partition matrix U to evaluate the participation of each vertex in the nc clusters of the cover. Nepusz et al. deﬁned the bridgeness bi of a vertex i as

bi = 1 −

c

2

nc nc − 1

1 nc

uji −

. (76)

j=1

If i belongs to a single cluster, bi = 0. If, for a vertex i, uik = 1/nc, ∀k, bi = 1 and i is a perfect bridge, as

it lies exactly between all clusters. However, a vertex with low bi may be simply an outlier, not belonging to any cluster. Since real bridges are usually rather central vertices, one can identify them by checking for large values of the centrality-corrected bridgeness, obtained by multiplying the bridgeness of Eq. 76 by the centrality of the vertex (expressed by, e.g., degree, betweenness (Freeman, 1977), etc.). A variant of the algorithm by Nepusz et al. can be downloaded from http://www.cs.rhul.ac.uk/home/tamas/assets/file s/fuzzyclust-static.tar.gz.

In real networks it is often easier to discriminate between intercluster and intracluster edges than recognizing overlapping vertices. For instance, in social networks, even though many people may belong to more groups, their social ties within each group can be easily spotted. Besides, it may happen that communities are joined to each other through their overlapping vertices (Fig. 24), without intercluster edges. For these reasons, it has been recently suggested that deﬁning clusters as sets of edges, rather than vertices, may be a promising strategy to analyze graphs with overlapping communities (Ahn et al., 2009; Evans and Lambiotte, 2009). One has to focus on the line graph (Balakrishnan, 1997), i. e. the graph whose vertices are the edges of the original graph; vertices of the line graph are linked if the corresponding edges in the original graph are adjacent, i. e. if they share one of their endvertices. Partitioning the line graph means grouping the edges of the starting graph21. Evans and Lambiotte (Evans and Lambiotte, 2009) introduced a set of quality functions, similar to Newman-Girvan modularity (Eq. 13), expressing the stability of partitions against random walks taking place on the graph, following the work of Delvenne et al. (Delvenne et al., 2008) [Section VIII.B]. They considered a projection of the traditional random walk on the line graph, along with two other diﬀusion processes, where walkers move between adjacent edges (rather than between neighboring vertices). Evans and Lambiotte optimized the three corresponding modularity functions to look for partitions in two real networks, Zachary’s karate club (Zachary, 1977) (Section XV.A) and the network of word associations derived from the University of South Florida Free Association Norms (Nelson et al., 1998) (Section II). The optimization was carried out with the hierarchical technique by Blondel et al. (Blondel et al., 2008) and the multi-level algorithm by Noack and Rotta (Noack and Rotta, 2009). While the results for the word association network are reasonable, the test on the karate club yields partitions in more than two clusters. However, the modularities used by Evans et Lambiotte can be modiﬁed to include longer random walks (just like in Ref. (Delvenne et al.,

21 Ideally one wants to put together only the edges lying within clusters, and exclude the others. Therefore partitioning does not necessarily mean assigning each vertex of the line graph to a group, as standard clustering techniques would do.

FIG. 24 Communities as sets of edges. In the ﬁgure, the graph has a natural division in two triangles, with the central vertex shared between them. If communities are identiﬁed by their internal edges, detecting the triangles and their overlapping vertex becomes easier than by using methods that group vertices. Reprinted ﬁgure with permission from Ref. (Evans and Lambiotte, 2009). c 2009 by the American Physical Society.

2008)), and the length of the walk represents a resolution parameter that can be tuned to get better results. Ahn et al. (Ahn et al., 2009) proposed to group edges with an agglomerative hierarchical clustering technique, called hierarchical link clustering (Section IV.B). They use a similarity measure for a pair of (adjacent) edges that expresses the size of the overlap between the neighborhoods of the non-coincident endvertices, divided by the total number of (diﬀerent) neighbors of such endvertices. Groups of edges are merged pairwise in descending order of similarity, until all edges are together in the same cluster. The resulting dendrogram provides the most complete information on the community structure of the graph. However, as usual, most of this information is redundant and is an artefact of the procedure itself. So, Ahn et al. introduced a quality function to select the most meaningful partition(s), called partition density, which is essentially the average edge density within the clusters. The method is able to ﬁnd meaningful clusters in biological networks, like protein-protein and metabolic networks, as well as in a social network of mobile phone communications. It can also be extended to multipartite and weighted graphs.

The idea of grouping edges is surely interesting. However it is not a priori better than grouping vertices. In fact, the two situations are somewhat symmetric. Edges connecting vertices of diﬀerent clusters are “overlapping”, but they will be assigned just to one cluster (or else the clusters would be merged).

The possibility of having overlapping communities makes most standard clustering methods inadequate, and enforces the design of new ad hoc techniques, like the ones we have described so far. On the other hand, if it were possible to identify the overlapping vertices and “separate” them among the clusters they belong to, the

overlaps would be removed and one could then apply any of the traditional clustering methods to the resulting graph. This idea is at the basis of a recent method proposed by Gregory (Gregory, 2009). It is a threestages procedure: ﬁrst, one transforms the graph into a larger graph without overlapping vertices; second, a clustering technique is applied to the resulting graph; third, one maps the partition obtained into a cover by replacing the vertices with those of the original graph. The transformation step, called Peacock, is performed by identifying the vertices with highest split betweenness (Section V.A) and splitting them in multiple parts, connected by edges. This is done as long as the split betweenness of the vertices is suﬃciently high, which is determined by a parameter s. In this way, most vertices of the resulting graph are exactly the same one had initially, the others are multiple copies of the overlapping vertices of the initial graph. The overlaps of the ﬁnal cover are obtained by checking if copies of the same initial vertex end up in diﬀerent disjoint clusters. The complexity is dominated by the Peacock algorithm, if one computes the exact values of the split betweenness for the vertices, which requires a time O(n3) on a sparse graph22. Gregory proposed an approximate local computation, which scales as O(nlog n): in this way the total complexity of the method becomes competitive, if one chooses a fast algorithm for the identiﬁcation of the clusters. The goodness of the results depends on the speciﬁc method one uses to ﬁnd the clusters after the graph transformation. The software of the version of the method used by Gregory in his applications can be found at http://www.cs.bris.ac.uk/∼steve/networks/peaco ckpaper/. The idea of Gregory is interesting, as it allows to exploit traditional methods even in the presence of overlapping communities. The choice of the parameter s, which determines whether a vertex is overlapping or not, does not seem to aﬀect signiﬁcantly the results, as long as s is taken suﬃciently small.

###### XII. MULTIRESOLUTION METHODS AND CLUSTER HIERARCHY

The existence of a resolution limit for Newman-Girvan modularity (Section VI.C) implies that the straight optimization of quality functions yields a coarse description of the cluster structure of the graph, at a scale which has a priori nothing to do with the actual scale of the clusters. In the absence of information on the cluster sizes of the graph, a method should be able to explore all possible scales, to make sure that it will eventually identify the right communities. Multiresolution methods

22 The split betweenness needs to be recalculated after each vertex split, just as one does for the edge betweenness in the GirvanNewman algorithm (Girvan and Newman, 2002). Therefore both computations have the same complexity.

are based on this principle. However, many real graphs display hierarchical cluster structures, with clusters inside other clusters (Simon, 1962). In these cases, there are more levels of organization of vertices in clusters, and more relevant scales. In principle, clustering algorithms should be able to identify them. Multiresolution methods can do the trick, in principle, as they scan continuously the range of possible cluster scales. Recently other methods have been developed, where partitions are by construction hierarchically nested in each other. In this section we discuss both classes of techniques.

- A. Multiresolution methods


In general, multiresolution methods have a freely tunable parameter, that allows to set the characteristic size of the clusters to be detected. The general spin glass framework by Reichardt and Bornholdt ((Reichardt and Bornholdt, 2006a) and Section VI.B) is a typical example, where γ is the resolution parameter. The extension of the method to weighted graphs has been recently discussed (Heimo et al., 2008).

Pons has proposed a method (Pons, 2006) consisting of the optimization of multiscale quality functions, including the multiscale modularity

nc

QMα =

c=1

lc m − (1 − α)

α

dc 2m

2

, (77)

and two other additive quality functions, derived from the performance (Eq. 12) and a measure based on the similarity of vertex pairs. In Eq. 77 0 ≤ α ≤ 1 is the resolution parameter and the notation is otherwise the same as in Eq. 14. We see that, for α = 1/2, one recovers standard modularity. However, since multiplicative factors in QMα do not change the results of the optimization, we can divide QMα by α, recovering the same quality function as in Eq. 46, with γ = (1 − α)/α, up to an irrelevant multiplicative constant. To evaluate the relevance of the partitions, for any given multiscale quality function, Pons suggested that the length of the α-range [αmin(C),αmax(C)], for which a community C “lives” in the maximum modularity partition, is a good indicator of the stability of the community. He then deﬁned the relevance function of a community C at scale α as

αmax(C) − αmin(C) 2

Rα(C) =

2(αmax(C) − α)(α − αmin(C)) αmax(C) − αmin(C)

+

. (78)

The relevance R(α) of a partition P at scale α is the average of the relevances of the clusters of the partition, weighted by the cluster sizes. Peaks in α of R(α) reveal the most meaningful partitions.

Another interesting technique has been devised by Arenas et al. (Arenas et al., 2008b), and consists of a modiﬁcation of the original expression of modularity. The

karate

10

modules

r = 0

(I)

1

1 10 100 r - rasymp

FIG. 25 Analysis of Zachary’s karate club with the multiresolution method by Arenas et al. (Arenas et al., 2008b). The plot shows the number of clusters obtained in correspondence of the resolution parameter r. The longest plateau (I) indicates the most stable partition, which exactly matches the social ﬁssion observed by Zachary. The partition obtained with straight modularity optimization (r = 0) consists of four clusters and is much less stable with respect to (I), as suggested by the much shorter length of its plateau. Reprinted ﬁgure with permission from Ref. (Arenas et al., 2008b). c 2008 by IOP Publishing.

idea is to make vertices contribute as well to the computation of the edge density of the clusters, by adding a self-loop of strength r to each vertex. Arenas et al. remarked that the parameter r does not aﬀect the structural properties of the graph in most cases, which are usually determined by an adjacency matrix without diagonal elements. With the introduction of the vertex strength r, modularity reads

nc

Qr =

c=1

2Wc + Ncr 2W + nr −

Sc + Ncr 2W + nr

2

, (79)

for the general case of a weighted graph. The notation is the same as in Eq. 36, Nc is the number of vertices in cluster c. We see that now the relative importance of the two terms in each summand depends on r, which can take any value in ] − 2W/n,∞[. Arenas et al. made a sweep in the range of r, and determined for each r the maximum modularity with extremal optimization (Section VI.A.3) and tabu search23 (Glover, 1986). Meaningful cluster structures correspond to plateaus in the

23 Tabu search consists in moving single vertices from one community to another, chosen at random, or to new communities, starting from some initial partition. After a sweep over all vertices, the best move, i. e. the one producing the largest increase of modularity, is accepted and applied, yielding a new partition. The procedure is repeated until modularity does not increase further. To escape local optima, a list of recent accepted moves

plot of the number of clusters versus r (Fig. 25). The length of a plateau gives a measure of the stability of the partition against the variation of r. The procedure is able to disclose the community structure of a number of real benchmark graphs. As expected, the most relevant partitions can be found in intervals of r not including the value r = 0, which corresponds to the case of standard modularity (Fig. 25). A drawback of the method is that it is very slow, as one has to compute the modularity maximum for many values of r in order to discriminate between relevant and irrelevant partitions. If the modularity maximum is computed with precise methods like simulated annealing and/or extremal optimization,

- as in Ref. (Arenas et al., 2008b), only graphs with a few hundred vertices can be analyzed on a single processor. On the other hand the algorithm can be trivially parallelized by running the optimization for diﬀerent values of r on diﬀerent processors. This is a common feature of all multiresolution methods discussed in this Section. In spite of the diﬀerent formal expressions of modularity, the methods by Arenas et al. and Reichardt and Bornholdt are somewhat related to each other and yield similar results (Kumpula et al., 2007a) on Zachary’s karate club (Zachary, 1977) (Section XV.A), synthetic graphs ´ la Ravasz-Barab´si (Ravasz and Barab´si, 2003) and on a model graph with the properties of real weighted social networks24. In fact, their modularities can be both recovered from the continuous-time version of the stability of clustering under random walk, introduced by Delvenne et al. (Delvenne et al., 2008) (Section VIII.B).

Lancichinetti et al. have designed a multiresolution method which is capable of detecting both the hierarchical structure of graphs and overlapping communities (Lancichinetti et al., 2009). It is based on the optimization of a ﬁtness function, which estimates the strength of a cluster and entails a resolution parameter α. The function could in principle be arbitrary, in their applications the authors chose a simple ansatz based on the tradeoﬀ between the internal and the total degree of the cluster. The optimization procedure starts from a cluster with a single vertex, arbitrarily selected. Given a cluster core, one keeps adding and removing neighboring vertices of the cluster as long as its ﬁtness increases. The ﬁtness is recalculated after each addition/removal of a vertex. At some point one reaches a local maximum and the cluster is “closed”. Then, another vertex is chosen

- at random, among those not yet assigned to a cluster, a new cluster is built, and so on, until all vertices have


is kept and updated, so that those moves are not accepted in the next update of the conﬁguration (tabu list). The cost of the procedure is about the same of other stochastic optimization techniques like, e. g., simulated annealing.

- 24 Related does not mean equivalent, though. Arenas et al. have shown that their method is better than that by Reichardt and Bornholdt when the graph at hand includes communities of different sizes (Arenas et al., 2008b).


been assigned to clusters. During the buildup of a cluster, vertices already assigned to other clusters may be included, i. e. communities may overlap. The computational complexity of the algorithm, estimated on sparse Erd¨s-R´enyi random graphs, is O(nβ), with β ∼ 2 for small values of the resolution parameter α, and β ∼ 1 if α is large. For a complete analysis, the worst-case computational complexity is O(n2 log n), where the factor log n comes from the minimum number of diﬀerent α-values which are needed to resolve the actual community structure of the graph. Relevant partitions are revealed by pronounced spikes in the histogram of the ﬁtness values of covers obtained for diﬀerent α-values, where the ﬁtness of a cover is deﬁned as the average ﬁtness of its clusters.

A technique based on the Potts model, similar to that of Reichardt and Bornholdt (Reichardt and Bornholdt, 2006a), has been suggested by Ronhovde and Nussinov (Ronhovde and Nussinov, 2008). The energy of their spin model is

1 2 i=j

H({σ}) = −

[Aij − γ(1 − Aij)]δ(σi,σj). (80)

The big diﬀerence with Eq. 46 is the absence of a null model term. The model considers pairs of vertices in the same community: edges between vertices are energetically rewarded, whereas missing edges are penalized. The parameter γ ﬁxes the tradeoﬀ between the two contributions. The energy is minimized by sequentially shifting single vertices/spins to the communities which yield the largest decrease of the system’s energy, until convergence. If, for each vertex, one just examines the communities of its neighbors, the energy is minimized in a time O(mβ), where β turns out to be slightly above 1 in most applications, allowing for the analysis of large graphs. This essentially eliminates the problem of limited resolution, as the criterion to decide about the merger or the split of clusters only depends on local parameters. Still, for the detection of possible hierarchical levels tuning γ is mandatory. In a successive paper (Ronhovde and Nussinov, 2009), the authors have introduced a new stability criterion for the partitions, consisting of the computation of the similarity of partitions obtained for the same γ and diﬀerent initial conditions. The idea is that, if a partition is robust in a given range of γ-values, most replicas delivered by the algorithm will be very similar. On the other hand, if one explores a region of resolutions in between two strong partitions, the algorithm will deliver the one or the other partition and the individual replicas will be, on average, not so similar to each other. So, by plotting the similarity as a function of the resolution parameter γ, stable communities are revealed by peaks. Ronhovde and Nussinov adopted similarity measures borrowed from information theory (Section XV.B). Their criterion of stability can be adopted to determine the relevance of partitions obtained with any multiresolution algorithm.

A general problem of multiresolution methods is how to assess the stability of partitions for large graphs. The

rapidly increasing number of partitions, obtained by minimal shifts of vertices between clusters, introduces a large amount of noise, that blurs signatures of stable partitions like plateaus, spikes, etc. that one can observe in small systems. In this respect, it seems far more reliable focusing on correlations between partitions (like the average similarity used by Ronhovde and Nussinov (Ronhovde and Nussinov, 2008; Ronhovde and Nussinov, 2009)) than on properties of the individual partitions (like the measures of occurrence used by Arenas et al. (Arenas et al.,

- 2008b) and by Lancichinetti et al. (Lancichinetti et al.,
- 2009)).


- B. Hierarchical methods


The natural procedure to detect the hierarchical structure of a graph is hierarchical clustering, that we have discussed in Section IV.B. There we have emphasized the main weakness of the procedure, which consists of the necessity to introduce a criterion to identify relevant partitions (hierarchical levels) out of the full dendrogram produced by the given algorithm. Furthermore, there is no guarantee that the results indeed reﬂect the actual hierarchical structure of the graph, and that they are not mere artefacts of the algorithm itself. Scholars have just started to deal with these problems.

Sales-Pardo et al. have proposed a top-down approach (Sales-Pardo et al., 2007). Their method consists of two steps: 1) measuring the similarity between vertices; 2) deriving the hierarchical structure of the graph from the similarity matrix. The similarity measure, named node aﬃnity, is based on Newman-Girvan modularity. Basically the aﬃnity between two vertices is the frequency with which they coexist in the same community in partitions corresponding to local optima of modularity. The latter are conﬁgurations for which modularity is stable, i. e. it cannot increase if one shifts one vertex from one cluster to another or by merging or splitting clusters. The set of these partitions is called Pmax. Before proceeding with the next step, one veriﬁes whether the graph has a signiﬁcant community structure or not. This is done by calculating the z-score (Eq. 51) for the average modularity of the partitions in Pmax with respect to the average modularity of partitions with local modularity optima of the equivalent ensemble of null model graphs, obtained as usual by randomly rewiring the edges of the original graph under the condition that the expected degree sequence is the same as the degree sequence of the graph. Large z-scores indicate meaningful cluster structure: Sales-Pardo et al. used a threshold corresponding to the 1% signiﬁcance level25. If the graph

has a relevant cluster structure, one proceeds with the second step, which consists in putting the aﬃnity matrix in a form as close as possible to block-diagonal, by minimizing a cost function expressing the average distance of connected vertices from the diagonal. The blocks correspond to the communities and the recovered partition represents the uppermost organization level. To determine lower levels, one iterates the procedure for each subgraph identiﬁed at the previous level, which is treated as an independent graph. The procedure stops when all blocks found do not have a relevant cluster structure, i. e. their z-scores are lower than the threshold. The partitions delivered by the method are hierarchical by construction, as communities at each level are nested within communities at higher levels. However, the method may ﬁnd no relevant partition (no community structure), a single partition (community structure but no hierarchy) or more (hierarchy) and in this respect it is better than most existing methods. The algorithm is not fast, as both the search of local optima for modularity and the rearrangement of the similarity matrix are performed with simulated annealing26, but delivers good results for computer generated networks, and meaningful partitions for some real networks, like the world airport network (Barrat et al., 2004), an email exchange network of a Catalan university (Guimer` et al., 2003), a network of electronic circuits (Itzkovitz et al., 2005) and metabolic networks of E. coli (Guimer` et al., 2007).

Clauset et al. (Clauset et al., 2007; Clauset et al., 2008) described the hierarchical organization of a graph by introducing a class of hierarchical random graphs. A hierarchical random graph is deﬁned by a dendrogram D, which is the natural representation of the hierarchy, and by a set of probabilities {pr} associated to the n−1 internal nodes of the dendrogram. An ancestor of a vertex i is any internal node of the dendrogram that is encountered by starting from the “leaf” vertex i and going all the way up to the top of the dendrogram. The probability that vertices i and j are linked to each other is given by the probability pr of the lowest common ancestor of i and j. Clauset et al. searched for the model (D,{pr}) that best ﬁts the observed graph topology, by using Bayesian inference (Section IX.A). The probability that the model ﬁts the graph is proportional to the likelihood

L(D,{pr}) =

r∈D

rRr−Er. (81)

pE

r (1 − pr)L

r

Here, Er is the number of edges connecting vertices whose lowest common ancestor is r, Lr and Rr are the numbers of graph vertices in the left and right subtrees descending from the dendrogram node r, and the product runs

- 25 We remind that the signiﬁcance of the z-score has to be computed with respect to the actual distribution of the maximum modularity for the null model graphs, as the latter is not Gaussian (Section VI.C).


26 The reordering of the matrix is by far the most time-consuming part of the method. The situation improves if one adopts faster optimization strategies than simulated annealing, at the cost of less accurate results.

- a

- b


- e

- f


c d

1/4

1/3

1/9

1

1

1

1

1

1

1

a b c d e f

a b c d e f

FIG. 26 Hierarchical random graphs by Clauset et al. (Clauset et al., 2008). The picture shows two possible dendrograms for the simple graph on the top. The linking probabilities on the internal nodes of the dendrograms yield the best ﬁt of the model graphs to the graph at study. Reprinted ﬁgure with permission from Ref. (Clauset et al., 2008). c 2008 by the Nature Publishing Group.

growth

contraction

t t+1

t t+1

merging

splitting

t t+1

t t+1

birth death

t t+1 t t+1

FIG. 27 Possible scenarios in the evolution of communities. Reprinted ﬁgure with permission from Ref. (Palla et al., 2007). c 2007 by the Nature Publishing Group.

over all internal dendrogram nodes. For a given dendrogram D, the maximum likelihood L(D) corresponds to the set of probabilities {p¯r}, where p¯r equals the actual density of edges Er/(LrRr) between the two subtrees of r (Fig. 26). One can deﬁne the statistical ensemble of hierarchical random graphs describing a given graph G, by assigning to each model graph (D,{p¯r}) a probability proportional to the maximum likelihood L(D). The ensemble can be sampled by a Markov chain Monte Carlo method (Newman and Barkema, 1999). The procedure suggested by Clauset et al. seems to converge to equilibrium roughly in a time O(n2), although the actual complexity may be much higher. Still, the authors were able to investigate graphs with a few thousand vertices. From suﬃciently large sets of model conﬁgurations sampled at equilibrium, one can compute average properties of the model, e. g. degree distributions, clustering coeﬃcients. etc., and compare them with the corresponding properties of the original graph. Tests on real graphs reveal that the model is indeed capable to describe closely the graph properties. Furthermore, the model enables one to predict missing connections between vertices of the original graph. This is a very important problem (Liben-Nowell and Kleinberg, 2003): edges of real graphs are the result of observations/experiments, that may fail to discover some relationships between the units of the system. From the ensemble of the hierarchical random graphs one can derive the average linking probability between all pairs of graph vertices. By ranking the probabilities corresponding to vertex pairs which are disconnected in the original graph, one may expect that the pairs with highest probabilities are likely to be connected in the system, even if such connections are not observed. Clauset et al. pointed out that their method does not deliver a sharp hierarchical organization for a given graph, but a class of possible organizations, with well-deﬁned probabilities. It is certainly reasonable to assume that many structures

are compatible with a given graph topology. In the case of community structure, it is not clear which information one can extract from averaging over the ensemble of hierarchical random graphs. Moreover, since the hierarchical structure is represented by a dendrogram, it is impossible to rank partitions according to their relevance. In fact, the work by Clauset et al. questions the concept of “relevant partition”, and opens a debate in the scientiﬁc community about the meaning itself of graph clustering. The software of the method can be found at http://www.santafe.edu/∼aaronc/hierarchy/.

###### XIII. DETECTION OF DYNAMIC COMMUNITIES

The analysis of dynamic communities is still in its infancy. Studies in this direction have been mostly hindered by the fact that the problem of graph clustering is already controversial on single graph realizations, so it is understandable that most eﬀorts still concentrate on the “static” version of the problem. Another diﬃculty is represented by the dearth of timestamped data on real graphs. Recently, several data sets have become available, enabling to monitor the evolution in time of real systems (Kumar et al., 2003, 2006; Leskovec et al., 2008, 2005). So it has become possible to investigate how communities form, evolve and die. The main phenomena occurring in the lifetime of a community are (Fig. 27): birth, growth, contraction, merger with other communities, split, death.

The ﬁrst study was carried out by Hopcroft et al. (Hopcroft et al., 2004), who analyzed several snapshots of the citation graph induced by the NEC CiteSeer Database (Giles et al., 1998). The snapshots cover the period from 1990 to 2001. Communities are detected by means of (agglomerative) hierarchical clustering (Section IV.B), where the similarity between vertices is the

cosine similarity of the vectors describing the corresponding papers, a well known measure used in information retrieval (Baeza-Yates and Ribeiro-Neto, 1999). In each snapshot Hopcroft et al. identiﬁed the natural communities, deﬁned as those communities of the hierarchical tree that are only slightly aﬀected by minor perturbations of the graph, where the perturbation consists in removing a small fraction of the vertices (and their edges). Such natural communities are conceptually similar to the stable communities we will see in Section XIV. Hopcroft et al. found the best matching natural communities across diﬀerent snapshots, and in this way they could follow the history of communities. In particular they could see the emergence of new communities, corresponding to new research topics. The main drawback of the method comes from the use of hierarchical clustering, which is unable to sort out meaningful communities out of the hierarchical tree, which includes many diﬀerent partitions of the graph.

More recently, Palla et al. performed a systematic analysis of dynamic communities (Palla et al., 2007). They studied two social systems: 1) a graph of phone calls between customers of a mobile phone company in a year’s time; 2) a collaboration network between scientists, describing the coauthorship of papers in condensed matter physics from the electronic e-print archive (condmat) maintained by Cornell University Library, spanning a period of 142 months. The ﬁrst problem is identifying the image of a community C(t+1) at time t+1 among the communities of the graph at time t. A simple criterion, used in other works, is to measure the relative overlap (Eq. 97) of C(t + 1) with all communities at time t, and pick the community which has the largest overlap with C(t+1). This is intuitive, but in many cases it may miss the actual evolution of the community. For instance, if C(t) at time t + 1 grows considerably and overlaps with another community B(t + 1) (which at the previous time step was disjoint from C(t)), the relative overlap between C(t+1) and B(t) may be larger than the relative overlap between C(t + 1) and C(t). It is not clear whether there is a general prescription to avoid this problem. Palla et al. solved it by exploiting the features of the Clique Percolation Method (CPM) (Section XI.A), that they used to detect communities. The idea is to analyze the graph G(t,t + 1), obtained by merging the two snapshots G(t) and G(t+1) of the evolving graph, at times t and t+1 (i. e., by putting together all their vertices and edges). Any CPM community of G(t) and G(t + 1) does not get lost,

- as it is included within one of the CPM communities of G(t,t + 1). For each CPM community Vk of G(t,t + 1),


one ﬁnds the CPM communities {Ckt} and {Ckt+1} (of G(t) and G(t+1), respectively) which are contained in Vk. The

image of any community in {Ckt+1} at time t is the community of {Ckt} that has the largest relative overlap with it.

The age τ of a community is the time since its birth. It turns out that the age of a community is positively correlated with its size s(τ), i. e. that older communities

are also larger (on average). The time evolution of a community C can be described by means of the relative overlap C(t) between states of the community separated by a time t:

C(t) = |C(t0) C(t0 + t)| |C(t0) C(t0 + t)|

. (82)

One ﬁnds that, in both data sets, C(t) decays faster for larger communities, so the composition of large communities is rather variable in time, whether small communities are essentially static. Another important question is whether it is possible to predict the evolution of communities from information on their structure or on their vertices. In Fig. 28a the probability pl that a vertex will leave the community in the next step of the evolution is plotted as a function of the relative external strength of the vertex, indicating how much of the vertex strength lies on edges connecting it to vertices outside its community. The plot indicates that there is a clear positive correlation: vertices which are only loosely connected to vertices of their community have a higher chance (on average) to leave the community than vertices which are more “committed” towards the other community members. The same principle holds at the community level too. Fig. 28b shows that the probability pd that a community will disintegrate in the next time step is positively correlated with the relative external strength of the community. Finally, Palla et al. have found that the probability for two communities to merge increases with the community sizes much more than what one expects from the size distribution, which is consistent with the faster dynamics observed for large communities. Palla et al. analyzed two diﬀerent real systems, a network of mobile phone communications and a coauthorship network, to be able to infer general properties of community evolution. However, communities were only found with the CPM, so their results need to be cross-checked by employing other clustering techniques.

Asur et al. (Asur et al., 2007) explored the dynamic relationship between vertices and communities. Communities were found with the MCL method by Van Dongen (Dongen, 2000a) (Section VIII.B), by analyzing the graph at diﬀerent timestamps. Asur et al. distinguished events involving communities and events involving the vertices. Events involving communities are Continue (the community keeps most of its vertices in consecutive time steps), κ-Merge (two clusters merge into another), κ-Split (two clusters split in two parts), Form (no pair of vertices of the cluster at time t + 1 were in the same cluster at time t) and Dissolve (opposite of Form). Events involving vertices are Appear (if a vertex joins the graph for the ﬁrst time), Disappear (if a vertex of the graph at time t is no longer there at time t + 1), Join (if a vertex of a cluster at time t + 1 was not in that cluster at time t) and Leave (if a vertex which was in a cluster at time t is not in that cluster at time t + 1). Based on such events, four measures are deﬁned in order to catch the behavioral tendencies of vertices contributing to the evolution

- a)
- b)


0.08 0.07 0.06 0.05 0.04 0.03 0.02 0.01

16

14

12

10 8

τn

6 4 2 0

pl

wout/(win+wout)

0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1

co−authorship

phone−call

0

0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1

wout /(win+wout)

0.2

35

30

25

0.15

20

τ∗

15

10

pd

0.1

5

Wout/(Win+Wout)

0

0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1

0.05

co−authorship phone−call

0

0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1

Wout /(Win +Wout)

FIG. 28 Relation between structural features and evolution of a community. a) Relation between the probability that a vertex will abandon the community in the next time step and its relative external strength. b) Relation between the probability of disintegration of a community in the next time step and its relative external strength. Reprinted ﬁgure with permission from Ref. (Palla et al., 2007). c 2007 by the Nature Publishing Group.

of the graph: the stability index (measuring the tendency of a vertex to interact with the same vertices over time), the sociability index (measuring the number of diﬀerent interactions of a vertex, basically the number of Join and Leave events), the popularity index (measuring the number of vertices attracted by a cluster in a given time interval) and the inﬂuence index (measuring the inﬂuence a vertex has on the others, which is computed from the number of vertices that leave or join a cluster together with the vertex). Applications on a coauthorship network of computer scientists and on a network of subjects for clinical trials show that the behavioral measures above enable one to make reliable predictions about the time evolution of such graphs (including, e. g., the inference of missing links (Liben-Nowell and Kleinberg, 2003)).

Dynamic communities can be as well detected with methods of information compression, such as some of those we have seen in Section IX.B. Sun et al. (Sun

et al., 2007) applied the Minimum Description Length (MDL) principle (Gru¨nwald et al., 2005; Rissanen, 1978) to ﬁnd the minimum encoding cost for the description of a time sequence of graphs and their partitions in communities. The method is quite similar to that successively developed by Rosvall and Bergstrom (Rosvall and Bergstrom, 2007), which is however deﬁned only for static graphs (Section IX.B). Here one considers bipartite graphs evolving in time. The time sequence of graphs can be separated in segments, each containing some number of consecutive snapshots of the system. The graphs of each segment are supposed to have the same modular structure (i. e. they represent the same phase in the history of the system), so they are characterized by the same partition of the two vertex classes. For each graph segment it is possible to deﬁne an encoding cost, which combines the encoding cost of the partition of the graphs of the segment with the entropy of compression of the segment in the subgraph segments induced by the partition. The total encoding cost C of the graph series is given by the sum of the encoding costs of its segments. Minimizing C enables one to ﬁnd not only the most modular partition for each graph segment (high modularity27 corresponds to low encoding costs for a partition), but also the most compact subdivision of the snapshots into segments, such that graphs in the same segment are strongly correlated with each other. The latter feature allows to identify change points in the time history of the system, i. e. short periods in which the dynamics produces big changes in the graph structure (corresponding to, e.g., extreme events). The minimization of C is NP-hard, so the authors propose an approximation method called GraphScope, which consists of two steps: ﬁrst, one looks for the best partition of each graph segment; second, one looks for the best division in segments. In both cases the “best” result corresponds to the minimal encoding cost. The best partition within a graph segment is found by local search. GraphScope has the big advantage not to require any input, like the number and sizes of the clusters. It is also suitable to operate in a streaming environment, in which new graph conﬁgurations are added in time, following the evolution of the system: the computational complexity required to process a snapshot (on average) is stable over time. Tests on real evolving data sets show that GraphScope is able to ﬁnd meaningful communities and change points.

Since keeping track of communities in diﬀerent time steps is not a trivial problem, as we have seen above, it is perhaps easier to adopt a vertex-centric perspective, in which one monitors the community of a given vertex at diﬀerent times. For any method, given a vertex i and a time t, the community to which i belongs at time t is

27 We stress that here by modularity we mean the feature of a graph having community structure, not the modularity of Newman and Girvan.

well deﬁned. Fenn et al. (Fenn et al., 2009) used the multiresolution method by Reichardt et al. (Reichardt and Bornholdt, 2006a) (Section VI.B) and investigated a fully connected graph with time-dependent weights, representing the correlations of time series of hourly exchange rate returns. The resolution parameter γ is ﬁxed to the value that occurs in most stability plateaus of the system at diﬀerent time steps. Motivated by the work of Guimer` and Amaral (Guimer` and Amaral, 2005) (Section XVI), Fenn et al. identify the role of individual vertices in their community through the pair (zin,zb), where zin is the z-score of the internal strength (weighted degree, Section A.1), deﬁned in Eq. 98, and zb the z-score of the site betweenness, deﬁned by replacing the internal degree with the site betweenness of Freeman (Freeman, 1977) in Eq. 98. We remind that the site betweenness is a measure of the number of shortest paths running through a vertex. The variable zb expresses the importance of a vertex in processes of information diﬀusion with respect to the other members of its community. Another important issue regards the persistence of communities in time, i. e. how stable they are during the evolution. As a measure of persistence, Fenn et al. introduced a vertex-centric version of the relative overlap of Eq. 82

ati(τ) = |Ci(t) Ci(t + τ)| |Ci(t) Ci(t + τ)|

, (83)

where i is the vertex and Ci(t), Ci(t+τ) the communities of i at times t, t + τ, respectively. The decay of ati(τ) depends on the type of vertex. In particular, if the vertex is strongly connected to its community (zin large), ati(τ) decays quite slowly, meaning that it tends to stay attached to a stable core of vertices.

The methods described above are basically two-stage approaches, in which clusters are detected at each timestamp of the graph evolution, independently of the results

- at diﬀerent times, and relationships between partitions


- at diﬀerent times are inferred successively. However, this often produces signiﬁcant variations between partitions close in time, especially when, as it usually happens, the datasets are noisy. In this case one would be forced to introduce ad hoc hypotheses on the graph evolution to justify the variability of the modular structure, whereas such variability is mostly an artefact of the approach. It would be desirable instead to have a uniﬁed framework, in which clusters are deduced both from the current structure of the graph and from the knowledge of the cluster structure at previous times. This is the principle of evolutionary clustering, a framework introduced by Chakrabarti et al. (Chakrabarti et al., 2006) and suc-


cessively adopted and reﬁned by other authors. Let Ct be the partition of the graph at time t. The snapshot quality of Ct measures the goodness of the partition with respect to the graph structure at time t. The history cost is a measure of the distance/dissimilarity of Ct with respect to the partition Ct−1 at the previous time step. The overall quality of Ct is given by a combination of the snapshot quality and the history cost at each time step.

Ideally, a good partition should have high snapshot quality (i. e. it should cluster well the data at time t) and low history cost (i. e. it should be similar to the partition at the previous time step). In order to ﬁnd Ct from Ct−1 and the relational data at time t Chakrabarti et al. suggested to minimize the diﬀerence between the snapshot quality and the history cost, with a relative weight cp that is a tunable parameter. The input of the procedure consists in the sequence of adjacency/similarity matrices at diﬀerent time steps. In practice, one could use modiﬁed versions of such matrices, obtained by performing (weighted) averages of the data over some time window, in order to make the relational data more robust against noise and the results of the clustering procedure more reliable. One can adopt arbitrary measures to compute the snapshot quality and the historical cost. Besides, several known clustering techniques used for static graphs can be reformulated within this evolutionary framework. Chakrabarti et al. derived evolutionary versions of hierarchical clustering (Section IV.B) and k-means clustering (Section IV.C), whereas Chi et al. (Chi et al., 2007) designed two implementations for spectral clustering (Section IV.D). Based on evolutionary clustering, Lin et al. (Lin et al., 2008) introduced a framework, called FacetNet, that allows vertices to belong to more communities at the same time. Here the snapshot cost28 is the Kullback-Leibler (KL) divergence (Kullback and Leibler, 1951) between the adjacency/similarity matrix at time t and the matrix describing the community structure of the graph at time t; the history cost is the KL divergence between the matrices describing the community structure of the graph at times t − 1 and t. FacetNet can be extended to handle adding and removing of vertices as well as variations of the number of clusters in consecutive time steps. However, it is not able to account for the creation and the disintegration of communities and not scalable to large systems due to the high number of iterations necessary for the matrix computations to reach convergence. These issues have been addressed in a recent approach by Kim and Han (Kim and Han, 2009).

Naturally, what one hopes to achieve at the end of the day is to see how real groups form and evolve in time. Backstrom et al. (Backstrom et al., 2006) have carried out an analysis of group dynamics in the free online community of LiveJournal (http://www.livejournal.com/) and in a coauthorship network of computer scientists. Here the groups are identiﬁed through the declared memberships of users (for LiveJournal) and conferences attended by computer scientists, respectively. Backstrom and coworkers have found that the probability that an individual joins a community grows with the number of friends/coauthors who are already in the community and

28 Lin et al. used the cost and not the quality to evaluate the ﬁt of the partition to the data. The two estimates are obviously related: the lower the cost, the higher the quality.

(for LiveJournal) with their degree of interconnectedness. Moreover, the probability of growth of LiveJournal communities is positively correlated to a combination of factors including the community size, the number of friends of community members which are not in the community and the ratio of these two numbers. A high density of triads within a community appears instead to hinder its growth.

###### XIV. SIGNIFICANCE OF CLUSTERING

Given a network, many partitions could represent meaningful clusterings in some sense, and it could be difﬁcult for some methods to discriminate between them. Quality functions evaluate the goodness of a partition (Section III.C.2), so one could say that high quality corresponds to meaningful partitions. But this is not necessarily true. In Section VI.C we have seen that high values of the modularity of Newman and Girvan do not necessarily indicate that a graph has a deﬁnite cluster structure. In particular we have seen that partitions of random graphs may also achieve considerably large values of Q, although we do not expect them to have community structure, due to the lack of correlations between the linking probabilities of the vertices. The optimization of quality functions, like modularity, delivers the best partition according to the criterion underlying the quality function. But is the optimal clustering also signiﬁcant, i. e. a relevant feature of the graph, or is it just a byproduct of randomness and basic structural properties like, e. g., the degree sequence? Little eﬀort has been devoted to this crucial issue, that we discuss here.

In some works the concept of signiﬁcance has been related to that of robustness or stability of a partition against random perturbations of the graph structure. The basic idea is that, if a partition is signiﬁcant, it will be recovered even if the structure of the graph is modiﬁed, as long as the modiﬁcation is not too extensive. Instead, if a partition is not signiﬁcant, one expects that minimal modiﬁcations of the graph will suﬃce to disrupt the partition, so other clusterings are recovered. A nice feature of this approach is the fact that it can be applied for any clustering technique. Gfeller et al. (Gfeller et al.,

- 2005) considered the general case of weighted graphs. A graph is modiﬁed, in that its edge weights are increased or decreased by a relative amount 0 < σ < 1. This choice also allows to account for the possible eﬀects of uncertainties in the values of the edge weights, resulting from measurements/experiments carried out on a given system. After ﬁxing σ (usually to 0.5), multiple realizations of the original graph are generated. The best partition for each realization is identiﬁed and, for each pair


of adjacent vertices i and j, the in-cluster probability pij is computed, i. e. the fraction of realizations in which i and j were classiﬁed in the same cluster. Edges with in-cluster probability smaller than a threshold θ (usually 0.8) are called external edges. The stability of a partition

is estimated through the clustering entropy

1 m

S = −

[pij log2 pij − (1 − pij)log2(1 − pij)],

(i,j):Aij=1

(84) where m is, as usual, the number of graph edges, and the sum runs over all edges. The most stable partition has pij = 0 along inter-cluster edges and pij = 1 along intra-cluster edges, which yields S = 0; the most unstable partition has pij = 1/2 on all edges, yielding S = 1. The absolute value of S is not meaningful, though, and needs to be compared with the corresponding value for a null model graph, similar to the original graph, but with supposedly no cluster structure. Gfeller et al. adopted the same null model of Newman-Girvan modularity, i. e. the class of graphs with expected degree sequence coinciding with that of the original graph. Since the null model is deﬁned on unweighted graphs, the signiﬁcance of S can be assessed only in this case, although it would not be hard to think of a generalization to weighted graphs. The approach enables one as well to identify unstable vertices, i. e. vertices lying at the boundary between clusters. In order to do that, the external edges are removed and the connected components of the resulting disconnected graph are associated with the clusters detected in the original graph, based on their relative overlap (computed through Eq. 97). Unstable vertices end up in components that are not associated to any of the initial clusters. A weakness of the method by Gfeller et al. is represented by the two parameters σ and θ, whose values are in principle arbitrary.

More recently, Karrer et al. (Karrer et al., 2008) adopted a similar strategy to unweighted graphs. Here one performs a sweep over all edges: the perturbation consists in removing each edge with a probability α and replacing it with another edge between a pair of vertices (i,j), chosen at random with probability pij = kikj/2m, where ki and kj are the degrees of i and j. We recognize the probability of the null model of Newman-Girvan modularity. Indeed, by varying the probability α from 0 to 1 one smoothly interpolates between the original graph (no perturbation) and the null model (maximal perturbation). The degree sequence of the graph remains invariant (on average) along the whole process, by construction. The idea is that the perturbation aﬀects solely the organization of the vertices, keeping the basic structural properties. For a given value of α, many realizations of the perturbed graph are generated, their cluster structures are identiﬁed with some method (Karrer et al. used modularity optimization) and compared with the partition obtained from the original unperturbed graph. The partitions are compared by computing the variation of information V (Section XV.B). From the plot of the average V versus α one can assess the stability of the cluster structure of the graph. If V (α) changes rapidly for small values of α the partition is likely to be unstable. As in the approach by Gfeller et al. the behaviour of the function V (α) does not have an absolute meaning,

but needs to be compared with the corresponding curve obtained for a null model. For consistency, the natural choice is again the null model of modularity, which is already used in the process of graph perturbation. The approaches by Gfeller et al. and Karrer et al., with suitable modiﬁcations, can also be used to check for the stability of the cluster structure in parts of a graph, up to the level of individual communities. This is potentially important

- as it may happen that some parts of the graph display a strong community structure and other parts weak or no community structure at all.


Rosvall and Bergstrom (Rosvall and Bergstrom, 2008) deﬁned the signiﬁcance of clusters with the bootstrap method (Efron and Tibshirani, 1993), which is a standard procedure to check for the accuracy of a measurement/estimate based on resampling from the empirical data. The graph at study is supposed to be generated by a parametric model, which is used to create many sam-

- ples. This is done by assigning to each edge a weight taken by a Poisson distribution with mean equal to the original edge weight. For the initial graph and each sample one identiﬁes the community structure with some method, that can be arbitrary. For each cluster of the partition of the original graph one determines the largest subset of vertices that are classiﬁed in the same cluster in at least 95% of all bootstrap samples. Identifying such cluster cores enables one to track the evolution in time of the community structure, as we explained in Section XIII.


A diﬀerent approach has been proposed by Massen and Doye (Massen and Doye, 2006). They analyzed an equilibrium canonical ensemble of partitions, with −Q playing the role of the energy, Q being Newman-Girvan modularity. This means that the probability of occurrence of a partition at temperature T is proportional to exp(Q/T). The idea is that, if a graph has a signiﬁcant cluster structure, at low temperatures one would recover essentially the same partition, corresponding to the modularity maximum, which is separated by an appreciable gap from the modularity values of the other partitions. On the contrary, graphs with no community structure, e. g. random graphs, have many competing (local) maxima, and the corresponding conﬁgurations will emerge already at low temperatures, since their modularity values are close to the absolute maximum29. These distinct behaviors can manifest themselves in various ways. For instance, if one considers the variation of the speciﬁc heat C = −dQ/dT with T, the gap in the modularity landscape is associated to a sharp peak of

- C around some temperature value, like it happens in a


29 As we have seen in Section VI.C, Good et al. (Good et al., 2009) have actually shown that the modularity landscape has a huge degeneracy of states with high modularity values, close to the global maximum, especially on graphs with community structure. So the results of the method by Massen and Doye may be misleading.

phase transition. If the gap is small and there are many partitions with similar modularity values, the peak of C becomes broad. Another strategy to assess the signiﬁcance of the maximum modularity partition consists of the investigation of the similarity between partitions recovered at a given temperature T. This similarity can be expressed by the frequency matrix, whose element fij indicates the relative number of times vertices i and j have been classiﬁed in the same cluster. If the graph has a clear community structure, at low temperatures the frequency matrix can be put in block-diagonal form, with the blocks corresponding to the communities of the best partition; if there is no signiﬁcant community structure, the frequency matrix is rather homogeneous. The Fiedler eigenvalue (Fiedler, 1973) λ2, the second smallest eigenvalue of the Laplacian matrix associated to the frequency matrix, allows to estimate how “block-diagonal” the matrix is (see Section IV.A). At low temperatures λ2 ∼ 0 if there is one (a few) partitions with maximum or near to maximum modularity; if there are many (almost) degenerate partitions, λ2 is appreciably diﬀerent from zero even when T → 0. A sharp transition from low to high values of λ2 by varying temperature indicates signiﬁcant community structure. Another clear signature of signiﬁcant community structure is the observation of a rapid drop of the average community size with T, as “strong” communities break up in many small pieces for a modest temperature increase, while the disintegration of “weak” communities takes place more slowly. In scalefree graphs (Section A.3) clusters are often not well separated, due to the presence of the hubs; in these cases the above-mentioned transitions of ensemble variables are not so sharp and take place over a broader temperature range. The canonical ensemble of partitions is generated through single spin heatbath simulated annealing (Reichardt and Bornholdt, 2006a), combined with parallel tempering (Earl and Deem, 2005). The approach by Massen and Doye could be useful to recognize graphs without cluster structure, if the modularity landscape is characterized by many maxima with close values (but see Footnote). However, it can happen that gaps between the absolute modularity maximum and the rest of the modularity values are created by ﬂuctuations, and the method is unable to identify these situations. Furthermore, the approach heavily relies on modularity and on a costly technique like simulated annealing: extensions to other quality functions and/or optimization procedures do not appear straightforward.

In a recent work by Bianconi et al. (Bianconi et al., 2009) the notion of entropy of graph ensembles (Bianconi, 2008; Bianconi et al., 2008) is employed to ﬁnd out how likely it is for a cluster structure to occur on a graph with a given degree sequence. The entropy is computed from the number of graph conﬁgurations which are compatible with a given classiﬁcation of the vertices in q groups. The clustering is quantitatively described by ﬁxing the number of edges A(q1,q2) running between clusters q1 and q2, for all choices of q1 = q2. Bianconi et al. proposed

the following indicator of clustering signiﬁcance

Σk,q  −  Σk,π(q ) π δΣ2k,π(q ) π

Θk,q  =

, (85)

where Σk,q  is the entropy of the graph conﬁgurations with given degree sequence k and clustering q  (with ﬁxed numbers of inter-cluster edges A(q1,q2)), and Σk,π(q ) π is the average entropy of the conﬁgurations with the same degree sequence and a random permutation π(q ) of the cluster labels. The absolute value of the entropy Σk,q  is not meaningful, so the comparison of Σk,q  and Σk,π(q ) π is crucial, as it tells how relevant the actual cluster structure is with respect to a random classiﬁcation of the vertices. However, diﬀerent permutations of the assignments

- q  yield diﬀerent values of the entropy, which can ﬂuctuate considerably. Therefore one has to compute the standard


deviation δΣ2k,π(q ) π of the entropy corresponding to all random permutations π(q ), to estimate how signiﬁcant

the diﬀerence between Σk,q  and Σk,π(q ) π is. In this way, if Θk,q  ≤ 1, the entropy of the given cluster structure is of the same order as the entropy of some random permutation of the cluster labels, so it is not relevant. Instead, if Θk,q  1, the cluster structure is far more likely than a random classiﬁcation of the vertices, so the clustering is relevant. The indicator Θk,q  can be simply generalized to the case of directed and weighted graphs.

Lancichinetti et al. (Lancichinetti et al., 2009) as well addressed the issue by comparing the cluster structure of the graph with that of a random graph with similar properties. An important novelty of this approach is the fact that it estimates the signiﬁcance of single communities, not of partitions. In fact, not all communities are equally signiﬁcant, in general, so it makes a lot of sense to check them individually. In particular, it may happen that real networks are not fully modular, due to their particular history or generating mechanisms, and that only portions of them display community structure. The main idea is to verify how likely it is that a community C is a subgraph of a random graph with the same degree sequence of the original graph. This likelihood is called C-score, and is computed by examining the vertex w of C, with the lowest internal degree kwin in C (the “worst” vertex). The C-score is deﬁned as the probability that the internal degree of the worst vertex in the corresponding community of the null model graphs is larger than or equal to kwin. This probability is computed by using tools from Extreme and Order Statistics (Beirlant et al., 2004; David and Nagaraja, 2003). A low value of the C-score (≤ 5%) is a strong indication that the group of vertices at study is a community and not the product of random ﬂuctuations. In addition, the measure can be used to check whether a subgraph has an internal modular structure. For that, one removes the vertices of the subgraph one

- at a time, starting from the worst and proceeding in increasing order of the internal degree, and observes how


the C-score varies at each vertex removal: sharp drops indicate the presence of dense subgraphs (Fig. 29). Therefore, one could think of using the C-score as ingredient of new clustering techniques. As we have seen, the C-score is based on the behavior of the vertex with lowest internal degree of the subgraph. Real networks are characterized by noise, which could strongly aﬀect the structural relationships between vertices and clusters. For this reason, relying on the properties of a single vertex to evaluate the signiﬁcance of a subgraph could be a problem for applications to real networks. Lancichinetti et al. have shown that the C-score can be easily extended to consider the t vertices with lowest internal degree, with t > 1 (Bscore). The main limit of the C-score is the fact that its null model is the same as that of Newman-Girvan modularity. According to this null model, each vertex can in principle be connected to any other, no matter how large the system is. This is however not realistic, especially for large graphs, where it is much more reasonable to assume that each vertex has its own “horizon”, i.e. a subset of other vertices with which it can interact, which is usually much smaller than the whole system (see Section VI.C). How to deﬁne such “horizons” and, more in general, realistic null models is still an open problem. However, the C-score could be easily reformulated with any null model, so one could readily derive more reliable deﬁnitions.

We conclude with a general issue which is related to the signiﬁcance of community structure. The question is: given a cluster structure in a graph, can it be recovered a priori by an algorithm? In a recent paper (Reichardt and Leone, 2008), Reichardt and Leone studied under which conditions a special built-in cluster structure can be recovered. The clusters have equal size and a pair of vertices is connected with probability p if they belong to the same cluster, with probability r < p otherwise. In computer science this is known as the planted partitioning problem (Condon and Karp, 2001). The goal is to propose algorithms that recover the planted partition for any choice of p and r. For dense graphs, i. e. graphs whose average degree grows with the number n of vertices, algorithms can be designed that ﬁnd the solution with a probability which equals 1 minus a term that vanishes in the limit of inﬁnite graph size, regardless of the diﬀerence p − r, which can then be chosen arbitrarily small. Since many real networks are not dense graphs, as their average degree k is usually much smaller than n and does not depend on it, Reichardt and Leone investigated the problem in the case of ﬁxed k and inﬁnite graph size. We indicate with q the number of clusters and with pin the probability that a randomly selected edge of the graph lies within any of the q clusters. In this way, if pin = 1/q, the inter-cluster edge density matches the intra-cluster edge density (i. e. p = r), and the planted partition would not correspond to a recoverable clustering, whereas for pin = 1, there are no inter-cluster edges and the partition can be trivially recovered. The value of pin is in principle unknown, so one has to detect the cluster structure ignoring this information. Reichardt

one cluster+ random nodes two clusters

100

100

| |
|---|
| |


| | |
|---|---|
| | |


10-2

10-2

## C-score

10-4

10-4

| | |
|---|---|


# (b)

# (a)

10-6

10-6

0 10 20 30 40

0 10 20 30 40 50 60 70

removed nodes

removed nodes

- FIG. 29 Application of the C-score by Lancichinetti et al. (Lancichinetti et al., 2009) to identify modules within subgraphs. In (a) the subgraph consists of a compact cluster (generated with the LFR benchmark (Lancichinetti and Fortunato, 2009; Lancichinetti et al., 2008)) plus some randomly added vertices. In (b) the subgraph consists of two compact clusters interconnected by a few edges. Vertices are removed from each subgraph in increasing order of their internal degree. The C-score displays sharp drops after all the spurious vertices (a) and all the vertices of one of the two clusters (b) are removed. We notice that the ﬁrst subgraph (a) is not signiﬁcant (high C-score) until the noise represented by the randomly added vertices disappears, whereas the second subgraph (b) is a community at the very beginning, as it should be, it loses signiﬁcance when one of the clusters is heavily damaged (because the remainder of the cluster appears as noise, just like the spurious vertices in (a)), and becomes signiﬁcant again when the damaged cluster is totally removed. Reprinted ﬁgure with permission from Ref. (Lancichinetti et al., 2009).


and Leone proposed to look for a minimum cut partition, i. e. for the partition that minimizes the number of inter-cluster edges, as it is usually done in the graph partitioning problem (discussed in Section IV.A). Clearly, for pin = 1 the minimum cut partition trivially coincides with the planted partition, whereas for 1/q < pin < 1 there should be some overlap, which is expected to vanish in the limit case pin = 1/q. The minimum cut partition corresponds to the minimum of the following ferromagnetic Potts model Hamiltonian

Hpart = −

i<j

Jijδσ

i,σj, (86)

over the set of all spin conﬁgurations with zero magnetization. Here the spin σi indicates the cluster vertex i belongs to, and the coupling matrix Jij is just the adjacency matrix of the graph. The constraint of zero magnetization ensures that the clusters have all the same size, as required by the planted partitioning problem. The energy of a spin conﬁguration, expressed by Eq. 86, is the negative of the number of edges that lie within clusters: the minimum energy corresponds to the maximum number of intra-cluster edges, which is coupled to the

minimum number of inter-cluster edges. The minimum energy can be computed with the cavity method, or belief propagation, at zero temperature (M´ezard and Parisi, 2003). The accuracy of the solution with respect to the planted partition is expressed by the fraction of vertices which are put in the same class in both partitions. The analysis yields a striking result: the planted clustering is accurately recovered for pin larger than a critical threshold pcin > 1/q. So, there is a range of values of pin, 1/q < pin < pcin, in which the clustering is not recoverable, as the minimum cut partition is uncorrelated with it. The threshold pcin depends on the degree distribution p(k) of the graph.

###### XV. TESTING ALGORITHMS

When a clustering algorithm is designed, it is necessary to test its performance, and compare it with that of other methods. In the previous sections we have said very little about the performance of the algorithms, other than their computational complexity. Indeed, the issue of testing algorithms has received very little attention in the literature on graph clustering. This is a serious

limit of the ﬁeld. Because of that, it is still impossible to state which method (or subset of methods) is the most reliable in applications, and people rely blindly on some algorithms instead of others for reasons that have nothing to do with the actual performance of the algorithms, like. e.g. popularity (of the method or of its inventor). This lack of control is also the main reason for the proliferation of graph clustering techniques in the last few years. Virtually in any paper, where a new method is introduced, the part about testing consists in applying the method to a small set of simple benchmark graphs, whose cluster structure is fairly easy to recover. Because of that, the freedom in the design of a clustering algorithm is basically inﬁnite, whereas it is not clear what a new procedure is adding to the ﬁeld, if anything.

In this section we discuss at length the issue of testing. First, we describe the fundamental ingredients of any testing procedure, i. e. benchmark graphs with built-in community structure, that methods have to identify (Section XV.A). We proceed by reviewing measures to compare graph partitions with each other (Section XV.B). In Section XV.C we present the comparative evaluations of diﬀerent methods that have been performed in the literature.

A. Benchmarks

Testing an algorithm essentially means applying it to a speciﬁc problem whose solution is known and comparing such solution with that delivered by the algorithm. In the case of graph clustering, a problem with a welldeﬁned solution is a graph with a clear community structure. This concept is not trivial, however. Many clustering algorithms are based on similar intuitive notions of what a community is, but diﬀerent implementations. So it is crucial that the scientiﬁc community agrees on a set of reliable benchmark graphs. This mostly applies to computer-generated graphs, where the built-in cluster structure can be arbitrarily designed. In the literature real networks are used as well, in those cases in which communities are well deﬁned because of information about the system.

We start our survey from computer-generated benchmarks. A special class of graphs has become quite popular in the last years. They are generated with the so-called planted -partition model (Condon and Karp,

- 2001). The model partitions a graph with n = g · vertices in groups with g vertices each. Vertices of the


same group are linked with a probability pin, whereas vertices of diﬀerent groups are linked with a probability pout. Each subgraph corresponding to a group is then a random graph ´ la Erd¨s-Re´nyi with connection probability p = pin (Section A.3). The average degree of a vertex is k = pin(g −1)+poutg( −1). If pin > pout the intra-cluster edge density exceeds the inter-cluster edge density and the graph has a community structure. This idea is quite intuitive and we have encountered it in sev-

eral occasions in the previous sections. Girvan and Newman considered a special case of the planted -partition model (Girvan and Newman, 2002). They set = 4, g = 32 (so the number of graph vertices is n = 128) and ﬁxed the average total degree k to 16. This implies that pin + 3pout ≈ 1/2, so the probabilities pin and pout are not independent parameters. In calculation it is common to use as parameters zin = pin(g − 1) = 31pin and zout = poutg( − 1) = 96pout, indicating the expected internal and external degree of a vertex, respectively. These particular graphs have by now gained the status of standard benchmarks (Girvan and Newman, 2002) (Fig. 30). In the ﬁrst applications of the graphs one assumed that communities are well deﬁned when zout < 8, corresponding to the situation in which the internal degree exceeds the external degree. However, the threshold zout = zin = 8 implies pin ≈ 1/4 and pout = 1/12, so it is not the actual threshold of the model, where pin = pout = 1/8, corresponding to zout ≈ 12. So, one expects30 to be able to detect the planted partition up until zout ≈ 12.

Testing a method against the Girvan-Newman benchmark consists in calculating the similarity between the partitions determined by the method and the natural partition of the graph in the four equal-sized groups. Several measures of partitions’ similarity may be adopted; we describe them in Section XV.B. One usually builds many graph realizations for a particular value of zout and computes the average similarity between the solutions of the method and the built-in solution. The procedure is then iterated for diﬀerent values of zout. The results are usually represented in a plot, where the average similarity is drawn as a function of zout. Most algorithms usually do a good job for small zout and start to fail when zout approaches 8. Fan et al. (Fan et al., 2007) have designed a weighted version of the benchmark of Girvan and Newman, in that one gives diﬀerent weights to edges inside and between communities. One could pick just two values, one for intra- and the other for intercommunity edges, or uniformly distributed values in two diﬀerent ranges. For this benchmark there are then two parameters that can be varied: zout and the relative importance of the internal and the external weights. Typically one ﬁxes the topological structure and varies the weights. This is particularly insightful when zout = 4, which delivers graphs without topological cluster structure: in this case, the question whether there are clusters or not depends entirely on the weights.

As we have remarked above, the planted -partition model generates mutually interconnected random graphs

30 However, we stress that, even if communities are there, methods may be unable to detect them. The reason is that, due to ﬂuctuations in the distribution of links in the graphs, already before the limit imposed by the planted partition model it may be impossible to detect the communities and the model graphs may look similar to random graphs.

![image 69](Community Detection in Graphs_images/imageFile69.png)

- FIG. 30 Benchmark of Girvan and Newman. The three pictures correspond to zin = 15 (a), zin = 11 (b) and zin = 8 (c). In (c) the four groups are hardly visible. Reprinted ﬁgure with permission from Ref. (Guimera` and Amaral, 2005). c 2005 by the Nature Publishing Group.


´ la Erd¨s-R´enyi. Therefore, all vertices have approximately the same degree. Moreover, all communities have exactly the same size by construction. These two features are at odds with what is observed in graph representations of real systems. Degree distributions are usually skewed, with many vertices with low degree coexisting with a few vertices with high degree. A similar heterogeneity is also observed in the distribution of cluster sizes, as we shall see in Section XVI. So, the planted -partition model is not a good description of a real graph with community structure. However, the model can be modiﬁed to account for the heterogeneity of degrees and community sizes. A modiﬁed version of the model, called Gaussian random partition generator, was designed by Brandes et al. (Brandes et al., 2003). Here the cluster sizes have a Gaussian distribution, so they are not the same, although they do not diﬀer much from each other. The heterogeneity of the cluster sizes introduces a heterogeneity in the degree distribution as well, as the expected degree of a vertex depends on the number of vertices of its cluster. Still, the variability of degree and cluster size is not appreciable. Besides, vertices of the same cluster keep having approximately the same degree. A better job in this direction has been recently done by Lancichinetti et al. (LFR benchmark) (Lancichinetti et al., 2008). They assume that the distributions of degree and community size are power laws, with exponents τ1 and τ2, respectively. Each vertex shares a fraction 1 − µ of its edges with the other vertices of its community and a fraction µ with the vertices of the other communities; 0 ≤ µ ≤ 1 is the mixing parameter. The graphs are built as follows:

- 1. A sequence of community sizes obeying the prescribed power law distribution is extracted. This is done by picking random numbers from a power law distribution with exponent τ2.
- 2. Each vertex i of a community receives an internal


degree (1 − µ)ki, where ki is the degree of vertex i, which is taken by a power law distribution with ex-

ponent τ1. In this way, each vertex i has a number of stubs (1 − µ)ki.

- 3. All stubs of vertices of the same community are randomly attached to each other, until no more stubs are “free”. In this way the sequence of internal degrees of each vertex in its community is maintained.
- 4. Each vertex i receives now an additional number of stubs, equal to µki (so that the ﬁnal degree of the vertex is ki), that are randomly attached to vertices of diﬀerent communities, until no more stub is “free”.


Numerical tests show that this procedure has a complexity O(m), where m is as usual the number of edges of the graph, so it can be used to create graphs of sizes spanning several orders of magnitude. Fig. 31 shows an example of a LFR benchmark graph. Recently the LFR benchmark has been extended to directed and weighted graphs with overlapping communities (Lancichinetti and Fortunato, 2009). The software to create the LFR benchmark graphs can be freely downloaded at http://santo.fortunato.googlepages.com/inthepre ss2.

A class of benchmark graphs with power law degree distributions had been previously introduced by Bagrow (Bagrow, 2008). The construction process starts from a graph with a power-law degree distribution. Bagrow used Barab´si-Albert scale free graphs (Barab´si and Albert, 1999). Then, vertices are randomly assigned to one of four equally-sized communities. Finally, pairs of edges between two communities are rewired so that either edge ends up within the same community, without altering the degree sequence (on average). This is straightforward: suppose that the edges join the vertex

![image 70](Community Detection in Graphs_images/imageFile70.png)

- FIG. 31 A realization of the LFR benchmark graphs (Lancichinetti et al., 2008), with 500 vertices. The distributions of the vertex degree and of the community size are both power laws. Such benchmark is a more faithful approximation of real-world networks with community structure than simpler benchmarks like, e. g., that by Girvan and Newman (Girvan and Newman,


- 2002). Reprinted ﬁgure with permission from Ref. (Lancichinetti et al., 2008). c 2008 by the American Physical Society.


pairs a1, b1 and a2, b2, where a1, a2 belong to community A and b1, b2 to community B. It the edges are replaced by a1-a2 and b1-b2 (provided they do not exist already), all vertices keep their degrees. With this rewiring procedure one can arbitrarily vary the edge density within and, consequently, between clusters. In this class of benchmarks, however, communities are all of the same size by construction, although one can in principle relax this condition.

A (seemingly) diﬀerent benchmark is represented by the class of relaxed caveman graphs, which were originally introduced to explain the clustering properties of social networks (Watts, 2003). The starting point is a set of disconnected cliques. With some probability edges are rewired to link diﬀerent cliques. Such model graphs are interesting as they are smooth variations of the ideal graph with “perfect” communities, i. e. disconnected cliques. On the other hand the model is equivalent to the planted -partition model, where pin = 1 − p and pout is proportional to p, with coeﬃcient depending on the size of the clusters.

Benchmark graphs have also been introduced to deal with special types of graphs and/or cluster structures. For instance, Arenas et al. (Arenas et al., 2006) have introduced a class of benchmark graphs with embedded

hierarchical structure, which extends the class of graphs by Girvan and Newman. Here there are 256 vertices and two hierarchical levels, corresponding to a partition in 16 groups (microcommunities) with 16 vertices and a partition in 4 larger groups of 64 vertices (macrocommunities), comprising each 4 of the smaller groups. The edge densities within and between the clusters are indicated by three parameters zin

, zin

###### and zout: zin

is the expected internal degree of a vertex within its microcommunity; zin

1

2

1

is the expected number of edges that the vertex shares with the vertices of the other microcommunities within its macrocommunity; zout is the expected number of edges connecting the vertex with vertices of the other three macrocommunities. The average degree

2

+ zout of a vertex is ﬁxed to 18. Fig. 7 shows an example of hierarchical graph constructed based on the same principle, with 512 vertices and an average degree of 32.

k = zin

###### + zin

1

2

Guimer` et al. (Guimer` et al., 2007) have proposed a model of bipartite graphs with built-in communities. They considered a bipartite graph of actors and teams, here we describe how to build the benchmarks for general bipartite graphs. One starts from a bipartite graph whose vertex classes A and B are partitioned into nc groups, CiA and CiB (i = 1,2,...,nc). Each cluster Ci

comprises all vertices of the subgroups CiA and CiB, respectively. With probability p edges are placed between

vertices of subgroups CiA and CiB (i = 1,2,...,nc), i. e. within clusters. With probability 1 − p, edges are placed

between vertices of subgroups CiA and CjB, where i and j are chosen at random, so they can be equal or diﬀerent. By construction, a non-zero value of the probability p indicates a preference by vertices to share links with vertices of the same cluster, i. e. for p > 0 the graph has a built-in community structure. For p = 1 there would be edges only within clusters, i. e. the graph has a perfect cluster structure.

Finally, Sawardecker et al. introduced a general model, that accounts for the possibility that clusters overlap (Sawardecker et al., 2009). The model is based on the reasonable assumption that the probability pij that two vertices are connected by an edge grows with the number n0 of communities both vertices belong to. For vertices in diﬀerent clusters, pij = p0, if they are in the same cluster (and only in that one) pij = p1, if they belong to the same two clusters pij = p2, etc.. By hypothesis, p0 < p1 ≤ p2 ≤ p3.... The planted -partition model is recovered when p1 = p2 = p3....

As we have seen, nearly all existing benchmark graphs are inspired by the planted -partition model, to some extent. However, the model needs to be reﬁned to provide a good description of real graphs with community structure. The hypothesis that the linking probabilities of each vertex with the vertices of its community or of the other communities are constant is not realistic. It is more plausible that each pair of vertices i and j has its own linking probability pij, and that such probabilities are correlated for vertices in the same cluster.

Tests on real networks usually focus on a very limited number of examples, for which one has precise information about the vertices and their properties.

In Section II we have introduced two popular real networks with known community structure, i. e. the social network of Zachary’s karate club and the social network of bottlenose dolphins living in Doubtful Sound (New Zealand), studied by Lusseau. Here, the question is whether the actual separation in two social groups could be predicted from the graph topology. Zachary’s karate club is by far the most investigated system. Several algorithms are actually able to identify the two classes, modulo a few intermediate vertices, which may be misclassiﬁed. Other methods are less successful: for instance, the maximum of Newman-Girvan modularity corresponds to a split of the network in four groups (Donetti and Mun˜oz, 2004; Duch and Arenas, 2005). Another well known example is the network of American college football teams, derived by Girvan and Newman (Girvan and Newman, 2002). There are 115 vertices, representing the teams, and two vertices are connected if their teams play against each other. The teams are divided into 12 conferences. Games between teams in the same conference are more frequent than games between teams of diﬀerent conferences, so one has a natural partition where the commu-

nities correspond to the conferences.

When dealing with real networks, it is useful to resolve their community structure with diﬀerent clustering techniques, to cross-check the results and make sure that they are consistent with each other, as in some cases the answer may strongly depend on the speciﬁc algorithm adopted. However, one has to keep in mind that there is no guarantee that “reasonable” communities, deﬁned on the basis of non-structural information, must coincide with those detected by methods based only on the graph structure.

B. Comparing partitions: measures

Checking the performance of an algorithm involves deﬁning a criterion to establish how “similar” the partition delivered by the algorithm is to the partition one wishes to recover. Several measures for the similarity of partitions exist. In this section we present and discuss the most popular measures. A thorough introduction of similarity measures for graph partitions has been given by Meil˘ (Meil˘, 2007) and we will follow it closely.

Let us consider two generic partitions X = (X1,X2,...,Xn

) and Y = (Y1,Y2,...,Yn

) of a graph G, with nX and nY clusters, respectively. We indicate with n the number of graph vertices, with nXi and nYj the number of vertices in clusters Xi and Yj and with nij the number of vertices shared by clusters Xi and Yj: nij = |Xi Yj|.

X

Y

In the ﬁrst tests using the benchmark graphs by Girvan and Newman (Section XV.A) scholars used a measure proposed by Girvan and Newman themselves, the fraction of correctly classiﬁed vertices. A vertex is correctly classiﬁed if it is in the same cluster with at least half of its “natural” partners. If the partition found by the algorithm has clusters given by the merging of two or more natural groups, all vertices of the cluster are considered incorrectly classiﬁed. The number of correctly classiﬁed vertices is then divided by the total size of the graph, to yield a number between 0 and 1. The recipe to label vertices as correctly or incorrectly classiﬁed is somewhat arbitrary, though.

Apart from the fraction of correctly classiﬁed vertices, which is somewhat ad hoc and distinguishes the roles of the natural partition and of the algorithm’s partition, most similarity measures can be divided in three categories: measures based on pair counting, cluster matching and information theory.

Measures based on pair counting depend on the number of pairs of vertices which are classiﬁed in the same (diﬀerent) clusters in the two partitions. In particular a11 indicates the number of pairs of vertices which are in the same community in both partitions, a01 (a10) the number of pairs of elements which are put in the same community in X (Y) and in diﬀerent communities in Y (X) and a00 the number of pairs of vertices that are in diﬀerent communities in both partitions. Wallace (Wal-

lace, 1983) proposed the two indices WI =

a11 k nYk (nYk − 1)/2

a11 k nXk (nXk − 1)/2

; WII =

.

(87) WI and WII represent the probability that vertex pairs in the same cluster of X are also in the same cluster for Y, and viceversa. These indices are asymmetrical, as the role of the two partitions is not the same. Fowlkes and Mallows (Fowlkes and Mallows, 1983) suggested to use the geometric mean of WI and WII, which is symmetric.

The Rand index (Rand, 1971) is the ratio of the number of vertex pairs correctly classiﬁed in both partitions (i. e. either in the same or in diﬀerent clusters), by the total number of pairs

a11 + a00 a11 + a01 + a10 + a00

R(X,Y) =

. (88)

A measure equivalent to the Rand index is the Mirkin metric (Mirkin, 1996)

M(X,Y) = 2(a01 + a10) = n(n − 1)[1 − R(X,Y)]. (89)

The Jaccard index is the ratio of the number of vertex pairs classiﬁed in the same cluster in both partitions, by the number of vertex pairs which are classiﬁed in the same cluster in at least one partition, i. e.

a11 a11 + a01 + a10

J(X,Y) =

. (90)

Adjusted versions of both the Rand and the Jaccard index exist, in that a null model is introduced, corresponding to the hypothesis of independence of the two partitions (Meil˘, 2007). The null model expectation value of the measure is subtracted from the unadjusted version, and the result is normalized by the range of this diﬀerence, yielding 1 for identical partitions and 0 as expected value for independent partitions (negative values are possible as well). Unadjusted indices have the drawback that they are not local, i. e. the result depends on how the whole graph is partitioned, even when the partitions diﬀer only in a small region of the graph.

Similarity measures based on cluster matching aim at ﬁnding the largest overlaps between pairs of clusters of diﬀerent partitions. For instance, the classiﬁcation error H(X,Y) is deﬁned as (Meil˘ and Heckerman, 2001)

nX

1 n

H(X,Y) = 1 −

max

nkπ(k), (91)

π

k=1

where π is an injective mapping from the cluster indices of partition Y to the cluster indices of partition X. The maximum is taken over all possible injections {π}. In this way one recovers the maximum overlap between the clusters of the two partitions. An alternative measure is the normalized Van Dongen metric, deﬁned as (van Dongen, 2000b)

1 2n

D(X,Y) = 1−

nY

nX

max

nkk +

max

nkk . (92)

k

k

k=1

k =1

A common problem of this type of measures is that some clusters may not be taken into account, if their overlap with clusters of the other partition is not large enough. Therefore if we compute the similarity between two partitions X and X and partition Y, with X and X diﬀering from each other by a diﬀerent subdivision of parts of the graph that are not used to compute the measure, one would obtain the same score.

The third class of similarity measures is based on reformulating the problem of comparing partitions as a problem of message decoding within the framework of information theory (Mackay, 2003). The idea is that, if two partitions are similar, one needs very little information to infer one partition given the other. This extra information can be used as a measure of dissimilarity. To evaluate the Shannon information content (Mackay, 2003) of a partition, one starts by considering the community assignments {xi} and {yi}, where xi and yi indicate the cluster labels of vertex i in partition X and Y, respectively. One assumes that the labels x and y are values of two random variables X and Y , with joint distribution P(x,y) = P(X = x,Y = y) = nxy/n, which implies that P(x) = P(X = x) = nXx /n and P(y) = P(Y = y) = nYy /n. The mutual information I(X,Y ) of two random variables has been previously deﬁned [Eq. (70)], and can be applied as well to partitions X and Y, since they are described by random variables. Actually I(X,Y ) = H(X) − H(X|Y ), where H(X) = − x P(x)log P(x) is the Shannon entropy of X and H(X|Y ) = − x,y P(x,y)log P(x|y) is the conditional entropy of X given Y . The mutual information is not ideal as a similarity measure: in fact, given a partition X, all partitions derived from X by further partitioning (some of) its clusters would all have the same mutual information with X, even though they could be very diﬀerent from each other. In this case the mutual information would simply equal the entropy H(X), because the conditional entropy would be systematically zero. To avoid that, Danon et al. adopted the normalized mutual information (Danon et al., 2005)

2I(X,Y ) H(X) + H(Y )

Inorm(X,Y) =

, (93)

which is currently very often used in tests of graph clustering algorithms. The normalized mutual information equals 1 if the partitions are identical, whereas it has an expected value of 0 if the partitions are independent. The measure, deﬁned for standard partitions, in which each vertex belongs to only one cluster, has been recently extended to the case of overlapping clusters by Lancichinetti et al. (Lancichinetti et al., 2009). The extension is not straightforward as the community assignments of a partition are now speciﬁed by a vectorial random variable, since each vertex may belong to more clusters simultaneously. In fact, the deﬁnition by Lancichinetti et al. is not a proper extension of the normalized mutual information, in the sense that it does not recover exactly the same value of the original measure for the compar-

ison of proper partitions without overlap, even though the values are close.

Meil˘ (Meil˘, 2007) introduced the variation of information

V (X,Y) = H(X|Y ) + H(Y |X), (94)

which has some desirable properties with respect to the normalized mutual information and other measures. In particular, it deﬁnes a metric in the space of partitions

- as it has the properties of distance. It is also a local measure, i. e. the similarity of partitions diﬀering only in a small portion of a graph depends on the diﬀerences of the clusters in that region, and not on the partition of the rest of the graph. The maximum value of the variation of information is log n, so similarity values for partitions of graphs with diﬀerent size cannot be compared with each other. For meaningful comparisons one could divide V (X,Y) by log n, as suggested by Karrer et al. (Karrer


- et al., 2008). A concept related to similarity is that of distance,


which indicates basically how many operations need to be performed in order to transform a partition to another. Gustafsson et al. deﬁned two distance measures for partitions (Gustafsson et al., 2006). They are both based on the concept of meet of two partitions, which is deﬁned as

nA

nB

M =

i=1

j=1

Xi Yj . (95)

The distance measures are mmoved and mdiv. In both cases they are determined by summing the distances of

X and Y from the meet M. For mmoved the distance of X (Y) from the meet is the minimum number of elements that must be moved between X and Y so that X (Y) and M coincide (Gusﬁeld, 2002). For mdiv the distance of X (Y) from the meet is the minimum number of divisions that must be done in X (Y) so that X (Y) and M coincide (Stanley, 1997). Such distance measures can easily be transformed in similarity measures, like

Imoved = 1 − mmoved/n, Idiv = 1 − mdiv/n. (96)

Identical partitions have zero mutual distance and similarity 1 based on Eqs. 96.

Finally an important problem is how to deﬁne the similarity between clusters. If two partitions X and Y of a graph are similar, each cluster of X will be very similar to one cluster of Y, and viceversa, and it is important to identify the pairs of corresponding clusters. For instance, if one has information about the time evolution of a graph, one could monitor the dynamics of single clusters as well, by keeping track of each cluster at diﬀerent time steps (Palla et al., 2007). Given clusters Xi and Yj, their similarity can be deﬁned through the relative overlap sij

sij = |Xi Yj| |Xi Yj|

. (97)

- z out = 6

- z out = 7

- z out = 8


Fraction of nodes correctly identified

- 0.8
- 1


0.6

0.4

0.2

0

NG GN FLM NF DM DMN ZL LP RB DA SA

Method

FIG. 32 Relative performances of the algorithms listed in Table I on the Girvan-Newman benchmark, for three values of the expected average external degree zout. Reprinted ﬁgure with permission from Ref. (Danon et al., 2005). c 2005 by IOP Publishing and SISSA.

In this way, looking for the cluster of Y corresponding to Xi means ﬁnding the cluster Yj that maximizes sij. The index sij can be used to deﬁne similarity measures for partitions as well (Fan et al., 2007; Zhang et al., 2006). An interesting discussion on the problem of comparing partitions, along with further deﬁnitions of similarity measures not discussed here, can be found in Ref. (Traud et al., 2008).

C. Comparing algorithms

The ﬁrst systematic comparative analysis of graph clustering techniques has been carried out by Danon et al. (Danon et al., 2005). They compared the performances of various algorithms on the benchmark graphs by Girvan and Newman (Section XV.A). The algorithms examined are listed in Table I, along with their complexity. Fig. 32 shows the performance of all algorithms. Instead of showing the whole curves of the similarity versus zout (Section XV.A), which would display a fuzzy picture with many strongly overlapping curves, diﬃcult to appreciate, Danon et al. considered three values for

|Author|Ref.|Label|Order|
|---|---|---|---|
|Eckmann & Moses|(Eckmann and Moses, 2002)|EM|O(m k2 )|
|Zhou & Lipowsky|(Zhou and Lipowsky, 2004)|ZL|O(n3)|
|Latapy & Pons|(Latapy and Pons, 2005)|LP|O(n3)|
|Clauset et al.|(Clauset et al., 2004)|NF|O(n log2 n)|
|Newman & Girvan|(Newman and Girvan, 2004)|NG|O(nm2)|
|Girvan & Newman|(Girvan and Newman, 2002)|GN|O(n2m)|
|Guimera` et al.|(Guimera` and Amaral, 2005; Guimera` et al., 2004)|SA|parameter dependent|
|Duch & Arenas|(Duch and Arenas, 2005)|DA|O(n2 log n)|
|Fortunato et al.|(Fortunato et al., 2004)|FLM|O(m3n)|
|Radicchi et al.|(Radicchi et al., 2004)|RCCLP|O(m4/n2)|
|Donetti & Mun˜oz|(Donetti and Mun˜oz, 2004, 2005)|DM/DMN|O(n3)|
|Bagrow & Bollt|(Bagrow and Bollt, 2005)|BB|O(n3)|
|Capocci et al.|(Capocci et al., 2005)|CSCC|O(n2)|
|Wu & Huberman|(Wu and Huberman, 2004)|WH|O(n + m)|
|Palla et al.|(Palla et al., 2005)|PK|O(exp(n))|
|Reichardt & Bornholdt|(Reichardt and Bornholdt, 2004)|RB|parameter dependent|


- TABLE I List of the algorithms used in the comparative analysis of Danon et al. (Danon et al., 2005). The ﬁrst column indicates the names of the algorithm designers, the second the original reference of the work, the third the symbol used to indicate the algorithm and the last the computational complexity of the technique. Adapted from Ref. (Danon et al., 2005).

|Author|Ref.|Label|Order|
|---|---|---|---|
|Girvan & Newman|(Girvan and Newman, 2002; Newman and Girvan, 2004)|GN|O(nm2)|
|Clauset et al.|(Clauset et al., 2004)|Clauset et al.|O(n log2 n)|
|Blondel et al.|(Blondel et al., 2008)|Blondel et al.|O(m)|
|Guimera` et al.|(Guimera` and Amaral, 2005; Guimera` et al., 2004)|Sim. Ann.|parameter dependent|
|Radicchi et al.|(Radicchi et al., 2004)|Radicchi et al.|O(m4/n2)|
|Palla et al.|(Palla et al., 2005)|Cﬁnder|O(exp(n))|
|Van Dongen|(Dongen, 2000a)|MCL|O(nk2), k < n parameter|
|Rosvall & Bergstrom|(Rosvall and Bergstrom, 2007)|Infomod|parameter dependent|
|Rosvall & Bergstrom|(Rosvall and Bergstrom, 2008)|Infomap|O(m)|
|Donetti & Mun˜oz|(Donetti and Mun˜oz, 2004, 2005)|DM|O(n3)|
|Newman & Leicht|(Newman and Leicht, 2007)|EM|parameter dependent|
|Ronhovde & Nussinov|(Ronhovde and Nussinov, 2009)|RN|O(mβ log n), β ∼ 1.3|


- TABLE II List of the algorithms used in the comparative analysis of Lancichinetti and Fortunato (Lancichinetti and Fortunato, 2009). The ﬁrst column indicates the names of the algorithm designers, the second the original reference of the work, the third the symbol used to indicate the algorithm and the last the computational complexity of the technique.


zout (6, 7 and 8), and represented the result for each algorithm as a group of three columns, indicating the average value of the similarity between the planted partition and the partition found by the method for each of the three zout-values. The similarity was measured in terms of the fraction of correctly classiﬁed vertices (Section XV.A). The comparison shows that modularity optimization via simulated annealing (Section VI.A.2) yields the best results, although it is a rather slow procedure, that cannot be applied to graphs of size of the order of 105 vertices or larger. On the other hand, we have already pointed out that the benchmark by Girvan and Newman is not a good representation of real graphs with community structure, which are characterized by heterogeneous distributions

of degree and community sizes. In this respect, the class of graphs designed by Lancichinetti et al. (LFR benchmark) (Lancichinetti et al., 2008) (Section XV.A) poses a far more severe test to clustering techniques. For instance, many methods have problems to detect clusters of very diﬀerent sizes (like most methods listed in Table I). For this reason, Lancichinetti and Fortunato have carried out a careful comparative analysis of community detection methods on the much more restrictive LFR benchmark (Lancichinetti and Fortunato, 2009). The algorithms chosen are listed in Table II. In Fig. 33 the performances of the algorithms on the LFR benchmark are compared. Whenever possible, tests on the versions of the LFR benchmark with directed edges, weighted edges

and/or overlapping communities (Lancichinetti and Fortunato, 2009) were carried out. Lancichinetti and Fortunato also tested the methods on random graphs, to check whether they are able to notice the absence of community structure. From the results of all tests, the Infomap method by Rosvall and Bergstrom (Rosvall and Bergstrom, 2008) appears to be the best, but also the algorithms by Blondel et al. (Blondel et al., 2008) and by Ronhovde and Nussinov (Ronhovde and Nussinov, 2009) have a good performance. These three methods are also very fast, with a complexity which is essentially linear in the system size, so they can be applied to large systems. On the other hand, modularity-based methods (with the exception of the method by Blondel et al.) have a rather poor performance, which worsens for larger systems and smaller communities, due to the well known resolution limit of modularity (Fortunato and Barth´elemy, 2007). The performance of the remaining methods worsens considerably if one increases the system size (DM and Infomod) or the community size (Cﬁnder, MCL and method by Radicchi et al.).

Fan et al. have evaluated the performance of some algorithms to detect communities on weighted graphs (Fan et al., 2007). The algorithms are: modularity maximization, carried out with extremal optimization (WEO) (Section VI.A.3); the Girvan-Newman algorithm (WGN) (Section V.A); the Potts model algorithm by Reichardt and Bornholdt (Potts) (Section VIII.A). All these techniques have been originally introduced for unweighted graphs, but we have shown that they can easily be extended to weighted graphs. The algorithms were tested on the weighted version of the benchmark of Girvan and Newman, that we discussed in Section XV.A. Edge weights have only two values: winter for inter-cluster edges and wintra for intra-cluster edges. Such values are linked by the relation wintra + winter = 2, so they are not independent. For testing one uses realizations of the benchmark with ﬁxed topology (i. e. ﬁxed zout) and variable weights. In Fig. 34 the comparative performance of the three algorithms is illustrated. The topology of the benchmark graphs corresponds to zout = 8, i. e. to graphs in which each vertex has approximately the same number of neighbors inside and outside its community. By varying winter from 0 to 2 one goes smoothly from a situation in which most of the weight is concentrated inside the clusters, to a situation in which instead the weight is concentrated between the clusters. From Fig. 34 we see that WEO and Potts are more reliable methods.

Sawardecker et al. have tested methods to detect overlapping communities (Sawardecker et al., 2009). They considered three algorithms: modularity optimization, the Clique Percolation Method (CPM) (Section XI.A) and the modularity landscape surveying method by Sales-Pardo et al. (Sales-Pardo et al., 2007) (Section XII.B). For testing, Sawardecker et al. deﬁned a class of benchmark graphs in which the linking probability between vertices is an increasing function of the number of clusters the vertices belong to. We have de-

- 0.8
- 1


- 0.8
- 1


Normalized Mutual Information

0.6

0.6

0.4

0.4

0.2

0.2

Blondel et al. MCL

0

0

0.2 0.4 0.6 0.8

0.2 0.4 0.6 0.8

- 0.8
- 1


- 0.8
- 1


|N=1000, S N=1000, B N=5000, S N=5000, B<br><br>|
|---|


0.6

0.6

0.4

0.4

0.2

0.2

Infomod Infomap

0

0

0.2 0.4 0.6 0.8

0.2 0.4 0.6 0.8

Mixing parameter t

- 0.8
- 1


- 0.8
- 1


N=1000, S N=1000, B N=5000, S N=5000, B

Normalized Mutual Information

0.6

0.6

Clauset et al.

0.4

0.4

0.2

0.2

Cfinder

0

0

0.2 0.4 0.6 0.8

0.2 0.4 0.6 0.8

- 0.8
- 1


- 0.8
- 1


0.6

0.6

0.4

0.4

Radicchi et al. Sim. ann.

0.2

0.2

0

0

0.2 0.4 0.6 0.8

0.2 0.4 0.6 0.8

Mixing parameter t

- 0.8
- 1


- 0.8
- 1


Normalized Mutual Information

0.6

0.6

0.4

0.4

0.2

0.2

GN DM

0

0

0 0.2 0.4 0.6 0.8

0 0.2 0.4 0.6 0.8

- 0.8
- 1


- 0.8
- 1


|N=1000, S N=1000, B N=5000, S N=5000, B<br><br>|
|---|


0.6

0.6

0.4

0.4

0.2

0.2

EM RN

0

0

0 0.2 0.4 0.6 0.8

0 0.2 0.4 0.6 0.8

Mixing parameter t

FIG. 33 Performances of several algorithms on the LFR benchmark (Lancichinetti and Fortunato, 2009). The plots show the normalized mutual information (in the version proposed in Ref. (Lancichinetti et al., 2009)) as a function of the mixing parameter of the benchmark graphs. The diﬀerent curves for each method refer to diﬀerent system sizes (1000 and 5000 vertices) and community size ranges [(S)=from 10 to 50 vertices, (B)=from 20 to 100 vertices]. For the GN algorithm only the smaller graph size was adopted, due to the high complexity of the method, whereas for the EM method there are eight curves instead of four because for each set of benchmark graphs the algorithm was run starting from two diﬀerent initial conditions. Reprinted ﬁgure with permission from Ref. (Lancichinetti and Fortunato, 2009). c 2009 by the American Physical Society.

|| |
|---|
|
|---|


|| |
|---|
|
|---|


- FIG. 34 Comparative evaluation of the performances of algorithms to ﬁnd communities in weighted graphs. Tests are carried out on a weighted version of the benchmark of Girvan and Newman. The two plots show how good the algorithms are in terms of the precision and accuracy with which they recover the planted partition of the benchmark. Precision indicates how close the values of similarity between the planted and the model partition are after repeated experiments with the same set of parameters; accuracy indicates how close the similarity values are to the ideal result (1) after repeated experiments with the same set of parameters. The similarity measure adopted here is based on the relative overlap of clusters of Eq. 97. We see that the maximization of modularity with extremal optimization (WEO) and the Potts model algorithm (Potts) are both precise and accurate as long as the weight of the inter-cluster edges winter remains lower than the weight of the intra-cluster edges (winter < 1). Reprinted ﬁgures with permission from Ref. (Fan et al., 2007). c 2007 by Elsevier.


scribed this benchmark in Section XV.A. It turns out that the modularity landscape surveying method is able to identify overlaps between communities, as long as the fraction of overlapping vertices is small. Curiously, the CPM, designed to ﬁnd overlapping communities, has a poor performance, as the overlapping vertices found by the algorithm are in general diﬀerent from the overlapping vertices of the planted partition of the benchmark. The authors also remark that, if the overlap between two clusters is not too small, it may be hard (for any method) to recognize whether the clusters are overlapping or hierarchically organized, i. e. loosely connected clusters within a large cluster.

We close the section with some general remarks concerning testing. We have seen that a testing procedure requires two crucial ingredients: benchmark graphs with built-in community structure and clustering algorithms that try to recover it. Such two elements are not independent, however, as they are both based on the concept of community. If the underlying notions of community for the benchmark and the algorithm are very diﬀerent, one can hardly expect that the algorithm will do a good job on the benchmark. Furthermore, there is a third element, i. e. the quality of a partition. All benchmarks start from a situation in which communities are clearly identiﬁed, i. e. connected components of the graph, and introduce some amount of noise, that eventually leads to a scenario where clusters are hardly or no longer detectable. It is then important to keep track of how the quality of the natural partition of the benchmark worsens as the amount of noise increases, in order to distinguish conﬁgurations in which the graphs have a cluster structure, that an algorithm should then be able to resolve, from conﬁgurations in which the noise prevails and the natural clusters are not meaningful. Moreover, quality functions are important to evaluate the performance of an algorithm on graphs whose community structure is unknown. Quality functions are strongly related to the concept of community as well, as they are supposed to evaluate the goodness of the clusters, so they require a clear quantitative concept of what a cluster is. It is very important for any testing framework to check for the mutual dependencies between the benchmark, the quality function used to evaluate partitions, and the clustering algorithm to be tested. This issue has so far received very little attention (Delling et al., 2007). Finally, empirical tests are also very important, as one ultimately wishes to apply clustering techniques to real graphs. Therefore, it is crucial to collect more data sets of graphs whose community structure is known or deducible from information on the vertices and their edges.

###### XVI. GENERAL PROPERTIES OF REAL CLUSTERS

What are the general properties of partitions and clusters of real graphs? In many papers on graph clustering applications to real systems are presented. In spite of the

100

|amazon0308 guide, α=−2.045<br><br>|
|---|


10−1

1−cdf, P(k>x)

10−2

10−3

10−4

100 101 102 103 104 105 106

community size

- FIG. 35 Cumulative distribution of community sizes for the Amazon purchasing network. The partition is derived by greedy modularity optimization. Reprinted ﬁgure with permission from Ref. (Clauset et al., 2004). c 2004 by the American Physical Society.


variety of clustering methods that one could employ, in many cases partitions derived from diﬀerent techniques are rather similar to each other, so the general properties of clusters do not depend much on the particular algorithm used. The analysis of clusters and their properties delivers a mesoscopic description of the graph, where the communities, and not the vertices, are the elementary units of the topology. The term mesoscopic is used because the relevant scale here lies between the scale of the vertices and that of the full graph.

One of the ﬁrst issues addressed was whether the communities of a graph are usually about of the same size or whether the community sizes have some special distribution. Most clustering techniques consistently ﬁnd skewed distributions of community sizes, with a tail described with good approximation by a power law (at least, a sizeable portion of the curve) with exponents in the range between 1 and 3 (Clauset et al., 2004; Danon et al., 2007; Newman, 2004a; Palla et al., 2005; Radicchi et al., 2004). So, there seems to be no characteristic size for a community: small communities usually coexist with large ones. As an example, Fig. 35 shows the cumulative distribution of community sizes for a recommendation network of the online vendor Amazon.com. Vertices are products and there is a connection between item A and B if B was frequently purchased by buyers of A. Recall that the cumulative distribution is the integral of the probability distribution: if the cumulative distribution is a power law s−α, the probability distribution is also a power law with exponent −(α + 1).

Leskovec et al. (Leskovec et al., 2008) have gone one step further. They carried out a systematic analysis of communities in large real networks, including traditional and on-line social networks, technological, information

networks and web graphs. The main goal was to assess the quality of communities at various sizes. As a quality function the conductance of the cluster was chosen. We remind that the conductance of a cluster is the ratio between the cut size of the cluster and the minimum between the total degree of the cluster and that of the rest of the graph (Section IV.A). So, if the cluster is much smaller than the whole graph, the conductance equals the ratio between the cut size and the total degree of the cluster. Since a “good” cluster is characterized by a low cut size and a large internal density of edges, low values of the conductance indicate good clusters. For each real network Leskovec et al. derived the network community proﬁle plot (NCPP), showing the minimum conductance score among subgraphs of a given size as a function of the size. Interestingly, they found that the NCPPs of all networks they studied have a characteristic shape: they go downwards up until subgraphs with about 100 vertices, and then they rise monotonically for larger subgraphs (Fig. 36). This seems to suggest that communities are well deﬁned only when they are fairly small in size. Such small clusters are weakly connected to the rest of the graph, often by a single edge (in this case they are called whiskers), and form the periphery of the network. The other vertices form a big core, in which larger clusters are well connected to each other, and are therefore barely distinguishable (Fig. 36). Leskovec et al. performed low-conductance cuts with several methods, to ensure that the result is not a simple artefact of a particular chosen technique. Moreover, they have also veriﬁed that, for large real networks with known community structure (such as, e.g., the social network of the on-line blogging site LiveJournal, with its user groups), the NCPP has the same qualitative shape if one takes the real communities instead of low-conductance subgraphs. The analysis by Leskovec et al. may shed new light on our understanding of community structure and its detection in large networks. The fact that the “best” communities appear to have a characteristic size of about 100 vertices is consistent with Dunbar conjecture that 150 is the upper size limit for a working human community (Dunbar, 1998). On the other hand, if large communities are very mixed with each other, as Leskovec et al. claim, they could hardly be considered communities, and the alleged “community structure” of large networks would be limited to their peripheral region. The results by Leskovec et al. may be aﬀected by the properties of conductance, and need to be validated with alternative approaches. In any case, whatever the value of the quality score of a cluster may be (low or high), it is necessary to estimate the signiﬁcance of the cluster (Section XIV), before deciding whether it is a meaningful structure or not.

If the community structure of a graph is known, it is possible to classify vertices according to their roles within their community, which may allow to infer individual properties of the vertices. A promising classiﬁcation has been proposed by Guimer` and Amaral (Guimer` and Amaral, 2005; Guimer` and Amaral, 2005). The

![image 71](Community Detection in Graphs_images/imageFile71.png)

![image 72](Community Detection in Graphs_images/imageFile72.png)

![image 73](Community Detection in Graphs_images/imageFile73.png)

![image 74](Community Detection in Graphs_images/imageFile74.png)

![image 75](Community Detection in Graphs_images/imageFile75.png)

![image 76](Community Detection in Graphs_images/imageFile76.png)

![image 77](Community Detection in Graphs_images/imageFile77.png)

![image 78](Community Detection in Graphs_images/imageFile78.png)

![image 79](Community Detection in Graphs_images/imageFile79.png)

![image 80](Community Detection in Graphs_images/imageFile80.png)

![image 81](Community Detection in Graphs_images/imageFile81.png)

![image 82](Community Detection in Graphs_images/imageFile82.png)

- FIG. 36 Analysis of communities in large real networks by Leskovec et al. (Leskovec et al., 2008). (Left) Typical shape of the network community proﬁle plot (NCPP), showing how the minimum conductance of subgraphs of size n varies with n. The plot indicates that the “best” communities have a size of about 100 vertices (minimum of the curve), whereas communities of larger sizes are not well-deﬁned. In the plot two other NCPPs are shown: the one labeled Rewired network corresponds to a randomized version of the network, where edges are randomly rewired by keeping the degree distribution; the one labeled Bag of whiskers gives the minimum conductance scores of clusters composed of disconnected pieces. (Right) Scheme of the core-periphery structure of large social and information networks derived by Leskovec et al. based on the results of their empirical analysis. Most of the vertices are in a central core, which does not have a clear community structure, whereas the best communities, which are rather small, are weakly connected to the core. Reprinted ﬁgure with permission from Ref. (Leskovec et al., 2008).


role of a vertex depends on the values of two indices, the within-module degree and the participation ratio (though other variables may be chosen, in principle). The withinmodule degree zi of vertex i is deﬁned as

κi − κ¯s

i

, (98)

zi =

###### σκ

si

![image 83](Community Detection in Graphs_images/imageFile83.png)

FIG. 37 Regions of the z − P plane deﬁning the roles of vertices in the modular structure of a graph, according to the scheme of Guimera` and Amaral (Guimer`a and Amaral, 2005; Guimera` and Amaral, 2005). Reprinted ﬁgure with permission from Ref. (Guimera` and Amaral, 2005). c 2005 by the Nature Publishing Group.

###### and σκ

###### where κi is the internal degree of i in its cluster si, κ¯s

i

the average and standard deviation of the internal

si

degrees for all vertices of cluster si. The within-module degree is then deﬁned as the z-score of the internal degree

κi. Large values of z indicate that the vertex has many more neighbors within its community than most other vertices of the community. Vertices with z ≥ 2.5 are classiﬁed as hubs, if z < 2.5 they are non-hubs. The participation ratio Pi of vertex i is deﬁned as

nc

Pi = 1 −

s=1

κis ki

2

. (99)

Here κis is the internal degree of i in cluster s, ki the degree of i. Values of P close to 1 indicate that the neighbors of the vertex are uniformly distributed among all clusters; if all neighbors are within the cluster of the vertex, instead, P = 0. Based on the values of the pair (z,P), Guimer` and Amaral distinguished seven roles for the vertices. Non-hub vertices can be ultraperipheral (P ≈ 0), peripheral (P < 0.625), connectors (0.625 < P < 0.8) and kinless vertices (P > 0.8). Hub vertices are classiﬁed in provincial hubs (P <∼ 0.3), connector hubs (0.3 < P < 0.75) and kinless hubs (P > 0.75). The regions of the z − P plane corresponding to the seven roles are highlighted in Fig. 37. We stress that the actual boundaries of the regions can be chosen rather arbitrarily. On graphs without community structure, like Erd¨s-R´enyi (Erd¨s and R´enyi, 1959)

random graphs and Barab´si-Albert (Barab´si and Albert, 1999) graphs (Section A.3), non-hubs are mostly kinless vertices. In addition, if there are hubs, like in Barab´si-Albert graphs, they are kinless hubs. Kinless hubs (non-hubs) vertices have less than half (one third) of their neighbors inside any cluster, so they are not clearly associated to a cluster. On real graphs, the topological roles can be correlated to functions of vertices: in metabolic networks, for instance, connector hubs, which share most edges with vertices of other clusters than their own, are often metabolites which are more conserved across species than other metabolites, i. e. they have an evolutionary advantage (Guimer` and Amaral, 2005).

If communities are overlapping, one can explore other statistical properties, like the distributions of the overlaps and of the vertex memberships. The overlap is deﬁned as the number of vertices shared by each pair of overlapping clusters; the membership of a vertex is the number of communities including the vertex. Both distributions turn out to be skewed, so there seem to be no characteristic values for the overlap and the membership. Moreover, one could derive a network, where the communities are the vertices and pairs of vertices are connected if their corresponding communities overlap (Palla et al.,

- 2005). Such networks seem to have some special properties. For instance, the degree distribution is a particular function, with an initial exponential decay followed by a slower power law decay31. We stress that the above results have been obtained with the Clique Percolation Method by Palla et al. (Section XI.A) and it is not clear whether other techniques would conﬁrm them or not. In a recent analysis it has been shown that the degree distribution of the network of communities can be reproduced by assuming that the graph grows according to a simple preferential attachment mechanism, where communities with large degree have an enhanced chance to interact/overlap with new communities (Pollner et al.,
- 2006).


###### XVII. APPLICATIONS ON REAL-WORLD NETWORKS

The ultimate goal of clustering algorithms is trying to infer properties of and relationships between vertices, that are not available from direct observation/measurement. If the scientiﬁc community agrees on a set of reliable techniques, one could then proceed with careful investigations of systems in various domains. So far, most works in the literature on graph clustering focused on the development of new algorithms, and applications were limited to those few benchmark graphs that one typically uses for testing (Section XV.A). Still, there

- 31 This holds for the networks considered by Palla et al. (Palla et al.,


2005) like, e. g., the word association network (Section II) and a coauthorship network of physicists. There is no a priori reason to believe that this result is general.

are also applications aiming at understanding real systems. Some results have been actually mentioned in the previous sections. This section is supposed to give a ﬂavor of what can be done by using clustering algorithms. Therefore, the list of works presented here is by no means exhaustive. Most studies focus on biological and social networks. We mention a few applications to other types of networks as well.

A. Biological networks

The recent abundance of genomic data has allowed us to explore the cell at an unprecedented depth. A wealth of information is available on interactions involving proteins and genes, metabolic processes, etc. In order to study cellular systems, the graph representation is regularly used. Protein-protein interaction networks (PIN), gene regulatory networks (GRN) and metabolic networks (MN) are meanwhile standard objects of investigation in biology and bioinformatics (Junker and Schreiber, 2008).

Biological networks are characterized by a remarkable modular organization, reﬂecting functional associations between their components. For instance, proteins tend to be associated in two types of cellular modules: protein complexes and functional modules. A protein complex is a group of proteins that mutually interact at the same time and space, forming a sort of physical object. Examples are transcription factor complexes, protein transport and export complexes, etc. Functional modules instead are groups of proteins taking place in the same cellular process, even if the interactions may happen at different times and places. Examples are the CDK/cyclin module, responsible for cell-cycle progression, the yeast pheromone response pathway, etc.. Identifying cellular modules is fundamental to uncover the organization and dynamics of cell functions. However, the information on cell units (e. g. proteins, genes) and their interactions is often incomplete, or even incorrect, due to noise in the data produced by the experiments. Therefore, inferring modules from the topology of cellular networks enables one to restrict the set of possible scenarios and can be a safe guide for future experiments.

Rives and Galitski (Rives and Galitski, 2003) studied the modular organization of a subset of the PIN of the yeast (Saccharomyces cerevisiae), consisting of the (signaling) proteins involved in the processes leading the microorganism to a ﬁlamentous form. The clusters were detected with a hierarchical clustering technique. Proteins mostly interacting with members of their own cluster are often essential proteins; edges between modules are important points of communication. Spirin and Mirny (Spirin and Mirny, 2003) identiﬁed protein complexes and functional modules in yeast with diﬀerent techniques: clique detection, superparamagnetic clustering (Blatt et al., 1996) and optimization of cluster edge density. They estimated the statistical signiﬁcance of the clusters by computing the p-values of seeing those clus-

ters in random graphs with the same expected degree sequence as the original network. From the known functional annotations of yeast genes one can see that the modules usually group proteins with the same or consistent biological functions. Indeed, in many cases, the modules exactly coincide with known protein complexes. The results appear robust if noise is introduced in the system, to simulate the noise present in the experimental data. Functional modules in yeast were also found by Chen and Yuan (Chen and Yuan, 2006), who applied the algorithm by Girvan and Newman with a modiﬁed deﬁnition of edge betweenness (Section V.A). The standard Girvan-Newman algorithm has proved to be reliable to detect functional modules in PINs (Dunn et al., 2005). The novelty of the work by Chen and Yuan is its focus on weighted PINs, where the weights come from information derived through microarray expression proﬁles. Weights add information about the system and should lead to a more reliable modular structure. By knocking out genes in the same structural cluster similar phenotypes appeared, suggesting that the genes have similar biological roles. Moreover, the clusters often contained known protein complexes, either entirely or to a large extent. Finally, Chen and Yuan were able to make predictions of the unknown function of some genes, based on the structural module they belong to: gene function prediction is the most promising outcome deriving from the application of clustering techniques to PINs. Farutin et al. (Farutin et al., 2006) have adopted a local concept of community, and derived a hierarchical decomposition of PINs, in that the modules identiﬁed at some level become the vertices of a network at the higher level. Communities are overlapping, to account for the fact that proteins (and whole modules) may have diverse biological functions. High level structures detected in a human PIN correspond to general biological concepts like signal transduction, regulation of gene expression, intercellular communication. Sen et al. (Sen et al., 2006) identiﬁed protein clusters for yeast from the eigenvectors of the Laplacian matrix (Section A.2), computed via Singular Value Decomposition. In a recent analysis, Lewis et al. (Lewis

- et al., 2009) carefully explored the relationship between structural communities of PINs and their biological function. Communities were detected with the multiresolution approach by Reichardt and Bornholt (Reichardt and Bornholdt, 2006a) (Section VI.B). A community is considered biologically homogeneous if the functional similarity between protein pairs of the community (extracted through the Gene Ontology database (Ashburner et al.,


- 2000)) is larger than the functional similarity between all protein pairs of the network. Lewis et al. also speciﬁed the comparison to interacting and non-interacting protein pairs. As a result, many communities turn out to be biologically homogeneous, especially if they are not too small. Moreover, some topological attributes of communities, like the within-community clustering coeﬃcient (i.e. the average value of the clustering coeﬃcients of the vertices of a community, computed by considering


just the neighbors belonging to the community) and link density (density of internal edges), are good indicators of biological homogeneity: the former is strongly correlated with biological homogeneity, independently of the community size, whereas for the latter the correlation is strong for large communities.

Metabolic networks have also been extensively investigated. We have already discussed the “functional cartography” designed by Guimer` and Amaral (Guimer` and Amaral, 2005; Guimer` and Amaral, 2005), which applies to general types of networks, not necessarily metabolic.

- A hierarchical decomposition of metabolic networks has been derived by Holme et al. (Holme et al., 2003), by using a hierarchical clustering technique inspired by the algorithm by Girvan and Newman (Section V.A). Here, vertices are removed based on their betweenness values, which are obtained by dividing the standard site betweenness scores (Freeman, 1977) by the indegree of the respective vertices. A picture of metabolic network emerges, in which there are core clusters centered at hub-substances, surrounded by outer shells of less connected substances, and a few other clusters at intermediate scales. In general, clusters at diﬀerent scales seem to be meaningful, so the whole hierarchy should be taken into account.

Wilkinson and Huberman (Wilkinson and Huberman, 2004) analyzed a network of gene co-occurrence to ﬁnd groups of related genes. The network is built by connecting pairs of genes that are mentioned together in the abstract of articles of the Medline database (http://medline.cos.com/). Clusters were found with a modiﬁed version of the algorithm by Girvan and Newman, in which edge betweenness is computed by considering the shortest paths of a small subset of all vertex pairs, to gain computer time (Section V.A). As a result, genes belonging to the same cluster turn out to be functionally related to each other. Co-occurrence of terms is also used to extract associations between genes and diseases, to ﬁnd out which genes are relevant for a speciﬁc disease. Communities of genes related to colon cancer can be helpful to identify the function of the genes.

- B. Social networks


Networks depicting social interactions between people have been studied for decades (Scott, 2000; Wasserman and Faust, 1994). Recently the modern Information and Communication Technology (ICT) has opened new interaction modes between individuals, like mobile phone communications and online interactions enabled by the Internet. Such new social exchanges can be accurately monitored for very large systems, including millions of individuals, whose study represents a huge opportunity for social science. Communities of social networks can be friendship circles, groups of people sharing common interests and/or activities, etc..

Blondel et al. have analyzed a network of mobile phone

![image 84](Community Detection in Graphs_images/imageFile84.png)

FIG. 38 Community structure of a social network of mobile phone communication in Belgium. Dots indicate subcommunities at the lower hierarchical level (with more than 100 people) and are colored in a red-green scale to represent the level of representation of the two main languages spoken in Belgium (red for French and green for Dutch). Communities of the two larger groups are linguistically homogeneous, with more than 85% of people speaking the same language. Only one community (zoomed), which lies at the border between the two main aggregations, has a more balanced distribution of languages. Reprinted ﬁgure with permission from Ref. (Blondel et al., 2008). c 2008 by IOP Publishing and SISSA.

communications between users of a Belgian phone operator (Blondel et al., 2008). The vertices of the graph are 2.6 millions and the edges are weighted by the cumulative duration of phone calls between users in the observation time frame. The clustering analysis, performed with a fast hierarchical modularity optimization technique developed by the authors (discussed in Section VI.A.1), delivers six hierarchical levels. The highest level consists of 261 groups with more than 100 vertices, which are clearly arranged in two main groups, linguistically homogeneous, reﬂecting the linguistic split of Belgian population (Fig. 38). Tyler et al. (Tyler et al., 2003) studied a network of e-mail exchanges between people working

- at HP Labs. They applied the same modiﬁed version of Girvan-Newman algorithm that two of the authors have used to ﬁnd communities of related genes (Wilkinson and Huberman, 2004) (Section XVII.A). The method enables one to measure the degree of membership of each vertex in a community and allows for overlaps between communities. The detected clusters matched quite closely the organization of the Labs in departments and project groups, as conﬁrmed by interviews conducted with re-


![image 85](Community Detection in Graphs_images/imageFile85.png)

FIG. 39 Communities in social networking sites. (Top) Visualization of a network of friendships between students at Caltech, constructed from Facebook data (September 2005). The colors/shapes indicate the dormitories (Houses) of the students. (Bottom) Topological communities of the network, which are quite homogeneous with respect to House aﬃliation. Reprinted ﬁgures with permission from Refs. (Porter et al., 2009) and (Traud et al., 2008).

searchers.

Social networking sites, like Myspace (www.myspace.com), Friendster (www.friendster.com), Facebook (www.facebook.com), etc. have become extremely popular in the last years. They are online platforms that allow people to communicate with friends, send e-mails, solicit opinions on speciﬁc issues, spread ideas and/or fads, etc. Traud et al. (Traud et al., 2008) used anonymous Facebook data to create networks of friendships between students of diﬀerent American universities, where vertices/students are connected if they are friends on Facebook. Communities were detected by applying a variant of Newman’s spectral optimization

of modularity (Section VI.A.4): the results were further reﬁned through additional steps ´ la Kernighan-Lin (Section IV.A). One of the goals of the study was to infer relationships between the online and oﬄine lives of the students. By using demographic information on the students’ populations, one ﬁnds that communities are organized by class year or by House (dormitory) aﬃliation, depending on the university (Fig. 39). Yuta et al. (Yuta et al., 2007) observed a gap in the community size distribution of a friendship network extracted from mixi (mixi.jp), the largest social networking site in Japan (as of December 2006). Communities were identiﬁed with the fast greedy modularity optimization by Clauset et al. (Clauset et al., 2004). The gap occurs in the intermediate range of sizes between 20 and 400, where but a few communities are observed. Yuta et al. introduced a model where people form new friendships both by “closing” ties with people who are friends of friends, and by setting new links with individuals having similar interests. In this way most groups turn out to be either small or large, and medium size groups are rare.

Collaboration networks, in which individuals are linked if they are (were) involved in a common activity, have been often studied because they embed an implicit objective concept of acquaintance, that is not easy to capture in direct social experiments/interviews. For instance, somebody may consider another individual a friend, while the latter may disagree. A collaboration instead is a proof of a social relationship between individuals. The analysis of the structure of scientiﬁc collaboration networks (Newman, 2001) has exerted a big inﬂuence on the development of the modern network science. Scientiﬁc collaboration is associated to coauthorship: two scientists are linked if they have coauthored at least one paper together. Information about coauthorships can be extracted from diﬀerent databases of research papers. Communities indicate groups of people with common research interests, i. e. topical or disciplinary groups. In the seminal paper by Girvan and Newman (Girvan and Newman, 2002), the authors applied their method on a collaboration network of scientists working at the Santa Fe Institute, and were able to discriminate between research divisions (Fig. 2b). The community structure of scientiﬁc collaboration networks has been investigated by many authors (Danon et al., 2006; Donetti and Mun˜oz, 2004; Duch and Arenas, 2005; Farkas et al., 2007; Gregory, 2007; Lehmann and Hansen, 2007; Nepusz et al.,

- 2008; Newman, 2004b, 2006a; Noack and Rotta, 2009; Palla et al., 2007, 2005; Pujol et al., 2006; Radicchi et al., 2004; Reichardt and Bornholdt, 2006a; Richardson et al.,
- 2009; S.-W. Son et al., 2006; Shen et al., 2009; Vragovic´ and Louis, 2006; White and Smyth, 2005; Zhou, 2003b). Other types of collaboration networks have been studied too. Gleiser and Danon (Gleiser and Danon, 2003) considered a collaboration network of jazz musicians. Vertices are either musicians, connected if they played in the same band, or bands, connected if they have a musician in common. By applying the algorithm of Girvan and


Newman they found that communities reﬂect both racial segregation (with two main groups comprising only black or white players) and geographical separation, due to the diﬀerent recording locations.

C. Other networks

Citation networks (de Solla Price, 1965) have been regularly used to understand the citation patterns of authors and to disclose relationships between disciplines. Rosvall and Bergstrom (Rosvall and Bergstrom, 2008) used a citation network of over 6000 scientiﬁc journals to derive a map of science. They used a clustering technique based on compressing the information on random walks taking place on the graph (Section IX.B). A random walk follows the ﬂow of citations from one ﬁeld to another, and the ﬁelds emerge naturally from the clustering analysis (Fig. 40). The structure of science resembles the letter U, with the social sciences and engineering at the terminals, joined through a chain including medicine, molecular biology, chemistry and physics.

Reichardt and Bornholdt (Reichardt and Bornholdt, 2007) performed a clustering analysis on a network built from bidding data taken from the German version of Ebay (www.ebay.de), the most popular online auction site. The vertices are bidders and two vertices are connected if the corresponding bidders have expressed interest for the same item. Clusters were detected with the multiresolution modularity optimization developed by the authors themselves (Reichardt and Bornholdt, 2006a) (Section VI.B). In spite of the variety of items that it is possible to purchase through Ebay, about 85% of bidders were classiﬁed into a few major clusters, reﬂecting bidders’ broad categories of interests. Ebay data were also examined by Jin et al. (Jin et al., 2007), who considered bidding networks where the vertices are the individual auctions and edges are placed between auctions having at least one common bidder. Communities, detected with greedy modularity optimization (Newman, 2004b) (Section VI.A.1), allow to identify substitute goods, i. e. products that have value for the same bidder, so that they can be purchased together or alternatively.

Legislative networks enable one to deduce associations between politicians through their parliamentary activity, which may be related or not to party aﬃliation. Porter and coworkers have carried out numerous studies on the subject (Porter et al., 2007, 2005; Zhang et al., 2008), by using data on the Congress of the United States. In Refs. (Porter et al., 2007, 2005), they examined the community structure of networks of committees in the US House of Representatives. Committees sharing common members are connected by edges, which are weighted by dividing the number of common members by the number one would expect to have if committee memberships were randomly assigned. Hierarchical clustering (Section IV.B) reveals close connections between some of the committees. In another work (Zhang et al., 2008),

Fluid Mechanics

Material Engineering

Circuits

Computer Science

Geosciences

Tribology

Operations Research

Astronomy & Astrophysics

Computer Imaging

Mathematics

Power Systems

Physics

Telecommunication

Electromagnetic Engineering

Control Theory

Chemical Engineering

Probability & Statistics

Chemistry

Environmental Chemistry & Microbiology

Applied Acoustics

Business & Marketing Analytic Chemistry

Geography

Economics

Psychology

Sociology

Crop Science

Education

Ecology & Evolution

Pharmacology

Political Science

Neuroscience

Agriculture

Law

Psychiatry

Environmental Health

Medical Imaging

Anthropology

###### Molecular & Cell Biology

Orthopedics Veterinary

Parasitology

Dentistry

Medicine

Citation ﬂow within ﬁeld

Ophthalmology

Otolaryngology

Citation ﬂow from B to A

Gastroenterology

###### B

A

Urology

Pathology

Dermatology

Rheumatology

Citation ﬂow from A to B

Citation ﬂow out of ﬁeld

- FIG. 40 Map of science derived from a clustering analysis of a citation network comprising more than 6000 journals. Reprinted ﬁgure with permission from Ref. (Rosvall and Bergstrom, 2008). c 2008 by the National Academy of Science of the USA.


Zhang et al. analyzed networks of legislation cosponsorship, in which vertices are legislators and two legislators are linked if they support at least one common bill. Communities, identiﬁed with a modiﬁcation of Newman’s spectral optimization of modularity (Section VI.A.4), are correlated with party aﬃliation, but also with geography and committee memberships of the legislators.

Networks of correlations between time series of stock returns have received a growing attention in the past few years (Mantegna, 1999). In early studies, scholars found clusters of correlated stocks by computing the maximum spanning tree of the network (Bonanno et al., 2003, 2000; Onnela et al., 2003, 2002) (Section A.1), and realized

that such clusters match quite well the economic sectors of the stocks. More recently, the community structure of the networks has been investigated by means of proper clustering algorithms. Farkas et al. (Farkas et al., 2007) have applied the weighted version of the Clique Percolation Method (Section XI.A) and found that the presence of two strong (i. e. carrying high correlation) edges in triangles is usually accompanied by the presence of a strong third edge. Heimo et al. (Heimo et al., 2008) used the weighted version of the multiresolution method by Reichardt and Bornholdt (Reichardt and Bornholdt, 2006a) (Section VI.B). Clusters correspond to relevant business sectors, as indicated by Forbes classiﬁcation; moreover,

smaller clusters at lower hierarchical levels seem to correspond to (economically) meaningful substructures of the main clusters.

###### XVIII. OUTLOOK

Despite the remote origins and the great popularity of the last years, research on graph clustering has not yet given a satisfactory solution of the problem and leaves us with a number of important open issues. From our exposition it appears that the ﬁeld has grown in a rather chaotic way, without a precise direction or guidelines. In some cases, interesting new ideas and tools have been presented, in others existing methods have been improved, becoming more accurate and/or faster.

What the ﬁeld lacks the most is a theoretical framework that deﬁnes precisely what clustering algorithms are supposed to do. Everybody has his/her own idea of what a community is, and most ideas are consistent with each other, but, as long as there is still disagreement, it remains impossible to decide which algorithm does the best job and there will be no control on the creation of new methods. Therefore, we believe that the ﬁrst and foremost task that the scientiﬁc community working on graph clustering has to solve in the future is deﬁning a set of reliable benchmark graphs, against which algorithms should be tested (Section XV.A). Deﬁning a benchmark goes far beyond the issue of testing. It means designing practical examples of graphs with communities, and, in order to do that, one has to agree on the fundamental concepts of community and partition. Clustering algorithms have to be devised consistently with such deﬁnitions, in order to give the best performance on the set of designated benchmarks, which represent a sort of ground truth. The explosion in the number of algorithms we have witnessed in recent times is due precisely to the present lack of reliable mechanisms of control of their quality and comparison of their performances. If the community agrees on a benchmark, the future development of the ﬁeld will be more coherent and the progress brought by new methods can be evaluated in an unbiased manner. The planted -partition model (Condon and Karp,

- 2001) is the easiest recipe one can think of when it comes to deﬁning clusters, and is the criterion underlying wellknown benchmarks, like that by Girvan and Newman. We believe that the new benchmarks have to be deﬁned along the same lines. The benchmark graphs recently introduced by Lancichinetti et al. (Lancichinetti and Fortunato, 2009; Lancichinetti et al., 2008) and by Sawardecker et al. (Sawardecker et al., 2009) are an important step in this direction.


Deﬁning a benchmark implies specifying the “natural” partition of a graph, the one that any algorithm should ﬁnd. This issue in turn involves the concept of quality of a partition, that has characterized large part of the development of the ﬁeld, in particular after the introduction of Newman-Girvan modularity (Section III.C.2).

Estimating the quality of a partition allows to discriminate among the large number of partitions of a graph. In some cases this is not diﬃcult. For instance, in the benchmark by Girvan and Newman there is a single meaningful partition, and it is hard to argue with that. But most graphs of the real world have a hierarchical structure, with communities including smaller communities and so on. Hence there are several meaningful partitions, corresponding to diﬀerent hierarchical levels, and discriminating among them is hard, as they may be all relevant, in a sense. If we consider the human body, we cannot say that the organization in tissues of the cells is more important than the organization in organs. We have seen that there are recent methods dealing with the problem of ﬁnding meaningful hierarchical levels (Section XII). Such methods rank the hierarchical partitions based on some criterion and one can assess their relevance through the ranking. One may wonder whether it makes sense sorting out levels, which means introducing a kind of threshold on the quality index chosen to rank partitions (to distinguish “good” from “bad” partitions), or whether it is more appropriate to keep the information given by the whole set of hierarchical partitions. The work by Clauset et al. on hierarchical random graphs (Clauset et al., 2007; Clauset et al., 2008), discussed in Section XII.B, indirectly raises this issue. There it was shown that the ensemble of model graphs, represented by dendrograms, encodes most of the information on the structure of the graph at study, like its degree distribution, transitivity and distribution of shortest path lengths. At the same time, by construction, the model reveals the whole hierarchy of communities, without any distinction between good and bad partitions. The information given by a dendrogram may become redundant and confusing when the graph is large, as then there is a big number of partitions. This is actually the reason why quality functions were originally introduced. However, in that case, one was dealing with artiﬁcial hierarchies, produced by techniques that systematically yield a dendrogram as a result of the analysis (like, e. g., hierarchical clustering), regardless of whether the graph actually has a hierarchical structure or not. Here instead we speak of real hierarchy, which is a fundamental element of real graphs and, as such, it must be considered in any serious approach to graph clustering. Any good clustering method must be able to tell whether a graph has community structure or not, and, in the ﬁrst case, whether the community structure is hierarchical (i. e. with two or more levels) or ﬂat (one level). We expect that the concept of hierarchy will become a key ingredient of future clustering techniques. In particular, assessing the consistence of the concepts of partitions’ quality and hierarchical structure is a major challenge.

A precise deﬁnition of null models, i. e. of graphs without community structure, is also missing. This aspect is extremely important, though, as deﬁning communities also implies deciding whether or not they exist in a speciﬁc graph. At the moment, it is generally accepted that

random graphs have no communities. The null model of modularity (Section III.C.2), by far the most popular, comprises all graphs with the same expected degree sequence of the original graph and random rewiring of edges. This class of graphs is characterized, by construction, by the fact that any vertex can be linked to any other, as long as the constraint on the degree sequence is satisﬁed. But this is by no means the only possibility. A community can be generically deﬁned as a subgraph whose vertices have a higher probability to be connected to the other vertices of the subgraph than to external vertices. The planted -partition model (Condon and Karp, 2001) is based on this principle, as we have seen. However, this does not mean that the linking probabilities of a vertex with respect to the other vertices in its community or in diﬀerent communities be constant (or simply proportional to their degrees, as in the conﬁguration model ( Luczak, 1992; Molloy and Reed, 1995)). In fact, in large networks it is reasonable to assume that the probability that a vertex is linked to most vertices is zero, as the vertex “ignores” their existence. This does not exclude that the probability that the vertex gets connected to the “known” vertices is the same (or proportional to their degrees), in which case the graph would still be random and have no communities. We believe that we are still far from a precise deﬁnition and a complete classiﬁcation of null models. This represents an important research line for the future of the ﬁeld, for three main reasons: 1) to better disentangle “true” communities from byproducts of random ﬂuctuations; 2) to pose a stringent test to existing and future clustering algorithms, whose reliability would be questionable if they found “false positives” in null model graphs; 3) to handle “hybrid” scenarios, where a graph displays community structure on some portions of it, while the rest is essentially random and has no communities.

In the previous chapters we have seen a great number of clustering techniques. Which one(s) shall we use? At the moment the scientiﬁc community is unable to tell. Modularity optimization is probably the most popular method, but the results of the analysis of large graphs are likely to be unreliable (Section VI.C). Nevertheless, people have become accustomed to use it, and there have been several attempts to improve the measure. A newcomer, who wishes to ﬁnd clusters in a given network and is not familiar with clustering techniques, would not know, oﬀ-hand, which method to use, and he/she would hardly ﬁnd indications about good methods in any single paper on graph clustering, except perhaps on the method presented in the paper. So, people keep using algorithms because they have heard of them, or because they know that other people are using them, or because of the reputation of the scientists who designed them. Waiting for future reliable benchmarks, that may give an objective assessment of the quality of the algorithms, there are at the moment hardly solid reasons to prefer an algorithm to another: the comparative analyses by Danon et al. (Danon et al., 2005) and by Lancichinetti and Fortu-

nato (Lancichinetti and Fortunato, 2009) (Section XV.C) represent a ﬁrst serious assessment of this issue. However, we want to stress that there is no such thing as the perfect method, so it is pointless to look for it. Among the other things, if one tries to look for a very general method, that should give good results on any type of graphs, one is inevitably forced to make very general assumptions on the structure of the graph and on the properties of communities. In this way one neglects a lot of speciﬁc features of the system, that may lead to a more accurate detection of the clusters. Informing a method with features characterizing some types of graphs makes it far more reliable to detect the community structure of those graphs than a general method, even if its applicability may be limited. Therefore in the future we envision the development of domain-speciﬁc clustering techniques. The challenge here is to identify the peculiar features of classes of graphs, which are bound to become crucial ingredients in the design of suitable algorithms. Some of the methods available today are actually based on assumptions that hold only for some speciﬁc categories of graphs. The Clique Percolation Method by Palla et al. (Palla et al., 2005), for instance, may work well for graphs characterized by a large number of cliques, like certain social networks, whereas it may give poor results otherwise.

Moving one step further, one should learn how to use speciﬁc information about a graph, whenever available, e. g. properties of vertices and/or partial information about their classiﬁcation. For instance, it may be that one has some information on a subset of vertices, like demographic data on people of a social network, and such data may highlight relationships between people that are not obvious from the network of social interactions. In this case, using only the social network may be reductive and ideally one should exploit both the structural and the non-structural information in the search of clusters, as the latter should be consistent with both inputs. How to do this is an open problem. The scientiﬁc community has just begun to study this aspect (Allahverdyan and Galstyan, 2009).

Most algorithms in the literature deal with the “classical” case of a graph with undirected and unweighted edges. This is certainly the simplest case one could think of, and graph clustering is already a complex task on such types of graphs. We know that real networks may be directed, have weighted connections, be bipartite. Methods to deal with such systems have been developed, as we have seen, especially in the most recent literature, but they are mostly preliminary attempts and there is room for improvement. Another situation that may occur in real systems is the presence of edges with positive and negative weights, indicating attractive and repulsive interactions, respectively. This is the case, for instance, of correlation data (Mantegna, 1999). In this case, ideal partitions would have positively weighted intracluster edges and negatively weighted intercluster edges. We have discussed some studies in this direction (Go´mez et al., 2009; Kaplan and Forrest, 2008; Traag and Brugge-

man, 2009), but we are just at the beginning of this endeavour. Instead, there are no algorithms yet which are capable to deal with graphs in which there are edges of several types, indicating diﬀerent kinds of interactions between the vertices (multigraphs). Agents of social networks, for instance, may be joined by working relationships, friendship, family ties, etc. At the moment there are essentially two ways of proceeding in these instances: 1) keeping edges of one type and forgetting the others, repeating the analysis for each type of edges and eventually comparing the results obtained; 2) analyzing a single (weighted) graph, obtained by “combining” the contributions of the diﬀerent types of edges in some way. Finally, since most real networks are built through the results of experiments, which carry errors in their estimates, it would be useful to consider as well the case in which edges have not only associated weights, but also errors on their values.

Since the paper by Palla et al. (Palla et al., 2005), overlapping communities have received a lot of attention (Section XI). However, there is still no consensus about a quantitative deﬁnition of the concept of overlapping community, and most deﬁnitions depend on the method adopted. Intuitively, one would expect that clusters share vertices lying at their borders, and this idea has inspired most algorithms. However, clusters detected with the Clique Percolation Method (Section XI.A) often share central vertices of the clusters, which makes sense in speciﬁc instances, especially in social networks. So, it is still unclear how to characterize overlapping vertices. Moreover, the concept of overlapping clusters seems at odds with that of hierarchical structure. No dendrogram can be drawn if there are overlapping vertices, at least in the standard way. Due to the relevance of both features in real networks, it is necessary to adapt them to each other in a consistent way. Overlapping vertices pose problems

- as well when it comes to comparing the results of diﬀerent methods on the same graph. Most similarity measures are deﬁned only in the case of partitions, where each vertex is assigned to a single cluster (Section XV.B). It is then necessary to extend such deﬁnitions to the case of overlapping communities, whenever possible.

Another issue that is getting increasingly more popular is the study of graphs evolving in time. This is now possible due to the availability of timestamped network data sets. Tracking the evolution of community structure in time is very important, to uncover how communities are generated and how they interact with each other. Scholars have just begun to study this problem (Asur et al., 2007; Chakrabarti et al., 2006; Chi et al., 2007; Fenn et al., 2009; Hopcroft et al., 2004; Kim and Han, 2009; Lin et al., 2008; Palla et al., 2007; Sun et al., 2007) (Section XIII). Typically one analyzes separately snapshots

- at diﬀerent times and checks what happened at time t+1 to the communities at time t. It would be probably better to use simultaneously the whole dynamic data set, and future work shall aim at deﬁning proper ways to do that. In this respect, the evolutionary clustering frame-


work by Chakrabarti et al. (Chakrabarti et al., 2006) is a promising starting point.

The computational complexity of graph clustering algorithms has improved by at least one power in the graph size (on average) in just a couple of years. Due to the large size of many systems one wishes to investigate, the ultimate goal would be to design techniques with linear or even sublinear complexity. Nowadays partitions in graphs with up to millions of vertices can be found. However, the results are not yet very reliable, as they are usually obtained by greedy optimizations, which yield rough approximations of the desired solution. In this respect the situation could improve by focusing on the development of eﬃcient local methods, for two reasons: 1) they enable analyses of portions of the graph, independently of the rest; 2) they are often suitable for parallel implementations, which may speed up considerably the computation.

Finally, if there has been a tremendous eﬀort in the design of clustering algorithms, basically nothing has been done to make sense of their results. What shall we do with communities? What can they tell us about a system? The hope is that they will enable one to disclose “hidden” relationships between vertices, due to features that are not known, because they are hard to measure, for instance. It is quite possible that the scientiﬁc community will converge sooner or later to a deﬁnition a posteriori of community. Already now, most algorithms yield similar results in practical applications. But what is the relationship between the vertex classiﬁcation given by the algorithms and real classiﬁcations? This is the main question beneath the whole endeavor.

###### Acknowledgments

I am indebted to these people for giving useful suggestions and advice to improve this manuscript at various stages: A. Arenas, J. W. Berry, A. Clauset, P. Csermely, S. G´mez, S. Gregory, V. Gudkov, R. Guimer`, Y. Ispolatov, R. Lambiotte, A. Lancichinetti, J.-P. Onnela, G. Palla, M. A. Porter, F. Radicchi, J. J. Ramasco, C. Wiggins. I gratefully acknowledge ICTeCollective, grant number 238597 of the European Commission.

Appendix A: Elements of Graph Theory

1. Basic Deﬁnitions

A graph G is a pair of sets (V,E), where V is a set of vertices or nodes and E is a subset of V 2, the set of unordered pairs of elements of V . The elements of E are called edges or links, the two vertices that identify an edge are called endpoints. An edge is adjacent to each of its endpoints. If each edge is an ordered pair of vertices one has a directed graph (or digraph). In this case an ordered pair (v,w) is an edge directed from v to w, or an edge beginning at v and ending at w. A graph is visualized as a set of points connected by lines, as shown in Fig. 41.

- FIG. 41 A sample graph with seven vertices and seven edges.


In many real examples, graphs are weighted, i. e. a real number is associated to each of the edges. Graphs do not include loops, i. e. edges connecting a vertex to itself, nor multiple edges, i. e. several edges joining the same pair of vertices. Graphs with loops and multiple edges are called multigraphs. Generalizations of graphs admitting edges between any number of vertices (not necessarily two) are called hypergraphs.

A graph G = (V ,E ) is a subgraph of G = (V,E) if

- V ⊂ V and E ⊂ E. If G contains all edges of G that join vertices of V one says that the subgraph G is induced or spanned by V . A partition of the vertex set V in two subsets S and V − S is called a cut; the cut size is the number of edges of G joining vertices of S with vertices of V − S.


We indicate the number of vertices and edges of a graph with n and m, respectively. The number of vertices is the order of the graph, the number of edges its size. The maximum size of a graph equals the total number of unordered pairs of vertices, n(n − 1)/2. If |V | = n and |E| = m = n(n − 1)/2, the graph is a clique (or complete graph), and is indicated as Kn. Two vertices are neighbors (or adjacent) if they are connected by an edge. The set of neighbors of a vertex v is called neighborhood, and we shall denote it with Γ(v). The degree kv of a vertex v is the number of its neighbors. The degree sequence is the list of the degrees of the graph vertices, kv

. On directed graphs, one distinguishes two types of degree for a vertex v: the indegree, i. e. the number of edges beginning at v and the outdegree, i. e. the number of edges ending at v. The analogue of degree on a weighted graph is the strength, i. e. the sum of the weights of the edges adjacent to the vertex. Another useful local property of graphs is transitivity or clustering (Watts and Strogatz, 1998), which indicates the level of cohesion between the neighbors of a vertex 32. The clustering coeﬃcient cv of

###### ,kv

###### ,...,kv

1

2

n

vertex v is the ratio between the number of edges joining pairs of neighbors of v and the total number of possible edges, given by kv(kv − 1)/2, kv being the degree of v. According to this deﬁnition, cv measures the probability that a pair of neighbors of v are connected. Since all neighbors of v are connected to v by deﬁnition, edges connecting pairs of neighbors of v form triangles with v. This is why the deﬁnition is often given in terms of number of triangles.

A path is a graph P = (V (P),E(P)), with V (P) = {x0,x1,...,xl} and E(P) = {x0x1,x1x2,...,xl−1xl}. The vertices x0 and xl are the endvertices of P, whereas l is its length. Given the notions of vertices, edges and paths, one can deﬁne the concept of independence. A set of vertices (or edges) of a graph are independent if no two elements of them are adjacent. Similarly, two paths are independent if they only share the endvertices. A cycle is a closed path whose vertices and edges are all distinct. Cycles of length l are indicated with Cl. The smallest non-trivial cycle is the triangle, C3.

Paths allow to deﬁne the concept of connectivity and distance in graphs. A graph is connected if, given any pair of vertices, there is at least one path going from one vertex to the other. In general, there may be multiple paths connecting two vertices, with diﬀerent lengths. A shortest path, or geodesic, between two vertices of a graph, is a path of minimal length. Such minimal length is the distance between the two vertices. The diameter of a connected graph is the maximal distance between two vertices. If there is no path between two vertices, the graph is divided in at least two connected subgraphs. Each maximal connected subgraph of a graph is called connected component.

A graph without cycles is a forest. A connected forest is a tree. Trees are very important in graph theory and deserve some attention. In a tree, there can be only one path from a vertex to any other. In fact, if there were at least two paths between the same pair of vertices they would form a cycle, while the tree is an acyclic graph by deﬁnition. Further, the number of edges of a tree with n vertices is n − 1. If any edge of a tree is removed, it would get disconnected in two parts; if a new edge is added, there would be at least one cycle. This is why a tree is a minimally connected, maximally acyclic graph of a given order. Every connected graph contains a spanning tree, i. e. a tree sharing all vertices of the graph. On weighted graphs, one can deﬁne a minimum (maximum) spanning tree, i. e. a spanning tree such that the sum of the weights on the edges is minimal (maximal). Minimum and maximum spanning trees are often used in graph optimization problems, including clustering.

A graph G is bipartite if the vertex set V is separated in

- 32 The term clustering is commonly adopted to indicate community detection in some disciplines, like computer science, and we


often used it in this context throughout the manuscript. We paid attention to disambiguate the occurrences in which clustering indicates instead the local property of a vertex neighborhood described here.

two disjoint subsets V1 and V2, or classes, and every edge joins a vertex of V1 with a vertex of V2. The deﬁnition can be extended to that of r-partition, where the vertex classes are r and no edge joins vertices within the same class. In this case one speaks of multipartite graphs.

###### 2. Graph Matrices

The whole information about the topology of a graph of order n is entailed in the adjacency matrix A, which is an n × n matrix whose element Aij equals 1 if there is an edge joining vertices i and j, otherwise it is zero. Due to the absence of loops the diagonal elements of the adjacency matrix are all zero. For an undirected graph A is a symmetric matrix. The sum of the elements of the i-th row or column yields the degree of node i. If the edges are weighted, one deﬁnes the weight matrix

- W, whose element Wij expresses the weight of the edge between vertices i and j.


The spectrum of a graph G is the set of eigenvalues of its adjacency matrix A. Spectral properties of graph matrices play an important role in the study of graphs. For instance, the stochastic matrices rule the process of diﬀusion (random walk) on a graph. The right stochastic matrix R is obtained from A by dividing the elements of each row i by the degree of vertex i. The left stochastic matrix T, or transfer matrix, is the transpose of R. The spectra of stochastic matrices allow to evaluate, for instance, the mixing time of the random walk, i. e. the time it takes to reach the stationary distribution of the process. The latter is obtained by computing the eigenvector of the transfer matrix corresponding to the largest eigenvalue.

Another important matrix is the Laplacian L = D−A, where D is the diagonal matrix whose element Dii equals the degree of vertex i. The matrix L is usually referred to as unnormalized Laplacian. In the literature one often uses normalized Laplacians (Chung, 1997), of which there are two main forms: Lsym = D−1/2LD−1/2 and Lrw = D−1L = I − D−1A = I − T. The matrix Lsym is symmetric; Lrw is not symmetric and is closely related to a random walk taking place on the graph. All Laplacian matrices have a straightforward extension to the case of weighted graphs. The Laplacian is one of the most studied matrices and ﬁnds application in many different contexts, like graph connectivity (Bollobas, 1998), synchronization (Barahona and Pecora, 2002; Nishikawa et al., 2003), diﬀusion (Chung, 1997) and graph partitioning (Pothen, 1997). By construction, the sum of the elements of each row of the Laplacian (normalized or unnormalized) is zero. This implies that L always has at least one zero eigenvalue, corresponding to the eigenvector with all equal components, such as (1,1,...,1). Eigenvectors corresponding to diﬀerent eigenvalues are all orthogonal to each other. Interestingly, L has as many zero eigenvalues as there are connected components in the graph. So, the Laplacian of a connected graph has but

one zero eigenvalue, all others being positive. Eigenvectors of Laplacian matrices are regularly used in spectral clustering (Section IV.D). In particular, the eigenvector corresponding to the second smallest eigenvalue, called Fiedler vector (Fiedler, 1973, 1975), is used for graph bipartitioning, as described in Section IV.A.

###### 3. Model graphs

In this section we present the most popular models of graphs introduced to describe real systems, at least to some extent. Such graphs are useful null models in community detection, as they do not have community structure, so they can be used for negative tests of clustering algorithms.

The oldest model is that of random graph, proposed by Solomonoﬀ and Rapoport (Solomonoﬀ and Rapoport, 1951) and independently by Erd¨s and R´enyi (Erd¨s and R´enyi, 1959). There are two parameters: the number of vertices n and the connection probability p. Each pair of vertices is connected with equal probability p independently of the other pairs. The expected number of edges of the graph is pn(n−1)/2, and the expected mean degree

k = p(n − 1). The degree distribution of the vertices of a random graph is binomial, and in the limit n → ∞, p → 0 for ﬁxed k it converges to a Poissonian. Therefore, the vertices have all about the same degree, close to k (Fig. 42, top). The most striking property of this class of graphs is the phase transition observed by varying k in the limit n → ∞. For k < 1, the graph is separated in connected components, each of them being microscopic, i. e. occupying but a vanishing portion of the system size. For k > 1, instead, one of the components becomes macroscopic (giant component), i. e. it occupies a ﬁnite fraction of the graph vertices.

The diameter of a random graph with n vertices is very small, growing only logarithmically with n. This property (small-world eﬀect) is very common in many real graphs. The ﬁrst evidence that social networks are characterized by paths of small length was provided by a series of famous experiments conducted by the phychologist Stanley Milgram (Milgram, 1967; Travers and Milgram, 1969). The expected clustering coeﬃcient of a vertex of a random graph is p, as the probability for two vertices to be connected is the same whether they are neighbors of the same vertex or not. Real graphs, however, are characterized by far higher values of the clustering coeﬃcient as compared to random graphs of the same size. Watts and Strogatz (Watts and Strogatz, 1998) showed that the small world property and high clustering coeﬃcient can coexist in the same system. They designed a class of graphs which result from an interpolation between a regular lattice, which has high clustering coeﬃcient, and a random graph, which has the small-world property. One starts from a ring lattice in which each vertex has degree k, and with a probability p each edge is rewired to a different target vertex (Fig. 42, center). It turns out that

| | |
|---|---|
| | |


Pajek

| | |
|---|---|
| | |


Pajek

| | |
|---|---|
| | |


Pajek

- FIG. 42 Basic models of complex networks. (Top) Erdo¨sRe´nyi random graph with 100 vertices and a link probability p = 0.02. (Center) Small world graph a´ la Watts-Strogatz, with 100 vertices and a rewiring probability p = 0.1. (Bottom) Baraba´si-Albert scale-free network, with 100 vertices and an average degree of 2. Courtesy by J. J. Ramasco.


low values of p suﬃce to reduce considerably the length of shortest paths between vertices, because rewired edges act as shortcuts between initially remote regions of the graph. On the other hand, the clustering coeﬃcient remains high, since few rewired edges do not perturb appreciably the local structure of the graph, which remains similar to the original ring lattice. For p = 1 all edges are rewired and the resulting structure is a random graph ´ la Erdo¨s and R´enyi.

The seminal paper of Watts and Strogatz triggered a huge interest towards the graph representation of real systems. One of the most important discoveries was that the distribution of the vertex degree of real graphs is very heterogeneous (Albert et al., 1999), with many vertices having few neighbors coexisting with some vertices with many neighbors. In several cases the tail of this distribution can be described as a power law with good approximation33, hence the expression scale-free networks. Such degree heterogeneity is responsible for a number of remarkable features of real networks, such as resilience to random failures/attacks (Albert et al., 2000), and the absence of a threshold for percolation (Cohen et al., 2000) and epidemic spreading (Pastor-Satorras and Vespignani, 2001). The most popular model of a graph with a power law degree distribution is the model by Barab´si and Albert (Barab´si and Albert, 1999). A version of the model for directed graphs had been proposed much earlier by de Solla Price (Price, 1976), building up on previous ideas developed by Simon (Simon, 1955). The graph is created with a dynamic procedure, where vertices are added one by one to an initial core. The probability for a new vertex to set an edge with a preexisting vertex is proportional to the degree of the latter. In this way, vertices with high degree have large probability of being selected as neighbors by new vertices; if this happens, their degree further increases so they will be even more likely to be chosen in the future. In the asymptotic limit of inﬁnite number of vertices, this rich-gets-richer strategy generates a graph with a degree distribution characterized by a power-law tail with exponent 3. In Fig. 42 (bottom) we show an example of Barab´si-Albert (BA) graph. The clustering coeﬃcient of a BA graph decays with the size of the graph, and it is much lower than in real networks. Moreover, the power law decays of the degree distributions observed in real networks are characterized by a range of exponents’ values (usually between 2 and 3), whereas the BA model yields a ﬁxed value. However, many reﬁnements of the BA model as well as plenty of diﬀerent models have been later introduced to account more closely for the features observed in real systems (for details see (Albert and Barab´si, 2002; Barrat et al., 2008;

33 The power law is however not necessary to explain the properties of complex networks. It is enough that the tails of the degree distributions are “fat”, i. e. spanning orders of magnitude in degree. They may or may not be accurately ﬁtted by a power law.

###### Boccaletti et al., 2006; Mendes and Dorogovtsev, 2003; Newman, 2003; Pastor-Satorras and Vespignani, 2004)).

References Adamcsek, B., G. Palla, I. J. Farkas, I. Dere´nyi, and T. Vic-

sek, 2006, Bioinformatics 22(8), 1021. Adomavicius, G., and A. Tuzhilin, 2005, IEEE Trans. Knowl.

Data Eng. 17(6), 734. Agarwal, G., and D. Kempe, 2008, Eur. Phys. J. B 66, 409. Agrawal, R., and H. V. Jagadish, 1994, Knowl. Data Eng.

6(2), 225.

Ahn, Y.-Y., J. P. Bagrow, and S. Lehmann, 2009, eprint arXiv:0903.3178.

Ahuja, R. K., T. L. Magnanti, and J. B. Orlin, 1993, Network Flows: Theory, Algorithms, and Applications (Prentice Hall, Englewood Cliﬀs, USA).

Akaike, H., 1974, IEEE Trans. Autom. Control 19(6), 716. Alba, R. D., 1973, J. Math. Sociol. 3, 113. Albert, R., and A.-L. Baraba´si, 2002, Rev. Mod. Phys. 74(1),

47.

- Albert, R., H. Jeong, and A.-L. Baraba´si, 1999, Nature 401, 130.
- Albert, R., H. Jeong, and A.-L. Baraba´si, 2000, Nature 406, 378.


Allahverdyan, A. E., and A. Galstyan, 2009, eprint

arXiv:0907.4803. Alves, N. A., 2007, Phys. Rev. E 76(3), 036101. Andrews, G. E., 1976, The theory of partitions (Addison-

Wesley, Boston, USA).

Anthonisse, J. M., 1971, The rush in a directed graph, Technical Report, Stichting Mathematisch Centrum, 2e Boerhaavestraat 49 Amsterdam, The Netherlands.

Arenas, A., and A. D´ıaz-Guilera, 2007, Eur. Phys. J. Special Topics 143, 19. Arenas, A., A. Dı´az-Guilera, and C. J. Pe´rez-Vicente, 2006, Phys. Rev. Lett. 96(11), 114102. Arenas, A., J. Duch, A. Ferna´ndez, and S. Go´mez, 2007, New J. Phys. 9, 176. Arenas, A., A. Ferna´ndez, S. Fortunato, and S. Go´mez, 2008a, J. Phys. A 41(22), 224001. Arenas, A., A. Ferna´ndez, and S. Go´mez, 2008b, New J. Phys.

10(5), 053039.

Asahiro, Y., R. Hassin, and K. Iwama, 2002, Discrete Appl. Math. 121(1-3), 15.

Ashburner, M., C. A. Ball, J. A. Blake, D. Botstein, H. Butler, J. M. Cherry, A. P. Davis, K. Dolinski, S. S. Dwight, J. T. Eppig, M. A. Harris, D. P. Hill, et al., 2000, Nature Genetics 25(1), 25.

Asur, S., S. Parthasarathy, and D. Ucar, 2007, in KDD ’07: Proceedings of the 13th ACM SIGKDD international conference on Knowledge discovery and data mining (ACM, New York, NY, USA), pp. 913–921.

Backstrom, L., D. Huttenlocher, J. Kleinberg, and X. Lan, 2006, in KDD ’06: Proceedings of the 12th ACM SIGKDD international conference on Knowledge discovery and data mining (ACM, New York, NY, USA), pp. 44–54.

Baeza-Yates, R., and B. Ribeiro-Neto, 1999, Modern Infor-

mation Retrieval (Addison-Wesley, Boston, USA). Bagrow, J. P., 2008, J. Stat. Mech. P05001. Bagrow, J. P., and E. M. Bollt, 2005, Phys. Rev. E 72(4),

046108.

Balakrishnan, V. K., 1997, Schaum’s Outline of Graph Theory (McGraw-Hill, New York, USA). Bansal, N., A. Blum, and S. Chawla, 2004, Mach. Learn.

56(1-3), 89. Baraba´si, A.-L., and R. Albert, 1999, Science 286, 509. Barahona, M., and L. M. Pecora, 2002, Phys. Rev. Lett.

89(5), 054101. Barber, M. J., 2007, Phys. Rev. E 76(6), 066102. Barber, M. J., and J. W. Clark, 2009, Phys. Rev. E 80(2),

026129.

Barber, M. J., M. Faria, L. Streit, and O. Strogan, 2008, in Stochastic and Quantum Dynamics of Biomolecular Systems, edited by C. C. Bernido and M. V. Carpio-Bernido (American Institute of Physics, Melville, USA), volume 1021 of American Institute of Physics Conference Series, pp. 171–182.

Barnes, E. R., 1982, SIAM J. Alg. Discr. Meth. 3, 541. Barrat, A., M. Barth´elemy, R. Pastor-Satorras, and

A. Vespignani, 2004, Proc. Natl. Acad. Sci. USA 101(11), 3747.

Barrat, A., M. Barthe´lemy, and A. Vespignani, 2008, Dynamical processes on complex networks (Cambridge University Press, Cambridge, UK).

Batagelj, V., and M. Zaversnik, 2003, eprint cs.DS/0310049. Baumes, J., M. Goldberg, and M. Magdon-Ismail, 2005a, in

IEEE International Conference on Intelligence and Security Informatics (ISI), pp. 27–36.

Baumes, J., M. K. Goldberg, M. S. Krishnamoorthy, M. Magdon-Ismail, and N. Preston, 2005b, in IADIS AC, edited by N. Guimaraes and P. T. Isaias (IADIS), pp. 97– 104.

Beal, M. J., 2003, Variational Algorithms for Approximate Bayesian Inference, Ph.D. thesis, Gatsby Computational Neuroscience Unit, University College London.

Beirlant, J., Y. Goegebeur, J. Segers, and J. Teugels, 2004, Statistics of Extremes: Theory and Applications (Wiley & Sons, Chichester, UK), 1 edition.

Berg, J., and M. La¨ssig, 2006, Proc. Natl. Acad. Sci. USA

103(29), 10967.

Berry, J. W., B. Hendrickson, R. A. LaViolette, V. J. Leung, and C. A. Phillips, 2007, eprint arXiv:0710.3800. Berry, J. W., B. Hendrickson, R. A. LaViolette, and C. A. Phillips, 2009, eprint arXiv:0903.1072.

Bezdek, J. C., 1981, Pattern Recognition with Fuzzy Objective Function Algorithms (Kluwer Academic Publishers, Norwell, USA).

Bhatia, R., 1997, Matrix Analysis (Springer-Verlag, New

York, USA). Bianconi, G., 2008, Europhys. Lett. 81, 28005. Bianconi, G., A. C. C. Coolen, and C. J. Perez Vicente, 2008,

Phys. Rev. E 78(1), 016114. Bianconi, G., P. Pin, and M. Marsili, 2009, Proc. Natl. Acad. Sci. USA 106(28), 11433. Biernacki, C., G. Celeux, and G. Govaert, 2000, IEEE Trans. Pattern Anal. Mach. Intell. 22(7), 719. Blake, A., and A. Zisserman, 1987, Visual Reconstruction (MIT Press, Cambridge, USA). Blatt, M., S. Wiseman, and E. Domany, 1996, Phys. Rev. Lett. 76, 3251. Blondel, V. D., J.-L. Guillaume, R. Lambiotte, and E. Lefebvre, 2008, J. Stat. Mech. P10008. Boccaletti, S., M. Ivanchenko, V. Latora, A. Pluchino, and A. Rapisarda, 2007, Phys. Rev. E 75(4), 045102. Boccaletti, S., V. Latora, Y. Moreno, M. Chavez, and D. U.

Hwang, 2006, Phys. Rep. 424(4-5), 175. Boettcher, S., and A. G. Percus, 2001, Phys. Rev. Lett. 86, 5211. Bollobas, B., 1998, Modern Graph Theory (Springer Verlag, New York, USA).

Bomze, I. M., M. Budinich, P. M. Pardalos, and M. Pelillo, 1999, in Handbook of Combinatorial Optimization, edited by D.-Z. Du and P. Pardalos (Kluwer Academic Publishers, Norwell, USA), pp. 1–74.

Bonacich, P., 1972, Journal of Mathematical Sociology 2(1), 113. Bonacich, P., 1987, The American Journal of Sociology 92(5), 1170. Bonanno, G., G. Caldarelli, F. Lillo, and R. N. Mantegna, 2003, Phys. Rev. E 68(4), 046130. Bonanno, G., N. Vandewalle, and R. N. Mantegna, 2000, Phys. Rev. E 62(6), R7615. Borgatti, S., M. Everett, and P. Shirey, 1990, Soc. Netw. 12,

337. Brandes, U., 2001, J. Math. Sociol. 25, 163. Brandes, U., D. Delling, M. Gaertler, R. Go¨rke, M. Hoefer,

Z. Nikolski, and D. Wagner, 2006, URL http://digbib. ubka.uni-karlsruhe.de/volltexte/documents/3255.

Brandes, U., M. Gaertler, and D. Wagner, 2003, in Proceedings of ESA (Springer-Verlag, Berlin, Germany), pp. 568– 579.

Brin, S., and L. E. Page, 1998, Comput. Networks ISDN 30,

107. Bron, C., and J. Kerbosch, 1973, Commun. ACM 16, 575. Burnham, K. P., and D. R. Anderson, 2002, Model Selec-

tion and Multimodel Inference: A Practical InformationTheoretic Approach (Springer, New York, USA).

Burt, R. S., 1976, Soc. Forces 55, 93. C. Castellano, F. Cecconi, V. Loreto, D. Parisi, and F. Radic-

chi, 2004, Eur. Phys. J. B 38(2), 311. Capocci, A., V. D. P. Servedio, G. Caldarelli, and F. Colaiori, 2005, Physica A 352, 669.

Chakrabarti, D., 2004, in PKDD, edited by J.-F. Boulicaut, F. Esposito, F. Giannotti, and D. Pedreschi (Springer), volume 3202 of Lect. Notes Comp. Sci., pp. 112–124, ISBN 3-540-23108-0.

Chakrabarti, D., R. Kumar, and A. Tomkins, 2006, in KDD ’06: Proceedings of the 12th ACM SIGKDD international conference on Knowledge discovery and data mining (ACM, New York, NY, USA), pp. 554–560.

Chan, P. K., M. D. F. Schlag, and J. Y. Zien, 1993, in Proceedings of the 30th International Conference on Design Automation (ACM Press, New York, USA), pp. 749–754.

Chandra, A. K., P. Raghavan, W. L. Ruzzo, and R. Smolensky, 1989, in STOC ’89: Proceedings of the twenty-ﬁrst annual ACM symposium on Theory of computing (ACM, New York, NY, USA), pp. 574–586.

Chen, J., and B. Yuan, 2006, Bioinformatics 22(18), 2283. Chen, W. Y. C., A. W. M. Dress, and W. Q. Yu, 2008, Math.

Comp. Sci. 1(3), 441.

Chi, Y., X. Song, D. Zhou, K. Hino, and B. L. Tseng, 2007, in KDD ’07: Proceedings of the 13th ACM SIGKDD international conference on Knowledge discovery and data mining (ACM, New York, NY, USA), pp. 153–162.

Chung, F., 1997, Spectral Graph Theory, Number 92 in CBMS Regional Conference Series in Mathematics (American Mathematical Society, Providence, USA).

Clauset, A., 2005, Phys. Rev. E 72(2), 026132. Clauset, A., C. Moore, and M. E. J. Newman, 2007, in Sta-

tistical Network Analysis: Models, Issues, and New Directions, edited by E. M. Airoldi, D. M. Blei, S. E. Fienberg, A. Goldenberg, E. P. Xing, and A. X. Zheng (Springer, Berlin, Germany), volume 4503 of Lect. Notes Comp. Sci., pp. 1–13.

Clauset, A., C. Moore, and M. E. J. Newman, 2008, Nature

453(7191), 98.

Clauset, A., M. E. J. Newman, and C. Moore, 2004, Phys. Rev. E 70(6), 066111. Cohen, R., K. Erez, D. ben Avraham, and S. Havlin, 2000, Phys. Rev. Lett. 85(21), 4626. Coleman, J. S., 1964, An Introduction to Mathematical Sociology (Collier-Macmillan, London, UK). Condon, A., and R. M. Karp, 2001, Random Struct. Algor.

18, 116.

Copiˇc,ˇ J., M. O. Jackson, and A. Kirman, 2005, URL http: //www.hss.caltech.edu/~{}jernej/netcommunity.pdf. Csermely, P., 2008, Trends Biochem. Sci. 33(12), 569. da Fontoura Costa, L., 2004, eprint cond-mat/0405022. Danon, L., A. Dı´az-Guilera, and A. Arenas, 2006, J. Stat.

Mech. 11, 10. Danon, L., A. Dı´az-Guilera, J. Duch, and A. Arenas, 2005, J. Stat. Mech. P09008.

Danon, L., J. Duch, A. Arenas, and A. Dı´az-Guilera, 2007, in Large Scale Structure and Dynamics of Complex Networks: From Information Technology to Finance and Natural Science, edited by Caldarelli G. and Vespignani A. (World Scientiﬁc, Singapore), pp. 93–114.

David, H. A., and H. N. Nagaraja, 2003, Order Statistics (Wiley-Interscience, Hoboken, USA). Davis, A., B. B. Gardner, and M. R. Gardner, 1941, Deep South (University of Chicago Press, Chicago, USA).

Delling, D., M. Gaertler, R. Go¨rke, Z. Nikoloski, and D. Wagner, 2007, How to Evaluate Clustering Techniques., Technical Report, Universita¨t Karlsruhe, Germany.

Delvenne, J. C., S. N. Yaliraki, and M. Barahona, 2008, eprint arXiv:0812.1811.

Demmel, J., J. Dongarra, A. Ruhe, and H. van der Vorst, 2000, Templates for the solution of algebraic eigenvalue problems: a practical guide (Society for Industrial and Applied Mathematics, Philadelphia, USA).

Dempster, A. P., N. M. Laird, and D. B. Rubin, 1977, J. Roy. Stat. Soc. B 39, 1. Dere´nyi, I., G. Palla, and T. Vicsek, 2005, Phys. Rev. Lett.

94(16), 160202.

Dhillon, I. S., Y. Guan, and B. Kulis, 2007, IEEE Trans. Pattern Anal. Mach. Intell. 29(11), 1944.

Djidjev, H., 2007, in WAW, edited by W. Aiello, A. Z. Broder, J. C. M. Janssen, and E. E. Milios (Springer-Verlag, Berlin, Germany), volume 4936 of Lecture Notes in Computer Science, pp. 117–128.

Donath, W., and A. Hoﬀman, 1973, IBM Journal of Research and Development 17(5), 420.

Donetti, L., and M. A. Mun˜oz, 2004, J. Stat. Mech. P10012. Donetti, L., and M. A. Mu˜noz, 2005, in Modeling Coopera-

tive Behavior in the Social Sciences, edited by P. Garrido, J. Maroo, and M. A. Mu˜noz, volume 779 of American Institute of Physics Conference Series, pp. 104–107.

van Dongen, S., 2000a, Graph Clustering by Flow Simulation, Ph.D. thesis, Dutch National Research Institute for Mathematics and Computer Science, University of Utrecht, Netherlands.

Dongen, S., 2000b, Performance criteria for graph clustering and Markov cluster experiments, Technical Report, Na-

tional Research Institute for Mathematics and Computer Science in the Netherlands, Amsterdam, The Netherlands.

Doreian, P., V. Batagelj, and A. Ferligoj, 2005, Generalized Blockmodeling (Cambridge University Press, New York, USA).

Dorogovtsev, S. N., and J. F. F. Mendes, 2002, Adv. Phys.

51, 1079.

Dourisboure, Y., F. Geraci, and M. Pellegrini, 2007, in WWW ’07: Proceedings of the 16th international conference on the World Wide Web (ACM, New York, NY, USA), pp. 461– 470.

Du, H., M. W. Feldman, S. Li, and X. Jin, 2007, Complexity

12(3), 53.

Du, N., B. Wang, B. Wu, and Y. Wang, 2008, in IEEE/WIC/ACM International Conference on Web Intelligence and Intelligent Agent Technology (IEEE Computer Society, Los Alamitos, CA, USA), pp. 176–179.

Duch, J., and A. Arenas, 2005, Phys. Rev. E 72(2), 027104. Dunbar, R., 1998, Grooming, Gossip, and the Evolution of Language (Harvard University Press, Cambridge, USA). Dunn, J. C., 1974, J. Cybernetics 3, 32. Dunn, R., F. Dudbridge, and C. M. Sanderson, 2005, BMC

Bioinf. 6, 39. Earl, D. J., and M. W. Deem, 2005, Phys. Chem. Chem. Phys.

7, 3910.

Eckmann, J.-P., and E. Moses, 2002, Proc. Natl. Acad. Sci. USA 99, 5825. Efron, B., and R. J. Tibshirani, 1993, An Introduction to the Bootstrap (Chapman & Hall, New York, USA). Elias, P., A. Feinstein, and C. E. Shannon, 1956, IRE Trans. Inf. Theory IT-2, 117.

Erdo¨s, P., and A. R´enyi, 1959, Publ. Math. Debrecen 6, 290. Eriksen, K. A., I. Simonsen, S. Maslov, and K. Sneppen, 2003,

Phys. Rev. Lett. 90(14), 148701.

- Estrada, E., and N. Hatano, 2008, Phys. Rev. E 77(3), 036111.
- Estrada, E., and N. Hatano, 2009, Appl. Math. Comput. 214, 500.


Euler, L., 1736, Commentarii Academiae Petropolitanae 8, 128. Evans, T. S., and R. Lambiotte, 2009, Phys. Rev. E 80(1), 016105. Everett, M. G., and S. P. Borgatti, 1994, J. Math. Soc. 19(1), 29. Everett, M. G., and S. P. Borgatti, 1998, Connections 21(1), 49. Fan, Y., M. Li, P. Zhang, J. Wu, and Z. Di, 2007, Physica A

377, 363.

Farkas, I., D. Abel,´ G. Palla, and T. Vicsek, 2007, New J. Phys. 9, 180.

Farutin, V., K. Robison, E. Lightcap, V. Dancik, A. Ruttenberg, S. Letovsky, and J. Pradines, 2006, Proteins 62(3), 800.

Feige, U., D. Peleg, and G. Kortsarz, 2001, Algorithmica

29(3), 410.

Feng, Z., X. Xu, N. Yuruk, and T. Schweiger, 2007, Lect. Notes Comp. Sci. 4654, 385. Fenn, D. J., M. A. Porter, M. McDonald, S. Williams, N. F.

Johnson, and N. S. Jones, 2009, Chaos 19(3), 033119. Fiedler, M., 1973, Czech. Math. J. 23(98), 298. Fiedler, M., 1975, Czech. Math. J. 25, 619. Fienberg, S. E., and S. Wasserman, 1981, Sociol. Methodol.

12, 156.

Flake, G. W., S. Lawrence, and C. L. Giles, 2000, in Sixth

ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (ACM Press, Boston, USA), pp. 150–160.

Flake, G. W., S. Lawrence, C. Lee Giles, and F. M. Coetzee,

2002, IEEE Computer 35, 66. F.Lorrain, and H. White, 1971, J. Math. Sociol. 1, 49. Ford, L. R., and D. R. Fulkerson, 1956, Canadian J. Math. 8,

399.

Fortunato, S., 2007, in Noise and Stochastics in Complex Systems and Finance, volume 6601 of SPIE Conference Series, p. 660108.

Fortunato, S., and M. Barthe´lemy, 2007, Proc. Natl. Acad. Sci. USA 104, 36.

Fortunato, S., and C. Castellano, 2009, in Encyclopedia of Complexity and Systems Science, edited by R. A. Meyers (Springer, Berlin, Germany), volume 1, eprint arXiv:0712.2716.

Fortunato, S., V. Latora, and M. Marchiori, 2004, Phys. Rev. E 70(5), 056104.

Fouss, F., and J.-M. Renders, 2007, IEEE Trans. on Knowl. and Data Eng. 19(3), 355, member-Pirotte, Alain and Member-Saerens, Marco.

Fowlkes, E. B., and C. L. Mallows, 1983, J. Am. Stat. Assoc.

78, 553. Freeman, L. C., 1977, Sociometry 40, 35. Freeman, L. C., 2004, The Development of Social Network

Analysis: A Study in the Sociology of Science (BookSurge Publishing).

Fu, Y., and P. Anderson, 1986, J. Phys. A 19, 1605. Gaertler, M., R. G¨orke, and D. Wagner, 2007, in AAIM, edited by M.-Y. Kao and X.-Y. Li (Springer, Berlin, Germany), volume 4508 of Lecture Notes in Computer Science, pp. 11–26.

Gallager, R. G., 1963, Low density parity check codes (MIT Press, Cambridge, USA).

Gan, G., C. Ma, and J. Wu, 2007, Data Clustering: Theory, Algorithms, and Applications (ASA-SIAM Series on Statistics and Applied Probability) (Society for Industrial and Applied Mathematics, Philadelphia, USA).

Garey, M. R., and D. S. Johnson, 1990, Computers and Intractability : A Guide to the Theory of NP-Completeness (W. H. Freeman & Co., New York, USA).

Gfeller, D., J.-C. Chappelier, and P. De Los Rios, 2005, Phys. Rev. E 72(5), 056135.

- Gfeller, D., and P. De Los Rios, 2007, Phys. Rev. Lett. 99(3), 038701.
- Gfeller, D., and P. De Los Rios, 2008, Phys. Rev. Lett. 100(17), 174104.


Ghosh, R., and K. Lerman, 2008, in Proceedings of KDD workshop on Social Network Analysis (SNAKDD), eprint arXiv:0805.4606.

Giles, C. L., K. Bollacker, and S. Lawrence, 1998, in Digital Libraries 98 - The Third ACM Conference on Digital Libraries, edited by I. Witten, R. Akscyn, and F. M. Shipman III (ACM Press, Pittsburgh, PA), pp. 89–98.

Girvan, M., and M. E. J. Newman, 2002, Proc. Natl. Acad.

Sci. USA 99(12), 7821. Gleiser, P., and L. Danon, 2003, Adv. Complex Syst. 6, 565. Glover, F., 1986, Comput. Oper. Res. 13(5), 533. Goldberg, A. V., and R. E. Tarjan, 1988, Journal of the ACM

35, 921.

Golub, G. H., and C. F. V. Loan, 1989, Matrix computations (John Hopkins University Press, Baltimore, USA). Go´mez, S., P. Jensen, and A. Arenas, 2009, Phys. Rev. E

80(1), 016114.

Good, B. H., Y. de Montjoye, and A. Clauset, 2009, eprint arXiv:0910.0165.

Gori, M., and A. Pucci, 2007, in IJCAI’07: Proceedings of the 20th international joint conference on Artiﬁcal intelligence (Morgan Kaufmann Publishers Inc., San Francisco, CA, USA), pp. 2766–2771.

Granovetter, M., 1973, Am. J. Sociol. 78, 1360. Gregory, S., 2007, in Proceedings of the 11th European Conference on Principles and Practice of Knowledge Discovery in Databases (PKDD 2007) (Springer-Verlag, Berlin, Germany), pp. 91–102.

Gregory, S., 2009, in Complex Networks, edited by S. Fortunato, R. Menezes, G. Mangioni, and V. Nicosia (Springer, Berlin, Germany), volume 207 of Studies on Computational Intelligence, pp. 47–62.

Gru¨nwald, P. D., I. J. Myung, and M. A. Pitt, 2005, Advances in Minimum Description Length: Theory and Applications (MIT Press, Cambridge, USA).

Gudkov, V., V. Montealegre, S. Nussinov, and Z. Nussinov, 2008, Phys. Rev. E 78(1), 016113. Guimera`, R., and L. A. N. Amaral, 2005, J. Stat. Mech.

P02001. Guimera`, R., and L. A. N. Amaral, 2005, Nature 433, 895. Guimera`, R., L. Danon, A. Dı´az-Guilera, F. Giralt, and

A. Arenas, 2003, Phys. Rev. E 68(6), 065103 (R). Guimera`, R., M. Sales-Pardo, and L. A. N. Amaral, 2007, Bioinformatics 23(13), 1616. Guimera`, R., M. Sales-Pardo, and L. A. N. Amaral, 2004, Phys. Rev. E 70(2), 025101 (R). Guimera`, R., M. Sales-Pardo, and L. A. N. Amaral, 2007,

Phys. Rev. E 76(3), 036102. Gusﬁeld, D., 2002, Inform. Process. Lett. 82(3), 159. Gustafsson, M., M. Ho¨rnquist, and A. Lombardi, 2006, Phys-

ica A 367, 559. Hagen, L., and A. B. Kahng, 1992, IEEE Trans. Comput. Aided Des. Integr. Circuits Syst. 11(9), 1074. Handcock, M. S., A. E. Raftery, and J. M. Tantrum, 2007, J. Roy. Stat. Soc. A 170(46), 1.

Harel, D., and Y. Koren, 2001, in FST TCS ’01: Proceedings of the 21st Conference on Foundations of Software Technology and Theoretical Computer Science (Springer-Verlag, London, UK), pp. 18–41.

Hastie, T., R. Tibshirani, and J. H. Friedman, 2001, The Elements of Statistical Learning (Springer, Berlin, Germany), ISBN 0387952845.

Hastings, M. B., 2006, Phys. Rev. E 74(3), 035102. Heimo, T., J. M. Kumpula, K. Kaski, and J. Sarama¨ki, 2008,

J. Stat. Mech. P08007. Hillier, F. S., and G. J. Lieberman, 2004, MP Introduction to Operations Research (McGraw-Hill, New York, USA). Hlaoui, A., and S. Wang, 2004, in Neural Networks and Computational Intelligence, pp. 158–163. Hofman, J. M., and C. H. Wiggins, 2008, Phys. Rev. Lett.

100(25), 258701.

Holland, J. H., 1992, Adaptation in natural and artiﬁcial systems (MIT Press, Cambridge, USA). Holland, P., K. B. Laskey, and S. Leinhardt, 1983, Soc. Netw.

5, 109.

Holme, P., M. Huss, and H. Jeong, 2003, Bioinformatics

19(4), 532.

Holmstro¨m, E., N. Bock, and J. Bra¨nnlund, 2009, Physica D

238, 1161.

Holzapfel, K., S. Kosub, M. G. Maa, and H. Ta¨ubig, 2003, in

CIAC, edited by R. Petreschi, G. Persiano, and R. Silvestri (Springer), volume 2653 of Lecture Notes in Computer Science, pp. 201–212.

Homans, G. C., 1950, The Human Groups (Harcourt, Brace & Co., New York). Hopcroft, J., O. Khan, B. Kulis, and B. Selman, 2004, Proc. Natl. Acad. Sci. USA 101, 5249. Hu, Y., H. Chen, P. Zhang, M. Li, Z. Di, and Y. Fan, 2008, Phys. Rev. E 78(2), 026121. Hu, Y., M. Li, P. Zhang, Y. Fan, and Z. Di, 2008, Phys. Rev.

E 78(1), 016115. Huﬀman, D. A., 1952, Proc. IRE 40(9), 1098. Hughes, B. D., 1995, Random Walks and Random Environ-

ments: Random Walks Vol. 1 (Clarendon Press, Oxford, UK).

Hui, P., E. Yoneki, S.-Y. Chan, and J. Crowcroft, 2007, in Proc. MobiArch. Ispolatov, I., I. Mazo, and A. Yuryev, 2006, J. Stat. Mech.

###### P09014.

Itzkovitz, S., R. Levitt, N. Kashtan, R. Milo, M. Itzkovitz, and U. Alon, 2005, Phys. Rev. E 71(1), 016127.

Jin, R. K.-X., D. C. Parkes, and P. J. Wolfe, 2007, in Proc. AAAI Workshop on Plan, Activity and Intent Recognition (PAIR), pp. 66–73.

Jonsson, P. F., T. Cavanna, D. Zicha, and P. A. Bates, 2006, BMC Bioinf. 7, 2. Jordan, M. I., Z. Ghahramani, T. S. Jaakkola, and L. K. Saul, 1999, Mach. Learn. 37(2), 183. Junker, B. H., and F. Schreiber, 2008, Analysis of Biological

Networks (Wiley-Interscience, New York, USA). Kaplan, T. D., and S. Forrest, 2008, eprint arXiv:0801.3290. Karloﬀ, H., 1991, Linear Programming (Birkha¨user Verlag,

Basel, Switzerland). Karrer, B., E. Levina, and M. E. J. Newman, 2008, Phys. Rev. E 77(4), 046119. Kernighan, B. W., and S. Lin, 1970, Bell System Tech. J. 49, 291. Kim, M.-S., and J. Han, 2009, in Proceedings of 2009 Int. Conf. on Very Large Data Bases (Lyon, France). Kim, Y., S.-W. Son, and H. Jeong, 2009, eprint arXiv:0902.3728. Kirkpatrick, S., C. D. Gelatt, and M. P. Vecchi, 1983, Science

220, 671. Klein, D. J., and M. Randic, 1993, J. Math. Chem. 12, 81. Kleinberg, J., 2002, in Advances in NIPS 15 (MIT Press,

Boston, USA), pp. 446–453. Koskinen, J. H., and T. A. B. Snijders, 2007, J. Stat. Plan. Infer. 137(12), 3930. Kottak, C. P., 2004, Cultural Anthropology (McGraw-Hill, New York, USA). Krause, A. E., K. A. Frank, D. M. Mason, R. E. Ulanowicz,

and W. W. Taylor, 2003, Nature 426, 282. Krawczyk, M. J., 2008, Phys. Rev. E 77(6), 065701. Krawczyk, M. J., and K. Kulakowski, 2007, eprint

arXiv:0709.0923. Krishnamurthy, B., and J. Wang, 2000, SIGCOMM Comput. Commun. Rev. 30(4), 97. Kullback, S., and R. A. Leibler, 1951, Annals of Mathematical Statistics 22, 49.

Kumar, R., J. Novak, P. Raghavan, and A. Tomkins, 2003, in WWW ’03: Proceedings of the twelfth international conference on the World Wide Web (ACM Press), pp. 568–576.

Kumar, R., J. Novak, and A. Tomkins, 2006, in KDD ’06: Proceedings of the 12th ACM SIGKDD international con-

ference on Knowledge discovery and data mining (ACM, New York, NY, USA), pp. 611–617.

Kumpula, J. M., M. Kivela¨, K. Kaski, and J. Sarama¨ki, 2008, Phys. Rev. E 78(2), 026109.

Kumpula, J. M., J. Sarama¨ki, K. Kaski, and J. Kerte´sz, 2007a, in Noise and Stochastics in Complex Systems and Finance, volume 6601 of SPIE Conference Series, p. 660116.

Kumpula, J. M., J. Sarama¨ki, K. Kaski, and J. Kerte´sz, 2007b, Eur. Phys. J. B 56, 41. Kuramoto, Y., 1984, Chemical Oscillations, Waves and Turbulence (Springer-Verlag, Berlin, Germany). Lambiotte, R., J. . Delvenne, and M. Barahona, 2008, eprint arXiv:0812.1770. Lancichinetti, A., and S. Fortunato, 2009, Phys. Rev. E 80(1), 016118. Lancichinetti, A., and S. Fortunato, 2009, Phys. Rev. E 80(1), 056117. Lancichinetti, A., S. Fortunato, and J. Kertesz, 2009, New J. Phys. 11(3), 033015. Lancichinetti, A., S. Fortunato, and F. Radicchi, 2008, Phys. Rev. E 78(4), 046110. Lancichinetti, A., F. Radicchi, and J. J. Ramasco, 2009,

eprint arXiv:0907.3708. Lanczos, C., 1950, J. Res. Natl. Bur. Stand. 45, 255. Latapy, M., and P. Pons, 2005, Lect. Notes Comp. Sci. 3733,

284. Latora, V., and M. Marchiori, 2001, Phys. Rev. Lett. 87(19), 198701. Lehmann, S., and L. K. Hansen, 2007, Eur. Phys. J. B 60, 83. Lehmann, S., M. Schwartz, and L. K. Hansen, 2008, Phys. Rev. E 78(1), 016108. Leicht, E. A., and M. E. J. Newman, 2008, Phys. Rev. Lett.

100(11), 118703.

Leskovec, J., L. Backstrom, R. Kumar, and A. Tomkins, 2008, in KDD ’08: Proceeding of the 14th ACM SIGKDD international conference on Knowledge discovery and data mining (ACM, New York, NY, USA), pp. 462–470.

- Leskovec, J., J. Kleinberg, and C. Faloutsos, 2005, in KDD ’05: Proceedings of the eleventh ACM SIGKDD international conference on Knowledge discovery in data mining (ACM, New York, NY, USA), pp. 177–187.
- Leskovec, J., K. J. Lang, A. Dasgupta, and M. W. Mahoney, 2008, eprint arXiv:0810.1355.


Leung, I. X. Y., P. Hui, P. Lio`, and J. Crowcroft, 2009, Phys. Rev. E 79(6), 066107. Lewis, A. C. F., N. S. Jones, M. A. Porter, and C. M. Deane, 2009, eprint arXiv:0904.0989.

Li, D., I. Leyva, J. A. Almendral, I. Sendi˜na-Nadal, J. M. Buldu´, S. Havlin, and S. Boccaletti, 2008a, Phys. Rev. Lett. 101(16), 168701.

Li, Z., S. Zhang, R.-S. Wang, X.-S. Zhang, and L. Chen, 2008b, Phys. Rev. E 77(3), 036109.

Liben-Nowell, D., and J. Kleinberg, 2003, in CIKM ’03: Proceedings of the twelfth international conference on Information and knowledge management (ACM, New York, NY, USA), pp. 556–559.

Lin, Y.-R., Y. Chi, S. Zhu, H. Sundaram, and B. L. Tseng, 2008, in WWW ’08: Proceedings of the 17th international conference on the World Wide Web (ACM, New York, NY, USA), pp. 685–694.

Liu, X., D. Li, S. Wang, and Z. Tao, 2007, in ICCS ’07: Proceedings of the 7th international conference on Compu-

tational Science, Part II (Springer-Verlag, Berlin, Heidelberg), pp. 657–664.

Lloyd, S., 1982, IEEE Trans. Inf. Theory 28(2), 129. Long, B., X. Xu, Z. Zhang, and P. S. Yu, 2007, in ICDM ’07: Proceedings of the 2007 Seventh IEEE International Conference on Data Mining (IEEE Computer Society, Washington, DC, USA), pp. 232–241.

Lov´asz, L., 1993, Combinatorial Problems and Exercises (North-Holland, Amsterdam, The Netherlands). Luccio, F., and M. Sami, 1969, IEEE Trans. Circuit Th. CT

16, 184. Luce, R. D., 1950, Psychometrika 15(2), 169. Luce, R. D., and A. D. Perry, 1949, Psychometrika 14(2), 95.  Luczak, T., 1992, in Proceedings of the Symposium on Ran-

dom Graphs, Pozna´n 1989 (John Wiley & Sons, New York, USA), pp. 165–182.

Lusseau, D., 2003, Proc. Royal Soc. London B 270, S186. von Luxburg, U., 2006, A tutorial on spectral clustering, Tech-

nical Report 149, Max Planck Institute for Biological Cybernetics.

Mackay, D. J. C., 2003, Information Theory, Inference, and Learning Algorithms (Cambridge University Press, Cambridge, UK).

MacQueen, J. B., 1967, in Proc. of the ﬁfth Berkeley Symposium on Mathematical Statistics and Probability, edited by L. M. L. Cam and J. Neyman (University of California Press, Berkeley, USA), volume 1, pp. 281–297.

Mancoridis, S., B. S. Mitchell, C. Rorres, Y. Chen, and E. R. Gansner, 1998, in IWPC ’98: Proceedings of the 6th International Workshop on Program Comprehension (IEEE Computer Society, Washington, DC, USA). Mantegna, R. N., 1999, Eur. Phys. J. B 11, 193. Mantegna, R. N., and H. E. Stanley, 2000, An introduction to

econophysics: correlations and complexity in ﬁnance (Cambridge University Press, New York, USA).

- Massen, C. P., and J. P. K. Doye, 2005, Phys. Rev. E 71(4), 046101.
- Massen, C. P., and J. P. K. Doye, 2006, eprint condmat/0610077.


Matsuda, H., T. Ishihara, and A. Hashimoto, 1999, Theor. Comp. Sci. 210, 305. Matula, D. W., and F. Shahrokhi, 1990, Discrete Appl. Math.

27(1-2), 113.

Medus, A., G. Acu˜na, and C. O. Dorso, 2005, Physica A 358, 593. Mei, J., S. He, G. Shi, Z. Wang, and W. Li, 2009, New Journal

of Physics 11(4), 043025. Meila˘, M., 2007, J. Multivar. Anal. 98(5), 873. Meila˘, M., and D. Heckerman, 2001, Mach. Learn. 42(1), 9. Meila˘, M., and J. Shi, 2001, in AI and STATISTICS (AIS-

TATS) 2001.

Mendes, J. F. F., and S. N. Dorogovtsev, 2003, Evolution of Networks: from biological nets to the Internet and WWW (Oxford University Press, Oxford, UK).

Me´zard, M., and G. Parisi, 2003, J. Stat. Phys. 111, 1. Mezard, M., G. Parisi, and M. Virasoro, 1987, Spin glass

theory and beyond (World Scientiﬁc Publishing Company, Singapore).

Middleton, A. A., and D. S. Fisher, 2002, Phys. Rev. B

65(13), 134411. Milgram, S., 1967, Psychol. Today 2, 60. Milo, R., S. Shen-Orr, S. Itzkovitz, N. Kashtan, D. Chklovskii,

and U. Alon, 2002, Science 298(5594), 824. Mirkin, B., 1996, Mathematical classiﬁcation and clustering

(Kluwer Academic Press, Norwell, USA). Mitrovi´c, M., and B. Tadic´, 2009, Phys. Rev. E 80(2), 026123. Mokken, R. J., 1979, Qual. Quant. 13(2), 161. Molloy, M., and B. Reed, 1995, Random Struct. Algor. 6, 161. Moody, J., and D. R. White, 2003, Am. Sociol. Rev. 68(1),

103. Muﬀ, S., F. Rao, and A. Caﬂisch, 2005, Phys. Rev. E 72(5), 056107. Mungan, M., and J. J. Ramasco, 2008, eprint arXiv:0809.1398.

Nadler, B., S. Lafon, R. R. Coifman, and I. G. Kevrekidis, 2006, Applied and Computational Harmonic Analysis 21(1), 113.

Narasimhamurthy, A., D. Greene, N. Hurley, and P. Cunningham, 2008, in Proc. 19th Irish Conference on Artiﬁcial Intelligence and Cognitive Science (AICS’08).

Nelson, D. L., C. L. McEvoy, and T. A. Schreiber, 1998, The university of south ﬂorida word association, rhyme, and word fragment norms.

Nepusz, T., A. Petro´czi, L. Ne´gyessy, and F. Bazso´, 2008, Phys. Rev. E 77(1), 016107. Newman, M. E. J., 2001, Proc. Nat. Acad. Sci. USA 98(2), 404.

- Newman, M. E. J., 2003, SIAM Rev. 45(2), 167.
- Newman, M. E. J., 2004, Phys. Rev. E 70(5), 056131.

- Newman, M. E. J., 2004a, Eur. Phys. J. B 38, 321.
- Newman, M. E. J., 2004b, Phys. Rev. E 69(6), 066133.


- Newman, M. E. J., 2005, Soc. Netw. 27, 39.
- Newman, M. E. J., 2006a, Phys. Rev. E 74(3), 036104. Newman, M. E. J., 2006b, Proc. Natl. Acad. Sci. USA 103,


8577.

Newman, M. E. J., and T. Barkema, 1999, Monte Carlo Methods in Statistical Physics (Oxford University Press, Oxford, UK).

Newman, M. E. J., and M. Girvan, 2004, Phys. Rev. E 69(2), 026113. Newman, M. E. J., and E. A. Leicht, 2007, Proc. Natl. Acad. Sci. USA 104, 9564.

Ng, A. Y., M. I. Jordan, and Y. Weiss, 2001, in Advances in Neural Information Processing Systems, edited by T. G. Dietterich, S. Becker, and Z. Ghahramani (MIT Press, Cambridge, USA), volume 14.

Nicosia, V., G. Mangioni, V. Carchiolo, and M. Malgeri, 2009, J. Stat. Mech. P03024. Nishikawa, T., A. E. Motter, Y.-C. Lai, and F. C. Hoppen-

steadt, 2003, Phys. Rev. Lett. 91(1), 014101. Noack, A., 2009, Phys. Rev. E 79(2), 026102. Noack, A., and R. Rotta, 2009, in SEA ’09: Proceedings of the

8th International Symposium on Experimental Algorithms (Springer-Verlag, Berlin, Heidelberg), pp. 257–268.

- Noh, J. D., and H. Rieger, 2001, Phys. Rev. Lett. 87(17), 176102.
- Noh, J. D., and H. Rieger, 2002, Phys. Rev. E 66(3), 036117. Nowicki, K., and T. A. B. Snijders, 2001, J. Am. Stat. Assoc.


96(455).

Ohkubo, J., and K. Tanaka, 2006, J. Phys. Soc. Jpn. 75(11), 115001. Onnela, J.-P., A. Chakraborti, K. Kaski, J. Kert´esz, and A. Kanto, 2003, Phys. Rev. E 68(5), 056110. Onnela, J.-P., A. Chakraborti, K. Kaski, and J. Kert´esz, 2002, Eur. Phys. J. B 30(3), 285.

Orponen, P., and S. E. Schaeﬀer, 2005, in Proceedings of the 4th International Workshop on Eﬃcient and Experimental Algorithms (WEA’05, Santorini, Greece, May

2005), edited by S. Nikoletseas (Springer-Verlag, BerlinHeidelberg), volume 3503 of Lect. Notes Comp. Sci., pp. 524–533.

Palla, G., A.-L. Baraba´si, and T. Vicsek, 2007, Nature 446, 664. Palla, G., I. Dere´nyi, I. Farkas, and T. Vicsek, 2005, Nature

435, 814.

Palmer, C. R., and C. Faloutsos, 2003, in Proceedings of PAKDD 2003, pp. 486–500. Papadimitriou, C. M., 1994, Computational complexity (Addison-Wesley, Reading, USA). Papadopoulos, S., A. Skusa, A. Vakali, Y. Kompatsiaris, and N. Wagner, 2009, eprint arXiv:0902.0871. Pastor-Satorras, R., and A. Vespignani, 2001, Phys. Rev. Lett. 86(14), 3200.

Pastor-Satorras, R., and A. Vespignani, 2004, Evolution and Structure of the Internet: A Statistical Physics Approach (Cambridge University Press, New York, NY, USA).

Peeters, R., 2003, Discrete Appl. Math. 131, 651. Perkins, C. E., 2001, Ad Hoc Networking (Addison-Wesley,

Reading, USA).

Peterson, C., and J. R. Anderson, 1987, Compl. Syst. 1, 995. Pikovsky, A., M. G. Rosenblum, and J. Kurths, 2001, Syn-

chronization : A Universal Concept in Nonlinear Sciences (Cambridge University Press, Cambridge, UK).

Pimm, S. L., 1979, Theor. Popul. Biol. 16, 144. Pinney, J. W., and D. R. Westhead, 2006, in Interdisci-

plinary Statistics and Bioinformatics (Leeds University Press, Leeds, UK), pp. 87–90.

Pluchino, A., V. Latora, and A. Rapisarda, 2005, Int. J. Mod. Phys. C 16, 515. Pollner, P., G. Palla, and T. Vicsek, 2006, Europhys. Lett.

73, 478.

Po´lya, G., and G. Szego¨, 1998, Problems and Theorems in

Analysis I (Springer-Verlag, Berlin, Germany). Pons, P., 2006, eprint arXiv:cs/0608050. Porter, M. A., P. J. Mucha, M. E. J. Newman, and A. J.

Friend, 2007, Physica A 386, 414.

Porter, M. A., P. J. Mucha, M. E. J. Newman, and C. M. Warmbrand, 2005, Proc. Natl. Acad. Sci. USA 102, 7057. Porter, M. A., J.-P. Onnela, and P. J. Mucha, 2009, Notices

of the American Mathematical Society 56(9), 1082.

Pothen, A., 1997, Graph Partitioning Algorithms with Applications to Scientiﬁc Computing, Technical Report, Norfolk, VA, USA.

Price, D. D., 1976, J. Am. Soc. Inform. Sci. 27(5), 292. Pujol, J. M., J. Be´jar, and J. Delgado, 2006, Phys. Rev. E

74(1), 016107.

Radicchi, F., C. Castellano, F. Cecconi, V. Loreto, and

- D. Parisi, 2004, Proc. Natl. Acad. Sci. USA 101, 2658.

Raghavan, U. N., R. Albert, and S. Kumara, 2007, Phys. Rev.

- E 76(3), 036106.


Ramasco, J. J., and M. Mungan, 2008, Phys. Rev. E 77(3), 036122. Rand, W. M., 1971, J. Am. Stat. Assoc. 66(336), 846.

- Rattigan, M. J., M. Maier, and D. Jensen, 2006, in SIGKDD’06: Proceedings of the 12th international conference on Knowledge Discovery and Data Mining, edited by T. Eliassi-Rad, L. H. Ungar, M. Craven, and D. Gunopulos (ACM), pp. 357–366.
- Rattigan, M. J., M. Maier, and D. Jensen, 2007, in ICML ’07: Proceedings of the 24th international conference on Machine learning (ACM, New York, NY, USA), pp. 783– 790.


Ravasz, E., and A.-L. Baraba´si, 2003, Phys. Rev. E 67(2), 026112. Ravasz, E., A. L. Somera, D. A. Mongru, Z. N. Oltvai, and A.-L. Barab´asi, 2002, Science 297(5586), 1551.

Reddy, K. P., M. Kitsuregawa, P. Sreekanth, and S. S. Rao, 2002, in DNIS ’02: Proceedings of the Second International Workshop on Databases in Networked Information Systems (Springer-Verlag, London, UK), pp. 188–200.

Reichardt, J., and S. Bornholdt, 2004, Phys. Rev. Lett.

93(21), 218701.

- Reichardt, J., and S. Bornholdt, 2006a, Phys. Rev. E 74(1), 016110.
- Reichardt, J., and S. Bornholdt, 2006b, Physica D 224, 20. Reichardt, J., and S. Bornholdt, 2007, J. Stat. Mech. P06016. Reichardt, J., and S. Bornholdt, 2007, Phys. Rev. E 76(1),


015102 (R). Reichardt, J., and M. Leone, 2008, Phys. Rev. Lett. 101(7), 078701. Reichardt, J., and D. R. White, 2007, Eur. Phys. J. B 60, 217. Ren, W., G. Yan, X. Liao, and L. Xiao, 2009, Phys. Rev. E

79(3), 036111.

Rhodes, C. J., and E. M. J. Keefe, 2007, J. Oper. Res. Soc.

58(12), 1605. Rice, S. A., 1927, Am. Polit. Sci. Rev. 21, 619. Richardson, T., P. J. Mucha, and M. A. Porter, 2009, Phys.

Rev. E 80(3), 036111. Rissanen, J., 1978, Automatica 14, 465. Rives, A. W., and T. Galitski, 2003, Proc. Natl. Acad. Sci.

USA 100(3), 1128. Rodrigues, F. A., G. Travieso, and L. da F. Costa, 2007, Int. J. Mod. Phys. C 18, 937.

- Ronhovde, P., and Z. Nussinov, 2008, eprint arXiv:0803.2548.
- Ronhovde, P., and Z. Nussinov, 2009, Phys. Rev. E 80(1), 016109.


Rosvall, M., D. Axelsson, and C. T. Bergstrom, 2009, eprint arXiv:0906.1405.

- Rosvall, M., and C. T. Bergstrom, 2007, Proc. Natl. Acad. Sci. USA 104, 7327.
- Rosvall, M., and C. T. Bergstrom, 2008, eprint arXiv:0812.1242.


Rosvall, M., and C. T. Bergstrom, 2008, Proc. Natl. Acad. Sci. USA 105, 1118.

Rowicka, M., and A. Kudlicki, 2004, in Bayesian Inference and Maximum Entropy Methods in Science and Engineering: 24th International Workshop on Bayesian Inference and Maximum Entropy Methods in Science and Engineering, edited by R. Fischer, R. Preuss, and U. von Toussaint (American Institute of Physics, Melville, USA), volume 735, pp. 283–288.

- Ruan, J., and W. Zhang, 2007, in ICDM ’07: Proceedings of the 2007 Seventh IEEE International Conference on Data Mining (IEEE Computer Society, Washington, DC, USA), pp. 643–648.
- Ruan, J., and W. Zhang, 2008, Phys. Rev. E 77(1), 016104. S.-W. Son, H. Jeong, and J.D. Noh, 2006, Eur. Phys. J. B


50(3), 431.

Saerens, M., F. Fouss, L. Yen, and P. Dupont, 2004, in Proc. Eur. Conf. on Machine Learning, URL citeseer.ist.psu. edu/saerens04principal.html.

Sales-Pardo, M., R. Guimera`, A. A. Moreira, and L. A. N. Amaral, 2007, Proc. Natl. Acad. Sci. USA 104, 15224. Sawardecker, E. N., M. Sales-Pardo, and L. A. N. Amaral, 2009, Eur. Phys. J. B 67, 277.

Schaeﬀer, S. E., 2007, Comput. Sci. Rev. 1(1), 27. Schenker, A., M. Last, H. Bunke, and A. Kandel, 2003, in IbPRIA’03: Proceedings of the 1st Iberian Conference on Pattern Recognition and Image Analysis, edited by F. J. P. Lo´pez, A. C. Campilho, N. P. de la Blanca, and A. Sanfeliu (Springer), volume 2652 of Lecture Notes in Computer Science, pp. 935–942.

Schuetz, P., and A. Caﬂisch, 2008a, Phys. Rev. E 77(4), 046112. Schuetz, P., and A. Caﬂisch, 2008b, Phys. Rev. E 78(2),

026112. Schwarz, G., 1978, Ann. Stat. 6(2), 461. Scott, J., 2000, Social Network Analysis: A Handbook (SAGE

Publications, London, UK). Seidman, S. B., 1983, Soc. Netw. 5, 269. Seidman, S. B., and B. L. Foster, 1978, J. Math. Sociol. 6,

139. Sen, T. Z., A. Kloczkowski, and R. L. Jernigan, 2006, BMC Bioinf. 7(1), 355. Shen, H., X. Cheng, K. Cai, and M.-B. Hu, 2009, Physica A

388, 1706.

Shen, H.-W., X.-Q. Cheng, and J.-F. Guo, 2009, J. Stat. Mech. P07042. Sherrington, D., and S. Kirkpatrick, 1975, Phys. Rev. Lett.

35, 1792.

Shi, J., and J. Malik, 1997, in CVPR ’97: Proceedings of the 1997 Conference on Computer Vision and Pattern Recognition (CVPR ’97) (IEEE Computer Society, Washington, DC, USA), p. 731.

Shi, J., and J. Malik, 2000, IEEE Transactions on Pattern Analysis and Machine Intelligence 22(8), 888.

Sı´ma,ˇ J., and S. E. Schaeﬀer, 2006, in Proceedings of the Thirty-second International Conference on Current Trends in Theory and Practice of Computer Science (Sofsem 06), edited by J. Wiedermann, G. Tel, J. Pokorn´y, M. Bielikova´, and J. Stullerˇ (Springer-Verlag, Berlin/Heidelberg, Germany), volume 3831 of Lecture Notes in Computer Science, pp. 530–537.

Simon, H. A., 1962, Proc. Am. Phil. Soc. 106(6), 467. Simon, H. A., 1955, Biometrika 42, 425. Simonsen, I., 2005, Physica A 357(2), 317. Simonsen, I., K. Astrup Eriksen, S. Maslov, and K. Sneppen,

2004, Physica A 336, 163. Slanina, F., and Y.-C. Zhang, 2005, Acta Phys. Pol. B 36,

2797. Snijders, T. A. B., and K. Nowicki, 1997, J. Classif. 14, 75. de Solla Price, D. J., 1965, Science 169, 510. Solomonoﬀ, R., and A. Rapoport, 1951, Bull. Math. Biophys.

13, 107.

Spielman, D. A., and S.-H. Teng, 1996, in IEEE Symposium on Foundations of Computer Science, pp. 96–105. Spirin, V., and L. A. Mirny, 2003, Proc. Natl. Acad. Sci. USA

100(21), 12123.

Stanley, R. P., 1997, Enumerative combinatorics, Vol. I (Cambridge University Press, Cambridge, UK). Steenstrup, M., 2001, Cluster-Based Networks (Addison Wesley, Reading, USA), chapter 4, pp. 75–138. Stewart, G. W., and J.-G. Sun, 1990, Matrix Perturbation Theory (Academic Press, New York, USA). Suaris, P. R., and G. Kedem, 1988, IEEE Trans. Circuits Syst.

35, 294.

Sun, J., C. Faloutsos, S. Papadimitriou, and P. S. Yu, 2007, in KDD ’07: Proceedings of the 13th ACM SIGKDD international conference on Knowledge discovery and data mining

(ACM, New York, USA), pp. 687–696. Sun, Y., B. Danila, K. Josic, and K. E. Bassler, 2009, Europhys. Lett. 86(2), 28004. Tasgin, M., A. Herdagdelen, and H. Bingol, 2007, eprint

arXiv:0711.0491. Tibe´ly, G., and J. Kerte´sz, 2008, Physica A 387, 4982. Tishby, N., F. Pereira, and W. Bialek, 1999, in Proceedings of

the 37-th Annual Allerton Conference on Communication, Control and Computing, pp. 368–377.

Tong, H., C. Faloutsos, and J.-Y. Pan, 2008, Knowl. Inf. Syst.

14(3), 327.

Traag, V. A., and J. Bruggeman, 2009, Phys. Rev. E 80(3), 036115. Traud, A. L., E. D. Kelsic, P. J. Mucha, and M. A. Porter,

2008, eprint arXiv:0809.0690. Travers, J., and S. Milgram, 1969, Sociometry 32, 425. Tumminello, M., F. Lillo, and R. N. Mantegna, 2008, eprint

arXiv:0809.4615.

Tyler, J. R., D. M. Wilkinson, and B. A. Huberman, 2003, in Communities and technologies (Kluwer, B.V., Deventer, The Netherlands), pp. 81–96.

Vazquez, A., 2008, eprint arXiv:0805.2689. Vazquez, A., 2008, Phys. Rev. E 77(6), 066106. Vragovi´c, I., and E. Louis, 2006, Phys. Rev. E 74(1), 016105. Wakita, K., and T. Tsurumi, 2007, eprint arXiv:cs/0702048. Wallace, C. S., and D. M. Boulton, 1968, The Computer Jour-

nal 11(2), 185. Wallace, D. L., 1983, J. Am. Stat. Assoc. 78, 569. Wang, G., Y. Shen, and M. Ouyang, 2008, Comput. Math.

Appl. 55(12), 2746. Ward, J. H., 1963, J. Am. Stat. Assoc. 58(301), 236. Wasserman, S., and K. Faust, 1994, Social network analysis

(Cambridge University Press, Cambridge, UK). Watts, D., and S. Strogatz, 1998, Nature 393, 440. Watts, D. J., 2003, Small Worlds : The Dynamics of Net-

works between Order and Randomness (Princeton University Press, Princeton, USA).

Wei, Y.-C., and C.-K. Cheng, 1989, in Proceedings of IEEE International Conference on Computer Aided Design (Institute of Electrical and Electronics Engineers, New York), pp. 298–301.

Weinan, E., T. Li, and E. Vanden-Eijnden, 2008, Proc. Natl. Acad. Sci. USA 105, 7907. Weiss, R. S., and E. Jacobson, 1955, Am. Sociol. Rev. 20,

661. White, D. R., and K. P. Reitz, 1983, Soc. Netw. 5, 193. White, S., and P. Smyth, 2003, in KDD ’03: Proceedings of the ninth ACM SIGKDD international conference on Knowledge discovery and data mining (ACM, New York, NY, USA), pp. 266–275.

White, S., and P. Smyth, 2005, in Proceedings of SIAM In-

ternational Conference on Data Mining, pp. 76–84. Wilkinson, D. M., and B. A. Huberman, 2004, Proc. Natl. Acad. Sci. U.S.A. 101, 5241.

Williams, R. J., and N. D. Martinez, 2000, Nature 404, 180. Winkler, R. L., 2003, Introduction to Bayesian Inference and

Decision (Probabilistic Publishing, Gainesville, USA).

Wu, A. Y., M. Garland, and J. Han, 2004, in KDD ’04: Proceedings of the tenth ACM SIGKDD international conference on Knowledge discovery and data mining (ACM Press, New York, NY, USA), pp. 719–724.

Wu, F., and B. A. Huberman, 2004, Eur. Phys. J. B 38, 331. Wu, F. Y., 1982, Rev. Mod. Phys. 54(1), 235. Xiang, B., E.-H. Chen, and T. Zhou, 2009, in Complex Networks, edited by S. Fortunato, R. Menezes, G. Mangioni, and V. Nicosia (Springer Verlag, Berlin/Heidelberg, Germany), volume 207 of Studies in Computational Intelligence, pp. 73–81.

Xu, G., S. Tsoka, and L.G. Papageorgiou, 2007, Eur. Phys.

J. B 60(2), 231. Yang, B., and J. Liu, 2008, ACM Trans. Web 2(1), 1. Ye, Z., S. Hu, and J. Yu, 2008, Phys. Rev. E 78(4), 046115. Yen, L., F. Fouss, C. Decaestecker, P. Francq, and M. Saerens,

2007, in PAKDD, pp. 1037–1045. Yen, L., F. Fouss, C. Decaestecker, P. Francq, and M. Saerens, 2009, Data Knowl. Eng. 68(3), 338. Yuta, K., N. Ono, and Y. Fujiwara, 2007, eprint

physics/0701168. Zachary, W. W., 1977, J. Anthropol. Res. 33, 452. Zanghi, H., C. Ambroise, and V. Miele, 2008, Pattern Recogn.

41(12), 3592. Zarei, M., and K. A. Samani, 2009, Physica A 388, 1721. Zhang, A., 2009, Protein Interaction Networks (Cambridge

University Press, Cambridge, UK). Zhang, P., M. Li, J. Wu, Z. Di, and Y. Fan, 2006, Physica A

367, 577.

Zhang, P., J. Wang, X. Li, Z. Di, and Y. Fan, 2007, eprint arXiv:0710.0117. Zhang, S., R.-S. Wang, and X.-S. Zhang, 2007, Physica A

374, 483.

Zhang, Y., A. J. Friend, A. L. Traud, M. A. Porter, J. H. Fowler, and P. J. Mucha, 2008, Physica A 387(7), 1705.

- Zhou, H., 2003a, Phys. Rev. E 67(6), 061901.
- Zhou, H., 2003b, Phys. Rev. E 67(4), 041908. Zhou, H., and R. Lipowsky, 2004, Lect. Notes Comp. Sci.


3038, 1062.

Zhou, T., J.-G. Liu, and B.-H. Wang, 2006, Chin. Phys. Lett.

23, 2327.

Ziv, E., M. Middendorf, and C. H. Wiggins, 2005, Phys. Rev. E 71(4), 046117.

