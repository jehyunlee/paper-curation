arXiv:cond-mat/9910332v1[cond-mat.dis-nn]21 Oct 1999

Emergence of Scaling in Random Networks

Albert-L´aszl´o Barab´asi∗ and R´eka Albert

Department of Physics, University of Notre-Dame, Notre-Dame, IN 46556

Systems as diverse as genetic networks or the world wide web are best described as networks with complex topology. A common property of many large networks is that the vertex connectivities follow a scale-free power-law distribution. This feature is found to be a consequence of the two generic mechanisms that networks expand continuously by the addition of new vertices, and new vertices attach preferentially to already well connected sites. A model based on these two ingredients reproduces the observed stationary scalefree distributions, indicating that the development of large networks is governed by robust self-organizing phenomena that go beyond the particulars of the individual systems.

![image 1](Emergence of Scaling in Random Networks_images/imageFile1.png)

∗alb@nd.edu

The inability of contemporary science to describe systems composed of non-identical elements that have diverse and nonlocal interactions currently limits advances in many disciplines, ranging from molecular biology to computer science (1). The diﬃculty in describing these systems lies partly in their topology: many of them form rather complex networks, whose vertices are the elements of the system and edges represent the interactions between them. For example, living systems form a huge genetic network, whose vertices are proteins and genes, the edges representing the chemical interactions between them (2). At a diﬀerent organizational level, a large network is formed by the nervous system, whose vertices are the nerve cells, connected by axons (3). But equally complex networks occur in social science, where vertices are individuals or organizations, and the edges characterize the social interaction between them (4), or describe the world wide web (www), whose vertices are HTML documents connected by links pointing from one page to another (5, 6). Due to their large size and the complexity of the interactions, the topology of these networks is largely unknown.

Traditionally, networks of complex topology have been described using the random graph theory of Erd˝os and R´enyi (ER) (7), but in the absence of data on large networks the predictions of the ER theory were rarely tested in the real world. However, driven by the computerization of data acquisition, such topological information is increasingly available, raising the possibility of understanding the dynamical and topological stability of large networks.

In this paper we report on the existence of a high degree of self-organization characterizing the large scale properties of complex networks. Exploring several large databases describing the topology of large networks that span as diverse ﬁelds as the www or the citation patterns in science we show that, independent of the system and the identity of its constituents, the probability P(k) that a vertex in the network interacts with k other vertices decays as a power-law, following P(k) ∼ k−γ. This result indicates that large networks self-organize into a scale-free state, a feature unexpected by all existing random network models. To understand the origin of this scale invariance, we show that existing network models fail to

incorporate growth and preferential attachment, two key features of real networks. Using a model incorporating these two ingredients, we show that they are responsible for the powerlaw scaling observed in real networks. Finally, we argue that these ingredients play an easily identiﬁable and important role in the formation of many complex systems, implying that our results are relevant to a large class of networks observed in Nature.

While there are a large number of systems that form complex networks, detailed topological data is available only for a few. The collaboration graph of movie actors represents a well documented example of a social network. Each actor is represented by a vertex, two actors being connected if they were cast together in the same movie. The probability that an actor has k links (characterizing his or her popularity) has a power-law tail for large k, following P(k) ∼ k−γ

, where γactor = 2.3 ± 0.1 (Fig.1A). A more complex network with over 800 million vertices (8) is the www, where a vertex is a document and the edges are the links pointing from one document to another. The topology of this graph determines the web’s connectivity and, consequently, our eﬀectiveness in locating information on the www (5). Information about P(k) can be obtained using robots (6), indicating that the probability that k documents point to a certain webpage follows a power-law, with γwww = 2.1 ± 0.1 ( Fig.1B) (9). A network whose topology reﬂects the historical patterns of urban and industrial development is the electrical powergrid of western US, the vertices representing generators, transformers and substations, the edges corresponding to the high voltage transmission lines between them (10). Due to the relatively modest size of the network, containing only 4941 vertices, the scaling region is less prominent, but is nevertheless approximated with a power-law with an exponent γpower ≃ 4 (Fig.1C). Finally, a rather large, complex network is formed by the citation patterns of the scientiﬁc publications, the vertices standing for papers published in refereed journals, the edges representing links to the articles cited in a paper. Recently Redner (11) has shown that the probability that a paper is cited k times (representing the connectivity of a paper within the network) follows a power-law with exponent γcite = 3.

