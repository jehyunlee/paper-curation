The Price–Pareto growth model of networks with community
structure
Łukasz Brzozowskia,∗, Marek Gagolewskia,b, Grzegorz Siudemc and Barbara Żogała-Siudemb
aWarsaw University of Technology, Faculty of Mathematics and Information Science, ul. Koszykowa 75, 00-662 Warsaw, Poland
bSystems Research Institute, Polish Academy of Sciences, ul. Newelska 6, 01-447 Warsaw, Poland
cWarsaw University of Technology, Faculty of Physics, ul. Koszykowa 75, 00-662 Warsaw, Poland
A R T I C L E I N F O
Keywords:
rich-get-richer
power law
Matthew effect
Gini index
communities
citation networks
Abstract
We introduce a new analytical framework for modelling degree sequences in individual com-
munities of real-world networks, e.g., citations to papers in different fields. Our work is inspired
by a recent modification of the Price’s model, which assumes that citations are gained partly
accidentally, and to some extent preferentially. Our work addresses the need to represent the
heterogeneity of various scientific domains, as standard homogeneous models fail to capture the
distinct growth ratios and citing cultures of different fields. Extending the model to networks
with a community structure allows us to devise the analytical formulae for, amongst others, cita-
tion counts in each cluster and their inequality as described by the Gini index. We also show that
a citation count distribution in each community tends to a Pareto type II distribution. Thanks to
the derived model parameter estimators, the new model can be fitted to real citation and similar
networks.
1. Introduction
In recent years, there has been a surge of interest in analysing real-life network data, stimulated by the development
of neural architectures for graph processing, such as Graph Neural Networks (Scarselli et al., 2009) and Graph Con-
volutional Networks (Kipf and Welling, 2017), as well as the emergence of open-access repositories of real networks,
such as SNAP (Leskovec and Krevl, 2014), DBLP, or AMiner datasets. There is thus a growing need for theoretical
network models, as they provide solid grounds for statistical reasoning and allow for simplifying assumptions about
data. Citation graphs are among the most prominently analysed and modelled networks: the publications represent
vertices and bibliographic references are stored as directed edges. Such graphs help uncover patterns of knowledge dis-
semination, academic influence, and research trends over time (Newman, 2018) that are crucial topics in bibliometrics
and science of science (Milojević, 2025).
In our work, we are specifically interested in modelling real networks as iteratively growing random graphs with
a community (cluster, subgroup) structure. The communities play a significant role in many types of real graphs, such
as biological, urban (Fortunato, 2010), and social networks (Chen et al., 2014), but their role in modern modelling of
citation networks, where there is a division to scientific fields and knowledge domains, is often underplayed. Also, the
problem of community detection has for a long time been prevalent in the area of network science (Fortunato, 2010).
While the problem of finding communities is long-standing and we already have access to highly effective methods
of finding communities, such as the Louvain (Blondel et al., 2008) and Leiden (Traag et al., 2019) algorithms, they
cannot directly help us distinguish which network parameters govern the emergence of community structure and how
the communities change over time.
As such, we wish to propose a new network model featuring a community structure with a focus on the flexibility
and interpretability of the underlying parameters. Our model can be applied to any network with either exogenous or
algorithmically found communities, as long as they promote associative connections; that is, we require that citations
are more likely to happen between two works from the same community. Also, while our model is derived on the
∗Corresponding author
Email addresses: lukasz.brzozowski@pw.edu.pl (Ł. Brzozowski); marek.gagolewski@pw.edu.pl (M. Gagolewski);
grzegorz.siudem@pw.edu.pl (G. Siudem); zogala@ibspan.waw.pl (B. Żogała-Siudem)
URL: https://www.gagolewski.com (M. Gagolewski); http://if.pw.edu.pl/~siudem (G. Siudem)
ORCID(s): 0000-0002-3625-3312 (Ł. Brzozowski); 0000-0003-0637-6028 (M. Gagolewski); 0000-0002-9391-6477 (G. Siudem);
0000-0002-2869-7300 (B. Żogała-Siudem)
Brzozowski, Gagolewski, Siudem, Żogała-Siudem: Preprint; Last updated on 24 February 2026
Page 1 of 21
arXiv:2510.13392v2  [physics.soc-ph]  23 Feb 2026

The Price–Pareto growth model of networks with community structure
ground of paper-to-paper citation networks, we also consider its applications to, e.g., author-to-author networks. To
formulate our model concisely and keep the number of parameters reasonable, we formulate our proposition as a min-
imal analytical extension of an existing 3DSI model (Siudem et al., 2020) which we describe below. Our generalisation
is motivated by the necessity to model the heterogeneity inherent in scientific landscapes. Existing research indicates
significant differences between how various scientific disciplines (represented here as communities or clusters) grow,
characterised by distinct growth ratios, average reference list lengths, and preferential citing tendencies (Cascarina,
2023; Harzing, 2010; Simkin and Roychowdhury, 2007). A single global parameter set cannot capture these local dy-
namics; for instance, a citation in a fast-moving field like Artificial Intelligence has different dynamical characteristics
than one in Classical Logic.
Continuing, we shortly describe the core areas in literature related to our model: the foundational models of citation
network science, the role of communities in networks, and key modern approaches to citation network modelling.
Foundational and citation-specific growth models. The earliest attempts to explain the scale-free nature of cita-
tion distributions focused on the “rich-get-richer” phenomenon. Price’s model of cumulative advantage (Price, 1965)
was among the first to formalise preferential attachment, a concept later generalised by the Barabási–Albert model (Al-
bert and Barabási, 2002), which highlighted the ubiquity of power-law distributions in complex networks. However,
simple preferential attachment inevitably leads to a strong bias towards older nodes. To address this, fitness-based mod-
els were introduced, such as the Bianconi–Barabási model (Bianconi and Barabási, 2001), which assigns an intrinsic
“fitness” to nodes to explain how younger papers can overtake older ones (e.g., “sleeping beauties”). More recently,
specific attention has been paid to the temporal dynamics of citations. Models proposed by Medo et al. (2011) and
Golosovsky (2017) explicitly incorporate mechanisms for node relevance decay, demonstrating that the probability of
receiving a citation must diminish over time to match empirical observations. This aligns with bibliometric studies on
“attention decay” (Parolo et al., 2015) and the long-term impact of scientific works (Wang et al., 2013), which show
that citation rates follow a rise-and-fall pattern not fully captured by standard scale-free models.
Modelling communities and structure. While growth models focus on temporal dynamics, a parallel stream of
research focuses on the modular structure of networks. The Stochastic Block Model (SBM) (Holland et al., 1983)
serves as the generative baseline for networks with latent group structures. Unlike growth models, SBMs are typically
static, but they offer rigorous connections between model parameters and structural properties; notably, Decelle et al.
(2011) identified precise phase transitions in SBMs that dictate when community structure becomes theoretically de-
tectable. Other approaches for generating clustered networks include the LFR Benchmark (Lancichinetti et al., 2008)
and GSCALER (Zhang and Tay, 2016). While these tools are invaluable for benchmarking community detection al-
gorithms, they are designed primarily to reproduce static structural features (e.g., degree distributions and community
sizes) rather than to model the process of network growth via citation dynamics. Topic models, such as Latent Dirichlet
Allocation (LDA) (Blei et al., 2003) and the Relational Topic Model (RTM) (Chang and Blei, 2009), bridge this gap by
representing papers as vectors of topic proportions and predicting links based on the similarity of these distributions.
However, these approaches often lack the analytical simplicity of pure random graph models. Notably, Drobyshevskiy
and Turdakov (2019) published a comprehensive survey including eight random graph models capable of generating
networks with a community structure, yet they found that none allowed for community structure under the preferential
attachment rule. This highlights a critical gap in analytical models that simultaneously capture the temporal growth of
citation networks and their heterogeneous community structure.
Recent approaches to citation network modelling. Many modern approaches generalise the previously mentioned
core models or focus on data-driven generation of new graphs. Here we can mention Graph Neural Networks (Kipf
and Welling, 2017) or Graph Variational Autoencoders (Li et al., 2020). However, these models often lack statistical
precision and elegance and are based on heuristic assumptions. Another approach gaining popularity is comprised
of Exponential Random Graph Models (ERGMs), which can be viewed as generalisations of SBMs (Fronczak et al.,
2013). Using a statistical framework, they define a probability distribution over the space of all possible graphs of
a certain size. While highly efficient in testing hypotheses on the networks, they still require computational-heavy
fitting to real data. On the other end of the spectrum are models such as the 3DSI (three dimensions of scientific
impact) model (Siudem et al., 2020); see Section 2.1. It generalises the standard procedure of iterative preferential
gains of the Barabási–Albert and Price models by adding an additional component of accidental attachments. The
name comes from the model’s ability to describe citation records using only three parameters: productivity, total
Brzozowski, Gagolewski, Siudem, Żogała-Siudem: Preprint; Last updated on 24 February 2026
Page 2 of 21