actor

The above examples (12) demonstrate that many large random networks share the com-

mon feature that the distribution of their local connectivity is free of scale, following a power-law for large k, with an exponent γ between 2.1 and 4 which is unexpected within the framework of the existing network models. The random graph model of ER (7) assumes that we start with N vertices, and connect each pair of vertices with probability p. In the model the probability that a vertex has k edges follows a Poisson distribution P(k) = e−λλk/k!, where λ = N

  pk(1 − p)N−1−k. In the small world model recently introduced by

  

N − 1 k

Watts and Strogatz (WS) (10), N vertices form a one-dimensional lattice, each vertex being connected to its two nearest and next-nearest neighbors. With probability p each edge is reconnected to a vertex chosen at random. The long-range connections generated by this process decrease the distance between the vertices, leading to a small-world phenomenon (13), often referred to as six degrees of separation (14). For p = 0 the probability distribution of the connectivities is P(k) = δ(k − z), where z is the coordination number in the lattice, while for ﬁnite p, P(k) is still peaked around z, but it gets broader (15). A common feature of the ER and WS models is that the probability of ﬁnding a highly connected vertex (that is, a large k) decreases exponentially with k, thus vertices with large connectivity are practically absent. In contrast, the power-law tail characterizing P(k) for the studied networks indicates that highly connected (large k) vertices have a large chance of occurring, dominating the connectivity.

There are two generic aspects of real networks that are not incorporated in these models. First, both models assume that we start with a ﬁxed number (N) of vertices, that are then randomly connected (ER model), or reconnected (WS model), without modifying N. In contrast, most real world networks are open, they form by the continuous addition of new vertices to the system, thus the number of vertices, N, increases throughout the lifetime of the network. For example, the actor network grows by the addition of new actors to the system, the www grows exponentially in time by the addition of new web pages (8), the research literature constantly grows by the publication of new papers. Consequently, a common feature of these systems is that the network continuously expands by the addition

of new vertices that are connected to the vertices already present in the system.

Second, the random network models assume that the probability that two vertices are connected is random and uniform. In contrast, most real networks exhibit preferential connectivity. For example, a new actor is cast most likely in a supporting role, with more established, well known actors. Consequently, the probability that a new actor is cast with an established one is much higher than casting with other less known actors. Similarly, a newly created webpage will more likely include links to well known, popular documents with already high connectivity, or a new manuscript is more likely to cite a well known and thus much cited paper than its less cited and consequently less known peer. These examples indicate that the probability with which a new vertex connects to the existing vertices is not uniform, but there is a higher probability to be linked to a vertex that already has a large number of connections.

We next show that a model based on these two ingredients naturally leads to the observed scale invariant distribution. To incorporate the growing character of the network, starting with a small number (m0) of vertices, at every timestep we add a new vertex with m(≤ m0) edges that link the new vertex to m diﬀerent vertices already present in the system. To incorporate preferential attachment, we assume that the probability Π that a new vertex will be connected to vertex i depends on the connectivity ki of that vertex, such that Π(ki) = ki/ j kj. After t timesteps the model leads to a random network with t + m0 vertices and mt edges. This network evolves into a scale-invariant state with the probability that a vertex has k edges following a power-law with an exponent γmodel = 2.9±0.1 (Fig.2A). As the power-law observed for real networks describes systems of rather diﬀerent sizes at diﬀerent stages of their development, it is expected that a correct model should provide a distribution whose main features are independent of time. Indeed, as Fig.2A demonstrates, P(k) is independent of time (and, subsequently, independent of the system size m0 + t), indicating that despite its continuous growth, the system organizes itself into a scale-free stationary state.

The development of the power-law scaling in the model indicates that growth and pref-

erential attachment play an important role in network development. To verify that both ingredients are necessary, we investigated two variants of the model. Model A keeps the growing character of the network, but preferential attachment is eliminated by assuming that a new vertex is connected with equal probability to any vertex in the system (that is, Π(k) = const = 1/(m0 + t − 1)). Such a model (Fig.2B) leads to P(k) ∼ exp(−βk), indicating that the absence of preferential attachment eliminates the scale-free feature of the distribution. In model B we start with N vertices and no edges. At each time step we randomly select a vertex and connect it with probability Π(ki) = ki/ j kj to vertex i in the system. While at early times the model exhibits power-law scaling, P(k) is not stationary: since N is constant, and the number of edges increases with time, after T ≃ N2 timesteps the system reaches a state in which all vertices are connected. The failure of models A and B indicates that both ingredients, namely growth and preferential attachment, are needed for the development of the stationary power-law distribution observed in Fig.1.

Due to the preferential attachment, a vertex that acquired more connections than another one will increase its connectivity at a higher rate, thus an initial diﬀerence in the connectivity between two vertices will increase further as the network grows. The rate at which a vertex acquires edges is ∂ki/∂t = ki/2t, which gives ki(t) = m(t/ti)0.5, where ti is the time at which vertex i was added to the system (see Fig.2C), a scaling property that could be directly tested once time-resolved data on network connectivity becomes available. Thus older (smaller ti) vertices increase their connectivity at the expense of the younger (larger ti) ones, leading with time to some vertices that are highly connected, a ”rich-gets-richer” phenomenon that can be easily detected in real networks. Furthermore, this property can be used to calculate γ analytically. The probability that a vertex i has a connectivity smaller than k, P(ki(t) < k), can be written as P(ti > m2t/k2). Assuming that we add the vertices at equal time intervals to the system, we obtain that P(ti > m2t/k2) = 1 − P(ti ≤ m2t/k2) = 1 − m2t/k2(t + m0). The probability density P(k) can be obtained from P(k) = ∂P(ki(t) < k)/∂k, which, at

long times, leads to the stationary solution

2m2 k3

P(k) =

,

![image 2](Emergence of Scaling in Random Networks_images/imageFile2.png)

giving γ = 3, independent of m. While it reproduces the observed scale-free distribution, the proposed model cannot be expected to account for all aspects of the studied networks. For this we need to model these systems in more detail. For example, in the model we assumed linear preferential attachment, that is Π(k) ∼ k. However, while in general Π(k) could have an arbitrary nonlinear form Π(k) ∼ kα, simulations indicate that scaling is present only for α = 1. Furthermore, the exponents obtained for the diﬀerent networks are scattered between 2.1 and 4. However, it is easy to modify our model to account for exponents diﬀerent from γ = 3. For example, if we assume that a fraction p of the links is directed, we obtain γ(p) = 3 − p, which is supported by numerical simulations (16). Finally, some networks evolve not only by adding new vertices, but by adding (and sometimes removing) connections between established vertices. While these and other system-speciﬁc features could modify the exponent γ, our model oﬀers the ﬁrst successful mechanism accounting for the scale-invariant nature of real networks.

Growth and preferential attachment are mechanisms common to a number of complex systems, including business networks (17, 18), social networks (describing individuals or organizations), transportation networks (19), etc. Consequently, we expect that the scaleinvariant state, observed in all systems for which detailed data has been available to us, is a generic property of many complex networks, its applicability reaching far beyond the quoted examples. A better description of these systems would help in understanding other complex systems as well, for which so far less topological information is available, including such important examples as genetic or signaling networks in biological systems. We often do not think of biological systems as open or growing, since their features are genetically coded. However, possible scale-free features of genetic and signaling networks could reﬂect the evolutionary history dominated by growth and aggregation of diﬀerent constituents, leading from simple molecules to complex organisms. With the fast advances in mapping

out genetic networks, answers to these questions might not be too far. Similar mechanisms could explain the origin of the social and economic disparities governing competitive systems, since the scale-free inhomogeneities are the inevitable consequence of self-organization due to the local decisions made by the individual vertices, based on information that is biased towards the more visible (richer) vertices, irrespective of the nature and the origin of this visibility.

References and Notes

- 1. R. Gallagher and T. Appenzeller, Science 284, 79 (1999); R. F. Service, Science 284,

80 (1999).

- 2. G. Weng, U. S. Bhalla, R. Iyengar, Science 284, 92 (1999).
- 3. C. Koch and G. Laurent, Science 284, 96 (1999).
- 4. S. Wasserman and K. Faust, Social Network Analysis, (Cambridge University Press,

Cambridge, 1994).