The Price–Pareto growth model of networks with community structure
impact, and how lucky an author has been so far. It is easy to fit to the data and offer valuable analytical insight into
the data, but in its standard formulation it does not allow communities in the data.
We thus lack analytical tools for modelling the growth of the citation networks with communities. There are
analytical models for simpler networks (BA, Price, 3DSI) and technically complex models suitable for communities
(GNNs, GVAs; see also Tian et al., 2023), but these on the other hand offer no theoretical insight and require black-box
explanations. In the current contribution, we would like to offer a solution to these issues: our proposal, which we set
forth in Section 2, is a generalisation of the 3DSI model which distinguishes between two types of citations: accidental,
which are purely random, and preferential, utilising the rich-get-richer scheme. While the 3DSI model was shown to
fit quite well to some real networks (Siudem et al., 2022), it is based on the assumption of relative homogeneity of
the papers in general, and as such is not ideal for modelling networks with local variability, such as networks with
a community structure.
We prove some theoretical results regarding, amongst others, the Gini index of the node degree distribution, as
well as some asymptotic properties, such as the limiting distribution’s being Paretian (Section 2.4). In Section 3, we
demonstrate the new model’s usefulness in describing real-world citation networks. Section 4 concludes the paper.
2. New model
2.1. Homogeneous Price–Pareto model
Here are the basic assumptions behind the standard 3DSI citation network growth presented in (Siudem et al.,
2020).
• In each iteration, a new publication is added to an existing citation network.
• The new work distributes 𝑚references among the nodes already in the network, such that for some parameter 𝜌:
– (1 −𝜌)𝑚citations are allocated uniformly at random,
– after that, 𝜌𝑚citations are allocated based on preferential attachment, i.e., nodes are selected with probab-
ilities proportional to their degrees.
• The above procedure can be repeated indefinitely or until a desired number of vertices has been created.
Siudem et al. (2022) showed that the approximate degree 𝑑(𝑡)(𝓁) of a node 𝓁at time 𝑡follows the recurrence
relation:
𝑑(𝑡)(𝓁)
⏟⏟⏟
the degree of node 𝓁
in turn 𝑡
=
𝑑(𝑡−1)(𝓁)
⏟⏞⏟⏞⏟
the degree of node 𝓁
in turn 𝑡−1
+
(𝑡)
Acc(𝓁)
⏟⏟⏟
accidental citation gain
+ 𝜌𝑚𝑑(𝑡−1)(𝓁) + Acc(𝑡)(𝓁)
(𝑡−1)𝑚+ (1 −𝜌)𝑚
⏟⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏟⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏟
preferential citation gain
.
We can instantly calculate Acc(𝑡)(𝓁) = (1−𝜌)𝑚
𝑡
as the number of citations added accidentally divided equally by all
𝑡nodes present at time 𝑡(note 𝑡and not 𝑡−1 since 3DSI allows loops). This formula, with the starting condition
𝑑(𝓁)(𝓁) = 0, resolves to an analytical equation:
𝑑(𝑡)(𝓁) = 𝑚(1 −𝜌)
𝜌
(Γ(𝓁−𝜌)Γ(𝑡+ 1)
Γ(𝓁)Γ(𝑡+ 1 −𝜌) −1
)
.
(1)
Conceptually, 3DSI is similar to the Price (1965) power-law-type model. However, in the latter, the preferential
citation gain of node 𝓁is proportional to 𝑑(𝑡)
𝑖(𝓁)+𝐶for some constant 𝐶. On the other hand, the key assumption behind
the 3DSI model is that in each turn, first the accidental citations are added, and only then the preferential ones. Thanks
to this simplification, the constant 𝐶is not necessary, since after the accidental distribution of citations the expected in-
degree of each article is non-zero. From an analytical perspective, this is a notable improvement over Price’s approach,
because the constant 𝐶was generally difficult to both estimate and interpret (Milojević, 2020). Moreover, as we will
mention below, asymptotically, 3DSI enjoys convergence to a Pareto type II distribution. To account for its standing
on the shoulders of giants, we will also be referring to 3DSI as the Price–Pareto model.
Brzozowski, Gagolewski, Siudem, Żogała-Siudem: Preprint; Last updated on 24 February 2026
Page 3 of 21

The Price–Pareto growth model of networks with community structure
2.2. Introducing community structure
Even though the original model was empirically shown to fit well to some existing citation networks on a large
portion of the domain, its standard formulation does not naturally allow for the emergence of communities, especially
not ones with a priori ground-truth information, which is particularly useful in community detection tasks. Therefore,
we propose to extend it in the following way:
1. In each iteration, a new node is assigned the community 𝑖with probability 𝑝𝑖, such that there are 𝑘communities
in total and ∑𝑘
𝑖=1 𝑝𝑖= 1.
2. Both parameters 𝑚and 𝜌are now community-specific: they depend on the cluster the new node belongs to; the
𝑖-th cluster has its own 𝑚𝑖and 𝜌𝑖, respectively.
3. When allocating accidental edges, the citation-receiving paper is selected uniformly at random from the whole
network. Preferential edges are drawn only from the vertices from the same community as the new node. The
loops are no longer allowed.
Such an algorithm naturally extends the standard 3DSI formulation based on empirically observed phenomena:
• papers from different scientific domains tend to cite papers from own domains in different ratios; see, e.g.,
(Cascarina, 2023) and (Harzing, 2010),
• different domains gain articles with different rates; see (Olejniczak et al., 2022),
• papers from various domains have varying average reference lists’ lengths; see (Dai et al., 2021).
Moreover, time is now considered locally, i.e., with respect to the current size of a selected community 𝑖. Since
the communities are drawn randomly, we expect that the community 𝑖grows by one paper at a time when the total
network grows by approximately 1
𝑝𝑖papers.
Notation. In the following derivations, let 𝑡denote the discrete local time step in the 𝑖-th community (𝑡𝑖suppressing
the subscript), corresponding directly to the number of vertices currently assigned to that community. Let 𝑑(𝑡)
𝑖(𝓁)
denote the in-degree of a vertex 𝓁belonging to community 𝑖at local time 𝑡. Finally, let Acc(𝑡)
𝑖(𝓁) denote the expected
accidental gain accumulated by vertex 𝓁in community 𝑖during the interval between local time steps 𝑡−1 and 𝑡. In
the derivations, we frequently make use of the fact that the vertex identifier corresponds to its entry time.
Iterative formula. We can formulate a general recurrence relation:
𝑑(𝑡)
𝑖(𝓁)
⏟⏟⏟
the in-degree of node 𝓁in cluster 𝑖
in (local) turn 𝑡
=
𝑑(𝑡−1)
𝑖
(𝓁)
⏟⏞⏟⏞⏟
the in-degree
in the previous turn
+
Acc (𝑡)
𝑖(𝓁)
⏟⏞⏞⏟⏞⏞⏟
accidental citation gain
+ 𝜌𝑖𝑚𝑖
𝑑(𝑡−1)
𝑖
(𝓁) + Acc(𝑡)
𝑖(𝓁)
∑𝑡−1
𝑟=1
[
𝑑(𝑡−1)
𝑖
(𝑟) + Acc(𝑡−1)
𝑖
(𝑟)
]
⏟⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏟⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏞⏟
preferential citation gain
.
(2)
To calculate Acc(𝑡)
𝑖(𝓁), we make a few observations:
1. At the local turn 𝑡−1, we know that there are exactly 𝑡−1 vertices in the community 𝑖. Unfortunately, we do not
know the exact size of the whole network: let us temporarily denote it with 𝑋. Note that 𝑋represents the total
number of turns it took to sample exactly 𝑡−1 vertices from the class 𝑖with probability 𝑝𝑖. We can thus model
𝑋as coming from the negative binomial1 distribution 𝑋∼NegBin(𝑟= 𝑡−1, 𝑝= 𝑝𝑖), i.e., the probability mass
function of 𝑋is given by the formula:
ℙ(𝑋= 𝑥) =
(
𝑥−1
𝑥−𝑟
)
(1 −𝑝)𝑥−𝑟𝑝𝑟.
1There are notational differences for the negative binomial distribution in the literature. We use the version where 𝑋represents the total number
of trials required for 𝑡−1 successes, which implies that the support of 𝑋is [𝑡−1, ∞) ∩ℕ.
Brzozowski, Gagolewski, Siudem, Żogała-Siudem: Preprint; Last updated on 24 February 2026
Page 4 of 21

The Price–Pareto growth model of networks with community structure
2. Since the network is growing, we consider the accidental gain for the node 𝓁at each of the global turns 𝑋+ 𝑠
for some 𝑠≥0. The variable 𝑠increases as long as we do not draw a new vertex from the community 𝑖. So
(1 −𝑝𝑖)𝑠−1 is the probability that the number of global steps between the local time 𝑡−1 and 𝑡is equal to at least
𝑠.
3. Since the community probabilities are independent of 𝑋and 𝑡, we can write that the expected accidental gain
of the vertex 𝓁in the global turn 𝑋+ 𝑠is equal to:
𝑘
∑
𝑗=1
𝑝𝑗
𝑚𝑗(1 −𝜌𝑗)
𝑋+ 𝑠
= ⟨𝑚⟩−⟨𝜌𝑚⟩
𝑋+ 𝑠
,
where ⟨𝑚⟩= ∑𝑘
𝑗=1 𝑝𝑗𝑚𝑗and ⟨𝜌𝑚⟩= ∑𝑘
𝑗=1 𝑝𝑗𝑚𝑗𝜌𝑗. Note that ⟨𝑚⟩−⟨𝜌𝑚⟩is a weighted average number of
accidental citations gained. For brevity, we further denote it by ⟨𝑎⟩∶= ⟨𝑚⟩−⟨𝜌𝑚⟩.
4. What follows is that the total expected accidental gain of the node 𝓁in the local turn 𝑡−1 is equal to:
Acc (𝑡)
𝑖(𝓁) = 𝔼𝑋
[ ∞
∑
𝑠=0
(1 −𝑝𝑖)𝑠⟨𝑎⟩
𝑋+ 𝑠
]
= ⟨𝑎⟩
∞
∑
𝑠=0
(1 −𝑝𝑖)𝑠𝔼𝑋
[
1
𝑋+ 𝑠
]
.
5. From the properties of the Beta function 𝐵, we have that for positive 𝑋+ 𝑠:
𝐵(1, 𝑋+ 𝑠) =
1
𝑋+ 𝑠= ∫
1
0
𝑢𝑋+𝑠−1𝑑𝑢,
we apply Fubini’s theorem and transform:
Acc (𝑡)
𝑖(𝓁) = ⟨𝑎⟩
∞
∑
𝑠=0
(1 −𝑝𝑖)𝑠
∫
1
0
𝔼𝑋
[𝑢𝑋+𝑠−1] 𝑑𝑢=
= ⟨𝑎⟩∫
1
0
∞
∑
𝑠=0
(1 −𝑝𝑖)𝑠𝑢𝑠𝔼𝑋
[𝑢𝑋−1] 𝑑𝑢=
= ⟨𝑎⟩∫
1
0
𝔼𝑋
[𝑢𝑋−1]
1 −(1 −𝑝𝑖)𝑢𝑑𝑢.
(3)
6. Since 𝑋follows the negative binomial distribution, we can use the formula for the probability generating function
of 𝑋as:
𝔼𝑋
[𝑢𝑋] =
(
𝑝𝑖𝑢
(1 −(1 −𝑝𝑖)𝑢)
)𝑡−1
⟹𝔼𝑋
[𝑢𝑋−1] =
𝑝𝑡−1
𝑖
𝑢𝑡−2
(1 −(1 −𝑝𝑖)𝑢)𝑡−1 ,
and thus:
Acc (𝑡)
𝑖(𝓁) = ⟨𝑎⟩∫
1
0
𝑝𝑡−1
𝑖
𝑢𝑡−2
(1 −(1 −𝑝𝑖)𝑢)𝑡𝑑𝑢=
= ⟨𝑎⟩
𝑝𝑡−1
𝑖
(1 −𝑝𝑖)𝑡−1 ∫
1−𝑝𝑖
0
𝑧𝑡−2
(1 −𝑧)𝑡𝑑𝑧=
= ⟨𝑎⟩∫
1−𝑝𝑖
𝑝𝑖
0
𝑦𝑡−2𝑑𝑦=
= ⟨𝑎⟩
𝑡−1.
(4)
Brzozowski, Gagolewski, Siudem, Żogała-Siudem: Preprint; Last updated on 24 February 2026
Page 5 of 21