- 5. Members of the Clever project, Sci. Am 280, 54 (June 1999).
- 6. R. Albert, H. Jeong and A.-L. Barab´asi, Nature 401, 130 (1999), see also

http://www.nd.edu/∼networks.

- 7. P. Erd˝os, and A. R´enyi, Publ. Math. Inst. Hung. Acad. Sci 5, 17 (1960); B. Bollob´as,

Random Graphs (Academic Press, London, 1985).

- 8. S. Lawrence and C. L. Giles, Science 280, 98 (1998); Nature 400, 107 (1999).
- 9. Note that in addition to the distribution of incoming links, the www displays a number


of other scale-free features, characterizing the organization of the webpages within a domain [B. A. Huberman and L. A. Adamic, Nature 401, 131 (1999)], the distribution of searches [B. A. Huberman, P. L. T. Pirolli, J. E. Pitkow and R. J. Lukose, Science 280, 95 (1998)], or the number of links per webpage (6).

- 10. D. J. Watts and S. H. Strogatz, Nature 393, 440 (1998).
- 11. S. Redner, European Physical Journal B 4, 131 (1998).
- 12. We also studied the neural network of the worm Caenorhabditis elegans (3, 10) and


the benchmark diagram of a computer chip

(http://vlsicad.cs.ucla.edu/∼cheese/ispd98.html). We ﬁnd that P(k) for both is consistent with power-law tails, despite the fact that for C. elegans the relatively small size of the system (306 vertices) limits severely the data quality, while for the wiring diagram of the chips vertices with over 200 edges have been eliminated from the database.

- 13. S. Milgram, Psychol. Today 2, 60 (1967); M. Kochen (ed.) The Small World (Ablex,

Norwood, NJ, 1989).

- 14. J. Guare, Six Degrees of Separation: A play (Vintage Books, New York, 1990).
- 15. M. Barth´el´emy and L. A. N. Amaral, Phys. Rev. Lett. 82, 15 (1999).
- 16. Note that for most networks the connectivity m of the newly added vertices is not

constant. However, choosing m randomly will not change the exponent γ [Y. Tu, private communication].

- 17. W. B. Arthur, Science 284, 107 (1999).
- 18. Note that preferential attachment was also used to model correlations between stock

prices [L. A. N. Amaral and M. Barth´el´emy, private communication].

- 19. J. R. Banavar, A. Maritan and A. Rinaldo, Nature 399, 130 (1999).
- 20. We thank D. J. Watts for providing the C. elegans and the power grid data, B. C.


Tjaden for supplying the actor data, H. Jeong for collecting the data on the www and L. A. N. Amaral for helpful discussions. This work was partially supported by NSF Career Award DMR-9710998.

### FIGURES

10-1

100

100

# A B C

10-2

10-2

- 10-1
- 10-2
- 10-3
- 10-4


10-3

## P(k)

10-4

10-4

10-6

10-5

10-8

10-6

100 101 102 103

100 101 102 103 104

100 101

k

FIG. 1. The distribution function of connectivities for various large networks. (A) Actor collaboration graph with N = 212,250 vertices and average connectivity k = 28.78; (B) World wide web, N = 325,729, k = 5.46 (6); (C) Powergrid data, N = 4,941, k = 2.67. The dashed lines have slopes (A) γactor = 2.3, (B) γwww = 2.1 and (C) γpower = 4.

100

100 103

# A B C

10-2

10-2

- 100
- 101
- 102


P(k)

P(k)

k(t)i

10-4

10-4

10-6

| | |
|---|---|


10-6

10-8

100 101 102 103

100 101 102 103 104 105

0 20 40 60 80

k

t

k

FIG. 2. (A) The power-law connectivity distribution at t = 150,000 (o) and t = 200,000 (✷) as obtained from the model (see text), using m0 = m = 5. The slope of the dashed line is γ = 2.9. (B) The exponential connectivity distribution for model A, in the case of m0 = m = 1 (o), m0 = m = 3 (✷), m0 = m = 5 (✸) and m0 = m = 7 (△). (C) Time evolution of the connectivity for two vertices added to the system at t1 = 5 and t2 = 95. The dashed line has slope 0.5.