The Price–Pareto growth model of networks with community structure
100
101
102
103
104
100
101
102
103
104
In-degree
mi = 2,
i = 0.8, pi = 0.33
mi = 5,
i = 0.8, pi = 0.33
mi = 9,
i = 0.8, pi = 0.33
100
101
102
103
104
Node rank
mi = 5,
i = 0.2, pi = 0.33
mi = 5,
i = 0.5, pi = 0.33
mi = 5,
i = 0.9, pi = 0.33
100
101
102
103
104
mi = 5,
i = 0.8, pi = 0.1
mi = 5,
i = 0.8, pi = 0.3
mi = 5,
i = 0.8, pi = 0.6
Example model-predicted degree sequences in a graph with 3 communities
Figure 1: Example model-predicted node in-degree sequences for communities in a graph with 𝑁= 30,000 nodes and
three communities
Before applying Formula (4) to Equation (2), let us also note that the total in-degree sum of cluster 𝑖after the local
turn 𝑡, denoted by Σ(𝑡)
𝑖, approximately follows:
Σ(𝑡)
𝑖
≈Σ(𝑡−1)
𝑖
+ 𝜌𝑖𝑚𝑖+
𝑡−1
∑
𝑟=1
(𝑡)
Acc
𝑖(𝑟) = Σ(𝑡−1)
𝑖
+ 𝜌𝑖𝑚𝑖+ ⟨𝑎⟩= (⟨𝑎⟩+ 𝜌𝑖𝑚𝑖)(𝑡−1),
(5)
where we assume Σ(1)
𝑖
= 0, which is natural as it disallows self-loops in the graph. Finally, applying both results to
Equation (2), we get:
𝑑(𝑡)
𝑖(𝓁) = 𝑑(𝑡−1)
𝑖
(𝓁) + ⟨𝑎⟩
𝑡−1 + 𝜌𝑖𝑚𝑖
𝑑(𝑡−1)
𝑖
(𝓁) + ⟨𝑎⟩
𝑡−1
∑𝑡−1
𝑟=1
[
𝑑(𝑡−1)
𝑖
(𝑟) + ⟨𝑎⟩
𝑡−1
] =
=
[
𝑑(𝑡−1)
𝑖
(𝓁) + ⟨𝑎⟩
𝑡−1
] [
1 +
𝜌𝑖𝑚𝑖
[⟨𝑎⟩+ 𝜌𝑖𝑚𝑖
] (𝑡−2) + ⟨𝑎⟩
]
=
=
[
𝑑(𝑡−1)
𝑖
(𝓁) + ⟨𝑎⟩
𝑡−1
]
𝑡−1
𝑡−1 −𝜈𝑖
,
where we introduce 𝜈𝑖as:
𝜈𝑖= 1 −
⟨𝑎⟩
⟨𝑎⟩+ 𝜌𝑖𝑚𝑖
=
𝜌𝑖𝑚𝑖
⟨𝑎⟩+ 𝜌𝑖𝑚𝑖
.
(6)
In the standard version of 3DSI, we have 𝜌= 𝜌𝑚
𝑚=
𝜌𝑚
(1−𝜌)𝑚+𝜌𝑚. As such, 𝜈𝑖can be considered an “effective” version of
𝜌from the original model. Assuming that 𝑝𝑖∈(0, 1), 𝜌𝑖∈(0, 1), 𝑘> 0, and 𝑚𝑖> 0, we have that 𝜈𝑖∈(0, 1).
Closed-form formula. Solving the recurrence using the telescopic rule, similarly to the solution presented in (Siudem
et al., 2020), and setting the starting condition 𝑑(𝓁)
𝑖
(𝓁) = 0, we obtain:
𝑑(𝑡)
𝑖(𝓁) = ⟨𝑎⟩
𝜈𝑖
[Γ(𝓁−𝜈𝑖)
Γ(𝓁)
Γ(𝑡)
Γ(𝑡−𝜈𝑖) −1
]
.
(7)
Sum of in-degrees. We can check that the in-degrees have the correct sum:
𝑡∑
𝓁=1
𝑑(𝑡)
𝑖(𝓁) = ⟨𝑎⟩
𝜈𝑖
(
−𝑡+
𝑡∑
𝓁=1
Γ(𝑡)Γ(𝓁−𝜈𝑖)
Γ(𝓁)Γ(𝑡−𝜈𝑖)
)
=
Brzozowski, Gagolewski, Siudem, Żogała-Siudem: Preprint; Last updated on 24 February 2026
Page 6 of 21

The Price–Pareto growth model of networks with community structure
= ⟨𝑎⟩
𝜈𝑖
(
−𝑡+ 𝑡−𝜈𝑖
1 −𝜈𝑖
)
Eq.(6)
=
(⟨𝑎⟩+ 𝜌𝑖𝑚𝑖
) (𝑡−1).
This confirms that the assumption (5) remains satisfied during the network growth.
It is tempting to try convert the formula (7) to a formula of a node in-degree in the global sequence. The degree of
the vertex 𝓁, aside from its community probability 𝑝𝑖, depends also on both the number of vertices from the same cluster
that precede it and succeed it in the global sequence. Combining with the fact that the values of 𝜈𝑖are not independent
between clusters, unfortunately, we found no simple analytical representation of the global degree sequence in this
model.
Figure 1 presents the node in-degrees output by our model for a graph with three communities on 30,000 vertices.
We observe that modifying different parameters has impact on different aspects of the final sequence: higher 𝑚𝑖mostly
impacts the overall slope of the sequence, 𝜌𝑖impacts the curvature of the degree sequence the most, while 𝑝𝑖changes
the amplitude of the sequence as it directly represents the number of vertices in the community.
2.3. Gini index
Noting that the above in-degrees are sorted decreasingly, we can also obtain the Gini coefficient of the vertex
degrees in the 𝑖-th cluster in local time 𝑡, denoted by (𝑡)
𝑖:
(𝑡)
𝑖
=
1
(𝑡−1)Σ(𝑡)
𝑖
𝑡∑
𝓁=1
(𝑡−2𝓁+ 1)𝑑(𝑡)
𝑖(𝓁) =
=
1
(𝑡−1)Σ(𝑡)
𝑖
⟨𝑎⟩
𝜈𝑖
[
(𝑡+ 1)
𝑡∑
𝓁=1
Γ(𝑡)Γ(𝓁−𝜈𝑖)
Γ(𝓁)Γ(𝑡−𝜈𝑖) −2
𝑡∑
𝓁=1
𝓁Γ(𝑡)Γ(𝓁−𝜈𝑖)
Γ(𝓁)Γ(𝑡−𝜈𝑖)
]
=
=
1
(𝑡−1)Σ(𝑡)
𝑖
⟨𝑎⟩
𝜈𝑖
[
(𝑡+ 1) 𝑡−𝜈𝑖
1 −𝜈𝑖
−2(𝑡−𝜈𝑖)(−𝜈𝑖𝑡+ 𝑡+ 1)
(1 −𝜈𝑖)(2 −𝜈𝑖)
]
=
= ⟨𝑎⟩
Σ(𝑡)
𝑖
𝑡−𝜈𝑖
(1 −𝜈𝑖)(2 −𝜈𝑖) = 𝑡−𝜈𝑖
𝑡−1
1
2 −𝜈𝑖
,
(8)
where the last equality follows by applying Equation (5). Of course, for large 𝑡, (𝑡)
𝑖
≈
1
2−𝜈𝑖.
As with the global degree sequence, finding the Gini coefficient of the whole sequence is difficult due to the mixture
nature of the modelled sample. We provide clean asymptotic results though, which we derive in the next section.
2.4. Asymptotic results: Price meets Pareto
We can consider the theoretical formulae asymptotically for 𝑡→∞, as both network sizes and community sizes
are often sufficiently big. Following (Siudem et al., 2022), we consider the inverse of the survival function:
𝑆−1
𝑖(𝑥) = lim
𝑡→∞𝑑(𝑡)
𝑖(𝑦𝑡) = lim
𝑡→∞
⟨𝑎⟩
𝜈𝑖
[Γ(𝑡) Γ(𝑦𝑡−𝜈𝑖)
Γ(𝑦𝑡) Γ(𝑡−𝜈𝑖) −1
]
,
(9)
where 𝑦∈[0, 1]. Since 𝜈𝑖∈(0, 1) ⟹1 −𝜈𝑖∈(0, 1), from Gautschi’s inequality (Gautschi, 1959) we have:
(
𝑡−1
𝑦𝑡
)𝜈𝑖
< Γ((𝑡−1) + 1) Γ((𝑦𝑡−1) + (1 −𝜈𝑖))
Γ((𝑡−1) + (1 −𝜈𝑖)) Γ((𝑦𝑡−1) + 1) <
(
𝑡
𝑦𝑡−1
)𝜈𝑖
.
Since the limit of both the lower and the upper bounds as 𝑡→∞is equal to 𝑦−𝜈𝑖, we get:
𝑆−1
𝑖(𝑥) = ⟨𝑎⟩
𝜈𝑖
(𝑦−𝜈𝑖(𝑥) −1) ,
𝑆𝑖(𝑥) =
( 𝜈𝑖
⟨𝑎⟩𝑥+ 1
) −1
𝜈𝑖.
Brzozowski, Gagolewski, Siudem, Żogała-Siudem: Preprint; Last updated on 24 February 2026
Page 7 of 21

The Price–Pareto growth model of networks with community structure
Note that 𝐹𝑖(𝑥) ∶= 1 −𝑆𝑖(𝑥) may be considered the CDF of the in-degree distribution in cluster 𝑖for sufficiently large
𝑡. We obtain that the density of the degree distribution can thus be modelled as:
𝑓𝑖(𝑥) = 𝑑𝐹𝑖(𝑥)
𝑑𝑥
= 1
⟨𝑎⟩
(
1 + 𝜈𝑖
⟨𝑎⟩𝑥
)−1−1
𝜈𝑖,
which is the Pareto type II (Lomax) distribution (Arnold, 2015) with parameters 𝛼= 1
𝜈𝑖and 𝜆= ⟨𝑎⟩
𝜈𝑖; compare (Bertoli-
Barsotti et al., 2024) for a similar result regarding the standard 3DSI model.
As a side note, from this it directly follows that the asymptotic expected degree exists if 𝑚𝑖𝜌𝑖𝑝𝑖> 0 ⟹𝜈𝑖> 0;
then 𝔼(𝑋)𝑋∼𝑓𝑖=
⟨𝑎⟩
1−𝜈𝑖. Indeed:
lim
𝑡→∞
𝑡∑
𝓁=1
1
𝑡𝑑(𝑡)(𝓁)
Eq.(5)
=
lim
𝑡→∞
𝑡−1
𝑡
(⟨𝑎⟩+ 𝜌𝑖𝑚𝑖
) = ⟨𝑎⟩+ 𝜌𝑖𝑚𝑖=
⟨𝑎⟩
1 −𝜈𝑖
=∶𝜇𝑖.
Overall Gini index. Since each paper comes from a cluster 𝑖with probability 𝑝𝑖, we have that the in-degree of a
randomly selected paper comes from a mixture distribution 𝐹(𝑥) = ∑𝑘
𝑗=1 𝑝𝑖𝐹𝑖(𝑥). Without loss of generality, assume
that for all 𝑖≤𝑗, 𝜈𝑖≤𝜈𝑗. By (Dorfman, 1979), this allows us to approximate the Gini coefficient of the whole degree
sequence:
=
1
⟨𝜇⟩∫
∞
0
𝑆(𝑥)(1 −𝑆(𝑥))𝑑𝑥=
(10)
=
1
⟨𝜇⟩
𝑘
∑
𝑖=1
𝑝𝑖∫
∞
0
𝑆𝑖(𝑥)𝑑𝑥−1
⟨𝜇⟩
𝑘
∑
𝑖,𝑗=1
𝑝𝑖𝑝𝑗∫
∞
0
𝑆𝑖(𝑥)𝑆𝑗(𝑥)𝑑𝑥,
(11)
where ⟨𝜇⟩= ∑𝑘
𝑖=1 𝑝𝑖𝜇𝑖. Let us also denote:
𝐴𝑖∶= ⟨𝑎⟩
𝜈𝑖
.
Then 𝑆𝑖(𝑥) =
(
𝑥
𝐴𝑖+ 1
) −1
𝜈𝑖= 𝐴
1
𝜈𝑖
𝑖(𝑥+ 𝐴𝑖)
−1
𝜈𝑖and from our assumptions follow that 1
𝜈𝑖> 1, 𝐴𝑖> 0. We directly obtain:
∫
∞
0
𝑆𝑖(𝑥)𝑑𝑥= 𝐴
1
𝜈𝑖
𝑖∫
∞
0
(𝑥+ 𝐴𝑖)
−1
𝜈𝑖𝑑𝑥= 𝐴
1
𝜈𝑖
𝑖
𝐴
1−1
𝜈𝑖
𝑖
𝜈𝑖
1 −𝜈𝑖
= 𝐴𝑖𝜈𝑖
1 −𝜈𝑖
=
⟨𝑎⟩
1 −𝜈𝑖
= 𝜇𝑖,
(12)
and
𝑅𝑖,𝑗∶= ∫
∞
0
𝑆𝑖(𝑥)𝑆𝑗(𝑥)𝑑𝑥= 𝐴
1
𝜈𝑖
𝑖𝐴
1
𝜈𝑗
𝑗∫
∞
0
(𝑥+ 𝐴𝑖)
−1
𝜈𝑖(𝑥+ 𝐴𝑗)
−1
𝜈𝑗𝑑𝑥.
(13)
Following, e.g., Formula 3.197.1 from (Gradshteyn and Ryzhik, 2007) we get:
𝑅𝑖,𝑗= 𝐴
1
𝜈𝑖
𝑖𝐴
1
𝜈𝑗
𝑗𝐴
−1
𝜈𝑖
𝑖𝐴
1−1
𝜈𝑗
𝑗
𝐵
(
1, 1
𝜈𝑖
+ 1
𝜈𝑗
−1
)
2𝐹1
(
1
𝜈𝑖
, 1; 1
𝜈𝑖
+ 1
𝜈𝑗
; 1 −
𝐴𝑗
𝐴𝑖
)
= 𝐴𝑗
𝜈𝑖𝜈𝑗
𝜈𝑖+ 𝜈𝑗−𝜈𝑖𝜈𝑗
2𝐹1
(
1
𝜈𝑖
, 1; 1
𝜈𝑖
+ 1
𝜈𝑗
; 1 −𝜈𝑖
𝜈𝑗
)
,
(14)
where 𝐵(𝑥, 𝑦) is the Beta function and 2𝐹1(𝑎, 𝑏; 𝑐; 𝑧) is the hypergeometric function. Note that we use the assumption
that 𝜈𝑖≤𝜈𝑗to make sure the hypergeometric series is convergent due to 1 −𝜈𝑖
𝜈𝑗< 1. For 𝑖= 𝑗, the hypergeometric
function simplifies to:
𝑅𝑖,𝑖= 𝐴𝑖
𝜈2
𝑖
2𝜈𝑖−𝜈2
𝑖
2𝐹1
(
1
𝜈𝑖
, 1; 2
𝜈𝑖
; 0
)
= 𝐴𝑖𝜈𝑖
2 −𝜈𝑖
=
⟨𝑎⟩
2 −𝜈𝑖
,
Brzozowski, Gagolewski, Siudem, Żogała-Siudem: Preprint; Last updated on 24 February 2026
Page 8 of 21

The Price–Pareto growth model of networks with community structure
which is also consistent with the formula used to evaluate Equation (12) if we applied it to ∫∞
0
𝑆2
𝑖(𝑥)𝑑𝑥. We could
also further approximate the hypergeometric function:
2𝐹1
(
1
𝜈𝑖
, 1; 1
𝜈𝑖
+ 1
𝜈𝑗
; 1 −𝜈𝑖
𝜈𝑗
)
=
∞
∑
𝑛=0
Γ( 1
𝜈𝑖+ 𝑛)Γ( 1
𝜈𝑖+ 1
𝜈𝑗)
Γ( 1
𝜈𝑖)Γ( 1
𝜈𝑖+ 1
𝜈𝑗+ 𝑛)
(𝜈𝑗−𝜈𝑖
𝜈𝑗
)𝑛
≈
∞
∑
𝑛=0
1
𝜈𝑛
𝑖
(
1
𝜈𝑖
+ 1
𝜈𝑗
)−𝑛(𝜈𝑗−𝜈𝑖
𝜈𝑗
)𝑛
,
(15)
where the approximation comes from taking the first terms of the Stirling approximation of the factorial. Tidying up
the terms and applying the formula for the sum of the geometric series, we find:
2𝐹1
(
1
𝜈𝑖
, 1; 1
𝜈𝑖
+ 1
𝜈𝑗
; 1 −𝜈𝑖
𝜈𝑗
)
≈
𝜈𝑖+ 𝜈𝑗
2𝜈𝑖
.
(16)
Finally, we can check that the expected in-degree is correct:
⟨𝜇⟩=
𝑘
∑
𝑖=1
𝑝𝑖𝜇𝑖= ⟨𝑎⟩
𝑘
∑
𝑖=1
1
1 −𝜈𝑖
= ⟨𝑎⟩
𝑘
∑
𝑖=1
⟨𝑎⟩+ 𝜌𝑖𝑚𝑖
⟨𝑎⟩
= ⟨𝑚⟩.
(17)
Overall, combining Equations (10)-(17) allows for a simpler representation of the Gini coefficient of the whole sample:
= 1 −
1
⟨𝑚⟩
𝑘
∑
𝑖,𝑗=1
𝑝𝑖𝑝𝑗𝑅𝑖,𝑗= 1 −⟨𝑎⟩
⟨𝑚⟩
𝑘
∑
𝑖,𝑗=1
𝑝𝑖𝑝𝑗
𝜈𝑖
𝜈𝑖+ 𝜈𝑗−𝜈𝑖𝜈𝑗
2𝐹1
(
1
𝜈𝑖
, 1; 1
𝜈𝑖
+ 1
𝜈𝑗
; 1 −𝜈𝑖
𝜈𝑗
)
≈1 −⟨𝑎⟩
⟨𝑚⟩
𝑘
∑
𝑖,𝑗=1
𝑝𝑖𝑝𝑗
𝜈𝑖+ 𝜈𝑗
2(𝜈𝑖+ 𝜈𝑗−𝜈𝑖𝜈𝑗).
(18)
Numerical tests conducted on a battery of samples with various sets of parameters and 10,000 ≤𝑁≤20,000 indicate
that the difference between the Gini coefficient value calculated with the exact formula and with the approximation
almost never exceeds 0.02 and that on average the difference is very close to 0. While (Siudem et al., 2022) also
presents clean derivation of the order statistics for the standard 3DSI degree sequence, we have found that introducing
the community mixture makes the resulting formulae unsimplifiable (though they can be represented using, i.a., the
Lauriciella generalised hypergeometric functions). As such, we omit this derivation here.
3. Experiments
3.1. Datasets and data curation
We fit our model to two well-established datasets. First, we utilise the Cora dataset (Sen et al., 2008), a benchmark
in machine learning research consisting of 2,708 scientific papers classified into seven distinct sub-disciplines (e.g.,
Neural Networks, Genetic Algorithms). This dataset represents a standard paper-to-paper citation network where edges
are directed citations. It is widely used as a benchmark dataset in tasks such as node classification.
Second, we analyse the DBLP v14 dataset (Tang et al., 2008), a comprehensive bibliographic database of computer
science publications. We use the fourteenth edition as it contains field-of-study information, which we use as the source
for ground-truth communities. To study an author-to-author topology, we projected the paper-to-paper graph into a
simple directed graph where nodes represent paper authors. Specifically, a directed edge is created from author 𝑢to
author 𝑣if author 𝑢has written a paper that cites any paper written by author 𝑣. To adhere to our model’s assumptions
(simple directed graph), we flattened the resulting multigraph by treating multiple citations between the same pair of
authors as a single unweighted edge and removed self-loops (self-citations). The ground-truth community of each
author was determined by weighted majority vote: the author is assigned to the community corresponding to the
discipline with the highest total weight over all the papers of this author, where the weight was extracted from the
field-of-study information in the data. The motivation for the transformation we performed on DBLP is two-fold: first,
it allows us to reduce the noise in ground-truth community labels that were assigned automatically; second, it allows
us to test our model on an author-to-author network instead of a standard paper-to-paper network.
Brzozowski, Gagolewski, Siudem, Żogała-Siudem: Preprint; Last updated on 24 February 2026
Page 9 of 21

The Price–Pareto growth model of networks with community structure
Table 1
General information about the analysed real networks
Dataset
Number of nodes
Number of edges
Number of communities
Average in-/out-degree
CORA
2,708
5,429
7
2.005
DBLP V14 Authors
481,387
58,544,370
8
121.616
3.2. Estimating network parameters
To fit our model to a real network given as an unweighted directed graph, we can estimate the parameters in a
straightforward manner from the graph’s adjacency matrix. After computing:
1. Σ𝑖– the sum of in-degrees in the cluster 𝑖,
2. Ψ𝑖– the sum of the out-degrees in the cluster 𝑖,
3. 𝑁𝑖– the number of vertices in the cluster 𝑖,
4. 𝑖– the Gini coefficient of the in-degree sequence in the cluster 𝑖,
5. 𝑁= ∑𝑘
𝑖=1 𝑁𝑖– the total number of papers,
we obtain:
̂𝑚𝑖=
Ψ𝑖
𝑁𝑖−1,
̂𝑝𝑖= 𝑁𝑖
𝑁
̂𝜌𝑖= Σ𝑖(2𝑖+ 𝑁𝑖−2𝑖𝑁𝑖)
Ψ𝑖(𝑖+ 1 −𝑖𝑁𝑖)
,
(19)
and the last equation follows from solving Equation (8) for 𝜌𝑖:
𝑖= 1 −
(𝑁𝑖−2)⟨𝑎⟩
(𝑡−1)(𝑚𝑖𝜌𝑖+ 2⟨𝑎⟩) ⟹𝜌𝑖= ⟨𝑎⟩(2𝑖+ 𝑁−2𝑖𝑁𝑖)
(𝑖−1)𝑚𝑖(𝑁𝑖−1)
.
From Equation (5), we have that ⟨𝑎⟩≈
Σ𝑖
𝑁𝑖−1 −𝜌𝑖𝑚𝑖, so substituting:
𝜌𝑖=
(
Σ𝑖
𝑁𝑖−1 −𝜌𝑖𝑚𝑖
) (2𝑖+ 𝑁−2𝑖𝑁𝑖)
(𝑖−1)𝑚𝑖(𝑁𝑖−1) ⟹𝜌𝑖=
Σ𝑖(2𝑖+ 𝑁𝑖−2𝑖𝑁𝑖)
𝑚𝑖(𝑁𝑖−1)(1 + 𝑖−𝑖𝑁𝑖).
Finally, by substituting 𝑚𝑖≈̂𝑚𝑖=
Ψ𝑖
𝑁𝑖−1, we obtain Formula (19).
Aside from Formula (19), there are also other ways to estimate 𝜌𝑖in real networks if we assume that they follow
our theoretical model. Below we present a few other possibilities.
Intra-cluster edges. If we have access to the full network, we can calculate the total number of the intra-cluster
citations in each community 𝑖, denoted by Ψ𝑖,𝑖(i.e., the sum of citations having both source and target in the community
𝑖). Note that each node, when it appears, gives out 𝜌𝑖𝑚𝑖preferential citations in intra-cluster edges and (1 −𝜌𝑖)𝑚𝑖𝑝𝑖
accidental intra-cluster citations. This yields:
Ψ𝑖,𝑖≈(𝑁𝑖−1) (𝜌𝑖𝑚𝑖+ (1 −𝜌𝑖)𝑚𝑖𝑝𝑖
) ⟹̂𝜌𝑖=
Ψ𝑖,𝑖
𝑁𝑖−1 −̂𝑚𝑖̂𝑝𝑖
̂𝑚𝑖(1 −̂𝑝𝑖)
=
𝑁Ψ𝑖,𝑖−𝑁𝑖Ψ𝑖
(𝑁−𝑁𝑖)Ψ𝑖
.
(20)
In-degree sum equation. Note that we can combine Equation (5) for all clusters to obtain a system of linear equations
to be solved with respect to the vector 𝐫= [𝜌1, 𝜌2, … , 𝜌𝑖]. Assuming 𝐀= (𝛼𝑖,𝑗)𝑘×𝑘and 𝐛= (𝑏𝑖)𝑘, we get:
𝐀𝐫𝑇= 𝐛,
where:
𝛼𝑖,𝑗=
{
−𝑝𝑗𝑚𝑗
𝑗≠𝑖,
(1 −𝑝𝑗)𝑚𝑗
𝑗= 𝑖,
Brzozowski, Gagolewski, Siudem, Żogała-Siudem: Preprint; Last updated on 24 February 2026
Page 10 of 21

The Price–Pareto growth model of networks with community structure
   
 
 
 
 
 
 

 

 

 

 

   	


   
 
 
 
 

 

 

 

   
   
 
 
 
 
 

 

 

 

   	
   
 
 
 
 

 

 

 

  
	
   
 
 
 

 

 

 

  


   
 
 
 
 

 

 

 

   
   
 
 
 
 

 

 

 

  

   
 
 
 
 
 

 

 

 

  

   
 
 
 
 
 
 

 

 

 

 

  
 	

 	



 	
	
 	
	
Figure 2: Complementary cumulative distribution functions of the observed and modelled in-degree sequences in the seven
clusters of the DBLP authors dataset. Our model was fitted using Gini-based 𝜌𝑖estimators. The last plot shows the full
in-degree sequences.
and:
𝑏𝑖=
Σ(𝑡)
𝑖
𝑡−1 −⟨𝑚⟩.
The matrix 𝐀is singular with rank at most 𝑘−1 since the average in-degree is also the average out-degree. After
plugging-in the estimates for 𝑚𝑖, 𝑡, we get:
𝐫=
Σ(𝑡)
𝑖−⟨𝑚⟩(𝑁𝑖−1)
Ψ𝑖
+ 𝑥
(𝑁1 −1
Ψ1
, 𝑁2 −1
Ψ2
, … , 𝑁𝑘−1
Ψ𝑘
)𝑇
,
(21)
Brzozowski, Gagolewski, Siudem, Żogała-Siudem: Preprint; Last updated on 24 February 2026
Page 11 of 21

The Price–Pareto growth model of networks with community structure
100
101
10
2
10
1
100
Case_Based
Observed
Theoretical
100
101
102
10
2
10
1
100
Genetic_Algorithms
100
101
102
10
3
10
2
10
1
100
Neural_Networks
100
101
102
10
2
10
1
100
Probabilistic_Methods
100
101
102
10
2
10
1
100
Reinforcement_Learning
100
101
10
2
10
1
100
Rule_Learning
100
101
102
10
2
10
1
100
Theory
100
101
102
10
3
10
2
10
1
100
Full Network
Observed
Estimated (Aggregated)
Standard 3DSI
In-Degree + 1 (d)
Fraction of nodes with in-degree 
 d
Cora - CCDF comparison
Figure 3: Complementary cumulative distribution functions of the observed and modelled in-degree sequences in the seven
clusters of the Cora dataset. Our model was fitted using Gini-based 𝜌𝑖estimators. The last plot shows the full in-degree
sequences.
where the first term is the same regardless of the chosen 𝑖, and 𝑥∈ℝis a free parameter. To ensure that each 0 < 𝜌𝑖< 1,
we need to have:
𝑥∈
(
max
𝑖
(−𝑏𝑖
) , min
𝑖
(𝑚𝑖−𝑏𝑖
))
There is a number of ways to choose 𝑥in the estimation: we could select a community and require any of the previous
estimates (Equations (19) and (20)) to hold for that community. Alternatively, we could fit 𝑥to the data numerically.
Our qualitative analysis showed that estimators (20) and (21), while analytically interesting, are subpar to the
estimator from Formula (19). As such we omit them from further study. However, in Appendix A, we will also
consider numerical minimisation of the mean squared log loss.
3.3. In-degree fit with exogenous communities
Figures 2 and 3 present the observed and modelled complementary cumulative distribution functions in the com-
munities of the real networks. We estimated all values from our predicted degree sequence for 𝜌𝑖values obtained using
estimator (19). First, looking at Figure 3, we observe that all our modelled densities fit well to the observed degree
sequences. Our model fits especially well when describing both low- and medium-degree nodes and only overestim-
ated largest in-degree in biggest communities. The other 𝜌𝑖estimators often fitted better near distribution means but
diverged from real distributions at tails.
Similarly, as per Figure 2, our modelled densities fits well to most of the clusters with again an especially good fit
to low- and medium-degree nodes while keeping the highest degrees bounded from above. Notably, the fit is extremely
good for all but the two biggest communities. There are clusters with degree sequences that our model was not able to
capture properly, but we believe that this is to be expected from real dataset where the behaviour of the network is not
fully predictable. We should also note that our parameter estimates and degree estimates are all related to each other
through the equations. That is, we cannot improve a fit to one community (e.g., “Control theory”) without risking that
fit to another community (e.g., ”Computer science”) suffers a decline in quality. As such, the quality of the density
estimation should be considered in total for all communities simultaneously. As for fitting to the whole network,
we observe that the distribution resulting from the standard 3DSI model is almost identical to the distribution from
our model aside from the tail, which suggests that we can use the standard model to approximate the global degree
sequence. The parameters for the standard model have been estimated as weighted averages over the communities
with probabilities 𝑝𝑖as weights. Overall, the results indicate that our model fits well to real network data, with the
Brzozowski, Gagolewski, Siudem, Żogała-Siudem: Preprint; Last updated on 24 February 2026
Page 12 of 21

The Price–Pareto growth model of networks with community structure
Table 2
Estimated values of the model parameters for all communities in both networks. Parameters ̂𝜌𝑖and ̂𝑚𝑖for the full network
have been estimated as weighted averages of the community parameters and used as input parameters when fitting the
standard 3DSI model.
Cora
DBLP authors
Cluster
̂𝑚𝑖
̂𝜌𝑖
̂𝑝𝑖
𝑖
Cluster
̂𝑚𝑖
̂𝜌𝑖
̂𝑝𝑖
𝑖
Case Based
1.973
0.457
0.110
0.674
Computer network
69.39
0.629
0.030
0.753
Genetic Algorithms
2.240
0.680
0.154
0.757
Computer science
144.31
0.741
0.711
0.794
Neural Networks
1.798
0.616
0.302
0.724
Computer vision
103.58
0.810
0.050
0.793
Prob. Methods
1.946
0.534
0.157
0.679
Control theory
46.21
0.737
0.075
0.814
Reinf. Learning
2.338
0.710
0.080
0.753
Electronic engineering
35.39
0.627
0.034
0.726
Rule Learning
1.955
0.528
0.066
0.711
Math. optimisation
68.18
0.780
0.029
0.759
Theory
2.166
0.677
0.130
0.728
Mathematics
45.35
0.786
0.046
0.769
Pattern recognition
118.79
0.523
0.025
0.796
Full network
2.005
0.605
1.000
0.721
Full network
121.62
0.735
1.000
0.801
Gini-based 𝜌𝑖estimation producing the high quality results with good tail estimates. The biggest discrepancy happens
in high-degree nodes, which our model consistently overestimates. This effect may have many explanations, but in
the context of citation networks the occurrence of ageing or attention decay seems the most likely. As our model does
not take the attention decay into account, the overestimation is expected for large communities. In Appendix A, we
propose an alternative version of our model that aims to alleviate this issue. Nonetheless, the problem does not occur
for the remaining clusters.
Overall, our model offers a unique possibility to analytically analyse the in-degree sequences of any network with
the in-degrees of each community considered separately.
Table 2 gives the estimated values of the parameters of our model for both networks. We observe that there is a large
variance of ̂𝜌in a single network which confirms that different disciplines tend to cite papers with different ratios of
accidentality-to-preferentiality. Our results regarding the Cora network confirm the observations made in (Mrowinski
et al., 2022), where the authors showed that theoretical fields tend to be governed in larger part by accidental citations,
while the applied fields have higher preferentiality. This effect is not clearly visible in our results on the DBLP authors
dataset, which is likely caused by either different type of topology or large inequality in cluster sizes.
3.4. In-degree fit with communities identified by the Leiden algorithm
To confirm that our model works not only with exogenous labels, we repeat the comparison on the Cora dataset
but instead of using the ground-truth label vector, we first run the Leiden (Traag et al., 2019) algorithm to find the
communities. The algorithm is run from a random initial membership until no improvement in modularity is detected.
The CCDF comparison on the seven largest found communities, as well as the full network, can be seen in Figure 4.
We selected seven largest communities because the Leiden algorithm found many (100+) clusters, for many of which
fitting our model would be pointless due to low sample size and high noise.
Similarly to what we have seen on real data, we observe a good fit to almost all large communities, both in peaks and
tails. The ageing bias is not visible likely due to the fairly small sizes of all communities. Overall, we found no indicator
that our model should be limited to exogenous communities and seems to work correctly also with algorithmically-
detected associative communities. One note to be made is that for extremely small communities, our model cannot be
reasonably fitted, and the in-degrees corresponding to such nodes were omitted from the full network CCDF plot.
4. Conclusion
We have devised an analytical in-degree sequence model for citation networks that is a direct generalisation of the
3DSI model accounting for the community structure in the graph. We note that it exactly mimics the original 3DSI
model with no communities (𝑘= 1) assuming no loops are allowed. Overall, our model has nice analytical properties
and allows for the derivation of many exact and asymptotic results, as well as fits well to some real networks. Since
it outputs a degree sequence for each community separately, it offers unique insight not seen previously in citation
network research.
Brzozowski, Gagolewski, Siudem, Żogała-Siudem: Preprint; Last updated on 24 February 2026
Page 13 of 21

The Price–Pareto growth model of networks with community structure
100
101
102
10
2
10
1
100
Community 1 (n=263)
Observed
Theoretical
100
101
102
10
2
10
1
100
Community 2 (n=194)
100
101
102
10
2
10
1
100
Community 3 (n=189)
100
101
10
2
10
1
100
Community 4 (n=172)
100
101
10
2
10
1
100
Community 5 (n=167)
100
101
102
10
2
10
1
100
Community 6 (n=157)
100
101
10
2
10
1
100
Community 7 (n=148)
100
101
102
10
3
10
2
10
1
100
Full Network
Estimated (Refined)
Observed
Standard 3DSI
In-Degree + 1 (d)
Fraction of nodes with in-degree 
 d
Cora with labels assigned by Leiden - CCDF comparison
Figure 4: Complementary cumulative distribution functions of the observed and modelled in-degree sequences in the seven
largest clusters of the Cora dataset with Leiden-assigned labels. Our model was fitted using Gini-based 𝜌𝑖estimators. The
last plot shows the full in-degree sequences.
Limitations. As our results indicate, the model fits best to communities that are too young to develop a noticeable
ageing or attention decay effect. This directly follows from the fact that our model, developed as the minimal analytical
extension of the 3DSI model, has no attention decay parameter and thus is not well suited to modelling networks where
the attention decay is prominent. To this end, in Appendix A, we propose a variant of our model that includes ageing;
while analytically appealing, it unfortunately requires numerical estimation of its parameters. We leave exhaustive
examination of its properties as future work. However, the comparison with the decay-equipped version of the model
suggests that overcompensation for ageing with increased accidental gain is not present, that is, the estimated values
of 1 −𝜌𝑖are not inflated.
Another limitation is that our model inherently relies on the community assignments that promote intra-cluster
connection but discourage inter-cluster ones. This is expected in citation networks where communities represent sci-
entific domains, but requires careful consideration in other types of networks. This requirement also disqualifies our
model from modelling in-degrees in, e.g., dissociative networks.
Notably, our proposition allows only uniformly distributed citations between communities. While intuitively this
assumption may be too strong, as preferential attachment likely happens also between communities, we rely on the
accidental terms to capture these relationships in order to reduce the number of parameters of the model. It is possible
to derive a similar proposition with a separate preferentiality parameter for each pair of communities, but we have
decided otherwise to keep the number of parameters linear with respect to 𝑘. Relaxing this assumption to allow for
preferential attachment between arbitrary pairs of communities would require estimating a 𝑘×𝑘matrix of preferentiality
parameters, akin to the SBM model. This would lead to a quadratic explosion in the number of parameters, making
the model prone to overfitting and difficult to interpret.
Future work. We will focus our future works on devising an algorithmic framework for generating benchmark graphs
that can be used for community detection, as we believe that our model will be complementary to approaches like
SBM or LFR in that it allows for flexible modification of the in-degree sequences inside the communities, allowing for
modelling broad families of networks. It would also be beneficial to consider further generalisations of our model in
which accidental edges are also distributed non-homogeneously, or in which the parameter values depend on the size
of the network as recent research indicates that interdisciplinary citations trends change non-randomly in time (Rong
et al., 2025).
Brzozowski, Gagolewski, Siudem, Żogała-Siudem: Preprint; Last updated on 24 February 2026
Page 14 of 21

The Price–Pareto growth model of networks with community structure
Overall, we believe that our current model proposition is both useful for modelling citation networks as well as
offers a new baseline from which to generate even more refined approaches.
Conflict of interest
The authors certify that they have no affiliations with or involvement in any organisation or entity with any financial
interest or non-financial interest in the subject matter or materials discussed in this manuscript.
CRediT authorship contribution statement
Łukasz Brzozowski: Conceptualisation of this study, Methodology, Investigation, Formal Analysis, Visualisation,
Software, Writing. Marek Gagolewski: Conceptualisation of this study, Methodology, Investigation, Writing, Super-
vision. Grzegorz Siudem: Conceptualisation of this study, Methodology, Investigation, Formal Analysis, Writing.
Barbara Żogała-Siudem: Data Curation, Investigation, Software.
A. Exponential decay
Let us introduce an alternative formulation of the above model that not only captures the information about the
communities, but also assumes exponential attention decay (or ageing) of the nodes. This proposal is directly motivated
by the fact that the ageing phenomenon is frequently observed in citation networks and that, as we have seen in the main
part of the article, fitting the proposed model to larger communities often suffers from overestimating the degrees of
oldest nodes. We assume that both preferential and accidental attractiveness of articles decay exponentially in time and
we offer the following explanation: the age is a natural limiting factor for the attractiveness of a research work. Thus,
even though the number of citations may be large, its attractiveness will diminish: this is the decay in the preferential
term. On the other hand, less popular articles not only gain smaller number of citations preferentially, but due to
decreased interest they are less frequent in, for example, search engine results, and are less likely to be cited “out of
luck”: this is the decay in the accidental term. For the sake of simplicity and for analytical tractability, we assume the
same decay parameter for both types of citations and all communities.
A.1. Preliminary derivation
To formulate the decaying model, we shall first propose an alternative derivation of our non-decaying model based
on the following postulates.
1. Preferential growth is linear in expectation, i.e., the expected (multiplicative) growth of a vertex in-degree
between times 𝑠and 𝑡is the ratio of the total numbers citations at times 𝑠and 𝑡. For example, if we assume
only preferential growth of the in-degree of vertex 𝓁between times 𝑠and 𝑡, we have in expectation:
𝑑(𝑡)(𝓁) = Σ(𝑡)
Σ(𝑠) 𝑑(𝑠)(𝓁),
where Σ(𝑠) and Σ(𝑡) are the total citation numbers at times 𝑠and 𝑡.
2. The expected total number of citations gained by community 𝑖in local turn 𝑡is composed of two elements:
community-independent expected accidental gain ⟨𝑎⟩, which does not depend on the community (see Eq. (4)),
and community-dependent preferential gain 𝜌𝑖𝑚𝑖.
3. Assuming all citations are distributed uniformly between the end of the previous turn and the end of the current
turn and that all accidental citations precede all preferential citations (the standard 3DSI assumption), it implies
that in turn 𝑡:
(a) first, between local moments 𝑡−1 and 𝑡−1 +
⟨𝑎⟩
⟨𝑎⟩+𝜌𝑖𝑚𝑖, all ⟨𝑎⟩accidental citations are added,
(b) in the remaining time interval from 𝑡−1 +
⟨𝑎⟩
⟨𝑎⟩+𝜌𝑖𝑚𝑖to 𝑡, all 𝜌𝑖𝑚𝑖preferential citations are added.
Note that this derivation gives a new interpretation to 𝜈𝑖=
𝜌𝑖𝑚𝑖
⟨𝑎⟩+𝜌𝑖𝑚𝑖. We can treat 1 −𝜈𝑖as the moment in
time between the end of turn 𝑡−1 and the end of turn 𝑡when all accidental citations have been added and all
preferential citations remain.
Brzozowski, Gagolewski, Siudem, Żogała-Siudem: Preprint; Last updated on 24 February 2026
Page 15 of 21

The Price–Pareto growth model of networks with community structure
4. Following the previous points, we model the growth of the node 𝓁in community 𝑖as a two-step process: additive
accidental citation gain and multiplicative preferential citation gain. We thus obtain:
𝑑(𝑡)
𝑖(𝓁) =
(
𝑑(𝑡−1)
𝑖
(𝓁) + ⟨𝑎⟩
𝑡−1
)
⋅
Σ(𝑡)
𝑖
Σ(𝑡−1+1−𝜈𝑖)
𝑖
=
(
𝑑(𝑡−1)
𝑖
(𝓁) + ⟨𝑎⟩
𝑡−1
)
𝑡−1
𝑡−1 −𝜈𝑖
,
which corresponds exactly to the derivation preceding Formula (6).
The above derivation of the standard model allows us to skip calculating preferential gain of individual vertices, as
well as exact values of Σ(𝑡)
𝑖, Σ(𝑡−𝜈𝑖)
𝑖
as long as we can calculate their ratio, which will be useful for composing the
recurrence involving decay. More importantly, it allows us to consider the state of the model only at three moments in
time: 𝑡−1, 𝑡−1 + 1 −𝜈𝑖= 𝑡−𝜈𝑖, and 𝑡.
A.2. Decaying model
We assume the same accidental and preferential citation gain as in the non-decaying model, but now the “value”
or “mass” of citations taken into account when calculating probabilities is not linearly proportional to the numbers of
citations, because we now assume that the citations diminish in the value exponentially over time. We introduce the
following notation:
• 𝑏(𝑡)
𝑖(𝓁) – in-degree of vertex 𝓁form community 𝑖at local time 𝑡in the decaying scenario,
• 𝑞– decay parameter such that 0 < 𝑞≤1; in each turn, existing citations diminish in value times 𝑞,
• 𝑄(𝑡)
𝑖
– total mass of citations in cluster 𝑖after the local turn 𝑡.
For simplicity, we assume that all accidental citations are added exactly at time 𝑡−𝜈𝑖in turn 𝑡. Since the initial mass
added in each local turn to community 𝑖is, without change, ⟨𝑎⟩+ 𝜌𝑖𝑚𝑖, and all citations decay with parameter 𝑞, we
have that the total mass satisfies the recurrence:
𝑄(𝑡)
𝑖
= 𝑞𝑄(𝑡−1)
𝑖
+ ⟨𝑎⟩𝑞𝜈𝑖+ 𝜌𝑖𝑚𝑖.
As before, 𝑄(1)
𝑖
= 0. The term 𝑞𝜈𝑖comes from the fact that between adding accidental edges and the end of the turn,
𝜈𝑖time units elapsed. From this we naturally obtain 𝑄(𝑡)
𝑖
= (⟨𝑎⟩𝑞𝜈𝑖+ 𝜌𝑖𝑚𝑖
) [𝑡−1]𝑞, where we the 𝑞-number is defined
as [𝑛]𝑞= 1−𝑞𝑛
1−𝑞. Please note, however, that since the masses do not grow linearly, the “switch” between accidental and
preferential edges does not necessarily happen at
⟨𝑎⟩
⟨𝑎⟩+𝜌𝑖𝑚𝑖. We derive this new 𝜈𝑖from the fact that 𝑄(𝑡−𝜈𝑖)
𝑖
∼[𝑡−1−𝜈𝑖]𝑞,
which leads to:
[1 −𝜈𝑖]𝑞
[𝜈𝑖]𝑞
= ⟨𝑎⟩
𝜌𝑖𝑚𝑖
⟹𝜈𝑖= log𝑞
(
⟨𝑎⟩−𝜌𝑖𝑚𝑖+
√
(⟨𝑎⟩−𝜌𝑖𝑚𝑖)2 + 4⟨𝑎⟩𝜌𝑖𝑚𝑖𝑞
2⟨𝑎⟩
)
.
We do not change the notation for 𝜈𝑖, because we only generalised the previous value. Namely, lim𝑞→1 𝜈𝑖=
𝜌𝑖𝑚𝑖
⟨𝑎⟩+𝜌𝑖𝑚𝑖.
While deriving the accidental gain in the decaying model of node 𝓁requires considering global time, we approximate
it with its local age. This approach allows us to relate article’s attractiveness only to its age compared to research in
the same domain; otherwise, the model would quickly diminish the impact of potentially important papers from slowly
growing scientific areas. As such, we assume that the accidental gain of a node 𝓁is proportional to its weight decaying
with age and inversely proportional to the sum of all weights in the same community. We thus write:
(𝑡)
qAcc
𝑖
(𝓁) = ⟨𝑎⟩𝑞𝑡−1−𝑙
[𝑡−1]𝑞
for the accidental decaying gain of node 𝓁in turn 𝑡in community 𝑖. Gathering all these components together, we
formulate the recurrence relation:
𝑏(𝑡)
𝑖(𝓁) =
(
𝑏(𝑡−1)
𝑖
(𝓁)𝑞1−𝜈𝑖+
(𝑡)
qAcc
𝑖
(𝓁)
)
𝑄(𝑡)
𝑖
𝑄(𝑡−𝜈𝑖)
𝑖
=
(
𝑏(𝑡−1)
𝑖
(𝓁)𝑞1−𝜈𝑖+ ⟨𝑎⟩𝑞𝑡−1−𝑙
[𝑡−1]𝑞
)
[𝑡−1]𝑞
[𝑡−1 −𝜈𝑖]𝑞
.
Brzozowski, Gagolewski, Siudem, Żogała-Siudem: Preprint; Last updated on 24 February 2026
Page 16 of 21

The Price–Pareto growth model of networks with community structure
100
101
102
103
104
100
101
102
103
104
In-degree
Varying m (q = 0.9999)
Dashed: q = 1 for reference
mi = 2,
i = 0.8, pi = 0.33
mi = 5,
i = 0.8, pi = 0.33
mi = 9,
i = 0.8, pi = 0.33
100
101
102
103
104
Node rank
Varying  (q = 0.9997)
Dashed: q = 1 for reference
mi = 5,
i = 0.2, pi = 0.33
mi = 5,
i = 0.5, pi = 0.33
mi = 5,
i = 0.9, pi = 0.33
100
101
102
103
104
Varying p (q = 0.995)
Dashed: q = 1 for reference
mi = 5,
i = 0.8, pi = 0.1
mi = 5,
i = 0.8, pi = 0.3
mi = 5,
i = 0.8, pi = 0.6
Example model-predicted degree sequences using the decaying model
Figure 5: Decaying model-predicted in-degree sequences for the same graph as presented in Figure 1, this time with varying
𝑞.
The factor 𝑞1−𝜈𝑖comes from the fact that if we assume all accidental citations are added at moment 𝑡−𝜈𝑖, the previous
citations have decayed over the interval 1 −𝜈𝑖. Following a similar telescopic process for unfolding the recurrence, we
obtain the closed-form formula:
𝑏(𝑡)
𝑖(𝓁) = ⟨𝑎⟩𝑞𝑡+𝜈𝑖−𝓁−1
[𝜈𝑖]𝑞
(
𝑞𝜈𝑖(𝓁−𝑡) Γ𝑞(𝑡)Γ𝑞(𝓁−𝜈𝑖)
Γ𝑞(𝑡−𝜈𝑖)Γ𝑞(𝓁) −1
)
,
where Γ𝑞is the 𝑞-analog of the Gamma function. Naturally we have lim𝑞→1 𝑏(𝑡)
𝑖(𝓁) = 𝑑(𝑡)
𝑖(𝓁). Figure 5 presents
how varying 𝑞impacts the resulting in-degree sequence in different scenarios. Even though the analytical form of the
decaying model is visually similar to the non-decaying model, gamma q-analogs are much more difficult to handle
both analytically and numerically. The decaying model currently suffers from the following limitations.
• Most parameters need to be estimated numerically; one disadvantage of exponential decay is that the decay
parameter 𝑞will have values near 1 for all reasonably-sized networks, which makes the numerical estimation
even harder.
• The analytical form contains a number of values that either grow or diminish exponentially. This causes the
decaying model to be prone to numerical instabilities both during estimation and plotting.
• While 𝑄(𝑡)
𝑖correctly models the effective attractiveness of publications in community 𝑖, it loses its interpretability
as the number of citations gained. Specifically, unless 𝑞is carefully estimated, the model could produce in-
degree sequences that are non-monotonic with respect to age, since this model allows – and even requires –
“losing citations”.
For completeness, we show how this decaying model with numerically estimated parameters fits to the two previ-
ously considered real networks with exogenous labels in Figures 6 and 7.
For numerical parameter estimation, we minimised the mean squared logarithmic error using the L-BFGS-B al-
gorithm (Zhu et al., 1997) with 100 restarts. To level the field, we fitted the standard version of the model (ND=non-
decaying) both numerically as well as using the previously derived estimators. To resolve ambiguous optimality of
𝜌𝑖𝑚𝑖, we required 𝑚𝑖∼Σ(𝑡)
𝑖
in the non-decaying model and 𝑚𝑖∼
𝑄(𝑡)
𝑖
[𝑡−1]𝑞in the decaying model. We observe that while
the fit to the tails has mostly improved over the analytical non-decaying model, it has often happened at the cost of
worsening the fit to a single community – Mathematical Optimisation in DBLP, and Theory in Cora network, respect-
ively. These artefacts may also stem from the difficulty posed by numerically fitting the decaying model due to high
sensitivity of the 𝑞parameter. At this point, we observe limited advantage of introducing the exponential decay into
the model, albeit with proper numerical estimation it may produce better fits to the data over the non-decaying model.
We leave these potential improvements, as well as considering other decay modelling approaches, as future work.
Table 3 presents the numerically estimated parameters on both datasets in the decayed model. We observe that to
alleviate the decay, most estimates of 𝜌𝑖in the Cora network are lower than in Table 2.
Brzozowski, Gagolewski, Siudem, Żogała-Siudem: Preprint; Last updated on 24 February 2026
Page 17 of 21

The Price–Pareto growth model of networks with community structure
   
 
 
 
 
 
 

 

 

 

 

   	


   
 
 
 
 

 

 

 

   
   
 
 
 
 
 

 

 

 

   	
   
 
 
 
 

 

 

 

  
	
   
 
 
 

 

 

 

  


   
 
 
 
 

 

 

 

   
   
 
 
 
 

 

 

 

  

   
 
 
 
 
 

 

 

 

  

   
 
 
 
 
 
 

 

 

 

 

  
 	

 	



 	
	
 	
	 	
Figure 6: Complementary cumulative distribution functions of the observed and modelled in-degree sequences in the seven
clusters of the DBLP authors dataset. The numerical parameter estimation was done using L-BFGS-B with mean squared
logarithmic error loss. The last plot shows the full in-degree sequences.
Brzozowski, Gagolewski, Siudem, Żogała-Siudem: Preprint; Last updated on 24 February 2026
Page 18 of 21

The Price–Pareto growth model of networks with community structure
100
101
10
2
10
1
100
Case_Based
Observed
Analytical ND
Numerical ND
Decaying
100
101
102
10
2
10
1
100
Genetic_Algorithms
100
101
102
10
3
10
2
10
1
100
Neural_Networks
100
101
102
10
2
10
1
100
Probabilistic_Methods
100
101
102
10
2
10
1
100
Reinforcement_Learning
100
101
10
2
10
1
100
Rule_Learning
100
101
102
10
2
10
1
100
Theory
100
101
102
10
3
10
2
10
1
100
Full Network
Observed
Analytical ND
Numerical ND
Decaying
In-Degree + 1 (d)
Fraction of nodes with in-degree 
 d
Cora - CCDF Comparison (Decaying Model)
Figure 7: Complementary cumulative distribution functions of the observed and modelled in-degree sequences in the
seven clusters of the Cora dataset. The numerical parameter estimation was done using L-BFGS-B with mean squared
logarithmic error loss. The last plot shows the full in-degree sequences. The numerical non-decaying distribution overlaps
nearly everywhere with the decaying distribution.
Table 3
Estimated values of the model parameters for all communities in both networks derived from the numerically fitted decaying
model.
Cora (q=0.999999898458)
DBLP authors (q=0.999999928008)
Cluster
̂𝑚𝑖
̂𝜌𝑖
Cluster
̂𝑚𝑖
̂𝜌𝑖
Case Based
1.919
0.308
Computer network
45.206
0.822
Genetic Algorithms
2.179
0.749
Computer science
95.130
0.546
Neural Networks
1.749
0.472
Computer vision
67.503
0.896
Probabilistic Methods
1.893
0.409
Control theory
30.129
0.903
Reinforcement Learning
2.274
0.583
Electronic engineering
23.059
0.766
Rule Learning
1.902
0.395
Math. optimisation
44.415
0.906
Theory
2.107
0.405
Mathematics
29.555
0.999
Pattern recognition
77.382
0.656
Brzozowski, Gagolewski, Siudem, Żogała-Siudem: Preprint; Last updated on 24 February 2026
Page 19 of 21

The Price–Pareto growth model of networks with community structure
References
Albert, R., Barabási, A.L., 2002. Statistical mechanics of complex networks. Reviews of Modern Physics 74, 47–97. doi:10.1103/RevModPhys.
74.47.
Arnold, B.C., 2015. Pareto Distributions. 2nd ed., Chapman and Hall/CRC. doi:10.1201/b18141.
Bertoli-Barsotti, L., Gagolewski, M., Siudem, G., Żogała Siudem, B., 2024. Gini-stable Lorenz curves and their relation to the generalised Pareto
distribution. Journal of Informetrics 18, 101499. doi:10.1016/j.joi.2024.101499.
Bianconi, G., Barabási, A.L., 2001.
Competition and multiscaling in evolving networks.
Europhysics Letters 54, 436.
doi:10.1209/epl/
i2001-00260-6.
Blei, D.M., Ng, A.Y., Jordan, M.I., 2003. Latent Dirichlet allocation. Journal of Machine Learning Research 3, 993–1022.
Blondel, V.D., Guillaume, J.L., Lambiotte, R., Lefebvre, E., 2008. Fast unfolding of communities in large networks. Journal of Statistical Mechanics:
Theory and Experiment 2008, P10008. doi:10.1088/1742-5468/2008/10/P10008.
Cascarina, S.M., 2023. Self-referencing rates in biological disciplines. Frontiers in Research Metrics and Analytics 8, 1215401. doi:10.3389/
frma.2023.1215401.
Chang, J., Blei, D., 2009. Relational topic models for document networks, in: van Dyk, D., Welling, M. (Eds.), Proceedings of the Twelfth
International Conference on Artificial Intelligence and Statistics, pp. 81–88.
Chen, Y.L., Chuang, C.H., Chiu, Y.T., 2014. Community detection based on social interactions in a social network. Journal of the Association for
Information Science and Technology 65, 539–550. doi:10.1002/asi.22986.
Dai, C., Chen, Q., Wan, T., Liu, F., Gong, Y., Wang, Q., 2021. Literary runaway: Increasingly more references cited per academic research article
from 1980 to 2019. PLOS ONE 16, e0255849. doi:10.1371/journal.pone.0255849.
Decelle, A., Krzakala, F., Moore, C., Zdeborová, L., 2011. Inference and phase transitions in the detection of modules in sparse networks. Physical
Review Letters 107, 065701.
Dorfman, R., 1979. A formula for the Gini coefficient. The Review of Economics and Statistics 61, 146–149.
Drobyshevskiy, M., Turdakov, D., 2019. Random graph modeling: A survey of the concepts. ACM Computing Surveys 52, 131. doi:10.1145/
3369782.
Fortunato, S., 2010. Community detection in graphs. Physics Reports 486, 75–174. doi:10.1016/j.physrep.2009.11.002.
Fronczak, P., Fronczak, A., Bujok, M., 2013. Exponential random graph models for networks with community structure. Physical Review E 88,
032810. doi:10.1103/PhysRevE.88.032810.
Gautschi, W., 1959. Some elementary inequalities relating to the Gamma and incomplete Gamma function. Journal of Mathematics and Physics
38, 77–81. doi:10.1002/sapm195938177.
Golosovsky, M., 2017. Growing complex network of citations of scientific papers: Modeling and measurements. Physical Review E 96, 032306.
Gradshteyn, I.S., Ryzhik, I.M., 2007. 3–4 — Definite integrals of elementary functions, in: Jeffrey, A., Zwillinger, D., Gradshteyn, I., Ryzhik, I.
(Eds.), Table of Integrals, Series, and Products. 7th ed.. Academic Press, Boston, pp. 247–617. doi:10.1016/B978-0-08-047111-2.50013-3.
Harzing, A., 2010. Citation analysis across disciplines: The impact of different data sources and citation metrics. White paper, Anne-Will Harz-
ing’s site. URL: https://harzing.com/publications/white-papers/citation-analysis-across-disciplines. available online,
accessed 30/09/2025.
Holland, P.W., Laskey, K.B., Leinhardt, S., 1983. Stochastic blockmodels: First steps. Social Networks 5, 109–137. doi:10.1016/0378-8733(83)
90021-7.
Kipf, T.N., Welling, M., 2017. Semi-supervised classification with graph convolutional networks, in: 5th International Conference on Learning
Representations, ICLR 2017.
Lancichinetti, A., Fortunato, S., Radicchi, F., 2008. Benchmark graphs for testing community detection algorithms. Physical Review E 78. doi:10.
1103/physreve.78.046110.
Leskovec, J., Krevl, A., 2014. SNAP Datasets: Stanford large network dataset collection. http://snap.stanford.edu/data.
Li, J., Yu, J., Li, J., Zhang, H., Zhao, K., Rong, Y., Cheng, H., Huang, J., 2020. Dirichlet graph variational autoencoder, in: Larochelle, H., Ranzato,
M., Hadsell, R., Balcan, M., Lin, H. (Eds.), Advances in Neural Information Processing Systems, pp. 5274–5283.
Medo, M., Cimini, G., Gualdi, S., 2011. Temporal dynamics of popularity: The case of scientific papers. Physical Review Letters 107, 238701.
Milojević, S., 2025. Science of science. Scientometrics 130, 3195–3211. doi:10.1007/s11192-025-05322-1.
Milojević, S., 2020. Towards a more realistic citation model: The key role of research team sizes. Entropy 22, 875. doi:10.3390/e22080875.
Mrowinski, M.J., Gagolewski, M., Siudem, G., 2022. Accidentality in journal citation patterns. Journal of Informetrics 16, 101341. doi:10.1016/
j.joi.2022.101341.
Newman, M., 2018. Networks. Oxford University Press. doi:10.1093/oso/9780198805090.001.0001.
Olejniczak, A.J., Savage, W.E., Wheeler, R., 2022. The rhythms of scholarly publication: Suggestions to enhance bibliometric comparisons across
disciplines. Frontiers in Research Metrics and Analytics 7. doi:10.3389/frma.2022.812312.
Parolo, P.D.B., Pan, R.K., Ghosh, R., Huberman, B.A., Kaski, K., Fortunato, S., 2015. Attention decay in science. Journal of Informetrics 9,
734–745.
Price, D., 1965. Networks of scientific papers. Science 149, 510–515. doi:10.1126/science.149.3683.510.
Rong, G., Chen, Y., Ma, F., Koch, T., 2025. Exploring interdisciplinary research trends through critical years for interdisciplinary citation. Journal
of Informetrics 19, 101726. doi:10.1016/j.joi.2025.101726.
Scarselli, F., Gori, M., Tsoi, A.C., Hagenbuchner, M., Monfardini, G., 2009. The graph neural network model. IEEE Transactions on Neural
Networks 20, 61–80. doi:10.1109/TNN.2008.2005605.
Sen, P., Namata, G.M., Bilgic, M., Getoor, L., Gallagher, B., Eliassi-Rad, T., 2008. Collective classification in network data. AI Magazine 29,
93–106.
Simkin, M., Roychowdhury, V., 2007. A mathematical theory of citing. Journal of the Association for Information Science and Technology 58,
1661–1673. doi:10.1002/asi.20653.
Brzozowski, Gagolewski, Siudem, Żogała-Siudem: Preprint; Last updated on 24 February 2026
Page 20 of 21

The Price–Pareto growth model of networks with community structure
Siudem, G., Nowak, P., Gagolewski, M., 2022. Power laws, the Price model, and the Pareto type-2 distribution. Physica A: Statistical Mechanics
and its Applications 606, 128059. doi:10.1016/j.physa.2022.128059.
Siudem, G., Żogała Siudem, B., Cena, A., Gagolewski, M., 2020. Three dimensions of scientific impact. Proceedings of the National Academy of
Sciences of the United States of America (PNAS) 117, 13896–13900. doi:10.1073/pnas.2001064117.
Tang, J., Zhang, J., Yao, L., Li, J., Zhang, L., Su, Z., 2008. Arnetminer: Extraction and mining of academic social networks, in: KDD’08, pp.
990–998.
Tian, Y., Li, G., Mao, J., 2023. Predicting the evolution of scientific communities by interpretable machine learning approaches. Journal of
Informetrics 17, 101399. doi:10.1016/j.joi.2023.101399.
Traag, V., Waltman, L., van Eck, N.J., 2019. From Louvain to Leiden: Guaranteeing well-connected communities. Scientific Reports 9, 5233.
doi:10.1038/s41598-019-41695-z.
Wang, D., Song, C., Barabási, A.L., 2013. Quantifying long-term scientific impact. Science 342, 127–132.
Zhang, J.W., Tay, Y.C., 2016. GSCALER: Synthetically scaling a given graph, in: Pitoura, E., Maabout, S., Koutrika, G., Marian, A., Tanca,
L., Manolescu, I., Stefanidis, K. (Eds.), Proceedings of the 19th International Conference on Extending Database Technology, EDBT 2016,
Bordeaux, France, March 15-16, 2016, Bordeaux, France, March 15-16, 2016, pp. 53–64. doi:10.5441/002/EDBT.2016.08.
Zhu, C., Byrd, R.H., Lu, P., Nocedal, J., 1997. Algorithm 778: L-BFGS-B: Fortran subroutines for large-scale bound-constrained optimization.
ACM Transactions on Mathematical Software 23, 550–560. doi:10.1145/279232.279236.
Brzozowski, Gagolewski, Siudem, Żogała-Siudem: Preprint; Last updated on 24 February 2026
Page 21 of 21
